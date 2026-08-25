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

# BEGIN MD
# ## Multitasking
# Unlike traditional multi-threaded servers, this server runs on a single event loop.
# By using `asyncio`, the server handles communications and updates differently than regular sync servers:
# it is able to switch tasks when it encounters an `await`.
# END MD


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

    # BEGIN MD
    # The `async with` statement manages the server lifecycle, ensuring
    # clean startup and shutdown without blocking the main event loop.
    # END MD

    # BEGIN CODE
    async with server:
        # END CODE
        print("Server running – press Ctrl+C to stop")
        i = 0

        # BEGIN MD
        # The `await asyncio.sleep(1)` is non-blocking.
        # Unlike `time.sleep(1)`, it hands control back over to the event loop,
        # allowing the server to process client requests while waiting.
        # END MD
        while True:
            # BEGIN CODE
            await asyncio.sleep(1)
            # END CODE
            i += 1
            temperature.value = 22.5 + i * 0.1
            print(f"  Temperature = {temperature.value:.1f}")


if __name__ == "__main__":
    # BEGIN MD
    # `asyncio.run` is the entry point that kicks off the event loop
    # and manages the lifecycle of the main task.
    # END MD
    try:
        # BEGIN CODE
        asyncio.run(main())
        # END CODE
    except KeyboardInterrupt:
        pass
