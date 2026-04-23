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
from types import SimpleNamespace
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
import o6
from o6._o6.types_builtin import NodeIdLike

if TYPE_CHECKING:
    import o6

class NamespaceMetadata:
    index: int | None
    short_name: str
    uri: str
    version: str
    publication_date: Optional[str]

class NamespaceNode(SimpleNamespace, o6.HasNodeId):
    _nodeid: o6.NodeId
    def __init__(self, nodeid: NodeIdLike) -> None: ...
    def __call__(self) -> o6.NodeId: ...

class NamespaceObjectNode(NamespaceNode): ...
class NamespaceVariableNode(NamespaceNode): ...
class NamespaceMethodNode(NamespaceNode): ...
class NamespaceObjectTypeNode(NamespaceNode): ...
class NamespaceVariableTypeNode(NamespaceNode): ...
class NamespaceReferenceTypeNode(NamespaceNode): ...

class NamespaceDataTypeNode(NamespaceNode):
    def __init__(self, nodeid: NodeIdLike, datatype: type | None) -> None: ...
    def __call__(self) -> o6.NodeId: ...

class NamespaceViewNode(NamespaceNode): ...

class Namespace:
    metadata: NamespaceMetadata
    _required_namespaces: List[Dict[str, str]]
    _structure_descriptions: List[Any]
    _enum_descriptions: List[Any]
    _types: SimpleNamespace
    _capsule: list[Any] | None
    _canonical_ns_table: Dict[str, int]
    _original_nodeids: tuple[list[tuple[str, str | None, list[str]]], list[str]] | None

    # The following are SimpleNamespace with values of NamespaceNode
    objects: SimpleNamespace  # Object, Variable, Method
    datatypes: SimpleNamespace  # DataTypeNode
    eventtypes: (
        SimpleNamespace  # ObjectTypeNode (parent EventType or name with "EventType")
    )
    ifacetypes: SimpleNamespace  # ObjectTypeNode
    objtypes: SimpleNamespace  # ObjectTypeNode
    reftypes: SimpleNamespace  # ReferenceTypeNode
    vartypes: SimpleNamespace  # VariableTypeNode
    views: SimpleNamespace  # ViewNode

    def __init__(
        self, uri: str, version: str = "", publication_date: Optional[str] = None
    ) -> None: ...
    def _copy_for_rebuild(self) -> Namespace: ...
    def _add_required_namespace(self, uri: str, version: str = "") -> None: ...
    def _add_structure_description(
        self,
        nodeid: str,
        browse_name: str,
        struct_data: Dict[str, Any] | o6.StructureDefinition,
        default_encoding_id: str | None = None,
    ) -> None: ...
    def _add_enum_description(
        self,
        nodeid: str,
        browse_name: str,
        enum_definition: Dict[str, Any],
    ) -> None: ...
