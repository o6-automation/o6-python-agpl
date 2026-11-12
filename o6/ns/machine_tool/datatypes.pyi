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

import o6.ns.di as di

import o6.ns.ia as ia

import o6.ns.isa95_jobcontrol_v2 as isa95_jobcontrol_v2

import o6.ns.machinery as machinery

import o6.ns.machinery_jobs as machinery_jobs

import o6.ns.ns0 as ns0

class ProcessIrregularity(enum.IntEnum):
    CAPABILITY_UNAVAILABLE = 0
    DETECTED = 1
    NOT_DETECTED = 2
    NOT_YET_DETERMINED = 3

class PartQuality(enum.IntEnum):
    CAPABILITY_UNAVAILABLE = 0
    GOOD = 1
    BAD = 2
    NOT_YET_MEASURED = 3
    WILL_NOT_BE_MEASURED = 4

class ChannelState(enum.IntEnum):
    ACTIVE = 0
    INTERRUPTED = 1
    RESET = 2

class MachineOperationMode(enum.IntEnum):
    MANUAL = 0
    AUTOMATIC = 1
    SETUP = 2
    AUTO_WITH_MANUAL_INTERVENTION = 3
    SERVICE = 4
    OTHER = 5

class ToolLocked(enum.IntEnum):
    CAPABILITY_UNAVAILABLE = 0
    BY_OPERATOR = 1
    TOOL_BREAK = 2
    TOOL_LIFE = 3
    MEASUREMENT_ERROR = 4
    OTHER = 5

class ChannelMode(enum.IntEnum):
    AUTOMATIC = 0
    MDA_MDI = 1
    JOG_MANUAL = 2
    JOG_INCREMENT = 3
    TEACHING_HANDLE = 4
    REMOTE = 5
    REFERENCE = 6
    OTHER = 7

class ToolLifeIndication(enum.IntEnum):
    TIME = 0
    NUMBER_OF_PARTS = 1
    NUMBER_OF_USAGES = 2
    FEED_DISTANCE = 3
    CUTTING_DISTANCE = 4
    LENGTH = 5
    DIAMETER = 6
    OTHER = 7

class ToolManagement(enum.IntEnum):
    NUMBER_BASED = 0
    GROUP_BASED = 1
    OTHER = 2

class LaserState(enum.IntEnum):
    UNDEFINED = 0
    READY = 1
    ACTIVE = 2
    ERROR = 3

class EDMGeneratorState(enum.IntEnum):
    UNDEFINED = 0
    READY = 1
    ACTIVE_LOW_VOLTAGE = 2
    ACTIVE_HIGH_VOLTAGE = 3
    ERROR = 4
