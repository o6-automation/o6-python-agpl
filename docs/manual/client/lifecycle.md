# Lifecycle

## Creating a client

A client is created before it knows anything about a connection. The
constructor takes the settings most applications need as keyword arguments;
everything else is set on `client.config` afterwards.

```python
from o6 import Client

client = Client("opc.tcp://localhost:4840")
```

The full constructor signature is:

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
    securityMode=None,       # o6.SecurityMode
    securityPolicy=None,     # o6.SecurityPolicy or short name
    applicationUri=None,     # URI sent in the ApplicationDescription
    username=None,           # UserNameIdentityToken
    password=None,
    name="",                 # process-unique client name
)
```

!!! info
    Nothing in that list is mandatory. `Client()` with no arguments is valid — the
    endpoint URL can be supplied later through `client.config.endpointUrl` (just note that connect will error, when no valid endpoint url is configured).

### The client name

Every client carries a `name`. When you do not pass one, the client is named
`client1`, `client2`, … in construction order. The name is not cosmetic: it
becomes the *scope* under which the server's namespaces are registered in the
process-wide namespace table (see [Namespaces and NodeIds](address-space.md#namespaces-and-nodeids)),
which is what lets several clients talk to servers that use the same namespace
URIs without colliding.

A name must be a valid Python identifier, must not look like `server<digits>`,
must not be `global` or `::global`, and must be unique in the process. Violations
raise `ValueError` immediately at construction:

```python
Client(url, name="plant-hmi")   # ValueError: not an identifier
Client(url, name="server1")     # ValueError: reserved pattern
Client(url, name="hmi")         # fine, once
Client(url, name="hmi")         # ValueError: not unique
```

### Everything else goes on `client.config`

`client.config` is the live `ClientConfig` behind the native client. Assign to
it any time before `connect()`:

```python
client = Client("opc.tcp://localhost:4840")
client.config.sessionName = "recipe-controller"
client.config.requestedSessionTimeout = 60_000       # ms
client.config.sessionLocaleIds = ["en-US", "de-DE"]
client.config.timeout = 5_000                        # per-request timeout, ms
client.connect()
```

The settings that matter most often:

| Property | Meaning |
| --- | --- |
| `endpointUrl` | Server URL. Required before any connect. |
| `endpoint` | A complete `EndpointDescription`, usually taken from `getEndpoints()`, to pin the exact endpoint instead of letting the client select one. |
| `securityMode` | `o6.SecurityMode.NONE` / `SIGN` / `SIGN_AND_ENCRYPT`. |
| `securityPolicy` | Short name (`"Basic256Sha256"`) or `o6.SecurityPolicy` member. `securityPolicyUri` holds the full URI. |
| `certificate`, `privateKey` | Client identity. Accepts a path string, a `Path`, or raw DER/PEM bytes. |
| `trustList`, `revocationList` | Certificates the client trusts, and their CRLs. |
| `applicationUri` | URI advertised in the `ApplicationDescription`. Must match the URI inside the client certificate on secured channels. |
| `applicationDescription` | The whole description, if you want to shape it in detail. |
| `sessionName`, `requestedSessionTimeout`, `sessionLocaleIds` | Session identity, lifetime, and preferred locales. |
| `timeout`, `secureChannelLifeTime`, `connectivityCheckInterval` | Request timeout, channel renewal interval, and keepalive period, all in ms. |
| `sendBufferSize`, `recvBufferSize`, `localMaxMessageSize`, `localMaxChunkCount` | Transport limits. Relevant when moving large arrays; see [Performance](../performance.md). |
| `outstandingPublishRequests` | How many Publish requests are kept in flight for subscriptions. |
| `logger` | Write-only. Redirects client log output to a Python logger. |
| `noReconnect`, `noNewSession` | Opt out of automatic reconnection or of creating a replacement session. |
| `allowNonePolicyPassword` | Permit a username/password token on an unencrypted channel. |

Credentials are set either through the constructor or through the config:

```python
client.config.setUsernamePassword("operator", "s3cr3t")
```

Passing `username=` to the constructor does the same thing and additionally
sets `allowNonePolicyPassword = True`, so that credentials work against a
development server with no encryption. On a real deployment you want an
encrypted channel instead — without it the stack will strip the
username/password `UserTokenPolicy` and log a warning that the password would
travel in the clear.

For certificate-based user authentication (as opposed to the channel
certificate) use `client.config.setAuthenticationCert(cert, key)`.

Certificates can be generated on the spot when you don't have a PKI at hand:

```python
from o6.util import createSelfSignedCertificate

