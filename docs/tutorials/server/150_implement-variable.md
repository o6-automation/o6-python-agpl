# Declare and implement a Variable

So far, every Variable's behaviour has come from calling `addVariable` a particular way — `writable=False` here, a value there. That's fine for one still, but it doesn't scale to a plant with fifty of them: there's no single place that says "this is what a Setpoint looks like," only fifty separate `addVariable` calls that all happen to agree. This page is a first look at the alternative — declaring the *shape* once, as a reusable type, and writing its behaviour once too.

Concretely: the distillery's `Setpoint` clamps out-of-range writes to `[0.0, 100.0]` — [Variables with sources](320_variables-with-sources.md), much later in these tutorials, builds exactly that by installing `read=`/`write=` callbacks on one already-built Variable node. This page reaches the same clamping behaviour a different way: declare a UA `ObjectType` that owns a `Setpoint`-shaped Variable, then implement its read and write behaviour in a separate Python class. Every object the server later builds from that type gets the behaviour for free — no per-instance callback wiring needed.

You don't need to have read the [declared-types pages](200_declare-object-type.md) first — this page introduces just enough of `@o6.objecttype` to make the pattern work. Those pages go deep on the declaration side alone; this one is about pairing a declaration with an implementation.

---

## The pattern has three parts

1. **Declare** a UA `ObjectType` with a Variable child as a pure contract, with `@o6.objecttype`. The declaration carries no behaviour.
2. **Implement** that contract in a separate subclass. `@o6.read("<member>")` and `@o6.write("<member>")` bind Python behaviour to the declared Variable, by its Python attribute name.
3. **Register** the implementation with `server.implement(Declaration, Impl)` so the server uses it whenever it builds an instance of that type.

---

## Declare the type

A declared type needs a namespace to live in — register one shortname once, then reference it as `ns="distillery"` below. `SetpointType` declares one Variable child, `setpoint`, readable and writable (`accessLevel=3`), but with no behaviour attached yet:

```python
import o6
from o6.ns import ns0

o6.ns.namespace(
    shortname="distillery",
    uri="http://o6-automation.com/UA/Distillery/",
    version="1.0",
)


@o6.objecttype(ns="distillery", nodeId="ns=distillery;i=6000", browseName="SetpointType")
class SetpointType(ns0.objtypes.BaseObjectType):
    """A setpoint object — declared only, implemented separately below."""

    setpoint: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=distillery;i=6001",
            browseName="ns=distillery;Setpoint",
            dataType=o6.Double,
            accessLevel=3,       # CurrentRead | CurrentWrite
            userAccessLevel=3,
        )
    )
```

Nothing here says what a read or write of `setpoint` actually does — that's deliberate. A declaration on its own is metadata; instantiating it right now would give every instance the default, unclamped storage behaviour.

---

## Implement read and write in a subclass

Subclass the declaration and bind behaviour to `setpoint` **by its Python attribute name** — not by its BrowseName. The value lives in an ordinary instance attribute, `self._value`, so the write callback can validate before storing:

```python
from typing import Any

class SetpointImpl(SetpointType):
    """Clamp writes to [0.0, 100.0] before storing them."""

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

Both callbacks take keyword-only context (`session`, `range`, `includeSourceTimestamp` for reads) that this example ignores via `**kwargs`. The write callback returning a *clamped* value rather than rejecting the write outright is a choice — [Variables with sources](320_variables-with-sources.md) shows the alternative, rejecting out-of-range writes with `BAD_OUT_OF_RANGE` instead.

---

## Register and instantiate

`server.implement(SetpointType, SetpointImpl)` is the line the whole pattern is about: it wires `SetpointImpl` in as the class the server uses whenever it builds a `SetpointType` instance. From then on, `addObject(typeDefinition=SetpointType, ...)` hands back a live, fully-wired object — `SetpointImpl` is never named at the call site.

```python
import sys
import time

server = o6.Server(port=4840)
server.ns.append(sys.modules[__name__])
server.implement(SetpointType, SetpointImpl)

device = server.addObject(
    "Reflux",
    server.objectsNode,
    typeDefinition=SetpointType,
    nodeId="ns=distillery;i=6100",
    ns=o6.ns.distillery.index,
)

server.start()
print(f"read            -> {server.read(device.setpoint)}")
server.write(device.setpoint, o6.Double(150.0))   # above range
print(f"read after 150  -> {server.read(device.setpoint)}")
server.write(device.setpoint, o6.Double(-5.0))    # below range
print(f"read after -5   -> {server.read(device.setpoint)}")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pass

server.stop()
```

!!! warning
    Pass `server=server` explicitly if a constructor call like this one runs from inside the same script that declared the namespace — o6 otherwise treats it as part of the declaration, not a live node. A namespace kept in its own importable module doesn't need this; only code in *that* module is affected.

`server.read(device.setpoint)` after the two out-of-range writes comes back `100.0` and `0.0` — the clamp lives entirely in `SetpointImpl`, and it fires whether the write comes from this script, another process on the server, or a remote OPC UA client.

---

## What's next?

The next page pairs the same declare/implement split with a Method instead of a Variable.

- [Declare and implement an ObjectType](160_implement-objecttype.md) — the same pattern, for a Method's behaviour.
- [Declare a variable type](210_declare-variable-type.md) — the full `@o6.variabletype` story: engineering units, ranges, and typed values.
- [Variables with sources](320_variables-with-sources.md) — the instance-level alternative: `Server.implement(variable, read=..., write=...)` on one already-built Variable.
- [Server Variable Read/Write Override](../../examples/server-S09_implement_readwrite.md) — the runnable example this page is based on.
