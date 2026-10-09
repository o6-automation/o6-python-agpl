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

#ifndef PYO6_SERVER_HISTORY_H_
#define PYO6_SERVER_HISTORY_H_

#include <open62541/server.h>

#ifndef UA_ENABLE_HISTORIZING
#error "o6 history support requires open62541 built with UA_ENABLE_HISTORIZING"
#endif

#include <open62541/plugin/historydata/history_data_backend.h>
#include <open62541/plugin/historydata/history_data_gathering.h>

/*
 * Server-side historizing: a UA_HistoryDataBackend and a UA_HistoryDataGathering
 * over one shared node table, plus a PyServerHistory facade that owns both and
 * installs a UA_HistoryDatabase_default on a UA_ServerConfig.
 *
 * Per node the table holds a store of `capacity` samples, fixed at registration
 * so the footprint is known then, or growing when registered unbounded. The
 * table itself always grows: how many nodes historize is a property of the
 * address space.
 *
 * Sharing the table means recording a sample costs one lookup rather than the
 * two upstream needs, and stores are found through an open-addressed index on
 * the NodeId hash, so that lookup is O(1).
 *
 * Index space. The plugin interface is index based and HistoryRead continuation
 * points carry those indices between requests, so physical slots - reused on
 * every wraparound - will not do. A store indexes by a monotonic sequence
 * number mapped to a slot as `seq % capacity`; the retained window is
 * [firstSeq, firstSeq + count), and firstSeq + count is the "no match" sentinel
 * every index-returning hook uses. Ordered indices are also why the backend
 * leaves getHistoryData NULL and keeps the generic paging of
 * UA_HistoryDatabase_default.
 *
 * Being unique for the life of a store is what lets a continuation point name
 * the next sample to deliver rather than a count of those already delivered.
 * A count is applied to a window that eviction has moved down and skips one
 * retained sample per evicted one; a sequence number costs only the samples
 * eviction actually took, and makes an overrun point detectable.
 *
 * What that cannot fix is the total: UA_HistoryDatabase_default recomputes it
 * from the current store on every page and subtracts a count of its own, so a
 * store that shrinks mid-read ends the read early and one that has outrun the
 * point reports BadContinuationPointInvalid. Owning it outright would mean
 * implementing getHistoryData and giving up the generic paging - which is what
 * upstream's _Circular backend does, and where its bugs live.
 *
 * Threading. Every entry point runs with the open62541 service mutex held -
 * from the server's event loop, or from a trampoline that takes it first.
 */

/* Stores allocated up front when the caller does not choose. */
#define PYO6_HISTORY_MAX_NODES_DEFAULT 10

/* Samples per node when the caller does not choose. Small on purpose: a nodeset
 * can declare hundreds of historizing Variables. */
#define PYO6_HISTORY_CAPACITY_DEFAULT 100

/* Values per HistoryRead response before continuation points kick in. */
#define PYO6_HISTORY_RESPONSE_DEFAULT 100

/* Allocation floor for a growing store registered with no initial size. */
#define PYO6_HISTORY_GROW_MIN 16

/* ==================================================== *
 *                       Backend                        *
 * ==================================================== */

/* One node's store, for diagnostics. oldest/newest are 0 while it is empty. */
typedef struct {
    size_t capacity;       /* samples it can hold before it evicts or grows */
    size_t count;          /* samples retained */
    UA_UInt64 stored;      /* samples accepted since registration */
    UA_UInt64 overwrites;  /* samples evicted to make room */
    UA_UInt64 dropped;     /* samples refused as older than the whole store */
    UA_Boolean unbounded;  /* grows instead of evicting */
    UA_DateTime oldest;
    UA_DateTime newest;
} PyHistoryStats;

/* Create the backend. Zero arguments take the PYO6_HISTORY_* defaults;
 * `initialNodes` only sizes the initial table, which grows on demand.
 *
 * A NULL `context` means allocation failed. The caller owns the result and must
 * release it with pyHistoryBackend_clear even after handing it to a
 * UA_HistorizingNodeIdSettings or to pyHistoryGathering_ring: those share the
 * context without owning it. */
UA_HistoryDataBackend
pyHistoryBackend_ring(size_t initialNodes, size_t defaultCapacity);

void
pyHistoryBackend_clear(UA_HistoryDataBackend *backend);

/* Allocate one node's store; `capacity` of 0 takes the backend default. With
 * `unbounded` the store grows instead of evicting and `capacity` is only the
 * initial allocation - nothing then bounds what one node costs, so it is for a
 * run of known length, not for a server that stays up.
 *
 * Returns BadNodeIdExists when the node already has a store. Stores are never
 * created by a write; registration is always explicit. */
