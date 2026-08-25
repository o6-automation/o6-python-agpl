# Listen to events

You've been watching the Kettle values change continuously, and you've tuned the deadband so the server only pushes meaningful changes. But the distillery also has *events* — discrete things that happen at specific moments (a batch starts, a batch ends, a state transition). Events are different from value changes: a value change is "the temperature moved from 20.0 to 20.1", an event is "the still just transitioned from `Filling` to `Heating`". This page is about subscribing to those.

`client.monitorEvent(...)` attaches an event filter to an *event notifier* — a node that the server treats as a source of events. The standard `Server` object (`i=2253`) is the canonical source for server-emitted events; any object that has an `EventNotifier` attribute set to a non-zero value can also be a source.

This page walks through three steps:

1. Subscribe to events on a notifier.
2. Read the callback's event fields.
3. Filter events with the SQL-like string syntax.

!!! info
    This tutorial expects the [example server running](../../tutorials.md#running-the-example-server) in the background, and assumes you know how to [create and connect](100_connect.md) a client, how to [browse](110_browse.md) the address space, how to [monitor data changes](200_monitor-datachange.md), and how to create separate [subscriptions](210_subscriptions.md). The `NodeId`s used below are the ones exposed by the distilling example server's `DistillingSystem` object at `ns=1;i=1000`.

---

## Subscribe to events on a notifier

The simplest call attaches a callback to a server's event notifier. Every event the server emits lands in the callback as a Python dict:

```python
item = client.monitorEvent(
    "i=2253",                                # the Server object
    callback=lambda fields: print("event:", fields),
)
```

The default `filter=` selects the standard `BaseEventType` fields (`EventId`, `EventType`, `SourceName`, `Time`, `Message`, `Severity`)

#### Putting it all together

```python
import time
from o6 import Client

with Client("opc.tcp://localhost:4840") as client:
    item = client.monitorEvent(
        "i=2253",
        callback=lambda fields: print("event:", fields),
    )
    time.sleep(5)
```

---

## Read the callback's event fields

The callback receives a `dict` whose keys are the `BrowseName`s of the event fields. The base event type is `o6.ns.ns0.objtypes.BaseEventType`, which defines:

| Field | Type |
|---|---|
| `EventId` | `ByteString` |
| `EventType` | `NodeId` |
| `SourceName` | `String` |
| `SourceNode` | `NodeId` |
| `Time` | `DateTime` |
| `ReceiveTime` | `DateTime` |
| `LocalTime` | `DateTime` |
| `Message` | `LocalizedText` |
| `Severity` | `UInt16` |

Companion specs extend this base with their own fields. For example, the standard `AuditEventType` adds `ActionTimeStamp`, `Status`, `ServerId`, `ClientAuditEntryId`, and so on.

A typical handler pulls out the fields it cares about and ignores the rest:

```python
def on_event(fields):
    print(f"{fields.get('Time')}  [{fields.get('Severity')}]  {fields.get('Message')}")
```

#### Putting it all together

```python
import time
from o6 import Client

def on_event(fields):
    print(f"{fields.get('Time')}  [{fields.get('Severity')}]  {fields.get('Message')}")

with Client("opc.tcp://localhost:4840") as client:
    client.monitorEvent("i=2253", callback=on_event)
    time.sleep(5)
```

---

## Filter events with the SQL-like string syntax

A blanket subscription on the `Server` object will see *every* event the server emits. To narrow it down, pass a `filter=` argument.

The full `EventFilter` object is built from `SimpleAttributeOperand`s and `ContentFilterElement`s — verbose but exact:

```python
import o6
from o6.ns.ns0.datatypes import (
    EventFilter, ContentFilter, ContentFilterElement, FilterOperator,
    SimpleAttributeOperand, LiteralOperand,
)

msg_operand = SimpleAttributeOperand("i=2041")        # BaseEventType
msg_operand.browsePath = [o6.QualifiedName("Message")]

severity_operand = SimpleAttributeOperand("i=2041")
severity_operand.browsePath = [o6.QualifiedName("Severity")]

threshold = LiteralOperand()
threshold.value = 500

where_clause = ContentFilter()
where_clause.elements = [
    ContentFilterElement(
        filterOperator=FilterOperator.GREATER_THAN_OR_EQUAL,
        filterOperands=[severity_operand, threshold],   # Severity >= 500
    ),
]

event_filter = EventFilter(
    selectClauses=[msg_operand],
    whereClause=where_clause,
)

client.monitorEvent(
    "i=2253",
    callback=lambda f: print("event:", f),
    filter=event_filter,
)
```

For most cases, o6\\Python offers a SQL-like syntax parsed from a single string instead of building the operands by hand:

```python
item = client.monitorEvent(
    "i=2253",
    callback=lambda f: print("warn:", f.get("Message")),
    filter="Severity >= 500",
)
```

The string form supports the standard comparison operators (`=`, `!=`, `<`, `<=`, `>`, `>=`) over any of the `BaseEventType` fields. The server applies the filter — events that don't match are dropped before they reach the client.

!!! warning
    `EventFilter` support is server-dependent: some servers (including the distillery `--sim` example server) only implement the *default* event filter and reject any custom `ContentFilter` — string or object form — with `BAD_EVENT_FILTER_INVALID`, even for a filter that's spec-correct. Wrap `monitorEvent(..., filter=...)` in a `try`/`except` and fall back to the unfiltered form if you don't control the server.

#### Putting it all together

```python
import time
from o6 import Client

with Client("opc.tcp://localhost:4840") as client:
    try:
        client.monitorEvent(
            "i=2253",
            callback=lambda f: print("event:", f.get("Message")),
            filter="Severity >= 500",
        )
    except Exception as exc:
        print("server rejected the filter, falling back to unfiltered:", exc)
        client.monitorEvent("i=2253", callback=lambda f: print("event:", f.get("Message")))
    time.sleep(5)
```

---

## What's next?

- [Security](300_security.md) — Configure the Client Connection.
- [Modify a subscription](220_modify-subscription.md) — change a monitored item's queue size, sampling interval, or filter after the fact.
