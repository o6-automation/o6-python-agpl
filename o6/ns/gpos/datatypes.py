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

"""Generated OPC UA gpos namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.ns0 as ns0
import o6.ns.rsl as rsl

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.datatype(nodeId="ns=gpos;i=3003", browseName="3DGeographicCoordinateDataType", description="Represents a geographic coordinate", defaultEncodingId="ns=gpos;i=5014")
class ThreeDGeographicCoordinateDataType(ns0.datatypes.Structure):
    longitude: o6.Double
    latitude: o6.Double
    elevation: o6.Double | None


@o6.datatype(
    nodeId="ns=gpos;i=3005",
    browseName="GroundControlPointDataType",
    description="Defines a pair of coordinates - local and global - to allow geo-references from local coordinate to a global coordinate system",
    defaultEncodingId="ns=gpos;i=5008",
)
class GroundControlPointDataType(ns0.datatypes.Structure):
    globalPosition: ThreeDGeographicCoordinateDataType
    localPosition: ns0.datatypes.ThreeDCartesianCoordinates


@o6.datatype(nodeId="ns=gpos;i=3006", browseName="GlobalPositionDataType", description="Represents a global position", defaultEncodingId="ns=gpos;i=5001")
class GlobalPositionDataType(ThreeDGeographicCoordinateDataType):
    longitude: o6.Double
    latitude: o6.Double
    elevation: o6.Double | None
    accuracy: o6.Double | None
    floor: o6.Float | None


@o6.datatype(nodeId="ns=gpos;i=3004", browseName="GlobalLocationDataType", description="Represents a global location", defaultEncodingId="ns=gpos;i=5004")
class GlobalLocationDataType(ns0.datatypes.Structure):
    position: GlobalPositionDataType
    orientation: ns0.datatypes.ThreeDOrientation | None


del Any, TYPE_CHECKING, uuid, o6, ns0, rsl
