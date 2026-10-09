# Data Source Updates

Demonstrates driving a Variable's value from an external process model
instead of assigning a constant. The pattern is: keep the "real" value in
plain Python state, and push it into the address space with `server.write()`
whenever it changes.

Note: the high-level API models this through explicit read/write rather
than a separate value-callback/data-source object — the loop below writes
after every state change, which is what a callback would have done for you.

`ProcessModel` holds the "real" value outside the address space, the way a
sensor driver or simulation would. `tick()` advances it; `read_temperature()`
is the read side, kept as its own method so the sampling points below stay
obvious even though the high-level API has no separate callback slot to
plug it into.

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
The initial value comes straight from the process model, so the
Variable starts in sync with the "real" state instead of at zero.

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
Each tick advances the process model, then `server.write()` pushes
the new value into the address space; any subscribed client sees
it on the next publish. This explicit write is what stands in for
a value callback: the address space is only ever as fresh as the
last write.

```python
print("\n--- 2. Manual updates ---")
for _ in range(5):
    process.tick()
    server.write(temp_node, process.read_temperature())
    print(f"Temperature = {server.read(temp_node)}")
    time.sleep(0.2)
```

## Source Code

Download [`S07_data_source.py`](server-S07_data_source/S07_data_source.py) to run it locally.
