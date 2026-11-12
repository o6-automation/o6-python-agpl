# Running on asyncio

The servers so far run on a background thread: `server.start()` returns immediately and the main thread loops and writes values. When your update loop needs to `await` other work, such as an async database driver or sensor client, run the server on a single `asyncio` event loop instead.

This page is an aside with its own small address space. The result is a `Kettle/Temperature` Variable that updates once a second, driven by `await asyncio.sleep(...)`.

---

## `async with` instead of `start()` / `stop()`

`Server` is an async context manager as well as a sync one. `async with server:` calls `start()` on entry and `stop()` on exit, including on an exception, like the sync `with server:` form.

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

The same API builds the address space in both modes. Inside an async task, `await` node creation, node calls and dynamic child lookups, including operations that complete immediately. Use `async with` for the lifecycle and `await asyncio.sleep(...)` to let other work run.

!!! warning
    `time.sleep(...)` inside an `async def` blocks the entire event loop: no client request is served while it runs. Use `await asyncio.sleep(...)`, which hands control back to the loop.

---

## `asyncio.run` is the entry point

`asyncio.run(main())` creates the event loop, runs `main()` to completion and closes the loop. There is no separate step to start the loop.

```python
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Server stopped.")
```

`KeyboardInterrupt` on the main thread cancels the running task. The `async with server:` block still runs `server.stop()` on the way out.

---

## Repeated callbacks can be `async def` too

`server.addRepeatedCallback(...)`, the timer API from [Server callbacks](330_server-callbacks.md), accepts a coroutine function. The server awaits it on its own loop:

```python
async def tick():
    await temperature((await temperature()) + 0.1)

server.addRepeatedCallback(tick, 1000.0)   # every 1 s, as a coroutine
```

This registers a timer in place of the explicit `while True: await asyncio.sleep(...)` loop. [Timers and async loops](350_timers.md) covers offloading blocking work to a thread pool and cancelling cleanly on shutdown.

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

The distillery server ([Set the stage](../setup.md)) uses the threaded form because its simulation runs in a background thread. Use the async form when the code that drives your updates is async, such as a database, an HTTP client or an async sensor SDK.

---

## Next steps

| Topic | What it covers |
|---|---|
| [Declare and implement a Variable](150_implement-variable.md) | The declared-type route to a Variable's read/write behaviour, in a separate implementer class. |
| [Timers and async loops](350_timers.md) | Cooperative cancellation, thread-pool offload, and the full `async def` callback story. |
| [Server Async](../../examples/server-S08_asynchronous.md) | The runnable example this page is based on. |
