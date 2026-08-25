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

"""Generated OPC UA di namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.ns0 as ns0
from . import reftypes as di_reftypes
from . import datatypes as di_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.variabletype(nodeId="ns=di;i=468", browseName="ns=di;LifetimeVariableType", displayName="LifetimeVariableType", description="Remaining lifetime", dataType=ns0.datatypes.Number)
class LifetimeVariableType(ns0.vartypes.AnalogUnitType):
    indication: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=di;i=471",
            browseName="ns=di;Indication",
            description="Indication gives an indication of what is actually measured / represented by the Value of the Variable and the StartValue and LimitValue.",
            dataType=o6.NodeId,
        )
    )
    limitValue: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=di;i=470", browseName="ns=di;LimitValue", description="LimitValue indicates when the end of lifetime has been reached.", dataType=ns0.datatypes.Number
        )
    )
    startValue: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=di;i=469",
            browseName="ns=di;StartValue",
            description="StartValue indicates the initial value, when there is still the full lifetime left.",
            dataType=ns0.datatypes.Number,
        )
    )
    warningValues: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=di;i=472",
            browseName="ns=di;WarningValues",
            description="WarningValues indicates one or more levels when the end of lifetime is reached soon and can be used to inform the user when reached.",
            dataType=ns0.datatypes.Number,
            valueRank=-3,
        )
    )


@o6.variabletype(nodeId="ns=di;i=6246", browseName="ns=di;UIElementType", displayName="UIElementType", isAbstract=True)
class UIElementType(ns0.vartypes.BaseDataVariableType):
    pass


del Any, TYPE_CHECKING, uuid, o6, ns0, di_reftypes, di_datypes
