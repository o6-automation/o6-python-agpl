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

"""Application Notifications, shared by `o6.Server` and `o6.Client`.

open62541 raises the same kind of notification on both peers, with the same
type encoding and the same `UA_KeyValueMap` payload shape. Only *which*
categories each peer raises differs — a client never sees a session or audit
notification — so the encoding, the `Notification` value type, and the
handler registry live here once instead of once per peer.
"""

from __future__ import annotations

import asyncio
import enum
import inspect
import logging
import threading
from dataclasses import dataclass, field
from types import MappingProxyType
from typing import TYPE_CHECKING, Any, Callable, Iterator, Mapping

from o6._dispatch import invoke_sync

if TYPE_CHECKING:
    import o6

# The category occupies the high 32 bits of a notification type, the
# sub-event the low 32. Defined in
# `deps/open62541/include/open62541/common.h`.
CATEGORY_MASK = 0xFFFFFFFF00000000

NotificationHandler = Callable[["Notification"], Any]


class NotificationType(enum.IntEnum):
    """open62541 Application Notification type encoding.

    The high 32 bits are the category, the low 32 the sub-event — see
    `deps/open62541/include/open62541/common.h`. These are open62541's own
    values, not part of the OPC UA specification, so
    `test_notification_type_matches_c_extension` in
    `tests/connections/test_server_notifications.py` cross-checks every member
    against the compiled extension's own constants: an upstream encoding
    change fails that test loudly instead of silently diverging here.

    Every member is listed, including the ones only a `Server` ever raises.
    A `Client` observes the `LIFECYCLE_*` and `SERVICE_*` members only.
    """

    LIFECYCLE_STARTED = (0x1 << 32) | 0x01
    LIFECYCLE_SHUTDOWN = (0x1 << 32) | 0x02
    LIFECYCLE_STOPPING = (0x1 << 32) | 0x03
    LIFECYCLE_STOPPED = (0x1 << 32) | 0x04

    SECURECHANNEL_OPENED = (0x2 << 32) | 0x01
    SECURECHANNEL_CLOSED = (0x2 << 32) | 0x02

    SESSION_CREATED = (0x4 << 32) | 0x01
    SESSION_ACTIVATED = (0x4 << 32) | 0x02
    SESSION_DEACTIVATED = (0x4 << 32) | 0x03
    SESSION_CLOSED = (0x4 << 32) | 0x04

    SERVICE_BEGIN = (0x8 << 32) | 0x01
    SERVICE_ASYNC = (0x8 << 32) | 0x02
    SERVICE_END = (0x8 << 32) | 0x03

    SUBSCRIPTION_CREATED = (0x10 << 32) | 0x01
    SUBSCRIPTION_MODIFIED = (0x10 << 32) | 0x02
    SUBSCRIPTION_PUBLISHINGMODE = (0x10 << 32) | 0x03
    SUBSCRIPTION_TRANSFERRED = (0x10 << 32) | 0x04
    SUBSCRIPTION_DELETED = (0x10 << 32) | 0x05

    MONITOREDITEM_CREATED = (0x20 << 32) | 0x01
    MONITOREDITEM_MODIFIED = (0x20 << 32) | 0x02
    MONITOREDITEM_MONITORINGMODE = (0x20 << 32) | 0x03
    MONITOREDITEM_DELETED = (0x20 << 32) | 0x04

    DISCOVERY_REGISTERSERVER = (0x80 << 32) | 0x01
    DISCOVERY_SERVERONNETWORK = (0x80 << 32) | 0x02

    AUDIT = 0x40 << 32
    AUDIT_SECURITY = (0x40 << 32) | (0x01 << 16)
    AUDIT_SECURITY_CHANNEL = (0x40 << 32) | (0x01 << 16) | (0x01 << 8)
    AUDIT_SECURITY_CHANNEL_OPEN = (0x40 << 32) | (0x01 << 16) | (0x01 << 8) | 0x01
    AUDIT_SECURITY_SESSION = (0x40 << 32) | (0x01 << 16) | (0x02 << 8)
    AUDIT_SECURITY_SESSION_CREATE = (0x40 << 32) | (0x01 << 16) | (0x02 << 8) | 0x01
    AUDIT_SECURITY_SESSION_ACTIVATE = (0x40 << 32) | (0x01 << 16) | (0x02 << 8) | 0x02
    AUDIT_SECURITY_SESSION_CANCEL = (0x40 << 32) | (0x01 << 16) | (0x02 << 8) | 0x03
    AUDIT_SECURITY_CERTIFICATE = (0x40 << 32) | (0x01 << 16) | (0x04 << 8)
    AUDIT_SECURITY_CERTIFICATE_DATAMISMATCH = (0x40 << 32) | (0x01 << 16) | (0x04 << 8) | 0x01
    AUDIT_SECURITY_CERTIFICATE_EXPIRED = (0x40 << 32) | (0x01 << 16) | (0x04 << 8) | 0x02
    AUDIT_SECURITY_CERTIFICATE_INVALID = (0x40 << 32) | (0x01 << 16) | (0x04 << 8) | 0x03
    AUDIT_SECURITY_CERTIFICATE_UNTRUSTED = (0x40 << 32) | (0x01 << 16) | (0x04 << 8) | 0x04
    AUDIT_SECURITY_CERTIFICATE_REVOKED = (0x40 << 32) | (0x01 << 16) | (0x04 << 8) | 0x05
    AUDIT_SECURITY_CERTIFICATE_MISMATCH = (0x40 << 32) | (0x01 << 16) | (0x04 << 8) | 0x06
    AUDIT_NODE = (0x40 << 32) | (0x02 << 16)
    AUDIT_NODE_ADD = (0x40 << 32) | (0x02 << 16) | 0x01
    AUDIT_NODE_DELETE = (0x40 << 32) | (0x02 << 16) | 0x02
    AUDIT_NODE_ADDREFERENCES = (0x40 << 32) | (0x02 << 16) | 0x03
    AUDIT_NODE_DELETEREFERENCES = (0x40 << 32) | (0x02 << 16) | 0x04
    AUDIT_UPDATE = (0x40 << 32) | (0x04 << 16)
    AUDIT_UPDATE_WRITE = (0x40 << 32) | (0x04 << 16) | 0x01
    AUDIT_UPDATE_HISTORY = (0x40 << 32) | (0x04 << 16) | 0x02
    AUDIT_UPDATE_METHOD = (0x40 << 32) | (0x04 << 16) | 0x03
    AUDIT_CLIENT = (0x40 << 32) | (0x08 << 16)
    AUDIT_CLIENT_UPDATEMETHOD = (0x40 << 32) | (0x08 << 16) | 0x01

    @property
    def category(self) -> int:
        """The high-32-bit category prefix, e.g. `NotificationType.LIFECYCLE_STARTED.category`."""
        return self.value >> 32

    @property
    def pointName(self) -> str:
        """The lowercased sub-event name, e.g. `"started"`."""
        _, _, sub_event = self.name.partition("_")
        return sub_event.lower()


