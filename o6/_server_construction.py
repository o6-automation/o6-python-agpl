# Copyright 2026 (c) o6 Automation GmbH
"""Construction of live Python-backed server nodes and declaration subtrees."""

from __future__ import annotations

import inspect
import re
from collections.abc import Mapping
from dataclasses import replace as dataclass_replace
from typing import Any, Callable, Optional, cast

import o6
from o6._declarations import (
    InstanceDeclaration,
    MethodSpec,
    ObjectSpec,
    ObjectTypeSpec,
    TypeDeclaration,
    VariableSpec,
    VariableTypeSpec,
    ViewSpec,
    _HAS_COMPONENT,
    _CallbackKind,
    _MemberPathTarget,
    _NodeClass,
    _TYPE_TO_INSTANCE,
    _browse_name_key,
    _child_declarations_by_key,
    _declaration_values,
    _instance_kind,
    _instance_declaration,
    _instance_node_type,
    _is_node_declaration,
    _type_declaration,
    _type_target_nodeid,
    _modelling_rule_nodeid,
    _resolved_modelling_rule,
    _namespace_index,
    _normalize_role_permissions,
)
from o6._server_types import (
    _effective_method_slots,
    _live_class,
    _live_implementation_type,
    _member_callback_slots,
    _member_resolutions,
    _python_node_implementation,
    _resolved_callback,
    _variable_callbacks,
)
from o6.util import _coerce_builtin_value

_UNSET = object()
_INITIALIZER_KWARGS = "_o6InitializerKwargs"


def _variable_callback_plan(
    server: Any, node: Any, type_id: Any
) -> list[tuple[Any, _CallbackKind, Callable[..., Any] | None, None]]:
    """Return the VariableType callbacks copied onto one concrete Variable."""
    read, write = _variable_callbacks(server, type_id, type(node))
    if read is None and write is None:
        return []
    return [(node, "read", read, None), (node, "write", write, None)]


def _python_node_lifecycle(
    server: Any,
    node_id: Any,
    type_id: Any,
    native_node: Any,
    node_class: int,
    early: bool,
) -> None:
    """Run the explicit early or final Python phase of native AddNodes."""
    from o6._node_backend import _server_node
    from o6.node import VariableNode
    from o6.ns import ns0

    if node_class not in (
        int(ns0.datatypes.NodeClass.VARIABLE),
        int(ns0.datatypes.NodeClass.OBJECT),
    ):
        return
    selected = _python_node_implementation(server, node_id, type_id, native_node, node_class)
    if early:
        if selected is not None:
            _prepare_implementation_children(server, *selected)
        return
    if selected is None:
        if node_class == int(ns0.datatypes.NodeClass.VARIABLE):
            node = native_node or _server_node(server, o6.NodeId(node_id), VariableNode)
            _install_callback_plan(server, _variable_callback_plan(server, node, type_id))
        return
    node, concrete = selected
    initializer_kwargs = node.__dict__.pop(_INITIALIZER_KWARGS, {})
    _invoke_initializer(node, concrete, initializer_kwargs)
    _finish_implementation_callbacks(server, node, concrete, type_id)


def _browse_children(server: Any, node: Any) -> dict[tuple[int, str, int], Any]:
    """Index direct hierarchical children once for construction-time resolution."""
    from o6.ns import ns0

    mask = int(
        ns0.datatypes.BrowseResultMask.BROWSE_NAME | ns0.datatypes.BrowseResultMask.NODE_CLASS
    )
    result = server.browse(node, resultMask=ns0.datatypes.BrowseResultMask(mask))
    references = result.references
    return {
        (
            reference.browseName.ns.index,
            reference.browseName.name,
            int(reference.nodeClass),
        ): reference.nodeId
        for reference in references
    }


def _resolve_member_node(
    server: Any,
    node: Any,
    klass: type,
    path: _MemberPathTarget,
    expected: type,
    child_cache: dict[Any, dict[tuple[int, str, int], Any]],
    member_cache: dict[type, Any],
) -> Any:
    """Resolve a declared Python member path once during construction."""
    from o6.node import Node

    current = node
    current_type = klass
    parts = path.members
    for index, member_name in enumerate(parts):
        live_type = _live_implementation_type(type(current))
        if isinstance(live_type, type):
            current_type = live_type
        members = member_cache.get(current_type)
        if members is None:
            members = _member_resolutions(current_type)
            member_cache[current_type] = members
        member = members.get(member_name)
        if member is None:
            raise TypeError(
                f"{klass.__qualname__} callback target {path.path!r} has no Python "
                f"member {member_name!r} on {current_type.__qualname__}"
            )
        declaration = member.declaration
        current_id = o6.NodeId(current)
        children = child_cache.get(current_id)
        if children is None:
            children = _browse_children(server, current)
            child_cache[current_id] = children
        child_id = children.get(
            (
                *_browse_name_key(declaration.browsename),
                int(declaration.nodeclass),
            )
        )
        if child_id is None:
            raise TypeError(
                f"{klass.__qualname__} callback target {path.path!r} is not instantiated"
            )
        declared_marker = (
            declaration.typeTarget if isinstance(declaration.typeTarget, type) else None
        )
        marker = member.implementation_type or declared_marker
        if index + 1 == len(parts):
            expected_nodeclass = (
                int(_NodeClass.METHOD)
                if expected.__name__ == "MethodNode"
                else int(_NodeClass.VARIABLE)
            )
            if int(declaration.nodeclass) != expected_nodeclass:
                kind = "Method" if expected.__name__ == "MethodNode" else "Variable"
                raise TypeError(
                    f"{klass.__qualname__} callback target {path.path!r} is not a {kind}"
                )
            child_type = expected
        elif marker is not None:
            type_declaration = _type_declaration(marker)
            child_type = _live_class(marker, _instance_node_type(type_declaration.nodeclass))
        else:
            raise TypeError(
                f"{klass.__qualname__} callback target {path.path!r} traverses leaf "
                f"member {member_name!r}"
            )
        child = node._backend.dispatch(node._backend.node_get(child_id, child_type))
        if not isinstance(child, Node):
            raise RuntimeError("callback target resolution must be synchronous")
        if child._construction_owner is None:
            child._construction_owner = current
        current = child
        if index + 1 == len(parts):
            break
        assert marker is not None
        current_type = marker
    if not isinstance(current, expected):
        kind = "Method" if expected.__name__ == "MethodNode" else "Variable"
        raise TypeError(f"{klass.__qualname__} callback target {path.path!r} is not a {kind}")
    return current


