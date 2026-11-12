# Creating a server

This page creates the OPC UA server for the distillery project: an [`o6.Server`](../../api_reference/server.md) that listens on the network. You construct it, start it, stop it, and check its state. By the end of the Foundation band the server reports on a still: temperature, batch state and a few settings an operator can change.

---

## What is a server, before it does anything?

A server listens on a TCP port and speaks OPC UA to connected clients. It answers questions about its *address space* (the tree of nodes it exposes), reads and writes values on request, and runs background work. Most of these tutorials build the address space.

A newly constructed server is not listening yet. Its address space holds only the standard nodes every OPC UA server carries:

```python
from o6 import Server

server = Server(port=4840)
print(server.running)        # False — not yet listening
print(server.endpointUrl)    # opc.tcp://localhost:4840
```

Constructing a `Server` only configures it. `port=4840` sets where it will listen. Nothing happens on the network until you call `start()`.

---

## Start it, and stop it again

`start()` opens the listening socket and `stop()` closes it. In between, the server accepts connections at `server.endpointUrl`:

```python
import time
from o6 import Server

server = Server(port=4840)
server.start()

print(server.running)        # True
print(server.endpointUrl)    # opc.tcp://localhost:4840

# ... serve ...
server.stop()
print(server.running)        # False
```

`port` defaults to `4840`, the port OPC UA reserves and these tutorials use, so `Server()` binds the same address as `Server(port=4840)`. Certificates, access control and the application URI are covered in [later pages](420_security-policies.md). You can add nodes before or after `start()`.

The process exits as soon as `start()` returns. To keep the server running, wait in a loop until Ctrl+C:

```python
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pass

server.stop()
```

This is a complete server listening at `opc.tcp://localhost:4840`, with an empty address space.

#### Putting it all together

```python
import time
from o6 import Server

server = Server(port=4840)
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

---

## Letting the server manage its own shutdown

A manual `stop()` is easy to miss on an exception or an early `return`. `Server` is a context manager: `with` calls `start()` on entry and `stop()` on exit, even if the body raises:

```python
from o6 import Server

with Server(port=4840) as server:
    print(server.running)        # True
    print(server.endpointUrl)    # opc.tcp://localhost:4840

# stopped automatically here, even if the body raised
```

Both forms do the same thing, and later pages use whichever fits. [Running on asyncio](140_async-server.md) covers the asynchronous form, `async with`, for a server that runs on an asyncio event loop instead of a background thread.

!!! info
    Without `stop()`, the socket and session state are released when the
    server is garbage-collected, but don't rely on it. An explicit `stop()`
    (or a `with` block) drains the listener and tears down the worker thread
    in a predictable order. Garbage collection guarantees neither.

---

## Checking whether it's listening

`server.running` is `True` after `start()` and `False` after `stop()`. It reads the listening socket's state directly, so it cannot disagree with it. Check it first when something doesn't work.

```python
with Server(port=4840) as server:
    assert server.running
    # ... build the address space, do work ...
```

---

## Three addresses worth knowing before we build anything

Three standard nodes already exist. The properties return `o6.NodeId` values (addresses into the tree, not the data itself). Everything you build hangs off one of them:

```python
server.objectsNode    # i=85, the Objects folder — where our nodes go
server.typesNode      # i=86, the Types folder — for declared types, much later
server.serverNode     # i=2253, the Server object itself
```

`server.objectsNode` is the standard `Objects` folder every OPC UA server publishes. Every node you add in the Foundation band sits under it, directly or through nested folders. `typesNode` is used once you [declare your own types](200_declare-object-type.md).

---

## Next steps

The server has nothing under `Objects/` yet. The next page adds a folder skeleton for the distillery.

| Topic | What it covers |
|---|---|
| [Add a hierarchy](105_add-hierarchy.md) | Group nodes into a small `DistillingSystem` folder with sub-objects. |
| [Server manual](../../manual/server/lifecycle.md) | Lifecycle and configuration in full. |
