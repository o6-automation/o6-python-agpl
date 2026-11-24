/* Copyright 2026 (c) o6 Automation GmbH (Author: Andreas Ebner) */
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

#include "client.h"
#include "../ua_extension_namespacemapping.h"
#include "../utils.h"
#include "../types_internal.h"
#include "../datatypes.h"
#include "../services_subscriptions.h"
// Needed to read haveNamespaces so we resolve connectFuture only after
// open62541's async namespace-array read has completed.
#include "ua_client_internal.h"

static PyObject *
pyClient_get_state(PyClient *self, PyObject *Py_UNUSED(ignored)) {
    O6_REQUIRE_LOOP_THREAD(pyClient_eventLoop(self), NULL);
    const UA_NamespaceMapping *nsMapping = &self->nsMapPy2UA;
    UA_StatusCode connectStatus = UA_STATUSCODE_GOOD;
    UA_SecureChannelState cState = 0;
    UA_SessionState sState = 0;

    if(!self->client)
        return Py_BuildValue("(iii)", 0, 0, 0);

    UA_Client_getState(self->client, &cState, &sState, &connectStatus);
    PyObject *a = PyLong_FromLong(cState);
    PyObject *b = PyLong_FromLong(sState);
    PyObject *c = UA2PY(&connectStatus, &UA_TYPES[UA_TYPES_STATUSCODE], nsMapping);

    if (!a || !b || !c) {
        Py_XDECREF(a);
        Py_XDECREF(b);
        Py_XDECREF(c);
        return NULL;
    }

    PyObject *tuple = PyTuple_Pack(3, a, b, c);
    Py_DECREF(a);
    Py_DECREF(b);
    Py_DECREF(c);
    return tuple;
}

/* Stop the timers of a connect that has ended */
static void
stopConnectTimers(PyClient *client) {
    if (client->connectPollId) {
        UA_Client_removeCallback(client->client, client->connectPollId);
        client->connectPollId = 0;
    }
    if (client->connectTimeoutId) {
        UA_Client_removeCallback(client->client, client->connectTimeoutId);
        client->connectTimeoutId = 0;
    }
    client->connectTimedOut = false;
}

static void
failConnectFuture(PyClient *client, UA_StatusCode connectStatus) {
    stopConnectTimers(client);
    /* Create exception object without polluting the exception state */
    PyObject *code = PyLong_FromUnsignedLong(connectStatus);
    PyObject *exc = code ? PyObject_CallOneArg(pyExc_StatusCode, code) : NULL;
    Py_XDECREF(code);
    if (exc) {
        PyObject *res = PyObject_CallMethod(client->connectFuture,
                                            "set_exception", "O", exc);
        Py_XDECREF(res);
        Py_DECREF(exc);
    }
    if (PyErr_Occurred())
        PyErr_Clear(); /* suppress InvalidStateError if future already resolved */
    Py_CLEAR(client->connectFuture);
}

static void
resolveConnectFuture(PyClient *client, UA_StatusCode connectStatus) {
    stopConnectTimers(client);
    PyObject *result = UA2PY(&connectStatus, &UA_TYPES[UA_TYPES_STATUSCODE],
                             &client->nsMapPy2UA);
    PyObject *res = result ? PyObject_CallMethod(client->connectFuture,
                                                 "set_result", "O", result) : NULL;
    Py_XDECREF(result);
    Py_XDECREF(res);
    if (PyErr_Occurred())
        PyErr_Clear();
    Py_CLEAR(client->connectFuture);
}

/* A SecureChannel-only connect is complete once the channel of the selected
 * endpoint is open. When the endpoint selected by GetEndpoints matches the
 * already open channel, no further state change follows. Poll until
 * open62541 considers the client fully connected. */
static void
connectPollCallback(UA_Client *cClient, void *data) {
    PyClient *client = (PyClient*)UA_Client_getConfig(cClient)->clientContext;
    if (!client)
        return;
    if (!client->connectFuture) {
        stopConnectTimers(client);
        return;
    }
    lockClient(cClient);
    UA_StatusCode connectStatus = cClient->connectStatus;
    UA_Boolean connected = isFullyConnected(cClient);
    unlockClient(cClient);
    if (connectStatus != UA_STATUSCODE_GOOD)
        failConnectFuture(client, connectStatus);
    else if (connected)
        resolveConnectFuture(client, connectStatus);
}

/* open62541 bounds only a synchronous connect by config.timeout, and o6
 * connects asynchronously. Without this deadline, a connect to a peer that
 * never answers the Hello waits forever. Close the channel, and fail the
 * connect once the channel is closed. */
static void
connectTimeoutCallback(UA_Client *cClient, void *data) {
    PyClient *client = (PyClient*)UA_Client_getConfig(cClient)->clientContext;
    if (!client)
        return;
    client->connectTimeoutId = 0;
    if (!client->connectFuture)
        return;

    UA_LOG_ERROR(UA_Client_getConfig(cClient)->logging, UA_LOGCATEGORY_CLIENT,
                 "The connection has timed out before it could be fully opened");
    /* The pending connect keeps connectStatus GOOD. The disconnect changes
     * it, so the state callback follows and fails the connect once the
     * channel is closed. */
    client->connectTimedOut = true;
    UA_Client_disconnectSecureChannelAsync(cClient);
}

/* Fail a pending connect future and drop it. Leaves no error set, so the
 * disconnect proceeds. */
static void
abortConnect(PyClient *client) {
    if (!client->connectFuture)
        return;
    stopConnectTimers(client);
    PyObject *exc = PyObject_CallFunction(PyExc_RuntimeError, "s",
                                          "The client was disconnected before "
                                          "completely connecting");
    PyObject *res = exc ? PyObject_CallMethod(client->connectFuture,
                                              "set_exception", "O", exc) : NULL;
    Py_XDECREF(res);
    Py_XDECREF(exc);
    PyErr_Clear(); /* InvalidStateError if the future is done, e.g. cancelled */
    Py_CLEAR(client->connectFuture);
}

static void
clientStateCallback(UA_Client *cClient,
                    UA_SecureChannelState channelState,
                    UA_SessionState sessionState,
                    UA_StatusCode connectStatus) {

    UA_ClientConfig *config = UA_Client_getConfig(cClient);
    PyClient *client = (PyClient*)config->clientContext;
    const UA_NamespaceMapping *nsMapping = &client->nsMapPy2UA;
    if (client->connectFuture) {
        // The connect timed out. Fail it once the channel is closed.
        if (client->connectTimedOut) {
            if (channelState == UA_SECURECHANNELSTATE_CLOSED)
                failConnectFuture(client, UA_STATUSCODE_BADTIMEOUT);
        }

        // The connection was aborted
        else if (connectStatus != UA_STATUSCODE_GOOD) {
            failConnectFuture(client, connectStatus);
        }

        // The connection was successful
        else if (sessionState == UA_SESSIONSTATE_ACTIVATED && cClient->haveNamespaces) {
            resolveConnectFuture(client, connectStatus);
        }

        // SecureChannel-only connect (no session requested). The first open
        // channel can be the SecurityPolicy#None channel for GetEndpoints,
        // before the channel with the requested security is opened.
        else if (channelState == UA_SECURECHANNELSTATE_OPEN &&
                 config->noSession && cClient->haveNamespaces) {
            if (isFullyConnected(cClient)) {
                resolveConnectFuture(client, connectStatus);
            } else if (!client->connectPollId &&
                       UA_Client_addRepeatedCallback(
                           cClient, connectPollCallback, NULL, 10.0,
                           &client->connectPollId) != UA_STATUSCODE_GOOD) {
                client->connectPollId = 0;
                failConnectFuture(client, UA_STATUSCODE_BADINTERNALERROR);
            }
        }
    }

    if (client->disconnectFuture) {
        if (channelState == UA_SECURECHANNELSTATE_CLOSED) {
            PyObject *result = UA2PY(&connectStatus, &UA_TYPES[UA_TYPES_STATUSCODE], nsMapping);
            PyObject *res = PyObject_CallMethod(client->disconnectFuture,
                                                "set_result", "O", result);
            Py_XDECREF(result);
            Py_XDECREF(res);
            Py_DECREF(client->disconnectFuture);
            client->disconnectFuture = NULL;
        }
    }
}

/* Invoke a stored Python notification callable with (notification_type, payload_dict).
 * Errors are printed and cleared. */
static void
callNotificationCallback(PyObject *pycb, UA_ApplicationNotificationType type, const UA_KeyValueMap payload, const UA_NamespaceMapping *nsMapping) {
    PyObject *pyType = PyLong_FromLong((long)type);
    if (!pyType) {
        PyErr_Clear();
        return;
    }
    PyObject *pyPayload = keyValueMap_to_pydict(&payload, nsMapping);
    if (!pyPayload) {
        Py_DECREF(pyType);
        PyErr_Clear();
        return;
    }
    PyObject *result = PyObject_CallFunction(pycb, "OO", pyType, pyPayload);
    Py_XDECREF(result);
    Py_DECREF(pyType);
    Py_DECREF(pyPayload);
    if (PyErr_Occurred())
        PyErr_Clear();
}

static void
clientGlobalNotificationCallback(UA_Client *cClient, UA_ApplicationNotificationType type, const UA_KeyValueMap payload) {
    UA_ClientConfig *config = UA_Client_getConfig(cClient);
    PyClient *client = (PyClient *)config->clientContext;
    if (client->globalNotificationCallback)
        callNotificationCallback(client->globalNotificationCallback, type, payload, &client->nsMapPy2UA);
}

static void
clientLifecycleNotificationCallback(UA_Client *cClient, UA_ApplicationNotificationType type, const UA_KeyValueMap payload) {
    UA_ClientConfig *config = UA_Client_getConfig(cClient);
    PyClient *client = (PyClient *)config->clientContext;
    if (client->lifecycleNotificationCallback)
        callNotificationCallback(client->lifecycleNotificationCallback, type, payload, &client->nsMapPy2UA);
}

