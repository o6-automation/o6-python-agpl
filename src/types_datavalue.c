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

static PyObject *
pyUADataValue_get_value(PyObject *self, void *closure) {
    PyUADataValue *dv = (PyUADataValue*)self;
    if(dv->value) {
        Py_INCREF(dv->value);
        return dv->value;
    }
    if(!dv->dv.hasValue || !dv->dv.value.type)
        return Py_None;
        
    dv->value = UA2PY(&dv->dv.value, &UA_TYPES[UA_TYPES_VARIANT]);
    if(!dv->value)
        return NULL;
    UA_Variant_init(&dv->dv.value);
    Py_INCREF(dv->value);
    return dv->value;
}

static int
pyUADataValue_set_value(PyObject *self, PyObject *value, void *closure) {
    PyUADataValue *dv = (PyUADataValue*)self;

    // If none, remove any preexisting value
    if(value == Py_None) {
        if(dv->value) {
            Py_DECREF(dv->value);
            dv->value = NULL;
        } else {
            UA_Variant_clear(&dv->dv.value);
        }
        dv->dv.hasValue = false;
        return 0;
    }

    // Check if the types can be used for the variant
    PyUATypeMatch match = PY2UAMatch(value);
    if(!match.uaType) {
        PyErr_SetString(PyExc_TypeError, "Cannot convert to an OPC UA Variant");
        return -1;
    }

    // Set a new value
    if(dv->value)
        Py_DECREF(dv->value);
    else
        UA_Variant_clear(&dv->dv.value);
    dv->value = value;
    Py_INCREF(value);
    dv->dv.hasValue = true;
    return 0;
}

static PyObject *
pyUADataValue_get_status(PyObject *self, void *closure) {
    PyUADataValue *dv = (PyUADataValue*)self;
    if(!dv->dv.hasStatus)
        return Py_None;
    return UA2PY(&dv->dv.status, &UA_TYPES[UA_TYPES_STATUSCODE]);
}

static int
pyUADataValue_set_status(PyObject *self, PyObject *value, void *closure) {
    PyUADataValue *dv = (PyUADataValue*)self;
    if(value == Py_None) {
        dv->dv.hasStatus = false;
        dv->dv.status = UA_STATUSCODE_GOOD;
        return 0;
    }
    PyObject *out = PY2UA_statuscode(value, &dv->dv.status);
    if(out)
        dv->dv.hasStatus = true;
    return (out) ? 0 : -1;
}

static int
pyUADataValue_set_server_timestamp(PyObject *self, PyObject *value, void *closure) {
    PyUADataValue *dv = (PyUADataValue*)self;
    if(value == Py_None) {
        dv->dv.hasServerTimestamp = false;
        dv->dv.serverTimestamp = 0;
        return 0;
    }
    PyObject *out = PY2UA_datetime(value, &dv->dv.serverTimestamp);
    if(out)
        dv->dv.hasServerTimestamp = true;
    return (out) ? 0: -1;
}

static PyObject*
pyUADataValue_get_server_timestamp(PyObject *self, void *closure) {
    PyUADataValue *dv = (PyUADataValue*)self;
    if(!dv->dv.hasServerTimestamp)
        Py_RETURN_NONE;
    return UA2PY(&dv->dv.serverTimestamp, &UA_TYPES[UA_TYPES_DATETIME]);
}

static int
pyUADataValue_set_server_picoseconds(PyObject *self, PyObject *value, void *closure) {
    PyUADataValue *dv = (PyUADataValue*)self;
    if(value == Py_None) {
        dv->dv.hasServerPicoseconds = false;
        dv->dv.serverPicoseconds = 0;
        return 0;
    }
    PyObject *out = PY2UA(value, &dv->dv.serverPicoseconds, &UA_TYPES[UA_TYPES_UINT16]);
    if(out)
        dv->dv.hasServerPicoseconds = true;
    return (out) ? 0: -1;
}

static PyObject*
pyUADataValue_get_server_picoseconds(PyObject *self, void *closure) {
    PyUADataValue *dv = (PyUADataValue*)self;
    if(!dv->dv.hasServerPicoseconds)
        Py_RETURN_NONE;
    return PyArray_Scalar(&dv->dv.serverPicoseconds, PyArray_DescrFromType(NPY_UINT16), NULL);
}

static PyObject*
pyUADataValue_get_source_timestamp(PyObject *self, void *closure) {
    PyUADataValue *dv = (PyUADataValue*)self;
    if(!dv->dv.hasSourceTimestamp)
        Py_RETURN_NONE;
    return UA2PY(&dv->dv.sourceTimestamp, &UA_TYPES[UA_TYPES_DATETIME]);
}

