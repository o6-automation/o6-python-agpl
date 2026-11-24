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

#include "server.h"
#include "../utils.h"
#include <open62541/driver/mdns.h>
#include "server/ua_server_internal.h"
#include <errno.h>
#include <time.h>
#ifdef _WIN32
# include <windows.h>
#endif

#ifdef UA_ENABLE_DRIVER_MDNS_MDNSD
#define O6_MDNS

typedef struct {
    UA_String hostname;
    UA_String address;
    UA_Boolean ipv6;
} MdnsAddress;

typedef struct {
    UA_MdnsDriver *driver; /* Owned by the server while attached. */
    size_t addressesSize;
    MdnsAddress *addresses;
    UA_UInt32 ttl;
    UA_Boolean announce;
    UA_Boolean announceRegistered;
} PyMdns;

static void
clearMdns(PyMdns *md) {
    if(!md)
        return;
    for(size_t i = 0; i < md->addressesSize; i++) {
        UA_String_clear(&md->addresses[i].hostname);
        UA_String_clear(&md->addresses[i].address);
    }
    UA_free(md->addresses);
    UA_free(md);
}

static int
configParam(PyServer *server, PyObject *config, const char *attr, const char *key,
            const UA_DataType *type, UA_KeyValueMap *params) {
    PyObject *value = PyObject_GetAttrString(config, attr);
    if(!value)
        return -1;
    if(value == Py_None) {
        Py_DECREF(value);
        return 0;
    }
    void *native = UA_new(type);
    if(!native) {
        Py_DECREF(value);
        PyErr_NoMemory();
        return -1;
    }
    int ok = PY2UA(value, native, type, &server->nsMapPy2UA, NULL) != NULL;
    Py_DECREF(value);
    UA_StatusCode status = UA_STATUSCODE_GOOD;
    if(ok)
        status = UA_KeyValueMap_setScalar(params, UA_QUALIFIEDNAME(0, (char*)key), native, type);
    UA_delete(native, type);
    if(!ok)
        return -1;
    if(status != UA_STATUSCODE_GOOD) {
        PyErr_StatusCode(status);
        return -1;
    }
    return 0;
}

static int
copyAddresses(PyServer *server, PyObject *config, PyMdns *md) {
    PyObject *mapping = PyObject_GetAttrString(config, "hostAddresses");
    if(!mapping)
        return -1;
    PyObject *items = PyMapping_Items(mapping);
    Py_DECREF(mapping);
    if(!items)
        return -1;
    for(Py_ssize_t i = 0; i < PyList_GET_SIZE(items); i++) {
        PyObject *pair = PyList_GET_ITEM(items, i);
        PyObject *addresses = PySequence_Fast(PyTuple_GET_ITEM(pair, 1), "address sequence required");
        if(!addresses) {
            Py_DECREF(items);
            return -1;
        }
        for(Py_ssize_t j = 0; j < PySequence_Fast_GET_SIZE(addresses); j++) {
            MdnsAddress *newAddresses = UA_realloc(md->addresses,
                (md->addressesSize + 1) * sizeof(MdnsAddress));
            if(!newAddresses) {
                Py_DECREF(addresses);
                Py_DECREF(items);
                PyErr_NoMemory();
                return -1;
            }
            md->addresses = newAddresses;
            MdnsAddress *entry = &md->addresses[md->addressesSize++];
            memset(entry, 0, sizeof(*entry));
            if(!PY2UA(PyTuple_GET_ITEM(pair, 0), &entry->hostname,
                      &UA_TYPES[UA_TYPES_STRING], &server->nsMapPy2UA, NULL) ||
               !PY2UA(PySequence_Fast_GET_ITEM(addresses, j), &entry->address,
                      &UA_TYPES[UA_TYPES_STRING], &server->nsMapPy2UA, NULL)) {
                Py_DECREF(addresses);
                Py_DECREF(items);
                return -1;
            }
            entry->ipv6 = memchr(entry->address.data, ':', entry->address.length) != NULL;
        }
        Py_DECREF(addresses);
    }
    Py_DECREF(items);
    return 0;
}

static size_t
findMdnsRecord(const PyServer *server, const UA_String *name) {
    size_t i = 0;
    while(i < server->mdnsRecordsSize &&
          !UA_String_equal(&server->mdnsRecords[i].serverName, name))
        i++;
    return i;
}

