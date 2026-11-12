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

Adds scalar variables of different data types under the Objects
folder, makes one of them read-only, and updates the values from a
server-side simulation loop.

Run any OPC UA client (for example ``C02_firststeps.py`` or
``C12_browser.py``) against this server to read the values and write
the writable ones.
"""

import os

import socket
import time
from o6 import Server

EXAMPLE_PORT = int(os.environ.get("O6_EXAMPLE_PORT", "4840"))
EXAMPLE_ENDPOINT = f"opc.tcp://localhost:{EXAMPLE_PORT}"

# BEGIN MD
# `Server.addVariable()` adds a scalar Variable to the address space. The
# Python type of the initial value sets the OPC UA data type: ``float`` →
# Double, ``int`` → Int32, ``str`` → String, ``bool`` → Boolean. Pass an
# explicit ``nodeId`` to keep NodeIds stable across runs, so client
# examples can use them.
# END MD


def main():
    localhost = "localhost"
    endpoint_url = EXAMPLE_ENDPOINT

    server = Server(port=EXAMPLE_PORT)

    # BEGIN MD
    # ## 1. Scalar variables
    # Four scalar types: Double, Int32, String and Boolean. Each is added
    # under the Objects folder with a fixed NodeId in namespace 1.
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
    # `writable=False` clears the write bit in the access level. Clients can
    # read the value; the server rejects writes with `Bad_NotWritable`. Use
    # it for values that come from firmware or hardware.
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
    # `server.start()` starts networking in the background. The simulation
    # loop assigns new values to the Variable handles once per second.
    # Subscribed clients see each change.
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
