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

"""Python source expressions for OPC UA DataTypes."""

from __future__ import annotations

from collections.abc import Callable, Iterable
from dataclasses import dataclass
import keyword
import re
from typing import Any
from xml.etree import ElementTree

from .frontend import LoadedNodeSet

_BUILTIN_DATATYPE_NAMES = {
    1: "Boolean",
    2: "SByte",
    3: "Byte",
    4: "Int16",
    5: "UInt16",
    6: "Int32",
    7: "UInt32",
    8: "Int64",
    9: "UInt64",
    10: "Float",
    11: "Double",
    12: "String",
    13: "DateTime",
    14: "Guid",
    15: "ByteString",
    16: "XmlElement",
    17: "NodeId",
    18: "ExpandedNodeId",
    19: "StatusCode",
    20: "QualifiedName",
    21: "LocalizedText",
    22: "ExtensionObject",
    23: "DataValue",
    24: "Variant",
    25: "DiagnosticInfo",
}

ASCII_SHORTNAMES = {
    " ": "space",
    "!": "bang",
    '"': "quote",
    "#": "hash",
    "$": "dollar",
    "%": "pct",
    "&": "amp",
    "'": "squote",
    "(": "lparen",
    ")": "rparen",
    "*": "star",
    "+": "plus",
    ",": "comma",
    "-": "minus",
    ".": "dot",
    "/": "slash",
    ":": "colon",
    ";": "semi",
    "<": "langle",
    "=": "eq",
    ">": "rangle",
    "?": "qmark",
    "@": "at",
    "[": "lbrack",
    "\\": "bslash",
    "]": "rbrack",
    "^": "caret",
    "`": "backtick",
    "{": "lbrace",
    "|": "pipe",
    "}": "rbrace",
    "~": "tilde",
}

_LEADING_DIGIT_NAMES = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
}


def _underscore_identifier(name: str) -> str:
    value = re.sub(r"\W", "_", name)
    if not value:
        value = "_"
    elif value[0].isdigit():
        value = f"_{value}"
    if keyword.iskeyword(value):
        value += "_"
    return value


def identifier(name: str) -> str:
    """Return the class-level Python spelling of an OPC UA name.

    A leading digit is spelled out (``3DVector`` becomes ``ThreeDVector``), which
    matches both the OPC UA type dictionary and open62541's ``UA_ThreeDVector``.
    Prefixing ``_`` instead would hide the class from ``import *`` and make the
    backend treat the symbol as private, degrading cross-references to NodeId
    lookups. Digits elsewhere are retained.
    """
    if name[:1] in _LEADING_DIGIT_NAMES:
        word = _LEADING_DIGIT_NAMES[name[0]].capitalize()
        rest = name[1:]
        name = word + (rest[:1].upper() + rest[1:] if rest else "")
    return _underscore_identifier(name)


def member_identifier(name: str) -> str:
    parts: list[str] = []
    capitalize_next = False
    for char in name:
        if not parts and char in _LEADING_DIGIT_NAMES:
            parts.append(_LEADING_DIGIT_NAMES[char])
            capitalize_next = True
            continue

        if not char.isprintable():
            parts.append("_")
            capitalize_next = False
            continue

        shortname = ASCII_SHORTNAMES.get(char)
        if shortname is not None:
            parts.append(shortname if not parts else shortname[:1].upper() + shortname[1:])
            capitalize_next = True
            continue

        valid = char.isidentifier() if not parts else f"a{char}".isidentifier()
        if valid:
            parts.append(char.upper() if capitalize_next else char)
            capitalize_next = False
        else:
            parts.append("_")
            capitalize_next = False

    value = "".join(parts) or "_"
    value = value[:1].lower() + value[1:]
    return value + "_" if keyword.iskeyword(value) else value


def attribute_identifier(name: str) -> str:
    """Return the public attribute spelling of a BrowseName."""
    return member_identifier(name)


def enum_member(name: str) -> str:
    # Keeps the ``_``-prefix spelling for a digit-leading field. Spelling only the
    # leading digit would turn ``16BIT`` into ``ONE6_BIT``; a correct rule has to
    # spell the whole leading number, which is not implemented yet.
    value = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", name)
    value = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", value).upper()
    return _underscore_identifier(value)


