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

#endif /* PYO6_SERVER_ACCESS_CONTROL_H_ */
