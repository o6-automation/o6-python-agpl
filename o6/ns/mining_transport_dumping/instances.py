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

"""Generated OPC UA mining_transport_dumping namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.machinery as machinery
import o6.ns.mining as mining
import o6.ns.ns0 as ns0
from . import objtypes as mining_transport_dumping_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

httpColonSlashSlashOpcfoundationDotOrgSlashUASlashMiningSlashTransportDumpingSlashGeneralSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=mining_transport_dumping;i=5001",
    browseName="ns=mining_transport_dumping;http://opcfoundation.org/UA/Mining/TransportDumping/General/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mining_transport_dumping;i=6002", browseName="IsNamespaceSubset", dataType=o6.Boolean, value=False)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_transport_dumping;i=6003", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2022-09-01T00:00:00Z")
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_transport_dumping;i=6004", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/Mining/TransportDumping/General/"
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mining_transport_dumping;i=6005", browseName="NamespaceVersion", dataType=o6.String, value="1.0.0")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_transport_dumping;i=6006",
                browseName="StaticNodeIdTypes",
                dataType=ns0.datatypes.IdType,
                valueRank=1,
                arrayDimensions=[2],
                value=[ns0.datatypes.IdType.NUMERIC, ns0.datatypes.IdType.STRING],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_transport_dumping;i=6007", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mining_transport_dumping;i=6008", browseName="StaticStringNodeIdPattern", dataType=o6.String)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
ns0.vartypes.AnalogUnitRangeType(
    nodeId="ns=mining_transport_dumping;i=6001",
    browseName="ns=mining_transport_dumping;CurrentPayload",
    description="The CurrentPayload variable describes the current payload of the hauling machine.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_transport_dumping;i=6009",
                browseName="EngineeringUnits",
                description="This is the EngineeringUnit of the current payload.",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5525061,
                    displayName=o6.LocalizedText("t", "en"),
                    description=o6.LocalizedText("tonne (metric ton)", "en"),
                ),
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_transport_dumping;i=6010",
                browseName="EURange",
                description="This is the EURange of the current payload.",
                dataType=ns0.datatypes.Range,
                value=ns0.datatypes.Range(low=0.0, high=200.0),
            )
        ),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitRangeType(
    nodeId="ns=mining_transport_dumping;i=6011",
    browseName="ns=mining_transport_dumping;PayloadCapacity",
    description="The PayloadCapacity variable describes the payload capacity of the hauling machine.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_transport_dumping;i=6012",
                browseName="EngineeringUnits",
                description="This is the EngineeringUnit of the payload capacity.",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5525061,
                    displayName=o6.LocalizedText("t", "en"),
                    description=o6.LocalizedText("tonne (metric ton)", "en"),
                ),
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_transport_dumping;i=6013",
                browseName="EURange",
                description="This is the EURange of the payload capacity.",
                dataType=ns0.datatypes.Range,
                value=ns0.datatypes.Range(low=0.0, high=200.0),
            )
        ),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=mining_transport_dumping;i=6019",
    browseName="ns=mining;Speed",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_transport_dumping;i=6020",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5067859,
                    displayName=o6.LocalizedText("m/s", "en"),
                    description=o6.LocalizedText("metre per second", "en"),
                ),
            )
        )
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes._3DCartesianCoordinatesType(
    nodeId="ns=mining_transport_dumping;i=6024",
    browseName="CartesianCoordinates",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_transport_dumping;i=6025", browseName="X", dataType=o6.Double)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_transport_dumping;i=6026", browseName="Y", dataType=o6.Double)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_transport_dumping;i=6027", browseName="Z", dataType=o6.Double)),
    ],
    dataType=ns0.datatypes._3DCartesianCoordinates,
)
ns0.vartypes._3DOrientationType(
    nodeId="ns=mining_transport_dumping;i=6028",
    browseName="Orientation",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_transport_dumping;i=6029", browseName="A", dataType=o6.Double)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_transport_dumping;i=6030", browseName="B", dataType=o6.Double)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_transport_dumping;i=6031", browseName="C", dataType=o6.Double)),
    ],
    dataType=ns0.datatypes._3DOrientation,
)
ns0.vartypes._3DCartesianCoordinatesType(
    nodeId="ns=mining_transport_dumping;i=6032",
    browseName="CartesianCoordinates",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_transport_dumping;i=6033", browseName="X", dataType=o6.Double)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_transport_dumping;i=6034", browseName="Y", dataType=o6.Double)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_transport_dumping;i=6035", browseName="Z", dataType=o6.Double)),
    ],
    dataType=ns0.datatypes._3DCartesianCoordinates,
)
ns0.vartypes._3DOrientationType(
    nodeId="ns=mining_transport_dumping;i=6036",
    browseName="Orientation",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_transport_dumping;i=6037", browseName="A", dataType=o6.Double)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_transport_dumping;i=6038", browseName="B", dataType=o6.Double)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_transport_dumping;i=6039", browseName="C", dataType=o6.Double)),
    ],
    dataType=ns0.datatypes._3DOrientation,
)
ns0.vartypes._3DFrameType(
    nodeId="ns=mining_transport_dumping;i=6022",
    browseName="ns=mining_transport_dumping;TailHeight",
    description="The TailHeight variable measures the tail height of the hauling machine.",
    references=[o6.hasComponent(o6.ns["ns=mining_transport_dumping;i=6032"]), o6.hasComponent(o6.ns["ns=mining_transport_dumping;i=6036"])],
    dataType=ns0.datatypes._3DFrame,
    value=ns0.datatypes._3DFrame(cartesianCoordinates=ns0.datatypes._3DCartesianCoordinates(x=0.0, y=0.0, z=0.0), orientation=ns0.datatypes._3DOrientation(a=0.0, b=0.0, c=0.0)),
)
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=mining_transport_dumping;i=6018",
    browseName="ns=mining_transport_dumping;MachineVelocity",
    description="The MachineVelocity variable describes the hauling machine’s velocity in terms of magnitude and direction.",
    references=[
        o6.hasComponent(o6.ns["ns=mining_transport_dumping;i=6019"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_transport_dumping;i=6021", browseName="X", dataType=o6.Double)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_transport_dumping;i=6040", browseName="Y", dataType=o6.Double)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_transport_dumping;i=6041", browseName="Z", dataType=o6.Double)),
    ],
    dataType=ns0.datatypes._3DVector,
    value=ns0.datatypes._3DVector(x=0.0, y=0.0, z=0.0),
)
ns0.vartypes.AnalogUnitRangeType(
    nodeId="ns=mining_transport_dumping;i=6042",
    browseName="ns=mining_transport_dumping;AsymmetryLoad",
    description="The AsymmetryLoad variable describes the asymmetry of the load on the truck-bed.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_transport_dumping;i=6043",
                browseName="EngineeringUnits",
                description="This is the EngineeringUnit of the asymmetric load indicator.",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20529, displayName=o6.LocalizedText("%"), description=o6.LocalizedText("percent")
                ),
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_transport_dumping;i=6044",
                browseName="EURange",
                description="This is the EURange of the asymmetric load indicator.",
                dataType=ns0.datatypes.Range,
                value=ns0.datatypes.Range(low=0.0, high=100.0),
            )
        ),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes._3DCartesianCoordinatesType(
    nodeId="ns=mining_transport_dumping;i=6014",
    browseName="ns=mining_transport_dumping;MachineShape",
    description="The MachineShape variable describes the hauling machine’s shape in terms of width, height and length. As this variable is an array, it can contain multiple shapes such as a shape for the truck-bed or for the cabin.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_transport_dumping;i=6046",
                browseName="LengthUnit",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5067858,
                    displayName=o6.LocalizedText("m", "en"),
                    description=o6.LocalizedText("metre", "en"),
                ),
            )
        ),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_transport_dumping;i=6015", browseName="X", dataType=o6.Double)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_transport_dumping;i=6016", browseName="Y", dataType=o6.Double)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_transport_dumping;i=6017", browseName="Z", dataType=o6.Double)),
    ],
    dataType=ns0.datatypes._3DCartesianCoordinates,
    valueRank=1,
    arrayDimensions=[0],
)
ns0.vartypes._3DFrameType(
    nodeId="ns=mining_transport_dumping;i=6023",
    browseName="ns=mining_transport_dumping;MachinePose",
    description="The MachinePose variable describes the pose of the hauling machine in terms of location coordinates, orientation and (optional) base frame.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mining_transport_dumping;i=6060", browseName="Constant", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mining_transport_dumping;i=6061", browseName="FixedBase", dataType=o6.Boolean)),
        o6.hasComponent(o6.ns["ns=mining_transport_dumping;i=6024"]),
        o6.hasComponent(o6.ns["ns=mining_transport_dumping;i=6028"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_transport_dumping;i=6059", browseName="BaseFrame", dataType=o6.NodeId)),
    ],
    dataType=ns0.datatypes._3DFrame,
    value=ns0.datatypes._3DFrame(cartesianCoordinates=ns0.datatypes._3DCartesianCoordinates(x=0.0, y=0.0, z=0.0), orientation=ns0.datatypes._3DOrientation(a=0.0, b=0.0, c=0.0)),
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=mining_transport_dumping;i=5003",
    browseName="ns=di;ParameterSet",
    description="Flat list of Parameters",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=mining_transport_dumping;i=6001"]),
        o6.hasComponent(o6.ns["ns=mining_transport_dumping;i=6011"]),
        o6.hasComponent(o6.ns["ns=mining_transport_dumping;i=6014"]),
        o6.hasComponent(o6.ns["ns=mining_transport_dumping;i=6018"]),
        o6.hasComponent(o6.ns["ns=mining_transport_dumping;i=6022"]),
        o6.hasComponent(o6.ns["ns=mining_transport_dumping;i=6023"]),
        o6.hasComponent(o6.ns["ns=mining_transport_dumping;i=6042"]),
    ],
)
o6.reference(mining_transport_dumping_objtypes.HaulageMachineType, ns0.reftypes.HasComponent, o6.ns["ns=mining_transport_dumping;i=5003"])


ns0.vartypes.PropertyType(
    nodeId="ns=mining_transport_dumping;i=6047",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=mining_transport_dumping;i=7001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="LoadingCompleteAcknowledged", dataType=o6.Boolean, valueRank=-1)],
)
o6.call(
    nodeId="ns=mining_transport_dumping;i=7001",
    browseName="ns=mining_transport_dumping;LoadingComplete",
    description="The LoadingComplete method call indicates the completion of the loading process.",
    outputArgs=o6.hasProperty(o6.ns["ns=mining_transport_dumping;i=6047"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=mining_transport_dumping;i=6048",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=mining_transport_dumping;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="PositioningStartAcknowledged", dataType=o6.Boolean, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=mining_transport_dumping;i=6058",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=mining_transport_dumping;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="TargetPose",
            dataType=ns0.datatypes._3DFrame,
            valueRank=-1,
            description=o6.LocalizedText(
                "The TargetPose property describe the coordinates and orientation a haulage machine should navigate to in order to position itself for loading", "en"
            ),
        )
    ],
)
o6.call(
    nodeId="ns=mining_transport_dumping;i=7002",
    browseName="ns=mining_transport_dumping;StartPositioning",
    description="The StartPositioning method call indicates the start of the positioning process.",
    inputArgs=o6.hasProperty(o6.ns["ns=mining_transport_dumping;i=6058"]),
    outputArgs=o6.hasProperty(o6.ns["ns=mining_transport_dumping;i=6048"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=mining_transport_dumping;i=6052",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=mining_transport_dumping;i=7003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="SetPriorityAcknowledged", dataType=o6.Boolean, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=mining_transport_dumping;i=6053",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=mining_transport_dumping;i=7003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="QueuePriority",
            dataType=o6.Boolean,
            valueRank=-1,
            description=o6.LocalizedText("The QueuePriority property describes the priority position of the of a haulage machine during a load cycle", "en"),
        )
    ],
)
o6.call(
    nodeId="ns=mining_transport_dumping;i=7003",
    browseName="ns=mining_transport_dumping;SetQueuePriority",
    description="The SetQueuePriority method call sets the queue priority of the hauling machine.",
    inputArgs=o6.hasProperty(o6.ns["ns=mining_transport_dumping;i=6053"]),
    outputArgs=o6.hasProperty(o6.ns["ns=mining_transport_dumping;i=6052"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=mining_transport_dumping;i=6049",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=mining_transport_dumping;i=7004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="UnloadingStartAcknowledged", dataType=o6.Boolean, valueRank=-1)],
)
o6.call(
    nodeId="ns=mining_transport_dumping;i=7004",
    browseName="ns=mining_transport_dumping;StartUnloading",
    description="The StartUnloading method call indicates the start of the unloading process.",
    outputArgs=o6.hasProperty(o6.ns["ns=mining_transport_dumping;i=6049"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=mining_transport_dumping;i=6051",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=mining_transport_dumping;i=7005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="UnloadingStopAcknowledged", dataType=o6.Boolean, valueRank=-1)],
)
o6.call(
    nodeId="ns=mining_transport_dumping;i=7005",
    browseName="ns=mining_transport_dumping;StopUnloading",
    description="The StopUnloading method call indicates the end of the unloading process.",
    outputArgs=o6.hasProperty(o6.ns["ns=mining_transport_dumping;i=6051"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=mining_transport_dumping;i=6054",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=mining_transport_dumping;i=7006",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="QueuePriority", dataType=o6.UInt16, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=mining_transport_dumping;i=6055",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=mining_transport_dumping;i=7006",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="JoinQueueAcknowledged", dataType=o6.Boolean, valueRank=-1)],
)
o6.call(
    nodeId="ns=mining_transport_dumping;i=7006",
    browseName="ns=mining_transport_dumping;JoinQueue",
    description="The JoinQueue method call indicates the joining of the waiting/spotting queue of the hauling machine.",
    inputArgs=o6.hasProperty(o6.ns["ns=mining_transport_dumping;i=6054"]),
    outputArgs=o6.hasProperty(o6.ns["ns=mining_transport_dumping;i=6055"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=mining_transport_dumping;i=6056",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=mining_transport_dumping;i=7007",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ClearSpotAcknowledged", dataType=o6.Boolean, valueRank=-1)],
)
o6.call(
    nodeId="ns=mining_transport_dumping;i=7007",
    browseName="ns=mining_transport_dumping;ClearSpot",
    description="The ClearSpot method call indicates the clearing of the spot within the queue.",
    outputArgs=o6.hasProperty(o6.ns["ns=mining_transport_dumping;i=6056"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=mining_transport_dumping;i=6050",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=mining_transport_dumping;i=7008",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="PositioningStopAcknowledged", dataType=o6.Boolean, valueRank=-1)],
)
o6.call(
    nodeId="ns=mining_transport_dumping;i=7008",
    browseName="ns=mining_transport_dumping;StopPositioning",
    description="The StopPositioning method call indicates the end of the positioning process.",
    outputArgs=o6.hasProperty(o6.ns["ns=mining_transport_dumping;i=6050"]),
)

ns0.objtypes.BaseObjectType(
    nodeId="ns=mining_transport_dumping;i=5002",
    browseName="ns=di;MethodSet",
    description="Flat list of Methods",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=mining_transport_dumping;i=7001"]),
        o6.hasComponent(o6.ns["ns=mining_transport_dumping;i=7002"]),
        o6.hasComponent(o6.ns["ns=mining_transport_dumping;i=7003"]),
        o6.hasComponent(o6.ns["ns=mining_transport_dumping;i=7004"]),
        o6.hasComponent(o6.ns["ns=mining_transport_dumping;i=7005"]),
        o6.hasComponent(o6.ns["ns=mining_transport_dumping;i=7006"]),
        o6.hasComponent(o6.ns["ns=mining_transport_dumping;i=7007"]),
        o6.hasComponent(o6.ns["ns=mining_transport_dumping;i=7008"]),
    ],
)
o6.reference(mining_transport_dumping_objtypes.HaulageMachineType, ns0.reftypes.HasComponent, o6.ns["ns=mining_transport_dumping;i=5002"])


del Any, TYPE_CHECKING, uuid, o6, di, ia, machinery, mining, ns0, mining_transport_dumping_objtypes
