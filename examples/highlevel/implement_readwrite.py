#!/usr/bin/env python3
# Copyright 2026 (c) o6 Automation GmbH
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

# BEGIN MD
# The pattern has three parts:
#
# 1. **Declare** a UA ``ObjectType`` with a Variable child as a pure contract
#    with ``@o6.objecttype``. The declaration carries no behavior.
# 2. **Implement** that contract in a separate subclass. ``@o6.read("<member>")``
#    and ``@o6.write("<member>")`` bind Python behavior to the declared Variable,
#    and ordinary instance attributes hold the value behind it.
# 3. **Register** the implementation with ``server.implement(Declaration, Impl)``
#    so the server uses it whenever it materialises that UA type.
# END MD

import time
from typing import Any

import o6
from o6.ns import ns0

# BEGIN MD
# ## 1. Declare the namespace and the ObjectType
# A custom type needs a namespace to live in. Registering it once makes the
# shortname ``"tutorial"`` usable as the ``ns=`` argument below.
#
# ``SetpointType`` is declared as an ``ObjectType`` owning a single ``Setpoint``
# Variable of type ``Double``. ``accessLevel``/``userAccessLevel`` = 3 marks it
# readable *and* writable so clients may write to it. No behavior is attached
# here — this class is only the contract.
# END MD

# BEGIN CODE
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
# Subclass the declaration and bind behavior to the declared Variable by its
# *Python member name* (``"setpoint"`` — the attribute above, not the
# ``ns=tutorial;Setpoint`` BrowseName). Unlike ``@o6.call``, the read/write
# decorators resolve by attribute name, so namespacing the BrowseName does not
# change their target. ``@o6.read`` returns ``(StatusCode, value)`` and
# ``@o6.write`` receives the incoming ``DataValue`` and returns ``(StatusCode,)``.
# Because the value lives in ``self._value`` rather than native storage, the
# write callback can validate it — here clamping to ``[0.0, 100.0]`` — before
# storing, and every read reflects the clamped value.
#
# Both callbacks also receive keyword-only context (``session``, ``range`` for
# an index-range access, and ``includeSourceTimestamp`` for reads); this example
# ignores them via ``**kwargs``.
# END MD


# BEGIN CODE
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
        print(f"    [write] requested={float(value.value):g} -> stored={clamped:g}")
        self._value = clamped
        return (o6.StatusCode.GOOD,)

    # END CODE


# BEGIN MD
# A throwaway module carrying ``__NAMESPACES__`` is how ``Server.ns.append``
# learns about a namespace defined in Python; a real NodeSet2 module builds the
# same shape. It also exposes the declared type so the server can publish it.
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
    endpoint_url = "opc.tcp://localhost:4840"

    # BEGIN CODE
    server = o6.Server(port=4840)
    server.ns.append(_tutorial_module())
    # END CODE

    # BEGIN MD
    # ## 3. Register the implementation
    # ``server.implement(SetpointType, SetpointImpl)`` wires ``SetpointImpl`` in
    # as the Python class the server uses whenever it materialises a
    # ``SetpointType`` instance. ``addObject()`` with the *declaration* as the
    # type definition then hands back a fully-wired *implementation* instance —
    # its ``Setpoint`` Variable already routes through the custom callbacks.
    # END MD

    # BEGIN CODE
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
    # A client reads and writes the ``Setpoint`` like any other Variable, but the
    # server routes each access through ``SetpointImpl``. Writing out-of-range
    # values shows the ``write`` override at work: the stored (and subsequently
    # read-back) value is clamped into ``[0.0, 100.0]``.
    # END MD

    # BEGIN CODE
    server.start()
    print(f"\nServer running at {endpoint_url}")
    time.sleep(0.2)

    client = o6.Client(endpoint_url)
    client.connect()
    variable = device.setpoint.nodeId
    print("\nOPC UA client read/write (Setpoint):")
    print(f"  read            -> {client.read(variable)}")
    client.write(variable, o6.Double(150.0))  # above range
    print(f"  read after 150  -> {client.read(variable)}")
    client.write(variable, o6.Double(-5.0))  # below range
    print(f"  read after -5   -> {client.read(variable)}")
    client.write(variable, o6.Double(42.0))  # in range
    print(f"  read after 42   -> {client.read(variable)}")
    client.disconnect()
    server.stop()
    # END CODE

    print("\n=== Variable read/write tutorial completed ===")


if __name__ == "__main__":
    main()
