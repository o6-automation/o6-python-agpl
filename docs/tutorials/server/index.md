# Server Tutorials

These tutorials build an o6\\Python server one concept at a time. The domain throughout is a small automated distillery: a still driven by a background simulation that exposes its state under `Objects/DistillingSystem` and accepts two writes, `Operating` (run / park) and `Setpoint` (target kettle temperature). The [client tutorials](../client/index.md) connect to this server.

The Foundation tutorials build one runnable project. The other groups cover
independent patterns and additional server features.

The [server examples](../../examples.md#server) provide complete scripts for the
Foundation and Patterns topics. [Set the Stage](../setup.md) provides the
complete runnable distillery.

!!! tip "Read Foundation in order"
    Each Foundation page builds on the previous page. Start with
    [Creating a server](100_create-server.md) so the imports and identifiers
    in the snippets match your project.

## Contents

Read Foundation in order. Patterns are self-contained examples; the later groups cover modelling, behaviour, and security.

### Foundation

| Topic | What it covers |
|---|---|
| [Creating a server](100_create-server.md) | Creating, starting, and stopping a server. |
| [Add a hierarchy](105_add-hierarchy.md) | Grouping nodes under the distillery's object hierarchy. |
| [Add a variable](110_add-variable.md) | Adding variables and configuring their values. |
| [Add a method](120_add-method.md) | Exposing Python callbacks as OPC UA methods. |

### Patterns

| Topic | What it covers |
|---|---|
| [Values from an external source](130_data-source.md) | Updating variables from an external Python model. |
| [Running on asyncio](140_async-server.md) | Running the server and update tasks with asyncio. |
| [Declare and implement a Variable](150_implement-variable.md) | Declaring a Variable and implementing its read/write behaviour. |
| [Declare and implement an ObjectType](160_implement-objecttype.md) | Declaring an ObjectType and implementing its Methods. |

### Composition

| Topic | What it covers |
|---|---|
| [Declare an object type](200_declare-object-type.md) | Defining and instantiating ObjectTypes with Python classes. |
| [Declare a variable type](210_declare-variable-type.md) | Declaring VariableTypes, datatypes, and value ranks. |
| [Declare a reference type](220_declare-reference-type.md) | Declaring custom relationships between nodes. |
| [Declare a data type](230_declare-data-type.md) | Declaring structures and enums for variables and methods. |

### Behaviour

| Topic | What it covers |
|---|---|
| [Method implementations](310_method-implementations.md) | Installing and replacing Method callbacks. |
| [Variables with sources](320_variables-with-sources.md) | Reading and writing variables through callbacks. |
| [Server callbacks](330_server-callbacks.md) | Lifecycle callbacks, repeated work, and retention cleanup. |
| [Events](340_events.md) | Creating event types, sources, and notifications. |
| [Timers and async loops](350_timers.md) | Scheduling async work and handling cancellation. |

### Security

| Topic | What it covers |
|---|---|
| [Access control — roles](400_access-control-roles.md) | Defining roles and granting node permissions. |
| [Access control — authentication](410_access-control-auth.md) | Authenticating sessions and assigning roles. |
| [Security policies and endpoints](420_security-policies.md) | Configuring encryption, endpoints, and certificates. |
| [Subscribe monitoring on the server side](430_server-monitoring.md) | Monitoring variables and events inside the server. |
| [Historical data](440_history.md) | Recording and serving historical values. |

### Complete example

| Topic | What it covers |
|---|---|
| [The distillery server](500_distillery_server.md) | The complete distillery project and its relationship to the tutorials. |

## Related topics

| Topic | What it covers |
|---|---|
| [Server manual](../../manual/server/index.md) | Server concepts, lifecycle, and operations. |
| [Lifecycle & configuration](../../manual/server/lifecycle.md) | Creating, configuring, and running a server. |
| [Building the address space](../../manual/server/address-space.md) | Adding nodes, variables, methods, and references. |
| [Declared types](../../manual/information-model-authoring/publishing.md) | Building an address space from an information model. |
| [Implementing behaviour](../../manual/information-model-authoring/implementing-types.md) | Attaching Python implementations to declared types. |
| [Server callbacks](../../manual/server/callbacks.md) | Callback signatures and resolution order. |
| [Events, monitored items & timers](../../manual/server/events.md) | Server-side notifications and periodic work. |
| [Access control & roles](../../manual/server/security.md) | Authentication and authorization. |
| [Operations & interoperability](../../manual/server/local-nodes.md) | History, discovery, reverse connect, and PubSub. |
| [API Reference](../../api_reference/server.md) | Public server methods and their signatures. |
