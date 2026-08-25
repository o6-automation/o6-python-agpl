# Copyright 2026 (c) o6 Automation GmbH
"""OPC UA DataType and enumeration authoring and native registration."""

from __future__ import annotations

import enum as _enum
import numbers
import re
import typing
import warnings
from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any, Callable, Optional, cast

import o6
from o6._o6 import types as _bootstrap  # type: ignore[import-not-found]
from o6._declarations import (
    DataTypeSpec,
    EnumTypeSpec,
    FieldSpec,
    InstanceDeclaration,
    NODE_ID_DESCRIPTOR as _NODE_ID_DESCRIPTOR,
    TypeDeclaration,
    UndefinedReference,
    _NodeClass,
    _abstract_new,
    _annotations,
    _collect_children,
    _declared_bases,
    _decorator_description,
    _namespace_index,
    _new_nodeid,
    _normalize_role_permissions,
    _is_node_declaration,
    _register_declaration,
    _resolve_annotations,
    _resolve_namespace,
    _resolve_type_identity,
    _unwrap_arrays,
    _unwrap_optional,
    bases_for_type,
    safe_setattr,
)

_StructureDescription = _bootstrap.StructureDescription
_StructureDefinition = _bootstrap.StructureDefinition
_StructureField = _bootstrap.StructureField
_EnumDescription = _bootstrap.EnumDescription
_EnumDefinition = _bootstrap.EnumDefinition
_EnumField = _bootstrap.EnumField

_REGISTER_DATATYPE = o6._o6._register_datatype

# ``StructureType.Union``, as `_datatype_structure_type` stores it.  o6 never
# registers `UnionWithSubtypedValues` (4), so this one value identifies a Union.
_UNION_STRUCTURE_TYPE = 2


def _datatype_nodeids(
    shortname: str,
    nodeid: Optional[str],
    encoding_id: Optional[str],
) -> tuple[str, str]:
    """Resolve a DataType NodeId and its Default Binary Encoding NodeId."""
    if shortname not in o6.ns:
        raise TypeError("ns= must be a registered namespace shortname")
    namespace_index = getattr(o6.ns, shortname).index
    offenders = [
        f"{label}={candidate!r}"
        for label, candidate in (("nodeid", nodeid), ("default_encoding_id", encoding_id))
        if candidate and _namespace_index(o6.NodeId(candidate).ns) != namespace_index
    ]
    if offenders:
        warnings.warn(
            f"o6.datatype: explicit id(s) not in namespace {shortname!r}: "
            f"{', '.join(offenders)}. Used as-is; make sure this "
            "cross-namespace assignment is intentional.",
            stacklevel=4,
        )
    actual_nodeid = nodeid or _new_nodeid(shortname)
    if encoding_id is not None:
        return actual_nodeid, encoding_id
    if nodeid is None:
        return actual_nodeid, _new_nodeid(shortname)
    match = re.match(r"^(.*i=)(\d+)$", actual_nodeid)
    encoding = f"{match.group(1)}{int(match.group(2)) + 1}" if match else _new_nodeid(shortname)
    return actual_nodeid, encoding


def _register(
    shortname: str,
    browse_name: str,
    description: Any,
    bases: tuple[type, ...] | None = None,
) -> Any:
    pair = _REGISTER_DATATYPE(shortname, description, bases or None)
    if pair is None:
        raise RuntimeError(
            f"register type: C extension returned no PyType for "
            f"{browse_name} in namespace {shortname!r}"
        )
    _, python_type = pair
    return python_type


def add_datatype(
    shortname: str,
    nodeid: str,
    browse_name: str,
    struct_data: dict[str, Any],
    default_encoding_id: str | None = None,
    bases: tuple[type, ...] | None = None,
) -> tuple[Any, Any]:
    """Build a structure description and register its native Python type."""
    description = _StructureDescription()
    description.dataTypeId = nodeid
    description.name = o6.QualifiedName(browse_name)

    definition = _StructureDefinition()
    if "structure_type" in struct_data:
        definition.structureType = struct_data["structure_type"]
    own_fields = []
    if isinstance(struct_data.get("fields"), list):
        for field_data in struct_data["fields"]:
            if not isinstance(field_data, dict):
                own_fields.append(field_data)
                continue
            field = _StructureField()
            for source, target in (
                ("name", "name"),
                ("description", "description"),
                ("is_optional", "isOptional"),
                ("value_rank", "valueRank"),
                ("data_type", "dataType"),
                ("array_dimensions", "arrayDimensions"),
                ("max_string_length", "maxStringLength"),
            ):
                value = field_data.get(source)
                if value is not None:
                    setattr(field, target, value)
            own_fields.append(field)

    # Fold inherited descriptions into the complete native/Python layout.
    inherited_fields: list[Any] = []
    positions: dict[str, int] = {}
    seen_types: set[type] = set()
    for base in bases or ():
        for ancestor in reversed(base.__mro__):
            if ancestor in seen_types:
                continue
            seen_types.add(ancestor)
            declaration = vars(ancestor).get("__o6_declaration__")
            type_spec = declaration.attributes if isinstance(declaration, TypeDeclaration) else None
            ancestor_description = getattr(type_spec, "structure_description", None)
            ancestor_definition = getattr(ancestor_description, "structureDefinition", None)
            for field in getattr(ancestor_definition, "fields", ()) or ():
                position = positions.get(field.name)
                if position is None:
                    positions[field.name] = len(inherited_fields)
                    inherited_fields.append(field)
                else:
                    inherited_fields[position] = field

    all_fields = list(inherited_fields)
    for field in own_fields:
        position = positions.get(field.name)
        if position is None:
            positions[field.name] = len(all_fields)
            all_fields.append(field)
        else:
            all_fields[position] = field
    definition.fields = all_fields
    if any(getattr(field, "isOptional", False) for field in all_fields):
        definition.structureType = max(int(definition.structureType), 1)
    if default_encoding_id is not None:
        definition.defaultEncodingId = o6.NodeId(default_encoding_id)
    description.structureDefinition = definition

    return _register(shortname, browse_name, description, bases), description


def add_enum(
    shortname: str,
    nodeid: str,
    browse_name: str,
    enum_data: dict[str, Any],
    bases: tuple[type, ...] | None = None,
    option_set_base: _OptionSetBase | None = None,
) -> tuple[Any, Any]:
    """Build an enum description and register its native Python type.

    ``option_set_base`` carries the OptionSet's declared base; ``None`` for an
    ordinary enumeration.  The base is set on the description's
    ``builtInType`` field — the encoding-spec builtin id is the same integer as
    the ns0 numeric identifier for every base in play (see
    ``_OPTION_SET_BASES_BY_ID``), so a single field carries both meanings.
    The C extension reads it from the description and compensates for
    open62541's enumeration-only handling of ``UA_DataType_fromDescription``;
    see ``build_one_type`` in ``src/datatypes.c``.
    """

    declared_builtin_id = (
        option_set_base.builtin_id
        if option_set_base is not None
        else _OPTION_SET_BASES_BY_ID[6].builtin_id
    )

    def description(*, python_names: bool = False) -> Any:
        result = _EnumDescription()
        result.dataTypeId = o6.NodeId(nodeid)
        result.name = o6.QualifiedName(browse_name)
        definition = _EnumDefinition()
        fields = []
        for field_data in enum_data.get("fields", ()):
            if not isinstance(field_data, dict):
                fields.append(field_data)
                continue
            field = _EnumField()
            if "name" in field_data:
                field.name = (
                    field_data.get("python_name", field_data["name"])
                    if python_names
                    else field_data["name"]
                )
            if "value" in field_data:
                field.value = field_data["value"]
            if "description" in field_data:
                field.description = field_data["description"]
            if "display_name" in field_data:
                field.displayName = field_data["display_name"]
            fields.append(field)
        definition.fields = fields
        result.enumDefinition = definition
        result.builtInType = declared_builtin_id
        return result

    enum_description = description()
    registration_description = description(python_names=True)
    return (
        _register(
            shortname,
            browse_name,
            registration_description,
            bases,
        ),
        enum_description,
    )


# =============================================================================
# Structured DataType authoring
# =============================================================================


