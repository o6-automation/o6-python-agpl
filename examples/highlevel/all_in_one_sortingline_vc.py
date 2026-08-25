#!/usr/bin/env python3
# Copyright 2026 (c) o6 Automation GmbH
"""
Sorting Line Example - All in one: Server, Controller, and HMI Client
=====================================================================
This tutorial demonstrates a complete OPC UA ecosystem using ``o6``.
It covers three distinct aspects of an industrial architecture:

1. **The Server**: It defines the data structure (nodes and Object Types).
2. **The Controller**: The automated logic loop (Machine-to-Machine OPC UA Client).
3. **The HMI Client**: Manual monitoring and control (Human-to-Machine) via an interactive interface.

![Sorting Line Simulation](../assets/vc_sortingline_screenshot.png)
"""

# BEGIN MD
# ## Prerequisites
# To fully experience this digital twin alongside the 3D physics simulation, you need:
# - **Visual Components** software installed.
# - The specific custom **Sorting Line layout** (`.vcmx` file) loaded.
# - Visual Components' OPC UA Connectivity plugin configured as a **Client** connecting to `opc.tcp://localhost:4840`.
# - Proper **variable mapping** established in Visual Components (ensure the `Simulation to Server` and `Server to Simulation` variable groups are correctly paired with the corresponding server NodeIDs).
#
# ## 1. The Server (Digital Data Hub)
# In this architecture, the Python script hosts the OPC UA Server. It acts as the central data hub.
# Visual Components acts as an OPC UA *Client* that connects to this Python
# server to read motor commands and write sensor feedback.
# END MD

import time
import threading
from o6 import Server, Client, StatusCodeError

endpoint_url = "opc.tcp://localhost:4840"
system_running = True

# BEGIN MD
# ### 1.1 Object Types
# Instead of redefining variables for each conveyor, we create a `ConveyorType`
# containing `Speed` and `IsRunning` properties. This ensures a scalable and clean architecture.
# END MD


