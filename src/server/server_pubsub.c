/* Copyright 2026 (c) o6 Automation GmbH */
#include "server.h"
#include "python_nodestore.h"
#include "server_services_util.h"
#include "../types_internal.h"
#include <open62541/server_pubsub.h>

#define PUBSUB_STATE_MACHINE_KEY "_o6_pubsub_state_machine"

typedef struct PyPubSubDispatchFrame {
    struct PyPubSubDispatchFrame *parent;
    void *nodeContext;
} PyPubSubDispatchFrame;

static O6_THREAD_LOCAL PyPubSubDispatchFrame *pubSubDispatchHead;
static PyObject *pubSubStateType;
static PyObject *statusCodeType;

static int
ensure_pubsub_types(void) {
    if(pubSubStateType)
        return 0;
    PyObject *datatypes = PyImport_ImportModule("o6.ns.ns0.datatypes");
    PyObject *o6 = PyImport_ImportModule("o6");
    if(!datatypes || !o6)
        goto error;
    pubSubStateType = PyObject_GetAttrString(datatypes, "PubSubState");
    statusCodeType = PyObject_GetAttrString(o6, "StatusCode");
    Py_DECREF(datatypes);
    Py_DECREF(o6);
    datatypes = NULL;
    o6 = NULL;
    if(!pubSubStateType || !statusCodeType)
        goto error;
    return 0;

error:
    Py_XDECREF(datatypes);
    Py_XDECREF(o6);
    Py_CLEAR(pubSubStateType);
    Py_CLEAR(statusCodeType);
    return -1;
}

static PyObject *
node_state_machine(void *nodeContext) {
    return pyNodeStore_getMetadata(nodeContext, PUBSUB_STATE_MACHINE_KEY);
}

static int
set_node_state_machine(PyObject *node, PyObject *callback) {
    return pyNodeStore_setMetadata(
        node, PUBSUB_STATE_MACHINE_KEY,
        callback == Py_None ? NULL : callback);
}

static UA_StatusCode
python_pubsub_state_machine(UA_Server *server, const UA_NodeId componentId,
                            void *componentContext, UA_PubSubState *state,
                            UA_PubSubState targetState) {
    (void)componentContext;
    assertGIL();
    if(!state)
        return UA_STATUSCODE_BADINVALIDARGUMENT;

    void *nodeContext = NULL;
    UA_StatusCode status =
        UA_Server_getNodeContext(server, componentId, &nodeContext);
    if(status != UA_STATUSCODE_GOOD || !nodeContext) {
        *state = UA_PUBSUBSTATE_ERROR;
        return status == UA_STATUSCODE_GOOD ?
            UA_STATUSCODE_BADINTERNALERROR : status;
    }

    for(PyPubSubDispatchFrame *current = pubSubDispatchHead;
        current; current = current->parent) {
        if(current->nodeContext == nodeContext) {
            *state = UA_PUBSUBSTATE_ERROR;
            return UA_STATUSCODE_BADINTERNALERROR;
        }
    }

    PyObject *callback = node_state_machine(nodeContext);
    if(!callback) {
        if(PyErr_Occurred())
            PyErr_WriteUnraisable((PyObject *)nodeContext);
        *state = UA_PUBSUBSTATE_ERROR;
        return UA_STATUSCODE_BADINTERNALERROR;
    }
    if(ensure_pubsub_types() < 0) {
        PyErr_WriteUnraisable(callback);
        Py_DECREF(callback);
        *state = UA_PUBSUBSTATE_ERROR;
        return UA_STATUSCODE_BADINTERNALERROR;
    }

    PyPubSubDispatchFrame frame = {pubSubDispatchHead, nodeContext};
    pubSubDispatchHead = &frame;
    PyObject *currentState = PyObject_CallFunction(
        pubSubStateType, "i", (int)*state);
    PyObject *target = PyObject_CallFunction(
        pubSubStateType, "i", (int)targetState);
    PyObject *result = NULL;
    if(currentState && target)
        result = PyObject_CallFunctionObjArgs(
            callback, currentState, target, NULL);
    Py_XDECREF(currentState);
    Py_XDECREF(target);

    status = UA_STATUSCODE_BADINTERNALERROR;
    if(result && PyTuple_Check(result) && PyTuple_GET_SIZE(result) == 2) {
        PyObject *statusObject = PyTuple_GET_ITEM(result, 0);
        PyObject *stateObject = PyTuple_GET_ITEM(result, 1);
        int isStatus = PyObject_IsInstance(statusObject, statusCodeType);
        int isState = PyObject_IsInstance(stateObject, pubSubStateType);
        if(isStatus > 0 && isState > 0) {
            unsigned long statusValue = PyLong_AsUnsignedLong(statusObject);
            long stateValue = PyLong_AsLong(stateObject);
            if(!PyErr_Occurred() && stateValue >= UA_PUBSUBSTATE_DISABLED &&
               stateValue <= UA_PUBSUBSTATE_PREOPERATIONAL) {
                status = (UA_StatusCode)statusValue;
                if(UA_StatusCode_isGood(status))
                    *state = (UA_PubSubState)stateValue;
                else
                    *state = UA_PUBSUBSTATE_ERROR;
            }
        } else if(!PyErr_Occurred()) {
            PyErr_SetString(
                PyExc_TypeError,
                "PubSub state machine must return (StatusCode, PubSubState)");
        }
    } else if(result && !PyErr_Occurred()) {
        PyErr_SetString(
            PyExc_TypeError,
            "PubSub state machine must return (StatusCode, PubSubState)");
    }

    if(PyErr_Occurred())
        PyErr_WriteUnraisable(callback);
    Py_XDECREF(result);
    Py_DECREF(callback);
    pubSubDispatchHead = frame.parent;
    if(UA_StatusCode_isBad(status))
        *state = UA_PUBSUBSTATE_ERROR;
    return status;
}

