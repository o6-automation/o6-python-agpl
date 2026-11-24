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

"""Generated OPC UA ijt_base namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.amb as amb
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.machinery as machinery
import o6.ns.machinery_result as machinery_result
import o6.ns.ns0 as ns0

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.datatype(
    nodeId="ns=ijt_base;i=3003",
    browseName="ns=ijt_base;CalibrationDataType",
    description="This structure contains the Calibration information. It is used as an input argument in SetCalibration method.\nNote: The input data sent in SetCalibration shall be updated in the respective parameters of the asset under Maintenance/Calibration.",
    defaultEncodingId="ns=ijt_base;i=5017",
)
class CalibrationDataType(ns0.datatypes.Structure):
    lastCalibration: o6.DateTime = o6.field(name="LastCalibration")
    calibrationPlace: o6.String | None = o6.field(name="CalibrationPlace")
    nextCalibration: o6.DateTime | None = o6.field(name="NextCalibration")
    calibrationValue: o6.Double | None = o6.field(name="CalibrationValue")
    sensorScale: o6.Double | None = o6.field(name="SensorScale")
    certificateUri: o6.String | None = o6.field(name="CertificateUri")
    engineeringUnits: ns0.datatypes.EUInformation | None = o6.field(name="EngineeringUnits")


@o6.datatype(
    nodeId="ns=ijt_base;i=3004",
    browseName="ns=ijt_base;ResultCounterDataType",
    description="This structure is used to provide various types of counters associated to a Result. These counters are related to a joining process with sub-processes.",
    defaultEncodingId="ns=ijt_base;i=5089",
)
class ResultCounterDataType(ns0.datatypes.Structure):
    name: o6.String | None = o6.field(name="Name")
    counterValue: o6.UInt32 = o6.field(name="CounterValue")
    counterType: o6.Int16 = o6.field(name="CounterType")


@o6.datatype(
    nodeId="ns=ijt_base;i=3006",
    browseName="ns=ijt_base;ErrorInformationDataType",
    description="This structure represents the errors occurred in the system which are outside the boundaries of the given program.",
    defaultEncodingId="ns=ijt_base;i=5053",
)
class ErrorInformationDataType(ns0.datatypes.Structure):
    errorType: o6.Byte = o6.field(name="ErrorType")
    errorId: o6.String | None = o6.field(name="ErrorId")
    legacyError: o6.String | None = o6.field(name="LegacyError")
    errorMessage: o6.LocalizedText | None = o6.field(name="ErrorMessage")


@o6.datatype(
    nodeId="ns=ijt_base;i=3007",
    browseName="ns=ijt_base;ResultValueDataType",
    description="It is used to report measurement values of the joining operation. Those are meant to characterize the quality of the process. It is used in JoiningResultDataType and StepResultDataType.",
    defaultEncodingId="ns=ijt_base;i=5056",
)
class ResultValueDataType(ns0.datatypes.Structure):
    measuredValue: o6.Double = o6.field(name="MeasuredValue")
    name: o6.String | None = o6.field(name="Name")
    resultEvaluation: machinery_result.datatypes.ResultEvaluationEnum | None = o6.field(name="ResultEvaluation")
    valueId: o6.String | None = o6.field(name="ValueId")
    valueTag: o6.Int16 | None = o6.field(name="ValueTag")
    tracePointIndex: o6.Int32 | None = o6.field(name="TracePointIndex")
    tracePointTimeOffset: o6.Double | None = o6.field(name="TracePointTimeOffset")
    parameterIdList: list[o6.String] | None = o6.field(name="ParameterIdList", arrayDimensions=[0])
    violationType: o6.Byte | None = o6.field(name="ViolationType")
    violationConsequence: o6.Byte | None = o6.field(name="ViolationConsequence")
    sensorId: o6.String | None = o6.field(name="SensorId")
    lowLimit: o6.Double | None = o6.field(name="LowLimit")
    highLimit: o6.Double | None = o6.field(name="HighLimit")
    targetValue: o6.Double | None = o6.field(name="TargetValue")
    resultStep: o6.String | None = o6.field(name="ResultStep")
    physicalQuantity: o6.Byte | None = o6.field(name="PhysicalQuantity")
    engineeringUnits: ns0.datatypes.EUInformation | None = o6.field(name="EngineeringUnits")


@o6.datatype(
    nodeId="ns=ijt_base;i=3008",
    browseName="ns=ijt_base;KeyValueDataType",
    description="This structure is similar to 0:KeyValuePair which uses 0:TrimmedString instead of 0:QualifiedName.",
    defaultEncodingId="ns=ijt_base;i=5148",
)
class KeyValueDataType(ns0.datatypes.Structure):
    key: o6.String = o6.field(name="Key")
    value: Any = o6.field(name="Value")


@o6.datatype(
    nodeId="ns=ijt_base;i=3009",
    browseName="ns=ijt_base;StepResultDataType",
    description="This structure represents the measurement values corresponding to a given step in the program. It is used in JoiningResultDataType.",
    defaultEncodingId="ns=ijt_base;i=5059",
)
class StepResultDataType(ns0.datatypes.Structure):
    stepResultId: o6.String = o6.field(name="StepResultId")
    programStepId: o6.String | None = o6.field(name="ProgramStepId")
    programStep: o6.String | None = o6.field(name="ProgramStep")
    name: o6.String | None = o6.field(name="Name")
    resultEvaluation: machinery_result.datatypes.ResultEvaluationEnum | None = o6.field(name="ResultEvaluation")
    startTimeOffset: o6.Double | None = o6.field(name="StartTimeOffset")
    stepTraceId: o6.String | None = o6.field(name="StepTraceId")
    stepResultValues: list[ResultValueDataType] | None = o6.field(name="StepResultValues", arrayDimensions=[0])


@o6.datatype(
    nodeId="ns=ijt_base;i=3010",
    browseName="ns=ijt_base;EntityDataType",
    description="This structure provides the identification data for a given entity in the system.",
    defaultEncodingId="ns=ijt_base;i=5079",
)
class EntityDataType(ns0.datatypes.Structure):
    name: o6.String | None = o6.field(name="Name")
    description: o6.String | None = o6.field(name="Description")
    entityId: o6.String = o6.field(name="EntityId")
    entityOriginId: o6.String | None = o6.field(name="EntityOriginId")
    isExternal: o6.Boolean | None = o6.field(name="IsExternal")
    entityType: o6.Int16 = o6.field(name="EntityType")


@o6.datatype(
    nodeId="ns=ijt_base;i=3011",
    browseName="ns=ijt_base;TraceDataType",
    description="It is a base type to encapsulate common data for a Trace.",
    defaultEncodingId="ns=ijt_base;i=5062",
)
class TraceDataType(ns0.datatypes.Structure):
    traceId: o6.String = o6.field(name="TraceId")
    resultId: o6.String = o6.field(name="ResultId")


@o6.datatype(
    nodeId="ns=ijt_base;i=3014",
    browseName="ns=ijt_base;TraceContentDataType",
    description="It is to describe the trace samples for a given program step. It is used in StepTraceDataType.",
    defaultEncodingId="ns=ijt_base;i=5071",
)
class TraceContentDataType(ns0.datatypes.Structure):
    values: list[o6.Double] = o6.field(name="Values", arrayDimensions=[0])
    sensorId: o6.String | None = o6.field(name="SensorId")
    name: o6.String | None = o6.field(name="Name")
    description: o6.String | None = o6.field(name="Description")
    physicalQuantity: o6.Byte | None = o6.field(name="PhysicalQuantity")
    engineeringUnits: ns0.datatypes.EUInformation | None = o6.field(name="EngineeringUnits")


@o6.datatype(
    nodeId="ns=ijt_base;i=3013",
    browseName="ns=ijt_base;StepTraceDataType",
    description="It is to describe of the trace for a given program step. It is used in JoiningTraceDataType.",
    defaultEncodingId="ns=ijt_base;i=5068",
)
class StepTraceDataType(ns0.datatypes.Structure):
    stepTraceId: o6.String = o6.field(name="StepTraceId")
    stepResultId: o6.String = o6.field(name="StepResultId")
    numberOfTracePoints: o6.UInt32 = o6.field(name="NumberOfTracePoints")
    samplingInterval: o6.Double | None = o6.field(name="SamplingInterval")
    startTimeOffset: o6.Double | None = o6.field(name="StartTimeOffset")
    stepTraceContent: list[TraceContentDataType] = o6.field(name="StepTraceContent", arrayDimensions=[0])


@o6.datatype(
    nodeId="ns=ijt_base;i=3012",
    browseName="ns=ijt_base;JoiningTraceDataType",
    description="This structure is to describe the content of traces for all the steps in the given program. It is used in JoiningResultDataType.",
    defaultEncodingId="ns=ijt_base;i=5065",
)
class JoiningTraceDataType(TraceDataType):
    traceId: o6.String = o6.field(name="TraceId")
    resultId: o6.String = o6.field(name="ResultId")
    stepTraces: list[StepTraceDataType] = o6.field(name="StepTraces", arrayDimensions=[0])


@o6.datatype(
    nodeId="ns=ijt_base;i=3005",
    browseName="ns=ijt_base;JoiningResultDataType",
    description="This structure represents the data associated with Joining Result and the corresponding measurement values.",
    defaultEncodingId="ns=ijt_base;i=5049",
)
class JoiningResultDataType(ns0.datatypes.Structure):
    failureReason: o6.Byte | None = o6.field(name="FailureReason")
    overallResultValues: list[ResultValueDataType] = o6.field(name="OverallResultValues", arrayDimensions=[0])
    stepResults: list[StepResultDataType] | None = o6.field(name="StepResults", arrayDimensions=[0])
    errors: list[ErrorInformationDataType] | None = o6.field(name="Errors", arrayDimensions=[0])
    failingStepResultId: o6.String | None = o6.field(name="FailingStepResultId")
    trace: JoiningTraceDataType | None = o6.field(name="Trace")


@o6.datatype(
    nodeId="ns=ijt_base;i=3015",
    browseName="ns=ijt_base;DesignValueDataType",
    description="This structure provides the design value for a given physical quantity. It is used in JointDesignDataType.",
    defaultEncodingId="ns=ijt_base;i=5082",
)
class DesignValueDataType(ns0.datatypes.Structure):
    physicalQuantity: o6.Byte | None = o6.field(name="PhysicalQuantity")
    name: o6.String | None = o6.field(name="Name")
    designValue: Any | None = o6.field(name="DesignValue")
    engineeringUnits: ns0.datatypes.EUInformation | None = o6.field(name="EngineeringUnits")


@o6.datatype(
    nodeId="ns=ijt_base;i=3019",
    browseName="ns=ijt_base;SignalDataType",
    description="This structure contains the signal information which is used in SetIOSignals and GetIOSignals methods.",
    defaultEncodingId="ns=ijt_base;i=5081",
)
class SignalDataType(ns0.datatypes.Structure):
    signalId: o6.String = o6.field(name="SignalId")
    signalValue: Any = o6.field(name="SignalValue")
    signalDescription: o6.String = o6.field(name="SignalDescription")
    signalType: o6.Int16 = o6.field(name="SignalType")


@o6.datatype(
    nodeId="ns=ijt_base;i=3020",
    browseName="ns=ijt_base;JoiningResultMetaDataType",
    description="This structure is a subtype of ResultMetaDataType. It is used to define additional meta data of a Result in a joining system.",
    defaultEncodingId="ns=ijt_base;i=5046",
)
class JoiningResultMetaDataType(machinery_result.datatypes.ResultMetaDataType):
    resultId: o6.String = o6.field(name="ResultId")
    hasTransferableDataOnFile: o6.Boolean | None = o6.field(name="HasTransferableDataOnFile")
    isPartial: o6.Boolean | None = o6.field(name="IsPartial")
    isSimulated: o6.Boolean | None = o6.field(name="IsSimulated")
    resultState: o6.Int32 | None = o6.field(name="ResultState")
    stepId: o6.String | None = o6.field(name="StepId")
    partId: o6.String | None = o6.field(name="PartId")
    externalRecipeId: o6.String | None = o6.field(name="ExternalRecipeId")
    internalRecipeId: o6.String | None = o6.field(name="InternalRecipeId")
    productId: o6.String | None = o6.field(name="ProductId")
    externalConfigurationId: o6.String | None = o6.field(name="ExternalConfigurationId")
    internalConfigurationId: o6.String | None = o6.field(name="InternalConfigurationId")
    jobId: o6.String | None = o6.field(name="JobId")
    creationTime: o6.DateTime | None = o6.field(name="CreationTime")
    processingTimes: machinery_result.datatypes.ProcessingTimesDataType | None = o6.field(name="ProcessingTimes")
    resultUri: list[o6.String] | None = o6.field(name="ResultUri", arrayDimensions=[0])
    resultEvaluation: machinery_result.datatypes.ResultEvaluationEnum | None = o6.field(name="ResultEvaluation")
    resultEvaluationCode: o6.Int64 | None = o6.field(name="ResultEvaluationCode")
    resultEvaluationDetails: o6.LocalizedText | None = o6.field(name="ResultEvaluationDetails")
    fileFormat: list[o6.String] | None = o6.field(name="FileFormat", arrayDimensions=[0])
    joiningTechnology: o6.LocalizedText | None = o6.field(name="JoiningTechnology")
    sequenceNumber: o6.UInt64 | None = o6.field(name="SequenceNumber")
    name: o6.String | None = o6.field(name="Name")
    description: o6.LocalizedText | None = o6.field(name="Description")
    classification: o6.Byte | None = o6.field(name="Classification")
    operationMode: o6.Byte | None = o6.field(name="OperationMode")
    assemblyType: o6.Byte | None = o6.field(name="AssemblyType")
    associatedEntities: list[EntityDataType] | None = o6.field(name="AssociatedEntities", arrayDimensions=[0])
    resultCounters: list[ResultCounterDataType] | None = o6.field(name="ResultCounters", arrayDimensions=[0])
    interventionType: o6.Byte | None = o6.field(name="InterventionType")
    isGeneratedOffline: o6.Boolean | None = o6.field(name="IsGeneratedOffline")
    extendedMetaData: list[KeyValueDataType] | None = o6.field(name="ExtendedMetaData", arrayDimensions=[0])


@o6.datatype(
    nodeId="ns=ijt_base;i=3021",
    browseName="ns=ijt_base;JointComponentDataType",
    description="This structure is the base container for any joint component such as Bolt, Rivet, Gasket, Glue string, etc. \nNote: The concrete definition of joint component is not defined in this version of the specification.",
    defaultEncodingId="ns=ijt_base;i=5104",
)
class JointComponentDataType(ns0.datatypes.Structure):
    jointComponentId: o6.String = o6.field(name="JointComponentId")
    name: o6.String | None = o6.field(name="Name")
    description: o6.LocalizedText | None = o6.field(name="Description")
    manufacturer: o6.LocalizedText | None = o6.field(name="Manufacturer")
    manufacturerUri: o6.String | None = o6.field(name="ManufacturerUri")
    jointComponentContent: Any | None = o6.field(name="JointComponentContent")


@o6.datatype(
    nodeId="ns=ijt_base;i=3022",
    browseName="ns=ijt_base;ReportedValueDataType",
    description="This structure provides the given value and corresponding limits for a given physical quantity (if applicable).",
    defaultEncodingId="ns=ijt_base;i=5095",
)
class ReportedValueDataType(ns0.datatypes.Structure):
    physicalQuantity: o6.Byte | None = o6.field(name="PhysicalQuantity")
    name: o6.String | None = o6.field(name="Name")
    currentValue: Any = o6.field(name="CurrentValue")
    previousValue: Any | None = o6.field(name="PreviousValue")
    lowLimit: o6.Double | None = o6.field(name="LowLimit")
    highLimit: o6.Double | None = o6.field(name="HighLimit")
    engineeringUnits: ns0.datatypes.EUInformation | None = o6.field(name="EngineeringUnits")


@o6.datatype(
    nodeId="ns=ijt_base;i=3024",
    browseName="ns=ijt_base;JoiningProcessMetaDataType",
    description="This structure provides the meta data which describes the joining process.",
    defaultEncodingId="ns=ijt_base;i=5118",
)
class JoiningProcessMetaDataType(ns0.datatypes.Structure):
    joiningProcessId: o6.String = o6.field(name="JoiningProcessId")
    joiningProcessOriginId: o6.String | None = o6.field(name="JoiningProcessOriginId")
    creationTime: o6.DateTime | None = o6.field(name="CreationTime")
    lastUpdatedTime: o6.DateTime | None = o6.field(name="LastUpdatedTime")
    name: o6.String | None = o6.field(name="Name")
    description: o6.LocalizedText | None = o6.field(name="Description")
    joiningTechnology: o6.LocalizedText | None = o6.field(name="JoiningTechnology")
    classification: o6.Int16 | None = o6.field(name="Classification")
    associatedEntities: list[EntityDataType] | None = o6.field(name="AssociatedEntities", arrayDimensions=[0])


@o6.datatype(
    nodeId="ns=ijt_base;i=3016",
    browseName="ns=ijt_base;JoiningProcessDataType",
    description="This structure provides the base container for any joining process in a joining system. \nNote: This specification defines the meta data of a JoiningProcess, and the actual content of the Joining Process is application specific.",
    defaultEncodingId="ns=ijt_base;i=5115",
)
class JoiningProcessDataType(ns0.datatypes.Structure):
    joiningProcessMetaData: JoiningProcessMetaDataType = o6.field(name="JoiningProcessMetaData")
    joiningProcessContent: list[Any] = o6.field(name="JoiningProcessContent", arrayDimensions=[0])


@o6.datatype(
    nodeId="ns=ijt_base;i=3025",
    browseName="ns=ijt_base;JointDesignDataType",
    description="This structure provides the design information of a given joint.",
    defaultEncodingId="ns=ijt_base;i=5107",
)
class JointDesignDataType(ns0.datatypes.Structure):
    jointDesignId: o6.String = o6.field(name="JointDesignId")
    name: o6.String | None = o6.field(name="Name")
    description: o6.LocalizedText | None = o6.field(name="Description")
    jointDesignContent: list[DesignValueDataType] | None = o6.field(name="JointDesignContent", arrayDimensions=[0])
    jointComponentIdList: list[o6.String] | None = o6.field(name="JointComponentIdList", arrayDimensions=[0])


@o6.datatype(
    nodeId="ns=ijt_base;i=3028",
    browseName="ns=ijt_base;JointDataType",
    description="This structure provides the joint information. Joint is the physical outcome of the joining operation which determines the properties of the point where multiple parts are assembled.",
    defaultEncodingId="ns=ijt_base;i=5110",
)
class JointDataType(ns0.datatypes.Structure):
    jointId: o6.String = o6.field(name="JointId")
    jointOriginId: o6.String | None = o6.field(name="JointOriginId")
    jointDesignId: o6.String | None = o6.field(name="JointDesignId")
    creationTime: o6.DateTime | None = o6.field(name="CreationTime")
    lastUpdatedTime: o6.DateTime | None = o6.field(name="LastUpdatedTime")
    name: o6.String | None = o6.field(name="Name")
    description: o6.LocalizedText | None = o6.field(name="Description")
    classification: o6.Int16 | None = o6.field(name="Classification")
    classificationDetails: o6.LocalizedText | None = o6.field(name="ClassificationDetails")
    jointStatus: o6.String | None = o6.field(name="JointStatus")
    associatedEntities: list[EntityDataType] | None = o6.field(name="AssociatedEntities", arrayDimensions=[0])
    joiningTechnology: o6.LocalizedText | None = o6.field(name="JoiningTechnology")


@o6.datatype(
    nodeId="ns=ijt_base;i=3029",
    browseName="ns=ijt_base;JoiningProcessIdentificationDataType",
    description="This structure contains the identification information of a Joining Process. It is used in set of methods defined in JoiningProcessManagementType.",
    defaultEncodingId="ns=ijt_base;i=5121",
)
class JoiningProcessIdentificationDataType(ns0.datatypes.Structure):
    joiningProcessId: o6.String | None = o6.field(name="JoiningProcessId")
    joiningProcessOriginId: o6.String | None = o6.field(name="JoiningProcessOriginId")
    selectionName: o6.String | None = o6.field(name="SelectionName")


del Any, TYPE_CHECKING, uuid, o6, amb, di, ia, machinery, machinery_result, ns0
