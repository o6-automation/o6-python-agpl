# Copyright 2026 (c) o6 Automation GmbH
"""Shared records and resolution helpers for declarative OPC UA authoring."""

from __future__ import annotations

import inspect
import sys
import typing
import dataclasses

from collections.abc import Mapping
from dataclasses import dataclass, field
from types import UnionType
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Literal,
    Optional,
    TypeAlias,
    TypeVar,
    cast,
    get_args,
    get_origin,
)

import numpy as np

if sys.version_info >= (3, 14):
    import annotationlib
else:  # Python < 3.14
    annotationlib = None

import o6
from o6 import _o6

if TYPE_CHECKING:
    from o6.ns.ns0 import NodeClass as _NodeClass
else:
    # These records are imported while ns0 is generated, before its public
    # NodeClass is available.
    _NodeClass = o6._types.NodeClass


_T = TypeVar("_T")
_BrowseNameKey = tuple[int, str]
_CallbackKind = Literal["read", "write", "call"]


_NativeNodeBase = getattr(_o6, "_NodeBase", object)
_native_nodeid = getattr(_NativeNodeBase, "_nodeid", None)


def _opcua_child_name(value: str | o6.QualifiedName) -> str:
    """Return the Python dot-syntax name of an OPC UA child BrowseName.

    Children of an instance are instances themselves, so they carry the
    lowerCamelCase member name.
    """
    name = o6.QualifiedName(value).name
    return name[:1].lower() + name[1:]


def _opcua_child_names(children: typing.Iterable["InstanceDeclaration"]) -> list[str]:
    return sorted(
        {name for child in children if (name := _opcua_child_name(child.browsename)).isidentifier()}
    )


class _NodeTypeMeta(type):
    """Expose declared OPC UA children through ``dir(TypeMarker)``."""

    def __dir__(cls) -> list[str]:
        return sorted(_all_child_members(cls))

    def __getattr__(cls, name: str) -> Any:
        try:
            return _namespace_node(_all_child_members(cls)[name], python_name=name)
        except KeyError:
            raise AttributeError(f"type object {cls.__name__!r} has no child {name!r}") from None


_NODE_TYPE_METAS: dict[type, type[_NodeTypeMeta]] = {}


def _declared_node_dir(instance: Any) -> list[str]:
    """Expose OPC UA children on declarations and live generated nodes."""
    from o6.node import Node

    if isinstance(instance, Node):
        return Node.__dir__(instance)

    return sorted(_instance_child_members(_instance_declaration(instance)))


def _with_node_type_meta(klass: type[_T]) -> type[_T]:
    """Give a root type marker the metaclass used for OPC UA child discovery."""
    if isinstance(klass, _NodeTypeMeta):
        return klass

    original_meta = type(klass)
    node_meta = _NODE_TYPE_METAS.get(original_meta)
    if node_meta is None:
        node_meta = type(
            f"_NodeTypeMeta_{original_meta.__name__}",
            (_NodeTypeMeta, original_meta),
            {},
        )
        _NODE_TYPE_METAS[original_meta] = node_meta

    body = {
        name: value
        for name, value in vars(klass).items()
        if name not in ("__dict__", "__weakref__")
    }
    rebuilt = node_meta(klass.__name__, klass.__bases__, body)

    # Functions using zero-argument super() capture the class created by the
    # statement. Retarget that cell to the decorator's replacement class.
    for value in vars(rebuilt).values():
        function = value.__func__ if isinstance(value, (classmethod, staticmethod)) else value
        if not inspect.isfunction(function) or "__class__" not in function.__code__.co_freevars:
            continue
        index = function.__code__.co_freevars.index("__class__")
        if function.__closure__ is not None and function.__closure__[index].cell_contents is klass:
            function.__closure__[index].cell_contents = rebuilt
    return cast(type[_T], rebuilt)


class _NodeIdDescriptor:
    """Expose one NodeId attribute on type declarations and native nodes."""

    def __get__(self, instance: Any, owner: type) -> Any:
        if instance is None:
            declaration = getattr(owner, "__o6_declaration__", None)
            if not isinstance(declaration, TypeDeclaration):
                raise AttributeError(f"{owner.__name__} has no declared NodeId")
            return declaration.nodeid
        if _native_nodeid is not None and isinstance(instance, _NativeNodeBase):
            return _native_nodeid.__get__(instance, owner)
        declaration = _instance_declaration(instance)
        if declaration.nodeid is None:
            raise AttributeError(f"{owner.__name__} instance has no declared NodeId")
        return declaration.nodeid

    def __set__(self, instance: Any, value: Any) -> None:
        if _native_nodeid is not None and isinstance(instance, _NativeNodeBase):
            _native_nodeid.__set__(instance, value)
        else:
            _instance_declaration(instance).nodeid = o6.NodeId(value)

    def __delete__(self, instance: Any) -> None:
        if _native_nodeid is not None and isinstance(instance, _NativeNodeBase):
            _native_nodeid.__delete__(instance)
        else:
            _instance_declaration(instance).nodeid = None


NODE_ID_DESCRIPTOR: _NodeIdDescriptor = _NodeIdDescriptor()


@dataclass(frozen=True)
class ObjectSpec:
    event_notifier: int = 0


