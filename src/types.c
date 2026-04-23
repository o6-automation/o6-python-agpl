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

#include <open62541/types.h>
#define NO_IMPORT_ARRAY
#include "types_internal.h"
#include <numpy/arrayobject.h>
#include <numpy/arrayscalars.h>
#include <numpy/ndarraytypes.h>

// For the struct types we store a pointer to UA_DataType inside the
// PyTypeObject. The tp_as_async slot is not used as __await__, __aiter__ and
// __anext__ are not defined for the type. Subtyping (Py_TPFLAGS_BASETYPE) is allowed.
// PyUA_TPFLAGS_ISUADATATYPE, PyTypeObject_setUAType, PyTypeObject_getUAType
// are defined in types_internal.h

/* Global linked list head for custom (runtime-registered) Python types */
static CustomPyType *customPyTypes = NULL;

void
registerCustomPyType(const UA_DataType *uaType, PyTypeObject *pyType,
                     const char *typeName) {
    CustomPyType *entry = (CustomPyType*)malloc(sizeof(CustomPyType));
    if(!entry)
        return;
    entry->uaType = uaType;
    entry->pyType = pyType;
    snprintf(entry->typeName, sizeof(entry->typeName), "%s", typeName);
    entry->next = customPyTypes;
    customPyTypes = entry;
}

PyTypeObject *
findCustomPyType(const UA_DataType *uaType) {
    for(CustomPyType *cur = customPyTypes; cur; cur = cur->next) {
        if(cur->uaType == uaType)
            return cur->pyType;
    }
    return NULL;
}

PyTypeObject * pyUATypes[UA_TYPES_COUNT];
static char pyTypeNames[UA_TYPES_COUNT][64];

// Not all of the following get properly initialized.
// Access only via the type->typeKind switch.
PyTypeObject pyUABuiltinTypes[UA_DATATYPEKIND_DIAGNOSTICINFO + 1];

#define NS0STACKTYPE(X) pyUABuiltinTypes[UA_TYPES_##X]
#define NS0TYPE(X) pyUATypes[UA_TYPES_##X]

PyTypeObject * pyUADateTime;
PyTypeObject * pyUAStatusCode;
PyTypeObject * pyUANodeId;
PyTypeObject * pyUAExpandedNodeId;
PyTypeObject * pyUAExtensionObject;
PyTypeObject * pyUAQualifiedName;
PyTypeObject * pyUALocalizedText;
PyTypeObject * pyUADataValue;

void types_free(void*) {
    Py_XDECREF(UUIDModule);
    Py_XDECREF(UUIDClass);
}

static const UA_DataType *
NP2UAType(int dtype) {
    switch(dtype) {
    case NPY_BOOL: return &UA_TYPES[UA_TYPES_BOOLEAN];
    case NPY_INT8: return &UA_TYPES[UA_TYPES_SBYTE];
    case NPY_UINT8: return &UA_TYPES[UA_TYPES_BYTE];
    case NPY_INT16: return &UA_TYPES[UA_TYPES_INT16];
    case NPY_UINT16: return &UA_TYPES[UA_TYPES_UINT16];
    case NPY_INT32: return &UA_TYPES[UA_TYPES_INT32];
    case NPY_UINT32: return &UA_TYPES[UA_TYPES_UINT32];
    case NPY_INT64: return &UA_TYPES[UA_TYPES_INT64];
    case NPY_UINT64: return &UA_TYPES[UA_TYPES_UINT64];
    case NPY_FLOAT32: return &UA_TYPES[UA_DATATYPEKIND_FLOAT];
    case NPY_FLOAT64: return &UA_TYPES[UA_DATATYPEKIND_DOUBLE];
    case NPY_VSTRING: return &UA_TYPES[UA_DATATYPEKIND_STRING];
    default:
        return NULL;
    }
}

int
UA2NPType(const UA_DataType *t) {
    switch(t->typeKind) {
    case UA_DATATYPEKIND_BOOLEAN: return NPY_BOOL;
    case UA_DATATYPEKIND_SBYTE: return NPY_INT8;
    case UA_DATATYPEKIND_BYTE: return NPY_UINT8;
    case UA_DATATYPEKIND_INT16: return NPY_INT16;
    case UA_DATATYPEKIND_UINT16: return NPY_UINT16;
    case UA_DATATYPEKIND_INT32: return NPY_INT32;
    case UA_DATATYPEKIND_UINT32: return NPY_UINT32;
    case UA_DATATYPEKIND_INT64: return NPY_INT64;
    case UA_DATATYPEKIND_UINT64: return NPY_UINT64;
    case UA_DATATYPEKIND_FLOAT: return NPY_FLOAT32;
    case UA_DATATYPEKIND_DOUBLE: return NPY_FLOAT64;
    default: return NPY_OBJECT;
    }
}

