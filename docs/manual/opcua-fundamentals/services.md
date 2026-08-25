# Services

In OPC UA, all communication is based on service calls, each consisting of a request and a response message. These messages are defined as data structures with a binary encoding and listed in Generated Data Type Definitions. Since all Services are pre-defined in the standard, they cannot be modified by the user. But you can use the Call service to invoke user-defined methods on the server.

Please refer to the Client and Server API where the services are exposed to end users. Please see part 4 of the OPC UA standard for the authoritative definition of the services and their behaviour.

## Discovery Service Set

This Service Set defines Services used to discover the Endpoints implemented by a Server and to read the security configuration for those Endpoints.

### FindServers Service

Returns the Servers known to a Server or Discovery Server. The Client may reduce the number of results returned by specifying filter criteria

### GetEndpoints Service

Returns the Endpoints supported by a Server and all of the configuration information required to establish a SecureChannel and a Session.

### FindServersOnNetwork Service

Returns the Servers known to a Discovery Server. Unlike FindServer, this Service is only implemented by Discovery Servers. It additionally returns servers which may have been detected through Multicast.

### RegisterServer

Registers a remote server in the local discovery service.

### RegisterServer2

This Service allows a Server to register its DiscoveryUrls and capabilities with a Discovery Server. It extends the registration information from RegisterServer with information necessary for FindServersOnNetwork.

## SecureChannel Service Set

This Service Set defines Services used to open a communication channel that ensures the confidentiality and Integrity of all Messages exchanged with the Server.

### OpenSecureChannel Service

Open or renew a SecureChannel that can be used to ensure Confidentiality and Integrity for Message exchange during a Session.

### CloseSecureChannel Service

Used to terminate a SecureChannel.

### Session Service Set

This Service Set defines Services for an application layer connection establishment in the context of a Session.

### CreateSession Service

Used by an OPC UA Client to create a Session and the Server returns two values which uniquely identify the Session. The first value is the sessionId which is used to identify the Session in the audit logs and in the Server’s address space. The second is the authenticationToken which is used to associate an incoming request with a Session.

### ActivateSession

Used by the Client to submit its SoftwareCertificates to the Server for validation and to specify the identity of the user associated with the Session. This Service request shall be issued by the Client before it issues any other Service request after CreateSession. Failure to do so shall cause the Server to close the Session.

### CloseSession

Used to terminate a Session.

### Cancel Service

Used to cancel outstanding Service requests. Successfully cancelled service requests shall respond with Bad_RequestCancelledByClient.

## NodeManagement Service Set

This Service Set defines Services to add and delete AddressSpace Nodes and References between them. All added Nodes continue to exist in the AddressSpace even if the Client that created them disconnects from the Server.

### AddNodes Service

Used to add one or more Nodes into the AddressSpace hierarchy. If the type or one of the supertypes has any HasInterface references (see OPC 10001-7 - Amendment 7, 4.9.2), the child nodes of the interfaces are added to the new object.

### AddReferences Service

Used to add one or more References to one or more Nodes.

### DeleteNodes Service

Used to delete one or more Nodes from the AddressSpace.

### DeleteReferences

Used to delete one or more References of a Node.

## View Service Set

Clients use the browse Services of the View Service Set to navigate through the AddressSpace or through a View which is a subset of the AddressSpace.

### Browse Service

Used to discover the References of a specified Node. The browse can be further limited by the use of a View. This Browse Service also supports a primitive filtering capability.

### BrowseNext Service

Used to request the next set of Browse or BrowseNext response information that is too large to be sent in a single response. “Too large” in this context means that the Server is not able to return a larger response or that the number of results to return exceeds the maximum number of results to return that was specified by the Client in the original Browse request.

### TranslateBrowsePathsToNodeIds Service

Used to translate textual node paths to their respective ids.

### RegisterNodes Service

Used by Clients to register the Nodes that they know they will access repeatedly (e.g. Write, Call). It allows Servers to set up anything needed so that the access operations will be more efficient.

### UnregisterNodes Service

This Service is used to unregister NodeIds that have been obtained via the RegisterNodes service.

