# Writing a Nodeset in Python

Compiling XML is one way to get a namespace. The other is to skip the XML entirely and **write the nodeset directly in Python**. 
The `o6\\python` decorators, emitted by the compiler, are intentionally designed as human readable syntax. 
A hand-written module and a generated package are the same shape, register the same way, and are indistinguishable to `server.ns.append` and to a client on the wire.

That makes this the natural path when the model is yours: an application-specific type system, a prototype you are still reshaping, a small vendor extension on top of a companion spec, or types generated at runtime from a device description.

!!! info
    If you already have a `*.NodeSet2.xml` — from a companion spec, a vendor, or a modelling tool — compile it. See [Compiling Nodesets](compiling-nodesets.md).

!!! info
    The declarations on this page mirror the spec's node classes and its
    DataType kinds. For what a `DataType` node carries, and how structured
    types, enumerations and OptionSets differ, see
    [DataType](../../opcua-fundamentals/datatype.md) in OPC UA Fundamentals.

---

## The shape of a namespace module

A namespace module is an ordinary Python module. Two things make it a nodeset:

1. A call to `o6.ns.namespace(...)` at the top, which registers the namespace in the process-wide `o6.ns` table **and** records it in the module's `__NAMESPACES__`.
2. Decorated classes in the module body — one per type.

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
```

`server.ns.append` then publishes it exactly like a compiled package:

```python
import o6
import plant

server = o6.Server(port=4840)
server.ns.append(plant)
server.start()
```

`o6.ns.plant` works from anywhere in the process afterwards, and `ns=plant;i=…` resolves in every `NodeId` string. The `shortname`, `uri` and `version` you passed are what a client sees in the server's NamespaceArray.

!!! tip
    For a single-file script, `__main__` is a module too — `server.ns.append(sys.modules[__name__])` publishes types declared in the script itself. Splitting the namespace into its own importable module is still preferable: it keeps declarations out of the `if __name__ == "__main__"` path and makes the module reusable by both a server and a client process.

### Declaration order is dependency order

A decorator runs when Python executes the `class` statement, and it resolves every reference it is given *at that moment*. A type must therefore be declared before anything that names it:

```python
@o6.datatype(ns="plant")
class Point:
    x: float


@o6.datatype(ns="plant")
class BoundingBox:
    min: Point          # Point already exists — fine
    max: Point
```

The reverse order fails with an explicit error rather than a half-built type:

```
TypeError: o6.datatype: cannot infer UA DataType for annotation ...
You have to declare types in dependency order: Type A must be declared
before Type B, if B has a field of type A.
```

Self-reference is the one exception — a type may name itself, because its NodeId is allocated before its fields are collected:

```python
@o6.datatype(ns="plant")
class Recursive:
    name: str
    children: list["Recursive"]
```

### NodeIds

Every decorator takes an optional `nodeId=`. Omit it and o6 allocates the next free numeric identifier in that namespace; pass it and the type pins that identifier forever.

```python
@o6.objecttype(ns="plant", nodeId="ns=plant;i=1001", browseName="MachineType")
class MachineType(ns0.objtypes.BaseObjectType):
    ...
```

Auto-allocation is fine while a model is private and always loaded from the same source. **Pin NodeIds explicitly as soon as the model is published**: clients that hard-code identifiers, historical data, and stored configuration all depend on them, and an auto-allocated identifier moves whenever you reorder declarations.

`browseName=` defaults to the Python class name. Give it explicitly when the UA BrowseName differs from the identifier you want in Python, and qualify it (`"ns=plant;MachineType"`) when it must live in a namespace other than the declaring one.

---

## `@o6.datatype` — structures

A `@o6.datatype` class is a **wire layout**. Each annotated attribute becomes a field of the type's `StructureDefinition`, and the decorator registers the layout with open62541 so values of this shape encode and decode as a real structure rather than an opaque `ExtensionObject`.

```python
@o6.datatype(ns="plant", description="3-D vector of doubles")
class Point:
    x: float
    y: float
    z: float

    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0) -> None:
        self.x, self.y, self.z = x, y, z

    def __repr__(self) -> str:
        return f"Point(x={self.x}, y={self.y}, z={self.z})"
