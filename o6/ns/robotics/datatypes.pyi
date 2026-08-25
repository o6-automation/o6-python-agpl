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

import o6.ns.ns0 as ns0

class OperationalModeEnumeration(enum.IntFlag):
    OTHER = 0
    MANUAL_REDUCED_SPEED = 1
    MANUAL_HIGH_SPEED = 2
    AUTOMATIC = 3
    AUTOMATIC_EXTERNAL = 4

class AxisMotionProfileEnumeration(enum.IntFlag):
    OTHER = 0
    ROTARY = 1
    ROTARY_ENDLESS = 2
    LINEAR = 3
    LINEAR_ENDLESS = 4

class ExecutionModeEnumeration(enum.IntFlag):
    CYCLE = 0
    CONTINUOUS = 1
    STEP = 2

class MotionDeviceCategoryEnumeration(enum.IntFlag):
    OTHER = 0
    ARTICULATED_ROBOT = 1
    SCARA_ROBOT = 2
    CARTESIAN_ROBOT = 3
    SPHERICAL_ROBOT = 4
    PARALLEL_ROBOT = 5
    CYLINDRICAL_ROBOT = 6
