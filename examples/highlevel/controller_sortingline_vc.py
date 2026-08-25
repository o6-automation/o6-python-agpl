#!/usr/bin/env python3
# Copyright 2026 (c) o6 Automation GmbH
"""
Sorting Line Example - Step 2: The Controller
=============================================
The controller acts as the "Brain" of the installation. It connects to the
server as an OPC UA Client. In this example, it uses an OPC UA Subscription
to react to changes from the optical color sensor and trigger sorting actions.
"""

# BEGIN MD
# ## 1. Setup and Connection
# The script defines the endpoint URL and connects to the OPC UA Digital Twin server.
# END MD

# BEGIN CODE
import queue
import threading
import time
from o6 import Client, StatusCodeError

# Robot state values, written and read to ns=1;i=131
STATE_IDLE = "Idle"
STATE_MOVING = "Moving"


def run_controller(endpoint_url: str) -> None:
    """Connect to the server and run the subscription-based control loop."""
    print("=== Sorting Line Controller ===")
    print(f"Connecting to {endpoint_url} ...")
    with Client(endpoint_url) as client:
        print("[CONTROLLER] Successfully connected to the OPC UA Server.")
        print(
            "[CONTROLLER] Waiting for physical parts from Visual Components... (Press Ctrl+C to exit)\n"
        )
        # END CODE

        # BEGIN MD
        # ## 2. Event-Driven Monitoring
        # Instead of a polling loop, we create an OPC UA `Subscription` and attach a
        # `MonitoredItem` to the color sensor node (`ns=1;i=114`). The server only
        # invokes our callback when the sensor value actually changes (sampled and
        # published every 100ms). This eliminates the busy polling loop and reduces
        # network traffic to actual events.
        # END MD

        # BEGIN MD
        # ### 2.1 The Subscription
        # A `Subscription` groups one or more `MonitoredItem`s and defines how often
        # the server is allowed to publish notifications. We create one with a 100ms
        # publishing interval (fast enough to react in real time).
        # END MD

        # BEGIN CODE
        # Dedicated subscription for the color sensor (100ms publishing interval)
        subscription = client.createSubscription(publishingInterval=100.0)
        # END CODE

        # BEGIN MD
        # ### 2.2 The Data-Change Callback
        # `client.monitor(...)` registers a `MonitoredItem` on the subscription. Every
        # time the color sensor value changes, the server calls our callback with the
        # new value.
        #
        # The callback only has one job: forward the new color to the actuator. We
        # keep it short so the client's internal event loop is never blocked. A
        # bounded queue (`maxsize=1`) holds at most one pending color. If a new one
        # arrives while the actuator is still busy, it simply replaces the old one.
        # END MD

        # BEGIN CODE
        # Bounded queue shared between the callback (producer) and the
        # actuator thread (consumer). maxsize=1 means: if the actuator is
        # still busy sorting a part, a newly detected color overwrites the
        # one waiting in the queue — we only care about the latest reading.
        part_queue: "queue.Queue[str]" = queue.Queue(maxsize=1)

        def on_color_change(monitored_item, value) -> None:
            """Server-pushed callback: invoked on every sensor value change."""
            current_color = str(value)

            # Sensor outputs '0' when no part is currently in front of it
            if current_color == "0":
                return

            # Replace any pending part with the latest reading
            try:
                part_queue.get_nowait()
            except queue.Empty:
                pass
            try:
                part_queue.put_nowait(current_color)
            except queue.Full:
                pass

        # END CODE

        # BEGIN MD
        # ### 2.3 The Actuation Worker
        # The actual sort sequence (reading the robot state, picking the right
        # command node, sending the pulse, waiting for the animation) does blocking
        # I/O and contains `time.sleep` waits. Running it directly inside the
        # subscription callback would block the client's event loop, so we hand it
        # off to a dedicated worker thread.
        #
        # The `client.read` and `client.write` calls below dispatch onto the client's
        # event loop internally; they block this worker thread until the result
        # comes back, but leave the event loop free to keep delivering notifications.
        # END MD

        # BEGIN CODE
        def actuator() -> None:
            """Drain the part queue and run the sort sequence for each part.

            Defined as a closure inside the `with` block so it can capture
            `client`, `part_queue`, and `STATE_*` directly from the enclosing
            scope.
            """
            while True:
                try:
                    current_color = part_queue.get()
                except Exception:
                    return

                try:
                    print(f"\n[EVENT] Color sensor detected new part: {current_color}")

                    # 1. Guard: only act if the robot is currently Idle
                    current_robot_state = str(client.read("ns=1;i=131"))
                    if current_robot_state != STATE_IDLE:
                        print(
                            f"[WARNING] Part detected but robot is busy ({current_robot_state}). Order skipped."
                        )
                        continue

                    # 2. Pick the right output based on the detected color.
                    #    The color sensor outputs '1' for Red and '4' for Blue.
                    #    Each color maps to a dedicated boolean command node on
                    #    the robot, mapped to a Visual Components digital input.
                    if current_color == "1":  # Red
                        cmd_node = "ns=1;i=132"  # VC Input 10 - Sort Red
                        print("[CONTROL] Action: Sending command to sort LEFT (Red)")
                    elif current_color == "4":  # Blue
                        cmd_node = "ns=1;i=133"  # VC Input 11 - Sort Blue
                        print("[CONTROL] Action: Sending command to sort RIGHT (Blue)")
                    else:
                        print(
                            f"[WARNING] Unrecognized color value: {current_color!r}. Order skipped."
                        )
                        continue

                    # 3. Trigger the robot: write a short electrical pulse on
                    #    the chosen command node and flip the robot state to
                    #    "Moving" so the next part is rejected until the sort
                    #    cycle is finished.
                    client.write(cmd_node, True)
                    client.write("ns=1;i=131", STATE_MOVING)

                    # 4. Hold the pulse for 0.2s, then release it. The 0.2s
                    #    is long enough for Visual Components to register the
                    #    rising edge and start the pre-programmed sort cycle.
                    time.sleep(0.2)
                    client.write(cmd_node, False)

                    # 5. Wait for the sort animation to finish before flipping
                    #    the state back to "Idle" and allowing the next part
                    #    through. The 1.5s matches the robot cycle time in
                    #    the Visual Components scene.
                    time.sleep(1.5)
                    client.write("ns=1;i=131", STATE_IDLE)
                    print("[CONTROL] Ready for next part.")

                except StatusCodeError as e:
                    print(f"[ERROR] Failed to read/write during sort: {e}")
                except Exception as e:
                    print(f"[ERROR] Unexpected error in actuator: {e}")

        # END CODE

        # BEGIN MD
        # ### 2.4 Start Monitoring
        # With the subscription, queue, callback, and worker all defined, we just need
        # to start the worker thread, register the monitored item on the subscription,
        # and keep the main thread alive so the client's event loop can keep delivering
        # notifications. A `Ctrl+C` cleanly tears down the client and its subscriptions
        # via the `with` block.
        # END MD

        # BEGIN CODE
        # Start the actuator thread as a daemon so it dies with the program.
        actuator_thread = threading.Thread(target=actuator, name="actuator", daemon=True)
        actuator_thread.start()

        # Register the monitored item on the subscription
        monitored_item = client.monitor(
            target="ns=1;i=114",
            callback=on_color_change,
            subscription=subscription,
            samplingInterval=100.0,
        )

        print(
            "[CONTROLLER] Subscription active. Waiting for color sensor events... (Press Ctrl+C to exit)\n"
        )

        while True:
            time.sleep(0.5)


if __name__ == "__main__":
    ENDPOINT_URL = "opc.tcp://localhost:4840"
    try:
        run_controller(ENDPOINT_URL)
    except StatusCodeError as e:
        print(f"[ERROR] Connection failed: {e}")
        print("Note: Please check if the OPC UA server is active on localhost:4840")
    except KeyboardInterrupt:
        print("\n[CONTROL] Stopping the controller client cleanly...")
# END CODE
