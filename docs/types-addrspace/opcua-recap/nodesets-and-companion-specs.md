# Nodeset Files & Companion Specs

!!! info
    This section will explain basics about nodeset files and companion specs and what their purpose is in the OPC UA ecosystem. If you are already familiar with the topic you may skip to [Namespace Mapping in o6\\Python](../namespace/namespace-mapping-in-o6.md).

A **Nodeset** is the OPC UA standard's way of packaging a slice of the address space into a portable XML file.
Nodesets are how vendors ship their type systems, how industry consortia ship domain models (DI, ISA‑95, motion control, machine vision, …), and how the spec itself distributes the hundreds of `ns=0` types you see on every server.

A **Companion Specification** is the published document that defines such a nodeset — together with its semantics, scope and versioning rules — so other vendors can implement against it.
Every companion spec is published as one or more nodeset files.
A nodeset without a published spec behind it is just a vendor's private information model.

## What this page covers

This page is a short summary of the most important concepts and is not a complete reference, yet we follow the structure of the OPC UA spec's
[Part 6, Annex F](https://reference.opcfoundation.org/Core/Part6/v105/docs/F):

1. **What a nodeset is** — the file format's role in the address space.
2. **Companion specs** — what they are and how they relate to nodesets.

---

## What a nodeset is

A nodeset is an XML document, conforming to the `UANodeSet` schema, that lists the nodes a server should materialise when the file is loaded.
It is *self-contained* in the sense that it carries everything needed to recreate the slice of address space it describes — the namespace URI it belongs to, the nodes themselves, and the references between them — but it is *not standalone*: the nodes it defines typically extend types from another nodeset, almost always `ns=0`, and the same identifiers must resolve to the same NodeIds once loaded.

A nodeset declares which other nodesets it builds on with a `<RequiredModel>` block. From the actual headers in [`OPCFoundation/UA-Nodeset`](https://github.com/OPCFoundation/UA-Nodeset), the dependency graph between a handful of representative companion specs looks like this:

```
   ┌──────┐
   │ AMB  │
   └──┬───┘
      ▼
   ┌──────┐     ┌──────┐     ┌──────┐
   │  UA  │◄─── │  DI  │◄─── │  IA  │
   └──────┘     └──────┘     └──────┘
```

The arrow reads as "depends on".
Layers are real, not decorative - A server that supports `IA` needs every node from `DI` as well.

Two practical properties to keep in mind:

- **Loading is additive.** A nodeset does not replace anything in the address space; it adds nodes under the namespace URI it declares. A server can load many nodesets, and a client sees them all merged into one graph.
- **Nodesets are textual.** They are not the binary protocol representation — for that, OPC UA defines [binary](https://reference.opcfoundation.org/Core/Part6/v105/docs/5.2), [XML](https://reference.opcfoundation.org/Core/Part6/v105/docs/5.3) and [JSON](https://reference.opcfoundation.org/Core/Part6/v105/docs/5.4) wire encodings. The nodeset is a *source* format that any server can parse at startup.

---

## Anatomy of a nodeset

A nodeset is an XML file whose root element is `UANodeSet`. The full XML schema is in the OPC UA spec's
[Part 6, Annex F — Information Model XML Schema](https://reference.opcfoundation.org/Core/Part6/v105/docs/F), and the versioned XSDs live in
[`OPCFoundation/UA-Nodeset`](https://github.com/OPCFoundation/UA-Nodeset). For the rest of this page that is all the reader needs to know.

---

## Companion specs

A **Companion Specification** is the human-readable document an organisation publishes alongside its nodeset: it gives the nodeset *meaning* — what the types represent, what semantics methods have, what rules a client can rely on — and a stable place to put version notes and conformance claims. Without it, the nodeset is just XML.

The OPC UA ecosystem groups companion specs into three rough categories:

- **Foundation companion specs**, published by the OPC Foundation itself alongside the core spec — e.g. the [DI](https://opcfoundation.org/about/opc-partners/opc-unified-architecture/opc-ua-companion-specifications/), [ISA‑95](https://opcfoundation.org/about/opc-partners/opc-unified-architecture/opc-ua-companion-specifications/), [FDI](https://opcfoundation.org/about/opc-partners/opc-unified-architecture/opc-ua-companion-specifications/), [Pub/Sub](https://opcfoundation.org/about/opc-partners/opc-unified-architecture/opc-ua-companion-specifications/) specs. These ship from the same `UA-Nodeset` repo as `Opc.Ua.<Name>.NodeSet2.xml` files.
- **Field‑level / domain companion specs**, published by industry consortia — e.g. [Weihenstephan](https://opcfoundation.org/about/opc-partners/opc-unified-architecture/opc-ua-companion-specifications/), [VDMA](https://opcfoundation.org/about/opc-partners/opc-unified-architecture/opc-ua-companion-specifications/), [AutomationML](https://opcfoundation.org/about/opc-partners/opc-unified-architecture/opc-ua-companion-specifications/). Each typically extends a foundation spec.
- **Vendor-specific information models**, not published as companion specs but packaged as the vendor's own nodeset. Useful for one vendor's product line; not portable across vendors.

The relationship is straightforward:

```
companion spec document                nodeset XML file
        │                                    │
        │  defines semantics,                │  defines nodes,
        │  conformance, version              │  references,
        │                                    │  namespace URI
        └─────────────┬──────────────────────┘
                      │
                      ▼
            a server loads the file,
            publishes the namespace under
            its assigned index
```

When a server advertises support for a companion spec, what it is really saying is *I have loaded the corresponding nodeset(s) under my assigned index(es), and the behaviour of those nodes matches the spec's documented semantics*. Clients confirm this by reading the server's `NamespaceArray` and looking up the URI(s) the spec defines.

The list of officially released companion specs is maintained on the [OPC Foundation website](https://opcfoundation.org/about/opc-partners/opc-unified-architecture/opc-ua-companion-specifications/); their nodeset files live in [`OPCFoundation/UA-Nodeset`](https://github.com/OPCFoundation/UA-Nodeset), one directory per spec, one `*.NodeSet2.xml` per major release.

---

## See also

- The OPC UA spec's normative treatment of the nodeset format:
  [Part 6, Annex F — Information Model XML Schema](https://reference.opcfoundation.org/Core/Part6/v105/docs/F).
- The XML schemas themselves, versioned alongside the spec:
  [`OPCFoundation/UA-Nodeset`](https://github.com/OPCFoundation/UA-Nodeset).
- Where URI ↔ index is defined and how namespaces get loaded at startup:
  [Namespace](namespace.md),
  [Part 5, §6.3.1 — ServerType](https://reference.opcfoundation.org/Core/Part5/v105/docs/6.3.1).
- The list of officially released companion specs:
  [OPC UA Companion Specifications](https://opcfoundation.org/about/opc-partners/opc-unified-architecture/opc-ua-companion-specifications/).
- How o6 loads nodesets and turns them into Python classes:
  [Namespace Mapping in o6\\Python](../namespace/namespace-mapping-in-o6.md).

