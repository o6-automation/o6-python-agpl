/* Copyright (c) 2026 o6 Automation GmbH
 *
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

#include "../types_internal.h"
#include "../module.h"
#include <open62541/types.h>
#include <open62541/types_generated.h>
#include <open62541/util.h>

#ifdef DEBUG_TYPE_REGISTRATION
#define TR_LOG(fmt, ...) printf("[TYPE_REG] " fmt "\n", ##__VA_ARGS__)
#else
#define TR_LOG(fmt, ...)
#endif

static UA_StatusCode
py_description_to_eo(PyObject *py_descr, UA_ExtensionObject *eo) {
    const UA_DataType *py_ua_type = PY2UAType(Py_TYPE(py_descr));
    if(!py_ua_type) {
        PyErr_SetString(PyExc_TypeError,
                        "Expected StructureDescription or EnumDescription");
        return UA_STATUSCODE_BADINVALIDARGUMENT;
    }

    const UA_DataType *descr_type = NULL;
    if(UA_NodeId_equal(&py_ua_type->typeId,
                       &UA_TYPES[UA_TYPES_STRUCTUREDESCRIPTION].typeId))
        descr_type = &UA_TYPES[UA_TYPES_STRUCTUREDESCRIPTION];
    else if(UA_NodeId_equal(&py_ua_type->typeId,
                            &UA_TYPES[UA_TYPES_ENUMDESCRIPTION].typeId))
        descr_type = &UA_TYPES[UA_TYPES_ENUMDESCRIPTION];
    else {
        PyErr_Format(PyExc_TypeError,
                     "Expected StructureDescription or EnumDescription, got %s",
                     Py_TYPE(py_descr)->tp_name);
        return UA_STATUSCODE_BADINVALIDARGUMENT;
    }

    void *ua_descr = UA_new(descr_type);
    if(!ua_descr)
        return UA_STATUSCODE_BADOUTOFMEMORY;

    PyObject *res = PY2UA(py_descr, ua_descr, descr_type);
    if(!res) {
        UA_delete(ua_descr, descr_type);
        return UA_STATUSCODE_BADINVALIDARGUMENT;
    }

    UA_ExtensionObject_setValue(eo, ua_descr, descr_type);
    return UA_STATUSCODE_GOOD;
}

/* Shared slots and methods for dynamically created struct types.
 * Identical to those used for ns0 types in types.c. */
static PyMethodDef customStruct_methods[] = {
    {"__dir__", (PyCFunction)pyUAStruct_dir, METH_NOARGS, NULL},
    {"__copy__", (PyCFunction)pyUAStruct_copy, METH_NOARGS, NULL},
    {NULL}
};

static PyType_Slot customStruct_slots[] = {
    {Py_tp_dealloc, (void *)pyUAStruct_dealloc},
    {Py_tp_traverse, (void *)pyUAStruct_traverse},
    {Py_tp_clear, (void *)pyUAStruct_clear},
    {Py_tp_new, (void *)PyType_GenericNew},
    {Py_tp_alloc, (void *)PyType_GenericAlloc},
    {Py_tp_str, (void *)pyUAStruct_str},
    {Py_tp_repr, (void *)pyUAStruct_repr},
    {Py_tp_getattro, (void *)pyUAStruct_getattro},
    {Py_tp_setattro, (void *)pyUAStruct_setattro},
    {Py_tp_methods, (void *)customStruct_methods},
    {0, NULL}
};

static PyType_Spec customStruct_spec = {
    .basicsize = sizeof(PyUAStruct),
    .flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HAVE_GC | Py_TPFLAGS_BASETYPE,
    .slots = customStruct_slots
};

