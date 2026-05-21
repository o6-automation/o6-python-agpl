"""
Type usage examples for the high-level O6 library.

This example shows how to use the various OPC UA types provided by the _o6 C extension.
"""

from o6 import types


def main():
    """Main example function."""
    print("=== High-Level O6 Types Example ===\n")

    # Example 1: NodeId creation
    print("1. NodeId Creation")
    print("-" * 30)

    # Various ways to create NodeIds
    node1 = types.NodeId("ns=1;s=Temperature")
    print(f"String NodeId: {node1}")

    node2 = types.NodeId("ns=2;i=1234")
    print(f"Numeric NodeId: {node2}")

    # Example 2: Variant creation
    print("\n2. Variant Creation")
    print("-" * 30)

    # Typed variants using low-level wrappers
    var1 = types.Int32(42)
    print(f"Int32: {var1}")

    var2 = types.Double(3.14159)
    print(f"Double: {var2}")

    var3 = types.String("Hello World")
    print(f"String: {var3}")

    var4 = types.Boolean(True)
    print(f"Boolean: {var4}")

    # Creating typed values (used in DataValue and method calls)
    var5 = types.UInt32(42)
    print(f"UInt32: {var5}")

    var6 = types.Float(3.14)
    print(f"Float: {var6}")

    # Example 3: DataValue creation
    print("\n3. DataValue Creation")
    print("-" * 30)

    # Simple data value with a variant
    dv1 = types.DataValue(value=types.Double(25.5))
    print(f"DataValue: {dv1}")
    print(f"  value: {dv1.value}")

    # Example 4: Localized text
    print("\n4. Localized Text")
    print("-" * 30)

    lt1 = types.LocalizedText("Hello World")
    print(f"LocalizedText: {lt1}")

    lt2 = types.LocalizedText("Hallo Welt", "de")
    print(f"German locale: {lt2}")

    lt3 = types.LocalizedText("Bonjour le monde", "fr")
    print(f"French locale: {lt3}")

    # Example 5: Qualified name
    print("\n5. Qualified Name")
    print("-" * 30)

    qn1 = types.QualifiedName("0:MyVariable")
    print(f"Default namespace: {qn1}")

    qn2 = types.QualifiedName("1:Temperature")
    print(f"Namespace 1: {qn2}")

    # Example 6: Struct types
    print("\n6. OPC UA Struct Types")
    print("-" * 30)

    # ApplicationDescription
    app_desc = types.ApplicationDescription()
    app_desc.application_uri = "urn:example:app"
    app_desc.application_name = types.LocalizedText("My Application")
    app_desc.application_type = types.ApplicationType.CLIENT
    app_desc.product_uri = "urn:example:product"
    print(f"ApplicationDescription: {app_desc}")
    print(f"  application_uri: {app_desc.application_uri}")
    print(f"  application_name: {app_desc.application_name}")
    print(f"  application_type: {app_desc.application_type}")

    # ReadValueId
    read_val_id = types.ReadValueId()
    read_val_id.nodeid = types.NodeId("ns=1;s=Temperature")
    read_val_id.attribute_id = types.UInt32(13)  # Value attribute
    print(f"\nReadValueId: {read_val_id}")

    # Example 7: Inspecting available types
    print("\n7. Available Struct/Enum Types")
    print("-" * 30)

    # Show some available types in the types module
    type_names = sorted(
        [name for name in dir(types) if not name.startswith("_") and name[0].isupper()]
    )
    print(f"Total available types: {len(type_names)}")
    print(f"First 20: {type_names[:20]}")

    print("\n=== Types example completed ===")


if __name__ == "__main__":
    main()
