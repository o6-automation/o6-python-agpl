/* Copyright 2026 (c) o6 Automation GmbH (Author: Andreas Ebner) */
#include "server.h"
#include "../module.h"
#include "../types_internal.h"

/*
 * Helper: Extract a UA_NodeId from a Python object.
 * Converts via PY2UA. Caller must clear the NodeId.
 */
static int
extract_nodeid(PyObject *obj, UA_NodeId *out) {
    UA_NodeId_init(out);
    PyObject *res = PY2UA(obj, out, &UA_TYPES[UA_TYPES_NODEID]);
    if (!res)
        return -1;
    return 0;
}

/*
 * Helper: Extract a UA_QualifiedName from a Python object.
 * Converts via PY2UA. Caller must clear the QualifiedName.
 */
static int
extract_qualifiedname(PyObject *obj, UA_QualifiedName *out) {
    UA_QualifiedName_init(out);
    PyObject *res = PY2UA(obj, out, &UA_TYPES[UA_TYPES_QUALIFIEDNAME]);
    if (!res)
        return -1;
    return 0;
}

/* ================================================================== */
/* Server async infrastructure                                          */
/*                                                                      */
/* Mirrors src/client/client_services_util.c.  Each pyServer_*          */
/* function below allocates a ServerAsyncCtx, calls a UA_Server_*_async */
/* function with a callback that resolves/rejects the asyncio Future,   */
/* and returns the Future to Python.                                    */
/* ================================================================== */

