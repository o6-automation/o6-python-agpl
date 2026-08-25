/* Copyright 2026 (c) o6 Automation GmbH */
#include "server.h"
#include "../module.h"
#include "../types_internal.h"
#include "../open62541_queue.h"
#include "../services_subscriptions.h"

/********************************************************************
 * DataChange MonitoredItem
 ********************************************************************/

static struct MonitoredItemBundleList s_datachange = { NULL };

static void
pyDataChangeCallback(UA_Server *server, UA_UInt32 monitoredItemId,
                     void *monitoredItemContext,
                     const UA_NodeId *nodeId, void *nodeContext,
                     UA_UInt32 attributeId,
                     const UA_DataValue *value) {
    MonitoredItemBundle *b = (MonitoredItemBundle *)monitoredItemContext;
    if (!b || !b->notification_cb)
        return;

    const UA_NamespaceMapping *nsMapping =
        b->pyServer ? &b->pyServer->nsMapPy2UA : NULL;

    PyObject *py_id   = PyLong_FromUnsignedLong(monitoredItemId);
    PyObject *py_node = UA2PY((void *)nodeId, &UA_TYPES[UA_TYPES_NODEID], nsMapping);
    PyObject *py_attr = PyLong_FromUnsignedLong(attributeId);
    PyObject *py_val  = UA2PY((void *)value, &UA_TYPES[UA_TYPES_DATAVALUE], nsMapping);

    if (!py_id || !py_node || !py_attr || !py_val) {
        Py_XDECREF(py_id); Py_XDECREF(py_node);
        Py_XDECREF(py_attr); Py_XDECREF(py_val);
        PyErr_Clear();
        return;
    }

    PyObject *ctx = b->context ? b->context : Py_None;
    PyObject *result = PyObject_CallFunctionObjArgs(
        b->notification_cb, py_id, py_node, py_attr, py_val, ctx, NULL);
    Py_DECREF(py_id); Py_DECREF(py_node);
    Py_DECREF(py_attr); Py_DECREF(py_val);
    handleServerCallbackResult(server, result);
}

/* Common tail of the three create paths: on success take ownership of the
 * monitoredItemId and register the bundle on *list*, on failure free the
 * bundle and raise. Consumes *result*. */
static PyObject *
finishMonitoredItemCreate(struct MonitoredItemBundleList *list,
                          MonitoredItemBundle *bundle,
                          UA_MonitoredItemCreateResult *result) {
    if (result->statusCode != UA_STATUSCODE_GOOD) {
        PyObject *err = PyErr_StatusCode(result->statusCode);
        UA_MonitoredItemCreateResult_clear(result);
        monitoredItemBundle_free(bundle);
        return err;
    }

    bundle->monitoredItemId = result->monitoredItemId;
    UA_UInt32 mid = result->monitoredItemId;
    UA_MonitoredItemCreateResult_clear(result);

    SLIST_INSERT_HEAD(list, bundle, entry);
    return PyLong_FromUnsignedLong(mid);
}

/********************************************************************
 * Event MonitoredItem
 ********************************************************************/

static struct MonitoredItemBundleList s_event = { NULL };

#ifdef UA_ENABLE_SUBSCRIPTIONS_EVENTS
static void
pyEventCallback(UA_Server *server, UA_UInt32 monitoredItemId,
                void *monitoredItemContext,
                const UA_KeyValueMap eventFields) {
    MonitoredItemBundle *b = (MonitoredItemBundle *)monitoredItemContext;
    if (!b || !b->notification_cb)
        return;

    const UA_NamespaceMapping *nsMapping =
        b->pyServer ? &b->pyServer->nsMapPy2UA : NULL;

    PyObject *py_id     = PyLong_FromUnsignedLong(monitoredItemId);
    PyObject *py_fields = keyValueMap_to_pydict(&eventFields, nsMapping);

    if (!py_id || !py_fields) {
        Py_XDECREF(py_id); Py_XDECREF(py_fields);
        PyErr_Clear();
        return;
    }

    PyObject *ctx = b->context ? b->context : Py_None;
    PyObject *result = PyObject_CallFunctionObjArgs(
        b->notification_cb, py_id, py_fields, ctx, NULL);
    Py_DECREF(py_id); Py_DECREF(py_fields);
    handleServerCallbackResult(server, result);
}
#endif /* UA_ENABLE_SUBSCRIPTIONS_EVENTS */

