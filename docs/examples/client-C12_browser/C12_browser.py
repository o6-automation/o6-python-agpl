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
Interactive Address-Space Browser
=================================

Walks the server's address space from a terminal using the high-level
``Client.browseInteractive()`` helper. The browser is a terminal
UI: arrow keys (or ``h/j/k/l``) move through the children of
the current node, ``Enter`` drills into a child, ``h`` / ``Backspace``
goes back up the tree, ``/`` filters children by a fuzzy substring
match, and ``q`` quits.

``browseInteractive()`` is the only entry point. When the user quits
with ``Enter`` on a child, a small dialog asks whether to return the
**NodeId** of the selected node or a **BrowsePath** slash-delimited
string. ``browseInteractive()`` then returns that string. The return
value is the part of the API a script can plug into a follow-up
``client.read(returned_string)`` call without re-walking the tree.

![OPC UA Interactive Browser](../assets/browse-interactive.png)

The example targets ``S03_firststeps.py``. ``browseInteractive()``
requires the standard-library ``curses`` module (on Windows, install
``windows-curses``).
"""


import socket
import sys
import o6
from o6 import Client, StatusCodeError


localhost = "localhost"
endpoint_url = f"opc.tcp://{localhost}:4840"

start_nodeid: str | None = None
if len(sys.argv) > 1:
    start_nodeid = sys.argv[1]
    print(f"Starting browser at {start_nodeid}")
else:
    print("Starting browser at the address-space root (pass a NodeId to start elsewhere)")



try:
    with Client(endpoint_url) as client:
        result = client.browseInteractive(start_nodeid)
        if result is not None:
            print()
            print(f"Selected: {result}")
except StatusCodeError as e:
    print(f"Error: failed to connect: {e.symbol} (0x{e.code:08x})")
    sys.exit(1)

