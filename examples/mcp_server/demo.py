#!/usr/bin/env python3
"""End-to-end demo for the o6 MCP server.

This script:

1. Starts a small OPC UA server in a background thread (port 4840).
2. Spawns the MCP server (``examples.mcp_server.server``) as a subprocess on stdio.
3. Connects to it via the official MCP Python client.
4. Calls the exposed tools and prints the results.

Run::

    python -m examples.mcp_server.demo
"""

from __future__ import annotations

import asyncio
import json
import sys
import threading
import time
from contextlib import AsyncExitStack

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from examples.mcp_server.demo_server import build_server


def _start_opcua_server() -> tuple[object, threading.Event]:
    server, vars_ = build_server()
    stop_evt = threading.Event()

    def _run() -> None:
        server.start()
        cycle = 0
        try:
            while not stop_evt.is_set():
                cycle += 1
                vars_["temperature"].value = 22.5 + (cycle % 50) * 0.1
                vars_["pressure"].value = 1013.25 + (cycle % 20) * 0.5
                vars_["is_running"].value = cycle % 30 != 0
                time.sleep(0.5)
        finally:
            server.stop()

    threading.Thread(target=_run, daemon=True).start()
    # Give the server a moment to come up
    time.sleep(1.0)
    return server, stop_evt


def _print_tool_result(name: str, result) -> None:
    print(f"\n>>> {name}")
    for c in result.content:
        text = getattr(c, "text", None)
        if text is None:
            print(c)
            continue
        try:
            parsed = json.loads(text)
            print(json.dumps(parsed, indent=2, default=str))
        except (ValueError, TypeError):
            print(text)


async def run_demo() -> None:
    params = StdioServerParameters(
        command=sys.executable,
        args=["-m", "examples.mcp_server.server"],
    )

    async with AsyncExitStack() as stack:
        read_, write_ = await stack.enter_async_context(stdio_client(params))
        session = await stack.enter_async_context(ClientSession(read_, write_))
        await session.initialize()

        tools = await session.list_tools()
        print("Available MCP tools:")
        for t in tools.tools:
            print(f"  - {t.name}: {(t.description or '').splitlines()[0]}")

        _print_tool_result(
            "get_endpoints",
            await session.call_tool("get_endpoints", {"server_url": "opc.tcp://localhost:4840"}),
        )

        _print_tool_result(
            "connect",
            await session.call_tool("connect", {"endpoint_url": "opc.tcp://localhost:4840"}),
        )

        _print_tool_result("status", await session.call_tool("status", {}))

        _print_tool_result("get_server_info", await session.call_tool("get_server_info", {}))

        _print_tool_result(
            "browse",
            await session.call_tool("browse", {"node_id": "i=85"}),
        )

        _print_tool_result(
            "read Temperature",
            await session.call_tool("read", {"node_id": "ns=1;s=Temperature"}),
        )

        _print_tool_result(
            "write SetPoint=42",
            await session.call_tool("write", {"node_id": "ns=1;s=SetPoint", "value": 42}),
        )

        _print_tool_result(
            "read SetPoint",
            await session.call_tool("read", {"node_id": "ns=1;s=SetPoint"}),
        )

        _print_tool_result(
            "browse_path",
            await session.call_tool(
                "browse_path",
                {"path": "Objects.Server.ServerStatus.CurrentTime"},
            ),
        )

        _print_tool_result("disconnect", await session.call_tool("disconnect", {}))


def main() -> None:
    server, stop_evt = _start_opcua_server()
    try:
        asyncio.run(run_demo())
    finally:
        stop_evt.set()
        time.sleep(0.5)


if __name__ == "__main__":
    main()
