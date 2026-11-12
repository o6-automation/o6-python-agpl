# Working with Local Nodes

Use typed node handles and server operations to inspect or update the local address space.
The snippets assume an existing `server` and nodes created with
[the address-space helpers](address-space.md).

## Finding existing nodes

The server exposes the same four typed folder handles as the client:

| Handle | Standard NodeId |
| --- | --- |
| `server.root` | `i=84` |
| `server.objects` | `i=85` |
| `server.types` | `i=86` |
| `server.views` | `i=87` |

Each is an `o6.node.ObjectNode`, available immediately, also before startup and
inside an async task. Use them as creation parents or navigation entry points:

```python
plant = server.addObject("Plant", server.objects)
temperature = server.addVariable("Temperature", plant, 22.5, nodeId="ns=1;s=Temperature")
assert server.objects.plant.temperature is temperature
assert server.objects["/1:Plant/1:Temperature"][0] is temperature
assert server["ns=1;s=Temperature"] is temperature
```

`server[nodeId]` accepts the same NodeId-like inputs as `client[nodeId]`:
strings, numeric namespace-zero IDs, `NodeId`, `ExpandedNodeId`, node handles
and registered type classes. It returns the matching `o6.node` class and keeps
existing modeled Object/Variable specialization and application state. Repeated
lookups return the same Python object as creation and navigation. Client handles
identify the same OPC UA nodes but are not the server's canonical Python
objects.

| Lookup caller | `server[nodeId]` result |
| --- | --- |
| Synchronous code, before or after startup | Node handle |
| Async task, before or after startup, on either loop | Awaitable resolving to a node handle |

```python
async def findTemperature(server):
    node = await server["ns=1;s=Temperature"]
    matches = await server.objects["/1:Plant/1:Temperature"]
    assert matches[0] is node
    return node
```