def field(
    *,
    name: Optional[str] = None,
    description: Optional[str] = None,
    isOptional: bool = False,
    valueRank: Optional[int] = None,
    arrayDimensions: Optional[list[int]] = None,
    maxStringLength: Optional[int] = None,
) -> Any:
    """Attach OPC UA metadata to an annotated DataType field.

    Used as the assigned value of an annotated attribute in a
    [`@o6.datatype`][o6.datatype] class body. The annotation still supplies the
    field's static type, so this factory deliberately returns `Any` to type
    checkers and adds only what the annotation cannot express.

    ```python
    @o6.datatype(ns="plant")
    class BatchRecord:
        batchId: str
        comment: Optional[str] = o6.field(description="free-text operator note")
        tag: str = o6.field(maxStringLength=32)
    ```

    Args:
        name: OPC UA field name. This renames the Python attribute along with
            the wire field, so it is mainly useful when a UA field name is not a
            valid Python identifier.
        description: The field's Description in the `StructureDefinition`.
        isOptional: Mark the field optional. `Optional[T]` in the annotation does
            the same thing and is the form to prefer.
        valueRank: Override the rank inferred from the annotation. Structure
            members must be scalars (`-1`) or 1-D arrays (`1`); anything else is
            rejected, because open62541 cannot represent a multi-dimensional
            array as a structure member.
        arrayDimensions: ArrayDimensions of the field.
        maxStringLength: Length hint for a `String` or `ByteString` field.

    See [Field metadata with `o6.field`](../manual/sdk-fundamentals/namespace/writing-nodesets-in-python.md#field-metadata-with-o6field).
    """
    return FieldSpec(
        name=name,
        description=description,
        is_optional=isOptional,
        value_rank=valueRank,
        array_dimensions=arrayDimensions,
        max_string_length=maxStringLength,
    )


def _require_annotations(klass: type) -> dict[str, Any]:
    annotations = _annotations(klass)
    if not annotations:
        raise TypeError(
            f"o6.datatype: class {klass.__name__!r} has no annotated fields. "
            "Add at least one type-annotated attribute."
        )
    return annotations


def _infer_data_type(
    annotation: Any,
    spec: FieldSpec,
    klass: Optional[type] = None,
    self_nodeid: Optional[str] = None,
) -> str:
    if isinstance(annotation, typing.ForwardRef):
        annotation = annotation.__forward_arg__
    annotation, optional = _unwrap_optional(annotation)
    spec.is_optional = spec.is_optional or optional
    annotation, is_array = _unwrap_arrays(annotation)
    if is_array:
        # 1D array by default; user can still override via spec.
        if spec.value_rank is None:
            spec.value_rank = 1
        if spec.array_dimensions is None:
            spec.array_dimensions = [0]
    elif spec.value_rank is None:
        spec.value_rank = -1
    if annotation is Any:
        return "i=24"  # Variant

    # Self-reference: a field of the type currently being defined (e.g. a recursive struct's `subproperties: list[Foo]`).
    # The class isn't registered yet, so `o6.NodeId(klass)` can't resolve it  — use the NodeId already allocated for this type.
    # Covers both the resolved class object and an unresolved forward-ref string equal to the class name.
    if self_nodeid is not None and klass is not None:
        if annotation is klass or annotation == klass.__name__:
            return self_nodeid

    declaration = (
        vars(annotation).get("__o6_declaration__") if isinstance(annotation, type) else None
    )
    type_spec = declaration.attributes if isinstance(declaration, TypeDeclaration) else None
    if isinstance(type_spec, DataTypeSpec) and type_spec.structure_description is None:
        if type_spec.is_abstract:
            return str(o6.NodeId(o6.ExtensionObject))
        if type_spec.parent is not None:
            # A concrete fieldless DataType is a simple/opaque subtype. It has
            # no independent C layout; fields retain the subtype annotation in
            # Python but use the parent's registered wire representation.
            return str(type_spec.parent)

    try:
        return str(o6.NodeId(annotation))
    except TypeError:
        raise TypeError(
            f"o6.datatype: cannot infer UA DataType for annotation {annotation!r}. "
            "You have to declare types in dependency order: Type A must be declared "
            "before Type B, if B has a field of type A. "
        )


def _make_field_dict(attr_name: str, data_type: str, spec: FieldSpec) -> dict[str, Any]:
    if spec.value_rank not in (-1, 1):
        raise TypeError(
            f"o6.datatype: field {attr_name!r} has value_rank={spec.value_rank}, "
            "but OPC UA struct fields support only scalars (value_rank=-1) or "
            "1D arrays (value_rank=1). Multi-dimensional arrays cannot be "
            "represented as struct members in open62541. Flatten the data to a "
            "1D array (and carry the shape in a separate field), or expose it as "
            "a standalone Variable whose value is a multi-dimensional array."
        )

    optional = {"description", "array_dimensions", "max_string_length"}
    if spec.is_optional:
        optional.add("is_optional")
    return {
        # The wire/DataTypeDefinition field name. Defaults to the Python attribute name,
        # but a spec may override it (`o6.field(name=...)`) when the UA field name is not a valid Python identifier
        #  e.g. `N/S Hemisphere` → attribute `n_S_Hemisphere` with the real name carried here.
        "name": spec.name or attr_name,
        "data_type": data_type,
        "value_rank": spec.value_rank,
        **{k: getattr(spec, k) for k in optional},
    }


def _is_o6_base(base: type) -> bool:
    try:
        o6.NodeId(base)
    except (TypeError, KeyError):
        return False
    return True


def _base_has_structure_description(klass: type) -> bool:
    """True if a direct o6 datatype base was built with a struct `UA_DataType` (a non-None `structure_description`).

    Used to decide whether a *fieldless* abstract struct still needs a real `UA_DataType`.
    It does when it sits between a field-bearing ancestor and a concrete subtype:

        `A(fields)` -> `Mid(A)` (abstract, no own fields) -> `C(Mid)`.

    The C-side field composition reads only the *direct* base's `UA_DataType`, so if `Mid` were a bare placeholder,
    `C` would compose from `Mid` (no type) and silently lose `A`'s fields.
    Building `Mid` as a composed, non-instantiable type keeps the chain of `UA_DataType`s unbroken.
    A base is always decorated before its subtype, so its declaration is fully resolved here.
    """
    for base in bases_for_type(klass, _is_o6_base) or ():
        declaration = vars(base).get("__o6_declaration__")
        spec = declaration.attributes if isinstance(declaration, TypeDeclaration) else None
        if isinstance(spec, DataTypeSpec) and spec.structure_description is not None:
            return True
    return False


def _datatype_parent_nodeid(klass: type) -> Optional[o6.NodeId]:
    for base in klass.__mro__[1:]:
        declaration = vars(base).get("__o6_declaration__")
        if isinstance(declaration, TypeDeclaration) and isinstance(
            declaration.attributes, (DataTypeSpec, EnumTypeSpec)
        ):
            return declaration.nodeid
    return None


def _datatype_structure_type(klass: type, fields: list[dict[str, Any]]) -> int:
    """Return the OPC UA StructureType value for a declared type."""
    for base in klass.__mro__[1:]:
        declaration = vars(base).get("__o6_declaration__")
        if isinstance(declaration, TypeDeclaration) and declaration.nodeid == o6.NodeId("i=12756"):
            return _UNION_STRUCTURE_TYPE
    return 1 if any(field.get("is_optional") for field in fields) else 0


