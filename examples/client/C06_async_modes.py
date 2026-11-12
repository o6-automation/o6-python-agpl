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
``o6.Client`` is a *hybrid* client. Every operation (`read`, `write`,
`subscribe`, …) works as a blocking method *and* as an awaitable, and
the client picks the form at runtime. ``client.read(...)`` returns a
value inside a ``with`` block and an awaitable inside an
``async with`` block.

The example covers four patterns:

- **Case A — Sync, self-contained.** The default. The client runs its
  own event loop in a worker thread. ``client.connect()``,
  ``client.read(...)`` and ``client.disconnect()`` block until the
  result is back.
- **Case B — Async (``async with`` + ``await``).** The same calls
  return coroutines that you ``await``. Use this inside
  ``asyncio.run()`` or any other running asyncio loop.
- **Case C — Sync with a shared event loop.** You hand the client a
  loop you manage. The loop must be *running*; the SDK does not start
  it.
- **Case D — Mix-and-match (sync connect + async reads).** Connect
  synchronously at startup, then run the I/O in async tasks. The same
  ``client.read(...)`` can be awaited from an async context.

The example runs against ``S03_firststeps.py``.
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
# This is the default. The client finds no running event loop,
# creates one in a background worker thread and runs the OPC UA session
# there. ``client.connect()``, ``client.read(...)`` and
# ``client.disconnect()`` are plain blocking calls.
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
# Inside an ``async with`` block every method returns an awaitable.
# ``asyncio.run(...)`` at the bottom of the script creates the event
# loop. ``await c.read(...)`` suspends the coroutine until the value
# arrives.
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
# You can pass the client an ``asyncio`` event loop that your application
# manages. The loop must already be running.
#
# Run the loop in a daemon thread, stop it with
# ``call_soon_threadsafe(loop.stop)`` and join the thread before the
# application exits.
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
# Connect synchronously at startup, then run the I/O in async tasks. The
# same ``client.read(...)`` returns a value in a sync context and an
# awaitable in an async one.
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