key, cert = createSelfSignedCertificate(
    appUri="urn:example:client",
    commonName="ExampleClient@localhost",
)
```

A fully secured client therefore looks like this:

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

The [Security tutorial](../../tutorials/client/300_security.md) walks through the
handshake step by step, including what each failure mode looks like, and
[Application Description](../../tutorials/client/310_application-description.md)
covers how the client identifies itself.

## Connecting and disconnecting

`connect()` takes the URL configured in teh `client.config`:

```python
client = Client("opc.tcp://localhost:4840")
client.connect()

client = Client()
client.config.endpointUrl = "opc.tcp://localhost:4840"
client.connect()
```

A plain `connect()` does considerably more than opening a socket. In order, it:

1. finalizes the encryption settings (certificate, key, trust list),
2. opens the SecureChannel,
3. creates *and* activates the Session,
4. reads the server's `ApplicationUri` and registers it as this client's
   namespace 1,
5. synchronizes all remaining server namespaces and their custom data types
   (`updateRemoteNamespaces()`),
6. creates the default subscription used by `monitor()`,
7. starts the background worker thread that drives the client's event loop.

If any of the post-session steps fail, the session that was already activated on
the server is closed again before the error propagates, so a failed `connect()`
never leaves an orphaned session behind.

To open only the SecureChannel — enough for discovery, or as the first half of a
session transfer — pass `noSession=True`:

```python
client.connect(noSession=True)
```

Disconnecting is the mirror image. By default it deletes all subscriptions,
closes the Session, closes the SecureChannel, and stops the worker thread:

```python
client.disconnect()
```

Two switches change that:

```python
client.disconnect(deleteSubscriptions=False)   # leave subscriptions on the server
client.disconnect(closeSession=False)          # close only the channel, keep the session
```

With `closeSession=False` the Session stays alive on the server and
`deleteSubscriptions` is ignored — that combination is what session transfer and
channel renewal need. `disconnect()` is always safe to call: on an already
disconnected client, or one whose event loop is gone, it returns `None` instead
of raising.

A client can be reconnected after disconnecting. Connecting again re-runs the
whole sequence above, which means a *new* default subscription with a new id.

### Context managers

The idiomatic form is the context manager, which connects on entry (if not
already connected) and disconnects on exit, including when the block raises:

```python
from o6 import Client

with Client("opc.tcp://localhost:4840") as client:
    value = client.read("ns=1;s=IntegerVariable")
```

The asynchronous counterpart behaves identically with `await` inside:

```python
async with Client("opc.tcp://localhost:4840") as client:
    value = await client.read("ns=1;s=IntegerVariable")
```

### Inspecting the connection

`client.connected` is `True` only when the channel is open **and** the session is
activated:

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

After a disconnect the same tuple reads `(CLOSED, CLOSED, BAD_CONNECTION_CLOSED)`.
There is no state-change callback — you poll `state` when you need it, which is
what the [State callbacks tutorial](../../tutorials/client/320_state-callbacks.md)
builds a supervision loop around.

Operations on a client that is not connected raise immediately rather than
silently doing nothing:

```python
client.read("ns=1;s=IntegerVariable")   # Exception: Client is not connected
```

## Discovery

Discovery answers two questions: *which servers exist* and *what endpoints does
this server offer*. Both are services, so they need an open SecureChannel — but
not a session. The usual shape is therefore a throwaway client with
`noSession=True`:

```python
from o6 import Client

client = Client("opc.tcp://localhost:4840")
client.connect(noSession=True)

for ep in client.getEndpoints("opc.tcp://localhost:4840"):
    print(ep.endpointUrl, ep.securityMode, ep.securityPolicyUri)

