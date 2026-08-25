Server Tutorial: Objects and Type Hierarchy
===========================================

Demonstrates how to organise a server's address space with object
nodes, define a custom ``ObjectType`` as a reusable template, and
declare a custom ``VariableType``. The result is a small "Plant"
hierarchy with two child devices and one sensor instantiated from
the custom type.

Start any OPC UA client (e.g. ``opcua_browser.py`` or
``client_browsing.py``) against this server to see the hierarchy.

`Server.addObject()` is the high-level way to add an `Object` to
the address space. `name` is the displayed name and `parent` is
the NodeId of the enclosing object. Passing an explicit `nodeid`
keeps the layout predictable across runs — without it the server
assigns numeric ids in the order calls are made.

## 1. Object hierarchy
Build a small "Plant" tree: two child devices (`Oven` and
`Conveyor`) each with two `Variable` children. Every node
gets an explicit `nodeid` in namespace 1 so client examples
can reference them by string.

```python
plant = server.addObject(name="Plant", parent=server.objectsNode, nodeId="ns=1;i=100")

oven = server.addObject("Oven", plant, nodeId="ns=1;i=110")
oven_temp = server.addVariable("Temperature", oven, 180.0, nodeId="ns=1;i=111")
oven_heater = server.addVariable("HeaterOn", oven, True, nodeId="ns=1;i=112")

conveyor = server.addObject("Conveyor", plant, nodeId="ns=1;i=120")
conveyor_speed = server.addVariable("Speed", conveyor, 1.5, nodeId="ns=1;i=121")
conveyor_running = server.addVariable("IsRunning", conveyor, False, nodeId="ns=1;i=122")
```

## 2. Custom ObjectType
`add_object_type()` returns a type node. Adding Variables to
it gives those variables to every object you later instantiate
with `typeDefinition=...`. Clients reading the type
definition discover what fields to expect. The main benefits:
reuse the layout across many devices, let clients
auto-discover "all sensors" by following `HasTypeDefinition`
backwards, and carry data-type/units metadata once on the
type instead of on every instance.

```python
sensor_type = server.addObjectType("SensorType", nodeId="ns=1;i=200")
server.addVariable("Value", sensor_type, 0.0, nodeId="ns=1;i=201")
server.addVariable("Unit", sensor_type, "", nodeId="ns=1;i=202", writable=False)

humidity_sensor = server.addObject(
    "HumiditySensor",
    oven,
    nodeId="ns=1;i=130",
    typeDefinition=sensor_type.nodeId,
)
server.addVariable("Value", humidity_sensor, 45.0, nodeId="ns=1;i=131")
server.addVariable("Unit", humidity_sensor, "%RH", nodeId="ns=1;i=132", writable=False)
```

## 3. Custom VariableType
`add_variable_type()` registers a new VariableType node. It is
useful when a value needs units, range, or engineering-meta
data attached. Clients can read this type by its NodeId.

```python
server.addVariableType(
    "TemperatureType",
    dataType="i=11",  # Double
    nodeId="ns=1;i=300",
)
```

## 4. Run and simulation loop
`server.start()` blocks until `server.stop()`. The wrapper
assigns new values to the `Variable` handles once per second
so any client can watch the values change live.

```python
    server.start()
    print(f"Server running at {endpoint_url}")
    print("Press Ctrl+C to stop.\n")

    try:
        cycle = 0
        while True:
            cycle += 1
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
```

## Complete Source Code

```python
#!/usr/bin/env python3
# Copyright 2026 (c) o6 Automation GmbH (Author: Andreas Ebner)
"""
Server Tutorial: Objects and Type Hierarchy
===========================================

Demonstrates how to organise a server's address space with object
nodes, define a custom ``ObjectType`` as a reusable template, and
declare a custom ``VariableType``. The result is a small "Plant"
hierarchy with two child devices and one sensor instantiated from
the custom type.

Start any OPC UA client (e.g. ``opcua_browser.py`` or
``client_browsing.py``) against this server to see the hierarchy.
"""

import socket
import time
from o6 import Server



def main():
    localhost = "localhost"
    endpoint_url = f"opc.tcp://{localhost}:4840"

    server = Server(port=4840)


    plant = server.addObject(name="Plant", parent=server.objectsNode, nodeId="ns=1;i=100")

    oven = server.addObject("Oven", plant, nodeId="ns=1;i=110")
    oven_temp = server.addVariable("Temperature", oven, 180.0, nodeId="ns=1;i=111")
    oven_heater = server.addVariable("HeaterOn", oven, True, nodeId="ns=1;i=112")

    conveyor = server.addObject("Conveyor", plant, nodeId="ns=1;i=120")
    conveyor_speed = server.addVariable("Speed", conveyor, 1.5, nodeId="ns=1;i=121")
    conveyor_running = server.addVariable("IsRunning", conveyor, False, nodeId="ns=1;i=122")


    sensor_type = server.addObjectType("SensorType", nodeId="ns=1;i=200")
    server.addVariable("Value", sensor_type, 0.0, nodeId="ns=1;i=201")
    server.addVariable("Unit", sensor_type, "", nodeId="ns=1;i=202", writable=False)

    humidity_sensor = server.addObject(
        "HumiditySensor",
        oven,
        nodeId="ns=1;i=130",
        typeDefinition=sensor_type.nodeId,
    )
    server.addVariable("Value", humidity_sensor, 45.0, nodeId="ns=1;i=131")
    server.addVariable("Unit", humidity_sensor, "%RH", nodeId="ns=1;i=132", writable=False)


    server.addVariableType(
        "TemperatureType",
        dataType="i=11",  # Double
        nodeId="ns=1;i=300",
    )


    server.start()
    print(f"Server running at {endpoint_url}")
    print("Press Ctrl+C to stop.\n")

    try:
        cycle = 0
        while True:
            cycle += 1
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
```
