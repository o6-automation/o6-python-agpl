#!/usr/bin/env python3
"""Python parity-style example for tutorial_server_events.

Server-side event creation/emission helpers are not currently exposed as a
high-level Python API in this repository. This example demonstrates the client
side event monitoring workflow as closest parity.
"""

import time
from o6 import Client


def on_event(event):
    print("Event:", event)


def main() -> None:
    print("=== tutorial_server_events (closest parity) ===")
    with Client("opc.tcp://localhost:4840") as client:
        listener = client.monitorEvent("i=2253", on_event)
        try:
            time.sleep(10)
        finally:
            listener.delete()


if __name__ == "__main__":
    main()