@dataclass(frozen=True)
class VariableSpec:
    data_type: Optional[o6.NodeId] = None
    value_rank: int = -1
    array_dimensions: Optional[list[int]] = None
    value: Optional[Any] = None
    access_level: Optional[int] = None
    user_access_level: Optional[int] = None
    minimum_sampling_interval: Optional[float] = None
    historizing: bool = False


@dataclass(frozen=True)
class MethodSpec:
    input_args: tuple[Any, ...] = ()
    output_args: tuple[Any, ...] = ()
    input_args_nodeid: Optional[o6.NodeId] = None
    output_args_nodeid: Optional[o6.NodeId] = None
    executable: bool = True
    user_executable: bool = True


@dataclass(frozen=True)
class ViewSpec:
    contains_no_loops: bool = True
    event_notifier: int = 0


InstanceSpec = ObjectSpec | VariableSpec | MethodSpec | ViewSpec
TypeTarget: TypeAlias = type | o6.NodeId


@dataclass
class InstanceDeclaration:
    """One instance node owned by a type, another instance, or a namespace."""

    browsename: str
    nodeclass: _NodeClass
    reference_type: o6.NodeId
    attributes: InstanceSpec
    python_name: Optional[str] = None
    inverse: bool = False
    typeTarget: Optional[TypeTarget] = None
    modelling_rule: Optional[o6.NodeId | str] = None
    writemask: Optional[int] = None
    user_writemask: Optional[int] = None
    role_permissions: dict[o6.NodeId, int] = field(default_factory=dict)
    access_restrictions: int = 0
    description: Optional[str] = None
    displayname: Optional[str] = None
    # May retain an unresolved ``ns=<shortname>`` spelling until the
    # declaration is attached to a server that has registered that namespace.
    nodeid: Optional[o6.NodeIdLike] = None
    parent: Optional[Any] = None
    allow_abstract: bool = False
    children: list["InstanceDeclaration"] = field(default_factory=list)
    references: list["ReferenceDeclaration"] = field(default_factory=list)

    def __post_init__(self) -> None:
        expected = {
            int(_NodeClass.OBJECT): ObjectSpec,
            int(_NodeClass.VARIABLE): VariableSpec,
            int(_NodeClass.METHOD): MethodSpec,
            int(_NodeClass.VIEW): ViewSpec,
        }.get(int(self.nodeclass))
        if expected is None:
            raise TypeError("InstanceDeclaration requires an instance NodeClass")
        if not isinstance(self.attributes, expected):
            raise TypeError(
                f"{_NodeClass(self.nodeclass).name} requires {expected.__name__}, "
                f"not {type(self.attributes).__name__}"
            )
        if int(self.nodeclass) == int(_NodeClass.METHOD) and self.typeTarget is not None:
            raise TypeError("Method declarations cannot have a TypeDefinition")

    @property
    def _nodeid(self) -> Optional[o6.NodeIdLike]:
        """Native NodeId protocol backed by the declaration's sole identity field."""
        return self.nodeid

    def __dir__(self) -> list[str]:
        return sorted(_instance_child_members(self))

    def __getattr__(self, name: str) -> "InstanceDeclaration":
        if name.startswith("_"):
            raise AttributeError(name)
        try:
            return _instance_child_members(self)[name]
        except KeyError:
            raise AttributeError(
                f"OPC UA child {self.browsename!r} has no child {name!r}"
            ) from None


class _NamespaceBackend:
    """Resolve generated namespace nodes entirely from declaration metadata."""

    def dispatch(self, coro: Any) -> Any:
        try:
            coro.send(None)
        except StopIteration as exc:
            return exc.value
        coro.close()
        raise RuntimeError("namespace declaration lookup unexpectedly suspended")

    def browse_children_sync(self, node: Any) -> list[Any]:
        declaration = node.__dict__["_namespace_declaration"]
        return [
            _namespace_node(child, python_name=name)
            for name, child in _instance_child_members(declaration).items()
        ]

    async def browse_children(self, node: Any) -> list[Any]:
        return self.browse_children_sync(node)

    async def node_read(self, *_args: Any, **_kwargs: Any) -> Any:
        raise ReferenceError("namespace declaration nodes are not connected to a server")

    async def node_write(self, *_args: Any, **_kwargs: Any) -> Any:
        raise ReferenceError("namespace declaration nodes are not connected to a server")

    async def node_call(self, *_args: Any, **_kwargs: Any) -> Any:
        raise ReferenceError("namespace declaration nodes are not connected to a server")


_NAMESPACE_BACKEND = _NamespaceBackend()


def _namespace_node(declaration: InstanceDeclaration, *, python_name: str | None = None) -> Any:
    """Materialize a real detached Node with the declaration's OPC UA NodeClass."""
    from o6.node import _nodeclass2type

    node_type = _nodeclass2type(declaration.nodeclass)
    node = node_type(
        _NAMESPACE_BACKEND,
        o6.NodeId(declaration.nodeid),
        o6.QualifiedName(declaration.browsename),
    )
    node.__dict__["_namespace_declaration"] = declaration
    node.__dict__["_python_name"] = python_name
    return node


