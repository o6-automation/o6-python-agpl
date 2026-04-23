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

#include "client.h"
#include "../utils.h"
#include <stddef.h>

// Property kind — drives the generic getter/setter logic
typedef enum {
    PROP_BOOL,
    PROP_UINT16,
    PROP_UINT32,
    PROP_UA_STRING, // UA_String mapped to Python str
    PROP_UA_STRING_ENDPOINT, // UA_String with endpoint-URI validation
    PROP_STRUCT, // Arbitrary UA struct via UA2PY/PY2UA
    PROP_ENUM_SECURITY_MODE // UA_MessageSecurityMode with range check
} ConfigPropKind;

// Descriptor for one config property
typedef struct {
    const char *name; // Python attribute name
    ConfigPropKind kind;
    size_t offset; // offsetof(UA_ClientConfig, field)
    int ua_type_index; // index into UA_TYPES[] for PROP_STRUCT
} ConfigPropDesc;

// ---- helpers ------------------------------------------------------------

static UA_ClientConfig *get_config(PyClientConfig *self) {
    if (!self->py_client || !self->py_client->client)
        return NULL;
    return UA_Client_getConfig(self->py_client->client);
}

static bool is_client_connected(UA_Client *client) {
    UA_SecureChannelState channelState;
    UA_SessionState sessionState;
    UA_StatusCode connectStatus;
    UA_Client_getState(client, &channelState, &sessionState, &connectStatus);
    return (channelState == UA_SECURECHANNELSTATE_OPEN ||
            sessionState == UA_SESSIONSTATE_ACTIVATED);
}

// Shared pre-check for all setters: config exists + not connected
static UA_ClientConfig *
setter_precheck(PyClientConfig *self, const char *name) {
    UA_ClientConfig *cfg = get_config(self);
    if (!cfg) {
        PyErr_SetString(PyExc_RuntimeError, "No UA_Client attached");
        return NULL;
    }
    if (is_client_connected(self->py_client->client)) {
        PyErr_Format(PyExc_RuntimeError,
                     "Cannot modify %s while client is connected", name);
        return NULL;
    }
    return cfg;
}

// ---- generic getter -----------------------------------------------------

static PyObject *
config_generic_get(PyClientConfig *self, void *closure) {
    const ConfigPropDesc *desc = (const ConfigPropDesc *)closure;
    UA_ClientConfig *cfg = get_config(self);
    if (!cfg) {
        PyErr_SetString(PyExc_RuntimeError, "No UA_Client attached");
        return NULL;
    }
    void *field = (char *)cfg + desc->offset;

    switch (desc->kind) {
    case PROP_BOOL:
        return PyBool_FromLong(*(UA_Boolean *)field);
    case PROP_UINT16:
        return PyLong_FromUnsignedLong(*(UA_UInt16 *)field);
    case PROP_UINT32:
        return PyLong_FromUnsignedLong(*(UA_UInt32 *)field);
    case PROP_ENUM_SECURITY_MODE:
        return PyLong_FromLong(*(UA_MessageSecurityMode *)field);
    case PROP_UA_STRING:
    case PROP_UA_STRING_ENDPOINT: {
        UA_String *s = (UA_String *)field;
        if (s->length == 0) {
            if (desc->kind == PROP_UA_STRING_ENDPOINT)
                Py_RETURN_NONE;
            return PyUnicode_FromString("");
        }
        return PyUnicode_FromStringAndSize((const char *)s->data, s->length);
    }
    case PROP_STRUCT:
        return UA2PY(field, &UA_TYPES[desc->ua_type_index]);
    }
    Py_RETURN_NONE; // unreachable
}

// ---- generic setter -----------------------------------------------------

