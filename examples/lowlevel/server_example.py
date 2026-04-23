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

import time
from o6 import _o6
import o6
from o6._o6 import types


def main():
    # ── Create and configure ─────────────────────────────────────
    server = _o6.Server(port=4840)

    cfg = server.config
    cfg.application_uri = "urn:example:lowlevel-server"

    app_desc = types.ApplicationDescription()
    app_desc.application_uri = "urn:example:lowlevel-server"
    app_desc.application_name = types.LocalizedText("Low-level Example Server")
    app_desc.application_type = types.ApplicationType.SERVER
    app_desc.product_uri = "urn:example:product"
    cfg.application_description = app_desc

    # ── Well-known NodeIds ───────────────────────────────────────
    OBJECTS = types.NodeId(o6.ns.ns0.objects.Root.Objects())
    ORGANIZES = types.NodeId(
        o6.ns.ns0.reftypes.References.HierarchicalReferences.Organizes()
    )
    HAS_COMPONENT = types.NodeId(
        o6.ns.ns0.reftypes.References.HierarchicalReferences.HasChild.Aggregates.HasComponent()
    )
    BASE_OBJECT = types.NodeId(o6.ns.ns0.objtypes.BaseObjectType())
    BASE_DATA_VAR = types.NodeId(
        o6.ns.ns0.vartypes.BaseVariableType.BaseDataVariableType()
    )

    # ── Add an object node ───────────────────────────────────────
    obj_attr = types.ObjectAttributes()
    obj_attr.display_name = types.LocalizedText("MyDevice")
    obj_attr.description = types.LocalizedText("A sample device object")

    device_id = server.add_object_node(
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
    var_attr.display_name = types.LocalizedText("Temperature")
    var_attr.description = types.LocalizedText("Current temperature reading")
    var_attr.data_type = types.NodeId(
        o6.ns.ns0.datatypes.BaseDataType.Number.Double()
    )  # Double
    var_attr.value_rank = -1  # scalar
    var_attr.access_level = 3  # Read | Write
    var_attr.user_access_level = 3
    var_attr.value = types.Double(22.5)

    temp_id = server.add_variable_node(
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
    counter_attr.display_name = types.LocalizedText("Counter")
    counter_attr.description = types.LocalizedText("Cycle counter")
    counter_attr.data_type = types.NodeId(
        o6.ns.ns0.datatypes.BaseDataType.Number.Integer.Int32()
    )  # Int32
    counter_attr.value_rank = -1
    counter_attr.access_level = 1  # Read-only
    counter_attr.user_access_level = 1
    counter_attr.value = types.Int32(0)

    counter_id = server.add_variable_node(
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
    method_attr.display_name = types.LocalizedText("Add")
    method_attr.description = types.LocalizedText("Add two doubles")
    method_attr.executable = True
    method_attr.user_executable = True

    input_a = types.Argument()
    input_a.name = "A"
    input_a.data_type = types.NodeId(o6.ns.ns0.datatypes.BaseDataType.Number.Double())
    input_a.value_rank = -1
    input_a.description = types.LocalizedText("First operand")

    input_b = types.Argument()
    input_b.name = "B"
    input_b.data_type = types.NodeId(o6.ns.ns0.datatypes.BaseDataType.Number.Double())
    input_b.value_rank = -1
    input_b.description = types.LocalizedText("Second operand")

    output_sum = types.Argument()
    output_sum.name = "Sum"
    output_sum.data_type = types.NodeId(
        o6.ns.ns0.datatypes.BaseDataType.Number.Double()
    )
    output_sum.value_rank = -1
    output_sum.description = types.LocalizedText("A + B")

    method_id = server.add_method_node(
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

    try:
        cycle = 0
        while True:
            cycle += 1

            # Update values on the server side
            server.write_value(temp_id, types.Double(22.5 + (cycle % 50) * 0.1))
            server.write_value(counter_id, types.Int32(cycle))

            if cycle % 10 == 0:
                temp_val = server.read_value(temp_id)
                counter_val = server.read_value(counter_id)
                print(f"  Cycle {cycle}: Temp={temp_val}, Counter={counter_val}")

            # Process network events (blocking for ~100 ms)
            server.run_iterate(True)

    except KeyboardInterrupt:
        print("\nShutting down…")
    finally:
        server.run_shutdown()
        print("Server stopped.")


if __name__ == "__main__":
    main()
