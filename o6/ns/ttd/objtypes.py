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

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(
    nodeId="ns=ttd;i=1006",
    browseName="ns=ttd;TTDResultReadyEventType",
    displayName="TTDResultReadyEventType",
    description="Provides information of a complete or partial result.",
    isAbstract=True,
)
class TTDResultReadyEventType(machinery_result.objtypes.ResultReadyEventType):
    result: ttd_vartypes.TTDResultType


@o6.objecttype(nodeId="ns=ttd;i=1009", browseName="ns=ttd;JobStatisticsType", displayName="JobStatisticsType")
class JobStatisticsType(ns0.objtypes.BaseObjectType):
    endTime: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ttd;i=6056", browseName="ns=ttd;EndTime", dataType=ns0.datatypes.UtcTime))
    startTime: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=ttd;i=6057", browseName="ns=ttd;StartTime", dataType=ns0.datatypes.UtcTime))
    totalInitializingTime: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=ttd;i=6058", browseName="ns=ttd;TotalInitializingTime", dataType=ns0.datatypes.Duration)
    )
    totalInterruptedTime: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=ttd;i=6059", browseName="ns=ttd;TotalInterruptedTime", dataType=ns0.datatypes.Duration)
    )
    totalRunningTime: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=ttd;i=6060", browseName="ns=ttd;TotalRunningTime", dataType=ns0.datatypes.Duration)
    )


@o6.objecttype(nodeId="ns=ttd;i=1004", browseName="ns=ttd;RecurrentPrognosisType", displayName="RecurrentPrognosisType")
class RecurrentPrognosisType(machine_tool.objtypes.PrognosisType):
    activity: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=ttd;i=6066", browseName="ns=ttd;Activity", dataType=o6.LocalizedText, accessLevel=3, userAccessLevel=1)
    )
    interval: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=ttd;i=6067", browseName="ns=ttd;Interval", dataType=ns0.datatypes.UtcTime, accessLevel=3, userAccessLevel=1)
    )
    lastExecutionTime: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=ttd;i=6068", browseName="ns=ttd;LastExecutionTime", dataType=ns0.datatypes.UtcTime, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=ttd;i=1010", browseName="ns=ttd;TextileTestingDeviceType", displayName="TextileTestingDeviceType")
class TextileTestingDeviceType(ns0.objtypes.BaseObjectType):
    availableExchangeableParts: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=ttd;i=6131",
            browseName="ns=ttd;AvailableExchangeableParts",
            dataType=ttd_datypes.ExchangeablePartDataType,
            valueRank=1,
            arrayDimensions=[0],
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    identification: machinery.objtypes.MachineIdentificationType
    installedTesterModules: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=ttd;i=6135",
            browseName="ns=ttd;InstalledTesterModules",
            dataType=ttd_datypes.OptionalModuleDataType,
            valueRank=1,
            arrayDimensions=[0],
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    machineStatistics: MachineStatisticsType
    machineryBuildingBlocks: ns0.objtypes.FolderType
    notification: machine_tool.objtypes.NotificationType = o6.hasComponent(
        machine_tool.objtypes.NotificationType(nodeId="ns=ttd;i=5050", browseName="ns=machine_tool;Notification")
    )
    recipeManagement: RecipeManagementType
    testProcedureIds: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=ttd;i=6146",
            browseName="ns=ttd;TestProcedureIds",
            dataType=ttd_datypes.TestProcedureIdDataType,
            valueRank=1,
            arrayDimensions=[0],
            accessLevel=3,
            userAccessLevel=1,
        )
    )


ns0.vartypes.PropertyType(
    nodeId="ns=ttd;i=6049",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ttd;i=7001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="RecipeIds", dataType=o6.NodeId("ns=ttd;i=3003"), valueRank=1, arrayDimensions=[0])],
)
o6.call(nodeId="ns=ttd;i=7001", browseName="ns=ttd;GetRecipeIds", outputArgs=o6.hasProperty(o6.ns["ns=ttd;i=6049"]))

ns0.vartypes.PropertyType(
    nodeId="ns=ttd;i=6050",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ttd;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="RecipeId", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ttd;i=6051",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ttd;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Recipe", dataType=o6.NodeId("ns=ttd;i=3018"), valueRank=-1)],
)
o6.call(nodeId="ns=ttd;i=7002", browseName="ns=ttd;GetRecipe", inputArgs=o6.hasProperty(o6.ns["ns=ttd;i=6050"]), outputArgs=o6.hasProperty(o6.ns["ns=ttd;i=6051"]))

ns0.vartypes.PropertyType(
    nodeId="ns=ttd;i=6052",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ttd;i=7003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="Recipe", dataType=o6.NodeId("ns=ttd;i=3018"), valueRank=-1), ns0.datatypes.Argument(name="Overwrite", dataType=o6.Boolean, valueRank=-1)],
)
o6.call(nodeId="ns=ttd;i=7003", browseName="ns=ttd;SetRecipe", inputArgs=o6.hasProperty(o6.ns["ns=ttd;i=6052"]))

