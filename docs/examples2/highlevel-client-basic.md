Client Basics: Read, Write, and Subscriptions
=============================================

This tutorial demonstrates the high-level pythonic interface of the ``o6`` library.
It acts as the fundamental guide for connecting to an OPC UA server, manipulating
data, and setting up event-driven monitoring (Subscriptions).

## Overview
The `o6.Client` class provides a simplified abstraction over raw OPC UA services.
This example requires an active OPC UA server running on `localhost:4840`
exposing basic test nodes.

```python
# Generate the endpoint URL dynamically based on the local hostname
localhost = socket.gethostname()
endpoint_url = f"opc.tcp://{localhost}:4840"
print(f"Connecting to {endpoint_url} ...")
```

```python
try:
    with Client(endpoint_url) as client:
        print("[INFO] Connected to server successfully!")

```

## 1. Basic Read/Write Operations
The client must be instantiated with the `endpointUrl` directly.
To read or write, simply pass the string representation of a NodeId.

```python
# Reading a single value
try:
    value = client.read("ns=1;s=IntegerVariable")
    print(f"[READ] Value: {value}")
except StatusCodeError as e:
    print(f"[ERROR] Read failed: {e}")

# Writing a single value
try:
    client.write("ns=1;s=IntegerVariable", 42)
    print("[WRITE] Write successful! (42)")

    # Read back to verify
    new_value = client.read("ns=1;s=IntegerVariable")
    print(f"[VERIFY] Verified value: {new_value}")
except StatusCodeError as e:
    print(f"[ERROR] Write failed: {e}")
```

## 2. Multiple Operations
To optimize network traffic, you can read or write multiple nodes in a single request
by passing a list (for reading) or a dictionary (for writing).

```python
# Read multiple values at once
try:
    values = client.read([
        "ns=1;s=IntegerVariable",
        "ns=1;s=DoubleVariable"
    ])
    print(f"[READ] Multiple read results: {values}")
except StatusCodeError as e:
    print(f"[ERROR] Multiple read failed: {e}")

# Write multiple values at once using a dictionary
try:
    client.write({
        "ns=1;s=IntegerVariable": 100,
        "ns=1;s=DoubleVariable": 2.7182,
    })
    print("[WRITE] Multiple write successful!")
except StatusCodeError as e:
    print(f"[ERROR] Multiple write failed: {e}")
```

## 3. Method Call
OPC UA servers can expose executable methods. You can trigger them by providing
the NodeId of the parent object, the NodeId of the method, and a list of arguments.

```python
try:
    result = client.call(
        "ns=1;s=TestMethods",        # Object NodeId
        "ns=1;s=MethodHelloString",  # Method NodeId
        ["World"]                    # Input arguments
    )
    print(f"[METHOD] Result: {result}")
except Exception as e:
    print(f"[ERROR] Method call failed: {e}")
```

## 4. Subscriptions (Event-Driven Architecture)
Instead of polling values continuously, use a Subscription.
You first define a `on_data_change` function.
The server will only trigger this callback when the monitored value physically changes.

```python
def on_data_change(node, val):
    print(f"[EVENT] Node {node} changed to -> {val}")

print("[INFO] Creating subscription...")

# Create a subscription with a publishing interval of 1000ms
subscription = client.createSubscription(1000)

# Subscribe to data changes for a specific node
node_to_monitor = "ns=1;s=IntegerVariable"
monitored_item = client.monitor(target=node_to_monitor, subscription=subscription, callback=on_data_change, samplingInterval=500)

print("[INFO] Monitoring started. Simulating external writes...")
for i in range(1, 4):
    client.write("ns=1;s=IntegerVariable", 200 + i)
    time.sleep(1)

print("[INFO] Cleaning up subscription...")
subscription.delete()
```

## 5. Node Browsing
You can easily fetch a Node object using dictionary-style access (`client["NodeId"]`)
to inspect its properties.

```python
node = client["ns=0;i=85"] # The standard 'Objects' folder
print(f"[BROWSE] Node target: {node}")
print(f"[BROWSE] Node name: {node(attr=AttributeId.BROWSE_NAME)}")
print(f"[BROWSE] Node class: {node(attr=AttributeId.NODE_CLASS)}")
print(f"[BROWSE] Node references: {client.browse(node)}")
```

## Complete Source Code

