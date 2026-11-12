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

#include "module.h"
#include "eventloop/eventloop_common.h"

/* Configuration parameters */
#define TCP_PARAMETERSSIZE 5
#define TCP_PARAMINDEX_ADDR 0
#define TCP_PARAMINDEX_PORT 1
#define TCP_PARAMINDEX_LISTEN 2
#define TCP_PARAMINDEX_VALIDATE 3
#define TCP_PARAMINDEX_REUSE 4

static UA_KeyValueRestriction tcpConnectionParams[TCP_PARAMETERSSIZE];

/* MSVC does not allow &global_array[index] as a static initializer (C2099).
 * Initialize the array at runtime on first use instead. */
static void
init_tcpConnectionParams(void) {
    static int initialized = 0;
    if(initialized) return;
    initialized = 1;
    tcpConnectionParams[TCP_PARAMINDEX_ADDR]     = (UA_KeyValueRestriction){{0, UA_STRING_STATIC("address")},  &UA_TYPES[UA_TYPES_STRING],   false, true, true};
    tcpConnectionParams[TCP_PARAMINDEX_PORT]     = (UA_KeyValueRestriction){{0, UA_STRING_STATIC("port")},     &UA_TYPES[UA_TYPES_UINT16],   true,  true, false};
    tcpConnectionParams[TCP_PARAMINDEX_LISTEN]   = (UA_KeyValueRestriction){{0, UA_STRING_STATIC("listen")},   &UA_TYPES[UA_TYPES_BOOLEAN],  false, true, false};
    tcpConnectionParams[TCP_PARAMINDEX_VALIDATE] = (UA_KeyValueRestriction){{0, UA_STRING_STATIC("validate")}, &UA_TYPES[UA_TYPES_BOOLEAN],  false, true, false};
    tcpConnectionParams[TCP_PARAMINDEX_REUSE]    = (UA_KeyValueRestriction){{0, UA_STRING_STATIC("reuse")},    &UA_TYPES[UA_TYPES_BOOLEAN],  false, true, false};
}


/******************/
/* Protocol Class */
/******************/

// The "factory" pass into create_connection
// So we already have a lot of context
static PyObject *
TCPProtocol_call(PyObject *self, PyObject *args, PyObject *kwargs) {
    Py_INCREF(self);
    return self;
}

static PyObject *
TCPProtocol_connection_made(AsyncIOConnection *self, PyObject *args) {
    PyObject *transport;
    if(!PyArg_ParseTuple(args, "O", &transport))
        return NULL;
    if(!self->cm)
        return PyObject_CallMethod(transport, "close", NULL);

    AsyncIOLoop *el = (AsyncIOLoop*)self->cm->cm.eventSource.eventLoop;
    UA_LOG_DEBUG(el->cLoop.logger, UA_LOGCATEGORY_EVENTLOOP, "connection made");

    // Already have a transport
    if(self->transport)
        return NULL;

    // Set the new transport
    Py_INCREF(transport);
    self->transport = transport;

    UA_LOG_DEBUG(self->cm->cm.eventSource.eventLoop->logger, UA_LOGCATEGORY_NETWORK,
                 "TCP %zu\t| Opened a connection", (unsigned)self->connectionId);

    // Notify the application the connection has opened
    self->notified = true;
    self->cb(&self->cm->cm, self->connectionId, self->application,
             &self->context, UA_CONNECTIONSTATE_ESTABLISHED,
             &UA_KEYVALUEMAP_NULL, UA_BYTESTRING_NULL);
    if(PyErr_Occurred())
        return NULL;
    Py_RETURN_NONE;
}

static PyObject *
TCPProtocol_data_received(AsyncIOConnection *self, PyObject *args) {
    if(!self->cm)
        Py_RETURN_NONE;

    AsyncIOLoop *el = (AsyncIOLoop*)self->cm->cm.eventSource.eventLoop;
    UA_LOG_DEBUG(el->cLoop.logger, UA_LOGCATEGORY_EVENTLOOP, "Receive data");

    // Proactor transports deliver bytearray; keep the buffer pinned during processing.
    Py_buffer buffer;
    if(!PyArg_ParseTuple(args, "y*", &buffer))
        return NULL;
    UA_ByteString msg = {(size_t)buffer.len, (UA_Byte*)buffer.buf};

    // Forward to the application
    self->cb(&self->cm->cm, self->connectionId, self->application,
             &self->context, UA_CONNECTIONSTATE_ESTABLISHED,
             &UA_KEYVALUEMAP_NULL, msg);
    PyBuffer_Release(&buffer);
    if(PyErr_Occurred())
        return NULL;

    Py_RETURN_NONE;
}

static PyObject *
TCPProtocol_eof_received(AsyncIOConnection *self, PyObject *args) {
    Py_RETURN_NONE;
}

static PyObject *
TCPProtocol_connection_lost(AsyncIOConnection *self, PyObject *args) {
    /* self->cm is set to NULL by AsyncIOTCP_eventSourceStop when the
     * ConnectionManager is torn down during client cleanup.  asyncio may still
     * deliver this callback afterwards (it was already queued); treat that as
     * a benign no-op so we don't touch the freed CM struct. */
    if(!self->cm) {
        Py_RETURN_NONE;
    }

    AsyncIOLoop *el = (AsyncIOLoop*)self->cm->cm.eventSource.eventLoop;

    // Remove self from the list
    AsyncIOConnectionManager *cm = self->cm;
    bool ownedByManager = false;
    for(size_t i = 0; i < cm->connectionsCapacity; i++) {
        if(cm->connections[i] == self) {
            cm->connections[i] = NULL;
            cm->connectionCount--;
            ownedByManager = true;
            break;
        }
    }

    // From Shutdown to closing?
    if(cm->cm.eventSource.state == UA_EVENTSOURCESTATE_STOPPING &&
       cm->connectionCount == 0) {
        cm->cm.eventSource.state = UA_EVENTSOURCESTATE_STOPPED;
    }

    // Signal closing to the application
    if(self->notified) {
        self->cb(&self->cm->cm, self->connectionId, self->application,
                 &self->context, UA_CONNECTIONSTATE_CLOSING,
                 &UA_KEYVALUEMAP_NULL, UA_BYTESTRING_NULL);
    }

    /* Tracebacks can keep the protocol alive after the manager is freed. */
    self->cm = NULL;
    if(ownedByManager)
        Py_DECREF(self); /* release connections[] ownership */

    Py_RETURN_NONE;
}

static void
TCPProtocol_dealloc(AsyncIOConnection *self) {
    /* cm is a borrowed native pointer and may already have been released. */
    Py_XDECREF(self->transport);
    Py_TYPE(self)->tp_free((PyObject *)self);
}