@dataclass(frozen=True)
class _OwnVariableSlot:
    """The read or write slot of the decorated VariableType itself."""


_OWN_VARIABLE_SLOT = _OwnVariableSlot()


@dataclass(frozen=True)
class _DirectMethodTarget:
    """One Method child identified by its BrowseName.

    ``qualified`` records whether namespace is part of the declaration. When it is
    ``False`` the ``browse_name`` index is a placeholder (namespace 0) and the
    target is resolved by matching its local name against the type's declared
    Methods — see :func:`o6._server_types._resolve_call_slots`.
    """

    browse_name: _BrowseNameKey
    qualified: bool = True

    def __post_init__(self) -> None:
        if (
            not isinstance(self.browse_name, tuple)
            or len(self.browse_name) != 2
            or not isinstance(self.browse_name[0], int)
            or not isinstance(self.browse_name[1], str)
            or not self.browse_name[1]
        ):
            raise TypeError("direct Method target requires a qualified BrowseName key")


@dataclass(frozen=True)
class _MemberPathTarget:
    """One nested target expressed as public Python member names."""

    members: tuple[str, ...]

    def __post_init__(self) -> None:
        if not self.members or any(not part or part.startswith("_") for part in self.members):
            raise ValueError("member path must contain public Python member names")

    @property
    def path(self) -> str:
        return ".".join(self.members)


_CallbackTarget: TypeAlias = _OwnVariableSlot | _DirectMethodTarget | _MemberPathTarget


@dataclass(frozen=True)
class CallbackBinding:
    """One class-local read, write, or call implementation declaration."""

    kind: _CallbackKind
    target: _CallbackTarget
    method_name: str

    def __post_init__(self) -> None:
        if self.kind not in ("read", "write", "call"):
            raise ValueError(f"unknown callback kind {self.kind!r}")
        if not isinstance(self.method_name, str) or not self.method_name:
            raise TypeError("CallbackBinding requires a Python method name")
        if not isinstance(self.target, (_OwnVariableSlot, _DirectMethodTarget, _MemberPathTarget)):
            raise TypeError("CallbackBinding requires a normalized callback target")
        if self.kind in ("read", "write") and isinstance(self.target, _DirectMethodTarget):
            raise TypeError(f"{self.kind} callback target cannot be a Method BrowseName")
        if self.kind == "call" and isinstance(self.target, _OwnVariableSlot):
            raise TypeError("call callback cannot target a VariableType slot")


@dataclass(frozen=True)
class DataTypeSpec:
    is_abstract: bool
    parent: Optional[o6.NodeId] = None
    structure_description: Optional[Any] = None


@dataclass(frozen=True)
class EnumTypeSpec:
    is_abstract: bool
    parent: Optional[o6.NodeId] = None
    enum_description: Optional[Any] = None


@dataclass(frozen=True)
class ReferenceTypeSpec:
    is_abstract: bool
    is_symmetric: bool = False
    inverse_name: Optional[o6.LocalizedText] = None


@dataclass(frozen=True)
class VariableTypeSpec:
    is_abstract: bool
    data_type: o6.NodeId
    value_rank: int
    array_dimensions: Optional[list[int]] = None
    value: Optional[Any] = None


@dataclass(frozen=True)
class ObjectTypeSpec:
    is_abstract: bool


TypeSpec = DataTypeSpec | EnumTypeSpec | ReferenceTypeSpec | VariableTypeSpec | ObjectTypeSpec


@dataclass
class TypeDeclaration:
    """Portable definition of one UA type node."""

    nodeid: o6.NodeId
    nodeclass: _NodeClass
    browsename: str
    displayname: str
    description: Optional[str]
    writemask: Optional[int]
    user_writemask: Optional[int]
    role_permissions: dict[o6.NodeId, int]
    access_restrictions: int
    attributes: TypeSpec
    bases: tuple[type, ...] = ()
    interfaces: tuple[Any, ...] = ()
    instances: list[InstanceDeclaration] = field(default_factory=list)
    references: list[ReferenceDeclaration] = field(default_factory=list)

    def __post_init__(self) -> None:
        expected_by_nodeclass: dict[int, type[Any] | tuple[type[Any], ...]] = {
            int(_NodeClass.DATA_TYPE): (DataTypeSpec, EnumTypeSpec),
            int(_NodeClass.REFERENCE_TYPE): ReferenceTypeSpec,
            int(_NodeClass.VARIABLE_TYPE): VariableTypeSpec,
            int(_NodeClass.OBJECT_TYPE): ObjectTypeSpec,
        }
        expected = expected_by_nodeclass.get(int(self.nodeclass), ())
        if not expected:
            raise TypeError("TypeDeclaration requires a type NodeClass")
        if not isinstance(self.attributes, expected):
            names = (
                " or ".join(item.__name__ for item in expected)
                if isinstance(expected, tuple)
                else expected.__name__
            )
            raise TypeError(
                f"{_NodeClass(self.nodeclass).name} requires {names}, "
                f"not {type(self.attributes).__name__}"
            )

    @property
    def is_abstract(self) -> bool:
        return self.attributes.is_abstract


ReferenceTarget: TypeAlias = o6.NodeIdLike | TypeDeclaration | InstanceDeclaration


