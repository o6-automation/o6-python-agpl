Sorting Line Tutorial - Step 3: The HMI Client
==============================================
The HMI (Human-Machine Interface) is an interactive console for operators.
It shows how to use the ``o6`` library to execute manual commands,
perform trajectory interpolations, and monitor the installation in real-time.

## 1. Client Configuration
The `clientDemo` class acts as an interface that holds the references to the
OPC UA nodes already defined within the Digital Twin server.
It provides the addresses (NodeIds) used to access the Command (`_cmd`)
and Feedback (`_fb`) variables instantiated by the server.

```python
import time
from o6 import Client, StatusCodeError, NodeId


class clientDemo:
    """
    Simplified class to interact with the Visual Components Sorting Robot Digital Twin.
    """

    def __init__(self, endpoint_url="opc.tcp://127.0.0.1:4840"):
        self.endpointUrl = endpoint_url
        self.client = Client(endpoint_url)
        self.connected = False

        # OPC UA Nodes
        self.id_robot_state = "ns=1;i=131"
        self.id_color_sensor = "ns=1;i=114"
        self.id_sort_red = "ns=1;i=132"
        self.id_sort_blue = "ns=1;i=133"
        self.id_inputconveyor_speed = "ns=1;i=111"

        # Robot Joints Nodes
        self.id_j1_fb = "ns=1;i=164"
        self.id_j2_fb = "ns=1;i=165"
        self.id_j3_fb = "ns=1;i=166"
        self.id_j4_fb = "ns=1;i=167"
        self.id_j5_fb = "ns=1;i=168"
        self.id_j6_fb = "ns=1;i=169"

        self.id_j1_cmd = "ns=1;i=174"
        self.id_j2_cmd = "ns=1;i=175"
        self.id_j3_cmd = "ns=1;i=176"
        self.id_j4_cmd = "ns=1;i=177"
        self.id_j5_cmd = "ns=1;i=178"
        self.id_j6_cmd = "ns=1;i=179"

    def connect(self) -> None:
        print(f"[o6 Python] Attempting to connect to server {self.endpointUrl}...")
        try:
            self.client.connect()
            self.connected = True
            print("[o6 Python] Successfully connected to the Digital Twin !")
        except StatusCodeError as e:
            print(f"[o6 Python] OPC UA Status Error: {e}")
        except Exception as e:
            print(f"[o6 Python] Connection Error: {e}")

    def disconnect(self) -> None:
        if self.connected:
            self.client.disconnect()
            print("[o6 Python] Disconnected from the server.")
```

## 2. Basic Node Operations
Simple methods are exposed to read states and force overrides using standard
`read()` and `write()` functions.

```python
def read_robot_state(self) -> str:
    try:
        state = self.client.read(self.id_robot_state)
        return str(state)
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
    """Forces the robot sorting cycle for Red parts."""
    print("[o6 Python] -> Sending override command: SORT RED (LEFT)")
    try:
        # Simulate electrical pulse
        self.client.write(self.id_sort_red, True)
        time.sleep(0.2)
        self.client.write(self.id_sort_red, False)
    except StatusCodeError as e:
        print(f"[o6 Python] Write failed: {e}")

def force_sort_blue(self) -> None:
    """Forces the robot sorting cycle for Blue parts."""
    print("[o6 Python] -> Sending override command: SORT BLUE (RIGHT)")
    try:
        # Simulate electrical pulse
        self.client.write(self.id_sort_blue, True)
        time.sleep(0.2)
        self.client.write(self.id_sort_blue, False)
    except StatusCodeError as e:
        print(f"[o6 Python] Write failed: {e}")

def set_conveyor_speed(self, speed_value: float) -> None:
    """Sets the conveyor speed."""
    try:
        float_val = float(speed_value)
        self.client.write(self.id_inputconveyor_speed, float_val)
        print(f"[o6 Python] Conveyor speed successfully set to {float_val}")
    except ValueError:
        print("[o6 Python] Invalid input: Speed must be a valid number.")
    except StatusCodeError as e:
        print(f"[o6 Python] Failed to set speed: {e}")
    except Exception as e:
        print(f"[o6 Python] Unexpected error: {e}")
```

