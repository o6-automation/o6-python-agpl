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

#include "server.h"
#include "../module.h"
#include "../types_internal.h"
#include "server_services_util.h"
#include "python_nodestore.h"
#include "server/ua_server_internal.h"

#include <limits.h>

typedef struct PyDispatchFrame {
    struct PyDispatchFrame *parent;
    const UA_Node *node; /* Variable or Method whose callback is running */
} PyDispatchFrame;

/* Synchronous callbacks can nest while executing arbitrary Python code. A
 * thread-local stack distinguishes recursion from independent calls on other
 * server threads without allocating per invocation. Suspended async callback
 * execution is deliberately outside this stack once the trampoline returns. */
static O6_THREAD_LOCAL PyDispatchFrame *pyDispatchHead;

typedef struct PyLifecycleErrorFrame {
    struct PyLifecycleErrorFrame *parent;
    PyObject *type;
    PyObject *value;
    PyObject *traceback;
} PyLifecycleErrorFrame;

static O6_THREAD_LOCAL PyLifecycleErrorFrame *pyLifecycleErrorHead;

static void
enterLifecycleErrors(PyLifecycleErrorFrame *frame) {
    memset(frame, 0, sizeof(*frame));
    frame->parent = pyLifecycleErrorHead;
    pyLifecycleErrorHead = frame;
}

static void
leaveLifecycleErrors(PyLifecycleErrorFrame *frame) {
    UA_assert(pyLifecycleErrorHead == frame);
    pyLifecycleErrorHead = frame->parent;
    if(frame->type || frame->value || frame->traceback)
        PyErr_Restore(frame->type, frame->value, frame->traceback);
}

static UA_Boolean
enterDispatch(PyDispatchFrame *frame, const UA_Node *node) {
    UA_assert(frame);
    UA_assert(node);

    for(PyDispatchFrame *current = pyDispatchHead;
        current; current = current->parent) {
        if(current->node == node)
            return false;
    }

    frame->parent = pyDispatchHead;
    frame->node = node;
    pyDispatchHead = frame;
    return true;
}

static void
leaveDispatch(PyDispatchFrame *frame) {
    UA_assert(frame);
    UA_assert(pyDispatchHead == frame);
    pyDispatchHead = frame->parent;
}

static UA_Boolean
isDispatching(const UA_Node *node) {
    for(PyDispatchFrame *current = pyDispatchHead;
        current; current = current->parent) {
        if(current->node == node)
            return true;
    }
    return false;
}

static PyObject *
invokeNodeCallback(PyObject *callback, const UA_Node *node,
                   PyObject *args, PyObject *kwargs,
                   UA_StatusCode *status) {
    PyDispatchFrame dispatch;
    if(!enterDispatch(&dispatch, node)) {
        *status = UA_STATUSCODE_BADINVALIDSTATE;
        return NULL;
    }
    PyObject *result = pyServer_invoke_sync_callback(callback, args, kwargs);
    leaveDispatch(&dispatch);
    if(!result) {
        PyErr_Print();
        *status = UA_STATUSCODE_BADINTERNALERROR;
        return NULL;
    }
    *status = UA_STATUSCODE_GOOD;
    return result;
}


/* ==================================================================== */
/* Server async infrastructure                                          */
/*                                                                      */
/* Mirrors src/client/client_services_util.c.  Each pyServer_*          */
/* function below allocates a ServerAsyncCtx, calls a UA_Server_*_async */
/* function with a callback that resolves/rejects the asyncio Future,   */
/* and returns the Future to Python.                                    */
/* ==================================================================== */

typedef struct {
    PyObject *future;
    int attr_id; /* AttributeId for read callbacks (to know how to convert) */
    UA_Boolean return_write_status;
    UA_Boolean return_call_status;
} ServerAsyncCtx;

static ServerAsyncCtx *
serverAsync_create_ctx(UA_Server *server, int attr_id) {
    ServerAsyncCtx *ctx = UA_calloc(1, sizeof(ServerAsyncCtx));
    if (!ctx) {
        PyErr_NoMemory();
        return NULL;
    }
    UA_ServerConfig *config = UA_Server_getConfig(server);
    AsyncIOLoop *el = (AsyncIOLoop*)config->eventLoop;
    PyObject *fut = PyObject_CallMethod(el->pyLoop, "create_future", NULL);
    if (!fut) {
        UA_free(ctx);
        return NULL;
    }
    Py_INCREF(fut);
    ctx->future = fut;
    ctx->attr_id = attr_id;
    return ctx;
}

static void
serverAsync_resolve(ServerAsyncCtx *ctx, PyObject *result) {
    /* Steals reference to result if non-NULL */
    if (result) {
        /* Use "(O)" so that a tuple `result` is not unpacked as multiple
         * positional args to set_result(). */
        PyObject *r = PyObject_CallMethod(ctx->future, "set_result", "(O)", result);
        Py_DECREF(result);
        Py_XDECREF(r);
    } else {
        /* result conversion failed — set a generic error if no exception */
        PyObject *ptype, *pvalue, *ptraceback;
        PyErr_Fetch(&ptype, &pvalue, &ptraceback);
        if (!pvalue)
            pvalue = PyObject_CallFunction(PyExc_RuntimeError, "s",
                                           "Async server call failed");
        PyObject *r = PyObject_CallMethod(ctx->future, "set_exception", "(O)", pvalue);
        Py_XDECREF(r);
        Py_XDECREF(ptype);
        Py_XDECREF(pvalue);
        Py_XDECREF(ptraceback);
    }
    Py_DECREF(ctx->future);
    UA_free(ctx);
}

static void
serverAsync_reject_status(ServerAsyncCtx *ctx, UA_StatusCode sc) {
    PyObject *code = PyLong_FromUnsignedLong(sc);
    PyObject *exc = code ? PyObject_CallOneArg(pyExc_StatusCode, code) : NULL;
    Py_XDECREF(code);
    if (exc) {
        PyObject *r = PyObject_CallMethod(ctx->future, "set_exception", "(O)", exc);
        Py_XDECREF(r);
        Py_DECREF(exc);
    }
    if (PyErr_Occurred())
        PyErr_Clear();
    Py_DECREF(ctx->future);
    UA_free(ctx);
}

/* Convert a UA_DataValue from a read_async callback into a Python value
 * appropriate for the given AttributeId.  Mirrors the per-attribute
 * conversion the previous synchronous read code performed. */
static PyObject *
serverAsync_convert_read(int attr_id, const UA_DataValue *dv,
                         const UA_NamespaceMapping *nsMapping) {
    if (!dv->hasValue || dv->value.type == NULL) {
        if (attr_id == UA_ATTRIBUTEID_VALUE)
            Py_RETURN_NONE;
        PyErr_SetString(PyExc_RuntimeError, "Server returned no value");
        return NULL;
    }
    /* Value (13) and ArrayDimensions (16) → return the Variant */
    if (attr_id == 13 || attr_id == 16)
        return UA2PY(&dv->value, &UA_TYPES[UA_TYPES_VARIANT], nsMapping);
    /* For every other attribute, the variant carries a single scalar of
     * the matching builtin type — return the unwrapped scalar. */
    return UA2PY(dv->value.data, dv->value.type, nsMapping);
}

static void
serverAsyncReadCallback(UA_Server *server, void *asyncOpContext, const UA_DataValue *result) {
    ServerAsyncCtx *ctx = (ServerAsyncCtx*)asyncOpContext;
    UA_ServerConfig *config = UA_Server_getConfig(server);
    /* Teardown guard: mirror asyncServiceCallback */
    if (!config->context) {
        Py_DECREF(ctx->future);
        UA_free(ctx);
        return;
    }
    assertGIL();
    if (result->hasStatus && !UA_StatusCode_isGood(result->status)) {
        serverAsync_reject_status(ctx, result->status);
        return;
    }
    const UA_NamespaceMapping *nsMapping = &((PyServer *)config->context)->nsMapPy2UA;
    PyObject *py_result = serverAsync_convert_read(ctx->attr_id, result, nsMapping);
    serverAsync_resolve(ctx, py_result);
}

static void
serverAsyncDataValueCallback(UA_Server *server, void *asyncOpContext,
                            const UA_DataValue *result) {
    ServerAsyncCtx *ctx = (ServerAsyncCtx*)asyncOpContext;
    UA_ServerConfig *config = UA_Server_getConfig(server);
    if (!config->context) {
        Py_DECREF(ctx->future);
        UA_free(ctx);
        return;
    }
    assertGIL();
    const UA_NamespaceMapping *nsMapping = &((PyServer *)config->context)->nsMapPy2UA;
    serverAsync_resolve(ctx, UA2PY(result, &UA_TYPES[UA_TYPES_DATAVALUE], nsMapping));
}

static void
serverAsyncWriteCallback(UA_Server *server, void *asyncOpContext, UA_StatusCode result) {
    ServerAsyncCtx *ctx = (ServerAsyncCtx*)asyncOpContext;
    UA_ServerConfig *config = UA_Server_getConfig(server);
    if (!config->context) {
        Py_DECREF(ctx->future);
        UA_free(ctx);
        return;
    }
    assertGIL();
    if (ctx->return_write_status) {
        serverAsync_resolve(ctx, PyLong_FromUnsignedLong(result));
        return;
    }
    if (result != UA_STATUSCODE_GOOD) {
        serverAsync_reject_status(ctx, result);
        return;
    }
    Py_INCREF(Py_None);
    serverAsync_resolve(ctx, Py_None);
}

static PyObject *
serverAsync_write_status(UA_Server *server, UA_StatusCode status, int return_status) {
    if (!return_status)
        return PyErr_StatusCode(status);
    ServerAsyncCtx *ctx = serverAsync_create_ctx(server, 0);
    if (!ctx)
        return NULL;
    ctx->return_write_status = true;
    PyObject *future = ctx->future;
    serverAsyncWriteCallback(server, ctx, status);
    return future;
}

static void
serverAsyncCallCallback(UA_Server *server, void *asyncOpContext, const UA_CallMethodResult *result) {
    ServerAsyncCtx *ctx = (ServerAsyncCtx*)asyncOpContext;
    UA_ServerConfig *config = UA_Server_getConfig(server);
    if (!config->context) {
        Py_DECREF(ctx->future);
        UA_free(ctx);
        return;
    }
    assertGIL();
    if (!ctx->return_call_status && result->statusCode != UA_STATUSCODE_GOOD) {
        serverAsync_reject_status(ctx, result->statusCode);
        return;
    }
    const UA_NamespaceMapping *nsMapping = &((PyServer *)config->context)->nsMapPy2UA;
    /* Preserve every output supplied by the method result, including failures. */
    Py_ssize_t out_count = (Py_ssize_t)result->outputArgumentsSize;
    PyObject *ret = PyTuple_New(1 + out_count);
    if (!ret) {
        serverAsync_resolve(ctx, NULL);
        return;
    }
    PyObject *sc = UA2PY(&result->statusCode, &UA_TYPES[UA_TYPES_STATUSCODE], nsMapping);
    if (!sc) {
        Py_DECREF(ret);
        serverAsync_resolve(ctx, NULL);
        return;
    }
    PyTuple_SET_ITEM(ret, 0, sc);
    for (Py_ssize_t i = 0; i < out_count; i++) {
        PyObject *v = UA2PY(&result->outputArguments[i], &UA_TYPES[UA_TYPES_VARIANT], nsMapping);
        if (!v) {
            Py_DECREF(ret);
            serverAsync_resolve(ctx, NULL);
            return;
        }
        PyTuple_SET_ITEM(ret, 1 + i, v);
    }
    serverAsync_resolve(ctx, ret);
}

/* Convert a Python value into a UA_WriteValue's `value` field for the
 * given AttributeId.  Returns 0 on success, -1 on error (Python
 * exception set).  Caller must clear `wv` regardless.
 * `nsMapping` is the server's Python->UA mapping and is applied to all
 * nested NodeId/QualifiedName/ExtensionObject fields of `py_value`. */
static int
build_write_value(const UA_NodeId *nodeId, UA_Boolean copyNodeId,
                  int attr_id, PyObject *py_value, UA_WriteValue *wv,
                  const UA_NamespaceMapping *nsMapping,
                  const UA_DataTypeArray *customDataTypes) {
    UA_WriteValue_init(wv);
    if(copyNodeId) {
        if(UA_NodeId_copy(nodeId, &wv->nodeId) != UA_STATUSCODE_GOOD) {
            PyErr_NoMemory();
            return -1;
        }
    } else {
        wv->nodeId = *nodeId;
    }
    wv->attributeId = (UA_UInt32)attr_id;
    wv->value.hasValue = true;

    /* Inline the same value-construction logic as the previous synchronous
     * pyServer_write_attribute did, but always wrap the result in
     * wv->value (a UA_DataValue containing a UA_Variant). */
    UA_Variant *var = &wv->value.value;
    UA_Variant_init(var);

    switch (attr_id) {
        case 3: { /* BrowseName */
            UA_QualifiedName qn;
            UA_QualifiedName_init(&qn);
            if (!PY2UA(py_value, &qn, &UA_TYPES[UA_TYPES_QUALIFIEDNAME], nsMapping, customDataTypes))
                return -1;
            UA_StatusCode sc = UA_Variant_setScalarCopy(
                var, &qn, &UA_TYPES[UA_TYPES_QUALIFIEDNAME]);
            UA_QualifiedName_clear(&qn);
            if (sc != UA_STATUSCODE_GOOD) { PyErr_NoMemory(); return -1; }
            break;
        }
        case 4: /* DisplayName */
        case 5: { /* Description */
            UA_LocalizedText lt;
            UA_LocalizedText_init(&lt);
            if (!PY2UA(py_value, &lt, &UA_TYPES[UA_TYPES_LOCALIZEDTEXT], nsMapping, customDataTypes))
                return -1;
            UA_StatusCode sc = UA_Variant_setScalarCopy(
                var, &lt, &UA_TYPES[UA_TYPES_LOCALIZEDTEXT]);
            UA_LocalizedText_clear(&lt);
            if (sc != UA_STATUSCODE_GOOD) { PyErr_NoMemory(); return -1; }
            break;
        }
        case 6: { /* WriteMask */
            PyObject *index = PyNumber_Index(py_value);
            if (!index) return -1;
            unsigned long v = PyLong_AsUnsignedLong(index);
            Py_DECREF(index);
            if (v == (unsigned long)-1 && PyErr_Occurred()) return -1;
            UA_UInt32 vv = (UA_UInt32)v;
            if (UA_Variant_setScalarCopy(var, &vv, &UA_TYPES[UA_TYPES_UINT32])
                != UA_STATUSCODE_GOOD) { PyErr_NoMemory(); return -1; }
            break;
        }
        case 13: { /* Value — move the variant in directly */
            if (!PY2UA(py_value, var, &UA_TYPES[UA_TYPES_VARIANT], nsMapping, customDataTypes))
                return -1;
            break;
        }
        case 14: { /* DataType */
            UA_NodeId dt;
            UA_NodeId_init(&dt);
            if (!PY2UA(py_value, &dt, &UA_TYPES[UA_TYPES_NODEID], nsMapping, customDataTypes))
                return -1;
            UA_StatusCode sc = UA_Variant_setScalarCopy(
                var, &dt, &UA_TYPES[UA_TYPES_NODEID]);
            UA_NodeId_clear(&dt);
            if (sc != UA_STATUSCODE_GOOD) { PyErr_NoMemory(); return -1; }
            break;
        }
        case 15: { /* ValueRank */
            long v = PyLong_AsLong(py_value);
            if (v == -1 && PyErr_Occurred()) return -1;
            UA_Int32 vv = (UA_Int32)v;
            if (UA_Variant_setScalarCopy(var, &vv, &UA_TYPES[UA_TYPES_INT32])
                != UA_STATUSCODE_GOOD) { PyErr_NoMemory(); return -1; }
            break;
        }
        case 16: { /* ArrayDimensions — Variant of UInt32 array */
            if (!PY2UA(py_value, var, &UA_TYPES[UA_TYPES_VARIANT], nsMapping, customDataTypes))
                return -1;
            break;
        }
        case 17: { /* AccessLevel */
            long v = PyLong_AsLong(py_value);
            if (v == -1 && PyErr_Occurred()) return -1;
            UA_Byte vv = (UA_Byte)v;
            if (UA_Variant_setScalarCopy(var, &vv, &UA_TYPES[UA_TYPES_BYTE])
                != UA_STATUSCODE_GOOD) { PyErr_NoMemory(); return -1; }
            break;
        }
        case 19: { /* MinimumSamplingInterval */
            double v = PyFloat_AsDouble(py_value);
            if (v == -1.0 && PyErr_Occurred()) return -1;
            UA_Double vv = (UA_Double)v;
            if (UA_Variant_setScalarCopy(var, &vv, &UA_TYPES[UA_TYPES_DOUBLE])
                != UA_STATUSCODE_GOOD) { PyErr_NoMemory(); return -1; }
            break;
        }
        case 20: /* Historizing */
        case 21: { /* Executable */
            int v = PyObject_IsTrue(py_value);
            if (v < 0) return -1;
            UA_Boolean vv = (UA_Boolean)v;
            if (UA_Variant_setScalarCopy(var, &vv, &UA_TYPES[UA_TYPES_BOOLEAN])
                != UA_STATUSCODE_GOOD) { PyErr_NoMemory(); return -1; }
            break;
        }
        default:
            if (!PY2UA(py_value, var, &UA_TYPES[UA_TYPES_VARIANT], nsMapping, customDataTypes))
                return -1;
            break;
    }
    return 0;
}

