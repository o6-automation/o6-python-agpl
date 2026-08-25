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

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(nodeId="ns=robotics;i=1007", browseName="ns=robotics;ExecutingSubstateMachineType", displayName="ExecutingSubstateMachineType")
class ExecutingSubstateMachineType(ns0.objtypes.FiniteStateMachineType):
    lastTransition: ns0.vartypes.FiniteTransitionVariableType
    lastTransitionReason: ns0.vartypes.MultiStateValueDiscreteType
    running: ns0.objtypes.InitialStateType
    runningToStopping: ns0.objtypes.TransitionType
    stopping: ns0.objtypes.StateType


o6.reference(ExecutingSubstateMachineType, "i=41", "i=2311")


@o6.objecttype(nodeId="ns=robotics;i=1009", browseName="ns=robotics;IdleSubstateMachineType", displayName="IdleSubstateMachineType")
class IdleSubstateMachineType(ns0.objtypes.FiniteStateMachineType):
    gettingReady: ns0.objtypes.StateType
    gettingReadyToStandBy: ns0.objtypes.TransitionType
    lastTransition: ns0.vartypes.FiniteTransitionVariableType
    lastTransitionReason: ns0.vartypes.MultiStateValueDiscreteType
    standBy: ns0.objtypes.InitialStateType
    standByToGettingReady: ns0.objtypes.TransitionType


o6.reference(IdleSubstateMachineType, "i=41", "i=2311")


@o6.objecttype(
    nodeId="ns=robotics;i=1018",
    browseName="ns=robotics;LoadType",
    displayName="LoadType",
    description="The LoadType is for describing loads mounted on the motion device typically by an integrator or a customer.",
)
class LoadType(ns0.objtypes.BaseObjectType):
    centerOfMass: ns0.vartypes.ThreeDFrameType | None
    inertia: ns0.vartypes.ThreeDVectorType | None
    mass: ns0.vartypes.AnalogUnitType


@o6.objecttype(nodeId="ns=robotics;i=1016", browseName="ns=robotics;TaskModuleType", displayName="TaskModuleType")
class TaskModuleType(ns0.objtypes.BaseObjectType):
    isReferenced: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6056", browseName="ns=robotics;IsReferenced", dataType=o6.Boolean, accessLevel=3)
    )
    name: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6054", browseName="ns=robotics;Name", dataType=o6.String, accessLevel=3))
    version: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6055", browseName="ns=robotics;Version", dataType=o6.String, accessLevel=3)
    )


@o6.objecttype(nodeId="ns=robotics;i=1028", browseName="ns=robotics;SystemOperationType", displayName="SystemOperationType")
class SystemOperationType(ns0.objtypes.BaseObjectType):
    conditions: ns0.objtypes.FolderType | None
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=robotics;i=6130", browseName="DefaultInstanceBrowseName", dataType=o6.QualifiedName, value=o6.QualifiedName("ia:SystemOperation"), accessLevel=3
        )
    )
    systemOperationStateMachine: SystemOperationStateMachineType


@o6.objecttype(nodeId="ns=robotics;i=1008", browseName="ns=robotics;TaskControlOperationType", displayName="TaskControlOperationType")
class TaskControlOperationType(ns0.objtypes.BaseObjectType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=robotics;i=6132", browseName="DefaultInstanceBrowseName", dataType=o6.QualifiedName, value=o6.QualifiedName("robotics:TaskControlOperation"), accessLevel=3
        )
    )
    motionDevicesUnderControl: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6131", browseName="ns=robotics;MotionDevicesUnderControl", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])
    )
    taskControlStateMachine: TaskControlStateMachineType


@o6.objecttype(nodeId="ns=robotics;i=1015", browseName="ns=robotics;MultiAcknowledgeableConditionType", displayName="MultiAcknowledgeableConditionType")
class MultiAcknowledgeableConditionType(ns0.objtypes.AcknowledgeableConditionType):
    conditionDescriptions: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=robotics;i=6140", browseName="ns=robotics;ConditionDescriptions", dataType=o6.LocalizedText, valueRank=1, arrayDimensions=[0], accessLevel=3
        )
    )


@o6.objecttype(
    nodeId="ns=robotics;i=1002",
    browseName="ns=robotics;MotionDeviceSystemType",
    displayName="MotionDeviceSystemType",
    description="Contains the set of controllers and motion devices in a closely-coupled motion device system.",
)
class MotionDeviceSystemType(di.objtypes.ComponentType):
    componentName: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6171", browseName="ns=di;ComponentName", dataType=o6.LocalizedText)
    )
    controllers: ns0.objtypes.FolderType
    motionDevices: ns0.objtypes.FolderType
    safetyStates: ns0.objtypes.FolderType