typedef struct {
    PyObject *future;
    int attr_id; /* AttributeId for read callbacks (to know how to convert) */
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
serverAsync_convert_read(int attr_id, const UA_DataValue *dv) {
    if (!dv->hasValue || dv->value.type == NULL) {
        PyErr_SetString(PyExc_RuntimeError, "Server returned no value");
        return NULL;
    }
    /* Value (13) and ArrayDimensions (16) → return the Variant */
    if (attr_id == 13 || attr_id == 16)
        return UA2PY((void*)&dv->value, &UA_TYPES[UA_TYPES_VARIANT]);
    /* For every other attribute, the variant carries a single scalar of
     * the matching builtin type — return the unwrapped scalar. */
    return UA2PY(dv->value.data, dv->value.type);
}

static void
serverAsyncReadCallback(UA_Server *server, void *asyncOpContext,
                        const UA_DataValue *result) {
    WITH_OWNER(server);
    ServerAsyncCtx *ctx = (ServerAsyncCtx*)asyncOpContext;
    UA_ServerConfig *config = UA_Server_getConfig(server);
    /* Teardown guard: mirror asyncServiceCallback */
    if (!config->context) {
        Py_DECREF(ctx->future);
        UA_free(ctx);
        return;
    }
    assertGIL();
    if (result->hasStatus && result->status != UA_STATUSCODE_GOOD) {
        serverAsync_reject_status(ctx, result->status);
        return;
    }
    PyObject *py_result = serverAsync_convert_read(ctx->attr_id, result);
    serverAsync_resolve(ctx, py_result);
    WITH_OWNER_END();
}

static void
serverAsyncWriteCallback(UA_Server *server, void *asyncOpContext,
                         UA_StatusCode result) {
    WITH_OWNER(server);
    ServerAsyncCtx *ctx = (ServerAsyncCtx*)asyncOpContext;
    UA_ServerConfig *config = UA_Server_getConfig(server);
    if (!config->context) {
        Py_DECREF(ctx->future);
        UA_free(ctx);
        return;
    }
    assertGIL();
    if (result != UA_STATUSCODE_GOOD) {
        serverAsync_reject_status(ctx, result);
        return;
    }
    Py_INCREF(Py_None);
    serverAsync_resolve(ctx, Py_None);
    WITH_OWNER_END();
}

static void
serverAsyncCallCallback(UA_Server *server, void *asyncOpContext,
                        const UA_CallMethodResult *result) {
    WITH_OWNER(server);
    ServerAsyncCtx *ctx = (ServerAsyncCtx*)asyncOpContext;
    UA_ServerConfig *config = UA_Server_getConfig(server);
    if (!config->context) {
        Py_DECREF(ctx->future);
        UA_free(ctx);
        return;
    }
    assertGIL();
    if (result->statusCode != UA_STATUSCODE_GOOD) {
        serverAsync_reject_status(ctx, result->statusCode);
        return;
    }
    /* Build (StatusCode, output1, output2, ...) tuple — same shape as
     * the previous synchronous pyServer_call return value. */
    Py_ssize_t out_count = (Py_ssize_t)result->outputArgumentsSize;
    PyObject *ret = PyTuple_New(1 + out_count);
    if (!ret) {
        serverAsync_resolve(ctx, NULL);
        return;
    }
    PyObject *sc = UA2PY((void*)&result->statusCode,
                         &UA_TYPES[UA_TYPES_STATUSCODE]);
    if (!sc) {
        Py_DECREF(ret);
        serverAsync_resolve(ctx, NULL);
        return;
    }
    PyTuple_SET_ITEM(ret, 0, sc);
    for (Py_ssize_t i = 0; i < out_count; i++) {
        PyObject *v = UA2PY(&result->outputArguments[i],
                            &UA_TYPES[UA_TYPES_VARIANT]);
        if (!v) {
            Py_DECREF(ret);
            serverAsync_resolve(ctx, NULL);
            return;
        }
        PyTuple_SET_ITEM(ret, 1 + i, v);
    }
    serverAsync_resolve(ctx, ret);
    WITH_OWNER_END();
}

/* Convert a Python value into a UA_WriteValue's `value` field for the
 * given AttributeId.  Returns 0 on success, -1 on error (Python
 * exception set).  Caller must clear `wv` regardless. */
static int
build_write_value(const UA_NodeId *nodeId, int attr_id, PyObject *py_value,
                  UA_WriteValue *wv) {
    UA_WriteValue_init(wv);
    if (UA_NodeId_copy(nodeId, &wv->nodeId) != UA_STATUSCODE_GOOD) {
        PyErr_NoMemory();
        return -1;
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
            if (!PY2UA(py_value, &qn, &UA_TYPES[UA_TYPES_QUALIFIEDNAME]))
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
            if (!PY2UA(py_value, &lt, &UA_TYPES[UA_TYPES_LOCALIZEDTEXT]))
                return -1;
            UA_StatusCode sc = UA_Variant_setScalarCopy(
                var, &lt, &UA_TYPES[UA_TYPES_LOCALIZEDTEXT]);
            UA_LocalizedText_clear(&lt);
            if (sc != UA_STATUSCODE_GOOD) { PyErr_NoMemory(); return -1; }
            break;
        }
        case 6: { /* WriteMask */
            unsigned long v = PyLong_AsUnsignedLong(py_value);
            if (v == (unsigned long)-1 && PyErr_Occurred()) return -1;
            UA_UInt32 vv = (UA_UInt32)v;
            if (UA_Variant_setScalarCopy(var, &vv, &UA_TYPES[UA_TYPES_UINT32])
                != UA_STATUSCODE_GOOD) { PyErr_NoMemory(); return -1; }
            break;
        }
        case 13: { /* Value — move the variant in directly */
            if (!PY2UA(py_value, var, &UA_TYPES[UA_TYPES_VARIANT]))
                return -1;
            break;
        }
        case 14: { /* DataType */
            UA_NodeId dt;
            UA_NodeId_init(&dt);
            if (!PY2UA(py_value, &dt, &UA_TYPES[UA_TYPES_NODEID]))
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
            if (!PY2UA(py_value, var, &UA_TYPES[UA_TYPES_VARIANT]))
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
            PyErr_SetString(PyExc_ValueError,
                            "Unsupported or read-only AttributeId");
            return -1;
    }
    return 0;
}

PyObject *
pyServer_find_data_type(PyObject *self, PyObject *args) {
    WITH_OWNER(((PyServer*)self)->server);
    PyObject *nodeId_obj;
    if (!PyArg_ParseTuple(args, "O", &nodeId_obj))
        return NULL;

    UA_NodeId typeId;
    UA_NodeId_init(&typeId);
    if (PY2UA(nodeId_obj, &typeId, &UA_TYPES[UA_TYPES_NODEID]) == NULL)
        return NULL;

    PyServer *srv = (PyServer *)self;
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
    if (PyDict_SetItemString(d, "type_name", name) < 0)
        goto fail_name;
    Py_DECREF(name);

    PyObject *tid = UA2PY((void *)&dt->typeId, &UA_TYPES[UA_TYPES_NODEID]);
    if (!tid)
        goto fail;
    if (PyDict_SetItemString(d, "type_id", tid) < 0)
        goto fail_tid;
    Py_DECREF(tid);

    PyObject *bid = UA2PY((void *)&dt->binaryEncodingId, &UA_TYPES[UA_TYPES_NODEID]);
    if (!bid)
        goto fail;
    if (PyDict_SetItemString(d, "binary_encoding_id", bid) < 0)
        goto fail_bid;
    Py_DECREF(bid);

    PyObject *kind = PyLong_FromUnsignedLong(dt->typeKind);
    if (!kind)
        goto fail;
    if (PyDict_SetItemString(d, "type_kind", kind) < 0)
        goto fail_kind;
    Py_DECREF(kind);

    PyObject *ms = PyLong_FromUnsignedLong(dt->membersSize);
    if (!ms)
        goto fail;
    if (PyDict_SetItemString(d, "members_size", ms) < 0)
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
    WITH_OWNER_END();
}

/************************************************************
 * add_variable_node(requested_id, parent_id, ref_type_id,
 *                   browse_name, type_definition, attributes)
 ************************************************************/
PyObject *
pyServer_add_variable_node(PyObject *self, PyObject *args) {
    WITH_OWNER(((PyServer*)self)->server);
    PyObject *py_requested, *py_parent, *py_reftype,
             *py_browse, *py_typedef, *py_attr;

    if (!PyArg_ParseTuple(args, "OOOOOO", &py_requested, &py_parent,
                          &py_reftype, &py_browse, &py_typedef, &py_attr))
        return NULL;

    UA_NodeId requestedId, parentId, refTypeId, typeDef;
    UA_QualifiedName browseName;
    UA_VariableAttributes attr;

    if (extract_nodeid(py_requested, &requestedId) < 0) return NULL;
    if (extract_nodeid(py_parent, &parentId) < 0) goto fail_parent;
    if (extract_nodeid(py_reftype, &refTypeId) < 0) goto fail_reftype;
    if (extract_qualifiedname(py_browse, &browseName) < 0) goto fail_browse;
    if (extract_nodeid(py_typedef, &typeDef) < 0) goto fail_typedef;

    UA_VariableAttributes_init(&attr);
    PyObject *conv = PY2UA(py_attr, &attr,
                           &UA_TYPES[UA_TYPES_VARIABLEATTRIBUTES]);
    if (!conv) goto fail_attr;

    UA_NodeId outId;
    UA_NodeId_init(&outId);
    PyServer *srv = (PyServer *)self;
    UA_StatusCode status = UA_Server_addVariableNode(
        srv->server, requestedId, parentId, refTypeId,
        browseName, typeDef, attr, NULL, &outId);

    UA_VariableAttributes_clear(&attr);
    UA_NodeId_clear(&typeDef);
    UA_QualifiedName_clear(&browseName);
    UA_NodeId_clear(&refTypeId);
    UA_NodeId_clear(&parentId);
    UA_NodeId_clear(&requestedId);

    if (status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);

    PyObject *result = UA2PY(&outId, &UA_TYPES[UA_TYPES_NODEID]);
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
    WITH_OWNER_END();
}

/************************************************************
 * add_object_node(requested_id, parent_id, ref_type_id,
 *                 browse_name, type_definition, attributes)
 ************************************************************/
PyObject *
pyServer_add_object_node(PyObject *self, PyObject *args) {
    WITH_OWNER(((PyServer*)self)->server);
    PyObject *py_requested, *py_parent, *py_reftype,
             *py_browse, *py_typedef, *py_attr;

    if (!PyArg_ParseTuple(args, "OOOOOO", &py_requested, &py_parent,
                          &py_reftype, &py_browse, &py_typedef, &py_attr))
        return NULL;

    UA_NodeId requestedId, parentId, refTypeId, typeDef;
    UA_QualifiedName browseName;
    UA_ObjectAttributes attr;

    if (extract_nodeid(py_requested, &requestedId) < 0) return NULL;
    if (extract_nodeid(py_parent, &parentId) < 0) goto fail_parent;
    if (extract_nodeid(py_reftype, &refTypeId) < 0) goto fail_reftype;
    if (extract_qualifiedname(py_browse, &browseName) < 0) goto fail_browse;
    if (extract_nodeid(py_typedef, &typeDef) < 0) goto fail_typedef;

    UA_ObjectAttributes_init(&attr);
    PyObject *conv = PY2UA(py_attr, &attr,
                           &UA_TYPES[UA_TYPES_OBJECTATTRIBUTES]);
    if (!conv) goto fail_attr;

    UA_NodeId outId;
    UA_NodeId_init(&outId);
    PyServer *srv = (PyServer *)self;
    UA_StatusCode status = UA_Server_addObjectNode(
        srv->server, requestedId, parentId, refTypeId,
        browseName, typeDef, attr, NULL, &outId);

    UA_ObjectAttributes_clear(&attr);
    UA_NodeId_clear(&typeDef);
    UA_QualifiedName_clear(&browseName);
    UA_NodeId_clear(&refTypeId);
    UA_NodeId_clear(&parentId);
    UA_NodeId_clear(&requestedId);

    if (status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);

    PyObject *result = UA2PY(&outId, &UA_TYPES[UA_TYPES_NODEID]);
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
    WITH_OWNER_END();
}

/************************************************************
 * add_object_type_node(requested_id, parent_id, ref_type_id,
 *                      browse_name, attributes)
 ************************************************************/
PyObject *
pyServer_add_object_type_node(PyObject *self, PyObject *args) {
    WITH_OWNER(((PyServer*)self)->server);
    PyObject *py_requested, *py_parent, *py_reftype,
             *py_browse, *py_attr;

    if (!PyArg_ParseTuple(args, "OOOOO", &py_requested, &py_parent,
                          &py_reftype, &py_browse, &py_attr))
        return NULL;

    UA_NodeId requestedId, parentId, refTypeId;
    UA_QualifiedName browseName;
    UA_ObjectTypeAttributes attr;

    if (extract_nodeid(py_requested, &requestedId) < 0) return NULL;
    if (extract_nodeid(py_parent, &parentId) < 0) goto fail_parent;
    if (extract_nodeid(py_reftype, &refTypeId) < 0) goto fail_reftype;
    if (extract_qualifiedname(py_browse, &browseName) < 0) goto fail_browse;

    UA_ObjectTypeAttributes_init(&attr);
    PyObject *conv = PY2UA(py_attr, &attr,
                           &UA_TYPES[UA_TYPES_OBJECTTYPEATTRIBUTES]);
    if (!conv) goto fail_attr;

    UA_NodeId outId;
    UA_NodeId_init(&outId);
    PyServer *srv = (PyServer *)self;
    UA_StatusCode status = UA_Server_addObjectTypeNode(
        srv->server, requestedId, parentId, refTypeId,
        browseName, attr, NULL, &outId);

    UA_ObjectTypeAttributes_clear(&attr);
    UA_QualifiedName_clear(&browseName);
    UA_NodeId_clear(&refTypeId);
    UA_NodeId_clear(&parentId);
    UA_NodeId_clear(&requestedId);

    if (status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);

    PyObject *result = UA2PY(&outId, &UA_TYPES[UA_TYPES_NODEID]);
    UA_NodeId_clear(&outId);
    return result;

fail_attr:
    UA_QualifiedName_clear(&browseName);
fail_browse:
    UA_NodeId_clear(&refTypeId);
fail_reftype:
    UA_NodeId_clear(&parentId);
fail_parent:
    UA_NodeId_clear(&requestedId);
    return NULL;
    WITH_OWNER_END();
}

/************************************************************
 * add_data_type_node(requested_id, parent_id, ref_type_id,
 *                    browse_name, attributes)
 ************************************************************/
PyObject *
pyServer_add_data_type_node(PyObject *self, PyObject *args) {
    WITH_OWNER(((PyServer*)self)->server);
    PyObject *py_requested, *py_parent, *py_reftype,
             *py_browse, *py_attr;

    if (!PyArg_ParseTuple(args, "OOOOO", &py_requested, &py_parent,
                          &py_reftype, &py_browse, &py_attr))
        return NULL;

    UA_NodeId requestedId, parentId, refTypeId;
    UA_QualifiedName browseName;
    UA_DataTypeAttributes attr;

    if (extract_nodeid(py_requested, &requestedId) < 0) return NULL;
    if (extract_nodeid(py_parent, &parentId) < 0) goto fail_parent;
    if (extract_nodeid(py_reftype, &refTypeId) < 0) goto fail_reftype;
    if (extract_qualifiedname(py_browse, &browseName) < 0) goto fail_browse;

    UA_DataTypeAttributes_init(&attr);
    PyObject *conv = PY2UA(py_attr, &attr,
                           &UA_TYPES[UA_TYPES_DATATYPEATTRIBUTES]);
    if (!conv) goto fail_attr;

    UA_NodeId outId;
    UA_NodeId_init(&outId);
    PyServer *srv = (PyServer *)self;
    UA_StatusCode status = UA_Server_addDataTypeNode(
        srv->server, requestedId, parentId, refTypeId,
        browseName, attr, NULL, &outId);

    UA_DataTypeAttributes_clear(&attr);
    UA_QualifiedName_clear(&browseName);
    UA_NodeId_clear(&refTypeId);
    UA_NodeId_clear(&parentId);
    UA_NodeId_clear(&requestedId);

    if (status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);

    PyObject *result = UA2PY(&outId, &UA_TYPES[UA_TYPES_NODEID]);
    UA_NodeId_clear(&outId);
    return result;

fail_attr:
    UA_QualifiedName_clear(&browseName);
fail_browse:
    UA_NodeId_clear(&refTypeId);
fail_reftype:
    UA_NodeId_clear(&parentId);
fail_parent:
    UA_NodeId_clear(&requestedId);
    return NULL;
    WITH_OWNER_END();
}

/************************************************************
 * add_variable_type_node(requested_id, parent_id, ref_type_id,
 *                        browse_name, type_definition, attributes)
 ************************************************************/
PyObject *
pyServer_add_variable_type_node(PyObject *self, PyObject *args) {
    WITH_OWNER(((PyServer*)self)->server);
    PyObject *py_requested, *py_parent, *py_reftype,
             *py_browse, *py_typedef, *py_attr;

    if (!PyArg_ParseTuple(args, "OOOOOO", &py_requested, &py_parent,
                          &py_reftype, &py_browse, &py_typedef, &py_attr))
        return NULL;

    UA_NodeId requestedId, parentId, refTypeId, typeDef;
    UA_QualifiedName browseName;
    UA_VariableTypeAttributes attr;

    if (extract_nodeid(py_requested, &requestedId) < 0) return NULL;
    if (extract_nodeid(py_parent, &parentId) < 0) goto fail_parent;
    if (extract_nodeid(py_reftype, &refTypeId) < 0) goto fail_reftype;
    if (extract_qualifiedname(py_browse, &browseName) < 0) goto fail_browse;
    if (extract_nodeid(py_typedef, &typeDef) < 0) goto fail_typedef;

    UA_VariableTypeAttributes_init(&attr);
    PyObject *conv = PY2UA(py_attr, &attr,
                           &UA_TYPES[UA_TYPES_VARIABLETYPEATTRIBUTES]);
    if (!conv) goto fail_attr;

    UA_NodeId outId;
    UA_NodeId_init(&outId);
    PyServer *srv = (PyServer *)self;
    UA_StatusCode status = UA_Server_addVariableTypeNode(
        srv->server, requestedId, parentId, refTypeId,
        browseName, typeDef, attr, NULL, &outId);

    UA_VariableTypeAttributes_clear(&attr);
    UA_NodeId_clear(&typeDef);
    UA_QualifiedName_clear(&browseName);
    UA_NodeId_clear(&refTypeId);
    UA_NodeId_clear(&parentId);
    UA_NodeId_clear(&requestedId);

    if (status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);

    PyObject *result = UA2PY(&outId, &UA_TYPES[UA_TYPES_NODEID]);
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
    WITH_OWNER_END();
}

/************************************************************
 * Method Node — Callback infrastructure
 ************************************************************/

/* Storage for Python method callbacks */
typedef struct {
    PyObject *callback;
    UA_NodeId methodId;
    UA_Server *server;
} PythonMethodCallback;

static PythonMethodCallback *method_callbacks = NULL;
static size_t method_callbacks_size = 0;
static size_t method_callbacks_capacity = 0;

static void
store_method_callback(PyObject *callback, const UA_NodeId *methodId,
                      UA_Server *server) {
    if (method_callbacks_size >= method_callbacks_capacity) {
        method_callbacks_capacity =
            method_callbacks_capacity == 0 ? 4 : method_callbacks_capacity * 2;
        method_callbacks = realloc(method_callbacks,
            method_callbacks_capacity * sizeof(PythonMethodCallback));
    }

    method_callbacks[method_callbacks_size].callback = callback;
    Py_INCREF(callback);
    UA_NodeId_copy(methodId, &method_callbacks[method_callbacks_size].methodId);
    method_callbacks[method_callbacks_size].server = server;
    method_callbacks_size++;
}

static void
remove_method_callback(const UA_NodeId *methodId, UA_Server *server) {
    for (size_t i = 0; i < method_callbacks_size; i++) {
        if (UA_NodeId_equal(methodId, &method_callbacks[i].methodId) &&
            server == method_callbacks[i].server) {
            Py_DECREF(method_callbacks[i].callback);
            UA_NodeId_clear(&method_callbacks[i].methodId);
            if (i < method_callbacks_size - 1)
                method_callbacks[i] = method_callbacks[method_callbacks_size - 1];
            method_callbacks_size--;
            break;
        }
    }
}

/************************************************************
 * Async method callback infrastructure
 *
 * When a Python method callback is an async def, pyMethodCallback
 * schedules it as an asyncio.Task and returns
 * UA_STATUSCODE_GOODCOMPLETESASYNCHRONOUSLY.  The PyMethodDoneCb
 * done-callback resolves the pending OPC UA service call later via
 * UA_Server_setAsyncCallMethodResult.
 ************************************************************/

typedef struct {
    UA_Variant *output;       /* output array owned by open62541, do NOT use after cancel */
    size_t      outputSize;
    UA_Server  *server;       /* nulled during server teardown */
    UA_Boolean  cancelled;    /* set by cancel callback or server teardown */
    PyObject   *task;         /* asyncio.Task, strong ref (may form a cycle — GC safe) */
} AsyncMethodCtx;

static AsyncMethodCtx **async_method_ctx_list = NULL;
static size_t async_method_ctx_size = 0;
static size_t async_method_ctx_capacity = 0;

static void
async_method_ctx_append(AsyncMethodCtx *ctx) {
    if (async_method_ctx_size >= async_method_ctx_capacity) {
        size_t newcap = async_method_ctx_capacity == 0 ? 4 : async_method_ctx_capacity * 2;
        async_method_ctx_list = realloc(async_method_ctx_list,
                                        newcap * sizeof(AsyncMethodCtx *));
        async_method_ctx_capacity = newcap;
    }
    async_method_ctx_list[async_method_ctx_size++] = ctx;
}

static void
async_method_ctx_remove(AsyncMethodCtx *ctx) {
    for (size_t i = 0; i < async_method_ctx_size; i++) {
        if (async_method_ctx_list[i] == ctx) {
            async_method_ctx_list[i] = async_method_ctx_list[--async_method_ctx_size];
            return;
        }
    }
}

/* Forward declaration — defined below after PyMethodDoneCbType */
static void asyncMethodCancelCallback(UA_Server *server, const void *out);

typedef struct {
    PyObject_HEAD
    AsyncMethodCtx *ctx; /* NULL after the callback has fired */
} PyMethodDoneCb;

static PyObject *
PyMethodDoneCb_call(PyObject *self, PyObject *args, PyObject *kwargs) {
    PyMethodDoneCb *cb = (PyMethodDoneCb *)self;
    AsyncMethodCtx *ctx = cb->ctx;
    if (!ctx) {
        Py_RETURN_NONE; /* already consumed */
    }
    cb->ctx = NULL; /* prevent double-call */

    assertGIL();

    /* Retrieve the task that completed (first positional arg from asyncio) */
    PyObject *task = NULL;
    if (args && PyTuple_Check(args) && PyTuple_GET_SIZE(args) >= 1)
        task = PyTuple_GET_ITEM(args, 0);

    UA_StatusCode result_status = UA_STATUSCODE_GOOD;

    if (ctx->cancelled || !ctx->server) {
        /* Operation was cancelled or server is tearing down.
         * open62541 already freed or invalidated the output pointer — do not
         * touch it.  Just clean up our tracking state. */
        goto cleanup;
    }

    /* Extract the task result; raises if the task raised an exception. */
    {
        PyObject *py_result = NULL;
        if (task) {
            py_result = PyObject_CallMethod(task, "result", NULL);
        }

        if (!py_result) {
            PyErr_Clear();
            result_status = UA_STATUSCODE_BADINTERNALERROR;
        } else {
            /* Convert Python result(s) to the output Variant array —
             * same logic as the synchronous path in pyMethodCallback. */
            if (ctx->outputSize > 0) {
                if (PyList_Check(py_result) || PyTuple_Check(py_result)) {
                    PyObject *seq = PySequence_Fast(py_result, "expected sequence");
                    if (!seq) {
                        result_status = UA_STATUSCODE_BADINTERNALERROR;
                        PyErr_Clear();
                    } else {
                        Py_ssize_t n = PySequence_Fast_GET_SIZE(seq);
                        if ((size_t)n != ctx->outputSize) {
                            result_status = UA_STATUSCODE_BADINVALIDARGUMENT;
                        } else {
                            for (size_t i = 0; i < ctx->outputSize; i++) {
                                PyObject *item = PySequence_Fast_GET_ITEM(seq, (Py_ssize_t)i);
                                PyObject *conv = PY2UA(item, &ctx->output[i],
                                                       &UA_TYPES[UA_TYPES_VARIANT]);
                                if (!conv) {
                                    result_status = UA_STATUSCODE_BADINTERNALERROR;
                                    PyErr_Clear();
                                    break;
                                }
                            }
                        }
                        Py_DECREF(seq);
                    }
                } else if (ctx->outputSize == 1) {
                    PyObject *conv = PY2UA(py_result, &ctx->output[0],
                                           &UA_TYPES[UA_TYPES_VARIANT]);
                    if (!conv) {
                        result_status = UA_STATUSCODE_BADINTERNALERROR;
                        PyErr_Clear();
                    }
                }
            }
            Py_DECREF(py_result);
        }

        UA_Server_setAsyncCallMethodResult(ctx->server, ctx->output, result_status);
    }

cleanup:
    async_method_ctx_remove(ctx);
    Py_DECREF(ctx->task);
    UA_free(ctx);
    Py_RETURN_NONE;
}

static void
PyMethodDoneCb_dealloc(PyObject *self) {
    PyMethodDoneCb *cb = (PyMethodDoneCb *)self;
    if (cb->ctx) {
        /* Done callback was never called (task GC'd without completion).
         * Best-effort: signal failure to open62541 if server is still alive. */
        AsyncMethodCtx *ctx = cb->ctx;
        cb->ctx = NULL;
        if (!ctx->cancelled && ctx->server) {
            UA_Server_setAsyncCallMethodResult(ctx->server, ctx->output,
                                               UA_STATUSCODE_BADINTERNALERROR);
        }
        async_method_ctx_remove(ctx);
        Py_XDECREF(ctx->task);
        UA_free(ctx);
    }
    Py_TYPE(self)->tp_free(self);
}

PyTypeObject PyMethodDoneCbType = {
    PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name      = "_o6.MethodDoneCb",
    .tp_basicsize = sizeof(PyMethodDoneCb),
    .tp_dealloc   = PyMethodDoneCb_dealloc,
    .tp_call      = PyMethodDoneCb_call,
    .tp_flags     = Py_TPFLAGS_DEFAULT,
};

/* Called by open62541 when an async operation is cancelled (e.g. timeout).
 * `out` is the output pointer passed to the method callback. */
static void
asyncMethodCancelCallback(UA_Server *server, const void *out) {
    assertGIL();
    for (size_t i = 0; i < async_method_ctx_size; i++) {
        AsyncMethodCtx *ctx = async_method_ctx_list[i];
        if (ctx->server == server && ctx->output == (const UA_Variant *)out) {
            ctx->cancelled = UA_TRUE;
            PyObject *r = PyObject_CallMethod(ctx->task, "cancel", NULL);
            Py_XDECREF(r);
            /* ctx cleanup happens in PyMethodDoneCb_call when the task
             * cancellation propagates to the done callback. */
            return;
        }
    }
}

void
clear_server_callbacks(UA_Server *server) {
    for (size_t i = 0; i < method_callbacks_size; ) {
        if (method_callbacks[i].server == server) {
            Py_DECREF(method_callbacks[i].callback);
            UA_NodeId_clear(&method_callbacks[i].methodId);
            if (i < method_callbacks_size - 1)
                method_callbacks[i] = method_callbacks[method_callbacks_size - 1];
            method_callbacks_size--;
        } else {
            i++;
        }
    }

    /* Mark all pending async method ops for this server as cancelled.
     * We null ctx->server so that if the done callback fires later it will
     * not attempt to call UA_Server_setAsyncCallMethodResult on a dead server.
     * We do NOT free ctx here — PyMethodDoneCb_call (or PyMethodDoneCb_dealloc)
     * owns the lifetime and will free it when the task resolves or is GC'd. */
    for (size_t i = 0; i < async_method_ctx_size; i++) {
        AsyncMethodCtx *ctx = async_method_ctx_list[i];
        if (ctx->server == server) {
            ctx->cancelled = UA_TRUE;
            ctx->server = NULL;
        }
    }
}

/* C callback that dispatches to Python */
static UA_StatusCode
pyMethodCallback(UA_Server *server,
                 const UA_NodeId *sessionId, void *sessionContext,
                 const UA_NodeId *methodId, void *methodContext,
                 const UA_NodeId *objectId, void *objectContext,
                 size_t inputSize, const UA_Variant *input,
                 size_t outputSize, UA_Variant *output) {
    WITH_OWNER(server);
    /* Find the Python callback */
    PyObject *callback = NULL;
    for (size_t i = 0; i < method_callbacks_size; i++) {
        if (server == method_callbacks[i].server &&
            UA_NodeId_equal(methodId, &method_callbacks[i].methodId)) {
            callback = method_callbacks[i].callback;
            break;
        }
    }

    if (!callback)
        return UA_STATUSCODE_BADINTERNALERROR;

    /* Ensure we hold the GIL */
    assertGIL();

    /* Convert input variants to a Python tuple for unpacking */
    PyObject *py_inputs = PyTuple_New((Py_ssize_t)inputSize);
    if (!py_inputs)
        return UA_STATUSCODE_BADINTERNALERROR;

    for (size_t i = 0; i < inputSize; i++) {
        PyObject *val = UA2PY((void *)&input[i], &UA_TYPES[UA_TYPES_VARIANT]);
        if (!val) {
            Py_DECREF(py_inputs);
            PyErr_Print();
            return UA_STATUSCODE_BADINTERNALERROR;
        }
        PyTuple_SET_ITEM(py_inputs, (Py_ssize_t)i, val);
    }

    /* Call the Python function: callback(*inputs) */
    PyObject *py_result = PyObject_Call(callback, py_inputs, NULL);
    Py_DECREF(py_inputs);

    if (!py_result) {
        PyErr_Print();
        return UA_STATUSCODE_BADINTERNALERROR;
    }

    /* ------------------------------------------------------------------ */
    /* Async path: if the callback is an async def, the result is a        */
    /* coroutine.  Schedule it as an asyncio.Task and return               */
    /* GoodCompletesAsynchronously so open62541 keeps the operation alive. */
    /* ------------------------------------------------------------------ */
    if (PyCoro_CheckExact(py_result)) {
        UA_ServerConfig *config = UA_Server_getConfig(server);
        if (!config->eventLoop) {
            /* Server not running on an asyncio loop — cannot execute coroutine */
            Py_DECREF(py_result);
            return UA_STATUSCODE_BADNOTIMPLEMENTED;
        }
        AsyncIOLoop *el = (AsyncIOLoop *)config->eventLoop;
        if (el->tearingDown) {
            Py_DECREF(py_result);
            return UA_STATUSCODE_BADSHUTDOWN;
        }

        AsyncMethodCtx *ctx = (AsyncMethodCtx *)UA_calloc(1, sizeof(AsyncMethodCtx));
        if (!ctx) {
            Py_DECREF(py_result);
            return UA_STATUSCODE_BADOUTOFMEMORY;
        }
        ctx->output     = output;
        ctx->outputSize = outputSize;
        ctx->server     = server;
        ctx->cancelled  = UA_FALSE;

        /* Create task; create_task steals no reference to the coro, so decref ours */
        PyObject *task = PyObject_CallMethod(el->pyLoop, "create_task", "O", py_result);
        Py_DECREF(py_result);
        if (!task) {
            UA_free(ctx);
            PyErr_Print();
            return UA_STATUSCODE_BADINTERNALERROR;
        }
        ctx->task = task; /* strong ref */

        /* Attach done callback */
        PyMethodDoneCb *done_cb = PyObject_New(PyMethodDoneCb, &PyMethodDoneCbType);
        if (!done_cb) {
            Py_DECREF(task);
            UA_free(ctx);
            return UA_STATUSCODE_BADOUTOFMEMORY;
        }
        done_cb->ctx = ctx;
        PyObject *r = PyObject_CallMethod(task, "add_done_callback", "O",
                                          (PyObject *)done_cb);
        Py_DECREF(done_cb);
        Py_XDECREF(r);

        async_method_ctx_append(ctx);

        /* Register cancel callback (idempotent — safe to overwrite with same value) */
        config->asyncOperationCancelCallback = asyncMethodCancelCallback;

        return UA_STATUSCODE_GOODCOMPLETESASYNCHRONOUSLY;
    }

    /* ------------------------------------------------------------------ */
    /* Synchronous path (original behaviour)                               */
    /* ------------------------------------------------------------------ */

    if (outputSize > 0) {
        if (PyList_Check(py_result) || PyTuple_Check(py_result)) {
            PyObject *seq = PySequence_Fast(py_result, "expected sequence");
            Py_ssize_t n = PySequence_Fast_GET_SIZE(seq);
            if ((size_t)n != outputSize) {
                Py_DECREF(seq);
                Py_DECREF(py_result);
                PyErr_Print();
                return UA_STATUSCODE_BADINVALIDARGUMENT;
            }
            for (size_t i = 0; i < outputSize; i++) {
                PyObject *item = PySequence_Fast_GET_ITEM(seq, (Py_ssize_t)i);
                PyObject *conv = PY2UA(item, &output[i],
                                       &UA_TYPES[UA_TYPES_VARIANT]);
                if (!conv) {
                    Py_DECREF(seq);
                    Py_DECREF(py_result);
                    PyErr_Print();
                    return UA_STATUSCODE_BADINTERNALERROR;
                }
            }
            Py_DECREF(seq);
        } else if (outputSize == 1) {
            /* Single return value → wrap in Variant */
            PyObject *conv = PY2UA(py_result, &output[0],
                                   &UA_TYPES[UA_TYPES_VARIANT]);
            if (!conv) {
                Py_DECREF(py_result);
                PyErr_Print();
                return UA_STATUSCODE_BADINTERNALERROR;
            }
        }
    }

    Py_DECREF(py_result);
    return UA_STATUSCODE_GOOD;
    WITH_OWNER_END();
}

/************************************************************
 * add_method_node(requested_id, parent_id, ref_type_id,
 *                 browse_name, attributes, callback,
 *                 input_arguments, output_arguments)
 ************************************************************/
PyObject *
pyServer_add_method_node(PyObject *self, PyObject *args) {
    WITH_OWNER(((PyServer*)self)->server);
    PyObject *py_requested, *py_parent, *py_reftype,
             *py_browse, *py_attr, *py_callback,
             *py_inargs, *py_outargs;

    if (!PyArg_ParseTuple(args, "OOOOOOOO", &py_requested, &py_parent,
                          &py_reftype, &py_browse, &py_attr, &py_callback,
                          &py_inargs, &py_outargs))
        return NULL;

    if (!PyCallable_Check(py_callback)) {
        PyErr_SetString(PyExc_TypeError, "callback must be callable");
        return NULL;
    }

    UA_NodeId requestedId, parentId, refTypeId;
    UA_QualifiedName browseName;
    UA_MethodAttributes attr;

    if (extract_nodeid(py_requested, &requestedId) < 0) return NULL;
    if (extract_nodeid(py_parent, &parentId) < 0) goto fail_parent;
    if (extract_nodeid(py_reftype, &refTypeId) < 0) goto fail_reftype;
    if (extract_qualifiedname(py_browse, &browseName) < 0) goto fail_browse;

    UA_MethodAttributes_init(&attr);
    PyObject *conv = PY2UA(py_attr, &attr,
                           &UA_TYPES[UA_TYPES_METHODATTRIBUTES]);
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
                PyObject *c = PY2UA(item, &inputArgs[i],
                                    &UA_TYPES[UA_TYPES_ARGUMENT]);
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
                PyObject *c = PY2UA(item, &outputArgs[i],
                                    &UA_TYPES[UA_TYPES_ARGUMENT]);
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
    PyServer *srv = (PyServer *)self;
    UA_StatusCode status = UA_Server_addMethodNode(
        srv->server, requestedId, parentId, refTypeId,
        browseName, attr, pyMethodCallback,
        inputSize, inputArgs, outputSize, outputArgs,
        NULL, &outId);

    /* Cleanup argument arrays */
    for (size_t i = 0; i < inputSize; i++)
        UA_Argument_clear(&inputArgs[i]);
    UA_free(inputArgs);
    for (size_t i = 0; i < outputSize; i++)
        UA_Argument_clear(&outputArgs[i]);
    UA_free(outputArgs);

    UA_MethodAttributes_clear(&attr);
    UA_QualifiedName_clear(&browseName);
    UA_NodeId_clear(&refTypeId);
    UA_NodeId_clear(&parentId);
    UA_NodeId_clear(&requestedId);

    if (status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);

    /* Store the callback so the C dispatcher can find it */
    store_method_callback(py_callback, &outId, srv->server);

    PyObject *result = UA2PY(&outId, &UA_TYPES[UA_TYPES_NODEID]);
    UA_NodeId_clear(&outId);
    return result;

fail_attr:
    UA_QualifiedName_clear(&browseName);
fail_browse:
    UA_NodeId_clear(&refTypeId);
fail_reftype:
    UA_NodeId_clear(&parentId);
fail_parent:
    UA_NodeId_clear(&requestedId);
    return NULL;
    WITH_OWNER_END();
}

/************************************************************
 * add_reference(source_id, ref_type_id, target_id, is_forward)
 ************************************************************/
PyObject *
pyServer_add_reference(PyObject *self, PyObject *args) {
    WITH_OWNER(((PyServer*)self)->server);
    PyObject *py_source, *py_reftype, *py_target;
    int is_forward = 1;

    if (!PyArg_ParseTuple(args, "OOO|p", &py_source, &py_reftype,
                          &py_target, &is_forward))
        return NULL;

    UA_NodeId sourceId, refTypeId;
    UA_ExpandedNodeId targetId;

    if (extract_nodeid(py_source, &sourceId) < 0) return NULL;
    if (extract_nodeid(py_reftype, &refTypeId) < 0) {
        UA_NodeId_clear(&sourceId);
        return NULL;
    }

    UA_ExpandedNodeId_init(&targetId);
    PyObject *conv = PY2UA(py_target, &targetId,
                           &UA_TYPES[UA_TYPES_EXPANDEDNODEID]);
    if (!conv) {
        UA_NodeId_clear(&refTypeId);
        UA_NodeId_clear(&sourceId);
        return NULL;
    }

    PyServer *srv = (PyServer *)self;
    UA_StatusCode status = UA_Server_addReference(
        srv->server, sourceId, refTypeId, targetId,
        (UA_Boolean)is_forward);

    UA_ExpandedNodeId_clear(&targetId);
    UA_NodeId_clear(&refTypeId);
    UA_NodeId_clear(&sourceId);

    if (status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);

    Py_RETURN_NONE;
    WITH_OWNER_END();
}

/************************************************************
 * delete_node(nodeid, delete_references=True)
 ************************************************************/
PyObject *
pyServer_delete_node(PyObject *self, PyObject *args) {
    WITH_OWNER(((PyServer*)self)->server);
    PyObject *py_nodeid;
    int delete_refs = 1;

    if (!PyArg_ParseTuple(args, "O|p", &py_nodeid, &delete_refs))
        return NULL;

    UA_NodeId nodeId;
    if (extract_nodeid(py_nodeid, &nodeId) < 0)
        return NULL;

    /* Remove any stored method callback for this node */
    PyServer *srv = (PyServer *)self;
    remove_method_callback(&nodeId, srv->server);
    UA_StatusCode status = UA_Server_deleteNode(
        srv->server, nodeId, (UA_Boolean)delete_refs);

    UA_NodeId_clear(&nodeId);

    if (status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);

    Py_RETURN_NONE;
    WITH_OWNER_END();
}

/************************************************************
 * read_value(nodeid) -> Future[variant value]
 ************************************************************/
PyObject *
pyServer_read_value(PyObject *self, PyObject *args) {
    WITH_OWNER(((PyServer*)self)->server);
    PyObject *py_nodeid;

    if (!PyArg_ParseTuple(args, "O", &py_nodeid))
        return NULL;

    UA_NodeId nodeId;
    if (extract_nodeid(py_nodeid, &nodeId) < 0)
        return NULL;

    PyServer *srv = (PyServer *)self;
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
    WITH_OWNER_END();
}

/************************************************************
 * write_value(nodeid, value) -> Future[None]
 ************************************************************/
PyObject *
pyServer_write_value(PyObject *self, PyObject *args) {
    WITH_OWNER(((PyServer*)self)->server);
    PyObject *py_nodeid, *py_value;

    if (!PyArg_ParseTuple(args, "OO", &py_nodeid, &py_value))
        return NULL;

    UA_NodeId nodeId;
    if (extract_nodeid(py_nodeid, &nodeId) < 0)
        return NULL;

    UA_WriteValue wv;
    if (build_write_value(&nodeId, UA_ATTRIBUTEID_VALUE, py_value, &wv) < 0) {
        UA_NodeId_clear(&nodeId);
        UA_WriteValue_clear(&wv);
        return NULL;
    }
    UA_NodeId_clear(&nodeId);

    PyServer *srv = (PyServer *)self;
    ServerAsyncCtx *ctx = serverAsync_create_ctx(srv->server, 0);
    if (!ctx) {
        UA_WriteValue_clear(&wv);
        return NULL;
    }

    PyObject *fut = ctx->future;
    UA_StatusCode sc = UA_Server_write_async(srv->server, &wv,
                                             serverAsyncWriteCallback, ctx, 0);
    UA_WriteValue_clear(&wv);
    if (sc != UA_STATUSCODE_GOOD) {
        Py_DECREF(fut);
        UA_free(ctx);
        return PyErr_StatusCode(sc);
    }
    return fut;
    WITH_OWNER_END();
}

/************************************************************
 * call(object_id, method_id, input_args) -> Future[(StatusCode, ...)]
 ************************************************************/
PyObject *
pyServer_call(PyObject *self, PyObject *args) {
    WITH_OWNER(((PyServer*)self)->server);
    PyObject *py_object_id, *py_method_id, *py_input_args;

    if (!PyArg_ParseTuple(args, "OOO", &py_object_id, &py_method_id,
                          &py_input_args))
        return NULL;

    UA_CallMethodRequest request;
    UA_CallMethodRequest_init(&request);

    if (extract_nodeid(py_object_id, &request.objectId) < 0)
        return NULL;
    if (extract_nodeid(py_method_id, &request.methodId) < 0) {
        UA_NodeId_clear(&request.objectId);
        return NULL;
    }

    /* Convert input arguments list/tuple -> UA_Variant array */
    if (py_input_args != Py_None && PySequence_Check(py_input_args)) {
        Py_ssize_t n = PySequence_Size(py_input_args);
        if (n < 0) {
            UA_CallMethodRequest_clear(&request);
            return NULL;
        }
        if (n > 0) {
            request.inputArguments =
                (UA_Variant *)UA_Array_new((size_t)n,
                                           &UA_TYPES[UA_TYPES_VARIANT]);
            if (!request.inputArguments) {
                UA_CallMethodRequest_clear(&request);
                return PyErr_NoMemory();
            }
            request.inputArgumentsSize = (size_t)n;
            for (Py_ssize_t i = 0; i < n; i++) {
                PyObject *item = PySequence_GetItem(py_input_args, i);
                PyObject *conv = PY2UA(item, &request.inputArguments[i],
                                       &UA_TYPES[UA_TYPES_VARIANT]);
                Py_DECREF(item);
                if (!conv) {
                    UA_CallMethodRequest_clear(&request);
                    return NULL;
                }
            }
        }
    }

    PyServer *srv = (PyServer *)self;
    ServerAsyncCtx *ctx = serverAsync_create_ctx(srv->server, 0);
    if (!ctx) {
        UA_CallMethodRequest_clear(&request);
        return NULL;
    }

    PyObject *fut = ctx->future;
    UA_StatusCode sc = UA_Server_call_async(srv->server, &request,
                                            serverAsyncCallCallback, ctx, 0);
    UA_CallMethodRequest_clear(&request);
    if (sc != UA_STATUSCODE_GOOD) {
        Py_DECREF(fut);
        UA_free(ctx);
        return PyErr_StatusCode(sc);
    }
    return fut;
    WITH_OWNER_END();
}

/* ------------------------------------------------------------------ */
/* register_historizing                                                 */
/* ------------------------------------------------------------------ */

PyObject *
pyServer_register_historizing(PyObject *self, PyObject *args, PyObject *kwds) {
    WITH_OWNER(((PyServer*)self)->server);
    static char *kwlist[] = {"nodeid", "max_values", "max_response", NULL};
    PyObject *py_nodeId = NULL;
    int max_values = 100;
    int max_response = 100;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "O|ii", kwlist,
                                     &py_nodeId, &max_values, &max_response))
        return NULL;

    PyServer *srv = (PyServer *)self;
    if (!srv->server) {
        PyErr_SetString(PyExc_RuntimeError, "Server not initialized");
        return NULL;
    }
    if (!srv->hasHistoryDB) {
        PyErr_SetString(PyExc_RuntimeError,
                        "No history database configured. "
                        "Call config.set_history_database() first.");
        return NULL;
    }

    UA_NodeId nodeId;
    if (extract_nodeid(py_nodeId, &nodeId) < 0)
        return NULL;

    UA_HistorizingNodeIdSettings setting;
    memset(&setting, 0, sizeof(setting));
    setting.historizingBackend =
        UA_HistoryDataBackend_Memory(1, (size_t)max_values);
    setting.maxHistoryDataResponseSize = (size_t)max_response;
    setting.historizingUpdateStrategy = UA_HISTORIZINGUPDATESTRATEGY_VALUESET;

    UA_StatusCode status =
        srv->gathering.registerNodeId(srv->server, srv->gathering.context,
                                      &nodeId, setting);
    UA_NodeId_clear(&nodeId);

    if (status != UA_STATUSCODE_GOOD) {
        setting.historizingBackend.deleteMembers(&setting.historizingBackend);
        return PyErr_StatusCode(status);
    }

    Py_RETURN_NONE;
    WITH_OWNER_END();
}

