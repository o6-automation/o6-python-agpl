# Subscriptions

A *subscription* is the server-side object that owns a set of monitored items and pushes their notifications to the client. `o6` creates a default subscription the first time you call `client.monitor(...)`. Create additional named subscriptions with `client.createSubscription(...)` when groups of items need separate publishing cadences or lifetimes.

The distillery has two rhythms. `Kettle.Temperature` rises from `20.0` °C to the `Setpoint` in a few seconds each batch and is worth sampling at 100 ms. The operator's `Setpoint` and the `Status.Cycle` counter change about once a minute, so sampling them at 100 ms wastes bandwidth. The deadband you tuned for the temperature also doesn't suit them. One subscription forces a single publishing cadence, sampling interval and lifetime on both groups. A separate subscription per group lets each run at its own pace.

This page covers:

- What `client.monitor(...)` does without the extra parameters.
- Tune the publishing cadence, lifetime, and keep-alive on a subscription.
- Create an additional named subscription when the default cadence doesn't fit.

!!! info
    This tutorial needs the [example server running](../setup.md) in the background. It assumes you know how to [create and connect](100_connect.md) a client, [browse](110_browse.md) the address space, and [monitor data changes](200_monitor-datachange.md). The NodeIds below belong to the example server's `DistillingSystem` object at `ns=1;i=1000`.

!!! tip
    For the parameters of a single monitored item (sampling interval, queue size, deadband filter, monitoring mode), see [Subscription filter](230_subscription-filter.md).

---

## Recap: monitoring on the default subscription

The first `client.monitor(...)` call creates an implicit *default subscription* on the server. Until you create another one, every monitored item is attached to it, and the server publishes notifications for all of them on the same cadence:

```python
item = client.monitor(
    "ns=1;i=1302",   # Kettle.Temperature
    callback=lambda v: print("kettle temperature:", v),
)
```

The default publishing interval is 100 ms. That suits the heating phase but wastes bandwidth on the operator's `Setpoint`. Tuning the item doesn't help: item settings change what the server samples, not how often it publishes. Give the slow values their own subscription that publishes less often.

`monitor()` returns a `MonitoredItem` handle. The item is removed when the client disconnects, when the subscription is deleted, or when you call `item.delete()`.

#### Putting it all together

```python
import time
from o6 import Client

with Client("opc.tcp://localhost:4840") as client:
    item = client.monitor(
        "ns=1;i=1302",   # Kettle.Temperature
        callback=lambda v: print("kettle temperature:", v),
    )

    # let the monitor print a couple of values
    time.sleep(5)
```

---

## Tune the subscription

`subscription.modify(...)` accepts the same parameters as `client.createSubscription(...)`. Pass only the values you want to change:

```python
sub = client.defaultSubscription
sub.modify(
    publishingInterval=50.0,   # ms — publish faster
    lifetimeCount=30,
    maxKeepaliveCount=10,
)
```

Subscription parameters:

- **`publishingInterval`** (ms) — how often the server publishes queued notifications. It sets the cadence for every item on the subscription.
- **`lifetimeCount`** — how many publishing intervals the server waits without a successful publish before considering the subscription dead.
- **`maxKeepaliveCount`** — how many intervals may pass without a notification before the server sends an empty keep-alive.
- **`maxNotificationsPerPublish`** — cap on notifications bundled into a single `Publish` response.
- **`publishingEnabled`** — `False` puts the subscription into "disabled" state (no publishes, no keep-alives).

Modifying the default subscription changes the cadence of every item on it. Use it for a short script such as "watch the temperature for a few seconds". For groups of items with different needs, create separate subscriptions.

#### Putting it all together

```python
import time
from o6 import Client

with Client("opc.tcp://localhost:4840") as client:
    # Faster cadence on the default subscription
    client.defaultSubscription.modify(
        publishingInterval=50.0,
        maxKeepaliveCount=10,
        lifetimeCount=30,
    )

    client.monitor(
        "ns=1;i=1302",   # Kettle.Temperature
        callback=lambda v: print("kettle temperature:", v),
    )

    time.sleep(5)
```

---

## Create a separate subscription

Create a subscription with `client.createSubscription(...)` and pass it to `client.monitor(...)` with `subscription=`:

```python
slow_sub = client.createSubscription(
    publishingInterval=1000.0,         # ms — slow, periodic updates
    lifetimeCount=10,
    maxKeepaliveCount=2,
    maxNotificationsPerPublish=100,
)

item = client.monitor(
    "ns=1;i=1204",   # Status.Setpoint
    callback=lambda v: print("setpoint changed:", v),
    subscription=slow_sub,
)
```

A common split for the distillery is:

- **Default subscription (100 ms):** `Kettle.Level`, `Kettle.Temperature`, `Kettle.WashStart` — the fast-moving values during a batch.
- **Slow subscription (1 s):** `Status.Setpoint`, `Status.State`, `Status.Cycle` — the operator-facing values that change at most a few times per minute.

The fast subscription drives the HMI's kettle gauge and the slow one the "current batch / setpoint" header. They are independent: slowing one doesn't throttle the other, and you can tune the lifetime and keep-alive of each separately.

All subscriptions are tracked in `client.subscriptions`, keyed by their server-assigned `SubscriptionId`:

```python
sub_a = client.createSubscription(publishingInterval=100.0)
sub_b = client.createSubscription(publishingInterval=1000.0)

print(len(client.subscriptions))        # 3: default + sub_a + sub_b

sub_b.delete()                          # server-side teardown
print(len(client.subscriptions))        # 2
```

Subscriptions are deleted automatically when the client disconnects. `delete()` removes one earlier.

#### Putting it all together

```python
import time
from o6 import Client

with Client("opc.tcp://localhost:4840") as client:
    # A slow subscription for the operator-facing values
    slow_sub = client.createSubscription(
        publishingInterval=1000.0,
        lifetimeCount=10,
        maxKeepaliveCount=2,
    )

    client.monitor(
        "ns=1;i=1204",   # Status.Setpoint
        callback=lambda v: print("setpoint changed:", v),
        subscription=slow_sub,
    )

    # The fast-moving kettle values stay on the default subscription,
    # which still publishes every 100 ms.
    client.monitor(
        "ns=1;i=1302",   # Kettle.Temperature
        callback=lambda v: print("kettle temperature:", v),
    )

    time.sleep(5)

    slow_sub.delete()
```

---

## Next steps

| Topic | What it covers |
|---|---|
| [Subscription filter](230_subscription-filter.md) | The per-item knobs (sampling interval, queue size, deadband filter, monitoring mode) for shaping what each monitored item pushes. |
| [Modify a subscription](220_modify-subscription.md) | Change publishing interval, lifetime count, or publishing-enabled flag on the whole subscription without recreating it. |
| [Listen to events](240_listen-to-events.md) | `client.monitorEvent(...)` is the same shape, but for events instead of value changes. |
