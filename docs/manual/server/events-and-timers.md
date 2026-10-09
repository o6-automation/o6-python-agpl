# Events, monitored items & timers

## Events

Emit immediately with `server.createEvent(...)` (also available as
`server.emitEvent(...)`), or construct a reusable Python draft with `o6.Event`:

```python
event = o6.Event(
    server,
    eventType=ns0.objtypes.BaseEventType,
    source=server.serverNode,
    message="Production started",
    severity=200,
)
event["/BatchId"] = "B-1042"
eventId = event.trigger()
```

Field keys are event-filter path strings such as `/BatchId`, or
`QualifiedName` values when a default namespace is needed. Explicit fields use
open62541's fast event-field map. An `Event` is a mutable mapping, so
`dict(event)`, `len(event)`, `del event[key]`, and iteration all work, and its
`eventType`, `source`, `message`, `severity`, and `fields` attributes can be
reassigned between triggers.

An existing object node can additionally supply the payload. Fields absent
from the explicit map are then resolved from that instance:

```python
event.eventInstance = machineEventInstance
event.trigger()
```

Resolution order is explicit `event.fields`, then `eventInstance`, then the
standard `BaseEventType` defaults. `trigger()` returns the generated 16-byte
`EventId`.

This follows C's field precedence even for `EventType` and `SourceNode`: a
stored property, including a null NodeId on a newly created instance, wins over
the corresponding emission argument. Populate these properties when preparing
the instance, or override them in `fields`. If the properties are absent, the
SDK uses the emission arguments. For example:

```python
machineEventInstance.EventType(o6.NodeId(MyEventType))
machineEventInstance.SourceNode(o6.NodeId(pump))
pump << machineEventInstance
```

`createEvent` emits without a draft and returns the `EventId`, matching
C's `UA_Server_createEvent`. `emitEvent` is an alias for the same operation:

```python
eventId = server.createEvent(
    ns0.objtypes.BaseEventType,
    source=server.serverNode,
    message="Shutdown requested",
    severity=500,
)
```

Both validate `severity` against the OPC UA range and raise `ValueError`
outside `1..1000`. `source` defaults to the Server object, so
`server.createEvent(message="...")` is a valid minimal call. To subscribe
directly to a custom source, enable its `EventNotifier`
SubscribeToEvents bit. Events also reach the standard Server object.

`o6.Event(server, ...)` constructs the draft directly without emitting or
accessing the address space. `createEvent`, `emitEvent`, and `trigger()`
return `MaybeAwaitable[bytes]`; callers on another asyncio loop must await
the result.

### Inferring the event type

`eventType` defaults to `None`. The type argument passed to the SDK is selected
in this order: explicit `eventType`, then `eventInstance`'s `HasTypeDefinition`
when supplied, otherwise `source`'s declared `GeneratesEvent` target. Field
resolution still follows the precedence described above.

When the source type has exactly one `GeneratesEvent` reference to an
EventType, that EventType is used:

```python
@o6.objecttype(ns="plant", browseName="PumpFaultType")
class PumpFaultType(ns0.objtypes.BaseEventType):
    pass

@o6.objecttype(ns="plant", browseName="CavitationFaultType")
class CavitationFaultType(ns0.objtypes.BaseEventType):
    pass

@o6.objecttype(ns="plant", browseName="PumpType")
class PumpType(ns0.objtypes.BaseObjectType):
    pass

server.addReference(
    source=o6.NodeId(PumpType),
    reftype=ns0.reftypes.GeneratesEvent,
    target=o6.NodeId(PumpFaultType),
)
pump = PumpType(parent=server.objectsNode, browseName="Pump1")

eventId = server.createEvent(source=pump, message="Cavitation detected")
# eventType resolved to PumpFaultType, no eventType= needed
```

A type that declares no `GeneratesEvent` target falls back to
`BaseEventType` — the `server.createEvent(message="...")` example above
resolves this way, since the Server object's own type declares none. A type
that declares more than one `GeneratesEvent` target cannot be inferred and
raises `ValueError` naming the ambiguity:

```python
@o6.objecttype(ns="plant", browseName="ValveType")
class ValveType(ns0.objtypes.BaseObjectType):
    pass

server.addReference(
    source=o6.NodeId(ValveType),
    reftype=ns0.reftypes.GeneratesEvent,
    target=o6.NodeId(PumpFaultType),
)
server.addReference(
    source=o6.NodeId(ValveType),
    reftype=ns0.reftypes.GeneratesEvent,
    target=o6.NodeId(CavitationFaultType),
)
valve = ValveType(parent=server.objectsNode, browseName="Valve1")

server.emitEvent(source=valve, message="which fault?")
# ValueError: cannot infer eventType: type ... declares more than one
# GeneratesEvent target; pass eventType= explicitly
```

Without an explicit type or event instance, a `source` with no type definition
at all raises `ValueError` too. For either
error, pass `eventType=` explicitly — it wins regardless of what `source`'s
type declares.

Inference reads the live information model, so a `GeneratesEvent` reference
added or removed at runtime takes effect on the very next
`createEvent`/`trigger()`. A reusable `Event` draft resolves the type on every
trigger, so reassigning `eventInstance` or `source` takes effect next time.
Inference leaves the draft's `eventType` attribute as `None`.

### Firing an event from a Node handle

An Object or View node handle can fire an event sourced at itself with `<<`,
without navigating back to the owning `Server` and passing `source=`
explicitly:

```python
pump << o6.Event(server, message="Cavitation detected")
```

`<<` also accepts a plain mapping in place of an `Event` draft, as shorthand
for a one-off event:

```python
pump << {"message": "Cavitation detected", "severity": 400}
```

An existing event instance can be passed directly, or as `eventInstance` in
an argument mapping or draft:

