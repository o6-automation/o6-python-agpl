# Node API syntax

The Node API is a thin syntax layer on the same connection. Instead of passing NodeId strings, you navigate the address space with `.` (children) and `[]` (paths) and act on a node by calling it. The manual introduces this model in [Nodes as Objects](../../manual/node-api/using-nodes.md).

This page covers:

1. Browse with `.` and `[]`.
2. Act on a node with `()`.
3. Use the same syntax from sync and async code.

!!! info
    This page assumes you can [create and connect](100_connect.md) a client and that the server from [Set the Stage](../setup.md) runs on localhost.

---

## Browse with `.` and `[]`

The dot operator runs a `Browse` on the server for the named child. Children are resolved lazily and cached:

```python
var = client.objects.DistillingSystem.Kettle.Temperature
method = client.objects.DistillingSystem.Start
```

Names are matched case-insensitively against `BrowseName`.
The result is a `Node` subclass — `VariableNode`, `ObjectNode`, `MethodNode`, … — depending on the child's `NodeClass`.

`[]` takes a browse path: a `/`-separated string of `<namespace-index>:<BrowseName>` segments in the OPC UA `RelativePath` string grammar:

```python
nodes = client.objects["/1:DistillingSystem/1:Kettle"]
```

Use `[]` when a BrowseName is *ambiguous*, meaning several children share the name (case-insensitively).
`.` cannot pick a single target then. `[]` returns a list of all matching targets; index into it to pick one. The distillery has no ambiguous names, so the list has one entry:

```python
nodes = client.objects["/1:DistillingSystem/1:Kettle"]   # a list, even with one match
kettle = nodes[0]                                          # pick the target
```

!!! tip
    In a Python REPL, `dir(client.objects)` and `<TAB>` completion both run a browse and list the children — see [Discovering children](../../manual/node-api/navigation.md#discovering-children).

#### Putting it all together

```python
from o6 import Client

with Client("opc.tcp://localhost:4840") as client:
    var = client.objects.DistillingSystem.Kettle.Temperature
    nodes = client.objects["/1:DistillingSystem/1:Kettle"]
```

---

## Act on a node with `()`

The `()` operator handles every interaction with a node; the arguments decide what it does.
A call without arguments reads the value:

```python
var = client.objects.DistillingSystem.Status.Setpoint
print(var())    # Reads Setpoint
```

A call with a value of the matching type writes it:

```python
var(90.0)         # Writes Setpoint
```

To read another attribute, pass its `o6.AttributeId` or string name as `attr`:

```python
name = var(attr="BrowseName")
```

Call a method node with its input arguments as positional arguments. The parent object is resolved automatically. `Start` takes no arguments and returns only a `StatusCode`:

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
    print(var())         # e.g. 90.0 — current Setpoint value
    var(90.0)            # write 90.0 back into Setpoint
    print(var())         # 90.0 — server echoes the just-written value

    status, = client.objects.DistillingSystem.Start()
    print(status == o6.StatusCode.GOOD)   # True
```

!!! info
    Both `print(var())` lines print the same number: the second read returns the value you wrote, which equals the current Setpoint. To see a change, write a different value such as `var(85.0)` and read again.

---

## Use the same syntax for sync and async code

Every node call is awaitable. In async code, add `await` to the same expressions:

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

---

## Next steps

| Topic | What it covers |
|---|---|
| [Node API](../../manual/node-api/index.md) | The full manual chapter, including interactive completion and the quick-reference table. |
| [Read / write value](120_read-write-node.md) | Reading and writing values through the high-level API. |
| [Call a method](130_call-method.md) | Calling methods through the high-level API. |
