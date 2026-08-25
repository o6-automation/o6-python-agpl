# Filter

You've split the distillery into two subscriptions — a fast one for the Kettle values and a slow one for the operator-facing `Status` variables. Both work, but two problems show up once you run them for a while:

- The fast subscription is *too* eager — `Kettle.Temperature` ticks 0.1 °C at a time during the steady-state distill phase, and you don't need a callback for every one of those.
- The slow subscription pushes the full `Status` object on every cycle, even during the long filling phase when you already know the values aren't going to change.

Filters give the server a way to suppress those. The deadband filter says *"only push when the change is meaningful"*, and the monitoring mode says *"stop pushing entirely for a while"*. Both are server-side — samples that don't qualify are dropped before they reach the client, so the callback simply isn't called.

This page walks through three steps:

- Apply a `DataChangeFilter` when creating the item (deadband, trigger).
- Modify the filter on an existing item without recreating it.
- Pause and resume notifications with `setMonitoringMode`.

!!! info
    This tutorial expects the [example server running](../setup.md) in the background, and assumes you know how to [create and connect](100_connect.md) a client, how to [browse](110_browse.md) the address space, how to [monitor data changes](200_monitor-datachange.md), and how to create separate [subscriptions](210_subscriptions.md). The `NodeId`s used below are the ones exposed by the distilling example server's `DistillingSystem` object at `ns=1;i=1000`.

---

## Apply a `DataChangeFilter` on creation

`DataChangeFilter` is the deadband-and-trigger filter for value-change monitors. Pass it as the `filter=` keyword to `client.monitor(...)`. The server then drops any sample whose value didn't move by at least `deadbandValue` since the last notification.

For the distillery's `Kettle.Temperature` (`ns=1;i=1302`), a 1 °C deadband is enough to catch every meaningful change (the sim drives the temperature in 0.5 °C-tick steps during heating, then sits at the setpoint):

```python
item = client.monitor(
    "ns=1;i=1302",   # Kettle.Temperature
    callback=lambda v: print("kettle temperature:", v),
    filter=DataChangeFilter(
        trigger=DataChangeTrigger.STATUS_VALUE,
        deadbandType=DeadbandType.ABSOLUTE,
        deadbandValue=1.0,
    ),
)
```

A few notes on the parameters:

- **`trigger`** controls what must change for a notification to fire — `STATUS` (status code only), `STATUS_VALUE` (status or value, the typical choice), or `STATUS_VALUE_TIMESTAMP` (all three, the spec default).
- **`deadbandType=NONE`** (the default) means "no deadband" — every sample becomes a notification.
- **`deadbandType=ABSOLUTE`** requires the absolute change since the last notification to be at least `deadbandValue`.
- **`deadbandType=PERCENT`** requires the relative change since the last notification to be at least `deadbandValue` percent.

The deadband is applied by the *server*, not the client. Samples that don't cross it are dropped before they reach the client.

#### Putting it all together

```python
import time
from o6 import Client
from o6.ns.ns0.datatypes import DataChangeFilter, DataChangeTrigger, DeadbandType

with Client("opc.tcp://localhost:4840") as client:
    item = client.monitor(
        "ns=1;i=1302",   # Kettle.Temperature
        callback=lambda v: print("kettle temperature:", v),
        filter=DataChangeFilter(
            trigger=DataChangeTrigger.STATUS_VALUE,
            deadbandType=DeadbandType.ABSOLUTE,
            deadbandValue=2.0,
        ),
    )
    time.sleep(10)
```

---

## Modify the filter on an existing item

You set a 2 °C deadband above, ran a batch, and realized that during the heating phase a 2 °C deadband is *too* coarse — you want every 1 °C tick so the chart looks smooth. You don't want to delete the item and recreate it (that loses its `MonitoredItemId` and any triggering links); instead, call `item.modify(filter=...)` to change the filter in place.

`modify(...)` takes only the parameters you want to change — any argument left as `None` is left alone:

```python
item.modify(
    filter=DataChangeFilter(
        trigger=DataChangeTrigger.STATUS_VALUE,
        deadbandType=DeadbandType.ABSOLUTE,
        deadbandValue=1.0,
    ),
)
```

