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

Walks through the configuration surface of ``o6.Client``. Every
property the client cares about (endpoint URL, request timeout,
session name, application identity, security settings, …) lives on
the ``ClientConfig`` object returned by ``client.config`` and can be
read and (in most cases) written through Python attribute
access.

The key rule this example demonstrates: **all writes to
``client.config`` must happen before the client is connected**. The
SDK raises ``RuntimeError`` if you try to mutate a field while the
session is active.

This example talks to the same address space as the other high-level
examples, served by ``S03_firststeps.py``.
"""

# BEGIN MD
# The ``o6.Client`` constructor takes a small set of *connect-time*
# keyword arguments (endpoint URL, security mode, application URI,
# certificate paths, username and password). The rest of the configuration fields (request timeout,
# session timeout, secure channel lifetime, application description,
# …) can only be reached through ``client.config``; they are *not*
# constructor arguments.
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
# `client.config` exposes the client settings. The defaults below are
# what the SDK ships with. You will not be using most of them, but
# it's useful to see them in one place before you start changing any.
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
# **connect-time** (set once, baked into the SecureChannel and
#   `ActivateSession` handshake), or
# **runtime** (read-only at runtime; can be inspected but not
#   changed once connected).
#
# The SDK enforces this: writing to a connect-time field while the
# client is connected raises `RuntimeError`. The block below
# demonstrates the failure mode so you can recognize it if you hit it.
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
# The correct workflow is: construct the client, mutate `client.config`
# as you like, then enter the `with` block (or call
# `connect()` explicitly).
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
# When the client opens a session, the server is told *who* is
# connecting: an `ApplicationDescription` with the application's
# URI, a human-readable name, the application type (client, server,
# or both), and a product URI.
#
# The `ApplicationDescription` class is on `ns0.datatypes`; the `LocalizedText`
# wrapper for the name field is on the `o6` module. Both
# are simple Python classes: instantiate them, set the fields,
# then assign the result to `client.config.applicationDescription`.
# This must also happen **before** the client is connected.
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
# A small number of connect-time settings can be passed either to
# the `o6.Client(...)` constructor (`application_uri`, the security
# mode/policy, certificate paths, username/password) **or**
# written to `client.config` *before* connecting. Both routes end up
# in the same underlying `ClientConfig` object.
#
# Everything else (timeout, session name, secure channel lifetime,
# the full `ApplicationDescription`, …) is **only** reachable through
# `client.config`. So these fields have to be defined before connecting.
#
# The block below uses the constructor for `application_uri` and
# `client.config` for the read-only inspection, then enters the
# `with` block to verify the value and read a real variable.
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
