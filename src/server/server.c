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
#include "../utils.h"
#include "module.h"

/**********************/
/* Server Lifecycle   */
/**********************/

static int
pyServer_init(PyServer *self, PyObject *args, PyObject *kwds) {
    static char *kwlist[] = {"port", "logger", "loop", NULL};
    int port = 4840;
    PyObject *pyLog = NULL;
    PyObject *pyLoop = NULL;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "|iOO", kwlist,
                                     &port, &pyLog, &pyLoop))
        return -1;

    if (port < 0 || port > 65535) {
        PyErr_SetString(PyExc_ValueError, "port must be between 0 and 65535");
        return -1;
    }

    if (pyLoop && pyLoop != Py_None) {
        /* Asyncio path: build a config with our AsyncIOLoop, then create
         * the server from that config.  UA_ServerConfig_setMinimal skips
         * event-loop creation when config->eventLoop is already set. */
        UA_ServerConfig config;
        memset(&config, 0, sizeof(UA_ServerConfig));

        if (pyLog && pyLog != Py_None) {
            config.logging = pyLogger(pyLog);
            if (!config.logging) {
                PyErr_SetString(PyExc_RuntimeError, "Could not create the logger");
                return -1;
            }
        }

        config.eventLoop = UA_EventLoop_new_AsyncIO(
            pyLoop, pyLog ? pyLog : Py_None);
        if (!config.eventLoop) {
            PyErr_SetString(PyExc_RuntimeError,
                            "Could not create the asyncio event loop");
            return -1;
        }

        // Store back-pointer on the event loop for deferred cleanup
        AsyncIOLoop *el = (AsyncIOLoop*)config.eventLoop;
        el->pyServer = self;

        UA_StatusCode sc = UA_ServerConfig_setMinimal(
            &config, (UA_UInt16)port, NULL);
        if (sc != UA_STATUSCODE_GOOD) {
            config.eventLoop->free(config.eventLoop);
            PyErr_SetString(PyExc_RuntimeError,
                            "UA_ServerConfig_setMinimal failed");
            return -1;
        }

        self->server = UA_Server_newWithConfig(&config);
        if (!self->server) {
            PyErr_NoMemory();
            return -1;
        }

        /* Mark as externally managed so that run_shutdown / server_clear
         * do not try to iterate the AsyncIO loop (which returns
         * BADNOTIMPLEMENTED from run()).  We manage the loop lifecycle
         * ourselves in pyServer_clear. */
        UA_Server_getConfig(self->server)->externalEventLoop = true;
    } else {
        /* Legacy path: default POSIX event loop (no asyncio) */
        self->server = UA_Server_new();
        if (!self->server) {
            PyErr_NoMemory();
            return -1;
        }

        UA_ServerConfig *config = UA_Server_getConfig(self->server);
        UA_ServerConfig_setMinimal(config, (UA_UInt16)port, NULL);

        if (pyLog && pyLog != Py_None) {
            UA_Logger *logging = pyLogger(pyLog);
            if (!logging) {
                PyErr_SetString(PyExc_RuntimeError,
                                "Could not create the logger");
                UA_Server_delete(self->server);
                self->server = NULL;
                return -1;
            }
            config->logging = logging;
        }
    }

    self->running = false;
    self->hasAsyncLoop = (pyLoop && pyLoop != Py_None) ? true : false;
    self->hasHistoryDB = false;
    memset(&self->gathering, 0, sizeof(UA_HistoryDataGathering));

    /* Store a back-pointer so callbacks can detect teardown via NULL check */
    UA_Server_getConfig(self->server)->context = self;

    self->linked_type_capsules = PyList_New(0);
    if(!self->linked_type_capsules) {
        UA_Server_delete(self->server);
        self->server = NULL;
        return -1;
    }
    return 0;
}

/* Core cleanup: delete the UA_Server, free the event loop.
 * Does NOT call tp_free — the caller is responsible for that.
 * Safe to call from __del__ (tp_finalize) where Python API calls
 * (Py_DECREF on asyncio handles) are safe, and from tp_dealloc. */
