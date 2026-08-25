#!/usr/bin/env python3
"""Demo OPC UA server for the o6 MCP demo.

Starts a small server on opc.tcp://localhost:4840 with a few variables
that change over time. Use together with `examples/mcp_server/demo.py`.

Run::

    python -m examples.mcp_server.demo_server
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
            vars_["temperature"].value = 22.5 + (cycle % 50) * 0.1
            vars_["pressure"].value = 1013.25 + (cycle % 20) * 0.5
            vars_["is_running"].value = cycle % 30 != 0
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        server.stop()


if __name__ == "__main__":
    main()
