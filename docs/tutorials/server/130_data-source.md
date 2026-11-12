# Values from an external source

So far each Variable holds whatever was last written to it, which suits a setting such as `Setpoint`. A reading such as `Kettle/Temperature` comes from the still itself. This page keeps that value in a Python model outside the address space and pushes it into the Variable.

The page uses a fresh server, not the one from the previous pages. [Variables with sources](320_variables-with-sources.md) applies the same idea to the running distillery.

---

## Keep the real value outside the address space

Keep two parts separate: a plain Python object that models the process, and the OPC UA Variable that reports on it. `KettleModel` has no OPC UA code:

```python
class KettleModel:
    """Stands in for the kettle's actual temperature sensor."""

    def __init__(self) -> None:
        self._temperature = 20.0

    def tick(self) -> None:
        """Advance one simulated step, heating up a little."""
        self._temperature += 0.5

    def read_temperature(self) -> float:
        return self._temperature
```

A plain model is easy to test on its own, to swap for a real sensor driver and to reuse from a client-side script. Mixing OPC UA into the class loses all three.

---

## Seed the Variable, then push updates

Create the Variable as usual, with its initial value taken from the model:

```python
import time
from o6 import Server

server = Server(port=4840)
sys = server.addObject("DistillingSystem", server.objectsNode, nodeId="ns=1;i=1000")
kettle = server.addObject("Kettle", sys, nodeId="ns=1;i=1300")

model = KettleModel()
temperature = server.addVariable(
    "Temperature",
    kettle,
    model.read_temperature(),   # seed with the model's current value
    nodeId="ns=1;i=1302",
    writable=False,
)
server.start()

try:
    while True:
        model.tick()
        server.write(temperature, model.read_temperature())
        print(f"Kettle temperature = {server.read(temperature):.1f} °C")
        time.sleep(0.5)
except KeyboardInterrupt:
    pass

server.stop()
```

Each iteration advances the model and writes the new reading with `server.write(...)`. A client subscribed to `Kettle/Temperature` receives each write as a data-change notification, as it would from a real sensor.

!!! info
    Keep `writable=False`. Only the model may change this value; the
    read-only access level stops a client from overwriting the simulated
    reading.

#### Putting it all together

```python
import time
from o6 import Server


class KettleModel:
    def __init__(self) -> None:
        self._temperature = 20.0

    def tick(self) -> None:
        self._temperature += 0.5

    def read_temperature(self) -> float:
        return self._temperature


model = KettleModel()

server = Server(port=4840)
sys = server.addObject("DistillingSystem", server.objectsNode, nodeId="ns=1;i=1000")
kettle = server.addObject("Kettle", sys, nodeId="ns=1;i=1300")
temperature = server.addVariable(
    "Temperature", kettle, model.read_temperature(), nodeId="ns=1;i=1302", writable=False
)
server.start()

try:
    while True:
        model.tick()
        server.write(temperature, model.read_temperature())
        time.sleep(0.5)
except KeyboardInterrupt:
    pass

server.stop()
```

The `server.py` from [Set the stage](../setup.md) works the same way: its loop ticks a larger simulation and mirrors it into every Variable under `DistillingSystem` with `server.write(...)`.

---

## Next steps

With explicit `server.write(...)` calls, the loop that owns the model must push every value on every tick. [Variables with sources](320_variables-with-sources.md) installs a read callback instead, so each read consults the model directly.

| Topic | What it covers |
|---|---|
| [Running on asyncio](140_async-server.md) | The same kind of update loop, running cooperatively instead of blocking a thread. |
| [Variables with sources](320_variables-with-sources.md) | The callback-based alternative to explicit `server.write(...)`. |
| [Server Data Source Updates](../../examples/server-S07_data_source.md) | The runnable example this page is based on. |