static int
pyUADataValue_set_source_timestamp(PyObject *self, PyObject *value, void *closure) {
    PyUADataValue *dv = (PyUADataValue*)self;
    if(value == Py_None) {
        dv->dv.hasSourceTimestamp = false;
        dv->dv.sourceTimestamp = 0;
        return 0;
    }
    PyObject *out = PY2UA_datetime(value, &dv->dv.sourceTimestamp);
    if(out)
        dv->dv.hasSourceTimestamp = true;
    return (out) ? 0: -1;
}

static PyObject *
pyUADataValue_get_source_picoseconds(PyObject *self, void *closure) {
    PyUADataValue *dv = (PyUADataValue*)self;
    if(!dv->dv.hasSourcePicoseconds)
        Py_RETURN_NONE;
    return PyArray_Scalar(&dv->dv.sourcePicoseconds, PyArray_DescrFromType(NPY_UINT16), NULL);
}

static int
pyUADataValue_set_source_picoseconds(PyObject *self, PyObject *value, void *closure) {
    PyUADataValue *dv = (PyUADataValue*)self;
    if(value == Py_None) {
        dv->dv.hasSourcePicoseconds = false;
        dv->dv.sourcePicoseconds = 0;
        return 0;
    }
    PyObject *out = PY2UA(value, &dv->dv.sourcePicoseconds, &UA_TYPES[UA_TYPES_UINT16]);
    if(out)
        dv->dv.hasSourcePicoseconds = true;
    return (out) ? 0: -1;
}

static PyObject *
pyUADataValue_str_payload(PyObject *self) {
    PyObject *parts = PyList_New(0);
    if(!parts)
        return NULL;

    // Add value
    PyObject *part;
    PyObject *value = pyUADataValue_get_value(self, NULL);
    if(value && (part = PyUnicode_FromFormat("value=%S, ", value))) {
        PyList_Append(parts, part);
        Py_DECREF(part);
    }
    Py_XDECREF(value);

    // Add status
    PyObject *status = pyUADataValue_get_status(self, NULL);
    if(status && (part = PyUnicode_FromFormat("status=%S, ", status))) {
        PyList_Append(parts, part);
        Py_DECREF(part);
    }
    Py_XDECREF(status);

    // Add source_timestamp
    PyObject *source_timestamp = pyUADataValue_get_source_timestamp(self, NULL);
    if(source_timestamp && (part = PyUnicode_FromFormat("source_timetamp=%S, ", source_timestamp))) {
        PyList_Append(parts, part);
        Py_DECREF(part);
    }
    Py_XDECREF(source_timestamp);

    // Add server_timestamp
    PyObject *server_timestamp = pyUADataValue_get_server_timestamp(self, NULL);
    if(server_timestamp && (part = PyUnicode_FromFormat("server_timetamp=%S, ", server_timestamp))) {
        PyList_Append(parts, part);
        Py_DECREF(part);
    }
    Py_XDECREF(server_timestamp);

    // Add source_picoseconds
    PyObject *source_picoseconds = pyUADataValue_get_source_picoseconds(self, NULL);
    if(source_picoseconds && (part = PyUnicode_FromFormat("source_picoseconds=%S, ", source_picoseconds))) {
        PyList_Append(parts, part);
        Py_DECREF(part);
    }
    Py_XDECREF(source_picoseconds);

    // Add server_picoseconds
    PyObject *server_picoseconds = pyUADataValue_get_server_picoseconds(self, NULL);
    if(server_picoseconds && (part = PyUnicode_FromFormat("server_picoseconds=%S", server_picoseconds))) {
        PyList_Append(parts, part);
        Py_DECREF(part);
    }
    Py_XDECREF(server_picoseconds);

    // Join parts
    PyObject *sep = PyUnicode_New(0,0);
    PyObject *result = PyUnicode_Join(sep, parts);
    Py_XDECREF(sep);
    Py_DECREF(parts);
    return result;
}

PyObject *
pyUADataValue_str(PyObject *self) {
    PyObject *str = pyUADataValue_str_payload(self);
    if(!str)
        return NULL;
    PyObject *result = PyUnicode_FromFormat("DataValue(%U)", str);
    Py_DECREF(str);
    return result;
}