# The ns0 identifiers of the unsigned integers an OPC UA OptionSet may subtype —
# Byte, UInt16, UInt32, UInt64, exactly what ``base=`` accepts.  The parent is
# recognised by its NodeId rather than resolved through ``names``, which finds
# ``Byte`` for an ns0-local OptionSet but nothing for a non-ns0 one; that is why
# option sets used to be generated base-less.  ``LengthInBits`` is not an
# alternative — it is a ``.bsd`` attribute, absent from the NodeSet2 corpus.
_OPTION_SET_BASE_IDS = frozenset({3, 5, 7, 9})


def _option_set_lines(
    name: str, common: list[str], elements: dict[str, int], parent: Any | None
) -> list[str]:
    """Render the integer form of an OPC UA OptionSet.

    An OptionSet is a bit field, not an enumeration: each member carries the
    *mask* of its bit, written as ``0x01 << n`` so the NodeSet's literal ``Value``
    stays readable as the shift count.  ``base`` is the unsigned integer the
    DataType subtypes and is mandatory — it carries the wire width and the
    ``HasSubtype`` parent, and it is spelled as a keyword because the inheritance
    form cannot be made real (a numpy scalar carries no o6 declaration).
    """
    base = None
    if (
        parent is not None
        and int(parent.id.ns) == 0
        and int(getattr(parent.id, "i", -1)) in _OPTION_SET_BASE_IDS
    ):
        base = f"o6.{parent.browseName.name}"
    if base is None:
        named = "no HasSubtype parent" if parent is None else f"{parent.id}"
        raise ValueError(
            f"OptionSet {name!r} subtypes {named}, which is none of the unsigned "
            "integers an OptionSet may subtype (ns0 i=3, i=5, i=7, i=9).  The base "
            "carries the OptionSet's wire width, so it cannot be omitted."
        )
    lines = [f"@o6.optionsettype({', '.join([*common, f'base={base}'])})", f"class {name}:"]
    if not elements:
        raise ValueError(
            f"OptionSet {name!r} declares no bits.  An OptionSet with no members "
            "has no bit field to generate."
        )
    used_members: set[str] = set()
    for field, value in sorted(elements.items(), key=lambda item: (int(item[1]), item[0])):
        member = _unique_identifier(enum_member(field), used_members)
        lines.append(f"    {member} = o6.bitmask(0x01 << {int(value)}, name={field!r})")
    return lines


def _unique_identifier(base: str, used: set[str]) -> str:
    candidate = base
    suffix = 2
    while candidate in used:
        candidate = f"{base}_{suffix}"
        suffix += 1
    used.add(candidate)
    return candidate


def python_names(
    nodes: Iterable[Any],
    nodes_module: Any,
    *,
    key: Callable[[Any], Any] | None = None,
) -> dict[str, str]:
    nodes = tuple(nodes)
    local_ids = {str(node.id) for node in nodes}
    names: dict[str, str] = {}
    used: set[str] = set()

    def is_owned_instance(node: Any) -> bool:
        if any(
            not reference.isForward and str(reference.referenceType).split(";", 1)[-1] == "i=38"
            for reference in getattr(node, "references", ())
        ):
            return True
        parent = getattr(node, "parent", None)
        if parent is None or str(parent.id) not in local_ids:
            return False
        seen: set[str] = set()
        current = parent
        while current is not None and str(current.id) not in seen:
            if isinstance(
                current,
                (
                    nodes_module.ObjectTypeNode,
                    nodes_module.VariableTypeNode,
                    nodes_module.DataTypeNode,
                    nodes_module.MethodNode,
                ),
            ):
                return True
            seen.add(str(current.id))
            current = getattr(current, "parent", None)
        reference_type = getattr(getattr(node, "parentReference", None), "id", None)
        return str(reference_type).split(";", 1)[-1] != "i=35"

    for node in sorted(nodes, key=key) if key is not None else nodes:
        base = identifier(node.browseName.name)
        is_variable = isinstance(node, nodes_module.VariableNode) and not isinstance(
            node, nodes_module.VariableTypeNode
        )
        is_object = isinstance(node, nodes_module.ObjectNode) and not isinstance(
            node, nodes_module.ObjectTypeNode
        )
        is_instance = (
            is_variable
            or is_object
            or isinstance(node, (nodes_module.MethodNode, nodes_module.ViewNode))
        )
        if is_instance:
            if is_owned_instance(node):
                base = "__" + member_identifier(node.browseName.name)
            else:
                base = member_identifier(node.browseName.name)
        names[str(node.id)] = _unique_identifier(base, used)
    return names