## 3. Trajectory Interpolation
To perform realistic movements in the 3D simulation, we read the current physical position
from the Feedback nodes (`_fb`), calculate a linear trajectory, and incrementally write
the micro-steps to the Command nodes (`_cmd`).

```python
def move_joints_smoothly(self, target_angles: list[float], steps: int = 50, duration: float = 2.0) -> None:
    """
    Moves the robotic arm smoothly using Linear Interpolation.
    It reads current position from Feedback, and writes steps to Command nodes.
    """
    print(f"[o6 Python] -> Calculating smooth trajectory over {duration}s...")
    current_angles = self.read_joints()

    if "Error" in current_angles:
        print("[o6 Python] [ERROR] Cannot move smoothly: Failed to read current Feedback angles.")
        return

    cmd_nodes = [self.id_j1_cmd, self.id_j2_cmd, self.id_j3_cmd, self.id_j4_cmd, self.id_j5_cmd, self.id_j6_cmd]

    sleep_time = duration / steps

    for step in range(1, steps + 1):
        for i in range(6):
            # Linear Interpolation: current + (target - current) * (progress percentage)
            interpolated_val = current_angles[i] + (float(target_angles[i]) - current_angles[i]) * (step / steps)

            try:
                self.client.write(cmd_nodes[i], float(interpolated_val))
            except StatusCodeError:
                pass

        time.sleep(sleep_time)  # Pause between each micro-movement

    print("[o6 Python] Robot successfully reached target position.")

def read_joints(self) -> list[float]:
    """Reads the current joint values from the robot."""
    try:
        j1 = float(self.client.read(self.id_j1_fb))
        j2 = float(self.client.read(self.id_j2_fb))
        j3 = float(self.client.read(self.id_j3_fb))
        j4 = float(self.client.read(self.id_j4_fb))
        j5 = float(self.client.read(self.id_j5_fb))
        j6 = float(self.client.read(self.id_j6_fb))
        return [j1, j2, j3, j4, j5, j6]
    except StatusCodeError:
        return ["Error"] * 6
    except Exception:
        return ["Error"] * 6
```

## 4. Live Monitoring with Subscriptions
The `live_monitor` method subscribes to the robot state, the color sensor,
and all six joint feedback nodes at once. The server then pushes a
notification to the client *only* when one of those values actually
changes so there is no polling loop on the client side. Every notification
updates a small `state` dictionary and re-renders a single line on the
console, so the operator sees the freshest values without flooding the
terminal.

```python
def live_monitor(self) -> None:
    """Run an event-driven live monitor until the operator presses Enter."""
    # Initial values (used to seed the display before the first notification)
    state: dict[str, str] = {
        "robot": self.read_robot_state(),
        "sensor": self.read_color_sensor(),
        "joints": self.read_joints(),
    }

    # All nodeids we want to follow, paired with a label used to update
    # the state dict and a small formatter for the display line.
    watched = [
        (self.id_robot_state, "robot", lambda v: str(v)),
        (
            self.id_color_sensor,
            "sensor",
            lambda v: ("Red detected" if str(v) == "1" else "Blue detected" if str(v) == "4" else "None/Waiting"),
        ),
        (self.id_j1_fb, "j1", lambda v: f"{float(v):.1f}°"),
        (self.id_j2_fb, "j2", lambda v: f"{float(v):.1f}°"),
        (self.id_j3_fb, "j3", lambda v: f"{float(v):.1f}°"),
        (self.id_j4_fb, "j4", lambda v: f"{float(v):.1f}°"),
        (self.id_j5_fb, "j5", lambda v: f"{float(v):.1f}°"),
        (self.id_j6_fb, "j6", lambda v: f"{float(v):.1f}°"),
    ]

    def render_line() -> None:
        joints = state["joints"]
        if isinstance(joints, list) and "Error" not in joints:
            joints_str = (
                f"[{joints[0]:.1f}°, {joints[1]:.1f}°, {joints[2]:.1f}°, "
                f"{joints[3]:.1f}°, {joints[4]:.1f}°, {joints[5]:.1f}°]"
            )
        else:
            joints_str = "[Error reading joints]"
        print(f" -> Robot: {state['robot']:<8} | " f"Sensor: {state['sensor']:<14} | " f"Joints: {joints_str}")

    # One callback handles all monitored items. We identify which one
    # fired by looking at its nodeid, then format the value and re-render.
    def on_any_change(monitored_item, value) -> None:
        for nodeid, label, fmt in watched:
            if str(monitored_item._item_to_monitor.nodeId) == nodeid:
                if label == "robot":
                    state["robot"] = fmt(value)
                elif label == "sensor":
                    state["sensor"] = fmt(value)
                else:
                    if not isinstance(state["joints"], list):
                        state["joints"] = [0.0] * 6
                    idx = int(label[1]) - 1  # "j1" -> 0, "j6" -> 5
                    state["joints"][idx] = float(value)
                break
        render_line()

    # 100ms publishing interval — fast enough to feel live, light enough
    # to keep network traffic down to actual change events.
    subscription = self.client.createSubscription(publishingInterval=100.0)
    nodeids = [nodeid for nodeid, _, _ in watched]
    try:
        self.client.monitor(
            target=nodeids,
            callback=on_any_change,
            subscription=subscription,
            samplingInterval=100.0,
        )
    except Exception as e:
        print(f"[o6 Python] Failed to register monitored items: {e}")
        return

    # Show the initial state immediately, then wait. The subscription
    # delivers subsequent updates asynchronously and prints them via the
    # callback. The HMI returns to the menu when the operator presses Enter.
    print("\n[MONITORING] Live monitoring active — press Enter to return to the menu.")
    render_line()
    try:
        input()
    except KeyboardInterrupt:
        pass
    finally:
        try:
            subscription.delete()
        except Exception:
            pass
        print("[MONITORING] Stopped.")
```

