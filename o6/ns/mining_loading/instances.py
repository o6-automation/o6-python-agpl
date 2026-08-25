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

"""Generated OPC UA mining_loading namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.machinery as machinery
import o6.ns.mining as mining
import o6.ns.ns0 as ns0
from . import objtypes as mining_loading_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

httpColonSlashSlashOpcfoundationDotOrgSlashUASlashMiningSlashLoadingSlashGeneralSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=mining_loading;i=5001",
    browseName="ns=mining_loading;http://opcfoundation.org/UA/Mining/Loading/General/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mining_loading;i=6002", browseName="IsNamespaceSubset", dataType=o6.Boolean, value=False)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=mining_loading;i=6003", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2022-09-01T00:00:00Z"))
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=mining_loading;i=6004", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/Mining/Loading/General/")
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mining_loading;i=6005", browseName="NamespaceVersion", dataType=o6.String, value="1.0.0")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_loading;i=6006",
                browseName="StaticNodeIdTypes",
                dataType=ns0.datatypes.IdType,
                valueRank=1,
                arrayDimensions=[2],
                value=[ns0.datatypes.IdType.NUMERIC, ns0.datatypes.IdType.STRING],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_loading;i=6007", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mining_loading;i=6008", browseName="StaticStringNodeIdPattern", dataType=o6.String)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
ns0.vartypes._3DCartesianCoordinatesType(
    nodeId="ns=mining_loading;i=6009",
    browseName="CartesianCoordinates",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_loading;i=6010", browseName="X", dataType=o6.Double)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_loading;i=6011", browseName="Y", dataType=o6.Double)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_loading;i=6012", browseName="Z", dataType=o6.Double)),
    ],
    dataType=ns0.datatypes._3DCartesianCoordinates,
)
ns0.vartypes._3DOrientationType(
    nodeId="ns=mining_loading;i=6013",
    browseName="Orientation",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_loading;i=6014", browseName="A", dataType=o6.Double)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_loading;i=6015", browseName="B", dataType=o6.Double)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_loading;i=6016", browseName="C", dataType=o6.Double)),
    ],
    dataType=ns0.datatypes._3DOrientation,
)
ns0.vartypes._3DFrameType(
    nodeId="ns=mining_loading;i=6001",
    browseName="ns=mining_loading;ExclusionZone",
    description="The ExclusionZone property describes the area that haulage machines, which are to be loaded, are not allowed to enter when approaching the loading machine",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mining_loading;i=6019", browseName="Constant", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mining_loading;i=6020", browseName="FixedBase", dataType=o6.Boolean)),
        o6.hasComponent(o6.ns["ns=mining_loading;i=6009"]),
        o6.hasComponent(o6.ns["ns=mining_loading;i=6013"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_loading;i=6018", browseName="BaseFrame", dataType=o6.NodeId)),
    ],
    dataType=ns0.datatypes._3DFrame,
    valueRank=1,
    arrayDimensions=[0],
)
ns0.vartypes._3DCartesianCoordinatesType(
    nodeId="ns=mining_loading;i=6024",
    browseName="CartesianCoordinates",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_loading;i=6025", browseName="X", dataType=o6.Double)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_loading;i=6026", browseName="Y", dataType=o6.Double)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_loading;i=6027", browseName="Z", dataType=o6.Double)),
    ],
    dataType=ns0.datatypes._3DCartesianCoordinates,
)
ns0.vartypes._3DOrientationType(
    nodeId="ns=mining_loading;i=6028",
    browseName="Orientation",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_loading;i=6029", browseName="A", dataType=o6.Double)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_loading;i=6030", browseName="B", dataType=o6.Double)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_loading;i=6031", browseName="C", dataType=o6.Double)),
    ],
    dataType=ns0.datatypes._3DOrientation,
)
ns0.vartypes._3DFrameType(
    nodeId="ns=mining_loading;i=6023",
    browseName="ns=mining_loading;MachinePose",
    description="The MachinePose variable describes the pose of the loading machine in terms of location coordinates, orientation and (optional) base frame.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mining_loading;i=6033", browseName="Constant", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mining_loading;i=6034", browseName="FixedBase", dataType=o6.Boolean)),
        o6.hasComponent(o6.ns["ns=mining_loading;i=6024"]),
        o6.hasComponent(o6.ns["ns=mining_loading;i=6028"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_loading;i=6032", browseName="BaseFrame", dataType=o6.NodeId)),
    ],
    dataType=ns0.datatypes._3DFrame,
    value=ns0.datatypes._3DFrame(cartesianCoordinates=ns0.datatypes._3DCartesianCoordinates(x=0.0, y=0.0, z=0.0), orientation=ns0.datatypes._3DOrientation(a=0.0, b=0.0, c=0.0)),
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=mining_loading;i=5003",
    browseName="ns=di;ParameterSet",
    description="Flat list of Parameters",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=mining_loading;i=6001"]), o6.hasComponent(o6.ns["ns=mining_loading;i=6023"])],
)
o6.reference(mining_loading_objtypes.LoadingMachineType, ns0.reftypes.HasComponent, o6.ns["ns=mining_loading;i=5003"])


ns0.vartypes.PropertyType(
    nodeId="ns=mining_loading;i=6021",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=mining_loading;i=7001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="LoadingStartAcknowledged",
            dataType=o6.Boolean,
            valueRank=-1,
            description=o6.LocalizedText("The LoadingStartAcknowledged variable indicates whether the loading request was successful or not", "en"),
        )
    ],
)
o6.call(
    nodeId="ns=mining_loading;i=7001",
    browseName="ns=mining_loading;RequestForLoading",
    description="The RequestForLoading method is called by a partnering machine when they want to start the loading procedure.",
    outputArgs=o6.hasProperty(o6.ns["ns=mining_loading;i=6021"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=mining_loading;i=6022",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=mining_loading;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="LoadingStopAcknowledged",
            dataType=o6.Boolean,
            valueRank=-1,
            description=o6.LocalizedText("The LoadingStartAcknowledged variable indicates whether the loading request was successful or not", "en"),
        )
    ],
)
o6.call(
    nodeId="ns=mining_loading;i=7002",
    browseName="ns=mining_loading;StopLoading",
    description="The StopLoading method is called by a partnering machine when they want to abort the loading procedure",
    outputArgs=o6.hasProperty(o6.ns["ns=mining_loading;i=6022"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=mining_loading;i=6035",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=mining_loading;i=7003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="PositioningCompleteResult",
            dataType=o6.Boolean,
            valueRank=-1,
            description=o6.LocalizedText("The PositioningComplete method is called by a partnering machine when they have completed the positioning procedure.", "en"),
        )
    ],
)
o6.call(
    nodeId="ns=mining_loading;i=7003",
    browseName="ns=mining_loading;PositioningComplete",
    description="The PositioningComplete method is called by a partnering machine when they have finished to position themselves in front of the loading machine",
    outputArgs=o6.hasProperty(o6.ns["ns=mining_loading;i=6035"]),
)

ns0.objtypes.BaseObjectType(
    nodeId="ns=mining_loading;i=5002",
    browseName="ns=di;MethodSet",
    description="Flat list of Methods",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=mining_loading;i=7001"]), o6.hasComponent(o6.ns["ns=mining_loading;i=7002"]), o6.hasComponent(o6.ns["ns=mining_loading;i=7003"])],
)
o6.reference(mining_loading_objtypes.LoadingMachineType, ns0.reftypes.HasComponent, o6.ns["ns=mining_loading;i=5002"])


del Any, TYPE_CHECKING, uuid, o6, di, ia, machinery, mining, ns0, mining_loading_objtypes
