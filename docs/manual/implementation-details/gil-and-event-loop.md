# GIL and event-loop bridging

o6\\Python integrates open62541 with an asyncio event loop. That loop may
run on an SDK worker thread or on an application-owned thread. This page
explains how the binding coordinates open62541's event-loop mutex and the
CPython GIL when multiple threads access the same client or server.

!!! info "Prerequisites"
    The user-facing pages [Server / Lifecycle & configuration][server-lifecycle]
    and [Client / Lifecycle](../client/lifecycle.md) describe the public
    event-loop model. This page explains the C-level mechanism behind it.

[server-lifecycle]: ../server/lifecycle.md

## The two locks

The loop thread drives I/O and callbacks. In a synchronous script it is
normally an SDK worker; in an async application it is normally the thread
running `asyncio.run()`. A supplied loop can run on another application thread.
See the [client](../client/lifecycle.md#event-loops-and-integration) and
[server](../server/lifecycle.md#event-loops-and-integration) loop-selection rules.

The following discussion assumes a separate calling thread accesses the same
object. Two locks are involved:

| Lock | Owner | Purpose |
| --- | --- | --- |
| `elMutex` | open62541 | Recursive mutex that protects every piece of `UA_EventLoop` state, including the linked list of event sources, the clock, and the timing wheel. |
| GIL | CPython | Non-recursive lock that protects the interpreter. Held by any thread that touches Python objects. Released around `syscall`s. |

Both threads need both locks at different moments. The loop thread calls
into Python to dispatch a callback, retire a subscription or convert a value.
The calling thread calls into open62541 for synchronous admin operations,
lifecycle calls and the destroy sequence.

## The deadlock

Without the lock-order rule below, `AsyncIOTCP_sendWithConnection` can create
a cycle while sending a request from the loop thread:

1. The loop thread holds `elMutex`; open62541 took it on loop entry.
2. The loop thread calls into Python's `sock_sendall`, which calls
   `sock_send`, which releases the GIL around the underlying `send()`.
3. The calling thread, no longer blocked by the GIL, runs user code. It
   reaches a path that acquires `elMutex`, for example
   `client.state` → `lockClient` or any synchronous `*_admin` call.
4. The calling thread now holds the GIL and is waiting for `elMutex`.
5. The loop thread's `send()` returns, and that thread waits to reacquire the
   GIL.

| Thread | Holds | Needs |
| --- | --- | --- |
| Loop thread | `elMutex` | GIL (to finish its callback) |
| Calling thread | GIL | `elMutex` |

Each thread waits for the lock the other holds. The scheduler cannot break
the cycle: the loop thread is blocked on the GIL, not on
`pthread_cond_wait`.

The cycle needs both conditions:

- a `client` or `server` operation on the calling thread takes `elMutex`;
- the loop thread runs a TCP send that releases the GIL for the duration of
  the `send()` syscall.

The cycle occurs only on the `lock` side of the recursive mutex.
`AsyncIOLoop_unlock` is called by the loop thread that already owns
`elMutex`, and recursive acquisition does not block.

## The rule

The binding does not hold the GIL while it waits for `elMutex`.
`AsyncIOLoop_lock` is the only function that crosses the boundary. It releases
the GIL around the `UA_LOCK` acquisition:

```c
static void
AsyncIOLoop_lock(AsyncIOLoop *public_el) {
    Py_BEGIN_ALLOW_THREADS
    UA_LOCK(&((AsyncIOLoop*)public_el)->elMutex);
    Py_END_ALLOW_THREADS
}
```

`AsyncIOLoop_unlock` does not release the GIL. Only the loop thread
that owns `elMutex` calls it. The recursive case is a no-op. The
non-recursive case is the loop thread's own re-entry, where the same thread already
holds the GIL.

## Why the rule is safe

1. **`AsyncIOLoop_lock` is the only contention point.** Every other
   `UA_LOCK` / `UA_UNLOCK` on `elMutex` in the binding runs on the loop
   thread that already owns it. Acquisition there is recursive and immediate,
   so it does not release the GIL.
2. **The critical window holds no Python state.** Between
   `Py_BEGIN_ALLOW_THREADS` and `Py_END_ALLOW_THREADS`, the only operation is
   `pthread_mutex_lock`. The loop thread cannot change the calling thread's
   view of the interpreter state in that window.
3. **The lock order is consistent.** The effective order is always `elMutex`
   first, GIL second. The loop thread takes `elMutex` on loop entry and the
   GIL on its first call into Python. The calling thread holds the GIL while it
   runs user code and takes `elMutex` only after releasing the GIL in
   `AsyncIOLoop_lock`. The two orders do not form a cycle.
4. **No timing dependence.** The rule does not rely on `pthread_cond_wait`
   timeouts, `try-lock` fallbacks or the kernel scheduler. Lock-order
   discipline breaks the cycle.

## Where the rule applies

The recursive `elMutex` is the only lock the binding holds while waiting
for a loop thread. The same discipline applies to the synchronous lifecycle
calls `Client.connect`, `Client.disconnect`, `Server.start` and `Server.stop`,
and to the `Client.state` getter.

Other `UA_LOCK` calls run while the calling thread already owns the lock
(recursive), so they do not release the GIL. The discipline is asymmetric:
acquire `elMutex` without the GIL, release it without changing the GIL.

## Symptoms when the rule is broken

A violation has this signature:

- two healthy threads;
- one thread permanently parked on `pthread_mutex_lock`;
- the other thread permanently parked on `PyGILState_Ensure` (or the
  GIL-equivalent `eval_breaker` timeout);
- zero CPU, zero progress, no exception, no log line beyond the
  last successful operation.

A `kill -3` on the process shows both threads in this state. Adding a
timeout on either side does not fix it. Every call site that takes `elMutex`
must go through `AsyncIOLoop_lock`. A new unprotected `UA_LOCK` call, even a
short-lived one, reintroduces the deadlock.

## Related topics

| Topic | What it covers |
|---|---|
| [Memory management](memory-management.md) | The Python-side ownership rules for the event-loop thread. |
| [Client / Lifecycle](../client/lifecycle.md) | The public side of the loop, including `connect` and `disconnect`. |
| [Server / Lifecycle & configuration](../server/lifecycle.md) | The server-side lifecycle. |
