# Node API syntax

The Node API is a thin dotted/bracketed/call-syntax layer on top of the same connection. Instead of carrying `NodeId` strings around, you navigate the address space with `.` (children) and `[]` (paths), and act on a node by calling it.

This page is a quick orientation. The full tour lives in the [Node API usage](../../node-api/usage.md); this page shows the three shapes you'll use most often and the connection between them and the high-level API.

This page walks through three steps:

1. Browse with `.` and `[]`.
2. Act on a node with `()`.
3. Use the same syntax from sync and async code.

!!! info
    This tutorials requires you to know how to [create and connect](100_connect.md) a client. We assume a server is running on localhost as described in [example server](../../node-api/usage.md#setting-the-stage) in the tutorials intro.

---

## Browse with `.` and `[]`

The dot operator triggers a server-side `Browse` for the named child. Children are resolved lazily and cached:

```python
var = client.objects.DistillingSystem.Kettle.Temperature
method = client.objects.DistillingSystem.Start
```

Names are matched case-insensitively against `BrowseName`.
The result is a `Node` subclass — `VariableNode`, `ObjectNode`, `MethodNode`, … — depending on the child's `NodeClass`.

We can use `[]` in conjunction with a browse path — a `/`-separated string of `<namespace-index>:<BrowseName>` segments, per the OPC UA `RelativePath` string grammar:

```python
nodes = client.objects["/1:DistillingSystem/1:Kettle"]
```

`[]` is the right tool when a `BrowseName` is *ambiguous* — i.e. more than one child has the same name (case-insensitively).
`.` cannot pick a single target in that case; `[]` returns a list of matching targets that you disambiguate yourself. The distillery doesn't have any ambiguous names, but the mechanism is the same either way — index into the returned list:

```python
nodes = client.objects["/1:DistillingSystem/1:Kettle"]   # a list, even with one match
kettle = nodes[0]                                          # pick the target
```

!!! tip
    In a Python REPL, `dir(client.objects)` and `<TAB>` completion both run a browse and list the children — see [Node API usage](../../node-api/usage.md#interactive-completion).

#### Putting it all together

```python
from o6 import Client

with Client("opc.tcp://localhost:4840") as client:
    var = client.objects.DistillingSystem.Kettle.Temperature
    nodes = client.objects["/1:DistillingSystem/1:Kettle"]
```

---

## Act on a node with `()`

Once you have a node, the same `()` operator handles every interaction.
The distinction is by argument shape, not by method.
Reading a variable value becomes a simple call with no arguments:

```python
var = client.objects.DistillingSystem.Status.Setpoint
print(var())    # Reads Setpoint
```

Similarly writing the variable is a call with an appropriately typed argument:

```python
var(90.0)         # Writes Setpoint
```

Non-`Value` attributes are read by specifying the `o6.AttributeId` (or its string name) for the parameter `attr`:

```python
name = var(attr="BrowseName")
```

Method nodes are called the same way — pass the input arguments positionally. The parent object is picked up automatically. `Start` takes no arguments and returns just a `StatusCode`:

```python
import o6

status, = client.objects.DistillingSystem.Start()
print(status == o6.StatusCode.GOOD)
```

#### Putting it all together

```python
import o6
from o6 import Client

with Client("opc.tcp://localhost:4840") as client:
    var = client.objects.DistillingSystem.Status.Setpoint
    print(var())
    var(90.0)
    print(var())

    status, = client.objects.DistillingSystem.Start()
    print(status == o6.StatusCode.GOOD)
```

---

## Use the same syntax for sync and async code

Every node call is awaitable. Sync and async use the same expressions — add or drop `await`:

```python
import asyncio
import o6
from o6 import Client

async def main():
    async with Client("opc.tcp://localhost:4840") as client:
        # Browse
        var = await client.objects.DistillingSystem.Status.Setpoint

        # Read
        value = await var()

        # Write
        await var(90.0)

        # Call
        status, = await client.objects.DistillingSystem.Start()

        print(value, status == o6.StatusCode.GOOD)

asyncio.run(main())
```

The dotted navigation, the bracket navigation, and the call syntax are identical in both modes — only the `await` keyword changes.

---

## What's next?

- [Node API tutorial](../../node-api/usage.md) — the full reference, including interactive completion and the quick-reference table.
- [Read / write value](120_read-write-node.md) and [Call a method](130_call-method.md) — the same operations through the high-level API.
