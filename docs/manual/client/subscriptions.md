# Subscriptions & Events

Monitor data changes and events through subscriptions on a connected client.

## Subscriptions and monitored items

A subscription is a server-side container with a publishing interval.
Monitored items live inside it and report changes. `o6` models both as objects
(`o6.subscription.Subscription`, `o6.subscription.MonitoredItem`). `connect()`
creates a default subscription, so monitoring a node takes one line. To skip
it, pass `createDefaultSubscription=False` to `connect()` and pass an
explicitly created subscription to the monitoring methods.

### Monitoring data changes

A complete synchronous monitoring client can watch the standard Server clock
(`i=2258`, ServerStatus.CurrentTime). Run it with a server listening on port
4840; press Ctrl+C to stop:

```python
import time
from o6 import Client

def onDataChange(value):
    print(value)

try:
    with Client("opc.tcp://localhost:4840") as client:
        client.monitor("i=2258", onDataChange, samplingInterval=500.0)
        while True:
            time.sleep(1)
except KeyboardInterrupt:
    pass
```

The main thread waits while the client's worker delivers notifications. Leaving
`with` disconnects and deletes the subscription and its items, including on
Ctrl+C. In an async application, wait with `await asyncio.Event().wait()`
inside `async with client`; `time.sleep()` would block its event loop.
Recovery after a lost Session is covered under
[Subscription recovery](#subscription-recovery).

The remaining fragments assume a connected `client` and the named application
nodes on its server. For example, monitor a Temperature Variable:

```python
def onDataChange(value):
    print(value)

item = client.monitor("ns=1;s=Temperature", onDataChange, samplingInterval=500.0)
```

Without a callback, a built-in one prints `MonitoredItem {id}: {value}`. The
callback takes one or two parameters: with one it receives the value, with two
it receives `(item, value)`. The number of required positional parameters
decides. `valueOnly=False` passes the full `DataValue`, with status and
timestamps, instead of the unwrapped value:

```python
client.monitor(
    "ns=1;s=Temperature",
    lambda item, dv: print(item.id, dv.value, dv.sourceTimestamp),
    valueOnly=False,
)
```

Callbacks run on the client's event loop thread. Data-change, event and
lifecycle callbacks can be async or return an awaitable. The client schedules
the awaitable on that loop and logs exceptions. Async callbacks can overlap,
and creation and deletion operations do not wait for them to finish. Blocking
work delays every other notification.

Delivery order is not completion order: an async handler processing an older
value can finish after one processing a newer value. There is no global
ordering across monitored items. If processing must remain sequential, use a
short synchronous handler to put notifications into a bounded `asyncio.Queue`
and one application task to consume them. Choose what to do when that queue
is full (for example, keep only the latest value for a display). The server's
`queueSize` does not bound pending Python callback tasks. When shutting down,
stop monitoring, then drain or cancel and await the application's consumer;
item deletion itself does not wait for already scheduled async callbacks.

Pass a list of targets to get a list of items. Pass a `ReadValueId` to monitor
a specific attribute or an index range instead of the whole value:

```python
items = client.monitor(["ns=1;s=IntegerVariable", "ns=1;s=DoubleVariable"], cb)

rvid = ns0.datatypes.ReadValueId()
rvid.nodeId = o6.NodeId("ns=1;s=ArrayVariable")
rvid.attributeId = o6.AttributeId.VALUE
rvid.indexRange = "0:2"
item = client.monitor(rvid, cb)
```

The remaining parameters map onto the OPC UA `MonitoringParameters`:
`filter` (a `DataChangeFilter`), `monitoringMode` (`REPORTING`, `SAMPLING`,
`DISABLED`), `queueSize` and `discardOldest`. `onCreated` and `onDeleted` are
lifecycle callbacks. `subscription` places the item in a specific
subscription. For `monitor()` and `monitorEvent()`, that subscription must
belong to the receiving client; a foreign subscription raises `ValueError`.
A deadband filter suppresses noise:

```python
item = client.monitor(
    "ns=1;s=Temperature",
    cb,
    queueSize=10,
    filter=ns0.datatypes.DataChangeFilter(
        trigger=ns0.datatypes.DataChangeTrigger.STATUS_VALUE,
        deadbandType=ns0.datatypes.DeadbandType.ABSOLUTE,
        deadbandValue=1.0,
    ),
)
```

### Monitoring events

`monitorEvent()` subscribes to an event notifier node, typically the Server
object `i=2253`:

```python
def onEvent(fields):
    print(fields)

item = client.monitorEvent("i=2253", onEvent)
```

Without a filter, the default selects `EventId`, `EventType`, `SourceName`,
`Time`, `Message` and `Severity`. A filter is an `EventFilter` object or a
query string:

```python
client.monitorEvent(
    "i=2253",
    onEvent,
    "SELECT /Message, /Severity WHERE /Severity > 100",
)
```

The callback receives a `dict[str, Any]` keyed by the selected event-filter
paths, such as `"/Message"` or `"/ConditionName/Id"`. A two-parameter callback
receives `(item, fields)`. `queueSize` defaults to 100 for events, because
events arrive in bursts.

### Managing subscriptions explicitly

The default subscription publishes every 100 ms. Create your own for
different timing, or to group items so you can enable and disable them
together:

```python
subscription = client.createSubscription(
    publishingInterval=1000.0,
    lifetimeCount=36000,
    maxKeepaliveCount=10,
    maxNotificationsPerPublish=10,
    publishingEnabled=True,
)

item = client.monitor("ns=1;s=Temperature", cb, subscription=subscription)
```

Three lifecycle callbacks are available:

```python
subscription = client.createSubscription(
    publishingInterval=500.0,
    onCreated=lambda sub, response: print("created", response.subscriptionId),
    onStatusChange=lambda sub, notification: print("status", notification),
    onDeleted=lambda sub: print("deleted"),
)
```

- `onCreated` fires when the server acknowledges creation. Take the id from
  `response.subscriptionId`; the `Subscription` object gets its id only after
  the callback runs.
- `onStatusChange` fires when the server publishes a
  `StatusChangeNotification`, for example on a keepalive timeout or a session
  transfer.
- `onDeleted` fires on explicit deletion and on session close.

Reconfigure or remove a subscription:

```python
subscription.modify(publishingInterval=2000.0, publishingEnabled=False)
subscription.delete()      # deletes its monitored items first
```

Read-only properties hold the current, server-revised state: `id`,
`publishingInterval`, `lifetimeCount`, `maxKeepaliveCount`,
`maxNotificationsPerPublish`, `enabled`, `monitoredItems` and `client`.
`modify()` stores the values the server revised.

`client.subscriptions` is a copy of the id → subscription map.
`client.defaultSubscription` is the subscription `monitor()` uses without
`subscription=`. It raises `RuntimeError` when the client is not connected or
has no default subscription. A normal disconnect/connect replaces it;
automatic recovery can instead preserve it or leave it absent.

### Subscription recovery

Subscriptions and their items survive a channel interruption only while the
server retains them and the same Session can be reactivated. A subscription
can expire even when the Session survives. Do not recreate monitoring just
because a channel reconnects: that can create duplicate monitored items.

Keep the returned `Subscription` and `MonitoredItem` objects. When the client
learns that they were deleted, their `id` becomes `None` and they are falsy.
`onDeleted` can signal an application recovery task; it does not mean the
connection is ready for new requests. After reconnection, check the objects
as well as `client.connected`.

If a subscription was lost, wait for an activated Session, refresh namespaces
if the server may have changed, then create a subscription and all its items
again. The following synchronous fragment assumes `onDataChange` from above
and an already recovered connection:

```python
client.updateRemoteNamespaces()
subscription = client.createSubscription(publishingInterval=500.0)
item = client.monitor("i=2258", onDataChange, subscription=subscription)
```

Keep the monitoring configuration in application code so it can be applied
again. The SDK does not replay it after Session loss, and automatic Session
replacement does not create a new default subscription. Use the explicit
`subscription=` above, or perform a normal disconnect/connect and set up
monitoring again. A deleted item in a surviving subscription only needs that
item recreated. See [Connection recovery](lifecycle.md#connection-recovery)
for pending operations and node handles.

### Managing monitored items

A `MonitoredItem` can be reconfigured in place:

```python
item.modify(samplingInterval=1000.0, queueSize=5)
item.setMonitoringMode(ns0.datatypes.MonitoringMode.DISABLED)
item.delete()
```

`modify()` also accepts a `filter`. A string filter is valid only for event
items. A `DataChangeFilter` on an event item, or the reverse, raises
`TypeError` before anything is sent.

Omitted arguments (or `None`) keep the last accepted settings, including the
filter and discard policy. `filter=None` does not clear the filter. Successful
changes update `params` with the server's revised values. Rejected
modifications or mode changes leave `params` and `mode` unchanged, so you can
retry with the same handle.

With triggering links, when the triggering item reports, the linked items
report too, even if they are only `SAMPLING`:

```python
trigger.setTriggering(linksToAdd=[item1, item2])
trigger.setTriggering(linksToRemove=[item1])
```

Every linked item must be live and belong to the same subscription as the
triggering item. Foreign or server-local items raise `ValueError`.
Uninitialized or deleted items raise `RuntimeError`. Both errors occur before
any links change.

An item's state is in `id`, `itemToMonitor`, `params`, `requestedParams`,
`mode`, `subscription` and `client`. `requestedParams` holds the parameters
submitted at creation, before server revisions or later modifications.
`itemToMonitor`, `params` and `requestedParams` return independent snapshots:
you can inspect them, but changing them does not change the item. A deleted
item is falsy, and operations on it raise `RuntimeError`.

Tutorials:
[Monitor datachange](../../tutorials/client/200_monitor-datachange.md),
[Subscriptions](../../tutorials/client/210_subscriptions.md),
[Modify a subscription](../../tutorials/client/220_modify-subscription.md), and
[Filter](../../tutorials/client/230_subscription-filter.md).
