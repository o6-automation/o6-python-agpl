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

import o6.ns.machinery as machinery

import o6.ns.ns0 as ns0

class SEMI_E10SystemStateDataType(ns0.datatypes.Structure):
    @property
    def id(self) -> o6.UInt32: ...
    @id.setter
    def id(self, value: _Integer) -> None: ...
    @property
    def priority(self) -> o6.UInt32: ...
    @priority.setter
    def priority(self, value: _Integer) -> None: ...

class SEMI_E10SystemStateInfoDataType(ns0.datatypes.Structure):
    @property
    def id(self) -> o6.UInt32: ...
    @id.setter
    def id(self, value: _Integer) -> None: ...
    @property
    def name(self) -> o6.LocalizedText: ...
    @name.setter
    def name(self, value: o6.LocalizedText) -> None: ...
    @property
    def parentStateId(self) -> o6.UInt32: ...
    @parentStateId.setter
    def parentStateId(self, value: _Integer) -> None: ...
    @property
    def description(self) -> o6.LocalizedText: ...
    @description.setter
    def description(self, value: o6.LocalizedText) -> None: ...
