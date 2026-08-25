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

class OperatingModeEnumeration(enum.IntFlag):
    """Actual operating mode of the TCD"""

    OTHER = 0
    READY_TO_OPERATE = 1
    NORMAL_OPERATION = 2
    LEAK_STOPPER = 3
    MOULD_EVACUATION = 4
    PRESSURE_RELIEF = 5
    COOLING = 6
    SAFETY_COOLING = 7
    ECO = 8
    BOOST = 9
