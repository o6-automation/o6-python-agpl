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

import o6.ns.machinery as machinery

import o6.ns.ns0 as ns0

import o6.ns.pack_ml as pack_ml

class TareMode(enum.IntFlag):
    NONE_0 = 0
    MEASURED_TARE_1 = 1
    PRESET_TARE_2 = 2
    PROPORTIONAL_TARE_3 = 3

class RecipeThresholdType(ns0.datatypes.Structure):
    @property
    def thresholdId(self) -> o6.UInt32: ...
    @thresholdId.setter
    def thresholdId(self, value: _Integer) -> None: ...
    @property
    def thresholdNodeId(self) -> o6.NodeId | None: ...
    @thresholdNodeId.setter
    def thresholdNodeId(self, value: o6.NodeId | None) -> None: ...
    @property
    def thresholdName(self) -> o6.LocalizedText: ...
    @thresholdName.setter
    def thresholdName(self, value: o6.LocalizedText) -> None: ...

class RecipeTargetValueType(ns0.datatypes.Structure):
    @property
    def targetValueId(self) -> o6.UInt32: ...
    @targetValueId.setter
    def targetValueId(self, value: _Integer) -> None: ...
    @property
    def targetValueNodeId(self) -> o6.NodeId | None: ...
    @targetValueNodeId.setter
    def targetValueNodeId(self, value: o6.NodeId | None) -> None: ...
    @property
    def targetValueName(self) -> o6.LocalizedText: ...
    @targetValueName.setter
    def targetValueName(self, value: o6.LocalizedText) -> None: ...

class RecipeReportElementType(ns0.datatypes.Structure):
    @property
    def reportMessage(self) -> o6.LocalizedText: ...
    @reportMessage.setter
    def reportMessage(self, value: o6.LocalizedText) -> None: ...
    @property
    def timestamp(self) -> o6.DateTime: ...
    @timestamp.setter
    def timestamp(self, value: o6.DateTime) -> None: ...

class ToleranceState(enum.IntFlag):
    IN_0 = 0
    UNDER_1 = 1
    OVER_2 = 2
    UNDER_OR_OVER_3 = 3

class EqualityAndRelationalOperator(enum.IntFlag):
    """This enumeration describes the different condition modes for an analog condition."""

    EQUAL_0 = 0
    NOT_EQUAL_1 = 1
    LESS_OR_EQUAL_THAN_2 = 2
    GREATER_OR_EQUAL_THAN_3 = 3
    LESS_THAN_4 = 4
    GREATER_THAN_5 = 5

class EdgeOperator(enum.IntFlag):
    RISING_0 = 0
    FALLING_1 = 1

class AbstractWeightType(ns0.datatypes.Structure):
    pass

class WeightType(AbstractWeightType):
    @property
    def gross(self) -> o6.Double: ...
    @gross.setter
    def gross(self, value: SupportsFloat) -> None: ...
    @property
    def net(self) -> o6.Double: ...
    @net.setter
    def net(self, value: SupportsFloat) -> None: ...
    @property
    def tare(self) -> o6.Double: ...
    @tare.setter
    def tare(self, value: SupportsFloat) -> None: ...

class PrintableWeightType(AbstractWeightType):
    @property
    def gross(self) -> o6.String: ...
    @gross.setter
    def gross(self, value: o6.String) -> None: ...
    @property
    def net(self) -> o6.String: ...
    @net.setter
    def net(self, value: o6.String) -> None: ...
    @property
    def tare(self) -> o6.String: ...
    @tare.setter
    def tare(self, value: o6.String) -> None: ...

class DraftShieldType(enum.IntFlag):
    RIGHT_0 = 0
    LEFT_1 = 1
    TOP_2 = 2
    ALL_3 = 3

class RateControlMode(enum.IntFlag):
    GRAVIMETRIC_0 = 0
    VOLUMETRIC_1 = 1
