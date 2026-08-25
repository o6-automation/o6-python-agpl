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

"""Generated OPC UA gms namespace declarations."""

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
import o6.ns.machinery_result as machinery_result
import o6.ns.ns0 as ns0
from . import datatypes as gms_datypes
from . import vartypes as gms_vartypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(nodeId="ns=gms;i=1002", browseName="ns=gms;GMSType", displayName="GMSType")
class GMSType(machine_tool.objtypes.MachineToolType):
    equipment: GMSEquipmentType
    identification: GMSIdentificationType
    monitoring: GMSMonitoringType
    notification: machine_tool.objtypes.NotificationType
    production: machine_tool.objtypes.ProductionType
    resultManagement: GMSResultManagementType


@o6.objecttype(nodeId="ns=gms;i=1004", browseName="ns=gms;GMSMonitoringType", displayName="GMSMonitoringType")
class GMSMonitoringType(machine_tool.objtypes.MonitoringType):
    loadingMonitoring: LoadingMonitoringType | None
    toolMonitoring: ToolMonitoringType | None


@o6.objecttype(nodeId="ns=gms;i=1008", browseName="ns=gms;GMSResultManagementType", displayName="GMSResultManagementType")
class GMSResultManagementType(machinery_result.objtypes.ResultManagementType):
    correctionsFolder: ns0.objtypes.FolderType | None


@o6.objecttype(nodeId="ns=gms;i=1014", browseName="ns=gms;LoadingMonitoringType", displayName="LoadingMonitoringType")
class LoadingMonitoringType(machine_tool.objtypes.ElementMonitoringType):
    isInLoadingPosition: ns0.vartypes.TwoStateDiscreteType | None
    loadStatus: ns0.vartypes.MultiStateDiscreteType


@o6.objecttype(nodeId="ns=gms;i=1003", browseName="ns=gms;GMSEquipmentType", displayName="GMSEquipmentType")
class GMSEquipmentType(machine_tool.objtypes.EquipmentType):
    accessories: ns0.objtypes.FolderType | None
    additionalSensor: ns0.objtypes.FolderType | None
    tools: machine_tool.objtypes.ToolListType | None = o6.hasComponent(machine_tool.objtypes.ToolListType(nodeId="ns=gms;i=5017", browseName="ns=machine_tool;Tools"))


@o6.objecttype(nodeId="ns=gms;i=1011", browseName="ns=gms;GMSIdentificationType", displayName="GMSIdentificationType")
class GMSIdentificationType(machine_tool.objtypes.MachineToolIdentificationType):
    subDeviceClass: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=gms;i=6012", browseName="ns=gms;SubDeviceClass", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    workspace: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=gms;i=6001", browseName="ns=gms;Workspace", dataType=gms_datypes.WorkspaceType)
    )


@o6.objecttype(nodeId="ns=gms;i=1012", browseName="ns=gms;MultiSensorType", displayName="MultiSensorType")
class MultiSensorType(machine_tool.objtypes.MultiToolType):
    alignment: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=gms;i=6018", browseName="ns=gms;Alignment", dataType=gms_datypes.ToolAlignmentState, accessLevel=3, userAccessLevel=1)
    )
    axes: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=gms;i=6016", browseName="ns=gms;Axes", dataType=o6.String, valueRank=1, arrayDimensions=[0], accessLevel=3, userAccessLevel=1)
    )
    langleToolRangle: SensorType | None


@o6.objecttype(nodeId="ns=gms;i=1010", browseName="ns=gms;SensorWarningAlarmType", displayName="SensorWarningAlarmType")
class SensorWarningAlarmType(ns0.objtypes.LimitAlarmType):
    errorCode: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=gms;i=6029", browseName="ns=gms;ErrorCode", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=gms;i=1006", browseName="ns=gms;ToolMonitoringType", displayName="ToolMonitoringType")
class ToolMonitoringType(machine_tool.objtypes.WorkingUnitMonitoringType):
    activeTool: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=gms;i=6068", browseName="ns=gms;ActiveTool", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0], accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=gms;i=1005", browseName="ns=gms;CorrectionType", displayName="CorrectionType")
