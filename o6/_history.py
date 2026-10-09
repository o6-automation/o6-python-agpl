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

"""The per-node historizing settings accepted by `historizing=`."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional

STRATEGIES = ("on-write", "poll", "manual")


@dataclass(frozen=True)
class History:
    """Per-variable history settings accepted by `historizing=`.

    `historizing=True` selects `History()`.

    Attributes:
        capacity: Samples retained per node. Zero uses the database default;
            None selects unbounded growth. A bounded store evicts oldest samples.
        strategy: "on-write" records Writes, "poll" samples through an internal
            MonitoredItem, and "manual" requires explicit insertion.
        interval: Poll interval in seconds, converted to native milliseconds.
    """

    capacity: Optional[int] = 0
    strategy: str = "on-write"
    interval: float = 1.0

    def __post_init__(self) -> None:
        if self.strategy not in STRATEGIES:
            expected = ", ".join(repr(name) for name in STRATEGIES)
            raise ValueError(f"unknown history strategy {self.strategy!r}, expected {expected}")
        if self.capacity is not None and self.capacity < 0:
            raise ValueError("capacity must not be negative, or None to grow without a limit")
        # open62541 counts the polling interval in milliseconds, so anything
        # that rounds to nothing would become "sample on every change".
        if self.strategy == "poll" and round(self.interval * 1000.0) < 1:
            raise ValueError("the poll strategy needs an interval of at least 0.001 seconds")


class HistoryBackend:
    """Base class for a user-supplied server-side history store.

    Subclass it and override the methods you can serve; leave the rest alone.
    Passed to `server.config.setHistoryDatabase(backend=...)` in place of the
    built-in in-memory store — the two are mutually exclusive for one server.

    ```python
    class MyBackend(o6.HistoryBackend):
        def onWrite(self, nodeId, value):
            ...  # store however you like

        def getHistoryData(self, nodeId, start, end, maxSize, numValues,
                            returnBounds, timestampsToReturn, range):
            ...  # serve ReadRaw entirely yourself
            return [...]  # list[o6.DataValue]

    server.config.setHistoryDatabase(backend=MyBackend())
    ```
    """

    _history_hooks = (
        "onWrite",
        "getHistoryData",
        "getHistoryPage",
        "insertDataValue",
        "replaceDataValue",
        "updateDataValue",
        "removeDataValue",
        "boundSupported",
        "timestampsToReturnSupported",
    )

    def onWrite(self, nodeId: Any, value: Any) -> None:
        """Record one sample from an on-write operation or polling callback."""
        raise NotImplementedError

    def getHistoryData(
        self,
        nodeId: Any,
        start: Any,
        end: Any,
        maxSize: int,
        numValues: int,
        returnBounds: bool,
        timestampsToReturn: Any,
        range: "tuple[slice, ...] | None",
    ) -> list:
        """Return DataValues for one ReadRaw request.

        `start` and `end` are DateTime values or None for unspecified bounds.
        The backend must apply range, timestamp selection, and requested bounds.
        `maxSize` and `numValues` provide limits; the binding does not truncate.

        Override getHistoryPage instead when the store needs continuation points.
        """
        raise NotImplementedError

    def getHistoryPage(
        self,
        nodeId: Any,
        start: Any,
        end: Any,
        maxSize: int,
        numValues: int,
        returnBounds: bool,
        timestampsToReturn: Any,
        range: "tuple[slice, ...] | None",
        continuationPoint: bytes,
        releaseContinuationPoints: bool,
        sessionId: Any,
    ) -> tuple[list, bytes]:
        """Return ``(dataValues, nextToken)`` for a ReadRaw page.

        An empty input token starts a read; an empty output token finishes it.
        Respect maxSize and numValues when nonzero. Tokens must belong to the
        requesting session and node; reject invalid tokens with
        StatusCodeError(BAD_CONTINUATION_POINT_INVALID). On release, free the
        token and return ([], b""). Expire abandoned tokens in the store.
        This hook takes precedence over getHistoryData when overridden.
        """
        raise NotImplementedError

    def insertDataValue(self, nodeId: Any, value: Any) -> None:
        """Serve a HistoryUpdate Insert. Unimplemented answers `BadHistoryOperationUnsupported`."""
        raise NotImplementedError

    def replaceDataValue(self, nodeId: Any, value: Any) -> None:
        """Serve a HistoryUpdate Replace. Unimplemented answers `BadHistoryOperationUnsupported`."""
        raise NotImplementedError

    def updateDataValue(self, nodeId: Any, value: Any) -> None:
        """Serve a HistoryUpdate Update (insert-or-replace). Unimplemented answers `BadHistoryOperationUnsupported`."""
        raise NotImplementedError

    def removeDataValue(self, nodeId: Any, start: Any, end: Any) -> None:
        """Serve a HistoryUpdate Delete over `[start, end)` (`o6.DateTime`). Unimplemented answers `BadHistoryOperationUnsupported`."""
        raise NotImplementedError

    def boundSupported(self, nodeId: Any) -> bool:
        """Whether this node can return bounding values. Default `False` (always legal to answer)."""
        return False

    def timestampsToReturnSupported(self, nodeId: Any, timestampsToReturn: Any) -> bool:
        """Whether this node supports the requested timestamp kind. Default `False`."""
        return False

    def _overridden_callbacks(self) -> "frozenset[str]":
        """Return hooks that need a C-to-Python callback trampoline."""
        plugin_type = type(self)
        return frozenset(
            name
            for name in self._history_hooks
            if getattr(plugin_type, name) is not getattr(HistoryBackend, name)
        )


def as_history(historizing: "bool | History | None") -> Optional[History]:
    """Normalize True to default History settings and False/None to None.

    Existing History instances pass through. Other values raise TypeError.
    """
    if historizing is None or historizing is False:
        return None
    if historizing is True:
        return History()
    if isinstance(historizing, History):
        return historizing
    raise TypeError(f"historizing must be a bool or o6.History, not {type(historizing).__name__}")
