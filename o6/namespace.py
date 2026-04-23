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

from typing import List, Dict, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from types import SimpleNamespace
import o6

if TYPE_CHECKING:
    import o6


@dataclass
class NamespaceMetadata:
    index: int | None
    short_name: str
    uri: str
    version: str
    publication_date: Optional[str]


class NamespaceNode(SimpleNamespace, o6.HasNodeId):
    def __init__(self, nodeid) -> None:
        super().__init__()
        self._nodeid: o6.NodeId = o6.NodeId(nodeid)

    def __call__(self) -> o6.NodeId:
        return self._nodeid


class NamespaceObjectNode(NamespaceNode):
    pass


class NamespaceVariableNode(NamespaceNode):
    pass


class NamespaceMethodNode(NamespaceNode):
    pass


class NamespaceObjectTypeNode(NamespaceNode):
    pass


class NamespaceVariableTypeNode(NamespaceNode):
    pass


class NamespaceReferenceTypeNode(NamespaceNode):
    pass


class NamespaceDataTypeNode(NamespaceNode):
    def __init__(self, nodeid: Any, datatype: type | None) -> None:
        super().__init__(nodeid)
        self._datatype: type | None = datatype

    def __call__(self) -> o6.NodeId:
        return self._nodeid


class NamespaceViewNode(NamespaceNode):
    pass


