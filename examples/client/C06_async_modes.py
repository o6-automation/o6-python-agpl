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
Client Modes : Sync & Async Flexibility
=======================================
The ``o6.Client`` is a *hybrid* client: every operation on it
(`read`, `write`, `subscribe`, …) is exposed as a synchronous,
blocking method *and* as an awaitable coroutine, and the client
adapts at runtime to whichever calling convention the surrounding
code uses. The same ``client.read(...)`` call returns a value
directly inside a ``with`` block, and an awaitable inside an
``async with`` block.

This example walks through the four useful patterns:

- **Case A — Sync, self-contained.** The default. The client
  creates and runs its own event loop in a worker thread; you
  call ``client.connect()`` / ``client.read(...)`` /
  ``client.disconnect()`` and they block until the result is back.
- **Case B — Async (``async with`` + ``await``).** Same client
  object, but the calls return coroutines and you ``await`` them.
  Use this from inside an ``asyncio.run()`` or any other running
  asyncio loop.
- **Case C — Sync with a shared event loop.** The SDK lets you
  hand the client a loop you already manage. The loop must be
  *running* (the SDK does not start it for you).
- **Case D — Mix-and-match (sync connect + async reads).** Real
  industrial code often opens the connection synchronously at
  startup and then dispatches the actual I/O to async tasks. The
  client supports that too: the same ``client.read(...)`` can be
  awaited from an async context.

``S03_firststeps.py`` works fine for this example.
"""

import os

import asyncio
import socket
import threading
import o6

EXAMPLE_PORT = int(os.environ.get("O6_EXAMPLE_PORT", "4840"))
EXAMPLE_ENDPOINT = f"opc.tcp://localhost:{EXAMPLE_PORT}"

# BEGIN CODE
localhost = "localhost"
endpoint_url = EXAMPLE_ENDPOINT
print(f"Connecting to {endpoint_url} ...")
# END CODE


# BEGIN MD
# ## 1. Case A — Sync, Self-Contained
# This is the **default** and the most common case. The client
# detects that no event loop is running, creates a new one in a
# background worker thread, and runs the OPC UA session on that
# thread. From the caller's perspective, ``client.connect()``,
# ``client.read(...)``, and ``client.disconnect()`` are plain
# blocking Python calls.
# END MD

# BEGIN CODE
print()
print("--- 1. Case A: Sync, Self-Contained ---")


def case_a_sync_self_contained() -> None:
    c = o6.Client(endpointUrl=endpoint_url)
    c.connect()
    v = c.read("i=2258")  # Standard OPC UA node for Server Time
    print(f"Read = {v}")
    c.disconnect()


case_a_sync_self_contained()
# END CODE


# BEGIN MD
# ## 2. Case B — Async (``async with`` + ``await``)
# Same client object, but inside an ``async with`` block, every
# method returns an awaitable instead of a value. The
# ``asyncio.run(...)`` call at the bottom of the script creates the
# application-side event loop, the ``async with`` block runs the
# client session, and ``await c.read(...)`` blocks the application
# coroutine until the value comes back.
# END MD

# BEGIN CODE
print()
print("--- 2. Case B: Async (async with + await) ---")


async def case_b_async_context() -> None:
    c = o6.Client(endpointUrl=endpoint_url)
    async with c:
        v = await c.read("i=2258")
        print(f"Read = {v}")


asyncio.run(case_b_async_context())
# END CODE


# BEGIN MD
# ## 3. Case C — Sync with a Shared Event Loop
# If your application already manages an ``asyncio`` event loop,
# you can hand the client that loop. However the **loop must already be
# running**.
#
# The working pattern is to run the loop in a daemon thread,
# stop it via ``call_soon_threadsafe(loop.stop)``, and join the
# thread before the application exits.
# END MD

# BEGIN CODE
print()
print("--- 3. Case C: Sync with a Shared Event Loop ---")


def case_c_shared_loop() -> None:
    loop = asyncio.new_event_loop()
    runner = threading.Thread(target=loop.run_forever, daemon=True)
    runner.start()

    c = o6.Client(endpointUrl=endpoint_url, loop=loop)
    c.connect()
    v = c.read("i=2258")
    print(f"Read = {v}")
    c.disconnect()

    # Stop the worker thread and wait for it to exit.
    loop.call_soon_threadsafe(loop.stop)
    runner.join(timeout=2.0)
    print("Loop stopped, thread joined.")


case_c_shared_loop()
# END CODE


# BEGIN MD
# ## 4. Case D — Mix-and-Match (Sync Connect, Async Reads)
# A common real-world pattern: open the connection synchronously
# at startup, then dispatch the actual I/O to async tasks once
# the application is up and running. The same ``client.read(...)``
# call returns a value in a sync context and an awaitable in an
# async one.
# END MD

# BEGIN CODE
print()
print("--- 4. Case D: Mix-and-Match (Sync Connect, Async Reads) ---")


def case_d_mix_and_match() -> None:
    c = o6.Client(endpointUrl=endpoint_url)
    c.connect()  # sync — runs in the main thread

    async def read_async() -> None:
        v = await c.read("i=2258")
        print(f"Read (async) = {v}")

    asyncio.run(read_async())  # async — runs in its own loop

    c.disconnect()  # sync — back on the main thread
    print("Disconnected.")


case_d_mix_and_match()

print()
print("=== Example completed ===")
# END CODE