static void
pyServer_do_cleanup(PyServer *self) {
    if (!self->server)
        return;

    UA_ServerConfig *config = UA_Server_getConfig(self->server);

    if(config)
        config->context = NULL;

    if(config && config->logging)
        config->logging->context = NULL;
    if(self->hasAsyncLoop && config && config->eventLoop &&
       config->eventLoop->logger)
        ((UA_Logger*)config->eventLoop->logger)->context = NULL;

    if (self->running) {
        self->running = false;
        UA_Server_run_shutdown(self->server);
    }

    if (self->hasAsyncLoop) {
        UA_EventLoop *el = config ? config->eventLoop : NULL;

        /* Mark tearingDown so that AsyncIOTCP_eventSourceStop skips
         * PyObject_CallMethod(transport/server, "close").  After
         * Server.stop() the connections are already closed; calling
         * Python methods during GC with coverage instrumentation
         * active can trigger segfaults. */
        if(el)
            ((AsyncIOLoop*)el)->tearingDown = 1;

        if (el && el->state != UA_EVENTLOOPSTATE_FRESH &&
            el->state != UA_EVENTLOOPSTATE_STOPPED) {
            PyErr_Clear();
            el->stop(el);
        }

        UA_Server_delete(self->server);
        self->server = NULL;

        if (el) {
            if (el->state != UA_EVENTLOOPSTATE_FRESH &&
                el->state != UA_EVENTLOOPSTATE_STOPPED) {
                PyErr_Clear();
                el->stop(el);
            }
            el->free(el);
        }
    } else {
        UA_Server_delete(self->server);
        self->server = NULL;
    }

    if(PyErr_Occurred())
        PyErr_Clear();
}

static void
pyServer_clear(PyServer *self) {
    /* If _cleanup() was not called from __del__, we are in tp_dealloc
     * (possibly during GC sweep).  Mark tearingDown so that
     * AsyncIOTCP_eventSourceStop skips PyObject_CallMethod calls. */
    if(self->server && self->hasAsyncLoop) {
        UA_ServerConfig *config = UA_Server_getConfig(self->server);
        if(config && config->eventLoop)
            ((AsyncIOLoop*)config->eventLoop)->tearingDown = 1;
    }
    pyServer_do_cleanup(self);
    Py_CLEAR(self->linked_type_capsules);
    Py_TYPE(self)->tp_free((PyObject *)self);
}

/* Python-callable cleanup method exposed as _cleanup().
 * Called from Python __del__ to eagerly release C resources while
 * Python API calls are still safe.  After this, self->server is NULL
 * so tp_dealloc just calls tp_free. */
static PyObject *
pyServer_cleanup(PyServer *self, PyObject *Py_UNUSED(ignored)) {
    pyServer_do_cleanup(self);
    Py_RETURN_NONE;
}

static PyObject *
pyServer_str(PyServer *self) {
    return PyUnicode_FromFormat("o6._o6.Server(%p)", self);
}

static PyObject *
pyServer_repr(PyServer *self) {
    return PyUnicode_FromFormat("o6._o6.Server(%p)", self);
}

/**********************/
/* Startup / Shutdown */
/**********************/

static PyObject *
pyServer_run_startup(PyServer *self, PyObject *args) {
    if (!self->server) {
        PyErr_SetString(PyExc_RuntimeError, "Server not initialized");
        return NULL;
    }

    /* Set the build info */
    UA_Variant val;
    UA_Variant_setScalar(&val, &buildInfo, &UA_TYPES[UA_TYPES_BUILDINFO]);
    UA_Server_writeValue(self->server, UA_NS0ID(SERVERSTATUSTYPE_BUILDINFO), val);

    UA_StatusCode status = UA_Server_run_startup(self->server);
    if (status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);
    self->running = true;
    Py_RETURN_NONE;
}

static PyObject *
pyServer_run_shutdown_py(PyServer *self, PyObject *args) {
    if (!self->server) {
        PyErr_SetString(PyExc_RuntimeError, "Server not initialized");
        return NULL;
    }
    self->running = false;
    UA_StatusCode status = UA_Server_run_shutdown(self->server);
    if (status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);
    Py_RETURN_NONE;
}

static PyObject *
pyServer_run_iterate_py(PyServer *self, PyObject *args) {
    if (!self->server) {
        PyErr_SetString(PyExc_RuntimeError, "Server not initialized");
        return NULL;
    }

    UA_Boolean waitInternal = true;
    if (PyTuple_Size(args) >= 1) {
        PyObject *wait_obj = PyTuple_GetItem(args, 0);
        if (PyBool_Check(wait_obj)) {
            waitInternal = PyObject_IsTrue(wait_obj);
        } else if (PyLong_Check(wait_obj)) {
            waitInternal = (UA_Boolean)PyLong_AsLong(wait_obj);
        } else {
            PyErr_SetString(PyExc_TypeError, "wait_internal must be a boolean");
            return NULL;
        }
    }

    UA_UInt16 timeout;
    Py_BEGIN_ALLOW_THREADS
    timeout = UA_Server_run_iterate(self->server, waitInternal);
    Py_END_ALLOW_THREADS
    return PyLong_FromUnsignedLong(timeout);
}

static PyObject *
pyServer_get_running(PyServer *self, void *closure) {
    return PyBool_FromLong(self->running);
}

static PyObject *
pyServer_get_fully_stopped(PyServer *self, void *closure) {
    if (!self->server)
        Py_RETURN_TRUE;
    return PyBool_FromLong(
        UA_Server_getLifecycleState(self->server) == UA_LIFECYCLESTATE_STOPPED);
}

