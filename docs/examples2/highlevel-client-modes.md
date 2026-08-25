Client Modes : Sync & Async Flexibility
=======================================
The ``o6.Client`` is a *hybrid* client: every operation on it
(`read`, `write`, `subscribe`, …) is exposed as a synchronous,
blocking method *and* as an awaitable coroutine, and the client
adapts at runtime to whichever calling convention the surrounding
code uses. The same ``client.read(...)`` call returns a value
directly inside a ``with`` block, and an awaitable inside an
``async with`` block.

This example walks through the four useful patterns:

- **Case A — Sync, self-contained.** The default. The client
  creates and runs its own event loop in a worker thread; you
  call ``client.connect()`` / ``client.read(...)`` /
  ``client.disconnect()`` and they block until the result is back.
- **Case B — Async (``async with`` + ``await``).** Same client
  object, but the calls return coroutines and you ``await`` them.
  Use this from inside an ``asyncio.run()`` or any other running
  asyncio loop.
- **Case C — Sync with a shared event loop.** The SDK lets you
  hand the client a loop you already manage. The loop must be
  *running* (the SDK does not start it for you).
- **Case D — Mix-and-match (sync connect + async reads).** Real
  industrial code often opens the connection synchronously at
  startup and then dispatches the actual I/O to async tasks. The
  client supports that too: the same ``client.read(...)`` can be
  awaited from an async context.

``basic_server.py`` works fine for this example.

```python
localhost = "localhost"
endpoint_url = f"opc.tcp://{localhost}:4840"
print(f"Connecting to {endpoint_url} ...")
```

## 1. Case A — Sync, Self-Contained
This is the **default** and the most common case. The client
detects that no event loop is running, creates a new one in a
background worker thread, and runs the OPC UA session on that
thread. From the caller's perspective, ``client.connect()``,
``client.read(...)``, and ``client.disconnect()`` are plain
blocking Python calls.

```python
print("\n=== Case A: Sync, self-contained ===")


def case_a_sync_self_contained() -> None:
    c = o6.Client(endpointUrl=endpoint_url)
    c.connect()
    v = c.read("i=2258")  # Standard OPC UA node for Server Time
    print(f'  read: v="{v}"')
    c.disconnect()


case_a_sync_self_contained()
```

## 2. Case B — Async (``async with`` + ``await``)
Same client object, but inside an ``async with`` block, every
method returns an awaitable instead of a value. The
``asyncio.run(...)`` call at the bottom of the script creates the
application-side event loop, the ``async with`` block runs the
client session, and ``await c.read(...)`` blocks the application
coroutine until the value comes back.

```python
print("\n=== Case B: Async with 'async with' + 'await' ===")


async def case_b_async_context() -> None:
    c = o6.Client(endpointUrl=endpoint_url)
    async with c:
        v = await c.read("i=2258")
        print(f'  read: v="{v}"')


asyncio.run(case_b_async_context())
```

## 3. Case C — Sync with a Shared Event Loop
If your application already manages an ``asyncio`` event loop,
you can hand the client that loop. However the **loop must already be
running**.

The working pattern is to run the loop in a daemon thread,
stop it via ``call_soon_threadsafe(loop.stop)``, and join the
thread before the application exits.

```python
print("\n=== Case C: Sync with a shared event loop ===")


def case_c_shared_loop() -> None:
    loop = asyncio.new_event_loop()
    runner = threading.Thread(target=loop.run_forever, daemon=True)
    runner.start()

    c = o6.Client(endpointUrl=endpoint_url, loop=loop)
    c.connect()
    v = c.read("i=2258")
    print(f'  read: v="{v}"')
    c.disconnect()

    # Stop the worker thread and wait for it to exit.
    loop.call_soon_threadsafe(loop.stop)
    runner.join(timeout=2.0)
    print("  loop stopped, thread joined")


case_c_shared_loop()
```

## 4. Case D — Mix-and-Match (Sync Connect, Async Reads)
A common real-world pattern: open the connection synchronously
at startup, then dispatch the actual I/O to async tasks once
the application is up and running. The same ``client.read(...)``
call returns a value in a sync context and an awaitable in an
async one.

