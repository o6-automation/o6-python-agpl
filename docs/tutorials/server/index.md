# Server Tutorials

These tutorials walk through the server side of `o6` by **building one server, one concept at a time**. The Foundation band builds one continuous project — a small distillery exposing an object hierarchy, live variables, and methods — and that project is the same distillery the [client tutorials](../client/index.md) ultimately connect to. Everything after Foundation applies the same domain, but as separate techniques you would reach for on a real deployment — Patterns, Composition, Behaviour, and Production are not folded back into that one running example. 

The pages build on each other in ascending complexity. Each one introduces one concept and leaves the server runnable, so you can leave it running between pages and watch the address space grow.

!!! tip "Start from the first page"
    The project state at the top of each page is the project state at the
    bottom of the previous one. If you skip ahead, the imports and identifiers
    in the snippets will not match what you have.

## Building a distillery server

Throughout the tutorials we build, one concept at a time, the same **automated distillery**: a still driven by a background simulation, exposing its state under `Objects/DistillingSystem` and accepting two writes — `Operating` (run / park) and `Setpoint` (target kettle temperature). On the way there we:

- start with the smallest possible server, then grow the address space by hand — that's the whole Foundation band, and it's the one continuous project;
- then work through the same handful of patterns the [server examples](../../examples.md#server) walk through — an external data source, an asyncio server, and the declare/implement split for a Variable and for an ObjectType — each as its own small, self-contained aside rather than a further extension of the running distillery;
- take a detour through the declarative alternative in depth — the same shapes as `@o6.objecttype`/`@o6.variabletype`/`@o6.datatype` classes, and custom `ReferenceType`s — as a technique worth knowing once a model gets bigger than a handful of nodes;
- attach write handlers, method implementations, events and timers once the hand-built data model is worth reacting to;
- then take a second detour through access control, authentication, security policies, monitoring and history — everything a server needs before it is hosted on a real network, but not things this particular small distillery turns on.

The very last page — [The distillery server](500_distillery_server.md) — points back at [Set the stage](../setup.md), which describes the two-file runnable project the Foundation band builds up to, and says plainly which bands are and aren't part of it.

## Topics

The tutorials are organised around what you typically *build* on a server, moving from the smallest runnable program to a fully modelled, secured endpoint. The first two bands track the same order as the [server examples](../../examples.md#server), one page per example; everything after that goes further than the examples do.

---
Foundation
---
1. [Creating a server](100_create-server.md) — create a `Server`, bind an endpoint, start it, stop it.
2. [Add a hierarchy](105_add-hierarchy.md) — group nodes into a small hierarchy under `Objects/`.
3. [Add a variable](110_add-variable.md) — drop the first values into the right slots.
4. [Add a method](120_add-method.md) — register a callable method, return values and `StatusCode`.
---
Patterns
---
The same shapes as the `S07`–`S10` server examples, each as its own small aside rather than a further extension of the running distillery.

5. [Values from an external source](130_data-source.md) — a Variable whose truth lives in a Python model, pushed in with `server.write(...)`.
6. [Running on asyncio](140_async-server.md) — `async with server:`, `await asyncio.sleep(...)`, and `asyncio.run(...)`.
7. [Declare and implement a Variable](150_implement-variable.md) — declare a Variable as a contract, implement its `read`/`write` in a separate class.
8. [Declare and implement an ObjectType](160_implement-objecttype.md) — the same declare/implement split, for a Method.
---
Composition
---
9. [Declare an object type](200_declare-object-type.md) — turn the hand-built hierarchy into a Python class with `@o6.objecttype`, define components, instantiate.
10. [Declare a variable type](210_declare-variable-type.md) — `@o6.variabletype` for typed values with their own `DataType`, `ValueRank`, modelling rules.
11. [Declare a reference type](220_declare-reference-type.md) — custom `ReferenceType`s for relationships beyond `HasComponent` / `HasProperty`.
12. [Declare a data type](230_declare-data-type.md) — `@o6.datatype` for a custom `Structure` / `Enum` used by your variables and methods.
---
Behaviour
---
The data model is now in place; the next band is what makes it *do* something — the instance-level counterpart to the declare/implement classes in Patterns.

13. [Method implementations](310_method-implementations.md) — install callbacks with `Server.implement(method, call=...)`, sync vs async, error mapping.
14. [Variables with sources](320_variables-with-sources.md) — install read and write callbacks with `Server.implement(variable, read=..., write=...)`, validate, mirror.
15. [Server callbacks](330_server-callbacks.md) — startup, shutdown, periodic timers, retention cleanup.
16. [Events](340_events.md) — the distillery's writable "event log" pattern, firing on state transitions, and when to graduate to real `BaseEventType` / `emitEvent` notifications.
17. [Timers and async loops](350_timers.md) — long-running background work, `asyncio` integration, cooperative cancellation.
---
Production
---
Take the distillery from "demo" to "ready for production".

18. [Access control — roles](400_access-control-roles.md) — `Role` / `o6.roles`, default-deny, granting reading / writing / calling per node, role mappings for built-in roles.
19. [Access control — authentication](410_access-control-auth.md) — session authentication, user token policies.
20. [Security policies and endpoints](420_security-policies.md) — `SecurityPolicy` selection, encrypted endpoints, certificate management.
21. [Subscribe monitoring on the server side](430_server-monitoring.md) — server-local monitored items for housekeeping.
22. [Historical data](440_history.md) — `historizing=True`, `server.config.setHistoryDatabase(...)` + `server._register_historizing(...)`, real `HistoryRead` against buffered values, and the `allowHistoryUpdate` / `allowHistoryDelete` hooks.

*The distillery page that finishes the project — [500_distillery_server.md](500_distillery_server.md) — defers to [Set the stage](../setup.md), which is the same server in runnable form: the Foundation band, built incrementally, plus the plain write-loop pattern from [Values from an external source](130_data-source.md). Patterns, Composition, Behaviour, and Production are separate techniques applied to the same distillery, not part of that one running file — 500_distillery_server.md says so explicitly.*

## Beyond the tutorials

The server manual collects the same topics as long-form narrative:

- [Server manual](../../manual/server/index.md) — the full narrative.
    - [Lifecycle & configuration](../../manual/server/lifecycle.md)
    - [Building the address space](../../manual/server/address-space.md)
    - [Declared types](../../manual/server/declared-types.md)
    - [Implementing behaviour](../../manual/server/behaviour.md)
    - [Server callbacks](../../manual/server/callbacks.md)
    - [Events, monitored items & timers](../../manual/server/events-and-timers.md)
    - [Access control & roles](../../manual/server/security.md)
    - [Operations & interoperability](../../manual/server/operations.md)
- [API Reference](../../api_reference/server.md) — every public method and its signature.
