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

#include "client.h"
#include "../types_internal.h"
#include <open62541/client_subscriptions.h>

/* Per-item bundle held behind open62541's monContext for each MonitoredItem.
 * The library guarantees the delete callback fires exactly once per registered
 * item on every teardown path (success, subscription delete, session close,
 * disconnect, and pre/post-async create failure — verified in
 * Client_MonitoredItems_createAsync and MonitoredItems_create_async_handler),
 * so the C delete callback is the universal cleanup point. */
typedef struct {
    PyObject *notification_cb; /* required: data-change or event callable */
    PyObject *deleted_cb;      /* optional: user on_deleted callable, may be NULL */
} MonitoredItemBundle;

static void
monitoredItemBundle_free(MonitoredItemBundle *bundle) {
    if (!bundle)
        return;
    Py_XDECREF(bundle->notification_cb);
    Py_XDECREF(bundle->deleted_cb);
    UA_free(bundle);
}

// Called by the library when a monitored item is destroyed.
static void
deleteMonitoredItemCallback(UA_Client *client, UA_UInt32 subId, void *subContext,
                            UA_UInt32 monId, void *context) {
    WITH_OWNER(client);
    (void)subContext;
    MonitoredItemBundle *bundle = (MonitoredItemBundle *)context;
    if (!bundle)
        return;
    if (bundle->deleted_cb) {
        UA_ClientConfig *config = UA_Client_getConfig(client);
        /* During teardown clientContext is NULL — avoid calling into Python
         * from tp_dealloc/GC (see asyncServiceCallback for the same guard). */
        if (config->clientContext) {
            PyObject *pySubId = PyLong_FromUnsignedLong(subId);
            PyObject *pyMonId = PyLong_FromUnsignedLong(monId);
            if (pySubId && pyMonId) {
                PyObject *result = PyObject_CallFunctionObjArgs(
                    bundle->deleted_cb, pySubId, pyMonId, NULL);
                if (!result) {
                    PyErr_Print();
                    PyErr_Clear();
                } else {
                    Py_DECREF(result);
                }
            } else {
                PyErr_Clear();
            }
            Py_XDECREF(pySubId);
            Py_XDECREF(pyMonId);
        }
    }
    monitoredItemBundle_free(bundle);
    WITH_OWNER_END();
}

/* Allocates parallel arrays plus per-item bundles. Bundle takes a new
 * reference to notification_cb and (if non-NULL) deleted_cb. Returns 0 on
 * success, -1 on OOM (PyErr set, partial allocations cleaned up). The caller
 * must UA_free() the three arrays. The bundles themselves are owned by
 * open62541 once handed off and freed in deleteMonitoredItemCallback. */
static int
monitoredItem_setupCallbacks(size_t num_items,
                             PyObject *notification_cb,
                             PyObject *deleted_cb,
                             void *notification_fn,
                             void ***notification_callbacks_out,
                             void ***contexts_out,
                             UA_Client_DeleteMonitoredItemCallback **delete_callbacks_out) {

    void **callbacks = UA_malloc(num_items * sizeof(void *));
    void **contexts = UA_malloc(num_items * sizeof(void *));
    UA_Client_DeleteMonitoredItemCallback *deleteCallbacks =
        UA_malloc(num_items * sizeof(UA_Client_DeleteMonitoredItemCallback));

    if (!callbacks || !contexts || !deleteCallbacks) {
        UA_free(callbacks);
        UA_free(contexts);
        UA_free(deleteCallbacks);
        PyErr_NoMemory();
        return -1;
    }

    for (size_t i = 0; i < num_items; i++) {
        MonitoredItemBundle *bundle = (MonitoredItemBundle *)UA_calloc(
            1, sizeof(MonitoredItemBundle));
        if (!bundle) {
            /* Free any earlier bundles we allocated. */
            for (size_t j = 0; j < i; j++)
                monitoredItemBundle_free((MonitoredItemBundle *)contexts[j]);
            UA_free(callbacks);
            UA_free(contexts);
            UA_free(deleteCallbacks);
            PyErr_NoMemory();
            return -1;
        }
        Py_INCREF(notification_cb);
        bundle->notification_cb = notification_cb;
        if (deleted_cb) {
            Py_INCREF(deleted_cb);
            bundle->deleted_cb = deleted_cb;
        }
        callbacks[i] = notification_fn;
        contexts[i] = bundle;
        deleteCallbacks[i] = deleteMonitoredItemCallback;
    }

    *notification_callbacks_out = callbacks;
    *contexts_out = contexts;
    *delete_callbacks_out = deleteCallbacks;
    return 0;
}

