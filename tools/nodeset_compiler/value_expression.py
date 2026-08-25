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

"""Render decoded OPC UA values as typed Python expressions.

This module deliberately knows nothing about NodeSet XML. Values have already
been decoded by open62541 before they reach this layer.
"""

from __future__ import annotations

import enum
import base64
from collections.abc import Iterable
from dataclasses import dataclass, field
import math
import numpy as np
import re
import types
from typing import Any, Callable, Mapping
import uuid
from xml.etree import ElementTree

from .frontend import LoadedNodeSet
from .datatype_expression import (
    _BUILTIN_DATATYPE_NAMES,
    _datatype_infos,
    _datatype_info,
    datatype_assignment_expression,
    datatype_lines,
    datatype_node,
    datatype_parent,
    identifier,
    python_names,
    resolve_datatype,
    UnsupportedDataTypeError,
)


class UnsupportedValueError(TypeError):
    pass


TypeExpression = Callable[[type[Any]], str]
NodeIdExpression = Callable[[Any], str]


def _type_spec(py_type: type[Any]) -> Any:
    declaration = getattr(py_type, "__o6_declaration__", None)
    return getattr(declaration, "attributes", None)


def _structure_fields(py_type: type[Any]) -> tuple[Any, ...]:
    """Return inherited and local structure fields once, in storage order."""
    fields: list[Any] = []
    positions: dict[str, int] = {}
    for base in reversed(py_type.__mro__):
        attributes = _type_spec(base)
        description = getattr(attributes, "structure_description", None)
        definition = getattr(description, "structureDefinition", None)
        for field in getattr(definition, "fields", ()):
            position = positions.get(field.name)
            if position is None:
                positions[field.name] = len(fields)
                fields.append(field)
            else:
                fields[position] = field
    return tuple(fields)


