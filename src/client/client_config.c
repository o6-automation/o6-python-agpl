/* Copyright 2026 (c) o6 Automation GmbH */
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

// ---- cert/key file loading, UA_ByteString array helpers, encryption apply -

/* Load a certificate or key from bytes or a file path (str / Path / bytes).
 * Returns a new reference to a bytes object, or NULL on error. */
static PyObject *
load_cert_bytes(PyObject *value) {
    if (PyBytes_Check(value)) {
        Py_INCREF(value);
        return value;
    }
    /* Handles str, bytes paths, and pathlib.Path via __fspath__ */
    PyObject *fspath = PyOS_FSPath(value);
    if (!fspath) return NULL;
    const char *path = PyUnicode_AsUTF8(fspath);
    if (!path) { Py_DECREF(fspath); return NULL; }
    FILE *f = fopen(path, "rb");
    if (!f) {
        PyErr_SetFromErrnoWithFilenameObject(PyExc_OSError, fspath);
        Py_DECREF(fspath);
        return NULL;
    }
    Py_DECREF(fspath);
    if (fseek(f, 0, SEEK_END) != 0) {
        fclose(f);
        PyErr_SetString(PyExc_OSError, "Failed to seek in certificate file");
        return NULL;
    }
    long size = ftell(f);
    if (size < 0) {
        fclose(f);
        PyErr_SetString(PyExc_OSError, "Failed to determine certificate file size");
        return NULL;
    }
    rewind(f);
    PyObject *result = PyBytes_FromStringAndSize(NULL, size);
    if (!result) { fclose(f); return NULL; }
    if ((long)fread(PyBytes_AS_STRING(result), 1, (size_t)size, f) != size) {
        fclose(f);
        Py_DECREF(result);
        PyErr_SetString(PyExc_OSError, "Failed to read certificate file");
        return NULL;
    }
    fclose(f);
    return result;
}

/* Load a list of cert/key entries from list[bytes|str|Path], or None → [].
 * Returns a new reference to list[bytes], or NULL on error. */
static PyObject *
load_cert_list(PyObject *value) {
    if (value == Py_None || value == NULL)
        return PyList_New(0);
    if (!PyList_Check(value)) {
        PyErr_SetString(PyExc_TypeError,
                        "expected a list of bytes/str/Path, or None");
        return NULL;
    }
    Py_ssize_t n = PyList_GET_SIZE(value);
    PyObject *result = PyList_New(n);
    if (!result) return NULL;
    for (Py_ssize_t i = 0; i < n; i++) {
        PyObject *b = load_cert_bytes(PyList_GET_ITEM(value, i));
        if (!b) { Py_DECREF(result); return NULL; }
        PyList_SET_ITEM(result, i, b);
    }
    return result;
}

/* Convert a Python list[bytes] to a heap-allocated UA_ByteString array.
 * Caller is responsible for calling free_ByteStringArray on the result. */
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
/* Apply UA_ClientConfig_setDefaultEncryption using the cert/key/trust/revoc
 * Applies UA_ClientConfig_setDefaultEncryption using the stored cert/key/trust/revoc.
 * Called from _finalize_encryption() just before connect; guarded by encryption_applied
 * so it only runs once per set of inputs.
 * Returns 0 on success, -1 with PyErr set on failure. */
