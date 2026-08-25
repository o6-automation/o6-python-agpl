# Async Clients

`Client` in `o6` is *dual-mode*: the same `connect()` / `disconnect()` calls work from plain synchronous code, from inside an `async` coroutine, or from a thread that owns its own event loop. The only thing that changes between those worlds is whether you `await` the call and which event loop the client uses behind the scenes. This page walks through the async side of that story.

This page assumes you have read [Connect / disconnect](100_connect.md) first — the basic construction and connect/disconnect cycle is covered there, and only the async-specific bits live here.

---

## Awaiting `connect()` and `disconnect()`

In async code, `connect()` and `disconnect()` are coroutines. You call them with `await` instead of blocking:

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

If the body of `try` raises, the `finally` block still runs `await client.disconnect()`, which is the same contract as the synchronous `with` form — just spelled out longhand.

---

## `async with` — the async context manager

`Client` is also an async context manager. The `async with` block calls `await client.connect()` on entry and `await client.disconnect()` on exit, including on exceptions. This is the recommended shape whenever you're inside an event loop and have more than one or two operations to perform:

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

`Client` runs a worker thread that holds an `asyncio` event loop. Every synchronous call (`client.read(...)`, `client.write(...)`, `client.monitor(...)`, …) dispatches onto that loop and blocks the caller until the result is ready. The choice of *which* loop the worker uses is made at construction time, and you have several options.

### Let `o6` create one for you — the default

When no loop is passed, the client creates its own loop, owns it, and tears it down on `disconnect()`. This is the right choice for plain scripts, notebooks that do not use asyncio at all, and one-off REPL experiments.

```python
from o6 import Client

client = Client("opc.tcp://localhost:4840")
# o6 created a fresh loop behind the scenes; you do not interact with it.
```

> **IPython / Jupyter:** the same `Client(url)` constructor automatically detects the IPython environment and gives the client its own loop, so synchronous `client.read(...)` calls do not interfere with the IPython kernel's loop.

### Pass an external loop you manage yourself

Useful for long-running services that own an event loop and want to share it across many subsystems. `o6` will *not* start or stop this loop — that is your responsibility.

```python
import asyncio
from o6 import Client

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

client = Client("opc.tcp://localhost:4840", loop=loop)
client.connect()
# ... later, when shutting down the service:
client.disconnect()
loop.close()
```

### Use the currently running loop

When you're already inside a coroutine and want the client to share the loop you're running on, hand it `asyncio.get_running_loop()`. This is the cleanest pattern for async services that interleave OPC UA calls with other async work:

```python
import asyncio
from o6 import Client

async def main():
    async with Client("opc.tcp://localhost:4840", loop=asyncio.get_running_loop()) as client:
        state = await client.read("ns=1;i=1201")   # Status/State
        print(state)

asyncio.run(main())
```