@o6.objecttype(
    nodeId="ns=robotics;i=1013",
    browseName="ns=robotics;SafetyStateType",
    displayName="SafetyStateType",
    description="SafetyStateType describes the safety states of the motion devices and controllers. One motion device system is associated with one or more instances of the SafetyStateType.",
)
class SafetyStateType(di.objtypes.ComponentType):
    componentName: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6179", browseName="ns=di;ComponentName", dataType=o6.LocalizedText)
    )
    emergencyStopFunctions: ns0.objtypes.FolderType | None
    parameterSet: ns0.objtypes.BaseObjectType
    protectiveStopFunctions: ns0.objtypes.FolderType | None


ns0.vartypes.PropertyType(
    nodeId="ns=robotics;i=6023",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=robotics;i=7001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="Status",
            dataType=o6.Int32,
            valueRank=-1,
            description=o6.LocalizedText(
                "0 &#8211; OK\nValues &gt; 0 are reserved for errors defined by this and future standards.\nValues &lt; 0 shall be used for application-specific errors"
            ),
        )
    ],
)
o6.call(nodeId="ns=robotics;i=7001", browseName="ns=robotics;Start", outputArgs=o6.hasProperty(o6.ns["ns=robotics;i=6023"]))

ns0.vartypes.PropertyType(
    nodeId="ns=robotics;i=6024",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=robotics;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="StopMode",
            dataType=o6.Int64,
            valueRank=-1,
            description=o6.LocalizedText(
                "provides a way to differentiate between different stop modes. This parameter should correspond to one of the values in the PossibleStopModes array"
            ),
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=robotics;i=6025",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=robotics;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="Status",
            dataType=o6.Int32,
            valueRank=-1,
            description=o6.LocalizedText(
                "0 &#8211; OK\nValues &gt; 0 are reserved for errors defined by this and future standards.\nValues &lt; 0 shall be used for application-specific errors"
            ),
        )
    ],
)
o6.call(nodeId="ns=robotics;i=7002", browseName="ns=robotics;Stop", inputArgs=o6.hasProperty(o6.ns["ns=robotics;i=6024"]), outputArgs=o6.hasProperty(o6.ns["ns=robotics;i=6025"]))


@o6.objecttype(nodeId="ns=robotics;i=1006", browseName="ns=robotics;OperationStateMachineType", displayName="OperationStateMachineType", isAbstract=True)
class OperationStateMachineType(ns0.objtypes.FiniteStateMachineType):
    configuredDefaultStopMode: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=robotics;i=6009", browseName="ns=robotics;ConfiguredDefaultStopMode", dataType=o6.Int16, accessLevel=3)
    )
    executing: ns0.objtypes.StateType
    executingToIdle: ns0.objtypes.TransitionType
    executingToReady: ns0.objtypes.TransitionType
    idle: ns0.objtypes.StateType
    idleToIdle: ns0.objtypes.TransitionType
    idleToReady: ns0.objtypes.TransitionType
    lastTransition: ns0.vartypes.FiniteTransitionVariableType
    lastTransitionReason: ns0.vartypes.MultiStateValueDiscreteType
    possibleStopModes: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=robotics;i=6008",
            browseName="ns=robotics;PossibleStopModes",
            dataType=ns0.datatypes.EnumValueType,
            valueRank=1,
            arrayDimensions=[5],
            value=[
                ns0.datatypes.EnumValueType(
                    value=1,
                    displayName=o6.LocalizedText("OnPath", "en"),
                    description=o6.LocalizedText("Stop program execution in a controlled manner along the programmed path", "en"),
                ),
                ns0.datatypes.EnumValueType(
                    value=2,
                    displayName=o6.LocalizedText("EndOfCycle", "en"),
                    description=o6.LocalizedText("Stop program execution when the current production cycle has been finished", "en"),
                ),
                ns0.datatypes.EnumValueType(
                    value=3,
                    displayName=o6.LocalizedText("ProcessStop", "en"),
                    description=o6.LocalizedText(
                        "Application dependent stop instruction that stops program execution at a favourable point for the application, e.g. at the end of a paint stroke or sealing bead",
                        "en",
                    ),
                ),
                ns0.datatypes.EnumValueType(
                    value=4,
                    displayName=o6.LocalizedText("QuickStop", "en"),
                    description=o6.LocalizedText(
                        "This stop is performed by ramping down motion as fast as possible using optimum motor performance. The robot may not stay on the path", "en"
                    ),
                ),
                ns0.datatypes.EnumValueType(
                    value=5,
                    displayName=o6.LocalizedText("EndOfInstruction", "en"),
                    description=o6.LocalizedText("This stop can be used to stop the program execution when the current instruction is completed", "en"),
                ),
            ],
            accessLevel=3,
        )
    )
    ready: ns0.objtypes.StateType
    readyToExecuting: ns0.objtypes.TransitionType
    readyToIdle: ns0.objtypes.TransitionType
    start: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=robotics;i=7001"])
    stop: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=robotics;i=7002"])


o6.reference(OperationStateMachineType, "i=41", "i=2311")