static int
config_generic_set(PyClientConfig *self, PyObject *value, void *closure) {
    const ConfigPropDesc *desc = (const ConfigPropDesc *)closure;
    UA_ClientConfig *cfg = setter_precheck(self, desc->name);
    if (!cfg)
        return -1;
    void *field = (char *)cfg + desc->offset;

    switch (desc->kind) {
    case PROP_BOOL:
        if (!PyBool_Check(value)) {
            PyErr_Format(PyExc_TypeError, "%s must be bool", desc->name);
            return -1;
        }
        *(UA_Boolean *)field = PyObject_IsTrue(value);
        return 0;

    case PROP_UINT16:
        if (!PyLong_Check(value)) {
            PyErr_Format(PyExc_TypeError, "%s must be int", desc->name);
            return -1;
        }
        *(UA_UInt16 *)field = (UA_UInt16)PyLong_AsUnsignedLong(value);
        return 0;

    case PROP_UINT32:
        if (!PyLong_Check(value)) {
            PyErr_Format(PyExc_TypeError, "%s must be int", desc->name);
            return -1;
        }
        *(UA_UInt32 *)field = (UA_UInt32)PyLong_AsUnsignedLong(value);
        return 0;

    case PROP_ENUM_SECURITY_MODE: {
        if (!PyLong_Check(value)) {
            PyErr_Format(PyExc_TypeError, "%s must be int", desc->name);
            return -1;
        }
        long mode = PyLong_AsLong(value);
        if (mode < 0 || mode > UA_MESSAGESECURITYMODE_SIGNANDENCRYPT) {
            PyErr_Format(PyExc_ValueError, "Invalid %s value", desc->name);
            return -1;
        }
        *(UA_MessageSecurityMode *)field = (UA_MessageSecurityMode)mode;
        return 0;
    }

    case PROP_UA_STRING:
    case PROP_UA_STRING_ENDPOINT: {
        if (!PyUnicode_Check(value)) {
            PyErr_Format(PyExc_TypeError, "%s must be str", desc->name);
            return -1;
        }
        const char *str = PyUnicode_AsUTF8(value);
        if (!str)
            return -1;
        if (desc->kind == PROP_UA_STRING_ENDPOINT && !validate_endpoint_uri(str)) {
            PyErr_SetString(PyExc_ValueError,
                            "Invalid endpoint_url schema. "
                            "Expected format: opc.tcp://host:port[/path]");
            return -1;
        }
        UA_String_clear((UA_String *)field);
        *(UA_String *)field = UA_STRING_ALLOC(str);
        return 0;
    }

    case PROP_STRUCT: {
        const UA_DataType *type = &UA_TYPES[desc->ua_type_index];
        // Convert into a temporary, then swap on success
        void *tmp = UA_new(type);
        if (!tmp)
            return -1;
        PyObject *result = PY2UA(value, tmp, type);
        if (!result) {
            UA_delete(tmp, type);
            return -1;
        }
        Py_DECREF(result);
        UA_clear(field, type);
        memcpy(field, tmp, type->memSize);
        UA_free(tmp); // shell only — contents now owned by cfg
        return 0;
    }
    }
    return -1; // unreachable
}

// ---- property descriptors (one per config field) ------------------------

#define PROP(py_name, kind_val, field, ...) \
    static ConfigPropDesc prop_##field = { \
        py_name, kind_val, offsetof(UA_ClientConfig, field), __VA_ARGS__ \
    }

PROP("timeout",                       PROP_UINT32,                timeout,                    0);
PROP("no_session",                    PROP_BOOL,                  noSession,                  0);
PROP("endpoint_url",                  PROP_UA_STRING_ENDPOINT,    endpointUrl,                0);
PROP("security_mode",                 PROP_ENUM_SECURITY_MODE,    securityMode,               0);
PROP("security_policy_uri",           PROP_UA_STRING,             securityPolicyUri,          0);
PROP("no_reconnect",                  PROP_BOOL,                  noReconnect,                0);
PROP("no_new_session",                PROP_BOOL,                  noNewSession,               0);
PROP("application_uri",               PROP_UA_STRING,             applicationUri,             0);
PROP("tcp_reuse_addr",                PROP_BOOL,                  tcpReuseAddr,               0);
PROP("allow_none_policy_password",    PROP_BOOL,                  allowNonePolicyPassword,    0);
PROP("application_description",       PROP_STRUCT,                clientDescription,          UA_TYPES_APPLICATIONDESCRIPTION);
PROP("user_identity_token",           PROP_STRUCT,                userIdentityToken,          UA_TYPES_EXTENSIONOBJECT);
PROP("endpoint",                      PROP_STRUCT,                endpoint,                   UA_TYPES_ENDPOINTDESCRIPTION);
PROP("user_token_policy",             PROP_STRUCT,                userTokenPolicy,            UA_TYPES_USERTOKENPOLICY);
PROP("session_name",                  PROP_UA_STRING,             sessionName,                0);
PROP("secure_channel_life_time",      PROP_UINT32,                secureChannelLifeTime,      0);
PROP("requested_session_timeout",     PROP_UINT32,                requestedSessionTimeout,    0);
PROP("connectivity_check_interval",   PROP_UINT32,                connectivityCheckInterval,  0);
PROP("outstanding_publish_requests",  PROP_UINT16,                outStandingPublishRequests, 0);
PROP("auth_security_policy_uri",      PROP_UA_STRING,             authSecurityPolicyUri,      0);
#ifdef UA_ENABLE_ENCRYPTION
PROP("max_trust_list_size",           PROP_UINT32,                maxTrustListSize,           0);
PROP("max_rejected_list_size",        PROP_UINT32,                maxRejectedListSize,        0);
#endif

