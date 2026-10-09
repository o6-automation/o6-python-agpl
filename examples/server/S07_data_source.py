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

# BEGIN MD
# `ProcessModel` holds the "real" value outside the address space, the way a
# sensor driver or simulation would. `tick()` advances it; `read_temperature()`
# is the read side, kept as its own method so the sampling points below stay
# obvious even though the high-level API has no separate callback slot to
# plug it into.
# END MD


# BEGIN CODE
class ProcessModel:
    def __init__(self) -> None:
        self._temperature = 20.0

    def tick(self) -> None:
        self._temperature += 0.05

    def read_temperature(self) -> float:
        return self._temperature


# END CODE


def main() -> None:
    process = ProcessModel()
    with Server(port=EXAMPLE_PORT) as server:
        # BEGIN MD
        # ## 1. Seed the variable
        # The initial value comes straight from the process model, so the
        # Variable starts in sync with the "real" state instead of at zero.
        # END MD

        # BEGIN CODE
        print("--- 1. Seed the variable ---")
        temp_node = server.addVariable(
            "ProcessTemperature",
            server.objectsNode,
            process.read_temperature(),
            nodeId="ns=1;s=ProcessTemperature",
        )
        print(f"Temperature = {server.read(temp_node)}")
        # END CODE

        # BEGIN MD
        # ## 2. Manual updates
        # Each tick advances the process model, then `server.write()` pushes
        # the new value into the address space; any subscribed client sees
        # it on the next publish. This explicit write is what stands in for
        # a value callback: the address space is only ever as fresh as the
        # last write.
        # END MD

        # BEGIN CODE
        print("\n--- 2. Manual updates ---")
        for _ in range(5):
            process.tick()
            server.write(temp_node, process.read_temperature()).check()
            print(f"Temperature = {server.read(temp_node)}")
            time.sleep(0.2)
        # END CODE

    print("\n=== Example completed ===")


if __name__ == "__main__":
    main()
