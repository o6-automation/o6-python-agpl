# Declare and implement an ObjectType

The previous page split a Variable into a declaration and a separate implementation. The same split applies to Methods, for the same reason: declare an `ObjectType` with a Method as a pure contract, implement its behaviour in a separate subclass, and register that class with `server.implement(Declaration, Impl)` so every instance the server builds dispatches to your code automatically. This page builds a `CycleCounterType` — the same idea behind the distillery's `Status/Cycle`, as a standalone reusable type.

---

## The pattern, once more

1. **Declare** the `ObjectType` and its Method with `@o6.objecttype` / `o6.call(...)`. No behaviour yet.
2. **Implement** the Method in a subclass, with `@o6.call("<name>")`. Ordinary instance attributes give each live node its own state.
3. **Register** with `server.implement(Declaration, Impl)`.

---

## Declare the type

`CycleCounterType` declares one Method, `Increment`, that takes an `Int32` step and returns the running `Int32` total. It reuses the same `distillery` namespace the rest of these tutorials register:

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

`Increment` is declared, not implemented — the class body only says what the Method's signature is.

---

## Implement the Method in a subclass

Subclass the declaration and bind Python behaviour to `Increment` with `@o6.call("Increment")` — the bare local name resolves against the type's declared Methods, so the qualified `ns=distillery;Increment` doesn't need spelling out here. Every live node gets its own `self._count`:

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

Both call paths — the in-process `counter.Increment(...)` above and a remote client's `Call` service request against the same Method — dispatch to `CycleCounterImpl._increment` and share the one instance's `_count`. `addObject(typeDefinition=CycleCounterType, ...)` hands back a fully-wired `CycleCounterImpl` instance; `CycleCounterImpl` itself is never named at the call site.

Add a second `addObject(typeDefinition=CycleCounterType, ...)` for a second still, and its counter starts independently at `0` — the shared behaviour lives on the type, the running count lives on each instance.

---

## What's next?

Declaration and implementation are two separate concerns from here on. The next pages go deep on the declaration side alone, and the "beyond the examples" pages later on cover the instance-level alternative to what these two pages just built.

- [Declare an object type](200_declare-object-type.md) — every decorator, modelling rule, and composition option `@o6.objecttype` supports.
- [Method implementations](310_method-implementations.md) — the instance-level alternative: `Server.implement(method, call=...)` on one already-built Method.
- [Server ObjectType Implementation](../../examples/server-S10_implement_objtype.md) — the runnable example this page is based on.
