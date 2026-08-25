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

from typing import Any, Sequence, SupportsFloat

import numpy as np

_Integer = int | np.integer[Any]

_Boolean = bool | np.bool_

import enum

from o6.node import ObjectNode as _ObjectNode, VariableNode as _VariableNode

import uuid

import o6

import o6.ns.di as di

import o6.ns.ns0 as ns0

class ControlModeEnumeration(enum.IntFlag):
    """Indication how the parameter is currently controlled"""

    OTHER = 0
    OFF = 1
    AUTOMATIC = 2
    TUNING = 3
    STANDBY = 4
    OPEN_LOOP = 5
    ONLY_MEASUREMENT = 6

class StorageEnumeration(enum.IntFlag):
    """Indication which parts of the production dataset shall be activated in the machine control after writing"""

    PRODUCTION = 1
    PREPARATION = 2
    FILE_SYSTEM = 4

class ProductionDatasetWriteOptionsType(ns0.datatypes.Structure):
    """Used as GenerateOptions in the Method GenerateFileForWrite in ProductionDatasetTransfer"""

    @property
    def storage(self) -> StorageEnumeration: ...
    @storage.setter
    def storage(self, value: _Integer) -> None: ...
    @property
    def name(self) -> o6.String: ...
    @name.setter
    def name(self, value: o6.String) -> None: ...
    @property
    def components(self) -> list[o6.UInt16]: ...
    @components.setter
    def components(self, value: Sequence[_Integer]) -> None: ...

class ProductionDatasetInformationType(ns0.datatypes.Structure):
    """Information on a production dataset"""

    @property
    def name(self) -> o6.String: ...
    @name.setter
    def name(self, value: o6.String) -> None: ...
    @property
    def description(self) -> o6.String: ...
    @description.setter
    def description(self, value: o6.String) -> None: ...
    @property
    def mESId(self) -> o6.String: ...
    @mESId.setter
    def mESId(self, value: o6.String) -> None: ...
    @property
    def creationTimestamp(self) -> o6.DateTime: ...
    @creationTimestamp.setter
    def creationTimestamp(self, value: o6.DateTime) -> None: ...
    @property
    def lastModificationTimestamp(self) -> o6.DateTime: ...
    @lastModificationTimestamp.setter
    def lastModificationTimestamp(self, value: o6.DateTime) -> None: ...
    @property
    def lastSaveTimestamp(self) -> o6.DateTime: ...
    @lastSaveTimestamp.setter
    def lastSaveTimestamp(self, value: o6.DateTime) -> None: ...
    @property
    def userName(self) -> o6.String: ...
    @userName.setter
    def userName(self, value: o6.String) -> None: ...
    @property
    def components(self) -> list[o6.UInt16]: ...
    @components.setter
    def components(self, value: Sequence[_Integer]) -> None: ...
    @property
    def manufacturer(self) -> o6.String: ...
    @manufacturer.setter
    def manufacturer(self, value: o6.String) -> None: ...
    @property
    def serialNumber(self) -> o6.String: ...
    @serialNumber.setter
    def serialNumber(self, value: o6.String) -> None: ...
    @property
    def model(self) -> o6.String: ...
    @model.setter
    def model(self, value: o6.String) -> None: ...
    @property
    def controllerName(self) -> o6.String: ...
    @controllerName.setter
    def controllerName(self, value: o6.String) -> None: ...
    @property
    def userMachineName(self) -> o6.String: ...
    @userMachineName.setter
    def userMachineName(self, value: o6.String) -> None: ...
    @property
    def locationName(self) -> o6.String: ...
    @locationName.setter
    def locationName(self, value: o6.String) -> None: ...
    @property
    def productName(self) -> list[o6.String]: ...
    @productName.setter
    def productName(self, value: Sequence[o6.String]) -> None: ...
    @property
    def mouldId(self) -> o6.String: ...
    @mouldId.setter
    def mouldId(self, value: o6.String) -> None: ...
    @property
    def numCavities(self) -> o6.UInt32: ...
    @numCavities.setter
    def numCavities(self, value: _Integer) -> None: ...

class ProductionDatasetReadOptionsType(ns0.datatypes.Structure):
    """Used as GenerateOptions in the Method GenerateFileForRead in ProductionDatasetTransfer"""

    @property
    def storage(self) -> StorageEnumeration: ...
    @storage.setter
    def storage(self, value: _Integer) -> None: ...
    @property
    def name(self) -> o6.String: ...
    @name.setter
    def name(self, value: o6.String) -> None: ...

