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
from . import vartypes as machine_vision_vartypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(nodeId="ns=machine_vision;i=1008", browseName="ns=machine_vision;RecipeFolderType", displayName="RecipeFolderType")
class RecipeFolderType(ns0.objtypes.FolderType):
    langleRecipeRangle: RecipeType | None


@o6.objecttype(nodeId="ns=machine_vision;i=1016", browseName="ns=machine_vision;ResultFolderType", displayName="ResultFolderType")
class ResultFolderType(ns0.objtypes.FolderType):
    langleResultVariableRangle: machine_vision_vartypes.ResultType | None


@o6.objecttype(nodeId="ns=machine_vision;i=1018", browseName="ns=machine_vision;StateChangedEventType", displayName="StateChangedEventType")
class StateChangedEventType(ns0.objtypes.TransitionEventType):
    pass


@o6.objecttype(nodeId="ns=machine_vision;i=1019", browseName="ns=machine_vision;ErrorEventType", displayName="ErrorEventType")
class ErrorEventType(ns0.objtypes.TransitionEventType):
    pass


@o6.objecttype(nodeId="ns=machine_vision;i=1020", browseName="ns=machine_vision;ErrorResolvedEventType", displayName="ErrorResolvedEventType")
class ErrorResolvedEventType(ns0.objtypes.TransitionEventType):
    pass


@o6.objecttype(nodeId="ns=machine_vision;i=1029", browseName="ns=machine_vision;LeaveStepSequenceEventType", displayName="LeaveStepSequenceEventType")
class LeaveStepSequenceEventType(ns0.objtypes.BaseEventType):
    pass


@o6.objecttype(nodeId="ns=machine_vision;i=1003", browseName="ns=machine_vision;VisionSystemType", displayName="VisionSystemType")
class VisionSystemType(ns0.objtypes.BaseObjectType):
    configurationManagement: ConfigurationManagementType | None
    diagnosticLevel: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_vision;i=6048", browseName="ns=machine_vision;DiagnosticLevel", dataType=o6.UInt16, accessLevel=3, userAccessLevel=1)
    )
    recipeManagement: RecipeManagementType | None
    resultManagement: ResultManagementType | None
    safetyStateManagement: SafetyStateManagementType | None
    systemState: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=machine_vision;i=6049",
            browseName="ns=machine_vision;SystemState",
            dataType=machine_vision_datypes.SystemStateDescriptionDataType,
            value=machine_vision_datypes.SystemStateDescriptionDataType(state=machine_vision_datypes.SystemStateDataType.NST_6, stateDescription=None),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    visionStateMachine: VisionStateMachineType


@o6.objecttype(nodeId="ns=machine_vision;i=1030", browseName="ns=machine_vision;VisionSafetyEventType", displayName="VisionSafetyEventType")
class VisionSafetyEventType(ns0.objtypes.BaseEventType):
    visionSafetyInformation: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6050", browseName="ns=machine_vision;VisionSafetyInformation", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    visionSafetyTriggered: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6051", browseName="ns=machine_vision;VisionSafetyTriggered", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=machine_vision;i=1011", browseName="ns=machine_vision;ConfigurationFolderType", displayName="ConfigurationFolderType")
class ConfigurationFolderType(ns0.objtypes.FolderType):
    langleConfigurationRangle: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=machine_vision;i=6120",
            browseName="ns=machine_vision;<Configuration>",
            modellingRule="OptionalPlaceholder",
            dataType=machine_vision_datypes.ConfigurationDataType,
            value=machine_vision_datypes.ConfigurationDataType(
                hasTransferableDataOnFile=None,
                externalId=None,
                internalId=machine_vision_datypes.ConfigurationIdDataType(id="", version=None, hash=None, hashAlgorithm=None, description=None),
                lastModified=o6.DateTime("1900-01-01T00:00:00Z"),
            ),
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(nodeId="ns=machine_vision;i=1013", browseName="ns=machine_vision;JobStartedEventType", displayName="JobStartedEventType")
class JobStartedEventType(ns0.objtypes.BaseEventType):
    jobId: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision;i=6141",
            browseName="ns=machine_vision;JobId",
            dataType=machine_vision_datypes.JobIdDataType,
            value=machine_vision_datypes.JobIdDataType(id=""),
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(nodeId="ns=machine_vision;i=1022", browseName="ns=machine_vision;RecipePreparedEventType", displayName="RecipePreparedEventType")
class RecipePreparedEventType(ns0.objtypes.BaseEventType):
    externalId: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision;i=6291", browseName="ns=machine_vision;ExternalId", dataType=machine_vision_datypes.RecipeIdExternalDataType, accessLevel=3, userAccessLevel=1
        )
    )
    internalId: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision;i=6140", browseName="ns=machine_vision;InternalId", dataType=machine_vision_datypes.RecipeIdInternalDataType, accessLevel=3, userAccessLevel=1
        )
    )
    productId: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision;i=6292",
            browseName="ns=machine_vision;ProductId",
            dataType=machine_vision_datypes.ProductIdDataType,
            value=machine_vision_datypes.ProductIdDataType(id="", description=None),
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(nodeId="ns=machine_vision;i=1023", browseName="ns=machine_vision;ReadyEventType", displayName="ReadyEventType")
class ReadyEventType(ns0.objtypes.BaseEventType):
    jobId: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision;i=6294",
            browseName="ns=machine_vision;JobId",
            dataType=machine_vision_datypes.JobIdDataType,
            value=machine_vision_datypes.JobIdDataType(id=""),
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(nodeId="ns=machine_vision;i=1024", browseName="ns=machine_vision;ResultReadyEventType", displayName="ResultReadyEventType")
class ResultReadyEventType(ns0.objtypes.BaseEventType):
    creationTime: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6303", browseName="ns=machine_vision;CreationTime", dataType=ns0.datatypes.UtcTime, accessLevel=3, userAccessLevel=1)
    )
    externalConfigurationId: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision;i=6045",
            browseName="ns=machine_vision;ExternalConfigurationId",
            dataType=machine_vision_datypes.ConfigurationIdDataType,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    externalRecipeId: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision;i=6301",
            browseName="ns=machine_vision;ExternalRecipeId",
            dataType=machine_vision_datypes.RecipeIdExternalDataType,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    internalConfigurationId: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision;i=6142",
            browseName="ns=machine_vision;InternalConfigurationId",
            dataType=machine_vision_datypes.ConfigurationIdDataType,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    internalRecipeId: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision;i=6302",
            browseName="ns=machine_vision;InternalRecipeId",
            dataType=machine_vision_datypes.RecipeIdInternalDataType,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    isPartial: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6296", browseName="ns=machine_vision;IsPartial", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
    )
    isSimulated: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6297", browseName="ns=machine_vision;IsSimulated", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
    )
    jobId: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision;i=6300",
            browseName="ns=machine_vision;JobId",
            dataType=machine_vision_datypes.JobIdDataType,
            value=machine_vision_datypes.JobIdDataType(id=""),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    measId: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision;i=6299",
            browseName="ns=machine_vision;MeasId",
            dataType=machine_vision_datypes.MeasIdDataType,
            value=machine_vision_datypes.MeasIdDataType(id="", description=None),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    partId: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision;i=6304",
            browseName="ns=machine_vision;PartId",
            dataType=machine_vision_datypes.PartIdDataType,
            value=machine_vision_datypes.PartIdDataType(id="", description=None),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    processingTimes: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision;i=6305",
            browseName="ns=machine_vision;ProcessingTimes",
            dataType=machine_vision_datypes.ProcessingTimesDataType,
            value=machine_vision_datypes.ProcessingTimesDataType(
                startTime=o6.DateTime("1900-01-01T00:00:00Z"), endTime=o6.DateTime("1900-01-01T00:00:00Z"), acquisitionDuration=None, processingDuration=None
            ),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    productId: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision;i=6143",
            browseName="ns=machine_vision;ProductId",
            dataType=machine_vision_datypes.ProductIdDataType,
            value=machine_vision_datypes.ProductIdDataType(id="", description=None),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    resultContent: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision;i=6306", browseName="ns=machine_vision;ResultContent", valueRank=1, arrayDimensions=[0], accessLevel=3, userAccessLevel=1
        )
    )
    resultId: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision;i=6295",
            browseName="ns=machine_vision;ResultId",
            dataType=machine_vision_datypes.ResultIdDataType,
            value=machine_vision_datypes.ResultIdDataType(id=""),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    resultState: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision;i=6298", browseName="ns=machine_vision;ResultState", dataType=machine_vision_datypes.ResultStateDataType, accessLevel=3, userAccessLevel=1
        )
    )


