"""MCP server exposing the o6 OPC UA client.

Run with::

    python -m examples.mcp_server.server                    # stdio transport (default)
    python -m examples.mcp_server.server --transport sse    # sse transport on :8000

Tools provided:
    connect, disconnect, status, get_endpoints,
    read, write, browse, browse_path, call_method,
    get_server_info

The server keeps a single shared `o6.Client` instance and serializes operations
through an internal asyncio lock.
"""

from __future__ import annotations

import argparse
import asyncio
import io
import logging
import os
import sys
from dataclasses import dataclass
from typing import Any


def _redirect_c_stdout_to_stderr() -> None:
    """Move OS-level fd 1 to point at fd 2.

    The o6 C extension prints a startup banner via ``printf`` to fd 1.  When
    the MCP server runs over stdio, fd 1 carries the JSON-RPC stream and any
    extra output corrupts it.  We dup fd 1 to a new fd, install that as
    Python-level ``sys.stdout`` (so MCP keeps writing JSON-RPC to the original
    stdout), and point fd 1 at fd 2 so all C-level prints go to stderr.
    """
    saved_fd = os.dup(1)
    os.dup2(2, 1)
    new_stdout = io.TextIOWrapper(
        os.fdopen(saved_fd, "wb", buffering=0),
        encoding="utf-8",
        write_through=True,
        line_buffering=True,
    )
    sys.stdout = new_stdout


# Must run BEFORE importing o6, otherwise the banner already hit fd 1.
if "--transport" not in sys.argv or "stdio" in sys.argv or len(sys.argv) == 1:
    # Default transport is stdio; protect it.  For sse/http it is harmless.
    if os.environ.get("O6_MCP_NO_REDIRECT") != "1":
        _redirect_c_stdout_to_stderr()


import o6  # noqa: E402
from mcp.server.fastmcp import FastMCP  # noqa: E402

logger = logging.getLogger("o6_mcp")

mcp = FastMCP("o6-opcua")


# --------------------------------------------------------------------------- #
# Shared client state
# --------------------------------------------------------------------------- #


@dataclass
class _State:
    client: o6.Client | None = None
    endpoint_url: str | None = None


_state = _State()
_lock = asyncio.Lock()


def _require_client() -> o6.Client:
    if _state.client is None or not _state.client.connected:
        raise RuntimeError("Not connected. Call the 'connect' tool with an endpoint_url first.")
    return _state.client


def _to_jsonable(value: Any) -> Any:
    """Convert o6 / OPC UA values into MCP-friendly JSON values."""
    if value is None or isinstance(value, (bool, int, float, str)):
        return value
    if isinstance(value, bytes):
        return value.hex()
    if isinstance(value, (list, tuple)):
        return [_to_jsonable(v) for v in value]
    if isinstance(value, dict):
        return {str(k): _to_jsonable(v) for k, v in value.items()}
    # NodeId, QualifiedName, LocalizedText, DateTime, StatusCode, structs ...
    return str(value)


# --------------------------------------------------------------------------- #
# Connection management
# --------------------------------------------------------------------------- #


@mcp.tool()
async def connect(
    endpoint_url: str,
    username: str | None = None,
    password: str | None = None,
) -> dict[str, Any]:
    """Connect the OPC UA client to a server.

    Args:
        endpoint_url: e.g. ``opc.tcp://localhost:4840``.
        username: optional username for username/password authentication.
        password: optional password for username/password authentication.
    """
    async with _lock:
        if _state.client is not None and _state.client.connected:
            return {
                "ok": True,
                "already_connected": True,
                "endpoint_url": _state.endpointUrl,
            }

        loop = asyncio.get_running_loop()
        kwargs: dict[str, Any] = {"loop": loop}
        if username is not None:
            kwargs["username"] = username
        if password is not None:
            kwargs["password"] = password

        client = o6.Client(endpoint_url, **kwargs)
        await client.connect()
        _state.client = client
        _state.endpointUrl = endpoint_url
        return {"ok": True, "endpoint_url": endpoint_url}


@mcp.tool()
async def disconnect() -> dict[str, Any]:
    """Disconnect the OPC UA client (if connected)."""
    async with _lock:
        if _state.client is None:
            return {"ok": True, "was_connected": False}
        try:
            await _state.client.disconnect()
        finally:
            _state.client = None
            _state.endpointUrl = None
        return {"ok": True, "was_connected": True}


@mcp.tool()
async def status() -> dict[str, Any]:
    """Report current connection status."""
    if _state.client is None:
        return {"connected": False}
    c = _state.client
    ch_state, sess_state, connect_status = c.state
    return {
        "connected": bool(c.connected),
        "connected": bool(c.connected),
        "endpoint_url": _state.endpointUrl,
        "channel_state": int(ch_state),
        "session_state": int(sess_state),
        "connect_status": str(connect_status),
    }


