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

"""NodeClass orchestration for the open62541-based Python source backend.

Naming, DataType source generation, and decoded value expressions live in
their focused sibling modules. This module orders nodes and emits declarations.
"""

from __future__ import annotations

import argparse
import ast
from collections import defaultdict
from dataclasses import dataclass
import heapq
import io
from pathlib import Path
import tokenize
from typing import Any

from .datatype_expression import (
    _datatype_infos,
    attribute_identifier,
    datatype_assignment_expression,
    datatype_dependencies,
    datatype_lines as _datatype_lines,
    member_identifier,
    python_names as _python_names,
    resolve_datatype,
)
from .frontend import LoadedNodeSet, ModelInput, load_nodeset
from .value_expression import (
    ValueExpressionContext,
    inherited_value_rank,
    prepare_value_context,
    render_node_value,
)


def _has_python_datatype_symbol(node: Any, parser_types: dict[str, Any]) -> bool:
    return (
        bool(getattr(node, "isAbstract", False))
        or getattr(node.id, "i", None) in {30, 12756}
        or type(parser_types.get(node.browseName.name)).__name__
        in {"EnumerationType", "StructType"}
    )


@dataclass(frozen=True)
class ReferenceRecord:
    source: str
    reference_type: str
    target: str


_REFERENCE_SHORTCUTS = {
    "i=35": "organizes",
    "i=36": "hasEventSource",
    "i=38": "hasEncoding",
    "i=46": "hasProperty",
    "i=47": "hasComponent",
    "i=48": "hasNotifier",
    "i=49": "hasOrderedComponent",
    "i=9004": "hasCondition",
    "i=17603": "hasInterface",
    "i=17604": "hasAddIn",
}

_NS0_ENTRY_POINTS = {"i=84", "i=85", "i=86", "i=87"}


def _nodeid_key(loaded: LoadedNodeSet, value: Any) -> tuple[Any, ...]:
    nodeid = loaded.endpoint(value).node.id
    namespace = loaded.namespace_uris[int(nodeid.ns)]
    if nodeid.i is not None:
        identifier = (0, int(nodeid.i))
    elif nodeid.s is not None:
        identifier = (1, str(nodeid.s))
    elif nodeid.g is not None:
        identifier = (2, tuple(int(part) for part in nodeid.g))
    else:
        identifier = (3, str(nodeid.b))
    return namespace, *identifier


def _node_key(loaded: LoadedNodeSet, node: Any) -> tuple[Any, ...]:
    return _nodeid_key(loaded, node.id)


def _reference_key(loaded: LoadedNodeSet, record: ReferenceRecord) -> tuple[Any, ...]:
    def endpoint_key(value: str) -> tuple[Any, ...]:
        if value in loaded.endpoints:
            return (0, *_nodeid_key(loaded, value))
        return (1, value)

    return (
        endpoint_key(record.source),
        endpoint_key(record.reference_type),
        endpoint_key(record.target),
    )


def _references(loaded: LoadedNodeSet) -> tuple[ReferenceRecord, ...]:
    records: list[ReferenceRecord] = []
    seen: set[tuple[str, str, str]] = set()
    for node in loaded.nodes:
        for reference in node.references:
            raw = (
                str(reference.source),
                str(reference.referenceType),
                str(reference.target),
            )
            canonical = raw if reference.isForward else (raw[2], raw[1], raw[0])
            if canonical in seen:
                continue
            seen.add(canonical)
            records.append(
                ReferenceRecord(
                    source=canonical[0],
                    reference_type=canonical[1],
                    target=canonical[2],
                )
            )
    for reference in loaded.external_references:
        raw = (reference.source, reference.reference_type, reference.target)
        canonical = raw if reference.is_forward else (raw[2], raw[1], raw[0])
        if canonical in seen:
            continue
        seen.add(canonical)
        records.append(ReferenceRecord(*canonical))
    return tuple(sorted(records, key=lambda record: _reference_key(loaded, record)))


def generate_inventory(loaded: LoadedNodeSet, *, source: str) -> str:
    """Emit a deterministic importable module describing the sorted graph."""

    nodes = [
        (str(node.id), type(node).__name__, str(node.browseName), index)
        for index, node in enumerate(
            sorted(loaded.generated_nodes, key=lambda node: _node_key(loaded, node))
        )
    ]
    references = [
        (record.source, record.reference_type, record.target, True)
        for record in _references(loaded)
    ]
    return (
        '"""Generated by the parallel open62541-based NodeSet compiler.\n\n'
        "This inventory backend is not yet a loadable o6 namespace module.\n"
        '"""\n\n'
        f"__SOURCE__ = {source!r}\n"
        f"__NAMESPACE_URIS__ = {loaded.namespace_uris!r}\n"
        f"__O6_NODES__ = {tuple(nodes)!r}\n"
        f"__O6_REFERENCES__ = {tuple(references)!r}\n"
    )


class UnsupportedNodeSetError(RuntimeError):
    pass


class SourceWriter:
    def __init__(self, initial: list[str] | None = None) -> None:
        self.lines = list(initial or ())

    def block(self, lines: list[str]) -> None:
        self.lines.extend(lines)
        self.lines.extend(["", ""])

    def section(self, title: str) -> None:
        border = "# " + "=" * 77
        self.block([border, f"# {title}", border])

    def finish(self) -> str:
        return "\n".join(self.lines) + "\n"