```

The `__init__` and `__repr__` are optional. Without them the type is still fully usable — o6 supplies a native initializer and a field-listing `repr`:

```python
p = Point()
p.x = 1.0
p                       # {x=1.0, y=0.0, z=0.0}
```

Annotations map to UA DataTypes directly. Python builtins resolve to their OPC UA counterparts, and the sized `o6` aliases are available whenever the exact width matters:

| Annotation | UA DataType |
|---|---|
| `bool`, `int`, `float`, `str`, `bytes` | `Boolean`, `Int64`, `Double`, `String`, `ByteString` |
| `o6.Int16`, `o6.UInt32`, `o6.Float`, `o6.Byte`, … | the exact built-in type |
| another `@o6.datatype` / `@o6.enumtype` class | that type |
| `o6.NodeId`, `o6.LocalizedText`, `o6.QualifiedName`, … | the built-in address/identity types |
| `list[T]` | `T` with `ValueRank = 1` (a 1-D array) |
| `typing.Any` | `BaseDataType` (`Variant`) |

### Field metadata with `o6.field`

`o6.field(...)` attaches OPC UA metadata to an annotated field. The annotation still supplies the type; the factory only adds what the annotation cannot express:

```python
@o6.datatype(ns="plant", description="One production batch")
class BatchRecord:
    batchId: str
    samples: list[float]
    comment: Optional[str] = o6.field(description="free-text operator note")
    tag: str = o6.field(maxStringLength=32)
```

- `description=` — the field's `Description` in the `StructureDefinition`.
- `isOptional=True` — an optional field. `Optional[T]` in the annotation does the same thing, and is the form to prefer.
- `valueRank=` / `arrayDimensions=` — override the rank inferred from the annotation. Struct fields are scalars (`-1`) or 1-D arrays (`1`); anything else is rejected, because open62541 cannot represent a multi-dimensional array as a struct member.
- `maxStringLength=` — a `String`/`ByteString` length hint.
- `name=` — the UA field name. This renames the Python attribute along with the wire field, so it is mainly useful to the nodeset compiler when a UA field name is not a valid Python identifier.

As soon as one field is optional the type's `StructureType` becomes `StructureWithOptionalFields`; an unset optional field reads back as `None`.

```python
record = BatchRecord()
record.batchId = "B-1042"
record.samples = [21.5, 21.7]
record                                  # {batchId='B-1042', samples=[21.5, 21.7], comment=None}
```

### Inheritance and abstract structures

Python inheritance is the `HasSubtype` chain, and a subtype inherits its parent's fields:

```python
@o6.datatype(ns="plant", isAbstract=True)
class AbstractResult:
    ok: bool


@o6.datatype(ns="plant")
class WeighResult(AbstractResult):
    mass: float


result = WeighResult()          # {ok=False, mass=0.0} — both fields
AbstractResult()                # TypeError: Cannot instantiate abstract data type
```

An abstract structure still carries a complete `DataTypeDefinition`, so it describes the shared layout for browsing clients while remaining non-instantiable. A field annotated with an abstract structure type is encoded as an `ExtensionObject`, which is what lets it carry any concrete subtype.

### Unions

Derive from `ns0.datatypes.Union` and the type's `StructureType` becomes `Union`. Assigning a field selects it; the previously selected field is cleared:

```python
@o6.datatype(ns="plant", description="Either a mass or a piece count")
class Measurement(ns0.datatypes.Union):
    mass: float
    count: o6.Int32


m = Measurement()
m.mass = 12.5
m                       # {mass=12.5}
```

!!! warning
    Select a field before a union value crosses an encoder. A union with no field set has no valid wire representation, and writing one into the address space is not currently rejected cleanly.

### Properties on a DataType node

A DataType node can own Properties. They are constructed first and linked in the class body like any other type child:

```python
_enumStrings = ns0.vartypes.PropertyType(
    browseName="EnumStrings",
    value=[o6.LocalizedText("OFF"), o6.LocalizedText("ON")],
    dataType=o6.LocalizedText,
    valueRank=1,
)


@o6.enumtype(ns="plant", browseName="Mode")
class Mode(ns0.datatypes.Enumeration):
    enumStrings: ns0.vartypes.PropertyType = o6.hasProperty(_enumStrings)
    OFF = 0
    ON = 1
