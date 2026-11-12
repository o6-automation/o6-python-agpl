# Reading & Writing

This page reads the state of the distilling example server and writes new values to it. Reads accept one node or a list; writes also accept a mapping. Both can target any attribute. Value-only reads raise on failure; raw reads keep per-target statuses in DataValues, and writes return statuses.

This page covers:

- Read one or several variables.
- Write one or several variables.
- Read and write non-`Value` attributes.

!!! info
    Start the [example server](../setup.md) in the background. This page assumes you can [create and connect](100_connect.md) a client and [browse](110_browse.md) the address space. The NodeIds below belong to the `DistillingSystem` object at `ns=1;i=1000`.

---

## Read one or several variables

`client.read(target)` takes a NodeId and returns the current value of its `Value` attribute.

Read `Level`, `Temperature` and `WashStart` of the `Kettle` at `ns=1;i=1300`:

```python
Level = client.read("ns=1;i=1301")
Temperature = client.read("ns=1;i=1302")
WashStart = client.read("ns=1;i=1303")
```

To read several variables in one round-trip, pass a list of NodeIds. The result list has the same order as the input:

```python
values = client.read([
        "ns=1;i=1301",
        "ns=1;i=1302",
        "ns=1;i=1303",
    ])
print(values)
```

The values change between reads: `Level` climbs as the kettle fills, `Temperature` rises during heating, and `WashStart` records the kettle level when the still started producing spirit.

If a node does not exist or the server rejects a value-only read, scalar and
list forms both raise `o6.StatusCodeError`. Its `.code` preserves the OPC UA
status. A list failure includes the failed index in an exception note.

```python
from o6 import Client, StatusCodeError

with Client("opc.tcp://localhost:4840") as client:
    try:
        values = client.read(["ns=1;i=1301", "ns=1;i=1302"])
    except StatusCodeError as e:
        print("read failed:", e.code, getattr(e, "__notes__", []))
```

Use `valueOnly=False` to receive a DataValue for every target, including failed
ones. `timestampsToReturn` selects SOURCE (the default), SERVER, BOTH, or
NEITHER from `ns0.datatypes.TimestampsToReturn`. Service failures still raise
`StatusCodeError`. The same read options and result shapes work with
`server.read`; local access uses administrative privileges.

!!! tip
    Any string form accepted by `o6.NodeId(...)` works: `i=`, `s=`, `ns=...;i=...`, `nsu=...;i=...`, and the shortname URI form once the matching nodeset is loaded. See [NodeIds and namespace info](430_nodeids-and-namespace-info.md) for the full syntax.

#### Putting it all together

```python
import o6
from o6 import Client

with Client("opc.tcp://localhost:4840") as client:
    # One read per round-trip
    level = client.read("ns=1;i=1301")
    temperature = client.read("ns=1;i=1302")

    # Or batch them in a single round-trip
    kettle = client.read([
        "ns=1;i=1301",
        "ns=1;i=1302",
        "ns=1;i=1303",
    ])
    print(kettle)

    print("level value:", level, "  is o6.Float?", isinstance(level, o6.Float))
```

---

## Write one or several variables

`client.write(target, value)` replaces the `Value` attribute of a node. On the distilling server only `Status.Operating` (`ns=1;i=1203`) and `Status.Setpoint` (`ns=1;i=1204`) are writable; everything under `Kettle`, `Distillate`, `Actuators` and `Events` is read-only. `AccessLevel` shows this:

```python
import o6
from o6 import AttributeId, Client
from o6.ns.ns0.datatypes import NodeClass

with Client("opc.tcp://localhost:4840") as client:
    writable = client.browse(
        "ns=1;i=1000",
        nodeClassMask=NodeClass.VARIABLE,
    )
    for ref in writable:
        access = client.read(ref.nodeId, attr=AttributeId.ACCESS_LEVEL)
        # bit 1 of AccessLevel = "writable"
        if access & 2:
            print(ref.browseName.name, "→", o6.NodeId(f"nsu={ref.nodeId.ns.uri};{ref.nodeId.id}"))
```

To pause the still, write `False` to `Operating`:

```python
client.write("ns=1;i=1203", False)
```

To write several variables in one round-trip, pass a list of NodeIds and a list of values of the same length and order. The result is a list with one `StatusCode` per write:

```python
statuses = client.write(
        ["ns=1;i=1203", "ns=1;i=1204"],
        [True, 90.0],
    )
```

A `StatusCode` other than `Good` means that write failed. The other writes in the call still happen, and `client.write` does not raise.

!!! info
    `client.write` also accepts a mapping, such as `client.write({"ns=1;i=1204": 90.0})`, for targets computed at runtime.

#### Putting it all together

```python
from o6 import Client

with Client("opc.tcp://localhost:4840") as client:
    # Single write
    client.write("ns=1;i=1203", False)

    # Or batch them in a single round-trip
    statuses = client.write(
        ["ns=1;i=1203", "ns=1;i=1204"],
        [True, 90.0],
    )
    print(statuses)
```

---

## Read and write non-`Value` attributes

`read` and `write` use the `Value` attribute by default. Use `attr=` to target another attribute, such as `BrowseName`, `DisplayName`, `NodeClass`, `Description`, `DataType`, `ValueRank` or `AccessLevel`.

### Read a non-`Value` attribute

Read the metadata of the `Setpoint` variable:

```python
name = client.read("ns=1;i=1204", attr="BrowseName")
display = client.read("ns=1;i=1204", attr="DisplayName")
klass = client.read("ns=1;i=1204", attr=AttributeId.NODE_CLASS)
access = client.read("ns=1;i=1204", attr=AttributeId.ACCESS_LEVEL)

# `name` is a QualifiedName; `.name` gives just the bare browse name.
print(name.name)        # "Setpoint"
print(display.text)     # LocalizedText.text — the bare string
print(int(klass))       # raw integer (the wire value, 2 == VARIABLE)
print(access)           # raw integer
```

`attr=` accepts a string or an `o6.AttributeId` member. Strings are case-insensitive and ignore punctuation, so `"BrowseName"`, `"browse_name"` and `"BROWSENAME"` all match.

### Write a non-`Value` attribute

Pass both `value=` and `attr=`. Wrap values of structured attributes in the matching type, for example `LocalizedText` for `Description`:

```python
from o6 import Client, LocalizedText, QualifiedName, StatusCodeError

with Client("opc.tcp://localhost:4840") as client:
    try:
        status = client.write(
            "ns=1;i=1204",
            value=LocalizedText("Target kettle temperature"),
            attr="Description",
        )
    except StatusCodeError as e:
        # The distillery server denies writes to non-Value attributes
        # (BAD_USER_ACCESS_DENIED); other servers may allow them.
        # The call shape is correct either way — it's the server's
        # AccessControl that decides.
        status = e.code
    print("description write:", status)

    try:
        client.write(
            "ns=1;i=1204",
            value=QualifiedName("Setpoint"),
            attr="BrowseName",
        )
    except StatusCodeError as e:
        # Same caveat: server-side access control may refuse.
        print("browsename write refused:", e.code)
```


#### Putting it all together

```python
import o6
from o6 import AttributeId, Client

with Client("opc.tcp://localhost:4840") as client:
    # Read a structured attribute (QualifiedName)
    name = client.read("ns=1;i=1204", attr="BrowseName")
    print(name.name)        # "Setpoint"  — QualifiedName.name strips the namespace

    # Read a scalar attribute (NodeClass enum -> raw int on the low-level read path)
    klass = client.read("ns=1;i=1204", attr=AttributeId.NODE_CLASS)
    print(int(klass))       # 2 — VARIABLE

    # AccessLevel: bit 1 set means writable
    access = client.read("ns=1;i=1204", attr=AttributeId.ACCESS_LEVEL)
    print("writable:", bool(access & 2))

    # The distillery server only allows `Value` writes; non-Value
    # attribute writes return BAD_USER_ACCESS_DENIED. The call
    # shape is correct — switch to a Value write (no `attr=`) for
    # an example that actually succeeds end-to-end:
    status = client.write("ns=1;i=1204", 90.0)   # writes the Value attribute
    print("setpoint write:", status)             # GOOD
```

---

## Next steps

| Topic | What it covers |
|---|---|
| [Call a method](130_call-method.md) | Call methods on objects. |
| [Low-level service calls](500_lowlevel-service-calls.md) | Use the raw `Read` / `Write` service for full control over the request. |
