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
Basic OPC UA Server
===========================

Demonstrates how to create a simple OPC UA server with:

- Variables of different types (int, float, string, bool)
- Object nodes for organizing the address space
- A method that clients can call
- Server-side updates that subscribed clients receive in real time

Connect to this server with any OPC UA client at:

    opc.tcp://localhost:4840
"""

# BEGIN MD
# Every line of this example goes through the high-level ``o6.Server`` API.
# The server is built up by calling ``addObject``/``addVariable``/
# ``addMethod`` on a single ``Server`` instance, then started with
# ``server.start()``. A ``try``/``finally`` block guarantees ``server.stop()``
# runs on exit, including on Ctrl+C.
# END MD

import os

import time
import o6
from o6 import Server
from o6.ns import ns0

EXAMPLE_PORT = int(os.environ.get("O6_EXAMPLE_PORT", "4840"))

# BEGIN MD
# ## 1. Server Setup
# `Server(port=...)` creates the server bound to the given TCP port.
# Nothing runs yet — `server.start()` opens the listening socket and
# `server.stop()` closes it, wrapped in `try`/`finally` below so the
# server always stops cleanly, including on Ctrl+C.
# END MD


# BEGIN CODE
def main():
    print("--- 1. Server Setup ---")

    # Create the server bound to the default OPC UA port (4840).
    server = Server(port=EXAMPLE_PORT)
    # END CODE

    # BEGIN MD
    # ## 2. Building the Address Space
    # OPC UA servers expose their data as a tree of *nodes*. The high-level
    # API mirrors that tree directly: `addObject` creates an `ObjectNode`
    # (a folder), `addVariable` creates a `VariableNode` (a leaf with a
    # value), and `addMethod` creates a `MethodNode` (a callable).
    #
    # Every node has a parent: usually the server's `objects` folder handle for
    # top-level entries, or another `ObjectNode` for nested ones. Below we
    # create one `Plant` object and put everything else inside it.
    # END MD

    # BEGIN CODE
    print()
    print("--- 2. Building the Address Space ---")

    plant = server.addObject("Plant", server.objects)
    # END CODE

    # BEGIN MD
    # ## 3. Variables
    # `addVariable(name, parent, value, nodeId=...)` creates a leaf node
    # whose OPC UA data type is *inferred from the Python type of `value`*:
    # `float` → `Double`, `int` → `Int32`, `str` → `String`, `bool` →
    # `Boolean`. The returned `VariableNode` is a live handle: calling it
    # with an argument (`node(23.5)`) writes to the server, and calling it
    # with none (`node()`) reads the current value back.
    #
    # Pinning a `nodeId` is optional but recommended for stable addresses
    # that clients can hard-code. Without it, the server allocates a
    # numeric id itself.
    # END MD

    # BEGIN CODE
    print()
    print("--- 3. Variables ---")

    temperature = server.addVariable(
        "Temperature",
        plant,
        22.5,  # float → OPC UA Double
        nodeId="ns=1;i=1001",
    )
    pressure = server.addVariable(
        "Pressure",
        plant,
        1013.25,  # float → OPC UA Double
        nodeId="ns=1;i=1002",
    )
    status = server.addVariable(
        "Status",
        plant,
        "idle",  # str → OPC UA String
        nodeId="ns=1;i=1003",
    )
    counter = server.addVariable(
        "Counter",
        plant,
        0,  # int → OPC UA Int32
        nodeId="ns=1;i=1004",
    )
    running = server.addVariable(
        "Running",
        plant,
        False,  # bool → OPC UA Boolean
        nodeId="ns=1;i=1005",
    )
    assert server["ns=1;i=1001"] is temperature
    assert server.objects.plant.temperature is temperature
    # END CODE

    # BEGIN MD
    # ## 4. Callable Method
    # `addMethod(name, parent, callback, inputArgs=..., outputArgs=...)`
    # exposes a Python function. The argument
    # descriptors are built directly with `ns0.datatypes.Argument(...)` —
    # `dataType` is the OPC UA NodeId of the type (`i=11` is `Double`).
    #
    # The callback receives positional inputs and returns status plus outputs.
    # END MD

    # BEGIN CODE
    print()
    print("--- 4. Callable Method ---")

    def add_numbers(node, a, b):
        """Add two doubles and return the result."""
        result = a + b
        print(f"Add({a}, {b}) = {result}")
        return (o6.StatusCode.GOOD, result)

    server.addMethod(
        "Add",
        plant,
        add_numbers,
        inputArgs=[
            ns0.datatypes.Argument(
                name="A",
                dataType=o6.Double,
                valueRank=o6.ValueRank.SCALAR,
                description="First operand",
            ),
            ns0.datatypes.Argument(
                name="B",
                dataType=o6.Double,
                valueRank=o6.ValueRank.SCALAR,
                description="Second operand",
            ),
        ],
        outputArgs=[
            ns0.datatypes.Argument(
                name="Sum", dataType=o6.Double, valueRank=o6.ValueRank.SCALAR, description="A + B"
            ),
        ],
        nodeId="ns=1;i=2001",
    )
    # END CODE

    # BEGIN MD
    # ## 5. Server-Side Updates
    # Once `server.start()` is called, the server runs in its own thread
    # and accepts client connections. The main thread is free to do
    # anything; for instance driving a simulation loop that updates the
    # variables over time.
    #
    # Calling a `VariableNode` with a value from the server side is
    # exactly the same operation a client would perform with
    # `client.write(...)`: the value is published to the address space,
    # and any client with an active `Subscription` on that node receives
    # a data-change notification.
    # END MD

    # BEGIN CODE
    print()
    print("--- 5. Server-Side Updates ---")

    server.start()
    print(f"Server running at opc.tcp://localhost:{EXAMPLE_PORT}")
    print("Press Ctrl+C to stop.")

    try:
        i = 0
        while True:
            # Simulate sensor updates — these writes are visible to
            # any subscribed client in real time.
            i += 1
            temperature(22.5 + (i % 10) * 0.1)
            pressure(1013.25 + (i % 5) * 0.05)
            counter(i)
            running((i % 20) < 10)  # toggle every 10 ticks

            if i % 10 == 0:
                print(f"Counter = {i}, Temp = {temperature():.1f}, Running = {running()}")

            time.sleep(1.0)
    # END CODE

    # BEGIN MD
    # ## 6. Lifecycle
    # `KeyboardInterrupt` (Ctrl+C) breaks out of the simulation loop. The
    # `finally` block calls `server.stop()` so the listening socket is
    # closed and the worker thread is joined. Without it, the process
    # would hang on exit.
    # END MD

    # BEGIN CODE
    except KeyboardInterrupt:
        print("Shutting down...")
    finally:
        server.stop()
        print("Server stopped.")


if __name__ == "__main__":
    main()
# END CODE
