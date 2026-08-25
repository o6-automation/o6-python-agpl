# Copyright 2026 (c) o6 Automation GmbH
"""Declarative OPC UA node-type and node-instance authoring APIs."""

from __future__ import annotations

import sys

from types import FrameType
from collections.abc import Iterator, Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Optional,
    TypeVar,
    cast,
    overload,
)

import numpy as np

import o6
from o6._declarations import (
    InstanceDeclaration,
    MethodSpec,
    NODE_ID_DESCRIPTOR as _NODE_ID_DESCRIPTOR,
    ObjectSpec,
    ObjectTypeSpec,
    ReferenceTypeSpec,
    TypeDeclaration,
    TypeSpec,
    UndefinedReference,
    VariableSpec,
    VariableTypeSpec,
    ViewSpec,
    _NodeClass,
    _abstract_new,
    _attach_declared_child,
    _browse_name_key,
    _child_declarations_by_key,
    _collect_children,
    _declared_bases,
    _declared_node_dir,
    _decorator_description,
    _declaration_values,
    _declared_type_nodeclass,
    _is_node_declaration,
    _instance_kind,
    _instance_declaration,
    _instance_child_override,
    _instance_nodeid,
    _instance_node_type,
    _modelling_rule_nodeid,
    _type_declaration,
    _with_node_type_meta,
    _new_nodeid,
    _normalize_role_permissions,
    _register_declaration,
    _remove_instance_root,
    _store_instance_child,
    _resolve_namespace,
    _resolve_type_identity,
    safe_setattr,
)

_T = TypeVar("_T")
_F = TypeVar("_F", bound=Callable[..., Any])
_UNSET = object()

if TYPE_CHECKING:
    from o6.node import ViewNode


# =============================================================================
# Portable type-declaration constants
# =============================================================================


_BASE_DATA_TYPE = "ns=ns0;i=24"


def _build_declared_type(
    klass: type[_T],
    *,
    nodeclass: _NodeClass,
    nodeid: Any,
    browsename: str,
    displayname: str,
    description: Optional[str],
    writemask: Optional[int],
    user_writemask: Optional[int],
    role_permissions: Optional[Mapping[Any, int]],
    access_restrictions: int,
    type_spec: TypeSpec,
    interfaces: tuple[Any, ...] = (),
) -> type[_T]:
    """Build a metadata-only VariableType or ObjectType marker class."""
    from o6._declarations import _OWN_VARIABLE_SLOT
    from o6._server_types import _callback_bindings, _validate_method_targets

    klass = _with_node_type_meta(klass)
    children = _collect_children(klass)
    bindings = _callback_bindings(klass)
    child_names = set(getattr(klass, "__annotations__", None) or {})
    for name, value in tuple(vars(klass).items()):
        if name in child_names and (
            isinstance(value, (InstanceDeclaration, UndefinedReference))
            or _is_node_declaration(value)
        ):
            delattr(klass, name)
    setattr(klass, "__new__", staticmethod(_instance_new))
    setattr(klass, "__dir__", _declared_node_dir)
    inherited_initializer = getattr(klass, "__init__", object.__init__)
    if vars(klass).get("__init__") is None and (
        inherited_initializer is object.__init__
        or getattr(inherited_initializer, "__module__", None) == "o6.node"
    ):
        setattr(klass, "__init__", _instance_init)
    _validate_method_targets(klass, children, interfaces)
    if not isinstance(type_spec, VariableTypeSpec) and (
        ("read", _OWN_VARIABLE_SLOT) in bindings or ("write", _OWN_VARIABLE_SLOT) in bindings
    ):
        raise TypeError("@o6.read and @o6.write require a @o6.variabletype class")
    py_type = klass

    declaration = TypeDeclaration(
        nodeid=o6.NodeId(nodeid),
        nodeclass=nodeclass,
        browsename=browsename,
        displayname=displayname,
        description=description,
        writemask=writemask,
        user_writemask=user_writemask,
        role_permissions=_normalize_role_permissions(role_permissions),
        access_restrictions=int(access_restrictions),
        attributes=type_spec,
        bases=_declared_bases(klass, type(type_spec)) or (),
        interfaces=interfaces,
        instances=children,
    )
    safe_setattr(py_type, "__o6_declaration__", declaration)
    safe_setattr(py_type, "_nodeid", _NODE_ID_DESCRIPTOR)
    return _register_declaration(cast(type[_T], py_type))


# =============================================================================
# Instance ownership and constructor dispatch
# =============================================================================


