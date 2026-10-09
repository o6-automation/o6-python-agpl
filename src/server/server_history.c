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

#include "server_history.h"

#include <open62541/client_subscriptions.h> /* UA_MonitoredItemCreateRequest_default */
#include <open62541/plugin/historydata/history_database_default.h>
#include <open62541/plugin/historydata/history_data_gathering_default.h>

#include <limits.h>
#include <stdint.h>
#include <string.h>

/* ==================================================== *
 *                      Ring store                      *
 * ==================================================== */

/* One node's store. `slots` and `stamps` are parallel arrays of `capacity`
 * entries and a sequence number in [firstSeq, firstSeq + count) addresses
 * slots[seq % capacity]; see the index-space note in server_history.h.
 *
 * Timestamps live apart from the values so ordering searches never touch a
 * DataValue, and so a HistoryUpdate replace cannot reorder an entry by
 * rewriting its own timestamps.
 *
 * The gathering's per-node state sits here too, which is what makes recording
 * one lookup rather than two. `registered` separates a store only the backend
 * knows about - what a failed registration leaves behind - from a node the
 * gathering records for. */
typedef struct {
    UA_NodeId nodeId;
    UA_UInt32 hash; /* of nodeId; the index probes on it */
    UA_DataValue *slots;
    UA_DateTime *stamps;
    size_t capacity;
    size_t count;
    size_t firstSeq;
    UA_Boolean unbounded; /* grow instead of evicting */
    UA_UInt64 stored;
    UA_UInt64 overwrites;
    UA_UInt64 dropped;

    UA_HistorizingNodeIdSettings setting;
    UA_MonitoredItemCreateResult monitoredResult; /* id 0 when not polling */
    UA_Boolean registered;
    UA_Boolean paused;
} PyHistoryNodeStore;

/* Empty index slot. Not a reachable node index: the table would have to hold
 * SIZE_MAX + 1 stores. */
#define PYO6_HISTORY_INDEX_EMPTY SIZE_MAX

#define PYO6_HISTORY_INDEX_MIN 16

/* Open-addressed NodeId hash -> slot in `nodes`, linear probing, no tombstones:
 * removing a node and growing the table both rebuild instead, and both are
 * registration-time paths. Entries are indices, not pointers, so growing
 * `nodes` does not invalidate them. `capacity` is a power of two kept at least
 * twice `nodesSize`, which bounds probes and guarantees the loop stops. */
typedef struct {
    size_t *slots;
    size_t capacity;
} PyHistoryIndex;

typedef struct {
    PyHistoryNodeStore *nodes;
    size_t nodesSize;     /* stores in use */
    size_t nodesCapacity; /* stores allocated */
    size_t defaultCapacity;
    PyHistoryIndex index;
} PyHistoryRingContext;

/* Returned for out-of-range indices, since UA_HistoryDatabase_default
 * dereferences the result unconditionally when it fabricates a bound. */
static const UA_DataValue emptyDataValue = {0};

static size_t
store_index(const PyHistoryNodeStore *store, size_t seq) {
    return seq % store->capacity;
}

static UA_DataValue *
store_slot(const PyHistoryNodeStore *store, size_t seq) {
    return &store->slots[store_index(store, seq)];
}

static UA_DateTime
store_stamp(const PyHistoryNodeStore *store, size_t seq) {
    return store->stamps[store_index(store, seq)];
}

/* One past the newest retained sequence number, and the "no match" sentinel of
 * the plugin interface. */
static size_t
store_end(const PyHistoryNodeStore *store) {
    return store->firstSeq + store->count;
}

static UA_Boolean
store_holds(const PyHistoryNodeStore *store, size_t seq) {
    return seq >= store->firstSeq && seq < store_end(store);
}

/* Lower bound over the retained window. *seq receives the insertion position,
 * store_end() when every retained sample is older. */
static UA_Boolean
store_search(const PyHistoryNodeStore *store, UA_DateTime timestamp,
             size_t *seq) {
    size_t lo = store->firstSeq;
    size_t hi = store_end(store);
    while(lo < hi) {
        size_t mid = lo + ((hi - lo) / 2);
        if(store_stamp(store, mid) < timestamp)
            lo = mid + 1;
        else
            hi = mid;
    }
    *seq = lo;
    return lo < store_end(store) && store_stamp(store, lo) == timestamp;
}

/* getDateTimeMatch on sequence numbers: upstream's memory backend with firstSeq
 * for index 0 and store_end() for storeEnd. */
static size_t
store_match(const PyHistoryNodeStore *store, UA_DateTime timestamp,
            MatchStrategy strategy) {
    size_t end = store_end(store);
    size_t seq = end;
    UA_Boolean equal = store_search(store, timestamp, &seq);
    switch(strategy) {
    case MATCH_EQUAL:
        return equal ? seq : end;
    case MATCH_EQUAL_OR_AFTER:
        return seq;
    case MATCH_AFTER:
        return equal ? seq + 1 : seq;
    case MATCH_EQUAL_OR_BEFORE:
        if(equal)
            return seq;
        /* fall through */
    case MATCH_BEFORE:
        return (seq > store->firstSeq) ? seq - 1 : end;
    default:
        break;
    }
    return end;
}

static UA_DateTime
value_timestamp(const UA_DataValue *value) {
    if(value->hasSourceTimestamp)
        return value->sourceTimestamp;
    if(value->hasServerTimestamp)
        return value->serverTimestamp;
    return UA_DateTime_now();
}

/* Overwrite `slot` in place, keeping the allocation its value already owns.
 * Only possible when both sides are a scalar of the same pointer-free type,
 * which is the steady state of one node recording one signal - and it is what
 * keeps a full store from doing a free and a malloc for every sample. */
static UA_Boolean
value_overwrite(UA_DataValue *slot, const UA_DataValue *value) {
    const UA_DataType *type = value->value.type;
    if(!slot->hasValue || !value->hasValue || type == NULL || !type->pointerFree)
        return false;
    if(slot->value.type != type || slot->value.storageType != UA_VARIANT_DATA)
        return false;
    if(!UA_Variant_isScalar(&slot->value) || !UA_Variant_isScalar(&value->value))
        return false;
    if(slot->value.arrayDimensionsSize > 0 || value->value.arrayDimensionsSize > 0)
        return false;

    memcpy(slot->value.data, value->value.data, type->memSize);
    UA_Variant owned = slot->value;
    *slot = *value;      /* timestamps, status and their flags */
    slot->value = owned; /* but the allocation stays ours */
    return true;
}

/* Double a growing store. A sample's slot is seq % capacity, so changing the
 * capacity moves every one of them - which rules out a realloc. The values are
 * moved into fresh arrays, and the old ones released without being cleared. */
static UA_StatusCode
store_grow(PyHistoryNodeStore *store) {
    size_t grown = store->capacity ? store->capacity * 2 : PYO6_HISTORY_GROW_MIN;
    if(grown <= store->capacity)
        return UA_STATUSCODE_BADOUTOFMEMORY; /* size_t would wrap */

    UA_DataValue *slots = (UA_DataValue *)UA_calloc(grown, sizeof(UA_DataValue));
    UA_DateTime *stamps = (UA_DateTime *)UA_calloc(grown, sizeof(UA_DateTime));
    if(!slots || !stamps) {
        UA_free(slots);
        UA_free(stamps);
        return UA_STATUSCODE_BADOUTOFMEMORY;
    }

    size_t end = store_end(store);
    for(size_t seq = store->firstSeq; seq < end; ++seq) {
        slots[seq % grown] = *store_slot(store, seq);
        stamps[seq % grown] = store_stamp(store, seq);
    }
    UA_free(store->slots);
    UA_free(store->stamps);
    store->slots = slots;
    store->stamps = stamps;
    store->capacity = grown;
    return UA_STATUSCODE_GOOD;
}

static void
store_evictOldest(PyHistoryNodeStore *store) {
    if(store->count == 0)
        return;
    UA_DataValue_clear(store_slot(store, store->firstSeq));
    ++store->firstSeq;
    --store->count;
    ++store->overwrites;
}

/* Insert at `seq`, shifting everything above it up by one. Requires
 * count < capacity and firstSeq <= seq <= store_end(). */
static UA_StatusCode
store_insertAt(PyHistoryNodeStore *store, size_t seq, const UA_DataValue *value,
               UA_DateTime timestamp) {
    /* Copy before shifting, so a failed copy leaves the store untouched. */
    UA_DataValue copy;
    UA_DataValue_init(&copy);
    UA_StatusCode status = UA_DataValue_copy(value, &copy);
    if(status != UA_STATUSCODE_GOOD)
        return status;

    if(!copy.hasServerTimestamp) {
        copy.serverTimestamp = timestamp;
        copy.hasServerTimestamp = true;
    }

    /* Walk the slots down rather than deriving each from its sequence number:
     * the wrap is one comparison where store_index would be four divisions. */
    size_t capacity = store->capacity;
    size_t to = store_index(store, store_end(store));
    for(size_t cur = store_end(store); cur > seq; --cur) {
        size_t from = (to == 0) ? capacity - 1 : to - 1;
        store->slots[to] = store->slots[from];
        store->stamps[to] = store->stamps[from];
        to = from;
    }

    store->slots[to] = copy; /* ownership moves into the store */
    store->stamps[to] = timestamp;
    ++store->count;
    ++store->stored;
    return UA_STATUSCODE_GOOD;
}

static UA_StatusCode
store_put(PyHistoryNodeStore *store, const UA_DataValue *value,
          UA_DateTime timestamp, UA_Boolean rejectExisting) {
    if(store->capacity == 0)
        return UA_STATUSCODE_BADOUTOFMEMORY;

    size_t end = store_end(store);
    UA_Boolean append =
        (store->count == 0 || timestamp > store_stamp(store, end - 1));

    size_t seq = end;
    UA_Boolean equal = false;
    if(!append)
        equal = store_search(store, timestamp, &seq);
    if(equal && rejectExisting)
        return UA_STATUSCODE_BADENTRYEXISTS;

    if(store->count < store->capacity)
        return store_insertAt(store, seq, value, timestamp);

    if(store->unbounded) {
        /* Growing keeps the sequence numbers already handed out, so even a
         * sample older than the oldest retained one still has a place. */
        UA_StatusCode status = store_grow(store);
        if(status != UA_STATUSCODE_GOOD)
            return status;
        return store_insertAt(store, seq, value, timestamp);
    }

    if(timestamp < store_stamp(store, store->firstSeq)) {
        ++store->dropped; /* no room below the oldest */
        return UA_STATUSCODE_GOODNODATA;
    }

    /* Appending onto a full store writes the very slot the eviction frees,
     * (firstSeq + capacity) % capacity being firstSeq % capacity, so the
     * allocation can carry straight over. */
    if(append) {
        UA_DataValue *slot = store_slot(store, store->firstSeq);
        if(value_overwrite(slot, value)) {
            if(!slot->hasServerTimestamp) {
                slot->serverTimestamp = timestamp;
                slot->hasServerTimestamp = true;
            }
            store->stamps[store_index(store, store->firstSeq)] = timestamp;
            ++store->firstSeq;
            ++store->overwrites;
            ++store->stored;
            return UA_STATUSCODE_GOOD;
        }
    }

    store_evictOldest(store);
    if(seq < store->firstSeq)
        seq = store->firstSeq;
    return store_insertAt(store, seq, value, timestamp);
}