// Data change notification callback
static void
dataChangeNotificationCallback(UA_Client *client, UA_UInt32 subId, void *subContext, UA_UInt32 monId, void *context, UA_DataValue *value) {
    WITH_OWNER(client);
    (void)client; (void)subId; (void)subContext; (void)monId;
    MonitoredItemBundle *bundle = (MonitoredItemBundle *)context;
    if (!bundle || !bundle->notification_cb)
        return;

    // Convert UA_DataValue to Python DataValue object so callbacks can access
    // status code and timestamps in addition to the raw value.
    PyObject *py_value = UA2PY(value, &UA_TYPES[UA_TYPES_DATAVALUE]);
    if (!py_value)
        return;

    // Call the Python callback
    PyObject *result = PyObject_CallOneArg(bundle->notification_cb, py_value);
    if (!result) {
        PyErr_Print();
    } else {
        Py_DECREF(result);
    }
    Py_DECREF(py_value);
    WITH_OWNER_END();
}

// Event notification callback
static void
eventNotificationCallback(UA_Client *client, UA_UInt32 subId, void *subContext, UA_UInt32 monId, void *context, const UA_KeyValueMap eventFields) {
    WITH_OWNER(client);
    (void)client; (void)subId; (void)subContext; (void)monId;
    MonitoredItemBundle *bundle = (MonitoredItemBundle *)context;
    if (!bundle || !bundle->notification_cb)
        return;

    // Convert UA_KeyValueMap to Python dict
    PyObject *event_dict = PyDict_New();
    if (!event_dict)
        return;

    for (size_t i = 0; i < eventFields.mapSize; i++) {
        const UA_KeyValuePair *pair = &eventFields.map[i];

        // Build key string from QualifiedName
        PyObject *py_key;
        if (pair->key.namespaceIndex == 0) {
            py_key = PyUnicode_FromStringAndSize(
                (const char*)pair->key.name.data, (Py_ssize_t)pair->key.name.length);
        } else {
            py_key = PyUnicode_FromFormat("ns=%u:%.*s",
                                          (unsigned)pair->key.namespaceIndex,
                                          (int)pair->key.name.length,
                                          (const char*)pair->key.name.data);
        }
        if (!py_key) {
            Py_DECREF(event_dict);
            return;
        }

        // Convert value (UA_Variant) to Python
        PyObject *py_val = UA2PY((void *)&pair->value, &UA_TYPES[UA_TYPES_VARIANT]);
        if (!py_val) {
            Py_DECREF(py_key);
            Py_DECREF(event_dict);
            return;
        }

        if (PyDict_SetItem(event_dict, py_key, py_val) < 0) {
            Py_DECREF(py_key);
            Py_DECREF(py_val);
            Py_DECREF(event_dict);
            return;
        }
        Py_DECREF(py_key);
        Py_DECREF(py_val);
    }

    // Call the Python callback with the event dict
    PyObject *result = PyObject_CallOneArg(bundle->notification_cb, event_dict);
    if (!result) {
        PyErr_Print();
    } else {
        Py_DECREF(result);
    }
    Py_DECREF(event_dict);
    WITH_OWNER_END();
}

/* Lifecycle callbacks forwarded to Python.
 *
 * open62541 supports three lifecycle hooks on UA_Client_Subscriptions_create_async:
 *   1) An async-create callback fired when the server's CreateSubscription
 *      response arrives (we always set this to drive the ServiceFuture, and
 *      additionally call a user-supplied Python callback if provided).
 *   2) A status-change callback fired on UA_StatusChangeNotification publishes.
 *   3) A delete callback fired exactly once when the internal subscription is
 *      torn down (explicit DeleteSubscription, session close, or disconnect).
 *
 * All state for a subscription lives in a single heap-allocated bundle that is
 * used as both `userdata` for the create callback and `subscriptionContext`
 * for the status/delete callbacks.  The status and delete C trampolines are
 * always registered; they early-return when the corresponding Python callable
 * is NULL.  The bundle is freed inside the delete callback because open62541
 * guarantees that callback fires once on any teardown path — with one
 * exception: if the server rejects the create request, deleteCallback is not
 * invoked, so createCallback frees the bundle in that path. */
