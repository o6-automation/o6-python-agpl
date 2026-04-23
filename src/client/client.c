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
#include "../utils.h"

static PyObject *
pyClient_get_state(PyClient *self, PyObject *Py_UNUSED(ignored)) {
    UA_StatusCode connectStatus = UA_STATUSCODE_GOOD;
    UA_SecureChannelState cState = 0;
    UA_SessionState sState = 0;

    UA_Client_getState(self->client, &cState, &sState, &connectStatus);
    PyObject *a = PyLong_FromLong(cState);
    PyObject *b = PyLong_FromLong(sState);
    PyObject *c = UA2PY(&connectStatus, &UA_TYPES[UA_TYPES_STATUSCODE]);

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

static void
clientStateCallback(UA_Client *cClient,
                    UA_SecureChannelState channelState,
                    UA_SessionState sessionState,
                    UA_StatusCode connectStatus) {
    UA_ClientConfig *config = UA_Client_getConfig(cClient);
    PyClient *client = (PyClient*)config->clientContext;
    if (client->connectFuture) {
        // The connection was aborted
        if (connectStatus != UA_STATUSCODE_GOOD) {
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
            Py_DECREF(client->connectFuture);
            client->connectFuture = NULL;
        }

        // The connection was successful
        else if (sessionState == UA_SESSIONSTATE_ACTIVATED) {
            PyObject *result = UA2PY(&connectStatus, &UA_TYPES[UA_TYPES_STATUSCODE]);
            PyObject *res = PyObject_CallMethod(client->connectFuture,
                                                "set_result", "O", result);
            Py_XDECREF(result);
            Py_XDECREF(res);
            Py_DECREF(client->connectFuture);
            client->connectFuture = NULL;
        }

        // SecureChannel-only connect (no session requested)
        else if (channelState == UA_SECURECHANNELSTATE_OPEN &&
                 config->noSession) {
            PyObject *result = UA2PY(&connectStatus, &UA_TYPES[UA_TYPES_STATUSCODE]);
            PyObject *res = PyObject_CallMethod(client->connectFuture,
                                                "set_result", "O", result);
            Py_XDECREF(result);
            Py_XDECREF(res);
            Py_DECREF(client->connectFuture);
            client->connectFuture = NULL;
        }

        // Channel closed while a connect was pending (e.g. TCP listen
        // failed during reverse connect) — treat as connection failure.
        else if (channelState == UA_SECURECHANNELSTATE_CLOSED) {
            PyObject *exc = PyObject_CallFunction(
                PyExc_ConnectionError, "s",
                "SecureChannel closed before connection completed");
            if (exc) {
                PyObject *res = PyObject_CallMethod(client->connectFuture,
                                                    "set_exception", "O", exc);
                Py_XDECREF(res);
                Py_DECREF(exc);
            }
            if (PyErr_Occurred())
                PyErr_Clear();
            Py_DECREF(client->connectFuture);
            client->connectFuture = NULL;
        }
    }

    if (client->disconnectFuture) {
        if (channelState == UA_SECURECHANNELSTATE_CLOSED) {
            PyObject *result = UA2PY(&connectStatus, &UA_TYPES[UA_TYPES_STATUSCODE]);
            PyObject *res = PyObject_CallMethod(client->disconnectFuture,
                                                "set_result", "O", result);
            Py_XDECREF(result);
            Py_XDECREF(res);
            Py_DECREF(client->disconnectFuture);
            client->disconnectFuture = NULL;
        }
    }
}

/* Convert a UA_KeyValueMap to a Python dict {str: Any}.
 * Returns a new reference, or NULL on error. */
static PyObject *
keyValueMap_to_pydict(const UA_KeyValueMap payload) {
    PyObject *pyDict = PyDict_New();
    if (!pyDict)
        return NULL;
    for (size_t i = 0; i < payload.mapSize; i++) {
        UA_QualifiedName *key = &payload.map[i].key;
        PyObject *pyKey = PyUnicode_FromStringAndSize(
            (char *)key->name.data, (Py_ssize_t)key->name.length);
        if (!pyKey) {
            Py_DECREF(pyDict);
            return NULL;
        }
        PyObject *pyVal = UA2PY(&payload.map[i].value, &UA_TYPES[UA_TYPES_VARIANT]);
        if (!pyVal) {
            Py_DECREF(pyKey);
            Py_DECREF(pyDict);
            return NULL;
        }
        int rc = PyDict_SetItem(pyDict, pyKey, pyVal);
        Py_DECREF(pyKey);
        Py_DECREF(pyVal);
        if (rc < 0) {
            Py_DECREF(pyDict);
            return NULL;
        }
    }
    return pyDict;
}

/* Invoke a stored Python notification callable with (notification_type, payload_dict).
 * Errors are printed and cleared. */
static void
callNotificationCallback(PyObject *pycb, UA_ApplicationNotificationType type,
                         const UA_KeyValueMap payload) {
    PyObject *pyType = PyLong_FromLong((long)type);
    if (!pyType) {
        PyErr_Clear();
        return;
    }
    PyObject *pyPayload = keyValueMap_to_pydict(payload);
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
clientGlobalNotificationCallback(UA_Client *cClient,
                                  UA_ApplicationNotificationType type,
                                  const UA_KeyValueMap payload) {
    UA_ClientConfig *config = UA_Client_getConfig(cClient);
    PyClient *client = (PyClient *)config->clientContext;
    if (client->globalNotificationCallback)
        callNotificationCallback(client->globalNotificationCallback, type, payload);
}

static void
clientLifecycleNotificationCallback(UA_Client *cClient,
                                    UA_ApplicationNotificationType type,
                                    const UA_KeyValueMap payload) {
    UA_ClientConfig *config = UA_Client_getConfig(cClient);
    PyClient *client = (PyClient *)config->clientContext;
    if (client->lifecycleNotificationCallback)
        callNotificationCallback(client->lifecycleNotificationCallback, type, payload);
}

static void
clientServiceNotificationCallback(UA_Client *cClient,
                                   UA_ApplicationNotificationType type,
                                   const UA_KeyValueMap payload) {
    UA_ClientConfig *config = UA_Client_getConfig(cClient);
    PyClient *client = (PyClient *)config->clientContext;
    if (client->serviceNotificationCallback)
        callNotificationCallback(client->serviceNotificationCallback, type, payload);
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
clientSubscriptionInactivityCallback(UA_Client *cClient, UA_UInt32 subId,
                                     void *subContext) {
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

static PyObject *
pyClient_connect(PyClient *self, PyObject *args) {
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
    
    UA_StatusCode status = UA_Client_connectAsync(client, NULL);
    if (status != UA_STATUSCODE_GOOD) {
        Py_DECREF(self->connectFuture);
        self->connectFuture = NULL;
        return PyErr_StatusCode(status);
    }

    Py_INCREF(self->connectFuture);
    return self->connectFuture;
}

static PyObject *
pyClient_disconnect(PyClient *self, PyObject *args) {
    // If we are still connecting, abort
    UA_Client *client = self->client;
    if (self->connectFuture) {
        PyObject *exc =
            PyObject_CallFunction(PyExc_RuntimeError, "s",
                                  "The client was disconnected before "
                                  "completely connecting");
        PyObject *res =
            PyObject_CallMethod(self->connectFuture, "set_exception", "O", exc);
        Py_DECREF(self->connectFuture);
        Py_XDECREF(res);
        Py_XDECREF(exc);
        self->connectFuture = NULL;
    }

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
    Py_INCREF(self->disconnectFuture);

    // Begin to disconnect and return
    UA_Client_disconnectAsync(client);
    return self->disconnectFuture;
}

static PyObject *
pyClient_connect_secure_channel(PyClient *self, PyObject *args) {
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

    // UA_Client_connectSecureChannelAsync sets noSession=true internally,
    // then calls __UA_Client_connect. We cannot set noSession from Python
    // because UA_Client_connectAsync resets it to false.
    UA_StatusCode status = UA_Client_connectSecureChannelAsync(client, NULL);
    if (status != UA_STATUSCODE_GOOD) {
        Py_DECREF(self->connectFuture);
        self->connectFuture = NULL;
        return PyErr_StatusCode(status);
    }

    Py_INCREF(self->connectFuture);
    return self->connectFuture;
}

static PyObject *
pyClient_disconnect_secure_channel(PyClient *self, PyObject *args) {
    UA_Client *client = self->client;

    // If we are still connecting, abort
    if (self->connectFuture) {
        PyObject *exc =
            PyObject_CallFunction(PyExc_RuntimeError, "s",
                                  "The client was disconnected before "
                                  "completely connecting");
        PyObject *res =
            PyObject_CallMethod(self->connectFuture, "set_exception", "O", exc);
        Py_DECREF(self->connectFuture);
        Py_XDECREF(res);
        Py_XDECREF(exc);
        self->connectFuture = NULL;
    }

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
    Py_INCREF(self->disconnectFuture);

    UA_StatusCode status = UA_Client_disconnectSecureChannelAsync(client);
    if (status != UA_STATUSCODE_GOOD) {
        Py_DECREF(self->disconnectFuture);
        Py_DECREF(self->disconnectFuture);
        self->disconnectFuture = NULL;
        return PyErr_StatusCode(status);
    }

    return self->disconnectFuture;
}

static PyObject *
pyClient_start_reverse_connect(PyClient *self, PyObject *args) {
    unsigned short port;
    PyObject *pyHostnames;
    if (!PyArg_ParseTuple(args, "HO", &port, &pyHostnames))
        return NULL;

    if (!PyList_Check(pyHostnames)) {
        PyErr_SetString(PyExc_TypeError, "hostnames must be a list of strings");
        return NULL;
    }

    Py_ssize_t count = PyList_Size(pyHostnames);
    UA_String *hostnames = (UA_String*)calloc(count, sizeof(UA_String));
    if (!hostnames)
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

    UA_StatusCode status = UA_Client_startListeningForReverseConnect(
        client, hostnames, (size_t)count, (UA_UInt16)port);

    for (Py_ssize_t i = 0; i < count; i++)
        UA_String_clear(&hostnames[i]);
    free(hostnames);

    if (status != UA_STATUSCODE_GOOD) {
        Py_DECREF(self->connectFuture);
        self->connectFuture = NULL;
        return PyErr_StatusCode(status);
    }

    Py_INCREF(self->connectFuture);
    return self->connectFuture;
}

static PyObject *
pyClient_get_session_auth_token(PyClient *self, PyObject *Py_UNUSED(ignored)) {
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

    PyObject *pyToken = UA2PY(&token, &UA_TYPES[UA_TYPES_NODEID]);
    PyObject *pyNonce = UA2PY(&nonce, &UA_TYPES[UA_TYPES_BYTESTRING]);
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

    UA_StatusCode status = UA_Client_activateCurrentSessionAsync(client);
    if (status != UA_STATUSCODE_GOOD) {
        Py_DECREF(self->connectFuture);
        self->connectFuture = NULL;
        return PyErr_StatusCode(status);
    }

    Py_INCREF(self->connectFuture);
    return self->connectFuture;
}

static PyObject *
pyClient_activate_session(PyClient *self, PyObject *args) {
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
    if (PY2UA(pyToken, &token, &UA_TYPES[UA_TYPES_NODEID]) == NULL) {
        PyErr_SetString(PyExc_TypeError, "Invalid authentication token");
        return NULL;
    }

    UA_ByteString nonce;
    UA_ByteString_init(&nonce);
    if (PY2UA(pyNonce, &nonce, &UA_TYPES[UA_TYPES_BYTESTRING]) == NULL) {
        UA_NodeId_clear(&token);
        PyErr_SetString(PyExc_TypeError, "Invalid server nonce");
        return NULL;
    }

    UA_Client *client = self->client;
    UA_ClientConfig *config = UA_Client_getConfig(client);
    AsyncIOLoop *el = (AsyncIOLoop*)config->eventLoop;
    self->connectFuture = PyObject_CallMethod(el->pyLoop, "create_future", NULL);
    if (!self->connectFuture) {
        UA_NodeId_clear(&token);
        UA_ByteString_clear(&nonce);
        PyErr_SetString(PyExc_RuntimeError, "Could not create the connect future");
        return NULL;
    }

    UA_StatusCode status = UA_Client_activateSessionAsync(client, token, nonce);
    UA_NodeId_clear(&token);
    UA_ByteString_clear(&nonce);

    if (status != UA_STATUSCODE_GOOD) {
        Py_DECREF(self->connectFuture);
        self->connectFuture = NULL;
        return PyErr_StatusCode(status);
    }

    Py_INCREF(self->connectFuture);
    return self->connectFuture;
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
    unsigned short index;
    if (!PyArg_ParseTuple(args, "H", &index))
        return NULL;
    PyClient *pyClient = (PyClient *)self;
    UA_String nsUri;
    UA_String_init(&nsUri);
    UA_StatusCode status = UA_Client_getNamespaceUri(pyClient->client, (UA_UInt16)index, &nsUri);
    if (status != UA_STATUSCODE_GOOD) {
        UA_String_clear(&nsUri);
        return PyErr_StatusCode(status);
    }
    PyObject *result = UA2PY(&nsUri, &UA_TYPES[UA_TYPES_STRING]);
    UA_String_clear(&nsUri);
    return result;
}

PyObject *
pyClient_get_namespace_index(PyObject *self, PyObject *args) {
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
pyClient_add_namespace(PyObject *self, PyObject *args) {
    const char *uri_data;
    Py_ssize_t uri_len;
    if (!PyArg_ParseTuple(args, "s#", &uri_data, &uri_len))
        return NULL;
    PyClient *pyClient = (PyClient *)self;
    UA_String nsUri = {.length = (size_t)uri_len, .data = (UA_Byte *)(uintptr_t)uri_data};
    UA_UInt16 outIndex = 0;
    UA_StatusCode status = UA_Client_addNamespace(pyClient->client, nsUri, &outIndex);
    if (status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);
    return PyLong_FromUnsignedLong(outIndex);
}

PyObject *
pyClient_find_data_type(PyObject *self, PyObject *args) {
    PyObject *nodeId_obj;
    if (!PyArg_ParseTuple(args, "O", &nodeId_obj))
        return NULL;
    PyClient *pyClient = (PyClient *)self;
    UA_NodeId typeId;
    UA_NodeId_init(&typeId);
    if (PY2UA(nodeId_obj, &typeId, &UA_TYPES[UA_TYPES_NODEID]) == NULL)
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
    if (name) { PyDict_SetItemString(d, "type_name", name); Py_DECREF(name); }
    PyObject *tid = UA2PY((void *)&dt->typeId, &UA_TYPES[UA_TYPES_NODEID]);
    if (tid) { PyDict_SetItemString(d, "type_id", tid); Py_DECREF(tid); }
    PyObject *bid = UA2PY((void *)&dt->binaryEncodingId, &UA_TYPES[UA_TYPES_NODEID]);
    if (bid) { PyDict_SetItemString(d, "binary_encoding_id", bid); Py_DECREF(bid); }
    PyObject *kind = PyLong_FromUnsignedLong(dt->typeKind);
    if (kind) { PyDict_SetItemString(d, "type_kind", kind); Py_DECREF(kind); }
    PyObject *ms = PyLong_FromUnsignedLong(dt->membersSize);
    if (ms) { PyDict_SetItemString(d, "members_size", ms); Py_DECREF(ms); }
    return d;
}

static int
pyClient_init(PyClient *self, PyObject *args, PyObject *kwds) {
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
    cc.stateCallback = clientStateCallback;
    self->client = UA_Client_newWithConfig(&cc);
    if (!self->client) {
        PyErr_NoMemory();
        return -1;
    }

    // The context pointer in the client config points to the Python object
    UA_ClientConfig *config = UA_Client_getConfig(self->client);
    config->clientContext = self;

    // Store back-pointer on the event loop for deferred cleanup
    AsyncIOLoop *el = (AsyncIOLoop*)config->eventLoop;
    el->pyClient = self;
    self->deleteme = 0;
    self->owns_loop = 0;

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

    self->linked_type_capsules = PyList_New(0);
    if(!self->linked_type_capsules) {
        UA_Client_delete(self->client);
        self->client = NULL;
        return -1;
    }

    // If endpoint_uri is provided, validate and set it in the config
    if (endpoint_uri) {
        if (!validate_endpoint_uri(endpoint_uri)) {
            PyErr_SetString(PyExc_ValueError, "Invalid endpointUri schema. Expected format: opc.tcp://host:port[/path]");
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
 * Normally called from Python __del__ (tp_finalize) via the _cleanup
 * method, where Python API calls are safe.  Also called from tp_dealloc
 * (via pyClient_full_cleanup) as a fallback if __del__ didn't run, and
 * from TCPProtocol_connection_lost for the deferred-cleanup path. */
static void
pyClient_do_cleanup(PyClient *self) {

    if(!self->client)
        return;

    UA_ClientConfig *config = UA_Client_getConfig(self->client);
    UA_EventLoop *el = NULL;
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

    if(el) {
        el->free(el);
        el = NULL;
    }

    Py_XDECREF(pyLoop);
    pyLoop = NULL;

    if(PyErr_Occurred())
        PyErr_Clear();
}

/* Full cleanup including freeing the Python object.
 * Called from tp_dealloc (fallback if __del__ didn't run) and from
 * TCPProtocol_connection_lost (deferred cleanup for connected GC'd
 * clients). */
void
pyClient_full_cleanup(PyClient *self) {
    pyClient_do_cleanup(self);
    Py_TYPE(self)->tp_free((PyObject *)self);
}

/* Python-callable cleanup method exposed as _cleanup().
 * Called from Python __del__ to eagerly release C resources while
 * Python API calls are still safe.  After this, self->client is NULL
 * so tp_dealloc just calls tp_free. */
static PyObject *
pyClient_cleanup(PyClient *self, PyObject *Py_UNUSED(ignored)) {
    pyClient_do_cleanup(self);
    Py_RETURN_NONE;
}

static void pyClient_clear(PyClient *self) {

    if(!self->client) {
        /* Nothing to clean up — just free */
        Py_TYPE(self)->tp_free((PyObject *)self);
        return;
    }


    self->deleteme = 1;
    UA_Client_disconnectAsync(self->client);

    /* Check whether a deferred disconnect is needed. */
    UA_SecureChannelState channelState = 0;
    UA_Client_getState(self->client, &channelState, NULL, NULL);

    if(self->deleteme &&
       channelState != UA_SECURECHANNELSTATE_CLOSED) {
        /* Still connected at tp_dealloc time (i.e. __del__ didn't clean
         * up because the client was connected).  The async disconnect is
         * now in flight; defer the actual UA_Client_delete / el->free /
         * tp_free to TCPProtocol_connection_lost which fires once the
         * transport closes. */

        return; /* Do NOT call tp_free — connection_lost will do it */
    }

    /* Fallback path: __del__ already called _cleanup() and self->client
     * would normally be NULL, but handle the edge case where it isn't.
     * Mark tearingDown so that AsyncIOTCP_eventSourceStop skips Python
     * API calls (we are inside tp_dealloc / GC sweep). */
    if(self->client) {
        UA_ClientConfig *config = UA_Client_getConfig(self->client);
        if(config && config->eventLoop)
            ((AsyncIOLoop*)config->eventLoop)->tearingDown = 1;
    }
    pyClient_full_cleanup(self);
}

static PyObject *pyClient_str(PyClient *self) {
    return PyUnicode_FromFormat("o6._o6.Client(%p)", self);
}

static PyObject *
pyClient_set_owns_loop(PyClient *self, PyObject *args) {
    int owns;
    if(!PyArg_ParseTuple(args, "p", &owns))
        return NULL;
    self->owns_loop = owns;
    Py_RETURN_NONE;
}

static PyObject *pyClient_repr(PyClient *self) {
    if (!self->client)
        return PyUnicode_FromString("o6._o6.Client(uninitialized)");
    UA_ClientConfig *config = UA_Client_getConfig(self->client);
    UA_SecureChannelState channelState = 0;
    UA_Client_getState(self->client, &channelState, NULL, NULL);
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
    return PyClientConfig_New(self);
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
    {"connect", (PyCFunction)pyClient_connect, METH_VARARGS, "Connect to OPC UA server using configured endpointUrl"},
    {"disconnect", (PyCFunction)pyClient_disconnect, METH_VARARGS, "Disconnect the client"},
    {"connect_secure_channel", (PyCFunction)pyClient_connect_secure_channel, METH_VARARGS, "Connect SecureChannel only (no session)"},
    {"disconnect_secure_channel", (PyCFunction)pyClient_disconnect_secure_channel, METH_VARARGS, "Disconnect only the secure channel (no CloseSession)"},
    {"start_reverse_connect", (PyCFunction)pyClient_start_reverse_connect, METH_VARARGS, "Start listening for reverse connections"},
    {"get_session_auth_token", (PyCFunction)pyClient_get_session_auth_token, METH_NOARGS, "Get the session authentication token and server nonce"},
    {"activate_current_session", (PyCFunction)pyClient_activate_current_session, METH_VARARGS, "Re-activate the current session"},
    {"activate_session", (PyCFunction)pyClient_activate_session, METH_VARARGS, "Activate a session from another client using auth token and nonce"},
    {"add_timed_callback", (PyCFunction)pyClient_add_timed_callback, METH_VARARGS, "Add a one-shot callback to fire after delay_ms milliseconds"},
    {"add_repeated_callback", (PyCFunction)pyClient_add_repeated_callback, METH_VARARGS, "Add a callback for cyclic repetition at interval_ms"},
    {"change_repeated_callback_interval", (PyCFunction)pyClient_change_repeated_callback_interval, METH_VARARGS, "Change the interval of a repeated callback"},
    {"remove_callback", (PyCFunction)pyClient_remove_callback, METH_VARARGS, "Remove a timed or repeated callback"},
    {"get_namespace_uri", (PyCFunction)pyClient_get_namespace_uri, METH_VARARGS, "Get namespace URI by index"},
    {"get_namespace_index", (PyCFunction)pyClient_get_namespace_index, METH_VARARGS, "Get namespace index by URI"},
    {"add_namespace", (PyCFunction)pyClient_add_namespace, METH_VARARGS, "Add a namespace URI, returns its index"},
    {"find_data_type", (PyCFunction)pyClient_find_data_type, METH_VARARGS, "Look up a DataType by NodeId"},
    {"link_custom_data_types", (PyCFunction)linkClientCustomDataTypes, METH_VARARGS, "Link a pre-built type capsule (from o6._o6.build_custom_data_types) into this client"},
    {"set_global_notification_callback", (PyCFunction)pyClient_set_global_notification_callback, METH_VARARGS, "Set callback for all application notifications: callback(type: int, payload: dict)"},
    {"set_lifecycle_notification_callback", (PyCFunction)pyClient_set_lifecycle_notification_callback, METH_VARARGS, "Set callback for lifecycle notifications: callback(type: int, payload: dict)"},
    {"set_service_notification_callback", (PyCFunction)pyClient_set_service_notification_callback, METH_VARARGS, "Set callback for service notifications: callback(type: int, payload: dict)"},
    {"set_inactivity_callback", (PyCFunction)pyClient_set_inactivity_callback, METH_VARARGS, "Set callback fired when connectivity check gets no response: callback()"},
    {"set_subscription_inactivity_callback", (PyCFunction)pyClient_set_subscription_inactivity_callback, METH_VARARGS, "Set callback fired when a subscription times out: callback(sub_id: int)"},

    /* Raw services
     * ------------
     * Discovery */
    {"_service_find_servers", (PyCFunction)pyClient_find_servers, METH_VARARGS,
     "Get a list of registered servers using FindServersRequest/Response"},
    {"_service_find_servers_on_network", (PyCFunction)pyClient_find_servers_on_network, METH_VARARGS,
     "Get a list of known servers on the network using FindServersOnNetworkRequest/Response (LDS only)"},
    {"_service_get_endpoints", (PyCFunction)pyClient_get_endpoints, METH_VARARGS,
     "Get a list of endpoints from a server using GetEndpointsRequest/Response"},

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
    .tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,
    .tp_new = PyType_GenericNew,
    .tp_methods = pyClient_methods,
    .tp_getset = pyClient_getsetters,
    .tp_init = (initproc)pyClient_init,
    .tp_dealloc = (destructor)pyClient_clear,
    .tp_str = (reprfunc)pyClient_str,
    .tp_repr = (reprfunc)pyClient_repr
};

PyObject *pyClientModule(void) {
    if (PyType_Ready(&ClientType) < 0)
        return NULL;
        
    return (PyObject*)&ClientType;
}
