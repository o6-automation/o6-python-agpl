# Container Types

| Type | Purpose |
| --- | --- |
| `o6.DataValue` | Value, status, and optional timestamps |
| `o6.ExtensionObject` | Decoded structured value or encoded payload with a type identifier |
| NumPy array | Typed array or matrix value |

## Variant

OPC UA Variants are implicit in Python values. There is no public
`o6.Variant` class. The Python type selects the wire datatype; use sized
`o6`/NumPy scalars when the width matters.
[Primitive Types](primitive-types.md#choosing-a-values-type) lists the inference
defaults and shows how to construct explicitly sized numeric values.

```python
import numpy as np
import o6

value = o6.DataValue(value=o6.Int32(42))
value.value = o6.Double(3.14)
value.value = "hello"
value.value = np.array([1.0, 2.0, 3.0], dtype=np.float64)
value.value = None
```

A non-empty sequence infers its element type from the first element; all
elements must be convertible to that type. A NumPy array selects its element
type from its dtype. Use a typed NumPy array for an empty array; bare `[]` has
no inferable element type. `None` represents an empty Variant (a null value).

## DataValue

| Field | Python type | Meaning |
| --- | --- | --- |
| `value` | Scalar, array, structure, or `None` | Implicit Variant payload |
| `status` | `o6.StatusCode` | Absent status reads as `GOOD` |
| `sourceTimestamp` | `o6.DateTime` or `None` | Source timestamp |
| `serverTimestamp` | `o6.DateTime` or `None` | Server timestamp |
| `sourcePicoseconds`, `serverPicoseconds` | UInt16 or `None` | Additional timestamp fractions in 10-picosecond units |

```python
import datetime
import o6

value = o6.DataValue(value=o6.Int32(42))
value.status = o6.StatusCode.BAD_TIMEOUT
value.sourceTimestamp = o6.DateTime(datetime.datetime.now(datetime.timezone.utc))
assert o6.DataValue().status == o6.StatusCode.GOOD
```

Read responses and data-change notifications carry DataValues. Write requests
accept them; Write responses contain status codes. Method outputs are Variants
unless the method declares a DataValue output.

See [DateTime](primitive-types.md#datetime) for timezone handling and conversion
of timestamps to Python datetime values.

Assigning `None` or deleting a DataValue field clears that field's presence.

## ExtensionObject

Structured Python values can be assigned directly to fields that carry
ExtensionObjects. An explicit wrapper exposes `body` and `typeId`; an unknown
encoded type may remain an opaque payload.

```python
import o6
from o6.ns import ns0

details = ns0.datatypes.UpdateDataDetails()
details.nodeId = o6.NodeId("ns=1;s=Temperature")
details.performInsertReplace = ns0.datatypes.PerformUpdateType.REPLACE
details.updateValues = [o6.DataValue(value=o6.Double(23.5))]

request = ns0.datatypes.HistoryUpdateRequest()
request.historyUpdateDetails = [o6.ExtensionObject(details)]
```

## NumPy for arrays and large data

- Decoding allocates a NumPy array and copies the native elements.
- Encoding copies contiguous native-endian numeric arrays in bulk.
- Strided, non-native-endian, object, and string arrays use element conversion.
- Multidimensional Variant arrays preserve a valid shape; structure array fields are one-dimensional.

Returned arrays are independently owned; they are not zero-copy views of a
network response. See [wire-format mapping](../../implementation-details/wire-format-mapping.md).
