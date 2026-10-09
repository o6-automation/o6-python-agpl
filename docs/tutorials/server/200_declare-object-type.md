# Declare an object type

Every node in the distillery so far — the folders, the `Setpoint`, the `Heater`, the `Shutdown` method — was built by calling `addObject` or `addVariable` one at a time, by hand. That's been perfectly fine for one still. But picture the plant this server stands in for: not one still, but a dozen of them on the same floor, each with its own kettle, its own setpoint, its own sensors. Building each one by hand would mean repeating the same sequence of calls over and over, and trusting every copy stays in sync with the others. That's the problem a **declared ObjectType** solves: a Python class, written with `@o6.objecttype`, that describes the shape of a distillery once and lets the server produce as many instances of it as the plant needs.

This page builds that class — `DistillingSystemType` — as the same shape as the hand-built distillery, just described as a type instead of assembled call by call. It's worth being upfront about what this is: a parallel technique, not a continuation of the exact running server from the earlier pages. By the end, `DistillingSystemType(...)` produces a whole hierarchy from a single constructor call, but on a fresh server and namespace of its own.

!!! info
    The reference server from [Set the Stage](../setup.md) (`examples/tutorial-server/server.py`) keeps building its address space imperatively — it doesn't switch to any of the declared types this page or the next three introduce. This band is a look at an alternative, more scalable way to model the same shape; the running example itself doesn't change.

---

## Declare an ObjectType with `@o6.objecttype`

`@o6.objecttype` declares a UA `ObjectType` whose instances are full subtrees. The declaration carries no behaviour — [Declare and implement an ObjectType](160_implement-objecttype.md), earlier in these tutorials, pairs a declaration like this one with a separate implementer class. For now, the type describes what every `DistillingSystem` looks like.

A custom type needs a namespace to live in. `o6.ns.namespace(...)` registers a shortname once; that shortname is what the type's `nodeId=` references.

```python
import time
import o6
from o6 import Server
from o6.ns import ns0

# Register the distillery namespace once at module load
o6.ns.namespace(
    shortname="distillery",
    uri="http://o6-automation.com/UA/Distillery/",
    version="1.0",
)


@o6.objecttype(ns="distillery", nodeId="ns=distillery;i=1000", browseName="DistillingSystemType")
class DistillingSystemType(ns0.objtypes.BaseObjectType):
    """The complete distillery — one folder with six sub-objects."""

    identification: ns0.objtypes.FolderType = o6.hasComponent(
        ns0.objtypes.FolderType(
            browseName="ns=distillery;Identification",
            nodeId="ns=distillery;i=1100",
        )
    )
```

`@o6.objecttype` turns the class body into a UA ObjectType declaration. A child is declared in two parts: the **instance** (`ns0.objtypes.FolderType(...)`) describes the child node itself, and the **linker** (`o6.hasComponent(...)`) states the reference type that attaches it to the parent and returns the instance unchanged — which is why the class attribute can be annotated with the child's concrete type (`identification: ns0.objtypes.FolderType`). The BrowseName and NodeId are qualified with `ns=distillery;...`, which is what tells `o6` to put the child into our namespace.

The declaration *itself* is just metadata: nothing is added to a server until you instantiate it or publish it on one.

!!! info
    The decorators and their linkers are part of the [declarative API](../../manual/server/declared-types.md) — the same model-driven route the manual covers in depth, alongside [Writing a Nodeset in Python](../../manual/sdk-fundamentals/namespace/writing-nodesets-in-python.md). These tutorials use it alongside the imperative `addX` calls from earlier pages; the two mix freely on one server.

---

## Add typed Variables and Methods

A folder by itself doesn't get us far — the distillery still needs values inside it, and at least one thing it can be told to do. Children of an ObjectType use the same `o6.hasComponent` / `o6.hasProperty` linkers regardless of whether the child is a Property, a Variable, or a Method. For a leaf Variable or Property you construct the concrete VariableType directly with its initial value, DataType, and access level; for a Method, `o6.call(...)` describes the input and output argument shape.

```python
@o6.objecttype(ns="distillery", nodeId="ns=distillery;i=1000", browseName="DistillingSystemType")
class DistillingSystemType(ns0.objtypes.BaseObjectType):
    identification: ns0.objtypes.FolderType = o6.hasComponent(
        ns0.objtypes.FolderType(
            browseName="ns=distillery;Identification",
            nodeId="ns=distillery;i=1100",
        )
    )

    # Declared directly on the type for this tutorial; nesting it under
    # `identification` instead would use the same composition pattern —
    # a further ObjectType with its own `name` child, attached the same way.
    name: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            browseName="ns=distillery;Name",
            nodeId="ns=distillery;i=1101",
            dataType=str,
            value="Distilling Demo Still",
            accessLevel=1,                   # read-only
        )
    )
```

