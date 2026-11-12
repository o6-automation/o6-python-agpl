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

"""Crawls a server's address space into an `_InformationModel`.

Uses only Browse, BrowseNext and Read, so any OPC UA server works.
"""

from __future__ import annotations

import logging
import re
from collections import deque
from xml.sax.saxutils import unescape
from typing import TYPE_CHECKING, Any, Awaitable, Literal, cast

import o6
from o6._browse import _browse_description
from o6._datatype_loading import (
    _ALL_RESULTS,
    _DataTypeLoader,
    _Services,
    _bad,
    _emptyModel,
    _isNull,
    _ns0NodeId,
    _read_id,
)
from o6._information_model import (
    _HAS_CHILD,
    _HAS_ENCODING,
    _HAS_SUBTYPE,
    _HAS_TYPE_DEFINITION,
    _HIERARCHICAL_REFERENCES,
    _INSTANCE_CLASSES,
    NS0_URI,
    NamespaceInfo,
    NodeRecord,
    NodeRef,
    QualifiedNameRef,
    Reference,
    TypeInfo,
    _InformationModel,
    _ns0,
)
from o6._node_backend import _attribute_id
from o6.ns import ns0
from o6.ns._generated_nodesets import _GLOBAL_NAMESPACES

if TYPE_CHECKING:
    from o6.client import Client

_logger = logging.getLogger("o6.informationmodel")

_NodeClass = ns0.datatypes.NodeClass
_Direction = ns0.datatypes.BrowseDirection

_REFERENCES = _ns0(31)
_HAS_PROPERTY = _ns0(46)
_ROOT_FOLDER = _ns0(84)
_SERVER = _ns0(2253)
_SERVER_NAMESPACES = _ns0(11715)
# The folders of the DataType dictionaries.
_XML_SCHEMA = _ns0(92)
_OPC_BINARY = _ns0(93)

# The model of a dictionary, such as `<ua:Model ModelUri="..." PublicationDate="..."/>`.
_DICTIONARY_MODEL = re.compile(r"<\w+:Model\b[^>]*>")
_XML_ATTRIBUTE = re.compile(r'(\w+)="([^"]*)"')

# Below the Server object the standard's runtime branches are never exported.
_SERVER_RUNTIME_CHILDREN = {
    _ns0(2256),  # ServerStatus
    _ns0(2274),  # ServerDiagnostics, with sessions and subscriptions
    _ns0(2296),  # ServerRedundancy
    _ns0(12637),  # ServerConfiguration
    _ns0(14443),  # PublishSubscribe
    _ns0(19372),  # ServerLog
    _ns0(24226),  # Resources
}

# The companion specifications o6 bundles. The crawler adds the namespaces with
# NamespaceMetadata on the server; the rest are the server's own.
_COMPANION_URIS = frozenset(uri for _shortname, uri, _version in _GLOBAL_NAMESPACES) - {NS0_URI}

_DEFAULT_XML = QualifiedNameRef(NS0_URI, "Default XML")
_DEFAULT_BINARY = QualifiedNameRef(NS0_URI, "Default Binary")
_DATA_TYPE_ENCODING_TYPE = _ns0(76)
_OPTION_SET_VALUES = QualifiedNameRef(NS0_URI, "OptionSetValues")
_UINTEGER = _ns0(28)

