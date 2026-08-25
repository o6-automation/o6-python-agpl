#!/usr/bin/env python3
"""Python parity for tutorial_client_firststeps.

C tutorial topics:
- Building a Simple Client
- Further tasks
"""

from o6 import Client, types


def main() -> None:
    print("=== tutorial_client_firststeps (Python parity) ===")
    with Client("opc.tcp://localhost:4840") as client:
        print("\n[Read current time]")
        server_time = client.read("i=2258")
        print("Server time:", server_time)

        print("\n[Further tasks]")
        value = client.read("ns=1;s=IntegerVariable")
        print("Before write:", value)

        client.write("ns=1;s=IntegerVariable", types.UInt32(123))
        value = client.read("ns=1;s=IntegerVariable")
        print("After write:", value)

        refs = client.browse("i=85")
        print("Objects children count:", len(refs))


if __name__ == "__main__":
    main()
