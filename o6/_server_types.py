# Copyright 2026 (c) o6 Automation GmbH
"""Server-side Python implementation classes and callback policy."""

from __future__ import annotations

import typing
from dataclasses import dataclass
from functools import update_wrapper
from types import UnionType
from typing import Any, Callable, TypeVar, cast, get_args, get_origin, overload

import o6
from o6._declarations import (
    CallbackBinding,
    ImplementationBinding,
    InstanceDeclaration,
    ObjectTypeSpec,
    TypeDeclaration,
    VariableTypeSpec,
    _BrowseNameKey,
    _CallbackKind,
    _CallbackTarget,
    _DirectMethodTarget,
    _MemberPathTarget,
    _OWN_VARIABLE_SLOT,
    _CHILD_BEARING_SPECS,
    _NodeClass,
    _TYPE_TO_INSTANCE,
    _all_children,
    _annotations,
    _browse_name_key,
    _browsename_is_qualified,
    _type_declaration,
    _type_target_nodeid,
    _resolve_annotations,
)

_F = TypeVar("_F", bound=Callable[..., Any])
_CALLBACK_BINDINGS_ATTR = "__o6_callbacks__"
_LIVE_CLASS_ATTR = "_o6LiveClassCache"
_IMPLEMENTATION_BINDING = "_o6ImplementationBinding"


def _local_variable_slot(cls: type, *, read: bool) -> str | None:
    return _callback_bindings(cls).get(("read" if read else "write", _OWN_VARIABLE_SLOT))


def _resolved_callback(klass: type, slot: str, kind: str) -> Callable[..., Any]:
    """Resolve one inherited callback slot while preserving instance semantics."""
    for owner in klass.__mro__:
        if slot not in vars(owner):
            continue
        if isinstance(vars(owner)[slot], (staticmethod, classmethod)):
            raise TypeError(
                f"@o6.{kind} implementation {klass.__qualname__}.{slot} must be an instance method"
            )
        break
    callback = getattr(klass, slot)
    if not callable(callback):
        raise TypeError(
            f"Python implementation {klass.__qualname__}.{slot} for @o6.{kind} is not callable"
        )
    return cast(Callable[..., Any], callback)


def _callback_bindings(klass: type) -> dict[tuple[_CallbackKind, _CallbackTarget], str]:
    """Validate the explicit callback records declared directly on a class."""
    bindings: dict[tuple[_CallbackKind, _CallbackTarget], str] = {}
    for attr_name, attr_value in vars(klass).items():
        callback = (
            attr_value.__func__ if isinstance(attr_value, (staticmethod, classmethod)) else None
        )
        if isinstance(callback, _CallbackMethod):
            raise TypeError(f"@o6.{callback.bindings[0].kind} requires an instance method")
    for binding in vars(klass).get(_CALLBACK_BINDINGS_ATTR, ()):
        if not isinstance(binding, CallbackBinding):
            raise TypeError(f"{klass.__qualname__} has invalid callback binding metadata")
        key = binding.kind, binding.target
        previous = bindings.get(key)
        if previous is not None:
            kind, target = key
            if target == _OWN_VARIABLE_SLOT:
                detail = f"a VariableType can declare only one @o6.{kind} method"
            elif isinstance(target, _DirectMethodTarget):
                detail = f"{klass.__qualname__} has competing @o6.call decorators"
            else:
                assert isinstance(target, _MemberPathTarget)
                detail = (
                    f"{klass.__qualname__} has competing " f"@o6.{kind}({target.path!r}) decorators"
                )
            raise TypeError(f"{detail}: {previous!r} and {binding.method_name!r}; keep one")
        bindings[key] = binding.method_name
    return bindings


