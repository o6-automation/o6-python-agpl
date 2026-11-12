# Compiling Nodesets

Compile supplied XML into an importable Python package. This workflow is useful
for clients decoding vendor values and servers publishing an existing model.

o6\\Python does not parse `*.NodeSet2.xml` at runtime. You compile a nodeset once into a Python package that registers its namespace and declares one decorated class per type, the same shape as the companion specifications shipped in `o6/ns/`. You then import it like any Python package.

!!! info
    Compilation gives editors named Python declarations for autocomplete and type checking, and keeps XML parsing out of application startup. For the minimal workflow, see [Loading & Using Nodesets](../sdk-fundamentals/namespace/loading-and-using-nodesets.md#loading-nodesets-from-xml).

---

## Getting the compiler

The compiler is a separate distribution, `o6-ncc`. It is a development tool, not a runtime dependency. Install it on the machine that builds your packages; don't ship it with your application:

```sh
pip install o6-ncc
```

It installs three console scripts. This page uses `pyncc`:

| Script | Purpose |
|---|---|
| `pyncc` | Compile a nodeset into an o6\\Python namespace package. |
| `cncc` | Compile a nodeset into open62541 C sources. |
| `ncc` | The combined entry point; `ncc python …` is identical to `pyncc …`. |

The OPC Foundation nodesets that the compiler resolves dependencies against are bundled with the distribution. Generation needs no repository checkout and no network access.

The generated package needs only the installed `o6` runtime. Compile on a build machine and ship the generated package with your application.

!!! info
    The compiled output is plain Python. It runs with the installed `o6` package and carries none of the compiler's licensing into your application.

---

## Step 1 — a nodeset that depends only on `ns0`

The minimal invocation takes the XML, the shortname of the namespace and an output directory:

```sh
--8<-- "docs/snippets/compile-nodeset.sh"
```

- **`--shortname mymodel`** is the handle for `o6.ns.mymodel`, `ns=mymodel;i=…` and the entry in the `o6.ns` table. It becomes part of your source code, so choose it carefully. Without it, the compiler falls back to a pinned name for the model's URI or to the filename stem.
- **`-e ns0`** binds the base OPC UA namespace from the bundled nodesets. Every nodeset references `ns0` ReferenceTypes (`HasProperty`, `HasComponent`, …), so you always need it.
- **`-o .`** is the parent directory. The package is created as `<output>/<shortname>/`, here `./mymodel/`. The directory is created if missing, and stale files from previous runs are removed.

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

Files for empty node categories are omitted.

`__init__.py` does the whole registration:

```python
"""Generated OPC UA mymodel namespace."""

from o6.ns import _initialize_namespace

_initialize_namespace(__name__, shortname='mymodel', uri='http://example.org/MyModel/',
                      version='1.0', publication_date='2026-01-31T00:00:00Z')

from . import reftypes as reftypes
from . import datatypes as datatypes
...
```

The URI, version and publication date come from the nodeset's `<Model>` element.

!!! warning "Regeneration replaces the package contents"
    Generated files are overwritten, and any other `.py` or `.pyi` file directly inside the package directory is deleted — including handwritten ones. Keep application code outside `mymodel/`.

---

## Step 2 — use it

The generated package registers itself on import. Put it anywhere on `sys.path`.
After the command above, run this from the directory containing `mymodel/`:

```python
--8<-- "docs/snippets/use-compiled-nodeset.py"
```

A server can then publish the generated model. This fragment assumes the XML
declares a structure named `MyStruct`; replace that name with your own type:

```python
import o6
import mymodel                       # registers 'mymodel' in o6.ns

server = o6.Server(port=4840)
server.ns.append(mymodel)             # publish it into the address space
# Publish before accepting client connections.
with server:
    input("Press Enter to stop the server\n")

value = mymodel.datatypes.MyStruct()
o6.NodeId("ns=mymodel;i=1")           # the shortname resolves
o6.ns.mymodel.index                   # also reachable through the registry
```

`o6.ns.mymodel` works even though the package is outside `o6/ns/`, because `_initialize_namespace` makes the importing module the namespace module for that shortname.

Clients need no extra step. They map the server's NamespaceArray by URI on connect; see [Loading & Using Nodesets](../sdk-fundamentals/namespace/loading-and-using-nodesets.md#appending-packaged-companion-specs).

---

## Step 3 — one dependency

Most nodesets build on another nodeset. Declare each dependency with its own `-e` flag so that cross-namespace parents resolve. For a companion specification bundled with the compiler, the bare shortname is enough:

```sh
pyncc path/to/MyDevice.NodeSet2.xml \
    --shortname mydevice \
    -e ns0 -e di \
    -o .
```

If you omit a dependency that the nodeset declares in its `<RequiredModel>`, compilation fails:

```
namespace http://opcfoundation.org/UA/DI/ has no supplied model binding
```

The generated source imports each dependency by the shortname you give it:

```python
# mydevice/objtypes.py
import o6.ns.ns0 as ns0
import o6.ns.di as di            # ← from -e di

@o6.objecttype(nodeId='ns=mydevice;i=1002', browseName='ns=mydevice;PumpType')
class PumpType(di.objtypes.DeviceType):
    ...
```

Because `di` is a bundled name, the generated code imports `o6.ns.di`, the package shipped in the runtime. For anything shipped in `o6/ns/`, use the bundled shortnames (`di`, `ia`, `machinery`, …).

At runtime, append dependencies to the server before the dependent nodeset:

```python
from o6.ns import di
import mydevice

server.ns.append(di)          # base first
server.ns.append(mydevice)
```

---

## Step 4 — a dependency chain

For deeper stacks, pass `-e` once per namespace in the transitive closure, not only the direct parents. Dependencies are never selected automatically. A machine-tool model needs DI, IA and Machinery:

```sh
pyncc path/to/MyMachine.NodeSet2.xml \
    --shortname mymachine \
    -e ns0 -e di -e ia -e machinery \
    -o .
```

Flag order does not matter: dependencies are resolved by the URI in each file's `<Model>` element. A generated address space contains at most one release per namespace URI. Several releases of the same URI can coexist in the process-wide `o6.ns` table under different shortnames.

A compiled package covers one namespace. Compile each nodeset separately and import all of them. `-e` only tells the compiler where to find the dependencies it resolves against.

### Dependencies you compiled yourself

Declare a dependency that is not a bundled companion specification as `shortname@parent.package=path/to.xml`. The parent package is the import prefix of the generated code, and the shortname is appended to it once:

| Declaration | Generated import |
|---|---|
| `-e 'base@myproject.ns=Base.NodeSet2.xml'` | `import myproject.ns.base as base` |
| `-e 'base@=Base.NodeSet2.xml'` | `import base as base` |

A model built on your own `base` package, compiled into `myproject/ns/`:

```sh
pyncc path/to/MyModel.NodeSet2.xml \
    --shortname mymodel \
    -e ns0 -e 'base@myproject.ns=path/to/Base.NodeSet2.xml' \
    -o ./myproject/ns
```

A bare XML path, or `SHORTNAME=PATH` without a package prefix, is rejected. The compiler needs to know what the generated module imports, not only where the XML is.

!!! warning
    A dependency's shortname must match the shortname it is registered under at runtime, and the prefix must match where its package lives. Neither is inferred from the filename or the Model URI. Reusing a bundled shortname for your own build of a stock specification produces a warning but continues; give it a distinct name instead.

---

## Step 5 — inspecting a nodeset first

To see what a model contains, for example when it fails to generate, use the `inventory` subcommand:

```sh
ncc inventory path/to/MyModel.NodeSet2.xml -e ns0 -o debug/inventory.json
```

It writes the parsed nodes and references as JSON. `ncc graphviz` renders the same information as a diagram.

---

## When generation fails

An unsupported node or node attribute fails compilation instead of producing a namespace that silently lacks part of the model. Exit status `2` means an argument or dependency-declaration error, `1` a generation failure. Common failures:

| Symptom | Cause |
|---|---|
| `namespace <uri> has no supplied model binding` | a `RequiredModel` dependency has no `-e` entry — including transitive ones |
| an unsupported-datatype or missing-ancestry diagnostic | the XML defining that datatype or its base types was not supplied |
| `uncached Description URL` | a URL-valued `<Description>` with no description-cache entry |
| `ModuleNotFoundError: o6` when importing the output | generation does not need the runtime, but running the result does |

Ordinary description text is emitted unchanged. A URL-valued description is substituted only from a cache you supply; the compiler never fetches the URL. Map each exact URL to its text in a JSON file and pass it:

```sh
pyncc path/to/MyModel.NodeSet2.xml \
    --shortname mymodel -e ns0 \
    --description-cache description_cache.json \
    -o .
```

Keep that cache beside your model inputs so generation stays reproducible.

---

## Related topics

| Topic | What it covers |
|---|---|
| [BrowseName to Python Names](../node-api/name-conversion.md) | Converting BrowseNames to Python identifiers. |
| [o6 NodeSet Compiler Collection](https://docs.o6-automation.com/o6-nodeset-compiler-collection/) | Compiler commands, options, and bundled companion specifications. |
| [Loading & Using Nodesets](../sdk-fundamentals/namespace/loading-and-using-nodesets.md) | Importing and using compiled namespaces. |
| [Namespace Mapping in o6\\Python](../sdk-fundamentals/namespace/namespace-mapping-in-o6.md) | The process-wide registry and shipped companion specifications. |
| [Nodeset Files & Companion Specs](../opcua-fundamentals/nodesets-and-companion-specs.md) | Nodeset files and the origins of companion specifications. |
| [Writing a Nodeset in Python](namespace-modules.md) | Declaring a nodeset in Python with `o6` decorators. |
| [Nodeset Authoring example](../../examples/type_authoring-T03_nodeset_authoring-example.md) | A complete hand-written nodeset and runnable client/server example. |
| [Implementing Object Behavior](implementing-types.md) | Attaching Method and Variable behaviour to declared types. |
| [Part 6, Annex F — Information Model XML Schema](https://reference.opcfoundation.org/Core/Part6/v105/docs/F) | The normative nodeset XML schema. |
