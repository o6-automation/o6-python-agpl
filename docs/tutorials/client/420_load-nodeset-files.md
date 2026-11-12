# Load nodeset files

Companion specifications that aren't bundled with o6\\Python, such as vendor specifications or your own models, come as `*.NodeSet2.xml` files. `o6` does not parse nodeset XML at runtime. You compile the nodeset once into a Python module and import that module like a bundled companion specification.

This page covers three steps:

- Compile a nodeset XML file into a Python module.
- Import the module to register it in the process-wide table.
- Use the loaded namespace's types and NodeIds.

!!! info
    This tutorial requires you to know how to [create and connect](100_connect.md) a client and how [namespaces](430_nodeids-and-namespace-info.md) work. It assumes a server is running on localhost as described in [Set the Stage](../setup.md). The distillery server does not publish a custom nodeset. This page shows the workflow for a server that does.

---

## Compile a nodeset into a Python module

The compiler is a separate development tool, `o6-ncc`. It is not part of the `o6` wheel; install it with `pip install o6-ncc`. Run `pyncc` with these arguments:

- the `*.NodeSet2.xml` file
- `--shortname`: the shortname of the namespace, the stable handle you use everywhere afterwards
- `-e ns0`: binds the base OPC UA namespace
- `-o`: the directory the package is written into

```bash
pyncc path/to/MyCustom.NodeSet2.xml \
    --shortname custom \
    -e ns0 \
    -o .
```

The generated `custom/` package has the same shape as the bundled `o6.ns.di` and `o6.ns.ia` packages. It registers its namespace on import and defines one decorated class per type definition, split into `datatypes`, `objtypes`, `vartypes`, `reftypes` and `instances`.

If the nodeset builds on another one (most vendor specifications depend on `DI`), declare each dependency with another `-e` so cross-namespace parents resolve. Refer to companion specifications bundled with the compiler by their shortname:

```bash
pyncc path/to/MyCustom.NodeSet2.xml \
    --shortname custom \
    -e ns0 -e di \
    -o .
```

!!! info
    o6\\Python does not load NodeSet2 XML files at runtime. Compile them and import the generated module. See [Compiling Nodesets](../../manual/information-model-authoring/compiling-nodesets.md) for the full workflow, including dependency chains and packaging.

---

## Import the module

Importing the generated module registers its namespace in the process-wide `o6.ns` registry and makes its declarations available, like a bundled companion specification:

```python
import o6
import mycustom          # your generated module

client = o6.Client("opc.tcp://localhost:4840")

# Registered in the global table; addressable by shortname.
print(o6.NodeId("ns=custom;i=1").ns.shortname)   # "custom"
```

If you place the generated directory in the `o6/ns/` package as `o6/ns/custom/`, it is also reachable as `o6.ns.custom` without an import of your own. Otherwise, import it by the module path you saved it under. `ns=custom;...` resolves in both cases once the module is loaded.

There is no per-client registration step. Registration is process-wide, and a client maps the server's namespace indices when it connects (see [NodeIds and namespace info](430_nodeids-and-namespace-info.md)).

---

## Use the types and NodeIds

The generated module exposes its declarations, and the shortname works in any `NodeId`:

```python
import o6
import mycustom
from mycustom import datatypes, objtypes, vartypes     # one per OPC UA type family
from o6 import Client

dt = datatypes.MyDataType          # the generated type class
value = dt()                       # construct an instance

with Client("opc.tcp://localhost:4840") as client:
    nid = o6.NodeId("ns=custom;s=SomeNode")
```

---

## Next steps

| Topic | What it covers |
|---|---|
| [Load packaged companion specs](410_load-packaged-companion-specs.md) | The bundled `o6.ns.di` and `o6.ns.ia`. |
| [NodeIds and namespace info](430_nodeids-and-namespace-info.md) | Shortname → index resolution and reading namespace metadata off any `NodeId`. |
| [Loading & Using Nodesets](../../manual/sdk-fundamentals/namespace/loading-and-using-nodesets.md) | The full reference for the `Namespace` machinery. |
| [Compiling Nodesets](../../manual/information-model-authoring/compiling-nodesets.md) | Compiler options, dependency chains, and packaging. |
