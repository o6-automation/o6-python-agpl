# Notification handler

open62541 exposes server-side *application notifications* — typed callbacks
the C library fires at well-defined points during a server's life: when it
starts, when a client opens a secure channel, when a session is created or
activated, when a service call begins or ends, when a subscription or
monitored item is added, when discovery registers another server, when an
audit-worthy action occurs.

`o6` exposes those points as a list-like, decorator-friendly registry
directly on the server: `server.on<category>Notification` is a category
of handlers you can read, call, decorate, replace, and clear.

## Adding, removing, and clearing handlers

A category is a list-like registry. There are four ways to add a handler:

```python
@server.onLifecycleNotification             # decorator (most common)
def a(n): ...

def b(n): ...                               # declare function to be added as callback later, like:

server.onLifecycleNotification(b)           # call form
server.onLifecycleNotification = [a, b]     # wholesale replacement
server.onLifecycleNotification = [a]        # clears b, keeps a
```

And three ways to remove:

```python
server.onLifecycleNotification.remove(a)  # remove one, raises if unknown
server.onLifecycleNotification.clear()    # remove all
server.onLifecycleNotification = []       # also remove all
```

Handlers fire in registration order. Multiple handlers per category are
supported, which is useful when an application library wants to subscribe
to a notification alongside user code without coordinating registration.

The category is a regular list for iteration too:

```python
for handler in server.onLifecycleNotification:
    print("registered:", handler)

print(bool(server.onLifecycleNotification))     # False when no handlers
print(len(server.onLifecycleNotification))      # 0 when no handlers
```

### Hot-swap

Handlers can be added, removed, and replaced at any time — before
`start()`, while the server is running, and after `stop()`:

```python
server = o6.Server(port=4840)
server.start()

# Register a handler while running
@server.onLifecycleNotification
def runtime_watcher(n):
    log.info("lifecycle: %s", n.lifecycle)

# Replace the whole list at any time
server.onLifecycleNotification = [runtime_watcher, another_handler]

# Or clear
server.onLifecycleNotification.clear()

server.stop()
```

A server with no registered handlers pays nothing for the mechanism.

## Synchronous and asynchronous handlers

A handler may be a plain function or `async def`. Async results are
scheduled on the server's event loop, so the server never blocks waiting
on a coroutine:

```python
@server.onLifecycleNotification
async def on_stopped(n):
    await asyncio.sleep(0)
    log.info("lifecycle: %s", n.lifecycle)
```

Returning a coroutine object is enough — no `await` is performed by the
server. Failures inside a coroutine are caught and logged the same way
synchronous failures are.

## Errors don't crash the server

An exception raised inside a handler is caught, logged, and swallowed —
the same pattern other server-side callbacks (Method, Variable,
MonitoredItem, access control) follow. The notification that triggered the
failure is dropped, the surrounding handlers still run, and the server and
the operation that triggered the notification continue.

## Server Notifications

The categories below are the notifications a server currently exposes.
Each one is registered the same way, via its own
`server.on<category>Notification` registry.

### Reading the payload

Every notification the handler receives is an
[`o6.Notification`](../../api_reference/notification.md). Besides `type` and
`lifecycle`, it carries `payload` — a read-only `str -> Any` mapping of
that category's fields, keyed exactly as documented in each section
below (e.g. `"session-id"`, `"subscription-id"`). Access it like any
mapping; a key documented for the category is always present, so a plain
subscript is fine:

```python
@server.onSessionNotification
def on_session(notification):
    session_id = notification.payload["session-id"]
    print(notification.type, session_id)
```

Values are already converted to the matching Python/`o6` type — a
`NodeId` stays an `o6.NodeId`, a `RegisteredServer` stays an
`o6.ns.ns0.datatypes.RegisteredServer`, and so on — so no manual
decoding is needed.

### Lifecycle

Fires when the server starts and when it stops. The lifecycle category has
no payload; the notification's `lifecycle` field names which point
occurred: `"started"`, `"shutdown"`, `"stopping"`, or `"stopped"`. A normal
run fires `"started"` once, and `"stopping"`/`"stopped"` once each on
`stop()` — a deferred shutdown path may also fire `"shutdown"`.

```python
server = o6.Server(port=4840)

@server.onLifecycleNotification
def on_lifecycle(notification):
    ...
```

The handler runs on the server's event loop thread — blocking inside it
blocks the whole server, so offload slow work to a queue or a thread pool.

Calling back into the server needs an `async def` handler. On the server's
own loop `server.emitEvent(...)`, `server.browse(...)`, and every other
`MaybeAwaitable` method return an awaitable; a plain `def` handler never
awaits it, so the call does nothing beyond a `RuntimeWarning: coroutine
was never awaited`.

```python
@server.onSessionNotification
async def on_session(notification):
    await server.emitEvent(message=f"session {notification.payload['session-id']}")
```

### Secure Channel

Fires once when a client opens a secure channel and once when it closes.
Both calls carry the same `securechannel-id`, `remote-address`, and
`security-policy-url`, since they describe the same channel at two points
in its life. `notification.lifecycle` is `None` here — use
`notification.type` (`NotificationType.SECURECHANNEL_OPENED` or
`SECURECHANNEL_CLOSED`) to tell open from close.

```python
server = o6.Server(port=4840)

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

Fires as a session moves through its lifecycle: created, activated,
deactivated (unbound from its secure channel), and closed. A plain client
connect/disconnect round-trip fires all four, in that order.
`notification.lifecycle` is `None` here — use `notification.type` to tell
created/activated/deactivated/closed apart.

```python
server = o6.Server(port=4840)

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

