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
from . import objtypes as machinery_result_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.objtypes.DataTypeEncodingType(nodeId="ns=machinery_result;i=5001", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=machinery_result;i=5002", browseName="Default XML")
o6.hasEncoding(machinery_result_datypes.ResultTransferOptionsDataType, o6.ns["ns=machinery_result;i=5002"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=machinery_result;i=5003", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=machinery_result;i=5004", browseName="Default XML")
o6.hasEncoding(machinery_result_datypes.ProcessingTimesDataType, o6.ns["ns=machinery_result;i=5004"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=machinery_result;i=5005", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=machinery_result;i=5006", browseName="Default XML")
o6.hasEncoding(machinery_result_datypes.ResultMetaDataType, o6.ns["ns=machinery_result;i=5006"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=machinery_result;i=5008", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=machinery_result;i=5009", browseName="Default XML")
o6.hasEncoding(machinery_result_datypes.ResultDataType, o6.ns["ns=machinery_result;i=5009"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=machinery_result;i=5012", browseName="Default JSON")
o6.hasEncoding(machinery_result_datypes.ResultTransferOptionsDataType, o6.ns["ns=machinery_result;i=5012"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=machinery_result;i=5013", browseName="Default JSON")
o6.hasEncoding(machinery_result_datypes.ProcessingTimesDataType, o6.ns["ns=machinery_result;i=5013"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=machinery_result;i=5014", browseName="Default JSON")
o6.hasEncoding(machinery_result_datypes.ResultDataType, o6.ns["ns=machinery_result;i=5014"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=machinery_result;i=5015", browseName="Default JSON")
o6.hasEncoding(machinery_result_datypes.ResultMetaDataType, o6.ns["ns=machinery_result;i=5015"])
ns0.vartypes.PropertyType(
    nodeId="ns=machinery_result;i=6001",
    browseName="EnumValues",
    parent="ns=machinery_result;i=3002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.EnumValueType(
            value=0, displayName=o6.LocalizedText("Undefined"), description=o6.LocalizedText("The evaluation of the result is unknown, for example because it failed")
        ),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("OK"), description=o6.LocalizedText("The result is in tolerance")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("NotOK"), description=o6.LocalizedText("The result is out of tolerance")),
        ns0.datatypes.EnumValueType(
            value=3, displayName=o6.LocalizedText("NotDecidable"), description=o6.LocalizedText("The decision is not possible due to measurement uncertainty.")
        ),
    ],
)
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashMachinerySlashResultSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=machinery_result;i=5007",
    browseName="ns=machinery_result;http://opcfoundation.org/UA/Machinery/Result/",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=machinery_result;i=6002", browseName="IsNamespaceSubset", dataType=o6.Boolean)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=machinery_result;i=6003", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2025-07-01T00:00:00Z"))
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=machinery_result;i=6004", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/Machinery/Result/")
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_result;i=6005", browseName="NamespaceVersion", dataType=o6.String, value="1.01.0")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machinery_result;i=6006",
                browseName="StaticNodeIdTypes",
                dataType=ns0.datatypes.IdType,
                valueRank=1,
                arrayDimensions=[1],
                value=[ns0.datatypes.IdType.NUMERIC],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machinery_result;i=6007", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_result;i=6008", browseName="StaticStringNodeIdPattern", dataType=o6.String)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=machinery_result;i=6009",
    browseName="ns=machinery_result;ResultMetaData",
    modellingRule="Mandatory",
    references=[
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machinery_result;i=6012",
                browseName="ns=machinery_result;ResultId",
                description="System-wide unique identifier, which is assigned by the system. This ID can be used for fetching exactly this result using the method GetResultById and it is identical to the ResultId of the ResultReadyEventType.\nIf the system does not manage resultIds, it should always be set to “NA”.",
                dataType=ns0.datatypes.TrimmedString,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "i=24136",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machinery_result;i=6013",
                browseName="ns=machinery_result;HasTransferableDataOnFile",
                description="Indicates that additional data for this result can be retrieved by temporary file transfer.\nIf not provided, it is assumed that no file is available.",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "i=24136",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machinery_result;i=6014",
                browseName="ns=machinery_result;IsPartial",
                description="Indicates whether the result is the partial result of a total result. When not all samples are finished yet the result is 'partial'.\nIf not provided, it is assumed to be a total result.",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "i=24136",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machinery_result;i=6015",
                browseName="ns=machinery_result;IsSimulated",
                description="Indicates whether the result was created in simulation mode.\nSimulation mode implies that the result is only generated for testing purposes and not based on real production data.\nIf not provided, it is assumed to not be simulated.",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "i=24136",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machinery_result;i=6016",
                browseName="ns=machinery_result;ResultState",
                description="ResultState provides information about the current state of the process or measurement creating a result.\nApplications may use negative values for application-specific states. All other values shall only be used as defined in the following:\n0 – Undefined initial value\n1 – Completed: Processing was carried out completely\n2 – Processing: Processing has not been finished yet\n3 – Aborted: Processing was stopped at some point before completion\n4 – Failed: Processing failed in some way.",
                dataType=o6.Int32,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "i=24136",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machinery_result;i=6017",
                browseName="ns=machinery_result;StepId",
                description="Identifies the step which produced the result.\nAlthough the system-wide unique JobId would be sufficient to identify the job which the result belongs to, this makes for easier filtering without keeping track of JobIds.\nThis specification does not define how the stepId is transmitted to the system. Typically, it is provided by the client when starting an execution.",
                dataType=ns0.datatypes.TrimmedString,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "i=24136",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machinery_result;i=6018",
                browseName="ns=machinery_result;PartId",
                description="Identifies the part used to produce the result.\nAlthough the system-wide unique JobId would be sufficient to identify the job which the result belongs to, this makes for easier filtering without keeping track of JobIds.\nThis specification does not define how the partId is transmitted to the system. Typically, it is provided by the client when starting the job.",
                dataType=ns0.datatypes.TrimmedString,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "i=24136",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machinery_result;i=6019",
                browseName="ns=machinery_result;ExternalRecipeId",
                description="External ID of the recipe in use which produced the result. The External ID is managed by the environment.\nThis specification does not define how the externalRecipeId is transmitted to the system. Typically, it is provided by the client.",
                dataType=ns0.datatypes.TrimmedString,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "i=24136",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machinery_result;i=6020",
                browseName="ns=machinery_result;InternalRecipeId",
                description="Internal ID of the recipe in use which produced the result. This ID is system-wide unique and it is assigned by the system.",
                dataType=ns0.datatypes.TrimmedString,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "i=24136",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machinery_result;i=6021",
                browseName="ns=machinery_result;ProductId",
                dataType=ns0.datatypes.TrimmedString,
                value="Identifies the product used to produce the result.\nThis specification does not define how the externalRecipeId is transmitted to the system. Typically, it is provided by the client.\n",
                accessLevel=3,
                userAccessLevel=1,
            ),
            "i=24136",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machinery_result;i=6022",
                browseName="ns=machinery_result;ExternalConfigurationId",
                dataType=ns0.datatypes.TrimmedString,
                value="External ID of the Configuration in use while the result was produced.\nIt is managed by the Environment.\nThis specification does not define how the externalConfigurationId is transmitted to the system. Typically, it is provided by the client.\n",
                accessLevel=3,
                userAccessLevel=1,
            ),
            "i=24136",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machinery_result;i=6023",
                browseName="ns=machinery_result;InternalConfigurationId",
                description="Internal ID of the Configuration in use while the result was produced. This ID is system-wide unique and it is assigned by the system.",
                dataType=ns0.datatypes.TrimmedString,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "i=24136",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machinery_result;i=6024",
                browseName="ns=machinery_result;JobId",
                description="Identifies the job which produced the result.\nThis ID is system-wide unique and it is assigned by the system.",
                dataType=ns0.datatypes.TrimmedString,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "i=24136",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machinery_result;i=6025",
                browseName="ns=machinery_result;CreationTime",
                description="CreationTime indicates the time when the result was created. Creation time on the measurement system (not the receive time of the server).\nIt is recommended to always provide the creationTime.",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "i=24136",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machinery_result;i=6026",
                browseName="ns=machinery_result;ProcessingTimes",
                description="Collection of different processing times that were needed to create the result.",
                dataType=machinery_result_datypes.ProcessingTimesDataType,
                value=machinery_result_datypes.ProcessingTimesDataType(
                    startTime=o6.DateTime("1900-01-01T00:00:00Z"), endTime=o6.DateTime("1900-01-01T00:00:00Z"), acquisitionDuration=None, processingDuration=None
                ),
                accessLevel=3,
                userAccessLevel=1,
            ),
            "i=24136",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machinery_result;i=6027",
                browseName="ns=machinery_result;ResultUri",
                description="Path to the actual measured result, managed external to the server.",
                dataType=ns0.datatypes.UriString,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            ),
            "i=24136",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machinery_result;i=6028",
                browseName="ns=machinery_result;ResultEvaluation",
                description="The ResultEvaluation indicates whether the result was in tolerance.",
                dataType=machinery_result_datypes.ResultEvaluationEnum,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "i=24136",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machinery_result;i=6029",
                browseName="ns=machinery_result;ResultEvaluationDetails",
                description="The optional EvaluationDetails provides high level status information in a user-friendly text. This can be left empty for successful operations.",
                dataType=o6.LocalizedText,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "i=24136",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machinery_result;i=6030",
                browseName="ns=machinery_result;ResultEvaluationCode",
                description="Vendor-specific code describing more details on resultEvaluation.",
                dataType=o6.Int64,
                value=0,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "i=24136",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machinery_result;i=6031",
                browseName="ns=machinery_result;FileFormat",
                description="The format in which the measurement results are available (e.g. QDAS, CSV, …) using the ResultTransfer Object. If multiple file formats are provided, the GenerateFileForRead of ResultTransfer should contain corresponding transferOptions, to select the file format. This specification does not define those transferOptions.",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            ),
            "i=24136",
        ),
    ],
    dataType=machinery_result_datypes.ResultMetaDataType,
)
o6.reference(machinery_result_vartypes.ResultType, ns0.reftypes.HasStructuredComponent, o6.ns["ns=machinery_result;i=6009"])
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=machinery_result;i=6046",
    browseName="ns=machinery_result;ResultMetaData",
    references=[
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machinery_result;i=6047",
                browseName="ns=machinery_result;ResultId",
                description="System-wide unique identifier, which is assigned by the system. This ID can be used for fetching exactly this result using the method GetResultById and it is identical to the ResultId of the ResultReadyEventType.\nIf the system does not manage resultIds, it should always be set to “NA”.",
                dataType=ns0.datatypes.TrimmedString,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "i=24136",
        )
    ],
    dataType=machinery_result_datypes.ResultMetaDataType,
)
machinery_result_vartypes.ResultType(
    nodeId="ns=machinery_result;i=6045",
    browseName="ns=machinery_result;<ResultVariable>",
    modellingRule="OptionalPlaceholder",
    references=[o6.reference(o6.ns["ns=machinery_result;i=6046"], "i=24136")],
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
    accessLevel=3,
    userAccessLevel=1,
)
ns0.objtypes.FolderType(
    nodeId="ns=machinery_result;i=5011", browseName="ns=machinery_result;Results", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=machinery_result;i=6045"])]
)
o6.reference(machinery_result_objtypes.ResultManagementType, ns0.reftypes.HasComponent, o6.ns["ns=machinery_result;i=5011"])
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=machinery_result;i=6033",
    browseName="ns=machinery_result;ResultMetaData",
    references=[
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machinery_result;i=6034",
                browseName="ns=machinery_result;ResultId",
                description="System-wide unique identifier, which is assigned by the system. This ID can be used for fetching exactly this result using the method GetResultById and it is identical to the ResultId of the ResultReadyEventType.\nIf the system does not manage resultIds, it should always be set to “NA”.",
                dataType=ns0.datatypes.TrimmedString,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "i=24136",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machinery_result;i=6056",
                browseName="ns=machinery_result;CreationTime",
                description="CreationTime indicates the time when the result was created. Creation time on the measurement system (not the receive time of the server).\nIt is recommended to always provide the creationTime.",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "i=24136",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machinery_result;i=6057",
                browseName="ns=machinery_result;ExternalConfigurationId",
                dataType=ns0.datatypes.TrimmedString,
                value="External ID of the Configuration in use while the result was produced.\nIt is managed by the Environment.\nThis specification does not define how the externalConfigurationId is transmitted to the system. Typically, it is provided by the client.\n",
                accessLevel=3,
                userAccessLevel=1,
            ),
            "i=24136",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machinery_result;i=6058",
                browseName="ns=machinery_result;ExternalRecipeId",
                description="External ID of the recipe in use which produced the result. The External ID is managed by the environment.\nThis specification does not define how the externalRecipeId is transmitted to the system. Typically, it is provided by the client.",
                dataType=ns0.datatypes.TrimmedString,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "i=24136",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machinery_result;i=6059",
                browseName="ns=machinery_result;FileFormat",
                description="The format in which the measurement results are available (e.g. QDAS, CSV, …) using the ResultTransfer Object. If multiple file formats are provided, the GenerateFileForRead of ResultTransfer should contain corresponding transferOptions, to select the file format. This specification does not define those transferOptions.",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            ),
            "i=24136",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machinery_result;i=6060",
                browseName="ns=machinery_result;HasTransferableDataOnFile",
                description="Indicates that additional data for this result can be retrieved by temporary file transfer.\nIf not provided, it is assumed that no file is available.",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "i=24136",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machinery_result;i=6061",
                browseName="ns=machinery_result;InternalConfigurationId",
                description="Internal ID of the Configuration in use while the result was produced. This ID is system-wide unique and it is assigned by the system.",
                dataType=ns0.datatypes.TrimmedString,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "i=24136",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machinery_result;i=6062",
                browseName="ns=machinery_result;InternalRecipeId",
                description="Internal ID of the recipe in use which produced the result. This ID is system-wide unique and it is assigned by the system.",
                dataType=ns0.datatypes.TrimmedString,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "i=24136",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machinery_result;i=6063",
                browseName="ns=machinery_result;IsPartial",
                description="Indicates whether the result is the partial result of a total result. When not all samples are finished yet the result is 'partial'.\nIf not provided, it is assumed to be a total result.",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "i=24136",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machinery_result;i=6064",
                browseName="ns=machinery_result;IsSimulated",
                description="Indicates whether the result was created in simulation mode.\nSimulation mode implies that the result is only generated for testing purposes and not based on real production data.\nIf not provided, it is assumed to not be simulated.",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "i=24136",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machinery_result;i=6065",
                browseName="ns=machinery_result;JobId",
                description="Identifies the job which produced the result.\nThis ID is system-wide unique and it is assigned by the system.",
                dataType=ns0.datatypes.TrimmedString,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "i=24136",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machinery_result;i=6066",
                browseName="ns=machinery_result;PartId",
                description="Identifies the part used to produce the result.\nAlthough the system-wide unique JobId would be sufficient to identify the job which the result belongs to, this makes for easier filtering without keeping track of JobIds.\nThis specification does not define how the partId is transmitted to the system. Typically, it is provided by the client when starting the job.",
                dataType=ns0.datatypes.TrimmedString,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "i=24136",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machinery_result;i=6067",
                browseName="ns=machinery_result;ProcessingTimes",
                description="Collection of different processing times that were needed to create the result.",
                dataType=machinery_result_datypes.ProcessingTimesDataType,
                value=machinery_result_datypes.ProcessingTimesDataType(
                    startTime=o6.DateTime("1900-01-01T00:00:00Z"), endTime=o6.DateTime("1900-01-01T00:00:00Z"), acquisitionDuration=None, processingDuration=None
                ),
                accessLevel=3,
                userAccessLevel=1,
            ),
            "i=24136",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machinery_result;i=6068",
                browseName="ns=machinery_result;ProductId",
                dataType=ns0.datatypes.TrimmedString,
                value="Identifies the product used to produce the result.\nThis specification does not define how the externalRecipeId is transmitted to the system. Typically, it is provided by the client.\n",
                accessLevel=3,
                userAccessLevel=1,
            ),
            "i=24136",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machinery_result;i=6069",
                browseName="ns=machinery_result;ResultEvaluation",
                description="The ResultEvaluation indicates whether the result was in tolerance.",
                dataType=machinery_result_datypes.ResultEvaluationEnum,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "i=24136",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machinery_result;i=6070",
                browseName="ns=machinery_result;ResultEvaluationCode",
                description="Vendor-specific code describing more details on resultEvaluation.",
                dataType=o6.Int64,
                value=0,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "i=24136",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machinery_result;i=6071",
                browseName="ns=machinery_result;ResultEvaluationDetails",
                description="The optional EvaluationDetails provides high level status information in a user-friendly text. This can be left empty for successful operations.",
                dataType=o6.LocalizedText,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "i=24136",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machinery_result;i=6072",
                browseName="ns=machinery_result;ResultState",
                description="ResultState provides information about the current state of the process or measurement creating a result.\nApplications may use negative values for application-specific states. All other values shall only be used as defined in the following:\n0 – Undefined initial value\n1 – Completed: Processing was carried out completely\n2 – Processing: Processing has not been finished yet\n3 – Aborted: Processing was stopped at some point before completion\n4 – Failed: Processing failed in some way.",
                dataType=o6.Int32,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "i=24136",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machinery_result;i=6073",
                browseName="ns=machinery_result;ResultUri",
                description="Path to the actual measured result, managed external to the server.",
                dataType=ns0.datatypes.UriString,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            ),
            "i=24136",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machinery_result;i=6074",
                browseName="ns=machinery_result;StepId",
                description="Identifies the step which produced the result.\nAlthough the system-wide unique JobId would be sufficient to identify the job which the result belongs to, this makes for easier filtering without keeping track of JobIds.\nThis specification does not define how the stepId is transmitted to the system. Typically, it is provided by the client when starting an execution.",
                dataType=ns0.datatypes.TrimmedString,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "i=24136",
        ),
    ],
    dataType=machinery_result_datypes.ResultMetaDataType,
)
machinery_result_vartypes.ResultType(
    nodeId="ns=machinery_result;i=6032",
    browseName="ns=machinery_result;Result",
    modellingRule="Mandatory",
    references=[o6.reference(o6.ns["ns=machinery_result;i=6033"], "i=24136")],
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
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(machinery_result_objtypes.ResultReadyEventType, ns0.reftypes.HasComponent, o6.ns["ns=machinery_result;i=6032"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=machinery_result;i=6079", browseName="ns=machinery_result;ResultTransferOptionsDataType", dataType=o6.String, value="ResultTransferOptionsDataType"
)
o6.reference(o6.ns["ns=machinery_result;i=5001"], "i=39", o6.ns["ns=machinery_result;i=6079"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=machinery_result;i=6080",
    browseName="ns=machinery_result;ResultTransferOptionsDataType",
    dataType=o6.String,
    value="//xs:element[@name='ResultTransferOptionsDataType']",
)
o6.reference(o6.ns["ns=machinery_result;i=5002"], "i=39", o6.ns["ns=machinery_result;i=6080"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=machinery_result;i=6081", browseName="ns=machinery_result;ProcessingTimesDataType", dataType=o6.String, value="ProcessingTimesDataType"
)
o6.reference(o6.ns["ns=machinery_result;i=5003"], "i=39", o6.ns["ns=machinery_result;i=6081"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=machinery_result;i=6082", browseName="ns=machinery_result;ProcessingTimesDataType", dataType=o6.String, value="//xs:element[@name='ProcessingTimesDataType']"
)
o6.reference(o6.ns["ns=machinery_result;i=5004"], "i=39", o6.ns["ns=machinery_result;i=6082"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=machinery_result;i=6083", browseName="ns=machinery_result;ResultDataType", dataType=o6.String, value="ResultDataType")
o6.reference(o6.ns["ns=machinery_result;i=5008"], "i=39", o6.ns["ns=machinery_result;i=6083"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=machinery_result;i=6084", browseName="ns=machinery_result;ResultDataType", dataType=o6.String, value="//xs:element[@name='ResultDataType']"
)
o6.reference(o6.ns["ns=machinery_result;i=5009"], "i=39", o6.ns["ns=machinery_result;i=6084"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=machinery_result;i=6085", browseName="ns=machinery_result;ResultMetaDataType", dataType=o6.String, value="ResultMetaDataType")
o6.reference(o6.ns["ns=machinery_result;i=5005"], "i=39", o6.ns["ns=machinery_result;i=6085"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=machinery_result;i=6086", browseName="ns=machinery_result;ResultMetaDataType", dataType=o6.String, value="//xs:element[@name='ResultMetaDataType']"
)
o6.reference(o6.ns["ns=machinery_result;i=5006"], "i=39", o6.ns["ns=machinery_result;i=6086"])
typeDictionary = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=machinery_result;i=6075",
    browseName="ns=machinery_result;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/Machinery/Result/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=machinery_result;i=6076", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/Machinery/Result/")
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=machinery_result;i=6087",
                browseName="Deprecated",
                description="Indicates that all of the DataType definitions represented by the DataTypeDictionaryType are available through a DataTypeDefinition Attribute.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(o6.ns["ns=machinery_result;i=6079"]),
        o6.hasComponent(o6.ns["ns=machinery_result;i=6081"]),
        o6.hasComponent(o6.ns["ns=machinery_result;i=6083"]),
        o6.hasComponent(o6.ns["ns=machinery_result;i=6085"]),
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" DefaultByteOrder="LittleEndian" xmlns:tns="http://opcfoundation.org/UA/Machinery/Result/" TargetNamespace="http://opcfoundation.org/UA/Machinery/Result/" xmlns:ua="http://opcfoundation.org/UA/" xmlns:opc="http://opcfoundation.org/BinarySchema/">\n <opc:Import Namespace="http://opcfoundation.org/UA/"/>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="BaseResultTransferOptionsDataType">\n  <opc:Documentation>Abstract type containing information which file should be provided.</opc:Documentation>\n  <opc:Field Name="ResultId" TypeName="opc:CharArray"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:BaseResultTransferOptionsDataType" Name="ResultTransferOptionsDataType">\n  <opc:Documentation>Contains information which file should be provided.</opc:Documentation>\n  <opc:Field Name="ResultId" TypeName="opc:CharArray" SourceType="tns:BaseResultTransferOptionsDataType"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="ProcessingTimesDataType">\n  <opc:Documentation>Contains measured times that were generated during the execution of a recipe.</opc:Documentation>\n  <opc:Field Name="AcquisitionDurationSpecified" TypeName="opc:Bit"/>\n  <opc:Field Name="ProcessingDurationSpecified" TypeName="opc:Bit"/>\n  <opc:Field Name="Reserved1" TypeName="opc:Bit" Length="30"/>\n  <opc:Field Name="StartTime" TypeName="opc:DateTime"/>\n  <opc:Field Name="EndTime" TypeName="opc:DateTime"/>\n  <opc:Field SwitchField="AcquisitionDurationSpecified" Name="AcquisitionDuration" TypeName="opc:Double"/>\n  <opc:Field SwitchField="ProcessingDurationSpecified" Name="ProcessingDuration" TypeName="opc:Double"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="ResultDataType">\n  <opc:Documentation>Contains fields that were created during the execution of a recipe.</opc:Documentation>\n  <opc:Field Name="ResultMetaData" TypeName="ua:ExtensionObject"/>\n  <opc:Field Name="NoOfResultContent" TypeName="opc:Int32"/>\n  <opc:Field LengthField="NoOfResultContent" Name="ResultContent" TypeName="ua:Variant"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="ResultMetaDataType">\n  <opc:Documentation>Meta data of a result, describing the result.</opc:Documentation>\n  <opc:Field Name="HasTransferableDataOnFileSpecified" TypeName="opc:Bit"/>\n  <opc:Field Name="IsPartialSpecified" TypeName="opc:Bit"/>\n  <opc:Field Name="IsSimulatedSpecified" TypeName="opc:Bit"/>\n  <opc:Field Name="ResultStateSpecified" TypeName="opc:Bit"/>\n  <opc:Field Name="StepIdSpecified" TypeName="opc:Bit"/>\n  <opc:Field Name="PartIdSpecified" TypeName="opc:Bit"/>\n  <opc:Field Name="ExternalRecipeIdSpecified" TypeName="opc:Bit"/>\n  <opc:Field Name="InternalRecipeIdSpecified" TypeName="opc:Bit"/>\n  <opc:Field Name="ProductIdSpecified" TypeName="opc:Bit"/>\n  <opc:Field Name="ExternalConfigurationIdSpecified" TypeName="opc:Bit"/>\n  <opc:Field Name="InternalConfigurationIdSpecified" TypeName="opc:Bit"/>\n  <opc:Field Name="JobIdSpecified" TypeName="opc:Bit"/>\n  <opc:Field Name="CreationTimeSpecified" TypeName="opc:Bit"/>\n  <opc:Field Name="ProcessingTimesSpecified" TypeName="opc:Bit"/>\n  <opc:Field Name="ResultUriSpecified" TypeName="opc:Bit"/>\n  <opc:Field Name="ResultEvaluationSpecified" TypeName="opc:Bit"/>\n  <opc:Field Name="ResultEvaluationCodeSpecified" TypeName="opc:Bit"/>\n  <opc:Field Name="ResultEvaluationDetailsSpecified" TypeName="opc:Bit"/>\n  <opc:Field Name="FileFormatSpecified" TypeName="opc:Bit"/>\n  <opc:Field Name="Reserved1" TypeName="opc:Bit" Length="13"/>\n  <opc:Field Name="ResultId" TypeName="opc:CharArray"/>\n  <opc:Field SwitchField="HasTransferableDataOnFileSpecified" Name="HasTransferableDataOnFile" TypeName="opc:Boolean"/>\n  <opc:Field SwitchField="IsPartialSpecified" Name="IsPartial" TypeName="opc:Boolean"/>\n  <opc:Field SwitchField="IsSimulatedSpecified" Name="IsSimulated" TypeName="opc:Boolean"/>\n  <opc:Field SwitchField="ResultStateSpecified" Name="ResultState" TypeName="opc:Int32"/>\n  <opc:Field SwitchField="StepIdSpecified" Name="StepId" TypeName="opc:CharArray"/>\n  <opc:Field SwitchField="PartIdSpecified" Name="PartId" TypeName="opc:CharArray"/>\n  <opc:Field SwitchField="ExternalRecipeIdSpecified" Name="ExternalRecipeId" TypeName="opc:CharArray"/>\n  <opc:Field SwitchField="InternalRecipeIdSpecified" Name="InternalRecipeId" TypeName="opc:CharArray"/>\n  <opc:Field SwitchField="ProductIdSpecified" Name="ProductId" TypeName="opc:CharArray"/>\n  <opc:Field SwitchField="ExternalConfigurationIdSpecified" Name="ExternalConfigurationId" TypeName="opc:CharArray"/>\n  <opc:Field SwitchField="InternalConfigurationIdSpecified" Name="InternalConfigurationId" TypeName="opc:CharArray"/>\n  <opc:Field SwitchField="JobIdSpecified" Name="JobId" TypeName="opc:CharArray"/>\n  <opc:Field SwitchField="CreationTimeSpecified" Name="CreationTime" TypeName="opc:DateTime"/>\n  <opc:Field SwitchField="ProcessingTimesSpecified" Name="ProcessingTimes" TypeName="tns:ProcessingTimesDataType"/>\n  <opc:Field SwitchField="ResultUriSpecified" Name="NoOfResultUri" TypeName="opc:Int32"/>\n  <opc:Field LengthField="NoOfResultUri" SwitchField="ResultUriSpecified" Name="ResultUri" TypeName="opc:CharArray"/>\n  <opc:Field SwitchField="ResultEvaluationSpecified" Name="ResultEvaluation" TypeName="tns:ResultEvaluationEnum"/>\n  <opc:Field SwitchField="ResultEvaluationCodeSpecified" Name="ResultEvaluationCode" TypeName="opc:Int64"/>\n  <opc:Field SwitchField="ResultEvaluationDetailsSpecified" Name="ResultEvaluationDetails" TypeName="ua:LocalizedText"/>\n  <opc:Field SwitchField="FileFormatSpecified" Name="NoOfFileFormat" TypeName="opc:Int32"/>\n  <opc:Field LengthField="NoOfFileFormat" SwitchField="FileFormatSpecified" Name="FileFormat" TypeName="opc:CharArray"/>\n </opc:StructuredType>\n <opc:EnumeratedType Name="ResultEvaluationEnum" LengthInBits="32">\n  <opc:Documentation>Indicates whether a result was in tolerance</opc:Documentation>\n  <opc:EnumeratedValue Name="Undefined" Value="0"/>\n  <opc:EnumeratedValue Name="OK" Value="1"/>\n  <opc:EnumeratedValue Name="NotOK" Value="2"/>\n  <opc:EnumeratedValue Name="NotDecidable" Value="3"/>\n </opc:EnumeratedType>\n</opc:TypeDictionary>\n',
)
typeDictionary_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=machinery_result;i=6077",
    browseName="ns=machinery_result;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/Machinery/Result/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machinery_result;i=6078", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/Machinery/Result/Types.xsd"
            )
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=machinery_result;i=6088",
                browseName="Deprecated",
                description="Indicates that all of the DataType definitions represented by the DataTypeDictionaryType are available through a DataTypeDefinition Attribute.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(o6.ns["ns=machinery_result;i=6080"]),
        o6.hasComponent(o6.ns["ns=machinery_result;i=6082"]),
        o6.hasComponent(o6.ns["ns=machinery_result;i=6084"]),
        o6.hasComponent(o6.ns["ns=machinery_result;i=6086"]),
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema elementFormDefault="qualified" targetNamespace="http://opcfoundation.org/UA/Machinery/Result/Types.xsd" xmlns:tns="http://opcfoundation.org/UA/Machinery/Result/Types.xsd" xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd" xmlns:xs="http://www.w3.org/2001/XMLSchema">\n <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd"/>\n <xs:simpleType name="ResultEvaluationEnum">\n  <xs:annotation>\n   <xs:documentation>Indicates whether a result was in tolerance</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Undefined_0"/>\n   <xs:enumeration value="OK_1"/>\n   <xs:enumeration value="NotOK_2"/>\n   <xs:enumeration value="NotDecidable_3"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element name="ResultEvaluationEnum" type="tns:ResultEvaluationEnum"/>\n <xs:complexType name="ListOfResultEvaluationEnum">\n  <xs:sequence>\n   <xs:element name="ResultEvaluationEnum" minOccurs="0" type="tns:ResultEvaluationEnum" maxOccurs="unbounded" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfResultEvaluationEnum" type="tns:ListOfResultEvaluationEnum" nillable="true"/>\n <xs:complexType name="BaseResultTransferOptionsDataType">\n  <xs:annotation>\n   <xs:documentation>Abstract type containing information which file should be provided.</xs:documentation>\n  </xs:annotation>\n  <xs:sequence>\n   <xs:element name="ResultId" minOccurs="0" type="xs:string" maxOccurs="1"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="BaseResultTransferOptionsDataType" type="tns:BaseResultTransferOptionsDataType"/>\n <xs:complexType name="ListOfBaseResultTransferOptionsDataType">\n  <xs:sequence>\n   <xs:element name="BaseResultTransferOptionsDataType" minOccurs="0" type="tns:BaseResultTransferOptionsDataType" maxOccurs="unbounded" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfBaseResultTransferOptionsDataType" type="tns:ListOfBaseResultTransferOptionsDataType" nillable="true"/>\n <xs:complexType name="ResultTransferOptionsDataType">\n  <xs:annotation>\n   <xs:documentation>Contains information which file should be provided.</xs:documentation>\n  </xs:annotation>\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence/>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element name="ResultTransferOptionsDataType" type="tns:ResultTransferOptionsDataType"/>\n <xs:complexType name="ListOfResultTransferOptionsDataType">\n  <xs:sequence>\n   <xs:element name="ResultTransferOptionsDataType" minOccurs="0" type="tns:ResultTransferOptionsDataType" maxOccurs="unbounded" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfResultTransferOptionsDataType" type="tns:ListOfResultTransferOptionsDataType" nillable="true"/>\n <xs:complexType name="ProcessingTimesDataType">\n  <xs:annotation>\n   <xs:documentation>Contains measured times that were generated during the execution of a recipe.</xs:documentation>\n  </xs:annotation>\n  <xs:sequence>\n   <xs:element name="EncodingMask" minOccurs="0" type="xs:unsignedInt"/>\n   <xs:element name="StartTime" minOccurs="0" type="xs:dateTime" maxOccurs="1"/>\n   <xs:element name="EndTime" minOccurs="0" type="xs:dateTime" maxOccurs="1"/>\n   <xs:element name="AcquisitionDuration" minOccurs="0" type="xs:double" maxOccurs="1"/>\n   <xs:element name="ProcessingDuration" minOccurs="0" type="xs:double" maxOccurs="1"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ProcessingTimesDataType" type="tns:ProcessingTimesDataType"/>\n <xs:complexType name="ListOfProcessingTimesDataType">\n  <xs:sequence>\n   <xs:element name="ProcessingTimesDataType" minOccurs="0" type="tns:ProcessingTimesDataType" maxOccurs="unbounded" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfProcessingTimesDataType" type="tns:ListOfProcessingTimesDataType" nillable="true"/>\n <xs:complexType name="ResultDataType">\n  <xs:annotation>\n   <xs:documentation>Contains fields that were created during the execution of a recipe.</xs:documentation>\n  </xs:annotation>\n  <xs:sequence>\n   <xs:element name="ResultMetaData" minOccurs="0" type="ua:ExtensionObject" maxOccurs="1"/>\n   <xs:element name="ResultContent" minOccurs="0" type="ua:ListOfVariant" maxOccurs="1"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ResultDataType" type="tns:ResultDataType"/>\n <xs:complexType name="ListOfResultDataType">\n  <xs:sequence>\n   <xs:element name="ResultDataType" minOccurs="0" type="tns:ResultDataType" maxOccurs="unbounded" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfResultDataType" type="tns:ListOfResultDataType" nillable="true"/>\n <xs:complexType name="ResultMetaDataType">\n  <xs:annotation>\n   <xs:documentation>Meta data of a result, describing the result.</xs:documentation>\n  </xs:annotation>\n  <xs:sequence>\n   <xs:element name="EncodingMask" minOccurs="0" type="xs:unsignedInt"/>\n   <xs:element name="ResultId" minOccurs="0" type="xs:string" maxOccurs="1"/>\n   <xs:element name="HasTransferableDataOnFile" minOccurs="0" type="xs:boolean" maxOccurs="1"/>\n   <xs:element name="IsPartial" minOccurs="0" type="xs:boolean" maxOccurs="1"/>\n   <xs:element name="IsSimulated" minOccurs="0" type="xs:boolean" maxOccurs="1"/>\n   <xs:element name="ResultState" minOccurs="0" type="xs:int" maxOccurs="1"/>\n   <xs:element name="StepId" minOccurs="0" type="xs:string" maxOccurs="1"/>\n   <xs:element name="PartId" minOccurs="0" type="xs:string" maxOccurs="1"/>\n   <xs:element name="ExternalRecipeId" minOccurs="0" type="xs:string" maxOccurs="1"/>\n   <xs:element name="InternalRecipeId" minOccurs="0" type="xs:string" maxOccurs="1"/>\n   <xs:element name="ProductId" minOccurs="0" type="xs:string" maxOccurs="1"/>\n   <xs:element name="ExternalConfigurationId" minOccurs="0" type="xs:string" maxOccurs="1"/>\n   <xs:element name="InternalConfigurationId" minOccurs="0" type="xs:string" maxOccurs="1"/>\n   <xs:element name="JobId" minOccurs="0" type="xs:string" maxOccurs="1"/>\n   <xs:element name="CreationTime" minOccurs="0" type="xs:dateTime" maxOccurs="1"/>\n   <xs:element name="ProcessingTimes" minOccurs="0" type="tns:ProcessingTimesDataType" maxOccurs="1"/>\n   <xs:element name="ResultUri" minOccurs="0" type="ua:ListOfString" maxOccurs="1"/>\n   <xs:element name="ResultEvaluation" minOccurs="0" type="tns:ResultEvaluationEnum" maxOccurs="1"/>\n   <xs:element name="ResultEvaluationCode" minOccurs="0" type="xs:long" maxOccurs="1"/>\n   <xs:element name="ResultEvaluationDetails" minOccurs="0" type="ua:LocalizedText" maxOccurs="1"/>\n   <xs:element name="FileFormat" minOccurs="0" type="ua:ListOfString" maxOccurs="1"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ResultMetaDataType" type="tns:ResultMetaDataType"/>\n <xs:complexType name="ListOfResultMetaDataType">\n  <xs:sequence>\n   <xs:element name="ResultMetaDataType" minOccurs="0" type="tns:ResultMetaDataType" maxOccurs="unbounded" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="ListOfResultMetaDataType" type="tns:ListOfResultMetaDataType" nillable="true"/>\n</xs:schema>\n',
)


ns0.vartypes.PropertyType(
    nodeId="ns=machinery_result;i=6038",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machinery_result;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="GenerateOptions",
            dataType=o6.NodeId("ns=machinery_result;i=3005"),
            valueRank=-1,
            description=o6.LocalizedText("Options how to generate the file, including the resultId of the result the file belongs to. "),
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machinery_result;i=6039",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machinery_result;i=7002",
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
    nodeId="ns=machinery_result;i=7002",
    browseName="GenerateFileForRead",
    inputArgs=o6.hasProperty(o6.ns["ns=machinery_result;i=6038"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machinery_result;i=6039"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machinery_result;i=6041",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machinery_result;i=7003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machinery_result;i=6042",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machinery_result;i=7003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="CompletionStateMachine", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(
    nodeId="ns=machinery_result;i=7003",
    browseName="CloseAndCommit",
    inputArgs=o6.hasProperty(o6.ns["ns=machinery_result;i=6041"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machinery_result;i=6042"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machinery_result;i=6043",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machinery_result;i=7004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="GenerateOptions", dataType=ns0.datatypes.BaseDataType, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machinery_result;i=6044",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machinery_result;i=7004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileNodeId", dataType=o6.NodeId, valueRank=-1), ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(
    nodeId="ns=machinery_result;i=7004",
    browseName="GenerateFileForWrite",
    inputArgs=o6.hasProperty(o6.ns["ns=machinery_result;i=6043"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machinery_result;i=6044"]),
)

machinery_result_objtypes.ResultTransferType(
    nodeId="ns=machinery_result;i=5010",
    browseName="ns=machinery_result;ResultTransfer",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery_result;i=6040", browseName="ClientProcessingTimeout", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(o6.ns["ns=machinery_result;i=7002"]),
        o6.hasComponent(o6.ns["ns=machinery_result;i=7003"]),
        o6.hasComponent(o6.ns["ns=machinery_result;i=7004"]),
    ],
)
o6.reference(machinery_result_objtypes.ResultManagementType, ns0.reftypes.HasComponent, o6.ns["ns=machinery_result;i=5010"])


del Any, TYPE_CHECKING, uuid, o6, ns0, machinery_result_datypes, machinery_result_vartypes, machinery_result_objtypes
