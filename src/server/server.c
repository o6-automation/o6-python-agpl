/* Copyright 2026 (c) o6 Automation GmbH (Author: Andreas Ebner) */
#include "server.h"
#include "../utils.h"
#include "module.h"
#include "../types_internal.h"
#include "../datatypes.h"
#include "../ua_extension_namespacemapping.h"
#include "python_nodestore.h"

/**********************/
/* Server Lifecycle   */
/**********************/

static void pyServer_do_cleanup(PyServer *self);

static UA_GlobalNodeLifecycle pyGlobalNodeLifecycle = {
    .earlyConstructor = pyGlobalNodeEarlyConstructor,
    .constructor = pyGlobalNodeConstructor,
};

static int
pyServer_init(PyServer *self, PyObject *args, PyObject *kwds) {
    if(o6_require_server() < 0)
        return -1;

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

    if(pubsub_enabled) {
        /* PubSub is server-only. Keep its transports out of client event loops
         * and out of Server configurations without the PubSub entitlement. */
        UA_ConnectionManager *udpCM = UA_ConnectionManager_new_AsyncIO_UDP();
        if(!udpCM || config.eventLoop->registerEventSource(
                         config.eventLoop, &udpCM->eventSource) != UA_STATUSCODE_GOOD) {
            if(udpCM)
                udpCM->eventSource.free(&udpCM->eventSource);
            config.eventLoop->free(config.eventLoop);
            PyErr_SetString(PyExc_RuntimeError,
                            "Could not create the UDP PubSub transport");
            return -1;
        }

#if defined(__linux__)
        UA_ConnectionManager *ethCM = UA_ConnectionManager_new_AsyncIO_Ethernet();
        if(!ethCM || config.eventLoop->registerEventSource(
                         config.eventLoop, &ethCM->eventSource) != UA_STATUSCODE_GOOD) {
            if(ethCM)
                ethCM->eventSource.free(&ethCM->eventSource);
            config.eventLoop->free(config.eventLoop);
            PyErr_SetString(PyExc_RuntimeError,
                            "Could not create the Ethernet PubSub transport");
            return -1;
        }
#endif

#ifdef UA_ENABLE_MQTT
        /* The architecture-independent MQTT manager uses the AsyncIO TCP manager
         * already registered by UA_EventLoop_new_AsyncIO. */
        UA_ConnectionManager *mqttCM =
            UA_ConnectionManager_new_MQTT(UA_STRING("mqtt connection manager"));
        if(!mqttCM || config.eventLoop->registerEventSource(
                          config.eventLoop, &mqttCM->eventSource) != UA_STATUSCODE_GOOD) {
            if(mqttCM)
                mqttCM->eventSource.free(&mqttCM->eventSource);
            config.eventLoop->free(config.eventLoop);
            PyErr_SetString(PyExc_RuntimeError,
                            "Could not create the MQTT PubSub transport");
            return -1;
        }
#endif
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

#ifdef UA_ENABLE_PUBSUB
    /* This prevents open62541 from allocating a PubSub manager or installing
     * its information-model methods when the active Credential omits PubSub. */
    config.pubsubEnabled = pubsub_enabled;
#endif

    /* Python state machines are attached to the concrete information-model
     * node. The PubSub component becomes visible only after that node has
     * finished construction, so the component lifecycle is the first point
     * where a constructor-installed callback can be applied. */
    if(pubsub_enabled)
        config.pubSubConfig.componentLifecycleCallback =
            pyPubSubComponentLifecycle;

    /* Install the o6 stable-pointer nodestore before UA_Server construction
     * populates namespace zero. */
    UA_Nodestore *pythonNodeStore = pyNodeStore_new(self);
    if(!pythonNodeStore) {
        UA_ServerConfig_clear(&config);
        if(!PyErr_Occurred())
            PyErr_NoMemory();
        return -1;
    }
    if(config.nodestore)
        config.nodestore->free(config.nodestore);
    config.nodestore = pythonNodeStore;
    config.nodeLifecycle = &pyGlobalNodeLifecycle;
    config.copyMethodsOnInstances = true;

    self->server = UA_Server_newWithConfig(&config);
    if (!self->server) {
        PyErr_NoMemory();
        return -1;
    }
#ifdef UA_ENABLE_PUBSUB
    UA_assert(UA_Server_getConfig(self->server)->pubsubEnabled == pubsub_enabled);
#endif

    /* A server must contain only server-indexed copies of custom DataTypes.
     * Attaching the process-global chain here mixes stable Python namespace
     * indexes with server-local indexes.  Once those numbers overlap,
     * UA_findDataTypeWithCustom can select an unrelated layout with the same
     * numeric NodeId.  add_namespace() copies each newly mapped namespace
     * into this initially empty server-owned chain. */
    UA_Server_getConfig(self->server)->customDataTypes = NULL;

    /* Mark as externally managed so that run_shutdown / server_clear
     * do not try to iterate the AsyncIO loop (which returns
     * BADNOTIMPLEMENTED from run()).  We manage the loop lifecycle
     * ourselves in pyServer_clear. */
    UA_Server_getConfig(self->server)->externalEventLoop = true;

    self->running = false;
    self->hasHistoryDB = false;
    memset(&self->gathering, 0, sizeof(UA_HistoryDataGathering));
    self->runtimeCallbackRefs = PyList_New(0);
    if (!self->runtimeCallbackRefs) {
        pyServer_do_cleanup(self);
        return -1;
    }

    /* Store a back-pointer so callbacks can detect teardown via NULL check */
    UA_Server_getConfig(self->server)->context = self;

    return 0;
}

/* Core cleanup: delete the UA_Server, free the event loop.
 * Does NOT call tp_free — the caller is responsible for that.
 * Safe to call from __del__ (tp_finalize) where Python API calls
 * (Py_DECREF on asyncio handles) are safe, and from tp_dealloc. */
static void
pyServer_do_cleanup(PyServer *self) {
    if (!self->server) {
        Py_CLEAR(self->runtimeCallbackRefs);
        return;
    }

    UA_ServerConfig *config = UA_Server_getConfig(self->server);
    config->context = NULL;

    if(config->logging)
        config->logging->context = NULL;
    if(config->eventLoop && config->eventLoop->logger)
        ((UA_Logger*)config->eventLoop->logger)->context = NULL;

    if (self->running) {
        self->running = false;
        UA_Server_run_shutdown(self->server);
    }

    /* Cancel callbacks whose lifetime is not tied to a node. Node-owned
     * references are released directly by the nodestore. */
    clear_server_runtime_callbacks(self->server, self);

    UA_EventLoop *el = config->eventLoop;

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

    /* Type lifecycle destructors need the back-pointer while
     * UA_Server_delete walks the remaining nodes. */
    config->context = self;
    UA_Server_delete(self->server);
    self->server = NULL;
    Py_CLEAR(self->runtimeCallbackRefs);

    /* Free the python<->UA namespace mapping tables allocated during
     * add_namespace. UA_NamespaceMapping_clear releases the URI strings
     * and the local2remote / remote2local arrays. */
    UA_NamespaceMapping_clear(&self->nsMapPy2UA);

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

int
pyServer_own_callback_ref(PyServer *server, PyObject *object) {
    if (!object || object == Py_None)
        return 0;
    if (!server || !server->server || !server->runtimeCallbackRefs) {
        PyErr_SetString(PyExc_RuntimeError, "server is already closed");
        return -1;
    }
    return PyList_Append(server->runtimeCallbackRefs, object);
}

void
pyServer_release_callback_ref(PyServer *server, PyObject *object) {
    if (!server || !server->runtimeCallbackRefs || !object)
        return;
    Py_ssize_t size = PyList_GET_SIZE(server->runtimeCallbackRefs);
    for (Py_ssize_t i = 0; i < size; i++) {
        if (PyList_GET_ITEM(server->runtimeCallbackRefs, i) == object) {
            if (PySequence_DelItem(server->runtimeCallbackRefs, i) < 0)
                PyErr_Clear();
            return;
        }
    }
}

static int
pyServer_traverse(PyServer *self, visitproc visit, void *arg) {
    Py_VISIT(self->runtimeCallbackRefs);
    if(pyNodeStore_traverse(self, visit, arg) < 0)
        return -1;
    return 0;
}

static int
pyServer_clear_refs(PyServer *self) {
    pyServer_do_cleanup(self);
    return 0;
}

static void
pyServer_clear(PyServer *self) {
    PyObject_GC_UnTrack(self);
    /* If _cleanup() was not called from __del__, we are in tp_dealloc
     * (possibly during GC sweep).  Mark tearingDown so that
     * AsyncIOTCP_eventSourceStop skips PyObject_CallMethod calls. */
    if(self->server) {
        UA_ServerConfig *config = UA_Server_getConfig(self->server);
        if(config && config->eventLoop)
            ((AsyncIOLoop*)config->eventLoop)->tearingDown = 1;
    }
    pyServer_clear_refs(self);
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
    unsigned short python_idx;
    if(!PyArg_ParseTuple(args, "sH", &uri, &python_idx))
        return NULL;
    if(!self->server) {
        PyErr_SetString(PyExc_RuntimeError, "Server not initialized");
        return NULL;
    }
    UA_UInt16 server_idx = UA_Server_addNamespace(self->server, uri);

    /* Atomically populate the python<->UA namespace mapping so callers can
     * subsequently build NodeIds / QualifiedNames with the global index
     * and have PY2UA/UA2PY translate them to the correct server-side index
     * in a single recursive walk. */
    UA_String src = UA_STRING((char*)(uintptr_t)uri);
    UA_StatusCode st = ua_extension_namespace_mapping_set(&self->nsMapPy2UA,
                                                          src,
                                                          (UA_UInt16)python_idx,
                                                          server_idx);
    if(st != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(st);

    /* Update the server's customDataTypes chain so that types from the
     * global registry whose namespace is now mapped get deep-copied
     * with server-side namespace indices. */
    st = o6_datatypes_update_custom_datatypes(
        &self->nsMapPy2UA,
        &UA_Server_getConfig(self->server)->customDataTypes);
    if(st != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(st);

    return PyLong_FromLong((long)server_idx);
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

    PyObject *result = UA2PY(
        &nsUri, &UA_TYPES[UA_TYPES_STRING], &self->nsMapPy2UA);
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
    {"_run_startup", (PyCFunction)pyServer_run_startup, METH_VARARGS,
     "Start the server networking layer"},
    {"_run_shutdown", (PyCFunction)pyServer_run_shutdown_py, METH_VARARGS,
     "Shut down the server networking layer"},
    {"_add_variable_node", (PyCFunction)pyServer_add_variable_node, METH_VARARGS,
     "Add a variable node to the server address space"},
    {"_add_node_begin", (PyCFunction)pyServer_add_node_begin, METH_VARARGS,
     "Two-phase add (begin): create a node with a requested NodeId without "
     "instantiating its type's children yet. Returns the actual NodeId.\n"
     "add_node_begin(nodeclass, requested, parent, reftype, browse, typedef, attr)"},
    {"_add_node_raw", (PyCFunction)pyServer_add_node_raw, METH_VARARGS,
     "Create and return the canonical Python node before defining references "
     "or constructors are applied"},
    {"_add_node_prepare", (PyCFunction)pyServer_add_node_prepare, METH_VARARGS,
     "Complete the begin phase for a raw node"},
    {"_add_node_finish", (PyCFunction)pyServer_add_node_finish, METH_VARARGS,
     "Two-phase add (finish): complete instantiation of a node begun with "
     "add_node_begin.\nadd_node_finish(nodeid)"},
    {"_set_type_abstract", (PyCFunction)pyServer_set_type_abstract, METH_VARARGS,
     "Internal NodeSet-loader hook for temporarily changing IsAbstract"},
    {"_add_object_node", (PyCFunction)pyServer_add_object_node, METH_VARARGS,
     "Add an object node to the server address space"},
    {"_add_object_type_node", (PyCFunction)pyServer_add_object_type_node, METH_VARARGS,
     "Add an object type node to the server address space"},
    {"_add_variable_type_node", (PyCFunction)pyServer_add_variable_type_node, METH_VARARGS,
     "Add a variable type node to the server address space"},
    {"_add_data_type_node", (PyCFunction)pyServer_add_data_type_node, METH_VARARGS,
     "Add a data type node to the server address space"},
    {"_add_reference_type_node", (PyCFunction)pyServer_add_reference_type_node, METH_VARARGS,
     "Add a reference type node to the server address space"},
    {"_add_view_node", (PyCFunction)pyServer_add_view_node, METH_VARARGS,
     "Add a view node to the server address space"},
    {"_add_method_node", (PyCFunction)pyServer_add_method_node, METH_VARARGS,
     "Add a method node to the server address space"},
    {"_set_callback_slot", (PyCFunction)pyServer_set_callback_slot, METH_VARARGS,
     "Replace one node-owned callback slot and its optional receiver"},
    {"_set_local_value", (PyCFunction)pyServer_set_local_value, METH_VARARGS,
     "Replace Variable callbacks with one explicit native DataValue"},
    {"_get_callback", (PyCFunction)pyServer_get_callback, METH_VARARGS,
     "Return one node-owned Python callback slot"},
    {"_get_node_type", (PyCFunction)pyServer_get_node_type, METH_VARARGS,
     "Return the HasTypeDefinition target for an Object or Variable"},
    {"_add_reference", (PyCFunction)pyServer_add_reference, METH_VARARGS,
     "Add a reference between two nodes"},
    {"_delete_reference", (PyCFunction)pyServer_delete_reference, METH_VARARGS,
     "Delete a reference between two nodes"},
    {"_delete_node", (PyCFunction)pyServer_delete_node, METH_VARARGS,
     "Delete a node from the address space"},
    {"_read_value", (PyCFunction)pyServer_read_value, METH_VARARGS,
     "Read a variable value: read_value(nodeid, index_range=None)"},
    {"_write_value", (PyCFunction)pyServer_write_value, METH_VARARGS,
     "Write a variable value: write_value(nodeid, value, index_range=None)"},
    {"_call", (PyCFunction)pyServer_call, METH_VARARGS,
     "Call a method node server-side with admin privileges.\n"
     "call(object_id, method_id, input_args) -> (StatusCode, ...)"},
    {"_emit_event", (PyCFunction)pyServer_emit_event, METH_VARARGS,
     "Emit an OPC UA event and return its EventId."},
    {"_set_pubsub_connection_enabled",
     (PyCFunction)pyServer_set_pubsub_connection_enabled, METH_VARARGS,
     "Enable or disable a native PubSubConnection."},
    {"_set_pubsub_component_enabled",
     (PyCFunction)pyServer_set_pubsub_component_enabled, METH_VARARGS,
     "Enable or disable one native PubSub component."},
    {"_remove_pubsub_connection",
     (PyCFunction)pyServer_remove_pubsub_connection, METH_VARARGS,
     "Remove a native PubSubConnection and its components."},
    {"_set_all_pubsub_components_enabled",
     (PyCFunction)pyServer_set_all_pubsub_components_enabled, METH_VARARGS,
     "Enable or disable every native PubSub component."},
    {"_read_object_property", (PyCFunction)pyServer_read_object_property, METH_VARARGS,
     "Read an object property by BrowseName"},
    {"_write_object_property", (PyCFunction)pyServer_write_object_property, METH_VARARGS,
     "Write an object property by BrowseName"},
    {"_add_reverse_connect", (PyCFunction)pyServer_add_reverse_connect, METH_VARARGS,
     "Register a reverse connect to a client URL"},
    {"_remove_reverse_connect", (PyCFunction)pyServer_remove_reverse_connect, METH_VARARGS,
     "Remove a reverse connect by handle"},
    {"_register_historizing", (PyCFunction)pyServer_register_historizing,
     METH_VARARGS | METH_KEYWORDS, "Register a node for historical data gathering."},
    {"_read_attribute", (PyCFunction)pyServer_read_attribute, METH_VARARGS,
     "Read a node attribute: read_attribute(nodeid, attr_id) -> value"},
    {"_write_attribute", (PyCFunction)pyServer_write_attribute, METH_VARARGS,
     "Write a node attribute: write_attribute(nodeid, attr_id, value) -> None"},
    {"_write_data_value", (PyCFunction)pyServer_write_data_value, METH_VARARGS,
     "Write a DataValue: write_data_value(nodeid, datavalue, index_range=None)"},
    {"_translate_browse_paths", (PyCFunction)pyServer_translate_browse_paths,
     METH_VARARGS,
     "Server-side translate browse paths to node ids"},
    {"_get_node", (PyCFunction)pyNodeStore_getNode, METH_VARARGS,
     "Return the canonical Python object for a server node"},
    {"_stop_event_loop", (PyCFunction)pyServer_stop_event_loop, METH_NOARGS,
     "Stop the C event loop (closes listeners and connections safely)"},
    {"_cleanup", (PyCFunction)pyServer_cleanup, METH_NOARGS, NULL},
    {"_add_namespace", (PyCFunction)pyServer_add_namespace, METH_VARARGS,
     "Register a namespace URI and return its index"},
    {"_get_namespace_index", (PyCFunction)pyServer_get_namespace_index, METH_VARARGS,
     "Get the namespace index for a URI (raises KeyError if not found)"},
    {"_get_namespace_uri", (PyCFunction)pyServer_get_namespace_uri, METH_VARARGS,
     "Get the namespace URI for an index"},
    {"_find_data_type", (PyCFunction)pyServer_find_data_type, METH_VARARGS,
     "Look up a DataType by NodeId and return its Python type or metadata."},
     {"_browse", (PyCFunction)pyServer_browse, METH_VARARGS,  NULL},
     {"_browse_next", (PyCFunction)pyServer_browse_next, METH_VARARGS,  NULL},
     {"_browse_recursive", (PyCFunction)pyServer_browse_recursive, METH_VARARGS,  NULL},
     {"_translate_browse_paths_to_nodeids", (PyCFunction)pyServer_translate_browse_paths_to_nodeids, METH_VARARGS,  NULL},
     {"_browse_simplified_browse_paths", (PyCFunction)pyServer_browse_simplified_browse_paths, METH_VARARGS,  NULL},
     {"_for_each_child_node", (PyCFunction)pyServer_for_each_child_node, METH_VARARGS,  NULL},
     {"_register_discovery", (PyCFunction)pyServer_register_discovery, METH_VARARGS,
      "Register this server at a Discovery Server (LDS).\n\n"
      "register_discovery(discovery_server_url, [semaphore_file_path]) -> None"},
     {"_deregister_discovery", (PyCFunction)pyServer_deregister_discovery, METH_VARARGS,
      "Deregister this server from a Discovery Server (LDS).\n\n"
      "deregister_discovery(discovery_server_url) -> None"},
     {"_set_register_server_callback", (PyCFunction)pyServer_set_register_server_callback, METH_VARARGS,
      "Set / clear the callback invoked when another server registers with this LDS.\n\n"
      "set_register_server_callback(callback) -> None\n"
      "Pass None to remove the callback."},
     {"_close_session", (PyCFunction)pyServer_close_session, METH_VARARGS, NULL},
     {"_get_session_attribute", (PyCFunction)pyServer_get_session_attribute, METH_VARARGS, NULL},
     {"_set_session_attribute", (PyCFunction)pyServer_set_session_attribute, METH_VARARGS, NULL},
     {"_delete_session_attribute", (PyCFunction)pyServer_delete_session_attribute, METH_VARARGS, NULL},
     {"_get_session_roles", (PyCFunction)pyServer_get_session_roles, METH_VARARGS, NULL},
     {"_set_session_roles", (PyCFunction)pyServer_set_session_roles, METH_VARARGS, NULL},
     {"_add_role", (PyCFunction)pyServer_add_role, METH_VARARGS, NULL},
     {"_update_role", (PyCFunction)pyServer_update_role, METH_VARARGS, NULL},
     {"_remove_role", (PyCFunction)pyServer_remove_role, METH_VARARGS, NULL},
     {"_get_role", (PyCFunction)pyServer_get_role, METH_VARARGS, NULL},
     {"_get_roles", (PyCFunction)pyServer_get_roles, METH_NOARGS, NULL},
     {"_set_node_role_permissions", (PyCFunction)pyServer_set_node_role_permissions, METH_VARARGS, NULL},
     {"_get_node_role_permissions", (PyCFunction)pyServer_get_node_role_permissions, METH_VARARGS, NULL},
     {"_remove_node_role_permissions", (PyCFunction)pyServer_remove_node_role_permissions, METH_VARARGS, NULL},
     {"_add_role_permissions", (PyCFunction)pyServer_add_role_permissions, METH_VARARGS, NULL},
     {"_remove_role_permissions", (PyCFunction)pyServer_remove_role_permissions, METH_VARARGS, NULL},
     {"_set_namespace_role_permissions", (PyCFunction)pyServer_set_namespace_role_permissions, METH_VARARGS, NULL},
     {"_get_namespace_role_permissions", (PyCFunction)pyServer_get_namespace_role_permissions, METH_VARARGS, NULL},
     {"_set_all_permissions_for_anonymous", (PyCFunction)pyServer_set_all_permissions_for_anonymous, METH_VARARGS, NULL},
#ifdef UA_ENABLE_DISCOVERY_MULTICAST
     {"_set_server_on_network_callback", (PyCFunction)pyServer_set_server_on_network_callback, METH_VARARGS,
      "Set / clear the callback invoked when a server is detected via mDNS.\n\n"
      "set_server_on_network_callback(callback) -> None\n"
      "Pass None to remove the callback.  Requires UA_ENABLE_DISCOVERY_MULTICAST."},
#endif

     {"_delete_monitored_item", (PyCFunction)pyServer_delete_monitored_item, METH_VARARGS,
      "delete_monitored_item(monitoredItemId) -> None\n\n"
      "Delete a local MonitoredItem by its numeric ID."},
     {"_create_data_change_monitored_item", (PyCFunction)pyServer_create_data_change_monitored_item, METH_VARARGS,
      "create_data_change_monitored_item(item, timestampsToReturn, context, callback) -> int\n\n"
      "Create a local DataChange MonitoredItem. Returns the monitoredItemId.\n"
      "callback(monitoredItemId, nodeId, attributeId, dataValue, context)"},
     {"_create_event_monitored_item", (PyCFunction)pyServer_create_event_monitored_item, METH_VARARGS,  NULL},
     {"_create_event_monitored_item_ex", (PyCFunction)pyServer_create_event_monitored_item_ex, METH_VARARGS,  NULL},
     {"_add_repeated_callback", (PyCFunction)pyServer_add_repeated_callback, METH_VARARGS,
      "add_repeated_callback(callback, interval_ms) -> callbackId\n\n"
      "Register a callback to be called at a fixed interval (in milliseconds).\n"
      "Returns an opaque integer ID that can be passed to\n"
      "change_repeated_callback_interval() or remove_callback()."},
     {"_change_repeated_callback_interval", (PyCFunction)pyServer_change_repeated_callback_interval, METH_VARARGS,
      "change_repeated_callback_interval(callbackId, interval_ms) -> None"},
     {"_remove_callback", (PyCFunction)pyServer_remove_callback, METH_VARARGS,
      "remove_callback(callbackId) -> None\n\nRemove a repeated callback by ID."},
    {NULL, NULL, 0, NULL}
};

static PyTypeObject ServerType = {
    .ob_base = PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "o6.Server",
    .tp_doc = PyDoc_STR("OPC UA Server"),
    .tp_basicsize = sizeof(PyServer),
    .tp_itemsize = 0,
    .tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE | Py_TPFLAGS_HAVE_GC,
    .tp_new = PyType_GenericNew,
    .tp_methods = pyServer_methods,
    .tp_getset = pyServer_getsetters,
    .tp_init = (initproc)pyServer_init,
    .tp_dealloc = (destructor)pyServer_clear,
    .tp_traverse = (traverseproc)pyServer_traverse,
    .tp_clear = (inquiry)pyServer_clear_refs,
    .tp_str = (reprfunc)pyServer_str,
    .tp_repr = (reprfunc)pyServer_repr
};

PyObject *pyServerModule(void) {
    if (PyType_Ready(&ServerType) < 0)
        return NULL;
    return (PyObject *)&ServerType;
}
