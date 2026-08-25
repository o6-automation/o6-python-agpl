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

"""Generated OPC UA ia namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
from . import reftypes as ia_reftypes
from . import datatypes as ia_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.variabletype(
    nodeId="ns=ia;i=2002",
    browseName="ns=ia;CalibrationValueType",
    displayName="CalibrationValueType",
    description="Represents the specific quantity and value (with engineering unit) that a calibration target provides for calibration of equipment.",
    dataType=ns0.datatypes.Number,
    valueRank=o6.ValueRank.ANY,
)
class CalibrationValueType(ns0.vartypes.DataItemType):
    engineeringUnits: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=ia;i=6057", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation, accessLevel=3, userAccessLevel=1)
    )


@o6.variabletype(
    nodeId="ns=ia;i=2003",
    browseName="ns=ia;CapacityRangeType",
    displayName="CapacityRangeType",
    description="Represent a scale of calibration values. The value defines the range (lowest and highest value), and the resolution property the size of each step.",
    dataType=ns0.datatypes.Range,
)
class CapacityRangeType(ns0.vartypes.DataItemType):
    engineeringUnits: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=ia;i=6058", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation, accessLevel=3, userAccessLevel=1)
    )
    resolution: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=ia;i=6059", browseName="ns=ia;Resolution", dataType=o6.Double, accessLevel=3, userAccessLevel=1)
    )


del Any, TYPE_CHECKING, uuid, o6, di, ns0, ia_reftypes, ia_datypes
