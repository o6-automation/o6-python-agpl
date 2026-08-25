#!/usr/bin/env python3
# Copyright 2026 (c) o6 Automation GmbH (Author: Andreas Ebner)
"""
Low-level Server Example
=========================

Demonstrates using the ``_o6`` C extension directly to create and
run an OPC UA server.  This gives full control over all attributes
and OPC UA types but requires more boilerplate than the high-level
``o6.Server`` wrapper.

Topics covered:
- Creating a server with ``_o6.Server``
- Configuring the application description
- Adding variable, object, and method nodes with explicit attributes
- Manual startup / iterate / shutdown lifecycle
- Reading and writing values on the server side

Connect with any OPC UA client at: opc.tcp://localhost:4840
"""

import asyncio
import logging
import time
from o6 import _o6
import o6
from o6._o6 import types


def main():
    # ── Create and configure ─────────────────────────────────────
    loop = asyncio.new_event_loop()
    logger = logging.getLogger(__name__)
    server = _o6.Server(port=4840, loop=loop, logger=logger)

    cfg = server.config
    cfg.applicationUri = "urn:example:lowlevel-server"

    app_desc = types.ApplicationDescription()
    app_desc.applicationUri = "urn:example:lowlevel-server"
    app_desc.applicationName = types.LocalizedText("Low-level Example Server")
    app_desc.applicationType = types.ApplicationType.SERVER
    app_desc.productUri = "urn:example:product"
    cfg.applicationDescription = app_desc

    # ── Well-known NodeIds ───────────────────────────────────────
    OBJECTS = types.NodeId(o6.ns.ns0.instances.objects)
    ORGANIZES = types.NodeId(o6.ns.ns0.reftypes.Organizes)
    HAS_COMPONENT = types.NodeId(o6.ns.ns0.reftypes.HasComponent)
    BASE_OBJECT = types.NodeId(o6.ns.ns0.objtypes.BaseObjectType)
    BASE_DATA_VAR = types.NodeId(o6.ns.ns0.vartypes.BaseDataVariableType)

    # ── Add an object node ───────────────────────────────────────
    obj_attr = types.ObjectAttributes()
    obj_attr.displayName = types.LocalizedText("MyDevice")
    obj_attr.description = types.LocalizedText("A sample device object")

    device_id = server.addObjectNode(
        types.NodeId("ns=1;i=100"),  # requested id
        OBJECTS,  # parent
        ORGANIZES,  # reference type
        types.QualifiedName("1:MyDevice"),  # browse name
        BASE_OBJECT,  # type definition
        obj_attr,
    )
    print(f"Added object node: {device_id}")

    # ── Add a Double variable ────────────────────────────────────
    var_attr = types.VariableAttributes()
    var_attr.displayName = types.LocalizedText("Temperature")
    var_attr.description = types.LocalizedText("Current temperature reading")
    var_attr.dataType = o6.NodeId(o6.Double)  # Double
    var_attr.valueRank = -1  # scalar
    var_attr.accessLevel = 3  # Read | Write
    var_attr.userAccessLevel = 3
    var_attr.value = types.Double(22.5)

    temp_id = server.addVariableNode(
        types.NodeId("ns=1;i=1001"),
        device_id,
        HAS_COMPONENT,
        types.QualifiedName("1:Temperature"),
        BASE_DATA_VAR,
        var_attr,
    )
    print(f"Added variable node: {temp_id}")

    # ── Add an Int32 variable ────────────────────────────────────
    counter_attr = types.VariableAttributes()
    counter_attr.displayName = types.LocalizedText("Counter")
    counter_attr.description = types.LocalizedText("Cycle counter")
    counter_attr.dataType = o6.NodeId(o6.Int32)  # Int32
    counter_attr.valueRank = -1
    counter_attr.accessLevel = 1  # Read-only
    counter_attr.userAccessLevel = 1
    counter_attr.value = types.Int32(0)

    counter_id = server.addVariableNode(
        types.NodeId("ns=1;i=1002"),
        device_id,
        HAS_COMPONENT,
        types.QualifiedName("1:Counter"),
        BASE_DATA_VAR,
        counter_attr,
    )
    print(f"Added variable node: {counter_id}")

    # ── Add a method node ────────────────────────────────────────
    def add_numbers(a, b):
        print(f"  [Method] Add({a}, {b}) = {a + b}")
        return [a + b]

    method_attr = types.MethodAttributes()
    method_attr.displayName = types.LocalizedText("Add")
    method_attr.description = types.LocalizedText("Add two doubles")
    method_attr.executable = True
    method_attr.userExecutable = True

    input_a = types.Argument()
    input_a.name = "A"
    input_a.dataType = o6.NodeId(o6.Double)
    input_a.valueRank = -1
    input_a.description = types.LocalizedText("First operand")

    input_b = types.Argument()
    input_b.name = "B"
    input_b.dataType = o6.NodeId(o6.Double)
    input_b.valueRank = -1
    input_b.description = types.LocalizedText("Second operand")

    output_sum = types.Argument()
    output_sum.name = "Sum"
    output_sum.dataType = o6.NodeId(o6.Double)
    output_sum.valueRank = -1
    output_sum.description = types.LocalizedText("A + B")

    method_id = server.addMethodNode(
        types.NodeId("ns=1;i=2001"),
        device_id,
        HAS_COMPONENT,
        types.QualifiedName("1:Add"),
        method_attr,
        add_numbers,
        [input_a, input_b],
        [output_sum],
    )
    print(f"Added method node: {method_id}")

    # ── Run the server ───────────────────────────────────────────
    server.run_startup()
    print("\nServer running at opc.tcp://localhost:4840")
    print("Press Ctrl+C to stop.\n")

    async def _drive():
        cycle = 0
        try:
            while True:
                cycle += 1

                # Update values on the server side
                await server.write_value(temp_id, types.Double(22.5 + (cycle % 50) * 0.1))
                await server.write_value(counter_id, types.Int32(cycle))

                if cycle % 10 == 0:
                    temp_val = await server.read_value(temp_id)
                    counter_val = await server.read_value(counter_id)
                    print(f"  Cycle {cycle}: Temp={temp_val}, Counter={counter_val}")

                # Yield to asyncio so it can drive the server's network IO.
                await asyncio.sleep(0.1)
        except asyncio.CancelledError:
            pass

    try:
        loop.run_until_complete(_drive())
    except KeyboardInterrupt:
        print("\nShutting down…")
    finally:
        server.run_shutdown()
        print("Server stopped.")


if __name__ == "__main__":
    main()
