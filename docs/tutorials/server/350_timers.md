# Timers and async loops

The distillery's update loop runs at 10 Hz from `Server.addRepeatedCallback(tick, 100.0)`. Repeated callbacks can also be `async def`. The server runs them on its asyncio event loop, and while a callback awaits, the rest of the loop keeps running.

[Running on asyncio](140_async-server.md) covers the basics: `async with server:`, `await asyncio.sleep(...)` and `asyncio.run(...)`. This page covers:

- `async def` callbacks for cooperative I/O.
- Long-running background work that must not block the loop.
- Cooperative cancellation on `server.stop()`.

---

## Async callbacks

`addRepeatedCallback` accepts a plain function or an `async def`. Both have the same result semantics. An `async def` callback can `await` other coroutines, run other tasks or hand work to a worker pool.

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

`poll_sensor` runs on the server's event loop. `await read_sensor_async()` yields control until the I/O completes, and other callbacks (Variable reads, method calls, the listener socket) run in the meantime.

Method, Variable read/write and timer callbacks can all be `async def`. Await
dual-mode API calls inside them. Synchronous callbacks keep immediate local
results. A callback that needs pending work on the same loop must be
asynchronous and await that work.

`async with server` runs the server on the same loop as your `asyncio.run(main())`:

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

`async with` enters the loop-bound lifecycle. `await asyncio.sleep(1)` doesn't block; the loop keeps running during the sleep.

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

`asyncio.run` drives the event loop and the main task. `KeyboardInterrupt` on the main thread cancels the main task, and the `async with` block runs `server.stop()` on exit.

---

## Long-running work

A callback that takes longer than its interval causes problems. Use one of:

1. **Cooperative I/O with `asyncio`** for I/O that has an async API, such as a database driver, a serial port or an HTTP client.
2. **A thread pool executor** for I/O that is inherently blocking, such as a legacy C library or a synchronous database driver.

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

`loop.run_in_executor(pool, fn)` runs `fn` on the thread pool and returns an awaitable. The loop stays responsive while the blocking call runs on a worker thread.

!!! warning
    `time.sleep(1)` inside a callback blocks the loop. Use `await asyncio.sleep(1)` or `loop.run_in_executor(...)` instead. A synchronous callback that does I/O without `await` stalls every other callback until it returns.

---

## Cancellation on stop

`server.stop()` drains in-flight callbacks before tearing down the loop. Plain `def` callbacks can't be interrupted; `async def` callbacks can be cancelled. If a long coroutine holds resources, wrap it in `try` / `except` / `finally`:

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

Re-raise `CancelledError` so the task completes normally. Put cleanup that must always run on shutdown in a `finally` branch.

For repeated callbacks, attach cleanup hooks at registration. `server.removeCallback(callback_id)` returns synchronously and cancels the next invocation; a running invocation continues until it returns.

---

## Next steps

| Topic | What it covers |
|---|---|
| [Access control — roles](400_access-control-roles.md) | `Role` / `o6.roles`, default-deny, granting reading / writing / calling per node, role mappings for built-in roles. |
| [Server manual](../../manual/server/callbacks.md) | Every callback type, its signature, and the resolution order. |