/* The tail both recording paths share. A sample older than the whole store is
 * counted and dropped rather than reported: there is no room below the oldest. */
static UA_StatusCode
store_record(PyHistoryNodeStore *store, const UA_DataValue *value) {
    UA_StatusCode status = store_put(store, value, value_timestamp(value), false);
    return (status == UA_STATUSCODE_GOODNODATA) ? UA_STATUSCODE_GOOD : status;
}

/* Remove the samples in [first, last], both retained. */
static void
store_removeRange(PyHistoryNodeStore *store, size_t first, size_t last) {
    size_t end = store_end(store);
    size_t removed = last - first + 1;

    for(size_t seq = first; seq <= last; ++seq)
        UA_DataValue_clear(store_slot(store, seq));

    if(first == store->firstSeq) {
        store->firstSeq = last + 1; /* dropping the head only moves the window */
        store->count -= removed;
        return;
    }

    size_t capacity = store->capacity;
    size_t to = store_index(store, first);
    size_t from = store_index(store, first + removed);
    for(size_t seq = first; seq + removed < end; ++seq) {
        store->slots[to] = store->slots[from];
        store->stamps[to] = store->stamps[from];
        to = (to + 1 == capacity) ? 0 : to + 1;
        from = (from + 1 == capacity) ? 0 : from + 1;
    }
    /* The vacated tail still aliases values that moved down. */
    for(size_t seq = end - removed; seq < end; ++seq)
        UA_DataValue_init(store_slot(store, seq));
    store->count -= removed;
}

/* Discard every sample but keep the store. Sequence numbers keep counting up so
 * that continuation points issued earlier cannot address the new samples. */
static void
store_clearSamples(PyHistoryNodeStore *store) {
    size_t end = store_end(store);
    for(size_t seq = store->firstSeq; seq < end; ++seq)
        UA_DataValue_clear(store_slot(store, seq));
    store->firstSeq = end;
    store->count = 0;
}

static void
store_clear(PyHistoryNodeStore *store) {
    store_clearSamples(store);
    UA_NodeId_clear(&store->nodeId);
    /* Carries an allocated filterResult even when polling never started. Any
     * MonitoredItem it names is the caller's to delete while the server lives. */
    UA_MonitoredItemCreateResult_clear(&store->monitoredResult);
    UA_free(store->slots);
    UA_free(store->stamps);
    memset(store, 0, sizeof(PyHistoryNodeStore));
}

/* ==================================================== *
 *                      Node index                      *
 * ==================================================== */

static void
index_clear(PyHistoryIndex *index) {
    UA_free(index->slots);
    index->slots = NULL;
    index->capacity = 0;
}

/* Place `node` in a table known to have room, so a run of occupied slots always
 * ends in an empty one. */
static void
index_place(PyHistoryIndex *index, const PyHistoryNodeStore *nodes,
            size_t node) {
    size_t mask = index->capacity - 1;
    size_t i = (size_t)nodes[node].hash & mask;
    while(index->slots[i] != PYO6_HISTORY_INDEX_EMPTY)
        i = (i + 1) & mask;
    index->slots[i] = node;
}

/* Re-place every store in the table it already has. Allocation free, so the
 * paths that shrink or reorder `nodes` cannot fail partway. */
static void
index_reindex(PyHistoryIndex *index, const PyHistoryNodeStore *nodes,
              size_t nodesSize) {
    if(!index->slots)
        return;
    memset(index->slots, 0xff, index->capacity * sizeof(size_t)); /* all EMPTY */
    for(size_t i = 0; i < nodesSize; ++i)
        index_place(index, nodes, i);
}

/* Grow to at least `wanted` slots, rounded up to a power of two. The old table
 * stays put when the new one cannot be allocated. */
static UA_StatusCode
index_grow(PyHistoryRingContext *ctx, size_t wanted) {
    size_t capacity = PYO6_HISTORY_INDEX_MIN;
    while(capacity < wanted) {
        size_t doubled = capacity * 2;
        if(doubled < capacity)
            return UA_STATUSCODE_BADOUTOFMEMORY; /* size_t would wrap */
        capacity = doubled;
    }

    size_t *slots = (size_t *)UA_malloc(capacity * sizeof(size_t));
    if(!slots)
        return UA_STATUSCODE_BADOUTOFMEMORY;

    index_clear(&ctx->index);
    ctx->index.slots = slots;
    ctx->index.capacity = capacity;
    index_reindex(&ctx->index, ctx->nodes, ctx->nodesSize);
    return UA_STATUSCODE_GOOD;
}

/* Make room for one more store, keeping the table at most half full. */
static UA_StatusCode
index_reserve(PyHistoryRingContext *ctx) {
    if(ctx->index.slots && (ctx->nodesSize + 1) * 2 <= ctx->index.capacity)
        return UA_STATUSCODE_GOOD;
    return index_grow(ctx, (ctx->nodesSize + 1) * 2);
}

/* ==================================================== *
 *                    Backend context                   *
 * ==================================================== */

/* Node stores are never created implicitly by a write: a write to an
 * unregistered node is an error rather than an unbudgeted allocation. */
static PyHistoryNodeStore *
ring_find(const PyHistoryRingContext *ctx, const UA_NodeId *nodeId) {
    if(!ctx || !nodeId || !ctx->index.slots)
        return NULL;
    UA_UInt32 hash = UA_NodeId_hash(nodeId);
    size_t mask = ctx->index.capacity - 1;
    for(size_t i = (size_t)hash & mask; ; i = (i + 1) & mask) {
        size_t node = ctx->index.slots[i];
        if(node == PYO6_HISTORY_INDEX_EMPTY)
            return NULL; /* the table is never full, so this always arrives */
        PyHistoryNodeStore *store = &ctx->nodes[node];
        /* Distinct NodeIds can share a hash; keep probing past a false hit. */
        if(store->hash == hash && UA_NodeId_equal(&store->nodeId, nodeId))
            return store;
    }
}

static PyHistoryNodeStore *
ring_store(void *context, const UA_NodeId *nodeId) {
    return ring_find((const PyHistoryRingContext *)context, nodeId);
}

/* ==================================================== *
 *              UA_HistoryDataBackend hooks             *
 * ==================================================== */

static UA_StatusCode
serverSetHistoryData_ring(UA_Server *server, void *context,
                          const UA_NodeId *sessionId, void *sessionContext,
                          const UA_NodeId *nodeId, UA_Boolean historizing,
                          const UA_DataValue *value) {
    (void)server;
    (void)sessionContext;
    /* Only meaningful when a session performed the write. readRaw refuses a
     * node whose attribute is false, so buffering would only consume the store. */
    if(sessionId != NULL && !historizing)
        return UA_STATUSCODE_GOOD;

    PyHistoryNodeStore *store = ring_store(context, nodeId);
    if(!store)
        return UA_STATUSCODE_BADNODEIDUNKNOWN;
    if(store->paused)
        return UA_STATUSCODE_GOOD;

    return store_record(store, value);
}

static size_t
getDateTimeMatch_ring(UA_Server *server, void *context,
                      const UA_NodeId *sessionId, void *sessionContext,
                      const UA_NodeId *nodeId, const UA_DateTime timestamp,
                      const MatchStrategy strategy) {
    (void)server;
    (void)sessionId;
    (void)sessionContext;
    const PyHistoryNodeStore *store = ring_store(context, nodeId);
    if(!store)
        return 0;
    return store_match(store, timestamp, strategy);
}

static size_t
getEnd_ring(UA_Server *server, void *context, const UA_NodeId *sessionId,
            void *sessionContext, const UA_NodeId *nodeId) {
    (void)server;
    (void)sessionId;
    (void)sessionContext;
    const PyHistoryNodeStore *store = ring_store(context, nodeId);
    if(!store)
        return 0;
    return store_end(store);
}

static size_t
lastIndex_ring(UA_Server *server, void *context, const UA_NodeId *sessionId,
               void *sessionContext, const UA_NodeId *nodeId) {
    (void)server;
    (void)sessionId;
    (void)sessionContext;
    const PyHistoryNodeStore *store = ring_store(context, nodeId);
    if(!store)
        return 0;
    /* An empty store reports the sentinel, which the service reads as
     * "no values". */
    if(store->count == 0)
        return store_end(store);
    return store_end(store) - 1;
}

static size_t
firstIndex_ring(UA_Server *server, void *context, const UA_NodeId *sessionId,
                void *sessionContext, const UA_NodeId *nodeId) {
    (void)server;
    (void)sessionId;
    (void)sessionContext;
    const PyHistoryNodeStore *store = ring_store(context, nodeId);
    if(!store)
        return 0;
    return store->firstSeq;
}

static size_t
resultSize_ring(UA_Server *server, void *context, const UA_NodeId *sessionId,
                void *sessionContext, const UA_NodeId *nodeId,
                size_t startIndex, size_t endIndex) {
    (void)server;
    (void)sessionId;
    (void)sessionContext;
    const PyHistoryNodeStore *store = ring_store(context, nodeId);
    if(!store || store->count == 0)
        return 0;

    size_t end = store_end(store);
    if(startIndex == end || endIndex == end)
        return 0;

    /* The service passes the pair in ascending order, reversed for reverse
     * reads. Accept either order rather than underflow. */
    size_t lo = startIndex < endIndex ? startIndex : endIndex;
    size_t hi = startIndex < endIndex ? endIndex : startIndex;
    if(hi < store->firstSeq || lo >= end)
        return 0;
    if(lo < store->firstSeq)
        lo = store->firstSeq;
    if(hi >= end)
        hi = end - 1;
    return hi - lo + 1;
}

/* UA_DataValue_copy over a NumericRange. A value that cannot be ranged is
 * reported through the copy's own StatusCode rather than failing the read. */
static void
copy_value_range(const UA_DataValue *src, UA_DataValue *dst,
                 const UA_NumericRange range) {
    *dst = *src;                  /* timestamps, status and their flags */
    dst->hasValue = false;
    UA_Variant_init(&dst->value); /* drop the alias the struct copy made */

    if(!src->hasValue) {
        dst->hasStatus = true;
        dst->status = UA_STATUSCODE_BADDATAUNAVAILABLE;
        return;
    }

    UA_StatusCode status = UA_Variant_copyRange(&src->value, &dst->value, range);
    if(status != UA_STATUSCODE_GOOD) {
        dst->hasStatus = true;
        dst->status = status;
        return;
    }
    dst->hasValue = true;
}