def _decode_nodeset_xml_value(
    xml: bytes | str,
    datatype: type[Any],
    namespaces: tuple[str | int, ...],
    datatype_types: Mapping[str, type[Any]] | None = None,
) -> Any:
    """Decode the NodeSet-specific ``<Value>`` envelope.

    The general o6 XML codec handles ordinary typed XML. NodeSet values add a
    Variant envelope and XML-local namespace indexes. OptionSet values stay
    here as well because open62541's generic Variant decoder cannot decode
    their standard ExtensionObject body safely.
    """
    payload = xml.encode() if isinstance(xml, str) else bytes(xml)
    if b"<OptionSet" in payload or b":OptionSet" in payload:
        option_set = ElementTree.fromstring(payload).find(".//{*}Body/{*}OptionSet")
        if option_set is not None:

            def field(name: str) -> bytes:
                element = option_set.find(f"{{*}}{name}")
                return base64.b64decode("" if element is None else element.text or "")

            return datatype(value=field("Value"), validBits=field("ValidBits"))

    import o6
    from o6._o6 import types as native_types

    namespace_indexes: list[int] = []
    for namespace in namespaces:
        if isinstance(namespace, int):
            namespace_indexes.append(namespace)
            continue
        matches = o6.ns.filter(uri=namespace)
        if not matches:
            raise KeyError(f"namespace URI is not registered: {namespace}")
        namespace_indexes.append(matches[0].index)

    def remap_nodeid(value: o6.NodeId) -> o6.NodeId:
        namespace = value.ns
        local_index = namespace if isinstance(namespace, int) else namespace.index
        if local_index == 0:
            return value
        if local_index >= len(namespace_indexes):
            raise ValueError(f"NodeSet value uses unknown namespace index {local_index}")
        _, separator, identifier = str(value).partition(";")
        if not separator:
            return value
        return o6.NodeId(f"ns={namespace_indexes[local_index]};{identifier}")

    root = ElementTree.fromstring(payload)
    body = root.find(".//{*}Body")
    body_value = next(iter(body), None) if body is not None else None

    def decode_typed(element: ElementTree.Element, py_type: type[Any]) -> Any:
        attributes = _type_spec(py_type)
        enum_description = getattr(attributes, "enum_description", None)
        if enum_description is not None:
            text = (element.text or "").strip()
            symbolic = re.sub(r"_\d+$", "", text)
            for enum_field in enum_description.enumDefinition.fields:
                if symbolic in {enum_field.name, enum_field.displayName.text}:
                    return py_type(enum_field.value)
            return py_type(int(text))

        structure_description = getattr(attributes, "structure_description", None)
        if structure_description is None:
            if not list(element) and element.text is not None and not element.text.strip():
                element.text = ""
            decoded = o6.decodeXml(ElementTree.tostring(element), py_type)
            return remap_nodeid(decoded) if py_type is o6.NodeId else decoded

        values: dict[str, Any] = {}
        elements = {child.tag.rsplit("}", 1)[-1].casefold(): child for child in element}
        for structure_field in _structure_fields(py_type):
            child = elements.get(structure_field.name.casefold())
            if child is None:
                continue
            field_nodeid = o6.NodeId(structure_field.dataType)
            builtin_name = (
                _BUILTIN_DATATYPE_NAMES.get(field_nodeid.id)
                if field_nodeid.ns.index == 0 and isinstance(field_nodeid.id, int)
                else None
            )
            if builtin_name == "Variant":
                contents = b"".join(ElementTree.tostring(item) for item in list(child))
                if not contents and not (child.text or "").strip():
                    values[structure_field.name] = [] if structure_field.valueRank >= 0 else None
                    continue
                try:
                    values[structure_field.name] = native_types._decodeXmlValue(
                        b"<Variant><Value>" + contents + b"</Value></Variant>",
                        o6.ExtensionObject,
                        namespaces,
                    )
                except Exception as exc:
                    exc.add_note(
                        f"while decoding Variant field {py_type.__name__}.{structure_field.name}: "
                        f"{ElementTree.tostring(child)!r}"
                    )
                    raise
                continue
            field_type = getattr(o6, builtin_name) if builtin_name is not None else None
            if field_type is None and datatype_types is not None:
                field_type = datatype_types.get(str(field_nodeid))
            if field_type is None:
                field_type = o6.ns[str(field_nodeid)]
            try:
                if structure_field.valueRank >= 0:
                    items = list(child)
                    if not items and child.text and child.text.strip():
                        items = [child]
                    values[structure_field.name] = [
                        decode_typed(item, field_type) for item in items
                    ]
                else:
                    values[structure_field.name] = decode_typed(child, field_type)
            except Exception as exc:
                exc.add_note(
                    f"while decoding {py_type.__name__}.{structure_field.name} as {field_type.__name__}"
                )
                raise
        try:
            return py_type(**values)
        except Exception as exc:
            exc.add_note(f"while constructing {py_type.__name__} with fields {tuple(values)}")
            raise

    declared = datatype
    structure_description = getattr(_type_spec(declared), "structure_description", None)
    list_of_extension_objects = root.find(".//{*}ListOfExtensionObject")
    if structure_description is not None and list_of_extension_objects is not None:
        values = []
        for extension_object in list_of_extension_objects.findall("{*}ExtensionObject"):
            item_body = extension_object.find("{*}Body")
            item_value = next(iter(item_body), None) if item_body is not None else None
            if item_value is not None:
                values.append(decode_typed(item_value, declared))
        return values

    if body_value is not None and structure_description is not None:
        return decode_typed(body_value, declared)

    return native_types._decodeXmlValue(
        b"<Variant>" + payload + b"</Variant>", datatype, namespace_indexes
    )


@dataclass(frozen=True)
class ValueExpressionContext:
    loaded: LoadedNodeSet
    target_index: int
    shortname: str
    compiler_types: dict[str, type[Any]]
    compiler_symbols: dict[str, str]
    runtime_modules: dict[str, str] = field(default_factory=dict)


