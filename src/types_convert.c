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

#define NO_IMPORT_ARRAY
#include "types_internal.h"
#include <numpy/arrayobject.h>
#include <numpy/arrayscalars.h>
#include <numpy/ndarraytypes.h>
#include <string.h> /* For strlen(), strncpy() */
#include <ctype.h>

void makeSnakeName(const char *caml, char *out) {
    if(!caml || !caml[0]) {
        out[0] = 0;
        return;
    }

    /* Pre-process: treat "NodeId" as a single word atom */
    char buf[128];
    size_t len = strlen(caml);
    if(len >= sizeof(buf)) len = sizeof(buf) - 1;
    memcpy(buf, caml, len);
    buf[len] = 0;
    for(size_t i = 0; i + 6 <= len; i++) {
        if((buf[i] == 'N' || buf[i] == 'n') && buf[i+1] == 'o' && buf[i+2] == 'd' &&
           buf[i+3] == 'e' && buf[i+4] == 'I' && buf[i+5] == 'd') {
            buf[i+4] = 'i';
            i += 5;
        }
    }

    const char *p = buf;
    size_t pos = 0;
    out[pos++] = tolower(*p);
    p++;

    char c;
    while((c = *p) && pos < 126) {
        if(isupper(c))
            out[pos++] = '_';
        out[pos++] = tolower(c);
        p++;
    }
    out[pos] = 0;
}

void makeCamlName(const char *snake, char *out) {
    if(!snake|| !snake[0]) {
        out[0] = 0;
        return;
    }

    size_t pos = 0;
    out[pos++] = toupper(*snake);
    snake++;

    char c;
    bool upper = false;
    while((c = *snake) && pos < 127) {
      if(c == '_') {
          upper = true;
      } else {
          out[pos++] = (upper) ? toupper(c) : c;
          upper = false;
      }
      snake++;
    }
    out[pos] = 0;

    /* Post-process: restore "NodeId" from "Nodeid" */
    for(size_t i = 0; i + 6 <= pos; i++) {
        if((out[i] == 'N' || out[i] == 'n') && out[i+1] == 'o' && out[i+2] == 'd' &&
           out[i+3] == 'e' && out[i+4] == 'i' && out[i+5] == 'd') {
            out[i+4] = 'I';
            i += 5;
        }
    }
}

/* Specialized conversion functions for builtin types */

PyObject *
PY2UA_datetime(PyObject *obj, UA_DateTime *p) {
    UA_DateTime dt;
    if(Py_TYPE(obj) == pyUADateTime) {
        dt = ((PyUABuiltin*)obj)->dateTime;
    } else if(PyLong_Check(obj)) {
        dt = PyLong_AsLongLong(obj);
        if(dt == (UA_DateTime)-1 && PyErr_Occurred())
            return NULL;
    } else if(PyUnicode_Check(obj)) {
        const char *b = PyUnicode_AsUTF8(obj);
        if(!b)
            return NULL;
        char buf[64];
        int buflen = snprintf(buf, 64, "\"%s\"", b);
        UA_ByteString input = {(size_t)buflen, (UA_Byte*)buf};
        UA_StatusCode res = UA_decodeJson(&input, &dt, &UA_TYPES[UA_TYPES_DATETIME], NULL);
        if(res != UA_STATUSCODE_GOOD) {
            PyErr_SetString(PyExc_TypeError, "Could not parse DateTime string");
            return NULL;
        }
    } else {
        // Check if it's a datetime object by checking its class name
        PyObject *class_name = PyObject_GetAttrString((PyObject*)Py_TYPE(obj), "__name__");
        if(class_name && PyUnicode_Check(class_name)) {
            const char *name = PyUnicode_AsUTF8(class_name);
            if(name && strcmp(name, "datetime") == 0) {
                // Try to convert datetime to timestamp (microseconds since epoch)
                PyObject *timestamp_method = PyObject_GetAttrString(obj, "timestamp");
                if(timestamp_method) {
                    PyObject *timestamp = PyObject_CallNoArgs(timestamp_method);
                    if(timestamp && PyFloat_Check(timestamp)) {
                        double ts = PyFloat_AsDouble(timestamp);
                        // Convert to UA_DateTime (100ns since 1601-01-01)
                        dt = (UA_DateTime)((ts + 11644473600.0) * 10000000.0);
                        Py_DECREF(timestamp);
                        Py_DECREF(timestamp_method);
                        Py_DECREF(class_name);
                        *p = dt;
                        return Py_None;
                    }
                    Py_XDECREF(timestamp);
                    Py_DECREF(timestamp_method);
                }
            }
        }
        Py_XDECREF(class_name);
        
        // Fall back to trying to convert to int
        PyObject *long_obj = PyNumber_Long(obj);
        if(long_obj) {
            dt = PyLong_AsLongLong(long_obj);
            Py_DECREF(long_obj);
            if(dt == (UA_DateTime)-1 && PyErr_Occurred())
                return NULL;
        } else {
            PyErr_SetString(PyExc_TypeError,
                            "DateTime can be cast only from int, date string, or datetime.datetime");
            return NULL;
        }
    }

    *p = dt;
    return Py_None;
}