static UA_StatusCode
update_component_state_machine(UA_Server *server, const UA_NodeId componentId,
                               UA_PubSubComponentType componentType,
                               UA_Boolean enabled) {
    UA_StatusCode status;
    switch(componentType) {
    case UA_PUBSUBCOMPONENT_CONNECTION: {
        UA_PubSubConnectionConfig config;
        memset(&config, 0, sizeof(config));
        status = UA_Server_getPubSubConnectionConfig(server, componentId, &config);
        if(status == UA_STATUSCODE_GOOD) {
            config.customStateMachine = enabled ? python_pubsub_state_machine : NULL;
            status = UA_Server_updatePubSubConnectionConfig(
                server, componentId, &config);
        }
        UA_PubSubConnectionConfig_clear(&config);
        return status == UA_STATUSCODE_BADINTERNALERROR ?
            UA_STATUSCODE_BADCONFIGURATIONERROR : status;
    }
    case UA_PUBSUBCOMPONENT_WRITERGROUP: {
        UA_WriterGroupConfig config;
        memset(&config, 0, sizeof(config));
        status = UA_Server_getWriterGroupConfig(server, componentId, &config);
        if(status == UA_STATUSCODE_GOOD) {
            config.customStateMachine = enabled ? python_pubsub_state_machine : NULL;
            status = UA_Server_updateWriterGroupConfig(server, componentId, &config);
        }
        UA_WriterGroupConfig_clear(&config);
        return status == UA_STATUSCODE_BADINTERNALERROR ?
            UA_STATUSCODE_BADCONFIGURATIONERROR : status;
    }
    case UA_PUBSUBCOMPONENT_DATASETWRITER: {
        UA_DataSetWriterConfig config;
        memset(&config, 0, sizeof(config));
        status = UA_Server_getDataSetWriterConfig(server, componentId, &config);
        if(status == UA_STATUSCODE_GOOD) {
            config.customStateMachine = enabled ? python_pubsub_state_machine : NULL;
            status = UA_Server_updateDataSetWriterConfig(server, componentId, &config);
        }
        UA_DataSetWriterConfig_clear(&config);
        return status == UA_STATUSCODE_BADINTERNALERROR ?
            UA_STATUSCODE_BADCONFIGURATIONERROR : status;
    }
    case UA_PUBSUBCOMPONENT_READERGROUP: {
        UA_ReaderGroupConfig config;
        memset(&config, 0, sizeof(config));
        status = UA_Server_getReaderGroupConfig(server, componentId, &config);
        if(status == UA_STATUSCODE_GOOD) {
            config.customStateMachine = enabled ? python_pubsub_state_machine : NULL;
            status = UA_Server_updateReaderGroupConfig(server, componentId, &config);
        }
        UA_ReaderGroupConfig_clear(&config);
        return status == UA_STATUSCODE_BADINTERNALERROR ?
            UA_STATUSCODE_BADCONFIGURATIONERROR : status;
    }
    case UA_PUBSUBCOMPONENT_DATASETREADER: {
        UA_DataSetReaderConfig config;
        memset(&config, 0, sizeof(config));
        status = UA_Server_getDataSetReaderConfig(server, componentId, &config);
        if(status == UA_STATUSCODE_GOOD) {
            config.customStateMachine = enabled ? python_pubsub_state_machine : NULL;
            status = UA_Server_updateDataSetReaderConfig(server, componentId, &config);
        }
        UA_DataSetReaderConfig_clear(&config);
        return status == UA_STATUSCODE_BADINTERNALERROR ?
            UA_STATUSCODE_BADCONFIGURATIONERROR : status;
    }
    default:
        return UA_STATUSCODE_BADNOTSUPPORTED;
    }
}

