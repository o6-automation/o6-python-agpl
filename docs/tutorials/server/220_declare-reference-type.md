# Declare a reference type

A reference type names how two nodes relate. `HasComponent` and `HasProperty` carry most relationships in an OPC UA server, and both mean some form of "owns". Some relationships are not ownership: a `Sensor` monitors a `Kettle`, a `Valve` controls a `Conveyor`, an `Alarm` reports on a `Reading`. Give those their own reference type.

This page declares a `Monitors` reference type and uses it to attach a temperature sensor to the kettle.

---

## Why custom reference types?

The standard `Organizes`, `HasComponent` and `HasProperty` types cover "this folder contains this thing". Use a custom type for:

- **Non-ownership edges.** A `Sensor` is not part of the kettle; it reads from it. `Monitors` describes that edge more accurately than `HasProperty`.
- **Targeted browsing.** `browse(reftype=Monitors)` returns exactly the sensors, without filtering the whole hierarchy.
- **Shared vocabulary.** A companion specification that defines a `Controls` or `Supplies` reference type gives every server that uses it the same terms, so tools that know them can present the relationships.

The distillery would work with the standard edges alone. `Monitors` states "this sensor watches this kettle" directly.

---

## Declare a reference type with `@o6.referencetype`

`@o6.referencetype` declares an OPC UA `ReferenceType` and optionally names the inverse direction. Python inheritance is the `HasSubtype` chain: the base class is the reference type's parent, with no implicit fallback.

```python
import o6
from o6.ns import ns0

o6.ns.namespace(
    shortname="distillery",
    uri="http://o6-automation.com/UA/Distillery/",
    version="1.0",
)


@o6.referencetype(
    ns="distillery",
    nodeId="ns=distillery;i=4000",
    browseName="Monitors",
    inverseName="MonitoredBy",
)
class MonitorsType(ns0.reftypes.NonHierarchicalReferences):
    """A sensor that watches a piece of equipment."""
```

`inverseName=` names the relationship in the opposite direction: the sensor `Monitors` the kettle, and the kettle is `MonitoredBy` the sensor. OPC UA requires an `InverseName` for non-symmetric, non-abstract reference types. A symmetric reference (`symmetric=True`) reads the same in both directions and needs no InverseName.

`MonitorsType` derives from `ns0.reftypes.NonHierarchicalReferences`, the parent for edges that are not ownership. For a more specific kind of hierarchical edge, derive from `ns0.reftypes.HasComponent` or `ns0.reftypes.HasProperty` instead.

A ReferenceType marker must have no annotated fields, and it is never instantiable.

---

## Attach a reference with `addReference`

A declared reference type connects nothing until you use it to link two nodes. `Server.addReference(source, reftype, target, ...)` adds an edge between two existing nodes, with the same contract as on the client. The distillery builds its sensor imperatively and links it to the kettle with `Monitors`:

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


@o6.referencetype(
    ns="distillery",
    nodeId="ns=distillery;i=4000",
    browseName="Monitors",
    inverseName="MonitoredBy",
)
class MonitorsType(ns0.reftypes.NonHierarchicalReferences):
    pass


server = Server(port=4840)
server.ns.append(sys.modules[__name__])

# Imperative skeleton
distilling_system = server.addObject("DistillingSystem", server.objectsNode, nodeId="ns=1;i=1000")
kettle = server.addObject("Kettle", distilling_system, nodeId="ns=1;i=1300")
sensors = server.addObject("Sensors", distilling_system, nodeId="ns=1;i=1700")
sensor = server.addVariable("KettleTemp", sensors, 20.0, nodeId="ns=1;i=1701")

# Custom reference: the sensor monitors the kettle
server.addReference(source=sensor, reftype=MonitorsType, target=kettle)

