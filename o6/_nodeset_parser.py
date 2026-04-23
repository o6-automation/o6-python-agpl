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
"""
OPC UA NodeSet2 XML parser.

Parses a NodeSet2 XML file (``*.NodeSet2.xml``) into a :class:`Namespace`
descriptor using only :mod:`xml.etree.ElementTree` from the standard library.

The parser handles:

* Metadata: namespace URI, version, publication date, required model URIs.
* Type definitions: structures, enums, and unions across OPC UA spec versions
  1.03 (``<DataTypeDefinition>``), 1.04 (``<StructureDefinition>`` /
  ``<EnumDefinition>``), and 1.05 (``<UnionDefinition>`` / ``StructureType=2``),
  as well as the compact inline ``<Definition>`` form that some node exporters
  emit.
* Node hierarchy: all eight UA node classes (Object, Variable, Method,
  ObjectType, VariableType, ReferenceType, DataType, View) are parsed and
  sorted into the eight typed containers on the returned ``Namespace``
  (``objects``, ``datatypes``, ``objtypes``, ``eventtypes``, ``ifacetypes``,
  ``reftypes``, ``vartypes``, ``views``), with children nested under their
  parents via hierarchical references.

Public API
----------
parse_nodeset(xml_path, owner) -> Namespace
"""

from __future__ import annotations

import codecs
import logging
import re
import xml.etree.ElementTree as ET
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .namespaces import Namespaces

from .namespace import (
    Namespace,
    NamespaceDataTypeNode,
    NamespaceMethodNode,
    NamespaceObjectNode,
    NamespaceObjectTypeNode,
    NamespaceReferenceTypeNode,
    NamespaceVariableNode,
    NamespaceVariableTypeNode,
    NamespaceViewNode,
)

_logger = logging.getLogger(__name__)

# XML namespace of NodeSet2 files
_XSD = "http://opcfoundation.org/UA/2011/03/UANodeSet.xsd"
_UA_URI = "http://opcfoundation.org/UA/"

# Hardcoded well-known ns=0 reference type NodeIds (canonical "i=NNN" form,
# i.e. the "ns=0;" prefix is always stripped during normalisation).
_HAS_SUBTYPE = "i=45"
_HAS_COMPONENT = "i=47"
_HAS_PROPERTY = "i=46"
_ORGANIZES = "i=35"
_HAS_ENCODING = "i=38"
_HIERARCHICAL_REFS = frozenset(
    {_HAS_SUBTYPE, _HAS_COMPONENT, _HAS_PROPERTY, _ORGANIZES}
)

# Roots of the EventType and InterfaceType hierarchies (ns=0)
_EVENT_TYPE_ROOT = "i=2041"  # BaseEventType
_IFACE_TYPE_ROOT = "i=17602"  # BaseInterfaceType

# ns=0 abstract DataTypes that cannot be built by the C extension.
# Each maps to its nearest buildable ancestor.
_NS0_UNRESOLVABLE: dict[str, str] = {
    "i=26": "i=24",  # Number        → Variant (abstract)
    "i=27": "i=24",  # Integer       → Variant (abstract)
    "i=28": "i=24",  # UInteger      → Variant (abstract)
    "i=30": "i=15",  # Image         → ByteString
    "i=50": "i=24",  # Decimal       → Variant (abstract)
    "i=25726": "i=12",  # EncodedTicket → String
    "i=31917": "i=7",  # Handle        → UInt32
    "i=31918": "i=12",  # TrimmedString → String
}

# ──────────────────────────────────────────────────────────────────────────────
# Public entry point
# ──────────────────────────────────────────────────────────────────────────────


def extract_model_info(xml_path: str) -> tuple[str, list[tuple[str, str]]]:
    """Return ``(model_uri, [(required_uri, required_version)])`` for a NodeSet2 file.

    Lightweight — only parses the ``<Models>`` block, no type or node extraction.
    Useful for resolving load order without doing a full parse.
    """
    text = _read_file(xml_path)
    root = ET.fromstring(text)
    model_uri, _, _ = _extract_metadata(root)
    required = _extract_required_models(root)
    return model_uri, required