static PyObject *
createCustomPyType(const UA_DataType *uaType, const char *namespaceName) {
    /* Build a name like "o6.<namespace>.<TypeName>".
     * Strip the namespace qualifier (e.g. "1:FetchResult" -> "FetchResult") */
    const char *rawName = uaType->typeName ? uaType->typeName : "Unknown";
    const char *colon = strchr(rawName, ':');
    const char *shortName = colon ? colon + 1 : rawName;

    char nameBuf[256];
    if(namespaceName && namespaceName[0])
        snprintf(nameBuf, sizeof(nameBuf), "o6.%s.%s", namespaceName, shortName);
    else
        snprintf(nameBuf, sizeof(nameBuf), "o6.%s", shortName);

    /* Enum types get a real Python IntEnum class */
    if(uaType->typeKind == UA_DATATYPEKIND_ENUM) {
        PyObject *enum_mod = PyImport_ImportModule("enum");
        if(!enum_mod)
            return NULL;
        PyObject *IntEnum = PyObject_GetAttrString(enum_mod, "IntEnum");
        Py_DECREF(enum_mod);
        if(!IntEnum)
            return NULL;

        /* Build {"NORMAL": 0, "FAILURE": 1, ...} */
        PyObject *members = PyDict_New();
        if(!members) {
            Py_DECREF(IntEnum);
            return NULL;
        }
        for(size_t i = 0; i < uaType->membersSize; i++) {
            const UA_DataTypeMember *dtm = &uaType->members[i];
            /* For enums, memberType stores the integer value cast to a pointer */
            long value = (long)(intptr_t)dtm->memberType;
            PyObject *pyVal = PyLong_FromLong(value);
            if(!pyVal) {
                Py_DECREF(members);
                Py_DECREF(IntEnum);
                return NULL;
            }
            if(PyDict_SetItemString(members, dtm->memberName, pyVal) < 0) {
                Py_DECREF(pyVal);
                Py_DECREF(members);
                Py_DECREF(IntEnum);
                return NULL;
            }
            Py_DECREF(pyVal);
        }

        /* IntEnum(shortName, members_dict) */
        PyObject *pyType = PyObject_CallFunction(IntEnum, "sO", shortName, members);
        Py_DECREF(members);
        Py_DECREF(IntEnum);
        if(!pyType)
            return NULL;

        PyTypeObject_setUAType((PyTypeObject*)pyType, uaType);
        registerCustomPyType(uaType, (PyTypeObject*)pyType, nameBuf);

        TR_LOG("Created Python IntEnum %s for UA enum %s",
               nameBuf, uaType->typeName ? uaType->typeName : "(null)");
        return pyType;
    }

    customStruct_spec.name = nameBuf;
    PyObject *pyType = PyType_FromSpec(&customStruct_spec);
    if(!pyType)
        return NULL;

    PyTypeObject_setUAType((PyTypeObject*)pyType, uaType);
    registerCustomPyType(uaType, (PyTypeObject*)pyType, nameBuf);

    TR_LOG("Created Python type %s for UA type %s (memSize=%zu)",
           nameBuf, uaType->typeName ? uaType->typeName : "(null)",
           uaType->memSize);

    return pyType;
}

/* Capsule name strings used by build/link capsules */
#define UA_DTA_OWNER_CAPSULE "UA_DataTypeArray.owner"
#define UA_DTA_LINK_CAPSULE  "UA_DataTypeArray.link"

/* Destructor for the owner capsule: clears every UA_DataType entry,
 * frees the types array and the UA_DataTypeArray struct itself. */
static void
freeOwnerCapsule(PyObject *capsule) {
    UA_DataTypeArray *array =
        (UA_DataTypeArray*)PyCapsule_GetPointer(capsule, UA_DTA_OWNER_CAPSULE);
    if(!array)
        return;
    for(size_t i = 0; i < array->typesSize; i++)
        UA_DataType_clear(&array->types[i]);
    UA_free((void*)array->types);
    UA_free(array);
}

/* Destructor for link capsules: frees only the thin-wrapper struct.
 * The actual type data is owned by the corresponding owner capsule. */
static void
freeLinkCapsule(PyObject *capsule) {
    UA_DataTypeArray *wrapper =
        (UA_DataTypeArray*)PyCapsule_GetPointer(capsule, UA_DTA_LINK_CAPSULE);
    UA_free(wrapper);
}

/* Converts every description in `descriptions` to a UA_DataType, creates the
 * matching Python type objects and builds the result list.  No linking into
 * any client/server config happens here.
 *
 * lookup_chain  existing type chain used to resolve member-type references
 *               during conversion.  May be NULL.
 * out_array     set to the freshly allocated UA_DataTypeArray on success.
 *               The array has cleanup=false; the caller (capsule destructor)
 *               is responsible for freeing it.
 *
 * Returns a PyList of (NodeId, PyType) tuples on success, NULL on error. */
