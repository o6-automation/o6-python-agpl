# Modify a subscription

`subscription.modify(...)` changes an existing subscription in place, and `MonitoredItem.modify(...)` does the same for one item's sampling interval, queue size, filter or monitoring mode. Both take the same arguments as the matching creation method. Pass only the values you want to change and leave the rest as `None`.

[Subscriptions](210_subscriptions.md) split the distillery into a fast subscription (the kettle values) and a slow one (the operator-facing `Status` values). Three situations call for changing a subscription rather than a single item:

- **The heating phase got longer.** You added a 0.5 °C pre-heat step at the start of the batch. At 100 ms the fast subscription now produces more notifications than the dashboard can render. Slow it down without losing the kettle gauge.
- **The network is unreliable.** The link between the control room and the still drops for a few seconds at a time. The server deletes the slow subscription because `lifetimeCount` is too low. Raise the lifetime so a short outage doesn't delete it.
- **You pause the run for maintenance.** No part of the still should report for the next ten minutes while a pump is replaced. With `publishingEnabled=False` the server stops sending anything. Set it back to `True` and publishing resumes where it left off.

This page covers:

- Modify the subscription's publishing cadence, lifetime, and publishing-enabled flag.
- Modify a monitored item's sampling interval, queue size, or filter.
- Pause, resume, and trigger notifications on items.

!!! info
    This tutorial needs the [example server running](../setup.md) in the background. It assumes you know how to [create and connect](100_connect.md) a client, [browse](110_browse.md) the address space, [monitor data changes](200_monitor-datachange.md), and create separate [subscriptions](210_subscriptions.md). The NodeIds below belong to the example server's `DistillingSystem` object at `ns=1;i=1000`.

---

## Modify the subscription's publishing cadence

The default subscription gets its publishing interval when the first `monitor(...)` call creates it. Change it, or any other subscription parameter, with `subscription.modify(...)`:

```python
sub = client.defaultSubscription
sub.modify(
    publishingInterval=50.0,    # ms — publish faster
    maxKeepaliveCount=10,
)
```

The parameters are the same as for `client.createSubscription(...)`:

- **`publishingInterval`** (ms) — how often the server publishes queued notifications. 1 s suits `Status.Setpoint` on the slow subscription. Lower it to 200 ms while a batch runs and you watch `Status.State` for the `Filling -> Heating -> Distilling -> Idle` transitions.
- **`lifetimeCount`** — how many publishing intervals the server waits without a successful publish before considering the subscription dead. On a flaky control-room link, raise it from `10` to `60` so a 5-second outage doesn't delete the subscription.
- **`maxKeepaliveCount`** — how many intervals may pass without a notification before the server sends an empty keep-alive.
- **`maxNotificationsPerPublish`** — cap on notifications bundled into a single `Publish` response.
- **`publishingEnabled`** — `False` puts the subscription into "disabled" state (no publishes, no keep-alives). Use it while the still is in maintenance.

A typical mid-batch change slows the fast subscription during a long heating phase and loosens the slow subscription's `lifetimeCount`:

```python
# Slow down the fast subscription during the long heating phase
client.defaultSubscription.modify(
    publishingInterval=500.0,    # was 100 ms
)

# Loosen the slow subscription's lifetime so a 2s blip doesn't kill it
slow_sub.modify(
    lifetimeCount=60,
    maxKeepaliveCount=10,
)
```

---

## Modify a monitored item's sampling interval or filter

`MonitoredItem.modify(...)` changes only that item. The most common changes are `samplingInterval` and `queueSize`:

```python
item = client.monitor(
    "ns=1;i=1302",   # Kettle.Temperature
    callback=lambda v: print("kettle temperature:", v),
)

item.modify(
    samplingInterval=1000.0,
    queueSize=50,
)
```

Typical item-level changes on the distillery:

- **During `Distilling` (steady state), `Kettle.Temperature`** doesn't need 100 ms sampling. Slow it to 1 s and add a `DataChangeFilter` deadband so the callback fires only when the value moves more than 0.5 °C from the last notification.
- **During `Filling`, `Kettle.Level`** matters most. Sample it at 50 ms with no deadband to get every change.

`modify(filter=...)` replaces the item's filter: a `DataChangeFilter` for data-change items or an `EventFilter` for event items (see [Listen to events](240_listen-to-events.md)). A `DataChangeFilter` sets a deadband for numeric values and a trigger (`StatusValue`, `Status`, `StatusValueTimestamp`):

