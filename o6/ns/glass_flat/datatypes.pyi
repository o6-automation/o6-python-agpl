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

class LimitedString64:
    pass

class SignificantSideEnumeration(enum.IntFlag):
    INDIFFERENT = 0
    TOP = 1
    DOWN = 2

class StructureAlignmentEnumeration(enum.IntFlag):
    INDIFFERENT = 0
    LONGITUDINAL = 1
    TRANSVERSE = 2

class SpacerMaterialClass(enum.IntFlag):
    OTHER = 0
    METALIC = 1
    TPS = 2
    PLASTIC = 3
    ELASTIC = 4

class UserProfileType(ns0.datatypes.Structure):
    @property
    def name(self) -> o6.String: ...
    @name.setter
    def name(self, value: o6.String) -> None: ...
    @property
    def loginTime(self) -> o6.DateTime: ...
    @loginTime.setter
    def loginTime(self, value: o6.DateTime) -> None: ...
    @property
    def language(self) -> o6.String: ...
    @language.setter
    def language(self, value: o6.String) -> None: ...
    @property
    def measurementFormat(self) -> o6.String: ...
    @measurementFormat.setter
    def measurementFormat(self, value: o6.String) -> None: ...
    @property
    def accessLevel(self) -> o6.String: ...
    @accessLevel.setter
    def accessLevel(self, value: o6.String) -> None: ...
    @property
    def opcUaUser(self) -> o6.Boolean: ...
    @opcUaUser.setter
    def opcUaUser(self, value: _Boolean) -> None: ...

class FileFormatType(ns0.datatypes.Structure):
    @property
    def name(self) -> o6.String: ...
    @name.setter
    def name(self, value: o6.String) -> None: ...
    @property
    def fileExtension(self) -> o6.String: ...
    @fileExtension.setter
    def fileExtension(self, value: o6.String) -> None: ...
    @property
    def version(self) -> o6.String: ...
    @version.setter
    def version(self, value: o6.String) -> None: ...

class CoordinateSystemEnumeration(enum.IntFlag):
    UNKNOWN = 0
    SYSTEM1 = 1
    SYSTEM2 = 2
    SYSTEM3 = 3
    SYSTEM4 = 4
    SYSTEM5 = 5
    SYSTEM6 = 6
    SYSTEM7 = 7
    SYSTEM8 = 8

class CoatingClassEnumeration(enum.IntFlag):
    HARD_COATING = 0
    SOFT_COATING = 1
    COATED_WITH_FOIL_PROTECTION = 2
    USER_DEFINED = 3
