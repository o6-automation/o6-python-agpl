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

class IRtextShort:
    pass

class IRtext:
    pass

class IRtextLong:
    pass

class IRLengthDataType(ns0.datatypes.Structure):
    @property
    def value(self) -> o6.Double: ...
    @value.setter
    def value(self, value: SupportsFloat) -> None: ...
    @property
    def unit(self) -> ns0.datatypes.EUInformation: ...
    @unit.setter
    def unit(self, value: ns0.datatypes.EUInformation) -> None: ...

class JobAssignmentTimeDataType(ns0.datatypes.Union):
    @property
    def expectedFinishTime(self) -> o6.DateTime: ...
    @expectedFinishTime.setter
    def expectedFinishTime(self, value: o6.DateTime) -> None: ...
    @property
    def expectedDuration(self) -> o6.Double: ...
    @expectedDuration.setter
    def expectedDuration(self, value: SupportsFloat) -> None: ...

class IRangle:
    pass

class DispFlag(enum.IntFlag):
    MACH_START = 0
    FILE_LOAD = 1

class IRVersion:
    pass

class AnyURI:
    pass

class Answer(enum.IntFlag):
    ACCEPTED = 0
    DELAYED = 1
    ACCEPTED_WITH_CONDITION = 2
    DENIED = 3

class LTPPMptFromType(enum.IntFlag):
    LOAD_PT = 0
    DUMP_PT = 1
    PARKING = 2
    WORKSHOP = 3
    OTHERS = 4

class LTPPMptToType(enum.IntFlag):
    LOAD_PT = 0
    DUMP_PT = 1
    PARKING = 2
    BOULDER = 3
    WORKSHOP = 4
    OTHERS = 5

class LTPPMaction(enum.IntFlag):
    LOAD = 0
    DUMP = 1
    PARKING = 2
    WORKSHOP = 3
    OTHER = 4