ns0.vartypes.PropertyType(
    nodeId="ns=robotics;i=6053",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=robotics;i=7003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="Status",
            dataType=o6.Int32,
            valueRank=-1,
            description=o6.LocalizedText(
                "0 &#8211; OK &#8211; Everything is OK\n1 &#8211; E_SystemState &#8211; The system is not in correct state for this operation\n2 &#8211; E_UnexpectedError &#8211; Unexpected Error during the method call\n3 &#8211; E_ActiveAlarm &#8211; An Active Alarm prevents the system start\n4 &#8211; E_AcknowledgeRequired &#8211; Condition needs to be acknowledged\n&lt;0 &#8211; shall be used for vendor-specific errors\n&gt;0 &#8211; are reserved for errors defined by this and future standards"
            ),
        )
    ],
)
o6.call(nodeId="ns=robotics;i=7003", browseName="ns=robotics;ResetToProgramStart", outputArgs=o6.hasProperty(o6.ns["ns=robotics;i=6053"]))


@o6.objecttype(nodeId="ns=robotics;i=1012", browseName="ns=robotics;ReadySubstateMachineType", displayName="ReadySubstateMachineType")
class ReadySubstateMachineType(ns0.objtypes.FiniteStateMachineType):
    atProgramStart: ns0.objtypes.StateType
    lastTransition: ns0.vartypes.FiniteTransitionVariableType
    lastTransitionReason: ns0.vartypes.MultiStateValueDiscreteType
    programStartToSuspended: ns0.objtypes.TransitionType
    resetToProgramStart: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=robotics;i=7003"])
    suspended: ns0.objtypes.StateType
    suspendedToProgramStart: ns0.objtypes.TransitionType


o6.reference(ReadySubstateMachineType, "i=41", "i=2311")


ns0.vartypes.PropertyType(
    nodeId="ns=robotics;i=6064",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=robotics;i=7004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="Status",
            dataType=o6.Int32,
            valueRank=-1,
            description=o6.LocalizedText(
                "0 &#8211; OK\nValues &gt; 0 are reserved for errors defined by this and future standards.\nValues &lt; 0 shall be used for application-specific errors"
            ),
        )
    ],
)
o6.call(nodeId="ns=robotics;i=7004", browseName="ns=robotics;Start", outputArgs=o6.hasProperty(o6.ns["ns=robotics;i=6064"]))

ns0.vartypes.PropertyType(
    nodeId="ns=robotics;i=6065",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=robotics;i=7005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="StopMode",
            dataType=o6.Int64,
            valueRank=-1,
            description=o6.LocalizedText(
                "provides a way to differentiate between different stop modes. This parameter should correspond to one of the values in the PossibleStopModes array"
            ),
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=robotics;i=6066",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=robotics;i=7005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="Status",
            dataType=o6.Int32,
            valueRank=-1,
            description=o6.LocalizedText(
                "0 &#8211; OK\nValues &gt; 0 are reserved for errors defined by this and future standards.\nValues &lt; 0 shall be used for application-specific errors"
            ),
        )
    ],
)
o6.call(nodeId="ns=robotics;i=7005", browseName="ns=robotics;Stop", inputArgs=o6.hasProperty(o6.ns["ns=robotics;i=6065"]), outputArgs=o6.hasProperty(o6.ns["ns=robotics;i=6066"]))

ns0.vartypes.PropertyType(
    nodeId="ns=robotics;i=6068",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=robotics;i=7006",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="Status",
            dataType=o6.Int32,
            valueRank=-1,
            description=o6.LocalizedText(
                "0 &#8211; OK\nValues &gt; 0 are reserved for errors defined by this and future standards.\nValues &lt; 0 shall be used for application-specific errors"
            ),
        )
    ],
)
o6.call(nodeId="ns=robotics;i=7006", browseName="ns=robotics;GetReady", outputArgs=o6.hasProperty(o6.ns["ns=robotics;i=6068"]))

ns0.vartypes.PropertyType(
    nodeId="ns=robotics;i=6070",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=robotics;i=7007",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="Status",
            dataType=o6.Int32,
            valueRank=-1,
            description=o6.LocalizedText(
                "0 &#8211; OK\nValues &gt; 0 are reserved for errors defined by this and future standards.\nValues &lt; 0 shall be used for application-specific errors"
            ),
        )
    ],
)
o6.call(nodeId="ns=robotics;i=7007", browseName="ns=robotics;StandDown", outputArgs=o6.hasProperty(o6.ns["ns=robotics;i=6070"]))


