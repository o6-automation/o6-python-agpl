# Copyright (c) 2026 o6 Automation GmbH
#
# SPDX-License-Identifier: AGPL-3.0-or-later
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

"""Generated OPC UA plastics_rubber namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.enumtype(nodeId="ns=plastics_rubber;i=3001", browseName="ns=plastics_rubber;ControlModeEnumeration", description="Indication how the parameter is currently controlled")
class ControlModeEnumeration(ns0.datatypes.Enumeration):
    OTHER = o6.enumfield(0, name="OTHER")
    OFF = o6.enumfield(1, name="OFF")
    AUTOMATIC = o6.enumfield(2, name="AUTOMATIC")
    TUNING = o6.enumfield(3, name="TUNING")
    STANDBY = o6.enumfield(4, name="STANDBY")
    OPEN_LOOP = o6.enumfield(5, name="OPEN_LOOP")
    ONLY_MEASUREMENT = o6.enumfield(6, name="ONLY_MEASUREMENT")


@o6.enumtype(
    nodeId="ns=plastics_rubber;i=3005",
    browseName="ns=plastics_rubber;StorageEnumeration",
    description="Indication which parts of the production dataset shall be activated in the machine control after writing",
)
class StorageEnumeration(ns0.datatypes.Enumeration):
    PRODUCTION = o6.enumfield(1, name="PRODUCTION")
    PREPARATION = o6.enumfield(2, name="PREPARATION")
    FILE_SYSTEM = o6.enumfield(4, name="FILE_SYSTEM")


@o6.datatype(
    nodeId="ns=plastics_rubber;i=3004",
    browseName="ns=plastics_rubber;ProductionDatasetWriteOptionsType",
    description="Used as GenerateOptions in the Method GenerateFileForWrite in ProductionDatasetTransfer",
    defaultEncodingId="ns=plastics_rubber;i=5005",
)
class ProductionDatasetWriteOptionsType(ns0.datatypes.Structure):
    storage: StorageEnumeration = o6.field(name="Storage")
    name: o6.String = o6.field(name="Name")
    components: list[o6.UInt16] = o6.field(name="Components", arrayDimensions=[0])


@o6.datatype(
    nodeId="ns=plastics_rubber;i=3006",
    browseName="ns=plastics_rubber;ProductionDatasetInformationType",
    description="Information on a production dataset",
    defaultEncodingId="ns=plastics_rubber;i=5004",
)
class ProductionDatasetInformationType(ns0.datatypes.Structure):
    name: o6.String = o6.field(name="Name")
    description: o6.String = o6.field(name="Description")
    mESId: o6.String = o6.field(name="MESId")
    creationTimestamp: o6.DateTime = o6.field(name="CreationTimestamp")
    lastModificationTimestamp: o6.DateTime = o6.field(name="LastModificationTimestamp")
    lastSaveTimestamp: o6.DateTime = o6.field(name="LastSaveTimestamp")
    userName: o6.String = o6.field(name="UserName")
    components: list[o6.UInt16] = o6.field(name="Components", arrayDimensions=[0])
    manufacturer: o6.String = o6.field(name="Manufacturer")
    serialNumber: o6.String = o6.field(name="SerialNumber")
    model: o6.String = o6.field(name="Model")
    controllerName: o6.String = o6.field(name="ControllerName")
    userMachineName: o6.String = o6.field(name="UserMachineName")
    locationName: o6.String = o6.field(name="LocationName")
    productName: list[o6.String] = o6.field(name="ProductName", arrayDimensions=[0])
    mouldId: o6.String = o6.field(name="MouldId")
    numCavities: o6.UInt32 = o6.field(name="NumCavities")


@o6.datatype(
    nodeId="ns=plastics_rubber;i=3007",
    browseName="ns=plastics_rubber;ProductionDatasetReadOptionsType",
    description="Used as GenerateOptions in the Method GenerateFileForRead in ProductionDatasetTransfer",
    defaultEncodingId="ns=plastics_rubber;i=5012",
)
class ProductionDatasetReadOptionsType(ns0.datatypes.Structure):
    storage: StorageEnumeration = o6.field(name="Storage")
    name: o6.String = o6.field(name="Name")


@o6.enumtype(nodeId="ns=plastics_rubber;i=3008", browseName="ns=plastics_rubber;MouldStatusEnumeration", description="Current (physical) status of the mould")
class MouldStatusEnumeration(ns0.datatypes.Enumeration):
    OTHER = o6.enumfield(0, name="OTHER")
    MOULD_NOT_INSTALLED = o6.enumfield(1, name="MOULD_NOT_INSTALLED")
    MOULD_CHANGE = o6.enumfield(2, name="MOULD_CHANGE")
    MOULD_INSTALLED = o6.enumfield(3, name="MOULD_INSTALLED")


@o6.enumtype(
    nodeId="ns=plastics_rubber;i=3009", browseName="ns=plastics_rubber;LogbookEventsEnumeration", description="Information which LogbookEvents are supported by the machine"
)
class LogbookEventsEnumeration(ns0.datatypes.Enumeration):
    PARAMETER_CHANGE = o6.enumfield(0, name="PARAMETER_CHANGE")
    USER = o6.enumfield(1, name="USER")
    REMOTE_ACCESS = o6.enumfield(2, name="REMOTE_ACCESS")
    SEQUENCE_CHANGE = o6.enumfield(3, name="SEQUENCE_CHANGE")
    MACHINE_MODE_CHANGE = o6.enumfield(4, name="MACHINE_MODE_CHANGE")
    PRODUCTION_STATUS_CHANGE = o6.enumfield(5, name="PRODUCTION_STATUS_CHANGE")
    PRODUCTION_DATASET_CHANGE = o6.enumfield(6, name="PRODUCTION_DATASET_CHANGE")
    PRODUCTION_DATASET_FROZEN = o6.enumfield(7, name="PRODUCTION_DATASET_FROZEN")
    STANDSTILL_REASON = o6.enumfield(8, name="STANDSTILL_REASON")
    MESSAGE = o6.enumfield(9, name="MESSAGE")
    USER_FEEDBACK = o6.enumfield(10, name="USER_FEEDBACK")


@o6.enumtype(nodeId="ns=plastics_rubber;i=3010", browseName="ns=plastics_rubber;UserChangeEnumeration", description="Information if a user logs in or off")
class UserChangeEnumeration(ns0.datatypes.Enumeration):
    LOG_ON = o6.enumfield(0, name="LOG_ON")
    LOG_OFF = o6.enumfield(1, name="LOG_OFF")


@o6.enumtype(
    nodeId="ns=plastics_rubber;i=3011", browseName="ns=plastics_rubber;MachineModeEnumeration", description="Current machine mode (as defined by mode selector on the machine)"
)
class MachineModeEnumeration(ns0.datatypes.Enumeration):
    OTHER = o6.enumfield(0, name="OTHER")
    AUTOMATIC = o6.enumfield(1, name="AUTOMATIC")
    SEMI_AUTOMATIC = o6.enumfield(2, name="SEMI_AUTOMATIC")
    MANUAL = o6.enumfield(3, name="MANUAL")
    SETUP = o6.enumfield(4, name="SETUP")
    SLEEP = o6.enumfield(5, name="SLEEP")


@o6.enumtype(nodeId="ns=plastics_rubber;i=3012", browseName="ns=plastics_rubber;SequenceChangeEnumeration", description="Classification of production sequence change")
class SequenceChangeEnumeration(ns0.datatypes.Enumeration):
    UPDATE = o6.enumfield(0, name="UPDATE")
    ADD = o6.enumfield(1, name="ADD")
    MODIFY = o6.enumfield(2, name="MODIFY")
    MOVE = o6.enumfield(3, name="MOVE")
    DELETE = o6.enumfield(4, name="DELETE")


@o6.enumtype(nodeId="ns=plastics_rubber;i=3013", browseName="ns=plastics_rubber;MaintenanceStatusEnumeration", description="Maintenance status of a machine/device/component")
class MaintenanceStatusEnumeration(ns0.datatypes.Enumeration):
    NOT_DUE = o6.enumfield(0, name="NOT_DUE")
    WARNING = o6.enumfield(1, name="WARNING")
    DUE = o6.enumfield(2, name="DUE")


@o6.datatype(
    nodeId="ns=plastics_rubber;i=3014",
    browseName="ns=plastics_rubber;PageEntryDataType",
    description="Information on a page that is implemented in the machine control system and shown on the screen of the machine",
    defaultEncodingId="ns=plastics_rubber;i=5024",
)
class PageEntryDataType(ns0.datatypes.Structure):
    id: o6.String = o6.field(name="Id")
    title: o6.LocalizedText = o6.field(name="Title")


@o6.datatype(
    nodeId="ns=plastics_rubber;i=3015",
    browseName="ns=plastics_rubber;StandstillReasonType",
    description="Description of a standstill reason",
    defaultEncodingId="ns=plastics_rubber;i=5026",
)
class StandstillReasonType(ns0.datatypes.Structure):
    id: o6.String = o6.field(name="Id")
    text: o6.LocalizedText = o6.field(name="Text")
    lockedByMES: o6.Boolean = o6.field(name="LockedByMES")


@o6.enumtype(nodeId="ns=plastics_rubber;i=3016", browseName="ns=plastics_rubber;ProductionStatusEnumeration", description="Production status of the machine")
class ProductionStatusEnumeration(ns0.datatypes.Enumeration):
    OTHER = o6.enumfield(0, name="OTHER")
    NO_PRODUCTION = o6.enumfield(1, name="NO_PRODUCTION")
    START_UP = o6.enumfield(2, name="START_UP")
    READY_FOR_PRODUCTION = o6.enumfield(3, name="READY_FOR_PRODUCTION")
    PRODUCTION = o6.enumfield(4, name="PRODUCTION")
    DRY_RUN = o6.enumfield(5, name="DRY_RUN")


@o6.enumtype(nodeId="ns=plastics_rubber;i=3017", browseName="ns=plastics_rubber;JobStatusEnumeration", description="Current status of the job")
class JobStatusEnumeration(ns0.datatypes.Enumeration):
    OTHER = o6.enumfield(0, name="OTHER")
    TRANSFERRED_ASSIGNED = o6.enumfield(1, name="TRANSFERRED_ASSIGNED")
    SET_UP_ACTIVE = o6.enumfield(2, name="SET_UP_ACTIVE")
    SET_UP_INTERRUPTED = o6.enumfield(3, name="SET_UP_INTERRUPTED")
    SET_UP_FINISHED = o6.enumfield(4, name="SET_UP_FINISHED")
    START_UP_ACTIVE = o6.enumfield(5, name="START_UP_ACTIVE")
    JOB_IN_PRODUCTION = o6.enumfield(6, name="JOB_IN_PRODUCTION")
    JOB_INTERRUPTED = o6.enumfield(7, name="JOB_INTERRUPTED")
    JOB_FINISHED = o6.enumfield(8, name="JOB_FINISHED")
    TEAR_DOWN_ACTIVE = o6.enumfield(9, name="TEAR_DOWN_ACTIVE")
    TEAR_DOWN_INTERRUPTED = o6.enumfield(10, name="TEAR_DOWN_INTERRUPTED")
    TEAR_DOWN_FINISHED = o6.enumfield(11, name="TEAR_DOWN_FINISHED")


@o6.enumtype(nodeId="ns=plastics_rubber;i=3018", browseName="ns=plastics_rubber;EventOriginatorEnumeration", description="Originator of an event")
class EventOriginatorEnumeration(ns0.datatypes.Enumeration):
    OTHER = o6.enumfield(0, name="OTHER")
    MACHINE = o6.enumfield(1, name="MACHINE")
    OPERATOR = o6.enumfield(2, name="OPERATOR")
    MES = o6.enumfield(3, name="MES")
    PERIPHERAL_DEVICE = o6.enumfield(4, name="PERIPHERAL_DEVICE")


@o6.enumtype(nodeId="ns=plastics_rubber;i=3019", browseName="ns=plastics_rubber;CycleQualityEnumeration", description="Quality of the whole cycle")
class CycleQualityEnumeration(ns0.datatypes.Enumeration):
    GOOD_CYCLE = o6.enumfield(0, name="GOOD_CYCLE")
    BAD_CYCLE = o6.enumfield(1, name="BAD_CYCLE")
    TEST_SAMPLE_CYCLE = o6.enumfield(2, name="TEST_SAMPLE_CYCLE")
    FAILED_CYCLE = o6.enumfield(3, name="FAILED_CYCLE")


@o6.enumtype(nodeId="ns=plastics_rubber;i=3020", browseName="ns=plastics_rubber;CavityCycleQualityEnumeration", description="Quality of the cycle for each cavity")
class CavityCycleQualityEnumeration(ns0.datatypes.Enumeration):
    NO_PART = o6.enumfield(0, name="NO_PART")
    GOOD_PART = o6.enumfield(1, name="GOOD_PART")
    BAD_PART = o6.enumfield(2, name="BAD_PART")
    REWORK = o6.enumfield(3, name="REWORK")


@o6.datatype(
    nodeId="ns=plastics_rubber;i=3021",
    browseName="ns=plastics_rubber;JobListElementType",
    description="Description of a job in a job list",
    defaultEncodingId="ns=plastics_rubber;i=5036",
)
class JobListElementType(ns0.datatypes.Structure):
    jobName: o6.String = o6.field(name="JobName")
    jobDescription: o6.String = o6.field(name="JobDescription")
    jobClassification: o6.String = o6.field(name="JobClassification")
    customerName: o6.String = o6.field(name="CustomerName")
    productionDatasetName: o6.String = o6.field(name="ProductionDatasetName")
    productionDatasetDescription: o6.String = o6.field(name="ProductionDatasetDescription")
    material: list[o6.String] = o6.field(name="Material", arrayDimensions=[0])
    productName: list[o6.String] = o6.field(name="ProductName", arrayDimensions=[0])
    productDescription: list[o6.String] = o6.field(name="ProductDescription", arrayDimensions=[0])
    jobPriority: o6.String = o6.field(name="JobPriority")
    plannedStart: o6.DateTime = o6.field(name="PlannedStart")
    plannedProductionTime: o6.Double = o6.field(name="PlannedProductionTime")
    latestEnd: o6.DateTime = o6.field(name="LatestEnd")


@o6.datatype(
    nodeId="ns=plastics_rubber;i=3022",
    browseName="ns=plastics_rubber;CyclicJobListElementType",
    description="Description of a job in a cyclic job list",
    defaultEncodingId="ns=plastics_rubber;i=5041",
)
class CyclicJobListElementType(JobListElementType):
    jobName: o6.String = o6.field(name="JobName")
    jobDescription: o6.String = o6.field(name="JobDescription")
    jobClassification: o6.String = o6.field(name="JobClassification")
    customerName: o6.String = o6.field(name="CustomerName")
    productionDatasetName: o6.String = o6.field(name="ProductionDatasetName")
    productionDatasetDescription: o6.String = o6.field(name="ProductionDatasetDescription")
    material: list[o6.String] = o6.field(name="Material", arrayDimensions=[0])
    productName: list[o6.String] = o6.field(name="ProductName", arrayDimensions=[0])
    productDescription: list[o6.String] = o6.field(name="ProductDescription", arrayDimensions=[0])
    jobPriority: o6.String = o6.field(name="JobPriority")
    plannedStart: o6.DateTime = o6.field(name="PlannedStart")
    plannedProductionTime: o6.Double = o6.field(name="PlannedProductionTime")
    latestEnd: o6.DateTime = o6.field(name="LatestEnd")
    nominalParts: o6.UInt64 = o6.field(name="NominalParts")
    nominalBoxParts: o6.UInt64 = o6.field(name="NominalBoxParts")
    expectedCycleTime: o6.Double = o6.field(name="ExpectedCycleTime")
    mouldId: o6.String = o6.field(name="MouldId")
    numCavities: o6.UInt32 = o6.field(name="NumCavities")


@o6.datatype(
    nodeId="ns=plastics_rubber;i=3023",
    browseName="ns=plastics_rubber;PIDParametersDataType",
    description="Structure for storing the parameters of a PID controller",
    defaultEncodingId="ns=plastics_rubber;i=5017",
)
class PIDParametersDataType(ns0.datatypes.Structure):
    p: o6.Double = o6.field(name="P")
    i: o6.Double = o6.field(name="I")
    d: o6.Double = o6.field(name="D")


@o6.datatype(nodeId="ns=plastics_rubber;i=3024", browseName="ns=plastics_rubber;ConfigurationParameterType", defaultEncodingId="ns=plastics_rubber;i=5003")
class ConfigurationParameterType(ns0.datatypes.Structure):
    id: o6.UInt32 = o6.field(name="Id")
    description: o6.LocalizedText = o6.field(name="Description")
    defaultValue: Any = o6.field(name="DefaultValue")
    unit: ns0.datatypes.EUInformation = o6.field(name="Unit")


@o6.enumtype(nodeId="ns=plastics_rubber;i=3025", browseName="ns=plastics_rubber;StartEnumeration")
class StartEnumeration(ns0.datatypes.Enumeration):
    NOT_READY_TO_START = o6.enumfield(0, name="NOT_READY_TO_START")
    START_BLOCKED_BY_CLIENT = o6.enumfield(1, name="START_BLOCKED_BY_CLIENT")
    READY_TO_START = o6.enumfield(2, name="READY_TO_START")
    START_REQUESTED = o6.enumfield(3, name="START_REQUESTED")
    STARTED = o6.enumfield(4, name="STARTED")
    STOP_REQUESTED = o6.enumfield(5, name="STOP_REQUESTED")


@o6.datatype(nodeId="ns=plastics_rubber;i=3026", browseName="ns=plastics_rubber;ParameterSettingType", defaultEncodingId="ns=plastics_rubber;i=5015")
class ParameterSettingType(ns0.datatypes.Structure):
    id: o6.UInt32 = o6.field(name="Id")
    value: Any = o6.field(name="Value")


@o6.enumtype(nodeId="ns=plastics_rubber;i=3027", browseName="ns=plastics_rubber;DiagnosticsStatusEnumeration")
class DiagnosticsStatusEnumeration(ns0.datatypes.Enumeration):
    OFF = o6.enumfield(0, name="OFF")
    ACTIVE_OK = o6.enumfield(1, name="ACTIVE_OK")
    ACTIVE_ERROR_DETECTED = o6.enumfield(2, name="ACTIVE_ERROR_DETECTED")
    COMPLETE = o6.enumfield(3, name="COMPLETE")
    COMPLETE_ERROR_DETECTED = o6.enumfield(4, name="COMPLETE_ERROR_DETECTED")


@o6.datatype(
    nodeId="ns=plastics_rubber;i=3028",
    browseName="ns=plastics_rubber;ActiveErrorDataType",
    description="Iinformation about an active error in a device",
    defaultEncodingId="ns=plastics_rubber;i=5048",
)
class ActiveErrorDataType(ns0.datatypes.Structure):
    id: o6.String = o6.field(name="Id")
    severity: o6.UInt16 = o6.field(name="Severity")
    message: o6.LocalizedText = o6.field(name="Message")


@o6.datatype(
    nodeId="ns=plastics_rubber;i=3003",
    browseName="ns=plastics_rubber;ClassifiedActiveErrorDataType",
    description="Iinformation about an active error in a device including the SoureNodes and a Classification",
    defaultEncodingId="ns=plastics_rubber;i=5065",
)
class ClassifiedActiveErrorDataType(ActiveErrorDataType):
    id: o6.String = o6.field(name="Id")
    severity: o6.UInt16 = o6.field(name="Severity")
    message: o6.LocalizedText = o6.field(name="Message")
    sourceNodes: list[o6.NodeId] = o6.field(name="SourceNodes", arrayDimensions=[0])
    classification: o6.UInt16 = o6.field(name="Classification")


@o6.enumtype(nodeId="ns=plastics_rubber;i=3029", browseName="ns=plastics_rubber;TemperatureZoneClassificationEnumeration", description="Type of the temperature zone")
class TemperatureZoneClassificationEnumeration(ns0.datatypes.Enumeration):
    OTHER = o6.enumfield(0, name="OTHER")
    HEATING = o6.enumfield(1, name="HEATING")
    COOLING = o6.enumfield(2, name="COOLING")
    TEMPERATURE_CONTROL = o6.enumfield(3, name="TEMPERATURE_CONTROL")
    HOT_RUNNER = o6.enumfield(4, name="HOT_RUNNER")
    MEASURING = o6.enumfield(5, name="MEASURING")


del Any, TYPE_CHECKING, uuid, o6, di, ns0