static const UA_ServerOnNetwork *
findServerOnNetwork(UA_Server *server, const UA_String *name) {
    for(size_t i = 0; i < server->serversOnNetworkSize; i++) {
        if(UA_String_equal(&server->serversOnNetwork[i].serverName, name))
            return &server->serversOnNetwork[i];
    }
    return NULL;
}

static void
removeMdnsRecord(PyServer *server, size_t i) {
    UA_ServerOnNetwork_clear(&server->mdnsRecords[i]);
    server->mdnsRecords[i] = server->mdnsRecords[--server->mdnsRecordsSize];
    if(server->mdnsRecordsSize == 0) {
        UA_free(server->mdnsRecords);
        server->mdnsRecords = NULL;
    }
}

/* open62541 gives a registration a ServerOnNetwork entry, named by its
 * mdnsServerName, only if it has an opc.tcp DiscoveryUrl. Mirrors the static
 * getTcpDiscoveryUrl and isRegisteredServerOnNetwork of open62541's
 * ua_services_discovery.c; recheck them when updating open62541. */
static UA_Boolean
hasServerOnNetwork(const RegisteredServerRecord *rs) {
    const UA_RegisteredServer *registered = &rs->registeredServer;
    for(size_t i = 0; i < registered->discoveryUrlsSize; i++) {
        const UA_String *url = &registered->discoveryUrls[i];
        if(url->length >= 10 && memcmp(url->data, "opc.tcp://", 10) == 0)
            return true;
    }
    return false;
}

static UA_Boolean
isRegistrationEntry(UA_Server *server, const UA_String *name) {
    RegisteredServerRecord *rs;
    LIST_FOREACH(rs, &server->registeredServers, pointers) {
        if(hasServerOnNetwork(rs) && UA_String_equal(&rs->mdnsServerName, name))
            return true;
    }
    return false;
}

/* Hands the entry to the driver as the server does when an announced entry is
 * added. The driver announces it unless it has the same entry announced. The
 * server's own notification would also reach the application handlers. */
static void
announceEntry(PyMdns *md, const UA_ServerOnNetwork *son) {
    UA_Boolean yes = true;
    UA_KeyValuePair kvp[3];
    kvp[0].key = UA_QUALIFIEDNAME(0, "server-on-network");
    UA_Variant_setScalar(&kvp[0].value, (void*)(uintptr_t)son,
                         &UA_TYPES[UA_TYPES_SERVERONNETWORK]);
    kvp[1].key = UA_QUALIFIEDNAME(0, "announce");
    UA_Variant_setScalar(&kvp[1].value, &yes, &UA_TYPES[UA_TYPES_BOOLEAN]);
    kvp[2].key = UA_QUALIFIEDNAME(0, "server-added");
    UA_Variant_setScalar(&kvp[2].value, &yes, &UA_TYPES[UA_TYPES_BOOLEAN]);
    UA_KeyValueMap payload = {3, kvp};
    md->driver->drv.notificationCallback(&md->driver->drv,
                                         UA_APPLICATIONNOTIFICATIONTYPE_DISCOVERY_SERVERONNETWORK,
                                         payload);
}

/* The driver announces entries only while it is started and forgets them when
 * it starts again. Announces the entries it should announce after a start:
 * the records of registerServerOnNetwork() and, if configured, the entries of
 * the registrations. */
static void
announceEntries(PyServer *server, PyMdns *md) {
    UA_Server *ua = server->server;
    lockServer(ua);
    /* The driver of a listening server registers received entries without
     * o6. Such an entry, like a registration's, replaces the record, which
     * then is no longer this server's to announce. */
    for(size_t i = server->mdnsRecordsSize; i-- > 0;) {
        UA_ServerOnNetwork *record = &server->mdnsRecords[i];
        const UA_ServerOnNetwork *son = findServerOnNetwork(ua, &record->serverName);
        if(son) {
            record->recordId = son->recordId; /* Not part of the comparison */
            if(UA_order(record, son, &UA_TYPES[UA_TYPES_SERVERONNETWORK]) != UA_ORDER_EQ)
                son = NULL;
        }
        if(!son || isRegistrationEntry(ua, &record->serverName))
            removeMdnsRecord(server, i);
        else if(md->announce)
            announceEntry(md, son);
    }
    if(md->announceRegistered) {
        RegisteredServerRecord *rs;
        LIST_FOREACH(rs, &ua->registeredServers, pointers) {
            const UA_ServerOnNetwork *son = hasServerOnNetwork(rs) ?
                findServerOnNetwork(ua, &rs->mdnsServerName) : NULL;
            if(son)
                announceEntry(md, son);
        }
    }
    unlockServer(ua);
}
#endif

