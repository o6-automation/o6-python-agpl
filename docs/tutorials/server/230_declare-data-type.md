# Declare a data type

Every value in the distillery so far has fit one of a handful of built-in types — strings, doubles, ints, booleans. That's plenty for a `Setpoint` or a `Name`, but it starts to strain on a value like the still's current `State`, which is really only ever one of five things: `Idle`, `Filling`, `Heating`, `Distilling`, `Draining`. Encoding that as a free-form string would work, technically, but it wouldn't say anything true about the value — a string field carries no declared set of legal values at all, so nothing in the model states what a valid `State` even is. The shape that actually fits is an `Enum` DataType: a named, closed set of values that the model, and any tooling reading it, can see explicitly.

This page declares a `StillState` enum and uses it as the DataType for the distillery's `Status.State` — the last stop in this tour of declaring things up front instead of building them by hand.

---

## Why declare a data type?

Two reasons:

1. **The wire format.** Encoding `"Distilling"` as a 16-byte UTF-8 string every time is wasteful. Encoding it as an `Int32` enum value is one byte. The DataType drives both the encoding and the visible shape of the value on the wire.
2. **A discoverable, closed set of values.** Once `StillState` is a UA `Enum` DataType, a read of the *data type* node shows exactly the allowed values, instead of a free-form string field that documents nothing. The enum DataType is metadata the server publishes; it does not by itself stop a client from writing an out-of-range integer — enforcing that boundary at write time is application logic, the same `Server.implement(variable, write=...)` validation covered on the [Variables with sources](320_variables-with-sources.md) page.

The same shape works for `Structure` types — anything a vendor's spec calls a "complex data type" is a UA Structure DataType.

---

## Declare an Enum with `@o6.enumtype`

Start with `State`, since it's the value that motivated this page. Enumerations use `@o6.enumtype`, not `@o6.datatype` — `@o6.datatype` is for Structures, and raises `TypeError` on a bare class-body assignment like `IDLE = 0`. A decorated `@o6.enumtype` class becomes a real `IntEnum`; the class body just lists the values, and each becomes a member:

```python
import o6
from o6.ns import ns0

o6.ns.namespace(
    shortname="distillery",
    uri="http://o6-automation.com/UA/Distillery/",
    version="1.0",
)


@o6.enumtype(ns="distillery", nodeId="ns=distillery;i=5000", browseName="StillState", description="The distillery's batch state machine")
class StillState:
    IDLE = 0
    FILLING = 1
    HEATING = 2
    DISTILLING = 3
    DRAINING = 4
```

The class body's assignments become the enum values — `StillState.IDLE == 0`, `StillState.DISTILLING == 3`, and so on. The server publishes the data type under `ns=distillery;i=5000`, and the values are read with the standard `Value` attribute path. `o6.enumfield(value, description=..., displayName=..., name=...)` adds per-member UA metadata when a bare integer isn't enough — the two forms mix freely in one class:

```python
@o6.enumtype(ns="distillery", nodeId="ns=distillery;i=5000", browseName="StillState")
class StillState:
    IDLE = 0
    FILLING = o6.enumfield(1, description="tank is filling")
    HEATING = 2
    DISTILLING = 3
    DRAINING = 4
```

For an OPC UA enum, the integer values themselves are the wire encoding — `StillState.DISTILLING` is `Int32(3)` on the wire. The DataType node documents which integers are legal; it does not by itself make the server reject an out-of-range one. A read of an in-range value comes back as the Python enum member (`StillState.IDLE`), and enforcing the boundary on writes — rejecting `5` before it reaches the nodestore — is application logic, covered on the [Variables with sources](320_variables-with-sources.md) page.

---

## Use the data type as a Variable's `dataType`

Declared on its own, `StillState` is still just metadata sitting in the namespace — it needs to be attached to an actual Variable before it means anything for the distillery. The new type plugs into the `dataType=` keyword of `addVariable`, taking the declared class directly:

```python
import sys
import time
import o6
from o6 import Server
from o6.ns import ns0

o6.ns.namespace(
    shortname="distillery",
    uri="http://o6-automation.com/UA/Distillery/",
    version="1.0",
)


@o6.enumtype(ns="distillery", nodeId="ns=distillery;i=5000", browseName="StillState")
class StillState:
    IDLE = 0
    FILLING = 1
    HEATING = 2
    DISTILLING = 3
    DRAINING = 4


server = Server(port=4840)
server.ns.append(sys.modules[__name__])     # publish the enum's namespace before using it

distilling_system = server.addObject("DistillingSystem", server.objectsNode, nodeId="ns=1;i=1000")
status = server.addObject("Status", distilling_system, nodeId="ns=1;i=1200")

# `dataType=` takes the declared enum class directly
state = server.addVariable(
    "State",
    status,
    int(StillState.IDLE),      # initial value, as the underlying Int32
    nodeId="ns=1;i=1201",
    dataType=StillState,
    writable=False,
)

server.start()
```

