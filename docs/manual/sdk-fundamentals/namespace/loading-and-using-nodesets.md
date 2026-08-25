# Loading & Using Nodesets

An application still has to declare that it uses types and objects from a specific nodeset specification. In the following we discuss how this is done for packaged companion specs and custom nodesets.

!!! info
    For what a nodeset file actually is, how companion specs relate to it, and
    how nodesets declare their dependencies, see
    [Nodeset Files & Companion Specs](../../opcua-fundamentals/nodesets-and-companion-specs.md)
    in OPC UA Fundamentals.

Conceptually o6\\Python injects a layer of abstraction between the step for loading nodesets and then actually using them.

```
Nodeset modules               o6.ns                        Server
  (imports)                (global index)                (local index)
                                                  
               imports                     appends            A
//───┐                       ┌─────┬───────────────────────── 2
│ di │ ────────────────────► │  2  ├───┐               ┌───── 3
└────┘                       └─────┘   |               | ┌─── 4
//───┐                       ┌─────┐   |               | |
│ ia │ ────────────────────► │  3  ├───────────────────┘ |
└────┘                       └─────┘   |                 |
//───────┐                   ┌─────┐   |                 |
│ custom ├ ─────────────┬──► │ 129 ├─────────────────────┘
└────────┘              |    └─────┘   |                      B
                        |    ┌─────┐   └───────────────────── 2
                        └──► │ 130 ├───────────────────────── 3
                             └─────┘
```

The graph shows that nodeset modules are first loaded.
Loading provisions the process wide global `o6.ns` creating a table entry for them.
A Server that wants to use these loaded nodesets then appends them. Server **A** appended `di`, `ia` and `custom`; server **B** appended `di` and an older release of the same custom nodeset — two table entries under distinct shortnames for one URI. The same table entry ends up at a different local index on each server, and none of those indices appear in your code.

The global table can then track namespaces transparently and is able to translate *local* server indices to *global* indices, valid to use with all clients and servers in this process.

!!! note
    From within o6\\Python you will likely never need to know the actual local namespace index on the server. Instead you deal with the globally unique indices or better yet the human-readable shortname.

---

## Appending packaged companion specs

Packaged companion specs are compiled Python packages under `o6/ns/`. A namespace is brought into the process with ordinary Python import syntax:

```python
import o6
from o6.ns import di            # or: import o6.ns.di
```

Behind `di` is a `NamespaceModule` — a real Python module carrying all the information described in [Namespace Mapping in o6\\Python](namespace-mapping-in-o6.md).

A **server** publishes the namespace into its address space by appending the module:

```python
server = o6.Server(port=4840)
server.ns.append(di)
server.start()
```

`append` registers every namespace the module declares (its `__NAMESPACES__` set) with the server's NamespaceArray and then injects the module's nodes and datatypes. It is idempotent — appending the same module twice is a no-op.

!!! warning
    Dependencies are **not** resolved for you. A companion spec whose types inherit from another spec's types needs its dependency appended first:

    ```python
    from o6.ns import di, ia   # IA builds on DI

    server.ns.append(di)       # base first
    server.ns.append(ia)
    ```

    Appending `ia` alone does not fail, but DI never reaches the NamespaceArray and the DI-derived parts of the IA model are incomplete.

A **client** does *not* append anything. There is no `client.ns`. On connect the client reads the server's NamespaceArray and maps each advertised URI onto the matching entry in the process-wide `o6.ns` table:

```python
client = o6.Client("opc.tcp://localhost:4840")
client.connect()

# The server's local index for DI is irrelevant — address by shortname.
value = client.read("ns=di;i=15889")
```

If a server adds namespaces at runtime, call `client.updateRemoteNamespaces()` to rebuild the mapping. Unchanged snapshots are not rebuilt, so calling it again is cheap.

When several compiled releases of the same URI are registered, the client reads the server's `NamespaceMetadata` (`NamespaceVersion`, `NamespacePublicationDate`) and picks the exact version, falling back to the newest registered release and logging a warning if the server is newer than anything the client has. A URI the client knows nothing about stays a plain numeric index and is logged as a warning.