@o6.objecttype(nodeId="ns=machine_vision;i=1025", browseName="ns=machine_vision;AcquisitionDoneEventType", displayName="AcquisitionDoneEventType")
class AcquisitionDoneEventType(ns0.objtypes.BaseEventType):
    jobId: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision;i=6308",
            browseName="ns=machine_vision;JobId",
            dataType=machine_vision_datypes.JobIdDataType,
            value=machine_vision_datypes.JobIdDataType(id=""),
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(nodeId="ns=machine_vision;i=1027", browseName="ns=machine_vision;EnterStepSequenceEventType", displayName="EnterStepSequenceEventType")
class EnterStepSequenceEventType(ns0.objtypes.BaseEventType):
    steps: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6322", browseName="ns=machine_vision;Steps", dataType=o6.Int32, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=machine_vision;i=1028", browseName="ns=machine_vision;NextStepEventType", displayName="NextStepEventType")
class NextStepEventType(ns0.objtypes.BaseEventType):
    step: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6324", browseName="ns=machine_vision;Step", dataType=o6.Int32, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=machine_vision;i=1033", browseName="ns=machine_vision;VisionConditionType", displayName="VisionConditionType", isAbstract=True)
class VisionConditionType(ns0.objtypes.AcknowledgeableConditionType):
    blockReaction: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6206", browseName="ns=machine_vision;BlockReaction", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
    )
    causePath: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6207", browseName="ns=machine_vision;CausePath", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    errorCode: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6208", browseName="ns=machine_vision;ErrorCode", dataType=o6.UInt64, accessLevel=3, userAccessLevel=1)
    )
    errorString: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6283", browseName="ns=machine_vision;ErrorString", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    externalConfigurationId: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision;i=6347",
            browseName="ns=machine_vision;ExternalConfigurationId",
            dataType=machine_vision_datypes.ConfigurationIdDataType,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    externalRecipeId: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision;i=6346",
            browseName="ns=machine_vision;ExternalRecipeId",
            dataType=machine_vision_datypes.RecipeIdExternalDataType,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    internalConfigurationId: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision;i=6192",
            browseName="ns=machine_vision;InternalConfigurationId",
            dataType=machine_vision_datypes.ConfigurationIdDataType,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    internalRecipeId: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision;i=6321",
            browseName="ns=machine_vision;InternalRecipeId",
            dataType=machine_vision_datypes.RecipeIdInternalDataType,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    jobId: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision;i=6343",
            browseName="ns=machine_vision;JobId",
            dataType=machine_vision_datypes.JobIdDataType,
            value=machine_vision_datypes.JobIdDataType(id=""),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    measId: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision;i=6344",
            browseName="ns=machine_vision;MeasId",
            dataType=machine_vision_datypes.MeasIdDataType,
            value=machine_vision_datypes.MeasIdDataType(id="", description=None),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    partId: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision;i=6307",
            browseName="ns=machine_vision;PartId",
            dataType=machine_vision_datypes.PartIdDataType,
            value=machine_vision_datypes.PartIdDataType(id="", description=None),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    productId: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision;i=6323",
            browseName="ns=machine_vision;ProductId",
            dataType=machine_vision_datypes.ProductIdDataType,
            value=machine_vision_datypes.ProductIdDataType(id="", description=None),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    resultId: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision;i=6345",
            browseName="ns=machine_vision;ResultId",
            dataType=machine_vision_datypes.ResultIdDataType,
            value=machine_vision_datypes.ResultIdDataType(id=""),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    stopReaction: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6293", browseName="ns=machine_vision;StopReaction", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=machine_vision;i=1034", browseName="ns=machine_vision;VisionWarningConditionType", displayName="VisionWarningConditionType")
