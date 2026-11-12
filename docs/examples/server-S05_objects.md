# Objects

Organizes a server's address space with object nodes, defines a custom
``ObjectType`` as a reusable template and declares a custom
``VariableType``. The result is a small "Plant" hierarchy with two
child devices and one sensor instantiated from the custom type.

Run any OPC UA client (for example ``C02_firststeps.py`` or
``C03_browsing.py``) against this server to see the hierarchy.

`Server.addObject()` adds an `Object` to the address space. `name` is
its BrowseName and DisplayName, `parent` the enclosing node. An
explicit `nodeId` keeps the layout the same across runs. Without it the
server assigns a numeric id in its namespace 1.

## 1. Object hierarchy
A "Plant" tree with two child devices (`Oven` and `Conveyor`), each
with two `Variable` children. Every node has an explicit `nodeId` in
namespace 1, so client examples can refer to it by string.

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
Child declarations are instantiated automatically only when they have
modelling rules. This example creates the Value and Unit children on
the instance explicitly.

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
`addVariableType()` adds a VariableType node. Use one to attach units,
a range or other engineering metadata to a value. Clients can read the
type by its NodeId.

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
`server.start()` returns once the listeners are ready; a background
thread drives I/O until `server.stop()`. The loop assigns new values
to the `Variable` handles once per second.

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
