# Tutorials

## Intro Example in a Python Shell

This quick example assumes an OPC UA server is already running on `localhost:4840`. It shows the minimal flow from connect to read/write and disconnect using the high-level `Client`.

### 1. Import the required objects

The `Client` class is the main entry point for a high-level OPC UA workflow. For namespace-aware references, `o6.ns` provides convenient helpers and prebuilt namespace definitions.

```python
import o6
```

### 2. Create a client and connect

Initialize the client with the server endpoint and connect. This establishes the OPC UA session and prepares the client for subsequent requests.

```python
client = o6.Client("opc.tcp://localhost:4840")
client.connect()
```

### 3. Browsing namespaces with o6.ns 

The `o6.ns` module lets you address OPC UA nodes using namespace-aware helpers and built-in identifiers. This keeps your code clearer and reduces the chance of mistakes when working with standard names or custom namespaces.

```python
current_time_nodeid = o6.ns.ns0.objects.Root.Objects.Server.ServerStatus.CurrentTime()
```

OPC UA companion specs are included as well

```python
o6.ns.di.objects.DeviceSet()
```
> `o6.NodeId('ns=1;i=5001')`

### 4. Read and write values

Use `read` and `write` to interact with NodeIds. If you resolve NodeIds through `o6.ns`, the API stays consistent and easier to maintain.

```python
client.read(current_time_nodeid)
```
> `o6.DateTime(2026-04-20T10:15:00.0000000Z)`

Write variables on the server

```python
client.write("ns=1;s=MyVariable", 20.0)
```

Or browse, read and write nodes directly

```python
client.read(current_time_nodeid)
```
> `o6.DateTime(2026-04-20T10:15:00.0000000Z)`

```python
c.root.Objects.Server.ServerStatus.CurrentTime(attr=o6.AttributeId.NODECLASS)
```
> `<NodeClass.Variable: 2>`

```python
c.root.Objects.MyVariable(123.4)
```



### 5. Disconnect the client

Always disconnect the client when you are done. This cleanly releases the session and any resources held by the connection. Dropping the `Client` object without calling `disconnect()` can cause side effects because cleanup and resource release will happen later in an unspecified order during garbage collection.

```python
client.disconnect()
```