class VisionWarningConditionType(VisionConditionType):
    pass


@o6.objecttype(nodeId="ns=machine_vision;i=1035", browseName="ns=machine_vision;VisionErrorConditionType", displayName="VisionErrorConditionType")
class VisionErrorConditionType(VisionConditionType):
    pass


@o6.objecttype(nodeId="ns=machine_vision;i=1036", browseName="ns=machine_vision;VisionPersistentErrorConditionType", displayName="VisionPersistentErrorConditionType")
class VisionPersistentErrorConditionType(VisionConditionType):
    pass


@o6.objecttype(nodeId="ns=machine_vision;i=1015", browseName="ns=machine_vision;VisionEventType", displayName="VisionEventType", isAbstract=True)
class VisionEventType(ns0.objtypes.BaseEventType):
    causePath: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6193", browseName="ns=machine_vision;CausePath", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    externalConfigurationId: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision;i=6550",
            browseName="ns=machine_vision;ExternalConfigurationId",
            dataType=machine_vision_datypes.ConfigurationIdDataType,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    externalRecipeId: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision;i=6195",
            browseName="ns=machine_vision;ExternalRecipeId",
            dataType=machine_vision_datypes.RecipeIdExternalDataType,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    internalConfigurationId: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision;i=6200",
            browseName="ns=machine_vision;InternalConfigurationId",
            dataType=machine_vision_datypes.ConfigurationIdDataType,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    internalRecipeId: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision;i=6198",
            browseName="ns=machine_vision;InternalRecipeId",
            dataType=machine_vision_datypes.RecipeIdInternalDataType,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    jobId: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision;i=6203",
            browseName="ns=machine_vision;JobId",
            dataType=machine_vision_datypes.JobIdDataType,
            value=machine_vision_datypes.JobIdDataType(id=""),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    measId: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision;i=6194",
            browseName="ns=machine_vision;MeasId",
            dataType=machine_vision_datypes.MeasIdDataType,
            value=machine_vision_datypes.MeasIdDataType(id="", description=None),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    partId: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision;i=6201",
            browseName="ns=machine_vision;PartId",
            dataType=machine_vision_datypes.PartIdDataType,
            value=machine_vision_datypes.PartIdDataType(id="", description=None),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    productId: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision;i=6199",
            browseName="ns=machine_vision;ProductId",
            dataType=machine_vision_datypes.ProductIdDataType,
            value=machine_vision_datypes.ProductIdDataType(id="", description=None),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    resultId: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision;i=6204",
            browseName="ns=machine_vision;ResultId",
            dataType=machine_vision_datypes.ResultIdDataType,
            value=machine_vision_datypes.ResultIdDataType(id=""),
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(nodeId="ns=machine_vision;i=1037", browseName="ns=machine_vision;VisionDiagnosticInfoEventType", displayName="VisionDiagnosticInfoEventType")
class VisionDiagnosticInfoEventType(VisionEventType):
    pass


@o6.objecttype(nodeId="ns=machine_vision;i=1038", browseName="ns=machine_vision;VisionInformationEventType", displayName="VisionInformationEventType")
class VisionInformationEventType(VisionEventType):
    pass


