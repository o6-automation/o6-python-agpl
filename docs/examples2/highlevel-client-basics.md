Client Basics: Read, Write, and Subscriptions
=============================================

Walks through the high-level ``o6.Client`` API end to end: connecting to
a server, reading and writing single and multiple values, calling a
method, subscribing to a variable for event-driven updates, and finally
introspecting the address space via ``client[NodeId]`` and ``client.browse()``.

The example is wired against `basic_server.py` so start that script in
one terminal before running this one, and it will talk to the address
space defined there (``Plant / Temperature``, ``Plant / Pressure``,
``Plant / Counter``, ``Plant / Running``, ``Plant / Add``, …).

Every line in this example goes through the high-level ``o6.Client``
API  (the same shortcuts the rest of the documentation uses for
everyday work). The raw ``serviceX`` methods (covered in
`lowlevel/client.py`) are what the high-level calls wrap internally.

## 1. Connection Setup
The endpoint URL points at the server. `socket.gethostname()` is the
same method used in the other examples: it makes the URL match the
hostname the server advertises during discovery, which keeps
encrypted endpoints happy.

```python
localhost = "localhost"
endpoint_url = f"opc.tcp://{localhost}:4840"
print(f"Connecting to {endpoint_url} ...")
```

## 2. Basic Read / Write
`client.read(nodeid)` fetches the current value of a variable;
`client.write(nodeid, value)` assigns a new one. Both correspond to
the OPC UA `Read` and `Write` services. NodeIds are passed as
strings, and the SDK infers the OPC UA data type from the Python
type of the value you provide.

The `with Client(...) as client:` block opens the secure channel
and session on `__enter__` and tears them down on `__exit__` —
connection failures appear as `StatusCodeError`.

```python
try:
    with Client(endpoint_url) as client:
        print("[INFO] Connected to server successfully!\n")

        # ── Single read ───────────────────────────────────────────
        try:
            value = client.read("ns=1;i=1004")  # Plant / Counter (Int32)
            print(f"[READ]   Counter = {value}")
        except StatusCodeError as e:
            print(f"[ERROR]  Read failed: {e}")

        # ── Single write ──────────────────────────────────────────
        try:
            client.write("ns=1;i=1004", 42)
            print("[WRITE]  Counter <- 42")

            new_value = client.read("ns=1;i=1004")
            print(f"[VERIFY] Counter = {new_value}")
        except StatusCodeError as e:
            print(f"[ERROR]  Write failed: {e}")
```

## 3. Multiple Read / Write
`client.read([...])` accepts a list and returns a list of values in
the same order; `client.write({...])` accepts a dictionary mapping each
NodeId to its new value. The SDK packs them into a single
`Read` / `Write` service request.

```python
# ── Read several variables at once ────────────────────────
try:
    values = client.read(
        [
            "ns=1;i=1001",  # Temperature (Double)
            "ns=1;i=1002",  # Pressure    (Double)
            "ns=1;i=1003",  # Status      (String)
            "ns=1;i=1004",  # Counter     (Int32)
        ]
    )
    print(f"\n[READ]   Multiple read results: {values}")
except StatusCodeError as e:
    print(f"\n[ERROR]  Multiple read failed: {e}")

# ── Write several variables at once ───────────────────────
try:
    client.write(
        {
            "ns=1;i=1001": 25.0,  # Temperature
            "ns=1;i=1003": "online",  # Status
            "ns=1;i=1004": 100,  # Counter
        }
    )
    print("[WRITE]  Multiple write successful!")
except StatusCodeError as e:
    print(f"[ERROR]  Multiple write failed: {e}")
```

## 4. Method Call
`client.call(object_id, method_id, input_args)` invokes a server-side
method. The return value is a tuple `(status_code, *output_args)`.
The first element is the per-call StatusCode, and the rest are the
declared output arguments in order.

`basic_server.py` exposes an `Add` method at `ns=1;i=2001` on the
`Plant` object. `Plant`'s NodeId is allocated dynamically at server
startup, so we resolve it by name with a single browse.

