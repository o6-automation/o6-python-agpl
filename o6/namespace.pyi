# Copyright 2026 (c) o6 Automation GmbH
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
    """Generic node-hierarchy entry: holds a NodeId and child node attributes.

    Used for Object, Variable, Method, ObjectType, VariableType, ReferenceType,
    and View nodes.  DataType nodes use :class:`NamespaceDataTypeNode`.

    ``node()`` returns the NodeId.  ``o6.NodeId(node)`` also yields the NodeId
    via the ``HasNodeId`` protocol (``node._nodeid``).
    """

    _nodeid: o6.NodeId
    def __init__(self, nodeid: NodeIdLike) -> None: ...
    def __call__(self) -> o6.NodeId: ...

class NamespaceDataTypeNode(NamespaceNode):
    """Node-hierarchy entry for a DataType.

    Carries the DataType's NodeId plus an optional reference to the concrete
    Python class (``_datatype``) used to instantiate values of that type.

    Calling the wrapper:
      * If ``_datatype`` is set (concrete DataType) → returns a
        default-constructed instance, e.g. ``np.int32(0)`` for ``Int32`` or
        ``o6.Argument()`` for ``Argument``.
      * Otherwise → raises ``TypeError``.  Reasons ``_datatype`` can be
        ``None``:

        * **Abstract/organisational DataTypes** with no concrete Python class
          — e.g. ``BaseDataType``, ``Number``, ``Integer``, ``UInteger``.
        * **Custom namespace DataTypes** whose nodeset XML carries no
          struct/enum definition (pure hierarchy nodes).

    ``o6.NodeId(wrapper)`` always yields the NodeId via ``_nodeid``.
    """

    _datatype: type | None
    def __init__(self, nodeid: NodeIdLike, datatype: type | None = None) -> None: ...
    def __call__(self) -> Any: ...

class Namespace:
    metadata: NamespaceMetadata
    _required_namespaces: List[Dict[str, str]]
    _structure_descriptions: List[Any]
    _enum_descriptions: List[Any]
    _types: SimpleNamespace
    _capsule: list[Any] | None
    _canonical_ns_table: Dict[str, int]
    _original_nodeids: tuple[list[tuple[str, str | None, list[str]]], list[str]] | None
    _abstract_data_types: set[str]

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
