/* Copyright 2026 (c) o6 Automation GmbH (Author: Andreas Ebner) */
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

#include <limits.h>

#include "server.h"
#include "../module.h"
#include "server_access_control.h"

/* Helper: get config from PyServerConfig */
static UA_ServerConfig *get_config(PyServerConfig *self) {
    if (!self->py_server || !self->py_server->server)
        return NULL;
    return UA_Server_getConfig(self->py_server->server);
}

static void
restore_o6_config_invariants(UA_ServerConfig *cfg) {
    cfg->copyMethodsOnInstances = true;
#ifdef UA_ENABLE_PUBSUB
    cfg->pubsubEnabled = pubsub_enabled;
    cfg->pubSubConfig.componentLifecycleCallback =
        pubsub_enabled ? pyPubSubComponentLifecycle : NULL;
#ifdef UA_ENABLE_PUBSUB_INFORMATIONMODEL
    if(!pubsub_enabled)
        cfg->pubSubConfig.enableInformationModelMethods = false;
#endif
#endif
}

/* --- Logger --- */
static int
PyServerConfig_set_logger(PyServerConfig *self, PyObject *value, void *closure) {
    if(!value) {
        PyErr_SetString(PyExc_AttributeError, "Cannot delete configuration properties");
        return -1;
    }
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
    UA_ApplicationDescription copy;
    UA_ApplicationDescription_init(&copy);
    UA_StatusCode status = UA_ApplicationDescription_copy(
        &cfg->applicationDescription, &copy);
    if(status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);
    PyObject *result = UA2PY(
        &copy, &UA_TYPES[UA_TYPES_APPLICATIONDESCRIPTION],
        &self->py_server->nsMapPy2UA);
    UA_ApplicationDescription_clear(&copy);
    return result;
}