def _attach_user_methods(py_type: type, klass: type) -> None:
    for attr_name, attr_value in vars(klass).items():
        if attr_name in ("__dict__", "__weakref__", "__annotations__"):
            continue
        # `_OptionSetBit` is a descriptor rather than a callable, and the only
        # non-field, non-method class attribute a generated DataType carries.
        if not callable(attr_value) and not isinstance(attr_value, (FieldSpec, _OptionSetBit)):
            continue
        # Read-only class-level names (e.g. `__bases__`, `__mro__`) cannot be reassigned;
        safe_setattr(py_type, attr_name, attr_value)

    # Field assignment must not be wrapped in Python here. `py_type` carries its
    # own C-level `tp_setattro` (see `customStruct_slots` in type_registration.c);
    # installing a Python `__setattr__` replaces that slot, and CPython then
    # refuses to let the replacement call the shadowed original ("can't apply
    # this __setattr__ to <type> object"). Value coercion for node handles
    # therefore happens in `__init__` below and in the native conversion path.

    if "__init__" not in vars(klass):
        native_init = cast(Callable[..., None], getattr(py_type, "__init__"))

        def __init__(self: Any, *args: Any, **kwargs: Any) -> None:
            # Initialise the native backing storage before assigning fields.
            native_init(self, *args)
            for name, value in kwargs.items():
                try:
                    current = getattr(self, name)
                except AttributeError as exc:
                    declaration = vars(type(self)).get("__o6_declaration__")
                    description = getattr(
                        getattr(declaration, "attributes", None),
                        "structure_description",
                        None,
                    )
                    definition = getattr(description, "structureDefinition", None)
                    union_fields = {field.name for field in getattr(definition, "fields", ()) or ()}
                    if (
                        int(getattr(definition, "structureType", 0)) != _UNION_STRUCTURE_TYPE
                        or name not in union_fields
                    ):
                        raise TypeError(
                            f"{type(self).__name__}() got an unexpected keyword argument {name!r}"
                        ) from exc
                    current = None
                if isinstance(current, o6.NodeId) and not isinstance(value, o6.NodeId):
                    value = o6.NodeId(value)
                elif isinstance(current, list) and isinstance(value, (list, tuple)):
                    # Node handles implement the native ``_nodeid`` protocol.
                    # Preserve normal array conversion, but eagerly cast node
                    # members for generated NodeId[] structure fields.
                    from o6.node import Node

                    value = [
                        o6.NodeId(member) if isinstance(member, Node) else member
                        for member in value
                    ]
                elif isinstance(current, o6.LocalizedText) and not isinstance(
                    value, o6.LocalizedText
                ):
                    value = o6.LocalizedText(value)
                try:
                    setattr(self, name, value)
                except Exception as exc:
                    exc.add_note(f"while assigning {type(self).__name__}.{name}")
                    raise

        safe_setattr(py_type, "__init__", __init__)


def _build_datatype_marker(
    ns: str,
    klass: type,
    nodeid: Optional[str],
    *,
    reason: str,
) -> tuple[type, o6.NodeId]:
    if _datatype_field_annotations(klass):
        raise TypeError(
            f"o6.datatype: marker class {klass.__name__!r} must not have annotated fields"
        )

    actual_nodeid = o6.NodeId(nodeid or _new_nodeid(ns))

    # Rebuild the marker class with an empty instance layout, carrying
    # over any user-defined methods/attributes from the class body.
    body: dict[str, Any] = {
        attr_name: attr_value
        for attr_name, attr_value in vars(klass).items()
        if attr_name not in ("__dict__", "__weakref__")
    }
    body["__slots__"] = ()
    # ``__new__`` set in a class body is auto-wrapped as a staticmethod
    # by ``type()``, so a plain function is the right thing to store here.
    body["__new__"] = lambda cls, *a, **kw: _abstract_new(cls, reason)
    return type(klass.__name__, klass.__bases__, body), actual_nodeid


def _collect_fields(klass: type, self_nodeid: Optional[str] = None) -> list[dict[str, Any]]:
    annotations = _require_annotations(klass)
    resolved_hints = _resolve_annotations(klass, annotations)

    fields: list[dict[str, Any]] = []
    for attr_name, annotation in annotations.items():
        value = getattr(klass, attr_name, None)
        if isinstance(value, (InstanceDeclaration, UndefinedReference)) or _is_node_declaration(
            value
        ):
            continue
        spec = value
        if not isinstance(spec, FieldSpec):
            spec = FieldSpec()
        data_type = _infer_data_type(
            resolved_hints.get(attr_name, annotation), spec, klass, self_nodeid
        )
        fields.append(_make_field_dict(attr_name, data_type, spec))
    return fields


def _datatype_field_annotations(klass: type) -> dict[str, Any]:
    """Return annotations describing wire fields rather than linked child nodes."""
    return {
        name: annotation
        for name, annotation in _annotations(klass).items()
        if not isinstance(
            (value := getattr(klass, name, None)),
            (InstanceDeclaration, UndefinedReference),
        )
        and not _is_node_declaration(value)
    }


def _structure_field_names(py_type: type) -> set[str]:
    """Every wire field the type carries, including those it inherits."""
    names: set[str] = set()
    for base in py_type.__mro__:
        declaration = vars(base).get("__o6_declaration__")
        description = getattr(
            getattr(declaration, "attributes", None), "structure_description", None
        )
        definition = getattr(description, "structureDefinition", None)
        names.update(field.name for field in getattr(definition, "fields", ()) or ())
    return names


#: The two ByteStrings the ns0 `OptionSet` structure (i=12755) declares, which are
#: what an `o6.optionsetbit` accessor reads and writes.
_OPTION_SET_MEMBERS = ("value", "validBits")


def _reject_unbacked_option_set_bits(klass: type, py_type: type) -> None:
    """An `o6.optionsetbit` accessor is useless without the pair it indexes."""
    bits = [name for name, value in vars(klass).items() if isinstance(value, _OptionSetBit)]
    if not bits:
        return
    carried = _structure_field_names(py_type)
    missing = [member for member in _OPTION_SET_MEMBERS if member not in carried]
    if not missing:
        return
    raise TypeError(
        f"o6.datatype: {klass.__name__!r} declares the OptionSet bit {bits[0]!r} with "
        f"o6.optionsetbit but carries no {' or '.join(missing)} field.  A structure-form "
        "OptionSet subtypes the ns0 OptionSet (i=12755) and reads its bits out of that "
        "type's Value and ValidBits ByteStrings."
    )


