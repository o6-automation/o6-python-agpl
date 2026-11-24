# Copyright 2026 (c) o6 Automation GmbH (Author: Andreas Ebner)
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

"""Public utilities and shared helpers for the high-level API.

Includes certificate generation and helpers for loading certificate material.
"""

from __future__ import annotations

import asyncio as _asyncio
from collections.abc import Awaitable as _Awaitable
from collections.abc import Callable as _Callable
from collections.abc import Iterable as _Iterable
import concurrent.futures as _concurrent_futures
from datetime import datetime as _datetime
import enum as _enum
import inspect as _inspect
from pathlib import Path as _Path
import threading as _threading
import warnings as _warnings
from typing import Any as _Any
import weakref as _weakref

import numpy as _np

import o6 as _o6_api

from . import _o6
from ._dispatch import invoke_sync as _invoke_sync
from ._registration_lock import registration_lock_held as _registration_lock_held

_create_certificate = _o6.create_certificate
del _o6


def createSelfSignedCertificate(
    *,
    appUri: str = "urn:o6-Python.unconfigured.application",
    commonName: str = "o6 Python@localhost",
    organization: str = "o6",
    country: str = "DE",
    altNames: list[str] | None = None,
    expiresInDays: int = 365,
    keySize: int = 2048,
    fmt: str = "DER",
    validFrom: _datetime | None = None,
) -> tuple[bytes, bytes]:
    """Create a self-signed certificate and private key.

    `DNS:localhost` and `URI:<appUri>` are always included as subject
    alternative names.

    Args:
        appUri: Application URI embedded as a subject alternative name.
            The default is the ApplicationUri of a server or client that sets
            none.
        commonName: Certificate subject common name, 1 to 64 characters.
        organization: Certificate subject organization, 1 to 64 characters.
        country: Two-letter certificate subject country code.
        altNames: Additional subject alternative names, such as
            `["DNS:myhost"]`.
        expiresInDays: Certificate validity in days, counted from
            `validFrom`.
        keySize: RSA key size in bits.
        fmt: Output format, either `"DER"` or `"PEM"`.
        validFrom: Start of the validity period. The default is the creation
            time. An earlier start, such as an hour ago, lets peers whose
            clocks run behind accept the certificate. A naive `datetime` is
            read as local time.

    Returns:
        A `(privateKey, certificate)` pair as raw bytes.

    Raises:
        ValueError: `commonName` or `organization` is empty or longer than
            the X.509 limit of 64 characters, or `country` does not have two
            characters.
    """
    # The native call reports a subject it cannot encode only as
    # Bad_InternalError. X.509 upper bounds: RFC 5280, Appendix A.
    for field, value in (("commonName", commonName), ("organization", organization)):
        if not 1 <= len(value) <= 64:
            raise ValueError(f"{field} must have 1 to 64 characters, not {len(value)}: {value!r}")
    if len(country) != 2:
        raise ValueError(f"country must be a two-letter code, not {country!r}")
    subject = [f"C={country}", f"O={organization}", f"CN={commonName}"]

    san: list[str] = [f"DNS:localhost", f"URI:{appUri}"]
    if altNames:
        for entry in altNames:
            if entry not in san:
                san.append(entry)

    return _create_certificate(
        subject,
        san,
        expires_in_days=expiresInDays,
        key_size=keySize,
        fmt=fmt,
        valid_from=None if validFrom is None else int(_o6_api.DateTime(validFrom)),
    )


def loadCertificate(path: str | _Path) -> bytes:
    """Load a DER- or PEM-encoded certificate from `path`.

    Returns the file's bytes unchanged. `Client.config` and the `Server`
    constructor also accept a path directly.

    Args:
        path: File to read.

    Returns:
        The raw certificate bytes.

    Raises:
        OSError: The file cannot be read.
    """
    return _Path(path).read_bytes()


