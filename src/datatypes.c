/* Copyright 2026 (c) o6 Automation GmbH */
/* SPDX-License-Identifier: AGPL-3.0-or-later
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Affero General Public License as published
 * by the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU Affero General Public License for more details.
 *
 * You should have received a copy of the GNU Affero General Public License
 * along with this program. If not, see <https://www.gnu.org/licenses/>.
 */

#include "datatypes.h"
#include "types_internal.h"
#include "ua_extension_namespacemapping.h"
#include "util/ua_util_internal.h"

#include <open62541/types.h>
#include <open62541/types_generated.h>
#include <open62541/util.h>

#include <stdlib.h>
#include <string.h>

/* Default capacity of a freshly-allocated block. */
#define DT_BLOCK_CAPACITY 1024

/* Singly-linked global chain of custom-DataType blocks, shared with open62541 configs.  
 * `g_chain_head` is the most-recently allocated block and doubles as the current fill target; 
 * `g_capacity` is the capacity of its `types` buffer.  Blocks are append-only and never moved, 
 * so every `UA_DataType*` handed out (to the generated PyTypes, the PyType registry, and sibling `memberType` pointers)
 * stays valid for the process lifetime. */
static UA_DataTypeArray *g_chain_head = NULL;
static size_t g_capacity = 0;

const UA_DataTypeArray *
o6_datatypes_global_chain(void) {
    return g_chain_head;
}

/* Allocate a fresh block with room for `capacity` types and prepend it to the global chain; 
 *
 * Returns 0 on success, -1 with a Python exception set on failure. */
static int
chain_add_block(size_t capacity) {
    if(capacity < 1)
        capacity = 1;

    UA_DataType *types = (UA_DataType*)UA_calloc(capacity, sizeof(UA_DataType));
    if(!types) {
        PyErr_NoMemory();
        return -1;
    }
    UA_DataTypeArray *arr = (UA_DataTypeArray*)UA_calloc(1, sizeof(UA_DataTypeArray));
    if(!arr) {
        UA_free(types);
        PyErr_NoMemory();
        return -1;
    }
    arr->types     = types;
    arr->typesSize = 0;             // grows as build_one_type fills it
    arr->cleanup   = false;         // freed at process shutdown; never by open62541
    arr->next      = g_chain_head;
    g_chain_head   = arr;
    g_capacity     = capacity;
    return 0;
}

/* Ensure the current block can hold at least ``n`` more types, adding a
 * new block (sized to at least ``n``, at least the default) if not.
 *
 * Returns 0 on success, -1 with a Python exception set on failure. */
static int
chain_reserve(size_t n) {
    size_t used = g_chain_head ? g_chain_head->typesSize : 0;
    if(g_chain_head && g_capacity - used >= n)
        return 0;
    size_t cap = n > DT_BLOCK_CAPACITY ? n : DT_BLOCK_CAPACITY;
    return chain_add_block(cap);
}

/* Membership predicate over the five OPC UA encoding-spec builtin ids an
 * EnumDescription's ``builtInType`` may carry: Byte=3, UInt16=5, Int32=6,
 * UInt32=7, UInt64=9.  These are the ns0 numeric identifiers (see
 * ``_OPTION_SET_BASES_BY_ID`` in the authoring layer), not the SDK's
 * ``UA_DATATYPEKIND_*`` enums — which are offset by the SDK's Boolean/SByte
 * prefix.  The authoring layer owns the table; this is the C-side check. */
static bool
is_supported_enumeration_builtin(UA_Byte builtinId) {
    switch(builtinId) {
    case 3: /* Byte */
    case 5: /* UInt16 */
    case 6: /* Int32 */
    case 7: /* UInt32 */
    case 9: /* UInt64 */
        return true;
    default:
        return false;
    }
}

/* Release a freshly-built ``UA_DataType``'s member-name strings and member array.
 * Not ``UA_DataType_clear``: the committed entry still needs the type name and NodeIds.
 * Used both for an OptionSet's corrected layout (§5 below) and for an
 * oversized enum's necessarily-incomplete one (see ``register_enumeration_type``). */