class UnsupportedDataTypeError(RuntimeError):
    pass


@dataclass(frozen=True)
class ResolvedDataType:
    expression: str
    python_type: type[Any] | None


@dataclass
class BuiltinType:
    name: str
    namespaceUri: str = "http://opcfoundation.org/UA/"


@dataclass
class TypeReference:
    name: str
    namespaceUri: str


@dataclass
class StructMember:
    name: str
    member_type: BuiltinType | TypeReference
    is_array: bool
    is_optional: bool


@dataclass
class StructType:
    name: str
    namespaceUri: str
    members: list[StructMember]
    is_union: bool = False
    # (bit name, bit position) for a structure-form OptionSet, in declaration
    # order.  Empty for every other structure.  These are the bits the NodeSet
    # ``Definition`` declares over the ``Value``/``ValidBits`` pair, and they are
    # the only reason the pair is readable by name in Python.
    option_set_bits: tuple[tuple[str, int], ...] = ()


@dataclass
class EnumerationType:
    name: str
    namespaceUri: str
    elements: dict[str, int]
    isOptionSet: bool = False


def localized_nodeid(nodeid: Any, target_index: int, shortname: str) -> str:
    text = str(nodeid)
    if ";" not in text or text.startswith("ns=0;"):
        return text.removeprefix("ns=0;")
    if text.startswith(f"ns={target_index};"):
        return f"ns={shortname};{text.split(';', 1)[1]}"
    return text


def _default_binary_encoding(loaded: LoadedNodeSet, node: Any) -> Any | None:
    encodings = [
        reference
        for reference in node.references
        if reference.isForward and str(reference.referenceType) in {"i=38", "ns=0;i=38"}
    ]
    for reference in encodings:
        target_node = loaded.nodeset.nodes.get(reference.target)
        if target_node and target_node.browseName.name == "Default Binary":
            return reference.target
    return encodings[0].target if encodings else None


