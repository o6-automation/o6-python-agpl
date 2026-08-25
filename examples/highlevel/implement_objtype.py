#!/usr/bin/env python3
# Copyright 2026 (c) o6 Automation GmbH
"""
Server Tutorial: Implementing a Custom ObjectType
=================================================

Demonstrates the *implementer class* pattern: declare a UA ``ObjectType`` as a
contract, implement its behavior in a separate Python class, and register that
class with ``Server.implement`` so every instance the server materialises for
the type dispatches to your code.
"""

# BEGIN MD
# The pattern has three parts:
#
# 1. **Declare** a UA ``ObjectType`` (its Methods, Variables, ...) as a pure
#    contract with ``@o6.objecttype``. The declaration carries no behavior.
# 2. **Implement** that contract in a separate subclass. Python methods
#    decorated with ``@o6.call("<BrowseName>")`` supply the behavior for the
#    declared UA Methods, and ordinary instance attributes give each node its
#    own state.
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
# ``CounterType`` is then declared as an ``ObjectType`` with a single
# ``Increment`` Method that takes an ``Int32`` step and returns the running
# ``Int32`` total. The method is *declared* with ``o6.call(...)`` but left
# unimplemented on purpose — this class is only the contract.
# END MD

# BEGIN CODE
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
    # END CODE


# BEGIN MD
# ## 2. Implement the ObjectType
# Subclass the declaration and bind Python behavior to the declared Method with
# ``@o6.call("Increment")``. You can pass just the local name: o6 matches it
# against the type's declared Methods and resolves it to the qualified
# ``ns=tutorial;Increment`` for you. Pass the fully-qualified BrowseName only to
# disambiguate a name that is declared in more than one namespace — o6 rejects an
# ambiguous bare name with an error telling you to qualify it. Because each live
# node is an instance of this class, ordinary attributes such as ``self._count``
# give every Counter object its own state.
# END MD


# BEGIN CODE
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
    module.CounterType = CounterType
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
    # ``server.implement(CounterType, CounterImpl)`` is the line the whole
    # example is about: it wires ``CounterImpl`` in as the Python class the
    # server uses whenever it materialises a ``CounterType`` instance.
    #
    # As a result, ``addObject()`` with the *declaration* as the type definition
    # hands back a fully-wired *implementation* instance — you never name
    # ``CounterImpl`` at the call site.
    # END MD

    # BEGIN CODE
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
    # END CODE

    # BEGIN MD
    # ## 4. Dispatch, in-process and over the wire
    # Calling the Method attribute directly (``counter.Increment(...)``) runs the
    # implementation in-process. Starting the server and calling the same node
    # with an OPC UA client goes through the full service stack — both routes
    # land in ``CounterImpl._increment`` and share the node's ``_count`` state.
    # END MD

    # BEGIN CODE
    print("\nIn-process calls (counter.Increment):")
    print(f"  Increment(5) -> {counter.Increment(o6.Int32(5))}")
    print(f"  Increment(3) -> {counter.Increment(o6.Int32(3))}")

    server.start()
    print(f"\nServer running at {endpoint_url}")
    time.sleep(0.2)

    client = o6.Client(endpoint_url)
    client.connect()
    print("OPC UA client calls (client.call):")
    method_id = counter.Increment.nodeId
    print(f"  Increment(10) -> {client.call(counter.nodeId, method_id, [o6.Int32(10)])}")
    print(f"  Increment(1)  -> {client.call(counter.nodeId, method_id, [o6.Int32(1)])}")
    client.disconnect()
    server.stop()
    # END CODE

    print("\n=== ObjectType implementation tutorial completed ===")


if __name__ == "__main__":
    main()
