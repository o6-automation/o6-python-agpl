# Building the Address Space

Create Objects, Variables, Methods, and references with the server helpers.
The snippets assume a `server` constructed as described in
[Lifecycle & Configuration](lifecycle.md).

## Building the address space imperatively

Every `addX` helper takes a display/browse name and a parent. It returns a node
handle from [`o6.node`](../node-api/index.md), directly or through an awaitable.
The handle is a live view of the node: calling it reads or writes, and
attribute access browses to children.

```python
plantObject = server.addObject("Plant", server.objectsNode, nodeId="ns=1;s=Plant")
temperature = server.addVariable("Temperature", plantObject, 22.5, nodeId="ns=1;s=Temp")
print(temperature())  # 22.5
temperature(23.0)
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

The returned handle belongs to the server and is the canonical node object.
Variable initialization and Method callback installation complete before the
awaitable resolves. Creation errors reach the caller through the awaitable.
Cancelling it does not guarantee that creation is prevented, and it does not
roll back a completed native creation. Inspect the address space before
retrying with the same identifier.

For remote creation through a client, see
[Changing the Address Space](../client/node-management.md). History registration
and Python callback installation are server-only operations.

`nodeId=` is optional everywhere. Omit it and the server assigns a numeric
NodeId such as `ns=1;i=50021` in its application namespace, index 1; namespace 0
is reserved for the OPC Foundation. The number is not stable across runs or
creation orders. Pass `nodeId=` to fix the identifier that clients, historical
data and stored configuration depend on. `ns=` (default `1`) selects the
namespace index of the BrowseName, not of the NodeId. A client's AddNodes
request without a requested NodeId gets a NodeId in the same namespace.

### Variables

`addVariable` infers the OPC UA DataType and ValueRank from the initial Python
value. A `float` becomes a scalar `Double`, a list becomes a one-dimensional
array, and a NumPy array keeps its dimensionality:

```python
server.addVariable("Temperature", plantObject, 22.5)              # Double, scalar
server.addVariable("Samples", plantObject, [1, 2, 3, 4, 5])       # Int32, 1-D array
server.addVariable("Serial", plantObject, "SN-1", writable=False) # String, read-only
server.addVariable("Counter", plantObject, o6.Int32(0), dataType=o6.Int32)
server.addVariable("Level", plantObject, 0.0, historizing=True)
```

- `dataType=` sets the type instead of inferring it. The ValueRank is still
  derived from the value, so arrays keep working. Empty NumPy arrays use their
  dtype when `dataType` is omitted. Empty Python sequences require an explicit
  `dataType`, for example `server.addVariable("Samples", plantObject,
  [], dataType=o6.Int32)`. Empty arrays keep their declared `ValueRank`, but
  their values read back as flat zero-length arrays because
  [OPC UA Binary omits empty-array dimensions](https://reference.opcfoundation.org/specs/OPC-10000-6/5.2.2.16).
- A `DataValue` as the initial value sets the DataType and ValueRank from its
  `value` and keeps its status and timestamps, as
  [`server.write`](local-nodes.md#reading-and-writing-server-side) does:
  `server.addVariable("Pressure", plantObject,
  o6.DataValue(value=0.0, status=o6.StatusCode.BAD_WAITING_FOR_INITIAL_DATA))`.
  With `dataType=o6.DataValue`, the DataValue is the value of a Variable of
  DataType DataValue.
- `writable=False` gives the node `CurrentRead` only; the default is
  read and write. Neither lets clients write a status or timestamps with the
  value; such writes return `BAD_WRITE_NOT_SUPPORTED`. `accessLevel=` sets the
  AccessLevel explicitly and replaces `writable`, for example
  `accessLevel=AccessLevelType.CURRENT_READ | AccessLevelType.CURRENT_WRITE |
  AccessLevelType.STATUS_WRITE | AccessLevelType.TIMESTAMP_WRITE` (from
  `ns0.datatypes`) for clients that always send a SourceTimestamp.
  `historizing` still adds the history bits. `userAccessLevel=` defaults to
  the AccessLevel; the server derives the UserAccessLevel it reports from the
  AccessLevel and the session's permissions.
- `historizing=True` registers history immediately on a running server, which
  requires a configured history database. Before startup, registration waits
  until `start()`. See [Historical data](history.md#registering-and-stopping-history).
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

| Helper | Default parent | Extra options |
| --- | --- | --- |
| `addObjectType` | `BaseObjectType` | |
| `addVariableType` | `BaseVariableType` | |
| `addReferenceType` | `NonHierarchicalReferences` | `symmetric=`, `abstract=` |
| `addView` | `Views` folder | `containsNoLoops=` (default `True`), `eventNotifier=` |

`addObject` and `addVariable` accept `parentReference` and default to
`Organizes`. Views use `Organizes`, type nodes use `HasSubtype`, and Methods use
`HasComponent`. Use [`addReference`](#references-and-deletion) to attach
additional references.

`addMethod` pairs a node with a Python callback:

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

!!! warning
    Set `valueRank=o6.ValueRank.SCALAR` on each scalar `Argument`. The default
    ValueRank is `0`, which means array. A client that passes a scalar to an
    array argument gets `BadInvalidArgument` before your callback runs. This is
    the most common cause of a Method that "does not work".

!!! warning
    Integer inputs arrive as fixed-width NumPy scalars of the declared
    DataType, for example `numpy.int32` for an `Int32` argument, not as Python
    `int`. Their arithmetic wraps around at that width; NumPy only emits a
    `RuntimeWarning`. `2**30 * 4` on two `Int32` inputs is `0`. Convert with
    `int(a)` before a range check:

    ```python
    def multiply(node, a, b):
        product = int(a) * int(b)
        if not -(2**31) <= product < 2**31:
            return (o6.StatusCode.BAD_OUT_OF_RANGE,)
        return (o6.StatusCode.GOOD, o6.Int32(product))
    ```

Method callbacks are covered in [Server callbacks](callbacks.md#methods).

## References and deletion

```python
from o6.ns import ns0

