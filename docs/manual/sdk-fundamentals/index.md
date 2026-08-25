# o6\\Python SDK Fundamentals

OPC UA ships a fixed set of datatypes that every server and client must understand but also offers extensibility with custom types.

## Contents

| # | Section | What it covers |
|---|---|---|
| 1 | [Built-in types](builtin/primitive-types.md) | 25 types: primitives, `StatusCode`, container types, address/identity types. |
| 2 | [Namespaces in o6\\Python](namespace/namespace-mapping-in-o6.md) | How o6\\Python abstracts from manual namespace managing. |
| 3 | [Writing a Nodeset in Python](namespace/writing-nodesets-in-python.md) | Declaring datatypes, enums, VariableTypes and ObjectTypes without any XML. |
| 4 | [Implementing Object Behavior](namespace/implementing-object-behavior.md) | The implement pattern: Method calls and Variable read/write behind a declared type. |

How the specification itself describes types, namespaces and nodeset files is covered in [OPC UA Fundamentals](../opcua-fundamentals/index.md) — see [DataType](../opcua-fundamentals/datatype.md), [Namespace](../opcua-fundamentals/namespace.md) and [Nodeset Files & Companion Specs](../opcua-fundamentals/nodesets-and-companion-specs.md).

Datatypes, Object, Variables, References are all organized into [Namespaces](../opcua-fundamentals/namespace.md) and distributed through nodeset xml files. **o6\Python** registers nodesets (NS0, a companion spec, or a vendor nodeset loaded at runtime) in a process-global registry and is identified by a short name, index, and URI.
