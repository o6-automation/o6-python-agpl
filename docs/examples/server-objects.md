# Server Objects and Types Example

Source example: `examples/highlevel/server_objects.py`

This example focuses on server object structure.

## Explanation

### Nested object hierarchy


```python
plant = server.addObject("Plant", server.objectsNode, nodeId="ns=1;i=100")
oven = server.addObject("Oven", plant, nodeId="ns=1;i=110")
conveyor = server.addObject("Conveyor", plant, nodeId="ns=1;i=120")
```

### Creating object types

```python
sensor_type = server.addObjectType("SensorType", nodeId="ns=1;i=200")
server.addVariable("Value", sensor_type, 0.0, nodeId="ns=1;i=201")
server.addVariable("Unit", sensor_type, "", nodeId="ns=1;i=202", writable=False)
```

### Instantiating from a type definition


```python
humidity_sensor = server.addObject(
    "HumiditySensor",
    oven,
    nodeId="ns=1;i=130",
    typeDefinition=sensor_type.nodeId,
)
```

## Full source

```python
#!/usr/bin/env python3

import time
from o6 import Server


def main():
    server = Server(port=4840)

    plant = server.addObject("Plant", server.objectsNode, nodeId="ns=1;i=100")

    oven = server.addObject("Oven", plant, nodeId="ns=1;i=110")
    oven_temp = server.addVariable("Temperature", oven, 180.0, nodeId="ns=1;i=111")
    oven_heater = server.addVariable("HeaterOn", oven, True, nodeId="ns=1;i=112")

    conveyor = server.addObject("Conveyor", plant, nodeId="ns=1;i=120")
    conveyor_speed = server.addVariable("Speed", conveyor, 1.5, nodeId="ns=1;i=121")
    conveyor_running = server.addVariable(
        "IsRunning", conveyor, False, nodeId="ns=1;i=122"
    )

    sensor_type = server.addObjectType(
        "SensorType",
        nodeId="ns=1;i=200",
    )
    server.addVariable("Value", sensor_type, 0.0, nodeId="ns=1;i=201")
    server.addVariable("Unit", sensor_type, "", nodeId="ns=1;i=202", writable=False)

    humidity_sensor = server.addObject(
        "HumiditySensor",
        oven,
        nodeId="ns=1;i=130",
        typeDefinition=sensor_type.nodeId,
    )
    server.addVariable("Value", humidity_sensor, 45.0, nodeId="ns=1;i=131")
    server.addVariable(
        "Unit", humidity_sensor, "%RH", nodeId="ns=1;i=132", writable=False
    )

    temperature_type = server.addVariableType(
        "TemperatureType",
        dataType="i=11",
        nodeId="ns=1;i=300",
    )

    server.start()
    print("Server running at opc.tcp://localhost:4840")
    print("Press Ctrl+C to stop.\n")
    print("Address space outline:")
    print("  Objects/")
    print("    └─ Plant/")
    print("         ├─ Oven/  (Temperature, HeaterOn, HumiditySensor)")
    print("         └─ Conveyor/  (Speed, IsRunning)")
    print()

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