@o6.objecttype(nodeId="ns=machine_vision;i=1010", browseName="ns=machine_vision;ProductFolderType", displayName="ProductFolderType")
class ProductFolderType(ns0.objtypes.FolderType):
    langleProductRangle: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=machine_vision;i=6621",
            browseName="ns=machine_vision;<Product>",
            modellingRule="OptionalPlaceholder",
            dataType=machine_vision_datypes.ProductDataType,
            accessLevel=3,
            userAccessLevel=1,
        )
    )


ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6024",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7007",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="ResultId", dataType=o6.NodeId("ns=machine_vision;i=3021"), valueRank=-1),
        ns0.datatypes.Argument(name="Timeout", dataType=o6.Int32, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6025",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7007",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[17],
    value=[
        ns0.datatypes.Argument(name="HasTransferableDataOnFile", dataType=o6.Boolean, valueRank=-1),
        ns0.datatypes.Argument(name="ResultHandle", dataType=o6.NodeId("ns=machine_vision;i=3018"), valueRank=-1),
        ns0.datatypes.Argument(name="IsPartial", dataType=o6.Boolean, valueRank=-1),
        ns0.datatypes.Argument(name="IsSimulated", dataType=o6.Boolean, valueRank=-1),
        ns0.datatypes.Argument(name="ResultState", dataType=o6.NodeId("ns=machine_vision;i=3009"), valueRank=-1),
        ns0.datatypes.Argument(name="MeasId", dataType=o6.NodeId("ns=machine_vision;i=3015"), valueRank=-1),
        ns0.datatypes.Argument(name="PartId", dataType=o6.NodeId("ns=machine_vision;i=3004"), valueRank=-1),
        ns0.datatypes.Argument(name="ExternalRecipeId", dataType=o6.NodeId("ns=machine_vision;i=3002"), valueRank=-1),
        ns0.datatypes.Argument(name="InternalRecipeId", dataType=o6.NodeId("ns=machine_vision;i=3013"), valueRank=-1),
        ns0.datatypes.Argument(name="ProductId", dataType=o6.NodeId("ns=machine_vision;i=3003"), valueRank=-1),
        ns0.datatypes.Argument(name="ExternalConfigurationId", dataType=o6.NodeId("ns=machine_vision;i=3008"), valueRank=-1),
        ns0.datatypes.Argument(name="InternalConfigurationId", dataType=o6.NodeId("ns=machine_vision;i=3008"), valueRank=-1),
        ns0.datatypes.Argument(name="JobId", dataType=o6.NodeId("ns=machine_vision;i=3016"), valueRank=-1),
        ns0.datatypes.Argument(name="CreationTime", dataType=ns0.datatypes.UtcTime, valueRank=-1),
        ns0.datatypes.Argument(name="ProcessingTimes", dataType=o6.NodeId("ns=machine_vision;i=3005"), valueRank=-1),
        ns0.datatypes.Argument(name="ResultContent", dataType=ns0.datatypes.BaseDataType, valueRank=1),
        ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1),
    ],
)
o6.call(
    nodeId="ns=machine_vision;i=7007",
    browseName="ns=machine_vision;GetResultComponentsById",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6024"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6025"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6086",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7009",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0.datatypes.Argument(name="MeasId", dataType=o6.NodeId("ns=machine_vision;i=3015"), valueRank=-1),
        ns0.datatypes.Argument(name="PartId", dataType=o6.NodeId("ns=machine_vision;i=3004"), valueRank=-1),
        ns0.datatypes.Argument(name="RecipeId", dataType=o6.NodeId("ns=machine_vision;i=3002"), valueRank=-1),
        ns0.datatypes.Argument(name="ProductId", dataType=o6.NodeId("ns=machine_vision;i=3003"), valueRank=-1),
        ns0.datatypes.Argument(name="Parameters", dataType=ns0.datatypes.BaseDataType, valueRank=1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6087",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7009",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="JobId", dataType=o6.NodeId("ns=machine_vision;i=3016"), valueRank=-1),
        ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1),
    ],
)
o6.call(
    nodeId="ns=machine_vision;i=7009",
    browseName="ns=machine_vision;StartContinuous",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6086"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6087"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6144",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7013",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="ExternalId", dataType=o6.NodeId("ns=machine_vision;i=3002"), valueRank=-1),
        ns0.datatypes.Argument(name="ProductId", dataType=o6.NodeId("ns=machine_vision;i=3003"), valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6145",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7013",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0.datatypes.Argument(name="InternalId", dataType=o6.NodeId("ns=machine_vision;i=3013"), valueRank=-1),
        ns0.datatypes.Argument(name="Recipe", dataType=o6.NodeId, valueRank=-1),
        ns0.datatypes.Argument(name="Product", dataType=o6.NodeId, valueRank=-1),
        ns0.datatypes.Argument(name="TransferRequired", dataType=o6.Boolean, valueRank=-1),
        ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1),
    ],
)
o6.call(
    nodeId="ns=machine_vision;i=7013",
    browseName="ns=machine_vision;AddRecipe",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6144"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6145"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6156",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7014",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[6],
    value=[
        ns0.datatypes.Argument(name="ExternalId", dataType=o6.NodeId("ns=machine_vision;i=3002"), valueRank=-1),
        ns0.datatypes.Argument(name="ProductId", dataType=o6.NodeId("ns=machine_vision;i=3003"), valueRank=-1),
        ns0.datatypes.Argument(name="IsPrepared", dataType=o6.NodeId("ns=machine_vision;i=3014"), valueRank=-1),
        ns0.datatypes.Argument(name="MaxResults", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="StartIndex", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="Timeout", dataType=o6.Int32, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6157",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7014",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0.datatypes.Argument(name="IsComplete", dataType=o6.Boolean, valueRank=-1),
        ns0.datatypes.Argument(name="ResultCount", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="RecipeHandle", dataType=o6.NodeId("ns=machine_vision;i=3018"), valueRank=-1),
        ns0.datatypes.Argument(name="RecipeList", dataType=o6.NodeId("ns=machine_vision;i=3013"), valueRank=1),
        ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1),
    ],
)
o6.call(
    nodeId="ns=machine_vision;i=7014",
    browseName="ns=machine_vision;GetRecipeListFiltered",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6156"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6157"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6148",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7015",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="ExternalId", dataType=o6.NodeId("ns=machine_vision;i=3002"), valueRank=-1),
        ns0.datatypes.Argument(name="InternalIdIn", dataType=o6.NodeId("ns=machine_vision;i=3013"), valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6149",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7015",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="InternalIdOut", dataType=o6.NodeId("ns=machine_vision;i=3013"), valueRank=-1),
        ns0.datatypes.Argument(name="IsCompleted", dataType=o6.Boolean, valueRank=-1),
        ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1),
    ],
)
o6.call(
    nodeId="ns=machine_vision;i=7015",
    browseName="ns=machine_vision;PrepareRecipe",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6148"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6149"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6096",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7025",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ExternalId", dataType=o6.NodeId("ns=machine_vision;i=3008"), valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6097",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7025",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.Argument(name="InternalId", dataType=o6.NodeId("ns=machine_vision;i=3008"), valueRank=-1),
        ns0.datatypes.Argument(name="Configuration", dataType=o6.NodeId, valueRank=-1),
        ns0.datatypes.Argument(name="TransferRequired", dataType=o6.Boolean, valueRank=-1),
        ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1),
    ],
)
o6.call(
    nodeId="ns=machine_vision;i=7025",
    browseName="ns=machine_vision;AddConfiguration",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6096"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6097"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6209",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7026",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="ResultId", dataType=o6.NodeId("ns=machine_vision;i=3021"), valueRank=-1),
        ns0.datatypes.Argument(name="Timeout", dataType=o6.Int32, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6210",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7026",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="ResultHandle", dataType=o6.NodeId("ns=machine_vision;i=3018"), valueRank=-1),
        ns0.datatypes.Argument(name="Result", dataType=o6.NodeId("ns=machine_vision;i=3006"), valueRank=-1),
        ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1),
    ],
)
o6.call(
    nodeId="ns=machine_vision;i=7026",
    browseName="ns=machine_vision;GetResultById",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6209"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6210"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6100",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7041",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="InternalId", dataType=o6.NodeId("ns=machine_vision;i=3008"), valueRank=-1),
        ns0.datatypes.Argument(name="Timeout", dataType=o6.Int32, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6101",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7041",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="ConfigurationHandle", dataType=o6.NodeId("ns=machine_vision;i=3018"), valueRank=-1),
        ns0.datatypes.Argument(name="Configuration", dataType=o6.NodeId("ns=machine_vision;i=3007"), valueRank=-1),
        ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1),
    ],
)
o6.call(
    nodeId="ns=machine_vision;i=7041",
    browseName="ns=machine_vision;GetConfigurationById",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6100"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6101"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6222",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7043",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="SafetyTriggered", dataType=o6.Boolean, valueRank=-1), ns0.datatypes.Argument(name="SafetyInformation", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6223",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7043",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7043",
    browseName="ns=machine_vision;ReportSafetyState",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6222"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6223"]),
)


