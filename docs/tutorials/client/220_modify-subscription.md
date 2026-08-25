# Modify a subscription

You split the distillery into a fast subscription (the kettle values) and a slow subscription (the operator-facing `Status` values). The distillery ran for a while, and now three things on the still have changed that demand a knob *on the subscription itself*, not on a single item:

- **The heater phase got longer.** You added a 0.5 °C pre-heat step at the start of the batch. The fast subscription that was publishing at 100 ms is now generating more notifications than the dashboard can render — slow it down without losing the kettle gauge.
- **The network is unreliable.** The link between the control room and the still drops for a few seconds at a time. The server keeps killing the slow subscription because `lifetimeCount` is too tight — lengthen the lifetime so a momentary blip doesn't tear it down.
- **You're pausing the run for maintenance.** A pump is being replaced and no part of the still should be reporting for the next ten minutes. Set `publishingEnabled=False` on the subscription and the server stops sending anything; flip it back to `True` and it picks up where it left off.

None of those need a new subscription — `subscription.modify(...)` changes the existing one in place. The same `modify(...)` is also available on a `MonitoredItem` for the per-item knobs (sampling interval, queue size, filter, monitoring mode). Both `modify(...)` methods use the same arguments as the corresponding creation methods — pass only the values you want to change, leave the rest as `None`.

This page walks through three steps:

- Modify the subscription's publishing cadence, lifetime, and publishing-enabled flag.
- Modify a monitored item's sampling interval, queue size, or filter.
- Pause, resume, and trigger notifications on items.

!!! info
    This tutorial expects the [example server running](../../tutorials.md#running-the-example-server) in the background, and assumes you know how to [create and connect](100_connect.md) a client, how to [browse](110_browse.md) the address space, how to [monitor data changes](200_monitor-datachange.md), and how to create separate [subscriptions](210_subscriptions.md). The `NodeId`s used below are the ones exposed by the distilling example server's `DistillingSystem` object at `ns=1;i=1000`.

---

## Modify the subscription's publishing cadence

The default subscription's publishing interval is whatever the client picked at first `monitor(...)` time. Change it (along with any of the other subscription parameters) with `subscription.modify(...)`:

```python
sub = client.defaultSubscription
sub.modify(
    publishingInterval=50.0,    # ms — publish faster
    maxKeepaliveCount=10,
)
```

The full list of parameters is the same as for `client.createSubscription(...)`:

- **`publishingInterval`** (ms) — how often the server publishes queued notifications. The distillery's slow subscription is fine at 1 s for `Status.Setpoint`, but you'll want to push this down to 200 ms once a batch is running and you're watching `Status.State` for the `Filling -> Heating -> Distilling -> Idle` transitions.
- **`lifetimeCount`** — how many publishing intervals the server waits without a successful publish before considering the subscription dead. If the control-room link is flaky, raise this from `10` to `60` so a 5-second outage doesn't tear the subscription down.
- **`maxKeepaliveCount`** — how many intervals may pass without a notification before the server sends an empty keep-alive.
- **`maxNotificationsPerPublish`** — cap on notifications bundled into a single `Publish` response.
- **`publishingEnabled`** — `False` puts the subscription into "disabled" state (no publishes at all, no keep-alives). The right setting while the still is in maintenance.

For the distillery, a typical mid-batch modification is to slow the fast subscription down because the heater phase drags on — once you've done it, the slow subscription's `lifetimeCount` no longer needs to be tight, so you bump that too:

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

A `MonitoredItem` also exposes `modify(...)` for changes that affect only that item. The two most common changes are `samplingInterval` and `queueSize`:

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

For the distillery, the typical item-level changes are:

- **During `Distilling` (steady state), `Kettle.Temperature`** doesn't need 100 ms sampling — slow it to 1 s and add a `DataChangeFilter` deadband so the callback only fires when the value moves by more than 0.5 °C from the last notification.
- **During `Filling`, `Kettle.Level`** is the interesting one. Speed its sampling up to 50 ms and remove any deadband — you want every change.

You can also swap in a `DataChangeFilter` (for value-change items) or an `EventFilter` (for event items — see [Listen to events](240_listen-to-events.md)). For data-change items, a `DataChangeFilter` lets you set a deadband for numeric values or a trigger (`StatusValue`, `Status`, `StatusValueTimestamp`):

```python
from o6.ns.ns0.datatypes import DataChangeFilter, DataChangeTrigger, DeadbandType

item.modify(filter=DataChangeFilter(
    trigger=DataChangeTrigger.STATUS_VALUE,
    deadbandValue=0.5,                  # only fire when value moved by 0.5
    deadbandType=DeadbandType.ABSOLUTE,
))
```

The deadband is applied by the *server* — samples that don't cross it are dropped before they reach the client, so the callback simply isn't called. See [Subscription filter](230_subscription-filter.md) for the full filter story.

---

## Pause, resume, and trigger notifications

A monitored item can be paused with `setMonitoringMode(SAMPLING)` — the server continues to sample, but no notifications are sent. Resume with `setMonitoringMode(REPORTING)`:

```python
from o6.ns.ns0.datatypes import MonitoringMode

item.setMonitoringMode(MonitoringMode.SAMPLING)   # paused
item.setMonitoringMode(MonitoringMode.REPORTING)  # resumed
```

The distillery's natural use of this is to silence a value during a phase where it's not interesting. `Kettle.WashStart` is read-only and only meaningful while a batch is in the `Distilling` phase — there's no point getting notifications about it during `Filling`:

```python
wash_start = client.monitor("ns=1;i=1303", callback=lambda v: print(v))

# Filling phase — silence the wash_start notifications
wash_start.setMonitoringMode(MonitoringMode.SAMPLING)
# ... filling ...
# Distilling phase — wash_start is interesting again
wash_start.setMonitoringMode(MonitoringMode.REPORTING)
```

The third mode, `DISABLED`, is harder: the server stops sampling *and* stops pushing. The item is still on the server, but it has no current value — `REPORTING` resumes the sampling too. Use `DISABLED` only when you want to free the server-side resources temporarily.

For more advanced setups, `setTriggering(linksToAdd=[...])` makes one monitored item a *trigger* for others — when the trigger fires, the linked items are also reported. On the distillery this is useful when a single value-change should refresh several dependent variables in the same `Publish` response. For example, when `Status.State` transitions to `Idle`, you also want the dashboard to re-read `Status.Cycle`, `Kettle.Level`, and `Distillate.Level` in the same notification batch — link them all to `Status.State` so a state transition pulls them along:

```python
state = client.monitor("ns=1;i=1201", callback=lambda v: print("state:", v))
cycle = client.monitor("ns=1;i=1202", callback=lambda v: print("cycle:", v))
level = client.monitor("ns=1;i=1301", callback=lambda v: print("level:", v))

state.setTriggering(linksToAdd=[cycle, level])
```

## Putting it all together

The full picture, in one script: subscribe to two items, modify the subscription's publishing cadence, modify one item's sampling and add a deadband filter, pause/resume the other, and finally link them so the trend value-change pulls the integer along in the same publish response.

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

## What's next?

- [Subscriptions](210_subscriptions.md) — go back to the basic subscription setup.
- [Listen to events](240_listen-to-events.md) — `EventFilter` syntax for event items.
