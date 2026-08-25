# Wire-format ↔ Python-value mapping

Every Python value that crosses the OPC UA boundary is encoded by
`PY2UA` and decoded by `UA2PY`. The two functions are the single
choke point for every protocol value the binding handles, including
struct fields, `Variant` payloads, `DataValue` payloads, and
`ReadValueId` parameters. This page describes the rules they follow
and the cases that surprise users.

!!! info "Prerequisites"
    The user-facing pages [DataType](../opcua-fundamentals/datatype.md)
    and [Container types](../sdk-fundamentals/builtin/container-types.md)
    describe the public conversion surface. The rest of this page
    spells out the dispatch rules and the corner cases that the public
    surface cannot afford to dwell on.

## The two dispatchers

`PY2UA` and `UA2PY` are the two dispatchers. They live in
[`src/types_convert.c`][src-types-convert] and are called by every
service-request encoder and by every value decoder in the binding.

The dispatch is by `UA_DATATYPEKIND_*` — the OPC UA type-kind taxonomy
that the open62541 type description exposes. Each kind has a small
chain of `case` labels; the dispatcher's job is to find the right
conversion.

The Python-side type guess is separate. The function `PY2UAType` in
[`src/types.c`][src-types] takes a Python type and returns the
`UA_DataType*` the binding will use to encode a value whose UA type
is not yet known. That guess is what callers like `client.write(...)`
need when they hand the binding a raw Python value and ask it to find
the right `Variant` shape.

## The kind-to-conversion table

The table below summarises the kind-to-conversion mapping. The
dispatcher is the only place the binding knows about the kinds;
the rest of the codebase talks about the data types.

