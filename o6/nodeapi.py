# Copyright 2026 (c) o6 Automation GmbH
from __future__ import annotations
from typing import Any, TYPE_CHECKING, Optional, Protocol, runtime_checkable
import asyncio
import concurrent.futures
import inspect

import o6
import numpy as np
from o6 import MaybeAwaitable, HasNodeId, NodeIdLike

if TYPE_CHECKING:
    from o6.client import Client
    from o6.server import Server


# ---------------------------------------------------------------------------
# NodeBackend protocol
# ---------------------------------------------------------------------------


@runtime_checkable
class NodeBackend(Protocol):
    @property
    def loop(self) -> asyncio.AbstractEventLoop: ...
    def dispatch(self, coro) -> MaybeAwaitable: ...
    async def node_browse(self, nodeid, result_mask) -> list: ...
    async def node_read(self, nodeid, attr) -> Any: ...
    async def node_write(self, nodeid, value, attr) -> None: ...
    async def node_call(self, obj_id, method_id, args) -> tuple: ...
    async def node_translate(self, request) -> Any: ...
    async def node_delete(self, nodeid) -> None: ...
    async def node_get(self, nodeid) -> Node: ...


# ---------------------------------------------------------------------------
# ClientBackend
# ---------------------------------------------------------------------------


class ClientBackend:
    def __init__(self, client: Client) -> None:
        self._client = client

    @property
    def loop(self) -> asyncio.AbstractEventLoop:
        return self._client._loop

    def dispatch(self, coro) -> MaybeAwaitable:
        return self._client._maybe_async(coro)

    async def node_browse(self, nodeid, result_mask) -> list:
        r = self._client.browse(nodeid, result_mask=result_mask)
        return (await r) if inspect.isawaitable(r) else r

    async def node_read(self, nodeid, attr) -> Any:
        r = self._client.read(target=nodeid, attr=attr)
        return (await r) if inspect.isawaitable(r) else r

    async def node_write(self, nodeid, value, attr) -> None:
        r = self._client.write(nodeid, value=value, attr=attr)
        if inspect.isawaitable(r):
            await r

    async def node_call(self, obj_id, method_id, args) -> tuple:
        r = self._client.call(obj_id, method_id, args)
        return (await r) if inspect.isawaitable(r) else r

    async def node_translate(self, request) -> Any:
        r = self._client._service_translateBrowsePathsToNodeIds(request)
        return (await r) if inspect.isawaitable(r) else r

    async def node_get(self, nodeid) -> Node:
        r = self._client[str(nodeid)]
        return (await r) if inspect.isawaitable(r) else r


# ---------------------------------------------------------------------------
# ServerBackend
# ---------------------------------------------------------------------------


class ServerBackend:
    def __init__(self, server: Server) -> None:
        self._server = server

    @property
    def loop(self) -> asyncio.AbstractEventLoop:
        return self._server._loop

    def dispatch(self, coro) -> MaybeAwaitable:
        loop = self._server._loop
        try:
            running = asyncio.get_running_loop()
        except RuntimeError:
            running = None
        if running is loop:
            # We're on the server's loop (e.g. async test or server callback).
            # ServerBackend coroutines wrap synchronous C calls — they never
            # actually yield, so we can drive them to completion inline rather
            # than returning an unawaited Task to sync callers (like .value).
            try:
                coro.send(None)
            except StopIteration as exc:
                return exc.value
            # Coroutine yielded unexpectedly — fall back to a task
            return loop.create_task(coro)
        return self._server._maybe_async_coro(coro)

    async def node_browse(self, nodeid, result_mask) -> list:
        return self._server.browse_node(o6.NodeId(nodeid), int(result_mask))

    async def node_read(self, nodeid, attr) -> Any:
        if attr is None:
            attr = o6.AttributeId.VALUE
        r = self._server.read(o6.NodeId(nodeid), attr=attr)
        return (await r) if inspect.isawaitable(r) else r

    async def node_write(self, nodeid, value, attr) -> None:
        r = self._server.write(
            o6.NodeId(nodeid), value, attr=attr or o6.AttributeId.VALUE
        )
        if inspect.isawaitable(r):
            await r

    async def node_call(self, obj_id, method_id, args) -> tuple:
        r = self._server.call(o6.NodeId(obj_id), o6.NodeId(method_id), args)
        return (await r) if inspect.isawaitable(r) else r

    async def node_translate(self, request) -> Any:
        return self._server.translate_browse_paths(request)

    async def node_delete(self, nodeid) -> None:
        self._server.delete_node(o6.NodeId(nodeid))

    async def node_get(self, nodeid) -> Node:
        nc_int, browse_name = self._server.read_node_info(o6.NodeId(nodeid))
        NodeType = _nodeclass2type(o6.NodeClass(nc_int))
        return NodeType(self, nodeid, browse_name)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _str2attributeid(s: str) -> o6.AttributeId:
    normalized = "".join(ch for ch in s.lower() if ch.isalnum())
    for attribute_id in o6.AttributeId:
        candidate = "".join(ch for ch in attribute_id.name.lower() if ch.isalnum())
        if candidate == normalized:
            return attribute_id
    raise ValueError(f"Unknown AttributeId: {s!r}")


