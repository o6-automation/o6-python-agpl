/* Copyright 2026 (c) o6 Automation GmbH */

/* Trampolines a user-supplied o6.HistoryBackend into open62541's
 * UA_HistoryDataBackend high-level API. The low-level index-based API
 * (getDateTimeMatch, firstIndex, lastIndex, resultSize, copyDataValues,
 * getDataValue) is never populated: history_data_backend.h requires it stay
 * NULL wherever getHistoryData is implemented, upstream never falls back
 * from one to the other.
 *
 * The only translation unit in the history feature that touches the Python
 * API - server_history.c stays plain C. One PyHistoryBackendContext is
 * shared by every node that historizes through this backend, the same way
 * the ring backend shares one context across nodes.
 */

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

#include "server.h"
#include "server_history.h"
#include "server_services_util.h"
#include "../module.h"

typedef struct {
    PyObject *pyBackend; /* incref'd o6.HistoryBackend instance */
    PyObject *pyServer;  /* incref'd owning PyServer */
    UA_Boolean paged;
} PyHistoryBackendContext;

/* ==================================================== *
 *                     Conversions                      *
 * ==================================================== */

static PyObject *
historyNodeIdToPython(PyHistoryBackendContext *ctx, const UA_NodeId *nodeId) {
    PyServer *pyServer = (PyServer *)ctx->pyServer;
    return UA2PY(nodeId, &UA_TYPES[UA_TYPES_NODEID], &pyServer->nsMapPy2UA);
}

static PyObject *
historyDataValueToPython(PyHistoryBackendContext *ctx, const UA_DataValue *value) {
    PyServer *pyServer = (PyServer *)ctx->pyServer;
    return UA2PY(value, &UA_TYPES[UA_TYPES_DATAVALUE], &pyServer->nsMapPy2UA);
}

/* A zero UA_DateTime is the OPC UA "unspecified" sentinel - becomes None,
 * not the epoch. Unrelated to _history_read's own INT64_MIN/MAX convention. */
static PyObject *
historyDateTimeToPython(PyHistoryBackendContext *ctx, UA_DateTime dt) {
    if(dt == 0)
        Py_RETURN_NONE;
    PyServer *pyServer = (PyServer *)ctx->pyServer;
    return UA2PY(&dt, &UA_TYPES[UA_TYPES_DATETIME], &pyServer->nsMapPy2UA);
}

static PyObject *
historyTimestampsToReturnToPython(PyHistoryBackendContext *ctx, UA_TimestampsToReturn ttr) {
    PyServer *pyServer = (PyServer *)ctx->pyServer;
    return UA2PY(&ttr, &UA_TYPES[UA_TYPES_TIMESTAMPSTORETURN], &pyServer->nsMapPy2UA);
}

/* A local copy of server_nodes.c's static numericRangeToPython - that one
 * isn't exported. getHistoryData's `range` is a by-value UA_NumericRange
 * (never NULL), dimensionsSize 0 meaning "no restriction". */
static PyObject *
historyRangeToPython(const UA_NumericRange *range) {
    if(range->dimensionsSize == 0)
        Py_RETURN_NONE;
    PyObject *tuple = PyTuple_New((Py_ssize_t)range->dimensionsSize);
    if(!tuple)
        return NULL;
    for(size_t i = 0; i < range->dimensionsSize; i++) {
        PyObject *start = PyLong_FromSize_t(range->dimensions[i].min);
        PyObject *stop = PyLong_FromSize_t(range->dimensions[i].max + 1);
        PyObject *slice = (start && stop) ? PySlice_New(start, stop, Py_None) : NULL;
        Py_XDECREF(start);
        Py_XDECREF(stop);
        if(!slice) {
            Py_DECREF(tuple);
            return NULL;
        }
        PyTuple_SET_ITEM(tuple, (Py_ssize_t)i, slice);
    }
    return tuple;
}

/* nodeId + value, the shape onWrite/insertDataValue/replaceDataValue/
 * updateDataValue all share. NULL on failure, with an exception set. */