def _prepare_implementation_children(server: Any, node: Any, klass: type) -> None:
    """Materialize and promote implementation-selected direct children."""
    from o6.node import Node

    members = _member_resolutions(klass)
    selections = {
        name: member for name, member in members.items() if member.implementation_type is not None
    }
    children = _browse_children(server, node) if selections else {}

    for member_name, member in selections.items():
        implementation = cast(type, member.implementation_type)
        optional = member.optional
        declaration = member.declaration
        implementation_declaration = _type_declaration(implementation)
        child_type = _live_class(
            implementation, _instance_node_type(implementation_declaration.nodeclass)
        )
        child_id = children.get(
            (
                *_browse_name_key(declaration.browsename),
                int(declaration.nodeclass),
            )
        )
        initialized = False
        if child_id is None:
            if optional:
                continue
            raw_value: Any = {} if isinstance(declaration.typeTarget, type) else None
            created = _precreate_children(
                server,
                o6.NodeId(node),
                klass,
                {declaration.browsename: raw_value},
                implementation_types={member_name: implementation},
            )
            initialized = True
            child_id = o6.NodeId(created[declaration.browsename])
            children[
                (
                    *_browse_name_key(declaration.browsename),
                    int(declaration.nodeclass),
                )
            ] = child_id
        child = node._backend.dispatch(node._backend.node_get(child_id, child_type))
        if not isinstance(child, Node):
            raise RuntimeError("member implementation initialization must be synchronous")
        if child._construction_owner is None:
            child._construction_owner = node
        if not initialized:
            _prepare_implementation_children(server, child, implementation)
            _invoke_initializer(child, implementation, {})
            _finish_implementation_callbacks(
                server, child, implementation, implementation_declaration.nodeid
            )


def _owner_callback_plan(
    server: Any,
    owner: Any,
    klass: type,
    child_cache: dict[Any, dict[tuple[int, str, int], Any]],
    member_cache: dict[type, Any],
    *,
    target_filter: Any | None = None,
    include_direct_methods: bool = True,
    ignore_missing_paths: bool = False,
) -> list[tuple[Any, _CallbackKind, Callable[..., Any] | None, Any | None]]:
    """Resolve callbacks contributed by one implementation owner."""
    from o6.node import MethodNode, Node, VariableNode

    members = member_cache.get(klass)
    if members is None:
        members = _member_resolutions(klass)
        member_cache[klass] = members
    has_methods = include_direct_methods and any(
        int(member.declaration.nodeclass) == int(_NodeClass.METHOD) for member in members.values()
    )
    member_callbacks = _member_callback_slots(klass)
    if has_methods or member_callbacks:
        owner_id = o6.NodeId(owner)
        children = child_cache.get(owner_id)
        if children is None:
            children = _browse_children(server, owner)
            child_cache[owner_id] = children
    else:
        children = {}

    callbacks: list[tuple[Any, _CallbackKind, Callable[..., Any] | None, Any | None]] = []
    method_slots = _effective_method_slots(klass)
    if include_direct_methods:
        for member in members.values():
            declaration = member.declaration
            if int(declaration.nodeclass) != int(_NodeClass.METHOD):
                continue
            method_id = children.get(
                (*_browse_name_key(declaration.browsename), int(_NodeClass.METHOD))
            )
            if method_id is None:
                continue
            target = owner._backend.dispatch(owner._backend.node_get(method_id, MethodNode))
            if not isinstance(target, Node):
                raise RuntimeError("Method callback initialization must be synchronous")
            if target._construction_owner is None:
                target._construction_owner = owner
            if target_filter is not None and o6.NodeId(target) != o6.NodeId(target_filter):
                continue
            slot = method_slots.get(_browse_name_key(declaration.browsename))
            callback = None if slot is None else _resolved_callback(klass, slot, "call")
            callbacks.append((target, "call", callback, None))

    paths_by_target: dict[tuple[Any, str], str] = {}
    for (kind, path), slot in member_callbacks.items():
        try:
            expected = MethodNode if kind == "call" else VariableNode
            target = _resolve_member_node(
                server, owner, klass, path, expected, child_cache, member_cache
            )
        except TypeError as exc:
            if ignore_missing_paths and "is not instantiated" in str(exc):
                continue
            exc.add_note(f"from @o6.{kind}({path.path!r})")
            raise
        if target_filter is not None and o6.NodeId(target) != o6.NodeId(target_filter):
            continue
        target_key = o6.NodeId(target), kind
        previous = paths_by_target.get(target_key)
        if previous is not None and previous != path.path:
            raise TypeError(
                f"{klass.__qualname__} paths {previous!r} and {path.path!r} target the "
                f"same Variable {target._nodeid} for {kind}"
            )
        paths_by_target[target_key] = path.path
        callback = _resolved_callback(klass, slot, kind)
        if kind != "call" and inspect.iscoroutinefunction(callback):
            raise TypeError("Variable callbacks cannot be async")
        callbacks.append((target, kind, callback, owner))

    # Reads go first so a paired write sees the concrete read slot regardless
    # of decorator declaration order.
    callbacks.sort(key=lambda item: item[1] != "read")
    return callbacks


