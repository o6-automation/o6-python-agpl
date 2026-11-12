# Advanced Session Management

Use session transfer or reverse connect when an application needs to manage channels separately from its session.
Session-transfer snippets assume configured clients and the authentication
token and nonce from the session being transferred.

## Sessions and channels, beyond connect

### Session transfer

An OPC UA Session can be re-bound to a new SecureChannel.

If this client owns the session and its channel was renewed or
re-established, re-bind it:

```python
client.activateCurrentSession()
```

If another client owns the session and you want to take it over, open a channel
without a session and activate the existing one with its authentication token
and server nonce:

```python
receiver.connect(noSession=True)
receiver.activateSession(authToken, serverNonce)
```

Both calls send `ActivateSession` and then create the default subscription.
On the handing-over side, close the channel and keep the session alive with
`disconnect(closeSession=False)`.

### Reverse connect

In reverse connect, the server opens the TCP connection. Use it to reach a
client behind a firewall. The client opens a listen socket and waits:

```python
from o6 import Client

client = Client("opc.tcp://localhost:4840")     # still needed: the server's URL
client.startReverseConnect(port=4843, hostnames=["0.0.0.0"])
# returns once a server has connected — the session is activated
value = client.read("i=2258")          # ServerStatus.CurrentTime
client.disconnect()
```

The call returns only after a server connects, so synchronous code blocks.
In an async function, the connection step can instead use a timeout:

```python
import asyncio

task = asyncio.ensure_future(client.startReverseConnect(4843))
await asyncio.wait_for(task, timeout=15)
print(client.connected)   # True
```

`hostnames` selects which interfaces to advertise. `None` or an empty list
lets the stack decide. You must still configure the endpoint URL; the client
uses it to identify the server it expects. Close the connection with
`disconnect()`. The server side is `server.addReverseConnect(url)` and
`server.removeReverseConnect(handle)`.
