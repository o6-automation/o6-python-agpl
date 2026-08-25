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

class RegistrationParameters(ns0.datatypes.Structure):
    @property
    def path(self) -> ns0.datatypes.RelativePath: ...
    @path.setter
    def path(self, value: ns0.datatypes.RelativePath) -> None: ...
    @property
    def selectionFlags(self) -> o6.UInt32: ...
    @selectionFlags.setter
    def selectionFlags(self, value: _Integer) -> None: ...

class RegisteredNode(ns0.datatypes.Structure):
    @property
    def nodeStatus(self) -> o6.Int32: ...
    @nodeStatus.setter
    def nodeStatus(self, value: _Integer) -> None: ...
    @property
    def onlineContextNodeId(self) -> o6.NodeId: ...
    @onlineContextNodeId.setter
    def onlineContextNodeId(self, value: o6.NodeId) -> None: ...
    @property
    def onlineDeviceNodeId(self) -> o6.NodeId: ...
    @onlineDeviceNodeId.setter
    def onlineDeviceNodeId(self, value: o6.NodeId) -> None: ...
    @property
    def offlineContextNodeId(self) -> o6.NodeId: ...
    @offlineContextNodeId.setter
    def offlineContextNodeId(self, value: o6.NodeId) -> None: ...
    @property
    def offlineDeviceNodeId(self) -> o6.NodeId: ...
    @offlineDeviceNodeId.setter
    def offlineDeviceNodeId(self, value: o6.NodeId) -> None: ...

class RegisterNodesResult(ns0.datatypes.Structure):
    @property
    def status(self) -> o6.Int32: ...
    @status.setter
    def status(self, value: _Integer) -> None: ...
    @property
    def registeredNodes(self) -> list[RegisteredNode]: ...
    @registeredNodes.setter
    def registeredNodes(self, value: Sequence[RegisteredNode]) -> None: ...

class TransferIncident(ns0.datatypes.Structure):
    @property
    def contextNodeId(self) -> o6.NodeId: ...
    @contextNodeId.setter
    def contextNodeId(self, value: o6.NodeId) -> None: ...
    @property
    def statusCode(self) -> o6.StatusCode: ...
    @statusCode.setter
    def statusCode(self, value: _Integer) -> None: ...
    @property
    def diagnostics(self) -> o6.DiagnosticInfo: ...
    @diagnostics.setter
    def diagnostics(self, value: o6.DiagnosticInfo) -> None: ...

class ApplyResult(ns0.datatypes.Structure):
    @property
    def status(self) -> o6.Int32: ...
    @status.setter
    def status(self, value: _Integer) -> None: ...
    @property
    def transferIncidents(self) -> list[TransferIncident]: ...
    @transferIncidents.setter
    def transferIncidents(self, value: Sequence[TransferIncident]) -> None: ...

class WindowModeType(enum.IntFlag):
    MODAL_WINDOW = 1
    NON_MODAL_WINDOW = 2
    UIP = 3

class StyleType(enum.IntFlag):
    WINDOW = 1
    DIALOG = 2