PyObject *
pyServer_find_data_type(PyObject *self, PyObject *args) {
    PyObject *nodeId_obj;
    if (!PyArg_ParseTuple(args, "O", &nodeId_obj))
        return NULL;
    PyServer *srv = (PyServer *)self;
    const UA_NamespaceMapping *nsMapping = &srv->nsMapPy2UA;
    const UA_DataTypeArray *customDataTypes =
        UA_Server_getConfig(srv->server)->customDataTypes;

    UA_NodeId typeId;
    UA_NodeId_init(&typeId);
    if (PY2UA(nodeId_obj, &typeId, &UA_TYPES[UA_TYPES_NODEID], nsMapping, customDataTypes) == NULL)
        return NULL;

    const UA_DataType *dt = UA_Server_findDataType(srv->server, &typeId);
    UA_NodeId_clear(&typeId);

    if (!dt)
        Py_RETURN_NONE;

    PyTypeObject *pyType = UA2PYType(dt);
    if (pyType) {
        Py_INCREF(pyType);
        return (PyObject *)pyType;
    }

    PyObject *d = PyDict_New();
    if (!d)
        return NULL;

#ifdef UA_ENABLE_TYPEDESCRIPTION
    PyObject *name = PyUnicode_FromString(dt->typeName ? dt->typeName : "");
#else
    PyObject *name = PyUnicode_FromString("");
#endif
    if (!name)
        goto fail;
    if (PyDict_SetItemString(d, "typeName", name) < 0)
        goto fail_name;
    Py_DECREF(name);

    PyObject *tid = UA2PY(&dt->typeId, &UA_TYPES[UA_TYPES_NODEID], nsMapping);
    if (!tid)
        goto fail;
    if (PyDict_SetItemString(d, "typeId", tid) < 0)
        goto fail_tid;
    Py_DECREF(tid);

    PyObject *bid = UA2PY(&dt->binaryEncodingId, &UA_TYPES[UA_TYPES_NODEID], nsMapping);
    if (!bid)
        goto fail;
    if (PyDict_SetItemString(d, "binaryEncodingId", bid) < 0)
        goto fail_bid;
    Py_DECREF(bid);

    PyObject *kind = PyLong_FromUnsignedLong(dt->typeKind);
    if (!kind)
        goto fail;
    if (PyDict_SetItemString(d, "typeKind", kind) < 0)
        goto fail_kind;
    Py_DECREF(kind);

    PyObject *ms = PyLong_FromUnsignedLong(dt->membersSize);
    if (!ms)
        goto fail;
    if (PyDict_SetItemString(d, "membersSize", ms) < 0)
        goto fail_members;
    Py_DECREF(ms);

    return d;

fail_members:
    Py_DECREF(ms);
fail_kind:
    Py_DECREF(kind);
fail_bid:
    Py_DECREF(bid);
fail_tid:
    Py_DECREF(tid);
fail_name:
    Py_DECREF(name);
fail:
    Py_DECREF(d);
    return NULL;
}

/* 
 * The attribute-only NodeClasses  all funnel through this helper.
 * The only things that differ between NodeClasses are the NodeClass tag and the attributes' UA_DataType.
  */
static PyObject *
add_node_impl(PyServer *srv, UA_NodeClass nodeClass,
              const UA_DataType *attrType,
              PyObject *py_requested, PyObject *py_parent,
              PyObject *py_reftype, PyObject *py_browse,
              PyObject *py_typedef, PyObject *py_attr, UA_Boolean finish) {
    /* A None typedef (passed from Python for type-nodes or a two-phase begin)
     * means "no type definition" -- normalise to C NULL so the optional
     * extract below is skipped, matching the fused wrappers that pass NULL. */
    if (py_typedef == Py_None)
        py_typedef = NULL;
    const UA_NamespaceMapping *nsMapping = &srv->nsMapPy2UA;
    const UA_DataTypeArray *customDataTypes =
        UA_Server_getConfig(srv->server)->customDataTypes;

    UA_NodeId requestedId, parentId, refTypeId, typeDef;
    UA_QualifiedName browseName;
    UA_NodeId_init(&typeDef); /* stays NULL for NodeClasses without a typedef */

    if (extract_nodeid(py_requested, &requestedId, nsMapping, customDataTypes) < 0)
        return NULL;
    if (extract_nodeid(py_parent, &parentId, nsMapping, customDataTypes) < 0)
        goto fail_parent;
    if (extract_nodeid(py_reftype, &refTypeId, nsMapping, customDataTypes) < 0)
        goto fail_reftype;
    if (extract_qualifiedname(py_browse, &browseName, nsMapping, customDataTypes) < 0)
        goto fail_browse;
    if (py_typedef &&
        extract_nodeid(py_typedef, &typeDef, nsMapping, customDataTypes) < 0)
        goto fail_typedef;

    /* Convert the attributes into a zeroed heap buffer of the exact attribute
     * type (VariableAttributes, ObjectAttributes, ...). */
    void *attr = UA_calloc(1, attrType->memSize);
    if (!attr) {
        PyErr_NoMemory();
        goto fail_attr;
    }
    PyObject *conv = PY2UA(py_attr, attr, attrType, nsMapping, customDataTypes);
    if (!conv) {
        UA_free(attr);
        goto fail_attr;
    }

    UA_NodeId outId;
    UA_NodeId_init(&outId);
    PyLifecycleErrorFrame lifecycleErrors;
    enterLifecycleErrors(&lifecycleErrors);
    UA_StatusCode status = UA_Server_addNode_begin(
        srv->server, nodeClass, requestedId, parentId, refTypeId,
        browseName, typeDef, attr, attrType, NULL, &outId);
    if (finish && status == UA_STATUSCODE_GOOD)
        status = UA_Server_addNode_finish(srv->server, outId);
    leaveLifecycleErrors(&lifecycleErrors);

    UA_clear(attr, attrType);
    UA_free(attr);
    UA_NodeId_clear(&typeDef);
    UA_QualifiedName_clear(&browseName);
    UA_NodeId_clear(&refTypeId);
    UA_NodeId_clear(&parentId);
    UA_NodeId_clear(&requestedId);

    if (status != UA_STATUSCODE_GOOD) {
        UA_NodeId_clear(&outId);
        if(PyErr_Occurred())
            return NULL;
        return PyErr_StatusCode(status);
    }

    PyObject *result = UA2PY(&outId, &UA_TYPES[UA_TYPES_NODEID], nsMapping);
    UA_NodeId_clear(&outId);
    return result;

fail_attr:
    UA_NodeId_clear(&typeDef);
fail_typedef:
    UA_QualifiedName_clear(&browseName);
fail_browse:
    UA_NodeId_clear(&refTypeId);
fail_reftype:
    UA_NodeId_clear(&parentId);
fail_parent:
    UA_NodeId_clear(&requestedId);
    return NULL;
}

/* Fused begin+finish -- the original add_node_common behaviour. All the
 * attribute-only NodeClass wrappers below funnel through this unchanged. */
static PyObject *
add_node_common(PyServer *srv, UA_NodeClass nodeClass,
                const UA_DataType *attrType,
                PyObject *py_requested, PyObject *py_parent,
                PyObject *py_reftype, PyObject *py_browse,
                PyObject *py_typedef, PyObject *py_attr) {
    return add_node_impl(srv, nodeClass, attrType, py_requested, py_parent,
                         py_reftype, py_browse, py_typedef, py_attr,
                         true);
}

/* Map an attribute-carrying NodeClass to its UA attributes DataType. Returns
 * NULL for NodeClasses not supported by the generic two-phase add. */
static const UA_DataType *
attr_type_for_nodeclass(UA_NodeClass nodeClass) {
    switch (nodeClass) {
        case UA_NODECLASS_VARIABLE:      return &UA_TYPES[UA_TYPES_VARIABLEATTRIBUTES];
        case UA_NODECLASS_OBJECT:        return &UA_TYPES[UA_TYPES_OBJECTATTRIBUTES];
        case UA_NODECLASS_VARIABLETYPE:  return &UA_TYPES[UA_TYPES_VARIABLETYPEATTRIBUTES];
        case UA_NODECLASS_OBJECTTYPE:    return &UA_TYPES[UA_TYPES_OBJECTTYPEATTRIBUTES];
        case UA_NODECLASS_REFERENCETYPE: return &UA_TYPES[UA_TYPES_REFERENCETYPEATTRIBUTES];
        case UA_NODECLASS_DATATYPE:      return &UA_TYPES[UA_TYPES_DATATYPEATTRIBUTES];
        case UA_NODECLASS_VIEW:          return &UA_TYPES[UA_TYPES_VIEWATTRIBUTES];
        default:                         return NULL;
    }
}

/* ==================================================== *
 *          add_node_begin / add_node_finish            *
 * ==================================================== */
/* Two-phase node add.
 *
 * add_node_begin(nodeclass, requested, parent, reftype, browse, typedef, attr)
 * creates the node with the requested NodeId but does NOT yet instantiate the
 * type's children; it returns the actual NodeId. Between begin and finish the
 * caller may pre-create children with chosen NodeIds/values -- addNode_finish
 * then fills only what is still missing (children are matched by BrowseName, so
 * pre-created ones are kept and never duplicated).
 *
 * add_node_finish(nodeid) completes the instantiation. */
PyObject *
pyServer_add_node_begin(PyObject *self, PyObject *args) {
    int nodeClassInt;
    PyObject *py_requested, *py_parent, *py_reftype,
             *py_browse, *py_typedef, *py_attr;
    if (!PyArg_ParseTuple(args, "iOOOOOO", &nodeClassInt, &py_requested,
                          &py_parent, &py_reftype, &py_browse,
                          &py_typedef, &py_attr))
        return NULL;
    UA_NodeClass nodeClass = (UA_NodeClass)nodeClassInt;
    const UA_DataType *attrType = attr_type_for_nodeclass(nodeClass);
    if (!attrType) {
        PyErr_Format(PyExc_ValueError,
                     "add_node_begin: unsupported node class %d", nodeClassInt);
        return NULL;
    }
    return add_node_impl((PyServer *)self, nodeClass, attrType, py_requested,
                         py_parent, py_reftype, py_browse, py_typedef, py_attr,
                         false);
}

PyObject *
pyServer_add_node_raw(PyObject *self, PyObject *args) {
    int nodeClassInt;
    PyObject *pyRequested, *pyBrowse, *pyTypeDef, *pyAttr, *pyType, *backend;
    if(!PyArg_ParseTuple(args, "iOOOOOO", &nodeClassInt, &pyRequested,
                         &pyBrowse, &pyTypeDef, &pyAttr, &pyType, &backend))
        return NULL;
    UA_NodeClass nodeClass = (UA_NodeClass)nodeClassInt;
    const UA_DataType *attrType = attr_type_for_nodeclass(nodeClass);
    if(!attrType) {
        PyErr_Format(PyExc_ValueError,
                     "add_node_raw: unsupported node class %d", nodeClassInt);
        return NULL;
    }

    PyServer *srv = (PyServer *)self;
    const UA_NamespaceMapping *mapping = &srv->nsMapPy2UA;
    const UA_DataTypeArray *customTypes =
        UA_Server_getConfig(srv->server)->customDataTypes;
    UA_NodeId requested, typeDefinition;
    UA_QualifiedName browseName;
    UA_NodeId_init(&typeDefinition);
    if(extract_nodeid(pyRequested, &requested, mapping, customTypes) < 0)
        return NULL;
    if(extract_qualifiedname(pyBrowse, &browseName, mapping, customTypes) < 0)
        goto failBrowse;
    if(pyTypeDef != Py_None &&
       extract_nodeid(pyTypeDef, &typeDefinition, mapping, customTypes) < 0)
        goto failType;

    void *attr = UA_calloc(1, attrType->memSize);
    if(!attr) {
        PyErr_NoMemory();
        goto failAttr;
    }
    PyObject *converted = PY2UA(pyAttr, attr, attrType, mapping, customTypes);
    if(!converted) {
        UA_free(attr);
        goto failAttr;
    }

    UA_AddNodesItem item;
    UA_AddNodesItem_init(&item);
    item.nodeClass = nodeClass;
    item.requestedNewNodeId.nodeId = requested;
    item.browseName = browseName;
    item.typeDefinition.nodeId = typeDefinition;
    UA_ExtensionObject_setValueNoDelete(&item.nodeAttributes, attr, attrType);
    UA_NodeId outId;
    UA_NodeId_init(&outId);
    lockServer(srv->server);
    UA_StatusCode status = addNode_raw(
        srv->server, &srv->server->adminSession, NULL, &item, &outId);
    PyObject *result = NULL;
    if(status == UA_STATUSCODE_GOOD) {
        const UA_Node *native = UA_NODESTORE_GET(srv->server, &outId);
        if(native) {
            result = pyNodeStore_nodeObject(srv, native, pyType, backend);
            UA_NODESTORE_RELEASE(srv->server, native);
        }
        if(!result) {
            deleteNode(srv->server, outId, true);
            if(!PyErr_Occurred())
                PyErr_SetString(PyExc_RuntimeError,
                                "raw node could not be promoted to Python");
        }
    }
    unlockServer(srv->server);

    UA_NodeId_clear(&outId);
    UA_clear(attr, attrType);
    UA_free(attr);
    UA_NodeId_clear(&typeDefinition);
    UA_QualifiedName_clear(&browseName);
    UA_NodeId_clear(&requested);
    if(status != UA_STATUSCODE_GOOD && !PyErr_Occurred())
        return PyErr_StatusCode(status);
    return result;

failAttr:
    UA_NodeId_clear(&typeDefinition);
failType:
    UA_QualifiedName_clear(&browseName);
failBrowse:
    UA_NodeId_clear(&requested);
    return NULL;
}

PyObject *
pyServer_add_node_prepare(PyObject *self, PyObject *args) {
    PyObject *pyNode, *pyParent, *pyRefType, *pyTypeDef;
    if(!PyArg_ParseTuple(args, "OOOO", &pyNode, &pyParent,
                         &pyRefType, &pyTypeDef))
        return NULL;
    PyServer *srv = (PyServer *)self;
    const UA_NamespaceMapping *mapping = &srv->nsMapPy2UA;
    const UA_DataTypeArray *customTypes =
        UA_Server_getConfig(srv->server)->customDataTypes;
    UA_NodeId nodeId, parentId, refTypeId, typeDefId;
    if(extract_nodeid(pyNode, &nodeId, mapping, customTypes) < 0)
        return NULL;
    if(extract_nodeid(pyParent, &parentId, mapping, customTypes) < 0)
        goto failParent;
    if(extract_nodeid(pyRefType, &refTypeId, mapping, customTypes) < 0)
        goto failRef;
    if(extract_nodeid(pyTypeDef, &typeDefId, mapping, customTypes) < 0)
        goto failTypeDef;

    PyLifecycleErrorFrame lifecycleErrors;
    enterLifecycleErrors(&lifecycleErrors);
    lockServer(srv->server);
    UA_StatusCode status = addNode_prepare(
        srv->server, &srv->server->adminSession, &nodeId, &parentId,
        &refTypeId, &typeDefId);
    unlockServer(srv->server);
    leaveLifecycleErrors(&lifecycleErrors);
    UA_NodeId_clear(&typeDefId);
    UA_NodeId_clear(&refTypeId);
    UA_NodeId_clear(&parentId);
    UA_NodeId_clear(&nodeId);
    if(PyErr_Occurred())
        return NULL;
    if(status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);
    Py_RETURN_NONE;

failTypeDef:
    UA_NodeId_clear(&refTypeId);
failRef:
    UA_NodeId_clear(&parentId);
failParent:
    UA_NodeId_clear(&nodeId);
    return NULL;
}

PyObject *
pyServer_add_node_finish(PyObject *self, PyObject *args) {
    PyObject *py_nodeid;
    if (!PyArg_ParseTuple(args, "O", &py_nodeid))
        return NULL;
    PyServer *srv = (PyServer *)self;
    const UA_NamespaceMapping *nsMapping = &srv->nsMapPy2UA;
    const UA_DataTypeArray *customDataTypes =
        UA_Server_getConfig(srv->server)->customDataTypes;
    UA_NodeId nid;
    if (extract_nodeid(py_nodeid, &nid, nsMapping, customDataTypes) < 0)
        return NULL;
    PyLifecycleErrorFrame lifecycleErrors;
    enterLifecycleErrors(&lifecycleErrors);
    UA_StatusCode status = UA_Server_addNode_finish(srv->server, nid);
    leaveLifecycleErrors(&lifecycleErrors);
    UA_NodeId_clear(&nid);
    if(PyErr_Occurred())
        return NULL;
    if (status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);
    Py_RETURN_NONE;
}

PyObject *
pyServer_set_type_abstract(PyObject *self, PyObject *args) {
    PyObject *py_nodeid;
    int isAbstract;
    if(!PyArg_ParseTuple(args, "Op", &py_nodeid, &isAbstract))
        return NULL;

    PyServer *srv = (PyServer *)self;
    const UA_DataTypeArray *customDataTypes =
        UA_Server_getConfig(srv->server)->customDataTypes;
    UA_NodeId nodeId;
    if(extract_nodeid(py_nodeid, &nodeId, &srv->nsMapPy2UA, customDataTypes) < 0)
        return NULL;

    UA_Node *node = UA_NODESTORE_GET_EDIT(srv->server, &nodeId);
    UA_NodeId_clear(&nodeId);
    if(!node)
        return PyErr_StatusCode(UA_STATUSCODE_BADNODEIDUNKNOWN);

    switch(node->head.nodeClass) {
    case UA_NODECLASS_VARIABLETYPE:
        node->variableTypeNode.isAbstract = (UA_Boolean)isAbstract;
        break;
    case UA_NODECLASS_OBJECTTYPE:
        node->objectTypeNode.isAbstract = (UA_Boolean)isAbstract;
        break;
    default:
        UA_NODESTORE_RELEASE(srv->server, node);
        PyErr_SetString(PyExc_TypeError, "node is not an ObjectType or VariableType");
        return NULL;
    }

    UA_NODESTORE_RELEASE(srv->server, node);
    Py_RETURN_NONE;
}

/* ==================================================== *
 *              add_variable_node                       *
 * ==================================================== */
PyObject *
pyServer_add_variable_node(PyObject *self, PyObject *args) {
    PyObject *py_requested, *py_parent, *py_reftype,
             *py_browse, *py_typedef, *py_attr;
    if (!PyArg_ParseTuple(args, "OOOOOO", &py_requested, &py_parent,
                          &py_reftype, &py_browse, &py_typedef, &py_attr))
        return NULL;
    return add_node_common((PyServer *)self, UA_NODECLASS_VARIABLE,
                           &UA_TYPES[UA_TYPES_VARIABLEATTRIBUTES],
                           py_requested, py_parent, py_reftype, py_browse,
                           py_typedef, py_attr);
}

/* ==================================================== *
 *              add_object_node                         *
 * ==================================================== */
PyObject *
pyServer_add_object_node(PyObject *self, PyObject *args) {
    PyObject *py_requested, *py_parent, *py_reftype,
             *py_browse, *py_typedef, *py_attr;
    if (!PyArg_ParseTuple(args, "OOOOOO", &py_requested, &py_parent,
                          &py_reftype, &py_browse, &py_typedef, &py_attr))
        return NULL;
    return add_node_common((PyServer *)self, UA_NODECLASS_OBJECT,
                           &UA_TYPES[UA_TYPES_OBJECTATTRIBUTES],
                           py_requested, py_parent, py_reftype, py_browse,
                           py_typedef, py_attr);
}

/* ==================================================== *
 *              add_object_type_node                    *
 * ==================================================== */
