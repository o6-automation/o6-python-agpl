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

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.datatype(nodeId="ns=profinet;i=3002", browseName="PnDeviceRoleOptionSet", defaultEncodingId="ns=profinet;i=5001")
class PnDeviceRoleOptionSet(ns0.datatypes.OptionSet):
    value: o6.ByteString
    validBits: o6.ByteString
    iO_DEVICE = o6.optionsetbit(0, name="IO_DEVICE")
    iO_CONTROLLER = o6.optionsetbit(1, name="IO_CONTROLLER")
    iO_MULTIDEVICE = o6.optionsetbit(2, name="IO_MULTIDEVICE")
    iO_SUPERVISOR = o6.optionsetbit(3, name="IO_SUPERVISOR")
    iO_CIM = o6.optionsetbit(4, name="IO_CIM")


@o6.enumtype(nodeId="ns=profinet;i=3003", browseName="PnDeviceStateEnumeration")
class PnDeviceStateEnumeration(ns0.datatypes.Enumeration):
    OFFLINE = o6.enumfield(0, name="OFFLINE")
    OFFLINE_DOCKING = o6.enumfield(1, name="OFFLINE_DOCKING")
    ONLINE = o6.enumfield(2, name="ONLINE")
    ONLINE_DOCKING = o6.enumfield(3, name="ONLINE_DOCKING")


@o6.enumtype(nodeId="ns=profinet;i=3004", browseName="PnARStateEnumeration")
class PnARStateEnumeration(ns0.datatypes.Enumeration):
    CONNECTED = o6.enumfield(0, name="CONNECTED")
    UNCONNECTED = o6.enumfield(1, name="UNCONNECTED")
    UNCONNECTED_ERR_DEVICE_NOT_FOUND = o6.enumfield(2, name="UNCONNECTED_ERR_DEVICE_NOT_FOUND")
    UNCONNECTED_ERR_DUPLICATE_IP = o6.enumfield(3, name="UNCONNECTED_ERR_DUPLICATE_IP")
    UNCONNECTED_ERR_DUPLICATE_NOS = o6.enumfield(4, name="UNCONNECTED_ERR_DUPLICATE_NOS")


@o6.enumtype(nodeId="ns=profinet;i=3005", browseName="PnARTypeEnumeration")
class PnARTypeEnumeration(ns0.datatypes.Enumeration):
    IOCAR_SINGLE = o6.enumfield(0, name="IOCARSingle")
    IOSAR = o6.enumfield(6, name="IOSAR")
    IOCAR_SINGLE_USING_RT_CLASS_3 = o6.enumfield(16, name="IOCARSingleUsingRT_CLASS_3")
    IOCARSR = o6.enumfield(32, name="IOCARSR")


@o6.enumtype(nodeId="ns=profinet;i=3006", browseName="PnModuleStateEnumeration")
class PnModuleStateEnumeration(ns0.datatypes.Enumeration):
    NO_MODULE = o6.enumfield(0, name="NO_MODULE")
    WRONG_MODULE = o6.enumfield(1, name="WRONG_MODULE")
    PROPER_MODULE = o6.enumfield(2, name="PROPER_MODULE")
    SUBSTITUTE = o6.enumfield(3, name="SUBSTITUTE")
    OK = o6.enumfield(4, name="OK")


@o6.enumtype(nodeId="ns=profinet;i=3007", browseName="PnSubmoduleAddInfoEnumeration")
class PnSubmoduleAddInfoEnumeration(ns0.datatypes.Enumeration):
    NO_ADD_INFO = o6.enumfield(0, name="NO_ADD_INFO")
    TAKEOVER_NOT_ALLOWED = o6.enumfield(1, name="TAKEOVER_NOT_ALLOWED")