/************************************************************
 * browse_node(nodeid, result_mask) -> list[ReferenceDescription]
 *
 * Forward-hierarchical browse of a node.
 ************************************************************/
PyObject *
pyServer_browse_node(PyObject *self, PyObject *args) {
    WITH_OWNER(((PyServer*)self)->server);
    PyObject *py_nodeid;
    int result_mask;

    if (!PyArg_ParseTuple(args, "Oi", &py_nodeid, &result_mask))
        return NULL;

    UA_NodeId nodeId;
    if (extract_nodeid(py_nodeid, &nodeId) < 0)
        return NULL;

    UA_BrowseDescription bd;
    UA_BrowseDescription_init(&bd);
    bd.nodeId = nodeId;
    bd.browseDirection = UA_BROWSEDIRECTION_FORWARD;
    bd.referenceTypeId = UA_NODEID_NUMERIC(0, UA_NS0ID_HIERARCHICALREFERENCES);
    bd.includeSubtypes = true;
    bd.resultMask = (UA_UInt32)result_mask;

    PyServer *srv = (PyServer *)self;
    UA_BrowseResult br = UA_Server_browse(srv->server, 0, &bd);
    UA_NodeId_clear(&nodeId);

    if (br.statusCode != UA_STATUSCODE_GOOD) {
        UA_StatusCode sc = br.statusCode;
        UA_BrowseResult_clear(&br);
        return PyErr_StatusCode(sc);
    }

    PyObject *list = PyList_New((Py_ssize_t)br.referencesSize);
    if (!list) {
        UA_BrowseResult_clear(&br);
        return NULL;
    }
    for (size_t i = 0; i < br.referencesSize; i++) {
        PyObject *item = UA2PY(&br.references[i],
                               &UA_TYPES[UA_TYPES_REFERENCEDESCRIPTION]);
        if (!item) {
            Py_DECREF(list);
            UA_BrowseResult_clear(&br);
            return NULL;
        }
        PyList_SET_ITEM(list, (Py_ssize_t)i, item);
    }
    UA_BrowseResult_clear(&br);
    return list;
    WITH_OWNER_END();
}

