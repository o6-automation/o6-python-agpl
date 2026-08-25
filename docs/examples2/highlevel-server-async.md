Async OPC UA Server
===================

Demonstrates running an OPC UA server cooperatively on an asyncio
event loop — no background threads needed.

    opc.tcp://localhost:4840

## Multitasking
Unlike traditional multi-threaded servers, this server runs on a single event loop.
By using `asyncio`, the server handles communications and updates differently than regular sync servers:
it is able to switch tasks when it encounters an `await`.

The `async with` statement manages the server lifecycle, ensuring
clean startup and shutdown without blocking the main event loop.

```python
async with server:
```

The `await asyncio.sleep(1)` is non-blocking.
Unlike `time.sleep(1)`, it hands control back over to the event loop,
allowing the server to process client requests while waiting.

```python
await asyncio.sleep(1)
```

`asyncio.run` is the entry point that kicks off the event loop
and manages the lifecycle of the main task.

```python
asyncio.run(main())
```

## Complete Source Code

```python
#!/usr/bin/env python3
# Copyright 2026 (c) o6 Automation GmbH
"""
Async OPC UA Server
===================

Demonstrates running an OPC UA server cooperatively on an asyncio
event loop — no background threads needed.

    opc.tcp://localhost:4840
"""

import asyncio
import o6
from o6 import Server
from o6.ns import ns0



async def main():
    server = Server(port=4840)

    # Add nodes before starting
    plant = server.addObject("Plant", server.objectsNode)
    temperature = server.addVariable("Temperature", plant, 22.5)

    def add_numbers(node, a, b):
        return (o6.StatusCode.GOOD, a + b)

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
