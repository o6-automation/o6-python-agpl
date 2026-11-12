# Declare and implement a Variable

So far each Variable's behaviour comes from its own `addVariable` call. With fifty stills, fifty calls have to agree on what a Setpoint looks like. Instead, declare the shape once as a type and implement its behaviour once.

The goal: a `Setpoint` that clamps out-of-range writes to `[0.0, 100.0]`. You declare an `ObjectType` that owns a `Setpoint` Variable and implement its read and write behaviour in a separate Python class. Every object the server builds from that type gets the behaviour, with no per-instance callbacks. [Variables with sources](320_variables-with-sources.md) builds the same clamp with `read=`/`write=` callbacks on one existing Variable node.

This page introduces only as much of `@o6.objecttype` as the pattern needs. The [declared-types pages](200_declare-object-type.md) cover declarations in depth.

---

## The pattern has three parts

1. **Declare** a UA `ObjectType` with a Variable child as a pure contract, with `@o6.objecttype`. The declaration carries no behaviour.
2. **Implement** that contract in a separate subclass. `@o6.read("<member>")` and `@o6.write("<member>")` bind Python behaviour to the declared Variable, by its Python attribute name.
3. **Register** the implementation with `server.implement(Declaration, Impl)` so the server uses it whenever it builds an instance of that type.

---

## Declare the type

A declared type needs a namespace. Register the shortname once, then reference it as `ns="distillery"`. `SetpointType` declares one readable and writable (`accessLevel=3`) Variable child, `setpoint`, with no behaviour:

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

A declaration on its own is metadata. Instantiated now, every instance would get the default, unclamped storage behaviour.

---

## Implement read and write in a subclass

Subclass the declaration and bind behaviour to `setpoint` by its Python attribute name, not by its BrowseName. The value lives in an ordinary instance attribute, `self._value`, so the write callback can validate before storing:

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

Both callbacks receive keyword-only context (`session`, `range`, and `includeSourceTimestamp` for reads), which this example ignores via `**kwargs`. This write callback clamps instead of rejecting. [Variables with sources](320_variables-with-sources.md) shows the alternative: rejecting out-of-range writes with `BAD_OUT_OF_RANGE`.

---

## Register and instantiate

`server.implement(SetpointType, SetpointImpl)` makes `SetpointImpl` the class the server uses whenever it builds a `SetpointType` instance. After that, `addObject(typeDefinition=SetpointType, ...)` returns a live object with the behaviour attached. The call site never names `SetpointImpl`.

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
    Pass `server=server` explicitly if a constructor call runs in the same script that declared the namespace. Otherwise o6 treats it as part of the declaration, not a live node. This affects only code in the module that declares the namespace; a namespace in its own importable module doesn't need it.

After the two out-of-range writes, `server.read(device.setpoint)` returns `100.0` and `0.0`. The clamp lives in `SetpointImpl` and applies whether the write comes from this script, another process on the server or a remote OPC UA client.

---

## Next steps

| Topic | What it covers |
|---|---|
| [Declare and implement an ObjectType](160_implement-objecttype.md) | The same pattern, for a Method's behaviour. |
| [Declare a variable type](210_declare-variable-type.md) | The full `@o6.variabletype` story: engineering units, ranges, and typed values. |
| [Variables with sources](320_variables-with-sources.md) | The instance-level alternative: `Server.implement(variable, read=..., write=...)` on one already-built Variable. |
| [Server Variable Read/Write Override](../../examples/server-S09_implement_readwrite.md) | The runnable example this page is based on. |
