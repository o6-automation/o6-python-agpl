/* Copyright 2026 (c) o6 Automation GmbH */
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

static PyObject *
py_ua_string(const UA_String *value) {
    return PyUnicode_DecodeUTF8((const char *)value->data,
                                (Py_ssize_t)value->length, "strict");
}

static int
dict_set_owned(PyObject *dict, const char *key, PyObject *value) {
    if(!value)
        return -1;
    int result = PyDict_SetItemString(dict, key, value);
    Py_DECREF(value);
    return result;
}

static int
dict_set_unsigned(PyObject *dict, const char *key, unsigned long long value) {
    return dict_set_owned(dict, key, PyLong_FromUnsignedLongLong(value));
}

static int
dict_set_double(PyObject *dict, const char *key, double value) {
    return dict_set_owned(dict, key, PyFloat_FromDouble(value));
}

static int
dict_set_string(PyObject *dict, const char *key, const UA_String *value) {
    return dict_set_owned(dict, key, py_ua_string(value));
}

static int
dict_set_publisher_id(PyObject *dict, const UA_PublisherId *publisherId) {
    if(dict_set_unsigned(dict, "publisher_id_type", publisherId->idType) < 0)
        return -1;
    switch(publisherId->idType) {
    case UA_PUBLISHERIDTYPE_BYTE:
        return dict_set_unsigned(dict, "publisher_id", publisherId->id.byte);
    case UA_PUBLISHERIDTYPE_UINT16:
        return dict_set_unsigned(dict, "publisher_id", publisherId->id.uint16);
    case UA_PUBLISHERIDTYPE_UINT32:
        return dict_set_unsigned(dict, "publisher_id", publisherId->id.uint32);
    case UA_PUBLISHERIDTYPE_UINT64:
        return dict_set_unsigned(dict, "publisher_id", publisherId->id.uint64);
    case UA_PUBLISHERIDTYPE_STRING:
        return dict_set_string(dict, "publisher_id", &publisherId->id.string);
    default:
        PyErr_SetString(PyExc_RuntimeError, "invalid native PublisherId type");
        return -1;
    }
}

static int
dict_set_datagram_qos(PyObject *dict, const UA_ExtensionObject *settings) {
    const UA_String *category = NULL;
    const UA_ExtensionObject *qos = NULL;
    size_t count = 0;
    if(UA_ExtensionObject_hasDecodedType(settings,
           &UA_TYPES[UA_TYPES_DATAGRAMWRITERGROUPTRANSPORT2DATATYPE])) {
        const UA_DatagramWriterGroupTransport2DataType *v = settings->content.decoded.data;
        category = &v->qosCategory; qos = v->datagramQos; count = v->datagramQosSize;
    } else if(UA_ExtensionObject_hasDecodedType(settings,
                  &UA_TYPES[UA_TYPES_DATAGRAMDATASETREADERTRANSPORTDATATYPE])) {
        const UA_DatagramDataSetReaderTransportDataType *v = settings->content.decoded.data;
        category = &v->qosCategory; qos = v->datagramQos; count = v->datagramQosSize;
    } else {
        return 0;
    }
    if(dict_set_string(dict, "qos_category", category) < 0 ||
       dict_set_unsigned(dict, "datagram_qos_count", count) < 0) return -1;
    PyObject *labels = PyList_New(0);
    if(!labels) return -1;
    for(size_t i = 0; i < count; ++i) {
        const UA_String *label = NULL;
        if(UA_ExtensionObject_hasDecodedType(&qos[i], &UA_TYPES[UA_TYPES_TRANSMITQOSPRIORITYDATATYPE]))
            label = &((UA_TransmitQosPriorityDataType*)qos[i].content.decoded.data)->priorityLabel;
        else if(UA_ExtensionObject_hasDecodedType(&qos[i], &UA_TYPES[UA_TYPES_RECEIVEQOSPRIORITYDATATYPE]))
            label = &((UA_ReceiveQosPriorityDataType*)qos[i].content.decoded.data)->priorityLabel;
        if(!label) continue;
        PyObject *text = py_ua_string(label);
        if(!text || PyList_Append(labels, text) < 0) {
            Py_XDECREF(text); Py_DECREF(labels); return -1;
        }
        Py_DECREF(text);
    }
    return dict_set_owned(dict, "priority_labels", labels);
}

