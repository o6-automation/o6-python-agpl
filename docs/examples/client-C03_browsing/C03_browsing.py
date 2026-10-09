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


import os

import asyncio
import socket
import o6
from o6 import Client, AttributeId
from o6.ns import ns0

EXAMPLE_PORT = int(os.environ.get("O6_EXAMPLE_PORT", "4840"))
EXAMPLE_ENDPOINT = f"opc.tcp://localhost:{EXAMPLE_PORT}"


print("--- 1. Connection Setup ---")
localhost = "localhost"
endpoint_url = EXAMPLE_ENDPOINT
print(f"Connecting to {endpoint_url} ...")



with Client(endpoint_url) as client:
    print()
    print("--- 2. Sync: Get a Node Directly ---")
    node = client["i=85"]  # The standard `Objects` folder
    print(f"Node       = {node}")
    print(f"BrowseName = {node(attr=AttributeId.BROWSE_NAME)}")
    print(f"NodeClass  = {node(attr=AttributeId.NODE_CLASS)}")


    print()
    print("--- 3. Sync: Dot Traversal ---")
    node = node.Plant
    print(f"Node       = {node}")
    print(f"BrowseName = {node(attr=AttributeId.BROWSE_NAME)}")
    print(f"NodeClass  = {node(attr=AttributeId.NODE_CLASS)}")


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


    print()
    print("--- 5. Sync: Read and Write Through the Node ---")
    node = node.Temperature  # Drill into a leaf variable
    print(f"Node  = {node}")
    print(f"Value = {node()}")

    node(25.0)  # Plain Python float -> OPC UA Double
    print("Wrote Value -> 25.0")
    print(f"Value = {node()}")




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