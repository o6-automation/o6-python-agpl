# Subscriptions & historical data

## Subscriptions and monitored items

A subscription is a server-side container with a publishing interval; monitored
items live inside it and report changes. `o6` models both as objects
(`o6.subscription.Subscription`, `o6.subscription.MonitoredItem`) and creates a
default subscription for you, so the simplest useful case is one line.

### Monitoring data changes

```python
def onDataChange(value):
    print(value)

item = client.monitor("ns=1;s=Temperature", onDataChange, samplingInterval=500.0)
```

With no callback, a built-in one prints `MonitoredItem {id}: {value}`, which is
handy at the REPL. The callback may take one or two parameters: with one it
receives the value, with two it receives `(item, value)` — the number of
*required* positional parameters decides. `valueOnly=False` hands the callback
the full `DataValue` instead of the unwrapped value, giving you status and
timestamps:

```python
client.monitor(
    "ns=1;s=Temperature",
    lambda item, dv: print(item.id, dv.value, dv.sourceTimestamp),
    valueOnly=False,
)
```

Callbacks run on the client's event loop thread. Anything slow in there delays
every other notification.

`monitor()` accepts a list of targets and then returns a list of items, and it
accepts a `ReadValueId` when you need to monitor something other than a whole
value — a specific attribute, or an index range:

```python
items = client.monitor(["ns=1;s=IntegerVariable", "ns=1;s=DoubleVariable"], cb)

rvid = ns0.datatypes.ReadValueId()
rvid.nodeId = o6.NodeId("ns=1;s=ArrayVariable")
rvid.attributeId = o6.AttributeId.VALUE
rvid.indexRange = "0:2"
item = client.monitor(rvid, cb)
```

The remaining parameters map straight onto the OPC UA `MonitoringParameters`:
`filter` (a `DataChangeFilter`), `monitoringMode` (`REPORTING`, `SAMPLING`,
`DISABLED`), `queueSize`, `discardOldest`, plus `onCreated` / `onDeleted`
lifecycle callbacks and `subscription` to place the item in a specific
subscription. A deadband filter, for instance, suppresses noise:

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

`monitorEvent()` subscribes to an event notifier node — typically the Server
object, `i=2253`:

```python
def onEvent(fields):
    print(fields)

item = client.monitorEvent("i=2253", onEvent)
```

Without a filter the default selects `EventId`, `EventType`, `SourceName`,
`Time`, `Message`, and `Severity`. A filter can be an `EventFilter` object or a
query string, which is far more convenient:

```python
client.monitorEvent(
    "i=2253",
    onEvent,
    "SELECT /Message, /Severity WHERE /Severity > 100",
)
```

The callback receives a dict of the selected fields (or `(item, fields)` for a
two-parameter callback). `queueSize` defaults to 100 here, because events arrive
in bursts.

### Managing subscriptions explicitly

The default subscription publishes every 100 ms. When you need different timing,
or want to group items so they can be enabled and disabled together, create your
own:

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

`onCreated` fires when the server acknowledges creation — take the id from
`response.subscriptionId`, since the `Subscription` object is only assigned its
id after the callback runs. `onStatusChange` fires when the server publishes a
`StatusChangeNotification`, for example a keepalive timeout or a session
transfer. `onDeleted` fires on explicit deletion and on session close.

Existing subscriptions can be reconfigured and removed:

```python
subscription.modify(publishingInterval=2000.0, publishingEnabled=False)
subscription.delete()      # deletes its monitored items first
```

Read-only properties describe the current, server-revised state: `id`,
`publishingInterval`, `lifetimeCount`, `maxKeepaliveCount`,
`maxNotificationsPerPublish`, `enabled`, `monitoredItems`, and `client`.
`modify()` writes back the values the server revised, so reading them afterwards
tells you what you actually got.

On the client, `client.subscriptions` is a copy of the id → subscription map and
`client.defaultSubscription` is the one `monitor()` uses when you do not pass
`subscription=`. The latter raises `RuntimeError` when the client is not
connected, and a reconnect replaces it with a fresh one.

### Managing monitored items

A `MonitoredItem` can be reconfigured in place:

```python
item.modify(samplingInterval=1000.0, queueSize=5)
item.setMonitoringMode(ns0.datatypes.MonitoringMode.DISABLED)
item.delete()
```

`modify()` also accepts a `filter`; passing a string filter is only valid for
event items, and mixing a `DataChangeFilter` into an event item (or the reverse)
raises `TypeError` before anything is sent.

Triggering links let a rarely-changing item pull others along: when the
triggering item reports, the linked items report too, even if they are only
`SAMPLING`:

```python
trigger.setTriggering(linksToAdd=[item1, item2])
trigger.setTriggering(linksToRemove=[item1])
```

The item's own state is available as `id`, `itemToMonitor`, `params`, `mode`,
`subscription`, and `client`. `itemToMonitor` and `params` return copies, so the
revised sampling interval and queue size can be inspected but not mutated behind
the client's back. An item is falsy once deleted, and operating on a deleted item
raises `RuntimeError`.

The subscription tutorials cover the same ground task by task:
[Monitor datachange](../../tutorials/client/200_monitor-datachange.md),
[Subscriptions](../../tutorials/client/210_subscriptions.md),
[Modify a subscription](../../tutorials/client/220_modify-subscription.md), and
[Filter](../../tutorials/client/230_subscription-filter.md).

## Historical data

Four methods cover historical access. They build the corresponding history
request internally and return unpacked results. All of them require a server
with a history backend — otherwise the service comes back `BAD_NOT_SUPPORTED`
and a `ValueError` is raised.

Reading raw history for a time interval:

```python
import datetime

end = datetime.datetime.now(datetime.timezone.utc)
start = end - datetime.timedelta(hours=1)

history = client.historyRead(
    "ns=1;s=Temperature",
    start,
    end,
    numValuesPerNode=0,     # 0 = as many as the server will give
    returnBounds=False,     # include the values bracketing the interval
    timestampsToReturn=ns0.datatypes.TimestampsToReturn.BOTH,
)
for dv in history.dataValues:
    print(dv.sourceTimestamp, dv.value)
```

A single target returns one `HistoryData`; a list of targets returns a list of
them, in order. A bad per-node status raises — `StatusCodeError` for the single
form, `ValueError` naming the index for the list form.

Writing history takes `DataValue` objects with their `sourceTimestamp` set:

```python
client.historyUpdateInsert("ns=1;s=Temperature", values)   # timestamps must be free
client.historyUpdateReplace("ns=1;s=Temperature", values)  # timestamps must exist
client.historyUpdateDelete("ns=1;s=Temperature", start, end)
```

Insert fails for a timestamp that already holds a value, replace fails for one
that does not, and delete removes everything in the interval. All three return
the raw per-node `HistoryUpdateResult`, so inspect its `statusCode` and
`operationResults`.