static int
dict_set_uadp_writer_settings(PyObject *dict,
                              const UA_ExtensionObject *settings) {
    if(!UA_ExtensionObject_hasDecodedType(
           settings, &UA_TYPES[UA_TYPES_UADPWRITERGROUPMESSAGEDATATYPE]))
        return 0;
    const UA_UadpWriterGroupMessageDataType *value =
        (const UA_UadpWriterGroupMessageDataType *)settings->content.decoded.data;
    if(dict_set_unsigned(dict, "network_message_content_mask",
                         value->networkMessageContentMask) < 0 ||
       dict_set_double(dict, "sampling_offset", value->samplingOffset) < 0)
        return -1;
    PyObject *offsets = PyTuple_New((Py_ssize_t)value->publishingOffsetSize);
    if(!offsets)
        return -1;
    for(size_t i = 0; i < value->publishingOffsetSize; i++) {
        PyObject *offset = PyFloat_FromDouble(value->publishingOffset[i]);
        if(!offset) {
            Py_DECREF(offsets);
            return -1;
        }
        PyTuple_SET_ITEM(offsets, (Py_ssize_t)i, offset);
    }
    return dict_set_owned(dict, "publishing_offsets", offsets);
}

static int
dict_set_uadp_reader_settings(PyObject *dict,
                              const UA_ExtensionObject *settings) {
    if(!UA_ExtensionObject_hasDecodedType(
           settings, &UA_TYPES[UA_TYPES_UADPDATASETREADERMESSAGEDATATYPE]))
        return 0;
    const UA_UadpDataSetReaderMessageDataType *value =
        (const UA_UadpDataSetReaderMessageDataType *)settings->content.decoded.data;
    if(dict_set_unsigned(dict, "group_version", value->groupVersion) < 0 ||
       dict_set_unsigned(dict, "network_message_number",
                         value->networkMessageNumber) < 0 ||
       dict_set_unsigned(dict, "data_set_offset", value->dataSetOffset) < 0 ||
       dict_set_unsigned(dict, "network_message_content_mask",
                         value->networkMessageContentMask) < 0 ||
       dict_set_unsigned(dict, "data_set_message_content_mask",
                         value->dataSetMessageContentMask) < 0 ||
       dict_set_double(dict, "publishing_interval", value->publishingInterval) < 0 ||
       dict_set_double(dict, "receive_offset", value->receiveOffset) < 0 ||
       dict_set_double(dict, "processing_offset", value->processingOffset) < 0)
        return -1;
    return 0;
}

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

