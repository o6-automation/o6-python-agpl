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
from typing import Any, Optional, TYPE_CHECKING

import o6
from o6 import MaybeAwaitable, HasNodeId, NodeIdLike, AttributeId

if TYPE_CHECKING:
    from o6.client import Client

def _nodeclass2type(node_class: o6.NodeClass) -> type[Node]: ...

class Node(HasNodeId):
    _client: Client
    _nodeid: o6.NodeId
    _browse_name: o6.QualifiedName

    def __init__(
        self,
        client: Client,
        nodeid: NodeIdLike,
        browse_name: o6.QualifiedName,
    ) -> None: ...
    def __call__(
        self,
        value: Optional[Any] = None,
        attr: Optional[AttributeId | str] = None,
    ) -> MaybeAwaitable[Any]: ...
    def __getattr__(self, name: str) -> Node | AwaitableNode: ...
    def __getitem__(self, key: str | o6.RelativePath) -> MaybeAwaitable[list[Any]]: ...
    def _delete_cache(self) -> None:
        """Empty the cache of known child-nodes.
        This forces a re-browsing on the next access.
        """
        ...

class AwaitableNode:
    """Supports chaining __getattr__ without intermediate awaits.

    Example::

        var = await client.root.objects.myfolder.myvariable
    """

    def __init__(self, client: Client, awaitable: Any) -> None: ...
    def __await__(self) -> Any: ...
    def __getattr__(self, name: str) -> AwaitableNode: ...
    def __call__(self, *args: Any, **kwargs: Any) -> AwaitableNode: ...

class ObjectNode(Node): ...

class VariableNode(Node):
    def __call__(
        self,
        value: Optional[Any] = None,
        attr: Optional[AttributeId | str] = None,
    ) -> MaybeAwaitable[Any]: ...

class VariableTypeNode(Node):
    def __call__(
        self,
        value: Optional[Any] = None,
        attr: Optional[AttributeId | str] = None,
    ) -> MaybeAwaitable[Any]: ...

class MethodNode(Node):
    _default_object: o6.NodeId  # The default is to call the method in the
    # context of the parent object

    def __call__(
        self,
        *args: Any,
        object_id: Optional[o6.NodeId] = None,
        attr: Optional[AttributeId | str] = None,
        value: Optional[Any] = None,
    ) -> MaybeAwaitable[Any]: ...

class ObjectTypeNode(Node): ...
class ReferenceTypeNode(Node): ...
class DataTypeNode(Node): ...
class ViewNode(Node): ...
