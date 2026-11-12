# Load packaged companion specs

OPC UA defines standard types such as `EUInformation`, `Range` and `ServerStatus`. Domain-specific types come from companion specifications. To use them from Python, load the matching companion specification into your client.

o6\\Python includes [packaged companion models](../../manual/sdk-fundamentals/namespace/namespace-mapping-in-o6.md#packaged-models) under `o6.ns.<shortname>` (`o6.ns.di`, `o6.ns.ia`, …). `print(o6.ns)` lists the installed names and versions. Import a module to access its declarations.

This page covers three steps:

- Import a bundled companion specification.
- See what is registered in the process-wide namespace table.
- Use the types and address nodes by their namespace URI.

!!! info
    This tutorial expects the [example server running](../setup.md) in the background, and assumes you know how to [create and connect](100_connect.md) a client, how to [browse](110_browse.md) the address space, and how to [secure](300_security.md) the connection. The distillery doesn't use companion specification types. The snippets use `o6.ns.di` (the Devices companion specification), which ships with `o6`.

---

### What are namespaces and companion specs useful for?

OPC UA defines its base types in `ns0`, the namespace of the specification itself (`http://opcfoundation.org/UA/`, index `0` on every server). `ns0` contains the built-in types (`Boolean`, `Double`, `String`), the service messages (`ReadRequest`, `WriteRequest`, `CallRequest`), the standard event types (`BaseEventType`) and the standard reference types (`HasComponent`, `HasProperty`, `Organizes`). Industrial equipment needs more: a pump exposes operating hours and motor current, a PLC exposes program organization units (POUs) and tag tables, an analyser exposes calibration certificates.

A *companion specification* is a nodeset, published by an industry group or standards body, that defines such domain-specific types in its own namespace. The OPC Foundation publishes a family of them, such as `DI` (Devices), `IA` (Industry Automation), `I4AAS` (Asset Administration Shell), `Machinery`, `Robotics` and `Safety`. Each is a self-contained `*.NodeSet2.xml` file. o6\\Python compiles the ones it ships into importable Python modules. Most real deployments load at least one.

Loading a companion specification gives you two things:

- **Importable types.** Generated declarations are grouped by kind under `o6.ns.<shortname>.datatypes`, `.objtypes`, `.vartypes`, `.reftypes` and `.instances`. You can construct datatype values, instantiate declared types and pass them to the server. `o6` does the encoding.
- **NodeIds addressable by shortname.** `ns=di;i=...`, `ns=ia;i=...` and so on work without hard-coding the server's numeric namespace index. Use `nsu=<full-uri>;...` for a full namespace URI.

Both sides must know a companion specification for the type definitions to agree. A server that publishes `ns=di;i=15889` as a `TransferResultDataDataType` only makes sense to a client that has the DI nodeset registered and can decode that type. Importing it on the client is enough to encode values. Reading values of that type from a server that does not publish the DI nodeset returns an opaque `ExtensionObject` instead of the decoded structure.

---

## Import a bundled companion spec

Each shipped companion specification is a module. Importing it registers the namespace in the process-wide table and makes its types available:

```python
import o6
import o6.ns.di    # register the Devices companion spec
```

!!! info
    Importing `o6` pre-registers every shipped namespace. Accessing `o6.ns.di` lazily loads its generated category modules and declarations.

There is no per-client registration step. Registration is process-wide, and a client maps the server's namespace indices to the registered URIs when it connects (see [NodeIds and namespace info](430_nodeids-and-namespace-info.md)).

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

To iterate the entries, use `filter()`. It returns the matching `NamespaceModule` singletons:

```python
for namespace in o6.ns.filter():
    print(namespace.index, namespace.shortname, namespace.uri)
```

---

## Use the types and address nodes

After the import, declarations are available through their category modules:

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

In a Python REPL, category modules give focused completion. For example, `o6.ns.di.datatypes.<TAB>` lists the DI datatypes.

---

## Next steps

| Topic | What it covers |
|---|---|
| [Load nodeset files](420_load-nodeset-files.md) | The same workflow for nodesets that aren't bundled (vendor specifications, your own models). |
| [NodeIds and namespace info](430_nodeids-and-namespace-info.md) | Shortname → index resolution and reading namespace metadata off any `NodeId`. |
| [Semantic discovery](440_semantic-discovery.md) | Navigate the distillery's address space by `BrowseName` instead of `NodeId`, as in `client.objects.DistillingSystem.Kettle.Temperature()`. |