## 5. Interactive Menu
A standard CLI loop exposes the HMI functionality to the operator, allowing
manual control and event-driven live monitoring of the system's states.

```python
def display_menu() -> None:
    print("\n" + "=" * 40)
    print("   CLIENT DEMONSTRATOR - o6 Python   ")
    print("=" * 40)
    print("1. Read current robot state")
    print("2. Read optical sensor value")
    print("3. Manual override: Sort LEFT (Red)")
    print("4. Manual override: Sort RIGHT (Blue)")
    print("5. Set Input Conveyor Speed (mm/s) (e.g. 200.0 or 10.5)")
    print("6. Set Robot Joints")
    print("7. Live monitoring")
    print("0. Quit")
    print("=" * 40)


def main():
    # Initialize the client
    my_robot = clientDemo()
    my_robot.connect()

    if not my_robot.connected:
        return

    try:
        while True:
            display_menu()
            choice = input("Choose an action (0-7): ")

            if choice == "1":
                state = my_robot.read_robot_state()
                print(f"\n[RESULT] Robotic arm state: {state}")

            elif choice == "2":
                sensor = my_robot.read_color_sensor()
                print(f"\n[RESULT] Entry sensor: {sensor}")

            elif choice == "3":
                state = my_robot.read_robot_state()
                if state == "Idle":
                    my_robot.force_sort_red()
                    print("\n[RESULT] Movement successfully initiated.")
                else:
                    print(f"\n[ERROR] Cannot send command, robot is busy ({state}).")

            elif choice == "4":
                state = my_robot.read_robot_state()
                if state == "Idle":
                    my_robot.force_sort_blue()
                    print("\n[RESULT] Movement successfully initiated.")
                else:
                    print(f"\n[ERROR] Cannot send command, robot is busy ({state}).")

            elif choice == "5":
                val = input("Enter new input conveyor speed (Double): ")
                my_robot.set_conveyor_speed(val)

            elif choice == "6":
                print("\nEnter joint values in degrees (from -180.0 to 180.0):")
                j1 = input("J1 (Base rotation)   : ") or "0.0"
                j2 = input("J2 (Shoulder)        : ") or "0.0"
                j3 = input("J3 (Elbow)           : ") or "0.0"
                j4 = input("J4 (Wrist 1)         : ") or "0.0"
                j5 = input("J5 (Wrist 2)         : ") or "0.0"
                j6 = input("J6 (Tool rotation)   : ") or "0.0"

                try:
                    targets = [float(j1), float(j2), float(j3), float(j4), float(j5), float(j6)]
                    my_robot.move_joints_smoothly(targets)
                except ValueError:
                    print("\n[ERROR] Invalid input. Please enter numbers only.")

            elif choice == "7":
                my_robot.live_monitor()

            elif choice == "0":
                print("\nClosing demonstrator...")
                break

            else:
                print("\n[ERROR] Invalid choice.")

            time.sleep(1)  # Small pause

    except KeyboardInterrupt:
        print("\nKeyboard interruption detected.")
    finally:
        my_robot.disconnect()


if __name__ == "__main__":
    main()
```

