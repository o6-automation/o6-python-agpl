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

"""Publication of namespace declaration graphs into one server."""

from __future__ import annotations

from contextlib import contextmanager
from functools import partial
import logging
from types import ModuleType
from typing import Any, Callable

import o6
from o6 import _server_construction
from o6._declarations import (
    DataTypeSpec,
    EnumTypeSpec,
    InstanceDeclaration,
    MethodSpec,
    ObjectTypeSpec,
    ReferenceTypeSpec,
    TypeDeclaration,
    VariableTypeSpec,
    _instance_declaration,
    _resolved_modelling_rule,
    _declaration_nodeid,
    _type_declaration,
    _type_target_nodeid,
)
from o6._server_construction import _apply_role_permissions, _construct_declaration
from o6.node import VariableNode
from o6.ns import ns0

_logger = logging.getLogger(__name__)

_ORGANIZES = "i=35"
_OBJECTS_FOLDER = "i=85"


def _is_referencetype_base(base: type) -> bool:
    declaration = vars(base).get("__o6_declaration__")
    return isinstance(declaration, TypeDeclaration) and isinstance(
        declaration.attributes, ReferenceTypeSpec
    )


def _is_variabletype_base(base: type) -> bool:
    declaration = vars(base).get("__o6_declaration__")
    return isinstance(declaration, TypeDeclaration) and isinstance(
        declaration.attributes, VariableTypeSpec
    )


def _is_objecttype_base(base: type) -> bool:
    declaration = vars(base).get("__o6_declaration__")
    return isinstance(declaration, TypeDeclaration) and isinstance(
        declaration.attributes, ObjectTypeSpec
    )


@contextmanager
def _temporarily_concrete(server: Any, type_ids: set[o6.NodeId]):
    for type_id in type_ids:
        server._on_event_loop(partial(server._set_type_abstract, type_id, False))
    try:
        yield
    finally:
        for type_id in type_ids:
            server._on_event_loop(partial(server._set_type_abstract, type_id, True))


def _namespace_values(ns: ModuleType) -> list[Any]:
    """Return declarations from a namespace package and its category modules."""
    modules = [ns]
    modules.extend(
        category
        for name in ("reftypes", "datatypes", "vartypes", "objtypes", "instances")
        if isinstance((category := getattr(ns, name, None)), ModuleType)
    )
    values: list[Any] = []
    seen: set[int] = set()
    for module in modules:
        for name, value in vars(module).items():
            if name.startswith("_") or id(value) in seen:
                continue
            seen.add(id(value))
            values.append(value)
    return values


class _NamespaceInventory:
    """One scan of the declarations exported by a namespace package."""

    __slots__ = ("module", "values", "markers", "instances")

    def __init__(self, ns: ModuleType) -> None:
        self.module = ns
        self.values = _namespace_values(ns)
        self.markers: dict[Any, list[type]] = {}
        for value in self.values:
            if not isinstance(value, type):
                continue
            declaration = vars(value).get("__o6_declaration__")
            if isinstance(declaration, TypeDeclaration):
                self.markers.setdefault(declaration.nodeclass, []).append(value)
        self.instances = list(ns.__dict__.get("__O6_INSTANCES__", ()))

    def for_nodeclass(self, nodeclass: Any) -> list[type]:
        return self.markers.get(nodeclass, [])


def _collect_variabletype_markers(ns: ModuleType) -> list[type]:
    return _NamespaceInventory(ns).for_nodeclass(ns0.datatypes.NodeClass.VARIABLE_TYPE)