@dataclass(frozen=True)
class ReferenceDeclaration:
    reference_type: o6.NodeId
    target: ReferenceTarget
    inverse: bool = False

    def __post_init__(self) -> None:
        if not isinstance(self.reference_type, o6.NodeId):
            raise TypeError("ReferenceDeclaration reference_type must be a NodeId")
        if isinstance(
            self.target,
            (TypeDeclaration, InstanceDeclaration, o6.ExpandedNodeId),
        ):
            return
        try:
            o6.NodeId(self.target)
        except (TypeError, ValueError, OverflowError) as exc:
            raise TypeError(
                "ReferenceDeclaration target must be NodeId-like or a declaration"
            ) from exc


@dataclass(frozen=True)
class ImplementationBinding:
    """One server-local implementation selected for a portable UA type."""

    declared_type: type
    implementation_type: type

    def __post_init__(self) -> None:
        if not isinstance(self.declared_type, type) or not isinstance(
            self.implementation_type, type
        ):
            raise TypeError("ImplementationBinding requires Python types")
        declaration = _type_declaration(self.declared_type)
        if not isinstance(declaration.attributes, (ObjectTypeSpec, VariableTypeSpec)):
            raise TypeError("ImplementationBinding requires an ObjectType or VariableType")
        if not issubclass(self.implementation_type, self.declared_type):
            raise TypeError(f"implementation must subclass {self.declared_type.__qualname__}")
        if (
            self.implementation_type is not self.declared_type
            and vars(self.implementation_type).get("__o6_declaration__") is not None
        ):
            raise TypeError("implementation must be undecorated; it must not declare a UA subtype")


def _type_declaration(marker: type) -> TypeDeclaration:
    """Return the nearest type declaration inherited by a marker or implementation."""
    declaration = getattr(marker, "__o6_declaration__", None)
    if not isinstance(declaration, TypeDeclaration):
        raise TypeError(f"{marker.__qualname__} is not an o6 type declaration")
    return declaration


def _type_target_nodeid(target: Optional[TypeTarget]) -> Optional[o6.NodeId]:
    """Resolve an instance TypeDefinition target to its UA NodeId."""
    if target is None:
        return None
    if isinstance(target, type):
        return _type_declaration(target).nodeid
    return o6.NodeId(target)


def _instance_node_type(type_nodeclass: _NodeClass) -> type:
    """Return the Python node base corresponding to one declared type kind."""
    from o6.node import ObjectNode, VariableNode

    if type_nodeclass == _NodeClass.VARIABLE_TYPE:
        return VariableNode
    if type_nodeclass == _NodeClass.OBJECT_TYPE:
        return ObjectNode
    raise NotImplementedError(f"no instance type for {_NodeClass(type_nodeclass)!r}")


def _instance_kind(type_nodeclass: _NodeClass) -> str:
    """Return the user-facing name of one declared instance kind."""
    if int(type_nodeclass) == int(_NodeClass.OBJECT_TYPE):
        return "object type"
    if int(type_nodeclass) == int(_NodeClass.METHOD):
        return "method"
    return "variable type"


@dataclass
class FieldSpec:
    """Optional OPC UA metadata for one field of a declared DataType."""

    name: Optional[str] = None
    description: Optional[str] = None
    is_optional: bool = False
    value_rank: Optional[int] = None
    array_dimensions: Optional[list[int]] = None
    max_string_length: Optional[int] = None


# =============================================================================
# Shared declaration identity and class introspection
# =============================================================================


_ARRAY_TYPES = (list, typing.List, np.ndarray)


def _namespace_index(namespace: Any) -> int:
    return namespace if isinstance(namespace, int) else namespace.index


def _normalize_role_permissions(
    permissions: Optional[Mapping[Any, int]],
) -> dict[o6.NodeId, int]:
    return {o6.NodeId(role): int(mask) for role, mask in (permissions or {}).items()}


def _new_nodeid(shortname: str) -> str:
    from o6.ns import _next_nodeid

    try:
        return _next_nodeid(shortname)
    except KeyError:
        raise TypeError("ns= must be a registered namespace shortname") from None


def _instance_nodeid(value: Optional[o6.NodeIdLike]) -> Optional[o6.NodeIdLike]:
    """Normalize a known NodeId while preserving an unresolved shortname."""
    if value is None:
        return None
    try:
        return o6.NodeId(value)
    except TypeError:
        if isinstance(value, str) and value.startswith("ns="):
            return value
        raise


def _abstract_new(cls: type, kind: str) -> None:
    raise TypeError(f"Cannot instantiate abstract {kind} {cls.__name__!r}")


def safe_setattr(target: Any, name: str, value: Any) -> None:
    try:
        setattr(target, name, value)
    except (AttributeError, TypeError):
        pass


def _register_declaration(value: _T, *, instance: bool = False) -> _T:
    """Register a completed declaration while importing a namespace module."""
    from o6.ns import _register_declaration as register

    return cast(_T, register(value, instance=instance))


