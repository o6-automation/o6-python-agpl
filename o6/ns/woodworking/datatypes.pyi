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

import o6.ns.ia as ia

import o6.ns.isa95_jobcontrol_v2 as isa95_jobcontrol_v2

import o6.ns.machinery as machinery

import o6.ns.machinery_jobs as machinery_jobs

import o6.ns.ns0 as ns0

class WwUnitModeEnumeration(enum.IntFlag):
    """This enumeration represents the generalized mode of a unit."""

    OTHER = 0
    AUTOMATIC = 1
    SEMIAUTOMATIC = 2
    MANUAL = 3
    SETUP = 4
    SLEEP = 5

class WwUnitStateEnumeration(enum.IntFlag):
    """This enumeration represents the generalized state of a unit."""

    OFFLINE = 0
    STANDBY = 1
    READY = 2
    WORKING = 3
    ERROR = 4

class WwMessageArgumentValueDataType(ns0.datatypes.Union):
    """The WwArgumentValueDataType definition defines the possible types of an argument value."""

    @property
    def array(self) -> list[WwMessageArgumentValueDataType]: ...
    @array.setter
    def array(self, value: Sequence[WwMessageArgumentValueDataType]) -> None: ...
    @property
    def boolean(self) -> o6.Boolean: ...
    @boolean.setter
    def boolean(self, value: _Boolean) -> None: ...
    @property
    def int16(self) -> o6.Int16: ...
    @int16.setter
    def int16(self, value: _Integer) -> None: ...
    @property
    def int32(self) -> o6.Int32: ...
    @int32.setter
    def int32(self, value: _Integer) -> None: ...
    @property
    def int64(self) -> o6.Int64: ...
    @int64.setter
    def int64(self, value: _Integer) -> None: ...
    @property
    def sByte(self) -> o6.SByte: ...
    @sByte.setter
    def sByte(self, value: _Integer) -> None: ...
    @property
    def uInt16(self) -> o6.UInt16: ...
    @uInt16.setter
    def uInt16(self, value: _Integer) -> None: ...
    @property
    def uInt32(self) -> o6.UInt32: ...
    @uInt32.setter
    def uInt32(self, value: _Integer) -> None: ...
    @property
    def uInt64(self) -> o6.UInt64: ...
    @uInt64.setter
    def uInt64(self, value: _Integer) -> None: ...
    @property
    def byte(self) -> o6.Byte: ...
    @byte.setter
    def byte(self, value: _Integer) -> None: ...
    @property
    def dateTime(self) -> o6.DateTime: ...
    @dateTime.setter
    def dateTime(self, value: o6.DateTime) -> None: ...
    @property
    def guid(self) -> o6.Guid: ...
    @guid.setter
    def guid(self, value: o6.Guid) -> None: ...
    @property
    def localizedText(self) -> o6.LocalizedText: ...
    @localizedText.setter
    def localizedText(self, value: o6.LocalizedText) -> None: ...
    @property
    def double(self) -> o6.Double: ...
    @double.setter
    def double(self, value: SupportsFloat) -> None: ...
    @property
    def float(self) -> o6.Float: ...
    @float.setter
    def float(self, value: SupportsFloat) -> None: ...
    @property
    def string(self) -> o6.String: ...
    @string.setter
    def string(self, value: o6.String) -> None: ...
    @property
    def other(self) -> o6.String: ...
    @other.setter
    def other(self, value: o6.String) -> None: ...

class WwMessageArgumentDataType(ns0.datatypes.Argument):
    """The WwArgumentDataType definition extends the argument structure with an argument value."""

    @property
    def name(self) -> o6.String: ...
    @name.setter
    def name(self, value: o6.String) -> None: ...
    @property
    def dataType(self) -> o6.NodeId: ...
    @dataType.setter
    def dataType(self, value: o6.NodeId) -> None: ...
    @property
    def valueRank(self) -> o6.Int32: ...
    @valueRank.setter
    def valueRank(self, value: _Integer) -> None: ...
    @property
    def arrayDimensions(self) -> list[o6.UInt32]: ...
    @arrayDimensions.setter
    def arrayDimensions(self, value: Sequence[_Integer]) -> None: ...
    @property
    def description(self) -> o6.LocalizedText: ...
    @description.setter
    def description(self, value: o6.LocalizedText) -> None: ...
    @property
    def value(self) -> WwMessageArgumentValueDataType: ...
    @value.setter
    def value(self, value: WwMessageArgumentValueDataType) -> None: ...

class WwEventCategoryEnumeration(enum.IntFlag):
    """This enumeration represents the category of an event."""

    OTHER = 0
    DIAGNOSTIC = 1
    INFORMATION = 2
    WARNING = 3
    ALARM = 4
    ERROR = 5
