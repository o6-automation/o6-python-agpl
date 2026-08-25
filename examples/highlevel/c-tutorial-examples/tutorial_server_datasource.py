#!/usr/bin/env python3
"""Python parity-style example for open62541 tutorial_server_datasource.

C tutorial topics:
- Updating variables manually
- Variable Value Callback
- Variable Data Sources

Note:
The current high-level Python API focuses on direct read/write for variables.
This script demonstrates manual updates and a callback-like read wrapper pattern.
"""

import time
from o6 import Server


class ProcessModel:
    def __init__(self) -> None:
        self._temperature = 20.0

    def tick(self) -> None:
        self._temperature += 0.05

    def read_temperature(self) -> float:
        # Callback-like read source.
        return self._temperature


def main() -> None:
    process = ProcessModel()
    with Server(port=4840) as server:
        temp_node = server.addVariable(
            "ProcessTemperature",
            server.objectsNode,
            process.read_temperature(),
            nodeId="ns=1;s=ProcessTemperature",
        )

        print("[Manual updates]")
        for _ in range(5):
            process.tick()
            server.write(temp_node.nodeId, process.read_temperature())
            print("Current value:", server.read(temp_node.nodeId))
            time.sleep(0.2)

        print("\n[Callback-like read wrapper]")
        print("Wrapped value:", process.read_temperature())

        print("\n[Data source parity]")
        print("The high-level API currently mirrors datasource behavior via explicit read/write.")


if __name__ == "__main__":
    main()
