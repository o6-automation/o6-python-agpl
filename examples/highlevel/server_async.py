#!/usr/bin/env python3
"""
Async OPC UA Server
===================

Demonstrates running an OPC UA server cooperatively on an asyncio
event loop — no background threads needed.

    opc.tcp://localhost:4840
"""

import asyncio
from o6 import Server
from o6.server import make_argument


async def main():
    server = Server(port=4840)

    # Add nodes before starting
    plant = server.add_object("Plant", server.objects_node)
    temperature = server.add_variable("Temperature", plant, 22.5)

    def add_numbers(a, b):
        return [a + b]

    server.add_method(
        "Add",
        plant,
        add_numbers,
        input_args=[
            make_argument("A", "i=11"),
            make_argument("B", "i=11"),
        ],
        output_args=[
            make_argument("Sum", "i=11"),
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
