# DataType

!!! info
    This section will explain basics about DataTypes in the OPC UA specification. If you are already familiar with the topic you may skip to [namespace](namespace.md) or [Namespace Mapping in o6\\Python](../namespace/namespace-mapping-in-o6.md)

A `DataType` is the central extensibility point of the OPC UA type system.
Every value that travels on the wire — a single `Int32`, a `DateTime`, a full
`ReadResponse`, or a vendor-specific `MachineStatus` — is represented by a
`DataType`.

`DataType` is itself a node in the address space, identified by a `NodeId` and
referenced from `Variable`, `Object`, `Method` and `ReferenceType` as **their
type definition**.

## What this page covers

This page is a short summary of the most important concepts and is not a complete reference, yet we follow the structure of the OPC UA spec's normative
[Part 3, §5.8 — DataTypes](https://reference.opcfoundation.org/Core/Part3/v105/docs/5.8):

1. **DataType Model** — how `Variable`s point to `DataType` nodes, and how structured types point to their `DataTypeEncoding` objects.
2. **Encoding Rules per kind** — the five flavors (Built-in, Simple, Structured, Enumeration, OptionSet) and how each is encoded on the wire.
3. **DataType NodeClass** — the attributes, references, and properties that make up a `DataType` node.

Everything else in *Types & Address Space* — built-in scalars, status codes,
namespaces, custom types — assumes you understand these four pieces.

The four subsections below mirror §5.8.1 – §5.8.4 in order and reuse the same
diagrams and NodeIds throughout.

---

## DataType Model (§5.8.1)

A `DataType` is a node, like any other node in OPC UA. That means it has:

- a `NodeId` (e.g. `i=6` for `Int32`, `ns=1;s=MachineStatus` for a vendor type),
- a `BrowseName` (e.g. `Int32`, `MachineStatus`),
- a set of *attributes* (the data type's own properties, see below),
- references to and from other nodes.

What is specific to a `DataType` is *how* other nodes point to it — this is the **DataType Model** defined in the spec [Part 3, §5.8.1](https://reference.opcfoundation.org/Core/Part3/v105/docs/5.8.1).

```
   ┌─────────────────────────┐                          ┌────────────────────────┐
   │  VariableType           │                          │  Variable (instance)   │
   │  e.g. AnalogItemType    │                          │  e.g. "Temperature"    │
   │  ─────────────────────  │                          │  ────────────────────  │
   │  HasTypeDefinition   ───┼────┐                 ┌───┼─ HasTypeDefinition     │
   └─────────────────────────┘    │                 │   └────────────────────────┘
                                  ▼                 ▼
                  ┌─────────────────────────────────────────────────┐
                  │  DataType  (e.g. Double, ns=0;i=11)             │
                  │  ─────────────────────────────────────────────  │
                  │  HasEncoding ──► DataTypeEncoding Object        │
                  │                  (BrowseName "Default Binary")  │
                  └─────────────────────────────────────────────────┘
```

Every `Variable` and `VariableType` carries a `DataType` attribute that points (via the standard `HasTypeDefinition` reference) at the same `DataType` node.
The `DataType` is *referenced from* both nodes.

```
       ┌──────────────────────────────────────────────────────┐
       │  DataType  (Structured, e.g. Argument, ns=0;i=296)   │
       └───────────┬──────────────────────┬───────────────────┘
                   │                      │
                   │ HasEncoding          │ HasEncoding
                   ▼                      ▼
       ┌──────────────────────┐   ┌──────────────────────┐
       │  DataTypeEncoding    │   │  DataTypeEncoding    │
       │  BrowseName:         │   │  BrowseName:         │
       │  "Default Binary"    │   │  "Default XML"       │
       └──────────────────────┘   └──────────────────────┘
```


A concrete Structured `DataType` points via `HasEncoding` at one or more `DataTypeEncoding` Objects (typically `Default Binary` and `Default XML`, both in `ns=0`). Each `DataTypeEncoding` is owned by *exactly one* `DataType`.
It is the `NodeId` of the `DataTypeEncoding` — **not** the `DataType` — that travels on the wire inside an `ExtensionObject` as the `TypeId`.

### Physical encoding of a structured value

The figures above are address-space diagrams.
The same identity also travels on the wire, attached to every structured value as a `TypeId` inside the `ExtensionObject` envelope.
Concrete example — the body of a `ReadRequest` message:

```
Wire value  ──────────────────────────────────────────────────

    ReadRequest
    ├── TypeId  =  i=631             ← DataType of the *request* itself
    ├── Body
    │   ├── NodesToRead[0]
    │   │   ├── NodeId    = i=2255   ← identifies the *variable* we read
    │   │   ├── Attribute = UInt32   ← field of ReadRequest,
    │   │   │                          DataType = UInt32  (i=7)
    │   │   └── ...
    │   └── ...
```

`TypeId = i=631` says: *the body that follows is a `ReadRequest`* — and both peers agree on what that means because `i=631` resolves to a well-known `DataType` (and, via its `HasEncoding`, to a known `DataTypeEncoding`).

---

## Encoding Rules per Kind

The OPC UA spec defines five concrete `DataType` kinds, plus an *abstract*
kind. Each kind dictates both **what the `DataType` node carries in its body**
and **how an instance of that kind appears on the wire** —
[Part 3, §5.8.2](https://reference.opcfoundation.org/Core/Part3/v105/docs/5.8.2)
is normative here.

```
     ┌────────────────────────────────────────────────────────────────┐
     │  BaseDataType  (i=24, abstract — never instantiated)           │
     └────────────┬───────────────────┬────────────────────┬──────────┘
                  │                   │                    │
                  ▼                   ▼                    ▼
   ┌────────────────────┐   ┌────────────────────┐   ┌────────────────────┐
   │  Built-in          │   │  Structure         │   │  Enumeration       │
   │  (i=1 … i=25)      │   │  (i=22)            │   │  (i=29)            │
   │  ──────────────    │   │  ──────────────    │   │  ──────────────    │
   │  No body, native   │   │  StructureDef      │   │  EnumDefinition    │
   │  wire encoding     │   │  ExtensionObject   │   │  Int32 on the wire │
   │  e.g. Int32 i=6    │   │  e.g. ReadRequest  │   │  e.g. ServerState  │
   └──────────────┬─────┘   └─────────┬──────────┘   └─────┬──────────────┘
                  │                   │                    │
                  │ HasSubtype        │ HasSubtype         │ HasSubtype
                  ▼                   ▼                    ▼
   ┌────────────────────┐   ┌────────────────────┐   ┌────────────────────┐
   │  Simple            │   │  Structured types  │   │  OptionSet         │
   │  (e.g. Duration)   │   │  (Argument,        │   │  (i=12755) or      │
   │  wire-encodes like │   │   vendor structs)  │   │  UInteger subtype  │
   │  parent Built-in   │   │                    │   │  bit mask on wire  │
   └────────────────────┘   └────────────────────┘   └────────────────────┘
```

**Read the boxes left-to-right:** Built-ins are fixed by the spec and have
empty bodies; Structured types carry a `StructureDefinition` and travel as
`ExtensionObject`s tagged with a `DataTypeEncoding` `TypeId`; Enumerations
travel as a plain `Int32` with the symbol table living only in the node.

## DataType NodeClass

The `DataType` NodeClass describes the syntax of a `Variable` value. A
`DataType` node inherits the Base NodeClass attributes (`NodeId`, `BrowseName`,
…) and adds `IsAbstract`, a `DataTypeDefinition` body (mandatory for
Structured / Enumeration / OptionSet, absent for Built-ins), plus three
reference targets: `HasSubtype`, `HasEncoding` (Structured only), and
`HasProperty` (for `NodeVersion`, `EnumStrings`, `OptionSetValues`, …).

For Structured types, `DataTypeDefinition` is a `StructureDefinition` —
ordered list of fields, each with name, `DataType`, value-rank, and
optionality. Example, the layout of `ReadRequest` (i=631):

```
StructureDefinition  (DataTypeDefinition attribute, i.e. DataType NodeClass)
│
├── defaultEncodingId   →  NodeId of the Default Binary encoding object
├── baseDataType        →  Structure (i=22)
├── structureType       →  Structure | StructureWithOptionalFields | Union
└── fields[]            ─ ordered list
      │
      ├── [0]  name="requestHeader"   dataType=RequestHeader (ns=0;i=389)
      │        valueRank=-1 (scalar)  isOptional=false
      ├── [1]  name="maxAge"          dataType=Double         (ns=0;i=11)
      │        valueRank=-1           isOptional=false
      ├── [2]  name="timestampsToReturn"  dataType=TimestampsToReturn (ns=0;i=396)
      │        valueRank=-1           isOptional=false
      └── [3]  name="nodesToRead"     dataType=Argument       (ns=0;i=296)
               valueRank=1 (array)    isOptional=false
```

In o6\\Python a Structured `DataType` shows up as a plain Python class with
typed attributes — see [Loading & Using Nodesets](../namespace/loading-and-using-nodesets.md)
for how this is wired up. The class layout mirrors the field list one-to-one.

---

## Where DataType definitions come from

`DataType`s are **not invented by o6\Python**. They are shipped by:

1. **The OPC UA specification itself** — every Built-in type (i=1 … i=25) and
   every standard Structured/Enumeration type (e.g. `ReadRequest` i=631,
   `Argument` i=296) lives in `ns=0`. These are loaded from the
   `Opc.Ua.NodeSet2.xml` companion file that ships with every conformant
   stack.
2. **Companion specifications** published by the OPC Foundation or industry
   bodies — DI, ISA-95, FDI, … — each in its own namespace.
3. **Vendor-specific nodesets** — anyone can publish a `*.NodeSet2.xml` and
   compile it into an importable namespace.


The [next section](namespace.md) covers this in more detail.

**o6\Python consumes these nodesets** (see [`_nodeset_parser.py`](https://github.com/o6-automation/o6-python-agpl/blob/main/o6/_nodeset_parser.py))
and makes their content available as Python classes and as run-time metadata
on the corresponding nodes. The spec defines both the old (`<DataTypeDefinition>`,
v1.03) and the modern (`<StructureDefinition>` / `<EnumDefinition>` /
`<UnionDefinition>`, v1.04+) XML representations; o6 handles all of them.

```
                             NodeSet2.xml
                                 │
                                 ▼
                       ┌────────────────────┐
                       │  _nodeset_parser   │
                       └─────────┬──────────┘
                                 │  Namespace descriptor
                  ┌──────────────┼─────────────────────┐
                  ▼              ▼                     ▼
             UA_NodeIds     Python classes     Type-registration table
             (build-time)   (build-time)      (runtime decode/encode)
```

---

## See also

- The OPC UA spec's normative treatment of `DataType`:
  [Part 3, §5.8 — DataTypes](https://reference.opcfoundation.org/Core/Part3/v105/docs/5.8).
- Wire encoding rules per kind:
  [Part 6, §5.1.2 — Built-in Types](https://reference.opcfoundation.org/Core/Part6/v105/docs/5.1.2).
- How o6 exposes these as Python types:
  [Built-in Types](../builtin/primitive-types.md) and [Loading & Using Nodesets](../namespace/loading-and-using-nodesets.md).