def parse_nodeset(xml_path: str, owner: "Namespaces") -> "Namespace":
    """Parse a NodeSet2 XML file and return a populated Namespace.

    Thread-safe: does not read or write any shared Namespaces state.
    Call Namespaces.append() sequentially in dependency order afterwards.
    """
    text = _read_file(xml_path)
    root = ET.fromstring(text)

    model_uri, version, pub_date = _extract_metadata(root)
    required_models = _extract_required_models(root)

    # [OPC_UA_URI, ns1_uri, ns2_uri, ...] — index matches the ns= prefix used
    # in NodeId strings within this file.
    ns_uri_list = _build_ns_uri_list(root)
    my_ns_index = _find_my_ns_index(ns_uri_list, model_uri)

    alias_map = _build_alias_map(root)

    descriptor = Namespace(uri=model_uri, version=version, publication_date=pub_date)
    for req_uri, req_ver in required_models:
        descriptor._add_required_namespace(req_uri, req_ver)

    # Build the encoding map first (needed by type-def extraction).
    # We build it directly from the XML instead of from the _NodeInfo table
    # so that non-our-namespace encoding objects are also captured.
    enc_map = _build_encoding_map_from_xml(root, alias_map)

    # Subtype map for abstract intermediate DataType resolution.
    subtype_map = _build_subtype_map(root, alias_map)

    # Extract StructureDescription / EnumDescription into descriptor.
    _extract_type_defs(root, descriptor, alias_map, enc_map, subtype_map)

    # Parse all nodes and populate the 8 node hierarchy containers.
    nodes = _parse_all_nodes(root, alias_map)
    _populate_hierarchy(nodes, descriptor, my_ns_index)

    return descriptor


# ──────────────────────────────────────────────────────────────────────────────
# File reading
# ──────────────────────────────────────────────────────────────────────────────


def _read_file(path: str) -> str:
    """Read an XML file, stripping BOM and the `uax:` element-name prefix
    that some UaModeler-generated files inject."""
    with open(path, "rb") as fh:
        raw = fh.read()
    if raw.startswith(codecs.BOM_UTF8):
        raw = raw[len(codecs.BOM_UTF8) :]
    text = raw.decode("utf-8")
    # Strip uax: prefix from element tags (UaModeler compatibility).
    text = re.sub(r"<([/]?)uax:(.+?)([/]?)>", r"<\1\2\3>", text)
    return text


# ──────────────────────────────────────────────────────────────────────────────
# Metadata helpers
# ──────────────────────────────────────────────────────────────────────────────


def _extract_metadata(root: ET.Element) -> tuple[str, str, str | None]:
    """Return (model_uri, version, publication_date)."""
    model_uri = ""
    version = "1.0.0"
    pub_date: str | None = None

    models_el = root.find(f".//{{{_XSD}}}Models")
    if models_el is not None:
        model_el = models_el.find(f"{{{_XSD}}}Model")
        if model_el is not None:
            model_uri = model_el.get("ModelUri", "")
            version = model_el.get("Version", "1.0.0")
            pub_date = model_el.get("PublicationDate")

    if not model_uri:
        uris = _extract_uri_list(root)
        model_uri = uris[-1] if uris else "http://example.com/unknown"

    return model_uri, version, pub_date


def _extract_required_models(root: ET.Element) -> list[tuple[str, str]]:
    """Return [(model_uri, version)] for every <RequiredModel> element."""
    result: list[tuple[str, str]] = []
    models_el = root.find(f".//{{{_XSD}}}Models")
    if models_el is None:
        return result
    for req in models_el.findall(f".//{{{_XSD}}}RequiredModel"):
        uri = req.get("ModelUri", "")
        ver = req.get("Version", "")
        if uri:
            result.append((uri, ver))
    return result


