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

Covers the high-level ``o6.Client`` API: connect, read and write single
and multiple values, call a method, subscribe to a variable, and inspect
the address space with ``client[NodeId]``.

The example uses the address space of `S03_firststeps.py`
(``Plant / Temperature``, ``Plant / Pressure``, ``Plant / Counter``,
``Plant / Running``, ``Plant / Add``, …).
"""

# BEGIN MD
# The high-level ``o6.Client`` calls wrap the raw ``serviceX`` methods
# shown in `C01_lowlevel.py`.
# END MD

import os

import socket
import time
from o6 import Client, StatusCodeError, AttributeId

EXAMPLE_PORT = int(os.environ.get("O6_EXAMPLE_PORT", "4840"))
EXAMPLE_ENDPOINT = f"opc.tcp://localhost:{EXAMPLE_PORT}"

# BEGIN MD
# ## 1. Connection Setup
# The endpoint URL points at the server on `localhost`. The
# `O6_EXAMPLE_PORT` environment variable overrides the default port 4840.
# END MD

# BEGIN CODE
print("--- 1. Connection Setup ---")
localhost = "localhost"
endpoint_url = EXAMPLE_ENDPOINT
print(f"Connecting to {endpoint_url} ...")
# END CODE

# BEGIN MD
# ## 2. Basic Read / Write
# `client.read(nodeid)` returns the current value of a variable.
# `client.write(nodeid, value)` assigns a new one. They use the OPC UA
# `Read` and `Write` services. NodeIds are passed as strings. The SDK
# infers the OPC UA data type from the Python type of the value.
#
# `with Client(...) as client:` opens the secure channel and session on
# `__enter__` and closes them on `__exit__`. Connection failures raise
# `StatusCodeError`.
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
        # `client.read([...])` takes a list and returns the values in the same
        # order. `client.write({...})` takes a dictionary that maps each NodeId to
        # its new value. Each call sends a single `Read` or `Write` request.
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
        # `client.call(object_id, method_id, input_args)` invokes a method on the
        # server. It returns a tuple `(status_code, *output_args)`: the per-call
        # StatusCode, then the declared output arguments in order.
        #
        # `Add` is at `ns=1;i=2001` on the `Plant` object. The server allocates
        # the NodeId of `Plant` at startup, so the code resolves it by name with
        # one browse.
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
        # A `Subscription` with one or more `MonitoredItem`s makes the server
        # publish a notification only when a value changes, instead of the client
        # polling.
        #
        # 1. Create a subscription with a publishing interval (how often the
        #    server may publish).
        # 2. Register a monitored item with a sampling interval (how often the
        #    server checks the value).
        # 3. Pass a callback. The SDK calls it on the client's event-loop thread
        #    for each new value.
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
    # `client[nodeid]` returns a `Node` for a NodeId. A `Node` can be printed,
    # passed to `client.browse(...)`, or read for any attribute with
    # `node(attr=AttributeId.X)`.
    #
    # `client.browse(node)` returns the `ReferenceDescription`s one level out
    # from the node. The `resultMask` keyword selects the fields each
    # reference carries (BrowseName, display name, node class, type
    # definition, ...). It defaults to `BrowseResultMask.ALL`.
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
