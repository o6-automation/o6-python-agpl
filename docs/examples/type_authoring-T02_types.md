# Built-in Types

Type usage examples for the high-level o6 library.

Uses the OPC UA types of the ``o6`` package. Scalar wrappers live at
the top level (``o6.NodeId``, ``o6.Int32``, ...). NS0 struct and enum
types live under ``o6.ns.ns0.datatypes``.

## 1. NodeId creation
`o6.NodeId(...)` parses the standard OPC UA string notation:
`ns=<namespace-index>;s=<string-id>` or `ns=<namespace-index>;i=<numeric-id>`.
Without `ns=` the NodeId is in namespace 0.

```python
print("--- 1. NodeId Creation ---")

node1 = o6.NodeId("ns=1;s=Temperature")
print(f"String NodeId: {node1}")

node2 = o6.NodeId("ns=2;i=1234")
print(f"Numeric NodeId: {node2}")
```

## 2. Scalar type wrappers
Every OPC UA built-in scalar type has a wrapper at the top level of
`o6`: `o6.Int32`, `o6.Double`, `o6.String`, `o6.Boolean`, `o6.UInt32`,
`o6.Float`, and so on. A wrapper fixes the wire type. Use one where the
type cannot be inferred from a plain Python value: method arguments,
`DataValue.value`, and any place where the type would be ambiguous
(`int` could mean `Int32`, `Int64`, `UInt32`, ...).

```python
print("\n--- 2. Scalar Type Wrappers ---")

var1 = o6.Int32(42)
print(f"Int32: {var1}")

var2 = o6.Double(3.14159)
print(f"Double: {var2}")

var3 = o6.String("Hello World")
print(f"String: {var3}")

var4 = o6.Boolean(True)
print(f"Boolean: {var4}")

var5 = o6.UInt32(42)
print(f"UInt32: {var5}")

var6 = o6.Float(3.14)
print(f"Float: {var6}")
```

## 3. DataValue
A `DataValue` holds a value with its status code and timestamps. The
`Read` and `Write` services carry it on the wire. `.value` accepts any
scalar wrapper.

```python
print("\n--- 3. DataValue Creation ---")

dv1 = o6.DataValue()
dv1.value = o6.Double(25.5)
print(f"DataValue: {dv1}")
print(f"  value: {dv1.value}")
```

## 4. LocalizedText
A `LocalizedText` pairs a display string with an optional locale code.
Without a locale the field stays unset. Servers use `LocalizedText`
for DisplayName and Description attributes with translations.

```python
print("\n--- 4. Localized Text ---")

lt1 = o6.LocalizedText("Hello World")
print(f"LocalizedText: {lt1}")

lt2 = o6.LocalizedText("Hallo Welt", "de")
print(f"German locale: {lt2}")

lt3 = o6.LocalizedText("Bonjour le monde", "fr")
print(f"French locale: {lt3}")
```

## 5. QualifiedName
A `QualifiedName` is a BrowseName: a namespace index plus a name,
written `<index>:<name>`. `browse()` results and BrowseName attributes
use it. A `NodeId` identifies the node itself; a `QualifiedName` names
it within its parent.

```python
print("\n--- 5. Qualified Name ---")

qn1 = o6.QualifiedName("0:MyVariable")
print(f"Default namespace: {qn1}")

qn2 = o6.QualifiedName("1:Temperature")
print(f"Namespace 1: {qn2}")
```

## 6. Struct types
Standard structs (OPC UA DataTypes with fields) live under
`ns0.datatypes`, not at the `o6` top level. Set fields by attribute
after construction. Enum-typed fields (like `applicationType` below)
take a member of the matching `ns0.datatypes` enum.

```python
print("\n--- 6. OPC UA Struct Types ---")

app_desc = ns0.datatypes.ApplicationDescription()
app_desc.applicationUri = "urn:example:app"
app_desc.applicationName = o6.LocalizedText("My Application")
app_desc.applicationType = ns0.datatypes.ApplicationType.CLIENT
app_desc.productUri = "urn:example:product"
print(f"ApplicationDescription: {app_desc}")
print(f"  application_uri: {app_desc.applicationUri}")
print(f"  application_name: {app_desc.applicationName}")
print(f"  application_type: {app_desc.applicationType}")

read_val_id = ns0.datatypes.ReadValueId()
read_val_id.nodeId = o6.NodeId("ns=1;s=Temperature")
read_val_id.attributeId = o6.UInt32(13)  # Value attribute
print(f"\nReadValueId: {read_val_id}")
```

## 7. Discovering available types
`dir(ns0.datatypes)` lists every struct and enum type generated from
the OPC UA namespace-0 nodeset.

```python
    print("\n--- 7. Available Struct/Enum Types ---")

    type_names = sorted(
        [name for name in dir(ns0.datatypes) if not name.startswith("_") and name[0].isupper()]
    )
    print(f"Total available types: {len(type_names)}")
    print(f"First 20: {type_names[:20]}")

    print("\n=== Example completed ===")


if __name__ == "__main__":
    main()
```

## Source Code

Download [`T02_types.py`](type_authoring-T02_types/T02_types.py) to run it locally.
