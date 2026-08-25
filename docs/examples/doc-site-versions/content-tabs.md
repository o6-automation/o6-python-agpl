# open62541 Tutorial Parity in Python (Tabbed View)

This page mirrors the open62541 C tutorial structure and shows the Python equivalent pattern used in this repository.

## Working with Data Types

=== "C (logical structure)"
    ```c
    UA_Int32 i = 42;
    UA_NodeId nid = UA_NODEID_STRING(1, "Temperature");
    UA_Variant v;
    UA_Variant_setScalar(&v, &i, &UA_TYPES[UA_TYPES_INT32]);
    ```

=== "Python (o6 parity)"
    ```python
    from o6 import types

    i = types.Int32(42)
    nid = types.NodeId("ns=1;s=Temperature")
    dv = types.DataValue(value=types.Double(12.5))
    ```

Python example page: [Working with Data Types](../C-Tutorials-in-Python/tutorial_datatypes.md)

## Building a Simple Server

=== "C (logical structure)"
    ```c
    UA_Server *server = UA_Server_new();
    UA_ServerConfig_setDefault(UA_Server_getConfig(server));
    UA_Server_run(server, &running);
    ```

=== "Python (o6 parity)"
    ```python
    from o6 import Server

    server = Server(port=4840)
    server.start()
    server.stop()
    ```

Python example page: [Building a Simple Server](../C-Tutorials-in-Python/tutorial_server_firststeps.md)

## Adding Variables to a Server

=== "C (logical structure)"
    ```c
    UA_Server_addVariableNode(...);
    ```

=== "Python (o6 parity)"
    ```python
    temperature = server.addVariable(
        "Temperature", server.objectsNode, 22.5, nodeId="ns=1;s=Temperature"
    )
    ```

Python example page: [Adding Variables to a Server](../C-Tutorials-in-Python/tutorial_server_variable.md)

## Connecting a Variable with a Physical Process

=== "C (logical structure)"
    ```c
    // manual updates, value callbacks, and external data source hooks
    UA_Server_writeValue(server, nodeId, value);
    ```

=== "Python (o6 parity)"
    ```python
    process.tick()
    temp_node.value = process.read_temperature()
    ```

Python example page: [Connecting a Variable with a Physical Process](../C-Tutorials-in-Python/tutorial_server_datasource.md)

## Working with Variable Types

=== "C (logical structure)"
    ```c
    UA_Server_addVariableTypeNode(...);
    ```

=== "Python (o6 parity)"
    ```python
    temp_type = server.addVariableType("TemperatureType", dataType="i=11")
    ```

Python example page: [Working with Variable Types](../C-Tutorials-in-Python/tutorial_server_variabletype.md)

## Working with Objects and Object Types

=== "C (logical structure)"
    ```c
    UA_Server_addObjectNode(...);
    UA_Server_addObjectTypeNode(...);
    ```

=== "Python (o6 parity)"
    ```python
    plant = server.addObject("Plant", server.objectsNode)
    machine_type = server.addObjectType("MachineType")
    machine = server.addObject("MachineA", plant, typeDefinition=machine_type.nodeId)
    ```

Python example page: [Working with Objects and Object Types](../C-Tutorials-in-Python/tutorial_server_object.md)

## Adding Methods to Objects

=== "C (logical structure)"
    ```c
    UA_Server_addMethodNode(...);
    ```

=== "Python (o6 parity)"
    ```python
    server.addMethod("HelloWorld", obj, hello, ...)
    server.addMethod("IncreaseArrayValues", obj, increase, ...)
    ```

Python example page: [Adding Methods to Objects](../C-Tutorials-in-Python/tutorial_server_method.md)

## Observing Attributes with Local MonitoredItems

=== "C (logical structure)"
    ```c
    // local monitored item callback on server attributes
    ```

=== "Python (closest exposed parity)"
    ```python
    sub = client.createSubscription(publishingInterval=500.0)
    mon = client.monitor("ns=1;s=IntegerVariable", on_change, subscription=sub)
    ```

Python example page: [Observing Attributes with Local MonitoredItems](../C-Tutorials-in-Python/tutorial_server_monitoreditems.md)

## Generating Events and Alarms/Conditions

=== "C (logical structure)"
    ```c
    // create event type, trigger event, alarms/conditions state changes
    ```

=== "Python (current state)"
    ```python
    # Server-side high-level event/alarm creation helpers are not yet exposed.
    # Closest parity: client-side monitorEvent(...)
    listener = client.monitorEvent("i=2253", on_event)
    ```

Python example pages:
- [Generating Events](../C-Tutorials-in-Python/tutorial_server_events.md)
- [Using Alarms and Conditions Server](../C-Tutorials-in-Python/tutorial_server_alarms_conditions.md)

## Building a Simple Client

=== "C (logical structure)"
    ```c
    UA_Client_connect(client, "opc.tcp://localhost:4840");
    UA_Client_readValueAttribute(...);
    UA_Client_writeValueAttribute(...);
    ```

=== "Python (o6 parity)"
    ```python
    with Client("opc.tcp://localhost:4840") as client:
        value = client.read("ns=1;s=IntegerVariable")
        client.write("ns=1;s=IntegerVariable", types.UInt32(123))
    ```

Python example page: [Building a Simple Client](../C-Tutorials-in-Python/tutorial_client_firststeps.md)

## Working with Publish/Subscribe

=== "C (logical structure)"
    ```c
    // configure writer groups / reader groups and published fields
    ```

=== "Python (current state)"
    ```python
    # Dedicated high-level PubSub helpers are not exposed yet.
    ```

Python example pages:
- [Publishing Fields](../C-Tutorials-in-Python/tutorial_pubsub_publish.md)
- [Subscribing Fields](../C-Tutorials-in-Python/tutorial_pubsub_subscribe.md)
