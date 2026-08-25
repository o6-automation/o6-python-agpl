# Implementing Object Behavior

A type declaration is a **contract**. `@o6.objecttype` says a `MachineType` has a `Reset` Method taking an `Int32` and returning a `Boolean`; it says nothing about what resetting a machine does. `@o6.variabletype` says a `Temperature` is a `Double`; it does not say where that Double comes from.

The **implement pattern** is how the behavior gets attached: a second, undecorated Python class that subclasses the declaration and carries the code, registered with `server.implement(Declaration, Implementation)`. From that point on, every instance the server materialises for that UA type is an instance of your class.

Keeping the two apart is what makes the pattern worth having:

- **A generated namespace stays untouched.** Compiled companion specs and vendor nodesets describe the UA interface and are regenerated whenever the XML changes. Behavior lives in your own module and survives regeneration.
- **The contract stays honest.** The declaration is exactly what a client browses. It cannot drift toward what the implementation happens to do.
- **Behavior is per server.** The binding is stored on that server's own type node, so two servers in one process can implement the same UA type differently, and neither needs a global registry.
- **State is per node.** Each live node *is* an instance of the implementation class, so ordinary `self.…` attributes give every object its own state.

!!! info
    This page is about applying behavior to your own or a generated type. The precedence rules it summarises are stated normatively in [Server callbacks](../../server/callbacks.md); the declaration side — `@o6.objecttype`, `o6.call(...)`, children and namespaces — is [Writing a Nodeset in Python](writing-nodesets-in-python.md).

---

## The three parts

### 1. Declare

The declaration under `o6.call(...)` carries the Method's BrowseName and signature, and no function body.

!!! info
    `CounterType` is written out here only so that every moving part of the pipeline is visible in one page — the declaration, the implementation and the registration side by side. **Step 1 is not something you always write.** Any ObjectType whose Methods are already declared by a precompiled companion spec — a packaged `o6.ns.*` module, or a package produced by the [nodeset compiler](compiling-nodesets.md) — arrives with its contract complete, and you start at step 2. That is in fact the pattern's main use: generated modules describe the UA interface and are regenerated whenever the XML changes, so behavior must live outside them. [Starting from a generated declaration](#starting-from-a-generated-declaration) shows that path once both remaining steps have been introduced.

```python
import o6
from o6.ns import ns0

o6.ns.namespace("tutorial", uri="http://o6-automation.com/UA/Tutorial/", version="1.0")


@o6.objecttype(ns="tutorial", nodeId="ns=tutorial;i=1", browseName="CounterType")
class CounterType(ns0.objtypes.BaseObjectType):
    """A counter object type — declared only, implemented separately."""

    increment: o6.node.MethodNode = o6.hasComponent(
        o6.call(
            browseName="ns=tutorial;Increment",
            inputArgs=[
                ns0.datatypes.Argument(
                    name="step",
                    dataType=o6.Int32,
                    valueRank=o6.ValueRank.SCALAR,
                    description="Amount to add to the counter",
                )
            ],
            outputArgs=[
                ns0.datatypes.Argument(
                    name="total",
                    dataType=o6.Int32,
                    valueRank=o6.ValueRank.SCALAR,
                    description="The counter value after incrementing",
                )
            ],
        )
    )
```

The Python member is `increment` (lowercase, the attribute name), while the UA BrowseName is `Increment`. Both names matter later, for different things.

### 2. Implement

Subclass the declaration — **undecorated**. A second `@o6.objecttype` would declare a new UA subtype, which is not what you want here and is rejected.

```python
from typing import Any


class CounterImpl(CounterType):
    """Provide the behavior for CounterType."""

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._count = 0

    @o6.call("Increment")
    def _increment(self, step: o6.Int32) -> tuple[o6.StatusCode, o6.Int32]:
        self._count += int(step)
        return (o6.StatusCode.GOOD, o6.Int32(self._count))
```

`@o6.call("Increment")` binds this Python method to the declared UA Method. `self._count` is per-node state: two Counter objects on the same server count independently.

`__init__` runs on the already-complete node, so `super().__init__(**kwargs)` is the ordinary cooperative Python call and does no OPC UA work. Accept `**kwargs` and pass it through — nodes created natively or over `AddNodes` carry no Python-only arguments, so any extra parameter your class wants needs a default or must come from server/node state.