```

`o6.hasProperty` also keeps the linked node out of Python's enum member table, so `Mode` has exactly the two members you declared.

---

## `@o6.enumtype` — enumerations

An `@o6.enumtype` class is a real `IntEnum` after decoration. Bare integer class attributes are enough:

```python
@o6.enumtype(ns="plant", description="Top-level machine state")
class MachineState:
    IDLE = 0
    RUNNING = o6.enumfield(1, description="executing a program")
    HOLD = o6.enumfield(2, description="paused by operator", displayName="HOLD")
    FAULT = 3
```

`o6.enumfield(value, ...)` adds per-member UA metadata — `description=`, `displayName=`, and `name=` for a UA member name that is not a valid Python identifier. Members without it are plain values; the two forms mix freely in one class. Duplicate numeric values are rejected, because they are ambiguous on the wire.

Use the type as an annotation to give a struct field or a Variable that enum's DataType, and as a value wherever an integer is expected:

```python
int(MachineState.RUNNING)               # 1
MachineState(1)                         # <MachineState.RUNNING: 1>
```

### Abstract enum parents

An `isAbstract=True` enum has no members and no wire representation — it is a pure type-system placeholder that concrete enums can share:

```python
@o6.enumtype(ns="plant", isAbstract=True, browseName="SpeedLimit")
class SpeedLimit:
    pass


@o6.enumtype(ns="plant", browseName="ConveyorSpeed")
class ConveyorSpeed(SpeedLimit):
    SLOW = 0
    FAST = 1


isinstance(ConveyorSpeed.FAST, SpeedLimit)      # True
```

This is the enum counterpart of an abstract structure: a Variable typed with the abstract parent accepts any of its concrete subtypes.

---

## `@o6.optionsettype` — option sets

An OPC UA OptionSet is a bit field, not an enumeration: several members can be set at once, and the DataType's value is their bitwise combination. Declare one with `@o6.optionsettype`, and each member with `o6.bitmask`:

```python
@o6.optionsettype(ns="plant", browseName="AccessLevelType", base=o6.Byte)
class AccessLevelType:
    CURRENT_READ = o6.bitmask(0x01 << 0, name="CurrentRead")
    CURRENT_WRITE = o6.bitmask(0x01 << 1, name="CurrentWrite")
    HISTORY_WRITE = o6.bitmask(0x01 << 3, name="HistoryWrite")
