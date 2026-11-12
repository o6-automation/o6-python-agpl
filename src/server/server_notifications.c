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

/* UA_ApplicationNotificationType is a 64-bit value; PyModule_AddIntConstant
 * takes a `long`, which is only 32 bits on Windows, so build the PyObject
 * ourselves instead. These constants exist so a Python test can cross-check
 * o6.server.NotificationType against the values this build actually uses. */
#define NOTIFICATION_TYPE(name) \
    {"_NOTIFICATION_" #name, UA_APPLICATIONNOTIFICATIONTYPE_##name}

static const struct {
    const char *name;
    UA_ApplicationNotificationType value;
} notificationTypeConstants[] = {
    NOTIFICATION_TYPE(LIFECYCLE_STARTED),
    NOTIFICATION_TYPE(LIFECYCLE_SHUTDOWN),
    NOTIFICATION_TYPE(LIFECYCLE_STOPPING),
    NOTIFICATION_TYPE(LIFECYCLE_STOPPED),
    NOTIFICATION_TYPE(SECURECHANNEL_OPENED),
    NOTIFICATION_TYPE(SECURECHANNEL_CLOSED),
    NOTIFICATION_TYPE(SESSION_CREATED),
    NOTIFICATION_TYPE(SESSION_ACTIVATED),
    NOTIFICATION_TYPE(SESSION_DEACTIVATED),
    NOTIFICATION_TYPE(SESSION_CLOSED),
    NOTIFICATION_TYPE(SERVICE_BEGIN),
    NOTIFICATION_TYPE(SERVICE_ASYNC),
    NOTIFICATION_TYPE(SERVICE_END),
    NOTIFICATION_TYPE(SUBSCRIPTION_CREATED),
    NOTIFICATION_TYPE(SUBSCRIPTION_MODIFIED),
    NOTIFICATION_TYPE(SUBSCRIPTION_PUBLISHINGMODE),
    NOTIFICATION_TYPE(SUBSCRIPTION_TRANSFERRED),
    NOTIFICATION_TYPE(SUBSCRIPTION_DELETED),
    NOTIFICATION_TYPE(MONITOREDITEM_CREATED),
    NOTIFICATION_TYPE(MONITOREDITEM_MODIFIED),
    NOTIFICATION_TYPE(MONITOREDITEM_MONITORINGMODE),
    NOTIFICATION_TYPE(MONITOREDITEM_DELETED),
    NOTIFICATION_TYPE(DISCOVERY_REGISTERSERVER),
    NOTIFICATION_TYPE(DISCOVERY_SERVERONNETWORK),
    NOTIFICATION_TYPE(AUDIT),
    NOTIFICATION_TYPE(AUDIT_SECURITY),
    NOTIFICATION_TYPE(AUDIT_SECURITY_CHANNEL),
    NOTIFICATION_TYPE(AUDIT_SECURITY_CHANNEL_OPEN),
    NOTIFICATION_TYPE(AUDIT_SECURITY_SESSION),
    NOTIFICATION_TYPE(AUDIT_SECURITY_SESSION_CREATE),
    NOTIFICATION_TYPE(AUDIT_SECURITY_SESSION_ACTIVATE),
    NOTIFICATION_TYPE(AUDIT_SECURITY_SESSION_CANCEL),
    NOTIFICATION_TYPE(AUDIT_SECURITY_CERTIFICATE),
    NOTIFICATION_TYPE(AUDIT_SECURITY_CERTIFICATE_DATAMISMATCH),
    NOTIFICATION_TYPE(AUDIT_SECURITY_CERTIFICATE_EXPIRED),
    NOTIFICATION_TYPE(AUDIT_SECURITY_CERTIFICATE_INVALID),
    NOTIFICATION_TYPE(AUDIT_SECURITY_CERTIFICATE_UNTRUSTED),
    NOTIFICATION_TYPE(AUDIT_SECURITY_CERTIFICATE_REVOKED),
    NOTIFICATION_TYPE(AUDIT_SECURITY_CERTIFICATE_MISMATCH),
    NOTIFICATION_TYPE(AUDIT_NODE),
    NOTIFICATION_TYPE(AUDIT_NODE_ADD),
    NOTIFICATION_TYPE(AUDIT_NODE_DELETE),
    NOTIFICATION_TYPE(AUDIT_NODE_ADDREFERENCES),
    NOTIFICATION_TYPE(AUDIT_NODE_DELETEREFERENCES),
    NOTIFICATION_TYPE(AUDIT_UPDATE),
    NOTIFICATION_TYPE(AUDIT_UPDATE_WRITE),
    NOTIFICATION_TYPE(AUDIT_UPDATE_HISTORY),
    NOTIFICATION_TYPE(AUDIT_UPDATE_METHOD),
    NOTIFICATION_TYPE(AUDIT_CLIENT),
    NOTIFICATION_TYPE(AUDIT_CLIENT_UPDATEMETHOD),
};

#undef NOTIFICATION_TYPE

int
server_notifications_add_constants(PyObject *mod) {
    for (size_t i = 0;
         i < sizeof(notificationTypeConstants) / sizeof(notificationTypeConstants[0]); i++) {
        PyObject *value =
            PyLong_FromUnsignedLongLong((unsigned long long)notificationTypeConstants[i].value);
        if (!value)
            return -1;
        if (PyModule_AddObject(mod, notificationTypeConstants[i].name, value) < 0) {
            Py_DECREF(value);
            return -1;
        }
    }
    return 0;
}
