/* Copyright (c) 2026 o6 Automation GmbH
 *
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

#include "server.h"
#include "../types_internal.h"
#include "../module.h"
#include <open62541/types.h>
#include <open62541/types_generated.h>
#include <open62541/util.h>
#include <open62541/server.h>

/* Server method: link_custom_data_types(capsule)
 *
 * Same as the client version but for servers.  See client/type_registration.c
 * for the full description. */
PyObject *
linkServerCustomDataTypes(PyServer *self, PyObject *args) {
    PyObject *capsule;
    if(!PyArg_ParseTuple(args, "O", &capsule))
        return NULL;
    if(!self->server) {
        PyErr_SetString(PyExc_RuntimeError, "Server is not initialized");
        return NULL;
    }

    UA_ServerConfig *config = UA_Server_getConfig(self->server);
    PyObject *link_capsule =
        linkCustomDataTypesImpl((UA_DataTypeArray **)&config->customDataTypes, capsule);
    if(!link_capsule)
        return NULL;

    if(PyList_Append(self->linked_type_capsules, link_capsule) < 0) {
        Py_DECREF(link_capsule);
        return NULL;
    }
    Py_DECREF(link_capsule);
    Py_RETURN_NONE;
}
