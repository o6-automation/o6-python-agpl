# Node API

**o6\\** gives you direct, pythonic access to OPC UA nodes and data types through the object model exposed by a connected client.

```python
value = client.root.objects.MyVariable() # reads MyVariable on connected server
```

The Node API is more than a service-based wrapper. You can navigate an OPC UA server's address space — including both nodes and type definitions — using Python's regular attribute, subscript, and call operators. Those operators are translated into service requests like `Browse`, `Read`, `Write`, `Call`, letting you write expressions like the one above without ever constructing a request object.

## A taste

```python
from o6 import Client

with Client("opc.tcp://localhost:4840") as client:
    print(client.objects.MyInteger())              # read
    client.objects.MyInteger(42)                   # write
    print(client.objects.TestMethods.Hello("o6")) # call
```

Jump straight to the [NodeAPI Usage](node-api/usage.md).

## Motivation

A service-based API is centered around OPC UA requests and response objects: building `ReadRequest`s, sending them, and parsing the result. This is powerful and explicit, but it is also low-level and often very verbose.

The Node API is a higher-level, object-oriented layer on top of the OPC UA services.

| Service API | Node API |
|---|---|
| `client.serviceRead(...)` | `client.root.objects.MyVariable.read()` |
| `client.serviceWrite(...)` | `client.root.objects.MyVariable(123)` |
| `client.serviceCall(...)` | `client.objects.MyMethod.call(...)` |

The `.` syntax in the Node API gives you canonical Python access to the server's actual UA objects, wrapped as Python node objects. This blends OPC UA's object-oriented model with Python's own object orientation so your code feels natural and easy to follow.

- It reduces boilerplate compared to manually constructing service requests.
- It makes address-space traversal readable and discoverable.
- It preserves OPC UA semantics while fitting naturally into Python code.
- It gives a smoother onboarding path for application developers who want the flexibility of OPC UA without leaving Python's object model.

The Node API is the bridge between OPC UA's object-oriented server model and Python's own object orientation.

## Easy access to OPC UA nodes from a client

When a client has connected, it exposes the server entry points as Python objects:

- `client.root`
- `client.objects`
- `client.types`
- `client.views`

These objects are live views into the server. The dotted attribute syntax represents the actual OPC UA nodes in the server address space, wrapped in Python node objects. Each path component is resolved on demand through a `Browse` request, cached for the lifetime of the node, and invalidated automatically when the model changes.

```python
from o6 import Client

client = Client("opc.tcp://localhost:4840")
client.connect()

node = client.root.objects.MyVariable

# The node object supports call-style to access attributes
print(node())                     # read the node value
print(node(attr="BrowseName"))    # read a specific attribute by name
# or use the OPC UA AttributeId enum
# print(node(attr=o6.AttributeId.BROWSE_NAME))
node(123)                         # write a new value to the node
```

Expected output:

```text
np.int32(42)
o6.QualifiedName('1:MyVariable')
```

In the example above, `client.root.objects.MyVariable` is a direct path into the server's object hierarchy. The node returned behaves like a Python object, while still representing the underlying UA node.

> Important: a node object can be safely cached for later use, only when we are sure the server model remains unchanged and the node is not being removed or renamed on the server side.


## What's next

The [next page](node-api/usage.md) walks through read, write, and call operations on a connected server and shows how the Node API supports interactive autocompletion in a Python REPL.