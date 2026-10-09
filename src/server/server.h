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

#ifndef PYO6_SERVER_H_
#define PYO6_SERVER_H_

#include "../module.h"
#include <open62541/server.h>
#include <open62541/server_config_default.h>
#include <open62541/server_pubsub.h>
#include "server_history.h"

/* PyServer structure definition */
typedef struct {
    PyObject_HEAD
    UA_Server *server;
    UA_Boolean running;
    PyServerHistory history; /* history database, gathering and ring backend */

    UA_NamespaceMapping nsMapPy2UA; /* maps python <-> UA namespaces, local == python, remote == UA */

    /* GC-visible ownership for Python objects borrowed by native callbacks. */
    PyObject *runtimeCallbackRefs;
    PyObject *localMonitoredItemIds;

} PyServer;

int pyHistoryBackend_traverse(UA_HistoryDataBackend *backend, visitproc visit, void *arg);

int pyServer_own_callback_ref(PyServer *server, PyObject *object);
void pyServer_release_callback_ref(PyServer *server, PyObject *object);

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
PyObject* pyServer_add_node_begin(PyObject *self, PyObject *args);
PyObject* pyServer_add_node_raw(PyObject *self, PyObject *args);
PyObject* pyServer_add_node_prepare(PyObject *self, PyObject *args);
PyObject* pyServer_add_node_finish(PyObject *self, PyObject *args);
PyObject* pyServer_set_type_abstract(PyObject *self, PyObject *args);
PyObject* pyServer_add_object_node(PyObject *self, PyObject *args);
PyObject* pyServer_add_object_type_node(PyObject *self, PyObject *args);
PyObject* pyServer_add_data_type_node(PyObject *self, PyObject *args);
PyObject* pyServer_add_variable_type_node(PyObject *self, PyObject *args);
PyObject* pyServer_add_reference_type_node(PyObject *self, PyObject *args);
PyObject* pyServer_add_view_node(PyObject *self, PyObject *args);
PyObject* pyServer_add_method_node(PyObject *self, PyObject *args);
PyObject* pyServer_set_callback_slot(PyObject *self, PyObject *args);
PyObject* pyServer_set_local_value(PyObject *self, PyObject *args);
PyObject* pyServer_get_callback(PyObject *self, PyObject *args);
PyObject* pyServer_get_node_type(PyObject *self, PyObject *args);
PyObject* pyServer_find_data_type(PyObject *self, PyObject *args);
PyObject* pyServer_add_reference(PyObject *self, PyObject *args);
PyObject* pyServer_delete_reference(PyObject *self, PyObject *args);
PyObject* pyServer_delete_node(PyObject *self, PyObject *args);
PyObject* pyServer_read_value(PyObject *self, PyObject *args);
PyObject* pyServer_write_value(PyObject *self, PyObject *args);
PyObject* pyServer_call(PyObject *self, PyObject *args);
PyObject* pyServer_register_historizing(PyObject *self, PyObject *args, PyObject *kwds);
PyObject* pyServer_history_add(PyObject *self, PyObject *args, PyObject *kwds);
PyObject* pyServer_history_pause(PyObject *self, PyObject *args, PyObject *kwds);
PyObject* pyServer_history_insert(PyObject *self, PyObject *args, PyObject *kwds);
PyObject* pyServer_history_remove(PyObject *self, PyObject *args);
PyObject* pyServer_history_read(PyObject *self, PyObject *args, PyObject *kwds);
PyObject* pyServer_history_stats(PyObject *self, PyObject *args);
PyObject* pyServer_history_clear(PyObject *self, PyObject *args);
PyObject* pyServer_read_object_property(PyObject *self, PyObject *args);
PyObject* pyServer_write_object_property(PyObject *self, PyObject *args);
PyObject* pyServer_read_attribute(PyObject *self, PyObject *args);
PyObject* pyServer_read_data_value(PyObject *self, PyObject *args);
PyObject* pyServer_write_attribute(PyObject *self, PyObject *args);
PyObject* pyServer_write_data_value(PyObject *self, PyObject *args);
PyObject* pyNode_read_attribute(PyObject *self, PyObject *args);
PyObject* pyNode_write_attribute(PyObject *self, PyObject *args);
PyObject* pyServer_translate_browse_paths(PyObject *self, PyObject *args);
PyObject* pyServer_browse(PyObject *self, PyObject *args);
PyObject* pyServer_browse_next(PyObject *self, PyObject *args);
PyObject* pyServer_browse_recursive(PyObject *self, PyObject *args);
PyObject* pyServer_translate_browse_paths_to_nodeids(PyObject *self, PyObject *args);
PyObject* pyServer_browse_simplified_browse_paths(PyObject *self, PyObject *args);
PyObject* pyServer_for_each_child_node(PyObject *self, PyObject *args);
PyObject* pyServer_register_discovery(PyObject *self, PyObject *args);
PyObject* pyServer_deregister_discovery(PyObject *self, PyObject *args);
PyObject* pyServer_register_server(PyObject *self, PyObject *args);
PyObject* pyServer_deregister_server(PyObject *self, PyObject *args);
PyObject* pyServer_register_server_on_network(PyObject *self, PyObject *args);
PyObject* pyServer_deregister_server_on_network(PyObject *self, PyObject *args);
PyObject* pyServer_set_register_server_callback(PyObject *self, PyObject *args);
PyObject* pyServer_set_server_on_network_callback(PyObject *self, PyObject *args);
PyObject* pyServer_emit_event(PyObject *self, PyObject *args);
PyObject* pyServer_pubsub_configuration(PyObject *self, PyObject *args);
PyObject* pyServer_add_published_dataset(PyObject *self, PyObject *args);
PyObject* pyServer_add_subscribed_dataset(PyObject *self, PyObject *args);
PyObject* pyServer_remove_subscribed_dataset(PyObject *self, PyObject *args);
PyObject* pyServer_set_pubsub_connection_enabled(PyObject *self, PyObject *args);
PyObject* pyServer_set_pubsub_component_enabled(PyObject *self, PyObject *args);
PyObject* pyServer_remove_pubsub_connection(PyObject *self, PyObject *args);
PyObject* pyServer_set_all_pubsub_components_enabled(PyObject *self, PyObject *args);
PyObject* pyNode_set_pubsub_state_machine(PyObject *self, PyObject *callback);
PyObject* pyNode_pubsub_configuration(PyObject *self, PyObject *args);
PyObject* pyNode_pubsub_field_source(PyObject *self, PyObject *args);
PyObject* pyNode_pubsub_offset_table(PyObject *self, PyObject *args);
PyObject* pyNode_pubsub_publish(PyObject *self, PyObject *args);
UA_StatusCode pyPubSubComponentLifecycle(
    UA_Server *server, const UA_NodeId id,
    UA_PubSubComponentType componentType, UA_Boolean remove);