@o6.enumtype(nodeId="ns=profinet;i=3008", browseName="PnSubmoduleARInfoEnumeration")
class PnSubmoduleARInfoEnumeration(ns0.datatypes.Enumeration):
    OWN = o6.enumfield(0, name="OWN")
    APPLICATION_READY_PENDING = o6.enumfield(128, name="APPLICATION_READY_PENDING")
    SUPERORDINATED_LOCKED = o6.enumfield(256, name="SUPERORDINATED_LOCKED")
    LOCKED_BY_IO_CONTROLLER = o6.enumfield(384, name="LOCKED_BY_IO_CONTROLLER")
    LOCKED_BY_IO_SUPERVISOR = o6.enumfield(512, name="LOCKED_BY_IO_SUPERVISOR")


@o6.enumtype(nodeId="ns=profinet;i=3009", browseName="PnSubmoduleIdentInfoEnumeration")
class PnSubmoduleIdentInfoEnumeration(ns0.datatypes.Enumeration):
    OK = o6.enumfield(0, name="OK")
    SUBSTITUTE = o6.enumfield(2048, name="SUBSTITUTE")
    WRONG = o6.enumfield(4096, name="WRONG")
    NO_SUBMODULE = o6.enumfield(6144, name="NO_SUBMODULE")


@o6.enumtype(nodeId="ns=profinet;i=3010", browseName="PnChannelTypeEnumeration")
class PnChannelTypeEnumeration(ns0.datatypes.Enumeration):
    UNSPECIFIC = o6.enumfield(0, name="UNSPECIFIC")
    _1_BIT = o6.enumfield(1, name="1BIT")
    _2_BIT = o6.enumfield(2, name="2BIT")
    _4_BIT = o6.enumfield(3, name="4BIT")
    _8_BIT = o6.enumfield(4, name="8BIT")
    _16_BIT = o6.enumfield(5, name="16BIT")
    _32_BIT = o6.enumfield(6, name="32BIT")
    _64_BIT = o6.enumfield(7, name="64BIT")


@o6.enumtype(nodeId="ns=profinet;i=3011", browseName="PnChannelAccumulativeEnumeration")
class PnChannelAccumulativeEnumeration(ns0.datatypes.Enumeration):
    SINGLE = o6.enumfield(0, name="SINGLE")
    ACCUMULATIVE = o6.enumfield(256, name="ACCUMULATIVE")


@o6.enumtype(nodeId="ns=profinet;i=3012", browseName="PnChannelMaintenanceEnumeration")
class PnChannelMaintenanceEnumeration(ns0.datatypes.Enumeration):
    FAULT = o6.enumfield(0, name="FAULT")
    MAINTENANCE_REQUIRED = o6.enumfield(512, name="MAINTENANCE_REQUIRED")
    MAINTENANCE_DEMANDED = o6.enumfield(1024, name="MAINTENANCE_DEMANDED")
    USE_QUALIFIED_CHANNEL_QUALIFIER = o6.enumfield(1536, name="USE_QUALIFIED_CHANNEL_QUALIFIER")


@o6.enumtype(nodeId="ns=profinet;i=3013", browseName="PnChannelSpecifierEnumeration")
class PnChannelSpecifierEnumeration(ns0.datatypes.Enumeration):
    ALL_DISAPPEARS = o6.enumfield(0, name="ALL_DISAPPEARS")
    APPEARS = o6.enumfield(2048, name="APPEARS")
    DISAPPEARS = o6.enumfield(4096, name="DISAPPEARS")
    DISAPPEARS_OTHER_REMAIN = o6.enumfield(6144, name="DISAPPEARS_OTHER_REMAIN")


@o6.enumtype(nodeId="ns=profinet;i=3014", browseName="PnChannelDirectionEnumeration")
class PnChannelDirectionEnumeration(ns0.datatypes.Enumeration):
    MANUFACTURER_SPECIFIC = o6.enumfield(0, name="MANUFACTURER_SPECIFIC")
    INPUT_CHANNEL = o6.enumfield(8192, name="INPUT_CHANNEL")
    OUTPUT_CHANNEL = o6.enumfield(16384, name="OUTPUT_CHANNEL")
    BIDIRECTIONAL_CHANNEL = o6.enumfield(24576, name="BIDIRECTIONAL_CHANNEL")


