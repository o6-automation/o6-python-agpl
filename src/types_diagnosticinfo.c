/* Copyright 2026 (c) o6 Automation GmbH */
/* DiagnosticInfo (OPC UA builtin type, UA_DATATYPEKIND_DIAGNOSTICINFO = 24) */

#include <open62541/types.h>
#define NO_IMPORT_ARRAY
#include "types_internal.h"

#include <numpy/arrayobject.h>
#include <numpy/arrayscalars.h>
#include <stdio.h>

/* --- Getters ------------------------------------------------------------ */

static PyObject *
pyUADiagnosticInfo_get_symbolicId(PyObject *self, void *closure) {
    PyUADiagnosticInfo *di = (PyUADiagnosticInfo*)self;
    if(!di->di.hasSymbolicId)
        Py_RETURN_NONE;
    return PyLong_FromLong(di->di.symbolicId);
}

static int
pyUADiagnosticInfo_set_symbolicId(PyObject *self, PyObject *value, void *closure) {
    PyUADiagnosticInfo *di = (PyUADiagnosticInfo*)self;
    if(value == Py_None) {
        di->di.hasSymbolicId = false;
        di->di.symbolicId = 0;
        return 0;
    }
    long v = PyLong_AsLong(value);
    if(v == -1 && PyErr_Occurred())
        return -1;
    di->di.symbolicId = (UA_Int32)v;
    di->di.hasSymbolicId = true;
    return 0;
}

static PyObject *
pyUADiagnosticInfo_get_namespaceUri(PyObject *self, void *closure) {
    PyUADiagnosticInfo *di = (PyUADiagnosticInfo*)self;
    if(!di->di.hasNamespaceUri)
        Py_RETURN_NONE;
    return PyLong_FromLong(di->di.namespaceUri);
}

static int
pyUADiagnosticInfo_set_namespaceUri(PyObject *self, PyObject *value, void *closure) {
    PyUADiagnosticInfo *di = (PyUADiagnosticInfo*)self;
    if(value == Py_None) {
        di->di.hasNamespaceUri = false;
        di->di.namespaceUri = 0;
        return 0;
    }
    long v = PyLong_AsLong(value);
    if(v == -1 && PyErr_Occurred())
        return -1;
    di->di.namespaceUri = (UA_Int32)v;
    di->di.hasNamespaceUri = true;
    return 0;
}

static PyObject *
pyUADiagnosticInfo_get_localizedText(PyObject *self, void *closure) {
    PyUADiagnosticInfo *di = (PyUADiagnosticInfo*)self;
    if(!di->di.hasLocalizedText)
        Py_RETURN_NONE;
    return PyLong_FromLong(di->di.localizedText);
}

static int
pyUADiagnosticInfo_set_localizedText(PyObject *self, PyObject *value, void *closure) {
    PyUADiagnosticInfo *di = (PyUADiagnosticInfo*)self;
    if(value == Py_None) {
        di->di.hasLocalizedText = false;
        di->di.localizedText = 0;
        return 0;
    }
    long v = PyLong_AsLong(value);
    if(v == -1 && PyErr_Occurred())
        return -1;
    di->di.localizedText = (UA_Int32)v;
    di->di.hasLocalizedText = true;
    return 0;
}

static PyObject *
pyUADiagnosticInfo_get_locale(PyObject *self, void *closure) {
    PyUADiagnosticInfo *di = (PyUADiagnosticInfo*)self;
    if(!di->di.hasLocale)
        Py_RETURN_NONE;
    return PyLong_FromLong(di->di.locale);
}

static int
pyUADiagnosticInfo_set_locale(PyObject *self, PyObject *value, void *closure) {
    PyUADiagnosticInfo *di = (PyUADiagnosticInfo*)self;
    if(value == Py_None) {
        di->di.hasLocale = false;
        di->di.locale = 0;
        return 0;
    }
    long v = PyLong_AsLong(value);
    if(v == -1 && PyErr_Occurred())
        return -1;
    di->di.locale = (UA_Int32)v;
    di->di.hasLocale = true;
    return 0;
}

