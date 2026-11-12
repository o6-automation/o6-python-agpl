# Discovery & Registration

Use `Client` to find OPC UA servers or register an application with a Local
Discovery Server (LDS). To host the LDS, see [server discovery](../server/discovery.md).

## Finding servers

Connect with `client.connect(noSession=True)`, then call:

| Method | Returns |
| --- | --- |
| [`findServers(lds_url)`](../../api_reference/client.md#o6.client.Client.findServers) | Applications registered with the connected LDS. |
| [`findServersOnNetwork()`](../../api_reference/client.md#o6.client.Client.findServersOnNetwork) | Applications announced through network discovery. |
| [`getEndpoints(server_url)`](../../api_reference/client.md#o6.client.Client.getEndpoints) | The connected server's endpoints and security options. |

Connect to the application server itself before calling `getEndpoints()`.
In async code, await connection and discovery calls.

## Confirmed LDS registration

This example registers an application already running on port 4841 with an LDS
on port 4840.

The LDS accepts registrations only over a signed channel with a client
certificate it trusts and whose application URI is the registered server URI.

```python
import o6

lds_url = "opc.tcp://localhost:4840"
server_uri = "urn:example:registered-application"
discovery_urls = ["opc.tcp://localhost:4841"]

client = o6.Client(
    lds_url,
    certificate="application_cert.der",
    privateKey="application_key.der",
    trustList=["lds_cert.der"],
    applicationUri=server_uri,
    securityMode=o6.SecurityMode.SIGN_AND_ENCRYPT,
    securityPolicy=o6.SecurityPolicy.BASIC256SHA256,
)
client.connect(noSession=True)

client.registerServer(
    server_uri,
    discovery_urls,
    serverName="Example application",
    serverCapabilities=["DA"],
)
print(client.findServers(lds_url, serverUris=[server_uri]))

# When the application stops:
client.unregisterServer(server_uri, discovery_urls)
client.disconnect()
```

Repeat `registerServer()` periodically to renew the registration, or call it
with changed metadata to update it. Keep the same URI and at least one existing
URL; unregister first when replacing every URL. Await these calls in async code.

With [LDS announcements enabled](../server/discovery.md#announce-lds-registrations),
the LDS publishes the application's name and capabilities through mDNS. Set
`mdnsServerName` to use a name different from `serverName`.

Both registration methods raise `StatusCodeError` on rejection. Success confirms
registration, but does not guarantee mDNS publication or reception. See
[publication failures](../server/discovery.md#registration-success-and-publication-failures).
For all options, see the [Client API reference](../../api_reference/client.md#o6.client.Client.registerServer).
