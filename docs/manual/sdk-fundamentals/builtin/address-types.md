# Address & Identity Types

In OPC UA, every node, every browse name, and every human-readable string is addressed with one of four built-in datatypes. The names and shapes come straight from the OPC UA specification — see [OPC UA Part 3 — Address Space Model, §8 Standard DataTypes](https://reference.opcfoundation.org/Core/Part3/v105/docs/8) for the normative definitions.

| o6\\Python type | |
|---|---|
`o6.NodeId` | The unique handle of a node in a server's address space. |
`o6.ExpandedNodeId` | A `NodeId` plus the optional namespace URI and server index — needed when the node lives *outside* the local server (e.g. in another server behind a server array). |
`o6.QualifiedName` | The *(namespace, name)* pair used as a node's **browse name** — the locale-independent path component that address-space navigation walks along. |

## NodeId

The *machine-readable* identity of a node. Every operation on the address space (read, write, browse, call, monitor, …) ultimately targets a `NodeId`.
Structurally a `NodeId` is just two fields:

    NodeId {
        namespace_index     # which naming authority the identifier belongs to
        id                  # numeric, string, GUID
    }

### Parsing NodeId

`o6.NodeId`'s can be constructed from several different expressions, i.e. from namespace index and id parameter:

```python
o6.NodeId(84)                       # ns=0 shorthand, numeric
o6.NodeId(ns=1, i=5)                # numeric (ns, i)
o6.NodeId(ns=1, s="Temperature")    # string   (ns, s)
o6.NodeId(ns=1, b=b"\x00\x01")      # bytestring (ns, b) — rare
o6.NodeId(ns=1, g=uuid.UUID("…"))   # GUID (ns, g) — globally unique
```

Namespace index and id can also be parsed from a single string:

```python
o6.NodeId("i=84")                   # ns=0 numeric shorthand
o6.NodeId("ns=1;s=Temperature")     # string id
o6.NodeId("ns=1;i=5")               # numeric id
o6.NodeId("ns=1;b=AQIDBA==")        # bytestring (base64)
o6.NodeId("ns=1;g=09087e75-…")      # GUID
```

#### Parsing from shortname or URI

o6\\Python provides a complete abstraction from manually handling namespace indices. As an extension `NodeId`s may be constructied by supplying a **shortname**, a human-readable string, that uniquely identifies a nodeset, or an (ammended) **URI**.

```python
o6.NodeId("ns=di;i=1")                                                  # ns by shortname
o6.NodeId("nsu=http://opcfoundation.org/UA/DI/;i=1")                    # ns by URI
o6.NodeId("nsu=http://opcfoundation.org/UA/DI/@::global!1.05.0;i=1")    # ns by URI + scope + version
```

!!! note
    URI alone is not necessarily unique, because there may be cases in which the same nodeset in different version needs to be addressed. To disambiguate the URI string can be ammended with a scope and version number. See [Namespaces](../../opcua-fundamentals/namespace.md) for more information.

#### Getting OPC UA type information

Finally `NodeId` can also be constructed from `DataType`s to easily obtain their id:

```python
o6.NodeId(o6.Double)                                    # >>> o6.NodeId(i=11)
dbl = o6.Double(3.1415)
o6.NodeId(type(dbl))                                    # >>> o6.NodeId(i=11)
o6.NodeId(o6.ns.di.datatypes.DeviceHealthEnumeration)   # >>> o6.NodeId('ns=di;i=6244')
```

### Inspecting a NodeId's namespace

In o6\\Python we can obtain additional information from a `NodeId` instance through it's namespace index. The `NodeId.ns` property is therefore not just an integer but makes namespace metadata retrievable. Among other information e.g.:

```python
n = o6.NodeId("ns=di;i=1")      # assume ns=2 is 'di'
n.ns.shortname                  # 'di'
n.ns.uri                        # 'http://opcfoundation.org/UA/DI/'
n.ns.version                    # '1.05.0'
```

---

## ExpandedNodeId

Same identity as `NodeId`, but augmented with a namespace **URI** (`nsu`) and an optional **server index** (`svr`). You will see `ExpandedNodeId` almost everywhere a server hands you a reference — `Browse` results, method outputs, monitored-item notifications — because the spec uses the expanded form whenever there is *any* ambiguity about which namespace or server the target lives in.

Like for `NodeId`, an `ExpandedNodeId` allows us to retrieve additional information through its namespace index via the ns property, see [here](#inspecting-a-nodeids-namespace)

```python
eni = o6.ExpandedNodeId("svr=1;nsu=http://opcfoundation.org/UA/DI/;i=5")
eni.ns       # Namespace module when loaded; otherwise its numeric index
eni.id       # id
eni.nsu      # 'http://opcfoundation.org/UA/DI/' — namespace URI
eni.svr      # server index
```

---

## QualifiedName

A `QualifiedName` is the cross-server, locale-independent, human-readable vocabulary used to describe nodes.

A `QualifiedName` carries the *meaning* of a node as a `(namespace, name)` pair. The same `QualifiedName` therefore identifies the same idea on every server, while the underlying `NodeId` is free to differ.

```python
o6.QualifiedName(1, "Temperature")                                  # namespace index + name
o6.QualifiedName("1:Pump")                                          # ns:name shorthand
o6.QualifiedName("ns=di;DeviceSet")                                # ns by shortname
o6.QualifiedName("nsu=http://opcfoundation.org/UA/DI/;DeviceSet")   # ns by URI
```

A `QualifiedName` exposes two properties, like for `NodeId` and `ExpandedNodeId` we can retrieve additional information through its namespace index via the ns property, see [here](#inspecting-a-nodeids-namespace)

```python
qn = o6.QualifiedName(1, "Temperature")
qn.ns       # Namespace module, or a numeric index if it is not loaded
qn.name     # 'Temperature'
```

Like `NodeId`, the namespace can be supplied as an index, a shortname, or a URI. Unlike a `NodeId`, a `QualifiedName` is **not unique** — many nodes can share the same one. It identifies *what* a node is, not *which* one.

---

## See also

- The OPC UA spec's normative definitions of `NodeId`, `ExpandedNodeId`, and `QualifiedName`, including `nsu=…`/`svr=…` form and the case-sensitive URI comparison rule:
  [Part 3, §8.2 — NodeId](https://reference.opcfoundation.org/Core/Part3/v105/docs/8.2),
  [Part 3, §8.3 — QualifiedName](https://reference.opcfoundation.org/Core/Part3/v105/docs/8.3),
  and the overview in
  [Part 3, §8 — Standard DataTypes](https://reference.opcfoundation.org/Core/Part3/v105/docs/8).
- The wire encoding of `NodeId` / `ExpandedNodeId` / `QualifiedName` (string form, URI form, binary form):
  [Part 6, §5.1.12 — QualifiedName, NodeId and ExpandedNodeId String Encoding](https://reference.opcfoundation.org/Core/Part6/v105/docs/5.1.12)
  and [Part 6, §5.2.2.9 — NodeId (binary)](https://reference.opcfoundation.org/Core/Part6/v105/docs/5.2.2.9).
- OPC UA datatypes and namespace concept [Namespace](../../opcua-fundamentals/namespace.md) and how o6\\Python builds on top of it [Namespace Mapping in o6\\Python](../namespace/namespace-mapping-in-o6.md).