PyObject *
pyServer_add_object_type_node(PyObject *self, PyObject *args) {
    PyObject *py_requested, *py_parent, *py_reftype, *py_browse, *py_attr;
    if (!PyArg_ParseTuple(args, "OOOOO", &py_requested, &py_parent,
                          &py_reftype, &py_browse, &py_attr))
        return NULL;
    return add_node_common((PyServer *)self, UA_NODECLASS_OBJECTTYPE,
                           &UA_TYPES[UA_TYPES_OBJECTTYPEATTRIBUTES],
                           py_requested, py_parent, py_reftype, py_browse,
                           NULL, py_attr);
}

/* ==================================================== *
 *              add_variable_type_node                  *
 * ==================================================== */
PyObject *
pyServer_add_variable_type_node(PyObject *self, PyObject *args) {
    PyObject *py_requested, *py_parent, *py_reftype,
             *py_browse, *py_typedef, *py_attr;
    if (!PyArg_ParseTuple(args, "OOOOOO", &py_requested, &py_parent,
                          &py_reftype, &py_browse, &py_typedef, &py_attr))
        return NULL;
    return add_node_common((PyServer *)self, UA_NODECLASS_VARIABLETYPE,
                           &UA_TYPES[UA_TYPES_VARIABLETYPEATTRIBUTES],
                           py_requested, py_parent, py_reftype, py_browse,
                           py_typedef, py_attr);
}

/* ==================================================== *
 *              add_data_type_node                      *
 * ==================================================== */
PyObject *
pyServer_add_data_type_node(PyObject *self, PyObject *args) {
    PyObject *py_requested, *py_parent, *py_reftype, *py_browse, *py_attr;
    if (!PyArg_ParseTuple(args, "OOOOO", &py_requested, &py_parent,
                          &py_reftype, &py_browse, &py_attr))
        return NULL;
    return add_node_common((PyServer *)self, UA_NODECLASS_DATATYPE,
                           &UA_TYPES[UA_TYPES_DATATYPEATTRIBUTES],
                           py_requested, py_parent, py_reftype, py_browse,
                           NULL, py_attr);
}

/* ==================================================== *
 *              add_reference_type_node                 *
 * ==================================================== */
PyObject *
pyServer_add_reference_type_node(PyObject *self, PyObject *args) {
    PyObject *py_requested, *py_parent, *py_reftype, *py_browse, *py_attr;
    if (!PyArg_ParseTuple(args, "OOOOO", &py_requested, &py_parent,
                          &py_reftype, &py_browse, &py_attr))
        return NULL;
    return add_node_common((PyServer *)self, UA_NODECLASS_REFERENCETYPE,
                           &UA_TYPES[UA_TYPES_REFERENCETYPEATTRIBUTES],
                           py_requested, py_parent, py_reftype, py_browse,
                           NULL, py_attr);
}

/* ==================================================== *
 *              add_view_node                           *
 * ==================================================== */
PyObject *
pyServer_add_view_node(PyObject *self, PyObject *args) {
    PyObject *py_requested, *py_parent, *py_reftype, *py_browse, *py_attr;
    if (!PyArg_ParseTuple(args, "OOOOO", &py_requested, &py_parent,
                          &py_reftype, &py_browse, &py_attr))
        return NULL;
    return add_node_common((PyServer *)self, UA_NODECLASS_VIEW,
                           &UA_TYPES[UA_TYPES_VIEWATTRIBUTES],
                           py_requested, py_parent, py_reftype, py_browse,
                           NULL, py_attr);
}

/* ==================================================== *
 *       Asynchronous node callback infrastructure      *
 * ==================================================== */

typedef enum {
    ASYNC_OPERATION_PENDING,
    ASYNC_OPERATION_CANCELLED,
    ASYNC_OPERATION_COMPLETED,
} AsyncOperationPhase;

typedef enum {
    ASYNC_OPERATION_CALL,
    ASYNC_OPERATION_READ,
    ASYNC_OPERATION_WRITE,
} AsyncOperationKind;

typedef struct {
    PyObject_HEAD
    void *output;
    size_t outputSize;
    UA_Variant outputDefinitions;
    PyObject *task;
    AsyncOperationPhase phase;
    AsyncOperationKind kind;
    PyServer *pyServer;
    UA_Server *server;
} PyAsyncOperationState;

static PyTypeObject PyAsyncOperationStateType;
static PyObject *PyAsyncOperationState_call(PyObject *self, PyObject *args,
                                            PyObject *kwargs);

static int
PyAsyncOperationState_traverse(PyAsyncOperationState *self, visitproc visit, void *arg) {
    Py_VISIT(self->task);
    return 0;
}

static int
PyAsyncOperationState_clear(PyAsyncOperationState *self) {
    self->phase = ASYNC_OPERATION_CANCELLED;
    self->output = NULL;
    self->server = NULL;
    self->pyServer = NULL;
    UA_Variant_clear(&self->outputDefinitions);
    Py_CLEAR(self->task);
    return 0;
}

static void
PyAsyncOperationState_dealloc(PyAsyncOperationState *self) {
    PyObject_GC_UnTrack(self);
    PyAsyncOperationState_clear(self);
    Py_TYPE(self)->tp_free((PyObject *)self);
}

static PyTypeObject PyAsyncOperationStateType = {
    PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "_o6.AsyncOperationState",
    .tp_basicsize = sizeof(PyAsyncOperationState),
    .tp_dealloc = (destructor)PyAsyncOperationState_dealloc,
    .tp_call = PyAsyncOperationState_call,
    .tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HAVE_GC,
    .tp_traverse = (traverseproc)PyAsyncOperationState_traverse,
    .tp_clear = (inquiry)PyAsyncOperationState_clear,
};

static PyAsyncOperationState *
new_async_operation_state(UA_Server *server, PyServer *pyServer,
                          AsyncOperationKind kind, void *output) {
    PyAsyncOperationState *state =
        PyObject_GC_New(PyAsyncOperationState, &PyAsyncOperationStateType);
    if(!state)
        return NULL;
    state->output = output;
    state->outputSize = 0;
    UA_Variant_init(&state->outputDefinitions);
    state->task = NULL;
    state->phase = ASYNC_OPERATION_PENDING;
    state->kind = kind;
    state->pyServer = pyServer;
    state->server = server;
    PyObject_GC_Track(state);
    return state;
}

static UA_StatusCode
pyVariableReadCallback(UA_Server *server,
                       const UA_NodeId *sessionId, void *sessionContext,
                       const UA_NodeId *nodeId, void *nodeContext,
                       UA_Boolean includeSourceTimeStamp,
                       const UA_NumericRange *range, UA_DataValue *value);

static UA_StatusCode
pyVariableWriteCallback(UA_Server *server, const UA_NodeId *sessionId,
                        void *sessionContext, const UA_NodeId *nodeId, void *nodeContext,
                        const UA_NumericRange *range, const UA_DataValue *value);

static UA_StatusCode statusFromObject(PyObject *statusObj, UA_StatusCode *status);

static UA_StatusCode variableReadResultToOutput(PyServer *pyServer, PyObject *result,
                                                UA_DataValue *value);

static UA_StatusCode variableWriteResultToStatus(PyObject *result);

/*
 * Async call/read/write callback infrastructure
 *
 * Coroutine callbacks run from their initial state in an asyncio.Task.
 * The native callback returns
 * UA_STATUSCODE_GOODCOMPLETESASYNCHRONOUSLY. The GC-tracked state resolves the
 * pending native call, read, or write operation when the Task finishes.
 */

static UA_StatusCode
methodResultToOutput(UA_Server *server, PyObject *result, size_t outputSize,
                     UA_Variant *output, const UA_Variant *definitionsValue,
                     const UA_NamespaceMapping *nsMapping,
                     const UA_DataTypeArray *customDataTypes) {
    if(!PyTuple_Check(result) || PyTuple_GET_SIZE(result) < 1) {
        PyErr_SetString(PyExc_TypeError,
                        "method callback must return (StatusCode, *outputs)");
        return UA_STATUSCODE_BADINTERNALERROR;
    }
    UA_StatusCode status;
    if(statusFromObject(PyTuple_GET_ITEM(result, 0), &status) !=
       UA_STATUSCODE_GOOD)
        return UA_STATUSCODE_BADINTERNALERROR;
    if(UA_StatusCode_isBad(status))
        return status;

    Py_ssize_t count = PyTuple_GET_SIZE(result) - 1;
    if((size_t)count != outputSize) {
        PyErr_Format(PyExc_ValueError,
                     "method callback returned %zd outputs; expected %zu",
                     count, outputSize);
        return UA_STATUSCODE_BADINVALIDARGUMENT;
    }
    const UA_Argument *definitions = NULL;
    size_t definitionsSize = 0;
    if(definitionsValue &&
       definitionsValue->type == &UA_TYPES[UA_TYPES_ARGUMENT]) {
        definitions = (const UA_Argument*)definitionsValue->data;
        definitionsSize = definitionsValue->arrayLength;
        if(definitionsSize == 0 &&
           definitionsValue->data > UA_EMPTY_ARRAY_SENTINEL)
            definitionsSize = 1;
    }
    for(size_t i = 0; i < outputSize; i++) {
        PyObject *item = PyTuple_GET_ITEM(result, (Py_ssize_t)i + 1);
        PyObject *conv = NULL;
        Py_ssize_t itemSize = PySequence_Check(item) ?
            PySequence_Size(item) : -1;
        if(itemSize == 0 && i < definitionsSize &&
           definitions[i].valueRank != UA_VALUERANK_SCALAR) {
            const UA_DataType *elementType = UA_Server_findDataType(
                server, &definitions[i].dataType);
            if(!elementType)
                elementType = &UA_TYPES[UA_TYPES_EXTENSIONOBJECT];
            output[i].type = elementType;
            output[i].data = UA_EMPTY_ARRAY_SENTINEL;
            conv = Py_None;
        }
        if(!conv)
            conv = PY2UA(item, &output[i], &UA_TYPES[UA_TYPES_VARIANT],
                          nsMapping, customDataTypes);
        if(!conv) {
            if(PyErr_ExceptionMatches(PyExc_TypeError))
                PyErr_Format(PyExc_TypeError,
                             "method output %zu cannot be converted to an "
                             "OPC UA native type", i + 1);
            return UA_STATUSCODE_BADINTERNALERROR;
        }
    }
    return status;
}

static void
cancel_async_operation_state(PyAsyncOperationState *state, UA_Boolean serverTeardown) {
    if(state->phase != ASYNC_OPERATION_PENDING)
        return;

    /* open62541 invalidates the output storage as soon as it cancels the
     * operation. Never retain that pointer in a non-pending state. */
    state->phase = ASYNC_OPERATION_CANCELLED;
    state->output = NULL;
    if(serverTeardown) {
        state->server = NULL;
        state->pyServer = NULL;
    }

    if(state->task) {
        PyObject *result = PyObject_CallMethod(
            state->task, "cancel", NULL);
        Py_XDECREF(result);
        if(!result)
            PyErr_Clear();
    }
}

/* The async callback state is itself registered with Task.add_done_callback.
 * Both directions of the state <-> Task cycle are therefore visible to the
 * Python cycle collector. */
static PyObject *
PyAsyncOperationState_call(PyObject *self, PyObject *args, PyObject *kwargs) {
    (void)kwargs;
    PyAsyncOperationState *state = (PyAsyncOperationState *)self;

    assertGIL();
    Py_INCREF(state); /* Releasing server ownership below may drop a reference. */

    if(state->phase == ASYNC_OPERATION_COMPLETED)
        goto cleanup;

    if(state->phase == ASYNC_OPERATION_PENDING) {
        PyObject *task = NULL;
        if(args && PyTuple_Check(args) && PyTuple_GET_SIZE(args) >= 1)
            task = PyTuple_GET_ITEM(args, 0);

        UA_Server *server = state->server;
        PyServer *pyServer = state->pyServer;
        void *output = state->output;
        UA_StatusCode resultStatus = UA_STATUSCODE_GOOD;
        PyObject *pyResult = NULL;

        /* Transition before entering open62541. Completion consumes the
         * output pointer even if the operation was concurrently cancelled. */
        state->phase = ASYNC_OPERATION_COMPLETED;
        state->output = NULL;

        if(task) {
            PyObject *cancelled = PyObject_CallMethod(task, "cancelled", NULL);
            int isCancelled = cancelled ? PyObject_IsTrue(cancelled) : -1;
            Py_XDECREF(cancelled);
            if(isCancelled > 0)
                resultStatus = UA_STATUSCODE_BADREQUESTCANCELLEDBYCLIENT;
            else if(isCancelled < 0) {
                PyErr_Print();
                resultStatus = UA_STATUSCODE_BADINTERNALERROR;
            }
            if(resultStatus == UA_STATUSCODE_GOOD)
                pyResult = PyObject_CallMethod(task, "result", NULL);
        }

        if(!pyResult && resultStatus == UA_STATUSCODE_GOOD) {
            if(PyErr_Occurred())
                PyErr_Print();
            resultStatus = UA_STATUSCODE_BADINTERNALERROR;
        } else if(pyResult) {
            if(state->kind == ASYNC_OPERATION_CALL) {
                const UA_NamespaceMapping *nsMapping =
                    pyServer ? &pyServer->nsMapPy2UA : NULL;
                const UA_DataTypeArray *customDataTypes =
                    server ? UA_Server_getConfig(server)->customDataTypes : NULL;
                resultStatus = methodResultToOutput(
                    server, pyResult, state->outputSize, (UA_Variant *)output,
                    &state->outputDefinitions, nsMapping, customDataTypes);
            } else if(state->kind == ASYNC_OPERATION_READ) {
                resultStatus = variableReadResultToOutput(pyServer, pyResult,
                                                          (UA_DataValue *)output);
            } else {
                resultStatus = variableWriteResultToStatus(pyResult);
            }
            Py_DECREF(pyResult);
            if(PyErr_Occurred())
                PyErr_Print();
        }

        if(server && output) {
            if(state->kind == ASYNC_OPERATION_CALL) {
                UA_Server_setAsyncCallMethodResult(server, (UA_Variant *)output,
                                                   resultStatus);
            } else if(state->kind == ASYNC_OPERATION_READ) {
                UA_DataValue *readOutput = (UA_DataValue *)output;
                if(UA_StatusCode_isBad(resultStatus) && !readOutput->hasStatus) {
                    readOutput->hasStatus = true;
                    readOutput->status = resultStatus;
                }
                UA_Server_setAsyncReadResult(server, readOutput);
            } else {
                UA_Server_setAsyncWriteResult(server, (const UA_DataValue *)output,
                                              resultStatus);
            }

            /* The SDK does not schedule ready-result delivery while STOPPED.
             * Local Python callbacks still run before startup and after stop.
             * Each binding operation owns a distinct ServerAsyncCtx. For an
             * already-ready operation cancelAsync's synchronous path delivers
             * its existing result unchanged and frees the native operation;
             * it does not cancel the completed Python task or other requests. */
            lockServer(server);
            if(server->state == UA_LIFECYCLESTATE_STOPPED) {
                UA_AsyncOperation *ready;
                while((ready = TAILQ_FIRST(&server->asyncManager.readyOps))) {
                    UA_Server_cancelAsync(server, ready->handling.callback.context,
                                          UA_STATUSCODE_GOOD, UA_TRUE);
                }
            }
            unlockServer(server);
        }
    }

cleanup: {
        /* Normal completion and native cancellation release the ownership
         * entry here. Server teardown nulls pyServer and clears the complete
         * ownership list after deleting the native server. */
        PyServer *owner = state->pyServer;
        state->pyServer = NULL;
        state->server = NULL;
        state->output = NULL;
        Py_CLEAR(state->task);
        if(owner)
            pyServer_release_callback_ref(owner, (PyObject *)state);
        Py_DECREF(state);
        Py_RETURN_NONE;
    }
}

static PyAsyncOperationState *
async_operation_state_for_output(PyServer *pyServer, UA_Server *server,
                                 const void *output) {
    if(!pyServer || !pyServer->runtimeCallbackRefs)
        return NULL;
    Py_ssize_t size = PyList_GET_SIZE(pyServer->runtimeCallbackRefs);
    for(Py_ssize_t i = 0; i < size; i++) {
        PyObject *item = PyList_GET_ITEM(pyServer->runtimeCallbackRefs, i);
        if(!PyObject_TypeCheck(item, &PyAsyncOperationStateType))
            continue;
        PyAsyncOperationState *state = (PyAsyncOperationState *)item;
        if(state->phase == ASYNC_OPERATION_PENDING && state->server == server &&
           state->output == output)
            return state;
    }
    return NULL;
}

/* Called by open62541 when an async operation is cancelled (e.g. timeout).
 * `out` is the stable operation pointer passed to the call/read/write callback. */
static void
asyncOperationCancelCallback(UA_Server *server, const void *out) {
    assertGIL();
    UA_ServerConfig *config = UA_Server_getConfig(server);
    PyServer *pyServer = config ? (PyServer *)config->context : NULL;
    PyAsyncOperationState *state =
        async_operation_state_for_output(pyServer, server, out);
    if(state)
        cancel_async_operation_state(state, UA_FALSE);
}

void
clear_server_runtime_callbacks(UA_Server *server, PyServer *py_server) {
    /* Node callbacks are owned by PyNode. Only pending async calls still use
     * the server's general callback ownership list. */
    if(py_server && py_server->runtimeCallbackRefs) {
        Py_ssize_t size = PyList_GET_SIZE(py_server->runtimeCallbackRefs);
        for(Py_ssize_t i = 0; i < size; i++) {
            PyObject *item = PyList_GET_ITEM(py_server->runtimeCallbackRefs, i);
            if(!PyObject_TypeCheck(item, &PyAsyncOperationStateType))
                continue;
            PyAsyncOperationState *state = (PyAsyncOperationState *)item;
            if(state->server == server)
                cancel_async_operation_state(state, UA_TRUE);
        }
    }

    clear_server_monitored_item_callbacks(server);
    clear_server_repeat_callbacks(server);
}

static UA_StatusCode
scheduleAsyncOperation(PyAsyncOperationState *state, PyObject *coroutine) {
    UA_ServerConfig *config = UA_Server_getConfig(state->server);
    if(!config->eventLoop)
        return UA_STATUSCODE_BADNOTIMPLEMENTED;
    AsyncIOLoop *el = (AsyncIOLoop *)config->eventLoop;
    if(el->tearingDown)
        return UA_STATUSCODE_BADSHUTDOWN;

    PyObject *task = PyObject_CallMethod(el->pyLoop, "create_task", "O", coroutine);
    if(!task) {
        PyErr_Print();
        return UA_STATUSCODE_BADINTERNALERROR;
    }
    state->task = task;

    if(pyServer_own_callback_ref(state->pyServer, (PyObject *)state) < 0) {
        cancel_async_operation_state(state, UA_TRUE);
        PyErr_Clear();
        return UA_STATUSCODE_BADOUTOFMEMORY;
    }
    PyObject *registered =
        PyObject_CallMethod(task, "add_done_callback", "O", (PyObject *)state);
    if(!registered) {
        PyServer *owner = state->pyServer;
        cancel_async_operation_state(state, UA_TRUE);
        pyServer_release_callback_ref(owner, (PyObject *)state);
        PyErr_Print();
        return UA_STATUSCODE_BADINTERNALERROR;
    }
    Py_DECREF(registered);
    config->asyncOperationCancelCallback = asyncOperationCancelCallback;
    return UA_STATUSCODE_GOODCOMPLETESASYNCHRONOUSLY;
}

