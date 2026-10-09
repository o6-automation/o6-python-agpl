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
Server Tutorial: Overriding Variable Read and Write
===================================================

Demonstrates the *implementer class* pattern applied to a Variable: declare a UA
``ObjectType`` that owns a Variable, then implement custom ``read`` and ``write``
behavior for that Variable in a separate Python class and register it with
``Server.implement``. Instead of storing the value in the node's native storage,
every read and write is routed through your Python code — here a setpoint that
clamps writes to a valid range.
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


@o6.objecttype(ns="tutorial", nodeId="ns=tutorial;i=1", browseName="SetpointType")
class SetpointType(ns0.objtypes.BaseObjectType):
    """A setpoint object type — declared only, implemented separately."""

    setpoint: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=tutorial;i=2",
            browseName="ns=tutorial;Setpoint",
            dataType=o6.Double,
            accessLevel=3,  # CurrentRead | CurrentWrite
            userAccessLevel=3,
        )
    )




print("\n--- 2. Implement read and write ---")


class SetpointImpl(SetpointType):
    """Provide custom read/write behavior for :class:`SetpointType`."""

    LOW, HIGH = 0.0, 100.0

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._value = 20.0

    @o6.read("setpoint")
    def _read_setpoint(self, **kwargs: Any) -> tuple[o6.StatusCode, o6.Double]:
        """Serve the current setpoint from Python state."""
        return (o6.StatusCode.GOOD, o6.Double(self._value))

    @o6.write("setpoint")
    def _write_setpoint(self, value: Any, **kwargs: Any) -> tuple[o6.StatusCode]:
        """Clamp the incoming value to a valid range, then store it."""
        clamped = max(self.LOW, min(self.HIGH, float(value.value)))
        print(f"Setpoint write requested={float(value.value):g} -> stored={clamped:g}")
        self._value = clamped
        return (o6.StatusCode.GOOD,)





def _tutorial_module() -> Any:
    import types

    module = types.ModuleType("tutorial_types")
    module.SetpointType = SetpointType
    module.__NAMESPACES__ = {o6.ns.tutorial}
    return module


def main() -> None:
    endpoint_url = EXAMPLE_ENDPOINT

    server = o6.Server(port=EXAMPLE_PORT)
    server.ns.append(_tutorial_module())


    print("\n--- 3. Register the implementation ---")
    server.implement(SetpointType, SetpointImpl)

    device = server.addObject(
        "Device",
        server.objectsNode,
        typeDefinition=SetpointType,
        nodeId="ns=tutorial;i=1000",
        ns=o6.ns.tutorial.index,
    )
    print(f"addObject(typeDefinition=SetpointType) -> {type(device).__name__}")
    print(f"  isinstance(device, SetpointImpl) = {isinstance(device, SetpointImpl)}")
    print(f"  server.read(Setpoint) = {server.read(device.setpoint)}")


    print("\n--- 4. Read and write over the wire ---")
    server.start()
    print(f"Server running at {endpoint_url}")
    time.sleep(0.2)

    client = o6.Client(endpoint_url)
    client.connect()
    variable = device.setpoint
    print(f"read            -> {client.read(variable)}")
    client.write(variable, o6.Double(150.0))  # above range
    print(f"read after 150  -> {client.read(variable)}")
    client.write(variable, o6.Double(-5.0))  # below range
    print(f"read after -5   -> {client.read(variable)}")
    client.write(variable, o6.Double(42.0))  # in range
    print(f"read after 42   -> {client.read(variable)}")
    client.disconnect()
    server.stop()

    print("\n=== Example completed ===")


if __name__ == "__main__":
    main()