/**********************/
/* Reverse Connect    */
/**********************/

typedef struct {
    PyObject *callback;  /* Python callable or NULL */
} ReverseConnectContext;

static void
reverseConnectStateCallback(UA_Server *server, UA_UInt64 handle,
                            UA_SecureChannelState state, void *ctx) {
    ReverseConnectContext *rc = (ReverseConnectContext*)ctx;
    if (!rc || !rc->callback)
        return;
    /* During teardown config->context is NULL — skip Python calls */
    UA_ServerConfig *config = UA_Server_getConfig(server);
    if (!config->context)
        return;

    assertGIL();
    PyObject *pyHandle = PyLong_FromUnsignedLongLong(handle);
    PyObject *pyState = PyLong_FromLong((long)state);
    if (pyHandle && pyState) {
        PyObject *result = PyObject_CallFunction(rc->callback, "OO",
                                                 pyHandle, pyState);
        Py_XDECREF(result);
        if (PyErr_Occurred())
            PyErr_Clear();
    }
    Py_XDECREF(pyHandle);
    Py_XDECREF(pyState);
}

static PyObject *
pyServer_add_reverse_connect(PyServer *self, PyObject *args) {
    const char *url;
    PyObject *pyCallback = Py_None;

    if (!PyArg_ParseTuple(args, "s|O", &url, &pyCallback))
        return NULL;

    if (!self->server) {
        PyErr_SetString(PyExc_RuntimeError, "Server not initialized");
        return NULL;
    }

    ReverseConnectContext *ctx = NULL;
    UA_Server_ReverseConnectStateCallback cb = NULL;

    if (pyCallback != Py_None) {
        if (!PyCallable_Check(pyCallback)) {
            PyErr_SetString(PyExc_TypeError,
                            "callback must be callable or None");
            return NULL;
        }
        ctx = (ReverseConnectContext*)calloc(1, sizeof(ReverseConnectContext));
        if (!ctx)
            return PyErr_NoMemory();
        Py_INCREF(pyCallback);
        ctx->callback = pyCallback;
        cb = reverseConnectStateCallback;
    }

    UA_UInt64 handle = 0;
    UA_StatusCode status = UA_Server_addReverseConnect(
        self->server, UA_STRING((char*)url), cb, ctx, &handle);

    if (status != UA_STATUSCODE_GOOD) {
        if (ctx) {
            Py_DECREF(ctx->callback);
            free(ctx);
        }
        return PyErr_StatusCode(status);
    }

    return PyLong_FromUnsignedLongLong(handle);
}

static PyObject *
pyServer_remove_reverse_connect(PyServer *self, PyObject *args) {
    unsigned long long handle;
    if (!PyArg_ParseTuple(args, "K", &handle))
        return NULL;

    if (!self->server) {
        PyErr_SetString(PyExc_RuntimeError, "Server not initialized");
        return NULL;
    }

    UA_StatusCode status = UA_Server_removeReverseConnect(
        self->server, (UA_UInt64)handle);
    if (status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);

    Py_RETURN_NONE;
}

/************************/
/* Namespace management */
/************************/

static PyObject *
pyServer_add_namespace(PyServer *self, PyObject *args) {
    const char *uri;
    if(!PyArg_ParseTuple(args, "s", &uri))
        return NULL;
    if(!self->server) {
        PyErr_SetString(PyExc_RuntimeError, "Server not initialized");
        return NULL;
    }
    UA_UInt16 idx = UA_Server_addNamespace(self->server, uri);
    return PyLong_FromLong((long)idx);
}

static PyObject *
pyServer_get_namespace_index(PyServer *self, PyObject *args) {
    const char *uri;
    if(!PyArg_ParseTuple(args, "s", &uri))
        return NULL;
    if(!self->server) {
        PyErr_SetString(PyExc_RuntimeError, "Server not initialized");
        return NULL;
    }
    size_t idx;
    UA_String nsUri = UA_STRING((char*)(uintptr_t)uri);
    UA_StatusCode res = UA_Server_getNamespaceByName(self->server, nsUri, &idx);
    if(res != UA_STATUSCODE_GOOD) {
        PyErr_SetString(PyExc_KeyError, uri);
        return NULL;
    }
    return PyLong_FromSize_t(idx);
}

/**********************/
/* Config Property    */
/**********************/

static PyObject *
pyServer_getConfig(PyServer *self, void *closure) {
    if (!self->server) {
        PyErr_SetString(PyExc_RuntimeError, "Server not initialized");
        return NULL;
    }
    return PyServerConfig_New(self);
}

/************************************/
/* Explicit C event loop teardown   */
/************************************/

