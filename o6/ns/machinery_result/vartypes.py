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
from . import datatypes as machinery_result_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.variabletype(
    nodeId="ns=machinery_result;i=2001",
    browseName="ns=machinery_result;ResultType",
    displayName="ResultType",
    description="Exposes the information of the ResultDataType in individual subvariables.",
    dataType=machinery_result_datypes.ResultDataType,
    value=machinery_result_datypes.ResultDataType(
        resultMetaData=machinery_result_datypes.ResultMetaDataType(
            resultId="",
            hasTransferableDataOnFile=None,
            isPartial=None,
            isSimulated=None,
            resultState=None,
            stepId=None,
            partId=None,
            externalRecipeId=None,
            internalRecipeId=None,
            productId=None,
            externalConfigurationId=None,
            internalConfigurationId=None,
            jobId=None,
            creationTime=None,
            processingTimes=None,
            resultUri=[],
            resultEvaluation=None,
            resultEvaluationCode=None,
            resultEvaluationDetails=None,
            fileFormat=[],
        ),
        resultContent=[],
    ),
)
class ResultType(ns0.vartypes.BaseDataVariableType):
    reducedResultContent: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=machinery_result;i=6011", browseName="ns=machinery_result;ReducedResultContent", valueRank=1, arrayDimensions=[0], accessLevel=3, userAccessLevel=1
        )
    )
    resultContent: ns0.vartypes.BaseDataVariableType | None = o6.reference(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=machinery_result;i=6010", browseName="ns=machinery_result;ResultContent", valueRank=1, arrayDimensions=[0]), "i=24136"
    )
    resultMetaData: ns0.vartypes.BaseDataVariableType


del Any, TYPE_CHECKING, uuid, o6, ns0, machinery_result_datypes
