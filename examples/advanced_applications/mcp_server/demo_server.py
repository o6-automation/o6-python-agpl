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

"""Demo OPC UA server for the o6 MCP demo.

Starts a small server on opc.tcp://localhost:4840 with a few variables
that change over time. Use together with `examples/advanced_applications/mcp_server/demo.py`.

Run::

    python -m examples.advanced_applications.mcp_server.demo_server
"""

from __future__ import annotations

import time

from o6 import Server


def build_server() -> tuple[Server, dict]:
    server = Server(port=4840)

    vars_ = {
        "temperature": server.addVariable(
            "Temperature", server.objectsNode, 22.5, nodeId="ns=1;s=Temperature"
        ),
        "pressure": server.addVariable(
            "Pressure", server.objectsNode, 1013.25, nodeId="ns=1;s=Pressure"
        ),
        "set_point": server.addVariable(
            "SetPoint", server.objectsNode, 25, nodeId="ns=1;s=SetPoint"
        ),
        "is_running": server.addVariable(
            "IsRunning", server.objectsNode, False, nodeId="ns=1;s=IsRunning"
        ),
        "machine_name": server.addVariable(
            "MachineName",
            server.objectsNode,
            "CNC-Mill-01",
            nodeId="ns=1;s=MachineName",
        ),
    }
    return server, vars_


def main() -> None:
    server, vars_ = build_server()
    server.start()
    print("Demo OPC UA server running at opc.tcp://localhost:4840")
    print("Variables: ns=1;s=Temperature, Pressure, SetPoint, IsRunning, MachineName")
    print("Press Ctrl+C to stop.")
    try:
        cycle = 0
        while True:
            cycle += 1
            vars_["temperature"](22.5 + (cycle % 50) * 0.1)
            vars_["pressure"](1013.25 + (cycle % 20) * 0.5)
            vars_["is_running"](cycle % 30 != 0)
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        server.stop()


if __name__ == "__main__":
    main()
