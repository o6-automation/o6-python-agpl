# NodeIds and namespace info

Every OPC UA node is identified by a `NodeId`. `o6.NodeId` accepts the standard `i=`, `s=`, and `g=` identifier forms. It also accepts `ns=<shortname>;...` for a registered shortname and `nsu=<full-uri>;...` for a full namespace URI.

A `NodeId` is really two things glued together: a **namespace** (which *authority* the identifier belongs to) and an **identifier** (the actual `i=...`, `s=...`, or `g=...` value inside that namespace). The same identifier string — `i=2253` — means the same thing on every server, because it's defined in **`ns0`**, the OPC UA namespace that the spec itself defines. An identifier like `i=1302` means different things on different servers, because that one belongs to the *server-local* namespace (`ns=1`), which carries the distillery's own nodes. The namespace is what gives the identifier its stable meaning across servers; the integer index is just a server-local slot.

This page walks through three steps:

1. Build a `NodeId` in any of the supported string forms.
2. Read namespace info (URI, version, index, …) off any `NodeId`.
3. Use `NodeId`s with the high-level and Node APIs.

!!! info
    For the bigger picture — what a namespace is, how URIs and indices relate, and why `ns0` is fixed — see [Namespaces](../../manual/opcua-fundamentals/namespace.md). The short version is: `ns0` is the namespace defined by the OPC UA specification itself, its index is **always `0`** on every server, and it carries the standard types and services (`NodeId`, `ReadRequest`, `BaseEventType`, `DataChangeFilter`, …) the protocol is built on.

---

## Build a NodeId in any of the supported string forms

The OPC UA spec defines three identifier types for `NodeId`:

- **`i=...`** — numeric, e.g. `"i=2253"` for the `Server` object. Numeric identifiers in `ns0` are assigned by the spec; numeric identifiers elsewhere are vendor- or server-assigned.
- **`s=...`** — string, e.g. `"ns=1;s=MyVariables.MyInteger"`. Useful for human-readable names that survive rebuilds of the address space.
- **`g=...`** — GUID, e.g. `"ns=1;g=ABC123..."`. Globally unique by construction; rare in practice.

Each is namespaced by an integer (`ns=2;...`), by an `o6` shortname (`ns=di;...`), or by a full URI (`nsu=http://opcfoundation.org/UA/DI/;...`). The integer index is just a slot in the server's namespace array — what makes a `NodeId` portable across servers is the URI behind the index, not the index itself:

```python
n0 = o6.NodeId("i=84")  # Root, in ns0 (the default when ns= is omitted)
```

The `ns=` parameter may be left, in this case `ns=0` is assumed. `i=84` is `Root`, the standard top of the address space, defined by the spec itself — every OPC UA server exposes it at the same `NodeId` because it lives in `ns0`.

```python
n1 = o6.NodeId("ns=1;s=MyVariables.MyInteger")
```

`ns=1` is also a special case. It's the **server-local namespace** — the distillery's own nodes live here — reserved for "this server" by [Part 5, §6.3.1](https://reference.opcfoundation.org/Core/Part5/v105/docs/6.3.1). For a server-local NodeId, `n1.ns` is just the integer index (`1`); it has no `.uri`, `.version`, or other metadata. To find the URI behind the server's `ns=1`, read it off the server's `ApplicationDescription` (see [Application Description](310_application-description.md)) — there is no other way to get it from a NodeId alone. For other registered namespaces, o6\\Python lets `ns=` accept a shortname:

```python
n2 = o6.NodeId("ns=di;i=15889")    # a DI type, looked up via the DI nodeset's shortname
```

The `ns=<shortname>` form resolves through `o6.ns`. Use `nsu=<full-uri>` when the full URI itself is the portable identifier. Numeric indices are server-local.

!!! tip
    Hard-coded numeric indices can break when a server rebuilds and shifts DI, IA, or vendor namespaces. Use `ns=di;...` with a registered shortname or `nsu=<full-uri>;...` instead.

---

## Read namespace info off any `NodeId`

A `NodeId` doesn't just carry its own identifier — it also carries the *resolved* namespace. The `.ns` attribute returns the namespace's `NamespaceModule` singleton, not a separate metadata wrapper:

```python
import o6
import o6.ns.di

n = o6.NodeId("ns=di;i=15889")
ns = n.ns
print(ns.shortname)         # "di"
print(ns.uri)               # "http://opcfoundation.org/UA/DI/"
print(ns.index)             # global numeric index, e.g. 7
print(ns.version)           # "1.05.0"
print(ns.scope)             # "::global"
print(ns.publicationDate)   # "" if the nodeset recorded none
```

The attributes come straight from the compiled namespace module. `shortname` is the registered handle (`"di"`, `"ia"`, `"ns0"`, `"custom"`, …); `uri` is the stable identity; `index` is the cached global slot (the same value on every server); `scope` marks where the namespace is valid; and `version` and `publicationDate` carry source metadata.

!!! note
    `ns.index` is a *cached* slot that `o6` allocates when the namespace registers, not a live read from a particular server. The number is stable across processes, but it's not guaranteed to match the index the server assigned (e.g. an admin who reordered the server's namespace array). For a stable, server-portable identifier, use `ns.uri`.

