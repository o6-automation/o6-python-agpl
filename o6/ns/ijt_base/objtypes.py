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
from . import vartypes as ijt_base_vartypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(
    nodeId="ns=ijt_base;i=1006",
    browseName="ns=ijt_base;JoiningSystemEventType",
    displayName="JoiningSystemEventType",
    description="The JoiningSystemEventType is used to send any type of events from a joining system. \nNote: The type of event is determined by the usage of respective Condition Class(es) and Condition SubClass(es) properties defined in 0:BaseEventType.",
    isAbstract=True,
)
class JoiningSystemEventType(ns0.objtypes.BaseEventType):
    joiningSystemEventContent: ijt_base_vartypes.JoiningSystemEventContentType | None


@o6.objecttype(
    nodeId="ns=ijt_base;i=1007",
    browseName="ns=ijt_base;JoiningSystemResultReadyEventType",
    displayName="JoiningSystemResultReadyEventType",
    description="This EventType provides information of a complete or partial result from a joining system.",
    isAbstract=True,
)
class JoiningSystemResultReadyEventType(machinery_result.objtypes.ResultReadyEventType):
    result: ijt_base_vartypes.JoiningSystemResultType


@o6.objecttype(
    nodeId="ns=ijt_base;i=1018",
    browseName="ns=ijt_base;AssetConnectedConditionClassType",
    displayName="AssetConnectedConditionClassType",
    description="Indicates that the asset is connected.",
)
class AssetConnectedConditionClassType(ns0.objtypes.BaseConditionClassType):
    pass


@o6.objecttype(
    nodeId="ns=ijt_base;i=1020",
    browseName="ns=ijt_base;JoiningSystemConditionType",
    displayName="JoiningSystemConditionType",
    description="The JoiningSystemConditionType is used to send any type of events with acknowledgement mechanism from a joining system.\nNote: The type of event is determined by the usage of respective Condition Class(es) and Condition SubClass(es) properties defined in 0:ConditionType.",
    interfaces=[amb.objtypes.IRootCauseIndicationType],
)
class JoiningSystemConditionType(ns0.objtypes.AcknowledgeableConditionType):
    joiningSystemEventContent: ijt_base_vartypes.JoiningSystemEventContentType | None


@o6.objecttype(
    nodeId="ns=ijt_base;i=1021",
    browseName="ns=ijt_base;AssetDisconnectedConditionClassType",
    displayName="AssetDisconnectedConditionClassType",
    description="Indicates that the asset is disconnected.",
)
class AssetDisconnectedConditionClassType(ns0.objtypes.BaseConditionClassType):
    pass


@o6.objecttype(
    nodeId="ns=ijt_base;i=1024",
    browseName="ns=ijt_base;AssetEnabledConditionClassType",
    displayName="AssetEnabledConditionClassType",
    description="Indicates that the asset is enabled.",
)
class AssetEnabledConditionClassType(ns0.objtypes.BaseConditionClassType):
    pass


@o6.objecttype(
    nodeId="ns=ijt_base;i=1027",
    browseName="ns=ijt_base;AssetDisabledConditionClassType",
    displayName="AssetDisabledConditionClassType",
    description="Indicates that the asset is disabled.",
)
class AssetDisabledConditionClassType(ns0.objtypes.BaseConditionClassType):
    pass


@o6.objecttype(
    nodeId="ns=ijt_base;i=1030",
    browseName="ns=ijt_base;ConfigurationChangeConditionClassType",
    displayName="ConfigurationChangeConditionClassType",
    description="Indicates a change in the configuration.",
)
class ConfigurationChangeConditionClassType(ns0.objtypes.BaseConditionClassType):
    pass


@o6.objecttype(
    nodeId="ns=ijt_base;i=1032",
    browseName="ns=ijt_base;SelectedEntityConditionClassType",
    displayName="SelectedEntityConditionClassType",
    description="Indicates that an entity is selected in a joining system.",
)
class SelectedEntityConditionClassType(ns0.objtypes.BaseConditionClassType):
    pass


@o6.objecttype(
    nodeId="ns=ijt_base;i=1033",
    browseName="ns=ijt_base;ThresholdViolationConditionClassType",
    displayName="ThresholdViolationConditionClassType",
    description="Indicates that a threshold is violated.",
)
class ThresholdViolationConditionClassType(ns0.objtypes.BaseConditionClassType):
    pass


@o6.objecttype(
    nodeId="ns=ijt_base;i=1034",
    browseName="ns=ijt_base;EntityExpiryWarningConditionClassType",
    displayName="EntityExpiryWarningConditionClassType",
    description="The EntityExpiryWarningConditionClassType is used to classify events or conditions to indicate that an entity is about to expire within a joining system.",
)
class EntityExpiryWarningConditionClassType(ns0.objtypes.BaseConditionClassType):
    pass


@o6.objecttype(
    nodeId="ns=ijt_base;i=1035",
    browseName="ns=ijt_base;RequestedResultEventType",
    displayName="RequestedResultEventType",
    description="This EventType provides the requested results from the Server using RequestResults method or RequestUnacknowledgedResults method.",
    isAbstract=True,
)
class RequestedResultEventType(JoiningSystemResultReadyEventType):
    pass


@o6.objecttype(
    nodeId="ns=ijt_base;i=1036",
    browseName="ns=ijt_base;ThresholdViolationResolvedConditionClassType",
    displayName="ThresholdViolationResolvedConditionClassType",
    description="Indicates that a violated threshold is resolved.",
)
class ThresholdViolationResolvedConditionClassType(ns0.objtypes.BaseConditionClassType):
    pass


@o6.objecttype(
    nodeId="ns=ijt_base;i=1037",
    browseName="ns=ijt_base;SelectedProcessConditionClassType",
    displayName="SelectedProcessConditionClassType",
    description="Indicates that a given joining process is selected in a joining system.",
)
class SelectedProcessConditionClassType(ns0.objtypes.BaseConditionClassType):
    pass


@o6.objecttype(
    nodeId="ns=ijt_base;i=1038",
    browseName="ns=ijt_base;StartedEntityConditionClassType",
    displayName="StartedEntityConditionClassType",
    description="Indicates that an entity is started.",
)
class StartedEntityConditionClassType(ns0.objtypes.BaseConditionClassType):
    pass


@o6.objecttype(
    nodeId="ns=ijt_base;i=1039",
    browseName="ns=ijt_base;JoiningSystemUserLoggedInConditionClassType",
    displayName="JoiningSystemUserLoggedInConditionClassType",
    description="Indicates that a joining system user has logged-in.",
)
class JoiningSystemUserLoggedInConditionClassType(ns0.objtypes.BaseConditionClassType):
    pass


@o6.objecttype(
    nodeId="ns=ijt_base;i=1041",
    browseName="ns=ijt_base;UnacknowledgedResultsConditionClassType",
    displayName="UnacknowledgedResultsConditionClassType",
    description="Indicates the result memory in a joining system is above the configured limit of unacknowledged results.",
)
class UnacknowledgedResultsConditionClassType(ns0.objtypes.BaseConditionClassType):
    pass


@o6.objecttype(
    nodeId="ns=ijt_base;i=1042",
    browseName="ns=ijt_base;JoiningSystemUserLoggedOutConditionClassType",
    displayName="JoiningSystemUserLoggedOutConditionClassType",
    description="Indicates that a joining system user logged-out.",
)
class JoiningSystemUserLoggedOutConditionClassType(ns0.objtypes.BaseConditionClassType):
    pass


@o6.objecttype(
    nodeId="ns=ijt_base;i=1044",
    browseName="ns=ijt_base;StoppedEntityConditionClassType",
    displayName="StoppedEntityConditionClassType",
    description="Indicates that an entity is stopped.",
)
class StoppedEntityConditionClassType(ns0.objtypes.BaseConditionClassType):
    pass


@o6.objecttype(
    nodeId="ns=ijt_base;i=1047",
    browseName="ns=ijt_base;NotAvailableEntityConditionClassType",
    displayName="NotAvailableEntityConditionClassType",
    description="Indicates that an entity is not available.",
)
class NotAvailableEntityConditionClassType(ns0.objtypes.BaseConditionClassType):
    pass


