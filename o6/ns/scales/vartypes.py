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
from . import datatypes as scales_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.variabletype(nodeId="ns=scales;i=52", browseName="ns=scales;MeasuredItemType", displayName="MeasuredItemType", valueRank=o6.ValueRank.ANY)
class MeasuredItemType(ns0.vartypes.DataItemType):
    eURange: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=324", browseName="EURange", dataType=ns0.datatypes.Range))
    engineeringUnits: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=scales;i=190", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)
    )
    instrumentRange: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=scales;i=133", browseName="ns=scales;InstrumentRange", dataType=ns0.datatypes.Range)
    )
    valuePrecision: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=scales;i=191",
            browseName="ValuePrecision",
            description="The maximum precision that the server can maintain for the item based on restrictions in the target environment.",
            dataType=o6.Double,
        )
    )


@o6.variabletype(nodeId="ns=scales;i=51", browseName="ns=scales;TargetItemType", displayName="TargetItemType", dataType=ns0.datatypes.Number, valueRank=o6.ValueRank.ANY)
class TargetItemType(ns0.vartypes.AnalogItemType):
    allowedEngineeringUnits: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=scales;i=433", browseName="ns=scales;AllowedEngineeringUnits", dataType=ns0.datatypes.EUInformation, valueRank=1, arrayDimensions=[0])
    )
    engineeringUnits: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=scales;i=168", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)
    )
    minusTolerance: ns0.vartypes.AnalogUnitType | None
    plusTolerance: ns0.vartypes.AnalogUnitType | None


@o6.variabletype(
    nodeId="ns=scales;i=53",
    browseName="ns=scales;WeightItemType",
    displayName="WeightItemType",
    dataType=scales_datypes.WeightType,
    value=scales_datypes.WeightType(gross=0.0, net=0.0, tare=0.0),
)
class WeightItemType(MeasuredItemType):
    centerOfZero: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=192", browseName="ns=scales;CenterOfZero", dataType=o6.Boolean))
    currentRangeId: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=scales;i=141", browseName="ns=scales;CurrentRangeId", dataType=o6.UInt16)
    )
    gross: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=scales;i=60033", browseName="ns=scales;Gross", dataType=o6.Double, accessLevel=3, userAccessLevel=1)
    )
    grossNegative: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=193", browseName="ns=scales;GrossNegative", dataType=o6.Boolean))
    highResolutionValue: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=scales;i=771", browseName="ns=scales;HighResolutionValue", dataType=scales_datypes.WeightType)
    )
    insideZero: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=scales;i=144",
            browseName="ns=scales;InsideZero",
            description="Defines if the current measured value is within the valid range for the setting zero procedure. This is a necessary condition to success the setZero() method if available.",
            dataType=o6.Boolean,
        )
    )
    legalForTrade: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=769", browseName="ns=scales;LegalForTrade", dataType=o6.Boolean))
    net: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=scales;i=60034", browseName="ns=scales;Net", dataType=o6.Double, accessLevel=3, userAccessLevel=1)
    )
    overload: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=142", browseName="ns=scales;Overload", dataType=o6.Boolean))
    printableValue: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=scales;i=770", browseName="ns=scales;PrintableValue", dataType=scales_datypes.PrintableWeightType)
    )
    tare: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=scales;i=60055", browseName="ns=scales;Tare", dataType=o6.Double, accessLevel=3, userAccessLevel=1)
    )
    tareMode: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=194", browseName="ns=scales;TareMode", dataType=scales_datypes.TareMode))
    underload: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=143", browseName="ns=scales;Underload", dataType=o6.Boolean))
    weightId: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=196", browseName="ns=scales;WeightId", dataType=o6.String))
    weightStable: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=199", browseName="ns=scales;WeightStable", dataType=o6.Boolean))


del Any, TYPE_CHECKING, uuid, o6, di, ia, machinery, ns0, pack_ml, scales_reftypes, scales_datypes
