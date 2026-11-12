# Declaring Custom DataTypes

Define the values carried by Variables and Method arguments.
These examples use the `plant` namespace and imports from
[Writing a Namespace Module](namespace-modules.md). Add the `Point` declaration
below to `plant.py` for the publishing example. The other declarations are
optional additions. Blocks that construct or inspect values are usage fragments
for a separate script after importing the corresponding classes from `plant`.

## `@o6.datatype` — structures

A `@o6.datatype` class is a wire layout. Each annotated attribute becomes a field of the type's `StructureDefinition`. The decorator registers the layout with open62541, so values encode and decode as a structure instead of an opaque `ExtensionObject`.

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

Continuing with this `Point` definition:

```python
p = Point()
p.x = 1.0
print(repr(p))          # Point(x=1.0, y=0.0, z=0.0)
```

`__init__` and `__repr__` are optional. As an alternative, omit both methods
from the declaration; o6 then supplies an initializer and a representation
such as `{x=1.0, y=0.0, z=0.0}`. Keep one `Point` declaration in the module.

Annotations declare a field's UA DataType. Plain `int` means Int32;
use `o6.Int64` for a 64-bit field. Field values encode against that declared
type, as explained in
[Primitive Types](../sdk-fundamentals/builtin/primitive-types.md#conversion-into-a-declared-field):

| Annotation | UA DataType |
|---|---|
| `bool`, `int`, `float`, `str`, `bytes` | `Boolean`, `Int32`, `Double`, `String`, `ByteString` |
| `o6.Int16`, `o6.UInt32`, `o6.Float`, `o6.Byte`, … | the exact built-in type |
| another `@o6.datatype` / `@o6.enumtype` class | that type |
| `o6.NodeId`, `o6.LocalizedText`, `o6.QualifiedName`, … | the built-in address/identity types |
| `list[T]` | `T` with `ValueRank = 1` (a 1-D array) |
| `typing.Any` | `BaseDataType` (`Variant`) |

### Encoding nodes

A concrete structure has a Default Binary encoding. Its NodeId identifies the
structure inside an `ExtensionObject` on the wire. `defaultEncodingId=` sets
it. By default it is the explicit numeric `nodeId=` plus one; otherwise it is
allocated in the namespace right after the DataType. Publishing the namespace
adds the `DataTypeEncodingType` Object `Default Binary` with this NodeId and
the `HasEncoding` reference from the DataType, as
[Part 3, DataType NodeClass](https://reference.opcfoundation.org/Core/Part3/v105/docs/5.8.3)
requires. An abstract structure gets one only with an explicit
`defaultEncodingId=`. A compiled companion specification declares its
encoding Objects itself, and publishing adds only the reference.

The encoding NodeId must be free. If another node of the model already uses
it, publishing logs a warning and adds no encoding node; choose NodeIds that
leave a gap after each structure or pass `defaultEncodingId=`.

### Field metadata with `o6.field`

`o6.field(...)` attaches OPC UA metadata to an annotated field. The annotation still supplies the type:

```python
@o6.datatype(ns="plant", description="One production batch")
class BatchRecord:
    batchId: str
    samples: list[float]
    comment: Optional[str] = o6.field(description="free-text operator note")
    tag: str = o6.field(maxStringLength=32)
```

- `description=` — the field's `Description` in the `StructureDefinition`.
- `isOptional=True` — an optional field. `Optional[T]` in the annotation does the same and is preferred.
- `valueRank=` / `arrayDimensions=` — override the rank inferred from the annotation. Structure fields are scalars (`-1`) or 1-D arrays (`1`). Anything else is rejected, because open62541 cannot represent a multi-dimensional array as a structure member.
- `maxStringLength=` — a `String`/`ByteString` length hint.
- `name=` — the UA field name. It renames the Python attribute as well as the wire field. The nodeset compiler uses it when a UA field name is not a valid Python identifier.

If any field is optional, the type's `StructureType` is `StructureWithOptionalFields`. An unset optional field reads as `None`.

```python
record = BatchRecord()
record.batchId = "B-1042"
record.samples = [21.5, 21.7]
print(record.batchId, record.comment)    # B-1042 None
```

### Inheritance and abstract structures

Python inheritance is the `HasSubtype` chain. A subtype inherits its parent's fields:

```python
@o6.datatype(ns="plant", isAbstract=True)
class AbstractResult:
    ok: bool


@o6.datatype(ns="plant")
class WeighResult(AbstractResult):
    mass: float
```

In a separate usage fragment, `WeighResult()` constructs a value with both
fields. Calling `AbstractResult()` raises `TypeError`; leave that deliberate
failure out of the namespace module.

An abstract structure has a complete `DataTypeDefinition` that describes the shared layout to browsing clients, but you can't instantiate it. A field annotated with an abstract structure type is encoded as an `ExtensionObject`, so it can carry any concrete subtype.

### Unions

A type derived from `ns0.datatypes.Union` has the `StructureType` `Union`. Assigning a field selects it and clears the previously selected field:

```python
@o6.datatype(ns="plant", description="Either a mass or a piece count")
class Measurement(ns0.datatypes.Union):
    mass: float
    count: o6.Int32
```

In a usage fragment after importing `Measurement` from `plant`:

```python
m = Measurement()
m.mass = 12.5
m                       # {mass=12.5}
```

!!! warning
    Select a field before a union value is encoded. A union with no field set has no valid wire representation, and writing one into the address space is not rejected cleanly.

### Properties on a DataType node

A DataType node can own Properties. Construct them first and link them in the class body like any other type child:

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

`o6.hasProperty` also keeps the linked node out of the enum member table, so `Mode` has only the two declared members.

Declaring `EnumStrings` yourself is optional: publishing adds it when an enumeration has none, see [below](#enumstrings-and-enumvalues).

---

## `@o6.enumtype` — enumerations

An `@o6.enumtype` class is an `enum.IntEnum` after decoration. Declare each member as an integer class attribute:

```python
@o6.enumtype(ns="plant", description="Top-level machine state")
class MachineState:
    IDLE = 0
    RUNNING = o6.enumfield(1, description="executing a program")
    HOLD = o6.enumfield(2, description="paused by operator", displayName="HOLD")
    FAULT = 3
```

`o6.enumfield(value, ...)` adds per-member UA metadata: `description=`, `displayName=`, and `name=` for a UA member name that is not a valid Python identifier. You can mix it with plain values in one class. Duplicate numeric values are rejected, because they are ambiguous on the wire.

Use the type as an annotation to give a structure field or a Variable that enum's DataType. Use its members wherever an integer is expected:

```python
int(MachineState.RUNNING)               # 1
MachineState(1)                         # <MachineState.RUNNING: 1>
```

Members behave as integers, not bit flags. `|`, `&` and `~` fall through to `int`: `MachineState.RUNNING | MachineState.HOLD` is the integer `3`, not `MachineState.FAULT` (also 3), and `MachineState.HOLD in some_value` raises `TypeError`. For a value that is a combination of bits, use [`@o6.optionsettype`](#o6optionsettype-option-sets).

A value from a peer that the declaration does not define still decodes, so one out-of-specification field does not fail the whole read. The value is integer-equal to what arrived, has no member name, and re-encodes unchanged in binary and JSON:

```python
MachineState(7).name                    # None
int(MachineState(7))                    # 7
```

It compares equal to itself and works as a dictionary key. It is not interned, so `MachineState(7) is MachineState(7)` is `False`; interning would grow the type with every value a non-conforming peer sends. It cannot be encoded as XML, because XML spells an enumeration as `Name_Value` and the value has no name.

### EnumStrings and EnumValues

Publishing the namespace gives every concrete enumeration the Property that
[Part 3](https://reference.opcfoundation.org/Core/Part3/v105/docs/5.8.3)
requires, unless the DataType already has an `EnumStrings` or `EnumValues`
Property:

- `EnumStrings`, a `LocalizedText` array, when the values are `0` to `n - 1`
  in declaration order;
- `EnumValues`, an `EnumValueType` array, otherwise, for example for
  `BLACK = 10`.

The texts are the members' display names. The Property's NodeId is a string
NodeId derived from the DataType's NodeId, for example
`ns=2;s=i=6003/EnumStrings`, so it does not use up a numeric NodeId of the
namespace.

### Abstract enum parents

An `isAbstract=True` enum has no members and no wire representation. It is a common parent for concrete enums:

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

As with an abstract structure, a Variable typed with the abstract parent accepts any of its concrete subtypes.

---

## `@o6.optionsettype` — option sets

An OPC UA OptionSet is a bit field: several members can be set at once, and the value is their bitwise combination. After decoration, an `@o6.optionsettype` class is an `enum.IntFlag`. `|` on two members gives a value of the OptionSet's own type, and any combination of its bits is a legal value. Declare each member with `o6.bitmask`:

```python
@o6.optionsettype(ns="plant", browseName="AccessLevelType", base=o6.Byte)
class AccessLevelType:
    CURRENT_READ = o6.bitmask(0x01 << 0, name="CurrentRead")
    CURRENT_WRITE = o6.bitmask(0x01 << 1, name="CurrentWrite")
    HISTORY_WRITE = o6.bitmask(0x01 << 3, name="HistoryWrite")
```

**A member's value is its mask, not its bit position.** Write it as `0x01 << n` so the source shows both:

```python
int(AccessLevelType.HISTORY_WRITE)                              # 8, not 3
AccessLevelType.CURRENT_READ | AccessLevelType.HISTORY_WRITE    # 9
AccessLevelType.CURRENT_READ in (AccessLevelType.CURRENT_READ | AccessLevelType.HISTORY_WRITE)  # True
```

`o6.bitmask(mask, ...)` takes the same per-member UA metadata as `o6.enumfield`: `name=`, `description=` and `displayName=`. It is the only member form an OptionSet accepts. A bare integer, a `bool`, a `float`, a NumPy scalar such as `o6.Byte(0x01 << 1)`, and `o6.enumfield(...)` are rejected. Non-numeric class attributes (helper constants, methods, properties) are left unchanged.

**`base=` is mandatory.** It names the unsigned integer type the OptionSet subtypes: `o6.Byte`, `o6.UInt16`, `o6.UInt32` or `o6.UInt64`. It is passed as a keyword, not a Python base class, because a NumPy scalar type cannot be a base of the `IntFlag` the SDK builds. `base=` determines:

- the legal bit range of the members;
- the width on the wire: a `base=o6.Byte` OptionSet is one byte inside a structure, not four;
- the `HasSubtype` parent of the published DataType node: a browsing client sees `Byte`, not `BaseDataType`.

An integer-form OptionSet in o6\\Python publishes no `DataTypeDefinition`
attribute; reading it returns `BadAttributeIdInvalid`. This is an SDK limitation:
[Part 3, DataType NodeClass](https://reference.opcfoundation.org/Core/Part3/v105/docs/5.8.3)
requires `DataTypeDefinition` for OptionSets, including unsigned-integer forms.
Clients can read its bit names from the `OptionSetValues` Property that
publishing adds unless the DataType declares one: one display name per bit
position, and an empty text for an unused bit. The structure form described
below uses the SDK's ordinary structure definition.

The member helpers are not interchangeable. `o6.bitmask` in an `@o6.enumtype` class and `o6.enumfield` in an `@o6.optionsettype` class are rejected, with an error that names the correct helper.

### What is rejected, and when

All checks run at decoration time. Every error message names the decorator, the class and the offending member or argument:

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

The width check prevents a mask that the base type cannot hold. It works only because `base` is mandatory.

The `EnumField` value that carries a member is a signed 64-bit integer. Bit 63 of a `UInt64` therefore has no representable mask and is rejected with a named error instead of an overflow from the C extension. `@o6.enumtype` with a value of 2⁶³ or more still produces that overflow.

### The structure form is an ordinary `@o6.datatype`

Some OptionSets are structures: a subtype of the ns0 `OptionSet` with `Value` and `ValidBits` ByteStrings, which record which bits are set and which bits are valid. These are ordinary [`@o6.datatype`](#o6datatype-structures) classes. They share only the name with `@o6.optionsettype`: registration, shape and member helper differ.

Declare each bit with `o6.optionsetbit`, next to the two ByteStrings:

```python
@o6.datatype(ns="plant", browseName="ExplosionZoneOptionSet")
class ExplosionZoneOptionSet(ns0.datatypes.OptionSet):
    value: o6.ByteString
    validBits: o6.ByteString

    zone0 = o6.optionsetbit(0, name="Zone 0")
    zone1 = o6.optionsetbit(1, name="Zone 1")
    zone8 = o6.optionsetbit(8, name="Zone 8")
```

The argument is the bit's position, counted from the low byte of `Value` and the least significant bit. The ByteStrings are indexed by position, and there is no single integer to hold a mask.

**Reading a bit returns one of three values.** `Value` says whether a bit is set. `ValidBits` says whether that bit is meaningful:

```python
zones = ExplosionZoneOptionSet(value=b"\x01\x01", validBits=b"\x03\x00")
zones.zone0    # True  -- set, and valid
zones.zone1    # False -- clear, and valid
zones.zone8    # None  -- ValidBits says nothing about this bit
```

A bit whose `ValidBits` byte is missing, because `ValidBits` is shorter than `Value`, also reads as not valid instead of raising:

```python
short = ExplosionZoneOptionSet(value=b"\xff\xff", validBits=b"\xff")
short.zone8    # None -- bit 8 lives in byte 1, which ValidBits does not reach
```

Assigning a bit writes `Value` and `ValidBits` together, so the accessor cannot produce an inconsistent pair. Both ByteStrings grow as needed:

```python
zones = ExplosionZoneOptionSet()
zones.zone1 = False       # value 0x00, validBits 0x02 -- clear, and said so
zones.zone1 = None        # validBits 0x00 -- the bit stops meaning anything
```

A bit whose name collides with `value` or `validBits` gets a unique name instead of shadowing the member, like a colliding enum member.

---
