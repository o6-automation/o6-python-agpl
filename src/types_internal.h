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

#ifndef TYPES_INTERNAL_H_
#define TYPES_INTERNAL_H_

#include "module.h"
#include "bootstrap_ns0_types.h"

/* This header should only be included by .c files with the types_ prefix.
 * This keeps the internal dependencies clean. */

/* Global variables */
extern PyObject *UUIDClass;
extern PyObject *UUIDModule;
extern PyObject *enumModule;
extern PyObject *enumMetaClass;

PyObject * PY_encodeBinary(PyObject *_, PyObject *obj);
PyObject * PY_decodeBinary(PyObject *_, PyObject *obj);
PyObject * PY_encodeXml(PyObject *_, PyObject *obj);
PyObject * PY_decodeXml(PyObject *_, PyObject *args);
PyObject * PY_decodeXmlValue(PyObject *_, PyObject *args);
PyObject * PY_encodeXmlValue(PyObject *_, PyObject *args);
PyObject * PY_encodeJson(PyObject *_, PyObject *obj);
PyObject * PY_decodeJson(PyObject *_, PyObject *obj);

/* Datatype metadata belongs to the type dictionary, never a protocol slot.
 * The capsule borrows the UA_DataType, whose lifetime is managed by the
 * datatype registry. Only this type's own dictionary is consulted here;
 * PY2UAType handles inheritance. */
#define PyUA_DATATYPE_CAPSULE "o6.UA_DataType"
#define PyUA_DATATYPE_ATTRIBUTE "_ua_datatype"

static inline int
PyTypeObject_setUAType(PyTypeObject *t, const UA_DataType *ua) {
    PyObject *capsule = PyCapsule_New((void *)ua, PyUA_DATATYPE_CAPSULE, NULL);
    if(!capsule)
        return -1;
    int result = PyDict_SetItemString(t->tp_dict, PyUA_DATATYPE_ATTRIBUTE, capsule);
    Py_DECREF(capsule);
    if(result == 0)
        PyType_Modified(t);
    return result;
}

static inline const UA_DataType *
PyTypeObject_getUAType(PyTypeObject *t) {
    if(!t->tp_dict)
        return NULL;
    PyObject *capsule = PyDict_GetItemString(t->tp_dict, PyUA_DATATYPE_ATTRIBUTE);
    if(!capsule || !PyCapsule_IsValid(capsule, PyUA_DATATYPE_CAPSULE))
        return NULL;
    return (const UA_DataType *)PyCapsule_GetPointer(capsule, PyUA_DATATYPE_CAPSULE);
}

/* Registry of dynamically created custom Python types, used by
 * UA2PYType() to resolve UA_DataType* -> PyTypeObject* for types
 * registered at runtime (e.g. from NodeSet2 XML).  The backing store is
 * private to types.c.  See type_registration.c for the
 * ``registerCustomPyType`` atomicity contract. */
int registerCustomPyType(const UA_DataType *uaType, PyTypeObject *pyType,
                         const char *typeName, bool mayPreemptBuiltin);
PyTypeObject *findCustomPyTypeWithFlag(const UA_DataType *uaType,
                                       bool *mayPreemptBuiltin);
PyTypeObject *findCustomEnumPyType(const UA_DataType *uaType);

/* type_registration.c — shared implementations */

/* py_description_to_eo converts a Python StructureDescription /
 * EnumDescription into a freshly-allocated UA_ExtensionObject for
 * UA_DataType_fromDescription().
 * createCustomPyType builds the Python class for a freshly constructed
 * UA_DataType (``layoutType``) and writes its qualified name to ``nameBuf``.
 * It runs Python code (the enum factory, ``__init_subclass__``, metaclasses)
 * and does not bind the class to any UA_DataType.
 * ``enumFactory`` is the callable the authoring layer chose to realize the
 * members with — ``IntEnum`` for an enumeration, ``IntFlag`` for an OptionSet —
 * and its presence is what decides between an enum class and a struct, not
 * ``layoutType->typeKind``; see the note in its body.  NULL for a struct.
 * ``enumOverrideMembers``, when not NULL, is used as the enum class's
 * ``{name: value}`` dict instead of one built from ``layoutType->members`` —
 * see ``register_enumeration_type`` in ``datatypes.c`` for why an oversized
 * enum's own member array can't carry it.
 * bindCustomPyType binds that class to ``bindType`` and registers it in the
 * UA_DataType* -> PyTypeObject index under ``name``.  It runs no Python code,
 * so ``build_one_type`` can bind and publish a chain slot in one step.
 * ``fromEnumFactory`` is whether the class came from an enum factory.
 * Returns 0 on success, -1 with a Python exception set. */
