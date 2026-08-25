# Manual

The manual is the reference narrative for o6\Python. It is written as a book:
each chapter builds on the vocabulary introduced by the ones before it, so the
examples grow shorter as those concepts become familiar. It therefore reads best
from top to bottom, following the order of the navigation, through to
[Server](server/index.md).

## Contents

| # | Chapter | What it gives you |
|---|---|---|
| 1 | [OPC UA Fundamentals](opcua-fundamentals/index.md) | The specification's concepts — protocol, services, information modelling, datatypes, namespaces, nodesets. Independent of any SDK. |
| 2 | [Node API](node-api.md) | The pythonic object model that the rest of the manual uses in nearly every example. |
| 3 | [o6\Python SDK Fundamentals](sdk-fundamentals/index.md) | How the SDK maps the specification onto Python: built-in types, the namespace registry, writing and compiling nodesets. |
| 4 | [Client](client/index.md) | The complete story of `o6.Client` — lifecycle, address space, subscriptions and history, raw services. |
| 5 | [Server](server/index.md) | The complete story of `o6.Server` — lifecycle, building an address space, declared types, behaviour and callbacks, events, access control, operations. |

If you already know OPC UA, chapter 1 is a refresher you can skim — chapters 2
and 3 are worth reading even then, as they establish the notation and the type
vocabulary that the Client and Server chapters use without further comment.

Chapters 4 and 5 are written so that you can read either without knowing the other.
if you only write clients, read [Client](client/index.md) and stop; 
if you only build servers, [Server](server/index.md) stands on its own after chapter 3.

## Advanced topics

The remaining two chapters are reference material rather than part of the
reading path. Neither is required to use the SDK, their order carries no
meaning, and each page stands alone and lists its own prerequisites.

- [Performance](performance.md) — end-to-end benchmarks against native
  open62541 C and asyncua, for both the client and the server role. Consult it
  when you need numbers, or when sizing a design's throughput budget.
- [Implementation details](implementation-details/index.md) — how the binding
  itself works: memory management, variable callbacks, namespace matching, GIL
  and event-loop bridging, wire-format mapping. Consult it to diagnose a non-obvious failure,
  to extend the binding, or to judge whether an unusual use case is supported.