```python
#!/usr/bin/env python3
# Copyright 2026 (c) o6 Automation GmbH
"""
Client Basics: Read, Write, and Subscriptions
=============================================

This tutorial demonstrates the high-level pythonic interface of the ``o6`` library.
It acts as the fundamental guide for connecting to an OPC UA server, manipulating
data, and setting up event-driven monitoring (Subscriptions).
"""


import time
import socket
from o6 import Client, StatusCodeError, AttributeId

def header(title: str) -> None:
    """Tiny helper to print a banner around each section."""
    print()
    print("=" * 64)
    print(title)
    print("=" * 64)

# Generate the endpoint URL dynamically based on the local hostname
localhost = socket.gethostname()
endpoint_url = f"opc.tcp://{localhost}:4840"
print(f"Connecting to {endpoint_url} ...")

# ---------------------------------------------------------------------------
# The client connection is held open using a `with` statement.
# All operations are performed sequentially within this block.
# ---------------------------------------------------------------------------

try:
    with Client(endpoint_url) as client:
        print("[INFO] Connected to server successfully!")


        # =======================================================================
        # 1. Basic Read/Write Operations
        # =======================================================================



        header("1. Basic Read/Write Operations")
        # Reading a single value
        try:
            value = client.read("ns=1;s=IntegerVariable")
            print(f"[READ] Value: {value}")
        except StatusCodeError as e:
            print(f"[ERROR] Read failed: {e}")

        # Writing a single value
        try:
            client.write("ns=1;s=IntegerVariable", 42)
            print("[WRITE] Write successful! (42)")

            # Read back to verify
            new_value = client.read("ns=1;s=IntegerVariable")
            print(f"[VERIFY] Verified value: {new_value}")
        except StatusCodeError as e:
            print(f"[ERROR] Write failed: {e}")

        # =======================================================================
        # 2. Multiple Operations
        # =======================================================================


        header("2. Multiple Operations")
        # Read multiple values at once
        try:
            values = client.read([
                "ns=1;s=IntegerVariable",
                "ns=1;s=DoubleVariable"
            ])
            print(f"[READ] Multiple read results: {values}")
        except StatusCodeError as e:
            print(f"[ERROR] Multiple read failed: {e}")

        # Write multiple values at once using a dictionary
        try:
            client.write({
                "ns=1;s=IntegerVariable": 100,
                "ns=1;s=DoubleVariable": 2.7182,
            })
            print("[WRITE] Multiple write successful!")
        except StatusCodeError as e:
            print(f"[ERROR] Multiple write failed: {e}")

        # =======================================================================
        # 3. Method Call
        # =======================================================================


        header("3. Method Call")
        try:
            result = client.call(
                "ns=1;s=TestMethods",        # Object NodeId
                "ns=1;s=MethodHelloString",  # Method NodeId
                ["World"]                    # Input arguments
            )
            print(f"[METHOD] Result: {result}")
        except Exception as e:
            print(f"[ERROR] Method call failed: {e}")

    # =======================================================================
    # 4. Subscriptions
    # =======================================================================



        header("4. Subscriptions (Event-Driven Architecture)")
        def on_data_change(node, val):
            print(f"[EVENT] Node {node} changed to -> {val}")

        print("[INFO] Creating subscription...")

        # Create a subscription with a publishing interval of 1000ms
        subscription = client.createSubscription(1000)

        # Subscribe to data changes for a specific node
        node_to_monitor = "ns=1;s=IntegerVariable"
        monitored_item = client.monitor(target=node_to_monitor, subscription=subscription, callback=on_data_change, samplingInterval=500)

        print("[INFO] Monitoring started. Simulating external writes...")
        for i in range(1, 4):
            client.write("ns=1;s=IntegerVariable", 200 + i)
            time.sleep(1)

        print("[INFO] Cleaning up subscription...")
        subscription.delete()

        # =======================================================================
        # 5. Node Browsing
        # =======================================================================


        header("5. Node Browsing")
        node = client["ns=0;i=85"] # The standard 'Objects' folder
        print(f"[BROWSE] Node target: {node}")
        print(f"[BROWSE] Node name: {node(attr=AttributeId.BROWSE_NAME)}")
        print(f"[BROWSE] Node class: {node(attr=AttributeId.NODE_CLASS)}")
        print(f"[BROWSE] Node references: {client.browse(node)}")

except StatusCodeError as e:
    print(f"[ERROR] Connection failed: {e}")
    print("Note: Make sure an OPC UA server is running on localhost:4840")

print()
print("Connection closed.")
header("End of high-level client example")
```
