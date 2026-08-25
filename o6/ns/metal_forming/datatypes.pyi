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

import o6.ns.irdi_v1_00 as irdi_v1_00

import o6.ns.isa95_jobcontrol_v2 as isa95_jobcontrol_v2

import o6.ns.machine_tool as machine_tool

import o6.ns.machinery as machinery

import o6.ns.machinery_jobs as machinery_jobs

import o6.ns.machinery_processvalues as machinery_processvalues

import o6.ns.ns0 as ns0

import o6.ns.padim as padim

class CyclicProcessValueDataType(ns0.datatypes.Structure):
    @property
    def analogSignal(self) -> o6.ExtensionObject: ...
    @analogSignal.setter
    def analogSignal(self, value: Any) -> None: ...
    @property
    def setpoint(self) -> o6.ExtensionObject: ...
    @setpoint.setter
    def setpoint(self, value: Any) -> None: ...
    @property
    def cycleCount(self) -> o6.UInt32: ...
    @cycleCount.setter
    def cycleCount(self, value: _Integer) -> None: ...
    @property
    def isActive(self) -> o6.Boolean: ...
    @isActive.setter
    def isActive(self, value: _Boolean) -> None: ...

class CyclicPartInformationDataType(ns0.datatypes.Structure):
    @property
    def cycleCount(self) -> o6.UInt32: ...
    @cycleCount.setter
    def cycleCount(self, value: _Integer) -> None: ...
    @property
    def partId(self) -> o6.String | None: ...
    @partId.setter
    def partId(self, value: o6.String | None) -> None: ...