class GenerationContext:
    def __init__(
        self,
        loaded: LoadedNodeSet,
        *,
        nodes: Any,
        target_index: int,
        shortname: str,
        names: dict[str, str],
        generated_nodes: tuple[Any, ...],
    ) -> None:
        self.loaded = loaded
        self.nodes = nodes
        self.target_index = target_index
        self.shortname = shortname
        self.uri = loaded.namespace_uris[target_index]
        self.names = names
        self.generated_nodes = generated_nodes
        self.references = _references(loaded)
        self.namespace_names: dict[int, dict[str, str]] = {}
        self.symbols: dict[str, str] = {}
        self.type_symbols: dict[tuple[str, str], str] = {}
        datatype_infos = _datatype_infos(loaded)
        for index, binding in enumerate(loaded.namespace_bindings):
            parser_types = {
                name: info for (uri, name), info in datatype_infos.items() if uri == binding.uri
            }
            namespace_nodes = tuple(node for node in loaded.nodes if int(node.id.ns) == index)
            namespace_names = _python_names(
                namespace_nodes,
                nodes,
                key=lambda node: _node_key(loaded, node),
            )
            self.namespace_names[index] = namespace_names
            for nodeid, name in namespace_names.items():
                prefix = ""
                if index != target_index:
                    prefix = f"{binding.shortname}."
                    endpoint = loaded.endpoints[nodeid].node
                    if isinstance(endpoint, nodes.ReferenceTypeNode):
                        prefix += "reftypes."
                    elif isinstance(endpoint, nodes.DataTypeNode):
                        prefix += "datatypes."
                    elif isinstance(endpoint, nodes.VariableTypeNode):
                        prefix += "vartypes."
                    elif isinstance(endpoint, nodes.ObjectTypeNode):
                        prefix += "objtypes."
                    else:
                        prefix += "instances."
                self.symbols[nodeid] = prefix + name
            for node in namespace_nodes:
                if (
                    isinstance(node, nodes.DataTypeNode)
                    and str(node.id) in namespace_names
                    and _has_python_datatype_symbol(node, parser_types)
                ):
                    self.type_symbols[(binding.uri, node.browseName.name)] = self.symbols[
                        str(node.id)
                    ]
        self.symbols.update(names)
        target_parser_types = {
            name: info for (uri, name), info in datatype_infos.items() if uri == self.uri
        }
        self.local_datatype_names = {
            names[str(node.id)]
            for node in generated_nodes
            if isinstance(node, nodes.DataTypeNode)
            and _has_python_datatype_symbol(node, target_parser_types)
        }
        self.value_context = prepare_value_context(
            loaded,
            target_index=target_index,
            shortname=shortname,
            symbols=self.symbols,
            type_symbols=self.type_symbols,
        )
        grouped: dict[tuple[str, str], list[ReferenceRecord]] = defaultdict(list)
        for reference in self.references:
            grouped[(reference.source, _short_nodeid(reference.reference_type))].append(reference)
        self.references_by_source = {key: tuple(value) for key, value in grouped.items()}

        self.method_arguments: dict[str, dict[str, Any]] = defaultdict(dict)
        generated_ids = {str(node.id) for node in generated_nodes}
        for node in sorted(generated_nodes, key=lambda node: _node_key(loaded, node)):
            if not isinstance(node, nodes.VariableNode) or isinstance(node, nodes.VariableTypeNode):
                continue
            parent = getattr(node, "parent", None)
            if (
                isinstance(parent, nodes.MethodNode)
                and str(parent.id) in generated_ids
                and node.browseName.name in {"InputArguments", "OutputArguments"}
            ):
                self.method_arguments[str(parent.id)][node.browseName.name] = node
        instances = (nodes.VariableNode, nodes.ObjectNode, nodes.MethodNode)
        prerequisites: dict[str, set[str]] = defaultdict(set)
        for reference in self.references:
            kind = _short_nodeid(reference.reference_type)
            if kind == "i=40":
                prerequisites[reference.source].add(reference.target)
            elif kind == "i=45":
                prerequisites[reference.target].add(reference.source)

        def depends_on(nodeid: str, prerequisite: str) -> bool:
            pending, seen = [nodeid], set()
            while pending:
                current = pending.pop()
                if current == prerequisite:
                    return True
                if current not in seen:
                    seen.add(current)
                    pending.extend(prerequisites[current])
            return False

        self.children_by_parent: dict[str, list[tuple[Any, str]]] = defaultdict(list)
        for reference in sorted(self.references, key=lambda item: _reference_key(loaded, item)):
            source = loaded.endpoints.get(reference.source)
            target = loaded.endpoints.get(reference.target)
            if (
                source is not None
                and target is not None
                and reference.source in names
                and reference.target in names
                and isinstance(source.node, instances)
                and not isinstance(source.node, (nodes.VariableTypeNode, nodes.ObjectTypeNode))
                and not isinstance(source.node, nodes.MethodNode)
                and isinstance(target.node, instances)
                and not isinstance(target.node, (nodes.VariableTypeNode, nodes.ObjectTypeNode))
                and target.node.parent is source.node
                and self.is_hierarchical_reference(reference.reference_type)
                and not depends_on(reference.target, reference.source)
            ):
                self.children_by_parent[reference.source].append(
                    (target.node, _short_nodeid(reference.reference_type))
                )
                prerequisites[reference.source].add(reference.target)
        self.owned_children = {
            str(child.id) for children in self.children_by_parent.values() for child, _ in children
        }
        parents_with_children = set(self.children_by_parent)

        def is_structural_child_reference(child: Any, reference: ReferenceRecord) -> bool:
            child_id = str(child.id)
            reference_type = _short_nodeid(reference.reference_type)
            return (
                reference_type == _short_nodeid(child.parentReference.id)
                and reference.source == str(child.parent.id)
                and reference.target == child_id
            ) or (reference_type in {"i=37", "i=40"} and reference.source == child_id)

        self.embedded_children = {
            str(child.id)
            for children in self.children_by_parent.values()
            for child, _ in children
            if str(child.id) not in parents_with_children
            and not (
                self.uri == "http://opcfoundation.org/UA/"
                and _short_nodeid(child.id) in _NS0_ENTRY_POINTS
            )
            and all(
                is_structural_child_reference(child, reference)
                for reference in self.references
                if str(child.id) in (reference.source, reference.target)
            )
        }

    def nodeid(self, value: Any) -> str:
        text = str(value)
        index = int(value.ns)
        if index == 0:
            return text.removeprefix("ns=0;")
        shortname = self.loaded.namespace_bindings[index].shortname
        return f"ns={shortname};{text.split(';', 1)[1]}"

    def expression(self, nodeid: Any) -> str:
        try:
            return self.symbols[str(nodeid)]
        except KeyError as exc:
            raise UnsupportedNodeSetError(f"node {nodeid} has no generated Python symbol") from exc

    def nodeid_expression(self, value: Any, *, prefer_symbol: bool = True) -> str:
        text = str(value)
        if text.startswith(("svr=", "nsu=")):
            return f"o6.ExpandedNodeId({text!r})"
        node = self.loaded.endpoint(value).node
        if prefer_symbol and int(node.id.ns) != self.target_index:
            member = self.member_expression(node)
            if member is not None:
                return member
            symbol = self.symbols.get(text)
            if symbol is not None and not symbol.rsplit(".", 1)[-1].startswith("_"):
                return symbol
            shortname = self.loaded.namespace_bindings[int(node.id.ns)].shortname
            identifier = str(node.id).split(";", 1)[-1]
            return f"o6.ns[{f'ns={shortname};{identifier}'!r}]"
        if prefer_symbol and text in self.symbols:
            symbol = self.symbols[text]
            if int(node.id.ns) == self.target_index and symbol.startswith("_"):
                return f"o6.ns[{self.nodeid(node.id)!r}]"
            return symbol
        return repr(self.nodeid(node.id))

    def member_expression(self, node: Any) -> str | None:
        """Return the public owner path for a type child."""
        if not isinstance(
            node,
            (self.nodes.VariableNode, self.nodes.ObjectNode, self.nodes.MethodNode),
        ) or isinstance(node, (self.nodes.VariableTypeNode, self.nodes.ObjectTypeNode)):
            return None
        parent = getattr(node, "parent", None)
        if not isinstance(parent, (self.nodes.VariableTypeNode, self.nodes.ObjectTypeNode)):
            return None
        if not self.is_hierarchical_reference(node.parentReference.id):
            return None
        owner = self.symbols.get(str(parent.id))
        if owner is None:
            return None
        return f"{owner}.{attribute_identifier(node.browseName.name)}"

    def targets(self, node: Any, reference_type: str) -> tuple[Any, ...]:
        records = self.references_by_source.get((str(node.id), _short_nodeid(reference_type)), ())
        return tuple(self.loaded.endpoint(record.target).node.id for record in records)

    def target(self, node: Any, reference_type: str) -> Any | None:
        targets = self.targets(node, reference_type)
        return targets[0] if targets else None

    def is_hierarchical_reference(self, reference_type: Any) -> bool:
        current = self.loaded.endpoint(reference_type).node
        seen: set[str] = set()
        while current is not None and str(current.id) not in seen:
            if _short_nodeid(current.id) == "i=33":
                return True
            seen.add(str(current.id))
            parent = getattr(current, "parent", None)
            current = parent if isinstance(parent, self.nodes.ReferenceTypeNode) else None
        return False

    def datatype_expression(self, datatype_id: Any) -> str:
        return datatype_assignment_expression(
            self.loaded,
            datatype_id,
            target_index=self.target_index,
            shortname=self.shortname,
            names=self.symbols,
        )


def _node_metadata_args(context: GenerationContext, node: Any) -> list[str]:
    args: list[str] = []
    description = getattr(node, "resolvedDescription", None)
    if description:
        args.append(f"description={description!r}")
    if getattr(node, "writeMask", None):
        args.append(f"writeMask={int(node.writeMask)}")
    if getattr(node, "userWriteMask", None):
        args.append(f"userWriteMask={int(node.userWriteMask)}")
    role_permissions = getattr(node, "rolePermissions", None)
    if role_permissions:
        entries = ", ".join(
            f"{role!r}: {_permission_expression(context, permissions)}"
            for role, permissions in sorted(role_permissions.items())
        )
        args.append(f"rolePermissions={{{entries}}}")
    access_restrictions = int(getattr(node, "accessRestrictions", 0))
    if access_restrictions:
        args.append(f"accessRestrictions={access_restrictions}")
    return args


_PERMISSION_NAMES = (
    "BROWSE",
    "READ_ROLE_PERMISSIONS",
    "WRITE_ATTRIBUTE",
    "WRITE_ROLE_PERMISSIONS",
    "WRITE_HISTORIZING",
    "READ",
    "WRITE",
    "READ_HISTORY",
    "INSERT_HISTORY",
    "MODIFY_HISTORY",
    "DELETE_HISTORY",
    "RECEIVE_EVENTS",
    "CALL",
    "ADD_REFERENCE",
    "REMOVE_REFERENCE",
    "DELETE_NODE",
    "ADD_NODE",
)


def _permission_owner(context: GenerationContext) -> str:
    """Name `PermissionType` the way any other type of the same namespace is named.

    Inside ns0 that is the bare name: the package splitter qualifies it against
    the sibling `datatypes` module, which ns0 imports first.
    """
    if context.uri == "http://opcfoundation.org/UA/":
        return "PermissionType"
    return "ns0.datatypes.PermissionType"


def _permission_expression(context: GenerationContext, value: int) -> str:
    remaining = int(value)
    owner = _permission_owner(context)
    terms = [
        f"{owner}.{name}"
        for bit, name in enumerate(_PERMISSION_NAMES)
        if remaining & (1 << bit)
    ]
    remaining &= ~((1 << len(_PERMISSION_NAMES)) - 1)
    if remaining or not terms:
        terms.append(str(remaining))
    return " | ".join(terms)


def _display_name(node: Any) -> str:
    return (
        getattr(node, "resolvedDisplayName", None)
        or getattr(node.displayName, "text", None)
        or node.browseName.name
    )


def _instance_browsename(context: GenerationContext, node: Any) -> str:
    namespace = int(node.browseName.ns)
    name = node.browseName.name
    if namespace == 0:
        return name
    return f"ns={context.loaded.namespace_bindings[namespace].shortname};{name}"


def _value_array_dimensions(expression: str | None) -> list[int] | None:
    """Return the rectangular dimensions of a generated list literal."""
    if expression is None:
        return None

    def shape(value: ast.AST) -> tuple[int, ...] | None:
        if not isinstance(value, ast.List):
            return ()
        child_shapes = {shape(child) for child in value.elts}
        if None in child_shapes or len(child_shapes) > 1:
            return None
        return (len(value.elts),) + (next(iter(child_shapes)) if child_shapes else ())

    dimensions = shape(ast.parse(expression, mode="eval").body)
    return list(dimensions) if dimensions else None


