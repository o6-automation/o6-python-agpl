# Building the address space

## Finding existing nodes

The server exposes the same four typed folder handles as the client:

| Handle | Standard NodeId |
| --- | --- |
| `server.root` | `i=84` |
| `server.objects` | `i=85` |
| `server.types` | `i=86` |
| `server.views` | `i=87` |

Each is an `o6.node.ObjectNode`, available immediately even before startup or
inside an async task. Use them as creation parents or navigation entry points:

```python
plant = server.addObject("Plant", server.objects)
temperature = server.addVariable("Temperature", plant, 22.5, nodeId="ns=1;s=Temperature")
assert server.objects.plant.temperature is temperature
assert server.objects["/1:Plant/1:Temperature"][0] is temperature
assert server["ns=1;s=Temperature"] is temperature
```

`server[nodeId]` accepts the same NodeId-like inputs as `client[nodeId]`: strings,
numeric namespace-zero IDs, `NodeId`, `ExpandedNodeId`, node handles, and
registered type classes. It resolves the node kind to the matching `o6.node`
class and preserves existing modeled Object/Variable specialization and
application state. Repeated server lookup returns the same Python object as
creation and navigation. Client handles identify the same UA nodes but do not
promise the server's canonical Python object identity.

| Lookup caller | `server[nodeId]` result |
| --- | --- |
| Synchronous code, before or after startup | Node handle |
| Async task before startup | Awaitable resolving to a node handle |
| Async task on the server's loop | Awaitable resolving to a node handle |
| Async task on another loop | Awaitable resolving to a node handle |

```python
async def findTemperature(server):
    node = await server["ns=1;s=Temperature"]
    matches = await server.objects["/1:Plant/1:Temperature"]
    assert matches[0] is node
    return node
```