## Query Service Set

This Service Set is used to issue a Query to a Server. OPC UA Query is generic in that it provides an underlying storage mechanism independent Query capability that can be used to access a wide variety of OPC UA data stores and information management systems. OPC UA Query permits a Client to access data maintained by a Server without any knowledge of the logical schema used for internal storage of the data. Knowledge of the AddressSpace is sufficient.

### QueryFirst Service (not implemented)

This Service is used to issue a Query request to the Server.

### QueryNext Service (not implemented)

This Service is used to request the next set of QueryFirst or QueryNext response information that is too large to be sent in a single response.

## Attribute Service Set

This Service Set provides Services to access Attributes that are part of Nodes.

### Read Service

Used to read attributes of nodes. For constructed attribute values whose elements are indexed, such as an array, this Service allows Clients to read the entire set of indexed values as a composite, to read individual elements or to read ranges of elements of the composite.

### Write Service

Used to write attributes of nodes. For constructed attribute values whose elements are indexed, such as an array, this Service allows Clients to write the entire set of indexed values as a composite, to write individual elements or to write ranges of elements of the composite.

### HistoryRead Service

Used to read historical values or Events of one or more Nodes. Servers may make historical values available to Clients using this Service, although the historical values themselves are not visible in the AddressSpace.

### HistoryUpdate Service

Used to update historical values or Events of one or more Nodes. Several request parameters indicate how the Server is to update the historical value or Event. Valid actions are Insert, Replace or Delete.

## Method Service Set

The Method Service Set defines the means to invoke methods. A method shall be a component of an Object. See the section on MethodNodes for more information.

### Call Service

Used to call (invoke) a methods. Each method call is invoked within the context of an existing Session. If the Session is terminated, the results of the method’s execution cannot be returned to the Client and are discarded.

## MonitoredItem Service Set

Clients define MonitoredItems to subscribe to data and Events. Each MonitoredItem identifies the item to be monitored and the Subscription to use to send Notifications. The item to be monitored may be any Node Attribute.

### CreateMonitoredItems Service

Used to create and add one or more MonitoredItems to a Subscription. A MonitoredItem is deleted automatically by the Server when the Subscription is deleted. Deleting a MonitoredItem causes its entire set of triggered item links to be deleted, but has no effect on the MonitoredItems referenced by the triggered items.

### DeleteMonitoredItems Service

Used to remove one or more MonitoredItems of a Subscription. When a MonitoredItem is deleted, its triggered item links are also deleted.

### ModifyMonitoredItems Service

Used to modify MonitoredItems of a Subscription. Changes to the MonitoredItem settings shall be applied immediately by the Server. They take effect as soon as practical but not later than twice the new revisedSamplingInterval.

Illegal request values for parameters that can be revised do not generate errors. Instead the server will choose default values and indicate them in the corresponding revised parameter.

### SetMonitoringMode Service

Used to set the monitoring mode for one or more MonitoredItems of a Subscription.

### SetTriggering Service

Used to create and delete triggering links for a triggering item.

## Subscription Service Set

Subscriptions are used to report Notifications to the Client.

### CreateSubscription Service

Used to create a Subscription. Subscriptions monitor a set of MonitoredItems for Notifications and return them to the Client in response to Publish requests.

### ModifySubscription Service

Used to modify a Subscription.

### SetPublishingMode Service

Used to enable sending of Notifications on one or more Subscriptions.

### Publish Service

Used for two purposes. First, it is used to acknowledge the receipt of NotificationMessages for one or more Subscriptions. Second, it is used to request the Server to return a NotificationMessage or a keep-alive Message.

### Republish Service

Requests the Subscription to republish a NotificationMessage from its retransmission queue.

### DeleteSubscriptions Service

Invoked to delete one or more Subscriptions that belong to the Client’s Session.

### TransferSubscription Service

Used to transfer a Subscription and its MonitoredItems from one Session to another. For example, a Client may need to reopen a Session and then transfer its Subscriptions to that Session. It may also be used by one Client to take over a Subscription from another Client by transferring the Subscription to its Session.