static void
clientServiceNotificationCallback(UA_Client *cClient, UA_ApplicationNotificationType type, const UA_KeyValueMap payload) {
    UA_ClientConfig *config = UA_Client_getConfig(cClient);
    PyClient *client = (PyClient *)config->clientContext;
    if (client->serviceNotificationCallback)
        callNotificationCallback(client->serviceNotificationCallback, type, payload, &client->nsMapPy2UA);
}

static void
clientInactivityCallback(UA_Client *cClient) {
    UA_ClientConfig *config = UA_Client_getConfig(cClient);
    PyClient *client = (PyClient *)config->clientContext;
    if (!client->inactivityCallback)
        return;
    PyObject *result = PyObject_CallNoArgs(client->inactivityCallback);
    Py_XDECREF(result);
    if (PyErr_Occurred())
        PyErr_Clear();
}

static void
clientSubscriptionInactivityCallback(UA_Client *cClient, UA_UInt32 subId, void *subContext) {
    UA_ClientConfig *config = UA_Client_getConfig(cClient);
    PyClient *client = (PyClient *)config->clientContext;
    if (!client->subscriptionInactivityCallback)
        return;
    PyObject *pySubId = PyLong_FromUnsignedLong(subId);
    if (!pySubId) { PyErr_Clear(); return; }
    PyObject *result = PyObject_CallOneArg(client->subscriptionInactivityCallback, pySubId);
    Py_XDECREF(result);
    Py_DECREF(pySubId);
    if (PyErr_Occurred())
        PyErr_Clear();
}

static PyObject *
pyClient_set_global_notification_callback(PyClient *self, PyObject *args) {
    O6_REQUIRE_LOOP_THREAD(pyClient_eventLoop(self), NULL);
    PyObject *callback;
    if (!PyArg_ParseTuple(args, "O", &callback))
        return NULL;
    if (callback != Py_None && !PyCallable_Check(callback)) {
        PyErr_SetString(PyExc_TypeError, "callback must be callable or None");
        return NULL;
    }
    if (!self->client) {
        PyErr_SetString(PyExc_RuntimeError, "Client not initialized");
        return NULL;
    }
    PyObject *old = self->globalNotificationCallback;
    if (callback == Py_None) {
        self->globalNotificationCallback = NULL;
        UA_Client_getConfig(self->client)->globalNotificationCallback = NULL;
    } else {
        Py_INCREF(callback);
        self->globalNotificationCallback = callback;
        UA_Client_getConfig(self->client)->globalNotificationCallback =
            clientGlobalNotificationCallback;
    }
    Py_XDECREF(old);
    Py_RETURN_NONE;
}

static PyObject *
pyClient_set_lifecycle_notification_callback(PyClient *self, PyObject *args) {
    O6_REQUIRE_LOOP_THREAD(pyClient_eventLoop(self), NULL);
    PyObject *callback;
    if (!PyArg_ParseTuple(args, "O", &callback))
        return NULL;
    if (callback != Py_None && !PyCallable_Check(callback)) {
        PyErr_SetString(PyExc_TypeError, "callback must be callable or None");
        return NULL;
    }
    if (!self->client) {
        PyErr_SetString(PyExc_RuntimeError, "Client not initialized");
        return NULL;
    }
    PyObject *old = self->lifecycleNotificationCallback;
    if (callback == Py_None) {
        self->lifecycleNotificationCallback = NULL;
        UA_Client_getConfig(self->client)->lifecycleNotificationCallback = NULL;
    } else {
        Py_INCREF(callback);
        self->lifecycleNotificationCallback = callback;
        UA_Client_getConfig(self->client)->lifecycleNotificationCallback =
            clientLifecycleNotificationCallback;
    }
    Py_XDECREF(old);
    Py_RETURN_NONE;
}

static PyObject *
pyClient_set_service_notification_callback(PyClient *self, PyObject *args) {
    O6_REQUIRE_LOOP_THREAD(pyClient_eventLoop(self), NULL);
    PyObject *callback;
    if (!PyArg_ParseTuple(args, "O", &callback))
        return NULL;
    if (callback != Py_None && !PyCallable_Check(callback)) {
        PyErr_SetString(PyExc_TypeError, "callback must be callable or None");
        return NULL;
    }
    if (!self->client) {
        PyErr_SetString(PyExc_RuntimeError, "Client not initialized");
        return NULL;
    }
    PyObject *old = self->serviceNotificationCallback;
    if (callback == Py_None) {
        self->serviceNotificationCallback = NULL;
        UA_Client_getConfig(self->client)->serviceNotificationCallback = NULL;
    } else {
        Py_INCREF(callback);
        self->serviceNotificationCallback = callback;
        UA_Client_getConfig(self->client)->serviceNotificationCallback =
            clientServiceNotificationCallback;
    }
    Py_XDECREF(old);
    Py_RETURN_NONE;
}

static PyObject *
pyClient_set_inactivity_callback(PyClient *self, PyObject *args) {
    O6_REQUIRE_LOOP_THREAD(pyClient_eventLoop(self), NULL);
    PyObject *callback;
    if (!PyArg_ParseTuple(args, "O", &callback))
        return NULL;
    if (callback != Py_None && !PyCallable_Check(callback)) {
        PyErr_SetString(PyExc_TypeError, "callback must be callable or None");
        return NULL;
    }
    if (!self->client) {
        PyErr_SetString(PyExc_RuntimeError, "Client not initialized");
        return NULL;
    }
    PyObject *old = self->inactivityCallback;
    if (callback == Py_None) {
        self->inactivityCallback = NULL;
        UA_Client_getConfig(self->client)->inactivityCallback = NULL;
    } else {
        Py_INCREF(callback);
        self->inactivityCallback = callback;
        UA_Client_getConfig(self->client)->inactivityCallback =
            clientInactivityCallback;
    }
    Py_XDECREF(old);
    Py_RETURN_NONE;
}

static PyObject *
pyClient_set_subscription_inactivity_callback(PyClient *self, PyObject *args) {
    O6_REQUIRE_LOOP_THREAD(pyClient_eventLoop(self), NULL);
    PyObject *callback;
    if (!PyArg_ParseTuple(args, "O", &callback))
        return NULL;
    if (callback != Py_None && !PyCallable_Check(callback)) {
        PyErr_SetString(PyExc_TypeError, "callback must be callable or None");
        return NULL;
    }
    if (!self->client) {
        PyErr_SetString(PyExc_RuntimeError, "Client not initialized");
        return NULL;
    }
    PyObject *old = self->subscriptionInactivityCallback;
    if (callback == Py_None) {
        self->subscriptionInactivityCallback = NULL;
        UA_Client_getConfig(self->client)->subscriptionInactivityCallback = NULL;
    } else {
        Py_INCREF(callback);
        self->subscriptionInactivityCallback = callback;
        UA_Client_getConfig(self->client)->subscriptionInactivityCallback =
            clientSubscriptionInactivityCallback;
    }
    Py_XDECREF(old);
    Py_RETURN_NONE;
}

/* A connect that failed synchronously. The state callback may already have
 * failed the future. Return that future, so the caller retrieves the
 * exception, instead of raising and leaving an unretrieved exception on the
 * dropped future. Steals the reference to future. */
static PyObject *
connectFailed(PyClient *self, PyObject *future, UA_StatusCode status) {
    PyObject *done = PyObject_CallMethod(future, "done", NULL);
    int isDone = done ? PyObject_IsTrue(done) : -1;
    Py_XDECREF(done);
    if(isDone == 0) {
        PyObject *code = PyLong_FromUnsignedLong(status);
        PyObject *exc = code ? PyObject_CallOneArg(pyExc_StatusCode, code) : NULL;
        Py_XDECREF(code);
        PyObject *res = exc
            ? PyObject_CallMethod(future, "set_exception", "O", exc) : NULL;
        Py_XDECREF(exc);
        Py_XDECREF(res);
        if(!res)
            isDone = -1;
    }
    if(self->connectFuture == future) {
        Py_DECREF(self->connectFuture);
        self->connectFuture = NULL;
    }
    if(isDone < 0) {
        Py_DECREF(future);
        return NULL;
    }
    return future;
}

/* A connect that started. Bound it by config.timeout unless the state
 * callback already completed it. A timeout of 0 waits without limit.
 * Steals the reference to future. */
static PyObject *
connectStarted(PyClient *self, PyObject *future) {
    UA_ClientConfig *config = UA_Client_getConfig(self->client);
    if (self->connectFuture != future || !config->timeout)
        return future;
    UA_EventLoop *el = config->eventLoop;
    UA_DateTime deadline = el->dateTime_nowMonotonic(el) +
        (UA_DateTime)config->timeout * UA_DATETIME_MSEC;
    UA_StatusCode status =
        UA_Client_addTimedCallback(self->client, connectTimeoutCallback, NULL,
                                   deadline, &self->connectTimeoutId);
    if (status == UA_STATUSCODE_GOOD)
        return future;
    UA_Client_disconnectSecureChannelAsync(self->client);
    return connectFailed(self, future, status);
}

