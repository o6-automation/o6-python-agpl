/* Copyright 2026 (c) o6 Automation GmbH (Author: Andreas Ebner) */
#ifndef PYO6_SERVER_H_
#define PYO6_SERVER_H_

#include "../module.h"
#include <open62541/server.h>
#include <open62541/server_config_default.h>
#include <open62541/plugin/historydata/history_data_backend_memory.h>
#include <open62541/plugin/historydata/history_data_gathering_default.h>
#include <open62541/plugin/historydata/history_database_default.h>

/* PyServer structure definition */
typedef struct {
    PyObject_HEAD
    UA_Server *server;
    UA_Boolean running;
    UA_Boolean hasHistoryDB; /* true after set_history_database() */
    UA_HistoryDataGathering gathering; /* kept alive for registerNodeId */
    PyObject *linked_type_capsules;  /* list of link-capsules keeping thin
                                       UA_DataTypeArray wrappers alive */
} PyServer;

/* Forward declaration for PyServerConfig */
typedef struct {
    PyObject_HEAD
    PyServer *py_server; /* Python server object reference */
} PyServerConfig;

extern PyTypeObject PyServerConfigType;

/* Factory to create a PyServerConfig for a given PyServer* */
PyObject *PyServerConfig_New(PyServer *py_server);

/* Server node management function declarations */
PyObject* pyServer_add_variable_node(PyObject *self, PyObject *args);
PyObject* pyServer_add_object_node(PyObject *self, PyObject *args);
PyObject* pyServer_add_object_type_node(PyObject *self, PyObject *args);
PyObject* pyServer_add_data_type_node(PyObject *self, PyObject *args);
PyObject* pyServer_add_variable_type_node(PyObject *self, PyObject *args);
PyObject* pyServer_add_method_node(PyObject *self, PyObject *args);
PyObject* pyServer_find_data_type(PyObject *self, PyObject *args);
PyObject* pyServer_add_reference(PyObject *self, PyObject *args);
PyObject* pyServer_delete_node(PyObject *self, PyObject *args);
PyObject* pyServer_read_value(PyObject *self, PyObject *args);
PyObject* pyServer_write_value(PyObject *self, PyObject *args);
PyObject* pyServer_call(PyObject *self, PyObject *args);
PyObject* pyServer_register_historizing(PyObject *self, PyObject *args, PyObject *kwds);
PyObject* pyServer_browse_node(PyObject *self, PyObject *args);
PyObject* pyServer_read_object_property(PyObject *self, PyObject *args);
PyObject* pyServer_write_object_property(PyObject *self, PyObject *args);
PyObject* pyServer_read_attribute(PyObject *self, PyObject *args);
PyObject* pyServer_write_attribute(PyObject *self, PyObject *args);
PyObject* pyServer_write_data_value(PyObject *self, PyObject *args);
PyObject* pyServer_translate_browse_paths(PyObject *self, PyObject *args);
PyObject* pyServer_read_node_info(PyObject *self, PyObject *args);

/* Remove all method callbacks registered for the given server */
void clear_server_callbacks(UA_Server *server);

/* Internal Python type used as a done-callback on asyncio Tasks created for
 * async method callbacks.  Must be initialized via Server_initTypes(). */
extern PyTypeObject PyMethodDoneCbType;
int Server_initTypes(void);

/* Custom data type registration (type_registration.c) */
PyObject *linkServerCustomDataTypes(PyServer *self, PyObject *args);

#endif /* PYO6_SERVER_H_ */
