/* Copyright 2026 (c) o6 Automation GmbH */
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

#include "client.h"
#include "../utils.h"
#include <ctype.h>
#include <open62541/client_config_default.h>
#include <open62541/plugin/certificategroup_default.h>
#include <open62541/plugin/create_certificate.h>
#include <open62541/plugin/securitypolicy_default.h>
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

/* UA_ClientConfig_setDefaultEncryption keeps the AcceptAll verification when
 * the trust list is empty, so every server certificate would be accepted.
 * Install an empty trust list first: setDefaultEncryption leaves a configured
 * verification in place, and it then rejects every server certificate.
 * acceptAll is the explicit development opt-in: like
 * ServerConfig.setAcceptAllCertificates, it replaces the trust list. */
static UA_StatusCode
set_default_encryption(UA_ClientConfig *cfg, UA_ByteString cert, UA_ByteString key,
                       const UA_ByteString *trustList, size_t trustSize,
                       const UA_ByteString *revocList, size_t revocSize,
                       UA_Boolean acceptAll) {
    if (trustSize == 0 && !acceptAll) {
        UA_NodeId group =
            UA_NS0ID(SERVERCONFIGURATION_CERTIFICATEGROUPS_DEFAULTAPPLICATIONGROUP);
        UA_StatusCode res =
            o6_set_trust_list(&cfg->certificateVerification, &group, cfg->logging,
                              NULL, 0, NULL, 0, revocList, revocSize);
        if (res != UA_STATUSCODE_GOOD)
            return res;
    }
    UA_StatusCode res = UA_ClientConfig_setDefaultEncryption(
        cfg, cert, key, trustList, trustSize, revocList, revocSize);
    if (res == UA_STATUSCODE_GOOD && acceptAll)
        UA_CertificateGroup_AcceptAll(&cfg->certificateVerification);
    return res;
}
typedef UA_StatusCode (*NewSecurityPolicy)(UA_SecurityPolicy *policy,
                                           const UA_ByteString localCertificate,
                                           const UA_ByteString localPrivateKey,
                                           const UA_Logger *logger);

/* Install the None and RSA policies of a certificate and key as the
 * authSecurityPolicies, which encrypt the user identity token */
static UA_StatusCode
set_token_policies(UA_ClientConfig *cfg, const UA_ByteString cert,
                   const UA_ByteString key) {
    static const NewSecurityPolicy rsaPolicies[] = {
        UA_SecurityPolicy_Basic256Sha256,
        UA_SecurityPolicy_Aes256Sha256RsaPss,
        UA_SecurityPolicy_Aes128Sha256RsaOaep,
    };
    size_t capacity = 1 + sizeof(rsaPolicies) / sizeof(rsaPolicies[0]);
    UA_SecurityPolicy *policies =
        (UA_SecurityPolicy *)UA_calloc(capacity, sizeof(UA_SecurityPolicy));
    if (!policies)
        return UA_STATUSCODE_BADOUTOFMEMORY;
    size_t size = 0;
    UA_StatusCode res = UA_SecurityPolicy_None(&policies[size], UA_BYTESTRING_NULL,
                                               cfg->logging);
    if (res == UA_STATUSCODE_GOOD)
        size++;
    for (size_t i = 0; res == UA_STATUSCODE_GOOD && i + 1 < capacity; i++) {
        if (rsaPolicies[i](&policies[size], cert, key, cfg->logging) == UA_STATUSCODE_GOOD)
            size++;
    }
    if (res != UA_STATUSCODE_GOOD || size < 2) {
        for (size_t i = 0; i < size; i++)
            policies[i].clear(&policies[i]);
        UA_free(policies);
        return res != UA_STATUSCODE_GOOD ? res : UA_STATUSCODE_BADCERTIFICATEINVALID;
    }
    for (size_t i = 0; i < cfg->authSecurityPoliciesSize; i++)
        cfg->authSecurityPolicies[i].clear(&cfg->authSecurityPolicies[i]);
    UA_free(cfg->authSecurityPolicies);
    cfg->authSecurityPolicies = policies;
    cfg->authSecurityPoliciesSize = size;
    return UA_STATUSCODE_GOOD;
}

/* The password of a UserName token is encrypted with the public key of the
 * server certificate. open62541 still needs an instance of the token's
 * SecurityPolicy, which it creates only from a client certificate. Without
 * one, a login on an endpoint whose UserTokenPolicy requires encryption failed
 * with BadIdentityTokenRejected. Create an ephemeral self-signed certificate
 * for the token policies only: the SecureChannel keeps the requested
 * SecurityPolicy, and the certificate is never sent. */
