# Tutorials

The tutorials walk through the client-side features of `o6` against a single, fixed example server that runs against a background simulation. Every snippet on every page assumes you can reach that server at `opc.tcp://localhost:4840` and that its address space looks like the layout described in the following section.

The tutorials build on each other — each page introduces one concept at a time and reuses the same server, so by the end you have walked through the full lifecycle: connecting, reading values, calling methods, subscribing to live data, reacting to state changes, and so on.

---

## The example server

Every tutorial on this site talks to the same example server: a small **automated still**.

### Driven by a simulation in the background

The server runs a simulation in the background: Wash goes in, gets heated to a setpoint, vapour turns into spirit on the way through the condenser, the spent wash drains out, and the still goes back to idle and waits for the next batch. Rinse, repeat.

### Running the example server

The fastest way to get going is the standalone **`distilling`** binary, which
bundles the server and simulation into one executable. Public o6\\Python wheels
are distributed through the [`o6` project on PyPI](https://pypi.org/project/o6/).

Once the binary is on your machine, start it with the simulation enabled:

```bash
distilling --sim
```

That's the default case: the server listens on `opc.tcp://localhost:4840`. You can adjust the simulation speed with another parameter:

```bash
distilling --sim --sim-speed 10
```

!!! info
    `--port` lets you pick a different port for the server, however the tutorials all assume `4840`, so make sure to update the `endpointUrl` if you pick a different port.

### Address space layout

The server exposes the following nodes under `Objects/` (alongside the standard `Server` object that open62541 adds automatically).

```
Objects/
└── DistillingSystem                            (Object, ns=1;i=1000)
    ├── Identification                          (Object, ns=1;i=1100)
    │   ├── Name            (String, read-only)                 (ns=1;i=1101)
    │   ├── Manufacturer    (String, read-only)                 (ns=1;i=1102)
    │   └── ModelNumber     (String, read-only)                 (ns=1;i=1103)
    ├── Status                                  (Object, ns=1;i=1200)
    │   ├── State           (String, read-only)                 (ns=1;i=1201)
    │   ├── Cycle           (Int32, read-only)                  (ns=1;i=1202)
    │   ├── Operating       (Boolean, writable)                 (ns=1;i=1203)
    │   └── Setpoint        (Double °C, writable)               (ns=1;i=1204)
    ├── Kettle                                  (Object, ns=1;i=1300)
    │   ├── Level           (Double %, read-only)                (ns=1;i=1301)
    │   ├── Temperature     (Double °C, read-only)              (ns=1;i=1302)
    │   └── WashStart       (Double %, read-only)                (ns=1;i=1303)
    ├── Distillate                              (Object, ns=1;i=1400)
    │   └── Level           (Double %, read-only)                (ns=1;i=1401)
    ├── Actuators                               (Object, ns=1;i=1500)
    │   ├── FillValve       (Boolean, read-only)                (ns=1;i=1501)
    │   ├── DrainValve      (Boolean, read-only)                (ns=1;i=1502)
    │   └── Heater          (Boolean, read-only)                (ns=1;i=1503)
    ├── Events                                  (Object, ns=1;i=1600)
    │   ├── EventCount      (Int32, read-only)                  (ns=1;i=1601)
    │   ├── LastEventTime   (DateTime, read-only)               (ns=1;i=1602)
    │   ├── LastEventMessage(String, read-only)                 (ns=1;i=1603)
    │   └── LastEventState  (String, read-only)                 (ns=1;i=1604)
    ├── Start            (Method)                               (ns=1;i=2001)
    └── Shutdown         (Method)                               (ns=1;i=2002)
```

A few things worth knowing before you start poking:

- **Mostly read-only.** Almost everything in the address space is read-only from a client's perspective. The only two variables you can write are `Status/Operating` and `Status/Setpoint`, and as described above those feed back into the sim rather than directly controlling hardware. The actuators (`FillValve`, `DrainValve`, `Heater`) look tempting — they sound like switches — but they are **not** writable: the sim drives them itself as part of the batch state machine. If a tutorial tells you to write `Setpoint`, it means it; if it tells you to write `Heater`, it's lying and you should open an issue.
- **Methods.** `Start` kicks off a new batch (no-op if one is already running) and `Shutdown` aborts the current batch and puts the still back to idle. Use them as the on/off buttons.
- **Events.** The `o6` high-level Server API does not currently expose `UA_Server_createEvent` at the Python level, so the server fakes events with a small "writable event log" pattern: every state transition appends an entry to the `Events` sub-object, and clients subscribe to `EventCount` / `LastEventMessage` to react to the change. From a client point of view you treat these exactly like any other monitored variables — the subscriptions and event-listening tutorials show how. When `o6` grows a real event API, the server will swap to proper `BaseEventType` notifications behind the scenes and existing client code will keep working.

---

## Topics

The tutorials are organized around what you typically *do* with a client:

---
First Steps
---
1. [Connect / disconnect](tutorials/client/100_connect.md)
2. [Browse](tutorials/client/110_browse.md)
3. [Read / write value](tutorials/client/120_read-write-node.md)
4. [Call a method](tutorials/client/130_call-method.md)
5. [Node API syntax](tutorials/client/140_node-api-syntax.md)
---
Monitoring
---
6. [Monitor Datachange](tutorials/client/200_monitor-datachange.md)
7. [Subscriptions](tutorials/client/210_subscriptions.md)
8. [Modify a subscription](tutorials/client/220_modify-subscription.md)
9. [Filter](tutorials/client/230_subscription-filter.md)
10. [Listen to events](tutorials/client/240_listen-to-events.md)
---
Client Configuration
---
11. [Security](tutorials/client/300_security.md)
12. [Application Description](tutorials/client/310_application-description.md)
13. [State Callbacks](tutorials/client/320_state-callbacks.md)
---
Information Modeling
---
14. [Load packaged companion specs](tutorials/client/410_load-packaged-companion-specs.md)
15. [Load nodeset files](tutorials/client/420_load-nodeset-files.md)
16. [NodeIds and namespace info](tutorials/client/430_nodeids-and-namespace-info.md)
17. [Semantic Discovery](tutorials/client/440_semantic-discovery.md)
---
Advanced Topics
---
18. [Low-level service calls](tutorials/client/500_lowlevel-service-calls.md)
19. [Async client](tutorials/client/510_async-client.md)
