#!/usr/bin/env python3
# Copyright 2026 (c) o6 Automation GmbH
"""
Client for the Pump Simulation Server
=====================================

Talks to the `basic_sim_server.py` example: it connects, reads the
current pump/valve values, drives the left inlet valve open and
shut again, browses the server's ``Objects`` folder, reads all
five valves in a single batch request, and finally subscribes to
all five valves to receive server-pushed change notifications.

Run `basic_sim_server.py` in one terminal before starting this
script.
"""

# BEGIN MD
# This example goes through the high-level ``o6.Client`` API end to
# end: connect, read, write, browse, batch read, and subscribe.
# The interaction is split across two `with Client(...)` blocks
# (one for request/response traffic, one for the subscription)
# because subscriptions are bound to the active session and the
# blocks cleanly tear down the secure channel and session on exit.
# END MD

import socket
import time
from o6 import Client, Double, StatusCodeError

# BEGIN MD
# ## 1. Connection Setup
# `socket.gethostname()` builds the endpoint URL the same way the
# server does.
# END MD

# BEGIN CODE
localhost = "localhost"
endpoint_url = f"opc.tcp://{localhost}:4840"
print(f"Connecting to {endpoint_url} ...")
# END CODE

# BEGIN MD
# ## 2. Basic Read / Write
# `client.read(nodeid)` and `client.write(nodeid, value)` are 1:1
# with the OPC UA `Read` and `Write` services.  NodeIds can be
# passed as strings, and the SDK infers the OPC UA data type from
# the Python value you supply. Wrapping a raw ``0.5`` in
# ``Double(0.5)`` is optional but explicit.
# END MD

# BEGIN CODE
try:
    with Client(endpoint_url) as client:
        print("[INFO] Connected to server successfully!\n")

        # Read the current value of the left inlet pump.
        value = client.read("ns=1;s=PumpLIOpen")
        print(f"[READ]   Initial left-inflow value: {value}")

        # Open the valve to half flow.
        client.write("ns=1;s=PumpLIOpen", Double(0.5))
        value = client.read("ns=1;s=PumpLIOpen")
        print(f"[WRITE]  Left-inflow now: {value}")

        # Close it again.
        client.write("ns=1;s=PumpLIOpen", Double(0.0))
        value = client.read("ns=1;s=PumpLIOpen")
        print(f"[WRITE]  Left-inflow closed: {value}")
        # END CODE

        # BEGIN MD
        # ## 3. Browsing the Address Space
        # `client.browse("ns=0;i=85")` walks one level out of the standard
        # ``Objects`` folder.  The default `result_mask` returns
        # `ReferenceDescription` objects with their node id and a
        # `browse_name`. Pass an explicit `result_mask=63` to populate
        # every field (display name, node class, type definition, ...).
        # END MD

        # BEGIN CODE
        print("\n[BROWSE] Objects folder (ns=0;i=85):")
        for ref in client.browse("ns=0;i=85", resultMask=63):
            print(f"  - {ref.browseName.name}  ({ref.nodeId})")
        # END CODE

        # BEGIN MD
        # ## 4. Batch Read
        # `client.read([...])` accepts a list of NodeIds and returns a
        # matching list of values in a single ``Read`` service request.
        # This is the easiest way to grab the full state of the simulation
        # at once.
        # END MD

        # BEGIN CODE
        values = client.read(
            [
                "ns=1;s=PumpLIOpen",
                "ns=1;s=PumpLOOpen",
                "ns=1;s=PumpRIOpen",
                "ns=1;s=PumpROOpen",
                "ns=1;s=PumpCOpen",
            ]
        )
        print(f"\n[READ]   All valves: {values}")
# END CODE

except StatusCodeError as e:
    print(f"[ERROR]  Connection failed: {e}")
    print("Note:   Make sure the server is running on localhost:4840")
    print("        (try: python examples/sim_examples/server/basic_sim_server.py)")
except Exception as e:
    print(f"[ERROR]  Unexpected error: {e}")

# BEGIN MD
# ## 5. Subscriptions
# Polling a value in a tight loop wastes network traffic when nothing
# is changing.  A `Subscription` plus one or more `MonitoredItem`s
# lets the server *publish* a notification only when a value
# actually changes.
#
# The method is the following: create a subscription with a publishing interval
# (how often the server is *allowed* to publish), register a
# monitored item with a sampling interval (how often the server
# *checks* the value), and provide a callback that the SDK will
# invoke on the client's event-loop thread whenever a new value
# arrives.
#
# Subscriptions are bound to the active session, so we open a
# second `with Client(...)` block to keep the read/write traffic
# and the subscription flow independent.
# END MD

# BEGIN CODE
try:
    with Client(endpoint_url) as client:

        def on_data_change(monitored_item, value) -> None:
            """Server-pushed callback — runs on the client's event loop."""
            print(f"[EVENT]  {monitored_item} -> {value}")

        print("\n[INFO]   Creating subscription (1 s publishing interval)...")
        subscription = client.createSubscription(publishingInterval=1000)

        print("[INFO]   Monitoring all five valves...")
        monitored_items = client.monitor(
            target=[
                "ns=1;s=PumpLIOpen",
                "ns=1;s=PumpLOOpen",
                "ns=1;s=PumpRIOpen",
                "ns=1;s=PumpROOpen",
                "ns=1;s=PumpCOpen",
            ],
            callback=on_data_change,
            subscription=subscription,
            samplingInterval=500,
        )

        # Drive a few writes to trigger notifications on the
        # left inlet valve while the subscription is active.
        print("[INFO]   Toggling left-inflow valve to trigger notifications...")
        for level in (0.0, 0.5, 1.0, 0.25):
            client.write("ns=1;s=PumpLIOpen", Double(level))
            time.sleep(1.0)

        print("\n[INFO]   Cleaning up subscription...")
        for item in monitored_items:
            item.delete()
        subscription.delete()
        print("[INFO]   Subscription deleted.")
# END CODE

except StatusCodeError as e:
    print(f"[ERROR]  Subscription failed: {e}")
    print("Note:   Make sure the server is running on localhost:4840")
except Exception as e:
    print(f"[ERROR]  Unexpected error: {e}")

print("\n=== Example completed ===")