def _extract_uri_list(root: ET.Element) -> list[str]:
    """Return the bare <Uri> strings from <NamespaceUris> (excludes ns=0)."""
    ns_uris_el = root.find(f".//{{{_XSD}}}NamespaceUris")
    if ns_uris_el is None:
        return []
    return [el.text.strip() for el in ns_uris_el.findall(f"{{{_XSD}}}Uri") if el.text]


def _build_ns_uri_list(root: ET.Element) -> list[str]:
    """Build ``[OPC_UA_URI, ns1_uri, ns2_uri, ...]`` namespace index list."""
    return [_UA_URI] + _extract_uri_list(root)


def _find_my_ns_index(ns_uri_list: list[str], model_uri: str) -> int:
    """Return the namespace index for the model URI being parsed."""
    try:
        return ns_uri_list.index(model_uri)
    except ValueError:
        return 1  # safe fallback for single-namespace files


# ──────────────────────────────────────────────────────────────────────────────
# Alias map
# ──────────────────────────────────────────────────────────────────────────────


def _build_alias_map(root: ET.Element) -> dict[str, str]:
    """Build ``{alias_name → NodeId_string}`` from <Aliases>."""
    aliases: dict[str, str] = {}
    aliases_el = root.find(f"{{{_XSD}}}Aliases")
    if aliases_el is None:
        return aliases
    for alias_el in aliases_el:
        name = alias_el.get("Alias", "")
        if name and alias_el.text:
            aliases[name] = alias_el.text.strip()
    return aliases


# ──────────────────────────────────────────────────────────────────────────────
# NodeId helpers
# ──────────────────────────────────────────────────────────────────────────────


def _norm_nid(s: str, aliases: dict[str, str] | None = None) -> str:
    """Normalise a NodeId or alias to canonical ``i=NNN`` / ``ns=X;i=NNN`` form.

    - Resolves aliases when the ``aliases`` dict is supplied.
    - Strips ``ns=0;`` prefix (``"ns=0;i=45"`` → ``"i=45"``).
    """
    s = s.strip()
    if aliases:
        s = aliases.get(s, s)
    if s.startswith("ns=0;"):
        return s[5:]
    return s


def _nid_ns_index(nodeid: str) -> int:
    """Return the namespace index embedded in a normalised NodeId string."""
    if nodeid.startswith("ns="):
        m = re.match(r"ns=(\d+);", nodeid)
        if m:
            return int(m.group(1))
    return 0


def _parse_browse_name(bn: str) -> str:
    """Strip optional ``N:`` namespace-index prefix from a BrowseName."""
    colon = bn.find(":")
    if colon > 0 and bn[:colon].isdigit():
        return bn[colon + 1 :]
    return bn


# ──────────────────────────────────────────────────────────────────────────────
# Node table
# ──────────────────────────────────────────────────────────────────────────────


class _NodeInfo:
    """Lightweight representation of a parsed OPC UA node."""

    __slots__ = ("nodeid", "browse_name", "kind", "refs")

    def __init__(
        self,
        nodeid: str,
        browse_name: str,
        kind: str,
        refs: list[tuple[str, str, bool]],
    ) -> None:
        self.nodeid = nodeid
        self.browse_name = browse_name
        # One of: "object"|"variable"|"method"|"objecttype"|"variabletype"|
        #         "referencetype"|"datatype"|"view"
        self.kind = kind
        # (normalised_ref_type, normalised_target, is_forward)
        self.refs = refs


# ElementTree tag → kind string (XSD-namespaced UA element names)
_KIND_TAGS: dict[str, str] = {
    f"{{{_XSD}}}UAObject": "object",
    f"{{{_XSD}}}UAVariable": "variable",
    f"{{{_XSD}}}UAMethod": "method",
    f"{{{_XSD}}}UAObjectType": "objecttype",
    f"{{{_XSD}}}UAVariableType": "variabletype",
    f"{{{_XSD}}}UAReferenceType": "referencetype",
    f"{{{_XSD}}}UADataType": "datatype",
    f"{{{_XSD}}}UAView": "view",
}

_REFS_TAG = f"{{{_XSD}}}References"
_REF_TAG = f"{{{_XSD}}}Reference"


