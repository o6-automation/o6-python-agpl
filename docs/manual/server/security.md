# Access Control & Roles

Use access control to authenticate users and limit the nodes and operations
each user can access. Configure it alongside certificate trust and message
protection:

| Layer | Configuration and purpose |
|---|---|
| Application identity and trust | `certificate`, `privateKey`, `applicationUri` and `trustList` identify and validate the applications on a secured channel. See [Server security configuration](lifecycle.md#security) for trust lists and rejected certificates. |
| Message protection | The client's `securityPolicy` and `securityMode` select an endpoint offered by the server. `SIGN` detects tampering; `SIGN_AND_ENCRYPT` also protects message contents. |
| User authentication | `AccessControl.activateSession` accepts or rejects the user identity token. A trusted application certificate does not select the user's permissions. |
| Authorization | Session roles, node permissions and access-control hooks determine which operations that user may perform. |

Default servers permit anonymous access, and nodes without permission rules
are permissive. Configure permissions for the Anonymous role if anonymous
users need restricted access. To require a login, omit the anonymous token
policy from your access-control plugin and reject tokens you do not
authenticate. The authorization hooks a custom plugin inherits enforce the
same role permissions as the default plugin.

Use [role permissions](#role-based-access-control) to restrict operations,
including access by anonymous users.

## GDS PushManagement

Use GDS PushManagement to let a certificate manager update a running server's
application certificate and trust lists. A *Global Discovery Server* (GDS) can
provide that management service. o6\\Python receives updates; it does not provide
a certificate authority (CA), GDS directory, pull management or a pushing-client
API. See the [receiving-server example](../../examples/advanced_applications-gds_push-server.md)
for a complete setup. Interoperability with external GDS products is unverified.

!!! info "Platform support"
    GDS PushManagement is supported on Linux and Windows only.
    Enabling it on macOS raises `NotImplementedError`.

[`server.enablePushManagement()`](../../api_reference/server.md#o6.server.Server.enablePushManagement)
enables the standard `ServerConfiguration` management methods.
Call it after configuring the server certificate, private key,
encrypted security policies and authentication, and before `start()`. Enabling it
more than once or during startup, operation or shutdown raises
`StatusCodeError`. Encryption and filestore configuration cannot be reset after
enabling PushManagement, even after stopping the server. Configure them before
attachment; create a new server instance to change them afterwards. Builds without
PushManagement support raise `NotImplementedError`.

Enabling PushManagement sets SecurityAdmin permissions on the standard
`ServerConfiguration` management methods. It preserves the anonymous
permission fallback. Grant SecurityAdmin only to the authenticated management
identity, for example by returning
`o6.SessionActivation(context=token.userName, roles=(o6.roles.security_admin,))`
after verifying that user's password in `activateSession`. The
`allowBrowseNode`, `getUserExecutable` and `getUserExecutableOnObject`
implementations that custom Python access-control plugins inherit check these
role permissions, so the management methods need SecurityAdmin there too. On
nodes without permission rules they allow browsing and calls; override them to
restrict those nodes as well. The example rejects all non-administrator
sessions and checks the administrator identity and role in each of these
hooks.

Require `SignAndEncrypt` in your application's `activateSession` callback to
protect management requests. The example rejects weaker sessions with
`BadSecurityModeInsufficient`. Management methods also accept `None` and `Sign`
sessions when your `AccessControl` permits them. See
[SecureChannels](../opcua-fundamentals/protocol.md#securechannel) for message
protection and [Sessions](../opcua-fundamentals/protocol.md#session) for user authentication.
Calls made locally through `server` run as the local administrator and do not
require a network connection.

Configure persistent storage separately before enabling PushManagement.
In-memory updates are lost on process restart. Application certificate operations
support `DefaultApplicationGroup` (`i=14156`, also selected by a null NodeId).
Read its `CertificateTypes` property (`i=14161`) for the configured types:
`RsaSha256ApplicationCertificateType` (`i=12560`) and, when legacy RSA policies
are configured, `RsaMinApplicationCertificateType` (`i=12559`). Updates affect
policies of the selected type. Unsupported types and groups return
`BadInvalidArgument`; ECC application certificate updates are not supported.

### Renewing the application certificate

Use a connected management client authenticated as SecurityAdmin over
`SignAndEncrypt`. The following fragments use synchronous `o6.Client.call`;
in an asyncio application, await each call. A Call service failure raises
`StatusCodeError`, but a method failure is returned as the first tuple element
and must be checked separately.

Request a DER-encoded PKCS #10 *certificate signing request* (CSR) with the
current key.

!!! warning "Regenerated keys are not saved"
    `CreateSigningRequest` with `RegeneratePrivateKey=True` works for an in-memory
    renewal, but its key is not saved by the filestore. Replacing that pending
    CSR with a retained-key request can crash the server, including after a
    stop/start cycle. Use retained-key renewal or supply a new key explicitly
    when updates must survive a process restart.

```python
result = manager.call(
    "i=12637", "i=12737",
    [o6.NodeId(), o6.NodeId(12560), "", False, b""],
)
if result[0] != o6.StatusCode.GOOD:
    raise o6.StatusCodeError(result[0])
csr_der = result[1]
```

Have your CA sign `csr_der`, preserving the server's application URI, hostnames
and certificate usages. `signed_certificate_der` below is the resulting leaf
certificate and `issuer_certificate_der` is the CA certificate. Keep the same
management session for staging and applying the update:

```python
result = manager.call(
    "i=12637", "i=13737",
    [o6.NodeId(), o6.NodeId(12560), signed_certificate_der,
     [issuer_certificate_der], "", b""],
)
if result[0] != o6.StatusCode.GOOD:
    raise o6.StatusCodeError(result[0])
if result[1]:  # ApplyChangesRequired
    status = manager.call("i=12637", "i=12740")[0]
    if status != o6.StatusCode.GOOD:
        raise o6.StatusCodeError(status)
```

The empty private key selects the retained key. To supply a replacement key
explicitly, pass `"PKCS8"` (DER-encoded PKCS#8) or `"PEM"` and its encoded bytes in the last two arguments.
Malformed certificates and mismatched supplied keys return error status codes.
Verify that a keyless replacement matches the requested CSR before submitting it.
The server does not reliably reject an unrelated certificate when a
regenerated CSR key is pending.

`UpdateCertificate` stages the replacement. `ApplyChanges` installs it and sends
its method result before closing certificate-related channels. Configure the
client to trust the replacement and its issuer chain, then reconnect. The
server accepts the `IssuerCertificates` argument but does not install
those certificates; provision required trust and issuers separately through
TrustList management. Do not infer trust installation from a successful update.

With the [PKI filestore](#pki-filestore-configuration), updated certificates are
saved under `ApplCerts/own/certs`. Explicitly supplied keys are saved under
`ApplCerts/own/private`, using the certificate-derived
basename and a `.key` suffix. Retained-key renewal with an empty key does not
write another key file: retain the original key securely. Protect the store
permissions before starting the server.

For a fresh server instance, pass the chosen saved certificate and its matching
key bytes to `setDefaultWithFilestore`. For retained-key renewal, use the saved
replacement certificate and original key. For an explicitly supplied replacement
key, use its saved `.key` file or the original securely held copy. Identify files
by the certificate you installed; old files can remain in the store. Supplying the
original credentials starts the original identity even when replacements are
present. No file is chosen automatically.

!!! warning "An update failure can leave partial changes"
    Certificate updates are not atomic across security policies and files.
    A policy can adopt the replacement in memory before a disk write fails,
    and the certificate file can exist without its key. Some storage failures
    are not reported by `ApplyChanges`, and retries can skip a missing key when
    the certificate already exists. Verify the endpoint identity and saved
    certificate/key pair even after a successful method result. Recover using
    explicitly known matching credentials; do not rely on retry to repair the
    store. Crash recovery and rollback across files are not guaranteed.

### Updating trust lists

The receiver manages `DefaultApplicationGroup/TrustList` (`i=12642`) and
`DefaultUserTokenGroup/TrustList` (`i=14123`). Use `OpenWithMasks`, chunked `Read`
and `Close` to inspect lists. The memory and file stores return their
complete stored TrustList payload, including its `SpecifiedLists`, even when a
subset is requested. Select the desired fields on the client.

For writes, encode `TrustListDataType` with the appropriate `SpecifiedLists` mask,
call `Open` with `Write | EraseExisting`, send chunks using `Write`, and call
`CloseAndUpdate`. If its `ApplyChangesRequired` result is `True`, call
`ApplyChanges` in the owning session.
`Close` discards a pending write. Abandoned sessions release their transactions
on the server's session-cleanup interval; transport loss alone is not session expiry.

`AddCertificate` immediately adds a trusted non-CA certificate; use binary
TrustList transfers for CAs, issuers and certificate revocation lists (CRLs).
`RemoveCertificate` applies immediately, but removing an issuer CA can leave its
CRLs behind. Use a complete TrustList transfer to update issuer certificates and
CRLs together. Neither
single-certificate method needs a further `ApplyChanges`. Application trust changes
revalidate SecureChannels, so retain the manager's trust while making changes.
User-token trust changes affect new certificate-authenticated sessions, without
revalidating tokens of existing sessions. Filestore retry support does not
guarantee crash atomicity or rollback across multiple directories on I/O failure.

### Stopping and restarting

Finish or discard management operations and close TrustList handles before
stopping the server. Allow expired-session cleanup to run while the server is
running. Stopping completes queued `ApplyChanges` operations and related channel
closures, but pending transactions and open handles can survive.

Starting the same instance retains its applied credentials and trust lists.
Do not call `enablePushManagement()` again. Create a new server instance if
pending management state cannot be cleared. For a new instance, select its
startup credentials as described under [certificate renewal](#renewing-the-application-certificate).

## A secured client/server pair

This complete local example accepts encrypted username/password sessions and
assigns read-only or read/write access to one Variable. It generates temporary
self-signed certificates and uses two fixed demo passwords. In an application,
load persistent certificates and authenticate against your user store.
Only public certificates are exchanged through trust lists; keep private keys
with their owning application.

```python
import o6
from o6.ns import ns0
from o6.ns.ns0.datatypes import PermissionType
from o6.util import createSelfSignedCertificate

server_key, server_cert = createSelfSignedCertificate(
    appUri="urn:example:server", commonName="ExampleServer@localhost",
)
client_key, client_cert = createSelfSignedCertificate(
    appUri="urn:example:client", commonName="ExampleClient@localhost",
)

class PasswordAccessControl(o6.AccessControl):
    def __init__(self):
        super().__init__(anonymous=False, username=True)

    def activateSession(self, endpoint, remoteCertificate, session, userIdentityToken):
        if endpoint.securityMode != o6.SecurityMode.SIGN_AND_ENCRYPT:
            raise o6.StatusCodeError(o6.StatusCode.BAD_SECURITY_MODE_INSUFFICIENT)
        if not isinstance(userIdentityToken, ns0.datatypes.UserNameIdentityToken):
            raise o6.StatusCodeError(o6.StatusCode.BAD_USER_ACCESS_DENIED)

        accounts = {
            "viewer": (b"viewer-demo", o6.roles.observer),
            "operator": (b"operator-demo", o6.roles.operator),
        }
        password, role = accounts.get(userIdentityToken.userName, (None, None))
        if password is None or userIdentityToken.password != password:
            raise o6.StatusCodeError(o6.StatusCode.BAD_USER_ACCESS_DENIED)
        return o6.SessionActivation(context=userIdentityToken.userName, roles=(role,))

server = o6.Server(
    certificate=server_cert,
    privateKey=server_key,
    trustList=[client_cert],
    applicationUri="urn:example:server",
    accessControl=PasswordAccessControl(),
)
temperature = server.addVariable("Temperature", server.objects, 22.5)
temperature._permissions = {
    o6.roles.observer: PermissionType.BROWSE | PermissionType.READ,
    o6.roles.operator: PermissionType.BROWSE | PermissionType.READ | PermissionType.WRITE,
}

with server:
    for username in ("viewer", "operator"):
        with o6.Client(
            "opc.tcp://localhost:4840",
            certificate=client_cert,
            privateKey=client_key,
            trustList=[server_cert],
            applicationUri="urn:example:client",
            securityMode=o6.SecurityMode.SIGN_AND_ENCRYPT,
            securityPolicy=o6.SecurityPolicy.BASIC256SHA256,
            username=username,
            password=username + "-demo",
        ) as client:
            remote_temperature = client.objects.temperature
            print(username, remote_temperature())
            try:
                remote_temperature(23.5)
                print("write accepted")
            except o6.StatusCodeError as error:
                if error.code != o6.StatusCode.BAD_USER_ACCESS_DENIED:
                    raise
                print("write denied")
```

Expected output, apart from server logs:

```text
viewer 22.5
write denied
operator 22.5
write accepted
```

The application URIs match those in the certificates. Each side trusts the
other's certificate; `acceptAllCertificates` and `allowNonePolicyPassword`
remain `False`. The access-control plugin requires `SIGN_AND_ENCRYPT` for
Session activation, then authenticates the user and assigns a role.
The inherited authorization hooks apply `temperature._permissions`: both
roles can read the value, and only the Operator role can write it.

The server retains a `None` endpoint for discovery. It does not accept an
application Session on that endpoint because the plugin rejects its mode.
Discovery traffic remains unencrypted. This is different from removing the
endpoint entirely with [`secureOnly=True`](lifecycle.md#security).

## Access control and authentication

Subclass `o6.AccessControl` to authenticate sessions or restrict individual
operations, then pass the instance to `o6.Server`, as above. Its `anonymous`
and `username` constructor flags advertise token types; `activateSession`
performs the actual authentication. A `UserTokenPolicy` describes the token
format and its cryptographic protection, not a user's node permissions.

Authorization callbacks receive an `o6.Session` proxy. Its `context` is the
object returned by `activateSession` (or `SessionActivation.context`); the
proxy also provides session attributes, assigned roles, the session's
effective permissions on a node, and `close()`.

!!! warning
    Hook names are lowerCamelCase: `activateSession`, `closeSession`,
    `allowBrowseNode` and so on. A method named `activate_session` overrides
    nothing. It is never called, the anonymous-only base implementation runs
    instead, and nothing warns you. If authentication seems ignored, check the
    spelling first.

To reject a session, `raise o6.StatusCodeError(...)`. The client gets that
status code from `connect()`. Returning normally accepts the session, and the
return value becomes `session.context`.

Inherited authorization hooks enforce [role permissions](#role-based-access-control).
When an override adds a restriction, return the corresponding `super()` result
after checking it. Returning an independent result replaces the role check
for that operation.

`allowCreateSubscription` permits every session by default.
`allowTransferSubscription` permits transfers between sessions of the same user.
Anonymous sessions require an encrypting SecurityPolicy and the same client
ApplicationUri. When the original session has closed, open62541 checks the saved
subscription owner before calling this hook with a null `oldSession.id`. The base
implementation permits that transfer; an override can still reject it.
`closeSession` is a cleanup callback; it does not authorize closing a session.
See [`AccessControl`](../../api_reference/accesscontrol.md) for hook contracts.

Configure access control before starting the server. Password-token encryption
is configured separately through
[`allowNonePolicyPassword`](lifecycle.md#security).

### The Session proxy

Use `Session` to inspect the requesting user, store application context, or
change assigned roles. Using it after the remote session closes raises
`StatusCodeError` with `BadSessionIdInvalid`.

```python
session.id                     # NodeId of the session
session.context                # whatever activateSession returned
session.set("shift", "night")  # server-side session attributes
session.get("shift")
session.delete("shift")        # a later get() raises BadNotFound
session.roles                  # tuple[Role, ...]
session.roles = (o6.roles.engineer,)
session.effectivePermissions(temperature)  # PermissionType of this session
session.close()                # terminate the session
```

Attribute keys are `QualifiedName` values or plain strings. Plain strings are
promoted to namespace 0. Closing a session does not lock the client out: a
client with automatic reconnection activates a new one.

## Role-based access control

The default server access-control plugin evaluates node and namespace role
permissions, including permissions for anonymous sessions. A custom
`AccessControl` applies the same checks through its inherited authorization
hooks. `session.effectivePermissions(nodeId)` returns the combined permissions
of the session's roles; it does not include access restrictions or custom hook
results. Assigning a role alone does not restrict a node without permission
rules.

Permissions are `PermissionType` flags; combine them with `|`. `o6.roles`
provides the well-known OPC UA roles. A node handle's `_permissions` member holds
its permissions. These fragments assume an existing `temperature` Variable:

```python
from o6.ns.ns0.datatypes import PermissionType

temperature._permissions = {
    o6.roles.observer: PermissionType.BROWSE | PermissionType.READ,
    o6.roles.operator: (
        PermissionType.BROWSE
        | PermissionType.READ
        | PermissionType.WRITE
    ),
}

temperature._permissions.grant(
    o6.roles.engineer,
    PermissionType.READ | PermissionType.WRITE,
    recursive=True,
)
```

!!! warning
    The leading underscore is part of the name. Every public helper on a node
    handle has one, because unprefixed attribute access browses to child nodes
    by BrowseName. Assigning to `node.permissions` silently creates an ordinary
    Python attribute and changes no permissions.

`_permissions` supports these operations. Each takes `recursive=True` to apply
to the whole subtree:

```python
temperature._permissions.get()                                    # dict[Role, PermissionType]
temperature._permissions.set({o6.roles.observer: PermissionType.BROWSE})
temperature._permissions.grant(role, PermissionType.READ, overwrite=False)
temperature._permissions.revoke(role, PermissionType.WRITE)
temperature._permissions.clear()
```

Register and look up roles through `server.roles`:

```python
maintenance = server.roles.add(
    o6.Role(
        "Maintenance",
        identities=(
            ns0.datatypes.IdentityMappingRuleType(
                criteriaType=ns0.datatypes.IdentityCriteriaType.USER_NAME,
                criteria="maintainer",
            ),
        ),
    )
)
```

- `add` returns the role as stored, with its assigned NodeId filled in.
- `server.roles[key]` looks a role up by `NodeId`, `QualifiedName` or plain name.
- `server.roles.update(role)` and `server.roles.remove(role)` modify the registry.
- Iterating `server.roles` yields every role, including the standard roles the
  server creates.

Namespace defaults apply when a node has no explicit role permissions:

```python
server.ns.set_default_permissions(
    "urn:example:machines",
    {o6.roles.observer: PermissionType.BROWSE | PermissionType.READ},
)
server.ns.get_default_permissions("urn:example:machines")
```

Pass the namespace as a URI or a numeric index. If neither the node nor its
namespace has permission rules, access is permissive by default.

### Deny access without permission rules

Set `rbacForAnonymous=True` on `Server` to deny operations on nodes without
node or namespace permission rules. The default is `False`. The setting
applies to every session role and remains in effect with encryption enabled.

With this setting, namespace 0 grants `BROWSE | READ` to Anonymous and
AuthenticatedUser so clients can read NamespaceArray and ServerStatus during
connection setup. If `SessionActivation.roles` replaces the session's roles,
include `o6.roles.authenticated_user` to retain those grants, or configure
namespace 0 with `server.ns.set_default_permissions(0, ...)`.

Nodes created without a NodeId belong to the server's application namespace,
index 1. They need explicit node or namespace grants when default-deny is
enabled.

Authentication can assign roles explicitly. The assignment is applied right
after activation, after the server evaluates the role identity mappings.

```python
def activateSession(self, endpoint, remoteCertificate, session, userIdentityToken):
    user = authenticate(userIdentityToken)
    return o6.SessionActivation(context=user, roles=(maintenance,))
```

## Access restrictions

Use `accessRestrictions` to require signing or encryption for a node,
regardless of the user's role. The following fragment assumes an existing
`server`. Pass `AccessRestrictionType` flags when declaring or creating the
node:

```python
from o6.ns import ns0
from o6.ns.ns0.datatypes import AccessLevelType, AccessRestrictionType

recipe = ns0.vartypes.BaseDataVariableType(
    server=server,
    parent=server.objects,
    nodeId="ns=1;s=Recipe",
    browseName="1:Recipe",
    value="secret",
    accessLevel=AccessLevelType.CURRENT_READ | AccessLevelType.CURRENT_WRITE,
    accessRestrictions=AccessRestrictionType.ENCRYPTION_REQUIRED,
)
```

The decorators and declarations that take `rolePermissions` take
`accessRestrictions` too. The server checks the security mode of the
session's SecureChannel:

| Bit | The node needs |
|---|---|
| `SIGNING_REQUIRED` | A `SIGN` or `SIGN_AND_ENCRYPT` channel |
| `ENCRYPTION_REQUIRED` | A `SIGN_AND_ENCRYPT` channel |
| `SESSION_REQUIRED` | A Session; node operations already require one |
| `APPLY_RESTRICTIONS_TO_BROWSE` | Apply signing and encryption requirements to Browse too |

If the channel does not meet the requirements, Read, Write and Call fail with
`BadUserAccessDenied`. Connect with the required security mode and a matching
policy to access the node. A Method call checks both the Method and its Object.
Attribute writes, history access and node or reference changes are also denied.
Browse is restricted only when `APPLY_RESTRICTIONS_TO_BROWSE` is set.

Restrictions apply with the default access control and custom `AccessControl`
subclasses, including hooks that grant access independently of role permissions.
Local server operations are unrestricted.

The following limitations apply:

- Reading or writing the AccessRestrictions Attribute fails with
  `BadAttributeIdInvalid`. Set restrictions when declaring or creating nodes;
  clients cannot inspect them through the Attribute.
- Children created automatically from a type's InstanceDeclarations do not
  inherit their access restrictions or role permissions.
- A restricted node can appear in its parent's browse results. Browse checks
  apply to the node being browsed.
- Events are not filtered by their source node's access restrictions.
- NamespaceMetadata's `DefaultAccessRestrictions` does not set defaults.

## Local server operations

Calls through `server` or its local node handles run as the server's local
administrator. They do not test a remote user's role permissions. For example,
`temperature(23.5)` in the server application can write even when a viewer's
`remote_temperature(23.5)` is denied. Check permissions through a connected
client using the identity whose access you want to verify.

### PKI filestore configuration

On Linux and Windows, configure persistent certificates and trust lists before startup:

```python
server.config.setDefaultWithFilestore(certificate_bytes, private_key_bytes, str(pki_root), port=4840)
server.config.applicationUri = "urn:example:server"
# Configure authentication and custom limits here, before startup.
# Enable PushManagement afterwards if required.
```

Credentials must be DER or PEM `bytes`; `storePath` is a nonempty `str` and
`port` defaults to 4840 (range 0–65535). This method resets server settings,
security policies and access control. Call it on a fully stopped server, before
setting application identity, authentication and custom limits, and before
enabling PushManagement. It creates a fresh store when needed and loads trust on
each setup.
The explicit certificate/key determine startup identity even when the store
contains other saved credentials. There is no automatic credential selection or
merging of constructor trust lists.

Under the PKI root, both `ApplCerts` and `UserTokenCerts` contain
`trusted/certs`, `trusted/crl`, `issuer/certs`, `issuer/crl`, `own/certs`,
`own/private`, and `rejected/certs`. Manually provision trusted management-client
certificates before configuring the server. Issuer certificates and trusted and
issuer CRLs also reload from these directories. Configure session
certificate authentication after setup to use the user-token trust group.

Private-key files are written using the OS's default file creation permissions.
On Linux, provision a protected directory and a restrictive umask (for example,
`077`) before starting the process. On Windows, restrict the directory ACL to
the service account and required administrators. This method does not change
process-global permissions or log private material. Filesystem failures raise
`StatusCodeError`; setup can leave partial configuration, so correct the
failure and configure again before startup. macOS and builds without filestore
support raise `NotImplementedError`.