ns0.vartypes.PropertyType(
    nodeId="ns=ttd;i=6053",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ttd;i=7004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="RecipeId", dataType=o6.String, valueRank=-1)],
)
o6.call(nodeId="ns=ttd;i=7004", browseName="ns=ttd;DeleteRecipe", inputArgs=o6.hasProperty(o6.ns["ns=ttd;i=6053"]))

ns0.vartypes.PropertyType(
    nodeId="ns=ttd;i=6054",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ttd;i=7005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Recipes", dataType=o6.NodeId("ns=ttd;i=3018"), valueRank=1, arrayDimensions=[0])],
)
o6.call(nodeId="ns=ttd;i=7005", browseName="ns=ttd;GetRecipes", outputArgs=o6.hasProperty(o6.ns["ns=ttd;i=6054"]))

ns0.vartypes.PropertyType(
    nodeId="ns=ttd;i=6055",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ttd;i=7006",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Recipes", dataType=o6.NodeId("ns=ttd;i=3018"), valueRank=1, arrayDimensions=[0]),
        ns0.datatypes.Argument(name="Overwrite", dataType=o6.Boolean, valueRank=-1),
    ],
)
o6.call(nodeId="ns=ttd;i=7006", browseName="ns=ttd;SetRecipes", inputArgs=o6.hasProperty(o6.ns["ns=ttd;i=6055"]))


@o6.objecttype(nodeId="ns=ttd;i=1003", browseName="ns=ttd;RecipeManagementType", displayName="RecipeManagementType")
class RecipeManagementType(ns0.objtypes.BaseObjectType):
    deleteRecipe: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=ttd;i=7004"])
    getRecipe: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=ttd;i=7002"])
    getRecipeIds: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=ttd;i=7001"])
    getRecipes: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=ttd;i=7005"])
    recipeIds: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=ttd;i=6016", browseName="ns=ttd;RecipeIds", dataType=ttd_datypes.RecipeIdDataType, valueRank=1, arrayDimensions=[0], accessLevel=3, userAccessLevel=1
        )
    )
    setRecipe: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=ttd;i=7003"])
    setRecipes: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=ttd;i=7006"])


@o6.objecttype(nodeId="ns=ttd;i=1012", browseName="ns=ttd;MachineStatisticsType", displayName="MachineStatisticsType", interfaces=[ia.objtypes.IStatisticsType])
class MachineStatisticsType(ns0.objtypes.BaseObjectType):
    resetStatistics: o6.node.MethodNode | None = o6.hasComponent(o6.call(nodeId="ns=ttd;i=7007", browseName="ns=ia;ResetStatistics"))
    startTime: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=ttd;i=6065", browseName="ns=ia;StartTime", dataType=o6.DateTime, accessLevel=3, userAccessLevel=1)
    )
    totalExecutingTime: ns0.vartypes.BaseDataVariableType = o6.reference(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=ttd;i=6061", browseName="ns=ttd;TotalExecutingTime", dataType=ns0.datatypes.Duration), "ns=ia;i=4002"
    )
    totalNotAvailableTime: ns0.vartypes.BaseDataVariableType = o6.reference(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=ttd;i=6062", browseName="ns=ttd;TotalNotAvailableTime", dataType=ns0.datatypes.Duration), "ns=ia;i=4002"
    )
    totalNotExecutingTime: ns0.vartypes.BaseDataVariableType = o6.reference(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=ttd;i=6063", browseName="ns=ttd;TotalNotExecutingTime", dataType=ns0.datatypes.Duration), "ns=ia;i=4002"
    )
    totalOutOfServiceTime: ns0.vartypes.BaseDataVariableType = o6.reference(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=ttd;i=6064", browseName="ns=ttd;TotalOutOfServiceTime", dataType=ns0.datatypes.Duration), "ns=ia;i=4002"
    )


ns0.vartypes.PropertyType(
    nodeId="ns=ttd;i=6111",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ttd;i=7009",
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
    nodeId="ns=ttd;i=6112",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ttd;i=7009",
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
o6.call(nodeId="ns=ttd;i=7009", browseName="ns=machinery_result;GetResultById", inputArgs=o6.hasProperty(o6.ns["ns=ttd;i=6111"]), outputArgs=o6.hasProperty(o6.ns["ns=ttd;i=6112"]))


@o6.objecttype(nodeId="ns=ttd;i=1007", browseName="ns=ttd;TTDResultManagementType", displayName="TTDResultManagementType")
class TTDResultManagementType(machinery_result.objtypes.ResultManagementType):
    getResultById: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=ttd;i=7009"])
    resultTransfer: machinery_result.objtypes.ResultTransferType
    results: ns0.objtypes.FolderType


o6.reference(TTDResultManagementType, "i=41", TTDResultReadyEventType)


del Any, TYPE_CHECKING, uuid, o6, di, ia, isa95_jobcontrol_v2, machine_tool, machinery, machinery_jobs, machinery_result, ns0, ttd_datypes, ttd_vartypes