/* C callback that dispatches to Python */
static PyObject *
nodeIdToPython(const UA_NodeId *nodeId, const UA_NamespaceMapping *nsMapping) {
    return UA2PY(nodeId, &UA_TYPES[UA_TYPES_NODEID], nsMapping);
}

static PyObject *callbackObjectNodeType;
static PyObject *callbackSessionType;
static PyObject *callbackStatusCodeType;
static PyObject *callbackDataValueType;

static int
ensureCallbackTypes(void) {
    if(callbackObjectNodeType)
        return 0;
    PyObject *nodeModule = PyImport_ImportModule("o6.node");
    PyObject *serverModule = PyImport_ImportModule("o6.server");
    PyObject *o6Module = PyImport_ImportModule("o6");
    if(!nodeModule || !serverModule || !o6Module)
        goto error;
    callbackObjectNodeType = PyObject_GetAttrString(nodeModule, "ObjectNode");
    callbackSessionType = PyObject_GetAttrString(serverModule, "Session");
    callbackStatusCodeType = PyObject_GetAttrString(o6Module, "StatusCode");
    callbackDataValueType = PyObject_GetAttrString(o6Module, "DataValue");
    Py_DECREF(nodeModule);
    Py_DECREF(serverModule);
    Py_DECREF(o6Module);
    nodeModule = NULL;
    serverModule = NULL;
    o6Module = NULL;
    if(!callbackObjectNodeType || !callbackSessionType ||
       !callbackStatusCodeType || !callbackDataValueType)
        goto error;
    return 0;
error:
    Py_XDECREF(nodeModule);
    Py_XDECREF(serverModule);
    Py_XDECREF(o6Module);
    Py_CLEAR(callbackObjectNodeType);
    Py_CLEAR(callbackSessionType);
    Py_CLEAR(callbackStatusCodeType);
    Py_CLEAR(callbackDataValueType);
    return -1;
}

static PyObject *
callbackSession(PyServer *server, const UA_NodeId *sessionId,
                void *sessionContext) {
    if(UA_NodeId_equal(sessionId,
                       &server->server->adminSession.sessionId))
        return Py_NewRef(Py_None);
    if(ensureCallbackTypes() < 0)
        return NULL;
    PyObject *pySessionId = nodeIdToPython(sessionId, &server->nsMapPy2UA);
    if(!pySessionId)
        return NULL;
    PyObject *context = sessionContext ? (PyObject *)sessionContext : Py_None;
    PyObject *result = PyObject_CallFunctionObjArgs(
        callbackSessionType, (PyObject *)server, pySessionId, context, NULL);
    Py_DECREF(pySessionId);
    return result;
}

static UA_StatusCode
statusFromObject(PyObject *statusObj, UA_StatusCode *status) {
    if(ensureCallbackTypes() < 0)
        return UA_STATUSCODE_BADINTERNALERROR;
    int isStatus = PyObject_IsInstance(statusObj, callbackStatusCodeType);
    if(isStatus <= 0) {
        if(isStatus == 0)
            PyErr_SetString(PyExc_TypeError,
                            "first callback result item must be StatusCode");
        return UA_STATUSCODE_BADINTERNALERROR;
    }
    unsigned long value = PyLong_AsUnsignedLong(statusObj);
    if(PyErr_Occurred())
        return UA_STATUSCODE_BADINTERNALERROR;
    *status = (UA_StatusCode)value;
    return UA_STATUSCODE_GOOD;
}

static UA_StatusCode
statusFromTuple(PyObject *result, Py_ssize_t requiredSize,
                const char *message, UA_StatusCode *status) {
    if(!PyTuple_Check(result) || PyTuple_GET_SIZE(result) != requiredSize) {
        PyErr_SetString(PyExc_TypeError, message);
        return UA_STATUSCODE_BADINTERNALERROR;
    }
    return statusFromObject(PyTuple_GET_ITEM(result, 0), status);
}

static UA_StatusCode
callPythonNodeLifecycle(UA_Server *server, const UA_NodeId *nodeId,
                        void **nodeContext, UA_Boolean early) {
    assertGIL();

    UA_ServerConfig *config = UA_Server_getConfig(server);
    PyServer *pyServer = config ? (PyServer *)config->context : NULL;
    if(!pyServer || pyServer->server != server)
        return UA_STATUSCODE_GOOD;

    /* Namespace zero is constructed inside UA_Server_newWithConfig, before
     * the high-level Python Server has created its node backend. */
    int initialized = PyObject_HasAttrString(
        (PyObject *)pyServer, "_node_backend");
    if(initialized <= 0) {
        if(initialized < 0)
            PyErr_Clear();
        return UA_STATUSCODE_GOOD;
    }

    UA_Node *nativeNode = pyNodeStore_contextNode(pyServer, *nodeContext);
    if(!nativeNode) {
        PyErr_Print();
        return UA_STATUSCODE_BADINTERNALERROR;
    }
    UA_NodeClass nodeClass = nativeNode->head.nodeClass;
    if(nodeClass != UA_NODECLASS_VARIABLE && nodeClass != UA_NODECLASS_OBJECT)
        return UA_STATUSCODE_GOOD;
    UA_NodeId typeId;
    UA_NodeId_init(&typeId);
    UA_StatusCode status = UA_Server_getNodeType(server, *nodeId, &typeId);
    if(status != UA_STATUSCODE_GOOD)
        return status;

    const UA_NamespaceMapping *nsMapping = &pyServer->nsMapPy2UA;
    PyObject *pyNodeId = nodeIdToPython(nodeId, nsMapping);
    PyObject *pyTypeId = nodeIdToPython(&typeId, nsMapping);
    UA_NodeId_clear(&typeId);
    if(!pyNodeId || !pyTypeId) {
        Py_XDECREF(pyNodeId);
        Py_XDECREF(pyTypeId);
        PyErr_Print();
        return UA_STATUSCODE_BADINTERNALERROR;
    }

    /* Python-created raw nodes already carry their final class. Native nodes
     * remain unpromoted here and are represented by None so Python can select
     * their class from the server-local TypeDefinition binding. */
    PyObject *pyNode = pyNodeStore_contextObject(
        pyServer, *nodeContext, NULL, NULL);
    if(!pyNode) {
        PyErr_Clear();
        pyNode = Py_NewRef(Py_None);
    }

    PyObject *result = PyObject_CallMethod(
        (PyObject *)pyServer, "_python_node_lifecycle", "OOOii",
        pyNodeId, pyTypeId, pyNode, (int)nodeClass, (int)early);
    Py_DECREF(pyNodeId);
    Py_DECREF(pyTypeId);
    Py_DECREF(pyNode);
    if(!result) {
        if(pyLifecycleErrorHead && !pyLifecycleErrorHead->type) {
            PyErr_Fetch(&pyLifecycleErrorHead->type,
                        &pyLifecycleErrorHead->value,
                        &pyLifecycleErrorHead->traceback);
        } else {
            PyErr_Print();
        }
        return UA_STATUSCODE_BADINTERNALERROR;
    }
    Py_DECREF(result);
    return UA_STATUSCODE_GOOD;
}

UA_StatusCode
pyGlobalNodeEarlyConstructor(UA_Server *server,
                             const UA_NodeId *sessionId, void *sessionContext,
                             const UA_NodeId *nodeId, void **nodeContext) {
    (void)sessionId;
    (void)sessionContext;
    return callPythonNodeLifecycle(server, nodeId, nodeContext, true);
}

UA_StatusCode
pyGlobalNodeConstructor(UA_Server *server,
                        const UA_NodeId *sessionId, void *sessionContext,
                        const UA_NodeId *nodeId, void **nodeContext) {
    (void)sessionId;
    (void)sessionContext;
    return callPythonNodeLifecycle(server, nodeId, nodeContext, false);
}

static UA_StatusCode
pyMethodCallback(UA_Server *server,
                 const UA_NodeId *sessionId, void *sessionContext,
                 const UA_NodeId *methodId, void *methodContext,
                 const UA_NodeId *objectId, void *objectContext,
                 size_t inputSize, const UA_Variant *input,
                 size_t outputSize, UA_Variant *output) {
    (void)sessionId;
    (void)sessionContext;
    (void)methodId;
    (void)objectId;
    assertGIL();
    if(!methodContext || !objectContext)
        return UA_STATUSCODE_BADINTERNALERROR;
    PyServer *py_server = (PyServer *)UA_Server_getConfig(server)->context;
    if(!py_server || py_server->server != server)
        return UA_STATUSCODE_BADINTERNALERROR;
    PyObject *receiver = NULL;
    PyObject *callback = pyNodeStore_getCallback(
        methodContext, PY_NODE_CALLBACK_CALL, &receiver);
    if(!callback)
        return UA_STATUSCODE_BADNOTIMPLEMENTED;
#define METHOD_RETURN(status) do { \
    Py_DECREF(callback); \
    return (status); \
} while(0)

    const UA_NamespaceMapping *nsMapping = &py_server->nsMapPy2UA;
    const UA_DataTypeArray *customDataTypes =
        UA_Server_getConfig(server)->customDataTypes;

    PyObject *pyObject = receiver;
    if(!pyObject)
        pyObject = pyNodeStore_getMethodOwner(methodContext, objectContext);
    if(!pyObject) {
        if(ensureCallbackTypes() < 0) {
            PyErr_Print();
            METHOD_RETURN(UA_STATUSCODE_BADINTERNALERROR);
        }
        PyObject *backend = PyObject_GetAttrString(
            (PyObject *)py_server, "_node_backend");
        pyObject = backend ? pyNodeStore_contextObject(
            py_server, objectContext, callbackObjectNodeType, backend) : NULL;
        Py_XDECREF(backend);
        if(!pyObject) {
            PyErr_Print();
            METHOD_RETURN(UA_STATUSCODE_BADINTERNALERROR);
        }
    }
    UA_Node *methodNode = pyNodeStore_contextNode(py_server, methodContext);
    if(!methodNode) {
        Py_DECREF(pyObject);
        PyErr_Print();
        METHOD_RETURN(UA_STATUSCODE_BADINTERNALERROR);
    }

    /* The stored callback receives (object, *inputs). */
    PyObject *py_inputs = PyTuple_New((Py_ssize_t)inputSize + 1);
    if(!py_inputs) {
        Py_XDECREF(py_inputs);
        Py_DECREF(pyObject);
        METHOD_RETURN(UA_STATUSCODE_BADINTERNALERROR);
    }
    PyTuple_SET_ITEM(py_inputs, 0, pyObject);
    for(size_t i = 0; i < inputSize; i++) {
        PyObject *val = UA2PY(&input[i], &UA_TYPES[UA_TYPES_VARIANT], nsMapping);
        if(!val) {
            Py_DECREF(py_inputs);
            PyErr_Print();
            METHOD_RETURN(UA_STATUSCODE_BADINTERNALERROR);
        }
        PyTuple_SET_ITEM(py_inputs, (Py_ssize_t)i + 1, val);
    }

    UA_StatusCode invokeStatus;
    PyObject *py_result = invokeNodeCallback(
        callback, methodNode, py_inputs, NULL, &invokeStatus);
    Py_DECREF(py_inputs);
    if(!py_result)
        METHOD_RETURN(invokeStatus);

    if(PyCoro_CheckExact(py_result)) {
        PyAsyncOperationState *asyncState = new_async_operation_state(
            server, py_server, ASYNC_OPERATION_CALL, output);
        if(!asyncState) {
            Py_DECREF(py_result);
            METHOD_RETURN(UA_STATUSCODE_BADOUTOFMEMORY);
        }
        asyncState->outputSize = outputSize;
        UA_StatusCode definitionsStatus = readObjectProperty(
            server, methodNode->head.nodeId, UA_QUALIFIEDNAME(0, "OutputArguments"),
            &asyncState->outputDefinitions);
        if(outputSize > 0 && definitionsStatus != UA_STATUSCODE_GOOD) {
            Py_DECREF(asyncState);
            Py_DECREF(py_result);
            METHOD_RETURN(definitionsStatus);
        }

        UA_StatusCode scheduleStatus = scheduleAsyncOperation(asyncState, py_result);
        Py_DECREF(py_result);
        Py_DECREF(asyncState);
        METHOD_RETURN(scheduleStatus);
    }

    UA_Variant outputDefinitions;
    UA_Variant_init(&outputDefinitions);
    UA_StatusCode definitionsStatus = readObjectProperty(
        server, methodNode->head.nodeId,
        UA_QUALIFIEDNAME(0, "OutputArguments"), &outputDefinitions);
    if(outputSize > 0 && definitionsStatus != UA_STATUSCODE_GOOD) {
        UA_Variant_clear(&outputDefinitions);
        Py_DECREF(py_result);
        METHOD_RETURN(definitionsStatus);
    }
    UA_StatusCode resultStatus = methodResultToOutput(
        server, py_result, outputSize, output, &outputDefinitions,
        nsMapping, customDataTypes);
    UA_Variant_clear(&outputDefinitions);
    Py_DECREF(py_result);
    if(PyErr_Occurred())
        PyErr_Print();
    METHOD_RETURN(resultStatus);
#undef METHOD_RETURN
}

