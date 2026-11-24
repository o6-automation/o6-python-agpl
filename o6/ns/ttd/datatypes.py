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


@o6.datatype(nodeId="ns=ttd;i=3003", browseName="ns=ttd;RecipeIdDataType", defaultEncodingId="ns=ttd;i=5002")
class RecipeIdDataType(ns0.datatypes.Structure):
    name: o6.String | None = o6.field(name="Name")
    id: o6.String = o6.field(name="Id")
    type: o6.String | None = o6.field(name="Type")
    description: o6.String | None = o6.field(name="Description")
    comment: o6.String | None = o6.field(name="Comment")
    modifiedDate: o6.DateTime | None = o6.field(name="ModifiedDate")
    version: o6.String | None = o6.field(name="Version")
    validated: o6.Boolean | None = o6.field(name="Validated")


@o6.datatype(nodeId="ns=ttd;i=3006", browseName="ns=ttd;ExchangeablePartDataType", defaultEncodingId="ns=ttd;i=5005")
class ExchangeablePartDataType(ns0.datatypes.Structure):
    partType: o6.String = o6.field(name="PartType")
    mounted: o6.Boolean = o6.field(name="Mounted")
    traceable: o6.Boolean | None = o6.field(name="Traceable")
    partId: o6.String | None = o6.field(name="PartId")
    machineReadable: o6.Boolean | None = o6.field(name="MachineReadable")
    lastCalibrationDate: o6.DateTime | None = o6.field(name="LastCalibrationDate")


@o6.datatype(nodeId="ns=ttd;i=3009", browseName="ns=ttd;OptionalModuleDataType", defaultEncodingId="ns=ttd;i=5008")
class OptionalModuleDataType(ns0.datatypes.Structure):
    moduleName: o6.String = o6.field(name="ModuleName")
    moduleType: o6.String = o6.field(name="ModuleType")
    isInstalled: o6.Boolean = o6.field(name="IsInstalled")
    version: o6.String | None = o6.field(name="Version")


@o6.datatype(nodeId="ns=ttd;i=3012", browseName="ns=ttd;StatisticResultContentDataType", defaultEncodingId="ns=ttd;i=5011")
class StatisticResultContentDataType(ns0.datatypes.Structure):
    resultKey: o6.String = o6.field(name="ResultKey")
    itemCount: o6.UInt32 = o6.field(name="ItemCount")
    meanValue: o6.Double = o6.field(name="MeanValue")
    standardDeviation: o6.Double = o6.field(name="StandardDeviation")
    coefficientOfVariation: o6.Double = o6.field(name="CoefficientOfVariation")
    minValue: o6.Double = o6.field(name="MinValue")
    maxValue: o6.Double = o6.field(name="MaxValue")
    confidenceInterval95: o6.Double = o6.field(name="ConfidenceInterval95")


@o6.datatype(nodeId="ns=ttd;i=3015", browseName="ns=ttd;StatisticResultContentWithUnitsDataType", defaultEncodingId="ns=ttd;i=5014")
class StatisticResultContentWithUnitsDataType(StatisticResultContentDataType):
    resultKey: o6.String = o6.field(name="ResultKey")
    itemCount: o6.UInt32 = o6.field(name="ItemCount")
    meanValue: o6.Double = o6.field(name="MeanValue")
    standardDeviation: o6.Double = o6.field(name="StandardDeviation")
    coefficientOfVariation: o6.Double = o6.field(name="CoefficientOfVariation")
    minValue: o6.Double = o6.field(name="MinValue")
    maxValue: o6.Double = o6.field(name="MaxValue")
    confidenceInterval95: o6.Double = o6.field(name="ConfidenceInterval95")
    unitItemCount: ns0.datatypes.EUInformation = o6.field(name="UnitItemCount")
    unitMeanValue: ns0.datatypes.EUInformation = o6.field(name="UnitMeanValue")
    unitStandardDeviation: ns0.datatypes.EUInformation = o6.field(name="UnitStandardDeviation")
    unitCoefficientOfVariation: ns0.datatypes.EUInformation = o6.field(name="UnitCoefficientOfVariation")
    unitMinValue: ns0.datatypes.EUInformation = o6.field(name="UnitMinValue")
    unitMaxValue: ns0.datatypes.EUInformation = o6.field(name="UnitMaxValue")
    unitConfidenceInterval: ns0.datatypes.EUInformation = o6.field(name="UnitConfidenceInterval")


