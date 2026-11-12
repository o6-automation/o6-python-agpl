# Monitor datachange

In [Call a method](130_call-method.md) you started a batch and set a new `Setpoint`. This page shows how to watch the batch progress. Polling costs a round-trip per read, and most reads return the same value. `client.monitor` instead registers a data-change monitored item on the client's default subscription. The server pushes each value change to your callback.

This page covers:

- Register a single data-change monitor with a callback.
- Monitor several variables in one round-trip.
- Use the lifecycle callbacks (`onCreated` / `onDeleted`) and a `DataChangeFilter` to control when you get notified.

!!! info
    This tutorial needs the [example server running](../setup.md) in the background. It assumes you know how to [create and connect](100_connect.md) a client and [browse](110_browse.md) the address space. The NodeIds below belong to the example server's `DistillingSystem` object at `ns=1;i=1000`.

---

## Register a single data-change monitor

Pass one NodeId and a callback. The callback runs once per value-change notification from the server. This example watches `Kettle.Temperature` (`ns=1;i=1302`), which climbs from `20.0` to `85.0` °C during the heating phase of every batch:

```python

item = client.monitor(
    "ns=1;i=1302",
    callback=lambda v: print("kettle temperature:", v),
)
```

The default sampling interval is 100 ms. The callback receives the new value. To also get the timestamp and status code, pass `value_only=False`; the callback then receives a `DataValue`.

`monitor()` returns a `MonitoredItem` handle. The item is removed when the client disconnects, when the subscription is deleted, or when you call `item.delete()`.

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

Pass a list of NodeIds to add several items in one round-trip. The result is a list of `MonitoredItem` handles in input order. The same callback runs for every change:

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

The callback receives only the value, so it cannot tell which node changed. For per-node routing, give each item its own callback, for example a closure that knows the source:

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

The lifecycle callbacks tell you when the server has accepted or removed an item. A `DataChangeFilter` suppresses notifications for small changes.

### Lifecycle callbacks

`onCreated` runs once the server has acknowledged the item and assigned it a `MonitoredItemId`. `onDeleted` runs when the item is removed:

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

By default the server notifies on every sample, even if the value moved by 0.001 °C. A `DataChangeFilter` sets a minimum change before a notification is published. This example notifies only when `Status.Setpoint` (`ns=1;i=1204`) moves by 1 °C or more:

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

- **`trigger`** controls what must change for a notification to fire — `STATUS` (status code), `STATUS_VALUE` (status or value), or `STATUS_VALUE_TIMESTAMP` (all three, the default).
- **`deadbandType=NONE`** (the default) suppresses nothing — every sample becomes a notification.
- **`deadbandType=ABSOLUTE`** requires the absolute change to be at least `deadbandValue` before a notification fires.
- **`deadbandType=PERCENT`** requires the relative change to be at least `deadbandValue` percent.

!!! tip
    The server applies the deadband. Samples that don't cross it are dropped before they reach the client, and the callback is not called.

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

## Next steps

| Topic | What it covers |
|---|---|
| [Subscriptions](210_subscriptions.md) | What `client.monitor` is using under the hood, and how to create additional named subscriptions. |