def datatype(
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
    defaultEncodingId: Optional[str] = None,
    parent: Optional[Any] = None,
) -> Any:
    """Declare an OPC UA structure DataType from an annotated Python class.

    The decorated class is a wire layout: every annotated attribute becomes a
    field of the type's `StructureDefinition`, and the layout is registered with
    open62541, so values encode and decode as a real structure instead of an
    opaque [`ExtensionObject`][o6.ExtensionObject]. Python builtins map to their
    OPC UA counterparts, the sized `o6` aliases pin an exact width, `list[T]`
    becomes a 1-D array of `T`, and another declared DataType nests as that type.

    Python inheritance is the `HasSubtype` chain, so a subtype inherits its
    parent's fields. Deriving from `ns0.datatypes.Union` makes the
    `StructureType` a Union, in which assigning one field clears the previously
    selected one. As soon as one field is optional, the `StructureType` becomes
    `StructureWithOptionalFields` and unset optional fields read back as `None`.
    Per-field metadata that the annotation cannot express is attached with
    [`o6.field`][o6.field].

    A user-supplied `__init__`, `__repr__`, and other methods are preserved; when
    they are absent, the native initializer and a field-listing `repr` are used.

    Args:
        ns: Shortname of the declaring namespace. Inferred from `nodeId` when
            that carries a namespace, otherwise required.
        nodeId: NodeId of the DataType node. Allocated in the declaring
            namespace when omitted.
        browseName: BrowseName of the node. Defaults to the class name.
        displayName: DisplayName of the node. Defaults to the BrowseName.
        description: Description attribute. Defaults to the class docstring.
        writeMask: WriteMask attribute of the node.
        userWriteMask: UserWriteMask attribute of the node.
        rolePermissions: RolePermissions, as a mapping of role to
            [`PermissionType`][o6.ns.ns0.datatypes.PermissionType] mask.
        accessRestrictions: AccessRestrictions attribute of the node.
        isAbstract: Declare the structure abstract. It keeps a complete
            `DataTypeDefinition` for browsing clients but cannot be
            instantiated, and a field annotated with it is encoded as an
            `ExtensionObject` so it can carry any concrete subtype.
        defaultEncodingId: NodeId of the Default Binary encoding node.
            Allocated alongside the DataType when omitted.
        parent: Node or declaration that owns the DataType node. Defaults to the
            `HasSubtype` parent implied by the Python base class.

    Raises:
        TypeError: The decorated object is not a class, the class has no
            annotated fields, a field's rank cannot be represented as a
            structure member, or the class declares an
            [`o6.optionsetbit`][o6.optionsetbit] accessor without carrying the
            `Value` and `ValidBits` members it reads.

    See [`@o6.datatype` — structures](../manual/sdk-fundamentals/namespace/writing-nodesets-in-python.md#o6datatype-structures).
    """
    ns = _resolve_namespace(ns, nodeId)

    def decorator(klass: type) -> type:
        if not isinstance(klass, type):
            raise TypeError(f"o6.datatype: expected a class, got {type(klass).__name__}")

        actual_nodeid: Any = None
        actual_default_encoding_id = None
        structure_description = None

        if isAbstract:
            # Allocate first (mirrors the concrete branch) so a self-referential
            # field can resolve to this type's own NodeId during field collection.
            has_annotations = bool(_datatype_field_annotations(klass))
            if has_annotations:
                actual_nodeid, _ = _datatype_nodeids(ns, nodeId, None)
                own_fields = _collect_fields(klass, self_nodeid=actual_nodeid)
            else:
                own_fields = []
            if own_fields or _base_has_structure_description(klass):
                # An abstract struct that carries a wire layout — its own fields and/or fields inherited through a struct base.
                # Build a real UA_DataType, but keep it non-instantiable.
                # It has no encoding NodeId. Its DataTypeDefinition still carries the complete layout.
                if actual_nodeid is None:
                    # No own annotations, but a struct base contributes the layout.
                    actual_nodeid, _ = _datatype_nodeids(ns, nodeId, None)
                py_type, structure_description = add_datatype(
                    ns,
                    nodeid=actual_nodeid,
                    browse_name=browseName or klass.__name__,
                    struct_data={
                        "structure_type": _datatype_structure_type(klass, own_fields),
                        "fields": own_fields,
                    },
                    default_encoding_id=None,
                    bases=bases_for_type(klass, _is_o6_base),
                )
                _attach_user_methods(py_type, klass)
                # Re-block instantiation: `add_datatype` returns a normal, instantiable struct class; an abstract type must reject it.
                safe_setattr(
                    py_type,
                    "__new__",
                    staticmethod(lambda cls, *a, **kw: _abstract_new(cls, "data type")),
                )
            else:
                # Pure-placeholder abstract type (no fields anywhere): no C UA_DataType, just a non-instantiable type-system marker.
                py_type, actual_nodeid = _build_datatype_marker(
                    ns, klass, nodeId, reason="abstract data type"
                )
        else:
            # Allocate the NodeId first so a self-referential field (a recursive struct: `subproperties: list[Foo]` inside `Foo`)
            # can resolve to this type's own NodeId while the class object isn't registered yet.
            actual_nodeid, actual_default_encoding_id = _datatype_nodeids(
                ns, nodeId, defaultEncodingId
            )
            has_fields = bool(_datatype_field_annotations(klass))
            if not has_fields and not _base_has_structure_description(klass):
                # A concrete simple/opaque DataType still needs an AddressSpace
                # marker even when no Python wire representation is available.
                # Keep it non-instantiable and let its UA parent describe its
                # type-system reference.
                py_type, _ = _build_datatype_marker(
                    ns, klass, actual_nodeid, reason="opaque data type"
                )
            else:
                fields = _collect_fields(klass, self_nodeid=actual_nodeid) if has_fields else []

                py_type, structure_description = add_datatype(
                    ns,
                    nodeid=actual_nodeid,
                    browse_name=browseName or klass.__name__,
                    struct_data={
                        "structure_type": _datatype_structure_type(klass, fields),
                        "fields": fields,
                    },
                    default_encoding_id=actual_default_encoding_id,
                    bases=bases_for_type(klass, _is_o6_base),
                )

                _attach_user_methods(py_type, klass)

        _reject_unbacked_option_set_bits(klass, py_type)

        actual_nodeid, actual_browsename, actual_displayname = _resolve_type_identity(
            klass, ns, actual_nodeid, browseName, displayName
        )
        declaration = TypeDeclaration(
            nodeid=o6.NodeId(actual_nodeid),
            nodeclass=_NodeClass.DATA_TYPE,
            browsename=actual_browsename,
            displayname=actual_displayname,
            description=_decorator_description(klass, description),
            writemask=writeMask,
            user_writemask=userWriteMask,
            role_permissions=_normalize_role_permissions(rolePermissions),
            access_restrictions=int(accessRestrictions),
            attributes=DataTypeSpec(
                is_abstract=isAbstract,
                parent=(
                    o6.NodeId(parent) if parent is not None else _datatype_parent_nodeid(py_type)
                ),
                structure_description=structure_description,
            ),
            bases=_declared_bases(py_type, (DataTypeSpec, EnumTypeSpec)) or (),
            instances=_collect_children(klass),
        )
        safe_setattr(py_type, "__o6_declaration__", declaration)
        safe_setattr(py_type, "_nodeid", _NODE_ID_DESCRIPTOR)

        return _register_declaration(py_type)

    return decorator


# =============================================================================
# Enumeration authoring
# =============================================================================


class _EnumFieldValue(int):
    """An integer carrying source-level OPC UA enum-field metadata."""

    # The public helper that produced this value.  An enumeration member and an
    # OptionSet member are different things, so each decorator accepts exactly
    # one spelling and names the other one when it sees it.
    helper = "o6.enumfield"

    ua_name: Optional[str]
    description: Optional[str]
    display_name: Optional[str]

    def __new__(
        cls,
        value: int,
        *,
        name: Optional[str] = None,
        description: Optional[str] = None,
        display_name: Optional[str] = None,
    ) -> "_EnumFieldValue":
        result = int.__new__(cls, value)
        result.ua_name = name
        result.description = description
        result.display_name = display_name
        return result


def enumfield(
    value: int,
    *,
    name: Optional[str] = None,
    description: Optional[str] = None,
    displayName: Optional[str] = None,
) -> int:
    """Attach OPC UA metadata to an enum member.

    Used as the assigned value of a member in an [`@o6.enumtype`][o6.enumtype]
    class body. Members declared as plain integers and members declared with this
    factory mix freely in one class.

    ```python
    @o6.enumtype(ns="plant")
    class MachineState:
        IDLE = 0
        RUNNING = o6.enumfield(1, description="executing a program")
    ```

    Args:
        value: Numeric value of the member. Must be unique within the
            enumeration.
        name: OPC UA member name, for a UA name that is not a valid Python
            identifier.
        description: Description of the member in the `EnumDefinition`.
        displayName: DisplayName of the member in the `EnumDefinition`.

    Returns:
        A value that behaves as the member's `int` and carries the metadata until
        the decorator consumes it.
    """
    return _EnumFieldValue(
        value,
        name=name,
        description=description,
        display_name=displayName,
    )


class _BitmaskValue(_EnumFieldValue):
    """An integer carrying source-level OPC UA option-set-member metadata."""

    helper = "o6.bitmask"


def bitmask(
    value: int,
    *,
    name: Optional[str] = None,
    description: Optional[str] = None,
    displayName: Optional[str] = None,
) -> int:
    """Declare one bit of an OPC UA OptionSet.

    Used as the assigned value of a member in an
    [`@o6.optionsettype`][o6.optionsettype] class body. `value` is the member's
    *mask*, not its bit position — write it as `0x01 << n` so the source shows
    the bit position and the value it produces at once.

    ```python
    @o6.optionsettype(ns="plant", base=o6.Byte)
    class AccessLevelType:
        CURRENT_READ = o6.bitmask(0x01 << 0, name="CurrentRead")
        HISTORY_WRITE = o6.bitmask(0x01 << 3, name="HistoryWrite")
    ```

    This is not an alias of [`o6.enumfield`][o6.enumfield]: an enumeration
    member and an OptionSet bit are different things, so each decorator accepts
    only its own helper.

    Args:
        value: The member's bit mask. Exactly one bit must be set, and it must
            lie inside the width of the OptionSet's declared `base`.
        name: OPC UA member name, for a UA name that is not a valid Python
            identifier.
        description: Description of the member in the `EnumDefinition`.
        displayName: DisplayName of the member in the `EnumDefinition`.

    Returns:
        A value that behaves as the member's `int` and carries the metadata until
        the decorator consumes it.
    """
    return _BitmaskValue(
        value,
        name=name,
        description=description,
        display_name=displayName,
    )


# Attribute names that `EnumMeta` injects into an enum class `__dict__` (the member table, the value→member lookup, flag masks, member-name list, …).
# When a concrete `@o6.enumtype` marker subclasses an abstract enum base, the marker itself becomes a real enum and carries these names;
# they must never be copied onto the C-built enum (see `_attach_user_attributes`).
def _compute_enum_managed_names() -> frozenset[str]:
    _Probe = _enum.IntEnum("_Probe", {"PROBE": 1})
    _ProbeFlag = _enum.IntFlag("_ProbeFlag", {"PROBE": 1})
    names = (set(vars(_Probe)) | set(vars(_ProbeFlag))) - {"PROBE"}
    # Keep user-facing dunders copyable (e.g. a class docstring); only the
    # enum machinery internals must be skipped.
    names -= {"__doc__", "__module__", "__qualname__"}
    return frozenset(names)


