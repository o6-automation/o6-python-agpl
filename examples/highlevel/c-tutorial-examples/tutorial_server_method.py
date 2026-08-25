#!/usr/bin/env python3
"""Python parity for open62541 tutorial_server_method."""

import o6
from o6 import Server
from o6.ns import ns0


def hello_world(node, name):
    return (o6.StatusCode.GOOD, f"Hello {name}")


def increase_array_values(node, values, delta):
    return (o6.StatusCode.GOOD, [value + delta for value in values])


def main() -> None:
    with Server(port=4840) as server:
        obj = server.addObject("MethodDemo", server.objectsNode, nodeId="ns=1;i=5000")

        hello = server.addMethod(
            "HelloWorld",
            obj.nodeId,
            hello_world,
            inputArgs=[
                ns0.datatypes.Argument(
                    name="Name", dataType=o6.String, valueRank=o6.ValueRank.SCALAR
                )
            ],
            outputArgs=[
                ns0.datatypes.Argument(
                    name="Message", dataType=o6.String, valueRank=o6.ValueRank.SCALAR
                )
            ],
            nodeId="ns=1;i=5001",
        )

        increase = server.addMethod(
            "IncreaseArrayValues",
            obj.nodeId,
            increase_array_values,
            inputArgs=[
                ns0.datatypes.Argument(
                    name="Values", dataType=o6.Double, valueRank=o6.ValueRank.ARRAY_1D
                ),
                ns0.datatypes.Argument(
                    name="Delta", dataType=o6.Double, valueRank=o6.ValueRank.SCALAR
                ),
            ],
            outputArgs=[
                ns0.datatypes.Argument(
                    name="Increased", dataType=o6.Double, valueRank=o6.ValueRank.ARRAY_1D
                )
            ],
            nodeId="ns=1;i=5002",
        )

        print("Added methods:", hello.nodeId, increase.nodeId)


if __name__ == "__main__":
    main()