def _nodeclass2type(nc: o6.NodeClass) -> type:
    if nc == o6.NodeClass.OBJECT:
        return ObjectNode
    elif nc == o6.NodeClass.VARIABLE:
        return VariableNode
    elif nc == o6.NodeClass.METHOD:
        return MethodNode
    elif nc == o6.NodeClass.OBJECTTYPE:
        return ObjectTypeNode
    elif nc == o6.NodeClass.VARIABLETYPE:
        return VariableTypeNode
    elif nc == o6.NodeClass.REFERENCETYPE:
        return ReferenceTypeNode
    elif nc == o6.NodeClass.DATATYPE:
        return DataTypeNode
    elif nc == o6.NodeClass.VIEW:
        return ViewNode
    raise Exception("Unknown NodeClass")


def _type2nodeclass(T: type) -> o6.NodeClass:
    if T == ObjectNode:
        return o6.NodeClass.OBJECT
    elif T == VariableNode:
        return o6.NodeClass.VARIABLE
    elif T == MethodNode:
        return o6.NodeClass.METHOD
    elif T == ObjectTypeNode:
        return o6.NodeClass.OBJECTTYPE
    elif T == VariableTypeNode:
        return o6.NodeClass.VARIABLETYPE
    elif T == ReferenceTypeNode:
        return o6.NodeClass.REFERENCETYPE
    elif T == DataTypeNode:
        return o6.NodeClass.DATATYPE
    elif T == ViewNode:
        return o6.NodeClass.VIEW
    raise Exception("Not a Node")


# ---------------------------------------------------------------------------
# Node classes
# ---------------------------------------------------------------------------


class Node(HasNodeId):
    def __init__(
        self,
        backend: NodeBackend,
        nodeid: NodeIdLike,
        browse_name: o6.QualifiedName,
    ) -> None:
        assert isinstance(browse_name, o6.QualifiedName)
        self._backend = backend
        self._nodeid: o6.NodeId = o6.NodeId(nodeid)
        self._browse_name = browse_name
        self._children: Optional[
            dict[str, o6.ReferenceDescription | list[o6.ReferenceDescription] | Node]
        ] = None

    @property
    def backend(self) -> NodeBackend:
        return self._backend

    @property
    def nodeid(self) -> o6.NodeId:
        return self._nodeid

    def __str__(self) -> str:
        return str(self._nodeid)

    def __repr__(self) -> str:
        return f"{self._browse_name}: {type(self).__name__}({self._nodeid})"

    def delete(self) -> None:
        self._backend.dispatch(self._backend.node_delete(self._nodeid))

    # Call Syntax
    def __call__(
        self, value: Optional[Any] = None, attr: Optional[o6.AttributeId | str] = None
    ) -> MaybeAwaitable[Any]:
        async def call():
            if isinstance(attr, str):
                attribute_id = _str2attributeid(attr)
            else:
                attribute_id = attr

            if value is not None:
                res = await self._backend.node_write(
                    self._nodeid, value=value, attr=attribute_id
                )
                if hasattr(res, "code") and res.code != 0:
                    raise Exception(f"Write failed with status {res}")
                return
            if attribute_id == o6.AttributeId.NODEID:
                return self._nodeid
            if attribute_id == o6.AttributeId.NODECLASS:
                return _type2nodeclass(type(self))
            if attribute_id == o6.AttributeId.BROWSENAME:
                return self._browse_name
            return await self._backend.node_read(self._nodeid, attr=attribute_id)

        return self._backend.dispatch(call())

    def _delete_cache(self):
        self._children = None

    # Dot Syntax
    async def _get_children(self):
        if self._children is not None:
            return
        mask = o6.BrowseResultMask.BROWSENAME | o6.BrowseResultMask.NODECLASS
        children = await self._backend.node_browse(self._nodeid, mask)

        self._children = dict()
        for c in children:
            key = c.browse_name.name.lower()
            old = self._children.get(key, None)
            if old is not None:
                if isinstance(old, list):
                    old.append(c)
                else:
                    self._children[key] = [old, c]
            else:
                self._children[key] = c

    async def _resolve_child(self, name: str) -> Node:
        if self._children is None:
            await self._get_children()
        assert self._children is not None
        name_lower = name.lower()
        child = self._children.get(name_lower, None)
        if child is None:
            raise Exception(f"Child-node {name} not found")
        if isinstance(child, list):
            raise Exception(f"Not unique, {len(child)} child-nodes match {name}")
        if isinstance(child, Node):
            return child

        nodeClassType = _nodeclass2type(child.node_class)
        node_child = nodeClassType(self._backend, str(child.nodeid), child.browse_name)

        if nodeClassType == MethodNode and type(self) == ObjectNode:
            node_child._default_object = self._nodeid

        self._children[name_lower] = node_child
        return node_child

    def __dir__(self):
        super_dir = super().__dir__()

        async def _dir():
            if self._children is None:
                await self._get_children()

            def child_name(child):
                if isinstance(child, list):
                    return child_name(child[0])
                if isinstance(child, Node):
                    return child._browse_name.name
                assert isinstance(child, o6.ReferenceDescription)
                return child.browse_name.name

            return super_dir + [child_name(c) for c in self._children.values()]

        fut = asyncio.run_coroutine_threadsafe(_dir(), self._backend.loop)
        return fut.result()

    def __getattr__(self, name: str) -> Node | AwaitableNode:
        if name.startswith("_"):
            raise AttributeError(name)
        try:
            r = self._backend.dispatch(self._resolve_child(name))
            if isinstance(r, Node):
                return r
            return AwaitableNode(self._backend, r)
        except Exception as e:
            raise AttributeError(name) from e

    # Index Syntax
    def __getitem__(self, key: str | o6.RelativePath) -> MaybeAwaitable[list[Any]]:
        async def _getitem() -> list[Any]:
            bp = o6.BrowsePath()
            bp.starting_node = self._nodeid
            if isinstance(key, o6.RelativePath):
                bp.relative_path = key
            else:
                bp.relative_path = o6.RelativePath(key)  # type: ignore[call-arg]
            request = o6.TranslateBrowsePathsToNodeIdsRequest()
            request.browse_paths = [bp]

            response = await self._backend.node_translate(request)
            if response.response_header.service_result != 0:
                raise Exception(
                    f"TranslateBrowsePathsToNodeIds failed: {response.response_header.service_result}"
                )
            result = response.results[0]
            if result.status_code != 0:
                raise KeyError(
                    f"Could not resolve browse path {key!r}: {result.status_code}"
                )
            if not result.targets:
                raise KeyError(f"No node found for browse path {key!r}")

            async def browse_path_result_to_node(bpr):
                if bpr.remaining_path_index != np.iinfo(np.uint32).max:
                    return bpr
                target = bpr.target_id
                if len(target.nsu) > 0 or target.svr != 0:
                    return target
                return await self._backend.node_get(str(target))

            return [await browse_path_result_to_node(x) for x in result.targets]

        return self._backend.dispatch(_getitem())