typedef struct {
    ServiceFuture *sf;          /* consumed by createCallback */
    PyObject *created_cb;       /* Python callable or NULL; released by createCallback */
    PyObject *status_change_cb; /* Python callable or NULL */
    PyObject *deleted_cb;       /* Python callable or NULL */
} SubscriptionBundle;

static void
subscriptionBundle_free(SubscriptionBundle *bundle) {
    if (!bundle)
        return;
    Py_XDECREF(bundle->created_cb);
    Py_XDECREF(bundle->status_change_cb);
    Py_XDECREF(bundle->deleted_cb);
    UA_free(bundle);
}

/* Called when the server publishes a StatusChangeNotification. */
static void
pySubscription_statusChangeCallback(UA_Client *cClient, UA_UInt32 subId,
                                    void *subContext,
                                    UA_StatusChangeNotification *notification) {
    WITH_OWNER(cClient);
    (void)cClient;
    SubscriptionBundle *bundle = (SubscriptionBundle *)subContext;
    if (!bundle || !bundle->status_change_cb)
        return;
    PyObject *pySubId = PyLong_FromUnsignedLong(subId);
    if (!pySubId) { PyErr_Clear(); return; }
    PyObject *pyNotif = UA2PY(notification, &UA_TYPES[UA_TYPES_STATUSCHANGENOTIFICATION]);
    if (!pyNotif) { Py_DECREF(pySubId); PyErr_Clear(); return; }
    PyObject *result = PyObject_CallFunctionObjArgs(bundle->status_change_cb,
                                                    pySubId, pyNotif, NULL);
    Py_DECREF(pySubId);
    Py_DECREF(pyNotif);
    if (!result) {
        PyErr_Print();
        PyErr_Clear();
    } else {
        Py_DECREF(result);
    }
    WITH_OWNER_END();
}

/* Called exactly once when the internal UA_Client_Subscription is destroyed.
 * Owns the bundle lifetime. */
static void
pySubscription_deleteCallback(UA_Client *cClient, UA_UInt32 subId,
                              void *subContext) {
    WITH_OWNER(cClient);
    SubscriptionBundle *bundle = (SubscriptionBundle *)subContext;
    if (!bundle)
        return;
    if (bundle->deleted_cb) {
        UA_ClientConfig *config = UA_Client_getConfig(cClient);
        /* During teardown clientContext is NULL — avoid calling into Python
         * from tp_dealloc/GC (see asyncServiceCallback for the same guard). */
        if (config->clientContext) {
            PyObject *pySubId = PyLong_FromUnsignedLong(subId);
            if (pySubId) {
                PyObject *result = PyObject_CallOneArg(bundle->deleted_cb, pySubId);
                Py_DECREF(pySubId);
                if (!result) {
                    PyErr_Print();
                    PyErr_Clear();
                } else {
                    Py_DECREF(result);
                }
            } else {
                PyErr_Clear();
            }
        }
    }
    subscriptionBundle_free(bundle);
    WITH_OWNER_END();
}

/* Async create-response handler.  Resolves the ServiceFuture (via
 * asyncServiceCallback) and additionally invokes a user-supplied
 * on_created callback. */
