# o6\\Python SDK Fundamentals

This chapter explains the values and identifiers shared by client and server
applications, error handling, and how to use existing information models.

A Python value, such as `o6.Double(21.5)`, carries data. A `NodeId` identifies a
node. A model declaration describes a type or node without contacting a server.
A live node handle is bound to a client or server and performs operations through
the [Node API](../node-api/index.md). Loading a model supplies declarations and
datatypes; publishing it creates its declared nodes on a server.

## Contents

### Built-in Types

| Topic | What it covers |
|---|---|
| [Primitive Types](builtin/primitive-types.md) | Built-in scalar types and their Python representations. |
| [StatusCode and Errors](builtin/statuscode.md) | Status values, severity, returned errors, and exceptions. |
| [Container Types](builtin/container-types.md) | Variants, DataValues, arrays, and structured values. |
| [Address & Identity Types](builtin/address-types.md) | NodeIds, expanded NodeIds, and qualified names. |

### Namespaces in o6

| Topic | What it covers |
|---|---|
| [Registry and Namespace Mapping](namespace/namespace-mapping-in-o6.md) | Global and endpoint-local indices, shortnames, scopes, and versions. |
| [Loading & Using Nodesets](namespace/loading-and-using-nodesets.md) | Importing models, a minimal XML compilation workflow, and publishing namespaces. |

For how the specification describes types, namespaces and nodeset files, see [DataType](../opcua-fundamentals/datatype.md), [Namespace](../opcua-fundamentals/namespace.md) and [Nodeset Files & Companion Specs](../opcua-fundamentals/nodesets-and-companion-specs.md) in [OPC UA Fundamentals](../opcua-fundamentals/index.md).

The later [Information Model Authoring](../information-model-authoring/index.md)
chapter covers the full compiler workflow, Python declarations, and implementing
model behavior. You can use a packaged model without authoring one.