static void
free_type_members(UA_DataType *type) {
    if(!type->members)
        return;
    for(size_t i = 0; i < type->membersSize; ++i) {
        const UA_DataTypeMember *m = &type->members[i];
        UA_free((void*)(uintptr_t)m->memberName);
    }
    UA_free((void*)(uintptr_t)type->members);
    type->members = NULL;
    type->membersSize = 0;
}

/* The SDK names a type "<ns>:<Name>"; the XML encoder needs a valid element name. */
static void
strip_type_name_namespace(UA_DataType *type) {
    char *name = (char*)(uintptr_t)type->typeName;
    if(!name)
        return;
    char *c = name;
    while(*c >= '0' && *c <= '9')
        c++;
    if(c != name && *c == ':')
        memmove(name, c + 1, strlen(c + 1) + 1);
}

/* Build a UA_DataType from an EnumDescription, correcting an integer-form
 * OptionSet's layout to the base its description's ``builtInType`` declares.
 * See ``dev_docs/optionset_datatype_definition.md``: Registration order and member storage.
 *
 * Also handles an ordinary enumeration whose declared field count exceeds
 * what ``UA_DataType.membersSize`` — an 8-bit bitfield packed with no spare
 * bits into a ``UA_UInt32`` alongside ``memSize``/``typeKind``/two flags (see
 * ``open62541/include/open62541/types.h``) — can ever represent: 255.  There
 * is no way to widen it without changing ``sizeof(UA_DataType)``, which would
 * break the layout of every statically-initialized ``UA_DataType`` table in
 * the vendored SDK.  Instead, ask the SDK to build only the first 255
 * members (its scalar fields come out identical regardless of field count),
 * then strip that necessarily-incomplete member array rather than publish
 * it — ``build_one_type`` rebuilds the Python class's full member set from
 * the untruncated description directly, and the type's own binary/JSON
 * encoding needs only ``memSize``/``typeKind``, not per-member metadata. */
static UA_StatusCode
register_enumeration_type(UA_DataType *dst, UA_ExtensionObject *eo,
                          const UA_DataTypeArray *customTypes) {
    UA_EnumDescription *ed = (UA_EnumDescription*)eo->content.decoded.data;
    UA_Byte declaredBase = ed->builtInType;
    if(declaredBase == 0 || !is_supported_enumeration_builtin(declaredBase)) {
        PyErr_Format(PyExc_RuntimeError,
                     "register datatype: EnumDescription.builtInType is %u, which is "
                     "not a supported declared base.  An enumeration description must "
                     "carry its declared base: the Int32 builtin id (6) for an ordinary "
                     "enum, or the unsigned integer's for an OptionSet (Byte=3, "
                     "UInt16=5, UInt32=7, UInt64=9).",
                     (unsigned)declaredBase);
        return UA_STATUSCODE_BADINVALIDARGUMENT;
    }

    size_t declaredFieldsSize = ed->enumDefinition.fieldsSize;
    bool oversized = declaredFieldsSize > UA_BYTE_MAX;
    if(oversized)
        ed->enumDefinition.fieldsSize = UA_BYTE_MAX;

    /* The SDK's guard accepts only the Int32 builtin id (6), which is also
     * ``UA_DATATYPEKIND_UINT32`` by coincidence — never name the latter here.
     * Restore the declared base and field count on both paths so the
     * failure-diagnostics path, and the caller, read the original values. */
    ed->builtInType = 6; /* Int32 encoding-spec builtin id */
    UA_StatusCode res = UA_DataType_fromDescription(dst, eo, customTypes);
    if(oversized)
        ed->enumDefinition.fieldsSize = declaredFieldsSize;
    if(res != UA_STATUSCODE_GOOD) {
        ed->builtInType = declaredBase;
        if(!PyErr_Occurred())
            PyErr_Format(PyExc_RuntimeError,
                         "UA_DataType_fromEnumDescription failed: %s",
                         UA_StatusCode_name(res));
        return res;
    }

    /* The SDK's pinned values are correct for an ordinary enum (declared
     * base == Int32).  For an OptionSet, overwrite with the declared
     * unsigned integer's; the memory size comes from the SDK's own builtin
     * type table.  Encoding-spec ids are offset by 1 from the type kinds
     * (Boolean=0, SByte=1 come before Byte=2), so the builtin entry is at
     * ``declaredBase - 1``. */
    if(declaredBase != 6) {
        dst->typeKind = (UA_DataTypeKind)(declaredBase - 1);
        dst->memSize = UA_TYPES[declaredBase - 1].memSize;
    } else if(oversized) {
        free_type_members(dst);
    }

    ed->builtInType = declaredBase;
    return UA_STATUSCODE_GOOD;
}