def _available_method_keys(
    klass: type,
    own_children: list[InstanceDeclaration] | None = None,
    interfaces: tuple[type, ...] = (),
) -> set[_BrowseNameKey]:
    """Collect the BrowseName keys of every Method this class declares or inherits."""
    available = {
        _browse_name_key(child.browsename)
        for child in own_children or []
        if int(child.nodeclass) == int(_NodeClass.METHOD)
    }
    interface_types = list(interfaces)
    for base in klass.__mro__[1:]:
        declaration = vars(base).get("__o6_declaration__")
        if not isinstance(declaration, TypeDeclaration) or not isinstance(
            declaration.attributes, _CHILD_BEARING_SPECS
        ):
            continue
        available.update(
            _browse_name_key(child.browsename)
            for child in declaration.instances
            if int(child.nodeclass) == int(_NodeClass.METHOD)
        )
        interface_types.extend(declaration.interfaces)
    seen_interfaces: set[type] = set()
    while interface_types:
        interface = interface_types.pop()
        if interface in seen_interfaces:
            continue
        seen_interfaces.add(interface)
        interface_declaration = (
            getattr(interface, "__o6_declaration__", None) if isinstance(interface, type) else None
        )
        if not isinstance(interface_declaration, TypeDeclaration) or not isinstance(
            interface_declaration.attributes, _CHILD_BEARING_SPECS
        ):
            continue
        available.update(
            _browse_name_key(child.browsename)
            for child in _all_children(interface)
            if int(child.nodeclass) == int(_NodeClass.METHOD)
        )
        interface_types.extend(interface_declaration.interfaces)
    return available


def _spell_call_key(key: _BrowseNameKey) -> str:
    """Render a BrowseName key as ``ns=<shortname>;Name`` (index if unresolved)."""
    index, name = key
    try:
        shortname = o6.ns[index].shortname
    except Exception:
        return f"ns={index};{name}"
    return f"ns={shortname};{name}"


def _resolve_call_slots(
    targets: dict[_DirectMethodTarget, str],
    available: set[_BrowseNameKey],
    klass: type,
) -> dict[_BrowseNameKey, str]:
    """Map each ``@o6.call`` target to a concrete ``(namespace, name)`` key.

    A qualified target keeps its BrowseName key verbatim. An unqualified target
    (a bare name, no ``ns=``) is matched by its local name against the type's
    declared Methods: a unique match binds it, several matches raise (ambiguous),
    and no match keeps the placeholder key so the caller reports it as unknown.
    """
    names_to_keys: dict[str, list[_BrowseNameKey]] = {}
    for key in available:
        names_to_keys.setdefault(key[1], []).append(key)

    resolved: dict[_BrowseNameKey, str] = {}
    for target, slot in targets.items():
        if target.qualified:
            key = target.browse_name
        else:
            name = target.browse_name[1]
            matches = sorted(set(names_to_keys.get(name, ())))
            if len(matches) > 1:
                spellings = ", ".join(f'"{_spell_call_key(match)}"' for match in matches)
                raise TypeError(
                    f"{klass.__qualname__}.{slot} uses @o6.call({name!r}), but that BrowseName "
                    f"is ambiguous across namespaces; qualify it with one of: {spellings}"
                )
            key = matches[0] if matches else target.browse_name
        previous = resolved.get(key)
        if previous is not None and previous != slot:
            raise TypeError(
                f"{klass.__qualname__} has competing @o6.call decorators for "
                f"'{_spell_call_key(key)}': {previous!r} and {slot!r}; keep one"
            )
        resolved[key] = slot
    return resolved


def _class_own_method_children(klass: type) -> list[InstanceDeclaration] | None:
    """Return the Method-bearing declaration instances a class declares itself."""
    declaration = vars(klass).get("__o6_declaration__")
    if isinstance(declaration, TypeDeclaration) and isinstance(
        declaration.attributes, _CHILD_BEARING_SPECS
    ):
        return declaration.instances
    return None


def _class_call_targets(klass: type) -> dict[_DirectMethodTarget, str]:
    """Collect the direct ``@o6.call`` targets declared on one class."""
    return {
        target: slot
        for (kind, target), slot in _callback_bindings(klass).items()
        if kind == "call" and isinstance(target, _DirectMethodTarget)
    }


