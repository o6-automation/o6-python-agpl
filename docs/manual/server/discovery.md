# Discovery & Registration

Use `Server.setMdns()` to announce OPC UA applications and discover them on the
local network. Configure mDNS before starting the server.

The [LDS example](../../examples/advanced_applications-lds-server.md) has
runnable LDS, application and client programs.

## Announce an application directly

For applications that do not register with an LDS:

```python
import o6
from o6.discovery import MdnsConfig

server = o6.Server(port=4840)
server.setMdns(MdnsConfig(interface="eth0"))

with server:
    server.registerServerOnNetwork("Workshop", "opc.tcp://workshop:4840", ["DA"])
    input("Press Enter to withdraw and stop\n")
    server.deregisterServerOnNetwork("Workshop")
```

The server announces its records while it runs: `stop()` withdraws them and
`start()` announces them again, including records added before startup. Records
added while no mDNS configuration with `announce=True` is attached are not
announced. Both record methods raise `StatusCodeError` on failure and are awaited
in async code. Removing an unknown name succeeds. To disable mDNS, call
`setMdns(None)` while the server is stopped.

Give the URL a bare hostname such as `workshop`, which listeners discover as
`workshop.local`. A host qualified with `.local` is announced as the bare
hostname. Other hosts, such as IP addresses or `plc.example.com`, raise
`ValueError`.

### Hosting an LDS

A Local Discovery Server (LDS) accepts other applications' registrations and
answers discovery queries. Configure the receiving server before starting it:

```python
from o6.ns.ns0.datatypes import ApplicationType

server.config.applicationType = ApplicationType.DISCOVERY_SERVER
```

This enables registration services (`server.config.registeredServersEnabled`,
which can also be set directly afterwards); it does not attach an mDNS driver. Observe
incoming registrations through
[discovery notifications](notification-handler.md#discovery-registerserver).

## Announce LDS registrations

Enable automatic announcements on a Local Discovery Server (LDS):

```python
import o6
from o6.discovery import MdnsConfig
from o6.ns.ns0.datatypes import ApplicationType

lds = o6.Server(port=4840)
lds.config.applicationType = ApplicationType.DISCOVERY_SERVER
lds.setMdns(MdnsConfig(interface="eth0", announceRegisteredServers=True))

with lds:
    input("Press Enter to stop the LDS\n")
```

Replace `eth0` with your network interface. Applications use
[`Client.registerServer()` and `Client.unregisterServer()`](../client/discovery.md#confirmed-lds-registration)
to register, renew, update and remove their announcements. The LDS also removes
announcements when registrations expire. No callback is needed.

`announceRegisteredServers` defaults to false and requires `announce=True` and
`ApplicationType.DISCOVERY_SERVER`. It only selects whether the mDNS driver
announces registered servers: every registration with an `opc.tcp://` DiscoveryUrl
gets a `FindServersOnNetwork` entry either way. The entry is named by the
`mdnsServerName` of the registration (else its first server name), points to the
first `opc.tcp://` DiscoveryUrl and lists `NA` as capability if the registration
gives none. Only the registration changes or removes the entry: a local
`registerServerOnNetwork()` or `deregisterServerOnNetwork()` with its name fails
with `BadNotWritable` or `BadNoDeleteRights`. Use announcement names of 1–63
UTF-8 bytes.

### Registration success and publication failures

A successful registration does not guarantee mDNS publication or reception.
Use `opc.tcp://` URLs with bare hostnames and no path, such as
`opc.tcp://workshop:4840`.

### Registering an application with an LDS

An application sends registration requests with `Client.registerServer()` and
`Client.unregisterServer()`. See the
[application-side walkthrough](../client/discovery.md#confirmed-lds-registration).

A running server can register itself with an LDS so that clients find it
through `FindServers`. Configure its capabilities before startup. For a server
that provides both current and historical data:

```python
server.config.serverCapabilities = ["DA", "HD"]
server.start()
server.registerDiscovery("opc.tcp://localhost:4840")
# ... serve ...
server.deregisterDiscovery("opc.tcp://localhost:4840")
```

`server.config.serverCapabilities` accepts the
[Part 12 capability identifiers](https://reference.opcfoundation.org/specs/OPC-10000-12/annex-d)
supported by the SDK. Advertise only the capabilities the application provides.
The default `[]` announces `NA` (no capability information) for a server. The
setting is writable only while fully stopped; apply it after security or
file-based configuration, which can reset it. Registration includes these
capabilities in `MdnsDiscoveryConfiguration`; an mDNS driver is not required.

The server registers its ApplicationDescription with the DiscoveryUrls of its
listeners. Both calls only start the request and return. The answer of the LDS
is logged by the server, not raised: check the registration with
`Client.findServers()` at the LDS. Repeat `registerDiscovery()` to renew the
registration before the LDS expires it. A request that does not complete
within 5 seconds is cancelled.

Only one `registerDiscovery()` or `deregisterDiscovery()` request can be pending
per server. An overlapping call raises `StatusCodeError` with
`BadTooManyOperations`; retry after the pending request completes.

With a certificate configured through `o6.Server` or `config.setEncryption()`,
the requests use SignAndEncrypt with Basic256Sha256 by default. The LDS must
trust the server certificate, and the server verifies the LDS certificate like
a client certificate, with its `trustList` or `acceptAllCertificates`. The
certificate must carry the server's `applicationUri`. Without a certificate,
the requests use SecurityPolicy#None, which an open62541 LDS rejects.
`securityMode=` and `securityPolicy=` select `NONE` or another RSA policy
explicitly; pass the same values to both calls.

`semaphoreFilePath=` names a semaphore file that coordinates shutdown across
instances. Deregister in your shutdown path.

Two LDS-side callbacks exist in the API but raise `NotImplementedError` in the
current build, because they depend on compile-time gated open62541 discovery
features:

- `setRegisterServerCallback`, invoked when another server registers with this
  one.
- `setServerOnNetworkCallback`, invoked when a server is discovered via mDNS.

## Discovering applications and resolving hostnames

To actively discover other applications, include these options in `MdnsConfig`:

```python
MdnsConfig(interface="eth0", queryPresence=True, queryDetails=True, queryInterval=60)
```

For discovery without announcing, also set `announce=False`. Without
queries, a listening server only records the applications that announce
themselves. Clients query results with
[`findServersOnNetwork()`](../client/discovery.md#finding-servers). To observe
changes on the server, use
[discovery notifications](notification-handler.md#discovery-serveronnetwork).

An announced hostname such as `workshop` is discovered as `workshop.local`.
Client machines need an mDNS-capable system resolver. If no other service
publishes the hostname's address, supply
`hostAddresses={"workshop.local": ["192.0.2.10"]}` in `MdnsConfig`, replacing the
address with the application's actual IP address.

See [`MdnsConfig`](../../api_reference/mdnsconfig.md) for all configuration options.

## Availability

Linux and macOS PyPI wheels include mDNS. No optional extra or separate mDNS
library is needed. Windows wheels do not include mDNS: the configuration types
are importable, but enabling mDNS raises `NotImplementedError`.

mDNS requires IPv4 multicast on the selected local network (UDP port 5353). Check
[`mdnsAvailable`](../../api_reference/mdnsavailable.md) for build support;
unavailable builds raise `NotImplementedError` when enabling mDNS.
