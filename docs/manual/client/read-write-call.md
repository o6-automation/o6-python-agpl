# Reading, Writing & Calling

Read and write node attributes or invoke Methods through a connected `Client`.
The snippets assume `client` is connected; see [Lifecycle & Configuration](lifecycle.md)
for connection and cleanup. IDs returned by this client are already mapped to
Python's namespace registry. For numeric IDs copied from another browser,
resolve the server's namespace URI first; see
[Registry and Namespace Mapping](../sdk-fundamentals/namespace/namespace-mapping-in-o6.md#process-indices-and-server-indices).
`ns=1` remains the application-local alias for this client's server.

## Reading attributes

`read()` reads the `Value` attribute of one node and returns a Python value:

```python
import o6
from o6.ns import ns0

value = client.read("ns=1;s=IntegerVariable")
```

The target is anything a `NodeId` can be built from: a NodeId string, an
`o6.NodeId`, an `ExpandedNodeId`, a [Node](../node-api/index.md) object or a generated
type class:

```python
client.read(o6.NodeId(2255))                       # NamespaceArray
client.read(client["ns=1;s=IntegerVariable"])      # a Node object
client.read(ns0.objtypes.BaseObjectType, attr="browseName")
```

A list of targets is read in one `Read` request, so it costs one round trip
instead of one per target:

```python
values = client.read([
    "ns=1;s=IntegerVariable",
    "ns=1;s=DoubleVariable",
])
# [np.int32(42), np.float64(3.14159)]
```

Numeric values are returned as NumPy scalars and arrays. They keep the exact
OPC UA data type (`Int32` stays 32 bit), and array data is cheap to process.

### Choosing the attribute

`attr` selects the attribute. It accepts an `o6.AttributeId` member or a name
string, matched case-insensitively and ignoring separators:

```python
client.read("ns=1;s=IntegerVariable", attr=o6.AttributeId.NODE_CLASS)
client.read("ns=1;s=IntegerVariable", attr="browseName")   # same as BROWSE_NAME
client.read("ns=1;s=IntegerVariable", attr="access_level")
```

Use it to read metadata: `BROWSE_NAME`, `DISPLAY_NAME`, `DESCRIPTION`,
`DATA_TYPE`, `VALUE_RANK`, `ARRAY_DIMENSIONS`, `ACCESS_LEVEL`, `HISTORIZING`,
`DATA_TYPE_DEFINITION` and the rest of `o6.AttributeId`.

### Values, or the whole `DataValue`

By default (`valueOnly=True`), `read()` returns the value for every
Good-severity status, including informational codes and flags, and raises for
Uncertain or Bad. Status and timestamps are discarded. With `valueOnly=False`,
you receive DataValues and interpret their quality yourself. Service failures
still raise, and the range-error handling below also applies:

```python
dv = client.read("ns=1;s=IntegerVariable", valueOnly=False)
print(dv.value, dv.status, dv.sourceTimestamp, dv.serverTimestamp)
```

Use this form when you need timestamps or status details, including
information carried by a successful read.

`timestampsToReturn` selects `SOURCE`, `SERVER`, `BOTH` or `NEITHER` from
`ns0.datatypes.TimestampsToReturn`. Omitting it (or passing `None`) selects
`SOURCE` on both client and server.

### Index ranges

`range` reads a slice of an array variable. It takes the inclusive OPC UA
string syntax or Python slices, which are stop-exclusive:

```python
client.read("ns=1;s=ArrayVariable", range="1:3")            # elements 1,2,3
client.read("ns=1;s=ArrayVariable", range=slice(1, 4))      # identical
client.read("ns=1;s=ArrayVariable", range=(slice(1, 4),))   # identical
client.read("ns=1;s=Matrix", range="1:3,4:6")               # two dimensions
client.read("ns=1;s=Matrix", range=(slice(1, 4), slice(4, 7)))
```

Slices must have explicit non-negative bounds and no step, because the OPC UA
`NumericRange` cannot express anything else. Violations raise `ValueError`
before a request is sent.

- A scalar range broadcasts across a target list. A range list must have
  exactly one entry per target.
- `None` and `""` request the entire attribute.
- Invalid, out-of-bounds and non-array ranges follow the read error policy
  below. With `valueOnly=False`, the returned DataValue keeps its error status;
  batch reads return one DataValue per target.
- A nonempty range on a non-Value attribute returns `BAD_INDEX_RANGE_NO_DATA`
  under the same error policy.
- Invalid range strings are OPC UA status failures. Malformed Python slices
  raise `TypeError` or `ValueError`.

An empty target list returns `[]` without a request, even when the client is
disconnected. Options and range-list lengths are still validated. Unsupported
Python argument types raise `TypeError`. Unknown attribute names, invalid
slices and mismatched range-list lengths raise `ValueError`. `valueOnly` must be
a bool. Only a Python list selects batch mode.

### What read raises

Client and server reads follow the shared
[error-handling contract](../sdk-fundamentals/builtin/statuscode.md#errors-and-status-codes):
value-only reads raise for Uncertain or Bad quality; full DataValue reads
retain per-target statuses. Service failures raise in either form. Batch
exceptions identify the failed target in `__notes__`. A disconnected client
raises `RuntimeError`.

Callable `node()` reads use the same value-only policy. It accepts all Good
severity codes, unlike the exact comparison performed by
[`StatusCode.check()`](../sdk-fundamentals/builtin/statuscode.md#good-severity-versus-exact-good).

```python
client.read("ns=1;s=DoesNotExist")
# o6.StatusCodeError: BadNodeIdUnknown (0x80340000)
```

## Writing attributes

`write()` has three forms.

One node, one value:

```python
status = client.write("ns=1;s=IntegerVariable", 42)
```

Parallel lists, when you want per-node index ranges:

```python
statuses = client.write(
    ["ns=1;s=IntegerVariable", "ns=1;s=DoubleVariable"],
    [100, 2.7182],
)
```

A mapping:

```python
statuses = client.write({
    "ns=1;s=IntegerVariable": 100,
    "ns=1;s=DoubleVariable": 2.7182,
})
```

Nonempty writes are sent as one `Write` request. Results:

- The single-node form returns one `o6.StatusCode`.
- The list and mapping forms return a list of status codes in input order, also
  for a one-element batch.
- Empty lists and mappings return `[]` without a service call.

Omit `value` for the mapping form; even explicit `value=None` conflicts with a
mapping. For the list form, `value` must be a list of matching length.
Anything else raises `ValueError` before writing. A list value for one scalar
target is an array. All targets are attempted despite per-target failures;
there is no rollback. `Server.write` takes the same arguments and returns the
same result types, with local administrative privileges.

Explicit `None` writes a null value in all three forms, like
`o6.DataValue(value=None)`. Nullable targets such as String variables accept
it. Non-nullable numeric targets return `BAD_TYPE_MISMATCH` and keep their
value. A typed empty array, such as `numpy.array([], dtype=numpy.int32)`, has
zero elements and is not null. `client.write(node)` without a value raises
`ValueError`. For callable nodes, `node()` reads and `node(None)` writes a
null, raising `StatusCodeError` if the target rejects it.

`attr` works as in `read()`, so you can write attributes other than Value:

```python
client.write("ns=1;s=IntegerVariable", o6.LocalizedText("Counter"), attr="displayName")
```

`range` accepts an inclusive string, a stop-exclusive slice or tuple of slices,
a broadcast range or a per-target list. `None` and `""` mean the whole
attribute. Nonempty ranges require the Value attribute. The single-node and
list forms support `range`; the mapping form does not:

```python
client.write("ns=1;s=ArrayVariable", [99, 98], range="1:2")
```

To write a status code or timestamps with the value, pass a `DataValue`.
Writing timestamps requires `AccessLevelType.TIMESTAMP_WRITE` and writing a
status requires `STATUS_WRITE`. Without them, the write returns
`BAD_WRITE_NOT_SUPPORTED`. `addVariable(..., writable=True)` grants neither;
pass `accessLevel=` to include them:

```python
dv = o6.DataValue()
dv.value = o6.Int32(77)
client.write("ns=1;s=IntegerVariable", dv)
```

Unlike `read()`, `Client.write()` never raises for a bad per-node status;
the status code is the return value. Service-level failures raise
`o6.StatusCodeError` with the actual `.code`. Python input errors raise
`TypeError` or `ValueError`. Check results yourself, or call
`StatusCode.check()`, which raises `StatusCodeError` for anything but `GOOD`:

```python
status = client.write("ns=1;s=IntegerVariable", "not an int")
print(status)                      # BAD_TYPE_MISMATCH
if o6.StatusCode.BAD in status:    # StatusCode is a full IntFlag
    ...
status.check()                     # raises o6.StatusCodeError
```

The `node(value)` shorthand checks the write result and raises `StatusCodeError`
on rejection, in both synchronous and asynchronous code.

Client, server and callable-node writes accept the same payloads. Value writes
infer the type from the Python payload; `123` selects Int32 and `23.5`
selects Double, as described in
[Choosing a value's type](../sdk-fundamentals/builtin/primitive-types.md#choosing-a-values-type).
The SDK does not read the target Variable's DataType and cast the payload to
match it. A mismatched type can return `BAD_TYPE_MISMATCH` even when the
numeric value would fit.

Use an explicitly sized value when the target needs another width. This
synchronous fragment assumes writable Float and Int64 Variables at the
placeholder NodeIds shown:

```python
client.write("ns=1;s=FloatValue", o6.Float(23.5)).check()
client.write("ns=1;s=Counter64", o6.Int64(2**40)).check()
```

A bare `23.5` would select Double; a bare `2**40` exceeds the inferred Int32
range and raises `OverflowError` during conversion.

Non-Value attributes require their expected data type, for example
`o6.LocalizedText("Description")` for Description, `o6.QualifiedName("Name")`
for BrowseName and `numpy.uint8(3)` for AccessLevel. No attribute-specific
coercion is applied. A `DataValue` with only a value is also accepted. Explicit
status or timestamp fields on non-Value attributes return
`BAD_WRITE_NOT_SUPPORTED`, even an explicit `GOOD` status.


## Calling methods

`call()` invokes an OPC UA method. It takes the object that owns the method,
the method and the input arguments in declaration order:

```python
status, greeting = client.call(
    "ns=1;s=TestMethods",
    "ns=1;s=MethodHelloString",
    ["World"],
)
# (StatusCode.GOOD, 'Hello World!')
```

The result is a tuple: the method's status code, then the decoded output
arguments. A method with no outputs returns a one-element tuple. `Node` objects
inside `inputArgs` are converted to NodeIds at any nesting depth, so you can
pass nodes where a method expects a NodeId.

A failing service raises `o6.StatusCodeError` with the original status in
`.code`. A method that returns a bad status code does not raise. Invalid
method selection and argument validation failures also return status tuples.
Available outputs are kept, so check the status before using them. Python
argument conversion failures raise Python exceptions such as `TypeError`.
`server.call()` has the same result contract with administrative privileges;
remote calls check session permissions.

`BAD_INVALID_ARGUMENT` usually means the argument list does not match the
method's `InputArguments` declaration in count, type or value rank.

The [Node API](../node-api/index.md) offers the same call in object syntax:

```python
client.objects.testMethods.MethodHelloString("World")
```

Method node calls check the method status and raise `StatusCodeError` on
failure. On success they return the status and outputs as a tuple. Use
`client.call()` to get a bad status as data. Both forms can be awaited from
async code.
