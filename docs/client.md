# Client

The client API gives Python applications access to OPC UA services through two layers.

OPC UA is defined around service sets, which are groups of related service operations such as SecureChannel/Session management, Discovery, Read/Write, Browse, Method Call, and Subscription. The raw service interface exposes these low-level operations directly, so you can construct and send requests that closely mirror the OPC UA specification.

On top of that, o6 provides a higher-level interface for the common workflows of connecting, reading, writing, browsing, calling methods, and creating subscriptions. This layer hides the request-building boilerplate, handles session and channel lifecycle, resolves NodeIds, decodes results into Python values, and supports both synchronous and asynchronous use. 


## Client Lifecycle

The main entry point is `o6.Client`. It manages the required asyncio machinery internally, including the event loop and the scheduling of OPC UA service requests. High-level methods such as `connect()`, `read()`, `write()`, and `disconnect()` abstract the low-level request construction and session/channel management.

In synchronous code, these methods block until the request completes. In asynchronous code, the same methods are awaitable, and the caller uses `await` to suspend until the result is available. This provides a consistent API surface across synchronous and asynchronous usage.

```python
from o6 import Client

client = Client("opc.tcp://localhost:4840")
client.connect()
client.disconnect()
```

The client may also be used as a context manager. In this form, connection setup and teardown are handled automatically, which is more idiomatic for Python applications.

```python
from o6 import Client

with Client("opc.tcp://localhost:4840") as client:
    value = client.read("ns=1;s=IntegerVariable")
```

The most important lifecycle-related properties and methods are:

- `Client(...)` to create a client instance
- `connect(...)` to open a SecureChannel and activate a Session
- `disconnect()` to close the connection and clean up subscriptions
- `connect_secure_channel(...)` and `disconnect_secure_channel()` if only the SecureChannel should be managed
- `connected` and `fully_connected` to inspect the current connection state
- `state` to get the current channel state, session state, and status code

## Connect to a Server

Configure the client, open a SecureChannel, then create and activate a Session.

The simplest form is:

```python
from o6 import Client

client = Client()
client.connect("opc.tcp://localhost:4840")
```

Username and password can be supplied at construction time.

```python
client = Client(
	"opc.tcp://localhost:4840",
	username="user1",
	password="password",
)
client.connect()
```

Session transfer is also supported. The current session token and server nonce can be retrieved from one client and activated on another client.

- `get_session_authentication_token()`
- `activate_current_session()`
- `activate_session(auth_token, server_nonce)`

For reverse connect scenarios, the client can listen for incoming reverse connections:

```python
client.start_reverse_connect(port=4840, hostnames=["0.0.0.0"])
```

## Discovery

The client exposes the common discovery services in simplified Python form:

- `get_endpoints(server_url, ...)`
- `find_servers(server_url, ...)`
- `find_servers_on_network(...)`

Example:

```python
from o6 import Client

client = Client()
endpoints = client.get_endpoints("opc.tcp://localhost:4840")
```

These methods are convenience wrappers around the raw discovery service requests and return the decoded result objects directly.

## Services

The raw OPC UA service sets remain available on the client. These methods accept request objects from the generated data types and return the full response objects.

Available service families include:

- Discovery: `service_find_servers`, `service_find_servers_on_network`, `service_get_endpoints`
- Node management: `service_add_nodes`, `service_delete_nodes`, `service_add_references`, `service_delete_references`
- View: `service_browse`, `service_browse_next`, `service_translate_browse_paths_to_nodeids`, `service_register_nodes`, `service_unregister_nodes`
- Attributes and history: `service_read`, `service_write`, `service_history_read`, `service_history_update`
- Methods: `service_call`


## High-Level Client Functionality

For most application code, the high-level API is the preferred entry point. It encapsulates OPC UA request construction, session management, value decoding, and error handling so application developers can operate on Python-friendly inputs and outputs without dealing directly with the raw service protocol.

