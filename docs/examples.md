# Examples

Complete runnable scripts, each with a walkthrough. They are grouped into
Client, Server, Type Authoring, and Advanced Applications.

Within a series, later examples build on earlier ones. Most client examples
expect an OPC UA server on `opc.tcp://localhost:4840`; each example's page says
which server script to start first. To use another port, set `O6_EXAMPLE_PORT`
to the same value for both scripts. The automated checker assigns an isolated
port to each example group and prints the directory that holds its process
logs.

## Contents

### Client

| Topic | What it covers |
|---|---|
| [Low-level](examples/client-C01_lowlevel.md) | Connecting and sending raw OPC UA service requests. |
| [First Steps](examples/client-C02_firststeps.md) | Connecting, browsing, reading, writing, and calling methods. |
| [Browsing](examples/client-C03_browsing.md) | Exploring nodes and references in the address space. |
| [Configuration](examples/client-C04_configuration.md) | Configuring a client before connecting. |
| [Username / Password Authentication](examples/client-C05_usernamepw.md) | Authenticating with a username and password. |
| [Sync/Async Calling Patterns](examples/client-C06_async_modes.md) | Using synchronous and asynchronous client operations. |
| [Node Management](examples/client-C07_nodemanagement.md) | Adding and deleting nodes and references. |
| [Subscriptions](examples/client-C08_subscriptions_firststeps.md) | Subscribing to variable changes. |
| [Subscription Modification](examples/client-C09_subscriptions_modify.md) | Changing an existing subscription and its monitored items. |
| [Subscription Events](examples/client-C10_subscriptions_events.md) | Subscribing to events and filtering their fields. |
| [Subscription Triggering](examples/client-C11_subscriptions_triggering.md) | Linking monitored items with subscription triggering. |
| [Interactive Browser](examples/client-C12_browser.md) | Exploring a server with an interactive terminal browser. |

### Server

| Topic | What it covers |
|---|---|
| [Low-level](examples/server-S01_lowlevel.md) | Building a server through the low-level API. |
| [Minimal](examples/server-S02_minimal.md) | Starting and stopping a minimal server. |
| [First Steps](examples/server-S03_firststeps.md) | Creating an address space and updating values. |
| [Variables](examples/server-S04_variables.md) | Adding variables and configuring their attributes. |
| [Objects](examples/server-S05_objects.md) | Organizing nodes into objects and hierarchies. |
| [Methods](examples/server-S06_methods.md) | Exposing Python callbacks as OPC UA methods. |
| [Data Source Updates](examples/server-S07_data_source.md) | Updating variables from an external data source. |
| [Async](examples/server-S08_asynchronous.md) | Running a server and update tasks with asyncio. |
| [Variable Read/Write Override](examples/server-S09_implement_readwrite.md) | Implementing a declared Variable's read and write behaviour. |
| [ObjectType Implementation](examples/server-S10_implement_objtype.md) | Attaching behaviour to a declared ObjectType. |
| [History](examples/server-S11_history.md) | Storing variable history and reading it from a client. |

### Type Authoring

| Topic | What it covers |
|---|---|
| [Types (Low-level)](examples/type_authoring-T01_lowlevel.md) | Constructing OPC UA values with low-level types. |
| [Built-in Types](examples/type_authoring-T02_types.md) | Using built-in OPC UA types in Python. |
| [Nodeset Authoring](examples/type_authoring-T03_nodeset_authoring-example.md) | Declaring and using a complete information model in Python. |

### Advanced Applications

| Topic | What it covers |
|---|---|
| [Local Discovery Server with mDNS](examples/advanced_applications-lds-server.md) | Running a Local Discovery Server with mDNS. |
