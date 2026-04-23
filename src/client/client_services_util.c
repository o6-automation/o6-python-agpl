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
#include <open62541/client_highlevel_async.h>

ServiceFuture *
createServiceFuture(UA_Client *client, const UA_DataType *responseType, void *extraData) {
    ServiceFuture *sf = UA_calloc(1, sizeof(ServiceFuture));
    if (!sf) {
        PyErr_NoMemory();
        return NULL;
    }

    UA_ClientConfig *config = UA_Client_getConfig(client);
    AsyncIOLoop *el = (AsyncIOLoop*)config->eventLoop;
    PyObject *fut = PyObject_CallMethod(el->pyLoop, "create_future", NULL);
    if (!fut) {
        PyErr_SetString(PyExc_RuntimeError, "Could not create the service future");
        UA_free(sf);
        return NULL;
    }

    Py_INCREF(fut);

    sf->future = fut;
    sf->responseType = responseType;
    sf->extraData = extraData;
    return sf;
}

void
serviceFuture_resolve(ServiceFuture *sf, void *response) {
    PyObject *result = UA2PY(response, sf->responseType);
    if (result) {
        PyObject *res = PyObject_CallMethod(sf->future, "set_result", "O", result);
        Py_DECREF(result);
        Py_XDECREF(res);
    } else {
        // UA2PY failed — forward the current Python exception to the future
        serviceFuture_reject(sf);
        return; // sf already freed by reject
    }
    Py_DECREF(sf->future);
    UA_free(sf);
}

void
serviceFuture_reject(ServiceFuture *sf) {
    // Fetch the current exception (if any) and set it on the future
    PyObject *ptype, *pvalue, *ptraceback;
    PyErr_Fetch(&ptype, &pvalue, &ptraceback);
    if (pvalue) {
        PyObject *res = PyObject_CallMethod(sf->future, "set_exception", "O", pvalue);
        Py_XDECREF(res);
    } else {
        // No exception pending — set a generic RuntimeError
        PyObject *exc = PyObject_CallFunction(PyExc_RuntimeError, "s",
                                              "Async service call failed");
        PyObject *res = PyObject_CallMethod(sf->future, "set_exception", "O", exc);
        Py_XDECREF(res);
        Py_XDECREF(exc);
    }
    Py_XDECREF(ptype);
    Py_XDECREF(pvalue);
    Py_XDECREF(ptraceback);
    Py_DECREF(sf->future);
    UA_free(sf);
}

void
asyncServiceCallback(UA_Client *client, void *userdata,
                     UA_UInt32 requestId, void *response) {
    ServiceFuture *sf = (ServiceFuture*)userdata;
    /* During teardown clientContext is NULL — just release the future
     * without calling back into Python (unsafe from tp_dealloc/GC). */
    UA_ClientConfig *config = UA_Client_getConfig(client);
    if (!config->clientContext) {
        Py_DECREF(sf->future);
        UA_free(sf);
        return;
    }
    serviceFuture_resolve(sf, response);
}

PyObject *
serviceCallAsync(PyObject *self, PyObject *args,
                 const UA_DataType *requestType,
                 const UA_DataType *responseType) {
    if (PyTuple_Size(args) != 1) {
        PyErr_Format(PyExc_TypeError,
                     "Expected 1 argument (%s), got %zd",
                     requestType->typeName, PyTuple_Size(args));
        return NULL;
    }

    PyObject *request_obj = PyTuple_GetItem(args, 0);
    // Allocate the request on the stack via a byte buffer sized to the type
    void *request = alloca(requestType->memSize);
    memset(request, 0, requestType->memSize);
    PyObject *conv = PY2UA(request_obj, request, requestType);
    if (!conv)
        return NULL;

    UA_Client *client = ((PyClient*)self)->client;
    ServiceFuture *sf = createServiceFuture(client, responseType, NULL);
    if (!sf) {
        UA_clear(request, requestType);
        return NULL;
    }

    UA_StatusCode retval = __UA_Client_AsyncService(
        client, request, requestType,
        asyncServiceCallback, responseType, sf, &sf->requestId);
    UA_clear(request, requestType);
    if (retval != UA_STATUSCODE_GOOD) {
        Py_DECREF(sf->future);
        UA_free(sf);
        return PyErr_StatusCode(retval);
    }
    return sf->future;
}