class _NamespacePublisher:
    """Cold-path publication of one namespace declaration graph."""

    def __init__(
        self,
        server: Any,
        registered_modules: list[ModuleType],
        inventory: _NamespaceInventory,
    ) -> None:
        self._server = server
        self._nodeset_modules = registered_modules
        self._inventory = inventory
        self._created_types: set[type] = set()
        self._created_children: set[tuple[type, int]] = set()
        self._materialized: dict[int, o6.NodeId] = {}
        self._completed_roots: set[int] = set()
        self._publishing = False

    def publish(self) -> None:
        if self._publishing:
            raise RuntimeError(
                f"Namespace {self._inventory.module.__name__} is already being published"
            )
        self._publishing = True
        try:
            self._inventory = _NamespaceInventory(self._inventory.module)
            self._inject_referencetype_markers()
            self._inject_datatype_markers()
            self._inject_datatype_children()
            self._inject_variabletype_markers()
            self._inject_objecttype_markers()
            self._inject_type_interfaces()
            self._inject_instances()
            self._inject_type_references()
            _materialize_instance_references(
                self._server,
                [
                    child
                    for marker in self._inventory.values
                    if isinstance(marker, type)
                    and isinstance(
                        declaration := vars(marker).get("__o6_declaration__"), TypeDeclaration
                    )
                    for child in declaration.instances
                ],
            )
        finally:
            self._publishing = False

    def _create_type(self, marker: type, create: Callable[[], Any]) -> None:
        if marker not in self._created_types:
            self._server._on_event_loop(create)
            self._created_types.add(marker)

    def _inject_datatype_children(self) -> None:
        for value in self._inventory.values:
            if not isinstance(value, type):
                continue
            declaration = vars(value).get("__o6_declaration__")
            if (
                isinstance(declaration, TypeDeclaration)
                and isinstance(declaration.attributes, (DataTypeSpec, EnumTypeSpec))
                and declaration.instances
            ):
                self._inject_type_children(value)

    def _inject_datatype_markers(self) -> None:
        if self._inventory.module is ns0:
            return
        markers = self._inventory.for_nodeclass(ns0.datatypes.NodeClass.DATA_TYPE)
        for marker in markers:
            declaration = _type_declaration(marker)
            spec = declaration.attributes
            assert isinstance(spec, (DataTypeSpec, EnumTypeSpec))
            parent = spec.parent or o6.NodeId(ns0.datatypes.BaseDataType)
            node_attrs = ns0.datatypes.DataTypeAttributes()
            node_attrs.displayName = o6.LocalizedText(declaration.displayname)
            node_attrs.isAbstract = bool(spec.is_abstract)
            try:
                self._create_type(
                    marker,
                    partial(
                        self._server._add_data_type_node,
                        declaration.nodeid,
                        parent,
                        o6.NodeId(ns0.reftypes.HasSubtype),
                        o6.QualifiedName(declaration.browsename),
                        node_attrs,
                    ),
                )
            except o6.StatusCodeError as exc:
                _logger.debug("Skipping data type %s: %s", marker.__name__, exc)
            _apply_role_permissions(self._server, declaration.nodeid, declaration.role_permissions)

    def _inject_instances(self) -> None:
        if self._inventory.instances:
            _materialize_instances(
                self._server, self._inventory.instances, self._materialized, self._completed_roots
            )

    def _inject_referencetype_markers(self) -> None:
        markers = self._inventory.for_nodeclass(ns0.datatypes.NodeClass.REFERENCE_TYPE)
        if not markers:
            return
        nid_to_marker = {str(_type_declaration(marker).nodeid): marker for marker in markers}
        for marker_list in self._registered_reference_types().values():
            for marker in marker_list:
                nid_to_marker.setdefault(str(_type_declaration(marker).nodeid), marker)
        references_root = o6.NodeId("i=31")
        for marker in self._toposort_markers(markers, nid_to_marker):
            parent_nid = self._parent_nodeid_of(marker, references_root)
            declaration = _type_declaration(marker)
            spec = declaration.attributes
            assert isinstance(spec, ReferenceTypeSpec)
            node_attrs = ns0.datatypes.ReferenceTypeAttributes()
            node_attrs.displayName = o6.LocalizedText(declaration.displayname)
            node_attrs.isAbstract = bool(spec.is_abstract)
            node_attrs.symmetric = bool(spec.is_symmetric)
            if spec.inverse_name is not None:
                node_attrs.inverseName = spec.inverse_name
            try:
                self._create_type(
                    marker,
                    partial(
                        self._server._add_reference_type_node,
                        declaration.nodeid,
                        parent_nid,
                        o6.NodeId(ns0.reftypes.HasSubtype),
                        o6.QualifiedName(declaration.browsename),
                        node_attrs,
                    ),
                )
            except o6.StatusCodeError as exc:
                _logger.debug("Skipping reference type %s: %s", marker.__name__, exc)
            _apply_role_permissions(self._server, declaration.nodeid, declaration.role_permissions)

    def _inject_variabletype_markers(self) -> None:
        markers = self._ordered_markers(
            ns0.datatypes.NodeClass.VARIABLE_TYPE, _is_variabletype_base
        )
        if not markers:
            return
        created: list[type] = []
        for marker in markers:
            declaration = _type_declaration(marker)
            spec = declaration.attributes
            assert isinstance(spec, VariableTypeSpec)
            parent = self._parent_nodeid_of(
                marker, o6.NodeId(ns0.vartypes.BaseVariableType), _is_variabletype_base
            )
            node_attrs = ns0.datatypes.VariableTypeAttributes()
            node_attrs.displayName = o6.LocalizedText(declaration.displayname)
            node_attrs.dataType = spec.data_type
            node_attrs.valueRank = spec.value_rank
            node_attrs.isAbstract = bool(spec.is_abstract)
            if spec.array_dimensions:
                node_attrs.arrayDimensions = [o6.UInt32(value) for value in spec.array_dimensions]
            elif spec.value_rank >= 1:
                node_attrs.arrayDimensions = [o6.UInt32(0)] * spec.value_rank
            if spec.value is not None:
                from o6.util import _coerce_builtin_value

                node_attrs.value = _coerce_builtin_value(spec.data_type, spec.value)
            try:
                self._create_type(
                    marker,
                    partial(
                        self._server._add_variable_type_node,
                        declaration.nodeid,
                        parent,
                        o6.NodeId(ns0.reftypes.HasSubtype),
                        o6.QualifiedName(declaration.browsename),
                        o6.NodeId(),
                        node_attrs,
                    ),
                )
            except o6.StatusCodeError as exc:
                exc.add_note(
                    f"while materializing VariableType {marker.__name__!r} "
                    f"({declaration.nodeid})"
                )
                raise
            self._server._attach_instance_type(marker, VariableNode)
            _apply_role_permissions(self._server, declaration.nodeid, declaration.role_permissions)
            created.append(marker)
        for marker in created:
            self._inject_type_children(marker)

    def _inject_objecttype_markers(self) -> None:
        markers = self._ordered_markers(ns0.datatypes.NodeClass.OBJECT_TYPE, _is_objecttype_base)
        if not markers:
            return
        created: list[type] = []
        for marker in markers:
            declaration = _type_declaration(marker)
            spec = declaration.attributes
            assert isinstance(spec, ObjectTypeSpec)
            parent = self._parent_nodeid_of(
                marker, o6.NodeId(ns0.objtypes.BaseObjectType), _is_objecttype_base
            )
            node_attrs = ns0.datatypes.ObjectTypeAttributes()
            node_attrs.displayName = o6.LocalizedText(declaration.displayname)
            node_attrs.isAbstract = bool(spec.is_abstract)
            try:
                self._create_type(
                    marker,
                    partial(
                        self._server._add_object_type_node,
                        declaration.nodeid,
                        parent,
                        o6.NodeId(ns0.reftypes.HasSubtype),
                        o6.QualifiedName(declaration.browsename),
                        node_attrs,
                    ),
                )
            except o6.StatusCodeError as exc:
                exc.add_note(
                    f"while materializing ObjectType {marker.__name__!r} " f"({declaration.nodeid})"
                )
                raise
            _apply_role_permissions(self._server, declaration.nodeid, declaration.role_permissions)
            created.append(marker)
        for marker in created:
            self._inject_type_children(marker)

    def _inject_type_interfaces(self) -> None:
        for marker in self._inventory.values:
            if not isinstance(marker, type):
                continue
            declaration = vars(marker).get("__o6_declaration__")
            if not isinstance(declaration, TypeDeclaration):
                continue
            for interface in declaration.interfaces:
                try:
                    self._server._add_reference_once(
                        declaration.nodeid,
                        o6.NodeId(interface),
                        o6.NodeId(ns0.reftypes.HasInterface),
                    )
                except o6.StatusCodeError as exc:
                    _logger.debug(
                        "Skipping interface %s on %s: %s", interface, marker.__name__, exc
                    )

    def _inject_type_references(self) -> None:
        for marker in self._inventory.values:
            if not isinstance(marker, type):
                continue
            declaration = vars(marker).get("__o6_declaration__")
            if not isinstance(declaration, TypeDeclaration):
                continue
            for reference in declaration.references:
                target_id: Any = _declaration_nodeid(reference.target)
                if target_id is None:
                    target_id = reference.target
                try:
                    self._server._add_reference_once(
                        declaration.nodeid,
                        target_id,
                        reference.reference_type,
                        forward=not reference.inverse,
                    )
                except o6.StatusCodeError as exc:
                    _logger.debug(
                        "Skipping reference on %s to %s: %s", marker.__name__, target_id, exc
                    )

    def _inject_type_children(self, marker: type) -> None:
        for child in _type_declaration(marker).instances:
            key = (marker, id(child))
            if key in self._created_children:
                continue
            try:
                with _temporarily_concrete(self._server, _template_abstract_types(child)):
                    _server_construction._construct_type_child(self._server, marker, child)
                self._created_children.add(key)
            except o6.StatusCodeError as exc:
                _logger.debug(
                    "Skipping type child %s.%s: %s", marker.__name__, child.browsename, exc
                )

    def _registered_reference_types(self) -> dict[str, list[type]]:
        out: dict[str, list[type]] = {}
        seen: set[type] = set()
        for module in [*self._nodeset_modules, self._inventory.module]:
            shortnames = [info.shortname for info in getattr(module, "__NAMESPACES__", ())]
            if not shortnames:
                shortnames = [module.__name__]
            inventory = _NamespaceInventory(module)
            for marker in inventory.for_nodeclass(ns0.datatypes.NodeClass.REFERENCE_TYPE):
                if marker in seen:
                    continue
                seen.add(marker)
                for shortname in shortnames:
                    out.setdefault(shortname, []).append(marker)
        return out

    def _ordered_markers(
        self,
        nodeclass: Any,
        base_pred: Callable[[type], bool],
    ) -> list[type]:
        markers = self._inventory.for_nodeclass(nodeclass)
        lookup = {str(_type_declaration(marker).nodeid): marker for marker in markers}
        return self._toposort_markers(markers, lookup, base_pred)

    def _toposort_markers(
        self,
        markers: list[type],
        nid_to_marker: dict[str, type],
        base_pred: Callable[[type], bool] = _is_referencetype_base,
    ) -> list[type]:
        marker_set = set(markers)
        prerequisites: dict[type, set[type]] = {}
        for marker in markers:
            dependencies: set[type] = set()
            parent = self._declared_parent(marker, nid_to_marker, base_pred)
            if parent is not None:
                dependencies.add(parent)
            declaration = _type_declaration(marker)
            for child in declaration.instances:
                dependency = nid_to_marker.get(str(_type_target_nodeid(child.typeTarget)))
                if dependency is not None and dependency is not marker:
                    dependencies.add(dependency)
            prerequisites[marker] = dependencies
        emitted: set[type] = set()
        ordered: list[type] = []
        while len(emitted) < len(markers):
            progress = False
            for marker in markers:
                if marker in emitted:
                    continue
                if all(dep not in marker_set or dep in emitted for dep in prerequisites[marker]):
                    ordered.append(marker)
                    emitted.add(marker)
                    progress = True
            if not progress:
                marker = next(candidate for candidate in markers if candidate not in emitted)
                ordered.append(marker)
                emitted.add(marker)
        return ordered

    def _declared_parent(
        self,
        marker: type,
        nid_to_marker: dict[str, type],
        base_pred: Callable[[type], bool] = _is_referencetype_base,
    ) -> type | None:
        for base in marker.__mro__[1:]:
            if base_pred(base) and str(_type_declaration(base).nodeid) in nid_to_marker:
                return base
        return None

    def _parent_nodeid_of(
        self,
        marker: type,
        fallback: o6.NodeId,
        base_pred: Callable[[type], bool] = _is_referencetype_base,
    ) -> o6.NodeId:
        return next(
            (_type_declaration(base).nodeid for base in marker.__mro__[1:] if base_pred(base)),
            fallback,
        )


