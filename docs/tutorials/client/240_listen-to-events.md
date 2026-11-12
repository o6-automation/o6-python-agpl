# Listen to events

An *event* is a discrete occurrence at a specific moment, such as a batch start, a batch end, a state transition or a client changing the setpoint. A value change says "the temperature moved from 20.0 to 20.1"; an event says "the still transitioned from `Filling` to `Heating`".

`client.monitorEvent(...)` attaches an event filter to an *event notifier*, a node the server treats as a source of events. The standard `Server` object (`i=2253`) is the source for server-emitted events. The distillery's `DistillingSystem` (`ns=1;i=1000`) is a notifier too, because its `EventNotifier` attribute is set.

This page covers:

1. Subscribe to events on a notifier.
2. Read the callback's event fields.
3. Filter events with the SQL-like string syntax.

!!! info
    This tutorial needs the [example server running](../setup.md) in the background. It assumes you know how to [create and connect](100_connect.md) a client, [browse](110_browse.md) the address space, [monitor data changes](200_monitor-datachange.md), and create separate [subscriptions](210_subscriptions.md). The NodeIds below belong to the example server's `DistillingSystem` object at `ns=1;i=1000`.

!!! tip "Getting an event on demand"
    A batch takes a minute or two at the default `--sim-speed`, so a five-second `sleep` rarely catches a state transition. Writing `Status/Setpoint` (`ns=1;i=1204`) fires an event immediately at any point in the batch. The snippets below do this.

---

## Subscribe to events on a notifier

Attach a callback to the server's event notifier. Each event arrives in the callback as a Python dict:

```python
item = client.monitorEvent(
    "i=2253",                                # the Server object
    callback=lambda fields: print("event:", fields),
)
```

The default `filter=` selects the standard `BaseEventType` fields (`EventId`, `EventType`, `SourceName`, `Time`, `Message`, `Severity`). Subscribing on `DistillingSystem` instead of the `Server` object narrows the source but keeps the same fields:

```python
item = client.monitorEvent(
    "ns=1;i=1000",                           # DistillingSystem
    callback=lambda fields: print("event:", fields),
)
```

#### Putting it all together

```python
import time
from o6 import Client

with Client("opc.tcp://localhost:4840") as client:
    item = client.monitorEvent(
        "i=2253",
        callback=lambda fields: print("event:", fields),
    )
    print("item:", item, "  item.id:", item.id)
    client.write("ns=1;i=1204", 87.0)   # fire an event immediately
    time.sleep(2)
```

---

## Read the callback's event fields

The callback receives a `dict` keyed by event-filter path strings such as `/EventId` and `/Message`, not by the bare BrowseName. The base event type is `o6.ns.ns0.objtypes.BaseEventType`, which defines:

| Field | Type |
|---|---|
| `/EventId` | `ByteString` |
| `/EventType` | `NodeId` |
| `/SourceName` | `String` |
| `/SourceNode` | `NodeId` |
| `/Time` | `DateTime` |
| `/ReceiveTime` | `DateTime` |
| `/LocalTime` | `DateTime` |
| `/Message` | `LocalizedText` |
| `/Severity` | `UInt16` |

Companion specifications and custom event types add their own fields, reached the same way. The distillery's `DistilleryEventType` adds `/1:Cycle` and `/1:State`, namespace-qualified because they are declared in namespace 1, not 0.

A typical handler reads the fields it needs and ignores the rest:

```python
def on_event(fields):
    print(f"{fields.get('/Time')}  [{fields.get('/Severity')}]  {fields.get('/Message')}")
```

#### Putting it all together

```python
import time
from o6 import Client

def on_event(fields):
    print(f"{fields.get('/Time')}  [{fields.get('/Severity')}]  {fields.get('/Message')}")

with Client("opc.tcp://localhost:4840") as client:
    client.monitorEvent("i=2253", callback=on_event)
    client.write("ns=1;i=1204", 87.5)
    time.sleep(2)
```

---

## Filter events with the SQL-like string syntax

A subscription on the `Server` object receives every event the server emits. Pass `filter=` to narrow it down. The simplest form is a string. The grammar is `SELECT <select-clause> WHERE <where-clause>`, with each clause a comma-separated list of `/<BrowseName>` paths. `/` alone means the event's root: `BaseEventType` for an untyped event, otherwise the concrete event type. Custom fields take their namespace prefix:

```python
item = client.monitorEvent(
    "i=2253",
    callback=lambda f: print("batch event:", f.get("/Message")),
    filter="SELECT /Message, /Severity, /1:Cycle, /1:State WHERE /Severity >= 500",
)
```

The string supports the comparison operators `=`, `!=`, `<`, `<=`, `>` and `>=` on any event field. The parser turns the string into an `EventFilter` object. The server applies the filter and drops non-matching events before they reach the client. The distillery emits severity `500` at a batch boundary (`Filling`, `Idle`), `400` for a client write and `200` for the steps in between. `WHERE /Severity >= 400` skips the routine ones.

For full control over the `EventFilter` (select clauses that aren't simple field paths, or `whereClause` trees the string grammar can't express), create the object with `EventFilter.parse(...)` and adjust it:

```python
from o6.ns.ns0.datatypes import EventFilter

event_filter = EventFilter.parse(
    "SELECT /Message, /Severity, /SourceName WHERE /Severity >= 500"
)
# event_filter.selectClauses, event_filter.whereClause are populated

client.monitorEvent(
    "i=2253",
    callback=lambda f: print("event:", f),
    filter=event_filter,
)
```

For operators the parser doesn't support, deeply nested `ContentFilter` trees, or operand types other than `SimpleAttributeOperand` and `LiteralOperand`, assemble the `EventFilter` from the raw structures (`SimpleAttributeOperand`, `ContentFilterElement`, `FilterOperator`, `ExtensionObject`). The [server events manual](../../manual/server/events.md) shows the structure.

!!! warning
    `EventFilter` support depends on the server. Some servers reject any custom `ContentFilter` (string or object form) with `BAD_EVENT_FILTER_INVALID`, even when it is spec-correct. If you don't control the server, wrap `monitorEvent(..., filter=...)` in `try`/`except` and fall back to the unfiltered form.

#### Putting it all together

```python
import time
from o6 import Client

with Client("opc.tcp://localhost:4840") as client:
    try:
        client.monitorEvent(
            "ns=1;i=1000",
            callback=lambda f: print("event:", f.get("/Message"), " severity:", f.get("/Severity")),
            filter="SELECT /Message, /Severity, /1:Cycle, /1:State WHERE /Severity >= 400",
        )
    except Exception as exc:
        # The client parser rejected the string syntax, or the server
        # doesn't honour custom ContentFilters at all (some servers
        # return BAD_EVENT_FILTER_INVALID). Either way, fall back to
        # the default filter and re-subscribe.
        print("custom filter refused, falling back to default:", exc)
        client.monitorEvent(
            "ns=1;i=1000",
            callback=lambda f: print("event:", f.get("/Message")),
        )
    client.write("ns=1;i=1204", 88.0)   # fire an event immediately
    time.sleep(2)
```

---

## Next steps

| Topic | What it covers |
|---|---|
| [Security](300_security.md) | Configure the Client Connection. |
| [Modify a subscription](220_modify-subscription.md) | Change a monitored item's queue size, sampling interval, or filter after the fact. |
| [Server tutorials: Events](../server/340_events.md) | How the distillery builds its event type and emits from the other side of the connection. |
