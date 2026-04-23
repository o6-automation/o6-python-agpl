# Client Modes Example

Source example: `examples/highlevel/client_modes.py`

This example shows the different ways the client can be used with and without asyncio.

## Explanation

### Running inside an async context

The first variant uses `async with` and awaits the read directly.

```python
asyncio.run(async_client())
```

### Using the client synchronously

The next variant creates a normal client and uses `connect`, `read`, and `disconnect` in sequence.

```python
c = o6.Client()
c.connect()
v = c.read("i=2258")
c.disconnect()
```

### Reusing an event loop

An externally created loop can be passed into the client when loop ownership matters.

```python
loop = asyncio.new_event_loop()
c = o6.Client(loop=loop)
```

### Mixing sync and async calls

The last example mixes both styles. This only works when the loop state matches the operation being performed.

```python
c.connect()
loop.run_until_complete(do_some_async_stuff())
c.disconnect()
```

## Full source

```python
#!/usr/bin/env python3

import sys
import os
import asyncio

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import o6
import socket

localhost = socket.gethostname()
endpoint_url = f"opc.tcp://{localhost}:4840"

print("=== Client inside an async context ===")


async def async_client():
    c = o6.Client()
    c.config.endpoint_url = endpoint_url
    async with c:
        v = await c.read("i=2258")
        print(f'Reading value v="{v}"')


asyncio.run(async_client())


print("\n=== Self contained Client (with its own asyncio loop) ===")


def self_contained_client():
    c = o6.Client()
    c.config.endpoint_url = endpoint_url

    c.connect()
    v = c.read("i=2258")
    print(f'Reading value v="{v}"')
    c.disconnect()


self_contained_client()


print("\n=== Reusing event loop outside of async context ===")


def reuse_event_loop_sync():
    loop = asyncio.new_event_loop()

    c = o6.Client(loop=loop)
    c.config.endpoint_url = endpoint_url

    c.connect()
    v = c.read("i=2258")
    print(f'Reading value v="{v}"')
    c.disconnect()


reuse_event_loop_sync()


print("\n=== Reusing event loop inside of async context ===")


def reuse_event_loop_async():
    loop = asyncio.new_event_loop()

    async def main():
        c = o6.Client(loop=loop)
        c.config.endpoint_url = endpoint_url

        async with c:
            future = c.read("ns=1;s=IntegerVariable")
            print("whatever")
            v = await future
            print(f'Reading value v="{v}"')

    loop.run_until_complete(main())


reuse_event_loop_async()


print("\n=== Reusing event loop with mix and match async ===")


def reuse_event_loop_mixmatch():
    loop = asyncio.new_event_loop()
    c = o6.Client(loop=loop)
    c.config.endpoint_url = endpoint_url

    c.connect()

    async def do_some_async_stuff():
        v = await c.read("i=2258")
        print(f'Reading value v="{v}"')

    loop.run_until_complete(do_some_async_stuff())
    c.disconnect()
```