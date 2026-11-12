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

"""NodeSet2 XML writer for an `_InformationModel`, one namespace per document.

The output follows the UA-Nodeset files and what `o6-ncc` accepts. Values are
encoded by open62541 and renumbered to the file's namespace indices.
"""

from __future__ import annotations

import datetime
import logging
import re
from typing import TYPE_CHECKING, Any, TypeVar, cast
from xml.sax.saxutils import escape, quoteattr, unescape

import o6
from o6._information_model import (
    _BASE_DATA_TYPE,
    _ENUMERATION,
    _HAS_CHILD,
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
    _ns0,
)
from o6.ns import ns0

if TYPE_CHECKING:
    from o6._information_model import _InformationModel

    _types: Any
else:
    from o6._o6 import types as _types

_logger = logging.getLogger("o6.informationmodel")

UANODESET_NS = "http://opcfoundation.org/UA/2011/03/UANodeSet.xsd"
TYPES_NS = "http://opcfoundation.org/UA/2008/02/Types.xsd"

_NodeClass = ns0.datatypes.NodeClass

# NodeSet2 element per NodeClass, in document order: types first, then instances.
_ELEMENT_NAMES = {
    int(_NodeClass.REFERENCE_TYPE): "UAReferenceType",
    int(_NodeClass.DATA_TYPE): "UADataType",
    int(_NodeClass.OBJECT_TYPE): "UAObjectType",
    int(_NodeClass.VARIABLE_TYPE): "UAVariableType",
    int(_NodeClass.OBJECT): "UAObject",
    int(_NodeClass.VARIABLE): "UAVariable",
    int(_NodeClass.METHOD): "UAMethod",
    int(_NodeClass.VIEW): "UAView",
}
_CLASS_ORDER = {node_class: rank for rank, node_class in enumerate(_ELEMENT_NAMES)}

_UINTEGER = _ns0(28)
_HAS_PROPERTY = _ns0(46)
_OPTION_SET_VALUES = QualifiedNameRef(NS0_URI, "OptionSetValues")

_VARIABLE_CLASSES = {int(_NodeClass.VARIABLE), int(_NodeClass.VARIABLE_TYPE)}
_UNIONS = {
    int(ns0.datatypes.StructureType.UNION),
    int(ns0.datatypes.StructureType.UNION_WITH_SUBTYPED_VALUES),
}

_TYPE_ID = re.compile(r"<TypeId><Identifier>([^<]*)</Identifier></TypeId>")
_NSU_NODE_ID = re.compile(r"nsu=(.*?);([igbs]=.*)$")
_DATE_TIME = re.compile(r"<DateTime>((-?\d+)-[^<]*)</DateTime>")
# open62541 writes the earliest DateTime as its epoch, Part 6 5.3.1.6 requires these.
_MIN_DATE_TIME = "0001-01-01T00:00:00Z"
_MAX_DATE_TIME = "9999-12-31T23:59:59Z"
_EPOCH = "1601-01-01T00:00:00Z"


_Child = TypeVar("_Child", bound="_Element | None")


class _Element:
    """An XML element; unlike ElementTree, it can put a default `xmlns` on a value."""

    __slots__ = ("tag", "attrs", "text", "children", "raw")

    def __init__(
        self,
        tag: str,
        attrs: dict[str, str] | None = None,
        text: str | None = None,
        *,
        raw: bool = False,
    ) -> None:
        self.tag = tag
        self.attrs = attrs or {}
        self.text = text
        self.children: list[_Element] = []
        self.raw = raw

    def add(self, child: _Child) -> _Child:
        if child is not None:
            self.children.append(child)
        return child

    def write(self, out: list[str], depth: int) -> None:
        pad = "  " * depth
        attrs = "".join(f" {name}={quoteattr(value)}" for name, value in self.attrs.items())
        if self.children:
            out.append(f"{pad}<{self.tag}{attrs}>")
            for child in self.children:
                child.write(out, depth + 1)
            out.append(f"{pad}</{self.tag}>")
        elif not self.text:
            out.append(f"{pad}<{self.tag}{attrs} />")
        else:
            text = self.text if self.raw else escape(self.text)
            out.append(f"{pad}<{self.tag}{attrs}>{text}</{self.tag}>")


def _isEmpty(value: Any) -> bool:
    """No value, or an empty array, which has no element type to encode."""
    if value is None:
        return True
    return not isinstance(value, (str, bytes)) and hasattr(value, "__len__") and len(value) == 0