def run_digital_twin_server():
    """Simulates the physical Digital Twin and OPC UA Server."""
    print("[SERVER] Starting Digital Twin OPC UA Server...")
    with Server(port=4840) as server:
        # BEGIN CODE
        # ── Type Definitions ──────────────────────────────
        # Template for standard conveyors
        conveyor_type = server.addObjectType("ConveyorType", nodeId="ns=1;i=200")
        server.addVariable("Speed", conveyor_type, 0.0, nodeId="ns=1;i=201")
        server.addVariable("IsRunning", conveyor_type, False, nodeId="ns=1;i=202")

        # Template for the color selection sensor
        color_sensor_type = server.addObjectType("ColorSensorType", nodeId="ns=1;i=210")
        server.addVariable("ProductColor", color_sensor_type, 0, nodeId="ns=1;i=211")

        # Template for the robot joints
        joint_type = server.addObjectType("JointType", nodeId="ns=1;i=220")
        server.addVariable("Value", joint_type, 0.0, nodeId="ns=1;i=221")
        # END CODE

        # BEGIN MD
        # ### 1.2 Node Instantiation
        # Once the templates are defined, we use `server.addObject()` and `server.addVariable()`to instantiate
        # our real-world objects and their properties in the server's address space.
        # END MD

        # BEGIN CODE
        # ── Create the Plant Object ────────────────────────────
        plant = server.addObject("Plant", server.objectsNode, nodeId="ns=1;i=100")

        # ── Instantiate Output Conveyors ─────────────────────────────
        red_conveyor = server.addObject(
            "RedConveyor", plant, nodeId="ns=1;i=140", typeDefinition=conveyor_type.nodeId
        )
        red_speed = server.addVariable("Speed", red_conveyor, 200.0, nodeId="ns=1;i=141")
        red_running = server.addVariable("IsRunning", red_conveyor, True, nodeId="ns=1;i=142")

        blue_conveyor = server.addObject(
            "BlueConveyor", plant, nodeId="ns=1;i=150", typeDefinition=conveyor_type.nodeId
        )
        blue_speed = server.addVariable("Speed", blue_conveyor, 200.0, nodeId="ns=1;i=151")
        blue_running = server.addVariable("IsRunning", blue_conveyor, True, nodeId="ns=1;i=152")

        # ── Instantiate Input Conveyor & Sensors ──────────────────────
        input_conveyor = server.addObject(
            "InputConveyor", plant, nodeId="ns=1;i=110", typeDefinition=conveyor_type.nodeId
        )
        input_speed = server.addVariable("Speed", input_conveyor, 200.0, nodeId="ns=1;i=111")
        input_running = server.addVariable("IsRunning", input_conveyor, True, nodeId="ns=1;i=112")

        color_sensor = server.addObject(
            "ColorSensor",
            input_conveyor,
            nodeId="ns=1;i=113",
            typeDefinition=color_sensor_type.nodeId,
        )
        color_sensor_value = server.addVariable(
            "ProductColor", color_sensor, 0, nodeId="ns=1;i=114"
        )

        # ── Instantiate Sorting Robot and its joints ─────────────────────────────────
        sorting_robot = server.addObject("SortingRobot", plant, nodeId="ns=1;i=130")
        robot_state = server.addVariable("State", sorting_robot, "Idle", nodeId="ns=1;i=131")
        sort_red = server.addVariable("SortRed", sorting_robot, False, nodeId="ns=1;i=132")
        sort_blue = server.addVariable("SortBlue", sorting_robot, False, nodeId="ns=1;i=133")

        # Example for Joint 1 (Command and Feedback structure)
        joint1 = server.addObject(
            "J1", sorting_robot, nodeId="ns=1;i=134", typeDefinition=joint_type.nodeId
        )
        joint1_value_fb = server.addVariable("J1_Value_FB", joint1, 0.0, nodeId="ns=1;i=164")
        joint1_value_cmd = server.addVariable("J1_Value_CMD", joint1, 0.0, nodeId="ns=1;i=174")

        # Joints 2 to 6...
        joint2 = server.addObject(
            "J2", sorting_robot, nodeId="ns=1;i=135", typeDefinition=joint_type.nodeId
        )
        joint2_value_fb = server.addVariable("J2_Value_FB", joint2, 0.0, nodeId="ns=1;i=165")
        joint2_value_cmd = server.addVariable("J2_Value_CMD", joint2, 0.0, nodeId="ns=1;i=175")

        joint3 = server.addObject(
            "J3", sorting_robot, nodeId="ns=1;i=136", typeDefinition=joint_type.nodeId
        )
        joint3_value_fb = server.addVariable("J3_Value_FB", joint3, 90.0, nodeId="ns=1;i=166")
        joint3_value_cmd = server.addVariable("J3_Value_CMD", joint3, 0.0, nodeId="ns=1;i=176")

        joint4 = server.addObject(
            "J4", sorting_robot, nodeId="ns=1;i=137", typeDefinition=joint_type.nodeId
        )
        joint4_value_fb = server.addVariable("J4_Value_FB", joint4, 0.0, nodeId="ns=1;i=167")
        joint4_value_cmd = server.addVariable("J4_Value_CMD", joint4, 0.0, nodeId="ns=1;i=177")

        joint5 = server.addObject(
            "J5", sorting_robot, nodeId="ns=1;i=138", typeDefinition=joint_type.nodeId
        )
        joint5_value_fb = server.addVariable("J5_Value_FB", joint5, 0.0, nodeId="ns=1;i=168")
        joint5_value_cmd = server.addVariable("J5_Value_CMD", joint5, 0.0, nodeId="ns=1;i=178")

        joint6 = server.addObject(
            "J6", sorting_robot, nodeId="ns=1;i=139", typeDefinition=joint_type.nodeId
        )
        joint6_value_fb = server.addVariable("J6_Value_FB", joint6, 0.0, nodeId="ns=1;i=169")
        joint6_value_cmd = server.addVariable("J6_Value_CMD", joint6, 0.0, nodeId="ns=1;i=179")
        # END CODE

        # BEGIN MD
        # ### 1.3 Server Execution
        # We start the server and keep the thread alive. The variables are automatically
        # exposed and can be read or written by any connected client.
        # END MD

        # BEGIN CODE
        # ── Start the Server ──────────────────────────────────────────
        server.start()
        print("[SERVER] OPC UA Server for Sorting Robot Demo running at opc.tcp://localhost:4840")

        # Keep server alive until shutdown signal
        while system_running:
            time.sleep(1.0)

        server.stop()
        print("[SERVER] Server stopped.")
        # END CODE