def _parse_refs(
    node_el: ET.Element,
    aliases: dict[str, str],
) -> list[tuple[str, str, bool]]:
    """Parse the ``<References>`` child of a node element."""
    refs_el = node_el.find(_REFS_TAG)
    if refs_el is None:
        return []
    refs: list[tuple[str, str, bool]] = []
    for ref_el in refs_el.findall(_REF_TAG):
        rt = _norm_nid(ref_el.get("ReferenceType", ""), aliases)
        target_text = ref_el.text
        if not target_text:
            continue
        target = _norm_nid(target_text, aliases)
        is_fwd = ref_el.get("IsForward", "true").lower() != "false"
        refs.append((rt, target, is_fwd))
    return refs


def _parse_all_nodes(
    root: ET.Element,
    alias_map: dict[str, str],
) -> dict[str, _NodeInfo]:
    """Build ``{normalised_nodeid → _NodeInfo}`` for every node in the file."""
    nodes: dict[str, _NodeInfo] = {}
    for el in root:
        kind = _KIND_TAGS.get(el.tag)
        if kind is None:
            continue
        raw_nid = el.get("NodeId", "")
        if not raw_nid:
            continue
        nodeid = _norm_nid(raw_nid)
        raw_bn = el.get("BrowseName", "")
        browse_name = _parse_browse_name(raw_bn) if raw_bn else ""
        if not browse_name:
            continue
        refs = _parse_refs(el, alias_map)
        nodes[nodeid] = _NodeInfo(nodeid, browse_name, kind, refs)
    return nodes


# ──────────────────────────────────────────────────────────────────────────────
# Binary encoding map
# ──────────────────────────────────────────────────────────────────────────────


def _build_encoding_map_from_xml(
    root: ET.Element,
    alias_map: dict[str, str],
) -> dict[str, str]:
    """Return ``{struct_nodeid → default_binary_encoding_nodeid}``.

    Two discovery paths are used (matching the original handler logic):

    * **Path 1** – A ``UAObject`` with ``BrowseName="Default Binary"`` carries a
      backward ``HasEncoding`` reference pointing to the owning DataType.
    * **Path 2** – A ``UADataType`` carries a forward ``HasEncoding`` reference
      pointing to its encoding object (expressed only in this direction in some
      nodesets).
    """
    enc_map: dict[str, str] = {}

    # Collect NodeIds of all "Default Binary" encoding objects (Path 1)
    default_binary_ids: set[str] = set()
    for obj_el in root.iter(f"{{{_XSD}}}UAObject"):
        raw_bn = _parse_browse_name(obj_el.get("BrowseName", ""))
        if raw_bn != "Default Binary":
            continue
        obj_id = _norm_nid(obj_el.get("NodeId", ""))
        if not obj_id:
            continue
        default_binary_ids.add(obj_id)

        refs_el = obj_el.find(_REFS_TAG)
        if refs_el is None:
            continue
        for ref_el in refs_el.findall(_REF_TAG):
            rt = _norm_nid(ref_el.get("ReferenceType", ""), alias_map)
            if rt != _HAS_ENCODING:
                continue
            is_fwd = ref_el.get("IsForward", "true").lower() != "false"
            if not is_fwd and ref_el.text:
                enc_map[_norm_nid(ref_el.text.strip(), alias_map)] = obj_id

    # Path 2 – forward HasEncoding on the DataType
    for dt_el in root.iter(f"{{{_XSD}}}UADataType"):
        dt_id = _norm_nid(dt_el.get("NodeId", ""))
        if not dt_id or dt_id in enc_map:
            continue
        refs_el = dt_el.find(_REFS_TAG)
        if refs_el is None:
            continue
        for ref_el in refs_el.findall(_REF_TAG):
            rt = _norm_nid(ref_el.get("ReferenceType", ""), alias_map)
            if rt != _HAS_ENCODING:
                continue
            is_fwd = ref_el.get("IsForward", "true").lower() != "false"
            if is_fwd and ref_el.text:
                target = _norm_nid(ref_el.text.strip(), alias_map)
                if target in default_binary_ids:
                    enc_map[dt_id] = target
                    break

    return enc_map


