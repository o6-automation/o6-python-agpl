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

"""Snapshot of a remote server's information model, as built by the crawler.

NodeIds are keyed by namespace URI: the client remaps indices into `o6.ns`,
and every NodeSet2 file numbers its namespaces differently.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from functools import cached_property
from pathlib import Path
from typing import Any, Iterator
from uuid import UUID

import o6
from o6.ns import _GLOBAL_SCOPE, ns0

NS0_URI = "http://opcfoundation.org/UA/"

_NodeClass = ns0.datatypes.NodeClass

_INSTANCE_CLASSES = {
    int(_NodeClass.OBJECT),
    int(_NodeClass.VARIABLE),
    int(_NodeClass.METHOD),
    int(_NodeClass.VIEW),
}

_IDENTIFIER_KINDS: tuple[tuple[type, str], ...] = (
    (int, "i"),
    (UUID, "g"),
    (bytes, "b"),
    (str, "s"),
)


@dataclass(frozen=True)
class NodeRef:
    """A NodeId keyed by namespace URI."""

    namespaceUri: str
    identifier: int | str | bytes | UUID

    @property
    def isNs0(self) -> bool:
        return self.namespaceUri == NS0_URI

    @property
    def identifierText(self) -> str:
        """The identifier in NodeId syntax, e.g. `i=5` or `s=Pump`."""
        kind = next(
            kind for py_type, kind in _IDENTIFIER_KINDS if isinstance(self.identifier, py_type)
        )
        return str(o6.NodeId(ns=0, **{kind: self.identifier}))  # type: ignore[arg-type]

    def sortKey(self) -> tuple[int, Any]:
        for rank, (py_type, _kind) in enumerate(_IDENTIFIER_KINDS):
            if isinstance(self.identifier, py_type):
                return (rank, str(self.identifier) if py_type is UUID else self.identifier)
        return (len(_IDENTIFIER_KINDS), self.identifier)

    def __str__(self) -> str:
        return f"nsu={self.namespaceUri};{self.identifierText}"


def _ns0(identifier: int) -> NodeRef:
    return NodeRef(NS0_URI, identifier)


_BASE_DATA_TYPE = _ns0(24)
_ENUMERATION = _ns0(29)
_HIERARCHICAL_REFERENCES = _ns0(33)
_HAS_CHILD = _ns0(34)
_HAS_ENCODING = _ns0(38)
_HAS_TYPE_DEFINITION = _ns0(40)
_HAS_SUBTYPE = _ns0(45)


@dataclass(frozen=True)
class QualifiedNameRef:
    """A BrowseName keyed by namespace URI."""

    namespaceUri: str
    name: str


@dataclass(frozen=True)
class Reference:
    """A reference as seen from the node that holds it."""

    referenceType: NodeRef
    target: NodeRef
    isForward: bool = True


@dataclass
class NamespaceInfo:
    uri: str
    version: str = ""
    publicationDate: str = ""
    isCompanion: bool = False  # a companion specification, with a published NodeSet


@dataclass
class NodeRecord:
    """An exported node.

    `attributes` uses NodeSet2 names. `DataType` is a `NodeRef`; `Value` and
    `DataTypeDefinition` are kept as the client decoded them.
    """

    nodeId: NodeRef
    nodeClass: ns0.datatypes.NodeClass
    browseName: QualifiedNameRef
    displayName: o6.LocalizedText | None = None
    description: o6.LocalizedText | None = None
    attributes: dict[str, Any] = field(default_factory=dict)
    references: list[Reference] = field(default_factory=list)

    def _first(self, referenceType: NodeRef, isForward: bool) -> NodeRef | None:
        return next(
            (
                r.target
                for r in self.references
                if r.referenceType == referenceType and r.isForward == isForward
            ),
            None,
        )

    @property
    def typeDefinition(self) -> NodeRef | None:
        return self._first(_HAS_TYPE_DEFINITION, True)

    @property
    def supertype(self) -> NodeRef | None:
        return self._first(_HAS_SUBTYPE, False)


@dataclass
class TypeInfo:
    """A DataType or ReferenceType the exported nodes use, from any namespace."""

    nodeId: NodeRef
    browseName: QualifiedNameRef
    supertype: NodeRef | None = None
    definition: Any = None


class _InformationModel:
    """The crawled nodes and types of a server, written out by `save`."""

    def __init__(self, namespaces: dict[str, NamespaceInfo], indexUris: dict[int, str]) -> None:
        self.namespaces = namespaces
        self.nodes: dict[NodeRef, NodeRecord] = {}
        self.types: dict[NodeRef, TypeInfo] = {}
        self.xmlEncodings: dict[NodeRef, NodeRef] = {}  # DataType -> its Default XML encoding
        self._indexUris = indexUris
        self._uriIndexes = {uri: index for index, uri in indexUris.items()}
        self._subtypes: dict[tuple[NodeRef, NodeRef], bool] = {}

    def _uri(self, ns: Any) -> str:
        index = ns if isinstance(ns, int) else ns.index
        uri = self._indexUris.get(index) or getattr(ns, "uri", None)
        if uri is None:
            raise KeyError(f"namespace index {index} is not known to this model")
        return uri

    @cached_property
    def serverIndexes(self) -> list[int]:
        """The `o6.ns` index of each namespace, in server order."""
        return [self.globalIndex(uri) for uri in self.namespaces]

    def globalIndex(self, uri: str) -> int:
        """The process-wide `o6.ns` index of a namespace URI."""
        return self._uriIndexes[uri]

    def ref(self, nodeId: o6.NodeId | o6.ExpandedNodeId) -> NodeRef:
        """Convert a NodeId the client returned into a `NodeRef`."""
        if isinstance(nodeId, o6.ExpandedNodeId) and nodeId.nsu:
            return NodeRef(nodeId.nsu, nodeId.id)
        return NodeRef(self._uri(nodeId.ns), nodeId.id)

    def qualifiedName(self, name: o6.QualifiedName) -> QualifiedNameRef:
        return QualifiedNameRef(self._uri(name.ns), name.name)

    @cached_property
    def exportedNamespaces(self) -> list[str]:
        """The URIs that own exported nodes, in server order."""
        owned = {node_id.namespaceUri for node_id in self.nodes}
        ordered = [uri for uri in self.namespaces if uri in owned]
        return ordered + sorted(owned.difference(ordered))

    @cached_property
    def basis(self) -> dict[str, set[str]]:
        """Namespace -> the namespaces its types, DataTypes and ReferenceTypes come from, transitively."""
        direct: dict[str, set[str]] = {}
        for node in self.nodes.values():
            uri = node.nodeId.namespaceUri
            used = {node.typeDefinition, node.supertype, node.attributes.get("DataType")}
            used.update(r.referenceType for r in node.references if r.isForward)
            direct.setdefault(uri, set()).update(
                other.namespaceUri
                for other in used
                if isinstance(other, NodeRef) and other.namespaceUri != uri
            )
        basis: dict[str, set[str]] = {}
        for uri in direct:
            found: set[str] = set()
            pending = list(direct[uri])
            while pending:
                other_uri = pending.pop()
                if other_uri not in found:
                    found.add(other_uri)
                    pending.extend(direct.get(other_uri, ()))
            basis[uri] = found - {uri}
        return basis

    def _ancestors(self, typeId: NodeRef) -> Iterator[NodeRef]:
        current: NodeRef | None = typeId
        seen: set[NodeRef] = set()
        while current is not None and current not in seen:
            yield current
            seen.add(current)
            info = self.types.get(current)
            current = info.supertype if info is not None else None

    def isSubtypeOf(self, typeId: NodeRef, ancestor: NodeRef) -> bool:
        """Whether `typeId` is `ancestor` or derives from it; cached, as types are final."""
        key = (typeId, ancestor)
        if key not in self._subtypes:
            self._subtypes[key] = ancestor in self._ancestors(typeId)
        return self._subtypes[key]

    def _registeredShortname(self, uri: str) -> str | None:
        hit = next(iter(o6.ns.filter(uri=uri, scope=_GLOBAL_SCOPE)), None)
        return hit.shortname if hit is not None else None

    def shortname(self, uri: str) -> str:
        """The registered `o6.ns` shortname, or a slug of the URI's last segment."""
        from o6.client import _namespace_slug

        return self._registeredShortname(uri) or _namespace_slug(uri)

    @cached_property
    def fileNames(self) -> dict[str, str]:
        """A unique file name per namespace; registered shortnames are taken first."""
        names: dict[str, str] = {}
        unregistered_last = sorted(
            self.exportedNamespaces, key=lambda uri: self._registeredShortname(uri) is None
        )
        for uri in unregistered_last:
            base = name = self.shortname(uri)
            suffix = 2
            while name in names.values():
                name = f"{base}_{suffix}"
                suffix += 1
            names[uri] = name
        return names

    def save(self, directory: str | Path) -> list[Path]:
        """Write one `<shortname>.NodeSet2.xml` per namespace."""
        from o6._nodeset_xml import write_nodeset

        target = Path(directory)
        target.mkdir(parents=True, exist_ok=True)
        written: list[Path] = []
        for uri in self.exportedNamespaces:
            path = target / f"{self.fileNames[uri]}.NodeSet2.xml"
            path.write_text(write_nodeset(self, uri), encoding="utf-8")
            written.append(path)
        return written
