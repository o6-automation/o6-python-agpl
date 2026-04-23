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

#include "types_internal.h"
#include <open62541/util.h>

/* Global variables definitions */
PyObject *UUIDClass;
PyObject *UUIDModule;
PyObject *enumModule;
PyObject *enumMetaClass;

// Doesn't make a copy
UA_StatusCode
Unicode2String(PyObject *o, UA_String *s) {
    *s = UA_STRING_NULL;
    if(!PyUnicode_Check(o))
        return UA_STATUSCODE_BADINTERNALERROR;
    Py_ssize_t length = 0;
    const char *data = PyUnicode_AsUTF8AndSize(o, &length);
    if(!data || length < 0)
        return UA_STATUSCODE_BADINTERNALERROR;
    s->length = (size_t)length;
    s->data = (UA_Byte *)(uintptr_t)data;
    return UA_STATUSCODE_GOOD;
}

bool
listContains(PyObject *list, PyObject *o) {
    Py_ssize_t len = PyList_Size(list);
    if(len < 0)
        return false;
    for(Py_ssize_t i = 0; i < len; i++) {
        PyObject *item = PyList_GetItem(list, i);
        if(!item)
            return false;
        int equal = PyObject_RichCompareBool(item, o, Py_EQ);
        if(equal == 1)
            return true;
    }
    return false;
}

PyObject *
pyUA_repr(PyObject *self) {
    PyTypeObject *type = Py_TYPE(self);
    PyObject *str = PyObject_Str(self);
    if(!str)
        return NULL;
    PyObject *result = PyUnicode_FromFormat("%s(%S)", type->tp_name, str);
    Py_DECREF(str);
    return result;
}

PyObject *
pyUA_reprQuoted(PyObject *self) {
    PyTypeObject *type = Py_TYPE(self);
    PyObject *str = PyObject_Str(self);
    if(!str)
        return NULL;
    PyObject *result = PyUnicode_FromFormat("%s(%R)", type->tp_name, str);
    Py_DECREF(str);
    return result;
}

// TODO: This can be made more efficient than the "double copy" Py -> UA -> Py
PyObject *
pyUA_deepcopy(PyObject *self, PyObject *memo) {
    const UA_DataType *dt = PY2UAType(Py_TYPE(self));
    if(!dt) {
        PyErr_SetString(PyExc_TypeError, "Not a known OPC UA type");
        return NULL;
    }

    if(dt->memSize > 512) {
        PyErr_SetString(PyExc_TypeError, "Type requires too much stack memory");
        return NULL;
    }

    char buf[512];
    PyObject *success = PY2UA(self, buf, dt);
    if(!success)
        return NULL;

    PyObject *out = UA2PY(buf, dt);
    UA_clear(buf, dt);
    if(!out)
        return NULL;

    // Handle memo. Normally this needs to be done earlier, but UA2PY does not
    // reference self or create cycles.
    PyObject *key = PyLong_FromVoidPtr(self);
    if(!key) {
        Py_DECREF(out);
        return NULL;
    }
    if(PyDict_SetItem(memo, key, (PyObject *)out) < 0) {
        Py_DECREF(key);
        Py_DECREF(out);
        return NULL;
    }
    Py_DECREF(key);

    return out;
}

#ifdef UA_ENABLE_SUBSCRIPTIONS_EVENTS
#ifdef UA_ENABLE_JSON_ENCODING

PyObject *
pyEventFilter_parse(PyObject *self, PyObject *args, PyObject *kwds) {
    const char *query = NULL;
    PyObject *pyLogObj = NULL;
    static char *kwlist[] = {"query", "logger", NULL};

    if(!PyArg_ParseTupleAndKeywords(args, kwds, "s|O", kwlist,
                                    &query, &pyLogObj))
        return NULL;

    UA_ByteString content = UA_String_fromChars(query);

    /* Set up parser options with optional Python logger for diagnostics */
    UA_EventFilterParserOptions opts;
    memset(&opts, 0, sizeof(opts));
    UA_Logger *logger = NULL;
    if(pyLogObj && pyLogObj != Py_None) {
        logger = pyLogger(pyLogObj);
        opts.logger = logger;
    }

    UA_EventFilter filter;
    UA_EventFilter_init(&filter);
    UA_StatusCode res = UA_EventFilter_parse(&filter, content, &opts);

    UA_String_clear(&content);
    if(logger) {
        if(logger->clear)
            logger->clear(logger);
        UA_free(logger);
    }

    if(res != UA_STATUSCODE_GOOD) {
        UA_EventFilter_clear(&filter);
        return PyErr_StatusCode(res);
    }

    PyObject *result = UA2PY(&filter, &UA_TYPES[UA_TYPES_EVENTFILTER]);
    UA_EventFilter_clear(&filter);
    return result;
}

#endif /* UA_ENABLE_JSON_ENCODING */
#endif /* UA_ENABLE_SUBSCRIPTIONS_EVENTS */


