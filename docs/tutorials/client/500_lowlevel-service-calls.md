# Low-level service calls

Every service the `o6` client supports has a `serviceX` method. It takes a request object and returns the response object. Use it when you need full control: set optional fields, override a default or inspect the raw response.
The high-level methods (`client.read`, `client.write`, `client.call`, `client.browse`, …) are thin wrappers over the same calls.

This page covers three steps:

- Build a request object.
- Call the corresponding `serviceX` method.
- Read fields off the response.

!!! info
    This tutorial requires you to know how to [create and connect](100_connect.md) a client and how to use the high-level API for [read / write](120_read-write-node.md) and [call](130_call-method.md). It assumes a server is running on localhost as described in [Set the Stage](../setup.md).

---

## Build a request object

Each service has a request type in `o6.ns.ns0`.
It has the same fields as the request message in the specification. Set the required fields; optional fields keep their defaults:

```python
from o6.ns.ns0.datatypes import ReadRequest, ReadValueId

req = ReadRequest()
req.nodesToRead = [ReadValueId("ns=1;i=1204")]
```

To read the `Value` attribute, pass a `NodeId` string to the `ReadValueId` constructor. Set the other fields (`attributeId=`, `indexRange=`, `dataEncoding=`) only when you need more than `Value`. Request types (`ReadRequest`, `WriteRequest`, …) take no constructor arguments. Create one with `Type()` and set its fields by attribute, as above.

---

## Call the corresponding `serviceX` method

The suffix of a `serviceX` method is the OPC UA service name.
Pass the request and receive the response:

```python
from o6 import Client

with Client("opc.tcp://localhost:4840") as client:
    response = client.serviceRead(req)
```

For the discovery and registration workflow, see the
[Discovery and registration manual](../../manual/client/discovery.md).

The client's `serviceX` methods, grouped by OPC UA service set:

- **Discovery**: `serviceFindServers`, `serviceFindServersOnNetwork`, `serviceGetEndpoints`, `serviceRegisterServer`, `serviceRegisterServer2`
- **Node management**: `serviceAddNodes`, `serviceDeleteNodes`, `serviceAddReferences`, `serviceDeleteReferences`
- **View**: `serviceBrowse`, `serviceBrowseNext`, `serviceTranslateBrowsePathsToNodeIds`, `serviceRegisterNodes`, `serviceUnregisterNodes`
- **Attribute**: `serviceRead`, `serviceHistoryRead`, `serviceWrite`, `serviceHistoryUpdate`
- **Method**: `serviceCall`

Every `serviceX` method returns a `MaybeAwaitable`, so it works in sync and async code. Add `await` in async code:

```python
async with Client("opc.tcp://localhost:4840") as client:
    response = await client.serviceRead(req)
```

---

## Read fields off the response

The response object has the fields of the response message in the specification. Read them as Python attributes:

```python
with Client("opc.tcp://localhost:4840") as client:
    req = ReadRequest()
    req.nodesToRead = [ReadValueId("ns=1;i=1204")]   # Status.Setpoint
    response = client.serviceRead(req)

    # First check the service-level result code
    print(response.responseHeader.serviceResult)   # StatusCode.GOOD

    # Then read the per-node results
    result = response.results[0]
    print(result.status)         # StatusCode.GOOD
    print(result.value)          # e.g. 90.0
```

A non-`Good` `responseHeader.serviceResult` means the whole service call failed, for example because the secure channel is in a bad state.
A non-`Good` per-node `status` means only that node failed.
The `serviceX` methods do not raise in either case. Check both codes yourself.

!!! tip
    Start with the high-level API (`client.read`, `client.write`, `client.call`, …). Use `serviceX` only when the wrapper is not enough, for example to set a header field, use an unusual parameter combination or debug a low-level status code.

---

## Next steps

| Topic | What it covers |
|---|---|
| [Read / write value](120_read-write-node.md) | Reading and writing values through the high-level API. |
| [Call a method](130_call-method.md) | Calling methods through the high-level API. |
| [The Client API reference](../../api_reference/client.md) | Full surface of every `serviceX` method. |
