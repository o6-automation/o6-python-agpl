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
#include "server.h"
#include "../module.h"

/* Helper: get config from PyServerConfig */
static UA_ServerConfig *get_config(PyServerConfig *self) {
    if (!self->py_server || !self->py_server->server)
        return NULL;
    return UA_Server_getConfig(self->py_server->server);
}

/* --- Logger --- */
static int
PyServerConfig_set_logger(PyServerConfig *self, PyObject *value, void *closure) {
    UA_ServerConfig *cfg = get_config(self);
    if (!cfg) {
        PyErr_SetString(PyExc_RuntimeError, "No UA_Server attached");
        return -1;
    }

    UA_Logger *logging = pyLogger(value);
    if (!logging) {
        PyErr_SetString(PyExc_RuntimeError, "Could not create the logger");
        return -1;
    }

    if (cfg->logging && cfg->logging->clear)
        cfg->logging->clear(cfg->logging);

    cfg->logging = logging;
    return 0;
}

/* --- Application Description --- */
static PyObject *
PyServerConfig_get_applicationDescription(PyServerConfig *self, void *closure) {
    UA_ServerConfig *cfg = get_config(self);
    if (!cfg) {
        PyErr_SetString(PyExc_RuntimeError, "No UA_Server attached");
        return NULL;
    }
    return UA2PY(&cfg->applicationDescription,
                 &UA_TYPES[UA_TYPES_APPLICATIONDESCRIPTION]);
}

static int
PyServerConfig_set_applicationDescription(PyServerConfig *self, PyObject *value,
                                          void *closure) {
    UA_ServerConfig *cfg = get_config(self);
    if (!cfg) {
        PyErr_SetString(PyExc_RuntimeError, "No UA_Server attached");
        return -1;
    }
    if (self->py_server->running) {
        PyErr_SetString(PyExc_RuntimeError,
                        "Cannot modify applicationDescription while server is running");
        return -1;
    }

    UA_ApplicationDescription tmp;
    PyObject *out = PY2UA(value, &tmp, &UA_TYPES[UA_TYPES_APPLICATIONDESCRIPTION]);
    if (!out)
        return -1;

    UA_ApplicationDescription_clear(&cfg->applicationDescription);
    cfg->applicationDescription = tmp;
    return 0;
}

/* --- Application URI --- */
static PyObject *
PyServerConfig_get_applicationUri(PyServerConfig *self, void *closure) {
    UA_ServerConfig *cfg = get_config(self);
    if (!cfg) {
        PyErr_SetString(PyExc_RuntimeError, "No UA_Server attached");
        return NULL;
    }
    if (cfg->applicationDescription.applicationUri.length == 0)
        return PyUnicode_FromString("");
    return PyUnicode_FromStringAndSize(
        (const char *)cfg->applicationDescription.applicationUri.data,
        cfg->applicationDescription.applicationUri.length);
}

static int
PyServerConfig_set_applicationUri(PyServerConfig *self, PyObject *value,
                                  void *closure) {
    UA_ServerConfig *cfg = get_config(self);
    if (!cfg) {
        PyErr_SetString(PyExc_RuntimeError, "No UA_Server attached");
        return -1;
    }
    if (self->py_server->running) {
        PyErr_SetString(PyExc_RuntimeError,
                        "Cannot modify application_uri while server is running");
        return -1;
    }
    if (!PyUnicode_Check(value)) {
        PyErr_SetString(PyExc_TypeError, "application_uri must be str");
        return -1;
    }
    const char *uri = PyUnicode_AsUTF8(value);
    UA_String_clear(&cfg->applicationDescription.applicationUri);
    cfg->applicationDescription.applicationUri = UA_STRING_ALLOC(uri);
    return 0;
}

/* --- Property Table --- */
static PyGetSetDef PyServerConfig_getset[] = {
    {"logger", NULL, (setter)PyServerConfig_set_logger, "logger", NULL},
    {"application_description",
     (getter)PyServerConfig_get_applicationDescription,
     (setter)PyServerConfig_set_applicationDescription,
     "application_description", NULL},
    {"application_uri",
     (getter)PyServerConfig_get_applicationUri,
     (setter)PyServerConfig_set_applicationUri,
     "application_uri", NULL},
    {NULL}
};