static int
_apply_token_encryption_if_needed(PyClientConfig *self) {
    UA_ClientConfig *cfg = get_config(self);
    if (!cfg) {
        PyErr_SetString(PyExc_RuntimeError, "No UA_Client attached");
        return -1;
    }
    const UA_ExtensionObject *token = &cfg->userIdentityToken;
    if (token->encoding < UA_EXTENSIONOBJECT_DECODED ||
        token->content.decoded.type != &UA_TYPES[UA_TYPES_USERNAMEIDENTITYTOKEN])
        return 0;
    for (size_t i = 0; i < cfg->authSecurityPoliciesSize; i++) {
        if (cfg->authSecurityPolicies[i].policyType != UA_SECURITYPOLICYTYPE_NONE)
            return 0; /* already able to encrypt the token */
    }

    UA_String subject[] = {UA_STRING("C=DE"), UA_STRING("O=o6"),
                           UA_STRING("CN=o6 UserName token encryption")};
    UA_String altNames[2] = {UA_STRING("DNS:localhost"), UA_STRING_NULL};
    size_t altNamesSize = 1;
    char uri[512];
    const UA_String *appUri = &cfg->clientDescription.applicationUri;
    if (appUri->length > 0 && appUri->length < sizeof(uri) - 5) {
        int length = snprintf(uri, sizeof(uri), "URI:%.*s", (int)appUri->length,
                              (const char *)appUri->data);
        altNames[altNamesSize++] = (UA_String){(size_t)length, (UA_Byte *)uri};
    }
    UA_KeyValueMap *params = UA_KeyValueMap_new();
    UA_UInt16 keySize = 2048;
    UA_StatusCode res = params ? UA_STATUSCODE_GOOD : UA_STATUSCODE_BADOUTOFMEMORY;
    if (res == UA_STATUSCODE_GOOD)
        res = UA_KeyValueMap_setScalar(params, UA_QUALIFIEDNAME(0, "key-size-bits"),
                                       &keySize, &UA_TYPES[UA_TYPES_UINT16]);
    UA_ByteString key = UA_BYTESTRING_NULL, cert = UA_BYTESTRING_NULL;
    if (res == UA_STATUSCODE_GOOD)
        res = UA_CreateCertificate(cfg->logging, subject, 3, altNames, altNamesSize,
                                   UA_CERTIFICATEFORMAT_DER, params, &key, &cert);
    UA_KeyValueMap_delete(params);
    if (res == UA_STATUSCODE_GOOD)
        res = set_token_policies(cfg, cert, key);
    UA_ByteString_memZero(&key);
    UA_ByteString_clear(&key);
    UA_ByteString_clear(&cert);
    if (res != UA_STATUSCODE_GOOD) {
        PyErr_Format(PyExc_RuntimeError,
                     "Encrypting the UserName token needs a client certificate. "
                     "Creating an ephemeral one failed with %s; pass certificate "
                     "and privateKey to the client.", UA_StatusCode_name(res));
        return -1;
    }
    return 0;
}

/* Apply UA_ClientConfig_setDefaultEncryption using the cert/key/trust/revoc
 * Applies UA_ClientConfig_setDefaultEncryption using the stored cert/key/trust/revoc.
 * Called from _finalize_encryption() just before connect; guarded by encryption_applied
 * so it only runs once per set of inputs. Without a certificate, it prepares the
 * encryption of a UserName token instead.
 * Returns 0 on success, -1 with PyErr set on failure. */
