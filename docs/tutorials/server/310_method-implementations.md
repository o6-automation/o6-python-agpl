# Method implementations

On [Add a method](120_add-method.md), `addMethod(name, parent, callback, ...)` binds the callback when the Method is created. `Server.implement(method, call=callback)` attaches a callback to a Method that already exists, built earlier or shared with another server, and lets you replace it later. This page uses it for Methods with arguments, multiple outputs and specific failure codes. Validation, outputs and error mapping work as on [Add a method](120_add-method.md).

!!! info
    This installs a callback on one Method node. To implement a Method once on a declared `ObjectType` so that every instance gets the behaviour, see [Declare and implement an ObjectType](160_implement-objecttype.md).

---

## Install a method callback with `Server.implement(method, call=...)`

`Server.implement(method, call=callback)` installs a function in the *call slot* of an existing Method. Calls to the Method then go to that function:

```python
import time
import o6
from o6 import Server, StatusCode

server = Server(port=4840)

sys = server.addObject("DistillingSystem", server.objectsNode, nodeId="ns=1;i=1000")

# Build the method without a callback at construction time — we will install one below.
shutdown_method = server.addMethod(
    "Shutdown",
    sys,
    nodeId="ns=1;i=2002",
)


def shutdown(node):
    """Stop the server when this Method is invoked."""
    print(f"  [Method] Shutdown called from {node.nodeId}")
    return (StatusCode.GOOD,)


server.implement(shutdown_method, call=shutdown)
server.start()
```

The callback receives the parent Object as its first argument, here `DistillingSystem` at `ns=1;i=1000`. It returns a `(StatusCode,)` tuple: `StatusCode.GOOD` accepts, anything else rejects. A Method without outputs returns nothing more.

#### Putting it all together

```python
import time
import o6
from o6 import Server, StatusCode

server = Server(port=4840)

sys = server.addObject("DistillingSystem", server.objectsNode, nodeId="ns=1;i=1000")
shutdown_method = server.addMethod("Shutdown", sys, nodeId="ns=1;i=2002")


def shutdown(node):
    print(f"  [Method] Shutdown called from {node.nodeId}")
    return (StatusCode.GOOD,)


server.implement(shutdown_method, call=shutdown)
server.start()

# The method's Body is now the shutdown function — call it directly to verify.
print(shutdown(sys))   # (StatusCode.GOOD,)

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pass

server.stop()
```

Calling the function directly returns the same `(StatusCode,)` tuple a client receives.

---

## Methods with input and output arguments

[Variables with sources](320_variables-with-sources.md) validates `Setpoint` writes with a write handler. This Method does the same job as an operation: it takes a setpoint as input, clamps it, and returns the clamped value:

```python
import time
import o6
from o6 import Server, StatusCode, ValueRank
from o6.ns import ns0

server = Server(port=4840)
sys = server.addObject("DistillingSystem", server.objectsNode, nodeId="ns=1;i=1000")

set_setpoint = server.addMethod(
    "SetSetpoint",
    sys,
    inputArgs=[
        ns0.datatypes.Argument(
            name="Value",
            dataType="i=11",         # Double
            valueRank=ValueRank.SCALAR,
            description="New setpoint, °C",
        ),
    ],
    outputArgs=[
        ns0.datatypes.Argument(
            name="Clamped",
            dataType="i=11",
            valueRank=ValueRank.SCALAR,
            description="The setpoint value actually stored",
        ),
    ],
    nodeId="ns=1;i=2003",
)

LOW, HIGH = 0.0, 100.0


def set_setpoint_callback(node, value):
    """Clamp the incoming value and return what was actually stored."""
    clamped = max(LOW, min(HIGH, float(value.value)))
    return (StatusCode.GOOD, o6.Double(clamped))


server.implement(set_setpoint, call=set_setpoint_callback)
server.start()
```

The Python signature mirrors the OPC UA signature:

- Input arguments are positional parameters in declaration order.
- The first element of the returned tuple is the `StatusCode`.
- The remaining elements are the outputs in declaration order.

