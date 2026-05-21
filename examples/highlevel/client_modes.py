#!/usr/bin/env python3

import sys
import os
import asyncio

# Add the o6 module to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import o6
import socket

# TODO: prevents the error: "server returned Endpoints with a different EndpointUrl" because "localhost" doesn't string match the hostname
localhost = socket.gethostname()
endpoint_url = f"opc.tcp://{localhost}:4840"

print("=== Client inside an async context ===")


async def async_client():
    c = o6.Client()
    c.config.endpoint_url = endpoint_url
    # async context will call conneect and disconnect automatically
    async with c:
        v = await c.read("i=2258")
        print(f'Reading value v="{v}"')


asyncio.run(async_client())


print("\n=== Self contained Client (with its own asyncio loop) ===")


def self_contained_client():
    c = o6.Client()
    c.config.endpoint_url = endpoint_url

    c.connect()
    v = c.read("i=2258")
    print(f'Reading value v="{v}"')
    c.disconnect()


self_contained_client()


print("\n=== Reusing event loop outside of async context ===")


def reuse_event_loop_sync():
    loop = asyncio.new_event_loop()

    c = o6.Client(loop=loop)
    c.config.endpoint_url = endpoint_url

    # The loop is not running at this point, which will trigger the client to run the loop internally until connect is done.
    # When connect returns the loop will NOT running anymore
    c.connect()
    v = c.read("i=2258")
    print(f'Reading value v="{v}"')
    c.disconnect()


reuse_event_loop_sync()


print("\n=== Using Client from an existing async application ===")


def existing_async_app():
    async def main():
        # In async code, let Client manage its own worker loop internally.
        # You only await the operations from the application loop.
        c = o6.Client()
        c.config.endpoint_url = endpoint_url

        async with c:
            v = await c.read("ns=1;s=IntegerVariable")
            print(f'Reading value v="{v}"')

    asyncio.run(main())


existing_async_app()


print("\n=== Reusing event loop with mix and match async ===")


def reuse_event_loop_mixmatch():
    c = o6.Client()
    c.config.endpoint_url = endpoint_url

    # Sync connect is fine.
    c.connect()

    # Async work can then await client operations from a separate app loop.
    async def do_some_async_stuff():
        v = await c.read("i=2258")
        print("whatever async stuff you want to do here")
        print(f'Reading value v="{v}"')

    asyncio.run(do_some_async_stuff())
    # Disconnect in synchronous mode again after the async work is done.
    c.disconnect()


reuse_event_loop_mixmatch()