#undef PROP


/* Helper: build a Python list[str] from a UA_String array */
static PyObject *
ua_string_array_to_pylist(const UA_String *arr, size_t size) {
    PyObject *list = PyList_New((Py_ssize_t)size);
    if (!list) return NULL;
    for (size_t i = 0; i < size; i++) {
        PyObject *s = PyUnicode_FromStringAndSize(
            (const char *)arr[i].data, (Py_ssize_t)arr[i].length);
        if (!s) { Py_DECREF(list); return NULL; }
        PyList_SET_ITEM(list, (Py_ssize_t)i, s);
    }
    return list;
}

/* Helper: build a UA_String array from a Python list[str].  Returns NULL
 * (with PyErr set) on failure.  *out_size is set on success. */
static UA_String *
pylist_to_ua_string_array(PyObject *value, size_t *out_size) {
    if (!PyList_Check(value)) {
        PyErr_SetString(PyExc_TypeError, "value must be a list of str");
        return NULL;
    }
    Py_ssize_t n = PyList_GET_SIZE(value);
    if (n == 0) { *out_size = 0; return NULL; }
    UA_String *arr = (UA_String *)UA_calloc((size_t)n, sizeof(UA_String));
    if (!arr) { PyErr_NoMemory(); return NULL; }
    for (Py_ssize_t i = 0; i < n; i++) {
        PyObject *item = PyList_GET_ITEM(value, i);
        if (!PyUnicode_Check(item)) {
            for (Py_ssize_t j = 0; j < i; j++) UA_String_clear(&arr[j]);
            UA_free(arr);
            PyErr_SetString(PyExc_TypeError, "list entries must be str");
            return NULL;
        }
        const char *s = PyUnicode_AsUTF8(item);
        if (!s) {
            for (Py_ssize_t j = 0; j < i; j++) UA_String_clear(&arr[j]);
            UA_free(arr);
            return NULL;
        }
        arr[i] = UA_STRING_ALLOC(s);
    }
    *out_size = (size_t)n;
    return arr;
}

/* session_locale_ids — getter */
static PyObject *
PyClientConfig_get_session_locale_ids(PyClientConfig *self, void *closure) {
    UA_ClientConfig *cfg = get_config(self);
    if (!cfg) { PyErr_SetString(PyExc_RuntimeError, "No UA_Client attached"); return NULL; }
    return ua_string_array_to_pylist(cfg->sessionLocaleIds, cfg->sessionLocaleIdsSize);
}

/* session_locale_ids — setter */
static int
PyClientConfig_set_session_locale_ids(PyClientConfig *self, PyObject *value, void *closure) {
    UA_ClientConfig *cfg = setter_precheck(self, "session_locale_ids");
    if (!cfg) return -1;
    size_t new_size = 0;
    UA_String *new_arr = pylist_to_ua_string_array(value, &new_size);
    if (PyErr_Occurred()) return -1;
    UA_Array_delete(cfg->sessionLocaleIds, cfg->sessionLocaleIdsSize, &UA_TYPES[UA_TYPES_STRING]);
    cfg->sessionLocaleIds = new_arr;
    cfg->sessionLocaleIdsSize = new_size;
    return 0;
}

/* namespaces — getter */
static PyObject *
PyClientConfig_get_namespaces(PyClientConfig *self, void *closure) {
    UA_ClientConfig *cfg = get_config(self);
    if (!cfg) { PyErr_SetString(PyExc_RuntimeError, "No UA_Client attached"); return NULL; }
    return ua_string_array_to_pylist(cfg->namespaces, cfg->namespacesSize);
}