static PyObject *
historyNodeIdValueArgs(PyHistoryBackendContext *ctx, const UA_NodeId *nodeId,
                       const UA_DataValue *value) {
    PyObject *pyNodeId = historyNodeIdToPython(ctx, nodeId);
    PyObject *pyValue = historyDataValueToPython(ctx, value);
    PyObject *args = (pyNodeId && pyValue) ? PyTuple_Pack(2, pyNodeId, pyValue) : NULL;
    Py_XDECREF(pyNodeId);
    Py_XDECREF(pyValue);
    return args;
}

/* ==================================================== *
 *                    Calling Python                    *
 * ==================================================== */

/* Consumes `args` (a tuple, NULL propagates as failure) and returns the raw
 * result of pyBackend.method(*args); NULL with an exception set on failure. */
static PyObject *
historyCall(PyObject *pyBackend, const char *method, PyObject *args) {
    if(!args)
        return NULL;
    PyObject *callable = PyObject_GetAttrString(pyBackend, method);
    if(!callable) {
        Py_DECREF(args);
        return NULL;
    }
    PyObject *result = pyServer_invoke_sync_callback(callable, args, NULL);
    Py_DECREF(callable);
    Py_DECREF(args);
    return result;
}

/* Mirrors server_access_control.c's access_control_exception_status: an
 * o6.StatusCodeError propagates as its exact code, anything else is printed
 * and mapped to `fallback`. Only for the per-call trampolines, which must
 * hand open62541 a plain UA_StatusCode - NOT for pyHistoryBackend_python's
 * own install-time failures, which leave the exception in place for
 * server_config.c to see. */
static UA_StatusCode
historyExceptionStatus(UA_StatusCode fallback) {
    UA_StatusCode status = fallback;
    PyObject *type = NULL, *value = NULL, *traceback = NULL;
    PyErr_Fetch(&type, &value, &traceback);
    PyErr_NormalizeException(&type, &value, &traceback);
    if(!value || PyObject_IsInstance(value, pyExc_StatusCode) != 1) {
        PyErr_Restore(type, value, traceback);
        PyErr_Print();
        return status;
    }
    PyObject *code = PyObject_GetAttrString(value, "code");
    if(code) {
        unsigned long raw = PyLong_AsUnsignedLong(code);
        if(!PyErr_Occurred())
            status = (UA_StatusCode)raw;
        Py_DECREF(code);
    }
    Py_XDECREF(type);
    Py_XDECREF(value);
    Py_XDECREF(traceback);
    PyErr_Clear();
    return status;
}

static UA_StatusCode
historyCallStatus(PyObject *pyBackend, const char *method, PyObject *args,
                  UA_StatusCode fallback) {
    PyObject *result = historyCall(pyBackend, method, args);
    if(!result)
        return historyExceptionStatus(fallback);
    Py_DECREF(result);
    return UA_STATUSCODE_GOOD;
}

static UA_Boolean
historyCallBool(PyObject *pyBackend, const char *method, PyObject *args) {
    PyObject *result = historyCall(pyBackend, method, args);
    if(!result) {
        PyErr_Print();
        return false;
    }
    int truth = PyObject_IsTrue(result);
    Py_DECREF(result);
    if(truth < 0)
        PyErr_Print();
    return truth > 0;
}

/* ==================================================== *
 *                      Trampolines                     *
 * ==================================================== */

static void
pyHistoryDeleteMembers(UA_HistoryDataBackend *backend) {
    if(!backend || !backend->context)
        return;
    assertGIL();
    PyHistoryBackendContext *ctx = (PyHistoryBackendContext *)backend->context;
    Py_XDECREF(ctx->pyBackend);
    Py_XDECREF(ctx->pyServer);
    UA_free(ctx);
    memset(backend, 0, sizeof(UA_HistoryDataBackend));
}

