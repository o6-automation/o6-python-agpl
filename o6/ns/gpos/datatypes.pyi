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

import o6.ns.rsl as rsl

class _3DGeographicCoordinateDataType(ns0.datatypes.Structure):
    """Represents a geographic coordinate"""

    @property
    def longitude(self) -> o6.Double: ...
    @longitude.setter
    def longitude(self, value: SupportsFloat) -> None: ...
    @property
    def latitude(self) -> o6.Double: ...
    @latitude.setter
    def latitude(self, value: SupportsFloat) -> None: ...
    @property
    def elevation(self) -> o6.Double | None: ...
    @elevation.setter
    def elevation(self, value: SupportsFloat | None) -> None: ...

class GroundControlPointDataType(ns0.datatypes.Structure):
    """Defines a pair of coordinates - local and global - to allow geo-references from local coordinate to a global coordinate system"""

    @property
    def globalPosition(self) -> _3DGeographicCoordinateDataType: ...
    @globalPosition.setter
    def globalPosition(self, value: _3DGeographicCoordinateDataType) -> None: ...
    @property
    def localPosition(self) -> ns0.datatypes._3DCartesianCoordinates: ...
    @localPosition.setter
    def localPosition(self, value: ns0.datatypes._3DCartesianCoordinates) -> None: ...

class GlobalPositionDataType(_3DGeographicCoordinateDataType):
    """Represents a global position"""

    @property
    def longitude(self) -> o6.Double: ...
    @longitude.setter
    def longitude(self, value: SupportsFloat) -> None: ...
    @property
    def latitude(self) -> o6.Double: ...
    @latitude.setter
    def latitude(self, value: SupportsFloat) -> None: ...
    @property
    def elevation(self) -> o6.Double | None: ...
    @elevation.setter
    def elevation(self, value: SupportsFloat | None) -> None: ...
    @property
    def accuracy(self) -> o6.Double | None: ...
    @accuracy.setter
    def accuracy(self, value: SupportsFloat | None) -> None: ...
    @property
    def floor(self) -> o6.Float | None: ...
    @floor.setter
    def floor(self, value: SupportsFloat | None) -> None: ...

class GlobalLocationDataType(ns0.datatypes.Structure):
    """Represents a global location"""

    @property
    def position(self) -> GlobalPositionDataType: ...
    @position.setter
    def position(self, value: GlobalPositionDataType) -> None: ...
    @property
    def orientation(self) -> ns0.datatypes._3DOrientation | None: ...
    @orientation.setter
    def orientation(self, value: ns0.datatypes._3DOrientation | None) -> None: ...
