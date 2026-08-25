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

from typing import Any, Sequence, SupportsFloat

import numpy as np

_Integer = int | np.integer[Any]

_Boolean = bool | np.bool_

import enum

from o6.node import ObjectNode as _ObjectNode, VariableNode as _VariableNode

import uuid

import o6

import o6.ns.ns0 as ns0

class CommandEnum(enum.IntFlag):
    CLOSE = 1
    OPEN = 2
    NONE = 4

class SEMEnum(enum.IntFlag):
    SEM_A = 1
    SEM_B = 2
    AUTO = 4

class ChokeMoveEnum(enum.IntFlag):
    MOVING = 1
    STOPPED = 2

class SignatureStatusEnum(enum.IntFlag):
    NOT_AVAILABLE = 1
    COMPLETED = 2
    FAILED = 4

class ChokeCommandEnum(enum.IntFlag):
    CLOSE = 1
    OPEN = 2

class ValvePositionEnum(enum.IntFlag):
    CLOSED = 1
    OPEN = 2
    MOVING = 4
    UNKNOWN = 8

class SetCalculatedPositionEnum(enum.IntFlag):
    INITIAL = 0
    INPROGRESS = 1
    COMPLETE = 2
    FAULT = 4

class MDISVersionDataType(ns0.datatypes.Structure):
    @property
    def majorVersion(self) -> o6.Byte: ...
    @majorVersion.setter
    def majorVersion(self, value: _Integer) -> None: ...
    @property
    def minorVersion(self) -> o6.Byte: ...
    @minorVersion.setter
    def minorVersion(self, value: _Integer) -> None: ...
    @property
    def build(self) -> o6.Byte: ...
    @build.setter
    def build(self, value: _Integer) -> None: ...

class CIMVMoveEnum(enum.IntFlag):
    MOVE_CLOSE = 1
    MOVE_OPEN = 2
    STOP = 4

class ArbitrationModeEnum(enum.IntFlag):
    AVERAGE = 1
    DEFAULT_A = 2
    DEFAULT_B = 4
    FORCE_A = 8
    FORCE_B = 16
    HIGH = 32
    LOW = 64

class MotorStateEnum(enum.IntFlag):
    ACTIVE = 1
    NON_ACTIVE = 2

class MotorOperationEnum(enum.IntFlag):
    OFF = 1
    AUTO = 2
    MANUAL = 4

class CIMVOperationModeEnum(enum.IntFlag):
    POSITION = 1
    FLOW = 2
    MANUAL = 4