static PyObject *
pyClient_connect(PyClient *self, PyObject *args) {
    O6_REQUIRE_LOOP_THREAD(pyClient_eventLoop(self), NULL);
    // connect() takes no arguments — uses endpointUrl from config
    if (PyTuple_Size(args) != 0) {
        PyErr_SetString(PyExc_ValueError,
                        "connect() takes no arguments. "
                        "Set endpointUrl in constructor or config");
        return NULL;
    }

    if (self->connectFuture || self->disconnectFuture) {
        PyErr_SetString(PyExc_RuntimeError,
                        "The client is already connecting");
        return NULL;
    }

    UA_Client *client = self->client;
    UA_ClientConfig *config = UA_Client_getConfig(client);
    if (config->endpointUrl.length == 0 || !config->endpointUrl.data) {
        PyErr_SetString(PyExc_ValueError,
                        "No endpointUrl configured. "
                        "Set endpointUrl in constructor or config.");
        return NULL;
    }

    // Create a future to wait for the connection to complete
    AsyncIOLoop *el = (AsyncIOLoop*)config->eventLoop;
    self->connectFuture = PyObject_CallMethod(el->pyLoop, "create_future", NULL);
    if (!self->connectFuture) {
        PyErr_SetString(PyExc_RuntimeError, "Could not create the connect future");
        return NULL;
    }

    /* Keep our own reference to the future to return. The state callback can
     * fire synchronously inside UA_Client_connectAsync and resolve + clear
     * self->connectFuture before connectAsync returns, so we must not rely on
     * self->connectFuture still being set afterwards. */
    PyObject *future = self->connectFuture;
    Py_INCREF(future);

    UA_StatusCode status = UA_Client_connectAsync(client, NULL);
    if (status != UA_STATUSCODE_GOOD)
        return connectFailed(self, future, status);

    return connectStarted(self, future);
}

static PyObject *
pyClient_disconnect(PyClient *self, PyObject *args) {
    O6_REQUIRE_LOOP_THREAD(pyClient_eventLoop(self), NULL);
    // If we are still connecting, abort
    UA_Client *client = self->client;
    abortConnect(self);

    // Are we already disconnected?
    UA_SecureChannelState channelState = 0;
    UA_Client_getState(client, &channelState, NULL, NULL);
    if (channelState == UA_SECURECHANNELSTATE_CLOSED)
        Py_RETURN_NONE;

    // Create a future for disconnecting
    UA_ClientConfig *config = UA_Client_getConfig(client);
    AsyncIOLoop *el = (AsyncIOLoop*)config->eventLoop;
    self->disconnectFuture = PyObject_CallMethod(el->pyLoop, "create_future", NULL);
    if (!self->disconnectFuture) {
        PyErr_SetString(PyExc_RuntimeError, "Could not create the disconnect future");
        return NULL;
    }

    /* Hold our own reference: UA_Client_disconnectAsync may resolve and clear
     * self->disconnectFuture synchronously via the state callback (e.g. when
     * the channel is already closed), leaving the member NULL. */
    PyObject *future = self->disconnectFuture;
    Py_INCREF(future);

    // Begin to disconnect and return
    UA_Client_disconnectAsync(client);
    return future;
}

static PyObject *
pyClient_connect_secure_channel(PyClient *self, PyObject *args) {
    O6_REQUIRE_LOOP_THREAD(pyClient_eventLoop(self), NULL);
    // connect_secure_channel() takes no arguments — uses endpointUrl from config
    if (PyTuple_Size(args) != 0) {
        PyErr_SetString(PyExc_ValueError,
                        "connect_secure_channel() takes no arguments. "
                        "Set endpointUrl in constructor or config");
        return NULL;
    }

    if (self->connectFuture || self->disconnectFuture) {
        PyErr_SetString(PyExc_RuntimeError,
                        "The client is already connecting");
        return NULL;
    }

    UA_Client *client = self->client;
    UA_ClientConfig *config = UA_Client_getConfig(client);
    if (config->endpointUrl.length == 0 || !config->endpointUrl.data) {
        PyErr_SetString(PyExc_ValueError,
                        "No endpointUrl configured. "
                        "Set endpointUrl in constructor or config.");
        return NULL;
    }

    // Create a future to wait for the connection to complete
    AsyncIOLoop *el = (AsyncIOLoop*)config->eventLoop;
    self->connectFuture = PyObject_CallMethod(el->pyLoop, "create_future", NULL);
    if (!self->connectFuture) {
        PyErr_SetString(PyExc_RuntimeError, "Could not create the connect future");
        return NULL;
    }

    /* See pyClient_connect: hold our own reference because the state callback
     * may resolve and clear self->connectFuture synchronously. */
    PyObject *future = self->connectFuture;
    Py_INCREF(future);

    // UA_Client_connectSecureChannelAsync sets noSession=true internally,
    // then calls __UA_Client_connect. We cannot set noSession from Python
    // because UA_Client_connectAsync resets it to false.
    UA_StatusCode status = UA_Client_connectSecureChannelAsync(client, NULL);
    if (status != UA_STATUSCODE_GOOD)
        return connectFailed(self, future, status);

    return connectStarted(self, future);
}

static PyObject *
pyClient_disconnect_secure_channel(PyClient *self, PyObject *args) {
    O6_REQUIRE_LOOP_THREAD(pyClient_eventLoop(self), NULL);
    UA_Client *client = self->client;

    // If we are still connecting, abort
    abortConnect(self);

    // Are we already disconnected?
    UA_SecureChannelState channelState = 0;
    UA_Client_getState(client, &channelState, NULL, NULL);
    if (channelState == UA_SECURECHANNELSTATE_CLOSED)
        Py_RETURN_NONE;

    // Create a future for disconnecting
    UA_ClientConfig *config = UA_Client_getConfig(client);
    AsyncIOLoop *el = (AsyncIOLoop*)config->eventLoop;
    self->disconnectFuture = PyObject_CallMethod(el->pyLoop, "create_future", NULL);
    if (!self->disconnectFuture) {
        PyErr_SetString(PyExc_RuntimeError, "Could not create the disconnect future");
        return NULL;
    }

    /* See pyClient_disconnect: hold our own reference because the state
     * callback may resolve and clear self->disconnectFuture synchronously. */
    PyObject *future = self->disconnectFuture;
    Py_INCREF(future);

    UA_StatusCode status = UA_Client_disconnectSecureChannelAsync(client);
    if (status != UA_STATUSCODE_GOOD) {
        if (self->disconnectFuture) {
            Py_DECREF(self->disconnectFuture);
            self->disconnectFuture = NULL;
        }
        Py_DECREF(future);
        return PyErr_StatusCode(status);
    }

    return future;
}

static PyObject *
pyClient_start_reverse_connect(PyClient *self, PyObject *args) {
    O6_REQUIRE_LOOP_THREAD(pyClient_eventLoop(self), NULL);
    unsigned short port;
    PyObject *pyHostnames;
    if (!PyArg_ParseTuple(args, "HO", &port, &pyHostnames))
        return NULL;

    if (!PyList_Check(pyHostnames)) {
        PyErr_SetString(PyExc_TypeError, "hostnames must be a list of strings");
        return NULL;
    }

    Py_ssize_t count = PyList_Size(pyHostnames);
    /* A non-null zero-length allocation looks like a scalar UA_Variant.
     * Preserve the native empty-array representation for wildcard listening. */
    UA_String *hostnames = count ? (UA_String*)calloc(count, sizeof(UA_String)) : NULL;
    if (count && !hostnames)
        return PyErr_NoMemory();

    for (Py_ssize_t i = 0; i < count; i++) {
        PyObject *item = PyList_GetItem(pyHostnames, i);
        if (!PyUnicode_Check(item)) {
            free(hostnames);
            PyErr_SetString(PyExc_TypeError, "hostnames must be a list of strings");
            return NULL;
        }
        Py_ssize_t len;
        const char *str = PyUnicode_AsUTF8AndSize(item, &len);
        hostnames[i] = UA_STRING_ALLOC(str);
    }

    if (self->connectFuture || self->disconnectFuture) {
        for (Py_ssize_t i = 0; i < count; i++)
            UA_String_clear(&hostnames[i]);
        free(hostnames);
        PyErr_SetString(PyExc_RuntimeError,
                        "The client is already connecting");
        return NULL;
    }

    UA_Client *client = self->client;
    UA_ClientConfig *config = UA_Client_getConfig(client);
    AsyncIOLoop *el = (AsyncIOLoop*)config->eventLoop;
    self->connectFuture = PyObject_CallMethod(el->pyLoop, "create_future", NULL);
    if (!self->connectFuture) {
        for (Py_ssize_t i = 0; i < count; i++)
            UA_String_clear(&hostnames[i]);
        free(hostnames);
        PyErr_SetString(PyExc_RuntimeError, "Could not create the connect future");
        return NULL;
    }

    /* See pyClient_connect: hold our own reference because the state callback
     * may resolve and clear self->connectFuture synchronously. */
    PyObject *future = self->connectFuture;
    Py_INCREF(future);

    UA_StatusCode status = UA_Client_startListeningForReverseConnect(
        client, hostnames, (size_t)count, (UA_UInt16)port);

    for (Py_ssize_t i = 0; i < count; i++)
        UA_String_clear(&hostnames[i]);
    free(hostnames);

    if (status != UA_STATUSCODE_GOOD) {
        if (self->connectFuture) {
            Py_DECREF(self->connectFuture);
            self->connectFuture = NULL;
        }
        Py_DECREF(future);
        return PyErr_StatusCode(status);
    }

    return future;
}

static PyObject *
pyClient_get_session_auth_token(PyClient *self, PyObject *Py_UNUSED(ignored)) {
    O6_REQUIRE_LOOP_THREAD(pyClient_eventLoop(self), NULL);
    const UA_NamespaceMapping *nsMapping = &self->nsMapPy2UA;
    UA_NodeId token;
    UA_NodeId_init(&token);
    UA_ByteString nonce;
    UA_ByteString_init(&nonce);

    UA_StatusCode status =
        UA_Client_getSessionAuthenticationToken(self->client, &token, &nonce);
    if (status != UA_STATUSCODE_GOOD) {
        UA_NodeId_clear(&token);
        UA_ByteString_clear(&nonce);
        return PyErr_StatusCode(status);
    }

    PyObject *pyToken = UA2PY(&token, &UA_TYPES[UA_TYPES_NODEID], nsMapping);
    PyObject *pyNonce = UA2PY(&nonce, &UA_TYPES[UA_TYPES_BYTESTRING], nsMapping);
    UA_NodeId_clear(&token);
    UA_ByteString_clear(&nonce);

    if (!pyToken || !pyNonce) {
        Py_XDECREF(pyToken);
        Py_XDECREF(pyNonce);
        return NULL;
    }

    PyObject *result = PyTuple_Pack(2, pyToken, pyNonce);
    Py_DECREF(pyToken);
    Py_DECREF(pyNonce);
    return result;
}

