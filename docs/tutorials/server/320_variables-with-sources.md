# Variables with sources

A passive Variable stores its value, returns it on read, and replaces it on any write whose DataType matches. So far `Operating` and `Setpoint` are passive. The distillery's `Kettle.Temperature`, `Kettle.Level`, `Distillate.Level`, `Actuators.Heater`, `Actuators.FillValve` and `Actuators.DrainValve` work the other way: the server owns the value and publishes it from a simulation in the server process, never from incoming writes. `Setpoint`, `Operating` and any other value that drives server state need server-side logic on write.

This page installs `read=` and `write=` callbacks on existing Variables with `Server.implement(...)`, the Variable counterpart of [Method implementations](310_method-implementations.md). It starts with a read callback on the imperative `Kettle/Temperature` from [Add a hierarchy](105_add-hierarchy.md), so that every read returns the current simulation state held in a Python object.

!!! info
    This installs callbacks on one Variable node. To implement `read`/`write` once on a declared `ObjectType` so that every instance gets the behaviour without a per-instance `Server.implement(...)` call, see [Declare and implement a Variable](150_implement-variable.md).

---

## Install a read callback with `Server.implement(variable, read=...)`

`Server.implement(variable, read=callback)` installs a function in the *read slot* of an existing Variable. Reads then call the function instead of returning the stored value:

```python
import time
import o6
from o6 import Server, StatusCode

server = Server(port=4840)

sys = server.addObject("DistillingSystem", server.objectsNode, nodeId="ns=1;i=1000")
kettle = server.addObject("Kettle", sys, nodeId="ns=1;i=1300")
kettle_temperature = server.addVariable(
    "Temperature",
    kettle,
    20.0,                              # initial value, used only as a seed
    nodeId="ns=1;i=1302",
    writable=False,
)

# Source of truth lives outside the Variables folder.
simulation_state = {"kettle_temp": 20.0}


def read_kettle_temperature(node, *, range, session, includeSourceTimestamp):
    return (StatusCode.GOOD, o6.Double(simulation_state["kettle_temp"]))


server.implement(kettle_temperature, read=read_kettle_temperature)
server.start()
```

The callback receives the Variable handle as its first argument and the keyword-only arguments `range=`, `session=` and `includeSourceTimestamp=`, which this callback ignores. It returns `(StatusCode.GOOD, value)`. A `Bad` status stands alone; a `Good` status must be followed by exactly one value.

`simulation_state["kettle_temp"]` is the source of truth. A timer can update the dict (see [Server callbacks](330_server-callbacks.md)), and the next read returns the new value.

!!! warning
    Once a Variable has a read callback, the callback owns the value. The initial `value=20.0` is only a seed the callback may read on first invocation; after that, reads return the callback's value. Server-side writes (`simulation_state["kettle_temp"] = 25.0`) bypass the callback and update the Python state directly.

#### Putting it all together

```python
import time
import o6
from o6 import Server, StatusCode

server = Server(port=4840)

sys = server.addObject("DistillingSystem", server.objectsNode, nodeId="ns=1;i=1000")
kettle = server.addObject("Kettle", sys, nodeId="ns=1;i=1300")
kettle_temperature = server.addVariable(
    "Temperature",
    kettle,
    20.0,
    nodeId="ns=1;i=1302",
    writable=False,
)

simulation_state = {"kettle_temp": 20.0}


def read_kettle_temperature(node, *, range, session, includeSourceTimestamp):
    return (StatusCode.GOOD, o6.Double(simulation_state["kettle_temp"]))


server.implement(kettle_temperature, read=read_kettle_temperature)
server.start()

# Drive the temperature from a quick update loop
with server:
    for cycle in range(20):
        time.sleep(0.1)
        simulation_state["kettle_temp"] = 20.0 + cycle
        print(f"  cycle {cycle}: temperature = {server.read('ns=1;i=1302')}")
```

The temperature never lands in native storage. Reading `Kettle/Temperature` every 100 ms shows the value climbing from `20.0` to `39.0`.