## Complete Source Code

```python
#!/usr/bin/env python3
# Copyright 2026 (c) o6 Automation GmbH
"""
Sorting Line Tutorial - Step 3: The HMI Client
==============================================
The HMI (Human-Machine Interface) is an interactive console for operators.
It shows how to use the ``o6`` library to execute manual commands,
perform trajectory interpolations, and monitor the installation in real-time.
"""


import time
from o6 import Client, StatusCodeError, NodeId


class clientDemo:
    """
    Simplified class to interact with the Visual Components Sorting Robot Digital Twin.
    """

    def __init__(self, endpoint_url="opc.tcp://127.0.0.1:4840"):
        self.endpointUrl = endpoint_url
        self.client = Client(endpoint_url)
        self.connected = False

        # OPC UA Nodes
        self.id_robot_state = "ns=1;i=131"
        self.id_color_sensor = "ns=1;i=114"
        self.id_sort_red = "ns=1;i=132"
        self.id_sort_blue = "ns=1;i=133"
        self.id_inputconveyor_speed = "ns=1;i=111"

        # Robot Joints Nodes
        self.id_j1_fb = "ns=1;i=164"
        self.id_j2_fb = "ns=1;i=165"
        self.id_j3_fb = "ns=1;i=166"
        self.id_j4_fb = "ns=1;i=167"
        self.id_j5_fb = "ns=1;i=168"
        self.id_j6_fb = "ns=1;i=169"

        self.id_j1_cmd = "ns=1;i=174"
        self.id_j2_cmd = "ns=1;i=175"
        self.id_j3_cmd = "ns=1;i=176"
        self.id_j4_cmd = "ns=1;i=177"
        self.id_j5_cmd = "ns=1;i=178"
        self.id_j6_cmd = "ns=1;i=179"

    def connect(self) -> None:
        print(f"[o6 Python] Attempting to connect to server {self.endpointUrl}...")
        try:
            self.client.connect()
            self.connected = True
            print("[o6 Python] Successfully connected to the Digital Twin !")
        except StatusCodeError as e:
            print(f"[o6 Python] OPC UA Status Error: {e}")
        except Exception as e:
            print(f"[o6 Python] Connection Error: {e}")

    def disconnect(self) -> None:
        if self.connected:
            self.client.disconnect()
            print("[o6 Python] Disconnected from the server.")



    def read_robot_state(self) -> str:
        try:
            state = self.client.read(self.id_robot_state)
            return str(state)
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
        """Forces the robot sorting cycle for Red parts."""
        print("[o6 Python] -> Sending override command: SORT RED (LEFT)")
        try:
            # Simulate electrical pulse
            self.client.write(self.id_sort_red, True)
            time.sleep(0.2)
            self.client.write(self.id_sort_red, False)
        except StatusCodeError as e:
            print(f"[o6 Python] Write failed: {e}")

    def force_sort_blue(self) -> None:
        """Forces the robot sorting cycle for Blue parts."""
        print("[o6 Python] -> Sending override command: SORT BLUE (RIGHT)")
        try:
            # Simulate electrical pulse
            self.client.write(self.id_sort_blue, True)
            time.sleep(0.2)
            self.client.write(self.id_sort_blue, False)
        except StatusCodeError as e:
            print(f"[o6 Python] Write failed: {e}")

    def set_conveyor_speed(self, speed_value: float) -> None:
        """Sets the conveyor speed."""
        try:
            float_val = float(speed_value)
            self.client.write(self.id_inputconveyor_speed, float_val)
            print(f"[o6 Python] Conveyor speed successfully set to {float_val}")
        except ValueError:
            print("[o6 Python] Invalid input: Speed must be a valid number.")
        except StatusCodeError as e:
            print(f"[o6 Python] Failed to set speed: {e}")
        except Exception as e:
            print(f"[o6 Python] Unexpected error: {e}")



    def move_joints_smoothly(self, target_angles: list[float], steps: int = 50, duration: float = 2.0) -> None:
        """
        Moves the robotic arm smoothly using Linear Interpolation.
        It reads current position from Feedback, and writes steps to Command nodes.
        """
        print(f"[o6 Python] -> Calculating smooth trajectory over {duration}s...")
        current_angles = self.read_joints()

        if "Error" in current_angles:
            print("[o6 Python] [ERROR] Cannot move smoothly: Failed to read current Feedback angles.")
            return

        cmd_nodes = [self.id_j1_cmd, self.id_j2_cmd, self.id_j3_cmd, self.id_j4_cmd, self.id_j5_cmd, self.id_j6_cmd]

        sleep_time = duration / steps

        for step in range(1, steps + 1):
            for i in range(6):
                # Linear Interpolation: current + (target - current) * (progress percentage)
                interpolated_val = current_angles[i] + (float(target_angles[i]) - current_angles[i]) * (step / steps)

                try:
                    self.client.write(cmd_nodes[i], float(interpolated_val))
                except StatusCodeError:
                    pass

            time.sleep(sleep_time)  # Pause between each micro-movement

        print("[o6 Python] Robot successfully reached target position.")

    def read_joints(self) -> list[float]:
        """Reads the current joint values from the robot."""
        try:
            j1 = float(self.client.read(self.id_j1_fb))
            j2 = float(self.client.read(self.id_j2_fb))
            j3 = float(self.client.read(self.id_j3_fb))
            j4 = float(self.client.read(self.id_j4_fb))
            j5 = float(self.client.read(self.id_j5_fb))
            j6 = float(self.client.read(self.id_j6_fb))
            return [j1, j2, j3, j4, j5, j6]
        except StatusCodeError:
            return ["Error"] * 6
        except Exception:
            return ["Error"] * 6



    def live_monitor(self) -> None:
        """Run an event-driven live monitor until the operator presses Enter."""
        # Initial values (used to seed the display before the first notification)
        state: dict[str, str] = {
            "robot": self.read_robot_state(),
            "sensor": self.read_color_sensor(),
            "joints": self.read_joints(),
        }

        # All nodeids we want to follow, paired with a label used to update
        # the state dict and a small formatter for the display line.
        watched = [
            (self.id_robot_state, "robot", lambda v: str(v)),
            (
                self.id_color_sensor,
                "sensor",
                lambda v: ("Red detected" if str(v) == "1" else "Blue detected" if str(v) == "4" else "None/Waiting"),
            ),
            (self.id_j1_fb, "j1", lambda v: f"{float(v):.1f}°"),
            (self.id_j2_fb, "j2", lambda v: f"{float(v):.1f}°"),
            (self.id_j3_fb, "j3", lambda v: f"{float(v):.1f}°"),
            (self.id_j4_fb, "j4", lambda v: f"{float(v):.1f}°"),
            (self.id_j5_fb, "j5", lambda v: f"{float(v):.1f}°"),
            (self.id_j6_fb, "j6", lambda v: f"{float(v):.1f}°"),
        ]

        def render_line() -> None:
            joints = state["joints"]
            if isinstance(joints, list) and "Error" not in joints:
                joints_str = (
                    f"[{joints[0]:.1f}°, {joints[1]:.1f}°, {joints[2]:.1f}°, "
                    f"{joints[3]:.1f}°, {joints[4]:.1f}°, {joints[5]:.1f}°]"
                )
            else:
                joints_str = "[Error reading joints]"
            print(f" -> Robot: {state['robot']:<8} | " f"Sensor: {state['sensor']:<14} | " f"Joints: {joints_str}")

        # One callback handles all monitored items. We identify which one
        # fired by looking at its nodeid, then format the value and re-render.
        def on_any_change(monitored_item, value) -> None:
            for nodeid, label, fmt in watched:
                if str(monitored_item._item_to_monitor.nodeId) == nodeid:
                    if label == "robot":
                        state["robot"] = fmt(value)
                    elif label == "sensor":
                        state["sensor"] = fmt(value)
                    else:
                        if not isinstance(state["joints"], list):
                            state["joints"] = [0.0] * 6
                        idx = int(label[1]) - 1  # "j1" -> 0, "j6" -> 5
                        state["joints"][idx] = float(value)
                    break
            render_line()

        # 100ms publishing interval — fast enough to feel live, light enough
        # to keep network traffic down to actual change events.
        subscription = self.client.createSubscription(publishingInterval=100.0)
        nodeids = [nodeid for nodeid, _, _ in watched]
        try:
            self.client.monitor(
                target=nodeids,
                callback=on_any_change,
                subscription=subscription,
                samplingInterval=100.0,
            )
        except Exception as e:
            print(f"[o6 Python] Failed to register monitored items: {e}")
            return

        # Show the initial state immediately, then wait. The subscription
        # delivers subsequent updates asynchronously and prints them via the
        # callback. The HMI returns to the menu when the operator presses Enter.
        print("\n[MONITORING] Live monitoring active — press Enter to return to the menu.")
        render_line()
        try:
            input()
        except KeyboardInterrupt:
            pass
        finally:
            try:
                subscription.delete()
            except Exception:
                pass
            print("[MONITORING] Stopped.")





def display_menu() -> None:
    print("\n" + "=" * 40)
    print("   CLIENT DEMONSTRATOR - o6 Python   ")
    print("=" * 40)
    print("1. Read current robot state")
    print("2. Read optical sensor value")
    print("3. Manual override: Sort LEFT (Red)")
    print("4. Manual override: Sort RIGHT (Blue)")
    print("5. Set Input Conveyor Speed (mm/s) (e.g. 200.0 or 10.5)")
    print("6. Set Robot Joints")
    print("7. Live monitoring")
    print("0. Quit")
    print("=" * 40)


def main():
    # Initialize the client
    my_robot = clientDemo()
    my_robot.connect()

    if not my_robot.connected:
        return

    try:
        while True:
            display_menu()
            choice = input("Choose an action (0-7): ")

            if choice == "1":
                state = my_robot.read_robot_state()
                print(f"\n[RESULT] Robotic arm state: {state}")

            elif choice == "2":
                sensor = my_robot.read_color_sensor()
                print(f"\n[RESULT] Entry sensor: {sensor}")

            elif choice == "3":
                state = my_robot.read_robot_state()
                if state == "Idle":
                    my_robot.force_sort_red()
                    print("\n[RESULT] Movement successfully initiated.")
                else:
                    print(f"\n[ERROR] Cannot send command, robot is busy ({state}).")

            elif choice == "4":
                state = my_robot.read_robot_state()
                if state == "Idle":
                    my_robot.force_sort_blue()
                    print("\n[RESULT] Movement successfully initiated.")
                else:
                    print(f"\n[ERROR] Cannot send command, robot is busy ({state}).")

            elif choice == "5":
                val = input("Enter new input conveyor speed (Double): ")
                my_robot.set_conveyor_speed(val)

            elif choice == "6":
                print("\nEnter joint values in degrees (from -180.0 to 180.0):")
                j1 = input("J1 (Base rotation)   : ") or "0.0"
                j2 = input("J2 (Shoulder)        : ") or "0.0"
                j3 = input("J3 (Elbow)           : ") or "0.0"
                j4 = input("J4 (Wrist 1)         : ") or "0.0"
                j5 = input("J5 (Wrist 2)         : ") or "0.0"
                j6 = input("J6 (Tool rotation)   : ") or "0.0"

                try:
                    targets = [float(j1), float(j2), float(j3), float(j4), float(j5), float(j6)]
                    my_robot.move_joints_smoothly(targets)
                except ValueError:
                    print("\n[ERROR] Invalid input. Please enter numbers only.")

            elif choice == "7":
                my_robot.live_monitor()

            elif choice == "0":
                print("\nClosing demonstrator...")
                break

            else:
                print("\n[ERROR] Invalid choice.")

            time.sleep(1)  # Small pause

    except KeyboardInterrupt:
        print("\nKeyboard interruption detected.")
    finally:
        my_robot.disconnect()


if __name__ == "__main__":
    main()
```
