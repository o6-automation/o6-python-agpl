# Lifecycle & Configuration

Configure a client, connect it, and release its session and network resources when finished.
Configuration snippets below are alternatives: apply the chosen settings before
connecting. They use the `Client` import shown first. For a complete minimal
program, see the [Client overview](index.md#one-api-synchronous-or-asynchronous).

For a long-running application, check the
[commercial build's Script Mode limit](../../home/commercial-build.md): without
a valid Credential, the process exits ten minutes after importing `o6`.
The AGPL build has no Script Mode timer.

## Creating a client

Constructing a client does not connect it. The constructor takes the common
settings as keyword arguments. Set everything else after construction on `client.config`.

```python
from o6 import Client

client = Client("opc.tcp://localhost:4840")
```

Constructor signature:

```python
Client(
    endpointUrl="",          # server to connect to
    loop=None,               # asyncio event loop to use
    *,
    logger=None,             # Python logger for all client output
    certificate=None,        # path, Path, or DER/PEM bytes
    privateKey=None,         # path, Path, or DER/PEM bytes
    trustList=None,          # list of trusted server certificates
    revocationList=None,     # list of CRLs
    acceptAllCertificates=False,  # development only: trust every server certificate
    loadUnknownDataTypes=True,    # load unknown structure DataTypes on demand
    securityMode=None,       # o6.SecurityMode
    securityPolicy=None,     # o6.SecurityPolicy or short name
    applicationUri=None,     # URI sent in the ApplicationDescription
    username=None,           # UserNameIdentityToken
    password=None,
    allowNonePolicyPassword=False,  # explicit opt-in for plaintext password tokens
    name="",                 # process-unique client name
)
```

!!! info
    All arguments are optional. `Client()` with no arguments is valid; set the
    endpoint URL later through `client.config.endpointUrl`. `connect()` fails
    when no valid endpoint URL is configured.

### The client name

Every client has a `name`. Without one, clients are named `client1`,
`client2`, … in construction order. The name is the *scope* under which the
server's namespaces are registered in the process-wide namespace table (see
[Namespaces and NodeIds](../sdk-fundamentals/namespace/namespace-mapping-in-o6.md#namespaces-and-nodeids)). Scopes let
several clients talk to servers that use the same namespace URIs without
colliding.

A name must be a valid Python identifier, must not match `server<digits>`,
must not be `global` or `::global`, and must be unique in the process.
Construction raises `ValueError` otherwise:

```python
Client(url, name="plant-hmi")   # ValueError: not an identifier
Client(url, name="server1")     # ValueError: reserved pattern
Client(url, name="hmi")         # fine, once
Client(url, name="hmi")         # ValueError: not unique
```

### Everything else goes on `client.config`

`client.config` is the live `ClientConfig` behind the native client. Assign to
it before `connect()`:

```python
client = Client("opc.tcp://localhost:4840")
client.config.sessionName = "recipe-controller"
client.config.requestedSessionTimeout = 60_000       # ms
client.config.sessionLocaleIds = ["en-US", "de-DE"]
client.config.timeout = 5_000                        # per-request timeout, ms
client.connect()
```

Common settings:

| Property | Meaning |
| --- | --- |
| `endpointUrl` | Server URL, `opc.tcp://host[:port][/path]`, with an IPv6 address in brackets such as `opc.tcp://[::1]:4840`. Required before any connect. |
| `endpoint` | A complete `EndpointDescription`, usually taken from `getEndpoints()`, to pin the exact endpoint instead of letting the client select one. |
| `securityMode` | `o6.SecurityMode.NONE` / `SIGN` / `SIGN_AND_ENCRYPT`. |
| `securityPolicy` | Short name (`"Basic256Sha256"`) or `o6.SecurityPolicy` member. `securityPolicyUri` holds the full URI. |
| `certificate`, `privateKey` | Client identity. Accepts a path string, a `Path`, or raw DER/PEM bytes. |
| `trustList`, `revocationList` | Trusted server or certificate authority (CA) certificates, and certificate revocation lists (CRLs). See [Secured connections](#secured-connections). |
| `acceptAllCertificates` | Skip server-certificate validation. Defaults to `False`; use only for development. |
| `loadUnknownDataTypes` | Load the DataType of a received structure the client cannot decode from the server, once per encoding. Defaults to `True`. Can change while connected. See [Unknown namespaces and structured values](../sdk-fundamentals/namespace/loading-and-using-nodesets.md#unknown-namespaces-and-structured-values). |
| `applicationUri` | URI advertised in the `ApplicationDescription`, `urn:o6-Python.unconfigured.application` by default. Must match the URI inside the client certificate on secured channels. |
| `applicationDescription` | The whole description, if you want to shape it in detail. |
| `sessionName`, `requestedSessionTimeout`, `sessionLocaleIds` | Session identity, lifetime, and preferred locales. |
| `timeout`, `secureChannelLifeTime`, `connectivityCheckInterval` | Request timeout, channel renewal interval, and keepalive period, all in ms. |
| `sendBufferSize`, `recvBufferSize`, `localMaxMessageSize`, `localMaxChunkCount` | Transport limits. Relevant when moving large arrays. |
| `outstandingPublishRequests` | How many Publish requests are kept in flight for subscriptions. |
| `maxAsyncServiceCalls` | Ceiling on concurrent service calls; the call that exceeds it fails with `BadTooManyOperations`. Defaults to `32`; `0` disables the limit. See [Too many concurrent calls](raw-services.md#concurrency-and-backpressure). |
| `logger` | Write-only. Redirects client log output to a Python logger. |
| `noReconnect`, `noNewSession` | Opt out of automatic reconnection or of creating a replacement session. |
| `allowNonePolicyPassword` | Permit an unencrypted username/password token. Defaults to `False`, even with credentials. |

Set credentials with `username=` and `password=` on the constructor, or on
the config:

```python
client.config.setUsernamePassword("operator", "s3cr3t")
```

Credentials never enable `allowNonePolicyPassword`; it stays `False`. If the
server offers password authentication only without encryption, `connect()`
fails. It does not weaken the policy or fall back to anonymous access.

Password tokens can be encrypted even on an unencrypted channel. Without
`certificate` and `privateKey`, the client can encrypt the password but does
not validate the server certificate, even when `trustList` is set. Configure
[certificate trust](#secured-connections) to authenticate the server.

Use an encrypted channel, as in the secured example below. To send plaintext
password tokens to a development endpoint, pass `allowNonePolicyPassword=True`
to `Client(...)` or set `client.config.allowNonePolicyPassword = True` before
connecting. The server must also allow that token policy.

For certificate-based user authentication (not the channel certificate), use
`client.config.setAuthenticationCert(cert, key)`.

### Secured connections

Configure application identity, channel protection and user identity separately:

- `certificate`, `privateKey`, `applicationUri` and `trustList` identify the
  applications and establish certificate trust. Each side needs to trust the
  other's certificate; the application URI must match its certificate.
  With a client certificate and an empty `trustList`, every server certificate
  is rejected. `acceptAllCertificates=True` bypasses validation and ignores
  the trust list; use it only for development.
- `securityPolicy` selects the algorithms and `securityMode` selects signing
  or signing with encryption. Use `SIGN_AND_ENCRYPT` to protect application
  data from being read on the network. `SIGN` alone does not encrypt it.
- `username` and `password` identify a user. The server authenticates that user
  and grants permissions independently of application-certificate trust.

Without a PKI, generate a self-signed certificate:

```python
from o6.util import createSelfSignedCertificate

key, cert = createSelfSignedCertificate(
    appUri="urn:example:client",
    commonName="ExampleClient@localhost",
)
```

A secured client configuration, assuming the named certificate files exist
and the server accepts these credentials:

```python
from pathlib import Path
from o6 import Client, SecurityMode, SecurityPolicy

client = Client(
    "opc.tcp://localhost:4840",
    certificate=Path("client_cert.der"),
    privateKey=Path("client_key.der"),
    trustList=[Path("server_cert.der")],
    securityMode=SecurityMode.SIGN_AND_ENCRYPT,
    securityPolicy=SecurityPolicy.BASIC256SHA256,
    applicationUri="urn:example:client",
    username="operator",
    password="s3cr3t",
)
client.connect()
```

The [secured client/server example](../server/security.md#a-secured-clientserver-pair)
includes matching trust lists, authentication and role permissions. The
[Security tutorial](../../tutorials/client/300_security.md) covers client-side
configuration and failure diagnosis.
[Application Description](../../tutorials/client/310_application-description.md)
covers how the client identifies itself.

### JSON5 configuration files

A client can also be configured from a JSON5 file in the format of open62541's
`UA_Client_newFromFile`. open62541 parses the file itself, so the same files
work in C and in o6. The open62541 repository has a commented example in
`examples/json_config/client_json_config.json5`.

```json5
// client.json5
{
  endpointUrl: "opc.tcp://localhost:4840",
  sessionName: "Line 3 HMI",
  timeout: 10000,
}
```

```python
client = o6.Client.newFromFile("client.json5")
client.connect()
```

`client.config.loadFromFile(path)` applies a file to an existing client that is
not connected.

- Every setting in the file is used, including `endpointUrl`, `securityMode`,
  `securityPolicyUri` and `userIdentityToken`. Everything the file leaves out
  gets the o6 default; the `endpointUrl` and `applicationUri` arguments of
  `newFromFile` count as o6 defaults.
- The security configuration comes from the file. `securityPolicies` and
  `authSecurityPolicies` name certificate and private key files, resolved
  against the working directory. Loading a file replaces `certificate`,
  `privateKey`, `trustList` and `revocationList`.
- Settings that the format has no keys for are reset to their defaults. Load
  the file first and set the rest on `client.config` afterwards.
- `asyncServiceCallRule` is ignored with a warning: requests beyond
  `maxAsyncServiceCalls` are always rejected with `BadTooManyOperations`,
  because waiting for capacity would block the client's event loop.

## Connecting and disconnecting

`connect()` uses the URL configured in `client.config`:

```python
client = Client("opc.tcp://localhost:4840")
client.connect()
```

Alternatively, set the URL after construction:

```python
client = Client()
client.config.endpointUrl = "opc.tcp://localhost:4840"
client.connect()
```

When the client owns a worker loop, `connect()` starts that worker before
connection setup. A client using a running application loop needs no worker.
Connection setup performs these steps:

1. finalizes the encryption settings (certificate, key, trust list),
2. opens the SecureChannel,
3. creates and activates the Session,
4. reads the server's `ApplicationUri` and registers it as this client's
   namespace 1,
5. synchronizes all remaining server namespaces and their custom data types
   (`updateRemoteNamespaces()`),
6. creates the default subscription used by `monitor()` unless opted out.

For sessions that do not need monitoring, skip the default subscription:

```python
client.connect(createDefaultSubscription=False)
```

Subscription limits or permissions then do not prevent reads, writes, calls
or browsing. To monitor later, create a subscription with
`createSubscription()` and pass it as `subscription=` to `monitor()` or
`monitorEvent()`. `defaultSubscription` raises `RuntimeError` while no default
exists.

If setup after session activation fails or is cancelled, `connect()` closes the
session before the error propagates. This includes a rejected
default-subscription creation.

To open only the SecureChannel, for discovery or as the first half of a
session transfer, pass `noSession=True`:

```python
client.connect(noSession=True)
```

By default, `disconnect()` deletes all subscriptions, closes the Session,
closes the SecureChannel and stops a client-owned worker thread:

```python
client.disconnect()
```

Two switches change this:

```python
client.disconnect(deleteSubscriptions=False)   # skip separate subscription-delete requests
client.disconnect(closeSession=False)          # close only the channel, keep the session
```

With `closeSession=False`, the Session stays alive on the server and
`deleteSubscriptions` is ignored. Session transfer and channel renewal need
this. `deleteSubscriptions=False` alone does not preserve subscriptions: the
current implementation still requests their deletion when closing the Session.
For deliberate session preservation, see [Advanced Session Management](sessions.md).
`disconnect()` never raises: on an already disconnected client, or one
whose event loop is gone, it returns `None`.

After a normal `disconnect()`, `connect()` runs the whole sequence above and
creates a new default subscription. Application monitoring must be set up again.

### Context managers

The context manager connects on entry (if not already connected) and
disconnects on exit, including when the block raises:

```python
from o6 import Client

with Client("opc.tcp://localhost:4840") as client:
    value = client.read("ns=1;s=IntegerVariable")
```

The asynchronous form behaves the same:

```python
async with Client("opc.tcp://localhost:4840") as client:
    value = await client.read("ns=1;s=IntegerVariable")
```

### Inspecting the connection

`client.connected` reports whether the Session is activated. It is a snapshot,
not a guarantee that the next request will succeed:

```python
print(client.connected)   # True
```

`client.state` returns the full picture as a 3-tuple of
`(SecureChannelState, SessionState, StatusCode)`:

```python
channel, session, status = client.state
print(channel)   # SecureChannelState.OPEN
print(session)   # SessionState.ACTIVATED
print(status)    # StatusCode.GOOD
```

After a disconnect, the tuple reads `(CLOSED, CLOSED, BAD_CONNECTION_CLOSED)`.

To receive connection notifications instead of polling, register a handler on
`client.onGlobalNotification` (see [Notification handler](notification-handler.md)).
It sees only connection start and stop, not every
`SecureChannelState`/`SessionState` transition. Poll `state` for those. The
[State callbacks tutorial](../../tutorials/client/320_state-callbacks.md) builds
a supervision loop around it.

Operations on a client that is not connected raise immediately:

```python
client.read("ns=1;s=IntegerVariable")   # Exception: Client is not connected
```

## Discovery

Discovery calls need an open SecureChannel but no Session. See
[Discovery and registration](discovery.md) for endpoint selection, LDS queries,
and registering an application.

## Connection recovery

By default, a lost connection triggers an attempt to reopen the channel and
reactivate the existing Session. If that Session has expired, the client may
create a replacement. Keep the client's event loop running during recovery.
`config.noReconnect=True` disables automatic reconnection;
`config.noNewSession=True` prevents replacing a lost Session.

| What happened | What the application needs to do |
|---|---|
| Channel lost, existing Session reactivated | Retain handles for unchanged nodes. Existing subscriptions and items can continue if the server has kept them alive. |
| Session lost and a replacement activated | Refresh namespaces with `updateRemoteNamespaces()`, resolve nodes again if the model changed, and recreate subscriptions and monitored items. Automatic recovery does not rerun the Python `connect()` setup. |
| Normal `disconnect()` followed by `connect()` | Namespace refresh and a new default subscription are part of `connect()`. Recreate the application's monitored items and any additional subscriptions. |
| A request was pending when the connection broke | Handle its failure separately. Reconnecting does not replay the request. |

An activated Session alone does not mean monitoring has recovered. See
[Subscription recovery](subscriptions.md#subscription-recovery) for detecting
lost subscriptions and rebuilding them. Reconnection also does not guarantee
delivery of every value change or event during an outage.

### Retrying operations

Reads can usually be retried after temporary connection or timeout failures,
with a delay and an application-defined retry limit. A write or Method call
may have reached the server even if its response was lost. Check the resulting
state, or use an application-specific way to detect duplicate commands,
before retrying an operation with side effects.

Authentication, certificate, permission, unknown-node and type-mismatch errors
need their cause corrected; reconnecting alone does not fix them. A failed
connection attempt is not an unlimited retry policy. Use `state` and the
operation's error to decide whether to wait, retry, rebuild setup or report
the failure.

### Node handles after recovery

A retained node handle keeps its NodeId; it does not track a replacement node
by BrowseName. It remains useful if the server still uses that identity.
Explicit `connect()` and `updateRemoteNamespaces()` clear navigation caches.
Automatic channel recovery alone does not. After an external model change,
call `client.invalidateNodeCache()` before navigating again, and replace
handles for deleted or replaced nodes. See
[Navigation caches and model changes](../node-api/navigation.md#navigation-caches-and-model-changes).

## Lifecycle notes

- The client owns native resources and, in a synchronous script, a worker
  thread. `disconnect()` releases the session and channel and stops that worker.
  Dropping the last reference triggers a best-effort cleanup in `__del__`. Do not rely on the garbage
  collector; use the context manager or call `disconnect()`.
- Client names, and therefore namespace scopes, are never reused within a
  process. Creating and discarding thousands of clients grows the namespace
  table. In a service, reconnect an existing client instead of constructing new
  ones.

## Event loops and integration

The ordinary `with` and `async with` patterns need no `loop=` argument.
`client.loop` exposes the event loop selected at construction; that choice
is fixed for the client's lifetime.

| Construction context | Loop selection |
|---|---|
| Ordinary script, no running loop | The client creates a loop and runs it on a worker thread when connecting. |
| Inside an async application | The client uses the running loop; the application keeps it running. |
| Explicit `loop=some_loop` | The client uses the supplied loop; the application owns it. |
| IPython/Jupyter with no explicit `loop=` | The client creates a worker loop so synchronous notebook calls do not block the kernel loop. |

A loop owned by the application remains open after `disconnect()`. Keep it
running while the client needs to receive responses or notifications. An
ordinary synchronous call with an idle supplied loop drives that loop until
the request completes, but this does not provide continuous notification delivery.

From another thread, a synchronous request waits for its result. An async
task on another loop awaits the request on its own loop; the client's loop
must remain running. Loop ownership does not mean every caller must use that
same loop.

In a notebook, use top-level `await` for the async form instead of calling
`asyncio.run()` inside the already-running kernel. A plain synchronous cell
can use the synchronous form with the default worker loop.

Callbacks run on the client's loop. Keep them short; client requests made
from a callback need an async handler so that the loop can process the response.
See [Application Notifications](notification-handler.md#synchronous-and-asynchronous-handlers)
and [Subscriptions & Events](subscriptions.md) for handler examples.