You can also change the sampling interval, queue size, and discard policy in the same call:

```python
item.modify(
    samplingInterval=50.0,   # ms — sample more often
    queueSize=20,            # buffer more notifications between publishes
    discardOldest=True,      # drop the oldest when the queue is full
    filter=DataChangeFilter(
        trigger=DataChangeTrigger.STATUS_VALUE,
        deadbandType=DeadbandType.ABSOLUTE,
        deadbandValue=1.0,
    ),
)
```

The server replies with a `revisedSamplingInterval` and `revisedQueueSize` — the values it actually accepted. The server may round your request up to its minimum supported sampling interval (often 50 ms or 100 ms), so check the response if precision matters.

#### Putting it all together

```python
import time
from o6 import Client
from o6.ns.ns0.datatypes import DataChangeFilter, DataChangeTrigger, DeadbandType

with Client("opc.tcp://localhost:4840") as client:
    item = client.monitor(
        "ns=1;i=1302",   # Kettle.Temperature
        callback=lambda v: print("kettle temperature:", v),
        filter=DataChangeFilter(
            trigger=DataChangeTrigger.STATUS_VALUE,
            deadbandType=DeadbandType.ABSOLUTE,
            deadbandValue=2.0,
        ),
    )

    time.sleep(2)

    # Tighten the deadband mid-batch — the server switches the filter
    # without removing and re-creating the item.
    item.modify(
        filter=DataChangeFilter(
            trigger=DataChangeTrigger.STATUS_VALUE,
            deadbandType=DeadbandType.ABSOLUTE,
            deadbandValue=1.0,
        ),
    )

    time.sleep(8)
```

---

## Pause and resume notifications

Sometimes the right answer isn't a smaller deadband — it's "stop pushing for a while". The still's `Filling` phase is a few seconds during which the `Kettle.Temperature` and `Kettle.Level` aren't going to do anything interesting. Tell the server to keep sampling but not push:

```python
from o6.ns.ns0.datatypes import MonitoringMode
item.setMonitoringMode(MonitoringMode.SAMPLING)   # server samples, no push
```

While in `SAMPLING`, the item is still alive on the server and the server keeps sampling — your callback just isn't called. When you want updates again, switch back:

```python
item.setMonitoringMode(MonitoringMode.REPORTING)  # resume notifications
```

The third mode, `DISABLED`, is harder: the server stops sampling *and* stops pushing. The item is still on the server, but it has no current value — `REPORTING` resumes the sampling too. Use `DISABLED` only when you want to free the server-side resources temporarily.

For the distillery, a common pattern is to keep a slow subscription running for the entire run, but pause items you don't need during a particular phase:

```python
# Filling phase — Kettle.Temperature will be near ambient for ~2s
kettle_temp.setMonitoringMode(MonitoringMode.SAMPLING)
# ... fill ...
kettle_temp.setMonitoringMode(MonitoringMode.REPORTING)
# Distilling phase — Kettle.Temperature is interesting again
```

`setMonitoringMode` returns a `MaybeAwaitable` — `await` it in async code.

#### Putting it all together

```python
import time
from o6 import Client
from o6.ns.ns0.datatypes import MonitoringMode

with Client("opc.tcp://localhost:4840") as client:
    item = client.monitor(
        "ns=1;i=1302",   # Kettle.Temperature
        callback=lambda v: print("kettle temperature:", v),
    )

    time.sleep(3)
    print("--- pausing notifications ---")
    item.setMonitoringMode(MonitoringMode.SAMPLING)
    time.sleep(3)
    print("--- resuming notifications ---")
    item.setMonitoringMode(MonitoringMode.REPORTING)
    time.sleep(3)
```

---

## What's next?

- [Modify a subscription](220_modify-subscription.md) — change the publishing interval, lifetime count, or publishing-enabled flag on the whole subscription without recreating it.
- [Listen to events](240_listen-to-events.md) — `client.monitorEvent(...)` is the same shape, but for events instead of value changes. Events use an `EventFilter` instead of a `DataChangeFilter`.