_ENUM_MANAGED_NAMES = _compute_enum_managed_names()


# Installed as ``__new_member__`` on abstract ``@o6.enumtype`` bases.
#
# When a concrete enum subclasses an abstract enum, ``enum.EnumMeta``
# builds the concrete class before our decorator runs and looks up the
# member constructor via ``enum._find_new_``, which prefers a
# ``__new_member__`` on the parent enum over ``__new__``.  Providing this
# hook means each ``FIELD = o6.enumfield(...)`` member is constructed
# here.  The temporary value is a real integer carrying source metadata,
# which is copied onto the enum member before the class body is discarded.
#
# ``__new_member__`` is used only for *member* construction; direct
# instantiation of the abstract base still goes through ``__new__``
# (``_abstract_new``), and concrete subclasses get their own value-lookup
# ``__new__`` from ``EnumMeta``, so this never shadows either.
def _member_new(
    cls: type,
    value: int,
    description: Optional[str] = None,
    display_name: Optional[str] = None,
) -> Any:
    obj: Any = int.__new__(cls, int(value))
    obj._value_ = int(value)
    obj._ua_name = getattr(value, "ua_name", None)
    obj._ua_description = getattr(value, "description", description)
    obj._ua_display_name = getattr(value, "display_name", display_name)
    obj._ua_helper = getattr(value, "helper", None)
    return obj


# The member helper each decorator owns.  ``o6.bitmask`` is deliberately not an
# alias of ``o6.enumfield``, which is what lets each decorator reject the other's
# spelling and name the right one.
_MEMBER_HELPER_OWNER = {
    "o6.enumfield": "@o6.enumtype",
    "o6.bitmask": "@o6.optionsettype",
}


@dataclass(frozen=True)
class _EnumDialect:
    """What one decorator accepts in a class body, and how it says so."""

    decorator: str
    helper: str
    member_spelling: str
    members_label: str
    member_example: str
    duplicate_noun: str
    # Whether every member must carry the helper.  ``@o6.optionsettype`` is new,
    # so it can require ``o6.bitmask`` and reject anything else numeric outright;
    # a bare integer is a released, documented spelling for ``@o6.enumtype``.
    require_helper: bool


_ENUM_DIALECT = _EnumDialect(
    decorator="o6.enumtype",
    helper="o6.enumfield",
    member_spelling="o6.enumfield(value, ...)",
    members_label="enum members",
    member_example="``RED = 0``",
    duplicate_noun="enum value",
    require_helper=False,
)

_OPTION_SET_DIALECT = _EnumDialect(
    decorator="o6.optionsettype",
    helper="o6.bitmask",
    member_spelling="o6.bitmask(0x01 << n)",
    members_label="OptionSet members",
    member_example="``CURRENT_READ = o6.bitmask(0x01 << 0)``",
    duplicate_noun="bit mask",
    require_helper=True,
)


def _reject_wrong_member_helper(
    klass: type, member: str, used: Optional[str], *, dialect: _EnumDialect
) -> None:
    if used == dialect.helper:
        return
    if used is None:
        if not dialect.require_helper:
            return
        raise TypeError(
            f"{dialect.decorator}: member {member!r} of {klass.__name__!r} must be "
            f"declared with {dialect.member_spelling}, not as a plain value."
        )
    raise TypeError(
        f"{dialect.decorator}: member {member!r} of {klass.__name__!r} is declared "
        f"with {used}, which belongs to "
        f"{_MEMBER_HELPER_OWNER.get(used, 'another decorator')}.  Declare it "
        f"with {dialect.member_spelling} instead."
    )


def _is_numeric_declaration(value: Any) -> bool:
    """Does this class attribute look like a member rather than a helper?

    A numpy scalar, a ``bool`` and a ``float`` are all plausible mis-spellings of
    a member — ``o6.Byte(0x01 << 1)`` especially, next to ``base=o6.Byte`` — and
    none of them is a Python ``int``, so the collector would otherwise drop them.

    A type is never a member declaration, and is excluded explicitly: numeric
    types carry ``__index__`` themselves, so ``Alias = o6.Byte`` would otherwise
    be mistaken for one.
    """
    if isinstance(value, type):
        return False
    return isinstance(value, numbers.Number) or hasattr(value, "__index__")


def _collect_enum_fields(klass: type, *, dialect: _EnumDialect) -> list[dict[str, Any]]:
    fields: list[dict[str, Any]] = []
    for attr_name, attr_value in vars(klass).items():
        # Skip dunders and private helpers.
        if attr_name.startswith("_"):
            continue

        # A decorator that requires its member helper accepts nothing else that
        # looks like a member; the normalising branches below then only ever see
        # a helper value, an already-built member, or a bare int.
        if (
            dialect.require_helper
            and not isinstance(attr_value, (_EnumFieldValue, _enum.Enum))
            and _is_numeric_declaration(attr_value)
        ):
            _reject_wrong_member_helper(klass, attr_name, None, dialect=dialect)

        # Three input shapes all normalise to the same dict:
        #   * metadata-carrying int (standalone case)
        #   * pre-built enum.IntEnum member (abstract-base subclass)
        #   * bare int (most common)
        if isinstance(attr_value, _EnumFieldValue):
            _reject_wrong_member_helper(klass, attr_name, attr_value.helper, dialect=dialect)
            ua_name = attr_value.ua_name or attr_name
            description = attr_value.description
            display_name = attr_value.display_name or ua_name
            value = int(attr_value)
        elif isinstance(attr_value, _enum.Enum):
            # ``EnumMeta`` already turned the class body into members (the
            # abstract-base subclass case); ``_member_new`` kept the helper.
            _reject_wrong_member_helper(
                klass, attr_name, getattr(attr_value, "_ua_helper", None), dialect=dialect
            )
            ua_name = getattr(attr_value, "_ua_name", None) or attr_name
            description = getattr(attr_value, "_ua_description", None)
            display_name = getattr(attr_value, "_ua_display_name", None) or ua_name
            value = attr_value.value
        elif isinstance(attr_value, int) and not isinstance(attr_value, bool):
            ua_name = attr_name
            description = None
            display_name = attr_name
            value = attr_value
        else:
            # Any non-numeric helper attribute (str, list, method, …) is silently skipped.
            continue

        fd: dict[str, Any] = {
            "name": ua_name,
            "python_name": attr_name,
            "value": value,
            "display_name": display_name,
        }
        if description is not None:
            fd["description"] = description
        fields.append(fd)

    return fields


def _build_abstract_enum(
    ns: str, klass: type, nodeid: Optional[str] = None
) -> tuple[type, o6.NodeId]:
    fields = _collect_enum_fields(klass, dialect=_ENUM_DIALECT)
    if fields:
        raise TypeError(
            f"o6.enumtype: abstract class {klass.__name__!r} must not "
            "have enum members. Abstract enum types are a type-system "
            "placeholder, not a wire layout."
        )

    # The C extension models *every* OPC UA enumeration as an `IntFlag`:
    # option sets such as `BrowseResultMask` need the bitwise `|` behaviour, and plain enumerations behave identically for their declared members.
    # A concrete enum is built as `IntFlag` and then re-based onto this abstract parent, so the parent must itself be an `IntFlag`
    # — an `IntEnum` base would strip `Flag` out of the concrete class's MRO and break `|` (`_get_value`).
    int_flag_factory = cast(Any, _enum.IntFlag)
    # Build the IntFlag without extra positional bases — Python 3.11's
    # `EnumType.__call__` only accepts `(value, names)` positionally, while
    # 3.12+ absorbs trailing positional args via `*values`.  We rebase
    # explicitly below so user-specified abstract bases still appear in
    # the MRO on every supported interpreter.
    py_type = int_flag_factory(klass.__name__, {}, boundary=_enum.FlagBoundary.KEEP)
    user_bases = bases_for_type(klass, _is_enum_base)
    if user_bases:
        # Keep `IntFlag` first so the resulting class is still a real
        # `IntFlag`; user abstract enum bases follow so isinstance/issubclass
        # model the UA hierarchy.
        py_type.__bases__ = (int_flag_factory, *user_bases)

    actual_nodeid = o6.NodeId(nodeid or _new_nodeid(ns))

    # `IntFlag` built with no members leaves `__slots__` in place, so the public `setattr` path is rejected.
    # Walk the descriptor protocol directly for the decorator-owned attrs (the marker attributes are attached separately
    # by the public ``enumtype()`` decorator).
    decorator_attrs: dict[str, Any] = {
        "__new__": lambda cls, *a, **kw: _abstract_new(cls, "enum type"),
        "__new_member__": _member_new,
    }
    user_attrs = (
        (attr_name, attr_value)
        for attr_name, attr_value in vars(klass).items()
        if attr_name not in ("__dict__", "__weakref__", "__annotations__", *decorator_attrs)
    )
    for attr_name, attr_value in (*decorator_attrs.items(), *user_attrs):
        type.__setattr__(py_type, attr_name, attr_value)

    return py_type, actual_nodeid