static int
_apply_encryption_if_ready(PyClientConfig *self) {
    if (!self->certificate || !self->private_key) {
        /* The server certificate of the selected endpoint is still verified,
         * for example the one that encrypts a UserName token */
        UA_ClientConfig *cfg = get_config(self);
        if (cfg && self->accept_all_certificates)
            UA_CertificateGroup_AcceptAll(&cfg->certificateVerification);
        return _apply_token_encryption_if_needed(self);
    }
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
    UA_StatusCode status = set_default_encryption(
        cfg, cert, key, trustList, trustSize, revocList, revocSize,
        self->accept_all_certificates != 0);
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
    if(!value) {
        PyErr_SetString(PyExc_AttributeError, "Cannot delete configuration properties");
        return -1;
    }
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
                            "Expected format: opc.tcp://host[:port][/path], "
                            "with an IPv6 address in brackets");
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
    if(!value) {
        PyErr_SetString(PyExc_AttributeError, "Cannot delete configuration properties");
        return -1;
    }
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
    if(!value) {
        PyErr_SetString(PyExc_AttributeError, "Cannot delete configuration properties");
        return -1;
    }
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
    if(!value) {
        PyErr_SetString(PyExc_AttributeError, "Cannot delete configuration properties");
        return -1;
    }
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
    if(!value) {
        PyErr_SetString(PyExc_AttributeError, "Cannot delete configuration properties");
        return -1;
    }
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
    if(!value) {
        PyErr_SetString(PyExc_AttributeError, "Cannot delete configuration properties");
        return -1;
    }
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
    if(!value) {
        PyErr_SetString(PyExc_AttributeError, "Cannot delete configuration properties");
        return -1;
    }
    UA_ClientConfig *cfg = setter_precheck(self, "local_max_chunk_count");
    if (!cfg) return -1;
    if (!PyLong_Check(value)) { PyErr_SetString(PyExc_TypeError, "local_max_chunk_count must be int"); return -1; }
    cfg->localConnectionConfig.localMaxChunkCount = (UA_UInt32)PyLong_AsUnsignedLong(value);
    return 0;
}

// ---- logger (write-only, stays custom) ----------------------------------

static int PyClientConfig_set_logger(PyClientConfig *self, PyObject *value, void *closure) {
    if(!value) {
        PyErr_SetString(PyExc_AttributeError, "Cannot delete configuration properties");
        return -1;
    }
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

/* The SecurityPolicy URIs of o6.SecurityPolicy */
static const char *knownSecurityPolicyUris[] = {
    "http://opcfoundation.org/UA/SecurityPolicy#None",
    "http://opcfoundation.org/UA/SecurityPolicy#Basic128Rsa15",
    "http://opcfoundation.org/UA/SecurityPolicy#Basic256",
    "http://opcfoundation.org/UA/SecurityPolicy#Basic256Sha256",
    "http://opcfoundation.org/UA/SecurityPolicy#Aes128_Sha256_RsaOaep",
    "http://opcfoundation.org/UA/SecurityPolicy#Aes256_Sha256_RsaPss",
    "http://opcfoundation.org/UA/SecurityPolicy#ECC_nistP256",
    "http://opcfoundation.org/UA/SecurityPolicy#ECC_nistP384",
    "http://opcfoundation.org/UA/SecurityPolicy#ECC_brainpoolP256r1",
    "http://opcfoundation.org/UA/SecurityPolicy#ECC_brainpoolP384r1",
    "http://opcfoundation.org/UA/SecurityPolicy#ECC_curve25519",
    "http://opcfoundation.org/UA/SecurityPolicy#ECC_curve448",
    "http://opcfoundation.org/UA/SecurityPolicy#ECC_nistP256_AesGcm",
    "http://opcfoundation.org/UA/SecurityPolicy#ECC_nistP256_ChaChaPoly",
};

/* Compare a short name with the part after '#', case-insensitively and
 * ignoring '_': "Basic256Sha256", "aes128_sha256_rsaoaep" and "ECCnistP256"
 * all match their URI. */
static bool
securityPolicyShortNameMatches(const char *name, const char *uri) {
    const char *suffix = strrchr(uri, '#') + 1;
    for(;;) {
        while(*name == '_')
            name++;
        while(*suffix == '_')
            suffix++;
        if(!*name || !*suffix)
            return !*name && !*suffix;
        if(tolower((unsigned char)*name) != tolower((unsigned char)*suffix))
            return false;
        name++;
        suffix++;
    }
}

/* A value with "://" is a URI and used as-is; an empty value clears the
 * preference. Other values must be a short name of a known policy. */
const char *
o6_resolve_security_policy(const char *value) {
    if(!*value || strstr(value, "://"))
        return value;
    size_t count = sizeof(knownSecurityPolicyUris) / sizeof(knownSecurityPolicyUris[0]);
    for(size_t i = 0; i < count; i++) {
        if(securityPolicyShortNameMatches(value, knownSecurityPolicyUris[i]))
            return knownSecurityPolicyUris[i];
    }
    PyErr_Format(PyExc_ValueError,
                 "Unknown security policy '%s'. Use a policy URI, an "
                 "o6.SecurityPolicy member or a short name such as "
                 "'Basic256Sha256'", value);
    return NULL;
}

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
    if(!value) {
        PyErr_SetString(PyExc_AttributeError, "Cannot delete configuration properties");
        return -1;
    }
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
    if (uri)
        uri = o6_resolve_security_policy(uri);
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
    if(!value) {
        PyErr_SetString(PyExc_AttributeError, "Cannot delete configuration properties");
        return -1;
    }
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
    if(!value) {
        PyErr_SetString(PyExc_AttributeError, "Cannot delete configuration properties");
        return -1;
    }
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
    if(!value) {
        PyErr_SetString(PyExc_AttributeError, "Cannot delete configuration properties");
        return -1;
    }
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
    if(!value) {
        PyErr_SetString(PyExc_AttributeError, "Cannot delete configuration properties");
        return -1;
    }
    if (!setter_precheck(self, "revocation_list")) return -1;
    self->encryption_applied = 0;  /* mark dirty */
    PyObject *lst = load_cert_list(value);
    if (!lst) return -1;
    Py_XDECREF(self->revocation_list);
    self->revocation_list = lst;
    return 0;
}