/* Build {"NAME": value, ...} directly from an EnumDescription's own field
 * list, bypassing ``UA_DataType.members`` -- the only source left once
 * ``register_enumeration_type`` has stripped an oversized enum's incomplete
 * one.  Returns a new reference, or NULL with a Python error set. */
static PyObject *
build_enum_members_dict(const UA_EnumDefinition *def) {
    PyObject *members = PyDict_New();
    if(!members)
        return NULL;
    for(size_t i = 0; i < def->fieldsSize; i++) {
        const UA_EnumField *ef = &def->fields[i];
        PyObject *name = PyUnicode_FromStringAndSize((const char*)ef->name.data,
                                                      (Py_ssize_t)ef->name.length);
        PyObject *value = name ? PyLong_FromLongLong(ef->value) : NULL;
        int rc = value ? PyDict_SetItem(members, name, value) : -1;
        Py_XDECREF(name);
        Py_XDECREF(value);
        if(rc < 0) {
            Py_DECREF(members);
            return NULL;
        }
    }
    return members;
}

/* Convert a single Python description (StructureDescription / EnumDescription)
 * into a registered UA_DataType and Python class.  Grows the global chain
 * as needed.  Returns 0 on success, -1 on failure. */
static int
build_one_type(const char *namespaceName,
               PyObject *py_descr, PyObject *bases, PyObject *enumFactory,
               PyObject **out_nodeid, PyObject **out_pytype) {

    if(chain_reserve(1) < 0)
        return -1;
    /* chain_add_block owns mutable storage; open62541 exposes a const view. */
    UA_DataType *dst = (UA_DataType*)(uintptr_t)&g_chain_head->types[g_chain_head->typesSize];
    PyObject *enumOverrideMembers = NULL;

    UA_ExtensionObject eo;
    UA_ExtensionObject_init(&eo);
    UA_StatusCode res = py_description_to_eo(py_descr, &eo);
    if(res != UA_STATUSCODE_GOOD) {
        if(!PyErr_Occurred())
            PyErr_Format(PyExc_RuntimeError,
                         "Failed to convert description: %s",
                         UA_StatusCode_name(res));
        return -1;
    }

    // open62541 only supports valueRank=1, arrayDimensions=[0] fields;
    // strip away fixed array_dimensions to avoid BadInternalError.
    if(UA_ExtensionObject_hasDecodedType(&eo,
            &UA_TYPES[UA_TYPES_STRUCTUREDESCRIPTION])) {
        UA_StructureDescription *sd = (UA_StructureDescription*)eo.content.decoded.data;
        for(size_t f = 0; f < sd->structureDefinition.fieldsSize; f++) {
            UA_StructureField *sf = &sd->structureDefinition.fields[f];
            if(sf->valueRank == 1 && sf->arrayDimensionsSize > 0) {
                UA_Array_delete(sf->arrayDimensions, sf->arrayDimensionsSize, &UA_TYPES[UA_TYPES_UINT32]);
                sf->arrayDimensions = NULL;
                sf->arrayDimensionsSize = 0;
            }
        }
    }

    // DEDUP: if this is an ns0 enum or struct/union whose dataTypeId
    // matches a UA_TYPES[] entry, reuse the canonical UA_DataType instead
    // of allocating a new one.  The decorated Python class still binds to
    // the canonical pointer so a struct field of this type resolves back
    // to the decorated class via findCustomPyTypeWithFlag(&UA_TYPES[i]).
    int reused_ns0_type = 0;
    const UA_DataType *canonicalType = NULL;
    size_t canonicalIndex = 0;
    UA_NodeId ns0DataTypeId = UA_NODEID_NULL;
    if(UA_ExtensionObject_hasDecodedType(&eo,
            &UA_TYPES[UA_TYPES_ENUMDESCRIPTION])) {
        ns0DataTypeId = ((UA_EnumDescription*)eo.content.decoded.data)->dataTypeId;
    } else if(UA_ExtensionObject_hasDecodedType(&eo,
            &UA_TYPES[UA_TYPES_STRUCTUREDESCRIPTION])) {
        ns0DataTypeId = ((UA_StructureDescription*)eo.content.decoded.data)->dataTypeId;
    }
    if(ns0DataTypeId.namespaceIndex == 0) {
        for(size_t i = 0; i < UA_TYPES_COUNT; i++) {
            if(!UA_NodeId_equal(&UA_TYPES[i].typeId, &ns0DataTypeId))
                continue;
            canonicalType = &UA_TYPES[i];
            canonicalIndex = i;
            reused_ns0_type = 1;
            break;
        }
    }

    // Build `dst` from the description when we need its members to build
    // the Python class: always for non-dedup'd types, and for dedup'd
    // ENUMS (whose user-facing enum class must carry the decorator's
    // UPPER_SNAKE member names).  Dedup'd STRUCTS reuse the canonical
    // layout directly.
    int is_enum = UA_ExtensionObject_hasDecodedType(&eo,
                    &UA_TYPES[UA_TYPES_ENUMDESCRIPTION]);

    if(is_enum && !enumFactory) {
        PyErr_SetString(PyExc_TypeError,
                        "register datatype: an enumeration description must carry "
                        "the enum factory its authoring path chose (@o6.enumtype "
                        "builds an IntEnum, @o6.optionsettype an IntFlag).");
        UA_ExtensionObject_clear(&eo);
        return -1;
    }

    // Bootstrapped enums (NodeClass, StructureType) are built in
    // bootstrap_ns0_types.c before o6.nsx.ns0 is imported, so the
    // decorators can stamp `_nodeclass = NodeClass.<X>` on ns0 markers.
    // When ns0.py later declares its own `@o6.enumtype NodeClass`, reuse
    // that pre-built object — otherwise a marker's `_nodeclass` and
    // `o6.ns.ns0.NodeClass` would be distinct enums that compare equal by
    // value but not by identity.  A non-NULL pyUATypes slot uniquely
    // identifies a bootstrapped enum.
    PyTypeObject *bootstrapEnum =
        (reused_ns0_type && is_enum) ? pyUATypes[canonicalIndex] : NULL;

    int build_dst = (!reused_ns0_type) || (is_enum && !bootstrapEnum);

    if(build_dst) {
        /* Enum descriptions go through the compensation in
         * ``register_enumeration_type``; struct descriptions call the SDK
         * directly.  ``register_enumeration_type`` also owns the unset-
         * declared-base error path. */
        if(is_enum)
            res = register_enumeration_type(dst, &eo, g_chain_head);
        else
            res = UA_DataType_fromDescription(dst, &eo, g_chain_head);
        if(res != UA_STATUSCODE_GOOD) {
            /* For a structure description, point at the field whose data
             * type could not be resolved — useful for "Types must be
             * declared in dependency order" debugging.  ``eo`` is still
             * live here, so we can read ``structureDefinition.fields``.
             * An enumeration description's failure already carries a
             * specific Python exception from ``register_enumeration_type``. */
            const char *bad_field = "<unknown>";
            UA_NodeId bad_id = UA_NODEID_NULL;
            if(!is_enum &&
               UA_ExtensionObject_hasDecodedType(&eo, &UA_TYPES[UA_TYPES_STRUCTUREDESCRIPTION])) {
                UA_StructureDescription *sd = (UA_StructureDescription*)eo.content.decoded.data;
                for(size_t f = 0; f < sd->structureDefinition.fieldsSize; f++) {
                    const UA_StructureField *sf = &sd->structureDefinition.fields[f];
                    const UA_DataType *t = UA_findDataTypeWithCustom(&sf->dataType, g_chain_head);
                    if(!t) {
                        /* Copy the field name to a stack buffer; the eo
                         * memory is cleared shortly. */
                        if(sf->name.data && sf->name.length > 0) {
                            static char nameBuf[128];
                            size_t n = sf->name.length;
                            if(n >= sizeof(nameBuf))
                                n = sizeof(nameBuf) - 1;
                            memcpy(nameBuf, sf->name.data, n);
                            nameBuf[n] = '\0';
                            bad_field = nameBuf;
                        }
                        bad_id = sf->dataType;
                        break;
                    }
                }
                PyErr_Format(PyExc_RuntimeError,
                             "UA_DataType_fromDescription failed (res=%s, field=%s, missing ref ns=%u;i=%u).",
                             UA_StatusCode_name(res), bad_field,
                             (unsigned)bad_id.namespaceIndex,
                             (unsigned)bad_id.identifier.numeric);
            }
            UA_ExtensionObject_clear(&eo);
            memset(dst, 0, sizeof(UA_DataType));
            return -1;
        }
        strip_type_name_namespace(dst);

        /* An oversized enum's ``dst->members`` was stripped inside
         * ``register_enumeration_type`` -- rebuild the Python class's full
         * member set from the original description while ``eo`` is still
         * decoded, since ``dst`` alone can no longer carry it. */
        if(is_enum && dst->typeKind == UA_DATATYPEKIND_ENUM && dst->membersSize == 0) {
            UA_EnumDescription *ed = (UA_EnumDescription*)eo.content.decoded.data;
            enumOverrideMembers = build_enum_members_dict(&ed->enumDefinition);
            if(!enumOverrideMembers) {
                UA_ExtensionObject_clear(&eo);
                memset(dst, 0, sizeof(UA_DataType));
                return -1;
            }
        }
    }
    UA_ExtensionObject_clear(&eo);

    if(bootstrapEnum) {
        // Reuse the pre-built bootstrap enum as the single canonical class.
        PyObject *nodeId = UA2PY(&canonicalType->typeId,
                                 &UA_TYPES[UA_TYPES_NODEID], NULL);
        if(!nodeId)
            return -1;
        Py_INCREF(bootstrapEnum);
        *out_nodeid = nodeId;
        *out_pytype = (PyObject*)bootstrapEnum;
        return 0;
    }

    // Read the class members/layout from `dst` when we built it
    const UA_DataType *layoutType = build_dst ? dst : canonicalType;
    const UA_DataType *bindType = reused_ns0_type ? canonicalType : dst;

    PyObject *pyType = createCustomPyTypeBound(
        layoutType, bindType, namespaceName,
        (bases && bases != Py_None) ? bases : NULL,
        enumFactory, enumOverrideMembers);
    Py_XDECREF(enumOverrideMembers); /* buildEnumPyType took its own reference */
    if(!pyType) {
        // Only a freshly-built `dst` owns its members; free it on failure.
        if(build_dst) {
            UA_DataType_clear(dst);
            memset(dst, 0, sizeof(UA_DataType));
        }
        return -1;
    }
    PyObject *nodeId = UA2PY(&bindType->typeId, &UA_TYPES[UA_TYPES_NODEID], NULL);
    if(!nodeId) {
        Py_DECREF(pyType);
        if(build_dst) {
            UA_DataType_clear(dst);
            memset(dst, 0, sizeof(UA_DataType));
        }
        return -1;
    }

    if(reused_ns0_type) {
        // Dedup'd: the canonical UA_TYPES[] entry is the wire type and consumes no chain slot.
        if(build_dst) {
            UA_DataType_clear(dst);
            memset(dst, 0, sizeof(UA_DataType));
        }
    } else {
        // Freshly-built type.  An OptionSet's corrected kind is no longer ENUM, and its
        // member array must not survive registration — see
        // ``dev_docs/optionset_datatype_definition.md``: Registration order and member storage.
        if(is_enum && dst->typeKind != UA_DATATYPEKIND_ENUM)
            free_type_members(dst);
        g_chain_head->typesSize++;
    }

    *out_nodeid = nodeId;
    *out_pytype = pyType;
    return 0;
}

