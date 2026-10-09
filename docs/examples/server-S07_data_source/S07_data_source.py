#!/usr/bin/env python3
# Copyright (c) 2026 o6 Automation GmbH
#
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
Server Tutorial: Data Source Updates
=====================================

Demonstrates driving a Variable's value from an external process model
instead of assigning a constant. The pattern is: keep the "real" value in
plain Python state, and push it into the address space with `server.write()`
whenever it changes.

Note: the high-level API models this through explicit read/write rather
than a separate value-callback/data-source object — the loop below writes
after every state change, which is what a callback would have done for you.
"""

import os

import time
from o6 import Server

EXAMPLE_PORT = int(os.environ.get("O6_EXAMPLE_PORT", "4840"))



class ProcessModel:
    def __init__(self) -> None:
        self._temperature = 20.0

    def tick(self) -> None:
        self._temperature += 0.05

    def read_temperature(self) -> float:
        return self._temperature




def main() -> None:
    process = ProcessModel()
    with Server(port=EXAMPLE_PORT) as server:

        print("--- 1. Seed the variable ---")
        temp_node = server.addVariable(
            "ProcessTemperature",
            server.objectsNode,
            process.read_temperature(),
            nodeId="ns=1;s=ProcessTemperature",
        )
        print(f"Temperature = {server.read(temp_node)}")


        print("\n--- 2. Manual updates ---")
        for _ in range(5):
            process.tick()
            server.write(temp_node, process.read_temperature()).check()
            print(f"Temperature = {server.read(temp_node)}")
            time.sleep(0.2)

    print("\n=== Example completed ===")


if __name__ == "__main__":
    main()