static PyObject *
numericRangeToPython(const UA_NumericRange *range) {
    if(!range)
        Py_RETURN_NONE;
    PyObject *tuple = PyTuple_New((Py_ssize_t)range->dimensionsSize);
    if(!tuple)
        return NULL;
    for(size_t i = 0; i < range->dimensionsSize; i++) {
        PyObject *start = PyLong_FromSize_t(range->dimensions[i].min);
        PyObject *stop = PyLong_FromSize_t(range->dimensions[i].max + 1);
        PyObject *slice = NULL;
        if(start && stop)
            slice = PySlice_New(start, stop, Py_None);
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

static PyObject *
variableCallbackKwargs(PyServer *server, const UA_NodeId *sessionId,
                       void *sessionContext, const UA_NumericRange *range,
                       int includeSourceTimestamp) {
    PyObject *kwargs = PyDict_New();
    PyObject *pyRange = numericRangeToPython(range);
    PyObject *session = callbackSession(server, sessionId, sessionContext);
    if(!kwargs || !pyRange || !session)
        goto error;
    if(PyDict_SetItemString(kwargs, "range", pyRange) < 0 ||
       PyDict_SetItemString(kwargs, "session", session) < 0)
        goto error;
    if(includeSourceTimestamp >= 0 &&
       PyDict_SetItemString(kwargs, "includeSourceTimestamp",
                            includeSourceTimestamp ? Py_True : Py_False) < 0)
        goto error;
    Py_DECREF(pyRange);
    Py_DECREF(session);
    return kwargs;
error:
    Py_XDECREF(kwargs);
    Py_XDECREF(pyRange);
    Py_XDECREF(session);
    return NULL;
}

static PyObject *
callVariableCallback(PyServer *server, void *nodeContext,
                     PyNodeCallbackKind kind, PyObject *value,
                     PyObject *kwargs, UA_StatusCode *status) {
    *status = kind == PY_NODE_CALLBACK_READ ?
        UA_STATUSCODE_BADNOTREADABLE : UA_STATUSCODE_BADNOTWRITABLE;

    PyObject *receiver = NULL;
    PyObject *callback = pyNodeStore_getCallback(
        nodeContext, kind, &receiver);
    if(!callback)
        return NULL;

    PyObject *args = NULL;
    PyObject *node = receiver ? receiver : pyNodeStore_contextObject(
        server, nodeContext, NULL, NULL);
    if(!node)
        goto error;
    args = value ? PyTuple_Pack(2, node, value) : PyTuple_Pack(1, node);
    Py_XDECREF(node);
    if(!args)
        goto error;

    UA_Node *nativeNode = pyNodeStore_contextNode(server, nodeContext);
    if(!nativeNode)
        goto error;

    PyObject *result = invokeNodeCallback(
        callback, nativeNode, args, kwargs, status);
    Py_DECREF(args);
    Py_DECREF(callback);
    return result;

error:
    Py_XDECREF(args);
    Py_DECREF(callback);
    if(PyErr_Occurred())
        PyErr_Print();
    *status = UA_STATUSCODE_BADINTERNALERROR;
    return NULL;
}

static UA_StatusCode
variableReadResultToOutput(PyServer *pyServer, PyObject *result, UA_DataValue *value) {
    const UA_NamespaceMapping *nsMapping = &pyServer->nsMapPy2UA;
    const UA_DataTypeArray *customDataTypes =
        UA_Server_getConfig(pyServer->server)->customDataTypes;
    if(!PyTuple_Check(result) || PyTuple_GET_SIZE(result) < 1) {
        PyErr_SetString(PyExc_TypeError,
                        "Variable read callback must return (StatusCode, value)");
        return UA_STATUSCODE_BADINTERNALERROR;
    }
    UA_StatusCode callbackStatus;
    if(statusFromObject(PyTuple_GET_ITEM(result, 0), &callbackStatus) !=
       UA_STATUSCODE_GOOD)
        return UA_STATUSCODE_BADINTERNALERROR;
    if(UA_StatusCode_isBad(callbackStatus)) {
        if(PyTuple_GET_SIZE(result) != 1) {
            PyErr_SetString(PyExc_TypeError,
                            "a Bad Variable read result cannot contain a value");
            return UA_STATUSCODE_BADINTERNALERROR;
        }
        value->hasStatus = true;
        value->status = callbackStatus;
        return callbackStatus;
    }
    if(PyTuple_GET_SIZE(result) != 2) {
        PyErr_SetString(PyExc_TypeError,
                        "a successful Variable read result requires exactly one value");
        return UA_STATUSCODE_BADINTERNALERROR;
    }
    PyObject *returned = PyTuple_GET_ITEM(result, 1);
    if(ensureCallbackTypes() < 0)
        return UA_STATUSCODE_BADINTERNALERROR;
    int isDataValue = PyObject_IsInstance(returned, callbackDataValueType);
    if(isDataValue < 0)
        return UA_STATUSCODE_BADINTERNALERROR;
    PyObject *conv = NULL;
    if(isDataValue) {
        conv = PY2UA(returned, value, &UA_TYPES[UA_TYPES_DATAVALUE], nsMapping,
                     customDataTypes);
    } else {
        conv = PY2UA(returned, &value->value, &UA_TYPES[UA_TYPES_VARIANT], nsMapping,
                     customDataTypes);
        if(conv)
            value->hasValue = true;
    }
    if(!conv)
        return UA_STATUSCODE_BADINTERNALERROR;
    value->hasStatus = true;
    value->status = callbackStatus;
    return UA_STATUSCODE_GOOD;
}

static UA_StatusCode
variableWriteResultToStatus(PyObject *result) {
    UA_StatusCode status;
    if(statusFromTuple(result, 1, "Variable write callback must return (StatusCode,)",
                       &status) != UA_STATUSCODE_GOOD)
        return UA_STATUSCODE_BADINTERNALERROR;
    return status;
}

static UA_StatusCode
pyVariableReadCallback(UA_Server *server,
                       const UA_NodeId *sessionId, void *sessionContext,
                       const UA_NodeId *nodeId, void *nodeContext,
                       UA_Boolean includeSourceTimeStamp,
                       const UA_NumericRange *range, UA_DataValue *value) {
    (void)nodeId;
    assertGIL();
    if(!nodeContext)
        return UA_STATUSCODE_BADNOTREADABLE;
    PyServer *pyServer = (PyServer *)UA_Server_getConfig(server)->context;
    if(!pyServer || pyServer->server != server)
        return UA_STATUSCODE_BADNOTREADABLE;
    PyObject *kwargs = variableCallbackKwargs(pyServer, sessionId, sessionContext, range,
                                              includeSourceTimeStamp ? 1 : 0);
    if(!kwargs) {
        PyErr_Print();
        return UA_STATUSCODE_BADINTERNALERROR;
    }
    UA_StatusCode invokeStatus;
    PyObject *result = callVariableCallback(pyServer, nodeContext, PY_NODE_CALLBACK_READ,
                                            NULL, kwargs, &invokeStatus);
    Py_DECREF(kwargs);
    if(!result)
        return invokeStatus;

    if(PyCoro_CheckExact(result)) {
        PyAsyncOperationState *state =
            new_async_operation_state(server, pyServer, ASYNC_OPERATION_READ, value);
        if(!state) {
            Py_DECREF(result);
            return UA_STATUSCODE_BADOUTOFMEMORY;
        }
        UA_StatusCode status = scheduleAsyncOperation(state, result);
        Py_DECREF(result);
        Py_DECREF(state);
        return status;
    }

    UA_StatusCode status = variableReadResultToOutput(pyServer, result, value);
    Py_DECREF(result);
    if(PyErr_Occurred())
        PyErr_Print();
    return status;
}

static UA_StatusCode
pyVariableWriteCallback(UA_Server *server,
                        const UA_NodeId *sessionId, void *sessionContext,
                        const UA_NodeId *nodeId, void *nodeContext,
                        const UA_NumericRange *range,
                        const UA_DataValue *value) {
    (void)nodeId;
    assertGIL();
    if(!nodeContext)
        return UA_STATUSCODE_BADNOTWRITABLE;
    PyServer *pyServer = (PyServer *)UA_Server_getConfig(server)->context;
    if(!pyServer || pyServer->server != server)
        return UA_STATUSCODE_BADNOTWRITABLE;
    const UA_NamespaceMapping *nsMapping = &pyServer->nsMapPy2UA;
    PyObject *pyValue = UA2PY(value, &UA_TYPES[UA_TYPES_DATAVALUE],
                              nsMapping);
    PyObject *kwargs = variableCallbackKwargs(
        pyServer, sessionId, sessionContext, range, -1);
    if(!pyValue || !kwargs) {
        Py_XDECREF(kwargs);
        Py_XDECREF(pyValue);
        PyErr_Print();
        return UA_STATUSCODE_BADINTERNALERROR;
    }
    UA_StatusCode invokeStatus;
    PyObject *result = callVariableCallback(pyServer, nodeContext, PY_NODE_CALLBACK_WRITE,
                                            pyValue, kwargs, &invokeStatus);
    Py_DECREF(pyValue);
    Py_DECREF(kwargs);
    if(!result)
        return invokeStatus;

    if(PyCoro_CheckExact(result)) {
        PyAsyncOperationState *state = new_async_operation_state(
            server, pyServer, ASYNC_OPERATION_WRITE, (void *)(uintptr_t)value);
        if(!state) {
            Py_DECREF(result);
            return UA_STATUSCODE_BADOUTOFMEMORY;
        }
        UA_StatusCode status = scheduleAsyncOperation(state, result);
        Py_DECREF(result);
        Py_DECREF(state);
        return status;
    }

    UA_StatusCode status = variableWriteResultToStatus(result);
    Py_DECREF(result);
    if(PyErr_Occurred())
        PyErr_Print();
    return status;
}

/* ==================================================== *
 *              add_method_node                         *
 * ==================================================== */  
PyObject *
pyServer_add_method_node(PyObject *self, PyObject *args) {
    PyObject *py_requested, *py_parent, *py_reftype,
             *py_browse, *py_attr,
             *py_inargs, *py_outargs, *py_inargs_id, *py_outargs_id;

    if (!PyArg_ParseTuple(args, "OOOOOOOOO", &py_requested, &py_parent,
                          &py_reftype, &py_browse, &py_attr,
                          &py_inargs, &py_outargs, &py_inargs_id,
                          &py_outargs_id))
        return NULL;
    PyServer *srv = (PyServer *)self;
    const UA_NamespaceMapping *nsMapping = &srv->nsMapPy2UA;
    const UA_DataTypeArray *customDataTypes =
        UA_Server_getConfig(srv->server)->customDataTypes;

    UA_NodeId requestedId, parentId, refTypeId, inputArgsId, outputArgsId;
    UA_QualifiedName browseName;
    UA_MethodAttributes attr;

    if (extract_nodeid(py_requested, &requestedId, nsMapping, customDataTypes) < 0) return NULL;
    if (extract_nodeid(py_parent, &parentId, nsMapping, customDataTypes) < 0) goto fail_parent;
    if (extract_nodeid(py_reftype, &refTypeId, nsMapping, customDataTypes) < 0) goto fail_reftype;
    if (extract_qualifiedname(py_browse, &browseName, nsMapping, customDataTypes) < 0) goto fail_browse;
    if (extract_nodeid(py_inargs_id, &inputArgsId, nsMapping, customDataTypes) < 0) goto fail_input_id;
    if (extract_nodeid(py_outargs_id, &outputArgsId, nsMapping, customDataTypes) < 0) goto fail_output_id;

    UA_MethodAttributes_init(&attr);
    PyObject *conv = PY2UA(py_attr, &attr, &UA_TYPES[UA_TYPES_METHODATTRIBUTES], nsMapping, customDataTypes);
    if (!conv) goto fail_attr;

    /* Convert input arguments list */
    size_t inputSize = 0;
    UA_Argument *inputArgs = NULL;
    if (py_inargs != Py_None) {
        if (!PyList_Check(py_inargs) && !PyTuple_Check(py_inargs)) {
            PyErr_SetString(PyExc_TypeError,
                            "input_arguments must be a list or None");
            goto fail_attr;
        }
        inputSize = (size_t)PySequence_Size(py_inargs);
        if (inputSize > 0) {
            inputArgs = (UA_Argument *)UA_calloc(inputSize, sizeof(UA_Argument));
            for (size_t i = 0; i < inputSize; i++) {
                PyObject *item = PySequence_GetItem(py_inargs, (Py_ssize_t)i);
                PyObject *c = PY2UA(item, &inputArgs[i], &UA_TYPES[UA_TYPES_ARGUMENT], nsMapping, customDataTypes);
                Py_DECREF(item);
                if (!c) {
                    for (size_t j = 0; j < i; j++)
                        UA_Argument_clear(&inputArgs[j]);
                    UA_free(inputArgs);
                    goto fail_attr;
                }
            }
        }
    }

    /* Convert output arguments list */
    size_t outputSize = 0;
    UA_Argument *outputArgs = NULL;
    if (py_outargs != Py_None) {
        if (!PyList_Check(py_outargs) && !PyTuple_Check(py_outargs)) {
            PyErr_SetString(PyExc_TypeError,
                            "output_arguments must be a list or None");
            for (size_t i = 0; i < inputSize; i++)
                UA_Argument_clear(&inputArgs[i]);
            UA_free(inputArgs);
            goto fail_attr;
        }
        outputSize = (size_t)PySequence_Size(py_outargs);
        if (outputSize > 0) {
            outputArgs = (UA_Argument *)UA_calloc(outputSize,
                                                   sizeof(UA_Argument));
            for (size_t i = 0; i < outputSize; i++) {
                PyObject *item = PySequence_GetItem(py_outargs, (Py_ssize_t)i);
                PyObject *c = PY2UA(item, &outputArgs[i], &UA_TYPES[UA_TYPES_ARGUMENT], nsMapping, customDataTypes);
                Py_DECREF(item);
                if (!c) {
                    for (size_t j = 0; j < i; j++)
                        UA_Argument_clear(&outputArgs[j]);
                    UA_free(outputArgs);
                    for (size_t j = 0; j < inputSize; j++)
                        UA_Argument_clear(&inputArgs[j]);
                    UA_free(inputArgs);
                    goto fail_attr;
                }
            }
        }
    }

    UA_NodeId outId;
    UA_NodeId_init(&outId);
    /* Install callback state only after the complete node and its argument
     * Properties exist. Until then the Method is inert and can be rolled back
     * without leaving a trampoline that has no Python state. */
    UA_StatusCode status = UA_Server_addMethodNodeEx(
        srv->server, requestedId, parentId, refTypeId,
        browseName, attr, NULL,
        inputSize, inputArgs, inputArgsId, NULL,
        outputSize, outputArgs, outputArgsId, NULL,
        NULL, &outId);

    /* Cleanup argument arrays */
    for (size_t i = 0; i < inputSize; i++)
        UA_Argument_clear(&inputArgs[i]);
    UA_free(inputArgs);
    for (size_t i = 0; i < outputSize; i++)
        UA_Argument_clear(&outputArgs[i]);
    UA_free(outputArgs);

    UA_MethodAttributes_clear(&attr);
    UA_NodeId_clear(&outputArgsId);
    UA_NodeId_clear(&inputArgsId);
    UA_QualifiedName_clear(&browseName);
    UA_NodeId_clear(&refTypeId);
    UA_NodeId_clear(&parentId);
    UA_NodeId_clear(&requestedId);

    if (status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);

    PyObject *result = UA2PY(&outId, &UA_TYPES[UA_TYPES_NODEID], nsMapping);
    UA_NodeId_clear(&outId);
    return result;

fail_attr:
    UA_NodeId_clear(&outputArgsId);
fail_output_id:
    UA_NodeId_clear(&inputArgsId);
fail_input_id:
    UA_QualifiedName_clear(&browseName);
fail_browse:
    UA_NodeId_clear(&refTypeId);
fail_reftype:
    UA_NodeId_clear(&parentId);
fail_parent:
    UA_NodeId_clear(&requestedId);
    return NULL;
}

static UA_Node *
attachedCallbackNode(PyServer *server, PyObject *object,
                     const char *description) {
    PyServer *owner = NULL;
    UA_Node *node = pyNodeStore_attachedNode(object, &owner);
    if(!node)
        return NULL;
    if(owner != server) {
        PyErr_Format(PyExc_ValueError, "%s belongs to another server",
                     description);
        return NULL;
    }
    return node;
}

PyObject *
pyServer_set_callback_slot(PyObject *self, PyObject *args) {
    PyObject *pyNode, *callback, *receiver;
    int kind;
    if(!PyArg_ParseTuple(args, "OiOO", &pyNode, &kind, &callback, &receiver))
        return NULL;
    if(kind < PY_NODE_CALLBACK_CALL || kind > PY_NODE_CALLBACK_WRITE) {
        PyErr_SetString(PyExc_ValueError, "unknown callback slot");
        return NULL;
    }
    if(callback != Py_None && !PyCallable_Check(callback)) {
        PyErr_SetString(PyExc_TypeError, "callback must be callable or None");
        return NULL;
    }
    if(callback == Py_None && receiver != Py_None) {
        PyErr_SetString(PyExc_TypeError, "an empty callback cannot have a receiver");
        return NULL;
    }
    PyServer *server = (PyServer *)self;
    UA_Node *node = attachedCallbackNode(server, pyNode, "callback node");
    if(!node)
        return NULL;
    PyObject *storedReceiver = receiver == Py_None ? NULL : receiver;
    if(storedReceiver &&
       !attachedCallbackNode(server, storedReceiver, "callback receiver"))
        return NULL;

    if((kind == PY_NODE_CALLBACK_CALL) !=
       (node->head.nodeClass == UA_NODECLASS_METHOD)) {
        PyErr_SetString(PyExc_TypeError,
                        "callback kind does not match the node class");
        return NULL;
    }
    UA_Boolean oldRead =
        pyNodeStore_hasCallback(node->head.context, PY_NODE_CALLBACK_READ);
    UA_Boolean oldWrite =
        pyNodeStore_hasCallback(node->head.context, PY_NODE_CALLBACK_WRITE);
    UA_Boolean read = kind == PY_NODE_CALLBACK_READ ?
        callback != Py_None : oldRead;
    UA_Boolean write = kind == PY_NODE_CALLBACK_WRITE ?
        callback != Py_None : oldWrite;
    UA_Boolean dropsValueSource =
        node->head.nodeClass == UA_NODECLASS_VARIABLE &&
        node->variableNode.valueSourceType != UA_VALUESOURCETYPE_INTERNAL &&
        !read && !write;
    if(dropsValueSource) {
        PyErr_SetString(PyExc_TypeError,
                        "removing the final Variable callback requires "
                        "implement(variable, value)");
        return NULL;
    }
    UA_StatusCode status = pyNodeStore_setCallback(
        node->head.context, (PyNodeCallbackKind)kind,
        callback == Py_None ? NULL : callback, storedReceiver);
    if(status == UA_STATUSCODE_GOOD &&
       node->head.nodeClass == UA_NODECLASS_METHOD &&
       node->methodNode.method != pyMethodCallback)
        status = UA_Server_setMethodNodeCallback(
            server->server, node->head.nodeId, pyMethodCallback);
    else if(status == UA_STATUSCODE_GOOD &&
            node->head.nodeClass == UA_NODECLASS_VARIABLE &&
            (oldRead != read || oldWrite != write))
        status = UA_Server_setVariableNode_callbackValueSource(
            server->server, node->head.nodeId,
            (UA_CallbackValueSource) {
                .read = read ? pyVariableReadCallback : NULL,
                .write = write ? pyVariableWriteCallback : NULL
            });
    if(PyErr_Occurred())
        return NULL;
    if(status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);
    Py_RETURN_NONE;
}

PyObject *
pyServer_set_local_value(PyObject *self, PyObject *args) {
    PyObject *pyNode, *pyValue;
    if(!PyArg_ParseTuple(args, "OO", &pyNode, &pyValue))
        return NULL;
    PyServer *server = (PyServer *)self;
    UA_Node *node = attachedCallbackNode(server, pyNode, "Variable");
    if(!node)
        return NULL;
    if(node->head.nodeClass != UA_NODECLASS_VARIABLE) {
        PyErr_SetString(PyExc_TypeError,
                        "local values can only be installed on Variables");
        return NULL;
    }
    if(isDispatching(node)) {
        PyErr_SetString(PyExc_RuntimeError,
                        "cannot replace Variable storage from its active callback");
        return NULL;
    }

    const UA_NamespaceMapping *nsMapping = &server->nsMapPy2UA;
    const UA_DataTypeArray *customDataTypes =
        UA_Server_getConfig(server->server)->customDataTypes;
    UA_DataValue value;
    UA_DataValue_init(&value);
    if(ensureCallbackTypes() < 0)
        return NULL;
    int isDataValue = PyObject_IsInstance(pyValue, callbackDataValueType);
    if(isDataValue < 0)
        return NULL;
    if(isDataValue) {
        if(!PY2UA_datavalue(pyValue, &value, nsMapping, customDataTypes)) {
            UA_DataValue_clear(&value);
            return NULL;
        }
    } else {
        value.hasValue = true;
        if(!PY2UA(pyValue, &value.value, &UA_TYPES[UA_TYPES_VARIANT],
                  nsMapping, customDataTypes)) {
            UA_DataValue_clear(&value);
            return NULL;
        }
    }

    UA_StatusCode status = UA_Server_setVariableNode_internalValueSource(
        server->server, node->head.nodeId, &value, NULL);
    UA_DataValue_clear(&value);
    if(status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);
    status = pyNodeStore_setCallback(
        node->head.context, PY_NODE_CALLBACK_READ, NULL, NULL);
    if(status == UA_STATUSCODE_GOOD)
        status = pyNodeStore_setCallback(
            node->head.context, PY_NODE_CALLBACK_WRITE, NULL, NULL);
    if(status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);
    Py_RETURN_NONE;
}

PyObject *
pyServer_get_callback(PyObject *self, PyObject *args) {
    PyObject *pyNode;
    int kind;
    if(!PyArg_ParseTuple(args, "Oi", &pyNode, &kind))
        return NULL;
    if(kind < PY_NODE_CALLBACK_CALL || kind > PY_NODE_CALLBACK_WRITE) {
        PyErr_SetString(PyExc_ValueError, "unknown callback slot");
        return NULL;
    }
    PyServer *server = (PyServer *)self;
    UA_Node *node = attachedCallbackNode(server, pyNode, "callback node");
    if(!node)
        return NULL;
    PyObject *callback = pyNodeStore_getCallback(
        node->head.context, (PyNodeCallbackKind)kind, NULL);
    if(!callback)
        Py_RETURN_NONE;
    return callback;
}

PyObject *
pyServer_get_node_type(PyObject *self, PyObject *args) {
    PyObject *pyNode;
    if(!PyArg_ParseTuple(args, "O", &pyNode))
        return NULL;
    PyServer *server = (PyServer *)self;
    const UA_DataTypeArray *customDataTypes =
        UA_Server_getConfig(server->server)->customDataTypes;
    UA_NodeId nodeId;
    if(extract_nodeid(pyNode, &nodeId, &server->nsMapPy2UA,
                      customDataTypes) < 0)
        return NULL;
    UA_NodeId typeId;
    UA_NodeId_init(&typeId);
    UA_StatusCode status = UA_Server_getNodeType(
        server->server, nodeId, &typeId);
    UA_NodeId_clear(&nodeId);
    if(status != UA_STATUSCODE_GOOD) {
        UA_NodeId_clear(&typeId);
        return PyErr_StatusCode(status);
    }
    PyObject *result = UA2PY(&typeId, &UA_TYPES[UA_TYPES_NODEID],
                             &server->nsMapPy2UA);
    UA_NodeId_clear(&typeId);
    return result;
}

/* ==================================================== *
 *              add_reference                           *
 * ==================================================== */
PyObject *
pyServer_add_reference(PyObject *self, PyObject *args) {
    PyObject *py_source, *py_reftype, *py_target;
    int is_forward = 1;

    if (!PyArg_ParseTuple(args, "OOO|p", &py_source, &py_reftype,
                          &py_target, &is_forward))
        return NULL;
    PyServer *srv = (PyServer *)self;
    const UA_NamespaceMapping *nsMapping = &srv->nsMapPy2UA;
    const UA_DataTypeArray *customDataTypes =
        UA_Server_getConfig(srv->server)->customDataTypes;

    UA_NodeId sourceId, refTypeId;
    UA_ExpandedNodeId targetId;

    if (extract_nodeid(py_source, &sourceId, nsMapping, customDataTypes) < 0) return NULL;
    if (extract_nodeid(py_reftype, &refTypeId, nsMapping, customDataTypes) < 0) {
        UA_NodeId_clear(&sourceId);
        return NULL;
    }

    UA_ExpandedNodeId_init(&targetId);
    PyObject *conv = PY2UA(py_target, &targetId, &UA_TYPES[UA_TYPES_EXPANDEDNODEID], nsMapping, customDataTypes);
    if (!conv) {
        UA_NodeId_clear(&refTypeId);
        UA_NodeId_clear(&sourceId);
        return NULL;
    }

    UA_StatusCode status = UA_Server_addReference(
        srv->server, sourceId, refTypeId, targetId,
        (UA_Boolean)is_forward);

    UA_ExpandedNodeId_clear(&targetId);
    UA_NodeId_clear(&refTypeId);
    UA_NodeId_clear(&sourceId);

    return UA2PY(&status, &UA_TYPES[UA_TYPES_STATUSCODE], nsMapping);
}

PyObject *
pyServer_delete_reference(PyObject *self, PyObject *args) {
    PyObject *py_source, *py_reftype, *py_target;
    int is_forward = 1;
    int delete_bidirectional = 1;

    if (!PyArg_ParseTuple(args, "OOO|pp", &py_source, &py_reftype,
                          &py_target, &is_forward, &delete_bidirectional))
        return NULL;
    PyServer *srv = (PyServer *)self;
    const UA_NamespaceMapping *nsMapping = &srv->nsMapPy2UA;
    const UA_DataTypeArray *customDataTypes =
        UA_Server_getConfig(srv->server)->customDataTypes;

    UA_NodeId sourceId, refTypeId;
    UA_ExpandedNodeId targetId;
    if (extract_nodeid(py_source, &sourceId, nsMapping, customDataTypes) < 0)
        return NULL;
    if (extract_nodeid(py_reftype, &refTypeId, nsMapping, customDataTypes) < 0) {
        UA_NodeId_clear(&sourceId);
        return NULL;
    }
    UA_ExpandedNodeId_init(&targetId);
    PyObject *conv = PY2UA(py_target, &targetId,
                           &UA_TYPES[UA_TYPES_EXPANDEDNODEID],
                           nsMapping, customDataTypes);
    if (!conv) {
        UA_NodeId_clear(&refTypeId);
        UA_NodeId_clear(&sourceId);
        return NULL;
    }

    UA_StatusCode status = UA_Server_deleteReference(
        srv->server, sourceId, refTypeId, (UA_Boolean)is_forward,
        targetId, (UA_Boolean)delete_bidirectional);
    UA_ExpandedNodeId_clear(&targetId);
    UA_NodeId_clear(&refTypeId);
    UA_NodeId_clear(&sourceId);
    return UA2PY(&status, &UA_TYPES[UA_TYPES_STATUSCODE], nsMapping);
}

/* ==================================================== *
 *              delete_node                             *
 * ==================================================== */  
PyObject *
pyServer_delete_node(PyObject *self, PyObject *args) {
    PyObject *py_nodeid;
    int delete_refs = 1;

    if (!PyArg_ParseTuple(args, "O|p", &py_nodeid, &delete_refs))
        return NULL;
    PyServer *srv = (PyServer *)self;
    const UA_NamespaceMapping *nsMapping = &srv->nsMapPy2UA;
    const UA_DataTypeArray *customDataTypes =
        UA_Server_getConfig(srv->server)->customDataTypes;

    UA_NodeId nodeId;
    if (extract_nodeid(py_nodeid, &nodeId, nsMapping, customDataTypes) < 0)
        return NULL;

    UA_StatusCode status = UA_Server_deleteNode(
        srv->server, nodeId, (UA_Boolean)delete_refs);

    UA_NodeId_clear(&nodeId);

    return UA2PY(&status, &UA_TYPES[UA_TYPES_STATUSCODE], nsMapping);
}

/************************************************************
 * Asynchronous value and DataValue reads
 ************************************************************/
PyObject *
pyServer_read_data_value(PyObject *self, PyObject *args) {
    PyObject *py_item;
    int timestamps;
    if (!PyArg_ParseTuple(args, "Oi", &py_item, &timestamps))
        return NULL;
    if (timestamps < UA_TIMESTAMPSTORETURN_SOURCE ||
        timestamps > UA_TIMESTAMPSTORETURN_NEITHER)
        return PyErr_StatusCode(UA_STATUSCODE_BADTIMESTAMPSTORETURNINVALID);

    PyServer *srv = (PyServer *)self;
    UA_ReadValueId item;
    UA_ReadValueId_init(&item);
    if (!PY2UA(py_item, &item, &UA_TYPES[UA_TYPES_READVALUEID],
               &srv->nsMapPy2UA, UA_Server_getConfig(srv->server)->customDataTypes)) {
        UA_ReadValueId_clear(&item);
        return NULL;
    }
    ServerAsyncCtx *ctx = serverAsync_create_ctx(srv->server, (int)item.attributeId);
    if (!ctx) {
        UA_ReadValueId_clear(&item);
        return NULL;
    }
    /* The callback can resolve immediately and free ctx. */
    PyObject *future = ctx->future;
    UA_StatusCode status = UA_Server_read_async(srv->server, &item,
        (UA_TimestampsToReturn)timestamps, serverAsyncDataValueCallback, ctx, 0);
    UA_ReadValueId_clear(&item);
    if (status != UA_STATUSCODE_GOOD) {
        Py_DECREF(ctx->future);
        Py_DECREF(future);
        UA_free(ctx);
        return PyErr_StatusCode(status);
    }
    return future;
}

PyObject *
pyServer_read_value(PyObject *self, PyObject *args) {
    PyObject *py_nodeid;
    const char *indexRange = NULL;

    if (!PyArg_ParseTuple(args, "O|z", &py_nodeid, &indexRange))
        return NULL;
    PyServer *srv = (PyServer *)self;
    const UA_NamespaceMapping *nsMapping = &srv->nsMapPy2UA;
    const UA_DataTypeArray *customDataTypes =
        UA_Server_getConfig(srv->server)->customDataTypes;

    UA_NodeId nodeId;
    if (extract_nodeid(py_nodeid, &nodeId, nsMapping, customDataTypes) < 0)
        return NULL;

    ServerAsyncCtx *ctx = serverAsync_create_ctx(srv->server,
                                                 UA_ATTRIBUTEID_VALUE);
    if (!ctx) {
        UA_NodeId_clear(&nodeId);
        return NULL;
    }

    UA_ReadValueId rvi;
    UA_ReadValueId_init(&rvi);
    rvi.nodeId = nodeId; /* moved */
    rvi.attributeId = UA_ATTRIBUTEID_VALUE;
    if(indexRange)
        rvi.indexRange = UA_String_fromChars(indexRange);

    /* Save future before submitting: callback may fire synchronously and
     * free ctx, making ctx->future a dangling read. */
    PyObject *fut = ctx->future;
    UA_StatusCode sc = UA_Server_read_async(srv->server, &rvi,
                                            UA_TIMESTAMPSTORETURN_NEITHER,
                                            serverAsyncReadCallback, ctx, 0);
    UA_ReadValueId_clear(&rvi);
    if (sc != UA_STATUSCODE_GOOD) {
        Py_DECREF(fut);
        UA_free(ctx);
        return PyErr_StatusCode(sc);
    }
    return fut;
}

/* ==================================================== *
 *                  write_value                         *
 * ==================================================== */
PyObject *
pyServer_write_value(PyObject *self, PyObject *args) {
    PyObject *py_nodeid, *py_value;
    const char *indexRange = NULL;
    int return_status = 0;

    if (!PyArg_ParseTuple(args, "OO|zp", &py_nodeid, &py_value, &indexRange, &return_status))
        return NULL;
    PyServer *srv = (PyServer *)self;
    const UA_NamespaceMapping *nsMapping = &srv->nsMapPy2UA;
    const UA_DataTypeArray *customDataTypes =
        UA_Server_getConfig(srv->server)->customDataTypes;

    UA_NodeId nodeId;
    if (extract_nodeid(py_nodeid, &nodeId, nsMapping, customDataTypes) < 0)
        return NULL;

    UA_WriteValue wv;
    if (build_write_value(&nodeId, true, UA_ATTRIBUTEID_VALUE, py_value,
                          &wv, nsMapping, customDataTypes) < 0) {
        UA_NodeId_clear(&nodeId);
        UA_WriteValue_clear(&wv);
        return NULL;
    }
    if(indexRange)
        wv.indexRange = UA_String_fromChars(indexRange);
    UA_NodeId_clear(&nodeId);
    ServerAsyncCtx *ctx = serverAsync_create_ctx(srv->server, 0);
    if (!ctx) {
        UA_WriteValue_clear(&wv);
        return NULL;
    }

    ctx->return_write_status = (UA_Boolean)return_status;
    PyObject *fut = ctx->future;
    UA_StatusCode sc = UA_Server_write_async(srv->server, &wv,
                                             serverAsyncWriteCallback, ctx, 0);
    UA_WriteValue_clear(&wv);
    if (sc != UA_STATUSCODE_GOOD) {
        Py_DECREF(fut);
        Py_DECREF(ctx->future);
        UA_free(ctx);
        return PyErr_StatusCode(sc);
    }
    return fut;
}

/* ==================================================== *
 *                  call                                *
 * ==================================================== */
PyObject *
pyServer_call(PyObject *self, PyObject *args) {
    PyObject *py_object_id, *py_method_id, *py_input_args;
    unsigned int timeout = 0;
    int return_status = 0;

    if (!PyArg_ParseTuple(args, "OOO|Ip", &py_object_id, &py_method_id,
                          &py_input_args, &timeout, &return_status))
        return NULL;
    PyServer *srv = (PyServer *)self;
    const UA_NamespaceMapping *nsMapping = &srv->nsMapPy2UA;
    const UA_DataTypeArray *customDataTypes =
        UA_Server_getConfig(srv->server)->customDataTypes;

    UA_CallMethodRequest request;
    UA_CallMethodRequest_init(&request);

    if (extract_nodeid(py_object_id, &request.objectId, nsMapping, customDataTypes) < 0)
        return NULL;
    if (extract_nodeid(py_method_id, &request.methodId, nsMapping, customDataTypes) < 0) {
        UA_NodeId_clear(&request.objectId);
        return NULL;
    }

    /* Empty Python sequences have no element from which PY2UA can infer a
     * Variant type. Read the Method metadata once and use it only for those
     * arguments. All populated arguments retain the normal dynamic subtype
     * conversion. */
    UA_Variant inputDefinitions;
    UA_Variant_init(&inputDefinitions);
    UA_StatusCode definitionsStatus = UA_Server_readObjectProperty(
        srv->server, request.methodId,
        UA_QUALIFIEDNAME(0, "InputArguments"), &inputDefinitions);
    const UA_Argument *definitions = NULL;
    size_t definitionsSize = 0;
    if(definitionsStatus == UA_STATUSCODE_GOOD &&
       inputDefinitions.type == &UA_TYPES[UA_TYPES_ARGUMENT]) {
        definitions = (const UA_Argument*)inputDefinitions.data;
        definitionsSize = inputDefinitions.arrayLength;
        if(definitionsSize == 0 &&
           inputDefinitions.data > UA_EMPTY_ARRAY_SENTINEL)
            definitionsSize = 1;
    }

    /* Convert input arguments list/tuple -> UA_Variant array */
    if (py_input_args != Py_None && PySequence_Check(py_input_args)) {
        Py_ssize_t n = PySequence_Size(py_input_args);
        if (n < 0) {
            UA_Variant_clear(&inputDefinitions);
            UA_CallMethodRequest_clear(&request);
            return NULL;
        }
        if (n > 0) {
            request.inputArguments =
                (UA_Variant *)UA_Array_new((size_t)n,
                                           &UA_TYPES[UA_TYPES_VARIANT]);
            if (!request.inputArguments) {
                UA_Variant_clear(&inputDefinitions);
                UA_CallMethodRequest_clear(&request);
                return PyErr_NoMemory();
            }
            request.inputArgumentsSize = (size_t)n;
            for (Py_ssize_t i = 0; i < n; i++) {
                PyObject *item = PySequence_GetItem(py_input_args, i);
                PyObject *conv = NULL;
                Py_ssize_t itemSize = PySequence_Check(item) ?
                    PySequence_Size(item) : -1;
                if(itemSize == 0 && (size_t)i < definitionsSize &&
                   definitions[i].valueRank != UA_VALUERANK_SCALAR) {
                    const UA_DataType *elementType = UA_Server_findDataType(
                        srv->server, &definitions[i].dataType);
                    /* Abstract Structure types need no native layout and may
                     * therefore be absent from customDataTypes. Their wire
                     * representation is ExtensionObject. */
                    if(!elementType)
                        elementType = &UA_TYPES[UA_TYPES_EXTENSIONOBJECT];
                    if(elementType) {
                        request.inputArguments[i].type = elementType;
                        request.inputArguments[i].data = UA_EMPTY_ARRAY_SENTINEL;
                        conv = Py_None;
                    }
                }
                if(!conv)
                    conv = PY2UA(item, &request.inputArguments[i],
                                  &UA_TYPES[UA_TYPES_VARIANT], nsMapping,
                                  customDataTypes);
                Py_DECREF(item);
                if (!conv) {
                    if(PyErr_ExceptionMatches(PyExc_TypeError))
                        PyErr_Format(PyExc_TypeError,
                                     "method argument %zd cannot be converted "
                                     "to an OPC UA native type", i + 1);
                    UA_Variant_clear(&inputDefinitions);
                    UA_CallMethodRequest_clear(&request);
                    return NULL;
                }
            }
        }
    }
    UA_Variant_clear(&inputDefinitions);

    ServerAsyncCtx *ctx = serverAsync_create_ctx(srv->server, 0);
    if (!ctx) {
        UA_CallMethodRequest_clear(&request);
        return NULL;
    }

    ctx->return_call_status = (UA_Boolean)return_status;
    PyObject *fut = ctx->future;
    UA_StatusCode sc = UA_Server_call_async(srv->server, &request,
                                            serverAsyncCallCallback, ctx,
                                            (UA_UInt32)timeout);
    UA_CallMethodRequest_clear(&request);
    if (sc != UA_STATUSCODE_GOOD) {
        Py_DECREF(fut);
        Py_DECREF(ctx->future);
        UA_free(ctx);
        return PyErr_StatusCode(sc);
    }
    return fut;
}

/* ==================================================== *
 *                   historical data                    *
 * ==================================================== */

static int
history_target(PyServer *srv, PyObject *py_nodeId, UA_NodeId *out) {
    if (!srv->server) {
        PyErr_SetString(PyExc_RuntimeError, "Server not initialized");
        return -1;
    }
    if (!pyHistory_enabled(&srv->history)) {
        PyErr_SetString(PyExc_RuntimeError,
                        "No history database configured. "
                        "Call config.setHistoryDatabase() first.");
        return -1;
    }
    const UA_DataTypeArray *customDataTypes =
        UA_Server_getConfig(srv->server)->customDataTypes;
    return extract_nodeid(py_nodeId, out, &srv->nsMapPy2UA, customDataTypes);
}

static int
history_strategy(const char *name, UA_HistorizingUpdateStrategy *out) {
    if (!name || strcmp(name, "on-write") == 0) {
        *out = UA_HISTORIZINGUPDATESTRATEGY_VALUESET;
        return 0;
    }
    if (strcmp(name, "poll") == 0) {
        *out = UA_HISTORIZINGUPDATESTRATEGY_POLL;
        return 0;
    }
    if (strcmp(name, "manual") == 0) {
        *out = UA_HISTORIZINGUPDATESTRATEGY_USER;
        return 0;
    }
    PyErr_Format(PyExc_ValueError,
                 "unknown history strategy '%s', expected 'on-write', 'poll' "
                 "or 'manual'",
                 name);
    return -1;
}

/* Interpret the `capacity` argument. None asks for a store that grows instead
 * of evicting, with the database default as its initial allocation. */
static int
history_capacity(PyObject *py_capacity, int *capacity, int *unbounded) {
    *capacity = 0;
    *unbounded = 0;
    if (py_capacity == NULL || py_capacity == Py_None) {
        *unbounded = (py_capacity == Py_None);
        return 0;
    }
    long value = PyLong_AsLong(py_capacity);
    if (value == -1 && PyErr_Occurred()) {
        PyErr_SetString(PyExc_TypeError,
                        "capacity must be an integer, or None to grow without "
                        "a limit");
        return -1;
    }
    if (value < 0) {
        PyErr_SetString(PyExc_ValueError, "capacity must not be negative");
        return -1;
    }
    if (value > INT_MAX) {
        PyErr_SetString(PyExc_ValueError, "capacity is too large");
        return -1;
    }
    *capacity = (int)value;
    return 0;
}

static PyObject *
history_add(PyServer *srv, PyObject *py_nodeId, int capacity, int unbounded,
            int max_response, const char *strategy_name, double interval) {
    UA_HistorizingUpdateStrategy strategy;
    if (history_strategy(strategy_name, &strategy) < 0)
        return NULL;
    size_t intervalMs = (size_t)(interval * 1000.0 + 0.5);
    if (strategy == UA_HISTORIZINGUPDATESTRATEGY_POLL && intervalMs == 0) {
        PyErr_SetString(PyExc_ValueError,
                        "the poll strategy needs an interval of at least "
                        "0.001 seconds");
        return NULL;
    }

    UA_NodeId nodeId;
    if (history_target(srv, py_nodeId, &nodeId) < 0)
        return NULL;

    /* `max_response` of 0 takes the response size from the history database.
     * Only the deprecated _register_historizing passes anything else: how many
     * values fit in one HistoryRead response is a transport policy rather than
     * a property of the signal.
     *
     * The history layer expects the service mutex, as the event loop holds it
     * when it records a sample. The lock is reentrant, so the MonitoredItem a
     * polled node starts may take it again. */
    lockServer(srv->server);
    UA_StatusCode status =
        pyHistory_register(&srv->history, srv->server, &nodeId,
                           (size_t)capacity, unbounded ? true : false,
                           (size_t)max_response, strategy, intervalMs);
    unlockServer(srv->server);
    UA_NodeId_clear(&nodeId);

    if (status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);
    Py_RETURN_NONE;
}

PyObject *
pyServer_history_add(PyObject *self, PyObject *args, PyObject *kwds) {
    static char *kwlist[] = {"nodeId", "capacity", "strategy", "interval", NULL};
    PyObject *py_nodeId = NULL;
    PyObject *py_capacity = NULL; /* absent or 0 takes the database default */
    const char *strategy = NULL;
    double interval = 1.0;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "O|Osd", kwlist, &py_nodeId,
                                     &py_capacity, &strategy, &interval))
        return NULL;

    int capacity = 0;
    int unbounded = 0;
    if (history_capacity(py_capacity, &capacity, &unbounded) < 0)
        return NULL;
    return history_add((PyServer *)self, py_nodeId, capacity, unbounded, 0,
                       strategy, interval);
}

