# Access control — roles

The distillery is running on an open channel — anyone who can reach `opc.tcp://localhost:4840` can browse it, read the kettle values, write a new `Setpoint`, and call `Shutdown`. That's fine while you're poking at the sim on a laptop, but the moment the server is on a real network, it needs a *role-based access control*. Not "anyone", but "the control plane can write and the HMI dashboard can only read".

This page is the first half of that: defining what a *role* is, granting permissions to nodes by role, and using the well-known roles `o6` ships with.

By the end of this page, an HMI dashboard session can browse and read but not write, and a control-plane session can do everything.

---

## The shape of a role

A *role* is a named identity the server can grant to a session. `o6` ships the well-known OPC UA roles (`Anonymous`, `AuthenticatedUser`, `Observer`, `Operator`, `Engineer`, `Supervisor`, `ConfigureAdmin`, `SecurityAdmin`) as instances of `o6.Role`, available from the `o6.roles` singleton (`o6.roles.anonymous`, `o6.roles.authenticated_user`, `o6.roles.observer`, ..., `o6.roles.configure_admin`, `o6.roles.security_admin`). New roles can be added through `server.roles.add(...)` for site-specific identities (control plane, HMI dashboard, lab test rig).

Permissions are `o6.Permission` flags, combined with `|`. The four that matter for the distillery are:

| Permission | Meaning |
|---|---|
| `BROWSE` | Browse into the node. |
| `READ` | Read the `Value` attribute. |
| `WRITE` | Write the `Value` attribute. |
| `CALL` | Invoke Methods under the node. |

A node's permissions are a dict from role to permission set. Permissions are inherited down the subtree unless a child overrides them.

---

## Grant permissions to a node

The `node._permissions` attribute holds a small object that supports the standard operations:

```python
import o6
from o6 import Server, Permission

server = Server(port=4840)
sys = server.addObject("DistillingSystem", server.objectsNode, nodeId="ns=1;i=1000")
status = server.addObject("Status", sys, nodeId="ns=1;i=1200")
setpoint = server.addVariable("Setpoint", status, 85.0, nodeId="ns=1;i=1204", writable=True)


# Everyone can read; only Operator and Engineer can write.
setpoint._permissions.grant(
    o6.roles.observer,
    Permission.BROWSE | Permission.READ,
)
setpoint._permissions.grant(
    o6.roles.operator,
    Permission.BROWSE | Permission.READ | Permission.WRITE,
)

server.start()
```

The `_permissions` attribute is on every node handle (object, variable, method). It carries `grant(...)`, `revoke(...)`, `clear()`, and the bulk `set(...)` / `get()`. With `recursive=True`, a grant applies to the whole subtree, which is what you want for a top-level folder.

!!! warning
    The leading underscore is part of the name. Every public helper on a node handle carries one, because unprefixed attribute access is reserved for browsing to child nodes by BrowseName. Assigning to `node.permissions` silently creates an ordinary Python attribute and changes no permissions at all.

#### Putting it all together

```python
import o6
from o6 import Permission, Server

server = Server(port=4840)
sys = server.addObject("DistillingSystem", server.objectsNode, nodeId="ns=1;i=1000")

# Read-only for everyone, write-on for operator+engineer, recursively
sys._permissions.grant(
    o6.roles.observer,
    Permission.BROWSE | Permission.READ,
    recursive=True,
)
sys._permissions.grant(
    o6.roles.operator,
    Permission.BROWSE | Permission.READ | Permission.WRITE | Permission.CALL,
    recursive=True,
)

server.start()
```

A `client.browse(...)` from a session that has only `observer` granted returns the hierarchy but every write attempt is rejected with `BAD_USER_ACCESS_DENIED`.

---

## Read the current permissions

`_permissions.get()` returns the dict-of-role-to-permissions for the node, keyed by the `Role` objects that were granted:

```python
for role, permission in setpoint._permissions.get().items():
    print(role.name, permission)
# Observer  Permission.BROWSE|READ
# Operator  Permission.BROWSE|READ|WRITE|CALL
```

`Permission` is an `IntFlag`, so each combination is also an integer — `Permission.BROWSE | Permission.READ` is `33` (`BROWSE=1`, `READ=32`), not a small bitmask, because the enum reserves separate bits for role-permission and history operations further down the flag space. Compare with `in` (`Permission.WRITE in permission`) rather than assuming low bit positions.

`set({role: perm, ...})` is the bulk form. `clear()` removes all role permissions on the node. The full set of helpers is in the [server manual](../../manual/server/security.md#role-based-access-control).

---

## Default-deny

A node with no role permissions is **permissive** by default — anyone can read and write. To switch a server to default-deny, set `rbacForAnonymous=True` on the `Server(...)` constructor, then explicitly grant permissions for each role you want to admit.

```python
server = Server(port=4840, rbacForAnonymous=True)
```

Anonymous sessions then have no permissions unless a node explicitly grants them. The distillery's default is permissive — the constructor leaves `rbacForAnonymous` at `False` — so a client without authentication still sees the address space. The right pattern for a deployed distillery is `rbacForAnonymous=True` plus explicit grants on every node that should be reachable from a given role.

---

## Grant per role, then assign roles to sessions

Permissions are *granted to roles*, not to sessions. To give a *session* permissions, the session needs the role. The next page covers how a session ends up with the right role — through authentication, through identity mappings, or through explicit assignment on the server side. The role definitions and the per-node grants live here.

```python
# The role itself — a site-specific "control plane" role, matched by the
# session's Application URI rather than by an identity-mapping rule.
control_plane = server.roles.add(
    o6.Role(
        "ControlPlane",
        applications=("urn:example:control-plane",),
    )
)

# The same role gets the permissions on the Setpoint
setpoint._permissions.grant(
    control_plane,
    Permission.BROWSE | Permission.READ | Permission.WRITE,
)
```

The role is registered once, then granted to it on whichever nodes the control plane should be able to write. `Role.applications` is a dedicated field for exactly this case — a tuple of Application URIs the role applies to (empty means "every application"); set `applicationsExclude=True` to treat it as a deny list instead. Sessions whose Application URI is in that tuple get the role and inherit its permissions, no `IdentityMappingRuleType` needed. Use `identities=(...)` instead when the mapping is based on user name, certificate thumbprint, or another `IdentityCriteriaType` — see the [authentication page](410_access-control-auth.md) and the [server manual](../../manual/server/security.md) for that story.

---

## What's next?

The distillery now has a role-based access control story. The next page covers the other half: *how* sessions get roles — the authentication hooks that map user-name identities to roles.

- [Access control — authentication](410_access-control-auth.md) — session authentication and role assignment via `activateSession`.
- [Server manual](../../manual/server/security.md#role-based-access-control) — the full role story, including `server.roles` registry APIs.