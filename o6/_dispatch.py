# Copyright 2026 (c) o6 Automation GmbH
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

"""Public result shaping and synchronous callback boundaries."""

import asyncio
from contextvars import ContextVar
from functools import wraps
import inspect
import weakref
from typing import Any, Callable, ParamSpec, TypeVar, cast

_P = ParamSpec("_P")
_R = TypeVar("_R")
_sync_task: ContextVar[weakref.ReferenceType[asyncio.Task[Any]] | None] = ContextVar(
    "o6_sync_task", default=None
)


def _current_task() -> asyncio.Task[Any] | None:
    try:
        return asyncio.current_task()
    except RuntimeError:
        return None


def async_caller() -> bool:
    task = _current_task()
    # A newly scheduled task inherits context variables, but not the caller's
    # synchronous callback contract.
    owner = _sync_task.get()
    return task is not None and (owner is None or task is not owner())


def invoke_sync(callback: Callable[..., _R], args: tuple, kwargs: dict | None = None) -> _R:
    """Invoke a callback or initializer without changing pending-work behavior."""
    task = _current_task()
    token = _sync_task.set(weakref.ref(task) if task is not None else None)
    try:
        return callback(*args, **(kwargs or {}))
    finally:
        _sync_task.reset(token)


def synchronous(callback: Callable[_P, _R]) -> Callable[_P, _R]:
    if not callable(callback):
        raise TypeError("callback must be callable")

    @wraps(callback)
    def invoke(*args: _P.args, **kwargs: _P.kwargs) -> _R:
        return invoke_sync(callback, args, kwargs)

    return invoke


def public_result(operation: Callable[_P, _R]) -> Callable[_P, _R]:
    """Keep native work immediate while making async public results awaitable.

    Apply only to operations whose declared return type already allows an
    awaitable. Internal calls within the operation retain immediate results.
    """

    @wraps(operation)
    def invoke(*args: _P.args, **kwargs: _P.kwargs) -> _R:
        if not async_caller():
            return operation(*args, **kwargs)
        loop = asyncio.get_running_loop()
        try:
            result = invoke_sync(operation, args, kwargs)
        except Exception as exc:
            failed = loop.create_future()
            failed.set_exception(exc)
            return cast(_R, failed)
        if inspect.isawaitable(result):
            return result
        completed = loop.create_future()
        completed.set_result(result)
        return cast(_R, completed)

    return invoke
