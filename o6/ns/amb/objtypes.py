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

"""Generated OPC UA amb namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.ns0 as ns0
from . import reftypes as amb_reftypes
from . import datatypes as amb_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(
    nodeId="ns=amb;i=1003",
    browseName="ns=amb;ConnectionFailureConditionClassType",
    displayName="ConnectionFailureConditionClassType",
    description="One or more connections have failed",
    isAbstract=True,
)
class ConnectionFailureConditionClassType(ns0.objtypes.SystemConditionClassType):
    pass


@o6.objecttype(
    nodeId="ns=amb;i=1004", browseName="ns=amb;OverTemperatureConditionClassType", displayName="OverTemperatureConditionClassType", description="Over temperature", isAbstract=True
)
class OverTemperatureConditionClassType(ns0.objtypes.SystemConditionClassType):
    pass


@o6.objecttype(
    nodeId="ns=amb;i=1005", browseName="ns=amb;CalibrationDueConditionClassType", displayName="CalibrationDueConditionClassType", description="Calibration is due", isAbstract=True
)
class CalibrationDueConditionClassType(ns0.objtypes.MaintenanceConditionClassType):
    pass


@o6.objecttype(
    nodeId="ns=amb;i=1006", browseName="ns=amb;SelfTestFailureConditionClassType", displayName="SelfTestFailureConditionClassType", description="Self-Test failure", isAbstract=True
)
class SelfTestFailureConditionClassType(ns0.objtypes.SystemConditionClassType):
    pass


@o6.objecttype(
    nodeId="ns=amb;i=1007",
    browseName="ns=amb;FlashUpdateInProgressConditionClassType",
    displayName="FlashUpdateInProgressConditionClassType",
    description="Flash update in progress",
    isAbstract=True,
)
class FlashUpdateInProgressConditionClassType(ns0.objtypes.MaintenanceConditionClassType):
    pass


@o6.objecttype(
    nodeId="ns=amb;i=1008",
    browseName="ns=amb;BadConfigurationConditionClassType",
    displayName="BadConfigurationConditionClassType",
    description="Configuration is bad",
    isAbstract=True,
)
class BadConfigurationConditionClassType(ns0.objtypes.SystemConditionClassType):
    pass


@o6.objecttype(
    nodeId="ns=amb;i=1009",
    browseName="ns=amb;OutOfResourcesConditionClassType",
    displayName="OutOfResourcesConditionClassType",
    description="Out of resources issues",
    isAbstract=True,
)
class OutOfResourcesConditionClassType(ns0.objtypes.SystemConditionClassType):
    pass


@o6.objecttype(
    nodeId="ns=amb;i=1010", browseName="ns=amb;OutOfMemoryConditionClassType", displayName="OutOfMemoryConditionClassType", description="Out of memory issues", isAbstract=True
)
class OutOfMemoryConditionClassType(OutOfResourcesConditionClassType):
    pass


@o6.objecttype(
    nodeId="ns=amb;i=1013",
    browseName="ns=amb;MaintenanceEventStateMachineType",
    displayName="MaintenanceEventStateMachineType",
    description="Information, whether a maintenance activity is planned, currently in execution, or has been executed",
)
class MaintenanceEventStateMachineType(ns0.objtypes.FiniteStateMachineType):
    executing: ns0.objtypes.StateType
    finished: ns0.objtypes.StateType
    fromExecutingToFinished: ns0.objtypes.TransitionType
    fromFinishedToPlanned: ns0.objtypes.TransitionType
    fromPlannedToExecuting: ns0.objtypes.TransitionType
    planned: ns0.objtypes.InitialStateType


@o6.objecttype(
    nodeId="ns=amb;i=1014",
    browseName="ns=amb;InspectionConditionClassType",
    displayName="InspectionConditionClassType",
    description="An inspection maintenance activity",
    isAbstract=True,
)
class InspectionConditionClassType(ns0.objtypes.MaintenanceConditionClassType):
    pass


@o6.objecttype(
    nodeId="ns=amb;i=1015",
    browseName="ns=amb;ExternalCheckConditionClassType",
    displayName="ExternalCheckConditionClassType",
    description="An external check maintenance activity",
    isAbstract=True,
)
class ExternalCheckConditionClassType(ns0.objtypes.MaintenanceConditionClassType):
    pass


@o6.objecttype(
    nodeId="ns=amb;i=1016",
    browseName="ns=amb;ServicingConditionClassType",
    displayName="ServicingConditionClassType",
    description="A servicing maintenance activity",
    isAbstract=True,
)
class ServicingConditionClassType(ns0.objtypes.MaintenanceConditionClassType):
    pass


@o6.objecttype(
    nodeId="ns=amb;i=1017", browseName="ns=amb;RepairConditionClassType", displayName="RepairConditionClassType", description="A repair maintenance activity", isAbstract=True
)
class RepairConditionClassType(ns0.objtypes.MaintenanceConditionClassType):
    pass


@o6.objecttype(
    nodeId="ns=amb;i=1018",
    browseName="ns=amb;ImprovementConditionClassType",
    displayName="ImprovementConditionClassType",
    description="An improvement maintenance activity",
    isAbstract=True,
)
class ImprovementConditionClassType(ns0.objtypes.MaintenanceConditionClassType):
    pass


@o6.objecttype(
    nodeId="ns=amb;i=1019",
    browseName="ns=amb;FlashUpdateFailedConditionClassType",
    displayName="FlashUpdateFailedConditionClassType",
    description="Flash update has failed",
    isAbstract=True,
)
class FlashUpdateFailedConditionClassType(ns0.objtypes.SystemConditionClassType):
    pass


@o6.objecttype(
    nodeId="ns=amb;i=1002",
    browseName="ns=amb;IRootCauseIndicationType",
    displayName="IRootCauseIndicationType",
    description="Information on the root cause of conditions, should be applied to alarms (AlarmType or subtypes)",
    isAbstract=True,
)
class IRootCauseIndicationType(ns0.objtypes.BaseInterfaceType):
    potentialRootCauses: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=amb;i=6015",
            browseName="ns=amb;PotentialRootCauses",
            description="An array of potential root causes of the alarm. This is intended to be a hint to the client and might be a local view on the potential root causes of the alarm. The list might not contain all potential root causes, that is, other potential root causes might exist as well. If the alarm itself is considered to be the root cause, the array shall be empty. If no potential root causes have been identified, there shall be at least one entry in the array indicating that the root cause is unknown.",
            dataType=amb_datypes.RootCauseDataType,
            valueRank=1,
            arrayDimensions=[0],
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=amb;i=1012",
    browseName="ns=amb;IMaintenanceEventType",
    displayName="IMaintenanceEventType",
    description="Information on maintenance activities, should by applied to conditions (ConditionType or subtypes)",
    isAbstract=True,
)
class IMaintenanceEventType(ns0.objtypes.BaseInterfaceType):
    configurationChanged: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=amb;i=6042",
            browseName="ns=amb;ConfigurationChanged",
            description="Information if the configuration of the asset is planned to be changed or has changed during the maintenance activity. FALSE indicates no change, and TRUE indicates a change. The content may change during the different MaintenanceStates. By accessing the history of Events a Client can distinguish between the planned and actual configuration changes during the maintenance activity.",
            dataType=o6.Boolean,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    estimatedDowntime: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=amb;i=6036",
            browseName="ns=amb;EstimatedDowntime",
            description="The estimated time the execution of the maintenance activity will take. In case of replanning, it is allowed to change the EstimatedDowntime. If during the execution of the maintenance activity the EstimatedDowntime can be adjusted (e.g., the asset needs to be repaired because an inspection found some issues) this should be done. Clients can access the history of Events to receive the information on the original estimates when the maintenance activity started.",
            dataType=ns0.datatypes.Duration,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    maintenanceMethod: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=amb;i=6041",
            browseName="ns=amb;MaintenanceMethod",
            description="Information about the planned or used maintenance method. The content may change during the different MaintenanceStates. By accessing the history of Events a Client can distinguish between the planned and actual used maintenance method during the maintenance activity.",
            dataType=amb_datypes.MaintenanceMethodEnum,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    maintenanceState: MaintenanceEventStateMachineType
    maintenanceSupplier: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=amb;i=6037",
            browseName="ns=amb;MaintenanceSupplier",
            description="Information on the supplier that is planned to execute, currently executing or has executed the maintenance activity. The content may change during the different MaintenanceStates. By accessing the history of Events a Client can distinguish between the planned and actual supplier that executed the maintenance activity. The value contains always a human-readable name of the supplier and optionally references a Node representing the supplier in the AddressSpace.",
            dataType=amb_datypes.NameNodeIdDataType,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    partsOfAssetReplaced: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=amb;i=6039",
            browseName="ns=amb;PartsOfAssetReplaced",
            description="Information on the parts of the assets that are planned to be serviced during the maintenance activity, currently serviced or have been serviced, depending on the different MaintenanceStates. The content may change during the different MaintenanceStates. By accessing the history of Events a Client can distinguish between the planned and actual parts of the assets serviced during the maintenance activity. The value contains always an array of a human-readable name of the qualification of the parts of the asset to be serviced and optionally references a Node representing the part of the asset in the AddressSpace.",
            dataType=amb_datypes.NameNodeIdDataType,
            valueRank=1,
            arrayDimensions=[0],
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    partsOfAssetServiced: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=amb;i=6040",
            browseName="ns=amb;PartsOfAssetServiced",
            description="Information on the parts of the assets that are planned to be serviced during the maintenance activity, currently serviced or have been serviced, depending on the different MaintenanceStates. The content may change during the different MaintenanceStates. By accessing the history of Events a Client can distinguish between the planned and actual parts of the assets serviced during the maintenance activity. The value contains always an array of a human-readable name of the qualification of the parts of the asset to be serviced and optionally references a Node representing the part of the asset in the AddressSpace.",
            dataType=amb_datypes.NameNodeIdDataType,
            valueRank=1,
            arrayDimensions=[0],
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    plannedDate: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=amb;i=6035",
            browseName="ns=amb;PlannedDate",
            description="Date for which the maintenance activity has been scheduled. In case of replanning, it is allowed to change the PlannedDate. However, it is not the intention that the PlannedDate is modified because the maintenance activity starts to get executed. If the PlannedDate depends for example on the operation hours of the asset, it might get adapted depending on the passed operation hours.",
            dataType=ns0.datatypes.UtcTime,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    qualificationOfPersonnel: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=amb;i=6038",
            browseName="ns=amb;QualificationOfPersonnel",
            description="Information on the qualification of the personnel that is planned to execute, currently executing or has executed the maintenance activity. The content may change during the different MaintenanceStates. By accessing the history of Events a Client can distinguish between the planned and actual qualification of the personnel that executed the maintenance activity. The value contains always a human-readable name of the qualification of the personnel and optionally references a Node representing the qualification of the personnel in the AddressSpace.",
            dataType=amb_datypes.NameNodeIdDataType,
            accessLevel=3,
            userAccessLevel=1,
        )
    )


ns0.vartypes.PropertyType(
    nodeId="ns=amb;i=6018",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=amb;i=7004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.Argument(
            name="LinkToExternalSource",
            dataType=ns0.datatypes.UriString,
            valueRank=-1,
            description=o6.LocalizedText("Link to an external source. The server might or might not check if a correct URI is provided, or if the URI is available/reachable."),
        ),
        ns0.datatypes.Argument(
            name="BrowseName",
            dataType=o6.QualifiedName,
            valueRank=-1,
            description=o6.LocalizedText("The BrowseName of the new created Node. Method fails if a Variable with the same BrowseName already exists."),
        ),
        ns0.datatypes.Argument(
            name="DisplayName",
            dataType=o6.LocalizedText,
            valueRank=-1,
            description=o6.LocalizedText(
                "The DisplayName of the new created Node. If the server supports multiple locales, and the Client wants to provide more than one locale, the Write operation on the Variable shall be used."
            ),
        ),
        ns0.datatypes.Argument(
            name="Description",
            dataType=o6.LocalizedText,
            valueRank=-1,
            description=o6.LocalizedText(
                "The Description of the new created Node. If the server supports multiple locales, and the Client wants to provide more than one locale, the Write operation on the Variable shall be used."
            ),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=amb;i=6019",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=amb;i=7004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="LinkVariable", dataType=o6.NodeId, valueRank=-1, description=o6.LocalizedText("The NodeId of the newly created Variable."))],
)
o6.call(
    nodeId="ns=amb;i=7004",
    browseName="ns=amb;AddLink",
    description="Method to add an end-user specific link that is stored persistently in the server.",
    inputArgs=o6.hasProperty(o6.ns["ns=amb;i=6018"]),
    outputArgs=o6.hasProperty(o6.ns["ns=amb;i=6019"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=amb;i=6020",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=amb;i=7005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="VariableToBeDeleted",
            dataType=o6.NodeId,
            valueRank=-1,
            description=o6.LocalizedText(
                "NodeId of the Variable containing a link, that should be deleted. Variable shall be referenced from the Object with a HasComponent Reference where the Method is called on."
            ),
        )
    ],
)
o6.call(
    nodeId="ns=amb;i=7005",
    browseName="ns=amb;RemoveLink",
    description="Method to remove an end-user specific link that is managed in the server.",
    inputArgs=o6.hasProperty(o6.ns["ns=amb;i=6020"]),
)


@o6.objecttype(
    nodeId="ns=amb;i=1011",
    browseName="ns=amb;DocumentationLinksType",
    displayName="DocumentationLinksType",
    description="AddIn to link documentation provided by the manufacturer and / or end-user.",
)
class DocumentationLinksType(ns0.objtypes.BaseObjectType):
    addLink: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=amb;i=7004"])
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=amb;i=6016",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("amb:DocumentationLinks"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    langleLinkRangle: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=amb;i=6017",
            browseName="ns=amb;<Link>",
            description="Represents links to externally managed documentation, typically URLs.",
            modellingRule="OptionalPlaceholder",
            dataType=ns0.datatypes.UriString,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    removeLink: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=amb;i=7005"])


del Any, TYPE_CHECKING, uuid, o6, ns0, amb_reftypes, amb_datypes
