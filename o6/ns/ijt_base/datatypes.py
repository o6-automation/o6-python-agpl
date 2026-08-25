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
    browseName="CalibrationDataType",
    description="This structure contains the Calibration information. It is used as an input argument in SetCalibration method.\nNote: The input data sent in SetCalibration shall be updated in the respective parameters of the asset under Maintenance/Calibration.",
    defaultEncodingId="ns=ijt_base;i=5017",
)
class CalibrationDataType(ns0.datatypes.Structure):
    lastCalibration: o6.DateTime
    calibrationPlace: o6.String | None
    nextCalibration: o6.DateTime | None
    calibrationValue: o6.Double | None
    sensorScale: o6.Double | None
    certificateUri: o6.String | None
    engineeringUnits: ns0.datatypes.EUInformation | None


@o6.datatype(
    nodeId="ns=ijt_base;i=3004",
    browseName="ResultCounterDataType",
    description="This structure is used to provide various types of counters associated to a Result. These counters are related to a joining process with sub-processes.",
    defaultEncodingId="ns=ijt_base;i=5089",
)
class ResultCounterDataType(ns0.datatypes.Structure):
    name: o6.String | None
    counterValue: o6.UInt32
    counterType: o6.Int16


@o6.datatype(
    nodeId="ns=ijt_base;i=3006",
    browseName="ErrorInformationDataType",
    description="This structure represents the errors occurred in the system which are outside the boundaries of the given program.",
    defaultEncodingId="ns=ijt_base;i=5053",
)
class ErrorInformationDataType(ns0.datatypes.Structure):
    errorType: o6.Byte
    errorId: o6.String | None
    legacyError: o6.String | None
    errorMessage: o6.LocalizedText | None


@o6.datatype(
    nodeId="ns=ijt_base;i=3007",
    browseName="ResultValueDataType",
    description="It is used to report measurement values of the joining operation. Those are meant to characterize the quality of the process. It is used in JoiningResultDataType and StepResultDataType.",
    defaultEncodingId="ns=ijt_base;i=5056",
)
class ResultValueDataType(ns0.datatypes.Structure):
    measuredValue: o6.Double
    name: o6.String | None
    resultEvaluation: machinery_result.datatypes.ResultEvaluationEnum | None
    valueId: o6.String | None
    valueTag: o6.Int16 | None
    tracePointIndex: o6.Int32 | None
    tracePointTimeOffset: o6.Double | None
    parameterIdList: list[o6.String] | None
    violationType: o6.Byte | None
    violationConsequence: o6.Byte | None
    sensorId: o6.String | None
    lowLimit: o6.Double | None
    highLimit: o6.Double | None
    targetValue: o6.Double | None
    resultStep: o6.String | None
    physicalQuantity: o6.Byte | None
    engineeringUnits: ns0.datatypes.EUInformation | None


@o6.datatype(
    nodeId="ns=ijt_base;i=3008",
    browseName="KeyValueDataType",
    description="This structure is similar to 0:KeyValuePair which uses 0:TrimmedString instead of 0:QualifiedName.",
    defaultEncodingId="ns=ijt_base;i=5148",
)
class KeyValueDataType(ns0.datatypes.Structure):
    key: o6.String
    value: Any


@o6.datatype(
    nodeId="ns=ijt_base;i=3009",
    browseName="StepResultDataType",
    description="This structure represents the measurement values corresponding to a given step in the program. It is used in JoiningResultDataType.",
    defaultEncodingId="ns=ijt_base;i=5059",
)
class StepResultDataType(ns0.datatypes.Structure):
    stepResultId: o6.String
    programStepId: o6.String | None
    programStep: o6.String | None
    name: o6.String | None
    resultEvaluation: machinery_result.datatypes.ResultEvaluationEnum | None
    startTimeOffset: o6.Double | None
    stepTraceId: o6.String | None
    stepResultValues: list[ResultValueDataType] | None


@o6.datatype(
    nodeId="ns=ijt_base;i=3010",
    browseName="EntityDataType",
    description="This structure provides the identification data for a given entity in the system.",
    defaultEncodingId="ns=ijt_base;i=5079",
)
class EntityDataType(ns0.datatypes.Structure):
    name: o6.String | None
    description: o6.String | None
    entityId: o6.String
    entityOriginId: o6.String | None
    isExternal: o6.Boolean | None
    entityType: o6.Int16


@o6.datatype(
    nodeId="ns=ijt_base;i=3011", browseName="TraceDataType", description="It is a base type to encapsulate common data for a Trace.", defaultEncodingId="ns=ijt_base;i=5062"
)
class TraceDataType(ns0.datatypes.Structure):
    traceId: o6.String
    resultId: o6.String


