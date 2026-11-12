# Writing a Namespace Module

Write declarations in Python when you own the model. A namespace module can be
imported by a client to decode values and published by a server to create nodes.
If you already have XML, use [Compiling Nodesets](compiling-nodesets.md).

## The shape of a namespace module

A namespace module is an ordinary Python module with:

1. A call to `o6.ns.namespace(...)` at the top, which registers the namespace in the process-wide `o6.ns` table and records it in the module's `__NAMESPACES__`.
2. Decorated classes in the module body — one per type. Add them in the following pages.

Start `plant.py` with the following imports and namespace registration. Keep
this file beside the server and client scripts that import it:

```python
# plant.py
from typing import Optional

import o6
from o6.ns import ns0

o6.ns.namespace("plant", uri="http://example.org/Plant/", version="1.0")

```

Continue this file with the declarations on the following pages. The later
publishing example needs `TemperatureType`, `DriveType`, `MachineType`,
`CncMachineType`, and `Point`. Other types illustrate optional additions;
blocks marked as alternatives replace a declaration instead of being appended.
Runtime examples that create or read values belong in a separate script.

This complete `publish_plant.py` program publishes the module like a compiled
package. Run it after saving `plant.py`:

```python
import o6
import plant

server = o6.Server(port=4840)
server.ns.append(plant)
with server:
    input("Press Enter to stop the server\n")
```

Importing `plant` registers `o6.ns.plant` in that Python process, so
`ns=plant;i=…` can resolve in NodeId strings. Appending it publishes the model
on that server and adds its URI to the server's `NamespaceArray`.

`NamespaceArray` contains URI strings only. The shortname `plant` is local to
the SDK registry. The version is model metadata; a server can expose version
and publication-date information separately through `NamespaceMetadataType`
Objects. See [Namespace](../opcua-fundamentals/namespace.md#the-namespace-array)
for the standard table and
[Registry and Namespace Mapping](../sdk-fundamentals/namespace/namespace-mapping-in-o6.md)
for SDK metadata.

!!! tip
    In a single-file script, `server.ns.append(sys.modules[__name__])` publishes the types declared in the script itself. A separate importable module is still better: it keeps declarations out of the `if __name__ == "__main__"` path, and both a server and a client process can import it.

### Declaration order is dependency order

The following snippets illustrate dependency order and are alternatives to the
model declarations on subsequent pages. They do not all belong in `plant.py`.

A decorator runs when Python executes the `class` statement and resolves every reference at that moment. Declare a type before anything that names it:

```python
@o6.datatype(ns="plant")
class Point:
    x: float


@o6.datatype(ns="plant")
class BoundingBox:
    min: Point          # Point already exists — fine
    max: Point
```

The reverse order fails with an error instead of producing a half-built type:

```
TypeError: o6.datatype: cannot infer UA DataType for annotation ...
You have to declare types in dependency order: Type A must be declared
before Type B, if B has a field of type A.
```

The exception is self-reference. A type may name itself, because its NodeId is allocated before its fields are collected:

```python
@o6.datatype(ns="plant")
class Recursive:
    name: str
    children: list["Recursive"]
```

### NodeIds

Every decorator takes an optional `nodeId=`. If you omit it, o6 allocates the next free numeric identifier in the namespace. If you pass it, the type keeps that identifier.

```python
@o6.objecttype(ns="plant", nodeId="ns=plant;i=1001", browseName="MachineType")
class MachineType(ns0.objtypes.BaseObjectType):
    ...
```

Auto-allocation is fine while a model is private and always loaded from the same source. An auto-allocated identifier changes when you reorder declarations. Pin NodeIds explicitly as soon as the model is published, because clients that hard-code identifiers, historical data and stored configuration depend on them.

`browseName=` defaults to the Python class name. Set it when the UA BrowseName differs from the Python identifier. Qualify it (`"ns=plant;MachineType"`) when it belongs to a namespace other than the declaring one.

---