static PyObject *
pyClient_activate_current_session(PyClient *self, PyObject *args) {
    O6_REQUIRE_LOOP_THREAD(pyClient_eventLoop(self), NULL);
    if (self->connectFuture) {
        PyErr_SetString(PyExc_RuntimeError,
                        "The client already has a pending connect/activate");
        return NULL;
    }

    UA_Client *client = self->client;
    UA_ClientConfig *config = UA_Client_getConfig(client);
    AsyncIOLoop *el = (AsyncIOLoop*)config->eventLoop;
    self->connectFuture = PyObject_CallMethod(el->pyLoop, "create_future", NULL);
    if (!self->connectFuture) {
        PyErr_SetString(PyExc_RuntimeError, "Could not create the connect future");
        return NULL;
    }

    /* See pyClient_connect: hold our own reference because the state callback
     * may resolve and clear self->connectFuture synchronously. */
    PyObject *future = self->connectFuture;
    Py_INCREF(future);

    UA_StatusCode status = UA_Client_activateCurrentSessionAsync(client);
    if (status != UA_STATUSCODE_GOOD) {
        if (self->connectFuture) {
            Py_DECREF(self->connectFuture);
            self->connectFuture = NULL;
        }
        Py_DECREF(future);
        return PyErr_StatusCode(status);
    }

    return future;
}

static PyObject *
pyClient_activate_session(PyClient *self, PyObject *args) {
    O6_REQUIRE_LOOP_THREAD(pyClient_eventLoop(self), NULL);
    const UA_NamespaceMapping *nsMapping = &self->nsMapPy2UA;
    UA_ClientConfig *config = UA_Client_getConfig(self->client);
    PyObject *pyToken;
    PyObject *pyNonce;
    if (!PyArg_ParseTuple(args, "OO", &pyToken, &pyNonce))
        return NULL;

    if (self->connectFuture) {
        PyErr_SetString(PyExc_RuntimeError,
                        "The client already has a pending connect/activate");
        return NULL;
    }

    UA_NodeId token;
    UA_NodeId_init(&token);
    if (PY2UA(pyToken, &token, &UA_TYPES[UA_TYPES_NODEID], nsMapping, config->customDataTypes) == NULL) {
        PyErr_SetString(PyExc_TypeError, "Invalid authentication token");
        return NULL;
    }

    UA_ByteString nonce;
    UA_ByteString_init(&nonce);
    if (PY2UA(pyNonce, &nonce, &UA_TYPES[UA_TYPES_BYTESTRING], nsMapping, config->customDataTypes) == NULL) {
        UA_NodeId_clear(&token);
        PyErr_SetString(PyExc_TypeError, "Invalid server nonce");
        return NULL;
    }

    UA_Client *client = self->client;
    AsyncIOLoop *el = (AsyncIOLoop*)config->eventLoop;
    self->connectFuture = PyObject_CallMethod(el->pyLoop, "create_future", NULL);
    if (!self->connectFuture) {
        UA_NodeId_clear(&token);
        UA_ByteString_clear(&nonce);
        PyErr_SetString(PyExc_RuntimeError, "Could not create the connect future");
        return NULL;
    }

    /* See pyClient_connect: hold our own reference because the state callback
     * may resolve and clear self->connectFuture synchronously. */
    PyObject *future = self->connectFuture;
    Py_INCREF(future);

    UA_StatusCode status = UA_Client_activateSessionAsync(client, token, nonce);
    UA_NodeId_clear(&token);
    UA_ByteString_clear(&nonce);

    if (status != UA_STATUSCODE_GOOD) {
        if (self->connectFuture) {
            Py_DECREF(self->connectFuture);
            self->connectFuture = NULL;
        }
        Py_DECREF(future);
        return PyErr_StatusCode(status);
    }

    return future;
}

/* Bridge callback: invoked by the open62541 timer, calls the Python callable
 * stored in *data. */
static void
pyClientCallbackBridge(UA_Client *client, void *data) {
    PyObject *callback = (PyObject *)data;
    if (!callback)
        return;
    PyObject *result = PyObject_CallNoArgs(callback);
    if (!result)
        PyErr_Print();
    else
        Py_DECREF(result);
}

PyObject *
pyClient_add_timed_callback(PyObject *self, PyObject *args) {
    O6_REQUIRE_LOOP_THREAD(pyClient_eventLoop((PyClient *)self), NULL);
    PyObject *callback;
    double delay_ms;
    if (!PyArg_ParseTuple(args, "Od", &callback, &delay_ms))
        return NULL;
    if (!PyCallable_Check(callback)) {
        PyErr_SetString(PyExc_TypeError, "callback must be callable");
        return NULL;
    }

    PyClient *pyClient = (PyClient *)self;
    UA_Client *client = pyClient->client;
    UA_ClientConfig *config = UA_Client_getConfig(client);
    UA_DateTime date = config->eventLoop->dateTime_nowMonotonic(config->eventLoop)
                       + (UA_DateTime)(delay_ms * UA_DATETIME_MSEC);

    Py_INCREF(callback);
    UA_UInt64 callbackId = 0;
    UA_StatusCode status = UA_Client_addTimedCallback(
        client, pyClientCallbackBridge, callback, date, &callbackId);
    if (status != UA_STATUSCODE_GOOD) {
        Py_DECREF(callback);
        return PyErr_StatusCode(status);
    }

    PyObject *key = PyLong_FromUnsignedLongLong(callbackId);
    PyDict_SetItem(pyClient->callbackDict, key, callback);
    Py_DECREF(key);
    return PyLong_FromUnsignedLongLong(callbackId);
}

PyObject *
pyClient_add_repeated_callback(PyObject *self, PyObject *args) {
    O6_REQUIRE_LOOP_THREAD(pyClient_eventLoop((PyClient *)self), NULL);
    PyObject *callback;
    double interval_ms;
    if (!PyArg_ParseTuple(args, "Od", &callback, &interval_ms))
        return NULL;
    if (!PyCallable_Check(callback)) {
        PyErr_SetString(PyExc_TypeError, "callback must be callable");
        return NULL;
    }

    PyClient *pyClient = (PyClient *)self;
    Py_INCREF(callback);
    UA_UInt64 callbackId = 0;
    UA_StatusCode status = UA_Client_addRepeatedCallback(
        pyClient->client, pyClientCallbackBridge, callback, interval_ms, &callbackId);
    if (status != UA_STATUSCODE_GOOD) {
        Py_DECREF(callback);
        return PyErr_StatusCode(status);
    }

    PyObject *key = PyLong_FromUnsignedLongLong(callbackId);
    PyDict_SetItem(pyClient->callbackDict, key, callback);
    Py_DECREF(key);
    return PyLong_FromUnsignedLongLong(callbackId);
}

PyObject *
pyClient_change_repeated_callback_interval(PyObject *self, PyObject *args) {
    O6_REQUIRE_LOOP_THREAD(pyClient_eventLoop((PyClient *)self), NULL);
    unsigned long long callbackId;
    double interval_ms;
    if (!PyArg_ParseTuple(args, "Kd", &callbackId, &interval_ms))
        return NULL;

    PyClient *pyClient = (PyClient *)self;
    UA_StatusCode status = UA_Client_changeRepeatedCallbackInterval(
        pyClient->client, (UA_UInt64)callbackId, interval_ms);
    if (status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);
    Py_RETURN_NONE;
}

PyObject *
pyClient_remove_callback(PyObject *self, PyObject *args) {
    O6_REQUIRE_LOOP_THREAD(pyClient_eventLoop((PyClient *)self), NULL);
    unsigned long long callbackId;
    if (!PyArg_ParseTuple(args, "K", &callbackId))
        return NULL;

    PyClient *pyClient = (PyClient *)self;
    UA_Client_removeCallback(pyClient->client, (UA_UInt64)callbackId);

    /* Release the Python callback reference */
    PyObject *key = PyLong_FromUnsignedLongLong(callbackId);
    PyObject *callback = PyDict_GetItem(pyClient->callbackDict, key);
    if (callback) {
        Py_DECREF(callback);  /* Matches the Py_INCREF when added */
        PyDict_DelItem(pyClient->callbackDict, key);
    }
    Py_DECREF(key);
    Py_RETURN_NONE;
}

PyObject *
pyClient_get_namespace_uri(PyObject *self, PyObject *args) {
    O6_REQUIRE_LOOP_THREAD(pyClient_eventLoop((PyClient *)self), NULL);
    unsigned short index;
    if (!PyArg_ParseTuple(args, "H", &index))
        return NULL;
    PyClient *pyClient = (PyClient *)self;
    const UA_NamespaceMapping *nsMapping = &pyClient->nsMapPy2UA;
    UA_String nsUri;
    UA_String_init(&nsUri);
    UA_StatusCode status = UA_Client_getNamespaceUri(pyClient->client, (UA_UInt16)index, &nsUri);
    if (status != UA_STATUSCODE_GOOD) {
        UA_String_clear(&nsUri);
        return PyErr_StatusCode(status);
    }
    PyObject *result = UA2PY(&nsUri, &UA_TYPES[UA_TYPES_STRING], nsMapping);
    UA_String_clear(&nsUri);
    return result;
}

