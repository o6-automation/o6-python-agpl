# Tutorial Parity (Collapsible + Top Language Switch)

Choose language at the top, then expand the examples you want.

=== "Python"

    <details>
    <summary>Working with Data Types</summary>

    Parity page: [Working with Data Types](../C-Tutorials-in-Python/tutorial_datatypes.md)

    ```python
    from o6 import types

    i = types.Int32(42)
    nid = types.NodeId("ns=1;s=Temperature")
    dv = types.DataValue(value=types.Double(12.5))
    ```
    </details>

    <details>
    <summary>Building a Simple Server</summary>

    Parity page: [Building a Simple Server](../C-Tutorials-in-Python/tutorial_server_firststeps.md)

    ```python
    from o6 import Server

    server = Server(port=4840)
    server.start()
    server.stop()
    ```
    </details>

    <details>
    <summary>Adding Variables to a Server</summary>

    Parity page: [Adding Variables to a Server](../C-Tutorials-in-Python/tutorial_server_variable.md)

    ```python
    temperature = server.addVariable(
        "Temperature", server.objectsNode, 22.5, nodeId="ns=1;s=Temperature"
    )
    ```
    </details>

    <details>
    <summary>Connecting a Variable with a Physical Process</summary>

    Parity page: [Connecting a Variable with a Physical Process](../C-Tutorials-in-Python/tutorial_server_datasource.md)

    ```python
    process.tick()
    temp_node.value = process.read_temperature()
    ```
    </details>

    <details>
    <summary>Working with Objects and Object Types</summary>

    Parity page: [Working with Objects and Object Types](../C-Tutorials-in-Python/tutorial_server_object.md)

    ```python
    plant = server.addObject("Plant", server.objectsNode)
    machine_type = server.addObjectType("MachineType")
    machine = server.addObject("MachineA", plant, typeDefinition=machine_type.nodeId)
    ```
    </details>

    <details>
    <summary>Adding Methods to Objects</summary>

    Parity page: [Adding Methods to Objects](../C-Tutorials-in-Python/tutorial_server_method.md)

    ```python
    server.addMethod("HelloWorld", obj, hello, ...)
    server.addMethod("IncreaseArrayValues", obj, increase, ...)
    ```
    </details>

    <details>
    <summary>Building a Simple Client</summary>

    Parity page: [Building a Simple Client](../C-Tutorials-in-Python/tutorial_client_firststeps.md)

    ```python
    with Client("opc.tcp://localhost:4840") as client:
        value = client.read("ns=1;s=IntegerVariable")
        client.write("ns=1;s=IntegerVariable", types.UInt32(123))
    ```
    </details>

=== "C"

    <details>
    <summary>Working with Data Types</summary>

    C tutorial equivalent: [Working with Data Types](https://open62541.org/doc/v1.5.3/tutorial_datatypes.html)

    ```c
    UA_Int32 i = 42;
    UA_NodeId nid = UA_NODEID_STRING(1, "Temperature");
    UA_Variant v;
    UA_Variant_setScalar(&v, &i, &UA_TYPES[UA_TYPES_INT32]);
    ```
    </details>

    <details>
    <summary>Building a Simple Server</summary>

    C tutorial equivalent: [Building a Simple Server](https://open62541.org/doc/v1.5.3/tutorial_server_firststeps.html)

    ```c
    UA_Server *server = UA_Server_new();
    UA_ServerConfig_setDefault(UA_Server_getConfig(server));
    UA_Server_run(server, &running);
    ```
    </details>

    <details>
    <summary>Adding Variables to a Server</summary>

    C tutorial equivalent: [Adding Variables to a Server](https://open62541.org/doc/v1.5.3/tutorial_server_variable.html)

    ```c
    UA_Server_addVariableNode(...);
    ```
    </details>

    <details>
    <summary>Connecting a Variable with a Physical Process</summary>

    C tutorial equivalent: [Connecting a Variable with a Physical Process](https://open62541.org/doc/v1.5.3/tutorial_server_datasource.html)

    ```c
    UA_Server_writeValue(server, nodeId, value);
    ```
    </details>

    <details>
    <summary>Working with Objects and Object Types</summary>

    C tutorial equivalent: [Working with Objects and Object Types](https://open62541.org/doc/v1.5.3/tutorial_server_object.html)

    ```c
    UA_Server_addObjectNode(...);
    UA_Server_addObjectTypeNode(...);
    ```
    </details>

    <details>
    <summary>Adding Methods to Objects</summary>

    C tutorial equivalent: [Adding Methods to Objects](https://open62541.org/doc/v1.5.3/tutorial_server_method.html)

    ```c
    UA_Server_addMethodNode(...);
    ```
    </details>

    <details>
    <summary>Building a Simple Client</summary>

    C tutorial equivalent: [Building a Simple Client](https://open62541.org/doc/v1.5.3/tutorial_client_firststeps.html)

    ```c
    UA_Client_connect(client, "opc.tcp://localhost:4840");
    UA_Client_readValueAttribute(...);
    UA_Client_writeValueAttribute(...);
    ```
    </details>

## Notes

- Events, alarms/conditions, and PubSub currently have dedicated parity pages in:
    - [Generating Events](../C-Tutorials-in-Python/tutorial_server_events.md)
    - [Using Alarms and Conditions Server](../C-Tutorials-in-Python/tutorial_server_alarms_conditions.md)
    - [Publishing Fields](../C-Tutorials-in-Python/tutorial_pubsub_publish.md)
    - [Subscribing Fields](../C-Tutorials-in-Python/tutorial_pubsub_subscribe.md)
