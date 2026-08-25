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

import o6.ns.irdi as irdi

import o6.ns.ns0 as ns0

class ResetModeEnum(enum.IntFlag):
    APPLICATION = 1
    COMMUNICATION = 2712
    FACTORY = 2713

class ExecutionModeEnum(enum.IntFlag):
    START = 2
    ABORT = 255

class PatDictionaryEnum(enum.IntFlag):
    CAS = 0
    PAT = 1
    USER_DEFINED = 2

class ChemicalSubstanceDataType(ns0.datatypes.Structure):
    @property
    def patDictionary(self) -> PatDictionaryEnum: ...
    @patDictionary.setter
    def patDictionary(self, value: _Integer) -> None: ...
    @property
    def label(self) -> o6.LocalizedText: ...
    @label.setter
    def label(self, value: o6.LocalizedText) -> None: ...
    @property
    def id(self) -> o6.LocalizedText: ...
    @id.setter
    def id(self, value: o6.LocalizedText) -> None: ...