---

## Read and write together

`Setpoint` is read for display and written to change the target, so it needs both callbacks. The read callback returns what the write callback last stored.

```python
import time
import o6
from o6 import Server, StatusCode

server = Server(port=4840)

sys = server.addObject("DistillingSystem", server.objectsNode, nodeId="ns=1;i=1000")
status = server.addObject("Status", sys, nodeId="ns=1;i=1200")
setpoint = server.addVariable(
    "Setpoint",
    status,
    85.0,
    nodeId="ns=1;i=1204",
    writable=True,
)

# Source of truth: a dict, updated by the write callback and read by the read callback.
setpoint_state = {"value": 85.0}
LOW, HIGH = 0.0, 100.0


def read_setpoint(node, *, range, session, includeSourceTimestamp):
    return (StatusCode.GOOD, o6.Double(setpoint_state["value"]))


def write_setpoint(node, value, *, range, session):
    incoming = float(value.value)
    if not (LOW <= incoming <= HIGH):
        return (StatusCode.BAD_OUT_OF_RANGE,)
    setpoint_state["value"] = incoming
    return (StatusCode.GOOD,)


server.implement(setpoint, read=read_setpoint, write=write_setpoint)
server.start()
```

No native storage is involved. The Python dict is the source of truth.

!!! info
    A read slot must exist before a write slot. open62541 requires callback value sources to be readable, so a write-only Variable is rejected.

#### Putting it all together

```python
import time
import o6
from o6 import Server, StatusCode

server = Server(port=4840)
sys = server.addObject("DistillingSystem", server.objectsNode, nodeId="ns=1;i=1000")
status = server.addObject("Status", sys, nodeId="ns=1;i=1200")
setpoint = server.addVariable("Setpoint", status, 85.0, nodeId="ns=1;i=1204", writable=True)

setpoint_state = {"value": 85.0}
LOW, HIGH = 0.0, 100.0


def read_setpoint(node, *, range, session, includeSourceTimestamp):
    return (StatusCode.GOOD, o6.Double(setpoint_state["value"]))


def write_setpoint(node, value, *, range, session):
    incoming = float(value.value)
    if not (LOW <= incoming <= HIGH):
        return (StatusCode.BAD_OUT_OF_RANGE,)
    setpoint_state["value"] = incoming
    return (StatusCode.GOOD,)


server.implement(setpoint, read=read_setpoint, write=write_setpoint)
server.start()

# Try the validation path
print(server.read("ns=1;i=1204"))                          # 85.0
print(server.write("ns=1;i=1204", 90.0))                  # StatusCode.GOOD
print(server.write("ns=1;i=1204", 105.0))                 # StatusCode.BAD_OUT_OF_RANGE
print(server.read("ns=1;i=1204"))                          # 90.0
```

---

## Validate and reject with `StatusCode`

A write callback returns `(StatusCode.GOOD,)` to accept or `(StatusCode.BAD_<something>,)` to reject. Pick the code that fits the failure, such as `BAD_OUT_OF_RANGE`, `BAD_USER_ACCESS_DENIED`, `BAD_INVALID_ARGUMENT` or `BAD_NOT_SUPPORTED`. The client receives that code.

```python
LOW, HIGH = 0.0, 100.0


def write_setpoint(node, value, *, range, session):
    incoming = float(value.value)
    if not (LOW <= incoming <= HIGH):
        return (StatusCode.BAD_OUT_OF_RANGE,)
    setpoint_state["value"] = incoming
    return (StatusCode.GOOD,)
```

This is the strict form: out-of-range values are rejected, not clamped. Choose per contract:

- `Setpoint` rejects, so an out-of-range request from the operator fails visibly.
- The `SetSetpoint` Method on [Method implementations](310_method-implementations.md) clamps and returns the stored value.
- `Operating` accepts anything. It is a Boolean, and the only possible failure, a wrong type, is caught before the callback runs.

#### Putting it all together