Folder access never needs `await`. Child and path operations follow the
[Node API's awaitability rules](../node-api/read-write-call.md#async-operations). Unknown or deleted IDs
raise `o6.StatusCodeError` with `.code == o6.StatusCode.BAD_NODE_ID_UNKNOWN`.
A reused ID resolves to the replacement object. Retained handles, including
folder handles, can outlive deletion or server cleanup as invalid tombstones.
They do not keep the server alive and do not become live again when an ID is
reused. Lookup after server cleanup raises `RuntimeError`.

`objectsNode`, `typesNode` and `serverNode` return the NodeIds `i=85`, `i=86`
and `i=2253`. Local discovery does not
add client sessions or network discovery services; server construction and
security remain separate server APIs.

## Reading and writing server-side

The server reads and writes its own nodes without going through a session:

```python
value = server.read("ns=1;s=Temp")
server.write("ns=1;s=Temp", 23.5)
```

Both take a single target or a list of targets. Reads and writes take the same
keyword-only `attr` argument as the client:

```python
server.read("ns=1;s=Temp", attr="browseName")
server.read("ns=1;s=Temp", attr=o6.AttributeId.DISPLAY_NAME)
server.write("ns=1;s=Temp", o6.LocalizedText("Kettle temperature"), attr="displayName")
```

Attribute names are case-insensitive and ignore separators: `"browseName"`,
`"BrowseName"` and `"browse_name"` are the same attribute.

A list read returns values in input order. Writes accept a scalar target/value,
equal-length target/value lists, or a target-to-value mapping:

```python
values = server.read(["ns=1;s=Temp", "ns=1;s=Counter"])
statuses = server.write(["ns=1;s=Temp", "ns=1;s=Level"], [30.0, 31.0])
statuses = server.write({"ns=1;s=Temp": 30.0, "ns=1;s=Level": 31.0})
for status in statuses:
    status.check()
```

A scalar write returns one `o6.StatusCode`. Lists and mappings return a list in
input order, also for a one-element batch; empty batches return `[]`. Per-target
failures stay in the results, and later targets are still attempted. Local
batches run sequentially without rollback. Local writes have administrative
privileges; remote session permissions can produce different statuses.

Explicit `None` writes a null value in scalar, list and mapping forms, like
`o6.DataValue(value=None)`. Nullable targets such as String Variables accept it.
Non-nullable numeric targets return `BAD_TYPE_MISMATCH` and keep their value. A
typed empty NumPy array stays a zero-element array. `server.write(node)` without
a value raises `ValueError`. Callable `node()` reads; `node(None)` writes a null
and raises `StatusCodeError` if rejected.

To write one value to several targets, pass
`server.write(nodes, [value] * len(nodes))` or a mapping. A list value for a
scalar target is written as an array.

Input shapes are validated before writing. These raise `ValueError`: mismatched
lists, a scalar value for a target list, a separate value argument for a mapping
(including `None`), or ranges with a mapping. Ranges can broadcast or be passed
as a list aligned with targets. `None` and `""` mean the entire attribute. An
invalid Python range raises `TypeError` or `ValueError`. An invalid OPC UA range
string is reported through the target's status.

`range=` reads or writes a slice of an array value, using OPC UA's inclusive
string syntax or stop-exclusive Python slices. Writes allow ranges only on the
`Value` attribute. Reads return `BAD_INDEX_RANGE_NO_DATA` for a nonempty range
on another attribute; `None` and `""` read the entire attribute:

```python
server.read("ns=1;s=Samples", range="1:3")           # elements 1,2,3
server.read("ns=1;s=Samples", range=slice(1, 4))     # identical
server.write("ns=1;s=Samples", [99, 98], range="1:2")
```

`server.read` supports the [same read contract as the client](../client/read-write-call.md#reading-attributes):
`attr`, `timestampsToReturn`, `valueOnly` and `range` are keyword-only. Scalar
targets return scalars, lists return results in input order, and empty lists
return `[]`.

```python
from o6.ns import ns0

dv = server.read("ns=1;s=Temp", valueOnly=False,
                 timestampsToReturn=ns0.datatypes.TimestampsToReturn.BOTH)
print(dv.value, dv.status, dv.sourceTimestamp, dv.serverTimestamp)
```

`timestampsToReturn` defaults to `SOURCE`; `SERVER`, `BOTH` and `NEITHER` are
also supported. Read callbacks receive `includeSourceTimestamp=True` for SOURCE
and BOTH (including the default) and `False` for SERVER and NEITHER.

Raw DataValues keep per-target statuses and supported metadata, including
failures. Value-only reads accept all Good-severity statuses and discard status
and timestamps. They raise `o6.StatusCodeError` for Uncertain or Bad; `.code`
holds the status and an exception note names the failed batch index. Service
failures raise the same exception. Python input errors raise `TypeError` or
`ValueError`.

Local reads have administrative privileges. Client reads use the remote
session's permissions, so differently authorized callers can get different
statuses. Local batches read targets sequentially and are not an atomic
snapshot. Reads can be awaited, also from another running event loop.

Writing an `o6.DataValue` to the `Value` attribute stores the value with its
explicit status and supported source timestamp metadata:

```python
import datetime

dv = o6.DataValue()
dv.value = o6.Double(42.0)
dv.sourceTimestamp = o6.DateTime(datetime.datetime.now(datetime.timezone.utc))
server.write("ns=1;s=Temp", dv)
```

For other attributes, the DataValue payload must have the attribute's OPC UA
DataType. For example, Description requires `o6.LocalizedText`:

```python
server.write(
    "ns=1;s=Temp",
    o6.DataValue(value=o6.LocalizedText("Kettle temperature")),
    attr=o6.AttributeId.DESCRIPTION,
)
```

A wrongly typed DataValue payload returns a bad status and changes neither
Value nor the requested attribute. Non-Value attributes cannot store DataValue
status or timestamp metadata. Supplying any of it, even an explicit `Good`,
returns `BadWriteNotSupported` before the target changes, on client and server.
Bare non-Value payloads must also have the exact attribute DataType, for
example `o6.LocalizedText` for Description and `numpy.uint8` for AccessLevel.
No attribute-specific coercion is applied. Ordinary Value writes keep their
type inference, including for bare Python integers.

Both public write methods return `MaybeAwaitable[StatusCode | list[StatusCode]]`.
Async tasks await the result, also from another running event loop. Service
failures raise `o6.StatusCodeError` with `.code` set. For exception-based
handling, check each returned status. Typed `node(value)` calls check write
failures themselves and raise:

```python
status = await server.write(temperature, 23.5)
status.check()
```

Value range writes keep source timestamps and source picoseconds, and require
the supplied status to match the stored status. The server generates server
timestamps on reads; a supplied server timestamp is not returned. As with bare
values, `range=` on another attribute raises `ValueError`.

`server.read` and callable `node()` reads accept Good severity, including
informational codes and flags, and raise `o6.StatusCodeError` for Uncertain or
Bad. To inspect quality on successful reads too, use
`server.read(..., valueOnly=False)` and check the returned DataValue's status.
If you store an Uncertain status, a value-only read raises:

```python
uncertain = o6.DataValue()
uncertain.value = o6.Double(1.0)
uncertain.status = o6.StatusCode.UNCERTAIN_SENSOR_NOT_ACCURATE
server.write("ns=1;s=Temp", uncertain)
server.read("ns=1;s=Temp")     # raises StatusCodeError: UncertainSensorNotAccurate (0x40930000)
```

### Node handles

The handle returned by `addX` is usually more convenient than a NodeId.
Calling a Variable node with no argument reads it, calling it with one argument
writes it, and `_value` is the property form:

```python
temperature()             # 22.5
temperature(23.5)         # write
temperature._value        # 23.5
temperature._value = 24.0
temperature(attr="browseName")
```

Attribute access browses to children by BrowseName, using the lowerCamelCase
spelling for instances. `dir()` lists the children, which helps in a REPL:

```python
plantObject.temperature()   # the child Variable, read
plantObject.serial()
dir(plantObject)            # ['add', 'counter', 'level', 'samples', 'serial', 'temperature']
```

A Method reached through its Object is bound to that Object and can be called
directly. The bare handle needs the Object passed explicitly:

```python
plantObject.add(2.0, 3.0)                # (StatusCode.GOOD, 5.0)
method(2.0, 3.0, object=plantObject)     # same call, unbound handle
```

`o6.NodeId(node)` converts any handle back to its NodeId. The full syntax,
including browse paths and the awaitable forms, is in
[Node API](../node-api/index.md).

## Methods

A Method callback receives the Object the Method was invoked on, then the input
arguments in declaration order. It returns a tuple whose first element is a
status code:

```python
def divide(node, dividend, divisor):
    if divisor == 0:
        return (o6.StatusCode.BAD_INVALID_ARGUMENT,)
    return (o6.StatusCode.GOOD, dividend / divisor)
```

A Bad status can be returned alone. A non-Bad status must be followed by
exactly the number of outputs the Method declares. Callbacks can be
`async def` with the same arguments and result tuple. Keep per-call state on
`node` or in a closure; there is no callback context. See
[Server callbacks](callbacks.md#methods) for the full contract.

To invoke a Method from inside the server, use `server.call`. It has the same
result contract as `client.call`:

```python
status, *outputs = server.call(plantObject, method, [10.0, 4.0])
status.check()
quotient = outputs[0]
```

Both return `(statusCode, *output_arguments)`, also for bad Method statuses,
invalid Method selection and argument-validation failures. Outputs are the
actual Method result; a result with no outputs is `(statusCode,)`. Node handles
are accepted for Object and Method IDs and normalized inside input arguments.
Synchronous and asynchronous callbacks use the same result contract. Await the
call from asynchronous code, also from a separate caller loop.

A Method without an implementation returns `BAD_NOT_IMPLEMENTED`: a declared
Method that no callback is bound to, and the Methods that o6 does not
implement, such as `Enable`, `Disable`, `Acknowledge` and `AddComment` of an
alarm instance and `ConditionRefresh`, because o6 binds no Alarms & Conditions
implementation. Methods that open62541 implements, such as `GetMonitoredItems`,
keep their behavior.

Service or local submission failures raise `o6.StatusCodeError`; `.code` holds
the original status. Python conversion errors raise Python exceptions such as
`TypeError`. Local calls have administrative privileges; remote calls check the
session's permissions.

To require exact `GOOD`, call `status.check()`. The shared
[error-handling contract](../sdk-fundamentals/builtin/statuscode.md#errors-and-status-codes)
distinguishes returned operation statuses from raised service failures:

```python
try:
    status, *outputs = server.call(plantObject, method, [10.0, 0.0])
    status.check()
except o6.StatusCodeError as error:
    print(error.symbol)      # BadInvalidArgument
```

Typed Method node calls such as `plantObject.divide(10.0, 4.0)` check the
Method status and raise on failure, locally and remotely. Their successful
result still includes the leading status.

To replace a Method's behaviour later, use `server.implement`; see
[Replacing behavior](callbacks.md#replacing-behavior).

## Browsing and address-space queries

`server.browse` and `client.browse` return a complete flat list of
`ReferenceDescription` objects and follow continuation points internally.

```python
references = server.browse(plantObject, resultMask=ns0.datatypes.BrowseResultMask.ALL)
for reference in references:
    print(reference.browseName, reference.nodeClass, reference.nodeId)
```

As on the client, `resultMask` defaults to `BrowseResultMask.ALL`. Pass only
the bits you need to shrink the response. `direction=`, `reftype=`, `refsubtypes=` and
`nodeClassMask=` narrow the traversal as on the client. Async tasks await the
call for Node and NodeId targets.

For explicit pagination, use `server.browsePage(..., maxReferences=...)` and
`server.browseNext(releaseContinuationPoint, continuationPoint)`. See
[Explicit pages](#explicit-pages) for continuation and release
examples.

`browseRecursive` walks the whole subtree in one call and returns a flat list of
`ExpandedNodeId` values:

```python
everything = server.browseRecursive(server.objectsNode)
```

Browse paths resolve without constructing a request:

```python
path = ns0.datatypes.BrowsePath()
path.startingNode = o6.NodeId(server.objectsNode)
path.relativePath = ns0.datatypes.RelativePath("/1:Plant/1:Temperature")

result = server.translateBrowsePathsToNodeIds(path)
print(result.statusCode, [str(t.targetId) for t in result.targets])
```

`browseSimplifiedBrowsePaths(origin, [QualifiedName, ...])` does the same for a
plain list of BrowseNames. `translateBrowsePaths(request)` takes a full
`TranslateBrowsePathsToNodeIdsRequest` for the service-level form.

`forEachChildNode(nodeId, callback)` calls
`callback(childId, isInverse, referenceTypeId)` for every reference on a
node, including the reference to its parent and its `HasTypeDefinition`
reference. It is a raw reference iterator, not a children-only browse.
`findDataType(nodeId)` returns the Python type registered for a DataType:

```python
server.findDataType(o6.NodeId(o6.Double))    # <class 'numpy.float64'>
```

### Explicit pages

`server.browsePage(target, maxReferences=...)` returns one page as a
`BrowseResult` with `references` and `continuationPoint` fields.
`maxReferences=0` sets no caller limit; backend limits can still produce a
continuation point.

`browseNext(False, token)` continues and `browseNext(True, token)` releases.
Both return a list of pages, one per token, so a single token returns a
one-element list. Tokens belong to the server that issued them. Update the token
before processing each page, and release it if processing stops:

```python
page = server.browsePage(target, maxReferences=100)
token = page.continuationPoint
try:
    while True:
        for reference in page.references:
            print(reference.nodeId)
        if not token:
            break
        page = server.browseNext(False, token)[0]
        token = page.continuationPoint
finally:
    if token:
        server.browseNext(True, token)
```

Async tasks also await `browsePage` and `browseNext`. The await resolves to
the page result; do not await that result a second time.

`browseNext` raises `StatusCodeError` for failed page statuses. If a batch
contains a failure, it first tries to release continuation points in the
successful pages. Clients also have `browsePage` and `browseNext`; see
[client pagination](../client/browsing.md#paging-and-translating-browse-paths).
Raw `serviceBrowse` and `serviceBrowseNext` return response objects whose status
fields callers must check.