int
pyHistoryBackend_traverse(UA_HistoryDataBackend *backend, visitproc visit, void *arg) {
    if(backend->deleteMembers == pyHistoryDeleteMembers && backend->context) {
        PyHistoryBackendContext *ctx = (PyHistoryBackendContext *)backend->context;
        Py_VISIT(ctx->pyBackend);
        Py_VISIT(ctx->pyServer);
    }
    return 0;
}

static UA_StatusCode
pyHistoryOnWrite(UA_Server *server, void *hdbContext,
                 const UA_NodeId *sessionId, void *sessionContext,
                 const UA_NodeId *nodeId, UA_Boolean historizing,
                 const UA_DataValue *value) {
    (void)server;
    (void)sessionContext;
    assertGIL();
    /* Mirrors the ring backend: a session-driven write to a node whose
     * Historizing attribute is off is not recorded; a poll/gathering-
     * internal call (sessionId NULL) always is. */
    if(sessionId != NULL && !historizing)
        return UA_STATUSCODE_GOOD;

    PyHistoryBackendContext *ctx = (PyHistoryBackendContext *)hdbContext;
    PyObject *args = historyNodeIdValueArgs(ctx, nodeId, value);
    if(!args)
        return historyExceptionStatus(UA_STATUSCODE_BADINTERNALERROR);
    return historyCallStatus(ctx->pyBackend, "onWrite", args, UA_STATUSCODE_BADINTERNALERROR);
}

static UA_Boolean
pyHistoryBoundSupported(UA_Server *server, void *hdbContext,
                        const UA_NodeId *sessionId, void *sessionContext,
                        const UA_NodeId *nodeId) {
    (void)server;
    (void)sessionId;
    (void)sessionContext;
    assertGIL();
    PyHistoryBackendContext *ctx = (PyHistoryBackendContext *)hdbContext;
    PyObject *pyNodeId = historyNodeIdToPython(ctx, nodeId);
    PyObject *args = pyNodeId ? PyTuple_Pack(1, pyNodeId) : NULL;
    Py_XDECREF(pyNodeId);
    if(!args) {
        PyErr_Print();
        return false;
    }
    return historyCallBool(ctx->pyBackend, "boundSupported", args);
}

static UA_Boolean
pyHistoryTimestampsToReturnSupported(UA_Server *server, void *hdbContext,
                                     const UA_NodeId *sessionId,
                                     void *sessionContext,
                                     const UA_NodeId *nodeId,
                                     const UA_TimestampsToReturn timestampsToReturn) {
    (void)server;
    (void)sessionId;
    (void)sessionContext;
    assertGIL();
    PyHistoryBackendContext *ctx = (PyHistoryBackendContext *)hdbContext;
    PyObject *pyNodeId = historyNodeIdToPython(ctx, nodeId);
    PyObject *pyTtr = historyTimestampsToReturnToPython(ctx, timestampsToReturn);
    PyObject *args = (pyNodeId && pyTtr) ? PyTuple_Pack(2, pyNodeId, pyTtr) : NULL;
    Py_XDECREF(pyNodeId);
    Py_XDECREF(pyTtr);
    if(!args) {
        PyErr_Print();
        return false;
    }
    return historyCallBool(ctx->pyBackend, "timestampsToReturnSupported", args);
}