/* Tracks the record of registerServerOnNetwork() for announcing it after a
 * start, or drops a removed or received record (`local` NULL). A record added
 * while mDNS does not announce was not checked for an announceable URL and is
 * dropped as well. Without memory the record is only not announced again after
 * a restart, so the registration stays successful. */
void
pyMdns_recordChanged(PyServer *server, const UA_String *name,
                     const UA_ServerOnNetwork *local) {
#ifdef O6_MDNS
    PyMdns *md = server->mdnsData;
    lockServer(server->server);
    size_t i = findMdnsRecord(server, name);
    if(i < server->mdnsRecordsSize)
        removeMdnsRecord(server, i);
    if(local && md && md->announce)
        UA_Array_appendCopy((void**)&server->mdnsRecords, &server->mdnsRecordsSize,
                            local, &UA_TYPES[UA_TYPES_SERVERONNETWORK]);
    unlockServer(server->server);
#else
    (void)server;
    (void)name;
    (void)local;
#endif
}

PyObject *
pyServer_set_mdns(PyObject *self, PyObject *config) {
    O6_REQUIRE_LOOP_THREAD(pyServer_eventLoop((PyServer *)self), NULL);
    PyServer *server = (PyServer*)self;
    if(server->running || UA_Server_getLifecycleState(server->server) != UA_LIFECYCLESTATE_STOPPED) {
        PyErr_SetString(PyExc_RuntimeError, "mDNS configuration requires a stopped server");
        return NULL;
    }
#ifndef O6_MDNS
    if(config != Py_None) {
        PyErr_SetString(PyExc_NotImplementedError, "This build has no bundled mDNSd support");
        return NULL;
    }
#else
    PyMdns *next = NULL;
    UA_StatusCode status = UA_STATUSCODE_GOOD;
    if(config != Py_None) {
        next = UA_calloc(1, sizeof(PyMdns));
        if(!next)
            return PyErr_NoMemory();
        UA_KeyValueMap params = UA_KEYVALUEMAP_NULL;
        int failed =
            configParam(server, config, "listen", "listen", &UA_TYPES[UA_TYPES_BOOLEAN], &params) < 0 ||
            configParam(server, config, "announce", "announce", &UA_TYPES[UA_TYPES_BOOLEAN], &params) < 0 ||
            configParam(server, config, "interface", "interface", &UA_TYPES[UA_TYPES_STRING], &params) < 0 ||
            configParam(server, config, "announceTtl", "announce-ttl", &UA_TYPES[UA_TYPES_UINT32], &params) < 0 ||
            configParam(server, config, "queryPresence", "query-presence", &UA_TYPES[UA_TYPES_BOOLEAN], &params) < 0 ||
            configParam(server, config, "queryDetails", "query-details", &UA_TYPES[UA_TYPES_BOOLEAN], &params) < 0 ||
            configParam(server, config, "queryInterval", "query-interval", &UA_TYPES[UA_TYPES_UINT32], &params) < 0;
        if(!failed) {
            next->ttl = *(const UA_UInt32*)UA_KeyValueMap_getScalar(
                &params, UA_QUALIFIEDNAME(0, "announce-ttl"), &UA_TYPES[UA_TYPES_UINT32]);
            failed = copyAddresses(server, config, next) < 0;
        }
        if(!failed) {
            PyObject *announceRegistered = PyObject_GetAttrString(config, "announceRegisteredServers");
            if(!announceRegistered)
                failed = true;
            else {
                next->announceRegistered = PyObject_IsTrue(announceRegistered);
                Py_DECREF(announceRegistered);
                const UA_Boolean *announce = UA_KeyValueMap_getScalar(
                    &params, UA_QUALIFIEDNAME(0, "announce"), &UA_TYPES[UA_TYPES_BOOLEAN]);
                next->announce = announce && *announce;
                if(next->announceRegistered && (!announce || !*announce ||
                   UA_Server_getConfig(server->server)->applicationDescription.applicationType !=
                   UA_APPLICATIONTYPE_DISCOVERYSERVER)) {
                    PyErr_SetString(PyExc_ValueError,
                                    "Registration announcements require announce=True and an LDS");
                    failed = true;
                }
            }
        }
        if(!failed) {
            next->driver = UA_MdnsDriver_Mdnsd(params);
            if(!next->driver) {
                PyErr_NoMemory();
                failed = true;
            }
        }
        UA_KeyValueMap_clear(&params);
        if(failed) {
            clearMdns(next);
            return NULL;
        }
        status = UA_Server_addDriver(server->server, &next->driver->drv);
        if(status != UA_STATUSCODE_GOOD) {
            next->driver->drv.free(&next->driver->drv);
            clearMdns(next);
            return PyErr_StatusCode(status);
        }
    }
    PyMdns *old = server->mdnsData;
    if(old) {
        status = UA_Server_removeDriver(server->server, &old->driver->drv);
        if(status != UA_STATUSCODE_GOOD) {
            if(next) {
                UA_Server_removeDriver(server->server, &next->driver->drv);
                next->driver->drv.free(&next->driver->drv);
                clearMdns(next);
            }
            return PyErr_StatusCode(status);
        }
        old->driver->drv.free(&old->driver->drv);
        clearMdns(old);
    }
    server->mdnsData = next;
    if(next) {
        UA_ServerConfig *sc = UA_Server_getConfig(server->server);
        sc->serversOnNetworkEnabled = true;
        /* The server creates the ServerOnNetwork entries of registered
         * servers itself; the flag only selects whether the driver announces
         * them. */
        sc->announceRegisteredServers = next->announceRegistered;
    }
#endif
    Py_RETURN_NONE;
}

