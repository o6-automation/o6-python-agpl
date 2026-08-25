#!/usr/bin/env python3
"""Python parity for open62541 tutorial_server_variable."""

from o6 import Server


def main() -> None:
    with Server(port=4840) as server:
        print("[Adding a variable]")
        scalar = server.addVariable(
            "The Answer",
            server.objectsNode,
            42,
            nodeId="ns=1;s=TheAnswer",
        )
        print("Initial value:", server.read(scalar.nodeId))

        print("\n[Writing to a variable]")
        server.write(scalar.nodeId, 43)
        print("Updated value:", server.read(scalar.nodeId))

        print("\n[Matrix variable]")
        matrix = server.addVariable(
            "Double Matrix",
            server.objectsNode,
            [[1.1, 1.2], [2.1, 2.2]],
            nodeId="ns=1;s=DoubleMatrix",
        )
        print("Matrix:", server.read(matrix.nodeId))

        print("\n[Wrong type write]")
        try:
            server.write(scalar.nodeId, "forty-two")
        except Exception as exc:
            print("Rejected incompatible write:", exc)


if __name__ == "__main__":
    main()