class CorrectionType(ns0.objtypes.BaseObjectType):
    characteristicIdentifier: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=gms;i=6009", browseName="ns=gms;CharacteristicIdentifier", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    correctionValueAbsolute: ns0.vartypes.AnalogUnitType | None
    correctionValueRelative: ns0.vartypes.AnalogUnitType | None
    description: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=gms;i=6082", browseName="ns=gms;Description", dataType=o6.LocalizedText, accessLevel=3, userAccessLevel=1)
    )
    identifier: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=gms;i=6002", browseName="ns=gms;Identifier", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    lowerControlLimit: ns0.vartypes.AnalogUnitType | None
    programName: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=gms;i=6050", browseName="ns=gms;ProgramName", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    upperControlLimit: ns0.vartypes.AnalogUnitType | None


@o6.objecttype(nodeId="ns=gms;i=1009", browseName="ns=gms;CharacteristicType", displayName="CharacteristicType")
class CharacteristicType(ns0.objtypes.BaseObjectType):
    characteristicIdentifier: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=gms;i=6028", browseName="ns=gms;CharacteristicIdentifier", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    characteristicsClass: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=gms;i=6046", browseName="ns=gms;CharacteristicsClass", dataType=o6.Byte, accessLevel=3, userAccessLevel=1)
    )
    formula: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=gms;i=6122", browseName="ns=gms;Formula", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    isValid: ns0.vartypes.PropertyType | None = o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
        # It is intentionally omitted; the server supplies a typed default.
        ns0.vartypes.PropertyType(nodeId="ns=gms;i=6111", browseName="ns=gms;IsValid", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
    )
    lowerToleranceLimit: ns0.vartypes.AnalogUnitType | None
    nominal: ns0.vartypes.AnalogUnitType | None
    resultEvaluation: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=gms;i=6038", browseName="ns=gms;ResultEvaluation", dataType=machinery_result.datatypes.ResultEvaluationEnum, accessLevel=3, userAccessLevel=1
        )
    )
    resultValue: ns0.vartypes.AnalogUnitType | None
    upperToleranceLimit: ns0.vartypes.AnalogUnitType | None


@o6.objecttype(nodeId="ns=gms;i=1001", browseName="ns=gms;IntermediateResultEventType", displayName="IntermediateResultEventType", isAbstract=True)
class IntermediateResultEventType(machinery_result.objtypes.ResultReadyEventType):
    langleCharacteristicsRangle: CharacteristicType = o6.hasComponent(
        CharacteristicType(nodeId="ns=gms;i=5033", browseName="ns=gms;<Characteristics>", modellingRule="MandatoryPlaceholder")
    )
    programName: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=gms;i=6121", browseName="ns=gms;ProgramName", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )


o6.reference(GMSResultManagementType, "i=41", IntermediateResultEventType)


@o6.objecttype(nodeId="ns=gms;i=1007", browseName="ns=gms;SensorType", displayName="SensorType")
class SensorType(machine_tool.objtypes.ToolType):
    absoluteProbe: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=gms;i=6127", browseName="ns=gms;AbsoluteProbe", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
    )
    alignment: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=gms;i=6021", browseName="ns=gms;Alignment", dataType=gms_datypes.ToolAlignmentState, accessLevel=3, userAccessLevel=1)
    )
    axes: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=gms;i=6084", browseName="ns=gms;Axes", dataType=o6.String, valueRank=1, arrayDimensions=[0], accessLevel=3, userAccessLevel=1)
    )
    capabilities: ns0.vartypes.MultiStateDiscreteType | None
    class_: ns0.vartypes.MultiStateDiscreteType
    engineeringUnit: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=gms;i=6126", browseName="ns=gms;EngineeringUnit", dataType=ns0.datatypes.EUInformation, accessLevel=3, userAccessLevel=1)
    )
    isQualifiedStatus: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=gms;i=6020", browseName="ns=gms;IsQualifiedStatus", dataType=gms_datypes.ToolIsQualifiedStatus, accessLevel=3, userAccessLevel=1)
    )
    measuringRange: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=gms;i=6123", browseName="ns=gms;MeasuringRange", dataType=o6.Double, accessLevel=3, userAccessLevel=1)
    )
    resolution: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=gms;i=6125", browseName="ns=gms;Resolution", dataType=o6.Double, accessLevel=3, userAccessLevel=1)
    )
    toolLife: ns0.objtypes.BaseObjectType
    workingRange: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=gms;i=6124", browseName="ns=gms;WorkingRange", dataType=o6.Double, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=gms;i=1015", browseName="ns=gms;SensorExchangeRackType", displayName="SensorExchangeRackType")
