# Declaring ReferenceTypes & Model Instances

Declare custom relationships and instances to publish with a namespace module.
Declaration blocks are optional additions to `plant.py`, using its imports
and registered namespace. Runtime usage is labeled separately.

## `@o6.referencetype` — custom references

A ReferenceType is address-space metadata only: it has no `UA_DataType`, no encoding and no instances. The marker class carries the NodeId, BrowseName, `InverseName`, `Symmetric` and `IsAbstract` that the server publishes. Python inheritance is the `HasSubtype` chain.

```python
@o6.referencetype(
    ns="plant",
    browseName="Feeds",
    inverseName="IsFedBy",
    description="Conveyor Feeds Machine",
)
class Feeds:
    pass
```

A ReferenceType marker must have no annotated fields and cannot be instantiated.
In a runtime script that has published `plant`, imported `Feeds` from it, and
created `conveyor` and `machine` nodes, either of these alternative calls adds
the reference:

```python
o6.reference(conveyor, Feeds, machine)          # between two live nodes
server.addReference(source=conveyor, reftype=Feeds, target=machine)   # equivalently
```

---

## Views

Views are address-space instances. Declare them with the `o6.view` factory, not
a class decorator:

```python
productionView = o6.view(
    nodeId="ns=plant;i=4001",
    browseName="Production",
    containsNoLoops=True,
)
```

The default parent is the standard `Views` folder and the default reference is
`Organizes`. Server selection follows the
[instance ownership rules](publishing.md#declared-type-instance-ownership): pass `server=`, let a live
parent or the sole live server select it, or pass `server=None` to keep the
declaration for a later `server.ns.append(module)`. `references=[...]` attaches
existing declarations to the View. The remaining arguments (`displayName`,
`description`, `eventNotifier`, `writeMask`, `rolePermissions`,
`accessRestrictions`) configure node metadata and access rules. See
[Access restrictions](../server/security.md#access-restrictions) for enforcement
and Attribute read/write limitations.

To create a View at runtime, use
[`server.addView`](../server/address-space.md#objects-types-views-and-methods).

## Model instances

Add instance declarations to the namespace module when they should be published
with the model. For example, this fragment adds a folder beneath Objects:

```python
motors = ns0.objtypes.FolderType(
    parent=ns0.instances.objects, browseName="Motors",
)
```

Construction during namespace module evaluation produces a declaration.
`server.ns.append(plant)` later publishes it on the selected server. Runtime
construction and ownership are covered in
[Publishing & Instantiating Models](publishing.md).
