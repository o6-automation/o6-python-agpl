#!/usr/bin/env python3
"""Python parity-style example for tutorial_server_monitoreditems.

This uses the client-side monitor API, which is the closest available high-level
Python equivalent for attribute observation workflows.
"""

import time
from o6 import Client


def on_change(value):
    print("Monitored value changed:", value)


def main() -> None:
    print("=== tutorial_server_monitoreditems (closest parity) ===")
    with Client("opc.tcp://localhost:4840") as client:
        sub = client.createSubscription(publishingInterval=500.0)
        mon = client.monitor("ns=1;s=IntegerVariable", on_change, subscription=sub)

        try:
            time.sleep(10)
        finally:
            mon.delete()
            sub.delete()


if __name__ == "__main__":
    main()
