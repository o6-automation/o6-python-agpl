#!/usr/bin/env python3
"""
Event monitoring example using the o6 high-level client API.

Subscribes to event notifications on the OPC UA Server node (i=2253).
The test server fires a synthetic BaseEventType event every 2 seconds via a
repeated server-side callback, so events should start arriving immediately.

The default EventFilter selects the six standard BaseEventType fields:
  EventId, EventType, SourceName, Time, Message, Severity

Run a compatible OPC UA server first, e.g. the test server:
    ./tests/testserver/testserver
"""

import asyncio
import o6
from o6 import types

ENDPOINT = "opc.tcp://localhost:4840"
# The OPC UA Server node (i=2253) has EventNotifier set; the test server fires
# a BaseEventType event on it every 2 seconds.
SERVER_NODE = "i=2253"


# --- Callback styles ---


def on_event_simple(event: dict) -> None:
    """1-argument callback receives just the event field dict."""
    msg = event.get("/Message")
    sev = event.get("/Severity")
    src = event.get("/SourceName")
    print(f"  [event] source={src}  severity={sev}  message={msg}")


def on_event_with_context(item: o6.MonitoredItem, event: dict) -> None:
    """2-argument callback also receives the MonitoredItem (use item.context for user data)."""
    msg = event.get("/Message")
    sev = event.get("/Severity")
    src = event.get("/SourceName")
    print(f"  [event] source={src}  severity={sev}  message={msg}")
    print(f"          >>> additional context={item.context}")


# ---------------------------------------------------------------------------
# Sync usage
# ---------------------------------------------------------------------------


def main_sync() -> None:
    print("=== Event monitoring (sync) ===")

    with o6.Client(ENDPOINT) as client:
        print(f"Connected. Monitoring events on {SERVER_NODE} ...")

        # Simplest form – uses the default subscription and default EventFilter
        listener = client.monitor_event(SERVER_NODE, on_event_simple)
        print(f"  MonitoredItem id={listener.monitored_item_id}")

        print("Deleting listener ...")
        listener.delete()

    print("Done (sync).")


# ---------------------------------------------------------------------------
# Async usage
# ---------------------------------------------------------------------------


async def main_async() -> None:
    print("=== Event monitoring (async) ===")

    async with o6.Client(ENDPOINT) as client:
        print(f"Connected. Monitoring events on {SERVER_NODE} ...")

        # Create an explicit subscription, then attach an event listener.
        sub = await client.create_subscription(publishing_interval=500.0)

        # Use a custom EventFilter – select only Message and Severity.
        event_filter = types.EventFilter()
        select_clauses = []
        for field in ("Message", "Severity"):
            sao = types.SimpleAttributeOperand()
            sao.type_definition_id = o6.ns.ns0.objtypes.BaseObjectType.BaseEventType
            sao.browse_path = [types.QualifiedName(field)]
            sao.attribute_id = o6.AttributeId.VALUE
            select_clauses.append(sao)
        event_filter.select_clauses = select_clauses

        listener = await sub.monitor_event(
            SERVER_NODE,
            on_event_with_context,
            event_filter=event_filter,
            context="my-context",
        )
        print(f"  MonitoredItem id={listener.monitored_item_id}")

        # Wait for the server's periodic events (fired every 2 seconds).
        await asyncio.sleep(5)

        await listener.delete()
        await sub.delete()

    print("Done (async).")


if __name__ == "__main__":
    main_sync()
    asyncio.run(main_async())