PyObject *
pyClient_get_namespace_index(PyObject *self, PyObject *args) {
    O6_REQUIRE_LOOP_THREAD(pyClient_eventLoop((PyClient *)self), NULL);
    const char *uri_data;
    Py_ssize_t uri_len;
    if (!PyArg_ParseTuple(args, "s#", &uri_data, &uri_len))
        return NULL;
    PyClient *pyClient = (PyClient *)self;
    UA_String nsUri = {.length = (size_t)uri_len, .data = (UA_Byte *)(uintptr_t)uri_data};
    UA_UInt16 outIndex = 0;
    UA_StatusCode status = UA_Client_getNamespaceIndex(pyClient->client, nsUri, &outIndex);
    if (status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);
    return PyLong_FromUnsignedLong(outIndex);
}

PyObject *
pyClient_apply_namespace_snapshot(PyObject *self, PyObject *args) {
    O6_REQUIRE_LOOP_THREAD(pyClient_eventLoop((PyClient *)self), NULL);
    PyObject *urisObj;
    PyObject *entriesObj;
    if(!PyArg_ParseTuple(args, "OO", &urisObj, &entriesObj))
        return NULL;
    PyObject *uris = PySequence_Fast(urisObj,
        "namespace uris must be an iterable of strings");
    if(!uris)
        return NULL;
    PyObject *entries = PySequence_Fast(entriesObj,
        "namespace snapshot must be an iterable of (uri, python_index, wire_index)");
    if(!entries) {
        Py_DECREF(uris);
        return NULL;
    }

    PyClient *pyClient = (PyClient *)self;
    UA_NamespaceMapping newPyMapping = {0};
    UA_NamespaceMapping *newChannelMapping =
        (UA_NamespaceMapping *)UA_calloc(1, sizeof(UA_NamespaceMapping));
    UA_DataTypeArray *newCustomTypes = NULL;
    if(!newChannelMapping) {
        Py_DECREF(uris);
        Py_DECREF(entries);
        return PyErr_NoMemory();
    }

    UA_StatusCode st = UA_STATUSCODE_GOOD;
    Py_ssize_t uriCount = PySequence_Fast_GET_SIZE(uris);
    for(Py_ssize_t i = 0; i < uriCount; i++) {
        PyObject *uriObj = PySequence_Fast_GET_ITEM(uris, i);
        Py_ssize_t uriLength;
        const char *uriData = PyUnicode_AsUTF8AndSize(uriObj, &uriLength);
        if(!uriData)
            goto fail;
        UA_String uri = {
            .length = (size_t)uriLength,
            .data = (UA_Byte *)(uintptr_t)uriData
        };
        st = ua_extension_namespace_mapping_set(
            newChannelMapping, uri, (UA_UInt16)i, (UA_UInt16)i);
        if(st != UA_STATUSCODE_GOOD)
            goto fail;
    }

    Py_ssize_t count = PySequence_Fast_GET_SIZE(entries);
    for(Py_ssize_t i = 0; i < count; i++) {
        const char *uriData;
        Py_ssize_t uriLength;
        unsigned short pythonIndex;
        unsigned short wireIndex;
        PyObject *entry = PySequence_Fast_GET_ITEM(entries, i);
        if(!PyArg_ParseTuple(entry, "s#HH", &uriData, &uriLength,
                             &pythonIndex, &wireIndex)) {
            st = UA_STATUSCODE_BADINVALIDARGUMENT;
            goto fail;
        }
        UA_String uri = {
            .length = (size_t)uriLength,
            .data = (UA_Byte *)(uintptr_t)uriData
        };
        st = ua_extension_namespace_mapping_set(
            &newPyMapping, uri, (UA_UInt16)pythonIndex, (UA_UInt16)wireIndex);
        if(st != UA_STATUSCODE_GOOD)
            goto fail;
    }

    UA_ClientConfig *config = UA_Client_getConfig(pyClient->client);
    st = o6_datatypes_update_custom_datatypes(&newPyMapping, &newCustomTypes);
    if(st != UA_STATUSCODE_GOOD)
        goto fail;

    UA_NamespaceMapping oldPyMapping = pyClient->nsMapPy2UA;
    UA_NamespaceMapping *oldChannelMapping = pyClient->client->channel.namespaceMapping;
    UA_DataTypeArray *oldCustomTypes = config->customDataTypes;
    pyClient->nsMapPy2UA = newPyMapping;
    pyClient->client->channel.namespaceMapping = newChannelMapping;
    config->customDataTypes = newCustomTypes;

    UA_NamespaceMapping_clear(&oldPyMapping);
    UA_NamespaceMapping_delete(oldChannelMapping);
    o6_datatypes_clear_custom_datatypes(&oldCustomTypes);
    Py_DECREF(uris);
    Py_DECREF(entries);

    Py_RETURN_NONE;

fail:
    UA_NamespaceMapping_clear(&newPyMapping);
    UA_NamespaceMapping_delete(newChannelMapping);
    o6_datatypes_clear_custom_datatypes(&newCustomTypes);
    Py_DECREF(uris);
    Py_DECREF(entries);
    if(PyErr_Occurred())
        return NULL;
    return PyErr_StatusCode(st);
}

PyObject *
pyClient_find_data_type(PyObject *self, PyObject *args) {
    O6_REQUIRE_LOOP_THREAD(pyClient_eventLoop((PyClient *)self), NULL);
    PyObject *nodeId_obj;
    if (!PyArg_ParseTuple(args, "O", &nodeId_obj))
        return NULL;
    PyClient *pyClient = (PyClient *)self;
    const UA_NamespaceMapping *nsMapping = &pyClient->nsMapPy2UA;
    UA_NodeId typeId;
    UA_NodeId_init(&typeId);
    if (PY2UA(nodeId_obj, &typeId, &UA_TYPES[UA_TYPES_NODEID], nsMapping, UA_Client_getConfig(pyClient->client)->customDataTypes) == NULL)
        return NULL;
    const UA_DataType *dt = UA_Client_findDataType(pyClient->client, &typeId);
    UA_NodeId_clear(&typeId);
    if (!dt)
        Py_RETURN_NONE;
    PyObject *d = PyDict_New();
    if (!d)
        return NULL;
#ifdef UA_ENABLE_TYPEDESCRIPTION
    PyObject *name = PyUnicode_FromString(dt->typeName ? dt->typeName : "");
#else
    PyObject *name = PyUnicode_FromString("");
#endif
    if (name) { PyDict_SetItemString(d, "typeName", name); Py_DECREF(name); }
    PyObject *tid = UA2PY(&dt->typeId, &UA_TYPES[UA_TYPES_NODEID], nsMapping);
    if (tid) { PyDict_SetItemString(d, "typeId", tid); Py_DECREF(tid); }
    PyObject *bid = UA2PY(&dt->binaryEncodingId, &UA_TYPES[UA_TYPES_NODEID], nsMapping);
    if (bid) { PyDict_SetItemString(d, "binaryEncodingId", bid); Py_DECREF(bid); }
    PyObject *kind = PyLong_FromUnsignedLong(dt->typeKind);
    if (kind) { PyDict_SetItemString(d, "typeKind", kind); Py_DECREF(kind); }
    PyObject *ms = PyLong_FromUnsignedLong(dt->membersSize);
    if (ms) { PyDict_SetItemString(d, "membersSize", ms); Py_DECREF(ms); }
    return d;
}

/* The typeIds of the still-encoded ExtensionObjects in a value, in Python
 * namespaces. The value is in the client-local (wire) namespaces. */
typedef struct {
    const UA_NamespaceMapping *nm;
    PyObject *binary;  /* list of NodeIds of binary bodies */
    PyObject *xml;     /* list of NodeIds of XML bodies */
    int failed;        /* a Python exception is set */
} EncodedScan;

static void scanEncoded(const void *p, const UA_DataType *type, EncodedScan *scan);

static void
scanEncodedArray(const void *p, size_t size, const UA_DataType *type, EncodedScan *scan) {
    uintptr_t ptr = (uintptr_t)p;
    for(size_t i = 0; i < size && !scan->failed; i++) {
        scanEncoded((const void *)ptr, type, scan);
        ptr += type->memSize;
    }
}

static void
scanEncodedMember(uintptr_t ptr, const UA_DataTypeMember *m, EncodedScan *scan) {
    if(!m->isArray)
        scanEncoded((const void *)ptr, m->memberType, scan);
    else
        scanEncodedArray(*(void **)(ptr + sizeof(size_t)), *(size_t *)ptr,
                         m->memberType, scan);
}

/* Follows the member layout that mapStructure in types_mapping.c walks. */
static void
scanEncodedStructure(const void *p, const UA_DataType *type, EncodedScan *scan) {
    uintptr_t ptr = (uintptr_t)p;
    for(size_t i = 0; i < type->membersSize && !scan->failed; i++) {
        const UA_DataTypeMember *m = &type->members[i];
        ptr += m->padding;
        if(!m->isOptional) {
            scanEncodedMember(ptr, m, scan);
            ptr += m->isArray ? sizeof(size_t) + sizeof(void *) : m->memberType->memSize;
        } else if(!m->isArray) {
            if(*(void **)ptr)
                scanEncoded(*(void **)ptr, m->memberType, scan);
            ptr += sizeof(void *);
        } else {
            scanEncodedMember(ptr, m, scan);
            ptr += sizeof(size_t) + sizeof(void *);
        }
    }
}

