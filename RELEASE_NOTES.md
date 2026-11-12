# Release Notes

## (unreleased)

<p>&nbsp;</p>
<p>&nbsp;</p>

## 3.0.0

### Upgrading from 2.x

3.0.0 changes generated names, default NodeIds and security defaults. Check these before upgrading; details are under Breaking Changes.

- Generated `o6.ns.*` and `dir(node)` names no longer spell punctuation as words (`<Collector>` → `collector_`). Update code that uses the old spellings.
- Nodes created without `nodeId=` now live in namespace 1 (`ns=1;i=…`) instead of namespace 0. Pass `nodeId=` where identifiers must stay stable.
- An application certificate with an empty `trustList` now rejects every peer. Supply trusted certificates, or set `acceptAllCertificates=True` for development.
- Role permissions and `accessRestrictions=` are now enforced, including in custom `o6.AccessControl` hooks that call `super()`.
- The NodeSet2 compiler moved to the separate `o6-ncc` package (`pip install o6-ncc`).
- Servers and clients without an `applicationUri` now use `urn:o6-Python.unconfigured.application`, which also changes the URI of namespace 1. Set `applicationUri` where peers or stored configuration depend on it.

### New Features

- Added GDS PushManagement receiving-server support on Linux and Windows through `Server.enablePushManagement()`, with optional SDK PKI persistence through `server.config.setDefaultWithFilestore()`. Authenticated SecurityAdmin clients can renew RSA application certificates (including regenerated CSR keys) and manage trust lists. Restart reloads trust and CRLs; applications explicitly supply the certificate/key to activate. The receiver verifies a pushed certificate and every certificate of a new application TrustList against the server's TrustList, so the issuing CA must already be in the issuer list. Includes an externally receiving-server example. Updates retain the SDK's non-atomic failure behavior; this does not add a CA or pushing-client API.

- Added prebuilt wheels for CPython 3.15 on Linux, macOS, and Windows.

- Added synchronous and asynchronous `Client.loadRemoteDataTypes()`. It reads the server's custom DataTypes and registers the structures of every namespace the client has no package for, so their values decode to Python classes instead of `ExtensionObject` on reads, method outputs, history and subscriptions. It returns the registered classes. Packaged namespaces are never extended, only the binary encoding is supported, and nothing loads automatically on connect. Servers before OPC UA 1.04, which describe structures in DataType dictionaries instead of the `DataTypeDefinition` attribute, are not supported: each such type logs one warning and stays undecoded.

- The client now decodes custom structures of server namespaces without a package on demand, without `loadRemoteDataTypes()`. The first time `read()`, a node value, `call()` or `historyRead()` returns a value whose DataType the client does not know, the client loads that DataType and the types it depends on from the server, once per encoding, and returns the value decoded. This also covers values in arrays, Variants and fields of known structures. Subscription and event notifications are not held back: the first notification of an unknown type arrives as `ExtensionObject` while the type loads in the background, and later ones arrive decoded. Call `loadRemoteDataTypes()` before subscribing to decode the first notification too. The `service*` methods decode only DataTypes the client already has. Turn on-demand loading off with `Client(loadUnknownDataTypes=False)` or `client.config.loadUnknownDataTypes = False`.

- Added `securityPolicies` to `Server` and `server.config.setEncryption()` and `setDefaultWithFilestore()`. It selects exactly which SecurityPolicies the server offers: `None`, `Basic256Sha256`, `Aes128_Sha256_RsaOaep`, `Aes256_Sha256_RsaPss` and, on request, the deprecated `Basic128Rsa15` and `Basic256`. Policies that are left out cannot open a channel. The deprecated policies get a non-zero SecurityLevel below all others. The option excludes `secureOnly`.

- Added `server.config.shutdownDelay` (milliseconds, default 0). With a delay, `stop()` keeps serving first, reports `ServerStatus/State` as Shutdown with a counting-down `SecondsTillShutdown`, and sends the `shutdown` lifecycle notification, so connected clients get advance notice.

- Added `server.config.verifyRequestTimestamp`. `True` (the default) rejects requests without a RequestHeader timestamp with `BadInvalidTimestamp`; `False` logs a warning and continues.

- Added server configuration readback and setters for session and monitored-item quotas, sampling and publishing ranges, queue limits, subscription maintenance, retransmission queues, and listening URLs, including loopback binding.

- Added the operation limits `maxNodesPerRead`, `maxNodesPerWrite`, `maxNodesPerMethodCall`, `maxNodesPerBrowse`, `maxNodesPerRegisterNodes`, `maxNodesPerTranslateBrowsePathsToNodeIds` and `maxNodesPerNodeManagement` to `server.config`, next to `maxMonitoredItemsPerCall`. The server rejects larger service calls with `BadTooManyOperations` and advertises the value in `Server/ServerCapabilities/OperationLimits`. The default of 0 means unlimited.

- Added `Client.registerServer()` and `unregisterServer()` for synchronous and asynchronous LDS registration, updates, and removal, with optional mDNS metadata and checked responses.

- Added mDNS configuration and address publication through `MdnsConfig` and `Server.setMdns()`, included by default in Linux and macOS PyPI wheels. `stop()` withdraws the server's announcements and addresses, and the next `start()` announces them again.

- Added synchronous and asynchronous `Server.registerServerOnNetwork()` and `deregisterServerOnNetwork()` for manual discovery announcements and removal. With an announcing mDNS configuration, the URL host must be a bare hostname or one qualified with `.local`, which is announced as the bare hostname; other hosts raise `ValueError`.

- Added `accessLevel=` and `userAccessLevel=` to `Server.addVariable()` and `Client.addVariable()`. An explicit AccessLevel replaces the one derived from `writable`, so a Variable can grant `STATUS_WRITE` and `TIMESTAMP_WRITE` to clients that write a status or SourceTimestamp with the value.

- Added `applicationName=` and `productUri=` to `o6.Server`, and `server.config.buildInfo` for the BuildInfo in `Server/ServerStatus`.

