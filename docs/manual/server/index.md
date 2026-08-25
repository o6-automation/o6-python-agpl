# Server

This section is the complete story of `o6.Server`. This page covers the two
routes to an address space and how one API serves both synchronous and
asynchronous code. From there:

- [Lifecycle and configuration](lifecycle.md) — creating and running a
  server, and configuring it.
- [Building the address space](address-space.md) — the imperative route:
  nodes, reads and writes, methods, references, and browsing.
- [Declared types](declared-types.md) — the model-first route.
- [Implementing behaviour](behaviour.md) and
  [Server callbacks](callbacks.md) — attaching Python behaviour, and the
  exact signatures and resolution order.
- [Events, monitored items and timers](events-and-timers.md) —
  server-side notification and scheduling.
- [Access control and roles](security.md) — authentication and
  role-based access control.
- [Operations and interoperability](operations.md) — history, discovery,
  reverse connect, PubSub, and status codes.

Its sibling page, [Client](../client/index.md), covers the other half of the protocol.

!!! warning
    The Server SDK is in beta. The API described here is implemented and
    exercised, but it has not yet been through a stable release.

## Two ways to build an address space

Everything a server exposes is nodes, and `o6` gives you two routes to them.

The **imperative route** is a handful of `addX` helpers on the server object:
`addObject`, `addVariable`, `addMethod`, and friends. You call them at runtime,
each one creates exactly one node, and you get a Python node handle back. This
is the shortest path from nothing to a working server, and it is the right
choice for scripts, gateways, and address spaces whose shape is decided by
configuration rather than by a model.

The **declarative route** is an OPC UA information model written as Python
classes — `@o6.objecttype`, `@o6.variabletype`, `@o6.datatype`, and the rest —
collected in a namespace module that the server publishes with
`server.ns.append(module)`. The types then behave like classes: instantiating
one creates a complete typed subtree, and the Python class carries the
behaviour. This is the right choice whenever the address space *is* a model —
a companion specification, a product line, anything a client should be able to
discover by type.

The two mix freely: a declarative model can sit next to imperatively created
nodes in the same server, and both end up in the same nodestore.

## One API, synchronous or asynchronous

The server owns an asyncio event loop, which drives all I/O, timers, and
callbacks. How that loop is driven depends on how you created the server.

When no loop is passed and none is running, the server creates its own loop and,
on `start()`, runs it on a background daemon thread. Synchronous calls —
`server.read(...)`, `server.write(...)`, `server.addVariable(...)` — are
dispatched onto that thread and block until they complete. This is the plain
script case, and it needs no asyncio knowledge at all.

When a loop is already running (or one is passed as `loop=`), the server uses
it and spawns no thread. Calls made from a coroutine on that loop return
awaitables:

```python
import asyncio
import inspect
import o6

async def main():
    server = o6.Server(port=4840)
    variable = server.addVariable("Async", server.objectsNode, 1.0, nodeId="ns=1;s=Async")
    server.start()

    result = server.read("ns=1;s=Async")
    print(await result if inspect.isawaitable(result) else result)

    server.stop()

asyncio.run(main())
```

The `inspect.isawaitable` check in that snippet is deliberate, and it is the one
place where the server's dual-mode API is less predictable than the client's:
node creation and configuration calls resolve inline and return plain values
even on a running loop, while service-style calls (`read`, `write`, `call`,
`browse`) return awaitables. When you write code that must work in both worlds,
either await defensively as above or keep to one mode per module.

Two consequences are worth internalizing:

- Callbacks — Method calls, Variable read/write callbacks, monitored-item
  notifications, timers — all run on the server's loop thread. Blocking inside
  one blocks the whole server. Hand slow work to a queue or a thread pool.
- A `Server` is bound to one loop for its lifetime. Use one server per loop.

## Where to go next

- [Writing a Nodeset in Python](../sdk-fundamentals/namespace/writing-nodesets-in-python.md)
  — every decorator, in depth, with a complete reference model.
- [Implementing Object Behavior](../sdk-fundamentals/namespace/implementing-object-behavior.md)
  — the declare/implement/register cycle and its precedence rules.
- [Server callbacks](callbacks.md) — exact signatures and resolution
  order for Method, Variable, ObjectType, and VariableType callbacks.
- [Using Nodesets](../sdk-fundamentals/namespace/loading-and-using-nodesets.md) —
  packaged companion specifications and XML nodesets.
- [Node API](../node-api.md) — the object syntax used for every node handle here.
- [Client](../client/index.md) — the other half, for talking to the server you just
  built.
- [Performance](../performance.md) — batching, buffer sizes, and large arrays.
- [API Reference](../../api_reference) — generated signature-level reference.