```python
# Find the Plant object once, by name.
refs = client.browse(
    "i=85",
    resultMask=63,  # ask for every reference field
)
plant_id = next(r.nodeId for r in refs if r.browseName.name == "Plant")
print(f"\n[INFO]   Plant NodeId = {plant_id}")

# Call the `Add` method on the Plant object.
try:
    result = client.call(
        plant_id,  # object_id
        "ns=1;i=2001",  # method_id (Plant / Add)
        [3.0, 4.0],  # input_args: two Doubles
    )
    status, *outputs = result
    print(f"[CALL]   Status: {status.name}, Result: {outputs}")
except Exception as e:
    print(f"[ERROR]  Method call failed: {e}")
```

## 5. Subscriptions
Polling a value in a tight loop wastes resources when nothing
is changing. A `Subscription` plus one or more `MonitoredItem`s lets
the server *publish* a notification only when a value actually changes.

The way is: create a subscription with a publishing interval
(how often the server is *allowed* to publish), register a monitored
item with a sampling interval (how often the server *checks* the
value), and provide a callback that the SDK will invoke on the
client's event-loop thread whenever a new value arrives.

```python
def on_data_change(monitored_item, value) -> None:
    """Server-pushed callback: runs on the client's event-loop thread."""
    print(f"[EVENT]  {monitored_item} -> {value}")

print("\n[INFO]   Creating subscription...")
subscription = client.createSubscription(publishingInterval=1000)

print("[INFO]   Monitoring Plant / Counter (ns=1;i=1004) ...")
monitored_item = client.monitor(
    target="ns=1;i=1004",
    callback=on_data_change,
    subscription=subscription,
    samplingInterval=500,
)

# Drive a few writes to trigger notifications.
print("[INFO]   Writing values to trigger notifications...")
for i in range(3):
    client.write("ns=1;i=1004", 200 + i)
    time.sleep(1)

print("[INFO]   Cleaning up subscription...")
monitored_item.delete()
subscription.delete()
```

## 6. Browsing the Address Space
`client[nodeid]` is a shortcut for fetching a `Node` object for a
given NodeId. The `Node` object can be
printed, used as the target of `client.browse(...)`, or read for any
of its attributes via `node(attr=AttributeId.X)`.

`client.browse(node)` walks one level out from the given node,
returning a list of `ReferenceDescription`s. The `result_mask`
keyword controls which fields each reference carries back
(browse name, display name, node class, type definition, ...). The
default is `0`; pass `63`(or `BrowseResultMask(63)`) to get every field populated.

```python
    # New `with` block — the previous one's subscription was deleted
    # and its `client` is no longer connected.
    with Client(endpoint_url) as client:
        node = client["i=85"]  # The standard `Objects` folder
        print(f"\n[BROWSE] Node         = {node}")
        print(f"[BROWSE] BrowseName   = {node(attr=AttributeId.BROWSE_NAME)}")
        print(f"[BROWSE] NodeClass    = {node(attr=AttributeId.NODE_CLASS)}")
        # (Browsing children of an ObjectNode is covered in
        # `lowlevel/client.py` — use `result_mask=63` to get names.)

except StatusCodeError as e:
    print(f"[ERROR]  Connection failed: {e}")
    print("Note:   Make sure an OPC UA server is running on localhost:4840")
    print("        (try: python examples/highlevel/basic_server.py)")

print()
print("Connection closed.")
print("=== Example completed ===")
```

## Complete Source Code

