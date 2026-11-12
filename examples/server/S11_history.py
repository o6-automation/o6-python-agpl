#!/usr/bin/env python3
# Copyright 2026 (c) o6 Automation GmbH (Author: Andreas Ebner)
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
Server Tutorial: History
==========================

Records a Variable's history and configures the server's history
database.

Run any OPC UA client (for example ``C02_firststeps.py`` or
``C12_browser.py``) against this server to read and write the values.
Read the recorded history with the client's ``historyRead``::

    data = client.historyRead("ns=1;i=1001", start, end)
    for dv in data.dataValues:
        print(dv.sourceTimestamp, dv.value)
"""

import os

import time

import o6
from o6 import Server

EXAMPLE_PORT = int(os.environ.get("O6_EXAMPLE_PORT", "4840"))
EXAMPLE_ENDPOINT = f"opc.tcp://localhost:{EXAMPLE_PORT}"

# BEGIN MD
# Configure the history database before `server.start()`.
#
# - `capacity` is the number of samples each historizing Variable keeps.
#   When a Variable's store is full, the oldest sample is evicted.
# - `maxResponseSize` is a server-wide cap, independent of `capacity`, on
#   the samples in one `historyRead` response. A request for more
#   values gets the first `maxResponseSize` plus a continuation point.
#   The client must call `historyRead` again with that token until it
#   comes back empty. The high-level `client.historyRead(...)` follows
#   continuation points until the interval or per-node limit is
#   exhausted.
# END MD


def main():
    localhost = "localhost"
    endpoint_url = EXAMPLE_ENDPOINT

    server = Server(port=EXAMPLE_PORT)

    # BEGIN CODE
    print("--- 1. History Database ---")

    server.config.setHistoryDatabase(capacity=1000, maxResponseSize=200)
    # END CODE

    # BEGIN MD
    # ## 2. Historizing variables
    # `historizing=True` is short for `historizing=o6.History()`: record a
    # sample on every Write, with the database's default capacity.
    # `o6.History(...)` changes that per Variable:
    #
    # - `capacity=` overrides the default store size.
    # - `strategy="poll"` samples the value every `interval` seconds through
    #   an internal MonitoredItem instead of hooking into the Write service.
    #
    # A Variable whose value changes without a Write (a read callback, a
    # lower-level update) is historized only with `poll`.
    # END MD

    # BEGIN CODE
    print()
    print("--- 2. Historizing Variables ---")

    temperature = server.addVariable(
        "Temperature",
        server.objectsNode,
        22.5,
        nodeId="ns=1;i=1001",
        historizing=True,
    )

    pressure = server.addVariable(
        "Pressure",
        server.objectsNode,
        1013.25,
        nodeId="ns=1;i=1002",
        historizing=o6.History(capacity=500, strategy="poll", interval=0.5),
    )
    # END CODE

    # BEGIN MD
    # ## 3. Run and update loop
    # `server.start()` returns once the listeners are ready; a background
    # thread drives I/O until `server.stop()`. Both Variables change once per
    # cycle, so either strategy captures them. `pressure` uses `poll` only to
    # show the configuration. A Variable backed by a read callback (see
    # `S09_implement_readwrite.py`) never receives a Write and needs `poll`.
    # END MD

    # BEGIN CODE
    print()
    print("--- 3. Run and Update Loop ---")

    server.start()
    print(f"Server running at {endpoint_url}")
    print("Press Ctrl+C to stop.")

    try:
        cycle = 0
        while True:
            cycle += 1
            temperature(22.5 + (cycle % 50) * 0.1)
            pressure(1013.25 + (cycle % 20) * 0.5)

            if cycle % 10 == 0:
                print(
                    f"Cycle {cycle}: Temp = {temperature():.1f}°C, "
                    f"Pressure = {pressure():.1f}hPa"
                )

            time.sleep(1.0)

    except KeyboardInterrupt:
        print("Shutting down...")
    finally:
        server.stop()
        print("Server stopped.")


if __name__ == "__main__":
    main()
    # END CODE
