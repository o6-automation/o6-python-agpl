# Client Tutorials

These tutorials cover the client features of `o6`. They run against one example server backed by a simulation. Every snippet assumes the server is reachable at `opc.tcp://localhost:4840` with the address space described in [Set the Stage](../setup.md).

Each page introduces one concept and builds on the earlier pages. Together they cover the client lifecycle: connecting, reading values, calling methods, subscribing to live data and reacting to state changes.

!!! tip "Start the server first"
    Save [`server.py`](../server.py) and [`sim.py`](../sim.py) into the same folder, and leave the server running in its own terminal:

    ```bash
    python server.py
    ```

    [Set the Stage](../setup.md) explains the server and lists every NodeId the pages below use.

---

## Contents

### First Steps

| Topic | What it covers |
|---|---|
| [Connect / disconnect](100_connect.md) | Connecting to a server and closing the session. |
| [Browse & Explore](110_browse.md) | Browsing nodes, references, and the address-space hierarchy. |
| [Reading & Writing](120_read-write-node.md) | Reading and writing node values and attributes. |
| [Calling a method](130_call-method.md) | Calling methods and handling their results. |
| [Node API syntax](140_node-api-syntax.md) | Dot, bracket, and call syntax for working with nodes. |

### Monitoring

| Topic | What it covers |
|---|---|
| [Monitor datachange](200_monitor-datachange.md) | Receiving variable changes through a callback. |
| [Subscriptions](210_subscriptions.md) | Creating subscriptions and attaching monitored items. |
| [Modify a subscription](220_modify-subscription.md) | Changing subscription settings without recreating the subscription. |
| [Filter](230_subscription-filter.md) | Sampling intervals, queues, monitoring modes, and deadband filters. |

### Client Configuration

| Topic | What it covers |
|---|---|
| [Security](300_security.md) | Configuring encryption, certificates, and authentication. |
| [Application Description](310_application-description.md) | Identifying the client application to the server. |
| [State Callbacks](320_state-callbacks.md) | Observing connection, session, and channel state changes. |

### Information Modelling

| Topic | What it covers |
|---|---|
| [Load packaged companion specs](410_load-packaged-companion-specs.md) | Loading bundled companion specifications on a client. |
| [Load nodeset files](420_load-nodeset-files.md) | Loading vendor or custom nodeset XML files. |
| [NodeIds and namespace info](430_nodeids-and-namespace-info.md) | Resolving NodeIds and inspecting namespace metadata. |
| [Semantic Discovery](440_semantic-discovery.md) | Finding nodes by BrowseName and information-model structure. |

### Advanced Topics

| Topic | What it covers |
|---|---|
| [Low-level service calls](500_lowlevel-service-calls.md) | Building and sending raw OPC UA service requests. |
| [Async Clients](510_async-client.md) | Using client operations with asyncio. |

## Related topics

| Topic | What it covers |
|---|---|
| [Listen to events](240_listen-to-events.md) | Monitoring events and filtering their fields. |
| [Client manual](../../manual/client/index.md) | The two service layers, sync vs. async, lifecycle. |
| [Node API](../../manual/node-api/index.md) | The object-oriented view of the address space. |
| [API Reference](../../api_reference/client.md) | Every public method and its signature. |
