# Application Notifications

Observe the client's runtime lifecycle and service calls from Python.
These hooks are useful for logging and diagnostics.

| What you want to observe | API |
| --- | --- |
| Client runtime activity and service calls | `client.on<category>Notification` on this page |
| Changes to a remote Variable's value | [`client.monitor`](subscriptions.md#monitoring-data-changes) |
| OPC UA events from the server | [`client.monitorEvent`](subscriptions.md) |

## Logging client activity

Register a handler before connecting to observe startup. This complete example
logs client startup, reads the server's current time, and disconnects.
It requires a running server at the shown URL:

```python
import logging
import o6

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("client.activity")
client = o6.Client("opc.tcp://localhost:4840")

@client.onLifecycleNotification
def on_lifecycle(notification):
    log.info("client %s", notification.lifecycle)

with client:
    print(client.read("i=2258"))
```

`notification.lifecycle` names a runtime transition (`"started"` or
`"stopped"`) and is `None` for other notifications. These are the underlying
client runtime's startup and cleanup notifications: ordinary `disconnect()`
does not emit a matching `"stopped"` notification. Use `client.connected` to
inspect the current connection and see
[Connection recovery](lifecycle.md#connection-recovery) for handling lost
connections.

## Choosing a registry and reading the payload

| Registry | Receives |
| --- | --- |
| `client.onGlobalNotification` | Every application notification the client produces. |
| `client.onLifecycleNotification` | Client runtime lifecycle. |
| `client.onServiceNotification` | Service call processing. |

A handler on a scoped registry and one on `onGlobalNotification` both receive
the matching notification. Each receives an
[`o6.Notification`](../../api_reference/notification.md): `type` identifies the
notification, and `payload` is a read-only mapping of its fields, empty for
lifecycle notifications. `auditEventType` is always `None` on the client.
The server uses the same object and registry interface, with
[additional categories and payloads](../server/notification-handler.md#choosing-a-category).

For example, add this handler before the opening program's `with client:`
block to log outgoing service calls:

```python
@client.onServiceNotification
def on_service(notification):
    if notification.type == o6.client.NotificationType.SERVICE_BEGIN:
        log.info("request %s", notification.payload["request-id"])
```

## Adding, removing, and clearing handlers

Decorators append handlers in registration order. A registry can hold several
handlers. These alternative fragments use the opening example's `client` and
`on_lifecycle`:

```python
client.onLifecycleNotification(on_lifecycle)     # append without a decorator
client.onLifecycleNotification = [on_lifecycle] # replace the whole list
list(client.onLifecycleNotification)            # inspect registered handlers
client.onLifecycleNotification.remove(on_lifecycle)
client.onLifecycleNotification.clear()          # remove all handlers
```

Assignment also accepts a single callable or `None` to clear the registry.
`remove()` raises `ValueError` if the handler is absent. An empty registry
has no Python handler dispatch.

## Synchronous and asynchronous handlers

Handlers run on the client's event loop. Keep them short: blocking work delays
connection processing and other callbacks. A handler can be a plain function
or `async def`; returned awaitables are scheduled on that loop without waiting
for them to finish. Async handlers can overlap, so registration order does not
guarantee completion order.

To issue client requests from a handler, use `async def` and await them.
Reads and browsing need the client's loop to process a remote response, so
a synchronous handler cannot block that loop waiting for the result.
Ordinary metadata properties such as `client.connected` need no await.
Avoid issuing a service request from a service-notification handler: that
request would itself produce service notifications.

## Errors don't crash the client

Exceptions in application-notification handlers are logged. Later handlers
still run, and the triggering operation continues. This applies to synchronous
handlers and scheduled awaitables.

## Related topics

| Topic | What it covers |
|---|---|
| [`o6.Notification`](../../api_reference/notification.md) | Notification fields passed to handlers. |
| [`o6.NotificationType`](../../api_reference/notificationtype.md) | Notification categories; clients receive the `LIFECYCLE_*` and `SERVICE_*` members. |