PyUATypeMatch
PY2UAMatch(PyObject *obj) {
    PyUATypeMatch out = {0};

    // Numpy array
    if(PyArray_Check(obj)) {
        out.dimension = PYVALUEDIMENSION_NDARRAY;

        // Get the type from the ndtype
        PyArrayObject *arr = (PyArrayObject*) obj;
        PyArray_Descr *descr = PyArray_DESCR(arr);
        out.uaType = NP2UAType(descr->type_num);
        if(out.uaType)
            return out;

        // If the type is not recognized, it must be object
        if(PyArray_TYPE(arr) != NPY_OBJECT)
            return out;

        // Get the type from the first member
        if(PyArray_SIZE(arr) == 0)
            return out;
        PyObject **data = (PyObject **)PyArray_DATA(arr);
        PyObject *first = data[0];
        out.uaType = PY2UAType(Py_TYPE(first));
        return out;
    }

    // Sequence
    if(PySequence_Check(obj) && !PyUnicode_Check(obj) && !PyBytes_Check(obj)) {
        out.dimension = PYVALUEDIMENSION_ARRAY;

        // At least one member needed to identify the type
        Py_ssize_t len = PySequence_Length(obj);
        if(len <= 0)
            return out;

        // Get the type from the first member
        PyObject *first = PySequence_GetItem(obj, 0);
        if(!first)
            return out;
        out.uaType = PY2UAType(Py_TYPE(first));
        Py_DECREF(first);
        return out;
    }

    // Scalar
    out.uaType = PY2UAType(Py_TYPE(obj));
    return out;
}

const UA_DataType *
PY2UAType(PyTypeObject *t) {
    // Check for a builtin type
    for(size_t i = 0; i <= UA_DATATYPEKIND_XMLELEMENT; i++) {
        if(t == pyUATypes[i])
            return &UA_TYPES[i];
    }

    // Special case for Boolean, as we use numpy.bool internally
    if(t == &PyBool_Type)
        return &UA_TYPES[UA_TYPES_BOOLEAN];

    // Python int -> int32
    if(t == &PyLong_Type)
        return &UA_TYPES[UA_TYPES_INT32];

    // Python float -> float32
    if(t == &PyFloat_Type)
        return &UA_TYPES[UA_TYPES_FLOAT];

    // Walk the MRO so that Python subclasses of C struct types also resolve.
    for(PyTypeObject *cur = t; cur != NULL; cur = cur->tp_base) {
        // The type has a pointer to UA_DataType baked in
        const UA_DataType *ua = PyTypeObject_getUAType(cur);
        if(ua)
            return ua;
    }

    return NULL;
}

PyTypeObject * UA2PYType(const UA_DataType *t) {
    switch(t->typeKind) {
    case UA_DATATYPEKIND_BOOLEAN:
    case UA_DATATYPEKIND_SBYTE:
    case UA_DATATYPEKIND_BYTE:
    case UA_DATATYPEKIND_INT16:
    case UA_DATATYPEKIND_UINT16:
    case UA_DATATYPEKIND_INT32:
    case UA_DATATYPEKIND_UINT32:
    case UA_DATATYPEKIND_INT64:
    case UA_DATATYPEKIND_UINT64:
    case UA_DATATYPEKIND_FLOAT:
    case UA_DATATYPEKIND_DOUBLE:
    case UA_DATATYPEKIND_STRING:
    case UA_DATATYPEKIND_DATETIME:
    case UA_DATATYPEKIND_GUID:
    case UA_DATATYPEKIND_BYTESTRING:
    case UA_DATATYPEKIND_XMLELEMENT:
    case UA_DATATYPEKIND_NODEID:
    case UA_DATATYPEKIND_EXPANDEDNODEID:
    case UA_DATATYPEKIND_STATUSCODE:
    case UA_DATATYPEKIND_QUALIFIEDNAME:
    case UA_DATATYPEKIND_LOCALIZEDTEXT:
    case UA_DATATYPEKIND_EXTENSIONOBJECT:
    case UA_DATATYPEKIND_DATAVALUE:
        return pyUATypes[t->typeKind];
    case UA_DATATYPEKIND_VARIANT:
        return NULL;
    case UA_DATATYPEKIND_STRUCTURE:
    case UA_DATATYPEKIND_OPTSTRUCT:
    case UA_DATATYPEKIND_ENUM:
        break;
    case UA_DATATYPEKIND_DIAGNOSTICINFO:
    case UA_DATATYPEKIND_DECIMAL:
    case UA_DATATYPEKIND_UNION:
    case UA_DATATYPEKIND_BITFIELDCLUSTER:
    default:
        return NULL;
    }

    // All ns0-types above the builtin types are heap-allocated
    for(size_t i = UA_DATATYPEKIND_DIAGNOSTICINFO + 1; i < UA_TYPES_COUNT; i++) {
      if(!pyUATypes[i])
          continue;
      if(PyTypeObject_getUAType(pyUATypes[i]) == t)
          return pyUATypes[i];
    }

    // Check custom (runtime-registered) types
    PyTypeObject *custom = findCustomPyType(t);
    if(custom)
        return custom;

    return NULL;
}

/* Parse a string into a RelativePath object using UA_RelativePath_parse from open62541 */
static PyObject *
_parseRelativePath(PyObject *self, PyObject *args) {
    const char *path_str = NULL;
    if (!PyArg_ParseTuple(args, "s", &path_str)) {
        return NULL;
    }

    UA_String input = UA_STRING((char*)(uintptr_t)path_str);
    UA_RelativePath relativePath;
    UA_StatusCode res = UA_RelativePath_parse(&relativePath, input);
    if(res != UA_STATUSCODE_GOOD) {
        PyErr_SetString(PyExc_ValueError, "Failed to parse RelativePath string");
        return NULL;
    }

    PyObject *out = UA2PY(&relativePath, &UA_TYPES[UA_TYPES_RELATIVEPATH]);
    UA_RelativePath_clear(&relativePath);
    return out;
}