@o6.objecttype(nodeId="ns=robotics;i=1021", browseName="ns=robotics;SystemOperationStateMachineType", displayName="SystemOperationStateMachineType")
class SystemOperationStateMachineType(OperationStateMachineType):
    configuredDefaultStopMode: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=robotics;i=6057", browseName="ns=robotics;ConfiguredDefaultStopMode", dataType=o6.Int16, accessLevel=3)
    )
    executing: ns0.objtypes.StateType
    executingSubstateMachine: ExecutingSubstateMachineType | None
    executingToIdle: ns0.objtypes.TransitionType
    executingToReady: ns0.objtypes.TransitionType
    getReady: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=robotics;i=7006"])
    idle: ns0.objtypes.StateType
    idleSubstateMachine: IdleSubstateMachineType | None
    idleToIdle: ns0.objtypes.TransitionType
    idleToReady: ns0.objtypes.TransitionType
    lastTransition: ns0.vartypes.FiniteTransitionVariableType
    lastTransitionReason: ns0.vartypes.MultiStateValueDiscreteType
    possibleStopModes: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=robotics;i=6063",
            browseName="ns=robotics;PossibleStopModes",
            dataType=ns0.datatypes.EnumValueType,
            valueRank=1,
            arrayDimensions=[5],
            value=[
                ns0.datatypes.EnumValueType(
                    value=1,
                    displayName=o6.LocalizedText("OnPath", "en"),
                    description=o6.LocalizedText("Stop program execution in a controlled manner along the programmed path", "en"),
                ),
                ns0.datatypes.EnumValueType(
                    value=2,
                    displayName=o6.LocalizedText("EndOfCycle", "en"),
                    description=o6.LocalizedText("Stop program execution when the current production cycle has been finished", "en"),
                ),
                ns0.datatypes.EnumValueType(
                    value=3,
                    displayName=o6.LocalizedText("ProcessStop", "en"),
                    description=o6.LocalizedText(
                        "Application dependent stop instruction that stops program execution at a favourable point for the application, e.g. at the end of a paint stroke or sealing bead",
                        "en",
                    ),
                ),
                ns0.datatypes.EnumValueType(
                    value=4,
                    displayName=o6.LocalizedText("QuickStop", "en"),
                    description=o6.LocalizedText(
                        "This stop is performed by ramping down motion as fast as possible using optimum motor performance. The robot may not stay on the path", "en"
                    ),
                ),
                ns0.datatypes.EnumValueType(
                    value=5,
                    displayName=o6.LocalizedText("EndOfInstruction", "en"),
                    description=o6.LocalizedText("This stop can be used to stop the program execution when the current instruction is completed", "en"),
                ),
            ],
            accessLevel=3,
        )
    )
    ready: ns0.objtypes.StateType
    readyToExecuting: ns0.objtypes.TransitionType
    readyToIdle: ns0.objtypes.TransitionType
    standDown: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=robotics;i=7007"])
    start: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=robotics;i=7004"])
    stop: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=robotics;i=7005"])


o6.reference(SystemOperationStateMachineType, "i=41", "i=2311")


ns0.vartypes.PropertyType(
    nodeId="ns=robotics;i=6101",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=robotics;i=7008",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="Status",
            dataType=o6.Int32,
            valueRank=-1,
            description=o6.LocalizedText(
                "0 &#8211; OK\nValues &gt; 0 are reserved for errors defined by this and future standards.\nValues &lt; 0 shall be used for application-specific errors"
            ),
        )
    ],
)
o6.call(nodeId="ns=robotics;i=7008", browseName="ns=robotics;Start", outputArgs=o6.hasProperty(o6.ns["ns=robotics;i=6101"]))

ns0.vartypes.PropertyType(
    nodeId="ns=robotics;i=6102",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=robotics;i=7009",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="StopMode",
            dataType=o6.Int64,
            valueRank=-1,
            description=o6.LocalizedText(
                "provides a way to differentiate between different stop modes. This parameter should correspond to one of the values in the PossibleStopModes array"
            ),
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=robotics;i=6103",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=robotics;i=7009",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="Status",
            dataType=o6.Int32,
            valueRank=-1,
            description=o6.LocalizedText(
                "0 &#8211; OK\nValues &gt; 0 are reserved for errors defined by this and future standards.\nValues &lt; 0 shall be used for application-specific errors"
            ),
        )
    ],
)
o6.call(nodeId="ns=robotics;i=7009", browseName="ns=robotics;Stop", inputArgs=o6.hasProperty(o6.ns["ns=robotics;i=6102"]), outputArgs=o6.hasProperty(o6.ns["ns=robotics;i=6103"]))