_COMMON_ATTRIBUTES = ("BrowseName", "DisplayName", "Description", "WriteMask")
_CLASS_ATTRIBUTES: dict[int, tuple[str, ...]] = {
    int(_NodeClass.OBJECT): ("EventNotifier",),
    int(_NodeClass.VARIABLE): (
        "Value",
        "DataType",
        "ValueRank",
        "ArrayDimensions",
        "AccessLevel",
        "MinimumSamplingInterval",
        "Historizing",
    ),
    int(_NodeClass.METHOD): ("Executable",),
    int(_NodeClass.OBJECT_TYPE): ("IsAbstract",),
    int(_NodeClass.VARIABLE_TYPE): (
        "Value",
        "DataType",
        "ValueRank",
        "ArrayDimensions",
        "IsAbstract",
    ),
    int(_NodeClass.REFERENCE_TYPE): ("IsAbstract", "Symmetric", "InverseName"),
    int(_NodeClass.DATA_TYPE): ("IsAbstract", "DataTypeDefinition"),
    int(_NodeClass.VIEW): ("ContainsNoLoops", "EventNotifier"),
}
_ACCESS_ATTRIBUTES = ("RolePermissions", "AccessRestrictions")
_CLASS_ACCESS_ATTRIBUTES: dict[int, tuple[str, ...]] = {
    int(_NodeClass.VARIABLE): ("AccessLevelEx",),
}
_ATTRIBUTE_IDS = {
    name: _attribute_id(name)
    for names in (
        _COMMON_ATTRIBUTES,
        _ACCESS_ATTRIBUTES,
        *_CLASS_ATTRIBUTES.values(),
        *_CLASS_ACCESS_ATTRIBUTES.values(),
    )
    for name in names
}


# Read results for an attribute the node does not have, or a Value it never got.
_ABSENT_ATTRIBUTE_STATUSES = (
    o6.StatusCode.BAD_ATTRIBUTE_ID_INVALID,
    o6.StatusCode.BAD_WAITING_FOR_INITIAL_DATA,
)


def _modelDates(dictionary: str) -> dict[str, str]:
    """ModelUri -> PublicationDate of the `Model` elements in a DataType dictionary."""
    dates = {}
    for element in _DICTIONARY_MODEL.finditer(dictionary):
        attributes = dict(_XML_ATTRIBUTE.findall(element.group(0)))
        uri, date = attributes.get("ModelUri"), attributes.get("PublicationDate", "")
        if uri and date and not date.startswith("0001-"):
            dates[unescape(uri)] = date
    return dates