static int
PyServerConfig_set_applicationDescription(PyServerConfig *self, PyObject *value,
                                          void *closure) {
    if(!value) {
        PyErr_SetString(PyExc_AttributeError, "Cannot delete configuration properties");
        return -1;
    }
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
    PyObject *out = PY2UA(
        value, &tmp, &UA_TYPES[UA_TYPES_APPLICATIONDESCRIPTION],
        &self->py_server->nsMapPy2UA, cfg->customDataTypes);
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
    if(!value) {
        PyErr_SetString(PyExc_AttributeError, "Cannot delete configuration properties");
        return -1;
    }
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

static PyObject *
PyServerConfig_get_allow_none_policy_password(PyServerConfig *self, void *closure) {
    UA_ServerConfig *cfg = get_config(self);
    if (!cfg) {
        PyErr_SetString(PyExc_RuntimeError, "No UA_Server attached");
        return NULL;
    }
    return PyBool_FromLong(cfg->allowNonePolicyPassword);
}

static int
PyServerConfig_set_allow_none_policy_password(PyServerConfig *self,
                                               PyObject *value, void *closure) {
    if(!value) {
        PyErr_SetString(PyExc_AttributeError, "Cannot delete configuration properties");
        return -1;
    }
    UA_ServerConfig *cfg = get_config(self);
    if (!cfg) {
        PyErr_SetString(PyExc_RuntimeError, "No UA_Server attached");
        return -1;
    }
    if (self->py_server->running) {
        PyErr_SetString(PyExc_RuntimeError,
                        "Cannot modify allow_none_policy_password while server is running");
        return -1;
    }
    int enabled = PyObject_IsTrue(value);
    if (enabled < 0)
        return -1;
    cfg->allowNonePolicyPassword = enabled ? true : false;
    return 0;
}

static PyObject *
PyServerConfig_get_auditing_enabled(PyServerConfig *self, void *closure) {
    UA_ServerConfig *cfg = get_config(self);
    if (!cfg) {
        PyErr_SetString(PyExc_RuntimeError, "No UA_Server attached");
        return NULL;
    }
    return PyBool_FromLong(cfg->auditingEnabled);
}

static int
PyServerConfig_set_auditing_enabled(PyServerConfig *self, PyObject *value, void *closure) {
    if(!value) {
        PyErr_SetString(PyExc_AttributeError, "Cannot delete configuration properties");
        return -1;
    }
    UA_ServerConfig *cfg = get_config(self);
    if (!cfg) {
        PyErr_SetString(PyExc_RuntimeError, "No UA_Server attached");
        return -1;
    }
    int enabled = PyObject_IsTrue(value);
    if (enabled < 0)
        return -1;
    cfg->auditingEnabled = enabled ? true : false;
    return 0;
}

static PyObject *
PyServerConfig_get_application_type(PyServerConfig *self, void *closure) {
    UA_ServerConfig *cfg = get_config(self);
    if (!cfg) {
        PyErr_SetString(PyExc_RuntimeError, "No UA_Server attached");
        return NULL;
    }
    return PyLong_FromLong((long)cfg->applicationDescription.applicationType);
}

static int
PyServerConfig_set_application_type(PyServerConfig *self, PyObject *value, void *closure) {
    if(!value) {
        PyErr_SetString(PyExc_AttributeError, "Cannot delete configuration properties");
        return -1;
    }
    UA_ServerConfig *cfg = get_config(self);
    if (!cfg) {
        PyErr_SetString(PyExc_RuntimeError, "No UA_Server attached");
        return -1;
    }
    long type = PyLong_AsLong(value);
    if (type == -1 && PyErr_Occurred())
        return -1;
    if (type < UA_APPLICATIONTYPE_SERVER || type > UA_APPLICATIONTYPE_DISCOVERYSERVER) {
        PyErr_SetString(PyExc_ValueError, "applicationType must be an ns0 ApplicationType member");
        return -1;
    }
    cfg->applicationDescription.applicationType = (UA_ApplicationType)type;
    return 0;
}

static PyObject *
PyServerConfig_get_servers_on_network_enabled(PyServerConfig *self, void *closure) {
    UA_ServerConfig *cfg = get_config(self);
    if (!cfg) {
        PyErr_SetString(PyExc_RuntimeError, "No UA_Server attached");
        return NULL;
    }
    return PyBool_FromLong(cfg->serversOnNetworkEnabled);
}

static int
PyServerConfig_set_servers_on_network_enabled(PyServerConfig *self, PyObject *value,
                                              void *closure) {
    if(!value) {
        PyErr_SetString(PyExc_AttributeError, "Cannot delete configuration properties");
        return -1;
    }
    UA_ServerConfig *cfg = get_config(self);
    if (!cfg) {
        PyErr_SetString(PyExc_RuntimeError, "No UA_Server attached");
        return -1;
    }
    int enabled = PyObject_IsTrue(value);
    if (enabled < 0)
        return -1;
    cfg->serversOnNetworkEnabled = enabled ? true : false;
    return 0;
}

static PyObject *
PyServerConfig_get_history_enabled(PyServerConfig *self, void *closure) {
    (void)closure;
    if (!self->py_server)
        Py_RETURN_FALSE;
    return PyBool_FromLong(pyHistory_enabled(&self->py_server->history));
}

#ifdef UA_ENABLE_SUBSCRIPTIONS
/* --- Subscription Limits --- */
static PyObject *
PyServerConfig_get_max_subscriptions(PyServerConfig *self, void *closure) {
    UA_ServerConfig *cfg = get_config(self);
    if (!cfg) {
        PyErr_SetString(PyExc_RuntimeError, "No UA_Server attached");
        return NULL;
    }
    return PyLong_FromUnsignedLong(cfg->maxSubscriptions);
}

static int
PyServerConfig_set_max_subscriptions(PyServerConfig *self, PyObject *value, void *closure) {
    if(!value) {
        PyErr_SetString(PyExc_AttributeError, "Cannot delete configuration properties");
        return -1;
    }
    UA_ServerConfig *cfg = get_config(self);
    if (!cfg) {
        PyErr_SetString(PyExc_RuntimeError, "No UA_Server attached");
        return -1;
    }
    unsigned long long v = PyLong_AsUnsignedLongLong(value);
    if (v == (unsigned long long)-1 && PyErr_Occurred())
        return -1;
    if (v > UA_UINT32_MAX) {
        PyErr_SetString(PyExc_OverflowError, "maxSubscriptions must fit in UInt32");
        return -1;
    }
    cfg->maxSubscriptions = (UA_UInt32)v;
    return 0;
}

static PyObject *
PyServerConfig_get_max_subscriptions_per_session(PyServerConfig *self, void *closure) {
    UA_ServerConfig *cfg = get_config(self);
    if (!cfg) {
        PyErr_SetString(PyExc_RuntimeError, "No UA_Server attached");
        return NULL;
    }
    return PyLong_FromUnsignedLong(cfg->maxSubscriptionsPerSession);
}

static int
PyServerConfig_set_max_subscriptions_per_session(PyServerConfig *self, PyObject *value,
                                                  void *closure) {
    if(!value) {
        PyErr_SetString(PyExc_AttributeError, "Cannot delete configuration properties");
        return -1;
    }
    UA_ServerConfig *cfg = get_config(self);
    if (!cfg) {
        PyErr_SetString(PyExc_RuntimeError, "No UA_Server attached");
        return -1;
    }
    unsigned long long v = PyLong_AsUnsignedLongLong(value);
    if (v == (unsigned long long)-1 && PyErr_Occurred())
        return -1;
    if (v > UA_UINT32_MAX) {
        PyErr_SetString(PyExc_OverflowError, "maxSubscriptionsPerSession must fit in UInt32");
        return -1;
    }
    cfg->maxSubscriptionsPerSession = (UA_UInt32)v;
    return 0;
}
#endif /* UA_ENABLE_SUBSCRIPTIONS */

/* --- Property Table --- */
static PyGetSetDef PyServerConfig_getset[] = {
    {"logger", NULL, (setter)PyServerConfig_set_logger, "logger", NULL},
    {"applicationDescription",
     (getter)PyServerConfig_get_applicationDescription,
     (setter)PyServerConfig_set_applicationDescription,
     "applicationDescription", NULL},
    {"applicationUri",
     (getter)PyServerConfig_get_applicationUri,
     (setter)PyServerConfig_set_applicationUri,
     "applicationUri", NULL},
    {"allowNonePolicyPassword",
     (getter)PyServerConfig_get_allow_none_policy_password,
     (setter)PyServerConfig_set_allow_none_policy_password,
     "Allow password tokens on SecurityPolicy None endpoints", NULL},
    {"auditingEnabled",
     (getter)PyServerConfig_get_auditing_enabled,
     (setter)PyServerConfig_set_auditing_enabled,
     "Generate audit application notifications for security/management activity", NULL},
    {"applicationType",
     (getter)PyServerConfig_get_application_type,
     (setter)PyServerConfig_set_application_type,
     "Advertised ApplicationType (ns0 ApplicationType); DISCOVERYSERVER enables RegisterServer",
     NULL},
    {"serversOnNetworkEnabled",
     (getter)PyServerConfig_get_servers_on_network_enabled,
     (setter)PyServerConfig_set_servers_on_network_enabled,
     "Maintain the ServerOnNetwork record list (FindServersOnNetwork, mDNS discovery)", NULL},
    {"historyEnabled",
     (getter)PyServerConfig_get_history_enabled, NULL,
     "Whether setHistoryDatabase() has configured a history database", NULL},
#ifdef UA_ENABLE_SUBSCRIPTIONS
    {"maxSubscriptions",
     (getter)PyServerConfig_get_max_subscriptions,
     (setter)PyServerConfig_set_max_subscriptions,
     "Maximum number of subscriptions across all sessions; 0 = unlimited", NULL},
    {"maxSubscriptionsPerSession",
     (getter)PyServerConfig_get_max_subscriptions_per_session,
     (setter)PyServerConfig_set_max_subscriptions_per_session,
     "Maximum number of subscriptions per session; 0 = unlimited", NULL},
#endif /* UA_ENABLE_SUBSCRIPTIONS */
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
    static char *kwlist[] = {"certificate", "privateKey", "port",
                             "trustList", "issuerList", "revocationList",
                             "secureOnly", NULL};
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

    /* The open62541 default helpers restore feature defaults. Reapply the
     * o6 nodestore and entitlement invariants before returning to Python. */
    restore_o6_config_invariants(cfg);

    Py_RETURN_NONE;
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
    static char *kwlist[] = {"maxNodes", "capacity", "maxResponseSize",
                             "backend", NULL};
    int max_nodes = PYO6_HISTORY_MAX_NODES_DEFAULT;
    int capacity = INT_MIN;
    int max_response = PYO6_HISTORY_RESPONSE_DEFAULT;
    PyObject *py_backend = NULL;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "|iiiO", kwlist, &max_nodes,
                                     &capacity, &max_response, &py_backend))
        return NULL;
    if (py_backend == Py_None)
        py_backend = NULL;

    if (max_nodes <= 0 || max_response <= 0) {
        PyErr_SetString(PyExc_ValueError,
                        "maxNodes and maxResponseSize must be positive");
        return NULL;
    }
    if (py_backend == NULL && capacity != INT_MIN && capacity <= 0) {
        PyErr_SetString(PyExc_ValueError, "capacity must be positive");
        return NULL;
    }

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
    if (pyHistory_enabled(&self->py_server->history)) {
        PyErr_SetString(PyExc_RuntimeError,
                        "History database already configured");
        return NULL;
    }

    if (py_backend) {
        UA_StatusCode status = pyHistory_enableCustom(
            &self->py_server->history, self->py_server->server, cfg, py_backend,
            (PyObject *)self->py_server, (size_t)max_nodes, (size_t)max_response);
        if (status != UA_STATUSCODE_GOOD) {
            if (!PyErr_Occurred())
                return PyErr_StatusCode(status);
            return NULL;
        }
        Py_RETURN_NONE;
    }

    if (capacity == INT_MIN)
        capacity = PYO6_HISTORY_CAPACITY_DEFAULT;
    UA_StatusCode status =
        pyHistory_enable(&self->py_server->history, self->py_server->server, cfg,
                         (size_t)max_nodes, (size_t)capacity,
                         (size_t)max_response);
    if (status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);

    Py_RETURN_NONE;
}

static PyMethodDef PyServerConfig_methods[] = {
    {"setAccessControl", (PyCFunction)PyAccessControl_install,
     METH_O, "Install a Python AccessControl plugin before server startup."},
    {"setEncryption", (PyCFunction)PyServerConfig_set_encryption,
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
    {"setAcceptAllCertificates", (PyCFunction)PyServerConfig_set_accept_all,
     METH_NOARGS,
     "Accept all client certificates without validation (testing only)."},
    {"setHistoryDatabase", (PyCFunction)PyServerConfig_set_history_database,
     METH_VARARGS | METH_KEYWORDS,
     "Configure the in-memory history database.\n\n"
     "Every historized node gets a ring buffer of a fixed size, so one node\n"
     "costs capacity samples and never more. Must be called before start().\n\n"
     "Args:\n"
     "    maxNodes: Node table size to allocate up front. The table grows as\n"
     "        further nodes are historized, so this is a hint (default: 10)\n"
     "    capacity: Samples buffered per node, unless the node overrides it\n"
     "        (default: 100)\n"
     "    maxResponseSize: Values per HistoryRead response before the server\n"
     "        continues with a continuation point (default: 100)"},
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