static UA_StatusCode
copyDataValues_ring(UA_Server *server, void *context, const UA_NodeId *sessionId,
                    void *sessionContext, const UA_NodeId *nodeId,
                    size_t startIndex, size_t endIndex, UA_Boolean reverse,
                    size_t maxValues, UA_NumericRange range,
                    UA_Boolean releaseContinuationPoints,
                    const UA_ByteString *continuationPoint,
                    UA_ByteString *outContinuationPoint,
                    size_t *providedValues, UA_DataValue *values) {
    (void)server;
    (void)sessionId;
    (void)sessionContext;
    if(providedValues)
        *providedValues = 0;
    if(releaseContinuationPoints)
        return UA_STATUSCODE_GOOD; /* nothing of ours is held between calls */

    UA_Boolean resuming = (continuationPoint->length > 0);
    size_t next = 0;
    if(resuming) {
        if(continuationPoint->length != sizeof(size_t))
            return UA_STATUSCODE_BADCONTINUATIONPOINTINVALID;
        memcpy(&next, continuationPoint->data, sizeof(size_t));
    }

    UA_StatusCode empty = resuming ? UA_STATUSCODE_BADCONTINUATIONPOINTINVALID
                                   : UA_STATUSCODE_GOOD;

    const PyHistoryNodeStore *store = ring_store(context, nodeId);
    if(!store)
        return UA_STATUSCODE_BADNODEIDUNKNOWN;

    size_t lo = reverse ? endIndex : startIndex;
    size_t hi = reverse ? startIndex : endIndex;
    if(hi < lo)
        return empty;

    /* Clamp into what the store still holds, so an evicted sample is lost
     * rather than read out of the slot it used to occupy. */
    size_t end = store_end(store);
    if(store->count == 0 || hi < store->firstSeq || lo >= end)
        return empty;
    if(lo < store->firstSeq)
        lo = store->firstSeq;
    if(hi >= end)
        hi = end - 1;

    if(resuming) {
        /* A point the window has overrun resumes at the oldest sample still
         * held - all a ring can honestly offer - but one that has nothing left
         * in front of it cannot be honoured at all. */
        if(reverse) {
            if(next < lo)
                return UA_STATUSCODE_BADCONTINUATIONPOINTINVALID;
            if(next < hi)
                hi = next;
        } else {
            if(next > hi)
                return UA_STATUSCODE_BADCONTINUATIONPOINTINVALID;
            if(next > lo)
                lo = next;
        }
    }

    size_t counter = 0;
    for(size_t i = 0; i <= hi - lo && counter < maxValues; ++i) {
        size_t seq = reverse ? hi - i : lo + i;
        const UA_DataValue *src = store_slot(store, seq);
        if(range.dimensionsSize > 0) {
            copy_value_range(src, &values[counter], range);
        } else {
            UA_StatusCode status = UA_DataValue_copy(src, &values[counter]);
            if(status != UA_STATUSCODE_GOOD) {
                if(providedValues)
                    *providedValues = counter;
                return status;
            }
        }
        ++counter;
    }

    if(resuming && counter < maxValues)
        return UA_STATUSCODE_BADCONTINUATIONPOINTINVALID;

    if(providedValues)
        *providedValues = counter;

    if(counter > 0 && counter <= hi - lo) {
        UA_Byte *cp = (UA_Byte *)UA_malloc(sizeof(size_t));
        if(!cp)
            return UA_STATUSCODE_BADOUTOFMEMORY;
        size_t next = reverse ? hi - counter : lo + counter;
        memcpy(cp, &next, sizeof(size_t));
        outContinuationPoint->data = cp;
        outContinuationPoint->length = sizeof(size_t);
    }

    return UA_STATUSCODE_GOOD;
}

static const UA_DataValue *
getDataValue_ring(UA_Server *server, void *context, const UA_NodeId *sessionId,
                  void *sessionContext, const UA_NodeId *nodeId, size_t index) {
    (void)server;
    (void)sessionId;
    (void)sessionContext;
    const PyHistoryNodeStore *store = ring_store(context, nodeId);
    if(!store || !store_holds(store, index))
        return &emptyDataValue;
    return store_slot(store, index);
}

static UA_Boolean
boundSupported_ring(UA_Server *server, void *context, const UA_NodeId *sessionId,
                    void *sessionContext, const UA_NodeId *nodeId) {
    (void)server;
    (void)context;
    (void)sessionId;
    (void)sessionContext;
    (void)nodeId;
    return true;
}

static UA_Boolean
timestampsToReturnSupported_ring(UA_Server *server, void *context,
                                 const UA_NodeId *sessionId,
                                 void *sessionContext, const UA_NodeId *nodeId,
                                 const UA_TimestampsToReturn
                                     timestampsToReturn) {
    (void)server;
    (void)sessionId;
    (void)sessionContext;
    const PyHistoryNodeStore *store = ring_store(context, nodeId);
    if(!store || store->count == 0)
        return true;

    const UA_DataValue *oldest = store_slot(store, store->firstSeq);
    if(timestampsToReturn == UA_TIMESTAMPSTORETURN_NEITHER ||
       timestampsToReturn == UA_TIMESTAMPSTORETURN_INVALID ||
       (timestampsToReturn == UA_TIMESTAMPSTORETURN_SERVER &&
        !oldest->hasServerTimestamp) ||
       (timestampsToReturn == UA_TIMESTAMPSTORETURN_SOURCE &&
        !oldest->hasSourceTimestamp) ||
       (timestampsToReturn == UA_TIMESTAMPSTORETURN_BOTH &&
        !(oldest->hasSourceTimestamp && oldest->hasServerTimestamp)))
        return false;
    return true;
}

static UA_StatusCode
insertDataValue_ring(UA_Server *server, void *context,
                     const UA_NodeId *sessionId, void *sessionContext,
                     const UA_NodeId *nodeId, const UA_DataValue *value) {
    (void)server;
    (void)sessionId;
    (void)sessionContext;
    if(!value->hasSourceTimestamp && !value->hasServerTimestamp)
        return UA_STATUSCODE_BADINVALIDTIMESTAMP;
    PyHistoryNodeStore *store = ring_store(context, nodeId);
    if(!store)
        return UA_STATUSCODE_BADNODEIDUNKNOWN;

    UA_DateTime timestamp = value->hasSourceTimestamp ? value->sourceTimestamp
                                                      : value->serverTimestamp;
    UA_StatusCode status = store_put(store, value, timestamp, true);
    if(status == UA_STATUSCODE_GOODNODATA)
        return UA_STATUSCODE_BADOUTOFMEMORY; /* no room below the oldest */
    return status;
}

static UA_StatusCode
replaceDataValue_ring(UA_Server *server, void *context,
                      const UA_NodeId *sessionId, void *sessionContext,
                      const UA_NodeId *nodeId, const UA_DataValue *value) {
    (void)server;
    (void)sessionId;
    (void)sessionContext;
    if(!value->hasSourceTimestamp && !value->hasServerTimestamp)
        return UA_STATUSCODE_BADINVALIDTIMESTAMP;
    PyHistoryNodeStore *store = ring_store(context, nodeId);
    if(!store)
        return UA_STATUSCODE_BADNODEIDUNKNOWN;

    UA_DateTime timestamp = value->hasSourceTimestamp ? value->sourceTimestamp
                                                      : value->serverTimestamp;
    size_t seq = store_match(store, timestamp, MATCH_EQUAL);
    if(seq == store_end(store))
        return UA_STATUSCODE_BADNOENTRYEXISTS;

    UA_DataValue copy;
    UA_DataValue_init(&copy);
    UA_StatusCode status = UA_DataValue_copy(value, &copy);
    if(status != UA_STATUSCODE_GOOD)
        return status;
    if(!copy.hasServerTimestamp) {
        copy.serverTimestamp = timestamp;
        copy.hasServerTimestamp = true;
    }

    /* The match was exact, so the sort key does not move. */
    UA_DataValue *slot = store_slot(store, seq);
    UA_DataValue_clear(slot);
    *slot = copy;
    return UA_STATUSCODE_GOOD;
}

static UA_StatusCode
updateDataValue_ring(UA_Server *server, void *context,
                     const UA_NodeId *sessionId, void *sessionContext,
                     const UA_NodeId *nodeId, const UA_DataValue *value) {
    UA_StatusCode status = replaceDataValue_ring(
        server, context, sessionId, sessionContext, nodeId, value);
    if(status == UA_STATUSCODE_GOOD)
        return UA_STATUSCODE_GOODENTRYREPLACED;

    status = insertDataValue_ring(server, context, sessionId, sessionContext,
                                 nodeId, value);
    if(status == UA_STATUSCODE_GOOD)
        return UA_STATUSCODE_GOODENTRYINSERTED;
    return status;
}

static UA_StatusCode
removeDataValue_ring(UA_Server *server, void *context,
                     const UA_NodeId *sessionId, void *sessionContext,
                     const UA_NodeId *nodeId, UA_DateTime startTimestamp,
                     UA_DateTime endTimestamp) {
    (void)server;
    (void)sessionId;
    (void)sessionContext;
    if(startTimestamp > endTimestamp)
        return UA_STATUSCODE_BADTIMESTAMPNOTSUPPORTED;
    PyHistoryNodeStore *store = ring_store(context, nodeId);
    if(!store)
        return UA_STATUSCODE_BADNODEIDUNKNOWN;

    size_t end = store_end(store);
    size_t first;
    size_t last;
    if(startTimestamp == endTimestamp) {
        first = store_match(store, startTimestamp, MATCH_EQUAL);
        if(first == end)
            return UA_STATUSCODE_BADNODATA;
        last = first;
    } else {
        /* Half-open range, as the upstream backend defines it: the end
         * timestamp itself is not deleted. */
        first = store_match(store, startTimestamp, MATCH_EQUAL_OR_AFTER);
        last = store_match(store, endTimestamp, MATCH_BEFORE);
        if(first == end || last == end || first > last)
            return UA_STATUSCODE_BADNODATA;
    }

    store_removeRange(store, first, last);
    return UA_STATUSCODE_GOOD;
}

/* ==================================================== *
 *                   Backend public API                 *
 * ==================================================== */

