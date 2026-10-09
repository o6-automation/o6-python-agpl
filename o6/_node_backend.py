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

"""Private client/server adapters behind the public Node API."""

from __future__ import annotations

import asyncio
import inspect
import weakref
from typing import TYPE_CHECKING, Any, Callable, cast

import o6
from o6._dispatch import public_result
from o6.util import _index_range_to_string

if TYPE_CHECKING:
    from o6.client import Client
    from o6.node import Node
    from o6.server import Server


def _without_traceback(exc: Exception) -> Exception:
    """Return *exc* without traceback frames from an internal sync/async bridge."""
    exc.__traceback__ = None
    return exc


def _attribute_id(value: o6.AttributeId | str) -> o6.AttributeId:
    """Normalize one public attribute spelling without involving a backend."""
    if not isinstance(value, str):
        return value
    normalized = "".join(ch for ch in value.lower() if ch.isalnum())
    for attribute_id in o6.AttributeId:
        candidate = "".join(ch for ch in attribute_id.name.lower() if ch.isalnum())
        if candidate == normalized:
            return attribute_id
    raise ValueError(f"Unknown AttributeId: {value!r}")


def _targets_and_ranges(
    target: o6.NodeIdLike | list[o6.NodeIdLike],
    index_range: o6.IndexRange | list[o6.IndexRange],
) -> tuple[bool, list[o6.NodeIdLike], list[str | None]]:
    """Return scalar shape, target list, and one normalized range per target."""
    is_scalar = not isinstance(target, list)
    targets = (
        [cast(o6.NodeIdLike, target)] if is_scalar else list(cast(list[o6.NodeIdLike], target))
    )
    if isinstance(index_range, list):
        if len(index_range) != len(targets):
            raise ValueError(
                f"range list length {len(index_range)} does not match "
                f"target list length {len(targets)}"
            )
        ranges = [_index_range_to_string(item) for item in index_range]
    elif index_range is not None:
        ranges = [_index_range_to_string(index_range)] * len(targets)
    else:
        ranges = [None] * len(targets)
    return is_scalar, targets, ranges


def _child_browse_result_mask() -> int:
    from o6.ns import ns0

    return int(
        ns0.datatypes.BrowseResultMask.NODE_CLASS | ns0.datatypes.BrowseResultMask.BROWSE_NAME
    )


async def _resolve_path_result(backend: Any, result: Any, path: Any) -> list[Any]:
    if result.statusCode != 0:
        raise KeyError(f"Could not resolve browse path {path!r}: {result.statusCode}")
    if not result.targets:
        raise KeyError(f"No node found for browse path {path!r}")

    async def result_to_node(target_result: Any) -> Any:
        if target_result.remainingPathIndex != (1 << 32) - 1:
            return target_result
        target = target_result.targetId
        if target.nsu or target.svr != 0:
            return target
        return await backend.node_get(str(target))

    return [await result_to_node(target) for target in result.targets]


def _make_browse_path(node: Node, path: Any) -> Any:
    from o6.ns import ns0

    browse_path = ns0.datatypes.BrowsePath()
    browse_path.startingNode = node._nodeid
    browse_path.relativePath = (
        path if isinstance(path, ns0.datatypes.RelativePath) else ns0.datatypes.RelativePath(path)
    )
    return browse_path


class _ClientBackend:
    def __init__(self, client: Client) -> None:
        self._client = client
        self.nodes: weakref.WeakSet[Node] = weakref.WeakSet()

    def invalidate_children(self, target: Any = None) -> None:
        nodeid = o6.NodeId(target) if target is not None else None
        for node in self.nodes:
            if nodeid is None or node._nodeid == nodeid:
                node._child_cache = None

    @property
    def loop(self) -> asyncio.AbstractEventLoop:
        return self._client._loop

    def dispatch(self, coro: Any) -> o6.MaybeAwaitable:
        return self._client._maybe_async(coro)

    async def browse_children(self, nodeid: Any) -> list:
        result = self._client.browse(
            nodeid,
            resultMask=_child_browse_result_mask(),
        )
        resolved = (await result) if inspect.isawaitable(result) else result
        return cast(list, resolved)

    async def node_read(self, nodeid: Any, attr: Any) -> Any:
        result = self._client.read(target=nodeid, attr=attr)
        return (await result) if inspect.isawaitable(result) else result

    async def node_write(self, nodeid: Any, value: Any, attr: Any) -> None:
        result = self._client.write(nodeid, value=value, attr=attr)
        if inspect.isawaitable(result):
            result = await result
        cast(o6.StatusCode, result).check()

    async def node_call(self, obj_id: Any, method_id: Any, args: Any) -> tuple:
        result = self._client.call(obj_id, method_id, args)
        result = (await result) if inspect.isawaitable(result) else result
        result[0].check()
        return result

    async def node_resolve_path(self, node: Node, path: Any) -> list[Any]:
        from o6.ns import ns0

        request = ns0.datatypes.TranslateBrowsePathsToNodeIdsRequest()
        request.browsePaths = [_make_browse_path(node, path)]
        result = self._client._service_translateBrowsePathsToNodeIds(request)
        response = (await result) if inspect.isawaitable(result) else result
        response.responseHeader.serviceResult.check(message="TranslateBrowsePathsToNodeIds")
        if len(response.results) != 1:
            raise RuntimeError("TranslateBrowsePathsToNodeIds returned an unexpected result count")
        return await _resolve_path_result(self, response.results[0], path)

    async def node_get(self, nodeid: Any) -> Node:
        result = self._client[str(nodeid)]
        return (await result) if inspect.isawaitable(result) else result


