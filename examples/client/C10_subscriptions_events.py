#!/usr/bin/env python3
# Copyright 2026 (c) o6 Automation GmbH
# SPDX-License-Identifier: AGPL-3.0-or-later
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

"""
Event monitoring with the o6 high-level client API.

Subscribes to events on the OPC UA Server node (i=2253). The example
runs its own embedded server, which fires a synthetic BaseEventType
event every 0.5 seconds from a repeated server-side callback, so events
arrive immediately.

The default EventFilter selects the six standard BaseEventType fields:
  EventId, EventType, SourceName, Time, Message, Severity
"""

import os

import asyncio
import o6
from o6 import Server
from o6.ns import ns0

EXAMPLE_PORT = int(os.environ.get("O6_EXAMPLE_PORT", "4840"))
EXAMPLE_ENDPOINT = f"opc.tcp://localhost:{EXAMPLE_PORT}"

ENDPOINT = EXAMPLE_ENDPOINT
# The OPC UA Server node (i=2253) has EventNotifier set; our embedded server
# fires a BaseEventType event on it every 0.5 seconds.
SERVER_NODE = "i=2253"


def _start_event_server() -> Server:
    """Start an embedded server that periodically fires a BaseEventType event."""
    server = Server(port=EXAMPLE_PORT)
    server.addRepeatedCallback(
        lambda: server.emitEvent(message=o6.LocalizedText("Periodic test event"), severity=200),
        500,
    )
    server.start()
    return server


# BEGIN MD
# ## 1. Event callback styles
# A 1-argument callback receives the event field dict, keyed by
# BrowsePath (`/Message`, `/Severity`, ...), with one entry per field the
# EventFilter selects. A 2-argument callback also receives the
# `MonitoredItem`, which tells events from several monitored nodes apart.
# END MD


# BEGIN CODE
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


# END CODE


# ---------------------------------------------------------------------------
# Sync usage
# ---------------------------------------------------------------------------

# BEGIN MD
# ## 2. Sync usage: `client.monitorEvent()`
# `monitorEvent(nodeId, callback)` attaches to the client's default
# subscription and uses the default EventFilter (the six standard
# BaseEventType fields). `listener.delete()` removes the monitored item.
# The subscription is removed when the `with` block exits.
# END MD


# BEGIN CODE
def main_sync() -> None:
    print("--- 2. Sync usage: client.monitorEvent() ---")

    with o6.Client(ENDPOINT) as client:
        print(f"Connected. Monitoring events on {SERVER_NODE} ...")

        listener = client.monitorEvent(SERVER_NODE, on_event_simple)
        print(f"Monitored item id = {listener.id}")

        listener.delete()
        print("Listener removed.")


# END CODE


# ---------------------------------------------------------------------------
# Async usage
# ---------------------------------------------------------------------------

# BEGIN MD
# ## 3. Async usage: an explicit subscription and a custom EventFilter
# The `selectClauses` of an `EventFilter` list the fields to receive.
# Each clause is a `SimpleAttributeOperand` that names a `BaseEventType`
# field by BrowsePath. A custom filter passed with `filter=` limits the
# event dict to the selected fields instead of the default six.
# END MD


# BEGIN CODE
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
    # END CODE


if __name__ == "__main__":
    server = _start_event_server()
    try:
        main_sync()
        asyncio.run(main_async())
        print()
        print("=== Example completed ===")
    finally:
        server.stop()