/* namespaces — setter */
static int
PyClientConfig_set_namespaces(PyClientConfig *self, PyObject *value, void *closure) {
    UA_ClientConfig *cfg = setter_precheck(self, "namespaces");
    if (!cfg) return -1;
    size_t new_size = 0;
    UA_String *new_arr = pylist_to_ua_string_array(value, &new_size);
    if (PyErr_Occurred()) return -1;
    UA_Array_delete(cfg->namespaces, cfg->namespacesSize, &UA_TYPES[UA_TYPES_STRING]);
    cfg->namespaces = new_arr;
    cfg->namespacesSize = new_size;
    return 0;
}

// ---- localConnectionConfig buffer-size properties -----------------------

static PyObject *
PyClientConfig_get_send_buffer_size(PyClientConfig *self, void *closure) {
    UA_ClientConfig *cfg = get_config(self);
    if (!cfg) { PyErr_SetString(PyExc_RuntimeError, "No UA_Client attached"); return NULL; }
    return PyLong_FromUnsignedLong(cfg->localConnectionConfig.sendBufferSize);
}
static int
PyClientConfig_set_send_buffer_size(PyClientConfig *self, PyObject *value, void *closure) {
    UA_ClientConfig *cfg = setter_precheck(self, "send_buffer_size");
    if (!cfg) return -1;
    if (!PyLong_Check(value)) { PyErr_SetString(PyExc_TypeError, "send_buffer_size must be int"); return -1; }
    cfg->localConnectionConfig.sendBufferSize = (UA_UInt32)PyLong_AsUnsignedLong(value);
    return 0;
}

static PyObject *
PyClientConfig_get_recv_buffer_size(PyClientConfig *self, void *closure) {
    UA_ClientConfig *cfg = get_config(self);
    if (!cfg) { PyErr_SetString(PyExc_RuntimeError, "No UA_Client attached"); return NULL; }
    return PyLong_FromUnsignedLong(cfg->localConnectionConfig.recvBufferSize);
}
static int
PyClientConfig_set_recv_buffer_size(PyClientConfig *self, PyObject *value, void *closure) {
    UA_ClientConfig *cfg = setter_precheck(self, "recv_buffer_size");
    if (!cfg) return -1;
    if (!PyLong_Check(value)) { PyErr_SetString(PyExc_TypeError, "recv_buffer_size must be int"); return -1; }
    cfg->localConnectionConfig.recvBufferSize = (UA_UInt32)PyLong_AsUnsignedLong(value);
    return 0;
}

static PyObject *
PyClientConfig_get_local_max_message_size(PyClientConfig *self, void *closure) {
    UA_ClientConfig *cfg = get_config(self);
    if (!cfg) { PyErr_SetString(PyExc_RuntimeError, "No UA_Client attached"); return NULL; }
    return PyLong_FromUnsignedLong(cfg->localConnectionConfig.localMaxMessageSize);
}
static int
PyClientConfig_set_local_max_message_size(PyClientConfig *self, PyObject *value, void *closure) {
    UA_ClientConfig *cfg = setter_precheck(self, "local_max_message_size");
    if (!cfg) return -1;
    if (!PyLong_Check(value)) { PyErr_SetString(PyExc_TypeError, "local_max_message_size must be int"); return -1; }
    cfg->localConnectionConfig.localMaxMessageSize = (UA_UInt32)PyLong_AsUnsignedLong(value);
    return 0;
}

static PyObject *
PyClientConfig_get_local_max_chunk_count(PyClientConfig *self, void *closure) {
    UA_ClientConfig *cfg = get_config(self);
    if (!cfg) { PyErr_SetString(PyExc_RuntimeError, "No UA_Client attached"); return NULL; }
    return PyLong_FromUnsignedLong(cfg->localConnectionConfig.localMaxChunkCount);
}
static int
PyClientConfig_set_local_max_chunk_count(PyClientConfig *self, PyObject *value, void *closure) {
    UA_ClientConfig *cfg = setter_precheck(self, "local_max_chunk_count");
    if (!cfg) return -1;
    if (!PyLong_Check(value)) { PyErr_SetString(PyExc_TypeError, "local_max_chunk_count must be int"); return -1; }
    cfg->localConnectionConfig.localMaxChunkCount = (UA_UInt32)PyLong_AsUnsignedLong(value);
    return 0;
}