def prepare_value_context(
    loaded: LoadedNodeSet,
    *,
    target_index: int,
    shortname: str,
    symbols: dict[str, str] | None = None,
    type_symbols: dict[tuple[str, str], str] | None = None,
) -> ValueExpressionContext:
    """Build the compiler-local o6 datatype universe used to decode values."""

    nodes_module = __import__(
        f"{type(loaded.nodeset).__module__.rsplit('.', 1)[0]}.nodes",
        fromlist=["nodes"],
    )
    if not any(
        isinstance(node, nodes_module.VariableNode) and node.value is not None
        for node in loaded.generated_nodes
    ):
        return ValueExpressionContext(loaded, target_index, shortname, {}, {})
    import o6

    runtime_modules = {
        binding.shortname: binding.module
        for binding in loaded.namespace_bindings
        if not binding.target
    }
    datatype_nodes = tuple(
        node for node in loaded.generated_nodes if isinstance(node, nodes_module.DataTypeNode)
    )
    if target_index == 0:
        ns0 = __import__("o6.ns", fromlist=["ns0"]).ns0
        compiler_types: dict[str, type[Any]] = {}
        compiler_symbols: dict[str, str] = dict(symbols or {})
        names = python_names(datatype_nodes, nodes_module)

        def python_type(node: Any) -> type[Any] | None:
            cached = compiler_types.get(str(node.id))
            if cached is not None:
                return cached
            name = names[str(node.id)]
            candidate = getattr(o6, name, None)
            if not isinstance(candidate, type):
                namespace_type = getattr(ns0.datatypes, name, None)
                attributes = _type_spec(namespace_type)
                if (
                    getattr(attributes, "structure_description", None) is not None
                    or getattr(attributes, "enum_description", None) is not None
                ):
                    candidate = namespace_type
            if not isinstance(candidate, type):
                parent = datatype_parent(loaded, node)
                candidate = python_type(parent) if parent is not None else None
            if isinstance(candidate, type):
                compiler_types[str(node.id)] = candidate
                return candidate
            return None

        for node in datatype_nodes:
            name = names[str(node.id)]
            compiler_symbols[str(node.id)] = name
            py_type = python_type(node)
        return ValueExpressionContext(
            loaded,
            target_index,
            shortname,
            compiler_types,
            compiler_symbols,
            runtime_modules,
        )
    bindings = {
        loaded.namespace_uris.index(binding.uri): binding for binding in loaded.namespace_bindings
    }
    for index, binding in bindings.items():
        if binding.shortname not in o6.ns:
            o6.ns.register(
                shortname=binding.shortname,
                uri=binding.uri,
                scope=o6.ns._GLOBAL_SCOPE,
                version=binding.version,
                publicationDate=binding.publication_date,
            )

    ns0_module = __import__("o6.ns", fromlist=["ns0"]).ns0
    infos = _datatype_infos(loaded)
    datatype_by_type = {
        (loaded.namespace_uris[int(node.id.ns)], node.browseName.name): node
        for node in loaded.nodes
        if isinstance(node, nodes_module.DataTypeNode)
    }
    datatype_by_id = {str(node.id): node for node in datatype_by_type.values()}
    roots = sorted(
        datatype_by_type.values(),
        key=lambda node: (
            loaded.namespace_uris[int(node.id.ns)],
            node.browseName.name,
            str(node.id),
        ),
    )
    ordered_datatypes: list[Any] = []
    aliases: dict[str, Any] = {}
    wire_markers: set[str] = set()
    emitted: set[str] = set()
    visiting: set[str] = set()

    def emit(node: Any) -> None:
        if node is None:
            return
        nodeid = str(node.id)
        if nodeid in emitted:
            return
        if nodeid in visiting:
            return
        if (
            int(node.id.ns) == 0
            and getattr(node.id, "i", None) in range(1, 26)
            and isinstance(getattr(o6, identifier(node.browseName.name), None), type)
        ):
            emitted.add(nodeid)
            return
        info = infos.get((loaded.namespace_uris[int(node.id.ns)], node.browseName.name))
        parent = datatype_parent(loaded, node)
        if type(info).__name__ == "StructType" and not getattr(info, "members", ()):
            ancestor = parent
            while ancestor is not None:
                ancestor_info = infos.get(
                    (loaded.namespace_uris[int(ancestor.id.ns)], ancestor.browseName.name)
                )
                if getattr(ancestor_info, "members", ()):
                    break
                ancestor = datatype_parent(loaded, ancestor)
            if ancestor is None:
                wire_markers.add(nodeid)
                emitted.add(nodeid)
                return
        if (
            info is not None
            and int(node.id.ns) == 0
            and isinstance(getattr(ns0_module, identifier(node.browseName.name), None), type)
        ):
            emitted.add(nodeid)
            return
        visiting.add(nodeid)
        emit(parent)
        if info is None:
            aliases[nodeid] = parent
            visiting.remove(nodeid)
            emitted.add(nodeid)
            return
        for member in getattr(info, "members", ()):
            emit(datatype_by_type.get((member.member_type.namespaceUri, member.member_type.name)))
        visiting.remove(nodeid)
        emitted.add(nodeid)
        ordered_datatypes.append(node)

    for node in roots:
        emit(node)

    target_names = python_names(
        (node for node in loaded.nodes if not node.hidden and int(node.id.ns) == target_index),
        nodes_module,
    )
    names: dict[str, str] = {}
    used: set[str] = set(target_names.values())
    for node in ordered_datatypes:
        nodeid = str(node.id)
        if int(node.id.ns) == target_index and nodeid in target_names:
            names[nodeid] = target_names[nodeid]
            continue
        binding = bindings[int(node.id.ns)]
        base = f"_compiler_{identifier(binding.shortname)}_{identifier(node.browseName.name)}"
        name = base
        suffix = 2
        while name in used:
            name = f"{base}_{suffix}"
            suffix += 1
        names[nodeid] = name
        used.add(name)
    proto_symbols = dict(type_symbols or {})
    proto_symbols.update(
        {
            (loaded.namespace_uris[int(node.id.ns)], node.browseName.name): names[str(node.id)]
            for node in ordered_datatypes
        }
    )
    base_symbols = {
        (loaded.namespace_uris[int(node.id.ns)], node.browseName.name): names[str(node.id)]
        for node in ordered_datatypes
    }

    def proto_symbol(node: Any) -> str | None:
        if node is None:
            return None
        nodeid = str(node.id)
        if nodeid in names:
            return names[nodeid]
        if nodeid in wire_markers:
            return "o6.ExtensionObject"
        if nodeid in aliases:
            return proto_symbol(aliases[nodeid])
        if int(node.id.ns) == 0:
            name = identifier(node.browseName.name)
            return (
                f"o6.{name}"
                if getattr(node.id, "i", None) in range(1, 26)
                else f"ns0.datatypes.{name}"
            )
        return None

    wire_aliases = {**aliases, **dict.fromkeys(wire_markers)}
    for nodeid, parent in wire_aliases.items():
        node = datatype_by_id[nodeid]
        symbol = "o6.ExtensionObject" if nodeid in wire_markers else proto_symbol(parent)
        if symbol is not None:
            proto_symbols[(loaded.namespace_uris[int(node.id.ns)], node.browseName.name)] = symbol
    lines = ["import o6", "from o6.ns import ns0", "from typing import Any, Optional", ""]

    def compiler_nodeid(value: Any) -> str:
        index = int(value.ns)
        text = str(value).split(";", 1)[-1]
        return text if index == 0 else f"ns={bindings[index].shortname};{text}"

    for node in ordered_datatypes:
        index = int(node.id.ns)
        binding = bindings[index]
        lines.extend(
            datatype_lines(
                loaded,
                node,
                target_index=index,
                target_uri=binding.uri,
                shortname=binding.shortname,
                names=names,
                local_names=set(names.values()),
                type_symbols=proto_symbols,
                base_symbols=base_symbols,
                nodeid_resolver=compiler_nodeid,
            )
        )
        lines.extend(["", ""])

    namespace: dict[str, Any] = {}
    exec(
        compile(
            "\n".join(lines),
            f"<{shortname}-compiler-datatypes>",
            "exec",
            dont_inherit=True,
        ),
        namespace,
    )
    types_by_nodeid = {nodeid: namespace[symbol] for nodeid, symbol in names.items()}
    for nodeid, parent in wire_aliases.items():
        symbol = "o6.ExtensionObject" if nodeid in wire_markers else proto_symbol(parent)
        if symbol is not None:
            types_by_nodeid[nodeid] = eval(symbol, {"o6": o6, "ns0": ns0_module, **namespace})
    symbols_by_nodeid: dict[str, str] = dict(symbols or {})
    for nodeid, proto_name in names.items():
        symbols_by_nodeid.setdefault(nodeid, proto_name)
    return ValueExpressionContext(
        loaded,
        target_index,
        shortname,
        types_by_nodeid,
        symbols_by_nodeid,
        runtime_modules,
    )


