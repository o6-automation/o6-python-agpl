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

// Registry of custom (runtime-registered) Python types, resolving UA_DataType* -> PyTypeObject*.
//
// Populated by createCustomPyTypeBound() below (via registerCustomPyType)
// Used consulted by UA2PYType() (via findCustomPyType) so that a decorated @o6.datatype / @o6.enumtype class wins over the plain C-generated PyType.
//
// A single growable array: 
// nothing holds a pointer to an individual entry (findCustomPyType returns the PyType, not the entry), 
// so the backing buffer is free to move on realloc.  
typedef struct CustomPyType {
    const UA_DataType *uaType;
    PyTypeObject *pyType;
    char typeName[128]; // Owned name buffer for PyType_Spec
} CustomPyType;

static CustomPyType *customPyTypes = NULL;
static size_t customPyTypesSize = 0;
static size_t customPyTypesCapacity = 0;

void
registerCustomPyType(const UA_DataType *uaType, PyTypeObject *pyType, const char *typeName) {
    if(customPyTypesSize == customPyTypesCapacity) {
        size_t new_cap = customPyTypesCapacity ? customPyTypesCapacity * 2 : 1024;
        CustomPyType *grown =
            (CustomPyType*)realloc(customPyTypes, new_cap * sizeof(CustomPyType));
        if(!grown)
            return;   // best-effort: drop the mapping on OOM, as before
        customPyTypes = grown;
        customPyTypesCapacity = new_cap;
    }

    CustomPyType *entry = &customPyTypes[customPyTypesSize++];
    entry->uaType = uaType;
    Py_INCREF(pyType);
    entry->pyType = pyType;
    snprintf(entry->typeName, sizeof(entry->typeName), "%s", typeName);
}

PyTypeObject *
findCustomPyType(const UA_DataType *uaType) {
    for(size_t i = 0; i < customPyTypesSize; i++) {
        if(customPyTypes[i].uaType == uaType)
            return customPyTypes[i].pyType;
    }
    return NULL;
}

UA_StatusCode
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

    PyObject *res = PY2UA(py_descr, ua_descr, descr_type, NULL, NULL);
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
    {"__deepcopy__", (PyCFunction)pyUA_deepcopy, METH_O, NULL},
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

/* Build a real Python IntEnum for a UA enum type.
 * Returns a new reference, or NULL with a Python error set. */
static PyObject *
buildEnumPyType(const UA_DataType *uaType, const char *shortName, PyObject *bases) {
    PyObject *enum_mod = PyImport_ImportModule("enum");
    if(!enum_mod)
        return NULL;
    // All OPC UA enumerations are modelled as `IntFlag`:
    // option-set / bitmask enums (BrowseResultMask, AttributeWriteMask, …) carry combined values such as 44 that a strict IntEnum would reject,
    // and the `FlagBoundary.KEEP` policy keeps otherwise-undefined bits intact on the wire.  
    // Plain enumerations behave identically to an IntEnum for their declared members, so this is a superset.
    PyObject *IntFlag = PyObject_GetAttrString(enum_mod, "IntFlag");
    PyObject *flagBoundary = PyObject_GetAttrString(enum_mod, "FlagBoundary");
    PyObject *keep = flagBoundary ? PyObject_GetAttrString(flagBoundary, "KEEP") : NULL;
    Py_XDECREF(flagBoundary);
    Py_DECREF(enum_mod);
    if(!IntFlag || !keep) {
        Py_XDECREF(IntFlag);
        Py_XDECREF(keep);
        return NULL;
    }

    /* Build {"NORMAL": 0, "FAILURE": 1, ...} */
    PyObject *members = PyDict_New();
    if(!members) {
        Py_DECREF(IntFlag);
        Py_DECREF(keep);
        return NULL;
    }
    for(size_t i = 0; i < uaType->membersSize; i++) {
        const UA_DataTypeMember *dtm = &uaType->members[i];
        /* For enums, memberType stores the integer value cast to a pointer */
        long value = (long)(intptr_t)dtm->memberType;
        PyObject *pyVal = PyLong_FromLong(value);
        int rc = pyVal ? PyDict_SetItemString(members, dtm->memberName, pyVal) : -1;
        Py_XDECREF(pyVal);
        if(rc < 0) {
            Py_DECREF(members);
            Py_DECREF(IntFlag);
            Py_DECREF(keep);
            return NULL;
        }
    }

    // IntFlag(shortName, members_dict, boundary=FlagBoundary.KEEP) 
    PyObject *args = Py_BuildValue("(sO)", shortName, members);
    PyObject *kwargs = PyDict_New();
    if(args && kwargs)
        PyDict_SetItemString(kwargs, "boundary", keep);
    PyObject *pyType = (args && kwargs) ? PyObject_Call(IntFlag, args, kwargs) : NULL;
    Py_XDECREF(args);
    Py_XDECREF(kwargs);
    Py_DECREF(members);
    Py_DECREF(IntFlag);
    Py_DECREF(keep);
    if(!pyType)
        return NULL;

    // Inject the user-supplied abstract base(s) into the MRO.
    if(bases && PyObject_SetAttrString(pyType, "__bases__", bases) < 0) {
        Py_DECREF(pyType);
        return NULL;
    }

    TR_LOG("Created Python IntFlag for UA enum %s",
           uaType->typeName ? uaType->typeName : "(null)");
    return pyType;
}

