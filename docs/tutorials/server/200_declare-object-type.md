# Declare an object type

So far every node in the distillery is built with one `addObject` or `addVariable` call at a time. A plant with a dozen stills would repeat the same calls for each one, and every copy would have to stay in sync. A declared ObjectType is a Python class, written with `@o6.objecttype`, that describes the shape of a distillery once. The server then builds as many instances as the plant needs.

This page builds `DistillingSystemType`, the hand-built distillery's shape as a type. It is a parallel technique on a fresh server and namespace, not a continuation of the running server. The result: `DistillingSystemType(...)` builds a whole hierarchy from one constructor call.

!!! info
    The reference server from [Set the Stage](../setup.md) keeps building its address space imperatively. It doesn't use the declared types from this page or the next three.

---

## Declare an ObjectType with `@o6.objecttype`

`@o6.objecttype` declares an `ObjectType` whose instances are full subtrees. The declaration carries no behaviour; [Declare and implement an ObjectType](160_implement-objecttype.md) pairs one with an implementer class.

A custom type needs a namespace. `o6.ns.namespace(...)` registers a shortname once, and the type's `nodeId=` references it.

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

A child is declared in two parts:

- The *instance* (`ns0.objtypes.FolderType(...)`) describes the child node.
- The *linker* (`o6.hasComponent(...)`) states the reference type that attaches it to the parent. It returns the instance unchanged, so you can annotate the class attribute with the child's concrete type (`identification: ns0.objtypes.FolderType`).

The `ns=distillery;...` qualifier on the BrowseName and NodeId puts the child into the distillery namespace.

The declaration is metadata. Nothing is added to a server until you instantiate it or publish it on one.

!!! info
    The decorators and linkers are part of the [declarative API](../../manual/information-model-authoring/publishing.md). See also [Writing a Nodeset in Python](../../manual/information-model-authoring/namespace-modules.md). Declared types and imperative `addX` calls mix freely on one server.

---

## Add typed Variables and Methods

Properties, Variables and Methods all attach with the same `o6.hasComponent` / `o6.hasProperty` linkers. For a Variable or Property, construct the concrete VariableType with its initial value, DataType and access level. For a Method, `o6.call(...)` describes the input and output arguments.

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

`value=` sets the initial value. `dataType=` takes a Python type (`str`, `float`, `bool`, or a declared `@o6.datatype`/`@o6.enumtype` class), and `o6` resolves it to the matching DataType. `accessLevel=1` is read-only and `accessLevel=3` is read-write.

Every child declared this way is Mandatory by default: every instance of `DistillingSystemType` gets it. To make a child optional, annotate it with `Optional[...]`:

```python
from typing import Optional

manufacturer: Optional[ns0.vartypes.PropertyType] = o6.hasProperty(
    ns0.vartypes.PropertyType(dataType=str)
)
```

Only the annotation sets optionality: `Optional[T]` gets the `Optional` ModellingRule, everything else gets `Mandatory`. There is no keyword for it. The rest of this page uses mandatory children.

Declare a Method with `o6.call(...)`. Its `inputArgs` and `outputArgs` are lists of `ns0.datatypes.Argument` descriptors, as in the imperative `addMethod` call:

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

The Method is declared but not implemented. [Declare and implement an ObjectType](160_implement-objecttype.md) shows how to add an implementer class.

---

## Instantiate the type on a server

Once a server has the namespace, constructing `DistillingSystemType(parent=...)` creates the entire subtree:

```python
import sys

server = Server(port=4840)
server.ns.append(sys.modules[__name__])     # publish this module's namespace on this server

# One constructor call → the full hierarchy
system = DistillingSystemType(parent=server.objectsNode, browseName="MainStill", server=server)

server.start()
```

`server.ns.append(...)` takes a module object, never a string. `sys.modules[__name__]` is the running script, which is enough for a single-file tutorial. A real namespace is usually its own importable module (`distillery_ns.py`), so a client process can `import distillery_ns` and decode the types too. See [Writing a Nodeset in Python](../../manual/information-model-authoring/namespace-modules.md#the-shape-of-a-namespace-module).

`DistillingSystemType(parent=..., browseName=...)` instantiates the type, attaches it to the parent and creates every mandatory child. The returned handle behaves like the imperative handle from the [hierarchy page](105_add-hierarchy.md): `system.name()` reads a leaf variable, `system.name(...)` writes it if it is writable, and attribute access browses children.

!!! warning
    Pass `server=server` explicitly when the namespace module is the running script, as here. o6 treats any constructor call inside a module that declared a namespace as part of that declaration, even after `server.start()` and even inside a function. Without `server=`, the call silently returns an inert declaration instead of a live node, and later reads such as `system.name()` fail with `AttributeError`. A namespace in its own importable module doesn't need this: a separate driver script that calls `distillery.DistillingSystemType(...)` gets a live node without the extra argument.

!!! info
    The instance does not inherit its BrowseName and NodeId from the type. Pass `browseName=` (and optionally `nodeId=`) to the constructor to set them.

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

Browsing `Objects/` shows `MainStill/Name`, `MainStill/Operating`, `MainStill/Setpoint` and `MainStill/Shutdown`, built by one constructor call instead of seven `addX` calls.

---

## Multiple instances, same type

Call the `DistillingSystemType(...)` constructor once per still:

```python
line_a = DistillingSystemType(parent=server.objectsNode, browseName="LineA", server=server)
line_b = DistillingSystemType(parent=server.objectsNode, browseName="LineB", server=server)
line_c = DistillingSystemType(parent=server.objectsNode, browseName="LineC", server=server)
```

Each call produces a complete, independent subtree. The shape lives in the type; state such as `Operating`, `Setpoint` and the cycle counter lives on each instance. All three stills have the same hierarchy and the same NodeId offsets within each instance, which dashboards and recipes rely on.

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

A client sees three independent objects, `LineA`, `LineB` and `LineC`, under `Objects/`. A fourth still is one more constructor call.

---

## Mix declared and imperative on the same server

Imperative `addObject` calls and declared instances can share one server. Clients cannot tell them apart:

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

Both end up in the same nodestore under `Objects/`. Most servers use declared types for what the model captures (devices, sensors, methods) and imperative calls for one-off configuration and operational state.

---

## Next steps

| Topic | What it covers |
|---|---|
| [Declare a variable type](210_declare-variable-type.md) | `@o6.variabletype` for typed values with their own `DataType` and `ValueRank`. |
| [Server manual](../../manual/information-model-authoring/publishing.md) | Every decorator, in depth, with a complete reference model. |