def _instance_args(
    context: GenerationContext, node: Any, *, include_parent: bool = True
) -> list[str]:
    args = [
        f"nodeId={context.nodeid(node.id)!r}",
        f"browseName={_instance_browsename(context, node)!r}",
        *_node_metadata_args(context, node),
    ]
    displayname = _display_name(node)
    if displayname and displayname != node.browseName.name:
        args.append(f"displayName={displayname!r}")
    modelling_rule = context.target(node, "i=37")
    if modelling_rule is not None:
        rule = context.loaded.endpoint(str(modelling_rule)).node
        rule_name = rule.browseName.name
        relationship_is_explicit = not include_parent or str(node.id) in context.owned_children
        if (
            str(node.id) in context.deferred_members
            or not relationship_is_explicit
            or rule_name not in {"Mandatory", "Optional"}
        ):
            args.append(f"modellingRule={rule_name!r}")
    children = context.children_by_parent.get(str(node.id), ())
    if children:
        links = []
        for child, reference_type in children:
            name = (
                _instance_expression(context, child, include_parent=False)
                if str(child.id) in context.embedded_children
                else context.nodeid_expression(child.id)
            )
            shortcut = _REFERENCE_SHORTCUTS.get(reference_type)
            links.append(
                f"o6.{shortcut}({name})"
                if shortcut is not None
                else f"o6.reference({name}, {context.nodeid(child.parentReference.id)!r})"
            )
        args.append(f"references=[{', '.join(links)}]")
    if (
        include_parent
        and str(node.id) not in context.owned_children
        and node.parent is not None
        and context.is_hierarchical_reference(node.parentReference.id)
    ):
        args.append(f"parent={context.nodeid(node.parent.id)!r}")
        args.append(f"referenceType={context.expression(node.parentReference.id)}")
    return args


def _typed_instance(
    context: GenerationContext, node: Any, *, include_parent: bool = True
) -> tuple[Any, list[str]]:
    typedef = context.target(node, "i=40")
    if typedef is None:
        raise UnsupportedNodeSetError(
            f"{type(node).__name__.removesuffix('Node')} {node.browseName} ({node.id}) "
            "has no TypeDefinition"
        )
    args = _instance_args(context, node, include_parent=include_parent)
    typedef_node = context.loaded.nodeset.nodes.get(typedef)
    if typedef_node is not None and bool(getattr(typedef_node, "isAbstract", False)):
        args.append("_allow_abstract=True")
    return typedef, args


def _type_parent_name(context: GenerationContext, node: Any) -> str | None:
    parent_id = next(
        (
            reference.source
            for reference in context.references
            if _short_nodeid(reference.reference_type) == "i=45"
            and reference.target == str(node.id)
        ),
        None,
    )
    parent = context.loaded.endpoint(parent_id).node if parent_id is not None else None
    if parent is None:
        if context.target_index == 0:
            return None
        raise UnsupportedNodeSetError(f"type {node.browseName} ({node.id}) has no parent")
    return context.expression(parent.id)


def _type_declaration(context: GenerationContext, node: Any) -> str:
    parent = _type_parent_name(context, node)
    name = context.names[str(node.id)]
    if parent is None and name == "BaseObjectType":
        parent = "_ObjectNode"
    elif parent is None and name == "BaseVariableType":
        parent = "_VariableNode"
    return f"class {name}({parent}):" if parent else f"class {name}:"


def _type_browsename(context: GenerationContext, node: Any) -> str:
    name = node.browseName.name
    return name if context.shortname == "ns0" else f"ns={context.shortname};{name}"


def _type_constructor(name: str) -> list[str]:
    """Type the runtime constructor installed by object/variable type decorators."""
    if name not in {"BaseVariableType", "BaseObjectType"}:
        return ["    pass"]
    common = [
        "server: object = ...",
        "nodeId: o6.NodeIdLike | None = None",
        "parent: o6.NodeIdLike | None = None",
        "referenceType: o6.NodeIdLike | None = None",
        "browseName: str | None = None",
        "values: dict[str, object] | None = None",
        "references: list[object] | None = None",
    ]
    if name == "BaseVariableType":
        common.extend(
            [
                "value: object = None",
                "dataType: o6.NodeIdLike | None = None",
                "valueRank: int | None = None",
                "arrayDimensions: list[int] | None = None",
                "accessLevel: int | None = None",
                "userAccessLevel: int | None = None",
                "minimumSamplingInterval: float | None = None",
                "historizing: bool = False",
            ]
        )
    common.extend(
        [
            "writeMask: int | None = None",
            "userWriteMask: int | None = None",
            "rolePermissions: dict[object, int] | None = None",
            "accessRestrictions: int = 0",
            "eventNotifier: int = 0",
            "description: str | None = None",
            "displayName: str | None = None",
            "modellingRule: str | None = None",
            "_allow_abstract: bool = False",
        ]
    )
    return [
        "    _nodeid: o6.NodeId",
        "    if TYPE_CHECKING:",
        "        def __init__(self, *,",
        *(f"            {arg}," for arg in common),
        "        ) -> None: ...",
    ]


def _variabletype_lines(
    context: GenerationContext,
    node: Any,
) -> list[str]:
    nodeid = context.nodeid(node.id)
    args = [
        f"nodeId={nodeid!r}",
        f"browseName={_type_browsename(context, node)!r}",
        f"displayName={_display_name(node)!r}",
        *_node_metadata_args(context, node),
    ]
    if bool(getattr(node, "isAbstract", False)):
        args.append("isAbstract=True")
    if node.dataType is not None:
        args.append(f"dataType={context.datatype_expression(node.dataType)}")
    if node.valueRank is not None:
        value_rank = int(node.valueRank)
        symbolic = {
            -3: "SCALAR_OR_1D",
            -2: "ANY",
            -1: "SCALAR",
            0: "ARRAY_ANY",
            1: "ARRAY_1D",
            2: "ARRAY_2D",
        }.get(value_rank)
        args.append(f"valueRank=o6.ValueRank.{symbolic}" if symbolic else f"valueRank={value_rank}")
    value = render_node_value(context.value_context, node)
    array_dimensions = [int(item) for item in node.arrayDimensions]
    value_dimensions = _value_array_dimensions(value)
    if value_dimensions and len(value_dimensions) == inherited_value_rank(
        context.value_context, node
    ):
        array_dimensions = value_dimensions
    if array_dimensions:
        args.append(f"arrayDimensions={array_dimensions!r}")
    if value is not None:
        args.append(f"value={value}")
    name = context.names[str(node.id)]
    return [
        *_omitted_value_warning(node, value),
        f"@o6.variabletype({', '.join(args)})",
        _type_declaration(context, node),
        *_type_constructor(name),
    ]


def _variable_lines(
    context: GenerationContext,
    node: Any,
    *,
    include_parent: bool = True,
) -> list[str]:
    typedef, args = _typed_instance(context, node, include_parent=include_parent)
    if node.dataType is not None:
        args.append(f"dataType={context.datatype_expression(node.dataType)}")
    if node.valueRank is not None:
        args.append(f"valueRank={int(node.valueRank)}")
    elif inherited_value_rank(context.value_context, node) == -3:
        # ScalarOrOneDimension needs the schema-default scalar choice on a
        # concrete Variable. Other type constraints remain inherited.
        args.append("valueRank=-1")
    value = render_node_value(context.value_context, node)
    array_dimensions = [int(item) for item in node.arrayDimensions]
    value_dimensions = _value_array_dimensions(value)
    declared_value_rank = -1 if node.valueRank is None else int(node.valueRank)
    if value_dimensions and len(value_dimensions) == declared_value_rank:
        array_dimensions = value_dimensions
    if array_dimensions:
        args.append(f"arrayDimensions={array_dimensions!r}")
    if value is not None:
        args.append(f"value={value}")
    if int(node.accessLevel) != 1:
        args.append(f"accessLevel={int(node.accessLevel)}")
    if int(node.userAccessLevel) != int(node.accessLevel):
        args.append(f"userAccessLevel={int(node.userAccessLevel)}")
    if float(node.minimumSamplingInterval) != 0.0:
        args.append(f"minimumSamplingInterval={float(node.minimumSamplingInterval)!r}")
    if bool(node.historizing):
        args.append("historizing=True")
    return [
        *_omitted_value_warning(node, value),
        f"{context.names[str(node.id)]} = {context.expression(typedef)}({', '.join(args)})",
    ]


def _omitted_value_warning(node: Any, rendered_value: str | None) -> list[str]:
    if getattr(node, "value", None) is None or rendered_value is not None:
        return []
    return [
        "# WARNING: The source NodeSet value does not match the declared DataType.",
        "# It is intentionally omitted; the server supplies a typed default.",
    ]


def _object_lines(
    context: GenerationContext,
    node: Any,
    *,
    include_parent: bool = True,
) -> list[str]:
    typedef, args = _typed_instance(context, node, include_parent=include_parent)
    if int(node.eventNotifier):
        args.append(f"eventNotifier={int(node.eventNotifier)}")
    return [f"{context.names[str(node.id)]} = {context.expression(typedef)}({', '.join(args)})"]


def _method_lines(
    context: GenerationContext,
    node: Any,
    *,
    include_parent: bool = True,
) -> list[str]:
    args = _instance_args(context, node, include_parent=include_parent)
    if not bool(node.executable):
        args.append("executable=False")
    if not bool(node.userExecutable):
        args.append("userExecutable=False")
    for browse_name, argument_name in (
        ("InputArguments", "inputArgs"),
        ("OutputArguments", "outputArgs"),
    ):
        argument_node = context.method_arguments.get(str(node.id), {}).get(browse_name)
        if argument_node is not None:
            argument = context.nodeid_expression(argument_node.id)
            args.append(f"{argument_name}=o6.hasProperty({argument})")
    return [f"{context.names[str(node.id)]} = o6.call({', '.join(args)})"]


