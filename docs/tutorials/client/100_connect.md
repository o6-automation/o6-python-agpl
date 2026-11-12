# Connect / disconnect

A client session starts with a [`Client`](../../api_reference/client.md) and ends with a disconnect. This page shows how to connect and disconnect, use the context manager, and set client options.

Start the [example server](../setup.md) in the background before you run the snippets.

---

## Create a client — basic connect / disconnect

Pass the server's endpoint URL to `Client`.

```python
from o6 import Client

client = Client("opc.tcp://localhost:4840")
```

Connect to the endpoint.

```python
client.connect()
print(client.connected)   # True
```

Disconnect when you are done.

```python
client.disconnect()
print(client.connected)   # False
```

!!! info
    Without `disconnect()`, the socket and session are cleaned up when the client is garbage-collected. Call `disconnect()` explicitly: it stops the worker loop, deletes subscriptions and lets the server release its session state promptly.

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

`Client` is a sync and async context manager.
The `with` / `async with` block calls `connect()` on entry and `disconnect()` on exit, including on exceptions.
Use the `with` form for short scripts.

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

`Client.__init__` takes the endpoint URL, an optional loop and keyword-only options for authentication, encryption and bookkeeping.
All options have defaults.

**`name="..."`** — A label that identifies the client.
Give each client in a process a distinct `name`. Without one, `o6` assigns `client1`, `client2`, ….
Must be a valid Python identifier, must not match `server\d+`, and must not be `::global` / `global`.

```python
from o6 import Client
line_a = Client("opc.tcp://line-a:4840", name="simple_client")
```

**`logger=...`** — A `logging.Logger` for the client to log to.
Defaults to a logger named after the module.

```python
import logging
from o6 import Client

log = logging.getLogger("my_app.opc")
client = Client("opc.tcp://localhost:4840", logger=log)
```

**`username=..., password=...`** — Username/password authentication.
The server's `UserTokenPolicy` must allow it; otherwise `activateSession` fails.
Password encryption alone does not authenticate the server or protect the
whole session. Configure certificate trust and channel encryption as shown in
[Security](300_security.md). The
[client manual](../../manual/client/lifecycle.md#secured-connections) explains
the certificate requirements.

Credentials do not enable plaintext password transmission. For a development
endpoint that requires unencrypted password tokens, pass
`allowNonePolicyPassword=True` (default `False`).

```python
from o6 import Client

client = Client("opc.tcp://localhost:4840", username="alice", password="s3cr3t")
```
