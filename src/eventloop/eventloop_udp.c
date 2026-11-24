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

#include "module.h"
#include "eventloop/eventloop_common.h"

#ifndef _WIN32
# include <arpa/inet.h>
# include <errno.h>
# include <fcntl.h>
# include <ifaddrs.h>
# include <net/if.h>
# include <netdb.h>
# include <sys/socket.h>
# include <unistd.h>
#endif

#define UDP_PARAMETERSSIZE 9
static UA_KeyValueRestriction udpParams[UDP_PARAMETERSSIZE];

typedef struct AsyncIOUDPManager AsyncIOUDPManager;
typedef struct {
    PyObject_HEAD
    int fd;
    uintptr_t connectionId;
    AsyncIOUDPManager *manager;
    UA_ConnectionManager_connectionCallback callback;
    void *application;
    void *context;
    UA_DelayedCallback closingCallback;
#ifndef _WIN32
    struct sockaddr_storage target;
    socklen_t targetLength;
#endif
} AsyncIOUDPConnection;

struct AsyncIOUDPManager {
    UA_ConnectionManager cm;
    AsyncIOUDPConnection **connections;
    size_t capacity;
    uintptr_t nextConnectionId;
};

static void
initUdpParams(void) {
    static UA_Boolean initialized = false;
    if(initialized)
        return;
    initialized = true;
    udpParams[0] = (UA_KeyValueRestriction){{0, UA_STRING_STATIC("listen")}, &UA_TYPES[UA_TYPES_BOOLEAN], false, true, false};
    udpParams[1] = (UA_KeyValueRestriction){{0, UA_STRING_STATIC("address")}, &UA_TYPES[UA_TYPES_STRING], false, true, true};
    udpParams[2] = (UA_KeyValueRestriction){{0, UA_STRING_STATIC("port")}, &UA_TYPES[UA_TYPES_UINT16], true, true, false};
    udpParams[3] = (UA_KeyValueRestriction){{0, UA_STRING_STATIC("interface")}, &UA_TYPES[UA_TYPES_STRING], false, true, false};
    udpParams[4] = (UA_KeyValueRestriction){{0, UA_STRING_STATIC("ttl")}, &UA_TYPES[UA_TYPES_UINT32], false, true, false};
    udpParams[5] = (UA_KeyValueRestriction){{0, UA_STRING_STATIC("loopback")}, &UA_TYPES[UA_TYPES_BOOLEAN], false, true, false};
    udpParams[6] = (UA_KeyValueRestriction){{0, UA_STRING_STATIC("reuse")}, &UA_TYPES[UA_TYPES_BOOLEAN], false, true, false};
    udpParams[7] = (UA_KeyValueRestriction){{0, UA_STRING_STATIC("sockpriority")}, &UA_TYPES[UA_TYPES_UINT32], false, true, false};
    udpParams[8] = (UA_KeyValueRestriction){{0, UA_STRING_STATIC("validate")}, &UA_TYPES[UA_TYPES_BOOLEAN], false, true, false};
}

static AsyncIOUDPConnection **
reserveSlot(AsyncIOUDPManager *manager) {
    for(size_t i = 0; i < manager->capacity; i++)
        if(!manager->connections[i])
            return &manager->connections[i];
    size_t oldCapacity = manager->capacity;
    size_t newCapacity = oldCapacity ? oldCapacity * 2 : 4;
    AsyncIOUDPConnection **entries = (AsyncIOUDPConnection**)UA_realloc(
        manager->connections, newCapacity * sizeof(*entries));
    if(!entries)
        return NULL;
    memset(entries + oldCapacity, 0,
           (newCapacity - oldCapacity) * sizeof(*entries));
    manager->connections = entries;
    manager->capacity = newCapacity;
    return &entries[oldCapacity];
}

