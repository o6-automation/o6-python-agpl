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

#ifndef PYO6_SERVER_NOTIFICATIONS_H_
#define PYO6_SERVER_NOTIFICATIONS_H_

#include "../module.h"
#include "server.h"
#include <open62541/server.h>

/* Install / remove the global notification trampoline on a PyServer's
 * UA_ServerConfig. The Python server keeps the per-category handler lists;
 * this function only flips the C callback pointer. */
PyObject *
server_notifications_set_global_trampoline(PyServer *self, int enabled);

/* Expose the raw UA_APPLICATIONNOTIFICATIONTYPE_LIFECYCLE_* values on *mod*
 * as private (leading-underscore) int constants, so a test can cross-check
 * o6.server.NotificationType's Python-side literals against the values the
 * compiled open62541 actually uses. Returns -1 with a Python exception set
 * on failure, 0 on success. */
int
server_notifications_add_constants(PyObject *mod);

#endif /* PYO6_SERVER_NOTIFICATIONS_H_ */
