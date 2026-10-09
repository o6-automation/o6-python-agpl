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
Client Browsing : Address Space Traversal
=========================================
Demonstrates how to walk an OPC UA server's address space from the
client: starting from the standard `Objects` folder, navigating to a
specific node by *browse name* (dot syntax) or *browse path* (index
syntax), enumerating the references coming out of a node with
`client.browse(...)`, and reading / writing the value of a leaf
variable through the resulting `Node` handle.

The example is wired against `S03_firststeps.py`. The address space we
walk is:

    Objects/
    └── Plant/                  (Object)
        ├── Temperature         (Double,  ns=1;i=1001)
        ├── Pressure            (Double,  ns=1;i=1002)
        ├── Status              (String,  ns=1;i=1003)
        ├── Counter             (Int32,   ns=1;i=1004)
        ├── Running             (Boolean, ns=1;i=1005)
        └── Add                 (Method,  ns=1;i=2001)

The example shows both the **synchronous** style (blocking `with
Client(...)` and direct attribute / value access) and the **asynchronous**
style (`async with`, `await` everywhere) so you can compare the two.
"""

# BEGIN MD
# Browsing the address space is one of the most useful patterns in a
# real OPC UA client: server-assigned NodeIds are often not known by the client,
# and the *browse name* of a node is the stable
# identifier you actually want to program against. The `o6` SDK gives
# you three layers of convenience on top of the raw `Browse` service:
# `client.browse(...)` returns a list of references, `client[NodeId]`
# hands back a `Node`, and `Node` itself supports dot syntax
# (`.Plant`) and browse-path syntax (`["/Objects/Plant"]`) so you can
# walk the tree without manually tracking NodeIds.
# END MD

import os

import asyncio
import socket
import o6
from o6 import Client, AttributeId
from o6.ns import ns0

EXAMPLE_PORT = int(os.environ.get("O6_EXAMPLE_PORT", "4840"))
EXAMPLE_ENDPOINT = f"opc.tcp://localhost:{EXAMPLE_PORT}"

# BEGIN MD
# ## 1. Connection Setup
# Same as in `C02_firststeps.py`: build the endpoint URL from the local
# hostname so it matches the URL the server advertises during discovery.
# END MD

# BEGIN CODE
print("--- 1. Connection Setup ---")
localhost = "localhost"
endpoint_url = EXAMPLE_ENDPOINT
print(f"Connecting to {endpoint_url} ...")
# END CODE


# BEGIN MD
# ## 2. Sync: Get a Node Directly
# `client[nodeid]` returns a `Node` object that mirrors the address
# space entry. In a synchronous `with` block the call blocks until the
# `NodeClass` and `BrowseName` attributes have been read; from there
# the `Node` is a local handle that can be printed, browsed, and
# indexed.
# END MD

# BEGIN CODE
with Client(endpoint_url) as client:
    print()
    print("--- 2. Sync: Get a Node Directly ---")
    node = client["i=85"]  # The standard `Objects` folder
    print(f"Node       = {node}")
    print(f"BrowseName = {node(attr=AttributeId.BROWSE_NAME)}")
    print(f"NodeClass  = {node(attr=AttributeId.NODE_CLASS)}")
    # END CODE

    # BEGIN MD
    # ## 3. Sync: Dot Traversal
    # `node.Child` walks one level into the address space by browse name
    # (the same way you'd navigate Python objects).
    #
    # We use this to reach `Plant` and then `Plant.Temperature`. Both
    # `Plant` (its NodeId is allocated at server startup) and
    # `Temperature` (its data type is `Double`) live in the user namespace.
    # END MD

    # BEGIN CODE
    print()
    print("--- 3. Sync: Dot Traversal ---")
    node = node.Plant
    print(f"Node       = {node}")
    print(f"BrowseName = {node(attr=AttributeId.BROWSE_NAME)}")
    print(f"NodeClass  = {node(attr=AttributeId.NODE_CLASS)}")
    # END CODE

    # BEGIN MD
    # ## 4. Sync: Enumerate Children with `client.browse(...)`
    # `client.browse(node, ...)` walks one level out from `node` and
    # returns a list of `ReferenceDescription`s. The `result_mask` keyword
    # controls which fields each reference carries back: `63` asks for
    # every reference field (browse name, display name, node class, type
    # definition, …) so we can print the children with full detail.
    # END MD

    # BEGIN CODE
    print()
    print("--- 4. Sync: Enumerate Children with client.browse(...) ---")
    refs = client.browse(
        node,
        resultMask=(
            ns0.datatypes.BrowseResultMask.BROWSE_NAME
            | ns0.datatypes.BrowseResultMask.NODE_CLASS
            | ns0.datatypes.BrowseResultMask.DISPLAY_NAME
            | ns0.datatypes.BrowseResultMask.TYPE_DEFINITION
        ),
    )
    for r in refs:
        print(
            f"  {r.nodeId}  "
            f"browseName={r.browseName}  "
            f"display_name={r.displayName}  "
            f"type={r.nodeClass.name}"
        )
    # END CODE

    # BEGIN MD
    # ## 5. Sync: Read and Write Through the `Node`
    # Calling a `Node` with no arguments (`node()`) returns the current
    # value of its `Value` attribute; calling it with a value
    # (`node(value)`) writes that value. The SDK interprets the OPC UA
    # data type from the Python type of the value, so a Python `float`
    # is written as a `Double`, a Python `int` as an `Int32`, and so on.
    # END MD

    # BEGIN CODE
    print()
    print("--- 5. Sync: Read and Write Through the Node ---")
    node = node.Temperature  # Drill into a leaf variable
    print(f"Node  = {node}")
    print(f"Value = {node()}")

    node(25.0)  # Plain Python float -> OPC UA Double
    print("Wrote Value -> 25.0")
    print(f"Value = {node()}")
# END CODE


# BEGIN MD
# ## 6. Async: The Same, Inside an Event Loop
# The asynchronous form is useful when the surrounding application
# (a web server, a UI loop, ...) is already running its own
# `asyncio` event loop. Inside an `async with Client(...) as client:`
# the same `client[...]` and `client.browse(...)` calls become
# awaitable. The dot-traversal also returns an `AwaitableNode` that
# chains `await`s for you.
# END MD


# BEGIN CODE
async def main() -> None:
    async with Client(endpoint_url) as client:
        print()
        print("--- 6. Async: The Same, Inside an Event Loop ---")
        # client["..."] returns an awaitable; the `await` resolves it
        # to a Node handle.
        node = await client["i=85"]
        node = await node.Plant  # async dot-traversal
        node = await node.Temperature  # async dot-traversal into a leaf

        print(f"Node  = {node}")
        print(f"Value = {await node()}")

        await node(30.0)
        print("Wrote Value -> 30.0")
        print(f"Value = {await node()}")


asyncio.run(main())
print()
print("=== Example completed ===")
# END CODE
