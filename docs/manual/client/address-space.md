# Working with the address space

## Reading attributes

`read()` is the workhorse. In its simplest form it reads the `Value` attribute
of one node and gives you a Python value:

```python
value = client.read("ns=1;s=IntegerVariable")
```

The target is anything a `NodeId` can be built from: a NodeId string, an
`o6.NodeId`, an `ExpandedNodeId`, a [Node](../node-api.md) object, or a generated
type class:

```python
client.read(o6.NodeId(2255))                       # NamespaceArray
client.read(client["ns=1;s=IntegerVariable"])      # a Node object
client.read(ns0.objtypes.BaseObjectType, attr="browseName")
```

Passing a list reads all of them in a **single** `Read` request, which is the
whole point — one round trip instead of *n*:

```python
values = client.read([
    "ns=1;s=IntegerVariable",
    "ns=1;s=DoubleVariable",
])
# [np.int32(42), np.float64(3.14159)]
```

Numeric values come back as NumPy scalars and arrays, which preserves the exact
OPC UA data type (`Int32` stays 32 bit) and makes array data cheap to work with.

### Choosing the attribute

`attr` selects which attribute to read. It accepts an `o6.AttributeId` member or
a name as a string, matched case-insensitively and ignoring separators:

```python
client.read("ns=1;s=IntegerVariable", attr=o6.AttributeId.NODE_CLASS)
client.read("ns=1;s=IntegerVariable", attr="browseName")   # same as BROWSE_NAME
client.read("ns=1;s=IntegerVariable", attr="access_level")
```

This is how you get at metadata: `BROWSE_NAME`, `DISPLAY_NAME`, `DESCRIPTION`,
`DATA_TYPE`, `VALUE_RANK`, `ARRAY_DIMENSIONS`, `ACCESS_LEVEL`, `HISTORIZING`,
`DATA_TYPE_DEFINITION`, and the rest of `o6.AttributeId`.

### Values, or the whole `DataValue`

By default `read()` unwraps the value and raises if the server reported a bad
status. With `valueOnly=False` you get the `DataValue` objects untouched, status
code and timestamps included, and nothing is raised:

```python
dv = client.read("ns=1;s=IntegerVariable", valueOnly=False)
print(dv.value, dv.status, dv.sourceTimestamp, dv.serverTimestamp)
```

This is the form to use when a bad status is expected and not exceptional, or
when you need timestamps.

