# Declare a variable type

`Setpoint` is more than a `Double`: it has units (degrees Celsius) and an operating range. So far that metadata is not in the model, so clients have to assume it. This page declares a custom `VariableType` and uses it as the type definition of a `Setpoint` Variable. The result is a typed Variable whose engineering metadata is carried on the type, not repeated on every instance.

!!! info
    For read/write behaviour on a declared Variable, such as validation or clamping, see [Declare and implement a Variable](150_implement-variable.md). It pairs a declared `Setpoint` with an implementer class that clamps writes.

---

## Declare a VariableType with `@o6.variabletype`

`@o6.variabletype` declares a `VariableType`: a template for Variables whose DataType, ValueRank and other metadata come from the type rather than from each node.

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

The instances of this VariableType are scalar `Double`s. The class body can declare further children, typically `EngineeringUnits` and `Range` properties.

The declared class is the type. To get a typed instance, construct `TemperatureType(...)` directly or annotate a leaf inside another declared type with `TemperatureType`. Either way, `o6` resolves the value's DataType, ValueRank and children from the class.

!!! info
    VariableType and ObjectType declarations live in the same namespace table. The shortname `distillery` is registered once and reused.

---

## Add `EngineeringUnits` and `Range` properties

OPC UA defines `EUInformation` and `Range` as the standard ways to attach units and an engineering range to a value. Declared on the type, they appear on every instance.

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

`EngineeringUnits` is an `EUInformation` and `InstrumentRange` is a `Range`. Both are `ns0.vartypes.PropertyType` instances: a leaf Property is always constructed from its concrete VariableType, never from a separate "variable" helper. Clients read them through the `Value` attribute like any other Variable. A client can tell from the `EngineeringUnits` value that this is a Celsius temperature with a defined engineering range.

!!! info
    The DataType identifiers `i=887` (`EUInformation`) and `i=884` (`Range`) come from the standard OPC UA namespace (`ns0`). Every server publishes them, so no extra nodeset import is needed. `dataType=` accepts a NodeId string like this or a Python type such as `float`.

---

## Use the type as a `typeDefinition`

Declaring `TemperatureType` puts nothing on a server. To create a Variable of this type, construct the class:

```python
setpoint = TemperatureType(
    parent=server.objectsNode,
    browseName="Setpoint",
    nodeId="ns=distillery;i=1204",
    value=85.0,
    server=server,     # required when this script also declared the namespace — see the note on the ObjectType page
)
```

`setpoint` is a `Double` Variable whose `HasTypeDefinition` points at `TemperatureType`. It gets the `EngineeringUnits` and `InstrumentRange` properties from the type and owns its own value (`85.0`).

The imperative equivalent passes the declared class to `addVariable(typeDefinition=...)`:

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

`typeDefinition=` accepts the declared class or its NodeId string, `"ns=distillery;i=3000"`. A client that follows `HasTypeDefinition` from `Setpoint` reaches `TemperatureType` and reads `EngineeringUnits` there. The units and range are not declared on each instance.

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

Following `HasTypeDefinition` from `MainStill/Setpoint` leads to `TemperatureType`, where a client reads the units and range. The value lives on the instance.

---

## Next steps

| Topic | What it covers |
|---|---|
| [Declare a reference type](220_declare-reference-type.md) | Custom `ReferenceType`s for relationships beyond `HasComponent` / `HasProperty`. |
| [Writing a Nodeset in Python](../../manual/information-model-authoring/object-variable-types.md#o6variabletype-typed-variables) | The full VariableType story, including `valueRank=` and array types. |
