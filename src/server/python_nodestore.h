/* Copyright 2026 (c) o6 Automation GmbH */
#ifndef PYO6_PYTHON_NODESTORE_H_
#define PYO6_PYTHON_NODESTORE_H_

#include "server.h"
#include <open62541/plugin/nodestore.h>

typedef enum {
    PY_NODE_CALLBACK_CALL,
    PY_NODE_CALLBACK_READ,
    PY_NODE_CALLBACK_WRITE
} PyNodeCallbackKind;

/* Create the stable-pointer nodestore used by o6 servers. The returned
 * nodestore owns all native node allocations and is consumed by
 * UA_Server_newWithConfig. */
UA_Nodestore *pyNodeStore_new(PyServer *server);

/* Fixed-layout base for all Python Node classes. Returns a new reference. */
PyObject *pyNodeBaseType(void);

/* Promote and return the canonical node for (nodeId, type, backend). */
PyObject *pyNodeStore_getNode(PyServer *server, PyObject *args);

/* Expose the nodestore's promoted-node pins to Python's cyclic GC as edges
 * owned by the server object. Traversal visits only the promoted-node list,
 * never the complete native nodestore. */
int pyNodeStore_traverse(PyServer *server, visitproc visit, void *arg);

/* Constant-time access from a borrowed native node. `type` and `backend` are
 * required only when the node has not previously been exposed to Python.
 * Returns a new reference. */
PyObject *pyNodeStore_nodeObject(PyServer *server, const UA_Node *node,
                                 PyObject *type, PyObject *backend);

/* Resolve the non-owning PyNode pointer reserved in UA_NodeHead.context.
 * The context form is the callback hot path and performs no container
 * conversion or nodestore lookup. Returns a new reference. */
PyObject *pyNodeStore_contextObject(PyServer *server, void *nodeContext,
                                    PyObject *type, PyObject *backend);

/* Return the embedded native node for a callback context. */
UA_Node *pyNodeStore_contextNode(PyServer *server, void *nodeContext);

/* Node-owned callback slots. Get returns a new reference or NULL without an
 * exception when the slot is empty. Set retains callback; NULL clears it. */
PyObject *pyNodeStore_getCallback(void *nodeContext, PyNodeCallbackKind kind,
                                  PyObject **receiver);
UA_Boolean pyNodeStore_hasCallback(void *nodeContext,
                                   PyNodeCallbackKind kind);
UA_StatusCode pyNodeStore_setCallback(void *nodeContext,
                                      PyNodeCallbackKind kind,
                                      PyObject *callback,
                                      PyObject *receiver);
PyObject *pyNodeStore_getMethodOwner(void *methodContext,
                                     void *objectContext);

/* Node dictionary metadata without materializing an empty dictionary. Get
 * returns a new reference or NULL without an exception when absent. Passing
 * NULL to set removes the key and treats an absent key as success. */
PyObject *pyNodeStore_getMetadata(void *nodeContext, const char *name);
int pyNodeStore_setMetadata(void *nodeContext, const char *name,
                            PyObject *value);

/* Return the stable native node embedded in an attached canonical Python
 * server node. The returned pointer is borrowed from the Python object. */
UA_Node *pyNodeStore_attachedNode(PyObject *node, PyServer **server);

#endif /* PYO6_PYTHON_NODESTORE_H_ */