For `ns0`, the same call gives you the spec-defined namespace directly:

```python
n0 = o6.NodeId("i=2253")           # the Server object, in ns0
print(n0.ns.shortname)             # "ns0"
print(n0.ns.uri)                   # "http://opcfoundation.org/UA/"
print(n0.ns.index)                 # 0 (always, on every server)
print(n0.ns.version)               # the spec version o6 was built against, e.g. "1.05.07"
print(n0.ns.publicationDate)       # the build date, e.g. "2026-07-30T00:00:00Z"
```

`ns0` is special: its index is **always `0`** on every server, and the URI is always `http://opcfoundation.org/UA/`. The metadata you read back (version, publication date) is the version of the OPC UA spec that `o6` was built against, not anything the server publishes.

---

## Use NodeId's with the high-level and Node APIs

Anywhere a `NodeId` is expected — `client.read`, `client.write`, `client.call`, `client.monitor`, … — you can pass a string, a parsed `NodeId`, or an `o6.ns.<shortname>.<type>` reference that resolves to one:

```python
import o6
import o6.ns.di          # register DI so its type symbols are importable
from o6 import Client

with Client("opc.tcp://localhost:4840") as client:
    # String form — works for ns0 (default) and ns=1; everything else
    # benefits from a registered shortname or full namespace URI.
    v1 = client.read("ns=1;i=1204")   # Status.Setpoint

    # Parsed NodeId
    nid = o6.NodeId("ns=1;i=1204")
    v2 = client.read(nid)

    # ns0 type reference (ns0 is auto-loaded with `import o6`)
    event_type = o6.ns.ns0.objtypes.BaseEventType

    # Companion-spec type reference (the matching module must be
    # imported — `import o6.ns.di` is what registered it above).
    transfer_dt = o6.ns.di.datatypes.TransferResultDataDataType
```

!!! info
    Most of the bundled companion specs (`o6.ns.di`, `o6.ns.ia`, …) are auto-loaded with `import o6`, so `o6.NodeId("ns=di;...")` works without an extra `import o6.ns.di`. Some smaller or vendor specs are deliberately *not* auto-loaded — for those, `import o6.ns.<shortname>` is required before `ns=<shortname>;...` will resolve. `o6.ns` lists what's currently registered.

The same `NodeId`s work as targets for the [Node API](140_node-api-syntax.md) when you navigate the address space with `.` or `[]`.

---

## What's next?

- [Load packaged companion specs](410_load-packaged-companion-specs.md) — what `o6.ns.di` / `o6.ns.ia` give you out of the box.
- [Loading & Using Nodesets](../../manual/sdk-fundamentals/namespace/loading-and-using-nodesets.md) — the full reference for the `Namespace` object.
- [Namespaces](../../manual/opcua-fundamentals/namespace.md) — the spec-level story: URIs vs indices, the namespace array, why `ns0` is fixed.
