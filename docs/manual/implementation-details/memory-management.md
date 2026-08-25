# Memory management

o6\\Python joins two lifetime systems: Python's reference counting and cyclic
garbage collector, and open62541's explicitly managed C objects. The binding
uses one overarching rule:

!!! important
    A Python wrapper owns its native object and every Python callback registered
    through that object. Native callback tables may borrow those references, but
    must never become independent owners of Python objects.

This makes the Python `Client` or `Server` the root of its complete resource
tree. Dropping that root releases the native client or server, its event-loop
resources, callbacks, and callback contexts—even when a callback closes over
its owner.

!!! info "Prerequisites"
    The user-facing pages [Client / Lifecycle](../client/lifecycle.md) and
    [Server / Lifecycle & configuration](../server/lifecycle.md) describe
    connecting, starting, stopping, and the context managers whose mechanics
    this page spells out.

## Object lifetime

`Client` and `Server` participate in Python's cyclic garbage collector. Their
GC traversal exposes all Python references held by the C extension, including
callbacks, pending connection futures, and cached configuration wrappers.
Consequently, cycles such as the following are collectible:

```python
server = o6.Server()
server.addRepeatedCallback(lambda: server, 1000)
```

Explicit `disconnect()`, `stop()`, and context managers remain the preferred
way to release network resources at a predictable point. Garbage collection is
the safety net: it provides deterministic native cleanup once Python decides
that an unreachable object may be finalized, but applications should not rely
on when a GC collection happens.

## Ownership rules inside the binding

The C extension follows these rules consistently:

1. A Python wrapper exclusively owns its `UA_Client` or `UA_Server`.
2. The wrapper owns callbacks and callback contexts in GC-visible Python
   containers or fields.
3. Native Method, Variable, and type-lifecycle callback contexts point directly
   at GC-tracked Python state. Dispatch does not perform a global registry
   lookup. The server's GC-visible ownership list is the lifetime root.
4. Pending asynchronous Method calls are GC-tracked callback states owned by
   the server. Each state keeps its asyncio Task alive until completion or
   cancellation consumes it.
5. Every strong reference has one clearly defined release path for success,
   submission failure, cancellation, and owner teardown.
6. Native pointers borrowed by separately retained Python objects are
   invalidated before the native owner is deleted. Access afterwards raises a
   Python exception instead of dereferencing stale memory.

Server callback dispatch has no global C registry. open62541's asynchronous
operation cancellation hook supplies only the native output pointer, so the
binding resolves that pointer by scanning the owning server's GC-visible state
list. This is a lookup over the existing ownership root, not a second index or
lifetime mechanism.

An asynchronous Method state and its asyncio Task reference one another while
the operation is pending. Both are Python GC-tracked objects. Successful
completion removes the state from the server and breaks that cycle. Native
cancellation invalidates the output pointer immediately and cancels the Task;
server teardown additionally clears the borrowed server pointers before the
native server is deleted.

Per-instance lifecycle contexts are also GC-tracked Python objects. The native
node borrows its context pointer, while the server's ownership list keeps the
object alive and exposes callback/context cycles to Python's collector.

## Teardown order

Cleanup runs in a strict order:

1. Mark the object and event loop as tearing down.
2. Disable open62541 hooks that could call back into Python.
3. Cancel or detach pending asynchronous operations.
4. Remove native callback registrations while their borrowed Python references
   are still valid, but retain lifecycle-instance state.
5. Stop native event sources and detach transports.
6. Delete the `UA_Client` or `UA_Server`, allowing node destructors to consume
   their still-live lifecycle state.
7. Release the remaining GC-visible Python references.
8. Clear namespace mappings, invalidate borrowed wrapper pointers, and finally
   free the Python wrapper.

No Python object is kept at reference count zero while network shutdown
continues asynchronously. In particular, transport `connection_lost` handlers
never finalize a client. A queued transport callback may observe that its
connection manager has already been detached; in that case it is a benign
no-op.

During native client deletion, all Python-facing state, lifecycle, service,
inactivity, and global notification hooks are disabled together with their
context. open62541 may emit shutdown notifications from `UA_Client_delete`, so
clearing only the context would leave a callable hook with no valid owner.

## Event-loop connections

The connection manager owns one Python reference for each protocol stored in
its connection array. `connection_lost` releases that reference only if it
actually removes the protocol from the array. Bulk event-source shutdown
detaches every protocol, releases every array reference, resets the connection
count, and moves directly to the stopped state. Later asyncio callbacks see the
detached sentinel and do nothing.

## Configuration wrappers

`Client.config` is cached by the client and contains a borrowed pointer back to
it. Code may retain the configuration object after releasing the client, so
client teardown explicitly invalidates that pointer. Subsequent configuration
access raises `RuntimeError` rather than accessing a deleted `UA_Client`.

`ServerConfig` holds a strong reference to its server. Retaining a server
configuration therefore intentionally retains the server; the server does not
cache the configuration, so this does not form a cycle.

## Testing lifetime changes

Changes to ownership or callbacks should cover all four outcomes where
applicable: successful completion, immediate submission failure, cancellation,
and owner teardown. A callback-owning API should also have a cyclic-GC test:

```python
ref = weakref.ref(owner)
owner.callback = lambda owner=owner: owner
del owner
gc.collect()
assert ref() is None
```

Tests should exercise cleanup both explicitly and from `__del__`/cyclic GC.
They should be run with the Python test server lifecycle enabled so queued
asyncio transport callbacks execute during teardown; reference leaks and stale
native pointers frequently remain invisible in purely disconnected tests.