@o6.objecttype(
    nodeId="ns=ijt_base;i=1048",
    browseName="ns=ijt_base;AssetLocationConditionClassType",
    displayName="AssetLocationConditionClassType",
    description="Indicates a change in the asset location.",
)
class AssetLocationConditionClassType(ns0.objtypes.BaseConditionClassType):
    pass


@o6.objecttype(
    nodeId="ns=ijt_base;i=1051",
    browseName="ns=ijt_base;LocationInZoneConditionClassType",
    displayName="LocationInZoneConditionClassType",
    description="Indicates the change of the entity location from out-of-zone to in-zone.",
)
class LocationInZoneConditionClassType(ns0.objtypes.BaseConditionClassType):
    pass


@o6.objecttype(
    nodeId="ns=ijt_base;i=1052",
    browseName="ns=ijt_base;NotSupportedEntityConditionClassType",
    displayName="NotSupportedEntityConditionClassType",
    description="Indicates that an entity is not supported.",
)
class NotSupportedEntityConditionClassType(ns0.objtypes.BaseConditionClassType):
    pass


@o6.objecttype(
    nodeId="ns=ijt_base;i=1054",
    browseName="ns=ijt_base;LocationOutOfZoneConditionClassType",
    displayName="LocationOutOfZoneConditionClassType",
    description="Indicates the change in the entity location from in-zone to out-of-zone.",
)
class LocationOutOfZoneConditionClassType(ns0.objtypes.BaseConditionClassType):
    pass


@o6.objecttype(
    nodeId="ns=ijt_base;i=1057",
    browseName="ns=ijt_base;DataValidationFailureConditionClassType",
    displayName="DataValidationFailureConditionClassType",
    description="Indicates a failure in the data validation.",
)
class DataValidationFailureConditionClassType(ns0.objtypes.BaseConditionClassType):
    pass


@o6.objecttype(
    nodeId="ns=ijt_base;i=1060",
    browseName="ns=ijt_base;InputValidationFailureConditionClassType",
    displayName="InputValidationFailureConditionClassType",
    description="Indicates a failure in the input validation.",
)
class InputValidationFailureConditionClassType(ns0.objtypes.BaseConditionClassType):
    pass


@o6.objecttype(
    nodeId="ns=ijt_base;i=1063", browseName="ns=ijt_base;ErrorConditionClassType", displayName="ErrorConditionClassType", description="Indicates an error in the system."
)
class ErrorConditionClassType(ns0.objtypes.BaseConditionClassType):
    pass


@o6.objecttype(
    nodeId="ns=ijt_base;i=1066",
    browseName="ns=ijt_base;SoftwareConditionClassType",
    displayName="SoftwareConditionClassType",
    description="Indicates a change in the software entity.",
)
class SoftwareConditionClassType(ns0.objtypes.BaseConditionClassType):
    pass


@o6.objecttype(
    nodeId="ns=ijt_base;i=1069",
    browseName="ns=ijt_base;HardwareConditionClassType",
    displayName="HardwareConditionClassType",
    description="Indicates a change in the hardware entity.",
)
class HardwareConditionClassType(ns0.objtypes.BaseConditionClassType):
    pass


@o6.objecttype(
    nodeId="ns=ijt_base;i=1072",
    browseName="ns=ijt_base;CertificateConditionClassType",
    displayName="CertificateConditionClassType",
    description="Indicates a change in the certificate.",
)
class CertificateConditionClassType(ns0.objtypes.BaseConditionClassType):
    pass


@o6.objecttype(
    nodeId="ns=ijt_base;i=1075", browseName="ns=ijt_base;LicenseConditionClassType", displayName="LicenseConditionClassType", description="Indicates a change in the license."
)
class LicenseConditionClassType(ns0.objtypes.BaseConditionClassType):
    pass


@o6.objecttype(
    nodeId="ns=ijt_base;i=1078",
    browseName="ns=ijt_base;MissingEntityConditionClassType",
    displayName="MissingEntityConditionClassType",
    description="Indicates that an entity is missing.",
)
class MissingEntityConditionClassType(ns0.objtypes.BaseConditionClassType):
    pass


@o6.objecttype(
    nodeId="ns=ijt_base;i=1081",
    browseName="ns=ijt_base;ExpiredEntityConditionClassType",
    displayName="ExpiredEntityConditionClassType",
    description="Indicates that an entity is expired.",
)
class ExpiredEntityConditionClassType(ns0.objtypes.BaseConditionClassType):
    pass


@o6.objecttype(
    nodeId="ns=ijt_base;i=1084",
    browseName="ns=ijt_base;InvalidEntityConditionClassType",
    displayName="InvalidEntityConditionClassType",
    description="Indicates that an entity is invalid.",
)
class InvalidEntityConditionClassType(ns0.objtypes.BaseConditionClassType):
    pass


@o6.objecttype(
    nodeId="ns=ijt_base;i=1087",
    browseName="ns=ijt_base;IncompatibleEntityConditionClassType",
    displayName="IncompatibleEntityConditionClassType",
    description="Indicates that an entity is incompatible.",
)
class IncompatibleEntityConditionClassType(ns0.objtypes.BaseConditionClassType):
    pass


@o6.objecttype(
    nodeId="ns=ijt_base;i=1090",
    browseName="ns=ijt_base;AcceptedEntityConditionClassType",
    displayName="AcceptedEntityConditionClassType",
    description="Indicates that an entity is accepted.",
)
class AcceptedEntityConditionClassType(ns0.objtypes.BaseConditionClassType):
    pass


@o6.objecttype(
    nodeId="ns=ijt_base;i=1093",
    browseName="ns=ijt_base;RejectedEntityConditionClassType",
    displayName="RejectedEntityConditionClassType",
    description="Indicates that an entity is rejected.",
)
class RejectedEntityConditionClassType(ns0.objtypes.BaseConditionClassType):
    pass


@o6.objecttype(
    nodeId="ns=ijt_base;i=1096",
    browseName="ns=ijt_base;AddedEntityConditionClassType",
    displayName="AddedEntityConditionClassType",
    description="Indicates that an entity is added.",
)
class AddedEntityConditionClassType(ns0.objtypes.BaseConditionClassType):
    pass


@o6.objecttype(
    nodeId="ns=ijt_base;i=1099",
    browseName="ns=ijt_base;UpdatedEntityConditionClassType",
    displayName="UpdatedEntityConditionClassType",
    description="Indicates that an entity is updated.",
)
class UpdatedEntityConditionClassType(ns0.objtypes.BaseConditionClassType):
    pass


@o6.objecttype(
    nodeId="ns=ijt_base;i=1102",
    browseName="ns=ijt_base;RemovedEntityConditionClassType",
    displayName="RemovedEntityConditionClassType",
    description="Indicates that an entity is removed.",
)
class RemovedEntityConditionClassType(ns0.objtypes.BaseConditionClassType):
    pass


@o6.objecttype(
    nodeId="ns=ijt_base;i=1105",
    browseName="ns=ijt_base;ReceivedEntityConditionClassType",
    displayName="ReceivedEntityConditionClassType",
    description="Indicates that an entity is received.",
)
class ReceivedEntityConditionClassType(ns0.objtypes.BaseConditionClassType):
    pass


ns0.objtypes.FolderType(
    nodeId="ns=ijt_base;i=5074", browseName="ns=machinery;MachineryBuildingBlocks", description="The MachineryBuildingBlocks contains building blocks from OPC UA for Machinery."
)


@o6.objecttype(
    nodeId="ns=ijt_base;i=1005",
    browseName="ns=ijt_base;JoiningSystemType",
    displayName="JoiningSystemType",
    description="The JoiningSystemType provides the overview of the information exposed from a given joining system.",
)
class JoiningSystemType(ns0.objtypes.BaseObjectType):
    assetManagement: di.objtypes.FunctionalGroupType | None
    identification: JoiningSystemIdentificationType
    joiningProcessManagement: JoiningProcessManagementType | None
    jointManagement: JointManagementType | None
    machineryBuildingBlocks: ns0.objtypes.FolderType | None = o6.hasComponent(o6.ns["ns=ijt_base;i=5074"])
    resultManagement: JoiningSystemResultManagementType | None


