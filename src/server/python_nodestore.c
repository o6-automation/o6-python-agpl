/* Copyright 2026 (c) o6 Automation GmbH
 *
 * The tree and NodeId-allocation algorithm are adapted from open62541's
 * CC0-licensed ua_nodestore_ziptree.c. The canonical node allocation differs:
 * it reserves a PyObject header and Python instance fields and replacement is
 * performed in place so its address never changes.
 */

#include "python_nodestore.h"
#include "../open62541_queue.h"
#include "server_services_util.h"
#include "../types_internal.h"

#include "pcg_basic.h"
#include "ziptree.h"

#include <stddef.h>
#include <stdint.h>
#include <string.h>

#ifndef container_of
#define container_of(ptr, type, member) \
    ((type *)((uintptr_t)(ptr) - offsetof(type, member)))
#endif

typedef struct PyNode PyNode;

typedef struct {
    UA_UInt32 hash;
    const UA_NodeId *nodeId;
} PyNodeKey;

typedef struct {
    PyObject *callable;
    PyObject *receiver;
} PyNodeCallback;

typedef union {
    struct {
        PyNodeCallback call;
    } method;
    struct {
        PyNodeCallback read;
        PyNodeCallback write;
    } variable;
} PyNodeCallbacks;

struct PyNode {
    PyObject_HEAD

    ZIP_ENTRY(PyNode) zipfields;
    PyNodeKey key;
    UA_UInt32 nativeRefs;
    UA_Boolean deleted;

    /* Borrowed while attached. NULL for a temporary node or tombstone. */
    PyServer *server;

    /* Intrusive list exposing promoted nodestore pins to Python's GC. */
    LIST_ENTRY(PyNode) promotedEntry;

    /* Python state, populated only after promotion. */
    PyObject *dict;
    PyObject *weakrefs;
    PyObject *constructionOwner;
    PyNodeCallbacks callbacks;

    UA_Node node;
};

ZIP_HEAD(PyNodeTree, PyNode);
typedef struct PyNodeTree PyNodeTree;
LIST_HEAD(PyNodeList, PyNode);

typedef struct {
    UA_Nodestore ns;
    PyServer *server; /* borrowed */
    PyNodeTree root;
    struct PyNodeList promotedNodes;
    size_t size;

    UA_NodeId referenceTypeIds[UA_REFERENCETYPESET_MAX];
    UA_Byte referenceTypeCounter;
} PyNodeStore;

static int
pyNodeCallback_traverse(PyNodeCallback *callback, visitproc visit, void *arg) {
    Py_VISIT(callback->callable);
    Py_VISIT(callback->receiver);
    return 0;
}

static void
pyNodeCallback_clear(PyNodeCallback *callback) {
    Py_CLEAR(callback->callable);
    Py_CLEAR(callback->receiver);
}

static int
pyNode_traverse(PyNode *self, visitproc visit, void *arg) {
    Py_VISIT(self->dict);
    Py_VISIT(self->constructionOwner);
    if(self->node.head.nodeClass == UA_NODECLASS_METHOD) {
        int result = pyNodeCallback_traverse(
            &self->callbacks.method.call, visit, arg);
        if(result)
            return result;
    } else if(self->node.head.nodeClass == UA_NODECLASS_VARIABLE ||
              self->node.head.nodeClass == UA_NODECLASS_VARIABLETYPE) {
        int result = pyNodeCallback_traverse(
            &self->callbacks.variable.read, visit, arg);
        if(result)
            return result;
        result = pyNodeCallback_traverse(
            &self->callbacks.variable.write, visit, arg);
        if(result)
            return result;
    }
    return 0;
}

static int
pyNode_clear(PyNode *self) {
    /* While attached, the nodestore owns these references and their teardown
     * ordering. Python GC may clear only detached nodes. */
    if(self->server)
        return 0;
    Py_CLEAR(self->dict);
    Py_CLEAR(self->constructionOwner);
    if(self->node.head.nodeClass == UA_NODECLASS_METHOD) {
        pyNodeCallback_clear(&self->callbacks.method.call);
    } else if(self->node.head.nodeClass == UA_NODECLASS_VARIABLE ||
              self->node.head.nodeClass == UA_NODECLASS_VARIABLETYPE) {
        pyNodeCallback_clear(&self->callbacks.variable.read);
        pyNodeCallback_clear(&self->callbacks.variable.write);
    }
    return 0;
}

static void
pyNode_dealloc(PyNode *self) {
    UA_assert(self->server == NULL);
    UA_assert(self->promotedEntry.le_prev == NULL);
    PyObject_GC_UnTrack(self);
    if(self->weakrefs)
        PyObject_ClearWeakRefs((PyObject *)self);
    pyNode_clear(self);
    UA_Node_clear(&self->node);
    PyObject_GC_Del(self);
}

static PyObject *
pyNode_checkAttached(PyNode *self, PyObject *Py_UNUSED(ignored)) {
    /* Detached and client-side nodes were never deleted from this nodestore.
     * A server node keeps the deleted marker after becoming a tombstone. */
    if(self->deleted && self->server == NULL) {
        PyErr_SetString(PyExc_ReferenceError,
                        "the OPC UA node has been deleted");
        return NULL;
    }
    Py_RETURN_NONE;
}

static PyObject *
pyNode_isNativeAttached(PyNode *self, PyObject *Py_UNUSED(ignored)) {
    return PyBool_FromLong(self->server != NULL);
}

