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

import o6.ns.di as di

import o6.ns.fx_data as fx_data

import o6.ns.ns0 as ns0

class FxVersion(ns0.datatypes.Structure):
    @property
    def major(self) -> o6.UInt16: ...
    @major.setter
    def major(self, value: _Integer) -> None: ...
    @property
    def minor(self) -> o6.UInt16: ...
    @minor.setter
    def minor(self, value: _Integer) -> None: ...
    @property
    def build(self) -> o6.UInt16: ...
    @build.setter
    def build(self, value: _Integer) -> None: ...
    @property
    def subBuild(self) -> o6.UInt16: ...
    @subBuild.setter
    def subBuild(self, value: _Integer) -> None: ...

class ClampKindEnum(enum.IntFlag):
    SCREW = 0
    THUMB = 1

class SocketKindEnum(enum.IntFlag):
    RJ45 = 0
    M12 = 1

class CommHealthOptionSet(enum.IntFlag):
    COMM_INITIAL = 1 << 0
    COMM_PRE_OPERATIONAL = 1 << 1
    COMM_ERROR = 1 << 2

class DeviceHealthOptionSet(enum.IntFlag):
    DEVICE_FAILURE = 1 << 0
    DEVICE_CHECK_FUNCTION = 1 << 1
    DEVICE_MAINTENANCE_REQUIRED = 1 << 2
    DEVICE_OFF_SPEC = 1 << 3

class ConnectionEndpointStatusEnum(enum.IntFlag):
    """This enumeration defines the values of the FlcConnectionStatus of an FlcConnectionEndpointType."""

    INITIAL = 0
    READY = 1
    PRE_OPERATIONAL = 2
    OPERATIONAL = 3
    ERROR = 4

class OperationalHealthOptionSet(enum.IntFlag):
    OPERATIONAL_WARNING = 1 << 16
    OPERATIONAL_ERROR = 1 << 17
    SUB_OPERATIONAL_WARNING = 1 << 18
    SUB_OPERATIONAL_ERROR = 1 << 19

class AggregatedHealthDataType(ns0.datatypes.Structure):
    @property
    def aggregatedDeviceHealth(self) -> DeviceHealthOptionSet: ...
    @aggregatedDeviceHealth.setter
    def aggregatedDeviceHealth(self, value: _Integer) -> None: ...
    @property
    def aggregatedOperationalHealth(self) -> OperationalHealthOptionSet: ...
    @aggregatedOperationalHealth.setter
    def aggregatedOperationalHealth(self, value: _Integer) -> None: ...

class PublisherQosDataType(ns0.datatypes.Structure):
    @property
    def qosCategory(self) -> o6.String: ...
    @qosCategory.setter
    def qosCategory(self, value: o6.String) -> None: ...
    @property
    def datagramQos(self) -> list[ns0.datatypes.TransmitQosDataType]: ...
    @datagramQos.setter
    def datagramQos(self, value: Sequence[ns0.datatypes.TransmitQosDataType]) -> None: ...

class SubscriberQosDataType(ns0.datatypes.Structure):
    @property
    def qosCategory(self) -> o6.String: ...
    @qosCategory.setter
    def qosCategory(self, value: o6.String) -> None: ...
    @property
    def datagramQos(self) -> list[ns0.datatypes.ReceiveQosDataType]: ...
    @datagramQos.setter
    def datagramQos(self, value: Sequence[ns0.datatypes.ReceiveQosDataType]) -> None: ...

class ApplicationId(ns0.datatypes.Union):
    @property
    def idNumeric(self) -> o6.UInt32: ...
    @idNumeric.setter
    def idNumeric(self, value: _Integer) -> None: ...
    @property
    def idString(self) -> o6.String: ...
    @idString.setter
    def idString(self, value: o6.String) -> None: ...
    @property
    def idGuid(self) -> o6.Guid: ...
    @idGuid.setter
    def idGuid(self, value: o6.Guid) -> None: ...
    @property
    def idByteString(self) -> o6.ByteString: ...
    @idByteString.setter
    def idByteString(self, value: o6.ByteString) -> None: ...

class ApplicationIdentifierDataType(ns0.datatypes.Structure):
    @property
    def name(self) -> o6.LocalizedText: ...
    @name.setter
    def name(self, value: o6.LocalizedText) -> None: ...
    @property
    def uniqueIdentifier(self) -> ApplicationId: ...
    @uniqueIdentifier.setter
    def uniqueIdentifier(self, value: ApplicationId) -> None: ...