@o6.enumtype(nodeId="ns=profinet;i=3015", browseName="PnAssetTypeEnumeration")
class PnAssetTypeEnumeration(ns0.datatypes.Enumeration):
    DEVICE = o6.enumfield(0, name="DEVICE")
    MODULE = o6.enumfield(1, name="MODULE")
    SUBMODULE = o6.enumfield(2, name="SUBMODULE")
    ASSET = o6.enumfield(3, name="ASSET")


@o6.enumtype(nodeId="ns=profinet;i=3016", browseName="PnAssetChangeEnumeration")
class PnAssetChangeEnumeration(ns0.datatypes.Enumeration):
    INSERTED = o6.enumfield(0, name="INSERTED")
    REMOVED = o6.enumfield(1, name="REMOVED")
    CHANGED = o6.enumfield(2, name="CHANGED")


@o6.enumtype(nodeId="ns=profinet;i=3017", browseName="PnLinkStateEnumeration")
class PnLinkStateEnumeration(ns0.datatypes.Enumeration):
    UP = o6.enumfield(1, name="UP")
    DOWN = o6.enumfield(2, name="DOWN")
    TESTING = o6.enumfield(3, name="TESTING")
    UNKNOWN = o6.enumfield(4, name="UNKNOWN")
    DORMANT = o6.enumfield(5, name="DORMANT")
    NOT_PRESENT = o6.enumfield(6, name="NOT_PRESENT")
    LOWER_LAYER_DOWN = o6.enumfield(7, name="LOWER_LAYER_DOWN")


@o6.enumtype(nodeId="ns=profinet;i=3018", browseName="PnPortStateEnumeration")
class PnPortStateEnumeration(ns0.datatypes.Enumeration):
    UNKNOWN = o6.enumfield(0, name="UNKNOWN")
    DISABLED_DISCARDING = o6.enumfield(1, name="DISABLED_DISCARDING")
    BLOCKING = o6.enumfield(2, name="BLOCKING")
    LISTENING = o6.enumfield(3, name="LISTENING")
    LEARNING = o6.enumfield(4, name="LEARNING")
    FORWARDING = o6.enumfield(5, name="FORWARDING")
    BROKEN = o6.enumfield(6, name="BROKEN")


@o6.datatype(nodeId="ns=profinet;i=3019", browseName="PnDeviceDiagnosisDataType", defaultEncodingId="ns=profinet;i=5004")
class PnDeviceDiagnosisDataType(ns0.datatypes.Structure):
    aPI: o6.UInt32
    slot: o6.UInt16
    subslot: o6.UInt16
    channelNumber: o6.UInt16
    type: PnChannelTypeEnumeration
    accumulative: PnChannelAccumulativeEnumeration
    maintenance: PnChannelMaintenanceEnumeration
    specifier: PnChannelSpecifierEnumeration
    direction: PnChannelDirectionEnumeration
    userStructureIdentifier: o6.UInt16
    channelErrorType: o6.UInt16
    extChannelErrorType: o6.UInt16
    extChannelAddValue: o6.UInt32
    qualifiedChannelQualifier: o6.UInt32
    manufacturerData: o6.ByteString
    message: o6.LocalizedText
    helpText: o6.LocalizedText


@o6.datatype(nodeId="ns=profinet;i=3020", browseName="PnIM5DataType", description="Contains the fields of the APDU element I&M5 | I&M5Data", defaultEncodingId="ns=profinet;i=5007")
class PnIM5DataType(ns0.datatypes.Structure):
    annotation: o6.String
    orderId: o6.String
    vendorId: o6.UInt16
    serialNumber: o6.String
    hardwareRevision: o6.String
    softwareRevision: o6.String


@o6.enumtype(nodeId="ns=profinet;i=3021", browseName="IMTagSelectorEnumeration")
class IMTagSelectorEnumeration(ns0.datatypes.Enumeration):
    FUNCTION = o6.enumfield(0, name="FUNCTION")
    LOCATION = o6.enumfield(1, name="LOCATION")
    BOTH = o6.enumfield(2, name="BOTH")


del Any, TYPE_CHECKING, uuid, o6, ns0, profinet_reftypes
