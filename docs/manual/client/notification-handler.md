# Notification handler

open62541 exposes client-side *application notifications* — the same
runtime-notification mechanism the [server side](../server/notification-handler.md)
uses, fired from the client's own connection instead: when it starts and
stops, and around every service call it makes.

`o6` exposes each notification scope as a handler registry on the client:
`client.onGlobalNotification` sees every notification the connection
produces, while `client.onLifecycleNotification` and
`client.onServiceNotification` narrow that down to their own scope. All
three behave exactly like the server's `on<category>Notification`
registries, so a handler written for one side works unchanged on the
other.

## Adding, removing, and clearing handlers

A registry is callable as a decorator, iterable as a list, and assignable
from a callable, a sequence, or `None`. Register any time before
`connect()`; leaving a registry empty (the default) means notifications are
simply not observed, at no runtime cost.

```python
import o6

client = o6.Client("opc.tcp://localhost:4840")

@client.onGlobalNotification
def on_notification(notification):
    print(notification.type, notification.payload)

client.connect()
```

Multiple handlers per registry are supported and fire in registration
order. Assignment replaces the whole list; `clear()` and `remove()` take
handlers back off:

```python
client.onGlobalNotification = on_notification          # replace with just this one
client.onGlobalNotification = [on_notification, audit] # or a whole list
list(client.onGlobalNotification)                      # read them back

client.onGlobalNotification.remove(audit)              # drop one
client.onGlobalNotification.clear()                    # drop all
client.onGlobalNotification = None                     # same as clear()
```

### Reading the payload

Every notification a handler receives is an
[`o6.Notification`](../../api_reference/notification.md) — the same value type the
server side delivers. Besides `type`, it carries `payload` — a read-only
`str -> Any` mapping of that notification's fields, empty for lifecycle
notifications. Values are already converted to the matching Python/`o6`
type, exactly as on the server side. (`auditEventType` is always `None`
here; a client never raises audit notifications.)

```python
@client.onGlobalNotification
def on_notification(notification):
    if notification.type == o6.client.NotificationType.SERVICE_BEGIN:
        print("request-id:", notification.payload["request-id"])
```

For lifecycle notifications, `notification.lifecycle` names the point
that occurred (`"started"` or `"stopped"`) instead — see [Client
lifecycle](../client/lifecycle.md#connecting-and-disconnecting) for what
triggers each one. It's `None` for any other notification.

```python
@client.onGlobalNotification
def on_notification(notification):
    if notification.lifecycle is not None:
        print("lifecycle:", notification.lifecycle)

client.connect()   # prints "lifecycle: started"
```

## Lifecycle and service notifications

`client.onLifecycleNotification` and `client.onServiceNotification` see
only their own scope — the client's own connection start/stop, or its own
service call begin/end — independently of `onGlobalNotification` and of
each other.

```python
@client.onLifecycleNotification
def on_lifecycle(notification):
    print("lifecycle:", notification.lifecycle)

@client.onServiceNotification
def on_service(notification):
    if notification.type == o6.client.NotificationType.SERVICE_BEGIN:
        print("request-id:", notification.payload["request-id"])

client.connect()        # prints "lifecycle: started"
client.browse("i=84")   # prints "request-id: ..."
```

Registering on a scoped registry and on `onGlobalNotification` at the same
time invokes both, independently, for the same event:

```python
client.onLifecycleNotification = on_lifecycle
client.onGlobalNotification = lambda n: print("global:", n.type)
client.connect()   # invokes both on_lifecycle and the global handler
```

## Synchronous and asynchronous handlers

A handler may be a plain function or `async def`. Async results are
scheduled on the client's event loop so the underlying connection never
blocks on a coroutine — returning a coroutine object is enough, no
`await` is performed for you:

```python
import asyncio

@client.onGlobalNotification
async def on_notification(notification):
    await asyncio.sleep(0)
    log.info("notification: %s", notification.type)
```

Calling back into the client needs an `async def` handler. On the client's
own loop `client.read(...)`, `client.browse(...)`, and every other
`MaybeAwaitable` method return an awaitable; a plain `def` handler never
awaits it, so the call does nothing beyond a `RuntimeWarning: coroutine
was never awaited`.

## Errors don't crash the client

An exception raised inside a handler — synchronous or from within an
async handler's coroutine — is caught, logged, and swallowed. The
handlers queued behind it still run, and the client and the operation
that produced the notification continue normally.

## Reference

- [`o6.Notification`](../../api_reference/notification.md) — `lifecycle` carries the
  human-readable lifecycle point name (`"started"`, `"stopped"`) for
  lifecycle notifications; `None` outside that category.
- [`o6.NotificationType`](../../api_reference/notificationtype.md) — the
  notification type encoding. A client only ever sees the `LIFECYCLE_*`
  and `SERVICE_*` members.
- `Client.onGlobalNotification` — the global registry.
- `Client.onLifecycleNotification` — the client's own lifecycle registry.
- `Client.onServiceNotification` — the client's own service-call registry.