def loadPrivateKey(path: str | _Path) -> bytes:
    """Load a DER- or PEM-encoded private key from `path`.

    Returns the file's bytes unchanged.

    Args:
        path: File to read.

    Returns:
        The raw private-key bytes.

    Raises:
        OSError: The file cannot be read.
    """
    return _Path(path).read_bytes()


def _load_cert_or_bytes(value: str | _Path | bytes | None) -> bytes | None:
    """Return certificate bytes from a path or an existing byte string."""
    if value is None:
        return None
    if isinstance(value, bytes):
        return value
    return _Path(value).read_bytes()


def _load_cert_list(values: list[str | _Path | bytes] | None) -> list[bytes]:
    """Load certificate bytes from a list of paths and byte strings."""
    if not values:
        return []
    return [b for v in values if (b := _load_cert_or_bytes(v)) is not None]


def _index_range_to_string(value: _o6_api.IndexRange) -> str | None:
    """Convert a public index range to OPC UA's inclusive string syntax."""
    if value is None:
        return None
    if isinstance(value, str):
        return value
    if isinstance(value, slice):
        value = (value,)
    if not isinstance(value, tuple) or not value:
        raise TypeError("index range must be a string or a non-empty tuple of slices")
    dimensions: list[str] = []
    for dimension in value:
        if not isinstance(dimension, slice):
            raise TypeError("index range tuple entries must be slices")
        if dimension.start is None or dimension.stop is None:
            raise ValueError("index range slices must have explicit start and stop values")
        if dimension.step is not None:
            raise ValueError("index range slices do not support a step")
        if dimension.start < 0 or dimension.stop <= dimension.start:
            raise ValueError("index range slices must describe a non-empty, non-negative range")
        inclusive_stop = dimension.stop - 1
        if inclusive_stop == dimension.start:
            dimensions.append(str(dimension.start))
        else:
            dimensions.append(f"{dimension.start}:{inclusive_stop}")
    return ",".join(dimensions)


class _WorkerLoop:
    """Background thread driving an asyncio event loop."""

    def __init__(self, loop: _asyncio.AbstractEventLoop) -> None:
        """Wrap an existing event loop with a worker-thread driver."""
        self._loop = loop
        self._thread: _threading.Thread | None = None
        self._close_on_exit = False

    @property
    def loop(self) -> _asyncio.AbstractEventLoop:
        """Return the asyncio event loop driven by this worker."""
        return self._loop

    @property
    def running(self) -> bool:
        """Return whether the worker thread is currently alive."""
        return self._thread is not None and self._thread.is_alive()

    @property
    def on_loop_thread(self) -> bool:
        """Return whether this code is running on the worker thread."""
        return self._thread is not None and _threading.current_thread() is self._thread

    def start(self) -> None:
        """Start the worker thread unless it is already running."""
        if self.running:
            return
        loop = self._loop

        def worker() -> None:
            _asyncio.set_event_loop(loop)
            loop.run_forever()
            if self._close_on_exit and not loop.is_closed():
                try:
                    loop.close()
                except Exception:
                    pass

        self._thread = _threading.Thread(target=worker, daemon=True)
        self._thread.start()

    def stop(self, timeout: float = 2.0) -> None:
        """Stop the loop and join its thread; the loop stays open."""
        thread = self._thread
        self._thread = None
        if thread is not None and thread.is_alive():
            try:
                self._loop.call_soon_threadsafe(self._loop.stop)
            except RuntimeError:
                pass
            if _threading.current_thread() is not thread:
                thread.join(timeout=timeout)

    def retire(self, close: bool) -> None:
        """Stop the loop from its own thread, which then optionally closes it.

        Unlike `stop`, this never joins, so it is safe in loop callbacks.
        """
        self._close_on_exit = close
        self._thread = None
        self._loop.stop()


