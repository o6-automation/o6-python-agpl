#!/usr/bin/env python3
# Copyright 2026 (c) o6 Automation GmbH (Author: Andreas Ebner)
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
Low-level Server Example
=========================

Builds a server's address space with explicit NodeIds, data types and
access levels instead of the defaults of ``addVariable`` /
``addObject`` / ``addMethod``.

Topics covered:
- Creating a server with an explicit application URI
- Adding object, variable and method nodes with explicit NodeIds
- A read-only variable via an explicit access level
- Reading and writing node values with ``server.read()`` / ``server.write()``
  instead of calling a node handle

Connect with any OPC UA client at: opc.tcp://localhost:4840
"""

import os

import time
import o6
from o6 import Server
from o6.ns import ns0

EXAMPLE_PORT = int(os.environ.get("O6_EXAMPLE_PORT", "4840"))

# BEGIN MD
# `Server(applicationUri=...)` sets the URI advertised in the server's
# `ApplicationDescription`. The other examples keep the default.
# END MD


def main():
    # BEGIN CODE
    server = Server(port=EXAMPLE_PORT, applicationUri="urn:example:lowlevel-server")
    # END CODE

    # BEGIN MD
    # ## 1. Explicit NodeIds
    # `addObject()`, `addVariable()` and `addMethod()` accept a `nodeId=`
    # keyword. An explicit `o6.NodeId` stays the same across restarts, which
    # matters once a client script or a nodeset export refers to it.
    # END MD

    # BEGIN CODE
    print("--- 1. Explicit NodeIds ---")

    device_id = o6.NodeId("ns=1;i=100")
    server.addObject(
        "MyDevice",
        server.objectsNode,
        nodeId=device_id,
    )
    print(f"Added object node: {device_id}")

    temp_id = o6.NodeId("ns=1;i=1001")
    server.addVariable(
        "Temperature",
        device_id,
        22.5,
        nodeId=temp_id,
        dataType=o6.Double,
    )
    print(f"Added variable node: {temp_id}")
    # END CODE

    # BEGIN MD
    # ## 2. Explicit data type and access level
    # `dataType=` sets the OPC UA data type instead of inferring it from the
    # Python value. `writable=False` clears the write bit in the access
    # level: clients can read the value, and write requests fail with
    # `Bad_NotWritable`.
    # END MD

    # BEGIN CODE
    print()
    print("--- 2. Explicit Data Type and Access Level ---")

    counter_id = o6.NodeId("ns=1;i=1002")
    server.addVariable(
        "Counter",
        device_id,
        0,
        nodeId=counter_id,
        dataType=o6.Int32,
        writable=False,
    )
    print(f"Added variable node: {counter_id}")
    # END CODE

    # BEGIN MD
    # ## 3. A method with typed arguments
    # `addMethod()` takes the callback plus `inputArgs=` and `outputArgs=`
    # lists of `Argument` structs. Each struct gives one parameter's name,
    # data type and value rank. The callback returns a
    # `(StatusCode, *outputs)` tuple; `StatusCode.GOOD` reports success.
    # END MD

    # BEGIN CODE
    print()
    print("--- 3. A Method With Typed Arguments ---")

    def add_numbers(node, a, b):
        print(f"Add({a}, {b}) = {a + b}")
        return (o6.StatusCode.GOOD, a + b)

    method_id = o6.NodeId("ns=1;i=2001")
    server.addMethod(
        name="Add",
        parent=device_id,
        callback=add_numbers,
        inputArgs=[
            ns0.datatypes.Argument(
                name="A",
                dataType=o6.Double,
                valueRank=o6.ValueRank.SCALAR,
                description="First operand",
            ),
            ns0.datatypes.Argument(
                name="B",
                dataType=o6.Double,
                valueRank=o6.ValueRank.SCALAR,
                description="Second operand",
            ),
        ],
        outputArgs=[
            ns0.datatypes.Argument(
                name="Sum", dataType=o6.Double, valueRank=o6.ValueRank.SCALAR, description="A + B"
            ),
        ],
        nodeId=method_id,
    )
    print(f"Added method node: {method_id}")
    # END CODE

    # BEGIN MD
    # ## 4. Read and write by NodeId
    # `server.read(nodeId)` and `server.write(nodeId, value)` take a NodeId
    # instead of a node handle (`node()` / `node(value)`). Use them when the
    # NodeId was computed or looked up rather than kept in a variable.
    # END MD

    # BEGIN CODE
    print()
    print("--- 4. Read and Write by NodeId ---")

    server.start()
    print(f"Server running at opc.tcp://localhost:{EXAMPLE_PORT}")
    print("Press Ctrl+C to stop.")

    try:
        cycle = 0
        while True:
            cycle += 1

            server.write(temp_id, 22.5 + (cycle % 50) * 0.1).check()
            server.write(counter_id, cycle).check()

            if cycle % 10 == 0:
                temp_val = server.read(temp_id)
                counter_val = server.read(counter_id)
                print(f"Cycle {cycle}: Temp = {temp_val}, Counter = {counter_val}")

            time.sleep(0.1)
    except KeyboardInterrupt:
        print("Shutting down...")
    finally:
        server.stop()
        print("Server stopped.")


if __name__ == "__main__":
    main()
    # END CODE
