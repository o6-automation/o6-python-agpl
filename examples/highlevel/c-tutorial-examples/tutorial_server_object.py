#!/usr/bin/env python3
"""Python parity for open62541 tutorial_server_object."""

from o6 import Server


def main() -> None:
    with Server(port=4840) as server:
        print("[Manual object hierarchy]")
        plant = server.addObject("Plant", server.objectsNode, nodeId="ns=1;i=4000")
        pump = server.addObject("Pump", plant.nodeId, nodeId="ns=1;i=4001")
        server.addVariable("Speed", pump.nodeId, 1450.0, nodeId="ns=1;i=4002")
        server.addVariable("Status", pump.nodeId, True, nodeId="ns=1;i=4003")

        print("\n[Object type hierarchy]")
        device_type = server.addObjectType("DeviceType", nodeId="ns=1;i=4100")
        pump_type = server.addObjectType(
            "PumpType",
            parent=device_type.nodeId,
            nodeId="ns=1;i=4101",
        )
        server.addVariable("Flow", pump_type.nodeId, 0.0, nodeId="ns=1;i=4102")

        print("\n[Instantiation]")
        boiler_pump = server.addObject(
            "BoilerPump",
            server.objectsNode,
            nodeId="ns=1;i=4200",
            typeDefinition=pump_type.nodeId,
        )
        print("Instantiated object:", boiler_pump.nodeId)


if __name__ == "__main__":
    main()
