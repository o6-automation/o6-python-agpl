# Core Concepts of OPC UA

In one sentence, OPC UA defines a framework for object-oriented information models that live in an OPC UA server together with a protocol that clients use to interact with those models over the network.

This page introduces the core concepts of OPC UA first. The final section explains how those concepts surface in pyo6.

For the full specification see the OPC UA standard at https://reference.opcfoundation.org/.

## Protocol

The most common OPC UA setup uses the binary protocol over TCP. Communication is based on a request-response model:

- Clients send requests to servers.
- Servers return responses for those requests.
- Responses do not have to arrive immediately or in strict request order.

That asynchronous behavior matters because some operations take time. A read may wait for a device, a method call may perform work on the server, and subscriptions are realized through publish interactions whose responses can be delayed.

### Connection Layers

An OPC UA client-server connection is built in three nested layers:

- TCP connection: transports the bytes and establishes low-level transport settings.
- SecureChannel: binds messages to a secure communication context and controls signing and encryption.
- Session: provides application-level identity and state.

In practical terms, a client connects to a server, opens a SecureChannel, creates a session, and activates that session before issuing most application requests.

### Endpoints and Security

Servers advertise one or more endpoints. An endpoint describes how a client can connect, including:

- the endpoint URL
- the security policy
- the message security mode
- the supported user authentication mechanisms

Security is not a single switch. It is the combination of endpoint selection, SecureChannel settings, and session authentication. Depending on the server, authentication may be anonymous, username/password based, or certificate based.

## Services

All OPC UA communication is expressed as service calls with standardized request and response types. These services are grouped into service sets.

### Discovery Service Set

This service set is used to find servers and inspect how they can be reached.

- FindServers
- GetEndpoints
- FindServersOnNetwork

These services are commonly used before a secure session is established.

### SecureChannel and Session Service Set

These services establish and maintain communication state.

- OpenSecureChannel and CloseSecureChannel manage the communication channel.
- CreateSession and ActivateSession establish the session.
- CloseSession terminates the session.
- Cancel can be used to cancel outstanding requests.

The transport connection, the SecureChannel, and the session are related but distinct concepts.

### Attribute Service Set

This service set accesses attributes of nodes.

- Read retrieves attributes such as Value, DisplayName, or DataType.
- Write modifies writable attributes.
- HistoryRead and HistoryUpdate operate on historical data where a server supports it.

For many applications, this is the most visible part of OPC UA because variable access is expressed through node attributes.

### View Service Set

This service set is used to navigate the address space.

- Browse
- BrowseNext
- TranslateBrowsePathsToNodeIds
- RegisterNodes and UnregisterNodes

These services are what let clients discover structure instead of assuming fixed node locations.

### Method Service Set

Methods are callable functions attached to objects in the information model. The Call service invokes them in the context of an active session.

### NodeManagement Service Set

This service set allows clients to modify the address space dynamically:

- AddNodes
- DeleteNodes
- AddReferences
- DeleteReferences

Not every server exposes these capabilities, but they are central when address spaces are created or extended programmatically.

### Query Service Set

The query service set provides a storage-independent way to query information exposed by a server. It is part of the OPC UA model even though many stacks and applications make little or no use of it.

### MonitoredItem Service Set

Monitored items define what data or events are observed.

- CreateMonitoredItems
- ModifyMonitoredItems
- DeleteMonitoredItems
- SetMonitoringMode
- SetTriggering

Monitored items belong to a subscription and describe what should be sampled or reported.

### Subscription Service Set

Subscriptions provide server-driven notifications instead of repeated polling.

- CreateSubscription
- ModifySubscription
- SetPublishingMode
- Publish
- Republish
- DeleteSubscriptions
- TransferSubscriptions

This service set is the core mechanism behind data change notifications and event delivery.

## Information Modelling

An OPC UA server exposes an address space. The address space is a graph of nodes connected by typed references.

- Nodes carry attributes and represent entities in the model.
- References define relationships between nodes.
- NodeIds uniquely identify nodes within the server.

Information modelling is central to OPC UA. Clients browse and read the model. Servers create, organize, and constrain it.

### Node Classes

OPC UA defines a fixed set of node classes. The most important ones are:

- Variable: stores a value together with metadata.
- VariableType: constrains variables and describes their structure.
- Object: represents a system, device, or logical component.
- ObjectType: defines the structure of objects.
- Method: defines callable behavior.
- DataType: defines the type of values.
- ReferenceType: defines the meaning of relationships.
- View: defines a subset of the address space for browsing.

The node class determines which attributes a node can carry and how it behaves in the model.

### Attributes

Each node is identified by a NodeId and carries attributes defined by its node class. Common attributes include BrowseName, DisplayName, Description, and NodeClass. Additional attributes depend on the specific node class.

In day-to-day OPC UA usage, many operations are simply reads or writes of node attributes.

### References

References are directed, typed links between nodes. They are what turn the address space into a navigable graph.

Some references express hierarchy, such as containment or organization. Others express type relationships, properties, or non-hierarchical semantics. The standard defines a common hierarchy of reference types, and information models may extend it.

### VariableNode

Variables store values together with metadata that constrains how those values are interpreted.

A variable typically combines:

- a Value
- a DataType
- a ValueRank
- optional ArrayDimensions
- access and sampling metadata

These attributes constrain what values are valid and how clients should interpret them.

#### Data Type

The data type constrains the type of the variable value. The data type is itself represented by a DataType node in the information model.

#### ValueRank

ValueRank describes whether the value is scalar or array-like and, if it is an array, how many dimensions it can have.

#### ArrayDimensions

If the value rank permits arrays, ArrayDimensions can further constrain the expected shape.

### VariableTypeNode

Variable types provide definitions and constraints for variable instances. They are used to describe structure and expected value semantics beyond the raw scalar type.

### ObjectNode

Objects represent systems, components, logical entities, or software-visible resources. They can contain variables, methods, and other objects.

### ObjectTypeNode

Object types provide reusable structure for object instances.

### ReferenceTypeNode

Reference types define the meaning of relationships between nodes. Some are hierarchical, some are symmetric, and many information models depend heavily on them for their domain semantics.

### DataTypeNode

Data types define the shape of values. OPC UA supports both built-in scalar types and structured data types. Data types may also be abstract and used only to constrain possible concrete values.

### MethodNode

Methods are callable nodes associated with objects. Their input and output signatures are described in the information model, while invocation happens through the Call service.

### ViewNode

Views define subsets of the address space for browsing and organization.

