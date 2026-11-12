# Access control — authentication

Require a login to the tutorial distillery and assign a role to each user.
The `hmi` user will read `Setpoint`; `control` will read and write it.
This builds on [Access control — roles](400_access-control-roles.md).

## Assign roles from `activateSession`

Add these imports and the plugin class to the tutorial server from
[Set the Stage](../setup.md), before `main()`:

```python
import o6
from o6.ns import ns0
from o6.ns.ns0.datatypes import PermissionType


class DistilleryAccessControl(o6.AccessControl):
    def __init__(self):
        super().__init__(anonymous=False, username=True)

    def activateSession(self, endpoint, remoteCertificate, session, userIdentityToken):
        if not isinstance(userIdentityToken, ns0.datatypes.UserNameIdentityToken):
            raise o6.StatusCodeError(o6.StatusCode.BAD_USER_ACCESS_DENIED)

        accounts = {
            "hmi": (b"dashboard", o6.roles.observer),
            "control": (b"operator", o6.roles.engineer),
        }
        password, role = accounts.get(userIdentityToken.userName, (None, None))
        if password is None or bytes(userIdentityToken.password) != password:
            raise o6.StatusCodeError(o6.StatusCode.BAD_USER_ACCESS_DENIED)
        return o6.SessionActivation(
            context={"username": userIdentityToken.userName},
            roles=(o6.roles.authenticated_user, role),
        )
```

`anonymous=False` removes the anonymous token policy. `activateSession` checks
the password and returns the user's context and roles. Raising
`StatusCodeError` rejects the login. Role names do not grant permissions by
themselves; the next step configures the node's grants.

## Configure the tutorial server

Replace the server construction and `build_address_space(server)` call in
`main()` with this fragment. Keep the existing simulation and server lifetime:

```python
server = o6.Server(
    port=args.port,
    accessControl=DistilleryAccessControl(),
    allowNonePolicyPassword=True,
)
vars = build_address_space(server)
setpoint = server["ns=1;i=1204"]
setpoint._permissions = {
    o6.roles.observer: PermissionType.BROWSE | PermissionType.READ,
    o6.roles.engineer: PermissionType.BROWSE | PermissionType.READ | PermissionType.WRITE,
}
```

!!! warning
    This local exercise uses fixed demo passwords and sends them without
    encryption. Run it only on a trusted development network. Configure
    [encrypted endpoints](420_security-policies.md) before deployment and
    leave `allowNonePolicyPassword=False` on both peers.

Restart the tutorial server. The inherited authorization hooks enforce the
`Setpoint` grants. Other nodes remain permissive because this exercise sets
permissions only on `Setpoint`.

## Check the two roles

Run this client against the modified tutorial server:

```python
import o6

for username, password in (("hmi", "dashboard"), ("control", "operator")):
    with o6.Client(
        "opc.tcp://localhost:4840",
        username=username,
        password=password,
        allowNonePolicyPassword=True,
    ) as client:
        value = client.read("ns=1;i=1204")
        status = client.write("ns=1;i=1204", value)
        print(username, status == o6.StatusCode.GOOD)
```

Expected output, apart from logs:

```text
hmi False
control True
```

The HMI write returns `BadUserAccessDenied`; the control write succeeds.
A wrong password makes `connect()` raise `StatusCodeError`. Correct the
credentials before retrying. If an authentication hook is not called, check
its lowerCamelCase name: it must be `activateSession`.

For additional authorization checks, override the relevant hook and call
`super()` to retain role-permission checks. The
[server manual](../../manual/server/security.md#access-control-and-authentication)
covers hook behavior and session inspection.

## Next steps

| Topic | What it covers |
|---|---|
| [Security policies and endpoints](420_security-policies.md) | Encrypt connections and configure certificate trust. |
| [Access Control & Roles](../../manual/server/security.md) | Authentication hooks, session roles, default-deny behavior and access restrictions. |
