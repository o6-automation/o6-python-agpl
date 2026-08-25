Client for the Distilling-System Server
=======================================

Talks to the `server.py` example: it connects, browses the
``DistillingSystem`` address space, reads the current batch state,
writes the writable ``Operating`` / ``Setpoint`` variables, calls
the ``Shutdown`` method, and finally subscribes to the
``LastEventMessage`` variable to receive server-pushed event
notifications as the sim cycles.

Run `server.py --sim` in one terminal before starting this
script.

This example goes through the high-level ``o6.Client`` API end to
end: connect, browse, read, write, call, subscribe.  Each
interaction is wrapped in its own ``with Client(...)`` block -
the call section uses a short-lived session, the subscription
section uses its own session to keep the connection open while
events stream in.

## 1. Connection Setup
`socket.gethostname()` builds the endpoint URL the same way the
server does - keeping encrypted endpoints happy when the
certificate was issued for the host's name.

```python
localhost = "localhost"
endpoint_url = f"opc.tcp://{localhost}:4840"
print(f"Connecting to {endpoint_url} ...")
```

## 2. Browsing the Address Space
`client.browse(nodeid, result_mask=63)` walks one level out from
the given node and returns a list of `ReferenceDescription`
objects.  The `result_mask=63` flag populates every field
(browse name, display name, node class, type definition, ...);
the default is `0`.

We start from the standard ``Objects`` folder (`i=85`) and drill
down to the `DistillingSystem` object so the script keeps
working even if the server's namespace index changes.

```python
try:
    with Client(endpoint_url) as client:
        print("[INFO] Connected to server successfully!\n")

        # Find the DistillingSystem object once, by name.
        for ref in client.browse("i=85", resultMask=63):
            if ref.browseName.name == "DistillingSystem":
                sys_id = ref.nodeId
                break
        else:
            raise RuntimeError("DistillingSystem not found in Objects folder")
        print(f"[BROWSE] DistillingSystem = {sys_id}\n")

        # Walk one level deeper: Kettle, Status, Actuators, ...
        for ref in client.browse(sys_id, resultMask=63):
            print(f"  {ref.browseName.name:<18} ({ref.nodeId})")
```

## 3. Reading the Live State
`client.read([...])` accepts a list of NodeIds and returns a
matching list of values in a single ``Read`` service request.

```python
try:
    with Client(endpoint_url) as client:
        # Grab every visible variable of the sim in one round-trip.
        values = client.read(
            [
                "ns=1;i=1201",  # Status/State
                "ns=1;i=1202",  # Status/Cycle
                "ns=1;i=1203",  # Status/Operating
                "ns=1;i=1204",  # Status/Setpoint
                "ns=1;i=1301",  # Kettle/Level
                "ns=1;i=1302",  # Kettle/Temperature
                "ns=1;i=1401",  # Distillate/Level
                "ns=1;i=1501",  # Actuators/FillValve
                "ns=1;i=1502",  # Actuators/DrainValve
                "ns=1;i=1503",  # Actuators/Heater
                "ns=1;i=1601",  # Events/EventCount
                "ns=1;i=1603",  # Events/LastEventMessage
            ]
        )

        labels = [
            "State",
            "Cycle",
            "Operating",
            "Setpoint",
            "Kettle/Level",
            "Kettle/Temperature",
            "Distillate/Level",
            "FillValve",
            "DrainValve",
            "Heater",
            "EventCount",
            "LastEvent",
        ]
        print("\n[READ]   Current state:")
        for label, value in zip(labels, values):
            print(f"  {label:<22} = {value}")
```

## 4. Writing the Writable Variables
The sim is autonomous: it drives its own valves and heater.
But the two writable OPC UA variables ``Operating`` (pause the
state machine) and ``Setpoint`` (target distilling temperature)
are exactly the knobs a client is expected to control.

Wrapping the value in `Double(0.0)` is optional; the SDK
infers the OPC UA data type from the Python type you pass in.
We use the explicit form here to make the wire type obvious.

