# Copyright (c) 2026 o6 Automation GmbH
#
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
from __future__ import annotations
from typing import Any, TYPE_CHECKING, Optional
import asyncio

import o6
import numpy as np
from o6 import MaybeAwaitable, HasNodeId, NodeIdLike

if TYPE_CHECKING:
    from o6.client import Client


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


def _type2nodeclass(T: type) -> o6.AttributeId:
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
    elif T == View:
        return o6.NodeClass.VIEW
    raise Exception("Not a Node")


class Node(HasNodeId):
    def __init__(
        self,
        client: Client,
        nodeid: NodeIdLike,
        browse_name: o6.QualifiedName,
    ) -> None:
        assert isinstance(browse_name, o6.QualifiedName)
        self._client = client
        self._nodeid: o6.NodeId = o6.NodeId(nodeid)
        self._browse_name = browse_name
        self._children: Optional[
            dict[str, o6.ReferenceDescription | list[o6.ReferenceDescription] | Node]
        ] = None

    # Call Syntax
    def __call__(
        self, value: Optional[Any] = None, attr: Optional[o6.AttributeId | str] = None
    ) -> MaybeAwaitable[Any]:
        async def call():
            if isinstance(attr, str):
                attribute_id = _str2attributeid(attr)
            else:
                attribute_id = attr

            if value != None:
                res = await self._client.write(
                    self._nodeid, value=value, attribute_id=attribute_id
                )
                if res.code != 0:
                    raise Exception(f"Write failed with status {res}")
                return
            if attribute_id == o6.AttributeId.NODEID:
                return self._nodeid
            if attribute_id == o6.AttributeId.NODECLASS:
                return _type2nodeclass(type(self))
            if attribute_id == o6.AttributeId.BROWSENAME:
                return self._browse_name
            return await self._client.read(target=self._nodeid, attribute_id=attribute_id)

        return self._client._maybe_async(call())

    def _delete_cache(self):
        self._children = None

    # Dot Syntax
    async def _get_children(self):
        if self._children != None:
            return
        mask = o6.BrowseResultMask.BROWSENAME | o6.BrowseResultMask.NODECLASS
        children = await self._client.browse(self._nodeid, result_mask=mask)

        # A dict of the children (or a list if the name is not unique)
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
        node_child = nodeClassType(self._client, str(child.nodeid), child.browse_name)

        # For methods, keep around from which parent we got it.
        # This is then the default object on which the method is called.
        if nodeClassType == MethodNode and type(self) == ObjectNode:
            node_child._default_object = self._nodeid

        self._children[name_lower] = node_child  # Cache the node-child
        return node_child

    def __dir__(self):
        super_dir = super().__dir__()

        async def _dir():
            if self._children == None:
                await self._get_children()

            def child_name(child):
                if isinstance(child, list):
                    return child_name(child[0])
                if isinstance(child, Node):
                    return child._browse_name.name
                assert isinstance(child, o6.ReferenceDescription)
                return child.browse_name.name

            return super_dir + [child_name(c) for c in self._children.values()]

        fut = asyncio.run_coroutine_threadsafe(_dir(), self._client._loop)
        return fut.result()

    def __getattr__(self, name: str) -> Node | AwaitableNode:
        if name.startswith("_"):
            raise AttributeError(name)
        try:
            r = self._client._maybe_async(self._resolve_child(name))
            if isinstance(r, Node):
                return r
            return AwaitableNode(self._client, r)
        except Exception as e:
            raise AttributeError(name) from e

    # Index Syntax
    def __getitem__(self, key: str | o6.RelativePath) -> MaybeAwaitable[list[Any]]:
        async def _getitem() -> list[Any]:
            # Prepare the request
            bp = o6.BrowsePath()
            bp.starting_node = self._nodeid
            if isinstance(key, o6.RelativePath):
                bp.relative_path = key
            else:
                bp.relative_path = o6.RelativePath(key)  # type: ignore[call-arg]
            request = o6.TranslateBrowsePathsToNodeIdsRequest()
            request.browse_paths = [bp]

            # Call the service and check the result
            response = await self._client._service_translateBrowsePathsToNodeIds(
                request
            )
            if response.response_header.service_result.code != 0:
                raise Exception(
                    f"TranslateBrowsePathsToNodeIds failed: {response.response_header.service_result}"
                )
            result = response.results[0]
            if result.status_code.code != 0:
                raise KeyError(
                    f"Could not resolve browse path {key!r}: {result.status_code}"
                )
            if not result.targets:
                raise KeyError(f"No node found for browse path {key!r}")

            # Resolve the results and return
            async def browse_path_result_to_node(bpr):
                if bpr.remaining_path_index != np.iinfo(np.uint32).max:
                    return bpr
                target = bpr.target_id
                if len(target.nsu) > 0 or target.svr != 0:
                    return target
                return await self._client[str(target)]

            return [await browse_path_result_to_node(x) for x in result.targets]

        return self._client._maybe_async(_getitem())


class AwaitableNode:

    def __init__(self, client: Client, awaitable: Any) -> None:
        self._client = client
        self._awaitable = awaitable

    def __await__(self):
        return self._awaitable.__await__()

    def __getattr__(self, name: str) -> AwaitableNode:
        if name.startswith("_"):
            raise AttributeError(name)
        parent = self._awaitable
        client = self._client

        async def chain() -> Node:
            node = await parent
            return await node._resolve_child(name)

        return AwaitableNode(client, chain())

    def __call__(self, *args: Any, **kwargs: Any) -> AwaitableNode:
        parent = self._awaitable
        client = self._client

        async def chain() -> Any:
            node = await parent
            result = node(*args, **kwargs)
            if hasattr(result, "__await__"):
                return await result
            return result

        return AwaitableNode(client, chain())


class ObjectNode(Node):
    pass


class VariableNode(Node):
    def __call__(
        self, value: Optional[Any] = None, attr: Optional[o6.AttributeId | str] = None
    ) -> MaybeAwaitable[Any]:
        if attr == None:
            attr = o6.AttributeId.VALUE
        return super().__call__(attr=attr, value=value)


class VariableTypeNode(Node):
    def __call__(
        self, value: Optional[Any] = None, attr: Optional[o6.AttributeId | str] = None
    ) -> MaybeAwaitable[Any]:
        if attr == None:
            attr = o6.AttributeId.VALUE
        return super().__call__(attr=attr, value=value)


class MethodNode(Node):
    _default_object: o6.NodeId | None

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
        return self._client.call(object_id, self._nodeid, list(args))


class ObjectTypeNode(Node):
    pass


class ReferenceTypeNode(Node):
    pass


class DataTypeNode(Node):
    pass


class ViewNode(Node):
    pass
