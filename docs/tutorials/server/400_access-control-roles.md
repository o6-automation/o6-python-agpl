# Access control — roles

So far, anyone who can reach `opc.tcp://localhost:4840` can browse the distillery, read the kettle values, write `Setpoint` and call `Shutdown`. On a real network the server needs role-based access control, for example "the control plane can write and the HMI dashboard can only read".

This page defines roles, grants permissions to nodes by role and uses the well-known roles that ship with `o6`. At the end, an HMI dashboard session can browse and read but not write, and a control-plane session can do everything. [Access control — authentication](410_access-control-auth.md) covers how sessions get their roles.

---

## The shape of a role

A *role* is a named identity the server grants to a session. `o6` ships the well-known OPC UA roles (`Anonymous`, `AuthenticatedUser`, `Observer`, `Operator`, `Engineer`, `Supervisor`, `ConfigureAdmin`, `SecurityAdmin`) as `o6.Role` instances on the `o6.roles` singleton (`o6.roles.anonymous`, `o6.roles.authenticated_user`, `o6.roles.observer`, ..., `o6.roles.configure_admin`, `o6.roles.security_admin`). Add site-specific roles, such as control plane, HMI dashboard or lab test rig, with `server.roles.add(...)`.

Permissions are `o6.Permission` flags, combined with `|`. The distillery uses four:

| Permission | Meaning |
|---|---|
| `BROWSE` | Browse into the node. |
| `READ` | Read the `Value` attribute. |
| `WRITE` | Write the `Value` attribute. |
| `CALL` | Invoke Methods under the node. |

A node's permissions map each role to a permission set. Permissions are inherited down the subtree unless a child overrides them.

---

## Grant permissions to a node

Use the `node._permissions` attribute:

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

Every node handle (Object, Variable, Method) has `_permissions`, with `grant(...)`, `revoke(...)`, `clear()` and the bulk `set(...)` / `get()`. With `recursive=True`, a grant applies to the whole subtree; use it for a top-level folder.

!!! warning
    The leading underscore is part of the name. Every public helper on a node handle has one, because unprefixed attribute access browses to child nodes by BrowseName. Assigning to `node.permissions` silently creates an ordinary Python attribute and changes no permissions.

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

A session that has only `observer` can `client.browse(...)` the hierarchy, but every write fails with `BAD_USER_ACCESS_DENIED`.

---

## Read the current permissions

`_permissions.get()` returns the node's permissions as a dict keyed by the granted `Role` objects:

```python
for role, permission in setpoint._permissions.get().items():
    print(role.name, permission)
# Observer  Permission.BROWSE|READ
# Operator  Permission.BROWSE|READ|WRITE|CALL
```

`Permission` is an `IntFlag`, so each combination is also an integer. `Permission.BROWSE | Permission.READ` is `33` (`BROWSE=1`, `READ=32`), because the enum reserves bits in between for role-permission and history operations. Test flags with `in` (`Permission.WRITE in permission`) instead of assuming bit positions.

`set({role: perm, ...})` is the bulk form. `clear()` removes all role permissions on the node. The [server manual](../../manual/server/security.md#role-based-access-control) lists all helpers.

---

## Default-deny

A node with no role permissions is permissive by default: anyone can read and write. For default-deny, pass `rbacForAnonymous=True` to `Server(...)` and grant permissions to each role you want to admit.

```python
server = Server(port=4840, rbacForAnonymous=True)
```

This applies to every session role. Grant permissions on each application node
or set namespace defaults before clients access it. Namespace 0 provides the
Browse and Read grants needed during connection setup. See
[Default-deny behavior](../../manual/server/security.md#deny-access-without-permission-rules)
for namespace defaults and explicit session-role assignment.

---

## Grant per role, then assign roles to sessions

Permissions are granted to roles, not to sessions. A session gets permissions by holding a role. It gets the role through authentication, identity mappings or explicit server-side assignment; see [Access control — authentication](410_access-control-auth.md).

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

Register the role once, then grant it permissions on each node the control plane must write.

- `Role.applications` is a tuple of Application URIs the role applies to. Empty means every application.
- `applicationsExclude=True` turns the tuple into a deny list.
- Sessions whose Application URI is in the tuple get the role and its permissions, without an `IdentityMappingRuleType`.
- Use `identities=(...)` instead to map by user name, certificate thumbprint or another `IdentityCriteriaType`. See the [authentication page](410_access-control-auth.md) and the [server manual](../../manual/server/security.md).

---

## Next steps

| Topic | What it covers |
|---|---|
| [Access control — authentication](410_access-control-auth.md) | Session authentication and role assignment via `activateSession`. |
| [Server manual](../../manual/server/security.md#role-based-access-control) | The full role story, including `server.roles` registry APIs. |