static PyMethodDef pyNode_methods[] = {
    {"_check_attached", (PyCFunction)pyNode_checkAttached, METH_NOARGS,
     "Raise ReferenceError for a deleted server node"},
    {"_is_native_attached", (PyCFunction)pyNode_isNativeAttached, METH_NOARGS,
     "Return whether this object is embedded in a live server nodestore"},
    {"_read_native_attribute", (PyCFunction)pyNode_read_attribute, METH_VARARGS,
     "Read an attribute directly from an attached canonical server node"},
    {"_write_native_attribute", (PyCFunction)pyNode_write_attribute, METH_VARARGS,
     "Write an attribute directly to an attached canonical server node"},
    {"_set_pubsub_state_machine",
     (PyCFunction)pyNode_set_pubsub_state_machine, METH_O,
     "Install or clear a custom state machine on a native PubSub component"},
    {"_pubsub_offset_table",
     (PyCFunction)pyNode_pubsub_offset_table, METH_NOARGS,
     "Compute a native PubSub offset table"},
    {"_pubsub_publish",
     (PyCFunction)pyNode_pubsub_publish, METH_NOARGS,
     "Publish one native WriterGroup immediately"},
    {NULL}
};

static PyObject *
pyNode_getDictField(PyNode *self, const char *name) {
    if(!self->dict) {
        PyErr_Format(PyExc_AttributeError, "%.200s has no attribute '%s'",
                     Py_TYPE(self)->tp_name, name);
        return NULL;
    }
    PyObject *value = PyDict_GetItemString(self->dict, name);
    if(!value) {
        PyErr_Format(PyExc_AttributeError, "%.200s has no attribute '%s'",
                     Py_TYPE(self)->tp_name, name);
        return NULL;
    }
    return Py_NewRef(value);
}

static int
pyNode_setDictField(PyNode *self, const char *name, PyObject *value) {
    if(!value) {
        if(!self->dict || PyDict_DelItemString(self->dict, name) < 0)
            return -1;
        return 0;
    }
    if(!self->dict) {
        self->dict = PyDict_New();
        if(!self->dict)
            return -1;
    }
    return PyDict_SetItemString(self->dict, name, value);
}

PyObject *
pyNodeStore_getMetadata(void *nodeContext, const char *name) {
    PyNode *node = (PyNode *)nodeContext;
    if(!node || !node->dict)
        return NULL;
    PyObject *value = PyDict_GetItemString(node->dict, name);
    return Py_XNewRef(value);
}

int
pyNodeStore_setMetadata(void *nodeContext, const char *name,
                        PyObject *value) {
    PyNode *node = (PyNode *)nodeContext;
    if(!node) {
        PyErr_SetString(PyExc_ReferenceError, "node context is unavailable");
        return -1;
    }
    if(value)
        return pyNode_setDictField(node, name, value);
    if(!node->dict)
        return 0;
    int result = PyDict_DelItemString(node->dict, name);
    if(result < 0 && PyErr_ExceptionMatches(PyExc_KeyError)) {
        PyErr_Clear();
        return 0;
    }
    return result;
}

static PyObject *
pyNode_getNodeId(PyNode *self, void *Py_UNUSED(closure)) {
    if(!self->server)
        return pyNode_getDictField(self, "_nodeid");

    UA_NodeId value;
    UA_NodeId_init(&value);
    if(UA_NodeId_copy(&self->node.head.nodeId, &value) != UA_STATUSCODE_GOOD)
        return PyErr_NoMemory();
    PyObject *result = UA2PY(&value, &UA_TYPES[UA_TYPES_NODEID],
                             &self->server->nsMapPy2UA);
    UA_NodeId_clear(&value);
    return result;
}

static int
pyNode_setNodeId(PyNode *self, PyObject *value, void *Py_UNUSED(closure)) {
    if(self->server) {
        PyErr_SetString(PyExc_AttributeError,
                        "an attached server node's NodeId is read-only");
        return -1;
    }
    return pyNode_setDictField(self, "_nodeid", value);
}

static PyObject *
pyNode_getBrowseName(PyNode *self, void *Py_UNUSED(closure)) {
    if(!self->server)
        return pyNode_getDictField(self, "_browse_name");

    UA_QualifiedName value;
    UA_QualifiedName_init(&value);
    if(UA_QualifiedName_copy(&self->node.head.browseName, &value) !=
       UA_STATUSCODE_GOOD)
        return PyErr_NoMemory();
    PyObject *result = UA2PY(&value, &UA_TYPES[UA_TYPES_QUALIFIEDNAME],
                             &self->server->nsMapPy2UA);
    UA_QualifiedName_clear(&value);
    return result;
}

static int
pyNode_setBrowseName(PyNode *self, PyObject *value,
                     void *Py_UNUSED(closure)) {
    if(self->server) {
        PyErr_SetString(PyExc_AttributeError,
                        "an attached server node's BrowseName is read-only");
        return -1;
    }
    return pyNode_setDictField(self, "_browse_name", value);
}

static PyObject *
pyNode_getConstructionOwner(PyNode *self, void *Py_UNUSED(closure)) {
    if(!self->constructionOwner)
        Py_RETURN_NONE;
    return Py_NewRef(self->constructionOwner);
}

typedef struct {
    const UA_NodeId *candidate;
    UA_Boolean matches;
} ConstructionOwnerContext;

