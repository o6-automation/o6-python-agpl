# Security policies and endpoints

Authentication gets a session onto the distillery, but the bytes are still flying over the wire in cleartext. Without encryption, anyone who can sniff the network segment reads every value the operator writes, and tampers with messages on the way back. This page adds the encryption layer: certificates, security policies, and the encrypted endpoints that advertise them.

By the end, the distillery listens for `None` (anonymous, plaintext) **and** `Basic256Sha256` (certificate + signed and encrypted), and a properly-configured client picks the secure one.

---

## What does a security policy do?

OPC UA separates the *algorithm suite* from the *level of protection* from the *who are you?* question:

- **Security policy** — the cryptographic suite. `o6.SecurityPolicy` has six members: `NONE`, `BASIC128RSA15`, `BASIC256`, `BASIC256SHA256`, `AES128_SHA256_RSAOAEP`, `AES256_SHA256_RSAPSS`. 

- **Security mode** — what is applied to each message: `None`, `Sign`, `SignAndEncrypt`.
- **User identity token** — `Anonymous`, `UserName` (username/password), `Certificate` (X.509).

The `Server(...)` constructor takes a certificate and private key that the server uses to identify itself; clients present certificates of their own that the server validates against the trust list. With both sides configured, the negotiated channel is encrypted end-to-end.

For the distillery, `Basic256Sha256` is the safe default: well-supported, audited, and built on RSA-2048 / SHA-256. The newer `Aes256_Sha256_RsaPss` is preferred where it is supported — RSA-PSS signatures and AES-256 session keys.

---

## Generate a self-signed certificate

`o6.util` ships a helper that creates a self-signed pair:

```python
from o6.util import createSelfSignedCertificate

srv_key, srv_cert = createSelfSignedCertificate(
    appUri="urn:example:distillery",
    commonName="DistilleryServer@localhost",
)
```

The return values are raw DER bytes. They can be passed directly to the `Server(...)` constructor or written to disk and loaded from a path:

```python
from pathlib import Path

Path("server_key.der").write_bytes(srv_key)
Path("server_cert.der").write_bytes(srv_cert)
```

The `applicationUri` must match the URI the server advertises. `Server(..., applicationUri="urn:example:distillery")` is the right knob when the certificate is generated separately — there is no separate setter method, the constructor keyword argument is the only way to set it.

---

## Configure encryption on the server

Pass the certificate and key to the `Server(...)` constructor, along with the trust list of clients to accept:

```python
import o6
from pathlib import Path
from o6.util import createSelfSignedCertificate

srv_key, srv_cert = createSelfSignedCertificate(
    appUri="urn:example:distillery",
    commonName="DistilleryServer@localhost",
)

# Load the client's certificate (issued out of band, or shared for local tests)
client_cert = Path("client_cert.der").read_bytes()

server = o6.Server(
    port=4840,
    certificate=srv_cert,
    privateKey=srv_key,
    trustList=[client_cert],
    applicationUri="urn:example:distillery",
)
```

With `certificate=` and `privateKey=` both set, the server enables the encrypting security policies for every cipher suite the build supports — typically `Basic256Sha256`, `Aes128_Sha256_RsaOaep`, and `Aes256_Sha256_RsaPss`. The trust list decides which client certificates are accepted during the secure-channel handshake.

!!! info
    Log lines such as `Could not add SecurityPolicy#EccNistP256_AesGcm with error code BadCertificateInvalid` on startup are expected with an RSA certificate: the elliptic-curve policies need an EC key and are skipped.

`acceptAllCertificates=True` accepts every client certificate without validation. It exists for development and interop testing, and it defeats the purpose of the trust list — do not ship it.

#### Putting it all together

```python
import time
from pathlib import Path

import o6
from o6.util import createSelfSignedCertificate

srv_key, srv_cert = createSelfSignedCertificate(
    appUri="urn:example:distillery",
    commonName="DistilleryServer@localhost",
)

server = o6.Server(
    port=4840,
    certificate=srv_cert,
    privateKey=srv_key,
    trustList=[Path("client_cert.der").read_bytes()],
    applicationUri="urn:example:distillery",
)

setpoint = server.addVariable("Setpoint", server.objectsNode, 85.0, nodeId="ns=1;i=1204")
server.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pass

server.stop()
```