def _view_lines(
    context: GenerationContext,
    node: Any,
) -> list[str]:
    args = _instance_args(context, node)
    args.append(f"containsNoLoops={bool(node.containsNoLoops)!r}")
    if int(node.eventNotifier):
        args.append(f"eventNotifier={int(node.eventNotifier)}")
    return [f"{context.names[str(node.id)]} = o6.view({', '.join(args)})"]


def _short_nodeid(value: Any) -> str:
    text = str(value)
    return text[5:] if text.startswith("ns=0;") else text


def _expression_names(expression: str | None) -> set[str]:
    """Return actual Python name references, excluding text inside literals."""
    if expression is None:
        return set()
    return {
        node.id
        for node in ast.walk(ast.parse(expression, mode="eval"))
        if isinstance(node, ast.Name)
    }


def _emission_order(context: GenerationContext) -> tuple[Any, ...]:
    """Topologically order declarations by their actual Python prerequisites."""
    argument_ids = {
        str(argument.id)
        for arguments in context.method_arguments.values()
        for argument in arguments.values()
    }
    nodes = {
        str(node.id): node for node in context.generated_nodes if str(node.id) not in argument_ids
    }
    dependencies: dict[str, set[str]] = {nodeid: set() for nodeid in nodes}
    for reference in context.references:
        reference_type = _short_nodeid(reference.reference_type)
        if reference_type == "i=40":  # HasTypeDefinition: type before instance
            prerequisite, dependent = reference.target, reference.source
        elif reference_type == "i=45":  # HasSubtype: supertype before subtype
            prerequisite, dependent = reference.source, reference.target
        elif (
            reference.source in context.children_by_parent
            and any(
                str(child.id) == reference.target
                for child, _ in context.children_by_parent[reference.source]
            )
            and not isinstance(
                context.loaded.endpoint(reference.source).node,
                (
                    context.nodes.ReferenceTypeNode,
                    context.nodes.DataTypeNode,
                    context.nodes.VariableTypeNode,
                    context.nodes.ObjectTypeNode,
                ),
            )
        ):
            prerequisite, dependent = reference.target, reference.source
        else:
            continue
        if prerequisite in nodes and dependent in nodes:
            dependencies[dependent].add(prerequisite)

    def depends_on(nodeid: str, prerequisite: str) -> bool:
        pending, seen = [nodeid], set()
        while pending:
            current = pending.pop()
            if current == prerequisite:
                return True
            if current not in seen:
                seen.add(current)
                pending.extend(dependencies[current])
        return False

    for reference in context.references:
        if reference.source not in nodes or reference.target not in nodes:
            continue
        source = context.loaded.endpoint(reference.source).node
        target = context.loaded.endpoint(reference.target).node
        if (
            target.parent is source
            and context.is_hierarchical_reference(reference.reference_type)
            and not isinstance(
                source,
                (
                    context.nodes.ReferenceTypeNode,
                    context.nodes.DataTypeNode,
                    context.nodes.VariableTypeNode,
                    context.nodes.ObjectTypeNode,
                ),
            )
            and not depends_on(reference.target, reference.source)
        ):
            dependencies[reference.source].add(reference.target)

    for nodeid, node in nodes.items():
        candidates = list(context.targets(node, "i=17603"))
        if getattr(node, "dataType", None) is not None:
            candidates.append(node.dataType)
        if isinstance(node, context.nodes.DataTypeNode):
            candidates.extend(datatype_dependencies(context.loaded, node))
        if getattr(node, "value", None) is not None:
            names = _expression_names(render_node_value(context.value_context, node))
            candidates.extend(
                candidate
                for candidate, symbol in context.symbols.items()
                if "." not in symbol and symbol in names
            )
        dependencies[nodeid].update(
            str(item) for item in candidates if str(item) in nodes and str(item) != nodeid
        )

    context.inline_members = set()
    for child_id, child in sorted(
        nodes.items(), key=lambda item: _node_key(context.loaded, item[1])
    ):
        parent = getattr(child, "parent", None)
        if (
            context.member_expression(child) is not None
            and isinstance(parent, (context.nodes.VariableTypeNode, context.nodes.ObjectTypeNode))
            and str(parent.id) in nodes
            and not depends_on(child_id, str(parent.id))
            and all(
                _emission_phase(context, nodes[prerequisite])[0]
                <= _emission_phase(context, parent)[0]
                for prerequisite in dependencies[child_id]
            )
        ):
            dependencies[str(parent.id)].add(child_id)
            context.inline_members.add(child_id)
    children = {
        str(node.parent.id)
        for node in nodes.values()
        if getattr(node, "parent", None) is not None and str(node.parent.id) in nodes
    }
    context.embedded_members = set()
    for child_id in context.inline_members:
        child = nodes[child_id]
        if child_id in children:
            continue

        def is_structural(record: ReferenceRecord) -> bool:
            reference_type = _short_nodeid(record.reference_type)
            return (
                reference_type == _short_nodeid(child.parentReference.id)
                and record.source == str(child.parent.id)
                and record.target == child_id
            ) or (reference_type in ("i=37", "i=40") and record.source == child_id)

        if all(
            is_structural(record)
            for record in context.references
            if child_id in (record.source, record.target)
        ):
            context.embedded_members.add(child_id)
    context.inline_support = {}
    for nodeid, node in nodes.items():
        current = node
        seen: set[str] = set()
        while current is not None and str(current.id) not in seen:
            current_id = str(current.id)
            seen.add(current_id)
            if current_id in context.inline_members:
                context.inline_support[nodeid] = current.parent
                break
            current = getattr(current, "parent", None)
    context.deferred_members = {
        str(node.id)
        for node in nodes.values()
        if context.member_expression(node) is not None
        and str(node.id) not in context.inline_members
    }

    ordered: list[Any] = []
    emitted: set[str] = set()
    dependents: dict[str, set[str]] = defaultdict(set)
    for dependent, prerequisites in dependencies.items():
        for prerequisite in prerequisites:
            dependents[prerequisite].add(dependent)

    def emission_key(nodeid: str) -> tuple[Any, ...]:
        node = nodes[nodeid]
        return (_emission_phase(context, node)[0], _node_key(context.loaded, node))

    for dependent, prerequisites in dependencies.items():
        dependent_phase = emission_key(dependent)[0]
        for prerequisite in prerequisites:
            prerequisite_phase = emission_key(prerequisite)[0]
            if prerequisite_phase > dependent_phase:
                raise UnsupportedNodeSetError(
                    "declaration dependency crosses emission phases: "
                    f"{prerequisite} -> {dependent}"
                )

    ready = [
        (emission_key(nodeid), nodeid) for nodeid, node in nodes.items() if not dependencies[nodeid]
    ]
    heapq.heapify(ready)
    while ready:
        _, root_id = heapq.heappop(ready)
        ordered.append(nodes[root_id])
        emitted.add(root_id)
        for dependent in sorted(
            dependents[root_id], key=lambda nodeid: _nodeid_key(context.loaded, nodeid)
        ):
            if dependencies[dependent] <= emitted:
                heapq.heappush(
                    ready,
                    (emission_key(dependent), dependent),
                )
    if len(emitted) != len(nodes):
        cycle = {
            nodeid: sorted(
                dependencies[nodeid] - emitted,
                key=lambda nodeid: _nodeid_key(context.loaded, nodeid),
            )
            for nodeid in nodes
            if nodeid not in emitted
        }
        raise UnsupportedNodeSetError(f"cyclic declaration dependencies: {cycle}")
    return tuple(ordered)


def _emission_phase(context: GenerationContext, node: Any) -> tuple[int, str]:
    """Return the fixed generated-source section for a node declaration."""
    owner = getattr(context, "inline_support", {}).get(str(node.id))
    if owner is not None:
        return _emission_phase(context, owner)
    if isinstance(node, context.nodes.ReferenceTypeNode):
        return 0, "Reference Types"
    if isinstance(node, context.nodes.DataTypeNode):
        return 1, "Data Types"
    if isinstance(node, context.nodes.VariableTypeNode):
        return 2, "Variable Types"
    if isinstance(node, context.nodes.ObjectTypeNode):
        return 3, "Object Types"
    if isinstance(node, context.nodes.ViewNode):
        return 4, "Views"
    return 5, "Instances"


