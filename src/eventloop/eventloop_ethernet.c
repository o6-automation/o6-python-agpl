/* Copyright 2026 (c) o6 Automation GmbH */
#include "module.h"
#include "eventloop/eventloop_common.h"

#if defined(__linux__)

# include <arpa/inet.h>
# include <errno.h>
# include <fcntl.h>
# include <linux/if_ether.h>
# include <linux/if_packet.h>
# include <net/if.h>
# include <stdio.h>
# include <sys/ioctl.h>
# include <sys/socket.h>
# include <unistd.h>

#define ETH_PARAMETERSSIZE 15
#define ETH_MAX_HEADER (2 * ETH_ALEN + 4 + 2)

static UA_KeyValueRestriction ethParams[ETH_PARAMETERSSIZE];

typedef struct AsyncIOEthernetManager AsyncIOEthernetManager;

typedef struct {
    PyObject_HEAD
    int fd;
    uintptr_t connectionId;
    AsyncIOEthernetManager *manager;
    UA_ConnectionManager_connectionCallback callback;
    void *application;
    void *context;
    UA_DelayedCallback closingCallback;
    struct sockaddr_ll target;
    UA_Byte header[ETH_MAX_HEADER];
    UA_Byte headerSize;
    UA_Byte lengthOffset;
    UA_Boolean listening;
} AsyncIOEthernetConnection;

struct AsyncIOEthernetManager {
    UA_ConnectionManager cm;
    AsyncIOEthernetConnection **connections;
    size_t capacity;
    uintptr_t nextConnectionId;
};