def _datatype_infos(loaded: LoadedNodeSet) -> dict[tuple[str, str], Any]:
    cached = getattr(loaded.nodeset, "_o6_datatype_infos", None)
    if cached is not None:
        return cached
    infos: dict[tuple[str, str], Any] = {}
    documents: list[tuple[ElementTree.Element, dict[str, str], tuple[str, ...]]] = []

    def graph_node(value: str, aliases: dict[str, str], xml_uris: tuple[str, ...]) -> Any | None:
        value = aliases.get(value, value)
        match = re.fullmatch(r"(?:ns=(\d+);)?(.+)", value)
        if match is None:
            return None
        local_index = int(match.group(1) or 0)
        graph_index = loaded.namespace_uris.index(xml_uris[local_index])
        nodeid = (
            f"ns=0;{match.group(2)}" if graph_index == 0 else f"ns={graph_index};{match.group(2)}"
        )
        endpoint = loaded.endpoints.get(nodeid)
        return endpoint.node if endpoint is not None else None

    for path in loaded.datatype_source_paths:
        root = ElementTree.parse(path).getroot()
        aliases = {
            alias.get("Alias", ""): (alias.text or "").strip()
            for alias in root.findall("{*}Aliases/{*}Alias")
        }
        xml_uris = (
            "http://opcfoundation.org/UA/",
            *(element.text or "" for element in root.findall("{*}NamespaceUris/{*}Uri")),
        )
        documents.append((root, aliases, xml_uris))

    defined_nodeids = {
        str(node.id)
        for root, aliases, xml_uris in documents
        for element in root.findall("{*}UADataType")
        if element.find("{*}Definition") is not None
        and (node := graph_node(element.get("NodeId", ""), aliases, xml_uris)) is not None
    }

    def member_type(datatype: Any) -> BuiltinType | TypeReference:
        current = datatype
        while current is not None:
            if (
                int(current.id.ns) == 0
                and current.id.i is not None
                and 1 <= int(current.id.i) <= 25
            ):
                return BuiltinType(current.browseName.name)
            if str(current.id) in defined_nodeids:
                return TypeReference(
                    current.browseName.name,
                    loaded.namespace_uris[int(current.id.ns)],
                )
            current = datatype_parent(loaded, current)
        return TypeReference(
            datatype.browseName.name,
            loaded.namespace_uris[int(datatype.id.ns)],
        )

    for root, aliases, xml_uris in documents:
        for element in root.findall("{*}UADataType"):
            definition = element.find("{*}Definition")
            nodeid = element.get("NodeId")
            node = graph_node(nodeid, aliases, xml_uris) if nodeid else None
            if definition is None or node is None:
                continue
            uri = loaded.namespace_uris[int(node.id.ns)]
            name = node.browseName.name
            fields = definition.findall("{*}Field")
            is_option_set = definition.get("IsOptionSet", "false").lower() == "true"
            parent = datatype_parent(loaded, node)
            is_struct_option_set = parent is not None and str(parent.id) in {
                "i=12755",
                "ns=0;i=12755",
            }
            if (
                fields
                and not is_struct_option_set
                and all(field.get("Value") is not None for field in fields)
            ):
                infos[uri, name] = EnumerationType(
                    name,
                    uri,
                    {field.get("Name", ""): int(field.get("Value", "0")) for field in fields},
                    is_option_set,
                )
                continue
            members: list[StructMember] = (
                [
                    StructMember("value", BuiltinType("ByteString"), False, False),
                    StructMember("validBits", BuiltinType("ByteString"), False, False),
                ]
                if is_struct_option_set
                else []
            )
            for field in () if is_struct_option_set else fields:
                field_name = field.get("Name", "")
                datatype_name = field.get("DataType")
                datatype = graph_node(datatype_name, aliases, xml_uris) if datatype_name else None
                members.append(
                    StructMember(
                        field_name[:1].lower() + field_name[1:],
                        # NodeSet2 omits DataType for Variant fields.
                        member_type(datatype) if datatype is not None else BuiltinType("Variant"),
                        field.get("ValueRank") is not None
                        and int(field.get("ValueRank", "-1")) != -1,
                        field.get("IsOptional", "false").lower() == "true",
                    )
                )
            infos[uri, name] = StructType(
                name,
                uri,
                members,
                definition.get("IsUnion", "false").lower() == "true",
                option_set_bits=(
                    tuple(
                        (field.get("Name", ""), int(field.get("Value", "0"))) for field in fields
                    )
                    if is_struct_option_set
                    else ()
                ),
            )
    loaded.nodeset._o6_datatype_infos = infos
    return infos


def _datatype_info(loaded: LoadedNodeSet, uri: str, name: str) -> Any | None:
    return _datatype_infos(loaded).get((uri, name))


def datatype_parent(loaded: LoadedNodeSet, node: Any) -> Any | None:
    for reference in node.references:
        if not reference.isForward and str(reference.referenceType) in {"i=45", "ns=0;i=45"}:
            return loaded.nodeset.nodes.get(reference.target)
    return None


def datatype_members(loaded: LoadedNodeSet, node: Any) -> tuple[Any, ...]:
    """Return the complete inherited structure field list for ``node``."""
    lineage: list[Any] = []
    current = node
    while current is not None:
        lineage.append(current)
        current = datatype_parent(loaded, current)

    members: list[Any] = []
    positions: dict[str, int] = {}
    for current in reversed(lineage):
        info = _datatype_info(
            loaded,
            loaded.namespace_uris[int(current.id.ns)],
            current.browseName.name,
        )
        for member in getattr(info, "members", ()):
            position = positions.get(member.name)
            if position is None:
                positions[member.name] = len(members)
                members.append(member)
            else:
                members[position] = member
    return tuple(members)