def _instance_new(cls: type, *, server: Any = _UNSET, **_kwargs: Any) -> Any:
    """Create either an ordinary declaration instance or a live server node."""
    declaration = _type_declaration(cls)
    kind = _instance_kind(declaration.nodeclass)
    parent = _kwargs.get("parent")
    is_declaration = server is None or (
        server is _UNSET and (_is_node_declaration(parent) or _called_from_namespace_module())
    )
    resolved = None if is_declaration else _resolve_instance_server(server=server, parent=parent)
    # Abstract types may still describe placeholder children in a
    # type declaration. They cannot be materialized as live address-space
    # instances.
    if (
        declaration.is_abstract
        and not _kwargs.get("_allow_abstract")
        and (
            resolved is not None
            or _kwargs.get("parent") is not None
            or (_kwargs.get("nodeId") is None and _kwargs.get("nodeid") is None)
        )
    ):
        raise TypeError(f"cannot instantiate abstract {kind} {cls.__name__!r}")
    if resolved is None:
        node_type = _instance_node_type(declaration.nodeclass)
        obj: Any = node_type.__new__(cls) if issubclass(cls, node_type) else object.__new__(cls)
    else:
        from o6._server_construction import _new_live_instance

        init_kwargs = dict(_kwargs)
        if server is not _UNSET:
            init_kwargs["server"] = server
        obj = _new_live_instance(cls, resolved, _kwargs, init_kwargs)
    return obj


def _parent_server(parent: Any) -> Any:
    """Return the server carried by a live parent node, if any."""
    if _is_node_declaration(parent):
        return None
    backend = getattr(parent, "_backend", None)
    return getattr(backend, "_server", None)


def _called_from_namespace_module() -> bool:
    """Whether this constructor call is executing in a registered namespace module."""
    try:
        frame: FrameType | None = sys._getframe(2)
    except ValueError:
        return False
    while frame is not None:
        if "__NAMESPACES__" in frame.f_globals and frame.f_code.co_name == "<module>":
            return True
        if "__module__" in frame.f_locals and "__qualname__" in frame.f_locals:
            return True
        frame = frame.f_back
    return False


def _resolve_instance_server(*, server: Any, parent: Any) -> Any:
    """Resolve omitted instance ownership to a server or a declaration."""
    parent_server = _parent_server(parent)

    if server is not _UNSET:
        if server is not None and parent_server is not None and server is not parent_server:
            raise TypeError("server= and the live parent node belong to different servers")
        return server

    if parent_server is not None:
        return parent_server
    if _is_node_declaration(parent):
        return None
    if _called_from_namespace_module():
        return None

    from o6.server import _get_live_servers

    live = _get_live_servers()
    if not live:
        return None
    if len(live) == 1:
        return live[0]
    raise TypeError(
        "cannot infer server: multiple live servers exist; pass server=<server> "
        "or server=None explicitly"
    )


def _instance_init(
    self: Any,
    *,
    server: Any = _UNSET,
    nodeId: Optional[o6.NodeIdLike] = None,
    parent: Optional[o6.NodeIdLike] = None,
    browseName: Optional[str | o6.QualifiedName] = None,
    referenceType: Optional[o6.NodeIdLike] = None,
    value: Any = None,
    values: Optional[dict[str, Any]] = None,
    references: Optional[list[Any]] = None,
    dataType: Optional[o6.NodeIdLike] = None,
    valueRank: Optional[int] = None,
    arrayDimensions: Optional[list[int]] = None,
    accessLevel: Optional[int] = None,
    userAccessLevel: Optional[int] = None,
    minimumSamplingInterval: Optional[float] = None,
    historizing: bool = False,
    writeMask: Optional[int] = None,
    userWriteMask: Optional[int] = None,
    rolePermissions: Optional[Mapping[Any, int]] = None,
    accessRestrictions: int = 0,
    eventNotifier: int = 0,
    description: Optional[str] = None,
    displayName: Optional[str] = None,
    modellingRule: Optional[str] = None,
    _allow_abstract: bool = False,
) -> None:
    """Initialize an ordinary node declaration; live construction belongs to __new__."""
    is_attached = getattr(self, "_is_native_attached", None)
    if callable(is_attached) and is_attached():
        return
    declaration = _type_declaration(type(self))
    type_spec = declaration.attributes
    if isinstance(type_spec, ObjectTypeSpec) and (
        value is not None or dataType is not None or valueRank is not None
    ):
        raise TypeError(
            f"{type(self).__name__}(...): value/dataType/valueRank are variable-only "
            "(an Object instance carries no Value)."
        )
    marker = type(self)
    nodeclass = {
        _NodeClass.OBJECT_TYPE: _NodeClass.OBJECT,
        _NodeClass.VARIABLE_TYPE: _NodeClass.VARIABLE,
    }[declaration.nodeclass]
    inherited_value = getattr(type_spec, "value", None)
    if dataType is not None and getattr(type_spec, "data_type", None) != o6.NodeId(dataType):
        inherited_value = None
    actual_value = value if value is not None else inherited_value
    if isinstance(actual_value, Iterator):
        actual_value = list(actual_value)
    if valueRank is not None and valueRank > 1 and isinstance(actual_value, (list, tuple)):
        actual_value = np.asarray(actual_value)
    if isinstance(type_spec, VariableTypeSpec):
        if _declared_type_nodeclass(dataType) is not None:
            raise TypeError(
                "dataType= expects a UA DataType, not a VariableType or ObjectType; "
                "annotate the member with its concrete child type"
            )
        attributes: ObjectSpec | VariableSpec = VariableSpec(
            data_type=o6.NodeId(dataType) if dataType is not None else type_spec.data_type,
            value_rank=(
                valueRank
                if valueRank is not None
                else (-1 if dataType is not None else type_spec.value_rank)
            ),
            array_dimensions=(
                list(arrayDimensions) if arrayDimensions is not None else type_spec.array_dimensions
            ),
            value=actual_value,
            access_level=accessLevel,
            user_access_level=userAccessLevel,
            minimum_sampling_interval=minimumSamplingInterval,
            historizing=historizing,
        )
    else:
        attributes = ObjectSpec(event_notifier=eventNotifier)
    rule = (
        _modelling_rule_nodeid(modellingRule) or modellingRule
        if modellingRule is not None
        else None
    )
    parent_declaration = _is_node_declaration(parent)
    instance_declaration = InstanceDeclaration(
        browsename=str(browseName) if browseName is not None else "",
        nodeclass=nodeclass,
        reference_type=o6.NodeId(referenceType or "i=47"),
        attributes=attributes,
        typeTarget=marker,
        modelling_rule=rule,
        writemask=writeMask,
        user_writemask=userWriteMask,
        role_permissions=_normalize_role_permissions(rolePermissions),
        access_restrictions=int(accessRestrictions),
        description=description,
        displayname=displayName,
        nodeid=_instance_nodeid(nodeId),
        parent=None if parent_declaration else parent,
        allow_abstract=_allow_abstract,
    )
    self.__dict__.update(
        _is_live=False,
        _backend=None,
        __o6_declaration__=instance_declaration,
    )
    _attach_declared_child(parent, self)
    for child in references or ():
        _declaration_values(child)
        child_declaration = _instance_declaration(child)
        _store_instance_child(instance_declaration, child_declaration)
        child_declaration.parent = None
        _remove_instance_root(child)
    if values:
        declarations = _child_declarations_by_key(marker)
        for name, child_value in values.items():
            child = declarations.get(_browse_name_key(name))
            if child is None:
                raise KeyError(f"{marker.__name__} has no child {name!r}")
            child_declaration = _instance_child_override(child, child_value)
            _store_instance_child(instance_declaration, child_declaration)
            if child.python_name is not None:
                setattr(self, child.python_name, child_value)
    _register_declaration(self, instance=True)


