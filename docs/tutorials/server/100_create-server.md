# Creating a server

This is the first page of a small project: building an OPC UA server for an automated distillery, one page at a time. By the end of the Foundation band we'll have a server that reports on a still — temperature, batch state, a couple of settings an operator can change — and every later page in these tutorials either extends that same server or applies the same ideas somewhere else. It starts here, with the one thing every server needs before anything else: something listening on the network.

In `o6`, that something is an [`o6.Server`](../../api_reference/server.md). This page covers constructing one, starting it, stopping it, and the couple of properties worth knowing before we start adding anything to it.

---

## What is a server, before it does anything?

A server is a process that listens on a TCP port and speaks the OPC UA protocol once something connects: it answers questions about its *address space* — the tree of nodes it exposes — reads and writes values on request, and runs whatever background work we give it. The address space is what the rest of these tutorials spend most of their time building.

A server that has just been constructed doesn't do any of that yet. It exists, but it isn't listening, and its address space is still just the handful of standard nodes every OPC UA server carries:

```python
from o6 import Server

server = Server(port=4840)
print(server.running)        # False — not yet listening
print(server.endpointUrl)    # opc.tcp://localhost:4840
```

Constructing a `Server` only configures it — `port=4840` says where it will listen once asked to. Nothing is actually happening on the network until `start()` is called.

---

## Start it, and stop it again

`start()` opens the listening socket; `stop()` closes it. Between the two, the server accepts connections at the address `server.endpointUrl` reports:

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

`port` defaults to `4840` — the port these tutorials use throughout, and the one OPC UA reserves for exactly this — so `Server()` alone would bind the same address as `Server(port=4840)`. The rest of a server's configuration — certificates, access control, the application URI — is covered in [later pages](420_security-policies.md), once there's a reason to need it. Nodes can be added to the address space either before or after `start()`, so there's no ordering to worry about yet.

Left as it is, the process would exit the moment `start()` returns. A server is meant to keep running, so the usual next step is a loop that just waits, until something — usually Ctrl+C — tells it to stop:

```python
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pass

server.stop()
```

That's a complete, if empty, server: listening at `opc.tcp://localhost:4840`, ready for a client to connect to, with nothing yet in its address space worth looking at.

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

Calling `stop()` by hand works, but it's easy to forget on an exception, or on an early `return`. `Server` is also a context manager, so `with` takes care of both ends of the lifecycle — `start()` on entry, `stop()` on exit, even if the body raises:

```python
from o6 import Server

with Server(port=4840) as server:
    print(server.running)        # True
    print(server.endpointUrl)    # opc.tcp://localhost:4840

# stopped automatically here, even if the body raised
```

The tutorials from here on use whichever form fits the example better; both end up doing the same thing. [Timers and async loops](350_timers.md) covers the asynchronous form, `async with`, for a server that runs on an asyncio event loop instead of a background thread.

!!! info
    Forgetting `stop()` entirely isn't fatal — the socket and session state are still released when the server is garbage-collected — but it isn't something to rely on. An explicit `stop()` (or a `with` block) drains the listener and tears down the worker thread in a predictable order; garbage collection doesn't promise either.

---

## Checking whether it's listening

`server.running` is the one property to check when something isn't behaving as expected: `True` once `start()` has run, `False` again after `stop()`. It's a direct read of the listening socket's state, not a separate health check that could disagree with reality.

```python
with Server(port=4840) as server:
    assert server.running
    # ... build the address space, do work ...
```

This is the check the rest of these tutorials fall back on after each step: if something isn't working, the first question is whether the server is actually running.

---

## Three addresses worth knowing before we build anything

Before adding a single node of our own, it's worth knowing the three that already exist. They're `o6.NodeId` values — addresses into the tree, not the data itself — and everything we build over the next few pages hangs off one of them:

```python
server.objectsNode    # i=85, the Objects folder — where our nodes go
server.typesNode      # i=86, the Types folder — for declared types, much later
server.serverNode     # i=2253, the Server object itself
```

For the distillery, `server.objectsNode` is the one that matters for now — it's the standard `Objects` folder every OPC UA server publishes, and it's the parent every node we add from here on hangs off, directly or through folders nested underneath it. `typesNode` doesn't come up until [we declare our own types](200_declare-object-type.md), much later in these tutorials.

---

## What's next?

The server is listening, but ask it about its address space and there's nothing under `Objects/` yet — the distillery doesn't exist. The next page starts building it: a folder skeleton with a place for everything the later pages will fill in.

- [Add a hierarchy](105_add-hierarchy.md) — group nodes into a small `DistillingSystem` folder with sub-objects.
- [Server manual](../../manual/server/lifecycle.md) — the full lifecycle and configuration story.
