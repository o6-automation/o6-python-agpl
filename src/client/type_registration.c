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

#include "client.h"
#include "../types_internal.h"
#include "../module.h"
#include <open62541/types.h>
#include <open62541/types_generated.h>
#include <open62541/util.h>
#include <open62541/client.h>

/* Client method: link_custom_data_types(capsule)
 *
 * Takes a capsule returned by _o6.build_custom_data_types() and links the
 * pre-built UA_DataType array into this client's config.  The link capsule is
 * kept alive inside the client object so the thin wrapper survives until the
 * client is destroyed.
 *
 * Returns None on success. */
PyObject *
linkClientCustomDataTypes(PyClient *self, PyObject *args) {
    PyObject *capsule;
    if(!PyArg_ParseTuple(args, "O", &capsule))
        return NULL;
    if(!self->client) {
        PyErr_SetString(PyExc_RuntimeError, "Client is not initialized");
        return NULL;
    }

    UA_ClientConfig *config = UA_Client_getConfig(self->client);
    PyObject *link_capsule =
        linkCustomDataTypesImpl((UA_DataTypeArray **)&config->customDataTypes, capsule);
    if(!link_capsule)
        return NULL;

    if(PyList_Append(self->linked_type_capsules, link_capsule) < 0) {
        Py_DECREF(link_capsule);
        return NULL;
    }
    Py_DECREF(link_capsule); /* list holds the reference */
    Py_RETURN_NONE;
}

PyObject *
getCustomDataTypes(PyClient *self, PyObject *Py_UNUSED(args)) {
    if(!self->client) {
        PyErr_SetString(PyExc_RuntimeError, "Client is not initialized");
        return NULL;
    }

    UA_ClientConfig *config = UA_Client_getConfig(self->client);
    PyObject *types_list = PyList_New(0);
    if(!types_list)
        return NULL;

    const UA_DataTypeArray *current = config->customDataTypes;
    while(current) {
        for(size_t i = 0; i < current->typesSize; i++) {
            const UA_DataType *type = &current->types[i];

            PyObject *type_dict = PyDict_New();
            if(!type_dict) {
                Py_DECREF(types_list);
                return NULL;
            }

            PyObject *type_id = UA2PY((void*)&type->typeId,
                                      &UA_TYPES[UA_TYPES_NODEID]);
            if(type_id) {
                PyDict_SetItemString(type_dict, "typeId", type_id);
                Py_DECREF(type_id);
            }

            PyObject *bin_id = UA2PY((void*)&type->binaryEncodingId,
                                     &UA_TYPES[UA_TYPES_NODEID]);
            if(bin_id) {
                PyDict_SetItemString(type_dict, "binaryEncodingId", bin_id);
                Py_DECREF(bin_id);
            }

            PyDict_SetItemString(type_dict, "memSize",
                                 PyLong_FromSize_t(type->memSize));
            PyDict_SetItemString(type_dict, "typeKind",
                                 PyLong_FromLong(type->typeKind));
            PyDict_SetItemString(type_dict, "membersSize",
                                 PyLong_FromSize_t(type->membersSize));
            PyDict_SetItemString(type_dict, "typeName",
                                 PyUnicode_FromString(
                                     type->typeName ? type->typeName : "Unknown"));

            if(PyList_Append(types_list, type_dict) < 0) {
                Py_DECREF(type_dict);
                Py_DECREF(types_list);
                return NULL;
            }
            Py_DECREF(type_dict);
        }
        current = current->next;
    }

    return types_list;
}