/* Build a C-backed struct type for a UA structure/union type.
 * Returns a new reference, or NULL with a Python error set. */
static PyObject *
buildStructPyType(const UA_DataType *uaType, const char *name, PyObject *bases) {
    customStruct_spec.name = name;

    /* When subclassing another UA type, the C-side customStruct_slots +
     * PyUAStruct basicsize are shared, so the new type is layout-compatible
     * with the base and accepts the same tp_getattro/tp_setattro behaviour.
     * PyType_FromSpecWithBases walks the bases' MRO to compute the resulting
     * tp_base, so any flags (Py_TPFLAGS_BASETYPE) on the base are inherited. */
    PyObject *pyType = bases ? PyType_FromSpecWithBases(&customStruct_spec, bases)
                             : PyType_FromSpec(&customStruct_spec);
    if(!pyType)
        return NULL;

    TR_LOG("Created Python type %s for UA type %s (memSize=%zu)",
           name, uaType->typeName ? uaType->typeName : "(null)", uaType->memSize);
    return pyType;
}

PyObject *
createCustomPyTypeBound(const UA_DataType *layoutType, const UA_DataType *bindType,
                        const char *namespaceName, PyObject *bases) {
    /* Build a name like "o6.<namespace>.<TypeName>".
     * Strip the namespace qualifier (e.g. "1:FetchResult" -> "FetchResult") */
    const char *rawName = layoutType->typeName ? layoutType->typeName : "Unknown";
    const char *colon = strchr(rawName, ':');
    const char *shortName = colon ? colon + 1 : rawName;

    char nameBuf[256];
    if(namespaceName && namespaceName[0])
        snprintf(nameBuf, sizeof(nameBuf), "o6.%s.%s", namespaceName, shortName);
    else
        snprintf(nameBuf, sizeof(nameBuf), "o6.%s", shortName);

    // `layoutType` supplies the members/values used to build the Python class. 
    // `bindType` is the UA_DataType the class is registered against for wire
    // encoding/decoding and for UA_DataType* -> PyType resolution
    PyObject *pyType = (layoutType->typeKind == UA_DATATYPEKIND_ENUM)
                           ? buildEnumPyType(layoutType, shortName, bases)
                           : buildStructPyType(layoutType, nameBuf, bases);
    if(!pyType)
        return NULL;

    PyTypeObject_setUAType((PyTypeObject *)pyType, bindType);
    registerCustomPyType(bindType, (PyTypeObject *)pyType, nameBuf);
    return pyType;
}

PyObject *
createCustomPyTypeWithBases(const UA_DataType *uaType, const char *namespaceName, PyObject *bases) {
    return createCustomPyTypeBound(uaType, uaType, namespaceName, bases);
}

PyObject *
createCustomPyType(const UA_DataType *uaType, const char *namespaceName) {
    /* Backwards-compatible entry point used by the prebuilt-namespace
     * loader and the parser: those paths always build top-level types
     * that don't need explicit Python bases.  For inheritance-aware
     * use (the @o6.datatype decorator), call
     * createCustomPyTypeWithBases() directly. */
    return createCustomPyTypeWithBases(uaType, namespaceName, NULL);
}