/* Helper: convert Python list of bytes to UA_ByteString array. */
static UA_ByteString *
pyList_to_ByteStringArray(PyObject *list, size_t *out_size) {
    if (!list || list == Py_None) {
        *out_size = 0;
        return NULL;
    }
    if (!PyList_Check(list)) {
        PyErr_SetString(PyExc_TypeError, "expected a list of bytes");
        return NULL;
    }
    Py_ssize_t n = PyList_Size(list);
    if (n == 0) {
        *out_size = 0;
        return NULL;
    }
    UA_ByteString *arr = (UA_ByteString *)UA_calloc((size_t)n, sizeof(UA_ByteString));
    if (!arr) {
        PyErr_NoMemory();
        return NULL;
    }
    for (Py_ssize_t i = 0; i < n; i++) {
        PyObject *item = PyList_GetItem(list, i);
        if (!PyBytes_Check(item)) {
            for (Py_ssize_t j = 0; j < i; j++)
                UA_ByteString_clear(&arr[j]);
            UA_free(arr);
            PyErr_SetString(PyExc_TypeError, "list entries must be bytes");
            return NULL;
        }
        char *buf;
        Py_ssize_t len;
        PyBytes_AsStringAndSize(item, &buf, &len);
        arr[i].length = (size_t)len;
        arr[i].data = (UA_Byte *)UA_malloc((size_t)len);
        if (!arr[i].data) {
            for (Py_ssize_t j = 0; j < i; j++)
                UA_ByteString_clear(&arr[j]);
            UA_free(arr);
            PyErr_NoMemory();
            return NULL;
        }
        memcpy(arr[i].data, buf, (size_t)len);
    }
    *out_size = (size_t)n;
    return arr;
}

static void
free_ByteStringArray(UA_ByteString *arr, size_t size) {
    if (!arr) return;
    for (size_t i = 0; i < size; i++)
        UA_ByteString_clear(&arr[i]);
    UA_free(arr);
}

/* --- set_encryption method --- */
static PyObject *
PyServerConfig_set_encryption(PyServerConfig *self,
                              PyObject *args, PyObject *kwds) {
#ifndef UA_ENABLE_ENCRYPTION
    PyErr_SetString(PyExc_RuntimeError,
                    "Encryption not available: open62541 was built without UA_ENABLE_ENCRYPTION");
    return NULL;
#else
    static char *kwlist[] = {"certificate", "private_key", "port",
                             "trust_list", "issuer_list", "revocation_list",
                             "secure_only", NULL};
    PyObject *py_cert = NULL, *py_key = NULL;
    int port = 4840;
    PyObject *py_trust = NULL, *py_issuer = NULL, *py_revoc = NULL;
    int secure_only = 0;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "SS|iOOOp", kwlist,
                                     &py_cert, &py_key, &port,
                                     &py_trust, &py_issuer, &py_revoc,
                                     &secure_only))
        return NULL;

    UA_ServerConfig *cfg = get_config(self);
    if (!cfg) {
        PyErr_SetString(PyExc_RuntimeError, "No UA_Server attached");
        return NULL;
    }
    if (self->py_server->running) {
        PyErr_SetString(PyExc_RuntimeError,
                        "Cannot configure encryption while server is running");
        return NULL;
    }

    char *cert_buf, *key_buf;
    Py_ssize_t cert_len, key_len;
    PyBytes_AsStringAndSize(py_cert, &cert_buf, &cert_len);
    PyBytes_AsStringAndSize(py_key, &key_buf, &key_len);

    UA_ByteString cert = {(size_t)cert_len, (UA_Byte *)cert_buf};
    UA_ByteString key = {(size_t)key_len, (UA_Byte *)key_buf};

    size_t trustSize = 0, issuerSize = 0, revocSize = 0;
    UA_ByteString *trustList = pyList_to_ByteStringArray(py_trust, &trustSize);
    if (PyErr_Occurred()) return NULL;
    UA_ByteString *issuerList = pyList_to_ByteStringArray(py_issuer, &issuerSize);
    if (PyErr_Occurred()) {
        free_ByteStringArray(trustList, trustSize);
        return NULL;
    }
    UA_ByteString *revocList = pyList_to_ByteStringArray(py_revoc, &revocSize);
    if (PyErr_Occurred()) {
        free_ByteStringArray(trustList, trustSize);
        free_ByteStringArray(issuerList, issuerSize);
        return NULL;
    }

    UA_StatusCode status;
    if (secure_only) {
        status = UA_ServerConfig_setDefaultWithSecureSecurityPolicies(
            cfg, (UA_UInt16)port, &cert, &key,
            trustList, trustSize,
            issuerList, issuerSize,
            revocList, revocSize);
    } else {
        status = UA_ServerConfig_setDefaultWithSecurityPolicies(
            cfg, (UA_UInt16)port, &cert, &key,
            trustList, trustSize,
            issuerList, issuerSize,
            revocList, revocSize);
    }

    free_ByteStringArray(trustList, trustSize);
    free_ByteStringArray(issuerList, issuerSize);
    free_ByteStringArray(revocList, revocSize);

    if (status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);

    Py_RETURN_NONE;
#endif
}

