# Connect / disconnect

Every client session in `o6` starts with constructing a [`Client`](../../api_reference/client.md) and ends with a clean shutdown. This page walks through the four common shapes that construction and connection can take.

This tutorial expects the [example server running](../setup.md) in the background.

---

## Create a client — basic connect / disconnect

A client is constructed with the endpoint URL of the server you want to talk to.
When you are done, call `disconnect()`.

```python
from o6 import Client

client = Client("opc.tcp://localhost:4840")
```

After creation we can connect the client object to the server at the selected endpoint.

```python
client.connect()
print(client.connected)   # True
```

When we are done with the client we disconnect.

```python
client.disconnect()
print(client.connected)   # False
```

!!! info
    If you forget `disconnect()` the underlying socket and session are still cleaned up when the client is garbage-collected, but explicit shutdown is the reliable path — it stops the worker loop, deletes subscriptions, and lets the server release its session state promptly.

#### Putting it all together

```python
from o6 import Client

client = Client("opc.tcp://localhost:4840")
client.connect()
print(client.connected)   # True

# ... do some work

client.disconnect()
print(client.connected)   # False
```

---

## Connect with context manager

`Client` is a context manager, both synchronously and asynchronously.
The `with` / `async with` block calls `connect()` on entry and `disconnect()` on exit, including on exceptions.
The `with` form is the recommended shape for short scripts and one-off scripts.

```python
from o6 import Client

with Client("opc.tcp://localhost:4840") as client:
    print(client.connected)   # True — connected on entry
    # ... do work ...

# disconnected automatically here, even if the body raised
```

> **Async:** the `async with` form is covered in [Async client](510_async-client.md).

---

## Create-client options

`Client.__init__` takes the endpoint URL and an optional loop, plus a number of keyword-only options for authentication, encryption, and bookkeeping.
They declare sensible defaults and only need to be set when needed.

**`name="..."`** — A label used to identify the client.
If you create more than one client in the same process, give each one a distinct `name`; otherwise `o6` assigns one automatically (`client1`, `client2`, …).
Must be a valid Python identifier, must not match `server\d+`, and must not be `::global` / `global`.

```python
from o6 import Client
line_a = Client("opc.tcp://line-a:4840", name="simple_client")
```

**`logger=...`** — A `logging.Logger` for the client to log to.
Defaults to a logger named after the module if not set.

```python
import logging
from o6 import Client

log = logging.getLogger("my_app.opc")
client = Client("opc.tcp://localhost:4840", logger=log)
```

**`username=..., password=...`** — Username/password authentication.
The server's `UserTokenPolicy` must allow this; otherwise the `activateSession` step will fail.

```python
from o6 import Client

client = Client("opc.tcp://localhost:4840", username="alice", password="s3cr3t")
```