ns0.vartypes.PropertyType(
    nodeId="ns=robotics;i=6141",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=robotics;i=7010",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="Id",
            dataType=o6.ExpandedNodeId,
            valueRank=-1,
            description=o6.LocalizedText("ExpandedNodeId pointing to an instance of FileType representing a task control program or module"),
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=robotics;i=6142",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=robotics;i=7010",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="Status",
            dataType=o6.Int32,
            valueRank=-1,
            description=o6.LocalizedText(
                "0 &#8211; OK &#8211; Everything is OK\n1 &#8211; E_SystemState &#8211; The system is not in correct state for this operation\n2 &#8211; E_UnexpectedError &#8211; Unexpected Error during the method call\n3 &#8211; E_ActiveAlarm &#8211; An Active Alarm prevents the system start\n4 &#8211; E_AcknowledgeRequired &#8211; Condition needs to be acknowledged\n&lt;0 &#8211; shall be used for vendor-specific errors\n&gt;0 &#8211; are reserved for errors defined by this and future standards"
            ),
        )
    ],
)
o6.call(
    nodeId="ns=robotics;i=7010",
    browseName="ns=robotics;LoadByNodeId",
    inputArgs=o6.hasProperty(o6.ns["ns=robotics;i=6141"]),
    outputArgs=o6.hasProperty(o6.ns["ns=robotics;i=6142"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=robotics;i=6143",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=robotics;i=7011",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Name", dataType=o6.String, valueRank=-1, description=o6.LocalizedText("Name to identify a task control program or module"))],
)
ns0.vartypes.PropertyType(
    nodeId="ns=robotics;i=6144",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=robotics;i=7011",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="Status",
            dataType=o6.Int32,
            valueRank=-1,
            description=o6.LocalizedText(
                "0 &#8211; OK &#8211; Everything is OK\n1 &#8211; E_SystemState &#8211; The system is not in correct state for this operation\n2 &#8211; E_UnexpectedError &#8211; Unexpected Error during the method call\n3 &#8211; E_ActiveAlarm &#8211; An Active Alarm prevents the system start\n4 &#8211; E_AcknowledgeRequired &#8211; Condition needs to be acknowledged\n&lt;0 &#8211; shall be used for vendor-specific errors\n&gt;0 &#8211; are reserved for errors defined by this and future standards"
            ),
        )
    ],
)
o6.call(
    nodeId="ns=robotics;i=7011", browseName="ns=robotics;LoadByName", inputArgs=o6.hasProperty(o6.ns["ns=robotics;i=6143"]), outputArgs=o6.hasProperty(o6.ns["ns=robotics;i=6144"])
)

ns0.vartypes.PropertyType(
    nodeId="ns=robotics;i=6145",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=robotics;i=7012",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="Status",
            dataType=o6.Int32,
            valueRank=-1,
            description=o6.LocalizedText(
                "0 &#8211; OK &#8211; Everything is OK\n1 &#8211; E_SystemState &#8211; The system is not in correct state for this operation\n2 &#8211; E_UnexpectedError &#8211; Unexpected Error during the method call\n3 &#8211; E_ActiveAlarm &#8211; An Active Alarm prevents the system start\n4 &#8211; E_AcknowledgeRequired &#8211; Condition needs to be acknowledged\n&lt;0 &#8211; shall be used for vendor-specific errors\n&gt;0 &#8211; are reserved for errors defined by this and future standards"
            ),
        )
    ],
)
o6.call(nodeId="ns=robotics;i=7012", browseName="ns=robotics;UnloadProgram", outputArgs=o6.hasProperty(o6.ns["ns=robotics;i=6145"]))

ns0.vartypes.PropertyType(
    nodeId="ns=robotics;i=6146",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=robotics;i=7013",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Id", dataType=o6.ExpandedNodeId, valueRank=-1, description=o6.LocalizedText("Expanded NodeId of the module to be unloaded"))],
)
ns0.vartypes.PropertyType(
    nodeId="ns=robotics;i=6147",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=robotics;i=7013",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="Status",
            dataType=o6.Int32,
            valueRank=-1,
            description=o6.LocalizedText(
                "0 &#8211; OK &#8211; Everything is OK\n1 &#8211; E_SystemState &#8211; The system is not in correct state for this operation\n2 &#8211; E_UnexpectedError &#8211; Unexpected Error during the method call\n3 &#8211; E_ActiveAlarm &#8211; An Active Alarm prevents the system start\n4 &#8211; E_AcknowledgeRequired &#8211; Condition needs to be acknowledged\n&lt;0 &#8211; shall be used for vendor-specific errors\n&gt;0 &#8211; are reserved for errors defined by this and future standards"
            ),
        )
    ],
)
o6.call(
    nodeId="ns=robotics;i=7013",
    browseName="ns=robotics;UnloadByNodeId",
    inputArgs=o6.hasProperty(o6.ns["ns=robotics;i=6146"]),
    outputArgs=o6.hasProperty(o6.ns["ns=robotics;i=6147"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=robotics;i=6067",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=robotics;i=7014",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Name", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=robotics;i=6069",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=robotics;i=7014",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Status", dataType=o6.Int32, valueRank=-1)],
)
o6.call(
    nodeId="ns=robotics;i=7014",
    browseName="ns=robotics;UnloadByName",
    inputArgs=o6.hasProperty(o6.ns["ns=robotics;i=6067"]),
    outputArgs=o6.hasProperty(o6.ns["ns=robotics;i=6069"]),
)