static void *
matchConstructionOwner(void *context, UA_ReferenceTarget *target) {
    ConstructionOwnerContext *ctx = (ConstructionOwnerContext *)context;
    UA_NodeId targetId = UA_NodePointer_toNodeId(target->targetId);
    if(UA_NodeId_equal(&targetId, ctx->candidate))
        ctx->matches = true;
    return NULL;
}

static int
pyNode_setConstructionOwner(PyNode *self, PyObject *value,
                            void *Py_UNUSED(closure)) {
    if(self->node.head.nodeClass != UA_NODECLASS_METHOD &&
       self->node.head.nodeClass != UA_NODECLASS_VARIABLE &&
       self->node.head.nodeClass != UA_NODECLASS_OBJECT) {
        PyErr_SetString(PyExc_TypeError,
                        "only Object, Variable and Method nodes have a construction owner");
        return -1;
    }
    if(!self->server) {
        PyErr_SetString(PyExc_TypeError,
                        "a construction owner requires an attached server node");
        return -1;
    }
    PyServer *ownerServer = NULL;
    UA_Node *owner = pyNodeStore_attachedNode(value, &ownerServer);
    if(!owner)
        return -1;
    if(ownerServer != self->server) {
        PyErr_SetString(PyExc_ValueError,
                        "node and construction owner belong to different servers");
        return -1;
    }
    if(owner->head.nodeClass != UA_NODECLASS_OBJECT &&
       owner->head.nodeClass != UA_NODECLASS_OBJECTTYPE) {
        PyErr_SetString(PyExc_TypeError,
                        "a construction owner must be an Object or ObjectType");
        return -1;
    }
    ConstructionOwnerContext ctx = {&owner->head.nodeId, false};
    for(size_t i = 0; i < self->node.head.referencesSize; i++) {
        UA_NodeReferenceKind *rk = &self->node.head.references[i];
        if(!rk->isInverse)
            continue;
        UA_NodeReferenceKind_iterate(rk, matchConstructionOwner, &ctx);
    }
    if(!ctx.matches) {
        PyErr_SetString(PyExc_ValueError,
                        "node does not reference this construction owner");
        return -1;
    }
    if(self->constructionOwner && self->constructionOwner != value) {
        PyErr_SetString(PyExc_ValueError,
                        "node already has a different construction owner");
        return -1;
    }
    Py_INCREF(value);
    Py_XSETREF(self->constructionOwner, value);
    return 0;
}

/* This underscored implementation base describes the reserved allocation
 * until promotion. A later promotion replaces the type stored in
 * PyObject_HEAD with the concrete public Node subclass. */
static PyGetSetDef pyNode_getset[] = {
    {"__dict__", PyObject_GenericGetDict, PyObject_GenericSetDict,
     "instance dictionary", NULL},
    {"_nodeid", (getter)pyNode_getNodeId, (setter)pyNode_setNodeId,
     "canonical native NodeId or detached/client identity", NULL},
    {"_browse_name", (getter)pyNode_getBrowseName,
     (setter)pyNode_setBrowseName,
     "canonical native BrowseName or detached/client identity", NULL},
    {"_construction_owner", (getter)pyNode_getConstructionOwner,
     (setter)pyNode_setConstructionOwner,
     "construction owner retained by an attached server node", NULL},
    {NULL}
};

static PyTypeObject PyNodeBaseType = {
    PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "o6._o6._NodeBase",
    .tp_basicsize = sizeof(PyNode),
    .tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE |
                Py_TPFLAGS_HAVE_GC,
    .tp_new = PyType_GenericNew,
    .tp_dealloc = (destructor)pyNode_dealloc,
    .tp_traverse = (traverseproc)pyNode_traverse,
    .tp_clear = (inquiry)pyNode_clear,
    .tp_methods = pyNode_methods,
    .tp_getset = pyNode_getset,
    .tp_dictoffset = offsetof(PyNode, dict),
    .tp_weaklistoffset = offsetof(PyNode, weakrefs),
};

static enum ZIP_CMP
compareNodeId(const void *a, const void *b) {
    const PyNodeKey *aa = (const PyNodeKey *)a;
    const PyNodeKey *bb = (const PyNodeKey *)b;
    if(aa->hash < bb->hash)
        return ZIP_CMP_LESS;
    if(aa->hash > bb->hash)
        return ZIP_CMP_MORE;
    return (enum ZIP_CMP)UA_NodeId_order(aa->nodeId, bb->nodeId);
}

ZIP_FUNCTIONS(PyNodeTree, PyNode, zipfields,
              PyNodeKey, key, compareNodeId)

static PyNode *
findNode(PyNodeStore *store, const UA_NodeId *nodeId) {
    PyNodeKey key = {UA_NodeId_hash(nodeId), nodeId};
    return ZIP_FIND(PyNodeTree, &store->root, &key);
}

static PyNode *
newEntry(UA_NodeClass nodeClass) {
    /* All o6 server entry points execute with the GIL. Keeping that invariant
     * explicit is essential once nodes can own Python references. */
    UA_assert(PyGILState_Check());

    PyNode *entry = PyObject_GC_New(PyNode, &PyNodeBaseType);
    if(!entry)
        return NULL;

    /* PyObject_GC_New initializes only the Python header. */
    memset((char *)entry + sizeof(PyObject), 0,
           sizeof(PyNode) - sizeof(PyObject));
    entry->node.head.nodeClass = nodeClass;
#ifdef UA_ENABLE_RBAC
    entry->node.head.permissionIndex = UA_PERMISSION_INDEX_INVALID;
#endif

    /* Native-only nodes are reserved GC-capable storage, not live Python
     * objects. Promotion establishes the nodestore pin before exposure. */
    Py_SET_REFCNT(entry, 0);
    return entry;
}