/* Register a single custom DataType in the given namespace, optionally
 * subclassing the Python classes in `bases` (a tuple or `None`).
 * `enum_factory` is the callable an EnumDescription's members are realized
 * with; `None` for a StructureDescription. */
PyObject *
o6_register_datatype(const char *namespaceName, PyObject *py_descr,
                     PyObject *bases, PyObject *enum_factory) {
    if(!py_descr) {
        PyErr_SetString(PyExc_TypeError,
                        "register_datatype: description is NULL");
        return NULL;
    }
    if(bases != NULL && bases != Py_None && !PyTuple_Check(bases)) {
        PyErr_SetString(PyExc_TypeError,
                        "register_datatype: bases must be a "
                        "tuple of classes or None");
        return NULL;
    }
    if(enum_factory == Py_None)
        enum_factory = NULL;
    if(enum_factory != NULL && !PyCallable_Check(enum_factory)) {
        PyErr_SetString(PyExc_TypeError,
                        "register_datatype: enum_factory must be callable or None");
        return NULL;
    }

    PyObject *nodeId = NULL;
    PyObject *pyType = NULL;
    if(build_one_type(namespaceName, py_descr, bases, enum_factory,
                      &nodeId, &pyType) < 0) {
        return NULL;
    }

    /* The generated PyType is kept alive for the process lifetime by
     * the custom-PyType registry (registerCustomPyType Py_INCREFs it),
     * so we don't retain a separate strong reference here.  The NodeId
     * and the returned tuple belong to the caller. */
    PyObject *tuple = PyTuple_Pack(2, nodeId, pyType);
    Py_DECREF(nodeId);
    Py_DECREF(pyType);
    return tuple;
}

