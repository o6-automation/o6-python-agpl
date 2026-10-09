# Access control — authentication

The [roles page](400_access-control-roles.md) explained how to grant permissions to a node by role. This page is about *how a session ends up with a role* — the authentication hooks that map a client identity to a server-side role.

By the end, the distillery rejects anonymous clients and accepts two named users — `hmi` and `control` — with role assignments that match what each client is allowed to do.

---

## The shape of an access control plugin

`o6.AccessControl` is the base class for the server-side authentication plugin. Subclass it and override the hooks for the identity flows you want to support:

```python
import o6
from o6.ns import ns0


class DistilleryAccessControl(o6.AccessControl):
    """Accept the distillery's two users; reject anonymous."""

    def __init__(self):
        super().__init__(anonymous=False, username=True)

    def activateSession(
        self,
        endpoint,
        remoteCertificate,
        session,
        userIdentityToken,
    ):
        if isinstance(userIdentityToken, ns0.datatypes.UserNameIdentityToken):
            user = userIdentityToken.userName
            pwd = bytes(userIdentityToken.password)
            if user == "hmi" and pwd == b"dashboard":
                return {"username": user, "role": "hmi"}
            if user == "control" and pwd == b"operator":
                return {"username": user, "role": "control"}
            raise o6.StatusCodeError(o6.StatusCode.BAD_USER_ACCESS_DENIED)
        raise o6.StatusCodeError(o6.StatusCode.BAD_USER_ACCESS_DENIED)


server = o6.Server(
    port=4840,
    accessControl=DistilleryAccessControl(),
)
```

`__init__(anonymous=..., username=...)` declares the identity-token types the server will advertise. `anonymous=False` removes the anonymous token policy — clients have to present a username and password.

`activateSession(...)` is called once per session. The server hands the hook the endpoint description, the remote certificate (or `None` for a None-policy endpoint), a `Session` proxy, and the user identity token. Returning a dict stores the dict as `session.context`; raising `StatusCodeError(BAD_...)` rejects the activation.

!!! warning
    The hook names are lowerCamelCase — `activateSession`, `closeSession`, `allowBrowseNode`, and so on. A method named `activate_session` does not override anything: it is never called, the permissive/anonymous-only base implementation runs instead, and nothing warns you. If authentication seems to be ignored, check the spelling first.

#### Putting it all together — a minimal access control

```python
import o6
from o6.ns import ns0


class DistilleryAccessControl(o6.AccessControl):
    def __init__(self):
        super().__init__(anonymous=False, username=True)

    def activateSession(self, endpoint, remoteCertificate, session, userIdentityToken):
        if isinstance(userIdentityToken, ns0.datatypes.UserNameIdentityToken):
            user = userIdentityToken.userName
            pwd = bytes(userIdentityToken.password)
            if user == "hmi" and pwd == b"dashboard":
                return {"username": user, "role": "hmi"}
            raise o6.StatusCodeError(o6.StatusCode.BAD_USER_ACCESS_DENIED)
        raise o6.StatusCodeError(o6.StatusCode.BAD_USER_ACCESS_DENIED)


server = o6.Server(
    port=4840,
    accessControl=DistilleryAccessControl(),
)
```

A client connecting with `username="hmi", password="dashboard"` activates successfully; anything else is rejected.

---

## Assign roles from `activateSession`

The `activateSession` hook can return a `SessionActivation` object instead of a bare context, attaching roles at the moment the session is born:

```python
def activateSession(self, endpoint, remoteCertificate, session, userIdentityToken):
    if isinstance(userIdentityToken, ns0.datatypes.UserNameIdentityToken):
        user = userIdentityToken.userName
        if user == "hmi":
            return o6.SessionActivation(
                context={"username": user},
                roles=(o6.roles.observer,),
            )
        if user == "control":
            return o6.SessionActivation(
                context={"username": user},
                roles=(o6.roles.engineer,),
            )
    raise o6.StatusCodeError(o6.StatusCode.BAD_USER_ACCESS_DENIED)
```

The HMI session gets `observer` (read-only); the control-plane session gets `engineer` (read-write). The same `Setpoint._permissions.grant(...)` from the [roles page](400_access-control-roles.md) then admits the right operations for each role.

---

## The `Session` proxy

The `session` argument to `activateSession` (and to authorization hooks like `allowBrowseNode`) is a `Session` proxy:

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

Attribute keys are `QualifiedName` values or plain strings, which are promoted to namespace 0. The proxy is a *resolving* wrapper — every operation validates the underlying session id, so using it after the remote session closes raises `BadSessionIdInvalid` safely.

`session.close()` does not lock the client out — a client with automatic reconnection simply activates a new one. It is the right way to log out a session that no longer needs to be alive (e.g. an inactive HMI tab).

---

## `allowBrowseNode` and friends

`activateSession` decides *who* the session belongs to. The rest of the access-control hooks decide *what* the session may do, on a per-operation basis:

- `closeSession` — accept or reject a `CloseSession` request.
- `getUserRightsMask` — combine into the per-session effective rights.
- `getUserAccessLevel` — restrict a Variable's effective `AccessLevel` per session.
- `getUserExecutable` / `getUserExecutableOnObject` — restrict a Method's effective executability per session.
- `allowAddNode` / `allowAddReference` / `allowDeleteNode` / `allowDeleteReference` — gate the AddNodes / AddReferences / DeleteNodes / DeleteReferences services.
- `allowBrowseNode` — gate the Browse service for a node.
- `allowCreateSubscription` / `allowTransferSubscription` — gate subscription creation / transfer.
- `allowHistoryUpdate` / `allowHistoryDelete` — gate history writes.

All have permissive defaults. Override only what the distillery actually needs:

```python
class DistilleryAccessControl(o6.AccessControl):
    def allowBrowseNode(self, session, nodeId, context):
        # HMI may not browse Actuators (the wiring internals)
        if session.context and session.context.get("role") == "hmi":
            if nodeId.namespace == 1 and nodeId.id == 1500:
                return False
        return True
```

The hooks run on every operation that matches them. Override only when needed — the default behaviour is the right one for most calls.

!!! info
    Inherited authorization hooks use native C defaults. Only hooks overridden by the concrete subclass cross into Python, so a plugin that overrides only `activateSession` and `closeSession` does not acquire the GIL for routine reads, writes, browses, or method calls.

---

## `allowNonePolicyPassword`

`allowNonePolicyPassword=True` permits `UserNameIdentityToken` authentication on an unencrypted endpoint. The flag is deliberately separate from access control, because it is a transport decision: without it the stack strips the username/password `UserTokenPolicy` from an insecure endpoint and logs a warning that the password would travel in the clear.

```python
server = o6.Server(
    port=4840,
    accessControl=DistilleryAccessControl(),
    allowNonePolicyPassword=True,    # username/password allowed over plaintext
)
```

Enable it for local testing only. In production, run a [secure endpoint](420_security-policies.md) and leave this flag at its default `False`.

---

## What's next?

The distillery now authenticates sessions and assigns roles. The next page adds the encryption and integrity layer on top — security policies, certificates, and encrypted endpoints.

- [Security policies and endpoints](420_security-policies.md) — `SecurityPolicy` selection, encrypted endpoints, certificate management.
- [Server manual](../../manual/server/security.md) — the full authentication and authorization story, including session diagnostics.