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
#include "server.h"
#include "../module.h"

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

/************************************************************
 * add_variable_node(requested_id, parent_id, ref_type_id,
 *                   browse_name, type_definition, attributes)
 ************************************************************/
PyObject *
pyServer_add_variable_node(PyObject *self, PyObject *args) {
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
}

/************************************************************
 * add_object_node(requested_id, parent_id, ref_type_id,
 *                 browse_name, type_definition, attributes)
 ************************************************************/
PyObject *
pyServer_add_object_node(PyObject *self, PyObject *args) {
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
}

/************************************************************
 * add_object_type_node(requested_id, parent_id, ref_type_id,
 *                      browse_name, attributes)
 ************************************************************/
PyObject *
pyServer_add_object_type_node(PyObject *self, PyObject *args) {
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
}

/************************************************************
 * add_data_type_node(requested_id, parent_id, ref_type_id,
 *                    browse_name, attributes)
 ************************************************************/
PyObject *
pyServer_add_data_type_node(PyObject *self, PyObject *args) {
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
}

/************************************************************
 * add_variable_type_node(requested_id, parent_id, ref_type_id,
 *                        browse_name, type_definition, attributes)
 ************************************************************/
PyObject *
pyServer_add_variable_type_node(PyObject *self, PyObject *args) {
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
}

/************************************************************
 * Method Node — Callback infrastructure
 ************************************************************/

/* Storage for Python method callbacks */
typedef struct {
    PyObject *callback;
    UA_NodeId methodId;
} PythonMethodCallback;

static PythonMethodCallback *method_callbacks = NULL;
static size_t method_callbacks_size = 0;
static size_t method_callbacks_capacity = 0;

static void
store_method_callback(PyObject *callback, const UA_NodeId *methodId) {
    if (method_callbacks_size >= method_callbacks_capacity) {
        method_callbacks_capacity =
            method_callbacks_capacity == 0 ? 4 : method_callbacks_capacity * 2;
        method_callbacks = realloc(method_callbacks,
            method_callbacks_capacity * sizeof(PythonMethodCallback));
    }

    method_callbacks[method_callbacks_size].callback = callback;
    Py_INCREF(callback);
    UA_NodeId_copy(methodId, &method_callbacks[method_callbacks_size].methodId);
    method_callbacks_size++;
}

static void
remove_method_callback(const UA_NodeId *methodId) {
    for (size_t i = 0; i < method_callbacks_size; i++) {
        if (UA_NodeId_equal(methodId, &method_callbacks[i].methodId)) {
            Py_DECREF(method_callbacks[i].callback);
            UA_NodeId_clear(&method_callbacks[i].methodId);
            if (i < method_callbacks_size - 1)
                method_callbacks[i] = method_callbacks[method_callbacks_size - 1];
            method_callbacks_size--;
            break;
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
    /* Find the Python callback */
    PyObject *callback = NULL;
    for (size_t i = 0; i < method_callbacks_size; i++) {
        if (UA_NodeId_equal(methodId, &method_callbacks[i].methodId)) {
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

    /* Convert outputs: expect a list/tuple or a single value */
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
}

/************************************************************
 * add_method_node(requested_id, parent_id, ref_type_id,
 *                 browse_name, attributes, callback,
 *                 input_arguments, output_arguments)
 ************************************************************/
PyObject *
pyServer_add_method_node(PyObject *self, PyObject *args) {
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
    store_method_callback(py_callback, &outId);

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
}

/************************************************************
 * add_reference(source_id, ref_type_id, target_id, is_forward)
 ************************************************************/
PyObject *
pyServer_add_reference(PyObject *self, PyObject *args) {
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
}

/************************************************************
 * delete_node(nodeid, delete_references=True)
 ************************************************************/
PyObject *
pyServer_delete_node(PyObject *self, PyObject *args) {
    PyObject *py_nodeid;
    int delete_refs = 1;

    if (!PyArg_ParseTuple(args, "O|p", &py_nodeid, &delete_refs))
        return NULL;

    UA_NodeId nodeId;
    if (extract_nodeid(py_nodeid, &nodeId) < 0)
        return NULL;

    /* Remove any stored method callback for this node */
    remove_method_callback(&nodeId);

    PyServer *srv = (PyServer *)self;
    UA_StatusCode status = UA_Server_deleteNode(
        srv->server, nodeId, (UA_Boolean)delete_refs);

    UA_NodeId_clear(&nodeId);

    if (status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);

    Py_RETURN_NONE;
}

/************************************************************
 * read_value(nodeid) -> variant value
 ************************************************************/
PyObject *
pyServer_read_value(PyObject *self, PyObject *args) {
    PyObject *py_nodeid;

    if (!PyArg_ParseTuple(args, "O", &py_nodeid))
        return NULL;

    UA_NodeId nodeId;
    if (extract_nodeid(py_nodeid, &nodeId) < 0)
        return NULL;

    UA_Variant value;
    UA_Variant_init(&value);

    PyServer *srv = (PyServer *)self;
    UA_StatusCode status = UA_Server_readValue(srv->server, nodeId, &value);

    UA_NodeId_clear(&nodeId);

    if (status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);

    PyObject *result = UA2PY(&value, &UA_TYPES[UA_TYPES_VARIANT]);
    UA_Variant_clear(&value);
    return result;
}

/************************************************************
 * write_value(nodeid, value)
 ************************************************************/
PyObject *
pyServer_write_value(PyObject *self, PyObject *args) {
    PyObject *py_nodeid, *py_value;

    if (!PyArg_ParseTuple(args, "OO", &py_nodeid, &py_value))
        return NULL;

    UA_NodeId nodeId;
    if (extract_nodeid(py_nodeid, &nodeId) < 0)
        return NULL;

    UA_Variant value;
    UA_Variant_init(&value);
    PyObject *conv = PY2UA(py_value, &value, &UA_TYPES[UA_TYPES_VARIANT]);
    if (!conv) {
        UA_NodeId_clear(&nodeId);
        return NULL;
    }

    PyServer *srv = (PyServer *)self;
    UA_StatusCode status = UA_Server_writeValue(srv->server, nodeId, value);

    UA_Variant_clear(&value);
    UA_NodeId_clear(&nodeId);

    if (status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);

    Py_RETURN_NONE;
}

/* ------------------------------------------------------------------ */
/* register_historizing                                                 */
/* ------------------------------------------------------------------ */

PyObject *
pyServer_register_historizing(PyObject *self, PyObject *args, PyObject *kwds) {
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
}
