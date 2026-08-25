# Implementing behaviour

Declared types describe the interface; the behaviour lives in Python classes and
callbacks that `server.implement` binds to them. The complete rules are in
[Server callbacks](callbacks.md) and
[Implementing Object Behavior](../sdk-fundamentals/namespace/implementing-object-behavior.md);
what follows is the server-side shape and the traps.

An implementation is an *undecorated* subclass of a declared type. Variable
behaviour uses the `@o6.read` / `@o6.write` decorators, Method behaviour uses
`@o6.call`:

```python
import o6
import plant

class TemperatureImpl(plant.TemperatureType):
    reading = 19.5

    @o6.read
    def _read(self, *, range, session, includeSourceTimestamp):
        return (o6.StatusCode.GOOD, self.reading)

    @o6.write
    def _write(self, value, *, range, session):
        if value.value < 0:
            return (o6.StatusCode.BAD_OUT_OF_RANGE,)
        self.reading = float(value.value)
        return (o6.StatusCode.GOOD,)

class MachineImpl(plant.MachineType):
    temperature: TemperatureImpl

    def __init__(self, *, tag="untagged", **kwargs):
        super().__init__(**kwargs)
        self.tag = tag

    @o6.call("ns=plant;Reset")
    def resetMachine(self, mode):
        return (o6.StatusCode.GOOD, True)
```

The pair is registered on one server, **after** the namespace is published and
before nodes of that type are created:

```python
server = o6.Server(port=4840)
server.ns.append(plant)                              # 1. publish the model
server.implement(plant.MachineType, MachineImpl)     # 2. bind the behaviour
server.implement(plant.TemperatureType, TemperatureImpl)
server.start()                                       # 3. serve
```

Getting that order wrong is a hard error, not a silent one: calling
`implement` before `ns.append` raises `KeyError` with the type's NodeId, because
the type node does not exist in the server's nodestore yet.

The `@o6.call` target deserves attention. A single-segment target is a
**qualified UA BrowseName** — `"Reset"` means `ns=0;Reset`, so a Method declared
in the `plant` namespace needs `"ns=plant;Reset"`. A target containing a dot is
a **Python member path** through the containing Object, such as
`"controller.reset"`. A target that matches nothing fails at registration with
`uses @o6.call for unknown UA Method`.

## The marker-versus-implementation trap

`server.implement(Type, Impl)` governs nodes that enter through *native type
instantiation* — a client's AddNodes request, a Mandatory member created as part
of a larger instance, `server.addObject(typeDefinition=...)`. It does **not**
change what direct Python construction produces:

```python
machine = plant.MachineType(parent=server.objectsNode, browseName="M-100")
type(machine).__name__          # 'MachineType__Live' — the generated class
machine.reset(o6.Int32(1))      # StatusCodeError: BadNotImplemented

machine = MachineImpl(parent=server.objectsNode, browseName="M-101", tag="line-1")
type(machine).__name__          # 'MachineImpl__Live'
machine.reset(o6.Int32(1))      # (StatusCode.GOOD, True)
machine.tag                     # 'line-1'
```

Instantiate the implementation class when you construct nodes from Python. The
`server.implement` binding is what makes *externally created* nodes come out as
`MachineImpl`. Members do follow the binding either way: `machine.temperature`
is a `TemperatureImpl` in both cases above, because it was created by type
instantiation.

## Runtime changes

`implement` also replaces individual callback slots on concrete nodes, which is
how you attach behaviour to imperatively created nodes:

```python
computed = server.addVariable("Computed", server.objectsNode, 0.0)

server.implement(computed, read=lambda node, **kw: (o6.StatusCode.GOOD, 3.5))
computed()                       # 3.5 — the callback owns the value now
server.implement(computed, write=lambda node, value, **kw: (o6.StatusCode.GOOD,))
```

A read slot must exist before a write slot: open62541's callback value sources
must be readable, so a write-only Variable is rejected. Once a Variable is
callback-backed, the callbacks own its state and no shadow value is kept.

Positional forms reset behaviour. `implement(node, None)` repeats the
construction-time resolution, and a positional value abandons the callbacks and
installs that value in native storage:

```python
server.implement(computed, o6.Double(11.0))     # back to native storage
computed()                                      # 11.0
```

Two edges are worth knowing because both surface as errors rather than
surprises. `implement(variable, None)` on a Variable that was *created* with
native storage raises `TypeError` telling you to pass a value instead — there is
no construction-time callback to restore. And `implement(method, None)` on a
Method created by `addMethod` clears the slot rather than restoring the original
function, so subsequent calls return `BadNotImplemented`; re-install the
callback with `call=` when you want it back.

Type-level changes never rewrite existing nodes:

```python
server.implement(plant.TemperatureType, read=type_read)   # future Variables only
server.implement(plant.MachineType, None)                 # future Objects only
```
