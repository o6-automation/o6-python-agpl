# Address & Identity Types

OPC UA identifies nodes and their BrowseNames with the built-in datatypes below. [OPC UA Part 3 — Address Space Model, §8 Standard DataTypes](https://reference.opcfoundation.org/Core/Part3/v105/docs/8) has the normative definitions. For human-readable strings, see [LocalizedText](primitive-types.md#localizedtext).

| o6\\Python type | Purpose |
|---|---|
`o6.NodeId` | The unique handle of a node in a server's address space. |
`o6.ExpandedNodeId` | A `NodeId` plus the optional namespace URI and server index — needed when the node lives outside the local server (e.g. in another server behind a server array). |
`o6.QualifiedName` | The (namespace, name) pair used as a node's BrowseName: the locale-independent path component used to navigate the address space. |

## NodeId

A `NodeId` is the machine-readable identity of a node. Every address-space operation (read, write, browse, call, monitor, …) targets a `NodeId`. It has two fields:

    NodeId {
        namespace_index     # which naming authority the identifier belongs to
        id                  # numeric, string, GUID, ByteString
    }

### Which namespace index?

A numeric index in an OPC UA message selects a URI from that server's
NamespaceArray. In an `o6.NodeId`, indices normally refer to the process-wide
`o6.ns` registry instead. The client or server translates between these two
sets of indices when exchanging values.

`ns=0` is always the standard namespace. `ns=1` is the exception to process-wide
lookup: it means the application namespace of whichever client or server
handles the operation. An index of 2 or above copied from another OPC UA
browser must be resolved through that server's namespace URI first.
[Registry and Namespace Mapping](../namespace/namespace-mapping-in-o6.md#process-indices-and-server-indices)
explains the URI and shortname forms. Prefer registered shortnames or URIs for other namespaces.

### Parsing NodeId

Construct an `o6.NodeId` from a namespace index and an identifier. These
examples use namespace 0 and the application-local alias 1:

```python
import uuid
import o6

o6.NodeId(84)                       # ns=0 shorthand, numeric
o6.NodeId(ns=1, i=5)                # numeric (ns, i)
o6.NodeId(ns=1, s="Temperature")    # string   (ns, s)
o6.NodeId(ns=1, b=b"\x00\x01")      # bytestring (ns, b) — rare
o6.NodeId(ns=1, g=uuid.UUID("09087e75-8e5e-4b7c-b29a-806350ed74dc"))   # GUID (ns, g) — globally unique
```

Or parse both from a single string:

```python
o6.NodeId("i=84")                   # ns=0 numeric shorthand
o6.NodeId("ns=1;s=Temperature")     # string id
o6.NodeId("ns=1;i=5")               # numeric id
o6.NodeId("ns=1;b=AQIDBA==")        # bytestring (base64)
o6.NodeId("ns=1;g=09087e75-8e5e-4b7c-b29a-806350ed74dc")      # GUID
```

#### Parsing from shortname or URI

A registered shortname identifies one entry in `o6.ns`. A URI resolves to an
existing registration, optionally filtered by scope and version. Packaged
namespace identities such as `di` are registered by `import o6`; remote
unknown URIs are registered when a client connects:

```python
o6.NodeId("ns=di;i=1")                                                  # ns by shortname
o6.NodeId("nsu=http://opcfoundation.org/UA/DI/;i=1")                    # ns by URI
o6.NodeId("nsu=http://opcfoundation.org/UA/DI/@::global!1.05.0;i=1")    # ns by URI + scope + version
```

!!! note
    A URI must match exactly one registry entry. Multiple versions or client
    scopes can share it. The SDK's `@scope!version` suffix selects a registration;
    see [Scope and version in identifiers](../namespace/namespace-mapping-in-o6.md#scope-and-version-in-identifiers).

#### Getting OPC UA type information

Construct a `NodeId` from a DataType class to get the DataType's NodeId:

```python
o6.NodeId(o6.Double)                                    # >>> o6.NodeId(i=11)
dbl = o6.Double(3.1415)
o6.NodeId(type(dbl))                                    # >>> o6.NodeId(i=11)
o6.NodeId(o6.ns.di.datatypes.DeviceHealthEnumeration)   # >>> o6.NodeId('ns=di;i=6244')
```

### Inspecting a NodeId's namespace

For a registered namespace, `NodeId.ns` returns its namespace module, even
if model declarations have not loaded. Metadata is available directly:

```python
n = o6.NodeId("ns=di;i=1")
n.ns.shortname                  # 'di'
n.ns.uri                        # 'http://opcfoundation.org/UA/DI/'
n.ns.version                    # '1.05.0'
```

For the application-local alias, `o6.NodeId("ns=1;i=5").ns` is the integer
`1`; the alias carries no endpoint URI of its own. A numeric index with no
registration also returns an integer. This is different from a remote URI
registered on connection, which has a namespace module even without a nodeset.

---

## ExpandedNodeId

An `ExpandedNodeId` carries a NodeId, an optional namespace URI (`nsu`),
and a server index (`svr`). Browse references use this type so they can point
to other servers. Method outputs or notifications contain it only when the
value's datatype calls for it.

An explicit URI is retained in `.nsu`; it does not have to resolve to a
registered Python namespace:

```python
eni = o6.ExpandedNodeId("svr=1;nsu=http://example.org/Plant/;i=5")
eni.id       # 5
eni.nsu      # 'http://example.org/Plant/'
eni.svr      # 1: an entry in the originating server's ServerArray
```

When `.nsu` is nonempty, use it as the namespace identity. `.ns` then reflects
the unused index 0, not the URI's registration. Without an explicit URI, `.ns`
resolves the index like `NodeId.ns`. A nonzero `.svr` refers to another server;
passing the identifier to the current client does not connect to that server.

---

## QualifiedName

A `QualifiedName` is a human-readable, locale-independent `(namespace, name)` pair that describes what a node means. The same `QualifiedName` identifies the same concept on every server, while the `NodeId` can differ between servers.

```python
o6.QualifiedName(1, "Temperature")                                  # namespace index + name
o6.QualifiedName("1:Pump")                                          # ns:name shorthand
o6.QualifiedName("ns=di;DeviceSet")                                # ns by shortname
o6.QualifiedName("nsu=http://opcfoundation.org/UA/DI/;DeviceSet")   # ns by URI
```

A `QualifiedName` uses the same process-index and application-alias rules as
`NodeId`. Its `ns` property returns a registered module or an integer as
described in [Inspecting a NodeId's namespace](#inspecting-a-nodeids-namespace):

```python
qn = o6.QualifiedName(1, "Temperature")
qn.ns       # 1: the application-local alias, with no module
qn.name     # 'Temperature'
```

Unlike a `NodeId`, a `QualifiedName` is not unique: many nodes can share one. It identifies what a node is, not which node.

Like `NodeId` and `ExpandedNodeId`, a `QualifiedName` is immutable and hashable. Equal names hash equally, so it works as a dictionary key or in a set, for example for the `fields` of an [event](../../server/events.md#event-fields).

---

## Related topics

| Topic | What it covers |
|---|---|
| [Part 3, §8.2 — NodeId](https://reference.opcfoundation.org/Core/Part3/v105/docs/8.2) | The normative NodeId definition. |
| [Part 3, §8.3 — QualifiedName](https://reference.opcfoundation.org/Core/Part3/v105/docs/8.3) | The normative QualifiedName definition. |
| [Part 3, §8 — Standard DataTypes](https://reference.opcfoundation.org/Core/Part3/v105/docs/8) | Standard address types, including ExpandedNodeId. |
| [Part 6, §5.1.12 — QualifiedName, NodeId and ExpandedNodeId String Encoding](https://reference.opcfoundation.org/Core/Part6/v105/docs/5.1.12) | String encoding of QualifiedName, NodeId, and ExpandedNodeId. |
| [Part 6, §5.2.2.9 — NodeId (binary)](https://reference.opcfoundation.org/Core/Part6/v105/docs/5.2.2.9) | Binary encoding of NodeId. |
| [Namespace](../../opcua-fundamentals/namespace.md) | OPC UA namespaces and URI-to-index mapping. |
| [Namespace Mapping in o6\\Python](../namespace/namespace-mapping-in-o6.md) | Namespace lookup and resolution in Python. |
