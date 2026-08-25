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
from . import vartypes as machinery_processvalues_vartypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(
    nodeId="ns=machinery_processvalues;i=1002",
    browseName="ns=machinery_processvalues;ZeroPointAdjustmentEventType",
    displayName="ZeroPointAdjustmentEventType",
    description="Provides information, that a zero-point adjustment took place",
    isAbstract=True,
)
class ZeroPointAdjustmentEventType(ns0.objtypes.BaseEventType):
    zeroPointAdjustmentResult: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machinery_processvalues;i=6032", browseName="ns=machinery_processvalues;ZeroPointAdjustmentResult", dataType=o6.StatusCode, accessLevel=3, userAccessLevel=1
        )
    )


o6.call(nodeId="ns=machinery_processvalues;i=7001", browseName="ns=padim;ZeroPointAdjustment", displayName="Zero point adjustment")
o6.reference(o6.ns["ns=machinery_processvalues;i=7001"], "i=41", ZeroPointAdjustmentEventType)


@o6.objecttype(
    nodeId="ns=machinery_processvalues;i=1003", browseName="ns=machinery_processvalues;ProcessValueType", displayName="ProcessValueType", description="Represents a process value"
)
class ProcessValueType(padim.objtypes.AnalogSignalType):
    alarmSuppression: ns0.vartypes.MultiStateValueDiscreteType | None
    analogSignal: padim.vartypes.AnalogSignalVariableType
    deviationAlarm: ns0.objtypes.ExclusiveDeviationAlarmType | None
    limitAlarm: ns0.objtypes.ExclusiveLimitAlarmType | None
    processValueSetpoint: machinery_processvalues_vartypes.ProcessValueSetpointVariableType | None
    status: ns0.vartypes.MultiStateValueDiscreteType | None
    zeroPointAdjustment: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=machinery_processvalues;i=7001"])


del Any, TYPE_CHECKING, uuid, o6, di, irdi, ns0, padim, machinery_processvalues_vartypes