### Namespace modules load lazily

Every packaged companion spec is registered in `o6.ns` — with its shortname, URI, version and global index — as soon as `o6` is imported. The generated declarations are only executed on **first attribute access**:

```python
o6.ns.di.__dict__["_o6_loaded"]     # False — registered, not yet loaded
o6.ns.di.objtypes.DeviceType        # triggers the load
o6.ns.di.__dict__["_o6_loaded"]     # True
```

This keeps startup cheap with well over a hundred namespaces registered, and it is transparent: naming anything inside a namespace loads it.

!!! warning
    Because the trigger is attribute access, a bare `import o6.ns.di` (or `from o6.ns import di`) does **not** by itself execute the module — the placeholder is already in `sys.modules`. Structured `DataType`s are registered with the codec when the module loads, so a client that never touches a declaration decodes that namespace's structs as opaque `ExtensionObject`s:

    ```python
    import o6.ns.ia
    client.read(node)          # → o6.ExtensionObject(typeId='ns=ia;i=5009', body=b'...')

    o6.ns.ia.datatypes         # force the load
    client.read(node)          # → RGBWDataType
    ```

    Normal code hits this by accident only when it reads values whose types it never names in Python. Touch the category module (or the type itself) before connecting if that is your case.

---

## Loading nodesets from XML

Runtime parsing of `*.NodeSet2.xml` is **not currently supported**. Instead the nodeset is compiled ahead of time into a Python package with the nodeset compiler, and that package is imported exactly like a packaged companion spec — into the same `o6/ns/` folder if you want `o6.ns.<shortname>` attribute access, or anywhere else on `sys.path`.

See [Compiling Nodesets](compiling-nodesets.md) for the full workflow.

!!! info
    Runtime XML loading may return in a future release. Precompiling is nevertheless the encouraged path:

    - **Ergonomics.** A compiled namespace is ordinary Python: editor autocomplete, jump-to-definition, and type checkers all work. The generator also emits `.pyi` stubs for the datatype modules, so struct fields keep their exact OPC UA types. A nodeset parsed at runtime can offer none of that — a typo in a type name is a `KeyError` at runtime rather than a red squiggle and catchable error by `mypy` or any other type checker.
    - **Performance.** Importing a compiled namespace takes a couple of milliseconds; parsing, merging and validating the equivalent XML takes seconds and repeats on every process start. Compiling is a build step you pay for once.
    - **Determinism.** Generation fails closed on anything the backend cannot represent faithfully, so an unsupported construct is a compile error rather than a silently incomplete address space.

---

## Accessing namespace content

A namespace module exposes its address space through five generated category submodules:

| Category | Contains |
|---|---|
| `reftypes` | `ReferenceType` declarations |
| `datatypes` | structures, enums, unions |
| `vartypes` | `VariableType` declarations |
| `objtypes` | `ObjectType` declarations |
| `instances` | `Object` / `Variable` / `Method` instance declarations |

```python
import o6

dt = o6.ns.di.datatypes.TransferResultDataDataType   # a struct class
value = dt()                                         # {sequenceNumber=0, endOfResults=False, parameterDefs=[]}
value.sequenceNumber = 42

health = o6.ns.di.datatypes.DeviceHealthEnumeration  # an enum
health.NORMAL                                        # 0

DeviceType = o6.ns.di.objtypes.DeviceType            # a decorated type class
o6.NodeId(DeviceType)                                # ns=di;i=1002

ConnectsTo = o6.ns.di.reftypes.ConnectsTo
o6.NodeId(ConnectsTo)                                # ns=di;i=6030
```

Declarations are **flat within their category** — inheritance is plain Python inheritance, not attribute nesting:

```python
issubclass(
    o6.ns.di.datatypes.TransferResultDataDataType,
    o6.ns.di.datatypes.FetchResultDataType,           # abstract parent, same module
)
```

The category modules are also importable directly, which is what you want for tab completion in a REPL and for short names in application code:

```python
import o6.ns.di.objtypes as diot
from o6.ns.di import datatypes as didt
from o6.ns import ns0

req = ns0.datatypes.ReadRequest()
nodeId = o6.NodeId(diot.DeviceType)
```