/********************************************************************
 * Server Repeated Callbacks
 ********************************************************************/

typedef struct ServerRepeatBundle ServerRepeatBundle;
struct ServerRepeatBundle {
    UA_UInt64  callbackId;
    UA_Server *server;
    PyObject  *callback;
    PyServer  *pyServer;
    SLIST_ENTRY(ServerRepeatBundle) entry;
};

SLIST_HEAD(RepeatBundleList, ServerRepeatBundle);
static struct RepeatBundleList s_repeat = { NULL };

static void
pyServerCallbackBridge(UA_Server *server, void *data) {
    PyObject *callback = (PyObject *)data;
    if (!callback)
        return;
    assertGIL();
    PyObject *result = PyObject_CallNoArgs(callback);
    handleServerCallbackResult(server, result);
}

/********************************************************************
 * Bulk cleanup (called from clear_server_runtime_callbacks in server_nodes.c)
 ********************************************************************/

void
clear_server_monitored_item_callbacks(UA_Server *server) {
    monitoredItemBundle_clear_server_from_list(&s_datachange, server);
    monitoredItemBundle_clear_server_from_list(&s_event, server);
}

void
clear_server_repeat_callbacks(UA_Server *server) {
    ServerRepeatBundle *b, *tmp;
    SLIST_FOREACH_SAFE(b, &s_repeat, entry, tmp) {
        if (b->server == server) {
            SLIST_REMOVE(&s_repeat, b, ServerRepeatBundle, entry);
            pyServer_release_callback_ref(b->pyServer, b->callback);
            UA_free(b);
        }
    }
}

/********************************************************************
 * MonitoredItem Service Set
 ********************************************************************/

PyObject *
pyServer_create_data_change_monitored_item(PyObject *self, PyObject *args) {
    PyServer *srv = (PyServer *)self;

    PyObject *mir_obj, *timestamps_obj, *context_obj, *callback_obj;
    if (!PyArg_ParseTuple(args, "OOOO",
                          &mir_obj, &timestamps_obj, &context_obj, &callback_obj))
        return NULL;

    if (!PyCallable_Check(callback_obj)) {
        PyErr_SetString(PyExc_TypeError, "callback must be callable");
        return NULL;
    }

    const UA_NamespaceMapping *nsMapping = &srv->nsMapPy2UA;
    const UA_DataTypeArray *customDataTypes =
        UA_Server_getConfig(srv->server)->customDataTypes;

    UA_MonitoredItemCreateRequest mir;
    UA_MonitoredItemCreateRequest_init(&mir);
    PyObject *res = PY2UA(mir_obj, &mir,
                          &UA_TYPES[UA_TYPES_MONITOREDITEMCREATEREQUEST],
                          nsMapping, customDataTypes);
    if (!res) {
        UA_MonitoredItemCreateRequest_clear(&mir);
        return NULL;
    }
    Py_DECREF(res);

    UA_TimestampsToReturn ttr = UA_TIMESTAMPSTORETURN_NEITHER;
    res = PY2UA(timestamps_obj, &ttr,
                &UA_TYPES[UA_TYPES_TIMESTAMPSTORETURN],
                nsMapping, customDataTypes);
    if (!res) {
        UA_MonitoredItemCreateRequest_clear(&mir);
        return NULL;
    }
    Py_DECREF(res);

    MonitoredItemBundle *bundle = monitoredItemBundle_new(
        NULL,
        srv,
        srv->server,
        callback_obj,
        context_obj != Py_None ? context_obj : NULL,
        NULL);
    if (!bundle) {
        UA_MonitoredItemCreateRequest_clear(&mir);
        return NULL;
    }

    UA_MonitoredItemCreateResult result =
        UA_Server_createDataChangeMonitoredItem(
            srv->server, ttr, mir, bundle, pyDataChangeCallback);

    UA_MonitoredItemCreateRequest_clear(&mir);

    return finishMonitoredItemCreate(&s_datachange, bundle, &result);
}