UA_StatusCode
pyHistoryBackend_addNode(UA_HistoryDataBackend *backend,
                         const UA_NodeId *nodeId, size_t capacity,
                         UA_Boolean unbounded);

/* Drop one node's store and its gathering registration. Any poll must be
 * stopped first - removal cannot reach the server to delete the MonitoredItem.
 * For the registration failure path and teardown, not for "stop historizing";
 * use pyHistory_setPaused for that. */
UA_StatusCode
pyHistoryBackend_removeNode(UA_HistoryDataBackend *backend,
                            const UA_NodeId *nodeId);

/* Discard one node's samples, keeping its store. Sequence numbers keep counting
 * up, so earlier continuation points cannot address the new samples. */
UA_StatusCode
pyHistoryBackend_clearNode(UA_HistoryDataBackend *backend,
                           const UA_NodeId *nodeId);

/* Store one sample directly, whatever the strategy - the hook behind
 * UA_HISTORIZINGUPDATESTRATEGY_USER. `value` needs a source or server
 * timestamp; a timestamp already held is BadEntryExists. */
UA_StatusCode
pyHistoryBackend_insert(UA_HistoryDataBackend *backend, const UA_NodeId *nodeId,
                        const UA_DataValue *value);

UA_StatusCode
pyHistoryBackend_stats(const UA_HistoryDataBackend *backend,
                       const UA_NodeId *nodeId, PyHistoryStats *stats);

/* Read samples without going through the HistoryRead service, on the same
 * interval arithmetic so that a local read and a client's ReadRaw of one range
 * agree: `start` inclusive, `end` exclusive, start == end reads that timestamp.
 * INT64_MIN and INT64_MAX are the open ends and `start` must not follow `end`.
 * `limit` of 0 reads the whole range, otherwise the newest `limit` samples when
 * `reverse` and the oldest otherwise.
 *
 * *out is a fresh array of *outSize deep copies, released with
 * UA_Array_delete(*out, *outSize, &UA_TYPES[UA_TYPES_DATAVALUE]). An empty
 * range is Good with *out NULL. */
UA_StatusCode
pyHistoryBackend_read(const UA_HistoryDataBackend *backend,
                      const UA_NodeId *nodeId, UA_DateTime start,
                      UA_DateTime end, size_t limit, UA_Boolean reverse,
                      UA_DataValue **out, size_t *outSize);

/* ==================================================== *
 *                      Gathering                       *
 * ==================================================== */

/* Create a gathering over the node table of `backend`, which must outlive it.
 * It borrows the table and releases nothing, so it is safe to hand to
 * UA_HistoryDatabase_default even though that clear() runs while the server is
 * still tearing nodes down. A NULL `context` means `backend` had none. */
UA_HistoryDataGathering
pyHistoryGathering_ring(const UA_HistoryDataBackend *backend);

/* Suspend or resume recording, on the write path and the poll path alike -
 * upstream honours its pause flag only on the former. Retained samples stay
 * readable. */
UA_StatusCode
pyHistoryGathering_setPaused(UA_HistoryDataGathering *gathering,
                             const UA_NodeId *nodeId, UA_Boolean paused);

/* Stop every running poll. Must run while the server is alive, since only it
 * can delete a MonitoredItem. Returns the first failure, having tried all. */
UA_StatusCode
pyHistoryGathering_stopPolls(UA_HistoryDataGathering *gathering,
                             UA_Server *server);

/* ==================================================== *
 *                       Facade                         *
 * ==================================================== */

/* One per PyServer, and the owner of the shared node table. The gathering copy
 * inside the UA_HistoryDatabase releases nothing: the config is cleaned partway
 * through UA_Server_delete, while nodes can still record, and freeing the table
 * there would write into released memory. pyHistory_clear is the one
 * owner-side path and runs after the server is gone. */
typedef struct {
    UA_HistoryDataGathering gathering;  /* borrows backend.context (ring mode),
                                          * or UA_HistoryDataGathering_Default
                                          * (customBackend mode) */
    UA_HistoryDataBackend backend;      /* owns the shared node table (ring
                                          * mode), or the one Python trampoline
                                          * backend shared by every node
                                          * (customBackend mode) */
    size_t initialNodes;
    size_t defaultCapacity;
    size_t defaultResponseSize;
    UA_Boolean enabled;
    UA_Boolean customBackend;  
    UA_NodeId *polledNodes;
    size_t polledNodesSize;
    size_t polledNodesCapacity;
} PyServerHistory;

void
pyHistory_init(PyServerHistory *history);

UA_Boolean
pyHistory_enabled(const PyServerHistory *history);

