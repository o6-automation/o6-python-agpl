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

import o6.ns.di as di

import o6.ns.ia as ia

import o6.ns.machinery as machinery

import o6.ns.ns0 as ns0

import o6.ns.robotics as robotics

class CraneOperationalModeEnum(enum.IntFlag):
    OTHER = 0
    MANUAL = 1
    SEMIAUTOMATIC = 2
    FULLAUTOMATIC = 3
    BYPASS_ON = 4
    MAINTENANCE = 5

class ExternalControlRequestEnum(enum.IntFlag):
    NOT_REQUESTED = 0
    REQUESTED_AND_CONTROL_ACTIVE = 1
    REQUESTED_AND_CONTROL_INACTIVE = 2
    REQUESTED_AND_CONTROL_BYPASSED = 3

class ProtectiveFunctionEnum(enum.IntFlag):
    OTHER = 0
    FORCE_LIMITER = 1
    OVERSPEED_CONTROL = 2
    MOTION_LIMITER = 3
    ANTICOLLISION = 4

class CraneMotionDeviceCategoryEnum(enum.IntFlag):
    HOIST = 0
    TROLLEY_TRAVERSE = 1
    BRIDGE_OR_GANTRY_TRAVEL = 2
    LOAD_LIFTING_ATTACHMENT = 3
    ROTATING_OR_SLEWING = 4
    LUFFING = 5
    POWER_SUPPLY_MACHINERY = 6
    OTHER = 7
