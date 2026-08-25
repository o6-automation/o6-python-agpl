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
from . import datatypes as ttd_datypes
from . import vartypes as ttd_vartypes
from . import objtypes as ttd_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.objtypes.DataTypeEncodingType(nodeId="ns=ttd;i=5002", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ttd;i=5003", browseName="Default XML")
o6.hasEncoding(ttd_datypes.RecipeIdDataType, o6.ns["ns=ttd;i=5003"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ttd;i=5004", browseName="Default JSON")
o6.hasEncoding(ttd_datypes.RecipeIdDataType, o6.ns["ns=ttd;i=5004"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ttd;i=5005", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ttd;i=5006", browseName="Default XML")
o6.hasEncoding(ttd_datypes.ExchangeablePartDataType, o6.ns["ns=ttd;i=5006"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ttd;i=5007", browseName="Default JSON")
o6.hasEncoding(ttd_datypes.ExchangeablePartDataType, o6.ns["ns=ttd;i=5007"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ttd;i=5008", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ttd;i=5009", browseName="Default XML")
o6.hasEncoding(ttd_datypes.OptionalModuleDataType, o6.ns["ns=ttd;i=5009"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ttd;i=5010", browseName="Default JSON")
o6.hasEncoding(ttd_datypes.OptionalModuleDataType, o6.ns["ns=ttd;i=5010"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ttd;i=5011", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ttd;i=5012", browseName="Default XML")
o6.hasEncoding(ttd_datypes.StatisticResultContentDataType, o6.ns["ns=ttd;i=5012"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ttd;i=5013", browseName="Default JSON")
o6.hasEncoding(ttd_datypes.StatisticResultContentDataType, o6.ns["ns=ttd;i=5013"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ttd;i=5014", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ttd;i=5015", browseName="Default XML")
o6.hasEncoding(ttd_datypes.StatisticResultContentWithUnitsDataType, o6.ns["ns=ttd;i=5015"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ttd;i=5016", browseName="Default JSON")
o6.hasEncoding(ttd_datypes.StatisticResultContentWithUnitsDataType, o6.ns["ns=ttd;i=5016"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ttd;i=5017", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ttd;i=5018", browseName="Default XML")
o6.hasEncoding(ttd_datypes.RecipeDataType, o6.ns["ns=ttd;i=5018"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ttd;i=5019", browseName="Default JSON")
o6.hasEncoding(ttd_datypes.RecipeDataType, o6.ns["ns=ttd;i=5019"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ttd;i=5020", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ttd;i=5021", browseName="Default XML")
o6.hasEncoding(ttd_datypes.TTDResultMetaDataType, o6.ns["ns=ttd;i=5021"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ttd;i=5022", browseName="Default JSON")
o6.hasEncoding(ttd_datypes.TTDResultMetaDataType, o6.ns["ns=ttd;i=5022"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ttd;i=5023", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ttd;i=5024", browseName="Default XML")
o6.hasEncoding(ttd_datypes.JobOrderDataType, o6.ns["ns=ttd;i=5024"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ttd;i=5025", browseName="Default JSON")
o6.hasEncoding(ttd_datypes.JobOrderDataType, o6.ns["ns=ttd;i=5025"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ttd;i=5026", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ttd;i=5027", browseName="Default XML")
o6.hasEncoding(ttd_datypes.TestNumDataType, o6.ns["ns=ttd;i=5027"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ttd;i=5028", browseName="Default JSON")
o6.hasEncoding(ttd_datypes.TestNumDataType, o6.ns["ns=ttd;i=5028"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ttd;i=5029", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ttd;i=5030", browseName="Default XML")
o6.hasEncoding(ttd_datypes.SampleInfoDataType, o6.ns["ns=ttd;i=5030"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ttd;i=5031", browseName="Default JSON")
o6.hasEncoding(ttd_datypes.SampleInfoDataType, o6.ns["ns=ttd;i=5031"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ttd;i=5032", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ttd;i=5033", browseName="Default XML")
o6.hasEncoding(ttd_datypes.TestProcedureIdDataType, o6.ns["ns=ttd;i=5033"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=ttd;i=5034", browseName="Default JSON")
o6.hasEncoding(ttd_datypes.TestProcedureIdDataType, o6.ns["ns=ttd;i=5034"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=ttd;i=6002",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ttd;i=6003", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
isa95_jobcontrol_v2.objtypes.ISA95JobOrderReceiverObjectType(
    nodeId="ns=ttd;i=5036",
    browseName="ns=machinery_jobs;JobOrderControl",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ttd;i=6008", browseName="ns=isa95_jobcontrol_v2;MaxDownloadableJobOrders", dataType=o6.UInt16)),
        o6.hasComponent(o6.ns["ns=ttd;i=6002"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ttd;i=6004",
                browseName="ns=isa95_jobcontrol_v2;EquipmentID",
                description="Defines a read-only set of Equipment Class IDs and Equipment IDs that may be specified in a job order.",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ttd;i=6005",
                browseName="ns=isa95_jobcontrol_v2;JobOrderList",
                description="Defines a read-only list of job order information available from the server.",
                dataType=isa95_jobcontrol_v2.datatypes.ISA95JobOrderAndStateDataType,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ttd;i=6006",
                browseName="ns=isa95_jobcontrol_v2;MaterialClassID",
                description="Defines a read-only set of Material Classes IDs that may be specified in a job order.",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ttd;i=6007",
                browseName="ns=isa95_jobcontrol_v2;MaterialDefinitionID",
                description="Defines a read-only set of Material Classes IDs that may be specified in a job order.",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ttd;i=6009",
                browseName="ns=isa95_jobcontrol_v2;PersonnelID",
                description="Defines a read-only set of Personnel IDs and Person IDs that may be specified in a job order.",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ttd;i=6010",
                browseName="ns=isa95_jobcontrol_v2;PhysicalAssetID",
                description="Defines a read-only set of Physical Asset Class IDs and Physical Asset IDs that may be specified in a job order.",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ttd;i=6011",
                browseName="ns=isa95_jobcontrol_v2;WorkMaster",
                description="Defines a read-only set of work master IDs that may be specified in a job order, and the read-only set of parameters that may be specified for a specific work master.",
                dataType=isa95_jobcontrol_v2.datatypes.ISA95WorkMasterDataType,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
    ],
)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=ttd;i=6001",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ttd;i=6027", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
machinery.objtypes.MachineryOperationModeStateMachineType(
    nodeId="ns=ttd;i=5001", browseName="ns=machinery;MachineryOperationMode", references=[o6.hasComponent(o6.ns["ns=ttd;i=6001"])]
)
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=ttd;i=6028",
    browseName="ns=machinery_result;ResultMetaData",
    modellingRule="Mandatory",
    references=[
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ttd;i=6029", browseName="ns=machinery_result;HasTransferableDataOnFile", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
            ),
            "i=24136",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=ttd;i=6030", browseName="ns=machinery_result;IsPartial", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1), "i=24136"
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ttd;i=6031", browseName="ns=machinery_result;CreationTime", dataType=ns0.datatypes.UtcTime, accessLevel=3, userAccessLevel=1
            ),
            "i=24136",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=ttd;i=6032", browseName="ns=ttd;ProductInstanceUri", dataType=o6.String, accessLevel=3, userAccessLevel=1), "i=24136"
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=ttd;i=6033", browseName="ns=ttd;TesterSampleResultId", dataType=o6.String, accessLevel=3, userAccessLevel=1), "i=24136"
        ),
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=ttd;i=6034", browseName="ns=ttd;SampleId", dataType=o6.String, accessLevel=3, userAccessLevel=1), "i=24136"),
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=ttd;i=6035", browseName="ns=ttd;TesterJobId", dataType=o6.String, accessLevel=3, userAccessLevel=1), "i=24136"),
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=ttd;i=6036", browseName="ns=ttd;CanBeDeleted", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1), "i=24136"),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ttd;i=6037", browseName="ns=ttd;JobOrder", dataType=isa95_jobcontrol_v2.datatypes.ISA95JobOrderDataType, accessLevel=3, userAccessLevel=1
            ),
            "i=24136",
        ),
    ],
    dataType=machinery_result.datatypes.ResultMetaDataType,
    value=machinery_result.datatypes.ResultMetaDataType(
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
)
o6.reference(ttd_vartypes.TTDResultType, ns0.reftypes.HasStructuredComponent, o6.ns["ns=ttd;i=6028"])
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=ttd;i=6039",
    browseName="ns=machinery_result;ResultMetaData",
    references=[
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=ttd;i=6040", browseName="ns=ttd;CanBeDeleted", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1), "i=24136"),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ttd;i=6041", browseName="ns=machinery_result;CreationTime", dataType=ns0.datatypes.UtcTime, accessLevel=3, userAccessLevel=1
            ),
            "i=24136",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ttd;i=6042", browseName="ns=machinery_result;HasTransferableDataOnFile", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
            ),
            "i=24136",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=ttd;i=6043", browseName="ns=machinery_result;IsPartial", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1), "i=24136"
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ttd;i=6044", browseName="ns=ttd;JobOrder", dataType=isa95_jobcontrol_v2.datatypes.ISA95JobOrderDataType, accessLevel=3, userAccessLevel=1
            ),
            "i=24136",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=ttd;i=6045", browseName="ns=ttd;ProductInstanceUri", dataType=o6.String, accessLevel=3, userAccessLevel=1), "i=24136"
        ),
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=ttd;i=6046", browseName="ns=ttd;SampleId", dataType=o6.String, accessLevel=3, userAccessLevel=1), "i=24136"),
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=ttd;i=6047", browseName="ns=ttd;TesterJobId", dataType=o6.String, accessLevel=3, userAccessLevel=1), "i=24136"),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=ttd;i=6048", browseName="ns=ttd;TesterSampleResultId", dataType=o6.String, accessLevel=3, userAccessLevel=1), "i=24136"
        ),
    ],
    dataType=machinery_result.datatypes.ResultMetaDataType,
    value=machinery_result.datatypes.ResultMetaDataType(
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
)
ttd_vartypes.TTDResultType(
    nodeId="ns=ttd;i=6038",
    browseName="ns=machinery_result;Result",
    modellingRule="Mandatory",
    references=[o6.reference(o6.ns["ns=ttd;i=6039"], "i=24136")],
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
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(ttd_objtypes.TTDResultReadyEventType, ns0.reftypes.HasComponent, o6.ns["ns=ttd;i=6038"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=ttd;i=6073", browseName="ns=ttd;ExchangeablePartDataType", dataType=o6.String, value="ExchangeablePartDataType")
o6.reference(o6.ns["ns=ttd;i=5005"], "i=39", o6.ns["ns=ttd;i=6073"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=ttd;i=6074", browseName="ns=ttd;ExchangeablePartDataType", dataType=o6.String, value="//xs:element[@name='ExchangeablePartDataType']"
)
o6.reference(o6.ns["ns=ttd;i=5006"], "i=39", o6.ns["ns=ttd;i=6074"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=ttd;i=6075", browseName="ns=ttd;JobOrderDataType", dataType=o6.String, value="JobOrderDataType")
o6.reference(o6.ns["ns=ttd;i=5023"], "i=39", o6.ns["ns=ttd;i=6075"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=ttd;i=6076", browseName="ns=ttd;JobOrderDataType", dataType=o6.String, value="//xs:element[@name='JobOrderDataType']")
o6.reference(o6.ns["ns=ttd;i=5024"], "i=39", o6.ns["ns=ttd;i=6076"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=ttd;i=6077", browseName="ns=ttd;OptionalModuleDataType", dataType=o6.String, value="OptionalModuleDataType")
o6.reference(o6.ns["ns=ttd;i=5008"], "i=39", o6.ns["ns=ttd;i=6077"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=ttd;i=6078", browseName="ns=ttd;OptionalModuleDataType", dataType=o6.String, value="//xs:element[@name='OptionalModuleDataType']")
o6.reference(o6.ns["ns=ttd;i=5009"], "i=39", o6.ns["ns=ttd;i=6078"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=ttd;i=6079", browseName="ns=ttd;RecipeDataType", dataType=o6.String, value="RecipeDataType")
o6.reference(o6.ns["ns=ttd;i=5017"], "i=39", o6.ns["ns=ttd;i=6079"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=ttd;i=6080", browseName="ns=ttd;RecipeDataType", dataType=o6.String, value="//xs:element[@name='RecipeDataType']")
o6.reference(o6.ns["ns=ttd;i=5018"], "i=39", o6.ns["ns=ttd;i=6080"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=ttd;i=6081", browseName="ns=ttd;RecipeIdDataType", dataType=o6.String, value="RecipeIdDataType")
o6.reference(o6.ns["ns=ttd;i=5002"], "i=39", o6.ns["ns=ttd;i=6081"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=ttd;i=6082", browseName="ns=ttd;RecipeIdDataType", dataType=o6.String, value="//xs:element[@name='RecipeIdDataType']")
o6.reference(o6.ns["ns=ttd;i=5003"], "i=39", o6.ns["ns=ttd;i=6082"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=ttd;i=6083", browseName="ns=ttd;TTDResultMetaDataType", dataType=o6.String, value="TTDResultMetaDataType")
o6.reference(o6.ns["ns=ttd;i=5020"], "i=39", o6.ns["ns=ttd;i=6083"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=ttd;i=6084", browseName="ns=ttd;TTDResultMetaDataType", dataType=o6.String, value="//xs:element[@name='TTDResultMetaDataType']")
o6.reference(o6.ns["ns=ttd;i=5021"], "i=39", o6.ns["ns=ttd;i=6084"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=ttd;i=6085", browseName="ns=ttd;SampleInfoDataType", dataType=o6.String, value="SampleInfoDataType")
o6.reference(o6.ns["ns=ttd;i=5029"], "i=39", o6.ns["ns=ttd;i=6085"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=ttd;i=6086", browseName="ns=ttd;SampleInfoDataType", dataType=o6.String, value="//xs:element[@name='SampleInfoDataType']")
o6.reference(o6.ns["ns=ttd;i=5030"], "i=39", o6.ns["ns=ttd;i=6086"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=ttd;i=6087", browseName="ns=ttd;StatisticResultContentDataType", dataType=o6.String, value="StatisticResultContentDataType")
o6.reference(o6.ns["ns=ttd;i=5011"], "i=39", o6.ns["ns=ttd;i=6087"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=ttd;i=6088", browseName="ns=ttd;StatisticResultContentDataType", dataType=o6.String, value="//xs:element[@name='StatisticResultContentDataType']"
)
o6.reference(o6.ns["ns=ttd;i=5012"], "i=39", o6.ns["ns=ttd;i=6088"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=ttd;i=6089", browseName="ns=ttd;StatisticResultContentWithUnitsDataType", dataType=o6.String, value="StatisticResultContentWithUnitsDataType"
)
o6.reference(o6.ns["ns=ttd;i=5014"], "i=39", o6.ns["ns=ttd;i=6089"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=ttd;i=6090", browseName="ns=ttd;StatisticResultContentWithUnitsDataType", dataType=o6.String, value="//xs:element[@name='StatisticResultContentWithUnitsDataType']"
)
o6.reference(o6.ns["ns=ttd;i=5015"], "i=39", o6.ns["ns=ttd;i=6090"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=ttd;i=6091", browseName="ns=ttd;TestNumDataType", dataType=o6.String, value="TestNumDataType")
o6.reference(o6.ns["ns=ttd;i=5026"], "i=39", o6.ns["ns=ttd;i=6091"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=ttd;i=6092", browseName="ns=ttd;TestNumDataType", dataType=o6.String, value="//xs:element[@name='TestNumDataType']")
o6.reference(o6.ns["ns=ttd;i=5027"], "i=39", o6.ns["ns=ttd;i=6092"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=ttd;i=6093", browseName="ns=ttd;TestProcedureIdDataType", dataType=o6.String, value="TestProcedureIdDataType")
o6.reference(o6.ns["ns=ttd;i=5032"], "i=39", o6.ns["ns=ttd;i=6093"])
typeDictionary = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=ttd;i=6069",
    browseName="ns=ttd;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/TTD/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ttd;i=6070", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/TTD/")),
        o6.hasComponent(o6.ns["ns=ttd;i=6073"]),
        o6.hasComponent(o6.ns["ns=ttd;i=6075"]),
        o6.hasComponent(o6.ns["ns=ttd;i=6077"]),
        o6.hasComponent(o6.ns["ns=ttd;i=6079"]),
        o6.hasComponent(o6.ns["ns=ttd;i=6081"]),
        o6.hasComponent(o6.ns["ns=ttd;i=6083"]),
        o6.hasComponent(o6.ns["ns=ttd;i=6085"]),
        o6.hasComponent(o6.ns["ns=ttd;i=6087"]),
        o6.hasComponent(o6.ns["ns=ttd;i=6089"]),
        o6.hasComponent(o6.ns["ns=ttd;i=6091"]),
        o6.hasComponent(o6.ns["ns=ttd;i=6093"]),
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:tns="http://opcfoundation.org/UA/TTD/" DefaultByteOrder="LittleEndian" xmlns:opc="http://opcfoundation.org/BinarySchema/" xmlns:ns1="http://opcfoundation.org/UA/Machinery/Result/" xmlns:ns2="http://opcfoundation.org/UA/ISA95-JOBCONTROL_V2/" xmlns:ua="http://opcfoundation.org/UA/" TargetNamespace="http://opcfoundation.org/UA/TTD/">\n <opc:Import Namespace="http://opcfoundation.org/UA/"/>\n <opc:Import Namespace="http://opcfoundation.org/UA/Machinery/Result/"/>\n <opc:Import Namespace="http://opcfoundation.org/UA/ISA95-JOBCONTROL_V2/"/>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="ExchangeablePartDataType">\n  <opc:Field TypeName="opc:Bit" Name="TraceableSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="PartIdSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="MachineReadableSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="LastCalibrationDateSpecified"/>\n  <opc:Field Length="28" TypeName="opc:Bit" Name="Reserved1"/>\n  <opc:Field TypeName="opc:CharArray" Name="PartType"/>\n  <opc:Field TypeName="opc:Boolean" Name="Mounted"/>\n  <opc:Field SwitchField="TraceableSpecified" TypeName="opc:Boolean" Name="Traceable"/>\n  <opc:Field SwitchField="PartIdSpecified" TypeName="opc:CharArray" Name="PartId"/>\n  <opc:Field SwitchField="MachineReadableSpecified" TypeName="opc:Boolean" Name="MachineReadable"/>\n  <opc:Field SwitchField="LastCalibrationDateSpecified" TypeName="opc:DateTime" Name="LastCalibrationDate"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="JobOrderDataType">\n  <opc:Field TypeName="opc:Bit" Name="AdditionalInfoSpecified"/>\n  <opc:Field Length="31" TypeName="opc:Bit" Name="Reserved1"/>\n  <opc:Field TypeName="opc:CharArray" Name="JobId"/>\n  <opc:Field TypeName="tns:RecipeIdDataType" Name="RecipeId"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfNumberOfTests"/>\n  <opc:Field LengthField="NoOfNumberOfTests" TypeName="tns:TestNumDataType" Name="NumberOfTests"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfSampleInfos"/>\n  <opc:Field LengthField="NoOfSampleInfos" TypeName="tns:SampleInfoDataType" Name="SampleInfos"/>\n  <opc:Field TypeName="opc:CharArray" Name="CarrierTypeId"/>\n  <opc:Field TypeName="opc:CharArray" Name="CarrierId"/>\n  <opc:Field SwitchField="AdditionalInfoSpecified" TypeName="opc:Int32" Name="NoOfAdditionalInfo"/>\n  <opc:Field LengthField="NoOfAdditionalInfo" SwitchField="AdditionalInfoSpecified" TypeName="ua:KeyValuePair" Name="AdditionalInfo"/>\n  <opc:Field TypeName="opc:Boolean" Name="Scheduled"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="OptionalModuleDataType">\n  <opc:Field TypeName="opc:Bit" Name="VersionSpecified"/>\n  <opc:Field Length="31" TypeName="opc:Bit" Name="Reserved1"/>\n  <opc:Field TypeName="opc:CharArray" Name="ModuleName"/>\n  <opc:Field TypeName="opc:CharArray" Name="ModuleType"/>\n  <opc:Field TypeName="opc:Boolean" Name="IsInstalled"/>\n  <opc:Field SwitchField="VersionSpecified" TypeName="opc:CharArray" Name="Version"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="RecipeDataType">\n  <opc:Field TypeName="tns:RecipeIdDataType" Name="RecipeId"/>\n  <opc:Field TypeName="opc:ByteString" Name="RecipeContent"/>\n  <opc:Field TypeName="opc:CharArray" Name="ContentEncoding"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="RecipeIdDataType">\n  <opc:Field TypeName="opc:Bit" Name="NameSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="TypeSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="DescriptionSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="CommentSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="ModifiedDateSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="VersionSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="ValidatedSpecified"/>\n  <opc:Field Length="25" TypeName="opc:Bit" Name="Reserved1"/>\n  <opc:Field SwitchField="NameSpecified" TypeName="opc:CharArray" Name="Name"/>\n  <opc:Field TypeName="opc:CharArray" Name="Id"/>\n  <opc:Field SwitchField="TypeSpecified" TypeName="opc:CharArray" Name="Type"/>\n  <opc:Field SwitchField="DescriptionSpecified" TypeName="opc:CharArray" Name="Description"/>\n  <opc:Field SwitchField="CommentSpecified" TypeName="opc:CharArray" Name="Comment"/>\n  <opc:Field SwitchField="ModifiedDateSpecified" TypeName="opc:DateTime" Name="ModifiedDate"/>\n  <opc:Field SwitchField="VersionSpecified" TypeName="opc:CharArray" Name="Version"/>\n  <opc:Field SwitchField="ValidatedSpecified" TypeName="opc:Boolean" Name="Validated"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ns1:ResultMetaDataType" Name="TTDResultMetaDataType">\n  <opc:Field TypeName="opc:Bit" Name="HasTransferableDataOnFileSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="IsPartialSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="IsSimulatedSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="ResultStateSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="StepIdSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="PartIdSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="ExternalRecipeIdSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="InternalRecipeIdSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="ProductIdSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="ExternalConfigurationIdSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="InternalConfigurationIdSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="JobIdSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="CreationTimeSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="ProcessingTimesSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="ResultUriSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="ResultEvaluationSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="ResultEvaluationCodeSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="ResultEvaluationDetailsSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="FileFormatSpecified"/>\n  <opc:Field Length="13" TypeName="opc:Bit" Name="Reserved1"/>\n  <opc:Field SourceType="ns1:ResultMetaDataType" TypeName="opc:CharArray" Name="ResultId"/>\n  <opc:Field SwitchField="HasTransferableDataOnFileSpecified" SourceType="ns1:ResultMetaDataType" TypeName="opc:Boolean" Name="HasTransferableDataOnFile"/>\n  <opc:Field SwitchField="IsPartialSpecified" SourceType="ns1:ResultMetaDataType" TypeName="opc:Boolean" Name="IsPartial"/>\n  <opc:Field SwitchField="IsSimulatedSpecified" SourceType="ns1:ResultMetaDataType" TypeName="opc:Boolean" Name="IsSimulated"/>\n  <opc:Field SwitchField="ResultStateSpecified" SourceType="ns1:ResultMetaDataType" TypeName="opc:Int32" Name="ResultState"/>\n  <opc:Field SwitchField="StepIdSpecified" SourceType="ns1:ResultMetaDataType" TypeName="opc:CharArray" Name="StepId"/>\n  <opc:Field SwitchField="PartIdSpecified" SourceType="ns1:ResultMetaDataType" TypeName="opc:CharArray" Name="PartId"/>\n  <opc:Field SwitchField="ExternalRecipeIdSpecified" SourceType="ns1:ResultMetaDataType" TypeName="opc:CharArray" Name="ExternalRecipeId"/>\n  <opc:Field SwitchField="InternalRecipeIdSpecified" SourceType="ns1:ResultMetaDataType" TypeName="opc:CharArray" Name="InternalRecipeId"/>\n  <opc:Field SwitchField="ProductIdSpecified" SourceType="ns1:ResultMetaDataType" TypeName="opc:CharArray" Name="ProductId"/>\n  <opc:Field SwitchField="ExternalConfigurationIdSpecified" SourceType="ns1:ResultMetaDataType" TypeName="opc:CharArray" Name="ExternalConfigurationId"/>\n  <opc:Field SwitchField="InternalConfigurationIdSpecified" SourceType="ns1:ResultMetaDataType" TypeName="opc:CharArray" Name="InternalConfigurationId"/>\n  <opc:Field SwitchField="JobIdSpecified" SourceType="ns1:ResultMetaDataType" TypeName="opc:CharArray" Name="JobId"/>\n  <opc:Field SwitchField="CreationTimeSpecified" SourceType="ns1:ResultMetaDataType" TypeName="opc:DateTime" Name="CreationTime"/>\n  <opc:Field SwitchField="ProcessingTimesSpecified" SourceType="ns1:ResultMetaDataType" TypeName="ns1:ProcessingTimesDataType" Name="ProcessingTimes"/>\n  <opc:Field SwitchField="ResultUriSpecified" SourceType="ns1:ResultMetaDataType" TypeName="opc:Int32" Name="NoOfResultUri"/>\n  <opc:Field LengthField="NoOfResultUri" SwitchField="ResultUriSpecified" SourceType="ns1:ResultMetaDataType" TypeName="opc:CharArray" Name="ResultUri"/>\n  <opc:Field SwitchField="ResultEvaluationSpecified" SourceType="ns1:ResultMetaDataType" TypeName="ns1:ResultEvaluationEnum" Name="ResultEvaluation"/>\n  <opc:Field SwitchField="ResultEvaluationCodeSpecified" SourceType="ns1:ResultMetaDataType" TypeName="opc:Int64" Name="ResultEvaluationCode"/>\n  <opc:Field SwitchField="ResultEvaluationDetailsSpecified" SourceType="ns1:ResultMetaDataType" TypeName="ua:LocalizedText" Name="ResultEvaluationDetails"/>\n  <opc:Field SwitchField="FileFormatSpecified" SourceType="ns1:ResultMetaDataType" TypeName="opc:Int32" Name="NoOfFileFormat"/>\n  <opc:Field LengthField="NoOfFileFormat" SwitchField="FileFormatSpecified" SourceType="ns1:ResultMetaDataType" TypeName="opc:CharArray" Name="FileFormat"/>\n  <opc:Field TypeName="opc:CharArray" Name="SampleId"/>\n  <opc:Field TypeName="opc:CharArray" Name="TesterJobId"/>\n  <opc:Field TypeName="opc:CharArray" Name="TesterSampleResultId"/>\n  <opc:Field TypeName="opc:CharArray" Name="ProductInstanceURI"/>\n  <opc:Field TypeName="opc:Boolean" Name="CanBeDeleted"/>\n  <opc:Field TypeName="ns2:ISA95JobOrderDataType" Name="JobOrder"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="SampleInfoDataType">\n  <opc:Field TypeName="opc:Bit" Name="MaterialDensitySpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="MaterialTypeSpecified"/>\n  <opc:Field Length="30" TypeName="opc:Bit" Name="Reserved1"/>\n  <opc:Field TypeName="opc:CharArray" Name="SampleId"/>\n  <opc:Field TypeName="opc:Double" Name="NominalLinearDensity"/>\n  <opc:Field SwitchField="MaterialDensitySpecified" TypeName="opc:Double" Name="MaterialDensity"/>\n  <opc:Field SwitchField="MaterialTypeSpecified" TypeName="opc:CharArray" Name="MaterialType"/>\n  <opc:Field TypeName="opc:CharArray" Name="PositionOnCarrier"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="StatisticResultContentDataType">\n  <opc:Field TypeName="opc:CharArray" Name="ResultKey"/>\n  <opc:Field TypeName="opc:UInt32" Name="ItemCount"/>\n  <opc:Field TypeName="opc:Double" Name="MeanValue"/>\n  <opc:Field TypeName="opc:Double" Name="StandardDeviation"/>\n  <opc:Field TypeName="opc:Double" Name="CoefficientOfVariation"/>\n  <opc:Field TypeName="opc:Double" Name="MinValue"/>\n  <opc:Field TypeName="opc:Double" Name="MaxValue"/>\n  <opc:Field TypeName="opc:Double" Name="ConfidenceInterval95"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:StatisticResultContentDataType" Name="StatisticResultContentWithUnitsDataType">\n  <opc:Field SourceType="tns:StatisticResultContentDataType" TypeName="opc:CharArray" Name="ResultKey"/>\n  <opc:Field SourceType="tns:StatisticResultContentDataType" TypeName="opc:UInt32" Name="ItemCount"/>\n  <opc:Field SourceType="tns:StatisticResultContentDataType" TypeName="opc:Double" Name="MeanValue"/>\n  <opc:Field SourceType="tns:StatisticResultContentDataType" TypeName="opc:Double" Name="StandardDeviation"/>\n  <opc:Field SourceType="tns:StatisticResultContentDataType" TypeName="opc:Double" Name="CoefficientOfVariation"/>\n  <opc:Field SourceType="tns:StatisticResultContentDataType" TypeName="opc:Double" Name="MinValue"/>\n  <opc:Field SourceType="tns:StatisticResultContentDataType" TypeName="opc:Double" Name="MaxValue"/>\n  <opc:Field SourceType="tns:StatisticResultContentDataType" TypeName="opc:Double" Name="ConfidenceInterval95"/>\n  <opc:Field TypeName="ua:EUInformation" Name="UnitItemCount"/>\n  <opc:Field TypeName="ua:EUInformation" Name="UnitMeanValue"/>\n  <opc:Field TypeName="ua:EUInformation" Name="UnitStandardDeviation"/>\n  <opc:Field TypeName="ua:EUInformation" Name="UnitCoefficientOfVariation"/>\n  <opc:Field TypeName="ua:EUInformation" Name="UnitMinValue"/>\n  <opc:Field TypeName="ua:EUInformation" Name="UnitMaxValue"/>\n  <opc:Field TypeName="ua:EUInformation" Name="UnitConfidenceInterval"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="TestNumDataType">\n  <opc:Field TypeName="opc:CharArray" Name="TestProcedureId"/>\n  <opc:Field TypeName="opc:UInt32" Name="NumberOfTests"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="TestProcedureIdDataType">\n  <opc:Field TypeName="opc:Bit" Name="DescriptionSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="ProcedureReferencesSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="IsProcedureLicensedSpecified"/>\n  <opc:Field Length="29" TypeName="opc:Bit" Name="Reserved1"/>\n  <opc:Field TypeName="opc:CharArray" Name="TestProcedureId"/>\n  <opc:Field SwitchField="DescriptionSpecified" TypeName="opc:CharArray" Name="Description"/>\n  <opc:Field SwitchField="ProcedureReferencesSpecified" TypeName="opc:Int32" Name="NoOfProcedureReferences"/>\n  <opc:Field LengthField="NoOfProcedureReferences" SwitchField="ProcedureReferencesSpecified" TypeName="opc:CharArray" Name="ProcedureReferences"/>\n  <opc:Field SwitchField="IsProcedureLicensedSpecified" TypeName="opc:Boolean" Name="IsProcedureLicensed"/>\n </opc:StructuredType>\n</opc:TypeDictionary>\n',
)
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=ttd;i=6094", browseName="ns=ttd;TestProcedureIdDataType", dataType=o6.String, value="//xs:element[@name='TestProcedureIdDataType']")
o6.reference(o6.ns["ns=ttd;i=5033"], "i=39", o6.ns["ns=ttd;i=6094"])
typeDictionary_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=ttd;i=6071",
    browseName="ns=ttd;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/TTD/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ttd;i=6072", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/TTD/Types.xsd")),
        o6.hasComponent(o6.ns["ns=ttd;i=6074"]),
        o6.hasComponent(o6.ns["ns=ttd;i=6076"]),
        o6.hasComponent(o6.ns["ns=ttd;i=6078"]),
        o6.hasComponent(o6.ns["ns=ttd;i=6080"]),
        o6.hasComponent(o6.ns["ns=ttd;i=6082"]),
        o6.hasComponent(o6.ns["ns=ttd;i=6084"]),
        o6.hasComponent(o6.ns["ns=ttd;i=6086"]),
        o6.hasComponent(o6.ns["ns=ttd;i=6088"]),
        o6.hasComponent(o6.ns["ns=ttd;i=6090"]),
        o6.hasComponent(o6.ns["ns=ttd;i=6092"]),
        o6.hasComponent(o6.ns["ns=ttd;i=6094"]),
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema elementFormDefault="qualified" targetNamespace="http://opcfoundation.org/UA/TTD/Types.xsd" xmlns:tns="http://opcfoundation.org/UA/TTD/Types.xsd" xmlns:ns3="http://opcfoundation.org/UA/Machinery/Result/Types.xsd" xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd" xmlns:ns6="http://opcfoundation.org/UA/ISA95-JOBCONTROL_V2/Types.xsd" xmlns:xs="http://www.w3.org/2001/XMLSchema">\n <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd"/>\n <xs:import namespace="http://opcfoundation.org/UA/ISA95-JOBCONTROL_V2/Types.xsd"/>\n <xs:import namespace="http://opcfoundation.org/UA/Machinery/Result/Types.xsd"/>\n <xs:complexType name="ExchangeablePartDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" type="xs:unsignedInt" name="EncodingMask"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="PartType"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:boolean" name="Mounted"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:boolean" name="Traceable"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="PartId"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:boolean" name="MachineReadable"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:dateTime" name="LastCalibrationDate"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ExchangeablePartDataType" name="ExchangeablePartDataType"/>\n <xs:complexType name="ListOfExchangeablePartDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ExchangeablePartDataType" name="ExchangeablePartDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfExchangeablePartDataType" name="ListOfExchangeablePartDataType" nillable="true"/>\n <xs:complexType name="JobOrderDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" type="xs:unsignedInt" name="EncodingMask"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="JobId"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:RecipeIdDataType" name="RecipeId"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:ListOfTestNumDataType" name="NumberOfTests"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:ListOfSampleInfoDataType" name="SampleInfos"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="CarrierTypeId"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="CarrierId"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfKeyValuePair" name="AdditionalInfo"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:boolean" name="Scheduled"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:JobOrderDataType" name="JobOrderDataType"/>\n <xs:complexType name="ListOfJobOrderDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:JobOrderDataType" name="JobOrderDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfJobOrderDataType" name="ListOfJobOrderDataType" nillable="true"/>\n <xs:complexType name="OptionalModuleDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" type="xs:unsignedInt" name="EncodingMask"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="ModuleName"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="ModuleType"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:boolean" name="IsInstalled"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="Version"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:OptionalModuleDataType" name="OptionalModuleDataType"/>\n <xs:complexType name="ListOfOptionalModuleDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:OptionalModuleDataType" name="OptionalModuleDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfOptionalModuleDataType" name="ListOfOptionalModuleDataType" nillable="true"/>\n <xs:complexType name="RecipeDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:RecipeIdDataType" name="RecipeId"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:base64Binary" name="RecipeContent"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="ContentEncoding"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:RecipeDataType" name="RecipeDataType"/>\n <xs:complexType name="ListOfRecipeDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:RecipeDataType" name="RecipeDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfRecipeDataType" name="ListOfRecipeDataType" nillable="true"/>\n <xs:complexType name="RecipeIdDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" type="xs:unsignedInt" name="EncodingMask"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="Name"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="Id"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="Type"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="Description"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="Comment"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:dateTime" name="ModifiedDate"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="Version"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:boolean" name="Validated"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:RecipeIdDataType" name="RecipeIdDataType"/>\n <xs:complexType name="ListOfRecipeIdDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:RecipeIdDataType" name="RecipeIdDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfRecipeIdDataType" name="ListOfRecipeIdDataType" nillable="true"/>\n <xs:complexType name="TTDResultMetaDataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ns3:ResultMetaDataType">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="SampleId"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="TesterJobId"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="TesterSampleResultId"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="ProductInstanceURI"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:boolean" name="CanBeDeleted"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="ns6:ISA95JobOrderDataType" name="JobOrder"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:TTDResultMetaDataType" name="TTDResultMetaDataType"/>\n <xs:complexType name="ListOfTTDResultMetaDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:TTDResultMetaDataType" name="TTDResultMetaDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfTTDResultMetaDataType" name="ListOfTTDResultMetaDataType" nillable="true"/>\n <xs:complexType name="SampleInfoDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" type="xs:unsignedInt" name="EncodingMask"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="SampleId"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="NominalLinearDensity"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="MaterialDensity"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="MaterialType"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="PositionOnCarrier"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:SampleInfoDataType" name="SampleInfoDataType"/>\n <xs:complexType name="ListOfSampleInfoDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:SampleInfoDataType" name="SampleInfoDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfSampleInfoDataType" name="ListOfSampleInfoDataType" nillable="true"/>\n <xs:complexType name="StatisticResultContentDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="ResultKey"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="ItemCount"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="MeanValue"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="StandardDeviation"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="CoefficientOfVariation"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="MinValue"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="MaxValue"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="ConfidenceInterval95"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:StatisticResultContentDataType" name="StatisticResultContentDataType"/>\n <xs:complexType name="ListOfStatisticResultContentDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:StatisticResultContentDataType" name="StatisticResultContentDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfStatisticResultContentDataType" name="ListOfStatisticResultContentDataType" nillable="true"/>\n <xs:complexType name="StatisticResultContentWithUnitsDataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="tns:StatisticResultContentDataType">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:EUInformation" name="UnitItemCount"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:EUInformation" name="UnitMeanValue"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:EUInformation" name="UnitStandardDeviation"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:EUInformation" name="UnitCoefficientOfVariation"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:EUInformation" name="UnitMinValue"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:EUInformation" name="UnitMaxValue"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:EUInformation" name="UnitConfidenceInterval"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:StatisticResultContentWithUnitsDataType" name="StatisticResultContentWithUnitsDataType"/>\n <xs:complexType name="ListOfStatisticResultContentWithUnitsDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:StatisticResultContentWithUnitsDataType" name="StatisticResultContentWithUnitsDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfStatisticResultContentWithUnitsDataType" name="ListOfStatisticResultContentWithUnitsDataType" nillable="true"/>\n <xs:complexType name="TestNumDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="TestProcedureId"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="NumberOfTests"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:TestNumDataType" name="TestNumDataType"/>\n <xs:complexType name="ListOfTestNumDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:TestNumDataType" name="TestNumDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfTestNumDataType" name="ListOfTestNumDataType" nillable="true"/>\n <xs:complexType name="TestProcedureIdDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" type="xs:unsignedInt" name="EncodingMask"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="TestProcedureId"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="Description"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfString" name="ProcedureReferences"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:boolean" name="IsProcedureLicensed"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:TestProcedureIdDataType" name="TestProcedureIdDataType"/>\n <xs:complexType name="ListOfTestProcedureIdDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:TestProcedureIdDataType" name="TestProcedureIdDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfTestProcedureIdDataType" name="ListOfTestProcedureIdDataType" nillable="true"/>\n</xs:schema>\n',
)
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=ttd;i=6121",
    browseName="ns=machinery_result;ResultMetaData",
    references=[
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=ttd;i=6122", browseName="ns=ttd;CanBeDeleted", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1), "i=24136"),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ttd;i=6123", browseName="ns=machinery_result;CreationTime", dataType=ns0.datatypes.UtcTime, accessLevel=3, userAccessLevel=1
            ),
            "i=24136",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=ttd;i=6124", browseName="ns=machinery_result;HasTransferableDataOnFile", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
            ),
            "i=24136",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=ttd;i=6125", browseName="ns=machinery_result;IsPartial", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1), "i=24136"
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=ttd;i=6126", browseName="ns=ttd;JobOrder", dataType=ttd_datypes.JobOrderDataType, accessLevel=3, userAccessLevel=1),
            "i=24136",
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=ttd;i=6127", browseName="ns=ttd;ProductInstanceUri", dataType=o6.String, accessLevel=3, userAccessLevel=1), "i=24136"
        ),
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=ttd;i=6128", browseName="ns=ttd;SampleId", dataType=o6.String, accessLevel=3, userAccessLevel=1), "i=24136"),
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=ttd;i=6129", browseName="ns=ttd;TesterJobId", dataType=o6.String, accessLevel=3, userAccessLevel=1), "i=24136"),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=ttd;i=6130", browseName="ns=ttd;TesterSampleResultId", dataType=o6.String, accessLevel=3, userAccessLevel=1), "i=24136"
        ),
    ],
    dataType=machinery_result.datatypes.ResultMetaDataType,
    value=machinery_result.datatypes.ResultMetaDataType(
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
)
ttd_vartypes.TTDResultType(
    nodeId="ns=ttd;i=6120",
    browseName="ns=machinery_result;<ResultVariable>",
    modellingRule="OptionalPlaceholder",
    references=[o6.reference(o6.ns["ns=ttd;i=6121"], "i=24136")],
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
    accessLevel=3,
    userAccessLevel=1,
)
ns0.objtypes.FolderType(nodeId="ns=ttd;i=5042", browseName="ns=machinery_result;Results", modellingRule="Mandatory", references=[o6.hasComponent(o6.ns["ns=ttd;i=6120"])])
o6.reference(ttd_objtypes.TTDResultManagementType, ns0.reftypes.HasComponent, o6.ns["ns=ttd;i=5042"])
machinery.objtypes.MachineIdentificationType(
    nodeId="ns=ttd;i=5044",
    browseName="ns=di;Identification",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ttd;i=6132",
                browseName="ns=di;ProductInstanceUri",
                description="A globally unique resource identifier provided by the manufacturer of the machine",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ttd;i=6133",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ttd;i=6134",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(ttd_objtypes.TextileTestingDeviceType, ns0.reftypes.HasAddIn, o6.ns["ns=ttd;i=5044"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=ttd;i=6136",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ttd;i=6137", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
machinery.objtypes.MachineryItemState_StateMachineType(nodeId="ns=ttd;i=5055", browseName="ns=machinery;MachineryItemState", references=[o6.hasComponent(o6.ns["ns=ttd;i=6136"])])
ttd_objtypes.MachineStatisticsType(
    nodeId="ns=ttd;i=5049",
    browseName="ns=ttd;MachineStatistics",
    modellingRule="Mandatory",
    references=[
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=ttd;i=6141", browseName="ns=ttd;TotalExecutingTime", dataType=ns0.datatypes.Duration), "ns=ia;i=4002"),
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=ttd;i=6142", browseName="ns=ttd;TotalNotAvailableTime", dataType=ns0.datatypes.Duration), "ns=ia;i=4002"),
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=ttd;i=6143", browseName="ns=ttd;TotalNotExecutingTime", dataType=ns0.datatypes.Duration), "ns=ia;i=4002"),
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=ttd;i=6144", browseName="ns=ttd;TotalOutOfServiceTime", dataType=ns0.datatypes.Duration), "ns=ia;i=4002"),
    ],
)
o6.reference(ttd_objtypes.TextileTestingDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=ttd;i=5049"])
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashTTDSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=ttd;i=5054",
    browseName="ns=ttd;http://opcfoundation.org/UA/TTD/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ttd;i=6147", browseName="IsNamespaceSubset", dataType=o6.Boolean, value=False)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ttd;i=6148", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2025-03-01T00:00:00Z"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ttd;i=6149", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/TTD/")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ttd;i=6150", browseName="NamespaceVersion", dataType=o6.String, value="1.0.0")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ttd;i=6151", browseName="StaticNodeIdTypes", dataType=ns0.datatypes.IdType, valueRank=1, arrayDimensions=[1], value=[ns0.datatypes.IdType.NUMERIC]
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=ttd;i=6152", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ttd;i=6153", browseName="StaticStringNodeIdPattern", dataType=o6.String)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)


ns0.vartypes.PropertyType(
    nodeId="ns=ttd;i=6012",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ttd;i=7008",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="JobOrderID", dataType=o6.String, valueRank=-1, description=o6.LocalizedText("Contains an ID of the job order, as specified by the method caller.")
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ttd;i=6013",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ttd;i=7008",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="JobResponse",
            dataType=o6.NodeId("ns=isa95_jobcontrol_v2;i=3013"),
            valueRank=-1,
            description=o6.LocalizedText(
                "Contains information about the execution of a job order, such as the current status of the job, actual material consumed, actual material produced, actual equipment used, and job specific data."
            ),
        ),
        ns0.datatypes.Argument(name="ReturnStatus", dataType=o6.UInt64, valueRank=-1, description=o6.LocalizedText("Returns the status of the method execution.")),
    ],
)
o6.call(
    nodeId="ns=ttd;i=7008",
    browseName="ns=isa95_jobcontrol_v2;RequestJobResponseByJobOrderID",
    inputArgs=o6.hasProperty(o6.ns["ns=ttd;i=6012"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ttd;i=6013"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ttd;i=6113",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ttd;i=7010",
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
    nodeId="ns=ttd;i=6114",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ttd;i=7010",
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
o6.call(nodeId="ns=ttd;i=7010", browseName="GenerateFileForRead", inputArgs=o6.hasProperty(o6.ns["ns=ttd;i=6113"]), outputArgs=o6.hasProperty(o6.ns["ns=ttd;i=6114"]))

ns0.vartypes.PropertyType(
    nodeId="ns=ttd;i=6116",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ttd;i=7011",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ttd;i=6117",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ttd;i=7011",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="CompletionStateMachine", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(nodeId="ns=ttd;i=7011", browseName="CloseAndCommit", inputArgs=o6.hasProperty(o6.ns["ns=ttd;i=6116"]), outputArgs=o6.hasProperty(o6.ns["ns=ttd;i=6117"]))

ns0.vartypes.PropertyType(
    nodeId="ns=ttd;i=6118",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ttd;i=7012",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="GenerateOptions", dataType=ns0.datatypes.BaseDataType, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ttd;i=6119",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ttd;i=7012",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileNodeId", dataType=o6.NodeId, valueRank=-1), ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=ttd;i=7012", browseName="GenerateFileForWrite", inputArgs=o6.hasProperty(o6.ns["ns=ttd;i=6118"]), outputArgs=o6.hasProperty(o6.ns["ns=ttd;i=6119"]))

machinery_result.objtypes.ResultTransferType(
    nodeId="ns=ttd;i=5043",
    browseName="ns=machinery_result;ResultTransfer",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ttd;i=6115", browseName="ClientProcessingTimeout", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(o6.ns["ns=ttd;i=7010"]),
        o6.hasComponent(o6.ns["ns=ttd;i=7011"]),
        o6.hasComponent(o6.ns["ns=ttd;i=7012"]),
    ],
)
o6.reference(ttd_objtypes.TTDResultManagementType, ns0.reftypes.HasComponent, o6.ns["ns=ttd;i=5043"])


ns0.vartypes.PropertyType(
    nodeId="ns=ttd;i=6014",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ttd;i=7013",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="JobOrderState",
            dataType=o6.NodeId("ns=isa95_jobcontrol_v2;i=3006"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText(
                "Contains a job status of the JobResponse to be returned. The array shall provide at least one entry representing the top level state and potentially additional entries representing substates. The first entry shall be the top level entry, having the BrowsePath set to null. The order of the substates is not defined."
            ),
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ttd;i=6015",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ttd;i=7013",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="JobResponses",
            dataType=o6.NodeId("ns=isa95_jobcontrol_v2;i=3013"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText(
                "Contains a list of information about the execution of a job order, such as the current status of the job, actual material consumed, actual material produced, actual equipment used, and job specific data. "
            ),
        ),
        ns0.datatypes.Argument(name="ReturnStatus", dataType=o6.UInt64, valueRank=-1, description=o6.LocalizedText("Returns the status of the method execution.")),
    ],
)
o6.call(
    nodeId="ns=ttd;i=7013",
    browseName="ns=isa95_jobcontrol_v2;RequestJobResponseByJobOrderState",
    inputArgs=o6.hasProperty(o6.ns["ns=ttd;i=6014"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ttd;i=6015"]),
)

isa95_jobcontrol_v2.objtypes.ISA95JobResponseProviderObjectType(
    nodeId="ns=ttd;i=5037", browseName="ns=machinery_jobs;JobOrderResults", references=[o6.hasComponent(o6.ns["ns=ttd;i=7008"]), o6.hasComponent(o6.ns["ns=ttd;i=7013"])]
)
machinery_jobs.objtypes.JobManagementType(
    nodeId="ns=ttd;i=5035", browseName="ns=machinery_jobs;JobManagement", references=[o6.hasComponent(o6.ns["ns=ttd;i=5036"]), o6.hasComponent(o6.ns["ns=ttd;i=5037"])]
)


ns0.vartypes.PropertyType(
    nodeId="ns=ttd;i=6145",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ttd;i=7014",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="RecipeIds", dataType=o6.NodeId("ns=ttd;i=3003"), valueRank=1, arrayDimensions=[0])],
)
o6.call(nodeId="ns=ttd;i=7014", browseName="ns=ttd;GetRecipeIds", outputArgs=o6.hasProperty(o6.ns["ns=ttd;i=6145"]))

ttd_objtypes.RecipeManagementType(
    nodeId="ns=ttd;i=5051",
    browseName="ns=ttd;RecipeManagement",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=ttd;i=6017", browseName="ns=ttd;RecipeIds", dataType=ttd_datypes.RecipeIdDataType, valueRank=1, arrayDimensions=[0], accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=ttd;i=7014"]),
    ],
)
o6.reference(ttd_objtypes.TextileTestingDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=ttd;i=5051"])


ns0.vartypes.PropertyType(
    nodeId="ns=ttd;i=6095",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ttd;i=7019",
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
    nodeId="ns=ttd;i=6096",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ttd;i=7019",
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
            dataType=o6.NodeId("ns=machinery_result;i=3008"),
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
o6.call(nodeId="ns=ttd;i=7019", browseName="ns=machinery_result;GetResultById", inputArgs=o6.hasProperty(o6.ns["ns=ttd;i=6095"]), outputArgs=o6.hasProperty(o6.ns["ns=ttd;i=6096"]))

ns0.vartypes.PropertyType(
    nodeId="ns=ttd;i=6098",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ttd;i=7020",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ttd;i=6099",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ttd;i=7020",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="CompletionStateMachine", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(nodeId="ns=ttd;i=7020", browseName="CloseAndCommit", inputArgs=o6.hasProperty(o6.ns["ns=ttd;i=6098"]), outputArgs=o6.hasProperty(o6.ns["ns=ttd;i=6099"]))

ns0.vartypes.PropertyType(
    nodeId="ns=ttd;i=6100",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ttd;i=7021",
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
    nodeId="ns=ttd;i=6101",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ttd;i=7021",
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
o6.call(nodeId="ns=ttd;i=7021", browseName="GenerateFileForRead", inputArgs=o6.hasProperty(o6.ns["ns=ttd;i=6100"]), outputArgs=o6.hasProperty(o6.ns["ns=ttd;i=6101"]))

ns0.vartypes.PropertyType(
    nodeId="ns=ttd;i=6102",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ttd;i=7022",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="GenerateOptions", dataType=ns0.datatypes.BaseDataType, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ttd;i=6103",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ttd;i=7022",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileNodeId", dataType=o6.NodeId, valueRank=-1), ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=ttd;i=7022", browseName="GenerateFileForWrite", inputArgs=o6.hasProperty(o6.ns["ns=ttd;i=6102"]), outputArgs=o6.hasProperty(o6.ns["ns=ttd;i=6103"]))

machinery_result.objtypes.ResultTransferType(
    nodeId="ns=ttd;i=5047",
    browseName="ns=machinery_result;ResultTransfer",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ttd;i=6097", browseName="ClientProcessingTimeout", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(o6.ns["ns=ttd;i=7020"]),
        o6.hasComponent(o6.ns["ns=ttd;i=7021"]),
        o6.hasComponent(o6.ns["ns=ttd;i=7022"]),
    ],
)
ttd_objtypes.TTDResultManagementType(
    nodeId="ns=ttd;i=5041",
    browseName="ns=machinery_result;ResultManagement",
    references=[
        o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=ttd;i=5046", browseName="ns=machinery_result;Results")),
        o6.hasComponent(o6.ns["ns=ttd;i=5047"]),
        o6.hasComponent(o6.ns["ns=ttd;i=7019"]),
    ],
)
ns0.objtypes.FolderType(
    nodeId="ns=ttd;i=5045",
    browseName="ns=machinery;MachineryBuildingBlocks",
    modellingRule="Mandatory",
    references=[o6.hasAddIn(o6.ns["ns=ttd;i=5001"]), o6.hasAddIn(o6.ns["ns=ttd;i=5035"]), o6.hasAddIn(o6.ns["ns=ttd;i=5041"]), o6.hasAddIn(o6.ns["ns=ttd;i=5055"])],
)
o6.reference(ttd_objtypes.TextileTestingDeviceType, ns0.reftypes.HasAddIn, o6.ns["ns=ttd;i=5045"])
o6.reference(o6.ns["ns=ttd;i=5045"], "i=17604", o6.ns["ns=ttd;i=5044"])


del Any, TYPE_CHECKING, uuid, o6, di, ia, isa95_jobcontrol_v2, machine_tool, machinery, machinery_jobs, machinery_result, ns0, ttd_datypes, ttd_vartypes, ttd_objtypes