static PyMethodDef TCPProtocol_methods[] = {
    {"connection_made", (PyCFunction)TCPProtocol_connection_made, METH_VARARGS, NULL},
    {"data_received", (PyCFunction)TCPProtocol_data_received, METH_VARARGS, NULL},
    {"eof_received", (PyCFunction)TCPProtocol_eof_received, METH_VARARGS, NULL},
    {"connection_lost", (PyCFunction)TCPProtocol_connection_lost, METH_VARARGS, NULL},
    {NULL, NULL, 0, NULL}
};

static PyTypeObject TCPProtocolType = {
    PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "o6._o6.TCPProtocol",
    .tp_basicsize = sizeof(AsyncIOConnection),
    .tp_dealloc = (destructor)TCPProtocol_dealloc,
    .tp_flags = Py_TPFLAGS_DEFAULT,
    .tp_methods = TCPProtocol_methods,
    .tp_call = TCPProtocol_call,
    .tp_new = PyType_GenericNew,
};

/***********************/
/* Listener (Passive)  */
/***********************/

/* An AsyncIOListener acts as a protocol_factory for asyncio.create_server().
 * Each time a new TCP client connects, asyncio calls listener() which
 * creates a fresh AsyncIOConnection (Protocol) for that client. */
struct AsyncIOListener {
    PyObject_HEAD
    AsyncIOConnectionManager *cm;
    UA_ConnectionManager_connectionCallback cb;
    void *application;
    void *context;
    uintptr_t listenConnectionId;
    PyObject *asyncioServer;  /* asyncio.Server object, to close later */
    PyObject *taskRef; /* Weak reference: the task already owns the listener. */
    UA_String host;    /* Requested host; empty when listening on all interfaces */
    UA_UInt16 port;    /* Requested port; 0 selects a free port */
};

/* Returns a new reference to the listener task, or NULL if it is gone.
 * PyWeakref_GetObject was removed from the 3.15 headers. */
static PyObject *
getListenerTask(AsyncIOListener *listener) {
    PyObject *task = NULL;
#if PY_VERSION_HEX >= 0x030D0000
    if(PyWeakref_GetRef(listener->taskRef, &task) < 0)
        PyErr_Clear();
#else
    task = PyWeakref_GetObject(listener->taskRef);
    if(!task)
        PyErr_Clear();
    else if(task == Py_None)
        task = NULL;
    else
        Py_INCREF(task);
#endif
    return task;
}

/* Snapshot startup tasks before returning control to asyncio. */
PyObject *
AsyncIOTCP_listenerTasks(UA_EventLoop *el) {
    PyObject *tasks = PyList_New(0);
    if(!tasks)
        return NULL;
    for(UA_EventSource *es = el->eventSources; es; es = es->next) {
        if(es->eventSourceType != UA_EVENTSOURCETYPE_CONNECTIONMANAGER)
            continue;
        UA_ConnectionManager *cm = (UA_ConnectionManager*)es;
        UA_String tcp = UA_STRING("tcp");
        if(!UA_String_equal(&cm->protocol, &tcp))
            continue;
        AsyncIOConnectionManager *acm = (AsyncIOConnectionManager*)cm;
        for(size_t i = 0; i < acm->listenersCapacity; i++) {
            AsyncIOListener *listener = acm->listeners[i];
            if(!listener || !listener->taskRef)
                continue;
            PyObject *task = getListenerTask(listener);
            if(!task)
                continue;
            int res = PyList_Append(tasks, task);
            Py_DECREF(task);
            if(res < 0) {
                Py_DECREF(tasks);
                return NULL;
            }
        }
    }
    return tasks;
}

static void
cancelListenerTask(AsyncIOListener *listener) {
    if(!listener->taskRef)
        return;
    PyObject *task = getListenerTask(listener);
    if(task) {
        PyObject *result = PyObject_CallMethod(task, "cancel", NULL);
        if(!result) PyErr_Clear();
        Py_XDECREF(result);
        Py_DECREF(task);
    }
}

static AsyncIOConnection **
reserveConnectionSlot(AsyncIOConnectionManager *acm) {
    for(size_t i = 0; i < acm->connectionsCapacity; i++) {
        if(!acm->connections[i])
            return &acm->connections[i];
    }
    size_t oldCapacity = acm->connectionsCapacity;
    size_t newCapacity = oldCapacity ? oldCapacity * 2 : 8;
    if(newCapacity < oldCapacity ||
       newCapacity > SIZE_MAX / sizeof(AsyncIOConnection *)) {
        PyErr_NoMemory();
        return NULL;
    }
    AsyncIOConnection **resized = (AsyncIOConnection **)UA_realloc(
        acm->connections, newCapacity * sizeof(AsyncIOConnection *));
    if(!resized) {
        PyErr_NoMemory();
        return NULL;
    }
    memset(&resized[oldCapacity], 0,
           (newCapacity - oldCapacity) * sizeof(AsyncIOConnection *));
    acm->connections = resized;
    acm->connectionsCapacity = newCapacity;
    return &resized[oldCapacity];
}

static AsyncIOListener **
reserveListenerSlot(AsyncIOConnectionManager *acm) {
    for(size_t i = 0; i < acm->listenersCapacity; i++) {
        if(!acm->listeners[i])
            return &acm->listeners[i];
    }
    size_t oldCapacity = acm->listenersCapacity;
    size_t newCapacity = oldCapacity ? oldCapacity * 2 : 4;
    if(newCapacity < oldCapacity ||
       newCapacity > SIZE_MAX / sizeof(AsyncIOListener *)) {
        PyErr_NoMemory();
        return NULL;
    }
    AsyncIOListener **resized = (AsyncIOListener **)UA_realloc(
        acm->listeners, newCapacity * sizeof(AsyncIOListener *));
    if(!resized) {
        PyErr_NoMemory();
        return NULL;
    }
    memset(&resized[oldCapacity], 0,
           (newCapacity - oldCapacity) * sizeof(AsyncIOListener *));
    acm->listeners = resized;
    acm->listenersCapacity = newCapacity;
    return &resized[oldCapacity];
}

