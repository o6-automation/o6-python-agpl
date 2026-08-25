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

class ExtrusionMessageClassificationEnumeration(enum.IntFlag):
    OTHER = 0
    LINE_CONTROL = 1
    MATERIAL_HANDLING = 2
    PRE_HEATING = 3
    FEEDING = 4
    DOSING = 5
    EXTRUDER = 6
    VACUUM_STATION = 7
    FILTER = 8
    MELT_PUMP = 9
    DIE = 10
    COOLING = 11
    HAUL_OFF = 12
    CORRUGATOR = 13
    SAW = 14
    CALIBRATION = 15
    ROLL_STACK = 16
    MDO = 17
    BIAX = 18
    CUTTING = 19
    WINDER = 20
    PELLETIZING = 21
    DRYER = 22
    HANDLING_SYSTEM = 23
    LAMINATION_SYSTEM = 24
    MEASURING_SYSTEM = 25
    QUALITY_SYSTEM = 26
    MANUAL_INSPECTION = 27
    MANUAL_OPERATION = 28

class ComponentStatusEnumeration(enum.IntFlag):
    OFFLINE = 0
    IDLE = 1
    PREPARING = 2
    READY_TO_RUN = 3
    MANUAL_RUN = 4
    CONTROLLED_RUN = 5
    MALFUNCTION = 6
    MAINTENANCE = 7