def _declaration_nodeid(value: Any) -> o6.NodeId | o6.ExpandedNodeId | None:
    """Return the native identity carried by a declaration or live node."""
    if isinstance(value, (o6.NodeId, o6.ExpandedNodeId)):
        return value
    declaration = (
        value
        if isinstance(value, (TypeDeclaration, InstanceDeclaration))
        else getattr(value, "__o6_declaration__", None)
    )
    for candidate in (
        getattr(value, "nodeId", None),
        getattr(value, "nodeid", None),
        getattr(declaration, "nodeid", None),
    ):
        if candidate is not None:
            return candidate if isinstance(candidate, o6.ExpandedNodeId) else o6.NodeId(candidate)
    return None


def _remove_instance_root(value: Any) -> None:
    """Mark a registered declaration as owned by another declaration."""
    from o6.ns import _remove_instance_root as remove

    remove(value)


def _attach_declared_child(parent: Any, child: Any) -> None:
    """Link a declaration to a declaration parent, if it has one."""
    try:
        parent_declaration = _instance_declaration(parent)
        child_declaration = _instance_declaration(child)
    except TypeError:
        return
    if not any(existing is child_declaration for existing in parent_declaration.children):
        parent_declaration.children.append(child_declaration)
    child_declaration.parent = None
    _remove_instance_root(child_declaration)


def bases_for_type(
    klass: type,
    predicate: Callable[[type], bool],
) -> Optional[tuple[type, ...]]:
    bases = tuple(
        base
        for base in getattr(klass, "__bases__", ())
        if base is not object and isinstance(base, type) and predicate(base)
    )
    return bases or None


def _declared_bases(
    klass: type,
    spec_type: type[Any] | tuple[type[Any], ...],
) -> Optional[tuple[type, ...]]:
    return bases_for_type(
        klass,
        lambda base: isinstance(
            getattr(vars(base).get("__o6_declaration__"), "attributes", None), spec_type
        ),
    )


def _resolve_type_identity(
    klass: type,
    ns: str,
    nodeid: Any,
    browsename: Optional[str],
    displayname: Optional[str],
) -> tuple[Any, str, str]:
    actual_nodeid = nodeid if nodeid is not None else _new_nodeid(ns)
    actual_browsename = browsename if browsename is not None else klass.__name__
    actual_displayname = displayname if displayname is not None else actual_browsename
    return actual_nodeid, actual_browsename, actual_displayname


def _resolve_namespace(ns: Optional[str], nodeid: Any) -> str:
    if ns is not None:
        return getattr(o6.ns, ns).shortname
    if isinstance(nodeid, str) and nodeid.startswith("ns="):
        shortname, separator, _ = nodeid[3:].partition(";")
        if separator and shortname and not shortname.isdecimal():
            return shortname
    namespace = o6.NodeId(nodeid).ns if nodeid is not None else o6.ns.ns0
    if isinstance(namespace, int):
        return str(namespace)
    return namespace.shortname


def _decorator_description(klass: type, explicit: Optional[str]) -> Optional[str]:
    if explicit is not None:
        return explicit
    docstring = vars(klass).get("__doc__")
    return inspect.cleandoc(docstring) if docstring else None


def _annotations(klass: type) -> dict[str, Any]:
    return (
        annotationlib.get_annotations(klass, format=annotationlib.Format.FORWARDREF)
        if annotationlib is not None
        else getattr(klass, "__annotations__", {}) or {}
    )


def _resolve_annotations(klass: type, annotations: dict[str, Any]) -> dict[str, Any]:
    module_globals = dict(vars(sys.modules[klass.__module__]))
    localns = dict(vars(klass))
    localns[klass.__name__] = klass
    resolved: dict[str, Any] = {}
    for name, annotation in annotations.items():
        if not isinstance(annotation, str):
            resolved[name] = annotation
            continue
        try:
            resolved[name] = eval(annotation, module_globals, localns)
        except (NameError, AttributeError):
            resolved[name] = annotation
    return resolved


def _unwrap_arrays(annotation: Any) -> tuple[Any, bool]:
    is_array = False
    while get_origin(annotation) in _ARRAY_TYPES:
        is_array = True
        args = get_args(annotation)
        if not args:
            break
        annotation = args[0]
    return annotation, is_array


def _unwrap_optional(annotation: Any) -> tuple[Any, bool]:
    if get_origin(annotation) in (typing.Union, UnionType):
        args = get_args(annotation)
        non_none = [argument for argument in args if argument is not type(None)]
        if len(non_none) == 1:
            return non_none[0], len(non_none) < len(args)
    return annotation, False


def _is_node_declaration(value: Any) -> bool:
    if isinstance(value, InstanceDeclaration):
        return True
    namespace = getattr(value, "__dict__", None)
    return isinstance(namespace, dict) and isinstance(
        namespace.get("__o6_declaration__"), InstanceDeclaration
    )


def _instance_declaration(value: Any) -> InstanceDeclaration:
    """Return the one portable declaration carried by an offline node."""
    if isinstance(value, InstanceDeclaration):
        return value
    namespace = getattr(value, "__dict__", None)
    declaration = namespace.get("__o6_declaration__") if isinstance(namespace, dict) else None
    if not isinstance(declaration, InstanceDeclaration):
        raise TypeError(f"{type(value).__name__} is not an o6 instance declaration")
    return declaration


