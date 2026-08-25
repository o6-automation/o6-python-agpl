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
from . import datatypes as ijt_base_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.variabletype(
    nodeId="ns=ijt_base;i=2014",
    browseName="ns=ijt_base;JoiningSystemResultType",
    displayName="JoiningSystemResultType",
    description="The JoiningSystemResultType is a subtype of ResultType. It is used to expose the information of the ResultDataType in individual sub-variables.",
    dataType=machinery_result.datatypes.ResultDataType,
    value=machinery_result.datatypes.ResultDataType(
        resultMetaData=machinery_result.datatypes.ResultMetaDataType(
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
class JoiningSystemResultType(machinery_result.vartypes.ResultType):
    resultMetaData: ns0.vartypes.BaseDataVariableType


@o6.variabletype(
    nodeId="ns=ijt_base;i=2011",
    browseName="ns=ijt_base;JoiningDataVariableType",
    displayName="JoiningDataVariableType",
    description="The JoiningDataVariableType is a subtype of the BaseDataVariableType. It is to describe common semantic required for variables in the system. In this version of the specification, it provides information about physical quantity and Engineering Units.",
)
class JoiningDataVariableType(ns0.vartypes.BaseDataVariableType):
    engineeringUnits: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=ijt_base;i=6042",
            browseName="ns=ijt_base;EngineeringUnits",
            description="0:EngineeringUnits defines the engineering unit of the values.",
            dataType=ns0.datatypes.EUInformation,
            value=ns0.datatypes.EUInformation(namespaceUri="", unitId=-1, displayName=o6.LocalizedText()),
        )
    )
    physicalQuantity: ns0.vartypes.MultiStateDiscreteType | None


@o6.variabletype(
    nodeId="ns=ijt_base;i=2008",
    browseName="ns=ijt_base;JoiningSystemEventContentType",
    displayName="JoiningSystemEventContentType",
    description="The JoiningSystemEventContentType is a subtype of 0:BaseVariableType. It is used JoiningSystemEventType and JoiningSystemConditionType.",
)
class JoiningSystemEventContentType(ns0.vartypes.BaseDataVariableType):
    associatedEntities: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=ijt_base;i=6026",
            browseName="ns=ijt_base;AssociatedEntities",
            description="AssociatedEntities is a list of identifiers of various entities/objects available in the given system. Example: An event maybe associated to Asset, Result, Joint, Error, etc.",
            dataType=ijt_base_datypes.EntityDataType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    eventCode: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=ijt_base;i=6030",
            browseName="ns=ijt_base;EventCode",
            description="EventCode is a system specific event code associated to the given event.",
            dataType=o6.Int64,
            value=0,
        )
    )
    eventText: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=ijt_base;i=6029",
            browseName="ns=ijt_base;EventText",
            description="EventText is a human readable text related to the context of the event.",
            dataType=o6.LocalizedText,
            value=o6.LocalizedText(),
        )
    )
    joiningTechnology: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=ijt_base;i=6025",
            browseName="ns=ijt_base;JoiningTechnology",
            description="JoiningTechnology is a human readable text to identify the joining technology which has triggered the event. Examples: Tightening, Gluing, Riveting, Flow Drill Fastening, etc.",
            dataType=o6.LocalizedText,
            value=o6.LocalizedText(),
        )
    )
    reportedValues: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=ijt_base;i=6279",
            browseName="ns=ijt_base;ReportedValues",
            description="ReportedValues is a list of values associated with the given event payload. Example: If it is an over temperature event, then the ReportedValue can be the measured value along with the corresponding limits.",
            dataType=ijt_base_datypes.ReportedValueDataType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )


del Any, TYPE_CHECKING, uuid, o6, amb, di, ia, machinery, machinery_result, ns0, ijt_base_datypes