def _reference_lines(
    context: GenerationContext,
) -> list[tuple[ReferenceRecord, frozenset[str], str]]:
    lines: list[tuple[ReferenceRecord, frozenset[str], str]] = []
    represented: set[ReferenceRecord] = set()
    for record in context.references:
        source_endpoint = context.loaded.endpoints.get(record.source)
        target_endpoint = context.loaded.endpoints.get(record.target)
        source_node = source_endpoint.node if source_endpoint else None
        target_node = target_endpoint.node if target_endpoint else None
        reference_type = _short_nodeid(record.reference_type)
        is_parent = (
            source_node is not None
            and target_node is not None
            and target_node.parent is source_node
            and _short_nodeid(target_node.parentReference.id) == reference_type
            and context.is_hierarchical_reference(record.reference_type)
        )
        default_binary_encoding = (
            reference_type == "i=38"
            and source_node is not None
            and target_node is not None
            and target_node.browseName.name == "Default Binary"
            and record.source in context.names
        )
        modelling_rule = reference_type == "i=37" and isinstance(
            source_node,
            (context.nodes.VariableNode, context.nodes.ObjectNode, context.nodes.MethodNode),
        )
        type_definition = (
            reference_type == "i=40"
            and isinstance(source_node, (context.nodes.VariableNode, context.nodes.ObjectNode))
            and not isinstance(source_node, context.nodes.VariableTypeNode)
        )
        if (
            is_parent
            or modelling_rule
            or type_definition
            or default_binary_encoding
            or (
                reference_type == "i=17603"
                and isinstance(source_node, context.nodes.ObjectTypeNode)
            )
        ):
            if record.source in context.names or record.target in context.names:
                represented.add(record)
            continue
        source_id, target_id = record.source, record.target
        local_source = context.names.get(source_id)
        local_target = context.names.get(target_id)
        if local_source is not None and local_source.startswith("_"):
            local_source = f"o6.ns[{context.nodeid(source_node.id)!r}]"
        if local_target is not None and local_target.startswith("_"):
            local_target = f"o6.ns[{context.nodeid(target_node.id)!r}]"
        if local_source is None and local_target is None:
            continue
        verb = context.nodeid(context.loaded.endpoint(record.reference_type).node.id)

        if local_source is not None:
            marker_to_owned_instance = isinstance(
                source_node,
                (context.nodes.VariableTypeNode, context.nodes.ObjectTypeNode),
            ) and isinstance(
                target_node,
                (context.nodes.VariableNode, context.nodes.ObjectNode, context.nodes.MethodNode),
            )
            target = context.nodeid_expression(
                target_id,
                prefer_symbol=not marker_to_owned_instance and target_id in context.names,
            )
            line = (
                f"o6.hasEncoding({local_source}, {target})"
                if reference_type == "i=38"
                else f"o6.reference({local_source}, {verb!r}, {target})"
            )
        else:
            source = context.nodeid_expression(source_id, prefer_symbol=source_id in context.names)
            line = f"o6.reference({local_target}, {verb!r}, {source}, inverse=True)"
        required = frozenset(
            endpoint for endpoint in (source_id, target_id) if endpoint in context.names
        )
        lines.append((record, required, line))
        represented.add(record)
    expected = {
        record
        for record in context.references
        if record.source in context.names or record.target in context.names
    }
    if represented != expected:
        missing = sorted(
            expected - represented, key=lambda record: _reference_key(context.loaded, record)
        )
        raise UnsupportedNodeSetError(f"unrepresented references: {missing}")
    return lines


def _member_line(context: GenerationContext, node: Any) -> tuple[str, str] | None:
    """Return the ownership path and linkage for a type child."""
    path = context.member_expression(node)
    if path is None:
        return None
    reference_type = context.nodeid(node.parentReference.id)
    name = context.nodeid_expression(node.id)
    shortcut = _REFERENCE_SHORTCUTS.get(reference_type)
    linkage = (
        f"o6.{shortcut}({name})"
        if shortcut is not None
        else f"o6.reference({name}, {reference_type!r})"
    )
    return path, f"{path}: {_member_type(context, node)} = {linkage}"


def _member_type(context: GenerationContext, node: Any) -> str:
    """Return the precise public type of a generated type member."""
    if isinstance(node, (context.nodes.VariableNode, context.nodes.ObjectNode)):
        typedef, _ = _typed_instance(context, node)
        annotation = _unquote_annotation(context.expression(typedef))
    elif isinstance(node, context.nodes.MethodNode):
        annotation = "o6.node.MethodNode"
    else:
        raise UnsupportedNodeSetError(f"cannot type member {type(node).__name__} {node.id}")
    modelling_rule = context.target(node, "i=37")
    if modelling_rule is not None:
        rule = context.loaded.endpoint(str(modelling_rule)).node.browseName.name
        if rule.startswith("Optional"):
            annotation += " | None"
    return annotation


def _unquote_annotation(expression: str) -> str:
    """Remove a redundant forward-reference quote from an annotation.

    Generated modules enable postponed annotations, so names need not be
    quoted even when they refer to the class currently being declared or to a
    class emitted later in the module. Keeping the quote would produce a
    string nested inside the postponed annotation and hide unions such as
    ``T | None`` from the decorators that derive modelling rules from them.
    """
    try:
        value = ast.literal_eval(expression)
    except (SyntaxError, ValueError):
        return expression
    return value if isinstance(value, str) else expression


def _inline_member_lines(context: GenerationContext, owner: Any) -> list[str]:
    """Return members embedded in, or linked from, the class body."""
    members: list[tuple[str, str]] = []
    paths: dict[str, str] = {}
    for node in context.generated_nodes:
        nodeid = str(node.id)
        if node.parent is not owner or nodeid not in (
            context.inline_members | context.deferred_members
        ):
            continue
        member = _member_line(context, node)
        if member is None:
            continue
        path, _ = member
        previous = paths.get(path)
        if previous is not None:
            raise UnsupportedNodeSetError(
                f"type {owner.browseName} ({owner.id}) has children {previous} and "
                f"{node.id} that both normalize to Python member {path.rsplit('.', 1)[-1]!r}"
            )
        paths[path] = str(node.id)
        if nodeid in context.deferred_members:
            annotation = _member_type(context, node)
            members.append(
                (
                    path,
                    f"    {path.rsplit('.', 1)[-1]}: {annotation}",
                )
            )
            continue
        reference_type = context.nodeid(node.parentReference.id)
        if nodeid in context.embedded_members:
            declaration = _instance_expression(context, node, include_parent=False)
        else:
            declaration = f"o6.ns[{context.nodeid(node.id)!r}]"
        shortcut = _REFERENCE_SHORTCUTS.get(reference_type)
        linkage = (
            f"o6.{shortcut}({declaration})"
            if shortcut is not None
            else f"o6.reference({declaration}, {reference_type!r})"
        )
        members.append(
            (
                path,
                f"    {path.rsplit('.', 1)[-1]}: {_member_type(context, node)} = {linkage}",
            )
        )
    return [line for _, line in sorted(members)]


def _instance_expression(
    context: GenerationContext, node: Any, *, include_parent: bool = True
) -> str:
    """Render an instance constructor without binding it to a module global."""
    if isinstance(node, context.nodes.VariableNode):
        lines = _variable_lines(context, node, include_parent=include_parent)
    elif isinstance(node, context.nodes.ObjectNode):
        lines = _object_lines(context, node, include_parent=include_parent)
    elif isinstance(node, context.nodes.MethodNode):
        lines = _method_lines(context, node, include_parent=include_parent)
    else:
        raise UnsupportedNodeSetError(f"cannot embed {type(node).__name__} {node.id}")
    expression = lines[-1].split(" = ", 1)[1]
    return "\n".join((*lines[:-1], expression))


def _unbound_instance_lines(
    context: GenerationContext, node: Any, *, include_parent: bool = True
) -> list[str]:
    """Emit a self-registering instance without retaining a Python binding."""
    if isinstance(node, context.nodes.MethodNode):
        lines = _method_emission(context, node)
        lines[-1] = _instance_expression(context, node, include_parent=include_parent)
        return lines
    return [_instance_expression(context, node, include_parent=include_parent)]


def _deferred_member_reference(context: GenerationContext, node: Any) -> str:
    """Attach a constructed recursive member instance to its owning type."""
    owner = context.expression(node.parent.id)
    reference_type = context.expression(node.parentReference.id)
    target = f"o6.ns[{context.nodeid(node.id)!r}]"
    return f"o6.reference({owner}, {reference_type}, {target})"


def _datatype_emission(context: GenerationContext, node: Any) -> list[str]:
    return _datatype_lines(
        context.loaded,
        node,
        target_index=context.target_index,
        target_uri=context.uri,
        shortname=context.shortname,
        names=context.names,
        local_names=context.local_datatype_names,
        type_symbols=context.type_symbols,
        nodeid_resolver=context.nodeid,
    )


def _method_emission(context: GenerationContext, node: Any) -> list[str]:
    lines: list[str] = []
    arguments = context.method_arguments.get(str(node.id), {})
    for argument in arguments.values():
        lines.append(_instance_expression(context, argument))
    lines.extend(_method_lines(context, node))
    return lines


def _referencetype_emission(context: GenerationContext, node: Any) -> list[str]:
    args = [
        f"nodeId={context.nodeid(node.id)!r}",
        f"browseName={_type_browsename(context, node)!r}",
        f"displayName={_display_name(node)!r}",
        *_node_metadata_args(context, node),
    ]
    inverse = getattr(node, "resolvedInverseName", None) or getattr(
        getattr(node, "inverseName", None), "text", None
    )
    if inverse:
        args.append(f"inverseName={inverse!r}")
    if bool(getattr(node, "symmetric", False)):
        args.append("symmetric=True")
    if bool(getattr(node, "isAbstract", False)):
        args.append("isAbstract=True")
    return [
        f"@o6.referencetype({', '.join(args)})",
        _type_declaration(context, node),
        "    pass",
    ]


def _objecttype_emission(context: GenerationContext, node: Any) -> list[str]:
    args = [
        f"nodeId={context.nodeid(node.id)!r}",
        f"browseName={_type_browsename(context, node)!r}",
        f"displayName={_display_name(node)!r}",
        *_node_metadata_args(context, node),
    ]
    if bool(getattr(node, "isAbstract", False)):
        args.append("isAbstract=True")
    interfaces = [context.expression(target) for target in context.targets(node, "i=17603")]
    if interfaces:
        args.append(f"interfaces=[{', '.join(interfaces)}]")
    name = context.names[str(node.id)]
    return [
        f"@o6.objecttype({', '.join(args)})",
        _type_declaration(context, node),
        *_type_constructor(name),
    ]


