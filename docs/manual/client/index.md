# Client

This section is the complete story of `o6.Client`. This page covers what a
client *is* and how one API serves both synchronous and asynchronous code. From
there:

- [Lifecycle](lifecycle.md) — constructing a client, discovery,
  connecting and disconnecting, sessions and channels.
- [Working with the address space](address-space.md) — reading, writing,
  calling, browsing, namespaces and NodeIds, and node management.
- [Subscriptions and historical data](subscriptions.md) — monitored
  items, subscriptions, and history.
- [Raw services and errors](raw-services.md) — the service-level
  interface and status-code handling.

The [tutorials](../../tutorials/index.md) walk through the same material task by task with
a running example server. This page is the connected picture behind them.

## The two layers

OPC UA is specified in terms of *service sets* — groups of related operations
such as SecureChannel and Session management, Discovery, Read/Write, Browse,
Method Call, and Subscriptions. `o6.Client` exposes those services on two
levels.

The **raw service interface** mirrors the specification one-to-one. Every method
is named `serviceX` — `serviceRead`, `serviceBrowse`, `serviceCall` — takes a
request object from the generated data types, and returns the full response
object. Nothing is interpreted for you: you build the request, you inspect
`responseHeader.serviceResult`, you unpack the results.

The **high-level interface** sits on top and covers the workflows applications
actually need: connect, read, write, browse, call, subscribe. It builds the
request objects, manages the SecureChannel and the Session, resolves NodeIds
across namespaces, decodes results into Python values, and works identically
from synchronous and asynchronous code. For the overwhelming majority of
applications this is the layer to use; reach for the raw services only when you
need a parameter the high-level call does not expose.

Both layers live on the same object, so you can mix them freely in one program.

## One API, synchronous or asynchronous

Every request-issuing method on the client — `connect`, `read`, `write`,
`browse`, `call`, `monitor`, all the `serviceX` methods — has a single
implementation that adapts to the calling context.

Called from ordinary synchronous code, the call **blocks** and returns the
result:

```python
value = client.read("ns=1;s=IntegerVariable")
```

Called from inside a coroutine, the very same call returns something awaitable:

```python
value = await client.read("ns=1;s=IntegerVariable")
```

What makes this work is a private event loop plus a worker thread. When you do
not pass `loop=`, the client creates its own loop, runs it on a daemon worker
thread, and every synchronous call is dispatched onto that thread and waited
for. When you *do* pass a loop, the client uses it and expects you to run it;
calls made from that loop are returned as awaitables, calls made from another
thread are scheduled onto it and block the caller. IPython and Jupyter are
detected specially: because the kernel's loop is already running and cannot be
blocked, the client always gets its own loop there, and synchronous calls keep
working in a notebook cell.

`client.loop` exposes the loop; it is fixed at construction time.

The practical rules that follow from this:

- Do not `await` a call in synchronous code, and do not forget to `await` it in
  async code. The return value is the plain result in the first case and an
  awaitable in the second.
- A client is bound to one loop for its whole life. To use one from several
  event loops, create one client per loop.
- Callbacks (data changes, events, subscription lifecycle) are invoked on the
  client's loop thread. Keep them short and never block them; hand work off to a
  queue if it takes real time.
- After `disconnect()` the worker thread is stopped. Calling a service method
  then raises `RuntimeError("Client event loop is not running")`.

The [Async client tutorial](../../tutorials/client/510_async-client.md) covers loop
ownership in more depth.

## Where to go next

- [First steps tutorials](../../tutorials/index.md) — connect, browse, read/write, call, all
  against a running example server.
- [Node API](../node-api.md) — the object-oriented view of the address space.
- [Namespace mapping in o6](../sdk-fundamentals/namespace/namespace-mapping-in-o6.md)
  — how NodeIds, namespaces, and compiled nodesets fit together.
- [Server](../server/index.md) — the other half, for building the server this client
  talks to.
- [Performance](../performance.md) — batching, buffer sizes, and what to expect
  from large arrays.
- [API Reference](../../api_reference) — the generated signature-level reference for
  every method mentioned here.