PyObject *
PY2UA_guid(PyObject *obj, UA_Guid *p) {
    PyObject *bytes_obj = PyObject_GetAttrString(obj, "bytes_le");
    if(!bytes_obj) return NULL;

    char *data = PyBytes_AsString(bytes_obj);
    if(!data) { Py_DECREF(bytes_obj); return NULL; }

    memcpy(p, data, 16);
    Py_DECREF(bytes_obj);
    return Py_None;
}

PyObject *
PY2UA_statuscode(PyObject *obj, UA_StatusCode *p) {
    if(Py_TYPE(obj) == pyUAStatusCode) {
        *p = ((PyUABuiltin*)obj)->statusCode;
    } else  {
        unsigned long long status = PyLong_AsUnsignedLongLong(obj);
        if(status == (unsigned long long)-1 && PyErr_Occurred())
            return NULL;
        if(status > UA_UINT32_MAX) {
            PyErr_SetString(PyExc_OverflowError, "Integer too big for a StatusCode");
            return NULL;
        }
        *p = (UA_StatusCode)status;
    }
    return Py_None;
}

PyObject *
PY2UA_nodeid(PyObject *obj, UA_NodeId *p) {
    UA_StatusCode res;
    if(Py_TYPE(obj) == pyUANodeId) {
        res = UA_NodeId_copy(&((PyUABuiltin*)obj)->nodeId, p);
        return (res == UA_STATUSCODE_GOOD) ? Py_None : NULL;
    }

    /* Plain integer → ns=0 numeric NodeId */
    if(PyLong_Check(obj)) {
        unsigned long id = PyLong_AsUnsignedLong(obj);
        if(id == (unsigned long)-1 && PyErr_Occurred())
            return NULL;
        *p = UA_NODEID_NUMERIC(0, (UA_UInt32)id);
        return Py_None;
    }

    UA_String str;
    res = Unicode2String(obj, &str);
    if(res != UA_STATUSCODE_GOOD) {
        PyErr_SetString(PyExc_TypeError,
                        "NodeIds must use a string argument like \"ns=1;i=5\" or a plain integer");
        return NULL;
    }

    res = UA_NodeId_parse(p, str);
    if(res != UA_STATUSCODE_GOOD) {
        PyErr_SetString(PyExc_TypeError, "Could not parse the NodeId string");
        return NULL;
    }
    return Py_None;
}

PyObject *
PY2UA_expandednodeid(PyObject *obj, UA_ExpandedNodeId *p) {
    UA_StatusCode res;
    if(Py_TYPE(obj) == pyUANodeId) {
        UA_ExpandedNodeId_init(p);
        res = UA_NodeId_copy(&((PyUABuiltin*)obj)->nodeId, &p->nodeId);
        return (res == UA_STATUSCODE_GOOD) ? Py_None : NULL;
    }

    if(Py_TYPE(obj) == pyUAExpandedNodeId) {
        res = UA_ExpandedNodeId_copy(&((PyUABuiltin*)obj)->expandedNodeId, p);
        return (res == UA_STATUSCODE_GOOD) ? Py_None : NULL;
    }

    UA_String str;
    res = Unicode2String(obj, &str);
    if(res != UA_STATUSCODE_GOOD) {
        PyErr_SetString(PyExc_TypeError, "ExpandedNodeIds must use a string argument like \"ns=1;i=5\"");
        return NULL;
    }

    res = UA_ExpandedNodeId_parse(p, str);
    if(res != UA_STATUSCODE_GOOD) {
        PyErr_SetString(PyExc_TypeError, "Could not parse the NodeId string");
        return NULL;
    }
    return Py_None;
}

PyObject *
PY2UA_extensionobject(PyObject *obj, UA_ExtensionObject *p) {
    /* Already an ExtensionObject (encoded bytestring or xml) — copy as-is */
    if(Py_TYPE(obj) == pyUAExtensionObject) {
        UA_StatusCode res = UA_ExtensionObject_copy(&((PyUABuiltin*)obj)->eo, p);
        return (res == UA_STATUSCODE_GOOD) ? Py_None : NULL;
    }

    /* Any other known OPC UA struct — wrap as a decoded ExtensionObject so
     * open62541 handles binary encoding and the typeId automatically. */
    const UA_DataType *uaType = PY2UAType(Py_TYPE(obj));
    if(uaType) {
        void *data = UA_new(uaType);
        if(!data)
            return PyErr_NoMemory();
        UA_init(data, uaType);
        PyObject *res = PY2UA(obj, data, uaType);
        if(!res) {
            UA_delete(data, uaType);
            return NULL;
        }
        UA_ExtensionObject_clear(p);
        p->encoding = UA_EXTENSIONOBJECT_DECODED;
        p->content.decoded.type = uaType;
        p->content.decoded.data = data;
        return Py_None;
    }

    PyErr_SetString(PyExc_TypeError,
                    "ExtensionObject field requires an ExtensionObject or an OPC UA type");
    return NULL;
}