ns0.objtypes.FolderType(
    nodeId="ns=ijt_base;i=5080", browseName="ns=machinery;MachineryBuildingBlocks", description="The MachineryBuildingBlocks contains building blocks from OPC UA for Machinery."
)


@o6.objecttype(
    nodeId="ns=ijt_base;i=1002",
    browseName="ns=ijt_base;IJoiningSystemAssetType",
    displayName="IJoiningSystemAssetType",
    description="This is a generic interface common for all assets in a given Joining System. The purpose of this interface is to provide a standard way of identification and common information for all the assets. \nThis interface has a standard MachineryItemIdentificationType add-in which can be assigned with MachineIdentificationType or MachineryComponentIdentificationType for a given asset based on the requirement of the system.",
    isAbstract=True,
)
class IJoiningSystemAssetType(ns0.objtypes.BaseInterfaceType):
    health: di.objtypes.FunctionalGroupType | None
    identification: machinery.objtypes.MachineryItemIdentificationType
    lifetimeCounters: machinery.objtypes.MachineryLifetimeCounterType | None
    machineryBuildingBlocks: ns0.objtypes.FolderType | None = o6.hasComponent(o6.ns["ns=ijt_base;i=5080"])
    maintenance: di.objtypes.FunctionalGroupType | None
    monitoring: machinery.objtypes.MonitoringType | None
    notifications: machinery.objtypes.NotificationsType | None = o6.hasAddIn(
        machinery.objtypes.NotificationsType(nodeId="ns=ijt_base;i=5163", browseName="ns=machinery;Notifications", description="Provides notifications as events or objects.")
    )
    operationCounters: machinery.objtypes.MachineryOperationCounterType | None
    parameters: ns0.objtypes.FolderType | None


@o6.objecttype(nodeId="ns=ijt_base;i=1003", browseName="ns=ijt_base;IControllerType", displayName="IControllerType", isAbstract=True)
class IControllerType(IJoiningSystemAssetType):
    parameters: ns0.objtypes.FolderType


@o6.objecttype(nodeId="ns=ijt_base;i=1004", browseName="ns=ijt_base;IToolType", displayName="IToolType", isAbstract=True)
class IToolType(IJoiningSystemAssetType):
    parameters: ns0.objtypes.FolderType


@o6.objecttype(nodeId="ns=ijt_base;i=1008", browseName="ns=ijt_base;IServoType", displayName="IServoType", isAbstract=True)
class IServoType(IJoiningSystemAssetType):
    parameters: ns0.objtypes.FolderType


@o6.objecttype(nodeId="ns=ijt_base;i=1009", browseName="ns=ijt_base;IPowerSupplyType", displayName="IPowerSupplyType", isAbstract=True)
class IPowerSupplyType(IJoiningSystemAssetType):
    parameters: ns0.objtypes.FolderType


@o6.objecttype(nodeId="ns=ijt_base;i=1010", browseName="ns=ijt_base;IBatteryType", displayName="IBatteryType", isAbstract=True)
class IBatteryType(IJoiningSystemAssetType):
    parameters: ns0.objtypes.FolderType


@o6.objecttype(nodeId="ns=ijt_base;i=1011", browseName="ns=ijt_base;ISensorType", displayName="ISensorType", isAbstract=True)
class ISensorType(IJoiningSystemAssetType):
    parameters: ns0.objtypes.FolderType


@o6.objecttype(nodeId="ns=ijt_base;i=1012", browseName="ns=ijt_base;IFeederType", displayName="IFeederType", isAbstract=True)
class IFeederType(IJoiningSystemAssetType):
    parameters: ns0.objtypes.FolderType


@o6.objecttype(nodeId="ns=ijt_base;i=1013", browseName="ns=ijt_base;IMemoryDeviceType", displayName="IMemoryDeviceType", isAbstract=True)
class IMemoryDeviceType(IJoiningSystemAssetType):
    parameters: ns0.objtypes.FolderType


@o6.objecttype(nodeId="ns=ijt_base;i=1014", browseName="ns=ijt_base;ICableType", displayName="ICableType", isAbstract=True)
class ICableType(IJoiningSystemAssetType):
    parameters: ns0.objtypes.FolderType


@o6.objecttype(nodeId="ns=ijt_base;i=1015", browseName="ns=ijt_base;IAccessoryType", displayName="IAccessoryType", isAbstract=True)
class IAccessoryType(IJoiningSystemAssetType):
    parameters: ns0.objtypes.FolderType


@o6.objecttype(nodeId="ns=ijt_base;i=1016", browseName="ns=ijt_base;ISubComponentType", displayName="ISubComponentType", isAbstract=True)
class ISubComponentType(IJoiningSystemAssetType):
    parameters: ns0.objtypes.FolderType | None


@o6.objecttype(nodeId="ns=ijt_base;i=1019", browseName="ns=ijt_base;ISoftwareType", displayName="ISoftwareType", isAbstract=True)
class ISoftwareType(IJoiningSystemAssetType):
    pass


@o6.objecttype(nodeId="ns=ijt_base;i=1031", browseName="ns=ijt_base;IVirtualStationType", displayName="IVirtualStationType", isAbstract=True)
class IVirtualStationType(IJoiningSystemAssetType):
    pass


@o6.objecttype(
    nodeId="ns=ijt_base;i=1017",
    browseName="ns=ijt_base;IJoiningAdditionalInformationType",
    displayName="IJoiningAdditionalInformationType",
    description="The IJoiningAdditionalInformationType provides additional parameters for Identification of a given asset.",
    isAbstract=True,
)
class IJoiningAdditionalInformationType(ns0.objtypes.BaseInterfaceType):
    description: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=ijt_base;i=6175",
            browseName="ns=ijt_base;Description",
            description="Description is the system specific description of the asset.",
            dataType=o6.LocalizedText,
            value=o6.LocalizedText(),
        )
    )
    joiningTechnology: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=ijt_base;i=6176",
            browseName="ns=ijt_base;JoiningTechnology",
            description="JoiningTechnology is a human readable text to identify the joining technology.",
            dataType=o6.LocalizedText,
            value=o6.LocalizedText(),
        )
    )
    supplierCode: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=ijt_base;i=6452",
            browseName="ns=ijt_base;SupplierCode",
            description="SupplierCode is the SAP or ERP Supplier Code of the asset.",
            dataType=o6.String,
            value="",
        )
    )