@o6.datatype(
    nodeId="ns=ijt_base;i=3014",
    browseName="TraceContentDataType",
    description="It is to describe the trace samples for a given program step. It is used in StepTraceDataType.",
    defaultEncodingId="ns=ijt_base;i=5071",
)
class TraceContentDataType(ns0.datatypes.Structure):
    values: list[o6.Double]
    sensorId: o6.String | None
    name: o6.String | None
    description: o6.String | None
    physicalQuantity: o6.Byte | None
    engineeringUnits: ns0.datatypes.EUInformation | None


@o6.datatype(
    nodeId="ns=ijt_base;i=3013",
    browseName="StepTraceDataType",
    description="It is to describe of the trace for a given program step. It is used in JoiningTraceDataType.",
    defaultEncodingId="ns=ijt_base;i=5068",
)
class StepTraceDataType(ns0.datatypes.Structure):
    stepTraceId: o6.String
    stepResultId: o6.String
    numberOfTracePoints: o6.UInt32
    samplingInterval: o6.Double | None
    startTimeOffset: o6.Double | None
    stepTraceContent: list[TraceContentDataType]


@o6.datatype(
    nodeId="ns=ijt_base;i=3012",
    browseName="JoiningTraceDataType",
    description="This structure is to describe the content of traces for all the steps in the given program. It is used in JoiningResultDataType.",
    defaultEncodingId="ns=ijt_base;i=5065",
)
class JoiningTraceDataType(TraceDataType):
    traceId: o6.String
    resultId: o6.String
    stepTraces: list[StepTraceDataType]


@o6.datatype(
    nodeId="ns=ijt_base;i=3005",
    browseName="JoiningResultDataType",
    description="This structure represents the data associated with Joining Result and the corresponding measurement values.",
    defaultEncodingId="ns=ijt_base;i=5049",
)
class JoiningResultDataType(ns0.datatypes.Structure):
    failureReason: o6.Byte | None
    overallResultValues: list[ResultValueDataType]
    stepResults: list[StepResultDataType] | None
    errors: list[ErrorInformationDataType] | None
    failingStepResultId: o6.String | None
    trace: JoiningTraceDataType | None


@o6.datatype(
    nodeId="ns=ijt_base;i=3015",
    browseName="DesignValueDataType",
    description="This structure provides the design value for a given physical quantity. It is used in JointDesignDataType.",
    defaultEncodingId="ns=ijt_base;i=5082",
)
class DesignValueDataType(ns0.datatypes.Structure):
    physicalQuantity: o6.Byte | None
    name: o6.String | None
    designValue: Any | None
    engineeringUnits: ns0.datatypes.EUInformation | None


@o6.datatype(
    nodeId="ns=ijt_base;i=3019",
    browseName="SignalDataType",
    description="This structure contains the signal information which is used in SetIOSignals and GetIOSignals methods.",
    defaultEncodingId="ns=ijt_base;i=5081",
)
class SignalDataType(ns0.datatypes.Structure):
    signalId: o6.String
    signalValue: o6.ExtensionObject
    signalDescription: o6.String
    signalType: o6.Int16


@o6.datatype(
    nodeId="ns=ijt_base;i=3020",
    browseName="JoiningResultMetaDataType",
    description="This structure is a subtype of ResultMetaDataType. It is used to define additional meta data of a Result in a joining system.",
    defaultEncodingId="ns=ijt_base;i=5046",
)
class JoiningResultMetaDataType(machinery_result.datatypes.ResultMetaDataType):
    resultId: o6.String
    hasTransferableDataOnFile: o6.Boolean | None
    isPartial: o6.Boolean | None
    isSimulated: o6.Boolean | None
    resultState: o6.Int32 | None
    stepId: o6.String | None
    partId: o6.String | None
    externalRecipeId: o6.String | None
    internalRecipeId: o6.String | None
    productId: o6.String | None
    externalConfigurationId: o6.String | None
    internalConfigurationId: o6.String | None
    jobId: o6.String | None
    creationTime: o6.DateTime | None
    processingTimes: machinery_result.datatypes.ProcessingTimesDataType | None
    resultUri: list[o6.String] | None
    resultEvaluation: machinery_result.datatypes.ResultEvaluationEnum | None
    resultEvaluationCode: o6.Int64 | None
    resultEvaluationDetails: o6.LocalizedText | None
    fileFormat: list[o6.String] | None
    joiningTechnology: o6.LocalizedText | None
    sequenceNumber: o6.UInt64 | None
    name: o6.String | None
    description: o6.LocalizedText | None
    classification: o6.Byte | None
    operationMode: o6.Byte | None
    assemblyType: o6.Byte | None
    associatedEntities: list[EntityDataType] | None
    resultCounters: list[ResultCounterDataType] | None
    interventionType: o6.Byte | None
    isGeneratedOffline: o6.Boolean | None
    extendedMetaData: list[KeyValueDataType] | None


