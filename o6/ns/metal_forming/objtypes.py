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

"""Generated OPC UA metal_forming namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.irdi_v1_00 as irdi_v1_00
import o6.ns.isa95_jobcontrol_v2 as isa95_jobcontrol_v2
import o6.ns.machine_tool as machine_tool
import o6.ns.machinery as machinery
import o6.ns.machinery_jobs as machinery_jobs
import o6.ns.machinery_processvalues as machinery_processvalues
import o6.ns.ns0 as ns0
import o6.ns.padim as padim
from . import datatypes as metal_forming_datypes
from . import vartypes as metal_forming_vartypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(nodeId="ns=metal_forming;i=1003", browseName="ns=metal_forming;FormingPositionsType", displayName="FormingPositionsType")
class FormingPositionsType(ns0.objtypes.BaseObjectType):
    bDC: CyclicProcessValueType | None
    retract: CyclicProcessValueType | None
    start: CyclicProcessValueType | None
    tDC: CyclicProcessValueType | None
    touch: CyclicProcessValueType | None


@o6.objecttype(nodeId="ns=metal_forming;i=1004", browseName="ns=metal_forming;ProcessWorkingUnitType", displayName="ProcessWorkingUnitType")
class ProcessWorkingUnitType(machine_tool.objtypes.WorkingUnitMonitoringType):
    langleCyclicProcessValueRangle: CyclicProcessValueType | None
    langleProcessValueRangle: machinery_processvalues.objtypes.ProcessValueType | None
    machineryItemState: machinery.objtypes.MachineryItemState_StateMachineType


@o6.objecttype(nodeId="ns=metal_forming;i=1008", browseName="ns=metal_forming;FormingProcessWorkingUnitType", displayName="FormingProcessWorkingUnitType")
class FormingProcessWorkingUnitType(ProcessWorkingUnitType):
    formingPositions: FormingPositionsType


@o6.objecttype(nodeId="ns=metal_forming;i=1010", browseName="ns=metal_forming;FormingToolType", displayName="FormingToolType")
class FormingToolType(machine_tool.objtypes.BaseToolType):
    location: ns0.objtypes.BaseObjectType | None


@o6.objecttype(nodeId="ns=metal_forming;i=1012", browseName="ns=metal_forming;FormingMultiToolType", displayName="FormingMultiToolType")
class FormingMultiToolType(machine_tool.objtypes.MultiToolType):
    langleFormingToolRangle: FormingToolType | None


@o6.objecttype(nodeId="ns=metal_forming;i=1023", browseName="ns=metal_forming;FormingProcessConditionClassType", displayName="FormingProcessConditionClassType", isAbstract=True)
class FormingProcessConditionClassType(ns0.objtypes.ProcessConditionClassType):
    pass


@o6.objecttype(
    nodeId="ns=metal_forming;i=1005", browseName="ns=metal_forming;OverloadTriggeredConditionClassType", displayName="OverloadTriggeredConditionClassType", isAbstract=True
)
class OverloadTriggeredConditionClassType(FormingProcessConditionClassType):
    pass


@o6.objecttype(
    nodeId="ns=metal_forming;i=1006", browseName="ns=metal_forming;EccentricLoadExceededConditionClassType", displayName="EccentricLoadExceededConditionClassType", isAbstract=True
)
class EccentricLoadExceededConditionClassType(FormingProcessConditionClassType):
    pass


@o6.objecttype(
    nodeId="ns=metal_forming;i=1009", browseName="ns=metal_forming;ProcessForceExceededConditionClassType", displayName="ProcessForceExceededConditionClassType", isAbstract=True
)
class ProcessForceExceededConditionClassType(FormingProcessConditionClassType):
    pass


@o6.objecttype(
    nodeId="ns=metal_forming;i=1011",
    browseName="ns=metal_forming;AllowableTiltingExceededConditionClassType",
    displayName="AllowableTiltingExceededConditionClassType",
    isAbstract=True,
)
class AllowableTiltingExceededConditionClassType(FormingProcessConditionClassType):
    pass


@o6.objecttype(
    nodeId="ns=metal_forming;i=1014",
    browseName="ns=metal_forming;BreakthroughTonnageExceededConditionClassType",
    displayName="BreakthroughTonnageExceededConditionClassType",
    isAbstract=True,
)
class BreakthroughTonnageExceededConditionClassType(FormingProcessConditionClassType):
    pass


@o6.objecttype(
    nodeId="ns=metal_forming;i=1017", browseName="ns=metal_forming;PositionOutOfRangeConditionClassType", displayName="PositionOutOfRangeConditionClassType", isAbstract=True
)
class PositionOutOfRangeConditionClassType(FormingProcessConditionClassType):
    pass


@o6.objecttype(
    nodeId="ns=metal_forming;i=1020",
    browseName="ns=metal_forming;CorrectionValueOutOfRangeConditionClassType",
    displayName="CorrectionValueOutOfRangeConditionClassType",
    isAbstract=True,
)
class CorrectionValueOutOfRangeConditionClassType(FormingProcessConditionClassType):
    pass


@o6.objecttype(nodeId="ns=metal_forming;i=1007", browseName="ns=metal_forming;CyclicProcessValueType", displayName="CyclicProcessValueType")
class CyclicProcessValueType(machinery_processvalues.objtypes.ProcessValueType):
    cyclicProcessValue: metal_forming_vartypes.CyclicProcessValueVariableType = o6.hasComponent(
        metal_forming_vartypes.CyclicProcessValueVariableType(
            nodeId="ns=metal_forming;i=6020",
            browseName="ns=metal_forming;CyclicProcessValue",
            dataType=metal_forming_datypes.CyclicProcessValueDataType,
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(nodeId="ns=metal_forming;i=1016", browseName="ns=metal_forming;CyclicEventType", displayName="CyclicEventType", isAbstract=True)
class CyclicEventType(ns0.objtypes.BaseEventType):
    currentProcessValue: machinery_processvalues.objtypes.ProcessValueType
    cycleCount: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=metal_forming;i=6055", browseName="ns=metal_forming;CycleCount", dataType=ns0.datatypes.Counter, accessLevel=3, userAccessLevel=1
        )
    )
    partId: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=metal_forming;i=6056", browseName="ns=metal_forming;PartId", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )


del (
    Any,
    TYPE_CHECKING,
    uuid,
    o6,
    di,
    ia,
    irdi_v1_00,
    isa95_jobcontrol_v2,
    machine_tool,
    machinery,
    machinery_jobs,
    machinery_processvalues,
    ns0,
    padim,
    metal_forming_datypes,
    metal_forming_vartypes,
)
