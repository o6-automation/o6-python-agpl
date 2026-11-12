# Application Description

Read the server's application description, set your client's own, and discover other servers.

An `ApplicationDescription` is the OPC UA structure that identifies an application: its name, product and URI. The server's description tells clients what they talk to. The client's description tells the server who connects, so server-side logs, audit trails and discovery responses can tell the control plane and the HMI dashboard apart.

- **Server side:** every server publishes its description. Read it with `client.findServers(...)` (the FindServers service) or `client.getEndpoints(...)`, which embeds it in every endpoint.
- **Client side:** set `applicationUri=` and the `name=` label on the `Client(...)` constructor. They end up in the CreateSession request and in the active session the server maintains.

!!! info
    This tutorial expects the [example server running](../setup.md) in the background. It builds on [Connect](100_connect.md), [Browse](110_browse.md) and [Security](300_security.md). The snippets read the distillery's default `ApplicationDescription`, which o6 publishes.

---

## Read the distillery's application description

The server publishes an `ApplicationDescription` for every endpoint. `client.findServers(...)` returns the descriptions without an active session, so connect with `client.connect(noSession=True)`:

```python
client.connect(noSession=True)
servers = client.findServers("opc.tcp://localhost:4840")
for srv in servers:
    print(srv.applicationUri)              # e.g. urn:o6-Python.unconfigured.application
    print(srv.applicationName.text)        # e.g. "o6-python Server"
    print(srv.productUri)                  # e.g. https://o6-automation.com/o6-python
    print(srv.applicationType.name)        # "SERVER" / "CLIENT" / "CLIENT_AND_SERVER"
    print(srv.discoveryUrls)               # URLs the server can be reached at
```

`getEndpoints(...)` returns an `EndpointDescription` per endpoint (security policy, mode, transport profile) with the same server description embedded:

```python
endpoints = client.getEndpoints("opc.tcp://localhost:4840")
for ep in endpoints:
    print(ep.endpointUrl, ep.securityPolicyUri, ep.securityMode.name)
    print("  server:", ep.server.applicationName.text)
```

A non-`NONE` `securityMode` means the server advertises a secure endpoint; `securityPolicyUri` names its policy. If you only see `NONE` / `None`, the server has no encryption enabled. Check its configuration before you use it in production.

#### Putting it all together

!!! caution
    Don't call `client.connect(noSession=True)` inside a `with Client(...) as client:` block. Entering the `with` block already connects with a full session, and a second `connect()` on a connected client hangs. Construct the client and connect once, manually:

```python
import o6
from o6 import Client

client = Client("opc.tcp://localhost:4840")
client.connect(noSession=True)

try:
    print("--- findServers ---")
    for srv in client.findServers("opc.tcp://localhost:4840"):
        print(f"{srv.applicationUri}  {srv.applicationName.text}  {srv.discoveryUrls}")

    print("--- getEndpoints ---")
    for ep in client.getEndpoints("opc.tcp://localhost:4840"):
        print(f"{ep.endpointUrl}  policy={ep.securityPolicyUri}  mode={ep.securityMode.name}")
finally:
    client.disconnect()
```

---

## Set the client-side description

The server tells the HMI dashboard from the control plane by the `username`/`password` from [Security](300_security.md). For human-readable identification in server-side logs, audit trails and the `o6.s` active session table, the client also sets its `applicationUri` and a `name` label. These fields are advisory; the distillery server accepts any value.

Give each distillery client a distinct URI and a `name` for the server's session log:

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

The `name` must be a valid Python identifier and must not collide with the auto-generated names `client1`, `client2`, …. The `applicationUri` is a free-form string; a URN is the convention.

Read back what the client sent:

```python
print(hmi.config.applicationUri)   # urn:distillery:hmi
print(hmi._name)                    # hmi_dashboard
```

!!! info
    On a certificate-based secure channel (see [Security](300_security.md)), open62541 enforces that the `applicationUri` in the certificate matches the one you pass to the client constructor. For a `username`/`password` connection it is advisory.

---

## Discover other servers on the network

`findServers(...)` queries a single endpoint. `findServersOnNetwork(...)` queries a *Local Discovery Server* (LDS) for the mDNS-registered servers visible on the network. Use it to find several OPC UA servers without knowing their URLs.

```python
# A regular server will return an empty list or an error for this
# call — it only makes sense when connected to an LDS.
servers = client.findServersOnNetwork()
for srv in servers:
    print(srv.serverName, srv.discoveryUrl, srv.serverCapabilities)
```

The result is paginated; page through large registries with `starting_record_id` and `max_records_to_return`. Each `ServerOnNetwork` carries a `recordId` for the next page, the server's `discoveryUrl` and a list of `serverCapabilities` strings (`"DA"` for Data Access, `"HE"` for Historical Events, etc.).

The tutorial runs no LDS, so the snippets below return an empty result.

#### Putting it all together

```python
import o6
from o6 import Client

with Client("opc.tcp://localhost:4840") as client:
    # 1. Read the server's own description
    for srv in client.findServers("opc.tcp://localhost:4840"):
        print(srv.applicationName.text, "@", srv.discoveryUrls)

    # 2. Endpoints this server exposes
    for ep in client.getEndpoints("opc.tcp://localhost:4840"):
        print(ep.endpointUrl, ep.securityMode.name, ep.securityPolicyUri)

    # 3. (LDS only) servers visible on the network
    for srv in client.findServersOnNetwork():
        print(srv.serverName, srv.discoveryUrl)
```

---

## Next steps

| Topic | What it covers |
|---|---|
| [State callbacks](320_state-callbacks.md) | Poll `client.state` to detect when the connection drops, the session is reactivated or the secure channel is renegotiated. |
