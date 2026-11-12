# Application Notifications

Observe the server's lifecycle, connections, service calls, and audit activity
from Python. These hooks are useful for logging and diagnostics.

| What you want to observe or decide | API |
| --- | --- |
| Server activity, such as a session opening or a service completing | `server.on<category>Notification` on this page |
| Changes to a local Variable's value | [Local monitored items](monitoring.md) |
| OPC UA events delivered to subscribers | [Events](events.md) |
| Whether a session or operation is allowed | [Access control](security.md) |

## Logging server activity

This complete server logs startup and shutdown, plus the session activity of
clients that connect while it is running:

```python
import logging
import o6

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("server.activity")
server = o6.Server(port=4840)

@server.onLifecycleNotification
def on_lifecycle(notification):
    log.info("server %s", notification.lifecycle)

@server.onSessionNotification
def on_session(notification):
    log.info("%s: session %s", o6.server.NotificationType(notification.type).name,
             notification.payload["session-id"])

with server:
    input("Server running; press Enter to stop.")
```

Each handler receives an `o6.Notification`. Its `type` identifies what happened,
`lifecycle` names a lifecycle transition, and `payload` holds fields such as
`"session-id"`. Choose the narrowest category you need; service notifications
can be much more frequent than connection or lifecycle notifications.

## Choosing a category

