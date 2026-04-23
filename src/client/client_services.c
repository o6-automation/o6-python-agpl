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
#include <open62541/client_highlevel_async.h>

PyObject *
pyClient_service_call(PyObject *self, PyObject *args) {
    return serviceCallAsync(self, args,
                            &UA_TYPES[UA_TYPES_CALLREQUEST],
                            &UA_TYPES[UA_TYPES_CALLRESPONSE]);
}

PyObject *
pyClient_service_read(PyObject *self, PyObject *args) {
    return serviceCallAsync(self, args,
                            &UA_TYPES[UA_TYPES_READREQUEST],
                            &UA_TYPES[UA_TYPES_READRESPONSE]);
}

PyObject *
pyClient_service_write(PyObject *self, PyObject *args) {
    return serviceCallAsync(self, args,
                            &UA_TYPES[UA_TYPES_WRITEREQUEST],
                            &UA_TYPES[UA_TYPES_WRITERESPONSE]);
}

PyObject *
pyClient_service_browse(PyObject *self, PyObject *args) {
    return serviceCallAsync(self, args,
                            &UA_TYPES[UA_TYPES_BROWSEREQUEST],
                            &UA_TYPES[UA_TYPES_BROWSERESPONSE]);
}

PyObject *
pyClient_service_browseNext(PyObject *self, PyObject *args) {
    return serviceCallAsync(self, args,
                            &UA_TYPES[UA_TYPES_BROWSENEXTREQUEST],
                            &UA_TYPES[UA_TYPES_BROWSENEXTRESPONSE]);
}

PyObject *
pyClient_service_registerNodes(PyObject *self, PyObject *args) {
    return serviceCallAsync(self, args,
                            &UA_TYPES[UA_TYPES_REGISTERNODESREQUEST],
                            &UA_TYPES[UA_TYPES_REGISTERNODESRESPONSE]);
}

PyObject *
pyClient_service_unregisterNodes(PyObject *self, PyObject *args) {
    return serviceCallAsync(self, args,
                            &UA_TYPES[UA_TYPES_UNREGISTERNODESREQUEST],
                            &UA_TYPES[UA_TYPES_UNREGISTERNODESRESPONSE]);
}

PyObject *
pyClient_service_translateBrowsePathsToNodeIds(PyObject *self, PyObject *args) {
    return serviceCallAsync(self, args,
                            &UA_TYPES[UA_TYPES_TRANSLATEBROWSEPATHSTONODEIDSREQUEST],
                            &UA_TYPES[UA_TYPES_TRANSLATEBROWSEPATHSTONODEIDSRESPONSE]);
}

PyObject *
pyClient_service_addNodes(PyObject *self, PyObject *args) {
    return serviceCallAsync(self, args,
                            &UA_TYPES[UA_TYPES_ADDNODESREQUEST],
                            &UA_TYPES[UA_TYPES_ADDNODESRESPONSE]);
}

PyObject *
pyClient_service_deleteNodes(PyObject *self, PyObject *args) {
    return serviceCallAsync(self, args,
                            &UA_TYPES[UA_TYPES_DELETENODESREQUEST],
                            &UA_TYPES[UA_TYPES_DELETENODESRESPONSE]);
}

PyObject *
pyClient_service_addReferences(PyObject *self, PyObject *args) {
    return serviceCallAsync(self, args,
                            &UA_TYPES[UA_TYPES_ADDREFERENCESREQUEST],
                            &UA_TYPES[UA_TYPES_ADDREFERENCESRESPONSE]);
}

PyObject *
pyClient_service_deleteReferences(PyObject *self, PyObject *args) {
    return serviceCallAsync(self, args,
                            &UA_TYPES[UA_TYPES_DELETEREFERENCESREQUEST],
                            &UA_TYPES[UA_TYPES_DELETEREFERENCESRESPONSE]);
}

PyObject *
pyClient_service_historyRead(PyObject *self, PyObject *args) {
    return serviceCallAsync(self, args,
                            &UA_TYPES[UA_TYPES_HISTORYREADREQUEST],
                            &UA_TYPES[UA_TYPES_HISTORYREADRESPONSE]);
}

PyObject *
pyClient_service_historyUpdate(PyObject *self, PyObject *args) {
    return serviceCallAsync(self, args,
                            &UA_TYPES[UA_TYPES_HISTORYUPDATEREQUEST],
                            &UA_TYPES[UA_TYPES_HISTORYUPDATERESPONSE]);
}

PyObject *
pyClient_service_queryFirst(PyObject *self, PyObject *args) {
    return serviceCallAsync(self, args,
                            &UA_TYPES[UA_TYPES_QUERYFIRSTREQUEST],
                            &UA_TYPES[UA_TYPES_QUERYFIRSTRESPONSE]);
}

PyObject *
pyClient_service_queryNext(PyObject *self, PyObject *args) {
    return serviceCallAsync(self, args,
                            &UA_TYPES[UA_TYPES_QUERYNEXTREQUEST],
                            &UA_TYPES[UA_TYPES_QUERYNEXTRESPONSE]);
}

/* Discovery */

PyObject *
pyClient_get_endpoints(PyObject *self, PyObject *args) {
    return serviceCallAsync(self, args,
                            &UA_TYPES[UA_TYPES_GETENDPOINTSREQUEST],
                            &UA_TYPES[UA_TYPES_GETENDPOINTSRESPONSE]);
}

PyObject *
pyClient_find_servers(PyObject *self, PyObject *args) {
    return serviceCallAsync(self, args,
                            &UA_TYPES[UA_TYPES_FINDSERVERSREQUEST],
                            &UA_TYPES[UA_TYPES_FINDSERVERSRESPONSE]);
}

PyObject *
pyClient_find_servers_on_network(PyObject *self, PyObject *args) {
    return serviceCallAsync(self, args,
                            &UA_TYPES[UA_TYPES_FINDSERVERSONNETWORKREQUEST],
                            &UA_TYPES[UA_TYPES_FINDSERVERSONNETWORKRESPONSE]);
}

