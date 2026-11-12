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

Uses the high-level subscription API: create a ``Subscription``, attach
a ``MonitoredItem`` with ``client.monitor(...)``, and receive a
callback each time the watched value changes, without polling.

The example runs against ``S03_firststeps.py``. Its simulation loop
updates ``Plant / Counter`` (``ns=1;i=1004``) once per second, so the
client receives one data-change notification per second.
"""

# BEGIN MD
# The high-level subscription API has three parts:
#
# - ``client.createSubscription(...)`` creates a subscription on the
#   server and returns a ``Subscription``. Its ``publishingInterval``
#   (milliseconds) sets how often the server may send a publish
#   response.
# - ``client.monitor(nodeid, callback, ...)`` registers a
#   ``MonitoredItem`` on a subscription. Its ``samplingInterval`` sets
#   how often the server checks the node for a change. The callback
#   runs on the client's event-loop thread for each published value.
# - ``monitored_item.delete()`` and ``subscription.delete()`` free the
#   server-side resources. Without them the items stay on the server
#   until the session ends.
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
# A 1-argument callback receives the new value. A 2-argument callback
# also receives the ``MonitoredItem``, which helps when one callback
# serves several items. The callback runs on the client's event-loop
# thread.
# END MD


# BEGIN CODE
def on_counter_change(value) -> None:
    print(f"Counter changed -> {value}")


# END CODE


# BEGIN MD
# ## 2. Open the subscription
# ``createSubscription(...)`` takes the publishing interval and some
# lifetime and keepalive settings. The defaults work for most cases. Set
# ``publishingInterval`` close to the fastest change rate you need.
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
        # ``client.monitor(...)`` returns a ``MonitoredItem``. Pass
        # ``subscription=`` to attach it to an existing subscription; omit it to
        # use the client's default subscription. Several items can share one
        # subscription.
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
        # The callback runs once per notification. ``asyncio.sleep`` keeps the
        # coroutine alive long enough to receive a few. Without it the
        # ``async with`` block closes the session immediately.
        # END MD

        # BEGIN CODE
        print()
        print("--- 4. Wait for Server Updates ---")
        for _ in range(5):
            await asyncio.sleep(1)
        # END CODE

        # BEGIN MD
        # ## 5. Clean up
        # Delete the monitored item first, then the subscription. Awaiting both
        # calls ensures the server has acknowledged the deletes before the
        # ``async with`` block closes the session.
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
