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
#include "eventloop_common.h"

#include "client/client.h"

/* Configuration parameters */
#define TCP_PARAMETERSSIZE 5
#define TCP_PARAMINDEX_ADDR 0
#define TCP_PARAMINDEX_PORT 1
#define TCP_PARAMINDEX_LISTEN 2
#define TCP_PARAMINDEX_VALIDATE 3
#define TCP_PARAMINDEX_REUSE 4

static UA_KeyValueRestriction tcpConnectionParams[TCP_PARAMETERSSIZE] = {
    {{0, UA_STRING_STATIC("address")}, &UA_TYPES[UA_TYPES_STRING], false, true, true},
    {{0, UA_STRING_STATIC("port")}, &UA_TYPES[UA_TYPES_UINT16], true, true, false},
    {{0, UA_STRING_STATIC("listen")}, &UA_TYPES[UA_TYPES_BOOLEAN], false, true, false},
    {{0, UA_STRING_STATIC("validate")}, &UA_TYPES[UA_TYPES_BOOLEAN], false, true, false},
    {{0, UA_STRING_STATIC("reuse")}, &UA_TYPES[UA_TYPES_BOOLEAN], false, true, false}
};

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
    if(!self->cm)
        Py_RETURN_NONE;

    AsyncIOLoop *el = (AsyncIOLoop*)self->cm->cm.eventSource.eventLoop;
    UA_LOG_DEBUG(el->cLoop.logger, UA_LOGCATEGORY_EVENTLOOP, "connection made");

    // Already have a transport
    if(self->transport)
        return NULL;

    // Set the new transport
    PyObject *transport;
    if(!PyArg_ParseTuple(args, "O", &transport))
        return NULL;
    Py_INCREF(transport);
    self->transport = transport;

    UA_LOG_DEBUG(self->cm->cm.eventSource.eventLoop->logger, UA_LOGCATEGORY_NETWORK,
                 "TCP %zu\t| Opened a connection", (unsigned)self->connectionId);

    // Notify the application the connection has opened
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

    // Get the data
    const char *data;
    Py_ssize_t len;
    if(!PyArg_ParseTuple(args, "y#", &data, &len))
        return NULL;
    UA_ByteString msg = {len, (UA_Byte*)data};

    // Forward to the application
    self->cb(&self->cm->cm, self->connectionId, self->application,
             &self->context, UA_CONNECTIONSTATE_ESTABLISHED,
             &UA_KEYVALUEMAP_NULL, msg);
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
    for(size_t i = 0; i < ASYNCIO_MAX_SOCKETS; i++) {
        if(cm->connections[i] == self) {
            cm->connections[i] = NULL;
            cm->connectionCount--;
            break;
        }
    }

    // From Shutdown to closing?
    if(cm->cm.eventSource.state == UA_EVENTSOURCESTATE_STOPPING &&
       cm->connectionCount == 0) {
        cm->cm.eventSource.state = UA_EVENTSOURCESTATE_STOPPED;
    }

    // Signal closing to the application
    self->cb(&self->cm->cm, self->connectionId, self->application,
             &self->context, UA_CONNECTIONSTATE_CLOSING,
             &UA_KEYVALUEMAP_NULL, UA_BYTESTRING_NULL);

    Py_DECREF(self); // After having removed ourselves from the list

    /* Deferred cleanup: the Python Client was GC'd while still connected.
     * __del__ left the loop running so the async disconnect could
     * complete; tp_dealloc called UA_Client_disconnectAsync() and
     * deferred the real cleanup to here.  Now that all connections are
     * gone we can safely delete the UA_Client, free the event loop,
     * stop the asyncio loop (so the worker thread exits run_forever()),
     * and free the PyClient struct. */
    

    if (el->pyClient) {
        PyClient *pyClient = (PyClient*)el->pyClient;
        if(pyClient && pyClient->deleteme && cm->connectionCount == 0) {

            /* Null out self->cm BEFORE full cleanup.  full_cleanup frees
             * the C event loop which frees the ConnectionManager struct
             * that self->cm points to.  Without this, TCPProtocol_dealloc
             * (which runs when asyncio drops its protocol reference) would
             * dereference the freed CM → use-after-free / segfault. */
            self->cm = NULL;

            /* Grab a reference to the Python asyncio loop BEFORE
             * pyClient_full_cleanup frees the C event loop struct. */
            PyObject *pyLoop = el->pyLoop;
            Py_XINCREF(pyLoop);

            pyClient_full_cleanup(pyClient);

            /* Stop the asyncio loop so the worker thread exits
             * run_forever().  This call is safe here (we are on the
             * event-loop thread inside a callback, not in GC). */
            if(pyLoop) {
                PyObject *r = PyObject_CallMethod(pyLoop, "stop", NULL);
                if(!r) PyErr_Clear();
                Py_XDECREF(r);
                Py_DECREF(pyLoop);
            }
        }
    }


    Py_RETURN_NONE;
}