- Added `Server.rejectedCertificates` to inspect rejected application certificates and `Server.onCertificateRejected(callback)` to handle application and X.509 user-token rejections. The server logs the subject, ApplicationUri and thumbprint of each rejected certificate. The in-memory list holds up to 100 distinct certificates; the next distinct rejection clears it and starts a new list.

### Breaking Changes

- Python names generated from BrowseNames no longer spell punctuation as words. Each run of characters that cannot appear in a Python identifier now collapses to a single `_`, a leading `_` is dropped, and a leading digit is still spelled out. Placeholder and separator-bearing members are renamed throughout `o6.ns.*`: `<Collector>` is now `collector_` rather than `langleCollectorRangle`, `Zone 0` is `zone_0` rather than `zoneSpace0`, and a URI-shaped BrowseName becomes a `_`-separated name rather than a chain of `Colon`/`Slash` words. The same rules now spell the `dir(node)` aliases, so a browsed child and its generated declaration agree. Names are also NFKC-normalized, matching what Python does to every identifier in a source file. Two consequences are worth checking: names differing only in their separators (`My Variable`, `My-Variable`, `My_Variable`) now share one spelling, as do names differing only by normalization, and a collision within one scope is disambiguated with `_2`, `_3`. Look a declaration up by NodeId where a name is ambiguous.

- Nodes created without a NodeId now get a numeric NodeId in the server's application namespace, index 1, instead of namespace 0, which belongs to the OPC Foundation. This covers `addVariable()`, `addObject()`, `addMethod()` and the other `add*` helpers of the server, declared instances without `nodeId=`, and AddNodes requests from any client without a requested NodeId. A node that was `i=50021` is now `ns=1;i=50021`; the numbers were never stable, so pass `nodeId=` where clients or stored configuration depend on the identifier. In one process, compare a server's `ns=1` NodeIds with a client's by namespace URI: the client returns the server's namespace 1 under its `<client>_ns1` registration. `Client.invalidateNodeCache()` and `Client.browse()` now accept the `ns=1` alias for handles obtained by navigation.

- Clients and servers configured with an application certificate now reject peer certificates when `trustList` is empty. Previously, they accepted them. Supply trusted peer or CA certificates; `issuerList` only completes certificate chains and does not establish trust. Server trust also applies to X.509 user tokens. For development, `acceptAllCertificates=True` bypasses validation; this option is now available on `Client` and `client.config` as well as `Server`.

- `rbacForAnonymous=True` now remains effective when encryption is configured, including through `config.setEncryption()`. Namespace 0 grants Browse and Read to Anonymous and AuthenticatedUser so clients can connect. Nodes created without an explicit NodeId belong to namespace 1 and need their own node or namespace grants.

- Inherited authorization hooks in custom `o6.AccessControl` plugins now enforce node and namespace role permissions, including roles assigned through `SessionActivation`. Previously, those hooks granted access regardless of role permissions. Overrides that call `super()` retain the checks; independent return values replace them. `Session.effectivePermissions(nodeId)` returns the permissions granted to a session by its roles.

- Servers and clients without an `applicationUri` now use `urn:o6-Python.unconfigured.application` instead of open62541's `urn:open62541.unconfigured.application`. A server publishes it in the ServerArray, as the URI of namespace 1 and in GetEndpoints and FindServers. Clients that find the server's namespace by URI, and peers that pin the old URI, need the new one; set `applicationUri` where it must stay stable. Clients also announce the ApplicationName `o6 Python Client` and the ProductUri `https://o6-automation.com/o6-python` instead of empty values. `createSelfSignedCertificate()` now defaults to the same ApplicationUri and the common name `o6 Python@localhost`, so a default certificate matches a server or client without `applicationUri`; previously it used `urn:open62541.server.application`, which matched neither.

