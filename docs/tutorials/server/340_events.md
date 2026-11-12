# Events

An event reports something that happens at a specific moment: a batch starts or ends, the state changes, or a client changes the setpoint. A value change says "the temperature moved from 20.0 to 20.1". An event says "the still transitioned from `Filling` to `Heating`".

On this page the server emits an event on every batch transition and every client write. Clients subscribed to the `Server` object or to `DistillingSystem` receive it. Optionally, the events use a declared `DistilleryEventType`.

---

## Emit one

An event needs no setup. `server.createEvent(...)` fires one from the
standard `Server` object, which every client can subscribe to:

```python
import o6
from o6 import Server

server = Server(port=4840)
server.start()

server.createEvent(message=o6.LocalizedText("Server is up", "en"), severity=100)
```

This is a complete `BaseEventType` notification. `severity` must be in
`1..1000`; `createEvent` raises `ValueError` outside that range.

For a message that contains a colon, pass `o6.LocalizedText(text, locale)`
instead of a bare string. A bare string is parsed as `"locale:text"`, so
`"Batch started: filling kettle"` would lose everything before the colon.

---

## Add the fields you care about

To report the batch and state, pass them as `fields`, keyed by the
event-filter path a subscriber selects them with:

```python
server.createEvent(
    message=o6.LocalizedText("Batch started: filling kettle with wash", "en"),
    severity=500,
    fields={"/1:Cycle": o6.Int32(1), "/1:State": "Filling"},
)
```