def _value_datatype(context: ValueExpressionContext, datatype_id: Any) -> type[Any]:
    datatype = datatype_node(context.loaded, datatype_id)
    if datatype is not None:
        info = _datatype_info(
            context.loaded,
            context.loaded.namespace_uris[int(datatype.id.ns)],
            datatype.browseName.name,
        )
        if bool(getattr(info, "isOptionSet", False)):
            ns0 = __import__("o6.ns", fromlist=["ns0"]).ns0
            return ns0.datatypes.OptionSet
    resolved = resolve_datatype(
        context.loaded,
        datatype_id,
        target_index=context.target_index,
        names=context.compiler_symbols,
        compiler_types=context.compiler_types,
    )
    if resolved.python_type is not None:
        return resolved.python_type

    import o6

    if resolved.expression.startswith("o6.NodeId("):
        return o6.ExtensionObject
    if resolved.expression.startswith("o6."):
        return getattr(o6, resolved.expression.removeprefix("o6."))
    if resolved.expression.startswith("ns0.datatypes."):
        ns0 = __import__("o6.ns", fromlist=["ns0"]).ns0
        return getattr(ns0.datatypes, resolved.expression.removeprefix("ns0.datatypes."))
    alias, separator, name = resolved.expression.partition(".")
    if separator and alias in context.runtime_modules:
        module = __import__(context.runtime_modules[alias], fromlist=[name])
        return getattr(module, name)
    raise UnsupportedValueError(f"no Python datatype for {datatype_id}")