def _attach_user_attributes(py_type: type, klass: type) -> None:
    member_names = set(getattr(py_type, "__members__", {}).keys())

    for attr_name, attr_value in vars(klass).items():
        if attr_name in member_names:
            # Already an enum member; the C extension owns it.
            continue
        if attr_name in ("__dict__", "__weakref__", "__annotations__"):
            continue
        if attr_name in _ENUM_MANAGED_NAMES:
            # When the marker class subclasses an abstract enum base (e.g. `Enumeration`), `EnumMeta` turns it into a real enum
            # and populates its `__dict__` with the member table and value-lookup maps (`_value2member_map_`, `_member_map_`, `_member_names_`, flag masks, …).
            # Those describe the *marker's* members, not the C-built enum's — copying them over would clobber `py_type`'s own members and break `py_type(value)` lookups.
            # Skip them.
            continue

        safe_setattr(py_type, attr_name, attr_value)


def _is_enum_base(base: type) -> bool:
    """Predicate: is ``base`` a UA enum type produced by ``@o6.enumtype``?"""
    declaration = vars(base).get("__o6_declaration__")
    return isinstance(declaration, TypeDeclaration) and isinstance(
        declaration.attributes, EnumTypeSpec
    )


def _require_non_empty_fields(
    klass: type, fields: list[dict[str, Any]], *, dialect: _EnumDialect
) -> None:
    if fields:
        return
    raise TypeError(
        f"{dialect.decorator}: class {klass.__name__!r} has no {dialect.members_label}.  "
        f"Define at least one, e.g. {dialect.member_example}."
    )


def _reject_duplicate_values(
    klass: type, fields: list[dict[str, Any]], *, dialect: _EnumDialect
) -> None:
    # Duplicate numeric values are ambiguous on the wire; the C
    # extension's IntEnum construction rejects them too, but a clearer
    # Python error beats a cryptic C traceback.
    seen: dict[int, str] = {}
    for fd in fields:
        v = fd["value"]
        if v in seen:
            raise TypeError(
                f"{dialect.decorator}: duplicate {dialect.duplicate_noun} {v} in "
                f"{klass.__name__!r} (members {seen[v]!r} and "
                f"{fd['python_name']!r})"
            )
        seen[v] = fd["python_name"]


def _declare_enum_datatype(
    klass: type,
    *,
    dialect: _EnumDialect,
    option_set_base: Optional[_OptionSetBase] = None,
    ns: str,
    nodeId: Optional[str],
    browseName: Optional[str],
    displayName: Optional[str],
    description: Optional[str],
    writeMask: Optional[bool],
    userWriteMask: Optional[bool],
    rolePermissions: Optional[Mapping[Any, int]],
    accessRestrictions: int,
    isAbstract: bool = False,
    validate_fields: Optional[Callable[[type, list[dict[str, Any]]], None]] = None,
) -> type:
    """Register the enumeration DataType behind ``@o6.enumtype`` and
    ``@o6.optionsettype``.

    Both decorators produce the same thing — a C-built ``IntFlag`` registered as
    an OPC UA enumeration DataType, with a ``TypeDeclaration`` carrying an
    ``EnumTypeSpec`` — and differ only in what they accept in the class body and,
    for an OptionSet, in the unsigned integer ``option_set_base`` names.
    ``dialect``, ``option_set_base`` and ``validate_fields`` carry that
    difference; everything else is shared so the two can never drift.
    """
    if not isinstance(klass, type):
        raise TypeError(f"{dialect.decorator}: expected a class, got {type(klass).__name__}")

    enum_description = None
    actual_nodeid: Any

    if isAbstract:
        # Abstract enums get no C UA_DataType — they are a pure-Python type-system placeholder.
        py_type, actual_nodeid = _build_abstract_enum(ns, klass, nodeId)
    else:
        fields = _collect_enum_fields(klass, dialect=dialect)
        _require_non_empty_fields(klass, fields, dialect=dialect)
        if validate_fields is not None:
            validate_fields(klass, fields)
        _reject_duplicate_values(klass, fields, dialect=dialect)

        actual_nodeid = nodeId or _new_nodeid(ns)

        py_type, enum_description = add_enum(
            ns,
            nodeid=actual_nodeid,
            browse_name=browseName or klass.__name__,
            enum_data={"fields": fields},
            bases=bases_for_type(klass, _is_enum_base),
            option_set_base=option_set_base,
        )

        # The C extension produces a real `IntEnum` subclass.
        # `IntEnum` values are constructed by `EnumMeta.__new__` which iterates over the class body;
        # if the user attached extra helpers to the marker class we want them to land on the real enum as class attributes.
        _attach_user_attributes(py_type, klass)

    actual_nodeid, actual_browsename, actual_displayname = _resolve_type_identity(
        klass, ns, actual_nodeid, browseName, displayName
    )
    declaration = TypeDeclaration(
        nodeid=o6.NodeId(actual_nodeid),
        nodeclass=_NodeClass.DATA_TYPE,
        browsename=actual_browsename,
        displayname=actual_displayname,
        description=_decorator_description(klass, description),
        writemask=writeMask,
        user_writemask=userWriteMask,
        role_permissions=_normalize_role_permissions(rolePermissions),
        access_restrictions=int(accessRestrictions),
        attributes=EnumTypeSpec(
            is_abstract=isAbstract,
            # An OptionSet subtypes its unsigned integer, which is a numpy scalar
            # carrying no o6 declaration, so ``base=`` is the only thing that can
            # supply the parent — see ``_OptionSetBase.nodeid``.
            parent=(
                o6.NodeId(option_set_base.nodeid)
                if option_set_base is not None
                else _datatype_parent_nodeid(py_type)
            ),
            enum_description=enum_description,
        ),
        bases=_declared_bases(py_type, EnumTypeSpec) or (),
        instances=_collect_children(klass),
    )
    safe_setattr(py_type, "__o6_declaration__", declaration)
    safe_setattr(py_type, "_nodeid", _NODE_ID_DESCRIPTOR)

    return _register_declaration(py_type)


