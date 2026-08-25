# Operations & interoperability

## Historical data

Historical access needs two things, and having only the first is the usual
reason a client's `historyRead` fails.

First, the server needs a history database, configured before `start()`:

```python
server.config.setHistoryDatabase(maxNodes=10)
```

Second, each node must be historizing *and* registered with the history
gathering. `addVariable(historizing=True)` only sets the attribute and the
history access levels — a client's `historyRead` against such a node returns
`BadHistoryOperationInvalid`. Per-node registration currently has no public
API; the internal call is:

```python
level = server.addVariable("Level", plant, 0.0, nodeId="ns=1;s=Level", historizing=True)
server._register_historizing(o6.NodeId("ns=1;s=Level"), max_values=1000, max_response=200)
```

Once registered, every write is recorded and a client can read it back:

```python
history = client.historyRead("ns=1;s=Level", start, end)
for dataValue in history.dataValues:
    print(dataValue.sourceTimestamp, dataValue.value)
```

Treat `_register_historizing` as provisional: it is private, its name and
signature may change, and a public equivalent is the obvious thing to add.

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
client in one important respect: where a client hands you status codes to
inspect, the server usually raises.

**`o6.StatusCodeError`** is raised by `read` when the value's status is not
`Good`, by `write`, `addReference`, `deleteReference`, `deleteNode`, and node
construction when the operation fails, and by `call` when a Method returns a bad
status. It carries `code` and `symbol`:

```python
try:
    server.write("ns=1;s=ReadOnly", 1.0)
except o6.StatusCodeError as error:
    print(error.symbol)      # e.g. BadUserAccessDenied
```

`o6.StatusCode` is an `IntFlag`, so `o6.StatusCode.BAD in status` works, and
`status.check()` raises for anything but `Good`.

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