static UA_StatusCode
pyHistoryGetHistoryData(UA_Server *server, const UA_NodeId *sessionId,
                        void *sessionContext, const UA_HistoryDataBackend *backend,
                        const UA_DateTime start, const UA_DateTime end,
                        const UA_NodeId *nodeId, size_t maxSizePerResponse,
                        UA_UInt32 numValuesPerNode, UA_Boolean returnBounds,
                        UA_TimestampsToReturn timestampsToReturn,
                        UA_NumericRange range, UA_Boolean releaseContinuationPoints,
                        const UA_ByteString *continuationPoint,
                        UA_ByteString *outContinuationPoint, UA_HistoryData *result) {
    (void)server;
    (void)sessionId;
    (void)sessionContext;
    assertGIL();
    if(outContinuationPoint)
        UA_ByteString_init(outContinuationPoint);

    PyHistoryBackendContext *ctx = (PyHistoryBackendContext *)backend->context;
    PyObject *pyNodeId = historyNodeIdToPython(ctx, nodeId);
    PyObject *pyStart = historyDateTimeToPython(ctx, start);
    PyObject *pyEnd = historyDateTimeToPython(ctx, end);
    PyObject *pyTtr = historyTimestampsToReturnToPython(ctx, timestampsToReturn);
    PyObject *pyRange = historyRangeToPython(&range);
    PyObject *args = NULL;
    if(pyNodeId && pyStart && pyEnd && pyTtr && pyRange)
        args = Py_BuildValue("OOOnIOOO", pyNodeId, pyStart, pyEnd,
                             (Py_ssize_t)maxSizePerResponse, (unsigned int)numValuesPerNode,
                             returnBounds ? Py_True : Py_False, pyTtr, pyRange);
    Py_XDECREF(pyNodeId);
    Py_XDECREF(pyStart);
    Py_XDECREF(pyEnd);
    Py_XDECREF(pyTtr);
    Py_XDECREF(pyRange);
    if(!args)
        return historyExceptionStatus(UA_STATUSCODE_BADINTERNALERROR);

    const char *method = "getHistoryData";
    if(ctx->paged) {
        PyObject *token = PyBytes_FromStringAndSize(
            (const char *)continuationPoint->data, (Py_ssize_t)continuationPoint->length);
        PyObject *session = sessionId ? historyNodeIdToPython(ctx, sessionId) : Py_NewRef(Py_None);
        PyObject *extra = token && session ? PyTuple_Pack(
            3, token, releaseContinuationPoints ? Py_True : Py_False, session) : NULL;
        Py_XDECREF(token);
        Py_XDECREF(session);
        PyObject *pagedArgs = extra ? PySequence_Concat(args, extra) : NULL;
        Py_XDECREF(extra);
        Py_DECREF(args);
        args = pagedArgs;
        if(!args)
            return historyExceptionStatus(UA_STATUSCODE_BADINTERNALERROR);
        method = "getHistoryPage";
    } else if(continuationPoint->length || releaseContinuationPoints) {
        Py_DECREF(args);
        return continuationPoint->length ? UA_STATUSCODE_BADCONTINUATIONPOINTINVALID : UA_STATUSCODE_GOOD;
    }

    PyObject *pyResult = historyCall(ctx->pyBackend, method, args);
    if(!pyResult)
        return historyExceptionStatus(UA_STATUSCODE_BADHISTORYOPERATIONUNSUPPORTED);
    PyObject *sequence = pyResult;
    if(ctx->paged) {
        if(!PyTuple_Check(pyResult) || PyTuple_GET_SIZE(pyResult) != 2 ||
           !PyBytes_Check(PyTuple_GET_ITEM(pyResult, 1))) {
            Py_DECREF(pyResult);
            PyErr_SetString(PyExc_TypeError, "getHistoryPage() must return (dataValues, bytes)");
            return historyExceptionStatus(UA_STATUSCODE_BADINTERNALERROR);
        }
        sequence = PyTuple_GET_ITEM(pyResult, 0);
    }
    PyObject *fast = PySequence_Fast(sequence, "history data must be a sequence");
    if(!fast) {
        Py_DECREF(pyResult);
        return historyExceptionStatus(UA_STATUSCODE_BADINTERNALERROR);
    }
    Py_ssize_t count = PySequence_Fast_GET_SIZE(fast);

    PyServer *pyServer = (PyServer *)ctx->pyServer;
    const UA_NamespaceMapping *nsMapping = &pyServer->nsMapPy2UA;
    const UA_DataTypeArray *customDataTypes =
        UA_Server_getConfig(pyServer->server)->customDataTypes;
    UA_DataValue *values =
        (UA_DataValue *)UA_Array_new((size_t)count, &UA_TYPES[UA_TYPES_DATAVALUE]);
    if(!values && count) {
        Py_DECREF(fast);
        Py_DECREF(pyResult);
        return UA_STATUSCODE_BADOUTOFMEMORY;
    }
    for(Py_ssize_t i = 0; i < count; i++) {
        PyObject *item = PySequence_Fast_GET_ITEM(fast, i);
        if(!PY2UA(item, &values[i], &UA_TYPES[UA_TYPES_DATAVALUE], nsMapping,
                  customDataTypes)) {
            Py_DECREF(fast);
            Py_DECREF(pyResult);
            UA_Array_delete(values, (size_t)count, &UA_TYPES[UA_TYPES_DATAVALUE]);
            return historyExceptionStatus(UA_STATUSCODE_BADINTERNALERROR);
        }
    }
    Py_DECREF(fast);
    if(ctx->paged && outContinuationPoint) {
        PyObject *token = PyTuple_GET_ITEM(pyResult, 1);
        UA_ByteString borrowed = {(size_t)PyBytes_GET_SIZE(token), (UA_Byte *)PyBytes_AS_STRING(token)};
        UA_StatusCode status = UA_ByteString_copy(&borrowed, outContinuationPoint);
        if(status != UA_STATUSCODE_GOOD) {
            Py_DECREF(pyResult);
            UA_Array_delete(values, (size_t)count, &UA_TYPES[UA_TYPES_DATAVALUE]);
            return status;
        }
    }
    Py_DECREF(pyResult);
    result->dataValuesSize = (size_t)count;
    result->dataValues = values;
    return UA_STATUSCODE_GOOD;
}