@o6.objecttype(nodeId="ns=robotics;i=1025", browseName="ns=robotics;TaskControlStateMachineType", displayName="TaskControlStateMachineType")
class TaskControlStateMachineType(OperationStateMachineType):
    configuredDefaultStopMode: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=robotics;i=6094", browseName="ns=robotics;ConfiguredDefaultStopMode", dataType=o6.Int16, accessLevel=3)
    )
    executing: ns0.objtypes.StateType
    executingToIdle: ns0.objtypes.TransitionType
    executingToReady: ns0.objtypes.TransitionType
    idle: ns0.objtypes.StateType
    idleToIdle: ns0.objtypes.TransitionType
    idleToReady: ns0.objtypes.TransitionType
    lastTransition: ns0.vartypes.FiniteTransitionVariableType
    lastTransitionReason: ns0.vartypes.MultiStateValueDiscreteType
    loadByName: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=robotics;i=7011"])
    loadByNodeId: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=robotics;i=7010"])
    possibleStopModes: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=robotics;i=6100",
            browseName="ns=robotics;PossibleStopModes",
            dataType=ns0.datatypes.EnumValueType,
            valueRank=1,
            arrayDimensions=[5],
            value=[
                ns0.datatypes.EnumValueType(
                    value=1,
                    displayName=o6.LocalizedText("OnPath", "en"),
                    description=o6.LocalizedText("Stop program execution in a controlled manner along the programmed path", "en"),
                ),
                ns0.datatypes.EnumValueType(
                    value=2,
                    displayName=o6.LocalizedText("EndOfCycle", "en"),
                    description=o6.LocalizedText("Stop program execution when the current production cycle has been finished", "en"),
                ),
                ns0.datatypes.EnumValueType(
                    value=3,
                    displayName=o6.LocalizedText("ProcessStop", "en"),
                    description=o6.LocalizedText(
                        "Application dependent stop instruction that stops program execution at a favourable point for the application, e.g. at the end of a paint stroke or sealing bead",
                        "en",
                    ),
                ),
                ns0.datatypes.EnumValueType(
                    value=4,
                    displayName=o6.LocalizedText("QuickStop", "en"),
                    description=o6.LocalizedText(
                        "This stop is performed by ramping down motion as fast as possible using optimum motor performance. The robot may not stay on the path", "en"
                    ),
                ),
                ns0.datatypes.EnumValueType(
                    value=5,
                    displayName=o6.LocalizedText("EndOfInstruction", "en"),
                    description=o6.LocalizedText("This stop can be used to stop the program execution when the current instruction is completed", "en"),
                ),
            ],
            accessLevel=3,
        )
    )
    ready: ns0.objtypes.StateType
    readySubstateMachine: ReadySubstateMachineType | None
    readyToExecuting: ns0.objtypes.TransitionType
    readyToIdle: ns0.objtypes.TransitionType
    start: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=robotics;i=7008"])
    stop: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=robotics;i=7009"])
    unloadByName: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=robotics;i=7014"])
    unloadByNodeId: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=robotics;i=7013"])
    unloadProgram: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=robotics;i=7012"])


o6.reference(TaskControlStateMachineType, "i=41", "i=2311")


ns0.objtypes.FolderType(nodeId="ns=robotics;i=15305", browseName="ns=robotics;Axes", description="Axes is a container for one or more instances of the AxisType.")
ns0.objtypes.FolderType(
    nodeId="ns=robotics;i=16443", browseName="ns=robotics;PowerTrains", description="PowerTrains is a container for one or more instances of the PowerTrainType."
)


@o6.objecttype(
    nodeId="ns=robotics;i=1004",
    browseName="ns=robotics;MotionDeviceType",
    displayName="MotionDeviceType",
    description="Represents a specific motion device in the motion device system like a robot, a linear unit or a positioner. A MotionDevice should have at least one axis.",
)
class MotionDeviceType(di.objtypes.ComponentType):
    additionalComponents: ns0.objtypes.FolderType | None
    assetId: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6172", browseName="ns=di;AssetId", dataType=o6.String))
    axes: ns0.objtypes.FolderType = o6.hasComponent(o6.ns["ns=robotics;i=15305"])
    componentName: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6173", browseName="ns=di;ComponentName", dataType=o6.LocalizedText)
    )
    deviceManual: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6174", browseName="ns=di;DeviceManual", dataType=o6.String))
    flangeLoad: LoadType | None
    manufacturer: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=16351", browseName="ns=di;Manufacturer", dataType=o6.LocalizedText))
    model: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=16353", browseName="ns=di;Model", dataType=o6.LocalizedText))
    motionDeviceCategory: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=robotics;i=16362",
            browseName="ns=robotics;MotionDeviceCategory",
            description="The variable MotionDeviceCategory provides the kind of motion device defined by MotionDeviceCategoryEnumeration based on ISO 8373.",
            dataType=robotics_datypes.MotionDeviceCategoryEnumeration,
        )
    )
    parameterSet: ns0.objtypes.BaseObjectType
    powerTrains: ns0.objtypes.FolderType = o6.hasComponent(o6.ns["ns=robotics;i=16443"])
    productCode: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=16359", browseName="ns=di;ProductCode", dataType=o6.String))
    serialNumber: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=16354", browseName="ns=di;SerialNumber", dataType=o6.String))
    taskControlReference: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=robotics;i=6001", browseName="ns=robotics;TaskControlReference", dataType=o6.NodeId)
    )


