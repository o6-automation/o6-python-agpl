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
from . import datatypes as gpos_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.variabletype(
    nodeId="ns=gpos;i=2003",
    browseName="ns=gpos;GlobalLocationType",
    displayName="GlobalLocationType",
    description="Defines the location of an object - in a global coordinate reference system",
    dataType=gpos_datypes.GlobalLocationDataType,
)
class GlobalLocationType(rsl.vartypes.SpatialLocationType):
    orientation: ns0.vartypes.ThreeDOrientationType | None
    position: GlobalPositionType


@o6.variabletype(
    nodeId="ns=gpos;i=2006",
    browseName="ns=gpos;GlobalPositionType",
    displayName="GlobalPositionType",
    description="Describes a point (i.e. a position) in 2 or 3 dimensions. Important: A Point object shall be interpreted according to the CoordinateReferenceSystem.",
    dataType=gpos_datypes.GlobalPositionDataType,
)
class GlobalPositionType(ns0.vartypes.BaseDataVariableType):
    accuracy: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=gpos;i=6028",
            browseName="ns=gpos;Accuracy",
            description="The horizontal accuracy of the position in meters.",
            dataType=o6.Double,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    coordinateReferenceSystem: ns0.vartypes.MultiStateValueDiscreteType
    elevation: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=gpos;i=6030",
            browseName="ns=gpos;Elevation",
            description="MUST be interpreted according to the ElevationReference. If floor, the height relative to specific floor in meter",
            dataType=o6.Double,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    elevationReference: ns0.vartypes.MultiStateValueDiscreteType | None
    floor: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=gpos;i=6012",
            browseName="ns=gpos;Floor",
            description="A logical and non-localized representation for a building floor. Floor 0 represents the floor designated as 'ground'. Negative numbers indicate floors below the ground floor and positive numbers indicate floors above the ground floor. When implemented, the floor value MUST match described logical numbering scheme, which can be different from any numbering used within a building. Values can be expressed as an integer value, or as a float as required for mezzanine floor levels.",
            dataType=o6.Float,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    latitude: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=gpos;i=6029",
            browseName="ns=gpos;Latitude",
            description="MUST be interpreted according to the CoordinateReferenceSystem",
            dataType=o6.Double,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    longitude: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=gpos;i=6027",
            browseName="ns=gpos;Longitude",
            description="MUST be interpreted according to the CoordinateReferenceSystem",
            dataType=o6.Double,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    sourceId: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=gpos;i=6038",
            browseName="ns=gpos;SourceId",
            description="Reference to the zone or provider calculating the position",
            dataType=o6.NodeId,
            accessLevel=3,
            userAccessLevel=1,
        )
    )


del Any, TYPE_CHECKING, uuid, o6, ns0, rsl, gpos_datypes
