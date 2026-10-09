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
Server Tutorial: Objects and Type Hierarchy
===========================================

Demonstrates how to organise a server's address space with object
nodes, define a custom ``ObjectType`` as a reusable template, and
declare a custom ``VariableType``. The result is a small "Plant"
hierarchy with two child devices and one sensor instantiated from
the custom type.

Start any OPC UA client (e.g. ``C02_firststeps.py`` or
``C03_browsing.py``) against this server to see the hierarchy.
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


    print("--- 1. Object Hierarchy ---")

    plant = server.addObject(name="Plant", parent=server.objectsNode, nodeId="ns=1;i=100")

    oven = server.addObject("Oven", plant, nodeId="ns=1;i=110")
    oven_temp = server.addVariable("Temperature", oven, 180.0, nodeId="ns=1;i=111")
    oven_heater = server.addVariable("HeaterOn", oven, True, nodeId="ns=1;i=112")

    conveyor = server.addObject("Conveyor", plant, nodeId="ns=1;i=120")
    conveyor_speed = server.addVariable("Speed", conveyor, 1.5, nodeId="ns=1;i=121")
    conveyor_running = server.addVariable("IsRunning", conveyor, False, nodeId="ns=1;i=122")


    print()
    print("--- 2. Custom ObjectType ---")

    sensor_type = server.addObjectType("SensorType", nodeId="ns=1;i=200")
    server.addVariable("Value", sensor_type, 0.0, nodeId="ns=1;i=201")
    server.addVariable("Unit", sensor_type, "", nodeId="ns=1;i=202", writable=False)

    humidity_sensor = server.addObject(
        "HumiditySensor",
        oven,
        nodeId="ns=1;i=130",
        typeDefinition=sensor_type,
    )
    server.addVariable("Value", humidity_sensor, 45.0, nodeId="ns=1;i=131")
    server.addVariable("Unit", humidity_sensor, "%RH", nodeId="ns=1;i=132", writable=False)


    print()
    print("--- 3. Custom VariableType ---")

    server.addVariableType(
        "TemperatureType",
        dataType="i=11",  # Double
        nodeId="ns=1;i=300",
    )


    print()
    print("--- 4. Run and Simulation Loop ---")

    server.start()
    print(f"Server running at {endpoint_url}")
    print("Press Ctrl+C to stop.")

    try:
        cycle = 0
        while True:
            cycle += 1
            oven_temp(180.0 + (cycle % 20) * 0.5)
            conveyor_speed(1.5 + (cycle % 10) * 0.1)
            conveyor_running(cycle % 15 != 0)

            if cycle % 10 == 0:
                print(
                    f"Cycle {cycle}: OvenTemp = {oven_temp():.1f}°C, "
                    f"ConvSpeed = {conveyor_speed():.1f}m/s"
                )

            time.sleep(1.0)

    except KeyboardInterrupt:
        print("Shutting down...")
    finally:
        server.stop()
        print("Server stopped.")


if __name__ == "__main__":
    main()