def _install_callback_plan(
    server: Any,
    callbacks: list[tuple[Any, _CallbackKind, Callable[..., Any] | None, Any | None]],
) -> None:
    """Install a resolved construction plan in dependency order."""
    for target, kind, callback, receiver in callbacks:
        if kind == "write" and server._node_callback(target, "read") is None:
            raise TypeError("a callback-backed Variable requires a read callback")
        server._set_node_callback(target, kind, callback, receiver)


def _finish_implementation_callbacks(server: Any, node: Any, klass: type, type_id: Any) -> None:
    """Resolve concrete callback slots after native child construction."""
    from o6.node import VariableNode

    callbacks = (
        _variable_callback_plan(server, node, type_id) if isinstance(node, VariableNode) else []
    )
    callbacks.extend(_owner_callback_plan(server, node, klass, {}, {}))
    _install_callback_plan(server, callbacks)


def _restore_construction_callbacks(server: Any, target: Any) -> None:
    """Replay the callback resolution that applied when *target* was created."""
    from o6.node import MethodNode, Node, VariableNode

    callbacks: dict[str, tuple[Callable[..., Any] | None, Node | None]] = {}
    if isinstance(target, VariableNode):
        type_id = server._get_node_type(o6.NodeId(target))
        read, write = _variable_callbacks(server, type_id, type(target))
        callbacks.update(read=(read, None), write=(write, None))
    elif not isinstance(target, MethodNode):
        raise TypeError("only concrete Variables and Methods have construction callbacks")

    owner = target._construction_owner
    direct_method = True
    child_cache: dict[Any, dict[tuple[int, str, int], Any]] = {}
    member_cache: dict[type, Any] = {}
    while isinstance(owner, Node):
        klass = _live_implementation_type(type(owner))
        if not isinstance(klass, type):
            break
        for _, kind, callback, receiver in _owner_callback_plan(
            server,
            owner,
            klass,
            child_cache,
            member_cache,
            target_filter=target,
            include_direct_methods=direct_method,
            ignore_missing_paths=True,
        ):
            callbacks[kind] = callback, receiver

        direct_method = False
        owner = owner._construction_owner

    if isinstance(target, MethodNode):
        callback, receiver = callbacks.get("call", (None, None))
        server._set_node_callback(target, "call", callback, receiver)
        return

    read, read_receiver = callbacks.get("read", (None, None))
    write, write_receiver = callbacks.get("write", (None, None))
    if read is None:
        raise TypeError(
            "this Variable was constructed with native storage; "
            "use implement(variable, value) to restore it"
        )
    server._set_node_callback(target, "read", read, read_receiver)
    server._set_node_callback(target, "write", write, write_receiver)


def _invoke_initializer(node: Any, klass: type, kwargs: Mapping[str, Any]) -> None:
    """Invoke an implementation initializer with normal Python return checks."""
    result = getattr(klass, "__init__", object.__init__)(node, **kwargs)
    if result is not None:
        raise TypeError(f"__init__() should return None, not {type(result).__name__!r}")


def _delete_live_node(server: Any, node: Any) -> None:
    """Best-effort rollback for a partially constructed live node."""
    if node._is_native_attached():
        try:
            server.deleteNode(o6.NodeId(node))
        except Exception:
            pass


