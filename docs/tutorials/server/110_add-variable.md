# Add a variable

Our distillery has a shape now — [Add a hierarchy](105_add-hierarchy.md) left us with `Objects/DistillingSystem/` and its six sub-folders — but every one of those folders is still empty. A still that can't report its own temperature isn't very useful. This page is where that changes: we put our first real values inside those folders, starting with the two things an operator would actually want to change — a `Setpoint` and an `Operating` switch — and then round out `Identification/` with a few descriptive facts about the machine.

Everything from here on reuses the same idea, so there's nothing to memorise: a Variable is a named slot with a value in it, hung off a parent node. Once that's clear, the rest of this page — and a good part of the tutorials that follow — is just applying it to different folders and different kinds of value.

---

## Give `Setpoint` a home

`Server.addVariable()` is how a slot gets created. It takes a name, the folder it lives in, and the value to start it off with, in that order:

```python
from o6 import Server

server = Server(port=4840)
sys = server.addObject("DistillingSystem", server.objectsNode, nodeId="ns=1;i=1000")
status = server.addObject("Status", sys, nodeId="ns=1;i=1200")

setpoint = server.addVariable(
    "Setpoint",
    status,
    85.0,                   # the still should aim for 85 °C
    nodeId="ns=1;i=1204",
)
server.start()
```

Notice the parent is `status`, not `server.objectsNode`. `Setpoint` isn't a top-level thing; it belongs inside the `Status` folder built on the previous page, where a client browsing the distillery would expect to find it. That's the one decision to make each time a value is added: which folder does it belong in?

The `nodeId=` pins the address by hand, the same way every folder's address was pinned on the previous page, so `Setpoint` stays at `ns=1;i=1204` across restarts, and every later page — and the client tutorials — can rely on it not moving.

`o6` also picks the value's OPC UA type for us, from whatever Python value we pass in:

| We write... | The still gets a... |
|---|---|
| `85.0` (a `float`) | `Double` |
| `1013` (an `int`) | `Int32` |
| `"idle"` (a `str`) | `String` |
| `True` (a `bool`) | `Boolean` |

`85.0` is a `float`, so `Setpoint` comes out as a `Double`. There's nothing to configure — write the kind of value you mean, and the wire type follows.

!!! info
    The `ns=1` in `ns=1;i=1204` is a namespace — bookkeeping OPC UA uses to keep different vendors' NodeIds from colliding. `1` is the default for anything a server defines itself, which is all we're doing here, so it's the number every NodeId in these tutorials starts with.

#### Putting it all together

```python
import time
from o6 import Server

server = Server(port=4840)
sys = server.addObject("DistillingSystem", server.objectsNode, nodeId="ns=1;i=1000")
status = server.addObject("Status", sys, nodeId="ns=1;i=1200")

setpoint = server.addVariable(
    "Setpoint",
    status,
    85.0,
    nodeId="ns=1;i=1204",
)
server.start()

print(f"Server running at {server.endpointUrl}")
print("Press Ctrl+C to stop.")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pass

server.stop()
```

Run that, and the distillery has something worth asking about for the first time. The simplest check is to read the value, write a new one, and read it back:

```python
print(server.read("ns=1;i=1204"))   # 85.0
server.write("ns=1;i=1204", 90.0)
print(server.read("ns=1;i=1204"))   # 90.0
```

Read, write, read again. It's a small check, but it's the one we'll repeat throughout these tutorials every time a new value is added.

---

## A shorter way to reach the same value

Typing out the NodeId every time is tedious, so `addVariable(...)` returns something more convenient than the address alone: a live handle to the Variable itself. Call it with no arguments to read, call it with one argument to write:

```python
print(setpoint())                 # 85.0  — read via the handle
setpoint(90.0)                    # write via the handle
```

That's the form used everywhere from here on — `some_variable()` to read, `some_variable(new_value)` to write — because it's shorter than spelling out `server.read(...)`/`server.write(...)` in a loop. It's still exactly the same operation underneath; the handle and `server.read`/`server.write` reach the same value, just through different syntax:

```python
setpoint._value = 91.0            # a third form, doing the same thing
print(server.read("ns=1;i=1204")) # 91.0 — visible immediately, however it was set
```