def generate_type_module(
    loaded: LoadedNodeSet,
    *,
    source: str,
) -> str:
    """Generate a loadable module, failing on every unsupported NodeClass."""

    if loaded.unsupported_features:
        feature = loaded.unsupported_features[0]
        raise UnsupportedNodeSetError(
            f"{feature.node_class} {feature.nodeid} has unsupported {feature.feature}"
        )

    nodes_module = __import__(
        f"{type(loaded.nodeset).__module__.rsplit('.', 1)[0]}.nodes",
        fromlist=["nodes"],
    )
    supported = (
        nodes_module.DataTypeNode,
        nodes_module.ReferenceTypeNode,
        nodes_module.VariableTypeNode,
        nodes_module.ObjectTypeNode,
        nodes_module.ObjectNode,
        nodes_module.VariableNode,
        nodes_module.MethodNode,
        nodes_module.ViewNode,
    )
    unsupported = [node for node in loaded.generated_nodes if not isinstance(node, supported)]
    if unsupported:
        node = unsupported[0]
        raise UnsupportedNodeSetError(
            f"{type(node).__name__} {node.browseName} ({node.id}) is not supported by the backend"
        )

    target_indexes = {int(node.id.ns) for node in loaded.generated_nodes}
    if len(target_indexes) != 1:
        raise UnsupportedNodeSetError(
            f"expected exactly one generated namespace, found {sorted(target_indexes)}"
        )
    target_index = target_indexes.pop()
    shortname = loaded.target_binding.shortname
    generated_nodes = tuple(loaded.generated_nodes)
    names = _python_names(
        generated_nodes,
        nodes_module,
        key=lambda node: _node_key(loaded, node),
    )
    context = GenerationContext(
        loaded,
        nodes=nodes_module,
        target_index=target_index,
        shortname=shortname,
        names=names,
        generated_nodes=generated_nodes,
    )
    argument_ids = {
        str(argument.id)
        for arguments in context.method_arguments.values()
        for argument in arguments.values()
    }
    emitters = {
        nodes_module.DataTypeNode: _datatype_emission,
        nodes_module.ReferenceTypeNode: _referencetype_emission,
        nodes_module.VariableTypeNode: _variabletype_lines,
        nodes_module.ObjectTypeNode: _objecttype_emission,
        nodes_module.VariableNode: _variable_lines,
        nodes_module.ObjectNode: _object_lines,
        nodes_module.MethodNode: _method_emission,
        nodes_module.ViewNode: _view_lines,
    }
    dependencies = sorted(
        (binding for binding in loaded.namespace_bindings if not binding.target),
        key=lambda binding: (binding.module, binding.shortname),
    )
    imports = ["from typing import Any, TYPE_CHECKING", "import uuid", "import o6"]
    imports.extend(f"import {binding.module} as {binding.shortname}" for binding in dependencies)
    writer = SourceWriter(
        [
            '"""Generated by the parallel open62541-based NodeSet compiler."""',
            "",
            *imports,
            "",
            "if TYPE_CHECKING:",
            "    from o6.node import ObjectNode as _ObjectNode",
            "    from o6.node import VariableNode as _VariableNode",
            "else:",
            "    _ObjectNode = object",
            "    _VariableNode = object",
            "",
            f"o6.ns.namespace(shortname={shortname!r}, uri={context.uri!r}, "
            f"version={loaded.version!r}, publicationDate={loaded.publication_date!r})",
            "",
        ]
    )
    emitted = [
        node
        for node in _emission_order(context)
        if str(node.id) not in argument_ids
        and str(node.id) not in context.embedded_members
        and str(node.id) not in context.embedded_children
    ]
    instance_types = (
        nodes_module.VariableNode,
        nodes_module.ObjectNode,
        nodes_module.MethodNode,
        nodes_module.ViewNode,
    )
    type_nodes = (nodes_module.VariableTypeNode, nodes_module.ObjectTypeNode)
    member_nodes = {
        str(node.id): (node, member)
        for node in context.generated_nodes
        if (member := _member_line(context, node)) is not None
    }
    members_by_endpoint: dict[str, set[str]] = defaultdict(set)
    local_ids = {str(node.id) for node in context.generated_nodes}
    available = {
        str(node.parent.id)
        for node, _ in member_nodes.values()
        if str(node.parent.id) not in local_ids
    }
    for child_id, (child, _) in member_nodes.items():
        members_by_endpoint[child_id].add(child_id)
        members_by_endpoint[str(child.parent.id)].add(child_id)
    published_members: set[str] = set(context.inline_members)
    loose_references = _reference_lines(context)
    references_by_endpoint: dict[str, set[ReferenceRecord]] = defaultdict(set)
    reference_details = {record: (required, line) for record, required, line in loose_references}
    for record, required, _ in loose_references:
        for endpoint in required:
            references_by_endpoint[endpoint].add(record)
    published_references: set[ReferenceRecord] = set()
    current_section: str | None = None
    for index, node in enumerate(emitted):
        _, section = _emission_phase(context, node)
        if section != current_section:
            writer.section(section)
            current_section = section
        private_instance = (
            isinstance(node, instance_types)
            and not isinstance(node, type_nodes)
            and context.names[str(node.id)].startswith("_")
        )
        if str(node.id) in context.inline_members:
            lines = _unbound_instance_lines(context, node, include_parent=False)
        elif private_instance:
            lines = _unbound_instance_lines(
                context,
                node,
                include_parent=str(node.id) not in context.deferred_members,
            )
        else:
            lines = emitters[type(node)](context, node)
        inline_members = _inline_member_lines(context, node)
        if inline_members:
            if lines[-1] == "    pass":
                lines.pop()
            lines.extend(inline_members)
        declared = {str(node.id)}
        declared.update(
            str(argument.id) for argument in context.method_arguments.get(str(node.id), {}).values()
        )
        available.update(declared)
        candidates = set().union(*(members_by_endpoint[item] for item in declared))
        for child_id in sorted(candidates, key=lambda item: member_nodes[item][1][0]):
            child, member = member_nodes[child_id]
            if (
                child_id not in published_members
                and child_id in available
                and str(child.parent.id) in available
            ):
                lines.append(
                    _deferred_member_reference(context, child)
                    if child_id in context.deferred_members
                    else member[1]
                )
                published_members.add(child_id)
        reference_candidates = set().union(*(references_by_endpoint[item] for item in declared))
        for record in sorted(
            reference_candidates, key=lambda item: _reference_key(context.loaded, item)
        ):
            required, line = reference_details[record]
            if record not in published_references and required <= available:
                lines.append(line)
                published_references.add(record)
        next_node = emitted[index + 1] if index + 1 < len(emitted) else None
        consecutive_instances = (
            isinstance(node, instance_types)
            and not isinstance(node, (*type_nodes, nodes_module.MethodNode))
            and isinstance(next_node, instance_types)
            and not isinstance(next_node, (*type_nodes, nodes_module.MethodNode))
        )
        writer.lines.extend(lines)
        if not consecutive_instances:
            writer.lines.extend([""] if isinstance(node, nodes_module.MethodNode) else ["", ""])
    if published_members != member_nodes.keys():
        missing = sorted(member_nodes.keys() - published_members)
        raise UnsupportedNodeSetError(f"unpublished type members: {missing}")
    if published_references != reference_details.keys():
        missing = sorted(
            reference_details.keys() - published_references,
            key=lambda item: _reference_key(context.loaded, item),
        )
        raise UnsupportedNodeSetError(f"unpublished references: {missing}")
    helpers = [
        "Any",
        "TYPE_CHECKING",
        "uuid",
        "o6",
        *(binding.shortname for binding in dependencies),
    ]
    writer.lines.append(f"del {', '.join(helpers)}")
    return writer.finish()


_NS0_CATEGORIES = (
    ("Reference Types", "reftypes"),
    ("Data Types", "datatypes"),
    ("Variable Types", "vartypes"),
    ("Object Types", "objtypes"),
    ("Instances", "instances"),
)


def _defined_names(source: str) -> set[str]:
    tree = ast.parse(source)
    names = {
        node.name
        for node in tree.body
        if isinstance(node, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef))
    }
    for node in tree.body:
        targets = (
            [node.target]
            if isinstance(node, ast.AnnAssign)
            else node.targets if isinstance(node, ast.Assign) else ()
        )
        names.update(target.id for target in targets if isinstance(target, ast.Name))
    return names


def _qualify_names(source: str, names: dict[str, str]) -> str:
    """Qualify bare generated symbols without touching strings or attributes."""
    tokens = list(tokenize.generate_tokens(io.StringIO(source).readline))
    result: list[tokenize.TokenInfo] = []
    previous_significant: tokenize.TokenInfo | None = None
    for token in tokens:
        replacement = names.get(token.string) if token.type == tokenize.NAME else None
        if replacement is not None and not (
            previous_significant is not None and previous_significant.string == "."
        ):
            token = tokenize.TokenInfo(
                token.type,
                replacement,
                token.start,
                token.end,
                token.line,
            )
        result.append(token)
        if token.type not in {
            tokenize.ENCODING,
            tokenize.INDENT,
            tokenize.DEDENT,
            tokenize.NEWLINE,
            tokenize.NL,
        }:
            previous_significant = token
    return tokenize.untokenize(result)