# =============================================================================
# ReferenceType, VariableType, and ObjectType authoring
# =============================================================================


def _resolve_interfaces(interfaces: Optional[list[Any]]) -> tuple[Any, ...]:
    """Validate and deduplicate explicit OPC UA InterfaceType targets."""
    resolved: list[Any] = []
    seen: set[str] = set()
    for interface in interfaces or ():
        if isinstance(interface, type):
            declaration = vars(interface).get("__o6_declaration__")
            if not isinstance(declaration, TypeDeclaration) or not isinstance(
                declaration.attributes, ObjectTypeSpec
            ):
                raise TypeError("interfaces= entries must be ObjectType markers")
            if not any(
                isinstance(vars(base).get("__o6_declaration__"), TypeDeclaration)
                and str(_type_declaration(base).nodeid) == "i=17602"
                for base in interface.__mro__
            ):
                raise TypeError(f"{interface.__name__} is not derived from BaseInterfaceType")
        try:
            key = str(o6.NodeId(interface))
        except (TypeError, ValueError) as exc:
            raise TypeError("interfaces= entries must be InterfaceType markers or NodeIds") from exc
        if key not in seen:
            seen.add(key)
            resolved.append(interface)
    return tuple(resolved)


def referencetype(
    *,
    ns: Optional[str] = None,
    nodeId: Optional[str] = None,
    browseName: Optional[str] = None,
    displayName: Optional[str] = None,
    description: Optional[str] = None,
    writeMask: Optional[bool] = None,
    userWriteMask: Optional[bool] = None,
    rolePermissions: Optional[Mapping[Any, int]] = None,
    accessRestrictions: int = 0,
    isAbstract: bool = False,
    symmetric: bool = False,
    inverseName: Optional[str] = None,
) -> Any:
    """Declare a custom OPC UA ReferenceType.

    The decorated class is a metadata-only marker: it is never instantiated,
    and its Python base class becomes the `HasSubtype` parent, so
    `class Controls(ns0.reftypes.NonHierarchicalReferences)` declares a subtype
    of `NonHierarchicalReferences`. Annotated fields are rejected, because a
    ReferenceType has no wire layout. Pass the resulting class wherever a
    ReferenceType is expected, for example to
    [`o6.reference`][o6.reference].

    Args:
        ns: Shortname of the declaring namespace. Inferred from `nodeId` when
            that carries a namespace, otherwise required.
        nodeId: NodeId of the ReferenceType node. Allocated in the declaring
            namespace when omitted.
        browseName: BrowseName of the node. Defaults to the class name.
        displayName: DisplayName of the node. Defaults to the BrowseName.
        description: Description attribute. Defaults to the class docstring.
        writeMask: WriteMask attribute of the node.
        userWriteMask: UserWriteMask attribute of the node.
        rolePermissions: RolePermissions, as a mapping of role to
            [`PermissionType`][o6.ns.ns0.datatypes.PermissionType] mask.
        accessRestrictions: AccessRestrictions attribute of the node.
        isAbstract: Declare the ReferenceType abstract, so only its subtypes
            may be used in references.
        symmetric: Declare the reference symmetric, which means it reads the
            same in both directions and has no separate InverseName.
        inverseName: InverseName attribute, the name of the reverse direction.
            Required by OPC UA for a non-symmetric, non-abstract ReferenceType.

    Raises:
        TypeError: The decorated object is not a class, or the class has
            annotated fields.

    See [`@o6.referencetype` — custom references](../manual/sdk-fundamentals/namespace/writing-nodesets-in-python.md#o6referencetype-custom-references).
    """
    ns = _resolve_namespace(ns, nodeId)

    def decorator(klass: type) -> type:
        if not isinstance(klass, type):
            raise TypeError(f"o6.referencetype: expected a class, got {type(klass).__name__}")

        if getattr(klass, "__annotations__", None):
            raise TypeError(
                f"o6.referencetype: {klass.__name__!r} must not have annotated fields. "
                "ReferenceTypes are a type-system placeholder, not a wire layout."
            )

        actual_nodeid, actual_browsename, actual_displayname = _resolve_type_identity(
            klass, ns, nodeId, browseName, displayName
        )

        # Build the marker class. ReferenceType is metadata-only
        body: dict[str, Any] = {
            attr_name: attr_value
            for attr_name, attr_value in vars(klass).items()
            if attr_name not in ("__dict__", "__weakref__")
        }
        body["__slots__"] = ()
        # ReferenceType is never instantiable: there is no UA_DataType,
        # so neither "abstract" nor "concrete" markers carry an allocator.
        # The custom ``__new__`` rejects any attempt at instantiation.
        body["__new__"] = lambda cls, *a, **kw: _abstract_new(cls, "reference type")
        py_type = type(
            klass.__name__,
            # Preserve the MRO the user wrote (`class Foo(Bar):`) so
            # `HasSubtype` chains in the IR resolve at module load time.
            _declared_bases(klass, ReferenceTypeSpec) or klass.__bases__,
            body,
        )

        declaration = TypeDeclaration(
            nodeid=o6.NodeId(actual_nodeid),
            nodeclass=_NodeClass.REFERENCE_TYPE,
            browsename=actual_browsename,
            displayname=actual_displayname,
            description=_decorator_description(klass, description),
            writemask=writeMask,
            user_writemask=userWriteMask,
            role_permissions=_normalize_role_permissions(rolePermissions),
            access_restrictions=int(accessRestrictions),
            attributes=ReferenceTypeSpec(
                is_abstract=bool(isAbstract),
                is_symmetric=bool(symmetric),
                inverse_name=o6.LocalizedText(inverseName) if inverseName is not None else None,
            ),
            bases=_declared_bases(py_type, ReferenceTypeSpec) or (),
        )
        safe_setattr(py_type, "__o6_declaration__", declaration)
        safe_setattr(py_type, "_nodeid", _NODE_ID_DESCRIPTOR)

        # ReferenceType is metadata-only, no C-side
        # The server discovers reference-type markers by walking the host module's class attributes.
        return _register_declaration(py_type)

    return decorator


