# Add a method

This page adds a `Shutdown` method that a client can call to stop the server, then methods with input and output arguments. A Method is a node that runs a Python function on request. The methods live under the `DistillingSystem` skeleton from the [hierarchy page](105_add-hierarchy.md).

---

## Add a method with `addMethod`

`Server.addMethod()` registers a callable on an Object node. The positional arguments are the name, the parent and the Python function the server invokes when the Method is called.

```python
import time
from o6 import Server, StatusCode

server = Server(port=4840)
sys = server.addObject("DistillingSystem", server.objectsNode, nodeId="ns=1;i=1000")
status = server.addObject("Status", sys, nodeId="ns=1;i=1200")

setpoint = server.addVariable("Setpoint", status, 85.0, nodeId="ns=1;i=1204")

def shutdown(node):
    """Stop the server when this method is invoked."""
    print(f"  [Method] Shutdown called from {node._nodeid}")
    return (StatusCode.GOOD,)

shutdown_method = server.addMethod(
    "Shutdown",
    sys,
    shutdown,
    nodeId="ns=1;i=2002",
)
server.start()
```

The function receives the parent Object as its first argument: `sys`, the `DistillingSystem` object, as in the reference server. It returns a one-tuple holding the `StatusCode`. `Good` accepts the call; anything else rejects it before the body even runs. The server wires the function up when `start()` runs and routes calls to it.

#### Putting it all together

```python
import time
from o6 import Server, StatusCode

server = Server(port=4840)
sys = server.addObject("DistillingSystem", server.objectsNode, nodeId="ns=1;i=1000")
status = server.addObject("Status", sys, nodeId="ns=1;i=1200")
setpoint = server.addVariable("Setpoint", status, 85.0, nodeId="ns=1;i=1204")

def shutdown(node):
    print(f"  [Method] Shutdown called from {node._nodeid}")
    return (StatusCode.GOOD,)

shutdown_method = server.addMethod("Shutdown", sys, shutdown, nodeId="ns=1;i=2002")
server.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pass

server.stop()
```

`addMethod` returns the Method node (`shutdown_method`). Calling it dispatches through the Call service, the same path a client's `Call` request takes, without the network round trip:

```python
print(shutdown_method())   # ()  — no OutputArguments declared, so nothing comes back
```

A `Bad` status raises `StatusCodeError`. `shutdown_method()` returns normally only when the callback accepts the call. Attach per-Object state to the [`node` parameter](../../manual/server/callbacks.md#methods); the server always passes the parent Object as the first argument.

---

## Methods that need inputs and outputs

`Start` and `Shutdown` take no inputs and return only a status. For arguments, pass `inputArgs=` and `outputArgs=` to `addMethod`: lists of `ns0.datatypes.Argument` descriptors, one entry per argument, in declaration order.

```python
from o6.ns import ns0
from o6 import ValueRank

def set_setpoint(node, value):
    """Update the distillery setpoint."""
    setpoint(value)
    return (StatusCode.GOOD,)

server.addMethod(
    "SetSetpoint",
    sys,
    set_setpoint,
    inputArgs=[
        ns0.datatypes.Argument(
            name="Value",
            dataType="i=11",                # Double
            valueRank=ValueRank.SCALAR,
            description="New setpoint, °C",
        ),
    ],
    nodeId="ns=1;i=2003",
)
```

The callback signature is `(node, value)`: the parent Object and the first input. With no outputs declared, it returns a `(StatusCode,)` tuple.

A method with outputs adds them to the return tuple, in declaration order:

```python
def add(node, a, b):
    """Return the sum of two doubles."""
    return (StatusCode.GOOD, a + b)

server.addMethod(
    "Add",
    sys,
    add,
    inputArgs=[
        ns0.datatypes.Argument(name="A", dataType="i=11", valueRank=ValueRank.SCALAR),
        ns0.datatypes.Argument(name="B", dataType="i=11", valueRank=ValueRank.SCALAR),
    ],
    outputArgs=[
        ns0.datatypes.Argument(name="Sum", dataType="i=11", valueRank=ValueRank.SCALAR),
    ],
    nodeId="ns=1;i=2010",
)
```

The first element is always the `StatusCode`. A `Bad` status may stand alone, as in `return (StatusCode.BAD_OUT_OF_RANGE,)`. A `Good` status must be followed by exactly the declared number of outputs.

!!! warning
    Set `valueRank=ValueRank.SCALAR` for scalar arguments. The default
    value rank is `0`, which means array. A scalar argument sent to an
    array-typed parameter fails with `BAD_INVALID_ARGUMENT` before the
    callback runs. This is the most common cause of a method that "doesn't
    work".

#### Putting it all together

```python
import time
from o6.ns import ns0
from o6 import Server, StatusCode, ValueRank

server = Server(port=4840)
sys = server.addObject("DistillingSystem", server.objectsNode, nodeId="ns=1;i=1000")
status = server.addObject("Status", sys, nodeId="ns=1;i=1200")
setpoint = server.addVariable("Setpoint", status, 85.0, nodeId="ns=1;i=1204")

def set_setpoint(node, value):
    setpoint(value)
    return (StatusCode.GOOD,)

server.addMethod(
    "SetSetpoint",
    sys,
    set_setpoint,
    inputArgs=[
        ns0.datatypes.Argument(
            name="Value",
            dataType="i=11",
            valueRank=ValueRank.SCALAR,
            description="New setpoint, °C",
        ),
    ],
    nodeId="ns=1;i=2003",
)

def add(node, a, b):
    return (StatusCode.GOOD, a + b)

server.addMethod(
    "Add",
    sys,
    add,
    inputArgs=[
        ns0.datatypes.Argument(name="A", dataType="i=11", valueRank=ValueRank.SCALAR),
        ns0.datatypes.Argument(name="B", dataType="i=11", valueRank=ValueRank.SCALAR),
    ],
    outputArgs=[
        ns0.datatypes.Argument(name="Sum", dataType="i=11", valueRank=ValueRank.SCALAR),
    ],
    nodeId="ns=1;i=2010",
)

server.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pass

server.stop()
```

---

## Next steps

The next pages cover where a value's content comes from, starting with values fed from outside the server.

| Topic | What it covers |
|---|---|
| [Values from an external source](130_data-source.md) | A Variable whose truth lives in a Python model instead of native storage. |
| [Add a hierarchy](105_add-hierarchy.md) | The folder skeleton layout. |
| [Server manual](../../manual/server/address-space.md#objects-types-views-and-methods) | Every keyword argument on `addMethod`, including `inputArgs=` and `outputArgs=`. |