def datatype_node(loaded: LoadedNodeSet, reference: Any) -> Any | None:
    """Resolve a DataType reference by NodeId, then by unique BrowseName."""
    node = loaded.nodeset.nodes.get(reference)
    if node is not None:
        return node
    text = str(reference)
    canonical = text.removeprefix("ns=0;")
    node = next(
        (
            candidate
            for candidate in loaded.nodes
            if type(candidate).__name__ == "DataTypeNode"
            and str(candidate.id).removeprefix("ns=0;") == canonical
        ),
        None,
    )
    if node is not None:
        return node
    if not isinstance(reference, str):
        return None
    name = reference.rsplit(":", 1)[-1]
    matches = [
        candidate
        for candidate in loaded.nodes
        if type(candidate).__name__ == "DataTypeNode" and candidate.browseName.name == name
    ]
    if len(matches) > 1:
        raise UnsupportedDataTypeError(
            f"ambiguous DataType BrowseName {reference!r}: "
            + ", ".join(str(candidate.id) for candidate in matches)
        )
    return matches[0] if matches else None


def datatype_dependencies(loaded: LoadedNodeSet, node: Any) -> tuple[Any, ...]:
    info = _datatype_info(
        loaded,
        loaded.namespace_uris[int(node.id.ns)],
        node.browseName.name,
    )
    required = {
        (member.member_type.namespaceUri, member.member_type.name)
        for member in getattr(info, "members", ())
    }
    if not required:
        return ()
    return tuple(
        candidate.id
        for candidate in loaded.generated_nodes
        if type(candidate).__name__ == "DataTypeNode"
        and (
            loaded.namespace_uris[int(candidate.id.ns)],
            candidate.browseName.name,
        )
        in required
    )


def _datatype_annotation(member_type: Any, target_uri: str, local_names: set[str]) -> str:
    name = identifier(member_type.name)
    uri = member_type.namespaceUri
    if uri == target_uri and name in local_names:
        return name
    if uri == "http://opcfoundation.org/UA/":
        if name == "Variant":
            return "Any"
        if name in {"BaseDataType", "Structure"}:
            return "o6.ExtensionObject"
        return (
            f"o6.{name}" if type(member_type).__name__ == "BuiltinType" else f"ns0.datatypes.{name}"
        )
    raise UnsupportedDataTypeError(
        f"datatype member {member_type.name} belongs to undeclared namespace {uri}"
    )


