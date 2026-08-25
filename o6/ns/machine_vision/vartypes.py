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

"""Generated OPC UA machine_vision namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.ns0 as ns0
from . import reftypes as machine_vision_reftypes
from . import datatypes as machine_vision_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.variabletype(
    nodeId="ns=machine_vision;i=2002",
    browseName="ns=machine_vision;ResultType",
    displayName="ResultType",
    dataType=machine_vision_datypes.ResultDataType,
    value=machine_vision_datypes.ResultDataType(
        resultId=machine_vision_datypes.ResultIdDataType(id=""),
        hasTransferableDataOnFile=None,
        isPartial=False,
        isSimulated=None,
        resultState=0,
        measId=None,
        partId=None,
        externalRecipeId=None,
        internalRecipeId=machine_vision_datypes.RecipeIdInternalDataType(id="", version=None, hash=None, hashAlgorithm=None, description=None),
        productId=None,
        externalConfigurationId=None,
        internalConfigurationId=machine_vision_datypes.ConfigurationIdDataType(id="", version=None, hash=None, hashAlgorithm=None, description=None),
        jobId=machine_vision_datypes.JobIdDataType(id=""),
        creationTime=o6.DateTime("1900-01-01T00:00:00Z"),
        processingTimes=None,
        resultContent=[],
    ),
)
class ResultType(ns0.vartypes.BaseDataVariableType):
    creationTime: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=machine_vision;i=6331", browseName="ns=machine_vision;CreationTime", dataType=ns0.datatypes.UtcTime, accessLevel=3, userAccessLevel=1
        )
    )
    externalConfigurationId: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=machine_vision;i=6328",
            browseName="ns=machine_vision;ExternalConfigurationId",
            dataType=machine_vision_datypes.ConfigurationIdDataType,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    externalRecipeId: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=machine_vision;i=6095",
            browseName="ns=machine_vision;ExternalRecipeId",
            dataType=machine_vision_datypes.RecipeIdExternalDataType,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    hasTransferableDataOnFile: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=machine_vision;i=6047", browseName="ns=machine_vision;HasTransferableDataOnFile", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
        )
    )
    internalConfigurationId: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=machine_vision;i=6329",
            browseName="ns=machine_vision;InternalConfigurationId",
            dataType=machine_vision_datypes.ConfigurationIdDataType,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    internalRecipeId: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=machine_vision;i=6284",
            browseName="ns=machine_vision;InternalRecipeId",
            dataType=machine_vision_datypes.RecipeIdInternalDataType,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    isPartial: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_vision;i=6052", browseName="ns=machine_vision;IsPartial", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
    )
    isSimulated: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_vision;i=6053", browseName="ns=machine_vision;IsSimulated", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
    )
    jobId: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=machine_vision;i=6330", browseName="ns=machine_vision;JobId", dataType=machine_vision_datypes.JobIdDataType, accessLevel=3, userAccessLevel=1
        )
    )
    measId: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=machine_vision;i=6055", browseName="ns=machine_vision;MeasId", dataType=machine_vision_datypes.MeasIdDataType, accessLevel=3, userAccessLevel=1
        )
    )
    partId: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=machine_vision;i=6094", browseName="ns=machine_vision;PartId", dataType=machine_vision_datypes.PartIdDataType, accessLevel=3, userAccessLevel=1
        )
    )
    processingTimes: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=machine_vision;i=6332",
            browseName="ns=machine_vision;ProcessingTimes",
            dataType=machine_vision_datypes.ProcessingTimesDataType,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    productId: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=machine_vision;i=6327", browseName="ns=machine_vision;ProductId", dataType=machine_vision_datypes.ProductIdDataType, accessLevel=3, userAccessLevel=1
        )
    )
    resultContent: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=machine_vision;i=6333", browseName="ns=machine_vision;ResultContent", valueRank=1, arrayDimensions=[1], accessLevel=3, userAccessLevel=1
        )
    )
    resultId: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=machine_vision;i=6046", browseName="ns=machine_vision;ResultId", dataType=machine_vision_datypes.ResultIdDataType, accessLevel=3, userAccessLevel=1
        )
    )
    resultState: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=machine_vision;i=6054", browseName="ns=machine_vision;ResultState", dataType=machine_vision_datypes.ResultStateDataType, accessLevel=3, userAccessLevel=1
        )
    )


del Any, TYPE_CHECKING, uuid, o6, ns0, machine_vision_reftypes, machine_vision_datypes