/* insertDataValue / replaceDataValue / updateDataValue share one shape:
 * (nodeId, value) -> the same-named Python method. pyHistoryBackend_python
 * only installs one of these when the subclass overrides it, so upstream
 * degrades an unoverridden call to BadHistoryOperationUnsupported itself,
 * without reaching Python. */
#define HISTORY_VALUE_CALLBACK(name, method)                                  \
    static UA_StatusCode                                                      \
    name(UA_Server *server, void *hdbContext, const UA_NodeId *sessionId,     \
        void *sessionContext, const UA_NodeId *nodeId,                       \
        const UA_DataValue *value) {                                          \
        (void)server;                                                         \
        (void)sessionId;                                                      \
        (void)sessionContext;                                                 \
        assertGIL();                                                          \
        PyHistoryBackendContext *ctx = (PyHistoryBackendContext *)hdbContext; \
        PyObject *args = historyNodeIdValueArgs(ctx, nodeId, value);          \
        if(!args)                                                             \
            return historyExceptionStatus(UA_STATUSCODE_BADINTERNALERROR);    \
        return historyCallStatus(ctx->pyBackend, method, args,                \
                                 UA_STATUSCODE_BADHISTORYOPERATIONUNSUPPORTED);\
    }

HISTORY_VALUE_CALLBACK(pyHistoryInsertDataValue, "insertDataValue")
HISTORY_VALUE_CALLBACK(pyHistoryReplaceDataValue, "replaceDataValue")
HISTORY_VALUE_CALLBACK(pyHistoryUpdateDataValue, "updateDataValue")

#undef HISTORY_VALUE_CALLBACK