PyObject *
PY2UA_qualifiedname(PyObject *obj, UA_QualifiedName *p) {
    UA_StatusCode res;
    if(Py_TYPE(obj) == pyUAQualifiedName) {
        res = UA_QualifiedName_copy(&((PyUABuiltin*)obj)->qualifiedName, p);
        return (res == UA_STATUSCODE_GOOD) ? Py_None : NULL;
    }

    UA_String str;
    res = Unicode2String(obj, &str);
    if(res != UA_STATUSCODE_GOOD) {
        // Clear any existing exception and set our own
        PyErr_Clear();
        PyErr_SetString(PyExc_TypeError, "QualifiedName requires a string argument");
        return NULL;
    }

    res = UA_QualifiedName_parse(p, str);
    if(res != UA_STATUSCODE_GOOD) {
        PyErr_SetString(PyExc_TypeError, "Could not parse the QualifiedName string");
        return NULL;
    }
    return Py_None;
}

PyObject *
PY2UA_localizedtext(PyObject *obj, UA_LocalizedText *p) {
    if(Py_TYPE(obj) == pyUALocalizedText) {
        UA_StatusCode res = UA_LocalizedText_copy(&((PyUABuiltin*)obj)->localizedText, p);
        return (res == UA_STATUSCODE_GOOD) ? Py_None : NULL;
    }

    // If it's a plain string, treat it as text with empty locale
    if(PyUnicode_Check(obj)) {
        UA_String str;
        UA_StatusCode res = Unicode2String(obj, &str);
        if(res != UA_STATUSCODE_GOOD) {
            PyErr_Clear();
            PyErr_SetString(PyExc_TypeError, "Could not convert string to LocalizedText");
            return NULL;
        }
        p->locale = UA_STRING_NULL;
        res = UA_String_copy(&str, &p->text);
        return (res == UA_STATUSCODE_GOOD) ? Py_None : NULL;
    }

    PyErr_SetString(PyExc_TypeError, "LocalizedText input must be a string or LocalizedText object");
    return NULL;
}

/**************************************************/
/* Translate any OPC UA DataType from Python to C */
/**************************************************/
// TOOD: Add all builtin types
// TODO: Traverse structures (trees with builtin types for the leaf nodes)

PyObject * UA2PY_guid(UA_Guid *guid) {
    PyObject *kwargs, *result = NULL;
    PyObject *args = PyTuple_New(0);
    if(!args)
        return NULL;
    kwargs = Py_BuildValue("{s:y#}", "bytes_le", guid, sizeof(UA_Guid));
    if(!kwargs)
        goto err;
    result = PyObject_Call(UUIDClass, args, kwargs);
    Py_DECREF(kwargs);
    err: Py_DECREF(args);
    return result;
}

static PyObject *
UA2PY_variant(UA_Variant *v) {
    if(!v->type)
        return Py_None;

    // Handle scalars
    if(UA_Variant_isScalar(v))
        return UA2PY(v->data, v->type);

    // Handle (multi-dimensional) arrays

    // Get the dtype
    int dtype = UA2NPType(v->type);
    if(dtype < 0) {
        // An array of variants becomes a variant of ANY
        if(v->type == &UA_TYPES[UA_TYPES_VARIANT]) {
            dtype = NPY_OBJECT;
        } else {
            PyErr_Format(PyExc_TypeError, "Datatype %s not registered for numpy",
                         v->type->typeName);
            return NULL;
        }
    }

    PyArray_Descr *descr = PyArray_DescrFromType(dtype);
    if(!descr ) {
        PyErr_Format(PyExc_TypeError, "Datatype %s not registered for numpy",
                     v->type->typeName);
        return NULL;
    }

    // Check the max dimensions we support
    if(v->arrayDimensionsSize > 10) {
        PyErr_Format(PyExc_TypeError, "Variant has %u dimensions -- too much!",
                     v->arrayDimensionsSize);
        return NULL;
    }

    // Prepare the dims array.
    // When arrayDimensionsSize == 0 (common for 1-D arrays written without
    // explicit dimension info) fall back to a flat 1-D array of arrayLength.
    int ndims;
    npy_intp dims[10];
    if(v->arrayDimensionsSize == 0) {
        ndims = 1;
        dims[0] = (npy_intp)v->arrayLength;
    } else {
        ndims = (int)v->arrayDimensionsSize;
        for(size_t i = 0; i < v->arrayDimensionsSize; i++)
            dims[i] = (npy_intp)v->arrayDimensions[i];
    }

    // Allocate the array
    PyObject *array = PyArray_SimpleNew(ndims, dims, dtype);
    if(!array)
        return NULL;

    // Copy the data
    void *arr_data = PyArray_DATA((PyArrayObject*)array);
    uintptr_t v_data = (uintptr_t)v->data;
    switch(v->type->typeKind) {
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
        memcpy(arr_data, v->data, v->type->memSize * v->arrayLength);
        break;
    default:
        for(size_t i = 0; i < v->arrayLength; i++) {
            PyObject *item = UA2PY((void*)v_data, v->type);
            if(!item) {
                Py_DECREF(array);
                return NULL;
            }
            char *ptr = PyArray_GETPTR1((PyArrayObject*)array, i);
            if(PyArray_Pack(descr, ptr, item) < 0) {
                Py_DECREF(item);
                Py_DECREF(array);
                return NULL;
            }
            Py_DECREF(item);
            v_data += v->type->memSize;
        }
    }
    return array;
}

