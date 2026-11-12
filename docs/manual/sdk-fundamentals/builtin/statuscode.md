# StatusCode and Errors

`o6.StatusCode` reports the outcome or quality of an OPC UA operation.
Some APIs return it for you to inspect; others raise `o6.StatusCodeError`.
Choose the handling that matches the API before using its result.

## Errors and status codes

A service status describes the request as a whole. An operation status
describes one target inside that request. A successful Read service can still
return `BAD_NODE_ID_UNKNOWN` for one node.

High-level client APIs check service failures and raise `StatusCodeError`.
Server helpers operate locally; failures to submit an operation can also
raise. Whether an individual target's failure is returned or raised depends
on the operation:

| Handling pattern | Examples | What you do |
|---|---|---|
| Automatic checks | Value-only reads, typed Node operations | Handle `StatusCodeError` when the operation rejects a status. |
| Returned operation statuses | High-level `write()` and `call()` | Check the returned status before using outputs; check each status for a batch. |
| Statuses inside result objects | Full DataValues, raw service responses | Inspect the embedded statuses. For raw responses, check the service first, then each operation. |

These rules apply to both synchronous and asynchronous calls. In an async
task, await the operation before inspecting its result. Raw calls can still
raise if a request cannot be submitted or completed; returning a response
does not imply that its statuses are successful.

### Checking a returned status

`status.check()` accepts only exact `o6.StatusCode.GOOD` (zero), returning
`None`. Any other value raises `o6.StatusCodeError`. This standalone example
uses the status a rejected write might return:

```python
import o6

status = o6.StatusCode.BAD_TYPE_MISMATCH
try:
    status.check(message="writing the setpoint")
except o6.StatusCodeError as error:
    print(error.symbol)                     # BadTypeMismatch
    print(error.code == o6.StatusCode.BAD_TYPE_MISMATCH)  # True
```

For an actual write, obtain `status` from `client.write(nodeId, value)` or
`server.write(nodeId, value)` inside the `try` block, then call `.check()`.
This catches both a raised service failure and a returned operation failure.
Checking a status does not undo the operation or roll back other batch items.

`error.code` retains the raw status integer; `error.symbol` is its OPC UA
spelling. The optional `message=` becomes an exception note, alongside any
operation or batch-index context supplied by the API.

## Good severity versus exact GOOD

A Good-severity status can include an informational code or flags. For
example, `GOOD_CLAMPED` indicates success with a value clamped to a limit;
it is not equal to `GOOD`. Value-only reads accept such statuses, while
`.check()` rejects them unless you pass that exact code as `expected=`.

`StatusCode` is a Python `enum.IntFlag`, with upper snake case members such
as `BAD_NODE_ID_UNKNOWN`. Severity occupies the top two bits. To accept
all Good-severity statuses, test those bits:

```python
import o6

status = o6.StatusCode.GOOD_CLAMPED
severity = int(status) & 0xC0000000
print(severity == 0)                        # True: Good severity.
print(status == o6.StatusCode.GOOD)          # False: not exact GOOD.
status.check(expected=o6.StatusCode.GOOD_CLAMPED)
```

`o6.StatusCode.BAD in status` and `o6.StatusCode.UNCERTAIN in status` test
the respective severity bits. Do not use `o6.StatusCode.GOOD in status`:
`GOOD` is zero, so that containment test is true even for Bad statuses.
Likewise, `if status:` tests for a nonzero integer, not for failure.

Use an explicit severity policy when accepting informational Good results.
For example, this fragment processes a `dv` returned by
`read(..., valueOnly=False)` and rejects Uncertain or Bad quality:

```python
if int(dv.status) & 0xC0000000:
    raise o6.StatusCodeError(dv.status)
print(dv.value)
```

An unset `DataValue.status` reads as `GOOD`, so the same check works when the
server omits the status field.

## The status bits

A StatusCode is a structured 32-bit integer:

| Field | Meaning |
|---|---|
| Severity | Good, Uncertain, or Bad. |
| Sub-code | The specific outcome, such as `BadTimeout` or `GoodClamped`. |
| Info bits | Additional information, such as `SemanticsChanged` or `StructureChanged`. |

!!! warning "Sub-codes are not independent flags"
    OR-ing two error codes does not describe two problems:
    `BAD_NODE_ID_UNKNOWN | BAD_ATTRIBUTE_ID_INVALID` equals
    `BAD_ATTRIBUTE_ID_INVALID`. Compare complete codes with `==`; reserve
    bitwise tests for severity and defined info bits.

## Python errors

Not every failure is an OPC UA status:

| Exception | Typical cause |
|---|---|
| `TypeError` | An unsupported Python argument type. |
| `ValueError` | An invalid argument value or combination, such as mismatched list lengths. |
| `RuntimeError` | An invalid lifecycle operation or a malformed response, such as an unexpected result count. |
| `KeyError` | A Node browse path matches no target. |
| `AttributeError` | Dotted child navigation finds no child or an ambiguous name. |
| `ImportError` | `browseInteractive()` cannot load `curses`. |

Client diagnostic messages use the logger passed to the constructor or
`client.config.logger`, defaulting to `o6.client`. Set it to `logging.DEBUG`
to investigate a failed handshake; logs do not replace result checks.

## Related topics

| Topic | What it covers |
|---|---|
| [Node operations](../../node-api/read-write-call.md) | Reading, writing, and calling through live node handles. |
| [Client operations](../../client/read-write-call.md) | Scalar and batch result shapes and argument validation. |
| [Local server nodes](../../server/local-nodes.md) | Local reads, writes, and Method calls. |
| [Raw Services](../../client/raw-services.md) | Checking service and operation results in response objects. |
| [Part 4 — Services, §7 StatusCodes](https://reference.opcfoundation.org/specs/OPC-10000-4/7.38) | Status-code symbols and their meanings. |
| [Part 6, §5.1.2 — Built-in Types](https://reference.opcfoundation.org/Core/Part6/v105/docs/5.1.2) | The StatusCode representation and encoding. |
| [Part 3, §8 — Standard DataTypes](https://reference.opcfoundation.org/Core/Part3/v105/docs/8) | Standard datatype definitions, including StatusCode. |
| [Container Types](container-types.md#datavalue) | StatusCode in DataValue and the default status of an unset value. |
