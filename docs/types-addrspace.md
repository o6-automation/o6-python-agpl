# Types & Address Space

OPC UA ships a fixed set of datatypes that every server and client must understand but also offers extensibility with custom types. In this chapter:

- [Built-in types](types-addrspace/builtin/primitive-types.md) — 25 types: primitives, `StatusCode`, container types, address/identity types.
- [OPC UA DataType and Namespace Recap](types-addrspace/opcua-recap/datatype.md) — Quick introduction in how types and namespaces are described by the specification
- [Namespaces in o6\\Python](types-addrspace/namespace/namespace-mapping-in-o6.md) — How o6\\Python abstracts from manual namespace managing

Datatypes, Object, Variables, References are all organized into [Namespaces](types-addrspace/opcua-recap/datatype.md) and distributed through nodeset xml files. **o6\Python** registers nodesets (NS0, a companion spec, or a vendor nodeset loaded at runtime) in a process-global registry and is identified by a short name, index, and URI.
