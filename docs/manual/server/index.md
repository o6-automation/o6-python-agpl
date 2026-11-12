# Server

This chapter covers `o6.Server`. This page describes the two ways to build an
address space and how one API serves synchronous and asynchronous code.

## Contents

| Topic | What it covers |
|---|---|
| [Lifecycle & Configuration](lifecycle.md) | Constructing, configuring, starting, and stopping a server. |
| [Building the Address Space](address-space.md) | Creating nodes and managing their references and lifetime. |
| [Working with Local Nodes](local-nodes.md) | Local lookup, reads, writes, Method calls, and browsing. |
| [Callbacks & External Data](callbacks.md) | Callback arguments, results, external values, and async execution. |
| [Timers & Periodic Updates](timers.md) | Scheduling periodic application updates. |
| [Events](events.md) | Emitting events from drafts, instances, and node handles. |
| [Local Monitored Items](monitoring.md) | Observing local values and events without a client session. |
| [Historical Data](history.md) | Recording values and configuring history storage. |
| [Access Control & Roles](security.md) | Authentication, sessions, roles, and node permissions. |
| [Discovery & Registration](discovery.md) | mDNS announcements, LDS hosting, and application registration. |
| [Reverse Connect](reverse-connect.md) | Initiating connections to listening clients. |
| [Application Notifications](notification-handler.md) | Lifecycle, session, service, discovery, and audit notifications. |
| [PubSub](pubsub.md) | Configuring and controlling publisher/subscriber communication. |

The [Client](../client/index.md) chapter covers the client side.


## Two ways to build an address space

A server exposes nodes. `o6` offers two ways to create them.

The *imperative route* uses the `addX` helpers on the server object, such as
`addObject`, `addVariable` and `addMethod`. Each call creates one node at
runtime and returns a Python node handle. Use it for scripts, gateways and
address spaces whose shape comes from configuration rather than from a model.

The *declarative route* writes an OPC UA information model as Python classes
(`@o6.objecttype`, `@o6.variabletype`, `@o6.datatype` and the rest) in a
namespace module. The server publishes the module with
`server.ns.append(module)`. Instantiating a type creates a complete typed
subtree, and the Python class carries the behaviour. Use it when the address
space is a model: a companion specification, a product line, or anything a
client should discover by type.

You can mix both routes in one server. All nodes end up in the same nodestore.

This chapter starts with the imperative route and local operations. The later
[Information Model Authoring](../information-model-authoring/index.md) chapter
covers declarations, instantiation, and implementation classes for both
handwritten and compiled models.

## One API, synchronous or asynchronous

A synchronous script can create a Variable and keep serving until Ctrl+C.
The context manager starts the server and stops it on exit:

```python
import time
import o6

try:
    with o6.Server(port=4840) as server:
        temperature = server.addVariable("Temperature", server.objects, 22.5)
        print(temperature())
        while True:
            time.sleep(1)
except KeyboardInterrupt:
    pass
```

In an async application, create the server inside `main()`, use `async with`,
and await node operations. This serves the same value until Ctrl+C:

```python
import asyncio
import o6

async def main():
    async with o6.Server(port=4840) as server:
        temperature = await server.addVariable("Temperature", server.objects, 22.5)
        print(await temperature())
        await asyncio.Event().wait()

try:
    asyncio.run(main())
except KeyboardInterrupt:
    pass
```

| Kind of API | Synchronous code | Async task |
|---|---|---|
| Node creation, lookup, navigation, reads, writes, and Method calls | Use the returned result. | Await the operation, even for local data available immediately. |
| Server lifetime | Use `with server`. | Use `async with server`. |
| Constructors, configuration, and metadata such as `server.objects` or `node._nodeid` | Use directly. | Use directly, without `await`. |
| Callbacks | Local operations can finish immediately; pending work needs an async handler. | Await operations inside `async def` callbacks. |

The operation rule also applies before startup and inside ordinary helpers
called by an async task. Property syntax for a child or attribute still performs
an operation. For writes in async code, use `await temperature(value)`.

Configure the server before entering the context manager. Manual `start()` and
`stop()` calls have their own readiness and shutdown rules; they do not follow
the node-operation rule. See [Lifecycle & Configuration](lifecycle.md).

Keep callbacks short: blocking one can stall the server. The
[callback chapter](callbacks.md#calling-the-api-from-callbacks) explains immediate
and pending callback operations. Custom loops and calls from other threads
are covered in [Event loops and integration](lifecycle.md#event-loops-and-integration).
