# Declare a reference type

The last two pages put a name on the shape of things — a whole distillery, a single `Setpoint`. But not everything worth naming in an address space is a node; sometimes what matters most is how two nodes relate to each other, and `HasComponent`/`HasProperty` don't tell that whole story. Those two reference types carry most of the relationships in a typical OPC UA server — folders, sub-objects, variables under objects — because most relationships really are some form of "owns". A few aren't: a `Sensor` *monitors* a `Kettle`; a `Valve` *controls* a `Conveyor`; an `Alarm` *reports on* a `Reading`. Relationships like those deserve their own reference type, so the address space can say what's actually happening instead of forcing everything into an ownership shape it doesn't fit.

This page declares a `Monitors` reference type and uses it to attach a temperature sensor to the kettle — the still finally gets a sensor of its own, wired up with a reference that names exactly what it's doing there.

---

## Why custom reference types?

The default `Organizes` / `HasComponent` / `HasProperty` types are enough for "this folder contains this thing". A few situations want their own type:

- **Non-ownership edges.** A `Sensor` is not part of the kettle — it reads from it. `Monitors` describes the edge more honestly than `HasProperty`, and a `browse(reftype=Monitors)` finds the temperature sensor that way.
- **Type-safe browsing.** Knowing the distillery uses `Monitors` for sensor relationships lets you issue `browse(reftype=Monitors)` and get back exactly the sensors — no need to filter the entire hierarchy.
- **Semantic interoperability.** A companion specification that defines a `Controls` or `Supplies` reference type gives every server that uses it the same vocabulary. Tools that understand the vocabulary can present the relationships meaningfully.

The distillery doesn't strictly need a custom reference type — every node fits the standard edges — but adding one is the natural way to express "this sensor watches this kettle".

---

## Declare a reference type with `@o6.referencetype`

With the motivation out of the way, the declaration itself is small. `@o6.referencetype` declares a UA `ReferenceType` and optionally names the inverse direction. Python inheritance is the `HasSubtype` chain — the base class you derive from *is* the reference type's parent, with no implicit fallback:

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

`inverseName=` is the name visible when the relationship is followed in the opposite direction — the kettle sees the sensor as `MonitoredBy` while the sensor sees the kettle as `Monitors`. OPC UA requires an `InverseName` for non-symmetric, non-abstract reference types. For symmetric references (`symmetric=True`), the type reads the same in both directions and no InverseName is needed.

Here `MonitorsType` derives from `ns0.reftypes.NonHierarchicalReferences` (the catch-all for "not strictly ownership"), which is what makes it `MonitorsType`'s `HasSubtype` parent. Derive from `ns0.reftypes.HasComponent` or `ns0.reftypes.HasProperty` instead when the reference is a more specific kind of hierarchical edge — whatever Python base class you write becomes the parent, full stop.

A ReferenceType marker must have no annotated fields, and it is never instantiable.

---

## Attach a reference with `addReference`

Declaring `MonitorsType` doesn't connect anything on its own — a reference type only means something once it links two real nodes. The imperative route to adding an edge between two existing nodes is `Server.addReference(source, reftype, target, ...)`, matching the client contract. The distillery builds its sensors imperatively and links them to the kettle with `Monitors`:

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

`addReference(source, reftype, target)` attaches the edge. Both sides are existing nodes — the imperative call adds an edge between them, not a new node. `MonitorsType` here is the declared class itself; the equivalent NodeId string `"ns=distillery;i=4000"` works too.

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

Custom references compose with the declarative route the same way they compose with the imperative one: declare the leaf as an ordinary `HasComponent` child so it materialises with every instance, then attach the extra, meaningful edge between the two *live* children once the instance exists — with `server.addReference(...)` or the equivalent three-argument `o6.reference(source, SomeReferenceType, target)`:

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

Both `kettle` and `kettleTemperature` are declared as ordinary `HasComponent` children, so every `DistillingSystemType` instance gets both. The `Monitors` edge between them is not part of the type's shape — it is added once, on the live instance, exactly as in the imperative section above. `system.kettleTemperature` and `system.kettle` are live node handles by then, so `addReference` (and a plain dot-access read like `system.kettleTemperature()`) both work on them directly.

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

The instance has `MainStill/Kettle` and `MainStill/KettleTemperature` both linked with `HasComponent` — that is the type's shape — plus a `Monitors` edge from `KettleTemperature` to `Kettle` added on this particular instance. A `browse(reftype=MonitorsType, direction=INVERSE)` from `MainStill/Kettle` finds `KettleTemperature` back as `MonitoredBy`.

---

## What's next?

The sensor now has a name for what it's doing to the kettle, not just a place in the tree. One piece is still missing from this tour of declaring things up front: a way to describe the values themselves, beyond the handful of numbers and strings OPC UA already knows.

- [Declare a data type](230_declare-data-type.md) — `@o6.datatype` for a custom `Structure`, and `@o6.enumtype` for a closed set of named values, used by your variables and methods.
- [Writing a Nodeset in Python](../../manual/sdk-fundamentals/namespace/writing-nodesets-in-python.md#o6referencetype-custom-references) — symmetric vs. asymmetric, abstract vs. concrete, and reference-type hierarchies.