def _build_node_attrs(
    nodeclass: _NodeClass,
    *,
    displayname: str,
    data_type: Any = None,
    value_rank: int = -1,
    array_dimensions: Optional[list[int]] = None,
    value: Any = None,
    access_level: Optional[int] = None,
    user_access_level: Optional[int] = None,
    minimum_sampling_interval: Optional[float] = None,
    historizing: bool = False,
    description: Optional[str] = None,
    writemask: Optional[int] = None,
    user_writemask: Optional[int] = None,
    event_notifier: int = 0,
) -> Any:
    from o6.ns import ns0

    if nodeclass == _NodeClass.OBJECT:
        attributes: Any = ns0.datatypes.ObjectAttributes()
        attributes.eventNotifier = event_notifier
    elif nodeclass == _NodeClass.VARIABLE:
        attributes = ns0.datatypes.VariableAttributes()
        attributes.dataType = data_type
        attributes.valueRank = value_rank
        attributes.accessLevel = access_level if access_level is not None else o6.AccessLevel.READ
        attributes.userAccessLevel = (
            user_access_level if user_access_level is not None else attributes.accessLevel
        )
        attributes.historizing = historizing
        if minimum_sampling_interval is not None:
            attributes.minimumSamplingInterval = minimum_sampling_interval
        if array_dimensions is not None:
            attributes.arrayDimensions = [o6.UInt32(item) for item in array_dimensions]
        elif value_rank >= 1:
            attributes.arrayDimensions = [o6.UInt32(0)] * value_rank
        is_empty_array = isinstance(value, (list, tuple)) and not value
        if value is not None and not is_empty_array:
            attributes.value = _coerce_builtin_value(data_type, value)
    else:
        raise NotImplementedError(f"no attributes for {_NodeClass(nodeclass)!r}")
    attributes.displayName = o6.LocalizedText(displayname)
    if description is not None:
        attributes.description = o6.LocalizedText(description)
    if writemask is not None:
        attributes.writeMask = writemask
    if user_writemask is not None:
        attributes.userWriteMask = user_writemask
    return attributes


def _child_attrs(decl: InstanceDeclaration, value: Any) -> Any:
    if isinstance(decl.attributes, ObjectSpec):
        return _build_node_attrs(
            decl.nodeclass,
            displayname=decl.displayname or decl.browsename,
            event_notifier=decl.attributes.event_notifier,
            description=decl.description,
            writemask=decl.writemask,
            user_writemask=decl.user_writemask,
        )
    if not isinstance(decl.attributes, VariableSpec):
        raise TypeError(f"{decl.browsename!r} is not an Object or Variable declaration")
    spec = decl.attributes
    return _build_node_attrs(
        decl.nodeclass,
        displayname=decl.displayname or decl.browsename,
        data_type=spec.data_type,
        value_rank=spec.value_rank,
        array_dimensions=spec.array_dimensions,
        value=value if value is not None else spec.value,
        access_level=spec.access_level,
        user_access_level=spec.user_access_level,
        minimum_sampling_interval=spec.minimum_sampling_interval,
        historizing=spec.historizing,
        description=decl.description,
        writemask=decl.writemask,
        user_writemask=decl.user_writemask,
    )


def _apply_role_permissions(server: Any, node_id: Any, permissions: Mapping[Any, int]) -> None:
    if permissions:
        server._on_event_loop(
            lambda: server._set_node_role_permissions(node_id, permissions, False)
        )


def _construct_live_child(
    server: o6.Server,
    parent: o6.NodeIdLike,
    declaration: InstanceDeclaration,
    marker: type,
    requested: o6.NodeId,
    browse_name: o6.QualifiedName,
    attributes: Any,
    values: Mapping[str, Any] | None = None,
) -> Any:
    return _construct_live_node(
        marker,
        server,
        declaration.nodeclass,
        requested,
        browse_name,
        cast(Any, _type_target_nodeid(declaration.typeTarget)),
        attributes,
        o6.NodeId(parent),
        declaration.reference_type,
        initializer_kwargs={},
        values=values,
        role_permissions=declaration.role_permissions,
    )


