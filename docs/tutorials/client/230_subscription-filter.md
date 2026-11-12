# Filter

Filters let the server suppress notifications you don't need. A deadband filter pushes only changes above a threshold. The monitoring mode stops pushing for a while. Both act on the server: samples that don't qualify are dropped before they reach the client, and the callback is not called.

The two distillery subscriptions from [Subscriptions](210_subscriptions.md) show why:

- The fast subscription is too eager. `Kettle.Temperature` moves 0.1 °C at a time during the steady-state distill phase, and you don't need a callback for each step.
- The slow subscription pushes the full `Status` object on every cycle, even during the long filling phase when the values don't change.

This page covers:

- Apply a `DataChangeFilter` when creating the item (deadband, trigger).
- Modify the filter on an existing item without recreating it.
- Pause and resume notifications with `setMonitoringMode`.

!!! info
    This tutorial needs the [example server running](../setup.md) in the background. It assumes you know how to [create and connect](100_connect.md) a client, [browse](110_browse.md) the address space, [monitor data changes](200_monitor-datachange.md), and create separate [subscriptions](210_subscriptions.md). The NodeIds below belong to the example server's `DistillingSystem` object at `ns=1;i=1000`.

---

## Apply a `DataChangeFilter` on creation

`DataChangeFilter` sets the deadband and trigger for data-change monitors. Pass it as `filter=` to `client.monitor(...)`. The server then drops any sample whose value moved less than `deadbandValue` since the last notification.

For `Kettle.Temperature` (`ns=1;i=1302`), a 1 °C deadband catches every meaningful change. The simulation raises the temperature in 0.5 °C steps during heating, then holds it at the setpoint:

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

- **`trigger`** controls what must change for a notification to fire — `STATUS` (status code only), `STATUS_VALUE` (status or value, the typical choice), or `STATUS_VALUE_TIMESTAMP` (all three, the spec default).
- **`deadbandType=NONE`** (the default) means no deadband: every sample becomes a notification.
- **`deadbandType=ABSOLUTE`** requires the absolute change since the last notification to be at least `deadbandValue`.
- **`deadbandType=PERCENT`** requires the relative change since the last notification to be at least `deadbandValue` percent.

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

The script above uses a 2 °C deadband, which is too coarse for a smooth chart during heating. To switch to 1 °C, call `item.modify(filter=...)`. It changes the filter in place. Deleting and recreating the item would lose its `MonitoredItemId` and any triggering links.

`modify(...)` changes only the parameters you pass. Arguments left as `None` keep their current value:

```python
item.modify(
    filter=DataChangeFilter(
        trigger=DataChangeTrigger.STATUS_VALUE,
        deadbandType=DeadbandType.ABSOLUTE,
        deadbandValue=1.0,
    ),
)
```

The same call can change the sampling interval, queue size, and discard policy:

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

The server replies with `revisedSamplingInterval` and `revisedQueueSize`, the values it accepted. It may round your request up to its minimum supported sampling interval (often 50 ms or 100 ms). Check the response if precision matters.

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

To stop notifications for a while, change the monitoring mode. During the few seconds of the `Filling` phase, `Kettle.Temperature` and `Kettle.Level` don't change in interesting ways. Tell the server to keep sampling but not push:

```python
from o6.ns.ns0.datatypes import MonitoringMode
item.setMonitoringMode(MonitoringMode.SAMPLING)   # server samples, no push
```

In `SAMPLING` mode the item stays on the server and is still sampled, but your callback isn't called. Switch back to get updates again:

```python
item.setMonitoringMode(MonitoringMode.REPORTING)  # resume notifications
```

In the third mode, `DISABLED`, the server stops sampling and stops pushing. The item stays on the server but has no current value. `REPORTING` resumes sampling too. Use `DISABLED` only to free server-side resources temporarily.

A common pattern keeps a slow subscription running for the entire run and pauses items you don't need in a particular phase:

```python
# Filling phase — Kettle.Temperature will be near ambient for ~2s
kettle_temp.setMonitoringMode(MonitoringMode.SAMPLING)
# ... fill ...
kettle_temp.setMonitoringMode(MonitoringMode.REPORTING)
# Distilling phase — Kettle.Temperature is interesting again
```

`setMonitoringMode` returns a `MaybeAwaitable`; `await` it in async code.

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

## Next steps

| Topic | What it covers |
|---|---|
| [Modify a subscription](220_modify-subscription.md) | Change the publishing interval, lifetime count, or publishing-enabled flag on the whole subscription without recreating it. |
| [Listen to events](240_listen-to-events.md) | `client.monitorEvent(...)` is the same shape, but for events instead of value changes. Events use an `EventFilter` instead of a `DataChangeFilter`. |
