#!/usr/bin/env python3
# Copyright 2026 (c) o6 Automation GmbH
"""
Client Subscriptions
=============

Demonstrates the high-level subscription API on the client: create a
``Subscription``, attach a ``MonitoredItem`` through
``client.monitor(...)``, and let the server push a callback every time
a watched value changes — no polling loop required.

The example talks to ``basic_server.py`` so start that script in one
terminal before running this one. The server's simulation loop
updates ``Plant / Counter`` (``ns=1;i=1004``) once per second, so the
client receives a data-change notification every tick.
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

import asyncio
import socket
import o6

localhost = "localhost"
endpoint_url = f"opc.tcp://{localhost}:4840"

# Plant / Counter (Int32) — updated by basic_server.py once per second.
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
    print(f"  [counter]  Plant.Counter = {value}")


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
        subscription = await client.createSubscription(
            publishingInterval=500.0,
            lifetimeCount=3600,
            maxKeepaliveCount=10,
        )
        print(f"Subscription created (id={subscription.id})")
        # END CODE

        # BEGIN MD
        # ## 3. Register a monitored item
        # ``client.monitor(...)`` returns a ``MonitoredItem``. Pass the
        # ``subscription=`` keyword to attach to an existing subscription;
        # omit it to use the client's default subscription. Multiple items
        # can share one subscription.
        # END MD

        # BEGIN CODE
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
        # ``basic_server.py`` updates ``Plant / Counter`` once per second, so
        # the callback above runs on the client's event loop once per
        # notification. The ``asyncio.sleep`` here just keeps the main
        # coroutine alive long enough to receive a few. Without it the
        # ``async with`` block would tear down the session immediately.
        # END MD

        # BEGIN CODE
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
        print("Cleaning up...")
        await counter_item.delete()
        await subscription.delete()

    print("Done.")


if __name__ == "__main__":
    asyncio.run(main())
# END CODE
