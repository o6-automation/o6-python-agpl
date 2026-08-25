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

``basic_server.py`` is unencrypted and does **not**
enforce authentication, so the example below will succeed even
with arbitrary credentials.

The ``o6.Client`` constructor takes ``username=`` and ``password=``
as keyword arguments. The SDK stashes them on the underlying
``ClientConfig`` object and also
sets ``allow_none_policy_password = True`` so the client can
connect to servers that advertise a username/password token
but with no transport encryption (the unencrypted
``basic_server.py`` falls into this category).

## 1. Connection Setup
`socket.gethostname()` matches the convention used by the other
examples; the actual URL is the same one the server is listening
on. The credentials are coded as constants for the purpose of this
example but in real code you'd typically load
them from environment variables, a vault,
or a CLI argument.

```python
localhost = "localhost"
endpoint_url = f"opc.tcp://{localhost}:4840"

USERNAME = "user1"
PASSWORD = "password"

print(f"Connecting to {endpoint_url} as '{USERNAME}' ...")
```

## 2. Construct the Client with Credentials
Passing ``username=`` and ``password=`` to the constructor is
the only thing that distinguishes this example from the
credential-less ``client_basic.py``.

```python
client = Client(endpoint_url, username=USERNAME, password=PASSWORD)
```

## 3. Open the Session
`connect()` runs the full OPC UA process: open the TCP
connection, open the SecureChannel, and then `ActivateSession`
with the username/password token. On a server that requires
authentication, the wrong credentials will cause this to fail
with a `BadIdentityTokenRejected` (or similar) StatusCode.

`basic_server.py` has no user-management system configured, so
it rejects this connection with `BadIdentityTokenRejected`
(which is the *correct* behavior for a server that doesn't know
the user).

```python
try:
    client.connect()
    print(f"  Connected to {endpoint_url}")
    AUTHENTICATED = True
except StatusCodeError as e:
    print(f"  Failed to connect: {e.symbol} (0x{e.code:08x})")
    if e.symbol == "BadIdentityTokenRejected":
        print("  The server rejected the username / password.")
        print("  basic_server.py has no user-management system configured")
        print("  — it does not know the user 'user1'.")
        print("  This is the expected, correct behavior for an")
        print("  unconfigured server.")
    else:
        print("  Unexpected error — see the message above for details.")
    AUTHENTICATED = False
```

## 4. Read After Authenticated Connect
Once `connect()` has returned, the client is in an authenticated
session. The credentials are stored in the SDK; every subsequent
`read`/`write`/`call`/`subscription` happens *inside* that
session, so there's no need to re-supply them.

The example reads a few nodes from `basic_server.py` (`Plant` /
`Counter` and `Plant` / `Temperature`) to demonstrate that
authenticated operations work the same as anonymous ones.

```python
if AUTHENTICATED:
    try:
        counter = client.read("ns=1;i=1004")
        print(f"  Counter    = {counter}")

        temperature = client.read("ns=1;i=1001")
        print(f"  Temperature = {temperature}")

        values = client.read(
            [
                "ns=1;i=1001",  # Temperature (Double)
                "ns=1;i=1002",  # Pressure    (Double)
                "ns=1;i=1003",  # Status      (String)
                "ns=1;i=1004",  # Counter     (Int32)
            ]
        )
        print(f"  Multiple read = {values}")
    except StatusCodeError as e:
        print(f"  Read failed: {e}")
else:
    print("  Skipping reads (no authenticated session).")
```

## 5. Disconnect
`disconnect()` closes the session and the SecureChannel.

```python
if AUTHENTICATED:
    client.disconnect()
    print("  Disconnected.")
else:
    print("  Skipping disconnect (no active session).")

print("\n=== Example completed ===")
```

## Complete Source Code

```python
#!/usr/bin/env python3
# Copyright 2026 (c) o6 Automation GmbH
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

``basic_server.py`` is unencrypted and does **not**
enforce authentication, so the example below will succeed even
with arbitrary credentials.
"""


import socket
from o6 import Client, StatusCodeError


localhost = "localhost"
endpoint_url = f"opc.tcp://{localhost}:4840"

USERNAME = "user1"
PASSWORD = "password"

print(f"Connecting to {endpoint_url} as '{USERNAME}' ...")


client = Client(endpoint_url, username=USERNAME, password=PASSWORD)



try:
    client.connect()
    print(f"  Connected to {endpoint_url}")
    AUTHENTICATED = True
except StatusCodeError as e:
    print(f"  Failed to connect: {e.symbol} (0x{e.code:08x})")
    if e.symbol == "BadIdentityTokenRejected":
        print("  The server rejected the username / password.")
        print("  basic_server.py has no user-management system configured")
        print("  — it does not know the user 'user1'.")
        print("  This is the expected, correct behavior for an")
        print("  unconfigured server.")
    else:
        print("  Unexpected error — see the message above for details.")
    AUTHENTICATED = False



if AUTHENTICATED:
    try:
        counter = client.read("ns=1;i=1004")
        print(f"  Counter    = {counter}")

        temperature = client.read("ns=1;i=1001")
        print(f"  Temperature = {temperature}")

        values = client.read(
            [
                "ns=1;i=1001",  # Temperature (Double)
                "ns=1;i=1002",  # Pressure    (Double)
                "ns=1;i=1003",  # Status      (String)
                "ns=1;i=1004",  # Counter     (Int32)
            ]
        )
        print(f"  Multiple read = {values}")
    except StatusCodeError as e:
        print(f"  Read failed: {e}")
else:
    print("  Skipping reads (no authenticated session).")



if AUTHENTICATED:
    client.disconnect()
    print("  Disconnected.")
else:
    print("  Skipping disconnect (no active session).")

print("\n=== Example completed ===")
```
