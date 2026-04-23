#!/usr/bin/env python3
# Copyright 2026 (c) o6 Automation GmbH (Author: Andreas Ebner)
"""
Basic OPC UA Server Example
============================

Demonstrates how to create a simple OPC UA server with:
- Variables (int, float, string, bool)
- Object nodes for organization
- A method that clients can call
- Reading and writing values from the server side

Connect to this server with any OPC UA client at:
    opc.tcp://localhost:4840
"""

import time
from o6 import Server
from o6.server import make_argument


def main():
    # Create and start the server on the default port (4840)
    server = Server(port=4840)

    # ── Create an organizational object ──────────────────────────
    plant = server.add_object("Plant", server.objects_node)

    # ── Add variables ────────────────────────────────────────────
    temperature = server.add_variable(
        "Temperature",
        plant,
        22.5,
        nodeid="ns=1;i=1001",
    )
    pressure = server.add_variable(
        "Pressure",
        plant,
        1013.25,
        nodeid="ns=1;i=1002",
    )
    status = server.add_variable(
        "Status",
        plant,
        "idle",
        nodeid="ns=1;i=1003",
    )
    counter = server.add_variable(
        "Counter",
        plant,
        0,
        nodeid="ns=1;i=1004",
    )

    # ── Add a method ─────────────────────────────────────────────
    def add_numbers(a, b):
        """Add two doubles and return the result."""
        print(f"  Method called: {a} + {b} = {a + b}")
        return [a + b]

    server.add_method(
        "Add",
        plant,
        add_numbers,
        input_args=[
            make_argument("A", "i=11", description="First operand"),
            make_argument("B", "i=11", description="Second operand"),
        ],
        output_args=[
            make_argument("Sum", "i=11", description="A + B"),
        ],
        nodeid="ns=1;i=2001",
    )

    # ── Start the server ─────────────────────────────────────────
    server.start()
    print("Server running at opc.tcp://localhost:4840")
    print("Press Ctrl+C to stop.\n")

    try:
        i = 0
        while True:
            # Simulate sensor updates
            i += 1
            temperature.value = 22.5 + (i % 10) * 0.1
            counter.value = i

            if i % 10 == 0:
                print(f"  Counter={i}, Temp={temperature.value:.1f}")

            time.sleep(1.0)
    except KeyboardInterrupt:
        print("\nShutting down…")
    finally:
        server.stop()
        print("Server stopped.")


if __name__ == "__main__":
    main()
