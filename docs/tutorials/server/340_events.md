# Events

You've been watching the Kettle values change continuously, and the [update loop](330_server-callbacks.md) mirrors the simulation into the address space every tick. But the distillery also has *events* — discrete things that happen at specific moments (a batch starts, a batch ends, a state transition, a client changes the setpoint). A value change says "the temperature moved from 20.0 to 20.1"; an event says "the still just transitioned from `Filling` to `Heating`". This page wires that up.

By the end, the server emits a real `BaseEventType` notification — of its own `DistilleryEventType` — on every batch transition and every client write, and a client subscribed to the `Server` object or to `DistillingSystem` directly sees it land.

---

## Emit one

An event needs no setup at all. `server.createEvent(...)` fires one from the
standard `Server` object, which every client can already subscribe to:

```python
import o6
from o6 import Server

server = Server(port=4840)
server.start()

server.createEvent(message=o6.LocalizedText("Server is up", "en"), severity=100)
```

That is a complete, valid `BaseEventType` notification. `severity` is `1..1000`
and `createEvent` raises `ValueError` outside that range.

A message with a colon in it needs an explicit `o6.LocalizedText(text, locale)`
rather than a bare string — a bare string is parsed as `"locale:text"`, so
`"Batch started: filling kettle"` would lose everything before the colon.

---

## Add the fields you care about

The distillery wants to say *which* batch and *which* state. Pass them as
`fields`, keyed by the event-filter path a subscriber will select them with:

```python
server.createEvent(
    message=o6.LocalizedText("Batch started: filling kettle with wash", "en"),
    severity=500,
    fields={"/1:Cycle": o6.Int32(1), "/1:State": "Filling"},
)
```

`/1:Cycle` means "the field named `Cycle` in namespace 1". Nothing has to be
declared for this to work — the field travels with the notification, and a
client that selects `/1:Cycle` receives it. See
[When you need more](#when-you-need-more) for what declaring it *does* buy.

---

## Give it a source

The `Server` object is a fine sender, but `SourceName` is more useful when it
names the thing that actually happened. Any Object will do:

```python
sys_obj = server.addObject("DistillingSystem", server.objectsNode,
                           nodeId="ns=1;i=1000")

server.createEvent(source=sys_obj, message=o6.LocalizedText("Filling", "en"),
                 severity=500)
```

Events emitted from `sys_obj` still propagate up to the standard `Server` object
on their own, so a client subscribed there sees them without knowing anything
about the distillery.

---

## Fire it repeatedly

The distillery fires the same shape of event over and over, with only the
message, severity, and two fields changing — which is what
`o6.Event(server, ...)` is for. It builds a reusable draft without touching
the address space, and `trigger()` re-reads whatever the draft currently holds:

```python
draft = o6.Event(server, source=sys_obj)

draft["/1:Cycle"] = o6.Int32(1)
draft["/1:State"] = "Filling"
draft.message = o6.LocalizedText("Batch started: filling kettle with wash", "en")
draft.severity = 500
draft.trigger()
```

`Event` is a mutable mapping, which is why the fields are set with `draft[...]`.
Build the draft once, then fire it as often as you like.

---

## Wire it into the update loop

The distillery's [update loop](330_server-callbacks.md) already detects state
and cycle changes on every tick. Emitting there is a small helper around the one
draft:

```python
def emit(draft, sim_state, message, severity):
    draft.message = o6.LocalizedText(message, "en")
    draft.severity = severity
    draft["/1:Cycle"] = o6.Int32(int(sim_state["cycle"]))
    draft["/1:State"] = sim_state["state"]
    draft.trigger()
```

Called on every state transition, with a severity that says how much the
transition matters — `500` at a batch boundary, `200` for the steps between:

```python
BATCH_BOUNDARIES = ("Filling", "Idle")

severity = 500 if sim_state["state"] in BATCH_BOUNDARIES else 200
emit(draft, sim_state, msg, severity)
```

And on a client write, so a subscriber hears about it immediately rather than at
the next batch step:

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

Two things the simple path leaves out. Skip them until you want them.

**A declared event type, so fields are discoverable.** Passing `fields` works
without declaring anything, but a client then has to know `/1:Cycle` in advance.
Declaring the fields as Properties of an ObjectType lets a client find them by
browsing, and makes `"SELECT /1:Cycle, /1:State"` a filter it can build from
what it discovered:

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
`o6.Event(server, eventType="ns=1;i=3000", source=sys_obj)`. `modellingRule="Mandatory"` marks the fields as always present
on an instance, matching the standard ones.

**A source clients can subscribe to directly.** Events already reach the
`Server` object, so subscribing there always works. If you want a client to be
able to point its subscription at `DistillingSystem` instead — and filter less —
that node needs a non-zero `EventNotifier`, which `addObject` does not set. The
declared form does:

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

The `HasNotifier` reference is what makes that path *browsable*, so a client can
discover it by walking the notifier hierarchy rather than being told the NodeId.

Both snippets need `from o6.ns import ns0`.

---

## The mirror pattern, for polling clients

Every event above is *also* written into four plain Variables under `Events/`:

```
Events/
├── EventCount       (Int32,    read-only)   (ns=1;i=1601)
├── LastEventTime    (DateTime, read-only)   (ns=1;i=1602)
├── LastEventMessage (String,   read-only)   (ns=1;i=1603)
└── LastEventState   (String,   read-only)   (ns=1;i=1604)
```

`EventCount` increments, and the other three carry the latest event's timestamp, message, and state. This is not a substitute for the real event — it is a second, simpler channel for the same information, useful for a client that already has a data-change subscription running and would rather not stand up a separate event subscription for one signal. A read of these Variables uses the standard data-change path: no `EventFilter`, no event notifier, just values that happen to move together.

The trade-off is shape: only the *latest* event is visible this way. There is no "last 100 events" or "all events in the last hour" without [historical access](440_history.md) on top — the real event, delivered as a `BaseEventType` notification, is the one a subscription actually pushes the moment it happens.

---

## What's next?

The distillery's event story is real events now, with the writable log as a convenience alongside it. The next page covers `asyncio` integration, long-running background work, and cooperative cancellation for the update loop that drives both.

- [Timers and async loops](350_timers.md) — `async def` callbacks, thread-pool offload, cooperative cancellation on `server.stop()`.
- [Listen to events](../client/240_listen-to-events.md) — the client side: `monitorEvent`, reading the callback's fields, filtering with the SQL-like string syntax.
- [Server manual](../../manual/server/events-and-timers.md) — the full `createEvent` / `Event` API, `GeneratesEvent` inference, and the `<<` shorthand.
