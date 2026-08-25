#!/usr/bin/env python3
# Copyright 2026 (c) o6 Automation GmbH
"""
Sorting Line Example - Step 1: The Server
=========================================
This tutorial demonstrates a complete OPC UA ecosystem using ``o6``.
It covers three distinct aspects of an industrial architecture:

1. **The Server**: It defines the data structure (nodes and Object Types).
2. **The Controller**: The automated logic loop (Machine-to-Machine OPC UA Client).
3. **The HMI Client**: Manual monitoring and control (Human-to-Machine) via an interactive interface.

![Sorting Line Simulation](../assets/vc_sortingline_screenshot.png)

The first step in creating our sorting line on Visual Components is to deploy an OPC UA Server.
This server acts as the central "Data Hub". It contains no automation
logic; it simply stores the physical state of the machine.

Visual Components (the 3D simulation) will connect to it to read
motor commands and write sensor states.
"""

# BEGIN MD
# ## Prerequisites
# To fully experience this digital twin alongside the 3D physics simulation, you need:

# - **Visual Components** software installed.
# - The specific custom **Sorting Line layout** (`.vcmx` file) loaded.
# - Visual Components' OPC UA Connectivity plugin configured as a **Client** connecting to `opc.tcp://localhost:4840`.
# - Proper **variable mapping** established in Visual Components (ensure the `Simulation to Server` and `Server to Simulation` variable groups are correctly paired with the corresponding server NodeIDs).
# END MD

# BEGIN MD
# ## 1. Defining Types
# We use OPC UA `ObjectTypes` to create reusable models.
# For instance, a `ConveyorType` is created
# with two properties: `Speed` and `IsRunning`.
# END MD

# BEGIN CODE
import time
from o6 import Server


def run_digital_twin_server():
    print("[SERVER] Starting Digital Twin OPC UA Server...")
    with Server(port=4840) as server:

        # ── Type Definitions ──────────────────────────────
        conveyor_type = server.addObjectType("ConveyorType", nodeId="ns=1;i=200")
        server.addVariable("Speed", conveyor_type, 0.0, nodeId="ns=1;i=201")
        server.addVariable("IsRunning", conveyor_type, False, nodeId="ns=1;i=202")

        color_sensor_type = server.addObjectType("ColorSensorType", nodeId="ns=1;i=210")
        server.addVariable("ProductColor", color_sensor_type, 0, nodeId="ns=1;i=211")

        joint_type = server.addObjectType("JointType", nodeId="ns=1;i=220")
        server.addVariable("Value", joint_type, 0.0, nodeId="ns=1;i=221")
        # END CODE

        # BEGIN MD
        # ## 2. Node Instantiation
        # Once templates are defined, we use `server.addObject()` and `server.addVariable()` to instantiate
        # our real-world objects and their properties in the server's address space.
        # END MD

        # BEGIN CODE
        plant = server.addObject("Plant", server.objectsNode, nodeId="ns=1;i=100")

        # ── Output Conveyors ─────────────────────────────
        red_conveyor = server.addObject(
            "RedConveyor", plant, nodeId="ns=1;i=140", typeDefinition=conveyor_type.nodeId
        )
        server.addVariable("Speed", red_conveyor, 200.0, nodeId="ns=1;i=141")
        server.addVariable("IsRunning", red_conveyor, True, nodeId="ns=1;i=142")

        blue_conveyor = server.addObject(
            "BlueConveyor", plant, nodeId="ns=1;i=150", typeDefinition=conveyor_type.nodeId
        )
        server.addVariable("Speed", blue_conveyor, 200.0, nodeId="ns=1;i=151")
        server.addVariable("IsRunning", blue_conveyor, True, nodeId="ns=1;i=152")

        # ── Input Conveyor & Sensors ──────────────────────
        input_conveyor = server.addObject(
            "InputConveyor", plant, nodeId="ns=1;i=110", typeDefinition=conveyor_type.nodeId
        )
        server.addVariable("Speed", input_conveyor, 200.0, nodeId="ns=1;i=111")
        server.addVariable("IsRunning", input_conveyor, True, nodeId="ns=1;i=112")

        color_sensor = server.addObject(
            "ColorSensor",
            input_conveyor,
            nodeId="ns=1;i=113",
            typeDefinition=color_sensor_type.nodeId,
        )
        server.addVariable("ProductColor", color_sensor, 0, nodeId="ns=1;i=114")

        # ── Sorting Robot and Joints ─────────────────────────────────
        sorting_robot = server.addObject("SortingRobot", plant, nodeId="ns=1;i=130")
        server.addVariable("State", sorting_robot, "Idle", nodeId="ns=1;i=131")
        server.addVariable("SortRed", sorting_robot, False, nodeId="ns=1;i=132")
        server.addVariable("SortBlue", sorting_robot, False, nodeId="ns=1;i=133")

        # Command (Cmd) / Feedback (Fb) architecture to prevent infinite loops
        for i, node_base in enumerate([134, 135, 136, 137, 138, 139], start=1):
            joint = server.addObject(
                f"J{i}",
                sorting_robot,
                nodeId=f"ns=1;i={node_base}",
                typeDefinition=joint_type.nodeId,
            )
            server.addVariable(
                f"J{i}_Value_FB", joint, 90.0 if i == 3 else 0.0, nodeId=f"ns=1;i={node_base+30}"
            )
            server.addVariable(f"J{i}_Value_CMD", joint, 0.0, nodeId=f"ns=1;i={node_base+40}")
        # END CODE

        # BEGIN MD
        # ## 3. Server Execution
        # The server is started and kept alive using a while True loop.
        # END MD

        # BEGIN CODE
        server.start()
        print("[SERVER] OPC UA Server online at opc.tcp://localhost:4840")
        print("[SERVER] Keep this terminal open and launch the Controller in another terminal.\n")

        try:
            while True:
                time.sleep(1.0)
        except KeyboardInterrupt:
            print("\n[SERVER] Shutdown requested...")
        finally:
            server.stop()
            print("[SERVER] Server stopped.")


if __name__ == "__main__":
    run_digital_twin_server()
# END CODE
