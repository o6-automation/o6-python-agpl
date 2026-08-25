/* Copyright 2026 (c) o6 Automation GmbH */
#include "module.h"
#include "types_internal.h"
#include "datatypes.h"
#include "ua_extension_namespacemapping.h"

#if defined(_WIN32)
#  include <malloc.h>
#  define UA_STACK_ALLOC(n) ((char*)_alloca(n))
#else
#  define UA_STACK_ALLOC(n) ((char*)__builtin_alloca(n))
#endif

PyObject * PY_encodeBinary(PyObject *_, PyObject *obj) {
    PyUATypeMatch m = PY2UAMatch(obj);
    const UA_DataType *uaType = m.uaType;
    if(!uaType || m.dimension != PYVALUEDIMENSION_SCALAR) {
        PyErr_SetString(PyExc_TypeError, "Expected a scalar OPC UA value");
        return NULL;
    }

    /* Make a "pure OPC UA" structure */
    char *data = UA_STACK_ALLOC(uaType->memSize);
    UA_init(data, uaType);
    PyObject *out = PY2UA(obj, data, uaType, NULL, NULL);
    if(!out)
        return out;

    /* Decode to a UA structure */
    UA_String bytes = UA_STRING_NULL;
    UA_StatusCode res = UA_encodeBinary(data, uaType, &bytes, NULL);
    UA_clear(data, uaType);
    if(res != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(res);

    /* Move into the outbut bytes object */
    out = PyBytes_FromStringAndSize((char*)bytes.data, bytes.length);
    UA_String_clear(&bytes);
    return out;
}

PyObject * PY_decodeBinary(PyObject *_, PyObject *args) {
    /* Unpack the arguments */
    PyObject *arg1, *arg2;
    if(!PyArg_ParseTuple(args, "OO", &arg1, &arg2))
        return NULL;

    /* Get the string argument */
    char *input;
    Py_ssize_t len;
    if(PyBytes_AsStringAndSize(arg1, &input, &len) < 0)
        return NULL;

    /* Get and validate the UA type. */
    PyTypeObject *type = (PyTypeObject*)arg2;
    const UA_DataType *uaType = PY2UAType(type);
    if(!uaType) {
        PyErr_SetString(PyExc_TypeError,
                        "Expected an OPC UA datatype for the second argument");
        return NULL;
    }

    /* Decode to a UA structure */
    char *data = UA_STACK_ALLOC(uaType->memSize);
    UA_ByteString encoding = {(size_t)len, (UA_Byte*)input};
    UA_StatusCode res = UA_decodeBinary(&encoding, data, uaType, NULL);
    if(res != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(res);

    /* Convert to a Python object and return */
    PyObject *out = UA2PY(data, uaType, NULL);
    if(!out)
        UA_clear(data, uaType);
    return out;
}

PyObject * PY_encodeXml(PyObject *_, PyObject *obj) {
#ifndef UA_ENABLE_XML_ENCODING
    PyErr_SetString(PyExc_NotImplementedError,
                    "o6 was built without open62541 XML encoding support");
    return NULL;
#else
    PyUATypeMatch m = PY2UAMatch(obj);
    const UA_DataType *uaType = m.uaType;
    if(!uaType || m.dimension != PYVALUEDIMENSION_SCALAR) {
        PyErr_SetString(PyExc_TypeError, "Expected a scalar OPC UA value");
        return NULL;
    }

    char *data = UA_STACK_ALLOC(uaType->memSize);
    UA_init(data, uaType);
    PyObject *out = PY2UA(obj, data, uaType, NULL, NULL);
    if(!out)
        return NULL;

    UA_ByteString bytes = UA_BYTESTRING_NULL;
    UA_StatusCode st = UA_encodeXml(data, uaType, &bytes, NULL);
    UA_clear(data, uaType);
    if(st != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(st);

    out = PyBytes_FromStringAndSize((char*)bytes.data, bytes.length);
    UA_ByteString_clear(&bytes);
    return out;
#endif
}

PyObject *
PY_decodeXml(PyObject *_, PyObject *args) {
#ifndef UA_ENABLE_XML_ENCODING
    PyErr_SetString(PyExc_NotImplementedError,
                    "o6 was built without open62541 XML decoding support");
    return NULL;
#else
    PyObject *pyXml, *pyType;
    if(!PyArg_ParseTuple(args, "OO", &pyXml, &pyType))
        return NULL;
    const UA_DataType *expectedType = PY2UAType((PyTypeObject*)pyType);
    if(!expectedType) {
        PyErr_SetString(PyExc_TypeError, "Expected an OPC UA datatype");
        return NULL;
    }

    char *input;
    Py_ssize_t inputLen;
    if(PyUnicode_Check(pyXml)) {
        input = (char*)PyUnicode_AsUTF8AndSize(pyXml, &inputLen);
        if(!input)
            return NULL;
    } else if(PyBytes_AsStringAndSize(pyXml, &input, &inputLen) < 0) {
        return NULL;
    }
    char *data = UA_STACK_ALLOC(expectedType->memSize);
    UA_ByteString xml = {(size_t)inputLen, (UA_Byte*)input};
    UA_DecodeXmlOptions options;
    memset(&options, 0, sizeof(options));
    options.customTypes = o6_datatypes_global_chain();
    UA_StatusCode st = UA_decodeXml(&xml, data, expectedType, &options);
    if(st != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(st);
    PyObject *out = UA2PY(data, expectedType, NULL);
    UA_clear(data, expectedType);
    return out;
#endif
}

PyObject *
PY_decodeXmlValue(PyObject *_, PyObject *args) {
#ifndef UA_ENABLE_XML_ENCODING
    PyErr_SetString(PyExc_NotImplementedError,
                    "o6 was built without open62541 XML decoding support");
    return NULL;
#else
    PyObject *pyXml, *pyType, *pyIndexes;
    if(!PyArg_ParseTuple(args, "OOO", &pyXml, &pyType, &pyIndexes))
        return NULL;
    const UA_DataType *expectedType = PY2UAType((PyTypeObject*)pyType);
    if(!expectedType) {
        PyErr_SetString(PyExc_TypeError, "Expected an OPC UA datatype");
        return NULL;
    }
    char *input;
    Py_ssize_t inputLen;
    if(PyBytes_AsStringAndSize(pyXml, &input, &inputLen) < 0)
        return NULL;
    PyObject *indexes = PySequence_Fast(
        pyIndexes, "namespace indexes must be a sequence of integers");
    if(!indexes)
        return NULL;

    UA_NamespaceMapping mapping;
    memset(&mapping, 0, sizeof(mapping));
    Py_ssize_t uriCount = PySequence_Fast_GET_SIZE(indexes);
    for(Py_ssize_t uaIndex = 0; uaIndex < uriCount; uaIndex++) {
        PyObject *item = PySequence_Fast_GET_ITEM(indexes, uaIndex);
        unsigned long globalIndex = PyLong_AsUnsignedLong(item);
        if(globalIndex == (unsigned long)-1 && PyErr_Occurred())
            goto fail;
        PyObject *namespace = o6_namespace_module((UA_UInt16)globalIndex);
        if(!namespace || PyLong_Check(namespace)) {
            Py_XDECREF(namespace);
            PyErr_Format(PyExc_KeyError,
                         "namespace index is not registered: %lu", globalIndex);
            goto fail;
        }
        PyObject *uriObject = PyObject_GetAttrString(namespace, "uri");
        Py_DECREF(namespace);
        if(!uriObject)
            goto fail;
        const char *uri = PyUnicode_AsUTF8(uriObject);
        if(!uri) {
            Py_DECREF(uriObject);
            goto fail;
        }
        UA_String uaUri = {(size_t)strlen(uri), (UA_Byte*)(uintptr_t)uri};
        UA_StatusCode st = ua_extension_namespace_mapping_set(
            &mapping, uaUri, (UA_UInt16)globalIndex, (UA_UInt16)uaIndex);
        Py_DECREF(uriObject);
        if(st != UA_STATUSCODE_GOOD) {
            PyErr_StatusCode(st);
            goto fail;
        }
    }

    UA_Variant value;
    UA_Variant_init(&value);
    UA_ByteString xml = {(size_t)inputLen, (UA_Byte*)input};
    UA_DecodeXmlOptions options;
    memset(&options, 0, sizeof(options));
    options.namespaceMapping = &mapping;
    options.customTypes = o6_datatypes_global_chain();
    UA_StatusCode st = UA_decodeXml(&xml, &value, &UA_TYPES[UA_TYPES_VARIANT], &options);
    if(st != UA_STATUSCODE_GOOD) {
        PyErr_StatusCode(st);
        goto fail;
    }
    /* UA_decodeXml has already remapped XML-local namespace indexes into the
     * process-global indexes. Do not apply the same mapping a second time
     * while converting the decoded value to Python. */
    PyObject *out = UA2PY(&value, &UA_TYPES[UA_TYPES_VARIANT], NULL);
    if(out && expectedType->typeKind == UA_DATATYPEKIND_ENUM &&
       value.type == &UA_TYPES[UA_TYPES_INT32]) {
        if(UA_Variant_isScalar(&value)) {
            PyObject *typed = PyObject_CallOneArg(pyType, out);
            Py_DECREF(out);
            out = typed;
        } else {
            PyObject *items = PySequence_Fast(out, "decoded enum array is not iterable");
            PyObject *typed = items ? PyList_New(PySequence_Fast_GET_SIZE(items)) : NULL;
            if(typed) {
                for(Py_ssize_t i = 0; i < PySequence_Fast_GET_SIZE(items); i++) {
                    PyObject *member = PyObject_CallOneArg(
                        pyType, PySequence_Fast_GET_ITEM(items, i));
                    if(!member) {
                        Py_CLEAR(typed);
                        break;
                    }
                    PyList_SET_ITEM(typed, i, member);
                }
            }
            Py_XDECREF(items);
            Py_DECREF(out);
            out = typed;
        }
    }
    UA_Variant_clear(&value);
    UA_NamespaceMapping_clear(&mapping);
    Py_DECREF(indexes);
    return out;

fail:
    UA_NamespaceMapping_clear(&mapping);
    Py_DECREF(indexes);
    return NULL;
#endif
}

PyObject * PY_encodeJson(PyObject *_, PyObject *obj) {
    PyUATypeMatch m = PY2UAMatch(obj);
    const UA_DataType *uaType = m.uaType;
    if(!uaType || m.dimension != PYVALUEDIMENSION_SCALAR) {
        PyErr_SetString(PyExc_TypeError, "Expected a scalar OPC UA value");
        return NULL;
    }

    /* Make a "pure OPC UA" structure */
    char *data = UA_STACK_ALLOC(uaType->memSize);
    UA_init(data, uaType);
    PyObject *out = PY2UA(obj, data, uaType, NULL, NULL);
    if(!out)
        return out;

    /* Decode to a UA structure */
    UA_String bytes = UA_STRING_NULL;
    UA_StatusCode res = UA_encodeJson(data, uaType, &bytes, NULL);
    UA_clear(data, uaType);
    if(res != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(res);

    /* Move into the outbut bytes object */
    out = PyBytes_FromStringAndSize((char*)bytes.data, bytes.length);
    UA_String_clear(&bytes);
    return out;
}

PyObject * PY_decodeJson(PyObject *_, PyObject *args) {
    /* Unpack the arguments */
    PyObject *arg1, *arg2;
    if(!PyArg_ParseTuple(args, "OO", &arg1, &arg2))
        return NULL;

    /* Get the string argument */
    char *input;
    Py_ssize_t len;
    if(PyBytes_AsStringAndSize(arg1, &input, &len) < 0)
        return NULL;

    /* Get and validate the UA type. */
    PyTypeObject *type = (PyTypeObject*)arg2;
    const UA_DataType *uaType = PY2UAType(type);
    if(!uaType) {
        PyErr_SetString(PyExc_TypeError,
                        "Expected an OPC UA datatype for the second argument");
        return NULL;
    }

    /* Decode to a UA structure */
    char *data = UA_STACK_ALLOC(uaType->memSize);
    UA_ByteString encoding = {(size_t)len, (UA_Byte*)input};
    UA_StatusCode res = UA_decodeJson(&encoding, data, uaType, NULL);
    if(res != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(res);

    /* Convert to a Python object and return */
    PyObject *out = UA2PY(data, uaType, NULL);
    if(!out)
        UA_clear(data, uaType);
    return out;
}