Only the category modules are packages' submodules — a declaration is not. `import o6.ns.di.datatypes.TransferResultDataDataType` raises `ModuleNotFoundError`; use `from o6.ns.di.datatypes import TransferResultDataDataType`.

### Namespace metadata

Metadata lives directly on the module and is available before the declarations load:

```python
di = o6.ns.di
di.shortname          # 'di'
di.uri                # 'http://opcfoundation.org/UA/DI/'
di.version            # '1.05.0'
di.publicationDate    # '2025-11-15T00:00:00Z'
di.scope              # '::global'
di.index              # the process-global index — assigned at registration,
                      #   stable within a process, not something to hard-code
repr(di)              # <o6 namespace 'di' version='1.05.0' uri='http://opcfoundation.org/UA/DI/'>
```

Shortname, URI, version, scope and index come from the registry and are readable while the module is still a lazy placeholder. `publicationDate` is filled in by the module itself, so it reads `''` until the namespace has loaded.

### Instances

Instance declarations that carry a usable BrowseName get a lowerCamelCase Python name:

```python
device_set = o6.ns.di.instances.deviceSet
o6.NodeId(device_set)                 # ns=di;i=5001
```

Names are derived mechanically from the BrowseName, so placeholder or URI-shaped BrowseNames produce deliberately unattractive identifiers (`langleCPIdentifierRangle` for `<CPIdentifier>`). Declarations that have no hierarchical parent may have no public name at all. For both cases, look the declaration up by NodeId instead of depending on a generated name.

### Looking up a declaration by NodeId

The `o6.ns` registry itself is subscriptable:

```python
declaration = o6.ns["ns=di;i=5001"]

# A NodeId object works too.
o6.ns[o6.NodeId("ns=di;i=5001")]

# As with every NodeId string, an omitted namespace means namespace 0.
root = o6.ns["i=84"]

# An integer key returns the namespace module for that global index.
o6.ns[o6.ns.di.index]                 # <o6 namespace 'di' ...>
```

For a type node the lookup returns the decorated type class; for an instance node it returns the registered instance declaration. Either accepts `o6.NodeId(...)`. The lookup reads the compiled namespace, **not** a live server — use `client[nodeid]` when you need a typed node bound to a server. It raises `KeyError` for a NodeId the generator emitted no declaration for.

Brackets are for indices and NodeIds only; a bare shortname raises `TypeError` and points you at attribute access:

```python
o6.ns["di"]        # TypeError: use o6.ns.di for namespace shortname access; ...
```

The index is built lazily from the loaded namespace module and cached. It is therefore independent of generated backing names such as `__property_2` and does not add lookup tables to every generated module.

### Querying the registry

```python
print(o6.ns)                          # the formatted table (see Namespace Mapping)
len(o6.ns)                            # number of registered namespaces
list(o6.ns)                           # ['ns0', 'amb', 'aml', ...] — shortnames
"di" in o6.ns                         # True — shortname membership
"ns=di;i=5001" in o6.ns               # True — declaration membership

o6.ns.filter(uri="http://opcfoundation.org/UA/DI/")
o6.ns.filter(version="1.05.0")
o6.ns.filter(scope="::global")
o6.ns.filter()                        # every entry, as NamespaceModule objects
```

`filter()` is the programmatic counterpart to printing the table — use it for URI, scope or version queries, and attribute access for shortnames.

### Registering a namespace by hand

A hand-written nodeset module declares its namespace with `o6.ns.namespace(...)`, which also records it in the calling module's `__NAMESPACES__` so `server.ns.append` can find it:

```python
o6.ns.namespace("myns", uri="http://o6.example.org/Myns/", version="1.0")
```

`o6.ns.register(...)` does the same registration and returns the module without touching the caller, for the rare case where you only need a table entry:

```python
module = o6.ns.register("myns", "http://o6.example.org/Myns/", version="1.0")
module.index
```