# =============================================================================
# Child declaration resolution
# =============================================================================


_HAS_PROPERTY = "ns=ns0;i=46"
_HAS_COMPONENT = "ns=ns0;i=47"
_PROPERTY_TYPE = "ns=ns0;i=68"
_BASE_DATA_VARIABLE_TYPE = "ns=ns0;i=63"
_TYPE_TO_INSTANCE = {
    _NodeClass.VARIABLE_TYPE: _NodeClass.VARIABLE,
    _NodeClass.OBJECT_TYPE: _NodeClass.OBJECT,
}
_MODELLING_RULE_ATTRS = {
    "Mandatory": "mandatory",
    "Optional": "optional",
    "ExposesItsArray": "exposesItsArray",
    "OptionalPlaceholder": "optionalPlaceholder",
    "MandatoryPlaceholder": "mandatoryPlaceholder",
}
_modelling_rule_nid_cache: dict[str, o6.NodeId] = {}


@dataclass(frozen=True)
class UndefinedReference:
    """A reference whose recursive target has not been resolved yet."""

    reference_type: Any
    inverse: bool = False


def _modelling_rule_nodeid(name: str) -> Optional[o6.NodeId]:
    nid = _modelling_rule_nid_cache.get(name)
    if nid is not None:
        return nid
    attr = _MODELLING_RULE_ATTRS.get(name)
    if attr is None:
        return None
    from o6.ns import ns0

    instances = getattr(ns0, "instances", None)
    obj = getattr(instances, attr, None) if instances is not None else None
    if obj is None:
        return None
    nid = o6.NodeId(obj)
    _modelling_rule_nid_cache[name] = nid
    return nid


def _resolved_modelling_rule(value: o6.NodeId | str) -> o6.NodeId:
    if isinstance(value, o6.NodeId):
        return value
    nodeid = _modelling_rule_nodeid(value)
    if nodeid is None:
        raise ValueError(f"unknown modelling rule {value!r}")
    return nodeid


def _declared_type_nodeclass(annotation: Any) -> Optional[_NodeClass]:
    declaration = (
        vars(annotation).get("__o6_declaration__") if isinstance(annotation, type) else None
    )
    if isinstance(declaration, TypeDeclaration) and isinstance(
        declaration.attributes, (VariableTypeSpec, ObjectTypeSpec)
    ):
        return _TYPE_TO_INSTANCE.get(declaration.nodeclass)
    return None


def _infer_child_data_type(
    annotation: Any,
    value_rank: Optional[int],
    array_dimensions: Optional[list[int]],
) -> tuple[str, int, Optional[list[int]]]:
    annotation, is_array = _unwrap_arrays(annotation)
    if is_array:
        if value_rank is None:
            value_rank = 1
        if array_dimensions is None:
            array_dimensions = [0]
    if value_rank is None:
        value_rank = -1
    try:
        return str(o6.NodeId(annotation)), value_rank, array_dimensions
    except TypeError:
        raise TypeError(
            "o6 child: cannot infer a UA DataType for child annotation "
            f"{annotation!r}. Annotate the child with an ns0 type / decorated "
            "type, or set data_type=... on the linked node instance. Custom "
            "types must be declared before the type that references them."
        )


def _resolve_method_child(
    attr_name: str, declaration: InstanceDeclaration, *, optional: bool = False
) -> InstanceDeclaration:
    if not isinstance(declaration.attributes, MethodSpec):
        raise TypeError(f"o6 child {attr_name!r} is not a Method declaration")
    modelling_rule = declaration.modelling_rule or _modelling_rule_nodeid(
        "Optional" if optional else "Mandatory"
    )
    return dataclasses.replace(
        declaration,
        browsename=declaration.browsename or attr_name,
        python_name=attr_name,
        modelling_rule=modelling_rule,
        parent=None,
    )