/************************************************************
 * read_object_property(nodeid, property_name) -> value
 *
 * Read a property value from an object by its BrowseName.
 ************************************************************/
PyObject *
pyServer_read_object_property(PyObject *self, PyObject *args) {
    WITH_OWNER(((PyServer*)self)->server);
    PyObject *py_objectid, *py_property_name;
    if (!PyArg_ParseTuple(args, "OO", &py_objectid, &py_property_name))
        return NULL;

    UA_NodeId objectId;
    if (extract_nodeid(py_objectid, &objectId) < 0)
        return NULL;

    UA_QualifiedName propertyName;
    if (extract_qualifiedname(py_property_name, &propertyName) < 0) {
        UA_NodeId_clear(&objectId);
        return NULL;
    }

    UA_Variant value;
    UA_Variant_init(&value);

    PyServer *srv = (PyServer *)self;
    UA_StatusCode status = UA_Server_readObjectProperty(
        srv->server, objectId, propertyName, &value);

    UA_NodeId_clear(&objectId);
    UA_QualifiedName_clear(&propertyName);

    if (status != UA_STATUSCODE_GOOD) {
        UA_Variant_clear(&value);
        return PyErr_StatusCode(status);
    }

    PyObject *result = UA2PY(&value, &UA_TYPES[UA_TYPES_VARIANT]);
    UA_Variant_clear(&value);
    return result;
    WITH_OWNER_END();
}

