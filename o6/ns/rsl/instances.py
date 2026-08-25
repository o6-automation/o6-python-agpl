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
from . import objtypes as rsl_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

relativeSpatialLocations = ns0.objtypes.FolderType(nodeId="ns=rsl;i=5001", browseName="ns=rsl;RelativeSpatialLocations", parent="i=31915", referenceType=ns0.reftypes.Organizes)
rsl_vartypes.SpatialLocationType(
    nodeId="ns=rsl;i=6014",
    browseName="ns=rsl;PositionFrame",
    modellingRule="Mandatory",
    references=[o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=rsl;i=6015", browseName="ns=rsl;Base", dataType=o6.NodeId, accessLevel=3, userAccessLevel=1))],
    _allow_abstract=True,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(rsl_objtypes.SpatialObjectType, ns0.reftypes.HasComponent, o6.ns["ns=rsl;i=6014"])
rsl_vartypes.SpatialLocationType(
    nodeId="ns=rsl;i=6018",
    browseName="ns=rsl;<FrameIdentifier>",
    modellingRule="MandatoryPlaceholder",
    references=[o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=rsl;i=6019", browseName="ns=rsl;Base", dataType=o6.NodeId, accessLevel=3, userAccessLevel=1))],
    _allow_abstract=True,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.objtypes.FolderType(nodeId="ns=rsl;i=5002", browseName="ns=rsl;AttachPoints", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=rsl;i=6018"])])
o6.reference(rsl_objtypes.SpatialObjectType, ns0.reftypes.HasComponent, o6.ns["ns=rsl;i=5002"])
rsl_vartypes.SpatialLocationType(
    nodeId="ns=rsl;i=6020",
    browseName="ns=rsl;<FrameIdentifier>",
    modellingRule="MandatoryPlaceholder",
    references=[o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=rsl;i=6021", browseName="ns=rsl;Base", dataType=o6.NodeId, accessLevel=3, userAccessLevel=1))],
    _allow_abstract=True,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.objtypes.FolderType(nodeId="ns=rsl;i=5004", browseName="ns=rsl;AlternativeFrames", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=rsl;i=6020"])])
o6.reference(rsl_objtypes.SpatialObjectType, ns0.reftypes.HasComponent, o6.ns["ns=rsl;i=5004"])
rsl_vartypes.SpatialLocationType(
    nodeId="ns=rsl;i=6022",
    browseName="ns=rsl;<FrameIdentifier>",
    modellingRule="MandatoryPlaceholder",
    references=[o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=rsl;i=6023", browseName="ns=rsl;Base", dataType=o6.NodeId, accessLevel=3, userAccessLevel=1))],
    _allow_abstract=True,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.objtypes.FolderType(nodeId="ns=rsl;i=5003", browseName="ns=rsl;InternalFrames", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=rsl;i=6022"])])
o6.reference(rsl_objtypes.SpatialObjectType, ns0.reftypes.HasComponent, o6.ns["ns=rsl;i=5003"])
rsl_vartypes.SpatialLocationType(
    nodeId="ns=rsl;i=6025",
    browseName="ns=rsl;WorldFrame",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=rsl;i=6026",
                browseName="ns=rsl;Base",
                description="WorldFrame as the origin of the coordinate system has no Base i.e. it must be null.",
                dataType=o6.NodeId,
                accessLevel=3,
                userAccessLevel=1,
            )
        )
    ],
    _allow_abstract=True,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(rsl_objtypes.SpatialObjectsListType, ns0.reftypes.HasComponent, o6.ns["ns=rsl;i=6025"])
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashRSLSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=rsl;i=5005",
    browseName="ns=rsl;http://opcfoundation.org/UA/RSL/",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=rsl;i=6028", browseName="IsNamespaceSubset", dataType=o6.Boolean)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=rsl;i=6029", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2023-01-12T00:00:00Z"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=rsl;i=6030", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/RSL/")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=rsl;i=6031", browseName="NamespaceVersion", dataType=o6.String, value="1.00.1")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=rsl;i=6032", browseName="StaticNodeIdTypes", dataType=ns0.datatypes.IdType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=rsl;i=6033", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=rsl;i=6034", browseName="StaticStringNodeIdPattern", dataType=o6.String)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
rsl_vartypes.SpatialLocationType(
    nodeId="ns=rsl;i=6038",
    browseName="ns=rsl;PositionFrame",
    references=[o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=rsl;i=6039", browseName="ns=rsl;Base", dataType=o6.NodeId, accessLevel=3, userAccessLevel=1))],
    _allow_abstract=True,
    accessLevel=3,
    userAccessLevel=1,
)
rsl_objtypes.SpatialObjectType(
    nodeId="ns=rsl;i=5006",
    browseName="ns=rsl;<SpatialObject>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=rsl;i=6035",
                browseName="DefaultInstanceBrowseName",
                description="The default BrowseName for instances of the type.",
                dataType=o6.QualifiedName,
                value=o6.QualifiedName("rsl:SpatialObject"),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=rsl;i=6038"]),
    ],
)
o6.reference(rsl_objtypes.SpatialObjectsListType, ns0.reftypes.Organizes, o6.ns["ns=rsl;i=5006"])
rsl_vartypes.RpyOrientationType(
    nodeId="ns=rsl;i=6006",
    browseName="ns=rsl;Orientation",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=rsl;i=6036", browseName="AngleUnit", dataType=ns0.datatypes.EUInformation)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=rsl;i=6042",
                browseName="ns=rsl;A",
                description="Rotation around X Axis (Roll) as per ISO 9787:2013",
                dataType=o6.Double,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=rsl;i=6043",
                browseName="ns=rsl;B",
                description="Rotation around Y Axis (Pitch) as per ISO 9787:2013",
                dataType=o6.Double,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=rsl;i=6044", browseName="ns=rsl;C", description="Rotation around Z Axis (Yaw) as per ISO 9787:2013", dataType=o6.Double, accessLevel=3, userAccessLevel=1
            )
        ),
    ],
    dataType=ns0.datatypes.ThreeDOrientation,
    value=ns0.datatypes.ThreeDOrientation(a=0.0, b=0.0, c=0.0),
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(rsl_vartypes.CartesianFrameAngleOrientationType, ns0.reftypes.HasComponent, o6.ns["ns=rsl;i=6006"])
ns0.vartypes.ThreeDCartesianCoordinatesType(
    nodeId="ns=rsl;i=6007",
    browseName="ns=rsl;Position",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=rsl;i=6045", browseName="LengthUnit", dataType=ns0.datatypes.EUInformation)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=rsl;i=6011", browseName="X", dataType=o6.Double)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=rsl;i=6012", browseName="Y", dataType=o6.Double)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=rsl;i=6013", browseName="Z", dataType=o6.Double)),
    ],
    dataType=ns0.datatypes.ThreeDCartesianCoordinates,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(rsl_vartypes.CartesianFrameAngleOrientationType, ns0.reftypes.HasComponent, o6.ns["ns=rsl;i=6007"])


del Any, TYPE_CHECKING, uuid, o6, ns0, rsl_vartypes, rsl_objtypes
