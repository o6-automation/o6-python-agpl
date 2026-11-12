# Namespace matching

When a client connects, it maps the server's wire-level namespace indices
(`ns=0`, `ns=1`, `ns=2`, ...) onto entries in the process-wide
[`o6.ns`][o6-ns] registry. This page describes how the mapping is built. For
how to use it, see [Namespace mapping in o6][ns-mapping] and
[Namespaces and NodeIds][address-space].

!!! info "Prerequisites"
    The user-facing pages [Namespace](../opcua-fundamentals/namespace.md)
    and [Namespace mapping in o6][ns-mapping] describe the registry and
    shortname system from the application's side.

[o6-ns]: ../sdk-fundamentals/namespace/namespace-mapping-in-o6.md
[ns-mapping]: ../sdk-fundamentals/namespace/namespace-mapping-in-o6.md
[address-space]: ../sdk-fundamentals/namespace/namespace-mapping-in-o6.md#namespaces-and-nodeids

## Why matching is non-trivial

A URI match alone is not enough:

1. The same URI can be registered several times in one process, with
   different scopes (`::global` or a per-client or per-server scope) or with
   different versions of the model. A URI match alone can pick the wrong
   entry.
2. A server can publish a URI that no module in the registry has. The client
   must still read the server's `NamespaceArray` and access its nodes.

The algorithm below handles both. It produces one wire-index → process-index
mapping per `Client`. A refresh also considers current registry candidates;
an unchanged mapping snapshot is not rebuilt.

## The wire-level flow

`Client.connect()` runs the matching in this order:

1. Open the SecureChannel and the Session.
2. Register `ns=1`. The client reads the server's `ApplicationUri`
   from a `GetEndpoints` call and registers it in the registry as
   `<client.name>_ns1`, scoped to the client's endpoint URL. The
   returned process-wide index is stored on the client as
   `_application_namespace_index`.
3. Read the server's `NamespaceArray` at `i=2255`. The result is a
   list of URIs; `uris[0]` is always `http://opcfoundation.org/UA/`
   and `uris[1]` is the application URI.
4. For each URI at `wire_index >= 2`, run the matching procedure
   described below. Build a candidate list per wire index and pick one.
5. Build a *provisional* mapping, the best guess without version
   information. If any wire index has more than one candidate, install the
   provisional mapping and read the server's `NamespaceMetadata` to resolve
   the ambiguity. Otherwise the provisional mapping is the final mapping.
6. Build the final mapping. If it differs from the previous
   snapshot, install it.

Both installations are atomic "namespace snapshots": the Python mapping, the
SecureChannel decoder mapping and the custom data type chain are replaced in
one C-level transaction. A failed refresh keeps the previous snapshot. An
unchanged snapshot is not rebuilt.

## The matching procedure

For each `(wire_index, uri)` pair with `wire_index >= 2` and a non-empty
`uri`, the client runs these steps.

### 1. Filter the registry by URI and scope

```python
hits = [
    hit
    for hit in o6.ns.filter(uri=uri)
    if hit.scope in (scope, o6.ns._GLOBAL_SCOPE)
]
```

`o6.ns.filter(uri=..., scope=...)` combines its arguments with AND, so the
client filters the scope in a second step. A hit is accepted when its scope is
the client's own scope (`self._name`) or the global scope (`::global`). Any
other scope is rejected.

`o6.ns.filter` orders results by process-wide index, so the first hit is the
lowest-indexed match.

### 2. Auto-register on miss

If `hits` is empty, no registration matches the URI in an eligible scope.
The URI may already exist under another client or server scope. The client registers it
under the client scope with a deterministic shortname:

```python
hits = [
    o6.ns.register(
        shortname=_remote_namespace_shortname(uri, scope),
        uri=uri,
        scope=scope,
    )
]
```

The shortname is the last non-empty URI path segment, snake-cased and
prefixed with the client scope. On collision, a twelve-character SHA-256
suffix of the URI is appended. The shortname is unique in the process and
deterministic within that client scope: refreshing the same client reuses
its registration. A second client has a different name and scope, so it
registers its own identity even when connecting to the same server. Shared
`::global` model registrations can be reused by both clients.

### 3. Pick a candidate

```python
selected[wire_index] = _select_namespace_candidate(hits, scope)
```

`_select_namespace_candidate` applies this priority order:

1. **Exact version match.** With a non-empty `server_version` argument, only
   candidates with `hit.version == server_version` are kept. Without one,
   this step is skipped and all `hits` are considered.
2. **Scope preference.** A candidate whose `scope` equals the client's own
   scope is preferred over `::global`. The comparison is
   `(hit.scope == scope, ...)`, which sorts `True > False`.
3. **Version key.** The candidate with the highest
   `_version_key(hit.version)` wins. The key splits the version string on
   digit/letter boundaries. Numeric segments sort as integers; alphabetic
   segments sort as lowercase strings, higher than integers. So `"1.10.0"`
   sorts above `"1.9.0"` and `"1.05.06"` above `"1.05.0RC"`.

The function uses `max(..., key=...)`, so remaining ties go to the lowest
process-wide index, the order of `o6.ns.filter`.

### 4. Resolve version ambiguity against the server

If a wire index has more than one candidate, the chosen one might not match
the version the server published. The client applies the provisional mapping
and walks the server's `NamespaceMetadata` (the `NamespaceMetadataType` object
under the Objects folder) to read `NamespaceVersion` for that wire index. It
then re-runs `_select_namespace_candidate(hits, scope, server_version)`, this
time with an exact version to match.

