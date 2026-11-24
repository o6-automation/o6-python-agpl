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

"""Generated OPC UA machinery_result namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.ns0 as ns0

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.enumtype(nodeId="ns=machinery_result;i=3002", browseName="ns=machinery_result;ResultEvaluationEnum", description="Indicates whether a result was in tolerance")
class ResultEvaluationEnum(ns0.datatypes.Enumeration):
    UNDEFINED = o6.enumfield(0, name="Undefined")
    OK = o6.enumfield(1, name="OK")
    NOT_OK = o6.enumfield(2, name="NotOK")
    NOT_DECIDABLE = o6.enumfield(3, name="NotDecidable")


@o6.datatype(
    nodeId="ns=machinery_result;i=3005",
    browseName="ns=machinery_result;BaseResultTransferOptionsDataType",
    description="Abstract type containing information which file should be provided.",
    isAbstract=True,
)
class BaseResultTransferOptionsDataType(ns0.datatypes.Structure):
    resultId: o6.String = o6.field(name="ResultId")


@o6.datatype(
    nodeId="ns=machinery_result;i=3004",
    browseName="ns=machinery_result;ResultTransferOptionsDataType",
    description="Contains information which file should be provided.",
    defaultEncodingId="ns=machinery_result;i=5001",
)
class ResultTransferOptionsDataType(BaseResultTransferOptionsDataType):
    resultId: o6.String = o6.field(name="ResultId")


@o6.datatype(
    nodeId="ns=machinery_result;i=3006",
    browseName="ns=machinery_result;ProcessingTimesDataType",
    description="Contains measured times that were generated during the execution of a recipe.",
    defaultEncodingId="ns=machinery_result;i=5003",
)
class ProcessingTimesDataType(ns0.datatypes.Structure):
    startTime: o6.DateTime = o6.field(name="StartTime")
    endTime: o6.DateTime = o6.field(name="EndTime")
    acquisitionDuration: o6.Double | None = o6.field(name="AcquisitionDuration")
    processingDuration: o6.Double | None = o6.field(name="ProcessingDuration")


@o6.datatype(
    nodeId="ns=machinery_result;i=3007",
    browseName="ns=machinery_result;ResultMetaDataType",
    description="Meta data of a result, describing the result.",
    defaultEncodingId="ns=machinery_result;i=5005",
)
class ResultMetaDataType(ns0.datatypes.Structure):
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
    processingTimes: ProcessingTimesDataType | None = o6.field(name="ProcessingTimes")
    resultUri: list[o6.String] | None = o6.field(name="ResultUri", arrayDimensions=[0])
    resultEvaluation: ResultEvaluationEnum | None = o6.field(name="ResultEvaluation")
    resultEvaluationCode: o6.Int64 | None = o6.field(name="ResultEvaluationCode")
    resultEvaluationDetails: o6.LocalizedText | None = o6.field(name="ResultEvaluationDetails")
    fileFormat: list[o6.String] | None = o6.field(name="FileFormat", arrayDimensions=[0])


@o6.datatype(
    nodeId="ns=machinery_result;i=3008",
    browseName="ns=machinery_result;ResultDataType",
    description="Contains fields that were created during the execution of a recipe.",
    defaultEncodingId="ns=machinery_result;i=5008",
)
class ResultDataType(ns0.datatypes.Structure):
    resultMetaData: ResultMetaDataType = o6.field(name="ResultMetaData")
    resultContent: list[Any] = o6.field(name="ResultContent", arrayDimensions=[0])


del Any, TYPE_CHECKING, uuid, o6, ns0
