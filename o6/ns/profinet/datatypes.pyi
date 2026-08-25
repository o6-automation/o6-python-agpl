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

from typing import Any, Sequence, SupportsFloat

import numpy as np

_Integer = int | np.integer[Any]

_Boolean = bool | np.bool_

import enum

from o6.node import ObjectNode as _ObjectNode, VariableNode as _VariableNode

import uuid

import o6

import o6.ns.ns0 as ns0

class PnDeviceRoleOptionSet(ns0.datatypes.OptionSet):
    @property
    def value(self) -> o6.ByteString: ...
    @value.setter
    def value(self, value: o6.ByteString) -> None: ...
    @property
    def validBits(self) -> o6.ByteString: ...
    @validBits.setter
    def validBits(self, value: o6.ByteString) -> None: ...

class PnDeviceStateEnumeration(enum.IntFlag):
    OFFLINE = 0
    OFFLINE_DOCKING = 1
    ONLINE = 2
    ONLINE_DOCKING = 3

class PnARStateEnumeration(enum.IntFlag):
    CONNECTED = 0
    UNCONNECTED = 1
    UNCONNECTED_ERR_DEVICE_NOT_FOUND = 2
    UNCONNECTED_ERR_DUPLICATE_IP = 3
    UNCONNECTED_ERR_DUPLICATE_NOS = 4

class PnARTypeEnumeration(enum.IntFlag):
    IOCAR_SINGLE = 0
    IOSAR = 6
    IOCAR_SINGLE_USING_RT_CLASS_3 = 16
    IOCARSR = 32

class PnModuleStateEnumeration(enum.IntFlag):
    NO_MODULE = 0
    WRONG_MODULE = 1
    PROPER_MODULE = 2
    SUBSTITUTE = 3
    OK = 4

class PnSubmoduleAddInfoEnumeration(enum.IntFlag):
    NO_ADD_INFO = 0
    TAKEOVER_NOT_ALLOWED = 1

class PnSubmoduleARInfoEnumeration(enum.IntFlag):
    OWN = 0
    APPLICATION_READY_PENDING = 128
    SUPERORDINATED_LOCKED = 256
    LOCKED_BY_IO_CONTROLLER = 384
    LOCKED_BY_IO_SUPERVISOR = 512

class PnSubmoduleIdentInfoEnumeration(enum.IntFlag):
    OK = 0
    SUBSTITUTE = 2048
    WRONG = 4096
    NO_SUBMODULE = 6144

class PnChannelTypeEnumeration(enum.IntFlag):
    UNSPECIFIC = 0

class PnChannelAccumulativeEnumeration(enum.IntFlag):
    SINGLE = 0
    ACCUMULATIVE = 256

class PnChannelMaintenanceEnumeration(enum.IntFlag):
    FAULT = 0
    MAINTENANCE_REQUIRED = 512
    MAINTENANCE_DEMANDED = 1024
    USE_QUALIFIED_CHANNEL_QUALIFIER = 1536

class PnChannelSpecifierEnumeration(enum.IntFlag):
    ALL_DISAPPEARS = 0
    APPEARS = 2048
    DISAPPEARS = 4096
    DISAPPEARS_OTHER_REMAIN = 6144

class PnChannelDirectionEnumeration(enum.IntFlag):
    MANUFACTURER_SPECIFIC = 0
    INPUT_CHANNEL = 8192
    OUTPUT_CHANNEL = 16384
    BIDIRECTIONAL_CHANNEL = 24576

class PnAssetTypeEnumeration(enum.IntFlag):
    DEVICE = 0
    MODULE = 1
    SUBMODULE = 2
    ASSET = 3

class PnAssetChangeEnumeration(enum.IntFlag):
    INSERTED = 0
    REMOVED = 1
    CHANGED = 2

class PnLinkStateEnumeration(enum.IntFlag):
    UP = 1
    DOWN = 2
    TESTING = 3
    UNKNOWN = 4
    DORMANT = 5
    NOT_PRESENT = 6
    LOWER_LAYER_DOWN = 7

