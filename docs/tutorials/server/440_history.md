# Historical data

A historizing Variable records its values over time, so a client can read a time range instead of only the current value. You need a history database on the server and a Variable marked as historizing. With both in place, recording and read-back are automatic.

The server from [Set the stage](../setup.md) historizes `Kettle/Temperature` from startup. Every value the simulation writes is recorded, and `HistoryRead` on `ns=1;i=1302` returns real data.

---

## Configuring the history database

Configure the database before `start()`:

```python
server.config.setHistoryDatabase(maxNodes=10)
```

`maxNodes` sizes the initial node table. The table grows on demand, so `maxNodes` is a pre-allocation, not a limit on how many Variables can historize. Calling `setHistoryDatabase(...)` after `start()` raises. The built-in store is in memory and does not survive a process restart.

---

## Marking a Variable historizing

`Server.addVariable(...)` accepts `historizing=`: `True` for the defaults, or an `o6.History(...)` to configure the recording:

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

`o6.History(...)` fields:

| Field | Meaning | Default |
|---|---|---|
| `capacity` | Samples kept per node; the oldest samples are evicted when full. `0` inherits the database default (100); `None` grows without eviction. | `0` |
| `strategy` | `"on-write"` records value writes; `"poll"` periodically reads and records reported changes, including callback values; `"manual"` records explicit historical insertions only. | `"on-write"` |
| `interval` | Poll period in seconds. Only meaningful with `strategy="poll"`. | 1.0 |

Variables created before startup register during `start()`, so `setHistoryDatabase(...)` may run before or after their creation. Startup raises if the database is missing or registration fails. Variables added after startup register immediately and require the database to be configured already.

A Variable your server didn't create with `addVariable(...)`, such as a nodeset node, a declared instance or one a client added at runtime, can't take `historizing=`. Use `server.historize(target, ...)` for those. It takes effect immediately instead of at `start()`, so the database must already be configured.

---

## Reading it back

Any client reads the history with the standard OPC UA `HistoryRead` service:

```python
data = client.historyRead("ns=1;i=1302", start, end)
for dv in data.dataValues:
    print(dv.sourceTimestamp, dv.value)
```

`start` and `end` are timezone-aware `datetime`s; `end` is exclusive. A large range is paged with a continuation point; `setHistoryDatabase(..., maxResponseSize=...)` sets the page size (default 100). `client.historyRead` follows all pages automatically. Its `numValuesPerNode` argument limits the total returned per node, with `0` meaning no total limit. Results accumulate in memory, so use a finite limit or smaller time windows for large histories. See [Paging and limits](../../manual/client/history.md#paging-and-limits).

---

## The `allowHistoryUpdate` / `allowHistoryDelete` hooks

`o6.AccessControl` has two authorization hooks for the `HistoryUpdate` and `HistoryDelete` services:

```python
class DistilleryAccessControl(o6.AccessControl):
    def allowHistoryUpdate(self, session, nodeId, performUpdateType, value):
        """Decide whether this session may push history into the Variable."""
        return o6.roles.engineer in session.roles

    def allowHistoryDelete(self, session, nodeId, startTimestamp, endTimestamp, isDeleteModified):
        """Decide whether this session may delete history."""
        return False   # never let clients delete history
```

- `allowHistoryUpdate` runs on every `HistoryUpdate` request. It receives `performUpdateType` (insert / replace / update / remove) and the `DataValue` being written.
- `allowHistoryDelete` runs on every `HistoryDelete` request. It receives the time range to delete and whether modified values are included.

The inherited hooks require `INSERT_HISTORY` for inserts, `MODIFY_HISTORY` for
updates or replacements, and `DELETE_HISTORY` for deletion. The override above
replaces the history-update role check with its own Engineer-role check.
Call `super().allowHistoryUpdate(...)` when an override should retain the node's
role-permission checks. See
[Role-based access control](../../manual/server/security.md#role-based-access-control).

The `session.roles` check uses the roles set up on the [authentication page](410_access-control-auth.md#assign-roles-from-activatesession). When `activateSession` returns `SessionActivation(roles=(o6.roles.engineer,))` for the control-plane user, `o6.roles.engineer in session.roles` is `True` for that session and `False` for the HMI's `observer` session. Roles are on `session.roles`, not in `session.context`.

---

## Next steps

| Topic | What it covers |
|---|---|
| [The distillery server](500_distillery_server.md) | The address space and behaviour assembled into the runnable two-file project. |
| [Server manual](../../manual/server/history.md#retention-and-response-size) | The full history reference, including ring sizing and the response-paging default. |
