# Async Clients

`Client` in `o6` is *dual-mode*. The same `connect()` / `disconnect()` calls work from synchronous code, from an `async` coroutine, or from a thread that owns its own event loop. What changes is whether you `await` the call and which event loop the client uses. This page covers the async side.

It assumes you have read [Connect / disconnect](100_connect.md), which covers construction and the connect/disconnect cycle.

---

## Awaiting `connect()` and `disconnect()`

In async code, `connect()` and `disconnect()` are coroutines. Call them with `await`:

```python
import asyncio
from o6 import Client

async def main():
    client = Client("opc.tcp://localhost:4840")
    await client.connect()
    try:
        print(client.connected)   # True
        # ... do work ...
    finally:
        await client.disconnect()

asyncio.run(main())
```

The `finally` block disconnects even if the body raises, the same contract as the synchronous `with` form.

---

## `async with` — the async context manager

`Client` is also an async context manager. `async with` calls `await client.connect()` on entry and `await client.disconnect()` on exit, including on exceptions. Use it inside an event loop whenever you perform more than one or two operations:

```python
import asyncio
from o6 import Client

async def main():
    async with Client("opc.tcp://localhost:4840") as client:
        print(client.connected)   # True
        # ... do work ...

    # disconnected automatically here, even if the body raised

asyncio.run(main())
```

---

## Controlling the event loop

`Client` runs a worker thread that holds an `asyncio` event loop. Every synchronous call (`client.read(...)`, `client.write(...)`, `client.monitor(...)`, …) runs on that loop and blocks the caller until the result is ready. You choose the loop at construction time.

### Let `o6` create one for you — the default

Without a `loop` argument, the client creates and owns its loop and tears it down on `disconnect()`. Use this for plain scripts, notebooks that don't use asyncio, and REPL experiments.

```python
from o6 import Client

client = Client("opc.tcp://localhost:4840")
# o6 created a fresh loop behind the scenes; you do not interact with it.
```

> **IPython / Jupyter:** `Client(url)` detects the IPython environment and gives the client its own loop, so synchronous `client.read(...)` calls don't interfere with the kernel's loop.

### Pass an external loop you manage yourself

Use this for long-running services that share one event loop across many subsystems. `o6` does not start or stop this loop; you drive it. In a service, you usually run it on a thread you own. The synchronous calls then work as they do with the default loop:

```python
import asyncio
import threading
from o6 import Client

loop = asyncio.new_event_loop()
runner = threading.Thread(target=loop.run_forever, daemon=True)
runner.start()

client = Client("opc.tcp://localhost:4840", loop=loop)
client.connect()
print(client.read("ns=1;i=1201"))   # Status/State

# ... later, when shutting down the service:
client.disconnect()
loop.call_soon_threadsafe(loop.stop)
runner.join(timeout=5)
loop.close()
```

!!! warning "The loop has to actually run for callbacks to arrive"
    If you hand over a loop that nobody drives, `o6` falls back to running each
    synchronous call inline (`loop.run_until_complete(...)`), so `connect()`,
    `read()` and `write()` still return values. Anything that arrives between
    your calls does not: subscription callbacks, event callbacks and state-change
    callbacks are only delivered while the loop is running. Start the loop —
    on its own thread as above, or via `run_until_complete` around your own
    coroutine as in the next section — before relying on any of them.

Don't wrap `connect()` in `run_until_complete`. Outside a coroutine, `connect()` is a blocking call: in `loop.run_until_complete(client.connect())`, `connect()` has already finished and returned `None` before `run_until_complete` runs. Call it synchronously, as above, or `await` it from a coroutine running on that loop.

### Use the currently running loop

Inside a coroutine, pass `asyncio.get_running_loop()` to share the running loop with the client. Use this for async services that interleave OPC UA calls with other async work:

```python
import asyncio
from o6 import Client

async def main():
    async with Client("opc.tcp://localhost:4840", loop=asyncio.get_running_loop()) as client:
        state = await client.read("ns=1;i=1201")   # Status/State
        print(state)

asyncio.run(main())
```