@o6.objecttype(
    nodeId="ns=ijt_base;i=1029",
    browseName="ns=ijt_base;JoiningSystemIdentificationType",
    displayName="JoiningSystemIdentificationType",
    description="It provides identification parameters of the joining system.",
)
class JoiningSystemIdentificationType(di.objtypes.FunctionalGroupType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=ijt_base;i=6234",
            browseName="DefaultInstanceBrowseName",
            description="The default BrowseName for instances of the type.",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("di:Identification"),
        )
    )
    description: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=ijt_base;i=6242",
            browseName="ns=ijt_base;Description",
            description="It is the description of the system which could be written by the customer to identify the system. It could be the purpose of the system in the assembly line.",
            dataType=o6.LocalizedText,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    integratorName: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=ijt_base;i=6241",
            browseName="ns=ijt_base;IntegratorName",
            description="IntegratorName is the name of the system integrator.",
            dataType=o6.String,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    joiningTechnology: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=ijt_base;i=6244",
            browseName="ns=ijt_base;JoiningTechnology",
            description="JoiningTechnology is a human readable text to identify the joining technology of the joining system.",
            dataType=o6.LocalizedText,
        )
    )
    location: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=ijt_base;i=6458",
            browseName="ns=machinery;Location",
            description="Location is the location of the given system in the given plant or factory in text format.",
            dataType=o6.String,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    manufacturer: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=ijt_base;i=6245",
            browseName="ns=di;Manufacturer",
            description="Manufacturer provides a human-readable, localized name of the joining system manufacturer.",
            dataType=o6.LocalizedText,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    manufacturerUri: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=ijt_base;i=6246",
            browseName="ns=di;ManufacturerUri",
            description="ManufacturerUri provides a unique identifier for this company. This identifier should be a fully qualified domain name; however, it may be a GUID or similar construct that ensures global uniqueness.",
            dataType=o6.String,
        )
    )
    model: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=ijt_base;i=6247",
            browseName="ns=di;Model",
            description="Model provides the type of the joining system. Examples: Fixtured System, Handheld System, etc.",
            dataType=o6.LocalizedText,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    name: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=ijt_base;i=6240",
            browseName="ns=ijt_base;Name",
            description="Name is the name of the joining system. It can also be the standard browse name of the instance of JoiningSystemType.",
            dataType=o6.String,
        )
    )
    productInstanceUri: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=ijt_base;i=6236",
            browseName="ns=di;ProductInstanceUri",
            description="ProductInstanceUri is a globally unique resource identifier provided by the manufacturer.",
            dataType=o6.String,
        )
    )
    systemId: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=ijt_base;i=6248",
            browseName="ns=ijt_base;SystemId",
            description="SystemId is the system integrator specific identifier for the system. It represents a reference to the manufacturer ERP system.",
            dataType=o6.String,
            accessLevel=3,
            userAccessLevel=1,
        )
    )


ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6040",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(
            name="CalibrationData",
            dataType=o6.NodeId("ns=ijt_base;i=3003"),
            valueRank=-1,
            description=o6.LocalizedText("It is the input calibration data which needs to be configured for the asset."),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6041",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7005",
    browseName="ns=ijt_base;SetCalibration",
    description="The Method SetCalibration is used to set the calibration information of a given asset. \nIt is intended to set the basic calibration information and does not cover the certification process.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6040"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6041"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6043",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7006",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(
            name="Enable",
            dataType=o6.Boolean,
            valueRank=-1,
            description=o6.LocalizedText(
                "If true, it will enable the asset, else it will disable the asset. The default value is false.\nNote: If the asset is performing the joining operation when the method is executed, then it shall disable the asset after the current operation.",
                "",
            ),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6046",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7006",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7006",
    browseName="ns=ijt_base;EnableAsset",
    description="The Method EnableAsset is used to Enable or Disable a given asset. It is mostly applicable for Tool.\nThe joining system can report a respective event when an asset is enabled or disabled.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6043"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6046"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6047",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7007",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(
            name="Disconnect", dataType=o6.Boolean, valueRank=-1, description=o6.LocalizedText("If true, it will prepare the asset for disconnect. The default value is false.")
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6051",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7007",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7007",
    browseName="ns=ijt_base;DisconnectAsset",
    description="The Method DisconnectAsset is used to disconnect or connect the asset.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6047"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6051"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6053",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7008",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6055",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7008",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7008",
    browseName="ns=ijt_base;RebootAsset",
    description="The Method RebootAsset is used to reboot an asset.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6053"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6055"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6056",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7009",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(
            name="OfflineTimer",
            dataType=ns0.datatypes.Duration,
            valueRank=-1,
            description=o6.LocalizedText("It is the offlineTimer to be set. The behaviour of the asset when the timer is elapsed is application specific."),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6057",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7009",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7009",
    browseName="ns=ijt_base;SetOfflineTimer",
    description="The Method SetOfflineTimer is used to set the offline timer for the asset to determine how long the asset can perform the joining operations in an offline mode. \nNote: If an asset performs the joining operation in offline mode after setting the offline timer, the corresponding results generated shall have the IsGeneratedOffline flag set to TRUE.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6056"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6057"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6058",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7010",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(
            name="FeedbackType",
            dataType=o6.Int16,
            valueRank=-1,
            description=o6.LocalizedText(
                "It is the type of feedback and has the following pre-defined values:\n0 &#8211; UNDEFINED\n1 &#8211; OTHER\n2 &#8211; TEXT\n3 &#8211; VISUAL\n4 &#8211; AUDIO\n5 &#8211; VIBRATE",
                "",
            ),
        ),
        ns0.datatypes.Argument(name="FeedbackText", dataType=o6.String, valueRank=-1, description=o6.LocalizedText("It is the text feedback if the feedbackType is TEXT.")),
        ns0.datatypes.Argument(
            name="FeedbackFile",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "It is the file available in the asset which needs to be run for different types of feedback such as AUDIO, VIBRATE, etc. This can be retrieved using the GetFeedbackFileList method.\nIt is optional and not applicable for text feedback."
            ),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6059",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7010",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7010",
    browseName="ns=ijt_base;SendFeedback",
    description="The Method SendFeedback is used to send any type of feedback to a given asset. The feedback can be a text input or other types of feedback supported by the asset.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6058"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6059"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6061",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7011",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6062",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7011",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="FeedbackFileList",
            dataType=o6.String,
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText(
                "It is the list of feedback files available in the system. It contains the feedback filenames or the file paths which can be used as an input in SendFeedback method."
            ),
        ),
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7011",
    browseName="ns=ijt_base;GetFeedbackFileList",
    description="The Method GetFeedbackFileList is used to get the list of feedback files from the asset.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6061"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6062"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6063",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7012",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(
            name="SignalList",
            dataType=o6.NodeId("ns=ijt_base;i=3019"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText("It is the list of signals which needs to be set in the asset."),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6064",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7012",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="SignalStatusList",
            dataType=o6.Int32,
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText(
                "It is the list of status for each signal.\n0 &#8211; OK\nValues &gt; 0 are reserved for errors defined by this and future standards.\nValues &lt; 0 shall be used for application-specific errors."
            ),
        ),
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7012",
    browseName="ns=ijt_base;SetIOSignals",
    description="The Method SetIOSignals is used to set a list of IO signals of the asset. The type of operations mapped to each signal is application specific.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6063"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6064"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6067",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7013",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(
            name="SignalIdList",
            dataType=ns0.datatypes.TrimmedString,
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText("It is the list of signal identifiers requested. If it is empty, then all the available signals are returned from the asset."),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6068",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7013",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="SignalList",
            dataType=o6.NodeId("ns=ijt_base;i=3019"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText(
                "It is the list of signals which are available in the asset based on the input signalIdList. \nIf the signalIdList is empty, then all the available signals are sent from the asset."
            ),
        ),
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7013",
    browseName="ns=ijt_base;GetIOSignals",
    description="The Method GetIOSignals is used to get the list of available signals from the asset.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6067"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6068"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6069",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7014",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(
            name="IdentifierNames",
            dataType=ns0.datatypes.TrimmedString,
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText("The list of names of the identifiers which are requested. If it is empty, then all available identifiers are returned."),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6070",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7014",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="EntityList",
            dataType=o6.NodeId("ns=ijt_base;i=3010"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText("It is the list of identifiers available in the joining system based on the input criteria."),
        ),
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7014",
    browseName="ns=ijt_base;GetIdentifiers",
    description="The Method GetIdentifiers is used to get the list of identifiers available in the system which were managed by external systems.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6069"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6070"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6072",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7015",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(
            name="EntityList",
            dataType=o6.NodeId("ns=ijt_base;i=3010"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText("It is the list of identifiers sent to the joining system."),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6078",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7015",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7015",
    browseName="ns=ijt_base;SendIdentifiers",
    description="The Method SendIdentifiers is used to send one or more identifiers to the joining system.\nThese identifiers can be used for selection of a joining process, etc.\nThese identifiers can often be part of the generated result. \nThe input argument to this method is an array of EntityDataType structure where every entity in the joining system can be associated to a specific type for filtering.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6072"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6078"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6079",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7016",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(
            name="IdentifierList",
            dataType=ns0.datatypes.TrimmedString,
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText("It is the list of identifiers sent to the joining system."),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6080",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7016",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7016",
    browseName="ns=ijt_base;SendTextIdentifiers",
    description="The Method SendTextIdentifiers is used to send one or more identifiers to a joining system. \nThese identifiers can be used for selection of a joining process, etc.\nThese identifiers can often be part of the generated result. \nNote: The decision on which set of identifiers are used for the selection of a joining process and which set of identifiers should be part of the generated result is application specific.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6079"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6080"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6081",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7017",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(
            name="IdentifierList",
            dataType=ns0.datatypes.TrimmedString,
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText(
                "It is the list of names of the identifiers which are requested to be reset. \nIf it is NOT empty, then resetAll and resetLatest flags are ignored.\nIf it is empty, then the resetAll or resetLatest flag is used."
            ),
        ),
        ns0.datatypes.Argument(
            name="ResetAll",
            dataType=o6.Boolean,
            valueRank=-1,
            description=o6.LocalizedText(
                "If True, it will reset all the identifiers available in the joining system and resetLatest flag is ignored.\nIf False and identifierList is empty then the resetLatest flag is used.\n"
            ),
        ),
        ns0.datatypes.Argument(
            name="ResetLatest",
            dataType=o6.Boolean,
            valueRank=-1,
            description=o6.LocalizedText(
                "If True, it will reset the latest identifier available in the system.\nNote: This is provided for supporting legacy systems. The criteria to determine which identifier is latest is application specific.",
                "",
            ),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6085",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7017",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7017",
    browseName="ns=ijt_base;ResetIdentifiers",
    description="The Method ResetIdentifiers is used to reset the specified identifiers.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6081"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6085"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6086",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7018",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(
            name="OperationType",
            dataType=o6.Int32,
            valueRank=-1,
            description=o6.LocalizedText(
                "It is the type of operation. The list of integer values corresponding to a specific operation is provided by the documentation or the joining system via some interface."
            ),
        ),
        ns0.datatypes.Argument(
            name="OperationText", dataType=o6.String, valueRank=-1, description=o6.LocalizedText("It is the optional text to provide information on the type of operation.")
        ),
        ns0.datatypes.Argument(
            name="VendorName",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText("It is the optional vendor&#8217;s name provided to identify the type of operations supported."),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6087",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7018",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7018",
    browseName="ns=ijt_base;ExecuteOperation",
    description="The Method ExecuteOperation is an application specific interface to execute any generic operations supported by a joining system.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6086"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6087"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6088",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7019",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(
            name="ErrorId",
            dataType=ns0.datatypes.TrimmedString,
            valueRank=-1,
            description=o6.LocalizedText(
                "It is the identifier of the error. It could be available as part of the JoiningResult.\nNote: If it is empty, the Server is allowed to return the latest error available.",
                "",
            ),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6102",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7019",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="ErrorContent",
            dataType=ns0.datatypes.BaseDataType,
            valueRank=-1,
            description=o6.LocalizedText("It is the detailed error information.\nExamples: Log file, Detailed Error Information or Event Logs, etc.\n", ""),
        ),
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7019",
    browseName="ns=ijt_base;GetErrorInformation",
    description="The Method GetErrorInformation is used to get the error information based on the input identifier. The details returned from the joining system is application specific.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6088"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6102"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6183",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7020",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(
            name="Joint",
            dataType=o6.NodeId("ns=ijt_base;i=3028"),
            valueRank=-1,
            description=o6.LocalizedText("With this argument the Client can provide the content of the joint."),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6184",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7020",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7020",
    browseName="ns=ijt_base;SendJoint",
    description="The Method SendJoint is used to send a joint to a joining system. If the input joint already exists in the system, it shall be overwritten.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6183"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6184"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6186",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7021",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(
            name="JointDesign",
            dataType=o6.NodeId("ns=ijt_base;i=3025"),
            valueRank=-1,
            description=o6.LocalizedText("With this argument the Client can provide the content of the joint design."),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6191",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7021",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7021",
    browseName="ns=ijt_base;SendJointDesign",
    description="The Method SendJointDesign is used to send a joint design to a joining system. If the input joint design already exists in the system, it shall be overwritten.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6186"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6191"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6192",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7022",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(
            name="JointComponent",
            dataType=o6.NodeId("ns=ijt_base;i=3021"),
            valueRank=-1,
            description=o6.LocalizedText("With this argument the Client can provide the joint component."),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6228",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7022",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7022",
    browseName="ns=ijt_base;SendJointComponent",
    description="The Method SendJointComponent is used to send a joint component to a joining system. If the input joint component already exists in the system, it shall be overwritten.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6192"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6228"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6229",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7023",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(
            name="JointId",
            dataType=ns0.datatypes.TrimmedString,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the joint which should be selected for performing the next joining operation."
            ),
        ),
        ns0.datatypes.Argument(
            name="JointOriginId",
            dataType=ns0.datatypes.TrimmedString,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the common identifier of the joint which should be selected for performing the next joining operation.\n\nIt is optional and can be empty if the underlying system does not manage revisions of a joint. If JointId is provided, then this argument shall be ignored."
            ),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6230",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7023",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7023",
    browseName="ns=ijt_base;SelectJoint",
    description="The Method SelectJoint is used to select the joint and the associated joining process.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6229"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6230"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6235",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7024",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6303",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7024",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="JointList",
            dataType=o6.NodeId("ns=ijt_base;i=3028"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText("It is the list of joints available in the system."),
        ),
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7024",
    browseName="ns=ijt_base;GetJointList",
    description="The Method GetJointList is used to get the list of available joints in the system.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6235"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6303"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6304",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7025",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6305",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7025",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="JointDesignList",
            dataType=o6.NodeId("ns=ijt_base;i=3025"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText("It is the list of joint designs available in the system."),
        ),
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7025",
    browseName="ns=ijt_base;GetJointDesignList",
    description="The Method GetJointDesignList is used to get the list of available joint designs in the system.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6304"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6305"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6306",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7026",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6307",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7026",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="JointComponentList",
            dataType=o6.NodeId("ns=ijt_base;i=3021"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText("It is the list of joint components available in the system."),
        ),
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7026",
    browseName="ns=ijt_base;GetJointComponentList",
    description="The Method GetJointComponentList is used to get the list of available joint components in the system.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6306"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6307"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6308",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7027",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(
            name="JointOriginId",
            dataType=ns0.datatypes.TrimmedString,
            valueRank=-1,
            description=o6.LocalizedText("It is the origin identifier of the joint which is used to manage the revisions of a given joint."),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6309",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7027",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="JointList",
            dataType=o6.NodeId("ns=ijt_base;i=3028"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText("It is the list of joints available in the system."),
        ),
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7027",
    browseName="ns=ijt_base;GetJointRevisionList",
    description="The Method GetJointRevisionList is used to get the list available revisions of a specific joint based on the JointOriginId.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6308"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6309"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6310",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7028",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(name="JointId", dataType=ns0.datatypes.TrimmedString, valueRank=-1, description=o6.LocalizedText("It is the identifier of the joint.")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6311",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7028",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="Joint", dataType=o6.NodeId("ns=ijt_base;i=3028"), valueRank=-1, description=o6.LocalizedText("It is the joint based on the input identifier.")
        ),
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7028",
    browseName="ns=ijt_base;GetJoint",
    description="The Method GetJoint is used to get the joint based on the input identifier.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6310"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6311"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6312",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7029",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(
            name="JointDesignId", dataType=ns0.datatypes.TrimmedString, valueRank=-1, description=o6.LocalizedText("It is the joint design based on the input identifier.")
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6313",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7029",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="JointDesign", dataType=o6.NodeId("ns=ijt_base;i=3025"), valueRank=-1, description=o6.LocalizedText("It is the joint design based on the input identifier.")
        ),
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7029",
    browseName="ns=ijt_base;GetJointDesign",
    description="The Method GetJointDesign is used to get the joint design based on the input identifier.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6312"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6313"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6314",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7030",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(
            name="JointComponentId", dataType=ns0.datatypes.TrimmedString, valueRank=-1, description=o6.LocalizedText("It is the identifier of the joint component.")
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6315",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7030",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="JointComponent", dataType=o6.NodeId("ns=ijt_base;i=3021"), valueRank=-1, description=o6.LocalizedText("It is the joint component based on the input identifier.")
        ),
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7030",
    browseName="ns=ijt_base;GetJointComponent",
    description="The Method GetJointComponent is used to get the joint component based on the input identifier.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6314"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6315"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6340",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7042",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(
            name="JoiningProcess",
            dataType=o6.NodeId("ns=ijt_base;i=3016"),
            valueRank=-1,
            description=o6.LocalizedText("With this argument the Client can provide the content of the joining process."),
        ),
        ns0.datatypes.Argument(
            name="SelectionName",
            dataType=ns0.datatypes.TrimmedString,
            valueRank=-1,
            description=o6.LocalizedText("With this argument the Client can provide the required selection name for the given joining process. It is optional and can be empty."),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6347",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7042",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7042",
    browseName="ns=ijt_base;SendJoiningProcess",
    description="The Method SendJoiningProcess is used to send a joining process to the joining system. It can be used to insert a joining program or joining batch or joining job or any other process applicable to a joining system. It shall overwrite the joining process if it already exists in the joining system.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6340"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6347"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6348",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7043",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6349",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7043",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="JoiningProcessList",
            dataType=o6.NodeId("ns=ijt_base;i=3024"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText("It is the list of joining process meta data available in the system."),
        ),
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7043",
    browseName="ns=ijt_base;GetJoiningProcessList",
    description="The Method GetJoiningProcessList is used to get the list of joining process meta data available in the system.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6348"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6349"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6350",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7044",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(
            name="JoiningProcessOriginId",
            dataType=ns0.datatypes.TrimmedString,
            valueRank=-1,
            description=o6.LocalizedText("It is the origin identifier of the joining process which is used to manage the revisions of a given joining process."),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6351",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7044",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="JoiningProcessList",
            dataType=o6.NodeId("ns=ijt_base;i=3024"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText("It is the list of joining process meta data available in the system."),
        ),
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7044",
    browseName="ns=ijt_base;GetJoiningProcessRevisionList",
    description="The Method GetJoiningProcessRevisionList is used to get the list available revisions of a specific joining process based on the joiningProcessOriginId.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6350"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6351"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6352",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7045",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(
            name="JoiningProcessIdentification",
            dataType=o6.NodeId("ns=ijt_base;i=3029"),
            valueRank=-1,
            description=o6.LocalizedText(
                "It is the identification information of the joining process which can be used to map the respective joiningProcessId with selectionName and joiningProcessOriginId.\n\nIt shall at least contain the joiningProcessId and selectionName."
            ),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6353",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7045",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7045",
    browseName="ns=ijt_base;SetJoiningProcessMapping",
    description="The Method SetJoiningProcessMapping is used to set the mapping of the joining process in a joining system. It can be used to map a joining process to a selection name.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6352"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6353"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6354",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7046",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(
            name="JoiningProcessIdentification",
            dataType=o6.NodeId("ns=ijt_base;i=3029"),
            valueRank=-1,
            description=o6.LocalizedText(
                "It is the identification information of the joining process which can be used to select the joiningProcess. \n\nIf it includes joiningProcessId then it is used for the selection and other arguments are ignored.\n\nIf it does not include joiningProcessId, then the system checks for joiningProcessOriginId which will be used for the selection.\n\nIf joiningProcessId and joiningProcessOriginId are not available, then the system uses the selectionName for the selection of the joining process."
            ),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6355",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7046",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7046",
    browseName="ns=ijt_base;SelectJoiningProcess",
    description="The Method SelectJoiningProcess is used to select the joining process based on the input arguments.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6354"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6355"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6356",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7047",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6357",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7047",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7047",
    browseName="ns=ijt_base;DeselectJoiningProcess",
    description="The Method DeselectJoiningProcess is used to deselect any selected joining process.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6356"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6357"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6358",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7048",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(
            name="JoiningProcessIdentification",
            dataType=o6.NodeId("ns=ijt_base;i=3029"),
            valueRank=-1,
            description=o6.LocalizedText(
                "It is the identification information of the joining process which can be used to select the joiningProcess. \n\nIf it includes joiningProcessId then it is used for the selection and other arguments are ignored.\n\nIf it does not include joiningProcessId, then the system checks for joiningProcessOriginId which will be used for the selection.\n\nIf joiningProcessId and joiningProcessOriginId are not available, then the system uses the selectionName for the selection of the joining process."
            ),
        ),
        ns0.datatypes.Argument(
            name="IncrementCount",
            dataType=o6.UInt32,
            valueRank=-1,
            description=o6.LocalizedText("It is the number of increments to be done for the joining process counter.\nThe default value is 1 if it is not provided."),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6359",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7048",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7048",
    browseName="ns=ijt_base;IncrementJoiningProcessCounter",
    description="The Method IncrementJoiningProcessCounter is used to increment the counter of the sequential joining processes such as Job, etc.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6358"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6359"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6360",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7049",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(
            name="JoiningProcessIdentification",
            dataType=o6.NodeId("ns=ijt_base;i=3029"),
            valueRank=-1,
            description=o6.LocalizedText(
                "It is the identification information of the joining process which can be used to select the joiningProcess. \n\nIf it includes joiningProcessId then it is used for the selection and other arguments are ignored.\n\nIf it does not include joiningProcessId, then the system checks for joiningProcessOriginId which will be used for the selection.\n\nIf joiningProcessId and joiningProcessOriginId are not available, then the system uses the selectionName for the selection of the joining process."
            ),
        ),
        ns0.datatypes.Argument(
            name="DecrementCount",
            dataType=o6.UInt32,
            valueRank=-1,
            description=o6.LocalizedText("It is the number of decrements to be done for the joining process counter.\nThe default value is 1 if it is not provided."),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6361",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7049",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7049",
    browseName="ns=ijt_base;DecrementJoiningProcessCounter",
    description="The Method DecrementJoiningProcessCounter used to decrement the counter of the sequential joining processes such as Job, etc.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6360"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6361"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6362",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7050",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(
            name="JoiningProcessIdentification",
            dataType=o6.NodeId("ns=ijt_base;i=3029"),
            valueRank=-1,
            description=o6.LocalizedText(
                "It is the identification information of the joining process which can be used to select the joiningProcess. \n\nIf it includes joiningProcessId then it is used for the selection and other arguments are ignored.\n\nIf it does not include joiningProcessId, then the system checks for joiningProcessOriginId which will be used for the selection.\n\nIf joiningProcessId and joiningProcessOriginId are not available, then the system uses the selectionName for the selection of the joining process."
            ),
        ),
        ns0.datatypes.Argument(name="CounterValue", dataType=o6.UInt32, valueRank=-1, description=o6.LocalizedText("It is the new counter value for the joining process.")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6363",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7050",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7050",
    browseName="ns=ijt_base;SetJoiningProcessCounter",
    description="The Method SetJoiningProcessCounter is used to set the counter of a sequential joining processes (such as Job, etc.) to the given input value.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6362"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6363"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6364",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7051",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(
            name="JoiningProcessIdentification",
            dataType=o6.NodeId("ns=ijt_base;i=3029"),
            valueRank=-1,
            description=o6.LocalizedText(
                "It is the identification information of the joining process which can be used to select the joiningProcess. \n\nIf it includes joiningProcessId then it is used for the selection and other arguments are ignored.\n\nIf it does not include joiningProcessId, then the system checks for joiningProcessOriginId which will be used for the selection.\n\nIf joiningProcessId and joiningProcessOriginId are not available, then the system uses the selectionName for the selection of the joining process."
            ),
        ),
        ns0.datatypes.Argument(name="MaxCounterSize", dataType=o6.UInt32, valueRank=-1, description=o6.LocalizedText("It is the maximum counter size for the joining process.")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6365",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7051",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7051",
    browseName="ns=ijt_base;SetJoiningProcessSize",
    description="The Method SetJoiningProcessSize is used to set the size of the batch joining process.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6364"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6365"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6366",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7052",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(
            name="JoiningProcessIdentification",
            dataType=o6.NodeId("ns=ijt_base;i=3029"),
            valueRank=-1,
            description=o6.LocalizedText(
                "It is the identification information of the joining process which can be used to select the joiningProcess. \n\nIf it includes joiningProcessId then it is used for the selection and other arguments are ignored.\n\nIf it does not include joiningProcessId, then the system checks for joiningProcessOriginId which will be used for the selection.\n\nIf joiningProcessId and joiningProcessOriginId are not available, then the system uses the selectionName for the selection of the joining process."
            ),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6367",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7052",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7052",
    browseName="ns=ijt_base;ResetJoiningProcess",
    description="The Method ResetJoiningProcess is used to reset/restart the sequential joining processes such as Job, etc.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6366"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6367"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6368",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7053",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(
            name="JoiningProcessIdentification",
            dataType=o6.NodeId("ns=ijt_base;i=3029"),
            valueRank=-1,
            description=o6.LocalizedText(
                "It is the identification information of the joining process which can be used to select the joiningProcess. \n\nIf it includes joiningProcessId then it is used for the selection and other arguments are ignored.\n\nIf it does not include joiningProcessId, then the system checks for joiningProcessOriginId which will be used for the selection.\n\nIf joiningProcessId and joiningProcessOriginId are not available, then the system uses the selectionName for the selection of the joining process."
            ),
        ),
        ns0.datatypes.Argument(
            name="AbortMessage",
            dataType=o6.LocalizedText,
            valueRank=-1,
            description=o6.LocalizedText("It is an optional message sent from the Client to the joining system to indicate the reason for aborting the joining operation."),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6369",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7053",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7053",
    browseName="ns=ijt_base;AbortJoiningProcess",
    description="The Method AbortJoiningProcess is used to abort the input joining process if it is under execution.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6368"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6369"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6127",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7054",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(
            name="JoiningProcessIdentification",
            dataType=o6.NodeId("ns=ijt_base;i=3029"),
            valueRank=-1,
            description=o6.LocalizedText(
                "It is the identification information of the joining process which can be used to select the joiningProcess. \n\nIf it includes joiningProcessId then it is used for the selection and other arguments are ignored.\n\nIf it does not include joiningProcessId, then the system checks for joiningProcessOriginId which will be used for the selection.\n\nIf joiningProcessId and joiningProcessOriginId are not available, then the system uses the selectionName for the selection of the joining process."
            ),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6140",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7054",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7054",
    browseName="ns=ijt_base;DeleteJoiningProcess",
    description="The Method DeleteJoiningProcess is used to delete the input joining process.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6127"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6140"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6141",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7055",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(name="JointId", dataType=ns0.datatypes.TrimmedString, valueRank=-1, description=o6.LocalizedText("It is the identifier of the joint.")),
        ns0.datatypes.Argument(
            name="JointOriginId",
            dataType=ns0.datatypes.TrimmedString,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the common identifier of the joint which should be selected for performing the next joining operation.\n\nIt is optional and can be empty if the underlying system does not manage revisions of a joint. If jointId is provided, then this argument shall be ignored."
            ),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6151",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7055",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7055",
    browseName="ns=ijt_base;DeleteJoint",
    description="The Method DeleteJoint is used to delete the joint based on the input identifier.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6141"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6151"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6374",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7056",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(
            name="JoiningProcessIdentification",
            dataType=o6.NodeId("ns=ijt_base;i=3029"),
            valueRank=-1,
            description=o6.LocalizedText(
                "It is the identification information of the joining process which can be used to select the joiningProcess. \n\nIf it includes joiningProcessId then it is used for the selection and other arguments are ignored.\n\nIf it does not include joiningProcessId, then the system checks for joiningProcessOriginId which will be used for the selection.\n\nIf joiningProcessId and joiningProcessOriginId are not available, then the system uses the selectionName for the selection of the joining process."
            ),
        ),
        ns0.datatypes.Argument(
            name="AssociatedEntities",
            dataType=o6.NodeId("ns=ijt_base;i=3010"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText("It is the list of identifiers used for performing the joining operation. It is optional and can be empty."),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6375",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7056",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7056",
    browseName="ns=ijt_base;StartJoiningProcess",
    description="The Method StartJoiningProcess is used to start the input joining process. \nNote: It is not intended to be used in a hard real-time use case.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6374"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6375"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6153",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7064",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(name="JointDesignId", dataType=ns0.datatypes.TrimmedString, valueRank=-1, description=o6.LocalizedText("It is the identifier of the joint design.")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6161",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7064",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7064",
    browseName="ns=ijt_base;DeleteJointDesign",
    description="The Method DeleteJointDesign is used to delete the joint design based on the input identifier.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6153"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6161"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6162",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7071",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(
            name="JointComponentId", dataType=ns0.datatypes.TrimmedString, valueRank=-1, description=o6.LocalizedText("It is the identifier of the joint component.")
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6163",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7071",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7071",
    browseName="ns=ijt_base;DeleteJointComponent",
    description="The Method DeleteJointComponent is used to delete the joint component based on the input identifier.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6162"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6163"]),
)


@o6.objecttype(
    nodeId="ns=ijt_base;i=1023",
    browseName="ns=ijt_base;JointManagementType",
    displayName="JointManagementType",
    description="The JointManagementType provides access to the Joint and associated information.",
)
class JointManagementType(ns0.objtypes.BaseObjectType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=ijt_base;i=6339",
            browseName="DefaultInstanceBrowseName",
            description="The default BrowseName for instances of the type.",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("JointManagement"),
        )
    )
    deleteJoint: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=ijt_base;i=7055"])
    deleteJointComponent: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=ijt_base;i=7071"])
    deleteJointDesign: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=ijt_base;i=7064"])
    getJoint: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=ijt_base;i=7028"])
    getJointComponent: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=ijt_base;i=7030"])
    getJointComponentList: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=ijt_base;i=7026"])
    getJointDesign: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=ijt_base;i=7029"])
    getJointDesignList: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=ijt_base;i=7025"])
    getJointList: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=ijt_base;i=7024"])
    getJointRevisionList: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=ijt_base;i=7027"])
    selectJoint: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=ijt_base;i=7023"])
    sendJoint: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=ijt_base;i=7020"])
    sendJointComponent: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=ijt_base;i=7022"])
    sendJointDesign: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=ijt_base;i=7021"])


ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6406",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7072",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(name="InputTime", dataType=ns0.datatypes.UtcTime, valueRank=-1, description=o6.LocalizedText("It is the input time to be configured in the asset.")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6407",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7072",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7072",
    browseName="ns=ijt_base;SetTime",
    description="The Method SetTime is used to set the time of the asset manually. It is recommended to be used only when an asset does not have automated time synchronization.\nThe joining system can report a respective event when the time is configured manually using this method.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6406"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6407"]),
)