PyObject *
pyServer_register_historizing(PyObject *self, PyObject *args, PyObject *kwds) {
    static char *kwlist[] = {"nodeid", "max_values", "max_response", NULL};
    PyObject *py_nodeId = NULL;
    int max_values = 0;
    int max_response = 0;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "O|ii", kwlist, &py_nodeId,
                                     &max_values, &max_response))
        return NULL;
    if (max_values < 0 || max_response < 0) {
        PyErr_SetString(PyExc_ValueError,
                        "max_values and max_response must not be negative");
        return NULL;
    }
    return history_add((PyServer *)self, py_nodeId, max_values, 0, max_response,
                       NULL, 0.0);
}

PyObject *
pyServer_history_pause(PyObject *self, PyObject *args, PyObject *kwds) {
    static char *kwlist[] = {"nodeId", "paused", NULL};
    PyObject *py_nodeId = NULL;
    int paused = 1;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "O|p", kwlist, &py_nodeId,
                                     &paused))
        return NULL;
    PyServer *srv = (PyServer *)self;

    UA_NodeId nodeId;
    if (history_target(srv, py_nodeId, &nodeId) < 0)
        return NULL;

    lockServer(srv->server);
    UA_StatusCode status = pyHistory_setPaused(&srv->history, srv->server,
                                               &nodeId, paused ? true : false);
    unlockServer(srv->server);
    UA_NodeId_clear(&nodeId);

    if (status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);
    Py_RETURN_NONE;
}