static PyObject *
buildCustomDataTypesCore(PyObject *descriptions,
                         const char *namespaceName,
                         const UA_DataTypeArray *lookup_chain,
                         UA_DataTypeArray **out_array) {
    if(!PyList_Check(descriptions)) {
        PyErr_SetString(PyExc_TypeError,
                        "Expected a list of StructureDescription / EnumDescription");
        return NULL;
    }

    Py_ssize_t count = PyList_Size(descriptions);
    if(count == 0) {
        /* Return an empty array + empty list */
        UA_DataTypeArray *array =
            (UA_DataTypeArray*)UA_calloc(1, sizeof(UA_DataTypeArray));
        if(!array) {
            PyErr_NoMemory();
            return NULL;
        }
        array->cleanup = false;
        *out_array = array;
        return PyList_New(0);
    }

    TR_LOG("Building %zd custom data types", count);

    UA_DataType *types =
        (UA_DataType*)UA_calloc((size_t)count, sizeof(UA_DataType));
    if(!types) {
        PyErr_NoMemory();
        return NULL;
    }

    UA_DataTypeArray *array =
        (UA_DataTypeArray*)UA_calloc(1, sizeof(UA_DataTypeArray));
    if(!array) {
        UA_free(types);
        PyErr_NoMemory();
        return NULL;
    }

    array->types    = types;
    array->typesSize = (size_t)count;
    array->cleanup  = false; /* owner capsule / caller handles cleanup */
    /* Temporarily chain to the lookup_chain so that UA_DataType_fromDescription
     * can resolve types that were already built (either in a previous batch
     * or earlier in this same array).                                        */
    array->next = (UA_DataTypeArray*)lookup_chain;

    for(Py_ssize_t i = 0; i < count; i++) {
        PyObject *py_descr = PyList_GetItem(descriptions, i);
        if(!py_descr)
            goto error;

        UA_ExtensionObject eo;
        UA_ExtensionObject_init(&eo);
        UA_StatusCode res = py_description_to_eo(py_descr, &eo);
        if(res != UA_STATUSCODE_GOOD) {
            if(!PyErr_Occurred())
                PyErr_Format(PyExc_RuntimeError,
                             "Failed to convert description %zd: %s",
                             i, UA_StatusCode_name(res));
            goto error;
        }

        /* NodeSet2 XML often leaves builtInType unset (0) for plain enums.
         * UA_DataType_fromEnumDescription requires Int32 (== UA_DATATYPEKIND_UINT32).
         * Default it here so UA_DataType_fromDescription works for all enums. */
        if(UA_ExtensionObject_hasDecodedType(&eo, &UA_TYPES[UA_TYPES_ENUMDESCRIPTION])) {
            UA_EnumDescription *ed =
                (UA_EnumDescription*)eo.content.decoded.data;
            if(ed->builtInType == 0)
                ed->builtInType = UA_DATATYPEKIND_UINT32;
        }

        res = UA_DataType_fromDescription(&types[i], &eo, array);
        UA_ExtensionObject_clear(&eo);

        if(res != UA_STATUSCODE_GOOD) {
            PyErr_Format(PyExc_RuntimeError,
                         "UA_DataType_fromDescription failed for entry %zd: %s",
                         i, UA_StatusCode_name(res));
            goto error;
        }

        TR_LOG("Converted type %zd: %s (memSize=%zu, members=%zu)",
               i, types[i].typeName ? types[i].typeName : "(null)",
               types[i].memSize, types[i].membersSize);
    }

    /* Detach from the lookup chain — the array is now standalone. */
    array->next = NULL;

    /* Create Python type objects and build the result list. */
    PyObject *result = PyList_New(count);
    if(!result)
        goto error;

    for(Py_ssize_t i = 0; i < count; i++) {
        PyObject *pyType = createCustomPyType(&types[i], namespaceName);
        if(!pyType) {
            Py_DECREF(result);
            goto error;
        }

        PyObject *nodeId = UA2PY((void*)&types[i].typeId,
                                 &UA_TYPES[UA_TYPES_NODEID]);
        if(!nodeId) {
            Py_DECREF(pyType);
            Py_DECREF(result);
            goto error;
        }

        PyObject *tuple = PyTuple_Pack(2, nodeId, pyType);
        Py_DECREF(nodeId);
        Py_DECREF(pyType);
        if(!tuple) {
            Py_DECREF(result);
            goto error;
        }

        PyList_SET_ITEM(result, i, tuple); /* steals reference */
    }

    TR_LOG("Built %zd custom data types with Python classes", count);
    *out_array = array;
    return result;

error:
    array->next = NULL;
    for(Py_ssize_t j = 0; j < count; j++)
        UA_DataType_clear(&types[j]);
    UA_free(types);
    UA_free(array);
    *out_array = NULL;
    return NULL;
}

