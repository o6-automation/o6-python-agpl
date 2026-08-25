# Access control & roles

## Access control and authentication

`o6.AccessControl` maps to open62541's `UA_AccessControl` plugin. Subclass it
to authenticate sessions or restrict individual operations, then pass the
instance to `o6.Server`. Authorization callbacks receive an `o6.Session`
proxy. Its `context` is the object returned by `activateSession`; the proxy
also provides session attributes, assigned roles, and `close()`.

```python
import o6
from o6.ns import ns0

class PasswordAccessControl(o6.AccessControl):
    def __init__(self):
        super().__init__(anonymous=True, username=True)

    def activateSession(self, endpoint, remoteCertificate, session, userIdentityToken):
        if isinstance(userIdentityToken, ns0.datatypes.AnonymousIdentityToken):
            return {"username": None}
        if (
            isinstance(userIdentityToken, ns0.datatypes.UserNameIdentityToken)
            and userIdentityToken.userName == "user1"
            and userIdentityToken.password == b"password"
        ):
            return {"username": userIdentityToken.userName}
        raise o6.StatusCodeError(o6.StatusCode.BAD_USER_ACCESS_DENIED)

server = o6.Server(
    accessControl=PasswordAccessControl(),
    allowNonePolicyPassword=True,
)
```

!!! warning
    The hook names are lowerCamelCase — `activateSession`, `closeSession`,
    `allowBrowseNode`, and so on. A method named `activate_session` does not
    override anything: it is never called, the permissive/anonymous-only base
    implementation runs instead, and nothing warns you. If authentication seems
    to be ignored, check the spelling first. (Older *parameter* names such as
    `session_id` are still adapted automatically; only the method name matters.)

Rejecting a session is `raise o6.StatusCodeError(...)`; the client sees the
status code from its `connect()` call. Returning normally accepts it, and
whatever you return becomes `session.context`.

The remaining hooks are authorization rather than authentication, and all have
permissive defaults: `closeSession`, `getUserRightsMask`, `getUserAccessLevel`,
`getUserExecutable`, `getUserExecutableOnObject`, `allowAddNode`,
`allowAddReference`, `allowDeleteNode`, `allowDeleteReference`,
`allowBrowseNode`, `allowCreateSubscription`, `allowTransferSubscription`,
`allowHistoryUpdate`, and `allowHistoryDelete`.

`allowNonePolicyPassword` is deliberately separate from access control. It
permits password tokens on an unencrypted endpoint and should normally only be
enabled for local tests. Access control and this transport setting cannot be
replaced after the server starts.

Inherited authorization hooks use native C defaults. Only hooks overridden by
the concrete subclass cross into Python, so a plugin that overrides only
`activateSession` and `closeSession` does not acquire the GIL for routine
reads, writes, browses, or method calls.

Access-control subclasses using the earlier `(session_id, session_context, ...)`
hook signatures continue to work. New code should use the `Session` form.

### The Session proxy

`Session` is a resolving proxy rather than a retained native pointer. Every
operation validates its NodeId against the server, so using it after the remote
session closes raises `BadSessionIdInvalid` safely.

```python
session.id                     # NodeId of the session
session.context                # whatever activateSession returned
session.set("shift", "night")  # server-side session attributes
session.get("shift")
session.delete("shift")        # a later get() raises BadNotFound
session.roles                  # tuple[Role, ...]
session.roles = (o6.roles.engineer,)
session.close()                # terminate the session
```

Attribute keys are `QualifiedName` values or plain strings, which are promoted
to namespace 0. Note that closing a session does not lock the client out — a
client with automatic reconnection simply activates a new one.

## Role-based access control

Permissions are `PermissionType` flags and may be combined with `|`. The
well-known OPC UA roles are available from `o6.roles`. Node permissions live
behind the `_permissions` member of a node handle:

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
    handle carries one, because unprefixed attribute access is reserved for
    browsing to child nodes by BrowseName. Assigning to `node.permissions`
    silently creates an ordinary Python attribute and changes no permissions at
    all.

The object behind `_permissions` supports the full set of operations, each of
which also takes `recursive=True` to apply to the whole subtree:

```python
temperature._permissions.get()                                    # dict[Role, PermissionType]
temperature._permissions.set({o6.roles.observer: PermissionType.BROWSE})
temperature._permissions.grant(role, PermissionType.READ, overwrite=False)
temperature._permissions.revoke(role, PermissionType.WRITE)
temperature._permissions.clear()
```

Roles can be registered and resolved through `server.roles`:

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

`add` returns the role as the server stored it, with its assigned NodeId filled
in. `server.roles[key]` looks a role up by `NodeId`, `QualifiedName`, or plain
name; `server.roles.update(role)` and `server.roles.remove(role)` modify the
registry; and iterating `server.roles` yields every role, including the
standard ones the server creates itself.

Namespace defaults apply when a node has no explicit role permissions:

```python
server.ns.set_default_permissions(
    "urn:example:machines",
    {o6.roles.observer: PermissionType.BROWSE | PermissionType.READ},
)
server.ns.get_default_permissions("urn:example:machines")
```

The namespace may be given as a URI or as a numeric index.

Anonymous sessions remain permissive for compatibility. Enable RBAC checks for
them explicitly:

```python
server = o6.Server(rbacForAnonymous=True)
```

Authentication may explicitly assign roles. Assignment is applied immediately
after activation, after the server has evaluated the role identity mappings.

```python
def activateSession(self, endpoint, remoteCertificate, session, userIdentityToken):
    user = authenticate(userIdentityToken)
    return o6.SessionActivation(context=user, roles=(maintenance,))
```
