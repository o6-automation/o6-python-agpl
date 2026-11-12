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
Server Tutorial: Implementing a Custom ObjectType
=================================================

The *implementer class* pattern: declare a UA ``ObjectType`` as a
contract, implement its behavior in a separate Python class, and
register that class with ``Server.implement``. Every instance the server
creates for the type then runs your code.
"""


import os

import time
from typing import Any

import o6
from o6.ns import ns0

EXAMPLE_PORT = int(os.environ.get("O6_EXAMPLE_PORT", "4840"))
EXAMPLE_ENDPOINT = f"opc.tcp://localhost:{EXAMPLE_PORT}"


print("--- 1. Declare the namespace and the ObjectType ---")

o6.ns.namespace(
    shortname="tutorial",
    uri="http://o6-automation.com/UA/Tutorial/",
    version="1.0",
)


@o6.objecttype(ns="tutorial", nodeId="ns=tutorial;i=1", browseName="CounterType")
class CounterType(ns0.objtypes.BaseObjectType):
    """A counter object type — declared only, implemented separately."""

    increment: o6.node.MethodNode = o6.hasComponent(
        o6.call(
            browseName="ns=tutorial;Increment",
            inputArgs=[
                ns0.datatypes.Argument(
                    name="step",
                    dataType=o6.Int32,
                    valueRank=o6.ValueRank.SCALAR,
                    description="Amount to add to the counter",
                )
            ],
            outputArgs=[
                ns0.datatypes.Argument(
                    name="total",
                    dataType=o6.Int32,
                    valueRank=o6.ValueRank.SCALAR,
                    description="The counter value after incrementing",
                )
            ],
        )
    )




print("\n--- 2. Implement the ObjectType ---")


class CounterImpl(CounterType):
    """Provide the behavior for :class:`CounterType`."""

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._count = 0

    @o6.call("Increment")
    def _increment(self, step: o6.Int32) -> tuple[o6.StatusCode, o6.Int32]:
        """Add ``step`` to this instance's counter and return the new total."""
        self._count += int(step)
        return (o6.StatusCode.GOOD, o6.Int32(self._count))





def _tutorial_module() -> Any:
    import types

    module = types.ModuleType("tutorial_types")
    module.CounterType = CounterType
    module.__NAMESPACES__ = {o6.ns.tutorial}
    return module


def main() -> None:
    endpoint_url = EXAMPLE_ENDPOINT

    server = o6.Server(port=EXAMPLE_PORT)
    server.ns.append(_tutorial_module())


    print("\n--- 3. Register the implementation ---")
    server.implement(CounterType, CounterImpl)

    counter = server.addObject(
        "Counter",
        server.objectsNode,
        typeDefinition=CounterType,
        nodeId="ns=tutorial;i=1000",
        ns=o6.ns.tutorial.index,
    )
    print(f"addObject(typeDefinition=CounterType) -> {type(counter).__name__}")
    print(f"  isinstance(counter, CounterImpl) = {isinstance(counter, CounterImpl)}")


    print("\n--- 4. Dispatch, in-process and over the wire ---")
    print("In-process calls (counter.Increment):")
    print(f"  Increment(5) -> {counter.Increment(o6.Int32(5))}")
    print(f"  Increment(3) -> {counter.Increment(o6.Int32(3))}")

    server.start()
    print(f"Server running at {endpoint_url}")
    time.sleep(0.2)

    client = o6.Client(endpoint_url)
    client.connect()
    print("OPC UA client calls (client.call):")
    method_id = counter.Increment
    print(f"  Increment(10) -> {client.call(counter, method_id, [o6.Int32(10)])}")
    print(f"  Increment(1)  -> {client.call(counter, method_id, [o6.Int32(1)])}")
    client.disconnect()
    server.stop()

    print("\n=== Example completed ===")


if __name__ == "__main__":
    main()