class AwaitableNode:

    def __init__(self, backend: NodeBackend, awaitable: Any) -> None:
        self._backend = backend
        self._awaitable = awaitable

    def __await__(self):
        return self._awaitable.__await__()

    def __getattr__(self, name: str) -> AwaitableNode:
        if name.startswith("_"):
            raise AttributeError(name)
        parent = self._awaitable
        backend = self._backend

        async def chain() -> Node:
            node = await parent
            return await node._resolve_child(name)

        return AwaitableNode(backend, chain())

    def __call__(self, *args: Any, **kwargs: Any) -> AwaitableNode:
        parent = self._awaitable
        backend = self._backend

        async def chain() -> Any:
            node = await parent
            result = node(*args, **kwargs)
            if hasattr(result, "__await__"):
                return await result
            return result

        return AwaitableNode(backend, chain())


class ObjectNode(Node):
    pass


class VariableNode(Node):
    @property
    def value(self) -> Any:
        result = self._backend.dispatch(
            self._backend.node_read(self._nodeid, o6.AttributeId.VALUE)
        )
        return result

    @value.setter
    def value(self, v: Any) -> None:
        self._backend.dispatch(
            self._backend.node_write(self._nodeid, v, o6.AttributeId.VALUE)
        )

    def __call__(
        self, value: Optional[Any] = None, attr: Optional[o6.AttributeId | str] = None
    ) -> MaybeAwaitable[Any]:
        if attr is None:
            attr = o6.AttributeId.VALUE
        return super().__call__(attr=attr, value=value)


class VariableTypeNode(Node):
    def __call__(
        self, value: Optional[Any] = None, attr: Optional[o6.AttributeId | str] = None
    ) -> MaybeAwaitable[Any]:
        if attr is None:
            attr = o6.AttributeId.VALUE
        return super().__call__(attr=attr, value=value)


class MethodNode(Node):
    _default_object: o6.NodeId | None = None

    def __call__(
        self,
        *args: Any,
        object_id: Optional[o6.NodeId] = None,
        attr: Optional[o6.AttributeId | str] = None,
        value: Optional[Any] = None,
    ) -> MaybeAwaitable[Any]:
        if attr is not None or value is not None:
            if len(args) != 0:
                raise Exception(
                    "Method-call syntax and attribute-access syntax do not mix"
                )
            if attr is None:
                attr = o6.AttributeId.VALUE
            return super().__call__(attr=attr, value=value)
        if object_id is None:
            if self._default_object is None:
                raise Exception(
                    "The object on which the method shall be called could not be automatically inferred"
                )
            object_id = self._default_object
        return self._backend.dispatch(
            self._backend.node_call(object_id, self._nodeid, list(args))
        )


class ObjectTypeNode(Node):
    pass


class ReferenceTypeNode(Node):
    pass


class DataTypeNode(Node):
    pass


class ViewNode(Node):
    pass
