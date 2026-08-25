# State callbacks

Picking up from [Application description](310_application-description.md): the control plane and the HMI dashboard are both connected, named, and authenticated. But the network is not always kind — the server restarts, the cable is unplugged, the OPC UA session times out. The next step is to teach your client to notice when the connection state changes and react.

`o6` exposes the live state of a client's connection as a 3-tuple: `(SecureChannelState, SessionState, StatusCode)`. The `client.state` property returns it on demand — there's no separate "callback registration" API, you poll it. For a dashboard that's running its own event loop, polling once per UI frame is enough; for a long-running service, a dedicated thread or asyncio task polling on a timer is the typical shape.

This page walks through state callback primitives:

- Read `client.state` and understand what each field means.
- Drive an asyncio task off the state tuple to react to drops.
- Distinguish "channel renegotiated" from "session reactivated" from "totally lost".

!!! info
    This tutorial expects the [example server running](../../tutorials.md#running-the-example-server) in the background, and assumes you know how to [create and connect](100_connect.md) a client, how to [browse](110_browse.md) the address space, how to [secure](300_security.md) the connection, and how to name your client in [Application description](310_application-description.md). The snippets use the distillery's `DistillingSystem` at `ns=1;i=1000` to demonstrate the state transitions.

---

## Read `client.state`

`client.state` returns a `tuple[SecureChannelState, SessionState, StatusCode]`. The two `*State` fields are enums, and the third is the most recent status code the worker thread saw. If you followed the other tutorials to this point, the channel shoud be `open` and the session `activated`:

```python
from o6 import Client, SecureChannelState, SessionState

with Client("opc.tcp://localhost:4840") as client:
    channel, session, status = client.state
    print("channel :", channel)   # e.g. SecureChannelState.OPEN
    print("session :", session)   # e.g. SessionState.ACTIVATED
    print("status  :", status)
```

The interesting values for a connected client are:

- **`SecureChannelState.OPEN`** — the secure channel is up and messages can flow.
- **`SessionState.ACTIVATED`** — the OPC UA session is active and the server has accepted our `user_identity_token`.

`client.connected` is a convenience for "channel OPEN **and** session ACTIVATED":

```python
print(client.connected)   # True
```

The full state machine has more values, but the common ones a dashboard cares about are:

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

Anything other than `OPEN` and `ACTIVATED` means the client is *not* in a usable state.

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

For a long-running service, a single asyncio task that polls `client.state` is the standard shape. When the session drops, log it; when it comes back, resume work. Let's look at the state of pur control loop of the distillery — make sure the client isn't "disconnected" and send a notification the moment the state moves off `ACTIVATED`.

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

If the distillery server restarts mid-run, the session goes `ACTIVATED -> CLOSING -> CLOSED`. If the network drops, the channel will hit a `BadCommunicationError` and the status code on the `state` tuple will record it. The watcher only has to compare against the last value and log the transitions.

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

`SecureChannelState` and `SessionState` move independently, which is useful when you're debugging connection issues. A common pattern:

- **`channel` changed but `session` is still `ACTIVATED`:** the channel was renegotiated (cert renewal, transport refresh) and the session was kept alive across it. Nothing to do.
- **`session` dropped but `channel` is still `OPEN`:** the OPC UA session expired or was closed by the server. You can still try to `client.connect()` again to reactivate it (the underlying channel survives).
- **Both `CLOSED`:** the connection is fully gone. Reconnect from scratch.

For the distillery, if the server is restarting while the client is running, you'll see the `session` field transition through `CLOSING -> CLOSED` while the `channel` field lingers on `OPEN` for a moment, then itself goes `CLOSING -> CLOSED`. Catching the session drop first is the right place to surface "reconnecting…" in the UI.

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

## What's next?

- [Load packaged companion specs](410_load-packaged-companion-specs.md) — make `o6.ns.di`, `o6.ns.ia`, and the other bundled companion-spec types available on a client, so the type tree in the distillery's address space can be navigated from Python.