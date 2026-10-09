# Listen to events

You've been watching the Kettle values change continuously, and you've tuned the deadband so the server only pushes meaningful changes. But the distillery also has *events* — discrete things that happen at specific moments (a batch starts, a batch ends, a state transition, a client changes the setpoint). Events are different from value changes: a value change is "the temperature moved from 20.0 to 20.1", an event is "the still just transitioned from `Filling` to `Heating`". This page is about subscribing to those.

`client.monitorEvent(...)` attaches an event filter to an *event notifier* — a node that the server treats as a source of events. The standard `Server` object (`i=2253`) is the canonical source for server-emitted events; the distillery's `DistillingSystem` (`ns=1;i=1000`) is one too, since its `EventNotifier` attribute is set.

This page walks through three steps:

1. Subscribe to events on a notifier.
2. Read the callback's event fields.
3. Filter events with the SQL-like string syntax.

!!! info
    This tutorial expects the [example server running](../setup.md) in the background, and assumes you know how to [create and connect](100_connect.md) a client, how to [browse](110_browse.md) the address space, how to [monitor data changes](200_monitor-datachange.md), and how to create separate [subscriptions](210_subscriptions.md). The `NodeId`s used below are the ones exposed by the distilling example server's `DistillingSystem` object at `ns=1;i=1000`.

!!! tip "Getting an event on demand"
    A batch takes a minute or two of wall clock at the default `--sim-speed`, so a state transition isn't something a five-second `sleep` reliably catches while you're following along. Writing `Status/Setpoint` (`ns=1;i=1204`) fires an event immediately regardless of where the batch is — that's what the snippets below do to get something to look at without waiting.

---

## Subscribe to events on a notifier

The simplest call attaches a callback to a server's event notifier. Every event the server emits lands in the callback as a Python dict:

```python
item = client.monitorEvent(
    "i=2253",                                # the Server object
    callback=lambda fields: print("event:", fields),
)
```

The default `filter=` selects the standard `BaseEventType` fields (`EventId`, `EventType`, `SourceName`, `Time`, `Message`, `Severity`). Subscribing on `DistillingSystem` directly instead of the `Server` object narrows the source without narrowing the fields:

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

The callback receives a `dict` whose keys are event-filter path strings — `/EventId`, `/Message`, and so on, not the bare `BrowseName`. The base event type is `o6.ns.ns0.objtypes.BaseEventType`, which defines:

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

Companion specs and custom event types extend this base with their own fields, reached the same way: the distillery's own `DistilleryEventType` adds `/1:Cycle` and `/1:State` (namespace-qualified, since they're declared in namespace 1, not 0).

A typical handler pulls out the fields it cares about and ignores the rest:

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

A blanket subscription on the `Server` object will see *every* event the server emits. To narrow it down, pass a `filter=` argument.

The string form is the easy one. The full grammar is `SELECT <select-clause> WHERE <where-clause>`, with each clause a comma-separated list of `/<BrowseName>` paths. `/` alone means "the event's root" — `BaseEventType` for an untyped event, the concrete event type otherwise. The distillery's custom fields are reached the same way as the standard ones, with their namespace prefix:

```python
item = client.monitorEvent(
    "i=2253",
    callback=lambda f: print("batch event:", f.get("/Message")),
    filter="SELECT /Message, /Severity, /1:Cycle, /1:State WHERE /Severity >= 500",
)
```

The string supports the standard comparison operators (`=`, `!=`, `<`, `<=`, `>`, `>=`) over any of the event's fields. The parser turns the string into an `EventFilter` object and the server applies the filter — events that don't match are dropped before they reach the client. The distillery emits `500` at a batch boundary (`Filling`, `Idle`), `400` for a client write, `200` for the steps in between — so `WHERE /Severity >= 400` is a reasonable way to skip the routine ones.

When you need full control over the `EventFilter` shape (custom `select` clauses that aren't simple field paths, or `whereClause` trees that the string grammar can't express), build the object yourself and parse a `SELECT` / `WHERE` query into it:

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

For completely bespoke filters — operators the parser doesn't support, deeply nested `ContentFilter` trees, or operand types other than `SimpleAttributeOperand` and `LiteralOperand` — assemble the `EventFilter` from the raw structures (`SimpleAttributeOperand`, `ContentFilterElement`, `FilterOperator`, `ExtensionObject`). The [server events manual](../../manual/server/events-and-timers.md) shows the full shape.

!!! warning
    `EventFilter` support is server-dependent. Some servers reject any custom `ContentFilter` (string or object form) with `BAD_EVENT_FILTER_INVALID` even for a filter that's spec-correct. Wrap `monitorEvent(..., filter=...)` in a `try`/`except` and fall back to the unfiltered form if you don't control the server.

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

## What's next?

- [Security](300_security.md) — Configure the Client Connection.
- [Modify a subscription](220_modify-subscription.md) — change a monitored item's queue size, sampling interval, or filter after the fact.
- [Server tutorials: Events](../server/340_events.md) — how the distillery builds its event type and emits from the other side of the connection.
