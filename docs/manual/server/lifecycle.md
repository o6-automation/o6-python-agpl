# Lifecycle & configuration

## Creating and running a server

A server is created, configured, filled with nodes, and started. Nodes may be
added before or after `start()`; only the configuration has an ordering
requirement.

```python
import o6

server = o6.Server(port=4840)
server.start()
# ... serve ...
server.stop()
```

The full constructor signature:

```python
Server(
    port=4840,                      # TCP port to listen on
    logger=None,                    # Python logger for all server output
    loop=None,                      # asyncio event loop to use
    *,
    certificate=None,               # path, Path, or DER/PEM bytes
    privateKey=None,
    trustList=None,                 # trusted client certificates
    issuerList=None,                # intermediate CA certificates
    revocationList=None,            # CRLs
    secureOnly=False,               # offer no unencrypted endpoint
    acceptAllCertificates=False,    # skip client certificate validation
    applicationUri=None,
    accessControl=None,             # o6.AccessControl subclass instance
    allowNonePolicyPassword=False,  # permit passwords on an open channel
    rbacForAnonymous=False,         # enforce role permissions for anonymous sessions
)
```

`server.running` reports whether the networking layer is up, and
`server.endpointUrl` gives the URL clients connect to:

```python
print(server.running)        # False before start()
print(server.endpointUrl)    # opc.tcp://localhost:4840
```

Both `start()` and `stop()` are idempotent — calling `start()` on a running
server or `stop()` on a stopped one does nothing. A stopped server can be
started again.

The context-manager form is the one to prefer, because it stops the server even
when the body raises:

```python
with o6.Server(port=4840) as server:
    temperature = server.addVariable("Temperature", server.objectsNode, 22.5)
    print(temperature())
```

Synchronous `start()` and both context managers wait until the network
listeners are ready and raise bind errors, for example if the port is occupied.
On the server's running asyncio loop, `start()` schedules listener creation;
use `await server.waitReady()` afterwards, or prefer `async with server`.
Cancelling the readiness wait shuts down startup and closes its listeners.

`server.loop` exposes the owning `asyncio.AbstractEventLoop` as a read-only
property, like `client.loop`. It is the loop supplied to the constructor, the
running loop detected there, or a newly created loop when neither is available.
Supplied and detected loops remain caller-owned; a loop created by the server
is managed by the server and must not be closed directly by application code.
Stopping the server does not replace the loop.

```python
import asyncio

async def serve():
    server = o6.Server(port=4840)
    assert server.loop is asyncio.get_running_loop()
    server.start()
    try:
        await server.waitReady()  # must run on server.loop
        await asyncio.Event().wait()
    finally:
        server.stop()
```

`stop()` normally completes synchronously. A callback running on a background
server's own worker loop starts shutdown without blocking and receives a Task;
an async callback can use `await server.stop()` to wait for cleanup. The worker
exits after that task completes. Restart from outside the worker after shutdown.

If a server is garbage-collected while still running, `__del__` stops it and
releases the native resources. That is a safety net, not a plan: hold the server
in a variable for as long as it should serve, and stop it explicitly.

### Well-known entry points

Three properties return the NodeIds every address space starts from:

```python
server.objectsNode    # i=85, the Objects folder — the usual parent
server.typesNode      # i=86, the Types folder
server.serverNode     # i=2253, the Server object — the default event source
```

