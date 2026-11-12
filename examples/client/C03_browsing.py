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
Walks an OPC UA server's address space from the client. It starts at the
standard `Objects` folder, navigates to a node by BrowseName (dot
syntax) or *browse path* (index syntax), lists the references of a node
with `client.browse(...)`, and reads and writes a leaf variable through
its `Node` handle.

The example uses the address space of `S03_firststeps.py`:

    Objects/
    └── Plant/                  (Object)
        ├── Temperature         (Double,  ns=1;i=1001)
        ├── Pressure            (Double,  ns=1;i=1002)
        ├── Status              (String,  ns=1;i=1003)
        ├── Counter             (Int32,   ns=1;i=1004)
        ├── Running             (Boolean, ns=1;i=1005)
        └── Add                 (Method,  ns=1;i=2001)

It shows the **synchronous** style (`with Client(...)`, direct attribute
and value access) and the **asynchronous** style (`async with`,
`await`).
"""

# BEGIN MD
# Clients often do not know server-assigned NodeIds. The *BrowseName* of a
# node is the stable identifier to program against. `o6` adds three layers
# on top of the raw `Browse` service:
#
# - `client.browse(...)` returns a list of references.
# - `client[NodeId]` returns a `Node`.
# - `Node` supports dot syntax (`.Plant`) and browse-path syntax
#   (`["/Objects/Plant"]`), so you can walk the tree without tracking
#   NodeIds.
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
# Same as in `C02_firststeps.py`.
# END MD

# BEGIN CODE
print("--- 1. Connection Setup ---")
localhost = "localhost"
endpoint_url = EXAMPLE_ENDPOINT
print(f"Connecting to {endpoint_url} ...")
# END CODE


# BEGIN MD
# ## 2. Sync: Get a Node Directly
# `client[nodeid]` returns a `Node` for the address space entry. In a
# synchronous `with` block the call blocks until the `NodeClass` and
# `BrowseName` attributes are read. The `Node` is then a local handle
# that can be printed, browsed and indexed.
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
    # `node.Child` moves one level down by BrowseName, like attribute access
    # on a Python object. `Plant` lives in the user namespace; the server
    # allocates its NodeId at startup.
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
    # `client.browse(node, ...)` returns the `ReferenceDescription`s one level
    # out from `node`. The `resultMask` keyword selects the fields each
    # reference carries. The code composes `BrowseResultMask` flags for
    # BrowseName, node class, display name and type definition.
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
    # `node()` returns the current value of the `Value` attribute.
    # `node(value)` writes a value. The SDK infers the OPC UA data type from
    # the Python type: a `float` is written as `Double`, an `int` as `Int32`,
    # and so on.
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
# Use the asynchronous form when the application (a web server, a UI
# loop, ...) already runs an `asyncio` event loop. Inside
# `async with Client(...) as client:` the `client[...]` and
# `client.browse(...)` calls are awaitable. Dot traversal returns an
# `AwaitableNode` that chains the `await`s.
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
