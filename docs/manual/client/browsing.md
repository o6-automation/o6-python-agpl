# Browsing & Node Lookup

Use browsing to discover nodes, resolve paths, and obtain typed handles.
The snippets assume a connected `client`.

## Browsing

`browse()` follows references from a node and returns a flat list of
`ReferenceDescription` objects. It issues `BrowseNext` as often as needed, so
the list is complete even when the server splits its response, including empty
intermediate pages. `server.browse()` accepts the same filters and returns the
same list shape. It accepts Node and NodeId targets. Await the call in async
tasks. Service and per-result failures raise `o6.StatusCodeError`. On failure
or cancellation, `browse()` tries to release the outstanding continuation
point; a lost connection can prevent release.

For explicit pagination, use `browsePage` and `browseNext`; see
[Paging and translating browse paths](#paging-and-translating-browse-paths).
For raw request and response access, use `serviceBrowse` and `serviceBrowseNext`
and check response-header and per-result statuses yourself.

```python
references = client.browse("i=85")
```

`resultMask` defaults to `BrowseResultMask.ALL`, so every
`ReferenceDescription` field is filled in. Fields left out of the mask keep
their zero values; `nodeId` is always returned:

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

`reftype` defaults to `HierarchicalReferences` with `refsubtypes=True`, which
returns the children. `INVERSE` walks to the parent. `nodeClassMask` defaults
to `UNSPECIFIED`, meaning every node class.

To resolve a path instead of listing children, index a node with a browse path.
This calls `TranslateBrowsePathsToNodeIds`:

```python
node, = client.objects["/1:Plant/1:IntegerVariable"]
```

### Browsing interactively

The client has a built-in interactive browser for exploring a server:

```python
selected = client.browseInteractive()          # starts at Objects
selected = client.browseInteractive("i=85")    # or anywhere else
```

It needs `curses`; without it, the call raises `ImportError`. On Windows,
install it with `pip install windows-curses`. Quitting with `n` or `p` returns
the selected NodeId or browse path as a string you can paste into code. Any
other exit returns `None`.

## The Node API from a client

Use the [Node API](../node-api/index.md) when you want typed handles instead of
reference descriptions. The standard folders `client.root`, `client.objects`,
`client.types`, and `client.views` are immediate navigation entry points.

```python
plant = client.objects.plant
node = client["ns=1;s=IntegerVariable"]
```

Lookup by NodeId returns the matching Node subclass, such as `VariableNode`.
An unknown NodeId raises `StatusCodeError` with code `BAD_NODE_ID_UNKNOWN`.

In async code, await child navigation and lookup by NodeId:

```python
plant = await client.objects.plant
node = await client["ns=1;s=IntegerVariable"]
```

[Navigation & Lookup](../node-api/navigation.md) explains browse paths, lookup
errors, interactive discovery with `dir()`, and navigation-cache invalidation.
[BrowseName to Python Names](../node-api/name-conversion.md) covers name
conversion and ambiguous children. These rules apply to both clients and
servers.

## Paging and translating browse paths

Client and server expose `browsePage(target, maxReferences=...)` and
`browseNext(releaseContinuationPoint, continuationPoint)`. `browsePage` returns
one `BrowseResult`. `browseNext` accepts a token or a list or tuple of tokens
and always returns a list of results. An empty token list returns `[]`. Tokens
belong to the issuing server or session. Release unused tokens when you abandon
a traversal:

```python
page = client.browsePage(parent, maxReferences=10)
try:
    for reference in page.references:
        print(reference.nodeId)
finally:
    if page.continuationPoint:
        client.browseNext(True, page.continuationPoint)
```

`browse` collects every page automatically. The paging methods raise on
service or per-page failures and try to release the token on failure or
cancellation.

`translateBrowsePathsToNodeIds` accepts a `BrowsePath` or a list and returns one
`BrowsePathResult` or a list in the same order. `[]` returns `[]`. Path
failures stay in each result's status; service failures raise.
`browseSimplifiedBrowsePaths(origin, ["1:Plant", "1:Temperature"])` resolves one
BrowseName chain through forward hierarchical references. It returns one
`BrowsePathResult`, which can hold an unresolved-path status. Both methods
behave the same on client and server.

`serviceTranslateBrowsePathsToNodeIds` gives raw request and response access on
client and server. The server also keeps `translateBrowsePaths(request)`.
`server.browseRecursive` is a local native traversal. Await all these calls in
async tasks.

## Discovering custom DataTypes

`getRemoteDataTypes()` returns the structure definitions of a server's custom
data types:

```python
for dt in client.getRemoteDataTypes():
    print(dt["typeName"], dt["typeId"], dt["structureType"], dt["membersSize"])
```

It walks the DataType hierarchy below `Structure` (`i=22`), follows every
browse page and reads `DataTypeDefinition` and `BrowseName` for each node. It
returns one dict per type with the keys `typeName`, `typeId`,
`binaryEncodingId`, `structureType` and `membersSize`.

- Only nodes with a `StructureDefinition` appear: structures, structures with
  optional fields and unions. Types without the optional DataTypeDefinition
  attribute are skipped.
- Numeric, string, GUID and opaque NodeIds are preserved.
- References with a remote server index or namespace URI are skipped, because
  they cannot be read as local NodeIds through this session.
- Failed browse or read services and attribute reads raise `StatusCodeError`.
- Pass a list of DataType NodeIds to query only those. An empty list returns
  `[]` without contacting the server.

`getRemoteDataTypes()` registers nothing. Values of these types in namespaces
without a package decode on demand, or after `loadRemoteDataTypes()`; see
[Unknown namespaces and structured values](../sdk-fundamentals/namespace/loading-and-using-nodesets.md#unknown-namespaces-and-structured-values).
See [Namespace mapping in o6](../sdk-fundamentals/namespace/namespace-mapping-in-o6.md)
for the namespace machinery.