static PyObject *
PyClientConfig_get_accept_all_certificates(PyClientConfig *self, void *closure) {
    return PyBool_FromLong(self->accept_all_certificates);
}

static int
PyClientConfig_set_accept_all_certificates(PyClientConfig *self, PyObject *value,
                                           void *closure) {
    if(!value) {
        PyErr_SetString(PyExc_AttributeError, "Cannot delete configuration properties");
        return -1;
    }
    if (!PyBool_Check(value)) {
        PyErr_SetString(PyExc_TypeError, "acceptAllCertificates must be bool");
        return -1;
    }
    if (!setter_precheck(self, "acceptAllCertificates")) return -1;
    self->encryption_applied = 0;  /* mark dirty */
    self->accept_all_certificates = value == Py_True;
    return 0;
}

static PyObject *
PyClientConfig_get_load_unknown_data_types(PyClientConfig *self, void *closure) {
    return PyBool_FromLong(self->load_unknown_data_types);
}

/* Read by the Python client before each on-demand DataType lookup, so it can
 * change while connected. */
static int
PyClientConfig_set_load_unknown_data_types(PyClientConfig *self, PyObject *value,
                                           void *closure) {
    if(!value) {
        PyErr_SetString(PyExc_AttributeError, "Cannot delete configuration properties");
        return -1;
    }
    if (!PyBool_Check(value)) {
        PyErr_SetString(PyExc_TypeError, "loadUnknownDataTypes must be bool");
        return -1;
    }
    self->load_unknown_data_types = value == Py_True;
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
    if(!value) {
        PyErr_SetString(PyExc_AttributeError, "Cannot delete configuration properties");
        return -1;
    }
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
    {"acceptAllCertificates",
     (getter)PyClientConfig_get_accept_all_certificates,
     (setter)PyClientConfig_set_accept_all_certificates,
     "Trust every server certificate and ignore trustList (development only)", NULL},
    {"loadUnknownDataTypes",
     (getter)PyClientConfig_get_load_unknown_data_types,
     (setter)PyClientConfig_set_load_unknown_data_types,
     "Load the DataType of a received value the client cannot decode", NULL},
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

    UA_StatusCode status = set_default_encryption(
        cfg, cert, key, trustList, trustSize, revocList, revocSize,
        self->accept_all_certificates != 0);

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

#ifdef UA_ENABLE_JSON_ENCODING
/* ---- _loadJson: the JSON configuration format of open62541 ---------------
 *
 * UA_ClientConfig_loadFromFile always starts from a zeroed config with the
 * open62541 defaults, so it cannot run on the config of an existing client.
 * It loads into a scratch config instead, which then receives the o6 runtime
 * plugins of the live config and replaces it. The server does the same in
 * server_config.c. o6/_json_config.py prepares the document. */

#define TRANSPLANT(field) \
    o6_swap_bytes(&live->field, &tmp->field, sizeof(live->field))

/* Move the plugins and callbacks that o6 installs into the scratch config.
 * The JSON format has no keys for them. Review this list when open62541 adds
 * a plugin or callback field to UA_ClientConfig. */
static void
transplant_o6_plugins(UA_ClientConfig *live, UA_ClientConfig *tmp) {
    TRANSPLANT(clientContext);
#ifdef UA_ENABLE_ENCRYPTION
    TRANSPLANT(privateKeyPasswordCallback);
#endif
    TRANSPLANT(customDataTypes);
    TRANSPLANT(globalNotificationCallback);
    TRANSPLANT(lifecycleNotificationCallback);
    TRANSPLANT(serviceNotificationCallback);
    TRANSPLANT(stateCallback);
    TRANSPLANT(inactivityCallback);
    TRANSPLANT(subscriptionInactivityCallback);
    TRANSPLANT(eventLoop);
    TRANSPLANT(externalEventLoop);
}

#undef TRANSPLANT

/* Parse a JSON document into a scratch config only, to find invalid settings */
static PyObject *
check_json(PyObject *arg) {
    Py_buffer view;
    if (PyObject_GetBuffer(arg, &view, PyBUF_SIMPLE) < 0)
        return NULL;
    UA_ByteString json = {(size_t)view.len, (UA_Byte *)view.buf};
    UA_ClientConfig tmp;
    UA_StatusCode status = UA_ClientConfig_loadFromFile(&tmp, json);
    if (status == UA_STATUSCODE_GOOD)
        UA_ClientConfig_clear(&tmp);
    PyBuffer_Release(&view);
    if (status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);
    Py_RETURN_NONE;
}

static PyObject *
PyClientConfig_load_json(PyClientConfig *self, PyObject *args, PyObject *kwds) {
    static char *kwlist[] = {"json", "dryRun", NULL};
    PyObject *arg;
    int dry_run = 0;
    if (!PyArg_ParseTupleAndKeywords(args, kwds, "O|$p", kwlist, &arg, &dry_run))
        return NULL;
    if (dry_run)
        return check_json(arg);

    UA_ClientConfig *live = setter_precheck(self, "the configuration");
    if (!live)
        return NULL;
    if (self->py_client->connectFuture) {
        PyErr_SetString(PyExc_RuntimeError,
                        "Cannot modify the configuration while the client is connecting");
        return NULL;
    }
    Py_buffer view;
    if (PyObject_GetBuffer(arg, &view, PyBUF_SIMPLE) < 0)
        return NULL;

    UA_ByteString json = {(size_t)view.len, (UA_Byte *)view.buf};
    UA_ClientConfig tmp;
    UA_StatusCode status = UA_ClientConfig_loadFromFile(&tmp, json);
    PyBuffer_Release(&view);
    if (status == UA_STATUSCODE_GOOD && !tmp.logging) {
        UA_ClientConfig_clear(&tmp);
        status = UA_STATUSCODE_BADOUTOFMEMORY;
    }
    if (status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);

    /* The security policies and the certificate verification of the scratch
     * config keep a pointer to its stdout logger. Turn that logger into the
     * Python logger and keep it, so they log to Python. */
    pyLogger_init(tmp.logging, (PyObject *)live->logging->context);
    if (live->eventLoop && live->eventLoop->logger == live->logging)
        live->eventLoop->logger = tmp.logging;

    transplant_o6_plugins(live, &tmp);
    /* The waiting rules spin on the event loop, which cannot advance the
     * Python-owned asyncio loop; see pyClient_init */
    tmp.asyncServiceCallRule = UA_RULEHANDLING_ABORT;
    UA_ClientConfig old = *live;
    *live = tmp;
    /* Frees the scratch event loop and the replaced settings, security and
     * logger */
    UA_ClientConfig_clear(&old);

    /* The security configuration came from the file. Drop the credentials
     * stored for the encryption that connect() applies. */
    Py_CLEAR(self->certificate);
    Py_CLEAR(self->private_key);
    Py_CLEAR(self->trust_list);
    Py_CLEAR(self->revocation_list);
    self->encryption_applied = 0;
    self->accept_all_certificates = 0;
    self->load_unknown_data_types = 1;
    Py_RETURN_NONE;
}
#endif /* UA_ENABLE_JSON_ENCODING */

static PyMethodDef PyClientConfig_methods[] = {
#ifdef UA_ENABLE_JSON_ENCODING
    {"loadFromFile", (PyCFunction)pyJsonConfig_load, METH_O,
     "Replace the configuration with the settings of a JSON5 file, and the\n"
     "o6 defaults for everything it leaves out."},
    {"_loadJson", (PyCFunction)PyClientConfig_load_json, METH_VARARGS | METH_KEYWORDS,
     "Replace the configuration with the settings of a JSON document (bytes),\n"
     "keeping the plugins and callbacks. Use loadFromFile."},
#endif
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
     "    trust_list: Optional list of trusted certificates (bytes); an empty\n"
     "        list rejects every server certificate unless\n"
     "        acceptAllCertificates is True\n"
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
    self->accept_all_certificates = 0;
    self->load_unknown_data_types = 1;
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
    obj->load_unknown_data_types = 1;
    return (PyObject*)obj;
}

void PyClientConfig_Invalidate(PyObject *config) {
    if (config && PyObject_TypeCheck(config, &PyClientConfigType))
        ((PyClientConfig *)config)->py_client = NULL;
}