```

**A member's value is its mask, not its bit position.** Write it as `0x01 << n` so the source shows the bit position and the value it produces at once:

```python
int(AccessLevelType.HISTORY_WRITE)                              # 8, not 3
AccessLevelType.CURRENT_READ | AccessLevelType.HISTORY_WRITE    # 9
AccessLevelType.CURRENT_READ in (AccessLevelType.CURRENT_READ | AccessLevelType.HISTORY_WRITE)  # True
```

`o6.bitmask(mask, ...)` takes the same per-member UA metadata as `o6.enumfield` — `name=`, `description=` and `displayName=`. It is the *only* member spelling an OptionSet accepts: a bare integer, a `bool`, a `float`, a numpy scalar such as `o6.Byte(0x01 << 1)`, and `o6.enumfield(...)` are all rejected. Non-numeric class attributes — helper constants, methods, properties — are left alone as before.

**`base=` is mandatory.** It names the unsigned integer the OptionSet subtypes — `o6.Byte`, `o6.UInt16`, `o6.UInt32` or `o6.UInt64` — which is the OptionSet's declared width. Nothing else in the declaration carries that width, and it bounds the bits a member may claim. It is spelled as a keyword rather than a Python base class, because a numpy scalar type cannot be a base of the `IntFlag` the SDK builds.

`base=` is load-bearing in three places. It bounds the legal bit range; it is the width the OptionSet occupies on the wire, so a `base=o6.Byte` OptionSet is one byte inside a structure and not four; and it is the `HasSubtype` parent the DataType node is published under, so a client browsing the type sees `Byte` rather than `BaseDataType`.

An integer-form OptionSet does not publish a `DataTypeDefinition` attribute — reading it answers `Bad_AttributeIdInvalid`, the same as the OptionSets in the standard namespace. That is the cost of encoding at the declared width, and it is permanent: the attribute carries a bare field list, with neither the width nor any indication that the fields are bits, so it could not have described the OptionSet in any case. The declared bit names still reach a client, through the `OptionSetValues` property o6 generates alongside the DataType node — which is what Part 3 defines as an OptionSet's carrier for them.

The two member helpers are not interchangeable: `o6.bitmask` in an `@o6.enumtype` class and `o6.enumfield` in an `@o6.optionsettype` class are both rejected, each naming the helper to use instead. There is exactly one legal spelling per decorator.

### What is rejected, and when

Everything is checked at decoration time, and every message names the decorator, the class and the offending member or argument:

| declaration | rejected because |
| --- | --- |
| `base=` omitted | an OptionSet's width has no default |
| `base=o6.Int32`, `base=int` | only `o6.Byte`, `o6.UInt16`, `o6.UInt32` and `o6.UInt64` are OptionSet bases |
| `o6.bitmask(0)`, `o6.bitmask(0x03)` | a member is exactly one set bit, not none and not several |
| two members with the same mask | the value would be ambiguous on the wire |
| `o6.bitmask(0x01 << 8)` under `base=o6.Byte` | the bit is outside the base's 8 bits |
| `o6.enumfield(...)`, `2`, `True`, `o6.Byte(2)` as a member | only `o6.bitmask` declares a bit; anything else numeric would silently not be a member |
| a class with no members | an OptionSet with no bits has no wire layout |
| a Python enum base, e.g. `class Flags(AbstractFlags)` | `base=` is what an OptionSet subtypes; a Python base would be silently overridden |

The width check is the load-bearing one: it is what stands between a wide OptionSet and a mask its base cannot hold, and it is possible only because `base` is mandatory.

One limit comes from the registration rather than from OptionSets themselves: the `EnumField` value that carries a member is a signed 64-bit integer, so bit 63 of a `UInt64` has no representable mask and is rejected by name instead of surfacing as an overflow from the C extension. The same overflow is still reachable through `@o6.enumtype` with a value of 2⁶³ or more.

### The structure form is an ordinary `@o6.datatype`

Some OptionSets are declared as structures instead: a subtype of the ns0 `OptionSet` with `Value` and `ValidBits` ByteStrings, carrying which bits are valid alongside the bits that are set. Those are ordinary [`@o6.datatype`](#o6datatype-structures) classes and share nothing with `@o6.optionsettype` but the name — different registration, different shape, and their own member helper.

Declare each bit with `o6.optionsetbit`, alongside the two ByteStrings:

```python
@o6.datatype(ns="plant", browseName="ExplosionZoneOptionSet")
class ExplosionZoneOptionSet(ns0.datatypes.OptionSet):
    value: o6.ByteString
    validBits: o6.ByteString

    zone0 = o6.optionsetbit(0, name="Zone 0")
    zone1 = o6.optionsetbit(1, name="Zone 1")
    zone8 = o6.optionsetbit(8, name="Zone 8")