`server.ns.append(...)` has to run before `dataType=StillState` is resolved — the DataType node only exists on a server once its namespace has been published there. The server publishes `Status.State` with the new data type, and the initial value `0` reads back as `StillState.IDLE`. As above, the DataType alone does not stop a write of an out-of-range integer — that validation is something a write callback adds explicitly.

!!! info
    The same enum works as an input argument on a method: declare `Argument(dataType=StillState, valueRank=ValueRank.SCALAR)` and `o6` rejects an argument of the wrong UA DataType before the callback runs — the same structural check any other typed argument gets, not a bounds check against the enum's members.

#### Putting it all together

```python
import sys
import time
import o6
from o6 import Server
from o6.ns import ns0

o6.ns.namespace(
    shortname="distillery",
    uri="http://o6-automation.com/UA/Distillery/",
    version="1.0",
)


@o6.enumtype(ns="distillery", nodeId="ns=distillery;i=5000", browseName="StillState")
class StillState:
    IDLE = 0
    FILLING = 1
    HEATING = 2
    DISTILLING = 3
    DRAINING = 4


server = Server(port=4840)
server.ns.append(sys.modules[__name__])
distilling_system = server.addObject("DistillingSystem", server.objectsNode, nodeId="ns=1;i=1000")
status = server.addObject("Status", distilling_system, nodeId="ns=1;i=1200")
server.addVariable(
    "State",
    status,
    int(StillState.IDLE),
    nodeId="ns=1;i=1201",
    dataType=StillState,
    writable=False,
)

server.start()
```

---

## Declare a Structure DataType

`StillState` covers a closed set of named values, but not every custom value is a choice among a handful of options — some are a small bundle of fields that belong together, like a summary of one finished batch. The same declarative pattern works for those compound types too, just with the other decorator: a `Structure` DataType has fields with names and types, and `@o6.datatype` reads a **plain type annotation** as the field's DataType — there is no separate field-declaration factory for the type itself. Extra metadata that the annotation can't express (a description, an optional field, a max string length) is layered on with `o6.field(...)`:

```python
import o6
from o6.ns import ns0

o6.ns.namespace(
    shortname="distillery",
    uri="http://o6-automation.com/UA/Distillery/",
    version="1.0",
)


@o6.datatype(ns="distillery", nodeId="ns=distillery;i=5010", browseName="BatchSummary", description="A summary of one completed batch")
class BatchSummary:
    cycle: int              # Int64 by default; use o6.UInt32 for the exact width
    yield_l: float           # litres
    duration_s: int          # seconds
```

`BatchSummary` is a three-field structure with `cycle`, `yield_l`, and `duration_s` — the annotation on each attribute *is* its DataType, the same way it is for a struct field anywhere else in `o6`. On the wire it is an ExtensionObject the server publishes under `ns=distillery;i=5010`.

To pin the exact integer width instead of the default `Int64`, annotate with one of the sized `o6` aliases, and add `o6.field(...)` where a plain annotation isn't enough:

```python
@o6.datatype(ns="distillery", nodeId="ns=distillery;i=5010", browseName="BatchSummary")
class BatchSummary:
    cycle: o6.UInt32
    yield_l: float = o6.field(description="litres produced")
    duration_s: o6.UInt32
```

Structure DataTypes are useful for the values a single Variable holds when a simple scalar isn't enough — readings with metadata, summaries, command payloads.

---

## What's next?

That's the data type story done, and with it the last of these model-first pages. The distillery now has declared types for its objects, its variables, the relationships between them, and the values themselves. What's left is behaviour: reacting to writes, calling methods, and reading values that come from somewhere other than the nodestore — the subject the next pages turn to.

- [Method implementations](310_method-implementations.md) — installing and swapping the Python callbacks that give Methods their behaviour.
- [Writing a Nodeset in Python](../../manual/sdk-fundamentals/namespace/writing-nodesets-in-python.md#o6datatype-structures) — the full DataType story, including field metadata, inheritance, Unions, and (further down) [enum value handling](../../manual/sdk-fundamentals/namespace/writing-nodesets-in-python.md#o6enumtype-enumerations).
