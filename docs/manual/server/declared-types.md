# Declared types

The declarative route describes the model once, as Python classes, and lets the
server build the nodes. A *namespace module* is an ordinary Python module that
calls `o6.ns.namespace(...)` at the top and defines decorated classes below it:

```python
# plant.py
from typing import Optional

import o6
from o6.ns import ns0

o6.ns.namespace("plant", uri="http://example.org/Plant/", version="1.0")

@o6.enumtype(ns="plant", description="Machine state")
class MachineState:
    IDLE = 0
    RUNNING = 1
    FAULT = 2

@o6.variabletype(ns="plant", dataType=o6.Double, valueRank=o6.ValueRank.SCALAR)
class TemperatureType(ns0.vartypes.BaseDataVariableType):
    engineeringUnits: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(dataType=str)
    )
    highLimit: Optional[ns0.vartypes.PropertyType] = o6.hasProperty(
        ns0.vartypes.PropertyType(dataType=float)
    )

@o6.objecttype(ns="plant", nodeId="ns=plant;i=1001", browseName="MachineType")
class MachineType(ns0.objtypes.BaseObjectType):
    state: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(dataType=MachineState)
    )
    temperature: TemperatureType = o6.hasComponent(TemperatureType())
    reset: o6.node.MethodNode = o6.hasComponent(
        o6.call(
            browseName="ns=plant;Reset",
            inputArgs=[ns0.datatypes.Argument(
                name="mode", dataType=o6.Int32, valueRank=o6.ValueRank.SCALAR)],
            outputArgs=[ns0.datatypes.Argument(
                name="ok", dataType=o6.Boolean, valueRank=o6.ValueRank.SCALAR)],
        )
    )
```

The server publishes it, and from then on the classes *are* the API:

```python
import o6
import plant

server = o6.Server(port=4840)
server.ns.append(plant)
server.start()

machine = plant.MachineType(
    parent=server.objectsNode,
    browseName="M-101",
    nodeId="ns=plant;i=5001",
    values={"state": int(plant.MachineState.RUNNING)},
)

machine.state()                    # 1
machine.temperature(23.5)
machine.temperature.engineeringUnits()
```

`server.ns.append(module)` registers every namespace the module declared (from
its `__NAMESPACES__` metadata) and then injects its decorated nodes. Appending
the same module twice is a no-op. A module that mixes already-published
namespace URIs with new ones is rejected, and when a URI is already published
only the index alias is added — one address space holds one release of a given
namespace URI. For a single-file script, `server.ns.append(sys.modules[__name__])`
works, though a separate importable module is preferable because a client
process can import the same module and decode the types.

The decorators themselves — `@o6.datatype`, `@o6.enumtype`,
`@o6.referencetype`, `@o6.variabletype`, `@o6.objecttype`, field metadata,
declaration order, NodeId allocation, and `values=` seeding — are the subject of
[Writing a Nodeset in Python](../sdk-fundamentals/namespace/writing-nodesets-in-python.md).
Packaged companion specifications (DI, IA, and friends) are appended the same
way and are covered in
[Using Nodesets](../sdk-fundamentals/namespace/loading-and-using-nodesets.md). The
rest of this chapter covers the parts that belong to the *server* rather than to
the model.

## Declared type instance ownership

Calling an `@o6.objecttype` or `@o6.variabletype` class creates either a live
server node or an ordinary declaration instance. The optional `server` argument
is resolved in this order:

1. An explicit `server=<Server>` selects that server. An explicit
   `server=None` forces a declaration instance.
2. A live parent node selects the server that owns that node. A conflicting
   explicit server is rejected.
3. A declaration parent produces another declaration.
4. Calls made while a registered Python namespace module is being evaluated
   remain declarations; `server.ns.append(module)` materializes them later.
5. Otherwise, exactly one live server in the Python process is inferred.
6. With no live server, the result is a declaration. With multiple live servers,
   construction is ambiguous and raises `TypeError`; pass `server=` explicitly.

A bare `NodeId` does not identify a server. It therefore relies on the unique
live-server rule — and `server.objectsNode` is a `NodeId`, not a node handle:

```python
import o6

server = o6.Server()

# The only live server is inferred even though objectsNode is a NodeId.
motor = MotorType(parent=server.objectsNode, browseName="Motor")

# Always a normal declaration instance, regardless of live servers.
declaration = MotorType(server=None)
```

With a second live server in the process, the same call fails with
`cannot infer server: multiple live servers exist; pass server=<server> or
server=None explicitly`. Pass `server=server` and it succeeds again.

Namespace declarations remain ordinary Python objects even if a server exists:

```python
import sys

import o6
from o6.ns import ns0

o6.ns.namespace(shortname="plant", uri="urn:example:plant")
motors = ns0.objtypes.FolderType(parent=ns0.instances.objects, browseName="Motors")
server.ns.append(sys.modules[__name__])
```