```

The argument is the bit's *position* — the low byte of `Value` first, least significant bit first — because that is what the pair is indexed by, and there is no single integer to carry a mask for.

**Reading a bit is three-valued.** `Value` says whether a bit is set; `ValidBits` says whether it says anything at all, and no integer flag can express the difference:

```python
zones = ExplosionZoneOptionSet(value=b"\x01\x01", validBits=b"\x03\x00")
zones.zone0    # True  -- set, and valid
zones.zone1    # False -- clear, and valid
zones.zone8    # None  -- ValidBits says nothing about this bit
```

A bit whose `ValidBits` byte is missing altogether, because `ValidBits` is shorter than `Value`, reads as not valid as well rather than raising:

```python
short = ExplosionZoneOptionSet(value=b"\xff\xff", validBits=b"\xff")
short.zone8    # None -- bit 8 lives in byte 1, which ValidBits does not reach
```

Assigning a bit writes `Value` and `ValidBits` together, so an inconsistent pair cannot be produced through the accessor, and both ByteStrings grow as needed:

```python
zones = ExplosionZoneOptionSet()
zones.zone1 = False       # value 0x00, validBits 0x02 -- clear, and said so
zones.zone1 = None        # validBits 0x00 -- the bit stops meaning anything
```

A bit whose name collides with `value` or `validBits` is uniqued rather than shadowing the member, the same way a colliding enum member is.

---

## `@o6.referencetype` — custom references

ReferenceTypes are address-space metadata only: no `UA_DataType`, no encoding, nothing to instantiate. The marker class carries the NodeId, BrowseName, `InverseName`, `Symmetric` and `IsAbstract` that the server publishes, and Python inheritance is the `HasSubtype` chain.

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

A ReferenceType marker must have no annotated fields, and it is never instantiable. Use it as the reference type argument wherever one is expected:

```python
o6.reference(conveyor, Feeds, machine)          # between two live nodes
server.addReference(conveyor, machine, Feeds)   # equivalently
```

---

## `@o6.variabletype` — typed Variables

A VariableType constrains a Variable's value and declares the children every Variable of that type gets. The value constraints are the decorator's own arguments:

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

- `dataType=`, `valueRank=`, `arrayDimensions=` describe the value. **Omitted, they are inherited from the base VariableType**, not reset to `BaseDataType`/`ANY` — OPC UA requires a subtype's constraints to be equal or narrower than its parent's, so inheriting is the only safe default.
- `value=` seeds a default value on the type node itself.
- `isAbstract=True` makes the type non-instantiable.
- `interfaces=[...]` adds `HasInterface` references (see [Server](../../server/declared-types.md#type-interfaces)).

Almost every VariableType derives from `ns0.vartypes.BaseDataVariableType`. `ns0.vartypes.PropertyType` is the right base — and the right child type — for metadata that describes another node rather than carrying process data.

### Children

Children are declared by *annotating* a class attribute with the child's concrete type and assigning a linked instance of that type:

```python
@o6.variabletype(ns="plant", description="Inlet/outlet temperature pair")
class ThermalProfileType(ns0.vartypes.BaseDataVariableType):
    inlet: TemperatureType = o6.hasComponent(TemperatureType())
    outlet: TemperatureType = o6.hasComponent(TemperatureType())
```

Two things are happening in one line, and it is worth separating them:

- **The instance** (`TemperatureType()`) describes the child node — its BrowseName, DataType, AccessLevel, default value. Constructed inside a namespace module with no live server, it stays an ordinary declaration.
- **The linker** (`o6.hasComponent` / `o6.hasProperty`) states the reference type that attaches it to the parent. Each takes exactly one instance and returns it unchanged, so the static type survives and `profile.inlet` is a `TemperatureType` to the type checker.

Beyond the two common ones, `o6.organizes`, `o6.hasEventSource`, `o6.hasNotifier`, `o6.hasOrderedComponent`, `o6.hasAddIn`, `o6.hasInterface`, `o6.hasCondition` and `o6.generatesEvent` cover the remaining standard hierarchies; their inverse forms (`o6.componentOf`, `o6.propertyOf`, `o6.organizedBy`, …) point the reference the other way; and `o6.reference(instance, SomeReferenceType)` links through any custom ReferenceType.

**Optionality belongs to the relationship** and is inferred exclusively from `Optional[T]` in the annotation — an `Optional[T]` child gets the `Optional` ModellingRule, everything else is `Mandatory`. Node constructors deliberately have no `optional` argument. A relationship can even be declared without an instance yet:

```python
documentation: Optional[ns0.vartypes.PropertyType] = o6.hasProperty(None)
```

---

## `@o6.objecttype` — typed Objects

An ObjectType is the same story with Object children and Methods added. Everything about children, linkers and optionality carries over unchanged.

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
        ns0.vartypes.PropertyType(dataType=MachineState)
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

`state`, `temperature` and `drive` show the three kinds of child: a leaf Property, a complex Variable, and a complex Object. `reset` is a **Method declaration** — `o6.call(...)` with `inputArgs`/`outputArgs` describes the signature and nothing else. The Python behavior behind it is supplied separately; that is the whole subject of [Implementing Object Behavior](implementing-object-behavior.md).

Subtyping is plain Python inheritance, and a subtype inherits every child of its base:

```python
@o6.objecttype(ns="plant", description="A CNC machine")
class CncMachineType(MachineType):
    serial: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(dataType=str))
```

`CncMachineType` has `state`, `temperature`, `drive`, `Reset` **and** `serial`.

An ObjectType may also declare an `__init__`. It runs on the fully constructed node, so `super().__init__(**kwargs)` is only the ordinary cooperative Python call and performs no OPC UA work:

```python
@o6.objecttype(ns="plant")
class PumpType(ns0.objtypes.BaseObjectType):
    def __init__(self, *, device=None, **kwargs):
        super().__init__(**kwargs)
        self.device = device