// TODO: w/o copy is possible for nested structures?
PyObject *
UA2PY(void *p, const UA_DataType *type) {
    int typenum = 0;
    PyTypeObject *pytype = NULL;
    size_t offset = offsetof(PyUABuiltin, dateTime); // Default for builtins
    switch(type->typeKind) {
    case UA_DATATYPEKIND_BOOLEAN: return (*(UA_Boolean*)p) ? Py_True : Py_False;
    case UA_DATATYPEKIND_SBYTE:  typenum = NPY_INT8;   goto np_type;
    case UA_DATATYPEKIND_BYTE:   typenum = NPY_UINT8;  goto np_type;
    case UA_DATATYPEKIND_INT16:  typenum = NPY_INT16;  goto np_type;
    case UA_DATATYPEKIND_UINT16: typenum = NPY_UINT16; goto np_type;
    case UA_DATATYPEKIND_INT32:  typenum = NPY_INT32;  goto np_type;
    case UA_DATATYPEKIND_UINT32: typenum = NPY_UINT32; goto np_type;
    case UA_DATATYPEKIND_INT64:  typenum = NPY_INT64;  goto np_type;
    case UA_DATATYPEKIND_UINT64: typenum = NPY_UINT64; goto np_type;
    case UA_DATATYPEKIND_FLOAT:  typenum = NPY_FLOAT;  goto np_type;
    case UA_DATATYPEKIND_DOUBLE: typenum = NPY_DOUBLE; goto np_type;
    case UA_DATATYPEKIND_DATETIME: pytype = pyUADateTime; goto object_type;
    case UA_DATATYPEKIND_STATUSCODE: pytype = pyUAStatusCode; goto object_type;
    case UA_DATATYPEKIND_NODEID: pytype = pyUANodeId; goto object_type;
    case UA_DATATYPEKIND_EXPANDEDNODEID: pytype = pyUAExpandedNodeId; goto object_type;
    case UA_DATATYPEKIND_QUALIFIEDNAME: pytype = pyUAQualifiedName; goto object_type;
    case UA_DATATYPEKIND_LOCALIZEDTEXT: pytype = pyUALocalizedText; goto object_type;
    case UA_DATATYPEKIND_EXTENSIONOBJECT: pytype = pyUAExtensionObject; goto object_type;
    case UA_DATATYPEKIND_GUID: return UA2PY_guid(p);
    case UA_DATATYPEKIND_STRING:
    case UA_DATATYPEKIND_XMLELEMENT: {
        UA_String *str = (UA_String*)p;
        return PyUnicode_FromStringAndSize((char*)str->data, str->length);
    }
    case UA_DATATYPEKIND_BYTESTRING: {
        UA_ByteString *str = (UA_ByteString*)p;
        return PyBytes_FromStringAndSize((char*)str->data, str->length);
    }
    case UA_DATATYPEKIND_STRUCTURE:
    case UA_DATATYPEKIND_OPTSTRUCT:
        pytype = UA2PYType(type);
        offset = offsetof(PyUAStruct, data);
        goto object_type;
    case UA_DATATYPEKIND_VARIANT:
        return UA2PY_variant((UA_Variant*)p);
    case UA_DATATYPEKIND_DATAVALUE:
        pytype = pyUADataValue;
        offset = offsetof(PyUADataValue, dv);
        goto object_type;
    case UA_DATATYPEKIND_ENUM: {
        UA_Int32 val = *(UA_Int32*)p;
        PyTypeObject *pyEnumType = UA2PYType(type);
        if(pyEnumType) {
            PyObject *intObj = PyLong_FromLong((long)val);
            if(!intObj) return NULL;
            PyObject *result = PyObject_CallFunctionObjArgs((PyObject*)pyEnumType, intObj, NULL);
            Py_DECREF(intObj);
            return result;
        }
        return PyLong_FromLong((long)val);
    }
    case UA_DATATYPEKIND_DIAGNOSTICINFO:
    case UA_DATATYPEKIND_DECIMAL:
    case UA_DATATYPEKIND_UNION:
    case UA_DATATYPEKIND_BITFIELDCLUSTER:
    default: break;
    }
    return Py_None;

 np_type:
    return PyArray_Scalar(p, PyArray_DescrFromType(typenum), NULL);

 object_type:
    PyObject *obj = pytype->tp_new(pytype, NULL, NULL);
    if(!obj)
        return NULL;
    void *dst = (void*)(((uintptr_t)obj) + offset);
    UA_StatusCode res = UA_copy(p, dst, type);
    if(res != UA_STATUSCODE_GOOD) {
        Py_DECREF(obj);
        return PyErr_StatusCode(res);
    }
    return obj;
}