static void
freeNativeEntry(PyNode *entry) {
    UA_assert(Py_REFCNT(entry) == 0);
    UA_assert(entry->promotedEntry.le_prev == NULL);
    UA_Node_clear(&entry->node);
    PyObject_GC_Del(entry);
}

static void
linkPromotedNode(PyNodeStore *store, PyNode *entry) {
    if(entry->promotedEntry.le_prev)
        return;
    LIST_INSERT_HEAD(&store->promotedNodes, entry, promotedEntry);
}

static void
unlinkPromotedNode(PyNode *entry) {
    if(!entry->promotedEntry.le_prev)
        return;
    LIST_REMOVE(entry, promotedEntry);
    entry->promotedEntry.le_next = NULL;
    entry->promotedEntry.le_prev = NULL;
}

static int
cacheDetachedIdentity(PyNode *entry) {
    if(!entry->dict)
        return 0;
    PyObject *nodeId = pyNode_getNodeId(entry, NULL);
    PyObject *browseName = pyNode_getBrowseName(entry, NULL);
    if(!nodeId || !browseName ||
       PyDict_SetItemString(entry->dict, "_nodeid", nodeId) < 0 ||
       PyDict_SetItemString(entry->dict, "_browse_name", browseName) < 0) {
        Py_XDECREF(nodeId);
        Py_XDECREF(browseName);
        return -1;
    }
    Py_DECREF(nodeId);
    Py_DECREF(browseName);
    return 0;
}

static void
releaseRemovedEntry(PyNode *entry) {
    UA_assert(entry->server == NULL);
    UA_assert(entry->nativeRefs == 0);
    if(Py_REFCNT(entry) == 0) {
        freeNativeEntry(entry);
        return;
    }
    /* Release the single nodestore pin. pyNode_dealloc runs immediately if
     * Python has no other reference; otherwise the allocation is a tombstone. */
    unlinkPromotedNode(entry);
    Py_DECREF(entry);
}

static void
cleanupEntry(PyNode *entry) {
    if(entry->nativeRefs > 0)
        return;
    if(entry->deleted) {
        releaseRemovedEntry(entry);
        return;
    }

    for(size_t i = 0; i < entry->node.head.referencesSize; i++) {
        UA_NodeReferenceKind *rk = &entry->node.head.references[i];
        if(rk->targetsSize > 16 && !rk->hasRefTree)
            UA_NodeReferenceKind_switch(rk);
    }
}

static UA_Node *
storeNewNode(UA_Nodestore *ns, UA_NodeClass nodeClass) {
    (void)ns;
    PyNode *entry = newEntry(nodeClass);
    return entry ? &entry->node : NULL;
}

static void
storeDeleteNode(UA_Nodestore *ns, UA_Node *node) {
    (void)ns;
    if(!node)
        return;
    PyNode *entry = container_of(node, PyNode, node);
    UA_assert(entry->server == NULL);
    UA_assert(entry->nativeRefs == 0);
    /* deleteNode owns only fresh or temporary native entries. Inserted nodes
     * leave the nodestore through removeNode instead. */
    UA_assert(Py_REFCNT(entry) == 0);
    freeNativeEntry(entry);
}

static const UA_Node *
storeGetNode(UA_Nodestore *ns, const UA_NodeId *nodeId,
             UA_UInt32 attributeMask, UA_ReferenceTypeSet references,
             UA_BrowseDirection referenceDirections) {
    (void)attributeMask;
    (void)references;
    (void)referenceDirections;
    PyNode *entry = findNode((PyNodeStore *)ns, nodeId);
    if(!entry)
        return NULL;
    entry->nativeRefs++;
    return &entry->node;
}

static const UA_Node *
storeGetNodeFromPtr(UA_Nodestore *ns, UA_NodePointer ptr,
                    UA_UInt32 attributeMask,
                    UA_ReferenceTypeSet references,
                    UA_BrowseDirection referenceDirections) {
    if(!UA_NodePointer_isLocal(ptr))
        return NULL;
    UA_NodeId id = UA_NodePointer_toNodeId(ptr);
    return storeGetNode(ns, &id, attributeMask,
                        references, referenceDirections);
}

static void
storeReleaseNode(UA_Nodestore *ns, const UA_Node *node) {
    (void)ns;
    if(!node)
        return;
    PyNode *entry = container_of(node, PyNode, node);
    UA_assert(entry->nativeRefs > 0);
    entry->nativeRefs--;
    cleanupEntry(entry);
}

static UA_StatusCode
storeGetNodeCopy(UA_Nodestore *ns, const UA_NodeId *nodeId,
                 UA_Node **outNode) {
    const UA_Node *node = storeGetNode(ns, nodeId,
                                      UA_NODEATTRIBUTESMASK_ALL,
                                      UA_REFERENCETYPESET_ALL,
                                      UA_BROWSEDIRECTION_BOTH);
    if(!node)
        return UA_STATUSCODE_BADNODEIDUNKNOWN;

    PyNode *copy = newEntry(node->head.nodeClass);
    if(!copy) {
        storeReleaseNode(ns, node);
        return UA_STATUSCODE_BADOUTOFMEMORY;
    }

    UA_StatusCode result = UA_Node_copy(node, &copy->node);
    if(result == UA_STATUSCODE_GOOD)
        *outNode = &copy->node;
    storeReleaseNode(ns, node);

    if(result != UA_STATUSCODE_GOOD)
        freeNativeEntry(copy);
    return result;
}

