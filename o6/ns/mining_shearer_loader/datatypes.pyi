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

import o6.ns.mining as mining

import o6.ns.ns0 as ns0

class ShearerDirectionEnum(enum.IntFlag):
    STOP = 0
    LEFT = 1
    RIGHT = 2

class ShearerDrumMountingPositionEnum(enum.IntFlag):
    MOUNTING_POSITION_LEFT = 0
    MOUNTING_POSITION_RIGHT = 1
    MOUNTING_POSITION_LEFT_LUMP_BREAKER = 2
    MOUNTING_POSITION_RIGHT_LUMP_BREAKER = 3