def generate_namespace_package(source: str, shortname: str) -> dict[str, str]:
    """Split a generated namespace module into node-category package files."""
    lines = source.splitlines()
    external_imports = [
        line for line in lines if line.startswith("import o6.ns.") and " as " in line
    ]
    starts = {
        category: lines.index(f"# {title}") - 1
        for title, category in _NS0_CATEGORIES
        if f"# {title}" in lines
    }
    generated: dict[str, str] = {}
    bodies: dict[str, str] = {}
    names_by_category: dict[str, set[str]] = {}
    for position, (_, category) in enumerate(_NS0_CATEGORIES):
        if category not in starts:
            bodies[category] = ""
            names_by_category[category] = set()
            continue
        start = starts[category]
        following = [
            starts[next_category]
            for _, next_category in _NS0_CATEGORIES[position + 1 :]
            if next_category in starts
        ]
        end = following[0] if following else len(lines)
        body = lines[start + 3 : end]
        while body and not body[0]:
            body.pop(0)
        if category == "instances" and body and body[-1].startswith("del "):
            body.pop()
        bodies[category] = "\n".join(body)
        names_by_category[category] = _defined_names(bodies[category])

    prior: list[str] = []
    for _, category in _NS0_CATEGORIES:
        if not bodies[category]:
            continue
        aliases = {
            name: f"{shortname}_{'datypes' if dependency == 'datatypes' else dependency}.{name}"
            for dependency in prior
            for name in names_by_category[dependency]
        }
        body = _qualify_names(bodies[category], aliases).splitlines()
        local_imports: list[str] = []
        if prior:
            local_imports.extend(
                f"from . import {dependency} as "
                f"{shortname}_{'datypes' if dependency == 'datatypes' else dependency}"
                for dependency in prior
            )
        helper_names = [
            "Any",
            "TYPE_CHECKING",
            "uuid",
            "o6",
            *(line.rsplit(" as ", 1)[1] for line in external_imports),
            *(line.rsplit(" as ", 1)[1] for line in local_imports),
        ]
        generated[f"{category}.py"] = "\n".join(
            [
                f'"""Generated OPC UA {shortname} namespace declarations."""',
                "",
                "from __future__ import annotations",
                "",
                "from typing import Any, TYPE_CHECKING",
                "import uuid",
                "import o6",
                *external_imports,
                *local_imports,
                "",
                "if TYPE_CHECKING:",
                "    from o6.node import ObjectNode as _ObjectNode",
                "    from o6.node import VariableNode as _VariableNode",
                "else:",
                "    _ObjectNode = object",
                "    _VariableNode = object",
                "",
                *body,
                "",
                f"del {', '.join(helper_names)}",
                "",
            ]
        )
        prior.append(category)

    registration = next(line for line in lines if line.startswith("o6.ns.namespace("))
    registration = registration.replace("o6.ns.namespace(", "_initialize_namespace(__name__, ", 1)
    registration = registration.replace("publicationDate=", "publication_date=", 1)
    category_imports = [
        f"from . import {category} as {category}"
        for _, category in _NS0_CATEGORIES
        if bodies[category]
    ]
    generated["__init__.py"] = "\n".join(
        [
            f'"""Generated OPC UA {shortname} namespace."""',
            "",
            "from o6.ns import _initialize_namespace",
            "",
            registration,
            "",
            *category_imports,
            "",
            "del _initialize_namespace",
            "",
        ]
    )
    return generated


def generate_ns0_package(source: str) -> dict[str, str]:
    """Backward-compatible wrapper for namespace-zero package generation."""
    return generate_namespace_package(source, "ns0")


def generate_namespace_datatypes_stub(source: str, shortname: str) -> str:
    """Generate a namespace's sole category stub, for native DataType classes."""
    datatype_source = generate_namespace_package(source, shortname)["datatypes.py"]
    datatype_tree = ast.parse(datatype_source)
    names = {
        node.name
        for node in datatype_tree.body
        if isinstance(node, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef))
    }
    for node in datatype_tree.body:
        targets = (
            [node.target]
            if isinstance(node, ast.AnnAssign)
            else node.targets if isinstance(node, ast.Assign) else ()
        )
        names.update(target.id for target in targets if isinstance(target, ast.Name))

    stub = generate_stub_module(source)
    kept: list[str] = []
    for node in ast.parse(stub).body:
        name = getattr(node, "name", None)
        targets = (
            [node.target]
            if isinstance(node, ast.AnnAssign)
            else node.targets if isinstance(node, ast.Assign) else ()
        )
        target_names = {target.id for target in targets if isinstance(target, ast.Name)}
        if (
            isinstance(node, (ast.Import, ast.ImportFrom))
            or (name is not None and name in names)
            or any(item in names or item.startswith("_") for item in target_names)
        ):
            segment = ast.get_source_segment(stub, node)
            if segment:
                kept.append(segment)
    return "\n\n".join(kept) + "\n"


def generate_ns0_datatypes_stub(source: str) -> str:
    """Backward-compatible wrapper for namespace-zero datatype stubs."""
    return generate_namespace_datatypes_stub(source, "ns0")


_INTEGER_ANNOTATIONS = {
    "o6.SByte",
    "o6.Byte",
    "o6.Int16",
    "o6.UInt16",
    "o6.Int32",
    "o6.UInt32",
    "o6.Int64",
    "o6.UInt64",
    "o6.StatusCode",
}


def _stub_annotation(annotation: ast.expr) -> ast.expr:
    """Return a stub annotation without runtime-only forward-reference quotes."""
    if isinstance(annotation, ast.Constant) and isinstance(annotation.value, str):
        return ast.parse(annotation.value, mode="eval").body
    return annotation


def _stub_write_annotation(annotation: ast.expr, enum_names: set[str]) -> ast.expr:
    """Return the values accepted by the native setter for an annotated field."""
    annotation = _stub_annotation(annotation)
    text = ast.unparse(annotation)
    if text in _INTEGER_ANNOTATIONS or text in enum_names:
        return ast.Name(id="_Integer")
    if text == "o6.Boolean":
        return ast.Name(id="_Boolean")
    if text in {"o6.Float", "o6.Double"}:
        return ast.Name(id="SupportsFloat")
    if text in {"Any", "o6.ExtensionObject"}:
        return ast.Name(id="Any")
    if isinstance(annotation, ast.BinOp) and isinstance(annotation.op, ast.BitOr):
        return ast.BinOp(
            left=_stub_write_annotation(annotation.left, enum_names),
            op=ast.BitOr(),
            right=_stub_write_annotation(annotation.right, enum_names),
        )
    if (
        isinstance(annotation, ast.Subscript)
        and isinstance(annotation.value, ast.Name)
        and annotation.value.id == "list"
    ):
        return ast.Subscript(
            value=ast.Name(id="Sequence"),
            slice=_stub_write_annotation(annotation.slice, enum_names),
        )
    return annotation


def _stub_property(
    name: str, annotation: ast.expr, enum_names: set[str]
) -> tuple[ast.FunctionDef, ast.FunctionDef]:
    getter = ast.FunctionDef(
        name=name,
        args=ast.arguments(
            posonlyargs=[],
            args=[ast.arg(arg="self")],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[],
        ),
        body=[ast.Expr(value=ast.Constant(value=Ellipsis))],
        decorator_list=[ast.Name(id="property")],
        returns=annotation,
    )
    setter = ast.FunctionDef(
        name=name,
        args=ast.arguments(
            posonlyargs=[],
            args=[
                ast.arg(arg="self"),
                ast.arg(arg="value", annotation=_stub_write_annotation(annotation, enum_names)),
            ],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[],
        ),
        body=[ast.Expr(value=ast.Constant(value=Ellipsis))],
        decorator_list=[ast.Attribute(value=ast.Name(id=name), attr="setter")],
        returns=ast.Constant(value=None),
    )
    return getter, setter