```python
import time
import o6
from o6 import Server, StatusCode

server = Server(port=4840)
sys = server.addObject("DistillingSystem", server.objectsNode, nodeId="ns=1;i=1000")
status = server.addObject("Status", sys, nodeId="ns=1;i=1200")
setpoint = server.addVariable("Setpoint", status, 85.0, nodeId="ns=1;i=1204", writable=True)

setpoint_state = {"value": 85.0}


def read_setpoint(node, *, range, session, includeSourceTimestamp):
    return (StatusCode.GOOD, o6.Double(setpoint_state["value"]))


def write_setpoint(node, value, *, range, session):
    incoming = float(value.value)
    if not (0.0 <= incoming <= 100.0):
        return (StatusCode.BAD_OUT_OF_RANGE,)
    setpoint_state["value"] = incoming
    return (StatusCode.GOOD,)


server.implement(setpoint, read=read_setpoint, write=write_setpoint)
server.start()

print(server.read("ns=1;i=1204"))                          # 85.0
print(server.write("ns=1;i=1204", 90.0))                  # StatusCode.GOOD
print(server.write("ns=1;i=1204", 105.0))                 # StatusCode.BAD_OUT_OF_RANGE
print(server.read("ns=1;i=1204"))                          # 90.0
```

---

## Mirror a write to another node

A write callback can react by writing another node. Writing `Operating=False` also clears the `Cycle` counter, so a new batch starts from `0`:

```python
import time
import o6
from o6 import Server, StatusCode

server = Server(port=4840)
sys = server.addObject("DistillingSystem", server.objectsNode, nodeId="ns=1;i=1000")
status = server.addObject("Status", sys, nodeId="ns=1;i=1200")

operating = server.addVariable("Operating", status, True, nodeId="ns=1;i=1203", writable=True)
cycle = server.addVariable("Cycle", status, 0, nodeId="ns=1;i=1202", writable=False)

operating_state = {"value": True}


def read_operating(node, *, range, session, includeSourceTimestamp):
    return (StatusCode.GOOD, o6.Boolean(operating_state["value"]))


def write_operating(node, value, *, range, session):
    print(f"  [write] Operating = {value.value}")
    operating_state["value"] = bool(value.value)
    if not operating_state["value"]:
        # Parked: reset the cycle counter on the Status object.
        cycle(0)
    return (StatusCode.GOOD,)


server.implement(operating, read=read_operating, write=write_operating)
server.start()
```

`cycle(0)` is a server-side write. `Cycle` has no write callback installed, so none runs; the server is the source of truth for the counter.

!!! warning
    Synchronous callback dispatch rejects recursion on the same node with `BadInvalidState`: a write callback cannot re-enter its own Variable's read or write callback. Other nodes are unaffected, so `write_operating` can write `cycle`. For side effects more involved than a one-line reset, use a server-side update loop, a timer or a queue.

In the distillery, write callbacks validate and log. A [background timer](330_server-callbacks.md) reads the validated values and pushes state into other Variables.

---

## Replace or clear a callback

`Server.implement(variable, read=None)` clears the read slot. Reads return to the construction-time behaviour: the stored value, seeded with the initial `value=...`:

```python
server.implement(setpoint, read=None, write=None)
# setpoint() now reads from native storage again, with the value it had when last written.
```

Passing a new callback replaces the existing one. `Server.implement` always takes precedence on the concrete Variable:

```python
def read_setpoint_v2(node, *, range, session, includeSourceTimestamp):
    return (StatusCode.GOOD, o6.Double(setpoint_state["value"] + 1.0))   # off-by-one variant

server.implement(setpoint, read=read_setpoint_v2)
```

The old function stays callable from Python but is no longer bound to the Variable.

---

## Next steps

| Topic | What it covers |
|---|---|
| [Server callbacks](330_server-callbacks.md) | Startup, shutdown, periodic timers, retention cleanup. |
| [Server manual](../../manual/server/callbacks.md#variables) | The full Variable callback signature, including `range=`, `session=`, and `includeSourceTimestamp=`. |
