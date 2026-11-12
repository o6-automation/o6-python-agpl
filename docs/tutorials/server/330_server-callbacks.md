# Server callbacks

A passive Variable holds the last written value. A callback-backed Variable returns whatever its read callback returns. A simulation sits between the two: a long-running loop that updates the kettle temperature, advances the state machine and pushes values into the Variables.

On this page you add a 10 Hz update loop that mirrors a simulated still into the address space.

---

## Where do callbacks live?

1. **Per-node callbacks**: `Server.implement(variable, read=..., write=...)` for Variables and `Server.implement(method, call=...)` for Methods. See [Variables with sources](320_variables-with-sources.md) and [Method implementations](310_method-implementations.md). They run on the server's event loop.
2. **Server-wide timers**: `Server.addRepeatedCallback(...)`. These also run on the loop, but they are not bound to a node. They are scheduled work that the server fires repeatedly.

The simulation's update loop is a server-wide timer. The Variable read callbacks are per-node callbacks that read the simulation state on every read.

---

## `addRepeatedCallback`

`addRepeatedCallback(callback, intervalMs)` registers `callback` to run every `intervalMs` milliseconds. The callback runs on the server's event loop, so keep it short.

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

`tick()` runs every 100 ms on the server's loop thread. It mutates a dict that read callbacks consult, so a read of `Kettle/Temperature` sees the value rise by 0.1 °C per tick.

- `changeRepeatedCallbackInterval(callback_id, newIntervalMs)` changes the interval without re-registering.
- `removeCallback(callback_id)` cancels the callback.
- The server removes the callback on shutdown, so you don't need to clean up at exit.

The next example uses a declared type instead of imperative Objects and Variables: an `@o6.objecttype` with a Variable child and an `@o6.read(...)`-decorated method. The read callback is resolved once when the Object is constructed, instead of being installed with `Server.implement(...)`. Both routes fill the same per-node callback slot; see the [server manual's callbacks page](../../manual/server/callbacks.md#variables).

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

Reads of `MainStill/KettleTemperature` see the value climb at 1 °C per second, whatever the read rate.

---

## Startup and shutdown hooks

Put project setup, such as opening a database, building simulation state or scheduling retention cleanup, between explicit `start()` and `stop()` calls or inside a context manager (`with server: ...`):

```python
server = Server(port=4840)

# ... build the address space ...

server.addRepeatedCallback(tick, 100.0)
server.start()

# The server is now listening and the tick is firing.
# ... main work ...

server.stop()
```

For a hook that runs once the loop is up, register a repeated callback that removes itself after its first run. open62541 treats one-shot and repeated callbacks the same way:

```python
def start_of_day():
    print("Server is now serving")
    server.removeCallback(start_of_day_id)

start_of_day_id = server.addRepeatedCallback(start_of_day, 1.0)
```

A 1 ms one-shot is the standard pattern for "do this as soon as the loop is up".

Retention cleanup uses a slower repeated callback that trims an in-memory buffer so it doesn't grow without bound:

```python
batch_log = []   # appended elsewhere, one entry per completed batch
MAX_ENTRIES = 100


def trim_batch_log():
    """Keep only the most recent MAX_ENTRIES batches in memory."""
    del batch_log[:-MAX_ENTRIES]


server.addRepeatedCallback(trim_batch_log, 60_000.0)   # once a minute
```

`trim_batch_log` runs on the loop thread. It stays cheap because it only slices a list and never touches the network or disk.

---

## Update loop discipline

1. **Keep callbacks short.** Every callback runs on the loop thread. A callback that takes 50 ms blocks every other callback for 50 ms. Move slow work to a queue, a thread or another process.
2. **Don't block the loop on I/O.** A sensor or database read must not stall incoming writes. Use `asyncio` for cooperative I/O on the loop, or a thread pool for blocking calls.
3. **Stop gracefully.** `server.stop()` drains in-flight callbacks before teardown. Long-running callbacks must still respect cancellation; see [Timers and async loops](350_timers.md).

!!! info
    `intervalMs` is not an exact cadence. If a callback runs longer than the interval, the next invocation is scheduled immediately. Read the interval as "no sooner than this", not "exactly every".

---

## Next steps

| Topic | What it covers |
|---|---|
| [Events](340_events.md) | Declaring an event type, making a source, and firing real events from the update loop with `o6.Event` / `trigger()`. |
| [Timers and async loops](350_timers.md) | Long-running background work, `asyncio` integration, cooperative cancellation. |
| [Server manual](../../manual/server/callbacks.md) | Every callback type, its signature, and the resolution order between callbacks. |