@o6.datatype(
    nodeId="ns=ijt_base;i=3021",
    browseName="JointComponentDataType",
    description="This structure is the base container for any joint component such as Bolt, Rivet, Gasket, Glue string, etc. \nNote: The concrete definition of joint component is not defined in this version of the specification.",
    defaultEncodingId="ns=ijt_base;i=5104",
)
class JointComponentDataType(ns0.datatypes.Structure):
    jointComponentId: o6.String
    name: o6.String | None
    description: o6.LocalizedText | None
    manufacturer: o6.LocalizedText | None
    manufacturerUri: o6.String | None
    jointComponentContent: Any | None


@o6.datatype(
    nodeId="ns=ijt_base;i=3022",
    browseName="ReportedValueDataType",
    description="This structure provides the given value and corresponding limits for a given physical quantity (if applicable).",
    defaultEncodingId="ns=ijt_base;i=5095",
)
class ReportedValueDataType(ns0.datatypes.Structure):
    physicalQuantity: o6.Byte | None
    name: o6.String | None
    currentValue: Any
    previousValue: Any | None
    lowLimit: o6.Double | None
    highLimit: o6.Double | None
    engineeringUnits: ns0.datatypes.EUInformation | None


@o6.datatype(
    nodeId="ns=ijt_base;i=3024",
    browseName="JoiningProcessMetaDataType",
    description="This structure provides the meta data which describes the joining process.",
    defaultEncodingId="ns=ijt_base;i=5118",
)
class JoiningProcessMetaDataType(ns0.datatypes.Structure):
    joiningProcessId: o6.String
    joiningProcessOriginId: o6.String | None
    creationTime: o6.DateTime | None
    lastUpdatedTime: o6.DateTime | None
    name: o6.String | None
    description: o6.LocalizedText | None
    joiningTechnology: o6.LocalizedText | None
    classification: o6.Int16 | None
    associatedEntities: list[EntityDataType] | None


@o6.datatype(
    nodeId="ns=ijt_base;i=3016",
    browseName="JoiningProcessDataType",
    description="This structure provides the base container for any joining process in a joining system. \nNote: This specification defines the meta data of a JoiningProcess, and the actual content of the Joining Process is application specific.",
    defaultEncodingId="ns=ijt_base;i=5115",
)
class JoiningProcessDataType(ns0.datatypes.Structure):
    joiningProcessMetaData: JoiningProcessMetaDataType
    joiningProcessContent: list[Any]


@o6.datatype(
    nodeId="ns=ijt_base;i=3025",
    browseName="JointDesignDataType",
    description="This structure provides the design information of a given joint.",
    defaultEncodingId="ns=ijt_base;i=5107",
)
class JointDesignDataType(ns0.datatypes.Structure):
    jointDesignId: o6.String
    name: o6.String | None
    description: o6.LocalizedText | None
    jointDesignContent: list[DesignValueDataType] | None
    jointComponentIdList: list[o6.String] | None


@o6.datatype(
    nodeId="ns=ijt_base;i=3028",
    browseName="JointDataType",
    description="This structure provides the joint information. Joint is the physical outcome of the joining operation which determines the properties of the point where multiple parts are assembled.",
    defaultEncodingId="ns=ijt_base;i=5110",
)
class JointDataType(ns0.datatypes.Structure):
    jointId: o6.String
    jointOriginId: o6.String | None
    jointDesignId: o6.String | None
    creationTime: o6.DateTime | None
    lastUpdatedTime: o6.DateTime | None
    name: o6.String | None
    description: o6.LocalizedText | None
    classification: o6.Int16 | None
    classificationDetails: o6.LocalizedText | None
    jointStatus: o6.String | None
    associatedEntities: list[EntityDataType] | None
    joiningTechnology: o6.LocalizedText | None


@o6.datatype(
    nodeId="ns=ijt_base;i=3029",
    browseName="JoiningProcessIdentificationDataType",
    description="This structure contains the identification information of a Joining Process. It is used in set of methods defined in JoiningProcessManagementType.",
    defaultEncodingId="ns=ijt_base;i=5121",
)
class JoiningProcessIdentificationDataType(ns0.datatypes.Structure):
    joiningProcessId: o6.String | None
    joiningProcessOriginId: o6.String | None
    selectionName: o6.String | None


del Any, TYPE_CHECKING, uuid, o6, amb, di, ia, machinery, machinery_result, ns0
