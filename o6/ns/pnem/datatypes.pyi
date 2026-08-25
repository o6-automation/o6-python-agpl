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

class PeVersionDataType(ns0.datatypes.Structure):
    @property
    def majorVersion(self) -> o6.Byte: ...
    @majorVersion.setter
    def majorVersion(self, value: _Integer) -> None: ...
    @property
    def minorVersion(self) -> o6.Byte: ...
    @minorVersion.setter
    def minorVersion(self, value: _Integer) -> None: ...
    @property
    def revision(self) -> o6.Byte: ...
    @revision.setter
    def revision(self, value: _Integer) -> None: ...

class AcPeDataType(ns0.datatypes.Structure):
    @property
    def a(self) -> o6.Float: ...
    @a.setter
    def a(self, value: SupportsFloat) -> None: ...
    @property
    def b(self) -> o6.Float: ...
    @b.setter
    def b(self, value: SupportsFloat) -> None: ...
    @property
    def c(self) -> o6.Float: ...
    @c.setter
    def c(self, value: SupportsFloat) -> None: ...

class AcPpDataType(ns0.datatypes.Structure):
    @property
    def a_b(self) -> o6.Float: ...
    @a_b.setter
    def a_b(self, value: SupportsFloat) -> None: ...
    @property
    def b_c(self) -> o6.Float: ...
    @b_c.setter
    def b_c(self, value: SupportsFloat) -> None: ...
    @property
    def c_a(self) -> o6.Float: ...
    @c_a.setter
    def c_a(self, value: SupportsFloat) -> None: ...

class PeClassEnumeration(enum.IntFlag):
    PE_CLASS1 = 0
    PE_CLASS2 = 1
    PE_CLASS3 = 2

class PeSubclassEnumeration(enum.IntFlag):
    PE_SUBCLASS1 = 0
    PE_SUBCLASS2 = 1

class AccuracyClassEnumeration(enum.IntFlag):
    ACCURACY_CLASS_0 = 0
    ACCURACY_CLASS_1 = 1
    ACCURACY_CLASS_2 = 2
    ACCURACY_CLASS_3 = 3
    ACCURACY_CLASS_4 = 4
    ACCURACY_CLASS_5 = 5
    ACCURACY_CLASS_6 = 6
    ACCURACY_CLASS_7 = 7
    ACCURACY_CLASS_8 = 8
    ACCURACY_CLASS_9 = 9
    ACCURACY_CLASS_10 = 10
    ACCURACY_CLASS_11 = 11
    ACCURACY_CLASS_12 = 12
    ACCURACY_CLASS_13 = 13
    ACCURACY_CLASS_14 = 14
    ACCURACY_CLASS_15 = 15

class AccuracyDomainEnumeration(enum.IntFlag):
    ACCURACY_DOMAIN_RESERVED = 0
    ACCURACY_DOMAIN_PERCENT_FULL_SCALE = 1
    ACCURACY_DOMAIN_PERCENT_ACTUAL_READING = 2
    ACCURACY_DOMAIN_IEC = 3
    ACCURACY_DOMAIN_EN = 4