def _template_abstract_types(root: InstanceDeclaration) -> set[o6.NodeId]:
    """Type declarations may contain placeholders with abstract TypeDefinitions."""
    found: set[o6.NodeId] = set()
    pending = [root]
    seen: set[int] = set()
    while pending:
        child = pending.pop()
        if id(child) in seen:
            continue
        seen.add(id(child))
        pending.extend(child.children)
        if isinstance(child.typeTarget, type):
            for marker in child.typeTarget.__mro__:
                declaration = vars(marker).get("__o6_declaration__")
                if isinstance(declaration, TypeDeclaration) and declaration.is_abstract:
                    found.add(declaration.nodeid)
    return found


def _materialize_instances(
    server: o6.Server,
    instances: list[Any],
    materialized: dict[int, o6.NodeId] | None = None,
    completed_roots: set[int] | None = None,
) -> None:
    """Materialize the registered roots of a namespace in *server*."""
    roots = list(
        {
            id(declaration): declaration
            for instance in instances
            for declaration in (_instance_declaration(instance),)
        }.values()
    )
    declarations: list[InstanceDeclaration] = []
    pending = list(roots)
    seen_declarations: set[int] = set()
    while pending:
        declaration = pending.pop()
        if id(declaration) in seen_declarations:
            continue
        seen_declarations.add(id(declaration))
        declarations.append(declaration)
        pending.extend(declaration.children)

    if materialized is None:
        materialized = {}
    if completed_roots is None:
        completed_roots = set()
    materialized_roots: list[Any] = []
    children_by_parent: dict[str, list[Any]] = {}
    for declaration in declarations:
        parent = declaration.parent
        if parent is not None:
            children_by_parent.setdefault(str(parent), []).append(declaration)

    def abstract_mandatory_types(type_nodeid: Any) -> set[o6.NodeId]:
        found: set[o6.NodeId] = set()
        pending = [str(type_nodeid)]
        seen_parents: set[str] = set()
        while pending:
            parent_id = pending.pop()
            if parent_id in seen_parents:
                continue
            seen_parents.add(parent_id)
            for child in children_by_parent.get(parent_id, ()):
                if child.modelling_rule is None or _resolved_modelling_rule(
                    child.modelling_rule
                ) != o6.NodeId("i=78"):
                    continue
                marker = child.typeTarget if isinstance(child.typeTarget, type) else None
                type_declaration = (
                    vars(marker).get("__o6_declaration__") if isinstance(marker, type) else None
                )
                if isinstance(type_declaration, TypeDeclaration) and type_declaration.is_abstract:
                    found.add(type_declaration.nodeid)
                child_nodeid = child.nodeid
                if child_nodeid is not None:
                    pending.append(str(child_nodeid))
        return found

    def nested_abstract_bases(declaration: Any) -> set[o6.NodeId]:
        """Abstract bases temporarily crossed by explicit concrete children.

        open62541 completes inherited Mandatory children before applying a
        subtype's concrete override.  A generated ``references=[...]`` tree
        supplies that override explicitly, so permit construction through its
        abstract base only for the duration of the enclosing instance add.
        """
        found: set[o6.NodeId] = set()
        pending = list(declaration.children)
        seen: set[int] = set()
        while pending:
            child = pending.pop()
            if id(child) in seen:
                continue
            seen.add(id(child))
            marker = child.typeTarget if isinstance(child.typeTarget, type) else None
            if isinstance(marker, type):
                for base in marker.__mro__[1:]:
                    type_declaration = vars(base).get("__o6_declaration__")
                    if (
                        isinstance(type_declaration, TypeDeclaration)
                        and type_declaration.is_abstract
                    ):
                        found.add(type_declaration.nodeid)
            pending.extend(child.children)
        return found

    for declaration in roots:
        materialized_roots.append(declaration)
        if id(declaration) in completed_roots:
            continue
        parent = declaration.parent
        is_root = parent is None
        browse_name = declaration.browsename
        parent_nid: o6.NodeIdLike
        if parent is None:
            # AddNodes requires a hierarchical construction parent. Remove this
            # temporary Organizes edge immediately after the node is finished.
            parent_nid = o6.NodeId(_OBJECTS_FOLDER)
        else:
            parent_nid = o6.NodeId(parent)

        marker = declaration.typeTarget if isinstance(declaration.typeTarget, type) else None
        type_declaration = (
            vars(marker).get("__o6_declaration__") if isinstance(marker, type) else None
        )
        relaxed_types = (
            abstract_mandatory_types(type_declaration.nodeid)
            if isinstance(type_declaration, TypeDeclaration)
            else set()
        )
        relaxed_types.update(nested_abstract_bases(declaration))
        if id(declaration) in materialized:
            live = materialized[id(declaration)]
        else:
            attempt: dict[int, o6.NodeId] = {}
            with _temporarily_concrete(server, relaxed_types):
                try:
                    if is_root:
                        live = _construct_declaration(
                            server,
                            parent_nid,
                            declaration,
                            attempt,
                            o6.NodeId(_ORGANIZES),
                        )
                    else:
                        live = _construct_declaration(server, parent_nid, declaration, attempt)
                except Exception as exc:
                    exc.add_note(
                        f"while materializing declared instance {browse_name!r} "
                        f"({declaration.nodeid})"
                    )
                    raise
            materialized.update(attempt)
        if is_root and not isinstance(declaration.attributes, MethodSpec):
            server.deleteReferenceLegacy(
                o6.NodeId(_OBJECTS_FOLDER),
                getattr(live, "nodeId", live),
                o6.NodeId(_ORGANIZES),
            )

        completed_roots.add(id(declaration))

    _materialize_instance_references(server, materialized_roots, materialized)


