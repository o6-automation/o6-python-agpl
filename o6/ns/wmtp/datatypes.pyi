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

class WMTPOutputDataType(ns0.datatypes.Structure):
    @property
    def engineeringUnits(self) -> ns0.datatypes.EUInformation: ...
    @engineeringUnits.setter
    def engineeringUnits(self, value: ns0.datatypes.EUInformation) -> None: ...
    @property
    def actualValue(self) -> o6.Double: ...
    @actualValue.setter
    def actualValue(self, value: SupportsFloat) -> None: ...
    @property
    def typeOfMeasurement(self) -> o6.UInt32: ...
    @typeOfMeasurement.setter
    def typeOfMeasurement(self, value: _Integer) -> None: ...
    @property
    def typeOfSample(self) -> o6.UInt32: ...
    @typeOfSample.setter
    def typeOfSample(self, value: _Integer) -> None: ...
    @property
    def instrumentRange(self) -> ns0.datatypes.Range: ...
    @instrumentRange.setter
    def instrumentRange(self, value: ns0.datatypes.Range) -> None: ...
    @property
    def eURange(self) -> ns0.datatypes.Range: ...
    @eURange.setter
    def eURange(self, value: ns0.datatypes.Range) -> None: ...
    @property
    def valuePrecision(self) -> o6.Double: ...
    @valuePrecision.setter
    def valuePrecision(self, value: SupportsFloat) -> None: ...
    @property
    def definition(self) -> o6.String: ...
    @definition.setter
    def definition(self, value: o6.String) -> None: ...
    @property
    def signalTag(self) -> o6.String: ...
    @signalTag.setter
    def signalTag(self, value: o6.String) -> None: ...
    @property
    def relativeUncertainty(self) -> o6.Double: ...
    @relativeUncertainty.setter
    def relativeUncertainty(self, value: SupportsFloat) -> None: ...
    @property
    def absoluteUncertainty(self) -> o6.Double: ...
    @absoluteUncertainty.setter
    def absoluteUncertainty(self, value: SupportsFloat) -> None: ...
    @property
    def timestamp(self) -> o6.DateTime: ...
    @timestamp.setter
    def timestamp(self, value: o6.DateTime) -> None: ...
    @property
    def index(self) -> o6.UInt32: ...
    @index.setter
    def index(self, value: _Integer) -> None: ...
    @property
    def measurementPeriod(self) -> o6.Double: ...
    @measurementPeriod.setter
    def measurementPeriod(self, value: SupportsFloat) -> None: ...
    @property
    def internalUpdateInterval(self) -> o6.Double: ...
    @internalUpdateInterval.setter
    def internalUpdateInterval(self, value: SupportsFloat) -> None: ...