static void
pySubscription_createCallback(UA_Client *cClient, void *userdata,
                              UA_UInt32 requestId,
                              UA_CreateSubscriptionResponse *response) {
    WITH_OWNER(cClient);
    SubscriptionBundle *bundle = (SubscriptionBundle *)userdata;
    UA_ClientConfig *config = UA_Client_getConfig(cClient);
    int clientAlive = (config->clientContext != NULL);
    int createFailed = (response &&
        response->responseHeader.serviceResult != UA_STATUSCODE_GOOD);

    /* Always resolve the future (this consumes bundle->sf). */
    asyncServiceCallback(cClient, bundle->sf, requestId, response);
    bundle->sf = NULL;

    /* Invoke the user's on_created callback if supplied. */
    if (clientAlive && bundle->created_cb && response) {
        PyObject *pyResp = UA2PY(response, &UA_TYPES[UA_TYPES_CREATESUBSCRIPTIONRESPONSE]);
        if (pyResp) {
            PyObject *result = PyObject_CallOneArg(bundle->created_cb, pyResp);
            Py_DECREF(pyResp);
            if (!result) {
                PyErr_Print();
                PyErr_Clear();
            } else {
                Py_DECREF(result);
            }
        } else {
            PyErr_Clear();
        }
    }

    /* Drop the create callback ref now — it's no longer needed. */
    Py_CLEAR(bundle->created_cb);

    /* If the server rejected the create request, open62541 will NOT call
     * deleteCallback later (the internal subscription is freed immediately in
     * Subscriptions_create_handler) — so release the bundle here. */
    if (createFailed)
        subscriptionBundle_free(bundle);
    WITH_OWNER_END();
}

PyObject *
pyClient_subscriptions_create(PyObject *self, PyObject *args) {
    PyObject *request_obj;
    PyObject *created_cb = Py_None;
    PyObject *status_change_cb = Py_None;
    PyObject *deleted_cb = Py_None;
    if (!PyArg_ParseTuple(args, "O|OOO:subscriptions_create",
                          &request_obj, &created_cb,
                          &status_change_cb, &deleted_cb))
        return NULL;

    /* Validate optional callbacks. */
    PyObject *cb_args[3] = { created_cb, status_change_cb, deleted_cb };
    const char *cb_names[3] = { "on_created", "on_status_change", "on_deleted" };
    for (int i = 0; i < 3; i++) {
        if (cb_args[i] != Py_None && !PyCallable_Check(cb_args[i])) {
            PyErr_Format(PyExc_TypeError,
                         "%s must be callable or None", cb_names[i]);
            return NULL;
        }
    }

    UA_CreateSubscriptionRequest request;
    PyObject *res = PY2UA(request_obj, &request,
                          &UA_TYPES[UA_TYPES_CREATESUBSCRIPTIONREQUEST]);
    if (!res)
        return NULL;

    UA_Client *client = ((PyClient*)self)->client;
    ServiceFuture *sf = createServiceFuture(
        client, &UA_TYPES[UA_TYPES_CREATESUBSCRIPTIONRESPONSE], NULL);
    if (!sf) {
        UA_CreateSubscriptionRequest_clear(&request);
        return NULL;
    }

    SubscriptionBundle *bundle = (SubscriptionBundle *)UA_calloc(
        1, sizeof(SubscriptionBundle));
    if (!bundle) {
        UA_CreateSubscriptionRequest_clear(&request);
        Py_DECREF(sf->future);
        UA_free(sf);
        PyErr_NoMemory();
        return NULL;
    }
    bundle->sf = sf;
    if (created_cb != Py_None) {
        Py_INCREF(created_cb);
        bundle->created_cb = created_cb;
    }
    if (status_change_cb != Py_None) {
        Py_INCREF(status_change_cb);
        bundle->status_change_cb = status_change_cb;
    }
    if (deleted_cb != Py_None) {
        Py_INCREF(deleted_cb);
        bundle->deleted_cb = deleted_cb;
    }

    UA_StatusCode retval = UA_Client_Subscriptions_create_async(
        client, request,
        bundle,
        pySubscription_statusChangeCallback,
        pySubscription_deleteCallback,
        (UA_ClientAsyncCreateSubscriptionCallback)pySubscription_createCallback,
        bundle, &sf->requestId);
    UA_CreateSubscriptionRequest_clear(&request);
    if (retval != UA_STATUSCODE_GOOD) {
        Py_DECREF(sf->future);
        UA_free(sf);
        subscriptionBundle_free(bundle);
        PyErr_SetString(PyExc_RuntimeError,
                        "Failed to create subscription async request");
        return NULL;
    }
    return sf->future;
}

