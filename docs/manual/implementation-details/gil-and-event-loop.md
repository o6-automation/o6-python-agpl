# GIL and event-loop bridging

o6\\Python connects open62541 to an asyncio event loop. The loop runs on an SDK
worker thread or on a thread of your application. This page tells you how the
binding keeps native client and server state on the thread of that loop. It
also tells you how the binding uses the open62541 event-loop mutex and the
CPython GIL together when more than one thread uses the same client or server.

!!! info "Prerequisites"
    The user-facing pages [Server / Lifecycle & configuration][server-lifecycle]
    and [Client / Lifecycle](../client/lifecycle.md) describe the public
    event-loop model. This page describes the mechanism behind it.

[server-lifecycle]: ../server/lifecycle.md

## The loop thread

The loop thread runs the I/O and the callbacks. In a synchronous script, it is
usually an SDK worker. In an async application, it is usually the thread that
runs `asyncio.run()`. A loop that you supply can also run on a different thread
of your application. For the selection rules, see the
[client](../client/lifecycle.md#event-loops-and-integration) and the
[server](../server/lifecycle.md#event-loops-and-integration) lifecycle pages.

## Loop-thread affinity

The binding obeys one rule:

**Only the loop thread touches native client and server state and the asyncio
loop. Any thread can touch them while no thread runs the loop.**

The binding does not store the identity of the loop thread. It does the check
again for each call: the caller is on the loop thread when
`asyncio._get_running_loop()` returns the loop of the object. A running loop
belongs to one thread only. Thus the check stays correct when an application
runs the same loop from different threads at different times.

Two layers enforce the rule:

| Layer | Mechanism |
|---|---|
| Python | The public API sends each native call to the loop thread. You can use it from any thread. |
| C | Each native entry point examines the caller. If the loop runs and the caller is on a different thread, it raises `RuntimeError`. C never sends calls to a different thread. |

The C layer is a guard behind the Python layer. Correct code that uses the
public API does not get its error.

### Python marshalling

The public `Client` and `Server` methods give each operation to an internal
helper, `o6.util._run_on_loop`. They give the operation as a callable and do
not call it first. The helper then runs the operation on the correct thread:

| Situation (checked in this order) | Behaviour |
|---|---|
| The caller runs on the loop of the object. | The operation runs inline. A raw `service*` method returns its future, and the request is already sent. |
| The o6 worker for the loop has stopped. | `RuntimeError`: the event loop is not running. |
| The loop runs on a different thread, or the o6 worker starts it. | The operation runs on the loop thread. A synchronous caller waits for the result. An async task on a different loop awaits the result on its own loop. |
| The loop is idle, and the caller runs a different loop. | The operation runs inline and returns an awaitable to the caller. |
| The loop is idle, and the caller runs no loop. | The operation runs inline. The caller runs the loop until the operation is complete. |

**Idle loop from several threads.** While the loop is idle, the calls of
different threads run inline, and each may run the loop. An asyncio loop is not
thread-safe. Thus one thread at a time holds the idle loop, and the calls of
the other threads wait:

- The objects that share a loop share it. A server has a loop of its own,
  unless you gave it one or created it while a loop ran. Thus a synchronous
  callback must not wait for a different thread that calls any object on the
  same idle loop.
- A synchronous callback that calls the same object again runs on the thread
  that holds the loop. It does not wait.
- A thread that holds the idle loop and runs it, for example for a coroutine
  Method, can wait for a different thread that calls the same object, for
  example with `await asyncio.to_thread(...)`. That thread does not wait for
  the loop. It gives its call to the running loop, and runs the loop itself if
  the first thread stops first. An async task on a different loop gets an
  awaitable for this, as usual. While the holder does not run the loop, an
  async task waits on its own loop thread, so a synchronous callback must not
  wait for that loop.
- `Server.start()` waits for the thread that holds the idle loop. The calls
  after it run on the new worker thread. Do not call `start()` from a thread
  that the holder waits for.
- A thread that holds the registration lock does not wait for the idle loop.
  It raises `RuntimeError` when a different thread holds the loop.
- A thread takes the idle loop of an object before the native locks of the
  object. A synchronous callback that calls an object on a different idle loop
  takes that loop next. Do not let the callbacks of two objects call each
  other from two threads. The native locks of the two objects already make
  these threads wait for each other forever.

Some synchronous native reads and writes must give a value to the caller, for
example `client.state` and the `Session` methods. They use a second helper,
`o6.util._call_native`:

- On the loop thread, or while no thread runs the loop, it runs the call
  inline. On an idle loop it holds the loop, as `_run_on_loop` does.
- In all other cases, the loop thread runs the call. The caller waits for the
  result, also when the caller is an async task on a different loop.

`client.config` and `server.config` are views. Each read, write and method call
on them goes through `_call_native`. Thus you can read a live configuration from
any thread. A write raises `RuntimeError` while the client is connected or the
server is running.

`Server.stop()` also goes through `_call_native` when you call it from a
different thread while an application-owned loop runs. The server then shuts
down on the loop thread, and `stop()` returns when the shutdown is complete.

A client that owns its loop starts its worker thread with the first operation
that needs the loop. It does not start the worker in `Client(...)`. Thus the
configuration that you do before `connect()` runs inline on the calling thread.

**When the loop stops.** A synchronous caller that waits for a marshalled call
makes sure that a thread still runs the loop:

- If the o6 worker stops or the loop closes before the call starts, the caller
  raises `RuntimeError`. The call then never runs, also if the worker starts
  again later.
- If the call has started, the caller waits for it. This is also true when the
  loop then stops permanently. Thus an async operation that waits at an `await`
  that never completes keeps its caller waiting.
- `disconnect()` closes the session before it stops the worker. This causes
  open service requests to fail. Thus a call that waits for a service response
  completes first.
- A caller that waits on an idle application-owned loop waits until the
  application runs the loop again.

**Blocking the loop thread.** The loop thread must be free to run a marshalled
call. Do not let the loop thread wait for a different thread that calls the
client or server, for example with `Thread.join()` or `Future.result()`. If it
does, the two threads wait for each other forever.

### The native guard

Each native entry point of `Client`, `Server`, their configuration objects and
the server nodes starts with a guard. The guard raises
`RuntimeError("o6 native call from a thread other than the event-loop thread")`
when these two conditions are true:

- the caller is not on the loop thread;
- the loop runs.

While the loop is idle, the guard lets the call continue. This is the case
before the first start and after a stop.

Configuration writes examine the client or server lifecycle before the guard.
Thus a write to a live configuration gives the lifecycle error, on all threads.

Some entry points do not touch native state, for example `Server.running` and
the configuration getters. These entry points have no guard. A lint test lists
each of these exemptions with its reason. The test fails for all other entry
points that have no guard.

Callbacks from the loop run on the loop thread, so the guard lets them
continue. Usually, application code gets the guard error only when it calls a
private native method directly from a different thread.

Debug builds have one more check. `AsyncIOLoop_lock` stops the process when a
thread other than the loop thread takes the lock while the loop runs. This
check is off during interpreter finalization and loop teardown. If it stops the
process, a native entry point has no guard.

## The two locks

Native code and Python code use two locks:

| Lock | Owner | Purpose |
| --- | --- | --- |
| `elMutex` | open62541 | Recursive mutex. open62541 takes it through `lockServer` and `lockClient` to protect its client and server state. o6 also takes it to start, stop and free the event loop, to open TCP connections, and to start and stop the TCP connection manager. |
| GIL | CPython | Non-recursive lock that protects the interpreter. A thread must hold it to touch Python objects. CPython releases it around `syscall`s. |

The asyncio loop does **not** hold `elMutex` while it dispatches. Timers,
delayed callbacks and socket callbacks run without it. The open62541 code in
these callbacks takes `elMutex` for its own parts only. The GIL and loop-thread
affinity protect the internal data of the event loop: its timers, delayed
callbacks and connections. This will change with the planned support for
free-threaded Python. That support will run dispatch under `elMutex`.

## The deadlock

The loop thread can hold `elMutex` while it waits for the GIL. An example is a
request that `AsyncIOTCP_sendWithConnection` sends from inside an open62541
section:

1. The loop thread holds `elMutex`, because open62541 took it around the send
   operation.
2. The loop thread calls `write()` on the asyncio transport. The transport
   releases the GIL around the system call `send()`.
3. A different thread gets the GIL and runs Python code. If this thread then
   tried to get `elMutex`, it would hold the GIL and wait for `elMutex`.
4. `send()` returns. The loop thread waits to get the GIL again.

| Thread | Holds | Needs |
| --- | --- | --- |
| Loop thread | `elMutex` | GIL (to complete its callback) |
| Calling thread | GIL | `elMutex` |

Each thread waits for the lock that the other thread holds. The scheduler cannot
stop this cycle, because the loop thread waits for the GIL, not in
`pthread_cond_wait`.

Loop-thread affinity prevents step 3. While the loop runs, no other thread gets
to native code that takes `elMutex`. The lock-order rule that follows is a
second protection.

## The lock-order rule

open62541 calls `AsyncIOLoop_lock` through `lockServer` and `lockClient`. This
function releases the GIL before it waits for `elMutex`, and gets the GIL again
after it has the mutex:

```c
static void
AsyncIOLoop_lock(AsyncIOLoop *public_el) {
#ifdef UA_DEBUG
    AsyncIOLoop_assertLoopThread(public_el);
#endif
    Py_BEGIN_ALLOW_THREADS
    UA_LOCK(&((AsyncIOLoop*)public_el)->elMutex);
    Py_END_ALLOW_THREADS
}
```

`AsyncIOLoop_unlock` does not release the GIL. It only releases a mutex that the
calling thread holds.

## Why the rule is safe

1. **The critical window touches no Python state.** Between
   `Py_BEGIN_ALLOW_THREADS` and `Py_END_ALLOW_THREADS`, the only operation is
   `pthread_mutex_lock`.
2. **The lock order is always the same.** A thread that waits for `elMutex` in
   `AsyncIOLoop_lock` does not hold the GIL. A thread that holds `elMutex` can
   wait for the GIL. These two orders cannot make a cycle.
3. **The direct `UA_LOCK` calls are safe because of affinity.** Some o6
   functions take `elMutex` and keep the GIL: event-loop start, stop and free,
   TCP connection open, and TCP connection-manager start and stop. Only the loop
   thread calls them, or a thread calls them while no thread runs the loop.
   Thus no other thread can hold `elMutex` and wait for the GIL at that time.
4. **The rule does not depend on timing.** It does not use `pthread_cond_wait`
   timeouts, `try-lock` fallbacks or the kernel scheduler.

## Finalizers

When you drop the last reference to a `Client` or `Server`, the dropping thread
never waits. This is true for all threads, also for the loop thread in a
callback.

- **While a thread runs the loop,** `__del__` schedules the teardown on the
  loop and returns. The scheduled callback keeps the object alive until it runs.
  It runs at top level, in a later loop iteration:
    - A running server shuts down in the same way as `stop()`. It serves
      `config.shutdownDelay` and then releases its native resources.
    - A connected client closes its channel natively and waits for a maximum of
      one second. Then it releases its native resources.
    - If o6 owns the worker, the worker stops and closes the loop that it made.
- **While no thread runs the loop,** or after the loop is closed, `__del__` does
  the teardown inline.
- **If the loop stops and closes before the scheduled teardown runs,** the
  teardown runs inline when Python releases the callback. An example is an async
  script whose `main()` ends while a local variable holds a live client or
  server.

A live object also gives a `ResourceWarning`, for example
`ResourceWarning("unclosed Client 'client1'")` or
`ResourceWarning("unclosed Server 'server0'")`. A client is live while it is
connected or connecting. A server is live while it runs. An idle object gives no
warning. Python shows `ResourceWarning`s only when warnings are on, for example
with `python -X dev` or `-W default`.

The teardown starts one loop iteration after the drop. The sockets close when
the teardown is complete. A subclass that overrides `__del__` and does not call
`super().__del__()` does not get this behaviour.

## The registration lock

All clients and servers share process-wide tables of namespaces and DataTypes.
One re-entrant lock, the registration lock, lets only one thread at a time
change these tables. It protects:

- namespace registration (`o6.ns.register`, `o6.ns.namespace` and the
  initialization of generated namespace packages), including the native call;
- each native DataType registration;
- the load of server DataTypes into a client at runtime, including their
  application to the decoder of the client. This load runs in tasks on the loop
  thread of the client.

The lock does not protect the load of a packaged namespace module. The import
system loads these modules. Its per-module locks make other threads wait for a
load that is in progress, and let the loading thread enter again.

The registration lock is a leaf lock. Code that holds it obeys three rules:

- **It never imports.** The import system holds the lock of a module while the
  module body registers types. Thus an import under the registration lock can
  cause a deadlock.
- **It never sends calls to an event loop, and never waits for one.** Loop
  threads take the lock when they load DataTypes. Thus `_run_on_loop` raises
  `RuntimeError` instead of marshalling while the caller holds the lock.
- **The notification path never takes it.** The notification decoder runs under
  the native client lock. Reads do not use the lock.

Native DataType registration builds each type in a local copy. It puts the copy
into the shared table only after all Python calls have returned. Thus no other
thread can see an incomplete entry.

## Symptoms when the rules are broken

A lock-order error has these symptoms:

- two threads that are not in an error state;
- one thread that waits permanently in `pthread_mutex_lock`;
- one thread that waits permanently in `PyGILState_Ensure` (or the
  GIL-equivalent `eval_breaker` timeout);
- no CPU use, no progress, no exception, and no log line after the last
  successful operation.

Send `kill -3` to the process to see both threads in this state. A timeout on
one of the two sides does not repair the problem. Each open62541 path that
takes `elMutex` off the loop must go through `AsyncIOLoop_lock`. Each direct
`UA_LOCK` call must stay behind loop-thread affinity.

A blocked loop thread, as described in
[Blocking the loop thread](#python-marshalling), has different symptoms. The
loop thread waits in Python for a different thread. That thread waits on a
`concurrent.futures.Future` for the loop.

## Related topics

| Topic | What it covers |
|---|---|
| [Memory management](memory-management.md) | The Python-side ownership rules for the event-loop thread. |
| [Client / Lifecycle](../client/lifecycle.md) | The public side of the loop, including `connect` and `disconnect`. |
| [Server / Lifecycle & configuration](../server/lifecycle.md) | The server-side lifecycle. |