def variabletype(
    *,
    ns: Optional[str] = None,
    nodeId: Optional[str] = None,
    browseName: Optional[str] = None,
    displayName: Optional[str] = None,
    description: Optional[str] = None,
    writeMask: Optional[int] = None,
    userWriteMask: Optional[int] = None,
    rolePermissions: Optional[Mapping[Any, int]] = None,
    accessRestrictions: int = 0,
    isAbstract: bool = False,
    dataType: Any = None,
    valueRank: Optional[int] = None,
    arrayDimensions: Optional[list[int]] = None,
    value: Optional[Any] = None,
    interfaces: Optional[list[Any]] = None,
) -> Callable[[type[_T]], type[_T]]:
    """Declare an OPC UA VariableType from a Python class.

    The Python base class becomes the `HasSubtype` parent, so
    `class TemperatureType(ns0.vartypes.BaseDataVariableType)` declares a
    subtype of `BaseDataVariableType`. Annotated class attributes assigned with
    a reference helper such as [`o6.hasProperty`][o6.hasProperty] become
    instance declarations of the type, and `Optional[T]` on the annotation makes
    the child Optional rather than Mandatory.

    Calling the decorated class afterwards either creates a live server node or
    another declaration, depending on the `server` and `parent` arguments of the
    call.

    `dataType`, `valueRank`, and `arrayDimensions` are inherited from the
    `HasSubtype` parent when omitted, because OPC UA requires a subtype's value
    constraints to be equal to or narrower than its parent's. A root type with
    no VariableType base falls back to `BaseDataType` and `ValueRank.ANY`.

    Args:
        ns: Shortname of the declaring namespace. Inferred from `nodeId` when
            that carries a namespace, otherwise required.
        nodeId: NodeId of the VariableType node. Allocated in the declaring
            namespace when omitted.
        browseName: BrowseName of the node. Defaults to the class name.
        displayName: DisplayName of the node. Defaults to the BrowseName.
        description: Description attribute. Defaults to the class docstring.
        writeMask: WriteMask attribute of the node.
        userWriteMask: UserWriteMask attribute of the node.
        rolePermissions: RolePermissions, as a mapping of role to
            [`PermissionType`][o6.ns.ns0.datatypes.PermissionType] mask.
        accessRestrictions: AccessRestrictions attribute of the node.
        isAbstract: Declare the type abstract, so it cannot be instantiated.
        dataType: DataType of the value: an `o6` builtin type, a generated
            DataType class, or any NodeId-like value.
        valueRank: ValueRank of the value, for example
            [`o6.ValueRank.SCALAR`][o6.common.ValueRank].
        arrayDimensions: ArrayDimensions of the value.
        value: Default value carried by the type node itself.
        interfaces: OPC UA InterfaceTypes this type implements. They become
            `HasInterface` references and do not enter the Python MRO.

    Raises:
        TypeError: The decorated object is not a class, or an entry of
            `interfaces` is not an InterfaceType.

    See [`@o6.variabletype` — typed Variables](../manual/sdk-fundamentals/namespace/writing-nodesets-in-python.md#o6variabletype-typed-variables).
    """
    ns = _resolve_namespace(ns, nodeId)

    def decorator(klass: type[_T]) -> type[_T]:
        if not isinstance(klass, type):
            raise TypeError(f"o6.variabletype: expected a class, got {type(klass).__name__}")

        actual_nodeid, actual_browsename, actual_displayname = _resolve_type_identity(
            klass, ns, nodeId, browseName, displayName
        )
        vt_bases = _declared_bases(klass, VariableTypeSpec)
        # The value constraints (DataType / ValueRank / ArrayDimensions) are
        # *inherited from the HasSubtype parent* when omitted. OPC UA requires
        # a subtype's constraints to be equal-or-narrower than its parent's;
        # inheriting the parent's is the safe default (a bare ``BaseDataType``
        # / ``ANY`` would be *broader* and rejected as an invalid subtype).
        # A root type (no VariableType base) falls back to the open62541
        # defaults: BaseDataType and ValueRank.ANY (-2).
        parent_spec = None
        if vt_bases:
            for base in vt_bases:
                candidate = _type_declaration(base).attributes
                if isinstance(candidate, VariableTypeSpec):
                    parent_spec = candidate
                    break

        if dataType is not None:
            actual_data_type = o6.NodeId(dataType)
        elif parent_spec is not None:
            actual_data_type = parent_spec.data_type
        else:
            actual_data_type = o6.NodeId(_BASE_DATA_TYPE)

        if valueRank is not None:
            actual_value_rank = int(valueRank)
        elif parent_spec is not None:
            actual_value_rank = parent_spec.value_rank
        else:
            actual_value_rank = -2  # ValueRank.ANY

        if arrayDimensions is not None:
            actual_array_dimensions: Optional[list[int]] = list(arrayDimensions)
        elif parent_spec is not None:
            actual_array_dimensions = (
                list(parent_spec.array_dimensions)
                if parent_spec.array_dimensions is not None
                else None
            )
        else:
            actual_array_dimensions = None

        return _build_declared_type(
            klass,
            nodeclass=_NodeClass.VARIABLE_TYPE,
            nodeid=actual_nodeid,
            browsename=actual_browsename,
            displayname=actual_displayname,
            description=_decorator_description(klass, description),
            writemask=writeMask,
            user_writemask=userWriteMask,
            role_permissions=rolePermissions,
            access_restrictions=accessRestrictions,
            type_spec=VariableTypeSpec(
                is_abstract=isAbstract,
                data_type=actual_data_type,
                value_rank=actual_value_rank,
                array_dimensions=actual_array_dimensions,
                value=value,
            ),
            interfaces=_resolve_interfaces(interfaces),
        )

    return decorator