@o6.objecttype(nodeId="ns=machine_vision;i=1009", browseName="ns=machine_vision;SafetyStateManagementType", displayName="SafetyStateManagementType")
class SafetyStateManagementType(ns0.objtypes.BaseObjectType):
    reportSafetyState: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=machine_vision;i=7043"])
    visionSafetyInformation: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=machine_vision;i=6042", browseName="ns=machine_vision;VisionSafetyInformation", dataType=o6.String, accessLevel=3, userAccessLevel=1
        )
    )
    visionSafetyTriggered: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=machine_vision;i=6041", browseName="ns=machine_vision;VisionSafetyTriggered", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
        )
    )


ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6104",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7045",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="MaxResults", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="StartIndex", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="Timeout", dataType=o6.Int32, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6105",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7045",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0.datatypes.Argument(name="IsComplete", dataType=o6.Boolean, valueRank=-1),
        ns0.datatypes.Argument(name="ResultCount", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="ConfigurationHandle", dataType=o6.NodeId("ns=machine_vision;i=3018"), valueRank=-1),
        ns0.datatypes.Argument(name="ConfigurationList", dataType=o6.NodeId("ns=machine_vision;i=3007"), valueRank=1),
        ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1),
    ],
)
o6.call(
    nodeId="ns=machine_vision;i=7045",
    browseName="ns=machine_vision;GetConfigurationList",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6104"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6105"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6108",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7046",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ConfigurationHandle", dataType=o6.NodeId("ns=machine_vision;i=3018"), valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6109",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7046",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7046",
    browseName="ns=machine_vision;ReleaseConfigurationHandle",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6108"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6109"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6112",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7047",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="InternalId", dataType=o6.NodeId("ns=machine_vision;i=3008"), valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6113",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7047",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7047",
    browseName="ns=machine_vision;RemoveConfiguration",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6112"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6113"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6116",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7048",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="InternalId", dataType=o6.NodeId("ns=machine_vision;i=3008"), valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6117",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7048",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7048",
    browseName="ns=machine_vision;ActivateConfiguration",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6116"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6117"]),
)


@o6.objecttype(nodeId="ns=machine_vision;i=1006", browseName="ns=machine_vision;ConfigurationManagementType", displayName="ConfigurationManagementType")
class ConfigurationManagementType(ns0.objtypes.BaseObjectType):
    activateConfiguration: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=machine_vision;i=7048"])
    activeConfiguration: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=machine_vision;i=6132",
            browseName="ns=machine_vision;ActiveConfiguration",
            dataType=machine_vision_datypes.ConfigurationDataType,
            value=machine_vision_datypes.ConfigurationDataType(
                hasTransferableDataOnFile=None,
                externalId=None,
                internalId=machine_vision_datypes.ConfigurationIdDataType(id="", version=None, hash=None, hashAlgorithm=None, description=None),
                lastModified=o6.DateTime("1900-01-01T00:00:00Z"),
            ),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    addConfiguration: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=machine_vision;i=7025"])
    configurationTransfer: ConfigurationTransferType | None
    configurations: ConfigurationFolderType | None = o6.hasComponent(ConfigurationFolderType(nodeId="ns=machine_vision;i=5010", browseName="ns=machine_vision;Configurations"))
    getConfigurationById: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=machine_vision;i=7041"])
    getConfigurationList: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=machine_vision;i=7045"])
    releaseConfigurationHandle: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=machine_vision;i=7046"])
    removeConfiguration: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=machine_vision;i=7047"])


ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6152",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7055",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="ExternalId", dataType=o6.NodeId("ns=machine_vision;i=3002"), valueRank=-1),
        ns0.datatypes.Argument(name="InternalIdIn", dataType=o6.NodeId("ns=machine_vision;i=3013"), valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6153",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7055",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="InternalIdOut", dataType=o6.NodeId("ns=machine_vision;i=3013"), valueRank=-1),
        ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1),
    ],
)
o6.call(
    nodeId="ns=machine_vision;i=7055",
    browseName="ns=machine_vision;UnprepareRecipe",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6152"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6153"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6160",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7056",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="RecipeHandle", dataType=o6.NodeId("ns=machine_vision;i=3018"), valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6161",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7056",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7056",
    browseName="ns=machine_vision;ReleaseRecipeHandle",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6160"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6161"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6164",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7057",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ExternalId", dataType=o6.NodeId("ns=machine_vision;i=3002"), valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6165",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7057",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7057",
    browseName="ns=machine_vision;RemoveRecipe",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6164"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6165"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6169",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7058",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="GenerateOptions", dataType=o6.NodeId("ns=machine_vision;i=3022"), valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6170",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7058",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="FileNodeId", dataType=o6.NodeId, valueRank=-1),
        ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="CompletionStateMachine", dataType=o6.NodeId, valueRank=-1),
    ],
)
o6.call(
    nodeId="ns=machine_vision;i=7058",
    browseName="GenerateFileForRead",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6169"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6170"]),
)