@o6.objecttype(
    nodeId="ns=ijt_base;i=1026",
    browseName="ns=ijt_base;JoiningSystemAssetMethodSetType",
    displayName="JoiningSystemAssetMethodSetType",
    description="The JoiningSystemAssetMethodSetType provides a set of methods for various assets in a joining system.",
)
class JoiningSystemAssetMethodSetType(ns0.objtypes.BaseObjectType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=ijt_base;i=6295",
            browseName="DefaultInstanceBrowseName",
            description="The default BrowseName for instances of the type.",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("di:MethodSet"),
        )
    )
    disconnectAsset: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=ijt_base;i=7007"])
    enableAsset: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=ijt_base;i=7006"])
    executeOperation: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=ijt_base;i=7018"])
    getErrorInformation: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=ijt_base;i=7019"])
    getFeedbackFileList: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=ijt_base;i=7011"])
    getIOSignals: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=ijt_base;i=7013"])
    getIdentifiers: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=ijt_base;i=7014"])
    rebootAsset: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=ijt_base;i=7008"])
    resetIdentifiers: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=ijt_base;i=7017"])
    sendFeedback: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=ijt_base;i=7010"])
    sendIdentifiers: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=ijt_base;i=7015"])
    sendTextIdentifiers: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=ijt_base;i=7016"])
    setCalibration: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=ijt_base;i=7005"])
    setIOSignals: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=ijt_base;i=7012"])
    setOfflineTimer: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=ijt_base;i=7009"])
    setTime: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=ijt_base;i=7072"])


ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6408",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7073",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(
            name="DeselectAfterJoining",
            dataType=o6.Boolean,
            valueRank=-1,
            description=o6.LocalizedText("If True, it will deselect the existing joining process after the joining operation is completed. The default value is False."),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6409",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7073",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7073",
    browseName="ns=ijt_base;StartSelectedJoining",
    description="The Method StartSelectedJoining is used to start the selected joining. The joining operation can be selected using SelectJoiningProcess or SelectJoint. \nNote: It is not intended to be used in a hard real-time use case.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6408"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6409"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6459",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7074",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0.datatypes.Argument(
            name="FromSequenceNumber",
            dataType=o6.UInt64,
            valueRank=-1,
            description=o6.LocalizedText(
                "The starting sequence number for the Requested Results.\n\nIt is a required argument if results are requested based on the input sequence number range.\n\nIt shall be a valid value &gt; 0.\nIf 0, then fromTime and toTime are used.",
                "en",
            ),
        ),
        ns0.datatypes.Argument(
            name="ToSequenceNumber",
            dataType=o6.UInt64,
            valueRank=-1,
            description=o6.LocalizedText(
                "The ending sequence number of the Requested Results.\n\nIt is a required argument if results are requested based on the input sequence number range.\n\nIt shall be a valid value &gt; 0 and shall be &gt;= fromSequenceNumber.\nIf 0, then fromTime and toTime are used.",
                "en",
            ),
        ),
        ns0.datatypes.Argument(
            name="FromTime",
            dataType=ns0.datatypes.UtcTime,
            valueRank=-1,
            description=o6.LocalizedText(
                "It is the start time for the Requested Results.\n\nThis argument is considered only when fromSequenceNumber and toSequenceNumber are set as 0.", "en"
            ),
        ),
        ns0.datatypes.Argument(
            name="ToTime",
            dataType=ns0.datatypes.UtcTime,
            valueRank=-1,
            description=o6.LocalizedText(
                "It is the end time for the Requested Results.\n\nThis argument is considered only when fromSequenceNumber and toSequenceNumber are set as 0.", "en"
            ),
        ),
        ns0.datatypes.Argument(
            name="RequestedMinimumDurationBetweenResults",
            dataType=ns0.datatypes.Duration,
            valueRank=-1,
            description=o6.LocalizedText(
                "The client can use this argument to configure a time interval between each Result to optimize the number of Results sent from the Server.\n\nThe Server can return the revised interval if the requested interval is not supported.\n\nNote: It is only a requested minimum time interval by the client and the server could take additional time for processing.",
                "en",
            ),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6460",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7074",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="RevisedMinimumDurationBetweenResults",
            dataType=ns0.datatypes.Duration,
            valueRank=-1,
            description=o6.LocalizedText("It is the minimum revised interval supported by the server.", "en"),
        ),
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.", "en")),
        ns0.datatypes.Argument(
            name="StatusMessage",
            dataType=o6.LocalizedText,
            valueRank=-1,
            description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.", "en"),
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7074",
    browseName="ns=ijt_base;RequestResults",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6459"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6460"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6461",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7091",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running.",
                "en",
            ),
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6462",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7091",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="SelectedJoiningProgram",
            dataType=o6.NodeId("ns=ijt_base;i=3024"),
            valueRank=-1,
            description=o6.LocalizedText("It is the selected joining program for the input asset.", "en"),
        ),
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.", "en")),
        ns0.datatypes.Argument(
            name="StatusMessage",
            dataType=o6.LocalizedText,
            valueRank=-1,
            description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.", "en"),
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7091",
    browseName="ns=ijt_base;GetSelectedJoiningProgram",
    description="The Method GetSelectedJoiningProgram is used to get the selected joining program for a given asset.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6461"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6462"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6470",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7092",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="MaxResults",
            dataType=o6.UInt32,
            valueRank=-1,
            description=o6.LocalizedText("It is the maximum results requested by the Client.\n\nIf 0, then the Server shall send all the unacknowledged results.", "en"),
        ),
        ns0.datatypes.Argument(
            name="RequestedMinimumDurationBetweenResults",
            dataType=ns0.datatypes.Duration,
            valueRank=-1,
            description=o6.LocalizedText(
                "The client can use this argument to configure a time interval between each Result to optimize the number of Results sent from the Server.\n\nThe Server can return the revised interval if the requested interval is not supported.\n\nNote: It is only a requested minimum time interval by the client and the server could take additional time for processing.",
                "en",
            ),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6471",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7092",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.Argument(
            name="RevisedMinimumDurationBetweenResults",
            dataType=ns0.datatypes.Duration,
            valueRank=-1,
            description=o6.LocalizedText("It is the minimum revised interval supported by the server.", "en"),
        ),
        ns0.datatypes.Argument(
            name="UnacknowledgedResultCount", dataType=o6.UInt32, valueRank=-1, description=o6.LocalizedText("It is the total count of unacknowledged results in the server.", "en")
        ),
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.", "en")),
        ns0.datatypes.Argument(
            name="StatusMessage",
            dataType=o6.LocalizedText,
            valueRank=-1,
            description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.", "en"),
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7092",
    browseName="ns=ijt_base;RequestUnacknowledgedResults",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6470"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6471"]),
)