UA_HistoryDataBackend
pyHistoryBackend_ring(size_t initialNodes, size_t defaultCapacity) {
    UA_HistoryDataBackend backend;
    memset(&backend, 0, sizeof(UA_HistoryDataBackend));

    if(initialNodes == 0)
        initialNodes = PYO6_HISTORY_MAX_NODES_DEFAULT;
    if(defaultCapacity == 0)
        defaultCapacity = PYO6_HISTORY_CAPACITY_DEFAULT;

    PyHistoryRingContext *ctx =
        (PyHistoryRingContext *)UA_calloc(1, sizeof(PyHistoryRingContext));
    if(!ctx)
        return backend; /* context == NULL signals failure */
    ctx->nodes = (PyHistoryNodeStore *)UA_calloc(initialNodes,
                                                sizeof(PyHistoryNodeStore));
    if(!ctx->nodes) {
        UA_free(ctx);
        return backend;
    }
    ctx->nodesCapacity = initialNodes;
    ctx->defaultCapacity = defaultCapacity;
    if(index_grow(ctx, initialNodes * 2) != UA_STATUSCODE_GOOD) {
        UA_free(ctx->nodes);
        UA_free(ctx);
        return backend;
    }

    /* deleteMembers and getHistoryData stay NULL: every node's settings hold a
     * copy of this struct sharing one context, so deleteMembers on a copy would
     * free it under the others, and a NULL getHistoryData keeps the generic
     * paging that the sequence-numbered indices are ordered enough to drive. */
    backend.context = ctx;
    backend.serverSetHistoryData = &serverSetHistoryData_ring;
    backend.getDateTimeMatch = &getDateTimeMatch_ring;
    backend.getEnd = &getEnd_ring;
    backend.lastIndex = &lastIndex_ring;
    backend.firstIndex = &firstIndex_ring;
    backend.resultSize = &resultSize_ring;
    backend.copyDataValues = &copyDataValues_ring;
    backend.getDataValue = &getDataValue_ring;
    backend.boundSupported = &boundSupported_ring;
    backend.timestampsToReturnSupported = &timestampsToReturnSupported_ring;
    backend.insertDataValue = &insertDataValue_ring;
    backend.replaceDataValue = &replaceDataValue_ring;
    backend.updateDataValue = &updateDataValue_ring;
    backend.removeDataValue = &removeDataValue_ring;
    return backend;
}

void
pyHistoryBackend_clear(UA_HistoryDataBackend *backend) {
    if(!backend || !backend->context)
        return;
    PyHistoryRingContext *ctx = (PyHistoryRingContext *)backend->context;
    for(size_t i = 0; i < ctx->nodesSize; ++i)
        store_clear(&ctx->nodes[i]);
    index_clear(&ctx->index);
    UA_free(ctx->nodes);
    UA_free(ctx);
    memset(backend, 0, sizeof(UA_HistoryDataBackend));
}

/* Allocate and index one node's store. Split out so registerNodeId can create
 * one for a node registered without it, rather than depending on call order. */
static UA_StatusCode
ring_addNode(PyHistoryRingContext *ctx, const UA_NodeId *nodeId,
             size_t capacity, UA_Boolean unbounded,
             PyHistoryNodeStore **out) {
    if(ring_find(ctx, nodeId))
        return UA_STATUSCODE_BADNODEIDEXISTS;
    if(ctx->nodesSize >= ctx->nodesCapacity) {
        /* Only the table grows; each store keeps the size it was registered
         * with. Refusing here would fail a server for one Variable too many. */
        size_t grown = ctx->nodesCapacity ? ctx->nodesCapacity * 2 : 8;
        PyHistoryNodeStore *nodes = (PyHistoryNodeStore *)UA_realloc(
            ctx->nodes, grown * sizeof(PyHistoryNodeStore));
        if(!nodes)
            return UA_STATUSCODE_BADOUTOFMEMORY;
        memset(&nodes[ctx->nodesCapacity], 0,
               (grown - ctx->nodesCapacity) * sizeof(PyHistoryNodeStore));
        ctx->nodes = nodes;
        ctx->nodesCapacity = grown;
    }
    /* Reserve first: growing the index can fail, and failing after the store
     * exists would leave one that nothing can look up. */
    UA_StatusCode indexed = index_reserve(ctx);
    if(indexed != UA_STATUSCODE_GOOD)
        return indexed;
    if(capacity == 0)
        capacity = ctx->defaultCapacity;

    PyHistoryNodeStore *store = &ctx->nodes[ctx->nodesSize];
    memset(store, 0, sizeof(PyHistoryNodeStore));
    store->slots = (UA_DataValue *)UA_calloc(capacity, sizeof(UA_DataValue));
    store->stamps = (UA_DateTime *)UA_calloc(capacity, sizeof(UA_DateTime));
    if(!store->slots || !store->stamps) {
        UA_free(store->slots);
        UA_free(store->stamps);
        memset(store, 0, sizeof(PyHistoryNodeStore));
        return UA_STATUSCODE_BADOUTOFMEMORY;
    }
    UA_StatusCode status = UA_NodeId_copy(nodeId, &store->nodeId);
    if(status != UA_STATUSCODE_GOOD) {
        UA_free(store->slots);
        UA_free(store->stamps);
        memset(store, 0, sizeof(PyHistoryNodeStore));
        return status;
    }
    store->hash = UA_NodeId_hash(nodeId);
    store->capacity = capacity;
    store->unbounded = unbounded;
    index_place(&ctx->index, ctx->nodes, ctx->nodesSize);
    ++ctx->nodesSize;
    if(out)
        *out = store;
    return UA_STATUSCODE_GOOD;
}

UA_StatusCode
pyHistoryBackend_addNode(UA_HistoryDataBackend *backend,
                         const UA_NodeId *nodeId, size_t capacity,
                         UA_Boolean unbounded) {
    if(!backend || !backend->context || !nodeId)
        return UA_STATUSCODE_BADINTERNALERROR;
    return ring_addNode((PyHistoryRingContext *)backend->context, nodeId,
                        capacity, unbounded, NULL);
}

UA_StatusCode
pyHistoryBackend_removeNode(UA_HistoryDataBackend *backend,
                            const UA_NodeId *nodeId) {
    if(!backend || !backend->context || !nodeId)
        return UA_STATUSCODE_BADINTERNALERROR;
    PyHistoryRingContext *ctx = (PyHistoryRingContext *)backend->context;
    PyHistoryNodeStore *store = ring_find(ctx, nodeId);
    if(!store)
        return UA_STATUSCODE_BADNODEIDUNKNOWN;

    store_clear(store);
    /* Keep the array dense by moving the last store into the hole. Nothing holds
     * a store pointer across calls; the poll callback looks its own up. */
    PyHistoryNodeStore *last = &ctx->nodes[ctx->nodesSize - 1];
    if(store != last)
        *store = *last;
    memset(last, 0, sizeof(PyHistoryNodeStore));
    --ctx->nodesSize;
    /* The move changed one slot and the removal left a hole probing must not
     * stop at, so rebuild rather than patch. This path is not hot. */
    index_reindex(&ctx->index, ctx->nodes, ctx->nodesSize);
    return UA_STATUSCODE_GOOD;
}

UA_StatusCode
pyHistoryBackend_insert(UA_HistoryDataBackend *backend, const UA_NodeId *nodeId,
                        const UA_DataValue *value) {
    if(!backend || !backend->context || !nodeId || !value)
        return UA_STATUSCODE_BADINTERNALERROR;
    /* The hook HistoryUpdate Insert goes through, so a value pushed locally and
     * one inserted by a client land under identical rules. */
    return insertDataValue_ring(NULL, backend->context, NULL, NULL, nodeId,
                                value);
}

UA_StatusCode
pyHistoryBackend_clearNode(UA_HistoryDataBackend *backend,
                           const UA_NodeId *nodeId) {
    if(!backend || !backend->context || !nodeId)
        return UA_STATUSCODE_BADINTERNALERROR;
    PyHistoryNodeStore *store =
        ring_find((PyHistoryRingContext *)backend->context, nodeId);
    if(!store)
        return UA_STATUSCODE_BADNODEIDUNKNOWN;
    store_clearSamples(store);
    return UA_STATUSCODE_GOOD;
}

UA_StatusCode
pyHistoryBackend_stats(const UA_HistoryDataBackend *backend,
                       const UA_NodeId *nodeId, PyHistoryStats *stats) {
    if(!backend || !backend->context || !nodeId || !stats)
        return UA_STATUSCODE_BADINTERNALERROR;
    const PyHistoryNodeStore *store =
        ring_find((const PyHistoryRingContext *)backend->context, nodeId);
    if(!store)
        return UA_STATUSCODE_BADNODEIDUNKNOWN;

    memset(stats, 0, sizeof(PyHistoryStats));
    stats->capacity = store->capacity;
    stats->count = store->count;
    stats->unbounded = store->unbounded;
    stats->stored = store->stored;
    stats->overwrites = store->overwrites;
    stats->dropped = store->dropped;
    if(store->count > 0) {
        stats->oldest = store_stamp(store, store->firstSeq);
        stats->newest = store_stamp(store, store_end(store) - 1);
    }
    return UA_STATUSCODE_GOOD;
}

UA_StatusCode
pyHistoryBackend_read(const UA_HistoryDataBackend *backend,
                      const UA_NodeId *nodeId, UA_DateTime start,
                      UA_DateTime end, size_t limit, UA_Boolean reverse,
                      UA_DataValue **out, size_t *outSize) {
    if(!backend || !backend->context || !nodeId || !out || !outSize)
        return UA_STATUSCODE_BADINTERNALERROR;
    *out = NULL;
    *outSize = 0;
    if(start > end)
        return UA_STATUSCODE_BADINVALIDARGUMENT;

    const PyHistoryNodeStore *store =
        ring_find((const PyHistoryRingContext *)backend->context, nodeId);
    if(!store)
        return UA_STATUSCODE_BADNODEIDUNKNOWN;
    if(store->count == 0)
        return UA_STATUSCODE_GOOD;

    /* The interval arithmetic of the HistoryRead service; see the header. */
    size_t storeEnd = store_end(store);
    size_t first;
    size_t last;
    if(start == end) {
        first = store_match(store, start, MATCH_EQUAL);
        if(first == storeEnd)
            return UA_STATUSCODE_GOOD;
        last = first;
    } else {
        first = store_match(store, start, MATCH_EQUAL_OR_AFTER);
        last = store_match(store, end, MATCH_BEFORE);
        if(first == storeEnd || last == storeEnd || last < first)
            return UA_STATUSCODE_GOOD;
    }

    size_t count = last - first + 1;
    if(limit > 0 && count > limit) {
        /* Keep the end of the range the caller reads first. */
        if(reverse)
            first = last - limit + 1;
        else
            last = first + limit - 1;
        count = limit;
    }

    UA_DataValue *values =
        (UA_DataValue *)UA_Array_new(count, &UA_TYPES[UA_TYPES_DATAVALUE]);
    if(!values)
        return UA_STATUSCODE_BADOUTOFMEMORY;

    for(size_t i = 0; i < count; ++i) {
        size_t seq = reverse ? last - i : first + i;
        UA_StatusCode status =
            UA_DataValue_copy(store_slot(store, seq), &values[i]);
        if(status != UA_STATUSCODE_GOOD) {
            UA_Array_delete(values, count, &UA_TYPES[UA_TYPES_DATAVALUE]);
            return status;
        }
    }

    *out = values;
    *outSize = count;
    return UA_STATUSCODE_GOOD;
}

/* ==================================================== *
 *                      Gathering                       *
 * ==================================================== */

/* Sample from a polled node's MonitoredItem. The context is the node table
 * rather than the store, because registering a further node can move stores and
 * a MonitoredItem outlives that; upstream hands over the store pointer and then
 * grows the array underneath it. The lookup costs a hash and a mask. */