# BEGIN MD
# ## 2. The Controller (Automated Logic)
# The controller acts as the "Brain". It connects as an OPC UA Client and processes the logic.
#
# ### 2.1 The Logic Execution
# The `execute_sort_command` function evaluates the current state of the robot.
# If it is ready (`Idle`), it uses `client.write()` to send an electrical pulse to the
# simulation, triggering the appropriate sorting animation.
# END MD


# BEGIN CODE
def execute_sort_command(client, current_color):
    """Evaluates the color and triggers the corresponding sorting action."""
    current_robot_state = str(client.read("ns=1;i=131"))

    if current_robot_state == "Idle":
        if current_color == "1":  # 1 = Red
            print("\n[CONTROLLER] Action: Sending command to sort LEFT (Red)")
            client.write("ns=1;i=132", True)
            client.write("ns=1;i=131", "Moving")

            time.sleep(0.2)  # Short pulse
            client.write("ns=1;i=132", False)

            time.sleep(3.8)  # Wait for simulation animation
            client.write("ns=1;i=131", "Idle")
            print("[CONTROLLER] Ready for next part.")

        elif current_color == "4":  # 4 = Blue
            print("\n[CONTROLLER] Action: Sending command to sort RIGHT (Blue)")
            client.write("ns=1;i=133", True)
            client.write("ns=1;i=131", "Moving")

            time.sleep(0.2)  # Short pulse
            client.write("ns=1;i=133", False)

            time.sleep(3.8)  # Wait for simulation animation
            client.write("ns=1;i=131", "Idle")
            print("[CONTROLLER] Ready for next part.")
    else:
        pass  # Robot is busy, skipping order


# END CODE

# BEGIN MD
# ### 2.2 Polling & State Monitoring (REPLACE POLLING WITH SUBSCRIPTION LATER)
# The main controller loop continuously polls the optical color sensor using `client.read()`.
# To prevent flooding the logic, it only triggers an action when the sensor value changes
# compared to the previous cycle.
# END MD


# BEGIN CODE
def run_controller():
    """Main polling loop for the automated controller."""
    time.sleep(1.5)  # Wait for the server to fully start

    try:
        with Client(endpoint_url) as client:
            print("[CONTROLLER] Successfully connected to the OPC UA Server.")
            last_color = "0"

            while system_running:
                try:
                    # Continuous reading of the sensor value node
                    current_color = str(client.read("ns=1;i=114"))

                    # Event triggered on state change
                    if current_color != "0" and current_color != last_color:
                        execute_sort_command(client, current_color)

                    last_color = current_color
                except StatusCodeError:
                    pass

                time.sleep(0.1)  # 100ms polling rate

    except Exception as e:
        print(f"[CONTROLLER] Connection failed: {e}")


# END CODE


# BEGIN MD
# ## 3. The HMI Client (Manual Control & Monitoring)
# An interactive client used by operators to monitor the installation and perform manual overrides.
#
# ### 3.1 Initialization
# The `clientDemo` class encapsulates the OPC UA client setup.
# END MD


