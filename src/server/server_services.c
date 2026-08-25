/* Copyright 2026 (c) o6 Automation GmbH */
#include "server.h"
#include "../module.h"
#include "../types_internal.h"
#include "python_nodestore.h"
#include "server_services_util.h"
#include "server/ua_server_internal.h"


/************************************************************
 * View Service Set
 ************************************************************/

 /* Browse Functions from View Service Set Methods  */

PyObject *
pyServer_browse(PyObject *self, PyObject *args) {
    PyObject *py_desc = NULL;
    PyObject *py_node = NULL;
    unsigned int max_refs = 0;

    Py_ssize_t argc = PyTuple_GET_SIZE(args);
    if(argc == 2) {
        if(!PyArg_ParseTuple(args, "IO", &max_refs, &py_desc))
            return NULL;
    } else if(argc == 3) {
        if(!PyArg_ParseTuple(args, "IOO", &max_refs, &py_desc, &py_node))
            return NULL;
    } else {
        PyErr_SetString(PyExc_TypeError,
                        "browse() expects (maxReferences, BrowseDescription) "
                        "or the internal direct-node form");
        return NULL;
    }

    UA_BrowseDescription bd;
    UA_BrowseDescription_init(&bd);
    PyServer *srv = (PyServer *)self;
    const UA_NamespaceMapping *nsMapping = &srv->nsMapPy2UA;
    const UA_DataTypeArray *customDataTypes =
        UA_Server_getConfig(srv->server)->customDataTypes;
    if (!PY2UA(py_desc, &bd, &UA_TYPES[UA_TYPES_BROWSEDESCRIPTION],
               nsMapping, customDataTypes)) {
        UA_BrowseDescription_clear(&bd);
        return NULL;
    }

    UA_BrowseResult br;
    UA_BrowseResult_init(&br);
    if(py_node) {
        PyServer *nodeServer = NULL;
        UA_Node *node = pyNodeStore_attachedNode(py_node, &nodeServer);
        if(!node) {
            UA_BrowseDescription_clear(&bd);
            return NULL;
        }
        if(nodeServer != srv) {
            UA_BrowseDescription_clear(&bd);
            PyErr_SetString(PyExc_ValueError,
                            "browse node belongs to a different server");
            return NULL;
        }
        UA_UInt32 maxReferences = (UA_UInt32)max_refs;
        lockServer(srv->server);
        Operation_BrowseWithNode(srv->server, &srv->server->adminSession,
                                 node, &maxReferences, &bd, &br);
        unlockServer(srv->server);
    } else {
        br = UA_Server_browse(srv->server, (UA_UInt32)max_refs, &bd);
    }
    UA_BrowseDescription_clear(&bd);

    if (br.statusCode != UA_STATUSCODE_GOOD) {
        UA_StatusCode sc = br.statusCode;
        UA_BrowseResult_clear(&br);
        return PyErr_StatusCode(sc);
    }
    PyObject *result = UA2PY(&br, &UA_TYPES[UA_TYPES_BROWSERESULT], nsMapping);
    UA_BrowseResult_clear(&br);
    return result;
}


