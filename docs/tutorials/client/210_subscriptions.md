# Subscriptions

You have built a simple control loop for the distillery server. The first [monitor](200_monitor-datachange.md) tutorial showed you how to receive value-change notifications on a single shared *subscription*; this page is about creating *additional* subscriptions when the default one isn't the right fit.

A still has two rhythms running at once. The `Kettle.Temperature` ticks up smoothly from `20.0` °C to the `Setpoint` every batch — a few seconds of fine-grained change worth sampling at 100 ms. The operator's `Setpoint` and the `Status.Cycle` counter change maybe once a minute — sampling them at 100 ms is pure waste, and worse, the deadband filter you tuned for the temperature doesn't transfer cleanly to the operator-facing values. Putting both kinds of value on the same subscription forces a single compromise on publishing cadence, sampling interval, and lifetime. Creating a separate subscription for each group lets each run at its own pace.

A *subscription* is the server-side object that owns a set of monitored items and pushes notifications from the server to the client. `o6` keeps a default subscription that is created automatically the first time you call `client.monitor(...)`; you can create additional named subscriptions with `client.createSubscription(...)` when you need separate publishing cadences or lifetimes.

This page walks through subscription primitives:

- Recall what `client.monitor(...)` does without the extra parameters.
- Tune the publishing cadence, lifetime, and keep-alive on a subscription.
- Create an additional named subscription when the default cadence isn't the right fit.

!!! info
    This tutorial expects the [example server running](../../tutorials.md#running-the-example-server) in the background, and assumes you know how to [create and connect](100_connect.md) a client, how to [browse](110_browse.md) the address space, and how to [monitor data changes](200_monitor-datachange.md). The `NodeId`s used below are the ones exposed by the distilling example server's `DistillingSystem` object at `ns=1;i=1000`.

!!! tip
    For the parameters that go on a *single monitored item* (sampling interval, queue size, deadband filter, monitoring mode), see [Subscription filter](230_subscription-filter.md). That page is the place to look when the question is "control what each item pushes".

---

## Recap: monitoring on the default subscription

The first `client.monitor(...)` call creates an implicit *default subscription* on the server. Until you ask for a second one, every monitored item you add is attached to that single subscription and the server publishes notifications for all of them on the same cadence:

```python
item = client.monitor(
    "ns=1;i=1302",   # Kettle.Temperature
    callback=lambda v: print("kettle temperature:", v),
)
```

The default publishing interval is 100 ms — fine for the heating phase, wasteful for the operator's `Setpoint`. The fix is not "tune the item" — tuning the item only changes what the *server* samples, not how often it *publishes*. The fix is "give the slow values their own subscription that publishes less often". That's what the rest of this page is about.

The `monitor()` call returns a `MonitoredItem` handle. The item is removed when the client disconnects, when the subscription is deleted, or when you call `item.delete()` explicitly.

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

Every parameter you would pass to `client.createSubscription(...)` can also be modified on an existing subscription with `subscription.modify(...)`. The shape is the same — pass only the values you want to change:

```python
sub = client.defaultSubscription
sub.modify(
    publishingInterval=50.0,   # ms — publish faster
    lifetimeCount=30,
    maxKeepaliveCount=10,
)
```

The full list of subscription-level parameters:

- **`publishingInterval`** (ms) — how often the server publishes queued notifications. This is the single most important knob: it sets the *cadence* for every item on the subscription.
- **`lifetimeCount`** — how many publishing intervals the server waits without a successful publish before considering the subscription dead.
- **`maxKeepaliveCount`** — how many intervals may pass without a notification before the server sends an empty keep-alive.
- **`maxNotificationsPerPublish`** — cap on notifications bundled into a single `Publish` response.
- **`publishingEnabled`** — `False` puts the subscription into "disabled" state (no publishes, no keep-alives).

For the distillery, tuning the default subscription in place is rarely the right answer — every monitored item on the still benefits from its own cadence. But for a one-shot "watch the temperature for a few seconds" script, modifying the default subscription is the simplest path.

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

This is the main story of the page. The distillery has two rhythms: the fast kettle variables (level, temperature, wash start) and the slow operator-facing variables (setpoint, state, cycle counter). The way to give each its own pace is to give each its own subscription.

Create one with `client.createSubscription(...)`:

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

The fast subscription drives the HMI's kettle gauge. The slow subscription drives the "current batch / setpoint" header. They're independent — slowing one to save bandwidth doesn't throttle the other, and the lifetime / keep-alive of one can be tuned without affecting the other.

All subscriptions are tracked in `client.subscriptions`, keyed by their server-assigned `SubscriptionId`:

```python
sub_a = client.createSubscription(publishingInterval=100.0)
sub_b = client.createSubscription(publishingInterval=1000.0)

print(len(client.subscriptions))        # 3: default + sub_a + sub_b

sub_b.delete()                          # server-side teardown
print(len(client.subscriptions))        # 2
```

Subscriptions are automatically cleaned up when the client disconnects, but can also be manually deleted:

```python
sub_b.delete()                     # server-side teardown
```

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

## What's next?

- [Subscription filter](230_subscription-filter.md) — the per-item knobs (sampling interval, queue size, deadband filter, monitoring mode) for shaping *what* each monitored item pushes.
- [Modify a subscription](220_modify-subscription.md) — change publishing interval, lifetime count, or publishing-enabled flag on the whole subscription without recreating it.
- [Listen to events](240_listen-to-events.md) — `client.monitorEvent(...)` is the same shape, but for events instead of value changes.