static PyObject *
AsyncIOListener_call(AsyncIOListener *self, PyObject *args, PyObject *kwargs) {
    /* A queued accept can outlive the listener. A detached protocol closes
     * its transport in connection_made without touching the native server. */
    if(!self->cm)
        return TCPProtocolType.tp_new(&TCPProtocolType, NULL, NULL);

    AsyncIOConnectionManager *acm = self->cm;
    AsyncIOLoop *el = (AsyncIOLoop*)acm->cm.eventSource.eventLoop;

    AsyncIOConnection **slot = reserveConnectionSlot(acm);
    if(!slot)
        return NULL;

    /* Create a new Protocol for the accepted client */
    AsyncIOConnection *cc = (AsyncIOConnection *)
        TCPProtocolType.tp_new(&TCPProtocolType, NULL, NULL);
    if(!cc)
        return NULL;

    cc->connectionId = acm->nextConnectionId++;
    acm->connectionCount++;
    cc->cm = acm;
    cc->cb = self->cb;
    cc->application = self->application;
    cc->context = self->context;  /* Inherit the listener's context so that the
                                   * server components see the existing serverConnection slot
                                   * instead of registering a second one. */

    /* Store in the connections array (extra ref for the array) */
    *slot = cc;
    Py_INCREF(cc);

    UA_LOG_DEBUG(el->cLoop.logger, UA_LOGCATEGORY_NETWORK,
                 "TCP %zu\t| Accepted a new client connection",
                 (unsigned)cc->connectionId);
    return (PyObject*)cc;
}

static void
AsyncIOListener_dealloc(AsyncIOListener *self) {
    Py_XDECREF(self->taskRef);
    Py_XDECREF(self->asyncioServer);
    UA_String_clear(&self->host);
    Py_TYPE(self)->tp_free((PyObject *)self);
}

static PyTypeObject ListenerType = {
    PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "o6._o6.TCPListener",
    .tp_basicsize = sizeof(AsyncIOListener),
    .tp_dealloc = (destructor)AsyncIOListener_dealloc,
    .tp_flags = Py_TPFLAGS_DEFAULT,
    .tp_call = (ternaryfunc)AsyncIOListener_call,
    .tp_new = PyType_GenericNew,
};

/* Describe the listen socket like the POSIX EventLoop does. open62541 derives
 * the DiscoveryUrls of a server from "listen-address" and "listen-port".
 * The wildcard reports the local hostname. IPv6 literals are bracketed so
 * that the resulting URL remains parseable. The caller clears *address. */
static void
listenerAddress(const AsyncIOListener *listener, PyObject *asyncioServer,
                UA_String *address, UA_UInt16 *port) {
    /* The bound port also covers port 0 */
    *port = listener->port;
    PyObject *sockets = PyObject_GetAttrString(asyncioServer, "sockets");
    PyObject *sock = (sockets && PySequence_Size(sockets) > 0)
        ? PySequence_GetItem(sockets, 0) : NULL;
    PyObject *name = sock ? PyObject_CallMethod(sock, "getsockname", NULL) : NULL;
    PyObject *boundPort = name ? PySequence_GetItem(name, 1) : NULL;
    if(boundPort) {
        long value = PyLong_AsLong(boundPort);
        if(value > 0 && value <= UINT16_MAX)
            *port = (UA_UInt16)value;
    }
    Py_XDECREF(boundPort);
    Py_XDECREF(name);
    Py_XDECREF(sock);
    Py_XDECREF(sockets);
    PyErr_Clear();

    UA_String_init(address);
    UA_String host = listener->host;
    PyObject *hostname = NULL;
    if(host.length == 0) {
        PyObject *socketModule = PyImport_ImportModule("socket");
        hostname = socketModule
            ? PyObject_CallMethod(socketModule, "gethostname", NULL) : NULL;
        Py_XDECREF(socketModule);
        Py_ssize_t len = 0;
        const char *utf8 = hostname ? PyUnicode_AsUTF8AndSize(hostname, &len) : NULL;
        if(!utf8 || len == 0) {
            Py_XDECREF(hostname);
            PyErr_Clear();
            return;
        }
        host.data = (UA_Byte*)(uintptr_t)utf8;
        host.length = (size_t)len;
    }

    UA_Boolean ipv6 = host.data[0] != '[' && memchr(host.data, ':', host.length);
    size_t length = host.length + (ipv6 ? 2 : 0);
    address->data = (UA_Byte*)UA_malloc(length);
    if(address->data) {
        address->length = length;
        if(ipv6) {
            address->data[0] = '[';
            address->data[length - 1] = ']';
        }
        memcpy(&address->data[ipv6 ? 1 : 0], host.data, host.length);
    }
    Py_XDECREF(hostname);
}

static PyObject *
TCP_listen_done_callback(PyObject *self, PyObject *args) {
    PyObject *task;
    if(!PyArg_ParseTuple(args, "O", &task))
        return NULL;

    AsyncIOListener *listener = (AsyncIOListener *)
        PyObject_GetAttrString(task, "_listener");
    if(!listener)
        return NULL;

    Py_CLEAR(listener->taskRef);

    /* The ConnectionManager may have been torn down */
    if(!listener->cm) {
        /* A cancelled/closed listener must never reopen a socket or call
         * back into an application that has already shut down. */
        PyObject *result = PyObject_CallMethod(task, "result", NULL);
        if(result) {
            PyObject *closed = PyObject_CallMethod(result, "close", NULL);
            Py_XDECREF(closed);
            Py_DECREF(result);
        }
        PyErr_Clear();
        Py_DECREF(listener);
        Py_RETURN_NONE;
    }

    AsyncIOConnectionManager *acm = listener->cm;
    AsyncIOLoop *el = (AsyncIOLoop*)acm->cm.eventSource.eventLoop;
    UA_LOG_DEBUG(el->cLoop.logger, UA_LOGCATEGORY_EVENTLOOP, "tcp listen done");

    /* Check if the coroutine raised an exception */
    PyObject *exc = PyObject_CallMethod(task, "exception", NULL);
    if(!exc) {
        PyErr_Print();
        goto errout;
    }
    if(exc != Py_None) {
        PyErr_Format(PyExc_RuntimeError, "TCP listen failed: %R", exc);
        PyErr_Print();
        Py_DECREF(exc);
        goto errout;
    }
    Py_DECREF(exc);

    /* Get the asyncio.Server result */
    PyObject *result = PyObject_CallMethod(task, "result", NULL);
    if(!result) {
        PyErr_Print();
        goto errout;
    }

    listener->asyncioServer = result; /* takes ownership */

    UA_LOG_DEBUG(el->cLoop.logger, UA_LOGCATEGORY_NETWORK,
                 "TCP %zu\t| Listening", (unsigned)listener->listenConnectionId);

    /* Notify the application that we are listening */
    UA_String listenAddress;
    UA_UInt16 listenPort;
    listenerAddress(listener, result, &listenAddress, &listenPort);
    UA_KeyValuePair params[2];
    params[0].key = UA_QUALIFIEDNAME(0, "listen-address");
    UA_Variant_setScalar(&params[0].value, &listenAddress, &UA_TYPES[UA_TYPES_STRING]);
    params[1].key = UA_QUALIFIEDNAME(0, "listen-port");
    UA_Variant_setScalar(&params[1].value, &listenPort, &UA_TYPES[UA_TYPES_UINT16]);
    UA_KeyValueMap paramMap = {listenAddress.length > 0 ? 2 : 0, params};
    listener->cb(&listener->cm->cm, listener->listenConnectionId,
                 listener->application, &listener->context,
                 UA_CONNECTIONSTATE_ESTABLISHED,
                 &paramMap, UA_BYTESTRING_NULL);
    UA_String_clear(&listenAddress);

    Py_DECREF(listener);
    Py_RETURN_NONE;

 errout:
    /* Notify the application that the listen failed */
    if(listener->cb) {
        listener->cb(&listener->cm->cm, listener->listenConnectionId,
                     listener->application, &listener->context,
                     UA_CONNECTIONSTATE_CLOSING,
                     &UA_KEYVALUEMAP_NULL, UA_BYTESTRING_NULL);
    }
    /* Remove from listeners array */
    for(size_t i = 0; i < acm->listenersCapacity; i++) {
        if(acm->listeners[i] == listener) {
            acm->listeners[i] = NULL;
            Py_DECREF(listener);
            break;
        }
    }
    Py_DECREF(listener);
    Py_RETURN_NONE;
}