def objecttype(
    *,
    ns: Optional[str] = None,
    nodeId: Optional[str] = None,
    browseName: Optional[str] = None,
    displayName: Optional[str] = None,
    description: Optional[str] = None,
    writeMask: Optional[int] = None,
    userWriteMask: Optional[int] = None,
    rolePermissions: Optional[Mapping[Any, int]] = None,
    accessRestrictions: int = 0,
    isAbstract: bool = False,
    interfaces: Optional[list[Any]] = None,
) -> Callable[[type[_T]], type[_T]]:
    """Declare an OPC UA ObjectType from a Python class.

    The Python base class becomes the `HasSubtype` parent, so
    `class MachineType(ns0.objtypes.BaseObjectType)` declares a subtype of
    `BaseObjectType`. Annotated class attributes assigned with a reference
    helper such as [`o6.hasComponent`][o6.hasComponent] become instance
    declarations of the type, Methods are declared with [`o6.call`][o6.call],
    and `Optional[T]` on the annotation makes the child Optional rather than
    Mandatory.

    Calling the decorated class afterwards either creates a live server node or
    another declaration, depending on the `server` and `parent` arguments of the
    call. Behaviour is added separately, either by subclassing the declared type
    or with [`Server.implement`][o6.server.Server].

    Args:
        ns: Shortname of the declaring namespace. Inferred from `nodeId` when
            that carries a namespace, otherwise required.
        nodeId: NodeId of the ObjectType node. Allocated in the declaring
            namespace when omitted.
        browseName: BrowseName of the node. Defaults to the class name.
        displayName: DisplayName of the node. Defaults to the BrowseName.
        description: Description attribute. Defaults to the class docstring.
        writeMask: WriteMask attribute of the node.
        userWriteMask: UserWriteMask attribute of the node.
        rolePermissions: RolePermissions, as a mapping of role to
            [`PermissionType`][o6.ns.ns0.datatypes.PermissionType] mask.
        accessRestrictions: AccessRestrictions attribute of the node.
        isAbstract: Declare the type abstract, so it cannot be instantiated.
        interfaces: OPC UA InterfaceTypes this type implements. They become
            `HasInterface` references and do not enter the Python MRO; their
            Mandatory members are instantiated by the normal OPC UA rules.

    Raises:
        TypeError: The decorated object is not a class, or an entry of
            `interfaces` is not an InterfaceType.

    See [`@o6.objecttype` — typed Objects](../manual/sdk-fundamentals/namespace/writing-nodesets-in-python.md#o6objecttype-typed-objects).
    """
    ns = _resolve_namespace(ns, nodeId)

    def decorator(klass: type[_T]) -> type[_T]:
        if not isinstance(klass, type):
            raise TypeError(f"o6.objecttype: expected a class, got {type(klass).__name__}")

        actual_nodeid, actual_browsename, actual_displayname = _resolve_type_identity(
            klass, ns, nodeId, browseName, displayName
        )
        return _build_declared_type(
            klass,
            nodeclass=_NodeClass.OBJECT_TYPE,
            nodeid=actual_nodeid,
            browsename=actual_browsename,
            displayname=actual_displayname,
            description=_decorator_description(klass, description),
            writemask=writeMask,
            user_writemask=userWriteMask,
            role_permissions=rolePermissions,
            access_restrictions=accessRestrictions,
            type_spec=ObjectTypeSpec(is_abstract=isAbstract),
            interfaces=_resolve_interfaces(interfaces),
        )

    return decorator


