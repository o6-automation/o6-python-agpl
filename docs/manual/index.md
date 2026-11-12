# Manual

The manual explains o6\\Python in navigation order. Start with the shared
concepts, types, and Node API, then learn the client and server workflows.
Information Model Authoring builds on those workflows to explain compilation,
declarations, and application behavior.

The examples assume an [installed SDK](../home/install.md). For commercial
wheels, check the [build modes and Credentials](../home/commercial-build.md)
before running a long-lived application.

## Contents

| Topic | What it covers |
|---|---|
| [OPC UA Fundamentals](opcua-fundamentals/index.md) | OPC UA protocol, services, information modelling, datatypes, and namespaces. |
| [o6\\Python SDK Fundamentals](sdk-fundamentals/index.md) | Built-in types, errors, namespace mapping, and using existing models. |
| [Node API](node-api/index.md) | Browsing and working with OPC UA nodes through Python objects. |
| [Client](client/index.md) | Client lifecycle, address-space operations, subscriptions, history, and raw services. |
| [Server](server/index.md) | Server lifecycle, address-space construction, callbacks, events, history, and access control. |
| [Information Model Authoring](information-model-authoring/index.md) | Compiling nodesets, declaring models, and implementing their types. |

If you already know OPC UA, skim OPC UA Fundamentals. Read o6\\Python SDK
Fundamentals and then Node API before Client or Server: both application chapters
use their notation and type vocabulary.

Client and Server are independent of each other. Read the chapter that matches
the application you are building.

## Advanced topics

The next two chapters are reference material, not part of the reading path. You
don't need either to use the SDK. Each page stands alone and lists its own
prerequisites.

| Topic | What it covers |
|---|---|
| [Benchmarks](benchmark.md) | Client and server throughput comparisons and benchmark methodology. |
| [Implementation details](implementation-details/index.md) | Memory management, callbacks, namespace matching, event loops, and wire-format mapping. |

## Release notes

| Topic | What it covers |
|---|---|
| [Release Notes](release-notes.md) | Features, improvements, fixes, and breaking changes by release. |
