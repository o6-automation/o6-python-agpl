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
    """Describe a declarative linkage or add a reference between live nodes.

    Two forms exist. `o6.reference(instance, referenceType)` attaches a node
    declaration to the type or Object that contains it through an arbitrary
    ReferenceType, and returns the same declaration so it can be assigned to a
    class attribute. `o6.reference(source, referenceType, target)` adds a
    reference between two *live* nodes immediately.

    The named helpers -- `o6.hasComponent`, `o6.hasProperty`, `o6.organizes`
    and their inverses -- are this function bound to a standard ReferenceType.
    Reach for `o6.reference` for a custom or non-standard ReferenceType.

    Args:
        subject: The node declaration to attach, the live source node of a
            two-ended reference, or `None` to describe the relationship without
            a target yet. `None` is only valid in the two-argument form.
        referenceType: Any NodeId-like value or generated ReferenceType class.
        object: The target of a two-ended reference. Live nodes are linked at
            once; a declaration becomes a child of the declaring type.
        inverse: Point the reference at the subject instead of away from it.
        server: The server that owns a live reference. Only needed when neither
            endpoint is a live node and more than one server is running.

    Raises:
        TypeError: The subject is neither a node declaration nor a live node,
            the endpoints belong to different servers, `server=` is combined
            with the two-argument form, or a Method is attached with
            `o6.hasProperty`.

    See [Type child relationships](../manual/server/declared-types.md#type-child-relationships) for
    how declared children, optionality, and ownership fit together.
    """
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
    """Attach a declaration to its containing type through `HasProperty`.

    Returns the declaration unchanged, so the static type of the class
    attribute is preserved. Pass `None` to declare the relationship without a
    target instance. On a generated enumeration, this also keeps the linked
    node out of Python's enum member table.

    See [Type child relationships](../manual/server/declared-types.md#type-child-relationships).
    """
    return reference(instance, _HAS_PROPERTY)


@overload
def hasComponent(instance: None, /) -> Any: ...


@overload
def hasComponent(instance: _T, /) -> _T: ...


def hasComponent(instance: _T | None, /) -> Any:
    """Attach a declaration to its containing type through `HasComponent`.

    Returns the declaration unchanged, so the static type of the class
    attribute is preserved. Works for Variables, Objects, Methods, and their
    subtypes. Pass `None` to declare the relationship without a target
    instance.

    See [Type child relationships](../manual/server/declared-types.md#type-child-relationships).
    """
    return reference(instance, _HAS_COMPONENT)


def hasEncoding(subject: _T, object: Any = UNSET, /) -> _T:
    """Link a DataType to one of its encodings through `HasEncoding`.

    With one argument, attaches the declaration to its containing type. With
    two, links the DataType `subject` to the encoding node `object`.

    See [Type child relationships](../manual/server/declared-types.md#type-child-relationships).
    """
    return (
        cast(_T, reference(subject, "i=38"))
        if object is UNSET
        else cast(_T, reference(subject, "i=38", object))
    )


def _forward(reference_type: str, instance: _T | None) -> Any:
    return reference(instance, reference_type)


def organizes(instance: _T | None, /) -> Any:
    """Attach a declaration to its containing node through `Organizes`.

    The non-type hierarchy used for folders and free-standing instances. Pass
    `None` to declare the relationship without a target instance.

    See [Type child relationships](../manual/server/declared-types.md#type-child-relationships).
    """
    return _forward("i=35", instance)


def hasEventSource(instance: _T | None, /) -> Any:
    """Attach a declaration to its containing node through `HasEventSource`.

    Marks the target as an event source of the declaring node. Pass `None` to
    declare the relationship without a target instance.

    See [Type child relationships](../manual/server/declared-types.md#type-child-relationships).
    """
    return _forward("i=36", instance)


def generatesEvent(instance: _T | None, /) -> Any:
    """Declare that the containing type emits an EventType, via `GeneratesEvent`.

    The target is the EventType, not an instance. Pass `None` to declare the
    relationship without a target.

    See [Type child relationships](../manual/server/declared-types.md#type-child-relationships).
    """
    return _forward("i=41", instance)


def hasNotifier(instance: _T | None, /) -> Any:
    """Attach a declaration to its containing node through `HasNotifier`.

    The event-hierarchy subtype of `HasEventSource` used between Objects that
    forward events. Pass `None` to declare the relationship without a target
    instance.

    See [Type child relationships](../manual/server/declared-types.md#type-child-relationships).
    """
    return _forward("i=48", instance)