static UA_StatusCode
storeInsertNode(UA_Nodestore *ns, UA_Node *node, UA_NodeId *addedNodeId) {
    PyNodeStore *store = (PyNodeStore *)ns;
    PyNode *entry = container_of(node, PyNode, node);

    PyNodeKey key = {0, &node->head.nodeId};

    if(node->head.nodeId.identifierType == UA_NODEIDTYPE_NUMERIC &&
       node->head.nodeId.identifier.numeric == 0) {
        PyNode *found;
        UA_UInt32 mask = 0x2F;
        pcg32_random_t rng;
        pcg32_srandom_r(&rng, store->size, 0);
        do {
            UA_UInt32 numeric = (pcg32_random_r(&rng) & mask) + 50000;
#if SIZE_MAX <= UA_UINT32_MAX
            if(numeric >= (0x01u << 24))
                numeric %= (0x01u << 24);
#endif
            node->head.nodeId.identifier.numeric = numeric;
            key.hash = UA_NodeId_hash(&node->head.nodeId);
            found = ZIP_FIND(PyNodeTree, &store->root, &key);
            if(found) {
                pcg32_srandom_r(
                    &rng, rng.state,
                    UA_QualifiedName_hash(&found->node.head.browseName));
                mask = (mask << 1) | 0x01;
            }
        } while(found);
    } else {
        key.hash = UA_NodeId_hash(&node->head.nodeId);
        if(ZIP_FIND(PyNodeTree, &store->root, &key)) {
            storeDeleteNode(ns, node);
            return UA_STATUSCODE_BADNODEIDEXISTS;
        }
    }

    if(addedNodeId) {
        UA_StatusCode result = UA_NodeId_copy(&node->head.nodeId, addedNodeId);
        if(result != UA_STATUSCODE_GOOD) {
            storeDeleteNode(ns, node);
            return result;
        }
    }

    if(node->head.nodeClass == UA_NODECLASS_REFERENCETYPE) {
        if(store->referenceTypeCounter >= UA_REFERENCETYPESET_MAX) {
            storeDeleteNode(ns, node);
            return UA_STATUSCODE_BADINTERNALERROR;
        }
        UA_Byte index = store->referenceTypeCounter;
        UA_StatusCode result = UA_NodeId_copy(
            &node->head.nodeId, &store->referenceTypeIds[index]);
        if(result != UA_STATUSCODE_GOOD) {
            storeDeleteNode(ns, node);
            return result;
        }
        node->referenceTypeNode.referenceTypeIndex = index;
        node->referenceTypeNode.subTypes = UA_REFTYPESET(index);
        store->referenceTypeCounter++;
    }

    /* The context is a non-owning pointer to the enclosing canonical PyNode.
     * The nodestore allocation, not this pointer, owns its lifetime. */
    node->head.context = entry;
    entry->key.hash = key.hash;
    entry->key.nodeId = &entry->node.head.nodeId;
    entry->server = store->server;
    /* Detached and client nodes keep Python identity fields. Once inserted in
     * the nodestore, the canonical native attributes are the only source of
     * truth. */
    if(entry->dict) {
        if(PyDict_DelItemString(entry->dict, "_nodeid") < 0)
            PyErr_Clear();
        if(PyDict_DelItemString(entry->dict, "_browse_name") < 0)
            PyErr_Clear();
    }
    ZIP_INSERT(PyNodeTree, &store->root, entry);
    if(Py_REFCNT(entry) > 0)
        linkPromotedNode(store, entry);
    store->size++;
    return UA_STATUSCODE_GOOD;
}

static UA_StatusCode
storeRejectReplaceNode(UA_Nodestore *ns, UA_Node *node) {
    /* o6 requires stable canonical nodes and configures open62541 for direct
     * in-place editing through getEditNode. Reaching replaceNode means that
     * copy-on-write was enabled or introduced unexpectedly. */
    UA_assert(false && "o6 nodestore does not support copy-on-write replacement");
    storeDeleteNode(ns, node);
    return UA_STATUSCODE_BADNOTSUPPORTED;
}

static UA_StatusCode
storeRemoveNode(UA_Nodestore *ns, const UA_NodeId *nodeId) {
    PyNodeStore *store = (PyNodeStore *)ns;
    PyNode *entry = findNode(store, nodeId);
    if(!entry)
        return UA_STATUSCODE_BADNODEIDUNKNOWN;
    if(cacheDetachedIdentity(entry) < 0)
        return UA_STATUSCODE_BADOUTOFMEMORY;

    ZIP_REMOVE(PyNodeTree, &store->root, entry);
    store->size--;
    /* Become a tombstone immediately. Native payload reclamation and release
     * of the nodestore pin wait for outstanding native borrows. */
    entry->server = NULL;
    entry->deleted = true;
    cleanupEntry(entry);
    return UA_STATUSCODE_GOOD;
}