def _inherited_datatype(context: ValueExpressionContext, node: Any) -> Any:
    """Resolve an omitted Variable DataType through its VariableType hierarchy."""

    seen: set[str] = set()
    current = node
    while current is not None:
        nodeid = str(current.id)
        if nodeid in seen:
            raise UnsupportedValueError(f"cyclic VariableType hierarchy at {nodeid}")
        seen.add(nodeid)
        if current.dataType is not None:
            return current.dataType
        if nodeid in {"i=62", "ns=0;i=62"}:  # BaseVariableType
            return type(current.id)("i=24")  # BaseDataType, the NodeSet2 default
        if type(current).__name__ == "VariableNode":
            current = context.loaded.nodeset.getNodeTypeDefinition(current)
        else:
            current = current.parent
    raise UnsupportedValueError(
        f"{type(node).__name__.removesuffix('Node')} {node.browseName} ({node.id}) "
        "has a Value but no resolvable DataType"
    )


def inherited_value_rank(context: ValueExpressionContext, node: Any) -> int:
    """Resolve an omitted ValueRank through its VariableType hierarchy."""

    seen: set[str] = set()
    current = node
    while current is not None:
        nodeid = str(current.id)
        if nodeid in seen:
            raise UnsupportedValueError(f"cyclic VariableType hierarchy at {nodeid}")
        seen.add(nodeid)
        if current.valueRank is not None:
            return int(current.valueRank)
        if nodeid in {"i=62", "ns=0;i=62"}:  # BaseVariableType
            return -2
        if type(current).__name__ == "VariableNode":
            current = context.loaded.nodeset.getNodeTypeDefinition(current)
        else:
            current = current.parent
    return -1  # UANodeSet.xsd default