static void
TCPProtocol_dealloc(AsyncIOConnection *self) {
    /* self->cm may be NULL if the CM was already torn down; skip debug log. */
    if(self->cm) {
        AsyncIOLoop *el = (AsyncIOLoop*)self->cm->cm.eventSource.eventLoop;
        UA_LOG_DEBUG(el->cLoop.logger, UA_LOGCATEGORY_EVENTLOOP, "dealloc");
    }
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
};

static PyObject *
AsyncIOListener_call(AsyncIOListener *self, PyObject *args, PyObject *kwargs) {
    if(!self->cm)
        Py_RETURN_NONE;

    AsyncIOConnectionManager *acm = self->cm;
    AsyncIOLoop *el = (AsyncIOLoop*)acm->cm.eventSource.eventLoop;

    /* Find a slot for the new connection */
    AsyncIOConnection **slot = NULL;
    for(size_t i = 0; i < ASYNCIO_MAX_SOCKETS; i++) {
        if(!acm->connections[i]) {
            slot = &acm->connections[i];
            break;
        }
    }
    if(!slot) {
        UA_LOG_ERROR(el->cLoop.logger, UA_LOGCATEGORY_NETWORK,
                     "TCP\t| Max number of connections reached");
        PyErr_SetString(PyExc_RuntimeError, "Max connections reached");
        return NULL;
    }

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
    Py_XDECREF(self->asyncioServer);
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

static PyObject *
TCP_listen_done_callback(PyObject *self, PyObject *args) {
    PyObject *task;
    if(!PyArg_ParseTuple(args, "O", &task))
        return NULL;

    AsyncIOListener *listener = (AsyncIOListener *)
        PyObject_GetAttrString(task, "_listener");
    if(!listener)
        return NULL;

    /* The ConnectionManager may have been torn down */
    if(!listener->cm) {
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
    listener->cb(&listener->cm->cm, listener->listenConnectionId,
                 listener->application, &listener->context,
                 UA_CONNECTIONSTATE_ESTABLISHED,
                 &UA_KEYVALUEMAP_NULL, UA_BYTESTRING_NULL);

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
    for(size_t i = 0; i < ASYNCIO_MAX_SOCKETS; i++) {
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

    /* Parse optional address */
    char hostname[512] = "0.0.0.0";
    const UA_String *addr = (const UA_String*)
        UA_KeyValueMap_getScalar(params, tcpConnectionParams[TCP_PARAMINDEX_ADDR].name,
                                 &UA_TYPES[UA_TYPES_STRING]);
    if(addr && addr->length > 0 && addr->length < 512) {
        strncpy(hostname, (const char*)addr->data, addr->length);
        hostname[addr->length] = 0;
    }

    /* Check reuse flag */
    UA_Boolean reuse = true;
    const UA_Boolean *reuseParam = (const UA_Boolean*)
        UA_KeyValueMap_getScalar(params, tcpConnectionParams[TCP_PARAMINDEX_REUSE].name,
                                 &UA_TYPES[UA_TYPES_BOOLEAN]);
    if(reuseParam)
        reuse = *reuseParam;

    /* Find a slot for the listener */
    AsyncIOListener **slot = NULL;
    for(size_t i = 0; i < ASYNCIO_MAX_SOCKETS; i++) {
        if(!acm->listeners[i]) {
            slot = &acm->listeners[i];
            break;
        }
    }
    if(!slot) {
        UA_LOG_ERROR(el->cLoop.logger, UA_LOGCATEGORY_NETWORK,
                     "TCP\t| Max number of listeners reached");
        return UA_STATUSCODE_BADINTERNALERROR;
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

    /* Call loop.create_server(listener, host, port, reuse_address=reuse) */
    PyObject *py_reuse = reuse ? Py_True : Py_False;

    PyObject *method = PyObject_GetAttrString(el->pyLoop, "create_server");
    if(!method) {
        PyErr_Print();
        Py_DECREF(listener);
        return UA_STATUSCODE_BADINTERNALERROR;
    }
    PyObject *posargs = Py_BuildValue("(Osi)", listener, hostname, port);
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
    Py_DECREF(task);
    if(!res) {
        PyErr_Print();
        Py_DECREF(listener);
        return UA_STATUSCODE_BADINTERNALERROR;
    }
    Py_DECREF(res);

    /* Store the listener */
    *slot = listener;

    UA_LOG_DEBUG(el->cLoop.logger, UA_LOGCATEGORY_NETWORK,
                 "TCP %zu\t| Opening a listen socket on \"%s\" port %i",
                 (unsigned)listener->listenConnectionId, hostname, port);

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
    for(size_t i = 0; i < ASYNCIO_MAX_SOCKETS; i++) {
        if(acm->connections[i] && acm->connections[i]->connectionId == connectionId) {
            c = acm->connections[i];
            break;
        }
    }

    if(!c)
        return UA_STATUSCODE_BADINTERNALERROR;

    if(!c->transport)
        return UA_STATUSCODE_BADINTERNALERROR;

    // Create a Python bytes object
    PyObject *py_bytes = PyBytes_FromStringAndSize((const char *)buf->data, buf->length);
    if(!py_bytes) {
        PyErr_Print();
        return UA_STATUSCODE_BADINTERNALERROR;
    }

    // Call transport.write(data)
    PyObject *result = PyObject_CallMethod(c->transport, "write", "O", py_bytes);
    Py_DECREF(py_bytes);

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
    for(size_t i = 0; i < ASYNCIO_MAX_SOCKETS; i++) {
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
            Py_DECREF(listener);
            return UA_STATUSCODE_GOOD;
        }
    }

    /* Find the connection and close its transport so that asyncio stops
     * delivering data and eventually calls connection_lost. */
    for(size_t i = 0; i < ASYNCIO_MAX_SOCKETS; i++) {
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
    for(size_t i = 0; i < ASYNCIO_MAX_SOCKETS; i++) {
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

    // TODO: Do more checks
    if(validate)
        return UA_STATUSCODE_GOOD;

    // Find a slot for the connection;
    AsyncIOConnection **c = NULL;
    for(size_t i = 0; i < ASYNCIO_MAX_SOCKETS; i++) {
        if(!acm->connections[i]) {
            c = &acm->connections[i];
            break;
        }
    }
    if(!c) {
        UA_LOG_ERROR(el->cLoop.logger, UA_LOGCATEGORY_NETWORK,
                     "TCP\t| Max number of connections reached");
        return UA_STATUSCODE_BADINTERNALERROR;
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
    strncpy(hostname, (const char*)addr->data, addr->length);
    hostname[addr->length] = 0;

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
    cc->cb(&cc->cm->cm, cc->connectionId, cc->application,
           &cc->context, UA_CONNECTIONSTATE_OPENING,
           &UA_KEYVALUEMAP_NULL, UA_BYTESTRING_NULL);

    return UA_STATUSCODE_GOOD;
}

static UA_StatusCode
AsyncIOTCP_openConnection(UA_ConnectionManager *cm, const UA_KeyValueMap *params,
                          void *application, void *context,
                          UA_ConnectionManager_connectionCallback connectionCallback) {
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

    /* When tearingDown is set we are inside tp_dealloc (GC).  Calling
     * Python methods (transport.close, server.close) is unsafe: coverage
     * instrumentation triggers instrumentation_cross_checks assertions,
     * and _PyType_Lookup asserts !PyErr_Occurred() in debug builds.
     * Skip all Python calls; just drop references. */
    int unsafe = el->tearingDown;

    if(!unsafe)
        PyErr_Clear();

    /* Close all listeners */
    for(size_t i = 0; i < ASYNCIO_MAX_SOCKETS; i++) {
        if(!acm->listeners[i])
            continue;
        AsyncIOListener *listener = acm->listeners[i];
        acm->listeners[i] = NULL;
        listener->cm = NULL;
        if(!unsafe && listener->asyncioServer) {
            PyObject *result =
                PyObject_CallMethod(listener->asyncioServer, "close", NULL);
            if(!result) PyErr_Clear();
            Py_XDECREF(result);
        }
        Py_DECREF(listener);
    }

    /* Shutdown all open connections. They remove themselves in the
     * connection_lost callback. */
    for(size_t i = 0; i < ASYNCIO_MAX_SOCKETS; i++) {
        if(!acm->connections[i])
            continue;
        AsyncIOConnection *conn = acm->connections[i];
        acm->connections[i] = NULL;
        /* Null out cm BEFORE closing the transport.  asyncio queues
         * _call_connection_lost asynchronously; by the time it fires the CM
         * struct will have been freed.  The NULL sentinel tells
         * TCPProtocol_connection_lost to skip the already-cleaned-up work. */
        conn->cm = NULL;
        if(!unsafe && conn->transport) {
            PyErr_Clear();
            PyObject *result = PyObject_CallMethod(conn->transport, "close", NULL);
            if(!result) PyErr_Clear();
            Py_XDECREF(result);
        }
        Py_DECREF(conn);
    }

    /* Prevent new connections to open */
    cm->eventSource.state = (acm->connectionCount == 0) ?
        UA_EVENTSOURCESTATE_STOPPED : UA_EVENTSOURCESTATE_STOPPING;

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
    UA_free(cm);
    return UA_STATUSCODE_GOOD;
}

static UA_StatusCode
AsyncIOTCP_allocNetworkBuffer(UA_ConnectionManager *cm,
                              uintptr_t connectionId,
                              UA_ByteString *buf,
                              size_t bufSize) {
    return UA_ByteString_allocBuffer(buf, bufSize);
}

static void
AsyncIOTCP_freeNetworkBuffer(UA_ConnectionManager *cm,
                             uintptr_t connectionId,
                             UA_ByteString *buf) {
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