static PyMethodDef listen_callback_def = {
    "TCP_listen_done_callback",
    (PyCFunction)TCP_listen_done_callback,
    METH_VARARGS,
    "Callback when TCP listen task is done"
};

/* Open a passive (listening) TCP connection */
static UA_StatusCode
AsyncIOTCP_openPassiveConnection(AsyncIOConnectionManager *acm,
                                 const UA_KeyValueMap *params,
                                 void *application, void *context,
                                 UA_ConnectionManager_connectionCallback cb,
                                 UA_Boolean validate) {
    AsyncIOLoop *el = (AsyncIOLoop*)acm->cm.eventSource.eventLoop;
    UA_LOG_DEBUG(el->cLoop.logger, UA_LOGCATEGORY_EVENTLOOP, "open passive connection");
    UA_LOCK_ASSERT(&el->elMutex);

    if(validate)
        return UA_STATUSCODE_GOOD;

    /* Parse port */
    const UA_UInt16 *uport = (const UA_UInt16*)
        UA_KeyValueMap_getScalar(params, tcpConnectionParams[TCP_PARAMINDEX_PORT].name,
                                 &UA_TYPES[UA_TYPES_UINT16]);
    if(!uport) {
        UA_LOG_ERROR(el->cLoop.logger, UA_LOGCATEGORY_NETWORK,
                     "TCP\t| No port defined for listen");
        return UA_STATUSCODE_BADINTERNALERROR;
    }
    int port = *uport;

    /* Check reuse flag */
    UA_Boolean reuse = true;
    const UA_Boolean *reuseParam = (const UA_Boolean*)
        UA_KeyValueMap_getScalar(params, tcpConnectionParams[TCP_PARAMINDEX_REUSE].name,
                                 &UA_TYPES[UA_TYPES_BOOLEAN]);
    if(reuseParam)
        reuse = *reuseParam;

    AsyncIOListener **slot = reserveListenerSlot(acm);
    if(!slot) {
        PyErr_Clear();
        return UA_STATUSCODE_BADOUTOFMEMORY;
    }

    /* Create the Listener (acts as protocol_factory) */
    AsyncIOListener *listener = (AsyncIOListener *)
        ListenerType.tp_new(&ListenerType, NULL, NULL);
    if(!listener) {
        PyErr_Print();
        return UA_STATUSCODE_BADINTERNALERROR;
    }

    listener->cm = acm;
    listener->cb = cb;
    listener->application = application;
    listener->context = context;
    listener->listenConnectionId = acm->nextConnectionId++;
    listener->asyncioServer = NULL;
    listener->port = (UA_UInt16)port;

    /* The helper prepares asyncio's listener before it begins accepting. */
    PyObject *py_reuse = reuse ? Py_True : Py_False;

    PyObject *module = PyImport_ImportModule("o6._eventloop");
    PyObject *method = module ? PyObject_GetAttrString(module, "create_listener") : NULL;
    Py_XDECREF(module);
    if(!method) {
        PyErr_Print();
        Py_DECREF(listener);
        return UA_STATUSCODE_BADINTERNALERROR;
    }
    /* The native server supplies an address array, while reverse listeners can
     * supply a scalar. asyncio accepts both a host string and a list of hosts.
     * Without an address, host None binds every interface of every address
     * family (IPv4 and IPv6), like the POSIX EventLoop. */
    const UA_Variant *addresses = UA_KeyValueMap_get(
        params, tcpConnectionParams[TCP_PARAMINDEX_ADDR].name);
    PyObject *hosts = NULL;
    if(!addresses || !addresses->data || addresses->data == UA_EMPTY_ARRAY_SENTINEL) {
        hosts = Py_NewRef(Py_None);
    } else if(addresses->type == &UA_TYPES[UA_TYPES_STRING]) {
        size_t count = UA_Variant_isScalar(addresses) ? 1 : addresses->arrayLength;
        const UA_String *strings = (const UA_String*)addresses->data;
        /* The first address names the listener in its DiscoveryUrl */
        if(count > 0 && UA_String_copy(&strings[0], &listener->host) != UA_STATUSCODE_GOOD)
            PyErr_NoMemory();
        else
            hosts = PyList_New((Py_ssize_t)count);
        if(hosts) {
            for(size_t i = 0; i < count; i++) {
                PyObject *host = PyUnicode_FromStringAndSize(
                    (const char*)strings[i].data, (Py_ssize_t)strings[i].length);
                if(!host) {
                    Py_CLEAR(hosts);
                    break;
                }
                PyList_SET_ITEM(hosts, (Py_ssize_t)i, host);
            }
        }
    } else {
        PyErr_SetString(PyExc_TypeError, "TCP listener addresses must be strings");
    }
    PyObject *posargs = NULL;
    if(hosts)
        posargs = Py_BuildValue("(OOOi)", el->pyLoop, listener, hosts, port);
    Py_XDECREF(hosts);
    if(!posargs) {
        PyErr_Print();
        Py_DECREF(method);
        Py_DECREF(listener);
        return UA_STATUSCODE_BADINTERNALERROR;
    }
    PyObject *kwargs = PyDict_New();
    if(!kwargs) {
        PyErr_Print();
        Py_DECREF(posargs);
        Py_DECREF(method);
        Py_DECREF(listener);
        return UA_STATUSCODE_BADINTERNALERROR;
    }
    PyDict_SetItemString(kwargs, "reuse_address", py_reuse);
    PyObject *coro = PyObject_Call(method, posargs, kwargs);
    Py_DECREF(kwargs);
    Py_DECREF(posargs);
    Py_DECREF(method);
    if(!coro) {
        PyErr_Print();
        Py_DECREF(listener);
        return UA_STATUSCODE_BADINTERNALERROR;
    }

    /* Wrap in a task */
    PyObject *task = PyObject_CallMethod(el->pyLoop, "create_task", "O", coro);
    Py_DECREF(coro);
    if(!task) {
        PyErr_Print();
        Py_DECREF(listener);
        return UA_STATUSCODE_BADINTERNALERROR;
    }

    /* Attach listener reference to task */
    if(PyObject_SetAttrString(task, "_listener", (PyObject*)listener) < 0) {
        PyErr_Print();
        Py_DECREF(listener);
        Py_DECREF(task);
        return UA_STATUSCODE_BADINTERNALERROR;
    }

    /* Add done callback */
    PyObject *py_callback = PyCFunction_New(&listen_callback_def, NULL);
    if(!py_callback) {
        PyErr_Print();
        Py_DECREF(listener);
        Py_DECREF(task);
        return UA_STATUSCODE_BADINTERNALERROR;
    }
    PyObject *res = PyObject_CallMethod(task, "add_done_callback", "O", py_callback);
    Py_DECREF(py_callback);
    listener->taskRef = PyWeakref_NewRef(task, NULL);
    Py_DECREF(task);
    if(!res || !listener->taskRef) {
        Py_XDECREF(res);
        PyErr_Print();
        Py_DECREF(listener);
        return UA_STATUSCODE_BADINTERNALERROR;
    }
    Py_DECREF(res);

    /* Store the listener */
    *slot = listener;

    UA_LOG_DEBUG(el->cLoop.logger, UA_LOGCATEGORY_NETWORK,
                 "TCP %zu\t| Opening a listen socket on port %i",
                 (unsigned)listener->listenConnectionId, port);

    return UA_STATUSCODE_GOOD;
}

