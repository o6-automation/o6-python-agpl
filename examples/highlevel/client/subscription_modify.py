#!/usr/bin/env python3
"""
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
"""

import asyncio
import socket
import time
import o6
from o6 import types

localhost = socket.gethostname()
endpoint_url = f"opc.tcp://{localhost}:4840"

NODE = "ns=1;s=IntegerVariable"
WRITE_INTERVAL = 0.1  # write a new value every 100 ms


async def main_subscription_modify():
    """Part 1: Subscription.modify() — changing the publishing interval."""
    async with o6.Client(endpoint_url) as client:
        received: list[tuple[float, object]] = []

        def on_change(value):
            received.append((time.monotonic(), value))
            print(f"  data change: {value}")

        async def run_phase(duration: float, expected_cbs_per_sec: float) -> None:
            print(f"Write NODE every {WRITE_INTERVAL:.1f} s for {duration:.1f} s...")
            received.clear()
            counter = 0
            start = time.monotonic()
            while time.monotonic() - start < duration:
                counter += 1
                await client.write(NODE, types.UInt32(counter))
                await asyncio.sleep(WRITE_INTERVAL)
            elapsed = time.monotonic() - start
            count = len(received)
            print(
                f"\n  → {count} callbacks in {elapsed:.1f} s "
                f"({count / elapsed:.1f} callbacks/s, expected ~{expected_cbs_per_sec}/s)\n"
            )

        # Create subscription and monitored item (sampling every 100 ms)
        sub = await client.create_subscription(
            publishing_interval=500.0, lifetime_count=3600, max_keepalive_count=10
        )
        mon = await sub.monitor(NODE, on_change, sampling_interval=100.0)
        print(
            f"Created subscription with publishing_interval: {sub.publishing_interval} ms"
        )

        await run_phase(duration=8.0, expected_cbs_per_sec=2)

        # Modify: slow down publishing
        await sub.modify(publishing_interval=2000.0)

        # NOTE: below code is perfectly fine in a sync context to modify the publishing interval
        # however, set properties do not have a return value that can be awaited, so they raise an error when used inside an async context.
        # sub.publishing_interval = 2000.0

        print(
            f"Modified subscription, publishing_interval: {sub.publishing_interval} ms"
        )

        await run_phase(duration=8.0, expected_cbs_per_sec=0.5)

        await sub.delete()


async def main_monitored_item_modify():
    """Part 2: MonitoredItem.modify() — changing the sampling interval.

    The sampling interval controls how often the *server* checks the node for
    changes, independently of how often PublishResponses are sent.
    """
    async with o6.Client(endpoint_url) as client:
        received: list[tuple[float, object]] = []

        def on_change(value):
            received.append((time.monotonic(), value))
            print(f"  data change: {value}")

        async def run_phase(duration: float, expected_cbs_per_sec: float) -> None:
            print(f"Write NODE every {WRITE_INTERVAL:.1f} s for {duration:.1f} s...")
            received.clear()
            counter = 0
            start = time.monotonic()
            while time.monotonic() - start < duration:
                counter += 1
                await client.write(NODE, types.UInt32(counter))
                await asyncio.sleep(WRITE_INTERVAL)
            elapsed = time.monotonic() - start
            count = len(received)
            print(
                f"\n  → {count} callbacks in {elapsed:.1f} s "
                f"({count / elapsed:.1f} callbacks/s, expected ~{expected_cbs_per_sec}/s)\n"
            )

        sub = await client.create_subscription(
            publishing_interval=500.0, lifetime_count=3600, max_keepalive_count=10
        )
        mon = await sub.monitor(NODE, on_change, sampling_interval=100.0)
        print(
            f"Created monitored item, sampling_interval: {mon.monitoring_params.sampling_interval:.0f} ms"
        )

        await run_phase(duration=8.0, expected_cbs_per_sec=2)

        # Slow down sampling: server will now only check the node every 2000 ms
        await mon.modify(sampling_interval=2000.0)
        print(
            f"Modified monitored item, sampling_interval: {mon.monitoring_params.sampling_interval:.0f} ms"
        )

        await run_phase(duration=8.0, expected_cbs_per_sec=0.5)

        await sub.delete()


async def run_all():
    print("=" * 60)
    print("Part 1: Subscription.modify() — changing publishing_interval")
    print("=" * 60)
    await main_subscription_modify()

    print("=" * 60)
    print("Part 2: MonitoredItem.modify() — changing sampling_interval")
    print("=" * 60)
    await main_monitored_item_modify()


asyncio.run(run_all())