static const UA_NodeId *
storeGetReferenceTypeId(UA_Nodestore *ns, UA_Byte index) {
    PyNodeStore *store = (PyNodeStore *)ns;
    if(index >= store->referenceTypeCounter)
        return NULL;
    return &store->referenceTypeIds[index];
}

typedef struct {
    UA_NodestoreVisitor visitor;
    void *context;
} VisitorData;

static void *
visitNode(void *data, PyNode *entry) {
    VisitorData *visitor = (VisitorData *)data;
    visitor->visitor(visitor->context, &entry->node);
    return NULL;
}

static void
storeIterate(UA_Nodestore *ns, UA_NodestoreVisitor visitor,
             void *visitorContext) {
    PyNodeStore *store = (PyNodeStore *)ns;
    VisitorData data = {visitor, visitorContext};
    ZIP_ITER(PyNodeTree, &store->root, visitNode, &data);
}

static void *
detachNode(void *data, PyNode *entry) {
    (void)data;
    if(cacheDetachedIdentity(entry) < 0)
        PyErr_Clear();
    entry->server = NULL;
    entry->deleted = true;
    /* Server teardown must not leave native borrows outstanding. */
    UA_assert(entry->nativeRefs == 0);
    cleanupEntry(entry);
    return NULL;
}

static void
storeFree(UA_Nodestore *ns) {
    PyNodeStore *store = (PyNodeStore *)ns;
    ZIP_ITER(PyNodeTree, &store->root, detachNode, NULL);
    UA_assert(LIST_EMPTY(&store->promotedNodes));
    for(size_t i = 0; i < store->referenceTypeCounter; i++)
        UA_NodeId_clear(&store->referenceTypeIds[i]);
    UA_free(store);
}

UA_Nodestore *
pyNodeStore_new(PyServer *server) {
    UA_assert(PyGILState_Check());
    if(PyType_Ready(&PyNodeBaseType) < 0)
        return NULL;

    PyNodeStore *store = (PyNodeStore *)UA_calloc(1, sizeof(PyNodeStore));
    if(!store)
        return NULL;

    store->server = server;
    ZIP_INIT(&store->root);
    LIST_INIT(&store->promotedNodes);

    store->ns.free = storeFree;
    store->ns.newNode = storeNewNode;
    store->ns.deleteNode = storeDeleteNode;
    store->ns.getNode = storeGetNode;
    store->ns.getNodeFromPtr = storeGetNodeFromPtr;
    store->ns.releaseNode = storeReleaseNode;
    store->ns.getNodeCopy = storeGetNodeCopy;
    store->ns.insertNode = storeInsertNode;
    store->ns.replaceNode = storeRejectReplaceNode;
    store->ns.removeNode = storeRemoveNode;
    store->ns.getReferenceTypeId = storeGetReferenceTypeId;
    store->ns.iterate = storeIterate;

    store->ns.getEditNode =
        (UA_Node *(*)(UA_Nodestore *, const UA_NodeId *, UA_UInt32,
                      UA_ReferenceTypeSet, UA_BrowseDirection))storeGetNode;
    store->ns.getEditNodeFromPtr =
        (UA_Node *(*)(UA_Nodestore *, UA_NodePointer, UA_UInt32,
                      UA_ReferenceTypeSet, UA_BrowseDirection))storeGetNodeFromPtr;

    return &store->ns;
}

static PyNodeStore *
getStore(PyServer *server) {
    if(!server || !server->server)
        return NULL;
    UA_Nodestore *ns = UA_Server_getConfig(server->server)->nodestore;
    if(!ns || ns->newNode != storeNewNode)
        return NULL;
    return (PyNodeStore *)ns;
}

static PyNodeCallback *
callbackSlot(PyNode *entry, PyNodeCallbackKind kind) {
    switch(kind) {
    case PY_NODE_CALLBACK_CALL:
        if(entry->node.head.nodeClass != UA_NODECLASS_METHOD)
            return NULL;
        return &entry->callbacks.method.call;
    case PY_NODE_CALLBACK_READ:
        if(entry->node.head.nodeClass != UA_NODECLASS_VARIABLE &&
           entry->node.head.nodeClass != UA_NODECLASS_VARIABLETYPE)
            return NULL;
        return &entry->callbacks.variable.read;
    case PY_NODE_CALLBACK_WRITE:
        if(entry->node.head.nodeClass != UA_NODECLASS_VARIABLE &&
           entry->node.head.nodeClass != UA_NODECLASS_VARIABLETYPE)
            return NULL;
        return &entry->callbacks.variable.write;
    }
    return NULL;
}

PyObject *
pyNodeStore_getCallback(void *nodeContext, PyNodeCallbackKind kind,
                        PyObject **receiver) {
    if(!nodeContext)
        return NULL;
    PyNode *entry = (PyNode *)nodeContext;
    PyNodeCallback *slot = callbackSlot(entry, kind);
    if(!slot || !slot->callable)
        return NULL;
    if(receiver)
        *receiver = Py_XNewRef(slot->receiver);
    return Py_NewRef(slot->callable);
}

UA_Boolean
pyNodeStore_hasCallback(void *nodeContext, PyNodeCallbackKind kind) {
    if(!nodeContext)
        return false;
    PyNodeCallback *slot = callbackSlot((PyNode *)nodeContext, kind);
    return slot && slot->callable;
}

