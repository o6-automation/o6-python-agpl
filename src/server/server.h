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
    UA_Boolean hasAsyncLoop; /* true when the server was created with an
                                asyncio event loop (needs special cleanup) */
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
PyObject* pyServer_add_reference(PyObject *self, PyObject *args);
PyObject* pyServer_delete_node(PyObject *self, PyObject *args);
PyObject* pyServer_read_value(PyObject *self, PyObject *args);
PyObject* pyServer_write_value(PyObject *self, PyObject *args);
PyObject* pyServer_register_historizing(PyObject *self, PyObject *args, PyObject *kwds);

/* Custom data type registration (type_registration.c) */
PyObject *linkServerCustomDataTypes(PyServer *self, PyObject *args);

#endif /* PYO6_SERVER_H_ */
