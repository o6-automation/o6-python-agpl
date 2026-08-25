# Building the address space

## Building the address space imperatively

Every `addX` helper takes a display/browse name and a parent, and returns a
node handle from [`o6.node`](../node-api.md). The handle is a live view of the
node: calling it reads or writes, attribute access browses to children.

```python
plantObject = server.addObject("Plant", server.objectsNode, nodeId="ns=1;s=Plant")
temperature = server.addVariable("Temperature", plantObject, 22.5, nodeId="ns=1;s=Temp")
```

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
  is still derived from the value, so arrays keep working.
- `writable=False` gives the node `CurrentRead` only; the default is
  read *and* write.
- `historizing=True` sets the `Historizing` attribute and adds the history
  access levels — see [Historical data](operations.md#historical-data) for what else that
  needs.
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

Both take a single target or a list of targets, and both accept the attribute as
the **second positional** argument — note the difference from the client, where
`attr` is keyword-only:

```python
server.read("ns=1;s=Temp", "browseName")
server.read("ns=1;s=Temp", attr=o6.AttributeId.DISPLAY_NAME)
server.write("ns=1;s=Temp", o6.LocalizedText("Kettle temperature"), "displayName")
```

Attribute names are matched case-insensitively and ignore separators, so
`"browseName"`, `"BrowseName"`, and `"browse_name"` are the same attribute.

A list target reads or writes each node in turn and, for `read`, returns a list
of values. Note that `write` with a list target writes the *same* value to every
node — it does not zip a list of values:

```python
values = server.read(["ns=1;s=Temp", "ns=1;s=Counter"])   # [np.float64(...), np.int32(...)]
server.write(["ns=1;s=Temp", "ns=1;s=Level"], 30.0)       # both set to 30.0
```

`range=` reads or writes a slice of an array value, using OPC UA's inclusive
string syntax or stop-exclusive Python slices, and is only valid for the `Value`
attribute (anything else raises `ValueError`):

```python
server.read("ns=1;s=Samples", range="1:3")           # elements 1,2,3
server.read("ns=1;s=Samples", range=slice(1, 4))     # identical
server.write("ns=1;s=Samples", [99, 98], range="1:2")
```

Passing an `o6.DataValue` to `write` stores the value together with its status
code and timestamps instead of wrapping a bare value:

```python
import datetime

dv = o6.DataValue()
dv.value = o6.Double(42.0)
dv.sourceTimestamp = o6.DateTime(datetime.datetime.now(datetime.timezone.utc))
server.write("ns=1;s=Temp", dv)
```

`server.read` raises `o6.StatusCodeError` whenever the resolved `DataValue`
status is anything other than `Good` — including merely *uncertain* statuses.
If you deliberately store a non-Good status, expect the paired read to raise:

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

Invoking a Method from inside the server uses `server.call`, which mirrors
`client.call` in shape but not in error behaviour:

```python
status, quotient = server.call(plantObject, method, [10.0, 4.0])
```

Where `client.call` hands you a bad method status inside the returned tuple,
`server.call` **raises** `o6.StatusCodeError`. Wrap it when a bad status is a
normal outcome:

```python
try:
    server.call(plantObject, method, [10.0, 0.0])
except o6.StatusCodeError as error:
    print(error.symbol)      # BadInvalidArgument
```

Replacing a Method's behaviour later is `server.implement`, described in
[Implementing behaviour](behaviour.md#implementing-behaviour).

## References and deletion

```python
from o6.ns import ns0

server.addReference(plantObject, temperature, ns0.reftypes.HasComponent)
server.deleteReference(plantObject, temperature, ns0.reftypes.HasComponent)
server.deleteNode(scratch)
```

The argument order is *(source, target, referenceType)* — different from the
client's `addReference(source, reftype, target)`, so it is worth a second look
when porting code between the two.

`addReference` takes `forward=False` for an inverse edge and accepts an
`o6.ExpandedNodeId` target, which is how a reference into another server's
address space is expressed. `deleteReference` additionally takes `forward=` and
`bidirectional=` (default `True`). `deleteNode` takes
`deleteReferences=True` by default, which also removes references pointing at
the node.

All three raise `o6.StatusCodeError` on failure rather than returning a status
code.

## Browsing and address-space queries

The server can walk its own address space. The most important difference from
the client is the return type: `server.browse` returns a **`BrowseResult`**, so
the references are one attribute deeper.

```python
result = server.browse(plantObject, resultMask=ns0.datatypes.BrowseResultMask.ALL)
for reference in result.references:
    print(reference.browseName, reference.nodeClass, reference.nodeId)
```

As on the client, the default `resultMask` is empty and fills in only the target
NodeId — pass `BrowseResultMask.ALL` (or the specific bits you need) to get
BrowseNames and node classes. `direction=`, `reftype=`, `refsubtypes=`, and
`nodeClassMask=` narrow the traversal exactly as they do on the client, and
`maxReferences=` caps the batch, with `browseNext(releaseContinuationPoint,
continuationPoint)` continuing it.

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
