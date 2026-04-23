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
#include "client/client.h"
#ifndef O6_NO_SERVER
#include "server/server.h"
#endif
#include <datetime.h>
#include <numpy/arrayobject.h>

PyObject *pyStatusCodeException;

/************************/
/* StatusCode Exception */
/************************/

PyObject *pyExc_StatusCode;

typedef struct {
    PyBaseExceptionObject base;
    UA_StatusCode status;
} PyStatusCodeException;

static int
PyStatusCodeException_init(PyStatusCodeException *self, PyObject *args, PyObject *kwds) {
    unsigned long status;
    if(!PyArg_ParseTuple(args, "k", &status))
        return -1;
    self->status = (UA_StatusCode)status;
    return 0;
}

static PyObject *
PyStatusCodeException_repr(PyStatusCodeException *self) {
    return PyUnicode_FromFormat("<StatusCodeError code=0x%02x, symbol=%s>",
                                self->status, UA_StatusCode_name(self->status));
}

PyObject *
pyStatusCodeError_get_code(PyStatusCodeException *self, void *closure) {
    return PyLong_FromUnsignedLong(self->status);
}

PyObject *
pyStatusCodeError_get_name(PyStatusCodeException *self, void *closure) {
    return PyUnicode_FromString(UA_StatusCode_name(self->status));
}

PyGetSetDef pyStatusCodeError_getsets[] = {
    {"code", (getter)pyStatusCodeError_get_code, NULL, "Integer code", NULL},
    {"symbol", (getter)pyStatusCodeError_get_name, NULL, "Human-readable description", NULL},
    {NULL}
};

static PyTypeObject PyStatusCodeErrorType = {
    PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "o6.StatusCodeError",
    .tp_basicsize = sizeof(PyStatusCodeException),
    .tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,
    .tp_doc = "Exception carrying an OPC UA StatusCode",
    //.tp_base = (PyTypeObject *)PyExc_Exception,
    .tp_init = (initproc)PyStatusCodeException_init,
    .tp_repr = (reprfunc)PyStatusCodeException_repr,
    .tp_getset = pyStatusCodeError_getsets
};

PyObject * PyErr_StatusCode(UA_StatusCode err) {
    PyErr_SetObject((PyObject*)&PyStatusCodeErrorType, PyLong_FromUnsignedLong(err));
    return NULL;
}

/****************************/
/* Certificate Generation   */
/****************************/

#ifdef UA_ENABLE_ENCRYPTION