// ---- logger (write-only, stays custom) ----------------------------------

static int PyClientConfig_set_logger(PyClientConfig *self, PyObject *value, void *closure) {
    UA_ClientConfig *cfg = get_config(self);
    if (!cfg) {
        PyErr_SetString(PyExc_RuntimeError, "No UA_Client attached");
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
    cfg->eventLoop->logger = logging;
    for (size_t i = 0; i < cfg->securityPoliciesSize; i++)
        cfg->securityPolicies[i].logger = logging;
    return 0;
}

// ---- getset table -------------------------------------------------------

#define GENERIC_PROP(py_name, field) \
    {py_name, (getter)config_generic_get, (setter)config_generic_set, \
     py_name, &prop_##field}

// --- applicationUri (custom: uses clientDescription.applicationUri) ---
static PyObject *PyClientConfig_get_applicationUri(PyClientConfig *self, void *closure) {
    UA_ClientConfig *cfg = get_config(self);
    if (!cfg) {
        PyErr_SetString(PyExc_RuntimeError, "No UA_Client attached");
        return NULL;
    }
    if (cfg->clientDescription.applicationUri.length == 0)
        return PyUnicode_FromString("");
    return PyUnicode_FromStringAndSize(
        (const char*)cfg->clientDescription.applicationUri.data,
        cfg->clientDescription.applicationUri.length);
}
static int PyClientConfig_set_applicationUri(PyClientConfig *self, PyObject *value, void *closure) {
    UA_ClientConfig *cfg = get_config(self);
    if (!cfg) {
        PyErr_SetString(PyExc_RuntimeError, "No UA_Client attached");
        return -1;
    }
    if (is_client_connected(self->py_client->client)) {
        PyErr_SetString(PyExc_RuntimeError, "Cannot modify applicationUri while client is connected");
        return -1;
    }
    if (!PyUnicode_Check(value)) {
        PyErr_SetString(PyExc_TypeError, "application_uri must be str");
        return -1;
    }
    const char *uri = PyUnicode_AsUTF8(value);
    UA_String_clear(&cfg->clientDescription.applicationUri);
    cfg->clientDescription.applicationUri = UA_STRING_ALLOC(uri);
    return 0;
}

static PyGetSetDef PyClientConfig_getset[] = {
    {"logger", NULL, (setter)PyClientConfig_set_logger, "logger", NULL},
    GENERIC_PROP("timeout",                     timeout),
    GENERIC_PROP("no_session",                  noSession),
    GENERIC_PROP("endpoint_url",                endpointUrl),
    GENERIC_PROP("application_description",     clientDescription),
    GENERIC_PROP("user_identity_token",         userIdentityToken),
    GENERIC_PROP("security_mode",               securityMode),
    GENERIC_PROP("security_policy_uri",         securityPolicyUri),
    GENERIC_PROP("no_reconnect",                noReconnect),
    GENERIC_PROP("no_new_session",              noNewSession),
    GENERIC_PROP("endpoint",                    endpoint),
    GENERIC_PROP("user_token_policy",           userTokenPolicy),
    {"application_uri", (getter)PyClientConfig_get_applicationUri,
     (setter)PyClientConfig_set_applicationUri, "application_uri", NULL},
    GENERIC_PROP("tcp_reuse_addr",                tcpReuseAddr),
    GENERIC_PROP("allow_none_policy_password",    allowNonePolicyPassword),
    GENERIC_PROP("session_name",                  sessionName),
    GENERIC_PROP("secure_channel_life_time",      secureChannelLifeTime),
    GENERIC_PROP("requested_session_timeout",     requestedSessionTimeout),
    GENERIC_PROP("connectivity_check_interval",   connectivityCheckInterval),
    GENERIC_PROP("outstanding_publish_requests",  outStandingPublishRequests),
    GENERIC_PROP("auth_security_policy_uri",      authSecurityPolicyUri),
#ifdef UA_ENABLE_ENCRYPTION
    GENERIC_PROP("max_trust_list_size",           maxTrustListSize),
    GENERIC_PROP("max_rejected_list_size",        maxRejectedListSize),
#endif
    {"session_locale_ids",
     (getter)PyClientConfig_get_session_locale_ids,
     (setter)PyClientConfig_set_session_locale_ids,
     "session_locale_ids", NULL},
    {"namespaces",
     (getter)PyClientConfig_get_namespaces,
     (setter)PyClientConfig_set_namespaces,
     "namespaces", NULL},
    {"send_buffer_size",
     (getter)PyClientConfig_get_send_buffer_size,
     (setter)PyClientConfig_set_send_buffer_size,
     "send_buffer_size", NULL},
    {"recv_buffer_size",
     (getter)PyClientConfig_get_recv_buffer_size,
     (setter)PyClientConfig_set_recv_buffer_size,
     "recv_buffer_size", NULL},
    {"local_max_message_size",
     (getter)PyClientConfig_get_local_max_message_size,
     (setter)PyClientConfig_set_local_max_message_size,
     "local_max_message_size", NULL},
    {"local_max_chunk_count",
     (getter)PyClientConfig_get_local_max_chunk_count,
     (setter)PyClientConfig_set_local_max_chunk_count,
     "local_max_chunk_count", NULL},
    {NULL}
};

#undef GENERIC_PROP

static PyObject *
PyClientConfig_set_username_password(PyClientConfig *self, PyObject *args) {
    const char *username, *password;
    if (!PyArg_ParseTuple(args, "ss", &username, &password))
        return NULL;

    UA_ClientConfig *cfg = setter_precheck(self, "set_username_password");
    if (!cfg)
        return NULL;

    UA_StatusCode res = UA_ClientConfig_setAuthenticationUsername(cfg, username, password);
    if (res != UA_STATUSCODE_GOOD) {
        PyErr_Format(PyExc_RuntimeError,
                     "set_username_password failed: 0x%08x", res);
        return NULL;
    }
    Py_RETURN_NONE;
}

/* Helper: convert a Python list of bytes objects to a UA_ByteString array. */
#ifdef UA_ENABLE_ENCRYPTION
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
#endif

/* --- set_encryption method --- */
static PyObject *
PyClientConfig_set_encryption(PyClientConfig *self, PyObject *args, PyObject *kwds) {
#ifndef UA_ENABLE_ENCRYPTION
    PyErr_SetString(PyExc_RuntimeError,
                    "Encryption not available: open62541 was built without UA_ENABLE_ENCRYPTION");
    return NULL;
#else
    static char *kwlist[] = {"certificate", "private_key",
                             "trust_list", "revocation_list", NULL};
    PyObject *py_cert = NULL, *py_key = NULL;
    PyObject *py_trust = NULL, *py_revoc = NULL;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "SS|OO", kwlist,
                                     &py_cert, &py_key, &py_trust, &py_revoc))
        return NULL;

    UA_ClientConfig *cfg = get_config(self);
    if (!cfg) {
        PyErr_SetString(PyExc_RuntimeError, "No UA_Client attached");
        return NULL;
    }
    if (is_client_connected(self->py_client->client)) {
        PyErr_SetString(PyExc_RuntimeError,
                        "Cannot configure encryption while client is connected");
        return NULL;
    }

    char *cert_buf, *key_buf;
    Py_ssize_t cert_len, key_len;
    PyBytes_AsStringAndSize(py_cert, &cert_buf, &cert_len);
    PyBytes_AsStringAndSize(py_key, &key_buf, &key_len);

    UA_ByteString cert = {(size_t)cert_len, (UA_Byte *)cert_buf};
    UA_ByteString key = {(size_t)key_len, (UA_Byte *)key_buf};

    size_t trustSize = 0, revocSize = 0;
    UA_ByteString *trustList = pyList_to_ByteStringArray(py_trust, &trustSize);
    if (PyErr_Occurred()) return NULL;
    UA_ByteString *revocList = pyList_to_ByteStringArray(py_revoc, &revocSize);
    if (PyErr_Occurred()) {
        free_ByteStringArray(trustList, trustSize);
        return NULL;
    }

    UA_StatusCode status = UA_ClientConfig_setDefaultEncryption(
        cfg, cert, key, trustList, trustSize, revocList, revocSize);

    free_ByteStringArray(trustList, trustSize);
    free_ByteStringArray(revocList, revocSize);

    if (status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);

    Py_RETURN_NONE;
#endif
}