| Registry | Receives |
| --- | --- |
| `server.onLifecycleNotification` | [Server startup and shutdown](#lifecycle) |
| `server.onSecureChannelNotification` | [Secure-channel open and close](#secure-channel) |
| `server.onSessionNotification` | [Session creation, activation, deactivation, and close](#session) |
| `server.onServiceNotification` | [Service request processing](#service) |
| `server.onSubscriptionNotification` | [Client subscription management](#subscription) |
| `server.onMonitoredItemNotification` | [Client monitored-item management](#monitoreditem) |
| `server.onDiscoveryRegisterServerNotification` | [Application registration with discovery](#discovery-registerserver) |
| `server.onDiscoveryServerOnNetworkNotification` | [mDNS discovery changes](#discovery-serveronnetwork) |
| `server.onAuditNotification` | [Audit activity](#audit), enabled with `server.config.auditingEnabled` |

Subscription and monitored-item notifications describe creation, changes to
configuration, and deletion. Use monitored-item callbacks to receive the values
or OPC UA events themselves.

## Adding, removing, and clearing handlers

The decorators above append handlers in registration order. Each registry can
hold several handlers. These alternative fragments use `server` and
`on_lifecycle` from the example:

```python
server.onLifecycleNotification(on_lifecycle)     # append a handler without a decorator
server.onLifecycleNotification = [on_lifecycle] # replace the whole list
list(server.onLifecycleNotification)            # inspect registered handlers
server.onLifecycleNotification.remove(on_lifecycle)
server.onLifecycleNotification.clear()          # remove all handlers
```

Assignment also accepts one callable or `None` to clear the registry.
`remove()` raises `ValueError` if the handler is absent. You can change
registrations before startup, while running, or after stopping. Register before
startup to observe the initial lifecycle transition. With no registered
handlers, the corresponding Python dispatch is disabled.

## Synchronous and asynchronous handlers

Handlers run on the server's event loop. Keep them short: blocking work delays
the server. A handler can be a plain function or `async def`; returned
awaitables are scheduled on that loop without waiting for them to finish.
Async handlers can overlap, so registration order does not guarantee completion
order.

Use the [callback operation rules](callbacks.md#calling-the-api-from-callbacks)
when a handler accesses nodes. For example, replace the session handler above
with this one to emit an OPC UA event explicitly:

```python
@server.onSessionNotification
async def on_session(notification):
    await server.emitEvent(message=f"session {notification.payload['session-id']}")
```

Registering an application-notification handler alone does not create a client
subscription or publish an OPC UA event.

## Errors don't crash the server

Exceptions in application-notification handlers are logged. Later handlers
still run, and the triggering operation continues. This applies to synchronous
handlers and scheduled awaitables.

These are observation hooks. Access-control callbacks decide whether an
operation is allowed; for example, `activateSession` can reject a connection by
raising `StatusCodeError`. Method and Variable callbacks also communicate their
own operation's status. See [Access Control & Roles](security.md) and
[Callbacks & External Data](callbacks.md) for those separate contracts.

## Notification reference

The following sections list the lifecycle points and payload fields for each
category. Handler fragments use the configured `server` and `log` above and
are alternatives to the corresponding handler in the opening example.

### Reading the payload

A handler receives an [`o6.Notification`](../../api_reference/notification.md).
Besides `type` and `lifecycle`, it has `payload`: a read-only `str -> Any`
mapping of the category's fields, keyed as listed in each section below (for
example `"session-id"`, `"subscription-id"`). Use the fields documented for the
notification type you handle; audit payloads vary by event subtype. For a session notification:

```python
@server.onSessionNotification
def on_session(notification):
    session_id = notification.payload["session-id"]
    print(notification.type, session_id)
```

Values are already converted to the matching Python or `o6` type: a `NodeId`
is an `o6.NodeId`, a `RegisteredServer` is an
`o6.ns.ns0.datatypes.RegisteredServer`, and so on.

### Lifecycle

Fires when the server starts and stops. This category has no payload. The
notification's `lifecycle` field names the point: `"started"`, `"shutdown"`,
`"stopping"` or `"stopped"`. A normal run fires `"started"` once, and
`"stopping"` and `"stopped"` once each on `stop()`. A deferred shutdown can
also fire `"shutdown"`.

```python
@server.onLifecycleNotification
def on_lifecycle(notification):
    ...
```

### Secure Channel

Fires once when a client opens a secure channel and once when it closes. Both
notifications carry the same `securechannel-id`, `remote-address` and
`security-policy-url`. `notification.lifecycle` is `None`; use
`notification.type` (`NotificationType.SECURECHANNEL_OPENED` or
`SECURECHANNEL_CLOSED`) to tell open from close.

```python
@server.onSecureChannelNotification
def on_secure_channel(notification):
    ...
```

The payload:

| Key | Meaning |
| --- | --- |
| `securechannel-id` | The channel's numeric identifier. |
| `connection-manager-name` | Name of the underlying connection manager (e.g. `"tcp-source"`). |
| `connection-id` | The connection manager's own connection identifier. |
| `remote-address` | The remote peer's address, as reported by the network layer. |
| `protocol-version` | Negotiated OPC UA TCP protocol version. |
| `recv-buffer-size` / `send-buffer-size` | Negotiated chunk buffer sizes. |
| `recv-max-message-size` / `send-max-message-size` | Negotiated maximum message sizes. |
| `recv-max-chunk-count` / `send-max-chunk-count` | Negotiated maximum chunk counts. |
| `endpoint-url` | The endpoint URL the client connected to. |
| `security-mode` | The channel's `MessageSecurityMode`. |
| `security-policy-url` | The channel's security policy URI. |
| `certificate-type-id` | NodeId of the certificate type, if any. |
| `remote-certificate` | The remote peer's certificate bytes, if any. |

### Session

Fires as a session is created, activated, deactivated (unbound from its secure
channel) and closed. A client connect/disconnect round trip fires all four, in
that order. `notification.lifecycle` is `None`; use `notification.type` to tell
the points apart.

```python
@server.onSessionNotification
def on_session(notification):
    ...
```

The payload:

| Key | Meaning |
| --- | --- |
| `session-id` | The session's `NodeId`, matching `Session.id` as seen by an [`AccessControl`](../../api_reference/accesscontrol.md) hook on the same session. |
| `securechannel-id` | The owning secure channel's numeric identifier, `0` once the session has been deactivated. |
| `session-name` | The client-supplied session name. |
| `client-description` | The client's `ApplicationDescription`. |
| `client-user-id` | The authenticated user id of the session. |
| `locale-ids` | The client's requested locale ids. |

### Service

Reports service request processing (for example Browse, Read, Write).
`NotificationType.SERVICE_BEGIN` and `SERVICE_END` carry the same `request-id`;
asynchronous processing can also produce `SERVICE_ASYNC` while a request is
pending. `notification.lifecycle` is `None`.

```python
@server.onServiceNotification
def on_service(notification):
    ...
```

The payload:

| Key | Meaning |
| --- | --- |
| `securechannel-id` | The secure channel the request arrived on. |
| `session-id` | The requesting session's `NodeId`, or the null NodeId if no session is bound to the channel. |
| `request-id` | Identifies the request/response pair — the same value on both the begin and end notification for a call. |
| `service-type` | `NodeId` of the request's DataType, e.g. `o6.NodeId(o6.ns.ns0.datatypes.BrowseRequest)`. |

### Subscription

Fires when a real client creates, modifies or deletes a subscription.
`notification.type` tells the points apart
(`NotificationType.SUBSCRIPTION_CREATED`, `_MODIFIED`, `_PUBLISHINGMODE`,
`_TRANSFERRED`, `_DELETED`). `notification.lifecycle` is `None`.

```python
@server.onSubscriptionNotification
def on_subscription(notification):
    ...
```

`Client.connect()` creates an internal subscription during connection setup.
A handler sees its created and deleted notifications too, next to those of
subscriptions the application creates. Use `subscription-id` to tell them
apart.

The payload:

| Key | Meaning |
| --- | --- |
| `session-id` | The owning session's `NodeId`, or the null NodeId if the subscription isn't bound to a session. |
| `subscription-id` | The subscription's identifier, unique within its session. |
| `publishing-interval` | Negotiated publishing interval in milliseconds. |
| `lifetime-count` | Publishing intervals without a Publish request before the subscription is deleted. |
| `max-keepalive-count` | Publishing intervals without notifications before a keepalive is sent. |
| `max-notifications-per-publish` | Cap on notifications per Publish response. |
| `priority` | Publishing priority relative to other subscriptions. |
| `publishing-enabled` | Whether the subscription currently publishes. |

### MonitoredItem

Fires when a real client's monitored item is created, modified, changes
monitoring mode, or is deleted. `notification.type` tells the points apart
(`NotificationType.MONITOREDITEM_CREATED`, `_MODIFIED`, `_MONITORINGMODE`,
`_DELETED`). `notification.lifecycle` is `None`. The `session-id`,
`subscription-id` and `monitoreditem-id` keys are the same at all four points
for one item, so you can track a specific client's monitored item across its
lifetime.

```python
@server.onMonitoredItemNotification
def on_monitored_item(notification):
    ...
```

The payload:

| Key | Meaning |
| --- | --- |
| `session-id` | The owning session's `NodeId`. |
| `subscription-id` | The owning subscription's identifier. |
| `monitoreditem-id` | The item's identifier, unique within its subscription. |
| `target-node` | `NodeId` of the monitored node (creation payload). |
| `attribute-id` | The monitored attribute, an `o6.AttributeId` value. |
| `index-range` | Non-empty if only part of an array value is monitored. |
| `timestamps-to-return` | The requested `TimestampsToReturn`. |
| `monitoring-mode` | The current `MonitoringMode` (`DISABLED`, `SAMPLING`, `REPORTING`). |
| `client-handle` | The client-supplied handle for this item. |
| `sampling-interval` | Negotiated sampling interval in milliseconds. |
| `filter` | The `DataChangeFilter` or `EventFilter` in effect, if any. |
| `queue-size` | Maximum queued notifications before discarding. |
| `discard-oldest` | Whether the oldest or the newest notification is dropped on overflow. |

### Discovery: RegisterServer

Fires when a server is added, updated or removed through the
RegisterServer/RegisterServer2 service or the equivalent local open62541 API
(`UA_Server_registerServer` / `UA_Server_deregisterServer`). Exactly one of
`server-added`, `server-updated`, `server-removed` is `True`.
`notification.lifecycle` is `None`.

```python
@server.onDiscoveryRegisterServerNotification
def on_register_server(notification):
    ...
```

The payload:

| Key | Meaning |
| --- | --- |
| `registered-server` | The registered server's `o6.ns.ns0.datatypes.RegisteredServer` information. |
| `discovery-configuration` | Additional configuration, typically an mDNS config, as a list of `ExtensionObject`. |
| `server-added` / `server-updated` / `server-removed` | Exactly one is `True`, naming which occurred. |
| `securechannel-id` | The secure channel the call arrived on, `0` for a locally-triggered call. |
| `session-id` | The calling session's `NodeId`, or the null NodeId for a locally-triggered call. |

### Discovery: ServerOnNetwork

Fires when mDNS server information is added, updated or removed, through mDNS
or the equivalent local open62541 API (`UA_Server_registerServerOnNetwork` /
`UA_Server_deregisterServerOnNetwork`). It is separate from
`onDiscoveryRegisterServerNotification` and has a disjoint payload; neither
category receives the other's notifications. `notification.lifecycle` is
`None`.

```python
@server.onDiscoveryServerOnNetworkNotification
def on_server_on_network(notification):
    ...
```

The payload:

| Key | Meaning |
| --- | --- |
| `server-on-network` | The discovered server's `o6.ns.ns0.datatypes.ServerOnNetwork` information. |
| `remote-address` | The source address the information was received from, if known. |
| `ttl` | Time-to-live of the DNS information in seconds; `0` means infinite. |
| `server-added` / `server-updated` / `server-removed` | Exactly one is `True`, naming which occurred. |

The server maintains the ServerOnNetwork record list only when
`server.config.serversOnNetworkEnabled` is `True`. Otherwise this category
never fires.

### Audit

Fires for audit-worthy security and management activity: secure-channel
open/close, session create/activate/cancel/close, certificate handling,
node-management operations (AddNodes, DeleteNodes, AddReferences,
DeleteReferences), and write, history and method updates. This category is
opt-in. Set `server.config.auditingEnabled = True` before `start()`; otherwise
open62541 drops every audit notification before it reaches the handlers.

`notification.auditEventType` identifies the audit sub-event. It is the
concrete standard `AuditEventType` subtype as an `o6.NodeId`, for example
`o6.NodeId(o6.ns.ns0.objtypes.AuditActivateSessionEventType)` for a session
activation or `o6.NodeId(o6.ns.ns0.objtypes.AuditAddNodesEventType)` for an
AddNodes call. `notification.lifecycle` is `None`.

```python
server.config.auditingEnabled = True   # before startup

@server.onAuditNotification
def on_audit(notification):
    if notification.auditEventType == o6.NodeId(o6.ns.ns0.objtypes.AuditActivateSessionEventType):
        log.info("session activated: %s", notification.payload["/SessionId"])
```

This handler observes audit activity inside the server. It does not subscribe
to OPC UA events; clients receive events through `monitorEvent` and a
subscription, as described in [Subscriptions & Events](../client/subscriptions.md).

The payload keys are event-filter property paths (`"/ActionTimeStamp"`,
`"/Status"`, `"/SessionId"`, ...), not a fixed key set. Each audit sub-event
has the fields of its position in the `AuditEventType` hierarchy. Access them as
described in [Reading the payload](#reading-the-payload), for example
`notification.payload["/Status"]`.

## Related topics

| Topic | What it covers |
|---|---|
| [`o6.Notification`](../../api_reference/notification.md) | Lifecycle and audit notification fields. |