@o6.objecttype(nodeId="ns=machine_vision;i=1039", browseName="ns=machine_vision;ResultTransferType", displayName="ResultTransferType")
class ResultTransferType(ns0.objtypes.TemporaryFileTransferType):
    generateFileForRead: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=machine_vision;i=7058"])


ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6176",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7059",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ProductId", dataType=o6.NodeId("ns=machine_vision;i=3003"), valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6177",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7059",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="InternalId", dataType=o6.NodeId("ns=machine_vision;i=3013"), valueRank=-1),
        ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1),
    ],
)
o6.call(
    nodeId="ns=machine_vision;i=7059",
    browseName="ns=machine_vision;UnprepareProduct",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6176"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6177"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6172",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7060",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ProductId", dataType=o6.NodeId("ns=machine_vision;i=3003"), valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6173",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7060",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="InternalId", dataType=o6.NodeId("ns=machine_vision;i=3013"), valueRank=-1),
        ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1),
    ],
)
o6.call(
    nodeId="ns=machine_vision;i=7060",
    browseName="ns=machine_vision;PrepareProduct",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6172"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6173"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6180",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7061",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="InternalId", dataType=o6.NodeId("ns=machine_vision;i=3013"), valueRank=-1),
        ns0.datatypes.Argument(name="ProductId", dataType=o6.NodeId("ns=machine_vision;i=3003"), valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6181",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7061",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7061",
    browseName="ns=machine_vision;UnlinkProduct",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6180"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6181"]),
)


@o6.objecttype(nodeId="ns=machine_vision;i=1004", browseName="ns=machine_vision;RecipeManagementType", displayName="RecipeManagementType")
class RecipeManagementType(ns0.objtypes.BaseObjectType):
    addRecipe: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=machine_vision;i=7013"])
    getRecipeListFiltered: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=machine_vision;i=7014"])
    prepareProduct: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=machine_vision;i=7060"])
    prepareRecipe: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=machine_vision;i=7015"])
    products: ProductFolderType | None
    recipeTransfer: RecipeTransferType | None
    recipes: RecipeFolderType | None = o6.hasComponent(RecipeFolderType(nodeId="ns=machine_vision;i=5005", browseName="ns=machine_vision;Recipes"))
    releaseRecipeHandle: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=machine_vision;i=7056"])
    removeRecipe: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=machine_vision;i=7057"])
    unlinkProduct: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=machine_vision;i=7061"])
    unprepareProduct: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=machine_vision;i=7059"])
    unprepareRecipe: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=machine_vision;i=7055"])


ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6190",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7062",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ProductId", dataType=o6.NodeId("ns=machine_vision;i=3003"), valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6191",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7062",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7062",
    browseName="ns=machine_vision;LinkProduct",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6190"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6191"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6196",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7063",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ProductId", dataType=o6.NodeId("ns=machine_vision;i=3003"), valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6197",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7063",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7063",
    browseName="ns=machine_vision;UnlinkProduct",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6196"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6197"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6202",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7064",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="IsCompleted", dataType=o6.Boolean, valueRank=-1), ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=machine_vision;i=7064", browseName="ns=machine_vision;Prepare", outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6202"]))

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6205",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7065",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=machine_vision;i=7065", browseName="ns=machine_vision;Unprepare", outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6205"]))


@o6.objecttype(nodeId="ns=machine_vision;i=1002", browseName="ns=machine_vision;RecipeType", displayName="RecipeType")
class RecipeType(ns0.objtypes.BaseObjectType):
    externalId: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision;i=6023",
            browseName="ns=machine_vision;ExternalId",
            description="Recipe ID for identifying the recipe outside the vision system. The ExternalID is only managed by the host system.",
            dataType=machine_vision_datypes.RecipeIdExternalDataType,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    handle: ns0.objtypes.FileType | None
    internalId: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision;i=6019",
            browseName="ns=machine_vision;InternalId",
            description="System-wide unique ID for identifying a recipe. This ID is assigned by the vision system.",
            dataType=machine_vision_datypes.RecipeIdInternalDataType,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    isPrepared: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6605", browseName="ns=machine_vision;IsPrepared", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
    )
    lastModified: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision;i=6017",
            browseName="ns=machine_vision;LastModified",
            description="The time when this recipe was last modified.",
            dataType=ns0.datatypes.UtcTime,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    linkProduct: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=machine_vision;i=7062"])
    linkedProducts: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision;i=6018",
            browseName="ns=machine_vision;LinkedProducts",
            dataType=machine_vision_datypes.ProductIdDataType,
            valueRank=1,
            arrayDimensions=[0],
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    prepare: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=machine_vision;i=7064"])
    unlinkProduct: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=machine_vision;i=7063"])
    unprepare: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=machine_vision;i=7065"])


ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6241",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7066",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Comment", dataType=o6.LocalizedText, valueRank=-1)],
)
o6.call(nodeId="ns=machine_vision;i=7066", browseName="ns=machine_vision;ConfirmAll", inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6241"]))

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6213",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7089",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[12],
    value=[
        ns0.datatypes.Argument(name="ResultState", dataType=o6.NodeId("ns=machine_vision;i=3009"), valueRank=-1),
        ns0.datatypes.Argument(name="MeasId", dataType=o6.NodeId("ns=machine_vision;i=3015"), valueRank=-1),
        ns0.datatypes.Argument(name="PartId", dataType=o6.NodeId("ns=machine_vision;i=3004"), valueRank=-1),
        ns0.datatypes.Argument(name="ExternalRecipeId", dataType=o6.NodeId("ns=machine_vision;i=3002"), valueRank=-1),
        ns0.datatypes.Argument(name="InternalRecipeId", dataType=o6.NodeId("ns=machine_vision;i=3013"), valueRank=-1),
        ns0.datatypes.Argument(name="ExternalConfigurationId", dataType=o6.NodeId("ns=machine_vision;i=3008"), valueRank=-1),
        ns0.datatypes.Argument(name="InternalConfigurationId", dataType=o6.NodeId("ns=machine_vision;i=3008"), valueRank=-1),
        ns0.datatypes.Argument(name="ProductId", dataType=o6.NodeId("ns=machine_vision;i=3003"), valueRank=-1),
        ns0.datatypes.Argument(name="JobId", dataType=o6.NodeId("ns=machine_vision;i=3016"), valueRank=-1),
        ns0.datatypes.Argument(name="MaxResults", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="StartIndex", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="Timeout", dataType=o6.Int32, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6214",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7089",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0.datatypes.Argument(name="IsComplete", dataType=o6.Boolean, valueRank=-1),
        ns0.datatypes.Argument(name="ResultCount", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="ResultHandle", dataType=o6.NodeId("ns=machine_vision;i=3018"), valueRank=-1),
        ns0.datatypes.Argument(name="ResultList", dataType=o6.NodeId("ns=machine_vision;i=3006"), valueRank=1),
        ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1),
    ],
)
o6.call(
    nodeId="ns=machine_vision;i=7089",
    browseName="ns=machine_vision;GetResultListFiltered",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6213"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6214"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6217",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7090",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ResultHandle", dataType=o6.NodeId("ns=machine_vision;i=3018"), valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6218",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7090",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7090",
    browseName="ns=machine_vision;ReleaseResultHandle",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6217"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6218"]),
)


