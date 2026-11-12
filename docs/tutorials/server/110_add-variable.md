# Add a variable

This page adds the first values to the folders from [Add a hierarchy](105_add-hierarchy.md): the two values an operator changes, `Setpoint` and `Operating`, then read-only values such as `Heater` and the `Identification/` text. A Variable is a named slot with a value, attached to a parent node.

---

## Give `Setpoint` a home

`Server.addVariable()` creates a Variable. It takes the name, the parent folder and the initial value, in that order:

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

The parent is `status`, not `server.objectsNode`, so `Setpoint` appears inside the `Status` folder where a browsing client expects it.

`nodeId=` pins the address, as for the folders. `Setpoint` stays at `ns=1;i=1204` across restarts, so later pages and the client tutorials can rely on it.

`o6` infers the OPC UA type from the Python value:

| Python value | OPC UA DataType |
|---|---|
| `85.0` (a `float`) | `Double` |
| `1013` (an `int`) | `Int32` |
| `"idle"` (a `str`) | `String` |
| `True` (a `bool`) | `Boolean` |

`85.0` is a `float`, so `Setpoint` is a `Double`.

!!! info
    The `ns=1` in `ns=1;i=1204` is a namespace index. Namespaces keep
    different vendors' NodeIds from colliding. `1` is the default for nodes
    a server defines itself, so every NodeId in these tutorials starts with
    it.

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

To check it, read the value, write a new one and read it back:

```python
print(server.read("ns=1;i=1204"))   # 85.0
server.write("ns=1;i=1204", 90.0)
print(server.read("ns=1;i=1204"))   # 90.0
```

---

## A shorter way to reach the same value

`addVariable(...)` returns a live handle to the Variable. Call it with no arguments to read and with one argument to write:

```python
print(setpoint())                 # 85.0  — read via the handle
setpoint(90.0)                    # write via the handle
```

Later pages use this form because it is shorter than `server.read(...)`/`server.write(...)`. Both reach the same value:

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

`Operating` is a `True`/`False` flag in `Status/` that says whether the distillery should run batches.

```python
operating = server.addVariable("Operating", status, True, nodeId="ns=1;i=1203", writable=True)
```

The value is a `bool`, so it becomes a `Boolean`. `writable=True` is the default; it is spelled out here because the next section turns it off.

---

## Values that shouldn't be writable

Everything else the still reports is read-only. With `writable=False`, the value can still be read, and write requests are rejected.

`Heater` looks like a switch, but the simulation drives it as part of the batch cycle and would overwrite an external write on the next tick. It is read-only and sits under `Actuators/`, not `Status/`:

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
    `writable=False` clears a bit in the Variable's `AccessLevel`
    attribute, which a client checks before it writes. In the distillery,
    `Setpoint` and `Operating` are the only values a client may change.
    Kettle readings, valve and heater state and identification text are
    read-only, because the simulation (or the machine's nameplate) is their
    source of truth.

`Identification/` holds three read-only strings that describe the machine:

```python
ident = server.addObject("Identification", sys, nodeId="ns=1;i=1100")
server.addVariable("Name",         ident, "Distilling Demo Still", nodeId="ns=1;i=1101", writable=False)
server.addVariable("Manufacturer", ident, "o6 Tutorials",          nodeId="ns=1;i=1102", writable=False)
server.addVariable("ModelNumber",  ident, "DS-1000",               nodeId="ns=1;i=1103", writable=False)
```

---

## When the exact wire type matters

Type inference covers every value in the tutorials. Python has only one `int` and one `float`, so inference cannot choose between `Int32` and `Int64`, or `Float` and `Double`. When the distinction matters, set `dataType=`:

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

`Cycle` is a plain `int` on the Python side either way. `dataType=` only changes the wire type.

---

## Next steps

The server answers reads and accepts writes, but cannot act on a request yet. The next page adds a `Shutdown` method that clients can call.

| Topic | What it covers |
|---|---|
| [Add a method](120_add-method.md) | Register a callable method, return values and `StatusCode`. |
| [Server manual](../../manual/server/address-space.md#variables) | Every keyword argument on `addVariable`, including `dataType=`, `valueRank`, and `historizing=`. |
