# Add a hierarchy

This page adds the distillery's folder skeleton to the server from [Creating a server](100_create-server.md): a `DistillingSystem` folder with six sub-objects, `Identification`, `Status`, `Kettle`, `Distillate`, `Actuators` and `Events`. The next pages fill them with values. The finished layout, which every later tutorial assumes, is:

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

`Server.addObject()` adds an `Object` node (here, a folder) to the address space. As with `addVariable` on the next page, the first two positional arguments are the name and the parent, and `nodeId=` pins the address:

```python
from o6 import Server

server = Server(port=4840)
sys = server.addObject("DistillingSystem", server.objectsNode, nodeId="ns=1;i=1000")

# `sys` is now a parent for everything else — including further folders.
status = server.addObject("Status", sys, nodeId="ns=1;i=1200")
```

`status` sits two levels under `Objects/` because its parent is `sys`, not `server.objectsNode`. Each `addObject` call decides where one branch attaches. Neither folder carries a value; Variables come on the next page.

!!! info
    Every node class attaches to its parent with a fixed reference type:
    `Object` and `Variable` with `Organizes`, `Method` with `HasComponent`.
    `addObject`/`addVariable` choose it automatically and don't take it as
    an argument. For a different edge, create the node first and add the
    reference with `Server.addReference`, as covered in
    [Declare a reference type](220_declare-reference-type.md).

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


---

## Building the rest of the skeleton

The full skeleton adds four more empty sub-objects next to `Status` and `Kettle`: `Identification`, `Distillate`, `Actuators` and `Events`. With the structure fixed up front, every later page knows where its Variables and Methods belong:

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

Later pages reuse these NodeIds without redefining them. Each folder gets a round hundred (`i=1100`, `i=1200`, `i=1300`, ...), and the values inside it take the numbers that follow.

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

Every folder is in place. None of them has a value yet.

---

## Next steps

| Topic | What it covers |
|---|---|
| [Add a variable](110_add-variable.md) | Drop the first writable Variable under `Status/`. |
| [Add a method](120_add-method.md) | Register a callable method on the distillery. |
| [Variables with sources](320_variables-with-sources.md) | Install read and write callbacks with `Server.implement(...)` and connect this skeleton to a real simulation. |
