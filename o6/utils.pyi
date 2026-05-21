# Copyright 2026 (c) o6 Automation GmbH
"""Utility functions for converting between Python and OPC UA types."""

from __future__ import annotations

import asyncio
import threading
from typing import Any, Tuple

import o6

class _WorkerLoop:
    """Background thread driving an asyncio event loop."""

    def __init__(self, loop: asyncio.AbstractEventLoop) -> None: ...
    @property
    def loop(self) -> asyncio.AbstractEventLoop: ...
    @property
    def running(self) -> bool: ...
    @property
    def on_loop_thread(self) -> bool: ...
    def start(self) -> None: ...
    def stop(self, close: bool = False, timeout: float = 2.0) -> None: ...

NS0_DT_BOOLEAN: o6.NodeId
NS0_DT_SBYTE: o6.NodeId
NS0_DT_BYTE: o6.NodeId
NS0_DT_INT16: o6.NodeId
NS0_DT_UINT16: o6.NodeId
NS0_DT_INT32: o6.NodeId
NS0_DT_UINT32: o6.NodeId
NS0_DT_INT64: o6.NodeId
NS0_DT_UINT64: o6.NodeId
NS0_DT_FLOAT: o6.NodeId
NS0_DT_DOUBLE: o6.NodeId
NS0_DT_STRING: o6.NodeId
NS0_DT_BASE_DATA_TYPE: o6.NodeId

def _infer_data_type(value: Any) -> Tuple[o6.NodeId, int]:
    """Infer the OPC UA DataType NodeId and ValueRank from a Python value.

    Returns (data_type_nodeid, value_rank).
    """
    ...
