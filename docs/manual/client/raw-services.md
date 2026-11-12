# Raw Services

Use raw requests when the high-level interface does not expose the operation or parameter you need.

## The raw service interface

Use the service layer when the high-level call does not expose a parameter
you need. Each method takes a request object and returns the full response
object without interpreting it. You check `responseHeader.serviceResult` and
the per-operation results, following the shared
[error-handling contract](../sdk-fundamentals/builtin/statuscode.md#errors-and-status-codes).

| Service set | Methods |
| --- | --- |
| Discovery | `serviceFindServers`, `serviceFindServersOnNetwork`, `serviceGetEndpoints`, `serviceRegisterServer`, `serviceRegisterServer2` |
| NodeManagement | `serviceAddNodes`, `serviceDeleteNodes`, `serviceAddReferences`, `serviceDeleteReferences` |
| View | `serviceBrowse`, `serviceBrowseNext`, `serviceTranslateBrowsePathsToNodeIds`, `serviceRegisterNodes`, `serviceUnregisterNodes` |
| Attribute | `serviceRead`, `serviceWrite`, `serviceHistoryRead`, `serviceHistoryUpdate` |
| Method | `serviceCall` |

The raw services decode structures only with the DataTypes the client already
has. Unlike `read()` or `call()`, they never look up an unknown DataType on the
server, so its values stay `ExtensionObject`s. See
[Unknown namespaces and structured values](../sdk-fundamentals/namespace/loading-and-using-nodesets.md#unknown-namespaces-and-structured-values).

This synchronous fragment assumes a connected `client` and an Int32 Variable
at `ns=1;s=IntegerVariable`. It requests both timestamps and checks both
status levels before consuming the value:

```python
import o6
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
dv.status.check(message="reading IntegerVariable")
print(dv.value, dv.sourceTimestamp, dv.serverTimestamp)
```

These `.check()` calls require exact `GOOD`. If your application accepts
informational Good statuses, use the
[severity check](../sdk-fundamentals/builtin/statuscode.md#good-severity-versus-exact-good)
for the DataValue instead. A Good service result alone says nothing about
the quality of this individual value.

`RegisterNodes` has no high-level equivalent. It asks the server for
optimized NodeIds for nodes you access repeatedly, which can speed up polling
loops.

```python
request = ns0.datatypes.RegisterNodesRequest()
request.nodesToRegister = [o6.NodeId("ns=1;s=IntegerVariable")]
response = client.serviceRegisterNodes(request)
response.responseHeader.serviceResult.check()
registered = response.registeredNodeIds
# ... use registered[0] for reads and writes ...
release = ns0.datatypes.UnregisterNodesRequest()
release.nodesToUnregister = list(registered)
response = client.serviceUnregisterNodes(release)
response.responseHeader.serviceResult.check()
```

Two service sets are not in the table:

- The Subscription and MonitoredItem services are driven by `Subscription`
  and `MonitoredItem`, which own the Publish loop and callback dispatch.
  Calling the services directly would leave the client's bookkeeping
  inconsistent.
- The Query service set is not exposed.

The `serviceX` calls block in synchronous code and are awaitable in async code.
The [Low-level service calls tutorial](../../tutorials/client/500_lowlevel-service-calls.md)
has more examples. For server registration, see
[Discovery and registration](discovery.md#confirmed-lds-registration).

## Concurrency and backpressure

A client admits at most `maxAsyncServiceCalls` application service calls at
once. The call that exceeds the ceiling does not wait. It fails immediately
with `BadTooManyOperations`. The default is `32`:

```python
import asyncio

reads = [asyncio.create_task(client.read(node_id)) for _ in range(33)]
results = await asyncio.gather(*reads, return_exceptions=True)
# Calls exceeding the simultaneous limit fail with BadTooManyOperations.
# How many fail depends on when earlier calls complete.
```

Publish requests and internal connection maintenance do not count, so
subscriptions do not consume the budget. Raise the ceiling, or set `0` to
remove the limit. This configuration fragment belongs before the
`async with client:` block of an async application:

```python
import o6

client = o6.Client("opc.tcp://localhost:4840")
client.config.maxAsyncServiceCalls = 512   # or 0 for unlimited
```

Removing the limit allows pending calls to consume more memory and can increase
latency when the server cannot keep up. Limits on the size of an individual
message are separate from this call budget.

To wait for a slot instead of failing fast, bound the concurrency in
Python. An `asyncio.Semaphore` stays cancellable and composes with
`asyncio.timeout()`:

```python
sem = asyncio.Semaphore(8)

async def read(node_id):
    async with sem:
        return await client.read(node_id)
```

Share this semaphore across callers. Its bound must leave room for other calls
on the same client, or those calls must use the same guard too. Keeping this
combined concurrency within `maxAsyncServiceCalls` avoids rejection by the
client's pending-call limit; a server can still reject a request for its own
reasons.
