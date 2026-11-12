# Primitive Types

OPC UA numeric types have fixed widths. Python's ordinary `int` and `float`
have default OPC UA mappings; use a sized `o6` or NumPy type when the model
requires another width.

## Choosing a value's type

When the SDK infers an OPC UA datatype from a Python value, it uses the
Python type:

| Python input | Inferred OPC UA datatype |
|---|---|
| `bool` | Boolean |
| `int` | Int32 |
| `float` | Double |
| `str` / `bytes` | String / ByteString |
| Explicit `o6` primitive or NumPy scalar | Its corresponding type, including numeric width and signedness |

A bare integer is not widened automatically: values outside the Int32 range
raise `OverflowError` during conversion.

### Choosing an explicit numeric width

Construct a sized value to select a different width:

```python
import o6

temperature = o6.Float(23.5)
count = o6.Int64(2**40)
```

A bare `23.5` would select Double; a bare `2**40` exceeds the inferred Int32
range.

These numeric types are fixed-width NumPy scalars. Continuing the example,
convert to ordinary Python numbers when another library needs them:

```python
python_temperature = float(temperature)
python_count = int(count)
print(python_temperature, python_count)     # 23.5 1099511627776
```

### Conversion into a declared field

A structure field already has a declared OPC UA datatype. In that context,
conversion uses the field's type: a Python `23` in an Int64 field encodes as
Int64. The value must still fit the declared type.

## Primitive type reference

Numeric `o6` types are aliases for fixed-width NumPy scalar classes
(`np` below); for example, `o6.Int32` is `numpy.int32`. Other primitives use
standard-library classes or SDK types as listed here.

| o6\\Python | Python representation | Range / notes |
|---|---|---|
| `o6.Boolean` | `np.bool_`; decoded as `bool` | `True` / `False` |
| `o6.SByte` | `np.int8` | -128 … 127 (signed 8-bit) |
| `o6.Byte` | `np.uint8` | 0 … 255 (unsigned 8-bit) |
| `o6.Int16` | `np.int16` | -32 768 … 32 767 |
| `o6.UInt16` | `np.uint16` | 0 … 65 535 |
| `o6.Int32` | `np.int32` | -2 147 483 648 … 2 147 483 647 |
| `o6.UInt32` | `np.uint32` | 0 … 4 294 967 295 |
| `o6.Int64` | `np.int64` | -2⁶³ … 2⁶³ - 1 |
| `o6.UInt64` | `np.uint64` | 0 … 2⁶⁴ - 1 |
| `o6.Float` | `np.float32` | IEEE-754 single precision (32-bit) |
| `o6.Double` | `np.float64` | IEEE-754 double precision (64-bit) |
| `o6.String` | `str` | Unicode text |
| `o6.DateTime` | SDK timestamp object | 100-nanosecond ticks since the OPC UA epoch (1601-01-01) |
| `o6.Guid` | `uuid.UUID` | 128-bit identifier — same type as the Python standard library |
| `o6.ByteString` | `bytes` | Raw byte buffer — same type as the Python standard library |
| `o6.XmlElement` | Subclass of `str` | Keeps XmlElement distinct from String |

`Guid` and `ByteString` are aliases for `uuid.UUID` and `bytes`.
`XmlElement` is a distinct `str` subclass so it retains its OPC UA datatype.
`DateTime` is an SDK type, not a subclass of `datetime.datetime`.

## DateTime

`o6.DateTime` represents an OPC UA timestamp. Construct it from a Python
`datetime` using a timezone-aware input so the instant does not depend on the
computer's local timezone:

```python
from datetime import datetime, timedelta, timezone
import o6

python_time = datetime(2026, 1, 2, 3, 4, 5, tzinfo=timezone.utc)
ua_time = o6.DateTime(python_time)
```

An aware datetime is converted to its UTC instant; the original timezone is
not retained. A naive datetime is interpreted as local time. `o6.DateTime()`
with no argument creates zero ticks, not the current time.

`int(ua_time)` gives 100-nanosecond ticks since 1601-01-01 UTC, not Unix
seconds. Continuing the example, convert back to a standard-library datetime:

```python
ua_epoch = datetime(1601, 1, 1, tzinfo=timezone.utc)
python_time = ua_epoch + timedelta(microseconds=int(ua_time) // 10)
print(python_time.isoformat())              # 2026-01-02T03:04:05+00:00
```

Python datetime has microsecond resolution; the division discards fractions
smaller than a microsecond. Conversion from a Python datetime can also round.
Keep the `o6.DateTime` or its integer tick count when exact timestamp precision
matters. Integer construction, such as `o6.DateTime(ticks)`, preserves ticks.

---

## LocalizedText

`LocalizedText` pairs a string with an IETF language tag (`en`, `de-DE`, `fr-CA`, …). The locale is part of the identity of the text, not metadata: two `LocalizedText` values with the same string but different locales are not equal ([§8.5 LocalizedText](https://reference.opcfoundation.org/Core/Part3/v105/docs/8.5)).

`o6.LocalizedText` is a built-in type with `text` and `locale` attributes:

```python
import o6

lt = o6.LocalizedText("Hello", "en")
lt.text       # "Hello"
lt.locale     # "en"

o6.LocalizedText("Hello")           # locale="" (no locale set), text="Hello"
o6.LocalizedText()                   # both empty
o6.LocalizedText(lt)                # copy
o6.LocalizedText("en:Hello")         # "locale:text" shorthand — first ':' splits
```

Two arguments are the text, then the locale. The single-string shorthand puts
the locale first, as `str()` prints it. Pass the locale separately when the
text itself contains a colon: `o6.LocalizedText("Batch: 1", "en")`.

---

## Related topics

| Topic | What it covers |
|---|---|
| [Part 3, §8 — Standard DataTypes](https://reference.opcfoundation.org/Core/Part3/v105/docs/8) | The normative catalogue of built-in types and their ranges. |
| [Part 3, §8.5 — LocalizedText](https://reference.opcfoundation.org/Core/Part3/v105/docs/8.5) | LocalizedText and its locale identifier. |
| [Part 6, §5.1.2 — Built-in Types](https://reference.opcfoundation.org/Core/Part6/v105/docs/5.1.2) | Wire encoding of built-in types. |
| [Container Types](container-types.md) | Arrays and containers that wrap primitive values. |
| [Address & Identity Types](address-types.md) | NodeId, ExpandedNodeId, and QualifiedName values in Python. |
| [DataType](../../opcua-fundamentals/datatype.md) | The OPC UA type system and its Python representation. |
