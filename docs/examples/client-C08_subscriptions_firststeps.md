# Subscriptions

Demonstrates the high-level subscription API on the client: create a
``Subscription``, attach a ``MonitoredItem`` through
``client.monitor(...)``, and let the server push a callback every time
a watched value changes — no polling loop required.

The example talks to ``S03_firststeps.py``. Its simulation loop updates
``Plant / Counter`` (``ns=1;i=1004``) once per second, so the client
receives a data-change notification every tick.

!!! info "This example needs a running server"
    Start [Server First Steps](server-S03_firststeps.md) first:

    ```
    python examples/server/S03_firststeps.py
    ```

The high-level subscription API has three pieces:

- ``client.createSubscription(...)``: opens a publishing channel
  with the server and returns a ``Subscription`` object. It takes a
  ``publishing_interval`` (in milliseconds) that controls how often
  the server is *allowed* to send a publish response.
- ``client.monitor(nodeid, callback, ...)``: registers a
  ``MonitoredItem`` on a subscription. The
  ``sampling_interval`` controls how often the server *checks* the
  node for a change. The callback is invoked on the client's event
  loop thread whenever a new value is published.
- ``monitored_item.delete()`` and ``subscription.delete()``: clean
  up server-side resources. Skipping them leaks items on the
  server until the session ends.

## 1. The data-change callback
A 1-argument callback receives the new value directly; a 2-argument
callback also receives the ``MonitoredItem`` (useful when one
callback handles several items). The callback runs on the client's
event-loop thread.

```python
def on_counter_change(value) -> None:
    print(f"Counter changed -> {value}")
```

## 2. Open the subscription
``createSubscription(...)`` accepts the publishing interval and a
few lifetime/keepalive knobs. The defaults are good enough for
demos; the important argument is ``publishing_interval``: set it
close to the fastest change rate you care about.

```python
async def main() -> None:
    async with o6.Client(endpoint_url) as client:
        print("--- 2. Open the Subscription ---")
        subscription = await client.createSubscription(
            publishingInterval=500.0,
            lifetimeCount=3600,
            maxKeepaliveCount=10,
        )
        print(f"Subscription created, id = {subscription.id}")
```

## 3. Register a monitored item
``client.monitor(...)`` returns a ``MonitoredItem``. Pass the
``subscription=`` keyword to attach to an existing subscription;
omit it to use the client's default subscription. Multiple items
can share one subscription.

```python
print()
print("--- 3. Register a Monitored Item ---")
counter_item = await client.monitor(
    COUNTER,
    on_counter_change,
    samplingInterval=250.0,
    subscription=subscription,
)
print(f"Monitoring {COUNTER} ...")
```

## 4. Wait for server updates
``S03_firststeps.py`` updates ``Plant / Counter`` once per second,
so the callback above runs on the client's event loop once per
notification. The ``asyncio.sleep`` here just keeps the main
coroutine alive long enough to receive a few. Without it the
``async with`` block would tear down the session immediately.

```python
print()
print("--- 4. Wait for Server Updates ---")
for _ in range(5):
    await asyncio.sleep(1)
```

## 5. Clean up
Delete the monitored item first, then the subscription. Both calls
return awaitables; awaiting them ensures the server has
acknowledged the deletes before the ``async with`` block tears
down the session.

```python
        print()
        print("--- 5. Clean Up ---")
        await counter_item.delete()
        await subscription.delete()
        print("Subscription and monitored item removed.")

    print()
    print("=== Example completed ===")


if __name__ == "__main__":
    asyncio.run(main())
```

## Source Code

Download [`C08_subscriptions_firststeps.py`](client-C08_subscriptions_firststeps/C08_subscriptions_firststeps.py) to run it locally.