server.start()
```

`addReference` adds an edge, not a node. Pass the declared class as `reftype`, or its NodeId string `"ns=distillery;i=4000"`.

`browse(reftype=MonitorsType)` from the kettle finds `KettleTemp`, and `browse(reftype=MonitorsType, direction=INVERSE)` from `KettleTemp` finds the kettle back as `MonitoredBy`.

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


@o6.referencetype(
    ns="distillery",
    nodeId="ns=distillery;i=4000",
    browseName="Monitors",
    inverseName="MonitoredBy",
)
class MonitorsType(ns0.reftypes.NonHierarchicalReferences):
    pass


server = Server(port=4840)
server.ns.append(sys.modules[__name__])

distilling_system = server.addObject("DistillingSystem", server.objectsNode, nodeId="ns=1;i=1000")
kettle = server.addObject("Kettle", distilling_system, nodeId="ns=1;i=1300")
sensors = server.addObject("Sensors", distilling_system, nodeId="ns=1;i=1700")
sensor = server.addVariable("KettleTemp", sensors, 20.0, nodeId="ns=1;i=1701")

server.addReference(source=sensor, reftype=MonitorsType, target=kettle)

server.start()
```

---

## Reference types on a declared type

With a declared ObjectType, declare both children as ordinary `HasComponent` children so every instance gets them. After you create the instance, attach the custom edge between the two live children with `server.addReference(...)` or the equivalent three-argument `o6.reference(source, SomeReferenceType, target)`:

```python
@o6.objecttype(ns="distillery", nodeId="ns=distillery;i=1000", browseName="DistillingSystemType")
class DistillingSystemType(ns0.objtypes.BaseObjectType):
    kettle: ns0.objtypes.BaseObjectType = o6.hasComponent(
        ns0.objtypes.BaseObjectType(
            browseName="ns=distillery;Kettle",
            nodeId="ns=distillery;i=1300",
        )
    )
    kettleTemperature: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            browseName="ns=distillery;KettleTemperature",
            nodeId="ns=distillery;i=1701",
            dataType=float,
            value=20.0,
        )
    )


system = DistillingSystemType(parent=server.objectsNode, browseName="MainStill", server=server)

# The sensor monitors the kettle — attached once both live nodes exist.
server.addReference(source=system.kettleTemperature, reftype=MonitorsType, target=system.kettle)
```

The `Monitors` edge is not part of the type's shape. It exists only on this instance. `system.kettleTemperature` and `system.kettle` are live node handles, so `addReference` and dot-access reads such as `system.kettleTemperature()` work on them directly.

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


@o6.referencetype(
    ns="distillery",
    nodeId="ns=distillery;i=4000",
    browseName="Monitors",
    inverseName="MonitoredBy",
)
class MonitorsType(ns0.reftypes.NonHierarchicalReferences):
    pass


@o6.objecttype(ns="distillery", nodeId="ns=distillery;i=1000", browseName="DistillingSystemType")
class DistillingSystemType(ns0.objtypes.BaseObjectType):
    kettle: ns0.objtypes.BaseObjectType = o6.hasComponent(
        ns0.objtypes.BaseObjectType(
            browseName="ns=distillery;Kettle",
            nodeId="ns=distillery;i=1300",
        )
    )
    kettleTemperature: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            browseName="ns=distillery;KettleTemperature",
            nodeId="ns=distillery;i=1701",
            dataType=float,
            value=20.0,
        )
    )


server = Server(port=4840)
server.ns.append(sys.modules[__name__])
system = DistillingSystemType(parent=server.objectsNode, browseName="MainStill", server=server)
server.addReference(source=system.kettleTemperature, reftype=MonitorsType, target=system.kettle)
server.start()
```

The instance has `MainStill/Kettle` and `MainStill/KettleTemperature`, both linked with `HasComponent`, plus a `Monitors` edge from `KettleTemperature` to `Kettle`. A `browse(reftype=MonitorsType, direction=INVERSE)` from `MainStill/Kettle` finds `KettleTemperature` back as `MonitoredBy`.

---

## Next steps

| Topic | What it covers |
|---|---|
| [Declare a data type](230_declare-data-type.md) | `@o6.datatype` for a custom `Structure`, and `@o6.enumtype` for a closed set of named values, used by your variables and methods. |
| [Writing a Nodeset in Python](../../manual/information-model-authoring/references-and-instances.md#o6referencetype-custom-references) | Symmetric vs. asymmetric, abstract vs. concrete, and reference-type hierarchies. |
