# Server Variables Example

Source example: `examples/highlevel/server_variables.py`

This example focuses on variables only.

## Explanation

### Creating variables

```python
temperature = server.add_variable("Temperature", server.objects_node, 22.5, nodeid="ns=1;i=1001")
pressure = server.add_variable("Pressure", server.objects_node, 1013.25, nodeid="ns=1;i=1002")
```

### Read-only variables

`FirmwareVersion` is created with `writable=False`, which keeps it visible to clients but not writable.

```python
firmware_version = server.add_variable(
    "FirmwareVersion",
    server.objects_node,
    "v2.1.0",
    nodeid="ns=1;i=1005",
    writable=False,
)
```

### Updating variables


```python
temperature.value = 22.5 + (cycle % 50) * 0.1
pressure.value = 1013.25 + (cycle % 20) * 0.5
is_running.value = cycle % 30 != 0
```

## Full source

```python
#!/usr/bin/env python3

import time
from o6 import Server


def main():
    server = Server(port=4840)

    temperature = server.add_variable(
        "Temperature",
        server.objects_node,
        22.5,
        nodeid="ns=1;i=1001",
    )

    pressure = server.add_variable(
        "Pressure",
        server.objects_node,
        1013.25,
        nodeid="ns=1;i=1002",
    )

    machine_name = server.add_variable(
        "MachineName",
        server.objects_node,
        "CNC-Mill-01",
        nodeid="ns=1;i=1003",
    )

    is_running = server.add_variable(
        "IsRunning",
        server.objects_node,
        False,
        nodeid="ns=1;i=1004",
    )

    firmware_version = server.add_variable(
        "FirmwareVersion",
        server.objects_node,
        "v2.1.0",
        nodeid="ns=1;i=1005",
        writable=False,
    )

    server.start()
    print("Server running at opc.tcp://localhost:4840")
    print("Press Ctrl+C to stop.\n")

    try:
        cycle = 0
        while True:
            cycle += 1

            temperature.value = 22.5 + (cycle % 50) * 0.1
            pressure.value = 1013.25 + (cycle % 20) * 0.5
            is_running.value = cycle % 30 != 0

            if cycle % 10 == 0:
                print(
                    f"  Cycle {cycle}: "
                    f"Temp={temperature.value:.1f}°C, "
                    f"Pressure={pressure.value:.1f}hPa, "
                    f"Running={is_running.value}"
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