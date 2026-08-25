# Namespace matching

When a client connects, the server's wire-level namespace indices
(`ns=0`, `ns=1`, `ns=2`, ...) need to be mapped onto entries in the
process-wide [`o6.ns`][o6-ns] registry. This page describes how that
mapping is built. It does not cover how to use it — that is the job of
[Namespace mapping in o6][ns-mapping] and
[Working with the address space][address-space].

!!! info "Prerequisites"
    The user-facing pages [Namespace](../opcua-fundamentals/namespace.md)
    and [Namespace mapping in o6][ns-mapping] describe the registry and
    shortname system from the application's side. This page assumes that
    surface and digs into the matching algorithm.

[o6-ns]: ../sdk-fundamentals/namespace/namespace-mapping-in-o6.md
[ns-mapping]: ../sdk-fundamentals/namespace/namespace-mapping-in-o6.md
[address-space]: ../client/address-space.md

## Why matching is non-trivial

A namespace URI is supposed to be unique, but a URI alone is not enough
information. Two reasons:

1. The same URI can be registered multiple times in the same process
   with different scopes (`::global` versus a per-client or per-server
   scope) or with different versions of the model. A URI match alone
   would pick the wrong entry.
2. A server may publish a URI that no module in the registry has. The
   client must still be able to read the server's `NamespaceArray` and
   talk to its nodes.

The algorithm below answers both. The result is one wire-index →
process-index mapping per `Client`, rebuilt only when the server's
`NamespaceArray` changes.

## The wire-level flow

`Client.connect()` triggers the matching. The flow, in order, is:

1. Open the secure channel and the session as usual.
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
5. Build a **provisional** mapping — the best non-version-aware guess —
   and, if any wire index has more than one candidate, install that
   provisional mapping and read the server's `NamespaceMetadata` to
   resolve the ambiguity. If no wire index is ambiguous, the
   provisional mapping is the final mapping.
6. Build the **final** mapping. If it differs from the previous
   snapshot, install it.

Both the provisional and final installations are atomic
"namespace snapshots" — Python mapping, SecureChannel decoder
mapping, and the custom datatype chain are all replaced in one C-level
transaction. A failed refresh leaves the previous snapshot in place.
An unchanged snapshot is not rebuilt.

## The matching procedure

For each `(wire_index, uri)` pair with `wire_index >= 2` and a
non-empty `uri`, the client does the following:

### 1. Filter the registry by URI and scope

```python
hits = [
    hit
    for hit in o6.ns.filter(uri=uri)
    if hit.scope in (scope, o6.ns._GLOBAL_SCOPE)
]
```

The filter combines as an AND — `o6.ns.filter(uri=..., scope=...)` —
but the client uses the two-step form to express the "either-or"
rule on scope: a hit is accepted when its scope is *either* the
client's own scope (`self._name`) *or* the global scope (`::global`).
Any other scope is rejected.

The default ordering of `o6.ns.filter` is by process-wide index, so
the first hit is the lowest-indexed match.

### 2. Auto-register on miss

If `hits` is empty, the URI is not in the registry at all. The client
auto-registers it under the client scope with a deterministic
shortname:

```python
hits = [
    o6.ns.register(
        shortname=_remote_namespace_shortname(uri, scope),
        uri=uri,
        scope=scope,
    )
]
```

The shortname is built from the last non-empty URI path segment,
snake-cased, prefixed with the client scope, and disambiguated with a
twelve-character SHA-256 suffix of the URI on collision. The result
is a unique, process-wide shortname that round-trips: a second client
that sees the same URI on the same server will compute the same
shortname and re-use the existing registration.

### 3. Pick a candidate

```python
selected[wire_index] = _select_namespace_candidate(hits, scope)
```

`_select_namespace_candidate` implements the priority order. With no
`server_version` argument, the priority is:

1. **Exact version match.** If the caller supplied a non-empty
   `server_version`, candidates with `hit.version == server_version`
   are kept and the rest are dropped. Without a `server_version`,
   this step is a no-op and the full `hits` list is considered.
2. **Scope preference.** Among the surviving candidates, the one
   whose `scope` equals the client's own scope (rather than
   `::global`) is preferred. The comparison is `(hit.scope == scope, ...)`,
   which sorts `True > False`.
3. **Version key.** Among the survivors, the one with the highest
   `_version_key(hit.version)` wins. The version key splits the
   version string on digit/letter boundaries and sorts numeric
   segments as integers (lower) and alphabetic segments as
   lower-cased strings (higher than integers), so `"1.10.0"` sorts
   above `"1.9.0"` and `"1.05.06"` sorts above `"1.05.0RC"`.

The function uses `max(..., key=...)`, so ties at the version key
are broken by process-wide index (lowest first), which is the order
of `o6.ns.filter`.