/****************************/
/* Active (Client) Connect  */
/****************************/

static UA_StatusCode
AsyncIOTCP_sendWithConnection(UA_ConnectionManager *cm, uintptr_t connectionId,
                              const UA_KeyValueMap *params, UA_ByteString *buf) {
    AsyncIOLoop *el = (AsyncIOLoop*)cm->eventSource.eventLoop;
    UA_LOG_DEBUG(el->cLoop.logger, UA_LOGCATEGORY_EVENTLOOP, "send");

    // Find the connection
    AsyncIOConnectionManager *acm = (AsyncIOConnectionManager*)cm;
    AsyncIOConnection *c = NULL;
    for(size_t i = 0; i < acm->connectionsCapacity; i++) {
        if(acm->connections[i] && acm->connections[i]->connectionId == connectionId) {
            c = acm->connections[i];
            break;
        }
    }

    /* The connection manager takes ownership of the send buffer and must
     * release it on every return path, success or failure, matching the
     * open62541 sendWithConnection contract.  */
    if(!c || !c->transport) {
        cm->freeNetworkBuffer(cm, connectionId, buf);
        return UA_STATUSCODE_BADINTERNALERROR;
    }

    // Create a Python bytes object
    PyObject *py_bytes = PyBytes_FromStringAndSize((const char *)buf->data, buf->length);
    if(!py_bytes) {
        PyErr_Print();
        cm->freeNetworkBuffer(cm, connectionId, buf);
        return UA_STATUSCODE_BADINTERNALERROR;
    }

    // Call transport.write(data)
    PyObject *result = PyObject_CallMethod(c->transport, "write", "O", py_bytes);
    Py_DECREF(py_bytes);
    cm->freeNetworkBuffer(cm, connectionId, buf);

    // Handle errors
    if(!result) {
        PyErr_Print();  // Python exception occurred
        return UA_STATUSCODE_BADINTERNALERROR;
    }

    Py_DECREF(result);
    return UA_STATUSCODE_GOOD;
}

static UA_StatusCode
AsyncIOTCP_shutdownConnection(UA_ConnectionManager *cm, uintptr_t connectionId) {
    AsyncIOConnectionManager *acm = (AsyncIOConnectionManager*)cm;
    AsyncIOLoop *el = (AsyncIOLoop*)cm->eventSource.eventLoop;
    UA_LOG_DEBUG(el->cLoop.logger, UA_LOGCATEGORY_EVENTLOOP,
                 "shutdown connection %zu", (size_t)connectionId);
    /* Check listeners first */
    for(size_t i = 0; i < acm->listenersCapacity; i++) {
        if(acm->listeners[i] &&
           acm->listeners[i]->listenConnectionId == connectionId) {
            AsyncIOListener *listener = acm->listeners[i];
            acm->listeners[i] = NULL;
            if(listener->asyncioServer) {
                PyObject *result =
                    PyObject_CallMethod(listener->asyncioServer, "close", NULL);
                Py_XDECREF(result);
            }
            /* Notify the application that the listen connection is closing */
            listener->cb(&listener->cm->cm, listener->listenConnectionId,
                         listener->application, &listener->context,
                         UA_CONNECTIONSTATE_CLOSING,
                         &UA_KEYVALUEMAP_NULL, UA_BYTESTRING_NULL);
            listener->cm = NULL;
            cancelListenerTask(listener);
            Py_DECREF(listener);
            return UA_STATUSCODE_GOOD;
        }
    }

    /* Find the connection and close its transport so that asyncio stops
     * delivering data and eventually calls connection_lost. */
    for(size_t i = 0; i < acm->connectionsCapacity; i++) {
        if(acm->connections[i] &&
           acm->connections[i]->connectionId == connectionId) {
            AsyncIOConnection *conn = acm->connections[i];
            if(conn->transport) {
                PyObject *result =
                    PyObject_CallMethod(conn->transport, "close", NULL);
                Py_XDECREF(result);
            }
            break;
        }
    }
    return UA_STATUSCODE_GOOD;
}

