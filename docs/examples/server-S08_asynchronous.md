# Async

Demonstrates running an OPC UA server cooperatively on an asyncio
event loop — no background threads needed.

    opc.tcp://localhost:4840

## Multitasking
This server runs on a single asyncio event loop instead of a background
thread. Because everything is cooperative, the server can only switch to
another task — handling a client request, for instance — at an `await`
point.

The `async with` statement manages the server lifecycle, ensuring
clean startup and shutdown without blocking the main event loop.

```python
async with server:
```

The `await asyncio.sleep(1)` is non-blocking. Unlike `time.sleep(1)`,
it hands control back to the event loop, letting the server process
client requests while waiting.

```python
await asyncio.sleep(1)
```

`asyncio.run` is the entry point that kicks off the event loop
and manages the lifecycle of the main task.

```python
asyncio.run(main())
```

## Source Code

Download [`S08_asynchronous.py`](server-S08_asynchronous/S08_asynchronous.py) to run it locally.
