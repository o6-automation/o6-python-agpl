# Client

The client API gives Python applications access to OPC UA services through two layers.

OPC UA is defined around service sets, which are groups of related service operations such as SecureChannel/Session management, Discovery, Read/Write, Browse, Method Call, and Subscription. The raw service interface exposes these low-level operations directly through `Client` methods named `serviceX`, such as `serviceRead`, and closely mirrors the OPC UA specification. They enable us to construct and send request objects and return response objects.

On top of that, o6 provides a higher-level interface for the common workflows of connecting, reading, writing, browsing, calling methods, and creating subscriptions. This layer hides the request-building boilerplate, handles session and channel lifecycle, resolves NodeIds, decodes results into Python values, and supports both synchronous and asynchronous use. For the majority of all application scenarios these higher-level functions should suffice and be preferred.


## Client Lifecycle

The `Client` manages the required asyncio machinery internally, including the event loop and the scheduling of OPC UA service requests. High-level methods such as `connect()`, `read()`, `write()`, and `disconnect()` abstract the low-level request construction and session/channel management.

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
- `connect(noSession=True)` and `disconnect(closeSession=False)` if only the SecureChannel should be managed
- `connected` to inspect the current connection state
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

Advanced session reactivation is available through `activateCurrentSession()` and
`activateSession(authToken, serverNonce)`.

For reverse connect scenarios, the client can listen for incoming reverse connections:

```python
client.startReverseConnect(port=4840, hostnames=["0.0.0.0"])
```

## Discovery

The client exposes the common discovery services in simplified Python form:

- `getEndpoints(endpointUrl, ...)`
- `findServers(endpointUrl, ...)`
- `findServersOnNetwork(...)`

Example:

```python
from o6 import Client

client = Client()
endpoints = client.getEndpoints("opc.tcp://localhost:4840")
```

These methods are convenience wrappers around the raw discovery service requests and return the decoded result objects directly.

## Services

The raw OPC UA service sets remain available on the client. These methods accept request objects from the generated data types and return the full response objects.

Available service families include:

- Discovery: `serviceFindServers`, `serviceFindServersOnNetwork`, `serviceGetEndpoints`
- Node management: `serviceAddNodes`, `serviceDeleteNodes`, `serviceAddReferences`, `serviceDeleteReferences`
- View: `serviceBrowse`, `serviceBrowseNext`, `serviceTranslateBrowsePathsToNodeIds`, `serviceRegisterNodes`, `serviceUnregisterNodes`
- Attributes and history: `serviceRead`, `serviceWrite`, `serviceHistoryRead`, `serviceHistoryUpdate`
- Methods: `serviceCall`


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

The attribute to read or write can also be selected explicitly with `attributeId=...`, which is useful for metadata such as browse names, data types, or access levels.

```python
client.read("ns=1;s=IntegerVariable", attr=o6.AttributeId.NODE_CLASS)
```

### Method calling

OPC UA methods are called with `call(objectId, methodId, inputArgs=...)`.

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

- `historyRead(...)`
- `historyUpdateInsert(...)`
- `historyUpdateReplace(...)`
- `historyUpdateDelete(...)`

These methods build the corresponding history request types internally and return unpacked Python-facing results.

### Node management

Client-side node management is also available for applications that need to modify a remote address space.

- `addVariableNode(...)`
- `addVariableTypeNode(...)`
- `addObjectNode(...)`
- `addObjectTypeNode(...)`
- `addViewNode(...)`
- `addReferenceTypeNode(...)`
- `addDataTypeNode(...)`
- `addMethodNode(...)`
- `deleteNode(...)`
- `addReference(...)`
- `deleteReference(...)`


## Subscriptions

Subscriptions are handled through a high-level API centered around `createSubscription(...)`.

```python
subscription = client.createSubscription(publishingInterval=1000)
```

The returned subscription object is then used to create monitored items such as data-change subscriptions.

```python
def onDataChange(value):
	print(value)

monitoredItem = client.monitor(
	"ns=1;s=IntegerVariable",
	onDataChange,
	samplingInterval=500,
	subscription=subscription,
)
```

## Client Utility Functions


- `getRemoteDataTypes(...)` to retrieve datatype definitions from the server
- namespace-related helper methods exposed through the underlying API and decoded type system
- node wrappers in `o6.node` for object-oriented access to nodes and attributes


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
	endpointUrl="opc.tcp://localhost:4840",
	securityMode=SecurityMode.SIGN_AND_ENCRYPT,
	securityPolicy=SecurityPolicy.BASIC256SHA256,
	certificate="client_cert.der",
	privateKey="client_key.pem",
)
```

For username/password authentication, pass the credentials to `Client(...)` at construction time.

## Asynchronous Services

The API is designed so the same high-level methods can be used from synchronous and asynchronous code. In synchronous code they block until the result is available; in asynchronous code they can be awaited.

```python
async with Client("opc.tcp://localhost:4840") as client:
	value = await client.read("ns=1;s=IntegerVariable")
```
