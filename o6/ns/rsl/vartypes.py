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

"""Generated OPC UA rsl namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.ns0 as ns0

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.variabletype(nodeId="ns=rsl;i=2002", browseName="ns=rsl;RelativeValueType", displayName="RelativeValueType", isAbstract=True, valueRank=o6.ValueRank.ANY)
class RelativeValueType(ns0.vartypes.BaseDataVariableType):
    base: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=rsl;i=6001", browseName="ns=rsl;Base", dataType=o6.NodeId, accessLevel=3, userAccessLevel=1)
    )


@o6.variabletype(nodeId="ns=rsl;i=2003", browseName="ns=rsl;SpatialLocationType", displayName="SpatialLocationType", isAbstract=True, valueRank=o6.ValueRank.ANY)
class SpatialLocationType(RelativeValueType):
    base: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=rsl;i=6002", browseName="ns=rsl;Base", dataType=o6.NodeId, accessLevel=3, userAccessLevel=1)
    )
    orientation: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=rsl;i=6004", browseName="ns=rsl;Orientation", accessLevel=3, userAccessLevel=1)
    )
    position: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=rsl;i=6003", browseName="ns=rsl;Position", accessLevel=3, userAccessLevel=1)
    )


@o6.variabletype(
    nodeId="ns=rsl;i=2004", browseName="ns=rsl;CartesianFrameAngleOrientationType", displayName="CartesianFrameAngleOrientationType", dataType=ns0.datatypes.ThreeDFrame
)
class CartesianFrameAngleOrientationType(SpatialLocationType):
    base: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=rsl;i=6005", browseName="ns=rsl;Base", dataType=o6.NodeId, accessLevel=3, userAccessLevel=1)
    )
    orientation: RpyOrientationType
    position: ns0.vartypes.ThreeDCartesianCoordinatesType


@o6.variabletype(
    nodeId="ns=rsl;i=2005",
    browseName="ns=rsl;RpyOrientationType",
    displayName="RpyOrientationType",
    dataType=ns0.datatypes.ThreeDOrientation,
    value=ns0.datatypes.ThreeDOrientation(a=0.0, b=0.0, c=0.0),
)
class RpyOrientationType(ns0.vartypes.OrientationType):
    a: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=rsl;i=6037", browseName="ns=rsl;A", description="Rotation around X Axis (Roll) as per ISO 9787:2013", dataType=o6.Double, accessLevel=3, userAccessLevel=1
        )
    )
    b: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=rsl;i=6040", browseName="ns=rsl;B", description="Rotation around Y Axis (Pitch) as per ISO 9787:2013", dataType=o6.Double, accessLevel=3, userAccessLevel=1
        )
    )
    c: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=rsl;i=6041", browseName="ns=rsl;C", description="Rotation around Z Axis (Yaw) as per ISO 9787:2013", dataType=o6.Double, accessLevel=3, userAccessLevel=1
        )
    )


del Any, TYPE_CHECKING, uuid, o6, ns0
