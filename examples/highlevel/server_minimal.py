#!/usr/bin/env python3
# Copyright 2026 (c) o6 Automation GmbH
"""
Minimal OPC UA Server
=====================

The smallest possible server – just 6 lines of code.
Starts an OPC UA server on port 4840 and runs until Ctrl+C.

    opc.tcp://localhost:4840
"""

# BEGIN MD
# This is the absolute baseline of an OPC UA Server.
# Just by calling `server.start()`, this script provides a fully compliant OPC UA endpoint.
# END MD

# BEGIN CODE
import time
from o6 import Server

server = Server(port=4840)
server.start()

print("Server running – press Ctrl+C to stop")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pass

server.stop()
# END CODE
