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

"""Generated OPC UA adi namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
from . import reftypes as adi_reftypes
from . import datatypes as adi_datypes
from . import vartypes as adi_vartypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(nodeId="ns=adi;i=1002", browseName="ns=adi;AnalyserDeviceStateMachineType", displayName="AnalyserDeviceStateMachineType")
class AnalyserDeviceStateMachineType(ns0.objtypes.FiniteStateMachineType):
    local: ns0.objtypes.StateType
    localToMaintenanceTransition: ns0.objtypes.TransitionType
    localToOperatingTransition: ns0.objtypes.TransitionType
    localToShutdownTransition: ns0.objtypes.TransitionType
    maintenance: ns0.objtypes.StateType
    maintenanceToLocalTransition: ns0.objtypes.TransitionType
    maintenanceToOperatingTransition: ns0.objtypes.TransitionType
    maintenanceToShutdownTransition: ns0.objtypes.TransitionType
    operating: ns0.objtypes.StateType
    operatingToLocalTransition: ns0.objtypes.TransitionType
    operatingToMaintenanceTransition: ns0.objtypes.TransitionType
    operatingToShutdownTransition: ns0.objtypes.TransitionType
    powerup: ns0.objtypes.InitialStateType
    powerupToOperatingTransition: ns0.objtypes.TransitionType
    shutdown: ns0.objtypes.StateType


@o6.objecttype(nodeId="ns=adi;i=1004", browseName="ns=adi;AnalyserChannelOperatingStateType", displayName="AnalyserChannelOperatingStateType")
class AnalyserChannelOperatingStateType(ns0.objtypes.StateType):
    pass


@o6.objecttype(nodeId="ns=adi;i=1005", browseName="ns=adi;AnalyserChannelLocalStateType", displayName="AnalyserChannelLocalStateType")
class AnalyserChannelLocalStateType(ns0.objtypes.StateType):
    pass


@o6.objecttype(nodeId="ns=adi;i=1006", browseName="ns=adi;AnalyserChannelMaintenanceStateType", displayName="AnalyserChannelMaintenanceStateType")
class AnalyserChannelMaintenanceStateType(ns0.objtypes.StateType):
    pass


@o6.objecttype(
    nodeId="ns=adi;i=1007",
    browseName="ns=adi;AnalyserChannelStateMachineType",
    displayName="AnalyserChannelStateMachineType",
    description="Contains a nested state model that defines the top level states Operating, Local and Maintenance",
)
class AnalyserChannelStateMachineType(ns0.objtypes.FiniteStateMachineType):
    local: AnalyserChannelLocalStateType
    localSubStateMachine: ns0.objtypes.FiniteStateMachineType | None
    localToMaintenanceTransition: ns0.objtypes.TransitionType
    localToOperatingTransition: ns0.objtypes.TransitionType
    localToSlaveModeTransition: ns0.objtypes.TransitionType
    maintenance: AnalyserChannelMaintenanceStateType
    maintenanceSubStateMachine: ns0.objtypes.FiniteStateMachineType | None
    maintenanceToLocalTransition: ns0.objtypes.TransitionType
    maintenanceToOperatingTransition: ns0.objtypes.TransitionType
    maintenanceToSlaveModeTransition: ns0.objtypes.TransitionType
    operating: AnalyserChannelOperatingStateType
    operatingSubStateMachine: AnalyserChannel_OperatingModeSubStateMachineType
    operatingToLocalTransition: ns0.objtypes.TransitionType
    operatingToMaintenanceTransition: ns0.objtypes.TransitionType
    operatingToSlaveModeTransition: ns0.objtypes.TransitionType
    slaveMode: ns0.objtypes.InitialStateType
    slaveModeToOperatingTransition: ns0.objtypes.TransitionType


@o6.objecttype(
    nodeId="ns=adi;i=1008",
    browseName="ns=adi;AnalyserChannel_OperatingModeSubStateMachineType",
    displayName="AnalyserChannel_OperatingModeSubStateMachineType",
    description="AnalyserChannel OperatingMode SubStateMachine",
)
class AnalyserChannel_OperatingModeSubStateMachineType(ns0.objtypes.FiniteStateMachineType):
    aborted: ns0.objtypes.StateType
    abortedToClearingTransition: ns0.objtypes.TransitionType
    aborting: ns0.objtypes.StateType
    abortingToAbortedTransition: ns0.objtypes.TransitionType
    clearing: ns0.objtypes.StateType
    clearingToStoppedTransition: ns0.objtypes.TransitionType
    complete: ns0.objtypes.StateType
    completeToAbortingTransition: ns0.objtypes.TransitionType
    completeToStoppedTransition: ns0.objtypes.TransitionType
    completeToStoppingTransition: ns0.objtypes.TransitionType
    completing: ns0.objtypes.StateType
    completingToAbortingTransition: ns0.objtypes.TransitionType
    completingToCompleteTransition: ns0.objtypes.TransitionType
    completingToStoppingTransition: ns0.objtypes.TransitionType
    completingTransition: ns0.objtypes.TransitionType
    execute: AnalyserChannelOperatingExecuteStateType
    executeToAbortingTransition: ns0.objtypes.TransitionType
    executeToCompletingTransition: ns0.objtypes.TransitionType
    executeToHoldingTransition: ns0.objtypes.TransitionType
    executeToStoppingTransition: ns0.objtypes.TransitionType
    executeToSuspendingTransition: ns0.objtypes.TransitionType
    held: ns0.objtypes.StateType
    heldToAbortingTransition: ns0.objtypes.TransitionType
    heldToStoppingTransition: ns0.objtypes.TransitionType
    heldToUnholdingTransition: ns0.objtypes.TransitionType
    holding: ns0.objtypes.StateType
    holdingToAbortingTransition: ns0.objtypes.TransitionType
    holdingToHeldTransition: ns0.objtypes.TransitionType
    holdingToStoppingTransition: ns0.objtypes.TransitionType
    holdingTransition: ns0.objtypes.TransitionType
    idle: ns0.objtypes.StateType
    idleToAbortingTransition: ns0.objtypes.TransitionType
    idleToStartingTransition: ns0.objtypes.TransitionType
    idleToStoppingTransition: ns0.objtypes.TransitionType
    operatingExecuteSubStateMachine: AnalyserChannel_OperatingModeExecuteSubStateMachineType
    resetting: ns0.objtypes.StateType
    resettingToAbortingTransition: ns0.objtypes.TransitionType
    resettingToIdleTransition: ns0.objtypes.TransitionType
    resettingToStoppingTransition: ns0.objtypes.TransitionType
    resettingTransition: ns0.objtypes.TransitionType
    starting: ns0.objtypes.StateType
    startingToAbortingTransition: ns0.objtypes.TransitionType
    startingToExecuteTransition: ns0.objtypes.TransitionType
    startingToStoppingTransition: ns0.objtypes.TransitionType
    startingTransition: ns0.objtypes.TransitionType
    stopped: ns0.objtypes.InitialStateType
    stoppedToAbortingTransition: ns0.objtypes.TransitionType
    stoppedToResettingTransition: ns0.objtypes.TransitionType
    stopping: ns0.objtypes.StateType
    stoppingToAbortingTransition: ns0.objtypes.TransitionType
    stoppingToStoppedTransition: ns0.objtypes.TransitionType
    suspended: ns0.objtypes.StateType
    suspendedToAbortingTransition: ns0.objtypes.TransitionType
    suspendedToStoppingTransition: ns0.objtypes.TransitionType
    suspendedToUnsuspendingTransition: ns0.objtypes.TransitionType
    suspending: ns0.objtypes.StateType
    suspendingToAbortingTransition: ns0.objtypes.TransitionType
    suspendingToStoppingTransition: ns0.objtypes.TransitionType
    suspendingToSuspendedTransition: ns0.objtypes.TransitionType
    suspendingTransition: ns0.objtypes.TransitionType
    unholding: ns0.objtypes.StateType
    unholdingToAbortingTransition: ns0.objtypes.TransitionType
    unholdingToExecuteTransition: ns0.objtypes.TransitionType
    unholdingToHoldingTransition: ns0.objtypes.TransitionType
    unholdingToStoppingTransition: ns0.objtypes.TransitionType
    unholdingTransition: ns0.objtypes.TransitionType
    unsuspending: ns0.objtypes.StateType
    unsuspendingToAbortingTransition: ns0.objtypes.TransitionType
    unsuspendingToExecuteTransition: ns0.objtypes.TransitionType
    unsuspendingToStoppingTransition: ns0.objtypes.TransitionType
    unsuspendingToSuspendingTransition: ns0.objtypes.TransitionType
    unsuspendingTransition: ns0.objtypes.TransitionType


@o6.objecttype(
    nodeId="ns=adi;i=1009", browseName="ns=adi;AnalyserChannel_OperatingModeExecuteSubStateMachineType", displayName="AnalyserChannel_OperatingModeExecuteSubStateMachineType"
)
class AnalyserChannel_OperatingModeExecuteSubStateMachineType(ns0.objtypes.FiniteStateMachineType):
    analyseCalibrationSample: ns0.objtypes.StateType
    analyseCalibrationSampleToPublishResultsTransition: ns0.objtypes.TransitionType
    analyseCalibrationSampleTransition: ns0.objtypes.TransitionType
    analyseSample: ns0.objtypes.StateType
    analyseSampleToPublishResultsTransition: ns0.objtypes.TransitionType
    analyseSampleTransition: ns0.objtypes.TransitionType
    analyseValidationSample: ns0.objtypes.StateType
    analyseValidationSampleToPublishResultsTransition: ns0.objtypes.TransitionType
    analyseValidationSampleTransition: ns0.objtypes.TransitionType
    cleaning: ns0.objtypes.StateType
    cleaningToPublishResultsTransition: ns0.objtypes.TransitionType
    cleaningTransition: ns0.objtypes.TransitionType
    cleanupSamplingSystem: ns0.objtypes.StateType
    cleanupSamplingSystemToSelectExecutionCycleTransition: ns0.objtypes.TransitionType
    cleanupSamplingSystemTransition: ns0.objtypes.TransitionType
    diagnostic: ns0.objtypes.StateType
    diagnosticToPublishResultsTransition: ns0.objtypes.TransitionType
    diagnosticTransition: ns0.objtypes.TransitionType
    ejectGrabSample: ns0.objtypes.StateType
    ejectGrabSampleToCleanupSamplingSystemTransition: ns0.objtypes.TransitionType
    ejectGrabSampleTransition: ns0.objtypes.TransitionType
    extractCalibrationSample: ns0.objtypes.StateType
    extractCalibrationSampleToPrepareCalibrationSampleTransition: ns0.objtypes.TransitionType
    extractCalibrationSampleTransition: ns0.objtypes.TransitionType
    extractSample: ns0.objtypes.StateType
    extractSampleToPrepareSampleTransition: ns0.objtypes.TransitionType
    extractSampleTransition: ns0.objtypes.TransitionType
    extractValidationSample: ns0.objtypes.StateType
    extractValidationSampleToPrepareValidationSampleTransition: ns0.objtypes.TransitionType
    extractValidationSampleTransition: ns0.objtypes.TransitionType
    prepareCalibrationSample: ns0.objtypes.StateType
    prepareCalibrationSampleToAnalyseCalibrationSampleTransition: ns0.objtypes.TransitionType
    prepareCalibrationSampleTransition: ns0.objtypes.TransitionType
    prepareSample: ns0.objtypes.StateType
    prepareSampleToAnalyseSampleTransition: ns0.objtypes.TransitionType
    prepareSampleTransition: ns0.objtypes.TransitionType
    prepareValidationSample: ns0.objtypes.StateType
    prepareValidationSampleToAnalyseValidationSampleTransition: ns0.objtypes.TransitionType
    prepareValidationSampleTransition: ns0.objtypes.TransitionType
    publishResults: ns0.objtypes.StateType
    publishResultsToCleanupSamplingSystemTransition: ns0.objtypes.TransitionType
    publishResultsToEjectGrabSampleTransition: ns0.objtypes.TransitionType
    selectExecutionCycle: ns0.objtypes.InitialStateType
    selectExecutionCycleToWaitForCalibrationTriggerTransition: ns0.objtypes.TransitionType
    selectExecutionCycleToWaitForCleaningTriggerTransition: ns0.objtypes.TransitionType
    selectExecutionCycleToWaitForDiagnosticTriggerTransition: ns0.objtypes.TransitionType
    selectExecutionCycleToWaitForSampleTriggerTransition: ns0.objtypes.TransitionType
    selectExecutionCycleToWaitForValidationTriggerTransition: ns0.objtypes.TransitionType
    waitForCalibrationTrigger: ns0.objtypes.StateType
    waitForCalibrationTriggerToExtractCalibrationSampleTransition: ns0.objtypes.TransitionType
    waitForCleaningTrigger: ns0.objtypes.StateType
    waitForCleaningTriggerToCleaningTransition: ns0.objtypes.TransitionType
    waitForDiagnosticTrigger: ns0.objtypes.StateType
    waitForDiagnosticTriggerToDiagnosticTransition: ns0.objtypes.TransitionType
    waitForSampleTrigger: ns0.objtypes.StateType
    waitForSampleTriggerToExtractSampleTransition: ns0.objtypes.TransitionType
    waitForValidationTrigger: ns0.objtypes.StateType
    waitForValidationTriggerToExtractValidationSampleTransition: ns0.objtypes.TransitionType


@o6.objecttype(
    nodeId="ns=adi;i=1018",
    browseName="ns=adi;AccessorySlotStateMachineType",
    displayName="AccessorySlotStateMachineType",
    description="Describes the behaviour of an AccessorySlot when a physical accessory is inserted or removed.",
)
class AccessorySlotStateMachineType(ns0.objtypes.FiniteStateMachineType):
    empty: ns0.objtypes.StateType
    emptyToInsertingTransition: ns0.objtypes.TransitionType
    emptyToShutdownTransition: ns0.objtypes.TransitionType
    inserting: ns0.objtypes.StateType
    insertingToInstalledTransition: ns0.objtypes.TransitionType
    insertingToRemovingTransition: ns0.objtypes.TransitionType
    insertingToShutdownTransition: ns0.objtypes.TransitionType
    insertingTransition: ns0.objtypes.TransitionType
    installed: ns0.objtypes.StateType
    installedToRemovingTransition: ns0.objtypes.TransitionType
    installedToShutdownTransition: ns0.objtypes.TransitionType
    powerup: ns0.objtypes.InitialStateType
    powerupToEmptyTransition: ns0.objtypes.TransitionType
    removing: ns0.objtypes.StateType
    removingToEmptyTransition: ns0.objtypes.TransitionType
    removingToShutdownTransition: ns0.objtypes.TransitionType
    removingTransition: ns0.objtypes.TransitionType
    shutdown: ns0.objtypes.StateType


ns0.objtypes.BaseObjectType(nodeId="ns=adi;i=5001", browseName="ns=di;ParameterSet", description="Flat list of Parameters")


@o6.objecttype(nodeId="ns=adi;i=8964", browseName="ns=adi;AnalyserChannelOperatingExecuteStateType", displayName="AnalyserChannelOperatingExecuteStateType")
class AnalyserChannelOperatingExecuteStateType(ns0.objtypes.StateType):
    pass


di.objtypes.FunctionalGroupType(nodeId="ns=adi;i=9386", browseName="ns=di;Identification", description="Used to organize parameters for identification of this TopologyElement")
o6.reference(o6.ns["ns=adi;i=9386"], "i=35", "ns=di;i=6001")
o6.reference(o6.ns["ns=adi;i=9386"], "i=35", "ns=di;i=6003")
o6.reference(o6.ns["ns=adi;i=9386"], "i=35", "ns=di;i=6004")


@o6.objecttype(nodeId="ns=adi;i=1001", browseName="ns=adi;AnalyserDeviceType", displayName="AnalyserDeviceType", isAbstract=True)
class AnalyserDeviceType(di.objtypes.DeviceType):
    analyserStateMachine: AnalyserDeviceStateMachineType
    configuration: di.objtypes.FunctionalGroupType
    factorySettings: di.objtypes.FunctionalGroupType = o6.hasComponent(di.objtypes.FunctionalGroupType(nodeId="ns=adi;i=9486", browseName="ns=adi;FactorySettings"))
    identification: di.objtypes.FunctionalGroupType = o6.hasComponent(o6.ns["ns=adi;i=9386"])
    langleAccessorySlotIdentifierRangle: AccessorySlotType | None
    langleChannelIdentifierRangle: AnalyserChannelType | None
    methodSet: ns0.objtypes.BaseObjectType
    parameterSet: ns0.objtypes.BaseObjectType | None = o6.hasComponent(o6.ns["ns=adi;i=5001"])
    status: di.objtypes.FunctionalGroupType


@o6.objecttype(nodeId="ns=adi;i=1012", browseName="ns=adi;ParticleSizeMonitorDeviceType", displayName="ParticleSizeMonitorDeviceType")
class ParticleSizeMonitorDeviceType(AnalyserDeviceType):
    pass


@o6.objecttype(nodeId="ns=adi;i=1013", browseName="ns=adi;ChromatographDeviceType", displayName="ChromatographDeviceType")
class ChromatographDeviceType(AnalyserDeviceType):
    pass


@o6.objecttype(nodeId="ns=adi;i=1014", browseName="ns=adi;MassSpectrometerDeviceType", displayName="MassSpectrometerDeviceType")
class MassSpectrometerDeviceType(AnalyserDeviceType):
    pass


@o6.objecttype(nodeId="ns=adi;i=1015", browseName="ns=adi;AcousticSpectrometerDeviceType", displayName="AcousticSpectrometerDeviceType")
class AcousticSpectrometerDeviceType(AnalyserDeviceType):
    pass


@o6.objecttype(nodeId="ns=adi;i=1016", browseName="ns=adi;NMRDeviceType", displayName="NMRDeviceType")
class NMRDeviceType(AnalyserDeviceType):
    pass


@o6.objecttype(nodeId="ns=adi;i=1003", browseName="ns=adi;AnalyserChannelType", displayName="AnalyserChannelType")
class AnalyserChannelType(di.objtypes.TopologyElementType):
    channelStateMachine: AnalyserChannelStateMachineType
    configuration: di.objtypes.FunctionalGroupType
    langleAccessorySlotIdentifierRangle: AccessorySlotType | None
    langleGroupIdentifierRangle: di.objtypes.FunctionalGroupType | None = o6.hasComponent(
        di.objtypes.FunctionalGroupType(nodeId="ns=adi;i=9788", browseName="ns=adi;<GroupIdentifier>", description="Group definition", modellingRule="OptionalPlaceholder")
    )
    langleStreamIdentifierRangle: StreamType | None
    methodSet: ns0.objtypes.BaseObjectType
    parameterSet: ns0.objtypes.BaseObjectType | None
    status: di.objtypes.FunctionalGroupType


ns0.objtypes.BaseObjectType(nodeId="ns=adi;i=10317", browseName="ns=di;ParameterSet", description="Flat list of Parameters")


@o6.objecttype(nodeId="ns=adi;i=1010", browseName="ns=adi;StreamType", displayName="StreamType")
class StreamType(di.objtypes.TopologyElementType):
    acquisitionData: di.objtypes.FunctionalGroupType
    acquisitionSettings: di.objtypes.FunctionalGroupType
    acquisitionStatus: di.objtypes.FunctionalGroupType
    chemometricModelSettings: di.objtypes.FunctionalGroupType = o6.hasComponent(
        di.objtypes.FunctionalGroupType(nodeId="ns=adi;i=10440", browseName="ns=adi;ChemometricModelSettings")
    )
    configuration: di.objtypes.FunctionalGroupType
    context: di.objtypes.FunctionalGroupType
    langleGroupIdentifierRangle: di.objtypes.FunctionalGroupType | None = o6.hasComponent(
        di.objtypes.FunctionalGroupType(nodeId="ns=adi;i=10444", browseName="ns=adi;<GroupIdentifier>", description="Group definition", modellingRule="OptionalPlaceholder")
    )
    parameterSet: ns0.objtypes.BaseObjectType | None = o6.hasComponent(o6.ns["ns=adi;i=10317"])
    status: di.objtypes.FunctionalGroupType


@o6.objecttype(nodeId="ns=adi;i=1031", browseName="ns=adi;MassSpectrometerDeviceStreamType", displayName="MassSpectrometerDeviceStreamType")
class MassSpectrometerDeviceStreamType(StreamType):
    pass


@o6.objecttype(nodeId="ns=adi;i=1033", browseName="ns=adi;AcousticSpectrometerDeviceStreamType", displayName="AcousticSpectrometerDeviceStreamType")
class AcousticSpectrometerDeviceStreamType(StreamType):
    pass


@o6.objecttype(nodeId="ns=adi;i=1034", browseName="ns=adi;ChromatographDeviceStreamType", displayName="ChromatographDeviceStreamType")
class ChromatographDeviceStreamType(StreamType):
    pass


@o6.objecttype(nodeId="ns=adi;i=1035", browseName="ns=adi;MNRDeviceStreamType", displayName="MNRDeviceStreamType")
class MNRDeviceStreamType(StreamType):
    pass


ns0.objtypes.BaseObjectType(nodeId="ns=adi;i=10446", browseName="ns=di;ParameterSet", description="Flat list of Parameters")


@o6.objecttype(nodeId="ns=adi;i=1030", browseName="ns=adi;SpectrometerDeviceStreamType", displayName="SpectrometerDeviceStreamType")
class SpectrometerDeviceStreamType(StreamType):
    acquisitionData: di.objtypes.FunctionalGroupType
    acquisitionSettings: di.objtypes.FunctionalGroupType
    acquisitionStatus: di.objtypes.FunctionalGroupType
    configuration: di.objtypes.FunctionalGroupType
    factorySettings: ns0.objtypes.BaseObjectType = o6.hasComponent(ns0.objtypes.BaseObjectType(nodeId="ns=adi;i=10638", browseName="ns=adi;FactorySettings"))
    parameterSet: ns0.objtypes.BaseObjectType | None = o6.hasComponent(o6.ns["ns=adi;i=10446"])


ns0.objtypes.BaseObjectType(nodeId="ns=adi;i=10768", browseName="ns=di;ParameterSet", description="Flat list of Parameters")


@o6.objecttype(nodeId="ns=adi;i=1032", browseName="ns=adi;ParticleSizeMonitorDeviceStreamType", displayName="ParticleSizeMonitorDeviceStreamType")
class ParticleSizeMonitorDeviceStreamType(StreamType):
    acquisitionData: di.objtypes.FunctionalGroupType
    parameterSet: ns0.objtypes.BaseObjectType | None = o6.hasComponent(o6.ns["ns=adi;i=10768"])


@o6.objecttype(nodeId="ns=adi;i=1011", browseName="ns=adi;SpectrometerDeviceType", displayName="SpectrometerDeviceType")
class SpectrometerDeviceType(AnalyserDeviceType):
    factorySettings: di.objtypes.FunctionalGroupType = o6.hasComponent(di.objtypes.FunctionalGroupType(nodeId="ns=adi;i=11411", browseName="ns=adi;FactorySettings"))
    parameterSet: ns0.objtypes.BaseObjectType | None


@o6.objecttype(
    nodeId="ns=adi;i=1017",
    browseName="ns=adi;AccessorySlotType",
    displayName="AccessorySlotType",
    description='Organizes zero or more Accessory objects identified by "AccessoryIdentifier" which represent Accessories currently being used on that AccessorySlot.',
)
class AccessorySlotType(di.objtypes.ConfigurableObjectType):
    accessorySlotStateMachine: AccessorySlotStateMachineType
    isEnabled: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=adi;i=12787", browseName="ns=adi;IsEnabled", description="True if this accessory slot is capable of accepting an accessory in it", dataType=o6.Boolean
        )
    )
    isHotSwappable: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=adi;i=12786",
            browseName="ns=adi;IsHotSwappable",
            description="True if an accessory can be inserted in the accessory slot while it is powered",
            dataType=o6.Boolean,
        )
    )
    langleAccessoryIdentifierRangle: AccessoryType | None


@o6.objecttype(nodeId="ns=adi;i=1019", browseName="ns=adi;AccessoryType", displayName="AccessoryType")
class AccessoryType(di.objtypes.TopologyElementType):
    configuration: di.objtypes.FunctionalGroupType = o6.hasComponent(di.objtypes.FunctionalGroupType(nodeId="ns=adi;i=12898", browseName="ns=adi;Configuration"))
    factorySettings: di.objtypes.FunctionalGroupType = o6.hasComponent(di.objtypes.FunctionalGroupType(nodeId="ns=adi;i=12902", browseName="ns=adi;FactorySettings"))
    isHotSwappable: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=adi;i=12904",
            browseName="ns=adi;IsHotSwappable",
            description="True if this accessory can be inserted in the accessory slot while it is powered",
            dataType=o6.Boolean,
        )
    )
    isReady: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=adi;i=12905", browseName="ns=adi;IsReady", description="True if this accessory is ready for use", dataType=o6.Boolean)
    )
    status: di.objtypes.FunctionalGroupType = o6.hasComponent(di.objtypes.FunctionalGroupType(nodeId="ns=adi;i=12900", browseName="ns=adi;Status"))


@o6.objecttype(nodeId="ns=adi;i=1020", browseName="ns=adi;GcOvenType", displayName="GcOvenType")
class GcOvenType(AccessoryType):
    pass


@o6.objecttype(nodeId="ns=adi;i=9350", browseName="ns=adi;DetectorType", displayName="DetectorType")
class DetectorType(AccessoryType):
    pass


@o6.objecttype(nodeId="ns=adi;i=9359", browseName="ns=adi;SmartSamplingSystemType", displayName="SmartSamplingSystemType")
class SmartSamplingSystemType(AccessoryType):
    pass


@o6.objecttype(nodeId="ns=adi;i=9368", browseName="ns=adi;SourceType", displayName="SourceType")
class SourceType(AccessoryType):
    pass


del Any, TYPE_CHECKING, uuid, o6, di, ns0, adi_reftypes, adi_datypes, adi_vartypes
