# Load nodeset files

Companion specs that aren't bundled with o6\\Python (vendor specs, your own models, …) come as `*.NodeSet2.xml` files. **o6** does *not* parse nodeset XML at runtime — instead you **compile** the nodeset once into a Python module, then import that module exactly like a bundled companion spec.

This page walks through three steps:

- Compile a nodeset XML file into a Python module.
- Import the module to register it in the process-wide table.
- Use the loaded namespace's types and NodeIds.

!!! info
    This tutorial requires you to know how to [create and connect](100_connect.md) a client and how [namespaces](430_nodeids-and-namespace-info.md) work. It assumes a server is running on localhost as described in [the example server](../../tutorials.md#the-example-server) in the tutorials intro. Note the distillery server does not itself publish a custom nodeset — this page is about the general workflow for any server that does.

---

## Compile a nodeset into a Python module

The compiler lives in the source repository under `tools/nodeset_compiler/` (it is not part of the PyPI wheel). Point it at the `*.NodeSet2.xml`, bind the base OPC UA namespace with `--existing`, give the namespace a **shortname** (the stable handle you'll use everywhere afterwards), and write the generated package with `--out`:

```bash
python -m tools.nodeset_compiler.backend_python path/to/MyCustom.NodeSet2.xml \
    --existing ns0=deps/UA-Nodeset/Schema/Opc.Ua.NodeSet2.Services.xml \
    --shortname custom \
    --out mycustom
```

The generated `mycustom/` package follows the same shape as the bundled `o6.ns.di` / `o6.ns.ia` packages: it registers its namespace on import and defines one decorated class per type definition, split into `datatypes`, `objtypes`, `vartypes`, `reftypes` and `instances`.

If the nodeset builds on another one (most vendor specs depend on `DI`), declare each dependency with another `--existing SHORTNAME=FILE` so cross-namespace parents resolve:

```bash
python -m tools.nodeset_compiler.backend_python path/to/MyCustom.NodeSet2.xml \
    --existing ns0=deps/UA-Nodeset/Schema/Opc.Ua.NodeSet2.Services.xml \
    --existing di=deps/UA-Nodeset/DI/Opc.Ua.Di.NodeSet2.xml \
    --shortname custom \
    --out mycustom
```

!!! info
    The legacy runtime-loading path (`o6.ns.load("…​.NodeSet2.xml")` / `server.ns.load(...)`) has been **retired**. Namespaces are declared by importing a compiled module, not by parsing XML at runtime. See [Compiling Nodesets](../../types-addrspace/namespace/compiling-nodesets.md) for the full workflow, including dependency chains and the batch pipeline.

---

## Import the module

Importing the generated module registers its namespace in the process-wide `o6.ns` registry and makes its declarations available — exactly like importing a bundled companion spec:

```python
import o6
import mycustom          # your generated module

client = o6.Client("opc.tcp://localhost:4840")

# Registered in the global table; addressable by shortname.
print(o6.NodeId("ns=custom;i=1").ns.shortname)   # "custom"
```

If you drop the generated directory into the `o6/ns/` package as `o6/ns/custom/`, it also becomes reachable as `o6.ns.custom` with no import of your own — the same attribute style as the bundled specs. Otherwise import it by whatever module path you saved it under; the `ns=custom;...` resolution works either way once the module has been loaded.

As with bundled specs, there is no per-client "append" step: registration is process-wide, and a client maps the server's namespace indices automatically when it connects (see [NodeIds and namespace info](430_nodeids-and-namespace-info.md)).

---

## Use the types and NodeIds

The generated module exposes its declarations, and the shortname works in any `NodeId`:

```python
import o6
import mycustom
from o6 import Client

dt = mycustom.MyDataType          # the generated type class
value = dt()                       # construct an instance

with Client("opc.tcp://localhost:4840") as client:
    nid = o6.NodeId("ns=custom;s=SomeNode")
    # ... read / write / call using nid, or mycustom types as values
```

---

## What's next?

- [Load packaged companion specs](410_load-packaged-companion-specs.md) — the bundled `o6.ns.di` / `o6.ns.ia`.
- [NodeIds and namespace info](430_nodeids-and-namespace-info.md) — shortname → index resolution and reading namespace metadata off any `NodeId`.
- [Loading & Using Nodesets](../../types-addrspace/namespace/loading-and-using-nodesets.md) — the full reference for the `Namespace` machinery.
- [Compiling Nodesets](../../types-addrspace/namespace/compiling-nodesets.md) — every compiler flag, dependency chains, and the batch pipeline.
