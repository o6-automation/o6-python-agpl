#!/usr/bin/env python3
# Copyright 2026 (c) o6 Automation GmbH (Author: Andreas Ebner)
"""
Server Tutorial: Adding Objects and Type Hierarchy
===================================================

Demonstrates how to organise the address space with object nodes
and how to define custom object types and variable types.

Topics covered:
- Creating object nodes for grouping
- Nested object hierarchies
- Defining custom ObjectTypes
- Defining custom VariableTypes
- References between nodes

Connect with any OPC UA client at: opc.tcp://localhost:4840
"""

import time
from o6 import Server


def main():
    server = Server(port=4840)

    # ── 1. Simple object hierarchy ───────────────────────────────
    #
    #   Objects/
    #     └─ Plant/
    #          ├─ Oven/
    #          │    ├─ Temperature  (Double)
    #          │    └─ HeaterOn     (Boolean)
    #          └─ Conveyor/
    #               ├─ Speed       (Double)
    #               └─ IsRunning   (Boolean)
    #
    plant = server.add_object("Plant", server.objects_node, nodeid="ns=1;i=100")

    oven = server.add_object("Oven", plant, nodeid="ns=1;i=110")
    oven_temp = server.add_variable("Temperature", oven, 180.0, nodeid="ns=1;i=111")
    oven_heater = server.add_variable("HeaterOn", oven, True, nodeid="ns=1;i=112")

    conveyor = server.add_object("Conveyor", plant, nodeid="ns=1;i=120")
    conveyor_speed = server.add_variable("Speed", conveyor, 1.5, nodeid="ns=1;i=121")
    conveyor_running = server.add_variable(
        "IsRunning", conveyor, False, nodeid="ns=1;i=122"
    )

    # ── 2. Custom object‑type definition ─────────────────────────
    #
    #   Define a "SensorType" as a reusable template.
    #
    sensor_type = server.add_object_type(
        "SensorType",
        nodeid="ns=1;i=200",
    )
    # Add a variable child to the type (serves as template)
    server.add_variable("Value", sensor_type, 0.0, nodeid="ns=1;i=201")
    server.add_variable("Unit", sensor_type, "", nodeid="ns=1;i=202", writable=False)

    # Instantiate the type: two sensors under Oven
    humidity_sensor = server.add_object(
        "HumiditySensor",
        oven,
        nodeid="ns=1;i=130",
        type_definition=sensor_type.nodeid,
    )
    server.add_variable("Value", humidity_sensor, 45.0, nodeid="ns=1;i=131")
    server.add_variable(
        "Unit", humidity_sensor, "%RH", nodeid="ns=1;i=132", writable=False
    )

    # ── 3. Custom variable type ──────────────────────────────────
    temperature_type = server.add_variable_type(
        "TemperatureType",
        data_type="i=11",  # Double
        nodeid="ns=1;i=300",
    )

    # ── Start the server ─────────────────────────────────────────
    server.start()
    print("Server running at opc.tcp://localhost:4840")
    print("Press Ctrl+C to stop.\n")
    print("Address space outline:")
    print("  Objects/")
    print("    └─ Plant/")
    print("         ├─ Oven/  (Temperature, HeaterOn, HumiditySensor)")
    print("         └─ Conveyor/  (Speed, IsRunning)")
    print()

    try:
        cycle = 0
        while True:
            cycle += 1
            # Simulate values
            oven_temp.value = 180.0 + (cycle % 20) * 0.5
            conveyor_speed.value = 1.5 + (cycle % 10) * 0.1
            conveyor_running.value = cycle % 15 != 0

            if cycle % 10 == 0:
                print(
                    f"  Cycle {cycle}: "
                    f"OvenTemp={oven_temp.value:.1f}°C, "
                    f"ConvSpeed={conveyor_speed.value:.1f}m/s"
                )

            time.sleep(1.0)

    except KeyboardInterrupt:
        print("\nShutting down…")
    finally:
        server.stop()
        print("Server stopped.")


if __name__ == "__main__":
    main()