@o6.objecttype(
    nodeId="ns=ijt_base;i=1022",
    browseName="ns=ijt_base;JoiningSystemResultManagementType",
    displayName="JoiningSystemResultManagementType",
    description="The JoiningSystemResultManagementType is a subtype of ResultManagementType and provides mechanism to access results generated by the underlying joining system.",
)
class JoiningSystemResultManagementType(machinery_result.objtypes.ResultManagementType):
    requestResults: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=ijt_base;i=7074"])
    requestUnacknowledgedResults: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=ijt_base;i=7092"])
    results: ns0.objtypes.FolderType | None


o6.reference(JoiningSystemResultManagementType, "i=41", JoiningSystemResultReadyEventType)
o6.reference(JoiningSystemResultManagementType, "i=41", RequestedResultEventType)


ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6448",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7093",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="ProductInstanceUri",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the Client can provide the identifier of the asset on which this method is applicable.\nIt can be empty if the method is modelled directly under the required asset. If it is empty, the system can consider the identifier of the asset where the Server is running."
            ),
        ),
        ns0.datatypes.Argument(
            name="JoiningProcessId", dataType=ns0.datatypes.TrimmedString, valueRank=-1, description=o6.LocalizedText("It is the identifier of the joining process.")
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=ijt_base;i=6449",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=ijt_base;i=7093",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.Argument(
            name="JoiningProcess", dataType=o6.NodeId("ns=ijt_base;i=3016"), valueRank=-1, description=o6.LocalizedText("It is the joining process available in the system.")
        ),
        ns0.datatypes.Argument(
            name="SelectionName",
            dataType=ns0.datatypes.TrimmedString,
            valueRank=-1,
            description=o6.LocalizedText("It is the selection name of the joining process configured in the system."),
        ),
        ns0.datatypes.Argument(name="Status", dataType=o6.Int64, valueRank=-1, description=o6.LocalizedText("It provides the status of the Method execution.")),
        ns0.datatypes.Argument(
            name="StatusMessage", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("It provides the high-level status information in a user-friendly text.")
        ),
    ],
)
o6.call(
    nodeId="ns=ijt_base;i=7093",
    browseName="ns=ijt_base;GetJoiningProcess",
    description="The Method GetJoiningProcess is used to get the joining process based on the input identifier.",
    inputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6448"]),
    outputArgs=o6.hasProperty(o6.ns["ns=ijt_base;i=6449"]),
)