@o6.objecttype(nodeId="ns=robotics;i=16601", browseName="ns=robotics;AxisType", displayName="AxisType", description="The AxisType describes an axis of a motion device.")
class AxisType(di.objtypes.ComponentType):
    additionalLoad: LoadType | None
    assetId: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6175", browseName="ns=di;AssetId", dataType=o6.String))
    langlePowerTrainIdentifierRangle: PowerTrainType | None
    motionProfile: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=robotics;i=16637",
            browseName="ns=robotics;MotionProfile",
            description="The kind of axis motion as defined with the AxisMotionProfileEnumeration.",
            dataType=robotics_datypes.AxisMotionProfileEnumeration,
        )
    )
    parameterSet: ns0.objtypes.BaseObjectType


@o6.objecttype(
    nodeId="ns=robotics;i=16794",
    browseName="ns=robotics;PowerTrainType",
    displayName="PowerTrainType",
    description="The PowerTrainType represents instances of powertrains of a motion device.",
)
class PowerTrainType(di.objtypes.ComponentType):
    componentName: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6176", browseName="ns=di;ComponentName", dataType=o6.LocalizedText)
    )
    langleAxisIdentifierRangle: AxisType | None
    langleGearIdentifierRangle: GearType | None
    langlePowerTrainIdentifierRangle: PowerTrainType | None


@o6.objecttype(
    nodeId="ns=robotics;i=1019", browseName="ns=robotics;MotorType", displayName="MotorType", description="The MotorType is for representing instances of electric motors."
)
class MotorType(di.objtypes.ComponentType):
    assetId: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6177", browseName="ns=di;AssetId", dataType=o6.String))
    langleDriveIdentifierRangle: ns0.objtypes.BaseObjectType | None = o6.reference(
        ns0.objtypes.BaseObjectType(nodeId="ns=robotics;i=5060", browseName="ns=robotics;<DriveIdentifier>", modellingRule="OptionalPlaceholder"), "ns=robotics;i=18180"
    )
    manufacturer: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=17101", browseName="ns=di;Manufacturer", dataType=o6.LocalizedText))
    model: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=17103", browseName="ns=di;Model", dataType=o6.LocalizedText))
    parameterSet: ns0.objtypes.BaseObjectType
    productCode: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=17109", browseName="ns=di;ProductCode", dataType=o6.String))
    serialNumber: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=17104", browseName="ns=di;SerialNumber", dataType=o6.String))


@o6.objecttype(
    nodeId="ns=robotics;i=1022",
    browseName="ns=robotics;GearType",
    displayName="GearType",
    description="The GearType describes a gear in a powertrain, e.g. a gear box or a spindle.",
)
class GearType(di.objtypes.ComponentType):
    assetId: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6178", browseName="ns=di;AssetId", dataType=o6.String))
    gearRatio: ns0.vartypes.RationalNumberType
    manufacturer: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=17152", browseName="ns=di;Manufacturer", dataType=o6.LocalizedText))
    model: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=17154", browseName="ns=di;Model", dataType=o6.LocalizedText))
    pitch: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=robotics;i=17165",
            browseName="ns=robotics;Pitch",
            description="Pitch describes the distance covered in millimeters (mm) for linear motion per one revolution of the output side of the driving unit. Pitch is used in combination with GearRatio to describe the overall transmission from input to output of the gear.",
            dataType=o6.Double,
        )
    )
    productCode: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=17160", browseName="ns=di;ProductCode", dataType=o6.String))
    serialNumber: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=17155", browseName="ns=di;SerialNumber", dataType=o6.String))


@o6.objecttype(
    nodeId="ns=robotics;i=17230",
    browseName="ns=robotics;EmergencyStopFunctionType",
    displayName="EmergencyStopFunctionType",
    description="According to ISO 10218-1:2011 Ch.5.5.2 Emergency stop the robot shall have one or more emergency stop functions.",
)
class EmergencyStopFunctionType(ns0.objtypes.BaseObjectType):
    active: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=robotics;i=17232",
            browseName="ns=robotics;Active",
            description="The Active variable is TRUE if this particular emergency stop function is active, e.g. that the emergency stop button is pressed, FALSE otherwise.",
            dataType=o6.Boolean,
        )
    )
    name: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=robotics;i=17231",
            browseName="ns=robotics;Name",
            description="The Name of the EmergencyStopFunctionType provides a manufacturer-specific emergency stop function identifier within the safety system.",
            dataType=o6.String,
        )
    )


@o6.objecttype(
    nodeId="ns=robotics;i=17233",
    browseName="ns=robotics;ProtectiveStopFunctionType",
    displayName="ProtectiveStopFunctionType",
    description="According to ISO 10218-1:2011 Ch.5.5.3 the robot shall have one or more protective stop functions designed for the connection of external protective devices.",
)
class ProtectiveStopFunctionType(ns0.objtypes.BaseObjectType):
    active: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=robotics;i=17236",
            browseName="ns=robotics;Active",
            description="–\tThe Active variable is TRUE if this particular protective stop function is active, i.e. that a stop is initiated, FALSE otherwise. If Enabled is FALSE then Active shall be FALSE.",
            dataType=o6.Boolean,
        )
    )
    enabled: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=robotics;i=17235",
            browseName="ns=robotics;Enabled",
            description="–\tThe Enabled variable is TRUE if this protective stop function is currently supervising the system, FALSE otherwise. A protective stop function may or may not be enabled at all times, e.g. the protective stop function of the safety doors are typically enabled in automatic operational mode and disabled in manual mode. On the other hand for example, the protective stop function of the teach pendant enabling device is enabled in manual modes and disabled in automatic modes.",
            dataType=o6.Boolean,
        )
    )
    name: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=robotics;i=17234",
            browseName="ns=robotics;Name",
            description="The Name of the ProtectiveStopFunctionType provides a manufacturer-specific protective stop function identifier within the safety system.",
            dataType=o6.String,
        )
    )


