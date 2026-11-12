# Data Source Updates

Drives a Variable's value from an external process model. The "real"
value lives in plain Python state, and `server.write()` copies it into
the address space whenever it changes.

The high-level API has no separate value-callback or data-source object
for this. The loop below writes after every state change, which does
what a callback would do.

`ProcessModel` holds the "real" value outside the address space, like a
sensor driver or simulation. `tick()` advances it. `read_temperature()`
is the read side, a separate method so the sampling points below are
easy to spot.

```python
class ProcessModel:
    def __init__(self) -> None:
        self._temperature = 20.0

    def tick(self) -> None:
        self._temperature += 0.05

    def read_temperature(self) -> float:
        return self._temperature
```

## 1. Seed the variable
The initial value comes from the process model, so the Variable starts
in sync with the "real" state instead of at zero.

```python
print("--- 1. Seed the variable ---")
temp_node = server.addVariable(
    "ProcessTemperature",
    server.objectsNode,
    process.read_temperature(),
    nodeId="ns=1;s=ProcessTemperature",
)
print(f"Temperature = {server.read(temp_node)}")
```

## 2. Manual updates
Each tick advances the process model, then `server.write()` copies the
new value into the address space. Subscribed clients see it on the next
publish. The address space is only as fresh as the last write.

```python
print("\n--- 2. Manual updates ---")
for _ in range(5):
    process.tick()
    server.write(temp_node, process.read_temperature()).check()
    print(f"Temperature = {server.read(temp_node)}")
    time.sleep(0.2)
```

## Source Code

Download [`S07_data_source.py`](server-S07_data_source/S07_data_source.py) to run it locally.
