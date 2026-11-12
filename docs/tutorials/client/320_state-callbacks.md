# State Callbacks

Detect when the connection state changes, for example when the server restarts, the cable is unplugged or the session times out, and react to it.

The `client.state` property returns the connection state as a 3-tuple `(SecureChannelState, SessionState, StatusCode)`. There is no callback registration API; you poll `client.state`. A dashboard with its own event loop polls once per UI frame. A long-running service polls on a timer from a dedicated thread or asyncio task.

!!! info
    This tutorial expects the [example server running](../setup.md) in the background. It builds on [Connect](100_connect.md), [Browse](110_browse.md), [Security](300_security.md) and [Application description](310_application-description.md). The snippets use the distillery's `DistillingSystem` at `ns=1;i=1000`.

---

## Read `client.state`

`client.state` returns a `tuple[SecureChannelState, SessionState, StatusCode]`. The two `*State` fields are enums. The third is the most recent status code the worker thread saw. On a connected client, the channel is `OPEN` and the session `ACTIVATED`:

```python
from o6 import Client, SecureChannelState, SessionState

with Client("opc.tcp://localhost:4840") as client:
    channel, session, status = client.state
    print("channel :", channel)   # e.g. SecureChannelState.OPEN
    print("session :", session)   # e.g. SessionState.ACTIVATED
    print("status  :", status)
```

- **`SecureChannelState.OPEN`**: the secure channel is up and messages can flow.
- **`SessionState.ACTIVATED`**: the session is active and the server accepted the `user_identity_token`.

`client.connected` is `True` when the channel is `OPEN` and the session is `ACTIVATED`:

```python
print(client.connected)   # True
```

The state machine has more values. The common ones are:

| `SecureChannelState` | Meaning |
|---|---|
| `CLOSED` | No channel. Default before `connect()`. |
| `CONNECTING` | TCP / handshake in progress. |
| `OPEN` | Channel up. |
| `CLOSING` | Channel tearing down. |

| `SessionState` | Meaning |
|---|---|
| `CLOSED` | No session. Default before `connect()`. |
| `CREATED` | `CreateSession` request sent / acknowledged. |
| `ACTIVATED` | `ActivateSession` accepted — fully usable. |
| `CLOSING` | Session tearing down. |

In any other combination than `OPEN` and `ACTIVATED`, the client is not usable.

#### Putting it all together

```python
from o6 import Client

with Client("opc.tcp://localhost:4840") as client:
    channel, session, status = client.state
    print(f"channel={channel.name}  session={session.name}  status={status}")
    print(f"connected: {client.connected}")
```

---

## React to state changes in an asyncio task

In a long-running service, poll `client.state` from one asyncio task. Log when the session drops and resume work when it comes back. The watcher below prints every session transition and stops when the session is `CLOSED`.

```python
import asyncio
from o6 import Client, SessionState

async def watch_state(client):
    last = None
    while True:
        _, session, status = client.state
        if session != last:
            print(f"session: {last} -> {session} (status={status})")
            last = session
        if session == SessionState.CLOSED:
            print("connection lost — stopping work")
            return
        await asyncio.sleep(0.5)

with Client("opc.tcp://localhost:4840") as client:
    asyncio.run(watch_state(client))
```

If the server restarts, the session goes `ACTIVATED -> CLOSING -> CLOSED`. If the network drops, the channel hits `BadCommunicationError` and the status code in the `state` tuple records it.

#### Putting it all together

```python
import asyncio
from o6 import Client, SessionState

async def watch(client):
    last = None
    while True:
        _, session, status = client.state
        if session != last:
            print(f"{last} -> {session}  ({status})")
            last = session
        if session == SessionState.CLOSED:
            break
        await asyncio.sleep(0.5)

with Client("opc.tcp://localhost:4840") as client:
    asyncio.run(watch(client))
```

---

## Distinguish "channel renegotiated" from "session lost"

`SecureChannelState` and `SessionState` change independently:

- **`channel` changed, `session` still `ACTIVATED`:** the channel was renegotiated (certificate renewal, transport refresh) and the session survived. Nothing to do.
- **`session` dropped, `channel` still `OPEN`:** the session expired or the server closed it. Call `client.connect()` again to reactivate it; the channel survives.
- **Both `CLOSED`:** the connection is gone. Reconnect from scratch.

When the server restarts, `session` goes `CLOSING -> CLOSED` first while `channel` stays `OPEN` for a moment, then also goes `CLOSING -> CLOSED`. Show "reconnecting…" in the UI when the session drops.

```python
import asyncio
from o6 import Client, SecureChannelState, SessionState

async def watch_both(client):
    last_ch, last_se = None, None
    while True:
        ch, se, status = client.state
        if ch != last_ch:
            print(f"channel: {last_ch} -> {ch}")
            last_ch = ch
        if se != last_se:
            print(f"session: {last_se} -> {se}  ({status})")
            last_se = se
        if ch == SecureChannelState.CLOSED and se == SessionState.CLOSED:
            print("fully disconnected — stopping watch")
            return
        await asyncio.sleep(0.25)

with Client("opc.tcp://localhost:4840") as client:
    asyncio.run(watch_both(client))
```

#### Putting it all together

```python
import asyncio
from o6 import Client, SecureChannelState, SessionState

async def watch(client):
    last_ch, last_se = None, None
    while True:
        ch, se, status = client.state
        if ch != last_ch or se != last_se:
            print(f"channel={ch.name}  session={se.name}  status={status}")
            last_ch, last_se = ch, se
        if ch == SecureChannelState.CLOSED and se == SessionState.CLOSED:
            return
        await asyncio.sleep(0.25)

with Client("opc.tcp://localhost:4840") as client:
    asyncio.run(watch(client))
```

---

## Next steps

| Topic | What it covers |
|---|---|
| [Load packaged companion specs](410_load-packaged-companion-specs.md) | Make `o6.ns.di`, `o6.ns.ia` and the other bundled companion specification types available on a client to navigate the distillery's type tree from Python. |
