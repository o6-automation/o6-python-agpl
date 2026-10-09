#!/usr/bin/env python3
# Copyright 2026 (c) o6 Automation GmbH
# SPDX-License-Identifier: AGPL-3.0-or-later
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

"""
Async OPC UA Server
===================

Demonstrates running an OPC UA server cooperatively on an asyncio
event loop — no background threads needed.

    opc.tcp://localhost:4840
"""

import os

import asyncio
import o6
from o6 import Server
from o6.ns import ns0

EXAMPLE_PORT = int(os.environ.get("O6_EXAMPLE_PORT", "4840"))


async def main():
    server = Server(port=EXAMPLE_PORT)

    # Add nodes before starting
    plant = await server.addObject("Plant", server.objectsNode)
    temperature = await server.addVariable("Temperature", plant, 22.5)

    def add_numbers(node, a, b):
        return (o6.StatusCode.GOOD, a + b)

    (
        await server.addMethod(
            "Add",
            plant,
            add_numbers,
            inputArgs=[
                ns0.datatypes.Argument(name="A", dataType=o6.Double, valueRank=o6.ValueRank.SCALAR),
                ns0.datatypes.Argument(name="B", dataType=o6.Double, valueRank=o6.ValueRank.SCALAR),
            ],
            outputArgs=[
                ns0.datatypes.Argument(
                    name="Sum", dataType=o6.Double, valueRank=o6.ValueRank.SCALAR
                ),
            ],
        )
    )

    async with server:
        print(f"Server running at opc.tcp://localhost:{EXAMPLE_PORT}")
        print("Press Ctrl+C to stop.")
        i = 0

        while True:
            await asyncio.sleep(1)
            i += 1
            await temperature(22.5 + i * 0.1)
            print(f"Temperature = {await temperature():.1f}")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Server stopped.")
