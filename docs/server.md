# Server

Configure the server, start it, build the address space, and expose values, methods, and references to clients.

## Server Lifecycle

The main entry point is `o6.Server`.

```python
from o6 import Server

server = Server(port=4840)
server.start()
server.stop()
```

Like the client, the server can also be used as a context manager.

```python
from o6 import Server

with Server(port=4840) as server:
	...
```

The high-level lifecycle methods are:

- `Server(...)` to create a server with the default configuration
- `start()` to run startup and begin serving
- `stop()` to shut the server down cleanly
- `running` from the underlying object to inspect whether the server is active

The API manages the event loop details internally. In synchronous code, `start()` launches the event loop in a background thread when needed. In asynchronous code, startup runs directly on the active loop.

## Server Configuration

The server configuration is available through `server.config`. It should be adjusted before the server is running.

Common configuration areas exposed by the API include:

- `application_uri`
- `application_description`
- encryption and certificate handling
- accepting all certificates for test setups

Example:

```python
from o6 import Server, ApplicationDescription, LocalizedText

server = Server(port=4840)

app = server.config.application_description
app.application_name = LocalizedText("en-US", "o6-python Test Server")
server.config.application_description = app
```

Encryption can be configured directly in the `Server(...)` constructor with:

- `certificate`
- `private_key`
- `trust_list`
- `issuer_list`
- `revocation_list`
- `secure_only`
- `accept_all_certificates`


## Address Space and Node Management

The Python server focuses on high-level node creation helpers rather than raw `AddNodes` structures.

Available helpers include:

- `add_object(...)`
- `add_variable(...)`
- `add_method(...)`
- `add_object_type(...)`
- `add_variable_type(...)`
- `add_reference(...)`
- `delete_node(...)`

These methods return `ServerNode` wrappers, which provide a compact Python interface over the created nodes.

### Objects

Objects are created below a parent node, usually the Objects folder.

```python
plant = server.add_object("Plant", server.objects_node)
```

### Variables

Variables can be created with an initial value, an optional explicit NodeId, and a data type inferred from the Python value.

```python
temperature = server.add_variable(
	"Temperature",
	plant,
	22.5,
	nodeid="ns=1;i=1001",
)
```

By default, `add_variable(...)` creates readable and writable variables. The helper can also mark variables as historizing and can accept an explicit datatype.

### Methods

Methods are exposed by attaching a Python callback to an object node.

```python
from o6.server import make_argument

def add_numbers(a, b):
	return [a + b]

server.add_method(
	"Add",
	plant,
	add_numbers,
	input_args=[
		make_argument("A", "i=11"),
		make_argument("B", "i=11"),
	],
	output_args=[
		make_argument("Sum", "i=11"),
	],
)
```

### References and deletion

References can be managed explicitly.

```python
server.add_reference(source_node, target_node, reference_type)
server.delete_node(nodeid, delete_references=True)
```

## Read and Write Operations

Server-side value access is intentionally simple:

- `read_value(nodeid)`
- `write_value(nodeid, value)`

The returned `ServerNode` objects expose the same functionality through the `value` property.

```python
temperature.value = 23.0
current = temperature.value
```

## Node Types

The API also exposes helpers for type nodes.

- `add_object_type(...)`
- `add_variable_type(...)`


## Reverse Connect

The server API exposes reverse connect support:

- `add_reverse_connect(url, callback=None)`
- `remove_reverse_connect(handle)`


## Utility Helpers

Several commonly used node identifiers:

- `OBJECTS_FOLDER`
- `TYPES_FOLDER`
- `VIEWS_FOLDER`
- `SERVER_NODE`
- `BASE_OBJECT_TYPE`
- `BASE_VARIABLE_TYPE`
- `BASE_DATA_VARIABLE_TYPE`
- `ORGANIZES`
- `HAS_COMPONENT`
- `HAS_PROPERTY`
- `HAS_TYPE_DEFINITION`
- `HAS_SUBTYPE`

The helper `make_argument(...)` simplifies method signature creation.

```python
from o6.server import make_argument

arg = make_argument("Temperature", "i=11", description="Current value")
```

For concrete examples, start with the basic server walkthrough in [examples/server-basic.md](examples/server-basic.md) and the other server examples in the examples section.