UA_StatusCode
pyNodeStore_setCallback(void *nodeContext, PyNodeCallbackKind kind,
                        PyObject *callback, PyObject *receiver) {
    if(!nodeContext)
        return UA_STATUSCODE_BADNODEIDUNKNOWN;
    PyNode *entry = (PyNode *)nodeContext;
    PyNodeCallback *slot = callbackSlot(entry, kind);
    if(!slot)
        return UA_STATUSCODE_BADNODECLASSINVALID;
    if(Py_REFCNT(entry) == 0) {
        PyErr_SetString(PyExc_RuntimeError,
                        "callback node must be promoted before binding");
        return UA_STATUSCODE_BADINTERNALERROR;
    }
    PyObject *oldCallable = slot->callable;
    PyObject *oldReceiver = slot->receiver;
    slot->callable = Py_XNewRef(callback);
    slot->receiver = callback ? Py_XNewRef(receiver) : NULL;
    Py_XDECREF(oldCallable);
    Py_XDECREF(oldReceiver);
    return UA_STATUSCODE_GOOD;
}

PyObject *
pyNodeStore_getMethodOwner(void *methodContext, void *objectContext) {
    if(!methodContext || !objectContext)
        return NULL;
    PyNode *entry = (PyNode *)methodContext;
    if(entry->node.head.nodeClass != UA_NODECLASS_METHOD ||
       (void *)entry->constructionOwner != objectContext)
        return NULL;
    return Py_NewRef(entry->constructionOwner);
}

int
pyNodeStore_traverse(PyServer *server, visitproc visit, void *arg) {
    PyNodeStore *store = getStore(server);
    if(!store)
        return 0;
    PyNode *entry;
    LIST_FOREACH(entry, &store->promotedNodes, promotedEntry) {
        int result = visit((PyObject *)entry, arg);
        if(result)
            return result;
    }
    return 0;
}

static void
promoteForOwnership(PyNodeStore *store, PyNode *entry) {
    if(Py_REFCNT(entry) == 0) {
        Py_SET_REFCNT(entry, 1);
        PyObject_GC_Track(entry);
    }
    linkPromotedNode(store, entry);
}

PyObject *
pyNodeBaseType(void) {
    if(PyType_Ready(&PyNodeBaseType) < 0)
        return NULL;
    return Py_NewRef((PyObject *)&PyNodeBaseType);
}

static int
initializeNodeDict(PyNode *entry, PyObject *backend) {
    PyObject *dict = PyDict_New();
    if(!dict || PyDict_SetItemString(dict, "_backend", backend) < 0) {
        Py_XDECREF(dict);
        return -1;
    }
    entry->dict = dict;
    return 0;
}

static PyObject *
nodeObject(PyServer *server, PyNode *entry,
           PyObject *type, PyObject *backend) {
    if(!entry || entry->node.head.context != entry) {
        PyErr_SetString(PyExc_RuntimeError,
                        "native node does not carry its canonical PyNode context");
        return NULL;
    }
    if(entry->server != server) {
        PyErr_SetString(PyExc_ReferenceError,
                        "native node is detached from this server");
        return NULL;
    }

    if(Py_REFCNT(entry) == 0 || Py_TYPE(entry) == &PyNodeBaseType) {
        if(!type || !backend) {
            PyErr_SetString(PyExc_RuntimeError,
                            "callback node was not promoted before dispatch");
            return NULL;
        }
        if(!PyType_Check(type) ||
           !PyType_IsSubtype((PyTypeObject *)type, &PyNodeBaseType) ||
           ((PyTypeObject *)type)->tp_basicsize != sizeof(PyNode)) {
            PyErr_SetString(PyExc_TypeError,
                            "callback node type must derive from o6.Node");
            return NULL;
        }
        if(initializeNodeDict(entry, backend) < 0)
            return NULL;
        Py_INCREF(type);
        Py_SET_TYPE(entry, (PyTypeObject *)type);
        promoteForOwnership(getStore(server), entry);
    } else if(type && !PyObject_TypeCheck((PyObject *)entry,
                                          (PyTypeObject *)type)) {
        /* Runtime node classes for two marker classes are siblings because
         * both include the fixed native Node base. Compare their concrete
         * marker classes as well, so an implementation-only subtype remains
         * retrievable through its declared UA VariableType/ObjectType. */
        PyObject *entryBases = (PyObject *)Py_TYPE(entry)->tp_bases;
        PyObject *requestedBases = (PyObject *)((PyTypeObject *)type)->tp_bases;
        PyObject *entryConcrete =
            PyTuple_Check(entryBases) && PyTuple_GET_SIZE(entryBases) >= 2
                ? PyTuple_GET_ITEM(entryBases, 0)
                : NULL;
        PyObject *requestedConcrete =
            PyTuple_Check(requestedBases) && PyTuple_GET_SIZE(requestedBases) >= 2
                ? PyTuple_GET_ITEM(requestedBases, 0)
                : NULL;
        PyObject *entryNodeBase =
            entryConcrete ? PyTuple_GET_ITEM(entryBases, 1) : NULL;
        PyObject *requestedNodeBase =
            requestedConcrete ? PyTuple_GET_ITEM(requestedBases, 1) : NULL;
        UA_Boolean validConcreteTypes = entryConcrete && requestedConcrete &&
            PyType_Check(entryConcrete) && PyType_Check(requestedConcrete) &&
            PyType_Check(entryNodeBase) && PyType_Check(requestedNodeBase) &&
            PyType_IsSubtype((PyTypeObject *)entryNodeBase, &PyNodeBaseType) &&
            PyType_IsSubtype((PyTypeObject *)requestedNodeBase, &PyNodeBaseType);
        UA_Boolean compatible = validConcreteTypes &&
            PyType_IsSubtype((PyTypeObject *)entryConcrete,
                             (PyTypeObject *)requestedConcrete);
        UA_Boolean canNarrow = validConcreteTypes && Py_REFCNT(entry) == 1 &&
            PyType_IsSubtype((PyTypeObject *)requestedConcrete,
                             (PyTypeObject *)entryConcrete);
        if(compatible)
            return Py_NewRef((PyObject *)entry);
        if(canNarrow) {
            PyTypeObject *oldType = Py_TYPE(entry);
            Py_INCREF(type);
            Py_SET_TYPE(entry, (PyTypeObject *)type);
            Py_DECREF(oldType);
            return Py_NewRef((PyObject *)entry);
        }
        PyErr_Clear();
        PyErr_Format(PyExc_TypeError,
                     "node is already exposed as %.200s, not %.200s",
                     Py_TYPE(entry)->tp_name,
                     ((PyTypeObject *)type)->tp_name);
        return NULL;
    }
    return Py_NewRef((PyObject *)entry);
}

