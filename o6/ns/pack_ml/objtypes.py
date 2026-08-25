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

"""Generated OPC UA pack_ml namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.ns0 as ns0
from . import reftypes as pack_ml_reftypes
from . import datatypes as pack_ml_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(nodeId="ns=pack_ml;i=4", browseName="ns=pack_ml;PackMLStatusObjectType", displayName="PackMLStatusObjectType")
class PackMLStatusObjectType(ns0.objtypes.BaseObjectType):
    curMachSpeed: ns0.vartypes.AnalogItemType
    equipmentBlocked: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pack_ml;i=211", browseName="ns=pack_ml;EquipmentBlocked", dataType=o6.Boolean)
    )
    equipmentStarved: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pack_ml;i=224", browseName="ns=pack_ml;EquipmentStarved", dataType=o6.Boolean)
    )
    machSpeed: ns0.vartypes.AnalogItemType
    materialInterlock: ns0.vartypes.BaseDataVariableType | None = o6.reference(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pack_ml;i=237", browseName="ns=pack_ml;MaterialInterlock", dataType=o6.Boolean, valueRank=1, arrayDimensions=[0]),
        "ns=pack_ml;i=21",
    )
    materialInterlocked: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pack_ml;i=236", browseName="ns=pack_ml;MaterialInterlocked", dataType=o6.Boolean)
    )
    parameter: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=pack_ml;i=121", browseName="ns=pack_ml;Parameter", dataType=pack_ml_datypes.PackMLDescriptorDataType, valueRank=1, arrayDimensions=[0]
        )
    )
    product: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=pack_ml;i=122", browseName="ns=pack_ml;Product", dataType=pack_ml_datypes.PackMLProductDataType, valueRank=1, arrayDimensions=[0]
        )
    )
    remoteParameter: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=pack_ml;i=123", browseName="ns=pack_ml;RemoteParameter", dataType=pack_ml_datypes.PackMLRemoteInterfaceDataType, valueRank=1, arrayDimensions=[0]
        )
    )
    stateChangeInProcess: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pack_ml;i=210", browseName="ns=pack_ml;StateChangeInProcess", dataType=o6.Boolean)
    )
    stateRequested: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pack_ml;i=209", browseName="ns=pack_ml;StateRequested", dataType=o6.Int32)
    )
    unitModeChangeInProcess: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pack_ml;i=201", browseName="ns=pack_ml;UnitModeChangeInProcess", dataType=o6.Boolean)
    )
    unitModeCurrent: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pack_ml;i=200", browseName="ns=pack_ml;UnitModeCurrent", dataType=ns0.datatypes.Enumeration)
    )
    unitModeRequested: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pack_ml;i=192", browseName="ns=pack_ml;UnitModeRequested", dataType=o6.Boolean)
    )
    unitSupportedModes: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pack_ml;i=193", browseName="ns=pack_ml;UnitSupportedModes", dataType=o6.NodeId)
    )


@o6.objecttype(nodeId="ns=pack_ml;i=5", browseName="ns=pack_ml;PackMLAdminObjectType", displayName="PackMLAdminObjectType")
class PackMLAdminObjectType(ns0.objtypes.BaseObjectType):
    accTimeSinceReset: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pack_ml;i=252", browseName="ns=pack_ml;AccTimeSinceReset", dataType=o6.Int32)
    )
    alarm: ns0.vartypes.BaseDataVariableType | None = o6.reference(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pack_ml;i=238", browseName="ns=pack_ml;Alarm", dataType=pack_ml_datypes.PackMLAlarmDataType, valueRank=1, arrayDimensions=[0]),
        "ns=pack_ml;i=22",
    )
    alarmExtent: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pack_ml;i=239", browseName="ns=pack_ml;AlarmExtent", dataType=o6.Int32)
    )
    alarmHistory: ns0.vartypes.BaseDataVariableType | None = o6.reference(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=pack_ml;i=240", browseName="ns=pack_ml;AlarmHistory", dataType=pack_ml_datypes.PackMLAlarmDataType, valueRank=1, arrayDimensions=[0]
        ),
        "ns=pack_ml;i=23",
    )
    alarmHistoryExtent: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pack_ml;i=241", browseName="ns=pack_ml;AlarmHistoryExtent", dataType=o6.Int32)
    )
    machDesignSpeed: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pack_ml;i=253", browseName="ns=pack_ml;MachDesignSpeed", dataType=o6.Float)
    )
    modeCumulativeTime: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pack_ml;i=247", browseName="ns=pack_ml;ModeCumulativeTime", dataType=o6.Int32, valueRank=1, arrayDimensions=[0])
    )
    modeCurrentTime: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pack_ml;i=246", browseName="ns=pack_ml;ModeCurrentTime", dataType=o6.Int32, valueRank=1, arrayDimensions=[0])
    )
    parameter: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=pack_ml;i=276", browseName="ns=pack_ml;Parameter", dataType=pack_ml_datypes.PackMLDescriptorDataType, valueRank=1, arrayDimensions=[0]
        )
    )
    prodConsumedCount: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=pack_ml;i=124", browseName="ns=pack_ml;ProdConsumedCount", dataType=pack_ml_datypes.PackMLCountDataType, valueRank=1, arrayDimensions=[0]
        )
    )
    prodDefectiveCount: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=pack_ml;i=119", browseName="ns=pack_ml;ProdDefectiveCount", dataType=pack_ml_datypes.PackMLCountDataType, valueRank=1, arrayDimensions=[0]
        )
    )
    prodProcessedCount: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=pack_ml;i=120", browseName="ns=pack_ml;ProdProcessedCount", dataType=pack_ml_datypes.PackMLCountDataType, valueRank=1, arrayDimensions=[0]
        )
    )
    stateCumulativeTime: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pack_ml;i=249", browseName="ns=pack_ml;StateCumulativeTime", dataType=o6.Int32, valueRank=2, arrayDimensions=[0, 0])
    )
    stateCurrentTime: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pack_ml;i=248", browseName="ns=pack_ml;StateCurrentTime", dataType=o6.Int32, valueRank=2, arrayDimensions=[0, 0])
    )
    stopReason: ns0.vartypes.BaseDataVariableType | None = o6.reference(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pack_ml;i=244", browseName="ns=pack_ml;StopReason", dataType=pack_ml_datypes.PackMLAlarmDataType), "ns=pack_ml;i=25"
    )
    stopReasonExtent: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pack_ml;i=245", browseName="ns=pack_ml;StopReasonExtent", dataType=o6.Int32)
    )
    warning: ns0.vartypes.BaseDataVariableType | None = o6.reference(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=pack_ml;i=242", browseName="ns=pack_ml;Warning", dataType=pack_ml_datypes.PackMLAlarmDataType, valueRank=1, arrayDimensions=[0]
        ),
        "ns=pack_ml;i=24",
    )
    warningExtent: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pack_ml;i=243", browseName="ns=pack_ml;WarningExtent", dataType=o6.Int32)
    )


o6.call(nodeId="ns=pack_ml;i=361", browseName="ns=pack_ml;Reset")

ns0.vartypes.PropertyType(
    nodeId="ns=pack_ml;i=118",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=pack_ml;i=362",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="RequestedMode",
            dataType=o6.Int32,
            valueRank=-1,
            description=o6.LocalizedText("The requested mode from the list of available modes in the enumeration from ModeSelection "),
        )
    ],
)
o6.call(nodeId="ns=pack_ml;i=362", browseName="ns=pack_ml;SetUnitMode", inputArgs=o6.hasProperty(o6.ns["ns=pack_ml;i=118"]))

o6.call(nodeId="ns=pack_ml;i=363", browseName="ns=pack_ml;Clear")

o6.call(nodeId="ns=pack_ml;i=364", browseName="ns=pack_ml;Abort")


@o6.objecttype(nodeId="ns=pack_ml;i=3", browseName="ns=pack_ml;PackMLBaseStateMachineType", displayName="PackMLBaseStateMachineType")
class PackMLBaseStateMachineType(ns0.objtypes.FiniteStateMachineType):
    abort: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=pack_ml;i=364"])
    aborted: ns0.objtypes.StateType
    abortedToCleared: ns0.objtypes.TransitionType
    aborting: ns0.objtypes.StateType
    abortingToAborted: ns0.objtypes.TransitionType
    availableStates: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pack_ml;i=167", browseName="AvailableStates", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])
    )
    availableTransitions: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pack_ml;i=158", browseName="AvailableTransitions", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])
    )
    clear: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=pack_ml;i=363"])
    cleared: ns0.objtypes.StateType | None
    clearedToAborting: ns0.objtypes.TransitionType
    machineState: PackMLMachineStateMachineType


o6.call(nodeId="ns=pack_ml;i=365", browseName="ns=pack_ml;ToComplete")

o6.call(nodeId="ns=pack_ml;i=366", browseName="ns=pack_ml;Hold")

o6.call(nodeId="ns=pack_ml;i=367", browseName="ns=pack_ml;Suspend")

o6.call(nodeId="ns=pack_ml;i=368", browseName="ns=pack_ml;Unhold")

ns0.vartypes.PropertyType(
    nodeId="ns=pack_ml;i=342",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=pack_ml;i=369",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="Parameter",
            dataType=o6.NodeId("ns=pack_ml;i=16"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText("The array of parameter that can be used by the method"),
        )
    ],
)
o6.call(nodeId="ns=pack_ml;i=369", browseName="ns=pack_ml;Start", inputArgs=o6.hasProperty(o6.ns["ns=pack_ml;i=342"]))

o6.call(nodeId="ns=pack_ml;i=372", browseName="ns=pack_ml;Unsuspend")


@o6.objecttype(nodeId="ns=pack_ml;i=1", browseName="ns=pack_ml;PackMLExecuteStateMachineType", displayName="PackMLExecuteStateMachineType")
class PackMLExecuteStateMachineType(ns0.objtypes.FiniteStateMachineType):
    availableStates: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pack_ml;i=125", browseName="AvailableStates", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])
    )
    availableTransitions: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pack_ml;i=126", browseName="AvailableTransitions", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])
    )
    complete: ns0.objtypes.StateType
    completeToResetting: ns0.objtypes.TransitionType
    completing: ns0.objtypes.StateType
    completingToComplete: ns0.objtypes.TransitionType
    execute: ns0.objtypes.StateType
    executeToCompleting: ns0.objtypes.TransitionType
    executeToHolding: ns0.objtypes.TransitionType
    executeToSuspending: ns0.objtypes.TransitionType
    held: ns0.objtypes.StateType
    heldToUnholding: ns0.objtypes.TransitionType
    hold: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=pack_ml;i=366"])
    holding: ns0.objtypes.StateType
    holdingToHeld: ns0.objtypes.TransitionType
    idle: ns0.objtypes.StateType
    idleToStarting: ns0.objtypes.TransitionType
    reset: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=pack_ml;i=361"])
    resetting: ns0.objtypes.StateType
    resettingToIdle: ns0.objtypes.TransitionType
    start: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=pack_ml;i=369"])
    starting: ns0.objtypes.StateType
    startingToExecute: ns0.objtypes.TransitionType
    startingToHolding: ns0.objtypes.TransitionType
    suspend: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=pack_ml;i=367"])
    suspended: ns0.objtypes.StateType
    suspendedToHolding: ns0.objtypes.TransitionType
    suspendedToUnsuspending: ns0.objtypes.TransitionType
    suspending: ns0.objtypes.StateType
    suspendingToHolding: ns0.objtypes.TransitionType
    suspendingToSuspended: ns0.objtypes.TransitionType
    toComplete: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=pack_ml;i=365"])
    unhold: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=pack_ml;i=368"])
    unholding: ns0.objtypes.StateType
    unholdingToExecute: ns0.objtypes.TransitionType
    unholdingToHolding: ns0.objtypes.TransitionType
    unsuspend: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=pack_ml;i=372"])
    unsuspending: ns0.objtypes.StateType
    unsuspendingToExecute: ns0.objtypes.TransitionType
    unsuspendingToHolding: ns0.objtypes.TransitionType


o6.call(nodeId="ns=pack_ml;i=375", browseName="ns=pack_ml;Stop")

o6.call(nodeId="ns=pack_ml;i=376", browseName="ns=pack_ml;Reset")


@o6.objecttype(nodeId="ns=pack_ml;i=2", browseName="ns=pack_ml;PackMLMachineStateMachineType", displayName="PackMLMachineStateMachineType")
class PackMLMachineStateMachineType(ns0.objtypes.FiniteStateMachineType):
    availableStates: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pack_ml;i=153", browseName="AvailableStates", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])
    )
    availableTransitions: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pack_ml;i=154", browseName="AvailableTransitions", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])
    )
    clearing: ns0.objtypes.StateType
    clearingToStopped: ns0.objtypes.TransitionType
    executeState: PackMLExecuteStateMachineType
    reset: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=pack_ml;i=376"])
    running: ns0.objtypes.StateType
    runningToStopping: ns0.objtypes.TransitionType
    stop: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=pack_ml;i=375"])
    stopped: ns0.objtypes.StateType
    stoppedToRunning: ns0.objtypes.TransitionType
    stopping: ns0.objtypes.StateType
    stoppingToStopped: ns0.objtypes.TransitionType


ns0.vartypes.PropertyType(
    nodeId="ns=pack_ml;i=348",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=pack_ml;i=400",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="RequestedMachineSpeed", dataType=o6.Float, valueRank=-1, description=o6.LocalizedText("The target machine speed"))],
)
o6.call(nodeId="ns=pack_ml;i=400", browseName="ns=pack_ml;SetMachSpeed", inputArgs=o6.hasProperty(o6.ns["ns=pack_ml;i=348"]))

ns0.vartypes.PropertyType(
    nodeId="ns=pack_ml;i=349",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=pack_ml;i=401",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="Product",
            dataType=o6.NodeId("ns=pack_ml;i=18"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText("This structure is an array of product definition, which includes the ProductId, ProcessVariables array and Ingredient array."),
        )
    ],
)
o6.call(nodeId="ns=pack_ml;i=401", browseName="ns=pack_ml;SetProduct", inputArgs=o6.hasProperty(o6.ns["ns=pack_ml;i=349"]))

ns0.vartypes.PropertyType(
    nodeId="ns=pack_ml;i=352",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=pack_ml;i=402",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="Parameter",
            dataType=o6.NodeId("ns=pack_ml;i=16"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText("The array of parameter that can be used by the method"),
        )
    ],
)
o6.call(nodeId="ns=pack_ml;i=402", browseName="ns=pack_ml;SetParameter", inputArgs=o6.hasProperty(o6.ns["ns=pack_ml;i=352"]))

ns0.vartypes.PropertyType(
    nodeId="ns=pack_ml;i=350",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=pack_ml;i=403",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="RemoteInterface",
            dataType=o6.NodeId("ns=pack_ml;i=19"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText("This structure is an array of remote interface information which include Number, ControlCmdNumber, CmdValue and Parameter."),
        )
    ],
)
o6.call(nodeId="ns=pack_ml;i=403", browseName="ns=pack_ml;RemoteCommand", inputArgs=o6.hasProperty(o6.ns["ns=pack_ml;i=350"]))

ns0.vartypes.PropertyType(
    nodeId="ns=pack_ml;i=351",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=pack_ml;i=404",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="InterlockId", dataType=o6.Int32, valueRank=-1, description=o6.LocalizedText("The NodeId of the interlock to set or reset.")),
        ns0.datatypes.Argument(
            name="State",
            dataType=o6.Boolean,
            valueRank=-1,
            description=o6.LocalizedText("The state that the targeted interlock should be set to.  True is set to interlocked, false is not interlocked."),
        ),
    ],
)
o6.call(nodeId="ns=pack_ml;i=404", browseName="ns=pack_ml;SetInterlock", inputArgs=o6.hasProperty(o6.ns["ns=pack_ml;i=351"]))


@o6.objecttype(nodeId="ns=pack_ml;i=6", browseName="ns=pack_ml;PackMLBaseObjectType", displayName="PackMLBaseObjectType")
class PackMLBaseObjectType(ns0.objtypes.BaseObjectType):
    admin: PackMLAdminObjectType = o6.hasComponent(PackMLAdminObjectType(nodeId="ns=pack_ml;i=73", browseName="ns=pack_ml;Admin"))
    baseStateMachine: PackMLBaseStateMachineType
    packMLVersion: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pack_ml;i=221", browseName="ns=pack_ml;PackMLVersion", dataType=o6.String, value="TR88.00.02-2015")
    )
    remoteCommand: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=pack_ml;i=403"])
    setInterlock: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=pack_ml;i=404"])
    setMachSpeed: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=pack_ml;i=400"])
    setParameter: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=pack_ml;i=402"])
    setProduct: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=pack_ml;i=401"])
    setUnitMode: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=pack_ml;i=362"])
    status: PackMLStatusObjectType
    tagID: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pack_ml;i=218", browseName="ns=pack_ml;TagID", dataType=o6.String))


del Any, TYPE_CHECKING, uuid, o6, ns0, pack_ml_reftypes, pack_ml_datypes
