# Examples

This section collects the runnable examples that ship in `examples/` and
explains what each one demonstrates.

The examples are grouped into three series:

- **Client** — connecting, reading/writing, browsing, subscriptions, node
  management, and configuration.
- **Server** — building an address space, exposing variables, objects,
  and methods, and driving them from a simulation loop.
- **Type Authoring** — constructing OPC UA values, structures, and custom
  types in Python.

Each series is numbered and graduated: later examples build on concepts
covered earlier in the same series. Most client examples expect a
compatible OPC UA server listening on `opc.tcp://localhost:4840` — the
example's own page says which server script to start first. Set
`O6_EXAMPLE_PORT` to the same port for both scripts to use another endpoint.
The automated checker assigns an isolated port to each example group and
prints the directory containing its process logs.

## Client

- [Client (Low-level)](examples/client-C01_lowlevel.md)
- [Client First Steps](examples/client-C02_firststeps.md)
- [Client Browsing](examples/client-C03_browsing.md)
- [Client Configuration](examples/client-C04_configuration.md)
- [Client Username / Password Authentication](examples/client-C05_usernamepw.md)
- [Client Sync/Async Calling Patterns](examples/client-C06_async_modes.md)
- [Client Node Management](examples/client-C07_nodemanagement.md)
- [Client Subscriptions](examples/client-C08_subscriptions_firststeps.md)
- [Client Subscription Modification](examples/client-C09_subscriptions_modify.md)
- [Client Subscription Events](examples/client-C10_subscriptions_events.md)
- [Client Subscription Triggering](examples/client-C11_subscriptions_triggering.md)
- [Client Interactive Browser](examples/client-C12_browser.md)

## Server

- [Server (Low-level)](examples/server-S01_lowlevel.md)
- [Server Minimal](examples/server-S02_minimal.md)
- [Server First Steps](examples/server-S03_firststeps.md)
- [Server Variables](examples/server-S04_variables.md)
- [Server Objects](examples/server-S05_objects.md)
- [Server Methods](examples/server-S06_methods.md)
- [Server Data Source Updates](examples/server-S07_data_source.md)
- [Server Async](examples/server-S08_asynchronous.md)
- [Server Variable Read/Write Override](examples/server-S09_implement_readwrite.md)
- [Server ObjectType Implementation](examples/server-S10_implement_objtype.md)

## Type Authoring

- [Types (Low-level)](examples/type_authoring-T01_lowlevel.md)
- [Built-in Types](examples/type_authoring-T02_types.md)
- [Nodeset Authoring](examples/type_authoring-T03_nodeset_authoring-example.md)
