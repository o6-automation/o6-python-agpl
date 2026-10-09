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

#include "server_services_util.h"
#include "../module.h"
#include "../types_internal.h"

int
extract_nodeid(PyObject *obj, UA_NodeId *out,
               const UA_NamespaceMapping *nsMapping,
               const UA_DataTypeArray *customDataTypes) {
    UA_NodeId_init(out);
    PyObject *res = PY2UA(obj, out, &UA_TYPES[UA_TYPES_NODEID], nsMapping, customDataTypes);
    if (!res)
        return -1;
    return 0;
}

int
extract_qualifiedname(PyObject *obj, UA_QualifiedName *out,
                      const UA_NamespaceMapping *nsMapping,
                      const UA_DataTypeArray *customDataTypes) {
    UA_QualifiedName_init(out);
    PyObject *res = PY2UA(obj, out, &UA_TYPES[UA_TYPES_QUALIFIEDNAME], nsMapping, customDataTypes);
    if (!res)
        return -1;
    return 0;
}

PyObject *
pyServer_invoke_sync_callback(PyObject *callback, PyObject *args, PyObject *kwargs) {
    PyObject *module = PyImport_ImportModule("o6._dispatch");
    PyObject *invoke = module ? PyObject_GetAttrString(module, "invoke_sync") : NULL;
    Py_XDECREF(module);
    PyObject *result = invoke ? PyObject_CallFunctionObjArgs(
        invoke, callback, args, kwargs ? kwargs : Py_None, NULL) : NULL;
    Py_XDECREF(invoke);
    return result;
}