def datatype_lines(
    loaded: LoadedNodeSet,
    node: Any,
    *,
    target_index: int,
    target_uri: str,
    shortname: str,
    names: dict[str, str],
    local_names: set[str],
    type_symbols: dict[tuple[str, str], str] | None = None,
    base_symbols: dict[tuple[str, str], str] | None = None,
    nodeid_resolver: Callable[[Any], str] | None = None,
) -> list[str]:
    name = names[str(node.id)]
    identifier_value = getattr(node.id, "i", None)
    if target_index == 0 and identifier_value in {*range(1, 22), 23, 25}:
        return [f"{name} = o6.{name}"]
    info = _datatype_info(loaded, target_uri, node.browseName.name)
    resolve_nodeid = nodeid_resolver or (
        lambda value: localized_nodeid(value, target_index, shortname)
    )
    nodeid = resolve_nodeid(node.id)
    common = [f"nodeId={nodeid!r}", f"browseName={node.browseName.name!r}"]
    description = getattr(node, "resolvedDescription", None)
    if description:
        common.append(f"description={description!r}")
    encoding = _default_binary_encoding(loaded, node)
    if encoding is not None:
        common.append(f"defaultEncodingId={resolve_nodeid(encoding)!r}")
    if bool(getattr(node, "isAbstract", False)):
        common.append("isAbstract=True")

    parent = datatype_parent(loaded, node)
    if info is None:
        if parent is not None:
            common.append(f"parent={resolve_nodeid(parent.id)!r}")
        body = (
            "    def __init__(self, *args: object, **kwargs: object) -> None: ..."
            if target_index == 0 and name == "Structure"
            else "    pass"
        )
        return [f"@o6.datatype({', '.join(common)})", f"class {name}:", body]

    if type(info).__name__ == "EnumerationType":
        common = [argument for argument in common if not argument.startswith("defaultEncodingId=")]
        elements = getattr(info, "elements", {})
        if bool(getattr(info, "isOptionSet", False)):
            return _option_set_lines(name, common, elements, parent)
        lines = [f"@o6.enumtype({', '.join(common)})"]
        parent_name = names.get(str(parent.id)) if parent is not None else None
        if parent is not None and parent_name is None:
            parent_name = (base_symbols if base_symbols is not None else type_symbols or {}).get(
                (
                    loaded.namespace_uris[int(parent.id.ns)],
                    parent.browseName.name,
                )
            )
        base = parent_name or ("" if target_index == 0 else "ns0.datatypes.Enumeration")
        lines.append(f"class {name}({base}):" if base else f"class {name}:")
        if not elements:
            lines.append("    pass")
        else:
            used_members: set[str] = set()
            for field, value in sorted(elements.items(), key=lambda item: (int(item[1]), item[0])):
                member = _unique_identifier(enum_member(field), used_members)
                lines.append(f"    {member} = o6.enumfield({int(value)}, name={field!r})")
        return lines

    parent_name = names.get(str(parent.id)) if parent is not None else None
    if parent is not None and parent_name is None:
        parent_name = (base_symbols if base_symbols is not None else type_symbols or {}).get(
            (
                loaded.namespace_uris[int(parent.id.ns)],
                parent.browseName.name,
            )
        )
    if parent is not None and parent_name is None and int(parent.id.ns) == 0:
        parent_name = (
            f"o6.{parent.browseName.name}"
            if 1 <= int(parent.id.i) <= 25 and int(parent.id.i) not in {22, 24}
            else f"ns0.datatypes.{parent.browseName.name}"
        )
    parent_name = parent_name or ("" if target_index == 0 else "ns0.datatypes.Structure")
    declaration = f"class {name}({parent_name}):" if parent_name else f"class {name}:"
    lines = [f"@o6.datatype({', '.join(common)})", declaration]
    if target_index == 0 and name == "EventFilter":
        lines.extend(
            [
                "    @classmethod",
                "    def parse(cls, query: str, logger: object | None = None) -> EventFilter: ...",
            ]
        )
    members = datatype_members(loaded, node)
    if not members:
        if (
            info is not None
            and type(info).__name__ == "StructType"
            and not bool(getattr(node, "isAbstract", False))
            and parent is None
        ):
            lines.append("    _placeholder: o6.NodeId = o6.field()")
        else:
            lines.append("    pass")
    used_members: set[str] = set()
    for member in members:
        annotation = (
            _datatype_annotation(member.member_type, target_uri, local_names)
            if type(member.member_type).__name__ == "BuiltinType"
            else (type_symbols or {}).get(
                (member.member_type.namespaceUri, member.member_type.name)
            )
            or _datatype_annotation(member.member_type, target_uri, local_names)
        )
        if member.is_array:
            annotation = f"list[{annotation}]"
        if member.is_optional:
            annotation = f"{annotation} | None"
        field_args: list[str] = []
        dimensions = getattr(node, "fieldArrayDimensions", {}).get(member.name.casefold())
        if dimensions is not None:
            field_args.append(f"arrayDimensions={dimensions!r}")
        field = f" = o6.field({', '.join(field_args)})" if field_args else ""
        name = _unique_identifier(identifier(member.name), used_members)
        lines.append(f"    {name}: {annotation}{field}")
    # A structure-form OptionSet keeps its ``Value``/``ValidBits`` members and
    # gains one accessor per declared bit.  ``used_members`` already holds the
    # member names, so a bit spelled like one of them is uniqued rather than
    # shadowing it.
    for bit, position in getattr(info, "option_set_bits", ()):
        accessor = _unique_identifier(member_identifier(bit), used_members)
        lines.append(f"    {accessor} = o6.optionsetbit({int(position)}, name={bit!r})")
    return lines


