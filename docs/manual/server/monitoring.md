# Local Monitored Items

Observe local values and events without creating a client session.

## Server-local monitored items

A server can monitor its own nodes without a client session. Use this to drive
internal logic from value changes and to observe your own events.

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

The callback can be a plain function or `async def`.

- `context` is passed back unchanged on every notification.
- `timestamps=` selects which timestamps the `DataValue` carries (default
  `SOURCE`).
- `monitoringMode=` sets the initial mode.

The call returns an `o6.subscription.MonitoredItem` whose `id` is the
server-local identifier. Delete it with either form:

```python
server.deleteMonitoredItem(item)          # or server.deleteMonitoredItem(item.id)
```

`item.itemToMonitor` identifies the monitored node and attribute. `item.mode`
is the accepted initial mode. `item.requestedParams` holds the creation
parameters. `item.params` includes the backend's revised sampling interval and
queue size. These properties return independent snapshots, including nested
filters; editing a snapshot does not reconfigure the item.

Keep the handle returned by creation to inspect its metadata.
`MonitoredItem(server=server, monitoredItemId=id)` creates an alias for validity
checks and deletion. Its configuration properties raise `RuntimeError`, because
it has no creation metadata. Deleting through any alias or numeric ID, or
cleaning up the native server, invalidates retained handles.

| Operation | Local support |
| --- | --- |
| Create and inspect | Supported for data changes and events |
| `item.delete()` / `server.deleteMonitoredItem(...)` | Supported on the owning server |
| `item.modify(...)` | Raises `NotImplementedError`; no public local backend API |
| `item.setMonitoringMode(...)` | Raises `NotImplementedError`; no public local backend API |
| `item.setTriggering(...)` | Raises `NotImplementedError`; no public local backend API |

Unsupported operations raise immediately, also in async code, before
scheduling work or changing state. To change the configuration, delete and
recreate the item. Local items have no client subscription or publishing
interval. Creation and deletion can be awaited from the server's loop or another
asyncio loop; synchronous callers get the result directly.

Event monitoring needs a filter with at least one select clause. Pass
`selectClauses=` or `eventFilter=`; `createEventMonitoredItem` raises
`ValueError` when both are missing. Build the filter with the query parser:

```python
eventFilter = ns0.datatypes.EventFilter.parse("SELECT /Message, /Severity, /SourceName")

item = server.createEventMonitoredItem(
    server.serverNode,
    lambda monitoredItemId, fields, context: print(fields),
    selectClauses=list(eventFilter.selectClauses),
)
```

`whereClause=` adds a `ContentFilter` next to `selectClauses=`. For full
control, pass `eventFilter=` with a complete `EventFilter`, plus `queueSize`,
`discardOldest`, `clientHandle`, `samplingInterval` and `monitoringMode`.
Combining `eventFilter=` with `selectClauses=` or `whereClause=` raises
`TypeError`:

```python
item = server.createEventMonitoredItem(
    server.serverNode,
    onEvent,
    eventFilter=eventFilter,
    queueSize=10,
)
```

The callback receives `(monitoredItemId, fields, context)`. `fields` is a
`dict[str, Any]` keyed by the selected event-filter paths, such as `"/Message"`
or `"/ConditionName/Id"`; read the message with `fields["/Message"]`.

For event items, `itemToMonitor.attributeId` is `EVENT_NOTIFIER` and
`params.filter` holds the event filter. Emission drives event notifications:
`samplingInterval` is stored and revised by the backend but sets no polling
period. `clientHandle` is stored but does not route local callbacks.
`queueSize` and `discardOldest` control local notification buffering. There is
no remote Publish request or client publishing schedule.
