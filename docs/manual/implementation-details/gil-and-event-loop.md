# GIL and event-loop bridging

o6\\Python runs an open62541 server and an asyncio event loop on a
background thread. The two threads have to coordinate. This page
describes the coordination: the recursive mutex open62541 uses to
protect its event-loop state, the GIL CPython uses to protect the
interpreter, and the rule the binding enforces to keep them from
deadlocking.

!!! info "Prerequisites"
    The user-facing pages [Server / Lifecycle & configuration][server-lifecycle]
    and [Client / Lifecycle](../client/lifecycle.md) describe the public
    event-loop model. The rest of this page assumes that surface and
    explains the C-level mechanism that makes it work.

[server-lifecycle]: ../server/lifecycle.md

## The two locks

o6\\Python maintains one open62541 event loop per `Client` or `Server`
that needs one. The loop runs on a private daemon thread that the
binding owns. The Python-facing object lives on the user's thread.

The binding therefore has two locks to consider:

| Lock | Owner | Purpose |
| --- | --- | --- |
| `elMutex` | open62541 | Recursive mutex that protects every piece of `UA_EventLoop` state, including the linked list of event sources, the clock, and the timing wheel. |
| GIL | CPython | Non-recursive lock that protects the interpreter. Held by any thread that touches Python objects. Released around `syscall`s. |

Both threads need both locks at different moments. The worker thread
calls into Python (to dispatch a callback, to retire a subscription,
to convert a value) and the main thread calls into open62541
(synchronous admin operations, lifecycle calls, the destroy sequence).

## The deadlock

The deadlock is a classic ABBA. It surfaces in `AsyncIOTCP_sendWithConnection`,
the path that sends a request from the worker's event loop:

1. The worker thread holds `elMutex` — open62541 took it when the loop
   was entered.
2. The worker thread calls into Python's `sock_sendall`, which calls
   `sock_send`, which releases the GIL around the underlying `send()`.
3. The main thread, no longer blocked by the GIL, runs user code. It
   reaches a path that needs to acquire `elMutex` — for example
   `client.state` → `lockClient`, or any synchronous `*_admin` call.
4. The main thread now holds the GIL and is waiting for `elMutex`.
5. The worker's `send()` returns. The GIL is reacquired by the worker
   *after* it returns. The worker is now waiting for the GIL.

| Thread | Holds | Needs |
| --- | --- | --- |
| Worker | `elMutex` | GIL (to finish its callback) |
| Main | GIL | `elMutex` |

Both threads wait for the lock the other holds. There is no scheduler
intervention that breaks the cycle — the daemon thread is not blocked
on `pthread_cond_wait`, it is blocked on the GIL.

The conditions that trigger the cycle are:

- a `client` or `server` operation runs on the main thread that takes
  `elMutex`;
- the worker thread is running a TCP send that releases the GIL for
  the duration of the `send()` syscall.

In practice the cycle only ever materializes on the `lock` side of the
recursive mutex. The other side, `AsyncIOLoop_unlock`, is called by the
worker thread that already owns `elMutex`; recursive acquisition does
not block.

## The rule

The binding breaks the cycle by *not* holding the GIL while it waits
for `elMutex`. The single `AsyncIOLoop_lock` function in
[`src/eventloop/eventloop.c`][src-eventloop] is the only place that
crosses the boundary, and it releases the GIL around the `UA_LOCK`
acquisition:

```c
static void
AsyncIOLoop_lock(AsyncIOLoop *public_el) {
    Py_BEGIN_ALLOW_THREADS
    UA_LOCK(&((AsyncIOLoop*)public_el)->elMutex);
    Py_END_ALLOW_THREADS
}
```

The matching `AsyncIOLoop_unlock` does *not* release the GIL. It is
only called by the worker thread that already owns `elMutex`; the
recursive case is a no-op and the non-recursive case is the worker's
own re-entry, in which case the GIL is already held by the same thread.

## Why the rule is safe

1. **`AsyncIOLoop_lock` is the only contention point.** Every other
   `UA_LOCK` / `UA_UNLOCK` on `elMutex` in the binding runs on the
   worker thread that already owns it. Lock acquisition there is
   recursive and instantaneous, so releasing the GIL would be
   unnecessary and would not be done.
2. **The critical window holds no Python state.** Between
   `Py_BEGIN_ALLOW_THREADS` and `Py_END_ALLOW_THREADS` the only
   operation is `pthread_mutex_lock`. Nothing the worker thread can
   do affects the main thread's view of the Python interpreter state
   during that window.
3. **The lock order is now consistent.** The effective order is
   always `elMutex` first, GIL second. The worker thread takes
   `elMutex` when it enters the loop and acquires the GIL on its
   first call into Python; the main thread takes the GIL the moment
   it begins executing user code and takes `elMutex` only after
   releasing the GIL via `AsyncIOLoop_lock`. The two orders do not
   form a cycle.
4. **No scheduler trick.** The fix does not rely on `pthread_cond_wait`
   timeouts, on `try-lock` fallbacks, or on the kernel scheduler
   breaking the tie. The cycle is broken by lock-order discipline, not
   by chance.

## Where the rule applies

The recursive `elMutex` is the only lock the binding holds while
*waiting* for a worker thread. The same discipline applies to
synchronous lifecycle calls — `Client.connect`, `Client.disconnect`,
`Server.start`, `Server.stop` — and to the `Client.state` getter, which
is the application-level path that originally surfaced the bug.

Other places in the binding use `UA_LOCK` while the calling thread
already owns the lock (recursive). They do not need the GIL release
and do not have it. The discipline is asymmetric by design: acquire
`elMutex` without the GIL, release it without changing the GIL.

## Symptoms when the rule is broken

A violation of the rule is hard to mistake once it manifests. The
diagnostic signature is:

- two healthy threads;
- one thread permanently parked on `pthread_mutex_lock`;
- the other thread permanently parked on `PyGILState_Ensure` (or the
  GIL-equivalent `eval_breaker` timeout);
- zero CPU, zero progress, no exception, no log line beyond the
  last successful operation.

A `kill -3` on the process shows both threads in the same shape. The
fix is not to add a timeout to either side — it is to enforce the
`AsyncIOLoop_lock` discipline at every new call site that takes
`elMutex`. Adding a new unprotected `UA_LOCK` call, even a
short-lived one, reintroduces the deadlock.

## See also

- [Memory management](memory-management.md) — the
  Python-side ownership rules that the event-loop thread lives within.
- [Client / Lifecycle](../client/lifecycle.md) — the public-driven
  side of the loop, including `connect` and `disconnect`.
- [Server / Lifecycle & configuration](../server/lifecycle.md) — the
  matching server-side lifecycle.

[src-eventloop]: https://github.com/o6-automation/o6-python/blob/main/src/eventloop/eventloop.c