server.addReference(source=plantObject, reftype=ns0.reftypes.HasComponent, target=temperature)
server.deleteReference(source=plantObject, reftype=ns0.reftypes.HasComponent, target=temperature)
server.deleteNode(scratch)
```

Both reference APIs take `(source, reftype, target)` and return a single
`StatusCode`. Call `.check()` on a synchronous result to raise for a rejected
change; see the shared
[error-handling contract](../sdk-fundamentals/builtin/statuscode.md#errors-and-status-codes).
In an async task, await the operation first, then check its status:

```python
status = await server.addReference(source=plantObject, reftype="i=47", target=temperature)
status.check()
status = await server.deleteReference(source=plantObject, reftype="i=47", target=temperature)
status.check()
```

Invalid Python arguments raise `TypeError` or `ValueError`.

- `forward=False` creates or deletes an inverse reference.
- Deletion uses `deleteBidirectional=True` by default; `False` removes only the
  requested source-side reference.
- Both operations accept NodeId-like or `ExpandedNodeId` targets and keep remote
  namespace URI and server index metadata.
- Creating an exact existing local reference returns
  `BAD_DUPLICATE_REFERENCE_NOT_ALLOWED`.
- Deleting an absent reference returns `UNCERTAIN_REFERENCE_NOT_DELETED`.
- The server stores remote references but omits them from browse results.
  Creating an exact remote reference again returns `GOOD` without adding
  another one.

Local creation accepts the same metadata keywords as the client. A nonempty
`targetServerUri` returns `BAD_NOT_IMPLEMENTED`, and a `targetNodeClass` other
than `UNSPECIFIED` returns `BAD_NOT_SUPPORTED`; neither creates a reference. The
client sends these fields to the remote server for validation.

### Node deletion

Use `server.deleteNode(nodeId, deleteTargetReferences=True)` to remove nodes.
Pass a Node, a NodeId-like value or a list of targets. A scalar target returns
one `StatusCode`. A list returns one status per target in input order, also for
one-element lists. Every target is attempted, even after a failure. An empty
list returns `[]` without a deletion request. Duplicate targets get separate
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

`deleteTargetReferences=True` removes incoming references from the remaining
nodes. `False` leaves dangling references to deleted targets. Browsing omits
dangling references, but they become visible again if the NodeId is reused.
With either flag, the native stack can also delete hierarchical children that
have no other parent. Retained server handles and aliases become invalid on
deletion. Reusing a NodeId creates a new live handle and does not revive the
old object.

Malformed Python arguments raise `TypeError` or `ValueError` before any target
is deleted. Individual deletion failures are returned in their target's status.
Server deletion has local administrative privileges. For deletion through a
remote session, see [client node management](../client/node-management.md).
