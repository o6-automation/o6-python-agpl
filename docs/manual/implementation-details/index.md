# Implementation details

This section describes how o6\\Python itself works. The audience is readers
who need to understand the binding's mechanics — for example, to debug a
non-obvious failure, to extend the binding safely, or to evaluate whether a
particular use case is supported. Pages here are written to be read
individually, not top to bottom.

!!! info
    Nothing in this section is required to use the SDK. The pages assume
    familiarity with the corresponding user-facing pages; each page lists the
    prerequisite reading at the top.

## Contents

| Section | What it covers |
|---|---|
| [Memory management](memory-management.md) | How Python reference counting and open62541's C lifetimes are joined. |
| [Variable callbacks](variable-callbacks.md) | How `o6.read`/`o6.write` and `Server.implement` are dispatched. |
| [Namespace matching](namespace-matching.md) | How `Client.connect` maps server `ns=N` indices to a process-wide namespace module. |
| [GIL and event-loop bridging](gil-and-event-loop.md) | How the custom `AsyncIOLoop` integrates open62541 with asyncio without deadlocking. |
| [Wire-format ↔ Python-value mapping](wire-format-mapping.md) | The `PY2UA` / `UA2PY` dispatchers and the kind-to-conversion table. |