static UA_Boolean
is_active_pubsub_node_type(UA_Server *server, const UA_NodeId nodeId) {
    UA_NodeId typeId;
    UA_NodeId_init(&typeId);
    UA_StatusCode status = UA_Server_getNodeType(server, nodeId, &typeId);
    if(status != UA_STATUSCODE_GOOD)
        return false;
    UA_Boolean result = false;
    if(typeId.namespaceIndex == 0 &&
       typeId.identifierType == UA_NODEIDTYPE_NUMERIC) {
        UA_UInt32 numeric = typeId.identifier.numeric;
        result = numeric == UA_NS0ID_PUBSUBCONNECTIONTYPE ||
                 numeric == UA_NS0ID_WRITERGROUPTYPE ||
                 numeric == UA_NS0ID_DATASETWRITERTYPE ||
                 numeric == UA_NS0ID_READERGROUPTYPE ||
                 numeric == UA_NS0ID_DATASETREADERTYPE;
    }
    UA_NodeId_clear(&typeId);
    return result;
}

UA_StatusCode
pyPubSubComponentLifecycle(UA_Server *server, const UA_NodeId id,
                           UA_PubSubComponentType componentType,
                           UA_Boolean remove) {
    if(!pubsub_enabled)
        return UA_STATUSCODE_BADUSERACCESSDENIED;
    assertGIL();
    if(remove)
        return UA_STATUSCODE_GOOD;
    if(componentType == UA_PUBSUBCOMPONENT_PUBLISHEDDATASET ||
       componentType == UA_PUBSUBCOMPONENT_SUBSCRIBEDDDATASET)
        return UA_STATUSCODE_GOOD;

    void *nodeContext = NULL;
    UA_StatusCode status = UA_Server_getNodeContext(server, id, &nodeContext);
    if(status != UA_STATUSCODE_GOOD || !nodeContext)
        return status;
    PyObject *callback = node_state_machine(nodeContext);
    if(!callback) {
        if(PyErr_Occurred()) {
            PyErr_WriteUnraisable((PyObject *)nodeContext);
            return UA_STATUSCODE_BADINTERNALERROR;
        }
        return UA_STATUSCODE_GOOD;
    }
    Py_DECREF(callback);
    return update_component_state_machine(server, id, componentType, true);
}

PyObject *
pyNode_set_pubsub_state_machine(PyObject *self, PyObject *callback) {
    if(o6_require_pubsub() < 0)
        return NULL;
    if(callback != Py_None && !PyCallable_Check(callback)) {
        PyErr_SetString(PyExc_TypeError,
                        "state machine must be callable or None");
        return NULL;
    }
    PyServer *server = NULL;
    UA_Node *node = pyNodeStore_attachedNode(self, &server);
    if(!node)
        return NULL;
    if(node->head.nodeClass != UA_NODECLASS_OBJECT) {
        PyErr_SetString(PyExc_TypeError,
                        "state machine requires a PubSub Object node");
        return NULL;
    }

    PyObject *previous = node_state_machine(node->head.context);
    if(!previous && PyErr_Occurred())
        return NULL;
    if(set_node_state_machine(self, callback) < 0) {
        Py_XDECREF(previous);
        return NULL;
    }

    UA_PubSubComponentType componentType;
    UA_StatusCode status = UA_Server_getPubSubComponentType(
        server->server, node->head.nodeId, &componentType);
    if(status == UA_STATUSCODE_BADNOTFOUND &&
       is_active_pubsub_node_type(server->server, node->head.nodeId)) {
        /* During information-model construction the PyNode precedes the
         * component registration. The lifecycle callback installs it. */
        Py_XDECREF(previous);
        Py_RETURN_NONE;
    }
    if(status == UA_STATUSCODE_BADNOTFOUND) {
        if(previous) {
            set_node_state_machine(self, previous);
            Py_DECREF(previous);
        } else {
            set_node_state_machine(self, Py_None);
        }
        PyErr_SetString(
            PyExc_TypeError,
            "setStateMachine requires a concrete native PubSub component");
        return NULL;
    }
    if(status == UA_STATUSCODE_GOOD)
        status = update_component_state_machine(
            server->server, node->head.nodeId, componentType,
            callback != Py_None);
    if(status == UA_STATUSCODE_GOOD) {
        Py_XDECREF(previous);
        Py_RETURN_NONE;
    }

    /* Keep Python metadata and native configuration in agreement when an
     * existing component rejects the update (normally because it is enabled). */
    if(previous) {
        set_node_state_machine(self, previous);
        Py_DECREF(previous);
    } else {
        set_node_state_machine(self, Py_None);
    }
    return PyErr_StatusCode(status);
}