LIFECYCLE_CATEGORY = NotificationType.LIFECYCLE_STARTED.category
SERVICE_CATEGORY = NotificationType.SERVICE_BEGIN.category
AUDIT_CATEGORY = NotificationType.AUDIT.category
DISCOVERY_CATEGORY = NotificationType.DISCOVERY_REGISTERSERVER.category


def dispatch_key(type: int) -> int:
    """The key a notification's handler registry is stored under.

    Every category except discovery is keyed by its top-32-bit category
    prefix, so several sub-events (e.g. session created/activated/
    deactivated/closed) share one registry. RegisterServer and
    ServerOnNetwork share open62541's DISCOVERY category prefix but have
    disjoint payloads and separate handler properties, so they're keyed by
    their full type value instead.
    """
    prefix = (type & CATEGORY_MASK) >> 32
    if prefix == DISCOVERY_CATEGORY:
        return type
    return prefix


def lifecycle_point(type: int) -> str | None:
    """The lifecycle point name for a lifecycle notification, else `None`."""
    if (type & CATEGORY_MASK) >> 32 != LIFECYCLE_CATEGORY:
        return None
    try:
        return NotificationType(type).pointName
    except ValueError:
        return None


@dataclass(frozen=True)
class Notification:
    """One application notification.

    A `type` identifies both the category (lifecycle, secure channel, session,
    service, subscription, monitored item, discovery, audit) and the specific
    event within that category. For the lifecycle category `type` is one of
    the `NotificationType.LIFECYCLE_*` members.

    Payload keys mirror open62541's `UA_KeyValueMap` entries — string keys
    whose values are converted to Python types (NodeIds as `o6.NodeId`,
    scalars as the matching `o6.*` wrapper, etc.). For audit notifications,
    the keys are event-filter property paths (`"/ActionTimeStamp"`,
    `"/Status"`, ...) — the same convention used for event field data
    elsewhere (e.g. `o6.Event.fields`, a monitored event item's callback).

    Attributes:
        type: The raw open62541 notification type.
        payload: A read-only mapping of `str -> Any` of the notification's
            payload fields.
        lifecycle: For lifecycle notifications only, the human-readable
            point name (`"started"`, `"shutdown"`, `"stopping"`, `"stopped"`).
            `None` for notifications of any other category.
        auditEventType: For audit notifications only, the standardized
            `AuditEventType` subtype (or a supertype thereof) this
            notification corresponds to, e.g.
            `o6.NodeId(o6.ns.ns0.objtypes.AuditActivateSessionEventType)`.
            `None` for notifications of any other category, and always
            `None` on a `Client`, which never raises audit notifications.
    """

    type: int
    payload: Mapping[str, Any] = field(default_factory=dict)
    lifecycle: str | None = None
    auditEventType: "o6.NodeId | None" = None

    def __post_init__(self) -> None:
        # The payload arrives as a plain dict built by the C trampoline;
        # handing it out read-only keeps one handler from corrupting it for
        # the handlers that run after it.
        object.__setattr__(self, "payload", MappingProxyType(dict(self.payload)))