class MouldStatusEnumeration(enum.IntFlag):
    """Current (physical) status of the mould"""

    OTHER = 0
    MOULD_NOT_INSTALLED = 1
    MOULD_CHANGE = 2
    MOULD_INSTALLED = 3

class LogbookEventsEnumeration(enum.IntFlag):
    """Information which LogbookEvents are supported by the machine"""

    PARAMETER_CHANGE = 0
    USER = 1
    REMOTE_ACCESS = 2
    SEQUENCE_CHANGE = 3
    MACHINE_MODE_CHANGE = 4
    PRODUCTION_STATUS_CHANGE = 5
    PRODUCTION_DATASET_CHANGE = 6
    PRODUCTION_DATASET_FROZEN = 7
    STANDSTILL_REASON = 8
    MESSAGE = 9
    USER_FEEDBACK = 10

class UserChangeEnumeration(enum.IntFlag):
    """Information if a user logs in or off"""

    LOG_ON = 0
    LOG_OFF = 1

class MachineModeEnumeration(enum.IntFlag):
    """Current machine mode (as defined by mode selector on the machine)"""

    OTHER = 0
    AUTOMATIC = 1
    SEMI_AUTOMATIC = 2
    MANUAL = 3
    SETUP = 4
    SLEEP = 5

class SequenceChangeEnumeration(enum.IntFlag):
    """Classification of production sequence change"""

    UPDATE = 0
    ADD = 1
    MODIFY = 2
    MOVE = 3
    DELETE = 4

class MaintenanceStatusEnumeration(enum.IntFlag):
    """Maintenance status of a machine/device/component"""

    NOT_DUE = 0
    WARNING = 1
    DUE = 2

class PageEntryDataType(ns0.datatypes.Structure):
    """Information on a page that is implemented in the machine control system and shown on the screen of the machine"""

    @property
    def id(self) -> o6.String: ...
    @id.setter
    def id(self, value: o6.String) -> None: ...
    @property
    def title(self) -> o6.LocalizedText: ...
    @title.setter
    def title(self, value: o6.LocalizedText) -> None: ...

class StandstillReasonType(ns0.datatypes.Structure):
    """Description of a standstill reason"""

    @property
    def id(self) -> o6.String: ...
    @id.setter
    def id(self, value: o6.String) -> None: ...
    @property
    def text(self) -> o6.LocalizedText: ...
    @text.setter
    def text(self, value: o6.LocalizedText) -> None: ...
    @property
    def lockedByMES(self) -> o6.Boolean: ...
    @lockedByMES.setter
    def lockedByMES(self, value: _Boolean) -> None: ...

class ProductionStatusEnumeration(enum.IntFlag):
    """Production status of the machine"""

    OTHER = 0
    NO_PRODUCTION = 1
    START_UP = 2
    READY_FOR_PRODUCTION = 3
    PRODUCTION = 4
    DRY_RUN = 5

class JobStatusEnumeration(enum.IntFlag):
    """Current status of the job"""

    OTHER = 0
    TRANSFERRED_ASSIGNED = 1
    SET_UP_ACTIVE = 2
    SET_UP_INTERRUPTED = 3
    SET_UP_FINISHED = 4
    START_UP_ACTIVE = 5
    JOB_IN_PRODUCTION = 6
    JOB_INTERRUPTED = 7
    JOB_FINISHED = 8
    TEAR_DOWN_ACTIVE = 9
    TEAR_DOWN_INTERRUPTED = 10
    TEAR_DOWN_FINISHED = 11

class EventOriginatorEnumeration(enum.IntFlag):
    """Originator of an event"""

    OTHER = 0
    MACHINE = 1
    OPERATOR = 2
    MES = 3
    PERIPHERAL_DEVICE = 4

class CycleQualityEnumeration(enum.IntFlag):
    """Quality of the whole cycle"""

    GOOD_CYCLE = 0
    BAD_CYCLE = 1
    TEST_SAMPLE_CYCLE = 2
    FAILED_CYCLE = 3

class CavityCycleQualityEnumeration(enum.IntFlag):
    """Quality of the cycle for each cavity"""

    NO_PART = 0
    GOOD_PART = 1
    BAD_PART = 2
    REWORK = 3

