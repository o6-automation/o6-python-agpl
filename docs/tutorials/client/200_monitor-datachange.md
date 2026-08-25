# Monitor datachange

Picking up from [Call a method](130_call-method.md): you started a batch with `Start` and set a new `Setpoint`. Now you want to *see* the batch progress. Polling the kettle values in a tight loop would work, but every poll is a round-trip and most return the same value. `client.monitor` registers a single subscription and lets the server push every change straight to a callback — the natural way to drive a dashboard off the distilling control loop.

A *data-change* monitor item from the server is pushed to you on every value change. `client.monitor(nodeid, callback=...)` registers one on the client's default subscription and hands the callback the new value every time the server sees a change. This is the foundation for any "react to value X moving" workflow — alarming, charting, control loops.

This page walks through the monitor service primitives:

- Register a single data-change monitor with a callback.
- Monitor several variables in one round-trip.
- Use the lifecycle callbacks (`onCreated` / `onDeleted`) and a `DataChangeFilter` to control when you get notified.

!!! info
    This tutorial expects the [example server running](../setup.md) in the background, and assumes you know how to [create and connect](100_connect.md) a client and how to [browse](110_browse.md) the address space. The `NodeId`s used below are the ones exposed by the distilling example server's `DistillingSystem` object at `ns=1;i=1000`.

---

## Register a single data-change monitor

The simplest `client.monitor` call takes one `NodeId` and a callback. The callback is called once per value-change notification from the server — instead of asking the server "what's the temperature now?" every 100 ms, you say "tell me when the temperature changes". Let's watch the `Kettle.Temperature` (`ns=1;i=1302`) — it climbs from `20.0` to `85.0` °C during the heating phase of every batch:

```python

item = client.monitor(
    "ns=1;i=1302",
    callback=lambda v: print("kettle temperature:", v),
)
```

The default sampling interval is 100 ms. The callback is called with the new value directly; if you also want the timestamp and status code, pass `value_only=False` and the callback receives a `DataValue` instead.

The `monitor()` call returns a `MonitoredItem` handle. The item is removed when the client disconnects, when the subscription is deleted, or when you call `item.delete()` explicitly.

#### Putting it all together

```python
import time
from o6 import Client

with Client("opc.tcp://localhost:4840") as client:
    item = client.monitor(
        "ns=1;i=1302",
        callback=lambda v: print("kettle temperature:", v),
    )

    # Let the monitor print a few values
    time.sleep(5)
```

---

## Monitor several variables

To add several items in a single round-trip, pass a list of `NodeId`s. The result is a list of `MonitoredItem` handles in the same order as the input, and the same callback is invoked for every change:

```python
items = client.monitor(
    [
        "ns=1;i=1301",   # Kettle.Level
        "ns=1;i=1302",   # Kettle.Temperature
        "ns=1;i=1303",   # Kettle.WashStart
    ],
    callback=lambda v: print("kettle:", v),
)
```

The callback receives *just* the value — there is no built-in way to tell which `NodeId` a particular callback invocation came from. If you need per-node routing, give each item its own callback, or wrap the values in a closure that knows the source:

```python
def make_logger(name):
    def _cb(v):
        print(f"{name}: {v}")
    return _cb

items = []
for nid, name in [
    ("ns=1;i=1301", "level"),
    ("ns=1;i=1302", "temperature"),
    ("ns=1;i=1303", "wash_start"),
]:
    items.append(
        client.monitor(nid, callback=make_logger(name))
    )
```

#### Putting it all together

```python
import time
from o6 import Client

with Client("opc.tcp://localhost:4840") as client:
    items = client.monitor(
        [
            "ns=1;i=1301",   # Kettle.Level
            "ns=1;i=1302",   # Kettle.Temperature
            "ns=1;i=1303",   # Kettle.WashStart
        ],
        callback=lambda v: print("kettle update:", v),
    )
    time.sleep(5)
```

---

## Lifecycle callbacks and `DataChangeFilter`

There are two more functionalities available on the data-change surface: the lifecycle callbacks (`onCreated` / `onDeleted`) so you know when the server has actually accepted the item or torn it down, and `DataChangeFilter` to suppress notifications whose change is too small to care about.

### Lifecycle callbacks

`onCreated` runs once the server has acknowledged the item and assigned it a `MonitoredItemId`; `onDeleted` runs when the item is being torn down:

```python
def created(item, result):
    print("created:", item.id)

def deleted(item, sub_id, mon_id):
    print("deleted:", item.id)

item = client.monitor(
    "ns=1;i=1302",
    callback=lambda v: print("kettle temperature:", v),
    onCreated=created,
    onDeleted=deleted,
)
```

### `DataChangeFilter` — only notify on meaningful changes

By default the server notifies on every sample, even if the value moved by 0.001 °C. A `DataChangeFilter` lets you set a minimum delta before a notification is published. For the `Kettle.Setpoint` (`ns=1;i=1204`) you might want to be told only when the temperature moves by 1 °C or more:

```python
from o6 import Client
from o6.ns.ns0.datatypes import DataChangeFilter, DataChangeTrigger, DeadbandType

with Client("opc.tcp://localhost:4840") as client:
    item = client.monitor(
        "ns=1;i=1204",
        callback=lambda v: print("setpoint:", v),
        filter=DataChangeFilter(
            trigger=DataChangeTrigger.STATUS_VALUE,
            deadbandType=DeadbandType.ABSOLUTE,
            deadbandValue=1.0,
        ),
    )
```

A few notes on the parameters:

- **`trigger`** controls what must change for a notification to fire — `STATUS` (status code), `STATUS_VALUE` (status or value), or `STATUS_VALUE_TIMESTAMP` (all three, the default).
- **`deadbandType=NONE`** (the default) suppresses nothing — every sample becomes a notification.
- **`deadbandType=ABSOLUTE`** requires the absolute change to be at least `deadbandValue` before a notification fires.
- **`deadbandType=PERCENT`** requires the relative change to be at least `deadbandValue` percent.

!!! tip
    The deadband is applied by the *server*, not by the client. With a `DataChangeFilter` in place, samples that don't cross the deadband are dropped before they reach the client — the callback simply isn't called.

#### Putting it all together

```python
import time
from o6 import Client
from o6.ns.ns0.datatypes import DataChangeFilter, DataChangeTrigger, DeadbandType

with Client("opc.tcp://localhost:4840") as client:
    item = client.monitor(
        "ns=1;i=1204",   # Status.Setpoint
        callback=lambda v: print("setpoint changed:", v),
        samplingInterval=250.0,
        filter=DataChangeFilter(
            trigger=DataChangeTrigger.STATUS_VALUE,
            deadbandType=DeadbandType.ABSOLUTE,
            deadbandValue=1.0,
        ),
        onCreated=lambda it, result: print("live:", it.id),
        onDeleted=lambda it, sub_id, mon_id: print("gone:", it.id),
    )

    time.sleep(10)
```

---

## What's next?

- [Subscriptions](210_subscriptions.md) — what `client.monitor` is using under the hood, and how to create additional named subscriptions.