static void
scanEncoded(const void *p, const UA_DataType *type, EncodedScan *scan) {
    switch(type->typeKind) {
    case UA_DATATYPEKIND_EXTENSIONOBJECT: {
        const UA_ExtensionObject *eo = (const UA_ExtensionObject *)p;
        if(eo->encoding == UA_EXTENSIONOBJECT_ENCODED_BYTESTRING ||
           eo->encoding == UA_EXTENSIONOBJECT_ENCODED_XML) {
            PyObject *list = eo->encoding == UA_EXTENSIONOBJECT_ENCODED_XML
                ? scan->xml : scan->binary;
            PyObject *typeId = UA2PY(&eo->content.encoded.typeId,
                                     &UA_TYPES[UA_TYPES_NODEID], scan->nm);
            if(!typeId || PyList_Append(list, typeId) < 0)
                scan->failed = 1;
            Py_XDECREF(typeId);
        } else if((eo->encoding == UA_EXTENSIONOBJECT_DECODED ||
                   eo->encoding == UA_EXTENSIONOBJECT_DECODED_NODELETE) &&
                  eo->content.decoded.data) {
            scanEncoded(eo->content.decoded.data, eo->content.decoded.type, scan);
        }
        break;
    }
    case UA_DATATYPEKIND_VARIANT: {
        const UA_Variant *v = (const UA_Variant *)p;
        if(v->type && v->data)
            scanEncodedArray(v->data, UA_Variant_isScalar(v) ? 1 : v->arrayLength,
                             v->type, scan);
        break;
    }
    case UA_DATATYPEKIND_DATAVALUE: {
        const UA_DataValue *dv = (const UA_DataValue *)p;
        if(dv->hasValue)
            scanEncoded(&dv->value, &UA_TYPES[UA_TYPES_VARIANT], scan);
        break;
    }
    case UA_DATATYPEKIND_STRUCTURE:
    case UA_DATATYPEKIND_OPTSTRUCT:
        scanEncodedStructure(p, type, scan);
        break;
    case UA_DATATYPEKIND_UNION: {
        UA_UInt32 selection = *(const UA_UInt32 *)p;
        if(selection == 0 || selection > type->membersSize)
            break;
        const UA_DataTypeMember *m = &type->members[selection - 1];
        scanEncodedMember((uintptr_t)p + m->padding, m, scan);
        break;
    }
    default:
        break;
    }
}

/* Whether a value of the type can contain an ExtensionObject. Deeply nested
 * or self-containing types are assumed to. */
static UA_Boolean
canHoldEncoded(const UA_DataType *type, int depth) {
    switch(type->typeKind) {
    case UA_DATATYPEKIND_EXTENSIONOBJECT:
    case UA_DATATYPEKIND_VARIANT:
    case UA_DATATYPEKIND_DATAVALUE:
        return true;
    case UA_DATATYPEKIND_STRUCTURE:
    case UA_DATATYPEKIND_OPTSTRUCT:
    case UA_DATATYPEKIND_UNION:
        if(depth >= 16)
            return true;
        for(size_t i = 0; i < type->membersSize; i++) {
            if(canHoldEncoded(type->members[i].memberType, depth + 1))
                return true;
        }
        return false;
    default:
        return false;
    }
}

/* _redecode(value) -> (value, binaryTypeIds, xmlTypeIds)
 *
 * Decodes the binary-encoded ExtensionObjects in an ExtensionObject,
 * DataValue, structure or union again with the client's current DataTypes, as
 * a response from the server would be. Returns the value, the same object when
 * nothing was encoded, with the typeIds of the ExtensionObjects that stay
 * encoded. Other values are returned unchanged, without typeIds. */
static PyObject *
pyClient_redecode(PyObject *self, PyObject *args) {
    O6_REQUIRE_LOOP_THREAD(pyClient_eventLoop((PyClient *)self), NULL);
    PyObject *obj;
    if(!PyArg_ParseTuple(args, "O", &obj))
        return NULL;
    PyClient *pyClient = (PyClient *)self;
    const UA_DataType *pyType = PY2UAType(Py_TYPE(obj));
    if(!pyType || !pyClient->client)
        return Py_BuildValue("(O[][])", obj);

    /* A structure travels as an ExtensionObject, whose decoded type the
     * namespace mapping retargets to the client-local DataType. */
    const UA_DataType *type;
    switch(pyType->typeKind) {
    case UA_DATATYPEKIND_DATAVALUE:
        type = &UA_TYPES[UA_TYPES_DATAVALUE];
        break;
    case UA_DATATYPEKIND_EXTENSIONOBJECT:
    case UA_DATATYPEKIND_STRUCTURE:
    case UA_DATATYPEKIND_OPTSTRUCT:
    case UA_DATATYPEKIND_UNION:
        if(!canHoldEncoded(pyType, 0))
            return Py_BuildValue("(O[][])", obj);
        type = &UA_TYPES[UA_TYPES_EXTENSIONOBJECT];
        break;
    default:
        return Py_BuildValue("(O[][])", obj);
    }

    const UA_NamespaceMapping *nm = &pyClient->nsMapPy2UA;
    UA_ClientConfig *config = UA_Client_getConfig(pyClient->client);
    EncodedScan scan = {nm, PyList_New(0), PyList_New(0), 0};
    PyObject *result = NULL;
    UA_ByteString encoded = UA_BYTESTRING_NULL;
    void *value = UA_new(type);
    if(!value || !scan.binary || !scan.xml) {
        PyErr_NoMemory();
        goto done;
    }
    if(!PY2UA(obj, value, type, nm, config->customDataTypes))
        goto done;
    scanEncoded(value, type, &scan);
    if(scan.failed)
        goto done;
    if(PyList_GET_SIZE(scan.binary) == 0) {
        result = Py_BuildValue("(OOO)", obj, scan.binary, scan.xml);
        goto done;
    }

    UA_StatusCode status = UA_encodeBinary(value, type, &encoded, NULL);
    UA_clear(value, type);
    if(status == UA_STATUSCODE_GOOD) {
        UA_DecodeBinaryOptions options;
        memset(&options, 0, sizeof(options));
        options.customTypes = config->customDataTypes;
        status = UA_decodeBinary(&encoded, value, type, &options);
    }
    if(status != UA_STATUSCODE_GOOD) {
        PyErr_StatusCode(status);
        goto done;
    }

    Py_SETREF(scan.binary, PyList_New(0));
    Py_SETREF(scan.xml, PyList_New(0));
    if(!scan.binary || !scan.xml)
        goto done;
    scanEncoded(value, type, &scan);
    if(scan.failed)
        goto done;

    PyObject *decoded;
    UA_ExtensionObject *eo = (UA_ExtensionObject *)value;
    if(type == &UA_TYPES[UA_TYPES_EXTENSIONOBJECT] &&
       (eo->encoding == UA_EXTENSIONOBJECT_DECODED ||
        eo->encoding == UA_EXTENSIONOBJECT_DECODED_NODELETE))
        decoded = UA2PY(eo->content.decoded.data, eo->content.decoded.type, nm);
    else
        decoded = UA2PY(value, type, nm);
    if(decoded) {
        result = Py_BuildValue("(OOO)", decoded, scan.binary, scan.xml);
        Py_DECREF(decoded);
    }

done:
    UA_ByteString_clear(&encoded);
    if(value)
        UA_delete(value, type);
    Py_XDECREF(scan.binary);
    Py_XDECREF(scan.xml);
    return result;
}

static int
pyClient_init(PyClient *self, PyObject *args, PyObject *kwds) {
    if(o6_require_client() < 0)
        return -1;

    const char *endpoint_uri = NULL;
    static char *kwlist[] = {"endpoint_uri", "logger", "loop", NULL};

    PyObject *pyLog = NULL;
    PyObject *pyLoop = NULL;
    
    if (!PyArg_ParseTupleAndKeywords(args, kwds, "|sOO", kwlist, &endpoint_uri, &pyLog, &pyLoop)) {
        return -1;
    }

    if (!pyLoop || pyLoop == Py_None) {
        PyErr_SetString(PyExc_TypeError,
                        "o6._o6.Client() requires a 'loop' argument (asyncio.AbstractEventLoop). "
                        "Use o6.Client() for automatic loop handling.");
        return -1;
    }
    if (!pyLog || pyLog == Py_None) {
        PyErr_SetString(PyExc_TypeError,
                        "o6._o6.Client() requires a 'logger' argument. "
                        "Use o6.Client() for automatic logger handling.");
        return -1;
    }

    UA_ClientConfig cc = {0};
    cc.logging = pyLogger(pyLog);
    cc.eventLoop = UA_EventLoop_new_AsyncIO(pyLoop, pyLog);
    UA_ClientConfig_setDefault(&cc);
    /* The client identifies itself as o6, not open62541. Later
     * UA_ClientConfig_setDefault calls keep a set ApplicationUri. */
    o6_set_default_application_uri(&cc.clientDescription.applicationUri);
    UA_String_clear(&cc.clientDescription.productUri);
    cc.clientDescription.productUri = UA_STRING_ALLOC(O6_PRODUCT_URI);
    UA_LocalizedText_clear(&cc.clientDescription.applicationName);
    cc.clientDescription.applicationName =
        UA_LOCALIZEDTEXT_ALLOC("en", O6_CLIENT_APPLICATION_NAME);
    cc.maxAsyncServiceCalls = 32;
    cc.asyncServiceCallRule = UA_RULEHANDLING_ABORT;
    cc.stateCallback = clientStateCallback;
    /* The asynchronous Python namespace handshake installs a complete custom
     * datatype snapshot after the NamespaceArray has been read. */
    cc.customDataTypes = NULL;
    self->client = UA_Client_newWithConfig(&cc);
    if (!self->client) {
        PyErr_NoMemory();
        return -1;
    }

    /* Namespace synchronization is performed asynchronously by
     * Client.update_remote_namespaces(). The built-in handshake uses blocking
     * service calls and would deadlock the Python-owned asyncio event loop. */
    self->client->haveNamespaces = true;

    // The context pointer in the client config points to the Python object
    UA_ClientConfig *config = UA_Client_getConfig(self->client);
    config->clientContext = self;
    ((AsyncIOLoop*)config->eventLoop)->owner = (PyObject*)self;

    self->owns_loop = 0;
    self->config_cache = NULL;

    // Initialize the callback tracking dict
    self->callbackDict = PyDict_New();
    if (!self->callbackDict) {
        UA_Client_delete(self->client);
        self->client = NULL;
        return -1;
    }

    // Notification callbacks start unset
    self->globalNotificationCallback = NULL;
    self->lifecycleNotificationCallback = NULL;
    self->serviceNotificationCallback = NULL;
    self->inactivityCallback = NULL;
    self->subscriptionInactivityCallback = NULL;

    // If endpoint_uri is provided, validate and set it in the config
    if (endpoint_uri) {
        if (!validate_endpoint_uri(endpoint_uri)) {
            PyErr_SetString(PyExc_ValueError, "Invalid endpointUri schema. Expected format: "
                            "opc.tcp://host[:port][/path], with an IPv6 address in brackets");
            UA_Client_delete(self->client);
            self->client = NULL;
            return -1;
        }
        
        if (config) {
            config->endpointUrl = UA_STRING_ALLOC(endpoint_uri);
        }
    }

    return 0;
}