A client connecting with a matching certificate and `SecurityMode.SIGN_AND_ENCRYPT` gets an encrypted session; clients without one still get the unencrypted `None` endpoint (because the server still advertises it for compatibility).

---

## `secureOnly`

`secureOnly=True` removes the `None` endpoint entirely. Clients have to negotiate a secure channel.

```python
server = o6.Server(
    port=4840,
    certificate=srv_cert,
    privateKey=srv_key,
    secureOnly=True,
)
```

!!! warning
    `secureOnly=True` removes the `None` endpoint entirely. In the current build no client can then connect — including a correctly configured secure `o6.Client` — because endpoint discovery is performed over the `None` endpoint before the secure channel is opened; every attempt fails with `BadSecurityPolicyRejected`. Leave `secureOnly` at its default and restrict access through [access control](410_access-control-auth.md) instead until this is resolved.

---

## What does a secure client look like?

The matching `o6.Client(...)` carries the same shape:

```python
from o6.util import createSelfSignedCertificate
from pathlib import Path
from o6 import Client, SecurityPolicy, SecurityMode

cli_key, cli_cert = createSelfSignedCertificate(
    appUri="urn:example:distillery-client",
    commonName="DistilleryClient@localhost",
)
Path("client_key.der").write_bytes(cli_key)
Path("client_cert.der").write_bytes(cli_cert)

client = Client(
    "opc.tcp://localhost:4840",
    certificate=cli_cert,
    privateKey=cli_key,
    trustList=[srv_cert],
    securityMode=SecurityMode.SIGN_AND_ENCRYPT,
    securityPolicy=SecurityPolicy.BASIC256SHA256,
    applicationUri="urn:example:distillery-client",
)
```

The same `applicationUri` must appear in both the certificate and the client constructor. The trust list contains the server's certificate, the security policy and mode are explicit, and the rest of the client API is unchanged.

#### Putting it all together

```python
from pathlib import Path

from o6 import Client, SecurityPolicy, SecurityMode
from o6.util import createSelfSignedCertificate

# Generate both sides for a local round-trip
srv_key, srv_cert = createSelfSignedCertificate(
    appUri="urn:example:distillery",
    commonName="DistilleryServer@localhost",
)
cli_key, cli_cert = createSelfSignedCertificate(
    appUri="urn:example:distillery-client",
    commonName="DistilleryClient@localhost",
)

Path("server_key.der").write_bytes(srv_key)
Path("server_cert.der").write_bytes(srv_cert)
Path("client_key.der").write_bytes(cli_key)
Path("client_cert.der").write_bytes(cli_cert)

client = Client(
    "opc.tcp://localhost:4840",
    certificate=cli_cert,
    privateKey=cli_key,
    trustList=[srv_cert],
    securityMode=SecurityMode.SIGN_AND_ENCRYPT,
    securityPolicy=SecurityPolicy.BASIC256SHA256,
    applicationUri="urn:example:distillery-client",
)

with client:
    print(client.read("ns=1;i=1204"))
```

The connection is end-to-end encrypted. The same `Client(...)` constructor accepts `username=` / `password=` for an additional user-identity layer on top of the channel authentication; see [the client security tutorial](../client/300_security.md) for the symmetric story.

---

## What's next?

The distillery now speaks encrypted channels, has a role-based access story, and authenticates sessions. The next pages cover the housekeeping parts of a real server: server-side monitored items, internal retention, and historical data.

- [Subscribe monitoring on the server side](430_server-monitoring.md) — what the server sees when a client subscribes, internal monitored items for housekeeping.
- [Server manual](../../manual/server/lifecycle.md#security) — every security-related keyword on `Server(...)`, including the issuer list, revocation list, and application URI.