UA_StatusCode py_description_to_eo(PyObject *py_descr, UA_ExtensionObject *eo);
PyObject *createCustomPyType(const UA_DataType *layoutType,
                             const char *namespaceName,
                             PyObject *bases,
                             PyObject *enumFactory,
                             PyObject *enumOverrideMembers,
                             char *nameBuf, size_t nameBufSize);
int bindCustomPyType(PyObject *pyType, const UA_DataType *bindType,
                     const char *name, bool fromEnumFactory);

/* UA_TYPES[i] -> PyTypeObject* table (builtins by typeKind, plus the six
 * NS0 bootstrap struct types populated by create_bootstrap_struct_types). */
extern PyTypeObject * pyUATypes[UA_TYPES_COUNT];

extern PyTypeObject * pyUADateTime;
extern PyTypeObject * pyUAStatusCode;
extern PyTypeObject * pyUANodeId;
extern PyTypeObject * pyUAExpandedNodeId;
extern PyTypeObject * pyUAExtensionObject;
extern PyTypeObject * pyUAQualifiedName;
extern PyTypeObject * pyUALocalizedText;
extern PyTypeObject * pyUADataValue;
extern PyTypeObject * pyUADiagnosticInfo;

// Builtin UA values are stored directly in the PyObject
typedef struct {
    PyObject_HEAD
    union {
        UA_DateTime dateTime;
        UA_StatusCode statusCode;
        UA_NodeId nodeId;
        UA_ExpandedNodeId expandedNodeId;
        UA_QualifiedName qualifiedName;
        UA_LocalizedText localizedText;

        // Only used for values that are not decoded.
        // Otherwise the value is unboxed automatically.
        UA_ExtensionObject eo;
    };
} PyUABuiltin;

// Lower-case the first character of an OPC UA member name.
// "StartingBitPosition" -> "startingBitPosition"
// out must be a buf of at least 128 bytes.
static inline void lcFirst(const char *name, char *out) {
    if(!name || !name[0]) { out[0] = 0; return; }
    size_t len = strlen(name);
    if(len >= 128) len = 127;
    memcpy(out, name, len);
    out[len] = 0;
    out[0] = (char)tolower((unsigned char)out[0]);
}

// The Python attribute name of member `index`
void memberPyName(PyTypeObject *pyType, const UA_DataType *uaType, size_t index, char *out);

// The first value access converts the native Variant into a cached PyObject
// and then clears the Variant. `converting` counts the reads converting it
// right now: the Variant is cleared only once no read converts it any more
// (see types_datavalue.c).
typedef struct {
    PyObject_HEAD
    UA_DataValue dv;
    PyObject *value;
    size_t converting;
} PyUADataValue;

// DiagnosticInfo is a struct-like builtin; members are exposed via getset
// and the has* bitfields of the underlying UA_DiagnosticInfo.
typedef struct {
    PyObject_HEAD
    UA_DiagnosticInfo di;
} PyUADiagnosticInfo;

// Structures keep converted or assigned members in a dict and the members
// still in native form in `data`. The first read of a member converts it
// into the dict and then releases it from `data` (see types_struct.c).
typedef struct {
    // define PyObject_HEAD
    // Py_ssize_t ob_refcnt;
    // struct _typeobject *ob_type;
    PyObject_HEAD
    PyObject *dict; // For dynamic structures

    // Buffer to keep the C struct.
    // Fill up to 512 (8 cache lines)
    // This fits perfectly the biggest struct in ns0 has memsize 488
    char data[512 - sizeof(PyObject*) - sizeof(Py_ssize_t) - sizeof(struct _typeobject*)];
} PyUAStruct;

// Which UA datatype does a python object map to?
typedef enum {
    PYVALUEDIMENSION_SCALAR = 0,
    PYVALUEDIMENSION_ARRAY,  // (flat) python sequence
    PYVALUEDIMENSION_NDARRAY // numpy array
} PyValueDimension;

