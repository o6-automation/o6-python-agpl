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

"""Generated OPC UA robotics namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.ns0 as ns0
from . import reftypes as robotics_reftypes
from . import datatypes as robotics_datypes
from . import objtypes as robotics_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.vartypes.FiniteTransitionVariableType(
    nodeId="ns=robotics;i=6005",
    browseName="LastTransition",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6006", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
o6.reference(robotics_objtypes.OperationStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=6005"])
ns0.objtypes.StateType(
    nodeId="ns=robotics;i=5005",
    browseName="ns=robotics;Idle",
    description="Entity is not in a condition to start execution.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6010", browseName="StateNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(robotics_objtypes.OperationStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=5005"])
ns0.objtypes.StateType(
    nodeId="ns=robotics;i=5006",
    browseName="ns=robotics;Ready",
    description="Entity is in a condition to start execution.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6011", browseName="StateNumber", dataType=o6.UInt32, value=2))],
)
o6.reference(robotics_objtypes.OperationStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=5006"])
ns0.objtypes.StateType(
    nodeId="ns=robotics;i=5007",
    browseName="ns=robotics;Executing",
    description="Entity is in a condition of execution.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6012", browseName="StateNumber", dataType=o6.UInt32, value=3))],
)
o6.reference(robotics_objtypes.OperationStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=5007"])
ns0.objtypes.TransitionType(
    nodeId="ns=robotics;i=5008",
    browseName="ns=robotics;ReadyToIdle",
    description="Changes from Ready to Idle",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6014", browseName="TransitionNumber", dataType=o6.UInt32, value=3))],
)
o6.reference(robotics_objtypes.OperationStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=5008"])
o6.reference(o6.ns["ns=robotics;i=5008"], "i=51", o6.ns["ns=robotics;i=5006"])
o6.reference(o6.ns["ns=robotics;i=5008"], "i=52", o6.ns["ns=robotics;i=5005"])
o6.reference(o6.ns["ns=robotics;i=5008"], "i=54", "i=2311")
ns0.objtypes.TransitionType(
    nodeId="ns=robotics;i=5009",
    browseName="ns=robotics;IdleToReady",
    description="Changes from Idle to Ready",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6015", browseName="TransitionNumber", dataType=o6.UInt32, value=2))],
)
o6.reference(robotics_objtypes.OperationStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=5009"])
o6.reference(o6.ns["ns=robotics;i=5009"], "i=51", o6.ns["ns=robotics;i=5005"])
o6.reference(o6.ns["ns=robotics;i=5009"], "i=52", o6.ns["ns=robotics;i=5006"])
o6.reference(o6.ns["ns=robotics;i=5009"], "i=54", "i=2311")
ns0.objtypes.TransitionType(
    nodeId="ns=robotics;i=5011",
    browseName="ns=robotics;ExecutingToReady",
    description="Changes from Executing to Ready",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6016", browseName="TransitionNumber", dataType=o6.UInt32, value=5))],
)
o6.reference(robotics_objtypes.OperationStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=5011"])
o6.reference(o6.ns["ns=robotics;i=5011"], "i=51", o6.ns["ns=robotics;i=5007"])
o6.reference(o6.ns["ns=robotics;i=5011"], "i=52", o6.ns["ns=robotics;i=5006"])
o6.reference(o6.ns["ns=robotics;i=5011"], "i=53", o6.ns["ns=robotics;i=7002"])
o6.reference(o6.ns["ns=robotics;i=5011"], "i=54", "i=2311")
ns0.objtypes.TransitionType(
    nodeId="ns=robotics;i=5012",
    browseName="ns=robotics;ReadyToExecuting",
    description="Changes from Ready to Executing",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6017", browseName="TransitionNumber", dataType=o6.UInt32, value=4))],
)
o6.reference(robotics_objtypes.OperationStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=5012"])
o6.reference(o6.ns["ns=robotics;i=5012"], "i=51", o6.ns["ns=robotics;i=5006"])
o6.reference(o6.ns["ns=robotics;i=5012"], "i=52", o6.ns["ns=robotics;i=5007"])
o6.reference(o6.ns["ns=robotics;i=5012"], "i=53", o6.ns["ns=robotics;i=7001"])
o6.reference(o6.ns["ns=robotics;i=5012"], "i=54", "i=2311")
ns0.objtypes.TransitionType(
    nodeId="ns=robotics;i=5013",
    browseName="ns=robotics;ExecutingToIdle",
    description="Changes from Executing to Idle",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6018", browseName="TransitionNumber", dataType=o6.UInt32, value=6))],
)
o6.reference(robotics_objtypes.OperationStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=5013"])
o6.reference(o6.ns["ns=robotics;i=5013"], "i=51", o6.ns["ns=robotics;i=5007"])
o6.reference(o6.ns["ns=robotics;i=5013"], "i=52", o6.ns["ns=robotics;i=5005"])
o6.reference(o6.ns["ns=robotics;i=5013"], "i=54", "i=2311")
ns0.objtypes.TransitionType(
    nodeId="ns=robotics;i=5014",
    browseName="ns=robotics;IdleToIdle",
    description="Changes from Idle to Idle.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6019", browseName="TransitionNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(robotics_objtypes.OperationStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=5014"])
o6.reference(o6.ns["ns=robotics;i=5014"], "i=51", o6.ns["ns=robotics;i=5005"])
o6.reference(o6.ns["ns=robotics;i=5014"], "i=52", o6.ns["ns=robotics;i=5005"])
o6.reference(o6.ns["ns=robotics;i=5014"], "i=54", "i=2311")
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=robotics;i=6007",
    browseName="ns=robotics;LastTransitionReason",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=robotics;i=6020",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[6],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Unknown", "en"), description=o6.LocalizedText("Caused by an unknown reason", "en")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("External", "en"), description=o6.LocalizedText("Caused by external operation", "en")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Direct", "en"), description=o6.LocalizedText("Caused by direct operation", "en")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("System", "en"), description=o6.LocalizedText("Caused by system specific behavior", "en")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("Error", "en"), description=o6.LocalizedText("Caused by an error", "en")),
                    ns0.datatypes.EnumValueType(
                        value=5, displayName=o6.LocalizedText("Application", "en"), description=o6.LocalizedText("Caused explicitly by end user program logic", "en")
                    ),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6021", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.Int16,
    accessLevel=3,
)
o6.reference(robotics_objtypes.OperationStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=6007"])
ns0.vartypes.PropertyType(
    nodeId="ns=robotics;i=6022",
    browseName="EnumStrings",
    parent="ns=robotics;i=3006",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        o6.LocalizedText("OTHER"),
        o6.LocalizedText("MANUAL_REDUCED_SPEED"),
        o6.LocalizedText("MANUAL_HIGH_SPEED"),
        o6.LocalizedText("AUTOMATIC"),
        o6.LocalizedText("AUTOMATIC_EXTERNAL"),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=robotics;i=6027",
    browseName="EnumStrings",
    parent="ns=robotics;i=3008",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[5],
    value=[o6.LocalizedText("OTHER"), o6.LocalizedText("ROTARY"), o6.LocalizedText("ROTARY_ENDLESS"), o6.LocalizedText("LINEAR"), o6.LocalizedText("LINEAR_ENDLESS")],
)
ns0.vartypes.FiniteTransitionVariableType(
    nodeId="ns=robotics;i=6026",
    browseName="LastTransition",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6028", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
o6.reference(robotics_objtypes.IdleSubstateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=6026"])
ns0.objtypes.InitialStateType(
    nodeId="ns=robotics;i=5015",
    browseName="ns=robotics;StandBy",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6030", browseName="StateNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(robotics_objtypes.IdleSubstateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=5015"])
ns0.objtypes.StateType(
    nodeId="ns=robotics;i=5017",
    browseName="ns=robotics;GettingReady",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6031", browseName="StateNumber", dataType=o6.UInt32, value=2))],
)
o6.reference(robotics_objtypes.IdleSubstateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=5017"])
ns0.objtypes.TransitionType(
    nodeId="ns=robotics;i=5018",
    browseName="ns=robotics;GettingReadyToStandBy",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6032", browseName="TransitionNumber", dataType=o6.UInt32, value=2))],
)
o6.reference(robotics_objtypes.IdleSubstateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=5018"])
o6.reference(o6.ns["ns=robotics;i=5018"], "i=51", o6.ns["ns=robotics;i=5017"])
o6.reference(o6.ns["ns=robotics;i=5018"], "i=52", o6.ns["ns=robotics;i=5015"])
o6.reference(o6.ns["ns=robotics;i=5018"], "i=54", "i=2311")
ns0.objtypes.TransitionType(
    nodeId="ns=robotics;i=5019",
    browseName="ns=robotics;StandByToGettingReady",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6033", browseName="TransitionNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(robotics_objtypes.IdleSubstateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=5019"])
o6.reference(o6.ns["ns=robotics;i=5019"], "i=51", o6.ns["ns=robotics;i=5015"])
o6.reference(o6.ns["ns=robotics;i=5019"], "i=52", o6.ns["ns=robotics;i=5017"])
o6.reference(o6.ns["ns=robotics;i=5019"], "i=54", "i=2311")
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=robotics;i=6029",
    browseName="ns=robotics;LastTransitionReason",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=robotics;i=6034",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[6],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Unknown", "en"), description=o6.LocalizedText("Caused by an unknown reason", "en")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("External", "en"), description=o6.LocalizedText("Caused by external operation", "en")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Direct", "en"), description=o6.LocalizedText("Caused by direct operation", "en")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("System", "en"), description=o6.LocalizedText("Caused by system specific behavior", "en")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("Error", "en"), description=o6.LocalizedText("Caused by an error", "en")),
                    ns0.datatypes.EnumValueType(
                        value=5, displayName=o6.LocalizedText("Application", "en"), description=o6.LocalizedText("Caused explicitly by end user program logic", "en")
                    ),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6035", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.Int16,
    accessLevel=3,
)
o6.reference(robotics_objtypes.IdleSubstateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=6029"])
ns0.vartypes.FiniteTransitionVariableType(
    nodeId="ns=robotics;i=6036",
    browseName="LastTransition",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6037", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
o6.reference(robotics_objtypes.ExecutingSubstateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=6036"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=robotics;i=6038",
    browseName="ns=robotics;LastTransitionReason",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=robotics;i=6039",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[6],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Unknown", "en"), description=o6.LocalizedText("Caused by an unknown reason", "en")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("External", "en"), description=o6.LocalizedText("Caused by external operation", "en")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Direct", "en"), description=o6.LocalizedText("Caused by direct operation", "en")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("System", "en"), description=o6.LocalizedText("Caused by system specific behavior", "en")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("Error", "en"), description=o6.LocalizedText("Caused by an error", "en")),
                    ns0.datatypes.EnumValueType(
                        value=5, displayName=o6.LocalizedText("Application", "en"), description=o6.LocalizedText("Caused explicitly by end user program logic", "en")
                    ),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6040", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.Int16,
    accessLevel=3,
)
o6.reference(robotics_objtypes.ExecutingSubstateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=6038"])
ns0.objtypes.InitialStateType(
    nodeId="ns=robotics;i=5020",
    browseName="ns=robotics;Running",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6041", browseName="StateNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(robotics_objtypes.ExecutingSubstateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=5020"])
ns0.objtypes.StateType(
    nodeId="ns=robotics;i=5021",
    browseName="ns=robotics;Stopping",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6042", browseName="StateNumber", dataType=o6.UInt32, value=2))],
)
o6.reference(robotics_objtypes.ExecutingSubstateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=5021"])
ns0.objtypes.TransitionType(
    nodeId="ns=robotics;i=5022",
    browseName="ns=robotics;RunningToStopping",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6043", browseName="TransitionNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(robotics_objtypes.ExecutingSubstateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=5022"])
o6.reference(o6.ns["ns=robotics;i=5022"], "i=51", o6.ns["ns=robotics;i=5020"])
o6.reference(o6.ns["ns=robotics;i=5022"], "i=52", o6.ns["ns=robotics;i=5021"])
o6.reference(o6.ns["ns=robotics;i=5022"], "i=54", "i=2311")
ns0.vartypes.FiniteTransitionVariableType(
    nodeId="ns=robotics;i=6044",
    browseName="LastTransition",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6045", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
o6.reference(robotics_objtypes.ReadySubstateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=6044"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=robotics;i=6046",
    browseName="ns=robotics;LastTransitionReason",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=robotics;i=6047",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[6],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Unknown", "en"), description=o6.LocalizedText("Caused by an unknown reason", "en")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("External", "en"), description=o6.LocalizedText("Caused by external operation", "en")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Direct", "en"), description=o6.LocalizedText("Caused by direct operation", "en")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("System", "en"), description=o6.LocalizedText("Caused by system specific behavior", "en")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("Error", "en"), description=o6.LocalizedText("Caused by an error", "en")),
                    ns0.datatypes.EnumValueType(
                        value=5, displayName=o6.LocalizedText("Application", "en"), description=o6.LocalizedText("Caused explicitly by end user program logic", "en")
                    ),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6048", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.Int16,
    accessLevel=3,
)
o6.reference(robotics_objtypes.ReadySubstateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=6046"])
ns0.objtypes.StateType(
    nodeId="ns=robotics;i=5023",
    browseName="ns=robotics;AtProgramStart",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6049", browseName="StateNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(robotics_objtypes.ReadySubstateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=5023"])
ns0.objtypes.StateType(
    nodeId="ns=robotics;i=5024",
    browseName="ns=robotics;Suspended",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6050", browseName="StateNumber", dataType=o6.UInt32, value=2))],
)
o6.reference(robotics_objtypes.ReadySubstateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=5024"])
ns0.objtypes.TransitionType(
    nodeId="ns=robotics;i=5025",
    browseName="ns=robotics;ProgramStartToSuspended",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6051", browseName="TransitionNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(robotics_objtypes.ReadySubstateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=5025"])
o6.reference(o6.ns["ns=robotics;i=5025"], "i=51", o6.ns["ns=robotics;i=5023"])
o6.reference(o6.ns["ns=robotics;i=5025"], "i=52", o6.ns["ns=robotics;i=5024"])
o6.reference(o6.ns["ns=robotics;i=5025"], "i=54", "i=2311")
ns0.objtypes.TransitionType(
    nodeId="ns=robotics;i=5026",
    browseName="ns=robotics;SuspendedToProgramStart",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6052", browseName="TransitionNumber", dataType=o6.UInt32, value=2))],
)
o6.reference(robotics_objtypes.ReadySubstateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=5026"])
o6.reference(o6.ns["ns=robotics;i=5026"], "i=51", o6.ns["ns=robotics;i=5024"])
o6.reference(o6.ns["ns=robotics;i=5026"], "i=52", o6.ns["ns=robotics;i=5023"])
o6.reference(o6.ns["ns=robotics;i=5026"], "i=53", o6.ns["ns=robotics;i=7003"])
o6.reference(o6.ns["ns=robotics;i=5026"], "i=54", "i=2311")
ns0.vartypes.FiniteTransitionVariableType(
    nodeId="ns=robotics;i=6058",
    browseName="LastTransition",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6059", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
o6.reference(robotics_objtypes.SystemOperationStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=6058"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=robotics;i=6060",
    browseName="ns=robotics;LastTransitionReason",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=robotics;i=6061",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[6],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Unknown", "en"), description=o6.LocalizedText("Caused by an unknown reason", "en")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("External", "en"), description=o6.LocalizedText("Caused by external operation", "en")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Direct", "en"), description=o6.LocalizedText("Caused by direct operation", "en")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("System", "en"), description=o6.LocalizedText("Caused by system specific behavior", "en")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("Error", "en"), description=o6.LocalizedText("Caused by an error", "en")),
                    ns0.datatypes.EnumValueType(
                        value=5, displayName=o6.LocalizedText("Application", "en"), description=o6.LocalizedText("Caused explicitly by end user program logic", "en")
                    ),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6062", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.Int16,
    accessLevel=3,
)
o6.reference(robotics_objtypes.SystemOperationStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=6060"])
ns0.vartypes.FiniteTransitionVariableType(
    nodeId="ns=robotics;i=6071",
    browseName="LastTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6072", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=robotics;i=6073",
    browseName="ns=robotics;LastTransitionReason",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=robotics;i=6074",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[1],
                value=[ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText())],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6075", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.Int16,
    accessLevel=3,
)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=robotics;i=6076",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6077", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
robotics_objtypes.IdleSubstateMachineType(
    nodeId="ns=robotics;i=5027",
    browseName="ns=robotics;IdleSubstateMachine",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=robotics;i=6071"]), o6.hasComponent(o6.ns["ns=robotics;i=6073"]), o6.hasComponent(o6.ns["ns=robotics;i=6076"])],
)
o6.reference(robotics_objtypes.SystemOperationStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=5027"])
ns0.vartypes.FiniteTransitionVariableType(
    nodeId="ns=robotics;i=6078",
    browseName="LastTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6079", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=robotics;i=6080",
    browseName="ns=robotics;LastTransitionReason",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=robotics;i=6081",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[6],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Unknown", "en"), description=o6.LocalizedText("Caused by an unknown reason", "en")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("External", "en"), description=o6.LocalizedText("Caused by external operation", "en")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Direct", "en"), description=o6.LocalizedText("Caused by direct operation", "en")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("System", "en"), description=o6.LocalizedText("Caused by system specific behavior", "en")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("Error", "en"), description=o6.LocalizedText("Caused by an error", "en")),
                    ns0.datatypes.EnumValueType(
                        value=5, displayName=o6.LocalizedText("Application", "en"), description=o6.LocalizedText("Caused explicitly by end user program logic", "en")
                    ),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6082", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.Int16,
    accessLevel=3,
)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=robotics;i=6083",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6084", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
robotics_objtypes.ExecutingSubstateMachineType(
    nodeId="ns=robotics;i=5028",
    browseName="ns=robotics;ExecutingSubstateMachine",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=robotics;i=6078"]), o6.hasComponent(o6.ns["ns=robotics;i=6080"]), o6.hasComponent(o6.ns["ns=robotics;i=6083"])],
)
o6.reference(robotics_objtypes.SystemOperationStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=5028"])
ns0.objtypes.StateType(
    nodeId="ns=robotics;i=5030",
    browseName="ns=robotics;Idle",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6085", browseName="StateNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(robotics_objtypes.SystemOperationStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=5030"])
o6.reference(o6.ns["ns=robotics;i=5030"], "i=117", o6.ns["ns=robotics;i=5027"])
ns0.objtypes.StateType(
    nodeId="ns=robotics;i=5031",
    browseName="ns=robotics;Ready",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6086", browseName="StateNumber", dataType=o6.UInt32, value=2))],
)
o6.reference(robotics_objtypes.SystemOperationStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=5031"])
ns0.objtypes.StateType(
    nodeId="ns=robotics;i=5032",
    browseName="ns=robotics;Executing",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6087", browseName="StateNumber", dataType=o6.UInt32, value=3))],
)
o6.reference(robotics_objtypes.SystemOperationStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=5032"])
o6.reference(o6.ns["ns=robotics;i=5032"], "i=117", o6.ns["ns=robotics;i=5028"])
ns0.objtypes.TransitionType(
    nodeId="ns=robotics;i=5033",
    browseName="ns=robotics;IdleToIdle",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6088", browseName="TransitionNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(robotics_objtypes.SystemOperationStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=5033"])
o6.reference(o6.ns["ns=robotics;i=5033"], "i=51", o6.ns["ns=robotics;i=5030"])
o6.reference(o6.ns["ns=robotics;i=5033"], "i=52", o6.ns["ns=robotics;i=5030"])
o6.reference(o6.ns["ns=robotics;i=5033"], "i=53", o6.ns["ns=robotics;i=7007"])
o6.reference(o6.ns["ns=robotics;i=5033"], "i=54", "i=2311")
ns0.objtypes.TransitionType(
    nodeId="ns=robotics;i=5034",
    browseName="ns=robotics;IdleToReady",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6089", browseName="TransitionNumber", dataType=o6.UInt32, value=2))],
)
o6.reference(robotics_objtypes.SystemOperationStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=5034"])
o6.reference(o6.ns["ns=robotics;i=5034"], "i=51", o6.ns["ns=robotics;i=5030"])
o6.reference(o6.ns["ns=robotics;i=5034"], "i=52", o6.ns["ns=robotics;i=5031"])
o6.reference(o6.ns["ns=robotics;i=5034"], "i=53", o6.ns["ns=robotics;i=7006"])
o6.reference(o6.ns["ns=robotics;i=5034"], "i=54", "i=2311")
ns0.objtypes.TransitionType(
    nodeId="ns=robotics;i=5035",
    browseName="ns=robotics;ReadyToIdle",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6090", browseName="TransitionNumber", dataType=o6.UInt32, value=3))],
)
o6.reference(robotics_objtypes.SystemOperationStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=5035"])
o6.reference(o6.ns["ns=robotics;i=5035"], "i=51", o6.ns["ns=robotics;i=5031"])
o6.reference(o6.ns["ns=robotics;i=5035"], "i=52", o6.ns["ns=robotics;i=5030"])
o6.reference(o6.ns["ns=robotics;i=5035"], "i=53", o6.ns["ns=robotics;i=7007"])
o6.reference(o6.ns["ns=robotics;i=5035"], "i=54", "i=2311")
ns0.objtypes.TransitionType(
    nodeId="ns=robotics;i=5036",
    browseName="ns=robotics;ReadyToExecuting",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6091", browseName="TransitionNumber", dataType=o6.UInt32, value=4))],
)
o6.reference(robotics_objtypes.SystemOperationStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=5036"])
o6.reference(o6.ns["ns=robotics;i=5036"], "i=51", o6.ns["ns=robotics;i=5031"])
o6.reference(o6.ns["ns=robotics;i=5036"], "i=52", o6.ns["ns=robotics;i=5032"])
o6.reference(o6.ns["ns=robotics;i=5036"], "i=53", o6.ns["ns=robotics;i=7004"])
o6.reference(o6.ns["ns=robotics;i=5036"], "i=54", "i=2311")
ns0.objtypes.TransitionType(
    nodeId="ns=robotics;i=5037",
    browseName="ns=robotics;ExecutingToReady",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6092", browseName="TransitionNumber", dataType=o6.UInt32, value=5))],
)
o6.reference(robotics_objtypes.SystemOperationStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=5037"])
o6.reference(o6.ns["ns=robotics;i=5037"], "i=51", o6.ns["ns=robotics;i=5032"])
o6.reference(o6.ns["ns=robotics;i=5037"], "i=52", o6.ns["ns=robotics;i=5031"])
o6.reference(o6.ns["ns=robotics;i=5037"], "i=53", o6.ns["ns=robotics;i=7005"])
o6.reference(o6.ns["ns=robotics;i=5037"], "i=54", "i=2311")
ns0.objtypes.TransitionType(
    nodeId="ns=robotics;i=5038",
    browseName="ns=robotics;ExecutingToIdle",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6093", browseName="TransitionNumber", dataType=o6.UInt32, value=6))],
)
o6.reference(robotics_objtypes.SystemOperationStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=5038"])
o6.reference(o6.ns["ns=robotics;i=5038"], "i=51", o6.ns["ns=robotics;i=5032"])
o6.reference(o6.ns["ns=robotics;i=5038"], "i=52", o6.ns["ns=robotics;i=5030"])
o6.reference(o6.ns["ns=robotics;i=5038"], "i=54", "i=2311")
ns0.vartypes.FiniteTransitionVariableType(
    nodeId="ns=robotics;i=6095",
    browseName="LastTransition",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6096", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
o6.reference(robotics_objtypes.TaskControlStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=6095"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=robotics;i=6097",
    browseName="ns=robotics;LastTransitionReason",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=robotics;i=6098",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[6],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Unknown", "en"), description=o6.LocalizedText("Caused by an unknown reason", "en")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("External", "en"), description=o6.LocalizedText("Caused by external operation", "en")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Direct", "en"), description=o6.LocalizedText("Caused by direct operation", "en")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("System", "en"), description=o6.LocalizedText("Caused by system specific behavior", "en")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("Error", "en"), description=o6.LocalizedText("Caused by an error", "en")),
                    ns0.datatypes.EnumValueType(
                        value=5, displayName=o6.LocalizedText("Application", "en"), description=o6.LocalizedText("Caused explicitly by end user program logic", "en")
                    ),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6099", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.Int16,
    accessLevel=3,
)
o6.reference(robotics_objtypes.TaskControlStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=6097"])
ns0.vartypes.FiniteTransitionVariableType(
    nodeId="ns=robotics;i=6104",
    browseName="LastTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6105", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=robotics;i=6106",
    browseName="ns=robotics;LastTransitionReason",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=robotics;i=6107",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[6],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Unknown", "en"), description=o6.LocalizedText("Caused by an unknown reason", "en")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("External", "en"), description=o6.LocalizedText("Caused by external operation", "en")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Direct", "en"), description=o6.LocalizedText("Caused by direct operation", "en")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("System", "en"), description=o6.LocalizedText("Caused by system specific behavior", "en")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("Error", "en"), description=o6.LocalizedText("Caused by an error", "en")),
                    ns0.datatypes.EnumValueType(
                        value=5, displayName=o6.LocalizedText("Application", "en"), description=o6.LocalizedText("Caused explicitly by end user program logic", "en")
                    ),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6108", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.Int16,
    accessLevel=3,
)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=robotics;i=6109",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6111", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
robotics_objtypes.ReadySubstateMachineType(
    nodeId="ns=robotics;i=5039",
    browseName="ns=robotics;ReadySubstateMachine",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=robotics;i=6104"]), o6.hasComponent(o6.ns["ns=robotics;i=6106"]), o6.hasComponent(o6.ns["ns=robotics;i=6109"])],
)
o6.reference(robotics_objtypes.TaskControlStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=5039"])
ns0.objtypes.StateType(
    nodeId="ns=robotics;i=5040",
    browseName="ns=robotics;Idle",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6112", browseName="StateNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(robotics_objtypes.TaskControlStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=5040"])
ns0.objtypes.StateType(
    nodeId="ns=robotics;i=5041",
    browseName="ns=robotics;Ready",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6113", browseName="StateNumber", dataType=o6.UInt32, value=2))],
)
o6.reference(robotics_objtypes.TaskControlStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=5041"])
o6.reference(o6.ns["ns=robotics;i=5041"], "i=117", o6.ns["ns=robotics;i=5039"])
ns0.objtypes.StateType(
    nodeId="ns=robotics;i=5042",
    browseName="ns=robotics;Executing",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6114", browseName="StateNumber", dataType=o6.UInt32, value=3))],
)
o6.reference(robotics_objtypes.TaskControlStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=5042"])
ns0.objtypes.TransitionType(
    nodeId="ns=robotics;i=5043",
    browseName="ns=robotics;IdleToIdle",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6115", browseName="TransitionNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(robotics_objtypes.TaskControlStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=5043"])
o6.reference(o6.ns["ns=robotics;i=5043"], "i=51", o6.ns["ns=robotics;i=5040"])
o6.reference(o6.ns["ns=robotics;i=5043"], "i=52", o6.ns["ns=robotics;i=5040"])
o6.reference(o6.ns["ns=robotics;i=5043"], "i=54", "i=2311")
ns0.objtypes.TransitionType(
    nodeId="ns=robotics;i=5044",
    browseName="ns=robotics;IdleToReady",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6116", browseName="TransitionNumber", dataType=o6.UInt32, value=2))],
)
o6.reference(robotics_objtypes.TaskControlStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=5044"])
o6.reference(o6.ns["ns=robotics;i=5044"], "i=51", o6.ns["ns=robotics;i=5040"])
o6.reference(o6.ns["ns=robotics;i=5044"], "i=52", o6.ns["ns=robotics;i=5041"])
o6.reference(o6.ns["ns=robotics;i=5044"], "i=53", o6.ns["ns=robotics;i=7010"])
o6.reference(o6.ns["ns=robotics;i=5044"], "i=53", o6.ns["ns=robotics;i=7011"])
o6.reference(o6.ns["ns=robotics;i=5044"], "i=54", "i=2311")
ns0.objtypes.TransitionType(
    nodeId="ns=robotics;i=5045",
    browseName="ns=robotics;ReadyToIdle",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6119", browseName="TransitionNumber", dataType=o6.UInt32, value=3))],
)
o6.reference(robotics_objtypes.TaskControlStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=5045"])
o6.reference(o6.ns["ns=robotics;i=5045"], "i=51", o6.ns["ns=robotics;i=5041"])
o6.reference(o6.ns["ns=robotics;i=5045"], "i=52", o6.ns["ns=robotics;i=5040"])
o6.reference(o6.ns["ns=robotics;i=5045"], "i=53", o6.ns["ns=robotics;i=7012"])
o6.reference(o6.ns["ns=robotics;i=5045"], "i=53", o6.ns["ns=robotics;i=7013"])
o6.reference(o6.ns["ns=robotics;i=5045"], "i=53", o6.ns["ns=robotics;i=7014"])
o6.reference(o6.ns["ns=robotics;i=5045"], "i=54", "i=2311")
ns0.objtypes.TransitionType(
    nodeId="ns=robotics;i=5046",
    browseName="ns=robotics;ReadyToExecuting",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6120", browseName="TransitionNumber", dataType=o6.UInt32, value=4))],
)
o6.reference(robotics_objtypes.TaskControlStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=5046"])
o6.reference(o6.ns["ns=robotics;i=5046"], "i=51", o6.ns["ns=robotics;i=5041"])
o6.reference(o6.ns["ns=robotics;i=5046"], "i=52", o6.ns["ns=robotics;i=5042"])
o6.reference(o6.ns["ns=robotics;i=5046"], "i=53", o6.ns["ns=robotics;i=7008"])
o6.reference(o6.ns["ns=robotics;i=5046"], "i=54", "i=2311")
ns0.objtypes.TransitionType(
    nodeId="ns=robotics;i=5047",
    browseName="ns=robotics;ExecutingToReady",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6121", browseName="TransitionNumber", dataType=o6.UInt32, value=5))],
)
o6.reference(robotics_objtypes.TaskControlStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=5047"])
o6.reference(o6.ns["ns=robotics;i=5047"], "i=51", o6.ns["ns=robotics;i=5042"])
o6.reference(o6.ns["ns=robotics;i=5047"], "i=52", o6.ns["ns=robotics;i=5041"])
o6.reference(o6.ns["ns=robotics;i=5047"], "i=53", o6.ns["ns=robotics;i=7009"])
o6.reference(o6.ns["ns=robotics;i=5047"], "i=54", "i=2311")
ns0.objtypes.TransitionType(
    nodeId="ns=robotics;i=5048",
    browseName="ns=robotics;ExecutingToIdle",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6122", browseName="TransitionNumber", dataType=o6.UInt32, value=6))],
)
o6.reference(robotics_objtypes.TaskControlStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=5048"])
o6.reference(o6.ns["ns=robotics;i=5048"], "i=51", o6.ns["ns=robotics;i=5042"])
o6.reference(o6.ns["ns=robotics;i=5048"], "i=52", o6.ns["ns=robotics;i=5040"])
o6.reference(o6.ns["ns=robotics;i=5048"], "i=54", "i=2311")
ns0.vartypes.FiniteTransitionVariableType(
    nodeId="ns=robotics;i=6123",
    browseName="LastTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6124", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=robotics;i=6125",
    browseName="ns=robotics;LastTransitionReason",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=robotics;i=6126",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[6],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Unknown", "en"), description=o6.LocalizedText("Caused by an unknown reason", "en")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("External", "en"), description=o6.LocalizedText("Caused by external operation", "en")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Direct", "en"), description=o6.LocalizedText("Caused by direct operation", "en")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("System", "en"), description=o6.LocalizedText("Caused by system specific behavior", "en")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("Error", "en"), description=o6.LocalizedText("Caused by an error", "en")),
                    ns0.datatypes.EnumValueType(
                        value=5, displayName=o6.LocalizedText("Application", "en"), description=o6.LocalizedText("Caused explicitly by end user program logic", "en")
                    ),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6127", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.Int16,
    accessLevel=3,
)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=robotics;i=6128",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6129", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
robotics_objtypes.SystemOperationStateMachineType(
    nodeId="ns=robotics;i=5049",
    browseName="ns=robotics;SystemOperationStateMachine",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=robotics;i=6123"]), o6.hasComponent(o6.ns["ns=robotics;i=6125"]), o6.hasComponent(o6.ns["ns=robotics;i=6128"])],
)
o6.reference(robotics_objtypes.SystemOperationType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=5049"])
ns0.vartypes.FiniteTransitionVariableType(
    nodeId="ns=robotics;i=6133",
    browseName="LastTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6134", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=robotics;i=6135",
    browseName="ns=robotics;LastTransitionReason",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=robotics;i=6136",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[6],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Unknown", "en"), description=o6.LocalizedText("Caused by an unknown reason", "en")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("External", "en"), description=o6.LocalizedText("Caused by external operation", "en")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Direct", "en"), description=o6.LocalizedText("Caused by direct operation", "en")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("System", "en"), description=o6.LocalizedText("Caused by system specific behavior", "en")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("Error", "en"), description=o6.LocalizedText("Caused by an error", "en")),
                    ns0.datatypes.EnumValueType(
                        value=5, displayName=o6.LocalizedText("Application", "en"), description=o6.LocalizedText("Caused explicitly by end user program logic", "en")
                    ),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6137", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.Int16,
    accessLevel=3,
)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=robotics;i=6138",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6139", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
robotics_objtypes.TaskControlStateMachineType(
    nodeId="ns=robotics;i=5051",
    browseName="ns=robotics;TaskControlStateMachine",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=robotics;i=6133"]), o6.hasComponent(o6.ns["ns=robotics;i=6135"]), o6.hasComponent(o6.ns["ns=robotics;i=6138"])],
)
o6.reference(robotics_objtypes.TaskControlOperationType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=5051"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=robotics;i=6148",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6149", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.FiniteTransitionVariableType(
    nodeId="ns=robotics;i=6150",
    browseName="LastTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6151", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=robotics;i=6152",
    browseName="ns=robotics;LastTransitionReason",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=robotics;i=6153",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[6],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Unknown", "en"), description=o6.LocalizedText("Caused by an unknown reason", "en")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("External", "en"), description=o6.LocalizedText("Caused by external operation", "en")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Direct", "en"), description=o6.LocalizedText("Caused by direct operation", "en")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("System", "en"), description=o6.LocalizedText("Caused by system specific behavior", "en")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("Error", "en"), description=o6.LocalizedText("Caused by an error", "en")),
                    ns0.datatypes.EnumValueType(
                        value=5, displayName=o6.LocalizedText("Application", "en"), description=o6.LocalizedText("Caused explicitly by end user program logic", "en")
                    ),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6154", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.Int16,
    accessLevel=3,
)
robotics_objtypes.TaskControlStateMachineType(
    nodeId="ns=robotics;i=5053",
    browseName="ns=robotics;TaskControlStateMachine",
    references=[o6.hasComponent(o6.ns["ns=robotics;i=6148"]), o6.hasComponent(o6.ns["ns=robotics;i=6150"]), o6.hasComponent(o6.ns["ns=robotics;i=6152"])],
)
robotics_objtypes.TaskControlOperationType(
    nodeId="ns=robotics;i=5052", browseName="ns=robotics;TaskControlOperation", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=robotics;i=5053"])]
)
o6.reference(robotics_objtypes.TaskControlType, ns0.reftypes.HasAddIn, o6.ns["ns=robotics;i=5052"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=robotics;i=6162",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6163", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.FiniteTransitionVariableType(
    nodeId="ns=robotics;i=6164",
    browseName="LastTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6165", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=robotics;i=6166",
    browseName="ns=robotics;LastTransitionReason",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=robotics;i=6167",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[6],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Unknown", "en"), description=o6.LocalizedText("Caused by an unknown reason", "en")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("External", "en"), description=o6.LocalizedText("Caused by external operation", "en")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Direct", "en"), description=o6.LocalizedText("Caused by direct operation", "en")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("System", "en"), description=o6.LocalizedText("Caused by system specific behavior", "en")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("Error", "en"), description=o6.LocalizedText("Caused by an error", "en")),
                    ns0.datatypes.EnumValueType(
                        value=5, displayName=o6.LocalizedText("Application", "en"), description=o6.LocalizedText("Caused explicitly by end user program logic", "en")
                    ),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6168", browseName="ValueAsText", dataType=o6.LocalizedText, value=o6.LocalizedText("Invalid"))),
    ],
    dataType=o6.Int16,
    accessLevel=3,
)
robotics_objtypes.SystemOperationStateMachineType(
    nodeId="ns=robotics;i=5056",
    browseName="ns=robotics;SystemOperationStateMachine",
    references=[o6.hasComponent(o6.ns["ns=robotics;i=6162"]), o6.hasComponent(o6.ns["ns=robotics;i=6164"]), o6.hasComponent(o6.ns["ns=robotics;i=6166"])],
)
robotics_objtypes.SystemOperationType(
    nodeId="ns=robotics;i=5055", browseName="ns=robotics;SystemOperation", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=robotics;i=5056"])]
)
o6.reference(robotics_objtypes.ControllerType, ns0.reftypes.HasAddIn, o6.ns["ns=robotics;i=5055"])
robotics_objtypes.TaskModuleType(
    nodeId="ns=robotics;i=5058",
    browseName="ns=robotics;<TaskModule>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6169", browseName="ns=robotics;Name", dataType=o6.String, accessLevel=3))],
)
ns0.objtypes.FolderType(nodeId="ns=robotics;i=5057", browseName="ns=robotics;TaskModules", modellingRule="Optional", references=[o6.organizes(o6.ns["ns=robotics;i=5058"])])
o6.reference(robotics_objtypes.TaskControlType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=5057"])
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=robotics;i=6185",
    browseName="AckedState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6186", browseName="Id", dataType=o6.Boolean))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=robotics;i=6188",
    browseName="EnabledState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6189", browseName="Id", dataType=o6.Boolean))],
    dataType=o6.LocalizedText,
)
o6.reference(o6.ns["ns=robotics;i=6188"], "i=9004", o6.ns["ns=robotics;i=6185"])
ns0.vartypes.ConditionVariableType(
    nodeId="ns=robotics;i=6193",
    browseName="Comment",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6194", browseName="SourceTimestamp", dataType=ns0.datatypes.UtcTime))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.ConditionVariableType(
    nodeId="ns=robotics;i=6200",
    browseName="LastSeverity",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6201", browseName="SourceTimestamp", dataType=ns0.datatypes.UtcTime))],
    dataType=o6.UInt16,
)
ns0.vartypes.ConditionVariableType(
    nodeId="ns=robotics;i=6202",
    browseName="Quality",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6203", browseName="SourceTimestamp", dataType=ns0.datatypes.UtcTime))],
    dataType=o6.StatusCode,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=robotics;i=6723",
    browseName="ns=robotics;Mass",
    description="The weight of the load mounted on one mounting point.",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6728", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
o6.reference(robotics_objtypes.LoadType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=6723"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=robotics;i=6757",
    browseName="ns=robotics;MotorTemperature",
    description='The motor temperature provides the temperature of the motor. If there is no temperature sensor the value is set to \\"null\\".',
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6762", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)


ns0.vartypes.PropertyType(
    nodeId="ns=robotics;i=6155",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=robotics;i=7015",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="DirectoryName", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=robotics;i=6156",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=robotics;i=7015",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="DirectoryNodeId", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(nodeId="ns=robotics;i=7015", browseName="CreateDirectory", inputArgs=o6.hasProperty(o6.ns["ns=robotics;i=6155"]), outputArgs=o6.hasProperty(o6.ns["ns=robotics;i=6156"]))

ns0.vartypes.PropertyType(
    nodeId="ns=robotics;i=6157",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=robotics;i=7016",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileName", dataType=o6.String, valueRank=-1), ns0.datatypes.Argument(name="RequestFileOpen", dataType=o6.Boolean, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=robotics;i=6158",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=robotics;i=7016",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileNodeId", dataType=o6.NodeId, valueRank=-1), ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=robotics;i=7016", browseName="CreateFile", inputArgs=o6.hasProperty(o6.ns["ns=robotics;i=6157"]), outputArgs=o6.hasProperty(o6.ns["ns=robotics;i=6158"]))

ns0.vartypes.PropertyType(
    nodeId="ns=robotics;i=6159",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=robotics;i=7017",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ObjectToDelete", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(nodeId="ns=robotics;i=7017", browseName="Delete", inputArgs=o6.hasProperty(o6.ns["ns=robotics;i=6159"]))

ns0.vartypes.PropertyType(
    nodeId="ns=robotics;i=6160",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=robotics;i=7018",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.Argument(name="ObjectToMoveOrCopy", dataType=o6.NodeId, valueRank=-1),
        ns0.datatypes.Argument(name="TargetDirectory", dataType=o6.NodeId, valueRank=-1),
        ns0.datatypes.Argument(name="CreateCopy", dataType=o6.Boolean, valueRank=-1),
        ns0.datatypes.Argument(name="NewName", dataType=o6.String, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=robotics;i=6161",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=robotics;i=7018",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="NewNodeId", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(nodeId="ns=robotics;i=7018", browseName="MoveOrCopy", inputArgs=o6.hasProperty(o6.ns["ns=robotics;i=6160"]), outputArgs=o6.hasProperty(o6.ns["ns=robotics;i=6161"]))

ns0.objtypes.FileDirectoryType(
    nodeId="ns=robotics;i=5054",
    browseName="ns=robotics;Programs",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=robotics;i=7015"]),
        o6.hasComponent(o6.ns["ns=robotics;i=7016"]),
        o6.hasComponent(o6.ns["ns=robotics;i=7017"]),
        o6.hasComponent(o6.ns["ns=robotics;i=7018"]),
    ],
)
o6.reference(robotics_objtypes.ControllerType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=5054"])


ns0.vartypes.PropertyType(
    nodeId="ns=robotics;i=6187",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=robotics;i=7019",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="EventId", dataType=o6.ByteString, valueRank=-1, description=o6.LocalizedText("The identifier for the event to comment.")),
        ns0.datatypes.Argument(name="Comment", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("The comment to add to the condition.")),
    ],
)
o6.call(nodeId="ns=robotics;i=7019", browseName="Acknowledge", inputArgs=o6.hasProperty(o6.ns["ns=robotics;i=6187"]))

ns0.vartypes.PropertyType(
    nodeId="ns=robotics;i=6190",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=robotics;i=7020",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="EventId", dataType=o6.ByteString, valueRank=-1, description=o6.LocalizedText("The identifier for the event to comment.")),
        ns0.datatypes.Argument(name="Comment", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("The comment to add to the condition.")),
    ],
)
o6.call(nodeId="ns=robotics;i=7020", browseName="AddComment", inputArgs=o6.hasProperty(o6.ns["ns=robotics;i=6190"]))

ns0.objtypes.AcknowledgeableConditionType(
    nodeId="ns=robotics;i=5059",
    browseName="ns=robotics;<AcknowledgeableCondition>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6191", browseName="BranchId", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6192", browseName="ClientUserId", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6195", browseName="ConditionClassId", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6196", browseName="ConditionClassName", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6197", browseName="ConditionName", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6198", browseName="ConditionSubClassId", dataType=o6.NodeId, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6199", browseName="ConditionSubClassName", dataType=o6.LocalizedText, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6204", browseName="Retain", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6205", browseName="EventId", dataType=o6.ByteString)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6206", browseName="EventType", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6207", browseName="Message", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6208", browseName="ReceiveTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6209", browseName="Severity", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6210", browseName="SourceName", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6211", browseName="SourceNode", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6212", browseName="Time", dataType=ns0.datatypes.UtcTime)),
        o6.hasComponent(o6.ns["ns=robotics;i=6185"]),
        o6.hasComponent(o6.ns["ns=robotics;i=6188"]),
        o6.hasComponent(o6.ns["ns=robotics;i=6193"]),
        o6.hasComponent(o6.ns["ns=robotics;i=6200"]),
        o6.hasComponent(o6.ns["ns=robotics;i=6202"]),
        o6.hasComponent(o6.ns["ns=robotics;i=7019"]),
        o6.hasComponent(o6.ns["ns=robotics;i=7020"]),
        o6.hasComponent(o6.call(nodeId="ns=robotics;i=7021", browseName="Disable")),
        o6.hasComponent(o6.call(nodeId="ns=robotics;i=7022", browseName="Enable")),
    ],
)
ns0.objtypes.FolderType(nodeId="ns=robotics;i=5050", browseName="ns=robotics;Conditions", modellingRule="Optional", references=[o6.organizes(o6.ns["ns=robotics;i=5059"])])
o6.reference(robotics_objtypes.SystemOperationType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=5050"])
ns0.objtypes.BaseObjectType(
    nodeId="ns=robotics;i=15024",
    browseName="ns=di;ParameterSet",
    description="Flat list of Parameters",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=robotics;i=15061",
                browseName="ns=robotics;SpeedOverride",
                description="SpeedOverride provides the current speed setting in percent of programmed speed (0 - 100%).",
                dataType=o6.Double,
            )
        )
    ],
)
ns0.objtypes.FolderType(nodeId="ns=robotics;i=15062", browseName="ns=robotics;Axes", description="Axes is a container for one or more instances of the AxisType.")
ns0.objtypes.FolderType(
    nodeId="ns=robotics;i=15208", browseName="ns=robotics;PowerTrains", description="PowerTrains is a container for one or more instances of the PowerTrainType."
)
robotics_objtypes.MotionDeviceType(
    nodeId="ns=robotics;i=15008",
    browseName="ns=robotics;<MotionDeviceIdentifier>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=15045", browseName="ns=di;Manufacturer", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=15047", browseName="ns=di;Model", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=15048", browseName="ns=di;SerialNumber", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=15053", browseName="ns=di;ProductCode", dataType=o6.String)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=robotics;i=15058",
                browseName="ns=robotics;MotionDeviceCategory",
                description="The variable MotionDeviceCategory provides the kind of motion device defined by MotionDeviceCategoryEnumeration based on ISO 8373.",
                dataType=robotics_datypes.MotionDeviceCategoryEnumeration,
            )
        ),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=robotics;i=6002", browseName="ns=robotics;TaskControlReference", dataType=o6.NodeId)),
        o6.hasComponent(o6.ns["ns=robotics;i=15024"]),
        o6.hasComponent(o6.ns["ns=robotics;i=15062"]),
        o6.hasComponent(o6.ns["ns=robotics;i=15208"]),
    ],
)
ns0.objtypes.FolderType(
    nodeId="ns=robotics;i=5002",
    browseName="ns=robotics;MotionDevices",
    description="Contains any kinematic or motion device which is part of the motion device system.",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=robotics;i=15008"])],
)
o6.reference(robotics_objtypes.MotionDeviceSystemType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=5002"])
robotics_objtypes.UserType(
    nodeId="ns=robotics;i=15440",
    browseName="ns=robotics;CurrentUser",
    description="The given name of the device.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=robotics;i=15441", browseName="ns=robotics;Level", description="The weight of the load mounted on one mounting point.", dataType=o6.String
            )
        )
    ],
)
ns0.objtypes.FolderType(
    nodeId="ns=robotics;i=15483", browseName="ns=robotics;Software", description="Software is a container for one or more instances of SoftwareType defined in OPC UA DI."
)
ns0.objtypes.FolderType(
    nodeId="ns=robotics;i=15518", browseName="ns=robotics;TaskControls", description="TaskControls is a container for one or more instances of TaskControlType."
)
robotics_objtypes.ControllerType(
    nodeId="ns=robotics;i=15405",
    browseName="ns=robotics;<ControllerIdentifier>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=15426", browseName="ns=di;Manufacturer", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=15428", browseName="ns=di;Model", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=15429", browseName="ns=di;SerialNumber", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=15434", browseName="ns=di;ProductCode", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=robotics;i=15440"]),
        o6.hasComponent(o6.ns["ns=robotics;i=15483"]),
        o6.hasComponent(o6.ns["ns=robotics;i=15518"]),
    ],
)
ns0.objtypes.FolderType(
    nodeId="ns=robotics;i=5001",
    browseName="ns=robotics;Controllers",
    description="Contains the set of controllers in the motion device system.",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=robotics;i=15405"])],
)
o6.reference(robotics_objtypes.MotionDeviceSystemType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=5001"])
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashRoboticsSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=robotics;i=15011",
    browseName="ns=robotics;http://opcfoundation.org/UA/Robotics/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=15034", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/Robotics/")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=15064", browseName="NamespaceVersion", dataType=o6.String, value="1.02")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=robotics;i=15091", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2025-09-08T00:00:00Z"))
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=robotics;i=15114", browseName="IsNamespaceSubset", dataType=o6.Boolean)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=robotics;i=15145", browseName="StaticNodeIdTypes", dataType=ns0.datatypes.IdType, valueRank=1, arrayDimensions=[1], value=[ns0.datatypes.IdType.NUMERIC]
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=robotics;i=15173", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=15209", browseName="StaticStringNodeIdPattern", dataType=o6.String)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=robotics;i=15583",
                browseName="DefaultRolePermissions",
                rolePermissions={
                    "i=15644": ns0.datatypes.PermissionType.BROWSE,
                    "i=15704": ns0.datatypes.PermissionType.READ_ROLE_PERMISSIONS | ns0.datatypes.PermissionType.READ | ns0.datatypes.PermissionType.WRITE,
                },
                dataType=ns0.datatypes.RolePermissionType,
                valueRank=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=15584", browseName="DefaultUserRolePermissions", dataType=ns0.datatypes.RolePermissionType, valueRank=1)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=robotics;i=15585",
                browseName="DefaultAccessRestrictions",
                rolePermissions={
                    "i=15644": ns0.datatypes.PermissionType.BROWSE,
                    "i=15704": ns0.datatypes.PermissionType.READ_ROLE_PERMISSIONS | ns0.datatypes.PermissionType.READ | ns0.datatypes.PermissionType.WRITE,
                },
                dataType=ns0.datatypes.AccessRestrictionType,
            )
        ),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=robotics;i=6624",
    browseName="ns=robotics;Mass",
    description="The weight of the load mounted on one mounting point.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=15659", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
robotics_objtypes.LoadType(
    nodeId="ns=robotics;i=5091",
    browseName="ns=robotics;FlangeLoad",
    description="The FlangeLoad is the load on the flange or at the mounting point of the MotionDevice. This can be the maximum load of the MotionDevice.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=robotics;i=6624"])],
)
o6.reference(robotics_objtypes.MotionDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=5091"])
ns0.objtypes.BaseObjectType(
    nodeId="ns=robotics;i=15698",
    browseName="ns=di;ParameterSet",
    description="Flat list of Parameters",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=robotics;i=15740",
                browseName="ns=robotics;OperationalMode",
                description="The OperationalMode variable provides information about the current operational mode. Allowed values are described in OperationalModeEnumeration, see ISO 10218-1:2011 Ch.5.7 Operational Modes.",
                dataType=robotics_datypes.OperationalModeEnumeration,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=robotics;i=15741",
                browseName="ns=robotics;EmergencyStop",
                description="The EmergencyStop variable is TRUE if one or more of the emergency stop functions in the robot system are active, FALSE otherwise. If the EmergencyStopFunctions object is provided, then the value of this variable is TRUE if one or more of the listed emergency stop functions are active.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=robotics;i=15742",
                browseName="ns=robotics;ProtectiveStop",
                description="The ProtectiveStop variable is TRUE if one or more of the enabled protective stop functions in the system are active, FALSE otherwise. If the ProtectiveStopFunctions object is provided, then the value of this variable is TRUE if one or more of the listed protective stop functions are enabled and active.",
                dataType=o6.Boolean,
            )
        ),
    ],
)
robotics_objtypes.SafetyStateType(
    nodeId="ns=robotics;i=15697", browseName="ns=robotics;<SafetyStateIdentifier>", modellingRule="MandatoryPlaceholder", references=[o6.hasComponent(o6.ns["ns=robotics;i=15698"])]
)
ns0.objtypes.FolderType(
    nodeId="ns=robotics;i=5010",
    browseName="ns=robotics;SafetyStates",
    description="Contains safety-related data from motion device system.",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=robotics;i=15697"])],
)
o6.reference(robotics_objtypes.MotionDeviceSystemType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=5010"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=robotics;i=15863",
    browseName="ns=robotics;ActualPosition",
    description="The axis position inclusive Unit and RangeOfMotion.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=15869", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=robotics;i=15744", browseName="ns=di;ParameterSet", description="Flat list of Parameters", references=[o6.hasComponent(o6.ns["ns=robotics;i=15863"])]
)
robotics_objtypes.AxisType(
    nodeId="ns=robotics;i=15743",
    browseName="ns=robotics;<AxisIdentifier>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=robotics;i=15808",
                browseName="ns=robotics;MotionProfile",
                description="The kind of axis motion as defined with the AxisMotionProfileEnumeration.",
                dataType=robotics_datypes.AxisMotionProfileEnumeration,
            )
        ),
        o6.hasComponent(o6.ns["ns=robotics;i=15744"]),
    ],
)
o6.reference(o6.ns["ns=robotics;i=15062"], "i=47", o6.ns["ns=robotics;i=15743"])
o6.reference(o6.ns["ns=robotics;i=15305"], "i=47", o6.ns["ns=robotics;i=15743"])
robotics_objtypes.PowerTrainType(nodeId="ns=robotics;i=15905", browseName="ns=robotics;<PowerTrainIdentifier>", modellingRule="MandatoryPlaceholder")
o6.reference(o6.ns["ns=robotics;i=15208"], "i=47", o6.ns["ns=robotics;i=15905"])
o6.reference(o6.ns["ns=robotics;i=16443"], "i=47", o6.ns["ns=robotics;i=15905"])
ns0.objtypes.BaseObjectType(
    nodeId="ns=robotics;i=5016",
    browseName="ns=di;ParameterSet",
    description="Flat list of Parameters",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=robotics;i=15882",
                browseName="ns=robotics;EmergencyStop",
                description="The EmergencyStop variable is TRUE if one or more of the emergency stop functions in the robot system are active, FALSE otherwise. If the EmergencyStopFunctions object is provided, then the value of this variable is TRUE if one or more of the listed emergency stop functions are active.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=robotics;i=15912",
                browseName="ns=robotics;OperationalMode",
                description="The OperationalMode variable provides information about the current operational mode. Allowed values are described in OperationalModeEnumeration, see ISO 10218-1:2011 Ch.5.7 Operational Modes.",
                dataType=robotics_datypes.OperationalModeEnumeration,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=robotics;i=15913",
                browseName="ns=robotics;ProtectiveStop",
                description="The ProtectiveStop variable is TRUE if one or more of the enabled protective stop functions in the system are active, FALSE otherwise. If the ProtectiveStopFunctions object is provided, then the value of this variable is TRUE if one or more of the listed protective stop functions are enabled and active.",
                dataType=o6.Boolean,
            )
        ),
    ],
)
o6.reference(robotics_objtypes.SafetyStateType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=5016"])
ns0.vartypes.RationalNumberType(
    nodeId="ns=robotics;i=15941",
    browseName="ns=robotics;GearRatio",
    description="The transmission ratio of the gear expressed as a fraction as input velocity (motor side) by output velocity (load side).",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=robotics;i=15615", browseName="Numerator", dataType=o6.Int32)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=robotics;i=15616", browseName="Denominator", dataType=o6.UInt32)),
    ],
    dataType=ns0.datatypes.RationalNumber,
)
o6.reference(robotics_objtypes.GearType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=15941"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=robotics;i=16034",
    browseName="ns=robotics;MotorTemperature",
    description='The motor temperature provides the temperature of the motor. If there is no temperature sensor the value is set to \\"null\\".',
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=16039", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=robotics;i=15999", browseName="ns=di;ParameterSet", description="Flat list of Parameters", references=[o6.hasComponent(o6.ns["ns=robotics;i=16034"])]
)
robotics_objtypes.MotorType(
    nodeId="ns=robotics;i=15998",
    browseName="ns=robotics;<MotorIdentifier>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=16019", browseName="ns=di;Manufacturer", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=16021", browseName="ns=di;Model", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=16025", browseName="ns=di;ProductCode", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=16028", browseName="ns=di;SerialNumber", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=robotics;i=15999"]),
    ],
)
o6.reference(o6.ns["ns=robotics;i=15905"], "i=47", o6.ns["ns=robotics;i=15998"])
o6.reference(robotics_objtypes.PowerTrainType, "i=47", "ns=robotics;i=15998")
ns0.vartypes.RationalNumberType(
    nodeId="ns=robotics;i=16076",
    browseName="ns=robotics;GearRatio",
    description="The transmission ratio of the gear expressed as a fraction as input velocity (motor side) by output velocity (load side).",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=robotics;i=16077", browseName="Numerator", dataType=o6.Int32)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=robotics;i=16078", browseName="Denominator", dataType=o6.UInt32)),
    ],
    dataType=ns0.datatypes.RationalNumber,
)
robotics_objtypes.GearType(
    nodeId="ns=robotics;i=16041",
    browseName="ns=robotics;<GearIdentifier>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=16062", browseName="ns=di;Manufacturer", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=16064", browseName="ns=di;Model", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=16068", browseName="ns=di;ProductCode", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=16071", browseName="ns=di;SerialNumber", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=robotics;i=16076"]),
    ],
)
o6.reference(robotics_objtypes.PowerTrainType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=16041"])
ns0.vartypes.ThreeDCartesianCoordinatesType(
    nodeId="ns=robotics;i=16130",
    browseName="CartesianCoordinates",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=robotics;i=16134", browseName="X", dataType=o6.Double)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=robotics;i=16135", browseName="Y", dataType=o6.Double)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=robotics;i=16136", browseName="Z", dataType=o6.Double)),
    ],
    dataType=ns0.datatypes.ThreeDCartesianCoordinates,
)
ns0.vartypes.ThreeDOrientationType(
    nodeId="ns=robotics;i=16132",
    browseName="Orientation",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=robotics;i=16137", browseName="A", dataType=o6.Double)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=robotics;i=16138", browseName="B", dataType=o6.Double)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=robotics;i=16139", browseName="C", dataType=o6.Double)),
    ],
    dataType=ns0.datatypes.ThreeDOrientation,
)
ns0.vartypes.ThreeDFrameType(
    nodeId="ns=robotics;i=6013",
    browseName="ns=robotics;CenterOfMass",
    description='The position and orientation of the center of the mass related to the mounting point using a FrameType. X, Y, Z define the position of the center of gravity relative to the mounting point coordinate system. A, B, C define the orientation of the principal axes of inertia relative to the mounting point coordinate system. Orientation A, B, C can be "0" for systems which do not need these  values.',
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=robotics;i=16130"]), o6.hasComponent(o6.ns["ns=robotics;i=16132"])],
    dataType=ns0.datatypes.ThreeDFrame,
)
o6.reference(robotics_objtypes.LoadType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=6013"])
ns0.objtypes.BaseObjectType(
    nodeId="ns=robotics;i=5029",
    browseName="ns=di;ParameterSet",
    description="Flat list of Parameters",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=robotics;i=16363",
                browseName="ns=robotics;OnPath",
                description="OnPath is true if the motion device is on or near enough the planned program path such that program execution can continue. If the MotionDevice deviates too much from this path in case of errors or an emergency stop, this value becomes false. If OnPath is false, the motion device needs repositioning to continue program execution.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=robotics;i=16364",
                browseName="ns=robotics;InControl",
                description='InControl provides the information if the actuators (in most cases a motor) of the motion device are powered up and in control: "true". The motion device might be in a standstill.',
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=robotics;i=16365",
                browseName="ns=robotics;SpeedOverride",
                description="SpeedOverride provides the current speed setting in percent of programmed speed (0 - 100%).",
                dataType=o6.Double,
            )
        ),
    ],
)
o6.reference(robotics_objtypes.MotionDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=5029"])
ns0.objtypes.FolderType(
    nodeId="ns=robotics;i=16566",
    browseName="ns=robotics;AdditionalComponents",
    description="AdditionalComponents is a container for one or more instances of subtypes of ComponentType defined in OPC UA DI. The listed components are installed at the motion device, e.g. an IO-board.",
    modellingRule="Optional",
    references=[
        o6.hasComponent(ns0.objtypes.BaseObjectType(nodeId="ns=robotics;i=5003", browseName="ns=robotics;<AdditionalComponentIdentifier>", modellingRule="MandatoryPlaceholder"))
    ],
)
o6.reference(robotics_objtypes.MotionDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=16566"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=robotics;i=16639",
    browseName="ns=robotics;Mass",
    description="The weight of the load mounted on one mounting point.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=16644", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
robotics_objtypes.LoadType(
    nodeId="ns=robotics;i=16638",
    browseName="ns=robotics;AdditionalLoad",
    description="The additional load which is mounted on this axis. E.g. for process-need a transformer for welding.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=robotics;i=16639"])],
)
o6.reference(robotics_objtypes.AxisType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=16638"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=robotics;i=16662",
    browseName="ns=robotics;ActualPosition",
    description="The axis position inclusive Unit and RangeOfMotion.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=16667", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=robotics;i=16668",
    browseName="ns=robotics;ActualSpeed",
    description="The axis speed on load side (after gear/spindle) inclusive Unit.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=16673", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=robotics;i=16674",
    browseName="ns=robotics;ActualAcceleration",
    description=": The ActualAcceleration variable provides the axis acceleration. Applicable acceleration limits of the axis shall be provided by the EURange property of the AnalogUnitType.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=16679", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=robotics;i=16602",
    browseName="ns=di;ParameterSet",
    description="Flat list of Parameters",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=robotics;i=16662"]), o6.hasComponent(o6.ns["ns=robotics;i=16668"]), o6.hasComponent(o6.ns["ns=robotics;i=16674"])],
)
o6.reference(robotics_objtypes.AxisType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=16602"])
ns0.objtypes.BaseObjectType(
    nodeId="ns=robotics;i=5105",
    browseName="ns=di;ParameterSet",
    description="Flat list of Parameters",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(o6.ns["ns=robotics;i=6757"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=robotics;i=6776",
                browseName="ns=robotics;EffectiveLoadRate",
                description="EffectiveLoadRate is expressed as a percentage of maximum continuous load. The Joule integral is typically used to calculate the current load. Duration should be defined and documented by the vendor.",
                dataType=o6.UInt16,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=robotics;i=17150",
                browseName="ns=robotics;BrakeReleased",
                description="Indicates an optional variable used only for motors with brakes. If BrakeReleased is TRUE the motor is free to run. FALSE means that the motor shaft is locked by the brake.",
                dataType=o6.Boolean,
            )
        ),
    ],
)
o6.reference(robotics_objtypes.MotorType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=5105"])
robotics_objtypes.UserType(
    nodeId="ns=robotics;i=17249",
    browseName="ns=robotics;CurrentUser",
    description="The current user of the system.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=robotics;i=17250", browseName="ns=robotics;Level", description="The weight of the load mounted on one mounting point.", dataType=o6.String
            )
        )
    ],
)
o6.reference(robotics_objtypes.ControllerType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=17249"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=robotics;i=17359",
    browseName="ns=robotics;TotalEnergyConsumption",
    description="The total accumulated energy consumed by the motion devices related with this controller instance.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=17364", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=robotics;i=17365",
    browseName="ns=robotics;CabinetFanSpeed",
    description="The speed of the cabinet fan.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=17370", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=robotics;i=17371",
    browseName="ns=robotics;CPUFanSpeed",
    description="The speed of the CPU fan.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=17376", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=robotics;i=17377",
    browseName="ns=robotics;InputVoltage",
    description="The input voltage of the controller which can be a configured value. To distinguish between an AC or DC supply the optional property Definition of the base type DataItemType shall be used.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=17382", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=robotics;i=17383",
    browseName="ns=robotics;Temperature",
    description="The controller temperature given by a temperature sensor inside of the controller.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=17388", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=robotics;i=5004",
    browseName="ns=di;ParameterSet",
    description="Flat list of Parameters",
    modellingRule="Optional",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=robotics;i=15365",
                browseName="ns=robotics;UpsState",
                description="The vendor specific status of an integrated UPS or accumulator system.",
                dataType=o6.String,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=robotics;i=15366", browseName="ns=robotics;StartUpTime", description="The date and time of the last start-up of the controller.", dataType=o6.DateTime
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=robotics;i=17358",
                browseName="ns=robotics;TotalPowerOnTime",
                description="The total accumulated time the controller was powered on.",
                dataType=ns0.datatypes.DurationString,
            )
        ),
        o6.hasComponent(o6.ns["ns=robotics;i=17359"]),
        o6.hasComponent(o6.ns["ns=robotics;i=17365"]),
        o6.hasComponent(o6.ns["ns=robotics;i=17371"]),
        o6.hasComponent(o6.ns["ns=robotics;i=17377"]),
        o6.hasComponent(o6.ns["ns=robotics;i=17383"]),
    ],
)
o6.reference(robotics_objtypes.ControllerType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=5004"])
ns0.objtypes.BaseObjectType(
    nodeId="ns=robotics;i=15883",
    browseName="ns=di;ParameterSet",
    description="Flat list of Parameters",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=robotics;i=17874", browseName="ns=robotics;TaskProgramName", description="A customer given identifier for the task program.", dataType=o6.String
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=robotics;i=17875",
                browseName="ns=robotics;TaskProgramLoaded",
                description="The TaskProgramLoaded variable is TRUE if a task program is loaded in the task control, FALSE otherwise.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=robotics;i=17876",
                browseName="ns=robotics;ExecutionMode",
                description="Execution mode of the task control (continuous or step-wise).",
                dataType=robotics_datypes.ExecutionModeEnumeration,
            )
        ),
    ],
)
o6.reference(robotics_objtypes.TaskControlType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=15883"])
ns0.vartypes.ThreeDVectorType(
    nodeId="ns=robotics;i=18170",
    browseName="ns=robotics;Inertia",
    description="The Inertia uses the VectorType to describe the three values of the principal moments of inertia with respect to the mounting point coordinate system. If inertia values are provided for rotary axis the CenterOfMass shall be completely filled as well.",
    modellingRule="Optional",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=robotics;i=18171", browseName="X", dataType=o6.Double)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=robotics;i=18172", browseName="Y", dataType=o6.Double)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=robotics;i=18173", browseName="Z", dataType=o6.Double)),
    ],
    dataType=ns0.datatypes.ThreeDVector,
)
o6.reference(robotics_objtypes.LoadType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=18170"])
ns0.vartypes.PropertyType(
    nodeId="ns=robotics;i=18192",
    browseName="EnumStrings",
    parent="ns=robotics;i=18191",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[3],
    value=[o6.LocalizedText("CYCLE"), o6.LocalizedText("CONTINUOUS"), o6.LocalizedText("STEP")],
)
ns0.vartypes.PropertyType(
    nodeId="ns=robotics;i=18194",
    browseName="EnumStrings",
    parent="ns=robotics;i=18193",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[7],
    value=[
        o6.LocalizedText("OTHER"),
        o6.LocalizedText("ARTICULATED_ROBOT"),
        o6.LocalizedText("SCARA_ROBOT"),
        o6.LocalizedText("CARTESIAN_ROBOT"),
        o6.LocalizedText("SPHERICAL_ROBOT"),
        o6.LocalizedText("PARALLEL_ROBOT"),
        o6.LocalizedText("CYLINDRICAL_ROBOT"),
    ],
)
robotics_objtypes.PowerTrainType(
    nodeId="ns=robotics;i=18344",
    browseName="ns=robotics;<PowerTrainIdentifier>",
    description="The Requires reference provides the relationship of axes to powertrains. For complex kinematics this does not need to be a one to one relationship, because more than one power train might influence the motion of one axis. This reference connects all power trains to an axis that must be actively driven when only this axis should move and all other axes should stand still. Virtual axes that are not actively driven by a power train do not have this reference.",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(o6.ns["ns=robotics;i=15998"])],
)
o6.reference(robotics_objtypes.AxisType, robotics_reftypes.Requires, o6.ns["ns=robotics;i=18344"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=robotics;i=18595",
    browseName="ns=robotics;ActualPosition",
    description="The axis position inclusive Unit and RangeOfMotion.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=18600", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=robotics;i=18537", browseName="ns=di;ParameterSet", description="Flat list of Parameters", references=[o6.hasComponent(o6.ns["ns=robotics;i=18595"])]
)
robotics_objtypes.AxisType(
    nodeId="ns=robotics;i=18536",
    browseName="ns=robotics;<AxisIdentifier>",
    description="Moves is a reference to provide the relationship of powertrains to axes. For complex kinematics this does not need to be a one to one relationship, because a powertrain might influence the motion of more than one axis. This reference connects all axis to a powertrain that that move when only this powertrain moves and all other powertrains stand still.",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=robotics;i=18570",
                browseName="ns=robotics;MotionProfile",
                description="The kind of axis motion as defined with the AxisMotionProfileEnumeration.",
                dataType=robotics_datypes.AxisMotionProfileEnumeration,
            )
        ),
        o6.hasComponent(o6.ns["ns=robotics;i=18537"]),
    ],
)
o6.reference(robotics_objtypes.PowerTrainType, robotics_reftypes.Moves, o6.ns["ns=robotics;i=18536"])
robotics_objtypes.PowerTrainType(
    nodeId="ns=robotics;i=18613",
    browseName="ns=robotics;<PowerTrainIdentifier>",
    description="HasSlave is a reference to provide the master-slave relationship of powertrains which provide torque for a common axis. The InverseName is IsSlaveOf.",
    modellingRule="OptionalPlaceholder",
)
o6.reference(robotics_objtypes.PowerTrainType, robotics_reftypes.HasSlave, o6.ns["ns=robotics;i=18613"])
o6.reference(o6.ns["ns=robotics;i=18613"], "i=47", o6.ns["ns=robotics;i=15998"])
robotics_objtypes.EmergencyStopFunctionType(
    nodeId="ns=robotics;i=18806",
    browseName="ns=robotics;<EmergencyStopFunctionIdentifier>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=robotics;i=18807",
                browseName="ns=robotics;Name",
                description="The Name of the EmergencyStopFunctionType provides a manufacturer-specific emergency stop function identifier within the safety system.",
                dataType=o6.String,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=robotics;i=18808",
                browseName="ns=robotics;Active",
                description="The Active variable is TRUE if this particular emergency stop function is active, e.g. that the emergency stop button is pressed, FALSE otherwise.",
                dataType=o6.Boolean,
            )
        ),
    ],
)
ns0.objtypes.FolderType(
    nodeId="ns=robotics;i=17221",
    browseName="ns=robotics;EmergencyStopFunctions",
    description="EmergencyStopFunctions is a container for one or more instances of the EmergencyStopFunctionType.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=robotics;i=18806"])],
)
o6.reference(robotics_objtypes.SafetyStateType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=17221"])
robotics_objtypes.ProtectiveStopFunctionType(
    nodeId="ns=robotics;i=18809",
    browseName="ns=robotics;<ProtectiveStopFunctionIdentifier>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=robotics;i=18810",
                browseName="ns=robotics;Name",
                description="The Name of the ProtectiveStopFunctionType provides a manufacturer-specific protective stop function identifier within the safety system.",
                dataType=o6.String,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=robotics;i=18811",
                browseName="ns=robotics;Enabled",
                description="–\tThe Enabled variable is TRUE if this protective stop function is currently supervising the system, FALSE otherwise. A protective stop function may or may not be enabled at all times, e.g. the protective stop function of the safety doors are typically enabled in automatic operational mode and disabled in manual mode. On the other hand for example, the protective stop function of the teach pendant enabling device is enabled in manual modes and disabled in automatic modes.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=robotics;i=18812",
                browseName="ns=robotics;Active",
                description="–\tThe Active variable is TRUE if this particular protective stop function is active, i.e. that a stop is initiated, FALSE otherwise. If Enabled is FALSE then Active shall be FALSE.",
                dataType=o6.Boolean,
            )
        ),
    ],
)
ns0.objtypes.FolderType(
    nodeId="ns=robotics;i=17225",
    browseName="ns=robotics;ProtectiveStopFunctions",
    description="ProtectiveStopFunctions is a container for one or more instances of the ProtectiveStopFunctionType.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=robotics;i=18809"])],
)
o6.reference(robotics_objtypes.SafetyStateType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=17225"])
di.objtypes.ComponentType(
    nodeId="ns=robotics;i=18813",
    browseName="ns=robotics;<ComponentIdentifier>",
    description="The intention is to integrate inside this container devices which are defined in other companion specifications using DI.",
    modellingRule="MandatoryPlaceholder",
    _allow_abstract=True,
)
o6.reference(o6.ns["ns=robotics;i=18813"], "i=17603", "ns=di;i=15035")
o6.reference(o6.ns["ns=robotics;i=18813"], "i=17603", "ns=di;i=15048")
ns0.objtypes.FolderType(
    nodeId="ns=robotics;i=17252",
    browseName="ns=robotics;Components",
    description="Components is a container for one or more instances of subtypes of ComponentType defined in OPC UA DI. The listed components are installed in the motion device system, e.g. a processing-unit, a power-supply, an IO-board or a drive, and have an electrical interface to the controller.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=robotics;i=18813"])],
)
o6.reference(robotics_objtypes.ControllerType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=17252"])
di.objtypes.SoftwareType(
    nodeId="ns=robotics;i=18847",
    browseName="ns=robotics;<SoftwareIdentifier>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=18868", browseName="ns=di;Manufacturer", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=18870", browseName="ns=di;Model", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=18873", browseName="ns=di;SoftwareRevision", dataType=o6.String)),
    ],
)
o6.reference(o6.ns["ns=robotics;i=15483"], "i=47", o6.ns["ns=robotics;i=18847"])
ns0.objtypes.FolderType(
    nodeId="ns=robotics;i=15800",
    browseName="ns=robotics;Software",
    description="Software is a container for one or more instances of SoftwareType defined in OPC UA DI.",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=robotics;i=18847"])],
)
o6.reference(robotics_objtypes.ControllerType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=15800"])
ns0.objtypes.BaseObjectType(
    nodeId="ns=robotics;i=18882",
    browseName="ns=di;ParameterSet",
    description="Flat list of Parameters",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=robotics;i=18915", browseName="ns=robotics;TaskProgramName", description="A customer given identifier for the task program.", dataType=o6.String
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=robotics;i=18916",
                browseName="ns=robotics;TaskProgramLoaded",
                description="The TaskProgramLoaded variable is TRUE if a task program is loaded in the task control, FALSE otherwise.",
                dataType=o6.Boolean,
            )
        ),
    ],
)
robotics_objtypes.TaskControlType(
    nodeId="ns=robotics;i=18881",
    browseName="ns=robotics;<TaskControlIdentifier>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=robotics;i=18914",
                browseName="ns=di;ComponentName",
                description="A user writable name provided by the vendor, integrator or user of the device.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasComponent(o6.ns["ns=robotics;i=18882"]),
    ],
)
o6.reference(o6.ns["ns=robotics;i=15518"], "i=47", o6.ns["ns=robotics;i=18881"])
ns0.objtypes.FolderType(
    nodeId="ns=robotics;i=15826",
    browseName="ns=robotics;TaskControls",
    description="TaskControls is a container for one or more instances of TaskControlType.",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=robotics;i=18881"])],
)
o6.reference(robotics_objtypes.ControllerType, ns0.reftypes.HasComponent, o6.ns["ns=robotics;i=15826"])
ns0.objtypes.BaseObjectType(
    nodeId="ns=robotics;i=18919",
    browseName="ns=di;ParameterSet",
    description="Flat list of Parameters",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=robotics;i=18961",
                browseName="ns=robotics;OperationalMode",
                description="The OperationalMode variable provides information about the current operational mode. Allowed values are described in OperationalModeEnumeration, see ISO 10218-1:2011 Ch.5.7 Operational Modes.",
                dataType=robotics_datypes.OperationalModeEnumeration,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=robotics;i=18962",
                browseName="ns=robotics;EmergencyStop",
                description="The EmergencyStop variable is TRUE if one or more of the emergency stop functions in the robot system are active, FALSE otherwise. If the EmergencyStopFunctions object is provided, then the value of this variable is TRUE if one or more of the listed emergency stop functions are active.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=robotics;i=18963",
                browseName="ns=robotics;ProtectiveStop",
                description="The ProtectiveStop variable is TRUE if one or more of the enabled protective stop functions in the system are active, FALSE otherwise. If the ProtectiveStopFunctions object is provided, then the value of this variable is TRUE if one or more of the listed protective stop functions are enabled and active.",
                dataType=o6.Boolean,
            )
        ),
    ],
)
robotics_objtypes.SafetyStateType(
    nodeId="ns=robotics;i=18918",
    browseName="ns=robotics;<SafetyStatesIdentifier>",
    description="The relationship of safety states to a controller.",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(o6.ns["ns=robotics;i=18919"])],
)
o6.reference(robotics_objtypes.ControllerType, robotics_reftypes.HasSafetyStates, o6.ns["ns=robotics;i=18918"])
ns0.objtypes.BaseObjectType(
    nodeId="ns=robotics;i=18965",
    browseName="ns=di;ParameterSet",
    description="Flat list of Parameters",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=robotics;i=19001",
                browseName="ns=robotics;SpeedOverride",
                description="SpeedOverride provides the current speed setting in percent of programmed speed (0 - 100%).",
                dataType=o6.Double,
            )
        )
    ],
)
ns0.objtypes.FolderType(
    nodeId="ns=robotics;i=19002",
    browseName="ns=robotics;Axes",
    description="Axes is a container for one or more instances of the AxisType.",
    references=[o6.hasComponent(o6.ns["ns=robotics;i=15743"])],
)
ns0.objtypes.FolderType(
    nodeId="ns=robotics;i=19080",
    browseName="ns=robotics;PowerTrains",
    description="PowerTrains is a container for one or more instances of the PowerTrainType.",
    references=[o6.hasComponent(o6.ns["ns=robotics;i=15905"])],
)
robotics_objtypes.MotionDeviceType(
    nodeId="ns=robotics;i=18964",
    browseName="ns=robotics;<MotionDeviceIdentifier>",
    description="The relationship of a motion device and controller.",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=18985", browseName="ns=di;Manufacturer", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=18987", browseName="ns=di;Model", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=18988", browseName="ns=di;SerialNumber", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=18993", browseName="ns=di;ProductCode", dataType=o6.String)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=robotics;i=18998",
                browseName="ns=robotics;MotionDeviceCategory",
                description="The variable MotionDeviceCategory provides the kind of motion device defined by MotionDeviceCategoryEnumeration based on ISO 8373.",
                dataType=robotics_datypes.MotionDeviceCategoryEnumeration,
            )
        ),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=robotics;i=6003", browseName="ns=robotics;TaskControlReference", dataType=o6.NodeId)),
        o6.hasComponent(o6.ns["ns=robotics;i=18965"]),
        o6.hasComponent(o6.ns["ns=robotics;i=19002"]),
        o6.hasComponent(o6.ns["ns=robotics;i=19080"]),
    ],
)
o6.reference(robotics_objtypes.ControllerType, robotics_reftypes.Controls, o6.ns["ns=robotics;i=18964"])
ns0.objtypes.BaseObjectType(
    nodeId="ns=robotics;i=19255",
    browseName="ns=di;ParameterSet",
    description="Flat list of Parameters",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=robotics;i=19291",
                browseName="ns=robotics;SpeedOverride",
                description="SpeedOverride provides the current speed setting in percent of programmed speed (0 - 100%).",
                dataType=o6.Double,
            )
        )
    ],
)
ns0.objtypes.FolderType(nodeId="ns=robotics;i=19292", browseName="ns=robotics;Axes", description="Axes is a container for one or more instances of the AxisType.")
o6.reference(o6.ns["ns=robotics;i=19292"], "i=47", o6.ns["ns=robotics;i=15743"])
ns0.objtypes.FolderType(
    nodeId="ns=robotics;i=19370", browseName="ns=robotics;PowerTrains", description="PowerTrains is a container for one or more instances of the PowerTrainType."
)
o6.reference(o6.ns["ns=robotics;i=19370"], "i=47", o6.ns["ns=robotics;i=15905"])
robotics_objtypes.MotionDeviceType(
    nodeId="ns=robotics;i=19254",
    browseName="ns=robotics;<MotionDeviceIdentifier>",
    description="Controls is a reference to provide the relationship between a task control and a motion device.",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=19275", browseName="ns=di;Manufacturer", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=19277", browseName="ns=di;Model", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=19278", browseName="ns=di;SerialNumber", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=19283", browseName="ns=di;ProductCode", dataType=o6.String)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=robotics;i=19288",
                browseName="ns=robotics;MotionDeviceCategory",
                description="The variable MotionDeviceCategory provides the kind of motion device defined by MotionDeviceCategoryEnumeration based on ISO 8373.",
                dataType=robotics_datypes.MotionDeviceCategoryEnumeration,
            )
        ),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=robotics;i=6004", browseName="ns=robotics;TaskControlReference", dataType=o6.NodeId)),
        o6.hasComponent(o6.ns["ns=robotics;i=19255"]),
        o6.hasComponent(o6.ns["ns=robotics;i=19292"]),
        o6.hasComponent(o6.ns["ns=robotics;i=19370"]),
    ],
)
o6.reference(robotics_objtypes.TaskControlType, robotics_reftypes.Controls, o6.ns["ns=robotics;i=19254"])


del Any, TYPE_CHECKING, uuid, o6, di, ia, ns0, robotics_reftypes, robotics_datypes, robotics_objtypes