PyObject *
PY2UA_uint(PyObject *obj, void *p, const UA_DataType *type) {
    // Convert input to unsigned long long
    unsigned long long tmp;
    if(PyLong_Check(obj)) {
        tmp = PyLong_AsUnsignedLongLong(obj);
        if(tmp == (unsigned long long)-1 && PyErr_Occurred())
            return NULL;
    } else {
        PyArray_Descr *descr = PyArray_DescrFromScalar(obj);
        if(!descr)
            return NULL;
        long long stmp;
        switch(descr->type_num) {
        case NPY_UINT8:  stmp = ((PyUInt8ScalarObject *)obj)->obval; break;
        case NPY_INT8:   stmp = ((PyInt8ScalarObject *) obj)->obval; break;
        case NPY_UINT16: stmp = ((PyUInt16ScalarObject *)obj)->obval; break;
        case NPY_INT16:  stmp = ((PyInt16ScalarObject *) obj)->obval; break;
        case NPY_UINT32: stmp = ((PyUInt32ScalarObject *)obj)->obval; break;
        case NPY_INT32:  stmp = ((PyInt32ScalarObject *) obj)->obval; break;
        case NPY_INT64:  stmp = ((PyInt64ScalarObject *) obj)->obval; break;
        case NPY_UINT64: tmp = ((PyUInt64ScalarObject *)obj)->obval; goto set_out;
        default:
            PyErr_SetString(PyExc_TypeError, "Expected a NumPy integer scalar");
            return NULL;
        }
        if(stmp < 0) {
            PyErr_SetString(PyExc_OverflowError, "Unsigned integer cannot represent negative values");
            return NULL;
        }
        tmp = (unsigned long long)stmp;
    }

 set_out:
    // Translate unsigned long long to output
    switch(type->typeKind) {
    case UA_DATATYPEKIND_BYTE:
        if(tmp > UA_BYTE_MAX) {
            PyErr_SetString(PyExc_OverflowError, "Integer value out of Byte range");
            return NULL;
        }
        *(UA_Byte*)p = (UA_Byte)tmp;
        break;
    case UA_DATATYPEKIND_UINT16:
        if(tmp > UA_UINT16_MAX) {
            PyErr_SetString(PyExc_OverflowError, "Integer value out of UInt16 range");
            return NULL;
        }
        *(UA_UInt16*)p = (UA_UInt16)tmp;
        break;
    case UA_DATATYPEKIND_UINT32:
        if(tmp > UA_UINT32_MAX) {
            PyErr_SetString(PyExc_OverflowError, "Integer value out of UInt32 range");
            return NULL;
        }
        *(UA_UInt32*)p = (UA_UInt32)tmp;
        break;
    case UA_DATATYPEKIND_UINT64:
    default:
        *(UA_UInt64*)p = tmp; break;
    }

    return Py_None;
}

PyObject *
PY2UA_int(PyObject *obj, void *p, const UA_DataType *type) {
    // Convert input to long long
    long long tmp;
    if(PyLong_Check(obj)) {
        tmp = PyLong_AsLongLong(obj);
        if(tmp == -1 && PyErr_Occurred())
            return NULL;
    } else {
        PyArray_Descr *descr = PyArray_DescrFromScalar(obj);
        if(!descr)
            return NULL;
        switch(descr->type_num) {
        case NPY_UINT8:  tmp = ((PyUInt8ScalarObject *)obj)->obval; break;
        case NPY_INT8:   tmp = ((PyInt8ScalarObject *) obj)->obval; break;
        case NPY_UINT16: tmp = ((PyUInt16ScalarObject *)obj)->obval; break;
        case NPY_INT16:  tmp = ((PyInt16ScalarObject *) obj)->obval; break;
        case NPY_UINT32: tmp = ((PyUInt32ScalarObject *)obj)->obval; break;
        case NPY_INT32:  tmp = ((PyInt32ScalarObject *) obj)->obval; break;
        case NPY_INT64:  tmp = ((PyInt64ScalarObject *) obj)->obval; break;
        case NPY_UINT64:
            if(((PyUInt64ScalarObject *)obj)->obval > UA_INT64_MAX) {
                PyErr_SetString(PyExc_OverflowError, "Uint64 too large to fit in signed integer");
                return NULL;
            }
            tmp = ((PyUInt64ScalarObject *)obj)->obval; break;
        default:
            PyErr_SetString(PyExc_TypeError, "Expected a NumPy integer scalar");
            return NULL;
        }
    }

    // Translate long long to output
    switch(type->typeKind) {
    case UA_DATATYPEKIND_SBYTE:
        if(tmp < UA_SBYTE_MIN || tmp > UA_SBYTE_MAX) {
            PyErr_SetString(PyExc_OverflowError, "Integer value out of SByte range");
            return NULL;
        }
        *(UA_SByte*)p = (UA_SByte)tmp;
        break;
    case UA_DATATYPEKIND_INT16:
        if(tmp < UA_INT16_MIN || tmp > UA_INT16_MAX) {
            PyErr_SetString(PyExc_OverflowError, "Integer value out of Int16 range");
            return NULL;
        }
        *(UA_Int16*)p = (UA_Int16)tmp;
        break;
    case UA_DATATYPEKIND_INT32:
        if(tmp < UA_INT32_MIN || tmp > UA_INT32_MAX) {
            PyErr_SetString(PyExc_OverflowError, "Integer value out of Int32 range");
            return NULL;
        }
        *(UA_Int32*)p = (UA_Int32)tmp;
        break;
    case UA_DATATYPEKIND_INT64:
    default:
        *(UA_Int64*)p = tmp; break;
    }

    return Py_None;
}