PyObject *
pyNode_pubsub_configuration(PyObject *self, PyObject *Py_UNUSED(args)) {
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

    PyObject *configuration = PyDict_New();
    if(!configuration)
        return NULL;
    if(dict_set_unsigned(configuration, "component_type", componentType) < 0)
        goto error;

    switch(componentType) {
    case UA_PUBSUBCOMPONENT_CONNECTION: {
        UA_PubSubConnectionConfig config;
        memset(&config, 0, sizeof(config));
        status = UA_Server_getPubSubConnectionConfig(
            server->server, node->head.nodeId, &config);
        if(status == UA_STATUSCODE_GOOD &&
           (dict_set_string(configuration, "transport_profile_uri",
                            &config.transportProfileUri) < 0 ||
            dict_set_publisher_id(configuration, &config.publisherId) < 0))
            status = UA_STATUSCODE_BADINTERNALERROR;
        if(status == UA_STATUSCODE_GOOD &&
           UA_Variant_hasScalarType(
               &config.address,
               &UA_TYPES[UA_TYPES_NETWORKADDRESSURLDATATYPE])) {
            const UA_NetworkAddressUrlDataType *address =
                (const UA_NetworkAddressUrlDataType *)config.address.data;
            if(dict_set_string(configuration, "network_interface",
                               &address->networkInterface) < 0 ||
               dict_set_string(configuration, "url", &address->url) < 0)
                status = UA_STATUSCODE_BADINTERNALERROR;
        }
        UA_PubSubConnectionConfig_clear(&config);
        break;
    }
    case UA_PUBSUBCOMPONENT_WRITERGROUP: {
        UA_WriterGroupConfig config;
        memset(&config, 0, sizeof(config));
        status = UA_Server_getWriterGroupConfig(
            server->server, node->head.nodeId, &config);
        if(status == UA_STATUSCODE_GOOD &&
           (dict_set_unsigned(configuration, "writer_group_id",
                              config.writerGroupId) < 0 ||
            dict_set_double(configuration, "publishing_interval",
                            config.publishingInterval) < 0 ||
            dict_set_unsigned(configuration, "priority", config.priority) < 0 ||
            dict_set_datagram_qos(configuration, &config.transportSettings) < 0 ||
            dict_set_uadp_writer_settings(configuration,
                                          &config.messageSettings) < 0))
            status = UA_STATUSCODE_BADINTERNALERROR;
        UA_WriterGroupConfig_clear(&config);
        break;
    }
    case UA_PUBSUBCOMPONENT_READERGROUP: {
        UA_ReaderGroupConfig config;
        memset(&config, 0, sizeof(config));
        status = UA_Server_getReaderGroupConfig(
            server->server, node->head.nodeId, &config);
        UA_ReaderGroupConfig_clear(&config);
        break;
    }
    case UA_PUBSUBCOMPONENT_DATASETREADER: {
        UA_DataSetReaderConfig config;
        memset(&config, 0, sizeof(config));
        status = UA_Server_getDataSetReaderConfig(
            server->server, node->head.nodeId, &config);
        if(status == UA_STATUSCODE_GOOD &&
           (dict_set_publisher_id(configuration, &config.publisherId) < 0 ||
            dict_set_unsigned(configuration, "writer_group_id",
                              config.writerGroupId) < 0 ||
            dict_set_unsigned(configuration, "data_set_writer_id",
                              config.dataSetWriterId) < 0 ||
            dict_set_double(configuration, "message_receive_timeout",
                            config.messageReceiveTimeout) < 0 ||
            dict_set_datagram_qos(configuration, &config.transportSettings) < 0 ||
            dict_set_uadp_reader_settings(configuration,
                                          &config.messageSettings) < 0))
            status = UA_STATUSCODE_BADINTERNALERROR;
        UA_DataSetReaderConfig_clear(&config);
        break;
    }
    default:
        Py_DECREF(configuration);
        PyErr_SetString(PyExc_TypeError,
                        "configuration requires a PubSubConnection, "
                        "WriterGroup, ReaderGroup, or DataSetReader");
        return NULL;
    }

    if(status != UA_STATUSCODE_GOOD) {
        Py_DECREF(configuration);
        if(PyErr_Occurred())
            return NULL;
        return PyErr_StatusCode(status);
    }
    return configuration;

error:
    Py_DECREF(configuration);
    return NULL;
}