```python
try:
    with Client(endpoint_url) as client:
        # Change the setpoint: a hotter distillation.
        client.write("ns=1;i=1204", Double(90.0))
        new_setpoint = client.read("ns=1;i=1204")
        print(f"\n[WRITE]  Setpoint <- 90.0 °C  (verified = {new_setpoint})")

        # Toggle Operating: pause the sim.
        client.write("ns=1;i=1203", False)
        time.sleep(0.2)
        new_operating = client.read("ns=1;i=1203")
        print(f"[WRITE]  Operating <- False   (verified = {new_operating})")

        # Resume the sim.
        client.write("ns=1;i=1203", True)
        time.sleep(0.2)
        new_operating = client.read("ns=1;i=1203")
        print(f"[WRITE]  Operating <- True    (verified = {new_operating})")
```

## 5. Calling a Method
`client.call(object_id, method_id, input_args)` invokes a
server-side method.  The return value is a tuple
``(status_code, *output_args)``. The first element is the
``StatusCode``, the rest are the declared output arguments
in order.

The ``Start`` method on the distilling system is a no-op
acknowledgement; ``Shutdown`` flips a flag the main loop checks
on the next tick.  We call ``Start`` here (safe) and leave
``Shutdown`` out of the default flow so a run of this example
doesn't kill the server while you're still poking at it.

```python
try:
    with Client(endpoint_url) as client:
        result = client.call(
            "ns=1;i=1000",  # DistillingSystem (object_id)
            "ns=1;i=2001",  # Start           (method_id)
            inputArgs=[],
        )
        status, *_ = result
        print(f"\n[CALL]   Start() -> {status.name}")
```

## 6. Subscribing to Events
Polling `LastEventMessage` is wasteful. It almost never
changes, but the client has no way to know that.  A
`Subscription` plus a `MonitoredItem` lets the server *push*
a notification only when the message actually changes.

We open a second `with Client(...)` block because
subscriptions are tied to the active session; the previous
block's session was already torn down on exit.

```python
try:
    with Client(endpoint_url) as client:

        def on_data_change(monitored_item, value) -> None:
            """Server-pushed callback -- runs on the client's event loop."""
            print(f"[EVENT]  {monitored_item} -> {value}")

        print("\n[INFO]   Creating subscription (500 ms publishing interval)...")
        subscription = client.createSubscription(publishingInterval=500)

        print("[INFO]   Monitoring LastEventMessage (ns=1;i=1603)...")
        monitored_item = client.monitor(
            target="ns=1;i=1603",
            callback=on_data_change,
            subscription=subscription,
            samplingInterval=250,
        )

        # Give the sim time to fire a few state transitions.
        print("[INFO]   Listening for 5 seconds of sim events...")
        time.sleep(5.0)

        print("\n[INFO]   Cleaning up subscription...")
        monitored_item.delete()
        subscription.delete()
        print("[INFO]   Subscription deleted.")
```

## Complete Source Code

