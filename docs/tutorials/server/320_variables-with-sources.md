# Variables with sources

The previous page gave Methods a way to pick up new behaviour after they were built, rather than only at construction time. Variables need the same freedom, and for much the same reason. Right now, the distillery's `Operating` and `Setpoint` are passive Variables — the server stores the value, hands it back on read, and replaces it on write. The distillery's `Kettle.Temperature`, `Kettle.Level`, `Distillate.Level`, `Actuators.Heater`, `Actuators.FillValve`, and `Actuators.DrainValve` are the opposite: the *server* owns the value, and the value is *published* from a simulation running in the server process — never stored from incoming writes.

This page reuses the imperative `Kettle/Temperature` from the [hierarchy page](105_add-hierarchy.md) and installs a read callback with `Server.implement(...)`. The callback reads from a Python object — the simulation state — and the simulation runs elsewhere in the process. By the end, every read of `Kettle/Temperature` returns the current simulation state, and the Python state is the source of truth.

A passive Variable accepts whatever is written, as long as the value's DataType matches. That's the right shape for sensor readings the server publishes — but for `Setpoint`, `Operating`, or any value the server uses to drive other state, the write needs server-side logic. That is what this page is about: turning a Variable into an active participant in the control loop by installing `read=` and `write=` callbacks.

!!! info
    This installs callbacks on one already-built Variable node. [Declare and implement a Variable](150_implement-variable.md), earlier in these tutorials, covers the type-level equivalent — implement a Variable's `read`/`write` once on a declared `ObjectType`, and every instance built from that type gets the behaviour automatically, with no per-instance `Server.implement(...)` call needed.

---

## Install a read callback with `Server.implement(variable, read=...)`

`Server.implement(variable, read=callback)` installs a function on the *read slot* of an existing Variable. From then on, the callback is called instead of returning the variable's stored value:

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

The callback receives the Variable handle as its first argument and the keyword-only metadata `range=`, `session=`, and `includeSourceTimestamp=` (the distillery's callback ignores them). It returns `(StatusCode.GOOD, value)` — `Bad` statuses stand alone, `Good` ones must be followed by exactly one value.

`simulation_state["kettle_temp"]` is the source of truth. A background update loop (covered in the next [server callbacks page](330_server-callbacks.md)) can poke that dict from a timer, and the next read sees the new value because the callback reads it on every read.

!!! warning
    Once a Variable has a read callback, *it owns the value*. The initial `value=20.0` is only the seed the callback receives on first invocation if it happens to read it; from then on the callback's return value is what is read. Server-side writes (`simulation_state["kettle_temp"] = 25.0`) bypass the callback and update the Python state directly.

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

The temperature value never lands in native storage — the callback reads from a Python dict, and the dict is updated from a background loop. A read of `Kettle/Temperature` every 100 ms walks the value from `20.0` up to `39.0`.

---

## Read and write together

`Setpoint` is the distillery's most useful example of a Variable with both halves: it is read (to display) and written (to change the target). Both slots need callbacks, and the read callback returns whatever the write callback last stored.

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

The two callbacks share `setpoint_state["value"]`. A read returns whatever the last write stored. There is no native storage involved — the Python dict is the source of truth, the read callback hands it out, the write callback accepts the new value (with validation).

!!! info
    A read slot must exist before a write slot. open62541's callback value sources must be readable, so a write-only Variable is rejected. That fits the read-write pattern anyway — if a value can be written, it must also be able to be read back.

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

The write validates the range before storing; the read returns whatever was stored. Two callbacks, one Python dict, no native storage.

---

## Validate and reject with `StatusCode`

A write callback returns `(StatusCode.GOOD,)` to accept, or `(StatusCode.BAD_<something>,)` to reject. The OPC UA spec lists the relevant codes — `BAD_OUT_OF_RANGE`, `BAD_USER_ACCESS_DENIED`, `BAD_INVALID_ARGUMENT`, `BAD_NOT_SUPPORTED`, etc. Pick the one that fits the failure; the rejection is reflected back on the wire.

```python
LOW, HIGH = 0.0, 100.0


def write_setpoint(node, value, *, range, session):
    incoming = float(value.value)
    if not (LOW <= incoming <= HIGH):
        return (StatusCode.BAD_OUT_OF_RANGE,)
    setpoint_state["value"] = incoming
    return (StatusCode.GOOD,)
```

This is the strict form: out-of-range is rejected outright, no clamping. Choose one or the other depending on the contract — the distillery's `Setpoint` Variable *rejects* here because the write should fail loudly when the operator asks for something out of range (the `SetSetpoint` Method on the [method implementations](310_method-implementations.md) page takes the opposite approach and *clamps* instead, echoing back what was actually stored); `Operating` *accepts anything* because it is a boolean and the only failure is the wrong type, which the type system catches before the callback runs.

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

The write validates the range before storing; the read returns whatever was stored. Two callbacks, one Python dict, no native storage.

---

## Mirror a write to another node

The most useful pattern is *write A, react by writing B*. The distillery's `Operating=False` should also clear the `Cycle` counter, so a new batch starts from `0`:

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

`cycle(0)` is a server-side write that does not invoke the cycle's write slot (none is installed). The bypass is intentional — the server is the source of truth for the cycle counter.

!!! warning
    Synchronous callback dispatch rejects recursion on the *same* node with `BadInvalidState` — a write callback cannot re-enter that same Variable's own read or write callback. Independent nodes are unaffected, which is why `write_operating` above can write `cycle` from inside its own write callback without issue. Still prefer triggering cross-node side-effects through a server-side update loop, a timer, or a queue when the logic grows more involved than a one-line reset.

For the distillery, the practical pattern is: write callbacks validate and log, the [background timer](330_server-callbacks.md) reacts by reading the validated values and pushing state into other Variables.

---

## Replace or clear a callback

`Server.implement(variable, read=None)` clears the read slot. A read returns to the construction-time behaviour — the original stored value, with the initial `value=...` as the seed:

```python
server.implement(setpoint, read=None, write=None)
# setpoint() now reads from native storage again, with the value it had when last written.
```

Passing a fresh callback replaces the existing one — `Server.implement` always wins on the concrete Variable:

```python
def read_setpoint_v2(node, *, range, session, includeSourceTimestamp):
    return (StatusCode.GOOD, o6.Double(setpoint_state["value"] + 1.0))   # off-by-one variant

server.implement(setpoint, read=read_setpoint_v2)
```

The new callback is the one that runs from that point on. The old one is still a Python function (still in scope, still callable) but no longer bound to the Variable.

---

## What's next?

The Variables now have either a read callback (publishing from a Python source), a write callback (validating incoming writes), or both. The next page is about the glue that wires the whole thing together — periodic timers, startup hooks, and the long-running background loop that drives a simulation.

- [Server callbacks](330_server-callbacks.md) — startup, shutdown, periodic timers, retention cleanup.
- [Server manual](../../manual/server/callbacks.md#variables) — the full Variable callback signature, including `range=`, `session=`, and `includeSourceTimestamp=`.