static void
pollCallback_ring(UA_Server *server, UA_UInt32 monitoredItemId,
                  void *monitoredItemContext, const UA_NodeId *nodeId,
                  void *nodeContext, UA_UInt32 attributeId,
                  const UA_DataValue *value) {
    (void)server;
    (void)monitoredItemId;
    (void)nodeContext;
    (void)attributeId;
    PyHistoryNodeStore *store =
        ring_find((PyHistoryRingContext *)monitoredItemContext, nodeId);
    /* Pausing stops a polled node too. Upstream consults its pause flag on the
     * write path only, so a paused polled node keeps recording there. */
    if(!store || !store->registered || store->paused)
        return;
    store_record(store, value);
}

static UA_StatusCode
registerNodeId_ring(UA_Server *server, void *context, const UA_NodeId *nodeId,
                    const UA_HistorizingNodeIdSettings setting) {
    (void)server;
    PyHistoryRingContext *ctx = (PyHistoryRingContext *)context;
    if(!ctx || !nodeId)
        return UA_STATUSCODE_BADINTERNALERROR;

    PyHistoryNodeStore *store = ring_find(ctx, nodeId);
    if(store && store->registered)
        return UA_STATUSCODE_BADNODEIDEXISTS;
    if(!store) {
        /* Only for a caller that went straight to the gathering; the facade
         * sizes the store first. */
        UA_StatusCode status = ring_addNode(ctx, nodeId, 0, false, &store);
        if(status != UA_STATUSCODE_GOOD)
            return status;
    }

    store->setting = setting;
    store->paused = false;
    store->registered = true;
    return UA_STATUSCODE_GOOD;
}

static const UA_HistorizingNodeIdSettings *
getHistorizingSetting_ring(UA_Server *server, void *context,
                           const UA_NodeId *nodeId) {
    (void)server;
    PyHistoryNodeStore *store =
        ring_find((PyHistoryRingContext *)context, nodeId);
    if(!store || !store->registered)
        return NULL;
    /* Valid until the next registration moves the table - the same contract
     * upstream's gathering offers, and the database holds it for one call. */
    return &store->setting;
}

static UA_StatusCode
startPoll_ring(UA_Server *server, void *context, const UA_NodeId *nodeId) {
    PyHistoryRingContext *ctx = (PyHistoryRingContext *)context;
    PyHistoryNodeStore *store = ring_find(ctx, nodeId);
    if(!store || !store->registered)
        return UA_STATUSCODE_BADNODEIDUNKNOWN;
    if(store->setting.historizingUpdateStrategy !=
       UA_HISTORIZINGUPDATESTRATEGY_POLL)
        return UA_STATUSCODE_BADNODEIDINVALID;
    if(store->monitoredResult.monitoredItemId > 0)
        return UA_STATUSCODE_BADMONITOREDITEMIDINVALID;

    /* Aliases `nodeId` rather than copying, as upstream does. */
    UA_MonitoredItemCreateRequest request =
        UA_MonitoredItemCreateRequest_default(*nodeId);
    request.requestedParameters.samplingInterval =
        (UA_Double)store->setting.pollingInterval;
    request.monitoringMode = UA_MONITORINGMODE_REPORTING;

    store->monitoredResult = UA_Server_createDataChangeMonitoredItem(
        server, UA_TIMESTAMPSTORETURN_BOTH, request, ctx, &pollCallback_ring);
    return store->monitoredResult.statusCode;
}

static UA_StatusCode
stopPoll_ring(UA_Server *server, void *context, const UA_NodeId *nodeId) {
    PyHistoryNodeStore *store =
        ring_find((PyHistoryRingContext *)context, nodeId);
    if(!store || !store->registered)
        return UA_STATUSCODE_BADNODEIDUNKNOWN;
    if(store->setting.historizingUpdateStrategy !=
       UA_HISTORIZINGUPDATESTRATEGY_POLL)
        return UA_STATUSCODE_BADNODEIDINVALID;
    if(store->monitoredResult.monitoredItemId == 0)
        return UA_STATUSCODE_BADMONITOREDITEMIDINVALID;

    UA_StatusCode status = UA_Server_deleteMonitoredItem(
        server, store->monitoredResult.monitoredItemId);
    /* Cleared either way: the result owns a filterResult, and one that could
     * not be deleted is not one this store can keep claiming. */
    UA_MonitoredItemCreateResult_clear(&store->monitoredResult);
    return status;
}

static UA_Boolean
updateNodeIdSetting_ring(UA_Server *server, void *context,
                         const UA_NodeId *nodeId,
                         const UA_HistorizingNodeIdSettings setting) {
    PyHistoryNodeStore *store =
        ring_find((PyHistoryRingContext *)context, nodeId);
    if(!store || !store->registered)
        return false;
    /* The old settings own the poll; drop it before they are replaced. */
    if(store->monitoredResult.monitoredItemId > 0)
        stopPoll_ring(server, context, nodeId);
    store->setting = setting;
    return true;
}

/* Called on every Write to every Variable, historized or not: the history
 * database's setValue hook is unconditional. */
static void
setValue_ring(UA_Server *server, void *context, const UA_NodeId *sessionId,
              void *sessionContext, const UA_NodeId *nodeId,
              UA_Boolean historizing, const UA_DataValue *value) {
    (void)server;
    (void)sessionId;
    (void)sessionContext;
    /* A node without the attribute records nothing and readRaw refuses it, so
     * answer before the lookup - on a real address space that is most calls. */
    if(!historizing)
        return;

    PyHistoryNodeStore *store =
        ring_find((PyHistoryRingContext *)context, nodeId);
    if(!store || !store->registered || store->paused)
        return;
    if(store->setting.historizingUpdateStrategy !=
       UA_HISTORIZINGUPDATESTRATEGY_VALUESET)
        return;
    store_record(store, value);
}

/* The table belongs to the backend; see PyServerHistory in server_history.h. */
static void
deleteMembers_ring(UA_HistoryDataGathering *gathering) {
    if(gathering)
        memset(gathering, 0, sizeof(UA_HistoryDataGathering));
}

UA_HistoryDataGathering
pyHistoryGathering_ring(const UA_HistoryDataBackend *backend) {
    UA_HistoryDataGathering gathering;
    memset(&gathering, 0, sizeof(UA_HistoryDataGathering));
    if(!backend || !backend->context)
        return gathering; /* context == NULL signals failure */

    gathering.context = backend->context;
    gathering.registerNodeId = &registerNodeId_ring;
    gathering.getHistorizingSetting = &getHistorizingSetting_ring;
    gathering.startPoll = &startPoll_ring;
    gathering.stopPoll = &stopPoll_ring;
    gathering.updateNodeIdSetting = &updateNodeIdSetting_ring;
    gathering.setValue = &setValue_ring;
    gathering.deleteMembers = &deleteMembers_ring;
    return gathering;
}

UA_StatusCode
pyHistoryGathering_setPaused(UA_HistoryDataGathering *gathering,
                             const UA_NodeId *nodeId, UA_Boolean paused) {
    if(!gathering || !gathering->context || !nodeId)
        return UA_STATUSCODE_BADINTERNALERROR;
    PyHistoryNodeStore *store =
        ring_find((PyHistoryRingContext *)gathering->context, nodeId);
    if(!store || !store->registered)
        return UA_STATUSCODE_BADNODEIDUNKNOWN;
    store->paused = paused;
    return UA_STATUSCODE_GOOD;
}

UA_StatusCode
pyHistoryGathering_stopPolls(UA_HistoryDataGathering *gathering,
                             UA_Server *server) {
    if(!gathering || !gathering->context)
        return UA_STATUSCODE_BADINTERNALERROR;
    if(!server)
        return UA_STATUSCODE_GOOD; /* the MonitoredItems went with it */

    PyHistoryRingContext *ctx = (PyHistoryRingContext *)gathering->context;
    UA_StatusCode result = UA_STATUSCODE_GOOD;
    for(size_t i = 0; i < ctx->nodesSize; ++i) {
        PyHistoryNodeStore *store = &ctx->nodes[i];
        if(store->monitoredResult.monitoredItemId == 0)
            continue;
        UA_StatusCode status = UA_Server_deleteMonitoredItem(
            server, store->monitoredResult.monitoredItemId);
        UA_MonitoredItemCreateResult_clear(&store->monitoredResult);
        if(status != UA_STATUSCODE_GOOD && result == UA_STATUSCODE_GOOD)
            result = status;
    }
    return result;
}

/* ==================================================== *
 *          HistoryRead/HistoryUpdate fixups             *
 * ==================================================== */

/* Tracks the one continuation point currently valid to resume a HistoryRead
 * with, per (session, node) */
typedef struct {
    UA_NodeId sessionId;
    UA_NodeId nodeId;
    UA_ByteString expectedCp;
} PyHistoryCpEntry;

typedef struct {
    PyHistoryCpEntry *entries;
    size_t size;
} PyHistoryCpTrack;

static PyHistoryCpEntry *
cpTrack_find(PyHistoryCpTrack *track, const UA_NodeId *sessionId, const UA_NodeId *nodeId) {
    for(size_t i = 0; i < track->size; i++) {
        if(UA_NodeId_equal(&track->entries[i].sessionId, sessionId) &&
           UA_NodeId_equal(&track->entries[i].nodeId, nodeId))
            return &track->entries[i];
    }
    return NULL;
}

static void
cpTrack_clearEntry(PyHistoryCpEntry *entry) {
    UA_NodeId_clear(&entry->sessionId);
    UA_NodeId_clear(&entry->nodeId);
    UA_ByteString_clear(&entry->expectedCp);
}

/* No-op if nothing was tracked for (sessionId, nodeId). */
static void
cpTrack_remove(PyHistoryCpTrack *track, const UA_NodeId *sessionId, const UA_NodeId *nodeId) {
    PyHistoryCpEntry *entry = cpTrack_find(track, sessionId, nodeId);
    if(!entry)
        return;
    cpTrack_clearEntry(entry);
    *entry = track->entries[--track->size]; /* swap-with-last, shrink */
}

/* Allocation failure just means a later legitimate resume gets wrongly
 * rejected instead of silently accepting anything - never unsafe - so
 * there is nothing useful to report back to the caller. */
static void
cpTrack_set(PyHistoryCpTrack *track, const UA_NodeId *sessionId, const UA_NodeId *nodeId,
           const UA_ByteString *cp) {
    UA_ByteString copy;
    if(UA_ByteString_copy(cp, &copy) != UA_STATUSCODE_GOOD)
        return;

    PyHistoryCpEntry *entry = cpTrack_find(track, sessionId, nodeId);
    if(entry) {
        UA_ByteString_clear(&entry->expectedCp);
        entry->expectedCp = copy;
        return;
    }

    PyHistoryCpEntry *grown = (PyHistoryCpEntry *)
        UA_realloc(track->entries, (track->size + 1) * sizeof(PyHistoryCpEntry));
    if(!grown) {
        UA_ByteString_clear(&copy);
        return;
    }
    track->entries = grown;
    entry = &track->entries[track->size];
    UA_NodeId_init(&entry->sessionId);
    UA_NodeId_init(&entry->nodeId);
    if(UA_NodeId_copy(sessionId, &entry->sessionId) != UA_STATUSCODE_GOOD ||
       UA_NodeId_copy(nodeId, &entry->nodeId) != UA_STATUSCODE_GOOD) {
        cpTrack_clearEntry(entry);
        UA_ByteString_clear(&copy);
        return;
    }
    entry->expectedCp = copy;
    track->size++;
}