static PyObject *
TCP_open_done_callback(PyObject *self, PyObject *args) {
    PyObject *task;
    if(!PyArg_ParseTuple(args, "O", &task)) {
        PyErr_SetString(PyExc_RuntimeError, "TCP opening coroutine task invalid");
        return NULL;
    }

    AsyncIOConnection *c = (AsyncIOConnection *)
        PyObject_GetAttrString(task, "_connection");
    if(!c) {
        PyErr_SetString(PyExc_RuntimeError, "TCP opening coroutine task invalid");
        return NULL;
    }

    /* The ConnectionManager may have been torn down while this task was
     * pending (e.g. client was destroyed).  Bail out safely. */
    if(!c->cm) {
        Py_DECREF(c);
        Py_RETURN_NONE;
    }

    AsyncIOConnectionManager *cm = (AsyncIOConnectionManager*)c->cm;
    AsyncIOLoop *el = (AsyncIOLoop*)cm->cm.eventSource.eventLoop;
    UA_LOG_DEBUG(el->cLoop.logger, UA_LOGCATEGORY_EVENTLOOP, "tcp open done");

    PyObject *result = NULL;

    // Check if the coroutine raised an exception
    PyObject *exc = PyObject_CallMethod(task, "exception", NULL);
    if(!exc) {
        PyErr_Print();
        goto errout;
    }

    // Print the exception
    if(exc != Py_None) {
        PyErr_Format(PyExc_RuntimeError, "TCP opening coroutine failed %R", exc);
        PyErr_Print();
        Py_DECREF(exc);
        goto errout;
    }

    Py_DECREF(exc); // exc == Py_None

    // Result is correct?
    result = PyObject_CallMethod(task, "result", NULL);
    if(!result) {
        PyErr_Print();
        goto errout;
    }

    // The good case.
    // The connection was already signaled in connection_made.
    Py_DECREF(result);
    Py_DECREF(c);
    Py_RETURN_NONE;

 errout:
    // Remove self from the list
    for(size_t i = 0; i < cm->connectionsCapacity; i++) {
        if(cm->connections[i] == c) {
            cm->connections[i] = NULL;
            cm->connectionCount--;
            Py_DECREF(c);
            break;
        }
    }

    // Notify the application that the connection failed
    c->cb(&c->cm->cm, c->connectionId, c->application,
          &c->context, UA_CONNECTIONSTATE_CLOSING,
          &UA_KEYVALUEMAP_NULL, UA_BYTESTRING_NULL);

    // Twice, once for the map-lookup and once for the list
    Py_DECREF(c);
    Py_RETURN_NONE;
}

static PyMethodDef callback_def = {
    "TCP_open_done_callback",  // Name of the callable
    (PyCFunction)TCP_open_done_callback,
    METH_VARARGS,
    "Callback when TCP connection task is done"
};

/* Open a TCP connection to a remote host */
static UA_StatusCode
AsyncIOTCP_openActiveConnection(AsyncIOConnectionManager *acm,
                                const UA_KeyValueMap *params,
                                void *application, void *context,
                                UA_ConnectionManager_connectionCallback connectionCallback,
                                UA_Boolean validate) {
    AsyncIOLoop *el = (AsyncIOLoop*)acm->cm.eventSource.eventLoop;
    UA_LOG_DEBUG(el->cLoop.logger, UA_LOGCATEGORY_EVENTLOOP, "open active connection");
    UA_LOCK_ASSERT(&el->elMutex);

    if(validate)
        return UA_STATUSCODE_GOOD;

    AsyncIOConnection **c = reserveConnectionSlot(acm);
    if(!c) {
        PyErr_Clear();
        return UA_STATUSCODE_BADOUTOFMEMORY;
    }

    // Set up the connection parameters
    int port;
    char hostname[512];

    /* Prepare the port parameter as a string */
    const UA_UInt16 *uport = (const UA_UInt16*)
        UA_KeyValueMap_getScalar(params, tcpConnectionParams[TCP_PARAMINDEX_PORT].name,
                                 &UA_TYPES[UA_TYPES_UINT16]);
    if(!uport) {
        UA_LOG_ERROR(el->cLoop.logger, UA_LOGCATEGORY_NETWORK,
                     "TCP\t| No port defined");
        return UA_STATUSCODE_BADINTERNALERROR;
    }
    port = *uport;

    const UA_String *addr = (const UA_String*)
        UA_KeyValueMap_getScalar(params, tcpConnectionParams[TCP_PARAMINDEX_ADDR].name,
                                 &UA_TYPES[UA_TYPES_STRING]);
    if(!addr) {
        UA_LOG_ERROR(el->cLoop.logger, UA_LOGCATEGORY_NETWORK,
                     "TCP\t| Open TCP Connection: No hostname defined, aborting");
        return UA_STATUSCODE_BADINTERNALERROR;
    }
    if(addr->length >= 512) {
        UA_LOG_ERROR(el->cLoop.logger, UA_LOGCATEGORY_EVENTLOOP,
                     "TCP\t| Open TCP Connection: Hostname too long, aborting");
        return UA_STATUSCODE_BADINTERNALERROR;
    }
    /* asyncio resolves an IPv6 literal without the URL brackets.
     * UA_parseEndpointUrl already strips them; accept both forms. */
    const UA_Byte *host = addr->data;
    size_t hostLength = addr->length;
    if(hostLength >= 2 && host[0] == '[' && host[hostLength - 1] == ']') {
        host++;
        hostLength -= 2;
    }
    if(hostLength > 0)
        memcpy(hostname, host, hostLength);
    hostname[hostLength] = 0;

    // Create a new Connection
    AsyncIOConnection *cc = (AsyncIOConnection *)
        TCPProtocolType.tp_new(&TCPProtocolType, NULL, NULL);
    if(!cc) {
        PyErr_Print();
        return UA_STATUSCODE_BADINTERNALERROR;;
    }

    // Set up the connection
    cc->connectionId = acm->nextConnectionId++;
    acm->connectionCount++;
    cc->cm = acm;
    cc->cb = connectionCallback;
    cc->application = application;
    cc->context = context;

    // Call create_connection for the eventloop
    PyObject *coro = PyObject_CallMethod(el->pyLoop, "create_connection", "Osi",
                                         cc, hostname, port);
    if(!coro) {
        PyErr_Print();
        Py_DECREF(cc);
        return UA_STATUSCODE_BADINTERNALERROR;;
    }

    // Create the task for async completion
    PyObject *task = PyObject_CallMethod(el->pyLoop, "create_task", "O", coro);
    Py_DECREF(coro);  // We no longer need the coroutine reference
    if(!task) {
        Py_DECREF(cc);
        PyErr_Print();
        return UA_STATUSCODE_BADINTERNALERROR;;
    }

    // Add a reference to the connection
    int res2 = PyObject_SetAttrString(task, "_connection", (PyObject*)cc);
    if(res2 < 0) {
        PyErr_Print();
        Py_DECREF(cc);
        Py_DECREF(task);
        return UA_STATUSCODE_BADINTERNALERROR;;
    }

    // Add the "done"-callback to handle success and failure
    PyObject *py_callback = PyCFunction_New(&callback_def, NULL);
    if(!py_callback) {
        PyErr_Print();
        Py_DECREF(cc);
        Py_DECREF(task);
        return UA_STATUSCODE_BADINTERNALERROR;;
    }

    PyObject *res = PyObject_CallMethod(task, "add_done_callback", "O", py_callback);
    Py_DECREF(py_callback);  // task keeps its own reference
    Py_DECREF(task);         // we no longer need our reference
    if(!res) {
        Py_DECREF(cc);
        PyErr_Print();
        return UA_STATUSCODE_BADINTERNALERROR;;
    }
    Py_DECREF(res);

    // Store the new connection in the list
    *c = cc;

    UA_LOG_DEBUG(cc->cm->cm.eventSource.eventLoop->logger, UA_LOGCATEGORY_NETWORK,
                "TCP %zu\t| Opening a connection to \"%s\" on port %i",
                (unsigned)cc->connectionId, hostname, port);

    // Notify the application about a new OPENING connection
    cc->notified = true;
    cc->cb(&cc->cm->cm, cc->connectionId, cc->application,
           &cc->context, UA_CONNECTIONSTATE_OPENING,
           &UA_KEYVALUEMAP_NULL, UA_BYTESTRING_NULL);

    return UA_STATUSCODE_GOOD;
}