```python
print("\n=== Case D: Mix-and-match (sync connect + async reads) ===")


def case_d_mix_and_match() -> None:
    c = o6.Client(endpointUrl=endpoint_url)
    c.connect()  # sync — runs in the main thread

    async def read_async() -> None:
        v = await c.read("i=2258")
        print(f'  async read: v="{v}"')

    asyncio.run(read_async())  # async — runs in its own loop

    c.disconnect()  # sync — back on the main thread
    print("  disconnected")


case_d_mix_and_match()

print("\n=== Example completed ===")
```

## Complete Source Code

```python
#!/usr/bin/env python3
# Copyright 2026 (c) o6 Automation GmbH
"""
Client Modes : Sync & Async Flexibility
=======================================
The ``o6.Client`` is a *hybrid* client: every operation on it
(`read`, `write`, `subscribe`, …) is exposed as a synchronous,
blocking method *and* as an awaitable coroutine, and the client
adapts at runtime to whichever calling convention the surrounding
code uses. The same ``client.read(...)`` call returns a value
directly inside a ``with`` block, and an awaitable inside an
``async with`` block.

This example walks through the four useful patterns:

- **Case A — Sync, self-contained.** The default. The client
  creates and runs its own event loop in a worker thread; you
  call ``client.connect()`` / ``client.read(...)`` /
  ``client.disconnect()`` and they block until the result is back.
- **Case B — Async (``async with`` + ``await``).** Same client
  object, but the calls return coroutines and you ``await`` them.
  Use this from inside an ``asyncio.run()`` or any other running
  asyncio loop.
- **Case C — Sync with a shared event loop.** The SDK lets you
  hand the client a loop you already manage. The loop must be
  *running* (the SDK does not start it for you).
- **Case D — Mix-and-match (sync connect + async reads).** Real
  industrial code often opens the connection synchronously at
  startup and then dispatches the actual I/O to async tasks. The
  client supports that too: the same ``client.read(...)`` can be
  awaited from an async context.

``basic_server.py`` works fine for this example.
"""

import asyncio
import socket
import threading
import o6

localhost = "localhost"
endpoint_url = f"opc.tcp://{localhost}:4840"
print(f"Connecting to {endpoint_url} ...")



print("\n=== Case A: Sync, self-contained ===")


def case_a_sync_self_contained() -> None:
    c = o6.Client(endpointUrl=endpoint_url)
    c.connect()
    v = c.read("i=2258")  # Standard OPC UA node for Server Time
    print(f'  read: v="{v}"')
    c.disconnect()


case_a_sync_self_contained()



print("\n=== Case B: Async with 'async with' + 'await' ===")


async def case_b_async_context() -> None:
    c = o6.Client(endpointUrl=endpoint_url)
    async with c:
        v = await c.read("i=2258")
        print(f'  read: v="{v}"')


asyncio.run(case_b_async_context())



print("\n=== Case C: Sync with a shared event loop ===")


def case_c_shared_loop() -> None:
    loop = asyncio.new_event_loop()
    runner = threading.Thread(target=loop.run_forever, daemon=True)
    runner.start()

    c = o6.Client(endpointUrl=endpoint_url, loop=loop)
    c.connect()
    v = c.read("i=2258")
    print(f'  read: v="{v}"')
    c.disconnect()

    # Stop the worker thread and wait for it to exit.
    loop.call_soon_threadsafe(loop.stop)
    runner.join(timeout=2.0)
    print("  loop stopped, thread joined")


case_c_shared_loop()



print("\n=== Case D: Mix-and-match (sync connect + async reads) ===")


def case_d_mix_and_match() -> None:
    c = o6.Client(endpointUrl=endpoint_url)
    c.connect()  # sync — runs in the main thread

    async def read_async() -> None:
        v = await c.read("i=2258")
        print(f'  async read: v="{v}"')

    asyncio.run(read_async())  # async — runs in its own loop

    c.disconnect()  # sync — back on the main thread
    print("  disconnected")


case_d_mix_and_match()

print("\n=== Example completed ===")
```