static void
cpTrack_clear(PyHistoryCpTrack *track) {
    for(size_t i = 0; i < track->size; i++)
        cpTrack_clearEntry(&track->entries[i]);
    UA_free(track->entries);
    track->entries = NULL;
    track->size = 0;
}

typedef struct {
    UA_HistoryDatabase inner;
    PyHistoryCpTrack cpTrack;
} PyHistoryDatabaseFixup;

static void
pyHistoryFixup_clear(UA_HistoryDatabase *hdb) {
    if(!hdb || !hdb->context)
        return;
    PyHistoryDatabaseFixup *fixup = (PyHistoryDatabaseFixup *)hdb->context;
    cpTrack_clear(&fixup->cpTrack);
    if(fixup->inner.clear)
        fixup->inner.clear(&fixup->inner);
    UA_free(fixup);
}

static void
pyHistoryFixup_setValue(UA_Server *server, void *context, const UA_NodeId *sessionId,
                        void *sessionContext, const UA_NodeId *nodeId,
                        UA_Boolean historizing, const UA_DataValue *value) {
    PyHistoryDatabaseFixup *fixup = (PyHistoryDatabaseFixup *)context;
    fixup->inner.setValue(server, fixup->inner.context, sessionId, sessionContext,
                          nodeId, historizing, value);
}

static void
historyReadRequestFail(UA_HistoryReadResponse *response, UA_StatusCode serviceResult) {
    response->responseHeader.serviceResult = serviceResult;
    UA_Array_delete(response->results, response->resultsSize,
                    &UA_TYPES[UA_TYPES_HISTORYREADRESULT]);
    response->results = NULL;
    response->resultsSize = 0;
}

/* A continuation point is only ever legal to resume with once (see
 * PyHistoryCpTrack); a fresh read (no continuation point given) always
 * starts over, discarding whatever was tracked before. */
static UA_StatusCode
historyCheckContinuationPoint(PyHistoryCpTrack *track, const UA_NodeId *sessionId,
                              const UA_NodeId *nodeId, const UA_ByteString *providedCp) {
    if(providedCp->length == 0)
        return UA_STATUSCODE_GOOD;
    PyHistoryCpEntry *entry = cpTrack_find(track, sessionId, nodeId);
    if(!entry || !UA_ByteString_equal(&entry->expectedCp, providedCp))
        return UA_STATUSCODE_BADCONTINUATIONPOINTINVALID;
    return UA_STATUSCODE_GOOD;
}

static void
historyFilterOutOfWindow(UA_HistoryData *hd, UA_Boolean dropOutOfWindow,
                         UA_DateTime windowLo, UA_DateTime windowHi) {
    UA_DataValue *values = hd->dataValues;
    size_t kept = 0;
    for(size_t j = 0; j < hd->dataValuesSize; j++) {
        UA_Boolean isPhantom = !values[j].hasValue && !values[j].hasStatus &&
                               !values[j].hasSourceTimestamp && !values[j].hasServerTimestamp;
        UA_Boolean isOutOfWindow = dropOutOfWindow && values[j].hasSourceTimestamp &&
                                   (values[j].sourceTimestamp < windowLo ||
                                    values[j].sourceTimestamp > windowHi);
        if(isPhantom || isOutOfWindow) {
            UA_DataValue_clear(&values[j]);
            continue;
        }
        if(kept != j)
            values[kept] = values[j];
        kept++;
    }
    hd->dataValuesSize = kept;
}

static UA_Boolean
historyWindowExhausted(const UA_HistoryData *hd, UA_Boolean descending,
                       UA_DateTime windowLo, UA_DateTime windowHi) {
    size_t count = hd->dataValuesSize;
    if(count == 0)
        return false;
    const UA_DataValue *last = &hd->dataValues[count - 1];
    if(!last->hasSourceTimestamp)
        return false; /* nothing to compare - trust the delegate's own answer */
    return descending ? last->sourceTimestamp <= windowLo : last->sourceTimestamp >= windowHi;
}

static void
pyHistoryFixup_readRaw(UA_Server *server, void *context, const UA_NodeId *sessionId,
                       void *sessionContext, const UA_RequestHeader *requestHeader,
                       const UA_ReadRawModifiedDetails *historyReadDetails,
                       UA_TimestampsToReturn timestampsToReturn,
                       UA_Boolean releaseContinuationPoints, size_t nodesToReadSize,
                       const UA_HistoryReadValueId *nodesToRead,
                       UA_HistoryReadResponse *response,
                       UA_HistoryData * const * const historyData) {
    PyHistoryDatabaseFixup *fixup = (PyHistoryDatabaseFixup *)context;

    if(timestampsToReturn != UA_TIMESTAMPSTORETURN_SOURCE &&
       timestampsToReturn != UA_TIMESTAMPSTORETURN_SERVER &&
       timestampsToReturn != UA_TIMESTAMPSTORETURN_BOTH) {
        historyReadRequestFail(response, UA_STATUSCODE_BADTIMESTAMPSTORETURNINVALID);
        return;
    }

    /* OPC UA Part 11 SS6.4.3.2: 2 of {StartTime, EndTime, NumValuesPerNode}. */
    int paramsSet = (historyReadDetails->startTime != 0) +
                    (historyReadDetails->endTime != 0) +
                    (historyReadDetails->numValuesPerNode != 0);
    if(paramsSet < 2) {
        historyReadRequestFail(response, UA_STATUSCODE_BADHISTORYOPERATIONINVALID);
        return;
    }

    UA_Boolean bothBoundsGiven =
        historyReadDetails->startTime != 0 && historyReadDetails->endTime != 0;
    UA_Boolean descending =
        bothBoundsGiven && historyReadDetails->startTime > historyReadDetails->endTime;
    UA_DateTime windowLo = 0, windowHi = 0;
    if(bothBoundsGiven) {
        windowLo = descending ? historyReadDetails->endTime : historyReadDetails->startTime;
        windowHi = descending ? historyReadDetails->startTime : historyReadDetails->endTime;
    }

    UA_ReadRawModifiedDetails fixedDetails = *historyReadDetails;
    if(fixedDetails.startTime == 0)
        fixedDetails.startTime = LLONG_MIN;
    if(fixedDetails.endTime == 0)
        fixedDetails.endTime = LLONG_MIN;

    /* The real per-node status, captured before the delegate discards it. */
    UA_StatusCode *nodeStatus =
        (UA_StatusCode *)UA_malloc(nodesToReadSize * sizeof(UA_StatusCode));
    if(!nodeStatus) {
        response->responseHeader.serviceResult = UA_STATUSCODE_BADOUTOFMEMORY;
        return;
    }
    for(size_t i = 0; i < nodesToReadSize; i++) {
        UA_Byte accessLevel = 0;
        nodeStatus[i] = UA_Server_readAccessLevel(server, nodesToRead[i].nodeId, &accessLevel);
        if(nodeStatus[i] == UA_STATUSCODE_GOOD && (accessLevel & UA_ACCESSLEVELMASK_HISTORYREAD)) {
            UA_Boolean historizing = false;
            UA_Server_readHistorizing(server, nodesToRead[i].nodeId, &historizing);
            if(!historizing)
                nodeStatus[i] = UA_STATUSCODE_BADHISTORYOPERATIONINVALID;
        }
        if(nodeStatus[i] == UA_STATUSCODE_GOOD)
            nodeStatus[i] = historyCheckContinuationPoint(&fixup->cpTrack, sessionId,
                                                          &nodesToRead[i].nodeId,
                                                          &nodesToRead[i].continuationPoint);
    }

    fixup->inner.readRaw(server, fixup->inner.context, sessionId, sessionContext,
                         requestHeader, &fixedDetails, timestampsToReturn,
                         releaseContinuationPoints, nodesToReadSize, nodesToRead,
                         response, historyData);

    for(size_t i = 0; i < nodesToReadSize; i++) {
        if(nodeStatus[i] == UA_STATUSCODE_GOOD)
            continue;
        response->results[i].statusCode = nodeStatus[i];
        if(nodeStatus[i] == UA_STATUSCODE_BADCONTINUATIONPOINTINVALID) {
            UA_Array_delete(historyData[i]->dataValues, historyData[i]->dataValuesSize,
                            &UA_TYPES[UA_TYPES_DATAVALUE]);
            historyData[i]->dataValues = NULL;
            historyData[i]->dataValuesSize = 0;
            UA_ByteString_clear(&response->results[i].continuationPoint);
        }
    }

    UA_Boolean dropOutOfWindow = bothBoundsGiven && !historyReadDetails->returnBounds;
    for(size_t i = 0; i < nodesToReadSize; i++) {
        if(response->results[i].statusCode == UA_STATUSCODE_GOOD)
            historyFilterOutOfWindow(historyData[i], dropOutOfWindow, windowLo, windowHi);
    }

    for(size_t i = 0; i < nodesToReadSize; i++) {
        if(nodeStatus[i] != UA_STATUSCODE_GOOD)
            continue;
        UA_Boolean forget = releaseContinuationPoints || !bothBoundsGiven ||
                           response->results[i].continuationPoint.length == 0 ||
                           historyWindowExhausted(historyData[i], descending, windowLo, windowHi);
        if(forget) {
            UA_ByteString_clear(&response->results[i].continuationPoint);
            cpTrack_remove(&fixup->cpTrack, sessionId, &nodesToRead[i].nodeId);
        } else {
            cpTrack_set(&fixup->cpTrack, sessionId, &nodesToRead[i].nodeId,
                       &response->results[i].continuationPoint);
        }
    }
    UA_free(nodeStatus);

    for(size_t i = 0; i < nodesToReadSize; i++) {
        if(response->results[i].statusCode != UA_STATUSCODE_GOOD)
            continue;

        UA_DataValue *values = historyData[i]->dataValues;
        size_t count = historyData[i]->dataValuesSize;
        if(count == 0) {
            if(!releaseContinuationPoints)
                response->results[i].statusCode = UA_STATUSCODE_GOODNODATA;
            continue;
        }

        UA_Boolean allIndexRangeNoData = true;
        for(size_t j = 0; j < count; j++) {
            if(timestampsToReturn == UA_TIMESTAMPSTORETURN_SOURCE)
                values[j].hasServerTimestamp = false;
            else if(timestampsToReturn == UA_TIMESTAMPSTORETURN_SERVER)
                values[j].hasSourceTimestamp = false;
            if(!(values[j].hasStatus && values[j].status == UA_STATUSCODE_BADINDEXRANGENODATA))
                allIndexRangeNoData = false;
        }

        if(allIndexRangeNoData) {
            response->results[i].statusCode = UA_STATUSCODE_BADINDEXRANGENODATA;
            UA_Array_delete(values, count, &UA_TYPES[UA_TYPES_DATAVALUE]);
            historyData[i]->dataValues = NULL;
            historyData[i]->dataValuesSize = 0;
        }
    }
}

