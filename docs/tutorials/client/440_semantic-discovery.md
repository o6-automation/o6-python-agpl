# Semantic Discovery

Picking up from [Load packaged companion specs](410_load-packaged-companion-specs.md): you've been carrying `NodeId` strings around the distillery code — `"ns=1;i=1302"` for `Kettle.Temperature`, `"ns=1;i=1204"` for `Status.Setpoint`. Those `NodeId`s are correct, but they make the code brittle: if the server is rebuilt and the namespace indices shift, every `NodeId` literal has to be updated by hand. The last piece of the user story is to replace those literals with a *semantic* lookup — navigate the address space by `BrowseName`, with the dotted `client.objects.DistillingSystem.Kettle.Temperature()` style, and let `o6` resolve the `NodeId` at the moment of the call.

This is the same operation [Browse](110_browse.md) does — traverse the address space looking for a child — but exposed as a Python expression rather than a list of `ReferenceDescription`. The `Node` object you get back can be read, written, or called with `()`; the underlying `NodeId` is hidden.

This page walks through three steps:

1. Navigate the distillery by BrowseName with `client.objects.DistillingSystem.Kettle.Temperature`.
2. Read, write, and call on the resulting `Node` with the `()` syntax.
3. Use `[]` for ambiguous BrowseNames and `dir(...)` for REPL discovery.

!!! info
    This tutorial expects the [example server running](../setup.md) in the background, and assumes you know how to [create and connect](100_connect.md) a client, how to [browse](110_browse.md) the address space, and how to [load packaged companion specs](410_load-packaged-companion-specs.md). The snippets use the distillery's `DistillingSystem` (`ns=1;i=1000`), `Kettle` (`ns=1;i=1300`), and `Status` (`ns=1;i=1200`) sub-objects as the running example.

---

## Navigate by BrowseName

The distillery's address space has a stable shape: under `Objects` you find `DistillingSystem`, and under `DistillingSystem` you find `Kettle`, `Status`, `Identification`, `Distillate`, `Actuators`, `Events`. The `Node` API exposes that as a dotted path:

```python
from o6 import Client

with Client("opc.tcp://localhost:4840") as client:
    objects = client.objects                           # the Objects folder
    distilling = objects.DistillingSystem              # ns=1;i=1000
    kettle = distilling.Kettle                          # ns=1;i=1300
    temperature = kettle.Temperature                   # ns=1;i=1302
```

Names are matched case-insensitively against `BrowseName` — `kettle`, `KETTLE`, and `Kettle` all resolve to the same child. Each `.` triggers a server-side `Browse` for the named child on the current node. The result is a `Node` subclass (`VariableNode`, `ObjectNode`, `MethodNode`, …) depending on the child's `NodeClass`.

The `Node` API hides the `NodeId` — `temperature.nodeId` is the underlying integer/string, but you rarely need to touch it. Read, write, and call are all done on the `Node` object itself.

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

The `()` operator handles every interaction. The distinction is by argument shape, not by method.

Reading a variable value becomes a call with no arguments:

```python
temperature = client.objects.DistillingSystem.Kettle.Temperature
print(temperature())               # e.g. 20.0
```

Writing the variable is a call with a single positional argument:

```python
setpoint = client.objects.DistillingSystem.Status.Setpoint
setpoint(90.0)                     # writes the Value attribute
```

Reading a non-`Value` attribute uses the `attr=` keyword:

```python
print(temperature(attr="BrowseName"))  # "Temperature"
print(temperature(attr="NodeClass"))   # "VARIABLE"
```

Writing a non-`Value` attribute uses both `value=` and `attr=`:

```python
temperature(value="KettleTemp", attr="BrowseName")
```

Calling a method on an object is also `()` — pass the input arguments positionally. The parent object is picked up automatically:

```python
distilling = client.objects.DistillingSystem
status, = distilling.Start()       # StatusCode, then any output args
```

The distillery's `Start` and `Shutdown` take no inputs and produce no outputs, so the destructure is just `status, = ...`. The first element of the tuple is the `StatusCode` (see [Call a method](130_call-method.md) for the full shape).

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

Two situations don't fit the dotted path cleanly:

- **Ambiguous BrowseNames.** If more than one child *of the same node* has the same `BrowseName` (case-insensitively), the dotted form can't pick a single target. Use `[]` with a browse path — a `/`-separated string of `<namespace-index>:<BrowseName>` segments (see [Node API syntax](140_node-api-syntax.md)) — and it returns *all* matching targets for you to pick from. The distillery doesn't have any actually-ambiguous names (both its `Level` variables — `Kettle.Level` at `ns=1;i=1301` and `Distillate.Level` at `ns=1;i=1401` — sit under *different* parents, so the path `/1:Kettle/1:Level` is already unambiguous), but the mechanism is the same either way — index into the returned list:

  ```python
  matches = client.objects.DistillingSystem["/1:Kettle/1:Level"]   # a list, even with one match
  kettle_level = matches[0]                                        # pick the target
  print(kettle_level())
  ```

- **REPL discovery.** When you don't know what children a node has, `dir(node)` runs a `Browse` and returns a list of the child names. Combined with `<TAB>` completion, it's the same workflow as the interactive browser in [Browse](110_browse.md) but inside a Python REPL:

  ```python
  >>> dir(client.objects.DistillingSystem)
  ['identification', 'status', 'kettle', 'distillate', 'actuators', 'events', 'start', 'shutdown']
  ```

  The list is fetched lazily on the first `dir(...)` and cached afterwards, so subsequent `dir()` calls are free.

!!! tip
    In a Python REPL, `dir(...)` plus `<TAB>` completion is the fastest way to explore a server you don't know yet. The first `dir(node)` triggers a `Browse`; once you know the names, the dotted path does the rest.

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

## What's next?

- [Node API syntax](140_node-api-syntax.md) — the same syntax you just learned, viewed from the language-feature angle: the three shapes (`.`, `[]`, `()`) and how they map to the high-level `client.read` / `client.write` / `client.call`.
- [NodeIds and namespace info](430_nodeids-and-namespace-info.md) — when you do need the `NodeId` (for logging, error messages, or handing off to a different system), this page shows how to get it back out of a `Node` and how shortnames resolve to indices on the server.