def generate_stub_module(source: str) -> str:
    """Project a generated namespace module into its minimal static API."""
    tree = ast.parse(source)
    # Both integer-form DataTypes the C extension builds as an ``IntFlag``: an
    # ordinary enumeration and an OptionSet.  The stub must say ``enum.IntFlag``
    # for both, or ``A | B``, ``int(A)`` and ``T(value)`` stop type-checking.
    enum_names = {
        node.name
        for node in tree.body
        if isinstance(node, ast.ClassDef)
        and any(
            ast.unparse(item.func).endswith(("enumtype", "optionsettype"))
            for item in node.decorator_list
            if isinstance(item, ast.Call)
        )
    }
    body: list[ast.stmt] = [
        ast.Expr(
            value=ast.Constant(
                value="Generated static API for the corresponding o6 namespace module."
            )
        ),
        ast.ImportFrom(
            module="typing",
            names=[
                ast.alias(name="Any"),
                ast.alias(name="Sequence"),
                ast.alias(name="SupportsFloat"),
            ],
            level=0,
        ),
        ast.Import(names=[ast.alias(name="numpy", asname="np")]),
        ast.Assign(
            targets=[ast.Name(id="_Integer")],
            value=ast.BinOp(
                left=ast.Name(id="int"),
                op=ast.BitOr(),
                right=ast.Subscript(
                    value=ast.Attribute(value=ast.Name(id="np"), attr="integer"),
                    slice=ast.Name(id="Any"),
                ),
            ),
        ),
        ast.Assign(
            targets=[ast.Name(id="_Boolean")],
            value=ast.BinOp(
                left=ast.Name(id="bool"),
                op=ast.BitOr(),
                right=ast.Attribute(value=ast.Name(id="np"), attr="bool_"),
            ),
        ),
        ast.Import(names=[ast.alias(name="enum")]),
        ast.ImportFrom(
            module="o6.node",
            names=[
                ast.alias(name="ObjectNode", asname="_ObjectNode"),
                ast.alias(name="VariableNode", asname="_VariableNode"),
            ],
            level=0,
        ),
    ]
    class_members = {
        statement.name: {
            member.target.id: _stub_annotation(member.annotation)
            for member in statement.body
            if isinstance(member, ast.AnnAssign) and isinstance(member.target, ast.Name)
        }
        for statement in tree.body
        if isinstance(statement, ast.ClassDef)
    }
    class_bases = {
        statement.name: [base.id for base in statement.bases if isinstance(base, ast.Name)]
        for statement in tree.body
        if isinstance(statement, ast.ClassDef)
    }

    def inherited_members(name: str) -> dict[str, ast.expr]:
        inherited: dict[str, ast.expr] = {}
        for base in class_bases.get(name, ()):
            inherited.update(inherited_members(base))
            inherited.update(class_members.get(base, {}))
        return inherited

    for statement in tree.body:
        if isinstance(statement, (ast.Import, ast.ImportFrom)):
            if not (isinstance(statement, ast.ImportFrom) and statement.module == "typing"):
                body.append(statement)
            continue
        if isinstance(statement, ast.ClassDef):
            datatype = any(
                isinstance(item, ast.Call)
                and ast.unparse(item.func).endswith(("datatype", "enumtype"))
                for item in statement.decorator_list
            )
            description = next(
                (
                    keyword.value.value
                    for item in statement.decorator_list
                    if isinstance(item, ast.Call)
                    for keyword in item.keywords
                    if keyword.arg == "description"
                    and isinstance(keyword.value, ast.Constant)
                    and isinstance(keyword.value.value, str)
                ),
                None,
            )
            class_body: list[ast.stmt] = []
            if description:
                class_body.append(ast.Expr(value=ast.Constant(value=description)))
            for member in statement.body:
                if isinstance(member, ast.AnnAssign) and isinstance(member.target, ast.Name):
                    if member.target.id.startswith("_") and member.target.id != "_nodeid":
                        continue
                    annotation = _stub_annotation(member.annotation)
                    if datatype and statement.name not in enum_names:
                        class_body.extend(_stub_property(member.target.id, annotation, enum_names))
                    elif not member.target.id.startswith("_"):
                        inherited = inherited_members(statement.name).get(member.target.id)
                        if inherited is not None and ast.unparse(inherited) != ast.unparse(
                            annotation
                        ):
                            annotation = ast.Name(id="Any")
                        class_body.append(
                            ast.AnnAssign(
                                target=member.target,
                                annotation=annotation,
                                value=None,
                                simple=1,
                            )
                        )
                elif isinstance(member, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    member.decorator_list = [
                        item
                        for item in member.decorator_list
                        if not ast.unparse(item).startswith("o6.")
                    ]
                    member.body = [ast.Expr(value=ast.Constant(value=Ellipsis))]
                    class_body.append(member)
                elif isinstance(member, ast.Assign):
                    for target in member.targets:
                        if isinstance(target, ast.Name) and not target.id.startswith("_"):
                            if statement.name in enum_names:
                                value: ast.expr = ast.Constant(value=Ellipsis)
                                # ``o6.enumfield(3)`` gives a Constant,
                                # ``o6.bitmask(0x01 << 3)`` a BinOp; both are the
                                # member's value and belong in the stub verbatim.
                                if (
                                    isinstance(member.value, ast.Call)
                                    and member.value.args
                                    and isinstance(member.value.args[0], (ast.Constant, ast.BinOp))
                                ):
                                    value = member.value.args[0]
                                class_body.append(ast.Assign(targets=[target], value=value))
                                continue
                            if isinstance(member.value, ast.Call) and ast.unparse(
                                member.value.func
                            ).endswith("optionsetbit"):
                                # One declared bit of a structure-form OptionSet.
                                # Reading it is three-valued -- ``None`` is "the
                                # ``ValidBits`` bit is clear", not an error -- and
                                # writing it goes through the same name.
                                class_body.extend(
                                    _stub_property(
                                        target.id,
                                        ast.parse("bool | None", mode="eval").body,
                                        enum_names,
                                    )
                                )
                                continue
                            class_body.append(
                                ast.AnnAssign(
                                    target=target,
                                    annotation=ast.Name(id=statement.name),
                                    value=None,
                                    simple=1,
                                )
                            )
            if not class_body:
                class_body.append(ast.Pass())
            body.append(
                ast.ClassDef(
                    name=statement.name,
                    bases=(
                        [ast.Name(id="_ObjectNode")]
                        if statement.name == "BaseObjectType"
                        else (
                            [ast.Name(id="_VariableNode")]
                            if statement.name == "BaseVariableType"
                            else (
                                [ast.Attribute(value=ast.Name(id="enum"), attr="IntFlag")]
                                if statement.name in enum_names
                                and any(isinstance(member, ast.Assign) for member in statement.body)
                                else (
                                    [ast.Name(id="int")]
                                    if statement.name == "Enumeration"
                                    else statement.bases
                                )
                            )
                        )
                    ),
                    keywords=[],
                    body=class_body,
                    decorator_list=[],
                )
            )
            continue
        if isinstance(statement, ast.AnnAssign):
            if isinstance(statement.target, ast.Name) and not statement.target.id.startswith("_"):
                statement.value = None
                body.append(statement)
            continue
        if isinstance(statement, ast.Assign):
            for target in statement.targets:
                if not isinstance(target, ast.Name) or target.id.startswith("_"):
                    continue
                if isinstance(statement.value, (ast.Name, ast.Attribute)):
                    body.append(ast.Assign(targets=[target], value=statement.value))
                    continue
                annotation: ast.expr = ast.Name(id="Any")
                if isinstance(statement.value, ast.Call):
                    function = statement.value.func
                    if isinstance(function, (ast.Name, ast.Attribute)):
                        annotation = function
                body.append(
                    ast.AnnAssign(
                        target=target,
                        annotation=annotation,
                        value=None,
                        simple=1,
                    )
                )
    return ast.unparse(ast.fix_missing_locations(ast.Module(body=body, type_ignores=[]))) + "\n"


def has_generated_datatypes(source: str) -> bool:
    """Return whether a generated namespace needs a datatype API stub."""
    return any(
        decorator in source
        for decorator in ("@o6.datatype(", "@o6.enumtype(", "@o6.optionsettype(")
    )


def main(argv: list[str] | None = None) -> int:
    def dependency(value: str) -> ModelInput:
        if "=" not in value:
            path = Path(value)
            from .frontend import _model_metadata

            if _model_metadata(path)[0] == "http://opcfoundation.org/UA/":
                return ModelInput(path, "ns0")
            raise argparse.ArgumentTypeError("dependencies require SHORTNAME=PATH")
        shortname, path = value.split("=", 1)
        return ModelInput(Path(path), shortname)

    parser = argparse.ArgumentParser()
    parser.add_argument("xml", type=Path, nargs="?")
    parser.add_argument("--existing", type=dependency, action="append", default=[])
    parser.add_argument("--out", type=Path)
    parser.add_argument(
        "--stub-source",
        type=Path,
        help="project an existing generated namespace module into a .pyi file",
    )
    parser.add_argument("--refresh-description-cache", action="store_true")
    parser.add_argument("--shortname")
    args = parser.parse_args(argv)

    if args.stub_source is not None:
        source = args.stub_source.read_text(encoding="utf-8")
        if not has_generated_datatypes(source):
            parser.error(f"{args.stub_source} contains no generated datatypes")
        output = args.out or args.stub_source.with_suffix(".pyi")
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(generate_stub_module(source), encoding="utf-8")
        return 0

    if args.refresh_description_cache:
        if args.xml is None:
            parser.error("xml is required with --refresh-description-cache")
        from .frontend import refresh_description_cache

        refresh_description_cache([args.xml])
        return 0
    if args.out is None:
        parser.error("--out is required unless --refresh-description-cache is used")
    if args.xml is None:
        parser.error("xml is required")

    target = ModelInput(args.xml, args.shortname or args.xml.stem)
    loaded = load_nodeset(target, existing=args.existing)
    source = (
        generate_type_module(loaded, source=str(args.xml))
        if args.shortname
        else generate_inventory(loaded, source=str(args.xml))
    )
    if args.shortname:
        package_dir = args.out.with_suffix("")
        package_dir.mkdir(parents=True, exist_ok=True)
        package = generate_namespace_package(source, args.shortname)
        expected = set(package)
        if has_generated_datatypes(source):
            expected.add("datatypes.pyi")
        for stale in (*package_dir.glob("*.py"), *package_dir.glob("*.pyi")):
            if stale.name not in expected:
                stale.unlink()
        for relative, content in package.items():
            (package_dir / relative).write_text(content, encoding="utf-8")
        if has_generated_datatypes(source):
            (package_dir / "datatypes.pyi").write_text(
                generate_namespace_datatypes_stub(source, args.shortname), encoding="utf-8"
            )
    else:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(source, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