```python
pump << machineEventInstance
pump << {"eventInstance": machineEventInstance}
pump << o6.Event(server, eventInstance=machineEventInstance)
```

The instance must be an Object of `BaseEventType` or a subtype on the same
server. Its current fields are read on every emission; the node is neither
modified nor deleted. To override a field for one emission:

```python
pump << {
    "eventInstance": machineEventInstance,
    "fields": {"/Message": o6.LocalizedText("Override for this emission")},
}
```

All forms emit from `pump`, identical to
`server.createEvent(source=pump, ...)`. A reusable `Event` draft's own `source`
field is left unchanged by `<<`, so the same draft can be fired against a
different node afterward. `<<` is only defined for Object and View nodes —
the only NodeClasses OPC UA defines an `EventNotifier` attribute for — so
`variable << o6.Event(...)` raises `TypeError` immediately, naming the
reason; a node handle obtained from a `Client` also raises `TypeError`,
since local event creation is server-only.

`<<` returns a `MaybeAwaitable[bytes]` like `emitEvent`, so on a server
running on an external asyncio loop it must be awaited **with
parentheses**:

```python
eventId = await (pump << o6.Event(server, message="Cavitation detected"))
```

Without the parentheses, `await pump << o6.Event(...)` parses as
`(await pump) << o6.Event(...)`, not `await (pump << o6.Event(...))` —
`await` binds to `pump` alone, since `<<` sits outside the grammar rule
`await` requires.

## Server-local monitored items

A server can subscribe to its own nodes without a client session. This is how
you drive internal logic from value changes and how you observe your own events.

```python
def onChange(monitoredItemId, nodeId, attributeId, dataValue, context):
    print(nodeId, dataValue.value)

item = server.createDataChangeMonitoredItem(
    "ns=1;s=Temp",
    onChange,
    samplingInterval=100.0,
    context={"tag": "temperature"},
)
```

The callback may be a plain function or `async def`. `context` is handed back
unchanged on every notification, `timestamps=` selects which timestamps the
`DataValue` carries (default `SOURCE`), and `monitoringMode=` sets the initial
mode. The returned object is an `o6.subscription.MonitoredItem` whose `id` is
the server-local identifier; delete it with either form:

```python
server.deleteMonitoredItem(item)          # or server.deleteMonitoredItem(item.id)
```

`item.itemToMonitor` identifies the monitored node and attribute; `item.mode`
reports the accepted initial mode. `item.requestedParams` retains the creation
parameters, and `item.params` includes the backend's revised sampling interval
and queue size. These properties return independent snapshots, including nested
filters. Editing a snapshot does not reconfigure the item.

Keep the handle returned by creation to inspect its metadata. Constructing
`MonitoredItem(server=server, monitoredItemId=id)` provides an alias for validity
checks and deletion, but its configuration properties raise `RuntimeError`
because creation metadata is unavailable. Deleting through any alias or numeric
ID, or cleaning up the native server, invalidates retained handles.

| Operation | Local support |
| --- | --- |
| Create and inspect | Supported for data changes and events |
| `item.delete()` / `server.deleteMonitoredItem(...)` | Supported on the owning server |
| `item.modify(...)` | Raises `NotImplementedError`; no public local backend API |
| `item.setMonitoringMode(...)` | Raises `NotImplementedError`; no public local backend API |
| `item.setTriggering(...)` | Raises `NotImplementedError`; no public local backend API |

Unsupported operations raise immediately, including in async code, before
scheduling work or changing state. Delete and recreate the item to change its
configuration. Local items have no client subscription or publishing interval.
Creation and deletion can be awaited from the server's loop or another asyncio
loop; synchronous callers receive the result directly.

Event monitoring needs a filter with at least one select clause;
`createEventMonitoredItem` raises `ValueError` without one. The easiest way
to build a filter is the query parser:

```python
eventFilter = ns0.datatypes.EventFilter.parse("SELECT /Message, /Severity, /SourceName")

item = server.createEventMonitoredItem(
    server.serverNode,
    lambda monitoredItemId, fields, context: print(fields),
    selectClauses=list(eventFilter.selectClauses),
)
```

`whereClause=` adds a `ContentFilter` alongside `selectClauses=`. For full
control — a complete `EventFilter`, plus `queueSize`, `discardOldest`,
`clientHandle`, `samplingInterval`, and `monitoringMode` — pass `eventFilter=`
instead (not together with `selectClauses=`/`whereClause=`; that raises
`TypeError`):

```python
item = server.createEventMonitoredItem(
    server.serverNode,
    onEvent,
    eventFilter=eventFilter,
    queueSize=10,
)
```

One of `selectClauses=` or `eventFilter=` is required; omitting both raises
`ValueError`.

The callback receives `(monitoredItemId, fields, context)`, where `fields` is a
`dict[str, Any]` keyed by selected event-filter paths, such as `"/Message"` or
`"/ConditionName/Id"`. For example, read the message with `fields["/Message"]`.

For event items, `itemToMonitor.attributeId` is `EVENT_NOTIFIER` and
`params.filter` retains the event filter. Events are driven by emission:
`samplingInterval` is retained and revised by the backend but does not set an
event polling period. `clientHandle` is retained but does not route local
callbacks. `queueSize` and `discardOldest` control local notification buffering;
there is no remote Publish request or client publishing schedule.

## Timers

Periodic work belongs on the server's event loop, not on a thread of your own:

```python
def poll():
    server.write("ns=1;s=Temp", read_sensor())

callbackId = server.addRepeatedCallback(poll, 500.0)      # every 500 ms
server.changeRepeatedCallbackInterval(callbackId, 1000.0)
server.removeCallback(callbackId)
```

The callback runs on the loop thread, so the same rule as everywhere else
applies: keep it short. Intervals are milliseconds.
