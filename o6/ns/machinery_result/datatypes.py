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


@o6.enumtype(nodeId="ns=machinery_result;i=3002", browseName="ResultEvaluationEnum", description="Indicates whether a result was in tolerance")
class ResultEvaluationEnum(ns0.datatypes.Enumeration):
    UNDEFINED = o6.enumfield(0, name="Undefined")
    OK = o6.enumfield(1, name="OK")
    NOT_OK = o6.enumfield(2, name="NotOK")
    NOT_DECIDABLE = o6.enumfield(3, name="NotDecidable")


@o6.datatype(
    nodeId="ns=machinery_result;i=3005",
    browseName="BaseResultTransferOptionsDataType",
    description="Abstract type containing information which file should be provided.",
    isAbstract=True,
)
class BaseResultTransferOptionsDataType(ns0.datatypes.Structure):
    resultId: o6.String


@o6.datatype(
    nodeId="ns=machinery_result;i=3004",
    browseName="ResultTransferOptionsDataType",
    description="Contains information which file should be provided.",
    defaultEncodingId="ns=machinery_result;i=5001",
)
class ResultTransferOptionsDataType(BaseResultTransferOptionsDataType):
    resultId: o6.String


@o6.datatype(
    nodeId="ns=machinery_result;i=3006",
    browseName="ProcessingTimesDataType",
    description="Contains measured times that were generated during the execution of a recipe.",
    defaultEncodingId="ns=machinery_result;i=5003",
)
class ProcessingTimesDataType(ns0.datatypes.Structure):
    startTime: o6.DateTime
    endTime: o6.DateTime
    acquisitionDuration: o6.Double | None
    processingDuration: o6.Double | None


@o6.datatype(
    nodeId="ns=machinery_result;i=3007",
    browseName="ResultMetaDataType",
    description="Meta data of a result, describing the result.",
    defaultEncodingId="ns=machinery_result;i=5005",
)
class ResultMetaDataType(ns0.datatypes.Structure):
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
    processingTimes: ProcessingTimesDataType | None
    resultUri: list[o6.String] | None = o6.field(arrayDimensions=[0])
    resultEvaluation: ResultEvaluationEnum | None
    resultEvaluationCode: o6.Int64 | None
    resultEvaluationDetails: o6.LocalizedText | None
    fileFormat: list[o6.String] | None = o6.field(arrayDimensions=[0])


@o6.datatype(
    nodeId="ns=machinery_result;i=3008",
    browseName="ResultDataType",
    description="Contains fields that were created during the execution of a recipe.",
    defaultEncodingId="ns=machinery_result;i=5008",
)
class ResultDataType(ns0.datatypes.Structure):
    resultMetaData: ResultMetaDataType
    resultContent: list[Any] = o6.field(arrayDimensions=[0])


del Any, TYPE_CHECKING, uuid, o6, ns0
