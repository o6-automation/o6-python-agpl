# StatusCode

`StatusCode` is a 32-bit structured integer that signals the outcome of any OPC UA operation. It encodes both the high-level outcome and the specific reason code drawn from the OPC UA status table.

| Field | Meaning |
|---|---|
| **Severity** | Good, Uncertain, Bad |
| **Sub-code** | The specific status within the severity — e.g. `BadTimeout`, `UncertainSensorNotAccurate` |
| **Info bits** | Optional flags layered on top, e.g. `SemanticsChanged`, `StructureChanged` |

See [Part 4 — Services, §7 StatusCodes](https://reference.opcfoundation.org/specs/OPC-10000-4/7.38) for a list off all OPC UA standart defined status code values.

## In o6\\Python

`StatusCode` is a Python `enum.IntFlag` — every symbolic value from the OPC UA status table is a member of the enum, spelled in upper snake case (`BadNodeIdUnknown` becomes `BAD_NODE_ID_UNKNOWN`), and the underlying value is just the raw 32-bit integer. That means the containment operator tests the severity directly, without masking by hand:

```python
status = o6.StatusCode.BAD_NODE_ID_UNKNOWN

if o6.StatusCode.BAD in status:
    print("is bad")
```

!!! warning
    Only the severity and the info bits are independent bit positions. Sub-codes
    are *values*, not flags, so OR-ing two of them together does not describe two
    problems — `BAD_NODE_ID_UNKNOWN | BAD_ATTRIBUTE_ID_INVALID` is simply
    `BAD_ATTRIBUTE_ID_INVALID`. Compare a sub-code with `==`, and use `in` only
    for the severity.

A `StatusCode` whose underlying value is `0` is the spec's `Good` *with no info bits set* — that's what an unset `DataValue.status` returns, so a missing status field is implicitly `Good`.

---

## See also

- The full OPC UA status-code table (every `Good_*` / `Uncertain_*` / `Bad_*` symbol and the info-bit layout):
  [Part 4 — Services, §7 StatusCodes](https://reference.opcfoundation.org/specs/OPC-10000-4/7.38).
- The normative `StatusCode` type itself (severity, sub-code, info bits, master flag):
  [Part 6, §5.1.2 — Built-in Types](https://reference.opcfoundation.org/Core/Part6/v105/docs/5.1.2)
  (and the `StatusCode` entry in
  [Part 3, §8 — Standard DataTypes](https://reference.opcfoundation.org/Core/Part3/v105/docs/8)).
- How `StatusCode` travels inside a `DataValue` (and the implicit-`Good` rule for missing status):
  [Container Types](container-types.md#datavalue).