def _validate_method_targets(
    klass: type,
    own_children: list[InstanceDeclaration] | None = None,
    interfaces: tuple[type, ...] = (),
) -> None:
    available = _available_method_keys(klass, own_children, interfaces)
    resolved = _resolve_call_slots(_class_call_targets(klass), available, klass)
    for key, attr_name in resolved.items():
        if key not in available:
            raise TypeError(
                f"{klass.__qualname__}.{attr_name} uses @o6.call for unknown "
                f"UA Method 'ns={key[0]};{key[1]}'; declare or inherit that Method child"
            )


# =============================================================================
# Python implementation classes and callback wiring
# =============================================================================


def _live_init_noop(self: Any, *args: Any, **kwargs: Any) -> None:
    """Absorb type.__call__'s init after __new__ ran it transactionally."""


_LIVE_METACLASSES: dict[tuple[type, type], type] = {}


def _live_metaclass(marker: type, node_cls: type) -> type:
    marker_meta = type(marker)
    node_meta = type(node_cls)
    if issubclass(marker_meta, node_meta):
        return marker_meta
    if issubclass(node_meta, marker_meta):
        return node_meta
    key = marker_meta, node_meta
    combined = _LIVE_METACLASSES.get(key)
    if combined is None:
        combined = type(
            f"_{marker_meta.__name__}_{node_meta.__name__}",
            key,
            {},
        )
        _LIVE_METACLASSES[key] = combined
    return combined


def _live_class(marker: type, node_cls: type) -> type:
    """Return the node-api-backed runtime subclass for a type marker."""
    live = vars(marker).get(_LIVE_CLASS_ATTR)
    if live is not None and not issubclass(live, node_cls):
        raise RuntimeError(
            f"{marker.__qualname__} already has a live class for an incompatible NodeClass"
        )
    if live is None:
        bindings = _callback_bindings(marker)
        declaration = getattr(marker, "__o6_declaration__", None)
        if (
            not isinstance(declaration, TypeDeclaration)
            or not isinstance(declaration.attributes, VariableTypeSpec)
        ) and (
            ("read", _OWN_VARIABLE_SLOT) in bindings or ("write", _OWN_VARIABLE_SLOT) in bindings
        ):
            raise TypeError("@o6.read and @o6.write require a VariableType implementation")
        _validate_method_targets(marker, _class_own_method_children(marker))
        live = _live_metaclass(marker, node_cls)(
            f"{marker.__name__}__Live",
            (marker, node_cls),
            {
                "__module__": marker.__module__,
                "__init__": _live_init_noop,
            },
        )
        setattr(marker, _LIVE_CLASS_ATTR, live)
    return live


def _attach_instance_type(server: Any, marker: type, node_type: type) -> None:
    """Attach a declared instance class to one server's UA type node."""
    from o6._node_backend import _server_node
    from o6.node import Node, ObjectNode, ObjectTypeNode, VariableNode, VariableTypeNode

    declaration = _type_declaration(marker)
    type_node_type = (
        VariableTypeNode if isinstance(declaration.attributes, VariableTypeSpec) else ObjectTypeNode
    )
    type_node = _server_node(server, declaration.nodeid, type_node_type)
    _live_class(marker, node_type)
    type_node.__dict__[_IMPLEMENTATION_BINDING] = ImplementationBinding(
        declared_type=marker,
        implementation_type=marker,
    )