/* Core cleanup: stop the C event loop, delete the UA_Client, and free
 * the C event loop struct.  Does NOT call tp_free — the caller is
 * responsible for that.
 *
 * Normally called from Python __del__ via the _cleanup method, where
 * Python API calls are safe. Also called directly from tp_dealloc as a
 * deterministic fallback. */
static void
pyClient_do_cleanup(PyClient *self) {
    if(!self->client)
        return;

    stopConnectTimers(self);
    UA_ClientConfig *config = UA_Client_getConfig(self->client);
    UA_EventLoop *el = NULL;
    if(config) {
        config->clientContext = NULL;
        config->stateCallback = NULL;
        config->globalNotificationCallback = NULL;
        config->lifecycleNotificationCallback = NULL;
        config->serviceNotificationCallback = NULL;
        config->inactivityCallback = NULL;
        config->subscriptionInactivityCallback = NULL;
    }
    if(config && !config->externalEventLoop) {
        el = config->eventLoop;
        config->externalEventLoop = true;
    }

    /* Grab the Python asyncio loop BEFORE freeing the C event loop.
     * el->free() will Py_XDECREF(el->pyLoop) and free the struct,
     * so we need our own reference to prevent a dangling pointer
     * during cleanup. */
    PyObject *pyLoop = NULL;
    if(el && self->owns_loop) {
        pyLoop = ((AsyncIOLoop*)el)->pyLoop;
        Py_XINCREF(pyLoop);
    }

    /* Stop the C event loop BEFORE UA_Client_delete.
     * UA_Client_delete -> UA_Client_disconnect -> disconnectSecureChannel
     * has a sync while-loop that spins on el->run() until the channel
     * reaches CLOSED.  With an asyncio-backed event loop, el->run()
     * cannot drive real I/O (it only flushes delayed callbacks), so the
     * channel state never transitions and we get an infinite loop that
     * holds the GIL.  Stopping the event loop first makes the while-loop
     * condition (el->state != STOPPED) false, so it is skipped entirely.
     *
     * Mark tearingDown so that AsyncIOTCP_eventSourceStop skips
     * PyObject_CallMethod(transport/server, "close").  After
     * disconnect() the connections are already closed; calling
     * Python methods during GC with coverage instrumentation
     * active can trigger segfaults. */
    if(el) {
        ((AsyncIOLoop*)el)->tearingDown = 1;
        if(el->state != UA_EVENTLOOPSTATE_FRESH &&
           el->state != UA_EVENTLOOPSTATE_STOPPED) {
            PyErr_Clear();
            el->stop(el);
        }
    }

    UA_Client_delete(self->client);
    self->client = NULL;

    UA_NamespaceMapping_clear(&self->nsMapPy2UA);

    /* An externally-held config wrapper must not retain a dangling borrowed
     * pointer after its UA_Client has gone away. */
    PyClientConfig_Invalidate(self->config_cache);
    Py_CLEAR(self->config_cache);

    if(el) {
        el->free(el);
        el = NULL;
    }

    Py_XDECREF(pyLoop);
    pyLoop = NULL;

    if(PyErr_Occurred())
        PyErr_Clear();
}

/* Python-callable cleanup method exposed as _cleanup().
 * Called from Python __del__ to eagerly release C resources while
 * Python API calls are still safe.  After this, self->client is NULL
 * so tp_dealloc just calls tp_free. */
static PyObject *
pyClient_cleanup(PyClient *self, PyObject *Py_UNUSED(ignored)) {
    O6_REQUIRE_LOOP_THREAD(pyClient_eventLoop(self), NULL);
    pyClient_do_cleanup(self);
    Py_RETURN_NONE;
}

static int
pyClient_traverse(PyClient *self, visitproc visit, void *arg) {
    ServiceFuture *sf;
    LIST_FOREACH(sf, &self->serviceFutures, entry) {
        Py_VISIT(sf->future);
        Py_VISIT(sf->pyClient);
    }
    if(pyClient_subscriptions_traverse(self, visit, arg) < 0)
        return -1;
    Py_VISIT(self->connectFuture);
    Py_VISIT(self->disconnectFuture);
    Py_VISIT(self->callbackDict);
    Py_VISIT(self->globalNotificationCallback);
    Py_VISIT(self->lifecycleNotificationCallback);
    Py_VISIT(self->serviceNotificationCallback);
    Py_VISIT(self->inactivityCallback);
    Py_VISIT(self->subscriptionInactivityCallback);
    Py_VISIT(self->config_cache);
    return 0;
}

/* Whether the native client is open or opening: lock-free, so finalizers
 * may call it on any thread. */
static PyObject *
pyClient_is_live(PyClient *self, PyObject *Py_UNUSED(ignored)) {
    return PyBool_FromLong(pyClient_isLive(self));
}

bool
pyClient_isLive(const PyClient *self) {
    return self && self->client &&
           (self->connectFuture != NULL ||
            self->client->channel.state != UA_SECURECHANNELSTATE_CLOSED);
}

static int
pyClient_clear_refs(PyClient *self) {
    pyClient_do_cleanup(self);
    Py_CLEAR(self->connectFuture);
    Py_CLEAR(self->disconnectFuture);
    Py_CLEAR(self->callbackDict);
    Py_CLEAR(self->globalNotificationCallback);
    Py_CLEAR(self->lifecycleNotificationCallback);
    Py_CLEAR(self->serviceNotificationCallback);
    Py_CLEAR(self->inactivityCallback);
    Py_CLEAR(self->subscriptionInactivityCallback);
    PyClientConfig_Invalidate(self->config_cache);
    Py_CLEAR(self->config_cache);
    return 0;
}

static void
pyClient_dealloc(PyClient *self) {
    PyObject_GC_UnTrack(self);
    pyClient_do_cleanup(self);
    pyClient_clear_refs(self);
    Py_TYPE(self)->tp_free((PyObject *)self);
}

static PyObject *pyClient_str(PyClient *self) {
    return PyUnicode_FromFormat("o6._o6.Client(%p)", self);
}

static PyObject *
pyClient_set_owns_loop(PyClient *self, PyObject *args) {
    O6_REQUIRE_LOOP_THREAD(pyClient_eventLoop(self), NULL);
    int owns;
    if(!PyArg_ParseTuple(args, "p", &owns))
        return NULL;
    self->owns_loop = owns;
    Py_RETURN_NONE;
}

static PyObject *pyClient_repr(PyClient *self) {
    if (!self->client)
        return PyUnicode_FromString("o6._o6.Client(uninitialized)");
    /* Lock-free like _is_live: repr stays callable from any thread, and
     * UA_Client_getState takes the client lock. */
    UA_ClientConfig *config = UA_Client_getConfig(self->client);
    UA_SecureChannelState channelState = self->client->channel.state;
    const char *state = (channelState == UA_SECURECHANNELSTATE_OPEN) ? "connected" : "disconnected";
    if (config->endpointUrl.length > 0 && config->endpointUrl.data)
        return PyUnicode_FromFormat("o6._o6.Client(%.*s, %s)",
                                   (int)config->endpointUrl.length,
                                   (const char *)config->endpointUrl.data, state);
    return PyUnicode_FromFormat("o6._o6.Client(%s)", state);
}

// Client getter for config property
static PyObject *pyClient_getConfig(PyClient *self, void *closure) {
    if (!self->client) {
        PyErr_SetString(PyExc_RuntimeError, "Client not initialized");
        return NULL;
    }
    if (!self->config_cache) {
        /* Create the singleton config object and cache it strongly.
         * PyClientConfig_New returns a new reference (refcount=1). */
        self->config_cache = PyClientConfig_New(self);
        if (!self->config_cache) return NULL;
    }
    Py_INCREF(self->config_cache);
    return self->config_cache;
}

// Client properties
static PyGetSetDef pyClient_getsetters[] = {
    {"config", (getter)pyClient_getConfig, NULL, "Client configuration object", NULL},
    {NULL} // Sentinel
};

