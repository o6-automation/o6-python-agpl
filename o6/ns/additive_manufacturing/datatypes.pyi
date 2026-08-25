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

import o6.ns.isa95_jobcontrol_v2 as isa95_jobcontrol_v2

import o6.ns.machine_tool as machine_tool

import o6.ns.machinery as machinery

import o6.ns.machinery_jobs as machinery_jobs

import o6.ns.machinery_processvalues as machinery_processvalues

import o6.ns.ns0 as ns0

import o6.ns.padim as padim

class FeedstockFunction(enum.IntFlag):
    """This enumeration indicates the function of a specific feedstock."""

    UNDEFINED = 0
    MAIN = 1
    ANCILLARY = 2
    CONSUMABLE = 3

class RunInfoDataType(ns0.datatypes.Structure):
    @property
    def currentLayer(self) -> o6.UInt32 | None: ...
    @currentLayer.setter
    def currentLayer(self, value: _Integer | None) -> None: ...
    @property
    def identifier(self) -> o6.String: ...
    @identifier.setter
    def identifier(self, value: o6.String) -> None: ...
    @property
    def state(self) -> isa95_jobcontrol_v2.datatypes.ISA95StateDataType: ...
    @state.setter
    def state(self, value: isa95_jobcontrol_v2.datatypes.ISA95StateDataType) -> None: ...
    @property
    def remainingTime(self) -> o6.Double | None: ...
    @remainingTime.setter
    def remainingTime(self, value: SupportsFloat | None) -> None: ...

class SensorSeverity(enum.IntFlag):
    """This enumeration indicates the severity of a specific sensor."""

    INFO = 0
    CRITICAL = 1

class SensorCategory(enum.IntFlag):
    """This enumeration indicates the severity of a specific sensor."""

    MACHINE_HEALTH = 0
    MAINTENANCE_TRACKING = 1
    PROCESS_MONITORING = 2
