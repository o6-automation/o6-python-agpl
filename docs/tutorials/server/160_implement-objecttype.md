# Declare and implement an ObjectType

This page applies the declare/implement split to a Method. You build `CycleCounterType`, a reusable batch counter like the distillery's `Status/Cycle`. Every instance the server builds from it dispatches Method calls to your implementation class.

---

## The pattern, once more

1. **Declare** the `ObjectType` and its Method with `@o6.objecttype` / `o6.call(...)`. No behaviour yet.
2. **Implement** the Method in a subclass, with `@o6.call("<name>")`. Ordinary instance attributes give each live node its own state.
3. **Register** with `server.implement(Declaration, Impl)`.

---

## Declare the type

`CycleCounterType` declares one Method, `Increment`, that takes an `Int32` step and returns the running `Int32` total. It uses the `distillery` namespace:

```python
import o6
from o6.ns import ns0

o6.ns.namespace(
    shortname="distillery",
    uri="http://o6-automation.com/UA/Distillery/",
    version="1.0",
)


@o6.objecttype(ns="distillery", nodeId="ns=distillery;i=7000", browseName="CycleCounterType")
class CycleCounterType(ns0.objtypes.BaseObjectType):
    """A batch counter — declared only, implemented separately below."""

    increment: o6.node.MethodNode = o6.hasComponent(
        o6.call(
            browseName="ns=distillery;Increment",
            nodeId="ns=distillery;i=7001",
            inputArgs=[
                ns0.datatypes.Argument(
                    name="step",
                    dataType=o6.Int32,
                    valueRank=o6.ValueRank.SCALAR,
                    description="Batches to add",
                )
            ],
            outputArgs=[
                ns0.datatypes.Argument(
                    name="total",
                    dataType=o6.Int32,
                    valueRank=o6.ValueRank.SCALAR,
                    description="Cycle count after incrementing",
                )
            ],
        )
    )
```

The class body declares only the Method's signature, not its behaviour.

---

## Implement the Method in a subclass

Subclass the declaration and bind behaviour to `Increment` with `@o6.call("Increment")`. The bare local name resolves against the type's declared Methods, so you don't need the qualified `ns=distillery;Increment`. Every live node gets its own `self._count`:

```python
from typing import Any

class CycleCounterImpl(CycleCounterType):
    """Track a running batch count per instance."""

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._count = 0

    @o6.call("Increment")
    def _increment(self, step: o6.Int32) -> tuple[o6.StatusCode, o6.Int32]:
        self._count += int(step)
        return (o6.StatusCode.GOOD, o6.Int32(self._count))
```

---

## Register and dispatch

```python
import sys
import time

server = o6.Server(port=4840)
server.ns.append(sys.modules[__name__])
server.implement(CycleCounterType, CycleCounterImpl)

counter = server.addObject(
    "BatchCounter",
    server.objectsNode,
    typeDefinition=CycleCounterType,
    nodeId="ns=distillery;i=7100",
    ns=o6.ns.distillery.index,
)

# In-process: calling the Method attribute runs CycleCounterImpl directly.
print(counter.Increment(o6.Int32(1)))    # (StatusCode.GOOD, Int32(1))
print(counter.Increment(o6.Int32(1)))    # (StatusCode.GOOD, Int32(2))

server.start()
print(f"Server running at {server.endpointUrl}")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pass

server.stop()
```

`addObject(typeDefinition=CycleCounterType, ...)` returns a `CycleCounterImpl` instance without naming that class at the call site. The in-process `counter.Increment(...)` and a remote client's `Call` request both dispatch to `CycleCounterImpl._increment` and share that instance's `_count`.

A second `addObject(typeDefinition=CycleCounterType, ...)` gets its own counter, starting at `0`. The behaviour lives on the type; the count lives on each instance.

---

## Next steps

| Topic | What it covers |
|---|---|
| [Declare an object type](200_declare-object-type.md) | Every decorator, modelling rule, and composition option `@o6.objecttype` supports. |
| [Method implementations](310_method-implementations.md) | The instance-level alternative: `Server.implement(method, call=...)` on one already-built Method. |
| [Server ObjectType Implementation](../../examples/server-S10_implement_objtype.md) | The runnable example this page is based on. |
