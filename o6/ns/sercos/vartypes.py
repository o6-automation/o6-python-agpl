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

"""Generated OPC UA sercos namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.variabletype(nodeId="ns=sercos;i=2001", browseName="ns=sercos;SercosParameterType", displayName="SercosParameterType", valueRank=o6.ValueRank.ANY)
class SercosParameterType(ns0.vartypes.BaseDataVariableType):
    attribute: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=sercos;i=6004", browseName="ns=sercos;Attribute", dataType=o6.UInt32))
    displayMaxValue: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=sercos;i=6008", browseName="ns=sercos;DisplayMaxValue", dataType=o6.String)
    )
    displayMinValue: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=sercos;i=6007", browseName="ns=sercos;DisplayMinValue", dataType=o6.String)
    )
    displayValue: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=sercos;i=6009", browseName="ns=sercos;DisplayValue", dataType=o6.String))
    exponent: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=sercos;i=6006", browseName="ns=sercos;Exponent", dataType=o6.SByte))
    maxValue: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=sercos;i=6001", browseName="ns=sercos;MaxValue"))
    minValue: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=sercos;i=6002", browseName="ns=sercos;MinValue"))
    procedureCommand: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=sercos;i=6005", browseName="ns=sercos;ProcedureCommand", dataType=o6.Boolean)
    )


del Any, TYPE_CHECKING, uuid, o6, di, ns0