@o6.objecttype(
    nodeId="ns=ijt_base;i=1025",
    browseName="ns=ijt_base;JoiningProcessManagementType",
    displayName="JoiningProcessManagementType",
    description="The JoiningProcessManagementType provides access to various joining processes in a joining system.",
)
class JoiningProcessManagementType(ns0.objtypes.BaseObjectType):
    abortJoiningProcess: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=ijt_base;i=7053"])
    decrementJoiningProcessCounter: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=ijt_base;i=7049"])
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=ijt_base;i=6338",
            browseName="DefaultInstanceBrowseName",
            description="The default BrowseName for instances of the type.",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("JoiningProcessManagement"),
        )
    )
    deleteJoiningProcess: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=ijt_base;i=7054"])
    deselectJoiningProcess: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=ijt_base;i=7047"])
    getJoiningProcess: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=ijt_base;i=7093"])
    getJoiningProcessList: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=ijt_base;i=7043"])
    getJoiningProcessRevisionList: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=ijt_base;i=7044"])
    getSelectedJoiningProgram: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=ijt_base;i=7091"])
    incrementJoiningProcessCounter: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=ijt_base;i=7048"])
    resetJoiningProcess: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=ijt_base;i=7052"])
    selectJoiningProcess: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=ijt_base;i=7046"])
    sendJoiningProcess: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=ijt_base;i=7042"])
    setJoiningProcessCounter: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=ijt_base;i=7050"])
    setJoiningProcessMapping: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=ijt_base;i=7045"])
    setJoiningProcessSize: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=ijt_base;i=7051"])
    startJoiningProcess: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=ijt_base;i=7056"])
    startSelectedJoining: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=ijt_base;i=7073"])


del Any, TYPE_CHECKING, uuid, o6, amb, di, ia, machinery, machinery_result, ns0, ijt_base_datypes, ijt_base_vartypes