static PyObject *
_printRelativePath(PyObject *self, PyObject *args) {
    PyObject *py_rp;
    if (!PyArg_ParseTuple(args, "O", &py_rp))
        return NULL;
    UA_RelativePath rp;
    if (!PY2UA(py_rp, &rp, &UA_TYPES[UA_TYPES_RELATIVEPATH]))
        return NULL;
    UA_String out = UA_STRING_NULL;
    UA_StatusCode res = UA_RelativePath_print(&rp, &out);
    if(res != UA_STATUSCODE_GOOD) {
        PyErr_SetString(PyExc_ValueError, "Failed to print RelativePath");
        return NULL;
    }
    PyObject *py_str = PyUnicode_FromStringAndSize((const char*)out.data, out.length);
    UA_String_clear(&out);
    return py_str;
}

/* Parse a string into a SimpleAttributeOperand object using UA_SimpleAttributeOperand_parse from open62541 */
static PyObject *
_parseSimpleAttributeOperand(PyObject *self, PyObject *args) {
    const char *sao_str = NULL;
    if (!PyArg_ParseTuple(args, "s", &sao_str)) {
        return NULL;
    }

    UA_String input = UA_STRING((char*)(uintptr_t)sao_str);
    UA_SimpleAttributeOperand sao;
    UA_StatusCode res = UA_SimpleAttributeOperand_parse(&sao, input);
    if(res != UA_STATUSCODE_GOOD) {
        PyErr_SetString(PyExc_ValueError, "Failed to parse SimpleAttributeOperand string");
        return NULL;
    }

    PyObject *out = UA2PY(&sao, &UA_TYPES[UA_TYPES_SIMPLEATTRIBUTEOPERAND]);
    UA_SimpleAttributeOperand_clear(&sao);
    return out;
}

static PyObject *
_printSimpleAttributeOperand(PyObject *self, PyObject *args) {
    PyObject *py_sao;
    if (!PyArg_ParseTuple(args, "O", &py_sao))
        return NULL;
    UA_SimpleAttributeOperand sao;
    if (!PY2UA(py_sao, &sao, &UA_TYPES[UA_TYPES_SIMPLEATTRIBUTEOPERAND]))
        return NULL;
    UA_String out = UA_STRING_NULL;
    UA_StatusCode res = UA_SimpleAttributeOperand_print(&sao, &out);
    if(res != UA_STATUSCODE_GOOD) {
        PyErr_SetString(PyExc_ValueError, "Failed to print SimpleAttributeOperand");
        return NULL;
    }
    PyObject *py_str = PyUnicode_FromStringAndSize((const char*)out.data, out.length);
    UA_String_clear(&out);
    return py_str;
}

/* Parse a string into a ReadValueId object using UA_ReadValueId_parse from open62541 */
static PyObject *
_parseReadValueId(PyObject *self, PyObject *args) {
    const char *rvi_str = NULL;
    if (!PyArg_ParseTuple(args, "s", &rvi_str)) {
        return NULL;
    }

    UA_String input = UA_STRING((char*)(uintptr_t)rvi_str);
    UA_ReadValueId rvi;
    UA_StatusCode res = UA_ReadValueId_parse(&rvi, input);
    if(res != UA_STATUSCODE_GOOD) {
        PyErr_SetString(PyExc_ValueError, "Failed to parse ReadValueId string");
        return NULL;
    }

    PyObject *out = UA2PY(&rvi, &UA_TYPES[UA_TYPES_READVALUEID]);
    UA_ReadValueId_clear(&rvi);
    return out;
}

static PyObject *
_printReadValueId(PyObject *self, PyObject *args) {
    PyObject *py_rvi;
    if (!PyArg_ParseTuple(args, "O", &py_rvi))
        return NULL;
    UA_ReadValueId rvi;
    if (!PY2UA(py_rvi, &rvi, &UA_TYPES[UA_TYPES_READVALUEID]))
        return NULL;
    UA_String out = UA_STRING_NULL;
    UA_StatusCode res = UA_ReadValueId_print(&rvi, &out);
    if(res != UA_STATUSCODE_GOOD) {
        PyErr_SetString(PyExc_ValueError, "Failed to print ReadValueId");
        return NULL;
    }
    PyObject *py_str = PyUnicode_FromStringAndSize((const char*)out.data, out.length);
    UA_String_clear(&out);
    return py_str;
}

