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

#ifndef PYO6_SERVER_ACCESS_CONTROL_H_
#define PYO6_SERVER_ACCESS_CONTROL_H_

#include "server.h"

/* Install a Python-backed UA_AccessControl plugin on a server config. */
PyObject *PyAccessControl_install(PyServerConfig *self, PyObject *plugin);

int pyAccessControl_traverse(UA_AccessControl *ac, visitproc visit, void *arg);

/* Whether the plugin was installed by PyAccessControl_install */
UA_Boolean pyAccessControl_isPython(const UA_AccessControl *ac);

/* Wrap the authorization hooks of the installed AccessControl, whichever it
 * is, to enforce the AccessRestrictions of the nodes. Call before startup:
 * setAccessControl and setEncryption replace the whole plugin. */
void pyAccessRestrictions_wrap(PyServer *server);
#ifdef UA_ENABLE_SUBSCRIPTIONS
/* The Subscription transfer policy of the open62541 default access control.
 * A NULL or null oldSid (detached Subscription) is denied. */
UA_Boolean pyAccessControl_allowTransferSubscription(UA_Server *server,
                                                     const UA_NodeId *oldSid,
                                                     const UA_NodeId *newSid);
#endif

#endif /* PYO6_SERVER_ACCESS_CONTROL_H_ */