PyObject *
pyServer_browse_next(PyObject *self, PyObject *args) {
    PyObject *py_release;
    PyObject *py_cp;
    if (!PyArg_ParseTuple(args, "OO", &py_release, &py_cp))
        return NULL;

    int release = PyObject_IsTrue(py_release);
    if (release < 0)
        return NULL;

    PyServer *srv = (PyServer *)self;
    const UA_NamespaceMapping *nsMapping = &srv->nsMapPy2UA;
    const UA_DataTypeArray *customDataTypes =
        UA_Server_getConfig(srv->server)->customDataTypes;

    int is_list = PyList_Check(py_cp) || PyTuple_Check(py_cp);
    size_t n = 0;
    UA_ByteString *cps = NULL;

    if (is_list) {
        Py_ssize_t len = PySequence_Fast_GET_SIZE(py_cp);
        n = (size_t)len;
        if (n > 0) {
            cps = (UA_ByteString*)UA_malloc(n * sizeof(UA_ByteString));
            if (!cps)
                return PyErr_NoMemory();
            memset(cps, 0, n * sizeof(UA_ByteString));
            for (size_t i = 0; i < n; i++) {
                PyObject *item = PySequence_Fast_GET_ITEM(py_cp, (Py_ssize_t)i);
                if (!PY2UA(item, &cps[i], &UA_TYPES[UA_TYPES_BYTESTRING],
                           nsMapping, customDataTypes)) {
                    for (size_t j = 0; j < i; j++)
                        UA_ByteString_clear(&cps[j]);
                    UA_free(cps);
                    return NULL;
                }
            }
        }
    } else {
        n = 1;
        cps = (UA_ByteString*)UA_malloc(sizeof(UA_ByteString));
        if (!cps)
            return PyErr_NoMemory();
        UA_ByteString_init(cps);
        if (!PY2UA(py_cp, cps, &UA_TYPES[UA_TYPES_BYTESTRING],
                   nsMapping, customDataTypes)) {
            UA_ByteString_clear(cps);
            UA_free(cps);
            return NULL;
        }
    }

    PyObject *out = NULL;
    UA_BrowseResult *results = NULL;

    if (n == 0) {
        UA_free(cps);
        return PyList_New(0);
    }

    results = (UA_BrowseResult*)UA_malloc(n * sizeof(UA_BrowseResult));
    if (!results) {
        for (size_t i = 0; i < n; i++)
            UA_ByteString_clear(&cps[i]);
        UA_free(cps);
        return PyErr_NoMemory();
    }

    for (size_t i = 0; i < n; i++) {
        results[i] = UA_Server_browseNext(srv->server, (UA_Boolean)release,
                                          &cps[i]);
    }

    for (size_t i = 0; i < n; i++)
        UA_ByteString_clear(&cps[i]);
    UA_free(cps);

    out = PyList_New((Py_ssize_t)n);
    if (!out) {
        for (size_t i = 0; i < n; i++)
            UA_BrowseResult_clear(&results[i]);
        UA_free(results);
        return NULL;
    }

    for (size_t i = 0; i < n; i++) {
        PyObject *py_r =
            UA2PY(&results[i], &UA_TYPES[UA_TYPES_BROWSERESULT], nsMapping);
        if (!py_r) {
            for (size_t j = i + 1; j < n; j++)
                UA_BrowseResult_clear(&results[j]);
            UA_free(results);
            Py_DECREF(out);
            return NULL;
        }
        UA_BrowseResult_clear(&results[i]);
        PyList_SET_ITEM(out, (Py_ssize_t)i, py_r);
    }
    UA_free(results);
    return out;
}

PyObject *
pyServer_browse_recursive(PyObject *self, PyObject *args) {
    PyObject *py_desc;
    if (!PyArg_ParseTuple(args, "O", &py_desc))
        return NULL;

    UA_BrowseDescription bd;
    UA_BrowseDescription_init(&bd);
    PyServer *srv = (PyServer *)self;
    const UA_NamespaceMapping *nsMapping = &srv->nsMapPy2UA;
    const UA_DataTypeArray *customDataTypes =
        UA_Server_getConfig(srv->server)->customDataTypes;
    if (!PY2UA(py_desc, &bd, &UA_TYPES[UA_TYPES_BROWSEDESCRIPTION],
               nsMapping, customDataTypes)) {
        UA_BrowseDescription_clear(&bd);
        return NULL;
    }

    size_t resultsSize = 0;
    UA_ExpandedNodeId *results = NULL;
    UA_StatusCode status = UA_Server_browseRecursive(srv->server, &bd,
                                                     &resultsSize, &results);
    UA_BrowseDescription_clear(&bd);

    if (status != UA_STATUSCODE_GOOD) {
        if (results)
            UA_Array_delete(results, resultsSize,
                            &UA_TYPES[UA_TYPES_EXPANDEDNODEID]);
        return PyErr_StatusCode(status);
    }

    PyObject *out = PyList_New((Py_ssize_t)resultsSize);
    if (!out) {
        UA_Array_delete(results, resultsSize,
                        &UA_TYPES[UA_TYPES_EXPANDEDNODEID]);
        return NULL;
    }

    for (size_t i = 0; i < resultsSize; i++) {
        PyObject *py_r = UA2PY(&results[i],
                               &UA_TYPES[UA_TYPES_EXPANDEDNODEID],
                               nsMapping);
        if (!py_r) {
            for (size_t j = i + 1; j < resultsSize; j++)
                UA_ExpandedNodeId_clear(&results[j]);
            UA_Array_delete(results, resultsSize,
                            &UA_TYPES[UA_TYPES_EXPANDEDNODEID]);
            Py_DECREF(out);
            return NULL;
        }
        UA_ExpandedNodeId_clear(&results[i]);
        PyList_SET_ITEM(out, (Py_ssize_t)i, py_r);
    }
    UA_Array_delete(results, resultsSize,
                    &UA_TYPES[UA_TYPES_EXPANDEDNODEID]);
    return out;
}

