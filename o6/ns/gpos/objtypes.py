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
from . import vartypes as gpos_vartypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(
    nodeId="ns=gpos;i=1005",
    browseName="ns=gpos;ZoneType",
    displayName="ZoneType",
    description="Defines an area, in which a local location is computed, e.g. via a RTLS or an proximity based system like RFID. For that reason it might have a set of GroundControlPoints defining the extent or just a point and a radius.",
)
class ZoneType(ns0.objtypes.BaseObjectType):
    building: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=gpos;i=6010", browseName="ns=gpos;Building", description="Name of the building", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    floor: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=gpos;i=6011", browseName="ns=gpos;Floor", description="Name of the floor", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    groundControlPoints: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=gpos;i=6047",
            browseName="ns=gpos;GroundControlPoints",
            description="Points defining the extent of the zone",
            dataType=gpos_datypes.GroundControlPointDataType,
            valueRank=1,
            arrayDimensions=[0],
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    incompleteConfiguration: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=gpos;i=6013",
            browseName="ns=gpos;IncompleteConfiguration",
            description="Indicates if the configuration is complete. FALSE if configuration is complete.",
            dataType=o6.Boolean,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    position: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=gpos;i=6045",
            browseName="ns=gpos;Position",
            description="Describes a point (i.e. a position) in 2 or 3 dimensions.",
            dataType=gpos_datypes._3DGeographicCoordinateDataType,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    radius: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=gpos;i=6046",
            browseName="ns=gpos;Radius",
            description="For proximity-based systems. Describes the zone as a circular region with a given radius in meters around the position.",
            dataType=o6.Double,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    site: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=gpos;i=6026", browseName="ns=gpos;Site", description="Name of the site", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    zoneId: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=gpos;i=6043", browseName="ns=gpos;ZoneId", description="A unique identifier of the zone (e.g. a GUID).", dataType=o6.String, accessLevel=3, userAccessLevel=1
        )
    )


del Any, TYPE_CHECKING, uuid, o6, ns0, rsl, gpos_datypes, gpos_vartypes