!!! note
    The `timestampsToReturn` parameter is accepted but not yet applied to the
    request, so `read()` returns whatever the server sends by default — the
    source timestamp. When you need both timestamps explicitly, issue the
    request through [`serviceRead`](raw-services.md#the-raw-service-interface) with
    `timestampsToReturn` set on it.

### Index ranges

`range` reads a slice of an array variable instead of the whole thing. It takes
OPC UA's inclusive string syntax or Python slices, which are stop-exclusive as
usual:

```python
client.read("ns=1;s=ArrayVariable", range="1:3")            # elements 1,2,3
client.read("ns=1;s=ArrayVariable", range=slice(1, 4))      # identical
client.read("ns=1;s=ArrayVariable", range=(slice(1, 4),))   # identical
client.read("ns=1;s=Matrix", range="1:3,4:6")               # two dimensions
client.read("ns=1;s=Matrix", range=(slice(1, 4), slice(4, 7)))
```

Slices must have explicit non-negative bounds and no step — OPC UA's
`NumericRange` cannot express anything else, and violations raise `ValueError`
before a request is sent. With a list of targets you may pass a list of ranges,
one per target. Applying a range to a node that is not an array logs a warning
and yields `[]` rather than an error.

### What read raises

The failure behaviour is worth internalizing because it differs by form:

| Situation | Result |
| --- | --- |
| Single target, bad status, `valueOnly=True` | raises `o6.StatusCodeError` |
| List of targets, any bad status, `valueOnly=True` | raises `ValueError` naming the index |
| Any target, `valueOnly=False` | no exception; inspect `DataValue.status` |
| Service itself failed | raises `ValueError` with the `serviceResult` |
| Client not connected | raises `Exception("Client is not connected")` |

```python
client.read("ns=1;s=DoesNotExist")
# o6.StatusCodeError: BAD_NODE_ID_UNKNOWN
```

## Writing attributes

`write()` mirrors `read()` and comes in three shapes.

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

Or a mapping, which is the most readable form for a batch:

```python
statuses = client.write({
    "ns=1;s=IntegerVariable": 100,
    "ns=1;s=DoubleVariable": 2.7182,
})
```

All three are sent as one `Write` request. The single-node form returns one
`o6.StatusCode`; the list and mapping forms return a list of status codes in
input order. The `value` argument must be omitted for the mapping form, and must
be a list of matching length for the list form — anything else raises
`ValueError`.

`attr` works exactly as in `read()`, so writes are not restricted to values:

```python
client.write("ns=1;s=IntegerVariable", o6.LocalizedText("Counter"), attr="displayName")
```

`range` writes into a slice of an array, and is supported for the single-node
and list forms (not the mapping form, which has nowhere to put it):

```python
client.write("ns=1;s=ArrayVariable", [99, 98], range="1:2")
```

To supply a status code or timestamps along with the value, pass a `DataValue`
instead of a bare Python value. The server must permit it — writing timestamps
requires `AccessLevel.TIMESTAMP_WRITE`, writing a status requires
`STATUS_WRITE`, and without them the write comes back
`BAD_WRITE_NOT_SUPPORTED`:

```python
dv = o6.DataValue()
dv.value = o6.Int32(77)
client.write("ns=1;s=IntegerVariable", dv)
```

Unlike `read()`, a write **never raises for a bad per-node status** — the status
code is the return value. Check it explicitly, either directly or with
`StatusCode.check()`, which raises `StatusCodeError` for anything but `GOOD`:

```python
status = client.write("ns=1;s=IntegerVariable", "not an int")
print(status)                      # BAD_TYPE_MISMATCH
if o6.StatusCode.BAD in status:    # StatusCode is a full IntFlag
    ...
status.check()                     # raises o6.StatusCodeError
```

## Calling methods

`call()` invokes an OPC UA method. It needs the object that owns the method, the
method itself, and the input arguments in declaration order:

```python
status, greeting = client.call(
    "ns=1;s=TestMethods",
    "ns=1;s=MethodHelloString",
    ["World"],
)
# (StatusCode.GOOD, 'Hello World!')
```

The return value is always a tuple whose first element is the method's status
code, followed by the decoded output arguments — so a method with no outputs
returns a one-element tuple. `Node` objects inside `inputArgs` are converted to
their NodeIds automatically, at any nesting depth, so you can pass nodes where a
method expects a NodeId.

A failing *service* (as opposed to a failing method) raises; a method that
returns a bad status code does not. `BAD_INVALID_ARGUMENT` almost always means
the argument list does not match the method's `InputArguments` declaration in
count, type, or value rank.

The [Node API](../node-api.md) offers the same call in object syntax, which reads
better when you already hold the node:

```python
client.objects.testMethods.MethodHelloString("World")
```

## Browsing

`browse()` follows references from a node and returns a flat list of
`ReferenceDescription` objects. Continuation points are handled internally: the
call issues `BrowseNext` as often as needed, so the list is always complete even
when the server chunks its response.

```python
references = client.browse("i=85")
```

There is one thing to know before using the result, and it catches everyone
once: the default `resultMask` is **empty**, so the server only fills in the
target `nodeId` and leaves `browseName`, `displayName`, `nodeClass`,
`referenceTypeId`, `isForward`, and `typeDefinition` at their zero values. Ask
for the fields you need:

```python
from o6.ns import ns0

for ref in client.browse("i=85", resultMask=ns0.datatypes.BrowseResultMask.ALL):
    print(ref.browseName, ref.nodeClass, ref.nodeId, ref.typeDefinition)
```

The remaining parameters narrow the traversal:

```python
references = client.browse(
    "ns=1;s=Plant",
    direction=ns0.datatypes.BrowseDirection.FORWARD,   # FORWARD, INVERSE, BOTH
    reftype=ns0.reftypes.HasComponent,                 # reference type to follow
    refsubtypes=True,                                  # include its subtypes
    nodeClassMask=ns0.datatypes.NodeClass.VARIABLE,    # only Variables
    resultMask=ns0.datatypes.BrowseResultMask.ALL,
)
```

`reftype` defaults to `HierarchicalReferences` with `refsubtypes=True`, which is
the "show me the children" traversal. `INVERSE` walks to the parent.
`nodeClassMask` defaults to `UNSPECIFIED`, meaning every node class.

To resolve a path rather than enumerate children, use the browse-path syntax on
a node — that goes through `TranslateBrowsePathsToNodeIds`:

```python
node, = client.objects["/1:Plant/1:IntegerVariable"]
```

### Browsing interactively

For exploring an unfamiliar server there is a fully interactive browser built into the
client:

```python
selected = client.browseInteractive()          # starts at Objects
selected = client.browseInteractive("i=85")    # or anywhere else
```

It needs `curses` (on Windows: `pip install windows-curses`, otherwise
`ImportError`). Quitting with `n` or `p` returns the selected NodeId or browse
path as a string so you can paste it straight into code; any other exit returns
`None`.

## Namespaces and NodeIds

A NodeId string like `"ns=1;s=IntegerVariable"` is namespace-relative, and the
index `1` means something different on every server. `o6` resolves this for you,
which is why `connect()` spends two of its steps on namespaces.

On connect, the client reads the server's `ApplicationUri` and registers it in
the process-wide namespace table under the shortname `<clientname>_ns1`, scoped
to the endpoint URL. Then `updateRemoteNamespaces()` reads the server's
`NamespaceArray` and maps every remaining namespace URI onto a compiled
namespace module, scoped to the client name. Where several compiled versions of
the same URI exist, the client reads the server's `NamespaceMetadata` (its
`NamespaceVersion`) and picks the matching one, falling back to the newest
available and logging a warning if the server is newer than anything you have
compiled.