# =============================================================================
# Method and variable callback authoring
# =============================================================================


@overload
def call(target: str, /) -> Callable[[_F], _F]: ...


@overload
def call(
    *,
    browseName: Optional[str] = None,
    nodeId: Optional[str] = None,
    inputArgs: Optional[list[Any]] = None,
    outputArgs: Optional[list[Any]] = None,
    executable: bool = True,
    userExecutable: bool = True,
    modellingRule: Optional[str] = None,
    referenceType: Optional[Any] = None,
    parent: Optional[Any] = None,
    description: Optional[str] = None,
    displayName: Optional[str] = None,
    writeMask: Optional[int] = None,
    userWriteMask: Optional[int] = None,
    rolePermissions: Optional[Mapping[Any, int]] = None,
    accessRestrictions: int = 0,
) -> Any: ...


def call(
    target: str | None = None,
    /,
    *,
    browseName: Optional[str] = None,
    nodeId: Optional[str] = None,
    inputArgs: Optional[list[Any]] = None,
    outputArgs: Optional[list[Any]] = None,
    executable: bool = True,
    userExecutable: bool = True,
    modellingRule: Optional[str] = None,
    referenceType: Optional[Any] = None,
    parent: Optional[Any] = None,
    description: Optional[str] = None,
    displayName: Optional[str] = None,
    writeMask: Optional[int] = None,
    userWriteMask: Optional[int] = None,
    rolePermissions: Optional[Mapping[Any, int]] = None,
    accessRestrictions: int = 0,
) -> Any:
    """Declare an OPC UA Method child, or bind a Python implementation to one.

    With keyword arguments, `o6.call(...)` declares a Method instance
    declaration in the body of a `@o6.objecttype` (or, rarely,
    `@o6.variabletype`) class. The child is attached with `HasComponent` unless
    `referenceType` says otherwise; annotate it as
    `Optional[o6.node.MethodNode]` to make the linkage Optional.

    ```python
    @o6.objecttype(ns="plant")
    class MachineType(ns0.objtypes.BaseObjectType):
        reset: o6.node.MethodNode = o6.hasComponent(
            o6.call(
                browseName="ns=plant;Reset",
                inputArgs=[ns0.datatypes.Argument(name="mode", dataType=o6.Int32)],
            )
        )
    ```

    With a positional target, `@o6.call("BrowseName")` binds a Python method as
    the implementation of a declared or inherited Method child, on an ObjectType
    or on an undecorated implementation subclass. The two forms cannot be mixed:
    passing declaration options together with a positional target raises
    `TypeError`.

    A dotted positional target is a Python member path, resolved once when the
    containing Object finishes, and stores the implementation with that Object on
    the concrete Method node:

    ```python
    class CellImpl(CellType):
        @o6.call("controller.reset")
        def resetController(self, mode):
            return (o6.StatusCode.GOOD,)
    ```

    The path uses generated Python member names, not OPC UA BrowseNames. It
    overrides behaviour copied from the Method's type implementation. As with
    [`o6.read`][o6.read] and [`o6.write`][o6.write] paths, clearing a callback
    later does not rerun Object construction or restore an earlier callback.

    Resolution happens once during Object creation. The most-derived matching
    type implementation is copied onto the concrete Method first. Dotted paths
    are then applied as containing Objects finish, replacing that concrete slot.
    Nested Objects finish before their containers, so an outer path that targets
    the same Method is applied last. The creation-time class lookup starts at the
    Object's concrete Python type and proceeds upwards through its base types. A
    subclass can override the same Python method normally, or repeat
    `@o6.call("BrowseName")` on a different Python method name. Invocation
    performs no class or path lookup: it calls the stored callback, or returns
    `BAD_NOT_IMPLEMENTED`.

    Every Object instance owns copies of its Mandatory and selected Optional
    Methods, so per-instance callbacks are isolated while both cases use the same
    construction-time resolution. Each class may associate only one Python method
    with a given qualified UA BrowseName; competing `@o6.call(...)` decorators
    raise `TypeError` naming the class, UA Method, and both Python attributes. A
    decorator that matches no declared, inherited, or interface Method is
    rejected as an unknown UA Method. Multiple inheritance is not ambiguous:
    normal Python type-hierarchy order selects the nearest base implementation.

    The invoking Object is part of the call, not of Method identity. Dot lookup
    returns a lightweight bound Method carrying the Object and Method node for
    that lookup, so `machine.reset()` works on clients and local servers alike.
    For a Method obtained directly by NodeId, pass the Object explicitly, as a
    node or a NodeId-like value:

    ```python
    reset = client[resetNodeId]
    reset(object=machine)
    ```

    Adding a reference never changes callback ownership.

    Args:
        target: BrowseName or dotted Python member path of the Method to
            implement. Selects the implementation form, and cannot be combined
            with any declaration option.
        browseName: BrowseName of the declared Method node.
        nodeId: NodeId of the declared Method node. Allocated in the declaring
            namespace when omitted.
        inputArgs: InputArguments, as a list of `ns0.datatypes.Argument` or a
            declared Variable holding them.
        outputArgs: OutputArguments, as a list of `ns0.datatypes.Argument` or a
            declared Variable holding them.
        executable: Executable attribute of the Method node.
        userExecutable: UserExecutable attribute of the Method node.
        modellingRule: Modelling rule of the child, for example `"Mandatory"`.
            Normally inferred from `Optional[...]` on the annotation instead.
        referenceType: ReferenceType linking the Method to its owner. Defaults
            to `HasComponent`.
        parent: Node or declaration that owns the Method, for a free-standing
            declaration outside a type body.
        description: Description attribute of the Method node.
        displayName: DisplayName attribute of the Method node.
        writeMask: WriteMask attribute of the Method node.
        userWriteMask: UserWriteMask attribute of the Method node.
        rolePermissions: RolePermissions, as a mapping of role to
            [`PermissionType`][o6.ns.ns0.datatypes.PermissionType] mask.
        accessRestrictions: AccessRestrictions attribute of the Method node.

    Raises:
        TypeError: A positional target is combined with declaration options, or
            `inputArgs`/`outputArgs` are declarations that are not Variables.

    See [Server callbacks](../manual/server/callbacks.md#one-resolution-rule) for the
    shared `read`/`write`/`call` precedence and reset behaviour.
    """
    if target is not None:
        declaration_options = (
            browseName,
            nodeId,
            inputArgs,
            outputArgs,
            modellingRule,
            referenceType,
            parent,
            description,
            displayName,
            writeMask,
            userWriteMask,
            rolePermissions,
        )
        if (
            any(option is not None for option in declaration_options)
            or not executable
            or not userExecutable
            or accessRestrictions != 0
        ):
            raise TypeError("positional call target cannot be combined with declaration options")
        from o6._server_types import _method_implementation

        return _method_implementation(target)
    for argument_value in (inputArgs, outputArgs):
        if _is_node_declaration(argument_value):
            _remove_instance_root(argument_value)

    def _arguments(value: Any) -> tuple[tuple[Any, ...], Optional[o6.NodeId]]:
        if _is_node_declaration(value):
            argument_declaration = _instance_declaration(value)
            payload = argument_declaration.attributes
            if not isinstance(payload, VariableSpec):
                raise TypeError("Method arguments must be declared Variables")
            raw = payload.value if payload.value is not None else ()
            return tuple(raw), argument_declaration.nodeid
        return tuple(value or ()), None

    input_args, input_nodeid = _arguments(inputArgs)
    output_args, output_nodeid = _arguments(outputArgs)
    rule = (
        _modelling_rule_nodeid(modellingRule) or modellingRule
        if modellingRule is not None
        else None
    )
    declaration = InstanceDeclaration(
        browsename=browseName or "",
        nodeclass=_NodeClass.METHOD,
        reference_type=o6.NodeId(referenceType or "i=47"),
        attributes=MethodSpec(
            input_args=input_args,
            output_args=output_args,
            input_args_nodeid=input_nodeid,
            output_args_nodeid=output_nodeid,
            executable=executable,
            user_executable=userExecutable,
        ),
        parent=None if _is_node_declaration(parent) else parent,
        nodeid=_instance_nodeid(nodeId),
        modelling_rule=rule,
        description=description,
        displayname=displayName,
        writemask=writeMask,
        user_writemask=userWriteMask,
        role_permissions=_normalize_role_permissions(rolePermissions),
        access_restrictions=int(accessRestrictions),
    )
    _attach_declared_child(parent, declaration)
    return _register_declaration(declaration, instance=True)