static PyObject *
py_create_certificate(PyObject *self, PyObject *args, PyObject *kwds) {
    static char *kwlist[] = {"subject", "alt_names", "expires_in_days",
                             "key_size", "fmt", NULL};
    PyObject *py_subject = NULL;
    PyObject *py_alt_names = NULL;
    int expires_in_days = 365;
    int key_size = 2048;
    const char *fmt = "DER";

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "OO|iis", kwlist,
                                     &py_subject, &py_alt_names,
                                     &expires_in_days, &key_size, &fmt))
        return NULL;

    if (!PyList_Check(py_subject)) {
        PyErr_SetString(PyExc_TypeError, "subject must be a list of strings");
        return NULL;
    }
    if (!PyList_Check(py_alt_names)) {
        PyErr_SetString(PyExc_TypeError, "alt_names must be a list of strings");
        return NULL;
    }

    Py_ssize_t subject_size = PyList_Size(py_subject);
    UA_String *subject = (UA_String *)UA_calloc((size_t)subject_size, sizeof(UA_String));
    if (!subject)
        return PyErr_NoMemory();

    for (Py_ssize_t i = 0; i < subject_size; i++) {
        PyObject *item = PyList_GetItem(py_subject, i);
        if (!PyUnicode_Check(item)) {
            UA_free(subject);
            PyErr_SetString(PyExc_TypeError, "subject entries must be strings");
            return NULL;
        }
        const char *s = PyUnicode_AsUTF8(item);
        subject[i] = UA_STRING((char *)(uintptr_t)s);
    }

    Py_ssize_t alt_size = PyList_Size(py_alt_names);
    UA_String *alt_names = (UA_String *)UA_calloc((size_t)alt_size, sizeof(UA_String));
    if (!alt_names) {
        UA_free(subject);
        return PyErr_NoMemory();
    }

    for (Py_ssize_t i = 0; i < alt_size; i++) {
        PyObject *item = PyList_GetItem(py_alt_names, i);
        if (!PyUnicode_Check(item)) {
            UA_free(subject);
            UA_free(alt_names);
            PyErr_SetString(PyExc_TypeError, "alt_names entries must be strings");
            return NULL;
        }
        const char *s = PyUnicode_AsUTF8(item);
        alt_names[i] = UA_STRING((char *)(uintptr_t)s);
    }

    UA_CertificateFormat certFmt = UA_CERTIFICATEFORMAT_DER;
    if (strcmp(fmt, "PEM") == 0)
        certFmt = UA_CERTIFICATEFORMAT_PEM;
    else if (strcmp(fmt, "DER") != 0) {
        UA_free(subject);
        UA_free(alt_names);
        PyErr_SetString(PyExc_ValueError, "fmt must be 'DER' or 'PEM'");
        return NULL;
    }

    UA_KeyValueMap *kvm = UA_KeyValueMap_new();
    UA_UInt16 days = (UA_UInt16)expires_in_days;
    UA_KeyValueMap_setScalar(kvm, UA_QUALIFIEDNAME(0, "expires-in-days"),
                             (void *)&days, &UA_TYPES[UA_TYPES_UINT16]);
    UA_UInt16 bits = (UA_UInt16)key_size;
    UA_KeyValueMap_setScalar(kvm, UA_QUALIFIEDNAME(0, "key-size-bits"),
                             (void *)&bits, &UA_TYPES[UA_TYPES_UINT16]);

    UA_ByteString privateKey = UA_BYTESTRING_NULL;
    UA_ByteString certificate = UA_BYTESTRING_NULL;

    UA_StatusCode status = UA_CreateCertificate(
        UA_Log_Stdout, subject, (size_t)subject_size,
        alt_names, (size_t)alt_size,
        certFmt, kvm, &privateKey, &certificate);

    UA_KeyValueMap_delete(kvm);
    UA_free(subject);
    UA_free(alt_names);

    if (status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);

    PyObject *py_key = PyBytes_FromStringAndSize(
        (const char *)privateKey.data, (Py_ssize_t)privateKey.length);
    PyObject *py_cert = PyBytes_FromStringAndSize(
        (const char *)certificate.data, (Py_ssize_t)certificate.length);

    UA_ByteString_clear(&privateKey);
    UA_ByteString_clear(&certificate);

    if (!py_key || !py_cert) {
        Py_XDECREF(py_key);
        Py_XDECREF(py_cert);
        return NULL;
    }

    PyObject *result = PyTuple_Pack(2, py_key, py_cert);
    Py_DECREF(py_key);
    Py_DECREF(py_cert);
    return result;
}

#endif /* UA_ENABLE_ENCRYPTION */

static PyObject *
py_encryption_available(PyObject *self, PyObject *args) {
#ifdef UA_ENABLE_ENCRYPTION
    Py_RETURN_TRUE;
#else
    Py_RETURN_FALSE;
#endif
}

static PyMethodDef module_methods[] = {
#ifdef UA_ENABLE_ENCRYPTION
    {"create_certificate", (PyCFunction)py_create_certificate,
     METH_VARARGS | METH_KEYWORDS,
     "Create a self-signed certificate and private key.\n\n"
     "Args:\n"
     "    subject: List of subject fields, e.g. ['C=DE', 'O=MyOrg', 'CN=MyApp']\n"
     "    alt_names: List of SAN entries, e.g. ['DNS:localhost', 'URI:urn:my:app']\n"
     "    expires_in_days: Certificate validity (default: 365)\n"
     "    key_size: RSA key size in bits (default: 2048)\n"
     "    fmt: 'DER' or 'PEM' (default: 'DER')\n\n"
     "Returns:\n"
     "    Tuple of (private_key_bytes, certificate_bytes)"},
#endif
    {"encryption_available", py_encryption_available, METH_NOARGS,
     "Return True if encryption support is compiled in."},
    {"build_custom_data_types",
     (PyCFunction)py_buildCustomDataTypes,
     METH_VARARGS,
     "build_custom_data_types(descriptions[, namespace_name[, lookup_capsule]])\n\n"
     "Build UA_DataType entries and Python type objects from a list of\n"
     "StructureDescription / EnumDescription objects without linking them to\n"
     "any client or server.\n\n"
     "lookup_capsule: optional owner capsule from a previous call; its array\n"
     "is used as the lookup chain so the new types can reference already-built\n"
     "types (needed for multi-pass dependency ordering).\n\n"
     "Returns (capsule, [(NodeId, PyType), ...]).  The capsule must be stored\n"
     "(e.g. in a Descriptor) for the lifetime of the Python types.  Pass it\n"
     "to client.link_custom_data_types() / server.link_custom_data_types() to\n"
     "make the types available for encoding/decoding."},
    {NULL, NULL, 0, NULL}
};

