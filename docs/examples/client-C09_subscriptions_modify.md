# Subscription Modification

Demonstrates modifying a subscription and a monitored item.

Part 1 – Subscription.modify():
  Creates a subscription with publishing interval 500 ms, then changes it to
  2000 ms. We monitor a variable that is updated every 100 ms to illustrate
  the changing frequency of callbacks.

Part 2 – MonitoredItem.modify():
  Creates a fresh subscription with publishing interval 500 ms and a monitored
  item with sampling interval 100 ms, then changes the sampling interval to
  2000 ms. The sampling interval controls how often the server checks the node
  for changes, independently of how often PublishResponses are sent.

## 1. `Subscription.modify()`
`sub.modify(publishingInterval=...)` changes how often the *server sends*
publish responses, without tearing down the subscription or its monitored
items. Awaiting the call ensures the server has applied the change before
the next phase starts timing callbacks.

```python
async def main_subscription_modify():
    """Part 1: Subscription.modify() — changing the publishing interval."""
    async with o6.Client(endpoint_url) as client:
        received: list[tuple[float, object]] = []

        def on_change(value):
            received.append((time.monotonic(), value))
            print(f"Data change -> {value}")

        async def run_phase(duration: float, expected_cbs_per_sec: float) -> None:
            print(f"Writing NODE every {WRITE_INTERVAL:.1f} s for {duration:.1f} s ...")
            received.clear()
            counter = 0
            start = time.monotonic()
            while time.monotonic() - start < duration:
                counter += 1
                await client.write(NODE, o6.UInt32(counter))
                await asyncio.sleep(WRITE_INTERVAL)
            elapsed = time.monotonic() - start
            count = len(received)
            print(
                f"{count} callbacks in {elapsed:.1f} s "
                f"({count / elapsed:.1f} callbacks/s, expected ~{expected_cbs_per_sec}/s)"
            )

        # Create subscription and monitored item (sampling every 100 ms)
        sub = await client.createSubscription(
            publishingInterval=500.0, lifetimeCount=3600, maxKeepaliveCount=10
        )
        mon = await client.monitor(NODE, on_change, samplingInterval=100.0, subscription=sub)
        print(f"Created subscription, publishing_interval = {sub.publishingInterval} ms")

        await run_phase(duration=8.0, expected_cbs_per_sec=2)

        # Modify: slow down publishing
        await sub.modify(publishingInterval=2000.0)

        # NOTE: assigning `sub.publishingInterval = 2000.0` directly is fine
        # in a sync context, but property setters have no return value to
        # await, so they raise an error in an async context — use modify()
        # instead.

        print(f"Modified subscription, publishing_interval = {sub.publishingInterval} ms")

        await run_phase(duration=8.0, expected_cbs_per_sec=0.5)

        await sub.delete()
```

## 2. `MonitoredItem.modify()`
`mon.modify(samplingInterval=...)` changes how often the *server checks
the node* for a change, independently of the subscription's publishing
interval set above. A monitored item can only report a new value as often
as it samples, so slowing sampling down thins out callbacks even while
publishing interval stays fixed.

```python
async def main_monitored_item_modify():
    """Part 2: MonitoredItem.modify() — changing the sampling interval."""
    async with o6.Client(endpoint_url) as client:
        received: list[tuple[float, object]] = []

        def on_change(value):
            received.append((time.monotonic(), value))
            print(f"Data change -> {value}")

        async def run_phase(duration: float, expected_cbs_per_sec: float) -> None:
            print(f"Writing NODE every {WRITE_INTERVAL:.1f} s for {duration:.1f} s ...")
            received.clear()
            counter = 0
            start = time.monotonic()
            while time.monotonic() - start < duration:
                counter += 1
                await client.write(NODE, o6.UInt32(counter))
                await asyncio.sleep(WRITE_INTERVAL)
            elapsed = time.monotonic() - start
            count = len(received)
            print(
                f"{count} callbacks in {elapsed:.1f} s "
                f"({count / elapsed:.1f} callbacks/s, expected ~{expected_cbs_per_sec}/s)"
            )

        sub = await client.createSubscription(
            publishingInterval=500.0, lifetimeCount=3600, maxKeepaliveCount=10
        )
        mon = await client.monitor(NODE, on_change, samplingInterval=100.0, subscription=sub)
        print(f"Created monitored item, sampling_interval = {mon.params.samplingInterval:.0f} ms")

        await run_phase(duration=8.0, expected_cbs_per_sec=2)

        # Slow down sampling: server will now only check the node every 2000 ms
        await mon.modify(samplingInterval=2000.0)
        print(f"Modified monitored item, sampling_interval = {mon.params.samplingInterval:.0f} ms")

        await run_phase(duration=8.0, expected_cbs_per_sec=0.5)

        await sub.delete()
```

## Source Code

Download [`C09_subscriptions_modify.py`](client-C09_subscriptions_modify/C09_subscriptions_modify.py) to run it locally.
