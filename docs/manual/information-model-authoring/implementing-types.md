# Implementing Declared Types

Attach application behavior to handwritten or compiled type declarations without
changing the model. Callback argument and result contracts are described in
[Callbacks & External Data](../server/callbacks.md).

A type declaration is a contract. `@o6.objecttype` says a `MachineType` has a `Reset` Method that takes an `Int32` and returns a `Boolean`. It does not say what resetting a machine does. `@o6.variabletype` says a `Temperature` is a `Double`, not where the value comes from.

The *implement pattern* attaches the behavior. You write a second, undecorated Python class that subclasses the declaration and contains the code, and register it with `server.implement(Declaration, Implementation)`. The binding applies to future instances created through server type
instantiation. Direct construction of a declaration class keeps that class;
construct the implementation class explicitly when using Python constructors.
See [Direct Python construction](#direct-python-construction-opts-out).

Keeping declaration and implementation separate has these effects:

- **A generated namespace stays untouched.** Compiled companion specifications and vendor nodesets are regenerated whenever the XML changes. Behavior lives in your own module and survives regeneration.
- **The contract stays accurate.** The declaration is exactly what a client browses, independent of the implementation.
- **Behavior is per server.** The binding is stored on that server's own type node. Two servers in one process can implement the same UA type differently, without a global registry.
- **State is per node.** Each live node is an instance of the implementation class, so `self.…` attributes give every object its own state.

## The three parts

This is a complete two-file example. Save step 1 as `counter_types.py`, then
combine steps 2 and 3 in `counter_server.py` beside it. Run
`python counter_server.py`; it increments once, prints `5`, and stops.

### 1. Declare

The declaration under `o6.call(...)` carries the Method's BrowseName and signature, and no function body.

!!! info
    **You don't always write step 1.** This page declares `CounterType` so that all three steps are visible. An ObjectType whose Methods are declared by a precompiled companion specification (a packaged `o6.ns.*` module, or a package produced by the [nodeset compiler](compiling-nodesets.md)) already has its contract, and you start at step 2. This is the pattern's main use. See [Starting from a generated declaration](#starting-from-a-generated-declaration).

```python
# counter_types.py
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

The Python member is `increment` (the attribute name). The UA BrowseName is `Increment`. The sections below use each name for different things.

### 2. Implement

Subclass the declaration without a decorator. A second `@o6.objecttype` would declare a new UA subtype, and `server.implement` rejects it.

```python
# counter_server.py
from typing import Any
import o6
import counter_types
from counter_types import CounterType


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

`__init__` runs on the already complete node, so `super().__init__(**kwargs)` is an ordinary cooperative Python call and does no OPC UA work. Accept `**kwargs` and pass it through. Nodes created natively or over `AddNodes` carry no Python-only arguments, so any extra parameter needs a default or must come from server or node state.

### 3. Register and instantiate

Continue `counter_server.py` with the following code. Publish the declaration,
register its implementation, then create instances:

```python
server = o6.Server(port=4840)
server.ns.append(counter_types)
server.implement(CounterType, CounterImpl)

counter = server.addObject(
    "Counter",
    server.objectsNode,
    typeDefinition=CounterType,        # the DECLARATION
    nodeId="ns=tutorial;i=1000",
    ns=o6.ns.tutorial.index,
)

assert isinstance(counter, CounterImpl)
with server:
    status, total = counter.increment(o6.Int32(5))
    print(int(total))                     # 5
```

You name the declaration at the call site and get the implementation back. `CounterImpl` appears only in the `implement` call. `addObject`, a client's `AddNodes` request and a nested child of another type don't need to know it exists.

### Direct Python construction opts out

Calling a Python class directly selects that class for the new node. These
are alternative fragments to insert before `with server:` in `counter_server.py`:

```python
plain = CounterType(parent=server.objects, browseName="PlainCounter")
implemented = CounterImpl(parent=server.objects, browseName="ImplementedCounter")

assert not isinstance(plain, CounterImpl)
assert isinstance(implemented, CounterImpl)
```

The first counter has its declared Method but no implementation for it. The
second has the behavior from `CounterImpl`, without needing a type binding.
This selection concerns the node being constructed. Its children can still
use their own server type bindings; an explicit member implementation
annotation takes precedence for that child, as explained
[below](#narrowing-a-members-python-class).

### Starting from a generated declaration

With a companion specification type, only steps 2 and 3 remain. `ns0.objtypes.FileType` declares `Open`, `Read`, `Write`, `Close`, `GetPosition` and `SetPosition` with their full signatures. The implementation subclasses the generated class and binds behavior to the BrowseNames the specification defines:

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

Both steps are the same as for `CounterType`. `ns0` needs no `append`, but any other companion specification does: call `server.ns.append(di)` first, then `server.implement(...)`.

You can implement only some of a type's Methods. The Methods you don't bind
stay declared but unimplemented and fail when called. If the type declares or
inherits Methods with the same local BrowseName in different namespaces, use
a qualified target such as `@o6.call("ns=di;TransferToDevice")`; see
[Binding a target](callback-binding.md#binding-a-target).

---

## Variables

A Variable has two independent slots, `read` and `write`. You fill them on the VariableType or on the owning Object.

### On the VariableType

The following fragments use the declarations in `plant.py`, already published
on `server`. Import `plant` in the implementation module.

Untargeted `@o6.read` / `@o6.write` implement the VariableType's own value:

```python
class TemperatureImpl(plant.TemperatureType):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self._reading = 20.0

    @o6.read
    def _read(self, *, range, session, includeSourceTimestamp):
        return (o6.StatusCode.GOOD, o6.Double(self._reading))

    @o6.write
    def _write(self, value, *, range, session):
        self._reading = float(value.value)
        return (o6.StatusCode.GOOD,)


server.implement(plant.TemperatureType, TemperatureImpl)
```

The binding applies to future Variables created through server type
instantiation, including children of other types. Direct Python construction
selects the class explicitly, as in the Counter example above.

### On the owning Object, by member path

`@o6.read("member")` / `@o6.write("member")` implement one specific Variable from the class that owns it. Use this form when you don't want to specialise the Variable's own type.

For this alternative, first add this declaration to `plant.py`:

```python
@o6.objecttype(ns="plant", browseName="SetpointType")
class SetpointType(ns0.objtypes.BaseObjectType):
    setpoint: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            browseName="ns=plant;Setpoint",
            dataType=o6.Double,
            accessLevel=3,                      # CurrentRead | CurrentWrite
            userAccessLevel=3,
        )
    )
```

The implementation targets the `setpoint` member:

```python
class SetpointImpl(plant.SetpointType):
    LOW, HIGH = 0.0, 100.0

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self._reading = 20.0

    @o6.read("setpoint")
    def _read_setpoint(self, **kwargs) -> tuple[o6.StatusCode, o6.Double]:
        return (o6.StatusCode.GOOD, o6.Double(self._reading))

    @o6.write("setpoint")
    def _write_setpoint(self, value, **kwargs) -> tuple[o6.StatusCode]:
        clamped = max(self.LOW, min(self.HIGH, float(value.value)))
        self._reading = clamped
        return (o6.StatusCode.GOOD,)
```

The value lives in `self._reading`. For a `controller` instance constructed
as `SetpointImpl`, writes store the clamped value and subsequent reads return it:

```python
controller.setpoint(150.0)
controller.setpoint()          # 100.0
controller.setpoint(-5.0)
controller.setpoint()          # 0.0
```

!!! warning
    The read/write target is the Python member name (`"setpoint"`), not the BrowseName. `@o6.call`, in contrast, resolves by BrowseName. Qualifying the child's BrowseName as `ns=plant;Setpoint` does not change the decorator's target. Dotted paths work as for `@o6.call`, for example `@o6.read("parameterSet.temperature")`, and every segment except the last must be an Object.

### Narrowing a member's Python class

An Object implementation can select a Python implementation class for one of
its children by annotating the member. This fragment uses the
`TemperatureImpl` above:

```python
class MachineImpl(plant.MachineType):
    temperature: TemperatureImpl
```

This selects the Python class of this Object's child, taking precedence over
a server binding for that child's type. It works both when `MachineImpl` is
selected by `server.implement` and when it is constructed directly. The
Variable keeps its UA TypeDefinition and address-space metadata. Independent
Temperature Variables follow their own construction choice and server binding.
The annotation composes through nested Object implementations.

For an inherited Optional member, the annotation also decides inclusion. `temperature: TemperatureImpl` includes the member in every instance built as this implementation. `temperature: TemperatureImpl | None` leaves it optional. The UA declaration and its ModellingRule are unchanged either way.

---

## What `server.implement` binds

### The binding is exact, and per server

The binding matches exactly one UA TypeDefinition. A subtype is a different
type node and is not covered. Continuing the preceding `MachineImpl` fragment,
after publishing `plant` on `server`:

```python
server.implement(plant.MachineType, MachineImpl)

machine = server.addObject("C", server.objects, typeDefinition=plant.CncMachineType)
assert not isinstance(machine, MachineImpl)
```

Register each subtype explicitly. As an alternative to the preceding
`MachineImpl`, define both implementations with a shared mixin before binding
either one on a fresh server:

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

The binding lives in the server's own nodestore, so it is local to that server. Repeating the same pair has no effect; a competing pair on the same server is rejected:

```
TypeError: MachineType is already implemented by MachineImpl on this server
```

The implementation must be undecorated. A `@o6.objecttype` subclass declares a UA subtype and is rejected with `implementation must be undecorated; it must not declare a UA subtype`.

### Register before nodes are created

The binding decides how nodes are constructed. A later `implement` never changes existing instances. Call it after `server.ns.append(...)` and before anything creates instances of the type, including before `server.start()` lets a client send `AddNodes`.

Passing `None` restores the declaration's own Python class for future instances only:

```python
server.implement(plant.MachineType, None)
```

## ObjectType and VariableType initialization

This optional declaration belongs in `plant.py`. A runtime caller can pass
an application-owned `device` when constructing `DeviceType` directly:

```python
@o6.objecttype(ns="plant")
class DeviceType(ns0.objtypes.BaseObjectType):
    def __init__(self, *, device=None, **kwargs):
        super().__init__(**kwargs)
        self.device = device

    def __del__(self):
        if self.device is not None:
            self.device.close()
```

Declared ObjectTypes and VariableTypes use ordinary Python construction.
`__new__` completes OPC UA node construction, then calls the application
initializer on the finished node. `super().__init__(...)` is the normal
cooperative Python initializer call and performs no OPC UA work. Initializers
and finalizers inherit through the Python type hierarchy as usual.

The server's nodestore keeps the Python object alive while the OPC UA node
exists. After the node is removed, remaining Python references can delay
`__del__`. Use `__del__` for Python-owned resources, not for protocol actions
that must happen at the moment of OPC UA deletion.
