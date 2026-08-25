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

import o6.ns.ns0 as ns0

class GsdGenIoConsistencyEnumeration(enum.IntFlag):
    ITEM_CONSISTENCY = 0
    ALL_ITEMS_CONSISTENCY = 1

class GsdGenIoQualityFormatEnumeration(enum.IntFlag):
    QUALIFIER = 0
    EMBEDDED_STATUS = 1
    STATUS = 2

class GsdGenChannelAccumulativeEnumeration(enum.IntFlag):
    SINGLE = 0
    ACCUMULATIVE = 256

class GsdGenChannelMaintenanceEnumeration(enum.IntFlag):
    FAULT = 0
    MAINTENANCE_REQUIRED = 512
    MAINTENANCE_DEMANDED = 1024
    USE_QUALIFIED_CHANNEL_QUALIFIER = 1536

class GsdGenChannelSpecifierEnumeration(enum.IntFlag):
    ALL_DISAPPEARS = 0
    APPEARS = 2048
    DISAPPEARS = 4096
    DISAPPEARS_OTHER_REMAIN = 6144

class GsdGenChannelDirectionEnumeration(enum.IntFlag):
    MANUFACTURER_SPECIFIC = 0
    INPUT_CHANNEL = 8192
    OUTPUT_CHANNEL = 16384
    BIDIRECTIONAL_CHANNEL = 24576

class GsdGenIoTimeStampDataType(ns0.datatypes.Structure):
    @property
    def status(self) -> o6.UInt16: ...
    @status.setter
    def status(self, value: _Integer) -> None: ...
    @property
    def seconds(self) -> o6.UInt64: ...
    @seconds.setter
    def seconds(self, value: _Integer) -> None: ...
    @property
    def nanoseconds(self) -> o6.UInt32: ...
    @nanoseconds.setter
    def nanoseconds(self, value: _Integer) -> None: ...

class GsdGenIoTimeDataType(ns0.datatypes.Structure):
    @property
    def numberOfMilliseconds(self) -> o6.UInt32: ...
    @numberOfMilliseconds.setter
    def numberOfMilliseconds(self, value: _Integer) -> None: ...
    @property
    def numberOfDays(self) -> o6.UInt16: ...
    @numberOfDays.setter
    def numberOfDays(self, value: _Integer) -> None: ...

class GsdGenIoCommunicationStatusEnumeration(enum.IntFlag):
    INDATA = 0
    OFFLINE = 1

class GsdGenIoConfigurationStatusEnumeration(enum.IntFlag):
    OK = 0
    SUBSTITUTE = 1
    WRONG = 2
    UNKNOWN = 3