/*************************/
/* Module Initialization */
/*************************/

static void mod_free(void *Py_UNUSED(module)) {
    Py_CLEAR(pyStatusCodeException);
    o6_clean_shutdown();
}

static struct PyModuleDef pymodule = {
    .m_base = PyModuleDef_HEAD_INIT,
    .m_name = "o6._o6",
    .m_doc = "OPC UA for Python",
    .m_size = -1, /* -1 if the module keeps state in global variables */
    .m_methods = module_methods,
    .m_slots = NULL,
    .m_traverse = NULL,
    .m_clear = NULL,
    .m_free = mod_free
};

static PyObject *mod = NULL;

PyMODINIT_FUNC PyInit__o6(void) {
    PyDateTime_IMPORT;
    import_array();

    /* Already initialized */
    if(mod) {
        Py_INCREF(mod);
        return mod;
    }

    /* Check and greet */
    if(!o6_check_greet())
        return NULL;

    /* Create module */
    mod = PyModule_Create(&pymodule);
    if(!mod)
        return NULL;

    /* Initialize event-loop PyType objects that are used at runtime by
     * UA_EventLoop_new_AsyncIO and UA_ConnectionManager_new_AsyncIO_TCP.
     * Must happen here (single-threaded module init) to avoid races when
     * multiple Client objects are created from different threads. */
    if(AsyncIOEventLoop_initTypes() < 0) {
        Py_DECREF(mod);
        mod = NULL;
        return NULL;
    }
    if(AsyncIOTCP_initTypes() < 0) {
        Py_DECREF(mod);
        mod = NULL;
        return NULL;
    }

    /* Add the StatusCodeError Exception */
    PyStatusCodeErrorType.tp_base = (PyTypeObject*)PyExc_Exception;
    if(PyType_Ready(&PyStatusCodeErrorType) < 0) {
        Py_DECREF(mod);
        mod = NULL;
        return NULL;
    }
    pyExc_StatusCode = (PyObject*)&PyStatusCodeErrorType;
    PyModule_AddObject(mod, "StatusCodeError", (PyObject *)&PyStatusCodeErrorType);

    /* Add types module */
    PyObject *types_mod = pyTypesModule();
    if(!types_mod) {
        Py_DECREF(mod);
        mod = NULL;
        return NULL;
    }
    PyModule_AddObject(mod, "types", types_mod);

    /* Add client module */
    if(client_enabled) {
        PyObject *client_mod = pyClientModule();
        if(!client_mod) {
            Py_DECREF(mod);
            mod = NULL;
            return NULL;
        }
        PyModule_AddObject(mod, "Client", client_mod);

        /* Add client config type */
        if(PyType_Ready(&PyClientConfigType) < 0) {
            Py_DECREF(mod);
            mod = NULL;
            return NULL;
        }
        PyModule_AddObject(mod, "ClientConfig", (PyObject*)&PyClientConfigType);
    }

    /* Add server module */
    if(server_enabled) {
#ifndef O6_NO_SERVER
        PyObject *server_mod = pyServerModule();
        if(!server_mod) {
            Py_DECREF(mod);
            mod = NULL;
            return NULL;
        }
        PyModule_AddObject(mod, "Server", server_mod);

        /* Add server config type */
        if(PyType_Ready(&PyServerConfigType) < 0) {
            Py_DECREF(mod);
            mod = NULL;
            return NULL;
        }
        PyModule_AddObject(mod, "ServerConfig", (PyObject*)&PyServerConfigType);
#endif
    }

    /* Add logging methods from logger.c */
    PyModule_AddFunctions(mod, pyLoggingMethods);

    /* Expose the open62541 threading level so Python can adapt */
    PyModule_AddIntConstant(mod, "MULTITHREADING", UA_MULTITHREADING);

    return mod;
}