static PyObject *
pyUADiagnosticInfo_get_additionalInfo(PyObject *self, void *closure) {
    PyUADiagnosticInfo *di = (PyUADiagnosticInfo*)self;
    if(!di->di.hasAdditionalInfo)
        Py_RETURN_NONE;
    return PyUnicode_FromStringAndSize((char*)di->di.additionalInfo.data,
                                       di->di.additionalInfo.length);
}

static int
pyUADiagnosticInfo_set_additionalInfo(PyObject *self, PyObject *value, void *closure) {
    PyUADiagnosticInfo *di = (PyUADiagnosticInfo*)self;
    if(value == Py_None) {
        di->di.hasAdditionalInfo = false;
        UA_String_clear(&di->di.additionalInfo);
        di->di.additionalInfo = UA_STRING_NULL;
        return 0;
    }
    UA_String str;
    UA_StatusCode sc = Unicode2String(value, &str);
    if(sc != UA_STATUSCODE_GOOD) {
        PyErr_SetString(PyExc_TypeError, "additionalInfo must be a string");
        return -1;
    }
    UA_String_copy(&str, &di->di.additionalInfo);
    di->di.hasAdditionalInfo = true;
    return 0;
}

static PyObject *
pyUADiagnosticInfo_get_innerStatusCode(PyObject *self, void *closure) {
    PyUADiagnosticInfo *di = (PyUADiagnosticInfo*)self;
    if(!di->di.hasInnerStatusCode) {
        UA_StatusCode good = UA_STATUSCODE_GOOD;
        return UA2PY(&good, &UA_TYPES[UA_TYPES_STATUSCODE], NULL);
    }
    return UA2PY(&di->di.innerStatusCode, &UA_TYPES[UA_TYPES_STATUSCODE], NULL);
}

static int
pyUADiagnosticInfo_set_innerStatusCode(PyObject *self, PyObject *value, void *closure) {
    PyUADiagnosticInfo *di = (PyUADiagnosticInfo*)self;
    if(value == Py_None) {
        di->di.hasInnerStatusCode = false;
        di->di.innerStatusCode = UA_STATUSCODE_GOOD;
        return 0;
    }
    PyObject *out = PY2UA_statuscode(value, &di->di.innerStatusCode);
    if(out)
        di->di.hasInnerStatusCode = true;
    return (out) ? 0 : -1;
}

static PyObject *
pyUADiagnosticInfo_get_innerDiagnosticInfo(PyObject *self, void *closure) {
    PyUADiagnosticInfo *di = (PyUADiagnosticInfo*)self;
    if(!di->di.hasInnerDiagnosticInfo || !di->di.innerDiagnosticInfo)
        Py_RETURN_NONE;
    return UA2PY(di->di.innerDiagnosticInfo, &UA_TYPES[UA_TYPES_DIAGNOSTICINFO], NULL);
}

static int
pyUADiagnosticInfo_set_innerDiagnosticInfo(PyObject *self, PyObject *value, void *closure) {
    PyUADiagnosticInfo *di = (PyUADiagnosticInfo*)self;
    if(value == Py_None) {
        if(di->di.hasInnerDiagnosticInfo && di->di.innerDiagnosticInfo) {
            UA_DiagnosticInfo_clear(di->di.innerDiagnosticInfo);
            UA_free(di->di.innerDiagnosticInfo);
            di->di.innerDiagnosticInfo = NULL;
        }
        di->di.hasInnerDiagnosticInfo = false;
        return 0;
    }
    if(Py_TYPE(value) != pyUADiagnosticInfo) {
        PyErr_SetString(PyExc_TypeError, "innerDiagnosticInfo must be a DiagnosticInfo");
        return -1;
    }
    UA_DiagnosticInfo *src = &((PyUADiagnosticInfo*)value)->di;
    if(!di->di.innerDiagnosticInfo) {
        di->di.innerDiagnosticInfo = (UA_DiagnosticInfo*)UA_calloc(1, sizeof(UA_DiagnosticInfo));
        if(!di->di.innerDiagnosticInfo) {
            PyErr_NoMemory();
            return -1;
        }
    } else {
        UA_DiagnosticInfo_clear(di->di.innerDiagnosticInfo);
    }
    UA_StatusCode res = UA_DiagnosticInfo_copy(src, di->di.innerDiagnosticInfo);
    if(res != UA_STATUSCODE_GOOD) {
        PyErr_SetString(PyExc_RuntimeError, "Failed to copy inner DiagnosticInfo");
        return -1;
    }
    di->di.hasInnerDiagnosticInfo = true;
    return 0;
}

