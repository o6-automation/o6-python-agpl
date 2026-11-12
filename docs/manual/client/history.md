# Historical Data

Read recorded values or update historical samples on a server that supports history.

## Reading recorded values

Four methods cover historical access. They build the history request and
return unpacked results. They require a server with a history backend.
An unsupported or rejected history service raises `o6.StatusCodeError`,
with the OPC UA code in `.code`.
See the shared [error-handling contract](../sdk-fundamentals/builtin/statuscode.md#errors-and-status-codes).

This fragment assumes a connected `client` and a historized Double Variable
at `ns=1;s=Temperature`, as in the [server example](../server/history.md#recording-writes).
Read raw history for a time interval:

```python
import datetime
from o6.ns import ns0

end = datetime.datetime.now(datetime.timezone.utc)
start = end - datetime.timedelta(hours=1)

history = client.historyRead(
    "ns=1;s=Temperature",
    start,
    end,
    numValuesPerNode=0,     # no total limit; follow all response pages
    returnBounds=False,    # True also requests values bracketing the interval
    timestampsToReturn=ns0.datatypes.TimestampsToReturn.BOTH,
)
for dv in history.dataValues:
    dv.status.check(message="reading a historical sample")
    print(dv.sourceTimestamp, dv.value)
```

A single target returns one `HistoryData`. A list of targets returns a list,
in order. Bad service and per-node statuses raise `StatusCodeError` in both
forms. Batch failures include the target index in the exception notes.
These result checks do not validate the quality of each recorded sample.
The example requires exact `GOOD` for each DataValue; use a
[severity check](../sdk-fundamentals/builtin/statuscode.md#good-severity-versus-exact-good)
if your application accepts informational Good codes.

## Paging and limits

`historyRead` follows server-issued continuation points automatically and keeps
target order for multiple nodes. `numValuesPerNode` limits the **total returned
per node**, not the size of an individual page. For example, a limit of `250`
can require several requests when the server returns at most `100` at a time.
The default `0` follows every page in the requested interval.

Results are accumulated in memory before the method returns. For large
histories, choose a finite limit or read smaller time windows.
Unused tokens are released when that limit is reached or when a read fails or
is cancelled. A broken connection can prevent release, so stores must expire
abandoned tokens.

## Updating historical samples

Writing history takes `DataValue` objects with `sourceTimestamp` set:

```python
import o6

values = [o6.DataValue(
    value=o6.Double(21.5),
    sourceTimestamp=o6.DateTime(start + datetime.timedelta(minutes=1)),
)]
result = client.historyUpdateInsert("ns=1;s=Temperature", values)
result.statusCode.check(message="inserting historical samples")
for status in result.operationResults:
    status.check()
```

Insert requires unused timestamps. Use
`client.historyUpdateReplace("ns=1;s=Temperature", values)` to replace samples
at existing timestamps, or
`client.historyUpdateDelete("ns=1;s=Temperature", start, end)` to remove an
interval. All three return a per-node `HistoryUpdateResult`; apply the same
checks to its `statusCode` and `operationResults`. A service failure raises
before a result is returned.