def render_value(
    value: Any,
    type_expression: TypeExpression,
    nodeid_expression: NodeIdExpression | None = None,
) -> str:
    """Return a deterministic Python expression recreating *value*."""

    if value is None:
        return "None"
    if (
        type(value).__module__.startswith("numpy")
        and type(value).__name__ != "ndarray"
        and hasattr(value, "item")
    ):
        return render_value(value.item(), type_expression, nodeid_expression)
    if isinstance(value, enum.Enum):
        type_name = type_expression(type(value))
        member = getattr(value, "name", None)
        return f"{type_name}.{member}" if member else f"{type_name}({int(value)})"
    if isinstance(value, bool):
        return repr(value)
    if isinstance(value, int):
        return repr(value)
    if isinstance(value, float):
        if math.isnan(value):
            return "float('nan')"
        if math.isinf(value):
            return "float('inf')" if value > 0 else "float('-inf')"
        return repr(value)
    if isinstance(value, (str, bytes)):
        return repr(value)
    if isinstance(value, uuid.UUID):
        return f"uuid.UUID({str(value)!r})"
    if type(value).__module__ == "o6" and type(value).__name__ == "LocalizedText":
        if not value.text and not value.locale:
            return "o6.LocalizedText()"
        if value.locale or ":" in value.text:
            return f"o6.LocalizedText({value.text!r}, {value.locale!r})"
        return f"o6.LocalizedText({value.text!r})"
    if type(value).__module__ == "o6" and type(value).__name__ == "QualifiedName":
        prefix = f"{value.ns.shortname}:" if value.ns.index else ""
        return f"o6.QualifiedName({prefix + value.name!r})"
    if type(value).__module__ == "o6" and type(value).__name__ == "DateTime":
        return f"o6.DateTime({str(value)!r})"
    if type(value).__module__ == "o6" and type(value).__name__ == "ExtensionObject":
        if value.type_id is None:
            return "o6.ExtensionObject()"
        return f"o6.ExtensionObject({str(value.type_id)!r}, {value.body!r})"

    attributes = _type_spec(type(value))
    description = getattr(attributes, "structure_description", None)
    fields = _structure_fields(type(value)) if description is not None else None
    if fields is not None:
        parts: list[str] = []
        for field in fields:
            name = field.name
            try:
                field_value = getattr(value, name)
            except AttributeError as exc:
                raise UnsupportedValueError(
                    f"decoded {type(value).__name__} has no field {name!r}"
                ) from exc
            if (
                name == "description"
                and type(field_value).__module__ == "o6"
                and type(field_value).__name__ == "LocalizedText"
                and not field_value.text
                and not field_value.locale
            ):
                continue
            if name == "arrayDimensions" and not field_value:
                continue
            rendered = (
                nodeid_expression(field_value)
                if name == "dataType" and nodeid_expression is not None
                else render_value(field_value, type_expression, nodeid_expression)
            )
            parts.append(f"{name}={rendered}")
        return f"{type_expression(type(value))}({', '.join(parts)})"

    if type(value).__module__ == "o6" and type(value).__name__ in {
        "DataValue",
        "DiagnosticInfo",
    }:
        fields = [
            name
            for name, descriptor in type(value).__dict__.items()
            if isinstance(descriptor, types.GetSetDescriptorType)
        ]
        parts = [
            f"{name}={render_value(getattr(value, name), type_expression, nodeid_expression)}"
            for name in fields
        ]
        return f"o6.{type(value).__name__}({', '.join(parts)})"

    if isinstance(value, Iterable):
        return (
            "["
            + ", ".join(render_value(item, type_expression, nodeid_expression) for item in value)
            + "]"
        )

    expression = repr(value)
    if expression.startswith("o6."):
        return expression
    raise UnsupportedValueError(
        f"no canonical Python expression for decoded {type(value).__module__}.{type(value).__name__}"
    )


