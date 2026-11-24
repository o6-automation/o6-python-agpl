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

#include "server_notifications.h"
#include "server.h"
#include "../module.h"
#include "../services_subscriptions.h"

#include <open62541/common.h>

/* Trampoline: open62541 calls this on every notification while the C
 * callback is installed. We dispatch into the Python server's
 * `_dispatch_notification(type, payload)` method. Errors are caught and
 * logged. The server-mutex is held by open62541 across this call. */
static void
pyServer_global_notification_callback(UA_Server *server,
                                      UA_ApplicationNotificationType type,
                                      const UA_KeyValueMap payload) {
    UA_ServerConfig *config = UA_Server_getConfig(server);
    if (!config || !config->context)
        return;
    PyServer *pyServer = (PyServer *)config->context;

    PyGILState_STATE gil = PyGILState_Ensure();

    PyObject *pyType = PyLong_FromUnsignedLongLong((unsigned long long)type);
    PyObject *pyPayload = keyValueMap_to_pydict(&payload, &pyServer->nsMapPy2UA);
    if (pyType && pyPayload) {
        PyObject *result = PyObject_CallMethod(
            (PyObject *)pyServer, "_dispatch_notification", "OO", pyType, pyPayload);
        Py_XDECREF(result);
        if (PyErr_Occurred())
            PyErr_Print();
    } else if (PyErr_Occurred()) {
        PyErr_Print();
    }
    Py_XDECREF(pyType);
    Py_XDECREF(pyPayload);

    PyGILState_Release(gil);
}

PyObject *
server_notifications_set_global_trampoline(PyServer *self, int enabled) {
    UA_Server *server = self->server;
    if (!server) {
        PyErr_SetString(PyExc_RuntimeError, "Server not initialized");
        return NULL;
    }
    UA_ServerConfig *config = UA_Server_getConfig(server);
    if (!config) {
        PyErr_SetString(PyExc_RuntimeError, "No UA_ServerConfig attached");
        return NULL;
    }
    config->globalNotificationCallback = enabled ?
        pyServer_global_notification_callback : NULL;
    Py_RETURN_NONE;
}