def _implement(server: Any, declaration: type, implementation: type | None) -> None:
    """Bind an undecorated implementation class to a server-local type node."""
    from o6._node_backend import _server_node
    from o6.node import ObjectNode, ObjectTypeNode, VariableNode, VariableTypeNode

    type_declaration = vars(declaration).get("__o6_declaration__")
    if not isinstance(type_declaration, TypeDeclaration) or not isinstance(
        type_declaration.attributes,
        (ObjectTypeSpec, VariableTypeSpec),
    ):
        raise TypeError("declaration must be a decorated ObjectType or VariableType")
    reset = implementation is None
    implementation_type = declaration if implementation is None else implementation
    if (
        not reset
        and isinstance(implementation_type, type)
        and vars(implementation_type).get("__o6_declaration__") is not None
    ):
        raise TypeError("implementation must be undecorated; it must not declare a UA subtype")
    binding = ImplementationBinding(
        declared_type=declaration,
        implementation_type=implementation_type,
    )

    if isinstance(type_declaration.attributes, ObjectTypeSpec):
        type_node = _server_node(server, type_declaration.nodeid, ObjectTypeNode)
        _live_class(binding.implementation_type, ObjectNode)
    else:
        type_node = _server_node(server, type_declaration.nodeid, VariableTypeNode)
        _live_class(binding.implementation_type, VariableNode)
    existing = type_node.__dict__.get(_IMPLEMENTATION_BINDING)
    if existing == binding:
        return
    if existing is not None and not isinstance(existing, ImplementationBinding):
        raise TypeError(f"{declaration.__qualname__} has invalid implementation metadata")
    if (
        isinstance(existing, ImplementationBinding)
        and not reset
        and existing.implementation_type is not declaration
    ):
        raise TypeError(
            f"{declaration.__qualname__} is already implemented by "
            f"{existing.implementation_type.__qualname__} on this server"
        )
    type_node.__dict__[_IMPLEMENTATION_BINDING] = binding


def _declared_instance_type(server: Any, type_id: Any, node_class: int) -> type | None:
    from o6._node_backend import _server_node
    from o6.node import Node, ObjectNode, ObjectTypeNode, VariableNode, VariableTypeNode
    from o6.ns import ns0

    if node_class == int(ns0.datatypes.NodeClass.VARIABLE):
        type_node_type: type[Node] = VariableTypeNode
    elif node_class == int(ns0.datatypes.NodeClass.OBJECT):
        type_node_type = ObjectTypeNode
    else:
        return None
    type_node = _server_node(server, o6.NodeId(type_id), type_node_type)
    binding = type_node.__dict__.get(_IMPLEMENTATION_BINDING)
    if not isinstance(binding, ImplementationBinding):
        return None
    node_type = VariableNode if node_class == int(ns0.datatypes.NodeClass.VARIABLE) else ObjectNode
    return _live_class(binding.implementation_type, node_type)


def _live_implementation_type(candidate: type) -> type | None:
    """Recover the implementation class from a generated live node class."""
    from o6.node import Node

    bases = candidate.__bases__
    if len(bases) < 2 or not isinstance(bases[0], type) or not issubclass(bases[1], Node):
        return None
    return bases[0]


def _variable_instance_type(server: Any, type_id: Any) -> type:
    from o6.node import VariableNode
    from o6.ns import ns0

    return (
        _declared_instance_type(server, type_id, int(ns0.datatypes.NodeClass.VARIABLE))
        or VariableNode
    )


def _variable_concrete_type(server: Any, type_id: Any, instance_type: type | None) -> type:
    """Normalize a live node class to its effective VariableType implementation."""
    declared_type = None
    if instance_type is None:
        declared_type = _variable_instance_type(server, type_id)
        instance_type = declared_type
    concrete_type = _live_implementation_type(instance_type) or instance_type
    if any(
        isinstance(
            getattr(vars(candidate).get("__o6_declaration__"), "attributes", None),
            VariableTypeSpec,
        )
        for candidate in concrete_type.__mro__
    ):
        return concrete_type
    declared_type = declared_type or _variable_instance_type(server, type_id)
    return _live_implementation_type(declared_type) or declared_type