@o6.objecttype(
    nodeId="ns=robotics;i=1003",
    browseName="ns=robotics;ControllerType",
    displayName="ControllerType",
    description="The ControllerType describes the control unit of motion devices. One motion device system can have one or more instances of the ControllerType.",
)
class ControllerType(di.objtypes.ComponentType):
    assetId: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6180", browseName="ns=di;AssetId", dataType=o6.String))
    componentName: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6181", browseName="ns=di;ComponentName", dataType=o6.LocalizedText)
    )
    components: ns0.objtypes.FolderType | None
    currentUser: UserType
    deviceManual: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6182", browseName="ns=di;DeviceManual", dataType=o6.String))
    langleMotionDeviceIdentifierRangle: MotionDeviceType | None
    langleSafetyStatesIdentifierRangle: SafetyStateType | None
    manufacturer: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=17237", browseName="ns=di;Manufacturer", dataType=o6.LocalizedText))
    model: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=17239", browseName="ns=di;Model", dataType=o6.LocalizedText))
    parameterSet: ns0.objtypes.BaseObjectType | None
    productCode: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=17245", browseName="ns=di;ProductCode", dataType=o6.String))
    programs: ns0.objtypes.FileDirectoryType | None
    serialNumber: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=17240", browseName="ns=di;SerialNumber", dataType=o6.String))
    software: ns0.objtypes.FolderType
    systemOperation: SystemOperationType | None
    taskControls: ns0.objtypes.FolderType


@o6.objecttype(
    nodeId="ns=robotics;i=17725",
    browseName="ns=robotics;AuxiliaryComponentType",
    displayName="AuxiliaryComponentType",
    description="Components mounted in a controller cabinet or a motion device e.g. an IO-board or a power supply.",
)
class AuxiliaryComponentType(di.objtypes.ComponentType):
    assetId: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6183", browseName="ns=di;AssetId", dataType=o6.String))
    productCode: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=robotics;i=17756",
            browseName="ns=di;ProductCode",
            description="The ProductCode property provides a unique combination of numbers and letters used to identify the product. It may be the order information displayed on type shields or in ERP systems.",
            dataType=o6.String,
        )
    )


@o6.objecttype(
    nodeId="ns=robotics;i=17793",
    browseName="ns=robotics;DriveType",
    displayName="DriveType",
    description="Drives (multi-slot or single-slot axis amplifier) mounted in a controller cabinet or a motion device.",
)
class DriveType(di.objtypes.ComponentType):
    assetId: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=robotics;i=6184", browseName="ns=di;AssetId", dataType=o6.String))
    productCode: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=robotics;i=17824",
            browseName="ns=di;ProductCode",
            description="The ProductCode property provides a unique combination of numbers and letters used to identify the product. It may be the order information displayed on type shields or in ERP systems.",
            dataType=o6.String,
        )
    )


@o6.objecttype(
    nodeId="ns=robotics;i=1011", browseName="ns=robotics;TaskControlType", displayName="TaskControlType", description="Represents a specific task control active on the controller."
)
class TaskControlType(di.objtypes.ComponentType):
    componentName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=robotics;i=17873",
            browseName="ns=di;ComponentName",
            description="A user writable name provided by the vendor, integrator or user of the device.",
            dataType=o6.LocalizedText,
        )
    )
    langleMotionDeviceIdentifierRangle: MotionDeviceType | None
    parameterSet: ns0.objtypes.BaseObjectType
    taskControlOperation: TaskControlOperationType | None
    taskModules: ns0.objtypes.FolderType | None


@o6.objecttype(
    nodeId="ns=robotics;i=18175",
    browseName="ns=robotics;UserType",
    displayName="UserType",
    description="The UserType ObjectType describes information of the registered user groups within the control system.",
)
class UserType(ns0.objtypes.BaseObjectType):
    level: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=robotics;i=18176",
            browseName="ns=robotics;Level",
            description="Provides information about the access rights and determines what can be viewed, updated, or deleted by a user",
            dataType=o6.String,
        )
    )
    name: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=robotics;i=18177", browseName="ns=robotics;Name", description="The name for the current user within the control system.", dataType=o6.String
        )
    )


del Any, TYPE_CHECKING, uuid, o6, di, ia, ns0, robotics_reftypes, robotics_datypes