static PyMethodDef pyClient_methods[] = {
    {"_set_owns_loop", (PyCFunction)pyClient_set_owns_loop, METH_VARARGS, "Set whether the client owns the asyncio loop"},
    {"_get_state", (PyCFunction)pyClient_get_state, METH_NOARGS, "Get the client connection state"},
    {"_cleanup", (PyCFunction)pyClient_cleanup, METH_NOARGS, NULL},
    {"_is_live", (PyCFunction)pyClient_is_live, METH_NOARGS,
     "Whether the client is connected or connecting; safe on any thread"},
    {"_connect", (PyCFunction)pyClient_connect, METH_VARARGS, "Connect to OPC UA server using configured endpointUrl"},
    {"_disconnect", (PyCFunction)pyClient_disconnect, METH_VARARGS, "Disconnect the client"},
    {"_connect_secure_channel", (PyCFunction)pyClient_connect_secure_channel, METH_VARARGS, "Connect SecureChannel only (no session)"},
    {"_disconnect_secure_channel", (PyCFunction)pyClient_disconnect_secure_channel, METH_VARARGS, "Disconnect only the secure channel (no CloseSession)"},
    {"_start_reverse_connect", (PyCFunction)pyClient_start_reverse_connect, METH_VARARGS, "Start listening for reverse connections"},
    {"_get_session_auth_token", (PyCFunction)pyClient_get_session_auth_token, METH_NOARGS, "Get the session authentication token and server nonce"},
    {"_activate_current_session", (PyCFunction)pyClient_activate_current_session, METH_VARARGS, "Re-activate the current session"},
    {"_activate_session", (PyCFunction)pyClient_activate_session, METH_VARARGS, "Activate a session from another client using auth token and nonce"},
    {"_add_timed_callback", (PyCFunction)pyClient_add_timed_callback, METH_VARARGS, "Add a one-shot callback to fire after delay_ms milliseconds"},
    {"_add_repeated_callback", (PyCFunction)pyClient_add_repeated_callback, METH_VARARGS, "Add a callback for cyclic repetition at interval_ms"},
    {"_change_repeated_callback_interval", (PyCFunction)pyClient_change_repeated_callback_interval, METH_VARARGS, "Change the interval of a repeated callback"},
    {"_remove_callback", (PyCFunction)pyClient_remove_callback, METH_VARARGS, "Remove a timed or repeated callback"},
    {"_get_namespace_uri", (PyCFunction)pyClient_get_namespace_uri, METH_VARARGS, "Get namespace URI by index"},
    {"_get_namespace_index", (PyCFunction)pyClient_get_namespace_index, METH_VARARGS, "Get namespace index by URI"},
    {"_apply_namespace_snapshot", (PyCFunction)pyClient_apply_namespace_snapshot, METH_VARARGS, "Internal: atomically replace namespace mappings and custom datatypes"},
    {"_find_data_type", (PyCFunction)pyClient_find_data_type, METH_VARARGS, "Look up a DataType by NodeId"},
    {"_redecode", (PyCFunction)pyClient_redecode, METH_VARARGS, "Internal: decode the encoded ExtensionObjects of a value again with the current DataTypes"},
    {"_set_global_notification_callback", (PyCFunction)pyClient_set_global_notification_callback, METH_VARARGS, "Set callback for all application notifications: callback(type: int, payload: dict)"},
    {"_set_lifecycle_notification_callback", (PyCFunction)pyClient_set_lifecycle_notification_callback, METH_VARARGS, "Set callback for lifecycle notifications: callback(type: int, payload: dict)"},
    {"_set_service_notification_callback", (PyCFunction)pyClient_set_service_notification_callback, METH_VARARGS, "Set callback for service notifications: callback(type: int, payload: dict)"},
    {"_set_inactivity_callback", (PyCFunction)pyClient_set_inactivity_callback, METH_VARARGS, "Set callback fired when connectivity check gets no response: callback()"},
    {"_set_subscription_inactivity_callback", (PyCFunction)pyClient_set_subscription_inactivity_callback, METH_VARARGS, "Set callback fired when a subscription times out: callback(sub_id: int)"},

    /* Raw services
     * ------------
     * Discovery */
    {"_service_find_servers", (PyCFunction)pyClient_find_servers, METH_VARARGS,
     "Get a list of registered servers using FindServersRequest/Response"},
    {"_service_find_servers_on_network", (PyCFunction)pyClient_find_servers_on_network, METH_VARARGS,
     "Get a list of known servers on the network using FindServersOnNetworkRequest/Response (LDS only)"},
    {"_service_get_endpoints", (PyCFunction)pyClient_get_endpoints, METH_VARARGS,
     "Get a list of endpoints from a server using GetEndpointsRequest/Response"},
    {"_service_register_server", (PyCFunction)pyClient_register_server, METH_VARARGS,
     "Register or unregister a server using RegisterServerRequest/Response"},
    {"_service_register_server2", (PyCFunction)pyClient_register_server2, METH_VARARGS,
     "Register or unregister with configuration using RegisterServer2Request/Response"},

    /* Node Management */
    {"_service_addNodes", (PyCFunction)pyClient_service_addNodes, METH_VARARGS,
     "Add nodes using UA_Client_Service_addNodes with AddNodesRequest/AddNodesResponse"},
    {"_service_addReferences", (PyCFunction)pyClient_service_addReferences, METH_VARARGS,
     "Add references using UA_Client_Service_addReferences with AddReferencesRequest/AddReferencesResponse"},
    {"_service_deleteNodes", (PyCFunction)pyClient_service_deleteNodes, METH_VARARGS,
     "Delete nodes using UA_Client_Service_deleteNodes with DeleteNodesRequest/DeleteNodesResponse"},
    {"_service_deleteReferences", (PyCFunction)pyClient_service_deleteReferences, METH_VARARGS,
     "Delete references using UA_Client_Service_deleteReferences with DeleteReferencesRequest/DeleteReferencesResponse"},

    /* View */
    {"_service_browse", (PyCFunction)pyClient_service_browse, METH_VARARGS,
     "Browse using UA_Client_Service_browse with BrowseRequest/BrowseResponse"},
    {"_service_browseNext", (PyCFunction)pyClient_service_browseNext, METH_VARARGS,
     "Browse next using UA_Client_Service_browseNext with BrowseNextRequest/BrowseNextResponse"},
    {"_service_translateBrowsePathsToNodeIds", (PyCFunction)pyClient_service_translateBrowsePathsToNodeIds, METH_VARARGS,
     "Translate browse paths using UA_Client_Service_translateBrowsePathsToNodeIds"},
    {"_service_registerNodes", (PyCFunction)pyClient_service_registerNodes, METH_VARARGS,
     "Register nodes using UA_Client_Service_registerNodes with RegisterNodesRequest/RegisterNodesResponse"},
    {"_service_unregisterNodes", (PyCFunction)pyClient_service_unregisterNodes, METH_VARARGS,
     "Unregister nodes using UA_Client_Service_unregisterNodes with UnregisterNodesRequest/UnregisterNodesResponse"},

    /* Query Service Set */
    {"_service_queryFirst", (PyCFunction)pyClient_service_queryFirst, METH_VARARGS,
     "Query first using UA_Client_Service_queryFirst with QueryFirstRequest/QueryFirstResponse"},
    {"_service_queryNext", (PyCFunction)pyClient_service_queryNext, METH_VARARGS,
     "Query next using UA_Client_Service_queryNext with QueryNextRequest/QueryNextResponse"},

    /* Attribute Service Set */
    {"_service_read", (PyCFunction)pyClient_service_read, METH_VARARGS,
     "Read using UA_Client_Service_read with ReadRequest/ReadResponse"},
    {"_service_write", (PyCFunction)pyClient_service_write, METH_VARARGS,
     "Write using UA_Client_Service_write with WriteRequest/WriteResponse"},
    {"_service_historyRead", (PyCFunction)pyClient_service_historyRead, METH_VARARGS,
     "History read using UA_Client_Service_historyRead with HistoryReadRequest/HistoryReadResponse"},
    {"_service_historyUpdate", (PyCFunction)pyClient_service_historyUpdate, METH_VARARGS,
     "History update using UA_Client_Service_historyUpdate with HistoryUpdateRequest/HistoryUpdateResponse"},

    /* Method Service Set */
    {"_service_call", (PyCFunction)pyClient_service_call, METH_VARARGS,
     "Call methods using UA_Client_Service_call with CallRequest/CallResponse"},

    /* MonitoredItem Service Set */
    {"_service_createMonitoredItems_datachange", (PyCFunction)pyClient_monitoredItems_createDataChange, METH_VARARGS,
     "Create monitored items for data change notifications"},
    {"_service_createMonitoredItems_event", (PyCFunction)pyClient_monitoredItems_createEvent, METH_VARARGS,
     "Create monitored items for event notifications"},
    {"_service_modifyMonitoredItems", (PyCFunction)pyClient_monitoredItems_modify, METH_VARARGS,
     "Modify monitored items"},
    {"_service_setMonitoringMode", (PyCFunction)pyClient_monitoredItems_setMonitoringMode, METH_VARARGS,
     "Set monitoring mode using UA_Client_MonitoredItems_setMonitoringMode_async"},
    {"_service_setTriggering", (PyCFunction)pyClient_monitoredItems_setTriggering, METH_VARARGS,
     "Set triggering links"},
    {"_service_deleteMonitoredItems", (PyCFunction)pyClient_monitoredItems_delete, METH_VARARGS,
     "Delete monitored items"},

    /* Subscriptions Service Set */
    {"_service_createSubscription", (PyCFunction)pyClient_subscriptions_create, METH_VARARGS,
     "Create subscription using UA_Client_Subscriptions_create"},
    {"_service_modifySubscription", (PyCFunction)pyClient_subscriptions_modify, METH_VARARGS,
     "Modify subscription using UA_Client_Subscriptions_modify_async"},
    {"_service_setPublishingMode", (PyCFunction)pyClient_subscriptions_setPublishingMode, METH_VARARGS,
     "Set publishing mode using SetPublishingModeRequest"},
    {"_service_deleteSubscriptions", (PyCFunction)pyClient_subscriptions_delete, METH_VARARGS,
     "Delete subscription using UA_Client_Subscriptions_delete"},
    {NULL, NULL, 0, NULL}
};

static PyTypeObject ClientType = {
    .ob_base = PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "o6.Client",
    .tp_doc = PyDoc_STR("OPC UA Client"),
    .tp_basicsize = sizeof(PyClient),
    .tp_itemsize = 0,
    .tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE | Py_TPFLAGS_HAVE_GC,
    .tp_new = PyType_GenericNew,
    .tp_methods = pyClient_methods,
    .tp_getset = pyClient_getsetters,
    .tp_init = (initproc)pyClient_init,
    .tp_dealloc = (destructor)pyClient_dealloc,
    .tp_traverse = (traverseproc)pyClient_traverse,
    .tp_clear = (inquiry)pyClient_clear_refs,
    .tp_str = (reprfunc)pyClient_str,
    .tp_repr = (reprfunc)pyClient_repr
};

PyObject *pyClientModule(void) {
    if (PyType_Ready(&ClientType) < 0)
        return NULL;
        
    return (PyObject*)&ClientType;
}