/************************************************************
 * write_object_property(nodeid, property_name, value) -> None
 *
 * Write a property value on an object by its BrowseName.
 ************************************************************/
PyObject *
pyServer_write_object_property(PyObject *self, PyObject *args) {
    WITH_OWNER(((PyServer*)self)->server);
    PyObject *py_objectid, *py_property_name, *py_value;
    if (!PyArg_ParseTuple(args, "OOO", &py_objectid, &py_property_name,
                          &py_value))
        return NULL;

    UA_NodeId objectId;
    if (extract_nodeid(py_objectid, &objectId) < 0)
        return NULL;

    UA_QualifiedName propertyName;
    if (extract_qualifiedname(py_property_name, &propertyName) < 0) {
        UA_NodeId_clear(&objectId);
        return NULL;
    }

    UA_Variant value;
    UA_Variant_init(&value);
    if (!PY2UA(py_value, &value, &UA_TYPES[UA_TYPES_VARIANT])) {
        UA_NodeId_clear(&objectId);
        UA_QualifiedName_clear(&propertyName);
        UA_Variant_clear(&value);
        return NULL;
    }

    PyServer *srv = (PyServer *)self;
    UA_StatusCode status = UA_Server_writeObjectProperty(
        srv->server, objectId, propertyName, value);

    UA_NodeId_clear(&objectId);
    UA_QualifiedName_clear(&propertyName);
    UA_Variant_clear(&value);

    if (status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);
    Py_RETURN_NONE;
    WITH_OWNER_END();
}

