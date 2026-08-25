# Raw services & errors

## The raw service interface

When the high-level call does not expose a parameter you need, drop to the
service layer. Every method takes a request object, returns the full response
object, and does no interpretation whatsoever — checking
`responseHeader.serviceResult` and the per-operation results is your job.

| Service set | Methods |
| --- | --- |
| Discovery | `serviceFindServers`, `serviceFindServersOnNetwork`, `serviceGetEndpoints` |
| NodeManagement | `serviceAddNodes`, `serviceDeleteNodes`, `serviceAddReferences`, `serviceDeleteReferences` |
| View | `serviceBrowse`, `serviceBrowseNext`, `serviceTranslateBrowsePathsToNodeIds`, `serviceRegisterNodes`, `serviceUnregisterNodes` |
| Attribute | `serviceRead`, `serviceWrite`, `serviceHistoryRead`, `serviceHistoryUpdate` |
| Method | `serviceCall` |

A raw read with both timestamps, for example:

```python
from o6.ns import ns0

rvi = ns0.datatypes.ReadValueId()
rvi.nodeId = o6.NodeId("ns=1;s=IntegerVariable")
rvi.attributeId = o6.AttributeId.VALUE

request = ns0.datatypes.ReadRequest()
request.nodesToRead = [rvi]
request.timestampsToReturn = ns0.datatypes.TimestampsToReturn.BOTH

response = client.serviceRead(request)
response.responseHeader.serviceResult.check()
dv = response.results[0]
print(dv.value, dv.sourceTimestamp, dv.serverTimestamp)
```

`RegisterNodes` is a service with no high-level equivalent and is worth knowing:
it asks the server for optimized NodeIds for nodes you will access repeatedly,
which can be a large win in polling loops.

```python
request = ns0.datatypes.RegisterNodesRequest()
request.nodesToRegister = [o6.NodeId("ns=1;s=IntegerVariable")]
registered = client.serviceRegisterNodes(request).registeredNodeIds
# ... use registered[0] for reads and writes ...
release = ns0.datatypes.UnregisterNodesRequest()
release.nodesToUnregister = list(registered)
client.serviceUnregisterNodes(release)
```

Two service sets are deliberately absent from this list. The **subscription and
monitored-item services** are driven by `Subscription` and `MonitoredItem`,
which also own the Publish loop and the callback dispatch — going around them
would leave the client's bookkeeping inconsistent, so use those objects instead.
The **Query** service set is not exposed.

Like every other method, the `serviceX` calls block in synchronous code and are
awaitable in async code. The
[Low-level service calls tutorial](../../tutorials/client/500_lowlevel-service-calls.md)
works through more examples.

## Errors and status codes

Three kinds of failure show up, and they are reported differently on purpose.

**Bad status codes** are OPC UA's normal way of saying "this operation did not
work". `o6.StatusCode` is an `IntFlag` with the full symbolic table, so it
supports bitwise tests, comparison, and `int()`:

```python
if o6.StatusCode.BAD in status:
    ...
status.check()                       # raises o6.StatusCodeError unless GOOD
status.check(message="reading the setpoint")   # adds a note to the exception
```

Where a status surfaces as an exception, it is `o6.StatusCodeError`, which
carries `code` and `symbol`. Reads of a single target raise it; writes return
it; `valueOnly=False` reads put it on the `DataValue`.

**Protocol and consistency failures** — the service itself failed, or the server
returned a different number of results than requested — raise `ValueError` or
`Exception` with the offending status code in the message. These indicate a
server or configuration problem rather than a data problem.

**Local usage errors** raise the ordinary Python exceptions you would expect:
`ValueError` for a malformed range or mismatched list lengths, `TypeError` for a
filter of the wrong kind, `KeyError` for an unknown NodeId through `client[...]`,
`AttributeError` for a missing or ambiguous child node, `RuntimeError` for
operating on a deleted subscription or item or after the loop has stopped, and
`ImportError` when `browseInteractive()` cannot find `curses`.

Client log output — reconnect attempts, dropped user token policies, ignored
index ranges — goes to the logger you passed to the constructor or to
`client.config.logger`, defaulting to the `o6.client` logger. Turning on
`logging.DEBUG` for it is the fastest way to see what the stack is doing during a
failed handshake.

## Concurrency and backpressure

A client admits at most `maxAsyncServiceCalls` application service calls at
once. The call that exceeds the ceiling does not wait — it fails immediately
with `BadTooManyOperations`. The default is `32`:

```python
import asyncio

reads = [asyncio.create_task(client.read(node_id)) for _ in range(33)]
results = await asyncio.gather(*reads, return_exceptions=True)
# 32 values, and one StatusCodeError(BAD_TOO_MANY_OPERATIONS)
```

The ceiling counts only application calls. Publish requests and internal
connection maintenance are not counted, so subscriptions do not consume the
budget. Raise it, or set `0` to remove the limit entirely:

```python
client = Client(url)
client.config.maxAsyncServiceCalls = 512   # or 0 for unlimited
await client.connect()
```

Like the rest of `client.config`, this must be set before `connect()`.

Removing the limit does not make deep concurrency free — it moves the failure
somewhere less obvious. Every open call holds its encoded request in memory,
and enough of them will run into the transport limits
(`sendBufferSize`, `localMaxChunkCount`) or into the server's own session and
per-request limits, which surface as service faults or a dropped channel.

If what you want is *wait for a slot* rather than *fail fast*, bound the
concurrency in Python rather than removing the ceiling. An `asyncio.Semaphore`
gives you that, and unlike a blocking limit it stays cancellable and composes
with `asyncio.timeout()`:

```python
sem = asyncio.Semaphore(256)

async def read(node_id):
    async with sem:
        return await client.read(node_id)
```

Keep the semaphore bound at or below `maxAsyncServiceCalls` and the client will
never reject a call for exceeding the ceiling.