static void
initEthParams(void) {
    static UA_Boolean initialized = false;
    if(initialized)
        return;
    initialized = true;
#define PARAM(INDEX, NAME, TYPE, REQUIRED)                                  \
    ethParams[INDEX] = (UA_KeyValueRestriction){                            \
        {0, UA_STRING_STATIC(NAME)}, &UA_TYPES[UA_TYPES_##TYPE],            \
        REQUIRED, true, false}
    PARAM(0, "address", STRING, false);
    PARAM(1, "listen", BOOLEAN, false);
    PARAM(2, "interface", STRING, true);
    PARAM(3, "ethertype", UINT16, false);
    PARAM(4, "vid", UINT16, false);
    PARAM(5, "pcp", BYTE, false);
    PARAM(6, "dei", BOOLEAN, false);
    PARAM(7, "promiscuous", BOOLEAN, false);
    PARAM(8, "priority", UINT32, false);
    PARAM(9, "txtime-enable", BOOLEAN, false);
    PARAM(10, "txtime-flags", UINT32, false);
    PARAM(11, "txtime", DATETIME, false);
    PARAM(12, "txtime-pico", UINT16, false);
    PARAM(13, "txtime-drop-late", BOOLEAN, false);
    PARAM(14, "validate", BOOLEAN, false);
#undef PARAM
}

static AsyncIOEthernetConnection **
reserveSlot(AsyncIOEthernetManager *manager) {
    for(size_t i = 0; i < manager->capacity; i++)
        if(!manager->connections[i])
            return &manager->connections[i];
    size_t oldCapacity = manager->capacity;
    size_t newCapacity = oldCapacity ? oldCapacity * 2 : 4;
    AsyncIOEthernetConnection **entries = (AsyncIOEthernetConnection**)UA_realloc(
        manager->connections, newCapacity * sizeof(*entries));
    if(!entries)
        return NULL;
    memset(entries + oldCapacity, 0,
           (newCapacity - oldCapacity) * sizeof(*entries));
    manager->connections = entries;
    manager->capacity = newCapacity;
    return &entries[oldCapacity];
}

static AsyncIOEthernetConnection *
findConnection(AsyncIOEthernetManager *manager, uintptr_t id) {
    for(size_t i = 0; i < manager->capacity; i++) {
        AsyncIOEthernetConnection *connection = manager->connections[i];
        if(connection && connection->connectionId == id)
            return connection;
    }
    return NULL;
}

static UA_StatusCode
parseMac(const UA_String *text, UA_Byte out[ETH_ALEN]) {
    if(!text || text->length != 17)
        return UA_STATUSCODE_BADINVALIDARGUMENT;
    char value[18];
    memcpy(value, text->data, 17);
    value[17] = 0;
    unsigned int octets[ETH_ALEN];
    if(sscanf(value, "%x-%x-%x-%x-%x-%x",
              &octets[0], &octets[1], &octets[2],
              &octets[3], &octets[4], &octets[5]) != ETH_ALEN)
        return UA_STATUSCODE_BADINVALIDARGUMENT;
    for(size_t i = 0; i < ETH_ALEN; i++) {
        if(octets[i] > 0xff)
            return UA_STATUSCODE_BADINVALIDARGUMENT;
        out[i] = (UA_Byte)octets[i];
    }
    return UA_STATUSCODE_GOOD;
}

static UA_Byte
makeHeader(UA_Byte *header, const UA_Byte destination[ETH_ALEN],
           const UA_Byte source[ETH_ALEN], UA_UInt16 etherType,
           UA_UInt16 vid, UA_Byte pcp, UA_Boolean dei,
           UA_Byte *lengthOffset) {
    size_t position = 0;
    memcpy(header + position, destination, ETH_ALEN);
    position += ETH_ALEN;
    memcpy(header + position, source, ETH_ALEN);
    position += ETH_ALEN;
    if(vid > 0 && vid != ETH_P_ALL) {
        UA_UInt16 tag = htons(0x8100);
        memcpy(header + position, &tag, sizeof(tag));
        position += sizeof(tag);
        UA_UInt16 tci = htons((UA_UInt16)(((UA_UInt16)pcp << 13) |
                                          ((UA_UInt16)dei << 12) | vid));
        memcpy(header + position, &tci, sizeof(tci));
        position += sizeof(tci);
    }
    if(etherType == 0 || etherType == ETH_P_ALL) {
        *lengthOffset = (UA_Byte)position;
    } else {
        UA_UInt16 encoded = htons(etherType);
        memcpy(header + position, &encoded, sizeof(encoded));
    }
    position += sizeof(UA_UInt16);
    return (UA_Byte)position;
}

static size_t
frameHeaderSize(const UA_Byte *frame, size_t size) {
    if(size < 14)
        return 0;
    UA_UInt16 field;
    memcpy(&field, frame + 12, sizeof(field));
    return ntohs(field) == 0x8100 ? (size >= 18 ? 18 : 0) : 14;
}

static PyObject *
ethernetReadable(AsyncIOEthernetConnection *connection, PyObject *args) {
    (void)args;
    if(!connection->manager)
        Py_RETURN_NONE;
    UA_Byte frame[65536];
    ssize_t received = recv(connection->fd, frame, sizeof(frame), 0);
    if(received < 0) {
        if(errno == EAGAIN || errno == EWOULDBLOCK)
            Py_RETURN_NONE;
        PyErr_SetFromErrno(PyExc_OSError);
        return NULL;
    }
    size_t offset = frameHeaderSize(frame, (size_t)received);
    if(offset == 0)
        Py_RETURN_NONE;
    UA_ByteString message = {(size_t)received - offset, frame + offset};
    connection->callback(&connection->manager->cm, connection->connectionId,
                         connection->application, &connection->context,
                         UA_CONNECTIONSTATE_ESTABLISHED,
                         &UA_KEYVALUEMAP_NULL, message);
    Py_RETURN_NONE;
}

static PyTypeObject AsyncIOEthernetConnectionType = {
    .ob_base = PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "o6._EthernetConnection",
    .tp_basicsize = sizeof(AsyncIOEthernetConnection),
    .tp_flags = Py_TPFLAGS_DEFAULT,
    .tp_call = (ternaryfunc)ethernetReadable,
    .tp_new = PyType_GenericNew,
};

static UA_StatusCode
ethernetOpen(UA_ConnectionManager *cm, const UA_KeyValueMap *params,
             void *application, void *context,
             UA_ConnectionManager_connectionCallback callback) {
    AsyncIOEthernetManager *manager = (AsyncIOEthernetManager*)cm;
    AsyncIOLoop *loop = (AsyncIOLoop*)cm->eventSource.eventLoop;
    if(!loop || cm->eventSource.state != UA_EVENTSOURCESTATE_STARTED)
        return UA_STATUSCODE_BADINVALIDSTATE;
    initEthParams();
    UA_StatusCode status = UA_KeyValueRestriction_validate(
        loop->cLoop.logger, "ETH", ethParams, ETH_PARAMETERSSIZE, params);
    if(status != UA_STATUSCODE_GOOD)
        return status;

    const UA_String *interface = (const UA_String*)UA_KeyValueMap_getScalar(
        params, ethParams[2].name, &UA_TYPES[UA_TYPES_STRING]);
    if(!interface || interface->length == 0 || interface->length >= IFNAMSIZ)
        return UA_STATUSCODE_BADINVALIDARGUMENT;
    char ifname[IFNAMSIZ];
    memcpy(ifname, interface->data, interface->length);
    ifname[interface->length] = 0;
    int ifindex = (int)if_nametoindex(ifname);
    if(ifindex == 0)
        return UA_STATUSCODE_BADINVALIDARGUMENT;

    const UA_Boolean *listen = (const UA_Boolean*)UA_KeyValueMap_getScalar(
        params, ethParams[1].name, &UA_TYPES[UA_TYPES_BOOLEAN]);
    UA_Boolean isListener = listen && *listen;
    const UA_UInt16 *etherTypeValue = (const UA_UInt16*)UA_KeyValueMap_getScalar(
        params, ethParams[3].name, &UA_TYPES[UA_TYPES_UINT16]);
    UA_UInt16 etherType = etherTypeValue ? *etherTypeValue : ETH_P_ALL;
    const UA_String *address = (const UA_String*)UA_KeyValueMap_getScalar(
        params, ethParams[0].name, &UA_TYPES[UA_TYPES_STRING]);
    UA_Byte destination[ETH_ALEN];
    if(address && parseMac(address, destination) != UA_STATUSCODE_GOOD)
        return UA_STATUSCODE_BADINVALIDARGUMENT;
    if(!isListener && !address)
        return UA_STATUSCODE_BADINVALIDARGUMENT;

    const UA_Boolean *txtime = (const UA_Boolean*)UA_KeyValueMap_getScalar(
        params, ethParams[9].name, &UA_TYPES[UA_TYPES_BOOLEAN]);
    if(txtime && *txtime)
        return UA_STATUSCODE_BADNOTSUPPORTED;
    const UA_Boolean *validate = (const UA_Boolean*)UA_KeyValueMap_getScalar(
        params, ethParams[14].name, &UA_TYPES[UA_TYPES_BOOLEAN]);
    if(validate && *validate)
        return UA_STATUSCODE_GOOD;

    int fd = socket(PF_PACKET, SOCK_RAW, isListener ? htons(etherType) : 0);
    if(fd < 0)
        return errno == EPERM || errno == EACCES ?
            UA_STATUSCODE_BADUSERACCESSDENIED : UA_STATUSCODE_BADCONNECTIONREJECTED;
    int flags = fcntl(fd, F_GETFL, 0);
    if(flags < 0 || fcntl(fd, F_SETFL, flags | O_NONBLOCK) < 0) {
        close(fd);
        return UA_STATUSCODE_BADINTERNALERROR;
    }

    AsyncIOEthernetConnection **slot = reserveSlot(manager);
    if(!slot) {
        close(fd);
        return UA_STATUSCODE_BADOUTOFMEMORY;
    }
    AsyncIOEthernetConnection *connection = (AsyncIOEthernetConnection*)
        AsyncIOEthernetConnectionType.tp_new(
            &AsyncIOEthernetConnectionType, NULL, NULL);
    if(!connection) {
        close(fd);
        return UA_STATUSCODE_BADOUTOFMEMORY;
    }
    connection->fd = fd;
    connection->connectionId = manager->nextConnectionId++;
    connection->manager = manager;
    connection->callback = callback;
    connection->application = application;
    connection->context = context;
    connection->listening = isListener;
    memset(&connection->target, 0, sizeof(connection->target));
    connection->target.sll_family = AF_PACKET;
    connection->target.sll_protocol = htons(etherType);
    connection->target.sll_ifindex = ifindex;
    connection->target.sll_halen = ETH_ALEN;

    if(isListener) {
        if(bind(fd, (struct sockaddr*)&connection->target,
                sizeof(connection->target)) != 0) {
            close(fd);
            Py_DECREF(connection);
            return UA_STATUSCODE_BADCONNECTIONREJECTED;
        }
        const UA_Boolean *promiscuous = (const UA_Boolean*)
            UA_KeyValueMap_getScalar(params, ethParams[7].name,
                                     &UA_TYPES[UA_TYPES_BOOLEAN]);
        if(promiscuous && *promiscuous) {
            struct packet_mreq membership;
            memset(&membership, 0, sizeof(membership));
            membership.mr_ifindex = ifindex;
            membership.mr_type = PACKET_MR_PROMISC;
            if(setsockopt(fd, SOL_PACKET, PACKET_ADD_MEMBERSHIP,
                          &membership, sizeof(membership)) != 0) {
                close(fd);
                Py_DECREF(connection);
                return UA_STATUSCODE_BADCONNECTIONREJECTED;
            }
        }
        if(address && (destination[0] & 1) != 0) {
            struct packet_mreq membership;
            memset(&membership, 0, sizeof(membership));
            membership.mr_ifindex = ifindex;
            membership.mr_type = PACKET_MR_MULTICAST;
            membership.mr_alen = ETH_ALEN;
            memcpy(membership.mr_address, destination, ETH_ALEN);
            if(setsockopt(fd, SOL_PACKET, PACKET_ADD_MEMBERSHIP,
                          &membership, sizeof(membership)) != 0) {
                close(fd);
                Py_DECREF(connection);
                return UA_STATUSCODE_BADCONNECTIONREJECTED;
            }
        }
        PyObject *registered = PyObject_CallMethod(
            loop->pyLoop, "add_reader", "iO", fd, connection);
        if(!registered) {
            close(fd);
            Py_DECREF(connection);
            PyErr_Clear();
            return UA_STATUSCODE_BADINTERNALERROR;
        }
        Py_DECREF(registered);
    } else {
        struct ifreq request;
        memset(&request, 0, sizeof(request));
        memcpy(request.ifr_name, ifname, interface->length);
        if(ioctl(fd, SIOCGIFHWADDR, &request) < 0) {
            close(fd);
            Py_DECREF(connection);
            return UA_STATUSCODE_BADCONNECTIONREJECTED;
        }
        memcpy(connection->target.sll_addr, destination, ETH_ALEN);
        const UA_UInt16 *vidValue = (const UA_UInt16*)UA_KeyValueMap_getScalar(
            params, ethParams[4].name, &UA_TYPES[UA_TYPES_UINT16]);
        const UA_Byte *pcpValue = (const UA_Byte*)UA_KeyValueMap_getScalar(
            params, ethParams[5].name, &UA_TYPES[UA_TYPES_BYTE]);
        const UA_Boolean *deiValue = (const UA_Boolean*)UA_KeyValueMap_getScalar(
            params, ethParams[6].name, &UA_TYPES[UA_TYPES_BOOLEAN]);
        connection->headerSize = makeHeader(
            connection->header, destination,
            (UA_Byte*)request.ifr_hwaddr.sa_data, etherType,
            vidValue ? *vidValue : 0, pcpValue ? *pcpValue : 0,
            deiValue ? *deiValue : false, &connection->lengthOffset);
        const UA_UInt32 *priority = (const UA_UInt32*)UA_KeyValueMap_getScalar(
            params, ethParams[8].name, &UA_TYPES[UA_TYPES_UINT32]);
        if(priority) {
            int nativePriority = (int)*priority;
            if(setsockopt(fd, SOL_SOCKET, SO_PRIORITY,
                          &nativePriority, sizeof(nativePriority)) != 0) {
                close(fd);
                Py_DECREF(connection);
                return UA_STATUSCODE_BADCONNECTIONREJECTED;
            }
        }
    }

    *slot = connection;
    callback(cm, connection->connectionId, application, &connection->context,
             UA_CONNECTIONSTATE_ESTABLISHED,
             &UA_KEYVALUEMAP_NULL, UA_BYTESTRING_NULL);
    return UA_STATUSCODE_GOOD;
}

static UA_StatusCode
ethernetAlloc(UA_ConnectionManager *cm, uintptr_t id,
              UA_ByteString *buffer, size_t size) {
    AsyncIOEthernetConnection *connection = findConnection(
        (AsyncIOEthernetManager*)cm, id);
    if(!connection || connection->listening)
        return UA_STATUSCODE_BADCONNECTIONREJECTED;
    UA_StatusCode status = UA_ByteString_allocBuffer(
        buffer, size + connection->headerSize);
    if(status == UA_STATUSCODE_GOOD) {
        buffer->data += connection->headerSize;
        buffer->length -= connection->headerSize;
    }
    return status;
}

static void
ethernetRelease(UA_ConnectionManager *cm, uintptr_t id,
                UA_ByteString *buffer) {
    AsyncIOEthernetConnection *connection = findConnection(
        (AsyncIOEthernetManager*)cm, id);
    if(connection) {
        buffer->data -= connection->headerSize;
        buffer->length += connection->headerSize;
    }
    UA_ByteString_clear(buffer);
}

static UA_StatusCode
ethernetSend(UA_ConnectionManager *cm, uintptr_t id,
             const UA_KeyValueMap *params, UA_ByteString *buffer) {
    (void)params;
    AsyncIOEthernetConnection *connection = findConnection(
        (AsyncIOEthernetManager*)cm, id);
    if(!connection)
        return UA_STATUSCODE_BADCONNECTIONREJECTED;
    if(connection->listening) {
        ethernetRelease(cm, id, buffer);
        return UA_STATUSCODE_BADCONNECTIONREJECTED;
    }
    buffer->data -= connection->headerSize;
    buffer->length += connection->headerSize;
    memcpy(buffer->data, connection->header, connection->headerSize);
    if(connection->lengthOffset) {
        UA_UInt16 length = htons((UA_UInt16)(buffer->length -
                                             connection->headerSize));
        memcpy(buffer->data + connection->lengthOffset,
               &length, sizeof(length));
    }
    ssize_t sent = sendto(connection->fd, buffer->data, buffer->length, 0,
                          (struct sockaddr*)&connection->target,
                          sizeof(connection->target));
    UA_StatusCode status = sent == (ssize_t)buffer->length ?
        UA_STATUSCODE_GOOD : UA_STATUSCODE_BADCOMMUNICATIONERROR;
    UA_ByteString_clear(buffer);
    return status;
}

static void
ethernetCloseDelayed(void *application, void *context) {
    (void)context;
    AsyncIOEthernetConnection *connection =
        (AsyncIOEthernetConnection*)application;
    AsyncIOEthernetManager *manager = connection->manager;
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
ethernetClose(UA_ConnectionManager *cm, uintptr_t id) {
    AsyncIOEthernetManager *manager = (AsyncIOEthernetManager*)cm;
    AsyncIOLoop *loop = (AsyncIOLoop*)cm->eventSource.eventLoop;
    for(size_t i = 0; i < manager->capacity; i++) {
        AsyncIOEthernetConnection *connection = manager->connections[i];
        if(!connection || connection->connectionId != id)
            continue;
        manager->connections[i] = NULL;
        if(connection->listening && !loop->tearingDown) {
            PyObject *removed = PyObject_CallMethod(
                loop->pyLoop, "remove_reader", "i", connection->fd);
            Py_XDECREF(removed);
            PyErr_Clear();
        }
        close(connection->fd);
        connection->fd = -1;
        if(loop->tearingDown) {
            connection->manager = NULL;
            Py_DECREF(connection);
        } else {
            connection->closingCallback.callback = ethernetCloseDelayed;
            connection->closingCallback.application = connection;
            loop->cLoop.addDelayedCallback(&loop->cLoop,
                                           &connection->closingCallback);
        }
        return UA_STATUSCODE_GOOD;
    }
    return UA_STATUSCODE_BADNOTFOUND;
}

static UA_StatusCode ethernetStart(UA_EventSource *source) {
    source->state = UA_EVENTSOURCESTATE_STARTED;
    return UA_STATUSCODE_GOOD;
}

static void ethernetStop(UA_EventSource *source) {
    AsyncIOEthernetManager *manager = (AsyncIOEthernetManager*)source;
    for(size_t i = 0; i < manager->capacity; i++)
        if(manager->connections[i])
            ethernetClose(&manager->cm,
                          manager->connections[i]->connectionId);
    source->state = UA_EVENTSOURCESTATE_STOPPED;
}

static UA_StatusCode ethernetFree(UA_EventSource *source) {
    AsyncIOEthernetManager *manager = (AsyncIOEthernetManager*)source;
    UA_KeyValueMap_clear(&source->params);
    UA_String_clear(&source->name);
    UA_free(manager->connections);
    UA_free(manager);
    return UA_STATUSCODE_GOOD;
}

int
AsyncIOEthernet_initTypes(void) {
    if(AsyncIOEthernetConnectionType.tp_flags & Py_TPFLAGS_READY)
        return 0;
    return PyType_Ready(&AsyncIOEthernetConnectionType);
}

UA_ConnectionManager *
UA_ConnectionManager_new_AsyncIO_Ethernet(void) {
    if(AsyncIOEthernet_initTypes() < 0)
        return NULL;
    AsyncIOEthernetManager *manager =
        (AsyncIOEthernetManager*)UA_calloc(1, sizeof(*manager));
    if(!manager)
        return NULL;
    manager->nextConnectionId = 1;
    UA_ConnectionManager *cm = &manager->cm;
    cm->eventSource.eventSourceType = UA_EVENTSOURCETYPE_CONNECTIONMANAGER;
    cm->eventSource.name = UA_STRING_ALLOC("ethernet-source");
    cm->eventSource.start = ethernetStart;
    cm->eventSource.stop = ethernetStop;
    cm->eventSource.free = ethernetFree;
    cm->protocol = UA_STRING((char*)(uintptr_t)"eth");
    cm->openConnection = ethernetOpen;
    cm->sendWithConnection = ethernetSend;
    cm->closeConnection = ethernetClose;
    cm->allocNetworkBuffer = ethernetAlloc;
    cm->freeNetworkBuffer = ethernetRelease;
    return cm;
}

#else

int
AsyncIOEthernet_initTypes(void) {
    return 0;
}

UA_ConnectionManager *
UA_ConnectionManager_new_AsyncIO_Ethernet(void) {
    return NULL;
}

#endif
