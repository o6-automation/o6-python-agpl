# Load packaged companion specs

The distillery's connections are stable now — the channel stays open, the session stays activated, the watchers log only the transitions you expect. Time to start using the *types* the server publishes, not just the values. The distillery's `Kettle.Temperature` is a `Double`, but the OPC UA type system also defines `EUInformation`, `Range`, `ServerStatus`, and many other standard types that an address space may reference. To use domain-specific types from Python, you load the matching companion spec into your client.

o6\\Python ships with several companion specs already bundled — see the [complete list](../../types-addrspace/namespace/namespace-mapping-in-o6.md#packaged-companion-specs). Each one is a compiled Python module under `o6.ns.<shortname>` (`o6.ns.di`, `o6.ns.ia`, …). Importing a module registers its namespace and exposes its types.

This page walks through three steps:

- Import a bundled companion spec.
- See what is registered in the process-wide namespace table.
- Use the types and address nodes by their namespace URI.

!!! info
    This tutorial expects the [example server running](../../tutorials.md#running-the-example-server) in the background, and assumes you know how to [create and connect](100_connect.md) a client, how to [browse](110_browse.md) the address space, and how to [secure](300_security.md) the connection. The distillery itself doesn't use any companion-spec types directly, but the snippets use `o6.ns.di` (the *Devices* companion spec) as the example, since it's the closest match to "industrial equipment" and ships with `o6` by default.

---

### What are namespaces and companion specs useful for?

OPC UA defines a fixed set of base types in **`ns0`** — the namespace the spec itself publishes (`http://opcfoundation.org/UA/`, index `0` on every server). That covers the basics: `Boolean`, `Double`, `String`, the standard services (`ReadRequest`, `WriteRequest`, `CallRequest`), the standard event types (`BaseEventType`), the standard reference types (`HasComponent`, `HasProperty`, `Organizes`), and so on. But "industrial equipment" is broader than that: a vendor's pump exposes operating hours and motor current, a PLC exposes program organization units (POUs) and tag tables, an analyser exposes calibration certificates, and so on.

A **companion spec** is a nodeset published by an industry group or standards body that defines those *domain-specific* types in its own namespace. The OPC Foundation publishes a family of them — `DI` (Devices), `IA` (Industry Automation), `I4AAS` (Asset Administration Shell), `Machinery`, `Robotics`, `Safety`, … — each one a self-contained `*.NodeSet2.xml` file. o6\\Python compiles the ones it ships into importable Python modules. The distillery is a simple example, so it doesn't use any of these, but a real industrial deployment almost always loads at least one.

In Python, two things matter:

- **The types become importable.** Generated declarations are grouped by kind under `o6.ns.<shortname>.datatypes`, `.objtypes`, `.vartypes`, `.reftypes`, and `.instances`. You can construct datatype values, instantiate declared types, and pass them to the server — `o6` does the encoding.
- **The nodes become addressable by shortname.** The matching `NodeId`s — `ns=di;i=...`, `ns=ia;i=...`, … — work without hard-coding the server's numeric namespace index. Use `nsu=<full-uri>;...` when carrying a full namespace URI.

The catch is that a companion spec must be known to *both* sides for the type definitions to agree. A server that publishes `ns=di;i=15889` as a `TransferResultDataDataType` only makes sense to a client that has the DI nodeset registered and knows how to decode that type. Importing it on the client is enough to *encode* values; reading values of that type from a server that does not publish the DI nodeset returns an opaque `ExtensionObject` instead of the decoded structure.

---

## Import a bundled companion spec

Each shipped companion spec is a module. Importing it registers the namespace in the process-wide table and makes its types available:

```python
import o6
import o6.ns.di    # register the Devices companion spec
```

!!! info
    Importing `o6` pre-registers every shipped namespace. Accessing `o6.ns.di` lazily loads its generated category modules and declarations.

Unlike the retired XML-loading workflow, there is no per-client "append" step: registration is process-wide, and when a client connects it automatically maps the server's namespace indices to the registered URIs (see [NodeIds and namespace info](430_nodeids-and-namespace-info.md)).

---

## See what is registered

The process-wide registry is the `o6.ns` singleton. Printing it shows every registered namespace with its shortname, URI, scope, version, and global index:

```python
import o6
import o6.ns.di

print(o6.ns)
# o6.ns (count=...):
#   name   uri                               scope    version  pub_date  index
#   ns0    http://opcfoundation.org/UA/      ::global 1.05.06            0
#   di     http://opcfoundation.org/UA/DI/   ::global 1.05.0             2
#   ...
```

To iterate the entries programmatically, use `filter()`, which returns matching `NamespaceModule` singletons:

```python
for namespace in o6.ns.filter():
    print(namespace.index, namespace.shortname, namespace.uri)
```

---

## Use the types and address nodes

Once the module is imported, declarations are available through their category modules:

```python
import o6
import o6.ns.di
from o6 import Client

tr = o6.ns.di.datatypes.TransferResultDataDataType
print(tr)
i = tr()                        # create an instance of this type
print(i)                        # {sequenceNumber=0, endOfResults=False, parameterDefs=[]}
i.sequenceNumber = 42

with Client("opc.tcp://localhost:4840") as client:
    # NodeIds addressed by URI/shortname work once connected — the server's
    # index for `di` is mapped automatically on connect.
    nid = o6.NodeId("ns=di;i=15889")
    print(nid.ns.shortname)     # "di"
```

In a Python REPL, category modules provide focused completion: for example, `o6.ns.di.datatypes.<TAB>` lists DI datatypes.

---

## What's next?

- [Load nodeset files](420_load-nodeset-files.md) — same shape, but for nodesets that aren't bundled (vendor specs, your own models).
- [NodeIds and namespace info](430_nodeids-and-namespace-info.md) — shortname → index resolution and reading namespace metadata off any `NodeId`.
- [Semantic discovery](440_semantic-discovery.md) — navigate the distillery's address space by `BrowseName` rather than by `NodeId`, with the dotted `client.objects.DistillingSystem.Kettle.Temperature()` style.