static PyObject *
offset_table_to_python(PyServer *server, UA_PubSubOffsetTable *table) {
    PyObject *message = PyBytes_FromStringAndSize(
        (const char *)table->networkMessage.data,
        (Py_ssize_t)table->networkMessage.length);
    PyObject *offsets = PyTuple_New((Py_ssize_t)table->offsetsSize);
    if(!message || !offsets) {
        Py_XDECREF(message);
        Py_XDECREF(offsets);
        return NULL;
    }
    for(size_t i = 0; i < table->offsetsSize; i++) {
        UA_NodeId component;
        UA_NodeId_init(&component);
        UA_StatusCode status = UA_NodeId_copy(
            &table->offsets[i].component, &component);
        if(status != UA_STATUSCODE_GOOD) {
            Py_DECREF(message);
            Py_DECREF(offsets);
            return PyErr_StatusCode(status);
        }
        PyObject *pyComponent = UA2PY(
            &component, &UA_TYPES[UA_TYPES_NODEID], &server->nsMapPy2UA);
        UA_NodeId_clear(&component);
        if(!pyComponent) {
            Py_DECREF(message);
            Py_DECREF(offsets);
            return NULL;
        }
        PyObject *entry = Py_BuildValue(
            "(inN)", (int)table->offsets[i].offsetType,
            (Py_ssize_t)table->offsets[i].offset, pyComponent);
        if(!entry) {
            Py_DECREF(message);
            Py_DECREF(offsets);
            return NULL;
        }
        PyTuple_SET_ITEM(offsets, (Py_ssize_t)i, entry);
    }
    return Py_BuildValue("NN", message, offsets);
}

PyObject *
pyNode_pubsub_offset_table(PyObject *self, PyObject *Py_UNUSED(args)) {
    if(o6_require_pubsub() < 0)
        return NULL;
    PyServer *server = NULL;
    UA_Node *node = pyNodeStore_attachedNode(self, &server);
    if(!node)
        return NULL;

    UA_PubSubComponentType componentType;
    UA_StatusCode status = UA_Server_getPubSubComponentType(
        server->server, node->head.nodeId, &componentType);
    if(status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);

    UA_PubSubOffsetTable table;
    memset(&table, 0, sizeof(table));
    if(componentType == UA_PUBSUBCOMPONENT_WRITERGROUP) {
        status = UA_Server_computeWriterGroupOffsetTable(
            server->server, node->head.nodeId, &table);
    } else if(componentType == UA_PUBSUBCOMPONENT_DATASETREADER) {
        status = UA_Server_computeDataSetReaderOffsetTable(
            server->server, node->head.nodeId, &table);
    } else {
        PyErr_SetString(
            PyExc_TypeError,
            "offsetTable requires a WriterGroup or DataSetReader");
        return NULL;
    }
    if(status != UA_STATUSCODE_GOOD) {
        UA_PubSubOffsetTable_clear(&table);
        return PyErr_StatusCode(status);
    }
    PyObject *result = offset_table_to_python(server, &table);
    UA_PubSubOffsetTable_clear(&table);
    return result;
}

PyObject *
pyNode_pubsub_publish(PyObject *self, PyObject *Py_UNUSED(args)) {
    if(o6_require_pubsub() < 0)
        return NULL;
    PyServer *server = NULL;
    UA_Node *node = pyNodeStore_attachedNode(self, &server);
    if(!node)
        return NULL;

    UA_PubSubComponentType componentType;
    UA_StatusCode status = UA_Server_getPubSubComponentType(
        server->server, node->head.nodeId, &componentType);
    if(status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);
    if(componentType != UA_PUBSUBCOMPONENT_WRITERGROUP) {
        PyErr_SetString(PyExc_TypeError,
                        "publish requires a concrete WriterGroup");
        return NULL;
    }

    status = UA_Server_triggerWriterGroupPublish(
        server->server, node->head.nodeId);
    if(status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);
    Py_RETURN_NONE;
}

