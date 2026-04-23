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
#ifndef MODULE_H_
#define MODULE_H_

#define NPY_TARGET_VERSION NPY_2_0_API_VERSION

// Use NumPy 2.x API for Python 3.11+
#ifndef NPY_NO_DEPRECATED_API
#define NPY_NO_DEPRECATED_API NPY_2_0_API_VERSION
#endif

#define PY_ARRAY_UNIQUE_SYMBOL o6_ARRAY_API
#define PY_SSIZE_T_CLEAN

#include <Python.h>

#include <open62541/client.h>
#include <open62541/client_highlevel.h>
#include <open62541/client_config_default.h>
#ifndef O6_NO_SERVER
#include <open62541/server.h>
#include <open62541/server_config_default.h>
#endif
#include <open62541/plugin/log.h>
#include <open62541/plugin/eventloop.h>

#ifdef UA_ENABLE_ENCRYPTION
#include <open62541/plugin/create_certificate.h>
#include <open62541/plugin/certificategroup_default.h>
#include <open62541/plugin/securitypolicy_default.h>
#include <open62541/plugin/log_stdout.h>
#endif

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
    void *pyClient; /* PyClient*, borrowed reference. Set by pyClient_init.
                     * Used by connection_lost for deferred cleanup. */
    void *pyServer; /* PyServer*, borrowed reference. Set by pyServer_init.
                     * Used by connection_lost for deferred cleanup. */
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

#define ASYNCIO_MAX_SOCKETS 32

struct AsyncIOConnectionManager {
    UA_ConnectionManager cm;
    AsyncIOConnection *connections[ASYNCIO_MAX_SOCKETS];
    AsyncIOListener *listeners[ASYNCIO_MAX_SOCKETS];
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

/* Must be called once during module initialization (PyInit__o6) to register
 * the PyType objects used by the event loop and TCP connection manager.
 * Calling PyType_Ready concurrently from multiple threads is not safe, so
 * these calls are lifted out of the per-client runtime paths. */
int AsyncIOEventLoop_initTypes(void);
int AsyncIOTCP_initTypes(void);

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

#ifndef O6_NO_SERVER
PyObject * pyServerModule(void);
#endif

/*********/
/* Types */
/*********/

PyObject * pyTypesModule(void);

/***********/
/* Returns Py_None on success. NULL for an exception. */
PyObject * PY2UA(PyObject *obj, void *p, const UA_DataType *type);
PyObject * UA2PY(void *p, const UA_DataType *type);

#endif // MODULE_H_
