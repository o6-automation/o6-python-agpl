# Values from an external source

Every Variable built so far holds whatever was last written to it — an operator sets `Setpoint`, the server stores it, a read hands it back. That's the right shape for a setting, but not for a reading. The distillery's `Kettle/Temperature` doesn't work like `Setpoint` at all: nobody writes it, because there's nothing to write to it — the number comes from the still itself. This page is about that other shape: a value whose truth lives outside the address space, in a small Python model, and gets pushed in rather than stored.

This page is a short detour from the main build — it uses a fresh, throwaway server rather than continuing the exact one from the last few pages, so it's a good place to try the idea out without worrying about the rest of the distillery. The pattern it shows comes back for real once we reach [Variables with sources](320_variables-with-sources.md), much later, where it's this same idea, wired directly into the running distillery.

---

## Keep the real value outside the address space

The pattern has two halves that stay deliberately separate: a plain Python object that *is* the process, and the OPC UA Variable that reports on it. Nothing about `KettleModel` below knows OPC UA exists — it just tracks a number and advances it:

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

Keeping the model this plain is worth the small extra step: it's trivial to test on its own, easy to swap for a real sensor driver later, and just as easy to reuse from a client-side script — none of which is true once OPC UA is mixed into the same class.

---

## Seed the Variable, then push updates

The Variable is created the same way as any other, except its initial value comes from the model instead of a literal:

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

Every iteration does the same two things: advance the model, then `server.write(...)` the new reading into the Variable. Any client with a subscription open on `Kettle/Temperature` sees each of those writes as a data-change notification — from the outside, this looks exactly like a real sensor reporting in, even though nothing more than a Python loop is behind it.

!!! info
    `writable=False` still matters here. The model, not an incoming write, is the only thing allowed to move this value — the read-only access level is what stops a client from overwriting the simulated reading with something else.

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

This is, in miniature, exactly what the real distillery server does: [Set the stage](../setup.md)'s `server.py` runs a loop that ticks a much bigger simulation and mirrors its state into the address space with the same `server.write(...)` calls, just for every Variable under `DistillingSystem` instead of one.

---

## What's next?

Explicit `server.write(...)` calls work, but they mean remembering to push every value on every tick, by hand, from whatever loop happens to own the model. [Variables with sources](320_variables-with-sources.md) shows the more automatic alternative, once we get there: installing a read callback so a read always consults the model directly, with no push step at all.

- [Running on asyncio](140_async-server.md) — the same kind of update loop, running cooperatively instead of blocking a thread.
- [Variables with sources](320_variables-with-sources.md) — the callback-based alternative to explicit `server.write(...)`.
- [Server Data Source Updates](../../examples/server-S07_data_source.md) — the runnable example this page is based on.
