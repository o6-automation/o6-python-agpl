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

"""Generated OPC UA ecm namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.ns0 as ns0
from . import datatypes as ecm_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.variabletype(nodeId="ns=ecm;i=2002", browseName="ns=ecm;EnergyMeasurementValueType", displayName="EnergyMeasurementValueType", valueRank=o6.ValueRank.ANY)
class EnergyMeasurementValueType(ns0.vartypes.BaseDataVariableType):
    accuracyClass: ns0.vartypes.MultiStateValueDiscreteType
    accuracyDomain: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6019", browseName="ns=ecm;AccuracyDomain", dataType=o6.NodeId))
    accuracyRange: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6010", browseName="ns=ecm;AccuracyRange", dataType=o6.Float, accessLevel=3, userAccessLevel=1)
    )
    engineeringUnits: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6021", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)
    )
    measurementID: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6018", browseName="ns=ecm;MeasurementID", dataType=o6.UInt16))
    measurementPeriod: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6015", browseName="ns=ecm;MeasurementPeriod", dataType=ecm_datypes.MeasurementPeriodDataType, accessLevel=3, userAccessLevel=1)
    )
    resource: ns0.vartypes.MultiStateValueDiscreteType
    valueBeforeReset: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ecm;i=6022", browseName="ns=ecm;ValueBeforeReset", valueRank=-2))


del Any, TYPE_CHECKING, uuid, o6, di, ia, ns0, ecm_datypes
