# Method implementations

The distillery's data model is complete now — Foundation gave it a hierarchy, Composition turned that same hierarchy into declared types a server can build instances from. None of that, on its own, makes the distillery act. Its `Shutdown` method, built back on the [add a method](120_add-method.md) page, only does anything because `addMethod(name, parent, callback, ...)` bound a callback to it at the moment it was created. That works fine while the method stays simple, but it stops covering the case once a Method needs to exchange arguments, return more than one output, or fail in a way its caller can actually tell apart from other failures.

This page is where methods start behaving like operations instead of fixed wiring. It centers on `Server.implement(method, call=callback)`, the imperative way to attach a callback to a Method that already exists — built earlier, or shared with another server — rather than fixing it in at construction time. The validation, output, and error-mapping ideas are the same ones the [add a method](120_add-method.md) page introduced; what changes here is how the callback gets attached, and that it can be replaced later.

!!! info
    This installs a callback on one already-built Method node. [Declare and implement an ObjectType](160_implement-objecttype.md), earlier in these tutorials, covers the type-level equivalent — implement a Method once on a declared `ObjectType`, and every instance the server builds from that type gets the behaviour automatically.

---

## Install a method callback with `Server.implement(method, call=...)`

`Server.implement(method, call=callback)` installs a function on the *call slot* of an existing Method. From then on, the callback is the function the method routes to:

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

The callback receives the parent Object as its first argument — here, the `DistillingSystem` folder at `ns=1;i=1000`. It returns a `(StatusCode,)` tuple; `StatusCode.GOOD` accepts, anything else rejects. For a no-output Method that is the whole result.

!!! info
    `Server.implement(method, call=None)` clears the slot. Subsequent invocations return `BadNotImplemented` until a fresh callback is installed.

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

The function is what the server invokes when the method is called. Calling it directly produces the same `(StatusCode,)` tuple the protocol would receive.

---

## Methods with input and output arguments

The next page, [Variables with sources](320_variables-with-sources.md), adds a write handler that validates and rejects out-of-range writes to the distillery's `Setpoint`. Here, the same kind of logic is exposed as a Method instead: it takes an input argument, clamps it, and returns the clamped value:

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

The Method signature on the Python side mirrors the UA signature: input arguments are positional parameters in declaration order, the return tuple's first element is the `StatusCode`, and the remaining elements are the outputs in declaration order.

`Argument(valueRank=ValueRank.SCALAR)` is not decoration — the default rank `0` means *array*, and a scalar argument arriving at an array-typed parameter gets `BAD_INVALID_ARGUMENT` before the callback runs.

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

An invocation of `SetSetpoint` with `value=105.0` returns `(StatusCode.GOOD, Double(100.0))` — the operation succeeded, and the clamped value is reported back. The whole point of the *output* is to echo the result: "I asked for 105, here's what I got".

---

## Map failures to specific StatusCodes

Clamping is one way to handle a bad input: quietly fix it, then report what was actually stored. It isn't always the right one — some failures need to be refused outright, with a `StatusCode` specific enough that the caller can tell what went wrong. A Method that can fail in multiple ways should pick the right `StatusCode` for each failure. The OPC UA spec lists the ones relevant to most control loops:

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

Every callback so far has returned as soon as it ran, synchronously. Not every operation can finish that quickly — a shutdown that has to close valves in sequence, or a call that waits on real hardware, needs to `await` without blocking the rest of the server while it does. The Method callback may be `async def`. Synchronous and asynchronous callbacks have the same positional arguments and the same result-tuple semantics; the server drives the coroutine on its event loop and the resolved values are returned over the wire.

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

Passing a fresh callback replaces the existing one, exactly like the Variable case on the [Variables with sources](320_variables-with-sources.md) page:

```python
server.implement(set_setpoint, call=set_setpoint_callback_v2)
```

`Server.implement(method, call=None)` clears the slot. Subsequent invocations return `BadNotImplemented` until a fresh callback is installed:

```python
server.implement(set_setpoint, call=None)
# set_setpoint() now returns BadNotImplemented.
```

The old callback is still a Python function (still in scope, still callable) but no longer bound to the Method.

---

## What's next?

With `Server.implement(method, call=...)`, the distillery's Methods can be wired, swapped, or cleared any time after they're built, not just at construction. That covers only half of what makes an address space active, though — Variables need the same kind of after-the-fact wiring for their own read and write behaviour, and that's exactly where the next page picks up.

- [Variables with sources](320_variables-with-sources.md) — install read and write callbacks with `Server.implement(...)`, validate, mirror to a simulation.
- [Server manual](../../manual/server/callbacks.md#methods) — the full Method callback signature, including `node`, `session`, and `range` keywords.