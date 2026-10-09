# Historical data

Historizing in the distillery: recording a Variable's values over time so a client can ask for a time range instead of only ever seeing the current value. It needs two things — a history database on the server, and a Variable marked as historizing — and once both are in place, recording and read-back are automatic.

The distillery already does this for `Kettle/Temperature`: [Set the stage](../setup.md) starts a server where that one Variable is historizing from the moment it comes up, so every value the simulation writes lands in the history and `HistoryRead` against `ns=1;i=1302` returns real data.

---

## Configuring the history database

One call, before `start()`, gives the server somewhere to record:

```python
server.config.setHistoryDatabase(maxNodes=10)
```

`maxNodes` sizes the *initial* node table — it grows on demand, so it isn't a hard ceiling on how many Variables can historize, just how much is pre-allocated. This has to run before `start()`; changing it afterwards raises.

---

## Marking a Variable historizing

`Server.addVariable(...)` accepts `historizing=` — either `True` for the defaults, or an `o6.History(...)` to size and tune the recording:

```python
import o6
from o6 import Server

server = Server(port=4840)
server.config.setHistoryDatabase(maxNodes=10)

temperature = server.addVariable(
    "KettleTemperature",
    server.objectsNode,
    20.0,
    nodeId="ns=1;i=1302",
    historizing=True,
)
server.start()
```



| Field | Meaning | Default |
|---|---|---|
| `capacity` | Samples kept per node — a ring buffer; the oldest sample is evicted once it fills. | 100 |
| `strategy` | `"on-write"` (record every write), or `"poll"` (sample on a timer, independent of writes). | `"on-write"` |
| `interval` | Poll period in seconds. Only meaningful with `strategy="poll"`. | 1.0 |

Variables created before startup register during `start()`, so `setHistoryDatabase(...)` may run before or after their creation. Startup raises if the database is missing or registration fails. Variables added after startup register immediately and require the database to be configured already.

A Variable your server didn't create — a nodeset node, a declared instance, or one a client added at runtime — can't take `historizing=` at construction time. `server.historize(target, ...)` is the equivalent for those: it takes effect immediately (the database has to already be configured), rather than waiting for `start()`.

---

## Reading it back

Once a Variable is historizing, any client reads it back the normal OPC UA way:

```python
data = client.historyRead("ns=1;i=1302", start, end)
for dv in data.dataValues:
    print(dv.sourceTimestamp, dv.value)
```

`start`/`end` are timezone-aware `datetime`s; `end` is exclusive. A large range comes back paged behind a continuation point sized by `setHistoryDatabase(..., maxResponseSize=...)` (default 100) — `client.historyRead` follows the first page only, so a full sweep over a big range needs `serviceHistoryRead` with the continuation point fed back in.

---

## The `allowHistoryUpdate` / `allowHistoryDelete` hooks

The `o6.AccessControl` base class exposes two authorization hooks for history, matching the `HistoryUpdate` and `HistoryDelete` service calls:

```python
class DistilleryAccessControl(o6.AccessControl):
    def allowHistoryUpdate(self, session, nodeId, performUpdateType, value):
        """Decide whether this session may push history into the Variable."""
        return o6.roles.engineer in session.roles

    def allowHistoryDelete(self, session, nodeId, startTimestamp, endTimestamp, isDeleteModified):
        """Decide whether this session may delete history."""
        return False   # never let clients delete history
```

`allowHistoryUpdate` is consulted on every `HistoryUpdate` request, with `performUpdateType` (insert / replace / update / remove) and the `DataValue` being written. `allowHistoryDelete` is consulted on every `HistoryDelete` request, with the time range being deleted and whether modified values are included. Both default to permissive — the base class returns `True` — so an `AccessControl` subclass that does not override them allows any session to write or delete history.

The `session.roles` check mirrors where the [authentication page](410_access-control-auth.md#assign-roles-from-activatesession) leaves the reader: once `activateSession` returns `SessionActivation(roles=(o6.roles.engineer,))` for the control-plane user, `o6.roles.engineer in session.roles` is `True` for that session and `False` for the HMI's `observer` session — roles live on `session.roles`, not folded into `session.context`.

---

## What's next?

The distillery's story is essentially complete. The last page in the tutorials assembles the core of it into the two files [Set the stage](../setup.md) distributes — the same server both the client and server tutorials talk to.

- [The distillery server](500_distillery_server.md) — the address space and behaviour assembled into the runnable two-file project.
- [Server manual](../../manual/server/operations.md#historical-data) — the full history story, including ring sizing and the response-paging default.
