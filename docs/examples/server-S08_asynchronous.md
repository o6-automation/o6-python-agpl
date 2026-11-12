# Async

Runs an OPC UA server cooperatively on an asyncio event loop, without
background threads.

    opc.tcp://localhost:4840

## Multitasking
The server runs on a single asyncio event loop instead of a background
thread. It switches to another task, such as handling a client request,
only at an `await`.

`async with` starts and stops the server without blocking the event
loop.

```python
async with server:
```

`await asyncio.sleep(1)` hands control back to the event loop, so the
server processes client requests while waiting. `time.sleep(1)` would
block it.

```python
await asyncio.sleep(1)
```

`asyncio.run` starts the event loop and runs the main task to
completion.

```python
asyncio.run(main())
```

## Source Code

Download [`S08_asynchronous.py`](server-S08_asynchronous/S08_asynchronous.py) to run it locally.