PyObject *
pyServer_delete_monitored_item(PyObject *self, PyObject *args) {
    PyServer *srv = (PyServer *)self;

    unsigned int mid;
    if (!PyArg_ParseTuple(args, "I", &mid))
        return NULL;

    UA_StatusCode status =
        UA_Server_deleteMonitoredItem(srv->server, (UA_UInt32)mid);
    if (status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);

    monitoredItemBundle_remove_from_list(&s_datachange, (UA_UInt32)mid, srv->server);
    monitoredItemBundle_remove_from_list(&s_event, (UA_UInt32)mid, srv->server);
    Py_RETURN_NONE;
}

#ifdef UA_ENABLE_SUBSCRIPTIONS_EVENTS

PyObject *
pyServer_create_event_monitored_item(PyObject *self, PyObject *args) {
    PyServer *srv = (PyServer *)self;

    PyObject *nodeid_obj, *filter_obj, *context_obj, *callback_obj;
    if (!PyArg_ParseTuple(args, "OOOO",
                          &nodeid_obj, &filter_obj, &context_obj, &callback_obj))
        return NULL;

    if (!PyCallable_Check(callback_obj)) {
        PyErr_SetString(PyExc_TypeError, "callback must be callable");
        return NULL;
    }

    const UA_NamespaceMapping *nsMapping = &srv->nsMapPy2UA;
    const UA_DataTypeArray *customDataTypes =
        UA_Server_getConfig(srv->server)->customDataTypes;

    UA_NodeId nodeId;
    UA_NodeId_init(&nodeId);
    PyObject *res = PY2UA(nodeid_obj, &nodeId, &UA_TYPES[UA_TYPES_NODEID],
                          nsMapping, customDataTypes);
    if (!res)
        return NULL;
    Py_DECREF(res);

    UA_EventFilter filter;
    UA_EventFilter_init(&filter);
    res = PY2UA(filter_obj, &filter, &UA_TYPES[UA_TYPES_EVENTFILTER],
                nsMapping, customDataTypes);
    if (!res) {
        UA_NodeId_clear(&nodeId);
        return NULL;
    }
    Py_DECREF(res);

    MonitoredItemBundle *bundle = monitoredItemBundle_new(
        NULL,
        srv,
        srv->server,
        callback_obj,
        context_obj != Py_None ? context_obj : NULL,
        NULL);
    if (!bundle) {
        UA_NodeId_clear(&nodeId);
        UA_EventFilter_clear(&filter);
        return NULL;
    }

    UA_MonitoredItemCreateResult result =
        UA_Server_createEventMonitoredItem(
            srv->server, nodeId, filter, bundle, pyEventCallback);

    UA_NodeId_clear(&nodeId);
    UA_EventFilter_clear(&filter);

    return finishMonitoredItemCreate(&s_event, bundle, &result);
}

PyObject *
pyServer_create_event_monitored_item_ex(PyObject *self, PyObject *args) {
    PyServer *srv = (PyServer *)self;

    PyObject *mir_obj, *context_obj, *callback_obj;
    if (!PyArg_ParseTuple(args, "OOO", &mir_obj, &context_obj, &callback_obj))
        return NULL;

    if (!PyCallable_Check(callback_obj)) {
        PyErr_SetString(PyExc_TypeError, "callback must be callable");
        return NULL;
    }

    const UA_NamespaceMapping *nsMapping = &srv->nsMapPy2UA;
    const UA_DataTypeArray *customDataTypes =
        UA_Server_getConfig(srv->server)->customDataTypes;

    UA_MonitoredItemCreateRequest mir;
    UA_MonitoredItemCreateRequest_init(&mir);
    PyObject *res = PY2UA(mir_obj, &mir,
                          &UA_TYPES[UA_TYPES_MONITOREDITEMCREATEREQUEST],
                          nsMapping, customDataTypes);
    if (!res) {
        UA_MonitoredItemCreateRequest_clear(&mir);
        return NULL;
    }
    Py_DECREF(res);

    MonitoredItemBundle *bundle = monitoredItemBundle_new(
        NULL,
        srv,
        srv->server,
        callback_obj,
        context_obj != Py_None ? context_obj : NULL,
        NULL);
    if (!bundle) {
        UA_MonitoredItemCreateRequest_clear(&mir);
        return NULL;
    }

    UA_MonitoredItemCreateResult result =
        UA_Server_createEventMonitoredItemEx(
            srv->server, mir, bundle, pyEventCallback);

    UA_MonitoredItemCreateRequest_clear(&mir);

    return finishMonitoredItemCreate(&s_event, bundle, &result);
}

