# Nodes as Objects

The Node API makes an OPC UA address space feel like a graph of Python
objects. Navigate to a Variable and call it to read or write; navigate to a
Method and call it with its inputs. The same syntax works on a connected
client and inside a local server.

## A taste

Start the [example server below](#example-server) in another terminal, then
run this client:

```python
import o6

with o6.Client("opc.tcp://localhost:4840") as client:
    plant = client.objects.plant
    plant.counter(42)                         # Write the Variable's Value.
    print("value:", plant.counter())          # Read it back.
    status, greeting = plant.hello("o6")       # Call the Method.
    print("greeting:", greeting)
```

Output:

```text
value: 42
greeting: Hello, o6!
```

`plant` is a live node handle, not a copy of the Object's data.
`plant.counter` resolves a child node; `plant.counter()` reads its current
value. The Method returns a status followed by its output arguments, so the
example unpacks the greeting before printing it.

## Motivation

OPC UA already describes applications as Objects with Variables and Methods.
The Node API lets your Python code follow that model directly. You can keep a
handle to a pump, explore its children, and operate on those children without
passing a NodeId to every operation.

There are three levels of access in o6\\Python:

| Interface | How you work |
|---|---|
| Node API | Follow the object model: `plant.counter()`, `plant.counter(42)`, `plant.hello("o6")`. |
| High-level client/server API | Pass targets explicitly: `client.read(nodeId)`, `client.write(nodeId, 42)`, `client.call(objectId, methodId, ["o6"])`. These helpers construct requests for you. |
| Raw client services | Build request objects and inspect responses with methods such as `client.serviceRead(...)`. |

Choose the Node API when the address-space structure is useful to your
application. The high-level APIs are convenient for known identifiers and
batch operations; raw services give you control over the complete request.
The [Client](../client/index.md) and [Server](../server/index.md) chapters
cover those interfaces and their lifecycles.

## Three operators, live nodes

| Syntax | Meaning |
|---|---|
| `parent.child` | Resolve a child by BrowseName or its Python alias. |
| `parent["/1:Child"]` | Resolve a browse path; return a list of matching targets. |
| `node(...)` | Read or write an attribute, or invoke a Method, depending on the node and arguments. |

A handle's Python class follows the node's NodeClass: `ObjectNode`,
`VariableNode`, `MethodNode`, and so on. An Object organizes children; it does
not have a Variable's Value attribute. Names such as `Plant` and `Counter`
become the Python aliases `plant` and `counter`. Detailed matching and
conversion rules live in [BrowseName to Python Names](name-conversion.md).

Public Node helpers deliberately have leading underscores, leaving ordinary
names available for children. For example, `counter._nodeid` identifies the
node and `counter._value` is a convenience property for its Value. These are
public APIs despite their spelling. Use `counter()` for reads and
`counter(42)` for writes throughout this chapter; `counter.value`,
`counter.read`, or `method.call` would attempt child lookup instead.

## Example server

This chapter uses one small address space, separate from the tutorial's
DistillingSystem. All four application nodes have namespace index 1 in this
server:

```text
Objects/
└── Plant             (Object, ns=1;i=1000)
    ├── Counter       (Variable, Int32, read/write, ns=1;i=1001)
    ├── Label         (Variable, String, read/write, ns=1;i=1002)
    └── Hello         (Method, String → String, ns=1;i=2001)
```

Save this as `node_server.py` and run it with `python node_server.py`. It
creates the model, starts listening at `opc.tcp://localhost:4840`, and stays
available until you press Enter. The context manager stops it on exit.

```python
import o6
from o6.ns import ns0


def hello(node, name):
    return o6.StatusCode.GOOD, f"Hello, {name}!"


server = o6.Server(port=4840)
plant = server.addObject("Plant", server.objects, nodeId="ns=1;i=1000")
server.addVariable("Counter", plant, 0, nodeId="ns=1;i=1001", writable=True)
server.addVariable("Label", plant, "ready", nodeId="ns=1;i=1002", writable=True)
server.addMethod(
    "Hello",
    plant,
    hello,
    nodeId="ns=1;i=2001",
    inputArgs=[ns0.datatypes.Argument(
        name="Name", dataType=o6.String, valueRank=o6.ValueRank.SCALAR,
    )],
    outputArgs=[ns0.datatypes.Argument(
        name="Greeting", dataType=o6.String, valueRank=o6.ValueRank.SCALAR,
    )],
)

with server:
    input("Server ready. Press Enter to stop.\n")
```

The `addObject`, `addVariable`, and `addMethod` helpers build the address
space; their full options are covered in
[Building the address space](../server/address-space.md). No custom nodeset
package is needed for this example.

### The same objects from the server

Server code accesses local nodes through the same operators. For example,
insert this fragment inside the `with server:` block, before `input(...)`:

```python
plant = server.objects.plant
plant.counter(42)
print("value:", plant.counter())
status, greeting = plant.hello("o6")
print("greeting:", greeting)
```

It prints the same output as the client. Local operations do not need a
network connection. A client handle belongs to its client session; a server
handle belongs to its local server. Keep the owning client or server alive
while using its nodes. The Server chapter explains
[local handle identity and lifetime](../server/local-nodes.md).

## Entry points

Both clients and servers expose the four standard folders as node handles:

| Client | Server | NodeId | What's inside |
|---|---|---|---|
| `client.root` | `server.root` | `i=84` | The address-space root, containing the folders below. |
| `client.objects` | `server.objects` | `i=85` | Application Objects, Variables, and Methods. |
| `client.types` | `server.types` | `i=86` | ObjectTypes, VariableTypes, ReferenceTypes, and DataTypes. |
| `client.views` | `server.views` | `i=87` | Server-defined Views, if any. |

These folder handles are available directly, including in async code.
Start from `objects` for most application work. Once you have a node, you can
[read, write, or call it](read-write-call.md), or
[navigate further and look up other nodes](navigation.md).
