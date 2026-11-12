# Subscription Events

Event monitoring with the o6 high-level client API.

Subscribes to events on the OPC UA Server node (i=2253). The example
runs its own embedded server, which fires a synthetic BaseEventType
event every 0.5 seconds from a repeated server-side callback, so events
arrive immediately.

The default EventFilter selects the six standard BaseEventType fields:
  EventId, EventType, SourceName, Time, Message, Severity

## 1. Event callback styles
A 1-argument callback receives the event field dict, keyed by
BrowsePath (`/Message`, `/Severity`, ...), with one entry per field the
EventFilter selects. A 2-argument callback also receives the
`MonitoredItem`, which tells events from several monitored nodes apart.

```python
def on_event_simple(event: dict) -> None:
    """1-argument callback receives just the event field dict."""
    msg = event.get("/Message")
    sev = event.get("/Severity")
    src = event.get("/SourceName")
    print(f"Event from {src}: severity={sev} message={msg}")


def on_event_with_context(item: o6.MonitoredItem, event: dict) -> None:
    """2-argument callback — the MonitoredItem is available for inspection."""
    msg = event.get("/Message")
    sev = event.get("/Severity")
    src = event.get("/SourceName")
    print(f"Event from {src}: severity={sev} message={msg}")
```

## 2. Sync usage: `client.monitorEvent()`
`monitorEvent(nodeId, callback)` attaches to the client's default
subscription and uses the default EventFilter (the six standard
BaseEventType fields). `listener.delete()` removes the monitored item.
The subscription is removed when the `with` block exits.

```python
def main_sync() -> None:
    print("--- 2. Sync usage: client.monitorEvent() ---")

    with o6.Client(ENDPOINT) as client:
        print(f"Connected. Monitoring events on {SERVER_NODE} ...")

        listener = client.monitorEvent(SERVER_NODE, on_event_simple)
        print(f"Monitored item id = {listener.id}")

        listener.delete()
        print("Listener removed.")
```

## 3. Async usage: an explicit subscription and a custom EventFilter
The `selectClauses` of an `EventFilter` list the fields to receive.
Each clause is a `SimpleAttributeOperand` that names a `BaseEventType`
field by BrowsePath. A custom filter passed with `filter=` limits the
event dict to the selected fields instead of the default six.

```python
async def main_async() -> None:
    print()
    print("--- 3. Async usage: custom EventFilter ---")

    async with o6.Client(ENDPOINT) as client:
        print(f"Connected. Monitoring events on {SERVER_NODE} ...")

        sub = await client.createSubscription(publishingInterval=500.0)

        event_filter = ns0.datatypes.EventFilter()
        select_clauses = []
        for field in ("Message", "Severity"):
            sao = ns0.datatypes.SimpleAttributeOperand()
            sao.typeDefinitionId = o6.ns.ns0.objtypes.BaseEventType
            sao.browsePath = [o6.QualifiedName(field)]
            sao.attributeId = o6.AttributeId.VALUE
            select_clauses.append(sao)
        event_filter.selectClauses = select_clauses

        listener = await client.monitorEvent(
            SERVER_NODE,
            on_event_with_context,
            filter=event_filter,
            subscription=sub,
        )
        print(f"Monitored item id = {listener.id}")

        # Wait for the server's periodic events.
        await asyncio.sleep(5)

        await listener.delete()
        await sub.delete()
        print("Listener and subscription removed.")
```

## Source Code

Download [`C10_subscriptions_events.py`](client-C10_subscriptions_events/C10_subscriptions_events.py) to run it locally.