### 3. Register

```python
server = o6.Server(port=4840)
server.ns.append(counter_types_module)
server.implement(CounterType, CounterImpl)

counter = server.addObject(
    "Counter",
    server.objectsNode,
    typeDefinition=CounterType,        # the DECLARATION
    nodeId="ns=tutorial;i=1000",
    ns=o6.ns.tutorial.index,
)

isinstance(counter, CounterImpl)       # True
```

Note the asymmetry that makes the pattern pleasant to use: you name the *declaration* at the call site and get the *implementation* back. `CounterImpl` appears exactly once, in the `implement` call. Nothing downstream — not `addObject`, not a client's `AddNodes` request, not a nested child of another type — has to know it exists.

### Starting from a generated declaration

With a companion-spec type, step 1 is already done and only steps 2 and 3 remain. `ns0.objtypes.FileType` declares `Open`, `Read`, `Write`, `Close`, `GetPosition` and `SetPosition` with their full signatures, so the implementation subclasses the generated class directly and binds behavior to the BrowseNames the spec defines:

```python
from o6.ns import ns0


class FileImpl(ns0.objtypes.FileType):                  # step 2
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._handle = 0

    @o6.call("Open")
    def _open(self, mode: o6.Byte) -> tuple[o6.StatusCode, o6.UInt32]:
        self._handle += 1
        return (o6.StatusCode.GOOD, o6.UInt32(self._handle))


server.implement(ns0.objtypes.FileType, FileImpl)       # step 3
```

Both steps are byte-for-byte the same as for `CounterType`; only the source of the declaration differs. `ns0` needs no `append`, but any other companion spec does — `server.ns.append(di)` first, then `server.implement(...)`.

Implementing only *some* of a type's Methods is normal: the ones you bind get your behavior, the rest stay declared-but-unimplemented and fail when called. And a Method whose BrowseName is declared in more than one appended namespace needs the qualified form, `@o6.call("ns=di;TransferToDevice")` — see [Binding a target](#binding-a-target) below.

---

## Methods

### Binding a target

`@o6.call(target)` takes the UA Method's BrowseName. A bare name is resolved against the Methods the type declares or inherits:

```python
@o6.call("Increment")                                  # resolved for you
@o6.call("ns=tutorial;Increment")                       # explicitly qualified
```

Pass the qualified form when the same bare name is declared in more than one namespace — o6 rejects an ambiguous bare name with an error telling you to qualify it. A target that matches nothing fails when the first instance is constructed:

```
TypeError: Broken._x uses @o6.call for unknown UA Method 'ns=0;Rset';
declare or inherit that Method child
```

which is deliberate: a misspelled target is reported rather than becoming a silently unreachable implementation.

A **dotted target** reaches a Method on a nested child. The path is made of **Python member names**, not BrowseNames:

```python
@o6.objecttype(ns="demo", browseName="CellType")
class CellType(ns0.objtypes.BaseObjectType):
    controller: ControllerType = o6.hasComponent(ControllerType())


class CellImpl(CellType):
    @o6.call("controller.reset")
    def _reset_controller(self) -> tuple[o6.StatusCode, o6.Boolean]:
        return (o6.StatusCode.GOOD, o6.Boolean(True))
```

This is how an outer type owns behavior that spans its children — the cell decides what resetting its controller means, without the controller type needing an implementation of its own. The path is resolved **once**, when the containing Object finishes construction, and the callable is stored directly on that instance's Method node. Calls never browse the address space.