class SensorExchangeRackType(ns0.objtypes.BaseObjectType):
    identification: machinery.objtypes.MachineryItemIdentificationType
    isAvailable: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=gms;i=6134", browseName="ns=gms;IsAvailable", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=gms;i=1022", browseName="ns=gms;TipExchangeRackType", displayName="TipExchangeRackType")
class TipExchangeRackType(ns0.objtypes.BaseObjectType):
    identification: machinery.objtypes.MachineryItemIdentificationType
    isAvailable: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=gms;i=6137", browseName="ns=gms;IsAvailable", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=gms;i=1016", browseName="ns=gms;GMSJobType", displayName="GMSJobType")
class GMSJobType(machine_tool.objtypes.ProductionJobType):
    batchIdentifier: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=gms;i=6312", browseName="ns=gms;BatchIdentifier", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    duration: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=gms;i=6114", browseName="ns=gms;Duration", dataType=ns0.datatypes.Duration, accessLevel=3, userAccessLevel=1)
    )
    measurementReason: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=gms;i=6085", browseName="ns=gms;MeasurementReason", dataType=gms_datypes.MeasurementReasonEnum, accessLevel=3, userAccessLevel=1)
    )
    remainingTime: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=gms;i=6119", browseName="ns=gms;RemainingTime", dataType=ns0.datatypes.Duration, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=gms;i=1017", browseName="ns=gms;GMSPartType", displayName="GMSPartType")
class GMSPartType(machine_tool.objtypes.ProductionPartType):
    nestIdentifier: gms_vartypes.CatalogType | None
    operator: gms_vartypes.CatalogType | None
    partAmendmentStatus: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=gms;i=6314", browseName="ns=gms;PartAmendmentStatus", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    partCarrierIdentifier: gms_vartypes.CatalogType | None
    partDescription: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=gms;i=6313", browseName="ns=gms;PartDescription", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    processParameter: gms_vartypes.CatalogType | None
    processingMachineIdentifier: gms_vartypes.CatalogType | None
    productionNumber: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=gms;i=6315", browseName="ns=gms;ProductionNumber", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=gms;i=1018", browseName="ns=gms;RotaryTableType", displayName="RotaryTableType")
class RotaryTableType(ns0.objtypes.BaseObjectType):
    identification: machinery.objtypes.MachineryItemIdentificationType
    isIntegrated: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=gms;i=6350", browseName="ns=gms;IsIntegrated", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
    )
    numberOfAxes: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=gms;i=6351", browseName="ns=gms;NumberOfAxes", dataType=o6.Byte, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=gms;i=1019", browseName="ns=gms;CalibrationPrognosisType", displayName="CalibrationPrognosisType")
class CalibrationPrognosisType(machine_tool.objtypes.PrognosisType):
    calibrated: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=gms;i=6352", browseName="ns=gms;Calibrated", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
    )
    calibrationCertificate: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=gms;i=6107", browseName="ns=gms;CalibrationCertificate", dataType=o6.String, valueRank=1, arrayDimensions=[0], accessLevel=3, userAccessLevel=1
        )
    )
    calibrationInterval: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=gms;i=6354", browseName="ns=gms;CalibrationInterval", dataType=ns0.datatypes.Duration, accessLevel=3, userAccessLevel=1)
    )
    calibrationPreptime: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=gms;i=6355", browseName="ns=gms;CalibrationPreptime", dataType=ns0.datatypes.Duration, accessLevel=3, userAccessLevel=1)
    )
    dateOfCalibration: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=gms;i=6353", browseName="ns=gms;DateOfCalibration", dataType=ns0.datatypes.UtcTime, accessLevel=3, userAccessLevel=1)
    )


del Any, TYPE_CHECKING, uuid, o6, di, ia, isa95_jobcontrol_v2, machine_tool, machinery, machinery_jobs, machinery_result, ns0, gms_datypes, gms_vartypes
