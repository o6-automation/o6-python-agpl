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

import o6.ns.irdi as irdi

import o6.ns.machinery as machinery

import o6.ns.machinery_processvalues as machinery_processvalues

import o6.ns.ns0 as ns0

import o6.ns.padim as padim

class AnalogDigitalEnum(enum.IntFlag):
    """Specifies the type of a sensor"""

    ANALOG = 0
    DIGITAL = 1

class ControlModeEnum(enum.IntFlag):
    """Describes the possibility of controlling the system externally"""

    AUTOMATIC = 0
    MANUAL = 1
    OTHER = 2

class AirConnectionOpenEnum(enum.IntFlag):
    """Describes whether the air connection is open, i.e., it is in a state in which air can be passed through"""

    OPEN = 0
    CLOSED = 1
    OPENING = 2
    CLOSING = 3

class FilterAidDeviceStatusEnum(enum.IntFlag):
    """Describes the action performed by the device for filter aid"""

    DEVICE_ACTIVE = 0
    DEVICE_INACTIVE = 1
    FILLING_ACTIVE = 2
    DISCHARGE_ACTIVE = 3