// Implementation of UA_Client_Subscriptions_delete functionality
PyObject *
pyClient_subscriptions_delete(PyObject *self, PyObject *args) {
    PyObject *request_obj;
    if (!PyArg_ParseTuple(args, "O:subscriptions_delete", &request_obj))
        return NULL;

    UA_DeleteSubscriptionsRequest request;
    PyObject *res = PY2UA(request_obj, &request, &UA_TYPES[UA_TYPES_DELETESUBSCRIPTIONSREQUEST]);
    if (!res)
        return NULL;

    UA_Client *client = ((PyClient*)self)->client;
    ServiceFuture *sf = createServiceFuture(client, &UA_TYPES[UA_TYPES_DELETESUBSCRIPTIONSRESPONSE], NULL);
    if (!sf) {
        UA_DeleteSubscriptionsRequest_clear(&request);
        return NULL;
    }

    UA_StatusCode retval = UA_Client_Subscriptions_delete_async(
        client, request, (UA_ClientAsyncDeleteSubscriptionsCallback)asyncServiceCallback, sf, &sf->requestId);
    UA_DeleteSubscriptionsRequest_clear(&request);
    if (retval != UA_STATUSCODE_GOOD) {
        Py_DECREF(sf->future);
        UA_free(sf);
        PyErr_SetString(PyExc_RuntimeError, "Failed to delete subscription async request");
        return NULL;
    }
    return sf->future;
}


PyObject *
pyClient_subscriptions_modify(PyObject *self, PyObject *args) {
    PyObject *request_obj;
    if (!PyArg_ParseTuple(args, "O:subscriptions_modify", &request_obj))
        return NULL;

    UA_ModifySubscriptionRequest request;
    PyObject *res = PY2UA(request_obj, &request, &UA_TYPES[UA_TYPES_MODIFYSUBSCRIPTIONREQUEST]);
    if (!res)
        return NULL;

    UA_Client *client = ((PyClient*)self)->client;
    ServiceFuture *sf = createServiceFuture(client, &UA_TYPES[UA_TYPES_MODIFYSUBSCRIPTIONRESPONSE], NULL);
    if (!sf) {
        UA_ModifySubscriptionRequest_clear(&request);
        return NULL;
    }

    UA_StatusCode retval = UA_Client_Subscriptions_modify_async(
        client, request, (UA_ClientAsyncModifySubscriptionCallback)asyncServiceCallback, sf, &sf->requestId);
    UA_ModifySubscriptionRequest_clear(&request);
    if (retval != UA_STATUSCODE_GOOD) {
        Py_DECREF(sf->future);
        UA_free(sf);
        PyErr_SetString(PyExc_RuntimeError, "Failed to modify subscription async request");
        return NULL;
    }
    return sf->future;
}

PyObject *
pyClient_subscriptions_setPublishingMode(PyObject *self, PyObject *args) {
    return serviceCallAsync(self, args,
                            &UA_TYPES[UA_TYPES_SETPUBLISHINGMODEREQUEST],
                            &UA_TYPES[UA_TYPES_SETPUBLISHINGMODERESPONSE]);
}


PyObject *
pyClient_monitoredItems_createDataChange(PyObject *self, PyObject *args);
PyObject *
pyClient_monitoredItems_createEvent(PyObject *self, PyObject *args);

/* Wrapper passed as userdata to UA_Client_MonitoredItems_createXxx_async to
 * forward the create response to (a) the ServiceFuture and (b) an optional
 * user on_created callback. */
typedef struct {
    ServiceFuture *sf;
    PyObject *created_cb; /* Python callable or NULL */
} MonitoredItemsCreateWrapper;

static void
pyMonitoredItems_createCallback(UA_Client *cClient, void *userdata,
                                UA_UInt32 requestId,
                                UA_CreateMonitoredItemsResponse *response) {
    WITH_OWNER(cClient);
    MonitoredItemsCreateWrapper *w = (MonitoredItemsCreateWrapper *)userdata;
    UA_ClientConfig *config = UA_Client_getConfig(cClient);
    int clientAlive = (config->clientContext != NULL);

    /* Always resolve the future (this consumes w->sf). */
    asyncServiceCallback(cClient, w->sf, requestId, response);

    /* Then invoke the user's on_created callback if supplied. */
    if (clientAlive && w->created_cb && response) {
        PyObject *pyResp = UA2PY(response,
                                 &UA_TYPES[UA_TYPES_CREATEMONITOREDITEMSRESPONSE]);
        if (pyResp) {
            PyObject *result = PyObject_CallOneArg(w->created_cb, pyResp);
            Py_DECREF(pyResp);
            if (!result) {
                PyErr_Print();
                PyErr_Clear();
            } else {
                Py_DECREF(result);
            }
        } else {
            PyErr_Clear();
        }
    }

    Py_XDECREF(w->created_cb);
    UA_free(w);
    WITH_OWNER_END();
}

