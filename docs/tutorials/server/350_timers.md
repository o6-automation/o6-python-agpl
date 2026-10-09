# Timers and async loops

The distillery's update loop runs at 10 Hz from `Server.addRepeatedCallback(tick, 100.0)`. The same callbacks also accept `async def` — the server runs them on its asyncio event loop, and `await` inside them is cooperative: while the callback is waiting, the rest of the loop keeps running.

[Running on asyncio](140_async-server.md), earlier in these tutorials, covers the basics — `async with server:`, `await asyncio.sleep(...)`, `asyncio.run(...)`. This page is the deeper version: long-running work that shouldn't block the loop, and cancelling cleanly on shutdown.

This page covers the three things you actually do with timers:

- `async def` callbacks for cooperative I/O.
- Long-running background work that should not block the loop.
- Cooperative cancellation on `server.stop()`.

---

## Async callbacks

`addRepeatedCallback` accepts a plain function or an `async def`. The two have the same result semantics; an `async def` callback can `await` other coroutines, run other tasks, or hand work to a worker pool.

```python
import asyncio
import time
import o6
from o6 import Server

server = Server(port=4840)


async def poll_sensor():
    """Read from an async sensor driver and push the value."""
    value = await read_sensor_async()      # cooperative I/O
    (await server.write("ns=1;i=1701", value)).check()


server.addRepeatedCallback(poll_sensor, 1000.0)   # every 1 s, as a coroutine
server.start()
```

`poll_sensor` runs on the server's event loop, and `await read_sensor_async()` yields control until the I/O completes. Other callbacks (variable reads, method calls, the listener socket) get their turn in the meantime.

Method, Variable read/write, and timer callbacks may all be `async def`.
Await dual-mode API calls inside them. Synchronous callbacks retain immediate
local results; a callback that needs pending work on the same loop must yield
control by becoming asynchronous and awaiting that work.

The `async with server` block puts the server on the same loop as your `asyncio.run(main())`:

```python
import asyncio
import o6
from o6 import Server

async def main():
    server = Server(port=4840)
    temperature = await server.addVariable("Temperature", server.objectsNode, 22.5)
    async with server:
        i = 0
        while True:
            await asyncio.sleep(1)
            i += 1
            await temperature(22.5 + i * 0.1)


asyncio.run(main())
```

`async with` enters the loop-bound lifecycle. `await asyncio.sleep(1)` is non-blocking — the loop continues to run while the sleep is in flight.

#### Putting it all together

```python
import asyncio
import o6
from o6 import Server


async def main():
    server = Server(port=4840)
    temperature = await server.addVariable("Temperature", server.objectsNode, 22.5)

    async with server:
        i = 0
        while True:
            await asyncio.sleep(1)
            i += 1
            await temperature(22.5 + i * 0.1)


try:
    asyncio.run(main())
except KeyboardInterrupt:
    pass
```

`asyncio.run` is the entry point that drives the event loop and manages the lifecycle of the main task. `KeyboardInterrupt` on the main thread cancels the main task; the `async with` block runs `server.stop()` on exit.

---

## Long-running work

A callback that takes longer than the polling interval is a footgun. Two solutions:

1. **Cooperative I/O with `asyncio`.** The right answer for I/O that has an async API — a database driver, a serial port, an HTTP client.
2. **Thread pool executor.** The right answer for I/O that is intrinsically blocking — a legacy C library, a synchronous database driver.

```python
import asyncio
import concurrent.futures
from o6 import Server

server = Server(port=4840)
pool = concurrent.futures.ThreadPoolExecutor(max_workers=2)


def blocking_read():
    """Read from a synchronous driver."""
    return sensor.read()


async def poll():
    loop = asyncio.get_running_loop()
    value = await loop.run_in_executor(pool, blocking_read)
    (await server.write("ns=1;i=1701", value)).check()


server.addRepeatedCallback(poll, 1000.0)
```

`loop.run_in_executor(pool, fn)` runs `fn` on the thread pool, returning a coroutine the loop awaits. The main loop stays responsive while the blocking call runs on a worker thread.

!!! warning
    A *plain* `time.sleep(1)` inside a callback blocks the loop. Use `await asyncio.sleep(1)` (cooperative) or `loop.run_in_executor(...)` (offloaded to a thread). A pure synchronous callback that does I/O with no `await` will stall every other callback until it returns.

---

## Cancellation on stop

`server.stop()` drains in-flight callbacks before tearing down the loop. Plain `def` callbacks cannot be interrupted; `async def` callbacks can be cancelled. Wrap a long coroutine in `try` / `except` / `finally` if it has resources to release:

```python
async def poll():
    try:
        while True:
            await read_sensor_async()
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        # server.stop() cancelled us — clean up
        await sensor.close()
        raise
```

The `CancelledError` propagates out of the coroutine; raising it lets the task machinery complete normally. Any cleanup that *must* run on shutdown goes in the `finally` branch.

For repeated callbacks, registration is the right place to attach cleanup hooks. `server.removeCallback(callback_id)` returns synchronously and removes the next invocation; the currently-running one continues until it returns.

---

## What's next?

The distillery is now running on the server's event loop, with the update loop, and a clean shutdown path. The next pages move from behaviour to production: who is allowed to talk to the server, and over what kind of channel.

- [Access control — roles](400_access-control-roles.md) — `Role` / `o6.roles`, default-deny, granting reading / writing / calling per node, role mappings for built-in roles.
- [Server manual](../../manual/server/callbacks.md) — every callback type, its signature, and the resolution order.