static UA_StatusCode
AsyncIOTCP_openConnection(UA_ConnectionManager *cm, const UA_KeyValueMap *params,
                          void *application, void *context,
                          UA_ConnectionManager_connectionCallback connectionCallback) {
    init_tcpConnectionParams();

    AsyncIOConnectionManager *acm = (AsyncIOConnectionManager*)cm;
    AsyncIOLoop *el = (AsyncIOLoop*)cm->eventSource.eventLoop;
    if(!el)
        return UA_STATUSCODE_BADINTERNALERROR;;

    UA_LOCK(&el->elMutex);

    if(cm->eventSource.state != UA_EVENTSOURCESTATE_STARTED) {
        UA_LOG_ERROR(el->cLoop.logger, UA_LOGCATEGORY_NETWORK,
                     "TCP\t| Cannot open a connection for a "
                     "ConnectionManager that is not started");
        UA_UNLOCK(&el->elMutex);
        return UA_STATUSCODE_BADINTERNALERROR;
    }

    /* Check the parameters */
    UA_StatusCode res =
        UA_KeyValueRestriction_validate(el->cLoop.logger, "TCP",
                                        tcpConnectionParams,
                                        TCP_PARAMETERSSIZE, params);
    if(res != UA_STATUSCODE_GOOD) {
        UA_UNLOCK(&el->elMutex);
        return res;
    }

    /* Only validate the parameters? */
    UA_Boolean validate = false;
    const UA_Boolean *validateParam = (const UA_Boolean*)
        UA_KeyValueMap_getScalar(params,
                                 tcpConnectionParams[TCP_PARAMINDEX_VALIDATE].name,
                                 &UA_TYPES[UA_TYPES_BOOLEAN]);
    if(validateParam)
        validate = *validateParam;

    /* Listen or active connection? */
    UA_Boolean listen = false;
    const UA_Boolean *listenParam = (const UA_Boolean*)
        UA_KeyValueMap_getScalar(params,
                                 tcpConnectionParams[TCP_PARAMINDEX_LISTEN].name,
                                 &UA_TYPES[UA_TYPES_BOOLEAN]);
    if(listenParam)
        listen = *listenParam;

    if(listen) {
        res = AsyncIOTCP_openPassiveConnection(acm, params, application, context,
                                               connectionCallback, validate);
    } else {
        res = AsyncIOTCP_openActiveConnection(acm, params, application, context,
                                              connectionCallback, validate);
    }

    UA_UNLOCK(&el->elMutex);
    return res;
}

static UA_StatusCode
AsyncIOTCP_eventSourceStart(UA_ConnectionManager *cm) {
    AsyncIOLoop *el = (AsyncIOLoop*)cm->eventSource.eventLoop;
    if(!el)
        return UA_STATUSCODE_BADINTERNALERROR;

    UA_LOCK(&el->elMutex);

    /* Check the state */
    if(cm->eventSource.state != UA_EVENTSOURCESTATE_STOPPED) {
        UA_LOG_ERROR(el->cLoop.logger, UA_LOGCATEGORY_NETWORK,
                     "TCP\t| To start the ConnectionManager, it has to be "
                     "registered in an EventLoop and not started yet");
        UA_UNLOCK(&el->elMutex);
        return UA_STATUSCODE_BADINTERNALERROR;
    }

    /* Size the reusable send buffer from open62541's own default chunk size,
     * which is what every channel here ends up configured with. A channel that
     * asks for more just takes the fallback allocation below. An existing buffer
     * is kept across a stop-then-start cycle -- freeing it here could pull it
     * out from under a claim. */
    AsyncIOConnectionManager *acm = (AsyncIOConnectionManager*)cm;
    if(acm->txBuffer.data == NULL) {
        UA_StatusCode res =
            UA_ByteString_allocBuffer(&acm->txBuffer,
                                      UA_ConnectionConfig_default.sendBufferSize);
        if(res != UA_STATUSCODE_GOOD) {
            UA_LOG_ERROR(el->cLoop.logger, UA_LOGCATEGORY_NETWORK,
                         "TCP\t| Could not allocate the shared send buffer");
            UA_UNLOCK(&el->elMutex);
            return res;
        }
        UA_atomic_store(&acm->txBufferInUse, (uintptr_t)0);
    }

    /* Set the EventSource to the started state */
    cm->eventSource.state = UA_EVENTSOURCESTATE_STARTED;

    UA_UNLOCK(&el->elMutex);
    return UA_STATUSCODE_GOOD;
}

static void
AsyncIOTCP_eventSourceStop(UA_ConnectionManager *cm) {
    AsyncIOConnectionManager *acm = (AsyncIOConnectionManager*)cm;
    AsyncIOLoop *el = (AsyncIOLoop*)cm->eventSource.eventLoop;
    if(!el)
        return;

    UA_LOCK(&el->elMutex);

    UA_LOG_DEBUG(cm->eventSource.eventLoop->logger, UA_LOGCATEGORY_NETWORK,
                 "TCP\t| Shutting down the ConnectionManager");
    cm->eventSource.state = UA_EVENTSOURCESTATE_STOPPING;

    /* When tearingDown is set we are inside tp_dealloc (GC).  Calling
     * Python methods (transport.close, server.close) is unsafe: coverage
     * instrumentation triggers instrumentation_cross_checks assertions,
     * and _PyType_Lookup asserts !PyErr_Occurred() in debug builds.
     * Skip all Python calls; just drop references. */
    int unsafe = el->tearingDown;

    if(!unsafe)
        PyErr_Clear();

    /* Close all listeners */
    for(size_t i = 0; i < acm->listenersCapacity; i++) {
        if(!acm->listeners[i])
            continue;
        AsyncIOListener *listener = acm->listeners[i];
        acm->listeners[i] = NULL;
        listener->cm = NULL;
        if(!unsafe)
            cancelListenerTask(listener);
        if(!unsafe && listener->asyncioServer) {
            PyObject *result =
                PyObject_CallMethod(listener->asyncioServer, "close", NULL);
            if(!result) PyErr_Clear();
            Py_XDECREF(result);
            listener->cb(&acm->cm, listener->listenConnectionId,
                         listener->application, &listener->context,
                         UA_CONNECTIONSTATE_CLOSING,
                         &UA_KEYVALUEMAP_NULL, UA_BYTESTRING_NULL);
        }
        Py_DECREF(listener);
    }

    /* Finish native cleanup before detaching the protocols. Asyncio may
     * deliver connection_lost later, when the manager is already freed. */
    for(size_t i = 0; i < acm->connectionsCapacity; i++) {
        if(!acm->connections[i])
            continue;
        AsyncIOConnection *conn = acm->connections[i];
        if(!unsafe) {
            if(conn->transport) {
                PyObject *result =
                    PyObject_CallMethod(conn->transport, "close", NULL);
                if(!result) PyErr_Clear();
                Py_XDECREF(result);
            }
            PyObject *result = TCPProtocol_connection_lost(conn, NULL);
            if(!result) PyErr_Clear();
            Py_XDECREF(result);
            continue;
        }
        acm->connections[i] = NULL;
        /* During GC only detach; queued callbacks may outlive the manager. */
        conn->cm = NULL;
        Py_DECREF(conn);
    }

    acm->connectionCount = 0;

    /* Prevent new connections to open */
    cm->eventSource.state = UA_EVENTSOURCESTATE_STOPPED;

    UA_UNLOCK(&el->elMutex);
}