def enumtype(
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
) -> Any:
    """Declare an OPC UA enumeration DataType from a Python class.

    The decorated class is a real `enum.IntEnum` afterwards, so its members are
    usable wherever an integer is expected and as the annotation that gives a
    struct field or Variable that DataType. Bare integer class attributes are
    enough; [`o6.enumfield`][o6.enumfield] adds per-member OPC UA metadata and
    mixes freely with plain values. Duplicate numeric values are rejected because
    they are ambiguous on the wire.

    A bit field is not an enumeration: declare it with
    [`@o6.optionsettype`][o6.optionsettype], whose members are masks. A member
    declared with [`o6.bitmask`][o6.bitmask] is rejected here.

    Python inheritance is the `HasSubtype` chain. An `isAbstract=True` enum has
    no members and no wire representation: it is a type-system placeholder that
    concrete enums share, and a Variable typed with it accepts any of its
    concrete subtypes.

    Args:
        ns: Shortname of the declaring namespace. Inferred from `nodeId` when
            that carries a namespace, otherwise required.
        nodeId: NodeId of the DataType node. Allocated in the declaring
            namespace when omitted.
        browseName: BrowseName of the node. Defaults to the class name.
        displayName: DisplayName of the node. Defaults to the BrowseName.
        description: Description attribute. Defaults to the class docstring.
        writeMask: WriteMask attribute of the node.
        userWriteMask: UserWriteMask attribute of the node.
        rolePermissions: RolePermissions, as a mapping of role to
            [`PermissionType`][o6.ns.ns0.datatypes.PermissionType] mask.
        accessRestrictions: AccessRestrictions attribute of the node.
        isAbstract: Declare the enumeration abstract, leaving it without members
            and without a wire representation.

    Raises:
        TypeError: The decorated object is not a class, a concrete enumeration
            has no members, two members share a numeric value, or a member is
            declared with [`o6.bitmask`][o6.bitmask].

    See [`@o6.enumtype` — enumerations](../manual/sdk-fundamentals/namespace/writing-nodesets-in-python.md#o6enumtype-enumerations).
    """
    ns = _resolve_namespace(ns, nodeId)

    def decorator(klass: type) -> type:
        return _declare_enum_datatype(
            klass,
            dialect=_ENUM_DIALECT,
            ns=ns,
            nodeId=nodeId,
            browseName=browseName,
            displayName=displayName,
            description=description,
            writeMask=writeMask,
            userWriteMask=userWriteMask,
            rolePermissions=rolePermissions,
            accessRestrictions=accessRestrictions,
            isAbstract=isAbstract,
        )

    return decorator


# =============================================================================
# OptionSet authoring
# =============================================================================

# The highest bit the *registration* can carry, not a property of an OptionSet:
# `EnumField.value` is a signed 64-bit integer, so the top bit of a `UInt64` has
# no mask that fits.  Still true now that the registered type's `typeKind` and
# `memSize` are corrected to the declared width: the correction happens *after*
# `UA_DataType_fromEnumDescription`, so a member's mask still reaches the C layer
# as an `EnumField.value`.  Re-check this if that ever stops being the route.
_MAX_REGISTRABLE_BIT = 62


@dataclass(frozen=True)
class _OptionSetBase:
    """One row in ``_OPTION_SET_BASES_BY_ID``, which is the single definition of
    the bases an enumeration or OptionSet may declare.  This class exists to give
    the rows a type, not to define them.
    """

    name: str
    #: Encoding-spec builtin id, equal to the ns0 numeric identifier.
    builtin_id: int
    #: Width in bytes.
    width: int
    #: ``True`` for the four unsigned integers a user may pass as ``base=``;
    #: ``False`` for ``Int32``, which is in the table for ordinary enumerations.
    selectable: bool

    @property
    def bits(self) -> int:
        """Width in bits."""
        return self.width * 8

    @property
    def nodeid(self) -> str:
        """NodeId of the ns0 builtin, which becomes the DataType node's
        ``HasSubtype`` parent.  Nothing else in the declaration carries it: a
        numpy scalar has no o6 declaration for ``_datatype_parent_nodeid`` to
        find, so without this an OptionSet is served under ``BaseDataType``."""
        return f"i={self.builtin_id}"

    @property
    def public_name(self) -> str:
        """``o6.<Name>`` — the spelling a user passes as ``base=`` and what
        error messages name.  Keeps the ``o6.`` prefix in one place."""
        return f"o6.{self.name}"


# Int32 is in the table for ordinary enumerations, which travel the same
# registration route; splitting it out would duplicate the table.
_OPTION_SET_BASES_BY_ID: Mapping[int, _OptionSetBase] = {
    3: _OptionSetBase("Byte", builtin_id=3, width=1, selectable=True),
    5: _OptionSetBase("UInt16", builtin_id=5, width=2, selectable=True),
    6: _OptionSetBase("Int32", builtin_id=6, width=4, selectable=False),
    7: _OptionSetBase("UInt32", builtin_id=7, width=4, selectable=True),
    9: _OptionSetBase("UInt64", builtin_id=9, width=8, selectable=True),
}


def _option_set_bases() -> dict[Any, _OptionSetBase]:
    """The unsigned integers an OptionSet may subtype, keyed on the ``o6.``
    class the user passes as ``base=``.

    ``base=`` is a keyword rather than Python inheritance because the inheritance
    form cannot be made real: ``bases_for_type`` drops any base without an o6
    declaration, and the C extension builds an ``IntFlag`` and then assigns
    ``__bases__``, which will not accept a numpy scalar type.

    Built per call rather than at import: ``o6.Byte`` etc. are not yet bound
    while this module is being imported.
    """
    return {
        getattr(o6, entry.name): entry
        for entry in _OPTION_SET_BASES_BY_ID.values()
        if entry.selectable
    }


def _option_set_base_hint() -> str:
    """``one of o6.Byte, o6.UInt16, ...`` — spelled from the table, not beside it."""
    return "one of " + ", ".join(entry.public_name for entry in _option_set_bases().values())


def _reject_python_enum_base(klass: type) -> None:
    """An OptionSet subtypes its unsigned integer, and nothing else.

    ``base=`` sets the published ``HasSubtype`` parent, so a Python enum base —
    which is what supplies the parent for ``@o6.enumtype`` — would be accepted and
    then silently have no effect on what the DataType node subtypes.  Rejecting it
    keeps one spelling for one meaning.
    """
    declared = bases_for_type(klass, _is_enum_base)
    if not declared:
        return
    names = ", ".join(base.__name__ for base in declared)
    raise TypeError(
        f"o6.optionsettype: class {klass.__name__!r} subclasses {names}, but an "
        "OptionSet subtypes the unsigned integer named by base= and nothing else.  "
        "Drop the Python base."
    )


def _resolve_option_set_base(klass: type, base: Any) -> _OptionSetBase:
    """Resolve ``base=`` to the unsigned integer it names."""
    if base is None:
        raise TypeError(
            f"o6.optionsettype: class {klass.__name__!r} must declare base=, the "
            f"unsigned integer it subtypes ({_option_set_base_hint()}).  It carries "
            "the OptionSet's width, which nothing else in the declaration does."
        )
    try:
        entry = _option_set_bases().get(base)
    except TypeError:  # unhashable, so certainly not one of the four
        entry = None
    if entry is None:
        raise TypeError(
            f"o6.optionsettype: class {klass.__name__!r} declares "
            f"base={getattr(base, '__name__', base)!r}, which is not an OPC UA "
            f"unsigned integer.  Pass {_option_set_base_hint()}."
        )
    return entry


def _reject_invalid_masks(
    klass: type, fields: list[dict[str, Any]], *, base: _OptionSetBase
) -> None:
    """Every OptionSet member is one bit, inside the declared base's width."""
    for fd in fields:
        member = fd["python_name"]
        value = fd["value"]
        if value <= 0 or value & (value - 1):
            raise TypeError(
                f"o6.optionsettype: member {member!r} of {klass.__name__!r} has "
                f"value {value}, which is not a single bit.  An OptionSet member "
                "is one bit's mask, written as ``0x01 << n``."
            )
        bit = value.bit_length() - 1
        if bit >= base.bits:
            raise TypeError(
                f"o6.optionsettype: member {member!r} of {klass.__name__!r} "
                f"declares bit {bit}, which is outside the {base.bits} bits of "
                f"base={base.public_name}."
            )
        if bit > _MAX_REGISTRABLE_BIT:
            raise TypeError(
                f"o6.optionsettype: member {member!r} of {klass.__name__!r} "
                f"declares bit {bit}, which cannot be registered: the EnumField "
                "value carrying a member is a signed 64-bit integer, so the "
                f"highest declarable bit is {_MAX_REGISTRABLE_BIT}."
            )


