# Add a hierarchy

The server from [Creating a server](100_create-server.md) is listening, but its address space under `Objects/` is empty — only the standard nodes every OPC UA server carries are there. Before adding anything to it, it's worth deciding what the distillery's address space should actually look like, rather than growing it one node at a time as an afterthought. This page builds that shape: a `DistillingSystem` folder with six sub-objects — `Identification`, `Status`, `Kettle`, `Distillate`, `Actuators`, and `Events` — each one waiting for the values the next few pages will put inside it.

By the end of this page the address space matches the layout every later tutorial assumes:

```
Objects/
└── DistillingSystem/
    ├── Identification/    Name, Manufacturer, ModelNumber
    ├── Status/            State, Cycle, Operating, Setpoint
    ├── Kettle/            Level, Temperature, WashStart
    ├── Distillate/        Level
    ├── Actuators/         FillValve, DrainValve, Heater
    ├── Events/            EventCount, LastEventTime, LastEventMessage, LastEventState
    ├── Start              (Method)
    └── Shutdown           (Method)
```

---

## A folder is just another node: `addObject`

`Server.addObject()` adds an `Object` node — in practice, a folder — to the address space. Like `addVariable` (the next page), the first two positional arguments are the name and the parent, and `nodeId=` pins the address:

```python
from o6 import Server

server = Server(port=4840)
sys = server.addObject("DistillingSystem", server.objectsNode, nodeId="ns=1;i=1000")

# `sys` is now a parent for everything else — including further folders.
status = server.addObject("Status", sys, nodeId="ns=1;i=1200")
```

That single line gives us a folder, and the second line gives us a folder inside it — `status` ends up nested two levels under `Objects/`, not directly beneath it, because its parent is `sys` rather than `server.objectsNode`. That's the whole idea behind a hierarchy: each `addObject` call decides where one more branch attaches, and the address space grows from there.

Neither `sys` nor `status` carries a value yet — they're folders, not Variables. Values are what the next page adds.

!!! info
    Every node class attaches to its parent with a fixed reference type — `Object` and `Variable` with `Organizes`, `Method` with `HasComponent` — chosen automatically, not something `addObject`/`addVariable` take as an argument. A different kind of edge is possible, but it means creating the node first and adding the reference separately with `Server.addReference` — a technique [its own later page](220_declare-reference-type.md) covers.

#### Putting it all together — the smallest meaningful hierarchy

```python
import time
from o6 import Server

server = Server(port=4840)

# Top-level folder
sys = server.addObject("DistillingSystem", server.objectsNode, nodeId="ns=1;i=1000")

# Nested folders inside it
status = server.addObject("Status", sys, nodeId="ns=1;i=1200")
kettle = server.addObject("Kettle", sys, nodeId="ns=1;i=1300")

server.start()
```

A read of `Objects/` now sees:

```
DistillingSystem (Object, ns=1;i=1000)
├── Status (Object, ns=1;i=1200)
└── Kettle (Object, ns=1;i=1300)
```

That's the first two layers of the distillery. The rest of this page just repeats the same call a few more times.

---

## Building the rest of the skeleton

The full skeleton adds four more sub-objects next to `Status` and `Kettle` — `Identification`, `Distillate`, `Actuators`, `Events` — all still just as empty. Deciding the structure up front, before any value exists to put inside it, means every later page already knows exactly where its Variables and Methods belong:

```python
from o6 import Server

server = Server(port=4840)
sys = server.addObject("DistillingSystem", server.objectsNode, nodeId="ns=1;i=1000")

ident = server.addObject("Identification", sys, nodeId="ns=1;i=1100")
status = server.addObject("Status", sys, nodeId="ns=1;i=1200")
kettle = server.addObject("Kettle", sys, nodeId="ns=1;i=1300")
distillate = server.addObject("Distillate", sys, nodeId="ns=1;i=1400")
actuators = server.addObject("Actuators", sys, nodeId="ns=1;i=1500")
events = server.addObject("Events", sys, nodeId="ns=1;i=1600")
```

Every NodeId here is one every later page reuses without redefining it, so it's worth taking a moment to notice the pattern: each folder gets a round hundred (`i=1100`, `i=1200`, `i=1300`, ...), leaving room for the values that go inside each one to sit close by in the numbering.

#### Putting it all together

```python
import time
from o6 import Server


def build_address_space(server: Server):
    sys = server.addObject("DistillingSystem", server.objectsNode, nodeId="ns=1;i=1000")

    ident = server.addObject("Identification", sys, nodeId="ns=1;i=1100")
    status = server.addObject("Status", sys, nodeId="ns=1;i=1200")
    kettle = server.addObject("Kettle", sys, nodeId="ns=1;i=1300")
    distillate = server.addObject("Distillate", sys, nodeId="ns=1;i=1400")
    actuators = server.addObject("Actuators", sys, nodeId="ns=1;i=1500")
    events = server.addObject("Events", sys, nodeId="ns=1;i=1600")

    return sys, ident, status, kettle, distillate, actuators, events


server = Server(port=4840)
build_address_space(server)
server.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pass

server.stop()
```

The address space is now the right shape: every folder in place, every future leaf's parent already decided. Nothing in it has a value yet — that's deliberately the next page's job, not this one's.

---

## What's next?

- [Add a variable](110_add-variable.md) — drop the first writable Variable under `Status/`.
- [Add a method](120_add-method.md) — register a callable method on the distillery.
- [Variables with sources](320_variables-with-sources.md) — much later, install read and write callbacks with `Server.implement(...)` and connect this skeleton to a real simulation.