static UA_StatusCode
AsyncIOTCP_eventSourceDelete(UA_ConnectionManager *cm) {
    if(cm->eventSource.state >= UA_EVENTSOURCESTATE_STARTING) {
        UA_LOG_ERROR(cm->eventSource.eventLoop->logger, UA_LOGCATEGORY_EVENTLOOP,
                     "TCP\t| The EventSource must be stopped before it can be deleted");
        return UA_STATUSCODE_BADINTERNALERROR;
    }

    UA_KeyValueMap_clear(&cm->eventSource.params);
    UA_String_clear(&cm->eventSource.name);
    AsyncIOConnectionManager *acm = (AsyncIOConnectionManager *)cm;
    UA_free(acm->connections);
    UA_free(acm->listeners);
    /* Still claimed here means a send path never released the buffer. */
    UA_assert(UA_atomic_load(&acm->txBufferInUse) == 0);
    UA_ByteString_clear(&acm->txBuffer);
    UA_free(cm);
    return UA_STATUSCODE_GOOD;
}

static UA_StatusCode
AsyncIOTCP_allocNetworkBuffer(UA_ConnectionManager *cm,
                              uintptr_t connectionId,
                              UA_ByteString *buf,
                              size_t bufSize) {
    AsyncIOConnectionManager *acm = (AsyncIOConnectionManager*)cm;
    /* The buffer is handed out WITHOUT being zeroed -- that is the entire point,
     * and it is safe only because every send path sets buf->length from the
     * bytes it actually wrote and writes padding and AEAD tags explicitly
     * instead of assuming zeros. 
     *
     * txBuffer.length is immutable while started, so it can be read outside the
     * exchange. The data test is not redundant with it: on an unstarted manager
     * bufSize 0 satisfies 0 >= 0 and would claim a NULL-string descriptor that
     * freeNetworkBuffer cannot recognise, wedging the flag permanently. */
    if(acm->txBuffer.data != NULL && acm->txBuffer.length >= bufSize) {
        uintptr_t was = 1;
        UA_atomic_xchg(&acm->txBufferInUse, (uintptr_t)1, &was);
        if(was == 0) {
            *buf = acm->txBuffer;
            buf->length = bufSize; /* struct copy; acm->txBuffer.length unchanged */
            return UA_STATUSCODE_GOOD;
        }
    }
    return UA_ByteString_allocBuffer(buf, bufSize);
}

static void
AsyncIOTCP_freeNetworkBuffer(UA_ConnectionManager *cm,
                             uintptr_t connectionId,
                             UA_ByteString *buf) {
    AsyncIOConnectionManager *acm = (AsyncIOConnectionManager*)cm;
    if(acm->txBuffer.data != NULL && buf->data == acm->txBuffer.data) {
        /* The init is not cosmetic: open62541 gates a second release on
         * `mc->messageBuffer.length > 0`, and that second release would clear a
         * flag a later send may already hold -- two users of one buffer. */
        UA_ByteString_init(buf);
        UA_atomic_store(&acm->txBufferInUse, (uintptr_t)0);
        return;
    }
    UA_ByteString_clear(buf);
}

static const char *tcpName = "tcp";

int
AsyncIOTCP_initTypes(void) {
    if(!(TCPProtocolType.tp_flags & Py_TPFLAGS_READY)) {
        if(PyType_Ready(&TCPProtocolType) < 0)
            return -1;
    }
    if(!(ListenerType.tp_flags & Py_TPFLAGS_READY)) {
        if(PyType_Ready(&ListenerType) < 0)
            return -1;
    }
    return 0;
}

UA_ConnectionManager *
UA_ConnectionManager_new_AsyncIO_TCP() {
    /* PyType_Ready was already called during module init */
    if(AsyncIOTCP_initTypes() < 0)
        return NULL;

    // Allocate the ConnectionManager
    UA_ConnectionManager *cm = (UA_ConnectionManager*)
        UA_calloc(1, sizeof(AsyncIOConnectionManager));
    if(!cm)
        return NULL;

    /* Start nextConnectionId at 1 so that connectionId 0 is never used.
     * open62541's BPM uses connectionId == 0 as "unoccupied slot" and
     * skips it during stop. */
    ((AsyncIOConnectionManager*)cm)->nextConnectionId = 1;

    // Set up the ConnectionManager
    UA_String tcpSourceName = UA_STRING("tcp-source");
    cm->eventSource.eventSourceType = UA_EVENTSOURCETYPE_CONNECTIONMANAGER;
    UA_String_copy(&tcpSourceName, &cm->eventSource.name);
    cm->eventSource.start = (UA_StatusCode (*)(UA_EventSource *))AsyncIOTCP_eventSourceStart;
    cm->eventSource.stop = (void (*)(UA_EventSource *))AsyncIOTCP_eventSourceStop;
    cm->eventSource.free = (UA_StatusCode (*)(UA_EventSource *))AsyncIOTCP_eventSourceDelete;
    cm->protocol = UA_STRING((char*)(uintptr_t)tcpName);
    cm->allocNetworkBuffer = AsyncIOTCP_allocNetworkBuffer;
    cm->freeNetworkBuffer = AsyncIOTCP_freeNetworkBuffer;
    cm->openConnection = AsyncIOTCP_openConnection;
    cm->sendWithConnection = AsyncIOTCP_sendWithConnection;
    cm->closeConnection = AsyncIOTCP_shutdownConnection;
    return cm;
}
