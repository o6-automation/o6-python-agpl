# Primitive Types

Numbers, booleans, strings and dates have direct Python representatives — one wrapper class per OPC UA built-in, backed by the corresponding [NumPy](https://numpy.org/) or Python standard-library type for the underlying value:

| o6\\Python | Underlying value | Range / notes |
|---|---|---|
| `o6.Boolean` | `bool` | `True` / `False` |
| `o6.SByte` | `np.int8` | -128 … 127 (signed 8-bit) |
| `o6.Byte` | `np.uint8` | 0 … 255 (unsigned 8-bit) |
| `o6.Int16` | `np.int16` | -32 768 … 32 767 |
| `o6.UInt16` | `np.uint16` | 0 … 65 535 |
| `o6.Int32` | `np.int32` | -2 147 483 648 … 2 147 483 647 |
| `o6.UInt32` | `np.uint32` | 0 … 4 294 967 295 |
| `o6.Int64` | `np.uint64` | -2⁶³ … 2⁶³ - 1 |
| `o6.UInt64` | `np.uint64` | 0 … 2⁶⁴ - 1 |
| `o6.Float` | `np.float32` | IEEE-754 single precision (32-bit) |
| `o6.Double` | `np.float64` | IEEE-754 double precision (64-bit) |
| `o6.String` | `str` | Unicode text |
| `o6.DateTime` | `datetime.datetime` | 100-nanosecond ticks since the OPC UA epoch (1601-01-01) |
| `o6.Guid` | `uuid.UUID` | 128-bit identifier — same type as the Python standard library |
| `o6.ByteString` | `bytes` | Raw byte buffer — same type as the Python standard library |
| `o6.XmlElement` | `str` | XML fragment stored as a string |

> **Note** — `Guid`, `ByteString` and `XmlElement` are not separate Python classes; the C extension reuses `uuid.UUID`, `bytes` and `str` directly. The wrapper names in the table are the *import aliases* you use to refer to them in the OPC UA context.

## Numeric Types with NumPy

All numeric wrappers (`SByte`, `Byte`, `Int16`, `UInt16`, `Int32`, `UInt32`, `Int64`, `UInt64`, `Float`, `Double`) store their value as a fixed-width NumPy scalar. OPC UA numeric types are sized (8/16/32/64-bit, signed or unsigned, IEEE-754 float), and NumPy is the de facto Python standard for fixed-width numeric values — making it the natural backing type so that width, signedness and overflow match the wire format exactly.

NumPy's fixed-width scalars also extend naturally to bulk transport — see [Container Types](container-types.md#numpy-for-arrays-and-large-data) for how the same backing enables efficient array transfers.

### Implicit casting of Python `int` and `float`

Using numeric literals in Python are the types `int` or `float`

```python
my_int = 23         # Python type: int
my_float = 1.6021   # Python type: float
```

A Python `int` or `float` does not differentiate between signedness and size. Using them will result in **implicitly casting** at the API boundary.

```python
client.write(nodeid, 23)    # 23 is a Python int
                            # the node on the server is an Int32
                            # -> cast to o6.Int32 (np.int32) and sent

client.write(nodeid, 23.5)  # 23.5 is a Python float
                            # the node is a Double
                            # -> cast to o6.Double (np.float64) and sent
```

If the server expects a different type you will receive a `StatusCode.BadTypeMissmatch`.

!!! info
    Python `float` is implicitly cast to `np.double`. Python floats are internally represented as 64 bit wide floating point numbers. This prevents loss of precision.

---

## LocalizedText

 `LocalizedText` pairs the string with an IETF language tag (`en`, `de-DE`, `fr-CA`, …). The spec calls this out explicitly: **the locale is part of the identity of the text**, not metadata, so two `LocalizedText` values with the same string but different locales are not equal. See also [§8.5 LocalizedText](https://reference.opcfoundation.org/Core/Part3/v105/docs/8.5).

In o6\\Python, `LocalizedText` is a real builtin type with `text` and `locale` attributes:

```python
lt = o6.LocalizedText("en", "Hello")
lt.text       # "Hello"
lt.locale     # "en"

o6.LocalizedText("Hello")           # locale="" (no locale set), text="Hello"
o6.LocalizedText()                   # both empty
o6.LocalizedText(existing_lt)        # copy
o6.LocalizedText("en:Hello")         # "locale:text" shorthand — first ':' splits
```

---

## See also

- The OPC UA spec's normative catalogue of the 25 built-in types and their ranges:
  [Part 3, §8 — Standard DataTypes](https://reference.opcfoundation.org/Core/Part3/v105/docs/8).
- The normative `LocalizedText` encoding, including the locale-as-identity rule:
  [Part 3, §8.5 — LocalizedText](https://reference.opcfoundation.org/Core/Part3/v105/docs/8.5).
- The on-the-wire encoding of the built-in types (binary, JSON, XML):
  [Part 6, §5.1.2 — Built-in Types](https://reference.opcfoundation.org/Core/Part6/v105/docs/5.1.2).
- How arrays and bulk transport wrap the same primitives:
  [Container Types](container-types.md).
- The `o6`-side `Int32` / `Double` / `DateTime` / … wrappers and their NumPy backing:
  [Address & Identity Types](address-types.md) and
  [DataType](../opcua-recap/datatype.md).
