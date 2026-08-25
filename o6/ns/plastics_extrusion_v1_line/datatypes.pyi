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

import o6.ns.plastics_rubber as plastics_rubber

class MaterialMappingType(ns0.datatypes.Structure):
    @property
    def materialId(self) -> o6.String: ...
    @materialId.setter
    def materialId(self, value: o6.String) -> None: ...
    @property
    def materialLot(self) -> o6.String: ...
    @materialLot.setter
    def materialLot(self, value: o6.String) -> None: ...
    @property
    def hopperId(self) -> o6.String: ...
    @hopperId.setter
    def hopperId(self, value: o6.String) -> None: ...
