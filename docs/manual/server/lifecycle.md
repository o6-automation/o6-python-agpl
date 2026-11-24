# Lifecycle & Configuration

For a long-running application, check the
[commercial build's Script Mode limit](../../home/commercial-build.md): without
a valid Credential, the process exits ten minutes after importing `o6`.
The AGPL build has no Script Mode timer.

## Creating and running a server

You create a server, configure it, add nodes and start it. You can add nodes
before or after `start()`. Only the configuration must be set before start.

```python
import o6

server = o6.Server(port=4840)
server.start()
input("Server is running. Press Enter to stop.\n")
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
    securityPolicies=None,          # names of the SecurityPolicies to offer
    acceptAllCertificates=False,    # skip client certificate validation
    applicationUri=None,
    applicationName=None,           # default "o6-python Server"
    productUri=None,                # default "https://o6-automation.com/o6-python"
    accessControl=None,             # o6.AccessControl subclass instance
    allowNonePolicyPassword=False,  # permit passwords on an open channel
    rbacForAnonymous=False,         # stricter fallback permissions; see Access Control & Roles
)
```

`server.running` reports whether the networking layer is up.
`server.endpointUrl` is a localhost convenience URL built from the constructor's
port. When using custom `server.config.serverUrls`, choose the client URL
explicitly; `endpointUrl` does not track listener changes:

```python
print(server.running)        # False before start()
print(server.endpointUrl)    # opc.tcp://localhost:4840
```

`start()` and `stop()` are idempotent: `start()` on a running server and
`stop()` on a stopped one do nothing. You can start a stopped server again.

Prefer the context manager. It stops the server even when the body raises
or Ctrl+C interrupts the wait:

```python
with o6.Server(port=4840) as server:
    temperature = server.addVariable("Temperature", server.objectsNode, 22.5)
    print(temperature())
    input("Server is running. Press Enter to stop.\n")
```

The server's worker handles requests while the main thread waits. For an
async serving lifetime, use `await asyncio.Event().wait()` inside
`async with server`, as shown in the [Server overview](index.md#one-api-synchronous-or-asynchronous).

Synchronous `start()` and both context managers wait until the network
listeners are ready. They raise bind errors, for example when the port is in
use. On the server's running asyncio loop, `start()` only schedules listener
creation. Call `await server.waitReady()` afterwards, or use
`async with server`. Cancelling the readiness wait shuts down startup and
closes its listeners.

If a running server is garbage-collected, `__del__` emits a `ResourceWarning`
and schedules the shutdown on the server's event loop. The shutdown serves
`config.shutdownDelay`, then releases the native resources. The collecting
thread does not wait for it. Don't rely on this: keep the server in a variable
for as long as it serves, and stop it explicitly.

### Well-known entry points

Three properties return the NodeIds every address space starts from:

```python
server.objectsNode    # i=85, the Objects folder — the usual parent
server.typesNode      # i=86, the Types folder
server.serverNode     # i=2253, the Server object — the default event source
```

They are `o6.NodeId` values, not node handles. See
[Declared type instance ownership](../information-model-authoring/publishing.md#declared-type-instance-ownership)
for where this matters.

## Configuration

`server.config` is the live configuration object. Set most of it before
`start()`. The security-related setters and the history database raise
`RuntimeError` when the server is running.

Clients see the application identity in `GetEndpoints` and `FindServers`.
Set it in the constructor, which applies it after the encryption setup:

```python
server = o6.Server(
    port=4840,
    applicationUri="urn:example:plant-server",
    applicationName="Plant Server",
    productUri="urn:example:plant",
)
```

Without these arguments, a server announces the ApplicationUri
`urn:o6-Python.unconfigured.application`, the ApplicationName
`o6-python Server` and the ProductUri `https://o6-automation.com/o6-python`.
Set `applicationUri` for every deployed server: it is also the URI of
namespace 1.
`server.config.applicationDescription` gives full control:

```python
description = server.config.applicationDescription
description.applicationName = o6.LocalizedText("Plant Server", "en-US")
server.config.applicationDescription = description
```

`applicationDescription` returns a copy. Mutating the returned object alone
changes nothing; assign it back as shown.

`server.config.buildInfo` is the `BuildInfo` that clients read from
`Server/ServerStatus/BuildInfo` (`i=2260`). It names o6-python by default:
ProductName `o6-python`, ManufacturerName `o6 Automation GmbH`, the o6 version
as SoftwareVersion, and the same ProductUri as the ApplicationDescription.
`productUri=` sets both. The property also returns a copy and can be assigned
only while the server is fully stopped:

```python
build_info = server.config.buildInfo
build_info.productName = "Plant Server"
build_info.softwareVersion = "1.4.2"
server.config.buildInfo = build_info
```

`config.setEncryption()` restores the o6 identity in both, so set it after the
encryption.

`server.config.logger` is write-only and redirects all server log output to a
Python logger. Like the other settings, it can be assigned only while the server
is fully stopped. You can also pass the logger as `Server(logger=...)`.

### Quotas, intervals, and listening addresses

The following properties expose the native open62541 configuration. Getters are
synchronous, including while running and inside server callbacks, and return
detached values read from native configuration. Changing a returned list does not
change the server. These properties can be assigned before startup or after
shutdown completes. Assignments during startup, operation, or shutdown raise
`RuntimeError`, including assignments to `maxSubscriptions` and
`maxSubscriptionsPerSession`. If `stop()` returns a Task, wait for shutdown and
worker retirement before configuring the next run.

| Property | Type / units | Native default |
| --- | --- | --- |
| `maxSessions` | UInt16 count; 0 = unlimited | 100 |
| `maxSessionTimeout` | Duration in ms | 3,600,000 |
| `shutdownDelay` | Duration in ms; 0 = stop at once | 0 |
| `maxSubscriptions` | UInt32 count; 0 = unlimited | 1,024 |
| `maxSubscriptionsPerSession` | UInt32 count; 0 = unlimited | 64 |
| `maxMonitoredItems` | UInt32 count; 0 = unlimited | 32,768 |
| `maxMonitoredItemsPerSubscription` | UInt32 count; 0 = unlimited | 32,768 |
| `maxMonitoredItemsPerCall` | UInt32 count; 0 = unlimited | 0 |
| `maxNodesPerRead` | UInt32 count per Read call; 0 = unlimited | 0 |
| `maxNodesPerWrite` | UInt32 count per Write call; 0 = unlimited | 0 |
| `maxNodesPerMethodCall` | UInt32 count per Call call; 0 = unlimited | 0 |
| `maxNodesPerBrowse` | UInt32 count per Browse call; 0 = unlimited | 0 |
| `maxNodesPerRegisterNodes` | UInt32 count per RegisterNodes and UnregisterNodes call; 0 = unlimited | 0 |
| `maxNodesPerTranslateBrowsePathsToNodeIds` | UInt32 count per TranslateBrowsePathsToNodeIds call; 0 = unlimited | 0 |
| `maxNodesPerNodeManagement` | UInt32 count per AddNodes, AddReferences, DeleteNodes and DeleteReferences call; 0 = unlimited | 0 |
| `samplingIntervalLimits` | `(min, max)` durations in ms | `(50.0, 86400000.0)` |
| `publishingIntervalLimits` | `(min, max)` durations in ms | `(100.0, 3600000.0)` |
| `queueSizeLimits` | `(min, max)` UInt32 queue sizes | `(1, 100)` |
| `lifeTimeCountLimits` | `(min, max)` UInt32 publishing cycles | `(3, 15000)` |
| `keepAliveCountLimits` | `(min, max)` UInt32 publishing cycles | `(1, 100)` |
| `maxPublishReqPerSession` | UInt32 queued requests; 0 = unlimited | 512 |
| `maxNotificationsPerPublish` | UInt32 notification count | 1,000 |
| `enableRetransmissionQueue` | `bool` | `True` |
| `serverUrls` | List of strings | `["opc.tcp://:PORT"]`, from the constructor |

With `shutdownDelay` above 0, `stop()` first keeps serving for that long. In
that time `Server/ServerStatus/State` reads `Shutdown` and `SecondsTillShutdown`
counts down, so connected clients can notice, and the `shutdown` lifecycle
notification fires. Only then does the shutdown begin. The delay applies to a
background server, the usual case; a `stop()` on a loop the server does not
drive stops at once.

A service call that carries more operations than its limit fails with
`BadTooManyOperations`. The `maxNodesPer…` limits and `maxMonitoredItemsPerCall`
are also the values clients read from `Server/ServerCapabilities/OperationLimits`.

Defaults are supplied by the bundled native SDK. Subscription-specific
properties are absent when compiled without subscription support;
`maxMonitoredItemsPerCall` and the `maxNodesPer…` operation limits remain available as native fields.

Integer setters accept Python integers.
UInt16 values must fit `0..65535`; UInt32 values must fit `0..4294967295`.
Negative integers or overflow raise `OverflowError`. Durations accept numeric
values convertible to `float`, must be finite and non-negative, and are measured
in milliseconds. Invalid durations raise `ValueError`. Boolean assignment
requires `True` or `False`.

Range setters accept a two-element tuple or list with `min <= max`. Getters
return tuples. Malformed or reversed ranges raise `ValueError`; wrong input
types raise `TypeError`. Validation and conversion finish before assignment,
so rejected values leave the previous configuration intact. Properties cannot
be deleted. Values are never silently clamped or wrapped.

Zero retains its field-specific native meaning. In particular,
`maxSessionTimeout=0` is a zero timeout, and `maxNotificationsPerPublish=0`
does not mean unlimited notifications. Zero range endpoints are stored
unchanged; whether a particular request works with them depends on native
negotiation and timer requirements.

Native request negotiation still applies. A node's minimum sampling interval
can raise the negotiated interval. Data-change queue requests of 0 or 1 use
size 1, even when a configured queue minimum is larger. Subscription lifetime
is at least three times the negotiated keepalive count. Read negotiated values
from the subscription or monitored item; configuration readback reports the
limits, not those negotiated results.

Sub-5 ms interval limits can be configured; the binding does not enforce the
5 ms header comment as a floor. Successful negotiation and sampling at a
requested interval do not guarantee timing accuracy or a specific throughput.

`serverUrls` accepts a tuple or list of strings and owns copies of them. Native
URL parsing and listener setup occur at startup. An empty list uses the native
TCP fallback: all interfaces at port 4840, regardless of the constructor's port.
An empty hostname, such as `opc.tcp://:4858`, listens on all IPv4 and IPv6
interfaces at that port.

A port of `0` selects one free port for all addresses of that listener,
including both IPv4 and IPv6. After startup, read the selected port from
`config.applicationDescription.discoveryUrls`.

After `start()`, every listener is announced in
`config.applicationDescription.discoveryUrls`, which GetEndpoints, FindServers,
`registerDiscovery()` and ReverseHello use. A listener on all interfaces is
announced with the local host name, such as `opc.tcp://myhost:4858`. A listener
with an explicit host is announced with that host. To listen only on IPv4
loopback:

```python
import o6

server = o6.Server(port=4858)
# Configure encryption here, before custom limits and URLs.
config = server.config
config.maxSessions = 1
config.maxSubscriptions = 1
config.maxSubscriptionsPerSession = 1
config.maxMonitoredItems = 100
config.maxMonitoredItemsPerSubscription = 100
config.maxMonitoredItemsPerCall = 100
config.samplingIntervalLimits = (0.1, 3_600_000.0)
config.queueSizeLimits = (1, 1)
config.enableRetransmissionQueue = False
config.serverUrls = ["opc.tcp://127.0.0.1:4858"]
client_url = config.serverUrls[0]
server.start()
try:
    with o6.Client(client_url) as client:
        pass  # Use the configured listener explicitly.
finally:
    server.stop()
```

The URL getter preserves the configured list, including `[]`; it does not
synthesize fallback URLs, resolve wildcard addresses, or discover dynamic ports.

### Security

Configure encryption before custom quotas, ranges, and listener URLs.
`config.setEncryption()` invokes native default-configuration helpers which
can overwrite custom settings, including replacing `serverUrls` with the helper's port.
Overrides are not automatically restored. Calling it again requires reapplying
custom settings afterward. Getters show the resulting native values.
Pass certificates to the constructor as file paths, `Path` objects or raw
DER/PEM bytes. A certificate plus a private key enables the encrypting security
policies. The trust list decides which client certificates are accepted:
list the client certificates, or the CA certificates that issued them. The
`issuerList` supplies certificate authority (CA) certificates needed to
complete trusted certificate chains; it does not establish trust on its own.
`revocationList` supplies those CAs' certificate revocation lists (CRLs). Without a trust list the server
rejects every client certificate. The same list also checks X.509 user tokens.
This identifies the client application on a secured channel. User login and
node permissions are separate; the
[secured client/server example](security.md#a-secured-clientserver-pair)
shows how to configure all three together.

Supply the certificate and private key together; neither may be empty.
`secureOnly=True` requires both. Invalid combinations raise `ValueError` during
construction. An explicit `applicationUri` is kept when encryption is
configured, and it should match the URI in the server certificate.

This configuration fragment assumes `client_cert` and `client_key` are the
certificate and private key for `urn:example:secure-client`. The client keeps
its private key; only its public certificate goes into the server's trust list.

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

The server then advertises a `None` endpoint plus `Sign` and `SignAndEncrypt`
endpoints for `Basic256Sha256`, `Aes128_Sha256_RsaOaep` and
`Aes256_Sha256_RsaPss`. A client with a trusted certificate can pick any of
them:

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

These three policies use RSA certificates. Elliptic-curve policies require an
EC certificate. The bundled SDK enables `ECC_nistP256_AesGcm` and
`ECC_nistP256_ChaChaPoly` by default for a compatible EC certificate; deprecated
ECC policies, including `ECC_curve25519` and `ECC_curve448`, are excluded.
The deprecated `Basic128Rsa15` and `Basic256` policies are
offered only when you select them, as described next. Each endpoint advertises
each user token policy once.

`securityPolicies` chooses the policies instead. Pass any of `"None"`,
`"Basic128Rsa15"`, `"Basic256"`, `"Basic256Sha256"`,
`"Aes128_Sha256_RsaOaep"` and `"Aes256_Sha256_RsaPss"`, or their full
`http://opcfoundation.org/UA/SecurityPolicy#…` URIs. The server offers exactly
the policies you list, with a `Sign` and a `SignAndEncrypt` endpoint for each
one except `"None"`. A policy you leave out cannot open a channel either.

```python
server = o6.Server(
    port=4840,
    certificate=cert,
    privateKey=key,
    trustList=[client_cert],
    # No unencrypted endpoint, and no Basic256Sha256
    securityPolicies=["Aes128_Sha256_RsaOaep", "Aes256_Sha256_RsaPss"],
)
```

`securityPolicies` requires a certificate and private key, and excludes
`secureOnly`: leave `"None"` out of the list instead. The deprecated policies
get a low but non-zero `SecurityLevel`, below every other policy, so clients
that pick the best endpoint still prefer the SHA-256 policies. open62541
assigns level 0 to them, which clients and the OPC Foundation CTT treat as
unusable. A policy that cannot be set up with the certificate fails the
constructor.

The same selection works for `server.config.setDefaultWithFilestore()` through
its `securityPolicies` argument. Without it, that call keeps everything
open62541 sets up for the certificate, including `"None"` and the deprecated
RSA policies.

Requests normally carry a RequestHeader timestamp. By default the server
answers a request with a timestamp of 0 with `BadInvalidTimestamp`. To log a
warning and continue instead, set `server.config.verifyRequestTimestamp = False`
while the server is stopped. Create the server, or call
`setDefaultWithFilestore()`, before you set it.

`acceptAllCertificates=True` accepts every client certificate without
validation. It bypasses the trust list. Use it only for development and interop
testing, never in production.

`secureOnly=True` removes the `None` endpoint. In the bundled client/server
configuration, an `o6.Client` using ordinary endpoint discovery first opens a
`None` channel; that discovery attempt fails with `BadSecurityPolicyRejected`.
Setting the client's requested policy and mode alone does not skip discovery.
A client with a matching, preconfigured `EndpointDescription` assigned to
`client.config.endpoint` can connect directly to a secured endpoint. That
description must include the server certificate and matching user-token
policies; obtain it from trusted configuration. This limitation concerns the
discovery path, not all clients or all secured connections.

For clients that need ordinary discovery, keep `secureOnly=False` and require
`SIGN_AND_ENCRYPT` in `AccessControl.activateSession`, as in the
[complete example](security.md#a-secured-clientserver-pair). This leaves
discovery available over `None` while rejecting application Sessions on
unencrypted or sign-only channels. Checking a username or assigning roles
alone does not enforce encryption.

`allowNonePolicyPassword=True` permits `UserNameIdentityToken` authentication on
an unencrypted endpoint. It is a transport setting, separate from access
control. Without it, the stack removes the username/password `UserTokenPolicy`
from an insecure endpoint and logs a warning that the password would travel in
the clear. Enable it for local testing only.

### Rejected certificates

A client whose certificate is not trusted fails to connect, typically with
`BadSecurityChecksFailed`. The server logs the subject, ApplicationUri and
thumbprint of every certificate it rejects, both application certificates and
X.509 user-token certificates:

```text
Rejected the application certificate /C=DE/O=o6/CN=Client (ApplicationUri urn:example:client, thumbprint 7C70D396...) with StatusCode BadCertificateUntrusted
```

[`server.rejectedCertificates`](../../api_reference/server.md#o6.server.Server.rejectedCertificates)
returns rejected application certificates as DER bytes, oldest first, without
duplicates. It holds at most 100 certificates; the next distinct rejection
clears the list and starts a new one. The list is in memory and is cleared by
`config.setEncryption()` or constructing a new server.

To handle application and X.509 user-token rejections, register
[`server.onCertificateRejected`](../../api_reference/server.md#o6.server.Server.onCertificateRejected).
The following fragment assumes an existing `server`. File writes run in a
worker thread so they do not block the server's event loop:

```python
import asyncio
import hashlib
from pathlib import Path


def store_rejected(certificate: bytes) -> None:
    folder = Path("pki/rejected")
    folder.mkdir(parents=True, exist_ok=True)
    thumbprint = hashlib.sha1(certificate).hexdigest().upper()
    (folder / f"{thumbprint}.der").write_bytes(certificate)


@server.onCertificateRejected
async def certificate_rejected(certificate: bytes, statusCode: o6.StatusCode) -> None:
    await asyncio.to_thread(store_rejected, certificate)
```

Each registration replaces the previous callback; pass `None` to remove it.
Callback exceptions are logged. Verify a rejected certificate's identity before
adding it to `trustList`, then recreate the server with that trust configuration.

### JSON5 configuration files

A server can also be configured from a JSON5 file in the format of open62541's
`UA_Server_newFromFile`. open62541 parses the file itself, so the same files
work in C and in o6, and the available keys are those of the bundled
open62541 version. The open62541 repository has a commented example of every
key in `examples/json_config/server_json_config.json5`.

```json5
// server.json5
{
  serverUrls: ["opc.tcp://localhost:4841"],
  buildInfo: { productName: "Plant Server", softwareVersion: "1.4.2" },
  maxSessions: 50,
  subscriptions: { maxSubscriptions: 100 },
}
```

```python
server = o6.Server.newFromFile("server.json5")
with server:
    ...
```

`server.config.loadFromFile(path)` applies a file to an existing, fully stopped
server.

- Every setting in the file is used. Everything the file leaves out gets the
  o6 default, also inside nested objects: the file above keeps the o6
  ManufacturerName and ProductUri in `buildInfo`.
- The `port`, `applicationUri`, `applicationName` and `productUri` arguments of
  `newFromFile` count as o6 defaults, so the file overrides them.
- Settings that the format has no keys for are reset to their defaults, for
  example `allowNonePolicyPassword` and `auditingEnabled`. Load the file first
  and use the other config setters afterwards.
- The security configuration comes from the file. `securityPolicies` adds
  policies with their certificate and private key files, and `pkiFolder` stores
  the trust lists in a directory. Without them the server is unencrypted, even
  if `setEncryption()` ran before. With `securityPolicies`, the server offers
  an endpoint for every policy and security mode, as `setEncryption()` does,
  and user tokens use the most secure policy. A certificate file that cannot
  be read is loaded as empty. Relative file paths are resolved against the
  working directory.
- Callbacks, the access control installed with `accessControl`, the address
  space and the logger are kept.
- `pubsubEnabled` only takes effect when the active credential includes PubSub.
- Load the file before enabling history or PushManagement; afterwards
  `loadFromFile` raises `RuntimeError`.

An invalid value raises `StatusCodeError` with a note that names the setting,
for example `Invalid setting 'maxSessions'`. While open62541 parses the file,
it writes its warnings, such as an unknown key, to stdout and not to the
server's logger.

## Lifecycle notes

Configuration is not hot-swappable. Security settings, access control and the
history database raise `RuntimeError` once the server is running. You can
change the address space at any time: adding and deleting nodes while clients
are connected is normal operation.

The server's nodestore keeps a node handle's Python object alive for as long as
the OPC UA node exists. After a node is deleted, remaining Python references can
delay `__del__`. Use `__del__` for Python-owned resources, not for protocol
actions that must happen at the moment of deletion.

Servers are named internally `server0`, `server1`, and so on. These names are
reserved: `Client(name="server1")` is rejected. Declarative construction infers
the server from a live-server registry that holds weak references. A server
disappears from inference as soon as your last reference to it goes away, so
keep it in a variable.

Stopping a server keeps its event loop alive, so later synchronous
configuration calls still work. The loop is closed when the object is
finalized.

`stop()` ends network service; it does not delete the address space. Restarting
the same Server object keeps its nodes and their values. A new Server object
needs its models and nodes set up again. Clients still need to handle channel
loss and possible Session or subscription expiry during downtime.

Application threads, device connections and tasks have their own lifetime.
Stop scheduling application work and finish or cancel it before disposing of
the resources it uses. Stopping the server does not join your threads. See
[Slow device reads](timers.md#slow-device-reads) for a bounded polling example
and its shutdown behavior.

To observe `start()` and `stop()` from Python, register a handler on
`server.onLifecycleNotification`. See [Notification handler](notification-handler.md)
for an example. You can add and remove handlers while the server is running.

## Event loops and integration

The ordinary scripts in the [Server overview](index.md#one-api-synchronous-or-asynchronous)
need no `loop=` argument. `server.loop` is fixed at construction: an explicit
`loop=` takes priority, otherwise the server uses the running loop or creates
one if no loop is running.

Inside `asyncio.run(main())`, the application drives the loop. `async with server`
starts the listeners and waits for readiness without starting a worker
thread. In a synchronous script, `start()` starts a worker when the selected
loop is idle. This also applies to an explicitly supplied, idle loop.

The application owns passed-in and automatically detected loops. The server
owns a loop it creates; do not close that loop yourself. Stopping the server
does not replace the selected loop or close an application-owned loop.

Async tasks await node operations whether they run on the server's loop or
another loop, including before startup. Keep the server's loop running while
it serves network traffic and pending callbacks. A synchronous caller on
another thread can wait for a result; a callback on the owning loop cannot
block that loop to wait for itself. See
[Calling the API from callbacks](callbacks.md#calling-the-api-from-callbacks).

!!! warning "Do not block the loop thread on a thread that calls the server"
    A server call from a different thread runs on the loop thread. Do not let
    the loop thread wait for a thread that calls the server, for example with
    `Thread.join()`, a lock or `Future.result()`. If it does, the two threads
    wait for each other forever. Keep the loop thread free, or wait with
    `await`, for example `await asyncio.to_thread(worker.join)` or
    `await loop.run_in_executor(...)`. See
    [GIL and event-loop bridging](../implementation-details/gil-and-event-loop.md#python-marshalling).

### Manual startup and shutdown

For an application that manages startup explicitly, `start()` on the running
server loop schedules listener creation. Await readiness before using the
endpoint. This is a complete alternative to `async with`:

```python
import asyncio
import o6

async def main():
    server = o6.Server(port=4840)
    server.start()
    try:
        await server.waitReady()
        await asyncio.Event().wait()
    finally:
        server.stop()

try:
    asyncio.run(main())
except KeyboardInterrupt:
    pass
```

`stop()` normally completes synchronously. Called on a background server's
own worker loop, it starts shutdown without blocking and returns a Task.
An async callback in that context can `await server.stop()` to wait for
cleanup. The worker exits after that task completes. Restart the server from
outside the worker.

In notebooks, await the application's async entry point directly instead of
nesting `asyncio.run()` in the kernel's running loop.
