# Running on asyncio

Every server built so far runs on its own background thread: `server.start()` returns immediately, and the main thread is free to loop, sleep, and write values. That's the right shape for a script. It's the wrong shape once the distillery's update loop wants to `await` other things — an async database driver, an async sensor client — without a thread in the picture at all. This page runs the same kind of server cooperatively on a single `asyncio` event loop instead.

Like the previous page, this one is a short aside rather than a continuation of the exact running server — it builds its own small address space to demonstrate the idea cleanly. By the end, a `Kettle/Temperature` Variable updates once a second, driven entirely by `await asyncio.sleep(...)`.

---

## `async with` instead of `start()` / `stop()`

`Server` is an async context manager as well as a sync one. `async with server:` calls `start()` on entry and `stop()` on exit — including on an exception — the same guarantee the sync `with server:` form makes, just on the event loop instead of a thread.

```python
import asyncio
from o6 import Server

async def main():
    server = Server(port=4840)
    sys = await server.addObject("DistillingSystem", server.objectsNode, nodeId="ns=1;i=1000")
    kettle = await server.addObject("Kettle", sys, nodeId="ns=1;i=1300")
    temperature = await server.addVariable(
        "Temperature", kettle, 20.0, nodeId="ns=1;i=1302", writable=False
    )

    async with server:
        print(f"Server running at {server.endpointUrl}")
        i = 0
        while True:
            await asyncio.sleep(1.0)
            i += 1
            await temperature(20.0 + i * 0.1)
            print(f"Kettle temperature = {await temperature():.1f} °C")


asyncio.run(main())
```

The same API builds the address space in either mode. Inside an async task, add `await` to creation, node calls, and dynamic child lookups, including operations that complete immediately. Use `async with` for lifecycle and `await asyncio.sleep(...)` to let other work progress.

!!! warning
    `time.sleep(...)` still works inside an `async def`, but it *blocks the entire event loop* — no client request is served while it runs. `await asyncio.sleep(...)` hands control back to the loop instead, which is the entire point of running this way. Mixing the two defeats the purpose.

---

## `asyncio.run` is the entry point

`asyncio.run(main())` creates the event loop, runs `main()` to completion, and tears the loop down afterward. It's the one call that starts everything — there is no separate "start the loop" step to remember.

```python
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Server stopped.")
```

`KeyboardInterrupt` on the main thread cancels the running task; the `async with server:` block still runs `server.stop()` on the way out, so shutdown is just as clean as the synchronous version.

---

## Repeated callbacks can be `async def` too

`server.addRepeatedCallback(...)` — the timer API used later, in [Server callbacks](330_server-callbacks.md) — accepts a coroutine function directly, and the server awaits it on its own loop:

```python
async def tick():
    await temperature((await temperature()) + 0.1)

server.addRepeatedCallback(tick, 1000.0)   # every 1 s, as a coroutine
```

That's a second way to reach the same "do this periodically" goal as the `while True: await asyncio.sleep(...)` loop above — a registered timer instead of an explicit loop. [Timers and async loops](350_timers.md) covers the deeper version of this: offloading genuinely blocking work to a thread pool, and cancelling cleanly on shutdown.

#### Putting it all together

```python
import asyncio
from o6 import Server


async def main():
    server = Server(port=4840)
    sys = await server.addObject("DistillingSystem", server.objectsNode, nodeId="ns=1;i=1000")
    kettle = await server.addObject("Kettle", sys, nodeId="ns=1;i=1300")
    temperature = await server.addVariable(
        "Temperature", kettle, 20.0, nodeId="ns=1;i=1302", writable=False
    )

    async with server:
        print(f"Server running at {server.endpointUrl}")
        print("Press Ctrl+C to stop.")
        i = 0
        while True:
            await asyncio.sleep(1.0)
            i += 1
            await temperature(20.0 + i * 0.1)
            print(f"Kettle temperature = {await temperature():.1f} °C")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Server stopped.")
```

The real distillery server ([Set the stage](../setup.md)) stays on the threaded form — its simulation already runs in a background thread, so there's no event loop to cooperate with. Reach for the async form when the code driving your updates is itself async: a database, an HTTP client, an async sensor SDK.

---

## What's next?

- [Declare and implement a Variable](150_implement-variable.md) — the declared-type route to a Variable's read/write behaviour, in a separate implementer class.
- [Timers and async loops](350_timers.md) — cooperative cancellation, thread-pool offload, and the full `async def` callback story.
- [Server Async](../../examples/server-S08_asynchronous.md) — the runnable example this page is based on.
