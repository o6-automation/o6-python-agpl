# Copyright (c) 2026 o6 Automation GmbH
#
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
