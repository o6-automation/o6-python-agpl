# Client Tutorials

These tutorials walk through the client-side features of `o6` against a single, fixed example server that runs against a background simulation. Every snippet on every page assumes you can reach that server at `opc.tcp://localhost:4840` and that its address space looks like the layout described in [Set the Stage](../setup.md).

The pages build on each other — each one introduces one concept at a time and reuses the same server, so by the end you have walked through the full lifecycle: connecting, reading values, calling methods, subscribing to live data, reacting to state changes, and so on.

!!! tip "Start the server first"
    Save [`server.py`](../server.py) and [`sim.py`](../sim.py) into the same folder, and leave the server running in its own terminal:

    ```bash
    python server.py
    ```

    [Set the Stage](../setup.md) walks through it, and lists every NodeId the pages below use.

---

## Topics

The tutorials are organized around what you typically *do* with a client:

---
First Steps
---
1. [Connect / disconnect](100_connect.md)
2. [Browse](110_browse.md)
3. [Read / write value](120_read-write-node.md)
4. [Call a method](130_call-method.md)
5. [Node API syntax](140_node-api-syntax.md)
---
Monitoring
---
6. [Monitor Datachange](200_monitor-datachange.md)
7. [Subscriptions](210_subscriptions.md)
8. [Modify a subscription](220_modify-subscription.md)
9. [Filter](230_subscription-filter.md)
10. [Listen to events](240_listen-to-events.md)
---
Client Configuration
---
11. [Security](300_security.md)
12. [Application Description](310_application-description.md)
13. [State Callbacks](320_state-callbacks.md)
---
Information Modeling
---
14. [Load packaged companion specs](410_load-packaged-companion-specs.md)
15. [Load nodeset files](420_load-nodeset-files.md)
16. [NodeIds and namespace info](430_nodeids-and-namespace-info.md)
17. [Semantic Discovery](440_semantic-discovery.md)
---
Advanced Topics
---
18. [Low-level service calls](500_lowlevel-service-calls.md)
19. [Async client](510_async-client.md)

---

## Beyond the tutorials

- [Client manual](../../manual/client/index.md) — the connected picture behind these pages: the two service layers, sync vs. async, lifecycle.
- [Node API](../../manual/node-api.md) — the object-oriented view of the address space.
- [API Reference](../../api_reference/client.md) — every public method and its signature.