static int
_apply_encryption_if_ready(PyClientConfig *self) {
    if (!self->certificate || !self->private_key)
        return 0;  /* not ready yet */
    if (self->encryption_applied)
        return 0;  /* already up to date — avoid double-init of security policies */
    UA_ClientConfig *cfg = get_config(self);
    if (!cfg) {
        PyErr_SetString(PyExc_RuntimeError, "No UA_Client attached");
        return -1;
    }
    char *cert_buf, *key_buf;
    Py_ssize_t cert_len, key_len;
    if (PyBytes_AsStringAndSize(self->certificate, &cert_buf, &cert_len) < 0) return -1;
    if (PyBytes_AsStringAndSize(self->private_key,  &key_buf,  &key_len)  < 0) return -1;
    UA_ByteString cert = {(size_t)cert_len, (UA_Byte *)cert_buf};
    UA_ByteString key  = {(size_t)key_len,  (UA_Byte *)key_buf};
    size_t trustSize = 0, revocSize = 0;
    UA_ByteString *trustList = NULL, *revocList = NULL;
    if (self->trust_list && PyList_Check(self->trust_list)) {
        trustList = pyList_to_ByteStringArray(self->trust_list, &trustSize);
        if (PyErr_Occurred()) return -1;
    }
    if (self->revocation_list && PyList_Check(self->revocation_list)) {
        revocList = pyList_to_ByteStringArray(self->revocation_list, &revocSize);
        if (PyErr_Occurred()) {
            free_ByteStringArray(trustList, trustSize);
            return -1;
        }
    }
    UA_StatusCode status = UA_ClientConfig_setDefaultEncryption(
        cfg, cert, key, trustList, trustSize, revocList, revocSize);
    free_ByteStringArray(trustList, trustSize);
    free_ByteStringArray(revocList, revocSize);
    if (status != UA_STATUSCODE_GOOD) {
        PyErr_StatusCode(status);
        return -1;
    }
    self->encryption_applied = 1;
    return 0;
}
/* Python-callable wrapper: applies encryption (once, idempotently) before connect. */
static PyObject *
PyClientConfig_finalize_encryption(PyClientConfig *self, PyObject *args) {
    if (_apply_encryption_if_ready(self) < 0)
        return NULL;
    Py_RETURN_NONE;
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
    case PROP_STRUCT: {
        const UA_DataType *type = &UA_TYPES[desc->ua_type_index];
        void *copy = UA_new(type);
        if(!copy)
            return PyErr_NoMemory();
        UA_StatusCode status = UA_copy(field, copy, type);
        if(status != UA_STATUSCODE_GOOD) {
            UA_delete(copy, type);
            return PyErr_StatusCode(status);
        }
        PyObject *result = UA2PY(copy, type, &self->py_client->nsMapPy2UA);
        UA_delete(copy, type);
        return result;
    }
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
        PyObject *result = PY2UA(value, tmp, type,
                                 &self->py_client->nsMapPy2UA,
                                 cfg->customDataTypes);
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
PROP("noSession",                     PROP_BOOL,                  noSession,                  0);
PROP("endpointUrl",                   PROP_UA_STRING_ENDPOINT,    endpointUrl,                0);
PROP("securityMode",                  PROP_ENUM_SECURITY_MODE,    securityMode,               0);
PROP("securityPolicyUri",             PROP_UA_STRING,             securityPolicyUri,          0);
PROP("noReconnect",                   PROP_BOOL,                  noReconnect,                0);
PROP("noNewSession",                  PROP_BOOL,                  noNewSession,               0);
PROP("tcpReuseAddr",                  PROP_BOOL,                  tcpReuseAddr,               0);
PROP("allowNonePolicyPassword",       PROP_BOOL,                  allowNonePolicyPassword,    0);
PROP("applicationDescription",        PROP_STRUCT,                clientDescription,          UA_TYPES_APPLICATIONDESCRIPTION);
PROP("userIdentityToken",             PROP_STRUCT,                userIdentityToken,          UA_TYPES_EXTENSIONOBJECT);
PROP("endpoint",                      PROP_STRUCT,                endpoint,                   UA_TYPES_ENDPOINTDESCRIPTION);
PROP("userTokenPolicy",               PROP_STRUCT,                userTokenPolicy,            UA_TYPES_USERTOKENPOLICY);
PROP("sessionName",                   PROP_UA_STRING,             sessionName,                0);
PROP("secureChannelLifeTime",         PROP_UINT32,                secureChannelLifeTime,      0);
PROP("requestedSessionTimeout",       PROP_UINT32,                requestedSessionTimeout,    0);
PROP("connectivityCheckInterval",     PROP_UINT32,                connectivityCheckInterval,  0);
PROP("outstandingPublishRequests",    PROP_UINT16,                outStandingPublishRequests, 0);
PROP("maxAsyncServiceCalls",          PROP_UINT32,                maxAsyncServiceCalls,       0);
PROP("authSecurityPolicyUri",         PROP_UA_STRING,             authSecurityPolicyUri,      0);
PROP("maxTrustListSize",              PROP_UINT32,                maxTrustListSize,           0);
PROP("maxRejectedListSize",           PROP_UINT32,                maxRejectedListSize,        0);

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

// ---- security_policy (enum-friendly alias for security_policy_uri) ------

static PyObject *
PyClientConfig_get_security_policy(PyClientConfig *self, void *closure) {
    UA_ClientConfig *cfg = get_config(self);
    if (!cfg) { PyErr_SetString(PyExc_RuntimeError, "No UA_Client attached"); return NULL; }
    if (cfg->securityPolicyUri.length == 0)
        return PyUnicode_FromString("");
    return PyUnicode_FromStringAndSize(
        (const char *)cfg->securityPolicyUri.data,
        (Py_ssize_t)cfg->securityPolicyUri.length);
}

static int
PyClientConfig_set_security_policy(PyClientConfig *self, PyObject *value, void *closure) {
    UA_ClientConfig *cfg = setter_precheck(self, "security_policy");
    if (!cfg) return -1;
    PyObject *str_val;
    if (PyUnicode_Check(value)) {
        str_val = value;
        Py_INCREF(str_val);
    } else {
        /* Accept SecurityPolicy enum or any object with a string .value */
        str_val = PyObject_GetAttrString(value, "value");
        if (!str_val) {
            PyErr_Clear();
            str_val = PyObject_Str(value);
            if (!str_val) return -1;
        }
        if (!PyUnicode_Check(str_val)) {
            Py_DECREF(str_val);
            PyErr_SetString(PyExc_TypeError,
                            "security_policy must be a str or enum with str .value");
            return -1;
        }
    }
    const char *uri = PyUnicode_AsUTF8(str_val);
    if (!uri) { Py_DECREF(str_val); return -1; }
    UA_String_clear(&cfg->securityPolicyUri);
    cfg->securityPolicyUri = UA_STRING_ALLOC(uri);
    Py_DECREF(str_val);
    return 0;
}

// ---- certificate, private_key, trust_list, revocation_list --------------

static PyObject *
PyClientConfig_get_certificate(PyClientConfig *self, void *closure) {
    if (!self->certificate) Py_RETURN_NONE;
    Py_INCREF(self->certificate);
    return self->certificate;
}

static int
PyClientConfig_set_certificate(PyClientConfig *self, PyObject *value, void *closure) {
    if (!setter_precheck(self, "certificate")) return -1;
    self->encryption_applied = 0;  /* mark dirty */
    if (value == Py_None) {
        Py_XDECREF(self->certificate);
        self->certificate = NULL;
        return 0;
    }
    PyObject *b = load_cert_bytes(value);
    if (!b) return -1;
    Py_XDECREF(self->certificate);
    self->certificate = b;
    return 0;
}

static PyObject *
PyClientConfig_get_private_key(PyClientConfig *self, void *closure) {
    if (!self->private_key) Py_RETURN_NONE;
    Py_INCREF(self->private_key);
    return self->private_key;
}

static int
PyClientConfig_set_private_key(PyClientConfig *self, PyObject *value, void *closure) {
    if (!setter_precheck(self, "private_key")) return -1;
    self->encryption_applied = 0;  /* mark dirty */
    if (value == Py_None) {
        Py_XDECREF(self->private_key);
        self->private_key = NULL;
        return 0;
    }
    PyObject *b = load_cert_bytes(value);
    if (!b) return -1;
    Py_XDECREF(self->private_key);
    self->private_key = b;
    return 0;
}

static PyObject *
PyClientConfig_get_trust_list(PyClientConfig *self, void *closure) {
    if (!self->trust_list) return PyList_New(0);
    Py_INCREF(self->trust_list);
    return self->trust_list;
}

static int
PyClientConfig_set_trust_list(PyClientConfig *self, PyObject *value, void *closure) {
    if (!setter_precheck(self, "trust_list")) return -1;
    self->encryption_applied = 0;  /* mark dirty */
    PyObject *lst = load_cert_list(value);
    if (!lst) return -1;
    Py_XDECREF(self->trust_list);
    self->trust_list = lst;
    return 0;
}

static PyObject *
PyClientConfig_get_revocation_list(PyClientConfig *self, void *closure) {
    if (!self->revocation_list) return PyList_New(0);
    Py_INCREF(self->revocation_list);
    return self->revocation_list;
}

static int
PyClientConfig_set_revocation_list(PyClientConfig *self, PyObject *value, void *closure) {
    if (!setter_precheck(self, "revocation_list")) return -1;
    self->encryption_applied = 0;  /* mark dirty */
    PyObject *lst = load_cert_list(value);
    if (!lst) return -1;
    Py_XDECREF(self->revocation_list);
    self->revocation_list = lst;
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
    GENERIC_PROP("noSession",                   noSession),
    GENERIC_PROP("endpointUrl",                 endpointUrl),
    GENERIC_PROP("applicationDescription",      clientDescription),
    GENERIC_PROP("userIdentityToken",           userIdentityToken),
    GENERIC_PROP("securityMode",                securityMode),
    GENERIC_PROP("securityPolicyUri",           securityPolicyUri),
    GENERIC_PROP("noReconnect",                 noReconnect),
    GENERIC_PROP("noNewSession",                noNewSession),
    GENERIC_PROP("endpoint",                    endpoint),
    GENERIC_PROP("userTokenPolicy",            userTokenPolicy),
    {"applicationUri", (getter)PyClientConfig_get_applicationUri,
     (setter)PyClientConfig_set_applicationUri, "applicationUri", NULL},
    GENERIC_PROP("tcpReuseAddr",                  tcpReuseAddr),
    GENERIC_PROP("allowNonePolicyPassword",       allowNonePolicyPassword),
    GENERIC_PROP("sessionName",                   sessionName),
    GENERIC_PROP("secureChannelLifeTime",         secureChannelLifeTime),
    GENERIC_PROP("requestedSessionTimeout",       requestedSessionTimeout),
    GENERIC_PROP("connectivityCheckInterval",     connectivityCheckInterval),
    GENERIC_PROP("outstandingPublishRequests",    outStandingPublishRequests),
    GENERIC_PROP("maxAsyncServiceCalls",          maxAsyncServiceCalls),
    GENERIC_PROP("authSecurityPolicyUri",         authSecurityPolicyUri),
    GENERIC_PROP("maxTrustListSize",              maxTrustListSize),
    GENERIC_PROP("maxRejectedListSize",           maxRejectedListSize),
    {"sessionLocaleIds",
     (getter)PyClientConfig_get_session_locale_ids,
     (setter)PyClientConfig_set_session_locale_ids,
     "sessionLocaleIds", NULL},
    {"namespaces",
     (getter)PyClientConfig_get_namespaces,
     (setter)PyClientConfig_set_namespaces,
     "namespaces", NULL},
    {"sendBufferSize",
     (getter)PyClientConfig_get_send_buffer_size,
     (setter)PyClientConfig_set_send_buffer_size,
     "sendBufferSize", NULL},
    {"recvBufferSize",
     (getter)PyClientConfig_get_recv_buffer_size,
     (setter)PyClientConfig_set_recv_buffer_size,
     "recvBufferSize", NULL},
    {"localMaxMessageSize",
     (getter)PyClientConfig_get_local_max_message_size,
     (setter)PyClientConfig_set_local_max_message_size,
     "localMaxMessageSize", NULL},
    {"localMaxChunkCount",
     (getter)PyClientConfig_get_local_max_chunk_count,
     (setter)PyClientConfig_set_local_max_chunk_count,
     "localMaxChunkCount", NULL},
    {"securityPolicy",
     (getter)PyClientConfig_get_security_policy,
     (setter)PyClientConfig_set_security_policy,
     "securityPolicy", NULL},
    {"certificate",
     (getter)PyClientConfig_get_certificate,
     (setter)PyClientConfig_set_certificate,
     "certificate", NULL},
    {"privateKey",
     (getter)PyClientConfig_get_private_key,
     (setter)PyClientConfig_set_private_key,
     "privateKey", NULL},
    {"trustList",
     (getter)PyClientConfig_get_trust_list,
     (setter)PyClientConfig_set_trust_list,
     "trustList", NULL},
    {"revocationList",
     (getter)PyClientConfig_get_revocation_list,
     (setter)PyClientConfig_set_revocation_list,
     "revocationList", NULL},
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

/* --- set_encryption method --- */
static PyObject *
PyClientConfig_set_encryption(PyClientConfig *self, PyObject *args, PyObject *kwds) {
    static char *kwlist[] = {"certificate", "privateKey",
                             "trustList", "revocationList", NULL};
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
}

/* --- set_authentication_cert method --- */
static PyObject *
PyClientConfig_set_authentication_cert(PyClientConfig *self,
                                       PyObject *args, PyObject *kwds) {
    static char *kwlist[] = {"certificate", "privateKey", NULL};
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
}

static PyMethodDef PyClientConfig_methods[] = {
    {"setUsernamePassword", (PyCFunction)PyClientConfig_set_username_password,
     METH_VARARGS, "Set username/password authentication for the session."},
    {"setCredentials", (PyCFunction)PyClientConfig_set_username_password,
     METH_VARARGS, "Set username/password authentication for the session."},
    {"_finalize_encryption", (PyCFunction)PyClientConfig_finalize_encryption,
     METH_NOARGS,
     "Apply stored certificate/key/trust_list/revocation_list encryption config. "
     "No-op if already applied or no certificate is set. Called automatically by connect()."},
    {"setEncryption", (PyCFunction)PyClientConfig_set_encryption,
     METH_VARARGS | METH_KEYWORDS,
     "Configure encryption with certificate and private key.\n\n"
     "Args:\n"
     "    certificate: Certificate as bytes (DER or PEM)\n"
     "    private_key: Private key as bytes (DER or PEM)\n"
     "    trust_list: Optional list of trusted certificates (bytes)\n"
     "    revocation_list: Optional list of CRLs (bytes)"},
    {"setAuthenticationCert", (PyCFunction)PyClientConfig_set_authentication_cert,
     METH_VARARGS | METH_KEYWORDS,
     "Configure certificate-based user authentication.\n\n"
     "Args:\n"
     "    certificate: Auth certificate as bytes\n"
     "    private_key: Auth private key as bytes"},
    {NULL, NULL, 0, NULL}
};

static void PyClientConfig_dealloc(PyClientConfig *self) {
    Py_XDECREF(self->certificate);
    Py_XDECREF(self->private_key);
    Py_XDECREF(self->trust_list);
    Py_XDECREF(self->revocation_list);
    /* py_client is a borrowed reference — do not DECREF */
    self->py_client = NULL;
    Py_TYPE(self)->tp_free((PyObject*)self);
}

static PyObject *PyClientConfig_new(PyTypeObject *type, PyObject *args, PyObject *kwds) {
    PyClientConfig *self = (PyClientConfig*)type->tp_alloc(type, 0);
    self->py_client = NULL;
    self->certificate = NULL;
    self->private_key = NULL;
    self->trust_list = NULL;
    self->revocation_list = NULL;
    self->encryption_applied = 0;
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

void PyClientConfig_Invalidate(PyObject *config) {
    if (config && PyObject_TypeCheck(config, &PyClientConfigType))
        ((PyClientConfig *)config)->py_client = NULL;
}