def _resolve_child(
    attr_name: str, annotation: Any, spec: InstanceDeclaration | UndefinedReference
) -> InstanceDeclaration:
    annotation, optional = _unwrap_optional(annotation)
    source = None if isinstance(spec, UndefinedReference) else spec
    reference_type = o6.NodeId(spec.reference_type)
    inverse = bool(spec.inverse)
    if source is not None and isinstance(source.attributes, MethodSpec):
        return _resolve_method_child(attr_name, source, optional=optional)
    is_property = reference_type == o6.NodeId(_HAS_PROPERTY)

    marker_declaration = (
        vars(annotation).get("__o6_declaration__") if isinstance(annotation, type) else None
    )
    is_leaf_carrier = (
        isinstance(marker_declaration, TypeDeclaration)
        and isinstance(marker_declaration.attributes, VariableTypeSpec)
        and (
            marker_declaration.nodeid
            in (o6.NodeId(_PROPERTY_TYPE), o6.NodeId(_BASE_DATA_VARIABLE_TYPE))
        )
    )
    child_nc = None if is_leaf_carrier else _declared_type_nodeclass(annotation)
    if child_nc is not None:
        type_declaration = _type_declaration(annotation)
        type_spec = type_declaration.attributes
        if is_property and child_nc is not _NodeClass.VARIABLE:
            raise TypeError(
                f"o6 complex non-Variable child {attr_name!r} cannot be attached "
                "with o6.hasProperty()"
            )
        if source is not None and int(source.nodeclass) != int(child_nc):
            raise TypeError(
                f"o6 child {attr_name!r}: expected {_NodeClass(child_nc).name}, "
                f"got {_NodeClass(source.nodeclass).name}"
            )
        attributes: InstanceSpec
        if source is not None:
            if not isinstance(source.attributes, (ObjectSpec, VariableSpec)):
                raise TypeError(f"o6 child {attr_name!r}: expected an Object or Variable")
            attributes = source.attributes
        elif isinstance(type_spec, VariableTypeSpec):
            attributes = VariableSpec(
                data_type=type_spec.data_type,
                value_rank=type_spec.value_rank,
                array_dimensions=type_spec.array_dimensions,
                value=type_spec.value,
            )
        else:
            attributes = ObjectSpec()
        type_target: TypeTarget = annotation
    else:
        child_nc = _NodeClass.VARIABLE
        if source is not None:
            if not isinstance(source.attributes, VariableSpec):
                raise TypeError(f"o6 child {attr_name!r}: a leaf child must be a Variable")
            attributes = source.attributes
        else:
            leaf_type_spec = (
                marker_declaration.attributes if marker_declaration is not None else None
            )
            if isinstance(leaf_type_spec, VariableTypeSpec):
                attributes = VariableSpec(
                    data_type=leaf_type_spec.data_type,
                    value_rank=leaf_type_spec.value_rank,
                    array_dimensions=leaf_type_spec.array_dimensions,
                    value=leaf_type_spec.value,
                )
            else:
                inferred, value_rank, array_dimensions = _infer_child_data_type(
                    annotation, None, None
                )
                attributes = VariableSpec(
                    data_type=o6.NodeId(inferred),
                    value_rank=value_rank,
                    array_dimensions=array_dimensions,
                )
        type_target = o6.NodeId(_PROPERTY_TYPE if is_property else _BASE_DATA_VARIABLE_TYPE)

    modelling_rule = (source.modelling_rule if source is not None else None) or (
        _modelling_rule_nodeid("Optional" if optional else "Mandatory")
    )
    return InstanceDeclaration(
        browsename=(source.browsename if source is not None else "") or attr_name,
        nodeclass=child_nc,
        reference_type=reference_type,
        attributes=attributes,
        python_name=attr_name,
        inverse=inverse,
        typeTarget=type_target,
        modelling_rule=modelling_rule,
        writemask=source.writemask if source is not None else None,
        user_writemask=source.user_writemask if source is not None else None,
        role_permissions=source.role_permissions if source is not None else {},
        access_restrictions=source.access_restrictions if source is not None else 0,
        description=source.description if source is not None else None,
        displayname=source.displayname if source is not None else None,
        nodeid=source.nodeid if source is not None else None,
        children=source.children if source is not None else [],
        references=source.references if source is not None else [],
    )


def _collect_children(klass: type) -> list[InstanceDeclaration]:
    annotations = _annotations(klass)
    if not annotations:
        return []
    resolved_hints = _resolve_annotations(klass, annotations)
    children: list[InstanceDeclaration] = []
    for attr_name, annotation in annotations.items():
        # Only declarations authored on this class participate here. Generated
        # marker classes expose inherited children virtually through their
        # metaclass, so getattr() would otherwise mistake an inherited child
        # for a new declaration when a subclass merely repeats its annotation.
        value = vars(klass).get(attr_name)
        spec = value if isinstance(value, (InstanceDeclaration, UndefinedReference)) else None
        if spec is None and _is_node_declaration(value):
            spec = _instance_declaration(value)
        if spec is None:
            continue
        resolved = resolved_hints.get(attr_name, annotation)
        try:
            children.append(_resolve_child(attr_name, resolved, spec))
        except TypeError:
            if isinstance(value, UndefinedReference) and isinstance(
                resolved, (str, typing.ForwardRef)
            ):
                continue
            raise
    return children


_CHILD_BEARING_SPECS = (VariableTypeSpec, ObjectTypeSpec)


def _browse_name_key(value: str | o6.QualifiedName) -> _BrowseNameKey:
    """Return one process-global identity for equivalent BrowseName spellings."""
    qualified = value if isinstance(value, o6.QualifiedName) else o6.QualifiedName(value)
    namespace = qualified.ns
    index = namespace if isinstance(namespace, int) else namespace.index
    return int(index), qualified.name


def _browsename_is_qualified(text: str) -> bool:
    """True when a BrowseName string names its namespace.

    Recognises the two spellings o6 accepts for a namespace prefix: ``ns=..;Name``
    (and ``nsu=..;Name``) and the numeric ``<index>:Name`` form. A bare ``"Name"``
    is unqualified and defaults to namespace 0.
    """
    if ";" in text:
        return True
    prefix, separator, _ = text.partition(":")
    return bool(separator) and prefix.isdigit()