def _precreate_children(
    server: o6.Server,
    parent_nid: o6.NodeIdLike,
    marker_cls: Optional[type],
    raw_values: dict[str, Any],
    *,
    implementation_types: Mapping[str, type] | None = None,
) -> dict[str, str]:
    """Pre-create children of *parent_nid* from *raw_values*,
    before the parent's finish phase (recursively).

    Each value may be a scalar, dict, node declaration, or an Optional Method
    selection. A COMPLEX child is created ``begin -> (recurse) -> finish`` so
    its own NodeId AND its descendants' NodeIds are preseeded; a LEAF uses a
    single native add. A declaration may preseed the child NodeId and value.
    ``finish`` on the parent then fills any Mandatory children not pre-created
    here (its ``copyChild`` dedups ours by BrowseName). Returns
    ``{browsename: nodeid str}`` of the top-level children created.
    """
    # Full child set incl. inherited (see _all_children): `values=` may name an
    # inherited child, and the recursion below also reaches a complex child whose
    # own type is a subtype with inherited children.
    decls = _child_declarations_by_key(marker_cls) if marker_cls is not None else {}
    created: dict[str, str] = {}
    for name, raw in raw_values.items():
        decl = decls.get(_browse_name_key(name))
        if decl is None and _is_node_declaration(raw):
            decl = _instance_declaration(raw)
        if decl is None:
            raise KeyError(f"{getattr(marker_cls, '__name__', '?')} has no child {name!r}")
        qn = o6.QualifiedName(decl.browsename)

        if int(decl.nodeclass) == int(_NodeClass.METHOD):
            mnid = _precreate_method_child(server, parent_nid, decl, qn, raw)
            created[name] = str(mnid)
            continue

        declared_marker = decl.typeTarget if isinstance(decl.typeTarget, type) else None
        if declared_marker is not None:
            # Complex child: begin -> pre-create its subtree -> finish.
            effective_decl = decl
            if _is_node_declaration(raw):
                declaration_value = _instance_declaration(raw)
                value_marker = (
                    declaration_value.typeTarget
                    if isinstance(declaration_value.typeTarget, type)
                    else None
                )
                if value_marker is None or not issubclass(value_marker, declared_marker):
                    if not declaration_value.allow_abstract:
                        raise TypeError(
                            f"complex child {name!r} expects {declared_marker.__name__}, "
                            f"got "
                            f"{getattr(value_marker, '__name__', 'declaration')}"
                        )
                payload = declaration_value.attributes
                cid = declaration_value.nodeid
                root_val = payload.value if isinstance(payload, VariableSpec) else None
                # Keep the public declaration object until its ordinary Python
                # attributes have been folded into the owned child records.
                sub = _declaration_values(raw)
                effective_decl = dataclass_replace(
                    declaration_value,
                    browsename=decl.browsename,
                    python_name=decl.python_name,
                    reference_type=decl.reference_type,
                    inverse=decl.inverse,
                    modelling_rule=None,
                    parent=None,
                )
            elif isinstance(raw, dict):
                cid, root_val, sub = None, None, raw
            else:
                raise TypeError(
                    f"complex child {name!r} needs a {declared_marker.__name__} "
                    f"declaration or a dict of values, got {type(raw).__name__}"
                )
            req = o6.NodeId(cid) if cid is not None else o6.NodeId()
            try:
                attr = _child_attrs(effective_decl, root_val)
            except (TypeError, ValueError) as exc:
                exc.add_note(f"while building declared child {name!r} below {parent_nid}")
                raise
            effective_marker = (
                effective_decl.typeTarget
                if isinstance(effective_decl.typeTarget, type)
                else declared_marker
            )
            child_marker = (implementation_types or {}).get(
                decl.python_name or "", effective_marker
            )
            child = _construct_live_child(
                server, parent_nid, effective_decl, child_marker, req, qn, attr, sub
            )
            cnid = o6.NodeId(child)
            created[name] = str(cnid)
        else:
            # Leaf child: one add carries its value + NodeId.
            if _is_node_declaration(raw):
                raw_declaration = _instance_declaration(raw)
                payload = raw_declaration.attributes
                if not isinstance(payload, VariableSpec):
                    raise TypeError(f"leaf child {name!r} expects a Variable declaration")
                lid, lval = raw_declaration.nodeid, payload.value
            elif isinstance(raw, dict):
                raise TypeError(f"leaf child {name!r} expects a scalar value, not a dict")
            else:
                lid, lval = None, raw
            req = o6.NodeId(lid) if lid is not None else o6.NodeId()
            attr = _child_attrs(decl, lval)
            leaf_marker = (implementation_types or {}).get(decl.python_name or "")
            if leaf_marker is None:
                child_id = _add_leaf_child(server, decl, req, o6.NodeId(parent_nid), qn, attr)
                _apply_role_permissions(server, child_id, decl.role_permissions)
            else:
                child = _construct_live_child(server, parent_nid, decl, leaf_marker, req, qn, attr)
                child_id = o6.NodeId(child)
            created[name] = str(child_id)
    return created


def _precreate_method_child(
    server: o6.Server,
    parent_nid: o6.NodeIdLike,
    decl: InstanceDeclaration,
    qn: o6.QualifiedName,
    selection: Any,
) -> Any:
    """Include an Optional Method as an independent instance node."""
    if _is_node_declaration(selection):
        decl = _instance_declaration(selection)
    elif selection is not None:
        raise TypeError(f"method child {decl.browsename!r} is enabled with None, not a value")
    method_id = _add_method_child(
        server,
        decl,
        o6.NodeId(),
        o6.NodeId(parent_nid),
        qn,
        declaration=False,
    )
    _apply_role_permissions(server, method_id, decl.role_permissions)
    return method_id


def _add_leaf_child(
    server: o6.Server,
    decl: InstanceDeclaration,
    req: o6.NodeId,
    parent: o6.NodeId,
    qn: o6.QualifiedName,
    attr: Any,
) -> Any:
    """Add a single leaf child of the node class ``decl.nodeclass`` (no children of its own)."""
    nc = int(decl.nodeclass)
    try:
        if nc == int(_NodeClass.VARIABLE):
            nodeid = server._on_event_loop(
                lambda: server._add_variable_node(
                    req,
                    parent,
                    decl.reference_type,
                    qn,
                    _type_target_nodeid(decl.typeTarget),
                    attr,
                )
            )
        elif nc == int(_NodeClass.OBJECT):
            nodeid = server._on_event_loop(
                lambda: server._add_object_node(
                    req,
                    parent,
                    decl.reference_type,
                    qn,
                    _type_target_nodeid(decl.typeTarget),
                    attr,
                )
            )
        else:
            raise NotImplementedError(
                f"unsupported child node class {_NodeClass(decl.nodeclass)!r} "
                f"for {decl.browsename!r}"
            )
    except (TypeError, o6.StatusCodeError) as exc:
        exc.add_note(
            f"while adding declared child {decl.browsename!r} "
            f"with TypeDefinition {_type_target_nodeid(decl.typeTarget)} below {parent}"
        )
        raise
    return nodeid


