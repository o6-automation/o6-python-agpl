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

"""Generated OPC UA machinery namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.ns0 as ns0

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(
    nodeId="ns=machinery;i=1006",
    browseName="ns=machinery;MachineComponentsType",
    displayName="MachineComponentsType",
    description="Contains all identifiable components of a machine",
)
class MachineComponentsType(ns0.objtypes.BaseObjectType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machinery;i=6018",
            browseName="DefaultInstanceBrowseName",
            description="The default BrowseName for instances of the type.",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("machinery:Components"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    langleComponentRangle: ns0.objtypes.BaseObjectType | None


@o6.objecttype(
    nodeId="ns=machinery;i=1002",
    browseName="ns=machinery;MachineryItemState_StateMachineType",
    displayName="MachineryItemState_StateMachineType",
    description="State machine representing the state of a machinery item",
)
class MachineryItemState_StateMachineType(ns0.objtypes.FiniteStateMachineType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machinery;i=6021",
            browseName="DefaultInstanceBrowseName",
            description="The default BrowseName for instances of the type",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("machinery:MachineryItemState"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    executing: ns0.objtypes.StateType
    fromExecutingToExecuting: ns0.objtypes.TransitionType
    fromExecutingToNotAvailable: ns0.objtypes.TransitionType
    fromExecutingToNotExecuting: ns0.objtypes.TransitionType
    fromExecutingToOutOfService: ns0.objtypes.TransitionType
    fromNotAvailableToExecuting: ns0.objtypes.TransitionType
    fromNotAvailableToNotAvailable: ns0.objtypes.TransitionType
    fromNotAvailableToNotExecuting: ns0.objtypes.TransitionType
    fromNotAvailableToOutOfService: ns0.objtypes.TransitionType
    fromNotExecutingToExecuting: ns0.objtypes.TransitionType
    fromNotExecutingToNotAvailable: ns0.objtypes.TransitionType
    fromNotExecutingToNotExecuting: ns0.objtypes.TransitionType
    fromNotExecutingToOutOfService: ns0.objtypes.TransitionType
    fromOutOfServiceToExecuting: ns0.objtypes.TransitionType
    fromOutOfServiceToNotAvailable: ns0.objtypes.TransitionType
    fromOutOfServiceToNotExecuting: ns0.objtypes.TransitionType
    fromOutOfServiceToOutOfService: ns0.objtypes.TransitionType
    notAvailable: ns0.objtypes.StateType
    notExecuting: ns0.objtypes.StateType
    outOfService: ns0.objtypes.StateType


@o6.objecttype(
    nodeId="ns=machinery;i=1003",
    browseName="ns=machinery;IMachineryItemVendorNameplateType",
    displayName="IMachineryItemVendorNameplateType",
    description="Interface containing identification and nameplate information for a MachineryItem provided by the vendor",
    isAbstract=True,
)
class IMachineryItemVendorNameplateType(di.objtypes.IVendorNameplateType):
    initialOperationDate: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machinery;i=6027",
            browseName="ns=machinery;InitialOperationDate",
            description="The date, when the MachineryItem was switched on the first time after it has left the manufacturer plant.",
            dataType=o6.DateTime,
        )
    )
    manufacturer: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machinery;i=6022",
            browseName="ns=di;Manufacturer",
            description="A human-readable, localized name of the manufacturer of the MachineryItem.",
            dataType=o6.LocalizedText,
        )
    )
    monthOfConstruction: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machinery;i=6026",
            browseName="ns=machinery;MonthOfConstruction",
            description="The month in which the manufacturing process of the MachineryItem has been completed. It shall be a number between 1 and 12, representing the month from January to December.",
            dataType=o6.Byte,
        )
    )
    serialNumber: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machinery;i=6024",
            browseName="ns=di;SerialNumber",
            description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
            dataType=o6.String,
        )
    )
    yearOfConstruction: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machinery;i=6025",
            browseName="ns=machinery;YearOfConstruction",
            description="The year (Gregorian calendar) in which the manufacturing process of the MachineryItem has been completed. It shall be a four-digit number and never change during the life-cycle of a MachineryItem.",
            dataType=o6.UInt16,
        )
    )


@o6.objecttype(
    nodeId="ns=machinery;i=1010",
    browseName="ns=machinery;IMachineVendorNameplateType",
    displayName="IMachineVendorNameplateType",
    description="Interface containing identification and nameplate information for a machine provided by the machine vendor",
    isAbstract=True,
)
class IMachineVendorNameplateType(IMachineryItemVendorNameplateType):
    productInstanceUri: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machinery;i=6023",
            browseName="ns=di;ProductInstanceUri",
            description="A globally unique resource identifier provided by the manufacturer of the machine",
            dataType=o6.String,
        )
    )


@o6.objecttype(
    nodeId="ns=machinery;i=1011",
    browseName="ns=machinery;IMachineTagNameplateType",
    displayName="IMachineTagNameplateType",
    description="Interface containing information of the identification of a machine set by the customer",
    isAbstract=True,
)
class IMachineTagNameplateType(di.objtypes.ITagNameplateType):
    location: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machinery;i=6028",
            browseName="ns=machinery;Location",
            description="To be used by end users to store the location of the machine in a scheme specific to the end user Servers shall support at least 60 Unicode characters for the clients writing this value, this means clients can expect to be able to write strings with a length of 60 Unicode characters into that field.",
            dataType=o6.String,
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=machinery;i=1008",
    browseName="ns=machinery;MachineryOperationModeStateMachineType",
    displayName="MachineryOperationModeStateMachineType",
    description="State machine representing the operation mode of a MachineryItem",
)
class MachineryOperationModeStateMachineType(ns0.objtypes.FiniteStateMachineType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machinery;i=6058",
            browseName="DefaultInstanceBrowseName",
            description="The default BrowseName for instances of the type",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("machinery:MachineryOperationMode"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    fromMaintenanceToMaintenance: ns0.objtypes.TransitionType
    fromMaintenanceToNone: ns0.objtypes.TransitionType
    fromMaintenanceToProcessing: ns0.objtypes.TransitionType
    fromMaintenanceToSetup: ns0.objtypes.TransitionType
    fromNoneToMaintenance: ns0.objtypes.TransitionType
    fromNoneToNone: ns0.objtypes.TransitionType
    fromNoneToProcessing: ns0.objtypes.TransitionType
    fromNoneToSetup: ns0.objtypes.TransitionType
    fromProcessingToMaintenance: ns0.objtypes.TransitionType
    fromProcessingToNone: ns0.objtypes.TransitionType
    fromProcessingToProcessing: ns0.objtypes.TransitionType
    fromProcessingToSetup: ns0.objtypes.TransitionType
    fromSetupToMaintenance: ns0.objtypes.TransitionType
    fromSetupToNone: ns0.objtypes.TransitionType
    fromSetupToProcessing: ns0.objtypes.TransitionType
    fromSetupToSetup: ns0.objtypes.TransitionType
    maintenance: ns0.objtypes.StateType
    none: ns0.objtypes.StateType
    processing: ns0.objtypes.StateType
    setup: ns0.objtypes.StateType


@o6.objecttype(
    nodeId="ns=machinery;i=1009",
    browseName="ns=machinery;MachineryOperationCounterType",
    displayName="MachineryOperationCounterType",
    interfaces=[di.objtypes.IOperationCounterType],
)
class MachineryOperationCounterType(di.objtypes.FunctionalGroupType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machinery;i=6082",
            browseName="DefaultInstanceBrowseName",
            description="The default BrowseName for instances of the type",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("di:OperationCounters"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    operationCycleCounter: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machinery;i=6081",
            browseName="ns=di;OperationCycleCounter",
            description="OperationCycleCounter is counting the times the component switches from not performing an activity to performing an activity. For example, each time a valve starts moving, is counted. This value shall only increase during the lifetime of the component and shall not be reset when the component is restarted.",
            dataType=ns0.datatypes.UInteger,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    operationDuration: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machinery;i=6080",
            browseName="ns=di;OperationDuration",
            description="OperationDuration is the duration the MachineryItem has been powered and performing an activity. This counter is intended for machines and components where a distinction is made between switched on and in operation. For example, a drive might be powered on but not operating. It is not intended for machines or components always performing an activity like sensors always measuring data. This value shall only increase during the lifetime of the MachineryItem and shall not be reset when it is restarted. The OperationDuration is provided as Duration, i.e., in milliseconds or even fractions of a millisecond. However, the Server is not expected to update the value in such a high frequency, but maybe once a minute or once an hour, depending on the application.",
            dataType=ns0.datatypes.Duration,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    powerOnDuration: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machinery;i=6079",
            browseName="ns=di;PowerOnDuration",
            description="PowerOnDuration is the duration the MachineryItem has been powered. The main purpose is to determine the time in which degradation of the MachineryItem occurred. The details, when the time is counted, is implementation-specific. Companion specifications might define specific rules. Typically, when the MachineryItem has supply voltage and the main CPU is running, the time is counted. This may include any kind of sleep mode, but may not include pure Wake on LAN. This value shall only increase during the lifetime of the MachineryItem and shall not be reset when it is restarted. The PowerOnDuration is provided as Duration, i.e., in milliseconds or even fractions of a millisecond. However, the Server is not expected to update the value in such a high frequency, but maybe once a minute or once an hour, depending on the application.",
            dataType=ns0.datatypes.Duration,
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(nodeId="ns=machinery;i=1015", browseName="ns=machinery;MachineryLifetimeCounterType", displayName="MachineryLifetimeCounterType")
class MachineryLifetimeCounterType(ns0.objtypes.FolderType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machinery;i=6087",
            browseName="DefaultInstanceBrowseName",
            description="The default BrowseName for instances of the type",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("machinery:LifetimeCounters"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    langleLifetimeVariableRangle: di.vartypes.LifetimeVariableType


@o6.objecttype(
    nodeId="ns=machinery;i=1004",
    browseName="ns=machinery;MachineryItemIdentificationType",
    displayName="MachineryItemIdentificationType",
    description="Contains information about the identification and nameplate of a MachineryItem",
    isAbstract=True,
    interfaces=[di.objtypes.ITagNameplateType, IMachineryItemVendorNameplateType],
)
class MachineryItemIdentificationType(di.objtypes.FunctionalGroupType):
    assetId: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machinery;i=6013",
            browseName="ns=di;AssetId",
            description="To be used by end users to store a unique identification in the context of their overall application. Servers shall support at least 40 Unicode characters for the clients writing this value, this means clients can expect to be able to write strings with a length of 40 Unicode characters into that field.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    componentName: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machinery;i=6014",
            browseName="ns=di;ComponentName",
            description="To be used by end users to store a human-readable localized text for the MachineryItem. The minimum number of locales supported for this property shall be two. Servers shall support at least 40 Unicode characters for the clients writing the text part of each locale, this means clients can expect to be able to write texts with a length of 40 Unicode characters into that field.",
            dataType=o6.LocalizedText,
            value=o6.LocalizedText(),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machinery;i=6088",
            browseName="DefaultInstanceBrowseName",
            description="The default BrowseName for instances of the type.",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("di:Identification"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    deviceClass: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machinery;i=6012", browseName="ns=di;DeviceClass", description="Indicates in which domain or for what purpose the MachineryItem is used.", dataType=o6.String
        )
    )
    hardwareRevision: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machinery;i=6010",
            browseName="ns=di;HardwareRevision",
            description="A string representation of the revision level of the hardware of a MachineryItem. Hardware is physical equipment, as opposed to programs, procedures, rules and associated documentation. Many machines will not provide such information due to the modular and configurable nature of the machine.",
            dataType=o6.String,
        )
    )
    initialOperationDate: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machinery;i=6006",
            browseName="ns=machinery;InitialOperationDate",
            description="The date, when the MachineryItem was switched on the first time after it has left the manufacturer plant.",
            dataType=o6.DateTime,
        )
    )
    manufacturer: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machinery;i=6002",
            browseName="ns=di;Manufacturer",
            description="A human-readable, localized name of the manufacturer of the MachineryItem.",
            dataType=o6.LocalizedText,
        )
    )
    manufacturerUri: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machinery;i=6007",
            browseName="ns=di;ManufacturerUri",
            description="A globally unique identifier of the manufacturer of the MachineryItem.",
            dataType=o6.String,
        )
    )
    model: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machinery;i=6008", browseName="ns=di;Model", description="A human-readable, localized name of the model of the MachineryItem.", dataType=o6.LocalizedText
        )
    )
    monthOfConstruction: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machinery;i=6005",
            browseName="ns=machinery;MonthOfConstruction",
            description="The month in which the manufacturing process of the MachineryItem has been completed. It shall be a number between 1 and 12, representing the month from January to December.",
            dataType=o6.Byte,
        )
    )
    productCode: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machinery;i=6009",
            browseName="ns=di;ProductCode",
            description="A machine-readable string of the model of the MachineryItem, that might include options like the hardware configuration of the model. This information might be provided by the ERP system of the vendor. For example, it can be used as order information.",
            dataType=o6.String,
        )
    )
    productInstanceUri: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machinery;i=6001",
            browseName="ns=di;ProductInstanceUri",
            description="A globally unique resource identifier provided by the manufacturer of the MachineryItem.",
            dataType=o6.String,
        )
    )
    serialNumber: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machinery;i=6003",
            browseName="ns=di;SerialNumber",
            description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
            dataType=o6.String,
        )
    )
    softwareRevision: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machinery;i=6011",
            browseName="ns=di;SoftwareRevision",
            description="A string representation of the revision level of a MachineryItem. In most cases, MachineryItems consist of several software components. In that case, information about the software components might be provided as additional information in the address space, including individual revision information. In that case, this property is either not provided or provides an overall software revision level. The value might change during the life-cycle of a MachineryItem.",
            dataType=o6.String,
        )
    )
    yearOfConstruction: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machinery;i=6004",
            browseName="ns=machinery;YearOfConstruction",
            description="The year (Gregorian calendar) in which the manufacturing process of the MachineryItem has been completed. It shall be a four-digit number and never change during the life-cycle of a MachineryItem.",
            dataType=o6.UInt16,
        )
    )


@o6.objecttype(
    nodeId="ns=machinery;i=1005",
    browseName="ns=machinery;MachineryComponentIdentificationType",
    displayName="MachineryComponentIdentificationType",
    description="Contains information about the identification and nameplate of a component",
)
class MachineryComponentIdentificationType(MachineryItemIdentificationType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machinery;i=6016",
            browseName="DefaultInstanceBrowseName",
            description="The default BrowseName for instances of the type.",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("di:Identification"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    deviceRevision: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machinery;i=6017",
            browseName="ns=di;DeviceRevision",
            description="A string representation of the overall revision level of the component. Often, it is increased when either the SoftwareRevision and / or the HardwareRevision of the component is increased. As an example, it can be used in ERP systems together with the ProductCode.",
            dataType=o6.String,
        )
    )


@o6.objecttype(
    nodeId="ns=machinery;i=1012",
    browseName="ns=machinery;MachineIdentificationType",
    displayName="MachineIdentificationType",
    description="Contains information about the identification and nameplate of a machine",
    interfaces=[IMachineVendorNameplateType, IMachineTagNameplateType],
)
class MachineIdentificationType(MachineryItemIdentificationType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machinery;i=6030",
            browseName="DefaultInstanceBrowseName",
            description="The default BrowseName for instances of the type.",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("di:Identification"),
        )
    )
    location: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machinery;i=6029",
            browseName="ns=machinery;Location",
            description="To be used by end users to store the location of the machine in a scheme specific to the end user. Servers shall support at least 60 Unicode characters for the clients writing this value, this means clients can expect to be able to write strings with a length of 60 Unicode characters into that field.",
            dataType=o6.String,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    productInstanceUri: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machinery;i=6015",
            browseName="ns=di;ProductInstanceUri",
            description="A globally unique resource identifier provided by the manufacturer of the machine",
            dataType=o6.String,
        )
    )


@o6.objecttype(
    nodeId="ns=machinery;i=1014", browseName="ns=machinery;MonitoringType", displayName="MonitoringType", description="Entry point for monitoring information of a MachineryItem."
)
class MonitoringType(ns0.objtypes.FolderType):
    consumption: ns0.objtypes.FolderType | None = o6.hasComponent(
        ns0.objtypes.FolderType(nodeId="ns=machinery;i=5047", browseName="ns=machinery;Consumption", description="Entry point for consumption information of the MachineryItem.")
    )
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machinery;i=6089",
            browseName="DefaultInstanceBrowseName",
            description="The default BrowseName for instances of the type.",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("machinery:Monitoring"),
        )
    )
    health: ns0.objtypes.FolderType | None
    process: ns0.objtypes.FolderType | None = o6.hasComponent(
        ns0.objtypes.FolderType(nodeId="ns=machinery;i=5046", browseName="ns=machinery;Process", description="Entry point for process information of the MachineryItem.")
    )
    status: ns0.objtypes.FolderType | None


@o6.objecttype(
    nodeId="ns=machinery;i=1013",
    browseName="ns=machinery;MachineryEquipmentFolderType",
    displayName="MachineryEquipmentFolderType",
    description="Defines an entry point for MachineryEquipment of a MachineryItem.",
)
class MachineryEquipmentFolderType(ns0.objtypes.FolderType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machinery;i=6105",
            browseName="DefaultInstanceBrowseName",
            description="The default BrowseName for instances of the type.",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("machinery:MachineryEquipment"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    langleMachineryEquipmentRangle: ns0.objtypes.BaseObjectType | None


@o6.objecttype(
    nodeId="ns=machinery;i=1017", browseName="ns=machinery;NotificationsType", displayName="NotificationsType", description="Provides notifications as events or objects."
)
class NotificationsType(ns0.objtypes.FolderType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machinery;i=6106",
            browseName="DefaultInstanceBrowseName",
            description="The default BrowseName for instances of the type.",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("machinery:Notifications"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=machinery;i=1007",
    browseName="ns=machinery;IMachineryEquipmentType",
    displayName="IMachineryEquipmentType",
    description="Provides base identification information of MachineryEquipment that can be set by the user.",
    isAbstract=True,
)
class IMachineryEquipmentType(IMachineTagNameplateType):
    description: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machinery;i=6107",
            browseName="ns=machinery;Description",
            description="Additional information and description about the MachineryEquipment. Should be used if Description Attribute cannot be written via OPC UA and should be ideally identical to Description Attribute.",
            dataType=o6.LocalizedText,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    equipmentLife: di.vartypes.LifetimeVariableType | None
    machineryEquipmentTypeId: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machinery;i=6108",
            browseName="ns=machinery;MachineryEquipmentTypeId",
            description="Identification of a generic MachineryEquipment. Defined by each company (e.g., company has an MachineryEquipmentTypeId for all 8 mm drills).",
            dataType=o6.String,
            accessLevel=3,
            userAccessLevel=1,
        )
    )


del Any, TYPE_CHECKING, uuid, o6, di, ia, ns0
