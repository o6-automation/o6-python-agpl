#!/usr/bin/env python3

import sys
import os
import asyncio
import time

# Add the o6 module to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import o6
from o6 import types


def on_data_change(value):
    print(f"Data changed: {value}")


def main_sync():

    c = o6.Client()
    c.config.endpoint_url = "opc.tcp://localhost:4840"

    c.connect()

    print(
        "Available subscription methods:",
        [m for m in dir(c) if "subscription" in m or "monitoredItem" in m],
    )

    sub = c.create_subscription(
        publishing_interval=1000.0, lifetime_count=3600, max_keepalive_count=10
    )

    print(f"Subscription created with ID: {sub.subscription_id}")

    mon = sub.monitor("ns=1;s=IntegerVariable", on_data_change, sampling_interval=500)

    for i in range(5):
        c.write("ns=1;s=IntegerVariable", types.UInt32(200 + i))
        time.sleep(1)

    print("Cleaning up subscription...")
    mon.delete()
    sub.delete()

    val = c.read("i=2258")
    print(val)

    c.disconnect()


async def main_async():
    c = o6.Client()
    c.config.endpoint_url = "opc.tcp://localhost:4840"

    async with c:
        sub = await o6.Subscription(c, 1000.0, 3600, 10)
        mon = await o6.MonitoredItem.data_change(
            sub, "ns=1;s=IntegerVariable", on_data_change, sampling_interval=500
        )

        for i in range(5):
            await c.write("ns=1;s=IntegerVariable", types.UInt32(300 + i))
            await asyncio.sleep(1)

        await mon.delete()
        await sub.delete()

        val = await c.read("i=2258")
        print(val)


def on_data_change_context(monitem: o6.MonitoredItem, value):
    dc = f"Data changed: {value}"
    print(f"{dc}, {' ' * (30 - len(dc))} Context: {monitem.context}")


async def main_with_context():
    c = o6.Client()
    c.config.endpoint_url = "opc.tcp://localhost:4840"

    async with c:

        mysubscripton = await c.create_subscription(
            publishing_interval=1000.0, lifetime_count=3600, max_keepalive_count=10
        )

        await c.monitor(
            "ns=1;s=IntegerVariable",
            on_data_change_context,
            sampling_interval=500,
            context="MyContext",
        )
        mon = await c.monitor(
            "ns=1;s=DoubleVariable",
            on_data_change_context,
            sampling_interval=500,
            subscription=mysubscripton,
            context="another context",
        )

        for i in range(5):
            await c.write("ns=1;s=IntegerVariable", types.UInt32(400 + i))
            await c.write("ns=1;s=DoubleVariable", types.Double(123.456 / (i + 1)))
            await asyncio.sleep(1)

        await mon.delete()

        val = await c.read("i=2258")
        print(val)


# main_sync()
# asyncio.run(main_async())
asyncio.run(main_with_context())
