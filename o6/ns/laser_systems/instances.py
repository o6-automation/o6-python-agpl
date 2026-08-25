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

"""Generated OPC UA laser_systems namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.isa95_jobcontrol_v2 as isa95_jobcontrol_v2
import o6.ns.machine_tool as machine_tool
import o6.ns.machinery as machinery
import o6.ns.machinery_jobs as machinery_jobs
import o6.ns.ns0 as ns0
from . import objtypes as laser_systems_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.vartypes.AnalogUnitType(
    nodeId="ns=laser_systems;i=6003",
    browseName="ns=laser_systems;Value",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6004", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
)
o6.reference(laser_systems_objtypes.ConsumptionDataMonitoringType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=6003"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=laser_systems;i=6006",
    browseName="ns=laser_systems;Value",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6007", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
)
o6.reference(laser_systems_objtypes.ConditionDataMonitoringType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=6006"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=laser_systems;i=6010",
    browseName="ns=laser_systems;PreviousValue",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6011", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
)
o6.reference(laser_systems_objtypes.ActivityDataMonitoringType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=6010"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=laser_systems;i=6012",
    browseName="ns=laser_systems;CurrentValue",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6013", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
)
o6.reference(laser_systems_objtypes.ActivityDataMonitoringType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=6012"])
machinery.objtypes.MachineryComponentIdentificationType(
    nodeId="ns=laser_systems;i=5001",
    browseName="ns=di;Identification",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=laser_systems;i=6017",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=laser_systems;i=6018",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(laser_systems_objtypes.LaserSystemType, ns0.reftypes.HasAddIn, o6.ns["ns=laser_systems;i=5001"])
o6.reference(o6.ns["ns=laser_systems;i=5103"], "i=17604", o6.ns["ns=laser_systems;i=5001"])
ia.objtypes.BasicStacklightType(
    nodeId="ns=laser_systems;i=5005",
    browseName="ns=laser_systems;Stacklight",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=laser_systems;i=6019",
                browseName="ns=ia;StacklightMode",
                description="Shows in what way (stack of individual lights, level meter, running light) the stacklight unit is used.",
                dataType=ia.datatypes.StacklightOperationMode,
                accessLevel=3,
                userAccessLevel=1,
            )
        )
    ],
)
o6.reference(laser_systems_objtypes.LaserSystemMonitoringType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5005"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=laser_systems;i=6020",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6021", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
laser_systems_objtypes.LaserSystemState_StateMachineType(
    nodeId="ns=laser_systems;i=5007", browseName="ns=laser_systems;LaserSystemState", references=[o6.hasComponent(o6.ns["ns=laser_systems;i=6020"])]
)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=laser_systems;i=6022",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6023", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
laser_systems_objtypes.LaserSystemState_StateMachineType(
    nodeId="ns=laser_systems;i=5013", browseName="ns=laser_systems;LaserSystemState", modellingRule="Mandatory", references=[o6.hasComponent(o6.ns["ns=laser_systems;i=6022"])]
)
o6.reference(laser_systems_objtypes.LaserSystemStatusType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5013"])
machine_tool.objtypes.LaserMonitoringType(
    nodeId="ns=laser_systems;i=5014",
    browseName="ns=laser_systems;MachineToolsLaserStatus",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6033", browseName="ns=machine_tool;Name", dataType=o6.String)),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(nodeId="ns=laser_systems;i=6031", browseName="ns=machine_tool;ControllerIsOn", dataType=o6.Boolean)
        ),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=laser_systems;i=6032", browseName="ns=machine_tool;LaserState", dataType=machine_tool.datatypes.LaserState)),
    ],
)
o6.reference(laser_systems_objtypes.LaserSystemStatusType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5014"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=laser_systems;i=6034",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6035", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
machinery.objtypes.MachineryItemState_StateMachineType(
    nodeId="ns=laser_systems;i=5015", browseName="ns=machinery;MachineryItemState", modellingRule="Mandatory", references=[o6.hasComponent(o6.ns["ns=laser_systems;i=6034"])]
)
o6.reference(laser_systems_objtypes.LaserSystemStatusType, ns0.reftypes.HasAddIn, o6.ns["ns=laser_systems;i=5015"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=laser_systems;i=6036",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6037", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
machinery.objtypes.MachineryOperationModeStateMachineType(
    nodeId="ns=laser_systems;i=5016", browseName="ns=machinery;MachineryOperationMode", modellingRule="Mandatory", references=[o6.hasComponent(o6.ns["ns=laser_systems;i=6036"])]
)
o6.reference(laser_systems_objtypes.LaserSystemStatusType, ns0.reftypes.HasAddIn, o6.ns["ns=laser_systems;i=5016"])
laser_systems_objtypes.LaserSystemOperationCounterType(
    nodeId="ns=laser_systems;i=5017",
    browseName="ns=di;OperationCounters",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6038", browseName="ns=di;OperationDuration", dataType=ns0.datatypes.Duration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6039", browseName="ns=di;PowerOnDuration", dataType=ns0.datatypes.Duration)),
    ],
)
o6.reference(laser_systems_objtypes.LaserSystemStatusType, ns0.reftypes.HasAddIn, o6.ns["ns=laser_systems;i=5017"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=laser_systems;i=6040",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6043", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
machinery.objtypes.MachineryItemState_StateMachineType(
    nodeId="ns=laser_systems;i=5018", browseName="ns=machinery;MachineryItemState", references=[o6.hasComponent(o6.ns["ns=laser_systems;i=6040"])]
)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=laser_systems;i=6044",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6045", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
machinery.objtypes.MachineryOperationModeStateMachineType(
    nodeId="ns=laser_systems;i=5019", browseName="ns=machinery;MachineryOperationMode", references=[o6.hasComponent(o6.ns["ns=laser_systems;i=6044"])]
)
machine_tool.objtypes.LaserMonitoringType(
    nodeId="ns=laser_systems;i=5020",
    browseName="ns=laser_systems;MachineToolsLaserStatus",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6048", browseName="ns=machine_tool;Name", dataType=o6.String)),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(nodeId="ns=laser_systems;i=6046", browseName="ns=machine_tool;ControllerIsOn", dataType=o6.Boolean)
        ),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=laser_systems;i=6047", browseName="ns=machine_tool;LaserState", dataType=machine_tool.datatypes.LaserState)),
    ],
)
laser_systems_objtypes.LaserSystemOperationCounterType(
    nodeId="ns=laser_systems;i=5021",
    browseName="ns=di;OperationCounters",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6049", browseName="ns=di;OperationDuration", dataType=ns0.datatypes.Duration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6050", browseName="ns=di;PowerOnDuration", dataType=ns0.datatypes.Duration)),
    ],
)
laser_systems_objtypes.LaserSystemStatusType(
    nodeId="ns=laser_systems;i=5006",
    browseName="ns=laser_systems;LaserSystemStatus",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(o6.ns["ns=laser_systems;i=5007"]),
        o6.hasComponent(o6.ns["ns=laser_systems;i=5020"]),
        o6.hasAddIn(o6.ns["ns=laser_systems;i=5018"]),
        o6.hasAddIn(o6.ns["ns=laser_systems;i=5019"]),
        o6.hasAddIn(o6.ns["ns=laser_systems;i=5021"]),
    ],
)
o6.reference(laser_systems_objtypes.LaserSystemMonitoringType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5006"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=laser_systems;i=6051",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6052", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
laser_systems_objtypes.LaserSystemState_StateMachineType(
    nodeId="ns=laser_systems;i=5023", browseName="ns=laser_systems;LaserSystemState", references=[o6.hasComponent(o6.ns["ns=laser_systems;i=6051"])]
)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=laser_systems;i=6053",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6054", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
machinery.objtypes.MachineryItemState_StateMachineType(
    nodeId="ns=laser_systems;i=5024", browseName="ns=machinery;MachineryItemState", references=[o6.hasComponent(o6.ns["ns=laser_systems;i=6053"])]
)
o6.reference(o6.ns["ns=laser_systems;i=5103"], "i=17604", o6.ns["ns=laser_systems;i=5024"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=laser_systems;i=6055",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6056", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
machinery.objtypes.MachineryOperationModeStateMachineType(
    nodeId="ns=laser_systems;i=5025", browseName="ns=machinery;MachineryOperationMode", references=[o6.hasComponent(o6.ns["ns=laser_systems;i=6055"])]
)
o6.reference(o6.ns["ns=laser_systems;i=5103"], "i=17604", o6.ns["ns=laser_systems;i=5025"])
machine_tool.objtypes.LaserMonitoringType(
    nodeId="ns=laser_systems;i=5026",
    browseName="ns=laser_systems;MachineToolsLaserStatus",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6059", browseName="ns=machine_tool;Name", dataType=o6.String)),
        o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.BaseDataVariableType(nodeId="ns=laser_systems;i=6057", browseName="ns=machine_tool;ControllerIsOn", dataType=o6.Boolean)
        ),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=laser_systems;i=6058", browseName="ns=machine_tool;LaserState", dataType=machine_tool.datatypes.LaserState)),
    ],
)
laser_systems_objtypes.LaserSystemOperationCounterType(
    nodeId="ns=laser_systems;i=5027",
    browseName="ns=di;OperationCounters",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6060", browseName="ns=di;OperationDuration", dataType=ns0.datatypes.Duration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6061", browseName="ns=di;PowerOnDuration", dataType=ns0.datatypes.Duration)),
    ],
)
o6.reference(o6.ns["ns=laser_systems;i=5103"], "i=17604", o6.ns["ns=laser_systems;i=5027"])
laser_systems_objtypes.LaserSystemStatusType(
    nodeId="ns=laser_systems;i=5022",
    browseName="ns=laser_systems;LaserSystemStatus",
    references=[
        o6.hasComponent(o6.ns["ns=laser_systems;i=5023"]),
        o6.hasComponent(o6.ns["ns=laser_systems;i=5026"]),
        o6.hasAddIn(o6.ns["ns=laser_systems;i=5024"]),
        o6.hasAddIn(o6.ns["ns=laser_systems;i=5025"]),
        o6.hasAddIn(o6.ns["ns=laser_systems;i=5027"]),
    ],
)
laser_systems_objtypes.LaserSystemMonitoringType(
    nodeId="ns=laser_systems;i=5004", browseName="ns=laser_systems;Monitoring", modellingRule="Mandatory", references=[o6.hasComponent(o6.ns["ns=laser_systems;i=5022"])]
)
o6.reference(laser_systems_objtypes.LaserSystemType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5004"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=laser_systems;i=6008",
    browseName="ns=laser_systems;UpperWarningLevel",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6063", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
)
o6.reference(laser_systems_objtypes.ConditionDataMonitoringType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=6008"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=laser_systems;i=6064",
    browseName="ns=laser_systems;UpperErrorLevel",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6065", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
)
o6.reference(laser_systems_objtypes.ConditionDataMonitoringType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=6064"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=laser_systems;i=6066",
    browseName="ns=laser_systems;LowerWarningLevel",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6067", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
)
o6.reference(laser_systems_objtypes.ConditionDataMonitoringType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=6066"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=laser_systems;i=6068",
    browseName="ns=laser_systems;LowerErrorLevel",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6069", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
)
o6.reference(laser_systems_objtypes.ConditionDataMonitoringType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=6068"])
ns0.objtypes.StateType(
    nodeId="ns=laser_systems;i=5028",
    browseName="ns=laser_systems;Off",
    description="The laser system is currently off or very close to off",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6080", browseName="StateNumber", dataType=o6.UInt32, value=0))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5028"])
ns0.objtypes.StateType(
    nodeId="ns=laser_systems;i=5029",
    browseName="ns=laser_systems;EnergySaving",
    description="The laser system is actively reducing its energy consumption",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6081", browseName="StateNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5029"])
ns0.objtypes.StateType(
    nodeId="ns=laser_systems;i=5030",
    browseName="ns=laser_systems;Idle",
    description="The laser system is operational but not perusing any activities to achieve the LaserReady state",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6082", browseName="StateNumber", dataType=o6.UInt32, value=2))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5030"])
ns0.objtypes.StateType(
    nodeId="ns=laser_systems;i=5031",
    browseName="ns=laser_systems;SetUp",
    description="The laser system is performing activities to achieve the LaserReady state",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6083", browseName="StateNumber", dataType=o6.UInt32, value=3))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5031"])
ns0.objtypes.StateType(
    nodeId="ns=laser_systems;i=5032",
    browseName="ns=laser_systems;LaserReady",
    description="The laser system is ready and is merely missing a trigger to actively emit radiation",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6084", browseName="StateNumber", dataType=o6.UInt32, value=4))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5032"])
ns0.objtypes.StateType(
    nodeId="ns=laser_systems;i=5033",
    browseName="ns=laser_systems;Maintenance",
    description="The laser system is currently not operational as maintenance is being performed on it",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6085", browseName="StateNumber", dataType=o6.UInt32, value=5))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5033"])
ns0.objtypes.StateType(
    nodeId="ns=laser_systems;i=5034",
    browseName="ns=laser_systems;Error",
    description="The laser system is not operational as it is in an error state",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6086", browseName="StateNumber", dataType=o6.UInt32, value=6))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5034"])
ns0.objtypes.StateType(
    nodeId="ns=laser_systems;i=5035",
    browseName="ns=laser_systems;LaserOn",
    description="The laser system is actively emitting radiation",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6087", browseName="StateNumber", dataType=o6.UInt32, value=7))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5035"])
ns0.objtypes.TransitionType(
    nodeId="ns=laser_systems;i=5036",
    browseName="ns=laser_systems;FromOffToOff",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6088", browseName="TransitionNumber", dataType=o6.UInt32, value=0))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5036"])
o6.reference(o6.ns["ns=laser_systems;i=5036"], "i=51", o6.ns["ns=laser_systems;i=5028"])
o6.reference(o6.ns["ns=laser_systems;i=5036"], "i=52", o6.ns["ns=laser_systems;i=5028"])
ns0.objtypes.TransitionType(
    nodeId="ns=laser_systems;i=5037",
    browseName="ns=laser_systems;FromOffToEnergySaving",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6089", browseName="TransitionNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5037"])
o6.reference(o6.ns["ns=laser_systems;i=5037"], "i=51", o6.ns["ns=laser_systems;i=5028"])
o6.reference(o6.ns["ns=laser_systems;i=5037"], "i=52", o6.ns["ns=laser_systems;i=5029"])
ns0.objtypes.TransitionType(
    nodeId="ns=laser_systems;i=5038",
    browseName="ns=laser_systems;FromOffToIdle",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6090", browseName="TransitionNumber", dataType=o6.UInt32, value=2))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5038"])
o6.reference(o6.ns["ns=laser_systems;i=5038"], "i=51", o6.ns["ns=laser_systems;i=5028"])
o6.reference(o6.ns["ns=laser_systems;i=5038"], "i=52", o6.ns["ns=laser_systems;i=5030"])
ns0.objtypes.TransitionType(
    nodeId="ns=laser_systems;i=5039",
    browseName="ns=laser_systems;FromOffToSetUp",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6091", browseName="TransitionNumber", dataType=o6.UInt32, value=3))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5039"])
o6.reference(o6.ns["ns=laser_systems;i=5039"], "i=51", o6.ns["ns=laser_systems;i=5028"])
o6.reference(o6.ns["ns=laser_systems;i=5039"], "i=52", o6.ns["ns=laser_systems;i=5031"])
ns0.objtypes.TransitionType(
    nodeId="ns=laser_systems;i=5040",
    browseName="ns=laser_systems;FromOffToLaserReady",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6092", browseName="TransitionNumber", dataType=o6.UInt32, value=4))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5040"])
o6.reference(o6.ns["ns=laser_systems;i=5040"], "i=51", o6.ns["ns=laser_systems;i=5028"])
o6.reference(o6.ns["ns=laser_systems;i=5040"], "i=52", o6.ns["ns=laser_systems;i=5032"])
ns0.objtypes.TransitionType(
    nodeId="ns=laser_systems;i=5041",
    browseName="ns=laser_systems;FromOffToMaintenance",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6093", browseName="TransitionNumber", dataType=o6.UInt32, value=5))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5041"])
o6.reference(o6.ns["ns=laser_systems;i=5041"], "i=51", o6.ns["ns=laser_systems;i=5028"])
o6.reference(o6.ns["ns=laser_systems;i=5041"], "i=52", o6.ns["ns=laser_systems;i=5033"])
ns0.objtypes.TransitionType(
    nodeId="ns=laser_systems;i=5042",
    browseName="ns=laser_systems;FromOffToError",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6094", browseName="TransitionNumber", dataType=o6.UInt32, value=6))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5042"])
o6.reference(o6.ns["ns=laser_systems;i=5042"], "i=51", o6.ns["ns=laser_systems;i=5028"])
o6.reference(o6.ns["ns=laser_systems;i=5042"], "i=52", o6.ns["ns=laser_systems;i=5034"])
ns0.objtypes.TransitionType(
    nodeId="ns=laser_systems;i=5043",
    browseName="ns=laser_systems;FromOffToLaserOn",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6095", browseName="TransitionNumber", dataType=o6.UInt32, value=7))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5043"])
o6.reference(o6.ns["ns=laser_systems;i=5043"], "i=51", o6.ns["ns=laser_systems;i=5028"])
o6.reference(o6.ns["ns=laser_systems;i=5043"], "i=52", o6.ns["ns=laser_systems;i=5035"])
ns0.objtypes.TransitionType(
    nodeId="ns=laser_systems;i=5044",
    browseName="ns=laser_systems;FromEnergySavingToOff",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6096", browseName="TransitionNumber", dataType=o6.UInt32, value=8))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5044"])
o6.reference(o6.ns["ns=laser_systems;i=5044"], "i=51", o6.ns["ns=laser_systems;i=5029"])
o6.reference(o6.ns["ns=laser_systems;i=5044"], "i=52", o6.ns["ns=laser_systems;i=5028"])
ns0.objtypes.TransitionType(
    nodeId="ns=laser_systems;i=5045",
    browseName="ns=laser_systems;FromEnergySavingToEnergySaving",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6097", browseName="TransitionNumber", dataType=o6.UInt32, value=9))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5045"])
o6.reference(o6.ns["ns=laser_systems;i=5045"], "i=51", o6.ns["ns=laser_systems;i=5029"])
o6.reference(o6.ns["ns=laser_systems;i=5045"], "i=52", o6.ns["ns=laser_systems;i=5029"])
ns0.objtypes.TransitionType(
    nodeId="ns=laser_systems;i=5046",
    browseName="ns=laser_systems;FromEnergySavingToIdle",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6098", browseName="TransitionNumber", dataType=o6.UInt32, value=10))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5046"])
o6.reference(o6.ns["ns=laser_systems;i=5046"], "i=51", o6.ns["ns=laser_systems;i=5029"])
o6.reference(o6.ns["ns=laser_systems;i=5046"], "i=52", o6.ns["ns=laser_systems;i=5030"])
ns0.objtypes.TransitionType(
    nodeId="ns=laser_systems;i=5047",
    browseName="ns=laser_systems;FromEnergySavingToSetUp",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6099", browseName="TransitionNumber", dataType=o6.UInt32, value=11))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5047"])
o6.reference(o6.ns["ns=laser_systems;i=5047"], "i=51", o6.ns["ns=laser_systems;i=5029"])
o6.reference(o6.ns["ns=laser_systems;i=5047"], "i=52", o6.ns["ns=laser_systems;i=5031"])
ns0.objtypes.TransitionType(
    nodeId="ns=laser_systems;i=5048",
    browseName="ns=laser_systems;FromEnergySavingToLaserReady",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6100", browseName="TransitionNumber", dataType=o6.UInt32, value=12))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5048"])
o6.reference(o6.ns["ns=laser_systems;i=5048"], "i=51", o6.ns["ns=laser_systems;i=5029"])
o6.reference(o6.ns["ns=laser_systems;i=5048"], "i=52", o6.ns["ns=laser_systems;i=5032"])
ns0.objtypes.TransitionType(
    nodeId="ns=laser_systems;i=5049",
    browseName="ns=laser_systems;FromEnergySavingToMaintenance",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6101", browseName="TransitionNumber", dataType=o6.UInt32, value=13))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5049"])
o6.reference(o6.ns["ns=laser_systems;i=5049"], "i=51", o6.ns["ns=laser_systems;i=5029"])
o6.reference(o6.ns["ns=laser_systems;i=5049"], "i=52", o6.ns["ns=laser_systems;i=5033"])
ns0.objtypes.TransitionType(
    nodeId="ns=laser_systems;i=5050",
    browseName="ns=laser_systems;FromEnergySavingToError",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6102", browseName="TransitionNumber", dataType=o6.UInt32, value=14))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5050"])
o6.reference(o6.ns["ns=laser_systems;i=5050"], "i=51", o6.ns["ns=laser_systems;i=5029"])
o6.reference(o6.ns["ns=laser_systems;i=5050"], "i=52", o6.ns["ns=laser_systems;i=5034"])
ns0.objtypes.TransitionType(
    nodeId="ns=laser_systems;i=5051",
    browseName="ns=laser_systems;FromEnergySavingToLaserOn",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6103", browseName="TransitionNumber", dataType=o6.UInt32, value=15))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5051"])
o6.reference(o6.ns["ns=laser_systems;i=5051"], "i=51", o6.ns["ns=laser_systems;i=5029"])
o6.reference(o6.ns["ns=laser_systems;i=5051"], "i=52", o6.ns["ns=laser_systems;i=5035"])
ns0.objtypes.TransitionType(
    nodeId="ns=laser_systems;i=5052",
    browseName="ns=laser_systems;FromIdleToOff",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6104", browseName="TransitionNumber", dataType=o6.UInt32, value=16))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5052"])
o6.reference(o6.ns["ns=laser_systems;i=5052"], "i=51", o6.ns["ns=laser_systems;i=5030"])
o6.reference(o6.ns["ns=laser_systems;i=5052"], "i=52", o6.ns["ns=laser_systems;i=5028"])
ns0.objtypes.TransitionType(
    nodeId="ns=laser_systems;i=5053",
    browseName="ns=laser_systems;FromIdleToEnergySaving",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6105", browseName="TransitionNumber", dataType=o6.UInt32, value=17))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5053"])
o6.reference(o6.ns["ns=laser_systems;i=5053"], "i=51", o6.ns["ns=laser_systems;i=5030"])
o6.reference(o6.ns["ns=laser_systems;i=5053"], "i=52", o6.ns["ns=laser_systems;i=5029"])
ns0.objtypes.TransitionType(
    nodeId="ns=laser_systems;i=5054",
    browseName="ns=laser_systems;FromIdleToIdle",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6106", browseName="TransitionNumber", dataType=o6.UInt32, value=18))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5054"])
o6.reference(o6.ns["ns=laser_systems;i=5054"], "i=51", o6.ns["ns=laser_systems;i=5030"])
o6.reference(o6.ns["ns=laser_systems;i=5054"], "i=52", o6.ns["ns=laser_systems;i=5030"])
ns0.objtypes.TransitionType(
    nodeId="ns=laser_systems;i=5055",
    browseName="ns=laser_systems;FromIdleToSetUp",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6107", browseName="TransitionNumber", dataType=o6.UInt32, value=19))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5055"])
o6.reference(o6.ns["ns=laser_systems;i=5055"], "i=51", o6.ns["ns=laser_systems;i=5030"])
o6.reference(o6.ns["ns=laser_systems;i=5055"], "i=52", o6.ns["ns=laser_systems;i=5031"])
ns0.objtypes.TransitionType(
    nodeId="ns=laser_systems;i=5056",
    browseName="ns=laser_systems;FromIdleToLaserReady",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6108", browseName="TransitionNumber", dataType=o6.UInt32, value=20))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5056"])
o6.reference(o6.ns["ns=laser_systems;i=5056"], "i=51", o6.ns["ns=laser_systems;i=5030"])
o6.reference(o6.ns["ns=laser_systems;i=5056"], "i=52", o6.ns["ns=laser_systems;i=5032"])
ns0.objtypes.TransitionType(
    nodeId="ns=laser_systems;i=5057",
    browseName="ns=laser_systems;FromIdleToMaintenance",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6109", browseName="TransitionNumber", dataType=o6.UInt32, value=21))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5057"])
o6.reference(o6.ns["ns=laser_systems;i=5057"], "i=51", o6.ns["ns=laser_systems;i=5030"])
o6.reference(o6.ns["ns=laser_systems;i=5057"], "i=52", o6.ns["ns=laser_systems;i=5033"])
ns0.objtypes.TransitionType(
    nodeId="ns=laser_systems;i=5058",
    browseName="ns=laser_systems;FromIdleToError",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6110", browseName="TransitionNumber", dataType=o6.UInt32, value=22))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5058"])
o6.reference(o6.ns["ns=laser_systems;i=5058"], "i=51", o6.ns["ns=laser_systems;i=5030"])
o6.reference(o6.ns["ns=laser_systems;i=5058"], "i=52", o6.ns["ns=laser_systems;i=5034"])
ns0.objtypes.TransitionType(
    nodeId="ns=laser_systems;i=5059",
    browseName="ns=laser_systems;FromIdleToLaserOn",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6111", browseName="TransitionNumber", dataType=o6.UInt32, value=23))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5059"])
o6.reference(o6.ns["ns=laser_systems;i=5059"], "i=51", o6.ns["ns=laser_systems;i=5030"])
o6.reference(o6.ns["ns=laser_systems;i=5059"], "i=52", o6.ns["ns=laser_systems;i=5035"])
ns0.objtypes.TransitionType(
    nodeId="ns=laser_systems;i=5060",
    browseName="ns=laser_systems;FromSetUpToOff",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6112", browseName="TransitionNumber", dataType=o6.UInt32, value=24))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5060"])
o6.reference(o6.ns["ns=laser_systems;i=5060"], "i=51", o6.ns["ns=laser_systems;i=5031"])
o6.reference(o6.ns["ns=laser_systems;i=5060"], "i=52", o6.ns["ns=laser_systems;i=5028"])
ns0.objtypes.TransitionType(
    nodeId="ns=laser_systems;i=5061",
    browseName="ns=laser_systems;FromSetUpToEnergySaving",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6113", browseName="TransitionNumber", dataType=o6.UInt32, value=25))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5061"])
o6.reference(o6.ns["ns=laser_systems;i=5061"], "i=51", o6.ns["ns=laser_systems;i=5031"])
o6.reference(o6.ns["ns=laser_systems;i=5061"], "i=52", o6.ns["ns=laser_systems;i=5029"])
ns0.objtypes.TransitionType(
    nodeId="ns=laser_systems;i=5062",
    browseName="ns=laser_systems;FromSetUpToIdle",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6114", browseName="TransitionNumber", dataType=o6.UInt32, value=26))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5062"])
o6.reference(o6.ns["ns=laser_systems;i=5062"], "i=51", o6.ns["ns=laser_systems;i=5031"])
o6.reference(o6.ns["ns=laser_systems;i=5062"], "i=52", o6.ns["ns=laser_systems;i=5030"])
ns0.objtypes.TransitionType(
    nodeId="ns=laser_systems;i=5063",
    browseName="ns=laser_systems;FromSetUpToSetUp",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6115", browseName="TransitionNumber", dataType=o6.UInt32, value=27))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5063"])
o6.reference(o6.ns["ns=laser_systems;i=5063"], "i=51", o6.ns["ns=laser_systems;i=5031"])
o6.reference(o6.ns["ns=laser_systems;i=5063"], "i=52", o6.ns["ns=laser_systems;i=5031"])
ns0.objtypes.TransitionType(
    nodeId="ns=laser_systems;i=5064",
    browseName="ns=laser_systems;FromSetUpToLaserReady",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6116", browseName="TransitionNumber", dataType=o6.UInt32, value=28))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5064"])
o6.reference(o6.ns["ns=laser_systems;i=5064"], "i=51", o6.ns["ns=laser_systems;i=5031"])
o6.reference(o6.ns["ns=laser_systems;i=5064"], "i=52", o6.ns["ns=laser_systems;i=5032"])
ns0.objtypes.TransitionType(
    nodeId="ns=laser_systems;i=5065",
    browseName="ns=laser_systems;FromSetUpToMaintenance",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6117", browseName="TransitionNumber", dataType=o6.UInt32, value=29))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5065"])
o6.reference(o6.ns["ns=laser_systems;i=5065"], "i=51", o6.ns["ns=laser_systems;i=5031"])
o6.reference(o6.ns["ns=laser_systems;i=5065"], "i=52", o6.ns["ns=laser_systems;i=5033"])
ns0.objtypes.TransitionType(
    nodeId="ns=laser_systems;i=5066",
    browseName="ns=laser_systems;FromSetUpToError",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6118", browseName="TransitionNumber", dataType=o6.UInt32, value=30))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5066"])
o6.reference(o6.ns["ns=laser_systems;i=5066"], "i=51", o6.ns["ns=laser_systems;i=5031"])
o6.reference(o6.ns["ns=laser_systems;i=5066"], "i=52", o6.ns["ns=laser_systems;i=5034"])
ns0.objtypes.TransitionType(
    nodeId="ns=laser_systems;i=5067",
    browseName="ns=laser_systems;FromSetUpToLaserOn",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6119", browseName="TransitionNumber", dataType=o6.UInt32, value=31))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5067"])
o6.reference(o6.ns["ns=laser_systems;i=5067"], "i=51", o6.ns["ns=laser_systems;i=5031"])
o6.reference(o6.ns["ns=laser_systems;i=5067"], "i=52", o6.ns["ns=laser_systems;i=5035"])
ns0.objtypes.TransitionType(
    nodeId="ns=laser_systems;i=5069",
    browseName="ns=laser_systems;FromLaserReadyToOff",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6120", browseName="TransitionNumber", dataType=o6.UInt32, value=32))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5069"])
o6.reference(o6.ns["ns=laser_systems;i=5069"], "i=51", o6.ns["ns=laser_systems;i=5032"])
o6.reference(o6.ns["ns=laser_systems;i=5069"], "i=52", o6.ns["ns=laser_systems;i=5028"])
ns0.objtypes.TransitionType(
    nodeId="ns=laser_systems;i=5070",
    browseName="ns=laser_systems;FromLaserReadyToEnergySaving",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6121", browseName="TransitionNumber", dataType=o6.UInt32, value=33))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5070"])
o6.reference(o6.ns["ns=laser_systems;i=5070"], "i=51", o6.ns["ns=laser_systems;i=5032"])
o6.reference(o6.ns["ns=laser_systems;i=5070"], "i=52", o6.ns["ns=laser_systems;i=5029"])
ns0.objtypes.TransitionType(
    nodeId="ns=laser_systems;i=5071",
    browseName="ns=laser_systems;FromLaserReadyToIdle",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6122", browseName="TransitionNumber", dataType=o6.UInt32, value=34))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5071"])
o6.reference(o6.ns["ns=laser_systems;i=5071"], "i=51", o6.ns["ns=laser_systems;i=5032"])
o6.reference(o6.ns["ns=laser_systems;i=5071"], "i=52", o6.ns["ns=laser_systems;i=5030"])
ns0.objtypes.TransitionType(
    nodeId="ns=laser_systems;i=5072",
    browseName="ns=laser_systems;FromLaserReadyToSetUp",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6123", browseName="TransitionNumber", dataType=o6.UInt32, value=35))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5072"])
o6.reference(o6.ns["ns=laser_systems;i=5072"], "i=51", o6.ns["ns=laser_systems;i=5032"])
o6.reference(o6.ns["ns=laser_systems;i=5072"], "i=52", o6.ns["ns=laser_systems;i=5031"])
ns0.objtypes.TransitionType(
    nodeId="ns=laser_systems;i=5073",
    browseName="ns=laser_systems;FromLaserReadyToLaserReady",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6124", browseName="TransitionNumber", dataType=o6.UInt32, value=36))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5073"])
o6.reference(o6.ns["ns=laser_systems;i=5073"], "i=51", o6.ns["ns=laser_systems;i=5032"])
o6.reference(o6.ns["ns=laser_systems;i=5073"], "i=52", o6.ns["ns=laser_systems;i=5032"])
ns0.objtypes.TransitionType(
    nodeId="ns=laser_systems;i=5074",
    browseName="ns=laser_systems;FromLaserReadyToMaintenance",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6125", browseName="TransitionNumber", dataType=o6.UInt32, value=37))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5074"])
o6.reference(o6.ns["ns=laser_systems;i=5074"], "i=51", o6.ns["ns=laser_systems;i=5032"])
o6.reference(o6.ns["ns=laser_systems;i=5074"], "i=52", o6.ns["ns=laser_systems;i=5033"])
ns0.objtypes.TransitionType(
    nodeId="ns=laser_systems;i=5075",
    browseName="ns=laser_systems;FromLaserReadyToError",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6126", browseName="TransitionNumber", dataType=o6.UInt32, value=38))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5075"])
o6.reference(o6.ns["ns=laser_systems;i=5075"], "i=51", o6.ns["ns=laser_systems;i=5032"])
o6.reference(o6.ns["ns=laser_systems;i=5075"], "i=52", o6.ns["ns=laser_systems;i=5034"])
ns0.objtypes.TransitionType(
    nodeId="ns=laser_systems;i=5076",
    browseName="ns=laser_systems;FromLaserReadyToLaserOn",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6127", browseName="TransitionNumber", dataType=o6.UInt32, value=39))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5076"])
o6.reference(o6.ns["ns=laser_systems;i=5076"], "i=51", o6.ns["ns=laser_systems;i=5032"])
o6.reference(o6.ns["ns=laser_systems;i=5076"], "i=52", o6.ns["ns=laser_systems;i=5035"])
ns0.objtypes.TransitionType(
    nodeId="ns=laser_systems;i=5077",
    browseName="ns=laser_systems;FromMaintenanceToOff",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6128", browseName="TransitionNumber", dataType=o6.UInt32, value=40))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5077"])
o6.reference(o6.ns["ns=laser_systems;i=5077"], "i=51", o6.ns["ns=laser_systems;i=5033"])
o6.reference(o6.ns["ns=laser_systems;i=5077"], "i=52", o6.ns["ns=laser_systems;i=5028"])
ns0.objtypes.TransitionType(
    nodeId="ns=laser_systems;i=5078",
    browseName="ns=laser_systems;FromMaintenanceToEnergySaving",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6129", browseName="TransitionNumber", dataType=o6.UInt32, value=41))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5078"])
o6.reference(o6.ns["ns=laser_systems;i=5078"], "i=51", o6.ns["ns=laser_systems;i=5033"])
o6.reference(o6.ns["ns=laser_systems;i=5078"], "i=52", o6.ns["ns=laser_systems;i=5029"])
ns0.objtypes.TransitionType(
    nodeId="ns=laser_systems;i=5079",
    browseName="ns=laser_systems;FromMaintenanceToIdle",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6130", browseName="TransitionNumber", dataType=o6.UInt32, value=42))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5079"])
o6.reference(o6.ns["ns=laser_systems;i=5079"], "i=51", o6.ns["ns=laser_systems;i=5033"])
o6.reference(o6.ns["ns=laser_systems;i=5079"], "i=52", o6.ns["ns=laser_systems;i=5030"])
ns0.objtypes.TransitionType(
    nodeId="ns=laser_systems;i=5080",
    browseName="ns=laser_systems;FromMaintenanceToSetUp",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6131", browseName="TransitionNumber", dataType=o6.UInt32, value=43))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5080"])
o6.reference(o6.ns["ns=laser_systems;i=5080"], "i=51", o6.ns["ns=laser_systems;i=5033"])
o6.reference(o6.ns["ns=laser_systems;i=5080"], "i=52", o6.ns["ns=laser_systems;i=5031"])
ns0.objtypes.TransitionType(
    nodeId="ns=laser_systems;i=5081",
    browseName="ns=laser_systems;FromMaintenanceToLaserReady",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6132", browseName="TransitionNumber", dataType=o6.UInt32, value=44))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5081"])
o6.reference(o6.ns["ns=laser_systems;i=5081"], "i=51", o6.ns["ns=laser_systems;i=5033"])
o6.reference(o6.ns["ns=laser_systems;i=5081"], "i=52", o6.ns["ns=laser_systems;i=5032"])
ns0.objtypes.TransitionType(
    nodeId="ns=laser_systems;i=5082",
    browseName="ns=laser_systems;FromMaintenanceToMaintenance",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6133", browseName="TransitionNumber", dataType=o6.UInt32, value=45))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5082"])
o6.reference(o6.ns["ns=laser_systems;i=5082"], "i=51", o6.ns["ns=laser_systems;i=5033"])
o6.reference(o6.ns["ns=laser_systems;i=5082"], "i=52", o6.ns["ns=laser_systems;i=5033"])
ns0.objtypes.TransitionType(
    nodeId="ns=laser_systems;i=5083",
    browseName="ns=laser_systems;FromMaintenanceToError",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6134", browseName="TransitionNumber", dataType=o6.UInt32, value=46))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5083"])
o6.reference(o6.ns["ns=laser_systems;i=5083"], "i=51", o6.ns["ns=laser_systems;i=5033"])
o6.reference(o6.ns["ns=laser_systems;i=5083"], "i=52", o6.ns["ns=laser_systems;i=5034"])
ns0.objtypes.TransitionType(
    nodeId="ns=laser_systems;i=5084",
    browseName="ns=laser_systems;FromMaintenanceToLaserOn",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6135", browseName="TransitionNumber", dataType=o6.UInt32, value=47))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5084"])
o6.reference(o6.ns["ns=laser_systems;i=5084"], "i=51", o6.ns["ns=laser_systems;i=5033"])
o6.reference(o6.ns["ns=laser_systems;i=5084"], "i=52", o6.ns["ns=laser_systems;i=5035"])
ns0.objtypes.TransitionType(
    nodeId="ns=laser_systems;i=5085",
    browseName="ns=laser_systems;FromErrorToOff",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6136", browseName="TransitionNumber", dataType=o6.UInt32, value=48))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5085"])
o6.reference(o6.ns["ns=laser_systems;i=5085"], "i=51", o6.ns["ns=laser_systems;i=5034"])
o6.reference(o6.ns["ns=laser_systems;i=5085"], "i=52", o6.ns["ns=laser_systems;i=5028"])
ns0.objtypes.TransitionType(
    nodeId="ns=laser_systems;i=5086",
    browseName="ns=laser_systems;FromErrorToEnergySaving",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6137", browseName="TransitionNumber", dataType=o6.UInt32, value=49))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5086"])
o6.reference(o6.ns["ns=laser_systems;i=5086"], "i=51", o6.ns["ns=laser_systems;i=5034"])
o6.reference(o6.ns["ns=laser_systems;i=5086"], "i=52", o6.ns["ns=laser_systems;i=5029"])
ns0.objtypes.TransitionType(
    nodeId="ns=laser_systems;i=5087",
    browseName="ns=laser_systems;FromErrorToIdle",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6138", browseName="TransitionNumber", dataType=o6.UInt32, value=50))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5087"])
o6.reference(o6.ns["ns=laser_systems;i=5087"], "i=51", o6.ns["ns=laser_systems;i=5034"])
o6.reference(o6.ns["ns=laser_systems;i=5087"], "i=52", o6.ns["ns=laser_systems;i=5030"])
ns0.objtypes.TransitionType(
    nodeId="ns=laser_systems;i=5088",
    browseName="ns=laser_systems;FromErrorToSetUp",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6139", browseName="TransitionNumber", dataType=o6.UInt32, value=51))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5088"])
o6.reference(o6.ns["ns=laser_systems;i=5088"], "i=51", o6.ns["ns=laser_systems;i=5034"])
o6.reference(o6.ns["ns=laser_systems;i=5088"], "i=52", o6.ns["ns=laser_systems;i=5031"])
ns0.objtypes.TransitionType(
    nodeId="ns=laser_systems;i=5089",
    browseName="ns=laser_systems;FromErrorToLaserReady",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6140", browseName="TransitionNumber", dataType=o6.UInt32, value=52))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5089"])
o6.reference(o6.ns["ns=laser_systems;i=5089"], "i=51", o6.ns["ns=laser_systems;i=5034"])
o6.reference(o6.ns["ns=laser_systems;i=5089"], "i=52", o6.ns["ns=laser_systems;i=5032"])
ns0.objtypes.TransitionType(
    nodeId="ns=laser_systems;i=5090",
    browseName="ns=laser_systems;FromErrorToMaintenance",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6141", browseName="TransitionNumber", dataType=o6.UInt32, value=53))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5090"])
o6.reference(o6.ns["ns=laser_systems;i=5090"], "i=51", o6.ns["ns=laser_systems;i=5034"])
o6.reference(o6.ns["ns=laser_systems;i=5090"], "i=52", o6.ns["ns=laser_systems;i=5033"])
ns0.objtypes.TransitionType(
    nodeId="ns=laser_systems;i=5091",
    browseName="ns=laser_systems;FromErrorToError",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6142", browseName="TransitionNumber", dataType=o6.UInt32, value=54))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5091"])
o6.reference(o6.ns["ns=laser_systems;i=5091"], "i=51", o6.ns["ns=laser_systems;i=5034"])
o6.reference(o6.ns["ns=laser_systems;i=5091"], "i=52", o6.ns["ns=laser_systems;i=5034"])
ns0.objtypes.TransitionType(
    nodeId="ns=laser_systems;i=5092",
    browseName="ns=laser_systems;FromErrorToLaserOn",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6143", browseName="TransitionNumber", dataType=o6.UInt32, value=55))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5092"])
o6.reference(o6.ns["ns=laser_systems;i=5092"], "i=51", o6.ns["ns=laser_systems;i=5034"])
o6.reference(o6.ns["ns=laser_systems;i=5092"], "i=52", o6.ns["ns=laser_systems;i=5035"])
ns0.objtypes.TransitionType(
    nodeId="ns=laser_systems;i=5093",
    browseName="ns=laser_systems;FromLaserOnToOff",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6144", browseName="TransitionNumber", dataType=o6.UInt32, value=56))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5093"])
o6.reference(o6.ns["ns=laser_systems;i=5093"], "i=51", o6.ns["ns=laser_systems;i=5035"])
o6.reference(o6.ns["ns=laser_systems;i=5093"], "i=52", o6.ns["ns=laser_systems;i=5028"])
ns0.objtypes.TransitionType(
    nodeId="ns=laser_systems;i=5094",
    browseName="ns=laser_systems;FromLaserOnToEnergySaving",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6145", browseName="TransitionNumber", dataType=o6.UInt32, value=57))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5094"])
o6.reference(o6.ns["ns=laser_systems;i=5094"], "i=51", o6.ns["ns=laser_systems;i=5035"])
o6.reference(o6.ns["ns=laser_systems;i=5094"], "i=52", o6.ns["ns=laser_systems;i=5029"])
ns0.objtypes.TransitionType(
    nodeId="ns=laser_systems;i=5095",
    browseName="ns=laser_systems;FromLaserOnToIdle",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6146", browseName="TransitionNumber", dataType=o6.UInt32, value=58))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5095"])
o6.reference(o6.ns["ns=laser_systems;i=5095"], "i=51", o6.ns["ns=laser_systems;i=5035"])
o6.reference(o6.ns["ns=laser_systems;i=5095"], "i=52", o6.ns["ns=laser_systems;i=5030"])
ns0.objtypes.TransitionType(
    nodeId="ns=laser_systems;i=5096",
    browseName="ns=laser_systems;FromLaserOnToSetUp",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6147", browseName="TransitionNumber", dataType=o6.UInt32, value=59))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5096"])
o6.reference(o6.ns["ns=laser_systems;i=5096"], "i=51", o6.ns["ns=laser_systems;i=5035"])
o6.reference(o6.ns["ns=laser_systems;i=5096"], "i=52", o6.ns["ns=laser_systems;i=5031"])
ns0.objtypes.TransitionType(
    nodeId="ns=laser_systems;i=5097",
    browseName="ns=laser_systems;FromLaserOnToLaserReady",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6148", browseName="TransitionNumber", dataType=o6.UInt32, value=60))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5097"])
o6.reference(o6.ns["ns=laser_systems;i=5097"], "i=51", o6.ns["ns=laser_systems;i=5035"])
o6.reference(o6.ns["ns=laser_systems;i=5097"], "i=52", o6.ns["ns=laser_systems;i=5032"])
ns0.objtypes.TransitionType(
    nodeId="ns=laser_systems;i=5098",
    browseName="ns=laser_systems;FromLaserOnToMaintenance",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6149", browseName="TransitionNumber", dataType=o6.UInt32, value=61))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5098"])
o6.reference(o6.ns["ns=laser_systems;i=5098"], "i=51", o6.ns["ns=laser_systems;i=5035"])
o6.reference(o6.ns["ns=laser_systems;i=5098"], "i=52", o6.ns["ns=laser_systems;i=5033"])
ns0.objtypes.TransitionType(
    nodeId="ns=laser_systems;i=5099",
    browseName="ns=laser_systems;FromLaserOnToError",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6150", browseName="TransitionNumber", dataType=o6.UInt32, value=62))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5099"])
o6.reference(o6.ns["ns=laser_systems;i=5099"], "i=51", o6.ns["ns=laser_systems;i=5035"])
o6.reference(o6.ns["ns=laser_systems;i=5099"], "i=52", o6.ns["ns=laser_systems;i=5034"])
ns0.objtypes.TransitionType(
    nodeId="ns=laser_systems;i=5100",
    browseName="ns=laser_systems;FromLaserOnToLaserOn",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6151", browseName="TransitionNumber", dataType=o6.UInt32, value=63))],
)
o6.reference(laser_systems_objtypes.LaserSystemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5100"])
o6.reference(o6.ns["ns=laser_systems;i=5100"], "i=51", o6.ns["ns=laser_systems;i=5035"])
o6.reference(o6.ns["ns=laser_systems;i=5100"], "i=52", o6.ns["ns=laser_systems;i=5035"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=laser_systems;i=6153",
    browseName="ns=laser_systems;CurrentValue",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6154", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
)
laser_systems_objtypes.ActivityDataMonitoringType(
    nodeId="ns=laser_systems;i=5003",
    browseName="ns=laser_systems;<ActivityData>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6025", browseName="NumberInList", dataType=o6.UInt16, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6026", browseName="ns=machine_tool;Name", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6155", browseName="ns=laser_systems;ParameterIdentifier", dataType=o6.String, value="ID987")),
        o6.hasComponent(o6.ns["ns=laser_systems;i=6153"]),
    ],
)
ns0.objtypes.OrderedListType(
    nodeId="ns=laser_systems;i=5008", browseName="ns=laser_systems;ActivityData", modellingRule="Optional", references=[o6.hasOrderedComponent(o6.ns["ns=laser_systems;i=5003"])]
)
o6.reference(laser_systems_objtypes.LaserSystemMonitoringType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5008"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=laser_systems;i=6159",
    browseName="ns=laser_systems;Value",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6160", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
)
laser_systems_objtypes.ConditionDataMonitoringType(
    nodeId="ns=laser_systems;i=5101",
    browseName="ns=laser_systems;<ConditionData>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6158", browseName="ns=laser_systems;ConditionParameterIdentifier", dataType=o6.String, value="ID123")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6161", browseName="ns=machine_tool;Name", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=laser_systems;i=6159"]),
    ],
)
ns0.objtypes.FolderType(
    nodeId="ns=laser_systems;i=5009", browseName="ns=laser_systems;ConditionData", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=laser_systems;i=5101"])]
)
o6.reference(laser_systems_objtypes.LaserSystemMonitoringType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5009"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=laser_systems;i=6163",
    browseName="ns=laser_systems;Value",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6164", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
)
laser_systems_objtypes.ConsumptionDataMonitoringType(
    nodeId="ns=laser_systems;i=5102",
    browseName="ns=laser_systems;<ConsumptionData>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6162", browseName="ns=laser_systems;ConsumableIdentifier", dataType=o6.String, value="ID 321")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6165", browseName="ns=machine_tool;Name", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=laser_systems;i=6163"]),
    ],
)
ns0.objtypes.FolderType(
    nodeId="ns=laser_systems;i=5010", browseName="ns=laser_systems;ConsumptionData", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=laser_systems;i=5102"])]
)
o6.reference(laser_systems_objtypes.LaserSystemMonitoringType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5010"])
laser_systems_objtypes.RecipeSettingsAndOverviewType(
    nodeId="ns=laser_systems;i=5104",
    browseName="ns=laser_systems;<Recipe>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6166", browseName="ns=laser_systems;LastModification", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6167", browseName="ns=laser_systems;LastUsage", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6168", browseName="ns=laser_systems;RecipeIdentifier", dataType=o6.String)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=laser_systems;i=6169", browseName="ns=laser_systems;RunsCompleted", dataType=o6.UInt64)),
    ],
)
ns0.objtypes.FolderType(
    nodeId="ns=laser_systems;i=5068",
    browseName="ns=laser_systems;RecipeSettingsAndOverviews",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=laser_systems;i=5104"])],
)
o6.reference(laser_systems_objtypes.LaserSystemProductionType, ns0.reftypes.HasComponent, o6.ns["ns=laser_systems;i=5068"])
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashLaserSystemsSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=laser_systems;i=5105",
    browseName="ns=laser_systems;http://opcfoundation.org/UA/LaserSystems/",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6156", browseName="IsNamespaceSubset", dataType=o6.Boolean)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6157", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2024-02-01T00:00:00Z"))
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6170", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/LaserSystems/")
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6171", browseName="NamespaceVersion", dataType=o6.String, value="1.0.0")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=laser_systems;i=6172",
                browseName="StaticNodeIdTypes",
                dataType=ns0.datatypes.IdType,
                valueRank=1,
                arrayDimensions=[1],
                value=[ns0.datatypes.IdType.NUMERIC],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=laser_systems;i=6173", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6174", browseName="StaticStringNodeIdPattern", dataType=o6.String)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)


del Any, TYPE_CHECKING, uuid, o6, di, ia, isa95_jobcontrol_v2, machine_tool, machinery, machinery_jobs, ns0, laser_systems_objtypes