```python
from o6.ns.ns0.datatypes import DataChangeFilter, DataChangeTrigger, DeadbandType

item.modify(filter=DataChangeFilter(
    trigger=DataChangeTrigger.STATUS_VALUE,
    deadbandValue=0.5,                  # only fire when value moved by 0.5
    deadbandType=DeadbandType.ABSOLUTE,
))
```

The server applies the deadband. Samples that don't cross it are dropped before they reach the client, and the callback is not called. See [Subscription filter](230_subscription-filter.md) for details.

---

## Pause, resume, and trigger notifications

`setMonitoringMode(SAMPLING)` pauses a monitored item: the server keeps sampling but sends no notifications. `setMonitoringMode(REPORTING)` resumes it:

```python
from o6.ns.ns0.datatypes import MonitoringMode

item.setMonitoringMode(MonitoringMode.SAMPLING)   # paused
item.setMonitoringMode(MonitoringMode.REPORTING)  # resumed
```

Use it to silence a value during a phase where it doesn't matter. `Kettle.WashStart` is read-only and only meaningful in the `Distilling` phase, so silence it during `Filling`:

```python
wash_start = client.monitor("ns=1;i=1303", callback=lambda v: print(v))

# Filling phase — silence the wash_start notifications
wash_start.setMonitoringMode(MonitoringMode.SAMPLING)
# ... filling ...
# Distilling phase — wash_start is interesting again
wash_start.setMonitoringMode(MonitoringMode.REPORTING)
```

In the third mode, `DISABLED`, the server stops sampling and stops pushing. The item stays on the server but has no current value. `REPORTING` resumes sampling too. Use `DISABLED` only to free server-side resources temporarily.

`setTriggering(linksToAdd=[...])` makes one monitored item a *trigger* for others. When the trigger fires, the linked items are reported too, in the same `Publish` response. For example, when `Status.State` changes to `Idle`, the dashboard also needs `Status.Cycle` and `Kettle.Level` in the same notification batch. Link them to `Status.State`:

```python
state = client.monitor("ns=1;i=1201", callback=lambda v: print("state:", v))
cycle = client.monitor("ns=1;i=1202", callback=lambda v: print("cycle:", v))
level = client.monitor("ns=1;i=1301", callback=lambda v: print("level:", v))

state.setTriggering(linksToAdd=[cycle, level])
```

## Putting it all together

One script that monitors two items, changes the subscription's publishing cadence, slows one item's sampling and adds a deadband, pauses and resumes the other, and links them with triggering.

```python
import time
from o6 import Client
from o6.ns.ns0.datatypes import (
    DataChangeFilter, DataChangeTrigger, DeadbandType, MonitoringMode,
)

with Client("opc.tcp://localhost:4840") as client:
    # Two items to play with
    trend   = client.monitor(
        "ns=1;i=1302",   # Kettle.Temperature
        callback=lambda v: print("trend:  ", v),
    )
    integer = client.monitor(
        "ns=1;i=1303",   # Kettle.WashStart
        callback=lambda v: print("integer:", v),
    )

    # 1. Modify the subscription's publishing cadence
    client.defaultSubscription.modify(
        publishingInterval=50.0,
        maxKeepaliveCount=10,
        lifetimeCount=30,
    )

    # 2. Modify a monitored item: slow its sampling, then add a deadband filter
    trend.modify(samplingInterval=1000.0, queueSize=50)
    trend.modify(filter=DataChangeFilter(
        trigger=DataChangeTrigger.STATUS_VALUE,
        deadbandValue=0.5,
        deadbandType=DeadbandType.ABSOLUTE,
    ))

    # 3. Pause the other item, let it sit, then resume it
    integer.setMonitoringMode(MonitoringMode.SAMPLING)
    time.sleep(2)
    integer.setMonitoringMode(MonitoringMode.REPORTING)

    # 4. Link them: when `trend` fires, `integer` is reported in the same response
    trend.setTriggering(linksToAdd=[integer])

    time.sleep(3)
```

---

## Next steps

| Topic | What it covers |
|---|---|
| [Subscriptions](210_subscriptions.md) | Go back to the basic subscription setup. |
| [Listen to events](240_listen-to-events.md) | `EventFilter` syntax for event items. |
