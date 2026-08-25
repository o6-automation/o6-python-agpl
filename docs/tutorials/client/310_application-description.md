


# Application Description

After you setup a control plane via monitoring and a HMI dashboard with security configurations with an encrypted channel, the server doesn't yet know *who* they are in human terms — it just knows the cert and the user token. The next step is to give each side a real *application description* (a name, a product, a URI) so server-side logs, audit trails, and discovery responses can tell the two clients apart more easily.

An `ApplicationDescription` is the OPC UA structure that identifies an endpoint — on the server side it tells clients what they're talking to, and on the client side it tells the server who's connecting. `o6` exposes this from both ends:

- **Server side:** the distillery's own description is published automatically — every server has one. You read it with `client.findServers(...)` (which calls the spec's *FindServers* service) or `client.getEndpoints(...)` (which embeds the server's `ApplicationDescription` in every endpoint).
- **Client side:** the client side of the description is set via the `Client(...)` constructor
    - `applicationUri=`
    - `name=` label

 These end up in the *CreateSession* request and in the `o6` style *active session* the server maintains.

This page walks through three steps:

- Read the distillery server's `ApplicationDescription` to confirm what you're connecting to.
- Set the client-side description so the server can tell your dashboards apart.
- Use `findServers` and `findServersOnNetwork` to discover other servers on the host.

!!! info
    This tutorial expects the [example server running](../setup.md) in the background, and assumes you know how to [create and connect](100_connect.md) a client, how to [browse](110_browse.md) the address space, and how to [secure](300_security.md) the connection. The snippets use the distillery's own `ApplicationDescription` (which open62541 publishes by default) as the example.

---

## Read the distillery's application description

The distillery server publishes an `ApplicationDescription` for every endpoint it exposes. `client.findServers(...)` returns the descriptions without needing an active session — it uses the `noSession` connection shape (`client.connect(noSession=True)`):

```python
client.connect(noSession=True)
servers = client.findServers("opc.tcp://localhost:4840")
for srv in servers:
    print(srv.applicationUri)        # e.g. urn:open62541.unconfigured.application
    print(srv.applicationName)      # e.g. "en:open62541-based OPC UA Application"
    print(srv.productUri)           # e.g. http://open62541.org
    print(srv.applicationType)      # 0 = SERVER, 1 = CLIENT, 2 = CLIENT_AND_SERVER
    print(srv.discoveryUrls)        # URLs the server can be reached at
```

`getEndpoints(...)` returns the same description embedded in each endpoint, plus the matching `EndpointDescription` (security policy, mode, transport profile):

```python
endpoints = client.getEndpoints("opc.tcp://localhost:4840")
for ep in endpoints:
    print(ep.endpointUrl, ep.securityPolicyUri, ep.securityMode)
    print("  server:", ep.server.applicationName)
```

A non-`NONE` `securityMode` in the endpoint tells you the server is advertising a secure endpoint; the `securityPolicyUri` tells you which one. If you only see `NONE` / `None`, the server has not enabled encryption and you should check the server's config before relying on it for anything real.

#### Putting it all together

!!! caution
    Don't call `client.connect(noSession=True)` from inside a `with Client(...) as client:` block — entering the `with` already connects (with a full session), and a second `connect()` call on an already-connected client hangs. Construct the client and connect manually instead, exactly once:

```python
import o6
from o6 import Client

client = Client("opc.tcp://localhost:4840")
client.connect(noSession=True)

try:
    print("--- findServers ---")
    for srv in client.findServers("opc.tcp://localhost:4840"):
        print(f"{srv.applicationUri}  {srv.applicationName}  {srv.discoveryUrls}")

    print("--- getEndpoints ---")
    for ep in client.getEndpoints("opc.tcp://localhost:4840"):
        print(f"{ep.endpointUrl}  policy={ep.securityPolicyUri}  mode={ep.securityMode}")
finally:
    client.disconnect()
```

---

## Set the client-side description

The server distinguishes the HMI dashboard from the control plane via the `username`/`password` you set in [Security](300_security.md). For human-readable identification (server-side logs, audit trails, the `o6.s` *active session* table) the client also sets its own `applicationUri` and a `name` label. The distillery's server is happy with anything you set here — these fields are advisory, not gated.

For the distillery's two clients, give each a distinct URI and a `name` that will show up in the server's session log:

```python
from o6 import Client

hmi = Client(
    "opc.tcp://localhost:4840",
    name="hmi_dashboard",
    applicationUri="urn:distillery:hmi",
)

control = Client(
    "opc.tcp://localhost:4840",
    name="control_plane",
    applicationUri="urn:distillery:control",
)
```

The `name` must be a valid Python identifier and must not collide with the auto-generated `client1`, `client2`, … (use a distinct string). The `applicationUri` is free-form — a URN is the convention, but anything that fits in a string is fine.

You can read back what the client sent on the `client.config`:

```python
print(hmi.config.applicationUri)   # urn:distillery:hmi
print(hmi._name)                    # hmi_dashboard
```

!!! info
    When you use a cert-based secure channel (the [Security](300_security.md) flow), the `applicationUri` in the cert must match the `applicationUri` you pass to the client constructor — open62541 enforces this. For a `username`/`password` connection it's advisory.
---

## Discover other servers on the network

`findServers(...)` queries a single endpoint. `findServersOnNetwork(...)` queries a *Local Discovery Server* (LDS) for the mDNS-registered servers visible on the network — useful when the distillery is one of several OPC UA servers on the same host and you want to find them all without knowing their URLs.

```python
# A regular server will return an empty list or an error for this
# call — it only makes sense when connected to an LDS.
servers = client.findServersOnNetwork()
for srv in servers:
    print(srv.serverName, srv.discoveryUrl, srv.serverCapabilities)
```

The result is paginated — large registries can be paged with `starting_record_id` and `max_records_to_return`. Each `ServerOnNetwork` carries a `recordId` for the next page, the server's `discoveryUrl`, and a list of `serverCapabilities` strings (`"DA"` for Data Access, `"HE"` for Historical Events, etc.).

For the distillery tutorial the LDS isn't running, so the snippets below expect an empty result on a regular server. The call is included for completeness — the LDS path is the production discovery workflow.

#### Putting it all together

```python
import o6
from o6 import Client

with Client("opc.tcp://localhost:4840") as client:
    # 1. Read the server's own description
    for srv in client.findServers("opc.tcp://localhost:4840"):
        print(srv.applicationName, "@", srv.discoveryUrls)

    # 2. Endpoints this server exposes
    for ep in client.getEndpoints("opc.tcp://localhost:4840"):
        print(ep.endpointUrl, ep.securityMode, ep.securityPolicyUri)

    # 3. (LDS only) servers visible on the network
    for srv in client.findServersOnNetwork():
        print(srv.serverName, srv.discoveryUrl)
```

---

## What's next?

- [State callbacks](320_state-callbacks.md) — poll `client.state` to know when the connection drops, the session is reactivated, or the secure channel is renegotiated.