/* Whether `type` is an entry of the process-global chain. */
static bool
in_global_chain(const UA_DataType *type) {
    for(const UA_DataTypeArray *a = o6_datatypes_global_chain(); a; a = a->next) {
        if(type >= a->types && type < a->types + a->typesSize)
            return true;
    }
    return false;
}

/* Point the members of the remapped copies in `chain` to the remapped copies
 * of their member types.  UA_DataType_copy keeps the member pointers, so a
 * copied structure still refers to process-global types with Python namespace
 * indices, and its DataTypeDefinition sends those indices to clients.  Both
 * layouts are identical; only the typeId of a member type differs.
 *
 * `chain` holds only copies made by o6_datatypes_update_custom_datatypes
 * (a server's chain starts empty, see server.c), so the member arrays are
 * owned heap memory.  The copies are freed together with the whole chain,
 * so pointers between arrays of one chain never dangle.  A member type whose
 * namespace is not mapped yet keeps its global type and is relinked by the
 * update that maps it. */
static void
relink_member_types(const UA_NamespaceMapping *nm, const UA_DataTypeArray *chain) {
    for(const UA_DataTypeArray *a = chain; a; a = a->next) {
        for(size_t i = 0; i < a->typesSize; i++) {
            const UA_DataType *type = &a->types[i];
            UA_DataTypeMember *members = (UA_DataTypeMember *)(uintptr_t)type->members;
            for(size_t j = 0; j < type->membersSize; j++) {
                const UA_DataType *memberType = members[j].memberType;
                if(!memberType || !in_global_chain(memberType))
                    continue;
                UA_UInt16 py_idx = memberType->typeId.namespaceIndex;
                if(py_idx >= nm->namespaceUrisSize || nm->namespaceUris[py_idx].length == 0)
                    continue;
                UA_NodeId remapped = memberType->typeId;
                remapped.namespaceIndex = UA_NamespaceMapping_Python2UA(nm, py_idx);
                const UA_DataType *copy = UA_findDataTypeWithCustom(&remapped, chain);
                if(copy && copy != memberType && copy->memSize == memberType->memSize &&
                   copy->typeKind == memberType->typeKind)
                    members[j].memberType = copy;
            }
        }
    }
}

