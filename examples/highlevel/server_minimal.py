#!/usr/bin/env python3
"""
Minimal OPC UA Server
=====================

The smallest possible server – just 6 lines of code.
Starts an OPC UA server on port 4840 and runs until Ctrl+C.

    opc.tcp://localhost:4840
"""

from o6 import Server

server = Server(port=4840)
server.start()

print("Server running – press Ctrl+C to stop")

try:
    while True:
        import time

        time.sleep(1)
except KeyboardInterrupt:
    pass

server.stop()
