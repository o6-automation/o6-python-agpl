# PubSub runtime hooks

Canonical path: `o6.pubsub.Offset`
Canonical path: `o6.pubsub.OffsetTable`
Canonical path: `o6.pubsub.OffsetType`
Canonical path: `o6.pubsub.StateMachine`
Canonical path: `o6.pubsub.offsetTable`
Canonical path: `o6.pubsub.publish`
Canonical path: `o6.pubsub.setStateMachine`

Configure and control PubSub through the standard namespace-zero information
model. The `o6.pubsub` module supplies only runtime hooks that are not
represented there: custom component state machines, fixed-layout message
offsets, and immediate WriterGroup publishing.

Commercial builds require the `pubsub` Credential feature in addition to
`server`. The module remains importable for discovery, but every operation
raises `PermissionError` when PubSub is not enabled. Servers constructed without
that feature have no native PubSub manager, information-model methods, or PubSub
transport connection managers. The AGPL build has no Credential checks.

## Immediate publishing

`publish(writerGroup)` publishes one message immediately through a configured,
enabled WriterGroup:

```python
o6.pubsub.publish(connection.writerGroup)
```

This is useful for event-driven publishing and deterministic external
scheduling. It does not enable components or replace their periodic publishing
configuration. The argument must be a live WriterGroup belonging to the
server; native configuration and transport failures raise `StatusCodeError`.

UDP/UADP and MQTT are configured with the standard namespace-zero PubSub
datatypes and methods. MQTT/UADP supports publishing and subscribing;
MQTT/JSON supports publishing, while JSON subscriber matching remains an
open62541 limitation. Ethernet/UADP uses `NetworkAddressUrlDataType` with an
interface name and `opc.eth://` address and is available on Linux, where raw
packet operation requires the usual operating-system privileges.

## Custom state machine

`setStateMachine(component, callback)` installs a synchronous state machine on
one concrete `PubSubConnection`, `WriterGroup`, `DataSetWriter`, `ReaderGroup`,
or `DataSetReader`. A natural place to install it is the implementation class:

```python
class WriterGroupImpl(o6.ns.ns0.objtypes.WriterGroupType):
    def __init__(self):
        o6.pubsub.setStateMachine(self, self.changeState)

    def changeState(self, current, target):
        # Configure or stop the external real-time backend here.
        return o6.StatusCode.GOOD, target


server.implement(o6.ns.ns0.objtypes.WriterGroupType, WriterGroupImpl)
```

The callback receives the current and requested `PubSubState` and returns
`(StatusCode, resultingState)`. A bad status, exception, recursive transition,
or malformed result moves the component to `ERROR`. Passing `None` restores
the native open62541 state machine. An existing component must be disabled
before its state machine is changed; construction-time installation happens
before the component is first enabled.

The callback is stored on the concrete node itself. It follows the node's
lifetime and needs no external registry.

## Offset table

`offsetTable(component)` returns an immutable `OffsetTable` for a configured
`WriterGroup` or `DataSetReader`:

```python
table = o6.pubsub.offsetTable(writerGroup)
packet = bytearray(table.message)
for entry in table.offsets:
    print(entry.type, entry.offset, entry.component)
```

`OffsetTable.message` is an owned Python `bytes` snapshot. Each `Offset`
contains its `OffsetType`, byte position, and the NodeId of the component whose
value occupies that position. WriterGroup offsets describe a complete network
message; DataSetReader offsets start at byte zero of its DataSetMessage.

The configuration must use a fixed binary layout. Unsupported or incomplete
configurations raise `StatusCodeError`.

## Public API

- `setStateMachine(component, callback)`
- `offsetTable(component)`
- `publish(writerGroup)`
- `StateMachine`
- `OffsetType`
- `Offset`
- `OffsetTable`
