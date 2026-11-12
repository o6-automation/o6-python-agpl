# Security policies and endpoints

Encrypt client connections to the tutorial distillery with certificates trusted
by both peers. This builds on
[Access control — authentication](410_access-control-auth.md): keep that page's
`DistilleryAccessControl` class and `Setpoint` grants.

## Generate certificates for the local exercise

Run this once in the directory from which you will start the server and client.
It writes a key and certificate for each application:

```python
from pathlib import Path
from o6.util import createSelfSignedCertificate

for name in ("server", "client"):
    key, certificate = createSelfSignedCertificate(
        appUri=f"urn:example:distillery-{name}",
        commonName=f"Distillery-{name}@localhost",
    )
    Path(f"{name}_key.der").write_bytes(key)
    Path(f"{name}_cert.der").write_bytes(certificate)
```

Each application keeps its private key. Exchange only public certificates.
The application URI in each configuration must match its certificate.
In a deployment, use persistent certificates managed by your organization.

## Configure the server

Add `from pathlib import Path` to the tutorial server. Replace its server
construction in `main()` with this fragment:

```python
server = o6.Server(
    port=args.port,
    certificate=Path("server_cert.der"),
    privateKey=Path("server_key.der"),
    trustList=[Path("client_cert.der")],
    applicationUri="urn:example:distillery-server",
    accessControl=DistilleryAccessControl(),
)
```

At the start of `DistilleryAccessControl.activateSession`, require encryption
before checking the user token:

```python
if endpoint.securityMode != o6.SecurityMode.SIGN_AND_ENCRYPT:
    raise o6.StatusCodeError(o6.StatusCode.BAD_SECURITY_MODE_INSUFFICIENT)
```

Keep the rest of the authentication method, address-space construction and
permission grants from the previous page. Restart the server after applying
the changes.

With these RSA certificates, the server advertises `Basic256Sha256`,
`Aes128_Sha256_RsaOaep` and `Aes256_Sha256_RsaPss` with `Sign` and
`SignAndEncrypt` modes. The access-control check requires `SignAndEncrypt`
for application Sessions. The `None` endpoint remains available for discovery.

An empty `trustList` rejects every client certificate. If connection setup
fails with `BadSecurityChecksFailed`, check the server log for the rejected
certificate and verify that it matches `client_cert.der`. See
[Rejected certificates](../../manual/server/lifecycle.md#rejected-certificates)
for inspection and callback options.

## Connect with encryption

Run this client from the directory containing the certificates:

```python
from pathlib import Path
import o6

with o6.Client(
    "opc.tcp://localhost:4840",
    certificate=Path("client_cert.der"),
    privateKey=Path("client_key.der"),
    trustList=[Path("server_cert.der")],
    applicationUri="urn:example:distillery-client",
    securityMode=o6.SecurityMode.SIGN_AND_ENCRYPT,
    securityPolicy=o6.SecurityPolicy.BASIC256SHA256,
    username="control",
    password="operator",
) as client:
    value = client.read("ns=1;i=1204")
    print(client.write("ns=1;i=1204", value) == o6.StatusCode.GOOD)
```

The client prints `True`: the channel is encrypted, both peers trust the
application certificates, and the Engineer role may write `Setpoint`.
Try `username="hmi", password="dashboard"`; the write is denied and the
client prints `False`.

Leave `acceptAllCertificates` and `allowNonePolicyPassword` at their default
`False`. Certificate trust identifies the applications; the password identifies
the user, and role permissions control node access.

## Discovery and `secureOnly`

`secureOnly=True` removes the `None` endpoint. Ordinary client discovery then
fails with `BadSecurityPolicyRejected`, even if the requested session mode is
secure. Keep the default `False` for this tutorial; the authentication hook
already requires encrypted Sessions. Clients using a trusted, preconfigured
endpoint can skip that discovery step. See
[Server security configuration](../../manual/server/lifecycle.md#security)
for this option and certificate-policy details.

## Next steps

| Topic | What it covers |
|---|---|
| [Subscribe monitoring on the server side](430_server-monitoring.md) | Observe client subscriptions and configure local monitored items. |
| [Lifecycle & Configuration](../../manual/server/lifecycle.md#security) | Certificate trust, supported policies and discovery options. |