The visible effect is that `ns=1` in your code means "namespace 1 *of the server
this client is connected to*", and NodeIds returned to you print with the
resolved shortname:

```python
print(client.read("ns=1;s=IntegerVariable", attr="browseName"))
# client1_ns1:IntegerVariable

info = o6.ns.client1_ns1
print(info.uri, info.scope, info.index)
# urn:open62541.unconfigured.application  opc.tcp://localhost:4840  129
```

If a connected server adds namespaces at runtime, call
`client.updateRemoteNamespaces()` again. It builds the new mapping — Python
namespace table, SecureChannel decoder mapping, and custom data type chain — and
swaps it in as one snapshot; a failed refresh leaves the previous, working
snapshot in place, and an unchanged one is not rebuilt.

To discover the structure definitions of a server's custom data types, use
`getRemoteDataTypes()`:

```python
for dt in client.getRemoteDataTypes():
    print(dt["typeName"], dt["typeId"], dt["structureType"], dt["membersSize"])
```

It walks the DataType hierarchy below `Structure` (`i=22`) and reads
`DataTypeDefinition` and `BrowseName` for every node it finds, returning one
dict per type with the keys `typeName`, `typeId`, `binaryEncodingId`,
`structureType`, and `membersSize`. Only nodes that actually carry a
`StructureDefinition` — structures, structures with optional fields, and unions
— appear. Pass a list of DataType NodeIds to query just those instead of walking
the tree; an empty list returns `[]` without contacting the server.

The namespace machinery itself is described in
[Namespace mapping in o6](../sdk-fundamentals/namespace/namespace-mapping-in-o6.md),
and loading nodesets so that custom types decode into real Python classes is
covered in
[Loading and using nodesets](../sdk-fundamentals/namespace/loading-and-using-nodesets.md).

## The Node API from a client

Everything above addresses nodes by NodeId. The [Node API](../node-api.md) lets you
address them the way the server models them — as an object graph. A connected
client exposes the four standard entry points as live nodes:

```python
client.root       # i=84
client.objects    # i=85
client.types      # i=86
client.views      # i=87
```

Attribute access resolves a child by BrowseName through a `Browse` request and
caches it; calling a node reads or writes it; indexing resolves a browse path:

```python
client.objects.plant.integerVariable()            # read the Value
client.objects.plant.integerVariable(42)          # write the Value
client.objects.plant.integerVariable(attr="browseName")
client.objects.testMethods.MethodHelloString("World")
```

`dir()` on a node browses it and returns its children, so **tab completion walks
the live address space**: type `client.objects.` in a REPL and the server's
actual nodes are offered, one `Browse` request at a time. That is the fastest way
to explore an unfamiliar server, and it is why the dotted form is worth using
even when you already know the NodeId.