```python
#!/usr/bin/env python3
# Copyright 2026 (c) o6 Automation GmbH
"""
Client Basics: Read, Write, and Subscriptions
=============================================

Walks through the high-level ``o6.Client`` API end to end: connecting to
a server, reading and writing single and multiple values, calling a
method, subscribing to a variable for event-driven updates, and finally
introspecting the address space via ``client[NodeId]`` and ``client.browse()``.

The example is wired against `basic_server.py` so start that script in
one terminal before running this one, and it will talk to the address
space defined there (``Plant / Temperature``, ``Plant / Pressure``,
``Plant / Counter``, ``Plant / Running``, ``Plant / Add``, …).
"""


import socket
import time
from o6 import Client, StatusCodeError, AttributeId


localhost = "localhost"
endpoint_url = f"opc.tcp://{localhost}:4840"
print(f"Connecting to {endpoint_url} ...")


try:
    with Client(endpoint_url) as client:
        print("[INFO] Connected to server successfully!\n")

        # ── Single read ───────────────────────────────────────────
        try:
            value = client.read("ns=1;i=1004")  # Plant / Counter (Int32)
            print(f"[READ]   Counter = {value}")
        except StatusCodeError as e:
            print(f"[ERROR]  Read failed: {e}")

        # ── Single write ──────────────────────────────────────────
        try:
            client.write("ns=1;i=1004", 42)
            print("[WRITE]  Counter <- 42")

            new_value = client.read("ns=1;i=1004")
            print(f"[VERIFY] Counter = {new_value}")
        except StatusCodeError as e:
            print(f"[ERROR]  Write failed: {e}")


        # ── Read several variables at once ────────────────────────
        try:
            values = client.read(
                [
                    "ns=1;i=1001",  # Temperature (Double)
                    "ns=1;i=1002",  # Pressure    (Double)
                    "ns=1;i=1003",  # Status      (String)
                    "ns=1;i=1004",  # Counter     (Int32)
                ]
            )
            print(f"\n[READ]   Multiple read results: {values}")
        except StatusCodeError as e:
            print(f"\n[ERROR]  Multiple read failed: {e}")

        # ── Write several variables at once ───────────────────────
        try:
            client.write(
                {
                    "ns=1;i=1001": 25.0,  # Temperature
                    "ns=1;i=1003": "online",  # Status
                    "ns=1;i=1004": 100,  # Counter
                }
            )
            print("[WRITE]  Multiple write successful!")
        except StatusCodeError as e:
            print(f"[ERROR]  Multiple write failed: {e}")


        # Find the Plant object once, by name.
        refs = client.browse(
            "i=85",
            resultMask=63,  # ask for every reference field
        )
        plant_id = next(r.nodeId for r in refs if r.browseName.name == "Plant")
        print(f"\n[INFO]   Plant NodeId = {plant_id}")

        # Call the `Add` method on the Plant object.
        try:
            result = client.call(
                plant_id,  # object_id
                "ns=1;i=2001",  # method_id (Plant / Add)
                [3.0, 4.0],  # input_args: two Doubles
            )
            status, *outputs = result
            print(f"[CALL]   Status: {status.name}, Result: {outputs}")
        except Exception as e:
            print(f"[ERROR]  Method call failed: {e}")


        def on_data_change(monitored_item, value) -> None:
            """Server-pushed callback: runs on the client's event-loop thread."""
            print(f"[EVENT]  {monitored_item} -> {value}")

        print("\n[INFO]   Creating subscription...")
        subscription = client.createSubscription(publishingInterval=1000)

        print("[INFO]   Monitoring Plant / Counter (ns=1;i=1004) ...")
        monitored_item = client.monitor(
            target="ns=1;i=1004",
            callback=on_data_change,
            subscription=subscription,
            samplingInterval=500,
        )

        # Drive a few writes to trigger notifications.
        print("[INFO]   Writing values to trigger notifications...")
        for i in range(3):
            client.write("ns=1;i=1004", 200 + i)
            time.sleep(1)

        print("[INFO]   Cleaning up subscription...")
        monitored_item.delete()
        subscription.delete()


    # New `with` block — the previous one's subscription was deleted
    # and its `client` is no longer connected.
    with Client(endpoint_url) as client:
        node = client["i=85"]  # The standard `Objects` folder
        print(f"\n[BROWSE] Node         = {node}")
        print(f"[BROWSE] BrowseName   = {node(attr=AttributeId.BROWSE_NAME)}")
        print(f"[BROWSE] NodeClass    = {node(attr=AttributeId.NODE_CLASS)}")
        # (Browsing children of an ObjectNode is covered in
        # `lowlevel/client.py` — use `result_mask=63` to get names.)

except StatusCodeError as e:
    print(f"[ERROR]  Connection failed: {e}")
    print("Note:   Make sure an OPC UA server is running on localhost:4840")
    print("        (try: python examples/highlevel/basic_server.py)")

print()
print("Connection closed.")
print("=== Example completed ===")
```