@o6.objecttype(nodeId="ns=machine_vision;i=1007", browseName="ns=machine_vision;ResultManagementType", displayName="ResultManagementType")
class ResultManagementType(ns0.objtypes.BaseObjectType):
    getResultById: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=machine_vision;i=7026"])
    getResultComponentsById: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=machine_vision;i=7007"])
    getResultListFiltered: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=machine_vision;i=7089"])
    releaseResultHandle: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=machine_vision;i=7090"])
    resultTransfer: ResultTransferType | None
    results: ResultFolderType | None = o6.hasComponent(ResultFolderType(nodeId="ns=machine_vision;i=5245", browseName="ns=machine_vision;Results"))


ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6256",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7093",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="Cause", dataType=o6.Int32, valueRank=-1), ns0.datatypes.Argument(name="CauseDescription", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6257",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7093",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7093",
    browseName="ns=machine_vision;Reset",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6256"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6257"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6254",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7094",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="Cause", dataType=o6.Int32, valueRank=-1), ns0.datatypes.Argument(name="CauseDescription", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6255",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7094",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7094",
    browseName="ns=machine_vision;Halt",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6254"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6255"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6258",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7095",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=machine_vision;i=7095", browseName="ns=machine_vision;SelectModeAutomatic", outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6258"]))


@o6.objecttype(nodeId="ns=machine_vision;i=1017", browseName="ns=machine_vision;VisionStateMachineType", displayName="VisionStateMachineType")
class VisionStateMachineType(ns0.objtypes.FiniteStateMachineType):
    automaticModeStateMachine: VisionAutomaticModeStateMachineType | None
    confirmAll: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=machine_vision;i=7066"])
    error: ns0.objtypes.StateType
    errorStepModel: VisionStepModelStateMachineType | None
    errorToHalted: ns0.objtypes.TransitionType
    errorToHaltedAuto: ns0.objtypes.TransitionType
    errorToOperationalAuto: ns0.objtypes.TransitionType
    errorToPreoperational: ns0.objtypes.TransitionType
    errorToPreoperationalAuto: ns0.objtypes.TransitionType
    halt: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=machine_vision;i=7094"])
    halted: ns0.objtypes.StateType
    haltedStepModel: VisionStepModelStateMachineType | None
    haltedToPreoperational: ns0.objtypes.TransitionType
    haltedToPreoperationalAuto: ns0.objtypes.TransitionType
    operational: ns0.objtypes.StateType
    operationalToErrorAuto: ns0.objtypes.TransitionType
    operationalToHalted: ns0.objtypes.TransitionType
    operationalToHaltedAuto: ns0.objtypes.TransitionType
    operationalToPreoperational: ns0.objtypes.TransitionType
    operationalToPreoperationalAuto: ns0.objtypes.TransitionType
    preoperational: ns0.objtypes.StateType
    preoperationalStepModel: VisionStepModelStateMachineType | None
    preoperationalToErrorAuto: ns0.objtypes.TransitionType
    preoperationalToHalted: ns0.objtypes.TransitionType
    preoperationalToHaltedAuto: ns0.objtypes.TransitionType
    preoperationalToInitialized: ns0.objtypes.TransitionType
    preoperationalToInitializedAuto: ns0.objtypes.TransitionType
    preoperationalToOperational: ns0.objtypes.TransitionType
    preoperationalToOperationalAuto: ns0.objtypes.TransitionType
    reset: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=machine_vision;i=7093"])
    selectModeAutomatic: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=machine_vision;i=7095"])


ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6287",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7096",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="Cause", dataType=o6.Int32, valueRank=-1), ns0.datatypes.Argument(name="CauseDescription", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6288",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7096",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7096",
    browseName="ns=machine_vision;Stop",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6287"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6288"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6285",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7097",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="Cause", dataType=o6.Int32, valueRank=-1), ns0.datatypes.Argument(name="CauseDescription", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6286",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7097",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7097",
    browseName="ns=machine_vision;Abort",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6285"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6286"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6281",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7098",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0.datatypes.Argument(name="MeasId", dataType=o6.NodeId("ns=machine_vision;i=3015"), valueRank=-1),
        ns0.datatypes.Argument(name="PartId", dataType=o6.NodeId("ns=machine_vision;i=3004"), valueRank=-1),
        ns0.datatypes.Argument(name="RecipeId", dataType=o6.NodeId("ns=machine_vision;i=3002"), valueRank=-1),
        ns0.datatypes.Argument(name="ProductId", dataType=o6.NodeId("ns=machine_vision;i=3003"), valueRank=-1),
        ns0.datatypes.Argument(name="Parameters", dataType=ns0.datatypes.BaseDataType, valueRank=1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6282",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7098",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="JobId", dataType=o6.NodeId("ns=machine_vision;i=3016"), valueRank=-1),
        ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1),
    ],
)
o6.call(
    nodeId="ns=machine_vision;i=7098",
    browseName="ns=machine_vision;StartSingleJob",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6281"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6282"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6289",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7100",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="Activate", dataType=o6.Boolean, valueRank=-1),
        ns0.datatypes.Argument(name="Cause", dataType=o6.Int32, valueRank=-1),
        ns0.datatypes.Argument(name="CauseDescription", dataType=o6.String, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6290",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7100",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7100",
    browseName="ns=machine_vision;SimulationMode",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6289"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6290"]),
)


