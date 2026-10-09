# Subscribe monitoring on the server side

A subscription is the standard view of value changes — *push* notifications the server sends on its publishing interval. The same mechanism exists server-side: a server can register a monitored item on its own address space and react to value changes the same way, with no monitoring session in sight.

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

The callback signature is `(monitored_item_id, node_id, attribute_id, data_value, context)`. `context` is the dict the caller passed at registration, handed back unchanged on every notification — useful for tagging the callback with metadata rather than capturing it in a closure.

The returned object is an `o6.subscription.MonitoredItem`. Delete it with `server.deleteMonitoredItem(item)` or `server.deleteMonitoredItem(item.id)`.

!!! info
    Server-local monitored items exist for internal logic, *not* for shipping data across the network. The standard subscription path is unchanged. The two coexist on the same nodestore.

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

Incoming writes of `90.0` to `Setpoint` trigger both the server-side monitor and any other subscription. The server's monitor is the right place for *internal* reactions — audit logging, cross-instance triggers, derived values — without the cost of polling.

---

## Event monitored items

Event monitoring is the same shape, with an event-specific filter. The filter selects which fields of an event are delivered, plus an optional `whereClause` for content filtering.

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

The `EventFilter.parse(...)` helper builds a valid filter from a query string — the same shape the [client subscription filter tutorial](../client/230_subscription-filter.md) uses. The callback receives `(monitored_item_id, fields, context)` where `fields` is a `dict[str, Any]` keyed by selected event-filter paths, such as `"/Message"` or `"/ConditionName/Id"`. Read a selected field with `fields["/Message"]`.

!!! info
    An empty `EventFilter` is rejected with `BadEventFilterInvalid`. Always specify at least one select clause, or use `EventFilter.parse(...)` to build one for you.

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

Server-local event monitors observe the same events an external subscription would. They are the right place for *cross-instance* logic: one still's `Operating=False` triggers another still's `Operating=False`, or a server-wide audit log captures every transition regardless of which session triggered it.

---

## Driving housekeeping from a monitor

The distillery's natural place for an internal monitor is `Operating`. When `Operating=False`, the simulation should park the still after the current batch:

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

The monitor fires on the loop thread the moment the value changes. The simulation's update loop sees the new value on its next tick and parks at the right boundary.

For cross-instance logic — a still finishing a batch triggers another still to start — event monitors on the source instance work the same way.

---

## What's next?

The distillery has its full server-side behaviour: typed model, write handlers, method implementations, periodic timers, internal monitors. The next page finishes the production story with one last loose end.

- [Server callbacks](330_server-callbacks.md) — the `addRepeatedCallback` API that drives the update loop in lockstep with these monitors.
- [Server manual](../../manual/server/events-and-timers.md#server-local-monitored-items) — the full server-local monitored item API, including `createEventMonitoredItemEx` for full control over an event filter (`createDataChangeMonitoredItem` has no `Ex` counterpart).
