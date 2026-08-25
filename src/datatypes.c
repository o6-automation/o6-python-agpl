/* Copyright 2026 (c) o6 Automation GmbH */
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

/* Convert a single Python description (StructureDescription / EnumDescription) into a py_type and append it
 * Optional Python `bases` for the generated PyType.
 * Grows the global chain as needed.
 *
 * Returns 0 on success, -1 on failure. */
static int
build_one_type(const char *namespaceName,
               PyObject *py_descr, PyObject *bases,
               PyObject **out_nodeid, PyObject **out_pytype) {

    if(chain_reserve(1) < 0)
        return -1;
    UA_DataType *dst = &g_chain_head->types[g_chain_head->typesSize];

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

    // Normalize: open62541 only supports valueRank=1, arrayDimensions=[0] fields
    // Strip away fixed array_dimensions to avoid BadInternalError
    if(UA_ExtensionObject_hasDecodedType(&eo,
            &UA_TYPES[UA_TYPES_ENUMDESCRIPTION])) {
        UA_EnumDescription *ed =
            (UA_EnumDescription*)eo.content.decoded.data;
        if(ed->builtInType == 0)
            ed->builtInType = UA_DATATYPEKIND_UINT32;
    }
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

    // DEDUP: 
    // if this is an NS0 enum or struct/union whose dataTypeId matches a UA_TYPES[] entry, 
    // reuse the canonical UA_DataType from UA_TYPES[] instead of allocating a new one. 
    // The Python class side (createCustomPyType below) is unchanged — 
    // our @o6.datatype / @o6.enumtype-decorated class is still the user-facing class, now bound to the single canonical UA_DataType.
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
            // Bind the decorated Python class straight to the canonical UA_TYPES[] entry — no chain copy. 
            // Binding the decorated class to the *canonical* pointer (rather than a copy) 
            // lets us resolve a struct field of this type back to the decorated class via findCustomPyType(&UA_TYPES[i]).
            canonicalType = &UA_TYPES[i];
            canonicalIndex = i;
            reused_ns0_type = 1;
            break;
        }
    }

    // Build `dst` from the description when we need its members to build the Python class: 
    // always for non-dedup'd types, and for dedup'd ENUMS (whose user-facing IntEnum must carry the
    // decorator's UPPER_SNAKE member names, not open62541's canonical PascalCase names). 
    // Dedup'd STRUCTS reuse the canonical layout directly.
    int is_enum = UA_ExtensionObject_hasDecodedType(&eo,
                    &UA_TYPES[UA_TYPES_ENUMDESCRIPTION]);

    // Bootstrapped enums (NodeClass, StructureType) are built on the C side in
    // bootstrap_ns0_types.c *before* o6.nsx.ns0 is imported, so the
    // several decorators can stamp `_nodeclass = NodeClass.<X>` on
    // markers declared in ns0.py.  When ns0.py later declares its own
    // `@o6.enumtype NodeClass`, reuse that pre-built object instead of
    // building a second, distinct enum class: otherwise a marker's
    // `_nodeclass` (the bootstrap enum) and `o6.ns.ns0.NodeClass` (a fresh
    // enum) would be different objects that compare equal by value but not by
    // identity.  pyUATypes[] is populated for these canonical entries *only* by
    // the bootstrap, so a non-NULL slot uniquely identifies a bootstrapped enum.
    PyTypeObject *bootstrapEnum =
        (reused_ns0_type && is_enum) ? pyUATypes[canonicalIndex] : NULL;

    int build_dst = (!reused_ns0_type) || (is_enum && !bootstrapEnum);

    if(build_dst) {
        // Resolve cross-references against the whole global chain
        res = UA_DataType_fromDescription(dst, &eo, g_chain_head);
        if(res != UA_STATUSCODE_GOOD) {
            /* Build a clear error message that points at the field whose
             * data type could not be resolved — extremely useful for
             * "Types must be declared in dependency order" debugging.
             * Note: ``eo`` is still live here (we haven't cleared it
             * yet), so we can read ``structureDefinition.fields`` to
             * pinpoint the offending field. */
            const char *bad_field = "<unknown>";
            UA_NodeId bad_id = UA_NODEID_NULL;
            if(UA_ExtensionObject_hasDecodedType(&eo, &UA_TYPES[UA_TYPES_STRUCTUREDESCRIPTION])) {
                UA_StructureDescription *sd = (UA_StructureDescription*)eo.content.decoded.data;
                for(size_t f = 0; f < sd->structureDefinition.fieldsSize; f++) {
                    const UA_StructureField *sf = &sd->structureDefinition.fields[f];
                    const UA_DataType *t = UA_findDataTypeWithCustom(&sf->dataType, g_chain_head);
                    if(!t) {
                        /* Guard against empty/NULL field names — passing
                         * NULL to %s would crash PyErr_Format. */
                        if(sf->name.data && sf->name.length > 0) {
                            /* Copy the field name to a small stack buffer
                             * since the underlying eo memory will be
                             * cleared shortly. */
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
            }
            PyErr_Format(PyExc_RuntimeError,
                         "UA_DataType_fromDescription failed (res=%s, field=%s, missing ref ns=%u;i=%u).",
                         UA_StatusCode_name(res), bad_field,
                         (unsigned)bad_id.namespaceIndex,
                         (unsigned)bad_id.identifier.numeric);
            UA_ExtensionObject_clear(&eo);
            memset(dst, 0, sizeof(UA_DataType));
            return -1;
        }
    }
    UA_ExtensionObject_clear(&eo);

    if(bootstrapEnum) {
        // Reuse the pre-built bootstrap enum as the single canonical class.
        PyObject *nodeId = UA2PY((void*)&canonicalType->typeId,
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
        (bases && bases != Py_None) ? bases : NULL);
    if(!pyType) {
        // Only a freshly-built `dst` owns its members; free it on failure.
        if(build_dst) {
            UA_DataType_clear(dst);
            memset(dst, 0, sizeof(UA_DataType));
        }
        return -1;
    }
    PyObject *nodeId = UA2PY((void*)&bindType->typeId, &UA_TYPES[UA_TYPES_NODEID], NULL);
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
        // Freshly-built type: commit the chain slot.
        g_chain_head->typesSize++;
    }

    *out_nodeid = nodeId;
    *out_pytype = pyType;
    return 0;
}

/* Register a single custom DataType in the given namespace, optionally
 * subclassing the Python classes in `bases` (a tuple or `None`). */
PyObject *
o6_register_datatype(const char *namespaceName, PyObject *py_descr,
                     PyObject *bases) {
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

    PyObject *nodeId = NULL;
    PyObject *pyType = NULL;
    if(build_one_type(namespaceName, py_descr, bases, &nodeId, &pyType) < 0) {
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