```python
#!/usr/bin/env python3
# Copyright 2026 (c) o6 Automation GmbH
"""
Client for the Distilling-System Server
=======================================

Talks to the `server.py` example: it connects, browses the
``DistillingSystem`` address space, reads the current batch state,
writes the writable ``Operating`` / ``Setpoint`` variables, calls
the ``Shutdown`` method, and finally subscribes to the
``LastEventMessage`` variable to receive server-pushed event
notifications as the sim cycles.

Run `server.py --sim` in one terminal before starting this
script.
"""


import socket
import time
from o6 import Client, Double, StatusCodeError


localhost = "localhost"
endpoint_url = f"opc.tcp://{localhost}:4840"
print(f"Connecting to {endpoint_url} ...")



try:
    with Client(endpoint_url) as client:
        print("[INFO] Connected to server successfully!\n")

        # Find the DistillingSystem object once, by name.
        for ref in client.browse("i=85", resultMask=63):
            if ref.browseName.name == "DistillingSystem":
                sys_id = ref.nodeId
                break
        else:
            raise RuntimeError("DistillingSystem not found in Objects folder")
        print(f"[BROWSE] DistillingSystem = {sys_id}\n")

        # Walk one level deeper: Kettle, Status, Actuators, ...
        for ref in client.browse(sys_id, resultMask=63):
            print(f"  {ref.browseName.name:<18} ({ref.nodeId})")

except StatusCodeError as e:
    print(f"[ERROR]  Connection failed: {e}")
    print("Note:   Make sure the server is running on localhost:4840")
    print("        (try: python examples/example-server/server.py --sim)")
except Exception as e:
    print(f"[ERROR]  Unexpected error: {e}")



try:
    with Client(endpoint_url) as client:
        # Grab every visible variable of the sim in one round-trip.
        values = client.read(
            [
                "ns=1;i=1201",  # Status/State
                "ns=1;i=1202",  # Status/Cycle
                "ns=1;i=1203",  # Status/Operating
                "ns=1;i=1204",  # Status/Setpoint
                "ns=1;i=1301",  # Kettle/Level
                "ns=1;i=1302",  # Kettle/Temperature
                "ns=1;i=1401",  # Distillate/Level
                "ns=1;i=1501",  # Actuators/FillValve
                "ns=1;i=1502",  # Actuators/DrainValve
                "ns=1;i=1503",  # Actuators/Heater
                "ns=1;i=1601",  # Events/EventCount
                "ns=1;i=1603",  # Events/LastEventMessage
            ]
        )

        labels = [
            "State",
            "Cycle",
            "Operating",
            "Setpoint",
            "Kettle/Level",
            "Kettle/Temperature",
            "Distillate/Level",
            "FillValve",
            "DrainValve",
            "Heater",
            "EventCount",
            "LastEvent",
        ]
        print("\n[READ]   Current state:")
        for label, value in zip(labels, values):
            print(f"  {label:<22} = {value}")

except StatusCodeError as e:
    print(f"[ERROR]  Read failed: {e}")
except Exception as e:
    print(f"[ERROR]  Unexpected error: {e}")



try:
    with Client(endpoint_url) as client:
        # Change the setpoint: a hotter distillation.
        client.write("ns=1;i=1204", Double(90.0))
        new_setpoint = client.read("ns=1;i=1204")
        print(f"\n[WRITE]  Setpoint <- 90.0 °C  (verified = {new_setpoint})")

        # Toggle Operating: pause the sim.
        client.write("ns=1;i=1203", False)
        time.sleep(0.2)
        new_operating = client.read("ns=1;i=1203")
        print(f"[WRITE]  Operating <- False   (verified = {new_operating})")

        # Resume the sim.
        client.write("ns=1;i=1203", True)
        time.sleep(0.2)
        new_operating = client.read("ns=1;i=1203")
        print(f"[WRITE]  Operating <- True    (verified = {new_operating})")

except StatusCodeError as e:
    print(f"[ERROR]  Write failed: {e}")
except Exception as e:
    print(f"[ERROR]  Unexpected error: {e}")



try:
    with Client(endpoint_url) as client:
        result = client.call(
            "ns=1;i=1000",  # DistillingSystem (object_id)
            "ns=1;i=2001",  # Start           (method_id)
            inputArgs=[],
        )
        status, *_ = result
        print(f"\n[CALL]   Start() -> {status.name}")

except StatusCodeError as e:
    print(f"[ERROR]  Method call failed: {e}")
except Exception as e:
    print(f"[ERROR]  Unexpected error: {e}")



try:
    with Client(endpoint_url) as client:

        def on_data_change(monitored_item, value) -> None:
            """Server-pushed callback -- runs on the client's event loop."""
            print(f"[EVENT]  {monitored_item} -> {value}")

        print("\n[INFO]   Creating subscription (500 ms publishing interval)...")
        subscription = client.createSubscription(publishingInterval=500)

        print("[INFO]   Monitoring LastEventMessage (ns=1;i=1603)...")
        monitored_item = client.monitor(
            target="ns=1;i=1603",
            callback=on_data_change,
            subscription=subscription,
            samplingInterval=250,
        )

        # Give the sim time to fire a few state transitions.
        print("[INFO]   Listening for 5 seconds of sim events...")
        time.sleep(5.0)

        print("\n[INFO]   Cleaning up subscription...")
        monitored_item.delete()
        subscription.delete()
        print("[INFO]   Subscription deleted.")

except StatusCodeError as e:
    print(f"[ERROR]  Subscription failed: {e}")
except Exception as e:
    print(f"[ERROR]  Unexpected error: {e}")

print("\n=== Example completed ===")
```