static PyMethodDef types_methods[] = {
    {"encodeBinary", PY_encodeBinary, METH_O, "Encode an object as binary"},
    {"decodeBinary", PY_decodeBinary, METH_VARARGS, "Decode an object as binary"},
    {"encodeJSON", PY_encodeJson, METH_O, "Encode an object as JSON"},
    {"decodeJSON", PY_decodeJson, METH_VARARGS, "Decode an object as JSON"},
    {"_parseRelativePath", _parseRelativePath, METH_VARARGS, "Parse a string into a RelativePath object using UA_RelativePath_parse."},
    {"_parseSimpleAttributeOperand", _parseSimpleAttributeOperand, METH_VARARGS, "Parse a string into a SimpleAttributeOperand object using UA_SimpleAttributeOperand_parse (if available)."},
    {"_parseReadValueId", _parseReadValueId, METH_VARARGS, "Parse a string into a ReadValueId object using UA_ReadValueId_parse."},
    {"_printSimpleAttributeOperand", _printSimpleAttributeOperand, METH_VARARGS, "Print a SimpleAttributeOperand object using UA_SimpleAttributeOperand_print."},
    {"_printRelativePath", _printRelativePath, METH_VARARGS, "Print a RelativePath object using UA_RelativePath_print."},
    {"_printReadValueId", _printReadValueId, METH_VARARGS, "Print a ReadValueId object using UA_ReadValueId_print."},
    {NULL, NULL, 0, NULL}  // sentinel
};

struct PyModuleDef types_module = {
    .m_base = PyModuleDef_HEAD_INIT,
    .m_name = "o6._o6.types",
    .m_doc = "OPC UA builtin types",
    .m_size = -1, /* -1 if the module keeps state in global variables */
    .m_methods = types_methods,
    .m_slots = NULL,
    .m_traverse = NULL,
    .m_clear = NULL,
    .m_free = types_free
};

static PyMethodDef pyUA_methods_deepcopy[] = {
    {"__deepcopy__", (PyCFunction)pyUA_deepcopy, METH_O, NULL},
    {NULL, NULL, 0, NULL}
};

