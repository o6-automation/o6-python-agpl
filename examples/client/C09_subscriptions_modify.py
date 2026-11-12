#!/usr/bin/env python3
# Copyright 2026 (c) o6 Automation GmbH
# SPDX-License-Identifier: AGPL-3.0-or-later
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

"""
Modifies a subscription and a monitored item.

Part 1 – Subscription.modify():
  Creates a subscription with a 500 ms publishing interval and changes it
  to 2000 ms. The monitored variable updates every 100 ms, so the
  callback rate shows the change.

Part 2 – MonitoredItem.modify():
  Creates a new subscription (500 ms publishing interval) with a
  monitored item sampled every 100 ms, then changes the sampling
  interval to 2000 ms. The sampling interval sets how often the server
  checks the node, independent of how often PublishResponses are sent.
"""

import os

import asyncio
import time
import o6
from o6 import Server

EXAMPLE_PORT = int(os.environ.get("O6_EXAMPLE_PORT", "4840"))
EXAMPLE_ENDPOINT = f"opc.tcp://localhost:{EXAMPLE_PORT}"

localhost = "localhost"
endpoint_url = EXAMPLE_ENDPOINT

NODE = "ns=1;s=IntegerVariable"
WRITE_INTERVAL = 0.1  # write a new value every 100 ms


def _start_variable_server() -> Server:
    """Start an embedded server exposing the variable this example monitors."""
    server = Server(port=EXAMPLE_PORT)
    server.addVariable("IntegerVariable", server.objectsNode, o6.UInt32(0), nodeId=NODE)
    server.start()
    return server


# BEGIN MD
# ## 1. `Subscription.modify()`
# `sub.modify(publishingInterval=...)` changes how often the server sends
# publish responses. The subscription and its monitored items stay in
# place. Awaiting the call ensures the server has applied the change
# before the next phase starts timing callbacks.
# END MD


# BEGIN CODE
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
        # END CODE


# BEGIN MD
# ## 2. `MonitoredItem.modify()`
# `mon.modify(samplingInterval=...)` changes how often the server checks
# the node, independent of the publishing interval. An item reports at
# most one new value per sample, so slower sampling means fewer callbacks
# at the same publishing interval.
# END MD


# BEGIN CODE
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
        # END CODE


async def run_all():
    print("--- Part 1: Subscription.modify() ---")
    await main_subscription_modify()

    print()
    print("--- Part 2: MonitoredItem.modify() ---")
    await main_monitored_item_modify()

    print()
    print("=== Example completed ===")


if __name__ == "__main__":
    server = _start_variable_server()
    try:
        asyncio.run(run_all())
    finally:
        server.stop()