Folder access itself never needs `await`; child and path operations retain
the [Node API's awaitability rules](../node-api.md). Unknown or deleted IDs
raise `o6.StatusCodeError` with `.code == o6.StatusCode.BAD_NODE_ID_UNKNOWN`.
Reusing an ID resolves to the replacement object. Retained handles, including
folder handles, can outlive deletion or server cleanup as invalid tombstones;
they do not keep the server alive or become live again when an ID is reused.
Lookup after server cleanup raises `RuntimeError`.

The compatibility properties `objectsNode`, `typesNode`, and `serverNode`
still return `NodeId` values for `i=85`, `i=86`, and `i=2253`. Typed folders are
additional entry points. Local discovery does not add client sessions or
network discovery services; server construction and security remain separate
server APIs.

## Building the address space imperatively

Every `addX` helper takes a display/browse name and a parent, and returns a
node handle from [`o6.node`](../node-api.md), directly or through an awaitable.
The handle is a live view of the
node: calling it reads or writes, attribute access browses to children.

```python
plantObject = server.addObject("Plant", server.objectsNode, nodeId="ns=1;s=Plant")
temperature = server.addVariable("Temperature", plantObject, 22.5, nodeId="ns=1;s=Temp")
```

### Creation in synchronous and asynchronous code

`addObject`, `addVariable`, `addMethod`, `addObjectType`, `addVariableType`,
`addReferenceType`, and `addView` return `MaybeAwaitable` handles:

| Caller | Return value |
| --- | --- |
| Async task, before startup or on either loop | Awaitable resolving to the handle |
| Ordinary synchronous code | Handle directly |
| Synchronous SDK callback on the owning loop | Immediate handle; pending operations remain awaitable |

In async code, always await creation before using or configuring the node:

```python
async def addMachine(server):
    machine = await server.addObject("Machine", server.objectsNode)
    temperature = await server.addVariable("Temperature", machine, 22.5)
    await temperature(23.0)
    return machine
```

The returned handle belongs to the server and preserves its canonical node
identity. Variable initialization and method callback installation complete
before the awaitable resolves. Creation errors reach the caller through the
awaitable. Cancelling it does not guarantee that creation is prevented and
does not roll back a native creation that has already completed; inspect the
address space before retrying with the same identifier.

`client.addObject` and `client.addVariable` expose the same convenience inputs
and return usable remote handles. Both conveniences default `parentReference`
to `Organizes`; pass `parentReference=ns0.reftypes.HasComponent` explicitly when
that relationship is intended. Attribute-based client `addObjectNode` and
`addVariableNode` keep their existing `HasComponent` default and NodeId results.
History registration and Python callback installation remain server operations.

`nodeId=` is optional everywhere. Omit it and the server assigns one; pass it
and the identifier is pinned, which is what clients, historical data, and stored
configuration all depend on. `ns=` (default `1`) selects the namespace index of
the *BrowseName* — the name's namespace, not the NodeId's.

### Variables

`addVariable` infers the OPC UA data type and value rank from the initial Python
value, so a `float` becomes a scalar `Double`, a list becomes a one-dimensional
array, and a NumPy array keeps its dimensionality:

```python
server.addVariable("Temperature", plantObject, 22.5)              # Double, scalar
server.addVariable("Samples", plantObject, [1, 2, 3, 4, 5])       # Int32, 1-D array
server.addVariable("Serial", plantObject, "SN-1", writable=False) # String, read-only
server.addVariable("Counter", plantObject, o6.Int32(0), dataType=o6.Int32)
server.addVariable("Level", plantObject, 0.0, historizing=True)
```

- `dataType=` pins the type explicitly instead of inferring it. The value rank
  is still derived from the value, so arrays keep working. Empty NumPy arrays
  use their dtype when `dataType` is omitted; empty Python sequences require an
  explicit `dataType`, for example `server.addVariable("Samples", plantObject,
  [], dataType=o6.Int32)`. Empty arrays keep their declared `ValueRank`, but
  their values read back as flat zero-length arrays because
  [OPC UA Binary omits empty-array dimensions](https://reference.opcfoundation.org/specs/OPC-10000-6/5.2.2.16).
- `writable=False` gives the node `CurrentRead` only; the default is
  read *and* write.
- `historizing=True` registers history immediately on a running server, which
  requires a configured history database. Before startup, registration is deferred
  until `start()` — see [Historical data](operations.md#historical-data).
- `typeDefinition=` selects the VariableType; the default is
  `BaseDataVariableType`.

With no `value`, the node is created as a scalar `Int32`.

### Objects, types, views, and methods

```python
machineType = server.addObjectType("MachineType", nodeId="ns=1;s=MachineType")
tempType = server.addVariableType("TempType", dataType=o6.Double, valueRank=-1)
controls = server.addReferenceType("Controls", inverseName="ControlledBy")
production = server.addView("Production")
```

`addObjectType` and `addVariableType` default their parent to `BaseObjectType`
and `BaseVariableType`; `addReferenceType` defaults to
`NonHierarchicalReferences` and additionally takes `symmetric=` and
`abstract=`. `addView` parents itself under the `Views` folder and takes
`containsNoLoops=` (default `True`) and `eventNotifier=`.

The reference type linking a new node to its parent is chosen per node class and
is not a parameter of these helpers: Objects, Variables, and Views are attached
with `Organizes`, type nodes with `HasSubtype`, and Methods with
`HasComponent`. When you need a different edge, create the node and then use
[`addReference`](#references-and-deletion).

Methods pair a node with a Python callback:

```python
from o6.ns import ns0

def add(node, a, b):
    return (o6.StatusCode.GOOD, a + b)

method = server.addMethod(
    "Add",
    plantObject,
    add,
    inputArgs=[
        ns0.datatypes.Argument(name="A", dataType=o6.Double, valueRank=o6.ValueRank.SCALAR),
        ns0.datatypes.Argument(name="B", dataType=o6.Double, valueRank=o6.ValueRank.SCALAR),
    ],
    outputArgs=[
        ns0.datatypes.Argument(name="Sum", dataType=o6.Double, valueRank=o6.ValueRank.SCALAR),
    ],
    nodeId="ns=1;s=Add",
)
```

`valueRank=o6.ValueRank.SCALAR` on each `Argument` is not decoration. The
default value rank is `0`, which means *array*, and a client passing a scalar
against an array declaration gets `BadInvalidArgument` before your callback ever
runs. This is the single most common cause of a method that "does not work".

Method callbacks are covered in [Server callbacks](callbacks.md#methods).

## Reading and writing server-side

The server reads and writes its own nodes without going through a session:

```python
value = server.read("ns=1;s=Temp")
server.write("ns=1;s=Temp", 23.5)
```

Both take a single target or a list of targets. Reads use the same keyword-only
`attr` argument as the client, and writes use the same keyword placement:

```python
server.read("ns=1;s=Temp", attr="browseName")
server.read("ns=1;s=Temp", attr=o6.AttributeId.DISPLAY_NAME)
server.write("ns=1;s=Temp", o6.LocalizedText("Kettle temperature"), attr="displayName")
```

Attribute names are matched case-insensitively and ignore separators, so
`"browseName"`, `"BrowseName"`, and `"browse_name"` are the same attribute.

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
input order, including a one-element batch; empty batches return `[]`. Per-target
failures remain in the results, and later targets are still attempted. Local
batches execute sequentially without rollback. Local writes have administrative
privileges; remote session permissions can produce different statuses.

Explicit `None` writes a null value in scalar, list, and mapping forms, matching
`o6.DataValue(value=None)`. Nullable targets such as String variables accept it;
non-nullable numeric targets return `BAD_TYPE_MISMATCH` without changing their
value. A typed empty NumPy array remains a zero-element array. Omitting the value
in `server.write(node)` raises `ValueError`; callable `node()` reads, while
`node(None)` writes a null and raises `StatusCodeError` if rejected.

To migrate a server broadcast call, replace `server.write(nodes, value)` with
`server.write(nodes, [value] * len(nodes))`, or use a mapping. A list value for a
scalar target remains an array. Pass the attribute with `attr=`. There is no
positional-attribute or implicit-broadcast compatibility form.

Input shapes are validated before writing: mismatched lists, a scalar value for
a target list, a separate value argument for a mapping (including `None`), or
ranges with a mapping raise `ValueError`. Ranges can broadcast or be supplied as
a list aligned with targets. `None` and `""` mean the entire attribute. An invalid
Python range raises `TypeError`/`ValueError`; an invalid OPC UA range string is
reported through the target's status.

`range=` reads or writes a slice of an array value, using OPC UA's inclusive
string syntax or stop-exclusive Python slices. Writes restrict ranges to the
`Value` attribute. Reads return `BAD_INDEX_RANGE_NO_DATA` for a nonempty range
on another attribute; `None` and `""` read the entire attribute:

```python
server.read("ns=1;s=Samples", range="1:3")           # elements 1,2,3
server.read("ns=1;s=Samples", range=slice(1, 4))     # identical
server.write("ns=1;s=Samples", [99, 98], range="1:2")
```

`server.read` supports the [same read contract as the client](../client/address-space.md#reading-attributes):
`attr`, `timestampsToReturn`, `valueOnly`, and `range` are keyword-only. Scalar
targets return scalars, lists return results in input order, and empty lists
return `[]`. Use `attr=` for existing positional attribute calls; there is no
positional compatibility form.

```python
from o6.ns import ns0

dv = server.read("ns=1;s=Temp", valueOnly=False,
                 timestampsToReturn=ns0.datatypes.TimestampsToReturn.BOTH)
print(dv.value, dv.status, dv.sourceTimestamp, dv.serverTimestamp)
```

Timestamp selection defaults to `SOURCE`; `SERVER`, `BOTH`, and `NEITHER` are
also supported. Read callbacks receive `includeSourceTimestamp=True` for
SOURCE and BOTH, including the default read; SERVER and NEITHER pass False.
Raw DataValues retain per-target statuses and supported
metadata, including failures. Value-only reads accept all Good-severity statuses
and discard status and timestamps. They raise `o6.StatusCodeError` for Uncertain
or Bad, with `.code` preserving the status and an exception note identifying
the failed batch index. Service failures use the same exception
family. Python input errors use `TypeError` or `ValueError`.

Local reads retain administrative privileges. Client reads still use the remote
session's permissions, so differently authorized callers can receive different
statuses. Local batches read targets sequentially and do not promise an atomic
snapshot. Reads can also be awaited, including from another running event loop.

Passing an `o6.DataValue` to `write` for the `Value` attribute stores the value
together with its explicit status and supported source timestamp metadata:

```python
import datetime

dv = o6.DataValue()
dv.value = o6.Double(42.0)
dv.sourceTimestamp = o6.DateTime(datetime.datetime.now(datetime.timezone.utc))
server.write("ns=1;s=Temp", dv)
```

For other attributes, the DataValue payload must have the attribute's OPC UA
datatype. For example, Description requires `o6.LocalizedText`:

```python
server.write(
    "ns=1;s=Temp",
    o6.DataValue(value=o6.LocalizedText("Kettle temperature")),
    attr=o6.AttributeId.DESCRIPTION,
)
```

An incorrectly typed DataValue payload returns a bad status without changing
Value or the requested attribute. Non-Value attributes cannot store DataValue
status or timestamp metadata; supplying any of it (including explicit `Good`)
returns `BadWriteNotSupported` before changing that target on both client and
server. Bare non-Value payloads must also have the exact attribute datatype:
use `o6.LocalizedText` for Description and `numpy.uint8` for AccessLevel.
Attribute-specific coercion is not applied. Ordinary Value writes retain their
existing type inference, including bare Python integers.

Both public write methods return `MaybeAwaitable[StatusCode | list[StatusCode]]`.
Async tasks await the result, including from another running event loop. Service
failures raise `o6.StatusCodeError`, preserving `.code`. To retain exception-based
handling, check each returned status; typed `node(value)` calls already check
write failures and continue to raise:

```python
status = await server.write(temperature, 23.5)
status.check()
```

Value range writes preserve source timestamps and source picoseconds, and
require the supplied status to match the stored status. Server timestamps on
reads are generated by the server; they do not round-trip a supplied timestamp.
As with bare values, `range=` on another attribute raises `ValueError`.

`server.read` and callable `node()` reads accept Good severity, including
informational codes and flags, and raise `o6.StatusCodeError` for Uncertain or
Bad. To inspect quality even on successful reads, choose
`server.read(..., valueOnly=False)` and interpret the returned DataValue's
status yourself. Write status handling and `StatusCode.check()` are unchanged.
If you deliberately store an Uncertain status, expect a value-only read to raise:

```python
uncertain = o6.DataValue()
uncertain.value = o6.Double(1.0)
uncertain.status = o6.StatusCode.UNCERTAIN_SENSOR_NOT_ACCURATE
server.write("ns=1;s=Temp", uncertain)
server.read("ns=1;s=Temp")     # raises StatusCodeError: UncertainSensorNotAccurate
```

### Node handles

The handle returned by every `addX` call is usually more convenient than a
NodeId. Calling a Variable node with no argument reads it, calling it with one
argument writes it, and `_value` is the property form of the same thing:

```python
temperature()             # 22.5
temperature(23.5)         # write
temperature._value        # 23.5
temperature._value = 24.0
temperature(attr="browseName")
```

Attribute access browses to children by BrowseName, using the lowerCamelCase
spelling for instances, and `dir()` lists them — which is what makes a REPL
usable:

```python
plantObject.temperature()   # the child Variable, read
plantObject.serial()
dir(plantObject)            # ['add', 'counter', 'level', 'samples', 'serial', 'temperature']
```

A Method reached through its Object is bound to that Object and can be called
directly; the bare handle needs the Object passed explicitly:

```python
plantObject.add(2.0, 3.0)                # (StatusCode.GOOD, 5.0)
method(2.0, 3.0, object=plantObject)     # same call, unbound handle
```

`o6.NodeId(node)` converts any handle back to its NodeId. The full syntax —
including browse paths and the awaitable forms — is described in
[Node API](../node-api.md).

## Methods

A Method callback receives the Object the Method was invoked on, followed by the
input arguments in declaration order, and returns a tuple whose first element is
a status code:

```python
def divide(node, dividend, divisor):
    if divisor == 0:
        return (o6.StatusCode.BAD_INVALID_ARGUMENT,)
    return (o6.StatusCode.GOOD, dividend / divisor)
```

A Bad status may be returned alone. A non-Bad status must be followed by exactly
the number of outputs the Method declares. Callbacks may be `async def`; the
positional arguments and the result tuple are identical either way. Per-call
state belongs on `node` or in a closure — there is no callback context.

Invoking a Method from inside the server uses `server.call`, with the same
result contract as `client.call`:

```python
status, *outputs = server.call(plantObject, method, [10.0, 4.0])
status.check()
quotient = outputs[0]
```

Both return `(statusCode, *output_arguments)`, including bad method statuses,
invalid method selection, and argument-validation failures. Outputs reflect the
actual method result; a result with no outputs is `(statusCode,)`. Node handles
are accepted for object and method IDs and normalized inside input arguments.
Synchronous and asynchronous callbacks use the same result contract. Await the
call from asynchronous code, including a separate caller loop.

Service or local submission failures raise `o6.StatusCodeError`, whose `.code`
retains the original status. Python conversion errors remain Python exceptions,
such as `TypeError`. Local calls use administrative privileges; remote calls
check the session's permissions.

**Migration:** `server.call` previously raised for bad method statuses. Inspect
the first tuple element, or call `status.check()` to retain exception handling:

```python
try:
    status, *outputs = server.call(plantObject, method, [10.0, 0.0])
    status.check()
except o6.StatusCodeError as error:
    print(error.symbol)      # BadInvalidArgument
```

Typed Method node calls such as `plantObject.divide(10.0, 4.0)` check the method
status and raise on failure, locally and remotely. Their successful result
still includes the leading status.

Replacing a Method's behaviour later is `server.implement`, described in
[Implementing behaviour](behaviour.md#implementing-behaviour).

## References and deletion

```python
from o6.ns import ns0

server.addReference(source=plantObject, reftype=ns0.reftypes.HasComponent, target=temperature)
server.deleteReference(source=plantObject, reftype=ns0.reftypes.HasComponent, target=temperature)
server.deleteNode(scratch)
```

Both reference APIs use `(source, reftype, target)` and return an individual `StatusCode`.
Call `.check()` on a synchronous result to raise for a rejected mutation;
inside an async task, await the operation first and then check its status.
```python
status = await server.addReference(source=plantObject, reftype="i=47", target=temperature)
status.check()
status = await server.deleteReference(source=plantObject, reftype="i=47", target=temperature)
status.check()
```

Client service failures raise `StatusCodeError`. Invalid Python arguments remain
`TypeError` or `ValueError`.

`forward=False` creates or deletes an inverse edge. Deletion uses
`deleteBidirectional=True` by default; `False` removes only the requested
source-side edge. Both operations accept NodeId-like or `ExpandedNodeId` targets
and preserve remote namespace URI and server index metadata. Creating an exact
existing local edge returns `BAD_DUPLICATE_REFERENCE_NOT_ALLOWED`. Deleting an absent
edge returns `UNCERTAIN_REFERENCE_NOT_DELETED`. The underlying server stores
remote edges but omits them from browse results; repeated creation of an exact
remote edge returns `GOOD` without adding another edge.

Local creation accepts the same metadata keywords as the client, but a nonempty
`targetServerUri` returns `BAD_NOT_IMPLEMENTED`, and an explicit
`targetNodeClass` other than `UNSPECIFIED` returns `BAD_NOT_SUPPORTED` without
creating an edge. The client sends these fields to the remote server for validation.

The server positional order is a breaking change. Migrate
`server.addReference(source, target, referenceType)` to
`server.addReference(source=source, reftype=referenceType, target=target)`;
use the same keywords for deletion and rename `bidirectional` to
`deleteBidirectional`. The canonical APIs do not guess argument order.
`addReferenceLegacy(source, target, referenceType, *, forward=True)` and
`deleteReferenceLegacy(source, target, referenceType, *, forward=True, bidirectional=True)`
retain the old server order, keyword names, and `None`/`StatusCodeError` behavior.
Both compatibility and canonical methods must be awaited inside async tasks,
including tasks on the server's own loop.

### Node deletion

Both client and server use `deleteNode(nodeId, deleteTargetReferences=True)`.
Pass a Node, NodeId-like value, or list of targets. A scalar target returns one
`StatusCode`; a list returns one status per target in input order, including
one-element lists. Every target is attempted even after a failure. An empty
list returns `[]` without a deletion request. Duplicate targets have separate
results: after a successful deletion, deleting the same NodeId again returns
`BAD_NODE_ID_UNKNOWN`.

```python
statuses = server.deleteNode([firstNode, "ns=1;s=Missing", lastNode])
# [GOOD, BAD_NODE_ID_UNKNOWN, GOOD]; both existing nodes have been deleted
for status in statuses:
    status.check()
```

Inside async tasks, await deletion before inspecting the result:

```python
status = await server.deleteNode(scratch, deleteTargetReferences=False)
status.check()
```

`deleteTargetReferences=True` removes incoming references from remaining nodes;
`False` leaves dangling references to deleted targets. Browsing omits dangling
edges, but they become visible if the NodeId is reused. The native stack can
also delete hierarchical children that have no other parent, with either flag.
Retained server handles and aliases become invalid on deletion; reusing a
NodeId creates a distinct live handle and does not revive the old object.

Malformed Python arguments raise `TypeError` or `ValueError` before any target
is deleted. Individual deletion failures are returned in their target's status;
client service failures raise `StatusCodeError`. Server deletion uses local
administrative privileges; client deletion remains subject to the remote
session's authorization.

**Migration:** rename the old server keyword `deleteReferences` to
`deleteTargetReferences`; the old keyword is no longer accepted. The flag can
also be passed as the second positional argument, matching the client.
Scalar server deletion returns a status instead of `None` and does not raise for
individual failures. Batch deletion on both backends now returns a list instead
of one aggregate status. Use `status.check()` on each result to retain exception
handling, and await deletion in async tasks, including tasks on the server's
own loop.

## Browsing and address-space queries

The server can walk its own address space. Both `server.browse` and
`client.browse` return a complete flat list of `ReferenceDescription` objects,
following continuation points internally.

```python
references = server.browse(plantObject, resultMask=ns0.datatypes.BrowseResultMask.ALL)
for reference in references:
    print(reference.browseName, reference.nodeClass, reference.nodeId)
```

As on the client, the default `resultMask` is empty and fills in only the target
NodeId — pass `BrowseResultMask.ALL` (or the specific bits you need) to get
BrowseNames and node classes. `direction=`, `reftype=`, `refsubtypes=`, and
`nodeClassMask=` narrow the traversal exactly as they do on the client.
Async tasks await the call for both Node and NodeId targets.

For explicit pagination, use `server.browsePage(..., maxReferences=...)` and
`server.browseNext(releaseContinuationPoint, continuationPoint)`. Old callers
that read `.references` from `browse` now use the list directly; old page-limit
callers move to `browsePage`. See [explicit pages and migration](operations.md#explicit-pages-and-migration)
for continuation and release examples.

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
plain list of BrowseNames, and `translateBrowsePaths(request)` takes a full
`TranslateBrowsePathsToNodeIdsRequest` when you need the service-level form.

Two more helpers round this out. `forEachChildNode(nodeId, callback)` invokes
`callback(childId, isInverse, referenceTypeId)` for **every** reference on a
node, including its parent edge and its `HasTypeDefinition` edge — it is a raw
reference iterator, not a children-only browse. And `findDataType(nodeId)`
returns the Python type registered for a DataType:

```python
server.findDataType(o6.NodeId(o6.Double))    # <class 'numpy.float64'>
```