PyObject *
pyServer_translate_browse_paths_to_nodeids(PyObject *self, PyObject *args) {
    PyObject *py_browse_path;
    PyObject *py_node = NULL;
    if (!PyArg_ParseTuple(args, "O|O", &py_browse_path, &py_node))
        return NULL;

    UA_BrowsePath bp;
    UA_BrowsePath_init(&bp);
    PyServer *srv = (PyServer *)self;
    const UA_NamespaceMapping *nsMapping = &srv->nsMapPy2UA;
    const UA_DataTypeArray *customDataTypes =
        UA_Server_getConfig(srv->server)->customDataTypes;
    if (!PY2UA(py_browse_path, &bp, &UA_TYPES[UA_TYPES_BROWSEPATH],
               nsMapping, customDataTypes)) {
        UA_BrowsePath_clear(&bp);
        return NULL;
    }

    UA_BrowsePathResult result;
    if(py_node) {
        PyServer *nodeServer = NULL;
        UA_Node *node = pyNodeStore_attachedNode(py_node, &nodeServer);
        if(!node) {
            UA_BrowsePath_clear(&bp);
            return NULL;
        }
        if(nodeServer != srv) {
            UA_BrowsePath_clear(&bp);
            PyErr_SetString(PyExc_ValueError,
                            "browse-path node belongs to a different server");
            return NULL;
        }
        lockServer(srv->server);
        result = translateBrowsePathToNodeIdsWithNode(srv->server, node, &bp);
        unlockServer(srv->server);
    } else {
        result = UA_Server_translateBrowsePathToNodeIds(srv->server, &bp);
    }
    UA_BrowsePath_clear(&bp);

    PyObject *py_result =
        UA2PY(&result, &UA_TYPES[UA_TYPES_BROWSEPATHRESULT], nsMapping);
    UA_BrowsePathResult_clear(&result);
    return py_result;
}

PyObject *
pyServer_browse_simplified_browse_paths(PyObject *self, PyObject *args) {
    PyObject *py_origin;
    PyObject *py_qn_list;
    if (!PyArg_ParseTuple(args, "OO", &py_origin, &py_qn_list))
        return NULL;

    PyServer *srv = (PyServer *)self;
    const UA_NamespaceMapping *nsMapping = &srv->nsMapPy2UA;
    const UA_DataTypeArray *customDataTypes =
        UA_Server_getConfig(srv->server)->customDataTypes;

    UA_NodeId origin;
    if (extract_nodeid(py_origin, &origin, nsMapping, customDataTypes) < 0)
        return NULL;

    UA_QualifiedName *qns = NULL;
    size_t n = 0;
    int is_seq = PyList_Check(py_qn_list) || PyTuple_Check(py_qn_list);
    if (is_seq) {
        Py_ssize_t len = PySequence_Fast_GET_SIZE(py_qn_list);
        n = (size_t)len;
        if (n > 0) {
            qns = (UA_QualifiedName*)UA_malloc(n * sizeof(UA_QualifiedName));
            if (!qns) {
                UA_NodeId_clear(&origin);
                return PyErr_NoMemory();
            }
            for (size_t i = 0; i < n; i++) {
                PyObject *item = PySequence_Fast_GET_ITEM(py_qn_list,
                                                          (Py_ssize_t)i);
                if (extract_qualifiedname(item, &qns[i],
                                          nsMapping, customDataTypes) < 0) {
                    for (size_t j = 0; j < i; j++)
                        UA_QualifiedName_clear(&qns[j]);
                    UA_free(qns);
                    UA_NodeId_clear(&origin);
                    return NULL;
                }
            }
        }
    } else {
        n = 1;
        qns = (UA_QualifiedName*)UA_malloc(sizeof(UA_QualifiedName));
        if (!qns) {
            UA_NodeId_clear(&origin);
            return PyErr_NoMemory();
        }
        if (extract_qualifiedname(py_qn_list, &qns[0],
                                  nsMapping, customDataTypes) < 0) {
            UA_free(qns);
            UA_NodeId_clear(&origin);
            return NULL;
        }
    }

    UA_BrowsePathResult bpr = UA_Server_browseSimplifiedBrowsePath(
        srv->server, origin, n, qns);

    for (size_t i = 0; i < n; i++)
        UA_QualifiedName_clear(&qns[i]);
    UA_free(qns);
    UA_NodeId_clear(&origin);

    PyObject *py_result =
        UA2PY(&bpr, &UA_TYPES[UA_TYPES_BROWSEPATHRESULT], nsMapping);
    UA_BrowsePathResult_clear(&bpr);
    return py_result;
}

