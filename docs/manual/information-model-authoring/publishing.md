# Publishing & Instantiating Models

Publish a namespace module, then construct instances of its declared types.
The examples use `plant.py` from the preceding declaration pages.

## Publishing a module

`server.ns.append(module)` registers the module's namespaces and publishes its
declared nodes. Append dependencies first. Appending the same module twice is
a no-op. A module mixing already-published URIs and new URIs is rejected. When
a URI is already published, only its index alias is added: one address space
holds one release of a namespace URI.

The declaration pages extend `plant.py`; alternative examples are not intended
to be pasted into that file together. The following example uses its
`CncMachineType`, `TemperatureType`, and `Point` declarations.

## Using the types

Once the module is appended, the declared classes are the API. Calling one creates a live server node or returns a declaration, depending on which server owns the construction. The [ownership rules](#declared-type-instance-ownership) explain server selection.

### Instantiating

Save this complete program as `plant_server.py` beside `plant.py`. Run it with
`python plant_server.py`; it keeps the server available for the separate client
example below until you press Enter.

```python
# plant_server.py
import o6
import plant

server = o6.Server(port=4840)
server.ns.append(plant)

machine = plant.CncMachineType(
    parent=server.objects,
    browseName="M-101",
    nodeId="ns=plant;i=5001",
    values={
        "state": 1,
        "serial": "SN-001",
        "drive": {"manufacturer": "ACME", "current": 0.0},
        "temperature": plant.TemperatureType(
            server=None, value=19.0, values={"engineeringUnits": "degC"},
        ),
    },
)

with server:
    input("Press Enter to stop the server\n")
```

`values=` seeds the instance's children by Python member name:

- A *leaf* child takes a plain Python value.
- A *complex* child (one whose type declares children) takes a dict of its children, applied recursively. Passing a scalar is an error (`complex child 'drive' needs a DriveType declaration or a dict of values`).
- To seed a complex child's own value as well as its children, pass a detached declaration instead of a dict. This is the `values=` argument already used above, shown separately for explanation:

    ```python
    values={
        "temperature": plant.TemperatureType(
            server=None,                       # force a declaration
            value=19.0,                        # the Variable's own value
            values={"engineeringUnits": "degC"},
        ),
    }
    ```

Mandatory children are created even when they are absent from `values=`.
Optional children are omitted unless explicitly included. Naming an Optional
child in `values=` opts it in; for example, add `"highLimit": 80.0` to the
Temperature declaration's `values` to create its optional HighLimit Property.
The same rule applies recursively to Optional Objects and complex Variables.

### Reading and writing

The following optional fragments go in `plant_server.py` after constructing
`machine` and before the `with server:` block. Access children with dot notation.
A Variable node is callable: with no argument it reads, with one argument it writes.

```python
print(machine.serial())                 # SN-001
print(machine.drive.manufacturer())     # ACME
machine.drive.current(1.25)             # write
print(machine.temperature.engineeringUnits())  # degC

o6.NodeId(machine.drive.current)        # ns=… — the NodeId of any node handle
```

A structure-valued Variable reads back as the Python class, not as an `ExtensionObject`:

```python
origin = server.addVariable("Origin", server.objectsNode, plant.Point(1.0, 2.0, 3.0))
print(repr(server.read(origin)))        # Point(x=1.0, y=2.0, z=3.0)
```

### From a client

A client appends nothing. On connect it maps the server's NamespaceArray to the `o6.ns` table. If the client process imports the same `plant` module, its types decode and `ns=plant;…` NodeIds resolve:

Leave `plant_server.py` running. Save this complete client as `plant_client.py`
in the same directory and run it in a second terminal:

```python
# plant_client.py
import o6
import plant

with o6.Client("opc.tcp://localhost:4840") as client:
    machine = client["ns=plant;i=5001"]
    print(machine.serial())                         # SN-001
    print(machine.temperature.engineeringUnits())   # degC
```

The model declares `Reset`, but it needs behavior before it can be called.
[Implementing Declared Types](implementing-types.md) explains that step.
A client without the module still registers the namespace URI under its own
scope and can browse nodes and read built-in values. That identity registration
does not define custom structures; their values may remain opaque
`ExtensionObject`s. See
[Unknown namespaces and structured values](../sdk-fundamentals/namespace/loading-and-using-nodesets.md#unknown-namespaces-and-structured-values)
for the distinction.

---

## Declared type instance ownership

Calling an `@o6.objecttype` or `@o6.variabletype` class creates either a live
server node or an ordinary declaration instance. The optional `server` argument
is resolved in this order:

1. An explicit `server=<Server>` selects that server. An explicit
   `server=None` forces a declaration instance.
2. A live parent node selects the server that owns that node. A conflicting
   explicit server is rejected.
3. A declaration parent produces another declaration.
4. Calls made while a registered Python namespace module is being evaluated
   remain declarations; `server.ns.append(module)` materializes them later.
5. Otherwise, exactly one live server in the Python process is inferred.
6. With no live server, the result is a declaration. With multiple live servers,
   construction is ambiguous and raises `TypeError`; pass `server=` explicitly.

A bare `NodeId` does not identify a server, so it relies on the unique
live-server rule. `server.objectsNode` is a `NodeId`, not a node handle:

```python
# The only live server is inferred even though objectsNode is a NodeId.
other = plant.CncMachineType(parent=server.objectsNode, browseName="M-102")

# Always a normal declaration instance, regardless of live servers.
declaration = plant.CncMachineType(server=None)
```

With a second live server in the process, the same call fails with
`cannot infer server: multiple live servers exist; pass server=<server> or
server=None explicitly`. Pass `server=server` to fix it.

This fragment also belongs before `with server:` in `plant_server.py`.
Declarations evaluated inside `plant.py` stay ordinary Python objects even
when a server exists. The [model-instance example](references-and-instances.md#model-instances)
shows a folder declaration that `server.ns.append(plant)` publishes later.