# ──────────────────────────────────────────────────────────────────────────────
# Subtype map (abstract DataType resolution for field data_type values)
# ──────────────────────────────────────────────────────────────────────────────

_DEFINITION_TAGS = frozenset(
    {
        f"{{{_XSD}}}StructureDefinition",
        f"{{{_XSD}}}EnumDefinition",
        f"{{{_XSD}}}UnionDefinition",
        f"{{{_XSD}}}Definition",
        f"{{{_XSD}}}DataTypeDefinition",
    }
)


def _build_subtype_map(
    root: ET.Element,
    alias_map: dict[str, str],
) -> dict[str, str]:
    """Return ``{abstract_nodeid → parent_nodeid}`` for DataTypes without a
    concrete definition (i.e. intermediate abstract types only).

    This map is walked when resolving a struct field's ``DataType`` attribute
    to its nearest actually-buildable ancestor.
    """
    subtype_map: dict[str, str] = {}
    for dt_el in root.iter(f"{{{_XSD}}}UADataType"):
        # Skip DataTypes that have their own type definition — those are
        # concrete types we will build directly.
        has_def = any(child.tag in _DEFINITION_TAGS for child in dt_el)
        if has_def:
            continue
        nodeid = _norm_nid(dt_el.get("NodeId", ""))
        if not nodeid:
            continue
        refs_el = dt_el.find(_REFS_TAG)
        if refs_el is None:
            continue
        for ref_el in refs_el.findall(_REF_TAG):
            rt = _norm_nid(ref_el.get("ReferenceType", ""), alias_map)
            if rt != _HAS_SUBTYPE:
                continue
            is_fwd = ref_el.get("IsForward", "true").lower() != "false"
            if not is_fwd and ref_el.text:
                subtype_map[nodeid] = _norm_nid(ref_el.text.strip(), alias_map)
                break
    return subtype_map


# ──────────────────────────────────────────────────────────────────────────────
# Data type resolution
# ──────────────────────────────────────────────────────────────────────────────


def _resolve_dt(
    dt: str,
    alias_map: dict[str, str],
    subtype_map: dict[str, str],
) -> str:
    """Resolve an alias and walk up the abstract subtype chain."""
    dt = _norm_nid(dt, alias_map)
    visited: set[str] = set()
    while dt not in visited:
        if dt in subtype_map:
            visited.add(dt)
            dt = subtype_map[dt]
        elif dt in _NS0_UNRESOLVABLE:
            visited.add(dt)
            dt = _NS0_UNRESOLVABLE[dt]
        else:
            break
    return dt


# ──────────────────────────────────────────────────────────────────────────────
# Type-definition extraction (structures + enums)
# ──────────────────────────────────────────────────────────────────────────────


def _extract_type_defs(
    root: ET.Element,
    descriptor: "Namespace",
    alias_map: dict[str, str],
    enc_map: dict[str, str],
    subtype_map: dict[str, str],
) -> None:
    """Walk every ``<UADataType>`` and add structure/enum descriptions."""
    for dt_el in root.iter(f"{{{_XSD}}}UADataType"):
        nodeid = _norm_nid(dt_el.get("NodeId", ""))
        if not nodeid:
            continue
        browse_name = _parse_browse_name(dt_el.get("BrowseName", ""))
        if not browse_name:
            continue
        try:
            _parse_datatype_el(
                dt_el, nodeid, browse_name, descriptor, alias_map, enc_map, subtype_map
            )
        except Exception as exc:
            _logger.warning(
                "Failed to parse DataType %s (%s): %s", browse_name, nodeid, exc
            )