static UA_StatusCode
pyHistoryRemoveDataValue(UA_Server *server, void *hdbContext,
                         const UA_NodeId *sessionId, void *sessionContext,
                         const UA_NodeId *nodeId, UA_DateTime startTimestamp,
                         UA_DateTime endTimestamp) {
    (void)server;
    (void)sessionId;
    (void)sessionContext;
    assertGIL();
    PyHistoryBackendContext *ctx = (PyHistoryBackendContext *)hdbContext;
    PyObject *pyNodeId = historyNodeIdToPython(ctx, nodeId);
    PyObject *pyStart = historyDateTimeToPython(ctx, startTimestamp);
    PyObject *pyEnd = historyDateTimeToPython(ctx, endTimestamp);
    PyObject *args =
        (pyNodeId && pyStart && pyEnd) ? PyTuple_Pack(3, pyNodeId, pyStart, pyEnd) : NULL;
    Py_XDECREF(pyNodeId);
    Py_XDECREF(pyStart);
    Py_XDECREF(pyEnd);
    if(!args)
        return historyExceptionStatus(UA_STATUSCODE_BADINTERNALERROR);
    return historyCallStatus(ctx->pyBackend, "removeDataValue", args,
                             UA_STATUSCODE_BADHISTORYOPERATIONUNSUPPORTED);
}

/* ==================================================== *
 *                       Install                        *
 * ==================================================== */

static int
overriddenContains(PyObject *overridden, const char *name) {
    PyObject *key = PyUnicode_FromString(name);
    if(!key)
        return -1;
    int contains = PySet_Contains(overridden, key);
    Py_DECREF(key);
    return contains;
}

UA_HistoryDataBackend
pyHistoryBackend_python(void *pyBackendRaw, void *pyServerRaw) {
    UA_HistoryDataBackend backend;
    memset(&backend, 0, sizeof(backend));

    PyObject *pyBackend = (PyObject *)pyBackendRaw;
    PyObject *pyServer = (PyObject *)pyServerRaw;

    PyObject *overridden = PyObject_CallMethod(pyBackend, "_overridden_callbacks", NULL);
    if(!overridden)
        return backend; /* exception already set - caller must not clear it */
    if(!PyAnySet_Check(overridden)) {
        Py_DECREF(overridden);
        PyErr_SetString(PyExc_TypeError,
                        "HistoryBackend._overridden_callbacks() must return a set");
        return backend;
    }

    int hasPage = overriddenContains(overridden, "getHistoryPage");
    int hasInsert = overriddenContains(overridden, "insertDataValue");
    int hasReplace = overriddenContains(overridden, "replaceDataValue");
    int hasUpdate = overriddenContains(overridden, "updateDataValue");
    int hasRemove = overriddenContains(overridden, "removeDataValue");
    Py_DECREF(overridden);
    if(hasPage < 0 || hasInsert < 0 || hasReplace < 0 || hasUpdate < 0 || hasRemove < 0)
        return backend; /* exception already set */

    PyHistoryBackendContext *ctx =
        (PyHistoryBackendContext *)UA_calloc(1, sizeof(PyHistoryBackendContext));
    if(!ctx)
        return backend; /* no exception set - caller maps to BADOUTOFMEMORY */
    Py_INCREF(pyBackend);
    Py_INCREF(pyServer);
    ctx->paged = hasPage;
    ctx->pyBackend = pyBackend;
    ctx->pyServer = pyServer;

    backend.context = ctx;
    backend.deleteMembers = pyHistoryDeleteMembers;
    /* Always installed: open62541 calls these with no NULL check
     * (readRaw_service_default), or falls back to the low-level API on NULL
     * (getHistoryData), which this backend never populates - either way a
     * NULL pointer here is a crash, not a graceful BadXxxUnsupported. */
    backend.serverSetHistoryData = pyHistoryOnWrite;
    backend.getHistoryData = pyHistoryGetHistoryData;
    backend.boundSupported = pyHistoryBoundSupported;
    backend.timestampsToReturnSupported = pyHistoryTimestampsToReturnSupported;
    /* Sparse: NULL when not overridden, so upstream answers
     * BadHistoryOperationUnsupported itself without ever reaching Python. */
    backend.insertDataValue = hasInsert ? pyHistoryInsertDataValue : NULL;
    backend.replaceDataValue = hasReplace ? pyHistoryReplaceDataValue : NULL;
    backend.updateDataValue = hasUpdate ? pyHistoryUpdateDataValue : NULL;
    backend.removeDataValue = hasRemove ? pyHistoryRemoveDataValue : NULL;
    return backend;
}
