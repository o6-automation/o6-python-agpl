# Copyright (c) 2026 o6 Automation GmbH
#
# SPDX-License-Identifier: AGPL-3.0-or-later
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

"""Generated OPC UA scales namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.machinery as machinery
import o6.ns.ns0 as ns0
import o6.ns.pack_ml as pack_ml
from . import reftypes as scales_reftypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.enumtype(nodeId="ns=scales;i=54", browseName="ns=scales;TareMode")
class TareMode(ns0.datatypes.Enumeration):
    NONE_0 = o6.enumfield(0, name="None_0")
    MEASURED_TARE_1 = o6.enumfield(1, name="MeasuredTare_1")
    PRESET_TARE_2 = o6.enumfield(2, name="PresetTare_2")
    PROPORTIONAL_TARE_3 = o6.enumfield(3, name="ProportionalTare_3")


@o6.datatype(nodeId="ns=scales;i=57", browseName="ns=scales;RecipeThresholdType", defaultEncodingId="ns=scales;i=100")
class RecipeThresholdType(ns0.datatypes.Structure):
    thresholdId: o6.UInt32 = o6.field(name="ThresholdId")
    thresholdNodeId: o6.NodeId | None = o6.field(name="ThresholdNodeId")
    thresholdName: o6.LocalizedText = o6.field(name="ThresholdName")


@o6.datatype(nodeId="ns=scales;i=58", browseName="ns=scales;RecipeTargetValueType", defaultEncodingId="ns=scales;i=103")
class RecipeTargetValueType(ns0.datatypes.Structure):
    targetValueId: o6.UInt32 = o6.field(name="TargetValueId")
    targetValueNodeId: o6.NodeId | None = o6.field(name="TargetValueNodeId")
    targetValueName: o6.LocalizedText = o6.field(name="TargetValueName")


@o6.datatype(nodeId="ns=scales;i=59", browseName="ns=scales;RecipeReportElementType", defaultEncodingId="ns=scales;i=106")
class RecipeReportElementType(ns0.datatypes.Structure):
    reportMessage: o6.LocalizedText = o6.field(name="ReportMessage")
    timestamp: o6.DateTime = o6.field(name="Timestamp")


@o6.enumtype(nodeId="ns=scales;i=60", browseName="ns=scales;ToleranceState")
class ToleranceState(ns0.datatypes.Enumeration):
    IN_0 = o6.enumfield(0, name="In_0")
    UNDER_1 = o6.enumfield(1, name="Under_1")
    OVER_2 = o6.enumfield(2, name="Over_2")
    UNDER_OR_OVER_3 = o6.enumfield(3, name="UnderOrOver_3")


@o6.enumtype(
    nodeId="ns=scales;i=61", browseName="ns=scales;EqualityAndRelationalOperator", description="This enumeration describes the different condition modes for an analog condition."
)
class EqualityAndRelationalOperator(ns0.datatypes.Enumeration):
    EQUAL_0 = o6.enumfield(0, name="Equal_0")
    NOT_EQUAL_1 = o6.enumfield(1, name="NotEqual_1")
    LESS_OR_EQUAL_THAN_2 = o6.enumfield(2, name="LessOrEqualThan_2")
    GREATER_OR_EQUAL_THAN_3 = o6.enumfield(3, name="GreaterOrEqualThan_3")
    LESS_THAN_4 = o6.enumfield(4, name="LessThan_4")
    GREATER_THAN_5 = o6.enumfield(5, name="GreaterThan_5")


@o6.enumtype(nodeId="ns=scales;i=62", browseName="ns=scales;EdgeOperator")
class EdgeOperator(ns0.datatypes.Enumeration):
    RISING_0 = o6.enumfield(0, name="Rising_0")
    FALLING_1 = o6.enumfield(1, name="Falling_1")


@o6.datatype(nodeId="ns=scales;i=63", browseName="ns=scales;AbstractWeightType", defaultEncodingId="ns=scales;i=109", isAbstract=True)
class AbstractWeightType(ns0.datatypes.Structure):
    pass


@o6.datatype(nodeId="ns=scales;i=55", browseName="ns=scales;WeightType", defaultEncodingId="ns=scales;i=88")
class WeightType(AbstractWeightType):
    gross: o6.Double = o6.field(name="Gross")
    net: o6.Double = o6.field(name="Net")
    tare: o6.Double = o6.field(name="Tare")


@o6.datatype(nodeId="ns=scales;i=56", browseName="ns=scales;PrintableWeightType", defaultEncodingId="ns=scales;i=97")
class PrintableWeightType(AbstractWeightType):
    gross: o6.String = o6.field(name="Gross")
    net: o6.String = o6.field(name="Net")
    tare: o6.String = o6.field(name="Tare")


@o6.enumtype(nodeId="ns=scales;i=65", browseName="ns=scales;DraftShieldType")
class DraftShieldType(ns0.datatypes.Enumeration):
    RIGHT_0 = o6.enumfield(0, name="Right_0")
    LEFT_1 = o6.enumfield(1, name="Left_1")
    TOP_2 = o6.enumfield(2, name="Top_2")
    ALL_3 = o6.enumfield(3, name="All_3")


@o6.enumtype(nodeId="ns=scales;i=30003", browseName="ns=scales;RateControlMode")
class RateControlMode(ns0.datatypes.Enumeration):
    GRAVIMETRIC_0 = o6.enumfield(0, name="Gravimetric_0")
    VOLUMETRIC_1 = o6.enumfield(1, name="Volumetric_1")


del Any, TYPE_CHECKING, uuid, o6, di, ia, machinery, ns0, pack_ml, scales_reftypes