`/1:Cycle` means "the field named `Cycle` in namespace 1". You don't have to
declare it: the field travels with the notification, and a client that selects
`/1:Cycle` receives it. [When you need more](#when-you-need-more) covers what
declaring it adds.

---

## Give it a source

`SourceName` is more useful when it names the object where the event
happened. Pass any Object as `source`:

```python
sys_obj = server.addObject("DistillingSystem", server.objectsNode,
                           nodeId="ns=1;i=1000")

server.createEvent(source=sys_obj, message=o6.LocalizedText("Filling", "en"),
                 severity=500)
```

Events emitted from `sys_obj` still propagate to the standard `Server` object,
so a client subscribed there sees them without knowing about the distillery.

---

## Fire it repeatedly

The distillery fires the same event shape repeatedly; only the message,
severity and two fields change. `o6.Event(server, ...)` builds a reusable
draft without touching the address space. `trigger()` fires whatever the draft
currently holds:

```python
draft = o6.Event(server, source=sys_obj)

draft["/1:Cycle"] = o6.Int32(1)
draft["/1:State"] = "Filling"
draft.message = o6.LocalizedText("Batch started: filling kettle with wash", "en")
draft.severity = 500
draft.trigger()
```

`Event` is a mutable mapping, so you set fields with `draft[...]`. Build the
draft once and fire it as often as needed.

---

## Wire it into the update loop

The [update loop](330_server-callbacks.md) detects state and cycle changes on
every tick. Emit from there with a helper around the draft:

```python
def emit(draft, sim_state, message, severity):
    draft.message = o6.LocalizedText(message, "en")
    draft.severity = severity
    draft["/1:Cycle"] = o6.Int32(int(sim_state["cycle"]))
    draft["/1:State"] = sim_state["state"]
    draft.trigger()
```

Call it on every state transition. Use severity `500` at a batch boundary and
`200` for the steps between:

```python
BATCH_BOUNDARIES = ("Filling", "Idle")

severity = 500 if sim_state["state"] in BATCH_BOUNDARIES else 200
emit(draft, sim_state, msg, severity)
```

Call it on a client write too, so subscribers hear about it immediately instead
of at the next batch step:

```python
if cur_setpoint != last_written_setpoint:
    sim_state["setpoint"] = float(cur_setpoint)
    emit(draft, sim_state, f"Setpoint set to {cur_setpoint:.1f} °C by a client", 400)
```

#### Putting it all together

```python
import time
import o6
from o6 import Server

server = Server(port=4840)
sys_obj = server.addObject("DistillingSystem", server.objectsNode,
                           nodeId="ns=1;i=1000")
draft = o6.Event(server, source=sys_obj)

server.start()

for cycle, state in ((1, "Filling"), (1, "Heating"), (2, "Filling")):
    draft["/1:Cycle"] = o6.Int32(cycle)
    draft["/1:State"] = state
    draft.message = o6.LocalizedText(f"Batch {cycle}: {state}", "en")
    draft.severity = 500 if state == "Filling" else 200
    draft.trigger()
    time.sleep(1)

server.stop()
```

---

## When you need more

Both additions are optional.

**A declared event type, so fields are discoverable.** Without a declaration, a
client has to know `/1:Cycle` in advance. Declaring the fields as Properties of
an ObjectType lets a client find them by browsing and build
`"SELECT /1:Cycle, /1:State"` from what it discovered:

```python
event_type = server.addObjectType("DistilleryEventType",
                                  ns0.objtypes.BaseEventType,
                                  nodeId="ns=1;i=3000")
for name, initial, node_id in (("Cycle", 0, "ns=1;i=3001"),
                               ("State", "", "ns=1;i=3002")):
    ns0.vartypes.PropertyType(
        parent=event_type, browseName=f"1:{name}", displayName=name,
        nodeId=node_id, referenceType=ns0.reftypes.HasProperty,
        modellingRule="Mandatory", value=initial, server=server,
    )
```

Then name the type when you emit: `server.createEvent("ns=1;i=3000",
source=sys_obj)`, or prepare a draft with
`o6.Event(server, eventType="ns=1;i=3000", source=sys_obj)`.
`modellingRule="Mandatory"` marks the fields as always present on an instance,
like the standard fields.

**A source clients can subscribe to directly.** Subscribing to the `Server`
object always works. For a client to subscribe to `DistillingSystem` instead,
and filter less, that node needs a non-zero `EventNotifier`. `addObject` does
not set it; the declared form does:

```python
sys_obj = ns0.objtypes.BaseObjectType(
    parent=server.objectsNode, browseName="1:DistillingSystem",
    displayName="DistillingSystem", nodeId="ns=1;i=1000",
    referenceType=ns0.reftypes.Organizes,
    eventNotifier=1,   # SubscribeToEvents
    server=server,
)
server.addReference(source=ns0.instances.server, reftype=ns0.reftypes.HasNotifier, target=sys_obj)
```

The `HasNotifier` reference makes that path browsable: a client can find it by
walking the notifier hierarchy instead of being given the NodeId.

Both snippets need `from o6.ns import ns0`.

---

## The mirror pattern, for polling clients

Every event is also written into four Variables under `Events/`:

```
Events/
├── EventCount       (Int32,    read-only)   (ns=1;i=1601)
├── LastEventTime    (DateTime, read-only)   (ns=1;i=1602)
├── LastEventMessage (String,   read-only)   (ns=1;i=1603)
└── LastEventState   (String,   read-only)   (ns=1;i=1604)
```

`EventCount` increments, and the other three hold the latest event's timestamp, message and state. This channel supplements the real event; it does not replace it. It suits a client that already runs a data-change subscription and doesn't want a separate event subscription for one signal. Clients read these Variables through the normal data-change path, without an `EventFilter` or event notifier.

Only the latest event is visible this way. "Last 100 events" or "all events in the last hour" requires [historical access](440_history.md). The real `BaseEventType` notification is what a subscription pushes the moment the event happens.

---

## Next steps

| Topic | What it covers |
|---|---|
| [Timers and async loops](350_timers.md) | `async def` callbacks, thread-pool offload, cooperative cancellation on `server.stop()`. |
| [Listen to events](../client/240_listen-to-events.md) | The client side: `monitorEvent`, reading the callback's fields, filtering with the SQL-like string syntax. |
| [Server manual](../../manual/server/events.md) | The full `createEvent` / `Event` API, `GeneratesEvent` inference, and the `<<` shorthand. |