class _ScheduledFinalizer:
    """A teardown step that falls back to inline cleanup if dropped unrun.

    `_finalize_native` schedules one as the loop callback, and the finalize
    tasks hold one so that a task that never runs still releases. A loop that
    stops and closes before running it drops it unrun; it then tears down
    inline, because no thread runs the loop any more. Without that, the object
    would reach the native deallocator only after garbage collection has
    cleared its Python state.
    """

    __slots__ = ("_loop", "_finalize", "_cleanup")

    def __init__(
        self,
        loop: _asyncio.AbstractEventLoop,
        finalize: _Callable[[], None],
        cleanup: _Callable[[], None],
    ) -> None:
        self._loop: _asyncio.AbstractEventLoop | None = loop
        self._finalize = finalize
        self._cleanup = cleanup

    def __call__(self) -> None:
        if self._loop is None:
            return  # one-shot: already run or disarmed
        self._loop = None
        self._finalize()

    def disarm(self) -> None:
        """Skip the inline teardown when this is dropped unrun."""
        self._loop = None

    def __del__(self) -> None:
        if self._loop is not None and not self._loop.is_running():
            self._cleanup()


def _finalize_native(
    owner: _Any,
    loop: _asyncio.AbstractEventLoop,
    worker: _WorkerLoop | None,
    *,
    live: _Callable[[], bool],
    finalize: _Callable[[], None],
    cleanup: _Callable[[], None],
) -> None:
    """Release a native client or server from `__del__` without blocking.

    While `loop` or `worker` runs, `finalize` is scheduled on the loop and
    tears down there, at top level, on a later iteration; this applies on the
    loop thread too. The scheduled bound method keeps `owner` alive until
    then. Otherwise, or when the loop is already closed, `cleanup` tears down
    inline. The teardown happens even if `live` raises, which then propagates.

    Emits `ResourceWarning` for a live owner, after the teardown is scheduled
    or done.

    Args:
        owner: The client or server being finalized.
        loop: Its event loop.
        worker: The worker thread o6 runs `loop` on, if any.
        live: Whether the owner is connected, connecting, running or starting.
        finalize: Teardown to run on the loop thread.
        cleanup: Teardown to run inline when no thread runs the loop.
    """
    is_live = False
    try:
        is_live = live()
    finally:
        if loop.is_running() or (worker is not None and worker.running):
            scheduled = _ScheduledFinalizer(loop, finalize, cleanup)
            try:
                loop.call_soon_threadsafe(scheduled)
            except RuntimeError:
                # asyncio refuses only once the loop is closed, and no thread
                # runs a closed loop, whatever its worker thread still does
                scheduled.disarm()
                cleanup()
        else:
            cleanup()
    if is_live:
        label = f"{type(owner).__name__} {getattr(owner, '_name', '?')!r}"
        _warnings.warn(f"unclosed {label}", ResourceWarning, source=owner)


# Seconds between checks, while a caller blocks on a marshalled call, that a
# thread still runs the loop, and while it waits for an idle loop, that the
# thread using the loop has started to run it.
_LOOP_ALIVE_POLL = 0.1


class _IdleLoop:
    """The hold on an event loop that calls use inline while no thread runs it.

    Calls on an idle loop run on the caller's thread: they create futures and
    tasks on the loop and may run it with `run_until_complete`. asyncio loops
    are not thread-safe, so only the holder of `lock` does either. Objects that
    share a loop share its hold. `lock` is reentrant, because a synchronous
    node callback that calls the same object runs on the holder's thread.

    The holder takes `lock` before the native locks of the objects on the
    loop. A callback that calls an object on another idle loop takes that
    loop's lock and then its native locks, so the locks nest in the same order
    as the native locks alone and add no deadlock.
    """

    __slots__ = ("lock", "running", "__weakref__")

    def __init__(self) -> None:
        self.lock = _threading.RLock()
        # Whether the holder runs the loop now; read by threads without `lock`.
        self.running = False

    def run(self, loop: _asyncio.AbstractEventLoop, awaitable: _Awaitable[_Any]) -> _Any:
        """Run `loop` until `awaitable` completes; the caller holds `lock`."""
        self.running = True
        try:
            return loop.run_until_complete(_awaited(awaitable))
        finally:
            self.running = False