class _Crawler(_Services):
    def __init__(
        self,
        client: Client,
        *,
        includeInstances: bool,
        includeCompleteServer: bool,
        includeValues: bool | Literal["types"],
        includeAccessAttributes: bool,
    ) -> None:
        super().__init__(client)
        self.includeInstances = includeInstances
        self.includeCompleteServer = includeCompleteServer
        self.includeValues = includeValues
        self.includeAccessAttributes = includeAccessAttributes
        self.companionUris = set(_COMPANION_URIS)
        self.belowServer = {_SERVER}  # the ns0 part of the Server subtree
        self.ns0Declarations: set[NodeRef] = set()  # instance declarations of ns0 types
        self.clientIds: dict[NodeRef, o6.NodeId] = {}
        self.nodeClasses: dict[NodeRef, ns0.datatypes.NodeClass] = {}
        self.references: dict[NodeRef, dict[Reference, None]] = {}

    async def run(self) -> _InformationModel:
        if not self.client.connected:
            raise RuntimeError("Client is not connected")
        self.model = await self._newModel()
        await self._readOperationLimits()
        await self._traverse()
        records = await self._readAttributes()
        self._addMissingInverses(records)
        self.model.nodes = records
        self.model.types = await self._resolveTypes(records)
        self._dropSkippedInstances()
        if not self.includeInstances:
            self._keepTypesOnly()
        self._dropReferencesToSkippedInstances()
        if self.includeValues:
            self._loadDataTypes()
            self._addXmlEncodings()
        await self._readValues()
        await self._deriveOptionSetDefinitions()
        await self._resolveXmlEncodings()
        return self.model

    # Namespaces

    async def _newModel(self) -> _InformationModel:
        """An empty model with the server's namespaces and the client's index mapping."""
        await cast(Awaitable[None], self.client.updateRemoteNamespaces())
        model = _emptyModel(self.client)
        await self._namespaceMetadata(model.namespaces)
        await self._dictionaryPublicationDates(model.namespaces)
        for info in model.namespaces.values():
            info.isCompanion = info.uri in self.companionUris
        return model

    async def _namespaceMetadata(self, infos: dict[str, NamespaceInfo]) -> None:
        """Fill version and publication date from Server/Namespaces; those are companion specs."""
        [(status, objects)] = await self._browse(
            [
                _browse_description(
                    _ns0NodeId(_SERVER_NAMESPACES),
                    _Direction.FORWARD,
                    _ns0NodeId(_HIERARCHICAL_REFERENCES),
                    True,
                    int(_NodeClass.OBJECT),
                    _ALL_RESULTS,
                )
            ]
        )
        if _bad(status):
            return
        objects = [o for o in objects if not o.nodeId.svr]
        properties = await self._browse(
            [
                _browse_description(
                    o6.NodeId(o.nodeId),
                    _Direction.FORWARD,
                    _ns0NodeId(_HAS_PROPERTY),
                    True,
                    int(_NodeClass.VARIABLE),
                    _ALL_RESULTS,
                )
                for o in objects
            ]
        )
        wanted = {"NamespaceUri", "NamespaceVersion", "NamespacePublicationDate"}
        items, slots = [], []
        for owner, (_status, found) in enumerate(properties):
            for prop in found:
                if prop.browseName.name in wanted and not prop.nodeId.svr:
                    items.append(_read_id(o6.NodeId(prop.nodeId), o6.AttributeId.VALUE))
                    slots.append((owner, prop.browseName.name))
        metadata: dict[int, dict[str, Any]] = {}
        for (owner, name), result in zip(slots, await self._read(items)):
            if not _bad(result.status):
                metadata.setdefault(owner, {})[name] = result.value
        for values in metadata.values():
            info = infos.get(str(values.get("NamespaceUri")))
            if info is None:
                continue
            self.companionUris.add(info.uri)
            if values.get("NamespaceVersion") is not None:
                info.version = str(values["NamespaceVersion"])
            date = values.get("NamespacePublicationDate")
            if date is not None and int(date) > 0:  # 0001-01-01 arrives below zero
                info.publicationDate = str(date)

    async def _dictionaryPublicationDates(self, infos: dict[str, NamespaceInfo]) -> None:
        """Fill missing publication dates from the `Model` element of the DataType dictionaries."""
        if all(info.publicationDate for info in infos.values()):
            return
        folders = await self._browse(
            [
                _browse_description(
                    _ns0NodeId(folder),
                    _Direction.FORWARD,
                    _ns0NodeId(_HIERARCHICAL_REFERENCES),
                    True,
                    int(_NodeClass.VARIABLE),
                    _ALL_RESULTS,
                )
                for folder in (_OPC_BINARY, _XML_SCHEMA)
            ]
        )
        items = [
            _read_id(o6.NodeId(d.nodeId), o6.AttributeId.VALUE)
            for status, dictionaries in folders
            if not _bad(status)
            for d in dictionaries
            if not d.nodeId.svr
        ]
        for result in await self._read(items):
            if _bad(result.status) or not isinstance(result.value, (bytes, bytearray)):
                continue
            for uri, date in _modelDates(result.value.decode("utf-8", "replace")).items():
                info = infos.get(uri)
                if info is not None and not info.publicationDate:
                    info.publicationDate = date

    # Walking the address space

    async def _traverse(self) -> None:
        """Breadth-first walk from the Root folder.

        Nodes outside ns0 are exported and browsed over all references in both
        directions; ns0 nodes only forward over hierarchical references, to
        reach the exported ones.
        """
        self.clientIds[_ROOT_FOLDER] = _ns0NodeId(_ROOT_FOLDER)
        self.nodeClasses[_ROOT_FOLDER] = _NodeClass.OBJECT
        queue = deque([_ROOT_FOLDER])

        while queue:
            batch = [queue.popleft() for _ in range(min(len(queue), self.batchSizes["Browse"]))]
            browsed = await self._browse([self._browseDescription(node_id) for node_id in batch])
            for node_id, (status, descriptions) in zip(batch, browsed):
                if _bad(status):
                    if not node_id.isNs0:
                        _logger.warning(f"Browse of {node_id} failed: {status.name}")
                    continue
                for description in descriptions:
                    if description.nodeId.svr:
                        continue  # on another server
                    target = self._record(node_id, description)
                    if self._shouldVisit(node_id, target, bool(description.isForward)):
                        try:
                            self.clientIds[target] = o6.NodeId(description.nodeId)
                        except Exception:
                            continue
                        queue.append(target)

    def _browseDescription(self, node_id: NodeRef) -> ns0.datatypes.BrowseDescription:
        if node_id.isNs0:
            direction, reference_type = _Direction.FORWARD, _HIERARCHICAL_REFERENCES
        else:
            direction, reference_type = _Direction.BOTH, _REFERENCES
        return _browse_description(
            self.clientIds[node_id], direction, _ns0NodeId(reference_type), True, 0, _ALL_RESULTS
        )

    def _record(self, source: NodeRef, description: ns0.datatypes.ReferenceDescription) -> NodeRef:
        """Keep the reference of an exported node, and the NodeClass of its target."""
        target = self.model.ref(description.nodeId)
        if not source.isNs0:
            reference = Reference(
                self.model.ref(description.referenceTypeId), target, bool(description.isForward)
            )
            self.references.setdefault(source, {})[reference] = None
        self.nodeClasses.setdefault(target, _NodeClass(int(description.nodeClass)))
        return target

    def _shouldVisit(self, source: NodeRef, target: NodeRef, isForward: bool) -> bool:
        """Whether the walk continues from `source` to `target`."""
        if target in self.clientIds:
            return False  # already visited
        if self._inNs0Type(source) and int(self.nodeClasses[target]) in _INSTANCE_CLASSES:
            if not target.isNs0:
                return False  # added to an ns0 type by the server, like open62541's
            if isForward:
                self.ns0Declarations.add(target)
        if target.isNs0:
            # ns0 is not exported, only walked downwards to reach exported nodes.
            if not isForward:
                return False
        elif not self.includeInstances and int(self.nodeClasses[target]) in _INSTANCE_CLASSES:
            # Without instances, only instance declarations: forward from an exported node.
            if source.isNs0 or not isForward:
                return False
        if source in self.belowServer:
            return not self._skipBelowServer(target)
        return True

    def _inNs0Type(self, node_id: NodeRef) -> bool:
        """Whether `node_id` is an ns0 type or an instance declaration of one."""
        node_class = self.nodeClasses.get(node_id)
        if not node_id.isNs0 or node_class is None:
            return False
        return int(node_class) not in _INSTANCE_CLASSES or node_id in self.ns0Declarations

    def _skipBelowServer(self, target: NodeRef) -> bool:
        """Whether to skip a child of the Server subtree.

        Runtime branches are always skipped. The server's own nodes are kept;
        companion-specification nodes only with `includeCompleteServer`. ns0
        nodes are added to `belowServer`, so the rules apply further down.
        """
        if target in _SERVER_RUNTIME_CHILDREN:
            return True
        if target.isNs0:
            self.belowServer.add(target)
            return False
        return target.namespaceUri in self.companionUris and not self.includeCompleteServer

    # Attributes and types

    async def _readNamed(
        self, wanted: dict[NodeRef, tuple[str, ...]]
    ) -> dict[NodeRef, dict[str, Any]]:
        """Read the named attributes of each node; unreadable ones are left out."""
        items, slots = [], []
        for node_id, names in wanted.items():
            for name in names:
                items.append(_read_id(self.clientIds[node_id], _ATTRIBUTE_IDS[name]))
                slots.append((node_id, name))
        values: dict[NodeRef, dict[str, Any]] = {node_id: {} for node_id in wanted}
        for (node_id, name), result in zip(slots, await self._read(items)):
            if not _bad(result.status):
                values[node_id][name] = result.value
            elif result.status not in _ABSENT_ATTRIBUTE_STATUSES:
                _logger.warning(f"{name} of {node_id} is not readable: {result.status!r}")
        return values

    async def _readAttributes(self) -> dict[NodeRef, NodeRecord]:
        """Read every attribute but the Value, which `_readValues` reads for the kept nodes."""
        wanted: dict[NodeRef, tuple[str, ...]] = {}
        for node_id in self.clientIds:
            if node_id.isNs0:
                continue
            node_class = int(self.nodeClasses[node_id])
            names = _COMMON_ATTRIBUTES + _CLASS_ATTRIBUTES.get(node_class, ())
            if self.includeAccessAttributes:
                names += _ACCESS_ATTRIBUTES + _CLASS_ACCESS_ATTRIBUTES.get(node_class, ())
            wanted[node_id] = tuple(name for name in names if name != "Value")
        values = await self._readNamed(wanted)

        records: dict[NodeRef, NodeRecord] = {}
        for node_id, attributes in values.items():
            browse_name = attributes.pop("BrowseName", None)
            if browse_name is None:
                _logger.warning(f"{node_id} has no readable BrowseName and is left out")
                continue
            data_type = attributes.pop("DataType", None)
            if not _isNull(data_type):  # some servers report BaseDataType as the null NodeId
                attributes["DataType"] = self.model.ref(data_type)
            if attributes.get("RolePermissions") is not None:
                attributes["RolePermissions"] = [
                    (self.model.ref(permission.roleId), int(permission.permissions))
                    for permission in attributes["RolePermissions"]
                ]
            records[node_id] = NodeRecord(
                nodeId=node_id,
                nodeClass=self.nodeClasses[node_id],
                browseName=self.model.qualifiedName(browse_name),
                displayName=attributes.pop("DisplayName", None),
                description=attributes.pop("Description", None),
                attributes=attributes,
                references=list(self.references.get(node_id, {})),
            )
        return records

    @staticmethod
    def _addMissingInverses(records: dict[NodeRef, NodeRecord]) -> None:
        """Mirror references onto exported targets, for servers that return forward ones only."""
        for record in records.values():
            for reference in record.references:
                other = records.get(reference.target)
                mirror = Reference(reference.referenceType, record.nodeId, not reference.isForward)
                if other is not None and mirror not in other.references:
                    other.references.append(mirror)

    def _fieldTypes(self, definition: Any) -> set[NodeRef]:
        return {
            self.model.ref(item.dataType)
            for item in getattr(definition, "fields", None) or ()
            if not _isNull(getattr(item, "dataType", None))
        }

    async def _resolveTypes(self, records: dict[NodeRef, NodeRecord]) -> dict[NodeRef, TypeInfo]:
        """Collect the DataTypes and ReferenceTypes in use, up to their roots."""
        type_classes = {int(_NodeClass.DATA_TYPE), int(_NodeClass.REFERENCE_TYPE)}
        types = {
            record.nodeId: TypeInfo(
                record.nodeId,
                record.browseName,
                record.supertype,
                record.attributes.get("DataTypeDefinition"),
            )
            for record in records.values()
            if int(record.nodeClass) in type_classes
        }
        wanted = {info.supertype for info in types.values() if info.supertype is not None}
        for record in records.values():
            wanted.update(reference.referenceType for reference in record.references)
            if isinstance(record.attributes.get("DataType"), NodeRef):
                wanted.add(record.attributes["DataType"])
            wanted |= self._fieldTypes(record.attributes.get("DataTypeDefinition"))

        while missing := [type_id for type_id in wanted if type_id not in types]:
            client_ids = [
                self.clientIds.get(type_id) or self._clientNodeId(type_id) for type_id in missing
            ]
            attributes = (o6.AttributeId.BROWSE_NAME, o6.AttributeId.DATA_TYPE_DEFINITION)
            reads = await self._read([_read_id(n, a) for n in client_ids for a in attributes])
            parents = await self._browse(
                [
                    _browse_description(
                        n, _Direction.INVERSE, _ns0NodeId(_HAS_SUBTYPE), False, 0, _ALL_RESULTS
                    )
                    for n in client_ids
                ]
            )
            for index, type_id in enumerate(missing):
                browse_name, definition = reads[2 * index : 2 * index + 2]
                if _bad(browse_name.status) or browse_name.value is None:
                    _logger.warning(f"Type {type_id} used by the model is not readable")
                    name = QualifiedNameRef(type_id.namespaceUri, str(type_id.identifier))
                    types[type_id] = TypeInfo(type_id, name)
                    continue
                status, supers = parents[index]
                supertype = None
                if not _bad(status) and supers and not supers[0].nodeId.svr:
                    supertype = self.model.ref(supers[0].nodeId)
                    self.clientIds.setdefault(supertype, o6.NodeId(supers[0].nodeId))
                    wanted.add(supertype)
                types[type_id] = TypeInfo(
                    type_id,
                    self.model.qualifiedName(browse_name.value),
                    supertype,
                    None if _bad(definition.status) else definition.value,
                )
                wanted |= self._fieldTypes(types[type_id].definition)
        return types

    def _clientNodeId(self, node_id: NodeRef) -> o6.NodeId:
        index = self.model.globalIndex(node_id.namespaceUri)
        return o6.NodeId(f"ns={index};{node_id.identifierText}")

    # Instances

    def _typeNodes(self) -> set[NodeRef]:
        """The types, their instance declarations and DataType encodings."""
        model = self.model
        keep = {
            node_id
            for node_id, node in model.nodes.items()
            if int(node.nodeClass) not in _INSTANCE_CLASSES
        }
        pending = list(keep)
        while pending:
            for reference in model.nodes[pending.pop()].references:
                target = reference.target
                if not reference.isForward or target not in model.nodes or target in keep:
                    continue
                if (
                    model.isSubtypeOf(reference.referenceType, _HAS_CHILD)
                    or reference.referenceType == _HAS_ENCODING
                ):
                    keep.add(target)
                    pending.append(target)
        return keep

    def _keepTypesOnly(self) -> None:
        """Drop instances: keep types, their instance declarations and DataType encodings."""
        keep = self._typeNodes()
        self.model.nodes = {
            node_id: node for node_id, node in self.model.nodes.items() if node_id in keep
        }

    # DataTypes

    def _loadDataTypes(self) -> None:
        """Register the model's structures the client cannot decode, so the Values read next decode."""
        _DataTypeLoader(
            self.client,
            self.model,
            self.clientIds,
            lambda type_id: self._encodings(type_id).get(_DEFAULT_BINARY),
        ).load()

    def _encodings(self, type_id: NodeRef) -> dict[QualifiedNameRef, NodeRef]:
        """The crawled DataTypeEncodings of a DataType, by BrowseName."""
        record = self.model.nodes.get(type_id)
        if record is None:
            return {}
        return {
            self.model.nodes[r.target].browseName: r.target
            for r in record.references
            if r.isForward and r.referenceType == _HAS_ENCODING and r.target in self.model.nodes
        }

    def _addXmlEncodings(self) -> None:
        """Give each exported structure without a Default XML encoding one, for the TypeIds of Values.

        Importers only need the TypeId to name the XML encoding of the type,
        through a `Default XML` node of the file.
        """
        nodes = self.model.nodes
        for type_id, record in list(nodes.items()):
            if not isinstance(
                record.attributes.get("DataTypeDefinition"), ns0.datatypes.StructureDefinition
            ):
                continue
            encoding = self._encodings(type_id).get(_DEFAULT_XML)
            if encoding is None:
                encoding = NodeRef(type_id.namespaceUri, f"{record.browseName.name}.DefaultXml")
                if encoding in nodes:
                    encoding = NodeRef(type_id.namespaceUri, f"{type_id.identifierText}.DefaultXml")
                nodes[encoding] = NodeRecord(
                    nodeId=encoding,
                    nodeClass=_NodeClass.OBJECT,
                    browseName=_DEFAULT_XML,
                    displayName=o6.LocalizedText(_DEFAULT_XML.name),
                    references=[
                        Reference(_HAS_TYPE_DEFINITION, _DATA_TYPE_ENCODING_TYPE),
                        Reference(_HAS_ENCODING, type_id, False),
                    ],
                )
                record.references.append(Reference(_HAS_ENCODING, encoding))
            self.model.xmlEncodings[type_id] = encoding

    async def _readValues(self) -> None:
        """Read the Value of the exported Variables and VariableTypes `includeValues` asks for."""
        if not self.includeValues:
            return
        nodes = self.model.nodes
        wanted = [
            node_id
            for node_id, node in nodes.items()
            if int(node.nodeClass) in (int(_NodeClass.VARIABLE), int(_NodeClass.VARIABLE_TYPE))
        ]
        if self.includeValues == "types":
            types = self._typeNodes()
            wanted = [node_id for node_id in wanted if node_id in types]
        values = await self._readNamed({node_id: ("Value",) for node_id in wanted})
        for node_id, attributes in values.items():
            nodes[node_id].attributes.update(attributes)

    async def _deriveOptionSetDefinitions(self) -> None:
        """Build the missing definition of an OptionSet DataType from its OptionSetValues.

        Some servers return no DataTypeDefinition for an OptionSet. The property
        names one bit per entry; an empty entry is an unused bit.
        """
        nodes = self.model.nodes
        properties: dict[NodeRef, NodeRef] = {}
        for node_id, node in nodes.items():
            if (
                int(node.nodeClass) != int(_NodeClass.DATA_TYPE)
                or node.attributes.get("DataTypeDefinition") is not None
                or not self.model.isSubtypeOf(node_id, _UINTEGER)
            ):
                continue
            option_set_values = next(
                (
                    r.target
                    for r in node.references
                    if r.isForward
                    and r.referenceType == _HAS_PROPERTY
                    and r.target in nodes
                    and nodes[r.target].browseName == _OPTION_SET_VALUES
                ),
                None,
            )
            if option_set_values is not None:
                properties[node_id] = option_set_values
        # Read the names when the Values are left out of the export.
        read = await self._readNamed(
            {
                prop: ("Value",)
                for prop in properties.values()
                if "Value" not in nodes[prop].attributes
            }
        )
        for data_type, prop in properties.items():
            names = nodes[prop].attributes.get("Value", read.get(prop, {}).get("Value"))
            fields = []
            for bit, name in enumerate(() if names is None else names):  # may be an ndarray
                if name is None or not name.text:
                    continue
                field = ns0.datatypes.EnumField()
                field.name = name.text
                field.value = bit
                field.displayName = name
                fields.append(field)
            if fields:
                definition = ns0.datatypes.EnumDefinition()
                definition.fields = fields
                nodes[data_type].attributes["DataTypeDefinition"] = definition

    async def _resolveXmlEncodings(self) -> None:
        """Find the Default XML encoding of each structure in a Value, for its TypeId.

        The exported DataTypes have theirs from `_addXmlEncodings`; only the
        others, such as those of ns0, are browsed.
        """
        from o6._nodeset_xml import _encodeValue, _typeIds

        used: set[NodeRef] = set()
        for node in self.model.nodes.values():
            value = node.attributes.get("Value")
            if value is None:
                continue
            try:
                used |= _typeIds(_encodeValue(self.model, value))
            except (o6.StatusCodeError, TypeError, KeyError):
                pass  # the writer warns when it leaves the Value out
        # Another TypeId of an exported namespace is the binary encoding of a
        # structure `_loadDataTypes` could not load and has warned about.
        used = {
            type_id
            for type_id in used
            if type_id not in self.model.xmlEncodings and type_id not in self.model.nodes
        }
        if not used:
            return
        type_ids = sorted(used, key=lambda type_id: (type_id.namespaceUri, type_id.sortKey()))
        found = await self._browse(
            [
                _browse_description(
                    self.clientIds.get(type_id) or self._clientNodeId(type_id),
                    _Direction.FORWARD,
                    _ns0NodeId(_HAS_ENCODING),
                    False,
                    int(_NodeClass.OBJECT),
                    _ALL_RESULTS,
                )
                for type_id in type_ids
            ]
        )
        missing = []
        for type_id, (status, encodings) in zip(type_ids, found):
            encoding = next(
                (
                    e
                    for e in encodings
                    if not e.nodeId.svr and self.model.qualifiedName(e.browseName) == _DEFAULT_XML
                ),
                None,
            )
            if _bad(status) or encoding is None:
                missing.append(type_id)
            else:
                self.model.xmlEncodings[type_id] = self.model.ref(encoding.nodeId)
        if missing:
            _logger.warning(
                f"{len(missing)} TypeIds in Values have no Default XML encoding and are "
                f"written as they are, e.g. {missing[0]}"
            )

    def _isHierarchical(self, reference: Reference) -> bool:
        return self.model.isSubtypeOf(reference.referenceType, _HIERARCHICAL_REFERENCES)

    def _allowedParent(self, parent: NodeRef, child: NodeRef) -> bool:
        """Whether the walk would export `child` below this ns0 parent."""
        if self._inNs0Type(parent) or parent not in self.clientIds:
            return False
        return parent not in self.belowServer or not self._skipBelowServer(child)

    def _dropSkippedInstances(self) -> None:
        """Drop instances in an ns0 type or a skipped part of the Server subtree.

        The walk can also reach them over other references, such as the inverse
        HasTypeDefinition from their type. An instance stays when one chain of
        hierarchical parents leads to an exported type or an allowed ns0 parent.
        """
        nodes = self.model.nodes
        instances = {
            node_id for node_id, node in nodes.items() if int(node.nodeClass) in _INSTANCE_CLASSES
        }

        def spread(start: set[NodeRef], among: set[NodeRef]) -> set[NodeRef]:
            """`start` and the instances in `among` below it."""
            found, pending = set(start), list(start)
            while pending:
                for reference in nodes[pending.pop()].references:
                    target = reference.target
                    if (
                        reference.isForward
                        and target in among
                        and target not in found
                        and self._isHierarchical(reference)
                    ):
                        found.add(target)
                        pending.append(target)
            return found

        # Per instance, whether each of its ns0 parents is allowed.
        allowed = {
            node_id: [
                self._allowedParent(r.target, node_id)
                for r in nodes[node_id].references
                if not r.isForward and r.target.isNs0 and self._isHierarchical(r)
            ]
            for node_id in instances
        }
        placed = spread(
            (set(nodes) - instances) | {node_id for node_id in instances if any(allowed[node_id])},
            instances,
        )
        unplaced = instances - placed
        # Unplaced with ns0 parents means none of them is allowed.
        skipped = spread({node_id for node_id in unplaced if allowed[node_id]}, unplaced)
        self.model.nodes = {
            node_id: node for node_id, node in nodes.items() if node_id not in skipped
        }

    def _dropReferencesToSkippedInstances(self) -> None:
        """Remove references to instances that are not exported, so no file needs them.

        A reference into a companion specification without exported nodes,
        such as HasDictionaryEntry into a dictionary below the Server object,
        stays: its published NodeSet becomes a required model. The others are
        reported, unless instances are left out on request.
        """
        nodes = self.model.nodes
        exported = {node_id.namespaceUri for node_id in nodes}

        def skipped(target: NodeRef) -> bool:
            is_instance = int(self.nodeClasses.get(target, 0)) in _INSTANCE_CLASSES
            if not is_instance or target.isNs0 or target in nodes:
                return False
            return target.namespaceUri in exported or target.namespaceUri not in self.companionUris

        dropped: list[tuple[NodeRef, Reference]] = []
        for node in nodes.values():
            kept = []
            for reference in node.references:
                if skipped(reference.target):
                    dropped.append((node.nodeId, reference))
                else:
                    kept.append(reference)
            node.references = kept
        if dropped and self.includeInstances:
            source, reference = dropped[0]
            _logger.warning(
                f"{len(dropped)} references to nodes that are not exported are left out, "
                f"e.g. from {source} to {reference.target}"
            )
