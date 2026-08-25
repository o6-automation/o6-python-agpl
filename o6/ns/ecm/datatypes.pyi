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

class StandbyModeTransitionDataType(ns0.datatypes.Structure):
    @property
    def iDDestination(self) -> o6.Byte: ...
    @iDDestination.setter
    def iDDestination(self, value: _Integer) -> None: ...
    @property
    def currentTimeToDestination(self) -> o6.Double: ...
    @currentTimeToDestination.setter
    def currentTimeToDestination(self, value: SupportsFloat) -> None: ...
    @property
    def currentTimeToOperate(self) -> o6.Double: ...
    @currentTimeToOperate.setter
    def currentTimeToOperate(self, value: SupportsFloat) -> None: ...
    @property
    def energyConsumptionToDestination(self) -> o6.Float: ...
    @energyConsumptionToDestination.setter
    def energyConsumptionToDestination(self, value: SupportsFloat) -> None: ...

class EnergyStateInformationDataType(ns0.datatypes.Structure):
    @property
    def iDSource(self) -> o6.Byte: ...
    @iDSource.setter
    def iDSource(self, value: _Integer) -> None: ...
    @property
    def iDDestination(self) -> o6.Byte: ...
    @iDDestination.setter
    def iDDestination(self, value: _Integer) -> None: ...
    @property
    def regularTimeToOperate(self) -> o6.Double: ...
    @regularTimeToOperate.setter
    def regularTimeToOperate(self, value: SupportsFloat) -> None: ...
    @property
    def modePowerConsumption(self) -> o6.Float: ...
    @modePowerConsumption.setter
    def modePowerConsumption(self, value: SupportsFloat) -> None: ...

class AcPeDataType(ns0.datatypes.Structure):
    @property
    def l1(self) -> o6.Float: ...
    @l1.setter
    def l1(self, value: SupportsFloat) -> None: ...
    @property
    def l2(self) -> o6.Float: ...
    @l2.setter
    def l2(self, value: SupportsFloat) -> None: ...
    @property
    def l3(self) -> o6.Float: ...
    @l3.setter
    def l3(self, value: SupportsFloat) -> None: ...

class AcPpDataType(ns0.datatypes.Structure):
    @property
    def l1L2(self) -> o6.Float: ...
    @l1L2.setter
    def l1L2(self, value: SupportsFloat) -> None: ...
    @property
    def l2L3(self) -> o6.Float: ...
    @l2L3.setter
    def l2L3(self, value: SupportsFloat) -> None: ...
    @property
    def l3L1(self) -> o6.Float: ...
    @l3L1.setter
    def l3L1(self, value: SupportsFloat) -> None: ...

class MeasurementPeriodEnum(enum.IntFlag):
    SLIDING_DEMAND = 0
    FIXED_BLOCK_COMPLETED = 1
    FIXED_BLOCK_INSTANTANEOUS = 2
    FIXED_BLOCK_PREDICTED = 3

class MeasurementPeriodDataType(ns0.datatypes.Structure):
    @property
    def duration(self) -> o6.Double: ...
    @duration.setter
    def duration(self, value: SupportsFloat) -> None: ...
    @property
    def definition(self) -> MeasurementPeriodEnum: ...
    @definition.setter
    def definition(self, value: _Integer) -> None: ...