typedef struct {
    PyValueDimension dimension;
    const UA_DataType *uaType;
} PyUATypeMatch;

// uaType is NULL if the type cannot be uniquely converted.
// The conversion can still fail later on.
PyUATypeMatch PY2UAMatch(PyObject *o);

const UA_DataType * PY2UAType(PyTypeObject *t);
PyTypeObject * UA2PYType(const UA_DataType *t);
int UA2NPType(const UA_DataType *t);

/* Common utility functions */
UA_StatusCode Unicode2String(PyObject *o, UA_String *s);
bool listContains(PyObject *list, PyObject *o);
PyObject *pyUA_repr(PyObject *self);
PyObject *pyUA_reprQuoted(PyObject *self);
PyObject *pyNodeId_str(PyObject *self);
PyObject *pyExpandedNodeId_str(PyObject *self);
PyObject *pyNodeId_repr(PyObject *self);
PyObject *pyQualifiedName_str(PyObject *self);
PyObject *pyQualifiedName_repr(PyObject *self);
PyObject *pyUA_deepcopy(PyObject *self, PyObject *memo);

/* Conversion functions */
PyObject * UA2PY_guid(UA_Guid *guid);

/* Specialized conversion functions */
PyObject * PY2UA_datetime(PyObject *obj, UA_DateTime *p);
PyObject * PY2UA_guid(PyObject *obj, UA_Guid *p);
PyObject * PY2UA_statuscode(PyObject *obj, UA_StatusCode *p);
PyObject * PY2UA_nodeid(PyObject *obj, UA_NodeId *p);
PyObject * PY2UA_expandednodeid(PyObject *obj, UA_ExpandedNodeId *p);
PyObject * PY2UA_qualifiedname(PyObject *obj, UA_QualifiedName *p);
PyObject * PY2UA_localizedtext(PyObject *obj, UA_LocalizedText *p);
PyObject * PY2UA_extensionobject(PyObject *obj, UA_ExtensionObject *p);
PyObject * PY2UA_variant(PyObject *obj, UA_Variant *p);
PyObject * PY2UA_datavalue(PyObject *obj, UA_DataValue *p,
                           const UA_NamespaceMapping *nsMapping,
                           const UA_DataTypeArray *customDataTypes);

/* Builtin type functions */
PyObject *pyUABuiltin_str(PyObject *self);
void pyUABuiltin_dealloc(PyObject *self);
PyObject *pyUABuiltin_richcompare(PyObject *self, PyObject *other, int op);

/* DateTime functions */
int pyDateTime_init(PyObject *self, PyObject *args, PyObject *kwds);
PyObject *pyDateTime_richcompare(PyObject *self, PyObject *other, int op);
PyObject *pyDateTime_int(PyObject *self);

/* NodeId functions */
int pyNodeId_init(PyObject *self, PyObject *args, PyObject *kwds);
PyObject *pyNodeId_get_ns(PyObject *self, void *closure);
PyObject *pyNodeId_get_id(PyObject *self, void *closure);
PyObject *_pyNodeId_get_id(UA_NodeId *id);
Py_hash_t pyNodeId_hash(PyObject *self);
extern PyGetSetDef pyNodeId_getsets[];

/* ExpandedNodeId functions */
int pyExpandedNodeId_init(PyObject *self, PyObject *args, PyObject *kwds);
PyObject *pyExpandedNodeId_get_ns(PyObject *self, void *closure);
PyObject *pyExpandedNodeId_get_id(PyObject *self, void *closure);
PyObject *pyExpandedNodeId_get_uri(PyObject *self, void *closure);
PyObject *pyExpandedNodeId_get_svr(PyObject *self, void *closure);
Py_hash_t pyExpandedNodeId_hash(PyObject *self);
extern PyGetSetDef pyExpandedNodeId_getsets[];

/* ExtensionObject functions */
int pyExtensionObject_init(PyObject *self, PyObject *args, PyObject *kwds);
PyObject * pyUAExtensionObject_str(PyObject *self);
PyObject * pyUAExtensionObject_repr(PyObject *self);
PyObject *pyExtensionObject_get_typeId(PyObject *self, void *closure);
PyObject *pyExtensionObject_get_body(PyObject *self, void *closure);
extern PyGetSetDef pyExtensionObject_getsets[];