def render_node_value(context: ValueExpressionContext, node: Any) -> str | None:
    """Decode, render, evaluate, and validate one Variable or VariableType value."""

    if node.value is None:
        return None
    import o6

    xml = _xml_value(context, node.value.toxml())
    declared_datatype = _value_datatype(context, _inherited_datatype(context, node))
    namespace_indexes = tuple(
        getattr(
            o6.ns,
            next(
                binding.shortname
                for binding in context.loaded.namespace_bindings
                if binding.uri == uri
            ),
        ).index
        for uri in context.loaded.xml_namespace_uris
    )
    compiler_types = {
        str(type_.__o6_declaration__.nodeid): type_
        for type_ in context.compiler_types.values()
        if getattr(getattr(type_, "__o6_declaration__", None), "nodeid", None) is not None
    }
    value = _decode_nodeset_xml_value(xml, declared_datatype, namespace_indexes, compiler_types)
    if not _decoded_value_matches_datatype(value, declared_datatype):
        # A few published NodeSets use Argument ExtensionObjects as schema
        # placeholders even when the Variable declares a concrete scalar
        # datatype.  They are not valid values for that datatype.  Omitting
        # them lets the server create the required typed default instead of
        # generating Python that cannot be injected.
        return None
    raw_value_rank = getattr(node, "valueRank", None)
    value_rank = -1 if raw_value_rank is None else int(raw_value_rank)
    if value_rank >= 1 and not isinstance(value, (list, tuple, np.ndarray)):
        # Some published NodeSets encode a single array element without the
        # ListOf wrapper even though ValueRank declares an array. Preserve the
        # declared shape in generated Python instead of emitting a scalar that
        # the server must reject.
        for _ in range(value_rank):
            value = [value]

    def type_expression(py_type: type[Any]) -> str:
        for nodeid, compiler_type in context.compiler_types.items():
            if compiler_type is py_type or (
                compiler_type.__module__ == py_type.__module__
                and compiler_type.__name__ == py_type.__name__
            ):
                return context.compiler_symbols[nodeid]
        # A previously imported generated module can leave its runtime class
        # in the global datatype registry. During regeneration, resolve such a
        # same-namespace class to the compiler-local symbol by its unique name.
        namespace_module = f"o6.ns.{context.shortname}"
        if py_type.__module__ == namespace_module or py_type.__module__.startswith(
            f"{namespace_module}."
        ):
            for nodeid, compiler_type in context.compiler_types.items():
                if compiler_type.__name__ == py_type.__name__:
                    return context.compiler_symbols[nodeid]
        declaration = getattr(py_type, "__o6_declaration__", None)
        nodeid = getattr(declaration, "nodeid", None)
        if nodeid is not None:
            nodeid_text = str(nodeid)
            symbol = context.compiler_symbols.get(nodeid_text) or context.compiler_symbols.get(
                f"ns=0;{nodeid_text}"
            )
            if symbol is not None:
                return symbol
        if py_type.__module__ in {"o6.ns0", "o6.ns.ns0"}:
            return (
                py_type.__name__
                if context.target_index == 0
                else f"ns0.datatypes.{py_type.__name__}"
            )
        if getattr(o6, py_type.__name__, None) is py_type:
            return f"o6.{py_type.__name__}"
        for alias, module in context.runtime_modules.items():
            if py_type.__module__ == module:
                return f"{alias}.{py_type.__name__}"
        raise UnsupportedValueError(
            f"decoded type {py_type.__module__}.{py_type.__name__} has no generated symbol"
        )

    def nodeid_expression(nodeid: Any) -> str:
        try:
            return datatype_assignment_expression(
                context.loaded,
                nodeid,
                target_index=context.target_index,
                shortname=context.shortname,
                names=context.compiler_symbols,
                compiler_types=context.compiler_types,
            )
        except UnsupportedDataTypeError:
            return render_value(nodeid, type_expression)

    expression = render_value(value, type_expression, nodeid_expression)
    return expression