typedef struct {
    PyObject *callback; /* strong reference */
    const UA_NamespaceMapping *nsMapping;
} PyNodeIterCtx;

UA_StatusCode
pyNodeIteratorCallback(UA_NodeId childId, UA_Boolean isInverse,
                       UA_NodeId referenceTypeId, void *handle) {
    PyNodeIterCtx *ctx = (PyNodeIterCtx*)handle;
    if (!ctx || !ctx->callback) {
        PyErr_SetString(PyExc_RuntimeError,
                        "for_each_child_node: missing callback context");
        return UA_STATUSCODE_BADINTERNALERROR;
    }

    PyObject *py_child = UA2PY(
        &childId, &UA_TYPES[UA_TYPES_NODEID], ctx->nsMapping);
    if (!py_child) {
        PyErr_Clear();
        return UA_STATUSCODE_GOOD;
    }
    PyObject *py_reftype =
        UA2PY(&referenceTypeId, &UA_TYPES[UA_TYPES_NODEID], ctx->nsMapping);
    if (!py_reftype) {
        PyErr_Clear();
        Py_DECREF(py_child);
        return UA_STATUSCODE_GOOD;
    }
    PyObject *py_inv = PyBool_FromLong(isInverse ? 1 : 0);
    if (!py_inv) {
        PyErr_Clear();
        Py_DECREF(py_child);
        Py_DECREF(py_reftype);
        return UA_STATUSCODE_GOOD;
    }

    PyObject *result = PyObject_CallFunction(
        ctx->callback, "OOO", py_child, py_inv, py_reftype);
    Py_DECREF(py_child);
    Py_DECREF(py_reftype);
    Py_DECREF(py_inv);

    if (!result) {
        return UA_STATUSCODE_BADINTERNALERROR;
    }
    Py_DECREF(result);
    return UA_STATUSCODE_GOOD;
}

PyObject *
pyServer_for_each_child_node(PyObject *self, PyObject *args) {
    PyObject *py_nodeid, *py_callback;
    if (!PyArg_ParseTuple(args, "OO", &py_nodeid, &py_callback))
        return NULL;

    if (!PyCallable_Check(py_callback)) {
        PyErr_SetString(PyExc_TypeError, "callback must be callable");
        return NULL;
    }

    PyServer *srv = (PyServer *)self;
    const UA_NamespaceMapping *nsMapping = &srv->nsMapPy2UA;
    const UA_DataTypeArray *customDataTypes =
        UA_Server_getConfig(srv->server)->customDataTypes;

    UA_NodeId nodeId;
    if (extract_nodeid(py_nodeid, &nodeId, nsMapping, customDataTypes) < 0)
        return NULL;

    PyNodeIterCtx ctx;
    Py_INCREF(py_callback);
    ctx.callback = py_callback;
    ctx.nsMapping = nsMapping;

    UA_StatusCode status = UA_Server_forEachChildNodeCall(
        srv->server, nodeId, pyNodeIteratorCallback, &ctx);
    UA_NodeId_clear(&nodeId);
    Py_DECREF(py_callback);

    if (PyErr_Occurred())
        return NULL;

    if (status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);

    Py_RETURN_NONE;
}
