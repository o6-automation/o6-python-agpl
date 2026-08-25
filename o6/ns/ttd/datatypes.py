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

"""Generated OPC UA ttd namespace declarations."""

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

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.datatype(nodeId="ns=ttd;i=3003", browseName="RecipeIdDataType", defaultEncodingId="ns=ttd;i=5002")
class RecipeIdDataType(ns0.datatypes.Structure):
    name: o6.String | None
    id: o6.String
    type: o6.String | None
    description: o6.String | None
    comment: o6.String | None
    modifiedDate: o6.DateTime | None
    version: o6.String | None
    validated: o6.Boolean | None


@o6.datatype(nodeId="ns=ttd;i=3006", browseName="ExchangeablePartDataType", defaultEncodingId="ns=ttd;i=5005")
class ExchangeablePartDataType(ns0.datatypes.Structure):
    partType: o6.String
    mounted: o6.Boolean
    traceable: o6.Boolean | None
    partId: o6.String | None
    machineReadable: o6.Boolean | None
    lastCalibrationDate: o6.DateTime | None


@o6.datatype(nodeId="ns=ttd;i=3009", browseName="OptionalModuleDataType", defaultEncodingId="ns=ttd;i=5008")
class OptionalModuleDataType(ns0.datatypes.Structure):
    moduleName: o6.String
    moduleType: o6.String
    isInstalled: o6.Boolean
    version: o6.String | None


@o6.datatype(nodeId="ns=ttd;i=3012", browseName="StatisticResultContentDataType", defaultEncodingId="ns=ttd;i=5011")
class StatisticResultContentDataType(ns0.datatypes.Structure):
    resultKey: o6.String
    itemCount: o6.UInt32
    meanValue: o6.Double
    standardDeviation: o6.Double
    coefficientOfVariation: o6.Double
    minValue: o6.Double
    maxValue: o6.Double
    confidenceInterval95: o6.Double


@o6.datatype(nodeId="ns=ttd;i=3015", browseName="StatisticResultContentWithUnitsDataType", defaultEncodingId="ns=ttd;i=5014")
class StatisticResultContentWithUnitsDataType(StatisticResultContentDataType):
    resultKey: o6.String
    itemCount: o6.UInt32
    meanValue: o6.Double
    standardDeviation: o6.Double
    coefficientOfVariation: o6.Double
    minValue: o6.Double
    maxValue: o6.Double
    confidenceInterval95: o6.Double
    unitItemCount: ns0.datatypes.EUInformation
    unitMeanValue: ns0.datatypes.EUInformation
    unitStandardDeviation: ns0.datatypes.EUInformation
    unitCoefficientOfVariation: ns0.datatypes.EUInformation
    unitMinValue: ns0.datatypes.EUInformation
    unitMaxValue: ns0.datatypes.EUInformation
    unitConfidenceInterval: ns0.datatypes.EUInformation


@o6.datatype(nodeId="ns=ttd;i=3018", browseName="RecipeDataType", defaultEncodingId="ns=ttd;i=5017")
class RecipeDataType(ns0.datatypes.Structure):
    recipeId: RecipeIdDataType
    recipeContent: o6.ByteString
    contentEncoding: o6.String


@o6.datatype(nodeId="ns=ttd;i=3022", browseName="TTDResultMetaDataType", defaultEncodingId="ns=ttd;i=5020")
class TTDResultMetaDataType(machinery_result.datatypes.ResultMetaDataType):
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
    sampleId: o6.String
    testerJobId: o6.String
    testerSampleResultId: o6.String
    productInstanceURI: o6.String
    canBeDeleted: o6.Boolean
    jobOrder: isa95_jobcontrol_v2.datatypes.ISA95JobOrderDataType


@o6.datatype(nodeId="ns=ttd;i=3028", browseName="TestNumDataType", defaultEncodingId="ns=ttd;i=5026")
class TestNumDataType(ns0.datatypes.Structure):
    testProcedureId: o6.String
    numberOfTests: o6.UInt32


@o6.datatype(nodeId="ns=ttd;i=3031", browseName="SampleInfoDataType", defaultEncodingId="ns=ttd;i=5029")
class SampleInfoDataType(ns0.datatypes.Structure):
    sampleId: o6.String
    nominalLinearDensity: o6.Double
    materialDensity: o6.Double | None
    materialType: o6.String | None
    positionOnCarrier: o6.String


@o6.datatype(nodeId="ns=ttd;i=3025", browseName="JobOrderDataType", defaultEncodingId="ns=ttd;i=5023")
class JobOrderDataType(ns0.datatypes.Structure):
    jobId: o6.String
    recipeId: RecipeIdDataType
    numberOfTests: list[TestNumDataType]
    sampleInfos: list[SampleInfoDataType]
    carrierTypeId: o6.String
    carrierId: o6.String
    additionalInfo: list[ns0.datatypes.KeyValuePair] | None
    scheduled: o6.Boolean


@o6.datatype(nodeId="ns=ttd;i=3034", browseName="TestProcedureIdDataType", defaultEncodingId="ns=ttd;i=5032")
class TestProcedureIdDataType(ns0.datatypes.Structure):
    testProcedureId: o6.String
    description: o6.String | None
    procedureReferences: list[o6.String] | None
    isProcedureLicensed: o6.Boolean | None


del Any, TYPE_CHECKING, uuid, o6, di, ia, isa95_jobcontrol_v2, machine_tool, machinery, machinery_jobs, machinery_result, ns0