/* --- set_authentication_cert method --- */
static PyObject *
PyClientConfig_set_authentication_cert(PyClientConfig *self,
                                       PyObject *args, PyObject *kwds) {
#ifndef UA_ENABLE_ENCRYPTION
    PyErr_SetString(PyExc_RuntimeError,
                    "Encryption not available: open62541 was built without UA_ENABLE_ENCRYPTION");
    return NULL;
#else
    static char *kwlist[] = {"certificate", "private_key", NULL};
    PyObject *py_cert = NULL, *py_key = NULL;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "SS", kwlist,
                                     &py_cert, &py_key))
        return NULL;

    UA_ClientConfig *cfg = get_config(self);
    if (!cfg) {
        PyErr_SetString(PyExc_RuntimeError, "No UA_Client attached");
        return NULL;
    }
    if (is_client_connected(self->py_client->client)) {
        PyErr_SetString(PyExc_RuntimeError,
                        "Cannot configure authentication while client is connected");
        return NULL;
    }

    char *cert_buf, *key_buf;
    Py_ssize_t cert_len, key_len;
    PyBytes_AsStringAndSize(py_cert, &cert_buf, &cert_len);
    PyBytes_AsStringAndSize(py_key, &key_buf, &key_len);

    UA_ByteString cert = {(size_t)cert_len, (UA_Byte *)cert_buf};
    UA_ByteString key = {(size_t)key_len, (UA_Byte *)key_buf};

    UA_StatusCode status = UA_ClientConfig_setAuthenticationCert(cfg, cert, key);
    if (status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);

    Py_RETURN_NONE;
