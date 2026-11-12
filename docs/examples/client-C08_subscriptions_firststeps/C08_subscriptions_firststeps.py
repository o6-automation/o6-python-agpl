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




def on_counter_change(value) -> None:
    print(f"Counter changed -> {value}")






async def main() -> None:
    async with o6.Client(endpoint_url) as client:
        print("--- 2. Open the Subscription ---")
        subscription = await client.createSubscription(
            publishingInterval=500.0,
            lifetimeCount=3600,
            maxKeepaliveCount=10,
        )
        print(f"Subscription created, id = {subscription.id}")


        print()
        print("--- 3. Register a Monitored Item ---")
        counter_item = await client.monitor(
            COUNTER,
            on_counter_change,
            samplingInterval=250.0,
            subscription=subscription,
        )
        print(f"Monitoring {COUNTER} ...")


        print()
        print("--- 4. Wait for Server Updates ---")
        for _ in range(5):
            await asyncio.sleep(1)


        print()
        print("--- 5. Clean Up ---")
        await counter_item.delete()
        await subscription.delete()
        print("Subscription and monitored item removed.")

    print()
    print("=== Example completed ===")


if __name__ == "__main__":
    asyncio.run(main())