def _variable_callbacks(
    server: Any,
    type_id: Any,
    instance_type: type | None = None,
    *,
    override_node: Any | None = None,
    override_read: Callable[..., Any] | None = None,
    override_write: Callable[..., Any] | None = None,
) -> tuple[Callable[..., Any] | None, Callable[..., Any] | None]:
    """Resolve read and write together from the nearest type layers."""
    from o6._node_backend import _server_node
    from o6.node import VariableTypeNode

    concrete_type = _variable_concrete_type(server, type_id, instance_type)
    candidates = list(concrete_type.__mro__)
    if not any(
        isinstance(
            getattr(vars(candidate).get("__o6_declaration__"), "attributes", None),
            VariableTypeSpec,
        )
        for candidate in candidates
    ):
        type_node = _server_node(server, o6.NodeId(type_id), VariableTypeNode)
        if override_node is type_node:
            read, write = override_read, override_write
        else:
            read = server._node_callback(type_node, "read")
            write = server._node_callback(type_node, "write")
    else:
        resolved: list[Callable[..., Any] | None] = [None, None]
        seen_type_ids: set[o6.NodeId] = set()
        for candidate in candidates:
            candidate_declaration = vars(candidate).get("__o6_declaration__")
            if isinstance(candidate_declaration, TypeDeclaration) and isinstance(
                candidate_declaration.attributes, VariableTypeSpec
            ):
                type_node = _server_node(server, candidate_declaration.nodeid, VariableTypeNode)
                type_node_id = o6.NodeId(type_node)
                if type_node_id not in seen_type_ids:
                    seen_type_ids.add(type_node_id)
                    callbacks = (
                        (override_read, override_write)
                        if override_node is type_node
                        else (
                            server._node_callback(type_node, "read"),
                            server._node_callback(type_node, "write"),
                        )
                    )
                    for index, callback in enumerate(callbacks):
                        if resolved[index] is None and callback is not None:
                            resolved[index] = callback
            for index, is_read in enumerate((True, False)):
                if resolved[index] is not None:
                    continue
                slot = _local_variable_slot(candidate, read=is_read)
                if slot is not None:
                    resolved[index] = _resolved_callback(
                        concrete_type, slot, "read" if is_read else "write"
                    )
            if all(item is not None for item in resolved):
                break
        read, write = resolved
    if write is not None and read is None:
        raise TypeError("a callback-backed Variable requires a read callback")
    return read, write


def _python_node_implementation(
    server: Any,
    node_id: Any,
    type_id: Any,
    native_node: Any,
    node_class: int,
) -> tuple[Any, type] | None:
    from o6._node_backend import _server_node
    from o6.node import Node, ObjectNode, VariableNode
    from o6.ns import ns0

    implementation = (
        type(native_node)
        if native_node is not None
        else _declared_instance_type(server, type_id, node_class)
    )
    if implementation is None:
        return None
    concrete = _live_implementation_type(implementation)
    if not isinstance(concrete, type):
        return None
    node_type = VariableNode if node_class == int(ns0.datatypes.NodeClass.VARIABLE) else ObjectNode
    try:
        node = native_node or _server_node(
            server, o6.NodeId(node_id), cast(type[Node], implementation)
        )
    except TypeError:
        return None
    if not isinstance(node, node_type):
        return None
    return node, concrete


def _implementation_annotation(annotation: Any) -> tuple[Any, bool]:
    """Return the implementation type and whether the member remains optional."""
    if get_origin(annotation) in (typing.Union, UnionType):
        members = tuple(item for item in get_args(annotation) if item is not type(None))
        if len(members) == 1 and len(members) != len(get_args(annotation)):
            return members[0], True
    return annotation, False


@dataclass(frozen=True)
class _MemberResolution:
    declaration: InstanceDeclaration
    implementation_type: type | None = None
    optional: bool = False