client.disconnect()
```

Note the endpoint URL appears twice, and for different reasons: the constructor
argument decides where the *channel* goes, the method argument is the URL
carried *inside* the request. Calling `getEndpoints()` on a client that has no
channel raises `StatusCodeError(BadServerNotConnected)`.

Three calls are available:

- **`getEndpoints(endpointUrl, *, localeIds=None, profileUris=None)`** returns the
  list of `EndpointDescription` objects: URL, security mode, security policy
  URI, transport profile, server certificate, and the accepted
  `UserTokenPolicy` entries. `profileUris` narrows the result to a transport
  profile.
- **`findServers(endpointUrl, *, serverUris=None, localeIds=None)`** returns
  `ApplicationDescription` objects. Against a Local Discovery Server this
  enumerates every registered server on the host; against a normal server it
  returns that server's own description, including the discovery URLs you can
  feed back into `getEndpoints()`.
- **`findServersOnNetwork(startingRecordId=0, maxRecordsToReturn=0, serverCapabilityFilter=None)`**
  queries an LDS for servers that announced themselves via mDNS or
  *RegisterServer2*. The result is paginated through `startingRecordId`; each
  `ServerOnNetwork` entry carries a `recordId` to continue from. A regular
  server returns an empty list.

A discovered endpoint can be pinned for the real connection:

```python
endpoints = probe.getEndpoints(url)

client = Client(url)
client.config.endpoint = endpoints[0]
client.connect()
```

## Sessions and channels, beyond connect

Two scenarios need more control than `connect()` / `disconnect()`.

### Session transfer

An OPC UA Session is not tied to a SecureChannel for life; it can be re-bound to
a new one. Both halves are available.

If *this* client owns the session and its channel was renewed or
re-established, re-bind it:

```python
client.activateCurrentSession()
```

If another client owns the session and you want to take it over, open a channel
without a session and activate the existing one with its authentication token
and server nonce:

```python
receiver.connect(noSession=True)
receiver.activateSession(authToken, serverNonce)
```

Both calls send `ActivateSession` and then create the default subscription, so
the client is fully usable afterwards. On the handing-over side, close the
channel but keep the session alive with `disconnect(closeSession=False)`.

### Reverse connect

In a reverse-connect deployment the *server* initiates the TCP connection, which
is how you reach a client that sits behind a firewall. The client opens a listen
socket and waits:

```python
client = Client("opc.tcp://localhost:4840")     # still needed: the server's URL
client.startReverseConnect(port=4843, hostnames=["0.0.0.0"])
# returns once a server has connected — the session is activated
value = client.read("ns=1;s=Rev")
client.disconnect()
```

The call does not return until a server actually connects, so in synchronous
code it blocks; in async code, schedule it as a task and await it with a timeout:

```python
task = asyncio.ensure_future(client.startReverseConnect(4843))
await asyncio.wait_for(task, timeout=15)
print(client.connected)   # True
```

`hostnames` selects which interfaces to advertise — `None` or an empty list lets
the stack decide. The endpoint URL still has to be configured, because the
client uses it to identify the server it expects. Tear the connection down with
the ordinary `disconnect()`. The server side of the handshake is
`server.addReverseConnect(url)` and `server.removeReverseConnect(handle)`.

## Lifecycle notes

A few practical details worth keeping in mind for long-running programs.

The client owns native resources and a thread. `disconnect()` releases the
session and channel and stops the worker; dropping the last reference triggers a
best-effort cleanup in `__del__`, but relying on the garbage collector for that
is fragile — prefer the context manager or an explicit `disconnect()`.

Subscriptions are deleted on disconnect by default. If you intend to keep them
alive across a channel renewal — the point of `disconnect(closeSession=False)` —
pass `deleteSubscriptions=False` or keep the session open.

Node objects cache their children. That cache is only valid while the server's
model does not change; after the server adds or renames nodes, resolve them
again from the client rather than reusing a cached node.

Client names, and therefore namespace scopes, are never reused within a process.
Creating and discarding thousands of clients in one process grows the namespace
table, so in a service, reconnect an existing client instead of constructing new
ones.