`value=` seeds the child's initial value; `dataType=` takes the Python type directly (`str`, `float`, `bool`, or a declared `@o6.datatype`/`@o6.enumtype` class) and `o6` resolves it to the matching UA DataType. Both `accessLevel=1` (read-only) and `accessLevel=3` (read-write) are accepted.

Every child declared this way is **Mandatory** by default — every instance of `DistillingSystemType` gets it. To make a child optional, annotate it with `Optional[...]` instead:

```python
from typing import Optional

manufacturer: Optional[ns0.vartypes.PropertyType] = o6.hasProperty(
    ns0.vartypes.PropertyType(dataType=str)
)
```

Optionality belongs entirely to the annotation — `Optional[T]` gets the `Optional` ModellingRule, everything else is `Mandatory`. There is no separate keyword for it. Most distillery leaves are mandatory, so the plain (non-`Optional`) form is what the rest of this page uses.

A Method uses `o6.call(...)` for its declaration, with `inputArgs` and `outputArgs` lists of `ns0.datatypes.Argument` descriptors exactly as the imperative `addMethod` call uses them:

```python
@o6.objecttype(ns="distillery", nodeId="ns=distillery;i=1000", browseName="DistillingSystemType")
class DistillingSystemType(ns0.objtypes.BaseObjectType):
    # ... leaves as above ...

    shutdown: o6.node.MethodNode = o6.hasComponent(
        o6.call(
            browseName="ns=distillery;Shutdown",
            nodeId="ns=distillery;i=2002",
        )
    )
```

The Method is *declared* with `o6.call(...)` but left unimplemented here. Pairing a declaration like this one with a separate implementer class is the subject of [Declare and implement an ObjectType](160_implement-objecttype.md), earlier in these tutorials — worth a look now if you skipped straight here.

---

## Instantiate the type on a server

The type is fully declared now — folder, values, an unimplemented method — but none of it exists on any server yet. Once a server has the namespace, constructing `DistillingSystemType(parent=...)` materialises the entire subtree:

```python
import sys

server = Server(port=4840)
server.ns.append(sys.modules[__name__])     # publish this module's namespace on this server

# One constructor call → the full hierarchy
system = DistillingSystemType(parent=server.objectsNode, browseName="MainStill", server=server)

server.start()
```