def _referenceOrder(reference: Reference) -> tuple[Any, ...]:
    return (
        not reference.isForward,
        reference.referenceType.namespaceUri,
        reference.referenceType.sortKey(),
        reference.target.namespaceUri,
        reference.target.sortKey(),
    )


def _localized(tag: str, text: o6.LocalizedText | None) -> _Element | None:
    if text is None or not text.text:
        return None
    return _Element(tag, {"Locale": text.locale} if text.locale else {}, text.text)


def _encodeValue(model: _InformationModel, value: Any) -> str:
    """A Value as open62541 encodes it, numbering namespaces by the server table."""
    return cast(str, _types._encodeXmlValue(value, model.serverIndexes).decode())


def _parseNodeIdText(text: str) -> NodeRef | None:
    """A NodeId as the value encoder writes it: `i=5` in ns0, `nsu=<uri>;i=5` otherwise."""
    text = unescape(text)
    match = _NSU_NODE_ID.match(text)
    uri, identifier = (match.group(1), match.group(2)) if match else (NS0_URI, text)
    try:
        return NodeRef(uri, o6.NodeId(identifier).id)
    except (TypeError, ValueError):
        return None


def _typeIds(xml: str) -> set[NodeRef]:
    """The ExtensionObject TypeIds in an encoded Value."""
    found = {_parseNodeIdText(match.group(1)) for match in _TYPE_ID.finditer(xml)}
    return {type_id for type_id in found if type_id is not None}


def _clampDateTime(match: re.Match[str]) -> str:
    """The earliest and latest DateTime as Part 6 writes them in XML."""
    text, year = match.group(1), int(match.group(2))
    if year < 1601 or text == _EPOCH:
        return f"<DateTime>{_MIN_DATE_TIME}</DateTime>"
    if year > 9999:
        return f"<DateTime>{_MAX_DATE_TIME}</DateTime>"
    return match.group(0)