def _decoded_value_matches_datatype(value: Any, datatype: type[Any]) -> bool:
    """Whether a decoded NodeSet value consists of its declared Python type."""
    import o6

    # BaseDataType resolves to ExtensionObject in the XML decoder and accepts
    # arbitrary scalar or array payloads.
    if datatype is o6.ExtensionObject:
        return True
    if isinstance(value, np.ndarray):
        values = value.flat
    elif isinstance(value, (list, tuple)):
        values = value
    else:
        values = (value,)
    try:
        return all(isinstance(item, datatype) for item in values)
    except TypeError:
        # Non-runtime typing constructs cannot participate in isinstance.
        return True


def _xml_value(context: ValueExpressionContext, xml: str) -> str:
    """Replace custom Default XML encoding ids with their DataType ids.

    Temporary compiler datatypes carry the standard Default Binary id. The
    open62541 XML decoder also accepts the DataType id, which lets us decode
    custom ExtensionObjects without mutating the runtime datatype registry.
    """
    encoding_to_datatype: dict[str, Any] = {}
    for datatype in context.loaded.nodes:
        if type(datatype).__name__ != "DataTypeNode":
            continue
        for reference in datatype.references:
            if not reference.isForward or str(reference.referenceType) not in {
                "i=38",
                "ns=0;i=38",
            }:
                continue
            encoding = context.loaded.nodeset.nodes.get(reference.target)
            if encoding is not None and encoding.browseName.name == "Default XML":
                encoding_to_datatype[str(reference.target)] = datatype.id
    if not encoding_to_datatype:
        return xml

    root = ElementTree.fromstring(xml)
    global_by_uri = {uri: index for index, uri in enumerate(context.loaded.namespace_uris)}
    local_by_uri = {uri: index for index, uri in enumerate(context.loaded.xml_namespace_uris)}
    changed = False
    for identifier_element in root.findall(".//{*}TypeId/{*}Identifier"):
        identifier = (identifier_element.text or "").strip()
        match = re.fullmatch(r"(?:ns=(\d+);)?([isgb])=(.+)", identifier)
        if match is None:
            continue
        local_index = int(match.group(1) or 0)
        if local_index >= len(context.loaded.xml_namespace_uris):
            continue
        uri = context.loaded.xml_namespace_uris[local_index]
        global_index = global_by_uri.get(uri)
        if global_index is None:
            continue
        kind, value = match.group(2), match.group(3)
        global_id = f"ns={global_index};{kind}={value}"
        datatype_id = encoding_to_datatype.get(global_id)
        if datatype_id is None:
            continue
        datatype_uri = context.loaded.namespace_uris[int(datatype_id.ns)]
        datatype_local_index = local_by_uri[datatype_uri]
        prefix = f"ns={datatype_local_index};" if datatype_local_index else ""
        identifier_element.text = f"{prefix}{str(datatype_id).rsplit(';', 1)[-1]}"
        changed = True
    return ElementTree.tostring(root, encoding="unicode") if changed else xml
