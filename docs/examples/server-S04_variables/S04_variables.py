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



def main():
    localhost = "localhost"
    endpoint_url = EXAMPLE_ENDPOINT

    server = Server(port=EXAMPLE_PORT)


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


    print()
    print("--- 2. Read-Only Variable ---")

    firmware_version = server.addVariable(
        "FirmwareVersion",
        server.objectsNode,
        "v2.1.0",
        nodeId="ns=1;i=1005",
        writable=False,
    )


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