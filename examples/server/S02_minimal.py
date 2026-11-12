#!/usr/bin/env python3
# Copyright 2026 (c) o6 Automation GmbH
# SPDX-License-Identifier: AGPL-3.0-or-later
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

"""
Minimal OPC UA Server
=====================

The smallest possible server: 6 lines of code.
Starts an OPC UA server on port 4840 and runs until Ctrl+C.

    opc.tcp://localhost:4840
"""

# BEGIN MD
# `server.start()` alone provides a fully compliant OPC UA endpoint.
# END MD

# BEGIN CODE
import os

import time
from o6 import Server

EXAMPLE_PORT = int(os.environ.get("O6_EXAMPLE_PORT", "4840"))

server = Server(port=EXAMPLE_PORT)
server.start()

print(f"Server running at opc.tcp://localhost:{EXAMPLE_PORT}")
print("Press Ctrl+C to stop.")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Shutting down...")

server.stop()
print("Server stopped.")
# END CODE
