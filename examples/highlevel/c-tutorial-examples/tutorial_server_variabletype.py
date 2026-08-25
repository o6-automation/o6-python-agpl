#!/usr/bin/env python3
"""Python parity for open62541 tutorial_server_variabletype."""

from o6 import Server


def main() -> None:
    with Server(port=4840) as server:
        print("[2DPoint variable type]")
        point_type = server.addVariableType(
            "2DPoint Type",
            dataType="i=11",
            valueRank=1,
            nodeId="ns=1;i=3001",
        )
        print("Created variable type:", point_type.nodeId)

        print("\n[2DPoint variable instance]")
        point = server.addVariable(
            "2DPoint Variable",
            server.objectsNode,
            [0.0, 0.0],
            dataType="i=11",
            nodeId="ns=1;i=3002",
        )
        print("Created variable:", point.nodeId)

        print("\n[Type mismatch]")
        try:
            server.write(point.nodeId, "2dpoint")
        except Exception as exc:
            print("Type mismatch rejected:", exc)

        print("\n[Valid write]")
        server.write(point.nodeId, [1.0, 1.0])
        print("Updated value:", server.read(point.nodeId))


if __name__ == "__main__":
    main()
