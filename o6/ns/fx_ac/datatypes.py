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

"""Generated OPC UA fx_ac namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.fx_data as fx_data
import o6.ns.ns0 as ns0
from . import reftypes as fx_ac_reftypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.datatype(nodeId="ns=fx_ac;i=25", browseName="FxVersion", defaultEncodingId="ns=fx_ac;i=91")
class FxVersion(ns0.datatypes.Structure):
    major: o6.UInt16
    minor: o6.UInt16
    build: o6.UInt16
    subBuild: o6.UInt16


@o6.enumtype(nodeId="ns=fx_ac;i=3001", browseName="ClampKindEnum")
class ClampKindEnum(ns0.datatypes.Enumeration):
    SCREW = o6.enumfield(0, name="Screw")
    THUMB = o6.enumfield(1, name="Thumb")


@o6.enumtype(nodeId="ns=fx_ac;i=3002", browseName="SocketKindEnum")
class SocketKindEnum(ns0.datatypes.Enumeration):
    RJ45 = o6.enumfield(0, name="RJ45")
    M12 = o6.enumfield(1, name="M12")


@o6.optionsettype(nodeId="ns=fx_ac;i=3004", browseName="CommHealthOptionSet", base=o6.UInt16)
class CommHealthOptionSet:
    COMM_INITIAL = o6.bitmask(0x01 << 0, name="CommInitial")
    COMM_PRE_OPERATIONAL = o6.bitmask(0x01 << 1, name="CommPreOperational")
    COMM_ERROR = o6.bitmask(0x01 << 2, name="CommError")


@o6.optionsettype(nodeId="ns=fx_ac;i=3005", browseName="DeviceHealthOptionSet", base=o6.UInt16)
class DeviceHealthOptionSet:
    DEVICE_FAILURE = o6.bitmask(0x01 << 0, name="DeviceFailure")
    DEVICE_CHECK_FUNCTION = o6.bitmask(0x01 << 1, name="DeviceCheckFunction")
    DEVICE_MAINTENANCE_REQUIRED = o6.bitmask(0x01 << 2, name="DeviceMaintenanceRequired")
    DEVICE_OFF_SPEC = o6.bitmask(0x01 << 3, name="DeviceOffSpec")


@o6.enumtype(
    nodeId="ns=fx_ac;i=3007",
    browseName="ConnectionEndpointStatusEnum",
    description="This enumeration defines the values of the FlcConnectionStatus of an FlcConnectionEndpointType.",
)
class ConnectionEndpointStatusEnum(ns0.datatypes.Enumeration):
    INITIAL = o6.enumfield(0, name="Initial")
    READY = o6.enumfield(1, name="Ready")
    PRE_OPERATIONAL = o6.enumfield(2, name="PreOperational")
    OPERATIONAL = o6.enumfield(3, name="Operational")
    ERROR = o6.enumfield(4, name="Error")


@o6.optionsettype(nodeId="ns=fx_ac;i=3010", browseName="OperationalHealthOptionSet", base=o6.UInt32)
class OperationalHealthOptionSet:
    OPERATIONAL_WARNING = o6.bitmask(0x01 << 16, name="OperationalWarning")
    OPERATIONAL_ERROR = o6.bitmask(0x01 << 17, name="OperationalError")
    SUB_OPERATIONAL_WARNING = o6.bitmask(0x01 << 18, name="SubOperationalWarning")
    SUB_OPERATIONAL_ERROR = o6.bitmask(0x01 << 19, name="SubOperationalError")


@o6.datatype(nodeId="ns=fx_ac;i=3003", browseName="AggregatedHealthDataType", defaultEncodingId="ns=fx_ac;i=5004")
class AggregatedHealthDataType(ns0.datatypes.Structure):
    aggregatedDeviceHealth: DeviceHealthOptionSet
    aggregatedOperationalHealth: OperationalHealthOptionSet


@o6.datatype(nodeId="ns=fx_ac;i=3011", browseName="PublisherQosDataType", defaultEncodingId="ns=fx_ac;i=5024")
class PublisherQosDataType(ns0.datatypes.Structure):
    qosCategory: o6.String
    datagramQos: list[ns0.datatypes.TransmitQosDataType]


@o6.datatype(nodeId="ns=fx_ac;i=3012", browseName="SubscriberQosDataType", defaultEncodingId="ns=fx_ac;i=5027")
class SubscriberQosDataType(ns0.datatypes.Structure):
    qosCategory: o6.String
    datagramQos: list[ns0.datatypes.ReceiveQosDataType]


@o6.datatype(nodeId="ns=fx_ac;i=3013", browseName="ApplicationId", defaultEncodingId="ns=fx_ac;i=5003")
class ApplicationId(ns0.datatypes.Union):
    idNumeric: o6.UInt32
    idString: o6.String
    idGuid: o6.Guid
    idByteString: o6.ByteString


@o6.datatype(nodeId="ns=fx_ac;i=28", browseName="ApplicationIdentifierDataType", defaultEncodingId="ns=fx_ac;i=60")
class ApplicationIdentifierDataType(ns0.datatypes.Structure):
    name: o6.LocalizedText
    uniqueIdentifier: ApplicationId


del Any, TYPE_CHECKING, uuid, o6, di, fx_data, ns0, fx_ac_reftypes
