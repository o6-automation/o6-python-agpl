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
Client Configuration
====================

Every client setting (endpoint URL, request timeout, session name,
application identity, security settings, …) lives on the
``ClientConfig`` object returned by ``client.config``. Most fields can
be read and written as Python attributes.

**Write to ``client.config`` only before the client connects.** Writing
a field while the session is active raises ``RuntimeError``.

The example uses the address space of ``S03_firststeps.py``.
"""

# BEGIN MD
# The ``o6.Client`` constructor takes a few connect-time keyword
# arguments: endpoint URL, security mode, application URI, certificate
# paths, username and password. All other fields (request timeout,
# session timeout, secure channel lifetime, application description, …)
# are reachable only through ``client.config``.
# END MD

import os

import socket
import o6
from o6 import LocalizedText
from o6.ns import ns0

EXAMPLE_PORT = int(os.environ.get("O6_EXAMPLE_PORT", "4840"))
EXAMPLE_ENDPOINT = f"opc.tcp://localhost:{EXAMPLE_PORT}"

# BEGIN MD
# ## 1. Inspect the Default Configuration
# `client.config` exposes the client settings. The values printed below
# are the SDK defaults.
# END MD

# BEGIN CODE
print("--- 1. Inspect the Default Configuration ---")
localhost = "localhost"
endpoint_url = EXAMPLE_ENDPOINT
print(f"Connecting to {endpoint_url} ...")

with o6.Client(endpoint_url) as client:
    cfg = client.config

    print(f"endpoint_url              = {cfg.endpointUrl!r}")
    print(f"timeout (ms)              = {cfg.timeout}")
    print(f"session_name              = {cfg.sessionName!r}")
    print(f"application_uri           = {cfg.applicationUri!r}")
    print(f"secure_channel_life_time  = {cfg.secureChannelLifeTime} ms")
    print(f"requested_session_timeout = {cfg.requestedSessionTimeout} ms")
    print(f"max_async_service_calls   = {cfg.maxAsyncServiceCalls}")
    print(f"no_session                = {cfg.noSession}")
    print(f"no_reconnect              = {cfg.noReconnect}")
    print(f"security_mode             = {cfg.securityMode}")
    print(f"security_policy           = {cfg.securityPolicy!r}")
# END CODE

# BEGIN MD
# ## 2. Configure Before You Connect
# Every field on `ClientConfig` is either
# **connect-time** (set once and used for the SecureChannel and
#   `ActivateSession` handshake), or
# **runtime** (can be inspected but not changed once connected).
#
# Writing a field while the client is connected raises `RuntimeError`.
# The code below triggers that error.
# END MD

# BEGIN CODE
print()
print("--- 2. Configure Before You Connect ---")
with o6.Client(endpoint_url) as client:
    cfg = client.config
    try:
        cfg.timeout = 1234
    except RuntimeError as e:
        print(f"Error: {e}")
# END CODE

# BEGIN MD
# ## 3. Set Scalar Fields Before Connecting
# Construct the client, set fields on `client.config`, then enter the
# `with` block or call `connect()`.
# END MD

# BEGIN CODE
print()
print("--- 3. Set Scalar Fields Before Connecting ---")
client = o6.Client(endpoint_url)
client.config.timeout = 1234  # milliseconds
client.config.sessionName = "hmi-client-1"  # shown in the server's session list
client.config.secureChannelLifeTime = 300_000  # 5 minutes
client.config.maxAsyncServiceCalls = 128  # concurrent calls; 0 disables the limit

print(f"timeout                  = {client.config.timeout}")
print(f"session_name             = {client.config.sessionName!r}")
print(f"secure_channel_life_time = {client.config.secureChannelLifeTime}")
print(f"max_async_service_calls  = {client.config.maxAsyncServiceCalls}")

with client as c:
    cfg = c.config
    print(f"timeout (connected)      = {cfg.timeout}")
# END CODE

# BEGIN MD
# ## 4. Set the Application Identity
# When the client opens a session, it sends the server an
# `ApplicationDescription`: the application URI, a human-readable name,
# the application type (client, server or both) and a product URI.
#
# `ApplicationDescription` is in `ns0.datatypes`. The `LocalizedText`
# used for the name is in `o6`. Create both, set the fields and assign
# the result to `client.config.applicationDescription` before the
# client connects.
# END MD

# BEGIN CODE
print()
print("--- 4. Set the Application Identity ---")
client = o6.Client(endpoint_url)
cfg = client.config

ApplicationDescription = ns0.datatypes.ApplicationDescription
ApplicationType = ns0.datatypes.ApplicationType

desc = ApplicationDescription()
desc.applicationUri = "urn:example:o6:demo-client"
desc.applicationName = LocalizedText("o6 Demo Client")
desc.applicationType = ApplicationType.CLIENT
desc.productUri = "urn:example:o6"

cfg.applicationDescription = desc

print(f"application_uri  = {cfg.applicationDescription.applicationUri!r}")
print(f"application_name = {cfg.applicationDescription.applicationName!r}")
print(f"application_type = {cfg.applicationDescription.applicationType}")
print(f"product_uri      = {cfg.applicationDescription.productUri!r}")

with client as c:
    cfg = c.config
    print(f"application_description (connected) = {cfg.applicationDescription}")
# END CODE

# BEGIN MD
# ## 5. Constructor and `client.config`
# A few connect-time settings can be passed to the `o6.Client(...)`
# constructor (`applicationUri`, security mode and policy, certificate
# paths, username and password) or written to `client.config` before
# connecting. Both set the same `ClientConfig`.
#
# All other fields (timeout, session name, secure channel lifetime, the
# full `ApplicationDescription`, …) are reachable only through
# `client.config`, before connecting.
#
# The code passes `applicationUri` to the constructor, then reads it back
# from `client.config` and reads a variable.
# END MD

# BEGIN CODE
print()
print("--- 5. Constructor and client.config ---")
with o6.Client(
    endpoint_url,
    applicationUri="urn:example:o6:demo-client",
) as client:
    cfg = client.config
    print(f"endpoint_url    = {cfg.endpointUrl!r}")
    print(f"application_uri = {cfg.applicationUri!r}")

    value = client.read("ns=1;i=1004")  # Plant / Counter
    print(f"Counter = {value}")

print()
print("=== Example completed ===")
# END CODE