def _parse_datatype_el(
    dt_el: ET.Element,
    nodeid: str,
    browse_name: str,
    descriptor: "Namespace",
    alias_map: dict[str, str],
    enc_map: dict[str, str],
    subtype_map: dict[str, str],
) -> None:
    """Dispatch a single ``<UADataType>`` to the appropriate sub-parser."""
    # v1.04+ explicit StructureDefinition
    struct_def = dt_el.find(f"{{{_XSD}}}StructureDefinition")
    if struct_def is not None:
        _parse_structure_def(
            struct_def, nodeid, browse_name, descriptor, alias_map, enc_map, subtype_map
        )
        return

    # v1.04+ explicit EnumDefinition
    enum_def = dt_el.find(f"{{{_XSD}}}EnumDefinition")
    if enum_def is not None:
        _parse_enum_def(enum_def, nodeid, browse_name, descriptor)
        return

    # v1.05 UnionDefinition (explicit union syntax)
    union_def = dt_el.find(f"{{{_XSD}}}UnionDefinition")
    if union_def is not None:
        _parse_union_def(
            union_def, nodeid, browse_name, descriptor, alias_map, enc_map, subtype_map
        )
        return

    # v1.04 compact inline <Definition> (Field elements; struct or enum by heuristic)
    definition = dt_el.find(f"{{{_XSD}}}Definition")
    if definition is not None:
        _parse_inline_def(
            definition, nodeid, browse_name, descriptor, alias_map, enc_map, subtype_map
        )
        return

    # v1.03 legacy <DataTypeDefinition>
    dt_def = dt_el.find(f"{{{_XSD}}}DataTypeDefinition")
    if dt_def is not None:
        _parse_v103_def(dt_def, nodeid, browse_name, descriptor, alias_map, subtype_map)


# ── Structure ─────────────────────────────────────────────────────────────────


def _parse_struct_fields(
    parent_el: ET.Element,
    field_tag: str,
    alias_map: dict[str, str],
    subtype_map: dict[str, str],
) -> list[dict[str, Any]]:
    fields: list[dict[str, Any]] = []
    for f in parent_el.findall(f".//{{{_XSD}}}{field_tag}"):
        fd: dict[str, Any] = {
            "name": f.get("Name", "UnknownField"),
            "value_rank": int(f.get("ValueRank", "-1")),
            "data_type": _resolve_dt(f.get("DataType", "i=24"), alias_map, subtype_map),
        }
        if f.get("IsOptional", "false").lower() == "true":
            fd["is_optional"] = True
        desc = f.get("Description", "")
        if desc:
            fd["description"] = desc
        arr_dim = f.get("ArrayDimensions", "")
        if arr_dim:
            fd["array_dimensions"] = arr_dim
        msl = f.get("MaxStringLength", "0")
        if msl and msl != "0":
            fd["max_string_length"] = int(msl)
        fields.append(fd)
    return fields


def _parse_structure_def(
    struct_def: ET.Element,
    nodeid: str,
    browse_name: str,
    descriptor: "Namespace",
    alias_map: dict[str, str],
    enc_map: dict[str, str],
    subtype_map: dict[str, str],
) -> None:
    struct_type = int(struct_def.get("StructureType", "0"))
    fields = _parse_struct_fields(struct_def, "StructureField", alias_map, subtype_map)
    descriptor._add_structure_description(
        nodeid,
        browse_name,
        {"structure_type": struct_type, "fields": fields},
        default_encoding_id=enc_map.get(nodeid),
    )


def _parse_union_def(
    union_def: ET.Element,
    nodeid: str,
    browse_name: str,
    descriptor: "Namespace",
    alias_map: dict[str, str],
    enc_map: dict[str, str],
    subtype_map: dict[str, str],
) -> None:
    fields = _parse_struct_fields(union_def, "StructureField", alias_map, subtype_map)
    if fields:
        descriptor._add_structure_description(
            nodeid,
            browse_name,
            {"structure_type": 2, "fields": fields},  # Union = StructureType 2
            default_encoding_id=enc_map.get(nodeid),
        )


# ── Enum ──────────────────────────────────────────────────────────────────────