/* Shared implementation for the datachange / event create paths.  They differ
 * only in the per-item notification trampoline and which open62541 entry-point
 * is invoked. */
typedef UA_StatusCode (*MonitoredItemsCreateAsyncFn)(
    UA_Client *client, const UA_CreateMonitoredItemsRequest request,
    void **contexts, void *notificationCallbacks,
    UA_Client_DeleteMonitoredItemCallback *deleteCallbacks,
    UA_ClientAsyncCreateMonitoredItemsCallback createCallback,
    void *userdata, UA_UInt32 *requestId);

static PyObject *
pyClient_monitoredItems_createCommon(PyObject *self, PyObject *args,
                                     const char *argspec,
                                     void *notification_fn,
                                     MonitoredItemsCreateAsyncFn create_async,
                                     const char *err_msg) {
    PyObject *request_obj;
    PyObject *notification_cb_obj;
    PyObject *created_cb = Py_None;
    PyObject *deleted_cb = Py_None;
    if (!PyArg_ParseTuple(args, argspec, &request_obj, &notification_cb_obj,
                          &created_cb, &deleted_cb))
        return NULL;

    if (!PyCallable_Check(notification_cb_obj)) {
        PyErr_SetString(PyExc_TypeError, "callback must be callable");
        return NULL;
    }
    if (created_cb != Py_None && !PyCallable_Check(created_cb)) {
        PyErr_SetString(PyExc_TypeError, "on_created must be callable or None");
        return NULL;
    }
    if (deleted_cb != Py_None && !PyCallable_Check(deleted_cb)) {
        PyErr_SetString(PyExc_TypeError, "on_deleted must be callable or None");
        return NULL;
    }

    UA_CreateMonitoredItemsRequest request;
    PyObject *res = PY2UA(request_obj, &request,
                          &UA_TYPES[UA_TYPES_CREATEMONITOREDITEMSREQUEST]);
    if (!res)
        return NULL;

    size_t numItems = request.itemsToCreateSize;
    void **contexts = NULL;
    void **callbacks = NULL;
    UA_Client_DeleteMonitoredItemCallback *deleteCallbacks = NULL;
    if (monitoredItem_setupCallbacks(numItems, notification_cb_obj,
                                     deleted_cb == Py_None ? NULL : deleted_cb,
                                     notification_fn,
                                     &callbacks, &contexts, &deleteCallbacks) < 0) {
        UA_CreateMonitoredItemsRequest_clear(&request);
        return NULL;
    }

    UA_Client *client = ((PyClient*)self)->client;
    ServiceFuture *sf = createServiceFuture(
        client, &UA_TYPES[UA_TYPES_CREATEMONITOREDITEMSRESPONSE], NULL);
    if (!sf) {
        for (size_t i = 0; i < numItems; i++)
            monitoredItemBundle_free((MonitoredItemBundle *)contexts[i]);
        UA_free(callbacks);
        UA_free(contexts);
        UA_free(deleteCallbacks);
        UA_CreateMonitoredItemsRequest_clear(&request);
        return NULL;
    }

    MonitoredItemsCreateWrapper *w = (MonitoredItemsCreateWrapper *)UA_calloc(
        1, sizeof(MonitoredItemsCreateWrapper));
    if (!w) {
        for (size_t i = 0; i < numItems; i++)
            monitoredItemBundle_free((MonitoredItemBundle *)contexts[i]);
        UA_free(callbacks);
        UA_free(contexts);
        UA_free(deleteCallbacks);
        Py_DECREF(sf->future);
        UA_free(sf);
        UA_CreateMonitoredItemsRequest_clear(&request);
        PyErr_NoMemory();
        return NULL;
    }
    w->sf = sf;
    if (created_cb != Py_None) {
        Py_INCREF(created_cb);
        w->created_cb = created_cb;
    }

    UA_StatusCode retval = create_async(
        client, request, contexts, callbacks, deleteCallbacks,
        (UA_ClientAsyncCreateMonitoredItemsCallback)pyMonitoredItems_createCallback,
        w, &sf->requestId);
    UA_free(callbacks);
    UA_free(contexts);
    UA_free(deleteCallbacks);
    UA_CreateMonitoredItemsRequest_clear(&request);
    if (retval != UA_STATUSCODE_GOOD) {
        /* On failure, open62541 internally calls each per-item deleteCallback
         * (see Client_MonitoredItems_createAsync failure path), which frees the
         * bundles. We only need to release the create-wrapper and future. */
        Py_DECREF(sf->future);
        UA_free(sf);
        Py_XDECREF(w->created_cb);
        UA_free(w);
        PyErr_SetString(PyExc_RuntimeError, err_msg);
        return NULL;
    }
    return sf->future;
}