def _materialize_instance_references(
    server: o6.Server,
    declarations: list[InstanceDeclaration],
    materialized: dict[int, o6.NodeId] | None = None,
) -> None:
    """Add explicit edges after their owning declaration trees are published."""
    materialized = materialized or {}
    pending = list(declarations)
    seen: set[int] = set()
    while pending:
        declaration = pending.pop()
        if id(declaration) in seen:
            continue
        seen.add(id(declaration))
        pending.extend(declaration.children)
        source: Any = materialized.get(id(declaration))
        if source is None:
            source = _declaration_nodeid(declaration)
        if source is None:
            continue
        for reference in declaration.references:
            target = reference.target
            try:
                target_declaration: Any = _instance_declaration(target)
            except TypeError:
                target_declaration = target
            target_id: Any = materialized.get(id(target_declaration))
            if target_id is None:
                raw_target: Any = _declaration_nodeid(target)
                if raw_target is None:
                    raw_target = target
                target_id = (
                    raw_target
                    if isinstance(raw_target, o6.ExpandedNodeId)
                    else o6.NodeId(raw_target)
                )
            try:
                server._add_reference_once(
                    source,
                    target_id,
                    reference.reference_type,
                    forward=not reference.inverse,
                )
            except Exception as exc:
                exc.add_note(
                    f"while adding reference {source} --[{reference.reference_type}]--> "
                    f"{target_id} (inverse={reference.inverse})"
                )
                raise