def _collect_enum_fields(
    parent_el: ET.Element,
    field_tag: str,
) -> list[dict[str, Any]]:
    fields: list[dict[str, Any]] = []
    for f in parent_el.findall(f".//{{{_XSD}}}{field_tag}"):
        fd: dict[str, Any] = {
            "name": f.get("Name", "UnknownValue"),
            "value": int(f.get("Value", "0")),
        }
        dn = f.get("DisplayName") or f.get("Name", "")
        if dn:
            fd["display_name"] = dn
        desc = f.get("Description", "")
        if desc:
            fd["description"] = desc
        fields.append(fd)
    return fields


def _parse_enum_def(
    enum_def: ET.Element,
    nodeid: str,
    browse_name: str,
    descriptor: "Namespace",
) -> None:
    fields = _collect_enum_fields(enum_def, "EnumField")
    if fields:
        descriptor._add_enum_description(nodeid, browse_name, {"fields": fields})


# ── Inline <Definition> (v1.03 / v1.04 compact) ──────────────────────────────


def _parse_inline_def(
    definition: ET.Element,
    nodeid: str,
    browse_name: str,
    descriptor: "Namespace",
    alias_map: dict[str, str],
    enc_map: dict[str, str],
    subtype_map: dict[str, str],
) -> None:
    field_tag = f"{{{_XSD}}}Field"
    fields = list(definition.findall(f".//{field_tag}"))

    if not fields:
        # Empty structure
        descriptor._add_structure_description(
            nodeid,
            browse_name,
            {"structure_type": 0, "fields": []},
            default_encoding_id=enc_map.get(nodeid),
        )
        return

    first = fields[0]
    if "Value" in first.attrib and "DataType" not in first.attrib:
        # Enum: fields carry a numeric Value but no DataType
        enum_fields = _collect_enum_fields(definition, "Field")
        descriptor._add_enum_description(nodeid, browse_name, {"fields": enum_fields})
    else:
        # Structure
        struct_fields: list[dict[str, Any]] = []
        has_optional = False
        for f in fields:
            fd: dict[str, Any] = {
                "name": f.get("Name", "UnknownField"),
                "value_rank": int(f.get("ValueRank", "-1")),
                "data_type": _resolve_dt(
                    f.get("DataType", "i=24"), alias_map, subtype_map
                ),
            }
            if f.get("IsOptional", "false").lower() == "true":
                fd["is_optional"] = True
                has_optional = True
            desc = f.get("Description", "")
            if desc:
                fd["description"] = desc
            struct_fields.append(fd)
        descriptor._add_structure_description(
            nodeid,
            browse_name,
            {"structure_type": 1 if has_optional else 0, "fields": struct_fields},
            default_encoding_id=enc_map.get(nodeid),
        )


# ── Legacy v1.03 <DataTypeDefinition> ────────────────────────────────────────


def _parse_v103_def(
    dt_def: ET.Element,
    nodeid: str,
    browse_name: str,
    descriptor: "Namespace",
    alias_map: dict[str, str],
    subtype_map: dict[str, str],
) -> None:
    # <Field> elements → structure; <EnumField> elements → enum
    struct_fields_el = list(dt_def.findall(f".//{{{_XSD}}}Field"))
    if struct_fields_el:
        fields: list[dict[str, Any]] = []
        for f in struct_fields_el:
            fd: dict[str, Any] = {
                "name": f.get("Name", "UnknownField"),
                "value_rank": int(f.get("ValueRank", "-1")),
                "data_type": _resolve_dt(
                    f.get("DataType", "i=24"), alias_map, subtype_map
                ),
            }
            if f.get("IsOptional", "false").lower() == "true":
                fd["is_optional"] = True
            desc = f.get("Description", "")
            if desc:
                fd["description"] = desc
            fields.append(fd)
        descriptor._add_structure_description(
            nodeid,
            browse_name,
            {"structure_type": 0, "fields": fields},
        )
        return

    enum_fields_el = list(dt_def.findall(f".//{{{_XSD}}}EnumField"))
    if enum_fields_el:
        fields_e = _collect_enum_fields(dt_def, "EnumField")
        if fields_e:
            descriptor._add_enum_description(nodeid, browse_name, {"fields": fields_e})


