/* Copyright 2026 (c) o6 Automation GmbH (Author: Andreas Ebner) */
#include "module.h"
#include "types_internal.h"
#include "datatypes.h"
#include "client/client.h"
#include "server/server.h"
#include "server/python_nodestore.h"
#include <datetime.h>
#include <numpy/arrayobject.h>

#define O6_NAMESPACE_ARRAY_INITIAL_CAPACITY 128u

typedef struct {
    char *shortname;
    PyObject *namespace_module;
} o6_NamespaceArrayEntry;

static o6_NamespaceArrayEntry *namespace_entries;
static size_t namespace_entries_capacity;
static PyObject *namespace_token_resolver;
static bool namespace_array_shutting_down;

static int
require_feature(bool enabled, const char *name) {
    if(enabled)
        return 0;
    PyErr_Format(PyExc_PermissionError,
                 "%s is not enabled by the active o6 Credential", name);
    return -1;
}

int o6_require_client(void) {
    return require_feature(client_enabled, "Client");
}

int o6_require_server(void) {
    return require_feature(server_enabled, "Server");
}

int o6_require_pubsub(void) {
    return require_feature(pubsub_enabled, "PubSub");
}

const char *
o6_parse_feature_scope(const UA_String *scope, o6_FeatureSet *features) {
    *features = (o6_FeatureSet){false, false, false};
    if(scope->length == 0) {
        features->client = true;
        features->server = true;
        features->pubsub = true;
        return NULL;
    }
    if(scope->length >= 512)
        return "FeatureScope is too long";
    if(memchr(scope->data, 0, scope->length))
        return "FeatureScope contains a null character";

    char buf[512];
    memcpy(buf, scope->data, scope->length);
    buf[scope->length] = 0;
    char *input = buf;
    while(input) {
        char *next = strchr(input, ',');
        if(next) {
            *next = 0;
            next++;
        }
        while(*input == ' ' || *input == '\t')
            input++;
        char *end = input + strlen(input);
        while(end > input && (end[-1] == ' ' || end[-1] == '\t'))
            *--end = 0;
        if(*input == 0)
            return "FeatureScope contains an empty feature";

        bool *flag = NULL;
        if(strcmp(input, "client") == 0)
            flag = &features->client;
        else if(strcmp(input, "server") == 0)
            flag = &features->server;
        else if(strcmp(input, "pubsub") == 0)
            flag = &features->pubsub;
        else
            return "FeatureScope contains an unknown feature";
        if(*flag)
            return "FeatureScope contains a duplicate feature";
        *flag = true;
        input = next;
    }

    if(features->pubsub && !features->server)
        return "FeatureScope enables pubsub without server";
    return NULL;
}

static int
namespace_array_grow(UA_UInt16 index) {
    size_t previous_capacity = namespace_entries_capacity;
    size_t capacity = namespace_entries_capacity
                          ? namespace_entries_capacity * 2
                          : O6_NAMESPACE_ARRAY_INITIAL_CAPACITY;
    while(capacity <= index)
        capacity *= 2;
    o6_NamespaceArrayEntry *entries =
        (o6_NamespaceArrayEntry *)PyMem_RawRealloc(
            namespace_entries, capacity * sizeof(*entries));
    if(!entries) {
        PyErr_NoMemory();
        return -1;
    }
    memset(entries + previous_capacity, 0,
           (capacity - previous_capacity) * sizeof(*entries));
    namespace_entries = entries;
    namespace_entries_capacity = capacity;
    return 0;
}

