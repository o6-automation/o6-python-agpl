# Compiling Nodesets

o6\\Python does not parse `*.NodeSet2.xml` at runtime. A nodeset becomes usable by being **compiled** once into a Python package that registers its namespace and declares one decorated class per type — the exact same shape as the companion specs shipped in `o6/ns/`. From then on it is an ordinary import.

This page walks the compiler from the simplest possible invocation to a full dependency chain and the batch pipeline used to regenerate the shipped specs.

!!! info
    Why a build step rather than runtime parsing — autocomplete, type checking, ~30 ms imports instead of multi-second XML parses, and fail-closed generation — is covered in [Using Nodesets](loading-and-using-nodesets.md#loading-nodesets-from-xml).

---

## Getting the compiler

The compiler is a **development tool and is not part of the PyPI wheel**. It ships only in the [AGPL source repository](https://github.com/o6-automation/o6-python-agpl.git), under `tools/nodeset_compiler/`:

```sh
git clone --recurse-submodules https://github.com/o6-automation/o6-python-agpl.git
cd o6-python-agpl

python3 -m venv .venv
source .venv/bin/activate
pip install . --no-build-isolation
```

`--recurse-submodules` matters twice over: the compiler's frontend delegates XML parsing, dependency merging, alias resolution and node sorting to the vendored open62541 nodeset compiler in `deps/open62541/`, and the OPC Foundation nodesets it resolves dependencies against live in `deps/UA-Nodeset/`.

Run it as a module from the repository root — it resolves `deps/` relative to the checkout:

```sh
python -m tools.nodeset_compiler.backend_python --help
```

The generated package only needs the installed `o6` runtime, so the checkout is a build-time requirement, not a deployment one. Compile on a machine with the repository, ship the generated package with your application.

!!! info
    The compiled output is plain generated Python. Nothing in it is AGPL-specific, and it imports only public `o6` API.

---

## Step 1 — a nodeset that depends only on `ns0`

The smallest useful invocation takes three things: the XML, the **shortname** the namespace will be known by, and an output path.

```sh
python -m tools.nodeset_compiler.backend_python path/to/MyModel.NodeSet2.xml \
    --existing ns0=deps/UA-Nodeset/Schema/Opc.Ua.NodeSet2.Services.xml \
    --shortname mymodel \
    --out mymodel
```

- **`--shortname mymodel`** is the handle everything else uses: `o6.ns.mymodel`, `ns=mymodel;i=…`, the entry in the `o6.ns` table. Pick it once — it becomes part of your source code.
- **`--existing ns0=…`** binds the base OPC UA namespace. Every nodeset references `ns0` reference types (`HasProperty`, `HasComponent`, …), so this is effectively mandatory; without it the frontend aborts with `Reference … has an unknown reference type`.
- **`--out mymodel`** is a **directory**, not a file. The compiler writes a package there and removes stale members of previous runs.

The result:

```
mymodel/
├── __init__.py        # registers the namespace, imports the categories in order
├── reftypes.py        # ReferenceType declarations
├── datatypes.py       # structures, enums, unions
├── datatypes.pyi      # static API projection for the datatypes above
├── vartypes.py        # VariableType declarations
├── objtypes.py        # ObjectType declarations
└── instances.py       # Object / Variable / Method instance declarations
```

`__init__.py` is the whole registration story:

```python
"""Generated OPC UA mymodel namespace."""

from o6.ns import _initialize_namespace

_initialize_namespace(__name__, shortname='mymodel', uri='http://example.org/MyModel/',
                      version='1.0', publication_date='2026-01-31T00:00:00Z')

from . import reftypes as reftypes
from . import datatypes as datatypes
...
```

The URI, version and publication date are read out of the nodeset's own `<Model>` element — you never restate them.

---

## Step 2 — use it

The generated package registers itself on import, so put it anywhere on `sys.path`:

```python
import o6
import mymodel                       # registers 'mymodel' in o6.ns

server = o6.Server(port=4840)
server.ns.append(mymodel)             # publish it into the address space
server.start()

value = mymodel.datatypes.MyStruct()
o6.NodeId("ns=mymodel;i=1")           # the shortname resolves
o6.ns.mymodel.index                   # also reachable through the registry
```

Note that `o6.ns.mymodel` works even though the package lives outside `o6/ns/` — `_initialize_namespace` adopts the importing module as the canonical namespace module for that shortname.

Clients need no extra step. They map the server's NamespaceArray by URI on connect — see [Using Nodesets](loading-and-using-nodesets.md#appending-packaged-companion-specs).

---

## Step 3 — one dependency

Most real nodesets build on another one. Declaring the base with `--existing` is what lets cross-namespace parents resolve; repeat the flag per dependency, always in `SHORTNAME=PATH` form:

```sh
python -m tools.nodeset_compiler.backend_python path/to/MyDevice.NodeSet2.xml \
    --existing ns0=deps/UA-Nodeset/Schema/Opc.Ua.NodeSet2.Services.xml \
    --existing di=deps/UA-Nodeset/DI/Opc.Ua.Di.NodeSet2.xml \
    --shortname mydevice \
    --out mydevice
```

Omitting a dependency the nodeset declares in its `<RequiredModel>` fails explicitly rather than generating something broken:

```
ValueError: namespace http://opcfoundation.org/UA/DI/ has no supplied model binding
```

The shortname you give a dependency is the one the generated source imports:

```python
# mydevice/objtypes.py
import o6.ns.ns0 as ns0
import o6.ns.di as di            # ← from --existing di=…

@o6.objecttype(nodeId='ns=mydevice;i=1002', browseName='ns=mydevice;PumpType')
class PumpType(di.objtypes.DeviceType):
    ...
```

!!! warning
    A dependency's shortname must match the shortname the dependency is *registered under at runtime*. Use the bundled shortnames (`di`, `ia`, `machinery`, …) for anything already shipped in `o6/ns/`, or the generated module will import a namespace that does not exist.

At runtime, dependencies must also be appended to the server before the dependent nodeset:

```python
from o6.ns import di
import mydevice

server.ns.append(di)          # base first
server.ns.append(mydevice)
```

---

## Step 4 — a dependency chain

Deeper stacks are the same flag, once per namespace in the transitive closure — not just the direct parents. A machine-tool style model needs DI, IA and Machinery underneath it:

```sh
python -m tools.nodeset_compiler.backend_python path/to/MyMachine.NodeSet2.xml \
    --existing ns0=deps/UA-Nodeset/Schema/Opc.Ua.NodeSet2.Services.xml \
    --existing di=deps/UA-Nodeset/DI/Opc.Ua.Di.NodeSet2.xml \
    --existing ia=deps/UA-Nodeset/IA/Opc.Ua.IA.NodeSet2.xml \
    --existing machinery=deps/UA-Nodeset/Machinery/Opc.Ua.Machinery.NodeSet2.xml \
    --shortname mymachine \
    --out mymachine
```

Flag order does not matter — dependency resolution is by URI, taken from each file's `<Model>` element. A single generated address space contains at most one release per namespace URI, though several releases of the same URI can coexist in the process-wide `o6.ns` table under different shortnames.

Compile each nodeset separately and import all of them; a compiled package is per-namespace, and `--existing` only tells the frontend where to find endpoints it must resolve against.

---

## Step 5 — inspecting a nodeset first

Dropping `--shortname` switches the backend into an **inventory** pass. It emits a single diagnostic module listing every node, its NodeClass and its BrowseName instead of a loadable namespace — useful when a model fails to generate and you want to see what is in it:

```sh
python -m tools.nodeset_compiler.backend_python path/to/MyModel.NodeSet2.xml \
    --existing ns0=deps/UA-Nodeset/Schema/Opc.Ua.NodeSet2.Services.xml \
    --out mymodel_inventory.py
```

Here `--out` is a plain `.py` file. The inventory is not importable as a namespace.

---

## When generation fails

The backend is deliberately strict: an unsupported node or node attribute **fails compilation** rather than producing a namespace that is quietly missing part of the model. Coverage is documented in [`tools/nodeset_compiler/README.md`](https://github.com/o6-automation/o6-python-agpl/blob/main/tools/nodeset_compiler/README.md) and the generation matrix. In practice the failures you are most likely to hit are:

| Symptom | Cause |
|---|---|
| `Reference … has an unknown reference type` | `--existing ns0=…` missing |
| `namespace <uri> has no supplied model binding` | a `RequiredModel` dependency has no `--existing` entry |
| an `UnsupportedFeature` / `UnsupportedNodeSetError` | a construct the Python backend does not represent yet |
| a description-cache miss | a URL-valued `<Description>` with no entry in `tools/nodeset_compiler/link_cache.json` |

Descriptions are deterministic inputs: ordinary text is emitted unchanged, and a URL-valued description is substituted only from the checked-in cache. Network access is confined to one explicit operation, which updates the cache and does not generate source in the same run:

```sh
python -m tools.nodeset_compiler.backend_python path/to/MyModel.NodeSet2.xml \
    --refresh-description-cache
```

---

## See also

- Importing, appending and using a compiled namespace:
  [Using Nodesets](loading-and-using-nodesets.md).
- The process-wide namespace table and the list of shipped companion specs:
  [Namespace Mapping in o6\\Python](namespace-mapping-in-o6.md).
- What a nodeset file is, and where companion specs come from:
  [Nodeset Files & Companion Specs](../opcua-recap/nodesets-and-companion-specs.md).
- Writing a nodeset directly in Python with the `@o6` decorators instead of compiling XML:
  [`examples/nodeset/myns.py`](https://github.com/o6-automation/o6-python-agpl/blob/main/examples/nodeset/myns.py).
- The normative nodeset XML schema:
  [Part 6, Annex F — Information Model XML Schema](https://reference.opcfoundation.org/Core/Part6/v105/docs/F).