They are `o6.NodeId` values, not node handles. That distinction matters exactly
once, in [Declared type instance ownership](declared-types.md#declared-type-instance-ownership).

## Configuration

`server.config` is the live configuration object. Most of it must be set before
`start()`; the security-related setters and the history database explicitly
raise `RuntimeError` if the server is already running.

The application identity is what a client sees in `GetEndpoints` and
`FindServers`:

```python
server.config.applicationUri = "urn:example:plant-server"

description = server.config.applicationDescription
description.applicationName = o6.LocalizedText("en-US", "Plant Server")
server.config.applicationDescription = description
```

`applicationDescription` returns a copy, so the read–modify–write above is the
correct shape; mutating the returned object alone changes nothing.

`server.config.logger` is write-only and redirects all server log output to a
Python logger. The same logger can be passed as `Server(logger=...)`.

### Security

Certificates are passed to the constructor as file paths, `Path` objects, or raw
DER/PEM bytes. Supplying both a certificate and a private key enables the
encrypting security policies; the trust list decides which client certificates
are accepted.

The certificate and private key must be supplied together and must not be empty.
`secureOnly=True` requires both; invalid combinations raise `ValueError` during
construction. The explicit `applicationUri` is preserved when encryption is
configured and should match the URI in the server certificate.

```python
from o6.util import createSelfSignedCertificate

key, cert = createSelfSignedCertificate(
    appUri="urn:example:plant-server",
    commonName="PlantServer@localhost",
)

server = o6.Server(
    port=4840,
    certificate=cert,
    privateKey=key,
    trustList=[client_cert],
    applicationUri="urn:example:plant-server",
)
```

With that configuration the server advertises a `None` endpoint plus `Sign` and
`SignAndEncrypt` endpoints for every policy its build supports — typically
`Basic256Sha256`, `Aes128_Sha256_RsaOaep`, and `Aes256_Sha256_RsaPss`. A client
that presents a trusted certificate can then pick any of them:

```python
client = o6.Client(
    "opc.tcp://localhost:4840",
    certificate=client_cert,
    privateKey=client_key,
    trustList=[cert],
    securityMode=o6.SecurityMode.SIGN_AND_ENCRYPT,
    securityPolicy=o6.SecurityPolicy.BASIC256SHA256,
    applicationUri="urn:example:secure-client",
)
```

Log lines such as `Could not add SecurityPolicy#EccNistP256_AesGcm with error
code BadCertificateInvalid` on startup are expected with an RSA certificate:
the elliptic-curve policies need an EC key and are skipped.

`acceptAllCertificates=True` accepts every client certificate without
validation. It exists for development and interop testing, and it defeats the
purpose of the trust list — do not ship it.

!!! warning
    `secureOnly=True` removes the `None` endpoint entirely. In the current
    build no client can then connect — including a correctly configured secure
    `o6.Client` — because endpoint discovery is performed over the `None`
    endpoint before the secure channel is opened; every attempt fails with
    `BadSecurityPolicyRejected`. Leave `secureOnly` at its default and restrict
    access through [access control](security.md#access-control-and-authentication) instead
    until this is resolved.

`allowNonePolicyPassword=True` permits `UserNameIdentityToken` authentication on
an unencrypted endpoint. It is deliberately separate from access control,
because it is a transport decision: without it the stack strips the
username/password `UserTokenPolicy` from an insecure endpoint and logs a warning
that the password would travel in the clear. Enable it for local testing only.

Neither access control nor these transport settings can be replaced after the
server starts.

## Lifecycle notes

A few practical details for long-running processes.

Configuration is not hot-swappable. Security settings, access control, and the
history database all raise `RuntimeError` once the server is running. Address
space changes, by contrast, are fine at any time — adding and deleting nodes
while clients are connected is normal operation.

Node handles keep their Python object alive through the server's nodestore
reference for as long as the OPC UA node exists. After a node is deleted,
remaining Python references may delay `__del__`, so use `__del__` for
Python-owned resources rather than protocol actions that must happen at the
instant of deletion.

Server names are assigned internally as `server0`, `server1`, … and are
reserved: a `Client(name="server1")` is rejected. The live-server registry that
declarative construction consults holds weak references, so a server becomes
invisible to inference as soon as your last reference goes away — which is
another reason to keep it in a variable.

Stopping a server keeps its event loop alive so that later synchronous
configuration calls still work; the loop is closed when the object is
finalized. A stopped server can be restarted with `start()`.

To observe `start()` and `stop()` from inside Python rather than waiting
for the next call site to check `server.running`, register a handler on
`server.onLifecycleNotification` — see [Notification handler](notification-handler.md)
for the worked example. Handlers can also be added and removed while the
server is running.