PyObject *
pyNode_pubsub_field_source(PyObject *self, PyObject *fieldIdObject) {
    if(o6_require_pubsub() < 0)
        return NULL;
    PyServer *server = NULL;
    UA_Node *node = pyNodeStore_attachedNode(self, &server);
    if(!node)
        return NULL;

    UA_NodeId fieldId;
    const UA_ServerConfig *serverConfig = UA_Server_getConfig(server->server);
    if(extract_nodeid(fieldIdObject, &fieldId, &server->nsMapPy2UA,
                      serverConfig->customDataTypes) < 0)
        return NULL;

    UA_DataSetFieldConfig config;
    memset(&config, 0, sizeof(config));
    UA_StatusCode status = UA_Server_getDataSetFieldConfig(
        server->server, fieldId, &config);
    UA_NodeId_clear(&fieldId);
    if(status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);
    if(config.dataSetFieldType != UA_PUBSUB_DATASETFIELD_VARIABLE) {
        UA_DataSetFieldConfig_clear(&config);
        PyErr_SetString(PyExc_TypeError,
                        "only PublishedVariable DataSetFields are supported");
        return NULL;
    }

    UA_NodeId source;
    UA_NodeId_init(&source);
    status = UA_NodeId_copy(
        &config.field.variable.publishParameters.publishedVariable, &source);
    UA_DataSetFieldConfig_clear(&config);
    if(status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);
    PyObject *result = UA2PY(&source, &UA_TYPES[UA_TYPES_NODEID],
                             &server->nsMapPy2UA);
    UA_NodeId_clear(&source);
    return result;
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

/* Native standalone datasets must be registered with the PubSub manager, not
 * merely represented by Python-created address-space nodes. */
PyObject *
pyServer_add_subscribed_dataset(PyObject *self, PyObject *args) {
    if(o6_require_pubsub() < 0)
        return NULL;
    PyObject *name, *metadata, *targets;
    if(!PyArg_ParseTuple(args, "OOO", &name, &metadata, &targets))
        return NULL;
    PyServer *server = (PyServer*)self;
    const UA_ServerConfig *config = UA_Server_getConfig(server->server);
    UA_SubscribedDataSetConfig sds = {0};
    sds.subscribedDataSetType = UA_PUBSUB_SDS_TARGET;
    if(!PY2UA(name, &sds.name, &UA_TYPES[UA_TYPES_STRING],
              &server->nsMapPy2UA, config->customDataTypes) ||
       !PY2UA(metadata, &sds.dataSetMetaData, &UA_TYPES[UA_TYPES_DATASETMETADATATYPE],
              &server->nsMapPy2UA, config->customDataTypes) ||
       !PY2UA(targets, &sds.subscribedDataSet.target, &UA_TYPES[UA_TYPES_TARGETVARIABLESDATATYPE],
              &server->nsMapPy2UA, config->customDataTypes)) {
        UA_SubscribedDataSetConfig_clear(&sds);
        return NULL;
    }
    if(sds.dataSetMetaData.fieldsSize != sds.subscribedDataSet.target.targetVariablesSize) {
        UA_SubscribedDataSetConfig_clear(&sds);
        return PyErr_StatusCode(UA_STATUSCODE_BADINVALIDARGUMENT);
    }
    UA_NodeId id = UA_NODEID_NULL;
    UA_StatusCode status = UA_Server_addSubscribedDataSet(server->server, &sds, &id);
    UA_SubscribedDataSetConfig_clear(&sds);
    if(status != UA_STATUSCODE_GOOD) {
        UA_NodeId_clear(&id);
        return PyErr_StatusCode(status);
    }
    PyObject *result = UA2PY(&id, &UA_TYPES[UA_TYPES_NODEID], &server->nsMapPy2UA);
    UA_NodeId_clear(&id);
    return result;
}

PyObject *
pyServer_remove_subscribed_dataset(PyObject *self, PyObject *args) {
    if(o6_require_pubsub() < 0)
        return NULL;
    PyObject *pyId;
    if(!PyArg_ParseTuple(args, "O", &pyId))
        return NULL;
    PyServer *server = (PyServer*)self;
    UA_NodeId id;
    if(pubsub_connection_id(server, pyId, &id) < 0)
        return NULL;
    UA_StatusCode status = UA_Server_removeSubscribedDataSet(server->server, id);
    UA_NodeId_clear(&id);
    if(status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);
    Py_RETURN_NONE;
}

/* Create a published-items template without dropping its metadata. */
PyObject *
pyServer_add_published_dataset(PyObject *self, PyObject *args) {
    if(o6_require_pubsub() < 0)
        return NULL;
    PyObject *pyConfig;
    if(!PyArg_ParseTuple(args, "O", &pyConfig))
        return NULL;
    PyServer *server = (PyServer*)self;
    const UA_ServerConfig *config = UA_Server_getConfig(server->server);
    UA_PublishedDataSetDataType value = {0};
    if(!PY2UA(pyConfig, &value, &UA_TYPES[UA_TYPES_PUBLISHEDDATASETDATATYPE],
              &server->nsMapPy2UA, config->customDataTypes))
        return NULL;
    UA_StatusCode status = UA_STATUSCODE_BADNOTSUPPORTED;
    UA_NodeId id = UA_NODEID_NULL;
    if(value.dataSetFolderSize == 0 && UA_ExtensionObject_hasDecodedType(
           &value.dataSetSource, &UA_TYPES[UA_TYPES_PUBLISHEDDATAITEMSDATATYPE])) {
        UA_PublishedDataItemsDataType *items = value.dataSetSource.content.decoded.data;
        UA_PublishedDataSetConfig pds = {0};
        pds.name = value.name;
        pds.publishedDataSetType = UA_PUBSUB_DATASET_PUBLISHEDITEMS_TEMPLATE;
        pds.config.itemsTemplate.metaData = value.dataSetMetaData;
        pds.config.itemsTemplate.variablesToAddSize = items->publishedDataSize;
        pds.config.itemsTemplate.variablesToAdd = items->publishedData;
        status = UA_Server_addPublishedDataSet(server->server, &pds, &id).addResult;
    }
    UA_PublishedDataSetDataType_clear(&value);
    if(status != UA_STATUSCODE_GOOD) {
        UA_NodeId_clear(&id);
        return PyErr_StatusCode(status);
    }
    PyObject *result = UA2PY(&id, &UA_TYPES[UA_TYPES_NODEID], &server->nsMapPy2UA);
    UA_NodeId_clear(&id);
    return result;
}

/* Read-only typed snapshots of native PubSub components. */
PyObject *
pyServer_pubsub_configuration(PyObject *self, PyObject *args) {
    PyObject *pyId;
    if(!PyArg_ParseTuple(args, "O", &pyId))
        return NULL;
    if(o6_require_pubsub() < 0)
        return NULL;
    PyServer *server = (PyServer*)self;
    UA_NodeId id = UA_NODEID_NULL;
    if(pubsub_connection_id(server, pyId, &id) < 0)
        return NULL;
    UA_PubSubComponentType kind;
    UA_StatusCode status = UA_Server_getPubSubComponentType(server->server, id, &kind);
    PyObject *result = NULL;
    if(status != UA_STATUSCODE_GOOD)
        goto done;
    switch(kind) {
    case UA_PUBSUBCOMPONENT_CONNECTION: {
        UA_PubSubConnectionConfig old = {0};
        status = UA_Server_getPubSubConnectionConfig(server->server, id, &old);
        if(status != UA_STATUSCODE_GOOD)
            break;
        UA_PubSubConnectionDataType value = {0};
        {
            value.name = old.name;
            value.enabled = old.enabled;
            value.transportProfileUri = old.transportProfileUri;
            value.connectionProperties = old.connectionProperties.map;
            value.connectionPropertiesSize = old.connectionProperties.mapSize;
            UA_PublisherId_toVariant(&old.publisherId, &value.publisherId);
            if(old.address.type)
                UA_ExtensionObject_setValueNoDelete(&value.address, old.address.data, old.address.type);
            if(old.connectionTransportSettings.type)
                UA_ExtensionObject_setValueNoDelete(&value.transportSettings,
                    old.connectionTransportSettings.data, old.connectionTransportSettings.type);
            UA_PubSubConnectionDataType copy = {0};
            status = UA_copy(&value, &copy, &UA_TYPES[UA_TYPES_PUBSUBCONNECTIONDATATYPE]);
            if(status == UA_STATUSCODE_GOOD)
                result = UA2PY(&copy, &UA_TYPES[UA_TYPES_PUBSUBCONNECTIONDATATYPE], &server->nsMapPy2UA);
            UA_PubSubConnectionDataType_clear(&copy);
            /* value.publisherId borrows storage from old. */
        }
        UA_PubSubConnectionConfig_clear(&old);
        break;
    }
    case UA_PUBSUBCOMPONENT_WRITERGROUP: {
        UA_WriterGroupConfig old = {0};
        status = UA_Server_getWriterGroupConfig(server->server, id, &old);
        if(status != UA_STATUSCODE_GOOD)
            break;
        UA_PubSubState componentState = UA_PUBSUBSTATE_DISABLED;
        UA_Server_getWriterGroupState(server->server, id, &componentState);
        old.enabled = componentState != UA_PUBSUBSTATE_DISABLED && componentState != UA_PUBSUBSTATE_ERROR;
        UA_WriterGroupDataType value = {0};
        {
            value.name = old.name;
            value.securityKeyServices = old.securityKeyServices;
            value.securityKeyServicesSize = old.securityKeyServicesSize;
            value.maxNetworkMessageSize = old.maxNetworkMessageSize;
            value.localeIds = old.localeIds;
            value.localeIdsSize = old.localeIdsSize;
            value.headerLayoutUri = old.headerLayoutUri;
            value.enabled = old.enabled;
            value.writerGroupId = old.writerGroupId;
            value.publishingInterval = old.publishingInterval;
            value.keepAliveTime = old.keepAliveTime;
            value.priority = old.priority;
            value.securityMode = old.securityMode;
            value.securityGroupId = old.securityGroupId;
            value.transportSettings = old.transportSettings;
            value.messageSettings = old.messageSettings;
            value.groupProperties = old.groupProperties.map;
            value.groupPropertiesSize = old.groupProperties.mapSize;
            UA_WriterGroupDataType copy = {0};
            status = UA_copy(&value, &copy, &UA_TYPES[UA_TYPES_WRITERGROUPDATATYPE]);
            if(status == UA_STATUSCODE_GOOD)
                result = UA2PY(&copy, &UA_TYPES[UA_TYPES_WRITERGROUPDATATYPE], &server->nsMapPy2UA);
            UA_WriterGroupDataType_clear(&copy);
        }
        UA_WriterGroupConfig_clear(&old);
        break;
    }
    case UA_PUBSUBCOMPONENT_READERGROUP: {
        UA_ReaderGroupConfig old = {0};
        status = UA_Server_getReaderGroupConfig(server->server, id, &old);
        if(status != UA_STATUSCODE_GOOD)
            break;
        UA_PubSubState componentState = UA_PUBSUBSTATE_DISABLED;
        UA_Server_getReaderGroupState(server->server, id, &componentState);
        old.enabled = componentState != UA_PUBSUBSTATE_DISABLED && componentState != UA_PUBSUBSTATE_ERROR;
        UA_ReaderGroupDataType value = {0};
        {
            value.name = old.name;
            value.securityKeyServices = old.securityKeyServices;
            value.securityKeyServicesSize = old.securityKeyServicesSize;
            value.maxNetworkMessageSize = old.maxNetworkMessageSize;
            value.messageSettings = old.messageSettings;
            value.enabled = old.enabled;
            value.securityMode = old.securityMode;
            value.securityGroupId = old.securityGroupId;
            value.transportSettings = old.transportSettings;
            value.groupProperties = old.groupProperties.map;
            value.groupPropertiesSize = old.groupProperties.mapSize;
            UA_ReaderGroupDataType copy = {0};
            status = UA_copy(&value, &copy, &UA_TYPES[UA_TYPES_READERGROUPDATATYPE]);
            if(status == UA_STATUSCODE_GOOD)
                result = UA2PY(&copy, &UA_TYPES[UA_TYPES_READERGROUPDATATYPE], &server->nsMapPy2UA);
            UA_ReaderGroupDataType_clear(&copy);
        }
        UA_ReaderGroupConfig_clear(&old);
        break;
    }
    case UA_PUBSUBCOMPONENT_DATASETWRITER: {
        UA_DataSetWriterConfig old = {0};
        status = UA_Server_getDataSetWriterConfig(server->server, id, &old);
        if(status != UA_STATUSCODE_GOOD)
            break;
        UA_PubSubState componentState = UA_PUBSUBSTATE_DISABLED;
        UA_Server_getDataSetWriterState(server->server, id, &componentState);
        old.enabled = componentState != UA_PUBSUBSTATE_DISABLED && componentState != UA_PUBSUBSTATE_ERROR;
        UA_DataSetWriterDataType value = {0};
        {
            value.name = old.name;
            value.enabled = old.enabled;
            value.dataSetWriterId = old.dataSetWriterId;
            value.dataSetFieldContentMask = old.dataSetFieldContentMask;
            value.keyFrameCount = old.keyFrameCount;
            value.messageSettings = old.messageSettings;
            value.transportSettings = old.transportSettings;
            value.dataSetName = old.dataSetName;
            value.dataSetWriterProperties = old.dataSetWriterProperties.map;
            value.dataSetWriterPropertiesSize = old.dataSetWriterProperties.mapSize;
            UA_DataSetWriterDataType copy = {0};
            status = UA_copy(&value, &copy, &UA_TYPES[UA_TYPES_DATASETWRITERDATATYPE]);
            if(status == UA_STATUSCODE_GOOD)
                result = UA2PY(&copy, &UA_TYPES[UA_TYPES_DATASETWRITERDATATYPE], &server->nsMapPy2UA);
            UA_DataSetWriterDataType_clear(&copy);
        }
        UA_DataSetWriterConfig_clear(&old);
        break;
    }
    case UA_PUBSUBCOMPONENT_DATASETREADER: {
        UA_DataSetReaderConfig old = {0};
        status = UA_Server_getDataSetReaderConfig(server->server, id, &old);
        if(status != UA_STATUSCODE_GOOD)
            break;
        UA_PubSubState componentState = UA_PUBSUBSTATE_DISABLED;
        UA_Server_getDataSetReaderState(server->server, id, &componentState);
        old.enabled = componentState != UA_PUBSUBSTATE_DISABLED && componentState != UA_PUBSUBSTATE_ERROR;
        UA_DataSetReaderDataType value = {0};
        {
            value.name = old.name;
            value.keyFrameCount = old.keyFrameCount;
            value.headerLayoutUri = old.headerLayoutUri;
            value.dataSetReaderProperties = old.dataSetReaderProperties.map;
            value.dataSetReaderPropertiesSize = old.dataSetReaderProperties.mapSize;
            value.enabled = old.enabled;
            value.writerGroupId = old.writerGroupId;
            value.dataSetWriterId = old.dataSetWriterId;
            value.dataSetMetaData = old.dataSetMetaData;
            value.dataSetFieldContentMask = old.dataSetFieldContentMask;
            value.messageReceiveTimeout = old.messageReceiveTimeout;
            value.messageSettings = old.messageSettings;
            value.transportSettings = old.transportSettings;
            if(old.publisherIdFilterEnabled)
                UA_PublisherId_toVariant(&old.publisherId, &value.publisherId);
            UA_StandaloneSubscribedDataSetRefDataType standalone = {old.linkedStandaloneSubscribedDataSetName};
            if(old.linkedStandaloneSubscribedDataSetName.length)
                UA_ExtensionObject_setValueNoDelete(&value.subscribedDataSet, &standalone,
                    &UA_TYPES[UA_TYPES_STANDALONESUBSCRIBEDDATASETREFDATATYPE]);
            else
                UA_ExtensionObject_setValueNoDelete(&value.subscribedDataSet, &old.subscribedDataSet.target,
                    &UA_TYPES[UA_TYPES_TARGETVARIABLESDATATYPE]);
            UA_DataSetReaderDataType copy = {0};
            status = UA_copy(&value, &copy, &UA_TYPES[UA_TYPES_DATASETREADERDATATYPE]);
            if(status == UA_STATUSCODE_GOOD)
                result = UA2PY(&copy, &UA_TYPES[UA_TYPES_DATASETREADERDATATYPE], &server->nsMapPy2UA);
            UA_DataSetReaderDataType_clear(&copy);
            /* value.publisherId borrows storage from old. */
        }
        UA_DataSetReaderConfig_clear(&old);
        break;
    }
    default:
        status = UA_STATUSCODE_BADNOTSUPPORTED;
    }
 done:
    UA_NodeId_clear(&id);
    if(status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);
    return result;
}