def _member_resolutions(klass: type) -> dict[str, _MemberResolution]:
    """Resolve declarations and Python-only child implementations together."""
    resolved = {
        child.python_name: _MemberResolution(child)
        for child in _all_children(klass)
        if child.python_name is not None
    }
    for owner in reversed(klass.__mro__):
        annotations = _annotations(owner)
        if not annotations:
            continue
        for name, annotation in _resolve_annotations(owner, annotations).items():
            implementation, optional = _implementation_annotation(annotation)
            if not isinstance(implementation, type):
                continue
            implementation_declaration = getattr(implementation, "__o6_declaration__", None)
            if not isinstance(implementation_declaration, TypeDeclaration) or not isinstance(
                implementation_declaration.attributes, _CHILD_BEARING_SPECS
            ):
                continue
            # A decorated marker annotation declares a UA child. Only an
            # undecorated subclass is an implementation narrowing.
            if vars(implementation).get("__o6_declaration__") is not None:
                continue
            member = resolved.get(name)
            if member is None:
                raise TypeError(
                    f"{owner.__qualname__}.{name} selects implementation "
                    f"{implementation.__qualname__}, but no such UA member exists"
                )
            declaration = member.declaration
            instance_nodeclass = _TYPE_TO_INSTANCE.get(implementation_declaration.nodeclass)
            if instance_nodeclass is not declaration.nodeclass:
                raise TypeError(
                    f"{owner.__qualname__}.{name} implementation has incompatible NodeClass"
                )
            declared_marker = (
                declaration.typeTarget if isinstance(declaration.typeTarget, type) else None
            )
            if declared_marker is not None:
                if not issubclass(implementation, declared_marker):
                    raise TypeError(
                        f"{owner.__qualname__}.{name} implementation must subclass "
                        f"{declared_marker.__qualname__}"
                    )
            elif str(implementation_declaration.nodeid) != str(
                _type_target_nodeid(declaration.typeTarget)
            ):
                raise TypeError(
                    f"{owner.__qualname__}.{name} implementation must retain TypeDefinition "
                    f"{_type_target_nodeid(declaration.typeTarget)}"
                )
            resolved[name] = _MemberResolution(declaration, implementation, optional)
    return resolved


def _member_callback_slots(
    klass: type,
) -> dict[tuple[_CallbackKind, _MemberPathTarget], str]:
    """Collect construction-time member callbacks, with derived classes winning."""
    selected: dict[tuple[_CallbackKind, _MemberPathTarget], str] = {}
    for owner in reversed(klass.__mro__):
        selected.update(
            ((kind, target), slot)
            for (kind, target), slot in _callback_bindings(owner).items()
            if isinstance(target, _MemberPathTarget)
        )
    return selected


def _effective_method_slots(klass: type) -> dict[_BrowseNameKey, str]:
    """Resolve class Method associations once, with derived classes winning."""
    targets: dict[_DirectMethodTarget, str] = {}
    for owner in reversed(klass.__mro__):
        targets.update(
            (target, slot)
            for (kind, target), slot in _callback_bindings(owner).items()
            if kind == "call" and isinstance(target, _DirectMethodTarget)
        )
    available = _available_method_keys(klass, _class_own_method_children(klass))
    return _resolve_call_slots(targets, available, klass)


# =============================================================================
# Public server implementation decorators
# =============================================================================


class _CallbackMethod:
    """Ephemeral descriptor that records bindings and restores the function."""

    def __init__(self, function: _F) -> None:
        self.function = function
        self.bindings: tuple[CallbackBinding, ...] = ()
        update_wrapper(self, function)

    def add(self, kind: _CallbackKind, target: _CallbackTarget) -> "_CallbackMethod":
        for binding in self.bindings:
            if binding.kind != kind:
                continue
            if binding.target == target:
                return self
            if kind == "call":
                raise TypeError("one Python method cannot implement two UA Methods")
            raise TypeError(
                f"one Python method cannot implement both a {kind} type callback "
                f"and a {kind} member path"
            )
        self.bindings += (CallbackBinding(kind, target, self.function.__name__),)
        return self

    def __get__(self, instance: Any, owner: type | None = None) -> Any:
        return self.function.__get__(instance, owner)

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        return self.function(*args, **kwargs)

    def __set_name__(self, owner: type, name: str) -> None:
        local = tuple(vars(owner).get(_CALLBACK_BINDINGS_ATTR, ()))
        recorded = tuple(CallbackBinding(item.kind, item.target, name) for item in self.bindings)
        for binding in recorded:
            if binding not in local:
                local += (binding,)
        setattr(owner, _CALLBACK_BINDINGS_ATTR, local)
        # Callback decoration must not change ordinary Python method behavior.
        setattr(owner, name, self.function)


