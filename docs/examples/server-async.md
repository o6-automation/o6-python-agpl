# Async Server Example

Source example: `examples/highlevel/server_async.py`

This example runs the server cooperatively on an asyncio event loop.

## Explanation

### Using `async with server`

The server lifecycle is managed directly by the async context manager.

```python
async with server:
    ...
```

### Updating values in the async loop

The loop sleeps asynchronously and updates the server-side value on each iteration.

```python
await asyncio.sleep(1)
temperature.value = 22.5 + i * 0.1
```

## Full source

```python
#!/usr/bin/env python3

import asyncio
import o6
from o6 import Server
from o6.ns import ns0


async def main():
    server = Server(port=4840)

    plant = server.addObject("Plant", server.objectsNode)
    temperature = server.addVariable("Temperature", plant, 22.5)

    def add_numbers(a, b):
        return [a + b]

    server.addMethod(
        "Add",
        plant,
        add_numbers,
        inputArgs=[
            ns0.datatypes.Argument(name="A", dataType=o6.Double, valueRank=o6.ValueRank.SCALAR),
            ns0.datatypes.Argument(name="B", dataType=o6.Double, valueRank=o6.ValueRank.SCALAR),
        ],
        outputArgs=[
            ns0.datatypes.Argument(name="Sum", dataType=o6.Double, valueRank=o6.ValueRank.SCALAR),
        ],
    )

    async with server:
        print("Server running – press Ctrl+C to stop")
        i = 0
        while True:
            await asyncio.sleep(1)
            i += 1
            temperature.value = 22.5 + i * 0.1
            print(f"  Temperature = {temperature.value:.1f}")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
```