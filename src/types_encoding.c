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

#include "module.h"
#include "types_internal.h"

PyObject * PY_encodeBinary(PyObject *_, PyObject *obj) {
    PyUATypeMatch m = PY2UAMatch(obj);
    const UA_DataType *uaType = m.uaType;
    if(!uaType || m.dimension != PYVALUEDIMENSION_SCALAR) {
        PyErr_SetString(PyExc_TypeError, "Expected a scalar OPC UA value");
        return NULL;
    }

    /* Make a "pure OPC UA" structure */
    char data[uaType->memSize];
    UA_init(data, uaType);
    PyObject *out = PY2UA(obj, data, uaType);
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

    /* Get the UA type // TODO: Typecheck */
    PyTypeObject *type = (PyTypeObject*)arg2;
    const UA_DataType *uaType = PY2UAType(type);
    if(!uaType) {
        PyErr_SetString(PyExc_TypeError,
                        "Expected an OPC UA datatype for the second argument");
        return NULL;
    }

    /* Decode to a UA structure */
    char data[uaType->memSize];
    UA_ByteString encoding = {(size_t)len, (UA_Byte*)input};
    UA_StatusCode res = UA_decodeBinary(&encoding, data, uaType, NULL);
    if(res != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(res);

    /* Convert to a Python object and return */
    PyObject *out = UA2PY(data, uaType);
    if(!out)
        UA_clear(data, uaType);
    return out;
}

PyObject * PY_encodeJson(PyObject *_, PyObject *obj) {
    PyUATypeMatch m = PY2UAMatch(obj);
    const UA_DataType *uaType = m.uaType;
    if(!uaType || m.dimension != PYVALUEDIMENSION_SCALAR) {
        PyErr_SetString(PyExc_TypeError, "Expected a scalar OPC UA value");
        return NULL;
    }

    /* Make a "pure OPC UA" structure */
    char data[uaType->memSize];
    UA_init(data, uaType);
    PyObject *out = PY2UA(obj, data, uaType);
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

    /* Get the UA type // TODO: Typecheck */
    PyTypeObject *type = (PyTypeObject*)arg2;
    const UA_DataType *uaType = PY2UAType(type);
    if(!uaType) {
        PyErr_SetString(PyExc_TypeError,
                        "Expected an OPC UA datatype for the second argument");
        return NULL;
    }

    /* Decode to a UA structure */
    char data[uaType->memSize];
    UA_ByteString encoding = {(size_t)len, (UA_Byte*)input};
    UA_StatusCode res = UA_decodeJson(&encoding, data, uaType, NULL);
    if(res != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(res);

    /* Convert to a Python object and return */
    PyObject *out = UA2PY(data, uaType);
    if(!out)
        UA_clear(data, uaType);
    return out;
}
