# Copyright 2026 (c) o6 Automation GmbH
"""Native runtime hooks for OPC UA PubSub components.

PubSub configuration and ordinary control remain available through the
standard namespace-zero information model. This module contains only the
runtime facilities that model does not expose.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import TYPE_CHECKING, Protocol

import o6
from . import _o6

if TYPE_CHECKING:
    from o6.node import ObjectNode
    from o6.ns.ns0.datatypes import PubSubState


class OffsetType(Enum):
    """Kind of content found at one byte offset in a fixed PubSub message."""

    NETWORK_MESSAGE_GROUP_VERSION = 0
    NETWORK_MESSAGE_SEQUENCE_NUMBER = 1
    NETWORK_MESSAGE_TIMESTAMP = 2
    NETWORK_MESSAGE_PICOSECONDS = 3
    DATA_SET_MESSAGE = 4
    DATA_SET_MESSAGE_SEQUENCE_NUMBER = 5
    DATA_SET_MESSAGE_STATUS = 6
    DATA_SET_MESSAGE_TIMESTAMP = 7
    DATA_SET_MESSAGE_PICOSECONDS = 8
    DATA_SET_FIELD_DATA_VALUE = 9
    DATA_SET_FIELD_VARIANT = 10
    DATA_SET_FIELD_RAW = 11


# NOTE: ``slots=True`` is intentionally omitted. On CPython 3.12.0–3.12.3 a
# ``frozen=True, slots=True`` dataclass generates a ``__setattr__`` that raises
# ``TypeError: super(type, obj): obj must be an instance or subtype of type``
# (instead of ``FrozenInstanceError``) when an unknown attribute is assigned,
# because the frozen ``__setattr__`` closes over the pre-slots class. ``frozen``
# alone gives the same immutability with correct errors on every version.
@dataclass(frozen=True)
class Offset:
    """One typed byte offset and the component responsible for its value."""

    type: OffsetType
    offset: int
    component: o6.NodeId


@dataclass(frozen=True)
class OffsetTable:
    """An encoded fixed-layout message and its mutable byte positions."""

    offsets: tuple[Offset, ...]
    message: bytes


class StateMachine(Protocol):
    """Callable implementing the transition of one PubSub component."""

    def __call__(
        self,
        current: PubSubState,
        target: PubSubState,
    ) -> tuple[o6.StatusCode, PubSubState]:
        """Move the component from one state to another.

        Called synchronously on the server's event loop, so it must not block.

        Args:
            current: The component's current `PubSubState`.
            target: The `PubSubState` the server is requesting.

        Returns:
            The StatusCode of the transition and the state actually reached. A bad
            status, an exception, a recursive transition, or a malformed result
            moves the component to `ERROR`.
        """


def _requireEnabled() -> None:
    _o6._require_pubsub()


def _server(component: ObjectNode):
    backend = getattr(component, "_backend", None)
    server = getattr(backend, "_server", None)
    if server is None or not component._is_native_attached():
        raise TypeError("PubSub runtime operations require a live server node")
    return server


def setStateMachine(
    component: ObjectNode,
    callback: StateMachine | None,
) -> None:
    """Set a custom state machine on one concrete native PubSub component.

    This may be called from an implementation class `__init__`. Passing
    `None` restores open62541's native state machine. An already-created
    component must be disabled before changing it.
    """

    _requireEnabled()
    if callback is not None and not callable(callback):
        raise TypeError("state machine must be callable or None")
    server = _server(component)
    server._on_event_loop(lambda: component._set_pubsub_state_machine(callback))


def offsetTable(component: ObjectNode) -> OffsetTable:
    """Compute a fixed-layout offset table for a WriterGroup or DataSetReader.

    WriterGroup offsets address a complete NetworkMessage. DataSetReader
    offsets begin at zero for its DataSetMessage.
    """

    _requireEnabled()
    server = _server(component)
    message, native_offsets = server._on_event_loop(component._pubsub_offset_table)
    offsets = tuple(
        Offset(OffsetType(type_value), byte_offset, component_id)
        for type_value, byte_offset, component_id in native_offsets
    )
    return OffsetTable(offsets=offsets, message=message)


def publish(writerGroup: ObjectNode) -> None:
    """Publish one configured WriterGroup immediately.

    The WriterGroup must be a live native server component in a state where
    open62541 permits publishing. Native failures raise `StatusCodeError`.
    """

    _requireEnabled()
    server = _server(writerGroup)
    server._on_event_loop(writerGroup._pubsub_publish)


__all__ = [
    "Offset",
    "OffsetTable",
    "OffsetType",
    "StateMachine",
    "offsetTable",
    "publish",
    "setStateMachine",
]


def __dir__() -> list[str]:
    return sorted(__all__)
