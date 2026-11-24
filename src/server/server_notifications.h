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

#endif /* PYO6_SERVER_NOTIFICATIONS_H_ */
