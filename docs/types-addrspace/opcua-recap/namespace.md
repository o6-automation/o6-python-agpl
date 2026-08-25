# Namespace

!!! info
    This section will explain basics about Namespaces in the OPC UA specification. If you are already familiar with the topic you may skip to how o6\\Python handles Namespaces: [Nodeset Files & Companion Specs](nodesets-and-companion-specs.md) or [Namespace Mapping in o6\\Python](../namespace/namespace-mapping-in-o6.md).

A `Namespace` is how OPC UA keeps the nodes of unrelated vendors and standards bodies from colliding in a single server's address space.
It is the partition of the address space under one owning authority — every `Node`, `Reference`, `DataType`, `ObjectType` and `Method` belongs to exactly one namespace, identified by a **namespace URI** the owner chooses.
On the wire the URI is replaced by a server-local **namespace index**, a 16‑bit integer the server assigns when it loads the namespace; the URI is the stable identity, the index is just a slot in the encoding.

## What this page covers

This page is a short summary of the most important concepts and is not a complete reference, yet we follow the structure of the OPC UA spec's normative [Part 3, §4](https://reference.opcfoundation.org/Core/Part3/v105/docs/4) `AddressSpace` concepts:

1. **URI vs index** — what is stable, what is server-local, and how they map.
2. **The Namespace array** — how a server publishes the URI ↔ index mapping to clients.
3. **`ns0` is special** — why namespace 0 is fixed and what it carries.
4. **`ns1` is special too** — why the server-local namespace sits at index 1.

The four subsections below mirror [Part 3, §4.2](https://reference.opcfoundation.org/Core/Part3/v105/docs/4.2) / [Part 3, §4.4](https://reference.opcfoundation.org/Core/Part3/v105/docs/4.4) in order and reuse the same terminology throughout.

---

## URI vs index

A namespace is identified on the wire and in any stored representation by its **index**, but the index is *meaningful only inside one server*.
The **URI** is what gives the namespace a stable, globally unique identity:

```
            URI                          index
             │                             │
             ▼                             ▼
 http://opcfoundation.org/UA/        ──►   0      (always, on every server)
 http://opcfoundation.org/UA/DI/     ──►   2      (server A)
 http://opcfoundation.org/UA/DI/     ──►   3      (server B)
```

Two clients talking to two different servers will see the same URI sitting at *different* indices, and that is fine — every server publishes its URI ↔ index table to clients during session setup, and clients use that table to resolve `NodeId`s.
As the spec puts it, *"Programs shall always treat URIs as opaque strings that can only be tested for equality with a case sensitive string comparison"* ([Part 3, §4.2](https://reference.opcfoundation.org/Core/Part3/v105/docs/4.2)).

---

## The Namespace array

Every server exposes a single server-side **Namespace array**: an ordered list of URI strings that defines the URI ↔ index mapping for that server.
Clients fetch it as the `NamespaceArray` variable during discovery and session creation.

```
Client                                          Server
   │                                               │
   │  ── CreateSession ───────────────────────►    │
   │                                               │
   │  ◄── NamespaceArray = [                       │
   │         "http://opcfoundation.org/UA/",       │  index 0
   │         "urn:mycompany:machine:1.0",          │  index 1
   │         "http://opcfoundation.org/UA/DI/",    │  index 2
   │       ] ─────────────────────────────────     │
   │                                               │
   │  all subsequent NodeIds carry an index        │
   │  into this array                              │
```

Two important details:

- The server is free to **add, remove or reorder** entries as it loads nodesets at startup, but the **URI** at index `0` is always `http://opcfoundation.org/UA/` and index `0` is always that URI.
- A client that receives a `NodeId` with a URI it doesn't recognise (e.g. `nsu=...` form, see below) can still resolve the node against its own copy of the namespace table — URIs are portable across servers.

For the exact contract, see server namespace array in
[Part 5, §8.5](https://reference.opcfoundation.org/Core/Part5/v105/docs/8.5)
and the discovery / session services in
[Part 4, §5.7.2](https://reference.opcfoundation.org/Core/Part4/v105/docs/5.7.2).

---

## `ns0` is special

Namespace 0 — URI `http://opcfoundation.org/UA/` — is the namespace defined by the OPC UA specification itself.
Every server is required to expose it, and its index is **always `0`** on every server, regardless of when the server starts or which nodesets it loads.
It carries the service envelopes, filter and query operands, metadata structures, and standard enums the protocol is built on.

In o6\\Python, `ns0` is pre-generated and shipped with the library, and its content may be accessed using `o6.ns.ns0`:

````python
req = o6.ns.ns0.datatypes.ReadRequest()
o6.ns.ns0.datatypes.NodeId          # the NodeId DataType, i=17
o6.ns.ns0.datatypes.ExpandedNodeId  # the ExpandedNodeId DataType, i=18
o6.ns.ns0.datatypes.ReadRequest     # the ReadRequest DataType, i=629
````

---

## `ns1` is special too

Namespace `1` is the **server-local namespace**: the namespace in which a server publishes its own types, its own instance layout, and any nodes it adds at runtime.

- **The index is reserved.** Per [Part 5, §6.3.1](https://reference.opcfoundation.org/Core/Part5/v105/docs/6.3.1), index `1` is the local Server, just as index `0` is the OPC UA namespace. Clients can rely on that slot referring to "this server" regardless of which URI it carries.
- **The URI is the server's `ApplicationUri`.** The same section requires the URI at `ns=1` to be the server's own `ApplicationUri`.
- **It holds the server's own nodes.** The ServerType instance and its mandatory Properties (`ServerArray`, `NamespaceArray`, `ServerStatus`, `ServerCapabilities`, `ServerRedundancy`) live here, together with any vendor types and runtime-added nodes. None of this is portable across servers.

---

## Everything else: nodesets

Every namespace after `ns0` and `ns1` — i.e. every namespace at index `2`, `3`, … — comes from a **nodeset**: a self-contained XML description of a slice of address space. Keep reading [Nodesets and Companion Specs](nodesets-and-companion-specs.md) for more details.

---

## See also

- The OPC UA spec's normative treatment of namespaces and URIs:
  [Part 3, §4.2 — URIs](https://reference.opcfoundation.org/Core/Part3/v105/docs/4.2)
  and [Part 3, §4.4 — Node Model](https://reference.opcfoundation.org/Core/Part3/v105/docs/4.4).
- How the server publishes its URI ↔ index table to clients:
  [Part 5, §8.5 — Server Array and Namespace Array](https://reference.opcfoundation.org/Core/Part5/v105/docs/8.5).
- How o6 exposes and resolves namespaces from Python:
  [Address & Identity Types](../builtin/address-types.md),
  [Namespace Mapping in o6\\Python](../namespace/namespace-mapping-in-o6.md),
  [Loading & Using Nodesets](../namespace/loading-and-using-nodesets.md),
  and [Nodesets and Companion Specs](nodesets-and-companion-specs.md).
