# Declaring ObjectTypes & VariableTypes

Describe a reusable node hierarchy with typed children and Methods.
The examples extend the `plant.py` module from
[Writing a Namespace Module](namespace-modules.md); add declarations in the order shown.

## `@o6.variabletype` — typed Variables

A VariableType constrains a Variable's value and declares the children every Variable of that type gets. The value constraints are decorator arguments:

```python
@o6.variabletype(
    ns="plant",
    dataType=o6.Double,
    valueRank=o6.ValueRank.SCALAR,
    description="A temperature in degrees Celsius",
)
class TemperatureType(ns0.vartypes.BaseDataVariableType):
    engineeringUnits: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(dataType=str, description="unit symbol")
    )
    highLimit: Optional[ns0.vartypes.PropertyType] = o6.hasProperty(
        ns0.vartypes.PropertyType(dataType=float)
    )
```

- `dataType=`, `valueRank=`, `arrayDimensions=` describe the value. If omitted, they are inherited from the base VariableType, not reset to `BaseDataType`/`ANY`. OPC UA requires a subtype's constraints to be equal to or narrower than its parent's.
- `value=` seeds a default value on the type node itself.
- `isAbstract=True` makes the type non-instantiable.
- `interfaces=[...]` adds `HasInterface` references (see [Type interfaces](#type-interfaces)).

Most VariableTypes derive from `ns0.vartypes.BaseDataVariableType`. Use `ns0.vartypes.PropertyType` as base and as child type for metadata that describes another node instead of carrying process data.

### Children

Declare a child by annotating a class attribute with the child's concrete type and assigning a linked instance of that type:

```python
@o6.variabletype(ns="plant", description="Inlet/outlet temperature pair")
class ThermalProfileType(ns0.vartypes.BaseDataVariableType):
    inlet: TemperatureType = o6.hasComponent(TemperatureType())
    outlet: TemperatureType = o6.hasComponent(TemperatureType())
```

Each line has two parts:

- **The instance** (`TemperatureType()`) describes the child node: its BrowseName, DataType, AccessLevel and default value. Constructed inside a namespace module with no live server, it is a declaration.
- **The linker** (`o6.hasComponent` / `o6.hasProperty`) sets the ReferenceType that attaches the child to the parent. Each linker takes one instance and returns it unchanged, so the type checker sees `profile.inlet` as a `TemperatureType`.

Other linkers:

- `o6.organizes`, `o6.hasEventSource`, `o6.hasNotifier`, `o6.hasOrderedComponent`, `o6.hasAddIn`, `o6.hasInterface`, `o6.hasCondition` and `o6.generatesEvent` cover the remaining standard hierarchies.
- The inverse forms (`o6.componentOf`, `o6.propertyOf`, `o6.organizedBy`, …) point the reference the other way.
- `o6.reference(instance, SomeReferenceType)` links through any custom ReferenceType.

**Optionality belongs to the relationship.** It is inferred only from `Optional[T]` in the annotation: an `Optional[T]` child gets the `Optional` ModellingRule, every other child is `Mandatory`. Node constructors have no `optional` argument. The following class-body fragment declares a relationship without an instance:

```python
documentation: Optional[ns0.vartypes.PropertyType] = o6.hasProperty(None)
```

---

## `@o6.objecttype` — typed Objects

An ObjectType works like a VariableType, with Object children and Methods added. Children, linkers and optionality work the same way.

```python
@o6.objecttype(ns="plant", description="A servo drive")
class DriveType(ns0.objtypes.BaseObjectType):
    manufacturer: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(dataType=str)
    )
    current: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(dataType=float, description="motor current [A]")
    )


@o6.objecttype(ns="plant", description="A machine with a drive and a temperature")
class MachineType(ns0.objtypes.BaseObjectType):
    state: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(dataType=o6.Int32)
    )
    temperature: TemperatureType = o6.hasComponent(TemperatureType())
    drive: DriveType = o6.hasComponent(DriveType())
    reset: o6.node.MethodNode = o6.hasComponent(
        o6.call(
            browseName="ns=plant;Reset",
            inputArgs=[
                ns0.datatypes.Argument(
                    name="mode", dataType=o6.Int32, valueRank=o6.ValueRank.SCALAR
                )
            ],
            outputArgs=[
                ns0.datatypes.Argument(
                    name="ok", dataType=o6.Boolean, valueRank=o6.ValueRank.SCALAR
                )
            ],
        )
    )
```

`state`, `temperature` and `drive` show the three kinds of child: a leaf Property, a complex Variable and a complex Object. `reset` is a Method declaration: `o6.call(...)` with `inputArgs`/`outputArgs` describes only the signature. You supply the behavior separately; see [Implementing Object Behavior](implementing-types.md).

Subtyping is Python inheritance. A subtype inherits every child of its base:

```python
@o6.objecttype(ns="plant", description="A CNC machine")
class CncMachineType(MachineType):
    serial: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(dataType=str))
```

`CncMachineType` has `state`, `temperature`, `drive`, `Reset` and `serial`.

An ObjectType can declare an `__init__`. It runs on the fully constructed node, so `super().__init__(**kwargs)` is an ordinary cooperative Python call and does no OPC UA work:

```python
@o6.objecttype(ns="plant")
class PumpType(ns0.objtypes.BaseObjectType):
    def __init__(self, *, device=None, **kwargs):
        super().__init__(**kwargs)
        self.device = device
```

---

## Type interfaces

The following is an alternative declaration. `IMaintainableType` stands for an
InterfaceType supplied by your model.

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
mixins. They do not enter the implementing class's MRO, and their members are
not copied into its class body. The server adds the `HasInterface` references
after all types in the module exist. Mandatory interface members are then
instantiated by the normal OPC UA type-instantiation rules.