class PnPortStateEnumeration(enum.IntFlag):
    UNKNOWN = 0
    DISABLED_DISCARDING = 1
    BLOCKING = 2
    LISTENING = 3
    LEARNING = 4
    FORWARDING = 5
    BROKEN = 6

class PnDeviceDiagnosisDataType(ns0.datatypes.Structure):
    @property
    def aPI(self) -> o6.UInt32: ...
    @aPI.setter
    def aPI(self, value: _Integer) -> None: ...
    @property
    def slot(self) -> o6.UInt16: ...
    @slot.setter
    def slot(self, value: _Integer) -> None: ...
    @property
    def subslot(self) -> o6.UInt16: ...
    @subslot.setter
    def subslot(self, value: _Integer) -> None: ...
    @property
    def channelNumber(self) -> o6.UInt16: ...
    @channelNumber.setter
    def channelNumber(self, value: _Integer) -> None: ...
    @property
    def type(self) -> PnChannelTypeEnumeration: ...
    @type.setter
    def type(self, value: _Integer) -> None: ...
    @property
    def accumulative(self) -> PnChannelAccumulativeEnumeration: ...
    @accumulative.setter
    def accumulative(self, value: _Integer) -> None: ...
    @property
    def maintenance(self) -> PnChannelMaintenanceEnumeration: ...
    @maintenance.setter
    def maintenance(self, value: _Integer) -> None: ...
    @property
    def specifier(self) -> PnChannelSpecifierEnumeration: ...
    @specifier.setter
    def specifier(self, value: _Integer) -> None: ...
    @property
    def direction(self) -> PnChannelDirectionEnumeration: ...
    @direction.setter
    def direction(self, value: _Integer) -> None: ...
    @property
    def userStructureIdentifier(self) -> o6.UInt16: ...
    @userStructureIdentifier.setter
    def userStructureIdentifier(self, value: _Integer) -> None: ...
    @property
    def channelErrorType(self) -> o6.UInt16: ...
    @channelErrorType.setter
    def channelErrorType(self, value: _Integer) -> None: ...
    @property
    def extChannelErrorType(self) -> o6.UInt16: ...
    @extChannelErrorType.setter
    def extChannelErrorType(self, value: _Integer) -> None: ...
    @property
    def extChannelAddValue(self) -> o6.UInt32: ...
    @extChannelAddValue.setter
    def extChannelAddValue(self, value: _Integer) -> None: ...
    @property
    def qualifiedChannelQualifier(self) -> o6.UInt32: ...
    @qualifiedChannelQualifier.setter
    def qualifiedChannelQualifier(self, value: _Integer) -> None: ...
    @property
    def manufacturerData(self) -> o6.ByteString: ...
    @manufacturerData.setter
    def manufacturerData(self, value: o6.ByteString) -> None: ...
    @property
    def message(self) -> o6.LocalizedText: ...
    @message.setter
    def message(self, value: o6.LocalizedText) -> None: ...
    @property
    def helpText(self) -> o6.LocalizedText: ...
    @helpText.setter
    def helpText(self, value: o6.LocalizedText) -> None: ...

class PnIM5DataType(ns0.datatypes.Structure):
    """Contains the fields of the APDU element I&M5 | I&M5Data"""

    @property
    def annotation(self) -> o6.String: ...
    @annotation.setter
    def annotation(self, value: o6.String) -> None: ...
    @property
    def orderId(self) -> o6.String: ...
    @orderId.setter
    def orderId(self, value: o6.String) -> None: ...
    @property
    def vendorId(self) -> o6.UInt16: ...
    @vendorId.setter
    def vendorId(self, value: _Integer) -> None: ...
    @property
    def serialNumber(self) -> o6.String: ...
    @serialNumber.setter
    def serialNumber(self, value: o6.String) -> None: ...
    @property
    def hardwareRevision(self) -> o6.String: ...
    @hardwareRevision.setter
    def hardwareRevision(self, value: o6.String) -> None: ...
    @property
    def softwareRevision(self) -> o6.String: ...
    @softwareRevision.setter
    def softwareRevision(self, value: o6.String) -> None: ...

class IMTagSelectorEnumeration(enum.IntFlag):
    FUNCTION = 0
    LOCATION = 1
    BOTH = 2