/* RBAC and Session management */
PyObject* pyServer_close_session(PyObject *self, PyObject *args);
PyObject* pyServer_get_session_attribute(PyObject *self, PyObject *args);
PyObject* pyServer_set_session_attribute(PyObject *self, PyObject *args);
PyObject* pyServer_delete_session_attribute(PyObject *self, PyObject *args);
PyObject* pyServer_get_session_roles(PyObject *self, PyObject *args);
PyObject* pyServer_set_session_roles(PyObject *self, PyObject *args);
PyObject* pyServer_add_role(PyObject *self, PyObject *args);
PyObject* pyServer_update_role(PyObject *self, PyObject *args);
PyObject* pyServer_remove_role(PyObject *self, PyObject *args);
PyObject* pyServer_get_role(PyObject *self, PyObject *args);
PyObject* pyServer_get_roles(PyObject *self, PyObject *args);
PyObject* pyServer_set_node_role_permissions(PyObject *self, PyObject *args);
PyObject* pyServer_get_node_role_permissions(PyObject *self, PyObject *args);
PyObject* pyServer_remove_node_role_permissions(PyObject *self, PyObject *args);
PyObject* pyServer_add_role_permissions(PyObject *self, PyObject *args);
PyObject* pyServer_remove_role_permissions(PyObject *self, PyObject *args);
PyObject* pyServer_set_namespace_role_permissions(PyObject *self, PyObject *args);
PyObject* pyServer_get_namespace_role_permissions(PyObject *self, PyObject *args);
PyObject* pyServer_set_all_permissions_for_anonymous(PyObject *self, PyObject *args);

/* MonitoredItem Service Set */
PyObject* pyServer_create_data_change_monitored_item(PyObject *self, PyObject *args);
PyObject* pyServer_delete_monitored_item(PyObject *self, PyObject *args);
PyObject* pyServer_create_event_monitored_item(PyObject *self, PyObject *args);

/* Server Callbacks */
PyObject* pyServer_add_repeated_callback(PyObject *self, PyObject *args);
PyObject* pyServer_change_repeated_callback_interval(PyObject *self, PyObject *args);
PyObject* pyServer_remove_callback(PyObject *self, PyObject *args);

/* Cancel callbacks whose lifetime is not owned by a node. */
void clear_server_runtime_callbacks(UA_Server *server, PyServer *py_server);
void clear_server_monitored_item_callbacks(UA_Server *server);
void clear_server_repeat_callbacks(UA_Server *server);

/* Global lifecycle hook. Called after recursive instance construction, when
 * the final HasTypeDefinition is available. */
UA_StatusCode pyGlobalNodeConstructor(UA_Server *server,
                                      const UA_NodeId *sessionId,
                                      void *sessionContext,
                                      const UA_NodeId *nodeId,
                                      void **nodeContext);
UA_StatusCode pyGlobalNodeEarlyConstructor(UA_Server *server,
                                           const UA_NodeId *sessionId,
                                           void *sessionContext,
                                           const UA_NodeId *nodeId,
                                           void **nodeContext);

/* Internal Python type used as a done-callback on asyncio Tasks created for
 * async method callbacks.  Must be initialized via Server_initTypes(). */
int Server_initTypes(void);

#endif /* PYO6_SERVER_H_ */