### Read and write attributes

`read(...)` and `write(...)` are the main convenience methods. They can work on a single node or on multiple nodes in one call.

```python
value = client.read("ns=1;s=IntegerVariable")
client.write("ns=1;s=IntegerVariable", 42)
```

Multiple values can be read by passing a list, and multiple writes can be issued by passing a mapping.

```python
values = client.read([
	"ns=1;s=IntegerVariable",
	"ns=1;s=DoubleVariable",
])

client.write({
	"ns=1;s=IntegerVariable": 100,
	"ns=1;s=DoubleVariable": 2.7182,
})
```

The attribute to read or write can also be selected explicitly with `attribute_id=...`, which is useful for metadata such as browse names, data types, or access levels.

```python
client.read("ns=1;s=IntegerVariable", attributeid=o6.AttributeId.NODECLASS)
```

### Method calling

OPC UA methods are called with `call(object_id, method_id, input_args=...)`.

```python
status, result = client.call(
	"ns=1;s=TestMethods",
	"ns=1;s=MethodHelloString",
	["World"],
)
```

The return value contains the method status code followed by the decoded output arguments.

### Browsing

The browse API is intentionally compact and maps well to the OPC UA view service set.

```python
references = client.browse("i=85")
```

Optional parameters such as browse direction, reference type, subtype inclusion, node class mask, and result mask can be used to narrow the result.

The client also exposes entry-point nodes as convenience properties:

- `root`
- `objects`
- `types`
- `views`

### History access

The API exposes several convenience methods for historical access:

- `history_read(...)`
- `history_read_modified(...)`
- `history_read_at_time(...)`
- `history_read_processed(...)`
- `history_update(...)`

These methods build the corresponding history request types internally and return unpacked Python-facing results.

### Node management

Client-side node management is also available for applications that need to modify a remote address space.

- `add_node(...)`
- `add_variable_node(...)`
- `add_variable_type_node(...)`
- `add_object_node(...)`
- `add_object_type_node(...)`
- `add_view_node(...)`
- `add_reference_type_node(...)`
- `add_data_type_node(...)`
- `add_method_node(...)`
- `delete_node(...)`
- `add_reference(...)`
- `delete_reference(...)`


## Subscriptions

Subscriptions are handled through a high-level API centered around `create_subscription(...)`.

```python
subscription = client.create_subscription(publishing_interval=1000)
```

The returned subscription object is then used to create monitored items such as data-change subscriptions.

```python
def on_data_change(node, value, data_value):
	print(node, value)

monitored_item = subscription.monitor_data_change(
	"ns=1;s=IntegerVariable",
	on_data_change,
	sampling_interval=500,
)
```

## Client Utility Functions


- `get_remote_data_types(...)` to retrieve datatype definitions from the server
- namespace-related helper methods exposed through the underlying API and decoded type system
- node wrappers in `o6.client_nodes` for more object-oriented access to nodes and attributes


## Client Configuration

Common configuration areas include:

- endpoint URL and endpoint selection
- security mode and security policy
- application URI and session name
- requested session timeout and locale IDs
- certificates, private key, trust list, and revocation list
- username/password or certificate-based session authentication

A secure configuration:

```python
from o6 import Client, SecurityMode, SecurityPolicy

client = Client(
	endpoint_url="opc.tcp://localhost:4840",
	security_mode=SecurityMode.SIGN_AND_ENCRYPT,
	security_policy=SecurityPolicy.BASIC256SHA256,
	certificate="client_cert.der",
	private_key="client_key.pem",
)
```

For username/password authentication, pass the credentials to `Client(...)` at construction time.

## Asynchronous Services

The API is designed so the same high-level methods can be used from synchronous and asynchronous code. In synchronous code they block until the result is available; in asynchronous code they can be awaited.

```python
async with Client("opc.tcp://localhost:4840") as client:
	value = await client.read("ns=1;s=IntegerVariable")
```