static int
pubsub_connection_id(PyServer *server, PyObject *object, UA_NodeId *nodeId) {
    const UA_ServerConfig *config = UA_Server_getConfig(server->server);
    return extract_nodeid(object, nodeId, &server->nsMapPy2UA,
                          config->customDataTypes);
}

PyObject *
pyServer_set_pubsub_connection_enabled(PyObject *self, PyObject *args) {
    if(o6_require_pubsub() < 0)
        return NULL;
    PyObject *pyNodeId;
    int enabled;
    if(!PyArg_ParseTuple(args, "Op", &pyNodeId, &enabled))
        return NULL;

    PyServer *server = (PyServer*)self;
    UA_NodeId nodeId;
    if(pubsub_connection_id(server, pyNodeId, &nodeId) < 0)
        return NULL;
    UA_StatusCode status = enabled ?
        UA_Server_enablePubSubConnection(server->server, nodeId) :
        UA_Server_disablePubSubConnection(server->server, nodeId);
    UA_NodeId_clear(&nodeId);
    if(status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);
    Py_RETURN_NONE;
}

PyObject *
pyServer_set_pubsub_component_enabled(PyObject *self, PyObject *args) {
    if(o6_require_pubsub() < 0)
        return NULL;
    PyObject *pyNodeId;
    int enabled;
    if(!PyArg_ParseTuple(args, "Op", &pyNodeId, &enabled))
        return NULL;

    PyServer *server = (PyServer*)self;
    UA_NodeId nodeId;
    if(pubsub_connection_id(server, pyNodeId, &nodeId) < 0)
        return NULL;
    UA_PubSubComponentType type;
    UA_StatusCode status = UA_Server_getPubSubComponentType(
        server->server, nodeId, &type);
    if(status == UA_STATUSCODE_GOOD) {
        switch(type) {
        case UA_PUBSUBCOMPONENT_CONNECTION:
            status = enabled ?
                UA_Server_enablePubSubConnection(server->server, nodeId) :
                UA_Server_disablePubSubConnection(server->server, nodeId);
            break;
        case UA_PUBSUBCOMPONENT_WRITERGROUP:
            status = enabled ?
                UA_Server_enableWriterGroup(server->server, nodeId) :
                UA_Server_disableWriterGroup(server->server, nodeId);
            break;
        case UA_PUBSUBCOMPONENT_DATASETWRITER:
            status = enabled ?
                UA_Server_enableDataSetWriter(server->server, nodeId) :
                UA_Server_disableDataSetWriter(server->server, nodeId);
            break;
        case UA_PUBSUBCOMPONENT_READERGROUP:
            status = enabled ?
                UA_Server_enableReaderGroup(server->server, nodeId) :
                UA_Server_disableReaderGroup(server->server, nodeId);
            break;
        case UA_PUBSUBCOMPONENT_DATASETREADER:
            status = enabled ?
                UA_Server_enableDataSetReader(server->server, nodeId) :
                UA_Server_disableDataSetReader(server->server, nodeId);
            break;
        default:
            status = UA_STATUSCODE_BADNOTSUPPORTED;
            break;
        }
    }
    UA_NodeId_clear(&nodeId);
    if(status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);
    Py_RETURN_NONE;
}

PyObject *
pyServer_remove_pubsub_connection(PyObject *self, PyObject *args) {
    if(o6_require_pubsub() < 0)
        return NULL;
    PyObject *pyNodeId;
    if(!PyArg_ParseTuple(args, "O", &pyNodeId))
        return NULL;

    PyServer *server = (PyServer*)self;
    UA_NodeId nodeId;
    if(pubsub_connection_id(server, pyNodeId, &nodeId) < 0)
        return NULL;
    UA_StatusCode status =
        UA_Server_removePubSubConnection(server->server, nodeId);
    UA_NodeId_clear(&nodeId);
    if(status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);
    Py_RETURN_NONE;
}

PyObject *
pyServer_set_all_pubsub_components_enabled(PyObject *self, PyObject *args) {
    if(o6_require_pubsub() < 0)
        return NULL;
    int enabled;
    if(!PyArg_ParseTuple(args, "p", &enabled))
        return NULL;

    PyServer *server = (PyServer*)self;
    UA_StatusCode status = UA_STATUSCODE_GOOD;
    if(enabled)
        status = UA_Server_enableAllPubSubComponents(server->server);
    else
        UA_Server_disableAllPubSubComponents(server->server);
    if(status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);
    Py_RETURN_NONE;
}
