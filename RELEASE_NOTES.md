# Release Notes

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
