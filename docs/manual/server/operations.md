# Operations & interoperability

## Browsing

`server.browse(target)` returns a complete flat list of
`ns0.datatypes.ReferenceDescription` objects, matching `client.browse(target)`.
Continuation points are followed until exhausted, even when a page is empty.
Synchronous code receives the list directly. Inside an async task, await the call:

```python
references = await server.browse(target)
for reference in references:
    print(reference.nodeId)
```

Both typed Node handles and NodeIds follow this contract, on the server's event
loop or a separate caller loop. Unknown or deleted targets and failed browse
results raise `o6.StatusCodeError`. Collection attempts to release outstanding
continuation points on failure. Client collection also attempts release on
cancellation; a lost connection can prevent release.

Typed-node child and attribute access return immediately in synchronous code and
on the server's own loop; async tasks on another loop await that access.

### Explicit pages and migration

Replace `server.browse(target).references` with `server.browse(target)` (or the
corresponding awaited call). Move old `server.browse(target, maxReferences=...)`
callers to `server.browsePage(target, maxReferences=...)`. Only `browsePage`
returns a `BrowseResult` with `references` and `continuationPoint` fields.
`maxReferences=0` requests no caller-imposed limit; backend limits may still
produce a continuation point.

Use `browseNext(False, token)` to continue and `browseNext(True, token)` to
release. Both return a **list of pages**, one per token; a single token still
returns a one-element list. Tokens belong to the server that issued them.
Update the token before processing each page, and release it if processing stops:

```python
page = server.browsePage(target, maxReferences=100)
token = page.continuationPoint
try:
    while True:
        for reference in page.references:
            print(reference.nodeId)
        if not token:
            break
        page = server.browseNext(False, token)[0]
        token = page.continuationPoint
finally:
    if token:
        server.browseNext(True, token)
```

Async tasks await `browsePage` and `browseNext` too. Awaiting an already returned
native `BrowseResult` itself raises `TypeError`.

`browseNext` raises `StatusCodeError` for failed page statuses. When a batch
contains a failure, it attempts to release continuation points in successful
returned pages before raising. Client applications that need explicit pages use
`serviceBrowse` and `serviceBrowseNext`; those raw services retain their response
objects and status fields, which callers must check.

## Historical data

Configure a history database before starting the server, then register each
Variable with `historizing=True` or `server.historize`:

```python
server.config.setHistoryDatabase(maxNodes=10, capacity=1000, maxResponseSize=200)
level = server.addVariable("Level", plant, 0.0, nodeId="ns=1;s=Level", historizing=True)
```

Variables created before startup register during `start()`, so the database can
be configured after creating them. Startup raises if the database is missing or
registration fails; pending registrations remain available for retry. Variables
added while running register immediately. Missing database configuration rejects
runtime creation, and failed initialization or registration removes the new node.

Writes are recorded automatically. `o6.History` configures per-node capacity and
on-write, polling, or manual sampling; `server.unhistorize(level)` stops recording.
In async code, await `server.historize(...)` and `server.unhistorize(...)`, including
when the server runs on another loop. Both require a configured history database;
failed configuration restores the node's previous history attributes.

```python
history = client.historyRead("ns=1;s=Level", start, end)
for dataValue in history.dataValues:
    print(dataValue.sourceTimestamp, dataValue.value)
```

`historyRead` follows server-issued continuation points and preserves target
order for multiple nodes. `numValuesPerNode` limits the total returned per node;
unused tokens are released when that limit is reached or a read fails or is
cancelled. A broken connection can prevent release, so stores must expire
abandoned tokens.

Custom `HistoryBackend` stores can override `getHistoryPage` to return
`(dataValues, nextToken)`. It receives the incoming token, a release flag, and
session identity in addition to the ordinary history-read parameters. Bind tokens
to the session and node, reject invalid tokens, and return `([], b"")` after
release. An empty output token finishes the read. The existing `getHistoryData`
hook remains available for stores that return the complete result in one response.

## Discovery and reverse connect

A server can register itself with a Local Discovery Server so that clients find
it through `FindServers`:

```python
server.registerDiscovery("opc.tcp://localhost:4840")
# ... serve ...
server.deregisterDiscovery("opc.tcp://localhost:4840")
```

`semaphoreFilePath=` names a semaphore file coordinating shutdown across
instances. Deregistration belongs in your shutdown path.

The two LDS-side callbacks — `setRegisterServerCallback`, invoked when another
server registers with this one, and `setServerOnNetworkCallback`, invoked when a
server is discovered via mDNS — are part of the API but **raise
`NotImplementedError` in the current build**: they depend on open62541 discovery
features that are compile-time gated. Do not build a design on them without
checking first.

In a reverse-connect deployment the server initiates the TCP connection to a
client that is listening, which is how you reach a client behind a firewall:

```python
handle = server.addReverseConnect("opc.tcp://localhost:4843")
# ... the server retries periodically until the client answers ...
server.removeReverseConnect(handle)
```

`callback=` receives `(handle, state)` on every state change. The client side is
`client.startReverseConnect(port)`, which does not return until the server has
connected — see [Client](../client/lifecycle.md#reverse-connect).

## PubSub

PubSub is configured through the standard namespace-zero information model
rather than through a separate Python API: you create `PubSubConnection`,
`WriterGroup`, `DataSetWriter`, and reader components as address-space nodes and
control them with the model's own methods. The `o6.pubsub` module adds only the
runtime facilities that model cannot express:

```python
import o6.pubsub

o6.pubsub.publish(writerGroup)                   # publish one message now
o6.pubsub.setStateMachine(component, callback)   # custom state transitions
table = o6.pubsub.offsetTable(writerGroup)       # fixed-layout byte offsets
```

`offsetTable` returns the encoded message together with typed byte offsets
(`OffsetType`), which is what makes deterministic, pre-encoded publishing
possible. `setStateMachine` takes a callable
`(current, target) -> (StatusCode, newState)` and may be called from an
implementation class's `__init__`; a component must be disabled before its state
machine is replaced. PubSub requires a build and Credential with the PubSub
feature scope enabled; without it these calls raise `PermissionError`.

## Errors and status codes

The server reports failures in three ways, and the pattern differs from the
client for some operations. Writes share the client status-return contract.

**`o6.StatusCodeError`** is raised by `read` when the value's status is not
`Good`, by `addReference`, `deleteReference`, `deleteNode`, and node
construction when the operation fails, and by `call` when a Method returns a bad
status. It carries `code` and `symbol`:

```python
try:
    server.write("ns=1;s=Missing", 1.0).check()
except o6.StatusCodeError as error:
    print(error.symbol)      # e.g. BadNodeIdUnknown
```

`o6.StatusCode` is an `IntFlag`, so `o6.StatusCode.BAD in status` works, and
`status.check()` raises for anything but `Good`. `write` returns one status per
target, attempts later targets after a per-target failure, and raises
`StatusCodeError` only for service failures. Check returned statuses when a
rejected write must stop your application. Typed-node writes keep their
exception behavior; see [write migration](address-space.md#reading-and-writing-server-side).

**Local usage errors** raise ordinary Python exceptions: `ValueError` for a
`range` on a non-Value attribute, a malformed index range, or an out-of-range
event severity; `TypeError` for a write-only Variable callback, a mismatched
`implement` combination, an ambiguous server inference, or a `@o6.call` target
that matches no Method; `KeyError` from `implement` when the type node has not
been published yet; `RuntimeError` when configuration is changed after
`start()`; and `NotImplementedError` for the discovery callbacks above.

**Callback failures** are reported to the client as status codes. Return
`(o6.StatusCode.BAD_..., )` from a Method or Variable callback to reject an
operation. An exception escaping a callback is logged rather than propagated to
the caller, so returning an explicit status is always better. Synchronous
callback dispatch also rejects recursion with `BadInvalidState`: a Variable
cannot re-enter its own read or write callback, and a Method cannot re-enter the
same Method node.

Server log output — access-control decisions, rejected security policies,
session activity — goes to the logger passed to the constructor or to
`server.config.logger`, defaulting to the `o6.server` logger. Enabling
`logging.DEBUG` on it is the fastest way to understand a refused connection.