class JobListElementType(ns0.datatypes.Structure):
    """Description of a job in a job list"""

    @property
    def jobName(self) -> o6.String: ...
    @jobName.setter
    def jobName(self, value: o6.String) -> None: ...
    @property
    def jobDescription(self) -> o6.String: ...
    @jobDescription.setter
    def jobDescription(self, value: o6.String) -> None: ...
    @property
    def jobClassification(self) -> o6.String: ...
    @jobClassification.setter
    def jobClassification(self, value: o6.String) -> None: ...
    @property
    def customerName(self) -> o6.String: ...
    @customerName.setter
    def customerName(self, value: o6.String) -> None: ...
    @property
    def productionDatasetName(self) -> o6.String: ...
    @productionDatasetName.setter
    def productionDatasetName(self, value: o6.String) -> None: ...
    @property
    def productionDatasetDescription(self) -> o6.String: ...
    @productionDatasetDescription.setter
    def productionDatasetDescription(self, value: o6.String) -> None: ...
    @property
    def material(self) -> list[o6.String]: ...
    @material.setter
    def material(self, value: Sequence[o6.String]) -> None: ...
    @property
    def productName(self) -> list[o6.String]: ...
    @productName.setter
    def productName(self, value: Sequence[o6.String]) -> None: ...
    @property
    def productDescription(self) -> list[o6.String]: ...
    @productDescription.setter
    def productDescription(self, value: Sequence[o6.String]) -> None: ...
    @property
    def jobPriority(self) -> o6.String: ...
    @jobPriority.setter
    def jobPriority(self, value: o6.String) -> None: ...
    @property
    def plannedStart(self) -> o6.DateTime: ...
    @plannedStart.setter
    def plannedStart(self, value: o6.DateTime) -> None: ...
    @property
    def plannedProductionTime(self) -> o6.Double: ...
    @plannedProductionTime.setter
    def plannedProductionTime(self, value: SupportsFloat) -> None: ...
    @property
    def latestEnd(self) -> o6.DateTime: ...
    @latestEnd.setter
    def latestEnd(self, value: o6.DateTime) -> None: ...

class CyclicJobListElementType(JobListElementType):
    """Description of a job in a cyclic job list"""

    @property
    def jobName(self) -> o6.String: ...
    @jobName.setter
    def jobName(self, value: o6.String) -> None: ...
    @property
    def jobDescription(self) -> o6.String: ...
    @jobDescription.setter
    def jobDescription(self, value: o6.String) -> None: ...
    @property
    def jobClassification(self) -> o6.String: ...
    @jobClassification.setter
    def jobClassification(self, value: o6.String) -> None: ...
    @property
    def customerName(self) -> o6.String: ...
    @customerName.setter
    def customerName(self, value: o6.String) -> None: ...
    @property
    def productionDatasetName(self) -> o6.String: ...
    @productionDatasetName.setter
    def productionDatasetName(self, value: o6.String) -> None: ...
    @property
    def productionDatasetDescription(self) -> o6.String: ...
    @productionDatasetDescription.setter
    def productionDatasetDescription(self, value: o6.String) -> None: ...
    @property
    def material(self) -> list[o6.String]: ...
    @material.setter
    def material(self, value: Sequence[o6.String]) -> None: ...
    @property
    def productName(self) -> list[o6.String]: ...
    @productName.setter
    def productName(self, value: Sequence[o6.String]) -> None: ...
    @property
    def productDescription(self) -> list[o6.String]: ...
    @productDescription.setter
    def productDescription(self, value: Sequence[o6.String]) -> None: ...
    @property
    def jobPriority(self) -> o6.String: ...
    @jobPriority.setter
    def jobPriority(self, value: o6.String) -> None: ...
    @property
    def plannedStart(self) -> o6.DateTime: ...
    @plannedStart.setter
    def plannedStart(self, value: o6.DateTime) -> None: ...
    @property
    def plannedProductionTime(self) -> o6.Double: ...
    @plannedProductionTime.setter
    def plannedProductionTime(self, value: SupportsFloat) -> None: ...
    @property
    def latestEnd(self) -> o6.DateTime: ...
    @latestEnd.setter
    def latestEnd(self, value: o6.DateTime) -> None: ...
    @property
    def nominalParts(self) -> o6.UInt64: ...
    @nominalParts.setter
    def nominalParts(self, value: _Integer) -> None: ...
    @property
    def nominalBoxParts(self) -> o6.UInt64: ...
    @nominalBoxParts.setter
    def nominalBoxParts(self, value: _Integer) -> None: ...
    @property
    def expectedCycleTime(self) -> o6.Double: ...
    @expectedCycleTime.setter
    def expectedCycleTime(self, value: SupportsFloat) -> None: ...
    @property
    def mouldId(self) -> o6.String: ...
    @mouldId.setter
    def mouldId(self, value: o6.String) -> None: ...
    @property
    def numCavities(self) -> o6.UInt32: ...
    @numCavities.setter
    def numCavities(self, value: _Integer) -> None: ...