## Views

Views are address-space instances, so they are declared with the `o6.view`
factory rather than a class decorator:

```python
productionView = o6.view(
    nodeId="ns=plant;i=5001",
    browseName="Production",
    containsNoLoops=True,
)
```

The default parent is the standard `Views` folder and the default reference is
`Organizes`. Server selection follows the same rules as other declared
instances: pass `server=` explicitly, let a live parent or the sole live server
select it, or use `server=None` to retain the declaration for a later
`server.ns.append(module)` call. `references=[...]` attaches existing
declarations to the View, and the remaining arguments (`displayName`,
`description`, `eventNotifier`, `writeMask`, `rolePermissions`,
`accessRestrictions`) map onto the corresponding attributes.

For a View created at runtime rather than declared in a model, use
[`server.addView`](address-space.md#objects-types-views-and-methods).

## Type child relationships

Children of an `@o6.variabletype` or `@o6.objecttype` are defined as node
instances first, then linked with one of two camel-case identity helpers:

```python
_name = ns0.vartypes.PropertyType(dataType=o6.String, browseName="Name")
_controller = ControllerType()
_reset = o6.call()

@o6.objecttype(nodeId="ns=plant;i=1001", browseName="MachineType")
class MachineType(ns0.objtypes.BaseObjectType):
    name: ns0.vartypes.PropertyType = o6.hasProperty(_name)
    controller: ControllerType = o6.hasComponent(_controller)
    reset: o6.node.MethodNode = o6.hasComponent(_reset)
```

`hasProperty` and `hasComponent` each take exactly one existing instance and
preserve its static type: an input of type `T` returns `T`. They work for
Variables, Objects, Methods, and their subtypes.

Beyond those two, `o6.organizes`, `o6.hasEventSource`, `o6.hasNotifier`,
`o6.hasOrderedComponent`, `o6.hasAddIn`, `o6.hasInterface`, `o6.hasCondition`,
`o6.generatesEvent`, and `o6.hasEncoding` cover the remaining standard
hierarchies. Each has an inverse form — `o6.propertyOf`, `o6.componentOf`,
`o6.organizedBy`, `o6.eventSourceOf`, `o6.notifierOf`,
`o6.orderedComponentOf`, `o6.addInOf`, `o6.interfaceOf`, `o6.isConditionOf`,
`o6.generatedBy` — that points the reference the other way. For a custom
ReferenceType, `o6.reference(instance, SomeReferenceType)` links through it, and
the three-argument form `o6.reference(source, SomeReferenceType, target)` adds
an edge between two *live* nodes immediately.

Optionality belongs to the relationship and is inferred exclusively from
`Optional[T]`:

```python
_componentName = ns0.vartypes.PropertyType(dataType=o6.LocalizedText)
componentName: Optional[ns0.vartypes.PropertyType] = o6.hasProperty(_componentName)

# The instance can also be left undefined.
documentation: Optional[ns0.vartypes.PropertyType] = o6.hasProperty(None)
```

Node constructors describe the node itself. They do not accept an `optional`
argument.

## Type interfaces

An ObjectType or VariableType implements OPC UA InterfaceTypes through the
decorator's `interfaces` argument:

```python
@o6.objecttype(
    nodeId="ns=plant;i=1001",
    browseName="MachineType",
    interfaces=[IMaintainableType, ns0.objtypes.IOrderedObjectType],
)
class MachineType(ns0.objtypes.BaseObjectType):
    pass
```

Interface markers are abstract ObjectTypes derived from
`ns0.objtypes.BaseInterfaceType`. Interfaces are OPC UA type metadata, not Python
mixins: they do not enter the implementing class's MRO and their members are
not copied into its class body. The server adds the `HasInterface` references
after all types in the module exist. Mandatory interface members are then
instantiated according to the normal OPC UA type-instantiation rules.

Properties owned directly by a DataType or EnumType are constructed before the
type and passed through the decorator's `children` argument:

```python
_enumStrings = ns0.vartypes.PropertyType(
    browseName="EnumStrings",
    value=[o6.LocalizedText("OFF"), o6.LocalizedText("ON")],
    dataType=o6.LocalizedText,
    valueRank=1,
)

@o6.enumtype(ns="plant", nodeId="ns=plant;i=1200", browseName="Mode")
class Mode(ns0.datatypes.Enumeration):
    enumStrings: ns0.vartypes.PropertyType = o6.hasProperty(_enumStrings)
    OFF = 0
    ON = 1
```

The relationship is declared on the type class, like other type children.
`o6.hasProperty` also keeps the linked node out of Python's enum member table.
These children are injected beneath the DataType node; they are not emitted as
free-standing instances with an explicit `parent` NodeId.
