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

``Client.browseInteractive()`` opens a terminal UI for the server's
address space. Arrow keys (or ``h/j/k/l``) move through the children of
the current node, ``Enter`` opens a child, ``h`` / ``Backspace`` goes
back up, ``/`` filters the children by a fuzzy substring match, and
``q`` quits.

``s`` on a child opens a dialog that quits and returns either the
**NodeId** of that node or its slash-delimited **BrowsePath**.
``browseInteractive()`` returns that string, which a script can pass to
``client.read(returned_string)`` without walking the tree again.

![OPC UA Interactive Browser](../assets/browse-interactive.png)

The example targets ``S03_firststeps.py``. ``browseInteractive()``
requires the standard-library ``curses`` module (on Windows, install
``windows-curses``).
"""

# BEGIN MD
# The interactive browser uses the same ``Browse`` service as
# ``client.browse()`` and ``client[NodeId]``, but shows the result in a
# UI instead of returning Python objects.
# END MD

import socket
import sys
import o6
from o6 import Client, StatusCodeError

# BEGIN MD
# ## 1. Endpoint and starting node
# The starting NodeId is optional. Without it the browser opens at the
# Root folder (``i=84``). Pass a NodeId as a CLI argument to start
# elsewhere, for example the Objects folder ``"i=85"`` or a sensor on
# ``S03_firststeps.py`` such as ``"ns=1;i=1001"``.
# END MD

# BEGIN CODE
localhost = "localhost"
endpoint_url = f"opc.tcp://{localhost}:4840"

start_nodeid: str | None = None
if len(sys.argv) > 1:
    start_nodeid = sys.argv[1]
    print(f"Starting browser at {start_nodeid}")
else:
    print("Starting browser at the address-space root (pass a NodeId to start elsewhere)")
# END CODE


# BEGIN MD
# ## 2. Connect and launch the browser
# The browser takes over the terminal until the user quits. The code
# connects, runs the browser inside a ``with`` block, and lets
# ``__exit__`` close the session. A ``StatusCodeError`` from
# ``connect()`` (server down, wrong URL, authentication rejected) is
# caught and reported. Exceptions raised while ``browseInteractive``
# runs propagate out of the ``with`` block.
#
# The function returns a NodeId string such as ``"ns=1;i=1001"``, a
# BrowsePath such as ``"/Objects/Plant/Temperature"``, or ``None``,
# depending on how the user quits. The example prints the result, so the
# script works as a "find me a NodeId" tool from the shell.
# END MD

# BEGIN CODE
try:
    with Client(endpoint_url) as client:
        result = client.browseInteractive(start_nodeid)
        if result is not None:
            print()
            print(f"Selected: {result}")
except StatusCodeError as e:
    print(f"Error: failed to connect: {e.symbol} (0x{e.code:08x})")
    sys.exit(1)
# END CODE


# BEGIN MD
# ## 3. Key bindings
# The browser starts in navigation mode. ``/`` switches to filter mode,
# where keystrokes edit the filter; ``Enter`` confirms it and ``Esc``
# cancels it.
#
# | key                       | action                                  |
# |---------------------------|-----------------------------------------|
# | ``j`` / Down              | move down one row                       |
# | ``k`` / Up                | move up one row                         |
# | ``J`` / Page Down         | move down one page                      |
# | ``K`` / Page Up           | move up one page                        |
# | ``h`` / Left / Backspace  | go back to the parent                   |
# | ``l`` / Right / Enter     | open the highlighted child              |
# | ``/``                     | start a fuzzy filter on the child list  |
# | ``Esc``                   | clear the filter                        |
# | ``s``                     | open the select dialog                  |
# | ``q``                     | quit (returns ``None``)                 |
#
# The select dialog has three options: quit with the NodeId (``n``), quit
# with the BrowsePath (``p``), or cancel (``q``).
# END MD