/************************************************************
 * read_attribute(nodeid, attr_id) -> Future[value]
 *
 * Read any standard OPC UA attribute by its integer AttributeId.
 ************************************************************/
PyObject *
pyServer_read_attribute(PyObject *self, PyObject *args) {
    WITH_OWNER(((PyServer*)self)->server);
    PyObject *py_nodeid;
    int attr_id;

    if (!PyArg_ParseTuple(args, "Oi", &py_nodeid, &attr_id))
        return NULL;

    if (attr_id < 1 || attr_id > 27) {
        PyErr_SetString(PyExc_ValueError, "Unsupported AttributeId");
        return NULL;
    }

    UA_NodeId nodeId;
    if (extract_nodeid(py_nodeid, &nodeId) < 0)
        return NULL;

    PyServer *srv = (PyServer *)self;
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
    WITH_OWNER_END();
}

/************************************************************
 * write_data_value(nodeid, datavalue) -> Future[None]
 *
 * Write a DataValue to a node's Value attribute, allowing explicit
 * status code and timestamps to be set alongside the value.
 ************************************************************/
PyObject *
pyServer_write_data_value(PyObject *self, PyObject *args) {
    WITH_OWNER(((PyServer*)self)->server);
    PyObject *py_nodeid, *py_datavalue;

    if (!PyArg_ParseTuple(args, "OO", &py_nodeid, &py_datavalue))
        return NULL;

    UA_NodeId nodeId;
    if (extract_nodeid(py_nodeid, &nodeId) < 0)
        return NULL;

    UA_WriteValue wv;
    UA_WriteValue_init(&wv);
    if (UA_NodeId_copy(&nodeId, &wv.nodeId) != UA_STATUSCODE_GOOD) {
        UA_NodeId_clear(&nodeId);
        return PyErr_NoMemory();
    }
    UA_NodeId_clear(&nodeId);
    wv.attributeId = UA_ATTRIBUTEID_VALUE;

    PyObject *conv = PY2UA_datavalue(py_datavalue, &wv.value);
    if (!conv) {
        UA_WriteValue_clear(&wv);
        return NULL;
    }

    PyServer *srv = (PyServer *)self;
    ServerAsyncCtx *ctx = serverAsync_create_ctx(srv->server, 0);
    if (!ctx) {
        UA_WriteValue_clear(&wv);
        return NULL;
    }

    PyObject *fut = ctx->future;
    UA_StatusCode sc = UA_Server_write_async(srv->server, &wv,
                                             serverAsyncWriteCallback, ctx, 0);
    UA_WriteValue_clear(&wv);
    if (sc != UA_STATUSCODE_GOOD) {
        Py_DECREF(fut);
        UA_free(ctx);
        return PyErr_StatusCode(sc);
    }
    return fut;
    WITH_OWNER_END();
}