static PyObject *
udpReadable(AsyncIOUDPConnection *connection, PyObject *args) {
    (void)args;
    if(!connection->manager)
        Py_RETURN_NONE;
#ifndef _WIN32
    UA_Byte buffer[65536];
    struct sockaddr_storage remote;
    socklen_t remoteLength = sizeof(remote);
    ssize_t received = recvfrom(connection->fd, buffer, sizeof(buffer), 0,
                                (struct sockaddr*)&remote, &remoteLength);
    if(received < 0) {
        if(errno == EAGAIN || errno == EWOULDBLOCK)
            Py_RETURN_NONE;
        PyErr_SetFromErrno(PyExc_OSError);
        return NULL;
    }
    char host[NI_MAXHOST], service[NI_MAXSERV];
    if(getnameinfo((struct sockaddr*)&remote, remoteLength, host, sizeof(host),
                   service, sizeof(service), NI_NUMERICHOST | NI_NUMERICSERV) != 0)
        Py_RETURN_NONE;
    UA_String address = UA_STRING(host);
    UA_UInt16 port = (UA_UInt16)strtoul(service, NULL, 10);
    UA_KeyValuePair pairs[2];
    pairs[0].key = UA_QUALIFIEDNAME(0, "remote-address");
    UA_Variant_setScalar(&pairs[0].value, &address, &UA_TYPES[UA_TYPES_STRING]);
    pairs[1].key = UA_QUALIFIEDNAME(0, "remote-port");
    UA_Variant_setScalar(&pairs[1].value, &port, &UA_TYPES[UA_TYPES_UINT16]);
    UA_KeyValueMap params = {2, pairs};
    UA_ByteString message = {(size_t)received, buffer};
    connection->callback(&connection->manager->cm, connection->connectionId,
                         connection->application, &connection->context,
                         UA_CONNECTIONSTATE_ESTABLISHED,
                         &params, message);
#endif
    Py_RETURN_NONE;
}

static PyTypeObject AsyncIOUDPConnectionType = {
    .ob_base = PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "o6._UDPConnection",
    .tp_basicsize = sizeof(AsyncIOUDPConnection),
    .tp_flags = Py_TPFLAGS_DEFAULT,
    .tp_call = (ternaryfunc)udpReadable,
    .tp_new = PyType_GenericNew,
};

#ifndef _WIN32
static UA_StatusCode
resolveAddress(const UA_String *address, UA_UInt16 port,
               struct addrinfo **result) {
    char host[512];
    if(address && address->length) {
        if(address->length >= sizeof(host))
            return UA_STATUSCODE_BADOUTOFRANGE;
        memcpy(host, address->data, address->length);
        host[address->length] = 0;
    } else {
        strcpy(host, "0.0.0.0");
    }
    char service[6];
    snprintf(service, sizeof(service), "%u", (unsigned)port);
    struct addrinfo hints;
    memset(&hints, 0, sizeof(hints));
    hints.ai_family = AF_UNSPEC;
    hints.ai_socktype = SOCK_DGRAM;
    return getaddrinfo(host, service, &hints, result) == 0 ?
        UA_STATUSCODE_GOOD : UA_STATUSCODE_BADCONNECTIONREJECTED;
}

/* Resolve only local IPv4 interface addresses. Never fall back for an explicit
 * selector: an unrelated route would publish on the wrong network. */
static UA_StatusCode
ipv4Interface(const UA_String *selector, struct in_addr *address) {
    address->s_addr = htonl(INADDR_ANY);
    if(!selector)
        return UA_STATUSCODE_GOOD;
    char name[256];
    if(!selector->length || selector->length >= sizeof(name))
        return UA_STATUSCODE_BADINVALIDARGUMENT;
    memcpy(name, selector->data, selector->length);
    name[selector->length] = 0;
    struct in_addr numeric;
    int isAddress = inet_pton(AF_INET, name, &numeric);
    struct ifaddrs *interfaces = NULL;
    if(getifaddrs(&interfaces) != 0)
        return UA_STATUSCODE_BADCONNECTIONREJECTED;
    UA_StatusCode status = UA_STATUSCODE_BADNOTFOUND;
    for(struct ifaddrs *entry = interfaces; entry; entry = entry->ifa_next) {
        if(!entry->ifa_addr || entry->ifa_addr->sa_family != AF_INET ||
           !(entry->ifa_flags & IFF_UP))
            continue;
        struct in_addr candidate = ((struct sockaddr_in*)entry->ifa_addr)->sin_addr;
        if((isAddress == 1 && candidate.s_addr == numeric.s_addr) ||
           (isAddress != 1 && strcmp(name, entry->ifa_name) == 0)) {
            *address = candidate;
            status = UA_STATUSCODE_GOOD;
            break;
        }
    }
    freeifaddrs(interfaces);
    return status;
}

static UA_Boolean
isIpv4Multicast(const struct sockaddr *address) {
    if(address->sa_family != AF_INET)
        return false;
    UA_UInt32 value = ntohl(((const struct sockaddr_in*)address)->sin_addr.s_addr);
    return IN_MULTICAST(value);
}
#endif

