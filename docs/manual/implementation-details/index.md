# Implementation details

This section describes the binding mechanics of o6\\Python. Read it to debug
a non-obvious failure or to decide whether a use case is supported. Each page
stands on its own.

!!! info
    You do not need this section to use the SDK. The pages assume you know the
    corresponding user-facing pages, and most list them as prerequisites at the
    top.

## Contents

| Topic | What it covers |
|---|---|
| [Memory management](memory-management.md) | How Python reference counting and open62541's C lifetimes are joined. |
| [Variable callbacks](variable-callbacks.md) | How `o6.read`/`o6.write` and `Server.implement` are dispatched. |
| [Namespace matching](namespace-matching.md) | How `Client.connect` maps server `ns=N` indices to a process-wide namespace module. |
| [GIL and event-loop bridging](gil-and-event-loop.md) | How the custom `AsyncIOLoop` integrates open62541 with asyncio without deadlocking. |
| [Wire-format ↔ Python-value mapping](wire-format-mapping.md) | The `PY2UA` / `UA2PY` dispatchers and the kind-to-conversion table. |