@mcp.tool()
async def get_endpoints(server_url: str) -> list[dict[str, Any]]:
    """List endpoints offered by an OPC UA server (no session required).

    Args:
        server_url: e.g. ``opc.tcp://localhost:4840``.
    """
    loop = asyncio.get_running_loop()
    client = o6.Client(server_url, loop=loop)
    try:
        await client.connect(noSession=True)
        endpoints = await client.getEndpoints(server_url)
    finally:
        try:
            await client.disconnect(closeSession=False)
        except Exception:  # noqa: BLE001
            pass
    out: list[dict[str, Any]] = []
    for ep in endpoints:
        out.append(
            {
                "endpoint_url": ep.endpointUrl,
                "security_mode": str(ep.securityMode),
                "security_policy_uri": ep.securityPolicyUri,
                "transport_profile_uri": ep.transportProfileUri,
            }
        )
    return out


# --------------------------------------------------------------------------- #
# Read / Write / Browse / Call
# --------------------------------------------------------------------------- #


@mcp.tool()
async def read(node_id: str, attribute: str = "VALUE") -> dict[str, Any]:
    """Read a node attribute.

    Args:
        node_id: OPC UA NodeId in string form, e.g. ``i=2258`` or ``ns=1;s=Temp``.
        attribute: AttributeId name, e.g. ``VALUE``, ``DISPLAYNAME``,
            ``DATATYPE``, ``NODECLASS``. Default: ``VALUE``.
    """
    client = _require_client()
    attr_id = getattr(o6.AttributeId, attribute.upper())
    value = await client.read(node_id, attr=attr_id)
    return {"node_id": node_id, "attribute": attribute, "value": _to_jsonable(value)}


@mcp.tool()
async def write(node_id: str, value: Any, attribute: str = "VALUE") -> dict[str, Any]:
    """Write a value to a node attribute.

    Args:
        node_id: OPC UA NodeId, e.g. ``ns=1;s=SetPoint``.
        value: JSON value to write (number, string, bool, list).
        attribute: AttributeId name (default ``VALUE``).
    """
    client = _require_client()
    attr_id = getattr(o6.AttributeId, attribute.upper())
    status_code = await client.write(node_id, value, attributeId=attr_id)
    return {"node_id": node_id, "status": str(status_code)}


@mcp.tool()
async def browse(
    node_id: str = "i=85",
    direction: str = "FORWARD",
    include_subtypes: bool = True,
) -> list[dict[str, Any]]:
    """Browse references of a node.

    Args:
        node_id: NodeId to browse from. Default ``i=85`` (Objects folder).
        direction: ``FORWARD``, ``INVERSE``, or ``BOTH``.
        include_subtypes: include subtypes of the reference type.
    """
    client = _require_client()
    dir_ = getattr(o6.ns.ns0.datatypes.BrowseDirection, direction.upper())
    refs = await client.browse(
        node_id,
        direction=dir_,
        refsubtypes=include_subtypes,
        resultMask=o6.ns.ns0.datatypes.BrowseResultMask.ALL,
    )
    out: list[dict[str, Any]] = []
    for r in refs:
        out.append(
            {
                "browse_name": str(r.browseName),
                "display_name": str(r.displayName),
                "node_id": str(r.nodeId),
                "node_class": r.nodeClass.name,
                "type_definition": str(r.typeDefinition),
                "reference_type_id": str(r.referenceTypeId),
                "is_forward": bool(r.isForward),
            }
        )
    return out


@mcp.tool()
async def browse_path(path: str) -> dict[str, Any]:
    """Resolve and read a value via dotted browse path under the Root node.

    Example::

        browse_path("Objects.Server.ServerStatus.CurrentTime")

    Args:
        path: dot-separated browse names, starting below the Root node.
    """
    client = _require_client()
    node = client.root
    parts = [p for p in path.split(".") if p]
    for part in parts:
        node = getattr(node, part)
    value = await node()
    return {"path": path, "value": _to_jsonable(value)}


@mcp.tool()
async def call_method(
    object_id: str,
    method_id: str,
    args: list[Any] | None = None,
) -> dict[str, Any]:
    """Invoke a method on the server.

    Args:
        object_id: NodeId of the object that owns the method.
        method_id: NodeId of the method.
        args: list of input arguments (defaults to no arguments).
    """
    client = _require_client()
    result = await client.call(object_id, method_id, args or [])
    return {"result": [_to_jsonable(r) for r in result]}


@mcp.tool()
async def get_server_info() -> dict[str, Any]:
    """Read common ServerStatus fields."""
    client = _require_client()
    base = "Objects.Server.ServerStatus"
    info: dict[str, Any] = {}
    for field in ("CurrentTime", "StartTime", "State"):
        try:
            node = client.root
            for p in (base + "." + field).split("."):
                node = getattr(node, p)
            info[field] = _to_jsonable(await node())
        except Exception as e:  # noqa: BLE001 - surface partial info
            info[field] = f"<error: {e}>"
    return info


# --------------------------------------------------------------------------- #
# Entry point
# --------------------------------------------------------------------------- #


def main() -> None:
    parser = argparse.ArgumentParser(description="o6 OPC UA MCP server")
    parser.add_argument(
        "--transport",
        choices=["stdio", "sse", "streamable-http"],
        default="stdio",
        help="MCP transport (default: stdio)",
    )
    parser.add_argument("--log-level", default="WARNING")
    args = parser.parse_args()

    logging.basicConfig(level=args.log_level.upper())
    mcp.run(transport=args.transport)


if __name__ == "__main__":
    main()