See [Writing a Nodeset in Python](writing-nodesets-in-python.md) for the full authoring guide, and [`examples/nodeset/myns.py`](https://github.com/o6-automation/o6-python-agpl/blob/main/examples/nodeset/myns.py) for a complete hand-written nodeset module.

---

## Practical use of shortname

Once a namespace is registered, its `shortname` becomes a stable handle you can carry around in code, copy-paste into config files, and reason about without thinking about server-assigned indices. The `shortname` is what `o6.ns.di`, `o6.ns.machinery`, `o6.ns.custom`, … resolve to — and the same string also goes into every `NodeId` string you write.

A `NodeId` accepts a registered shortname in its `ns=…` form. The `nsu=…`
form is reserved for a full namespace URI, optionally qualified by scope and
version:

````python
# URI form — full namespace URI
n1 = o6.NodeId("nsu=http://opcfoundation.org/UA/DI/;i=1")

# Shortname form — same NodeId, much easier to type
n2 = o6.NodeId("ns=di;i=1")

# URI + scope + version — for when several versions of the same nodeset
# live side by side
n3 = o6.NodeId("nsu=http://opcfoundation.org/UA/DI/@::global!1.05.0;i=1")

# Numeric form still works — but the index is the *global* one, not the
# index the server put on the wire
n4 = o6.NodeId(f"ns={o6.ns.di.index};i=1")
````

All four normalise to the same textual form, `ns=di;i=1`. `QualifiedName` accepts the shortname the same way:

````python
o6.QualifiedName("ns=di;DeviceSet")   # di:DeviceSet
````

A `NodeId` exposes its resolved namespace through `.ns`. Unknown or
application-local namespaces remain numeric indices:

````python
n = o6.NodeId("ns=di;i=1")

n.ns                                # → o6.ns.di
n.ns.index                          # → process-global index
n.ns.shortname                      # → 'di'
n.ns.uri                            # → 'http://opcfoundation.org/UA/DI/'
n.ns.version                        # → '1.05.0'
n.ns.publicationDate                # → '2025-11-15T00:00:00Z'
n.ns.scope                          # → '::global'

o6.NodeId("ns=1;i=1").ns            # → 1, the application-local namespace
````

!!! tip
    Prefer `ns=<shortname>` or `nsu=<uri>` over numeric indices in source code. Numeric namespace forms are global indices assigned in registration order — they are stable within a process, but not something to hard-code, and never the same as the index a server puts on the wire.

---

## See also

- Compile a `*.NodeSet2.xml` into an importable namespace package:
  [Compiling Nodesets](compiling-nodesets.md).
- Declare a namespace and its types entirely in Python, with no XML involved:
  [Writing a Nodeset in Python](writing-nodesets-in-python.md), and
  [Implementing Object Behavior](implementing-object-behavior.md) for the behavior behind them.
- The OPC UA spec's normative treatment of the nodeset format (`UANodeSet` schema, `RequiredModel`, `<DataTypeDefinition>` / `<StructureDefinition>` / `<EnumDefinition>` / `<UnionDefinition>`):
  [Part 6, Annex F — Information Model XML Schema](https://reference.opcfoundation.org/Core/Part6/v105/docs/F).
- The XML schemas themselves, versioned alongside the spec:
  [`OPCFoundation/UA-Nodeset`](https://github.com/OPCFoundation/UA-Nodeset).
- How a server publishes its URI ↔ index table and where `ns=1` (the local Server) is reserved:
  [Namespace](../../opcua-fundamentals/namespace.md),
  [Part 5, §6.3.1 — ServerType](https://reference.opcfoundation.org/Core/Part5/v105/docs/6.3.1),
  and [Part 3, §4.2 — URIs](https://reference.opcfoundation.org/Core/Part3/v105/docs/4.2).
- How a loaded nodeset becomes Python types via the C extension's type-registration table:
  [DataType](../../opcua-fundamentals/datatype.md) and
  [Address & Identity Types](../builtin/address-types.md).
- The official list of companion specifications and their nodeset files:
  [OPC UA Companion Specifications](https://opcfoundation.org/about/opc-partners/opc-unified-architecture/opc-ua-companion-specifications/).
- Continue with the process-wide view of namespaces in o6:
  [Namespace Mapping in o6\\Python](namespace-mapping-in-o6.md).
