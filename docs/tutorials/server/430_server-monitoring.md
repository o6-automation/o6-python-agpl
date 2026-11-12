# Subscribe monitoring on the server side

Clients receive value changes through subscriptions: notifications the server pushes on its publishing interval. A server can also register monitored items on its own address space and react to changes without a client session.

This page covers two patterns:

- **Internal monitored items.** Drive housekeeping logic from value changes (`Operating` flips, `Setpoint` is rewritten, a batch boundary happens).
- **Server-side subscriptions to its own nodes.** Useful for cross-instance reactions, audit trails, and trigger logic without polling.

---

## Server-local data-change monitored items

`Server.createDataChangeMonitoredItem(...)` registers a monitored item on a server-local Variable. The callback runs on the server's event loop on every value change.

```python
import o6
from o6 import Server, StatusCode

server = Server(port=4840)

setpoint = server.addVariable("Setpoint", server.objectsNode, 85.0, nodeId="ns=1;i=1204")


def on_change(monitored_item_id, node_id, attribute_id, data_value, context):
    print(f"  [monitor] Setpoint changed to {data_value.value.value}")


server.createDataChangeMonitoredItem(
    "ns=1;i=1204",
    on_change,
    samplingInterval=100.0,            # 100 ms
    context={"label": "setpoint"},
)
```

The callback signature is `(monitored_item_id, node_id, attribute_id, data_value, context)`. `context` is the dict passed at registration, returned unchanged on every notification. Use it to attach metadata to the callback instead of capturing it in a closure.

The returned object is an `o6.subscription.MonitoredItem`. Delete it with `server.deleteMonitoredItem(item)` or `server.deleteMonitoredItem(item.id)`.

!!! info
    Server-local monitored items are for internal logic, not for sending data over the network. Client subscriptions work as before, and both kinds coexist on the same nodestore.

#### Putting it all together

```python
import time
import o6
from o6 import Server, StatusCode

server = Server(port=4840)
setpoint = server.addVariable("Setpoint", server.objectsNode, 85.0, nodeId="ns=1;i=1204")


def on_change(item_id, node_id, attr_id, dv, ctx):
    print(f"  [monitor] {ctx['label']} = {dv.value.value}")


server.createDataChangeMonitoredItem(
    "ns=1;i=1204",
    on_change,
    samplingInterval=100.0,
    context={"label": "setpoint"},
)
server.start()
```

A write of `90.0` to `Setpoint` triggers both the server-side monitor and any client subscription. Use server-side monitors for internal reactions such as audit logging, cross-instance triggers and derived values, without polling.

---

## Event monitored items

Event monitoring works the same way with an event filter. The filter selects which event fields are delivered and can add a `whereClause` to filter on content.

```python
from o6.ns import ns0


def on_event(item_id, fields, context):
    print(f"  [event] {fields}")


event_filter = ns0.datatypes.EventFilter.parse(
    "SELECT /Message, /Severity, /SourceName"
)

server.createEventMonitoredItem(
    server.serverNode,
    on_event,
    selectClauses=list(event_filter.selectClauses),
)
```

`EventFilter.parse(...)` builds a valid filter from a query string, as in the [client subscription filter tutorial](../client/230_subscription-filter.md). The callback receives `(monitored_item_id, fields, context)` where `fields` is a `dict[str, Any]` keyed by selected event-filter paths, such as `"/Message"` or `"/ConditionName/Id"`. Read a selected field with `fields["/Message"]`.

!!! info
    An empty `EventFilter` is rejected with `BadEventFilterInvalid`. Specify at least one select clause, or build the filter with `EventFilter.parse(...)`.

#### Putting it all together

```python
import time
import o6
from o6 import Server
from o6.ns import ns0

server = Server(port=4840)


def on_event(item_id, fields, context):
    print(f"  [event] {fields}")


event_filter = ns0.datatypes.EventFilter.parse(
    "SELECT /Message, /Severity, /SourceName"
)

server.createEventMonitoredItem(
    server.serverNode,
    on_event,
    selectClauses=list(event_filter.selectClauses),
)
server.start()
```

Server-local event monitors see the same events as a client subscription. Use them for cross-instance logic, for example one still's `Operating=False` setting another still's `Operating=False`, or for a server-wide audit log of every transition regardless of which session caused it.

---

## Driving housekeeping from a monitor

In the distillery, `Operating` is a good candidate for an internal monitor. When `Operating=False`, the simulation parks the still after the current batch:

```python
def on_operating_change(item_id, node_id, attr_id, dv, ctx):
    new_value = bool(dv.value.value)
    if not new_value:
        print("  [housekeeping] Operating=False — will park after current batch")


server.createDataChangeMonitoredItem(
    "ns=1;i=1203",
    on_operating_change,
    samplingInterval=100.0,
    context={"label": "operating"},
)
```

The monitor fires on the loop thread when the value changes. The simulation's update loop picks up the new value on its next tick and parks at the batch boundary.

For cross-instance logic, such as one still finishing a batch and starting another, use event monitors on the source instance.

---

## Next steps

| Topic | What it covers |
|---|---|
| [Server callbacks](330_server-callbacks.md) | The `addRepeatedCallback` API that drives the update loop in lockstep with these monitors. |
| [Server manual](../../manual/server/monitoring.md#server-local-monitored-items) | The full server-local monitored item API, including `createEventMonitoredItemEx` for full control over an event filter (`createDataChangeMonitoredItem` has no `Ex` counterpart). |
