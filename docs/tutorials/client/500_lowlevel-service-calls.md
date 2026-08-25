# Low-level service calls

If you need full control over a request — fill in every optional field, override a default, or capture the raw response — every service the o6 client supports has a `serviceX` method that takes a pre-built request object and returns a pre-built response.
The high-level methods (`client.read`, `client.write`, `client.call`, `client.browse`, …) are thin wrappers over the same calls.

This page walks through the low-level basics:

- Build a request object.
- Call the corresponding `serviceX` method.
- Read fields off the response.

!!! info
    This tutorials requires you to know how to [create and connect](100_connect.md) a client and how to use the high-level API for [read / write](120_read-write-node.md) and [call](130_call-method.md). We assume a server is running on localhost as described in [example server](../../tutorials.md#the-example-server) in the tutorials intro.

---

## Build a request object

Each service has a paired request type that lives in `o6.ns.ns0`.
The request has the same fields as the spec's request message — required fields set, optional fields left at their defaults:

```python
from o6.ns.ns0.datatypes import ReadRequest, ReadValueId

req = ReadRequest()
req.nodesToRead = [ReadValueId("ns=1;i=1204")]
```

`ReadValueId` accepts a plain `NodeId` string directly in its constructor for the simple case of reading the `Value` attribute — you only need to build it up field-by-field (`attributeId=`, `indexRange=`, `dataEncoding=`) when you're after something other than `Value`. Request types themselves (`ReadRequest`, `WriteRequest`, …) take no constructor arguments — build one with `Type()` and set its fields by attribute, as above.

---

## Call the corresponding `serviceX` method

The suffix of a `serviceX` method is the OPC UA service name.
Pass the request, get the response back:

```python
from o6 import Client

with Client("opc.tcp://localhost:4840") as client:
    response = client.serviceRead(req)
```

The complete list of `serviceX` methods on the client mirrors the OPC UA service sets:

- **Discovery**: `serviceFindServers`, `serviceFindServersOnNetwork`, `serviceGetEndpoints`
- **Node management**: `serviceAddNodes`, `serviceDeleteNodes`, `serviceAddReferences`, `serviceDeleteReferences`
- **View**: `serviceBrowse`, `serviceBrowseNext`, `serviceTranslateBrowsePathsToNodeIds`, `serviceRegisterNodes`, `serviceUnregisterNodes`
- **Attribute**: `serviceRead`, `serviceHistoryRead`, `serviceWrite`, `serviceHistoryUpdate`
- **Method**: `serviceCall`

Every `serviceX` method returns a `MaybeAwaitable` to be readily used in both sync and async contexts — add `await` in async code:

```python
async with Client("opc.tcp://localhost:4840") as client:
    response = await client.serviceRead(req)
```

---

## Read fields off the response

The response object mirrors the spec's response message. Read the fields you care about the same way you read any Python attribute:

```python
with Client("opc.tcp://localhost:4840") as client:
    req = ReadRequest()
    req.nodesToRead = [ReadValueId("ns=1;i=1204")]   # Status.Setpoint
    response = client.serviceRead(req)

    # First check the service-level result code
    print(response.responseHeader.serviceResult)   # StatusCode.Good

    # Then read the per-node results
    result = response.results[0]
    print(result.status)         # StatusCode.Good
    print(result.value)          # e.g. 90.0
```

A non-`Good` `responseHeader.serviceResult` means the whole service call failed (e.g. the secure channel is in a bad state).
A non-`Good` per-node `status` means only that node failed.
The `serviceX` methods do *not* raise on either — they hand you the raw response and let you decide.

!!! tip
    Start with the high-level API (`client.read`, `client.write`, `client.call`, …). Drop down to `serviceX` only when you've outgrown the wrapper — typically because you need a header field, an unusual parameter combination, or to debug a low-level status code.

---

## What's next?

- [Read / write value](120_read-write-node.md) and [Call a method](130_call-method.md) — the high-level wrappers.
- [The Client API reference](../../api_reference/index.md) — full surface of every `serviceX` method.