/* Module-level Python callable: build types without any client/server.
 *
 * build_custom_data_types(descriptions[, namespace_name[, lookup_capsule]])
 *   -> (capsule, [(NodeId, PyType), ...])
 *
 * lookup_capsule (optional): owner capsule from a previous
 *   build_custom_data_types() call.  The array it owns is used as the lookup
 *   chain so the new types can reference already-built types.  Pass this when
 *   building a batch of types in multiple passes (dependency ordering).
 *
 * The returned capsule must be stored (e.g. in a Descriptor) for as long as
 * the Python types are needed.  Pass it to
 * client.link_custom_data_types() / server.link_custom_data_types() to make
 * the types available for encoding/decoding. */
PyObject *
py_buildCustomDataTypes(PyObject *Py_UNUSED(module), PyObject *args) {
    PyObject *descriptions;
    const char *namespaceName = NULL;
    PyObject *lookup_capsule = NULL;
    if(!PyArg_ParseTuple(args, "O|zO", &descriptions, &namespaceName,
                         &lookup_capsule))
        return NULL;

    const UA_DataTypeArray *lookup_chain = NULL;
    if(lookup_capsule && lookup_capsule != Py_None) {
        lookup_chain = (const UA_DataTypeArray*)PyCapsule_GetPointer(
            lookup_capsule, UA_DTA_OWNER_CAPSULE);
        if(!lookup_chain)
            return NULL; /* PyCapsule_GetPointer set an error */
    }

    UA_DataTypeArray *array = NULL;
    PyObject *result =
        buildCustomDataTypesCore(descriptions, namespaceName, lookup_chain, &array);
    if(!result)
        return NULL;

    /* Chain the new array onto the lookup so this capsule IS the full lookup
     * chain for subsequent builds.  buildCustomDataTypesCore already cleared
     * array->next; we set it here so callers passing this capsule as
     * lookup_capsule can see all previously-built types in the chain.
     *
     * NOTE: freeOwnerCapsule does NOT traverse next, so the chain pointer
     * does not affect cleanup ordering.  All capsules in the chain must be
     * kept alive externally (e.g. stored in Descriptor._capsule list).    */
    array->next = (UA_DataTypeArray*)lookup_chain;

    PyObject *capsule =
        PyCapsule_New(array, UA_DTA_OWNER_CAPSULE, freeOwnerCapsule);
    if(!capsule) {
        array->next = NULL;
        for(size_t i = 0; i < array->typesSize; i++)
            UA_DataType_clear(&array->types[i]);
        UA_free((void*)array->types);
        UA_free(array);
        Py_DECREF(result);
        return NULL;
    }

    PyObject *ret = PyTuple_Pack(2, capsule, result);
    Py_DECREF(capsule);
    Py_DECREF(result);
    return ret;
}

/* Link an owner capsule into *configCustomTypes.
 *
 * Creates a thin UA_DataTypeArray wrapper (cleanup=false) pointing to the
 * same types array owned by the capsule, appends it to the config chain, and
 * returns a "link capsule" that must be kept alive while the client/server is
 * alive (its destructor frees only the thin wrapper struct).             */
PyObject *
linkCustomDataTypesImpl(UA_DataTypeArray **configCustomTypes,
                        PyObject *capsule) {
    UA_DataTypeArray *src =
        (UA_DataTypeArray*)PyCapsule_GetPointer(capsule, UA_DTA_OWNER_CAPSULE);
    if(!src)
        return NULL; /* PyCapsule_GetPointer already set an error */

    UA_DataTypeArray *wrapper =
        (UA_DataTypeArray*)UA_calloc(1, sizeof(UA_DataTypeArray));
    if(!wrapper) {
        PyErr_NoMemory();
        return NULL;
    }

    wrapper->types     = (UA_DataType*)src->types;
    wrapper->typesSize = src->typesSize;
    wrapper->cleanup   = false; /* open62541 must not free the shared types */
    wrapper->next      = NULL;

    if(*configCustomTypes) {
        UA_DataTypeArray *tail = *configCustomTypes;
        while(tail->next)
            tail = tail->next;
        tail->next = wrapper;
    } else {
        *configCustomTypes = wrapper;
    }

    return PyCapsule_New(wrapper, UA_DTA_LINK_CAPSULE, freeLinkCapsule);
}