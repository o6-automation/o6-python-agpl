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

"""Generated OPC UA pndrv namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
import o6.ns.pnenc as pnenc

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.variabletype(nodeId="ns=pndrv;i=2003", browseName="ns=pndrv;HomingModeType", displayName="HomingModeType", dataType=o6.Byte)
class HomingModeType(ns0.vartypes.MultiStateDiscreteType):
    pass


ns0.vartypes.PropertyType(
    nodeId="ns=pndrv;i=6152",
    browseName="EnumStrings",
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[3],
    value=[o6.LocalizedText("LINEAR", "en"), o6.LocalizedText("ROTATORY", "en"), o6.LocalizedText("ROTATORY_MODULO", "en")],
)


@o6.variabletype(nodeId="ns=pndrv;i=2000", browseName="ns=pndrv;AxisTypeVariableType", displayName="AxisTypeVariableType", dataType=o6.Byte)
class AxisTypeVariableType(ns0.vartypes.MultiStateDiscreteType):
    enumStrings: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=pndrv;i=6152"])


@o6.variabletype(nodeId="ns=pndrv;i=2001", browseName="ns=pndrv;TemperatureVariableType", displayName="TemperatureVariableType", dataType=o6.Float)
class TemperatureVariableType(ns0.vartypes.AnalogUnitType):
    faultThreshold: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pndrv;i=6206", browseName="ns=pndrv;FaultThreshold", dataType=o6.Float))
    warningThreshold: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pndrv;i=6205", browseName="ns=pndrv;WarningThreshold", dataType=o6.Float)
    )


ns0.vartypes.PropertyType(
    nodeId="ns=pndrv;i=6257",
    browseName="EnumStrings",
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[2],
    value=[o6.LocalizedText("POSITIVE"), o6.LocalizedText("NEGATIVE")],
)


@o6.variabletype(nodeId="ns=pndrv;i=2002", browseName="ns=pndrv;HomingDirectionType", displayName="HomingDirectionType", dataType=o6.Byte)
class HomingDirectionType(ns0.vartypes.MultiStateDiscreteType):
    enumStrings: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=pndrv;i=6257"])


del Any, TYPE_CHECKING, uuid, o6, di, ns0, pnenc
