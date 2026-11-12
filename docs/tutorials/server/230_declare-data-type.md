# Declare a data type

The still's `State` is always one of five values: `Idle`, `Filling`, `Heating`, `Distilling`, `Draining`. A string DataType declares no set of legal values. An `Enum` DataType declares a named, closed set that the model and any tooling reading it can see.

This page declares a `StillState` enum, uses it as the DataType of `Status.State`, and then declares a `Structure` DataType.

---

## Why declare a data type?

1. **The wire format.** Encoding `"Distilling"` as a 16-byte UTF-8 string every time is wasteful. Encoding it as an `Int32` enum value is one byte. The DataType drives both the encoding and the shape of the value on the wire.
2. **A discoverable, closed set of values.** A read of the `StillState` DataType node shows exactly the allowed values. The DataType is metadata only. It does not stop a client from writing an out-of-range integer; enforce that in a write callback with `Server.implement(variable, write=...)`, covered on [Variables with sources](320_variables-with-sources.md).

The same applies to `Structure` types. What a vendor's specification calls a "complex data type" is an OPC UA Structure DataType.

---

## Declare an Enum with `@o6.enumtype`

Declare enumerations with `@o6.enumtype`. `@o6.datatype` is for Structures and raises `TypeError` on a bare class-body assignment such as `IDLE = 0`. The decorated class becomes an `IntEnum`, and each assignment in the class body becomes a member:

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

`StillState.IDLE == 0`, `StillState.DISTILLING == 3`, and so on. The server publishes the DataType under `ns=distillery;i=5000`, and values are read through the standard `Value` attribute. To add per-member metadata, use `o6.enumfield(value, description=..., displayName=..., name=...)`. Bare integers and `o6.enumfield` mix in one class:

```python
@o6.enumtype(ns="distillery", nodeId="ns=distillery;i=5000", browseName="StillState")
class StillState:
    IDLE = 0
    FILLING = o6.enumfield(1, description="tank is filling")
    HEATING = 2
    DISTILLING = 3
    DRAINING = 4
```

The integer values are the wire encoding: `StillState.DISTILLING` is `Int32(3)` on the wire. A read of an in-range value returns the Python enum member (`StillState.IDLE`). The server does not reject an out-of-range value such as `5`; rejecting it before it reaches the nodestore is application logic, covered on [Variables with sources](320_variables-with-sources.md).

---

## Use the data type as a Variable's `dataType`

Pass the declared class to the `dataType=` keyword of `addVariable`:

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

Call `server.ns.append(...)` before `dataType=StillState` is resolved. The DataType node exists on a server only after its namespace is published there. `Status.State` reads back its initial value `0` as `StillState.IDLE`.

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

A `Structure` DataType bundles named, typed fields, such as a summary of one finished batch. Declare it with `@o6.datatype`. A plain type annotation sets each field's DataType; there is no separate factory for the type. Add metadata the annotation can't express (a description, an optional field, a max string length) with `o6.field(...)`:

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

The server publishes `BatchSummary` under `ns=distillery;i=5010`. On the wire a value is an ExtensionObject.

To pin an integer width instead of the default `Int64`, annotate with a sized `o6` alias:

```python
@o6.datatype(ns="distillery", nodeId="ns=distillery;i=5010", browseName="BatchSummary")
class BatchSummary:
    cycle: o6.UInt32
    yield_l: float = o6.field(description="litres produced")
    duration_s: o6.UInt32
```

Use a Structure DataType when one Variable holds more than a scalar: readings with metadata, summaries, command payloads.

---

## Next steps

The next pages add behaviour: method callbacks, write handling, and values that come from outside the nodestore.

| Topic | What it covers |
|---|---|
| [Method implementations](310_method-implementations.md) | Installing and swapping the Python callbacks that give Methods their behaviour. |
| [Writing a Nodeset in Python](../../manual/information-model-authoring/datatypes.md#o6datatype-structures) | The full DataType story, including field metadata, inheritance, Unions, and (further down) [enum value handling](../../manual/information-model-authoring/datatypes.md#o6enumtype-enumerations). |