PyObject *
pyUADataValue_repr(PyObject *self) {
    PyObject *str = pyUADataValue_str_payload(self);
    if(!str)
        return NULL;
    PyObject *result = PyUnicode_FromFormat("%s(%U)", Py_TYPE(self)->tp_name, str);
    Py_DECREF(str);
    return result;
}

void
pyUADataValue_dealloc(PyObject *self) {
    PyUADataValue *dv = (PyUADataValue*)self;
    UA_DataValue_clear(&dv->dv);
    Py_XDECREF(dv->value);
    pyUABuiltin_dealloc(self);
}

int
pyUADataValue_traverse(PyObject *self, visitproc visit, void *arg) {
    PyUADataValue *dv = (PyUADataValue*)self;
    Py_VISIT(dv->value);
    return 0;
}

int
pyUADataValue_clear(PyObject *self) {
    PyUADataValue *dv = (PyUADataValue*)self;
    Py_CLEAR(dv->value);
    return 0;
}

int
pyUADataValue_init(PyObject *self, PyObject *args, PyObject *kwds) {
    // Initialize
    PyUADataValue *dv = (PyUADataValue*)self;
    Py_XDECREF(dv->value);
    dv->value = NULL;
    UA_DataValue_clear(&dv->dv);
    
    // Parse arguments
    static char *kwlist[] = {"value", "status", "source_timestamp", "server_timestamp",
                             "source_picoseconds", "server_picoseconds", NULL};
    PyObject *value = NULL, *status = NULL, *source_timestamp = NULL,
        *server_timestamp = NULL, *source_picoseconds = NULL, *server_picoseconds = NULL;
    
    if(!PyArg_ParseTupleAndKeywords(args, kwds, "|OOOOOO", kwlist,
                                   &value, &status, &source_timestamp, &server_timestamp,
                                   &source_picoseconds, &server_picoseconds))
        return -1;
    
    // Set arguments
    if(value && pyUADataValue_set_value(self, value, NULL) < 0)
        return -1;
    
    if(status && pyUADataValue_set_status(self, status, NULL) < 0)
        return -1;
    
    if(source_timestamp && pyUADataValue_set_source_timestamp(self, source_timestamp, NULL) < 0)
        return -1;

    if(source_picoseconds && pyUADataValue_set_source_picoseconds(self, source_picoseconds, NULL) < 0)
        return -1;
    
    if(server_timestamp && pyUADataValue_set_server_timestamp(self, server_timestamp, NULL) < 0)
        return -1;

    if(server_picoseconds && pyUADataValue_set_server_picoseconds(self, server_picoseconds, NULL) < 0)
        return -1;
    
    return 0;
}

PyObject *
PY2UA_datavalue(PyObject *obj, UA_DataValue *datavalue) {
    if(obj == Py_None) {
        UA_DataValue_init(datavalue);
        return Py_None;
    }
    
    // Has to be a datavalue object
    if(Py_TYPE(obj) != pyUADataValue) {
        PyErr_Format(PyExc_TypeError, "Expected DataValue object, got %s", 
                     Py_TYPE(obj)->tp_name);
        return NULL;
    }

    PyObject *out = NULL;
    PyUADataValue *dv = (PyUADataValue*)obj;
    if(dv->value) {
        UA_DataValue tmp = dv->dv;
        out = PY2UA_variant(dv->value, &tmp.value);
        if(!out)
            return NULL;
        tmp.hasValue = true;
        *datavalue = tmp;
    } else {
        UA_StatusCode res = UA_DataValue_copy(&dv->dv, datavalue);
        if(res != UA_STATUSCODE_GOOD) {
            PyErr_SetString(PyExc_RuntimeError, "Failed to copy DataValue");
            return NULL;
        }
    }
    return Py_None;
}

PyGetSetDef pyUADataValue_getsets[] = {
    {"value", pyUADataValue_get_value, pyUADataValue_set_value, "The value as a Variant", NULL},
    {"status", pyUADataValue_get_status, pyUADataValue_set_status, "The status code", NULL},
    {"source_timestamp", pyUADataValue_get_source_timestamp,
                         pyUADataValue_set_source_timestamp, "Source timestamp", NULL},
    {"server_timestamp", pyUADataValue_get_server_timestamp,
                         pyUADataValue_set_server_timestamp, "Server timestamp", NULL},
    {"source_picoseconds", pyUADataValue_get_source_picoseconds,
                           pyUADataValue_set_source_picoseconds, "Source picoseconds", NULL},
    {"server_picoseconds", pyUADataValue_get_server_picoseconds,
                           pyUADataValue_set_server_picoseconds, "Server picoseconds", NULL},
    {NULL}
};
