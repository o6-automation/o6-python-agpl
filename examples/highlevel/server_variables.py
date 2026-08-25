#!/usr/bin/env python3
# Copyright 2026 (c) o6 Automation GmbH (Author: Andreas Ebner)
"""
Server Tutorial: Variables
==========================

Demonstrates how to add scalar variables of different data types
under the Objects folder, mark one of them read-only, and update
their values from a server-side simulation loop.

Start any OPC UA client (e.g. ``client_basic.py`` or
``opcua_browser.py``) against this server to read and (for the
writable variables) write the values.
"""

import socket
import time
from o6 import Server

# BEGIN MD
# `Server.addVariable()` adds a scalar Variable to the address
# space. The Python type of the initial value decides the OPC UA
# data type: ``float`` → Double, ``int`` → Int32, ``str`` → String,
# ``bool`` → Boolean. Pass an explicit ``nodeid`` to keep ids
# stable across runs so client examples can reference them.
# END MD


def main():
    localhost = "localhost"
    endpoint_url = f"opc.tcp://{localhost}:4840"

    server = Server(port=4840)

    # BEGIN MD
    # ## 1. Scalar variables
    # Four common scalar types side by side: Double, Int32, String
    # and Boolean. Each is added directly under the Objects folder
    # with a fixed NodeId in namespace 1.
    # END MD

    # BEGIN CODE
    temperature = server.addVariable(
        "Temperature",
        server.objectsNode,
        22.5,
        nodeId="ns=1;i=1001",
    )

    pressure = server.addVariable(
        "Pressure",
        server.objectsNode,
        1013,  # int → OPC UA Int32
        nodeId="ns=1;i=1002",
    )

    machine_name = server.addVariable(
        "MachineName",
        server.objectsNode,
        "CNC-Mill-01",
        nodeId="ns=1;i=1003",
    )

    is_running = server.addVariable(
        "IsRunning",
        server.objectsNode,
        False,
        nodeId="ns=1;i=1004",
    )
    # END CODE

    # BEGIN MD
    # ## 2. Read-only variable
    # `writable=False` clears the write bit in the access level so
    # clients can read the value but any write request is rejected
    # by the server with `Bad_NotWritable`. It can be useful for values that
    # come from firmware/hardware and must not be modified.
    # END MD

    # BEGIN CODE
    firmware_version = server.addVariable(
        "FirmwareVersion",
        server.objectsNode,
        "v2.1.0",
        nodeId="ns=1;i=1005",
        writable=False,
    )
    # END CODE

    # BEGIN MD
    # ## 3. Run and update loop
    # `server.start()` blocks until `server.stop()`. The
    # simulation loop assigns new values to the Variable handles
    # once per second; any subscribed client sees the changes
    # immediately.
    # END MD

    # BEGIN CODE
    server.start()
    print(f"Server running at {endpoint_url}")
    print("Press Ctrl+C to stop.\n")

    try:
        cycle = 0
        while True:
            cycle += 1
            temperature.value = 22.5 + (cycle % 50) * 0.1
            pressure.value = 1013.25 + (cycle % 20) * 0.5
            is_running.value = cycle % 30 != 0

            if cycle % 10 == 0:
                print(
                    f"  Cycle {cycle}: "
                    f"Temp={temperature.value:.1f}°C, "
                    f"Pressure={pressure.value:.1f}hPa, "
                    f"Running={is_running.value}"
                )

            time.sleep(1.0)

    except KeyboardInterrupt:
        print("\nShutting down…")
    finally:
        server.stop()
        print("Server stopped.")


if __name__ == "__main__":
    main()
    # END CODE