def _add_method_child(
    server: o6.Server,
    decl: InstanceDeclaration,
    req: o6.NodeId,
    parent: o6.NodeId,
    qn: o6.QualifiedName,
    *,
    declaration: bool = True,
) -> Any:
    """Add a Method instance-declaration child under *parent* via `add_method_node`.

    Methods are untyped (no TypeDefinition); the argument signature (`input_args` / `output_args`) and the executable flags come from *decl*.
    The declaration is added without behavior. `@o6.call` or
    `Server.implement` installs the generic Python dispatcher later.
    """
    from o6.ns import ns0

    if not isinstance(decl.attributes, MethodSpec):
        raise TypeError(f"{decl.browsename!r} is not a Method declaration")
    spec = decl.attributes
    attr = ns0.datatypes.MethodAttributes()
    attr.displayName = o6.LocalizedText(decl.displayname or decl.browsename)
    attr.executable = bool(spec.executable)
    attr.userExecutable = bool(spec.user_executable)
    if decl.description is not None:
        attr.description = o6.LocalizedText(decl.description)
    if decl.writemask is not None:
        attr.writeMask = decl.writemask
    if decl.user_writemask is not None:
        attr.userWriteMask = decl.user_writemask
    return server._on_event_loop(
        lambda: server._add_method_node(
            req,
            parent,
            decl.reference_type,
            qn,
            attr,
            list(spec.input_args),
            list(spec.output_args),
            (spec.input_args_nodeid or o6.NodeId()) if declaration else o6.NodeId(),
            (spec.output_args_nodeid or o6.NodeId()) if declaration else o6.NodeId(),
        )
    )


def _construct_type_child(server: Any, marker: type, child: InstanceDeclaration) -> Any:
    """Publish one instance-declaration child below a UA type node."""
    type_nodeid = _type_declaration(marker).nodeid
    return _construct_declaration(server, type_nodeid, child, template=True)


def _finish_live_instance(
    node: Any,
    marker: type,
    server: Any,
    parent: o6.NodeIdLike,
    reference_type: o6.NodeIdLike,
    type_definition: o6.NodeIdLike,
    *,
    values: Mapping[str, Any] | None = None,
    references: list[Any] | None = None,
    role_permissions: Mapping[Any, int] | None = None,
    modelling_rule: o6.NodeId | str | None = None,
    allow_abstract: bool = False,
) -> None:
    """Advance one promoted raw node through prepare and finish."""
    node_id = o6.NodeId(node)
    if allow_abstract:
        server._on_event_loop(lambda: server._set_type_abstract(type_definition, False))
    try:
        server._on_event_loop(
            lambda: server._add_node_prepare(
                node_id, o6.NodeId(parent), o6.NodeId(reference_type), type_definition
            )
        )
        if values:
            _precreate_children(
                server,
                node_id,
                marker,
                dict(values),
                implementation_types={
                    name: member.implementation_type
                    for name, member in _member_resolutions(marker).items()
                    if member.implementation_type is not None
                },
            )
        for reference in references or ():
            _construct_declaration(server, node_id, _instance_declaration(reference))
        server._on_event_loop(lambda: server._add_node_finish(node_id))
        permissions = _normalize_role_permissions(role_permissions)
        _apply_role_permissions(server, node_id, permissions)
        if modelling_rule is not None:
            rule = _resolved_modelling_rule(modelling_rule)
            server.addReference(node_id, rule, o6.NodeId("i=37"))
    finally:
        if allow_abstract:
            server._on_event_loop(lambda: server._set_type_abstract(type_definition, True))


def _construct_live_node(
    marker: type,
    server: Any,
    nodeclass: _NodeClass,
    requested: o6.NodeIdLike,
    browse_name: o6.QualifiedName,
    type_definition: o6.NodeIdLike,
    native_attrs: Any,
    parent: o6.NodeIdLike,
    reference_type: o6.NodeIdLike,
    *,
    initializer_kwargs: Mapping[str, Any],
    values: Mapping[str, Any] | None = None,
    references: list[Any] | None = None,
    role_permissions: Mapping[Any, int] | None = None,
    modelling_rule: o6.NodeId | str | None = None,
    allow_abstract: bool = False,
) -> Any:
    """Run the single raw-to-initialized live-node transaction."""
    target = _live_class(marker, _instance_node_type(_type_declaration(marker).nodeclass))
    node = server._on_event_loop(
        lambda: server._add_node_raw(
            int(nodeclass),
            requested,
            browse_name,
            type_definition,
            native_attrs,
            target,
            server._node_backend,
        )
    )
    node.__dict__[_INITIALIZER_KWARGS] = dict(initializer_kwargs)
    try:
        _finish_live_instance(
            node,
            marker,
            server,
            parent,
            reference_type,
            type_definition,
            values=values,
            references=references,
            role_permissions=role_permissions,
            modelling_rule=modelling_rule,
            allow_abstract=allow_abstract,
        )
    except BaseException:
        _delete_live_node(server, node)
        raise
    return node


