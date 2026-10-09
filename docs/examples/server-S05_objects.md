# Objects

Demonstrates how to organise a server's address space with object
nodes, define a custom ``ObjectType`` as a reusable template, and
declare a custom ``VariableType``. The result is a small "Plant"
hierarchy with two child devices and one sensor instantiated from
the custom type.

Start any OPC UA client (e.g. ``C02_firststeps.py`` or
``C03_browsing.py``) against this server to see the hierarchy.

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
print("--- 1. Object Hierarchy ---")

plant = server.addObject(name="Plant", parent=server.objectsNode, nodeId="ns=1;i=100")

oven = server.addObject("Oven", plant, nodeId="ns=1;i=110")
oven_temp = server.addVariable("Temperature", oven, 180.0, nodeId="ns=1;i=111")
oven_heater = server.addVariable("HeaterOn", oven, True, nodeId="ns=1;i=112")

conveyor = server.addObject("Conveyor", plant, nodeId="ns=1;i=120")
conveyor_speed = server.addVariable("Speed", conveyor, 1.5, nodeId="ns=1;i=121")
conveyor_running = server.addVariable("IsRunning", conveyor, False, nodeId="ns=1;i=122")
```

## 2. Custom ObjectType
`addObjectType()` creates a type definition. Instances refer to it
through `typeDefinition`; clients can inspect its declarations.
Child declarations require modelling rules for automatic instantiation.
This example explicitly creates the Value and Unit children on the instance.

```python
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
```

## 3. Custom VariableType
`addVariableType()` registers a new VariableType node. It is
useful when a value needs units, range, or engineering-meta
data attached. Clients can read this type by its NodeId.

```python
print()
print("--- 3. Custom VariableType ---")

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
```

## Source Code

Download [`S05_objects.py`](server-S05_objects/S05_objects.py) to run it locally.