Fires around every individual service request the server processes (e.g.
Browse, Read, Write) — once when processing begins, once when it ends. A
single call fires the handler twice: once with
`NotificationType.SERVICE_BEGIN`, once with `NotificationType.SERVICE_END`,
both carrying the same `request-id`. `notification.lifecycle` is `None`
here.

This category fires at a much higher frequency than lifecycle, secure
channel, or session — once per service call rather than once per
connection — but a server with no handlers registered pays nothing for
it.

```python
server = o6.Server(port=4840)

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

Fires when a real client creates, modifies, or deletes a subscription.
`notification.type` tells the points apart
(`NotificationType.SUBSCRIPTION_CREATED`, `_MODIFIED`,
`_PUBLISHINGMODE`, `_TRANSFERRED`, `_DELETED`); `notification.lifecycle`
is `None` here.

```python
server = o6.Server(port=4840)

@server.onSubscriptionNotification
def on_subscription(notification):
    ...
```

Note that `Client.connect()` creates its own internal subscription as
part of connection setup, so a handler sees that subscription's
created/deleted notifications too, alongside any subscription the
application creates explicitly. Use `subscription-id` to tell them
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

Fires once per lifecycle point of a real client's monitored item —
created, modified, monitoring-mode changed, or deleted.
`notification.type` tells the points apart
(`NotificationType.MONITOREDITEM_CREATED`, `_MODIFIED`,
`_MONITORINGMODE`, `_DELETED`); `notification.lifecycle` is `None`
here. The `session-id`, `subscription-id`, and `monitoreditem-id` keys
are present and consistent across all four points for the same item,
which is what lets an application correlate a specific client's
specific monitored item across its lifetime — the foundation a future,
separately-scoped feature can build on to target an event at one
client's monitored item.

```python
server = o6.Server(port=4840)

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

Fires when a server is added, updated, or removed via the
RegisterServer/RegisterServer2 service, or the equivalent local
open62541 API (`UA_Server_registerServer` / `UA_Server_deregisterServer`).
Exactly one of `server-added`, `server-updated`, `server-removed` is
`True` on a given notification. `notification.lifecycle` is `None`
here.

```python
server = o6.Server(port=4840)

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

Fires when multicast-DNS-discovered server information is added,
updated, or removed — via mDNS or the equivalent local open62541 API
(`UA_Server_registerServerOnNetwork` / `UA_Server_deregisterServerOnNetwork`).
This is a separate category from `onDiscoveryRegisterServerNotification`
with a disjoint payload — a RegisterServer notification never reaches
this handler and vice versa. `notification.lifecycle` is `None` here.

```python
server = o6.Server(port=4840)

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

The server only maintains the ServerOnNetwork record list when
`server.config.serversOnNetworkEnabled` is `True`; leave it off and this
category never fires.

### Audit

Fires for audit-worthy security and management activity: secure-channel
open/close, session create/activate/cancel/close, certificate handling,
and node-management operations (AddNodes, DeleteNodes, AddReferences,
DeleteReferences), plus write/history/method updates. Unlike the other
categories, this one is opt-in — set `server.config.auditingEnabled =
True` before `start()`, or open62541 drops every audit notification
before it reaches this mechanism at all.

`notification.auditEventType` is what tells the many audit sub-events
apart: it's the concrete, standardized `AuditEventType` subtype the
notification corresponds to, as an `o6.NodeId` into the standard
information model — e.g. `o6.NodeId(o6.ns.ns0.objtypes.AuditActivateSessionEventType)`
for a session activation, `o6.NodeId(o6.ns.ns0.objtypes.AuditAddNodesEventType)`
for an AddNodes call. `notification.lifecycle` is `None` here.

```python
server = o6.Server(port=4840)
server.config.auditingEnabled = True

@server.onAuditNotification
def on_audit(notification):
    if notification.auditEventType == o6.NodeId(o6.ns.ns0.objtypes.AuditActivateSessionEventType):
        log.info("session activated: %s", notification.payload["/SessionId"])
```

The payload's keys are event-filter property paths (`"/ActionTimeStamp"`,
`"/Status"`, `"/SessionId"`, ...) rather than the fixed key sets the other
categories use — every audit sub-event has its own field set, inherited
from its position in the `AuditEventType` hierarchy. They're addressable
exactly like any other event's field data in this codebase (see
[Reading the payload](#reading-the-payload)), e.g.
`notification.payload["/Status"]`.

## Reference

- [`o6.Notification`](../../api_reference/notification.md) — `lifecycle` carries the
  human-readable lifecycle point name (`"started"`, `"shutdown"`,
  `"stopping"`, `"stopped"`) for lifecycle notifications; `auditEventType`
  carries the standardized `AuditEventType` NodeId for audit notifications;
  both are `None` outside their own category.
- `Server.onLifecycleNotification` — the lifecycle registry.
- `Server.onSecureChannelNotification` — the secure-channel registry.
- `Server.onSessionNotification` — the session registry.
- `Server.onServiceNotification` — the service registry.
- `Server.onSubscriptionNotification` — the subscription registry.
- `Server.onMonitoredItemNotification` — the monitored-item registry.
- `Server.onDiscoveryRegisterServerNotification` — the discovery
  RegisterServer registry.
- `Server.onDiscoveryServerOnNetworkNotification` — the discovery
  ServerOnNetwork registry.
- `Server.onAuditNotification` — the audit registry.