static UA_StatusCode
udpOpen(UA_ConnectionManager *cm, const UA_KeyValueMap *params,
        void *application, void *context,
        UA_ConnectionManager_connectionCallback callback) {
    AsyncIOUDPManager *manager = (AsyncIOUDPManager*)cm;
    AsyncIOLoop *loop = (AsyncIOLoop*)cm->eventSource.eventLoop;
    if(!loop || cm->eventSource.state != UA_EVENTSOURCESTATE_STARTED)
        return UA_STATUSCODE_BADINVALIDSTATE;
    initUdpParams();
    UA_StatusCode status = UA_KeyValueMap_validate(
        params, udpParams, UDP_PARAMETERSSIZE, false,
        loop->cLoop.logger, UA_LOGCATEGORY_EVENTLOOP, "UDP");
    if(status != UA_STATUSCODE_GOOD)
        return status;
    const UA_UInt16 *port = (const UA_UInt16*)UA_KeyValueMap_getScalar(
        params, udpParams[2].name, &UA_TYPES[UA_TYPES_UINT16]);
    const UA_String *address = (const UA_String*)UA_KeyValueMap_getScalar(
        params, udpParams[1].name, &UA_TYPES[UA_TYPES_STRING]);
    const UA_Boolean *validate = (const UA_Boolean*)UA_KeyValueMap_getScalar(
        params, udpParams[8].name, &UA_TYPES[UA_TYPES_BOOLEAN]);
    const UA_Boolean *listen = (const UA_Boolean*)UA_KeyValueMap_getScalar(
        params, udpParams[0].name, &UA_TYPES[UA_TYPES_BOOLEAN]);
    if(!port)
        return UA_STATUSCODE_BADINVALIDARGUMENT;
#ifdef _WIN32
    (void)address; (void)validate; (void)listen; (void)application;
    (void)context; (void)callback; (void)manager;
    return UA_STATUSCODE_BADNOTSUPPORTED;
#else
    struct addrinfo *resolved = NULL;
    status = resolveAddress(address, *port, &resolved);
    if(status != UA_STATUSCODE_GOOD)
        return status;
    if(validate && *validate) {
        freeaddrinfo(resolved);
        return UA_STATUSCODE_GOOD;
    }
    int fd = socket(resolved->ai_family, SOCK_DGRAM, 0);
    if(fd < 0) {
        freeaddrinfo(resolved);
        return UA_STATUSCODE_BADCONNECTIONREJECTED;
    }
    int flags = fcntl(fd, F_GETFL, 0);
    if(flags < 0 || fcntl(fd, F_SETFL, flags | O_NONBLOCK) < 0) {
        close(fd); freeaddrinfo(resolved);
        return UA_STATUSCODE_BADINTERNALERROR;
    }
    const UA_Boolean *reuse = (const UA_Boolean*)UA_KeyValueMap_getScalar(
        params, udpParams[6].name, &UA_TYPES[UA_TYPES_BOOLEAN]);
    if(reuse && *reuse) {
        int enabled = 1;
        int result = setsockopt(fd, SOL_SOCKET, SO_REUSEADDR, &enabled, sizeof(enabled));
#ifdef __APPLE__
        /* Share the mDNS port with the system responder and other observers. */
        result |= setsockopt(fd, SOL_SOCKET, SO_REUSEPORT, &enabled, sizeof(enabled));
#endif
        if(result != 0) {
            close(fd); freeaddrinfo(resolved);
            return UA_STATUSCODE_BADCONNECTIONREJECTED;
        }
    }
    struct in_addr interfaceAddress = {.s_addr = htonl(INADDR_ANY)};
    if(isIpv4Multicast(resolved->ai_addr)) {
        const UA_String *selector = UA_KeyValueMap_getScalar(
            params, udpParams[3].name, &UA_TYPES[UA_TYPES_STRING]);
        status = ipv4Interface(selector, &interfaceAddress);
        const UA_UInt32 *ttl = UA_KeyValueMap_getScalar(
            params, udpParams[4].name, &UA_TYPES[UA_TYPES_UINT32]);
        const UA_Boolean *loopback = UA_KeyValueMap_getScalar(
            params, udpParams[5].name, &UA_TYPES[UA_TYPES_BOOLEAN]);
        unsigned char hops = ttl ? (unsigned char)*ttl : 1;
        unsigned char echo = loopback ? *loopback : 1;
        if(status != UA_STATUSCODE_GOOD || (ttl && *ttl > 255) ||
           setsockopt(fd, IPPROTO_IP, IP_MULTICAST_IF, &interfaceAddress, sizeof(interfaceAddress)) ||
           setsockopt(fd, IPPROTO_IP, IP_MULTICAST_TTL, &hops, sizeof(hops)) ||
           setsockopt(fd, IPPROTO_IP, IP_MULTICAST_LOOP, &echo, sizeof(echo))) {
            close(fd); freeaddrinfo(resolved);
            return status != UA_STATUSCODE_GOOD ? status : UA_STATUSCODE_BADCONNECTIONREJECTED;
        }
#ifdef IP_MULTICAST_ALL
        int all = 0;
        setsockopt(fd, IPPROTO_IP, IP_MULTICAST_ALL, &all, sizeof(all));
#endif
    }
    if(listen && *listen) {
        if(isIpv4Multicast(resolved->ai_addr)) {
            struct sockaddr_in local = *(struct sockaddr_in*)resolved->ai_addr;
            local.sin_addr.s_addr = htonl(INADDR_ANY);
            if(bind(fd, (struct sockaddr*)&local, sizeof(local)) != 0) {
                close(fd); freeaddrinfo(resolved);
                return UA_STATUSCODE_BADCONNECTIONREJECTED;
            }
            struct ip_mreq membership = {
                .imr_multiaddr = ((struct sockaddr_in*)resolved->ai_addr)->sin_addr,
                .imr_interface = interfaceAddress,
            };
            if(setsockopt(fd, IPPROTO_IP, IP_ADD_MEMBERSHIP,
                          &membership, sizeof(membership)) != 0) {
                close(fd); freeaddrinfo(resolved);
                return UA_STATUSCODE_BADCONNECTIONREJECTED;
            }
        } else if(bind(fd, resolved->ai_addr, resolved->ai_addrlen) != 0) {
            close(fd); freeaddrinfo(resolved);
            return UA_STATUSCODE_BADCONNECTIONREJECTED;
        }
    }
    AsyncIOUDPConnection **slot = reserveSlot(manager);
    if(!slot) {
        close(fd); freeaddrinfo(resolved);
        return UA_STATUSCODE_BADOUTOFMEMORY;
    }
    AsyncIOUDPConnection *connection = (AsyncIOUDPConnection*)
        AsyncIOUDPConnectionType.tp_new(&AsyncIOUDPConnectionType, NULL, NULL);
    if(!connection) {
        close(fd); freeaddrinfo(resolved);
        return UA_STATUSCODE_BADOUTOFMEMORY;
    }
    connection->fd = fd;
    connection->connectionId = manager->nextConnectionId++;
    connection->manager = manager;
    connection->callback = callback;
    connection->application = application;
    connection->context = context;
    memcpy(&connection->target, resolved->ai_addr, resolved->ai_addrlen);
    connection->targetLength = (socklen_t)resolved->ai_addrlen;
    freeaddrinfo(resolved);
    *slot = connection;
    if(listen && *listen) {
        PyObject *registered = PyObject_CallMethod(
            loop->pyLoop, "add_reader", "iO", fd, connection);
        if(!registered) {
            *slot = NULL; close(fd); Py_DECREF(connection); PyErr_Clear();
            return UA_STATUSCODE_BADINTERNALERROR;
        }
        Py_DECREF(registered);
    }
    callback(cm, connection->connectionId, application, &connection->context,
             UA_CONNECTIONSTATE_ESTABLISHED,
             &UA_KEYVALUEMAP_NULL, UA_BYTESTRING_NULL);
    return UA_STATUSCODE_GOOD;
#endif
}