class Namespace:
    def __init__(
        self, uri: str, version: str = "", publication_date: Optional[str] = None
    ) -> None:
        self.metadata = NamespaceMetadata(
            index=None,
            short_name=self._extract_short_name(uri),
            uri=uri,
            version=version,
            publication_date=publication_date,
        )

        self._required_namespaces: List[Dict[str, str]] = []

        self._structure_descriptions: List[o6.StructureDescription] = []
        self._enum_descriptions: List[o6.EnumDescription] = []

        self._types: SimpleNamespace = SimpleNamespace()

        # holds the owner PyCapsule that keeps the UA_DataType array alive
        # independent of any client/server.
        self._capsule: Any = None

        # Full canonical namespace table snapshot (URI → index) at build
        # time.  Used by clients to register all slots (incl. transitive
        # deps) so that canonical indices are reproduced exactly.
        self._canonical_ns_table: Dict[str, int] = {}

        # Original (pre-remap) NodeId strings for each description.
        # Stored before the first remap so that servers can rebuild from
        # original XML indices without re-parsing the XML.
        # Format: (struct_tuples, enum_id_strings) where each struct tuple
        # is (data_type_id, default_encoding_id | None, [field_data_types]).
        self._original_nodeids: (
            tuple[list[tuple[str, str | None, list[str]]], list[str]] | None
        ) = None

        # Node hierarchy containers — populated eagerly by the type loader or
        # _parse_nodeset_prebuilt.  Plain attributes; no lazy access overhead.
        self.objects: SimpleNamespace = SimpleNamespace()  # Object, Variable, Method
        self.datatypes: SimpleNamespace = SimpleNamespace()  # DataTypeNode
        self.eventtypes: SimpleNamespace = (
            SimpleNamespace()
        )  # ObjectTypeNode (parent EventType or name with "EventType")
        self.ifacetypes: SimpleNamespace = SimpleNamespace()  # ObjectTypeNode
        self.objtypes: SimpleNamespace = SimpleNamespace()  # ObjectTypeNode
        self.reftypes: SimpleNamespace = SimpleNamespace()  # ReferenceTypeNode
        self.vartypes: SimpleNamespace = SimpleNamespace()  # VariableTypeNode
        self.views: SimpleNamespace = SimpleNamespace()  # ViewNode

    def __dir__(self) -> list[str]:
        containers = [
            "objects",
            "datatypes",
            "eventtypes",
            "ifacetypes",
            "objtypes",
            "reftypes",
            "vartypes",
            "views",
        ]
        return ["metadata"] + containers + list(vars(self._types).keys())

    def __getattr__(self, name: str) -> Any:
        try:
            return getattr(object.__getattribute__(self, "_types"), name)
        except AttributeError:
            raise AttributeError(
                f"'{type(self).__name__}' object has no attribute '{name}'"
            ) from None

    def _copy_for_rebuild(self) -> Namespace:
        """Create a shallow copy suitable for rebuilding types with different
        namespace indices.  Copies metadata and original NodeIds but not
        built capsules or types."""
        d = Namespace(
            self.metadata.uri, self.metadata.version, self.metadata.publication_date
        )
        d.metadata.short_name = self.metadata.short_name
        d._structure_descriptions = list(self._structure_descriptions)
        d._enum_descriptions = list(self._enum_descriptions)
        d._original_nodeids = self._original_nodeids
        # Share the already-populated node containers (node NodeIds are XML-index
        # strings that don't change with namespace remapping, so sharing is safe).
        d.objects = self.objects
        d.datatypes = self.datatypes
        d.eventtypes = self.eventtypes
        d.ifacetypes = self.ifacetypes
        d.objtypes = self.objtypes
        d.reftypes = self.reftypes
        d.vartypes = self.vartypes
        d.views = self.views
        return d

    def _extract_short_name(self, uri: str) -> str:
        """
        Extract a short name from the namespace URI.

        Examples:
        - "http://opcfoundation.org/UA/" -> "UA"
        - "http://example.com/MyModel/v1.0" -> "v1.0"
        - "urn:example:mymodel" -> "mymodel"
        """
        if uri.startswith(("http://", "https://")):
            # splitting by /
            parts = [part.strip() for part in uri.split("/") if part.strip()]
        elif uri.startswith("urn:"):
            # splitting by : for URNs
            parts = [part.strip() for part in uri.split(":") if part.strip()]
        else:
            # For other schemes (test://, custom://), split by / after removing scheme
            scheme_end = uri.find("://") + 3 if "://" in uri else 0
            path_part = uri[scheme_end:]
            parts = [part.strip() for part in path_part.split("/") if part.strip()]

        # Try to return the last part, working backwards
        while parts:
            last_part = parts.pop()
            if last_part and last_part not in ["http", "https", "urn"]:
                return last_part

        return "unknown"

    def _add_required_namespace(self, uri: str, version: str = "") -> None:
        """Add a required namespace dependency."""
        dependency = {"uri": uri, "version": version}
        if dependency not in self._required_namespaces:
            self._required_namespaces.append(dependency)

    def _add_structure_description(
        self,
        nodeid: str,
        browse_name: str,
        struct_data: Dict[str, Any] | o6.StructureDefinition,
        default_encoding_id: str | None = None,
    ) -> None:
        import o6 as _o6

        sd = _o6.StructureDescription()
        sd.data_type_id = nodeid
        sd.name = o6.QualifiedName(browse_name)

        if isinstance(struct_data, dict):
            defn = _o6.StructureDefinition()
            if "structure_type" in struct_data:
                defn.structure_type = _o6.StructureType(struct_data["structure_type"])
            if "fields" in struct_data and isinstance(struct_data["fields"], list):
                fields = []
                for fd in struct_data["fields"]:
                    if isinstance(fd, dict):
                        f = _o6.StructureField()
                        if "name" in fd:
                            f.name = fd["name"]
                        if "description" in fd:
                            f.description = fd["description"]
                        if "is_optional" in fd:
                            f.is_optional = fd["is_optional"]
                        if "value_rank" in fd:
                            f.value_rank = fd["value_rank"]
                        if "data_type" in fd:
                            f.data_type = fd["data_type"]
                        if "array_dimensions" in fd:
                            f.array_dimensions = fd["array_dimensions"]
                        if "max_string_length" in fd:
                            f.max_string_length = fd["max_string_length"]
                        fields.append(f)
                    else:
                        fields.append(fd)
                defn.fields = fields
            if default_encoding_id is not None:
                defn.default_encoding_id = o6.NodeId(default_encoding_id)
            sd.structure_definition = defn
        else:
            sd.structure_definition = struct_data

        self._structure_descriptions.append(sd)

    def _add_enum_description(
        self,
        nodeid: str,
        browse_name: str,
        enum_data: Dict[str, Any] | o6.EnumDefinition,
    ) -> None:
        import o6 as _o6

        ed = _o6.EnumDescription()
        ed.data_type_id = o6.NodeId(nodeid)
        ed.name = o6.QualifiedName(browse_name)

        if isinstance(enum_data, dict):
            defn = _o6.EnumDefinition()
            if "fields" in enum_data and isinstance(enum_data["fields"], list):
                fields = []
                for fd in enum_data["fields"]:
                    if isinstance(fd, dict):
                        f = _o6.EnumField()
                        if "name" in fd:
                            f.name = fd["name"]
                        if "value" in fd:
                            f.value = fd["value"]
                        if "description" in fd:
                            f.description = fd["description"]
                        if "display_name" in fd:
                            f.display_name = fd["display_name"]
                        fields.append(f)
                    else:
                        fields.append(fd)
                defn.fields = fields
            ed.enum_definition = defn
        else:
            ed.enum_definition = enum_data

        self._enum_descriptions.append(ed)

    def _validate(self) -> List[str]:
        issues = []

        if not self.metadata.uri:
            issues.append("Namespace URI is required")

        # Allow more flexible URI formats for testing and custom protocols
        valid_schemes = (
            "http://",
            "https://",
            "urn:",
            "test://",
            "example://",
            "custom://",
        )
        if not self.metadata.uri.startswith(valid_schemes):
            issues.append(f"Invalid URI format: {self.metadata.uri}")

        # Validate required namespace references
        for i, req_ns in enumerate(self._required_namespaces):
            if not req_ns.get("uri"):
                issues.append(f"Required namespace {i} missing URI")

        return issues

    def __str__(self) -> str:
        return "Namespace" + str(self.metadata)[17:]

    def __repr__(self) -> str:
        return "o6." + str(self)
