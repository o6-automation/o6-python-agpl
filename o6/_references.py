# Copyright 2026 (c) o6 Automation GmbH
"""Declarative OPC UA reference helpers."""

from __future__ import annotations

from typing import Any, TypeVar, cast, overload

import o6
from o6._declarations import (
    InstanceDeclaration,
    MethodSpec,
    ObjectTypeSpec,
    ReferenceDeclaration,
    TypeDeclaration,
    UndefinedReference,
    VariableTypeSpec,
    _instance_declaration,
    _is_node_declaration,
    _remove_instance_root,
)

_T = TypeVar("_T")
_HAS_PROPERTY = "ns=ns0;i=46"
_HAS_COMPONENT = "ns=ns0;i=47"
UNSET = object()


@overload
def reference(instance: None, referenceType: Any, /, *, inverse: bool = False) -> Any: ...


@overload
def reference(instance: _T, referenceType: Any, /, *, inverse: bool = False) -> _T: ...


@overload
def reference(
    subject: _T,
    referenceType: Any,
    object: Any,
    /,
    *,
    inverse: bool = False,
    server: Any = UNSET,
) -> _T: ...


def reference(
    subject: _T | None,
    referenceType: Any,
    object: Any = UNSET,
    /,
    *,
    inverse: bool = False,
    server: Any = UNSET,
) -> _T | None:
    """Describe a declarative linkage or add a reference between live nodes."""
    if object is not UNSET:
        target = object
        if subject is None:
            raise TypeError("the source of a two-ended reference cannot be None")
        if _is_node_declaration(subject):
            _instance_declaration(subject).references.append(
                ReferenceDeclaration(o6.NodeId(referenceType), target, inverse)
            )
            return cast(_T, subject)

        type_declaration = (
            vars(subject).get("__o6_declaration__") if isinstance(subject, type) else None
        )
        if isinstance(type_declaration, TypeDeclaration):
            if not isinstance(
                type_declaration.attributes, (VariableTypeSpec, ObjectTypeSpec)
            ) or not _is_node_declaration(target):
                type_declaration.references.append(
                    ReferenceDeclaration(o6.NodeId(referenceType), target, inverse)
                )
                return cast(_T, subject)
            declared_target = cast(Any, target)
            declaration = _instance_declaration(declared_target)
            declaration.reference_type = o6.NodeId(referenceType)
            declaration.inverse = inverse
            declaration.parent = None
            _remove_instance_root(declaration)
            name = declaration.browsename
            if not name:
                raise TypeError("a type declaration child needs a browsename")
            existing = next(
                (
                    index
                    for index, child in enumerate(type_declaration.instances)
                    if child.browsename == declaration.browsename
                    and child.reference_type == declaration.reference_type
                    and child.inverse == declaration.inverse
                ),
                None,
            )
            if existing is None:
                type_declaration.instances.append(declaration)
            else:
                type_declaration.instances[existing] = declaration
            return cast(_T, subject)

        source_server = getattr(getattr(subject, "_backend", None), "_server", None)
        target_server = getattr(getattr(target, "_backend", None), "_server", None)
        if (
            source_server is not None
            and target_server is not None
            and source_server is not target_server
        ):
            raise TypeError("reference endpoints belong to different servers")
        endpoint_server = source_server or target_server
        if server is not UNSET:
            if server is None:
                raise TypeError("server=None is valid only for node declarations")
            if endpoint_server is not None and server is not endpoint_server:
                raise TypeError(
                    "server= and the live reference endpoints belong to different servers"
                )
            resolved_server = server
        elif endpoint_server is not None:
            resolved_server = endpoint_server
        else:
            from o6.server import _get_live_servers

            live = _get_live_servers()
            if len(live) != 1:
                raise TypeError(
                    "cannot infer server for reference: pass server=<server> or use live nodes"
                )
            resolved_server = live[0]
        resolved_server.addReference(
            getattr(subject, "nodeId", subject),
            getattr(target, "nodeId", target),
            referenceType,
            forward=not inverse,
        )
        return cast(_T, subject)

    if server is not UNSET:
        raise TypeError("server= is only accepted by the three-argument reference form")
    if subject is None:
        return cast(_T | None, UndefinedReference(referenceType, inverse))
    if _is_node_declaration(subject):
        declaration = _instance_declaration(subject)
        if isinstance(declaration.attributes, MethodSpec) and o6.NodeId(referenceType) == o6.NodeId(
            _HAS_PROPERTY
        ):
            raise TypeError("a Method cannot be attached with o6.hasProperty()")
        declaration.reference_type = o6.NodeId(referenceType)
        declaration.inverse = inverse
        declaration.parent = None
        _remove_instance_root(declaration)
        return cast(_T, subject)
    raise TypeError(
        f"o6.reference() expects a node declaration or method instance, got {type(subject).__name__}"
    )


@overload
def hasProperty(instance: None, /) -> Any: ...


@overload
def hasProperty(instance: _T, /) -> _T: ...


def hasProperty(instance: _T | None, /) -> Any:
    return reference(instance, _HAS_PROPERTY)


@overload
def hasComponent(instance: None, /) -> Any: ...


@overload
def hasComponent(instance: _T, /) -> _T: ...


def hasComponent(instance: _T | None, /) -> Any:
    return reference(instance, _HAS_COMPONENT)


def hasEncoding(subject: _T, object: Any = UNSET, /) -> _T:
    return (
        cast(_T, reference(subject, "i=38"))
        if object is UNSET
        else cast(_T, reference(subject, "i=38", object))
    )


def _forward(reference_type: str, instance: _T | None) -> Any:
    return reference(instance, reference_type)


def organizes(instance: _T | None, /) -> Any:
    return _forward("i=35", instance)


def hasEventSource(instance: _T | None, /) -> Any:
    return _forward("i=36", instance)


def generatesEvent(instance: _T | None, /) -> Any:
    return _forward("i=41", instance)


def hasNotifier(instance: _T | None, /) -> Any:
    return _forward("i=48", instance)


def hasOrderedComponent(instance: _T | None, /) -> Any:
    return _forward("i=49", instance)


def hasCondition(instance: _T | None, /) -> Any:
    return _forward("i=9006", instance)


def hasInterface(instance: _T | None, /) -> Any:
    return _forward("i=17603", instance)


def hasAddIn(instance: _T | None, /) -> Any:
    return _forward("i=17604", instance)


def _inverse(reference_type: str, instance: _T) -> _T:
    return cast(_T, reference(instance, reference_type, inverse=True))


def propertyOf(instance: _T, /) -> _T:
    return _inverse(_HAS_PROPERTY, instance)


def componentOf(instance: _T, /) -> _T:
    return _inverse(_HAS_COMPONENT, instance)


def organizedBy(instance: _T, /) -> _T:
    return _inverse("i=35", instance)


def eventSourceOf(instance: _T, /) -> _T:
    return _inverse("i=36", instance)


def generatedBy(instance: _T, /) -> _T:
    return _inverse("i=41", instance)


def notifierOf(instance: _T, /) -> _T:
    return _inverse("i=48", instance)


def orderedComponentOf(instance: _T, /) -> _T:
    return _inverse("i=49", instance)


def isConditionOf(instance: _T, /) -> _T:
    return _inverse("i=9006", instance)


def interfaceOf(instance: _T, /) -> _T:
    return _inverse("i=17603", instance)


def addInOf(instance: _T, /) -> _T:
    return _inverse("i=17604", instance)
