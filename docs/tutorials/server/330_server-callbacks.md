# Server callbacks

A passive Variable holds whatever was last written. A callback-backed Variable holds whatever the read callback returns. The simulation is the thing in the middle — the long-running process that updates the kettle temperature, advances the state machine, and pushes values into the Variables.

This page wires a periodic update loop to the distillery. By the end, the server is running a 10 Hz tick that mirrors a simulated still into the address space.

---

## Where do callbacks live?

Two places:

1. **Per-node callbacks** — `Server.implement(variable, read=..., write=...)` for Variables, `Server.implement(method, call=...)` for Methods. The [previous pages](320_variables-with-sources.md) and [method implementations](310_method-implementations.md) covered those. They run on the server's event loop.
2. **Server-wide timers** — `Server.addRepeatedCallback(...)`: These run on the loop too, but they are not bound to a node; they are *scheduled work* the server keeps firing.

The simulation's update loop is a server-wide timer. The Variable read callbacks are per-node callbacks that consult the simulation's state on every read.

---

## `addRepeatedCallback`

`addRepeatedCallback(callback, intervalMs)` registers `callback` to run every `intervalMs` milliseconds. The callback runs on the server's event loop — keep it short.

```python
import time
import o6
from o6 import Server

server = Server(port=4840)

state = {"kettle_temperature": 20.0}


def tick():
    """Advance the simulated kettle temperature by 0.1 °C per tick."""
    state["kettle_temperature"] += 0.1


callback_id = server.addRepeatedCallback(tick, 100.0)   # 100 ms = 10 Hz

server.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pass

server.stop()
```

`tick()` runs every 100 ms on the server's loop thread. It mutates a Python dict that read callbacks consult; a read of `Kettle/Temperature` sees the value walk up by 0.1 °C every tick.

`changeRepeatedCallbackInterval(callback_id, newIntervalMs)` adjusts the cadence without re-registering; `removeCallback(callback_id)` cancels it. The callback is removed automatically on shutdown, so a long-running server does not need to clean up at exit.

This section built the update loop with the same imperative Objects and Variables used throughout the tutorial so far. The next example wires the same read callback through a *declared* type instead — an `@o6.objecttype` with a Variable child and an `@o6.read(...)`-decorated method, resolved once when the Object is constructed rather than installed by hand with `Server.implement(...)`. It is a second way to reach the same per-node callback slot, documented fully on the [server manual's callbacks page](../../manual/server/callbacks.md#variables).

#### Putting it all together — the distillery's 10 Hz update loop

```python
import time
import o6
from o6 import Server, StatusCode
from o6.ns import ns0

o6.ns.namespace(
    shortname="distillery",
    uri="http://o6-automation.com/UA/Distillery/",
    version="1.0",
)


@o6.objecttype(ns="distillery", nodeId="ns=distillery;i=1000", browseName="DistillingSystemType")
class DistillingSystemType(ns0.objtypes.BaseObjectType):
    kettle_temperature: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            browseName="ns=distillery;KettleTemperature",
            nodeId="ns=distillery;i=1302",
            dataType="i=11",
            value=20.0,
            accessLevel=1,
        )
    )


class DistillingSystemImpl(DistillingSystemType):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._kettle_temperature = 20.0

    @o6.read("kettle_temperature")
    def _read_kettle_temperature(self, *, range, session, includeSourceTimestamp):
        return (StatusCode.GOOD, o6.Double(self._kettle_temperature))


server = Server(port=4840)
server.ns.append("distillery")
server.implement(DistillingSystemType, DistillingSystemImpl)
system = DistillingSystemType(parent=server.objectsNode, browseName="MainStill")


def tick():
    system._kettle_temperature += 0.1


server.addRepeatedCallback(tick, 100.0)
server.start()
```

A read of `MainStill/KettleTemperature` repeatedly sees the value climb at 1 °C / second. The same read callback handles reads at any cadence.

---

## Startup and shutdown hooks

The server runs `start()` and `stop()` itself, but a project usually wants to do additional setup between them — open a database, build a simulation state, schedule retention cleanup. The cleanest place is a context manager (`with server: ...`) or explicit start/stop:

```python
server = Server(port=4840)

# ... build the address space ...

server.addRepeatedCallback(tick, 100.0)
server.start()

# The server is now listening and the tick is firing.
# ... main work ...

server.stop()
```

For a project that wants hooks before/after `start()` runs, schedule them with `server.addRepeatedCallback(...)` on a one-shot timer — open62541's callback model treats one-shot and repeated the same, just stop the callback once it has run:

```python
def start_of_day():
    print("Server is now serving")
    server.removeCallback(start_of_day_id)

start_of_day_id = server.addRepeatedCallback(start_of_day, 1.0)
```

A 1 ms one-shot is the standard pattern for "do this as soon as the loop is up".

Retention cleanup is the same idea applied on a slower, repeating cadence — a callback that trims an in-memory buffer instead of letting it grow forever:

```python
batch_log = []   # appended elsewhere, one entry per completed batch
MAX_ENTRIES = 100


def trim_batch_log():
    """Keep only the most recent MAX_ENTRIES batches in memory."""
    del batch_log[:-MAX_ENTRIES]


server.addRepeatedCallback(trim_batch_log, 60_000.0)   # once a minute
```

`trim_batch_log` runs on the loop thread like any other repeated callback — it stays cheap because it only slices a list, never touches the network or disk.

---

## Update loop discipline

Three things matter once the loop is running:

1. **Keep callbacks short.** Every callback runs on the loop thread. A 50 ms callback that blocks the loop for 50 ms means *every other callback waits*. Move slow work to a queue, a thread, or another process.
2. **Don't block the loop on I/O.** Reading from a sensor or database should not stall incoming writes. Use `asyncio` for cooperative I/O on the loop, or a thread pool for blocking calls.
3. **Stop gracefully.** When `server.stop()` is called, the loop drains in-flight callbacks before tearing down. Long-running callbacks should still respect cancellation — see the [timers and async loops page](350_timers.md).

!!! info
    `addRepeatedCallback(callback, intervalMs)` does not guarantee the cadence — it guarantees the callback runs at least every `intervalMs` milliseconds. If a callback runs longer than the interval, the next invocation is scheduled immediately. The right mental model is "no sooner than this", not "exactly every".

---

## What's next?

The distillery's update loop is in place. The next page uses that loop to publish state transitions as events; the page after that covers scheduling work cooperatively and tying the whole thing to a real state machine.

- [Events](340_events.md) — declaring an event type, making a source, and firing real events from the update loop with `o6.Event` / `trigger()`.
- [Timers and async loops](350_timers.md) — long-running background work, `asyncio` integration, cooperative cancellation.
- [Server manual](../../manual/server/callbacks.md) — every callback type, its signature, and the resolution order between callbacks.