static UA_StatusCode
udpSend(UA_ConnectionManager *cm, uintptr_t connectionId,
        const UA_KeyValueMap *params, UA_ByteString *buffer) {
    (void)params;
    AsyncIOUDPManager *manager = (AsyncIOUDPManager*)cm;
    for(size_t i = 0; i < manager->capacity; i++) {
        AsyncIOUDPConnection *connection = manager->connections[i];
        if(!connection || connection->connectionId != connectionId)
            continue;
#ifndef _WIN32
        ssize_t sent = sendto(connection->fd, buffer->data, buffer->length, 0,
                              (struct sockaddr*)&connection->target,
                              connection->targetLength);
        UA_StatusCode status = sent == (ssize_t)buffer->length ?
            UA_STATUSCODE_GOOD : UA_STATUSCODE_BADCOMMUNICATIONERROR;
        UA_ByteString_clear(buffer);
        return status;
#else
        UA_ByteString_clear(buffer);
        return UA_STATUSCODE_BADNOTSUPPORTED;
#endif
    }
    UA_ByteString_clear(buffer);
    return UA_STATUSCODE_BADNOTFOUND;
}

static void
udpCloseDelayed(void *application, void *context) {
    (void)context;
    AsyncIOUDPConnection *connection = (AsyncIOUDPConnection*)application;
    AsyncIOUDPManager *manager = connection->manager;
    if(manager) {
        connection->callback(&manager->cm, connection->connectionId,
                             connection->application, &connection->context,
                             UA_CONNECTIONSTATE_CLOSING,
                             &UA_KEYVALUEMAP_NULL, UA_BYTESTRING_NULL);
        connection->manager = NULL;
    }
    Py_DECREF(connection);
}