class _ServerBackend:
    def __init__(self, server: Server) -> None:
        self._server_ref = weakref.ref(server)

    @property
    def _server(self) -> Server:
        server = self._server_ref()
        if server is None:
            raise ReferenceError("server node is detached")
        return server

    @property
    def loop(self) -> asyncio.AbstractEventLoop:
        return self._server._loop

    def dispatch(self, coro: Any) -> o6.MaybeAwaitable:
        loop = self._server._loop
        try:
            running = asyncio.get_running_loop()
        except RuntimeError:
            running = None
        if running is loop:
            return loop.create_task(coro)
        return self._server._maybe_async_coro(coro)

    @public_result
    def dispatch_native(self, operation: Callable[[], Any]) -> Any:
        result = self._server._on_event_loop(operation)
        if inspect.isawaitable(result):
            try:
                running = asyncio.get_running_loop()
            except RuntimeError:
                running = None
            if asyncio.isfuture(result) and result.get_loop() is running:
                return result
            return self._server._maybe_async(result)
        return result

    def node_call_native(self, obj_id: Any, method_id: Any, args: Any) -> Any:
        return self.dispatch_native(
            lambda: self._server._call(o6.NodeId(obj_id), o6.NodeId(method_id), args)
        )

    async def browse_children(self, node: Node) -> list:
        return self.browse_children_native(node)

    def browse_children_native(self, node: Node) -> list:
        from o6.ns import ns0

        description = ns0.datatypes.BrowseDescription(
            nodeId=o6.NodeId(node),
            browseDirection=ns0.datatypes.BrowseDirection.FORWARD,
            referenceTypeId=o6.NodeId(ns0.reftypes.HierarchicalReferences),
            includeSubtypes=True,
            resultMask=_child_browse_result_mask(),
        )
        return self._server._browse_references(node, description)

    async def node_call(self, obj_id: Any, method_id: Any, args: Any) -> tuple:
        result = self._server.call(o6.NodeId(obj_id), o6.NodeId(method_id), args)
        result = (await result) if inspect.isawaitable(result) else result
        result[0].check()
        return result

    async def node_resolve_path(self, node: Node, path: Any) -> list[Any]:
        browse_path = _make_browse_path(node, path)
        result = self._server._translate_browse_paths_to_nodeids(browse_path, node)
        resolved = (await result) if inspect.isawaitable(result) else result
        return await _resolve_path_result(self, resolved, path)

    async def node_get(self, nodeid: Any, node_type: type[Node] | None = None) -> Node:
        return self.node_get_native(nodeid, node_type)

    def node_get_native(self, nodeid: Any, node_type: type[Node] | None = None) -> Node:
        from o6.node import VariableNode, _nodeclass2type
        from o6.ns import ns0

        if node_type is None:
            result = self._server._read_attribute(o6.NodeId(nodeid), int(o6.AttributeId.NODE_CLASS))
            nodeclass = result.result() if asyncio.isfuture(result) else result
            node_type = _nodeclass2type(ns0.datatypes.NodeClass(nodeclass))
        if node_type is VariableNode:
            type_id = self._server._get_node_type(o6.NodeId(nodeid))
            node_type = self._server._variable_instance_type(type_id)
        return self._server._get_node(o6.NodeId(nodeid), node_type, self)


def _server_node(server: Server, node_id: Any, node_type: type[Node]) -> Node:
    """Return the server-owned Python wrapper for an existing native node."""
    return cast(Any, server._get_node(o6.NodeId(node_id), node_type, server._node_backend))
