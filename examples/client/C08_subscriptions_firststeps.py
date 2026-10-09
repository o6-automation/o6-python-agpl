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
Client Subscriptions
=====================

Demonstrates the high-level subscription API on the client: create a
``Subscription``, attach a ``MonitoredItem`` through
``client.monitor(...)``, and let the server push a callback every time
a watched value changes — no polling loop required.

The example talks to ``S03_firststeps.py``. Its simulation loop updates
``Plant / Counter`` (``ns=1;i=1004``) once per second, so the client
receives a data-change notification every tick.
"""

# BEGIN MD
# The high-level subscription API has three pieces:
#
# - ``client.createSubscription(...)``: opens a publishing channel
#   with the server and returns a ``Subscription`` object. It takes a
#   ``publishing_interval`` (in milliseconds) that controls how often
#   the server is *allowed* to send a publish response.
# - ``client.monitor(nodeid, callback, ...)``: registers a
#   ``MonitoredItem`` on a subscription. The
#   ``sampling_interval`` controls how often the server *checks* the
#   node for a change. The callback is invoked on the client's event
#   loop thread whenever a new value is published.
# - ``monitored_item.delete()`` and ``subscription.delete()``: clean
#   up server-side resources. Skipping them leaks items on the
#   server until the session ends.
# END MD

import os

import asyncio
import socket
import o6

EXAMPLE_PORT = int(os.environ.get("O6_EXAMPLE_PORT", "4840"))
EXAMPLE_ENDPOINT = f"opc.tcp://localhost:{EXAMPLE_PORT}"

localhost = "localhost"
endpoint_url = EXAMPLE_ENDPOINT

# Plant / Counter (Int32) — updated by S03_firststeps.py once per second.
COUNTER = "ns=1;i=1004"


# BEGIN MD
# ## 1. The data-change callback
# A 1-argument callback receives the new value directly; a 2-argument
# callback also receives the ``MonitoredItem`` (useful when one
# callback handles several items). The callback runs on the client's
# event-loop thread.
# END MD


# BEGIN CODE
def on_counter_change(value) -> None:
    print(f"Counter changed -> {value}")


# END CODE


# BEGIN MD
# ## 2. Open the subscription
# ``createSubscription(...)`` accepts the publishing interval and a
# few lifetime/keepalive knobs. The defaults are good enough for
# demos; the important argument is ``publishing_interval``: set it
# close to the fastest change rate you care about.
# END MD


# BEGIN CODE
async def main() -> None:
    async with o6.Client(endpoint_url) as client:
        print("--- 2. Open the Subscription ---")
        subscription = await client.createSubscription(
            publishingInterval=500.0,
            lifetimeCount=3600,
            maxKeepaliveCount=10,
        )
        print(f"Subscription created, id = {subscription.id}")
        # END CODE

        # BEGIN MD
        # ## 3. Register a monitored item
        # ``client.monitor(...)`` returns a ``MonitoredItem``. Pass the
        # ``subscription=`` keyword to attach to an existing subscription;
        # omit it to use the client's default subscription. Multiple items
        # can share one subscription.
        # END MD

        # BEGIN CODE
        print()
        print("--- 3. Register a Monitored Item ---")
        counter_item = await client.monitor(
            COUNTER,
            on_counter_change,
            samplingInterval=250.0,
            subscription=subscription,
        )
        print(f"Monitoring {COUNTER} ...")
        # END CODE

        # BEGIN MD
        # ## 4. Wait for server updates
        # ``S03_firststeps.py`` updates ``Plant / Counter`` once per second,
        # so the callback above runs on the client's event loop once per
        # notification. The ``asyncio.sleep`` here just keeps the main
        # coroutine alive long enough to receive a few. Without it the
        # ``async with`` block would tear down the session immediately.
        # END MD

        # BEGIN CODE
        print()
        print("--- 4. Wait for Server Updates ---")
        for _ in range(5):
            await asyncio.sleep(1)
        # END CODE

        # BEGIN MD
        # ## 5. Clean up
        # Delete the monitored item first, then the subscription. Both calls
        # return awaitables; awaiting them ensures the server has
        # acknowledged the deletes before the ``async with`` block tears
        # down the session.
        # END MD

        # BEGIN CODE
        print()
        print("--- 5. Clean Up ---")
        await counter_item.delete()
        await subscription.delete()
        print("Subscription and monitored item removed.")

    print()
    print("=== Example completed ===")


if __name__ == "__main__":
    asyncio.run(main())
# END CODE