def _new_live_instance(
    cls: type,
    server: Any,
    kwargs: Mapping[str, Any],
    initializer_kwargs: Mapping[str, Any],
) -> Any:
    """Create, finish, and return the one nodestore-backed Python object."""
    declaration = _type_declaration(cls)
    type_spec = declaration.attributes
    parent = kwargs.get("parent")
    if parent is None:
        raise TypeError(
            f"instantiating {_instance_kind(declaration.nodeclass)} {cls.__name__!r} "
            "requires parent=<node id>"
        )
    value = kwargs.get("value")
    data_type = kwargs.get("dataType")
    value_rank = kwargs.get("valueRank")
    if isinstance(type_spec, ObjectTypeSpec) and (
        value is not None or data_type is not None or value_rank is not None
    ):
        raise TypeError(
            f"{cls.__name__}(...): value/dataType/valueRank are variable-only "
            "(an Object instance carries no Value)."
        )
    if isinstance(type_spec, VariableTypeSpec):
        inherited_value = type_spec.value
        declared_data_type: o6.NodeId | None = type_spec.data_type
        declared_value_rank: int | None = type_spec.value_rank
        declared_array_dimensions = type_spec.array_dimensions
    elif isinstance(type_spec, ObjectTypeSpec):
        inherited_value = None
        declared_data_type = None
        declared_value_rank = None
        declared_array_dimensions = None
    else:
        raise TypeError(f"{cls.__qualname__} is not an ObjectType or VariableType")

    browse = kwargs.get("browseName") or declaration.browsename
    qn = browse if isinstance(browse, o6.QualifiedName) else o6.QualifiedName(browse)
    reference_type = kwargs.get("referenceType")
    ref = o6.NodeId(reference_type) if reference_type is not None else o6.NodeId(_HAS_COMPONENT)
    nodeclass = _TYPE_TO_INSTANCE[declaration.nodeclass]
    if data_type is not None and declared_data_type != o6.NodeId(data_type):
        inherited_value = None
    initial = value if value is not None else inherited_value
    if data_type is not None:
        initial = _coerce_builtin_value(data_type, initial)
    if isinstance(initial, (list, tuple)) and not initial:
        initial = None
    dt = o6.NodeId(data_type) if data_type is not None else declared_data_type
    if initial is None and data_type is not None and dt == declared_data_type:
        dt = None
    vr = value_rank if value_rank is not None else declared_value_rank
    array_dimensions = kwargs.get("arrayDimensions")
    array_dims = (
        list(array_dimensions) if array_dimensions is not None else declared_array_dimensions
    )
    if initial is not None and (dt is None or vr is None):
        from o6.util import _infer_data_type

        inferred_dt, inferred_vr = _infer_data_type(initial)
        if dt is None:
            dt = inferred_dt
        if vr is None:
            vr = inferred_vr
    if vr is None:
        vr = -1
    if vr >= 1 and array_dims is None:
        array_dims = [0] * vr
    native_attrs = _build_node_attrs(
        nodeclass,
        displayname=kwargs.get("displayName") or declaration.displayname or str(browse),
        data_type=dt,
        value_rank=vr,
        array_dimensions=array_dims,
        value=initial,
        access_level=kwargs.get("accessLevel"),
        user_access_level=kwargs.get("userAccessLevel"),
        minimum_sampling_interval=kwargs.get("minimumSamplingInterval"),
        historizing=bool(kwargs.get("historizing", False)),
        description=kwargs.get("description"),
        writemask=kwargs.get("writeMask"),
        user_writemask=kwargs.get("userWriteMask"),
        event_notifier=int(kwargs.get("eventNotifier", 0)),
    )
    requested_value = kwargs.get("nodeId")
    requested = o6.NodeId(requested_value) if requested_value is not None else o6.NodeId()
    return _construct_live_node(
        cls,
        server,
        nodeclass,
        requested,
        qn,
        declaration.nodeid,
        native_attrs,
        o6.NodeId(parent),
        ref,
        initializer_kwargs=initializer_kwargs,
        values=kwargs.get("values"),
        references=kwargs.get("references"),
        role_permissions=kwargs.get("rolePermissions"),
        modelling_rule=kwargs.get("modellingRule"),
        allow_abstract=bool(declaration.is_abstract and kwargs.get("_allow_abstract", False)),
    )


def _construct_view(
    server: Any,
    declaration: InstanceDeclaration,
    parent: o6.NodeIdLike,
    reference_type: o6.NodeIdLike,
) -> Any:
    from o6.node import ViewNode
    from o6.ns import ns0

    if not isinstance(declaration.attributes, ViewSpec):
        raise TypeError(f"{declaration.browsename!r} is not a View declaration")
    spec = declaration.attributes
    attrs = ns0.datatypes.ViewAttributes()
    attrs.displayName = o6.LocalizedText(declaration.displayname or declaration.browsename)
    attrs.containsNoLoops = spec.contains_no_loops
    attrs.eventNotifier = spec.event_notifier
    attrs.writeMask = declaration.writemask or 0
    attrs.userWriteMask = declaration.user_writemask or 0
    if declaration.description is not None:
        attrs.description = o6.LocalizedText(declaration.description)

    requested = o6.NodeId(declaration.nodeid) if declaration.nodeid is not None else o6.NodeId()
    browse = declaration.browsename
    if not re.match(r"^(?:ns=[^;]+;|\d+:)", browse):
        namespace = requested.ns
        index = _namespace_index(namespace)
        browse = f"{index}:{browse}"
    qn = o6.QualifiedName(browse)
    node = server._create_node(
        lambda: server._add_view_node(
            requested,
            o6.NodeId(parent),
            o6.NodeId(reference_type),
            qn,
            attrs,
        ),
        qn,
        ViewNode,
    )
    _apply_role_permissions(server, node._nodeid, declaration.role_permissions)
    node._access_restrictions = declaration.access_restrictions
    return node