static void
pyHistoryFixup_readModified(UA_Server *server, void *context, const UA_NodeId *sessionId,
                            void *sessionContext, const UA_RequestHeader *requestHeader,
                            const UA_ReadRawModifiedDetails *historyReadDetails,
                            UA_TimestampsToReturn timestampsToReturn,
                            UA_Boolean releaseContinuationPoints, size_t nodesToReadSize,
                            const UA_HistoryReadValueId *nodesToRead,
                            UA_HistoryReadResponse *response,
                            UA_HistoryModifiedData * const * const historyData) {
    if(historyReadDetails->returnBounds) {
        for(size_t i = 0; i < nodesToReadSize; i++)
            response->results[i].statusCode = UA_STATUSCODE_BADINVALIDARGUMENT;
        return;
    }

    UA_HistoryData *raw = (UA_HistoryData *)UA_calloc(nodesToReadSize, sizeof(UA_HistoryData));
    if(!raw) {
        response->responseHeader.serviceResult = UA_STATUSCODE_BADOUTOFMEMORY;
        return;
    }
    UA_HistoryData **rawPtrs =
        (UA_HistoryData **)UA_malloc(nodesToReadSize * sizeof(UA_HistoryData *));
    if(!rawPtrs) {
        UA_free(raw);
        response->responseHeader.serviceResult = UA_STATUSCODE_BADOUTOFMEMORY;
        return;
    }
    for(size_t i = 0; i < nodesToReadSize; i++)
        rawPtrs[i] = &raw[i];

    pyHistoryFixup_readRaw(server, context, sessionId, sessionContext, requestHeader,
                           historyReadDetails, timestampsToReturn, releaseContinuationPoints,
                           nodesToReadSize, nodesToRead, response,
                           (UA_HistoryData * const * const)rawPtrs);

    if(response->resultsSize == nodesToReadSize) {
        for(size_t i = 0; i < nodesToReadSize; i++) {
            historyData[i]->dataValuesSize = raw[i].dataValuesSize;
            historyData[i]->dataValues = raw[i].dataValues; /* ownership moves */
            raw[i].dataValuesSize = 0;
            raw[i].dataValues = NULL;
        }
    }
    for(size_t i = 0; i < nodesToReadSize; i++)
        UA_HistoryData_clear(&raw[i]); /* no-op wherever ownership already moved out */
    UA_free(rawPtrs);
    UA_free(raw);
}

static void
pyHistoryFixup_updateData(UA_Server *server, void *context, const UA_NodeId *sessionId,
                          void *sessionContext, const UA_RequestHeader *requestHeader,
                          const UA_UpdateDataDetails *details, UA_HistoryUpdateResult *result) {
    PyHistoryDatabaseFixup *fixup = (PyHistoryDatabaseFixup *)context;
    UA_Byte accessLevel = 0;
    UA_StatusCode nodeStatus = UA_Server_readAccessLevel(server, details->nodeId, &accessLevel);
    fixup->inner.updateData(server, fixup->inner.context, sessionId, sessionContext,
                            requestHeader, details, result);
    if(nodeStatus != UA_STATUSCODE_GOOD)
        result->statusCode = nodeStatus;
}

static void
pyHistoryFixup_deleteRawModified(UA_Server *server, void *context, const UA_NodeId *sessionId,
                                 void *sessionContext, const UA_RequestHeader *requestHeader,
                                 const UA_DeleteRawModifiedDetails *details,
                                 UA_HistoryUpdateResult *result) {
    PyHistoryDatabaseFixup *fixup = (PyHistoryDatabaseFixup *)context;
    UA_Byte accessLevel = 0;
    UA_StatusCode nodeStatus = UA_Server_readAccessLevel(server, details->nodeId, &accessLevel);
    fixup->inner.deleteRawModified(server, fixup->inner.context, sessionId, sessionContext,
                                   requestHeader, details, result);
    if(nodeStatus != UA_STATUSCODE_GOOD)
        result->statusCode = nodeStatus;
}

static UA_HistoryDatabase
pyHistoryDatabase_fixupNodeIdOrder(UA_HistoryDatabase inner) {
    if(!inner.context)
        return inner;

    PyHistoryDatabaseFixup *fixup =
        (PyHistoryDatabaseFixup *)UA_calloc(1, sizeof(PyHistoryDatabaseFixup));
    if(!fixup) {
        inner.context = NULL;
        return inner;
    }
    fixup->inner = inner;

    UA_HistoryDatabase wrapped;
    memset(&wrapped, 0, sizeof(wrapped));
    wrapped.context = fixup;
    wrapped.clear = pyHistoryFixup_clear;
    wrapped.setValue = inner.setValue ? pyHistoryFixup_setValue : NULL;
    wrapped.readRaw = inner.readRaw ? pyHistoryFixup_readRaw : NULL;
    wrapped.readModified = inner.readRaw ? pyHistoryFixup_readModified : NULL;
    wrapped.updateData = inner.updateData ? pyHistoryFixup_updateData : NULL;
    wrapped.deleteRawModified =
        inner.deleteRawModified ? pyHistoryFixup_deleteRawModified : NULL;
    return wrapped;
}

/* ==================================================== *
 *                  Server-side facade                  *
 * ==================================================== */

void
pyHistory_init(PyServerHistory *history) {
    if(!history)
        return;
    memset(history, 0, sizeof(PyServerHistory));
}

UA_Boolean
pyHistory_enabled(const PyServerHistory *history) {
    return history && history->enabled;
}

/* Write one HistoryServerCapabilities Variable through the admin session. */
static void
history_writeCapability(UA_Server *server, UA_UInt32 nodeId, void *value,
                        const UA_DataType *type) {
    UA_Variant variant;
    UA_Variant_setScalar(&variant, value, type);
    /* Aliases the caller's stack slot; the write deep-copies and the variant is
     * never cleared, so nothing here owns heap memory. */
    UA_Server_writeValue(server, UA_NODEID_NUMERIC(0, nodeId), variant);
}

/* Fill in Server.ServerCapabilities.HistoryServerCapabilities */
static void
history_advertiseCapabilities(UA_Server *server, UA_ServerConfig *config,
                              size_t maxResponseSize) {
    UA_Boolean yes = true;
    UA_UInt32 maxValues = (UA_UInt32)maxResponseSize;

    config->accessHistoryDataCapability = true;
    config->maxReturnDataValues = maxValues;
    config->insertDataCapability = true;
    config->replaceDataCapability = true;
    config->updateDataCapability = true;
    config->deleteRawCapability = true;

    history_writeCapability(
        server, UA_NS0ID_HISTORYSERVERCAPABILITIES_ACCESSHISTORYDATACAPABILITY,
        &yes, &UA_TYPES[UA_TYPES_BOOLEAN]);
    history_writeCapability(
        server, UA_NS0ID_HISTORYSERVERCAPABILITIES_INSERTDATACAPABILITY, &yes,
        &UA_TYPES[UA_TYPES_BOOLEAN]);
    history_writeCapability(
        server, UA_NS0ID_HISTORYSERVERCAPABILITIES_REPLACEDATACAPABILITY, &yes,
        &UA_TYPES[UA_TYPES_BOOLEAN]);
    history_writeCapability(
        server, UA_NS0ID_HISTORYSERVERCAPABILITIES_UPDATEDATACAPABILITY, &yes,
        &UA_TYPES[UA_TYPES_BOOLEAN]);
    history_writeCapability(
        server, UA_NS0ID_HISTORYSERVERCAPABILITIES_DELETERAWCAPABILITY, &yes,
        &UA_TYPES[UA_TYPES_BOOLEAN]);
    /* 0 would mean "no limit", which is not what a paged backend does. */
    history_writeCapability(
        server, UA_NS0ID_HISTORYSERVERCAPABILITIES_MAXRETURNDATAVALUES,
        &maxValues, &UA_TYPES[UA_TYPES_UINT32]);
}

UA_StatusCode
pyHistory_enable(PyServerHistory *history, UA_Server *server,
                 UA_ServerConfig *config, size_t initialNodes,
                 size_t defaultCapacity, size_t defaultResponseSize) {
    if(!history || !server || !config)
        return UA_STATUSCODE_BADINTERNALERROR;
    if(history->enabled)
        return UA_STATUSCODE_BADINVALIDSTATE;

    if(initialNodes == 0)
        initialNodes = PYO6_HISTORY_MAX_NODES_DEFAULT;
    if(defaultCapacity == 0)
        defaultCapacity = PYO6_HISTORY_CAPACITY_DEFAULT;
    if(defaultResponseSize == 0)
        defaultResponseSize = PYO6_HISTORY_RESPONSE_DEFAULT;

    UA_HistoryDataBackend backend =
        pyHistoryBackend_ring(initialNodes, defaultCapacity);
    if(!backend.context)
        return UA_STATUSCODE_BADOUTOFMEMORY;

    /* A second view of the backend's table, which grows, so one Variable too
     * many never turns into a startup failure. */
    UA_HistoryDataGathering gathering = pyHistoryGathering_ring(&backend);

    UA_HistoryDatabase database = UA_HistoryDatabase_default(gathering);
    //Check if valid NodeId
    database = pyHistoryDatabase_fixupNodeIdOrder(database);
    if(!database.context) {
        pyHistoryBackend_clear(&backend);
        return UA_STATUSCODE_BADOUTOFMEMORY;
    }

    /* The wrapper belongs to the config now; the table stays ours. */
    config->historyDatabase = database;
    history->gathering = gathering;
    history->backend = backend;
    history->initialNodes = initialNodes;
    history->defaultCapacity = defaultCapacity;
    history->defaultResponseSize = defaultResponseSize;
    history->enabled = true;

    history_advertiseCapabilities(server, config, defaultResponseSize);
    return UA_STATUSCODE_GOOD;
}

UA_StatusCode
pyHistory_enableCustom(PyServerHistory *history, UA_Server *server,
                       UA_ServerConfig *config, void *pyBackend,
                       void *pyServer, size_t initialNodes,
                       size_t defaultResponseSize) {
    if(!history || !server || !config || !pyBackend || !pyServer)
        return UA_STATUSCODE_BADINTERNALERROR;
    if(history->enabled)
        return UA_STATUSCODE_BADINVALIDSTATE;

    if(initialNodes == 0)
        initialNodes = PYO6_HISTORY_MAX_NODES_DEFAULT;
    if(defaultResponseSize == 0)
        defaultResponseSize = PYO6_HISTORY_RESPONSE_DEFAULT;

    /* Built in server_history_python.c */
    UA_HistoryDataBackend backend = pyHistoryBackend_python(pyBackend, pyServer);
    if(!backend.context)
        return UA_STATUSCODE_BADINTERNALERROR;

    /* Upstream's own generic gathering */
    UA_HistoryDataGathering gathering = UA_HistoryDataGathering_Default(initialNodes);
    if(!gathering.context) {
        backend.deleteMembers(&backend);
        return UA_STATUSCODE_BADOUTOFMEMORY;
    }

    UA_HistoryDatabase database = UA_HistoryDatabase_default(gathering);
    //Check if valid NodeId
    database = pyHistoryDatabase_fixupNodeIdOrder(database);
    if(!database.context) {
        gathering.deleteMembers(&gathering);
        backend.deleteMembers(&backend);
        return UA_STATUSCODE_BADOUTOFMEMORY;
    }

    config->historyDatabase = database;
    history->gathering = gathering;
    history->backend = backend;
    history->initialNodes = initialNodes;
    history->defaultCapacity = 0; /* meaningless without a ring; never read */
    history->defaultResponseSize = defaultResponseSize;
    history->enabled = true;
    history->customBackend = true;

    /* HistoryServerCapabilities is the user's own responsibility with a
     * custom backend - o6 does not infer what it implements. */
    config->accessHistoryDataCapability = true;
    config->maxReturnDataValues = (UA_UInt32)defaultResponseSize;
    return UA_STATUSCODE_GOOD;
}