/* --- set_accept_all_certificates method --- */
static PyObject *
PyServerConfig_set_accept_all(PyServerConfig *self, PyObject *args) {
    UA_ServerConfig *cfg = get_config(self);
    if (!cfg) {
        PyErr_SetString(PyExc_RuntimeError, "No UA_Server attached");
        return NULL;
    }
    if (self->py_server->running) {
        PyErr_SetString(PyExc_RuntimeError,
                        "Cannot modify certificate policy while server is running");
        return NULL;
    }

    cfg->secureChannelPKI.clear(&cfg->secureChannelPKI);
    UA_CertificateGroup_AcceptAll(&cfg->secureChannelPKI);
    cfg->sessionPKI.clear(&cfg->sessionPKI);
    UA_CertificateGroup_AcceptAll(&cfg->sessionPKI);

    Py_RETURN_NONE;
}

/* --- set_history_database method --- */
static PyObject *
PyServerConfig_set_history_database(PyServerConfig *self,
                                    PyObject *args, PyObject *kwds) {
    static char *kwlist[] = {"max_nodes", NULL};
    int max_nodes = 10;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "|i", kwlist, &max_nodes))
        return NULL;

    UA_ServerConfig *cfg = get_config(self);
    if (!cfg) {
        PyErr_SetString(PyExc_RuntimeError, "No UA_Server attached");
        return NULL;
    }
    if (self->py_server->running) {
        PyErr_SetString(PyExc_RuntimeError,
                        "Cannot configure history database while server is running");
        return NULL;
    }
    if (self->py_server->hasHistoryDB) {
        PyErr_SetString(PyExc_RuntimeError,
                        "History database already configured");
        return NULL;
    }

    self->py_server->gathering =
        UA_HistoryDataGathering_Default((size_t)max_nodes);
    cfg->historyDatabase =
        UA_HistoryDatabase_default(self->py_server->gathering);
    self->py_server->hasHistoryDB = true;

    Py_RETURN_NONE;
}

static PyMethodDef PyServerConfig_methods[] = {
    {"set_encryption", (PyCFunction)PyServerConfig_set_encryption,
     METH_VARARGS | METH_KEYWORDS,
     "Configure security policies with certificate and private key.\n\n"
     "Args:\n"
     "    certificate: Server certificate as bytes (DER or PEM)\n"
     "    private_key: Private key as bytes (DER or PEM)\n"
     "    port: Server port (default: 4840)\n"
     "    trust_list: Optional list of trusted certificates (bytes)\n"
     "    issuer_list: Optional list of issuer certificates (bytes)\n"
     "    revocation_list: Optional list of CRLs (bytes)\n"
     "    secure_only: If True, do not offer unencrypted endpoints"},
    {"set_accept_all_certificates", (PyCFunction)PyServerConfig_set_accept_all,
     METH_NOARGS,
     "Accept all client certificates without validation (testing only)."},
    {"set_history_database", (PyCFunction)PyServerConfig_set_history_database,
     METH_VARARGS | METH_KEYWORDS,
     "Configure in-memory history database.\n\n"
     "Args:\n"
     "    max_nodes: Initial node-id store size (default: 10)"},
    {NULL, NULL, 0, NULL}
};

/* --- Type Lifecycle --- */
static void
PyServerConfig_dealloc(PyServerConfig *self) {
    Py_XDECREF(self->py_server);
    Py_TYPE(self)->tp_free((PyObject *)self);
}

static PyObject *
PyServerConfig_new(PyTypeObject *type, PyObject *args, PyObject *kwds) {
    PyServerConfig *self = (PyServerConfig *)type->tp_alloc(type, 0);
    self->py_server = NULL;
    return (PyObject *)self;
}

static int
PyServerConfig_init(PyServerConfig *self, PyObject *args, PyObject *kwds) {
    PyErr_SetString(PyExc_TypeError,
                    "ServerConfig cannot be instantiated directly");
    return -1;
}

PyTypeObject PyServerConfigType = {
    PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "o6.ServerConfig",
    .tp_basicsize = sizeof(PyServerConfig),
    .tp_flags = Py_TPFLAGS_DEFAULT,
    .tp_new = PyServerConfig_new,
    .tp_init = (initproc)PyServerConfig_init,
    .tp_dealloc = (destructor)PyServerConfig_dealloc,
    .tp_getset = PyServerConfig_getset,
    .tp_methods = PyServerConfig_methods,
};

PyObject *
PyServerConfig_New(PyServer *py_server) {
    PyServerConfig *obj =
        (PyServerConfig *)PyServerConfigType.tp_alloc(&PyServerConfigType, 0);
    if (!obj)
        return NULL;
    Py_INCREF(py_server);
    obj->py_server = py_server;
    return (PyObject *)obj;
}