`server.ns.append(...)` takes a **module object**, never a string — `sys.modules[__name__]` is the running script itself, which is enough for a single-file tutorial. A real namespace is usually its own importable module (`distillery_ns.py`) so a client process can `import distillery_ns` and decode the types too; see [Writing a Nodeset in Python](../../manual/sdk-fundamentals/namespace/writing-nodesets-in-python.md#the-shape-of-a-namespace-module).

`DistillingSystemType(parent=..., browseName=...)` instantiates the type and attaches it to the parent; the constructor takes care of every mandatory child node. The returned handle behaves like the imperative handle from the [hierarchy page](105_add-hierarchy.md) — `system.name()` reads a leaf variable, `system.name(...)` would write it if it were writable, attribute access browses children.

!!! warning
    Pass `server=server` explicitly whenever the namespace module *is* the running script, as it is here. o6 treats any constructor call still running inside a module that declared a namespace as part of that declaration — even after `server.start()`, even from inside a function — so without an explicit `server=`, the call silently returns an inert declaration instead of a live node, and every later `system.name()`-style read fails with an `AttributeError`. A namespace kept in its own importable module doesn't need this: only code in *that* module is affected, so a separate driver script instantiating `distillery.DistillingSystemType(...)` gets a live node with no extra argument.

!!! info
    The instance BrowseName and NodeId are *not* inherited from the type. The type declares the shape; the instance owns its own identity on the server. Pass `browseName=` (and optionally `nodeId=`) to the constructor to pin them.

#### Putting it all together

```python
import sys
import time
import o6
from o6 import Server
from o6.ns import ns0

o6.ns.namespace(
    shortname="distillery",
    uri="http://o6-automation.com/UA/Distillery/",
    version="1.0",
)


@o6.objecttype(ns="distillery", nodeId="ns=distillery;i=1000", browseName="DistillingSystemType")
class DistillingSystemType(ns0.objtypes.BaseObjectType):
    name: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            browseName="ns=distillery;Name",
            nodeId="ns=distillery;i=1101",
            dataType=str,
            value="Distilling Demo Still",
            accessLevel=1,
        )
    )

    operating: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            browseName="ns=distillery;Operating",
            nodeId="ns=distillery;i=1203",
            dataType=bool,
            value=True,
            accessLevel=3,                # read-write
        )
    )

    setpoint: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            browseName="ns=distillery;Setpoint",
            nodeId="ns=distillery;i=1204",
            dataType=float,
            value=85.0,
            accessLevel=3,
        )
    )

    shutdown: o6.node.MethodNode = o6.hasComponent(
        o6.call(
            browseName="ns=distillery;Shutdown",
            nodeId="ns=distillery;i=2002",
        )
    )


server = Server(port=4840)
server.ns.append(sys.modules[__name__])
system = DistillingSystemType(parent=server.objectsNode, browseName="MainStill", server=server)
server.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pass

server.stop()
```

A read of `Objects/` returns exactly the same tree the imperative version built — `MainStill/Name`, `MainStill/Operating`, `MainStill/Setpoint`, `MainStill/Shutdown` — but it was built by one constructor call rather than seven `addX` calls.

---

## Multiple instances, same type

The whole point of a declared type is reuse. The same `DistillingSystemType(...)` constructor can be called as many times as the plant has stills:

```python
line_a = DistillingSystemType(parent=server.objectsNode, browseName="LineA", server=server)
line_b = DistillingSystemType(parent=server.objectsNode, browseName="LineB", server=server)
line_c = DistillingSystemType(parent=server.objectsNode, browseName="LineC", server=server)
```

Each call produces a complete, independent subtree. The shared shape lives in the type; the per-instance state (current `Operating`, current `Setpoint`, current cycle counter) lives on each instance. The three stills look identical from the outside — same hierarchy, same `NodeId` offsets within each instance — which is exactly what dashboards and recipes rely on.

#### Putting it all together

```python
import sys
import time
import o6
from o6 import Server
from o6.ns import ns0

o6.ns.namespace(
    shortname="distillery",
    uri="http://o6-automation.com/UA/Distillery/",
    version="1.0",
)


@o6.objecttype(ns="distillery", nodeId="ns=distillery;i=1000", browseName="DistillingSystemType")
class DistillingSystemType(ns0.objtypes.BaseObjectType):
    name: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            browseName="ns=distillery;Name",
            nodeId="ns=distillery;i=1101",
            dataType=str,
            value="Distilling Demo Still",
            accessLevel=1,
        )
    )
    operating: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            browseName="ns=distillery;Operating",
            nodeId="ns=distillery;i=1203",
            dataType=bool,
            value=True,
            accessLevel=3,
        )
    )
    setpoint: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            browseName="ns=distillery;Setpoint",
            nodeId="ns=distillery;i=1204",
            dataType=float,
            value=85.0,
            accessLevel=3,
        )
    )


server = Server(port=4840)
server.ns.append(sys.modules[__name__])
DistillingSystemType(parent=server.objectsNode, browseName="LineA", server=server)
DistillingSystemType(parent=server.objectsNode, browseName="LineB", server=server)
DistillingSystemType(parent=server.objectsNode, browseName="LineC", server=server)
server.start()
```

A client connecting now sees three independent `LineA`, `LineB`, `LineC` objects under `Objects/`, each with the same shape — and adding a fourth means one extra constructor call.

---

## Mix declared and imperative on the same server

The two routes are not mutually exclusive. Imperative `addObject` calls and declared instances can sit next to each other on the same server, and clients cannot tell which is which:

```python
import sys

server = Server(port=4840)

# Imperative
scratch = server.addObject("Scratch", server.objectsNode, nodeId="ns=1;s=Scratch")
server.addVariable("Counter", scratch, 0, nodeId="ns=1;s=Counter")

# Declarative
server.ns.append(sys.modules[__name__])
DistillingSystemType(parent=server.objectsNode, browseName="MainStill", server=server)

server.start()
```

Both end up in the same nodestore, browsable from the same `Objects/`. Most real servers mix the two: declarative types for the things the model captures (devices, sensors, methods), imperative helpers for one-off configurations and operational state.

---

## What's next?

The distillery itself is now a typed class — something the server can produce on demand instead of assembling by hand, node by node. The same idea, that a type can carry shape and metadata once instead of repeating it on every instance, works just as well one level down, on a single value rather than a whole hierarchy.

- [Declare a variable type](210_declare-variable-type.md) — `@o6.variabletype` for typed values with their own `DataType` and `ValueRank`.
- [Server manual](../../manual/server/declared-types.md) — every decorator, in depth, with a complete reference model.