/* Build a new UA_DataTypeArray with deep-copied, namespace-remapped types
 * from the global chain and chain it in front of *customDataTypes.
 * Skipps types that are already present with the correct remapped indices. */
UA_StatusCode
o6_datatypes_update_custom_datatypes(const UA_NamespaceMapping *nm, UA_DataTypeArray **customDataTypes) {
    /* First pass: count types from the global chain that (a) belong to a
     * namespace that has an explicit mapping and (b) are not yet present
     * in the customDataTypes chain after remapping the namespace index. */
    size_t total = 0;
    for(const UA_DataTypeArray *a = o6_datatypes_global_chain(); a; a = a->next) {
        for(size_t i = 0; i < a->typesSize; i++) {
            const UA_DataType *src = &a->types[i];
            UA_UInt16 py_idx = src->typeId.namespaceIndex;
            if(py_idx >= nm->namespaceUrisSize || nm->namespaceUris[py_idx].length == 0)
                continue;
            UA_NodeId remapped = src->typeId;
            remapped.namespaceIndex = UA_NamespaceMapping_Python2UA(nm, py_idx);
            if(UA_findDataTypeWithCustom(&remapped, *customDataTypes))
                continue;  /* already present with correct UA ns index */
            total++;
        }
    }

    if(total == 0)
        return UA_STATUSCODE_GOOD;

    UA_DataType *types = (UA_DataType *)UA_calloc(total, sizeof(UA_DataType));
    if(!types)
        return UA_STATUSCODE_BADOUTOFMEMORY;

    UA_DataTypeArray *arr = (UA_DataTypeArray *)UA_calloc(1, sizeof(UA_DataTypeArray));
    if(!arr) {
        UA_free(types);
        return UA_STATUSCODE_BADOUTOFMEMORY;
    }

    /* The owner (client/server) will UA_DataType_clear each element and free the arrays. */
    arr->types     = types;
    arr->typesSize = total;
    arr->cleanup   = true;
    arr->next      = *customDataTypes;

    /* Second pass: deep-copy new types with remapped namespace indices. */
    size_t out = 0;
    for(const UA_DataTypeArray *a = o6_datatypes_global_chain(); a; a = a->next) {
        for(size_t i = 0; i < a->typesSize; i++) {
            const UA_DataType *src = &a->types[i];
            UA_UInt16 py_idx = src->typeId.namespaceIndex;
            if(py_idx >= nm->namespaceUrisSize || nm->namespaceUris[py_idx].length == 0)
                continue;
            UA_UInt16 ua_idx = UA_NamespaceMapping_Python2UA(nm, py_idx);
            UA_NodeId remapped = src->typeId;
            remapped.namespaceIndex = ua_idx;
            if(UA_findDataTypeWithCustom(&remapped, *customDataTypes))
                continue;

            UA_DataType *dst = &types[out++];
            UA_StatusCode st = UA_DataType_copy(src, dst);
            if(st != UA_STATUSCODE_GOOD) {
                for(size_t j = 0; j < out; j++)
                    UA_DataType_clear(&types[j]);
                UA_free(types);
                UA_free(arr);
                return st;
            }
            dst->typeId.namespaceIndex = ua_idx;
            dst->binaryEncodingId.namespaceIndex =
                UA_NamespaceMapping_Python2UA(nm, dst->binaryEncodingId.namespaceIndex);
            dst->xmlEncodingId.namespaceIndex =
                UA_NamespaceMapping_Python2UA(nm, dst->xmlEncodingId.namespaceIndex);
        }
    }

    /* Relink over the whole chain: the new copies can be member types of
     * structures copied by an earlier update, and vice versa. */
    relink_member_types(nm, arr);

    *customDataTypes = arr;
    return UA_STATUSCODE_GOOD;
}

void
o6_datatypes_clear_custom_datatypes(UA_DataTypeArray **customDataTypes) {
    if(!customDataTypes || !*customDataTypes)
        return;
    UA_cleanupDataTypeWithCustom(*customDataTypes);
    *customDataTypes = NULL;
}