# ──────────────────────────────────────────────────────────────────────────────
# Node hierarchy population
# ──────────────────────────────────────────────────────────────────────────────


def _make_ns_node(info: _NodeInfo) -> Any:
    """Instantiate the appropriate ``NamespaceXxxNode`` for *info*."""
    nid = info.nodeid
    kind = info.kind
    if kind == "datatype":
        return NamespaceDataTypeNode(nid, None)
    if kind == "objecttype":
        return NamespaceObjectTypeNode(nid)
    if kind == "referencetype":
        return NamespaceReferenceTypeNode(nid)
    if kind == "variabletype":
        return NamespaceVariableTypeNode(nid)
    if kind == "view":
        return NamespaceViewNode(nid)
    if kind == "method":
        return NamespaceMethodNode(nid)
    if kind == "variable":
        return NamespaceVariableNode(nid)
    return NamespaceObjectNode(nid)


def _pick_container(
    descriptor: "Namespace",
    kind: str,
    nid: str,
    event_ids: set[str],
    iface_ids: set[str],
) -> Any:
    if kind == "datatype":
        return descriptor.datatypes
    if kind == "objecttype":
        if nid in event_ids:
            return descriptor.eventtypes
        if nid in iface_ids:
            return descriptor.ifacetypes
        return descriptor.objtypes
    if kind == "referencetype":
        return descriptor.reftypes
    if kind == "variabletype":
        return descriptor.vartypes
    if kind == "view":
        return descriptor.views
    # object / variable / method
    return descriptor.objects


def _populate_hierarchy(
    nodes: dict[str, _NodeInfo],
    descriptor: "Namespace",
    my_ns_index: int,
) -> None:
    """Populate the 8 ``Namespace`` node containers from *nodes*."""
    # Filter to only our namespace
    my_nodes: dict[str, _NodeInfo] = {
        nid: info for nid, info in nodes.items() if _nid_ns_index(nid) == my_ns_index
    }

    # Build lightweight wrapper objects for every node in our namespace
    ns_nodes: dict[str, Any] = {
        nid: _make_ns_node(info) for nid, info in my_nodes.items()
    }

    # Find each node's parent via its first backward hierarchical reference
    parents: dict[str, str | None] = {}
    for nid, info in my_nodes.items():
        parent = None
        for rt, target, is_fwd in info.refs:
            if rt in _HIERARCHICAL_REFS and not is_fwd:
                parent = target
                break
        parents[nid] = parent

    # Classify ObjectTypeNodes into eventtypes / ifacetypes / objtypes
    # by walking the HasSubtype reference chain up to the root seeds.
    event_ids: set[str] = {_EVENT_TYPE_ROOT}
    iface_ids: set[str] = {_IFACE_TYPE_ROOT}
    objtype_nids = [nid for nid, info in my_nodes.items() if info.kind == "objecttype"]

    changed = True
    while changed:
        changed = False
        for nid in objtype_nids:
            if nid in event_ids or nid in iface_ids:
                continue
            for rt, target, is_fwd in my_nodes[nid].refs:
                if rt == _HAS_SUBTYPE and not is_fwd:
                    if target in event_ids:
                        event_ids.add(nid)
                        changed = True
                    elif target in iface_ids:
                        iface_ids.add(nid)
                        changed = True
                    break

    # Name-based fallback for types not yet classified via subtype traversal
    for nid in objtype_nids:
        if nid in event_ids or nid in iface_ids:
            continue
        name = my_nodes[nid].browse_name
        if "EventType" in name:
            event_ids.add(nid)
        elif "InterfaceType" in name:
            iface_ids.add(nid)

    # Assign each node to its container, nesting children under parents
    for nid, info in my_nodes.items():
        ns_node = ns_nodes[nid]
        container = _pick_container(descriptor, info.kind, nid, event_ids, iface_ids)
        parent_nid = parents[nid]
        if parent_nid and parent_nid in ns_nodes:
            setattr(ns_nodes[parent_nid], info.browse_name, ns_node)
        else:
            setattr(container, info.browse_name, ns_node)
