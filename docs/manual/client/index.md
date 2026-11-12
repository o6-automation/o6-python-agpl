# Client

This chapter covers `o6.Client`. This page explains the client's two API
layers and how one API serves both synchronous and asynchronous code.

## Contents

| Topic | What it covers |
|---|---|
| [Lifecycle & Configuration](lifecycle.md) | Constructing, configuring, connecting, and cleaning up a client. |
| [Reading, Writing & Calling](read-write-call.md) | Attribute values, batch operations, and Method results. |
| [Browsing & Node Lookup](browsing.md) | Discovery of nodes, typed lookup, paths, pagination, and datatype metadata. |
| [Subscriptions & Events](subscriptions.md) | Monitoring values and events and managing subscriptions. |
| [Historical Data](history.md) | Reading and updating recorded values. |
| [Changing the Address Space](node-management.md) | Creating and deleting remote nodes and references. |
| [Discovery & Registration](discovery.md) | Finding endpoints and registering applications with an LDS. |
| [Advanced Session Management](sessions.md) | Session transfer and reverse connect. |
| [Raw Services](raw-services.md) | Request/response structures and bounded concurrency. |
| [Application Notifications](notification-handler.md) | Observing connection lifecycle and service calls. |

The [tutorials](../../tutorials/index.md) cover the same material task by task
against a running example server.

## The two layers

OPC UA groups its operations into *service sets*, such as SecureChannel and
Session management, Discovery, Read/Write, Browse, Method Call and
Subscriptions. `o6.Client` exposes these services on two levels:

- The *raw service interface* mirrors the specification one-to-one. Each
  method is named `serviceX` (`serviceRead`, `serviceBrowse`, `serviceCall`),
  takes a request object from the generated data types and returns the full
  response object. You build the request, check
  `responseHeader.serviceResult` and unpack the results yourself.
- The *high-level interface* covers connect, read, write, browse, call and
  subscribe. It builds the request objects, manages the SecureChannel and the
  Session, resolves NodeIds across namespaces, decodes results into Python
  values and works the same from synchronous and asynchronous code.

Use the high-level interface by default. Use the raw services when you need a
parameter the high-level call does not expose. Both layers live on the same
object, so you can mix them in one program.

## One API, synchronous or asynchronous

In an ordinary script, operations return their results directly. This complete
example connects to a running server, reads its standard CurrentTime Variable
(`i=2258`), and disconnects on exit:

```python
import o6

with o6.Client("opc.tcp://localhost:4840") as client:
    print(client.read("i=2258"))
```

In an async application, use `async with` and await operations. Create the
client inside `main()`:

```python
import asyncio
import o6

async def main():
    async with o6.Client("opc.tcp://localhost:4840") as client:
        print(await client.read("i=2258"))

asyncio.run(main())
```

The same rule applies to the Node API introduced in the preceding chapter.
An ordinary `def` helper called by an async task also receives an awaitable
from an operation. It can return that awaitable for its caller to await;
putting a call in a helper does not make it synchronous.

| Kind of API | Synchronous code | Async task |
|---|---|---|
| Requests: read, write, browse, call, monitoring, raw services | Use the returned result. | Await the operation. |
| Connection lifetime | Use `with client`. | Use `async with client`. |
| Constructors, configuration, and metadata such as `client.connected` or `node._nodeid` | Use directly. | Use directly, without `await`. |
| Callbacks | Keep plain handlers short; use `async def` for work that must await. | Async handlers await their operations. |

Child navigation and attribute reads are operations, even when written with
property syntax. Standard folder handles such as `client.objects` are already
available and need no await. Use callable-node writes in async code rather
than assigning to `_value`.

The SDK manages the default execution setup for both examples. Custom loops,
notebooks, and calls from other threads are covered later in
[Event loops and integration](lifecycle.md#event-loops-and-integration).