# =============================================================================
# View declarations
# =============================================================================


def view(
    *,
    nodeId: Optional[o6.NodeIdLike] = None,
    browseName: Optional[str] = None,
    displayName: Optional[o6.LocalizedTextLike] = None,
    description: Optional[o6.LocalizedTextLike] = None,
    containsNoLoops: bool = True,
    eventNotifier: int = 0,
    writeMask: int = 0,
    userWriteMask: int = 0,
    rolePermissions: Optional[Mapping[Any, int]] = None,
    accessRestrictions: int = 0,
    parent: Any = "i=87",
    referenceType: o6.NodeIdLike = "i=35",
    references: Optional[list[Any]] = None,
    ns: Optional[str] = None,
    server: Any = _UNSET,
) -> "ViewNode":
    """Declare or immediately create an OPC UA View node.

    A View narrows browsing to a chosen subset of the address space. The
    references listed in `references` are the View's members; nodes stay owned by
    their original parents.

    The return value is a live [`ViewNode`][o6.node.ViewNode] when a server is
    resolved, and an unmaterialized declaration otherwise. Resolution follows the
    same rules as declared type instances: an explicit `server` wins, then a live
    `parent`, and calls made while a registered namespace module is being
    evaluated stay declarations until `server.ns.append(module)` runs.

    Args:
        nodeId: NodeId of the View node. Allocated in `ns` when omitted.
        browseName: BrowseName of the node. Defaults to `"View"`.
        displayName: DisplayName of the node. Defaults to the BrowseName.
        description: Description attribute of the node.
        containsNoLoops: ContainsNoLoops attribute, asserting that browsing the
            View cannot revisit a node.
        eventNotifier: EventNotifier attribute of the node.
        writeMask: WriteMask attribute of the node.
        userWriteMask: UserWriteMask attribute of the node.
        rolePermissions: RolePermissions, as a mapping of role to
            [`PermissionType`][o6.ns.ns0.datatypes.PermissionType] mask.
        accessRestrictions: AccessRestrictions attribute of the node.
        parent: Node or declaration that owns the View. Defaults to the standard
            `ViewsFolder` (`i=87`).
        referenceType: ReferenceType linking the View to its parent. Defaults to
            `Organizes`.
        references: Nodes that make up the View's contents.
        ns: Shortname of the declaring namespace. Inferred from `nodeId` when
            that carries a namespace.
        server: Server that should create the node. `None` forces a declaration.

    See [Views](../manual/server/declared-types.md#views).
    """
    shortname = _resolve_namespace(ns, nodeId)
    actual_nodeid = nodeId or _new_nodeid(shortname)
    actual_browsename = browseName or "View"
    declaration = InstanceDeclaration(
        browsename=actual_browsename,
        nodeclass=_NodeClass.VIEW,
        reference_type=o6.NodeId(referenceType),
        attributes=ViewSpec(
            contains_no_loops=containsNoLoops,
            event_notifier=eventNotifier,
        ),
        nodeid=_instance_nodeid(actual_nodeid),
        parent=None if _is_node_declaration(parent) else parent,
        displayname=displayName or actual_browsename,
        description=description,
        writemask=writeMask,
        user_writemask=userWriteMask,
        role_permissions=_normalize_role_permissions(rolePermissions),
        access_restrictions=int(accessRestrictions),
    )
    _attach_declared_child(parent, declaration)
    for child in references or ():
        _declaration_values(child)
        child_declaration = _instance_declaration(child)
        _store_instance_child(declaration, child_declaration)
        child_declaration.parent = None
        _remove_instance_root(child_declaration)
    resolved = _resolve_instance_server(server=server, parent=parent)
    if resolved is None:
        return _register_declaration(declaration, instance=True)
    from o6._server_construction import _construct_declaration

    return _construct_declaration(resolved, parent, declaration)