PyObject *
PY2UA_float(PyObject *obj, void *p, const UA_DataType *type) {
    double val;
    if(PyFloat_Check(obj)) {
        val = PyFloat_AsDouble(obj);
    } else if(PyArray_IsScalar(obj, Float64)) {
        PyArray_ScalarAsCtype(obj, &val);
    } else if(PyArray_IsScalar(obj, Float32)) {
        float fval;
        PyArray_ScalarAsCtype(obj, &fval);
        val = fval;
    } else {
        PyErr_SetString(PyExc_TypeError, "Expected a floating point value");
        return NULL;
    }

    if(type->typeKind == UA_DATATYPEKIND_DOUBLE)
        *(double*)p = val;
    else
        *(float*)p = val;
    return Py_None;
}

PyObject *
PY2UA_structure(PyObject *obj, void *p, const UA_DataType *type) {
    uintptr_t pos = (uintptr_t)p;

    const UA_DataType *objUAType = PY2UAType(Py_TYPE(obj));

    // If obj is a PyUAStruct, then we can save a UA2PY - PY2UA roundtrip
    uintptr_t src_pos = (uintptr_t)&((PyUAStruct*)obj)->data;
    PyObject *src_dict = (objUAType == type) ? ((PyUAStruct*)obj)->dict : NULL;
    
    for(size_t i = 0; i < type->membersSize; i++) {
        // Get the member
        const UA_DataTypeMember *m = &type->members[i];
        pos += m->padding;
        char snakeName[128];
        makeSnakeName(m->memberName, snakeName);

        PyObject *key = PyUnicode_FromString(snakeName) ;
        if(!key) {
            UA_clear(p, type);
            return NULL;
        }

        // Get existing python member or raw data
        PyObject *value = NULL;
        void *uaValue = NULL;

        // Already lifted into the dictionary of the PyUAStruct
        if(src_dict) {
            value = PyDict_GetItemWithError(src_dict, key);
            if(!value && PyErr_Occurred()) {
                UA_clear(p, type);
                return NULL;
            }
            Py_XINCREF(value);
        }

        // Get direct UA pointer or try a normal read
        if(!value) {
            if(objUAType == type) {
                uaValue = (void*)(src_pos + (pos - (uintptr_t)p));
            } else {
                value = PyObject_GetAttr(obj, key);
                if(!value) {
                    if(!PyErr_ExceptionMatches(PyExc_AttributeError)) {
                        UA_clear(p, type);
                        return NULL;
                    }
                    PyErr_Clear();  // ok - missing the attribute
                }
            }
        }

        // Copy an array
        PyObject *res = Py_None;
        if(m->isArray) {
            // Get the array pointers and increase pos
            size_t *arr_len = (size_t*)pos;
            pos += sizeof(size_t);
            void **arr = (void**)pos;
            pos += sizeof(void*);

            // Copy the array from UA to UA
            if(uaValue) {
                size_t src_len = *(size_t*)uaValue;
                uaValue += sizeof(size_t);
                void *src_arr = *(void**)uaValue;
                UA_StatusCode status = UA_Array_copy(src_arr, src_len, arr, m->memberType);
                if(status != UA_STATUSCODE_GOOD)
                    return PyErr_StatusCode(status);
                *arr_len = src_len;
                continue;
            }

            // Not found or None -> empty array
            if(!value || value == Py_None) {
                Py_XDECREF(value);
                continue;
            }

            // Get the length
            Py_ssize_t length = PyObject_Length(value);
            if(length == -1) {
                Py_DECREF(value);
                return NULL;
            }

            // Allocate the array
            *arr = UA_calloc(length, m->memberType->memSize);
            if(!*arr) {
                Py_DECREF(value);
                PyErr_NoMemory();
                return NULL;
            }
            *arr_len = (size_t)length;

            // Copy the members
            uintptr_t arrpos = (uintptr_t)*arr;
            for(size_t j = 0; j < (size_t)length; j++) {
                PyObject *elem = PySequence_GetItem(value, j);
                if(!elem) {
                    res = NULL;
                    break;
                }
                res = PY2UA(elem, (void*)arrpos, m->memberType);
                Py_DECREF(elem);
                if(!res)
                    break;
                arrpos += m->memberType->memSize;
            }

            Py_DECREF(value);
            if(!res)
                return NULL;
            continue;
        }

        // Copy an optional scalar (stored as a pointer in the C struct)
        if(m->isOptional) {
            if(uaValue) {
                void *src_ptr = *(void**)uaValue;
                if(src_ptr) {
                    void *allocated = UA_new(m->memberType);
                    if(!allocated) {
                        Py_XDECREF(value);
                        PyErr_NoMemory();
                        return NULL;
                    }
                    UA_StatusCode status = UA_copy(src_ptr, allocated, m->memberType);
                    if(status != UA_STATUSCODE_GOOD) {
                        UA_free(allocated);
                        Py_XDECREF(value);
                        return PyErr_StatusCode(status);
                    }
                    *(void**)pos = allocated;
                }
            } else if(value && value != Py_None) {
                void *allocated = UA_new(m->memberType);
                if(!allocated) {
                    Py_XDECREF(value);
                    PyErr_NoMemory();
                    return NULL;
                }
                res = PY2UA(value, allocated, m->memberType);
                if(!res) {
                    UA_delete(allocated, m->memberType);
                    Py_XDECREF(value);
                    return NULL;
                }
                *(void**)pos = allocated;
            }
            pos += sizeof(void*);
            Py_XDECREF(value);
            continue;
        }

        // Copy a scalar
        if(uaValue) {
            UA_StatusCode status = UA_copy(uaValue, (void*)pos, m->memberType);
            if(status != UA_STATUSCODE_GOOD)
                return PyErr_StatusCode(status);
        } else if(value && value != Py_None) {
            res = PY2UA(value, (void*)pos, m->memberType);
        }
        pos += m->memberType->memSize;
        Py_XDECREF(value);
        if(!res)
            return NULL;
    }

    return Py_None;
}