#endif
}

static PyMethodDef PyClientConfig_methods[] = {
    {"set_username_password", (PyCFunction)PyClientConfig_set_username_password,
     METH_VARARGS, "Set username/password authentication for the session."},
    {"set_encryption", (PyCFunction)PyClientConfig_set_encryption,
     METH_VARARGS | METH_KEYWORDS,
     "Configure encryption with certificate and private key.\n\n"
     "Args:\n"
     "    certificate: Certificate as bytes (DER or PEM)\n"
     "    private_key: Private key as bytes (DER or PEM)\n"
     "    trust_list: Optional list of trusted certificates (bytes)\n"
     "    revocation_list: Optional list of CRLs (bytes)"},
    {"set_authentication_cert", (PyCFunction)PyClientConfig_set_authentication_cert,
     METH_VARARGS | METH_KEYWORDS,
     "Configure certificate-based user authentication.\n\n"
     "Args:\n"
     "    certificate: Auth certificate as bytes\n"
     "    private_key: Auth private key as bytes"},
    {NULL, NULL, 0, NULL}
};

static void PyClientConfig_dealloc(PyClientConfig *self) {
    /* py_client is a borrowed reference — do not DECREF */
    self->py_client = NULL;
    Py_TYPE(self)->tp_free((PyObject*)self);
}

static PyObject *PyClientConfig_new(PyTypeObject *type, PyObject *args, PyObject *kwds) {
    PyClientConfig *self = (PyClientConfig*)type->tp_alloc(type, 0);
    self->py_client = NULL;
    return (PyObject*)self;
}

static int PyClientConfig_init(PyClientConfig *self, PyObject *args, PyObject *kwds) {
    PyErr_SetString(PyExc_TypeError, "ClientConfig cannot be instantiated directly");
    return -1;
}

PyTypeObject PyClientConfigType = {
    PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "o6.ClientConfig",
    .tp_basicsize = sizeof(PyClientConfig),
    .tp_flags = Py_TPFLAGS_DEFAULT,
    .tp_new = PyClientConfig_new,
    .tp_init = (initproc)PyClientConfig_init,
    .tp_dealloc = (destructor)PyClientConfig_dealloc,
    .tp_getset = PyClientConfig_getset,
    .tp_methods = PyClientConfig_methods,
};

PyObject *PyClientConfig_New(PyClient *py_client) {
    PyClientConfig *obj = (PyClientConfig*)PyClientConfigType.tp_alloc(&PyClientConfigType, 0);
    if (!obj) return NULL;
    /* Borrowed reference — the config is only accessible through the client,
     * so the client is always alive while py_client is used.  A strong
     * reference would create a cycle invisible to GC (PyClient has no
     * tp_traverse) and prevent the client from ever being collected. */
    obj->py_client = py_client;
    return (PyObject*)obj;
}