class clientDemo:
    # BEGIN CODE
    def __init__(self, endpoint_url="opc.tcp://127.0.0.1:4840"):
        self.endpointUrl = endpoint_url
        self.client = Client(endpoint_url)
        self.connected = False

        # Node Mapping
        self.id_robot_state = "ns=1;i=131"
        self.id_color_sensor = "ns=1;i=114"
        self.id_sort_red = "ns=1;i=132"
        self.id_sort_blue = "ns=1;i=133"
        self.id_inputconveyor_speed = "ns=1;i=111"

        # Joints Command Nodes
        self.id_j1_cmd = "ns=1;i=174"
        self.id_j2_cmd = "ns=1;i=175"
        self.id_j3_cmd = "ns=1;i=176"
        self.id_j4_cmd = "ns=1;i=177"
        self.id_j5_cmd = "ns=1;i=178"
        self.id_j6_cmd = "ns=1;i=179"

        # Joints Feedback Nodes
        self.id_j1_fb = "ns=1;i=164"
        self.id_j2_fb = "ns=1;i=165"
        self.id_j3_fb = "ns=1;i=166"
        self.id_j4_fb = "ns=1;i=167"
        self.id_j5_fb = "ns=1;i=168"
        self.id_j6_fb = "ns=1;i=169"

    def connect(self) -> None:
        try:
            self.client.connect()
            self.connected = True
            print("\n[CLIENT] HMI Successfully connected to the Digital Twin!")
        except Exception as e:
            print(f"[CLIENT] Connection Error: {e}")

    def disconnect(self) -> None:
        if self.connected:
            self.client.disconnect()
            print("[CLIENT] HMI Disconnected from the server.")

    # END CODE

    # BEGIN MD
    # ### 3.2 Basic Node Operations
    # Simple methods are exposed to read states and force overrides using standard
    # `read()` and `write()` functions.
    # END MD

    # BEGIN CODE
    def read_robot_state(self) -> str:
        try:
            return str(self.client.read(self.id_robot_state))
        except StatusCodeError as e:
            return f"Read error: {e}"

    def read_color_sensor(self) -> str:
        try:
            value = str(self.client.read(self.id_color_sensor))
            if value == "1":
                return "Red detected"
            elif value == "4":
                return "Blue detected"
            else:
                return "None/Waiting"
        except StatusCodeError:
            return "Sensor error"

    def force_sort_red(self) -> None:
        print("[CLIENT] -> Sending override command: SORT RED (LEFT)")
        try:
            self.client.write(self.id_sort_red, True)
            time.sleep(0.2)
            self.client.write(self.id_sort_red, False)
        except StatusCodeError as e:
            pass

    def set_conveyor_speed(self, speed_value: float) -> None:
        try:
            self.client.write(self.id_inputconveyor_speed, float(speed_value))
            print(f"[CLIENT] Conveyor speed successfully set to {float(speed_value)}")
        except Exception as e:
            print(f"[CLIENT] Failed to set speed: {e}")

    # END CODE

    # BEGIN MD
    # ### 3.3 Trajectory Interpolation
    # To perform realistic movements in Visual Components, we read the current physical position from the Feedback nodes
    # (`_fb`), calculate a linear trajectory, and incrementally write the steps to the Command nodes (`_cmd`).
    # END MD

    # BEGIN CODE
    def read_joints(self) -> list[float]:
        """Reads the current joint values from the robot."""
        try:
            return [
                float(self.client.read(self.id_j1_fb)),
                float(self.client.read(self.id_j2_fb)),
                float(self.client.read(self.id_j3_fb)),
                float(self.client.read(self.id_j4_fb)),
                float(self.client.read(self.id_j5_fb)),
                float(self.client.read(self.id_j6_fb)),
            ]
        except Exception:
            return ["Error"] * 6

    def move_joints_smoothly(
        self, target_angles: list[float], steps: int = 50, duration: float = 2.0
    ) -> None:
        print(f"[CLIENT] -> Calculating smooth trajectory over {duration}s...")
        current_angles = self.read_joints()

        if "Error" in current_angles:
            return

        cmd_nodes = [
            self.id_j1_cmd,
            self.id_j2_cmd,
            self.id_j3_cmd,
            self.id_j4_cmd,
            self.id_j5_cmd,
            self.id_j6_cmd,
        ]

        sleep_time = duration / steps

        for step in range(1, steps + 1):
            for i in range(6):
                # Linear Interpolation
                interpolated_val = current_angles[i] + (
                    float(target_angles[i]) - current_angles[i]
                ) * (step / steps)
                try:
                    self.client.write(cmd_nodes[i], float(interpolated_val))
                except StatusCodeError:
                    pass
            time.sleep(sleep_time)

        print("[CLIENT] Robot successfully reached target position.")

    # END CODE