PyObject *
PY2UA_structure_array(PyObject *obj, void *arrayPtr, const UA_DataType *type) {
    if (!PySequence_Check(obj)) {
        PyErr_SetString(PyExc_TypeError, "Expected a sequence for array");
        return NULL;
    }
    
    Py_ssize_t length = PySequence_Size(obj);
    if (length < 0) return NULL;
    
    // Allocate C array
    void *array = UA_Array_new((size_t)length, type);
    if (!array && length > 0) {
        PyErr_NoMemory();
        return NULL;
    }
    
    // Convert each element
    for (Py_ssize_t i = 0; i < length; i++) {
        PyObject *item = PySequence_GetItem(obj, i);
        if (!item) {
            UA_Array_delete(array, (size_t)length, type);
            return NULL;
        }
        
        void *elementPtr = (char*)array + (i * type->memSize);
        PyObject *result = PY2UA(item, elementPtr, type);
        Py_DECREF(item);
        
        if (!result) {
            UA_Array_delete(array, (size_t)length, type);
            return NULL;
        }
    }
    
    // Store in the struct
    *(size_t*)arrayPtr = (size_t)length;
    *(void**)((char*)arrayPtr + sizeof(size_t)) = array;
    
    return Py_None;
}

PyObject *
PY2UA_variant(PyObject *obj, UA_Variant *variant) {
    if(obj == Py_None) {
        UA_Variant_init(variant);
        return Py_None;
    }

    PyUATypeMatch match = PY2UAMatch(obj);
    if(!match.uaType) {
        PyErr_SetString(PyExc_TypeError,
                        "Object cannot be converted to an OPC UA native type");
        return NULL;
    }

    // Handle NumPy array
    if(PyArray_Check(obj)) {
        // Allocate the array
        PyArrayObject *arr = (PyArrayObject*)obj;
        npy_intp size = PyArray_SIZE(arr);
        variant->data = UA_Array_new(size, match.uaType);
        if(!variant->data) {
            PyErr_NoMemory();
            return NULL;
        }
        variant->type = match.uaType;
        variant->arrayLength = size;

        // Set the array dimensions (if dims > 1)
        int ndim = PyArray_NDIM(arr);
        npy_intp *shape = PyArray_SHAPE(arr);
        if(ndim > 1) {
            variant->arrayDimensions = UA_Array_new(ndim, &UA_TYPES[UA_TYPES_UINT32]);
            if(!variant->arrayDimensions) {
                UA_Variant_clear(variant);
                PyErr_NoMemory();
                return NULL;
            }
            variant->arrayDimensionsSize = ndim;

            for(int i = 0; i < ndim; i++) {
                variant->arrayDimensions[i] = shape[i];
            }
        }

        // Copy the content
        void *np_data = PyArray_DATA(arr);
        switch(variant->type->typeKind) {
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
            memcpy(variant->data, np_data, size * variant->type->memSize);
            break;

        default:
            uintptr_t np_pos = (uintptr_t)np_data;
            uintptr_t var_pos = (uintptr_t)variant->data;
            for(npy_intp i = 0; i < size; i++) {
                np_pos += sizeof(PyObject*);
                var_pos += variant->type->memSize;
                PyObject *out = PY2UA((PyObject*)np_pos, (void*)var_pos, variant->type);
                if(!out) {
                    UA_Variant_clear(variant);
                    return NULL;
                }
            }
        }
        return Py_None;
    }

    // Handle native python sequence
    // Handle strings specially (they are sequences but should be treated as scalars).
    if(PySequence_Check(obj) && !PyUnicode_Check(obj) && !PyBytes_Check(obj)) {
        Py_ssize_t len = PySequence_Length(obj);
        variant->data = UA_Array_new(len, match.uaType);
        if(!variant->data) {
            PyErr_NoMemory();
            return NULL;
        }
        variant->type = match.uaType;
        variant->arrayLength = len;

        // Convert the members - assume they have the same type as the first
        uintptr_t arr_pos = (uintptr_t)variant->data;
        for(Py_ssize_t i = 0; i < len; ++i) {
            PyObject *item = PySequence_GetItem(obj, i);  // New reference
            if(!item) {
                UA_Variant_clear(variant);
                return NULL;
            }

            PyObject *out = PY2UA(item, (void*)arr_pos, variant->type);
            Py_DECREF(item);
            if(!out) {
                UA_Variant_clear(variant);
                return NULL;
            }

            arr_pos += variant->type->memSize;
        }
        return Py_None;
    }

    // Scalar type
    void *data = UA_malloc(match.uaType->memSize);
    if(!data) {
        PyErr_NoMemory();
        return NULL;
    }

    PyObject *out = PY2UA(obj, data, match.uaType);
    if(!out) {
        UA_free(data);
        return NULL;
    }

    UA_Variant_setScalar(variant, data, match.uaType);
    return Py_None;
}