_idle_loops: _weakref.WeakKeyDictionary[_asyncio.AbstractEventLoop, _IdleLoop] = (
    _weakref.WeakKeyDictionary()
)
_idle_loops_guard = _threading.Lock()


def _idle_loop(loop: _asyncio.AbstractEventLoop) -> _IdleLoop:
    """Return the hold on `loop` for inline use while no thread runs it."""
    with _idle_loops_guard:
        idle = _idle_loops.get(loop)
        if idle is None:
            idle = _idle_loops[loop] = _IdleLoop()
        return idle


def _take_idle_loop(idle: _IdleLoop, owner: str) -> bool:
    """Acquire `idle.lock`, or return `False` once its holder runs the loop.

    The holder may then wait for the caller, for example in a coroutine
    callback that awaits a thread calling the same object, so the caller must
    not wait for the lock.

    Raises:
        RuntimeError: Another thread holds the lock while the caller holds the
            registration lock, which must not wait for an event loop.
    """
    while not idle.lock.acquire(blocking=False):
        if idle.running:
            return False
        if _registration_lock_held():
            raise RuntimeError(
                f"{owner}: cannot wait for the event loop while holding the registration lock"
            )
        if idle.lock.acquire(timeout=_LOOP_ALIVE_POLL):
            return True
    return True


def _run_on_loop(
    loop: _asyncio.AbstractEventLoop,
    worker: _Callable[[], _WorkerLoop | None],
    fn: _Callable[[], _Any],
    *,
    sync_result: bool = False,
    wait: bool = False,
    owner: str = "o6",
) -> _Any:
    """Run `fn` on the thread of `loop`, or inline while no thread runs it.

    `fn` is evaluated on the loop thread whenever the loop runs, so native
    state behind it is touched only there. Pass the operation uncalled: a
    lambda, a `functools.partial` or an `async def` function. `fn` may return
    a value, a future or a coroutine.

    | Situation, checked in order | Result |
    |---|---|
    | The caller runs on `loop` | `fn()` unchanged |
    | `worker` exists and has stopped | `RuntimeError` |
    | `worker` runs, or `loop` runs on another thread | `fn` runs in a coroutine on `loop`: sync callers (and loop callbacks outside a task) block for the result; tasks on another loop get an awaitable, or block with `wait` |
    | `loop` is idle and the caller runs another loop | `fn()` for the caller to await |
    | `loop` is idle and the caller runs no loop | `fn()`, awaited with `loop.run_until_complete` if awaitable |

    A running worker counts as running `loop` before the loop reaches
    `run_forever`, so calls in that window wait for it. A blocked caller
    raises, and its call never runs, when the worker stops or `loop` closes
    before the call started.

    On an idle loop one thread at a time runs `fn()` and the loop, under
    `_idle_loop`; the others wait. A caller that finds the holder running the
    loop queues `fn` on it instead, and runs the loop itself if the holder
    stops first. A task on another loop gets an awaitable for that wait.

    Args:
        loop: The event loop that owns the native state.
        worker: Returns the worker thread driving `loop` when o6 owns it, else
            `None`. Called again once the caller holds the idle loop, because
            another thread may have started a worker meanwhile.
        fn: Zero-argument callable performing the operation.
        sync_result: On the inline paths, return the result of a future that
            `fn()` returns already done instead of the future.
        wait: Block a task on another loop for the result as well, for call
            sites whose caller needs the value rather than an awaitable.
        owner: Name of the owning object type for error messages.

    Returns:
        The result as described above.

    Raises:
        RuntimeError: The worker has stopped, the loop is closed and the
            operation must be scheduled on it, the worker stopped or the loop
            closed before a blocked caller's operation started, or the caller
            would marshal to another thread or wait for the idle loop while
            holding the registration lock.
    """
    caller = _asyncio._get_running_loop()
    if caller is loop:
        return _done_result(_invoke_sync(fn, ()), sync_result)

    current = worker()
    taken_over = None
    if current is None:
        idle = _idle_loop(loop)
        if _take_idle_loop(idle, owner):
            try:
                current = worker()
                if current is None and not loop.is_running():
                    return _run_inline(loop, idle, fn, caller, sync_result, owner)
            finally:
                idle.lock.release()
        else:
            # Another thread runs the idle loop inline and may stop before it
            # runs `fn`; the wait for the result then takes the loop over.
            taken_over = idle

    if current is not None and not current.running:
        raise RuntimeError(f"{owner} event loop is not running")

    if _registration_lock_held():
        # Loop threads take the lock to load DataTypes; waiting for one could deadlock.
        raise RuntimeError(
            f"{owner}: cannot run on the event loop while holding the registration lock"
        )

    # Decides once whether the loop runs `fn` or a blocked caller gives up:
    # cancelling it fails once the loop has started the call, and vice versa.
    claim: _concurrent_futures.Future[None] = _concurrent_futures.Future()

    async def call() -> _Any:
        if not claim.set_running_or_notify_cancel():
            raise _asyncio.CancelledError()
        result = _invoke_sync(fn, ())
        return await result if _inspect.isawaitable(result) else result

    coro = call()
    try:
        future = _asyncio.run_coroutine_threadsafe(coro, loop)
    except RuntimeError:
        coro.close()
        raise RuntimeError(f"{owner} event loop is not running") from None
    blocks = wait or caller is None or _asyncio.current_task(caller) is None
    if taken_over is not None:
        args = (future, claim, loop, worker, taken_over, owner)
        if blocks:
            return _taken_over_result(*args)
        awaitable = caller.run_in_executor(None, _taken_over_result, *args)  # type: ignore[union-attr]

        def cancel_call(waited: _asyncio.Future[_Any]) -> None:
            # As cancelling a wrapped future would; also ends the wait.
            if waited.cancelled():
                claim.cancel()
                future.cancel()

        awaitable.add_done_callback(cancel_call)
    elif blocks:
        return _marshalled_result(future, claim, loop, current, owner)
    else:
        awaitable = _asyncio.wrap_future(future, loop=caller)
    # Lets a sync caller holding the awaitable block on the result.
    awaitable._concurrent_future = future  # type: ignore[attr-defined]
    return awaitable


