# Types Example

Source example: `examples/highlevel/types_example.py`

This example lists some of the high-level types defined in `o6.types`.

## Explanation

### `NodeId`

```python
node1 = types.NodeId("ns=1;s=Temperature")
node2 = types.NodeId("ns=2;i=1234")
```

### Basic Types


```python
var1 = types.Int32(42)
var2 = types.Double(3.14159)
var3 = types.String("Hello World")
var4 = types.Boolean(True)
var5 = types.UInt32(42)
var6 = types.Float(3.14)
```

### Structured OPC UA values

```python
dv1 = types.DataValue(value=types.Double(25.5))
lt1 = types.LocalizedText("Hello World")
qn1 = types.QualifiedName("0:MyVariable")
```


## Full source

```python
from o6 import types


def main():
    print("=== High-Level O6 Types Example ===\n")

    print("1. NodeId Creation")
    print("-" * 30)

    node1 = types.NodeId("ns=1;s=Temperature")
    print(f"String NodeId: {node1}")

    node2 = types.NodeId("ns=2;i=1234")
    print(f"Numeric NodeId: {node2}")

    print("\n2. Variant Creation")
    print("-" * 30)

    var1 = types.Int32(42)
    print(f"Int32: {var1}")

    var2 = types.Double(3.14159)
    print(f"Double: {var2}")

    var3 = types.String("Hello World")
    print(f"String: {var3}")

    var4 = types.Boolean(True)
    print(f"Boolean: {var4}")

    var5 = types.UInt32(42)
    print(f"UInt32: {var5}")

    var6 = types.Float(3.14)
    print(f"Float: {var6}")

    print("\n3. DataValue Creation")
    print("-" * 30)

    dv1 = types.DataValue(value=types.Double(25.5))
    print(f"DataValue: {dv1}")
    print(f"  value: {dv1.value}")

    print("\n4. Localized Text")
    print("-" * 30)

    lt1 = types.LocalizedText("Hello World")
    print(f"LocalizedText: {lt1}")

    lt2 = types.LocalizedText("Hallo Welt", "de")
    print(f"German locale: {lt2}")

    lt3 = types.LocalizedText("Bonjour le monde", "fr")
    print(f"French locale: {lt3}")

    print("\n5. Qualified Name")
    print("-" * 30)

    qn1 = types.QualifiedName("0:MyVariable")
    print(f"Default namespace: {qn1}")

    qn2 = types.QualifiedName("1:Temperature")
    print(f"Namespace 1: {qn2}")

    print("\n6. OPC UA Struct Types")
    print("-" * 30)

    app_desc = types.ApplicationDescription()
    app_desc.application_uri = "urn:example:app"
    app_desc.application_name = types.LocalizedText("My Application")
    app_desc.application_type = types.ApplicationType.Client
    app_desc.product_uri = "urn:example:product"
    print(f"ApplicationDescription: {app_desc}")
    print(f"  application_uri: {app_desc.application_uri}")
    print(f"  application_name: {app_desc.application_name}")
    print(f"  application_type: {app_desc.application_type}")

    read_val_id = types.ReadValueId()
    read_val_id.nodeid = types.NodeId("ns=1;s=Temperature")
    read_val_id.attribute_id = types.UInt32(13)
    print(f"\nReadValueId: {read_val_id}")

    print("\n7. Available Struct/Enum Types")
    print("-" * 30)

    type_names = sorted(
        [name for name in dir(types) if not name.startswith("_") and name[0].isupper()]
    )
    print(f"Total available types: {len(type_names)}")
    print(f"First 20: {type_names[:20]}")

    print("\n=== Types example completed ===")


if __name__ == "__main__":
    main()
```