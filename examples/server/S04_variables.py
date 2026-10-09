#!/usr/bin/env python3
# Copyright 2026 (c) o6 Automation GmbH (Author: Andreas Ebner)
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
Server Tutorial: Variables
==========================

Demonstrates how to add scalar variables of different data types
under the Objects folder, mark one of them read-only, and update
their values from a server-side simulation loop.

Start any OPC UA client (e.g. ``C02_firststeps.py`` or
``C12_browser.py``) against this server to read and (for the
writable variables) write the values.
"""

import os

import socket
import time
from o6 import Server

EXAMPLE_PORT = int(os.environ.get("O6_EXAMPLE_PORT", "4840"))
EXAMPLE_ENDPOINT = f"opc.tcp://localhost:{EXAMPLE_PORT}"

# BEGIN MD
# `Server.addVariable()` adds a scalar Variable to the address
# space. The Python type of the initial value decides the OPC UA
# data type: ``float`` → Double, ``int`` → Int32, ``str`` → String,
# ``bool`` → Boolean. Pass an explicit ``nodeid`` to keep ids
# stable across runs so client examples can reference them.
# END MD


def main():
    localhost = "localhost"
    endpoint_url = EXAMPLE_ENDPOINT

    server = Server(port=EXAMPLE_PORT)

    # BEGIN MD
    # ## 1. Scalar variables
    # Four common scalar types side by side: Double, Int32, String
    # and Boolean. Each is added directly under the Objects folder
    # with a fixed NodeId in namespace 1.
    # END MD

    # BEGIN CODE
    print("--- 1. Scalar Variables ---")

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
    print()
    print("--- 2. Read-Only Variable ---")

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
    # `server.start()` starts networking in the background. The
    # simulation loop assigns new values to the Variable handles
    # once per second; any subscribed client sees the changes
    # immediately.
    # END MD

    # BEGIN CODE
    print()
    print("--- 3. Run and Update Loop ---")

    server.start()
    print(f"Server running at {endpoint_url}")
    print("Press Ctrl+C to stop.")

    try:
        cycle = 0
        while True:
            cycle += 1
            temperature(22.5 + (cycle % 50) * 0.1)
            pressure(1013 + cycle % 20)
            is_running(cycle % 30 != 0)

            if cycle % 10 == 0:
                print(
                    f"Cycle {cycle}: Temp = {temperature():.1f}°C, "
                    f"Pressure = {pressure():.1f}hPa, Running = {is_running()}"
                )

            time.sleep(1.0)

    except KeyboardInterrupt:
        print("Shutting down...")
    finally:
        server.stop()
        print("Server stopped.")


if __name__ == "__main__":
    main()
    # END CODE
