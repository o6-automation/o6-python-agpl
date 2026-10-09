# Declare a variable type

The previous page gave the whole distillery a type of its own, so the server could produce as many identical stills as the plant ever needs. The same habit of thought works at a much smaller scale too — on a single value. Take `Setpoint`: it isn't really just a `Double`. It has units (degrees Celsius), a sensible operating range, an EngineeringUnits field — metadata that turns "a number" into "a temperature" an operator can actually trust. None of that context lives anywhere in the model yet; it would only ever live in a comment, or in whatever a client happens to assume. This page declares a custom `VariableType` and uses it as the type definition of a `Setpoint`-shaped Variable, so that metadata travels with the value instead of living outside it.

By the end of this page, a `Setpoint` is a typed Variable with engineering metadata carried on the *type*, not repeated on every instance.

!!! info
    Looking for read/write *behaviour* on a declared Variable — validation, clamping — rather than metadata? [Declare and implement a Variable](150_implement-variable.md), earlier in these tutorials, pairs a declared Variable with a separate implementer class using exactly the `Setpoint`-clamping example this page's `Setpoint` is named after.

---

## Declare a VariableType with `@o6.variabletype`

`@o6.variabletype` declares a UA `VariableType` — a template for Variables whose DataType, ValueRank, and other metadata come from the type rather than from each individual node.

```python
import o6
from o6.ns import ns0

o6.ns.namespace(
    shortname="distillery",
    uri="http://o6-automation.com/UA/Distillery/",
    version="1.0",
)


@o6.variabletype(
    ns="distillery",
    nodeId="ns=distillery;i=3000",
    browseName="TemperatureType",
    dataType=float,            # Double
    valueRank=o6.ValueRank.SCALAR,
)
class TemperatureType(ns0.vartypes.BaseDataVariableType):
    """A temperature, in degrees Celsius, with an EngineeringUnits property."""
```

`@o6.variabletype(...)` declares a UA VariableType whose instances are scalar `Double`s. The class body can declare further children — typically the `EngineeringUnits` and `Range` companion-spec properties that turn a `Double` into a real engineering value.

The declared class is the type. To get a typed instance, you construct `TemperatureType(...)` directly, or annotate a leaf inside another declared type with `TemperatureType` — either way `o6` resolves the value's DataType, ValueRank and children from the class.

!!! info
    VariableType and ObjectType declarations live in the same namespace table. The shortname `distillery` is registered once and reused.

---

## Add `EngineeringUnits` and `Range` properties

A "temperature" without units is just a number. The OPC UA companion specs define `EUInformation` and `Range` as the standard ways to attach units and an engineering range to a value. Declaring them on the type means every instance inherits them automatically.

```python
import o6
from o6.ns import ns0

o6.ns.namespace(
    shortname="distillery",
    uri="http://o6-automation.com/UA/Distillery/",
    version="1.0",
)


@o6.variabletype(
    ns="distillery",
    nodeId="ns=distillery;i=3000",
    browseName="TemperatureType",
    dataType=float,
    valueRank=o6.ValueRank.SCALAR,
)
class TemperatureType(ns0.vartypes.BaseDataVariableType):
    """A temperature in degrees Celsius, with EUInformation and Range."""

    engineeringUnits: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            browseName="ns=distillery;EngineeringUnits",
            nodeId="ns=distillery;i=3001",
            dataType="i=887",       # EUInformation
        )
    )

    instrumentRange: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            browseName="ns=distillery;InstrumentRange",
            nodeId="ns=distillery;i=3002",
            dataType="i=884",       # Range
        )
    )
```

Two `hasProperty` children: `EngineeringUnits` (an `EUInformation`) and `InstrumentRange` (a `Range`). Both are declared as `ns0.vartypes.PropertyType` instances — a leaf Property is always constructed directly from the concrete VariableType it should be, never from a separate "variable" helper. They ride along on every instance of `TemperatureType`. The values are read by the same `Value` attribute path used for any other Variable, and a reader that knows the OPC UA companion specs can recognise "this is a Celsius temperature with a defined engineering range" by inspecting the `EngineeringUnits` value.

