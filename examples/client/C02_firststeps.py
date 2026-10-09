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
Client Basics: Read, Write, and Subscriptions
=============================================

Walks through the high-level ``o6.Client`` API end to end: connecting to
a server, reading and writing single and multiple values, calling a
method, subscribing to a variable for event-driven updates, and finally
introspecting the address space via ``client[NodeId]`` and ``client.browse()``.

The example is wired against `S03_firststeps.py` and talks to the
address space defined there (``Plant / Temperature``, ``Plant / Pressure``,
``Plant / Counter``, ``Plant / Running``, ``Plant / Add``, …).
"""

# BEGIN MD
# Every line in this example goes through the high-level ``o6.Client``
# API — the same shortcuts the rest of the documentation uses for
# everyday work. The raw ``serviceX`` methods (covered in
# `C01_lowlevel.py`) are what the high-level calls wrap internally.
# END MD

import os

import socket
import time
from o6 import Client, StatusCodeError, AttributeId

EXAMPLE_PORT = int(os.environ.get("O6_EXAMPLE_PORT", "4840"))
EXAMPLE_ENDPOINT = f"opc.tcp://localhost:{EXAMPLE_PORT}"

# BEGIN MD
# ## 1. Connection Setup
# The endpoint URL points at the server. `socket.gethostname()` is the
# same method used in the other examples: it makes the URL match the
# hostname the server advertises during discovery, which keeps
# encrypted endpoints happy.
# END MD

# BEGIN CODE
print("--- 1. Connection Setup ---")
localhost = "localhost"
endpoint_url = EXAMPLE_ENDPOINT
print(f"Connecting to {endpoint_url} ...")
# END CODE

# BEGIN MD
# ## 2. Basic Read / Write
# `client.read(nodeid)` fetches the current value of a variable;
# `client.write(nodeid, value)` assigns a new one. Both correspond to
# the OPC UA `Read` and `Write` services. NodeIds are passed as
# strings, and the SDK infers the OPC UA data type from the Python
# type of the value you provide.
#
# The `with Client(...) as client:` block opens the secure channel
# and session on `__enter__` and tears them down on `__exit__` —
# connection failures appear as `StatusCodeError`.
# END MD

# BEGIN CODE
try:
    with Client(endpoint_url) as client:
        print("Connected.")

        print()
        print("--- 2. Basic Read / Write ---")
        try:
            value = client.read("ns=1;i=1004")  # Plant / Counter (Int32)
            print(f"Counter = {value}")
        except StatusCodeError as e:
            print(f"Error: read failed: {e}")

        try:
            client.write("ns=1;i=1004", 42)
            print("Wrote Counter -> 42")

            new_value = client.read("ns=1;i=1004")
            print(f"Counter = {new_value}")
        except StatusCodeError as e:
            print(f"Error: write failed: {e}")
        # END CODE

        # BEGIN MD
        # ## 3. Multiple Read / Write
        # `client.read([...])` accepts a list and returns a list of values in
        # the same order; `client.write({...])` accepts a dictionary mapping each
        # NodeId to its new value. The SDK packs them into a single
        # `Read` / `Write` service request.
        # END MD

        # BEGIN CODE
        print()
        print("--- 3. Multiple Read / Write ---")
        try:
            values = client.read(
                [
                    "ns=1;i=1001",  # Temperature (Double)
                    "ns=1;i=1002",  # Pressure    (Double)
                    "ns=1;i=1003",  # Status      (String)
                    "ns=1;i=1004",  # Counter     (Int32)
                ]
            )
            print(f"Read = {values}")
        except StatusCodeError as e:
            print(f"Error: multiple read failed: {e}")

        try:
            client.write(
                {
                    "ns=1;i=1001": 25.0,  # Temperature
                    "ns=1;i=1003": "online",  # Status
                    "ns=1;i=1004": 100,  # Counter
                }
            )
            print("Wrote Temperature, Status, Counter.")
        except StatusCodeError as e:
            print(f"Error: multiple write failed: {e}")
        # END CODE

        # BEGIN MD
        # ## 4. Method Call
        # `client.call(object_id, method_id, input_args)` invokes a server-side
        # method. The return value is a tuple `(status_code, *output_args)`.
        # The first element is the per-call StatusCode, and the rest are the
        # declared output arguments in order.
        #
        # `S03_firststeps.py` exposes an `Add` method at `ns=1;i=2001` on
        # the `Plant` object. `Plant`'s NodeId is allocated dynamically at
        # server startup, so we resolve it by name with a single browse.
        # END MD

        # BEGIN CODE
        print()
        print("--- 4. Method Call ---")
        refs = client.browse(
            "i=85",
            resultMask=63,  # ask for every reference field
        )
        plant_id = next(r.nodeId for r in refs if r.browseName.name == "Plant")
        print(f"Plant NodeId = {plant_id}")

        try:
            result = client.call(
                plant_id,  # object_id
                "ns=1;i=2001",  # method_id (Plant / Add)
                [3.0, 4.0],  # input_args: two Doubles
            )
            status, *outputs = result
            print(f"Add(3.0, 4.0) -> status {status.name}, result {outputs}")
        except Exception as e:
            print(f"Error: method call failed: {e}")
        # END CODE

        # BEGIN MD
        # ## 5. Subscriptions
        # Polling a value in a tight loop wastes resources when nothing
        # is changing. A `Subscription` plus one or more `MonitoredItem`s lets
        # the server *publish* a notification only when a value actually changes.
        #
        # The way is: create a subscription with a publishing interval
        # (how often the server is *allowed* to publish), register a monitored
        # item with a sampling interval (how often the server *checks* the
        # value), and provide a callback that the SDK will invoke on the
        # client's event-loop thread whenever a new value arrives.
        # END MD

        # BEGIN CODE
        def on_data_change(monitored_item, value) -> None:
            """Server-pushed callback: runs on the client's event-loop thread."""
            print(f"Counter changed -> {value}")

        print()
        print("--- 5. Subscriptions ---")
        subscription = client.createSubscription(publishingInterval=1000)

        print("Monitoring Plant / Counter (ns=1;i=1004) ...")
        monitored_item = client.monitor(
            target="ns=1;i=1004",
            callback=on_data_change,
            subscription=subscription,
            samplingInterval=500,
        )

        for i in range(3):
            client.write("ns=1;i=1004", 200 + i)
            time.sleep(1)

        print("Cleaning up subscription.")
        monitored_item.delete()
        subscription.delete()
    # END CODE

    # BEGIN MD
    # ## 6. Browsing the Address Space
    # `client[nodeid]` is a shortcut for fetching a `Node` object for a
    # given NodeId. The `Node` object can be
    # printed, used as the target of `client.browse(...)`, or read for any
    # of its attributes via `node(attr=AttributeId.X)`.
    #
    # `client.browse(node)` walks one level out from the given node,
    # returning a list of `ReferenceDescription`s. The `result_mask`
    # keyword controls which fields each reference carries back
    # (browse name, display name, node class, type definition, ...). The
    # default is `0`; pass `63`(or `BrowseResultMask(63)`) to get every field populated.
    # END MD

    # BEGIN CODE
    # New `with` block — the previous one's subscription was deleted
    # and its `client` is no longer connected.
    with Client(endpoint_url) as client:
        print()
        print("--- 6. Browsing the Address Space ---")
        node = client["i=85"]  # The standard `Objects` folder
        print(f"Node       = {node}")
        print(f"BrowseName = {node(attr=AttributeId.BROWSE_NAME)}")
        print(f"NodeClass  = {node(attr=AttributeId.NODE_CLASS)}")
        # (Browsing children of an ObjectNode is covered in
        # `C01_lowlevel.py` — use `result_mask=63` to get names.)

except StatusCodeError as e:
    print(f"Error: connection failed: {e}")
    print(f"Make sure an OPC UA server is running on localhost:{EXAMPLE_PORT}")
    print("(try: python examples/server/S03_firststeps.py)")

print()
print("Connection closed.")
print("=== Example completed ===")
# END CODE