class NotificationHandlers:
    """The handler registry behind one `on<category>Notification` property.

    Callable as a decorator, iterable as a list, and mutable by
    `remove` / `clear` / assigning a sequence. `on_change` is invoked
    (outside the lock) after every mutation, so the owner can install or
    remove its native callback as the registry becomes non-empty or empty.
    """

    def __init__(self, on_change: Callable[[], None]) -> None:
        self._on_change = on_change
        self._handlers: list[NotificationHandler] = []
        self._lock = threading.Lock()

    def __call__(self, handler: NotificationHandler) -> NotificationHandler:
        with self._lock:
            self._handlers.append(handler)
        self._on_change()
        return handler

    def __iter__(self) -> Iterator[NotificationHandler]:
        return iter(self.snapshot())

    def __len__(self) -> int:
        with self._lock:
            return len(self._handlers)

    def __bool__(self) -> bool:
        return len(self) > 0

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.snapshot()!r})"

    def replace(self, value: Any) -> None:
        """Swap the whole handler list. Accepts `None`, one callable, or a sequence."""
        if value is None:
            new: list[NotificationHandler] = []
        elif callable(value) and not isinstance(value, type):
            new = [value]
        else:
            new = list(value)
        with self._lock:
            self._handlers = new
        self._on_change()

    def clear(self) -> None:
        """Unregister every handler."""
        self.replace(None)

    def remove(self, handler: NotificationHandler) -> None:
        """Unregister one handler. Raises `ValueError` if not registered."""
        with self._lock:
            self._handlers.remove(handler)
        self._on_change()

    def snapshot(self) -> list[NotificationHandler]:
        """The handlers as they are right now, safe to iterate while others mutate."""
        with self._lock:
            return list(self._handlers)


def run_handlers(
    handlers: list[NotificationHandler],
    notification: Notification,
    loop: asyncio.AbstractEventLoop,
    logger: logging.Logger,
) -> None:
    """Invoke every handler, scheduling coroutines and swallowing failures.

    A handler that raises must not take down the notification that triggered
    it, the handlers queued behind it, or the server/client operation the
    notification came from — the same contract every other Python callback in
    this SDK follows.
    """
    for handler in handlers:
        try:
            result = invoke_sync(handler, (notification,))
        except Exception:
            logger.exception("Notification handler %r raised; continuing with the rest", handler)
            continue
        if inspect.isawaitable(result):
            schedule_coroutine(result, loop, logger)


def schedule_coroutine(coro: Any, loop: asyncio.AbstractEventLoop, logger: logging.Logger) -> None:
    """Hand a handler's coroutine to `loop` and log whatever it raises."""

    def _log(task: "asyncio.Future[Any]") -> None:
        if task.cancelled():
            return
        exc = task.exception()
        if exc is not None:
            logger.error(
                "Notification handler coroutine raised; continuing with the rest", exc_info=exc
            )

    try:
        task = asyncio.ensure_future(coro, loop=loop)
    except Exception:
        logger.exception("Notification handler coroutine could not be scheduled")
        return
    task.add_done_callback(_log)