!!! info
    The DataType identifiers — `i=887` for `EUInformation`, `i=884` for `Range` — come from the standard OPC UA namespace (`ns0`). They are part of the base types every server publishes, so no extra nodeset import is needed. `dataType=` accepts either a NodeId string like this or a Python type such as `float`; both resolve to the same UA DataType.

---

## Use the type as a `typeDefinition`

`TemperatureType` is fully declared now — DataType, EngineeringUnits, InstrumentRange, all in one place — but declaring it doesn't put anything on a server yet. With `TemperatureType` declared, a Variable can be constructed with `TemperatureType` as its type definition wherever the imperative `addVariable` would hold a bare `Double`. The declarative route constructs the class directly:

```python
setpoint = TemperatureType(
    parent=server.objectsNode,
    browseName="Setpoint",
    nodeId="ns=distillery;i=1204",
    value=85.0,
    server=server,     # required when this script also declared the namespace — see the note on the ObjectType page
)
```

`setpoint` is now a `Double` Variable whose `HasTypeDefinition` points at `TemperatureType` — its `EngineeringUnits` and `InstrumentRange` properties come along automatically, because they are declared on the type. The instance still owns its own value (`85.0`).

The imperative equivalent uses `addVariable(typeDefinition=...)`, passing the declared class itself as the type:

```python
setpoint = server.addVariable(
    "Setpoint",
    server.objectsNode,
    85.0,
    nodeId="ns=1;i=1204",
    typeDefinition=TemperatureType,
    writable=True,
)
```

`typeDefinition=` accepts the declared class directly (or the equivalent NodeId string, `"ns=distillery;i=3000"`). Either way, a `browse` that follows `HasTypeDefinition` from `Setpoint` lands on `TemperatureType`, reads `EngineeringUnits` from the type, and decodes the value's units and range without them being declared on every instance.

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


@o6.variabletype(
    ns="distillery",
    nodeId="ns=distillery;i=3000",
    browseName="TemperatureType",
    dataType=float,
    valueRank=o6.ValueRank.SCALAR,
)
class TemperatureType(ns0.vartypes.BaseDataVariableType):
    engineeringUnits: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            browseName="ns=distillery;EngineeringUnits",
            nodeId="ns=distillery;i=3001",
            dataType="i=887",
        )
    )
    instrumentRange: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            browseName="ns=distillery;InstrumentRange",
            nodeId="ns=distillery;i=3002",
            dataType="i=884",
        )
    )


@o6.objecttype(ns="distillery", nodeId="ns=distillery;i=1000", browseName="DistillingSystemType")
class DistillingSystemType(ns0.objtypes.BaseObjectType):
    setpoint: TemperatureType = o6.hasComponent(
        TemperatureType(
            browseName="ns=distillery;Setpoint",
            nodeId="ns=distillery;i=1204",
            value=85.0,
        )
    )


server = Server(port=4840)
server.ns.append(sys.modules[__name__])
system = DistillingSystemType(parent=server.objectsNode, browseName="MainStill", server=server)
server.start()
```

A read following `HasTypeDefinition` from `Setpoint` lands on `TemperatureType`, can read `EngineeringUnits` from there, and now has units, range, and value — three pieces of information carried on two nodes.

---

## What's next?

`Setpoint` is no longer a bare Double — it's a typed value that carries its own engineering context with it, wherever it's used. Types have now shaped a whole object and a single value; the next page turns the same model-first habit toward something different again: not a node, but the relationship between two nodes. That's what custom `ReferenceType`s are for.

- [Declare a reference type](220_declare-reference-type.md) — custom `ReferenceType`s for relationships beyond `HasComponent` / `HasProperty`.
- [Writing a Nodeset in Python](../../manual/sdk-fundamentals/namespace/writing-nodesets-in-python.md#o6variabletype-typed-variables) — the full VariableType story, including `valueRank=` and array types.