def _decorate_callback(kind: _CallbackKind, target: _CallbackTarget, fn: _F) -> _F:
    _require_instance_callback(kind, fn)
    decorated = fn if isinstance(fn, _CallbackMethod) else _CallbackMethod(fn)
    return cast(_F, decorated.add(kind, target))


@overload
def read(fn: _F) -> _F: ...


@overload
def read(fn: str) -> Callable[[_F], _F]: ...


def read(fn: _F | str) -> _F | Callable[[_F], _F]:
    """Implement this VariableType's value read, or one concrete member path.

    `@o6.read` marks an ordinary VariableType instance method as its value-read
    implementation. The decorator preserves the method and its Python signature,
    so subclasses can override it without repeating the decorator, and calling it
    directly still works.

    `@o6.read("member.child")` instead resolves a Python member path when the
    containing Object finishes, and stores the implementation and containing
    Object on that concrete Variable. The callback receives `range`, `session`,
    and `includeSourceTimestamp` as keyword arguments.

    See [Server callbacks](../manual/server/callbacks.md#one-resolution-rule) for the
    shared `read`/`write`/`call` precedence and reset behaviour.
    """
    if isinstance(fn, str):
        return _member_callback("read", fn)
    return _variable_callback("read", fn)


@overload
def write(fn: _F) -> _F: ...


@overload
def write(fn: str) -> Callable[[_F], _F]: ...


def write(fn: _F | str) -> _F | Callable[[_F], _F]:
    """Implement this VariableType's value write, or one concrete member path.

    `@o6.write` marks an ordinary VariableType instance method as its value-write
    implementation. The decorator preserves the method and its Python signature,
    so subclasses can override it without repeating the decorator, and calling it
    directly still works.

    `@o6.write("member.child")` instead resolves a Python member path when the
    containing Object finishes, and stores the implementation and containing
    Object on that concrete Variable. The callback receives the requested
    [`DataValue`][o6.DataValue] plus `range` and `session` keyword arguments.

    See [Server callbacks](../manual/server/callbacks.md#one-resolution-rule) for the
    shared `read`/`write`/`call` precedence and reset behaviour.
    """
    if isinstance(fn, str):
        return _member_callback("write", fn)
    return _variable_callback("write", fn)


def _method_implementation(target: str) -> Callable[[_F], _F]:
    """Bind a Python implementation to one Method or nested Method path.

    Use in a `@o6.objecttype` class body to implement a Method that is declared
    on the type or inherited from a base (including codegen-emitted types the user
    does not own):

    ```python
    @o6.objecttype(ns="mytypes", browsename="MyServerType")
    class MyServerType(ns0.objtypes.ServerType):
        @o6.call("GetMonitoredItems")
        def _get_monitored_items(self, subscription_id):
            return (
                o6.StatusCode.GOOD,
                self.runtime.get_monitored_items(subscription_id),
            )
    ```
    """

    if "." in target:
        return _member_callback("call", target)

    qualified = _browsename_is_qualified(target)

    def deco(fn: _F) -> _F:
        method_target = _DirectMethodTarget(_browse_name_key(target), qualified)
        return _decorate_callback("call", method_target, fn)

    return deco


def _variable_callback(kind: _CallbackKind, fn: _F) -> _F:
    """Mark one ordinary VariableType method as its read or write slot."""
    return _decorate_callback(kind, _OWN_VARIABLE_SLOT, fn)


def _require_instance_callback(kind: str, fn: Any) -> None:
    if isinstance(fn, (staticmethod, classmethod)):
        raise TypeError(f"@o6.{kind} requires an instance method")
    if not callable(fn):
        raise TypeError(f"@o6.{kind} requires a callable")


def _member_callback(kind: _CallbackKind, path: str) -> Callable[[_F], _F]:
    try:
        target = _MemberPathTarget(tuple(path.split(".")))
    except ValueError as exc:
        raise ValueError(f"@o6.{kind} member path must contain public Python member names") from exc

    def decorate(fn: _F) -> _F:
        return _decorate_callback(kind, target, fn)

    return decorate