PyObject * pyTypesModule() {
    PyObject *m = PyModule_Create(&types_module);
    if(!m)
        goto error;

    /* Boolean (reuse NumPy class) */
    NS0TYPE(BOOLEAN) = &PyBoolArrType_Type;
    if(PyModule_AddObjectRef(m, "Boolean", (PyObject*)&PyBoolArrType_Type) < 0)
        goto error;

    /* SByte (reuse NumPy class) */
    NS0TYPE(SBYTE) = &PyInt8ArrType_Type;
    if(PyModule_AddObjectRef(m, "SByte", (PyObject*)&PyInt8ArrType_Type) < 0)
        goto error;

    /* Byte (reuse NumPy class) */
    NS0TYPE(BYTE) = &PyUInt8ArrType_Type;
    if(PyModule_AddObjectRef(m, "Byte", (PyObject*)&PyUInt8ArrType_Type) < 0)
        goto error;

    /* Int16 (reuse NumPy class) */
    NS0TYPE(INT16) = &PyInt16ArrType_Type;
    if(PyModule_AddObjectRef(m, "Int16", (PyObject*)&PyInt16ArrType_Type) < 0)
        goto error;

    /* UInt16 (reuse NumPy class) */
    NS0TYPE(UINT16) = &PyUInt16ArrType_Type;
    if(PyModule_AddObjectRef(m, "UInt16", (PyObject*)&PyUInt16ArrType_Type) < 0)
        goto error;

    /* Int32 (reuse NumPy class) */
    NS0TYPE(INT32) = &PyInt32ArrType_Type;
    if(PyModule_AddObjectRef(m, "Int32", (PyObject*)&PyInt32ArrType_Type) < 0)
        goto error;

    /* UInt32 (reuse NumPy class) */
    NS0TYPE(UINT32) = &PyUInt32ArrType_Type;
    if(PyModule_AddObjectRef(m, "UInt32", (PyObject*)&PyUInt32ArrType_Type) < 0)
        goto error;

    /* Int64 (reuse NumPy class) */
    NS0TYPE(INT64) = &PyInt64ArrType_Type;
    if(PyModule_AddObjectRef(m, "Int64", (PyObject*)&PyInt64ArrType_Type) < 0)
        goto error;

    /* UInt64 (reuse NumPy class) */
    NS0TYPE(UINT64) = &PyUInt64ArrType_Type;
    if(PyModule_AddObjectRef(m, "UInt64", (PyObject*)&PyUInt64ArrType_Type) < 0)
        goto error;

    /* Float (reuse NumPy class) */
    NS0TYPE(FLOAT) = &PyFloat32ArrType_Type;
    if(PyModule_AddObjectRef(m, "Float", (PyObject*)&PyFloat32ArrType_Type) < 0)
        goto error;

    /* Double (reuse NumPy class) */
    NS0TYPE(DOUBLE) = &PyFloat64ArrType_Type;
    if(PyModule_AddObjectRef(m, "Double", (PyObject*)&PyFloat64ArrType_Type) < 0)
        goto error;

    /* String (reuse Python class) */
    NS0TYPE(STRING) = &PyUnicode_Type;
    if(PyModule_AddObjectRef(m, "String", (PyObject*)&PyUnicode_Type) < 0)
        goto error;

    /* ByteString (reuse Python class) */
    NS0TYPE(BYTESTRING) = &PyBytes_Type;
    if(PyModule_AddObjectRef(m, "ByteString", (PyObject*)&PyBytes_Type) < 0)
        goto error;

    /* XmlElement (reuse Python class) */
    NS0TYPE(XMLELEMENT) = &PyUnicode_Type;
    if(PyModule_AddObjectRef(m, "XmlElement", (PyObject*)&PyUnicode_Type) < 0)
        goto error;

    /* DateTime */
    static PyNumberMethods pyDateTime_as_number = { .nb_int = pyDateTime_int };
    NS0STACKTYPE(DATETIME) = (PyTypeObject) {
        .ob_base = PyVarObject_HEAD_INIT(NULL, 0)
        .tp_name = "o6.DateTime",
        .tp_doc = PyDoc_STR("DateTime (OPC UA builtin type)"),
        .tp_flags = Py_TPFLAGS_DEFAULT,
        .tp_init = pyDateTime_init,
        .tp_richcompare = pyDateTime_richcompare,
        .tp_as_number = &pyDateTime_as_number,
        .tp_basicsize = sizeof(PyUABuiltin),
        .tp_str = pyUABuiltin_str,
        .tp_repr = pyUA_repr,
        .tp_new = PyType_GenericNew,
        .tp_alloc = PyType_GenericAlloc,
        .tp_methods = pyUA_methods_deepcopy,
    };
    if(PyType_Ready(&NS0STACKTYPE(DATETIME)) < 0 ||
       PyModule_AddObjectRef(m, "DateTime", (PyObject*)&NS0STACKTYPE(DATETIME)) < 0)
        goto error;
    PyTypeObject_setUAType(&NS0STACKTYPE(DATETIME), &UA_TYPES[UA_TYPES_DATETIME]);
    pyUATypes[UA_TYPES_DATETIME] = &NS0STACKTYPE(DATETIME);
    pyUADateTime = &NS0STACKTYPE(DATETIME);

    /* Guid (reuse the Python class) */
    UUIDModule = PyImport_ImportModule("uuid");
    if(!UUIDModule)
        goto error;
    UUIDClass = PyObject_GetAttrString(UUIDModule, "UUID");
    if(!UUIDClass)
        goto error;
    NS0TYPE(GUID) = (PyTypeObject*)UUIDClass;
    if(PyModule_AddObjectRef(m, "Guid", UUIDClass) < 0)
        goto error;

    /* NodeId */
    NS0STACKTYPE(NODEID) = (PyTypeObject) {
        .ob_base = PyVarObject_HEAD_INIT(NULL, 0)
        .tp_name = "o6.NodeId",
        .tp_doc = PyDoc_STR("NodeId (OPC UA builtin type)"),
        .tp_flags = Py_TPFLAGS_DEFAULT,
        .tp_init = pyNodeId_init,
        .tp_basicsize = sizeof(PyUABuiltin),
        .tp_getset = pyNodeId_getsets,
        .tp_richcompare = pyUABuiltin_richcompare, // not inherited if tp_hash is non-Null
        .tp_hash = pyNodeId_hash,
        .tp_str = pyUABuiltin_str,
        .tp_repr = pyUA_reprQuoted,
        .tp_new = PyType_GenericNew,
        .tp_dealloc = pyUABuiltin_dealloc,
        .tp_methods = pyUA_methods_deepcopy,
    };
    if(PyType_Ready(&NS0STACKTYPE(NODEID)) < 0 ||
       PyModule_AddObjectRef(m, "NodeId", (PyObject*)&NS0STACKTYPE(NODEID)) < 0)
        goto error;
    PyTypeObject_setUAType(&NS0STACKTYPE(NODEID), &UA_TYPES[UA_TYPES_NODEID]);
    NS0TYPE(NODEID) = &NS0STACKTYPE(NODEID);
    pyUANodeId = &NS0STACKTYPE(NODEID);

    /* ExpandedNodeId */
    NS0STACKTYPE(EXPANDEDNODEID) = (PyTypeObject) {
        .ob_base = PyVarObject_HEAD_INIT(NULL, 0)
        .tp_name = "o6.ExpandedNodeId",
        .tp_doc = PyDoc_STR("ExpandedNodeId (OPC UA builtin type)"),
        .tp_flags = Py_TPFLAGS_DEFAULT,
        .tp_init = pyExpandedNodeId_init,
        .tp_getset = pyExpandedNodeId_getsets,
        .tp_richcompare = pyUABuiltin_richcompare, // not inherited if tp_hash is non-Null
        .tp_hash = pyExpandedNodeId_hash,
        .tp_str = pyUABuiltin_str,
        .tp_repr = pyUA_reprQuoted,
        .tp_basicsize = sizeof(PyUABuiltin),
        .tp_new = PyType_GenericNew,
        .tp_dealloc = pyUABuiltin_dealloc,
        .tp_methods = pyUA_methods_deepcopy,
    };
    if(PyType_Ready(&NS0STACKTYPE(EXPANDEDNODEID)) < 0 ||
       PyModule_AddObjectRef(m, "ExpandedNodeId", (PyObject*)&NS0STACKTYPE(EXPANDEDNODEID)) < 0)
        goto error;
    PyTypeObject_setUAType(&NS0STACKTYPE(EXPANDEDNODEID), &UA_TYPES[UA_TYPES_EXPANDEDNODEID]);
    NS0TYPE(EXPANDEDNODEID) = &NS0STACKTYPE(EXPANDEDNODEID);
    pyUAExpandedNodeId = &NS0STACKTYPE(EXPANDEDNODEID);

    /* StatusCode */
    static PyNumberMethods pyStatusCode_as_number = { .nb_int = pyStatusCode_int };
    NS0STACKTYPE(STATUSCODE) = (PyTypeObject) {
        .ob_base = PyVarObject_HEAD_INIT(NULL, 0)
        .tp_name = "o6.StatusCode",
        .tp_doc = PyDoc_STR("StatusCode (OPC UA builtin type)"),
        .tp_flags = Py_TPFLAGS_DEFAULT,
        .tp_basicsize = sizeof(PyUABuiltin),
        .tp_init = pyStatusCode_init,
        .tp_getset = pyStatusCode_getsets,
        .tp_str = pyUABuiltin_str,
        .tp_repr = pyStatusCode_repr,
        .tp_richcompare = pyUABuiltin_richcompare,
        .tp_as_number = &pyStatusCode_as_number,
        .tp_new = PyType_GenericNew,
        .tp_alloc = PyType_GenericAlloc,
        .tp_methods = pyUA_methods_deepcopy,
    };
    if(PyType_Ready(&NS0STACKTYPE(STATUSCODE)) < 0 ||
       PyModule_AddObjectRef(m, "StatusCode", (PyObject*)&NS0STACKTYPE(STATUSCODE)) < 0)
        goto error;
    PyTypeObject_setUAType(&NS0STACKTYPE(STATUSCODE), &UA_TYPES[UA_TYPES_STATUSCODE]);
    NS0TYPE(STATUSCODE) = &NS0STACKTYPE(STATUSCODE);
    pyUAStatusCode = &NS0STACKTYPE(STATUSCODE);

    /* QualifiedName */
    NS0STACKTYPE(QUALIFIEDNAME) = (PyTypeObject) {
        .ob_base = PyVarObject_HEAD_INIT(NULL, 0)
        .tp_name = "o6.QualifiedName",
        .tp_doc = PyDoc_STR("QualifiedName (OPC UA builtin type)"),
        .tp_flags = Py_TPFLAGS_DEFAULT,
        .tp_init = pyQualifiedName_init,
        .tp_getset = pyQualifiedName_getsets,
        .tp_str = pyUABuiltin_str,
        .tp_repr = pyUA_reprQuoted,
        .tp_richcompare = pyUABuiltin_richcompare,
        .tp_basicsize = sizeof(PyUABuiltin),
        .tp_new = PyType_GenericNew,
        .tp_dealloc = pyUABuiltin_dealloc,
        .tp_methods = pyUA_methods_deepcopy,
    };
    if(PyType_Ready(&NS0STACKTYPE(QUALIFIEDNAME)) < 0 ||
       PyModule_AddObjectRef(m, "QualifiedName", (PyObject*)&NS0STACKTYPE(QUALIFIEDNAME)) < 0)
        goto error;
    PyTypeObject_setUAType(&NS0STACKTYPE(QUALIFIEDNAME), &UA_TYPES[UA_TYPES_QUALIFIEDNAME]);
    NS0TYPE(QUALIFIEDNAME) = &NS0STACKTYPE(QUALIFIEDNAME);
    pyUAQualifiedName = &NS0STACKTYPE(QUALIFIEDNAME);

    /* LocalizedText */
    NS0STACKTYPE(LOCALIZEDTEXT) = (PyTypeObject) {
        .ob_base = PyVarObject_HEAD_INIT(NULL, 0)
        .tp_name = "o6.LocalizedText",
        .tp_doc = PyDoc_STR("LocalizedText (OPC UA builtin type)"),
        .tp_flags = Py_TPFLAGS_DEFAULT,
        .tp_init = pyLocalizedText_init,
        .tp_getset = pyLocalizedText_getsets,
        .tp_str = pyUABuiltin_str,
        .tp_repr = pyUA_reprQuoted,
        .tp_richcompare = pyUABuiltin_richcompare,
        .tp_basicsize = sizeof(PyUABuiltin),
        .tp_new = PyType_GenericNew,
        .tp_dealloc = pyUABuiltin_dealloc,
        .tp_methods = pyUA_methods_deepcopy,
    };
    if(PyType_Ready(&NS0STACKTYPE(LOCALIZEDTEXT)) < 0 ||
       PyModule_AddObjectRef(m, "LocalizedText", (PyObject*)&NS0STACKTYPE(LOCALIZEDTEXT)) < 0)
        goto error;
    PyTypeObject_setUAType(&NS0STACKTYPE(LOCALIZEDTEXT), &UA_TYPES[UA_TYPES_LOCALIZEDTEXT]);
    NS0TYPE(LOCALIZEDTEXT) = &NS0STACKTYPE(LOCALIZEDTEXT);
    pyUALocalizedText = &NS0STACKTYPE(LOCALIZEDTEXT);

    /* ExtensionObject */
    NS0STACKTYPE(EXTENSIONOBJECT) = (PyTypeObject) {
        .ob_base = PyVarObject_HEAD_INIT(NULL, 0)
        .tp_name = "o6.ExtensionObject",
        .tp_doc = PyDoc_STR("ExtensionObject (OPC UA builtin type)"),
        .tp_flags = Py_TPFLAGS_DEFAULT,
        .tp_init = pyExtensionObject_init,
        .tp_getset = pyExtensionObject_getsets,
        .tp_str = pyUAExtensionObject_str,
        .tp_repr = pyUAExtensionObject_repr,
        .tp_richcompare = pyUABuiltin_richcompare,
        .tp_basicsize = sizeof(PyUABuiltin),
        .tp_new = PyType_GenericNew,
        .tp_dealloc = pyUABuiltin_dealloc,
        .tp_methods = pyUA_methods_deepcopy,
    };
    if(PyType_Ready(&NS0STACKTYPE(EXTENSIONOBJECT)) < 0 ||
       PyModule_AddObjectRef(m, "ExtensionObject", (PyObject*)&NS0STACKTYPE(EXTENSIONOBJECT)) < 0)
        goto error;
    PyTypeObject_setUAType(&NS0STACKTYPE(EXTENSIONOBJECT), &UA_TYPES[UA_TYPES_EXTENSIONOBJECT]);
    NS0TYPE(EXTENSIONOBJECT) = &NS0STACKTYPE(EXTENSIONOBJECT);
    pyUAExtensionObject = &NS0STACKTYPE(EXTENSIONOBJECT);

    /* DataValue */
    NS0STACKTYPE(DATAVALUE) = (PyTypeObject) {
        .ob_base = PyVarObject_HEAD_INIT(NULL, 0)
        .tp_name = "o6.DataValue",
        .tp_flags = Py_TPFLAGS_DEFAULT,
        .tp_doc = "OPC UA DataValue",
        .tp_str = pyUADataValue_str,
        .tp_repr = pyUADataValue_repr,
        .tp_init = pyUADataValue_init,
        .tp_getset = pyUADataValue_getsets,
        .tp_basicsize = sizeof(PyUADataValue),
        .tp_new = PyType_GenericNew,
        .tp_dealloc = pyUADataValue_dealloc,
        .tp_traverse = pyUADataValue_traverse,
        .tp_clear = pyUADataValue_clear,
        .tp_methods = pyUA_methods_deepcopy,
    };
    if(PyType_Ready(&NS0STACKTYPE(DATAVALUE)) < 0 ||
       PyModule_AddObjectRef(m, "DataValue", (PyObject*)&NS0STACKTYPE(DATAVALUE)) < 0)
        goto error;
    PyTypeObject_setUAType(&NS0STACKTYPE(DATAVALUE), &UA_TYPES[UA_TYPES_DATAVALUE]);
    NS0TYPE(DATAVALUE) = &NS0STACKTYPE(DATAVALUE);
    pyUADataValue = &NS0STACKTYPE(DATAVALUE);
    
    /* DiagnosticInfo (TODO) */

    /* OPC UA enums (autogenerated from NodeSet2) */
    create_all_enums(m);

    /* DataTypeKind — open62541 internal enum, not in the OPC UA spec, so
     * the autogenerator never sees it. Register it here by hand. */
    {
        PyObject *enum_mod = PyImport_ImportModule("enum");
        if(enum_mod) {
            PyObject *IntEnum = PyObject_GetAttrString(enum_mod, "IntEnum");
            if(IntEnum) {
                /* Build a dict of name->value pairs, then call IntEnum(name, dict) */
                PyObject *members = PyDict_New();
                if(members) {
#define _DK(name, val) PyDict_SetItemString(members, name, PyLong_FromLong(val))
                    _DK("Boolean",         UA_DATATYPEKIND_BOOLEAN);
                    _DK("SByte",           UA_DATATYPEKIND_SBYTE);
                    _DK("Byte",            UA_DATATYPEKIND_BYTE);
                    _DK("Int16",           UA_DATATYPEKIND_INT16);
                    _DK("UInt16",          UA_DATATYPEKIND_UINT16);
                    _DK("Int32",           UA_DATATYPEKIND_INT32);
                    _DK("UInt32",          UA_DATATYPEKIND_UINT32);
                    _DK("Int64",           UA_DATATYPEKIND_INT64);
                    _DK("UInt64",          UA_DATATYPEKIND_UINT64);
                    _DK("Float",           UA_DATATYPEKIND_FLOAT);
                    _DK("Double",          UA_DATATYPEKIND_DOUBLE);
                    _DK("String",          UA_DATATYPEKIND_STRING);
                    _DK("DateTime",        UA_DATATYPEKIND_DATETIME);
                    _DK("Guid",            UA_DATATYPEKIND_GUID);
                    _DK("ByteString",      UA_DATATYPEKIND_BYTESTRING);
                    _DK("XmlElement",      UA_DATATYPEKIND_XMLELEMENT);
                    _DK("NodeId",          UA_DATATYPEKIND_NODEID);
                    _DK("ExpandedNodeId",  UA_DATATYPEKIND_EXPANDEDNODEID);
                    _DK("StatusCode",      UA_DATATYPEKIND_STATUSCODE);
                    _DK("QualifiedName",   UA_DATATYPEKIND_QUALIFIEDNAME);
                    _DK("LocalizedText",   UA_DATATYPEKIND_LOCALIZEDTEXT);
                    _DK("ExtensionObject", UA_DATATYPEKIND_EXTENSIONOBJECT);
                    _DK("DataValue",       UA_DATATYPEKIND_DATAVALUE);
                    _DK("Variant",         UA_DATATYPEKIND_VARIANT);
                    _DK("DiagnosticInfo",  UA_DATATYPEKIND_DIAGNOSTICINFO);
                    _DK("Decimal",         UA_DATATYPEKIND_DECIMAL);
                    _DK("Enum",            UA_DATATYPEKIND_ENUM);
                    _DK("Structure",       UA_DATATYPEKIND_STRUCTURE);
                    _DK("OptStruct",       UA_DATATYPEKIND_OPTSTRUCT);
                    _DK("Union",           UA_DATATYPEKIND_UNION);
                    _DK("BitFieldCluster", UA_DATATYPEKIND_BITFIELDCLUSTER);
#undef _DK
                    /* Use IntEnum(name, members) functional form:
                     * IntEnum("DataTypeKind", {"Boolean": 0, ...}) */
                    PyObject *cls = PyObject_CallFunction(
                        IntEnum, "sO", "DataTypeKind", members);
                    if(cls) {
                        PyModule_AddObject(m, "DataTypeKind", cls);
                        /* cls reference taken by PyModule_AddObject */
                    } else {
                        PyErr_Clear();
                    }
                    Py_DECREF(members);
                }
                Py_DECREF(IntEnum);
            }
            Py_DECREF(enum_mod);
        }
        PyErr_Clear(); /* non-fatal if it fails */
    }

    for(size_t i = 0; i < UA_TYPES_COUNT; i++) {
        if(UA_TYPES[i].typeKind == UA_DATATYPEKIND_ENUM) {
            pyUATypes[i] = (PyTypeObject*)PyObject_GetAttrString(m, UA_TYPES[i].typeName);
            if(pyUATypes[i])
                PyTypeObject_setUAType(pyUATypes[i], &UA_TYPES[i]);
            PyErr_Clear();
            Py_XDECREF(pyUATypes[i]);
        }
    }

    static PyMethodDef struct_methods[] = {
        {"__dir__", (PyCFunction)pyUAStruct_dir, METH_NOARGS, NULL},
        {"__copy__", (PyCFunction)pyUAStruct_copy, METH_NOARGS, NULL},
        {"__deepcopy__", (PyCFunction)pyUA_deepcopy, METH_O, NULL},
        {NULL}
    };

    for(size_t i = 0; i < UA_TYPES_COUNT; i++) {
        if(UA_TYPES[i].typeKind != UA_DATATYPEKIND_STRUCTURE)
            continue;

        snprintf(&pyTypeNames[i][0], 64, "o6.%s", UA_TYPES[i].typeName);

        static PyType_Slot pyUAStruct_slots[] = {
            {Py_tp_dealloc, (void *)pyUAStruct_dealloc},
            {Py_tp_traverse, (void *)pyUAStruct_traverse},
            {Py_tp_clear, (void *)pyUAStruct_clear},
            {Py_tp_new, (void *)PyType_GenericNew},
            {Py_tp_alloc, (void *)PyType_GenericAlloc},
            {Py_tp_str, (void *)pyUAStruct_str},
            {Py_tp_repr, (void *)pyUAStruct_repr},
            {Py_tp_getattro, (void *)pyUAStruct_getattro},
            {Py_tp_setattro, (void *)pyUAStruct_setattro},
            {Py_tp_methods, (void *)struct_methods},
            {0, NULL}  // terminator
        };

        static PyType_Spec structSpec = {
            .basicsize = sizeof(PyUAStruct),
            .flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HAVE_GC | Py_TPFLAGS_BASETYPE,
            .slots = pyUAStruct_slots
        };
        structSpec.name = &pyTypeNames[i][0];

        PyObject *pyUAStructType = PyType_FromSpec(&structSpec);
        if(!pyUAStructType)
            goto error;
        if(PyModule_AddObjectRef(m, UA_TYPES[i].typeName, pyUAStructType) < 0)
            goto error;
        PyTypeObject_setUAType((PyTypeObject*)pyUAStructType, &UA_TYPES[i]);
        pyUATypes[i] = (PyTypeObject*)pyUAStructType;
    }

    /* Add EventFilter.parse() classmethod */
#ifdef UA_ENABLE_SUBSCRIPTIONS_EVENTS
#ifdef UA_ENABLE_JSON_ENCODING
    {
        static PyMethodDef ef_parse_def = {
            "parse", (PyCFunction)pyEventFilter_parse,
            METH_VARARGS | METH_KEYWORDS | METH_CLASS,
            "Parse an EventFilter from a SQL-like query string."
        };
        PyTypeObject *efType = pyUATypes[UA_TYPES_EVENTFILTER];
        if(efType) {
            PyObject *descr = PyDescr_NewClassMethod(efType, &ef_parse_def);
            if(descr) {
                if(PyObject_SetAttrString((PyObject*)efType, "parse", descr) < 0) {
                    Py_DECREF(descr);
                    goto error;
                }
                Py_DECREF(descr);
            }
        }
    }
#endif
#endif

    return m;

error:
    Py_XDECREF(UUIDModule);
    Py_XDECREF(UUIDClass);
    Py_XDECREF(enumModule);
    Py_XDECREF(enumMetaClass);
    Py_XDECREF(m);
    return NULL;
}