static PyObject *
pyServer_stop_event_loop(PyServer *self, PyObject *Py_UNUSED(ignored)) {
    if (!self->server || !self->hasAsyncLoop)
        Py_RETURN_NONE;
    UA_ServerConfig *config = UA_Server_getConfig(self->server);
    UA_EventLoop *el = config ? config->eventLoop : NULL;
    if (el && el->state != UA_EVENTLOOPSTATE_FRESH &&
        el->state != UA_EVENTLOOPSTATE_STOPPED) {
        PyErr_Clear();
        el->stop(el);
    }
    Py_RETURN_NONE;
}

/**********************/
/* Type Definition    */
/**********************/

static PyGetSetDef pyServer_getsetters[] = {
    {"config", (getter)pyServer_getConfig, NULL, "Server configuration object", NULL},
    {"running", (getter)pyServer_get_running, NULL, "Whether the server is running", NULL},
    {"_is_fully_stopped", (getter)pyServer_get_fully_stopped, NULL,
     "Whether the server has reached the STOPPED lifecycle state", NULL},
    {NULL}
};

static PyMethodDef pyServer_methods[] = {
    {"run_startup", (PyCFunction)pyServer_run_startup, METH_VARARGS,
     "Start the server networking layer"},
    {"run_shutdown", (PyCFunction)pyServer_run_shutdown_py, METH_VARARGS,
     "Shut down the server networking layer"},
    {"run_iterate", (PyCFunction)pyServer_run_iterate_py, METH_VARARGS,
     "Process server events (wait_internal=True)"},
    {"add_variable_node", (PyCFunction)pyServer_add_variable_node, METH_VARARGS,
     "Add a variable node to the server address space"},
    {"add_object_node", (PyCFunction)pyServer_add_object_node, METH_VARARGS,
     "Add an object node to the server address space"},
    {"add_object_type_node", (PyCFunction)pyServer_add_object_type_node, METH_VARARGS,
     "Add an object type node to the server address space"},
    {"add_variable_type_node", (PyCFunction)pyServer_add_variable_type_node, METH_VARARGS,
     "Add a variable type node to the server address space"},
    {"add_data_type_node", (PyCFunction)pyServer_add_data_type_node, METH_VARARGS,
     "Add a data type node to the server address space"},
    {"add_method_node", (PyCFunction)pyServer_add_method_node, METH_VARARGS,
     "Add a method node to the server address space"},
    {"add_reference", (PyCFunction)pyServer_add_reference, METH_VARARGS,
     "Add a reference between two nodes"},
    {"delete_node", (PyCFunction)pyServer_delete_node, METH_VARARGS,
     "Delete a node from the address space"},
    {"read_value", (PyCFunction)pyServer_read_value, METH_VARARGS,
     "Read the value attribute of a variable node"},
    {"write_value", (PyCFunction)pyServer_write_value, METH_VARARGS,
     "Write the value attribute of a variable node"},
    {"add_reverse_connect", (PyCFunction)pyServer_add_reverse_connect, METH_VARARGS,
     "Register a reverse connect to a client URL"},
    {"remove_reverse_connect", (PyCFunction)pyServer_remove_reverse_connect, METH_VARARGS,
     "Remove a reverse connect by handle"},
    {"register_historizing", (PyCFunction)pyServer_register_historizing,
     METH_VARARGS | METH_KEYWORDS, "Register a node for historical data gathering."},
    {"_stop_event_loop", (PyCFunction)pyServer_stop_event_loop, METH_NOARGS,
     "Stop the C event loop (closes listeners and connections safely)"},
    {"_cleanup", (PyCFunction)pyServer_cleanup, METH_NOARGS, NULL},
    {"link_custom_data_types", (PyCFunction)linkServerCustomDataTypes,
     METH_VARARGS, "Link a pre-built type capsule (from o6._o6.build_custom_data_types) into this server"},
    {"add_namespace", (PyCFunction)pyServer_add_namespace, METH_VARARGS,
     "Register a namespace URI and return its index"},
    {"get_namespace_index", (PyCFunction)pyServer_get_namespace_index, METH_VARARGS,
     "Get the namespace index for a URI (raises KeyError if not found)"},
    {NULL, NULL, 0, NULL}
};

static PyTypeObject ServerType = {
    .ob_base = PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "o6.Server",
    .tp_doc = PyDoc_STR("OPC UA Server"),
    .tp_basicsize = sizeof(PyServer),
    .tp_itemsize = 0,
    .tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,
    .tp_new = PyType_GenericNew,
    .tp_methods = pyServer_methods,
    .tp_getset = pyServer_getsetters,
    .tp_init = (initproc)pyServer_init,
    .tp_dealloc = (destructor)pyServer_clear,
    .tp_str = (reprfunc)pyServer_str,
    .tp_repr = (reprfunc)pyServer_repr
};

PyObject *pyServerModule(void) {
    if (PyType_Ready(&ServerType) < 0)
        return NULL;
    return (PyObject *)&ServerType;
}
