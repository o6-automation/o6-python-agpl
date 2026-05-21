# open62541 Client API — Python Coverage

Coverage of the [open62541 Client API](https://open62541.org/doc/master/client.html) in the `o6` Python module.

**Legend:**
- ✅ Covered — fully accessible from Python
- 🔧 Partial — accessible via a lower-level path (e.g. raw service call), but no dedicated high-level wrapper
- ❌ Not covered — no Python access currently
- 🔒 Managed internally — not needed as user-facing Python API

---

## Client Lifecycle & Configuration

| C Function Group | Python API | Coverage | Notes |
|---|---|---|---|
| `UA_Client_new` / `UA_Client_newWithConfig` | — | 🔒 | Created automatically when constructing `Client(...)` |
| `UA_Client_getConfig` | `client.config` | 🔒 | Returned as `_o6.ClientConfig`; user sets fields on it |
| `UA_Client_getContext` / `UA_Client_getContext` macro | — | ❌ | `clientContext` pointer not exposed |
| `UA_Client_delete` | — | 🔒 | Called automatically in `__del__` / `__exit__` |
| `UA_Client_run_iterate` | — | 🔒 | Driven by the internal asyncio event-loop worker thread |
| `UA_ClientConfig_copy` / `UA_ClientConfig_clear` / `UA_ClientConfig_delete` | — | 🔒 | Internal lifecycle helpers; not needed from Python |
| `UA_ClientConfig_setAuthenticationUsername` | `Client(endpoint_url=..., username=..., password=...)` or `client.connect(username=..., password=...)` | ✅ | Username/password set before connecting |
| `UA_ClientConfig_setAuthenticationCert` | `Client(certificate=..., private_key=...)` | ✅ | Certificate authentication configured at init |

---

## State / Status

| C Function Group | Python API | Coverage | Notes |
|---|---|---|---|
| `UA_Client_getState` | `client.get_state()` · `client.is_connected()` · `client.is_connected()` | ✅ | Returns `(SecureChannelState, SessionState, connectStatus)` |

---

## Connect to a Server

| C Function Group | Python API | Coverage | Notes |
|---|---|---|---|
| `UA_Client_connect` / `UA_Client_connectAsync` | `client.connect()` | ✅ | Async variant used internally; sync mode blocks until connected |
| `UA_Client_connectUsername` | `client.connect(username=..., password=...)` | ✅ | Sets `UserIdentityToken` then calls `connectAsync` |
| `UA_Client_connectSecureChannel` / `UA_Client_connectSecureChannelAsync` | `client.connect(no_session=True)` | ✅ | Opens only SecureChannel (no Session) |
| `UA_Client_startListeningForReverseConnect` | `client.start_reverse_connect(listen_hostnames, port)` | ✅ | Reverse-connect listener |
| `UA_Client_disconnect` / `UA_Client_disconnectAsync` | `client.disconnect()` | ✅ | Async variant used internally |
| `UA_Client_disconnectSecureChannel` / `UA_Client_disconnectSecureChannelAsync` | `client.disconnect(close_session=False)` | ✅ | Closes only SecureChannel, keeps Session alive |

---

## Session Management

| C Function Group | Python API | Coverage | Notes |
|---|---|---|---|
| `UA_Client_getSessionAuthenticationToken` | `client.get_session_authentication_token()` | ✅ | Returns `(NodeId, bytes)` (authToken, serverNonce) |
| `UA_Client_activateCurrentSession` / `UA_Client_activateCurrentSessionAsync` | `client.activate_current_session()` | ✅ | Re-activates the current session |
| `UA_Client_activateSession` / `UA_Client_activateSessionAsync` | `client.activate_session(auth_token, server_nonce)` | ✅ | Transfers a session from another client |

---

## Discovery

| C Function Group | Python API | Coverage | Notes |
|---|---|---|---|
| `UA_Client_getEndpoints` | `client.get_endpoints()` · `client.service_get_endpoints(GetEndpointsRequest)` | ✅ | Dispatched via `__UA_Client_AsyncService` |
| `UA_Client_findServers` | `client.find_servers()` · `client.service_find_servers(FindServersRequest)` | ✅ | Returns list of `ApplicationDescription` |
| `UA_Client_findServersOnNetwork` | `client.find_servers_on_network()` · `client.service_find_servers_on_network(FindServersOnNetworkRequest)` | ✅ | LDS-only; returns list of `ServerOnNetwork` |

---

## Raw Services — Attribute Service Set

| C Function Group | Python API | Coverage | Notes |
|---|---|---|---|
| `UA_Client_Service_read` | `client.service_read(ReadRequest) → ReadResponse` | ✅ | Synchronous batch read |
| `UA_Client_Service_write` | `client.service_write(WriteRequest) → WriteResponse` | ✅ | Synchronous batch write |
| `UA_Client_Service_historyRead` | `client.service_history_read(HistoryReadRequest) → HistoryReadResponse` | ✅ | Raw history read (requires `UA_ENABLE_HISTORIZING`) |
| `UA_Client_Service_historyUpdate` | `client.service_history_update(HistoryUpdateRequest) → HistoryUpdateResponse` | ✅ | Raw history update |

---

## Raw Services — Method Service Set

| C Function Group | Python API | Coverage | Notes |
|---|---|---|---|
| `UA_Client_Service_call` | `client.service_call(CallRequest) → CallResponse` | ✅ | Batch method call |

---

## Raw Services — NodeManagement Service Set

| C Function Group | Python API | Coverage | Notes |
|---|---|---|---|
| `UA_Client_Service_addNodes` | `client.service_add_nodes(AddNodesRequest) → AddNodesResponse` | ✅ | |
| `UA_Client_Service_addReferences` | `client.service_add_references(AddReferencesRequest) → AddReferencesResponse` | ✅ | |
| `UA_Client_Service_deleteNodes` | `client.service_delete_nodes(DeleteNodesRequest) → DeleteNodesResponse` | ✅ | |
| `UA_Client_Service_deleteReferences` | `client.service_delete_references(DeleteReferencesRequest) → DeleteReferencesResponse` | ✅ | |

---

## Raw Services — View Service Set

| C Function Group | Python API | Coverage | Notes |
|---|---|---|---|
| `UA_Client_Service_browse` | `client.service_browse(BrowseRequest) → BrowseResponse` | ✅ | |
| `UA_Client_Service_browseNext` | `client.service_browse_next(BrowseNextRequest) → BrowseNextResponse` | ✅ | |
| `UA_Client_Service_translateBrowsePathsToNodeIds` | `client.service_translate_browse_paths_to_nodeids(TranslateBrowsePathsToNodeIdsRequest)` | ✅ | |
| `UA_Client_Service_registerNodes` | `client.service_register_nodes(RegisterNodesRequest) → RegisterNodesResponse` | ✅ | |
| `UA_Client_Service_unregisterNodes` | `client.service_unregister_nodes(UnregisterNodesRequest) → UnregisterNodesResponse` | ✅ | |

---

## Raw Services — Query Service Set

| C Function Group | Python API | Coverage | Notes |
|---|---|---|---|
| `UA_Client_Service_queryFirst` | `client.service_queryFirst(QueryFirstRequest) → QueryFirstResponse` | ✅ | |
| `UA_Client_Service_queryNext` | `client.service_queryNext(QueryNextRequest) → QueryNextResponse` | ✅ | |

---

## Highlevel — Read / Write Value

| C Function Group | Python API | Coverage | Notes |
|---|---|---|---|
| `UA_Client_read` / `UA_Client_readValueAttribute` | `client.read(nodeid, attribute_id?)` | ✅ | Returns value or `DataValue`; defaults to `Value` attribute |
| `UA_Client_readAttribute_async` / `UA_Client_readValueAttribute_async` etc. | — | 🔧 | Async variants cover all attributes; accessible via `service_read` with a `ReadRequest` built manually |
| `UA_Client_write` / `UA_Client_writeValueAttribute` | `client.write(nodeid, value)` | ✅ | Convenience wrapper |
| `UA_Client_writeValueAttribute_scalar` / `UA_Client_writeValueAttributeEx` | — | 🔧 | Accessible via `service_write` with a `WriteRequest` |
| All other `UA_Client_read*Attribute` / `UA_Client_write*Attribute` variants (NodeClass, BrowseName, DisplayName, Description, WriteMask, IsAbstract, Symmetric, InverseName, ContainsNoLoops, EventNotifier, DataType, ValueRank, ArrayDimensions, AccessLevel, AccessLevelEx, UserAccessLevel, MinimumSamplingInterval, Historizing, Executable, UserExecutable, DatatypeDefinition, …) | — | 🔧 | No per-attribute high-level wrappers; use `client.service_read(ReadRequest)` with the appropriate `attributeId` |

---

## Highlevel — Historical Access

| C Function Group | Python API | Coverage | Notes |
|---|---|---|---|
| `UA_Client_HistoryRead_raw` | `client.history_read(nodeid, start, end, ...)` | ✅ | |
| `UA_Client_HistoryRead_modified` | `client.history_read_modified(nodeid, start, end, ...)` | ✅ | |
| `UA_Client_HistoryRead_events` | — | 🔧 | Use `client.service_history_read(HistoryReadRequest)` with event filter details |
| `UA_Client_HistoryUpdate_insert` / `_replace` / `_update` | `client.history_update_insert(nodeid, values)` / `client.history_update_replace(nodeid, values)` | ✅ | Specialized per update kind |
| `UA_Client_HistoryUpdate_deleteRaw` | `client.history_delete(nodeid, start, end)` | ✅ | |

---

## Highlevel — Method Calling

| C Function Group | Python API | Coverage | Notes |
|---|---|---|---|
| `UA_Client_call` / `UA_Client_call_async` | `client.call(object_id, method_id, *inputs)` | ✅ | Async variant used internally; sync and async Python modes both supported |

---

## Highlevel — Browsing

| C Function Group | Python API | Coverage | Notes |
|---|---|---|---|
| `UA_Client_browse` / `UA_Client_browseNext` | `client.browse(nodeid, ...)` | ✅ | Automatically follows continuation points |
| `UA_Client_translateBrowsePathToNodeIds` | — | 🔧 | Use `client.service_translate_browse_paths_to_nodeids(...)` directly |
| `UA_Client_NamespaceGetIndex` | — | ❌ | No Python wrapper; use `service_read` to read namespace array |
| `UA_Client_forEachChildNodeCall` | — | ❌ | No Python wrapper; iterate browse results manually |

---

## Highlevel — Node Management

| C Function Group | Python API | Coverage | Notes |
|---|---|---|---|
| `UA_Client_addVariableNode` / `_async` | `client.add_variable_node(...)` | ✅ | |
| `UA_Client_addVariableTypeNode` / `_async` | `client.add_variable_type_node(...)` | ✅ | |
| `UA_Client_addObjectNode` / `_async` | `client.add_object_node(...)` | ✅ | |
| `UA_Client_addObjectTypeNode` / `_async` | `client.add_object_type_node(...)` | ✅ | |
| `UA_Client_addViewNode` / `_async` | `client.add_view_node(...)` | ✅ | |
| `UA_Client_addReferenceTypeNode` / `_async` | `client.add_reference_type_node(...)` | ✅ | |
| `UA_Client_addDataTypeNode` / `_async` | `client.add_data_type_node(...)` | ✅ | |
| `UA_Client_addMethodNode` / `_async` | `client.add_method_node(...)` | ✅ | |
| `UA_Client_addReference` | `client.add_reference(source, ref_type, is_forward, target, ...)` | ✅ | |
| `UA_Client_deleteReference` | `client.delete_reference(source, ref_type, is_forward, target, ...)` | ✅ | |
| `UA_Client_deleteNode` | `client.delete_node(nodeid, delete_target_references)` | ✅ | |

---

## Subscriptions

| C Function Group | Python API | Coverage | Notes |
|---|---|---|---|
| `UA_Client_Subscriptions_create` / `_async` | `client.create_subscription(...)` · `client.service_createSubscription(CreateSubscriptionRequest)` | ✅ | Async variant used internally |
| `UA_Client_Subscriptions_modify` / `_async` | `client.service_modifySubscription(ModifySubscriptionRequest)` | ✅ | No dedicated high-level modify wrapper yet |
| `UA_Client_Subscriptions_delete` / `_async` | `client.service_deleteSubscription(DeleteSubscriptionsRequest)` | ✅ | Async variant used internally |
| `UA_Client_Subscriptions_deleteSingle` | `Subscription.delete()` | ✅ | Deletes just that subscription; calls `service_deleteSubscription` with a single ID internally |
| `UA_Client_Subscriptions_setPublishingMode` | `client.service_setPublishingMode(SetPublishingModeRequest)` | ✅ | |
| `UA_Client_Subscriptions_getContext` / `UA_Client_Subscriptions_setContext` | — | 🔒 | Context is managed internally by the Python `Subscription` object |

---

## MonitoredItems

| C Function Group | Python API | Coverage | Notes |
|---|---|---|---|
| `UA_Client_MonitoredItems_createDataChanges` / `_async` · `createDataChange` (single) | `client.monitor_data_change(sub_id, nodeid, callback)` · `sub.monitor_data_change(...)` · `client.service_createMonitoredItems(...)` | ✅ | Async variant used internally |
| `UA_Client_MonitoredItems_createEvents` / `_async` · `createEvent` (single) | `client.monitor_event(sub_id, nodeid, event_filter, callback)` · `sub.monitor_event(...)` · `client.service_createEventMonitoredItems(...)` | ✅ | Async variant used internally |
| `UA_Client_MonitoredItems_delete` / `_async` | `client.service_deleteMonitoredItems(DeleteMonitoredItemsRequest)` | ✅ | Async variant used internally |
| `UA_Client_MonitoredItems_deleteSingle` | `MonitoredItem.delete()` | ✅ | Deletes just that monitored item; calls `service_deleteMonitoredItems` with a single ID internally |
| `UA_Client_MonitoredItems_modify` / `_async` | `client.service_modifyMonitoredItems(ModifyMonitoredItemsRequest)` | ✅ | Async variant used internally |
| `UA_Client_MonitoredItems_setMonitoringMode` / `_async` | `client.service_setMonitoringMode(SetMonitoringModeRequest)` | ✅ | Async variant used internally |
| `UA_Client_MonitoredItems_setTriggering` / `_async` | `client.service_setTriggering(SetTriggeringRequest)` | ✅ | Async variant used internally |
| `UA_Client_MonitoredItem_getContext` / `UA_Client_MonitoredItem_setContext` | — | 🔒 | Context managed internally |

---

## Application Notification Callbacks

| C Function Group | Python API | Coverage | Notes |
|---|---|---|---|
| `config.globalNotificationCallback` | `client.set_global_notification_callback(callback)` | ✅ | `callback(type: int, payload: dict)` |
| `config.lifecycleNotificationCallback` | `client.set_lifecycle_notification_callback(callback)` | ✅ | Subset: only lifecycle events |
| `config.serviceNotificationCallback` | `client.set_service_notification_callback(callback)` | ✅ | Subset: only service events |
| `config.stateCallback` (old-style) | — | 🔧 | Use `set_lifecycle_notification_callback` instead |
| `config.inactivityCallback` | `client.set_inactivity_callback(callback)` | ✅ | Fired when connectivity check gets no response |
| `config.subscriptionInactivityCallback` | `client.set_subscription_inactivity_callback(callback)` | ✅ | `callback(sub_id: int)` |

---

## Client Utility Functions — Timed / Repeated Callbacks

| C Function Group | Python API | Coverage | Notes |
|---|---|---|---|
| `UA_Client_addTimedCallback` | `client.add_timed_callback(callback, delay_ms)` | ✅ | Returns callback ID |
| `UA_Client_addRepeatedCallback` | `client.add_repeated_callback(callback, interval_ms)` | ✅ | Returns callback ID |
| `UA_Client_changeRepeatedCallbackInterval` | `client.change_repeated_callback_interval(callback_id, interval_ms)` | ✅ | |
| `UA_Client_removeCallback` / `UA_Client_removeRepeatedCallback` | `client.remove_callback(callback_id)` | ✅ | |

---

## Client Utility Functions — Namespace

| C Function Group | Python API | Coverage | Notes |
|---|---|---|---|
| `UA_Client_getNamespaceUri` | `client.get_namespace_uri(index)` | ✅ | |
| `UA_Client_getNamespaceIndex` | `client.get_namespace_index(uri)` | ✅ | |
| `UA_Client_addNamespace` | `client.add_namespace(uri)` | ✅ | |

---

## Client Utility Functions — Data Types

| C Function Group | Python API | Coverage | Notes |
|---|---|---|---|
| `UA_Client_findDataType` | `client.find_data_type(type_id)` | ✅ | Returns `dict` or `None` |
| `UA_Client_getRemoteDataTypes` | `client.get_remote_data_types(type_nodes)` | ✅ | Registers returned types in client config |

---

## Client Utility Functions — Connection Attributes

| C Function Group | Python API | Coverage | Notes |
|---|---|---|---|
| `UA_Client_getConnectionAttribute` | — | ❌ | Not exposed (runtime attrs: `serverDescription`, `securityPolicyUri`, `securityMode`) |
| `UA_Client_getConnectionAttributeCopy` | — | ❌ | |
| `UA_Client_getConnectionAttribute_scalar` | — | ❌ | |

---

## Asynchronous Services — Cancellation & SecureChannel Renewal

| C Function Group | Python API | Coverage | Notes |
|---|---|---|---|
| `__UA_Client_AsyncService` | — | 🔒 | Used internally by all async service dispatch; not exposed directly |
| `UA_Client_sendAsyncReadRequest` / `sendAsyncWriteRequest` / `sendAsyncBrowseRequest` / `sendAsyncBrowseNextRequest` | — | 🔧 | Covered by `service_read`, `service_write`, `service_browse`, `service_browse_next` respectively |
| `UA_Client_cancelByRequestHandle` | — | ❌ | Not exposed |
| `UA_Client_cancelByRequestId` | — | ❌ | Not exposed |
| `UA_Client_renewSecureChannel` | — | ❌ | Not exposed; renewal is handled automatically by the event loop |

