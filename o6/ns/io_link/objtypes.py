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

"""Generated OPC UA io_link namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
from . import reftypes as io_link_reftypes
from . import datatypes as io_link_datypes
from . import vartypes as io_link_vartypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

di.objtypes.FunctionalGroupType(nodeId="ns=io_link;i=5004", browseName="ns=io_link;General")
di.objtypes.FunctionalGroupType(nodeId="ns=io_link;i=5018", browseName="ns=io_link;Capabilities")
di.objtypes.FunctionalGroupType(nodeId="ns=io_link;i=5019", browseName="ns=io_link;Management")
di.objtypes.FunctionalGroupType(nodeId="ns=io_link;i=5020", browseName="ns=io_link;Statistics")
di.objtypes.FunctionalGroupType(nodeId="ns=io_link;i=5028", browseName="ns=io_link;Capabilities")
di.objtypes.FunctionalGroupType(nodeId="ns=io_link;i=5029", browseName="ns=io_link;Information")
di.objtypes.FunctionalGroupType(nodeId="ns=io_link;i=5030", browseName="ns=io_link;Statistics")
di.objtypes.FunctionalGroupType(nodeId="ns=io_link;i=5032", browseName="ns=io_link;SIOProcessData")
ns0.vartypes.PropertyType(nodeId="ns=io_link;i=6004", browseName="ns=io_link;VendorID", dataType=o6.UInt16)
ns0.vartypes.PropertyType(nodeId="ns=io_link;i=6005", browseName="ns=io_link;DeviceID", dataType=o6.UInt32)


@o6.objecttype(nodeId="ns=io_link;i=1003", browseName="ns=io_link;IOLinkEventType", displayName="IOLinkEventType", isAbstract=True)
class IOLinkEventType(ns0.objtypes.BaseEventType):
    iOLinkEventCode: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=io_link;i=6018", browseName="ns=io_link;IOLinkEventCode", dataType=o6.UInt16))


@o6.objecttype(nodeId="ns=io_link;i=1004", browseName="ns=io_link;IOLinkDeviceEventType", displayName="IOLinkDeviceEventType")
class IOLinkDeviceEventType(IOLinkEventType):
    pass


@o6.objecttype(nodeId="ns=io_link;i=1006", browseName="ns=io_link;IOLinkMasterEventType", displayName="IOLinkMasterEventType", isAbstract=True)
class IOLinkMasterEventType(IOLinkEventType):
    pass


@o6.objecttype(nodeId="ns=io_link;i=1007", browseName="ns=io_link;IOLinkAlarmType", displayName="IOLinkAlarmType", isAbstract=True)
class IOLinkAlarmType(ns0.objtypes.OffNormalAlarmType):
    iOLinkEventCode: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=io_link;i=6019", browseName="ns=io_link;IOLinkEventCode", dataType=o6.UInt16))


@o6.objecttype(nodeId="ns=io_link;i=1008", browseName="ns=io_link;IOLinkDeviceAlarmType", displayName="IOLinkDeviceAlarmType")
class IOLinkDeviceAlarmType(IOLinkAlarmType):
    pass


@o6.objecttype(nodeId="ns=io_link;i=1010", browseName="ns=io_link;IOLinkPortAlarmType", displayName="IOLinkPortAlarmType")
class IOLinkPortAlarmType(IOLinkAlarmType):
    pass


@o6.objecttype(nodeId="ns=io_link;i=1011", browseName="ns=io_link;IOLinkMasterAlarmType", displayName="IOLinkMasterAlarmType")
class IOLinkMasterAlarmType(IOLinkAlarmType):
    pass


@o6.objecttype(nodeId="ns=io_link;i=1009", browseName="ns=io_link;IOLinkIODDDeviceAlarmType", displayName="IOLinkIODDDeviceAlarmType")
class IOLinkIODDDeviceAlarmType(IOLinkDeviceAlarmType):
    name: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=io_link;i=6020", browseName="ns=io_link;Name", dataType=o6.LocalizedText))


ns0.vartypes.PropertyType(
    nodeId="ns=io_link;i=6029", browseName="ns=di;SerialNumber", description="Identifier that uniquely identifies, within a manufacturer, a device instance", dataType=o6.String
)


@o6.objecttype(nodeId="ns=io_link;i=1013", browseName="ns=io_link;DeviceVariantType", displayName="DeviceVariantType")
class DeviceVariantType(ns0.objtypes.BaseObjectType):
    description: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=io_link;i=6068", browseName="ns=io_link;Description", dataType=o6.LocalizedText))
    deviceIcon: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=io_link;i=6070", browseName="ns=io_link;DeviceIcon", dataType=ns0.datatypes.Image, value=b"")
    )
    deviceSymbol: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=io_link;i=6069", browseName="ns=io_link;DeviceSymbol", dataType=ns0.datatypes.Image, value=b"")
    )
    name: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=io_link;i=6067", browseName="ns=io_link;Name", dataType=o6.LocalizedText))
    productId: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=io_link;i=6066", browseName="ns=io_link;ProductId", dataType=o6.String))


ns0.vartypes.PropertyType(nodeId="ns=io_link;i=6078", browseName="ns=io_link;DeviceID", dataType=o6.UInt32)
ns0.vartypes.PropertyType(nodeId="ns=io_link;i=6082", browseName="ns=io_link;VendorID", dataType=o6.UInt16)


@o6.objecttype(nodeId="ns=io_link;i=1002", browseName="ns=io_link;IOLinkDeviceType", displayName="IOLinkDeviceType")
class IOLinkDeviceType(di.objtypes.TopologyElementType):
    alarms: ns0.objtypes.FolderType | None = o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=io_link;i=5006", browseName="ns=io_link;Alarms"))
    deviceAccessLocks: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=io_link;i=6006", browseName="ns=io_link;DeviceAccessLocks", dataType=o6.UInt16, accessLevel=3, userAccessLevel=1)
    )
    deviceHealth: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=io_link;i=6142", browseName="ns=di;DeviceHealth", dataType=di.datatypes.DeviceHealthEnumeration)
    )
    deviceID: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=io_link;i=6005"])
    general: di.objtypes.FunctionalGroupType = o6.hasComponent(o6.ns["ns=io_link;i=5004"])
    hardwareRevision: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=io_link;i=6140", browseName="ns=di;HardwareRevision", dataType=o6.String)
    )
    identification: di.objtypes.FunctionalGroupType
    manufacturer: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=io_link;i=6129", browseName="ns=di;Manufacturer", dataType=o6.LocalizedText))
    methodSet: ns0.objtypes.BaseObjectType
    minCycleTime: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=io_link;i=6002", browseName="ns=io_link;MinCycleTime", dataType=ns0.datatypes.Duration)
    )
    model: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=io_link;i=6139", browseName="ns=di;Model", dataType=o6.LocalizedText))
    parameterSet: ns0.objtypes.BaseObjectType
    productID: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=io_link;i=6009", browseName="ns=io_link;ProductID", dataType=o6.String))
    productText: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=io_link;i=6010", browseName="ns=io_link;ProductText", dataType=o6.String))
    profileCharacteristic: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=io_link;i=6007", browseName="ns=io_link;ProfileCharacteristic", dataType=o6.UInt16, valueRank=1)
    )
    revisionID: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=io_link;i=6003", browseName="ns=io_link;RevisionID", dataType=o6.String))
    serialNumber: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=io_link;i=6029"])
    softwareRevision: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=io_link;i=6141", browseName="ns=di;SoftwareRevision", dataType=o6.String)
    )
    vendorID: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=io_link;i=6004"])
    vendorText: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=io_link;i=6008", browseName="ns=io_link;VendorText", dataType=o6.String))


o6.reference(IOLinkDeviceType, "i=41", IOLinkDeviceEventType)
o6.reference(IOLinkDeviceType, "i=41", IOLinkDeviceAlarmType)


@o6.objecttype(nodeId="ns=io_link;i=1012", browseName="ns=io_link;IOLinkIODDDeviceType", displayName="IOLinkIODDDeviceType", isAbstract=True)
class IOLinkIODDDeviceType(IOLinkDeviceType):
    deviceName: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=io_link;i=6057", browseName="ns=io_link;DeviceName", dataType=o6.LocalizedText))
    deviceTypeImage: ns0.objtypes.FolderType | None
    deviceVariant: DeviceVariantType
    deviceVariants: ns0.objtypes.FolderType = o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=io_link;i=5012", browseName="ns=io_link;DeviceVariants"))
    iODDInformation: ns0.objtypes.FolderType
    maintenance: di.objtypes.FunctionalGroupType = o6.organizes(di.objtypes.FunctionalGroupType(nodeId="ns=io_link;i=5009", browseName="ns=io_link;Maintenance"))
    observer: di.objtypes.FunctionalGroupType = o6.organizes(di.objtypes.FunctionalGroupType(nodeId="ns=io_link;i=5010", browseName="ns=io_link;Observer"))
    parameterSet: ns0.objtypes.BaseObjectType
    specialist: di.objtypes.FunctionalGroupType = o6.organizes(di.objtypes.FunctionalGroupType(nodeId="ns=io_link;i=5008", browseName="ns=io_link;Specialist"))
    vendorLogo: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=io_link;i=6058", browseName="ns=io_link;VendorLogo", dataType=ns0.datatypes.Image, value=b"")
    )
    vendorURL: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=io_link;i=6056", browseName="ns=io_link;VendorURL", dataType=o6.String))


@o6.objecttype(nodeId="ns=io_link;i=1015", browseName="ns=io_link;IOLinkPortType", displayName="IOLinkPortType")
class IOLinkPortType(di.objtypes.TopologyElementType):
    alarms: ns0.objtypes.FolderType | None = o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=io_link;i=5038", browseName="ns=io_link;Alarms"))
    capabilities: di.objtypes.FunctionalGroupType = o6.hasComponent(o6.ns["ns=io_link;i=5028"])
    configuration: di.objtypes.FunctionalGroupType
    device: IOLinkDeviceType | None = o6.hasComponent(IOLinkDeviceType(nodeId="ns=io_link;i=5033", browseName="ns=io_link;Device"))
    deviceConfigurationDisabled: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=io_link;i=6113", browseName="ns=io_link;DeviceConfigurationDisabled", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
    )
    information: di.objtypes.FunctionalGroupType = o6.hasComponent(o6.ns["ns=io_link;i=5029"])
    methodSet: ns0.objtypes.BaseObjectType
    parameterSet: ns0.objtypes.BaseObjectType
    sIOProcessData: di.objtypes.FunctionalGroupType = o6.hasComponent(o6.ns["ns=io_link;i=5032"])
    statistics: di.objtypes.FunctionalGroupType = o6.hasComponent(o6.ns["ns=io_link;i=5030"])


o6.reference(IOLinkPortType, "i=41", IOLinkPortAlarmType)


@o6.objecttype(nodeId="ns=io_link;i=1014", browseName="ns=io_link;IOLinkMasterType", displayName="IOLinkMasterType")
class IOLinkMasterType(di.objtypes.TopologyElementType):
    alarms: ns0.objtypes.FolderType | None = o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=io_link;i=5025", browseName="ns=io_link;Alarms"))
    capabilities: di.objtypes.FunctionalGroupType = o6.hasComponent(o6.ns["ns=io_link;i=5018"])
    deviceID: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=io_link;i=6078"])
    iOLinkStackRevision: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=io_link;i=6084", browseName="ns=io_link;IOLinkStackRevision", dataType=o6.String)
    )
    identification: di.objtypes.FunctionalGroupType
    management: di.objtypes.FunctionalGroupType = o6.hasComponent(o6.ns["ns=io_link;i=5019"])
    masterConfigurationDisabled: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=io_link;i=6085", browseName="ns=io_link;MasterConfigurationDisabled", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
    )
    methodSet: ns0.objtypes.BaseObjectType
    parameterSet: ns0.objtypes.BaseObjectType
    portLangleNRangle: IOLinkPortType = o6.hasComponent(IOLinkPortType(nodeId="ns=io_link;i=5023", browseName="ns=io_link;Port<n>", modellingRule="MandatoryPlaceholder"))
    productID: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=io_link;i=6079", browseName="ns=io_link;ProductID", dataType=o6.String))
    productText: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=io_link;i=6080", browseName="ns=io_link;ProductText", dataType=o6.String))
    revisionID: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=io_link;i=6081", browseName="ns=io_link;RevisionID", dataType=o6.String))
    statistics: di.objtypes.FunctionalGroupType = o6.hasComponent(o6.ns["ns=io_link;i=5020"])
    vendorID: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=io_link;i=6082"])
    vendorURL: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=io_link;i=6083", browseName="ns=io_link;VendorURL", dataType=o6.String))


o6.reference(IOLinkMasterType, "i=41", IOLinkMasterEventType)
o6.reference(IOLinkMasterType, "i=41", IOLinkMasterAlarmType)


@o6.objecttype(nodeId="ns=io_link;i=1021", browseName="ns=io_link;IOLinkIODDDeviceEventType", displayName="IOLinkIODDDeviceEventType")
class IOLinkIODDDeviceEventType(IOLinkDeviceEventType):
    name: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=io_link;i=6205", browseName="ns=io_link;Name", dataType=o6.LocalizedText))


@o6.objecttype(nodeId="ns=io_link;i=1005", browseName="ns=io_link;IOLinkPortEventType", displayName="IOLinkPortEventType", isAbstract=True)
class IOLinkPortEventType(IOLinkEventType):
    iOLinkEventCode: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=io_link;i=6338", browseName="ns=io_link;IOLinkEventCode", dataType=o6.UInt16))


o6.reference(IOLinkPortType, "i=41", IOLinkPortEventType)


del Any, TYPE_CHECKING, uuid, o6, di, ns0, io_link_reftypes, io_link_datypes, io_link_vartypes