/************************************************************
 * write_attribute(nodeid, attr_id, value) -> Future[None]
 *
 * Write any standard OPC UA attribute by its integer AttributeId.
 ************************************************************/
PyObject *
pyServer_write_attribute(PyObject *self, PyObject *args) {
    WITH_OWNER(((PyServer*)self)->server);
    PyObject *py_nodeid, *py_value;
    int attr_id;

    if (!PyArg_ParseTuple(args, "OiO", &py_nodeid, &attr_id, &py_value))
        return NULL;

    UA_NodeId nodeId;
    if (extract_nodeid(py_nodeid, &nodeId) < 0)
        return NULL;

    UA_WriteValue wv;
    if (build_write_value(&nodeId, attr_id, py_value, &wv) < 0) {
        UA_NodeId_clear(&nodeId);
        UA_WriteValue_clear(&wv);
        return NULL;
    }
    UA_NodeId_clear(&nodeId);

    PyServer *srv = (PyServer *)self;
    ServerAsyncCtx *ctx = serverAsync_create_ctx(srv->server, 0);
    if (!ctx) {
        UA_WriteValue_clear(&wv);
        return NULL;
    }

    PyObject *fut = ctx->future;
    UA_StatusCode sc = UA_Server_write_async(srv->server, &wv,
                                             serverAsyncWriteCallback, ctx, 0);
    UA_WriteValue_clear(&wv);
    if (sc != UA_STATUSCODE_GOOD) {
        Py_DECREF(fut);
        UA_free(ctx);
        return PyErr_StatusCode(sc);
    }
    return fut;
    WITH_OWNER_END();
}

