# Add a method

Everything the distillery has exposed so far is a value: something a client reads, and in a couple of cases writes. That covers a lot of ground, but it doesn't cover *actions* — there's no way, yet, to tell the server to actually do something. This page adds the first one: a `Shutdown` method a client can call to stop the server.

A Method is a different kind of node from anything built so far — not a value that changes, but a function the server runs on request. By the end of this page the distillery exposes one Variable and one Method, both living under the `DistillingSystem` skeleton built on the [hierarchy page](105_add-hierarchy.md).

---

## Add a method with `addMethod`

`Server.addMethod()` registers a callable on an Object node. The first two positional arguments are the name and the parent; the third is a Python function the server invokes when the Method is called.

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

The function receives the parent Object as its first argument (here, `sys` — the `DistillingSystem` object — because we hung the method directly under it, the same way the reference server does). It returns a one-tuple holding the `StatusCode` — `Good` accepts the call, anything else rejects it before the body even runs.

That is the entire pattern. A method is a node that points at a Python function; the server wires the function up when `start()` runs and routes the next call to it.

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

That server has a `Setpoint` and a `Shutdown` method. `addMethod` handed back the Method node itself (`shutdown_method`), and calling it dispatches through the real Call service — the same path a client's `Call` request takes, just without the network round trip:

```python
print(shutdown_method())   # ()  — no OutputArguments declared, so nothing comes back
```

A `Bad` status raises `StatusCodeError` instead of returning — `shutdown_method()` only returns normally once the callback has actually accepted the call. The [`node` parameter](../../manual/server/callbacks.md#methods) is the right place to attach per-Object state to — the parent Object is always the first argument the server passes to the body.

---

## Methods that need inputs and outputs

`Start` and `Shutdown` take no inputs and return just a status. Real methods exchange arguments. `addMethod` takes optional `inputArgs=` and `outputArgs=` lists of `ns0.datatypes.Argument` descriptors — one entry per argument, in declaration order.

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

The callback signature now is `(node, value)` — `node` is the parent Object, `value` is the first input. The return value is still a `(StatusCode,)` tuple, because there are no outputs declared.

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

The first element is always `StatusCode`. A `Bad` status may stand alone — `return (StatusCode.BAD_OUT_OF_RANGE,)` — but a `Good` status must be followed by exactly the declared number of outputs.

!!! warning
    `valueRank=ValueRank.SCALAR` is not decoration. The default value rank is `0`, which means *array*, and a scalar argument arriving at an array-typed parameter gets `BAD_INVALID_ARGUMENT` before the callback runs. This is the single most common cause of a method that "doesn't work".

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

## What's next?

The distillery has one Variable and one Method, both living under the `DistillingSystem` skeleton from the [hierarchy page](105_add-hierarchy.md). The next pages move from "how do you add a node?" to "how does a value get its content?" — starting with values that come from somewhere other than a plain write.

- [Values from an external source](130_data-source.md) — a Variable whose truth lives in a Python model instead of native storage.
- [Add a hierarchy](105_add-hierarchy.md) — re-visit the folder skeleton any time you need to remind yourself of the layout.
- [Server manual](../../manual/server/address-space.md#objects-types-views-and-methods) — every keyword argument on `addMethod`, including `inputArgs=` and `outputArgs=`.