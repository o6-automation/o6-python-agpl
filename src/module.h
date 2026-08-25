/* Copyright 2026 (c) o6 Automation GmbH (Author: Andreas Ebner) */
#ifndef MODULE_H_
#define MODULE_H_

#define NPY_TARGET_VERSION NPY_2_0_API_VERSION

// Keep one NumPy 2.x ABI target across every supported CPython version.
#ifndef NPY_NO_DEPRECATED_API
#define NPY_NO_DEPRECATED_API NPY_2_0_API_VERSION
#endif

#define PY_ARRAY_UNIQUE_SYMBOL o6_ARRAY_API
#define PY_SSIZE_T_CLEAN

/* MSVC's C compiler doesn't support the standard _Thread_local keyword. */
#ifdef _MSC_VER
#define O6_THREAD_LOCAL __declspec(thread)
#else
#define O6_THREAD_LOCAL _Thread_local
#endif

#include <Python.h>

#include <open62541/client.h>
#include <open62541/client_highlevel.h>
#include <open62541/client_config_default.h>
#include <open62541/server.h>
#include <open62541/server_config_default.h>
#include <open62541/plugin/log.h>
#include <open62541/plugin/eventloop.h>

#ifndef UA_ENABLE_ENCRYPTION
#error "o6 requires open62541 encryption support"
#endif

#include <open62541/plugin/create_certificate.h>
#include <open62541/plugin/certificategroup_default.h>
#include <open62541/plugin/securitypolicy_default.h>
#include <open62541/plugin/log_stdout.h>

#include "client/client.h"

#include "open62541_queue.h"

/* Logging: free-floating module-level functions (logging.c) */
UA_Logger *pyLogger(PyObject *pyLog);
extern PyMethodDef pyLoggingMethods[];

/******************/
/* Initialization */
/******************/

extern bool client_enabled;
extern bool server_enabled;
extern bool pubsub_enabled;

typedef struct {
    bool client;
    bool server;
    bool pubsub;
} o6_FeatureSet;

/* Parse a signed Credential FeatureScope without mutating active entitlement
 * state. Return NULL on success or a stable error description. */
const char *o6_parse_feature_scope(const UA_String *scope,
                                   o6_FeatureSet *features);

/* Runtime entitlement checks. Return 0 when enabled, otherwise set a Python
 * PermissionError and return -1. */
int o6_require_client(void);
int o6_require_server(void);
int o6_require_pubsub(void);

/* Process-global namespaces used by native type parsing and accessors. */
int o6_namespace_array_register(const char *shortname, UA_UInt16 index,
                                PyObject *namespace_module);
bool o6_namespace_array_index(const char *shortname, UA_UInt16 *index);
const char *o6_namespace_array_shortname(UA_UInt16 index);
bool o6_namespace_resolve_token(const char *token, UA_UInt16 *index);
PyObject *o6_namespace_module(UA_UInt16 index);

/* Check compatibility and print the welcome message */
bool o6_check_greet(void);
void o6_clean_shutdown(void);

/* Global variable with the build information */
extern UA_BuildInfo buildInfo;

/*************/
/* Eventloop */
/*************/

/* The client and server are 100% driven by the Python AsyncIO EventLoop. So the
 * current thread already has the GIL when we get a callback from Python. Assert
 * this to find potential issues early on. */
#define assertGIL() assert(PyGILState_Check())

struct PyUATimer;
typedef struct PyUATimer PyUATimer;

typedef struct {
    UA_EventLoop cLoop;
    PyObject *pyLoop; // Keep the refcount increased during the el lifetime
    UA_Lock elMutex;

    UA_DelayedCallback *delayed;

    LIST_HEAD(, PyUATimer) timers;
    LIST_HEAD(, PyUATimer) delayedTimers; /* tracks call_soon_threadsafe timers from addDelayedCallback */
    UA_UInt64 timerIndex;
    void *pyServer; /* PyServer*, borrowed reference. Set by pyServer_init. */
    int tearingDown; /* Set by tp_dealloc before el->stop / el->free to
                      * signal that Python API calls are unsafe (GC). */
} AsyncIOLoop;

struct AsyncIOConnectionManager;
typedef struct AsyncIOConnectionManager AsyncIOConnectionManager;

struct AsyncIOListener;
typedef struct AsyncIOListener AsyncIOListener;

// Instance of a Protocol class
typedef struct {
    PyObject_HEAD
    PyObject *transport;
    uintptr_t connectionId;
    AsyncIOConnectionManager *cm;
    UA_ConnectionManager_connectionCallback cb;
    void *application;
    void *context;
} AsyncIOConnection;

struct AsyncIOConnectionManager {
    UA_ConnectionManager cm;
    AsyncIOConnection **connections;
    size_t connectionsCapacity;
    AsyncIOListener **listeners;
    size_t listenersCapacity;
    size_t connectionCount;
    uintptr_t nextConnectionId; /* monotonic counter; starts at 1 so that
                                   connectionId 0 is never assigned (0 means
                                   "unused slot" in open62541's BPM) */
};

// pyLoop needs to expose the asyncio API
// logger needs to expose the logging API
UA_EventLoop * UA_EventLoop_new_AsyncIO(PyObject *pyLoop, PyObject *pyLog);

UA_ConnectionManager *
UA_ConnectionManager_new_AsyncIO_TCP();
UA_ConnectionManager *
UA_ConnectionManager_new_AsyncIO_UDP(void);
UA_ConnectionManager *
UA_ConnectionManager_new_AsyncIO_Ethernet(void);

/* Must be called once during module initialization (PyInit__o6) to register
 * the PyType objects used by the event loop and TCP connection manager.
 * Calling PyType_Ready concurrently from multiple threads is not safe, so
 * these calls are lifted out of the per-client runtime paths. */
int AsyncIOEventLoop_initTypes(void);
int AsyncIOTCP_initTypes(void);
int AsyncIOUDP_initTypes(void);
int AsyncIOEthernet_initTypes(void);

/**************/
/* Exceptions */
/**************/

extern PyObject *pyExc_StatusCode;
PyObject * PyErr_StatusCode(UA_StatusCode err);

/**********/
/* Logger */
/**********/

UA_Logger * pyLogger(PyObject *pyLog);

/**********/
/* Client */
/**********/

PyObject * pyClientModule(void);

/**********/
/* Server */
/**********/

PyObject * pyServerModule(void);

/*********/
/* Types */
/*********/

PyObject * pyTypesModule(void);

/***********/
/* Returns Py_None on success. NULL for an exception.
 * `nsMapping` is an optional Python<->UA namespace mapping applied AFTER
 * the conversion writes the raw indices. NULL means no translation. */
PyObject * PY2UA(PyObject *obj, void *p, const UA_DataType *type, const UA_NamespaceMapping *nm, const UA_DataTypeArray *localTypesArray);
PyObject * UA2PY(void *p, const UA_DataType *type, const UA_NamespaceMapping *nm);

/* Perform the namespace-mapping for an OPC UA DataType instance.
 * mapNamespaceUA2Py uses the global datatypes chain as the type-lookup
 * target (appropriate when reading data out of a server, since Python
 * wants the canonical global-type view).
 * mapNamespacePy2UA uses the per-client/per-server local customDataTypes
 * chain (appropriate when writing data to a server, since the wire format
 * needs server-local typeIds and the corresponding server-local types). */
void mapNamespaceUA2Py(void *p, const UA_DataType **type, const UA_NamespaceMapping *nm);
void mapNamespacePy2UA(void *p, const UA_DataType **type, const UA_NamespaceMapping *nm, const UA_DataTypeArray *customDataTypes);

#endif // MODULE_H_