#else /* UA_ENABLE_SUBSCRIPTIONS_EVENTS not defined */

PyObject *
pyServer_create_event_monitored_item(PyObject *self, PyObject *args) {
    (void)self; (void)args;
    PyErr_SetString(PyExc_NotImplementedError,
                    "Event MonitoredItems require UA_ENABLE_SUBSCRIPTIONS_EVENTS "
                    "in the open62541 build");
    return NULL;
}

PyObject *
pyServer_create_event_monitored_item_ex(PyObject *self, PyObject *args) {
    (void)self; (void)args;
    PyErr_SetString(PyExc_NotImplementedError,
                    "Event MonitoredItems require UA_ENABLE_SUBSCRIPTIONS_EVENTS "
                    "in the open62541 build");
    return NULL;
}

#endif /* UA_ENABLE_SUBSCRIPTIONS_EVENTS */

/********************************************************************
 * Callbacks and Repeated Callbacks
 ********************************************************************/

PyObject *
pyServer_add_repeated_callback(PyObject *self, PyObject *args) {
    PyServer *srv = (PyServer *)self;

    PyObject *callback;
    double interval_ms;
    if (!PyArg_ParseTuple(args, "Od", &callback, &interval_ms))
        return NULL;

    if (!PyCallable_Check(callback)) {
        PyErr_SetString(PyExc_TypeError, "callback must be callable");
        return NULL;
    }

    ServerRepeatBundle *bundle =
        (ServerRepeatBundle *)UA_calloc(1, sizeof(ServerRepeatBundle));
    if (!bundle) {
        PyErr_NoMemory();
        return NULL;
    }
    bundle->server = srv->server;
    bundle->callback = callback;
    bundle->pyServer = srv;
    if (pyServer_own_callback_ref(srv, callback) < 0) {
        UA_free(bundle);
        return NULL;
    }

    UA_UInt64 callbackId = 0;
    UA_StatusCode status = UA_Server_addRepeatedCallback(
        srv->server, pyServerCallbackBridge, callback, interval_ms, &callbackId);
    if (status != UA_STATUSCODE_GOOD) {
        pyServer_release_callback_ref(srv, callback);
        UA_free(bundle);
        return PyErr_StatusCode(status);
    }

    bundle->callbackId = callbackId;
    SLIST_INSERT_HEAD(&s_repeat, bundle, entry);
    return PyLong_FromUnsignedLongLong(callbackId);
}

PyObject *
pyServer_change_repeated_callback_interval(PyObject *self, PyObject *args) {
    PyServer *srv = (PyServer *)self;

    unsigned long long callbackId;
    double interval_ms;
    if (!PyArg_ParseTuple(args, "Kd", &callbackId, &interval_ms))
        return NULL;

    UA_StatusCode status = UA_Server_changeRepeatedCallbackInterval(
        srv->server, (UA_UInt64)callbackId, interval_ms);
    if (status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);
    Py_RETURN_NONE;
}

PyObject *
pyServer_remove_callback(PyObject *self, PyObject *args) {
    PyServer *srv = (PyServer *)self;

    unsigned long long callbackId;
    if (!PyArg_ParseTuple(args, "K", &callbackId))
        return NULL;

    UA_Server_removeCallback(srv->server, (UA_UInt64)callbackId);

    ServerRepeatBundle *b, *tmp;
    SLIST_FOREACH_SAFE(b, &s_repeat, entry, tmp) {
        if (b->callbackId == (UA_UInt64)callbackId && b->server == srv->server) {
            SLIST_REMOVE(&s_repeat, b, ServerRepeatBundle, entry);
            pyServer_release_callback_ref(b->pyServer, b->callback);
            UA_free(b);
            break;
        }
    }
    Py_RETURN_NONE;
}