PyObject *
pyServer_history_read(PyObject *self, PyObject *args, PyObject *kwds) {
    static char *kwlist[] = {"nodeId", "start",   "end",
                             "limit",  "reverse", NULL};
    PyObject *py_nodeId = NULL;
    PyObject *py_start = Py_None;
    PyObject *py_end = Py_None;
    Py_ssize_t limit = 0;
    int reverse = 0;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "O|OOnp", kwlist, &py_nodeId,
                                     &py_start, &py_end, &limit, &reverse))
        return NULL;
    if (limit < 0) {
        PyErr_SetString(PyExc_ValueError, "limit must not be negative");
        return NULL;
    }
    PyServer *srv = (PyServer *)self;

    /* An open end of the interval is the oldest respectively newest sample. */
    UA_DateTime start = INT64_MIN;
    UA_DateTime end = INT64_MAX;
    if (py_start != Py_None && !PY2UA_datetime(py_start, &start))
        return NULL;
    if (py_end != Py_None && !PY2UA_datetime(py_end, &end))
        return NULL;

    UA_NodeId nodeId;
    if (history_target(srv, py_nodeId, &nodeId) < 0)
        return NULL;

    UA_DataValue *values = NULL;
    size_t size = 0;
    lockServer(srv->server);
    UA_StatusCode status =
        pyHistory_read(&srv->history, &nodeId, start, end, (size_t)limit,
                       reverse ? true : false, &values, &size);
    unlockServer(srv->server);
    UA_NodeId_clear(&nodeId);

    if (status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);

    PyObject *list = PyList_New((Py_ssize_t)size);
    if (!list) {
        UA_Array_delete(values, size, &UA_TYPES[UA_TYPES_DATAVALUE]);
        return NULL;
    }
    for (size_t i = 0; i < size; i++) {
        PyObject *item = UA2PY(&values[i], &UA_TYPES[UA_TYPES_DATAVALUE],
                               &srv->nsMapPy2UA);
        if (!item) {
            Py_DECREF(list);
            UA_Array_delete(values, size, &UA_TYPES[UA_TYPES_DATAVALUE]);
            return NULL;
        }
        PyList_SET_ITEM(list, (Py_ssize_t)i, item); /* steals the reference */
    }
    UA_Array_delete(values, size, &UA_TYPES[UA_TYPES_DATAVALUE]);
    return list;
}

PyObject *
pyServer_history_insert(PyObject *self, PyObject *args, PyObject *kwds) {
    static char *kwlist[] = {"nodeId", "value", NULL};
    PyObject *py_nodeId = NULL;
    PyObject *py_value = NULL;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "OO", kwlist, &py_nodeId,
                                     &py_value))
        return NULL;
    PyServer *srv = (PyServer *)self;

    UA_DataValue value;
    UA_DataValue_init(&value);
    const UA_DataTypeArray *customDataTypes =
        UA_Server_getConfig(srv->server)->customDataTypes;
    if (!PY2UA(py_value, &value, &UA_TYPES[UA_TYPES_DATAVALUE],
               &srv->nsMapPy2UA, customDataTypes))
        return NULL;

    if (!value.hasSourceTimestamp && !value.hasServerTimestamp) {
        value.sourceTimestamp = UA_DateTime_now();
        value.hasSourceTimestamp = true;
    }

    UA_NodeId nodeId;
    if (history_target(srv, py_nodeId, &nodeId) < 0) {
        UA_DataValue_clear(&value);
        return NULL;
    }

    lockServer(srv->server);
    UA_StatusCode status = pyHistory_insert(&srv->history, &nodeId, &value);
    unlockServer(srv->server);
    UA_NodeId_clear(&nodeId);
    UA_DataValue_clear(&value);

    if (status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);
    Py_RETURN_NONE;
}

PyObject *
pyServer_history_remove(PyObject *self, PyObject *args) {
    PyObject *py_nodeId = NULL;
    if (!PyArg_ParseTuple(args, "O", &py_nodeId))
        return NULL;
    PyServer *srv = (PyServer *)self;

    UA_NodeId nodeId;
    if (history_target(srv, py_nodeId, &nodeId) < 0)
        return NULL;

    lockServer(srv->server);
    UA_StatusCode status =
        pyHistory_unregister(&srv->history, srv->server, &nodeId);
    unlockServer(srv->server);
    UA_NodeId_clear(&nodeId);

    if (status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);
    Py_RETURN_NONE;
}

/* Set one dict entry and release the value, whether or not it was created. */
static int
history_stats_entry(PyObject *dict, const char *key, PyObject *value) {
    if (!value)
        return -1;
    int res = PyDict_SetItemString(dict, key, value);
    Py_DECREF(value);
    return res;
}

PyObject *
pyServer_history_stats(PyObject *self, PyObject *args) {
    PyObject *py_nodeId = NULL;
    if (!PyArg_ParseTuple(args, "O", &py_nodeId))
        return NULL;
    PyServer *srv = (PyServer *)self;

    UA_NodeId nodeId;
    if (history_target(srv, py_nodeId, &nodeId) < 0)
        return NULL;

    PyHistoryStats stats;
    lockServer(srv->server);
    UA_StatusCode status = pyHistory_stats(&srv->history, &nodeId, &stats);
    unlockServer(srv->server);
    UA_NodeId_clear(&nodeId);
    if (status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);

    PyObject *dict = PyDict_New();
    if (!dict)
        return NULL;

    /* An empty ring has no timestamps to report. */
    PyObject *oldest = Py_None;
    PyObject *newest = Py_None;
    if (stats.count > 0) {
        oldest = UA2PY(&stats.oldest, &UA_TYPES[UA_TYPES_DATETIME],
                       &srv->nsMapPy2UA);
        newest = UA2PY(&stats.newest, &UA_TYPES[UA_TYPES_DATETIME],
                       &srv->nsMapPy2UA);
    } else {
        Py_INCREF(oldest);
        Py_INCREF(newest);
    }

    /* Every entry is consumed even after a failure, so a half-built dict cannot
     * leak the values it did not take. */
    int failed = history_stats_entry(dict, "oldest", oldest);
    failed |= history_stats_entry(dict, "newest", newest);
    failed |= history_stats_entry(dict, "capacity",
                                  PyLong_FromSize_t(stats.capacity));
    failed |= history_stats_entry(dict, "count", PyLong_FromSize_t(stats.count));
    failed |= history_stats_entry(dict, "stored",
                                  PyLong_FromUnsignedLongLong(stats.stored));
    failed |= history_stats_entry(dict, "overwrites",
                                  PyLong_FromUnsignedLongLong(stats.overwrites));
    failed |= history_stats_entry(dict, "dropped",
                                  PyLong_FromUnsignedLongLong(stats.dropped));
    failed |= history_stats_entry(dict, "unbounded",
                                  PyBool_FromLong(stats.unbounded));
    if (failed) {
        Py_DECREF(dict);
        return NULL;
    }
    return dict;
}

PyObject *
pyServer_history_clear(PyObject *self, PyObject *args) {
    PyObject *py_nodeId = NULL;
    if (!PyArg_ParseTuple(args, "O", &py_nodeId))
        return NULL;
    PyServer *srv = (PyServer *)self;

    UA_NodeId nodeId;
    if (history_target(srv, py_nodeId, &nodeId) < 0)
        return NULL;

    lockServer(srv->server);
    UA_StatusCode status = pyHistory_clearNode(&srv->history, &nodeId);
    unlockServer(srv->server);
    UA_NodeId_clear(&nodeId);

    if (status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);
    Py_RETURN_NONE;
}

/* ==================================================== *
 *              read_object_property                    *
 * ==================================================== */
PyObject *
pyServer_read_object_property(PyObject *self, PyObject *args) {
    PyObject *py_objectid, *py_property_name;
    if (!PyArg_ParseTuple(args, "OO", &py_objectid, &py_property_name))
        return NULL;
    PyServer *srv = (PyServer *)self;
    const UA_NamespaceMapping *nsMapping = &srv->nsMapPy2UA;
    const UA_DataTypeArray *customDataTypes =
        UA_Server_getConfig(srv->server)->customDataTypes;

    UA_NodeId objectId;
    if (extract_nodeid(py_objectid, &objectId, nsMapping, customDataTypes) < 0)
        return NULL;

    UA_QualifiedName propertyName;
    if (extract_qualifiedname(py_property_name, &propertyName, nsMapping, customDataTypes) < 0) {
        UA_NodeId_clear(&objectId);
        return NULL;
    }

    UA_Variant value;
    UA_Variant_init(&value);

    UA_StatusCode status = UA_Server_readObjectProperty(
        srv->server, objectId, propertyName, &value);

    UA_NodeId_clear(&objectId);
    UA_QualifiedName_clear(&propertyName);

    if (status != UA_STATUSCODE_GOOD) {
        UA_Variant_clear(&value);
        return PyErr_StatusCode(status);
    }

    PyObject *result = UA2PY(&value, &UA_TYPES[UA_TYPES_VARIANT], nsMapping);
    UA_Variant_clear(&value);
    return result;
}

/************************************************************
 * write_object_property(nodeid, property_name, value) -> None
 *
 * Write a property value on an object by its BrowseName.
 ************************************************************/
PyObject *
pyServer_write_object_property(PyObject *self, PyObject *args) {
    PyObject *py_objectid, *py_property_name, *py_value;
    if (!PyArg_ParseTuple(args, "OOO", &py_objectid, &py_property_name,
                          &py_value))
        return NULL;
    PyServer *srv = (PyServer *)self;
    const UA_NamespaceMapping *nsMapping = &srv->nsMapPy2UA;
    const UA_DataTypeArray *customDataTypes =
        UA_Server_getConfig(srv->server)->customDataTypes;

    UA_NodeId objectId;
    if (extract_nodeid(py_objectid, &objectId, nsMapping, customDataTypes) < 0)
        return NULL;

    UA_QualifiedName propertyName;
    if (extract_qualifiedname(py_property_name, &propertyName, nsMapping, customDataTypes) < 0) {
        UA_NodeId_clear(&objectId);
        return NULL;
    }

    UA_Variant value;
    UA_Variant_init(&value);
    if (!PY2UA(py_value, &value, &UA_TYPES[UA_TYPES_VARIANT], nsMapping, customDataTypes)) {
        UA_NodeId_clear(&objectId);
        UA_QualifiedName_clear(&propertyName);
        UA_Variant_clear(&value);
        return NULL;
    }

    UA_StatusCode status = UA_Server_writeObjectProperty(
        srv->server, objectId, propertyName, value);

    UA_NodeId_clear(&objectId);
    UA_QualifiedName_clear(&propertyName);
    UA_Variant_clear(&value);

    if (status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);
    Py_RETURN_NONE;
}

/* ==================================================== *
 *              read_attribute                          *
 * ==================================================== */
PyObject *
pyServer_read_attribute(PyObject *self, PyObject *args) {
    PyObject *py_nodeid;
    int attr_id;

    if (!PyArg_ParseTuple(args, "Oi", &py_nodeid, &attr_id))
        return NULL;
    PyServer *srv = (PyServer *)self;
    if (!srv->server) {
        PyErr_SetString(PyExc_RuntimeError, "server is already closed");
        return NULL;
    }
    const UA_NamespaceMapping *nsMapping = &srv->nsMapPy2UA;
    const UA_DataTypeArray *customDataTypes =
        UA_Server_getConfig(srv->server)->customDataTypes;

    if (attr_id < 1 || attr_id > 27) {
        PyErr_SetString(PyExc_ValueError, "Unsupported AttributeId");
        return NULL;
    }

    UA_NodeId nodeId;
    if (extract_nodeid(py_nodeid, &nodeId, nsMapping, customDataTypes) < 0)
        return NULL;

    ServerAsyncCtx *ctx = serverAsync_create_ctx(srv->server, attr_id);
    if (!ctx) {
        UA_NodeId_clear(&nodeId);
        return NULL;
    }

    UA_ReadValueId rvi;
    UA_ReadValueId_init(&rvi);
    rvi.nodeId = nodeId; /* moved */
    rvi.attributeId = (UA_UInt32)attr_id;

    PyObject *fut = ctx->future;
    UA_StatusCode sc = UA_Server_read_async(srv->server, &rvi,
                                            UA_TIMESTAMPSTORETURN_NEITHER,
                                            serverAsyncReadCallback, ctx, 0);
    UA_ReadValueId_clear(&rvi);
    if (sc != UA_STATUSCODE_GOOD) {
        Py_DECREF(fut);
        UA_free(ctx);
        return PyErr_StatusCode(sc);
    }
    return fut;
}

PyObject *
pyNode_read_attribute(PyObject *self, PyObject *args) {
    int attr_id;
    if(!PyArg_ParseTuple(args, "i", &attr_id))
        return NULL;
    if(attr_id < 1 || attr_id > 27) {
        PyErr_SetString(PyExc_ValueError, "Unsupported AttributeId");
        return NULL;
    }

    PyServer *srv;
    UA_Node *node = pyNodeStore_attachedNode(self, &srv);
    if(!node)
        return NULL;

    ServerAsyncCtx *ctx = serverAsync_create_ctx(srv->server, attr_id);
    if(!ctx)
        return NULL;

    UA_ReadValueId rvi;
    UA_ReadValueId_init(&rvi);
    rvi.nodeId = node->head.nodeId; /* borrowed from the canonical node */
    rvi.attributeId = (UA_UInt32)attr_id;

    PyObject *fut = ctx->future;
    lockServer(srv->server);
    UA_StatusCode sc = readWithNode_async(
        srv->server, &srv->server->adminSession, node, &rvi,
        UA_TIMESTAMPSTORETURN_NEITHER, serverAsyncReadCallback, ctx, 0);
    unlockServer(srv->server);
    if(sc != UA_STATUSCODE_GOOD) {
        Py_DECREF(fut);
        UA_free(ctx);
        return PyErr_StatusCode(sc);
    }
    return fut;
}

/* ==================================================== *
 *              write_data_value                        *
 * ==================================================== */
PyObject *
pyServer_write_data_value(PyObject *self, PyObject *args) {
    PyObject *py_nodeid, *py_datavalue;
    const char *indexRange = NULL;
    int attr_id = UA_ATTRIBUTEID_VALUE;
    int return_status = 0;

    if (!PyArg_ParseTuple(args, "OO|zip", &py_nodeid, &py_datavalue,
                          &indexRange, &attr_id, &return_status))
        return NULL;
    if (indexRange && attr_id != UA_ATTRIBUTEID_VALUE) {
        PyErr_SetString(PyExc_ValueError,
                        "range is only supported for the Value attribute");
        return NULL;
    }
    PyServer *srv = (PyServer *)self;
    const UA_NamespaceMapping *nsMapping = &srv->nsMapPy2UA;
    const UA_DataTypeArray *customDataTypes =
        UA_Server_getConfig(srv->server)->customDataTypes;

    UA_NodeId nodeId;
    if (extract_nodeid(py_nodeid, &nodeId, nsMapping, customDataTypes) < 0)
        return NULL;

    UA_WriteValue wv;
    UA_WriteValue_init(&wv);
    if (UA_NodeId_copy(&nodeId, &wv.nodeId) != UA_STATUSCODE_GOOD) {
        UA_NodeId_clear(&nodeId);
        return PyErr_NoMemory();
    }
    UA_NodeId_clear(&nodeId);
    wv.attributeId = (UA_UInt32)attr_id;
    if(indexRange)
        wv.indexRange = UA_String_fromChars(indexRange);

    PyObject *conv = PY2UA_datavalue(py_datavalue, &wv.value, nsMapping, customDataTypes);
    if (!conv) {
        UA_WriteValue_clear(&wv);
        return NULL;
    }
    if (attr_id != UA_ATTRIBUTEID_VALUE &&
        (wv.value.hasStatus || wv.value.hasSourceTimestamp ||
         wv.value.hasServerTimestamp || wv.value.hasSourcePicoseconds ||
         wv.value.hasServerPicoseconds)) {
        UA_WriteValue_clear(&wv);
        return serverAsync_write_status(srv->server,
                                        UA_STATUSCODE_BADWRITENOTSUPPORTED, return_status);
    }
    /* Model-change tracking inspects DataType before backend type validation. */
    if (attr_id == UA_ATTRIBUTEID_DATATYPE &&
        (!wv.value.hasValue ||
         !UA_Variant_hasScalarType(&wv.value.value, &UA_TYPES[UA_TYPES_NODEID]))) {
        UA_WriteValue_clear(&wv);
        return serverAsync_write_status(srv->server,
                                        UA_STATUSCODE_BADTYPEMISMATCH, return_status);
    }

    ServerAsyncCtx *ctx = serverAsync_create_ctx(srv->server, 0);
    if (!ctx) {
        UA_WriteValue_clear(&wv);
        return NULL;
    }

    ctx->return_write_status = (UA_Boolean)return_status;
    PyObject *fut = ctx->future;
    UA_StatusCode sc = UA_Server_write_async(srv->server, &wv,
                                             serverAsyncWriteCallback, ctx, 0);
    UA_WriteValue_clear(&wv);
    if (sc != UA_STATUSCODE_GOOD) {
        Py_DECREF(fut);
        Py_DECREF(ctx->future);
        UA_free(ctx);
        return PyErr_StatusCode(sc);
    }
    return fut;
}

