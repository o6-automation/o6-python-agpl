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

Applies the *implementer class* pattern to a Variable. A UA
``ObjectType`` declares the Variable. A separate Python class
implements custom ``read`` and ``write`` behavior for it and is
registered with ``Server.implement``. Every read and write then runs
your Python code instead of using the node's native storage. Here, a
setpoint clamps writes to a valid range.
"""

# BEGIN MD
# The pattern has three parts:
#
# 1. **Declare** a UA ``ObjectType`` with a Variable child as a pure contract
#    with ``@o6.objecttype``. The declaration carries no behavior.
# 2. **Implement** the contract in a subclass. ``@o6.read("<member>")``
#    and ``@o6.write("<member>")`` bind Python behavior to the declared Variable.
#    Ordinary instance attributes hold the value.
# 3. **Register** the implementation with ``server.implement(Declaration, Impl)``.
#    The server then uses it for every instance of that UA type.
# END MD

import os

import time
from typing import Any

import o6
from o6.ns import ns0

EXAMPLE_PORT = int(os.environ.get("O6_EXAMPLE_PORT", "4840"))
EXAMPLE_ENDPOINT = f"opc.tcp://localhost:{EXAMPLE_PORT}"

# BEGIN MD
# ## 1. Declare the namespace and the ObjectType
# A custom type needs a namespace. Once registered, the short name
# ``"tutorial"`` works as the ``ns=`` argument below.
#
# ``SetpointType`` is an ``ObjectType`` with one ``Setpoint`` Variable of
# type ``Double``. ``accessLevel``/``userAccessLevel`` = 3 makes it
# readable and writable. The class is only the contract and has no
# behavior.
# END MD

# BEGIN CODE
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
    # END CODE


# BEGIN MD
# ## 2. Implement read and write
# Subclass the declaration and bind behavior to the Variable by its
# Python member name: ``"setpoint"``, not the ``ns=tutorial;Setpoint``
# BrowseName. Unlike ``@o6.call``, the read/write decorators resolve by
# attribute name, so the BrowseName namespace does not affect them.
#
# - ``@o6.read`` returns ``(StatusCode, value)``.
# - ``@o6.write`` receives the incoming ``DataValue`` and returns
#   ``(StatusCode,)``.
#
# The value lives in ``self._value`` instead of native storage, so the
# write callback can validate it before storing. Here it clamps to
# ``[0.0, 100.0]``, and every read returns the clamped value.
#
# Both callbacks also receive keyword-only context: ``session``,
# ``range`` for an index-range access, and ``includeSourceTimestamp`` for
# reads. This example ignores them via ``**kwargs``.
# END MD


# BEGIN CODE
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

    # END CODE


# BEGIN MD
# ``Server.ns.append`` learns about a namespace defined in Python from a
# module with ``__NAMESPACES__``. A generated NodeSet2 module has the same
# shape. The module also exposes the declared type so the server can
# publish it.
# END MD


# BEGIN CODE
def _tutorial_module() -> Any:
    import types

    module = types.ModuleType("tutorial_types")
    module.SetpointType = SetpointType
    module.__NAMESPACES__ = {o6.ns.tutorial}
    return module
    # END CODE


def main() -> None:
    endpoint_url = EXAMPLE_ENDPOINT

    # BEGIN CODE
    server = o6.Server(port=EXAMPLE_PORT)
    server.ns.append(_tutorial_module())
    # END CODE

    # BEGIN MD
    # ## 3. Register the implementation
    # ``server.implement(SetpointType, SetpointImpl)`` makes ``SetpointImpl``
    # the Python class for every ``SetpointType`` instance. ``addObject()``
    # with the declaration as type definition returns an implementation
    # instance whose ``Setpoint`` Variable already uses the custom callbacks.
    # END MD

    # BEGIN CODE
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
    # END CODE

    # BEGIN MD
    # ## 4. Read and write over the wire
    # A client reads and writes ``Setpoint`` like any other Variable. The
    # server routes each access through ``SetpointImpl``. Out-of-range writes
    # are clamped into ``[0.0, 100.0]``, and the read-back shows the clamped
    # value.
    # END MD

    # BEGIN CODE
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
    # END CODE

    print("\n=== Example completed ===")


if __name__ == "__main__":
    main()
