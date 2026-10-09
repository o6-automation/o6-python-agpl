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

#ifndef PYO6_SERVICES_SUBSCRIPTIONS_H_
#define PYO6_SERVICES_SUBSCRIPTIONS_H_

#include "./client/client.h"
#include "./server/server.h"
#include "./open62541_queue.h"

/* Per-monitored-item context shared between the client and server bindings.
 * Exactly one of pyClient/pyServer is set, depending on which side owns the
 * item. */
typedef struct MonitoredItemBundle {
    /* Common callback hooks */
    PyObject *notification_cb; /* required callback */
    PyObject *deleted_cb;      /* optional callback */
    PyObject *context;         /* optional callback context */

    /* Owner references (only one side is used) */
    PyClient *pyClient;        /* borrowed */
    PyServer *pyServer;        /* borrowed; server owns callback refs */

    /* Server bookkeeping fields */
    UA_UInt32 monitoredItemId;
    UA_Server *server;

    SLIST_ENTRY(MonitoredItemBundle) entry;
    LIST_ENTRY(MonitoredItemBundle) clientEntry;
} MonitoredItemBundle;

SLIST_HEAD(MonitoredItemBundleList, MonitoredItemBundle);

MonitoredItemBundle *
monitoredItemBundle_new(PyClient *pyClient,
                        PyServer *pyServer,
                        UA_Server *server,
                        PyObject *notification_cb,
                        PyObject *context,
                        PyObject *deleted_cb);

void
monitoredItemBundle_free(MonitoredItemBundle *bundle);

/* Shared converter used by client/server event monitored-item callbacks. */
PyObject *
keyValueMap_to_pydict(const UA_KeyValueMap *payload,
                      const UA_NamespaceMapping *nsMapping);

/* Shared server-side monitored-item list helpers. */
void
monitoredItemBundle_remove_from_list(struct MonitoredItemBundleList *list,
                                     UA_UInt32 id,
                                     UA_Server *server);

void
monitoredItemBundle_clear_server_from_list(struct MonitoredItemBundleList *list,
                                           UA_Server *server);

/* Shared result handling for server callbacks; prints errors and schedules
 * coroutine results on the server event loop when available. */
void
handleServerCallbackResult(UA_Server *server, PyObject *result);

/* Call a Python callback and print/clear errors. Does not steal references. */
void
callPyCallbackOneArg(PyObject *callback, PyObject *arg);

void
callPyCallbackTwoArgs(PyObject *callback, PyObject *arg1, PyObject *arg2);

#endif /* PYO6_SERVICES_SUBSCRIPTIONS_H_ */
