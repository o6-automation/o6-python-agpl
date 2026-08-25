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
// Used consulted by UA2PYType() (via findCustomPyTypeWithFlag) so that a decorated @o6.datatype / @o6.enumtype class wins over the plain C-generated PyType.
//
// A growable array plus a pointer-keyed index over it (below):
// nothing holds a pointer to an individual entry (the lookups return the PyType, not the entry),
// so the backing buffer is free to move on realloc.
typedef struct CustomPyType {
    const UA_DataType *uaType;
    PyTypeObject *pyType;
    // True iff this registration may pre-empt a builtin typeKind in UA2PYType.
    // Computed by the caller as `builtFromEnumDescription && bindType->typeKind != ENUM`.
    bool mayPreemptBuiltin;
    char typeName[128]; // Owned name buffer for PyType_Spec
} CustomPyType;

static CustomPyType *customPyTypes = NULL;
static size_t customPyTypesSize = 0;
static size_t customPyTypesCapacity = 0;

/* Open-addressed `UA_DataType*` -> entry index over `customPyTypes`, holding
 * `index + 1` per slot (0 means empty).  `slotsMask` is `slots - 1`, with
 * `slots` a power of two. */
static size_t *customPyTypeSlots = NULL;
static size_t customPyTypeSlotsMask = 0;

static size_t
customPyTypeHash(const UA_DataType *uaType) {
    /* Multiplicative mix; `UA_DataType`s are array elements, so neighbouring
     * pointers differ only in their low bits and must not be used as-is. */
    uint64_t key = (uint64_t)(uintptr_t)uaType;
    key ^= key >> 33;
    key *= 0xff51afd7ed558ccdULL;
    key ^= key >> 29;
    return (size_t)key;
}

/* Insert one entry, keeping the *first* registration for a duplicated
 * `UA_DataType*` — the linear scan this replaces returned the earliest match. */
static void
customPyTypeSlotsInsert(size_t entry) {
    size_t slot = customPyTypeHash(customPyTypes[entry].uaType) & customPyTypeSlotsMask;
    for(;;) {
        size_t held = customPyTypeSlots[slot];
        if(held == 0) {
            customPyTypeSlots[slot] = entry + 1;
            return;
        }
        if(customPyTypes[held - 1].uaType == customPyTypes[entry].uaType)
            return;  /* already indexed by an earlier registration */
        slot = (slot + 1) & customPyTypeSlotsMask;
    }
}

/* Grow the index to `slots` and re-insert every entry.  Returns 0 on success. */
static int
customPyTypeSlotsRebuild(size_t slots) {
    size_t *grown = (size_t*)calloc(slots, sizeof(size_t));
    if(!grown)
        return -1;
    free(customPyTypeSlots);
    customPyTypeSlots = grown;
    customPyTypeSlotsMask = slots - 1;
    for(size_t i = 0; i < customPyTypesSize; i++)
        customPyTypeSlotsInsert(i);
    return 0;
}

/* Register a UA_DataType -> PyTypeObject mapping.
 * Returns 0 on success, -1 with a Python exception set on failure.
 * Atomic: a failed grow or rebuild leaves no half-written state behind. */
int
registerCustomPyType(const UA_DataType *uaType, PyTypeObject *pyType,
                     const char *typeName, bool mayPreemptBuiltin) {
    if(customPyTypesSize == customPyTypesCapacity) {
        size_t new_cap = customPyTypesCapacity ? customPyTypesCapacity * 2 : 1024;
        CustomPyType *grown =
            (CustomPyType*)realloc(customPyTypes, new_cap * sizeof(CustomPyType));
        if(!grown) {
            PyErr_NoMemory();
            return -1;
        }
        customPyTypes = grown;
        customPyTypesCapacity = new_cap;
    }

    /* Bump the size together with the write so the load-factor check and
     * rebuild below see the new entry. */
    size_t entry = customPyTypesSize;
    customPyTypes[entry].uaType = uaType;
    Py_INCREF(pyType);
    customPyTypes[entry].pyType = pyType;
    customPyTypes[entry].mayPreemptBuiltin = mayPreemptBuiltin;
    snprintf(customPyTypes[entry].typeName,
             sizeof(customPyTypes[entry].typeName), "%s", typeName);
    customPyTypesSize = entry + 1;

    /* Keep the load factor at or below 1/2 so probe chains stay short. */
    if(customPyTypesSize * 2 > customPyTypeSlotsMask + 1) {
        size_t slots = customPyTypeSlotsMask ? (customPyTypeSlotsMask + 1) * 2 : 4096;
        if(customPyTypeSlotsRebuild(slots) < 0) {
            /* The rebuild failed before swapping the slot array, so the
             * prior index is intact.  Just drop the half-written entry. */
            Py_DECREF(pyType);
            memset(&customPyTypes[entry], 0, sizeof(CustomPyType));
            customPyTypesSize = entry;
            PyErr_NoMemory();
            return -1;
        }
        return 0;
    }
    customPyTypeSlotsInsert(entry);
    return 0;
}

static const CustomPyType *
lookupCustomPyType(const UA_DataType *uaType) {
    if(!customPyTypeSlots)
        return NULL;
    size_t slot = customPyTypeHash(uaType) & customPyTypeSlotsMask;
    for(;;) {
        size_t held = customPyTypeSlots[slot];
        if(held == 0)
            return NULL;
        if(customPyTypes[held - 1].uaType == uaType)
            return &customPyTypes[held - 1];
        slot = (slot + 1) & customPyTypeSlotsMask;
    }
}

PyTypeObject *
findCustomPyTypeWithFlag(const UA_DataType *uaType, bool *mayPreemptBuiltin) {
    const CustomPyType *entry = lookupCustomPyType(uaType);
    if(!entry)
        return NULL;
    if(mayPreemptBuiltin)
        *mayPreemptBuiltin = entry->mayPreemptBuiltin;
    return entry->pyType;
}

PyTypeObject *
findCustomEnumPyType(const UA_DataType *uaType) {
    // Thin wrapper for the integer-conversion hook in src/types_convert.c.
    bool mayPreemptBuiltin = false;
    PyTypeObject *pyType = findCustomPyTypeWithFlag(uaType, &mayPreemptBuiltin);
    return mayPreemptBuiltin ? pyType : NULL;
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
                        const char *namespaceName, PyObject *bases,
                        bool builtFromEnumDescription) {
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

    /* ``builtFromEnumDescription`` decides between ``IntFlag`` and struct
     * — *not* ``layoutType->typeKind``, which the OptionSet compensation
     * in ``src/datatypes.c`` overwrites before we get here.  Looks wrong;
     * is not — the layout's members, member-size and type name are still
     * correct; the class builder touches only the member array, its size
     * and the type name. */
    PyObject *pyType = builtFromEnumDescription
        ? buildEnumPyType(layoutType, shortName, bases)
        : buildStructPyType(layoutType, nameBuf, bases);
    if(!pyType)
        return NULL;

    bool mayPreemptBuiltin = builtFromEnumDescription &&
        bindType->typeKind != UA_DATATYPEKIND_ENUM;

    PyTypeObject_setUAType((PyTypeObject *)pyType, bindType);
    if(registerCustomPyType(bindType, (PyTypeObject *)pyType, nameBuf,
                            mayPreemptBuiltin) < 0) {
        Py_DECREF(pyType);
        return NULL;
    }
    return pyType;
}
