# Reverse Connect

Let the server initiate the TCP connection to a listening client.

## Reverse connect

With reverse connect, the server opens the TCP connection to a listening
client. Use it to reach a client behind a firewall:

```python
handle = server.addReverseConnect("opc.tcp://localhost:4843")
# ... the server retries periodically until the client answers ...
server.removeReverseConnect(handle)
```

`callback=` receives `(handle, state)` on every state change. On the client,
`client.startReverseConnect(port)` returns only after the server has connected.
See [Client](../client/sessions.md#reverse-connect).
