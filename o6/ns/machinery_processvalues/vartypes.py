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

"""Generated OPC UA machinery_processvalues namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.irdi as irdi
import o6.ns.ns0 as ns0
import o6.ns.padim as padim

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.variabletype(
    nodeId="ns=machinery_processvalues;i=2002",
    browseName="ns=machinery_processvalues;ProcessValueVariableType",
    displayName="ProcessValueVariableType",
    description="Provides a process value and additional meta data",
    dataType=ns0.datatypes.Number,
    valueRank=o6.ValueRank.ANY,
)
class ProcessValueVariableType(padim.vartypes.AnalogSignalVariableType):
    highHighLimit: ns0.vartypes.AnalogUnitType | None
    highLimit: ns0.vartypes.AnalogUnitType | None
    lowLimit: ns0.vartypes.AnalogUnitType | None
    lowLowLimit: ns0.vartypes.AnalogUnitType | None
    percentageValue: ns0.vartypes.AnalogUnitRangeType | None


@o6.variabletype(
    nodeId="ns=machinery_processvalues;i=2003",
    browseName="ns=machinery_processvalues;ProcessValueSetpointVariableType",
    displayName="ProcessValueSetpointVariableType",
    description="Define the desired value of the Variable it belongs to.",
    dataType=ns0.datatypes.Number,
    valueRank=o6.ValueRank.ANY,
)
class ProcessValueSetpointVariableType(ns0.vartypes.AnalogUnitRangeType):
    autoDeviationAdjustment: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machinery_processvalues;i=6027",
            browseName="ns=machinery_processvalues;AutoDeviationAdjustment",
            description="Defines if the deviation variables are automatically adjusted.",
            dataType=o6.Boolean,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    deviationSensitivity: ns0.vartypes.MultiStateValueDiscreteType | None
    highDeviation: ns0.vartypes.AnalogUnitType | None
    highHighDeviation: ns0.vartypes.AnalogUnitType | None
    lowDeviation: ns0.vartypes.AnalogUnitType | None
    lowLowDeviation: ns0.vartypes.AnalogUnitType | None
    substituteValue: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=machinery_processvalues;i=6031",
            browseName="ns=machinery_processvalues;SubstituteValue",
            description="Value that should be used when the process value setpoint cannot be controlled anymore.",
            dataType=ns0.datatypes.Number,
            valueRank=-2,
            accessLevel=3,
            userAccessLevel=1,
        )
    )


del Any, TYPE_CHECKING, uuid, o6, di, irdi, ns0, padim
