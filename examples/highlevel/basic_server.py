#!/usr/bin/env python3
# Copyright 2026 (c) o6 Automation GmbH
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
# The server is built up by calling ``add_object``/``add_variable``/
# ``add_method`` on a single ``Server`` instance, then started with
# ``server.start()``. The whole script is wrapped in a ``with`` block so
# the server is cleanly stopped on exit.
# END MD

import time
import o6
from o6 import Server
from o6.ns import ns0

# BEGIN MD
# ## 1. Server Setup
# `Server(port=...)` creates the server bound to the given TCP port. The
# `with` statement takes care of starting it on `__enter__` and stopping
# it on `__exit__`, so we never have to call `server.start()` nor
# `server.stop()` manually but we *do* call them explicitly below to
# show the lifecycle.
# END MD


# BEGIN CODE
def main():
    # Create the server bound to the default OPC UA port (4840).
    server = Server(port=4840)
    # END CODE

    # BEGIN MD
    # ## 2. Building the Address Space
    # OPC UA servers expose their data as a tree of *nodes*. The high-level
    # API mirrors that tree directly: `add_object` creates an `ObjectNode`
    # (a folder), `add_variable` creates a `VariableNode` (a leaf with a
    # value), and `add_method` creates a `MethodNode` (a callable).
    #
    # Every node has a parent: usually the server's `objects_node` for
    # top-level entries, or another `ObjectNode` for nested ones. Below we
    # create one `Plant` object and put everything else inside it.
    # END MD

    # BEGIN CODE
    # ── Create an organizational object ──────────────────────────
    plant = server.addObject("Plant", server.objectsNode)
    # END CODE

    # BEGIN MD
    # ## 3. Variables
    # `add_variable(name, parent, value, nodeId=...)` creates a leaf node
    # whose OPC UA data type is *inferred from the Python type of `value`*:
    # `float` → `Double`, `int` → `Int32`, `str` → `String`, `bool` →
    # `Boolean`. The returned `VariableNode` is a live handle: assigning
    # to its `.value` attribute writes to the server, and reading it
    # fetches the current value back.
    #
    # Pinning a `nodeid` is optional but recommended for stable addresses
    # that clients can hard-code. Without it, the server allocates a
    # numeric id itself.
    # END MD

    # BEGIN CODE
    # ── Add variables of different types ─────────────────────────
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
    # END CODE

    # BEGIN MD
    # ## 4. Callable Method
    # `add_method(name, parent, callback, inputArgs=..., outputArgs=...)`
    # exposes a Python function. The argument
    # descriptors are built directly with `ns0.datatypes.Argument(...)` —
    # `data_type` is the OPC UA NodeId of the type (`i=11` is `Double`).
    #
    # The callback receives positional inputs and returns status plus outputs.
    # END MD

    # BEGIN CODE
    # ── Add a method ─────────────────────────────────────────────
    def add_numbers(node, a, b):
        """Add two doubles and return the result."""
        result = a + b
        print(f"  Method called: {a} + {b} = {result}")
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
    # Assigning to a `VariableNode.value` from the server side is exactly
    # the same operation a client would perform with `client.write(...)`:
    # the value is published to the address space, and any client with an
    # active `Subscription` on that node receives a
    # data-change notification.
    # END MD

    # BEGIN CODE
    # ── Start the server ─────────────────────────────────────────
    server.start()
    print("Server running at opc.tcp://localhost:4840")
    print("Press Ctrl+C to stop.\n")

    try:
        i = 0
        while True:
            # Simulate sensor updates — these writes are visible to
            # any subscribed client in real time.
            i += 1
            temperature.value = 22.5 + (i % 10) * 0.1
            pressure.value = 1013.25 + (i % 5) * 0.05
            counter.value = i
            running.value = (i % 20) < 10  # toggle every 10 ticks

            if i % 10 == 0:
                print(
                    f"  Counter={i}, " f"Temp={temperature.value:.1f}, " f"Running={running.value}"
                )

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
        print("\nShutting down…")
    finally:
        server.stop()
        print("Server stopped.")


if __name__ == "__main__":
    main()
# END CODE