# BEGIN MD
# ### 3.4 Interactive Menu REPLACE POLLING WITH SUBSCRIPTION LATER
# A standard CLI loop exposes the HMI functionality to the operator.
# END MD


# BEGIN CODE
def display_menu() -> None:
    print("\n" + "=" * 45)
    print("   CLIENT DEMONSTRATOR - o6 Python   ")
    print("=" * 45)
    print("1. Read current robot state")
    print("2. Read optical sensor value")
    print("3. Manual override: Sort LEFT (Red)")
    print("5. Set Input Conveyor Speed")
    print("6. Set Robot Joints (Interpolated)")
    print("7. Live monitoring")
    print("0. Quit")
    print("=" * 45)


def run_hmi_client():
    my_robot = clientDemo()
    time.sleep(2)
    my_robot.connect()
    if not my_robot.connected:
        return

    try:
        while system_running:
            display_menu()
            choice = input("Choose an action (0-7): ")

            if choice == "1":
                print(f"\n[RESULT] Robotic arm state: {my_robot.read_robot_state()}")
            elif choice == "2":
                print(f"\n[RESULT] Entry sensor: {my_robot.read_color_sensor()}")
            elif choice == "3":
                if my_robot.read_robot_state() == "Idle":
                    my_robot.force_sort_red()
            elif choice == "5":
                val = input("Enter new input conveyor speed (Double): ")
                my_robot.set_conveyor_speed(val)
            elif choice == "6":
                print("\nEnter joint values in degrees:")
                j1 = input("J1 (Base rotation)   : ") or "0.0"
                j2 = input("J2 (Shoulder)        : ") or "0.0"
                j3 = input("J3 (Elbow)           : ") or "0.0"
                j4 = input("J4 (Wrist 1)         : ") or "0.0"
                j5 = input("J5 (Wrist 2)         : ") or "0.0"
                j6 = input("J6 (Tool rotation)   : ") or "0.0"
                try:
                    my_robot.move_joints_smoothly(
                        [float(j1), float(j2), float(j3), float(j4), float(j5), float(j6)]
                    )
                except ValueError:
                    print("\n[ERROR] Invalid input.")
            elif choice == "7":
                for _ in range(10):
                    state = my_robot.read_robot_state()
                    joints = my_robot.read_joints()
                    joints_str = (
                        "[Error]"
                        if "Error" in joints
                        else f"[{joints[0]:.1f}°, {joints[1]:.1f}°, {joints[2]:.1f}°...]"
                    )
                    print(f" -> Robot: {state.ljust(8)} | Joints: {joints_str}")
                    time.sleep(1)
            elif choice == "0":
                break
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        my_robot.disconnect()


# END CODE


# BEGIN MD
# ## Execution
# We use threads to run the Server, the automated Controller, and the
# interactive HMI Client simultaneously within a single script for demonstration purposes.
# END MD

# BEGIN CODE
if __name__ == "__main__":
    print("=" * 60)
    print("Starting Full Sorting Line Ecosystem")
    print("=" * 60)

    server_thread = threading.Thread(target=run_digital_twin_server)
    server_thread.start()

    controller_thread = threading.Thread(target=run_controller)
    controller_thread.start()

    run_hmi_client()

    print("\n[SYSTEM] Shutting down ecosystem...")
    system_running = False

    server_thread.join()
    controller_thread.join()
    print("[SYSTEM] Done.")
# END CODE
