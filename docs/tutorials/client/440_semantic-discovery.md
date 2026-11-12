# Semantic Discovery

NodeId literals such as `"ns=1;i=1302"` (`Kettle.Temperature`) make code brittle. If the server is rebuilt and the namespace indices shift, you must update every literal by hand. Instead, navigate the address space by `BrowseName`, as in `client.objects.DistillingSystem.Kettle.Temperature()`, and let `o6` resolve the `NodeId` at the time of the call.

This is the operation [Browse](110_browse.md) performs, exposed as a Python expression instead of a list of `ReferenceDescription`. You read, write or call the returned `Node` object with `()`. The underlying `NodeId` stays hidden.

This page covers three steps:

1. Navigate the distillery by BrowseName with `client.objects.DistillingSystem.Kettle.Temperature`.
2. Read, write, and call on the resulting `Node` with the `()` syntax.
3. Use `[]` for ambiguous BrowseNames and `dir(...)` for REPL discovery.

!!! info
    This tutorial expects the [example server running](../setup.md) in the background, and assumes you know how to [create and connect](100_connect.md) a client, how to [browse](110_browse.md) the address space, and how to [load packaged companion specs](410_load-packaged-companion-specs.md). The snippets use the distillery's `DistillingSystem` (`ns=1;i=1000`), `Kettle` (`ns=1;i=1300`), and `Status` (`ns=1;i=1200`) sub-objects as the running example.

---

## Navigate by BrowseName

Under `Objects`, the distillery has `DistillingSystem`, with the children `Kettle`, `Status`, `Identification`, `Distillate`, `Actuators` and `Events`. The `Node` API exposes that as a dotted path:

```python
from o6 import Client

with Client("opc.tcp://localhost:4840") as client:
    objects = client.objects                           # the Objects folder
    distilling = objects.DistillingSystem              # ns=1;i=1000
    kettle = distilling.Kettle                          # ns=1;i=1300
    temperature = kettle.Temperature                   # ns=1;i=1302
```

Names match `BrowseName` case-insensitively: `kettle`, `KETTLE` and `Kettle` resolve to the same child. Each `.` triggers a server-side `Browse` for the named child of the current node. The result is a `Node` subclass (`VariableNode`, `ObjectNode`, `MethodNode`, …) that matches the child's `NodeClass`.

`temperature.nodeId` holds the underlying `NodeId`, but you rarely need it. You read, write and call on the `Node` object itself.

#### Putting it all together

```python
from o6 import Client

with Client("opc.tcp://localhost:4840") as client:
    temperature = client.objects.DistillingSystem.Kettle.Temperature
    print(temperature)                # ns=client1_ns1;i=1302
    print(type(temperature).__name__) # VariableNode
```

---

## Read, write, and call on the resulting `Node`

The `()` operator handles every interaction. The arguments decide what it does.

Read a variable value with no arguments:

```python
temperature = client.objects.DistillingSystem.Kettle.Temperature
print(temperature())               # e.g. 20.0
```

Write the value with one positional argument:

```python
setpoint = client.objects.DistillingSystem.Status.Setpoint
setpoint(90.0)                     # writes the Value attribute
```

Read another attribute with the `attr=` keyword:

```python
print(temperature(attr="BrowseName"))  # "Temperature"
print(temperature(attr="NodeClass"))   # "VARIABLE"
```

Write another attribute with `value=` and `attr=`:

```python
temperature(value="KettleTemp", attr="BrowseName")
```

Call a method with `()` and pass the input arguments positionally. `o6` uses the parent object automatically:

```python
distilling = client.objects.DistillingSystem
status, = distilling.Start()       # StatusCode, then any output args
```

The first element of the returned tuple is the `StatusCode`, followed by any output arguments (see [Call a method](130_call-method.md)). The distillery's `Start` and `Shutdown` have no inputs or outputs, so the tuple has one element.

#### Putting it all together

```python
import o6
from o6 import Client

with Client("opc.tcp://localhost:4840") as client:
    # Read
    temperature = client.objects.DistillingSystem.Kettle.Temperature
    print("temperature:", temperature())

    # Write
    setpoint = client.objects.DistillingSystem.Status.Setpoint
    setpoint(90.0)

    print("browse name:", temperature(attr="BrowseName"))
    print("node class:", temperature(attr="NodeClass"))

    # Call a method
    distilling = client.objects.DistillingSystem
    status, = distilling.Start()
    print("start status:", status == o6.StatusCode.GOOD)
```

---

## Disambiguate with `[]` and explore with `dir(...)`

Two situations don't fit the dotted path:

- **Ambiguous BrowseNames.** If more than one child of the same node has the same `BrowseName` (case-insensitively), the dotted form can't pick a single target. Use `[]` with a browse path, a `/`-separated string of `<namespace-index>:<BrowseName>` segments (see [Node API syntax](140_node-api-syntax.md)). It returns all matching targets as a list. The distillery has no ambiguous names: its two `Level` variables, `Kettle.Level` (`ns=1;i=1301`) and `Distillate.Level` (`ns=1;i=1401`), sit under different parents. The mechanism is the same either way. Index into the returned list:

  ```python
  matches = client.objects.DistillingSystem["/1:Kettle/1:Level"]   # a list, even with one match
  kettle_level = matches[0]                                        # pick the target
  print(kettle_level())
  ```

- **REPL discovery.** `dir(node)` runs a `Browse` and returns the child names. With `<TAB>` completion, this gives you the interactive browser from [Browse](110_browse.md) inside a Python REPL:

  ```python
  >>> dir(client.objects.DistillingSystem)
  ['identification', 'status', 'kettle', 'distillate', 'actuators', 'events', 'start', 'shutdown']
  ```

  The first `dir(...)` fetches the list. Later `dir()` calls use the cached list and make no server request.

!!! tip
    To explore an unknown server, use `dir(...)` and `<TAB>` completion in a Python REPL, then write the dotted path.

#### Putting it all together

```python
from o6 import Client

with Client("opc.tcp://localhost:4840") as client:
    # Browse path navigation via []
    matches = client.objects.DistillingSystem["/1:Kettle/1:Level"]
    print(f"{len(matches)} match(es):")
    for m in matches:
        print(f"  {m}  ({m()})")

    # REPL discovery 
    print("children of DistillingSystem:", dir(client.objects.DistillingSystem))
```

---

## Next steps

| Topic | What it covers |
|---|---|
| [Node API syntax](140_node-api-syntax.md) | The three shapes (`.`, `[]`, `()`) and how they map to `client.read`, `client.write` and `client.call`. |
| [NodeIds and namespace info](430_nodeids-and-namespace-info.md) | When you need the `NodeId` (for logging, error messages or another system): string forms, shortnames and namespace metadata. |
