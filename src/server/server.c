/* Copyright 2026 (c) o6 Automation GmbH (Author: Andreas Ebner) */
#include "server.h"
#include "../utils.h"
#include "module.h"
#include "../types_internal.h"

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

    if (!pyLoop || pyLoop == Py_None) {
        PyErr_SetString(PyExc_TypeError,
                        "o6._o6.Server() requires a 'loop' argument (asyncio.AbstractEventLoop). "
                        "Use o6.Server() for automatic loop handling.");
        return -1;
    }
    if (!pyLog || pyLog == Py_None) {
        PyErr_SetString(PyExc_TypeError,
                        "o6._o6.Server() requires a 'logger' argument. "
                        "Use o6.Server() for automatic logger handling.");
        return -1;
    }

    /* Asyncio path: build a config with our AsyncIOLoop, then create
     * the server from that config.  UA_ServerConfig_setMinimal skips
     * event-loop creation when config->eventLoop is already set. */
    UA_ServerConfig config;
    memset(&config, 0, sizeof(UA_ServerConfig));

    config.logging = pyLogger(pyLog);
    if (!config.logging) {
        PyErr_SetString(PyExc_RuntimeError, "Could not create the logger");
        return -1;
    }

    config.eventLoop = UA_EventLoop_new_AsyncIO(pyLoop, pyLog);
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

    self->running = false;
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
    if(config && config->eventLoop && config->eventLoop->logger)
        ((UA_Logger*)config->eventLoop->logger)->context = NULL;

    if (self->running) {
        self->running = false;
        UA_Server_run_shutdown(self->server);
    }

    /* Drop all Python callbacks registered for this server before the
     * UA_Server pointer is freed and potentially reused. */
    clear_server_callbacks(self->server);

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

    UA_Server *server_ptr = self->server;
    UA_Server_delete(self->server);
    self->server = NULL;

    /* Drop any (owner -> per-owner UA_DataType) registry entries that
     * referenced this server. */
    unregisterOwnerTypes(server_ptr);

    if (el) {
        if (el->state != UA_EVENTLOOPSTATE_FRESH &&
            el->state != UA_EVENTLOOPSTATE_STOPPED) {
            PyErr_Clear();
            el->stop(el);
        }
        el->free(el);
    }

    if(PyErr_Occurred())
        PyErr_Clear();
}

static void
pyServer_clear(PyServer *self) {
    /* If _cleanup() was not called from __del__, we are in tp_dealloc
     * (possibly during GC sweep).  Mark tearingDown so that
     * AsyncIOTCP_eventSourceStop skips PyObject_CallMethod calls. */
    if(self->server) {
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
    WITH_OWNER(server);
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
    WITH_OWNER_END();
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

static PyObject *
pyServer_get_namespace_uri(PyServer *self, PyObject *args) {
    unsigned short index;
    if(!PyArg_ParseTuple(args, "H", &index))
        return NULL;
    if(!self->server) {
        PyErr_SetString(PyExc_RuntimeError, "Server not initialized");
        return NULL;
    }

    UA_String nsUri;
    UA_String_init(&nsUri);
    UA_StatusCode status = UA_Server_getNamespaceByIndex(
        self->server, (size_t)index, &nsUri);
    if(status != UA_STATUSCODE_GOOD) {
        UA_String_clear(&nsUri);
        return PyErr_StatusCode(status);
    }

    PyObject *result = UA2PY(&nsUri, &UA_TYPES[UA_TYPES_STRING]);
    UA_String_clear(&nsUri);
    return result;
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
    if (!self->server)
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
    {"call", (PyCFunction)pyServer_call, METH_VARARGS,
     "Call a method node server-side with admin privileges.\n"
     "call(object_id, method_id, input_args) -> (StatusCode, ...)"},
    {"read_object_property", (PyCFunction)pyServer_read_object_property, METH_VARARGS,
     "Read an object property by BrowseName"},
    {"write_object_property", (PyCFunction)pyServer_write_object_property, METH_VARARGS,
     "Write an object property by BrowseName"},
    {"add_reverse_connect", (PyCFunction)pyServer_add_reverse_connect, METH_VARARGS,
     "Register a reverse connect to a client URL"},
    {"remove_reverse_connect", (PyCFunction)pyServer_remove_reverse_connect, METH_VARARGS,
     "Remove a reverse connect by handle"},
    {"register_historizing", (PyCFunction)pyServer_register_historizing,
     METH_VARARGS | METH_KEYWORDS, "Register a node for historical data gathering."},
    {"browse_node", (PyCFunction)pyServer_browse_node, METH_VARARGS,
     "Browse child nodes: browse_node(nodeid, result_mask) -> list[ReferenceDescription]"},
    {"read_attribute", (PyCFunction)pyServer_read_attribute, METH_VARARGS,
     "Read a node attribute: read_attribute(nodeid, attr_id) -> value"},
    {"write_attribute", (PyCFunction)pyServer_write_attribute, METH_VARARGS,
     "Write a node attribute: write_attribute(nodeid, attr_id, value) -> None"},
    {"write_data_value", (PyCFunction)pyServer_write_data_value, METH_VARARGS,
     "Write a DataValue (value + status + timestamps): write_data_value(nodeid, datavalue) -> None"},
    {"translate_browse_paths", (PyCFunction)pyServer_translate_browse_paths,
     METH_VARARGS,
     "Server-side translate browse paths to node ids"},
    {"read_node_info", (PyCFunction)pyServer_read_node_info, METH_VARARGS,
     "Read node class and browse name: read_node_info(nodeid) -> (nc_int, browse_name)"},
    {"_stop_event_loop", (PyCFunction)pyServer_stop_event_loop, METH_NOARGS,
     "Stop the C event loop (closes listeners and connections safely)"},
    {"_cleanup", (PyCFunction)pyServer_cleanup, METH_NOARGS, NULL},
    {"link_custom_data_types", (PyCFunction)linkServerCustomDataTypes,
     METH_VARARGS, "Link a pre-built type capsule (from o6._o6.build_custom_data_types) into this server"},
    {"add_namespace", (PyCFunction)pyServer_add_namespace, METH_VARARGS,
     "Register a namespace URI and return its index"},
    {"get_namespace_index", (PyCFunction)pyServer_get_namespace_index, METH_VARARGS,
     "Get the namespace index for a URI (raises KeyError if not found)"},
    {"get_namespace_uri", (PyCFunction)pyServer_get_namespace_uri, METH_VARARGS,
     "Get the namespace URI for an index"},
    {"find_data_type", (PyCFunction)pyServer_find_data_type, METH_VARARGS,
     "Look up a DataType by NodeId and return its Python type or metadata."},
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
