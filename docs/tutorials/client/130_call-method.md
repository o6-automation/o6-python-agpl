# Calling a method

This page starts a batch on the distilling server with the `Start` method.

`client.call` invokes an OPC UA method on a server object. It takes the NodeId of the object the method belongs to, the method NodeId and a list of input arguments. It returns a tuple `(status_code, *output_arguments)`.

This page covers:

- Build the object and method NodeIds.
- Call a method and read the result.
- Handle the case where the method takes inputs.

!!! info
    Start the [example server](../setup.md) in the background. This page assumes you can [create and connect](100_connect.md) a client and [browse](110_browse.md) the address space. The NodeIds below belong to the `DistillingSystem` object at `ns=1;i=1000`.

---

## Build the object and method NodeIds

The distilling server exposes two methods on the `DistillingSystem` object at `ns=1;i=1000`:

- **`Start`** at `ns=1;i=2001` — Start a new distilling batch.
- **`Shutdown`** at `ns=1;i=2002` — Stop the current batch.

A method belongs to an object. `client.call` takes the NodeId of the parent object that owns the method and the NodeId of the method as separate arguments:

```python
parent = "ns=1;i=1000"   # DistillingSystem
method = "ns=1;i=2001"   # Start
```

Both are `o6.NodeId` strings; see [NodeIds and namespace info](430_nodeids-and-namespace-info.md) for the syntax.

---

## Call the method and read the result

For a method without outputs, `client.call` returns `(status_code,)`. Start a new batch and check the `StatusCode`:

```python
import o6

status, = client.call(parent, method)
print(status == o6.StatusCode.GOOD)
```

`o6.StatusCode.GOOD` means the server accepted the call and the method ran. A non-`Good` status means the server rejected the call before it reached the method, for example because of a bad object/method NodeId pair, a security rejection or a wrong number of arguments. `client.call` does not raise on a rejected call; it returns the `StatusCode`.

#### Putting it all together

```python
import o6
from o6 import Client

with Client("opc.tcp://localhost:4840") as client:
    parent = "ns=1;i=1000"   # DistillingSystem
    method = "ns=1;i=2001"   # Start

    status, = client.call(parent, method)
    print(status == o6.StatusCode.GOOD)
```

---

## Handle the case where the method takes inputs

Pass input arguments as a list in the third argument. A method with one input:

```python
status, greeting = client.call(parent, "ns=1;s=TestMethods.Hello", ["World"])
```

A method with several inputs takes a list of the same length, in declaration order:

```python
client.call(parent, method, [arg1, arg2, arg3])
```

If you pass too few or too many inputs, the server rejects the call with a non-`Good` status. `o6` does not type-check the inputs; it forwards them as-is and the server decides whether they match the method signature.

!!! info
    The distilling server's `Start` and `Shutdown` methods take no inputs. The snippets in this section are placeholders for methods such as `TestMethods.Hello` on other servers and do not run against the distilling server.

---

## Next steps

| Topic | What it covers |
|---|---|
| [Monitor data changes](200_monitor-datachange.md) | Push value changes from the server to a callback. |
| [Low-level service calls](500_lowlevel-service-calls.md) | Use `client.serviceCall(...)` for full control over the `Call` request. |
