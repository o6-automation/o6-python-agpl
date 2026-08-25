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

class SoftwareVersionFileType(enum.IntFlag):
    CURRENT = 0
    PENDING = 1
    FALLBACK = 2

class UpdateBehavior(enum.IntFlag):
    KEEPS_PARAMETERS = 1 << 0
    WILL_DISCONNECT = 1 << 1
    REQUIRES_POWER_CYCLE = 1 << 2
    WILL_REBOOT = 1 << 3
    NEEDS_PREPARATION = 1 << 4

class SoftwareClass(enum.IntFlag):
    FIRMWARE = 0
    APPLICATION = 1
    CONFIGURATION = 2
    SOLUTION = 3

class LocationIndicationType(enum.IntFlag):
    VISUAL = 1 << 0
    AUDIBLE = 1 << 1

class DeviceHealthEnumeration(enum.IntFlag):
    NORMAL = 0
    FAILURE = 1
    CHECK_FUNCTION = 2
    OFF_SPEC = 3
    MAINTENANCE_REQUIRED = 4

class FetchResultDataType(ns0.datatypes.Structure):
    pass

class ParameterResultDataType(ns0.datatypes.Structure):
    @property
    def nodePath(self) -> list[o6.QualifiedName]: ...
    @nodePath.setter
    def nodePath(self, value: Sequence[o6.QualifiedName]) -> None: ...
    @property
    def statusCode(self) -> o6.StatusCode: ...
    @statusCode.setter
    def statusCode(self, value: _Integer) -> None: ...
    @property
    def diagnostics(self) -> o6.DiagnosticInfo: ...
    @diagnostics.setter
    def diagnostics(self, value: o6.DiagnosticInfo) -> None: ...

class TransferResultErrorDataType(FetchResultDataType):
    @property
    def status(self) -> o6.Int32: ...
    @status.setter
    def status(self, value: _Integer) -> None: ...
    @property
    def diagnostics(self) -> o6.DiagnosticInfo: ...
    @diagnostics.setter
    def diagnostics(self, value: o6.DiagnosticInfo) -> None: ...

class TransferResultDataDataType(FetchResultDataType):
    @property
    def sequenceNumber(self) -> o6.Int32: ...
    @sequenceNumber.setter
    def sequenceNumber(self, value: _Integer) -> None: ...
    @property
    def endOfResults(self) -> o6.Boolean: ...
    @endOfResults.setter
    def endOfResults(self, value: _Boolean) -> None: ...
    @property
    def parameterDefs(self) -> list[ParameterResultDataType]: ...
    @parameterDefs.setter
    def parameterDefs(self, value: Sequence[ParameterResultDataType]) -> None: ...