@o6.objecttype(nodeId="ns=machine_vision;i=1021", browseName="ns=machine_vision;VisionAutomaticModeStateMachineType", displayName="VisionAutomaticModeStateMachineType")
class VisionAutomaticModeStateMachineType(ns0.objtypes.FiniteStateMachineType):
    abort: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=machine_vision;i=7097"])
    continuousExecution: ns0.objtypes.StateType
    continuousExecutionStepModel: VisionStepModelStateMachineType | None
    continuousExecutionToReadyAbort: ns0.objtypes.TransitionType
    continuousExecutionToReadyAuto: ns0.objtypes.TransitionType
    continuousExecutionToReadyStop: ns0.objtypes.TransitionType
    initialized: ns0.objtypes.StateType
    initializedStepModel: VisionStepModelStateMachineType | None
    initializedToReadyAuto: ns0.objtypes.TransitionType
    initializedToReadyProduct: ns0.objtypes.TransitionType
    initializedToReadyRecipe: ns0.objtypes.TransitionType
    ready: ns0.objtypes.StateType
    readyStepModel: VisionStepModelStateMachineType | None
    readyToContinuousExecution: ns0.objtypes.TransitionType
    readyToContinuousExecutionAuto: ns0.objtypes.TransitionType
    readyToInitializedAuto: ns0.objtypes.TransitionType
    readyToInitializedProduct: ns0.objtypes.TransitionType
    readyToInitializedRecipe: ns0.objtypes.TransitionType
    readyToSingleExecution: ns0.objtypes.TransitionType
    readyToSingleExecutionAuto: ns0.objtypes.TransitionType
    simulationMode: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=machine_vision;i=7100"])
    singleExecution: ns0.objtypes.StateType
    singleExecutionStepModel: VisionStepModelStateMachineType | None
    singleExecutionToReadyAbort: ns0.objtypes.TransitionType
    singleExecutionToReadyAuto: ns0.objtypes.TransitionType
    singleExecutionToReadyStop: ns0.objtypes.TransitionType
    startContinuous: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=machine_vision;i=7009"])
    startSingleJob: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=machine_vision;i=7098"])
    stop: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=machine_vision;i=7096"])


ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6319",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7101",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="Cause", dataType=o6.Int32, valueRank=-1), ns0.datatypes.Argument(name="CauseDescription", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6320",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7101",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7101",
    browseName="ns=machine_vision;Sync",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6319"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6320"]),
)


@o6.objecttype(nodeId="ns=machine_vision;i=1026", browseName="ns=machine_vision;VisionStepModelStateMachineType", displayName="VisionStepModelStateMachineType")
class VisionStepModelStateMachineType(ns0.objtypes.FiniteStateMachineType):
    entry: ns0.objtypes.InitialStateType
    entryToExitAuto: ns0.objtypes.TransitionType
    entryToWaitAuto: ns0.objtypes.TransitionType
    exit: ns0.objtypes.StateType
    step: ns0.objtypes.StateType
    stepToExitAuto: ns0.objtypes.TransitionType
    stepToWaitAuto: ns0.objtypes.TransitionType
    sync: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=machine_vision;i=7101"])
    wait: ns0.objtypes.StateType
    waitToStep: ns0.objtypes.TransitionType
    waitToStepAuto: ns0.objtypes.TransitionType


ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6184",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7123",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="generateOptions", dataType=o6.NodeId("ns=machine_vision;i=3012"), valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6185",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7123",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="fileNodeId", dataType=o6.NodeId, valueRank=-1),
        ns0.datatypes.Argument(name="fileHandle", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="completionStateMachine", dataType=o6.NodeId, valueRank=-1),
    ],
)
o6.call(
    nodeId="ns=machine_vision;i=7123",
    browseName="GenerateFileForRead",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6184"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6185"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6583",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7124",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="GenerateOptions", dataType=o6.NodeId("ns=machine_vision;i=3012"), valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6584",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7124",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileNodeId", dataType=o6.NodeId, valueRank=-1), ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7124",
    browseName="GenerateFileForWrite",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6583"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6584"]),
)


@o6.objecttype(nodeId="ns=machine_vision;i=1014", browseName="ns=machine_vision;RecipeTransferType", displayName="RecipeTransferType")
class RecipeTransferType(ns0.objtypes.TemporaryFileTransferType):
    generateFileForRead: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=machine_vision;i=7123"])
    generateFileForWrite: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=machine_vision;i=7124"])


ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6617",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7129",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="GenerateOptions", dataType=o6.NodeId("ns=machine_vision;i=3011"), valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6618",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7129",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="FileNodeId", dataType=o6.NodeId, valueRank=-1),
        ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="CompletionStateMachine", dataType=o6.NodeId, valueRank=-1),
    ],
)
o6.call(
    nodeId="ns=machine_vision;i=7129",
    browseName="GenerateFileForRead",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6617"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6618"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6121",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7130",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="GenerateOptions", dataType=o6.NodeId("ns=machine_vision;i=3011"), valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6122",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7130",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileNodeId", dataType=o6.NodeId, valueRank=-1), ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7130",
    browseName="GenerateFileForWrite",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6121"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6122"]),
)


@o6.objecttype(nodeId="ns=machine_vision;i=1012", browseName="ns=machine_vision;ConfigurationTransferType", displayName="ConfigurationTransferType")
class ConfigurationTransferType(ns0.objtypes.TemporaryFileTransferType):
    generateFileForRead: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=machine_vision;i=7129"])
    generateFileForWrite: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=machine_vision;i=7130"])


del Any, TYPE_CHECKING, uuid, o6, ns0, machine_vision_reftypes, machine_vision_datypes, machine_vision_vartypes