@o6.datatype(nodeId="ns=ttd;i=3018", browseName="ns=ttd;RecipeDataType", defaultEncodingId="ns=ttd;i=5017")
class RecipeDataType(ns0.datatypes.Structure):
    recipeId: RecipeIdDataType = o6.field(name="RecipeId")
    recipeContent: o6.ByteString = o6.field(name="RecipeContent")
    contentEncoding: o6.String = o6.field(name="ContentEncoding")


@o6.datatype(nodeId="ns=ttd;i=3022", browseName="ns=ttd;TTDResultMetaDataType", defaultEncodingId="ns=ttd;i=5020")
class TTDResultMetaDataType(machinery_result.datatypes.ResultMetaDataType):
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
    sampleId: o6.String = o6.field(name="SampleId")
    testerJobId: o6.String = o6.field(name="TesterJobId")
    testerSampleResultId: o6.String = o6.field(name="TesterSampleResultId")
    productInstanceURI: o6.String = o6.field(name="ProductInstanceURI")
    canBeDeleted: o6.Boolean = o6.field(name="CanBeDeleted")
    jobOrder: isa95_jobcontrol_v2.datatypes.ISA95JobOrderDataType = o6.field(name="JobOrder")


@o6.datatype(nodeId="ns=ttd;i=3028", browseName="ns=ttd;TestNumDataType", defaultEncodingId="ns=ttd;i=5026")
class TestNumDataType(ns0.datatypes.Structure):
    testProcedureId: o6.String = o6.field(name="TestProcedureId")
    numberOfTests: o6.UInt32 = o6.field(name="NumberOfTests")


@o6.datatype(nodeId="ns=ttd;i=3031", browseName="ns=ttd;SampleInfoDataType", defaultEncodingId="ns=ttd;i=5029")
class SampleInfoDataType(ns0.datatypes.Structure):
    sampleId: o6.String = o6.field(name="SampleId")
    nominalLinearDensity: o6.Double = o6.field(name="NominalLinearDensity")
    materialDensity: o6.Double | None = o6.field(name="MaterialDensity")
    materialType: o6.String | None = o6.field(name="MaterialType")
    positionOnCarrier: o6.String = o6.field(name="PositionOnCarrier")


@o6.datatype(nodeId="ns=ttd;i=3025", browseName="ns=ttd;JobOrderDataType", defaultEncodingId="ns=ttd;i=5023")
class JobOrderDataType(ns0.datatypes.Structure):
    jobId: o6.String = o6.field(name="JobId")
    recipeId: RecipeIdDataType = o6.field(name="RecipeId")
    numberOfTests: list[TestNumDataType] = o6.field(name="NumberOfTests", arrayDimensions=[0])
    sampleInfos: list[SampleInfoDataType] = o6.field(name="SampleInfos", arrayDimensions=[0])
    carrierTypeId: o6.String = o6.field(name="CarrierTypeId")
    carrierId: o6.String = o6.field(name="CarrierId")
    additionalInfo: list[ns0.datatypes.KeyValuePair] | None = o6.field(name="AdditionalInfo", arrayDimensions=[0])
    scheduled: o6.Boolean = o6.field(name="Scheduled")


@o6.datatype(nodeId="ns=ttd;i=3034", browseName="ns=ttd;TestProcedureIdDataType", defaultEncodingId="ns=ttd;i=5032")
class TestProcedureIdDataType(ns0.datatypes.Structure):
    testProcedureId: o6.String = o6.field(name="TestProcedureId")
    description: o6.String | None = o6.field(name="Description")
    procedureReferences: list[o6.String] | None = o6.field(name="ProcedureReferences", arrayDimensions=[0])
    isProcedureLicensed: o6.Boolean | None = o6.field(name="IsProcedureLicensed")


del Any, TYPE_CHECKING, uuid, o6, di, ia, isa95_jobcontrol_v2, machine_tool, machinery, machinery_jobs, machinery_result, ns0
