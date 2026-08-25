/* Copyright 2026 (c) o6 Automation GmbH */
#include "client.h"
#include "../types_internal.h"
#include <open62541/client_highlevel_async.h>

#if defined(_WIN32)
#  include <malloc.h>
#  define UA_STACK_ALLOC(n) ((char*)_alloca(n))
#else
#  define UA_STACK_ALLOC(n) ((char*)__builtin_alloca(n))
#endif

ServiceFuture *
createServiceFuture(PyClient *pyClient, const UA_DataType *responseType, void *extraData) {
    ServiceFuture *sf = UA_calloc(1, sizeof(ServiceFuture));
    if (!sf) {
        PyErr_NoMemory();
        return NULL;
    }

    UA_Client *client = pyClient->client;
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
    sf->pyClient = pyClient;
    Py_INCREF(pyClient);
    return sf;
}

void
serviceFuture_abort_before_return(ServiceFuture *sf) {
    Py_DECREF(sf->future); /* callback-context ownership */
    Py_DECREF(sf->future); /* not-returned caller ownership */
    Py_DECREF(sf->pyClient);
    UA_free(sf);
}

void
serviceFuture_resolve(ServiceFuture *sf, void *response) {
    const UA_NamespaceMapping *nsMapping = &sf->pyClient->nsMapPy2UA;
    PyObject *result = UA2PY(response, sf->responseType, nsMapping);
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
    Py_DECREF(sf->pyClient);
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
    Py_DECREF(sf->pyClient);
    UA_free(sf);
}

void
asyncServiceCallback(UA_Client *client, void *userdata, UA_UInt32 requestId, void *response) {
    ServiceFuture *sf = (ServiceFuture*)userdata;
    /* During teardown clientContext is NULL — just release the future
     * without calling back into Python (unsafe from tp_dealloc/GC). */
    UA_ClientConfig *config = UA_Client_getConfig(client);
    if (!config->clientContext) {
        Py_DECREF(sf->future);
        Py_DECREF(sf->pyClient);
        UA_free(sf);
        return;
    }
    serviceFuture_resolve(sf, response);
}

PyObject *
serviceCallAsync(PyObject *self, PyObject *args, const UA_DataType *requestType, const UA_DataType *responseType) {
    PyClient *pyClient = (PyClient *)self;
    UA_Client *client = pyClient->client;

    if (PyTuple_Size(args) != 1) {
        PyErr_Format(PyExc_TypeError,
                     "Expected 1 argument (%s), got %zd",
                     requestType->typeName, PyTuple_Size(args));
        return NULL;
    }

    PyObject *request_obj = PyTuple_GetItem(args, 0);
    // Allocate the request on the stack via a byte buffer sized to the type
    void *request = UA_STACK_ALLOC(requestType->memSize);
    memset(request, 0, requestType->memSize);
    const UA_NamespaceMapping *nsMapping = &pyClient->nsMapPy2UA;
    UA_ClientConfig *config = UA_Client_getConfig(client);
    PyObject *conv = PY2UA(request_obj, request, requestType, nsMapping, config->customDataTypes);
    if (!conv)
        return NULL;

    ServiceFuture *sf = createServiceFuture(pyClient, responseType, NULL);
    if (!sf) {
        UA_clear(request, requestType);
        return NULL;
    }

    /* One reference belongs to the callback context and one is returned to
     * Python. Save the latter before dispatch: a backend is allowed to invoke
     * the completion callback synchronously and consume sf. */
    PyObject *future = sf->future;
    UA_StatusCode retval = __UA_Client_AsyncService(
        client, request, requestType,
        asyncServiceCallback, responseType, sf, &sf->requestId);
    UA_clear(request, requestType);
    if (retval != UA_STATUSCODE_GOOD) {
        /* No callback will consume the context reference on submission
         * failure, and no future is returned to consume the caller ref. */
        serviceFuture_abort_before_return(sf);
        return PyErr_StatusCode(retval);
    }
    return future;
}