If the server is newer than every compiled version, the client uses the
highest available version and logs a warning naming the URI, the server's
version and the client's best match:

> Namespace URI `<uri>` from server has version `<server_version>`
> which is newer than the client's best match version
> `<client_version>`.

The client then builds the final mapping and installs it atomically. The
provisional mapping is in effect only during the metadata walk. The `Client`
you use always exposes the final mapping.

## Priority order — summary

From most to least specific:

| Step | Source of disambiguation | Applied to |
| --- | --- | --- |
| 1 | Wire index fixed by server (`ns=0`, `ns=1`, `ns>=2`) | The URI list itself |
| 2 | URI exact match against the registry | The registry |
| 3 | Scope must be the client's scope or `::global` | The candidate set |
| 4 | If URI is unknown, auto-register under client scope | The registry |
| 5 | Version exact match against `NamespaceMetadata.NamespaceVersion` | The candidate set, when ambiguous |
| 6 | Scope preference (client > `::global`) | The candidate set, ties |
| 7 | `_version_key(version)` (numeric-aware) | The candidate set, ties |
| 8 | Process-wide index (lowest first) | The candidate set, final ties |

URI and scope are the main filters. The version key and the exact-version
probe matter only when several compiled modules share a URI. This is rare,
but expected for companion specifications with several published releases.

## `ns=0` and `ns=1` are special

`ns=0` and `ns=1` are handled outside the matching procedure:

- `ns=0` always maps to the `ns0` module, which is registered at
  import time and never has a per-client scope.
- `ns=1` maps to the `<client.name>_ns1` registration that step 2 of
  the wire-level flow installs, with the wire index `1` and the
  process index stored in `_application_namespace_index`.

Both mappings are pinned into the entries list before the candidate loop
runs, so the candidate logic never decides them.

## Idempotence and runtime additions

You can call `Client.updateRemoteNamespaces` repeatedly. The Python mapping,
the SecureChannel decoder mapping and the custom data type chain are rebuilt
together, and an unchanged snapshot is detected before any work is done.

A connected server can add a namespace at runtime. The new URI appears in the
server's `NamespaceArray`, and the client sees it on the next call. A URI
with an eligible registration reuses an entry. Otherwise it gets a new
client-scoped entry through auto-registration, and the snapshot is rebuilt.

The client never deletes a registry entry. A namespace registered for one
server stays in the registry after disconnect. Reconnecting the same client
can reuse it; a new client uses its own scope.

## Edge cases

- **Empty URI at `ns>=2`.** The wire index is skipped and not added to the
  mapping.
- **Empty `NamespaceArray`.** `updateRemoteNamespaces` returns
  without modifying state.
- **Server version older than every compiled version.** No exact match is
  found. The client picks the highest available version and logs no warning.
- **Server version equal to the highest compiled version.** The exact match
  picks that hit, and the final mapping equals the provisional one. The
  snapshot is rebuilt only if it differs from the previous snapshot.
- **Failed snapshot transaction.** A failure in `_apply_namespace_snapshot`
  propagates to the caller, and the previous snapshot stays in effect. No
  partial state is installed. The test
  `test_failed_namespace_snapshot_preserves_previous_mapping` in
  `tests/namespaces/test_declarations_and_mapping.py` covers this path.
- **Two connected servers with the same URI but different application
  URIs.** Each server has its own client, and each client its own `ns=1`
  registration. The shared URI resolves to one registration under the global
  scope if one exists, or else to one registration per client scope. Wire
  indices are server-local; the mapping is client-local.

## Where to look in the code

- `Client._set_ns1_mapping` in `o6/client.py` — the `ns=1`
  registration.
- `Client.updateRemoteNamespaces` in `o6/client.py` — the procedure
  above, from reading `i=2255` to applying the final snapshot.
- `_select_namespace_candidate`, `_version_key`, and
  `_remote_namespace_shortname` in `o6/client.py` — the priority
  logic, the version key, and the auto-register shortname.
- `_NamespacePackage.filter` in `o6/ns/__init__.py` — the
  AND-combined URI / scope / version filter.
- `_apply_namespace_snapshot` (Python helper plus the
  `pyClient_apply_namespace_snapshot` C call) — the atomic snapshot
  transaction.

The priority order is tested in `tests/namespaces/test_client_mapping.py`:

- `test_version_selection_prefers_exact_match` — step 5.
- `test_version_selection_defaults_to_latest` — step 7.
- `test_version_selection_prefers_client_scope` — step 6.
- `test_remote_namespace_shortname_is_client_scoped` — step 4.
- `test_remote_namespace_shortname_disambiguates_collisions` — step 4.
- `test_unknown_remote_namespace_is_registered_and_mapped` — step 4
  end-to-end against the test server.

## Related topics

| Topic | What it covers |
|---|---|
| [Namespace mapping in o6](../sdk-fundamentals/namespace/namespace-mapping-in-o6.md) | The registry, shortnames, scopes and the user-facing API. |
| [Namespaces and NodeIds](../sdk-fundamentals/namespace/namespace-mapping-in-o6.md#namespaces-and-nodeids) | The user-facing description of the `ns=1` registration and `updateRemoteNamespaces`. |
| [Loading and using nodesets](../sdk-fundamentals/namespace/loading-and-using-nodesets.md) | Importing compiled declarations and decoding custom values. |
