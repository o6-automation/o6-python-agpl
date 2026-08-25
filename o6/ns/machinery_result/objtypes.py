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
from . import vartypes as machinery_result_vartypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(
    nodeId="ns=machinery_result;i=1002",
    browseName="ns=machinery_result;ResultReadyEventType",
    displayName="ResultReadyEventType",
    description="Provides information of a complete or partial result.",
    isAbstract=True,
)
class ResultReadyEventType(ns0.objtypes.BaseEventType):
    result: machinery_result_vartypes.ResultType


ns0.vartypes.PropertyType(
    nodeId="ns=machinery_result;i=6035",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machinery_result;i=7001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="GenerateOptions",
            dataType=machinery_result_datypes.BaseResultTransferOptionsDataType,
            valueRank=-1,
            description=o6.LocalizedText("Options how to generate the file, including the resultId of the result the file belongs to. "),
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machinery_result;i=6036",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machinery_result;i=7001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="FileNodeId", dataType=o6.NodeId, valueRank=-1, description=o6.LocalizedText("NodeId of the temporary file.")),
        ns0.datatypes.Argument(
            name="FileHandle",
            dataType=o6.UInt32,
            valueRank=-1,
            description=o6.LocalizedText("The FileHandle of the opened TransferFile.\nThe FileHandle can be used to access the TransferFile methods Read and Close.\n"),
        ),
        ns0.datatypes.Argument(
            name="CompletionStateMachine",
            dataType=o6.NodeId,
            valueRank=-1,
            description=o6.LocalizedText(
                "If the creation of the file is completed asynchronously, the parameter returns the NodeId of the corresponding FileTransferStateMachineType Object.\nIf the creation of the file is already completed, the parameter is null.\nIf a FileTransferStateMachineType object NodeId is returned, the Read Method of the file fails until the TransferState changed to ReadTransfer.\n"
            ),
        ),
    ],
)
o6.call(
    nodeId="ns=machinery_result;i=7001",
    browseName="GenerateFileForRead",
    inputArgs=o6.hasProperty(o6.ns["ns=machinery_result;i=6035"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machinery_result;i=6036"]),
)


@o6.objecttype(
    nodeId="ns=machinery_result;i=1003", browseName="ns=machinery_result;ResultTransferType", displayName="ResultTransferType", description="Transfers result data as a file."
)
class ResultTransferType(ns0.objtypes.TemporaryFileTransferType):
    generateFileForRead: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=machinery_result;i=7001"])


ns0.vartypes.PropertyType(
    nodeId="ns=machinery_result;i=6048",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machinery_result;i=7005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="ResultId", dataType=ns0.datatypes.TrimmedString, valueRank=-1, description=o6.LocalizedText("System-wide unique identifier for the result.")),
        ns0.datatypes.Argument(
            name="Timeout",
            dataType=o6.Int32,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the client can give a hint to the server how long it will need access to the result data.\nA value &gt; 0 indicates an estimated maximum time for processing the data in milliseconds. \nA value = 0 indicates that the client will not need anything besides the data returned by the method call.\nA value &lt; 0 indicates that the client cannot give an estimate.\nThe client cannot rely on the data being available during the indicated time period. The argument is merely a hint allowing the server to optimize its resource management."
            ),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machinery_result;i=6049",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machinery_result;i=7005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="ResultHandle",
            dataType=ns0.datatypes.Handle,
            valueRank=-1,
            description=o6.LocalizedText(
                "The server shall return to each client requesting result data a system-wide unique handle identifying the result set / client combination. This handle should be used by the client to indicate to the server that the result data is no longer needed, allowing the server to optimize its resource handling.\nIf the instance of ResultManagementType does not support the ReleaseResultHandle Method, the resultHandle should always be set to 0.\nIf the error is set to a value other than 0, the resultHandle may be set to 0."
            ),
        ),
        ns0.datatypes.Argument(
            name="Result",
            dataType=machinery_result_datypes.ResultDataType,
            valueRank=-1,
            description=o6.LocalizedText("The result including metadata. May be set to Null, if error is set to a value other than 0."),
        ),
        ns0.datatypes.Argument(
            name="Error",
            dataType=o6.Int32,
            valueRank=-1,
            description=o6.LocalizedText(
                "0 &#8211; OK\nValues &gt; 0 are reserved for errors defined by this and future standards.\nValues &lt; 0 shall be used for application-specific errors."
            ),
        ),
    ],
)
o6.call(
    nodeId="ns=machinery_result;i=7005",
    browseName="ns=machinery_result;GetResultById",
    description="The server shall return to each client requesting result data a system-wide unique handle identifying the result set / client combination. This handle should be used by the client to indicate to the server that the result data is no longer needed, allowing the server to optimize its resource handling.\nIf the instance of ResultManagementType does not support the ReleaseResultHandle Method, the resultHandle should always be set to 0.\nIf the error is set to a value other than 0, the resultHandle may be set to 0.",
    inputArgs=o6.hasProperty(o6.ns["ns=machinery_result;i=6048"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machinery_result;i=6049"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machinery_result;i=6050",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machinery_result;i=7006",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.Argument(
            name="Filter",
            dataType=ns0.datatypes.ContentFilter,
            valueRank=-1,
            description=o6.LocalizedText(
                "Filter used to filter for specific results based on the meta data of the results. Valid BrowsePaths used in the filter can be built from the fields of the ResultReadyEventType, the ResultType VariableType or the ResultDataType or corresponding subtypes."
            ),
        ),
        ns0.datatypes.Argument(
            name="OrderedBy",
            dataType=ns0.datatypes.RelativePath,
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText(
                "An array of BrowsePaths (as array of QualifiedName) identifying the ordering criteria for the results. If the array is null or empty, no ordering is executed.\nIf several BrowsePaths are provided, the first entry in the array is used as first ordering criteria, etc.\n"
            ),
        ),
        ns0.datatypes.Argument(
            name="MaxResults",
            dataType=o6.UInt32,
            valueRank=-1,
            description=o6.LocalizedText("Defines how many resultIds the Client wants to receive at most. If no maximum should be provided, it is set to 0."),
        ),
        ns0.datatypes.Argument(
            name="Timeout",
            dataType=o6.Int32,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the client can give a hint to the server how long it will need access to the result data.\nA value &gt; 0 indicates an estimated maximum time for processing the data in milliseconds. \nA value = 0 indicates that the client will not need anything besides the data returned by the method call.\nA value &lt; 0 indicates that the client cannot give an estimate.\nThe client cannot rely on the data being available during the indicated time period. The argument is merely a hint allowing the server to optimize its resource management."
            ),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machinery_result;i=6051",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machinery_result;i=7006",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="ResultHandle",
            dataType=ns0.datatypes.Handle,
            valueRank=-1,
            description=o6.LocalizedText(
                "The server shall return to each client requesting result data a system-wide unique handle identifying the result set / client combination. This handle has to be used by the client to release the result set.\nIf the instance of ResultManagementType does not support the ReleaseResultHandle Method, the resultHandle should always be set to 0.\nIf the error is set to a value other than 0, the resultHandle may be set to 0.\n"
            ),
        ),
        ns0.datatypes.Argument(
            name="ResultIdList",
            dataType=ns0.datatypes.TrimmedString,
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText("List of resultIds of results matching the Filter."),
        ),
        ns0.datatypes.Argument(
            name="Error",
            dataType=o6.Int32,
            valueRank=-1,
            description=o6.LocalizedText(
                "0 &#8211; OK\nValues &gt; 0 are reserved for errors defined by this and future standards.\nValues &lt; 0 shall be used for application-specific errors."
            ),
        ),
    ],
)
o6.call(
    nodeId="ns=machinery_result;i=7006",
    browseName="ns=machinery_result;GetResultIdListFiltered",
    inputArgs=o6.hasProperty(o6.ns["ns=machinery_result;i=6050"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machinery_result;i=6051"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machinery_result;i=6052",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machinery_result;i=7007",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ResultHandle",
            dataType=ns0.datatypes.Handle,
            valueRank=-1,
            description=o6.LocalizedText("Handle returned by GetResultById or GetResultIdListFiltered, identifying the result set/client combination."),
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machinery_result;i=6053",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machinery_result;i=7007",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="Error",
            dataType=o6.Int32,
            valueRank=-1,
            description=o6.LocalizedText(
                "0 &#8211; OK\nValues &gt; 0 are reserved for errors defined by this and future standards.\nValues &lt; 0 shall be used for application-specific errors."
            ),
        )
    ],
)
o6.call(
    nodeId="ns=machinery_result;i=7007",
    browseName="ns=machinery_result;ReleaseResultHandle",
    inputArgs=o6.hasProperty(o6.ns["ns=machinery_result;i=6052"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machinery_result;i=6053"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machinery_result;i=6054",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machinery_result;i=7008",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="Timeout",
            dataType=o6.Int32,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the client can give a hint to the server how long it will need access to the result data.\nA value &gt; 0 indicates an estimated maximum time for processing the data in milliseconds. \nA value = 0 indicates that the client will not need anything besides the data returned by the method call.\nA value &lt; 0 indicates that the client cannot give an estimate.\nThe client cannot rely on the data being available during the indicated time period. The argument is merely a hint allowing the server to optimize its resource management."
            ),
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machinery_result;i=6055",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machinery_result;i=7008",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="ResultHandle",
            dataType=ns0.datatypes.Handle,
            valueRank=-1,
            description=o6.LocalizedText(
                "The server shall return to each client requesting result data a system-wide unique handle identifying the result set / client combination. This handle should be used by the client to indicate to the server that the result data is no longer needed, allowing the server to optimize its resource handling.\nIf the instance of ResultManagementType does not support the ReleaseResultHandle Method, the resultHandle should always be set to 0.\nIf the error is set to a value other than 0, the resultHandle may be set to 0.\n"
            ),
        ),
        ns0.datatypes.Argument(name="Result", dataType=machinery_result_datypes.ResultDataType, valueRank=-1, description=o6.LocalizedText("The result including metadata.")),
        ns0.datatypes.Argument(
            name="Error",
            dataType=o6.Int32,
            valueRank=-1,
            description=o6.LocalizedText(
                "0 &#8211; OK\nValues &gt; 0 are reserved for errors defined by this and future standards.\nValues &lt; 0 shall be used for application-specific errors.\n"
            ),
        ),
    ],
)
o6.call(
    nodeId="ns=machinery_result;i=7008",
    browseName="ns=machinery_result;GetLatestResult",
    inputArgs=o6.hasProperty(o6.ns["ns=machinery_result;i=6054"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machinery_result;i=6055"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machinery_result;i=6089",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machinery_result;i=7009",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ResultIds", dataType=ns0.datatypes.TrimmedString, valueRank=1, arrayDimensions=[0], description=o6.LocalizedText("List of result identifiers to be acknowledged.")
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machinery_result;i=6090",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machinery_result;i=7009",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="ErrorPerResultId",
            dataType=o6.Int32,
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText(
                "Shall be null or empty if error equals 0. Shall have the same length as resultIds if error is not equal 0. Indicates for each resultId in resultIds, if the acknowledge was successful.\nPer entry:\n0 &#8211; OK\nValues &gt; 0 are reserved for errors defined by this and future standards.\nValues &lt; 0 shall be used for application-specific errors.\n",
                "",
            ),
        ),
        ns0.datatypes.Argument(
            name="Error",
            dataType=o6.Int32,
            valueRank=-1,
            description=o6.LocalizedText(
                "0 &#8211; OK\nValues &gt; 0 are reserved for errors defined by this and future standards.\nValues &lt; 0 shall be used for application-specific errors.\nShall be not equal 0 if any resultId of resultIds was not successfully acknowledged. Shall be 0 if all resultIds where acknowledged successful."
            ),
        ),
    ],
)
o6.call(
    nodeId="ns=machinery_result;i=7009",
    browseName="ns=machinery_result;AcknowledgeResults",
    inputArgs=o6.hasProperty(o6.ns["ns=machinery_result;i=6089"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machinery_result;i=6090"]),
)


@o6.objecttype(
    nodeId="ns=machinery_result;i=1004",
    browseName="ns=machinery_result;ResultManagementType",
    displayName="ResultManagementType",
    description="Provides mechanism to access results generated by the underlying system.",
)
class ResultManagementType(ns0.objtypes.BaseObjectType):
    acknowledgeResults: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=machinery_result;i=7009"])
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machinery_result;i=6037",
            browseName="DefaultInstanceBrowseName",
            description="The default BrowseName for instances of the type.",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("machinery_result:ResultManagement"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    getLatestResult: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=machinery_result;i=7008"])
    getResultById: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=machinery_result;i=7005"])
    getResultIdListFiltered: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=machinery_result;i=7006"])
    releaseResultHandle: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=machinery_result;i=7007"])
    resultTransfer: ResultTransferType | None
    results: ns0.objtypes.FolderType | None


o6.reference(ResultManagementType, "i=41", ResultReadyEventType)


del Any, TYPE_CHECKING, uuid, o6, ns0, machinery_result_datypes, machinery_result_vartypes