- `accessRestrictions=` now enforces signing and encryption requirements for remote node operations, including Browse when `APPLY_RESTRICTIONS_TO_BROWSE` is set. Previously, these settings were ignored. An insufficiently protected channel receives `BadUserAccessDenied`. The AccessRestrictions Attribute remains unavailable for Read and Write. See [Access restrictions](https://docs.o6-automation.com/o6-python/manual/server/security/#access-restrictions) for supported operations and limitations.

### Improvements

- The NodeSet2 compiler now ships as the separate `o6-ncc` distribution (`pip install o6-ncc`, commands `pyncc` / `ncc python`) instead of living in the source repository under `tools/nodeset_compiler/`. It bundles the OPC Foundation nodesets it resolves against, so compiling no longer needs a source checkout or its submodules. Dependencies are declared with `-e ns0` rather than `--existing ns0=<path>`, and `-o` names the directory the generated package is written into. See [Compiling Nodesets](https://docs.o6-automation.com/o6-python/manual/information-model-authoring/compiling-nodesets/).

### Bug Fixes

- Fixed TCP connections failing for clients and servers using Windows’ default asyncio Proactor event loop.

- Servers can configure their LDS registration capabilities through `server.config.serverCapabilities`, for example `["DA", "HD"]`, instead of always advertising `NA`. Set it before starting the server.

- Fixed connections accepted during server shutdown sometimes remaining open and causing asyncio errors.

- Fixed Credential files with an empty `FeatureScope` (all features) failing the signature check and falling back to Script Mode. The verifier now also accepts empty fields in the null form the signing tool uses, so issued Credentials verify without being reissued.

- Fixed crashes when garbage collection runs during client or server timer callbacks, including client housekeeping after failed connections.

- Fixed `server.config.maxSubscriptions` and `maxSubscriptionsPerSession` allowing changes while the server was active; both now enforce open62541's requirement that configuration changes occur only while the server is fully stopped.

- `createSelfSignedCertificate()` now raises `ValueError` for a subject that X.509 cannot hold: a `commonName` or `organization` that is empty or longer than 64 characters, or a `country` that does not have two characters. It raised `StatusCodeError` (`Bad_InternalError`) before, and only the log said that setting the subject failed. A common name that contains a long host name, such as `MyServer@host.example.com`, can exceed the limit; keep the full host name in `altNames`.

- The ten-minute Script Mode timeout now reports “Scripting Period ended” instead of “Trial period ended”.

- `dir(node)` now exposes valid Python aliases for child names containing spaces, punctuation, leading digits, or keywords; the same aliases work with dot access.

- Client and server `browse()` and `browsePage()` now return all reference fields by default; explicit result masks remain supported.

- Local `ExpandedNodeId` values, including browse results, now display registered namespace shortnames and accept those strings when reconstructed.

- `addVariable()` on the server and client, and VariableType instantiation, now create scalar Variables for `StatusCode` and OptionSet values. Iterable `enum.Flag` members were inferred as arrays, which raised `StopIteration` or `Bad_TypeMismatch`.

- `Server.addVariable()` with an `o6.DataValue` as the initial value now takes the DataType and ValueRank from its `value` and keeps its status and timestamps. It created a Variable of DataType `DataValue` before. `Client.addVariable()` rejects a DataValue with `TypeError`, because AddNodes carries no status. With `dataType=o6.DataValue`, both keep the DataValue as the value of a Variable of DataType DataValue.

- A server's DataTypeDefinition of a custom structure now gives the DataType of a field whose type is another custom structure or enumeration with the server's namespace index. It carried the process-wide index, so clients in another process could not resolve nested fields and decode the structure from its definition.

- Publishing a namespace now adds the nodes OPC UA Part 3 requires for DataTypes. A structure gets its `Default Binary` DataTypeEncoding Object at its `defaultEncodingId` and the `HasEncoding` reference to it; compiled companion specifications such as DI get the missing reference to their declared encoding Object. An enumeration without an `EnumStrings` or `EnumValues` Property gets `EnumStrings` for the values `0..n-1` and `EnumValues` otherwise, and an integer OptionSet gets `OptionSetValues`. The encoding Object now occupies the encoding NodeId, which is the DataType's numeric NodeId plus one unless `defaultEncodingId=` is given; if another node of the model already uses that NodeId, a warning is logged and no encoding Object is added.

- `createEvent()`, `emitEvent()` and `o6.Event` now translate the keys of `fields` into the paths with server namespace indexes that event filters select. A key can be the BrowseName of a field of the event type (`"Counter"`), a path with registered shortnames or process-wide namespace indexes (`"/verif:Counter"`), or a `QualifiedName`. Before, such fields were emitted as null without notice. A key that is likely a mistake, such as an unknown shortname or `"/Counter"` for a field in another namespace, emits a `UserWarning` once per event type. `o6.QualifiedName` is now hashable, so it can be used as a key.

- Calling a Method without an implementation now returns `Bad_NotImplemented` instead of `Bad_InternalError`. This covers declared Methods without a bound callback and the Condition Methods of alarm instances, such as `Enable` and `Acknowledge`, and `ConditionRefresh`, which o6 does not implement. Methods implemented by open62541, such as `GetMonitoredItems`, are unchanged.

- The typing stub of `o6.LocalizedText` and two manual examples now give the two-argument order the runtime uses: `o6.LocalizedText(text, locale)`. They said `(locale, text)`, so code written from them created values with text and locale swapped; check two-argument calls whose first argument is a locale such as `"en"`. The single-string shorthand stays `"locale:text"`.

- A server listening on all interfaces, the default, now accepts IPv6 connections as well as IPv4. Clients that resolve `localhost` to `::1` first, such as open62541 clients on macOS, can connect again.

- The client accepts IPv6 endpoint URLs with the address in brackets, such as `opc.tcp://[::1]:4840`, with or without a port. The endpoint URL check now also rejects ports outside 1 to 65535.

- A started server now announces its listeners in `config.applicationDescription.discoveryUrls`: `opc.tcp://<hostname>:<port>` for all interfaces, or the configured host. GetEndpoints, FindServers and ReverseHello now carry a DiscoveryUrl, and `Server.registerDiscovery()` is no longer rejected with `Bad_DiscoveryUrlMissing`.

- `Server.registerDiscovery()` now defaults to SignAndEncrypt with Basic256Sha256 when the server has a certificate, and verifies the LDS certificate with the server's trust configuration. Without a certificate it uses SecurityPolicy#None. `deregisterDiscovery()` uses the same security; it defaulted to SignAndEncrypt without a certificate, and the open62541 discovery client then opened thousands of SecureChannels per second at the LDS until the server stopped. Both take `securityMode=` and `securityPolicy=`, and a request that does not complete within 5 seconds is cancelled. The docstrings now state that both calls only start the request and log the answer.

- `str(StatusCodeError)` now names the status and its code, such as `BadSecurityChecksFailed (0x80130000)`, instead of the decimal code or the `StatusCode` member name. Code that matches the message text should compare `error.code` or `error.symbol` instead.

- `Client(securityPolicy=...)` and `client.config.securityPolicy` now accept the documented short names, such as `"Basic256Sha256"`, in any case and with or without `_`, and store the full URI. An unknown short name raises `ValueError` instead of failing the connect with a misleading `Bad_IdentityTokenRejected`. `o6.SecurityPolicy` also lists the ECC policy URIs.

- A server now identifies itself as o6-python instead of open62541. `Server/ServerStatus/BuildInfo` (`i=2260`) reports ProductName `o6-python`, ManufacturerName `o6 Automation GmbH` and the o6 version; o6 had written its BuildInfo to the ServerStatusType declaration (`i=2142`) instead. GetEndpoints, FindServers and LDS registrations announce the ApplicationName `o6-python Server`. Both use the ProductUri `https://o6-automation.com/o6-python`.

- `Client.connect(noSession=True)` now completes once the SecureChannel with the requested security is open. With encryption, it completed on the unencrypted channel used for GetEndpoints, so requests sent right after the connect, such as RegisterServer2 or FindServers, went unencrypted.

- A client connect that fails before any network activity, for example on a pinned endpoint whose policy the client lacks, no longer makes asyncio log "Future exception was never retrieved".

- Servers with RSA certificates now offer the three supported RSA security policies without spurious ECC warnings. Endpoints list each user token policy once. Invalid private keys raise `StatusCodeError` instead of prompting for a password, and failed `config.setEncryption()` calls preserve the server configuration.

- Username/password login now supports encrypted password tokens without a client application certificate; it previously failed with `BadIdentityTokenRejected` on such endpoints. This does not authenticate the server or encrypt the channel. Configure `certificate`, `privateKey` and `trustList` for server authentication, and `SIGN_AND_ENCRYPT` for message protection. `connect()` also applies certificate settings changed after construction.

<p>&nbsp;</p>
<p>&nbsp;</p>

## 2.2.0

### New Features

- Added bundled namespaces for CNC, DI package metadata, FDT, plastics dosing and foam cutting, surface cleaning and multi-stage systems, and unattended retail.

- Client `browsePage`/`browseNext` and shared path-translation helpers match server browsing contracts.

- Client `addObject`/`addVariable` return typed handles with server-style inputs; both conveniences accept `parentReference` and default to `Organizes`.

- `server.loop` exposes the server's owning asyncio event loop as a read-only property.

- `Client.connect(createDefaultSubscription=False)` opens a session without requiring subscription support or capacity.

- `Client.invalidateNodeCache(node)` clears cached child navigation; omit `node` to invalidate all handles.

- Servers expose typed `server[nodeId]` lookup and `root`, `objects`, `types`, and `views` folder handles, preserving node identity and application state; await indexing in async tasks.

- Python history backends can serve pages through `getHistoryPage`, including token release and session validation.

### Improvements

- The Server SDK is now considered stable; removed the beta warning from startup banners and documentation.

- Event-monitoring callback types and guides describe path-string payload keys, including nested fields.

- `MonitoredItem.requestedParams` exposes the original creation settings; configuration snapshots also isolate nested filters.

- Clarified value conversion, namespace mapping, and API behavior in the guides and examples, and repaired reference links.

### Bug Fixes

- Value-only client/server reads and callable nodes accept all Good-severity statuses; use `valueOnly=False` to inspect status and timestamps.

- Scalar `write(node, None)` now matches batch null writes; callable local nodes return `None` when reading an accepted null value.

- Variables added with `historizing=True` to a running server register for history immediately; failed registration removes the new node.

- Variable creation accepts typed empty NumPy arrays and explicitly typed empty sequences, retaining the datatype and declared ValueRank.

- Automatic datatype discovery preserves string, GUID, and opaque NodeIds, follows every browse page, and reports read failures.

- Client child-navigation caches refresh after client mutations, reconnects, namespace updates, explicit browsing, and cached misses.

- Callable local nodes preserve DataValue status and timestamp metadata, matching client nodes.

- Client node creation and history failures preserve `StatusCodeError.code`; batch history errors identify the failed target in exception notes.

- Node lookup validates service and attribute results; malformed responses raise `RuntimeError`.

- `Server.historize()` and `unhistorize()` work in async code and restore node attributes when history configuration fails.

- Calling `Server.stop()` from its worker loop no longer blocks shutdown; async worker callbacks can await the returned task.

- Repeated `Server.deleteMonitoredItem(handle)` calls remain awaitable in async code.

- Client monitored items retain accepted filters, discard policies, monitoring modes, and server-revised parameters across partial modifications.

- Async client monitoring and subscription lifecycle callbacks now run on the client loop and log failures.

- Monitoring rejects subscriptions owned by another client; triggering links reject foreign, uninitialized, or deleted items before sending requests.

- `Server` now raises `ValueError` for incomplete or empty certificate/key pairs and for `secureOnly=True` without credentials.

- Encrypted servers preserve the constructor's `applicationUri` in configuration and discovery responses.

- `deleteNode([])` returns `[]` without a deletion request on both client and server.

- `Client.deleteReference()` now preserves the namespace URI and server index of `ExpandedNodeId` targets.

- `Client.addReference()` and `deleteReference()` service failures now raise `StatusCodeError` instead of `ValueError`, preserving the status code.

- Browsing attempts to release outstanding continuation points on failure or cancellation, including tokens returned during client cancellation.

- `Client.call()` service failures now raise `StatusCodeError` with the original status available in `.code`.

- Remote typed Method calls now raise `StatusCodeError` for failed method results, matching local calls and the documented behavior.

- `Server.read()` now matches client read options, including raw DataValues and timestamp selection (SOURCE by default); explicit attributes use `attr=`.

- Read service and value-only batch failures consistently raise `StatusCodeError`, preserving status codes and identifying failed batch entries.

- Server-local monitored items report their actual target, mode, filter, and revised settings; ID-only handles explicitly report unavailable metadata.

- Unsupported local `modify()`, `setMonitoringMode()`, and `setTriggering()` calls raise `NotImplementedError` without changing the item.

- `Server.write()` with a `DataValue` now honors the requested attribute and rejects unsupported combinations without overwriting Value.

- Awaiting server node creation from another event loop now returns a usable, fully configured handle and preserves creation errors.

- Fixed crashes when awaiting `Server.browse()` with typed nodes; async calls now consistently require `await` for both Node and NodeId targets.

- Synchronous server startup and asynchronous context entry wait for listening sockets and raise bind failures. Asynchronous callers of `start()` can await `waitReady()` before connecting clients.

- Servers can restart after shutdown with active or pending TCP connections.

- Namespace publication can be retried after a failure without recreating completed nodes or rerunning their initializers.

- Role equality is consistent with hashing; name-only roles remain usable in permission APIs but are distinct from resolved roles.

- Failed subscription and monitored-item deletions preserve retry handles; native deletion clears client handles, and subscription modifications retain accepted settings.

- Server-local monitored-item handles become invalid after numeric deletion or server cleanup; foreign handles and out-of-range numeric IDs are rejected before deletion.

- Repeated value encoding and decoding no longer leak datatype references, field names, or partially converted values.

- Range reads retain error statuses in raw DataValues and raise on invalid or out-of-bounds value-only reads.

- `historyRead` follows server-issued pages and releases unused continuation points on limits, failure, or cancellation.

- Writes through `node(value)` now raise `StatusCodeError` when the server rejects them.

- Node introspection no longer blocks its own event loop during interactive completion.

- Client and server callback cycles are collected, including Python plugins and pending requests.

- Cancelled client requests no longer raise errors when their responses arrive.

- Namespace conversion preserves native values during callbacks and repeated datatype lookups.

- Fixed Python 3.11 reference-count corruption during value conversion, DateTime comparisons, and timer callbacks.

- DateTime comparisons with unrelated types now follow Python comparison semantics.

- Empty union values no longer crash namespace conversion.

- Deleting optional DataValue or DiagnosticInfo fields clears them safely; deleting required native properties raises `AttributeError`.

- `Client.read` now honors `timestampsToReturn`.

- Newly created subscriptions report the publishing interval, lifetime, and keepalive count revised by the server.

- Fixed memory leaks during binary/JSON decoding, `DataValue.value` access, and structure formatting.

- Non-type codec datatype arguments, oversized DateTime strings, invalid Guid byte lengths, and invalid string inputs are now rejected safely.

- Async method, read, and write callbacks run on the server event loop and may suspend; shutdown cancels pending callbacks.

- Fields declared with an abstract structured DataType accept concrete subtype values.

### Breaking Changes

- Commercial wheels without a valid Credential now use ten-minute Script Mode instead of the two-hour evaluation period; commercial use is permitted in Script Mode.

- Async tasks must await local server creation, node calls, dynamic child lookups, reference mutations, reverse-connect, discovery, and dataset operations, even for immediate results; synchronous SDK callbacks retain their nonblocking behavior.

- Client credentials no longer enable plaintext password tokens implicitly; configure encryption or explicitly set `allowNonePolicyPassword=True`.

- Startup raises for pending history registrations without a configured database or when registration fails, retaining pending entries for retry.

- `Client.getEndpoints()`, `findServers()`, and `findServersOnNetwork()` raise `StatusCodeError` for service failures instead of returning empty lists; raw discovery services still return full responses.

- Non-Value writes require the attribute's expected datatype on client, server, and callable nodes; use `LocalizedText` for Description and `numpy.uint8` for AccessLevel. Ordinary Value writes retain type inference.

- Client non-Value writes reject DataValue status/timestamp metadata with `BAD_WRITE_NOT_SUPPORTED` instead of allowing it to be discarded.

- Unknown `client[nodeId]` lookups raise `StatusCodeError(BAD_NODE_ID_UNKNOWN)` instead of `KeyError`, matching server lookup; local disconnected-client checks and malformed responses raise `RuntimeError`.

- `Client.deleteNode()` and `Server.deleteNode()` return a list of per-target statuses for batch calls instead of one aggregate status; scalar calls return one `StatusCode`.

- Rename the server deletion keyword `deleteReferences` to `deleteTargetReferences`, and await `deleteNode()` inside async tasks.

- `Client.deleteNode()` service failures now raise `StatusCodeError` instead of `ValueError`.

- `addReference()` and `deleteReference()` now use `(source, reftype, target)` and `deleteBidirectional`, return `StatusCode`, and require `await` in async tasks; use `addReferenceLegacy()` / `deleteReferenceLegacy()` to retain the old contract.

- `Server.browse()` now returns a complete list of references, matching `Client.browse()`; remove `.references` access and move `maxReferences=` calls to `Server.browsePage()` for explicit pagination.

- `Client.browse()` failures now raise `StatusCodeError` instead of `ValueError`; `Server.browseNext()` now raises `StatusCodeError` for failed page statuses.

- `Server.call()` now returns `(status, *outputs)` for method failures, matching `Client.call()`; use `status.check()` to retain exception-based handling.

- `Server.write()` now accepts parallel target/value lists or a mapping; replace broadcast calls with `write(nodes, [value] * len(nodes))` and pass attributes with `attr=`.

- `Server.write()` returns one status or an ordered list of statuses and continues batches after individual failures; check results with `status.check()` to retain exception-based handling.

- `Client.write()` service failures now raise `StatusCodeError` instead of `ValueError`.

### Known Issues

- Malformed binary union values can crash the underlying SDK decoder; an upstream fix is required.

<p>&nbsp;</p>
<p>&nbsp;</p>

## 2.1.0

### New Features

- `Server.createEvent()` emits immediately, matching the C SDK, with
  `emitEvent()` as an alias. Construct reusable drafts with `o6.Event(server, ...)`
  and emit them with `trigger()`.

- When `eventType` is omitted, emission uses the type of `eventInstance` if
  supplied; otherwise, the source's type definition is browsed for a
  `GeneratesEvent` reference, and that EventType is used.

  ```python
  server.addReference(
      source=o6.NodeId(PumpType),
      reftype=ns0.reftypes.GeneratesEvent,
      target=o6.NodeId(PumpFaultType),
  )
  pump = PumpType(parent=server.objectsNode, browseName="Pump1")

  server.createEvent(source=pump, message="Cavitation detected")   # PumpFaultType
  ```

  Without an event instance, a type declaring no `GeneratesEvent` target falls
  back to `BaseEventType`. A type declaring more than one, or a source with no
  type definition at all, raises `ValueError`. Passing `eventType=` explicitly
  selects the type argument. An `Event` draft resolves it at each `trigger()`.
  Field values retain C's precedence: explicit fields, instance properties,
  then emission defaults.

- `ObjectNode` and `ViewNode` fire an event sourced at themselves with `<<`,
  without going back to the owning `Server`:

  ```python
  pump << o6.Event(server, message="Cavitation detected")
  pump << {"message": "Cavitation detected", "severity": 400}
  pump << eventInstance
  pump << {"eventInstance": eventInstance}
  ```

  An event instance must be an Object of `BaseEventType` or a subtype on the
  same server; emission reads its current fields without modifying the node.

- Variable read and write callbacks may be `async def`, matching Method
  callbacks:

  ```python
  @o6.read
  async def _read(self, **kwargs):
      return (o6.StatusCode.GOOD, await self.device.readTemperature())
  ```

  A coroutine that returns without awaiting completes synchronously. One that
  awaits leaves the operation pending and completes it when the coroutine
  finishes; server shutdown cancels it. This previously raised
  `TypeError: Variable callbacks cannot be async`.

- `@o6.enumtype` supports declaring more than 255 members. This previously
  failed registration outright:

  ```python
  RuntimeError: UA_DataType_fromEnumDescription failed: BadEncodingLimitsExceeded
  ```

  This unblocks `o6.ns.bacnet`, whose `BACnetPropertyIdentifier` declares 396.

- Server-side historizing is added. `historizing=True` on
  `addVariable` used to only set the `Historizing` attribute; once
  `server.config.setHistoryDatabase(...)` is configured, it registers the
  Variable too:

  ```python
  server.config.setHistoryDatabase(capacity=100)
  server.addVariable("Level", plant, 0.0, historizing=True)
  ```

  `historizing=o6.History(capacity=, strategy=, interval=)` customizes
  capacity and sampling strategy per Variable; `server.historize(target, ...)`
  / `unhistorize(target)` do the same for a node this server didn't create.

- Server and client application notifications are exposed as handler
  registries. Each `server.on<Category>Notification` — `Lifecycle`,
  `SecureChannel`, `Session`, `Service`, `Subscription`, `MonitoredItem`,
  `DiscoveryRegisterServer`, `DiscoveryServerOnNetwork` and `Audit` — is a
  list-like registry usable as a decorator, assignable as a whole, and
  changeable while the server runs:

  ```python
  @server.onSessionNotification
  def _audit(notification):
      print(notification.type, notification.payload)
  ```

  The client side offers `onLifecycleNotification`, `onServiceNotification`,
  and `onGlobalNotification`, which sees every notification the connection
  produces. A handler on either side receives an `o6.Notification` carrying
  `type` and `payload`, a read-only `str -> Any` mapping of that
  notification's fields.

- `Server.addSubscribedDataSet(name, metadata, targets)` creates a native
  standalone subscribed DataSet, and `removeSubscribedDataSet(dataSetId)`
  removes it. This defines the dataset without creating or enabling a
  `DataSetReader`.

- `ServerConfig.maxSubscriptions` and `ServerConfig.maxSubscriptionsPerSession`
  cap the number of subscriptions across all sessions and within one session:

  ```python
  server.config.maxSubscriptions = 50
  ```

### Improvements

- `Server.createEventMonitoredItem` raises `ValueError` when the effective
  `EventFilter` has no select clauses, instead of letting the server answer
  `BadEventFilterInvalid`.

- The server manual gains a tutorial series covering type declaration, method
  implementations, variables with sources, callbacks, events and timers,
  access control, security policies, monitoring and history.
- History reads now support continuation points for paging large result sets.
  Use `client.serviceHistoryRead()` with `HistoryReadValueId.continuationPoint`
  to resume reading from where the previous batch ended.

### Bug Fixes

- An OPC UA enumeration is a Python `enum.IntEnum`, an OptionSet an
  `enum.IntFlag`, chosen by the declaring decorator. An enumeration no longer
  drops a member valued zero, or one whose value is the sum of two others, from
  iteration, `dir()` and `repr`:

  ```python
  list(ApplicationType)   # all four members, not two
  ```

  Members consequently compose as integers: `A | B` is a plain `int` rather than
  a member, and `issubclass(SomeEnum, enum.Flag)` is `False`. OptionSets are
  unchanged — in ns0, 48 enumerations change and 19 OptionSets do not.

- An enumeration value outside the declared set decodes instead of raising, so
  one out-of-specification field no longer fails the read containing it. The
  value is preserved as sent, including a negative one:

  ```python
  BrowseResultMask(12).name   # None
  int(BrowseResultMask(12))   # 12
  ```

- `value in SomeType` now answers the same question on every supported
  interpreter, for both enumerations and OptionSets — including `StatusCode`.
  On 3.13+, an expression like `99 in SomeOptionSet` used to answer `True` for
  every integer; it now discriminates. On 3.11, the same kind of expression
  used to raise `TypeError`; it now answers instead:

  ```python
  999999 in AccessLevelType   # False, not True (3.13+) or TypeError (3.11)
  ```

- A notification payload no longer reports a corrupted namespace index for the
  node it concerns. The conversion borrowed the native namespace index rather
  than copying it, so a monitored `NodeId` could surface under the wrong
  namespace once the native value was released.

- A default `DisplayName` derived from a `BrowseName` no longer carries the
  namespace qualifier:

  ```python
  machine = Machine(server=server, parent=server.objectsNode, browseName="ns=plant;Machine")
  machine(attr=o6.AttributeId.DISPLAY_NAME)   # "Machine", not "ns=plant;Machine"
  ```

  An explicitly passed `displayName` is preserved unchanged.

- Building from source on Windows no longer fails on a backslashed nodeset
  directory path handed to CMake.

<p>&nbsp;</p>
<p>&nbsp;</p>

## 2.0.3

### New Features

- `@o6.optionsettype` and `o6.bitmask` declare an integer-form OPC UA OptionSet.
  Members are bit masks, and `base=` names the unsigned integer the OptionSet
  subtypes — it carries the wire width and the `HasSubtype` parent, and is
  mandatory:

  ```python
  @o6.optionsettype(ns="plant", base=o6.Byte)
  class AccessLevelType:
      CURRENT_READ = o6.bitmask(0x01 << 0, name="CurrentRead")
      HISTORY_WRITE = o6.bitmask(0x01 << 3, name="HistoryWrite")
  ```

  Bit fields declared with `@o6.enumtype` should move to it; `@o6.enumtype` now
  rejects `o6.bitmask` members, and `@o6.optionsettype` rejects `o6.enumfield`.

- `o6.optionsetbit` declares one bit of a structure-form OptionSet — an
  `@o6.datatype` subtyping the ns0 `OptionSet`. Reading a bit is three-valued
  (`None` when `ValidBits` says the bit means nothing); assigning writes `Value`
  and `ValidBits` together. Generated structure-form OptionSets now carry one
  accessor per declared bit instead of leaving the two ByteStrings to be
  hand-masked.

### Improvements

- The client's limit on concurrent service calls is now configurable through
  `client.config.maxAsyncServiceCalls` (default `32`, `0` disables it). Like
  all `client.config` fields, it must be set before `connect()`.
- Reusing send buffer improves async throughput by ~25% 

### Bug Fixes

- Synchronous client calls no longer hang forever when the event loop passed as
  `Client(loop=...)` is not being run; they are driven to completion inline.
  Callbacks (data change, event, state) are still only delivered while that loop
  runs.
- OptionSet-typed structure fields now surface as their flag class on read-back,
  in every namespace including ns0.
- `del instance.member` on a generated structure no longer crashes the
  interpreter; it raises `AttributeError`, since a structure member always has a
  value on the wire. `instance.__dict__` and `vars(instance)` now answer with a
  dictionary instead of raising, so debuggers and generic introspection work on
  structure instances.
- `import o6.ns.<x>.datatypes` no longer executes the module body twice.
- `Argument.dataType` resolved to the wrong namespace in several regenerated
  packages; it now points at the specification the argument's namespace
  actually intends:

  | namespace | was | is |
  |---|---|---|
  | `additive_manufacturing`, `cutting_tool` | `ns=dexpi;i=3006`, `ns=dexpi;i=3013` | `ns=isa95_jobcontrol_v2;i=3006`, `ns=isa95_jobcontrol_v2;i=3013` |
  | `glass_flat_v2` | `ns=aml;i=3006`, `ns=aml;i=3013` | `ns=isa95_jobcontrol_v2;i=3006`, `ns=isa95_jobcontrol_v2;i=3013` |
  | `machine_tool`, `shotblasting`, `surface_technology_plasma`, `woodworking` | `ns=bacnet;i=3006`, `ns=bacnet;i=3013` | `ns=isa95_jobcontrol_v2;i=3006`, `ns=isa95_jobcontrol_v2;i=3013` |
  | `machinery_jobs` | `ns=amb;i=3006`, `ns=amb;i=3013` | `ns=isa95_jobcontrol_v2;i=3006`, `ns=isa95_jobcontrol_v2;i=3013` |
  | `wire_harness` | `ns=amb;i=3008`, `ns=amb;i=3010` | `ns=isa95_jobcontrol_v2;i=3008`, `ns=isa95_jobcontrol_v2;i=3010` |
  | `gms` | `ns=amb;i=3005`, `ns=amb;i=3008` | `ns=machinery_result;i=3005`, `ns=machinery_result;i=3008` |
- Integer-form OptionSet member values are now masks, not bit positions. Applies
  to every integer-form OptionSet, including `AccessLevelType`,
  `AttributeWriteMask` and `PermissionType`. Ordinary `@o6.enumtype`
  enumerations are unaffected.

  If a value relied on the previous bit position, drop the extra shift:

  ```python
  # before — double-shifted because members were bit positions
  value = 1 << int(my_flag) | 1 << int(my_other_flag)

  # after — members are masks
  value = my_flag | my_other_flag
  ```

- The wire format of five struct fields is now correct against conformant
  equipment. Sizes are in bytes, measured against the same NodeSet on
  each release:

  | field | declared base | v2.0.2 | now |
  |---|---|---|---|
  | `safety.RequestSPDUDataType.inFlags` | Byte | 4 | 1 |
  | `safety.ResponseSPDUDataType.outFlags` | Byte | 4 | 1 |
  | `fx_ac.AggregatedHealthDataType.aggregatedDeviceHealth` | UInt16 | 4 | 2 |
  | `fx_cm.ConnectionDiagnosticsDataType.lastActivity` | UInt16 | 4 | 2 |
  | `machinery_jobs.OutputInformationDataType.outputInfo` | Byte | 4 | 1 |

- `o6.AccessLevel`, `o6.WriteMask` and `o6.Permission` are retired. They aliased
  generated NS0 OptionSet DataTypes; the generated types are now the only spelling.

  | before | after |
  |---|---|
  | `o6.AccessLevel` | `o6.ns.ns0.datatypes.AccessLevelType` |
  | `o6.WriteMask` | `o6.ns.ns0.datatypes.AttributeWriteMask` |
  | `o6.Permission` | `o6.ns.ns0.datatypes.PermissionType` |

<p>&nbsp;</p>
<p>&nbsp;</p>

## 2.0.2

### Improvements

- New documentation site at <https://docs.o6-automation.com/o6-python/>, with a
  restructured manual, client and server tutorials, a full API reference, and
  performance benchmarks.
- The PyPI project page now renders the package documentation and links to the
  docs site.

### Bug Fixes

- `@o6.enumtype(isAbstract=True)` no longer crashes on Python 3.11 (the
  abstract-enum path used a functional-API call shape that 3.12's
  `enum.IntFlag` accepts but 3.11 rejects).

### Breaking Changes

- Generated type names starting with a digit are spelled out instead of
  `_`-prefixed: `_3DVector` becomes `ThreeDVector`, `_3DFrameType` becomes
  `ThreeDFrameType`, and so on for all `_3D*` types in `ns0` and the companion
  specs. This matches the OPC UA type dictionary and open62541. Enum members are
  unaffected and keep their `_16_BIT` spelling.

<p>&nbsp;</p>
<p>&nbsp;</p>

## 2.0.1

### Distribution

- Public `o6` wheels contain the full Client and Server API.
- Without an issued Credential, the public wheel runs in the existing two-hour
  evaluation mode. Its process-wide timer starts when `o6` is imported; a valid
  Credential removes the time limit. Expiry terminates the process with a
  failure exit status; POSIX expiry is an immediate signal-safe hard exit.
- An unreadable, malformed, incorrectly signed, not-yet-valid, or expired
  Credential prints the reason and falls back to evaluation mode instead of
  failing import. Fallback warnings remain visible when routine startup output
  is suppressed, as do the Trial Mode and expiry notices.
- Commercial builds use `O6PYTHON_LICENSE_FILE` when set; otherwise they check
  `o6python_license.json` in the current working directory. AGPL builds do not
  use Credentials or evaluation mode. A missing configured path warns; a
  missing default file proceeds directly to the Trial Mode message.
- Credential Feature Scopes independently control `client`, `server`, and
  `pubsub`; PubSub requires Server. Compiled symbols remain importable, while
  unauthorized construction or PubSub operations raise `PermissionError`.
  PubSub-disabled Servers omit the native PubSub manager, information-model
  methods, and transports.
- Standard GIL-enabled CPython 3.11–3.14 is supported on Linux and macOS
  `x86_64`/ARM64 and Windows AMD64/ARM64.
- Linux wheels require glibc 2.28 or newer (`manylinux_2_28`).
- macOS wheels require macOS 15 Sequoia or newer.
- Windows AMD64 supports Windows 10 Enterprise LTSC 2021 and Windows Server
  2022 or newer; Windows ARM64 supports Windows 11 or newer.
- Supported NumPy versions are `>=2.0,<3`; the native extension targets the
  NumPy 2.0 C API and is tested with minimum and current NumPy 2.x releases.

### API organization

- Added explicit public exports for `o6` and its public modules.
- Moved subscription classes to the canonical `o6.subscription` module and
  callback protocols and contexts to `o6.server`; the previous paths have
  been removed.
- Made declaration, decorator, reference, datatype-registration, and node
  backend implementation paths private without changing the supported root
  authoring helpers.
- Standardized public methods, properties, parameters, and model members on
  lowerCamelCase (`nodeId`, `browseName`, `addVariable`, `encodeJson`). Types
  remain PascalCase and decorators remain lowercase compounds. Previous public
  spellings have been removed rather than retained as compatibility aliases.
- Grouped companion-spec symbols under each namespace's `datatypes`,
  `objtypes`, `vartypes`, `reftypes`, and `instances` modules instead of
  flattening them onto the namespace object.
- Standardized datatype-discovery result keys on lowerCamelCase (`typeName`,
  `typeId`, `binaryEncodingId`, `typeKind`, `structureType`, `membersSize`).

### Breaking Changes

- `o6.ns.<ns>.datatypes.<X>()` now **instantiates** the concrete datatype. 

    | | returns |
    | --- | --- |
    | `o6.Int32()` | `numpy.int32(0)` |
    | `o6.nsx.ns0.BaseDataType.Structure.Argument()` | `o6.Argument` |

    To obtain the NodeId, use `o6.NodeId(o6.ns.<ns>.datatypes.<X>)`. 
    Abstract datatypes (e.g. `BaseDataType`, `Number`, `Integer`) will throw when tried to instantiate.

- struct members caml vs. snake case. 

    In order to be PEP8 compliant previous versions converted member names of UA Structs and DataTypes to snake case naming convention.
    For better clarity, we are dropping this conversion and replacing these member names with their official names from the UA Namespace 0 and companion specs.
    In order to adhere closer to PEP8 we allow a single exception to the UA naming convention:
    the first character may be lower case for class members of python classes, that represent UA DataTypes and Structs.

- enum members are consequently converted to capitalized snake case

- `dir()` on a node lists instance children in lowerCamelCase

    Browsing a node now surfaces its Object, Variable, Method and View children under the
    lowerCamelCase name derived from their BrowseName, so completion offers
    `client.objects.server.serverStatus` instead of `ServerStatus` — the same spelling that
    generated declarations already use for their members. Type children (ObjectType,
    VariableType, ReferenceType, DataType) keep their PascalCase BrowseName.
    Dot access remains case-insensitive, so `client.objects.server.ServerStatus` still resolves.

### New Features

- OPC UA Browser, now built in feature of the `o6.Client` available through `client.browseInteractive`
- Cleaned up Client API
    * removed `client.fully_connected`, `client.connected` is now only true when there's a secure channel and a session
    * removed `client.disconnect_secure_channel` in favor of `client.disconnect()` parameters `closeSession` and `deleteSubscriptions`
    * added range parameter for `client.read` and `client.write`, that lets one read into a slice of an array variable with e.g. "1:10"
    * StatusCode is now a proper Python `IntFlag` with full bitwise support:
        ```python
        if o6.StatusCode.Bad in status_code:
            #...

        my_status_code = o6.StatusCode.Good | o6.StatusCode.UncertainLastUsableValue
        ```
    * added support for browse continuation point, i.e. `client.browse` now guarantees to return the complete list of references
    * cleand up and simplified history access through the client
    * revised the client node-management function parameters and added useful defaults for
        + `parentReference` - `o6.ns.ns0.hasComponent`
        + `typeDefinition` - `o6.ns.ns0.objtypes.BaseDataVariableType`
    * added callbacks for subscriptions
        + `onCreated` - fires when this subscription was created on the server
        + `onStatusChange` - fires when the server reports a status change for this subscription (e.g. keepalive timeout exceeded, session transfer on reconnect), receives the new `StatusCode`
        + `onDeleted` - fires when this subscription was deleted on the server
    * added callbacks for monitored item
        + `onCreated` - fires when this monitored item was created on the server
        + `onDeleted` - fires when this monitored item was deleted on the server

### Bug Fixes