/* QualifiedName functions */
int pyQualifiedName_init(PyObject *self, PyObject *args, PyObject *kwds);
Py_hash_t pyQualifiedName_hash(PyObject *self);
PyObject *pyQualifiedName_get_ns(PyObject *self, void *closure);
PyObject *pyQualifiedName_get_name(PyObject *self, void *closure);
extern PyGetSetDef pyQualifiedName_getsets[];

/* LocalizedText functions */
int pyLocalizedText_init(PyObject *self, PyObject *args, PyObject *kwds);
PyObject *pyLocalizedText_get_locale(PyObject *self, void *closure);
PyObject *pyLocalizedText_get_text(PyObject *self, void *closure);
int pyLocalizedText_set_locale(PyObject *self, PyObject *value, void *closure);
int pyLocalizedText_set_text(PyObject *self, PyObject *value, void *closure);
extern PyGetSetDef pyLocalizedText_getsets[];

/* DataValue functions */
int pyUADataValue_init(PyObject *self, PyObject *args, PyObject *kwds);
int pyUADataValue_clear(PyObject *self);
PyObject *pyUADataValue_str(PyObject *self);
PyObject *pyUADataValue_repr(PyObject *self);
void pyUADataValue_dealloc(PyObject *self);
int pyUADataValue_traverse(PyObject *self, visitproc visit, void *arg);
extern PyGetSetDef pyUADataValue_getsets[];

/* DiagnosticInfo functions */
int pyUADiagnosticInfo_init(PyObject *self, PyObject *args, PyObject *kwds);
int pyUADiagnosticInfo_clear(PyObject *self);
PyObject *pyUADiagnosticInfo_str(PyObject *self);
PyObject *pyUADiagnosticInfo_repr(PyObject *self);
PyObject *pyUADiagnosticInfo_richcompare(PyObject *self, PyObject *other, int op);
void pyUADiagnosticInfo_dealloc(PyObject *self);
int pyUADiagnosticInfo_traverse(PyObject *self, visitproc visit, void *arg);
extern PyGetSetDef pyUADiagnosticInfo_getsets[];
PyObject *PY2UA_diagnosticinfo(PyObject *obj, UA_DiagnosticInfo *p);

/* Structure functions */
int pyUAStruct_traverse(PyObject *self, visitproc visit, void *arg);
int pyUAStruct_clear(PyObject *self);
PyObject *pyUAStruct_str(PyObject *self);
PyObject *pyUAStruct_repr(PyObject *self);
void pyUAStruct_dealloc(PyObject *self);
PyObject *pyUAStruct_dir(PyObject *self, PyObject *Py_UNUSED(ignored));
int pyUAStruct_setattro(PyObject *self, PyObject *name, PyObject *value);
PyObject *pyUAStruct_getattro(PyObject *self, PyObject *name);
PyObject *pyUAStruct_copy(PyObject *self, PyObject *Py_UNUSED(ignored));


/* EventFilter generator function & Json Config Parser */
#ifdef UA_ENABLE_JSON_ENCODING
PyObject * pyJson5_parse(PyObject *self, PyObject *arg);
#ifdef UA_ENABLE_SUBSCRIPTIONS_EVENTS
PyObject * pyEventFilter_parse(PyObject *self, PyObject *args, PyObject *kwds);
#endif
#endif

/* Conversion function helpers */
PyObject *PY2UA_uint(PyObject *obj, void *p, const UA_DataType *type);
PyObject *PY2UA_int(PyObject *obj, void *p, const UA_DataType *type);
PyObject *PY2UA_float(PyObject *obj, void *p, const UA_DataType *type);
PyObject *PY2UA_structure(PyObject *obj, void *p, const UA_DataType *type);
PyObject *PY2UA_structure_array(PyObject *obj, void *arrayPtr, const UA_DataType *type);

/* NumPy array functions */
int np_setitem(PyObject *item, void *data, void *arr);

/* Module definitions */
extern struct PyModuleDef types_module;
void types_free(void*);

#endif // PYO6_TYPES_INTERNAL_H_
