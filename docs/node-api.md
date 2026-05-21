# Node API

o6 gives you direct, pythonic access to OPC UA nodes and data types through the object model exposed by a connected client.

This is more than a service-based wrapper. Instead of only sending raw OPC UA requests, you can navigate the server's address space like a normal Python object, including both nodes and type definitions.


## Motivation

A service-based API is centered around OPC UA requests and response objects, buliding `ReadRequest`s, sending them, and parsing the result. That is powerful and explicit, but it is also low-level.

The Node API is a higher-level, object-oriented layer on top of the OPC UA services.

| Service API | Node API |
|---|---|
| `client.service_read(...)` | `client.root.objects.MyVariable.read()` |
| `client.service_write(...)` | `client.root.objects.MyVariable(123)` |
| `client.service_call(...)` | `client.objects.MyMethod.call(...)` |

The `.` syntax in the Node API gives you canonical Python access to the server's actual UA objects, wrapped as Python node objects. This blends OPC UA's object-oriented model with Python object orientation so your code feels natural and easy to follow.

- It reduces boilerplate compared to manually constructing service requests.
- It makes address-space traversal readable and discoverable.
- It preserves OPC UA semantics while fitting naturally into Python code.
- It gives a smoother onboarding path for application developers who want the flexibility of OPC UA without leaving Python's object model.

The Node API is the bridge between OPC UA's object-oriented server model and Python's own object orientation.


## Easy access to OPC UA nodes

When a client connects, it exposes the server entry points as Python objects:

- `client.root`
- `client.objects`
- `client.types`
- `client.views`

These objects are live views into the server. That means the dotted attribute syntax represents the actual OPC UA nodes in the server address space, wrapped in Python node objects.

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


## Data types through namespaces

Node API also makes data type access intuitive. Namespaces are exposed as Python packages under `o6.ns`.

```python
from o6 import Client

# get the nodeid for the datatype
info = o6.ns.di.datatypes.FetchResultDataType.TransferResultDataDataType()
# structs and enums can be directly instantiated 
pyclass = o6.ns.di.FetchResultDataType
instance = o6.ns.di.FetchResultDataType()
print(info)
print(pyclass)
print(instance)
```

Expected output:

```text
o6.NodeId('ns=1;i=15889')
<class 'o6.di.TransferResultDataDataType'>
{sequence_number=0, end_of_results=False, parameter_defs=[]}
```

Because `o6.ns.di` is a prebuilt namespace object, you can use it even before a client connects. 
We make use of these prebuilt namespace objects or custom xml defined nodesets in a client in a single line, before connecting the client:

```python
import o6

client = o6.Client("opc.tcp://localhost:4840")
client.ns.append(o6.ns.di)
client.ns.append("custom.nodeset2.xml")
client.connect()

info = client.ns.custom.datatypes.CustomDataType()
pyclass = client.ns.custom.CustomDataType
instance = client.ns.costom.CustomDataType()
print(info)
print(pyclass)
print(instance)
```

Expected output:

```text
o6.NodeId('ns=2;i=12345')
<class 'o6.custom.MyCustomType'>
{member_a=0, member_b=0.0, member_c=False}
```

`o6.ns.di.TransferResultDataDataType()` constructs a Python representation of the OPC UA data type from the `di` namespace. The same pattern works for your own custom NodeSet definitions. Your code stays idiomatic while still using UA schema-derived types.

Types from the OPC UA schemas like `o6.ns.di` may be shared between clients, a type object created once can be reused by multiple clients no need for explicit namespace index conversions. Each client maintains its own namespace mapping, so the shared DI definitions are translated to the local client namespace index automatically when you append `ns.di` to that client. 

