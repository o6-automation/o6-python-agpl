# Copyright (c) 2026 o6 Automation GmbH
#
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

from typing import Any, Sequence, SupportsFloat

import numpy as np

_Integer = int | np.integer[Any]

_Boolean = bool | np.bool_

import enum

from o6.node import ObjectNode as _ObjectNode, VariableNode as _VariableNode

import uuid

import o6

import o6.ns.ns0 as ns0

class CncSpindleTurnDirection(enum.IntEnum):
    """Turn direction of a CNC spindle."""

    NONE = 0
    CW = 1
    CCW = 2

class CncChannelProgramStatus(enum.IntEnum):
    """Status of program execution within a channel."""

    STOPPED = 0
    RUNNING = 1
    WAITING = 2
    INTERRUPTED = 3
    CANCELED = 4

class CncChannelStatus(enum.IntEnum):
    """Status of a CNC channel."""

    ACTIVE = 0
    INTERRUPTED = 1
    RESET = 2

class CncAxisStatus(enum.IntEnum):
    """Status of a CNC axis."""

    IN_POSITION = 0
    MOVING = 1
    PARKED = 2

class CncSpindleStatus(enum.IntEnum):
    """Status of a CNC spindle."""

    STOPPED = 0
    IN_TARGET_AREA = 1
    ACCELERATING = 2
    DECELERATING = 3
    PARKED = 4

class CncOperationMode(enum.IntEnum):
    """Modes of operation."""

    MANUAL = 0
    MDA = 1
    AUTOMATIC = 2

class CncPositionDataType(ns0.datatypes.Structure):
    """Structure of position elements."""

    @property
    def actPos(self) -> o6.Double: ...
    @actPos.setter
    def actPos(self, value: SupportsFloat) -> None: ...
    @property
    def cmdPos(self) -> o6.Double: ...
    @cmdPos.setter
    def cmdPos(self, value: SupportsFloat) -> None: ...
    @property
    def remDist(self) -> o6.Double: ...
    @remDist.setter
    def remDist(self, value: SupportsFloat) -> None: ...