def _construct_declaration(
    server: o6.Server,
    parent: o6.NodeIdLike,
    declaration: InstanceDeclaration,
    materialized: Optional[dict[int, o6.NodeId]] = None,
    reference_type: Any = _UNSET,
    *,
    template: bool = False,
) -> Any:
    """Materialize one node declaration nested through ``references=[...]``.

    Marker children use their normal two-phase constructor, which recursively
    creates their own explicit children before ``add_node_finish``. This lets
    open62541's mandatory-child completion reuse the requested child nodes
    rather than creating replacements with generated NodeIds.
    """
    if isinstance(declaration.attributes, ViewSpec):
        view_reference = declaration.reference_type if reference_type is _UNSET else reference_type
        live = _construct_view(server, declaration, parent, view_reference)
        if materialized is not None:
            materialized[id(declaration)] = o6.NodeId(live._nodeid)
        for child in declaration.children:
            _construct_declaration(server, live._nodeid, child, materialized)
        return live
    if isinstance(declaration.attributes, MethodSpec):
        requested = o6.NodeId(declaration.nodeid) if declaration.nodeid is not None else o6.NodeId()
        inverse = declaration.inverse
        creation_decl = (
            dataclass_replace(declaration, reference_type=o6.NodeId()) if inverse else declaration
        )
        live = _add_method_child(
            server,
            creation_decl,
            requested,
            o6.NodeId() if inverse else o6.NodeId(parent),
            o6.QualifiedName(declaration.browsename or "Method"),
        )
        _apply_role_permissions(server, live, declaration.role_permissions)
        if inverse:
            server.addReference(live, parent, declaration.reference_type)
        if declaration.modelling_rule is not None:
            server.addReference(
                live,
                _resolved_modelling_rule(declaration.modelling_rule),
                o6.NodeId("i=37"),
            )
        if materialized is not None:
            materialized[id(declaration)] = o6.NodeId(live)
        return live
    if reference_type is _UNSET:
        reference_type = declaration.reference_type
    inverse = declaration.inverse
    marker = declaration.typeTarget if isinstance(declaration.typeTarget, type) else None
    payload = declaration.attributes
    if isinstance(payload, VariableSpec):
        value = payload.value
    elif isinstance(payload, ObjectSpec):
        value = None
    else:
        raise TypeError(f"{declaration.browsename!r} is not an Object or Variable declaration")
    requested = o6.NodeId(declaration.nodeid) if declaration.nodeid is not None else o6.NodeId()
    browse_name = o6.QualifiedName(declaration.browsename)
    creation_parent = o6.NodeId() if inverse else o6.NodeId(parent)
    creation_reference = o6.NodeId() if inverse else o6.NodeId(reference_type)
    attributes = _child_attrs(declaration, value)
    if template:
        creation_declaration = (
            dataclass_replace(declaration, reference_type=o6.NodeId()) if inverse else declaration
        )
        if marker is not None and declaration.children:
            live = server._on_event_loop(
                lambda: server._add_node_begin(
                    int(declaration.nodeclass),
                    requested,
                    creation_parent,
                    creation_reference,
                    browse_name,
                    _type_target_nodeid(declaration.typeTarget),
                    attributes,
                )
            )
            _precreate_children(
                server,
                live,
                marker,
                _declaration_values(declaration),
            )
            server._on_event_loop(lambda: server._add_node_finish(live))
        else:
            live = _add_leaf_child(
                server,
                creation_declaration,
                requested,
                creation_parent,
                browse_name,
                attributes,
            )
    else:
        if marker is None:
            raise TypeError(f"{declaration.browsename!r} has no Python implementation type")
        live = _construct_live_node(
            marker,
            server,
            declaration.nodeclass,
            requested,
            browse_name,
            cast(Any, _type_target_nodeid(declaration.typeTarget)),
            attributes,
            creation_parent,
            creation_reference,
            initializer_kwargs={},
            references=declaration.children,
            role_permissions=declaration.role_permissions,
            modelling_rule=declaration.modelling_rule,
            allow_abstract=declaration.allow_abstract,
        )
    if inverse:
        server.addReference(live, parent, reference_type)
    if template:
        _apply_role_permissions(server, live, declaration.role_permissions)
        if declaration.modelling_rule is not None:
            server.addReference(
                live,
                _resolved_modelling_rule(declaration.modelling_rule),
                o6.NodeId("i=37"),
            )
    live_id = o6.NodeId(live)
    if materialized is not None:
        materialized[id(declaration)] = live_id
    return live