/* Install a history database on `config` and fill in the ns0
 * HistoryServerCapabilities to match what the backend implements. open62541
 * writes those nodes from the config while the server is being created, before
 * this can run, which is why `server` is needed and not just `config`.
 *
 * Must run before the server starts, and after anything that rebuilds the
 * config wholesale - UA_ServerConfig_setDefaultWith*SecurityPolicies, which
 * setEncryption calls, discards a history database. Returns BadInvalidState
 * when history is already enabled. */
UA_StatusCode
pyHistory_enable(PyServerHistory *history, UA_Server *server,
                 UA_ServerConfig *config, size_t initialNodes,
                 size_t defaultCapacity, size_t defaultResponseSize);

/* Install a history database backed by a user-supplied o6.HistoryBackend
 * instead of the built-in ring. `pyBackend`/`pyServer` are a borrowed
 * PyObject* each (the HistoryBackend instance and the owning PyServer) -
 * typed void* here so this header stays Python-agnostic; the caller in
 * server_config.c passes them straight through. Mirrors pyHistory_enable
 * otherwise, including running the same guards before calling this.
 *
 * On failure, a Python exception may already be set (e.g. `pyBackend`'s
 * `_overridden_callbacks()` raised) - the caller must check PyErr_Occurred()
 * before mapping the returned status through PyErr_StatusCode, or it will
 * clobber the real error. */
UA_StatusCode
pyHistory_enableCustom(PyServerHistory *history, UA_Server *server,
                       UA_ServerConfig *config, void *pyBackend,
                       void *pyServer, size_t initialNodes,
                       size_t defaultResponseSize);

/* Build the one shared UA_HistoryDataBackend that trampolines into a Python
 * o6.HistoryBackend instance. Defined in server_history_python.c, which is
 * the only translation unit in this feature that touches the Python API.
 *
 * A NULL `context` on the result means failure; check PyErr_Occurred() (see
 * pyHistory_enableCustom) to tell a Python-level failure (already has an
 * exception set) from a plain allocation failure (does not). */
UA_HistoryDataBackend
pyHistoryBackend_python(void *pyBackend, void *pyServer);

/* Start historizing one node. Zero `capacity` and `maxResponseSize` take the
 * pyHistory_enable defaults; see pyHistoryBackend_addNode for `unbounded`.
 *
 * VALUESET records on every write. POLL samples through an internal
 * MonitoredItem every `pollingIntervalMs`, which is what a callback-backed
 * Variable needs; the poll is started here and stopped by pyHistory_stopPolls,
 * and one that cannot start rolls the whole registration back. USER records
 * nothing on its own - pyHistory_insert is the way in.
 *
 * The node's Historizing attribute and history access levels are the caller's
 * business: a node registered but not marked Historizing records nothing and
 * cannot be read back. */
UA_StatusCode
pyHistory_register(PyServerHistory *history, UA_Server *server,
                   const UA_NodeId *nodeId, size_t capacity,
                   UA_Boolean unbounded, size_t maxResponseSize,
                   UA_HistorizingUpdateStrategy strategy,
                   size_t pollingIntervalMs);

/* Stop historizing one node and release its store, undoing pyHistory_register.
 * Any running poll is stopped first. Returns BadNodeIdUnknown when the node was
 * not historized.
 *
 * The node's Historizing attribute and history access levels are the caller's
 * business, as they are on the way in. */
UA_StatusCode
pyHistory_unregister(PyServerHistory *history, UA_Server *server,
                     const UA_NodeId *nodeId);

UA_Boolean
pyHistory_registered(const PyServerHistory *history, UA_Server *server,
                     const UA_NodeId *nodeId);

UA_StatusCode
pyHistory_setPaused(PyServerHistory *history, UA_Server *server,
                    const UA_NodeId *nodeId, UA_Boolean paused);

UA_StatusCode
pyHistory_stats(const PyServerHistory *history, const UA_NodeId *nodeId,
                PyHistoryStats *stats);

UA_StatusCode
pyHistory_read(const PyServerHistory *history, const UA_NodeId *nodeId,
               UA_DateTime start, UA_DateTime end, size_t limit,
               UA_Boolean reverse, UA_DataValue **out, size_t *outSize);

UA_StatusCode
pyHistory_insert(PyServerHistory *history, const UA_NodeId *nodeId,
                 const UA_DataValue *value);

UA_StatusCode
pyHistory_clearNode(PyServerHistory *history, const UA_NodeId *nodeId);

UA_StatusCode
pyHistory_stopPolls(PyServerHistory *history, UA_Server *server);

/* Release the node table and reset. Stops outstanding polls when `server` is
 * still valid. The UA_HistoryDatabase wrapper belongs to the config and is
 * released by UA_ServerConfig_clean, so this is safe before or after the server
 * is deleted - but not while one that could still record is alive. */
void
pyHistory_clear(PyServerHistory *history, UA_Server *server);

#endif /* PYO6_SERVER_HISTORY_H_ */