PyObject *
pyNodeStore_nodeObject(PyServer *server, const UA_Node *node,
                       PyObject *type, PyObject *backend) {
    if(!node) {
        PyErr_SetString(PyExc_RuntimeError, "native node is NULL");
        return NULL;
    }
    PyNode *entry = container_of(node, PyNode, node);
    return nodeObject(server, entry, type, backend);
}

PyObject *
pyNodeStore_contextObject(PyServer *server, void *nodeContext,
                          PyObject *type, PyObject *backend) {
    if(!nodeContext) {
        PyErr_SetString(PyExc_RuntimeError, "native node context is NULL");
        return NULL;
    }
    return nodeObject(server, (PyNode *)nodeContext, type, backend);
}

UA_Node *
pyNodeStore_contextNode(PyServer *server, void *nodeContext) {
    if(!nodeContext) {
        PyErr_SetString(PyExc_RuntimeError, "native node context is NULL");
        return NULL;
    }
    PyNode *entry = (PyNode *)nodeContext;
    if(entry->node.head.context != entry) {
        PyErr_SetString(PyExc_RuntimeError,
                        "native node does not carry its canonical PyNode context");
        return NULL;
    }
    if(entry->server != server) {
        PyErr_SetString(PyExc_ReferenceError,
                        "native node is detached from this server");
        return NULL;
    }
    return &entry->node;
}

static PyObject *
getNode(PyServer *server, PyObject *args) {
    PyObject *pyNodeId;
    PyObject *pyType;
    PyObject *backend;
    if(!PyArg_ParseTuple(args, "OOO", &pyNodeId, &pyType, &backend))
        return NULL;
    if(!server->server) {
        PyErr_SetString(PyExc_RuntimeError, "server is already closed");
        return NULL;
    }
    if(!PyType_Check(pyType) ||
       !PyType_IsSubtype((PyTypeObject *)pyType, &PyNodeBaseType)) {
        PyErr_SetString(PyExc_TypeError,
                        "node type must derive from o6.Node");
        return NULL;
    }
    if(((PyTypeObject *)pyType)->tp_basicsize != sizeof(PyNode)) {
        PyErr_SetString(PyExc_TypeError,
                        "node subclasses cannot add native instance layout");
        return NULL;
    }

    UA_NodeId nodeId;
    const UA_DataTypeArray *customTypes =
        UA_Server_getConfig(server->server)->customDataTypes;
    if(extract_nodeid(pyNodeId, &nodeId, &server->nsMapPy2UA,
                      customTypes) < 0)
        return NULL;

    PyNodeStore *store = getStore(server);
    UA_Nodestore *ns = store ? &store->ns : NULL;
    if(!ns) {
        UA_NodeId_clear(&nodeId);
        PyErr_SetString(PyExc_RuntimeError,
                        "server does not use the PyNode nodestore");
        return NULL;
    }

    const UA_Node *native = storeGetNode(ns, &nodeId,
                                         UA_NODEATTRIBUTESMASK_ALL,
                                         UA_REFERENCETYPESET_ALL,
                                         UA_BROWSEDIRECTION_BOTH);
    UA_NodeId_clear(&nodeId);
    if(!native) {
        PyErr_SetObject(PyExc_KeyError, pyNodeId);
        return NULL;
    }

    PyObject *result = pyNodeStore_nodeObject(server, native, pyType, backend);
    storeReleaseNode(ns, native);
    return result;
}

PyObject *
pyNodeStore_getNode(PyServer *server, PyObject *args) {
    return getNode(server, args);
}

UA_Node *
pyNodeStore_attachedNode(PyObject *node, PyServer **server) {
    if(!PyObject_TypeCheck(node, &PyNodeBaseType)) {
        PyErr_SetString(PyExc_TypeError,
                        "native attribute access requires an o6.Node");
        return NULL;
    }
    PyNode *entry = (PyNode *)node;
    if(!entry->server) {
        if(entry->deleted)
            PyErr_SetString(PyExc_ReferenceError,
                            "the OPC UA node has been deleted");
        else
            PyErr_SetString(PyExc_TypeError,
                            "native attribute access requires an attached server node");
        return NULL;
    }
    if(server)
        *server = entry->server;
    return &entry->node;
}
