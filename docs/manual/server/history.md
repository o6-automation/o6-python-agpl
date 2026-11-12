# Historical Data

Record a Variable's values over time so clients can read earlier samples.
The built-in database keeps samples in memory; it does not persist them across
process restarts. Use a custom backend when history must survive a restart.

## Recording writes

Configure the database before starting the server and mark the Variable as
historizing. With the default strategy, subsequent writes record samples:

```python
import o6

server = o6.Server(port=4840)
server.config.setHistoryDatabase(capacity=1000, maxResponseSize=200)
temperature = server.addVariable(
    "Temperature", server.objects, 20.0,
    nodeId="ns=1;s=Temperature", historizing=True,
)

with server:
    temperature(21.0)
    temperature(22.0)
    input("Serving recorded temperatures; press Enter to stop.")
```

A connected client can read these samples using
[`client.historyRead`](../client/history.md). Reading history and reading the
Variable's current value are separate operations.

## Retention and response size

`setHistoryDatabase` configures the built-in store once, before startup:

| Setting | Default | Meaning |
| --- | --- | --- |
| `maxNodes` | `10` | Initial allocation for historized nodes. It grows as needed; this is not a node limit. |
| `capacity` | `100` | Maximum retained samples per node. When full, the oldest samples are evicted. |
| `maxResponseSize` | `100` | Maximum values per node in one history response page. This does not change retention. |

All three settings must be positive. Capacity counts samples, not bytes or
seconds: an array-valued sample occupies one slot but can use much more memory
than a scalar sample.

Use `historizing=o6.History(capacity=5000)` to override retention for one
Variable. The `History.capacity` default of `0` inherits the database capacity;
`None` keeps growing without eviction. An unbounded store needs an application
that can afford its memory growth.

## Choosing how to record

`historizing=True` is shorthand for `historizing=o6.History()`.
The `strategy` field chooses what produces a sample:

| Strategy | When samples are recorded |
| --- | --- |
| `"on-write"` (default) | Successful writes to the Variable's value. Changes to Python state behind a read callback alone do not record anything. |
| `"poll"` | An internal monitored item reads the value periodically, including through a read callback, and records reported changes. Unchanged values need not produce a sample every tick. |
| `"manual"` | Explicit historical insertion, for example through `client.historyUpdateInsert`. Ordinary writes to the current value are not recorded. |

For polling, `History.interval` is in **seconds**, defaults to `1.0`, and must
be at least `0.001`. This differs from [timer intervals](timers.md), which use
milliseconds.

For example, add this callback-backed Variable to a server with a configured
history database, before starting it:

```python
state = {"temperature": 22.5}

def read_sensor(node, **kwargs):
    return o6.StatusCode.GOOD, o6.Double(state["temperature"])

sensor = server.addVariable("Sensor", server.objects, 0.0)
server.implement(sensor, read=read_sensor)
server.historize(sensor, strategy="poll", interval=0.5)
```

Changes to `state["temperature"]` can now be recorded without a write to
`sensor`. The callback must return quickly; for slow devices, refresh cached
state as shown in [Slow device reads](timers.md#slow-device-reads).

## Registering and stopping history

Use `server.historize(target, ...)` for existing Variables, including nodes
loaded from a nodeset. It accepts the same capacity, strategy, and interval
settings and requires an already configured database.

Variables created with `historizing=` before startup register during `start()`;
variables added while running register immediately. Startup raises if the
database is missing or registration fails, leaving pending registrations
available for retry. If runtime creation fails, the new node is removed.

`server.unhistorize(target)` stops recording, clears the history attributes,
and **discards the built-in store's samples**. Registering the node again starts
with an empty store; this is not a pause operation. In async code, await both
`server.historize(...)` and `server.unhistorize(...)`.

## Custom backends

Supply `server.config.setHistoryDatabase(backend=backend)` to replace the
in-memory store with your own [`o6.HistoryBackend`](../../api_reference/historybackend.md).
The backend owns storage, retention, and persistence; the built-in capacity
settings do not apply. Implement `onWrite` to receive samples and
`getHistoryData` to return a read result within the requested limits. Override
`timestampsToReturnSupported` to declare the timestamp selections you support;
its default rejects all selections. The API reference describes the time-range,
bounds, and timestamp parameters, plus optional update hooks.

For results that need paging, override `getHistoryPage` instead. It returns
`(dataValues, nextToken)` and receives the incoming token, a release flag, and
the session identity. Bind tokens to the session and node, reject invalid
tokens, and return `([], b"")` after release. An empty output token ends the
read. Expire abandoned tokens too: a disconnected client may be unable to
release them.
