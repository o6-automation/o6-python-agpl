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

"""Generated OPC UA profinet namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.ns0 as ns0
from . import reftypes as profinet_reftypes
from . import datatypes as profinet_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(nodeId="ns=profinet;i=1004", browseName="ns=profinet;PnTopologyChangedEventType", displayName="PnTopologyChangedEventType")
class PnTopologyChangedEventType(ns0.objtypes.BaseEventType):
    pass


@o6.objecttype(nodeId="ns=profinet;i=1007", browseName="ns=profinet;PnAssetContainerType", displayName="PnAssetContainerType")
class PnAssetContainerType(ns0.objtypes.BaseObjectType):
    langleAssetsRangle: PnAssetType | None


@o6.objecttype(nodeId="ns=profinet;i=1009", browseName="ns=profinet;PnInterfaceContainerType", displayName="PnInterfaceContainerType")
class PnInterfaceContainerType(ns0.objtypes.BaseObjectType):
    langleInterfacesRangle: ns0.objtypes.BaseObjectType | None


@o6.objecttype(nodeId="ns=profinet;i=1016", browseName="ns=profinet;NetworkComponentFeatureType", displayName="NetworkComponentFeatureType", isAbstract=True)
class NetworkComponentFeatureType(ns0.objtypes.BaseObjectType):
    pass


@o6.objecttype(nodeId="ns=profinet;i=1021", browseName="ns=profinet;PnRealSubmoduleContainerType", displayName="PnRealSubmoduleContainerType")
class PnRealSubmoduleContainerType(ns0.objtypes.BaseObjectType):
    langleSubmodulesRangle: ns0.objtypes.BaseObjectType | None


@o6.objecttype(nodeId="ns=profinet;i=1023", browseName="ns=profinet;PnExpectedSubmoduleContainerType", displayName="PnExpectedSubmoduleContainerType")
class PnExpectedSubmoduleContainerType(ns0.objtypes.BaseObjectType):
    langleSubmodulesRangle: ns0.objtypes.BaseObjectType | None


@o6.objecttype(nodeId="ns=profinet;i=1026", browseName="ns=profinet;PnRealModuleContainerType", displayName="PnRealModuleContainerType")
class PnRealModuleContainerType(ns0.objtypes.BaseObjectType):
    langleModulesRangle: ns0.objtypes.BaseObjectType | None


@o6.objecttype(nodeId="ns=profinet;i=1028", browseName="ns=profinet;PnExpectedModuleContainerType", displayName="PnExpectedModuleContainerType")
class PnExpectedModuleContainerType(ns0.objtypes.BaseObjectType):
    langleModulesRangle: ns0.objtypes.BaseObjectType | None


@o6.objecttype(nodeId="ns=profinet;i=1030", browseName="ns=profinet;PnApplicationRelationContainerType", displayName="PnApplicationRelationContainerType")
class PnApplicationRelationContainerType(ns0.objtypes.BaseObjectType):
    langleARsRangle: PnApplicationRelationType | None


@o6.objecttype(nodeId="ns=profinet;i=1033", browseName="ns=profinet;PnEquipmentContainerType", displayName="PnEquipmentContainerType")
class PnEquipmentContainerType(ns0.objtypes.BaseObjectType):
    langlePnEquipmentsRangle: ns0.objtypes.BaseObjectType | None


@o6.objecttype(nodeId="ns=profinet;i=1031", browseName="ns=profinet;IPnDomainType", displayName="IPnDomainType", isAbstract=True)
class IPnDomainType(ns0.objtypes.BaseInterfaceType):
    nodes: PnEquipmentContainerType = o6.hasComponent(PnEquipmentContainerType(nodeId="ns=profinet;i=5036", browseName="ns=profinet;Nodes"))


@o6.objecttype(nodeId="ns=profinet;i=1002", browseName="ns=profinet;PnDiagnosisAlarmType", displayName="PnDiagnosisAlarmType")
class PnDiagnosisAlarmType(ns0.objtypes.AlarmConditionType):
    aPI: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6024", browseName="ns=profinet;API", dataType=o6.UInt32))
    accumulative: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6029", browseName="ns=profinet;Accumulative", dataType=profinet_datypes.PnChannelAccumulativeEnumeration)
    )
    channelErrorType: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6034", browseName="ns=profinet;ChannelErrorType", dataType=o6.UInt16)
    )
    channelNumber: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6027", browseName="ns=profinet;ChannelNumber", dataType=o6.UInt16))
    direction: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6032", browseName="ns=profinet;Direction", dataType=profinet_datypes.PnChannelDirectionEnumeration)
    )
    extChannelAddValue: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6036", browseName="ns=profinet;ExtChannelAddValue", dataType=o6.UInt32)
    )
    extChannelErrorType: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6035", browseName="ns=profinet;ExtChannelErrorType", dataType=o6.UInt16)
    )
    helpText: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6039", browseName="ns=profinet;HelpText", dataType=o6.LocalizedText)
    )
    maintenance: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6030", browseName="ns=profinet;Maintenance", dataType=profinet_datypes.PnChannelMaintenanceEnumeration)
    )
    manufacturerData: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6038", browseName="ns=profinet;ManufacturerData", dataType=o6.ByteString)
    )
    qualifiedChannelQualifier: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6037", browseName="ns=profinet;QualifiedChannelQualifier", dataType=o6.UInt32)
    )
    slot: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6025", browseName="ns=profinet;Slot", dataType=o6.UInt16))
    specifier: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6031", browseName="ns=profinet;Specifier", dataType=profinet_datypes.PnChannelSpecifierEnumeration)
    )
    subslot: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6026", browseName="ns=profinet;Subslot", dataType=o6.UInt16))
    type: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6028", browseName="ns=profinet;Type", dataType=profinet_datypes.PnChannelTypeEnumeration)
    )
    userStructureIdentifier: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6033", browseName="ns=profinet;UserStructureIdentifier", dataType=o6.UInt16)
    )


@o6.objecttype(nodeId="ns=profinet;i=1003", browseName="ns=profinet;PnAssetChangedEventType", displayName="PnAssetChangedEventType")
class PnAssetChangedEventType(ns0.objtypes.BaseEventType):
    assetChange: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6041", browseName="ns=profinet;AssetChange", dataType=profinet_datypes.PnAssetChangeEnumeration)
    )
    assetType: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6040", browseName="ns=profinet;AssetType", dataType=profinet_datypes.PnAssetTypeEnumeration)
    )


@o6.objecttype(nodeId="ns=profinet;i=1006", browseName="ns=profinet;PnAssetType", displayName="PnAssetType")
class PnAssetType(ns0.objtypes.BaseObjectType):
    annotation: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6067", browseName="ns=profinet;Annotation", dataType=o6.String))
    deviceId: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6075", browseName="ns=profinet;DeviceId", dataType=o6.UInt16))
    deviceSubId: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6076", browseName="ns=profinet;DeviceSubId", dataType=o6.UInt16))
    hardwareRevision: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6070", browseName="ns=profinet;HardwareRevision", dataType=o6.String)
    )
    location: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6066", browseName="ns=profinet;Location", dataType=o6.String))
    orderId: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6068", browseName="ns=profinet;OrderId", dataType=o6.String))
    organization: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6073", browseName="ns=profinet;Organization", dataType=o6.UInt16))
    serialNumber: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6071", browseName="ns=profinet;SerialNumber", dataType=o6.String))
    softwareRevision: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6069", browseName="ns=profinet;SoftwareRevision", dataType=o6.String)
    )
    typeIdentification: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6072", browseName="ns=profinet;TypeIdentification", dataType=o6.UInt16)
    )
    uniqueIdentifier: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6065", browseName="ns=profinet;UniqueIdentifier", dataType=o6.Guid)
    )
    vendorId: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6074", browseName="ns=profinet;VendorId", dataType=o6.UInt16))


o6.reference(PnAssetType, "i=41", PnAssetChangedEventType)


@o6.objecttype(nodeId="ns=profinet;i=1012", browseName="ns=profinet;PnPortStatisticType", displayName="PnPortStatisticType")
class PnPortStatisticType(ns0.objtypes.BaseObjectType):
    inDiscards: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=profinet;i=6105", browseName="ns=profinet;InDiscards", dataType=o6.UInt32)
    )
    inErrors: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=profinet;i=6107", browseName="ns=profinet;InErrors", dataType=o6.UInt32)
    )
    inOctets: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=profinet;i=6103", browseName="ns=profinet;InOctets", dataType=o6.UInt32)
    )
    outDiscards: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=profinet;i=6106", browseName="ns=profinet;OutDiscards", dataType=o6.UInt32)
    )
    outErrors: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=profinet;i=6108", browseName="ns=profinet;OutErrors", dataType=o6.UInt32)
    )
    outOctets: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=profinet;i=6104", browseName="ns=profinet;OutOctets", dataType=o6.UInt32)
    )


@o6.objecttype(nodeId="ns=profinet;i=1013", browseName="ns=profinet;NetworkComponentType", displayName="NetworkComponentType", isAbstract=True)
class NetworkComponentType(ns0.objtypes.BaseObjectType):
    enabled: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=profinet;i=6109", browseName="ns=profinet;Enabled", dataType=o6.Boolean)
    )
    langleComponentNameRangle: NetworkComponentType | None
    langleFeatureNameRangle: NetworkComponentFeatureType | None = o6.hasComponent(
        NetworkComponentFeatureType(nodeId="ns=profinet;i=5014", browseName="ns=profinet;<FeatureName>", modellingRule="OptionalPlaceholder", _allow_abstract=True)
    )


@o6.objecttype(nodeId="ns=profinet;i=1017", browseName="ns=profinet;IPv4FeatureType", displayName="IPv4FeatureType")
class IPv4FeatureType(NetworkComponentFeatureType):
    defaultGateway: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=profinet;i=6113", browseName="ns=profinet;DefaultGateway", dataType=o6.Byte, valueRank=1, arrayDimensions=[4])
    )
    dhcpEnabled: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=profinet;i=6114", browseName="ns=profinet;DhcpEnabled", dataType=o6.Boolean)
    )
    ipAddress: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=profinet;i=6111", browseName="ns=profinet;IpAddress", dataType=o6.Byte, valueRank=1, arrayDimensions=[4])
    )
    subnetMask: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=profinet;i=6112", browseName="ns=profinet;SubnetMask", dataType=o6.Byte, valueRank=1, arrayDimensions=[4])
    )


@o6.objecttype(nodeId="ns=profinet;i=1018", browseName="ns=profinet;PnSubmoduleStateType", displayName="PnSubmoduleStateType")
class PnSubmoduleStateType(ns0.objtypes.BaseObjectType):
    aRInfo: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=profinet;i=6128", browseName="ns=profinet;ARInfo", dataType=profinet_datypes.PnSubmoduleARInfoEnumeration)
    )
    addInfo: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=profinet;i=6123", browseName="ns=profinet;AddInfo", dataType=profinet_datypes.PnSubmoduleAddInfoEnumeration)
    )
    diagInfo: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=profinet;i=6127", browseName="ns=profinet;DiagInfo", dataType=o6.Boolean)
    )
    identInfo: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=profinet;i=6129", browseName="ns=profinet;IdentInfo", dataType=profinet_datypes.PnSubmoduleIdentInfoEnumeration)
    )
    maintenanceDemanded: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=profinet;i=6126", browseName="ns=profinet;MaintenanceDemanded", dataType=o6.Boolean)
    )
    maintenanceRequired: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=profinet;i=6125", browseName="ns=profinet;MaintenanceRequired", dataType=o6.Boolean)
    )
    qualifiedInfo: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=profinet;i=6124", browseName="ns=profinet;QualifiedInfo", dataType=o6.Boolean)
    )


@o6.objecttype(nodeId="ns=profinet;i=1019", browseName="ns=profinet;IPnSubmoduleType", displayName="IPnSubmoduleType", isAbstract=True)
class IPnSubmoduleType(ns0.objtypes.BaseInterfaceType):
    aPI: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6130", browseName="ns=profinet;API", dataType=o6.UInt32))
    gSDDescription: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6134", browseName="ns=profinet;GSDDescription", dataType=o6.String)
    )
    gSDName: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6133", browseName="ns=profinet;GSDName", dataType=o6.String))
    identNumber: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6132", browseName="ns=profinet;IdentNumber", dataType=o6.UInt32))
    subslot: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6131", browseName="ns=profinet;Subslot", dataType=o6.UInt16))


@o6.objecttype(nodeId="ns=profinet;i=1022", browseName="ns=profinet;IPnExpectedSubmoduleType", displayName="IPnExpectedSubmoduleType", isAbstract=True)
class IPnExpectedSubmoduleType(IPnSubmoduleType):
    state: PnSubmoduleStateType | None = o6.hasComponent(PnSubmoduleStateType(nodeId="ns=profinet;i=5026", browseName="ns=profinet;State"))


@o6.objecttype(nodeId="ns=profinet;i=1020", browseName="ns=profinet;IPnRealSubmoduleType", displayName="IPnRealSubmoduleType", isAbstract=True)
class IPnRealSubmoduleType(IPnSubmoduleType):
    alarms: ns0.objtypes.FolderType | None = o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=profinet;i=5024", browseName="ns=profinet;Alarms"))
    diagnosis: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=profinet;i=6143",
            browseName="ns=profinet;Diagnosis",
            dataType=profinet_datypes.PnDeviceDiagnosisDataType,
            valueRank=1,
            arrayDimensions=[1],
            value=[
                profinet_datypes.PnDeviceDiagnosisDataType(
                    aPI=0,
                    slot=0,
                    subslot=0,
                    channelNumber=0,
                    type=profinet_datypes.PnChannelTypeEnumeration.UNSPECIFIC,
                    accumulative=profinet_datypes.PnChannelAccumulativeEnumeration.SINGLE,
                    maintenance=profinet_datypes.PnChannelMaintenanceEnumeration.FAULT,
                    specifier=profinet_datypes.PnChannelSpecifierEnumeration.ALL_DISAPPEARS,
                    direction=profinet_datypes.PnChannelDirectionEnumeration.MANUFACTURER_SPECIFIC,
                    userStructureIdentifier=0,
                    channelErrorType=0,
                    extChannelErrorType=0,
                    extChannelAddValue=0,
                    qualifiedChannelQualifier=0,
                    manufacturerData=b"",
                    message=o6.LocalizedText(),
                    helpText=o6.LocalizedText(),
                )
            ],
        )
    )
    iM: PnIdentificationType | None


o6.reference(IPnRealSubmoduleType, "i=41", PnDiagnosisAlarmType)
o6.reference(IPnRealSubmoduleType, "i=41", PnAssetChangedEventType)


@o6.objecttype(nodeId="ns=profinet;i=1024", browseName="ns=profinet;IPnModuleType", displayName="IPnModuleType", isAbstract=True)
class IPnModuleType(ns0.objtypes.BaseInterfaceType):
    gSDDescription: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6147", browseName="ns=profinet;GSDDescription", dataType=o6.String)
    )
    gSDName: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6146", browseName="ns=profinet;GSDName", dataType=o6.String))
    identNumber: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6145", browseName="ns=profinet;IdentNumber", dataType=o6.UInt32))
    slot: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6144", browseName="ns=profinet;Slot", dataType=o6.UInt16))


@o6.objecttype(nodeId="ns=profinet;i=1025", browseName="ns=profinet;IPnRealModuleType", displayName="IPnRealModuleType", isAbstract=True)
class IPnRealModuleType(IPnModuleType):
    alarms: ns0.objtypes.FolderType | None = o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=profinet;i=5030", browseName="ns=profinet;Alarms"))
    diagnosis: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=profinet;i=6156",
            browseName="ns=profinet;Diagnosis",
            dataType=profinet_datypes.PnDeviceDiagnosisDataType,
            valueRank=1,
            arrayDimensions=[1],
            value=[
                profinet_datypes.PnDeviceDiagnosisDataType(
                    aPI=0,
                    slot=0,
                    subslot=0,
                    channelNumber=0,
                    type=profinet_datypes.PnChannelTypeEnumeration.UNSPECIFIC,
                    accumulative=profinet_datypes.PnChannelAccumulativeEnumeration.SINGLE,
                    maintenance=profinet_datypes.PnChannelMaintenanceEnumeration.FAULT,
                    specifier=profinet_datypes.PnChannelSpecifierEnumeration.ALL_DISAPPEARS,
                    direction=profinet_datypes.PnChannelDirectionEnumeration.MANUFACTURER_SPECIFIC,
                    userStructureIdentifier=0,
                    channelErrorType=0,
                    extChannelErrorType=0,
                    extChannelAddValue=0,
                    qualifiedChannelQualifier=0,
                    manufacturerData=b"",
                    message=o6.LocalizedText(),
                    helpText=o6.LocalizedText(),
                )
            ],
        )
    )
    iM: PnIdentificationType | None
    submodules: PnRealSubmoduleContainerType | None = o6.hasComponent(PnRealSubmoduleContainerType(nodeId="ns=profinet;i=5028", browseName="ns=profinet;Submodules"))


o6.reference(IPnRealModuleType, "i=41", PnDiagnosisAlarmType)
o6.reference(IPnRealModuleType, "i=41", PnAssetChangedEventType)


@o6.objecttype(nodeId="ns=profinet;i=1027", browseName="ns=profinet;IPnExpectedModuleType", displayName="IPnExpectedModuleType", isAbstract=True)
class IPnExpectedModuleType(IPnModuleType):
    state: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=profinet;i=6157", browseName="ns=profinet;State", dataType=profinet_datypes.PnModuleStateEnumeration)
    )
    submodules: PnExpectedSubmoduleContainerType | None = o6.hasComponent(PnExpectedSubmoduleContainerType(nodeId="ns=profinet;i=5032", browseName="ns=profinet;Submodules"))


@o6.objecttype(nodeId="ns=profinet;i=1029", browseName="ns=profinet;PnApplicationRelationType", displayName="PnApplicationRelationType")
class PnApplicationRelationType(ns0.objtypes.BaseObjectType):
    dataHoldFactor: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6163", browseName="ns=profinet;DataHoldFactor", dataType=o6.UInt16)
    )
    id: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6159", browseName="ns=profinet;Id", dataType=o6.Guid))
    modules: PnExpectedModuleContainerType | None = o6.hasComponent(PnExpectedModuleContainerType(nodeId="ns=profinet;i=5034", browseName="ns=profinet;Modules"))
    reductionRatio: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6162", browseName="ns=profinet;ReductionRatio", dataType=o6.UInt16)
    )
    sendClockFactor: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6161", browseName="ns=profinet;SendClockFactor", dataType=o6.UInt16)
    )
    state: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=profinet;i=6158", browseName="ns=profinet;State", dataType=profinet_datypes.PnARStateEnumeration, accessLevel=3, userAccessLevel=1
        )
    )
    type: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6160", browseName="ns=profinet;Type", dataType=profinet_datypes.PnARTypeEnumeration)
    )


@o6.objecttype(nodeId="ns=profinet;i=1015", browseName="ns=profinet;EthernetPortType", displayName="EthernetPortType")
class EthernetPortType(NetworkComponentType):
    langleEthernetPortRangle: EthernetPortType | None
    physAddress: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=profinet;i=6179", browseName="ns=profinet;PhysAddress", dataType=o6.Byte, valueRank=1, arrayDimensions=[6])
    )


@o6.objecttype(nodeId="ns=profinet;i=1014", browseName="ns=profinet;EthernetInterfaceType", displayName="EthernetInterfaceType")
class EthernetInterfaceType(NetworkComponentType):
    langlePortNameRangle: EthernetPortType = o6.reference(
        EthernetPortType(nodeId="ns=profinet;i=5017", browseName="ns=profinet;<PortName>", modellingRule="MandatoryPlaceholder"), "ns=profinet;i=4015"
    )
    macAddress: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=profinet;i=6110", browseName="ns=profinet;MacAddress", dataType=o6.Byte, valueRank=1, arrayDimensions=[6])
    )


@o6.objecttype(nodeId="ns=profinet;i=1010", browseName="ns=profinet;PnPortType", displayName="PnPortType")
class PnPortType(ns0.objtypes.BaseObjectType):
    cableDelay: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=profinet;i=6100", browseName="ns=profinet;CableDelay", dataType=o6.UInt32)
    )
    ethernetPort: EthernetPortType | None = o6.reference(EthernetPortType(nodeId="ns=profinet;i=5018", browseName="ns=profinet;EthernetPort"), "ns=profinet;i=4015")
    isWireless: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=profinet;i=6102", browseName="ns=profinet;IsWireless", dataType=o6.Boolean)
    )
    linkState: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=profinet;i=6096", browseName="ns=profinet;LinkState", dataType=profinet_datypes.PnLinkStateEnumeration)
    )
    mAUType: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=profinet;i=6099", browseName="ns=profinet;MAUType", dataType=o6.UInt16)
    )
    portState: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=profinet;i=6097", browseName="ns=profinet;PortState", dataType=profinet_datypes.PnPortStateEnumeration)
    )
    powerBudget: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=profinet;i=6101", browseName="ns=profinet;PowerBudget", dataType=o6.UInt32)
    )
    statistic: PnPortStatisticType | None = o6.hasComponent(PnPortStatisticType(nodeId="ns=profinet;i=5019", browseName="ns=profinet;Statistic"))


o6.reference(PnPortType, "i=41", PnTopologyChangedEventType)


@o6.objecttype(nodeId="ns=profinet;i=1011", browseName="ns=profinet;PnPortContainerType", displayName="PnPortContainerType")
class PnPortContainerType(ns0.objtypes.BaseObjectType):
    langlePortsRangle: PnPortType | None = o6.reference(
        PnPortType(nodeId="ns=profinet;i=5013", browseName="ns=profinet;<Ports>", modellingRule="OptionalPlaceholder"), "ns=profinet;i=4008"
    )


ns0.vartypes.PropertyType(
    nodeId="ns=profinet;i=6062",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=profinet;i=7001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="Tag_Selector",
            dataType=profinet_datypes.IMTagSelectorEnumeration,
            valueRank=-1,
            description=o6.LocalizedText("If 1, Tag_Function shall be written, If 2, Tag_Location shall be written, if 3 both."),
        ),
        ns0.datatypes.Argument(
            name="Tag_Function",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText("String containing the new I&amp;M1 | IM_Tag_Function to be written remanent to the device. "),
        ),
        ns0.datatypes.Argument(
            name="Tag_Location",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText("String containing the new I&amp;M1 | IM_Tag_Location to be written remanent to the device."),
        ),
    ],
)
o6.call(nodeId="ns=profinet;i=7001", browseName="ns=profinet;SetTags", inputArgs=o6.hasProperty(o6.ns["ns=profinet;i=6062"]))

ns0.vartypes.PropertyType(
    nodeId="ns=profinet;i=6063",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=profinet;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Date", dataType=o6.DateTime, valueRank=-1, description=o6.LocalizedText("New I&amp;M2 | IM_Date to be written remanent to the device. "))],
)
o6.call(nodeId="ns=profinet;i=7002", browseName="ns=profinet;SetDate", inputArgs=o6.hasProperty(o6.ns["ns=profinet;i=6063"]))

ns0.vartypes.PropertyType(
    nodeId="ns=profinet;i=6064",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=profinet;i=7003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="Descriptor", dataType=o6.String, valueRank=-1, description=o6.LocalizedText("New I&amp;M3 | IM_Descriptor to be written remanent to the device. ")
        )
    ],
)
o6.call(nodeId="ns=profinet;i=7003", browseName="ns=profinet;SetDescriptor", inputArgs=o6.hasProperty(o6.ns["ns=profinet;i=6064"]))


@o6.objecttype(nodeId="ns=profinet;i=1005", browseName="ns=profinet;PnIdentificationType", displayName="PnIdentificationType")
class PnIdentificationType(ns0.objtypes.BaseObjectType):
    date: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6058", browseName="ns=profinet;Date", dataType=o6.DateTime))
    descriptor: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6059", browseName="ns=profinet;Descriptor", dataType=o6.String))
    hardwareRevision: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6050", browseName="ns=profinet;HardwareRevision", dataType=o6.String)
    )
    iM5: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6061", browseName="ns=profinet;IM5", dataType=profinet_datypes.PnIM5DataType, valueRank=1, arrayDimensions=[0])
    )
    iMSupported: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6055", browseName="ns=profinet;IMSupported", dataType=o6.UInt16))
    orderId: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6047", browseName="ns=profinet;OrderId", dataType=o6.String))
    profileId: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6051", browseName="ns=profinet;ProfileId", dataType=o6.UInt32))
    profileSpecificType: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6052", browseName="ns=profinet;ProfileSpecificType", dataType=o6.UInt16)
    )
    revisionCounter: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6054", browseName="ns=profinet;RevisionCounter", dataType=o6.UInt16)
    )
    serialNumber: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6048", browseName="ns=profinet;SerialNumber", dataType=o6.String))
    setDate: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=profinet;i=7002"])
    setDescriptor: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=profinet;i=7003"])
    setTags: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=profinet;i=7001"])
    signature: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6060", browseName="ns=profinet;Signature", dataType=o6.ByteString))
    softwareRevision: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6049", browseName="ns=profinet;SoftwareRevision", dataType=o6.String)
    )
    tagFunction: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6056", browseName="ns=profinet;TagFunction", dataType=o6.String))
    tagLocation: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6057", browseName="ns=profinet;TagLocation", dataType=o6.String))
    vendorId: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6046", browseName="ns=profinet;VendorId", dataType=o6.UInt16))
    version: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6053", browseName="ns=profinet;Version", dataType=o6.String))


ns0.vartypes.PropertyType(
    nodeId="ns=profinet;i=6095",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=profinet;i=7004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="NameOfStation",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "String containing the new NameOfStation to be written remanent to the device. The maximum length shall be limited to 240 characters (See [PN Protocol] for details).\n"
            ),
        )
    ],
)
o6.call(nodeId="ns=profinet;i=7004", browseName="ns=profinet;SetNameOfStation", inputArgs=o6.hasProperty(o6.ns["ns=profinet;i=6095"]))


@o6.objecttype(nodeId="ns=profinet;i=1008", browseName="ns=profinet;IPnInterfaceType", displayName="IPnInterfaceType", isAbstract=True)
class IPnInterfaceType(ns0.objtypes.BaseInterfaceType):
    deviceId: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6091", browseName="ns=profinet;DeviceId", dataType=o6.UInt16))
    deviceInstance: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6092", browseName="ns=profinet;DeviceInstance", dataType=o6.UInt16)
    )
    deviceRole: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6088", browseName="ns=profinet;DeviceRole", dataType=profinet_datypes.PnDeviceRoleOptionSet)
    )
    deviceVendor: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6089", browseName="ns=profinet;DeviceVendor", dataType=o6.String)
    )
    ethernetInterface: EthernetInterfaceType | None
    nameOfStation: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6087", browseName="ns=profinet;NameOfStation", dataType=o6.String))
    oEMDeviceId: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6094", browseName="ns=profinet;OEMDeviceId", dataType=o6.UInt16))
    oEMVendorId: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6093", browseName="ns=profinet;OEMVendorId", dataType=o6.UInt16))
    ports: PnPortContainerType = o6.hasComponent(PnPortContainerType(nodeId="ns=profinet;i=5020", browseName="ns=profinet;Ports"))
    setNameOfStation: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=profinet;i=7004"])
    statistic: PnPortStatisticType | None = o6.hasComponent(PnPortStatisticType(nodeId="ns=profinet;i=5021", browseName="ns=profinet;Statistic"))
    vendorId: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6090", browseName="ns=profinet;VendorId", dataType=o6.UInt16))


@o6.objecttype(nodeId="ns=profinet;i=1032", browseName="ns=profinet;IPnEquipmentType", displayName="IPnEquipmentType", isAbstract=True)
class IPnEquipmentType(ns0.objtypes.BaseInterfaceType):
    alarms: ns0.objtypes.FolderType | None = o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=profinet;i=5041", browseName="ns=profinet;Alarms"))
    assets: PnAssetContainerType | None = o6.hasComponent(PnAssetContainerType(nodeId="ns=profinet;i=5039", browseName="ns=profinet;Assets"))
    diagnosis: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=profinet;i=6176",
            browseName="ns=profinet;Diagnosis",
            dataType=profinet_datypes.PnDeviceDiagnosisDataType,
            valueRank=1,
            arrayDimensions=[1],
            value=[
                profinet_datypes.PnDeviceDiagnosisDataType(
                    aPI=0,
                    slot=0,
                    subslot=0,
                    channelNumber=0,
                    type=profinet_datypes.PnChannelTypeEnumeration.UNSPECIFIC,
                    accumulative=profinet_datypes.PnChannelAccumulativeEnumeration.SINGLE,
                    maintenance=profinet_datypes.PnChannelMaintenanceEnumeration.FAULT,
                    specifier=profinet_datypes.PnChannelSpecifierEnumeration.ALL_DISAPPEARS,
                    direction=profinet_datypes.PnChannelDirectionEnumeration.MANUFACTURER_SPECIFIC,
                    userStructureIdentifier=0,
                    channelErrorType=0,
                    extChannelErrorType=0,
                    extChannelAddValue=0,
                    qualifiedChannelQualifier=0,
                    manufacturerData=b"",
                    message=o6.LocalizedText(),
                    helpText=o6.LocalizedText(),
                )
            ],
        )
    )
    iM: PnIdentificationType | None
    interfaces: PnInterfaceContainerType = o6.hasComponent(PnInterfaceContainerType(nodeId="ns=profinet;i=5037", browseName="ns=profinet;Interfaces"))
    modules: PnRealModuleContainerType | None = o6.hasComponent(PnRealModuleContainerType(nodeId="ns=profinet;i=5038", browseName="ns=profinet;Modules"))
    showLocation: o6.node.MethodNode | None = o6.hasComponent(o6.call(nodeId="ns=profinet;i=7005", browseName="ns=profinet;ShowLocation"))
    vendor: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6175", browseName="ns=profinet;Vendor", dataType=o6.String))


o6.reference(IPnEquipmentType, "i=41", PnDiagnosisAlarmType)
o6.reference(IPnEquipmentType, "i=41", PnAssetChangedEventType)


@o6.objecttype(nodeId="ns=profinet;i=1034", browseName="ns=profinet;IPnDeviceType", displayName="IPnDeviceType", isAbstract=True)
class IPnDeviceType(IPnEquipmentType):
    gSDDescription: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=profinet;i=6177", browseName="ns=profinet;GSDDescription", dataType=o6.String)
    )
    state: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=profinet;i=6178", browseName="ns=profinet;State", dataType=profinet_datypes.PnDeviceStateEnumeration)
    )


@o6.objecttype(nodeId="ns=profinet;i=1035", browseName="ns=profinet;IPnControllerType", displayName="IPnControllerType", isAbstract=True)
class IPnControllerType(IPnEquipmentType):
    aRs: PnApplicationRelationContainerType | None = o6.hasComponent(PnApplicationRelationContainerType(nodeId="ns=profinet;i=5043", browseName="ns=profinet;ARs"))


del Any, TYPE_CHECKING, uuid, o6, ns0, profinet_reftypes, profinet_datypes