int
o6_namespace_array_register(const char *shortname, UA_UInt16 index,
                            PyObject *namespace_module) {
    if(namespace_array_shutting_down) {
        PyErr_SetString(PyExc_RuntimeError,
                        "namespace registry is shutting down");
        return -1;
    }
    if(!shortname || !shortname[0]) {
        PyErr_SetString(PyExc_ValueError, "namespace shortname must not be empty");
        return -1;
    }

    if(index >= namespace_entries_capacity && namespace_array_grow(index) < 0)
        return -1;

    for(size_t i = 0; i < namespace_entries_capacity; i++) {
        const o6_NamespaceArrayEntry *entry = &namespace_entries[i];
        if(entry->shortname && i != index &&
           strcmp(entry->shortname, shortname) == 0) {
            PyErr_Format(PyExc_ValueError,
                         "namespace shortname '%s' is already mapped to index %u",
                         shortname, (unsigned)i);
            return -1;
        }
    }

    o6_NamespaceArrayEntry *entry = &namespace_entries[index];
    if(entry->shortname) {
        if(strcmp(entry->shortname, shortname) != 0) {
            PyErr_Format(PyExc_ValueError,
                         "namespace index %u is already mapped to shortname '%s'",
                         (unsigned)index, entry->shortname);
            return -1;
        }
        if(namespace_module && namespace_module != Py_None) {
            Py_INCREF(namespace_module);
            Py_XSETREF(entry->namespace_module, namespace_module);
        }
        return 0;
    }

    size_t length = strlen(shortname);
    char *copy = (char *)PyMem_RawMalloc(length + 1);
    if(!copy) {
        PyErr_NoMemory();
        return -1;
    }
    memcpy(copy, shortname, length + 1);
    entry->shortname = copy;
    if(namespace_module && namespace_module != Py_None) {
        Py_INCREF(namespace_module);
        entry->namespace_module = namespace_module;
    }
    return 0;
}

bool
o6_namespace_array_index(const char *shortname, UA_UInt16 *index) {
    if(!shortname)
        return false;
    for(size_t i = 0; i < namespace_entries_capacity; i++) {
        const o6_NamespaceArrayEntry *entry = &namespace_entries[i];
        if(entry->shortname && strcmp(entry->shortname, shortname) == 0) {
            if(index)
                *index = (UA_UInt16)i;
            return true;
        }
    }
    return false;
}

const char *
o6_namespace_array_shortname(UA_UInt16 index) {
    if(index >= namespace_entries_capacity)
        return NULL;
    return namespace_entries[index].shortname;
}

bool
o6_namespace_resolve_token(const char *token, UA_UInt16 *index) {
    if(!namespace_token_resolver)
        return false;
    PyObject *result = PyObject_CallFunction(namespace_token_resolver, "s", token);
    if(!result) {
        PyErr_Clear();
        return false;
    }
    unsigned long value = PyLong_AsUnsignedLong(result);
    Py_DECREF(result);
    if((value == (unsigned long)-1 && PyErr_Occurred()) || value > UINT16_MAX) {
        PyErr_Clear();
        return false;
    }
    if(index)
        *index = (UA_UInt16)value;
    return true;
}

PyObject *
o6_namespace_module(UA_UInt16 index) {
    if(index < namespace_entries_capacity &&
       namespace_entries[index].namespace_module)
        return Py_NewRef(namespace_entries[index].namespace_module);
    return PyLong_FromUnsignedLong(index);
}

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
    PyObject *code = PyLong_FromUnsignedLong(err);
    if (!code)
        return NULL;
    PyErr_SetObject((PyObject*)&PyStatusCodeErrorType, code);
    Py_DECREF(code);
    return NULL;
}

/****************************/
/* Certificate Generation   */
/****************************/

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

static PyObject *
py_register_namespace(PyObject *self, PyObject *args) {
    (void)self;
    const char *shortname;
    unsigned short index;
    PyObject *namespace_module;
    if(!PyArg_ParseTuple(args, "sHO", &shortname, &index, &namespace_module))
        return NULL;
    if(o6_namespace_array_register(shortname, (UA_UInt16)index,
                                   namespace_module) < 0)
        return NULL;
    Py_RETURN_NONE;
}

static PyObject *
py_set_namespace_resolver(PyObject *self, PyObject *args) {
    (void)self;
    PyObject *token_resolver;
    if(!PyArg_ParseTuple(args, "O", &token_resolver))
        return NULL;
    if(!PyCallable_Check(token_resolver)) {
        PyErr_SetString(PyExc_TypeError, "namespace resolver must be callable");
        return NULL;
    }
    Py_INCREF(token_resolver);
    Py_XSETREF(namespace_token_resolver, token_resolver);
    Py_RETURN_NONE;
}

static PyObject *
py_register_datatype(PyObject *self, PyObject *args) {
    (void)self;
    const char *shortname;
    PyObject *description;
    PyObject *bases = Py_None;
    if(!PyArg_ParseTuple(args, "sO|O", &shortname, &description, &bases))
        return NULL;
    return o6_register_datatype(shortname, description, bases);
}

static PyObject *
py_require_client(PyObject *self, PyObject *Py_UNUSED(args)) {
    (void)self;
    if(o6_require_client() < 0)
        return NULL;
    Py_RETURN_NONE;
}

