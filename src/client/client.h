/* Copyright 2026 (c) o6 Automation GmbH */
#ifndef CLIENT_H_
#define CLIENT_H_

#include "../module.h"
#include <open62541/client.h>

// PyClient structure definition
typedef struct {
    PyObject_HEAD
    UA_Client *client;
    int owns_loop; // Whether the client owns the Python asyncio loop
    PyObject *connectFuture; // While a connect is ongoing
    PyObject *disconnectFuture; // While a disconnect is ongoing
    PyObject *callbackDict; // {callbackId: pyCallable} for timed/repeated callbacks
    PyObject *globalNotificationCallback;     // optional Python callable for all notifications
    PyObject *lifecycleNotificationCallback;  // optional Python callable for lifecycle notifications
    PyObject *serviceNotificationCallback;    // optional Python callable for service notifications
    PyObject *inactivityCallback;             // optional Python callable fired on connectivity check failure
    PyObject *subscriptionInactivityCallback; // optional Python callable fired on subscription timeout
    PyObject *config_cache;          /* cached PyClientConfig singleton — ensures
                                       c.config is always the same object so that
                                       stored cert/key/trust survive across accesses */

    
    UA_NamespaceMapping nsMapPy2UA; /* maps python <-> UA namespaces, local == python, remote == UA */
} PyClient;

// Forward declaration for PyClientConfig
typedef struct {
    PyObject_HEAD
    PyClient *py_client;      // Python client object reference (borrowed)
    PyObject *certificate;    // bytes or NULL — stored for deferred set_encryption
    PyObject *private_key;    // bytes or NULL — stored for deferred set_encryption
    PyObject *trust_list;     // list[bytes] or NULL — stored for deferred set_encryption
    PyObject *revocation_list;// list[bytes] or NULL — stored for deferred set_encryption
    int encryption_applied;   // 1 after UA_ClientConfig_setDefaultEncryption ran; 0 = dirty
} PyClientConfig;
extern PyTypeObject PyClientConfigType;

// Factory to create a PyClientConfig for a given PyClient*
PyObject *PyClientConfig_New(PyClient *py_client);
void PyClientConfig_Invalidate(PyObject *config);

// Client services function declarations
PyObject *pyClient_service_call(PyObject *self, PyObject *args);
PyObject *pyClient_service_read(PyObject *self, PyObject *args);
PyObject *pyClient_service_write(PyObject *self, PyObject *args);
PyObject *pyClient_service_browse(PyObject *self, PyObject *args);
PyObject *pyClient_service_browseNext(PyObject *self, PyObject *args);
PyObject *pyClient_service_registerNodes(PyObject *self, PyObject *args);
PyObject *pyClient_service_unregisterNodes(PyObject *self, PyObject *args);
PyObject *pyClient_service_translateBrowsePathsToNodeIds(PyObject *self, PyObject *args);
PyObject *pyClient_service_addNodes(PyObject *self, PyObject *args);
PyObject *pyClient_service_deleteNodes(PyObject *self, PyObject *args);
PyObject *pyClient_service_addReferences(PyObject *self, PyObject *args);
PyObject *pyClient_service_deleteReferences(PyObject *self, PyObject *args);
PyObject *pyClient_service_historyRead(PyObject *self, PyObject *args);
PyObject *pyClient_service_historyUpdate(PyObject *self, PyObject *args);
PyObject *pyClient_service_queryFirst(PyObject *self, PyObject *args);
PyObject *pyClient_service_queryNext(PyObject *self, PyObject *args);

// Discovery function declarations
PyObject *pyClient_get_endpoints(PyObject *self, PyObject *args);
PyObject *pyClient_find_servers(PyObject *self, PyObject *args);
PyObject *pyClient_find_servers_on_network(PyObject *self, PyObject *args);

// Timed callback function declarations
PyObject *pyClient_add_timed_callback(PyObject *self, PyObject *args);
PyObject *pyClient_add_repeated_callback(PyObject *self, PyObject *args);
PyObject *pyClient_change_repeated_callback_interval(PyObject *self, PyObject *args);
PyObject *pyClient_remove_callback(PyObject *self, PyObject *args);

// Namespace utility function declarations
PyObject *pyClient_get_namespace_uri(PyObject *self, PyObject *args);
PyObject *pyClient_get_namespace_index(PyObject *self, PyObject *args);
PyObject *pyClient_get_application_uri(PyObject *self, PyObject *args);
PyObject *pyClient_apply_namespace_snapshot(PyObject *self, PyObject *args);

// DataType utility function declarations
PyObject *pyClient_find_data_type(PyObject *self, PyObject *args);

// Client subscription services function declarations
PyObject *pyClient_subscriptions_create(PyObject *self, PyObject *args);
PyObject *pyClient_subscriptions_delete(PyObject *self, PyObject *args);
PyObject *pyClient_subscriptions_modify(PyObject *self, PyObject *args);
PyObject *pyClient_subscriptions_setPublishingMode(PyObject *self, PyObject *args);
PyObject *pyClient_monitoredItems_createDataChange(PyObject *self, PyObject *args);
PyObject *pyClient_monitoredItems_createEvent(PyObject *self, PyObject *args);
PyObject *pyClient_monitoredItems_delete(PyObject *self, PyObject *args);
PyObject *pyClient_monitoredItems_modify(PyObject *self, PyObject *args);
PyObject *pyClient_monitoredItems_setMonitoringMode(PyObject *self, PyObject *args);
PyObject *pyClient_monitoredItems_setTriggering(PyObject *self, PyObject *args);

// Utility for async service implementation
typedef struct {
    PyObject *future;
    const UA_DataType *responseType;
    UA_UInt32 requestId;
    void *extraData;
    PyClient *pyClient;            /* owning Python wrapper; provides nsMapPy2UA and access to config->customDataTypes for PY2UA/UA2PY */
} ServiceFuture;

ServiceFuture *createServiceFuture(PyClient *pyClient, const UA_DataType *responseType, void *extraData);
void serviceFuture_abort_before_return(ServiceFuture *sf);

// Resolve a ServiceFuture: convert the response to Python via UA2PY, set it
// on the future, then DECREF + free. On conversion failure, rejects with the
// current Python exception instead. Always consumes sf.
void serviceFuture_resolve(ServiceFuture *sf, void *response);

// Reject a ServiceFuture with an exception string, DECREF + free.
void serviceFuture_reject(ServiceFuture *sf);

void asyncServiceCallback(UA_Client *client, void *userdata, UA_UInt32 requestId, void *response);

// Generic async service call: converts args[0] from Python to a UA request,
// dispatches it via __UA_Client_AsyncService, and returns a future.
PyObject *serviceCallAsync(PyObject *self, PyObject *args,
                           const UA_DataType *requestType,
                           const UA_DataType *responseType);

#endif // CLIENT_H_
