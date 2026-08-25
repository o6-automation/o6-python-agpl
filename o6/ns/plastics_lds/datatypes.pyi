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

import o6.ns.ns0 as ns0

import o6.ns.plastics_rubber as plastics_rubber

class AdditiveStatusEnumeration(enum.IntFlag):
    """Actual status of the additive provides a minimal error handling for devices without event support."""

    GOOD = 0
    WARNING = 1
    ADVANCE_WARNING_ADDITIVE_CHANGE = 2
    ERROR_EMPTY = 3
    ERROR = 4

class ComponentStatusEnumeration(enum.IntFlag):
    """Actual status of the component provides a minimal error handling for devices without event support."""

    GOOD = 0
    WARNING = 1
    WARNING_PRESSURE_TOO_HIGH = 2
    WARNING_PRESSURE_TOO_LOW = 3
    ADVANCE_WARNING_DRUM_CHANGE = 4
    ERROR_DRUM_EMPTY = 5
    ERROR = 6

class PurgeStatusEnumeration(enum.IntFlag):
    OFF = 0
    COMPONENT_A = 1
    COMPONENT_B = 2
    COMPONENT_A_AND_B = 3
    COMPONENT_A_AND_B_CYCLIC = 4

class MaterialBalanceSystemTypeEnumeration(enum.IntFlag):
    NOT_AVAILABLE = 0
    ALWAYS_ACTIVE = 1
    SELECTABLE = 2