/* Trampoline wrappers around the typed open62541 entry points so they match
 * the MonitoredItemsCreateAsyncFn signature (void* for the callbacks array). */
static UA_StatusCode
monitoredItems_createDataChanges_async_thunk(
    UA_Client *client, const UA_CreateMonitoredItemsRequest request,
    void **contexts, void *notificationCallbacks,
    UA_Client_DeleteMonitoredItemCallback *deleteCallbacks,
    UA_ClientAsyncCreateMonitoredItemsCallback createCallback,
    void *userdata, UA_UInt32 *requestId) {
    return UA_Client_MonitoredItems_createDataChanges_async(
        client, request, contexts,
        (UA_Client_DataChangeNotificationCallback *)notificationCallbacks,
        deleteCallbacks, createCallback, userdata, requestId);
}

static UA_StatusCode
monitoredItems_createEvents_async_thunk(
    UA_Client *client, const UA_CreateMonitoredItemsRequest request,
    void **contexts, void *notificationCallbacks,
    UA_Client_DeleteMonitoredItemCallback *deleteCallbacks,
    UA_ClientAsyncCreateMonitoredItemsCallback createCallback,
    void *userdata, UA_UInt32 *requestId) {
    return UA_Client_MonitoredItems_createEvents_async(
        client, request, contexts,
        (UA_Client_EventNotificationCallback *)notificationCallbacks,
        deleteCallbacks, createCallback, userdata, requestId);
}

PyObject *
pyClient_monitoredItems_createDataChange(PyObject *self, PyObject *args) {
    return pyClient_monitoredItems_createCommon(
        self, args, "OO|OO:monitoredItems_createDataChange",
        (void *)dataChangeNotificationCallback,
        monitoredItems_createDataChanges_async_thunk,
        "Failed to create monitored items async request");
}

PyObject *
pyClient_monitoredItems_createEvent(PyObject *self, PyObject *args) {
    return pyClient_monitoredItems_createCommon(
        self, args, "OO|OO:monitoredItems_createEvent",
        (void *)eventNotificationCallback,
        monitoredItems_createEvents_async_thunk,
        "Failed to create event monitored items async request");
}

PyObject *
pyClient_monitoredItems_delete(PyObject *self, PyObject *args) {
    PyObject *request_obj;
    if (!PyArg_ParseTuple(args, "O:monitoredItems_delete", &request_obj))
        return NULL;

    UA_DeleteMonitoredItemsRequest request;
    PyObject *res = PY2UA(request_obj, &request, &UA_TYPES[UA_TYPES_DELETEMONITOREDITEMSREQUEST]);
    if (!res)
        return NULL;

    UA_Client *client = ((PyClient*)self)->client;
    ServiceFuture *sf = createServiceFuture(client, &UA_TYPES[UA_TYPES_DELETEMONITOREDITEMSRESPONSE], NULL);
    if (!sf) {
        UA_DeleteMonitoredItemsRequest_clear(&request);
        return NULL;
    }

    UA_StatusCode retval = UA_Client_MonitoredItems_delete_async(
        client, request,
        (UA_ClientAsyncDeleteMonitoredItemsCallback)asyncServiceCallback,
        sf, &sf->requestId);
    UA_DeleteMonitoredItemsRequest_clear(&request);
    if (retval != UA_STATUSCODE_GOOD) {
        Py_DECREF(sf->future);
        UA_free(sf);
        PyErr_SetString(PyExc_RuntimeError, "Failed to delete monitored items async request");
        return NULL;
    }
    return sf->future;
}

