# Read / write value

You're building a small control loop against the distilling example server: discover the writables, peek at the current state, then change it. The first half of that loop — *see what the still is doing* and *tell it to do something different* — lives on this page. The next page, [Call a method](130_call-method.md), flips the on-switch; the one after that, [Monitor data changes](200_monitor-datachange.md), is where you stop polling and let the server push values to you.

Once you know which `NodeId`s a server exposes — from [browsing](110_browse.md) — the next step is reading their current values and, where the server allows it, writing new ones. The `Read` and `Write` services can handle a single node, a list of nodes, or a mapping; they can target any attribute (not just `Value`); and they return a `StatusCode` per node on partial failure rather than raising.

This page walks through read and write primitives:

- Read one or several variables.
- Write one or several variables.
- Read and write non-`Value` attributes.

!!! info
    This tutorial expects the [example server running](../../tutorials.md#running-the-example-server) in the background, and assumes you know how to [create and connect](100_connect.md) a client and how to [browse](110_browse.md) the address space. The `NodeId`s used below are the ones exposed by the distilling example server's `DistillingSystem` object at `ns=1;i=1000`.

---

## Read one or several variables

`client.read(target)` is the basic read service call: hand it a `NodeId` and get back the current value of its `Value` attribute. The simplest read takes one `NodeId` and returns its current value.

Let's look into the `Kettle` at `ns=1;i=1300` — its `Level`, `Temperature` and `WashStart`:

```python
Level = client.read("ns=1;i=1301")
Temperature = client.read("ns=1;i=1302")
WashStart = client.read("ns=1;i=1303")
```

To read several variables in one round-trip, pass a list of `NodeId`s. The result is a list in the same order as the input:

```python
values = client.read([
        "ns=1;i=1301",
        "ns=1;i=1302",
        "ns=1;i=1303",
    ])
print(values)
```

The values of the distillig server will be different on every read — `Level` climbs as the kettle fills, `Temperature` rises during heating, and `WashStart` records the kettle level at the moment the still started producing spirit.

If a node does not exist or the server rejects the read, the corresponding entry in the returned list is the `StatusCode` that came back from the server — `client.read` does **not** raise on partial failure.

!!! tip
    Any string form accepted by `o6.NodeId(...)` works here — `i=`, `s=`, `ns=...;i=...`, `nsu=...;i=...`, even the shortname URI form once the matching nodeset is loaded. See [NodeIds and namespace info](430_nodeids-and-namespace-info.md) for the full syntax.

#### Putting it all together

```python
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
```

---

## Write one or several variables

`client.write(target, value)` is the basic write service call: hand it a `NodeId` and a new value, and the server replaces the `Value` attribute. In the distilling example the only writable variables on the server are `Status.Operating` (`ns=1;i=1203`) and `Status.Setpoint` (`ns=1;i=1204`) — everything under `Kettle`, `Distillate`, `Actuators` and `Events` is read-only. You can see that directly from `AccessLevel`:

```python
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
            print(ref.browseName.name, "→", ref.nodeId)
```

To pause the still, write `False` to `Operating`:

```python
client.write("ns=1;i=1203", False)
```

To write several variables in one round-trip, pass a list of `NodeId`s and a parallel list of values (same order, same length). The result is a list of `StatusCode`s, one per write:

```python
statuses = client.write(
        ["ns=1;i=1203", "ns=1;i=1204"],
        [True, 90.0],
    )
```

A `StatusCode` other than `Good` on any entry means that particular write failed — the other writes in the same call still happened, and `client.write` does not raise.

!!! info
    If you'd rather treat writes as key/value pairs, `client.write({"ns=1;i=1204": 90.0})` is accepted as well — useful when the targets are computed dynamically and live in a dict.

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

By default both `read` and `write` operate on the `Value` attribute of a variable. The `attr=` keyword lets you target a different attribute — `BrowseName`, `DisplayName`, `NodeClass`, `Description`, `DataType`, `ValueRank`, `AccessLevel`, and so on.

### Read a non-`Value` attribute

Let's inspect the `Setpoint` variable's metadata without reading its value:

```python
name = client.read("ns=1;i=1204", attr="BrowseName")
display = client.read("ns=1;i=1204", attr="DisplayName")
klass = client.read("ns=1;i=1204", attr=AttributeId.NODE_CLASS)
access = client.read("ns=1;i=1204", attr=AttributeId.ACCESS_LEVEL)
```

The `attr=` value can be either a string (case-insensitive, ignores punctuation — `"BrowseName"`, `"browse_name"`, `"BROWSENAME"` all match) or an `o6.AttributeId` enum member if you want exactness.

### Write a non-`Value` attribute

Writing a non-`Value` attribute uses both `value=` and `attr=`. Attributes that are themselves structured types — `Description` is a `LocalizedText` — must be wrapped in the matching type:

```python
from o6 import Client, LocalizedText

status = client.write(
    "ns=1;i=1204",
    value=LocalizedText("Target kettle temperature"),
    attr="Description",
)
print(status)   # GOOD on success
```

#### Putting it all together

```python
from o6 import AttributeId, Client, LocalizedText

with Client("opc.tcp://localhost:4840") as client:
    name = client.read("ns=1;i=1204", attr="BrowseName")
    print(name)

    klass = client.read("ns=1;i=1204", attr=AttributeId.NODE_CLASS)
    print(klass)

    access = client.read("ns=1;i=1204", attr=AttributeId.ACCESS_LEVEL)
    print("writable:", bool(access & 2))

    status = client.write(
        "ns=1;i=1204",
        value=LocalizedText("Target kettle temperature"),
        attr="Description",
    )
    print("description write:", status)
```

---

## What's next?

- [Call a method](130_call-method.md) — same shape of call, but for methods on objects.
- [Low-level service calls](500_lowlevel-service-calls.md) — drop down to the raw `Read` / `Write` service when you need full control over the request.