UA_StatusCode
pyMdns_started(PyServer *server) {
#ifdef O6_MDNS
    PyMdns *md = server->mdnsData;
    if(md) {
        if(md->announceRegistered &&
           UA_Server_getConfig(server->server)->applicationDescription.applicationType !=
           UA_APPLICATIONTYPE_DISCOVERYSERVER)
            return UA_STATUSCODE_BADINVALIDARGUMENT;
        /* The base server does not propagate driver startup failures. */
        if(md->driver->drv.state != UA_LIFECYCLESTATE_STARTED)
            return UA_STATUSCODE_BADINTERNALERROR;
        for(size_t i = 0; i < md->addressesSize; i++) {
            MdnsAddress *entry = &md->addresses[i];
            UA_StatusCode status = entry->ipv6 ?
                md->driver->addAAAARecord(md->driver, entry->hostname, entry->address, md->ttl) :
                md->driver->addARecord(md->driver, entry->hostname, entry->address, md->ttl);
            if(status != UA_STATUSCODE_GOOD)
                return status;
        }
        announceEntries(server, md);
    }
#endif
    return UA_STATUSCODE_GOOD;
}

void
pyMdns_stop(PyServer *server) {
#ifdef O6_MDNS
    PyMdns *md = server->mdnsData;
    if(md && md->driver->drv.state == UA_LIFECYCLESTATE_STARTED) {
        for(size_t i = 0; i < md->addressesSize; i++) {
            MdnsAddress *entry = &md->addresses[i];
            if(entry->ipv6)
                md->driver->removeAAAARecord(md->driver, entry->hostname, entry->address);
            else
                md->driver->removeARecord(md->driver, entry->hostname, entry->address);
        }
        /* libmdnsd queues the goodbyes of shared records (address and
         * PTR/SRV/TXT records once announced) until a single deadline at most
         * 119 us after its last send or receive, and every new goodbye resets
         * that deadline. The flush after each removal can come too early, and
         * so can the flush in the driver stop right after its service
         * retraction, which then closes the sockets with the goodbyes still
         * queued. Waiting 1 ms after the last flush puts the deadline that the
         * driver stop sets in the past, so its own flush sends every queued
         * address and service goodbye before the sockets close. The deadline
         * is wall-clock time; only a backward clock step during the wait can
         * leave goodbyes queued. */
#ifdef _WIN32
        Sleep(1);
#else
        struct timespec delay = {0, 1000000};
        while(nanosleep(&delay, &delay) != 0 && errno == EINTR) {}
#endif
        md->driver->drv.stop(&md->driver->drv);
    }
#endif
}

void
pyMdns_clear(PyServer *server) {
#ifdef O6_MDNS
    clearMdns(server->mdnsData);
#endif
    server->mdnsData = NULL;
    UA_Array_delete(server->mdnsRecords, server->mdnsRecordsSize,
                    &UA_TYPES[UA_TYPES_SERVERONNETWORK]);
    server->mdnsRecords = NULL;
    server->mdnsRecordsSize = 0;
}