def _run_inline(
    loop: _asyncio.AbstractEventLoop,
    idle: _IdleLoop,
    fn: _Callable[[], _Any],
    caller: _asyncio.AbstractEventLoop | None,
    sync_result: bool,
    owner: str,
) -> _Any:
    """Run `fn` on idle `loop` from the caller's thread, which holds `idle.lock`."""
    result = _invoke_sync(fn, ())
    if caller is not None or not _inspect.isawaitable(result):
        return _done_result(result, sync_result)
    if loop.is_closed():
        if _inspect.iscoroutine(result):
            result.close()
        raise RuntimeError(f"{owner} event loop is closed")
    return idle.run(loop, result)


def _marshalled_result(
    future: _concurrent_futures.Future[_Any],
    claim: _concurrent_futures.Future[None],
    loop: _asyncio.AbstractEventLoop,
    worker: _WorkerLoop | None,
    owner: str,
) -> _Any:
    """Block for the result of a call marshalled onto `loop`.

    A call still queued when the o6 worker has stopped, or when `loop` is
    closed, would never run, so the caller raises instead of waiting forever.
    The call then never runs, even if the worker restarts. A call the loop has
    started, and a call on an idle loop the application runs again later, are
    waited for.
    """
    while not future.done():
        _concurrent_futures.wait((future,), timeout=_LOOP_ALIVE_POLL)
        if future.done() or loop.is_running():
            continue
        stopped = loop.is_closed() or (worker is not None and not worker.running)
        if stopped and claim.cancel():
            future.cancel()
            raise RuntimeError(f"{owner} event loop stopped before completing the call")
    return future.result()


