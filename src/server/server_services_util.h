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

#ifndef PYO6_SERVER_SERVICES_UTIL_H_
#define PYO6_SERVER_SERVICES_UTIL_H_

#include "server.h"

/*
 * Helper: Extract a UA_NodeId from a Python object.
 * Converts via PY2UA and applies the optional server namespace mapping.
 * Caller must clear the NodeId.
 */
int
extract_nodeid(PyObject *obj, UA_NodeId *out,
               const UA_NamespaceMapping *nsMapping,
               const UA_DataTypeArray *customDataTypes);

/*
 * Helper: Extract a UA_QualifiedName from a Python object.
 * Converts via PY2UA and applies the optional server namespace mapping.
 * Caller must clear the QualifiedName.
 */
int
extract_qualifiedname(PyObject *obj, UA_QualifiedName *out,
                      const UA_NamespaceMapping *nsMapping,
                      const UA_DataTypeArray *customDataTypes);

/* Invoke a Python hook in a synchronous callback scope. Borrowed arguments;
 * returns a new reference, or NULL with the callback exception set. */
PyObject *
pyServer_invoke_sync_callback(PyObject *callback, PyObject *args, PyObject *kwargs);

#endif /* PYO6_SERVER_SERVICES_UTIL_H_ */
