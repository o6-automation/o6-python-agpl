# Username / Password Authentication

Opens an OPC UA session with a username and password through the
high-level ``o6.Client`` API. The credentials are keyword arguments of
the ``Client(...)`` constructor. The SDK sends them in the
``ActivateSession`` request on connect.

Username and password identify a client on a server that does not use
certificates for user authentication. Typical use cases:

- The server keeps a list of allowed users and refuses anonymous
  sessions.
- Several human users of one application should appear separately in
  the server's session list.

The example permits plaintext password tokens for a local development
server. Authentication succeeds only against a server that accepts the
credentials; ``S03_firststeps.py`` rejects unknown users.

!!! info "This example needs a running server"
    Start [Server First Steps](server-S03_firststeps.md) first:

    ```
    python examples/server/S03_firststeps.py
    ```

The ``o6.Client`` constructor takes ``username=`` and ``password=``
keyword arguments. They do not weaken the default password policy. This
example sets ``allowNonePolicyPassword=True`` to permit unencrypted
password tokens. In deployment, configure encryption and keep the
default ``False``.

## 1. Connection Setup
The credentials are constants here. In real code, load them from
environment variables, a vault or a CLI argument.

```python
print("--- 1. Connection Setup ---")
localhost = "localhost"
endpoint_url = EXAMPLE_ENDPOINT

USERNAME = "user1"
PASSWORD = "password"

print(f"Connecting to {endpoint_url} as '{USERNAME}' ...")
```

## 2. Construct the Client with Credentials
Pass the credentials and explicitly opt in to this demonstration's
plaintext password transmission.

```python
print()
print("--- 2. Construct the Client with Credentials ---")
client = Client(endpoint_url, username=USERNAME, password=PASSWORD, allowNonePolicyPassword=True)
```

## 3. Open the Session
`connect()` opens the TCP connection and the SecureChannel, then calls
`ActivateSession` with the username/password token. Wrong credentials
on a server that requires authentication fail with
`BadIdentityTokenRejected` or a similar StatusCode.

`S03_firststeps.py` has no user management, so it rejects this
connection with `BadIdentityTokenRejected`. That is the correct
behavior for a server that does not know the user.

```python
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
```

## 4. Read After Authenticated Connect
After `connect()` returns, the session is authenticated. Every later
`read`, `write`, `call` and subscription runs inside that session
without re-sending the credentials. Authenticated operations work the
same as anonymous ones.

```python
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
```

## 5. Disconnect
`disconnect()` closes the session and the SecureChannel.

```python
print()
print("--- 5. Disconnect ---")
if AUTHENTICATED:
    client.disconnect()
    print("Disconnected.")
else:
    print("Skipping disconnect (no active session).")

print()
print("=== Example completed ===")
```

## Source Code

Download [`C05_usernamepw.py`](client-C05_usernamepw/C05_usernamepw.py) to run it locally.