def optionsettype(
    *,
    base: Any = None,
    ns: Optional[str] = None,
    nodeId: Optional[str] = None,
    browseName: Optional[str] = None,
    displayName: Optional[str] = None,
    description: Optional[str] = None,
    writeMask: Optional[bool] = None,
    userWriteMask: Optional[bool] = None,
    rolePermissions: Optional[Mapping[Any, int]] = None,
    accessRestrictions: int = 0,
) -> Any:
    """Declare an OPC UA OptionSet DataType from a Python class.

    An OptionSet is a bit field, not an enumeration: each member is the *mask* of
    one bit, and members compose with `|`. Every member is declared with
    [`o6.bitmask`][o6.bitmask] and written as `0x01 << n`, so the source shows the
    bit position and the value it produces at once.

    ```python
    @o6.optionsettype(nodeId="ns=plant;i=15031", browseName="AccessLevelType", base=o6.Byte)
    class AccessLevelType:
        CURRENT_READ = o6.bitmask(0x01 << 0, name="CurrentRead")
        HISTORY_WRITE = o6.bitmask(0x01 << 3, name="HistoryWrite")


    int(AccessLevelType.HISTORY_WRITE)                          # 8
    AccessLevelType.CURRENT_READ | AccessLevelType.HISTORY_WRITE  # 9
    ```

    `base` is the unsigned integer the OptionSet subtypes and is mandatory: it is
    the OptionSet's width, and nothing else in the declaration carries it. It is
    a keyword rather than a Python base class because the inheritance form cannot
    be made real.

    This decorator declares the *integer* form of an OptionSet. The structure
    form — a subtype of the ns0 `OptionSet` with `Value` and `ValidBits`
    ByteStrings — is an ordinary [`@o6.datatype`][o6.datatype].

    Args:
        base: The unsigned integer the OptionSet subtypes: `o6.Byte`,
            `o6.UInt16`, `o6.UInt32` or `o6.UInt64`. Mandatory.
        ns: Shortname of the declaring namespace. Inferred from `nodeId` when
            that carries a namespace, otherwise required.
        nodeId: NodeId of the DataType node. Allocated in the declaring
            namespace when omitted.
        browseName: BrowseName of the node. Defaults to the class name.
        displayName: DisplayName of the node. Defaults to the BrowseName.
        description: Description attribute. Defaults to the class docstring.
        writeMask: WriteMask attribute of the node.
        userWriteMask: UserWriteMask attribute of the node.
        rolePermissions: RolePermissions, as a mapping of role to
            [`PermissionType`][o6.ns.ns0.datatypes.PermissionType] mask.
        accessRestrictions: AccessRestrictions attribute of the node.

    Raises:
        TypeError: The decorated object is not a class; `base` is missing or is
            not one of the four unsigned integers; the class has no members; a
            member is not exactly one set bit; a member's bit lies outside the
            base's width; two members carry the same mask; or a member is not
            declared with `o6.bitmask` — a bare integer, a numpy scalar and
            [`o6.enumfield`][o6.enumfield] are all rejected, so a mis-spelled
            member cannot silently drop out of the bit field.

    See [`@o6.optionsettype` — option sets](../manual/sdk-fundamentals/namespace/writing-nodesets-in-python.md#o6optionsettype-option-sets).
    """
    ns = _resolve_namespace(ns, nodeId)

    def decorator(klass: type) -> type:
        if not isinstance(klass, type):
            raise TypeError(f"o6.optionsettype: expected a class, got {type(klass).__name__}")

        _reject_python_enum_base(klass)
        resolved_base = _resolve_option_set_base(klass, base)

        def validate_fields(klass: type, fields: list[dict[str, Any]]) -> None:
            _reject_invalid_masks(klass, fields, base=resolved_base)

        return _declare_enum_datatype(
            klass,
            dialect=_OPTION_SET_DIALECT,
            option_set_base=resolved_base,
            ns=ns,
            nodeId=nodeId,
            browseName=browseName,
            displayName=displayName,
            description=description,
            writeMask=writeMask,
            userWriteMask=userWriteMask,
            rolePermissions=rolePermissions,
            accessRestrictions=accessRestrictions,
            validate_fields=validate_fields,
        )

    return decorator


# =============================================================================
# Structure-form OptionSet authoring
# =============================================================================
#
# The *structure* form of an OPC UA OptionSet is a `@o6.datatype` subtyping the
# ns0 `OptionSet` (i=12755) with `Value` and `ValidBits` ByteStrings.  It shares
# a name with the integer form above and nothing else: different registration,
# different Python shape, different accessors.
#
# Its bits need an accessor of their own because the pair is three-valued.
# `Value` says whether a bit is set; `ValidBits` says whether it says anything at
# all.  Hand-masking two ByteStrings against a bit position read out of the
# NodeSet XML is what the accessor replaces.


class _OptionSetBit:
    """A three-valued accessor for one declared bit of a structure-form OptionSet."""

    __slots__ = ("attribute", "byte", "mask", "position", "ua_name")

    def __init__(self, position: int, *, name: Optional[str] = None) -> None:
        if position < 0:
            raise ValueError(
                f"o6.optionsetbit: bit position {position} is negative.  A position "
                "indexes the bits of the OptionSet's Value ByteString, low byte and "
                "least significant bit first."
            )
        self.position = position
        # The name the NodeSet declares, kept because it is what the Python
        # spelling was derived from and is often not a legal identifier
        # (``2006_42_EC``, ``to-offnormal``).  A structure-form OptionSet
        # publishes no bit names, so nothing on the wire reads it.
        self.ua_name = name
        self.attribute = name or f"bit {position}"
        self.byte = position // 8
        self.mask = 1 << (position % 8)

    def __set_name__(self, owner: type, name: str) -> None:
        self.attribute = name

    def __repr__(self) -> str:
        return f"<o6.optionsetbit {self.attribute!r} at bit {self.position}>"

    def __get__(self, instance: Any, owner: Optional[type] = None) -> Any:
        if instance is None:
            return self
        # `_reject_unbacked_option_set_bits` guarantees both members exist.
        valid = bytes(instance.validBits or b"")
        # A byte the ByteString does not reach says nothing about its bits, so the
        # bit is not valid — the same answer as a zero `ValidBits` bit, and not a
        # raise from deep inside decoding.
        if self.byte >= len(valid) or not valid[self.byte] & self.mask:
            return None
        value = bytes(instance.value or b"")
        if self.byte >= len(value):
            return False
        return bool(value[self.byte] & self.mask)

    def __set__(self, instance: Any, state: Any) -> None:
        value = bytearray(instance.value or b"")
        valid = bytearray(instance.validBits or b"")
        if state is None:
            # The inverse of a not-valid read.  Nothing is padded: a byte that
            # does not exist already reads as not valid.
            for buffer in (value, valid):
                if self.byte < len(buffer):
                    buffer[self.byte] &= ~self.mask & 0xFF
        else:
            needed = self.byte + 1
            for buffer in (value, valid):
                buffer.extend(bytes(max(0, needed - len(buffer))))
            valid[self.byte] |= self.mask
            # Any non-`None` state is a truth value: only `None` means "not valid".
            if state:
                value[self.byte] |= self.mask
            else:
                value[self.byte] &= ~self.mask & 0xFF
        # Both ByteStrings are written, so the accessor cannot leave a bit set in
        # `Value` that `ValidBits` calls meaningless.
        instance.value = bytes(value)
        instance.validBits = bytes(valid)


def optionsetbit(position: int, *, name: Optional[str] = None) -> Any:
    """Declare one bit of a structure-form OPC UA OptionSet.

    Used as the assigned value of an attribute in an [`@o6.datatype`][o6.datatype]
    class body that subtypes the ns0 `OptionSet`, alongside its `Value` and
    `ValidBits` members. `position` is the bit's position, exactly as the NodeSet
    `Definition` declares it — the low byte of `Value` first, least significant
    bit first.

    ```python
    @o6.datatype(ns="plant")
    class ExplosionZoneOptionSet(ns0.datatypes.OptionSet):
        value: o6.ByteString
        validBits: o6.ByteString

        zone0 = o6.optionsetbit(0, name="Zone 0")
        zone1 = o6.optionsetbit(1, name="Zone 1")
    ```

    Reading the attribute is three-valued: `True` when the bit is set and valid,
    `False` when it is clear and valid, and `None` when `ValidBits` says the bit
    means nothing — including when `ValidBits` is too short to reach it.
    Assigning `True` or `False` updates `Value` and `ValidBits` together, so an
    inconsistent pair cannot be produced through the accessor; assigning `None`
    makes the bit not valid again.

    This is the structure form of an OptionSet. The integer form is declared with
    [`@o6.optionsettype`][o6.optionsettype] and [`o6.bitmask`][o6.bitmask]
    instead; the two share a name and nothing else.

    Args:
        position: Bit position within the `Value` ByteString.
        name: OPC UA bit name, for a UA name that is not a valid Python
            identifier.

    Returns:
        An accessor for the declared bit.

    Raises:
        ValueError: The bit position is negative.
    """
    return _OptionSetBit(position, name=name)
