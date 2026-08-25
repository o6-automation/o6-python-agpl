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

"""Generated OPC UA pnem namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
from . import reftypes as pnem_reftypes
from . import datatypes as pnem_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.variabletype(nodeId="ns=pnem;i=2002", browseName="ns=pnem;MeasurementValueType", displayName="MeasurementValueType", valueRank=o6.ValueRank.ANY)
class MeasurementValueType(ns0.vartypes.BaseDataVariableType):
    accuracyClass: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6020", browseName="ns=pnem;AccuracyClass", dataType=pnem_datypes.AccuracyClassEnumeration)
    )
    accuracyDomain: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6019", browseName="ns=pnem;AccuracyDomain", dataType=pnem_datypes.AccuracyDomainEnumeration)
    )
    engineeringUnits: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6021", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)
    )
    peMeasurementID: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6018", browseName="ns=pnem;PeMeasurementID", dataType=o6.UInt16))
    valueBeforeReset: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6022", browseName="ns=pnem;ValueBeforeReset"))


del Any, TYPE_CHECKING, uuid, o6, di, ns0, pnem_reftypes, pnem_datypes