class PIDParametersDataType(ns0.datatypes.Structure):
    """Structure for storing the parameters of a PID controller"""

    @property
    def p(self) -> o6.Double: ...
    @p.setter
    def p(self, value: SupportsFloat) -> None: ...
    @property
    def i(self) -> o6.Double: ...
    @i.setter
    def i(self, value: SupportsFloat) -> None: ...
    @property
    def d(self) -> o6.Double: ...
    @d.setter
    def d(self, value: SupportsFloat) -> None: ...

class ConfigurationParameterType(ns0.datatypes.Structure):
    @property
    def id(self) -> o6.UInt32: ...
    @id.setter
    def id(self, value: _Integer) -> None: ...
    @property
    def description(self) -> o6.LocalizedText: ...
    @description.setter
    def description(self, value: o6.LocalizedText) -> None: ...
    @property
    def defaultValue(self) -> Any: ...
    @defaultValue.setter
    def defaultValue(self, value: Any) -> None: ...
    @property
    def unit(self) -> ns0.datatypes.EUInformation: ...
    @unit.setter
    def unit(self, value: ns0.datatypes.EUInformation) -> None: ...

class StartEnumeration(enum.IntFlag):
    NOT_READY_TO_START = 0
    START_BLOCKED_BY_CLIENT = 1
    READY_TO_START = 2
    START_REQUESTED = 3
    STARTED = 4
    STOP_REQUESTED = 5

class ParameterSettingType(ns0.datatypes.Structure):
    @property
    def id(self) -> o6.UInt32: ...
    @id.setter
    def id(self, value: _Integer) -> None: ...
    @property
    def value(self) -> Any: ...
    @value.setter
    def value(self, value: Any) -> None: ...

class DiagnosticsStatusEnumeration(enum.IntFlag):
    OFF = 0
    ACTIVE_OK = 1
    ACTIVE_ERROR_DETECTED = 2
    COMPLETE = 3
    COMPLETE_ERROR_DETECTED = 4

class ActiveErrorDataType(ns0.datatypes.Structure):
    """Iinformation about an active error in a device"""

    @property
    def id(self) -> o6.String: ...
    @id.setter
    def id(self, value: o6.String) -> None: ...
    @property
    def severity(self) -> o6.UInt16: ...
    @severity.setter
    def severity(self, value: _Integer) -> None: ...
    @property
    def message(self) -> o6.LocalizedText: ...
    @message.setter
    def message(self, value: o6.LocalizedText) -> None: ...

class ClassifiedActiveErrorDataType(ActiveErrorDataType):
    """Iinformation about an active error in a device including the SoureNodes and a Classification"""

    @property
    def id(self) -> o6.String: ...
    @id.setter
    def id(self, value: o6.String) -> None: ...
    @property
    def severity(self) -> o6.UInt16: ...
    @severity.setter
    def severity(self, value: _Integer) -> None: ...
    @property
    def message(self) -> o6.LocalizedText: ...
    @message.setter
    def message(self, value: o6.LocalizedText) -> None: ...
    @property
    def sourceNodes(self) -> list[o6.NodeId]: ...
    @sourceNodes.setter
    def sourceNodes(self, value: Sequence[o6.NodeId]) -> None: ...
    @property
    def classification(self) -> o6.UInt16: ...
    @classification.setter
    def classification(self, value: _Integer) -> None: ...

class TemperatureZoneClassificationEnumeration(enum.IntFlag):
    """Type of the temperature zone"""

    OTHER = 0
    HEATING = 1
    COOLING = 2
    TEMPERATURE_CONTROL = 3
    HOT_RUNNER = 4
    MEASURING = 5