def _all_children(cls: type) -> list[InstanceDeclaration]:
    """Return inherited declarations in base-to-derived override order."""
    by_name: dict[_BrowseNameKey, InstanceDeclaration] = {}
    order: list[_BrowseNameKey] = []
    for base in reversed(cls.__mro__):
        declaration = vars(base).get("__o6_declaration__")
        if not isinstance(declaration, TypeDeclaration) or not isinstance(
            declaration.attributes, _CHILD_BEARING_SPECS
        ):
            continue
        for child in declaration.instances:
            key = _browse_name_key(child.browsename)
            if key not in by_name:
                order.append(key)
            by_name[key] = child
    return [by_name[key] for key in order]


def _annotation_child_name(cls: type, child: InstanceDeclaration) -> str | None:
    browse_name = _opcua_child_name(child.browsename)
    for name in vars(cls).get("__annotations__") or {}:
        if name.rstrip("_").casefold() == browse_name.casefold():
            return name
    return None


def _all_child_members(cls: type) -> dict[str, InstanceDeclaration]:
    """Return inherited type children keyed by their public Python name."""
    by_browse_name: dict[_BrowseNameKey, tuple[str, InstanceDeclaration]] = {}
    order: list[_BrowseNameKey] = []
    for base in reversed(cls.__mro__):
        declaration = vars(base).get("__o6_declaration__")
        if not isinstance(declaration, TypeDeclaration) or not isinstance(
            declaration.attributes, _CHILD_BEARING_SPECS
        ):
            continue
        for child in declaration.instances:
            key = _browse_name_key(child.browsename)
            old = by_browse_name.get(key)
            name = (
                child.python_name
                or _annotation_child_name(base, child)
                or (old[0] if old is not None else _opcua_child_name(child.browsename))
            )
            if not name.isidentifier():
                continue
            if old is None:
                order.append(key)
            by_browse_name[key] = name, child
    return {by_browse_name[key][0]: by_browse_name[key][1] for key in order}


def _instance_child_members(
    declaration: InstanceDeclaration,
) -> dict[str, InstanceDeclaration]:
    """Return effective declaration children keyed for namespace dot syntax."""
    inherited = (
        _all_child_members(declaration.typeTarget)
        if isinstance(declaration.typeTarget, type)
        else {}
    )
    by_browse_name = {
        _browse_name_key(child.browsename): (name, child) for name, child in inherited.items()
    }
    order = list(by_browse_name)
    for child in declaration.children:
        key = _browse_name_key(child.browsename)
        old = by_browse_name.get(key)
        name = child.python_name or (
            old[0] if old is not None else _opcua_child_name(child.browsename)
        )
        if not name.isidentifier():
            continue
        if old is None:
            order.append(key)
        by_browse_name[key] = name, child
    return {by_browse_name[key][0]: by_browse_name[key][1] for key in order}


def _child_declarations_by_key(cls: type) -> dict[_BrowseNameKey, InstanceDeclaration]:
    return {_browse_name_key(child.browsename): child for child in _all_children(cls)}


def _store_instance_child(
    parent: InstanceDeclaration, child: InstanceDeclaration
) -> InstanceDeclaration:
    key = _browse_name_key(child.browsename)
    for index, existing in enumerate(parent.children):
        if _browse_name_key(existing.browsename) == key:
            parent.children[index] = child
            return child
    parent.children.append(child)
    return child


def _instance_child_override(template: InstanceDeclaration, value: Any) -> InstanceDeclaration:
    """Turn one explicit child value into its owned declaration."""
    if _is_node_declaration(value):
        _declaration_values(value)
        declaration = _instance_declaration(value)
        # The owned child is a copy carrying the template's BrowseName; the
        # original is what registered itself as a namespace root. Drop that
        # registration, or both get materialized and the second collides with
        # the first on the NodeId they share.
        _remove_instance_root(declaration)
        child = dataclasses.replace(
            declaration,
            browsename=template.browsename,
            python_name=template.python_name,
            reference_type=template.reference_type,
            inverse=template.inverse,
            typeTarget=template.typeTarget,
            modelling_rule=None,
            parent=None,
        )
    elif isinstance(value, dict) and isinstance(template.typeTarget, type):
        child_object = template.typeTarget(server=None, values=value)
        child = _instance_child_override(template, child_object)
    elif isinstance(template.attributes, VariableSpec):
        child = dataclasses.replace(
            template,
            nodeid=None,
            modelling_rule=None,
            attributes=dataclasses.replace(template.attributes, value=value),
            children=[],
            references=[],
            parent=None,
        )
    elif isinstance(template.attributes, MethodSpec) and value is None:
        child = dataclasses.replace(
            template,
            nodeid=None,
            modelling_rule=None,
            children=[],
            references=[],
            parent=None,
        )
    else:
        raise TypeError(
            f"object child {template.browsename!r} requires a declaration or value mapping"
        )
    return child


def _declaration_values(value: Any) -> dict[str, Any]:
    """Return explicit child declarations and values by BrowseName."""
    declaration = _instance_declaration(value)
    namespace = vars(value) if not isinstance(value, InstanceDeclaration) else {}
    marker = declaration.typeTarget if isinstance(declaration.typeTarget, type) else None
    if marker is not None:
        for child in _all_children(marker):
            if child.python_name is not None and child.python_name in namespace:
                _store_instance_child(
                    declaration,
                    _instance_child_override(child, namespace[child.python_name]),
                )
    return {child.browsename: child for child in declaration.children}
