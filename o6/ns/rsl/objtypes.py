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
from . import vartypes as rsl_vartypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(nodeId="ns=rsl;i=1002", browseName="ns=rsl;SpatialObjectType", displayName="SpatialObjectType")
class SpatialObjectType(ns0.objtypes.BaseObjectType):
    alternativeFrames: ns0.objtypes.FolderType | None
    attachPoints: ns0.objtypes.FolderType | None
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=rsl;i=6017",
            browseName="DefaultInstanceBrowseName",
            description="The default BrowseName for instances of the type.",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("rsl:SpatialObject"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    identifier: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=rsl;i=6016", browseName="ns=rsl;Identifier", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    internalFrames: ns0.objtypes.FolderType | None
    positionFrame: rsl_vartypes.SpatialLocationType


@o6.objecttype(nodeId="ns=rsl;i=1003", browseName="ns=rsl;SpatialObjectsListType", displayName="SpatialObjectsListType")
class SpatialObjectsListType(ns0.objtypes.BaseObjectType):
    identifier: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=rsl;i=6024", browseName="ns=rsl;Identifier", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    langleSpatialObjectRangle: SpatialObjectType | None
    nodeVersion: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=rsl;i=6027", browseName="NodeVersion", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    worldFrame: rsl_vartypes.SpatialLocationType


o6.reference(SpatialObjectsListType, "i=41", "i=2133")


del Any, TYPE_CHECKING, uuid, o6, ns0, rsl_vartypes