/* ==================================================== *
 *              write_attribute                         *
 * ==================================================== */
PyObject *
pyServer_write_attribute(PyObject *self, PyObject *args) {
    PyObject *py_nodeid, *py_value;
    int attr_id;
    int return_status = 0;

    if (!PyArg_ParseTuple(args, "OiO|p", &py_nodeid, &attr_id, &py_value, &return_status))
        return NULL;
    PyServer *srv = (PyServer *)self;
    const UA_NamespaceMapping *nsMapping = &srv->nsMapPy2UA;
    const UA_DataTypeArray *customDataTypes =
        UA_Server_getConfig(srv->server)->customDataTypes;

    UA_NodeId nodeId;
    if (extract_nodeid(py_nodeid, &nodeId, nsMapping, customDataTypes) < 0)
        return NULL;

    UA_WriteValue wv;
    if (build_write_value(&nodeId, true, attr_id, py_value, &wv,
                          nsMapping, customDataTypes) < 0) {
        UA_NodeId_clear(&nodeId);
        UA_WriteValue_clear(&wv);
        return NULL;
    }
    UA_NodeId_clear(&nodeId);

    ServerAsyncCtx *ctx = serverAsync_create_ctx(srv->server, 0);
    if (!ctx) {
        UA_WriteValue_clear(&wv);
        return NULL;
    }

    ctx->return_write_status = (UA_Boolean)return_status;
    PyObject *fut = ctx->future;
    UA_StatusCode sc = UA_Server_write_async(srv->server, &wv,
                                             serverAsyncWriteCallback, ctx, 0);
    UA_WriteValue_clear(&wv);
    if (sc != UA_STATUSCODE_GOOD) {
        Py_DECREF(fut);
        Py_DECREF(ctx->future);
        UA_free(ctx);
        return PyErr_StatusCode(sc);
    }
    return fut;
}

static void
clearWriteValueWithBorrowedNodeId(UA_WriteValue *wv) {
    UA_NodeId_init(&wv->nodeId);
    UA_WriteValue_clear(wv);
}

PyObject *
pyNode_write_attribute(PyObject *self, PyObject *args) {
    int attr_id;
    PyObject *py_value;
    if(!PyArg_ParseTuple(args, "iO", &attr_id, &py_value))
        return NULL;

    PyServer *srv;
    UA_Node *node = pyNodeStore_attachedNode(self, &srv);
    if(!node)
        return NULL;
    const UA_NamespaceMapping *nsMapping = &srv->nsMapPy2UA;
    const UA_DataTypeArray *customDataTypes =
        UA_Server_getConfig(srv->server)->customDataTypes;

    UA_WriteValue wv;
    if(build_write_value(&node->head.nodeId, false, attr_id, py_value,
                         &wv, nsMapping, customDataTypes) < 0) {
        clearWriteValueWithBorrowedNodeId(&wv);
        return NULL;
    }

    ServerAsyncCtx *ctx = serverAsync_create_ctx(srv->server, 0);
    if(!ctx) {
        clearWriteValueWithBorrowedNodeId(&wv);
        return NULL;
    }

    PyObject *fut = ctx->future;
    lockServer(srv->server);
    UA_StatusCode sc = writeWithNode_async(
        srv->server, &srv->server->adminSession, node, &wv,
        serverAsyncWriteCallback, ctx, 0);
    unlockServer(srv->server);
    clearWriteValueWithBorrowedNodeId(&wv);
    if(sc != UA_STATUSCODE_GOOD) {
        Py_DECREF(fut);
        UA_free(ctx);
        return PyErr_StatusCode(sc);
    }
    return fut;
}

/* ==================================================== *
 *              translate_browse_paths                  *
 * ==================================================== */
PyObject *
pyServer_translate_browse_paths(PyObject *self, PyObject *args) {
    PyObject *py_request;

    if (!PyArg_ParseTuple(args, "O", &py_request))
        return NULL;
    PyServer *srv = (PyServer *)self;
    const UA_NamespaceMapping *nsMapping = &srv->nsMapPy2UA;
    const UA_DataTypeArray *customDataTypes =
        UA_Server_getConfig(srv->server)->customDataTypes;

    UA_TranslateBrowsePathsToNodeIdsRequest req;
    UA_TranslateBrowsePathsToNodeIdsRequest_init(&req);
    PyObject *conv = PY2UA(py_request, &req, &UA_TYPES[UA_TYPES_TRANSLATEBROWSEPATHSTONODEIDSREQUEST], nsMapping, customDataTypes);
    if (!conv)
        return NULL;

    UA_TranslateBrowsePathsToNodeIdsResponse resp;
    UA_TranslateBrowsePathsToNodeIdsResponse_init(&resp);

    if (req.browsePathsSize > 0) {
        resp.results = (UA_BrowsePathResult *)UA_calloc(
            req.browsePathsSize, sizeof(UA_BrowsePathResult));
        if (!resp.results) {
            UA_TranslateBrowsePathsToNodeIdsRequest_clear(&req);
            return PyErr_NoMemory();
        }
        resp.resultsSize = req.browsePathsSize;
        for (size_t i = 0; i < req.browsePathsSize; i++)
            resp.results[i] = UA_Server_translateBrowsePathToNodeIds(
                srv->server, &req.browsePaths[i]);
    }

    PyObject *py_resp = UA2PY(&resp,
        &UA_TYPES[UA_TYPES_TRANSLATEBROWSEPATHSTONODEIDSRESPONSE], nsMapping);

    for (size_t i = 0; i < resp.resultsSize; i++)
        UA_BrowsePathResult_clear(&resp.results[i]);
    UA_free(resp.results);
    resp.results = NULL;
    resp.resultsSize = 0;
    UA_TranslateBrowsePathsToNodeIdsRequest_clear(&req);

    return py_resp;
}

/************************************************************
 * Discovery
 *
 ************************************************************/


PyObject *
pyServer_register_discovery(PyObject *self, PyObject *args) {
    PyObject *py_endpoint_url;
    PyObject *py_semaphore_path = Py_None;
    if (!PyArg_ParseTuple(args, "O|O", &py_endpoint_url, &py_semaphore_path))
        return NULL;

    PyServer *srv = (PyServer *)self;
    const UA_NamespaceMapping *nsMapping = &srv->nsMapPy2UA;
    const UA_DataTypeArray *customDataTypes =
        UA_Server_getConfig(srv->server)->customDataTypes;

    UA_String endpoint_url;
    UA_String_init(&endpoint_url);
    if (!PY2UA(py_endpoint_url, &endpoint_url, &UA_TYPES[UA_TYPES_STRING],
               nsMapping, customDataTypes)) {
        UA_String_clear(&endpoint_url);
        return NULL;
    }

    UA_String semaphore_path;
    UA_String_init(&semaphore_path);
    if (py_semaphore_path != Py_None) {
        if (!PY2UA(py_semaphore_path, &semaphore_path,
                   &UA_TYPES[UA_TYPES_STRING], nsMapping, customDataTypes)) {
            UA_String_clear(&endpoint_url);
            return NULL;
        }
    }

    UA_ClientConfig cc;
    memset(&cc, 0, sizeof(UA_ClientConfig));
    UA_StatusCode cfg_sc = UA_ClientConfig_setDefault(&cc);
    if (cfg_sc != UA_STATUSCODE_GOOD) {
        UA_String_clear(&endpoint_url);
        UA_String_clear(&semaphore_path);
        return PyErr_StatusCode(cfg_sc);
    }
    cc.securityMode = UA_MESSAGESECURITYMODE_NONE;

    UA_StatusCode status = UA_Server_registerDiscovery(
        srv->server, &cc, endpoint_url, semaphore_path);

    UA_String_clear(&endpoint_url);
    UA_String_clear(&semaphore_path);

    if (status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);
    Py_RETURN_NONE;
}

PyObject *
pyServer_deregister_discovery(PyObject *self, PyObject *args) {
    PyObject *py_endpoint_url;
    if (!PyArg_ParseTuple(args, "O", &py_endpoint_url))
        return NULL;

    PyServer *srv = (PyServer *)self;
    const UA_NamespaceMapping *nsMapping = &srv->nsMapPy2UA;
    const UA_DataTypeArray *customDataTypes =
        UA_Server_getConfig(srv->server)->customDataTypes;

    UA_String endpoint_url;
    UA_String_init(&endpoint_url);
    if (!PY2UA(py_endpoint_url, &endpoint_url, &UA_TYPES[UA_TYPES_STRING],
               nsMapping, customDataTypes)) {
        UA_String_clear(&endpoint_url);
        return NULL;
    }

    UA_ClientConfig cc;
    memset(&cc, 0, sizeof(UA_ClientConfig));
    UA_StatusCode cfg_sc = UA_ClientConfig_setDefault(&cc);
    if (cfg_sc != UA_STATUSCODE_GOOD) {
        UA_String_clear(&endpoint_url);
        return PyErr_StatusCode(cfg_sc);
    }

    UA_StatusCode status = UA_Server_deregisterDiscovery(
        srv->server, &cc, endpoint_url);

    UA_String_clear(&endpoint_url);

    if (status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);
    Py_RETURN_NONE;
}

/* Convert a Python sequence of `str` into a freshly-allocated UA_String
 * array. Returns 0 on success (`*out`/`*size` set; `*out` is NULL for an
 * empty sequence), -1 with a Python exception set on failure. */
static int
pystrs_to_ua_string_array(PyObject *seq, const UA_NamespaceMapping *nsMapping,
                          const UA_DataTypeArray *customDataTypes,
                          UA_String **out, size_t *size) {
    PyObject *fast = PySequence_Fast(seq, "expected an iterable of str");
    if (!fast)
        return -1;
    Py_ssize_t count = PySequence_Fast_GET_SIZE(fast);
    UA_String *items = count
        ? (UA_String *)UA_Array_new((size_t)count, &UA_TYPES[UA_TYPES_STRING])
        : NULL;
    if (count && !items) {
        Py_DECREF(fast);
        PyErr_NoMemory();
        return -1;
    }
    for (Py_ssize_t i = 0; i < count; i++) {
        if (!PY2UA(PySequence_Fast_GET_ITEM(fast, i), &items[i],
                   &UA_TYPES[UA_TYPES_STRING], nsMapping, customDataTypes)) {
            UA_Array_delete(items, (size_t)count, &UA_TYPES[UA_TYPES_STRING]);
            Py_DECREF(fast);
            return -1;
        }
    }
    Py_DECREF(fast);
    *out = items;
    *size = (size_t)count;
    return 0;
}

PyObject *
pyServer_register_server(PyObject *self, PyObject *args) {
    PyObject *py_registered_server;
    if (!PyArg_ParseTuple(args, "O", &py_registered_server))
        return NULL;

    PyServer *srv = (PyServer *)self;
    const UA_NamespaceMapping *nsMapping = &srv->nsMapPy2UA;
    const UA_DataTypeArray *customDataTypes =
        UA_Server_getConfig(srv->server)->customDataTypes;

    UA_RegisteredServer rs;
    UA_RegisteredServer_init(&rs);
    if (!PY2UA(py_registered_server, &rs, &UA_TYPES[UA_TYPES_REGISTEREDSERVER],
               nsMapping, customDataTypes)) {
        UA_RegisteredServer_clear(&rs);
        return NULL;
    }

    UA_StatusCode status = UA_Server_registerServer(srv->server, &rs, 0, NULL, NULL);
    UA_RegisteredServer_clear(&rs);

    if (status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);
    Py_RETURN_NONE;
}

PyObject *
pyServer_deregister_server(PyObject *self, PyObject *args) {
    PyObject *py_server_uri;
    PyObject *py_discovery_urls = NULL;
    if (!PyArg_ParseTuple(args, "O|O", &py_server_uri, &py_discovery_urls))
        return NULL;

    PyServer *srv = (PyServer *)self;
    const UA_NamespaceMapping *nsMapping = &srv->nsMapPy2UA;
    const UA_DataTypeArray *customDataTypes =
        UA_Server_getConfig(srv->server)->customDataTypes;

    UA_String server_uri;
    UA_String_init(&server_uri);
    if (!PY2UA(py_server_uri, &server_uri, &UA_TYPES[UA_TYPES_STRING],
               nsMapping, customDataTypes)) {
        UA_String_clear(&server_uri);
        return NULL;
    }

    UA_String *discovery_urls = NULL;
    size_t discovery_urls_size = 0;
    if (py_discovery_urls && py_discovery_urls != Py_None) {
        if (pystrs_to_ua_string_array(py_discovery_urls, nsMapping, customDataTypes,
                                      &discovery_urls, &discovery_urls_size) < 0) {
            UA_String_clear(&server_uri);
            return NULL;
        }
    }

    UA_StatusCode status = UA_Server_deregisterServer(
        srv->server, server_uri, discovery_urls_size, discovery_urls);

    UA_String_clear(&server_uri);
    UA_Array_delete(discovery_urls, discovery_urls_size, &UA_TYPES[UA_TYPES_STRING]);

    if (status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);
    Py_RETURN_NONE;
}

PyObject *
pyServer_register_server_on_network(PyObject *self, PyObject *args) {
    PyObject *py_server_on_network;
    PyObject *py_remote_address = Py_None;
    PyObject *py_ttl = Py_None;
    if (!PyArg_ParseTuple(args, "O|OO", &py_server_on_network,
                          &py_remote_address, &py_ttl))
        return NULL;

    PyServer *srv = (PyServer *)self;
    const UA_NamespaceMapping *nsMapping = &srv->nsMapPy2UA;
    const UA_DataTypeArray *customDataTypes =
        UA_Server_getConfig(srv->server)->customDataTypes;

    UA_ServerOnNetwork son;
    UA_ServerOnNetwork_init(&son);
    if (!PY2UA(py_server_on_network, &son, &UA_TYPES[UA_TYPES_SERVERONNETWORK],
               nsMapping, customDataTypes)) {
        UA_ServerOnNetwork_clear(&son);
        return NULL;
    }

    UA_String remote_address = UA_STRING_NULL;
    UA_UInt32 ttl = 0;
    UA_KeyValuePair kvp[2];
    size_t kvp_size = 0;

    if (py_remote_address != Py_None) {
        if (!PY2UA(py_remote_address, &remote_address, &UA_TYPES[UA_TYPES_STRING],
                   nsMapping, customDataTypes)) {
            UA_ServerOnNetwork_clear(&son);
            return NULL;
        }
        kvp[kvp_size].key.namespaceIndex = 0;
        kvp[kvp_size].key.name = (UA_String)UA_STRING_STATIC("remote-address");
        UA_Variant_setScalar(&kvp[kvp_size].value, &remote_address,
                             &UA_TYPES[UA_TYPES_STRING]);
        kvp_size++;
    }

    if (py_ttl != Py_None) {
        long ttl_value = PyLong_AsLong(py_ttl);
        if (ttl_value < 0 && PyErr_Occurred()) {
            UA_String_clear(&remote_address);
            UA_ServerOnNetwork_clear(&son);
            return NULL;
        }
        ttl = (UA_UInt32)ttl_value;
        kvp[kvp_size].key.namespaceIndex = 0;
        kvp[kvp_size].key.name = (UA_String)UA_STRING_STATIC("ttl");
        UA_Variant_setScalar(&kvp[kvp_size].value, &ttl, &UA_TYPES[UA_TYPES_UINT32]);
        kvp_size++;
    }

    UA_KeyValueMap kvm = {kvp_size, kvp_size ? kvp : NULL};
    UA_StatusCode status = UA_Server_registerServerOnNetwork(srv->server, &son, kvm);

    UA_String_clear(&remote_address);
    UA_ServerOnNetwork_clear(&son);

    if (status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);
    Py_RETURN_NONE;
}

PyObject *
pyServer_deregister_server_on_network(PyObject *self, PyObject *args) {
    PyObject *py_server_name;
    if (!PyArg_ParseTuple(args, "O", &py_server_name))
        return NULL;

    PyServer *srv = (PyServer *)self;
    const UA_NamespaceMapping *nsMapping = &srv->nsMapPy2UA;
    const UA_DataTypeArray *customDataTypes =
        UA_Server_getConfig(srv->server)->customDataTypes;

    UA_String server_name;
    UA_String_init(&server_name);
    if (!PY2UA(py_server_name, &server_name, &UA_TYPES[UA_TYPES_STRING],
               nsMapping, customDataTypes)) {
        UA_String_clear(&server_name);
        return NULL;
    }

    UA_StatusCode status = UA_Server_deregisterServerOnNetwork(srv->server, server_name);

    UA_String_clear(&server_name);

    if (status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);
    Py_RETURN_NONE;
}

PyObject *
pyServer_set_register_server_callback(PyObject *self, PyObject *args) {
    (void)self;
    (void)args;
    PyErr_SetString(PyExc_NotImplementedError,
                    "register-server callbacks are not available with the "
                    "current open62541 discovery API");
    return NULL;
}

PyObject *
pyServer_set_server_on_network_callback(PyObject *self, PyObject *args) {
    (void)self;
    (void)args;
    PyErr_SetString(PyExc_NotImplementedError,
                    "server-on-network callbacks are not available with the "
                    "current open62541 discovery API");
    return NULL;
}

/************************************************************
 * Module type initialisation
 ************************************************************/
int
Server_initTypes(void) {
    if(PyType_Ready(&PyAsyncOperationStateType) < 0)
        return -1;
    return 0;
}