def hasOrderedComponent(instance: _T | None, /) -> Any:
    """Attach a declaration through `HasOrderedComponent`.

    The subtype of `HasComponent` whose targets carry a defined order, used by
    `IOrderedObjectType`. Pass `None` to declare the relationship without a
    target instance.

    See [Type child relationships](../manual/server/declared-types.md#type-child-relationships).
    """
    return _forward("i=49", instance)


def hasCondition(instance: _T | None, /) -> Any:
    """Attach a declaration to its containing node through `HasCondition`.

    Links a node to the ConditionType or Condition instance that reports on it.
    Pass `None` to declare the relationship without a target.

    See [Type child relationships](../manual/server/declared-types.md#type-child-relationships).
    """
    return _forward("i=9006", instance)


def hasInterface(instance: _T | None, /) -> Any:
    """Attach a declaration to its containing node through `HasInterface`.

    Declared types normally list their InterfaceTypes in the `interfaces`
    argument of `o6.objecttype` or `o6.variabletype`; this helper covers the
    remaining cases where the reference is declared like any other child.

    See [Type interfaces](../manual/server/declared-types.md#type-interfaces).
    """
    return _forward("i=17603", instance)


def hasAddIn(instance: _T | None, /) -> Any:
    """Attach a declaration to its containing node through `HasAddIn`.

    The DI-style hierarchy for optional add-in components. Pass `None` to
    declare the relationship without a target instance.

    See [Type child relationships](../manual/server/declared-types.md#type-child-relationships).
    """
    return _forward("i=17604", instance)


def _inverse(reference_type: str, instance: _T) -> _T:
    return cast(_T, reference(instance, reference_type, inverse=True))


def propertyOf(instance: _T, /) -> _T:
    """Attach a declaration through an inverse `HasProperty` reference.

    The inverse of [`hasProperty`][o6.hasProperty]: the declaring node becomes
    the Property of the target instead of its owner.
    """
    return _inverse(_HAS_PROPERTY, instance)


def componentOf(instance: _T, /) -> _T:
    """Attach a declaration through an inverse `HasComponent` reference.

    The inverse of [`hasComponent`][o6.hasComponent]: the declaring node
    becomes a component of the target instead of its owner.
    """
    return _inverse(_HAS_COMPONENT, instance)


def organizedBy(instance: _T, /) -> _T:
    """Attach a declaration through an inverse `Organizes` reference.

    The inverse of [`organizes`][o6.organizes], which places the declaring node
    inside the target folder rather than the other way round.
    """
    return _inverse("i=35", instance)


def eventSourceOf(instance: _T, /) -> _T:
    """Attach a declaration through an inverse `HasEventSource` reference.

    The inverse of [`hasEventSource`][o6.hasEventSource]: the declaring node is
    the event source of the target.
    """
    return _inverse("i=36", instance)


def generatedBy(instance: _T, /) -> _T:
    """Attach a declaration through an inverse `GeneratesEvent` reference.

    The inverse of [`generatesEvent`][o6.generatesEvent]: the declaring
    EventType is generated by the target.
    """
    return _inverse("i=41", instance)


def notifierOf(instance: _T, /) -> _T:
    """Attach a declaration through an inverse `HasNotifier` reference.

    The inverse of [`hasNotifier`][o6.hasNotifier]: the declaring node notifies
    the target.
    """
    return _inverse("i=48", instance)


def orderedComponentOf(instance: _T, /) -> _T:
    """Attach a declaration through an inverse `HasOrderedComponent` reference.

    The inverse of [`hasOrderedComponent`][o6.hasOrderedComponent]: the
    declaring node is an ordered component of the target.
    """
    return _inverse("i=49", instance)


def isConditionOf(instance: _T, /) -> _T:
    """Attach a declaration through an inverse `HasCondition` reference.

    The inverse of [`hasCondition`][o6.hasCondition]: the declaring Condition
    reports on the target node.
    """
    return _inverse("i=9006", instance)


def interfaceOf(instance: _T, /) -> _T:
    """Attach a declaration through an inverse `HasInterface` reference.

    The inverse of [`hasInterface`][o6.hasInterface]: the declaring
    InterfaceType is implemented by the target.
    """
    return _inverse("i=17603", instance)


def addInOf(instance: _T, /) -> _T:
    """Attach a declaration through an inverse `HasAddIn` reference.

    The inverse of [`hasAddIn`][o6.hasAddIn]: the declaring node is an add-in
    of the target.
    """
    return _inverse("i=17604", instance)