!!! warning "BrowseNames are not Python identifiers — sometimes you need `[]`"
    A BrowseName is an arbitrary OPC UA string. A Python attribute name is an
    identifier. Dot syntax can only reach the children whose BrowseName happens
    to be a valid identifier, and `dir()` deliberately lists only those — so a
    child missing from tab completion is not missing from the server.

    Within that subset, lookup matches the BrowseName exactly first and then
    case-insensitively, so `ServerStatus` and `serverStatus` both resolve.
    Completion offers the spelling the generated declarations use: instances
    (Objects, Variables, Methods, Views) with a lowercased first letter,
    type nodes (ObjectType, VariableType, ReferenceType, DataType) in their
    original PascalCase.

    Everything else goes through the browse-path form, `node["/<ns>:<BrowseName>"]`:

    ```python
    plant = client.objects.plant

    plant["/1:Device Name"]      # spaces
    plant["/1:2Fast"]            # leading digit
    plant["/1:Motor-Current"]    # dashes and other punctuation
    plant["/1:class"]            # a Python keyword
    plant["/1:Set&.Point"]       # '.' escaped with '&'
    ```

    `.`, `/`, `&`, `<`, `>`, `:`, `#`, and `!` are reserved in a browse path and
    are escaped with a leading `&`.

    The other case that needs `[]` is ambiguity. When two references from the
    same node carry the same BrowseName, dot access refuses to guess and raises
    `AttributeError` listing the candidates, while the browse path returns all
    matches — indexing always returns a **list**, even for a single hit:

    ```python
    plant.shared                 # AttributeError: ... is ambiguous; 2 matching references
    plant["/1:Shared"]           # [VariableNode(...Dup1), VariableNode(...Dup2)]
    node, = plant["/1:Temperature"]
    ```

Indexing the *client* itself resolves a NodeId into a typed node without knowing
its node class up front. It reads `NodeClass` and `BrowseName` and returns the
matching subclass — `VariableNode`, `ObjectNode`, `MethodNode`, and so on:

```python
node = client["ns=1;s=IntegerVariable"]
print(repr(node))     # client1_ns1:IntegerVariable: VariableNode(ns=1;s=IntegerVariable)
```

An unknown NodeId raises `KeyError`, and so does a browse path that resolves to
nothing; a missing child raises `AttributeError`. In async code every form is
awaited:

```python
node = await client["ns=1;s=IntegerVariable"]
value = await client.objects.plant.integerVariable()
```

The [Node API usage guide](../node-api.md#usage) and the
[Node API syntax tutorial](../../tutorials/client/140_node-api-syntax.md) go through
this in detail.

## Changing the server's address space

A client can modify a remote address space, provided the server allows it. There
is one method per node class, all keyword-only, all returning the NodeId the
server assigned:

```python
from o6.ns import ns0

attrs = ns0.datatypes.VariableAttributes()
attrs.displayName = o6.LocalizedText("FromClient")
attrs.dataType = o6.NodeId(ns0.datatypes.Int32)
attrs.valueRank = int(o6.ValueRank.SCALAR)
attrs.accessLevel = int(o6.AccessLevel.READ | o6.AccessLevel.WRITE)
attrs.value = o6.Int32(7)

nodeId = client.addVariableNode(
    parent="ns=1;s=Plant",
    browseName=o6.QualifiedName(1, "FromClient"),
    attributes=attrs,
    requestedNodeId="ns=1;s=FromClient",     # optional; omit to let the server pick
)
```

The family is `addVariableNode`, `addVariableTypeNode`, `addObjectNode`,
`addObjectTypeNode`, `addViewNode`, `addReferenceTypeNode`, `addDataTypeNode`,
and `addMethodNode`. Each takes `parent`, `browseName`, `attributes` (the
matching `*Attributes` structure), an optional `requestedNodeId`, and a
`parentReference` that defaults sensibly per node class — `HasComponent` for
Variables, Objects, Views, and Methods, `HasSubtype` for the type node classes.
`addVariableNode` and `addObjectNode` additionally take a `typeDefinition`,
defaulting to `BaseDataVariableType` and `BaseObjectType`.

References and nodes can be removed and rewired:

```python
client.addReference("i=85", ns0.reftypes.Organizes, nodeId)
client.deleteReference("i=85", ns0.reftypes.Organizes, nodeId)
client.deleteNode(nodeId)                      # or a list of NodeIds
```

`addReference` also takes `forward`, `targetNodeClass`, and `targetServerUri`
for references into another server's address space; `deleteReference` takes
`forward` and `deleteBidirectional`; `deleteNode` takes
`deleteTargetReferences`. Each returns a `StatusCode` — `deleteNode` returns the
first non-Good one from the batch — and a failed *service* raises `ValueError`.

Note that a client adding a Method node can only create the node, not its
behaviour: the implementation lives on the server. See [Server](../server/index.md) for
that side.