PyGetSetDef pyUADiagnosticInfo_getsets[] = {
    {"symbolicId",          pyUADiagnosticInfo_get_symbolicId,          pyUADiagnosticInfo_set_symbolicId,          "Symbolic ID",          NULL},
    {"namespaceUri",        pyUADiagnosticInfo_get_namespaceUri,        pyUADiagnosticInfo_set_namespaceUri,        "Namespace URI",        NULL},
    {"localizedText",       pyUADiagnosticInfo_get_localizedText,       pyUADiagnosticInfo_set_localizedText,       "Localized text",       NULL},
    {"locale",              pyUADiagnosticInfo_get_locale,              pyUADiagnosticInfo_set_locale,              "Locale",               NULL},
    {"additionalInfo",      pyUADiagnosticInfo_get_additionalInfo,      pyUADiagnosticInfo_set_additionalInfo,      "Additional info",      NULL},
    {"innerStatusCode",     pyUADiagnosticInfo_get_innerStatusCode,     pyUADiagnosticInfo_set_innerStatusCode,     "Inner status code",    NULL},
    {"innerDiagnosticInfo", pyUADiagnosticInfo_get_innerDiagnosticInfo, pyUADiagnosticInfo_set_innerDiagnosticInfo, "Inner diagnostic info",NULL},
    {NULL}
};

/* --- str / repr --------------------------------------------------------- */

static PyObject *
pyUADiagnosticInfo_str_payload(PyObject *self) {
    (void)self;
    PyObject *parts = PyList_New(0);
    if(!parts)
        return NULL;

    const char *names[] = {
        "symbolicId", "namespaceUri", "localizedText", "locale",
        "additionalInfo", "innerStatusCode", "innerDiagnosticInfo"
    };
    PyObject *(*getters[])(PyObject*, void*) = {
        pyUADiagnosticInfo_get_symbolicId,
        pyUADiagnosticInfo_get_namespaceUri,
        pyUADiagnosticInfo_get_localizedText,
        pyUADiagnosticInfo_get_locale,
        pyUADiagnosticInfo_get_additionalInfo,
        pyUADiagnosticInfo_get_innerStatusCode,
        pyUADiagnosticInfo_get_innerDiagnosticInfo,
    };

    for(size_t i = 0; i < sizeof(names)/sizeof(names[0]); i++) {
        PyObject *val = getters[i](self, NULL);
        if(!val) {
            Py_DECREF(parts);
            return NULL;
        }
        if(val != Py_None) {
            PyObject *entry = PyUnicode_FromFormat("%s=%S", names[i], val);
            Py_DECREF(val);
            if(!entry) {
                Py_DECREF(parts);
                return NULL;
            }
            if(PyList_Append(parts, entry) < 0) {
                Py_DECREF(entry);
                Py_DECREF(parts);
                return NULL;
            }
            Py_DECREF(entry);
        } else {
            Py_DECREF(val);
        }
    }

    PyObject *sep = PyUnicode_FromString(", ");
    if(!sep) {
        Py_DECREF(parts);
        return NULL;
    }
    PyObject *joined = PyUnicode_Join(sep, parts);
    Py_DECREF(sep);
    Py_DECREF(parts);
    return joined;
}

PyObject *
pyUADiagnosticInfo_str(PyObject *self) {
    PyObject *inner = pyUADiagnosticInfo_str_payload(self);
    if(!inner)
        return NULL;
    PyObject *out = PyUnicode_FromFormat("DiagnosticInfo(%U)", inner);
    Py_DECREF(inner);
    return out;
}

PyObject *
pyUADiagnosticInfo_repr(PyObject *self) {
    PyObject *inner = pyUADiagnosticInfo_str_payload(self);
    if(!inner)
        return NULL;
    PyObject *out = PyUnicode_FromFormat("%s(%U)", Py_TYPE(self)->tp_name, inner);
    Py_DECREF(inner);
    return out;
}