static UA_StatusCode
udpClose(UA_ConnectionManager *cm, uintptr_t connectionId) {
    AsyncIOUDPManager *manager = (AsyncIOUDPManager*)cm;
    AsyncIOLoop *loop = (AsyncIOLoop*)cm->eventSource.eventLoop;
    for(size_t i = 0; i < manager->capacity; i++) {
        AsyncIOUDPConnection *connection = manager->connections[i];
        if(!connection || connection->connectionId != connectionId)
            continue;
        manager->connections[i] = NULL;
#ifndef _WIN32
        if(!loop->tearingDown) {
            PyObject *removed = PyObject_CallMethod(
                loop->pyLoop, "remove_reader", "i", connection->fd);
            Py_XDECREF(removed);
            PyErr_Clear();
        }
        close(connection->fd);
#endif
        connection->fd = -1;
        if(loop->tearingDown) {
            connection->manager = NULL;
            Py_DECREF(connection);
        } else {
            connection->closingCallback.callback = udpCloseDelayed;
            connection->closingCallback.application = connection;
            loop->cLoop.addDelayedCallback(&loop->cLoop,
                                           &connection->closingCallback);
        }
        return UA_STATUSCODE_GOOD;
    }
    return UA_STATUSCODE_BADNOTFOUND;
}

static UA_StatusCode udpStart(UA_EventSource *source) {
    source->state = UA_EVENTSOURCESTATE_STARTED;
    return UA_STATUSCODE_GOOD;
}

static void udpStop(UA_EventSource *source) {
    AsyncIOUDPManager *manager = (AsyncIOUDPManager*)source;
    for(size_t i = 0; i < manager->capacity; i++)
        if(manager->connections[i])
            udpClose(&manager->cm, manager->connections[i]->connectionId);
    source->state = UA_EVENTSOURCESTATE_STOPPED;
}

static UA_StatusCode udpFree(UA_EventSource *source) {
    AsyncIOUDPManager *manager = (AsyncIOUDPManager*)source;
    UA_KeyValueMap_clear(&source->params);
    UA_String_clear(&source->name);
    UA_free(manager->connections);
    UA_free(manager);
    return UA_STATUSCODE_GOOD;
}

static UA_StatusCode udpAlloc(UA_ConnectionManager *cm, uintptr_t id,
                              UA_ByteString *buffer, size_t size) {
    (void)cm; (void)id;
    return UA_ByteString_allocBuffer(buffer, size);
}
static void udpRelease(UA_ConnectionManager *cm, uintptr_t id,
                       UA_ByteString *buffer) {
    (void)cm; (void)id;
    UA_ByteString_clear(buffer);
}

int AsyncIOUDP_initTypes(void) {
    if(AsyncIOUDPConnectionType.tp_flags & Py_TPFLAGS_READY)
        return 0;
    return PyType_Ready(&AsyncIOUDPConnectionType);
}

UA_ConnectionManager *
UA_ConnectionManager_new_AsyncIO_UDP(void) {
    if(AsyncIOUDP_initTypes() < 0)
        return NULL;
    AsyncIOUDPManager *manager = (AsyncIOUDPManager*)UA_calloc(1, sizeof(*manager));
    if(!manager)
        return NULL;
    manager->nextConnectionId = 1;
    UA_ConnectionManager *cm = &manager->cm;
    cm->eventSource.eventSourceType = UA_EVENTSOURCETYPE_CONNECTIONMANAGER;
    cm->eventSource.name = UA_STRING_ALLOC("udp-source");
    cm->eventSource.start = udpStart;
    cm->eventSource.stop = udpStop;
    cm->eventSource.free = udpFree;
    cm->protocol = UA_STRING((char*)(uintptr_t)"udp");
    cm->openConnection = udpOpen;
    cm->sendWithConnection = udpSend;
    cm->closeConnection = udpClose;
    cm->allocNetworkBuffer = udpAlloc;
    cm->freeNetworkBuffer = udpRelease;
    return cm;
}