PyObject *
PY2UA(PyObject *obj, void *p, const UA_DataType *type) {
    UA_init(p, type);

    switch(type->typeKind) {
    case UA_DATATYPEKIND_BOOLEAN: {
        int val = PyObject_IsTrue(obj);
        if(val < 0)
            return NULL;
        *(UA_Boolean*)p = (val == 0) ? false : true;
        return Py_None;
    }
    case UA_DATATYPEKIND_SBYTE:
    case UA_DATATYPEKIND_INT16:
    case UA_DATATYPEKIND_INT32:
    case UA_DATATYPEKIND_INT64:
        return PY2UA_int(obj, p, type);
    case UA_DATATYPEKIND_BYTE:
    case UA_DATATYPEKIND_UINT16:
    case UA_DATATYPEKIND_UINT32:
    case UA_DATATYPEKIND_UINT64:
        return PY2UA_uint(obj, p, type);
    case UA_DATATYPEKIND_FLOAT:
    case UA_DATATYPEKIND_DOUBLE:
        return PY2UA_float(obj, p, type);
    case UA_DATATYPEKIND_STRING:
    case UA_DATATYPEKIND_XMLELEMENT: {
        Py_ssize_t size;
        const char *buf = PyUnicode_AsUTF8AndSize(obj, &size);
        if(size < 0)
            return NULL;
        UA_String tmp = {(size_t)size, (UA_Byte*)(uintptr_t)buf};
        UA_StatusCode res = UA_String_copy(&tmp, (UA_String*)p);
        return (res == UA_STATUSCODE_GOOD) ? Py_None : NULL;
    }
    case UA_DATATYPEKIND_BYTESTRING: {
        char *buf;
        Py_ssize_t size;
        int res = PyBytes_AsStringAndSize(obj, &buf, &size);
        if(res < 0)
            return NULL;
        UA_ByteString tmp = {(size_t)size, (UA_Byte*)buf};
        UA_StatusCode status = UA_ByteString_copy(&tmp, (UA_ByteString*)p);
        return (status == UA_STATUSCODE_GOOD) ? Py_None : NULL;
    }
    case UA_DATATYPEKIND_DATETIME:
        return PY2UA_datetime(obj, (UA_DateTime*)p);
    case UA_DATATYPEKIND_GUID:
        return PY2UA_guid(obj, (UA_Guid*)p);
    case UA_DATATYPEKIND_STATUSCODE:
        return PY2UA_statuscode(obj, (UA_StatusCode*)p);
    case UA_DATATYPEKIND_NODEID:
        return PY2UA_nodeid(obj, (UA_NodeId*)p);
    case UA_DATATYPEKIND_EXPANDEDNODEID:
        return PY2UA_expandednodeid(obj, (UA_ExpandedNodeId*)p);
    case UA_DATATYPEKIND_QUALIFIEDNAME:
        return PY2UA_qualifiedname(obj, (UA_QualifiedName*)p);
    case UA_DATATYPEKIND_LOCALIZEDTEXT:
        return PY2UA_localizedtext(obj, (UA_LocalizedText*)p);
    case UA_DATATYPEKIND_EXTENSIONOBJECT:
        return PY2UA_extensionobject(obj, (UA_ExtensionObject*)p);
    case UA_DATATYPEKIND_STRUCTURE:
    case UA_DATATYPEKIND_OPTSTRUCT:
        return PY2UA_structure(obj, p, type);
    case UA_DATATYPEKIND_VARIANT:
        return PY2UA_variant(obj, (UA_Variant*)p);
    case UA_DATATYPEKIND_DATAVALUE:
        return PY2UA_datavalue(obj, (UA_DataValue*)p);
    case UA_DATATYPEKIND_ENUM: {
        long val = PyLong_AsLong(obj);
        if(val == -1 && PyErr_Occurred()) {
            PyErr_Clear();
            obj = PyObject_GetAttrString(obj, "value");
            if(!obj)
                return NULL;
            Py_DECREF(obj);
            val = PyLong_AsLong(obj);
            if(val == -1 && PyErr_Occurred())
                return NULL;
        }
        *(UA_Int32*)p = (UA_Int32)val;
        return Py_None;
    }
    case UA_DATATYPEKIND_DIAGNOSTICINFO:
    case UA_DATATYPEKIND_DECIMAL:
    case UA_DATATYPEKIND_UNION:
    case UA_DATATYPEKIND_BITFIELDCLUSTER:
    default:
        break;
    }

    return NULL;
}

/***************/
/* Numpy Array */
/***************/

int
np_setitem(PyObject *item, void *data, void *arr) {
    PyArrayObject *array = (PyArrayObject *)arr;
    PyArray_Descr *descr = PyArray_DESCR(array);
    PyTypeObject *type = descr->typeobj;
    if(!PyObject_TypeCheck(item, type)) {
        PyErr_Format(PyExc_TypeError, "Expected an instance of %s", type->tp_name);
        return -1;
    }

    // Decref the existing object (if any)
    PyObject **slot = (PyObject **)data;
    Py_XDECREF(*slot);

    // Store the item in the array
    Py_INCREF(item);
    *slot = item;

    return PyErr_Occurred() ? -1 : 0;
}