### 4. Resolve version ambiguity against the server

If a wire index has more than one candidate, the chosen candidate
might not be the version the server actually published. The client
applies the provisional mapping, then walks the server's
`NamespaceMetadata` (the `NamespaceMetadataType` object under the
Objects folder) to read `NamespaceVersion` for that wire index, and
re-runs `_select_namespace_candidate(hits, scope, server_version)`.

This time the exact version match has data to work on. If the server
is newer than anything the client has compiled, the match falls back
to the highest available version, and the binding logs a warning
naming the URI, the server's version, and the client's best match:

> Namespace URI `<uri>` from server has version `<server_version>`
> which is newer than the client's best match version
> `<client_version>`.

The mapping is then rebuilt as the **final** mapping and installed
atomically. The provisional mapping is in effect only for the
duration of the metadata walk; the user-visible `Client` always
exposes the final mapping.

## Priority order — summary

In order from most to least specific, the algorithm uses:

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

URI and scope are the dominant filters. The version key and the
exact-version probe only matter when the URI is shared by multiple
compilations — which is rare, but expected for companion specs that
ship in multiple historical releases.

## `ns=0` and `ns=1` are special

`ns=0` and `ns=1` are handled outside the matching procedure:

- `ns=0` always maps to the `ns0` module, which is registered at
  import time and never has a per-client scope.
- `ns=1` maps to the `<client.name>_ns1` registration that step 2 of
  the wire-level flow installs, with the wire index `1` and the
  process index stored in `_application_namespace_index`.

Both mappings are pinned into the entries list *before* the
candidates loop runs, so the candidate logic is never asked to
decide between them.

## Idempotence and runtime additions

`Client.updateRemoteNamespaces` is safe to call again. The snapshot
transaction is idempotent on equal snapshots: the Python mapping, the
SecureChannel decoder mapping, and the custom datatype chain are
all rebuilt together, and an unchanged snapshot is detected before
any work is done.

A connected server can add a new namespace at runtime. The new URI
appears in the server's `NamespaceArray` and the client sees it on
the next call. If the URI is already in the registry, the existing
mapping is reused; if not, the auto-register step creates a new
client-scoped entry and the snapshot is rebuilt.

The client never deletes an entry from the registry. A namespace
that was registered for one server remains in the registry after
disconnect and may be reused by a later connection.

## Edge cases

- **Empty URI at `ns>=2`.** The wire index is skipped. Empty URIs
  are not added to the mapping.
- **Empty `NamespaceArray`.** `updateRemoteNamespaces` returns
  without modifying state.
- **Server version older than every compiled version.** The exact
  match step finds nothing, the client picks the highest available
  version, and no warning is logged.
- **Server version equal to the highest compiled version.** The
  exact match step picks that hit, and the final mapping matches
  the provisional mapping. The snapshot is rebuilt only if it
  differs from the previous snapshot.
- **Failed snapshot transaction.** A failure inside
  `_apply_namespace_snapshot` is propagated to the caller, but the
  previous snapshot remains in effect. The binding does not roll
  forward to a partial state. The test
  `test_failed_namespace_snapshot_preserves_previous_mapping` in
  [tests/e2e/test_decorators.py][tests-e2e-decorators] exercises
  this path.
- **Two connected servers with the same URI but different
  application URIs.** Each server has its own client, so each
  client has its own `ns=1` registration. The shared URI is
  registered once at process level under the global scope (because
  both clients have a hit there) or under each client's scope (if
  not). The wire indices are server-local; the mapping is
  client-local.

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

The priority order is exercised by
[tests/client/test_utility_functions.py][tests-utility]:

- `test_version_selection_prefers_exact_match` — step 5.
- `test_version_selection_defaults_to_latest` — step 7.
- `test_version_selection_prefers_client_scope` — step 6.
- `test_remote_namespace_shortname_is_client_scoped` — step 4.
- `test_remote_namespace_shortname_disambiguates_collisions` — step 4.
- `test_unknown_remote_namespace_is_registered_and_mapped` — step 4
  end-to-end against the test server.

[tests-utility]: https://github.com/o6-automation/o6-python/blob/main/tests/client/test_utility_functions.py
[tests-e2e-decorators]: https://github.com/o6-automation/o6-python/blob/main/tests/e2e/test_decorators.py

## See also

- [Namespace mapping in o6](../sdk-fundamentals/namespace/namespace-mapping-in-o6.md)
  — the registry, shortnames, scopes, and the user-facing API.
- [Working with the address space](../client/address-space.md) — the
  user-facing description of the `ns=1` registration and
  `updateRemoteNamespaces`.
- [Loading and using nodesets](../sdk-fundamentals/namespace/loading-and-using-nodesets.md)
  — the `Namespace.from_xml` companion to the client-side matching.
