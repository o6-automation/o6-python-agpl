# Container Types

Values that carry metadata, or that act as generic carriers:

| o6\\Python | |
|---|---|
| `o6.DataValue` | A value with optional `StatusCode`, `sourceTimestamp`, `serverTimestamp`, and sub-millisecond `*_picoseconds` fields. |
| `o6.ExtensionObject` | A generic carrier for structured values whose type is identified by a `NodeId` — used for any value of an NS0 datatype. |

!!! info
    o6\\Python **does not declare an explicit `Variant` type.** We achieve this through Python's dynamic typing — see [the next section](#variant) below for more information.

## Variant

Most OPC UA libraries introduce a `Variant` class that can hold *any* of the 25 built-in types — you create a `Variant` and the library figures out the actual type at runtime.

o6\\Python **does not do this.** There is effectively no `Variant` in the public API.

Python is dynamically typed, so the underlying value's class already carries the type information.

`Variant` is transparently handled *internally* by the C implementation without exposing it to the python layer.

---

## DataValue

`DataValue` is a small struct that travels with every variable read/write response on the wire. It carries:

| Field | Type | Description |
|---|---|---|
| `value` | 25 built-in types / `ExtensionObject` / (NumPy-)array of any of those | the actual scalar / array being transferred |
| `status` | `o6.StatusCode` | *optional* — what the server thinks of the value (`Good`, `Bad`, …) |
| `sourceTimestamp` / `sourcePicoseconds` | `o6.DateTime` / `int` | *optional* — when the underlying sensor/device *produced* the value |
| `serverTimestamp` / `serverPicoseconds` | `o6.DateTime` / `int` | *optional* — when the server *received* the value from the source |

The `*_picoseconds` fields give you the 10⁻⁷-second sub-tick precision that `DateTime` cannot represent (it's an integer count of 100-ns ticks).

Clients return `DataValue`s from when read, write, call services, and servers produce them when they hand values to subscriptions.

#### Constructing a DataValue

```python
dv = o6.DataValue()
dv.value = o6.Int32(42)
dv.status = o6.StatusCode.BadTimeout
dv.sourceTimestamp = o6.DateTime(datetime.datetime.now())
```

A missing `status` is implicitly `Good`.

```python
dv = o6.DataValue()
assert dv.status == o6.StatusCode.Good   # not None
```

#### Value member as Variant

The OPC UA specification models `DataValue.value` as a `Variant` — a discriminated union over the 25 built-in datatypes, arrays, and matrices. In o6\\Python that union is implicit and we can simply assign directly:

```python
dv = o6.DataValue()
dv.value = o6.Int32(42)               # Int32
dv.value = o6.Double(3.14)            # same field, now a Double
dv.value = "hello"                    # a String
dv.value = None                       # empty
dv.value = np.array([1.0, 2.0, 3.0])  # NumPy array of float64
dv.value = [1.0, 2.0, 3.0]            # Python list (internally converted into np.array)
```

See [Variant](#variant) for more details, how this is achived.

---

## ExtensionObject

An `ExtensionObject` is the OPC UA spec's open-type carrier: a `NodeId` identifies the actual datatype bundeled with the encoded payload.

`ExtensionObject` is mostly handled implicitly in o6\\Python: reads return the decoded Python object from `o6.ns.ns0` or a custom namespace, and writes accept the Python object directly.

`ExtnensionObject` appears user-facing at low-level seams where the spec accepts any of N possible structured types — for example, the polymorphic `history_update_details` field of `HistoryUpdateRequest`:

```python
import o6
from o6.ns import ns0

details = ns0.datatypes.UpdateDataDetails()
details.nodeId = o6.NodeId("ns=2;s=Temperature")
details.perform_insert_replace = ns0.datatypes.PerformUpdateType.REPLACE
details.update_values = [o6.DataValue(value=o6.Double(23.5))]

request = ns0.datatypes.HistoryUpdateRequest()
request.history_update_details = [o6.ExtensionObject(details)]
```

!!! info
    You may encounter `ExtensionObject` also when the Client receives a value of an unknown DataType and therefore doesn't know how to decode it from it on-the-wire representation.


---

## NumPy for arrays and large data

Anything that may carry an *array* of values internally — bulk numeric arrays, large string / bytestring / XML buffers, `DataValue` array payloads — is utilizing NumPy, the underlying C implementation stores those values in native contiguous buffers and a NumPy view over that memory keeps the round-trip cheap.

- **Zero-copy reads** — when possible, the array you get back is a view over the same memory the C implementation holds, so reading a large array does not allocate.
- **Vectorised math** — the standard NumPy operators work on numeric OPC UA values, no conversion step required.
- **Ecosystem fit** — the arrays pass straight through to pandas, matplotlib, scikit-learn, etc., with no extra glue.

---

## See also

- The `Variant` discriminated union over the 25 built-in types, and the normative layout of `DataValue` and `ExtensionObject` (the three "container" types the spec defines):
  [Part 6, §5.1.2 — Built-in Types](https://reference.opcfoundation.org/Core/Part6/v105/docs/5.1.2).
- The `ExtensionObject` envelope and the `Variant` encoding rules:
  [Part 6, §5.1.8 — ExtensionObject](https://reference.opcfoundation.org/Core/Part6/v105/docs/5.1.8)
  and [Part 6, §5.1.9 — Variant](https://reference.opcfoundation.org/Core/Part6/v105/docs/5.1.9).
- The on-the-wire binary encoding of `DataValue`, `Variant`, and `ExtensionObject`:
  [Part 6, §5.2.2.17 — DataValue](https://reference.opcfoundation.org/Core/Part6/v105/docs/5.2.2.17),
  [Part 6, §5.2.2.16 — Variant](https://reference.opcfoundation.org/Core/Part6/v105/docs/5.2.2.16),
  and [Part 6, §5.2.2.15 — ExtensionObject](https://reference.opcfoundation.org/Core/Part6/v105/docs/5.2.2.15).
- The catalogue of 25 built-in types (what `Variant` discriminates over):
  [Part 3, §8 — Standard DataTypes](https://reference.opcfoundation.org/Core/Part3/v105/docs/8).
