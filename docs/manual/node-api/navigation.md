# Navigation & Lookup

Use dot navigation when you know the model's structure, a browse path when
you need explicit names or namespaces, and a NodeId when you already know a
node's identity. All three give you nodes to
[read, write, or call](read-write-call.md).

Unless labeled async, the client fragments on this page belong inside the
connected `with o6.Client(...) as client:` block from
[Nodes as Objects](using-nodes.md#a-taste), with its example server running.
The same navigation syntax is available on the local `server`.

## Following children with dots

Each dot resolves one child, returning a Node subclass for its NodeClass:

```python
plant = client.objects.plant
counter = plant.counter
print(counter())
```

The original BrowseNames here are `Plant` and `Counter`; `plant` and
`counter` are their Python aliases. An exact original-name match takes
precedence; otherwise, lookup matches original names and aliases
case-insensitively. A missing or ambiguous child raises `AttributeError`.

Ordinary Python attributes take precedence over child lookup. Use a browse
path if such an attribute hides a child. The detailed conversion and
collision rules are in [BrowseName to Python Names](name-conversion.md).

## Looking up a NodeId

Index the client or server itself to get one node by identity:

```python
counter = client[o6.NodeId("ns=1;i=1001")]
print(counter())
```

The local server equivalent is `server[o6.NodeId("ns=1;i=1001")]`.
`counter._nodeid` gives the identifier held by either handle. The example's
`ns=1` refers to the server's application namespace; do not extrapolate this
to numeric indices copied from other servers. See
[Registry and Namespace Mapping](../sdk-fundamentals/namespace/namespace-mapping-in-o6.md#process-indices-and-server-indices)
for URI and shortname lookup.

A NodeId is independent of a browse path. For a client Method obtained this
way, supply its Object when calling it, as described in
[Which Object receives the call?](read-write-call.md#which-object-receives-the-call).

## Resolving browse paths with brackets

Index a node with a relative browse path to get a list of matches:

```python
counter, = client.objects["/1:Plant/1:Counter"]
print(counter())

plant = client.objects.plant
label, = plant["/1:Label"]
print(label())
```

The comma in `counter, = ...` unpacks a list expected to contain exactly one
result. If a path can match several nodes, keep the list and choose using
known identities or attributes; do not assume the first result is the
intended one. No match raises `KeyError`.

Paths start from the node being indexed, even with a leading `/`. Each `/`
step follows hierarchical references. `1:Counter` is the original
BrowseName with its namespace index, not the Python alias `counter`.
Omitting the namespace selects namespace zero, so `"Plant/Counter"` does not
resolve this example's namespace-1 nodes.

Within a BrowseName, escape the reserved characters `.`, `/`, `&`, `<`, `>`,
`:`, `#`, and `!` with a leading `&`. For example, `plant["/1:Set&.Point"]`
looks up a child whose original BrowseName is `Set.Point`. Spaces and Python
keywords need no conversion in a browse path.

Namespace qualification can distinguish children with the same name in
different namespaces. If the same qualified path still identifies multiple
targets, use a known NodeId for an unambiguous lookup. The API also accepts a
`ns0.datatypes.RelativePath`; see
[Browse paths](../client/browsing.md) for reference types and advanced path
construction.

The example paths resolve completely within one server and return node
handles. Paths that cross servers or resolve only partially can instead
return `ExpandedNodeId` or `BrowsePathTarget` entries; see the
[client browsing contracts](../client/browsing.md) before assuming every
possible target is callable.

## Discovering children

In a synchronous interactive session, `dir(node)` lists Python aliases for
children. With the example server, this fragment prints `True`:

```python
plant = client.objects.plant
print({"counter", "label", "hello"}.issubset(dir(plant)))
```

REPL or editor completion that consults `dir()` can show these names when
you press Tab after `plant.`. Support depends on the editor: static analysis
alone cannot discover a remote server's live model. Bundled type hints help
with known Node APIs and keyword arguments such as `attr=`.

`dir()` always returns synchronously. On the client's owning event loop it
uses cached children and Python attributes, without issuing a blocking
remote request. Use `await client.browse(plant)` for fresh discovery there;
see [Browsing](../client/browsing.md) for the returned reference descriptions.

## Navigation caches and model changes

A client caches child names after browsing a parent. Repeated dot lookups
can use that cache; a missing name gets one fresh browse before failing.
This caches navigation, not Variable values: `counter()` reads the current
Value. Some identity attributes can be served from the handle's metadata.

A cached hit can become stale when the server or another client changes the
model. Invalidate the affected parent's children before navigating again:

```python
client.invalidateNodeCache(plant)
counter = plant.counter
```

Use `client.invalidateNodeCache()` to invalidate all existing handles.
Invalidating navigation does not replace a retained handle: if a node was
deleted or replaced, resolve it again before using it.

Node and reference changes made through the client, BrowseName writes,
explicit `connect()` calls, and `updateRemoteNamespaces()` invalidate navigation caches.
Automatic channel recovery does not; see [Connection recovery](../client/lifecycle.md#connection-recovery).
A complete `client.browse(plant)` also invalidates that parent's cache,
including other handles for the same NodeId. Local server handles resolve
against the local address space; they do not use the client's remote cache.

## Async lookup

The following fragment belongs inside the `async with o6.Client(...) as
client:` block from [Async operations](read-write-call.md#async-operations):

```python
plant = await client.objects.plant
counter = await client[o6.NodeId("ns=1;i=1001")]
label, = await plant["/1:Label"]
await client.invalidateNodeCache(plant)
print(await counter())
```

Standard folder handles such as `client.objects` are immediate. Child
navigation, lookup by NodeId, and browse-path resolution must be awaited in
async tasks, on both clients and servers. Await cache invalidation too.
Resolve a pending child handle before indexing it: use the resolved `plant`
as above. Chained dot access supports a single `await`, but bracket indexing
requires an already resolved node.
