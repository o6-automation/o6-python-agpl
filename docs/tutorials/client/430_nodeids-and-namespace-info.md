# NodeIds and namespace info

Every OPC UA node is identified by a `NodeId`. `o6.NodeId` accepts the standard `i=`, `s=`, and `g=` identifier forms. It also accepts `ns=<shortname>;...` for a registered shortname and `nsu=<full-uri>;...` for a full namespace URI.

A NodeId combines a namespace with a numeric, string, GUID, or ByteString
identifier. `i=2253` identifies the standard Server Object in namespace 0.
`ns=1;i=1302` identifies an application node in whichever server handles the
operation; here, that is the distillery.

On the wire, a namespace index selects a URI from the server's NamespaceArray.
Python normally uses the process-wide `o6.ns` index instead. Namespace 0 is
fixed, and `ns=1` is the application-local alias.

This page covers three steps:

1. Build a `NodeId` in any of the supported string forms.
2. Read namespace info (URI, version, index, …) off any `NodeId`.
3. Use `NodeId`s with the high-level and Node APIs.

!!! info
    For what a namespace is, how URIs and indices relate and why `ns0` is fixed, see [Namespaces](../../manual/opcua-fundamentals/namespace.md). In short: `ns0` is defined by the OPC UA specification, its index is always `0` on every server, and it holds the standard types and services (`NodeId`, `ReadRequest`, `BaseEventType`, `DataChangeFilter`, …).

---

## Build a NodeId in any of the supported string forms

A NodeId supports four identifier types:

- **`i=...`** — numeric, e.g. `"i=2253"` for the `Server` object. The specification assigns numeric identifiers in `ns0`. Vendors or servers assign them elsewhere.
- **`s=...`** — string, e.g. `"ns=1;s=MyVariables.MyInteger"`. A string identifier assigned by the server or model.
- **`g=...`** — GUID, e.g. `"ns=1;g=09087e75-8e5e-4b7c-b29a-806350ed74dc"`. Globally unique by construction. Rare in practice.
- **`b=...`** — ByteString, e.g. `"ns=1;b=AQIDBA=="` with base64 encoding.

Each is qualified by a namespace index (`ns=2;...`), an `o6` shortname (`ns=di;...`) or a full URI (`nsu=http://opcfoundation.org/UA/DI/;...`). In an `o6.NodeId`, a numeric index selects a process registry entry, except
for the application-local alias 1. The corresponding index on the wire
selects a URI in the server's NamespaceArray. Use that URI when transferring
an identifier between tools:

```python
import o6

n0 = o6.NodeId("i=84")  # Root, in ns0 (the default when ns= is omitted)
```

Without `ns=`, `ns=0` is assumed. `i=84` is `Root`, the top of the address space. It lives in `ns0`, so every OPC UA server exposes it at the same `NodeId`.

```python
n1 = o6.NodeId("ns=1;s=MyVariables.MyInteger")
```

`ns=1` is also a special case. It is the *server-local namespace*, reserved for "this server" by [Part 5, §6.3.1](https://reference.opcfoundation.org/Core/Part5/v105/docs/6.3.1). The distillery's own nodes live here. For a server-local NodeId, `n1.ns` is the integer index (`1`), with no `.uri`, `.version` or other metadata. A NodeId alone can't give you the URI behind the server's `ns=1`. Read `client.read("i=2255")[1]` from the connected server's NamespaceArray.
Returned namespace-1 identifiers can instead carry a concrete registry
module such as `client1_ns1`.

For other registered namespaces, `ns=` accepts a shortname:

```python
n2 = o6.NodeId("ns=di;i=15889")    # a DI type, looked up via the DI nodeset's shortname
```

The `ns=<shortname>` form resolves through `o6.ns`. Use `nsu=<full-uri>` when you carry the full URI and it uniquely identifies a
registered entry. For a copied numeric ID, follow
[Registry and Namespace Mapping](../../manual/sdk-fundamentals/namespace/namespace-mapping-in-o6.md#process-indices-and-server-indices).

!!! tip
    A process index can differ from a server index and can change between runs. Use `ns=di;...` with a registered shortname or `nsu=<full-uri>;...` instead.

---

## Read namespace info off any `NodeId`

For a registered namespace, `.ns` returns the `NamespaceModule` singleton
that holds its metadata. The application-local alias 1 remains an integer:

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

The attributes come from the compiled namespace module:

| Attribute | Meaning |
|---|---|
| `shortname` | The registered handle (`"di"`, `"ia"`, `"ns0"`, `"custom"`, …) |
| `uri` | The stable identity |
| `index` | The cached global slot `o6` allocated (see the note below) |
| `scope` | Where the namespace is valid |
| `version`, `publicationDate` | Metadata from the source nodeset |

!!! note
    `ns.index` is a cached slot that `o6` allocates when the namespace registers, not a live read from a server. The number is stable within the current process, but must not be treated as
    portable between processes or as a server's local index. For a stable, server-portable identifier, use `ns.uri`.

For `ns0`, the same attributes describe the specification's namespace:

```python
n0 = o6.NodeId("i=2253")           # the Server object, in ns0
print(n0.ns.shortname)             # "ns0"
print(n0.ns.uri)                   # "http://opcfoundation.org/UA/"
print(n0.ns.index)                 # 0 (always, on every server)
print(n0.ns.version)               # the spec version o6 was built against, e.g. "1.05.07"
print(n0.ns.publicationDate)       # the build date, e.g. "2026-07-30T00:00:00Z"
```

The index of `ns0` is always `0` on every server, and its URI is always `http://opcfoundation.org/UA/`. Version and publication date describe the OPC UA specification that `o6` was built against, not anything the server publishes.

---

## Use NodeIds with the high-level and Node APIs

Wherever a `NodeId` is expected (`client.read`, `client.write`, `client.call`, `client.monitor`, …), you can pass a string, a parsed `NodeId` or an `o6.ns.<shortname>.<type>` reference that resolves to one:

```python
import o6
import o6.ns.di          # access the packaged DI namespace
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

    # Accessing a declaration loads the packaged model's types.
    transfer_dt = o6.ns.di.datatypes.TransferResultDataDataType
```

!!! info
    Bundled companion namespace identities register with `import o6`.
    Their declarations load on first access; a bare `import o6.ns.di` does
    not force datatype loading. Import a custom generated package before
    using its shortname. An unknown server URI gets an identity-only client
    registration on connection, which supplies no custom structure classes.
    See [Unknown namespaces and structured values](../../manual/sdk-fundamentals/namespace/loading-and-using-nodesets.md#unknown-namespaces-and-structured-values).

The same `NodeId`s work as targets for the [Node API](140_node-api-syntax.md) when you navigate the address space with `.` or `[]`.

---

## Next steps

| Topic | What it covers |
|---|---|
| [Load packaged companion specs](410_load-packaged-companion-specs.md) | What `o6.ns.di` / `o6.ns.ia` give you out of the box. |
| [Loading & Using Nodesets](../../manual/sdk-fundamentals/namespace/loading-and-using-nodesets.md) | The full reference for the `Namespace` object. |
| [Namespaces](../../manual/opcua-fundamentals/namespace.md) | URIs vs indices, the namespace array, why `ns0` is fixed. |