/* customBackend mode only: upstream's UA_HistoryDataGathering_Default has no
 * "enumerate registered nodes" primitive, so this is the side-list
 * pyHistory_stopPolls walks at shutdown. Doubling growth, same idiom as
 * ring_addNode. Does nothing on OOM other than fail the caller - a poll that
 * cannot be tracked is rolled back by the caller the same as any other
 * registration failure. */
static UA_StatusCode
historyPolledNodes_add(PyServerHistory *history, const UA_NodeId *nodeId) {
    if(history->polledNodesSize >= history->polledNodesCapacity) {
        size_t grown = history->polledNodesCapacity ? history->polledNodesCapacity * 2 : 8;
        UA_NodeId *grownArray = (UA_NodeId *)UA_realloc(
            history->polledNodes, grown * sizeof(UA_NodeId));
        if(!grownArray)
            return UA_STATUSCODE_BADOUTOFMEMORY;
        history->polledNodes = grownArray;
        history->polledNodesCapacity = grown;
    }
    UA_StatusCode status = UA_NodeId_copy(
        nodeId, &history->polledNodes[history->polledNodesSize]);
    if(status != UA_STATUSCODE_GOOD)
        return status;
    ++history->polledNodesSize;
    return UA_STATUSCODE_GOOD;
}

static void
historyPolledNodes_remove(PyServerHistory *history, const UA_NodeId *nodeId) {
    for(size_t i = 0; i < history->polledNodesSize; ++i) {
        if(!UA_NodeId_equal(&history->polledNodes[i], nodeId))
            continue;
        UA_NodeId_clear(&history->polledNodes[i]);
        /* Keep the array dense by moving the last entry into the hole. */
        --history->polledNodesSize;
        if(i != history->polledNodesSize)
            history->polledNodes[i] = history->polledNodes[history->polledNodesSize];
        return;
    }
}

UA_StatusCode
pyHistory_register(PyServerHistory *history, UA_Server *server,
                   const UA_NodeId *nodeId, size_t capacity,
                   UA_Boolean unbounded, size_t maxResponseSize,
                   UA_HistorizingUpdateStrategy strategy,
                   size_t pollingIntervalMs) {
    if(!history || !server || !nodeId)
        return UA_STATUSCODE_BADINTERNALERROR;
    if(!history->enabled)
        return UA_STATUSCODE_BADINVALIDSTATE;

    if(maxResponseSize == 0)
        maxResponseSize = history->defaultResponseSize;

    UA_StatusCode status;
    if(history->customBackend) {
        /* capacity has no meaning without a ring to size - the caller
         * (server_nodes.c) rejects a non-default one before this point, this
         * is just belt-and-suspenders for any future direct caller. */
        if(capacity != 0 || unbounded)
            return UA_STATUSCODE_BADNOTSUPPORTED;
        status = UA_STATUSCODE_GOOD;
    } else {
        /* For a growing store `capacity` is the initial allocation, not a cap. */
        if(capacity == 0)
            capacity = history->defaultCapacity;
        status = pyHistoryBackend_addNode(&history->backend, nodeId, capacity, unbounded);
        if(status != UA_STATUSCODE_GOOD)
            return status;
    }

    UA_HistorizingNodeIdSettings setting;
    memset(&setting, 0, sizeof(UA_HistorizingNodeIdSettings));
    /* A copy sharing this server's one context, which the facade owns -
     * ring mode shares the ring's node table, customBackend mode shares the
     * one Python HistoryBackend instance. */
    setting.historizingBackend = history->backend;
    setting.maxHistoryDataResponseSize = maxResponseSize;
    setting.historizingUpdateStrategy = strategy;
    setting.pollingInterval = pollingIntervalMs;

    status = history->gathering.registerNodeId(server, history->gathering.context,
                                               nodeId, setting);
    if(status != UA_STATUSCODE_GOOD) {
        if(!history->customBackend)
            pyHistoryBackend_removeNode(&history->backend, nodeId);
        return status;
    }

    if(strategy == UA_HISTORIZINGUPDATESTRATEGY_POLL) {
        if(history->customBackend) {
            status = historyPolledNodes_add(history, nodeId);
            if(status != UA_STATUSCODE_GOOD)
                return status;
        }
        status = history->gathering.startPoll(server, history->gathering.context,
                                              nodeId);
        if(status != UA_STATUSCODE_GOOD) {
            if(history->customBackend)
                historyPolledNodes_remove(history, nodeId);
            pyHistory_unregister(history, server, nodeId);
            return status;
        }
    }

    return UA_STATUSCODE_GOOD;
}

UA_StatusCode
pyHistory_unregister(PyServerHistory *history, UA_Server *server,
                     const UA_NodeId *nodeId) {
    if(!history || !nodeId)
        return UA_STATUSCODE_BADINTERNALERROR;
    if(!history->enabled)
        return UA_STATUSCODE_BADINVALIDSTATE;

    /* Stop any poll first, since removal cannot reach the server. The status is
     * not consulted: a MonitoredItem that outlives the store is harmless, as
     * its callback finds the store by NodeId and no longer finds one. */
    if(server && history->gathering.stopPoll)
        history->gathering.stopPoll(server, history->gathering.context, nodeId);

    if(history->customBackend) {
        historyPolledNodes_remove(history, nodeId);
        return UA_STATUSCODE_GOOD;
    }

    return pyHistoryBackend_removeNode(&history->backend, nodeId);
}

UA_Boolean
pyHistory_registered(const PyServerHistory *history, UA_Server *server,
                     const UA_NodeId *nodeId) {
    if(!history || !history->enabled || !server || !nodeId)
        return false;
    if(!history->gathering.getHistorizingSetting)
        return false;
    return history->gathering.getHistorizingSetting(
               server, history->gathering.context, nodeId) != NULL;
}

UA_StatusCode
pyHistory_setPaused(PyServerHistory *history, UA_Server *server,
                    const UA_NodeId *nodeId, UA_Boolean paused) {
    if(!history || !server || !nodeId)
        return UA_STATUSCODE_BADINTERNALERROR;
    if(!history->enabled)
        return UA_STATUSCODE_BADINVALIDSTATE;
    if(history->customBackend) {
        if(!history->gathering.getHistorizingSetting ||
           !history->gathering.getHistorizingSetting(server, history->gathering.context,
                                                      nodeId))
            return UA_STATUSCODE_BADNODEIDUNKNOWN;
        gathering_default_pauseRecording(&history->gathering, nodeId, paused);
        return UA_STATUSCODE_GOOD;
    }
    return pyHistoryGathering_setPaused(&history->gathering, nodeId, paused);
}

UA_StatusCode
pyHistory_stats(const PyServerHistory *history, const UA_NodeId *nodeId,
                PyHistoryStats *stats) {
    if(!history)
        return UA_STATUSCODE_BADINTERNALERROR;
    if(!history->enabled)
        return UA_STATUSCODE_BADINVALIDSTATE;
    if(history->customBackend)
        return UA_STATUSCODE_BADNOTSUPPORTED;
    return pyHistoryBackend_stats(&history->backend, nodeId, stats);
}

UA_StatusCode
pyHistory_read(const PyServerHistory *history, const UA_NodeId *nodeId,
               UA_DateTime start, UA_DateTime end, size_t limit,
               UA_Boolean reverse, UA_DataValue **out, size_t *outSize) {
    if(!history)
        return UA_STATUSCODE_BADINTERNALERROR;
    if(!history->enabled)
        return UA_STATUSCODE_BADINVALIDSTATE;
    if(history->customBackend)
        return UA_STATUSCODE_BADNOTSUPPORTED;
    return pyHistoryBackend_read(&history->backend, nodeId, start, end, limit,
                                 reverse, out, outSize);
}

UA_StatusCode
pyHistory_insert(PyServerHistory *history, const UA_NodeId *nodeId,
                 const UA_DataValue *value) {
    if(!history)
        return UA_STATUSCODE_BADINTERNALERROR;
    if(!history->enabled)
        return UA_STATUSCODE_BADINVALIDSTATE;
    if(history->customBackend)
        return UA_STATUSCODE_BADNOTSUPPORTED;
    return pyHistoryBackend_insert(&history->backend, nodeId, value);
}

UA_StatusCode
pyHistory_clearNode(PyServerHistory *history, const UA_NodeId *nodeId) {
    if(!history)
        return UA_STATUSCODE_BADINTERNALERROR;
    if(!history->enabled)
        return UA_STATUSCODE_BADINVALIDSTATE;
    if(history->customBackend)
        return UA_STATUSCODE_BADNOTSUPPORTED;
    return pyHistoryBackend_clearNode(&history->backend, nodeId);
}

UA_StatusCode
pyHistory_stopPolls(PyServerHistory *history, UA_Server *server) {
    if(!history)
        return UA_STATUSCODE_BADINTERNALERROR;
    if(!history->enabled)
        return UA_STATUSCODE_GOOD;
    if(history->customBackend) {
        if(!server || !history->gathering.stopPoll)
            return UA_STATUSCODE_GOOD;
        UA_StatusCode result = UA_STATUSCODE_GOOD;
        for(size_t i = 0; i < history->polledNodesSize; ++i) {
            UA_StatusCode status = history->gathering.stopPoll(
                server, history->gathering.context, &history->polledNodes[i]);
            if(status != UA_STATUSCODE_GOOD && result == UA_STATUSCODE_GOOD)
                result = status;
        }
        return result;
    }
    return pyHistoryGathering_stopPolls(&history->gathering, server);
}

void
pyHistory_clear(PyServerHistory *history, UA_Server *server) {
    if(!history)
        return;
    pyHistory_stopPolls(history, server);
    if(history->customBackend) {
        if(history->backend.deleteMembers)
            history->backend.deleteMembers(&history->backend);
        for(size_t i = 0; i < history->polledNodesSize; ++i)
            UA_NodeId_clear(&history->polledNodes[i]);
        UA_free(history->polledNodes);
    } else {
        pyHistoryBackend_clear(&history->backend);
    }
    memset(history, 0, sizeof(PyServerHistory));
}
