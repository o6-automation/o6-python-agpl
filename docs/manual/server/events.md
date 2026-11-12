# Events

Emit application events for clients or local monitored items to observe.

## Events

Emit an event immediately with `server.createEvent(...)` (alias
`server.emitEvent(...)`), or build a reusable Python draft with `o6.Event`:

```python
event = o6.Event(
    server,
    eventType=ns0.objtypes.BaseEventType,
    source=server.serverNode,
    message="Production started",
    severity=200,
)
event["/Severity"] = o6.UInt16(300)
eventId = event.trigger()
```

Field keys name fields of the event type: a BrowseName such as `"Severity"`,
a path such as `"/Severity"`, or a `QualifiedName`. See
[Event fields](#event-fields). Explicit fields use open62541's fast event-field
map. An `Event` is a mutable mapping:
`dict(event)`, `len(event)`, `del event[key]` and iteration work. You can
reassign its `eventType`, `source`, `message`, `severity` and `fields`
attributes between triggers.

An existing Object node can also supply the payload. Fields missing from the
explicit map are then read from that instance:

```python
event.eventInstance = machineEventInstance
event.trigger()
```

Resolution order is explicit `event.fields`, then `eventInstance`, then the
standard `BaseEventType` defaults. `trigger()` returns the generated 16-byte
`EventId`.

This follows open62541's field precedence, also for `EventType` and
`SourceNode`. A stored property wins over the matching emission argument, even
a null NodeId on a newly created instance. Set these properties when you
prepare the instance, or override them in `fields`. If the properties are
absent, the SDK uses the emission arguments:

```python
machineEventInstance.EventType(o6.NodeId(MyEventType))
machineEventInstance.SourceNode(o6.NodeId(pump))
pump << machineEventInstance
```

`createEvent` emits without a draft and returns the `EventId`, like
open62541's `UA_Server_createEvent`. `emitEvent` is an alias:

```python
eventId = server.createEvent(
    ns0.objtypes.BaseEventType,
    source=server.serverNode,
    message="Shutdown requested",
    severity=500,
)
```

Both raise `ValueError` for a `severity` outside the OPC UA range `1..1000`.
`source` defaults to the Server object, so `server.createEvent(message="...")`
is a valid minimal call. To let clients subscribe directly to a custom source,
set the SubscribeToEvents bit of its `EventNotifier`. Events also reach the
standard Server object.

`o6.Event(server, ...)` builds the draft without emitting or accessing the
address space. `createEvent`, `emitEvent` and `trigger()` return
`MaybeAwaitable[bytes]`; callers on another asyncio loop must await the
result.

### Event fields

A client selects an event field by the BrowseNames on its path from the event
type, for example `SELECT /Message` or `SELECT /2:BatchId` with the server's
namespace index. The keys of `fields` name the same fields in any of these
forms:

- The BrowseName of a field of the event type or a supertype, such as
  `"BatchId"` or `"Message"`. It must be unique among the fields by name.
- A path of BrowseNames, such as `"/Message"`, `"/plant:BatchId"` or
  `"/EnabledState/Id"`. A segment names its namespace with a registered
  shortname or a process-wide namespace index, like
  [`QualifiedName`](../sdk-fundamentals/builtin/address-types.md#qualifiedname)
  and `NodeId`; without a prefix it is in namespace 0. An optional `#Attribute`
  or `[IndexRange]` suffix is kept.
- A `QualifiedName`, such as `o6.QualifiedName("ns=plant;BatchId")`. A name
  starting with `/` is a path whose unprefixed segments are in the
  QualifiedName's namespace, as in open62541.

```python
@o6.objecttype(ns="plant", browseName="BatchEventType")
class BatchEventType(ns0.objtypes.BaseEventType):
    BatchId: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(browseName="ns=plant;BatchId", dataType=o6.String)
    )

server.createEvent(BatchEventType, message="Batch started", fields={"BatchId": "B-1042"})
# Equivalent keys: "/plant:BatchId", o6.QualifiedName("ns=plant;BatchId")
```

The fragment assumes that the `plant` namespace is registered and
`BatchEventType` is published, see
[Information Model Authoring](../information-model-authoring/index.md).

Each emission resolves field names against the current event type and
translates namespace prefixes to the server's namespace indexes. A path
does not have to be declared by the event type: the field travels with the
event, and a client that selects the same path receives it. A key that is
likely a mistake emits a `UserWarning` once per event type. The warning
reports the key used in the emitted event:

- a BrowseName that names no field, or several fields in different
  namespaces;
- a prefix that is not a registered shortname, or a namespace that is not
  published on the server;
- a one-segment path that names no field while a field of that name exists in
  another namespace. `"/BatchId"` names a field in namespace 0 and warns with
  a hint to `plant:BatchId`.

Keys that start with a TypeDefinitionId or contain escapes are used unchanged.

### Inferring the event type

`eventType` defaults to `None`. The SDK's type argument is chosen in this
order:

1. Explicit `eventType`.
2. `eventInstance`'s `HasTypeDefinition`, when supplied.
3. `source`'s declared `GeneratesEvent` target.

Field resolution still follows the precedence above.

When the source type has exactly one `GeneratesEvent` reference to an
EventType, that EventType is used. The following model fragments assume the
`plant` namespace is registered and their types are published before calling
`addReference` or creating instances. Declaration and publication are covered
in [Information Model Authoring](../information-model-authoring/index.md):

```python
@o6.objecttype(ns="plant", browseName="PumpFaultType")
class PumpFaultType(ns0.objtypes.BaseEventType):
    pass

@o6.objecttype(ns="plant", browseName="CavitationFaultType")
class CavitationFaultType(ns0.objtypes.BaseEventType):
    pass

@o6.objecttype(ns="plant", browseName="PumpType")
class PumpType(ns0.objtypes.BaseObjectType):
    pass

server.addReference(
    source=o6.NodeId(PumpType),
    reftype=ns0.reftypes.GeneratesEvent,
    target=o6.NodeId(PumpFaultType),
)
pump = PumpType(parent=server.objectsNode, browseName="Pump1")

eventId = server.createEvent(source=pump, message="Cavitation detected")
# eventType resolved to PumpFaultType, no eventType= needed
```

A type with no `GeneratesEvent` target falls back to `BaseEventType`. The
`server.createEvent(message="...")` call above resolves this way, because the
Server object's type declares none. A type with more than one `GeneratesEvent`
target raises `ValueError` naming the ambiguity:

```python
@o6.objecttype(ns="plant", browseName="ValveType")
class ValveType(ns0.objtypes.BaseObjectType):
    pass

server.addReference(
    source=o6.NodeId(ValveType),
    reftype=ns0.reftypes.GeneratesEvent,
    target=o6.NodeId(PumpFaultType),
)
server.addReference(
    source=o6.NodeId(ValveType),
    reftype=ns0.reftypes.GeneratesEvent,
    target=o6.NodeId(CavitationFaultType),
)
valve = ValveType(parent=server.objectsNode, browseName="Valve1")

server.emitEvent(source=valve, message="which fault?")
# ValueError: cannot infer eventType: type ... declares more than one
# GeneratesEvent target; pass eventType= explicitly
```

Without an explicit type or event instance, a `source` with no type definition
also raises `ValueError`. For either error, pass `eventType=`; it wins over
anything `source`'s type declares.

Inference reads the live information model. A `GeneratesEvent` reference added
or removed at runtime takes effect on the next `createEvent` or `trigger()`. A
reusable `Event` draft resolves the type on every trigger, so a reassigned
`eventInstance` or `source` takes effect on the next trigger. Inference leaves
the draft's `eventType` attribute as `None`.

### Firing an event from a Node handle

An Object or View node handle fires an event with itself as source using `<<`.
You don't need the owning `Server` or `source=`:

```python
pump << o6.Event(server, message="Cavitation detected")
```

For a one-off event, `<<` also accepts a plain mapping instead of an `Event`
draft:

```python
pump << {"message": "Cavitation detected", "severity": 400}
```

Pass an existing event instance directly, or as `eventInstance` in a mapping
or draft:

```python
pump << machineEventInstance
pump << {"eventInstance": machineEventInstance}
pump << o6.Event(server, eventInstance=machineEventInstance)
```

The instance must be an Object of `BaseEventType` or a subtype, on the same
server. Its current fields are read on every emission. The node is not modified
or deleted. To override a field for one emission:

```python
pump << {
    "eventInstance": machineEventInstance,
    "fields": {"/Message": o6.LocalizedText("Override for this emission")},
}
```

All forms emit from `pump`, the same as `server.createEvent(source=pump, ...)`.
`<<` does not change a draft's own `source` field, so you can fire the same
draft at another node later.

`<<` is defined only for Object and View nodes, the only NodeClasses with an
`EventNotifier` attribute. `variable << o6.Event(...)` raises `TypeError`
immediately, naming the reason. A node handle from a `Client` also raises
`TypeError`, because local event creation is server-only.

`<<` returns a `MaybeAwaitable[bytes]` like `emitEvent`. On a server running on
an external asyncio loop, await it with parentheses:

```python
eventId = await (pump << o6.Event(server, message="Cavitation detected"))
```

Without parentheses, `await pump << o6.Event(...)` parses as
`(await pump) << o6.Event(...)`, because `await` binds tighter than `<<`.