static PyObject *
py_require_server(PyObject *self, PyObject *Py_UNUSED(args)) {
    (void)self;
    if(o6_require_server() < 0)
        return NULL;
    Py_RETURN_NONE;
}

static PyObject *
py_require_pubsub(PyObject *self, PyObject *Py_UNUSED(args)) {
    (void)self;
    if(o6_require_pubsub() < 0)
        return NULL;
    Py_RETURN_NONE;
}

static PyObject *
py_parse_feature_scope(PyObject *self, PyObject *scopeObject) {
    (void)self;
    Py_ssize_t length;
    const char *scopeData = PyUnicode_AsUTF8AndSize(scopeObject, &length);
    if(!scopeData)
        return NULL;
    UA_String scope = {(size_t)length, (UA_Byte *)(uintptr_t)scopeData};
    o6_FeatureSet features;
    const char *error = o6_parse_feature_scope(&scope, &features);
    if(error) {
        PyErr_SetString(PyExc_ValueError, error);
        return NULL;
    }
    return Py_BuildValue("(OOO)",
                         features.client ? Py_True : Py_False,
                         features.server ? Py_True : Py_False,
                         features.pubsub ? Py_True : Py_False);
}

static PyMethodDef module_methods[] = {
    {"_register_namespace",
     (PyCFunction)py_register_namespace, METH_VARARGS,
     "Register a native namespace entry and its optional Python module."},
    {"_set_namespace_resolver", py_set_namespace_resolver, METH_VARARGS,
     "Install the Python namespace token resolver."},
    {"_register_datatype", py_register_datatype, METH_VARARGS,
     "Register a native custom datatype."},
    {"_require_client", py_require_client, METH_NOARGS,
     "Raise PermissionError unless Client is enabled by the active Credential."},
    {"_require_server", py_require_server, METH_NOARGS,
     "Raise PermissionError unless Server is enabled by the active Credential."},
    {"_require_pubsub", py_require_pubsub, METH_NOARGS,
     "Raise PermissionError unless PubSub is enabled by the active Credential."},
    {"_parse_feature_scope", py_parse_feature_scope, METH_O,
     "Validate a Credential FeatureScope without changing active entitlements."},
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
    {NULL, NULL, 0, NULL}
};

/*************************/
/* Module Initialization */
/*************************/

static void mod_free(void *Py_UNUSED(module)) {
    /* Detach every Python-visible root before running any decref.  Releasing a
     * namespace module can execute arbitrary finalizers; those must observe an
     * empty registry rather than a partially destroyed table. */
    namespace_array_shutting_down = true;
    o6_NamespaceArrayEntry *entries = namespace_entries;
    size_t capacity = namespace_entries_capacity;
    PyObject *token_resolver = namespace_token_resolver;
    namespace_entries = NULL;
    namespace_entries_capacity = 0;
    namespace_token_resolver = NULL;

    for(size_t i = 0; i < capacity; i++) {
        PyMem_RawFree(entries[i].shortname);
        Py_XDECREF(entries[i].namespace_module);
    }
    PyMem_RawFree(entries);
    Py_XDECREF(token_resolver);
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
    if(AsyncIOUDP_initTypes() < 0) {
        Py_DECREF(mod);
        mod = NULL;
        return NULL;
    }
    if(AsyncIOEthernet_initTypes() < 0) {
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

    /* The compiled API is always importable. Runtime entitlements are checked
     * when Client and Server objects are constructed. */
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

    /* Add server module */
    if(Server_initTypes() < 0) {
        Py_DECREF(mod);
        mod = NULL;
        return NULL;
    }

    PyObject *nodeBase = pyNodeBaseType();
    if(!nodeBase) {
        Py_DECREF(mod);
        mod = NULL;
        return NULL;
    }
    if(PyModule_AddObject(mod, "_NodeBase", nodeBase) < 0) {
        Py_DECREF(nodeBase);
        Py_DECREF(mod);
        mod = NULL;
        return NULL;
    }

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

    /* Add logging methods from logger.c */
    PyModule_AddFunctions(mod, pyLoggingMethods);

    /* Expose the open62541 threading level so Python can adapt */
    PyModule_AddIntConstant(mod, "MULTITHREADING", UA_MULTITHREADING);

    return mod;
}
