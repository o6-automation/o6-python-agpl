# open62541 Tutorial Parity in Python (Collapsible Details View)

This is an alternative to the tabbed presentation in [content-tabs.md](content-tabs.md).
Open a section, then click the C or Python tab inside it.

<details>
<summary>Working with Data Types</summary>

Python parity page: [Working with Data Types](../C-Tutorials-in-Python/tutorial_datatypes.md)

=== "C"
    ```c
    UA_Int32 i = 42;
    UA_NodeId nid = UA_NODEID_STRING(1, "Temperature");
    UA_Variant v;
    UA_Variant_setScalar(&v, &i, &UA_TYPES[UA_TYPES_INT32]);
    ```

=== "Python"
    ```python
    from o6 import types

    i = types.Int32(42)
    nid = types.NodeId("ns=1;s=Temperature")
    dv = types.DataValue(value=types.Double(12.5))
    ```
</details>

<details>
<summary>Building a Simple Server</summary>

Python parity page: [Building a Simple Server](../C-Tutorials-in-Python/tutorial_server_firststeps.md)

=== "C"
    ```c
    UA_Server *server = UA_Server_new();
    UA_ServerConfig_setDefault(UA_Server_getConfig(server));
    UA_Server_run(server, &running);
    ```

=== "Python"
    ```python
    from o6 import Server

    server = Server(port=4840)
    server.start()
    server.stop()
    ```
</details>

<details>
<summary>Adding Variables to a Server</summary>

Python parity page: [Adding Variables to a Server](../C-Tutorials-in-Python/tutorial_server_variable.md)

=== "C"
    ```c
    UA_Server_addVariableNode(...);
    ```

=== "Python"
    ```python
    temperature = server.addVariable(
        "Temperature", server.objectsNode, 22.5, nodeId="ns=1;s=Temperature"
    )
    ```
</details>

<details>
<summary>Connecting a Variable with a Physical Process</summary>

Python parity page: [Connecting a Variable with a Physical Process](../C-Tutorials-in-Python/tutorial_server_datasource.md)

=== "C"
    ```c
    UA_Server_writeValue(server, nodeId, value);
    ```

=== "Python"
    ```python
    process.tick()
    temp_node.value = process.read_temperature()
    ```
</details>

<details>
<summary>Working with Variable Types</summary>

Python parity page: [Working with Variable Types](../C-Tutorials-in-Python/tutorial_server_variabletype.md)

=== "C"
    ```c
    UA_Server_addVariableTypeNode(...);
    ```

=== "Python"
    ```python
    temp_type = server.addVariableType("TemperatureType", dataType="i=11")
    ```
</details>

<details>
<summary>Working with Objects and Object Types</summary>

Python parity page: [Working with Objects and Object Types](../C-Tutorials-in-Python/tutorial_server_object.md)

=== "C"
    ```c
    UA_Server_addObjectNode(...);
    UA_Server_addObjectTypeNode(...);
    ```

=== "Python"
    ```python
    plant = server.addObject("Plant", server.objectsNode)
    machine_type = server.addObjectType("MachineType")
    machine = server.addObject("MachineA", plant, typeDefinition=machine_type.nodeId)
    ```
</details>

<details>
<summary>Adding Methods to Objects</summary>

Python parity page: [Adding Methods to Objects](../C-Tutorials-in-Python/tutorial_server_method.md)

=== "C"
    ```c
    UA_Server_addMethodNode(...);
    ```

=== "Python"
    ```python
    server.addMethod("HelloWorld", obj, hello, ...)
    server.addMethod("IncreaseArrayValues", obj, increase, ...)
    ```
</details>

<details>
<summary>Observing Attributes with Local MonitoredItems</summary>

Python parity page: [Observing Attributes with Local MonitoredItems](../C-Tutorials-in-Python/tutorial_server_monitoreditems.md)

=== "C"
    ```c
    /* Local monitored item callback on server-side attributes */
    ```

=== "Python"
    ```python
    sub = client.createSubscription(publishingInterval=500.0)
    mon = client.monitor("ns=1;s=IntegerVariable", on_change, subscription=sub)
    ```
</details>

<details>
<summary>Generating Events and Alarms/Conditions</summary>

Python parity pages:
- [Generating Events](../C-Tutorials-in-Python/tutorial_server_events.md)
- [Using Alarms and Conditions Server](../C-Tutorials-in-Python/tutorial_server_alarms_conditions.md)

Current high-level parity is client-side event monitoring.

=== "C"
    ```c
    /* Create event types, trigger events, and alarms state transitions */
    ```

=== "Python"
    ```python
    listener = client.monitorEvent("i=2253", on_event)
    ```
</details>

<details>
<summary>Building a Simple Client</summary>

Python parity page: [Building a Simple Client](../C-Tutorials-in-Python/tutorial_client_firststeps.md)

=== "C"
    ```c
    UA_Client_connect(client, "opc.tcp://localhost:4840");
    UA_Client_readValueAttribute(...);
    UA_Client_writeValueAttribute(...);
    ```

=== "Python"
    ```python
    with Client("opc.tcp://localhost:4840") as client:
        value = client.read("ns=1;s=IntegerVariable")
        client.write("ns=1;s=IntegerVariable", types.UInt32(123))
    ```
</details>

<details>
<summary>Working with Publish/Subscribe</summary>

Python parity pages:
- [Publishing Fields](../C-Tutorials-in-Python/tutorial_pubsub_publish.md)
- [Subscribing Fields](../C-Tutorials-in-Python/tutorial_pubsub_subscribe.md)

Dedicated high-level PubSub helpers are not exposed yet.

=== "C"
    ```c
    /* Configure PublishedDataSet, WriterGroup, ReaderGroup */
    ```

=== "Python"
    ```python
    # High-level PubSub helpers are currently not exposed.
    ```
</details>
