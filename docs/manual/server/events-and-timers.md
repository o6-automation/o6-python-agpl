# Events, monitored items & timers

## Events

Emit a one-shot event with `emitEvent`, or retain a reusable event draft from
`createEvent`:

```python
event = server.createEvent(
    ns0.objtypes.BaseEventType,
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
event.payloadSource = machineEventInstance
event.trigger()
```

Resolution order is explicit `event.fields`, then `payloadSource`, then the
standard `BaseEventType` defaults. `trigger()` returns the generated 16-byte
`EventId`.

`emitEvent` is the same call without the draft, and it returns the same
`EventId`:

```python
eventId = server.emitEvent(
    ns0.objtypes.BaseEventType,
    source=server.serverNode,
    message="Shutdown requested",
    severity=500,
)
```

Both validate `severity` against the OPC UA range and raise `ValueError`
outside `1..1000`. The defaults are `BaseEventType` and the Server object as
source, so `server.emitEvent(message="...")` is a valid minimal call. Remember
that only nodes whose `EventNotifier` attribute permits it can act as a source;
the Server object always can.

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

Event monitoring needs a filter with at least one select clause — an empty
`EventFilter` is rejected with `BadEventFilterInvalid`. The easiest way to build
one is the query parser:

```python
eventFilter = ns0.datatypes.EventFilter.parse("SELECT /Message, /Severity, /SourceName")

item = server.createEventMonitoredItem(
    server.serverNode,
    lambda monitoredItemId, fields, context: print(fields),
    selectClauses=list(eventFilter.selectClauses),
)
```

`whereClause=` adds a `ContentFilter`, and `createEventMonitoredItemEx` takes
the whole `EventFilter` plus `queueSize`, `discardOldest`, `clientHandle`,
`samplingInterval`, and `monitoringMode` when you need full control:

```python
item = server.createEventMonitoredItemEx(
    server.serverNode,
    onEvent,
    eventFilter=eventFilter,
    queueSize=10,
)
```

The callback receives `(monitoredItemId, fields, context)`, where `fields` is a
dict keyed by `QualifiedName`.

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