```

---

## Using the types

Once the module is appended, the declared classes are the API. Calling one either creates a live server node or returns a declaration, depending on which server owns the construction — the full resolution order is in [Server](../../server/declared-types.md#declared-type-instance-ownership).

### Instantiating

```python
import o6
import plant

server = o6.Server(port=4840)
server.ns.append(plant)

machine = plant.CncMachineType(
    parent=server.objectsNode,
    browseName="M-101",
    nodeId="ns=plant;i=5001",
    values={
        "state": int(plant.MachineState.RUNNING),
        "serial": "SN-001",
        "drive": {"manufacturer": "ACME", "current": 0.0},
    },
)
```

`values=` seeds the instance's children by Python member name:

- A **leaf** child takes a plain Python value.
- A **complex** child — one whose own type declares children — takes a **dict** of its children, applied recursively. Passing a scalar there is an error (`complex child 'drive' needs a DriveType declaration or a dict of values`).
- To seed a complex child's *own* value as well as its children, pass a detached declaration instead of a dict:

    ```python
    values={
        "temperature": plant.TemperatureType(
            server=None,                       # force a declaration
            value=19.0,                        # the Variable's own value
            values={"engineeringUnits": "degC"},
        ),
    }
    ```

Children not named in `values=` are still created — every Mandatory child of the type exists on every instance, with a zero-initialized value.

### Reading and writing

Children are reached by dot access, and a Variable node is callable: no argument reads, one argument writes.

```python
machine.serial()                        # 'SN-001'
machine.drive.manufacturer()            # 'ACME'
machine.drive.current(1.25)             # write
machine.temperature.engineeringUnits()  # 'degC'

o6.NodeId(machine.drive.current)        # ns=… — the NodeId of any node handle
```

A struct-valued Variable round-trips as the Python class, not as an `ExtensionObject`:

```python
origin = server.addVariable("Origin", server.objectsNode, plant.Point(1.0, 2.0, 3.0))
server.read(origin)                     # {x=1.0, y=2.0, z=3.0}
```

### From a client

A client appends nothing. On connect it maps the server's NamespaceArray onto the `o6.ns` table, so as long as the same `plant` module is importable in the client process, its types decode and `ns=plant;…` NodeIds resolve:

```python
import plant                            # registers the namespace in this process too

client = o6.Client("opc.tcp://localhost:4840")
client.connect()

client.read("ns=plant;i=5001")
client.call(o6.NodeId(machine), o6.NodeId(machine.Reset), [o6.Int32(1)])
```

A client that never imports the module still talks to the server, but sees numeric namespace indices and decodes `plant` structures as opaque `ExtensionObject`s. See [Using Nodesets](loading-and-using-nodesets.md#namespace-modules-load-lazily) for why merely importing is sometimes not enough for a *compiled* namespace.

---

## See also

- The complete hand-written reference nodeset — a 6-DOF robot arm exercising every decorator:
  [`examples/nodeset/myns.py`](https://github.com/o6-automation/o6-python-agpl/blob/main/examples/nodeset/myns.py),
  driven end-to-end by [`examples/nodeset/example.py`](https://github.com/o6-automation/o6-python-agpl/blob/main/examples/nodeset/example.py).
- Giving the declared Methods and Variables actual behavior:
  [Implementing Object Behavior](implementing-object-behavior.md).
- Turning an existing `*.NodeSet2.xml` into the same shape automatically:
  [Compiling Nodesets](compiling-nodesets.md).
- Importing, appending and addressing a namespace, and the `o6.ns` registry:
  [Using Nodesets](loading-and-using-nodesets.md),
  [Namespace Mapping in o6\\Python](namespace-mapping-in-o6.md).
- Instance ownership, type children, interfaces and access control:
  [Server](../../server/index.md).
- What the OPC UA specification says about the constructs above:
  [Part 3 — Address Space Model](https://reference.opcfoundation.org/Core/Part3/v105/docs/),
  and [Part 6, Annex F — Information Model XML Schema](https://reference.opcfoundation.org/Core/Part6/v105/docs/F)
  for the XML form of the same declarations.
