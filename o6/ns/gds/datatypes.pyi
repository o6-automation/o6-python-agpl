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

class ApplicationRecordDataType(ns0.datatypes.Structure):
    @property
    def applicationId(self) -> o6.NodeId: ...
    @applicationId.setter
    def applicationId(self, value: o6.NodeId) -> None: ...
    @property
    def applicationUri(self) -> o6.String: ...
    @applicationUri.setter
    def applicationUri(self, value: o6.String) -> None: ...
    @property
    def applicationType(self) -> ns0.datatypes.ApplicationType: ...
    @applicationType.setter
    def applicationType(self, value: ns0.datatypes.ApplicationType) -> None: ...
    @property
    def applicationNames(self) -> list[o6.LocalizedText]: ...
    @applicationNames.setter
    def applicationNames(self, value: Sequence[o6.LocalizedText]) -> None: ...
    @property
    def productUri(self) -> o6.String: ...
    @productUri.setter
    def productUri(self, value: o6.String) -> None: ...
    @property
    def discoveryUrls(self) -> list[o6.String]: ...
    @discoveryUrls.setter
    def discoveryUrls(self, value: Sequence[o6.String]) -> None: ...
    @property
    def serverCapabilities(self) -> list[o6.String]: ...
    @serverCapabilities.setter
    def serverCapabilities(self, value: Sequence[o6.String]) -> None: ...