!!! warning
    A dotted path traverses **Objects**. A segment naming a complex *Variable* child fails construction with `a construction owner must be an Object or ObjectType`. Implement the VariableType itself instead (see [Variables](#variables) below).

### The callback signature

```python
(self, *inputs) -> (o6.StatusCode, *outputs)
```

`self` is the Object the Method was invoked on. Inputs and outputs follow the declared `InputArguments` / `OutputArguments` order.

- A Bad status may be returned **alone**: `return (o6.StatusCode.BAD_INVALID_ARGUMENT,)`.
- A non-Bad status must be followed by **exactly** the declared number of outputs.
- `async def` works, with identical arguments and result-tuple behavior.

```python
@o6.call("Divide")
def _divide(self, dividend: o6.Double, divisor: o6.Double):
    if divisor == 0:
        return (o6.StatusCode.BAD_INVALID_ARGUMENT,)
    return (o6.StatusCode.GOOD, o6.Double(dividend / divisor))
```

A declared Method with no implementation is a valid node — browsable, with correct arguments — that fails when called. Declaring the contract before the behavior exists is a normal intermediate state.

### One dispatcher, two entry points

The same callback serves in-process attribute calls and OPC UA `Call` service requests, and both share the node's state:

```python
counter.Increment(o6.Int32(5))                  # in-process → (GOOD, 5)
counter.Increment(o6.Int32(3))                  # in-process → (GOOD, 8)

client.call(o6.NodeId(counter), o6.NodeId(counter.Increment), [o6.Int32(10)])   # → (GOOD, 18)
```

Note that the *attribute* is `counter.Increment` — capitalised, from the BrowseName — while the declaration's Python member was `increment`. The live node exposes its children under their BrowseNames.

o6 configures open62541 to copy every Method declaration into each Object instance, so each object has its own Method NodeId and its own callback slot. Nothing is looked up at invocation time: the callback is already stored on the concrete Method node.

### Overriding in a subclass

An ordinary Python override needs no decorator — same method name, new body. Repeat `@o6.call(...)` only when the *Python* name changes:

```python
class AuditedCounterImpl(CounterImpl):
    @o6.call("Increment")
    def _increment_with_audit(self, step: o6.Int32):
        self.log(step)
        return super()._increment(step)
```

Two decorators in **one** class body may not target the same UA Method; class creation reports both competing Python names.

---

## Variables

Variables have two independent slots, `read` and `write`, and two ways to fill them.

### On the VariableType

Undecorated `@o6.read` / `@o6.write` implement the VariableType's *own* value:

```python
@o6.variabletype(ns="plant", dataType=o6.Double)
class TemperatureType(ns0.vartypes.BaseDataVariableType):
    pass


class TemperatureImpl(TemperatureType):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._value = 20.0

    @o6.read
    def _read(self, *, range, session, includeSourceTimestamp):
        return (o6.StatusCode.GOOD, o6.Double(self._value))

    @o6.write
    def _write(self, value, *, range, session):
        self._value = float(value.value)
        return (o6.StatusCode.GOOD,)


server.implement(TemperatureType, TemperatureImpl)
```

Registered this way, the behavior applies to every Variable of that type the server materialises — including ones that appear as children of other types.

### On the owning Object, by member path

`@o6.read("member")` / `@o6.write("member")` implement one *specific* Variable from the class that owns it. This is the form to reach a Variable whose own type you do not want to specialise:

```python
@o6.objecttype(ns="tutorial", nodeId="ns=tutorial;i=1", browseName="SetpointType")
class SetpointType(ns0.objtypes.BaseObjectType):
    setpoint: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=tutorial;i=2",
            browseName="ns=tutorial;Setpoint",
            dataType=o6.Double,
            accessLevel=3,                      # CurrentRead | CurrentWrite
            userAccessLevel=3,
        )
    )


class SetpointImpl(SetpointType):
    LOW, HIGH = 0.0, 100.0

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._value = 20.0

    @o6.read("setpoint")
    def _read_setpoint(self, **kwargs: Any) -> tuple[o6.StatusCode, o6.Double]:
        return (o6.StatusCode.GOOD, o6.Double(self._value))

    @o6.write("setpoint")
    def _write_setpoint(self, value: Any, **kwargs: Any) -> tuple[o6.StatusCode]:
        clamped = max(self.LOW, min(self.HIGH, float(value.value)))
        self._value = clamped
        return (o6.StatusCode.GOOD,)
```

Because the value lives in `self._value` instead of the node's native storage, the write callback can validate before storing, and every subsequent read reflects the stored — clamped — value:

```python
client.write(variable, o6.Double(150.0))
client.read(variable)                           # 100.0
client.write(variable, o6.Double(-5.0))
client.read(variable)                           # 0.0
```

!!! warning
    The read/write target is the **Python member name** (`"setpoint"`), not the BrowseName. This is the opposite of `@o6.call`, which resolves by BrowseName. Qualifying the child's BrowseName as `ns=tutorial;Setpoint` therefore does not change the decorator's target. Dotted paths work the same way as for `@o6.call` — `@o6.read("parameterSet.temperature")` — and every segment except the last must be an Object.

### The callback signature

```python
read:  (self, *, range, session, includeSourceTimestamp) -> (StatusCode, value)
write: (self, value, *, range, session)                  -> (StatusCode,)
```

- A Bad status is returned **alone**. A successful read returns exactly **one** value, converted using the Variable's declared DataType — or an `o6.DataValue` when you need to supply timestamps or picoseconds explicitly.
- `value` on write is the requested `o6.DataValue`; `value.value` is the payload.
- `range` is `None` for a whole-value access, or a tuple of stop-exclusive Python slices for an IndexRange — OPC UA `2:5` arrives as `(slice(2, 6),)`.
- `session` is an `o6.Session` for client operations and `None` for internal ones.
- Variable callbacks are **synchronous**, and recursion is rejected with `BadInvalidState`: a read may not re-enter the same Variable's read or write.

Accept `**kwargs` when you do not need the context, as both examples above do.

### Which value source a Variable ends up with

The two slots decide it together:

| `read` slot | `write` slot | Result |
|---|---|---|
| absent | absent | native stored value |
| present | present | Python callbacks own the value |
| present | absent | Python callbacks, read-only |
| absent | present | **rejected** — an open62541 callback value source must be readable |

Once a Variable is callback-backed, its callbacks own the state; o6 keeps no shadow value. `variable()` and `variable(value)` are normal Value reads and writes and go through the callbacks like any client access — there is no syntax that reaches behind them into native storage.

### Narrowing a member's Python class

An Object implementation can select a Python-only implementation class for one of its Variable (or Object) children by annotating the member:

```python
class MachineImpl(vendor.objtypes.MachineType):
    temperature: TemperatureImpl
```

This changes only the concrete Python class for *this* Object's child. The Variable keeps its UA TypeDefinition and all address-space metadata, and an independently created `TemperatureType` elsewhere still uses its generated class. The annotation composes through nested Object implementations.

For an inherited **Optional** member the annotation also decides inclusion: `temperature: TemperatureImpl` includes it in every instance built as this implementation, while `temperature: TemperatureImpl | None` leaves it optional. The UA declaration and its ModellingRule are unchanged either way.

---

## What `server.implement` actually binds

### The binding is exact, and per server

It matches **that one UA TypeDefinition**. A subtype is a different type node and is not covered:

```python
server.implement(MachineType, MachineImpl)

server.addObject("C", ..., typeDefinition=CncMachineType)   # NOT MachineImpl
```

Register each subtype explicitly. To share behavior across them, put it in a plain mixin rather than in a registered implementation class:

```python
class ResetBehaviour:
    @o6.call("Reset")
    def _reset(self, mode):
        return (o6.StatusCode.GOOD, o6.Boolean(True))


class MachineImpl(ResetBehaviour, plant.MachineType): ...
class CncImpl(ResetBehaviour, plant.CncMachineType): ...

server.implement(plant.MachineType, MachineImpl)
server.implement(plant.CncMachineType, CncImpl)
```

The binding lives in that server's own nodestore, which is what makes it naturally server-local. Repeating the same pair is harmless; a **competing** pair on the same server is rejected:

```
TypeError: MachineType is already implemented by MachineImpl on this server
```

The implementation must be undecorated — a `@o6.objecttype` subclass declares a UA subtype and is rejected with `implementation must be undecorated; it must not declare a UA subtype`.

### Register before nodes are created

The binding decides how nodes are *constructed*. Existing instances are never rewritten by a later `implement`, so call it after `server.ns.append(...)` and before anything creates instances of the type — including before `server.start()` lets a client issue `AddNodes`.

Passing `None` restores the declaration's own Python class for **future** instances only:

```python
server.implement(MachineType, None)
```

### Direct Python construction opts out

The binding covers nodes entering through native type instantiation: `Server.addObject`, native APIs, and client `AddNodes` requests. Calling the declaration class directly deliberately keeps the generated Python class, for itself *and* for its children:

```python
m = plant.MachineType(parent=server.objectsNode, browseName="M")
type(m).__name__                # MachineType__Live — not MachineImpl
```

Instantiate the implementation class when that is what you want:

```python
m = MachineImpl(parent=server.objectsNode, browseName="M")
```

This is a common surprise when a hand-written namespace module creates its own instances: those instances are built by Python construction and therefore ignore `implement` bindings.

### Replacing a single slot at runtime

`call=`, `read=` and `write=` set one slot on one concrete node — or on a VariableType, as a template for Variables created afterwards:

```python
server.implement(method, call=divide)                      # one Method node
server.implement(machine.temperature, read=instance_read)   # one Variable
server.implement(TemperatureType, read=type_read)           # future Variables of that type
```

Here the callables are plain functions whose first parameter is the node, rather than bound methods:

```python
def divide(node, dividend, divisor):
    if divisor == 0:
        return (o6.StatusCode.BAD_INVALID_ARGUMENT,)
    return (o6.StatusCode.GOOD, dividend / divisor)
```

`None` clears a slot without revealing or recomputing an earlier one:

```python
server.implement(machine.temperature, read=None)
```

Removing the *last* callback from a concrete Variable needs an explicit whole-node decision. Positional `None` repeats construction-time resolution; a positional value switches the Variable to native storage without consulting the old read callback:

```python
server.implement(machine.temperature, None)              # re-resolve as at construction
server.implement(machine.temperature, o6.Double(20))     # native storage, value 20
```

Positional `None` on a Variable that was constructed with native storage in the first place is an error (`use implement(variable, value) to restore it`) — there is nothing to restore.

---

## Precedence, in one paragraph

`read`, `write` and `call` all resolve the same way, and only ever at **construction** time:

1. Start at the node's concrete Python implementation type and search upwards through its bases. The first matching callback is copied onto the concrete Variable or Method node.
2. As containing Objects finish — innermost first — every matching `@o6.read("path")`, `@o6.write("path")` or `@o6.call("path")` **replaces** that slot. An outer path therefore wins when two paths target the same node.
3. A later `Server.implement` replaces or clears the slot directly.

Invocation never searches a type hierarchy and never resolves a path; it calls the callback already stored on the node. The full normative statement, including Optional-member behavior and the async-Method details, is in [Server callbacks](../../server/callbacks.md).

---

## Pitfalls

| Symptom | Cause |
|---|---|
| `addObject` returns the declaration class, not the implementation | `implement` not called, called after the node was created, or the node's TypeDefinition is a *subtype* of the registered one |
| `implementation must be undecorated; it must not declare a UA subtype` | the implementation carries `@o6.objecttype` / `@o6.variabletype` |
| `uses @o6.call for unknown UA Method 'ns=0;X'` | misspelled or undeclared target; a bare name that needs qualifying |
| `one Python method cannot implement two UA Methods` | two `@o6.call` decorators on one function |
| `a construction owner must be an Object or ObjectType` | a dotted `read`/`write`/`call` path traverses a complex *Variable* child |
| a `@o6.read("…")` never fires | the target is the **Python member name**, not the BrowseName |
| writes silently do nothing | a `write` callback that returns `GOOD` without storing — a callback-backed Variable has no native storage behind it |
| behavior missing on a Python-constructed instance | direct construction of the declaration class bypasses `implement` |

---

## See also

- The two runnable tutorials this page is built from:
  [`examples/highlevel/implement_objtype.py`](https://github.com/o6-automation/o6-python-agpl/blob/main/examples/highlevel/implement_objtype.py)
  and [`examples/highlevel/implement_readwrite.py`](https://github.com/o6-automation/o6-python-agpl/blob/main/examples/highlevel/implement_readwrite.py).
- The normative callback reference — signatures, resolution, Optional members, async Methods, recursion guards:
  [Server callbacks](../../server/callbacks.md).
- Declaring the types these implementations attach to:
  [Writing a Nodeset in Python](writing-nodesets-in-python.md).
- Implementing a type that came from XML rather than from Python:
  [Compiling Nodesets](compiling-nodesets.md).
- Instance ownership, type children and access control:
  [Server](../../server/index.md).
- What the specification says about Methods and their arguments:
  [Part 4, §5.11 — Method Service Set](https://reference.opcfoundation.org/Core/Part4/v105/docs/5.11)
  and [Part 3, §4.7 — Methods](https://reference.opcfoundation.org/Core/Part3/v105/docs/4.7).