`Argument(valueRank=ValueRank.SCALAR)` is required for scalars. The default rank `0` means array, and a scalar sent to an array-typed parameter gets `BAD_INVALID_ARGUMENT` before the callback runs.

#### Putting it all together

```python
import time
import o6
from o6 import Server, StatusCode, ValueRank
from o6.ns import ns0

server = Server(port=4840)
sys = server.addObject("DistillingSystem", server.objectsNode, nodeId="ns=1;i=1000")

set_setpoint = server.addMethod(
    "SetSetpoint",
    sys,
    inputArgs=[
        ns0.datatypes.Argument(
            name="Value",
            dataType="i=11",
            valueRank=ValueRank.SCALAR,
            description="New setpoint, °C",
        ),
    ],
    outputArgs=[
        ns0.datatypes.Argument(
            name="Clamped",
            dataType="i=11",
            valueRank=ValueRank.SCALAR,
            description="The setpoint value actually stored",
        ),
    ],
    nodeId="ns=1;i=2003",
)

LOW, HIGH = 0.0, 100.0


def set_setpoint_callback(node, value):
    clamped = max(LOW, min(HIGH, float(value.value)))
    return (StatusCode.GOOD, o6.Double(clamped))


server.implement(set_setpoint, call=set_setpoint_callback)
server.start()

# Try the validation path
print(set_setpoint_callback(sys, o6.Double(105.0)))     # (StatusCode.GOOD, Double(100.0))
print(set_setpoint_callback(sys, o6.Double(50.0)))      # (StatusCode.GOOD, Double(50.0))
```

Calling `SetSetpoint` with `value=105.0` returns `(StatusCode.GOOD, Double(100.0))`. The output tells the caller which value was stored.

---

## Map failures to specific StatusCodes

To refuse an input instead of clamping it, return a `StatusCode` that tells the caller what went wrong. Pick a specific code for each failure. These OPC UA codes cover most control loops:

- `BAD_OUT_OF_RANGE` — argument outside an accepted range
- `BAD_INVALID_ARGUMENT` — argument type or count wrong (the spec usually catches this before the callback)
- `BAD_USER_ACCESS_DENIED` — the caller has no permission for this operation
- `BAD_NOT_SUPPORTED` — the server cannot do this operation right now
- `BAD_INVALID_STATE` — the server is in a state where this operation is not allowed

```python
def set_setpoint_callback(node, value):
    incoming = float(value.value)
    if not (LOW <= incoming <= HIGH):
        return (StatusCode.BAD_OUT_OF_RANGE,)
    return (StatusCode.GOOD, o6.Double(incoming))
```

A `Bad` status stands alone. A `Good` status must be followed by exactly the declared number of outputs — there is no way to return a partial result.

---

## Async Method bodies

A Method callback may be `async def`, for example to close valves in sequence or wait on hardware without blocking the server. Sync and async callbacks take the same positional arguments and return the same result tuple. The server runs the coroutine on its event loop and returns the resolved values to the client.

```python
import asyncio

async def shutdown(node):
    """Stop the server after an ordered teardown."""
    await asyncio.sleep(0.5)
    print("  [Method] Shutdown complete")
    return (StatusCode.GOOD,)


server.implement(shutdown_method, call=shutdown)
```

Async Method execution is not guarded after the callback has returned its coroutine.

---

## Replace or clear a callback

Passing a new callback replaces the existing one, as for Variables on [Variables with sources](320_variables-with-sources.md):

```python
server.implement(set_setpoint, call=set_setpoint_callback_v2)
```

`Server.implement(method, call=None)` clears the slot. Calls then return `BadNotImplemented` until you install a new callback:

```python
server.implement(set_setpoint, call=None)
# set_setpoint() now returns BadNotImplemented.
```

The old function stays callable from Python but is no longer bound to the Method.

---

## Next steps

| Topic | What it covers |
|---|---|
| [Variables with sources](320_variables-with-sources.md) | Install read and write callbacks with `Server.implement(...)`, validate, mirror to a simulation. |
| [Server manual](../../manual/server/callbacks.md#methods) | The full Method callback signature, including `node`, `session`, and `range` keywords. |