def resolve_datatype(
    loaded: LoadedNodeSet,
    datatype_id: Any,
    *,
    target_index: int,
    names: dict[str, str],
    compiler_types: dict[str, type[Any]] | None = None,
) -> ResolvedDataType:
    """Resolve one DataType once for both source generation and value decoding."""
    text = str(datatype_id).removeprefix("ns=0;")
    if text.startswith("i="):
        identifier_value = int(text[2:])
        builtin = _BUILTIN_DATATYPE_NAMES.get(identifier_value)
        if builtin is not None:
            if identifier_value in {22, 24}:
                return ResolvedDataType(f"o6.NodeId('i={identifier_value}')", None)
            import o6

            python_type = getattr(o6, builtin)
            return ResolvedDataType(f"o6.{builtin}", python_type)
    datatype = datatype_node(loaded, datatype_id)
    if datatype is None:
        raise UnsupportedDataTypeError(f"unknown DataType {datatype_id}")
    identifier_value = getattr(datatype.id, "i", None)
    if int(datatype.id.ns) == 0 and identifier_value in range(1, 26):
        if identifier_value in {22, 24}:
            return ResolvedDataType(
                f"o6.NodeId('i={identifier_value}')",
                None,
            )
        name = identifier(datatype.browseName.name)
        import o6

        return ResolvedDataType(f"o6.{name}", getattr(o6, name))
    local_name = names.get(str(datatype.id))
    if local_name is not None:
        return ResolvedDataType(
            local_name,
            (compiler_types or {}).get(str(datatype.id)),
        )
    if datatype.hidden and int(datatype.id.ns) != 0:
        uri = loaded.namespace_uris[int(datatype.id.ns)]
        binding = next(binding for binding in loaded.namespace_bindings if binding.uri == uri)
        name = identifier(datatype.browseName.name)
        module = __import__(binding.module, fromlist=[name])
        return ResolvedDataType(f"{binding.shortname}.{name}", getattr(module, name))
    current = datatype
    while current is not None:
        name = identifier(current.browseName.name)
        current_local = names.get(str(current.id))
        if current_local is not None:
            return ResolvedDataType(
                current_local,
                (compiler_types or {}).get(str(current.id)),
            )
        if int(current.id.ns) != 0:
            current = datatype_parent(loaded, current)
            continue
        current_identifier = getattr(current.id, "i", None)
        if current_identifier in {22, 24}:
            return ResolvedDataType(
                f"o6.NodeId('i={current_identifier}')",
                None,
            )
        if current_identifier in range(1, 26):
            import o6

            return ResolvedDataType(f"o6.{name}", getattr(o6, name))
        info = _datatype_info(
            loaded,
            loaded.namespace_uris[int(current.id.ns)],
            current.browseName.name,
        )
        if current.hidden and (
            current_identifier in {26, 27, 28, 29, 30, 12756}
            or type(info).__name__ in {"EnumerationType", "StructType"}
        ):
            return ResolvedDataType(f"ns0.datatypes.{name}", None)
        current = current.parent
    raise UnsupportedDataTypeError(
        f"DataType {datatype.browseName} ({datatype.id}) has no generated Python datatype"
    )


def datatype_assignment_expression(
    loaded: LoadedNodeSet,
    datatype_id: Any,
    *,
    target_index: int,
    shortname: str,
    names: dict[str, str],
    compiler_types: dict[str, type[Any]] | None = None,
) -> str:
    """Resolve a datatype without losing aliases sharing one Python type."""
    datatype = datatype_node(loaded, datatype_id)
    if datatype is not None:
        index = int(datatype.id.ns)
        name = identifier(datatype.browseName.name)
        identifier_value = getattr(datatype.id, "i", None)
        if index == 0 and identifier_value in {*range(1, 22), 23, 25}:
            return f"o6.{name}"
        symbol = names.get(str(datatype.id))
        if symbol is None and index != target_index:
            binding = next(
                binding
                for binding in loaded.namespace_bindings
                if binding.uri == loaded.namespace_uris[index]
            )
            symbol = f"{binding.shortname}.{name}"
        symbol = symbol or name
        return symbol.rsplit(".", 1)[-1] if index == target_index else symbol
    resolved = resolve_datatype(
        loaded,
        datatype_id,
        target_index=target_index,
        names=names,
        compiler_types=compiler_types,
    )
    return resolved.expression