def _taken_over_result(
    future: _concurrent_futures.Future[_Any],
    claim: _concurrent_futures.Future[None],
    loop: _asyncio.AbstractEventLoop,
    worker: _Callable[[], _WorkerLoop | None],
    idle: _IdleLoop,
    owner: str,
) -> _Any:
    """Block for a call queued on a loop that another thread runs inline.

    That thread stops running the loop once its own call completes. If the
    loop is then idle and no worker started, the caller takes `idle.lock` and
    runs the loop itself until the call completes. A worker started meanwhile
    runs the call. As in `_marshalled_result`, a call still queued when that
    worker stops or the loop closes never runs, and the caller raises.
    """
    while not future.done():
        _concurrent_futures.wait((future,), timeout=_LOOP_ALIVE_POLL)
        if future.done() or idle.running or loop.is_running():
            continue
        current = worker()
        if current is None and not loop.is_closed():
            if idle.lock.acquire(blocking=False):
                try:
                    if worker() is None and not loop.is_running():
                        return idle.run(loop, _asyncio.wrap_future(future, loop=loop))
                finally:
                    idle.lock.release()
            continue
        stopped = loop.is_closed() or (current is not None and not current.running)
        if stopped and claim.cancel():
            future.cancel()
            raise RuntimeError(f"{owner} event loop stopped before completing the call")
    return future.result()


def _call_native(
    loop: _asyncio.AbstractEventLoop,
    worker: _Callable[[], _WorkerLoop | None],
    fn: _Callable[[], _Any],
    *,
    owner: str = "o6",
) -> _Any:
    """Return `fn()` from any thread, evaluated on the thread of `loop` while one runs it.

    For synchronous native reads and writes whose caller needs the value, such
    as properties. While `loop` or the worker runs on another thread, `fn` runs
    there through `_run_on_loop` and the caller blocks, even a task on another
    loop. Otherwise `fn` runs inline: on the loop thread, and also while
    nothing runs `loop`, including after the worker has stopped, where
    `_run_on_loop` raises. Inline on an idle loop it holds `_idle_loop`, so
    that the native locks of the objects on `loop` keep nesting inside it.

    Args:
        loop: The event loop that owns the native state.
        worker: Returns the worker thread driving `loop` when o6 owns it, else
            `None`.
        fn: Zero-argument callable performing a synchronous operation.
        owner: Name of the owning object type for error messages.

    Returns:
        The result of `fn()`.
    """
    if _asyncio._get_running_loop() is loop:
        return fn()
    current = worker()
    if current is None or not current.running:
        idle = _idle_loop(loop)
        if _take_idle_loop(idle, owner):
            try:
                current = worker()
                if (current is None or not current.running) and not loop.is_running():
                    return fn()
            finally:
                idle.lock.release()
    return _run_on_loop(loop, worker, fn, sync_result=True, wait=True, owner=owner)


class _ConfigView:
    """The configuration of a `Client` or `Server`, usable from any thread.

    Forwards each attribute read, write, deletion and method call to the native
    configuration through the owner's `_call_native`: on the loop thread while a
    thread runs the owner's loop, inline otherwise. The native configuration
    only accepts calls from that thread, and refuses writes while the owner is
    live, so a live configuration stays readable from any thread but cannot be
    changed. `__class__` reports the native type, so `isinstance` checks against
    `ClientConfig` and `ServerConfig` hold.
    """

    __slots__ = ("_owner", "_native")

    def __init__(self, owner: _Any, native: _Any) -> None:
        object.__setattr__(self, "_owner", owner)
        object.__setattr__(self, "_native", native)

    @property  # type: ignore[misc]
    def __class__(self) -> type:  # noqa: D105
        return type(self._native)

    def __getattr__(self, name: str) -> _Any:
        native = self._native
        value = self._owner._call_native(lambda: getattr(native, name))
        if getattr(value, "__self__", None) is native and callable(value):
            # A bound method of the native config: marshal the call as well
            owner = self._owner

            def method(*args: _Any, **kwargs: _Any) -> _Any:
                return owner._call_native(lambda: value(*args, **kwargs))

            method.__name__ = name
            method.__doc__ = value.__doc__
            return method
        return value

    def __setattr__(self, name: str, value: _Any) -> None:
        native = self._native
        self._owner._call_native(lambda: setattr(native, name, value))

    def __delattr__(self, name: str) -> None:
        native = self._native
        self._owner._call_native(lambda: delattr(native, name))

    def __dir__(self) -> list[str]:
        return dir(self._native)

    def __repr__(self) -> str:
        native = self._native
        return self._owner._call_native(lambda: repr(native))


