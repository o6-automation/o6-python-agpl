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

class RootCauseDataType(ns0.datatypes.Structure):
    """Root cause of an alarm"""

    @property
    def rootCauseId(self) -> o6.NodeId: ...
    @rootCauseId.setter
    def rootCauseId(self, value: o6.NodeId) -> None: ...
    @property
    def rootCause(self) -> o6.LocalizedText: ...
    @rootCause.setter
    def rootCause(self, value: o6.LocalizedText) -> None: ...

class NameNodeIdDataType(ns0.datatypes.Structure):
    """A human-readable name of something plus optionally the NodeId in case the something is represented in the AddressSpace"""

    @property
    def name(self) -> o6.LocalizedText: ...
    @name.setter
    def name(self, value: o6.LocalizedText) -> None: ...
    @property
    def nodeId(self) -> o6.NodeId: ...
    @nodeId.setter
    def nodeId(self, value: o6.NodeId) -> None: ...

class MaintenanceMethodEnum(enum.IntFlag):
    LOCAL = 0
    REMOTE = 1