PyObject *
pyClient_monitoredItems_modify(PyObject *self, PyObject *args) {
    PyObject *request_obj;
    if (!PyArg_ParseTuple(args, "O:monitoredItems_modify", &request_obj))
        return NULL;

    UA_ModifyMonitoredItemsRequest request;
    PyObject *res = PY2UA(request_obj, &request, &UA_TYPES[UA_TYPES_MODIFYMONITOREDITEMSREQUEST]);
    if (!res)
        return NULL;

    UA_Client *client = ((PyClient*)self)->client;
    ServiceFuture *sf = createServiceFuture(client, &UA_TYPES[UA_TYPES_MODIFYMONITOREDITEMSRESPONSE], NULL);
    if (!sf) {
        UA_ModifyMonitoredItemsRequest_clear(&request);
        return NULL;
    }

    UA_StatusCode retval = UA_Client_MonitoredItems_modify_async(
        client, request,
        (UA_ClientAsyncModifyMonitoredItemsCallback)asyncServiceCallback,
        sf, &sf->requestId);
    UA_ModifyMonitoredItemsRequest_clear(&request);
    if (retval != UA_STATUSCODE_GOOD) {
        Py_DECREF(sf->future);
        UA_free(sf);
        PyErr_SetString(PyExc_RuntimeError, "Failed to modify monitored items async request");
        return NULL;
    }
    return sf->future;
}

PyObject *
pyClient_monitoredItems_setMonitoringMode(PyObject *self, PyObject *args) {
    PyObject *request_obj;
    if (!PyArg_ParseTuple(args, "O:monitoredItems_setMonitoringMode", &request_obj))
        return NULL;

    UA_SetMonitoringModeRequest request;
    PyObject *res = PY2UA(request_obj, &request, &UA_TYPES[UA_TYPES_SETMONITORINGMODEREQUEST]);
    if (!res)
        return NULL;

    UA_Client *client = ((PyClient*)self)->client;
    ServiceFuture *sf = createServiceFuture(client, &UA_TYPES[UA_TYPES_SETMONITORINGMODERESPONSE], NULL);
    if (!sf) {
        UA_SetMonitoringModeRequest_clear(&request);
        return NULL;
    }

    UA_StatusCode retval = UA_Client_MonitoredItems_setMonitoringMode_async(
        client, request,
        (UA_ClientAsyncSetMonitoringModeCallback)asyncServiceCallback,
        sf, &sf->requestId);
    UA_SetMonitoringModeRequest_clear(&request);
    if (retval != UA_STATUSCODE_GOOD) {
        Py_DECREF(sf->future);
        UA_free(sf);
        PyErr_SetString(PyExc_RuntimeError, "Failed to set monitoring mode async request");
        return NULL;
    }
    return sf->future;
}

PyObject *
pyClient_monitoredItems_setTriggering(PyObject *self, PyObject *args) {
    PyObject *request_obj;
    if (!PyArg_ParseTuple(args, "O:monitoredItems_setTriggering", &request_obj))
        return NULL;

    UA_SetTriggeringRequest request;
    PyObject *res = PY2UA(request_obj, &request, &UA_TYPES[UA_TYPES_SETTRIGGERINGREQUEST]);
    if (!res)
        return NULL;

    UA_Client *client = ((PyClient*)self)->client;
    ServiceFuture *sf = createServiceFuture(client, &UA_TYPES[UA_TYPES_SETTRIGGERINGRESPONSE], NULL);
    if (!sf) {
        UA_SetTriggeringRequest_clear(&request);
        return NULL;
    }

    UA_StatusCode retval = UA_Client_MonitoredItems_setTriggering_async(
        client, request,
        (UA_ClientAsyncSetTriggeringCallback)asyncServiceCallback,
        sf, &sf->requestId);
    UA_SetTriggeringRequest_clear(&request);
    if (retval != UA_STATUSCODE_GOOD) {
        Py_DECREF(sf->future);
        UA_free(sf);
        PyErr_SetString(PyExc_RuntimeError, "Failed to set triggering async request");
        return NULL;
    }
    return sf->future;
}