def _done_result(result: _Any, unwrap: bool) -> _Any:
    """Return the result of `result` if it is a done future and `unwrap` is set."""
    if unwrap and _asyncio.isfuture(result) and result.done():
        return result.result()
    return result


async def _awaited(awaitable: _Awaitable[_Any]) -> _Any:
    return await awaitable


def _value_rank(value: _Any) -> int:
    """Infer the ValueRank for Variable creation.

    NumPy arrays keep their dimensions; other iterable values except text,
    bytes and enum members are one-dimensional. Native conversion validates
    the value. Enum members are scalars, although `enum.Flag` members such as
    StatusCodes and OptionSets are iterable.
    """
    if isinstance(value, _np.ndarray):
        return value.ndim
    if isinstance(value, (str, bytes, _enum.Enum)):
        return -1
    if isinstance(value, _Iterable):
        return 1
    return -1


def _empty_sequence_shape(value: _Any) -> tuple[int, ...] | None:
    """Return the shape of a rectangular nested sequence with no elements."""
    if not isinstance(value, (list, tuple)):
        return None
    if not value:
        return (0,)
    shape = _empty_sequence_shape(value[0])
    if shape is not None and all(_empty_sequence_shape(item) == shape for item in value[1:]):
        return (len(value), *shape)
    return None


def _infer_data_type(value: _Any) -> tuple[_o6_api.NodeId, int]:
    """Infer the OPC UA data-type NodeId and value rank for `value`."""
    value_rank = _value_rank(value)

    normalized = _o6_api.DataValue()
    normalized.value = value
    normalized_value = normalized.value
    if isinstance(normalized_value, _np.ndarray) and normalized_value.size == 0:
        element_type = normalized_value.dtype.type
        if normalized_value.dtype.kind == "T":
            element_type = str
        return _o6_api.NodeId(element_type), value_rank
    if value_rank >= 1:
        if isinstance(normalized_value, _np.ndarray):
            normalized_value = normalized_value.flat[0]
        else:
            normalized_value = next(iter(normalized_value))
    return _o6_api.NodeId(type(normalized_value)), value_rank


def _coerce_builtin_value(data_type: _Any, value: _Any) -> _Any:
    """Wrap values in the native scalar type selected by an ns0 DataType."""
    if value is None:
        return None
    nodeid = _o6_api.NodeId(data_type)
    namespace = nodeid.ns if isinstance(nodeid.ns, int) else nodeid.ns.index
    if namespace != 0 or not isinstance(nodeid.id, int) or not 1 <= nodeid.id <= 11:
        return value
    wrapper = (
        _o6_api.Boolean,
        _o6_api.SByte,
        _o6_api.Byte,
        _o6_api.Int16,
        _o6_api.UInt16,
        _o6_api.Int32,
        _o6_api.UInt32,
        _o6_api.Int64,
        _o6_api.UInt64,
        _o6_api.Float,
        _o6_api.Double,
    )[nodeid.id - 1]
    try:
        if isinstance(value, list):
            return [wrapper(item) for item in value]
        if isinstance(value, tuple):
            return tuple(wrapper(item) for item in value)
        return wrapper(value)
    except (TypeError, ValueError) as exc:
        exc.add_note(f"while coercing a value declared with DataType {nodeid}")
        raise


__all__ = ["createSelfSignedCertificate", "loadCertificate", "loadPrivateKey"]


def __dir__() -> list[str]:
    return sorted(__all__)


# ---------------------------------------------------------------------------