PyObject *
pyUADiagnosticInfo_richcompare(PyObject *self, PyObject *other, int op) {
    if(op != Py_EQ && op != Py_NE)
        return Py_NewRef(Py_NotImplemented);
    UA_Boolean equal = false;
    if(Py_TYPE(self) == Py_TYPE(other)) {
        PyUADiagnosticInfo *a = (PyUADiagnosticInfo*)self;
        PyUADiagnosticInfo *b = (PyUADiagnosticInfo*)other;
        equal = UA_DiagnosticInfo_equal(&a->di, &b->di);
    }
    return PyBool_FromLong(op == Py_EQ ? equal : !equal);
}

/* --- init / dealloc / clear / traverse ---------------------------------- */

int
pyUADiagnosticInfo_init(PyObject *self, PyObject *args, PyObject *kwds) {
    PyUADiagnosticInfo *di = (PyUADiagnosticInfo*)self;
    UA_DiagnosticInfo_init(&di->di);

    Py_ssize_t argsSize = args ? PyTuple_Size(args) : 0;
    Py_ssize_t kwdsSize = kwds ? PyDict_Size(kwds) : 0;
    if(argsSize == 0 && kwdsSize == 0)
        return 0;

    static char *kwlist[] = {
        "symbolicId", "namespaceUri", "localizedText", "locale",
        "additionalInfo", "innerStatusCode", "innerDiagnosticInfo", NULL
    };
    PyObject *symbolicId = NULL, *namespaceUri = NULL, *localizedText = NULL,
             *locale = NULL, *additionalInfo = NULL, *innerStatusCode = NULL,
             *innerDiagnosticInfo = NULL;
    if(!PyArg_ParseTupleAndKeywords(args, kwds, "|OOOOOOO", kwlist,
                                   &symbolicId, &namespaceUri, &localizedText,
                                   &locale, &additionalInfo, &innerStatusCode,
                                   &innerDiagnosticInfo))
        return -1;

    if(symbolicId && pyUADiagnosticInfo_set_symbolicId(self, symbolicId, NULL) < 0)
        return -1;
    if(namespaceUri && pyUADiagnosticInfo_set_namespaceUri(self, namespaceUri, NULL) < 0)
        return -1;
    if(localizedText && pyUADiagnosticInfo_set_localizedText(self, localizedText, NULL) < 0)
        return -1;
    if(locale && pyUADiagnosticInfo_set_locale(self, locale, NULL) < 0)
        return -1;
    if(additionalInfo && pyUADiagnosticInfo_set_additionalInfo(self, additionalInfo, NULL) < 0)
        return -1;
    if(innerStatusCode && pyUADiagnosticInfo_set_innerStatusCode(self, innerStatusCode, NULL) < 0)
        return -1;
    if(innerDiagnosticInfo && pyUADiagnosticInfo_set_innerDiagnosticInfo(self, innerDiagnosticInfo, NULL) < 0)
        return -1;

    return 0;
}

void
pyUADiagnosticInfo_dealloc(PyObject *self) {
    PyUADiagnosticInfo *di = (PyUADiagnosticInfo*)self;
    UA_DiagnosticInfo_clear(&di->di);
    Py_TYPE(self)->tp_free(self);
}

int
pyUADiagnosticInfo_traverse(PyObject *self, visitproc visit, void *arg) {
    (void)self; (void)visit; (void)arg;
    return 0;
}

int
pyUADiagnosticInfo_clear(PyObject *self) {
    PyUADiagnosticInfo *di = (PyUADiagnosticInfo*)self;
    UA_DiagnosticInfo_clear(&di->di);
    return 0;
}

/* --- PY2UA / UA2PY helpers (called from types_convert.c) ---------------- */

PyObject *
PY2UA_diagnosticinfo(PyObject *obj, UA_DiagnosticInfo *p) {
    if(obj == Py_None) {
        UA_DiagnosticInfo_init(p);
        return Py_None;
    }
    if(Py_TYPE(obj) != pyUADiagnosticInfo) {
        PyErr_Format(PyExc_TypeError,
                     "Expected DiagnosticInfo object, got %s",
                     Py_TYPE(obj)->tp_name);
        return NULL;
    }
    UA_StatusCode res = UA_DiagnosticInfo_copy(&((PyUADiagnosticInfo*)obj)->di, p);
    if(res != UA_STATUSCODE_GOOD) {
        PyErr_SetString(PyExc_RuntimeError, "Failed to copy DiagnosticInfo");
        return NULL;
    }
    return Py_None;
}
