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

"""Generated OPC UA pngsdgm namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
from . import reftypes as pngsdgm_reftypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.enumtype(nodeId="ns=pngsdgm;i=3002", browseName="GsdGenIoConsistencyEnumeration")
class GsdGenIoConsistencyEnumeration(ns0.datatypes.Enumeration):
    ITEM_CONSISTENCY = o6.enumfield(0, name="ITEM_CONSISTENCY")
    ALL_ITEMS_CONSISTENCY = o6.enumfield(1, name="ALL_ITEMS_CONSISTENCY")


@o6.enumtype(nodeId="ns=pngsdgm;i=3003", browseName="GsdGenIoQualityFormatEnumeration")
class GsdGenIoQualityFormatEnumeration(ns0.datatypes.Enumeration):
    QUALIFIER = o6.enumfield(0, name="QUALIFIER")
    EMBEDDED_STATUS = o6.enumfield(1, name="EMBEDDED_STATUS")
    STATUS = o6.enumfield(2, name="STATUS")


@o6.enumtype(nodeId="ns=pngsdgm;i=3004", browseName="GsdGenChannelAccumulativeEnumeration")
class GsdGenChannelAccumulativeEnumeration(ns0.datatypes.Enumeration):
    SINGLE = o6.enumfield(0, name="SINGLE")
    ACCUMULATIVE = o6.enumfield(256, name="ACCUMULATIVE")


@o6.enumtype(nodeId="ns=pngsdgm;i=3005", browseName="GsdGenChannelMaintenanceEnumeration")
class GsdGenChannelMaintenanceEnumeration(ns0.datatypes.Enumeration):
    FAULT = o6.enumfield(0, name="FAULT")
    MAINTENANCE_REQUIRED = o6.enumfield(512, name="MAINTENANCE_REQUIRED")
    MAINTENANCE_DEMANDED = o6.enumfield(1024, name="MAINTENANCE_DEMANDED")
    USE_QUALIFIED_CHANNEL_QUALIFIER = o6.enumfield(1536, name="USE_QUALIFIED_CHANNEL_QUALIFIER")


@o6.enumtype(nodeId="ns=pngsdgm;i=3006", browseName="GsdGenChannelSpecifierEnumeration")
class GsdGenChannelSpecifierEnumeration(ns0.datatypes.Enumeration):
    ALL_DISAPPEARS = o6.enumfield(0, name="ALL_DISAPPEARS")
    APPEARS = o6.enumfield(2048, name="APPEARS")
    DISAPPEARS = o6.enumfield(4096, name="DISAPPEARS")
    DISAPPEARS_OTHER_REMAIN = o6.enumfield(6144, name="DISAPPEARS_OTHER_REMAIN")


@o6.enumtype(nodeId="ns=pngsdgm;i=3007", browseName="GsdGenChannelDirectionEnumeration")
class GsdGenChannelDirectionEnumeration(ns0.datatypes.Enumeration):
    MANUFACTURER_SPECIFIC = o6.enumfield(0, name="MANUFACTURER_SPECIFIC")
    INPUT_CHANNEL = o6.enumfield(8192, name="INPUT_CHANNEL")
    OUTPUT_CHANNEL = o6.enumfield(16384, name="OUTPUT_CHANNEL")
    BIDIRECTIONAL_CHANNEL = o6.enumfield(24576, name="BIDIRECTIONAL_CHANNEL")


@o6.datatype(nodeId="ns=pngsdgm;i=3008", browseName="GsdGenIoTimeStampDataType", defaultEncodingId="ns=pngsdgm;i=5001")
class GsdGenIoTimeStampDataType(ns0.datatypes.Structure):
    status: o6.UInt16
    seconds: o6.UInt64
    nanoseconds: o6.UInt32


@o6.datatype(nodeId="ns=pngsdgm;i=3009", browseName="GsdGenIoTimeDataType", defaultEncodingId="ns=pngsdgm;i=5004")
class GsdGenIoTimeDataType(ns0.datatypes.Structure):
    numberOfMilliseconds: o6.UInt32
    numberOfDays: o6.UInt16


@o6.enumtype(nodeId="ns=pngsdgm;i=3012", browseName="GsdGenIoCommunicationStatusEnumeration")
class GsdGenIoCommunicationStatusEnumeration(ns0.datatypes.Enumeration):
    INDATA = o6.enumfield(0, name="INDATA")
    OFFLINE = o6.enumfield(1, name="OFFLINE")


@o6.enumtype(nodeId="ns=pngsdgm;i=3015", browseName="GsdGenIoConfigurationStatusEnumeration")
class GsdGenIoConfigurationStatusEnumeration(ns0.datatypes.Enumeration):
    OK = o6.enumfield(0, name="OK")
    SUBSTITUTE = o6.enumfield(1, name="SUBSTITUTE")
    WRONG = o6.enumfield(2, name="WRONG")
    UNKNOWN = o6.enumfield(3, name="UNKNOWN")


del Any, TYPE_CHECKING, uuid, o6, di, ns0, pngsdgm_reftypes