| UA kind | Python side | Notes |
| --- | --- | --- |
| `BOOLEAN` | `bool` | Uses `numpy.bool` internally for array handling. |
| `SBYTE`, `INT16`, `INT32`, `INT64` | `int` | Signed. |
| `BYTE`, `UINT16`, `UINT32`, `UINT64` | `int` | Unsigned. |
| `FLOAT`, `DOUBLE` | `float` | Bare Python `float` is **always** mapped to `DOUBLE` by the type guess; see [Python float is double](#python-float-is-double). |
| `STRING`, `XMLELEMENT` | `str` | Empty strings encode as `NULL` on the wire; see [Empty string becomes NULL](#empty-string-becomes-null). |
| `BYTESTRING` | `bytes` | |
| `NODEID` | `o6.NodeId` | |
| `EXPANDEDNODEID` | `o6.ExpandedNodeId` | |
| `QUALIFIEDNAME` | `o6.QualifiedName` | Inner `name` field uses the empty-string rule. |
| `LOCALIZEDTEXT` | `o6.LocalizedText` | |
| `EXTENSIONOBJECT` | `o6.ExtensionObject` | |
| `GUID` | `uuid.UUID` | |
| `DATETIME` | `datetime.datetime` | |
| `STRUCTURE`, `OPTSTRUCT`, `UNION` | generated Python class | The Python class carries a `data` pointer that the dispatcher walks in lockstep with the UA structure layout. |
| `VARIANT` | `o6.Variant` (or any value) | Bare Python values are wrapped in a `Variant` via the type guess. |
| `DATAVALUE` | `o6.DataValue` | Carries status, value, source timestamp, server timestamp, and picosecond fields. |
| `DIAGNOSTICINFO` | `o6.DiagnosticInfo` | |
| `ENUM` | the matching Python enum | The integer value is transported; the enum class is the binding-side decoding. |

## Two encodings that look like one

The OPC UA binary protocol distinguishes two string encodings that
the OPC UA spec treats as semantically equal for *payload* values
but as semantically different for *filter* values:

| Encoding | Wire bytes | C name | Python name |
| --- | --- | --- | --- |
| `NULL` string | `ff ff ff ff` | `UA_STRING_NULL` | `None` |
| Empty string | `00 00 00 00`, `data = NULL` | zero-length `UA_String` | `""` |

The protocol treats them as equal for plain `Variant` values. The
trouble is that several services use `String` fields as filters
where the two encodings have different meanings:

- `ReadValueId.indexRange` — `NULL` means "no index range filter";
  a length-0 string is technically still no filter, but many stacks
  short-circuit *only* on the `NULL` form. With a length-0
  `indexRange`, the server enters the array-slice branch, validates
  the (empty) range against the scalar value, decides it does not
  match, and silently drops the data from notifications.
- `ReadValueId.dataEncoding.name` — same story.
- `QualifiedName.name` — same story, because the same field type is
  reused inside the structure.

The C reference client in open62541 always emits `NULL` for "unset".
The binding matches that convention.

### Empty string becomes NULL

In the `STRING` / `XMLELEMENT` branch of `PY2UA`, an empty Python
string produces a zero-initialised `UA_String` (i.e. `NULL`) instead
of a length-0 non-`NULL` value:

```c
case UA_DATATYPEKIND_STRING:
case UA_DATATYPEKIND_XMLELEMENT: {
    Py_ssize_t size;
    const char *buf = PyUnicode_AsUTF8AndSize(obj, &size);
    if(size < 0) return NULL;
    if(size == 0) {
        UA_String_init((UA_String*)p);
        return Py_None;
    }
    UA_String tmp = {(size_t)size, (UA_Byte*)(uintptr_t)buf};
    UA_StatusCode res = UA_String_copy(&tmp, (UA_String*)p);
    return (res == UA_STATUSCODE_GOOD) ? Py_None : NULL;
}
```

The same normalisation is applied to `QualifiedName.name` on both the
typed-`QualifiedName` path and the parse-from-string path.

The rule is symmetric on the way in: a `NULL` `UA_String` decodes to
an empty Python `""`. A length-0 non-`NULL` `UA_String` is rare on
the wire, but the binding accepts it and decodes it to `""` as well.
The semantic difference only matters for fields that act as filters.

The rule is *not* applied to `ByteString`. An empty Python `b""`
encodes as a length-0 non-`NULL` `UA_ByteString`, because the
filter-wire asymmetry does not apply to byte strings.

## Python float is double

Python's `float` is an IEEE-754 double-precision value. The binding
maps it to `UA_TYPES_DOUBLE` and not `UA_TYPES_FLOAT`. The relevant
code in `PY2UAType` is:

```c
if(t == &PyFloat_Type)
    return &UA_TYPES[UA_TYPES_DOUBLE];
```

The fix matters because `UA_TYPES_FLOAT` is 32-bit. Without the
override, a bare Python `3.14` is silently rounded to a 32-bit
float before it reaches the wire, and the resulting `Variant` is
`Float` rather than `Double`. Writing to a `Double` node then
fails with `BadTypeMismatch`, and the follow-up notification never
fires.

Array writes are the case that originally surfaced the bug. A bare
Python list of floats, written to a `Double[]` node, was being
packed as a `Float[]` `Variant`. The server rejected the variant
shape, and the subscription never saw the update.

Users who deliberately want a 32-bit `Float` value can still
construct one explicitly:

```python
import numpy as np
client.write(float_node, np.float32(3.14))
# or
client.write(float_node, o6.Float(3.14))
```

Only the implicit type guess for a bare Python `float` was changed.
The explicit conversion path was always correct.

### How the dispatcher uses the type

The dispatcher is the one that writes the actual bytes. `PY2UA_float`
takes the `UA_DataType*` and writes either a `double` or a `float`
to the destination pointer:

```c
if(type->typeKind == UA_DATATYPEKIND_DOUBLE)
    *(double*)p = val;
else
    *(float*)p = val;
```

So the binding has two stages: the type guess (`PY2UAType`) decides
which `UA_DataType*` the dispatcher will use, and the dispatcher
(`PY2UA_float`) writes the value into that destination. The bug was
in the first stage; the second stage was always correct.

## DataValue handling

A `DataValue` carries up to five fields: the value itself, the status
code, the source timestamp, the server timestamp, and the picoseconds
fields for the two timestamps. The Python binding exposes the
`DataValue` type and treats the optional fields as ordinary Python
attributes.

The two surfaces that read and write `DataValue` are:

- **Server-side Variable callbacks.** A read callback may return a
  `DataValue` to set timestamps and picoseconds explicitly. The
  binding copies the value-bearing fields and forwards the
  status bits to the open62541 response. A bare `(StatusCode, value)`
  tuple takes the server's current time as the source timestamp and
  the system clock as the picoseconds field.
- **Client-side read and MonitoredItem notifications.** The decoded
  `DataValue` is exposed on the read result. The `value` field is the
  Python payload; the `statusCode` field is the OPC UA `StatusCode`;
  the two timestamps are `datetime.datetime` instances, possibly
  `None` when the wire side did not set them.

The dispatcher turns the wire `UA_DataValue` into a `PyUADataValue`
by walking the kind chain. The Python-side `value` is then decoded
by `UA2PY` recursively with the value's own `UA_DataType*`. The
status and timestamps are copied field by field.

## Variant framing

The `Variant` framing is the same as the inner value framing — the
`UA_DataType*` of the variant body is the binding's pointer to
encode the value. The binding does not wrap a Python value in a
`Variant` class on the way out; the public surface accepts a raw
Python value and the dispatcher does the framing.

The four cases that come up on the wire are:

- **Scalar value.** Typed directly. The Variant's `type` is the
  inferred UA type.
- **One-dimensional array.** Python `list` of the element type. The
  Variant's `type` is the matching array type.
- **Multi-dimensional array.** Not directly supported at the public
  API; the binding enforces one-dimensional arrays.
- **Empty Variant.** A `None` value encodes as a Variant with body
  type `UA_TYPES_EXTENSIONOBJECT` and a `NULL` body. The same
  encoding is produced by `o6.Variant.empty()`.

The dispatcher's array branching is the one place where the type
guess and the element type have to agree. The public API does not
expose the multi-dimensional case; the binding's `Variant` wrapper
exists for the cases where the OPC UA wire shape needs an explicit
framing.

## Where to look in the code

- `PY2UA` and `UA2PY` in [`src/types_convert.c`][src-types-convert] —
  the kind dispatchers.
- `PY2UAType` in [`src/types.c`][src-types] — the bare-Python type
  guess.
- `PY2UA_float` in [`src/types_convert.c`][src-types-convert] — the
  dispatcher's float path, which writes to either `double` or
  `float` based on the destination type.
- The `UA_String` / `QualifiedName` empty-string normalisations in
  [`src/types_convert.c`][src-types-convert] — the two patches that
  keep the wire bytes aligned with the C reference client.

## See also

- [DataType](../opcua-fundamentals/datatype.md) — the OPC UA
  type-kind taxonomy from the spec's perspective.
- [Container types](../sdk-fundamentals/builtin/container-types.md) —
  the structured Python types the dispatcher builds.
- [Primitive types](../sdk-fundamentals/builtin/primitive-types.md) —
  the public conversion surface for scalars.
- [Namespace matching](namespace-matching.md) — the matching
  algorithm that has to decide between a `Float` and `Double` type
  identification when the Variant comes back from the server.

[src-types-convert]: https://github.com/o6-automation/o6-python/blob/main/src/types_convert.c
[src-types]: https://github.com/o6-automation/o6-python/blob/main/src/types.c