/************************************************************
 * translate_browse_paths(request) -> TranslateBrowsePathsToNodeIdsResponse
 *
 * Server-side translate browse paths to node ids.
 ************************************************************/
PyObject *
pyServer_translate_browse_paths(PyObject *self, PyObject *args) {
    WITH_OWNER(((PyServer*)self)->server);
    PyObject *py_request;

    if (!PyArg_ParseTuple(args, "O", &py_request))
        return NULL;

    UA_TranslateBrowsePathsToNodeIdsRequest req;
    UA_TranslateBrowsePathsToNodeIdsRequest_init(&req);
    PyObject *conv = PY2UA(py_request, &req,
                           &UA_TYPES[UA_TYPES_TRANSLATEBROWSEPATHSTONODEIDSREQUEST]);
    if (!conv)
        return NULL;

    PyServer *srv = (PyServer *)self;
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
        &UA_TYPES[UA_TYPES_TRANSLATEBROWSEPATHSTONODEIDSRESPONSE]);

    for (size_t i = 0; i < resp.resultsSize; i++)
        UA_BrowsePathResult_clear(&resp.results[i]);
    UA_free(resp.results);
    resp.results = NULL;
    resp.resultsSize = 0;
    UA_TranslateBrowsePathsToNodeIdsRequest_clear(&req);

    return py_resp;
    WITH_OWNER_END();
}

/************************************************************
 * read_node_info(nodeid) -> (node_class_int, browse_name)
 *
 * Returns (NodeClass as int, QualifiedName) for a node.
 ************************************************************/
PyObject *
pyServer_read_node_info(PyObject *self, PyObject *args) {
    WITH_OWNER(((PyServer*)self)->server);
    PyObject *py_nodeid;

    if (!PyArg_ParseTuple(args, "O", &py_nodeid))
        return NULL;

    UA_NodeId nodeId;
    if (extract_nodeid(py_nodeid, &nodeId) < 0)
        return NULL;

    PyServer *srv = (PyServer *)self;

    UA_NodeClass nc;
    UA_StatusCode sc = UA_Server_readNodeClass(srv->server, nodeId, &nc);
    if (sc != UA_STATUSCODE_GOOD) {
        UA_NodeId_clear(&nodeId);
        return PyErr_StatusCode(sc);
    }

    UA_QualifiedName bn;
    sc = UA_Server_readBrowseName(srv->server, nodeId, &bn);
    UA_NodeId_clear(&nodeId);
    if (sc != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(sc);

    PyObject *py_bn = UA2PY(&bn, &UA_TYPES[UA_TYPES_QUALIFIEDNAME]);
    UA_QualifiedName_clear(&bn);
    if (!py_bn)
        return NULL;

    PyObject *result = PyTuple_Pack(2, PyLong_FromLong((long)nc), py_bn);
    Py_DECREF(py_bn);
    return result;
    WITH_OWNER_END();
}

/************************************************************
 * Module type initialisation
 ************************************************************/
int
Server_initTypes(void) {
    if (PyType_Ready(&PyMethodDoneCbType) < 0)
        return -1;
    return 0;
}
