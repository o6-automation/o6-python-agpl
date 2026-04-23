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
#include <open62541/client_subscriptions.h>

// Called by the library when a monitored item is destroyed — releases the Python callback ref
static void
deleteMonitoredItemCallback(UA_Client *client, UA_UInt32 subId, void *subContext, UA_UInt32 monId, void *context) {
    (void)client; (void)subId; (void)subContext; (void)monId;
    Py_XDECREF((PyObject *)context);
}

// Allocates and fills the callbacks, contexts, and deleteCallbacks arrays.
// Returns 0 on success, -1 on OOM (PyErr set). Caller must UA_free() all three arrays.
static int
monitoredItem_setupCallbacks(size_t num_items, 
                             PyObject *python_notification_callback,
                             void *notification_fn,
                             void ***notification_callbacks_out,
                             void ***contexts_out,
                             UA_Client_DeleteMonitoredItemCallback **delete_callbacks_out) {

    void **callbacks = UA_malloc(num_items * sizeof(void *));
    void **contexts = UA_malloc(num_items * sizeof(void *));
    UA_Client_DeleteMonitoredItemCallback *deleteCallbacks = UA_malloc(num_items * sizeof(UA_Client_DeleteMonitoredItemCallback));

    if (!callbacks || !contexts || !deleteCallbacks) {
        UA_free(callbacks);
        UA_free(contexts);
        UA_free(deleteCallbacks);
        PyErr_NoMemory();
        return -1;
    }

    for (size_t i = 0; i < num_items; i++) {
        callbacks[i] = notification_fn;
        Py_INCREF(python_notification_callback);
        contexts[i] = python_notification_callback;
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
    (void)client; (void)subId; (void)subContext; (void)monId;
    PyObject *callback = (PyObject *)context;
    if (!callback)
        return;

    // Convert UA_DataValue to Python
    PyObject *py_value = UA2PY(&value->value, &UA_TYPES[UA_TYPES_VARIANT]);
    if (!py_value)
        return;

    // Call the Python callback
    PyObject *result = PyObject_CallOneArg(callback, py_value);
    if (!result) {
        PyErr_Print();
    } else {
        Py_DECREF(result);
    }
    Py_DECREF(py_value);
}

// Event notification callback
static void
eventNotificationCallback(UA_Client *client, UA_UInt32 subId, void *subContext, UA_UInt32 monId, void *context, const UA_KeyValueMap eventFields) {
    (void)client; (void)subId; (void)subContext; (void)monId;
    PyObject *callback = (PyObject *)context;
    if (!callback)
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
    PyObject *result = PyObject_CallOneArg(callback, event_dict);
    if (!result) {
        PyErr_Print();
    } else {
        Py_DECREF(result);
    }
    Py_DECREF(event_dict);
}

PyObject *
pyClient_subscriptions_create(PyObject *self, PyObject *args) {
    PyObject *request_obj;
    if (!PyArg_ParseTuple(args, "O:subscriptions_create", &request_obj))
        return NULL;

    UA_CreateSubscriptionRequest request;
    PyObject *res = PY2UA(request_obj, &request, &UA_TYPES[UA_TYPES_CREATESUBSCRIPTIONREQUEST]);
    if (!res)
        return NULL;

    UA_Client *client = ((PyClient*)self)->client;
    ServiceFuture *sf = createServiceFuture(client, &UA_TYPES[UA_TYPES_CREATESUBSCRIPTIONRESPONSE], NULL);
    if (!sf) {
        UA_CreateSubscriptionRequest_clear(&request);
        return NULL;
    }

    UA_StatusCode retval = UA_Client_Subscriptions_create_async(
        client, request, NULL, NULL, NULL,
        (UA_ClientAsyncCreateSubscriptionCallback)asyncServiceCallback, sf, &sf->requestId);
    UA_CreateSubscriptionRequest_clear(&request);
    if (retval != UA_STATUSCODE_GOOD) {
        Py_DECREF(sf->future);
        UA_free(sf);
        PyErr_SetString(PyExc_RuntimeError, "Failed to create subscription async request");
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
pyClient_monitoredItems_createDataChange(PyObject *self, PyObject *args) {
    PyObject *request_obj, *python_notification_callback_obj;
    if (!PyArg_ParseTuple(args, "OO:monitoredItems_createDataChange",
                          &request_obj, &python_notification_callback_obj))
        return NULL;

    // Convert request
    UA_CreateMonitoredItemsRequest request;
    PyObject *res = PY2UA(request_obj, &request, &UA_TYPES[UA_TYPES_CREATEMONITOREDITEMSREQUEST]);
    if (!res)
        return NULL;

    // Check if callback is callable
    if (!PyCallable_Check(python_notification_callback_obj)) {
        UA_CreateMonitoredItemsRequest_clear(&request);
        PyErr_SetString(PyExc_TypeError, "callback must be callable");
        return NULL;
    }

    size_t numItems = request.itemsToCreateSize;
    void **contexts;
    void **callbacks;
    UA_Client_DeleteMonitoredItemCallback *deleteCallbacks;
    if (monitoredItem_setupCallbacks(numItems, 
                                     python_notification_callback_obj,
                                     (void *)dataChangeNotificationCallback,
                                     &callbacks, &contexts, &deleteCallbacks) < 0) {
        UA_CreateMonitoredItemsRequest_clear(&request);
        return NULL;
    }

    UA_Client *client = ((PyClient*)self)->client;
    ServiceFuture *sf = createServiceFuture(client, &UA_TYPES[UA_TYPES_CREATEMONITOREDITEMSRESPONSE], NULL);
    if (!sf) {
        for (size_t i = 0; i < numItems; i++)
            Py_DECREF(python_notification_callback_obj);
        UA_free(callbacks);
        UA_free(contexts);
        UA_free(deleteCallbacks);
        UA_CreateMonitoredItemsRequest_clear(&request);
        return NULL;
    }

    UA_StatusCode retval = UA_Client_MonitoredItems_createDataChanges_async(
        client, request, contexts,
        (UA_Client_DataChangeNotificationCallback *)callbacks, deleteCallbacks,
        (UA_ClientAsyncCreateMonitoredItemsCallback)asyncServiceCallback, sf, &sf->requestId);
    UA_free(callbacks);
    UA_free(contexts);
    UA_free(deleteCallbacks);
    UA_CreateMonitoredItemsRequest_clear(&request);
    if (retval != UA_STATUSCODE_GOOD) {
        // Library did not take ownership — release refs we added
        for (size_t i = 0; i < numItems; i++)
            Py_DECREF(python_notification_callback_obj);
        Py_DECREF(sf->future);
        UA_free(sf);
        PyErr_SetString(PyExc_RuntimeError, "Failed to create monitored items async request");
        return NULL;
    }
    return sf->future;
}

PyObject *
pyClient_monitoredItems_createEvent(PyObject *self, PyObject *args) {
    PyObject *request_obj, *python_notification_callback_obj;
    if (!PyArg_ParseTuple(args, "OO:monitoredItems_createEvent",
                          &request_obj, &python_notification_callback_obj))
        return NULL;

    // Convert request
    UA_CreateMonitoredItemsRequest request;
    PyObject *res = PY2UA(request_obj, &request, &UA_TYPES[UA_TYPES_CREATEMONITOREDITEMSREQUEST]);
    if (!res)
        return NULL;

    // Check if callback is callable
    if (!PyCallable_Check(python_notification_callback_obj)) {
        UA_CreateMonitoredItemsRequest_clear(&request);
        PyErr_SetString(PyExc_TypeError, "callback must be callable");
        return NULL;
    }

    size_t numItems = request.itemsToCreateSize;
    void **contexts;
    void **callbacks;
    UA_Client_DeleteMonitoredItemCallback *deleteCallbacks;
    if (monitoredItem_setupCallbacks(numItems, python_notification_callback_obj,
                                     (void *)eventNotificationCallback,
                                     &callbacks, &contexts, &deleteCallbacks) < 0) {
        UA_CreateMonitoredItemsRequest_clear(&request);
        return NULL;
    }

    UA_Client *client = ((PyClient*)self)->client;
    ServiceFuture *sf = createServiceFuture(client, &UA_TYPES[UA_TYPES_CREATEMONITOREDITEMSRESPONSE], NULL);
    if (!sf) {
        for (size_t i = 0; i < numItems; i++)
            Py_DECREF(python_notification_callback_obj);
        UA_free(callbacks);
        UA_free(contexts);
        UA_free(deleteCallbacks);
        UA_CreateMonitoredItemsRequest_clear(&request);
        return NULL;
    }

    UA_StatusCode retval = UA_Client_MonitoredItems_createEvents_async(
        client, request, contexts,
        (UA_Client_EventNotificationCallback *)callbacks, deleteCallbacks,
        (UA_ClientAsyncCreateMonitoredItemsCallback)asyncServiceCallback, sf, &sf->requestId);
    UA_free(callbacks);
    UA_free(contexts);
    UA_free(deleteCallbacks);
    UA_CreateMonitoredItemsRequest_clear(&request);
    if (retval != UA_STATUSCODE_GOOD) {
        // Library did not take ownership — release refs we added
        for (size_t i = 0; i < numItems; i++)
            Py_DECREF(python_notification_callback_obj);
        Py_DECREF(sf->future);
        UA_free(sf);
        PyErr_SetString(PyExc_RuntimeError, "Failed to create event monitored items async request");
        return NULL;
    }
    return sf->future;
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
