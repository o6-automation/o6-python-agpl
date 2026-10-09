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
Client Username / Password Authentication
==================================

Demonstrates how to open an OPC UA session with a username and
password using the high-level ``o6.Client`` API. The credentials
are passed as keyword arguments to the ``Client(...)`` constructor;
the SDK forwards them to the server's ``ActivateSession`` request
when the connection is established.

Username / password authentication is the most common way to
identify a client on a non-certificate-protected server. Typical
use cases:

- The server's user-management system has a list of allowed
  usernames and passwords, and refuses anonymous sessions.
- The application has multiple human users that should appear separately
  in the server's session list.

This demonstration explicitly permits plaintext password tokens for a local
development server. Successful authentication still requires a server that
accepts these credentials; ``S03_firststeps.py`` rejects unknown users.
"""


import os

import socket
from o6 import Client, StatusCodeError

EXAMPLE_PORT = int(os.environ.get("O6_EXAMPLE_PORT", "4840"))
EXAMPLE_ENDPOINT = f"opc.tcp://localhost:{EXAMPLE_PORT}"


print("--- 1. Connection Setup ---")
localhost = "localhost"
endpoint_url = EXAMPLE_ENDPOINT

USERNAME = "user1"
PASSWORD = "password"

print(f"Connecting to {endpoint_url} as '{USERNAME}' ...")


print()
print("--- 2. Construct the Client with Credentials ---")
client = Client(endpoint_url, username=USERNAME, password=PASSWORD, allowNonePolicyPassword=True)



print()
print("--- 3. Open the Session ---")
try:
    client.connect()
    print(f"Connected to {endpoint_url}")
    AUTHENTICATED = True
except StatusCodeError as e:
    print(f"Error: failed to connect: {e.symbol} (0x{e.code:08x})")
    if e.symbol == "BadIdentityTokenRejected":
        print("The server rejected the username / password: S03_firststeps.py")
        print("has no user-management system configured, so it does not know")
        print("the user 'user1'. This is the expected, correct behavior for")
        print("an unconfigured server.")
    else:
        print("Unexpected error — see the message above for details.")
    AUTHENTICATED = False



print()
print("--- 4. Read After Authenticated Connect ---")
if AUTHENTICATED:
    try:
        counter = client.read("ns=1;i=1004")
        print(f"Counter = {counter}")

        temperature = client.read("ns=1;i=1001")
        print(f"Temperature = {temperature}")

        values = client.read(
            [
                "ns=1;i=1001",  # Temperature (Double)
                "ns=1;i=1002",  # Pressure    (Double)
                "ns=1;i=1003",  # Status      (String)
                "ns=1;i=1004",  # Counter     (Int32)
            ]
        )
        print(f"Read = {values}")
    except StatusCodeError as e:
        print(f"Error: read failed: {e}")
else:
    print("Skipping reads (no authenticated session).")



print()
print("--- 5. Disconnect ---")
if AUTHENTICATED:
    client.disconnect()
    print("Disconnected.")
else:
    print("Skipping disconnect (no active session).")

print()
print("=== Example completed ===")