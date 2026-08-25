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

import o6.ns.amb as amb

import o6.ns.di as di

import o6.ns.ia as ia

import o6.ns.machinery as machinery

import o6.ns.ns0 as ns0

class MaintenanceTaskResultEnum(enum.IntFlag):
    """This enumeration defines the different results when executing a Task.."""

    SUCCESS = 0
    FAILURE = 1
    UNDETERMINED = 2

class SampleInfoType(ns0.datatypes.Structure):
    """This DataType contains metadata for a sample, specifically data on the identification and location of the sample in a container."""

    @property
    def containerId(self) -> o6.String: ...
    @containerId.setter
    def containerId(self, value: o6.String) -> None: ...
    @property
    def sampleId(self) -> o6.String: ...
    @sampleId.setter
    def sampleId(self, value: o6.String) -> None: ...
    @property
    def position(self) -> o6.String: ...
    @position.setter
    def position(self, value: o6.String) -> None: ...
    @property
    def customData(self) -> o6.String: ...
    @customData.setter
    def customData(self, value: o6.String) -> None: ...

class KeyValueType(ns0.datatypes.Structure):
    """A key-value pair similar to 0:KeyValuePair which uses 0:String instead of 0:Qualifiedname for easu of use."""

    @property
    def key(self) -> o6.String: ...
    @key.setter
    def key(self, value: o6.String) -> None: ...
    @property
    def value(self) -> o6.String: ...
    @value.setter
    def value(self, value: o6.String) -> None: ...
