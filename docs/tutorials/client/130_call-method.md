# Call a method

You've discovered the writable nodes, peeked at the state, and adjusted the still's `Setpoint`. Methods are the on-switches — `Start` kicks off a batch, `Shutdown` ends it.

This is the second half of the control loop. You know what the still is doing and told it what to change, now the still can actually start - flip the on-switch.

`client.call` invokes an OPC UA method on a server object. It takes the *object* the method belongs to, the *method* NodeId, and a list of input arguments, and returns a tuple `(status_code, *output_arguments)`.

This page walks through three steps:

- Build the object and method NodeIds.
- Call a method and read the result.
- Handle the case where the method takes inputs.

!!! info
    This tutorial expects the [example server running](../../tutorials.md#running-the-example-server) in the background, and assumes you know how to [create and connect](100_connect.md) a client and how to [browse](110_browse.md) the address space. The `NodeId`s used below are the ones exposed by the distilling example server's `DistillingSystem` object at `ns=1;i=1000`.

---

## Build the object and method NodeIds

The distilling server exposes two methods on the `DistillingSystem` object at `ns=1;i=1000`:

- **`Start`** at `ns=1;i=2001` — Start a new distilling batch.
- **`Shutdown`** at `ns=1;i=2002` — Stop the current batch.

A method always belongs to an object. `client.call`'s signature takes them as two separate arguments — the *parent* object NodeId and the *method* NodeId:

```python
parent = "ns=1;i=1000"   # DistillingSystem
method = "ns=1;i=2001"   # Start
```

The parent is the object node that *owns* the method (`DistillingSystem` in the example server), and the method NodeId is the method node itself. Both are normal `o6.NodeId` strings — see [NodeIds and namespace info](430_nodeids-and-namespace-info.md) for the full syntax.

---

## Call the method and read the result

`client.call` returns a tuple `(status_code, *output_arguments)`. For a method with no inputs and no outputs, that is just `(status_code,)` — destructure it to read the call result.

Let's start a new batch on the Distilling System and look at the 'StatusCode' to see whether the call was successfull:

```python
import o6

status, = client.call(parent, method)
print(status == o6.StatusCode.GOOD)
```

A status equal to `o6.StatusCode.GOOD` means the server accepted the call and the method ran. A non-`Good` status means the call was rejected before it reached the method — for example, a bad object/method NodeId pair, a security rejection, or a wrong arity. `client.call` does not raise on a rejected call; it hands you the `StatusCode` and lets you decide.

#### Putting it all together

```python
import o6
from o6 import Client

with Client("opc.tcp://localhost:4840") as client:
    parent = "ns=1;i=1000"   # DistillingSystem
    method = "ns=1;i=2001"   # Start

    status, = client.call(parent, method)
    print(status == o6.StatusCode.GOOD)
```

---

## Handle the case where the method takes inputs

The distilling server's methods take no inputs, but most real-world methods do. When a method declares inputs, pass them as a list as the third argument to `client.call`. A method with a single input:

```python
status, greeting = client.call(parent, "ns=1;s=TestMethods.Hello", ["World"])
```

A method with several inputs takes a list of the same length, in declaration order:

```python
client.call(parent, method, [arg1, arg2, arg3])
```

If a method declares inputs but you pass too few or too many, the server will reject the call and the status code will not be `Good`. There is no Python-side type checking on the input list — the values are forwarded to the server as-is, and the server's type system decides whether they match the method signature.

!!! info
    The distilling server's `Start` and `Shutdown` methods take no inputs, so this section is illustrative — the snippets use generic `TestMethods.Hello`-style methods that you'd find on a typical server. On the distilling server itself, stick to the no-input pattern from the previous section.

---

## What's next?

- [Monitor data changes](200_monitor-datachange.md) — push value changes from the server to a callback.
- [Low-level service calls](500_lowlevel-service-calls.md) — drop down to `client.serviceCall(...)` when you need full control over the `Call` request.