class _Writer:
    def __init__(self, model: _InformationModel, uri: str) -> None:
        self.model = model
        self.uri = uri
        self.uris = [uri]
        self.aliases: dict[str, NodeRef] = {}
        self.exported = set(model.exportedNamespaces)
        self.basis = model.basis
        # The value encoder numbers namespaces by their position in the server table.
        self.serverUris = list(model.namespaces)

    def nsIndex(self, uri: str) -> int:
        if uri == NS0_URI:
            return 0
        if uri not in self.uris:
            self.uris.append(uri)
        return self.uris.index(uri) + 1

    def nsPrefix(self, uri: str) -> str:
        index = self.nsIndex(uri)
        return f"ns={index};" if index else ""

    def nodeIdText(self, ref: NodeRef) -> str:
        return self.nsPrefix(ref.namespaceUri) + ref.identifierText

    def aliasOrId(self, ref: NodeRef) -> str:
        """An ns0 DataType or ReferenceType by alias, anything else by NodeId."""
        info = self.model.types.get(ref)
        if ref.isNs0 and info is not None and info.browseName.name:
            name = info.browseName.name
            if self.aliases.setdefault(name, ref) == ref:
                return name
        return self.nodeIdText(ref)

    def browseNameText(self, name: QualifiedNameRef) -> str:
        index = self.nsIndex(name.namespaceUri)
        return name.name if index == 0 else f"{index}:{name.name}"

    def document(self) -> str:
        nodes = sorted(
            (node for ref, node in self.model.nodes.items() if ref.namespaceUri == self.uri),
            key=lambda node: (_CLASS_ORDER.get(int(node.nodeClass), 9), node.nodeId.sortKey()),
        )
        elements = [self.node(node) for node in nodes]

        root = _Element(
            "UANodeSet",
            {
                "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
                "xmlns:xsd": "http://www.w3.org/2001/XMLSchema",
                "LastModified": datetime.datetime.now(datetime.timezone.utc).strftime(
                    "%Y-%m-%dT%H:%M:%SZ"
                ),
                "xmlns": UANODESET_NS,
            },
        )
        namespace_uris = root.add(_Element("NamespaceUris"))
        for uri in self.uris:
            namespace_uris.add(_Element("Uri", text=uri))

        models = root.add(_Element("Models"))
        model = models.add(_Element("Model", self._modelAttrs(self.uri)))
        for required in [NS0_URI, *self.uris[1:]]:
            model.add(_Element("RequiredModel", self._modelAttrs(required)))

        if self.aliases:
            aliases = root.add(_Element("Aliases"))
            for name, ref in sorted(self.aliases.items(), key=lambda item: item[1].sortKey()):
                aliases.add(_Element("Alias", {"Alias": name}, self.nodeIdText(ref)))

        root.children.extend(elements)
        out = ['<?xml version="1.0" encoding="utf-8"?>']
        root.write(out, 0)
        return "\n".join(out) + "\n"

    def _modelAttrs(self, uri: str) -> dict[str, str]:
        attrs = {"ModelUri": uri}
        info = self.model.namespaces.get(uri) or NamespaceInfo(uri)
        if info.version:
            attrs["Version"] = info.version
        if info.publicationDate:
            attrs["PublicationDate"] = info.publicationDate
        return attrs

    def node(self, node: NodeRecord) -> _Element:
        node_class = int(node.nodeClass)
        attributes = node.attributes
        element = _Element(_ELEMENT_NAMES[node_class])
        attrs = element.attrs
        attrs["NodeId"] = self.nodeIdText(node.nodeId)
        attrs["BrowseName"] = self.browseNameText(node.browseName)

        self._warnMissing(node, node_class)
        references, parent = self.references(node)
        if parent is not None and self.model.isSubtypeOf(parent.referenceType, _HAS_CHILD):
            attrs["ParentNodeId"] = self.nodeIdText(parent.target)
        self._classAttributes(node_class, attributes, attrs)

        element.add(
            _localized("DisplayName", node.displayName)
            or _Element("DisplayName", text=node.browseName.name)
        )
        element.add(_localized("Description", node.description))

        refs = element.add(_Element("References"))
        for reference in references:
            ref_attrs = {"ReferenceType": self.aliasOrId(reference.referenceType)}
            if not reference.isForward:
                ref_attrs["IsForward"] = "false"
            refs.add(_Element("Reference", ref_attrs, self.nodeIdText(reference.target)))

        if attributes.get("RolePermissions"):
            permissions = element.add(_Element("RolePermissions"))
            for role, mask in attributes["RolePermissions"]:
                permissions.add(
                    _Element("RolePermission", {"Permissions": str(mask)}, self.nodeIdText(role))
                )

        if node_class == int(_NodeClass.REFERENCE_TYPE):
            element.add(_localized("InverseName", attributes.get("InverseName")))
        if node_class == int(_NodeClass.DATA_TYPE):
            element.add(self.definition(node))
        value = attributes.get("Value")
        if node_class in _VARIABLE_CLASSES and not _isEmpty(value):
            try:
                xml = self.valueXml(value)
            except (o6.StatusCodeError, TypeError, KeyError) as error:
                _logger.warning(f"{node.nodeId}: Value left out ({error})")
            else:
                if xml is not None:
                    element.add(_Element("Value", text=xml, raw=True))
        return element

    def _classAttributes(
        self, node_class: int, attributes: dict[str, Any], attrs: dict[str, str]
    ) -> None:
        """The NodeClass-specific XML attributes; defaults are left out."""
        if node_class in _VARIABLE_CLASSES:
            data_type = attributes.get("DataType")
            if isinstance(data_type, NodeRef) and data_type != _BASE_DATA_TYPE:
                attrs["DataType"] = self.aliasOrId(data_type)
            value_rank = attributes.get("ValueRank")
            if value_rank is not None:
                attrs["ValueRank"] = str(int(value_rank))
            dimensions = attributes.get("ArrayDimensions")
            if dimensions is not None and len(dimensions):
                attrs["ArrayDimensions"] = ",".join(str(int(d)) for d in dimensions)
        if node_class == int(_NodeClass.VARIABLE):
            access = attributes.get("AccessLevelEx", attributes.get("AccessLevel"))
            if access is not None and int(access) != 1:
                attrs["AccessLevel"] = str(int(access))
            interval = attributes.get("MinimumSamplingInterval")
            if interval:
                attrs["MinimumSamplingInterval"] = f"{float(interval):g}"
            if attributes.get("Historizing"):
                attrs["Historizing"] = "true"
        if node_class in (int(_NodeClass.OBJECT), int(_NodeClass.VIEW)):
            notifier = attributes.get("EventNotifier")
            if notifier:
                attrs["EventNotifier"] = str(int(notifier))
        if node_class == int(_NodeClass.VIEW) and attributes.get("ContainsNoLoops"):
            attrs["ContainsNoLoops"] = "true"
        if node_class == int(_NodeClass.METHOD):
            executable = attributes.get("Executable")
            if executable is not None and not executable:
                attrs["Executable"] = "false"
        if attributes.get("IsAbstract") and node_class not in _INSTANCE_CLASSES:
            attrs["IsAbstract"] = "true"
        if node_class == int(_NodeClass.REFERENCE_TYPE) and attributes.get("Symmetric"):
            attrs["Symmetric"] = "true"
        access_restrictions = attributes.get("AccessRestrictions")
        if access_restrictions:
            attrs["AccessRestrictions"] = str(int(access_restrictions))
        write_mask = attributes.get("WriteMask")
        if write_mask:
            attrs["WriteMask"] = str(int(write_mask))

    def valueXml(self, value: Any) -> str | None:
        """The content of `<Value>`, encoded by open62541 and renumbered for this file.

        The encoder writes NodeIds with their namespace URI and QualifiedNames
        with the namespace's position in the server table. `None` for a value
        holding a null structure, which has no body to write. A TypeId names
        the Default XML encoding of the DataType, and DateTimes out of range are
        written as the earliest or latest one.
        """
        xml = _encodeValue(self.model, value)
        if "<ExtensionObject></ExtensionObject>" in xml:
            return None
        xml = _TYPE_ID.sub(self._xmlEncodingTypeId, xml)
        xml = _DATE_TIME.sub(_clampDateTime, xml)
        xml = re.sub(
            r"<Identifier>nsu=([^;<]+);",
            lambda m: f"<Identifier>{self.nsPrefix(unescape(m.group(1)))}",
            xml,
        )
        xml = re.sub(
            r"<NamespaceIndex>(\d+)<",
            lambda m: f"<NamespaceIndex>{self.nsIndex(self.serverUris[int(m.group(1))])}<",
            xml,
        )
        xml = xml.removeprefix("<Variant><Value>").removesuffix("</Value></Variant>")
        return re.sub(r"^<(\w+)", rf'<\1 xmlns="{TYPES_NS}"', xml, count=1)

    def _xmlEncodingTypeId(self, match: re.Match[str]) -> str:
        """The TypeId as the Default XML encoding, in the encoder's `nsu=` form."""
        type_id = _parseNodeIdText(match.group(1))
        encoding = self.model.xmlEncodings.get(type_id) if type_id is not None else None
        if encoding is None:
            return match.group(0)
        text = encoding.identifierText
        if not encoding.isNs0:
            text = f"nsu={encoding.namespaceUri};{text}"
        return f"<TypeId><Identifier>{escape(text)}</Identifier></TypeId>"

    def _keeps(self, reference: Reference) -> bool:
        """Write a cross-namespace reference in one file only, so files don't require each other."""
        target = reference.target.namespaceUri
        if target in (self.uri, NS0_URI):
            return True
        if target not in self.exported:
            return True  # into the published NodeSet of a required model
        if reference.target not in self.model.nodes:
            return False  # not crawled, no file could resolve it
        if target in self.basis.get(self.uri, ()):
            return True
        if self.uri in self.basis.get(target, ()):
            return False
        return self._dependsOn(target)

    def _dependsOn(self, other: str) -> bool:
        """Whether this file holds the references to `other`, a namespace it is unrelated to.

        The server's own namespace builds on a companion specification;
        otherwise the later one in the server's namespace table builds on the
        earlier one. Either way all references between the two go into one file.
        """
        companion = self._isCompanion(self.uri)
        if companion != self._isCompanion(other):
            return not companion
        return self._serverOrder(self.uri) > self._serverOrder(other)

    def _isCompanion(self, uri: str) -> bool:
        info = self.model.namespaces.get(uri)
        return info is not None and info.isCompanion

    def _serverOrder(self, uri: str) -> int:
        return self.serverUris.index(uri) if uri in self.serverUris else len(self.serverUris)

    def references(self, node: NodeRecord) -> tuple[list[Reference], Reference | None]:
        """The node's references in UA-Nodeset order, and its parent reference.

        HasTypeDefinition comes first, then the parent: the compiler takes the
        first inverse hierarchical reference as the parent.
        """
        # Types don't list their instances, as in the published NodeSets.
        kept = [
            r
            for r in node.references
            if (r.isForward or r.referenceType != _HAS_TYPE_DEFINITION) and self._keeps(r)
        ]
        type_definition = next(
            (r for r in kept if r.isForward and r.referenceType == _HAS_TYPE_DEFINITION), None
        )
        parent = self._parent(node, kept)
        head = [r for r in (type_definition, parent) if r is not None]
        rest = sorted((r for r in kept if r not in head), key=_referenceOrder)
        return head + rest, parent if int(node.nodeClass) in _INSTANCE_CLASSES else None

    def _parent(self, node: NodeRecord, references: list[Reference]) -> Reference | None:
        """The parent reference: the supertype of a type, the container of an instance."""
        inverse = [r for r in references if not r.isForward]
        if int(node.nodeClass) not in _INSTANCE_CLASSES:
            return next((r for r in inverse if r.referenceType == _HAS_SUBTYPE), None)
        parents = [
            r for r in inverse if self.model.isSubtypeOf(r.referenceType, _HIERARCHICAL_REFERENCES)
        ]
        # HasComponent, HasProperty, ... before Organizes.
        parents.sort(key=lambda r: not self.model.isSubtypeOf(r.referenceType, _HAS_CHILD))
        return parents[0] if parents else None

    def _warnMissing(self, node: NodeRecord, node_class: int) -> None:
        """Warn about a missing HasTypeDefinition or supertype, which o6-ncc rejects."""
        if node_class in (int(_NodeClass.OBJECT), int(_NodeClass.VARIABLE)):
            if node.typeDefinition is None:
                _logger.warning(f"{node.nodeId}: no HasTypeDefinition")
        elif node_class not in _INSTANCE_CLASSES and node.supertype is None:
            _logger.warning(f"{node.nodeId}: no supertype")

    def optionSetDefinition(self, node: NodeRecord) -> _Element | None:
        """The OptionSet bits from the OptionSetValues Property, for a server without DataTypeDefinition."""
        if not self.model.isSubtypeOf(node.nodeId, _UINTEGER):
            return None
        properties = (
            self.model.nodes.get(r.target)
            for r in node.references
            if r.referenceType == _HAS_PROPERTY and r.isForward
        )
        values = next((p for p in properties if p and p.browseName == _OPTION_SET_VALUES), None)
        if values is None or values.attributes.get("Value") is None:
            return None
        element = _Element(
            "Definition", {"Name": self.browseNameText(node.browseName), "IsOptionSet": "true"}
        )
        for bit, name in enumerate(values.attributes["Value"]):
            if name.text:
                element.add(_Element("Field", {"Name": name.text, "Value": str(bit)}))
        return element

    def definition(self, node: NodeRecord) -> _Element | None:
        definition = node.attributes.get("DataTypeDefinition")
        if definition is None:
            return self.optionSetDefinition(node)
        element = _Element("Definition", {"Name": self.browseNameText(node.browseName)})
        if isinstance(definition, ns0.datatypes.StructureDefinition):
            if int(definition.structureType) in _UNIONS:
                element.attrs["IsUnion"] = "true"
            for item in definition.fields or ():
                attrs = {"Name": item.name}
                data_type = self.model.ref(item.dataType)
                if data_type != _BASE_DATA_TYPE:
                    attrs["DataType"] = self.aliasOrId(data_type)
                if int(item.valueRank) != -1:
                    attrs["ValueRank"] = str(int(item.valueRank))
                if item.arrayDimensions is not None and len(item.arrayDimensions):
                    attrs["ArrayDimensions"] = ",".join(str(int(d)) for d in item.arrayDimensions)
                if item.isOptional:
                    attrs["IsOptional"] = "true"
                if item.maxStringLength:
                    _logger.warning(
                        f"{node.nodeId}: MaxStringLength of field {item.name} is left out"
                    )
                field_element = element.add(_Element("Field", attrs))
                field_element.add(_localized("Description", item.description))
        elif isinstance(definition, ns0.datatypes.EnumDefinition):
            if not self.model.isSubtypeOf(node.nodeId, _ENUMERATION):
                element.attrs["IsOptionSet"] = "true"
            for entry in definition.fields or ():
                field_element = element.add(
                    _Element("Field", {"Name": entry.name, "Value": str(int(entry.value))})
                )
                if entry.displayName is not None and entry.displayName.text != entry.name:
                    field_element.add(_localized("DisplayName", entry.displayName))
                field_element.add(_localized("Description", entry.description))
        else:
            return None
        return element


def write_nodeset(model: _InformationModel, uri: str) -> str:
    """Render one namespace of `model` as a NodeSet2 XML document."""
    return _Writer(model, uri).document()