#### Putting it all together

```python
import time
from o6 import Server

server = Server(port=4840)
sys = server.addObject("DistillingSystem", server.objectsNode, nodeId="ns=1;i=1000")
status = server.addObject("Status", sys, nodeId="ns=1;i=1200")
setpoint = server.addVariable("Setpoint", status, 85.0, nodeId="ns=1;i=1204")
server.start()

# Read and write from the server side
print(setpoint())           # 85.0
setpoint(90.0)
print(setpoint._value)      # 90.0
print(server.read("ns=1;i=1204"))  # 90.0

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pass

server.stop()
```

---

## A second writable value: `Operating`

A still an operator can retarget but never start or stop isn't much better. `Operating` is the second dial: a plain `True`/`False` flag, in the same `Status/` folder, saying whether the distillery should be running a batch at all.

```python
operating = server.addVariable("Operating", status, True, nodeId="ns=1;i=1203", writable=True)
```

Nothing new here — the same helper, the same folder, just a different kind of value (`bool`, so it becomes a `Boolean`). Once the `Setpoint` pattern is familiar, adding a second value is one line, not a new concept. `writable=True` is already the default; it's spelled out here because the next section is about turning it off.

---

## Values that shouldn't be writable

Two writable values — `Setpoint` and `Operating` — is the right number for this still. Everything else it reports should be readable but not writable, and OPC UA has a flag for exactly that: `writable=False`. Set it, and the value can still be read; an incoming write request is rejected instead of accepted.

`Heater` is the clearest example. It looks like something an operator should be able to switch — but the simulation drives it as part of the batch cycle, and a write from outside would just be overwritten again on the next tick. So it's locked down, and placed where it actually belongs: under `Actuators/`, not `Status/`.

```python
actuators = server.addObject("Actuators", sys, nodeId="ns=1;i=1500")
heater = server.addVariable(
    "Heater",
    actuators,
    False,
    nodeId="ns=1;i=1503",
    writable=False,
)
```

!!! info
    `writable=False` clears a bit in the Variable's `AccessLevel` attribute — the field a client checks before it writes at all. From here on, the distillery's rule is simple: `Setpoint` and `Operating` are the only two values anyone outside the server may change. Everything else — kettle readings, valve and heater state, identification text — is read-only, because the simulation (or the machine's nameplate) is the one source of truth for it.

The same reasoning covers `Identification/`: three lines of descriptive text about the machine that nobody ever writes to.

```python
ident = server.addObject("Identification", sys, nodeId="ns=1;i=1100")
server.addVariable("Name",         ident, "Distilling Demo Still", nodeId="ns=1;i=1101", writable=False)
server.addVariable("Manufacturer", ident, "o6 Tutorials",          nodeId="ns=1;i=1102", writable=False)
server.addVariable("ModelNumber",  ident, "DS-1000",               nodeId="ns=1;i=1103", writable=False)
```

Three calls, the same shape as everything above.

---

## When the exact wire type matters

The inference table further up covers every value the tutorials actually use — but it's worth knowing its limit: Python has only one `int` and one `float`, so it can't tell an `Int32` from an `Int64`, or a `Float` from a `Double`. When that distinction matters, `dataType=` states it directly instead of leaving it to inference:

```python
import o6

cycle = server.addVariable(
    "Cycle",
    status,
    0,
    nodeId="ns=1;i=1202",
    dataType=o6.Int32,      # explicit, instead of leaving int → Int32 to inference
    writable=False,
)
```

`Cycle` is still a plain `int` on the Python side either way — `dataType=` only changes what goes out on the wire. It's worth remembering for later; most of what we build in these tutorials won't need it.

---

## What's next?

The distillery now has `Setpoint` and `Operating` under `Status/`, three lines of `Identification/` text, and a read-only `Heater` under `Actuators/`. It can already answer a read and accept a write. What it still can't do is act on a request — the next page gives it a first one of those: a `Shutdown` method a remote request can call.

- [Add a method](120_add-method.md) — register a callable method, return values and `StatusCode`.
- [Server manual](../../manual/server/address-space.md#variables) — every keyword argument on `addVariable`, including `dataType=`, `valueRank`, and `historizing=`.
