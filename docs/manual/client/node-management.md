# Changing the Address Space

Create or remove remote nodes and references when the server permits it.
These operations use the connected client session's permissions.

## Changing the server's address space

A client can modify a remote address space if the server allows it. There is
one method per node class. All are keyword-only and return the NodeId the
server assigned:

```python
from o6.ns import ns0

attrs = ns0.datatypes.VariableAttributes()
attrs.displayName = o6.LocalizedText("FromClient")
attrs.dataType = o6.NodeId(ns0.datatypes.Int32)
attrs.valueRank = int(o6.ValueRank.SCALAR)
attrs.accessLevel = int(
    ns0.datatypes.AccessLevelType.CURRENT_READ
    | ns0.datatypes.AccessLevelType.CURRENT_WRITE
)
attrs.value = o6.Int32(7)

nodeId = client.addVariableNode(
    parent="ns=1;s=Plant",
    browseName=o6.QualifiedName(1, "FromClient"),
    attributes=attrs,
    requestedNodeId="ns=1;s=FromClient",     # optional; omit to let the server pick
)
```

The methods are `addVariableNode`, `addVariableTypeNode`, `addObjectNode`,
`addObjectTypeNode`, `addViewNode`, `addReferenceTypeNode`, `addDataTypeNode`
and `addMethodNode`. Each takes `parent`, `browseName`, `attributes` (the
matching `*Attributes` structure), an optional `requestedNodeId` and a
`parentReference`. Without `requestedNodeId` the server picks the NodeId; an o6
server assigns a numeric NodeId in its application namespace, index 1. `parentReference` defaults to `HasComponent` for Variables,
Objects, Views and Methods, and to `HasSubtype` for the type node classes.
`addVariableNode` and `addObjectNode` also take a `typeDefinition`, defaulting
to `BaseDataVariableType` and `BaseObjectType`.

Add and remove references, and delete nodes:

```python
client.addReference("i=85", ns0.reftypes.Organizes, nodeId)
client.deleteReference("i=85", ns0.reftypes.Organizes, nodeId)
client.deleteNode(nodeId)                      # or a list of NodeIds
```

`addReference` and `deleteReference` return a `StatusCode`; await them in
async tasks. Rejected changes return non-Good statuses. Service failures raise
`StatusCodeError`. Use `forward=False` for inverse edges and
`deleteBidirectional=False` to remove only the requested edge. Both accept
expanded targets and keep their remote metadata. `addReference` also accepts
`targetNodeClass` and `targetServerUri` for validation by the remote server.
The server takes the same arguments; see
[References and deletion](../server/address-space.md#references-and-deletion).

`deleteNode(nodeId, deleteTargetReferences=True)` accepts one Node or
NodeId-like target, or a list. A single target returns one `StatusCode`. A list
returns one status per target in input order, also for a one-element list.
Every target is attempted despite individual failures. An empty list returns
`[]` without a request. Call `status.check()` on each result to raise for
individual failures. Service failures raise `StatusCodeError`. Malformed Python
arguments raise `TypeError` or `ValueError` before deletion starts. Await the
call in async tasks.

```python
targets = [firstNode, "ns=1;s=Missing", lastNode]
statuses = client.deleteNode(targets)
for target, status in zip(targets, statuses):
    print(target, status)
```

`deleteTargetReferences=True` removes incoming references from remaining nodes.
`False` leaves dangling references, which browse omits until the target NodeId
is reused. With either flag, the native stack can also delete hierarchical
children that have no other parent. Client operations use the remote session's
permissions. See [Node deletion](../server/address-space.md#node-deletion)
for the local administrative API and retained-handle behavior.

A client can create a Method node, but not its behavior; the implementation
lives on the server. See [Server](../server/index.md).

## Creating nodes with friendly inputs

`addObject` and `addVariable` match the server conveniences and return typed
nodes. In async tasks, await creation and later node operations.

```python
parent = client.addObject("Plant", client.objects)
temperature = client.addVariable("Temperature", parent, 22.5)
print(temperature())
```

Use `nodeId`, `typeDefinition` and `ns` to control identity and naming.
Variables also accept `dataType`, `writable`, `accessLevel` and
`userAccessLevel`. Numeric and array type
inference matches the server, including typed empty arrays. Unlike the server,
the client rejects a `DataValue` as the initial value with `TypeError`, because
AddNodes carries no status or timestamps; write the DataValue after creation.
With `dataType=o6.DataValue`, the DataValue is the value itself.
Both methods
default `parentReference` to `Organizes` and accept an explicit reference type.
The attribute-based `addObjectNode` and `addVariableNode` still return NodeIds
and default to `HasComponent`. Local history registration and Python behavior
installation are server-only.

If a call is cancelled after the server creates the node, the client tries to
remove the node before propagating the cancellation. Cleanup needs a working
connection. A failed cleanup is attached as an exception note.
