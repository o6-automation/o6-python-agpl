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

"""Generated OPC UA mining_rear_dump_truck namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.machinery as machinery
import o6.ns.mining as mining
import o6.ns.mining_transport_dumping as mining_transport_dumping
import o6.ns.ns0 as ns0
from . import objtypes as mining_rear_dump_truck_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

httpColonSlashSlashOpcfoundationDotOrgSlashUASlashMiningSlashTransportDumpingSlashRearDumpTruckSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=mining_rear_dump_truck;i=5001",
    browseName="ns=mining_rear_dump_truck;http://opcfoundation.org/UA/Mining/TransportDumping/RearDumpTruck/",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=mining_rear_dump_truck;i=6001", browseName="IsNamespaceSubset", dataType=o6.Boolean)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_rear_dump_truck;i=6002", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2022-09-01T00:00:00Z")
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_rear_dump_truck;i=6003", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/Mining/TransportDumping/RearDumpTruck/"
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mining_rear_dump_truck;i=6004", browseName="NamespaceVersion", dataType=o6.String, value="1.0.0")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_rear_dump_truck;i=6005",
                browseName="StaticNodeIdTypes",
                dataType=ns0.datatypes.IdType,
                valueRank=1,
                arrayDimensions=[2],
                value=[ns0.datatypes.IdType.NUMERIC, ns0.datatypes.IdType.STRING],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_rear_dump_truck;i=6006", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mining_rear_dump_truck;i=6007", browseName="StaticStringNodeIdPattern", dataType=o6.String)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
ns0.vartypes.AnalogUnitRangeType(
    nodeId="ns=mining_rear_dump_truck;i=6025",
    browseName="ns=mining_transport_dumping;AsymmetryLoad",
    description="The AsymmetryLoad variable describes the asymmetry of the load on the truck-bed.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_rear_dump_truck;i=6026",
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
                nodeId="ns=mining_rear_dump_truck;i=6027",
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
ns0.vartypes.AnalogUnitRangeType(
    nodeId="ns=mining_rear_dump_truck;i=6028",
    browseName="ns=mining_transport_dumping;CurrentPayload",
    description="The CurrentPayload variable describes the current payload of the hauling machine.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_rear_dump_truck;i=6029",
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
                nodeId="ns=mining_rear_dump_truck;i=6030",
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
ns0.vartypes.ThreeDCartesianCoordinatesType(
    nodeId="ns=mining_rear_dump_truck;i=6032",
    browseName="CartesianCoordinates",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_rear_dump_truck;i=6033", browseName="X", dataType=o6.Double)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_rear_dump_truck;i=6034", browseName="Y", dataType=o6.Double)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_rear_dump_truck;i=6035", browseName="Z", dataType=o6.Double)),
    ],
    dataType=ns0.datatypes.ThreeDCartesianCoordinates,
)
ns0.vartypes.ThreeDOrientationType(
    nodeId="ns=mining_rear_dump_truck;i=6036",
    browseName="Orientation",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_rear_dump_truck;i=6037", browseName="A", dataType=o6.Double)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_rear_dump_truck;i=6038", browseName="B", dataType=o6.Double)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_rear_dump_truck;i=6039", browseName="C", dataType=o6.Double)),
    ],
    dataType=ns0.datatypes.ThreeDOrientation,
)
ns0.vartypes.ThreeDCartesianCoordinatesType(
    nodeId="ns=mining_rear_dump_truck;i=6040",
    browseName="ns=mining_transport_dumping;MachineShape",
    description="The MachineShape variable describes the hauling machine’s shape in terms of width, height and length. As this variable is an array, it can contain multiple shapes such as a shape for the truck-bed or for the cabin.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_rear_dump_truck;i=6041",
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
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_rear_dump_truck;i=6042", browseName="X", dataType=o6.Double)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_rear_dump_truck;i=6043", browseName="Y", dataType=o6.Double)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_rear_dump_truck;i=6044", browseName="Z", dataType=o6.Double)),
    ],
    dataType=ns0.datatypes.ThreeDCartesianCoordinates,
    valueRank=1,
    arrayDimensions=[0],
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=mining_rear_dump_truck;i=6046",
    browseName="ns=mining;Speed",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_rear_dump_truck;i=6047",
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
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=mining_rear_dump_truck;i=6045",
    browseName="ns=mining_transport_dumping;MachineVelocity",
    description="The MachineVelocity variable describes the hauling machine’s velocity in terms of magnitude and direction.",
    references=[
        o6.hasComponent(o6.ns["ns=mining_rear_dump_truck;i=6046"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_rear_dump_truck;i=6048", browseName="X", dataType=o6.Double)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_rear_dump_truck;i=6049", browseName="Y", dataType=o6.Double)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_rear_dump_truck;i=6050", browseName="Z", dataType=o6.Double)),
    ],
    dataType=ns0.datatypes.ThreeDVector,
    value=ns0.datatypes.ThreeDVector(x=0.0, y=0.0, z=0.0),
)
ns0.vartypes.AnalogUnitRangeType(
    nodeId="ns=mining_rear_dump_truck;i=6051",
    browseName="ns=mining_transport_dumping;PayloadCapacity",
    description="The PayloadCapacity variable describes the payload capacity of the hauling machine.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_rear_dump_truck;i=6052",
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
                nodeId="ns=mining_rear_dump_truck;i=6053",
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
ns0.vartypes.ThreeDCartesianCoordinatesType(
    nodeId="ns=mining_rear_dump_truck;i=6055",
    browseName="CartesianCoordinates",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_rear_dump_truck;i=6056", browseName="X", dataType=o6.Double)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_rear_dump_truck;i=6057", browseName="Y", dataType=o6.Double)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_rear_dump_truck;i=6058", browseName="Z", dataType=o6.Double)),
    ],
    dataType=ns0.datatypes.ThreeDCartesianCoordinates,
)
ns0.vartypes.ThreeDOrientationType(
    nodeId="ns=mining_rear_dump_truck;i=6059",
    browseName="Orientation",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_rear_dump_truck;i=6060", browseName="A", dataType=o6.Double)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_rear_dump_truck;i=6061", browseName="B", dataType=o6.Double)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_rear_dump_truck;i=6062", browseName="C", dataType=o6.Double)),
    ],
    dataType=ns0.datatypes.ThreeDOrientation,
)
ns0.vartypes.ThreeDFrameType(
    nodeId="ns=mining_rear_dump_truck;i=6054",
    browseName="ns=mining_transport_dumping;TailHeight",
    description="The TailHeight variable measures the tail height of the hauling machine.",
    references=[o6.hasComponent(o6.ns["ns=mining_rear_dump_truck;i=6055"]), o6.hasComponent(o6.ns["ns=mining_rear_dump_truck;i=6059"])],
    dataType=ns0.datatypes.ThreeDFrame,
    value=ns0.datatypes.ThreeDFrame(
        cartesianCoordinates=ns0.datatypes.ThreeDCartesianCoordinates(x=0.0, y=0.0, z=0.0), orientation=ns0.datatypes.ThreeDOrientation(a=0.0, b=0.0, c=0.0)
    ),
)
ns0.vartypes.ThreeDFrameType(
    nodeId="ns=mining_rear_dump_truck;i=6031",
    browseName="ns=mining_transport_dumping;MachinePose",
    description="The MachinePose variable describes the pose of the hauling machine in terms of location coordinates, orientation and (optional) base frame.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mining_rear_dump_truck;i=6064", browseName="Constant", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mining_rear_dump_truck;i=6065", browseName="FixedBase", dataType=o6.Boolean)),
        o6.hasComponent(o6.ns["ns=mining_rear_dump_truck;i=6032"]),
        o6.hasComponent(o6.ns["ns=mining_rear_dump_truck;i=6036"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_rear_dump_truck;i=6063", browseName="BaseFrame", dataType=o6.NodeId)),
    ],
    dataType=ns0.datatypes.ThreeDFrame,
    value=ns0.datatypes.ThreeDFrame(
        cartesianCoordinates=ns0.datatypes.ThreeDCartesianCoordinates(x=0.0, y=0.0, z=0.0), orientation=ns0.datatypes.ThreeDOrientation(a=0.0, b=0.0, c=0.0)
    ),
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=mining_rear_dump_truck;i=5005",
    browseName="ns=di;ParameterSet",
    description="Flat list of Parameters",
    references=[
        o6.hasComponent(o6.ns["ns=mining_rear_dump_truck;i=6025"]),
        o6.hasComponent(o6.ns["ns=mining_rear_dump_truck;i=6028"]),
        o6.hasComponent(o6.ns["ns=mining_rear_dump_truck;i=6031"]),
        o6.hasComponent(o6.ns["ns=mining_rear_dump_truck;i=6040"]),
        o6.hasComponent(o6.ns["ns=mining_rear_dump_truck;i=6045"]),
        o6.hasComponent(o6.ns["ns=mining_rear_dump_truck;i=6051"]),
        o6.hasComponent(o6.ns["ns=mining_rear_dump_truck;i=6054"]),
    ],
)
mining.objtypes.MiningEquipmentIdentificationType(
    nodeId="ns=mining_rear_dump_truck;i=5002",
    browseName="ns=mining;MiningEquipmentIdentification",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_rear_dump_truck;i=6008",
                browseName="ns=di;DeviceClass",
                description="Indicates in which domain or for what purpose the MachineryItem is used.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_rear_dump_truck;i=6009",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_rear_dump_truck;i=6010",
                browseName="ns=di;ManufacturerUri",
                description="A globally unique identifier of the manufacturer of the MachineryItem.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_rear_dump_truck;i=6011",
                browseName="ns=di;Model",
                description="A human-readable, localized name of the model of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_rear_dump_truck;i=6012",
                browseName="ns=di;ProductInstanceUri",
                description="A globally unique resource identifier provided by the manufacturer of the machine",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_rear_dump_truck;i=6013",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_rear_dump_truck;i=6068",
                browseName="ns=di;AssetId",
                description="To be used by end users to store a unique identification in the context of their overall application. Servers shall support at least 40 Unicode characters for the clients writing this value, this means clients can expect to be able to write strings with a length of 40 Unicode characters into that field.",
                dataType=o6.String,
                value="",
            )
        ),
    ],
)
o6.reference(mining_rear_dump_truck_objtypes.RearDumpTruckType, ns0.reftypes.HasAddIn, o6.ns["ns=mining_rear_dump_truck;i=5002"])


ns0.vartypes.PropertyType(
    nodeId="ns=mining_rear_dump_truck;i=6014",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=mining_rear_dump_truck;i=7001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ClearSpotAcknowledged", dataType=o6.Boolean, valueRank=-1)],
)
o6.call(
    nodeId="ns=mining_rear_dump_truck;i=7001",
    browseName="ns=mining_transport_dumping;ClearSpot",
    description="The ClearSpot method call indicates the clearing of the spot within the queue.",
    outputArgs=o6.hasProperty(o6.ns["ns=mining_rear_dump_truck;i=6014"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=mining_rear_dump_truck;i=6015",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=mining_rear_dump_truck;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="QueuePriority", dataType=o6.UInt16, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=mining_rear_dump_truck;i=6016",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=mining_rear_dump_truck;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="JoinQueueAcknowledged", dataType=o6.Boolean, valueRank=-1)],
)
o6.call(
    nodeId="ns=mining_rear_dump_truck;i=7002",
    browseName="ns=mining_transport_dumping;JoinQueue",
    description="The JoinQueue method call indicates the joining of the waiting/spotting queue of the hauling machine.",
    inputArgs=o6.hasProperty(o6.ns["ns=mining_rear_dump_truck;i=6015"]),
    outputArgs=o6.hasProperty(o6.ns["ns=mining_rear_dump_truck;i=6016"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=mining_rear_dump_truck;i=6017",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=mining_rear_dump_truck;i=7003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="LoadingCompleteAcknowledged", dataType=o6.Boolean, valueRank=-1)],
)
o6.call(
    nodeId="ns=mining_rear_dump_truck;i=7003",
    browseName="ns=mining_transport_dumping;LoadingComplete",
    description="The LoadingComplete method call indicates the completion of the loading process.",
    outputArgs=o6.hasProperty(o6.ns["ns=mining_rear_dump_truck;i=6017"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=mining_rear_dump_truck;i=6018",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=mining_rear_dump_truck;i=7004",
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
ns0.vartypes.PropertyType(
    nodeId="ns=mining_rear_dump_truck;i=6019",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=mining_rear_dump_truck;i=7004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="SetPriorityAcknowledged", dataType=o6.Boolean, valueRank=-1)],
)
o6.call(
    nodeId="ns=mining_rear_dump_truck;i=7004",
    browseName="ns=mining_transport_dumping;SetQueuePriority",
    description="The SetQueuePriority method call sets the queue priority of the hauling machine.",
    inputArgs=o6.hasProperty(o6.ns["ns=mining_rear_dump_truck;i=6018"]),
    outputArgs=o6.hasProperty(o6.ns["ns=mining_rear_dump_truck;i=6019"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=mining_rear_dump_truck;i=6020",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=mining_rear_dump_truck;i=7005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="TargetPose",
            dataType=ns0.datatypes.ThreeDFrame,
            valueRank=-1,
            description=o6.LocalizedText(
                "The TargetPose property describe the coordinates and orientation a haulage machine should navigate to in order to position itself for loading", "en"
            ),
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=mining_rear_dump_truck;i=6021",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=mining_rear_dump_truck;i=7005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="PositioningStartAcknowledged", dataType=o6.Boolean, valueRank=-1)],
)
o6.call(
    nodeId="ns=mining_rear_dump_truck;i=7005",
    browseName="ns=mining_transport_dumping;StartPositioning",
    description="The StartPositioning method call indicates the start of the positioning process.",
    inputArgs=o6.hasProperty(o6.ns["ns=mining_rear_dump_truck;i=6020"]),
    outputArgs=o6.hasProperty(o6.ns["ns=mining_rear_dump_truck;i=6021"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=mining_rear_dump_truck;i=6022",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=mining_rear_dump_truck;i=7006",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="UnloadingStartAcknowledged", dataType=o6.Boolean, valueRank=-1)],
)
o6.call(
    nodeId="ns=mining_rear_dump_truck;i=7006",
    browseName="ns=mining_transport_dumping;StartUnloading",
    description="The StartUnloading method call indicates the start of the unloading process.",
    outputArgs=o6.hasProperty(o6.ns["ns=mining_rear_dump_truck;i=6022"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=mining_rear_dump_truck;i=6023",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=mining_rear_dump_truck;i=7007",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="PositioningStopAcknowledged", dataType=o6.Boolean, valueRank=-1)],
)
o6.call(
    nodeId="ns=mining_rear_dump_truck;i=7007",
    browseName="ns=mining_transport_dumping;StopPositioning",
    description="The StopPositioning method call indicates the end of the positioning process.",
    outputArgs=o6.hasProperty(o6.ns["ns=mining_rear_dump_truck;i=6023"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=mining_rear_dump_truck;i=6024",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=mining_rear_dump_truck;i=7008",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="UnloadingStopAcknowledged", dataType=o6.Boolean, valueRank=-1)],
)
o6.call(
    nodeId="ns=mining_rear_dump_truck;i=7008",
    browseName="ns=mining_transport_dumping;StopUnloading",
    description="The StopUnloading method call indicates the end of the unloading process.",
    outputArgs=o6.hasProperty(o6.ns["ns=mining_rear_dump_truck;i=6024"]),
)

ns0.objtypes.BaseObjectType(
    nodeId="ns=mining_rear_dump_truck;i=5004",
    browseName="ns=di;MethodSet",
    description="Flat list of Methods",
    references=[
        o6.hasComponent(o6.ns["ns=mining_rear_dump_truck;i=7001"]),
        o6.hasComponent(o6.ns["ns=mining_rear_dump_truck;i=7002"]),
        o6.hasComponent(o6.ns["ns=mining_rear_dump_truck;i=7003"]),
        o6.hasComponent(o6.ns["ns=mining_rear_dump_truck;i=7004"]),
        o6.hasComponent(o6.ns["ns=mining_rear_dump_truck;i=7005"]),
        o6.hasComponent(o6.ns["ns=mining_rear_dump_truck;i=7006"]),
        o6.hasComponent(o6.ns["ns=mining_rear_dump_truck;i=7007"]),
        o6.hasComponent(o6.ns["ns=mining_rear_dump_truck;i=7008"]),
    ],
)
mining_transport_dumping.objtypes.HaulageMachineType(
    nodeId="ns=mining_rear_dump_truck;i=5003",
    browseName="ns=mining_rear_dump_truck;HaulageMachine",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=mining_rear_dump_truck;i=5004"]), o6.hasComponent(o6.ns["ns=mining_rear_dump_truck;i=5005"])],
)
o6.reference(mining_rear_dump_truck_objtypes.RearDumpTruckType, ns0.reftypes.HasAddIn, o6.ns["ns=mining_rear_dump_truck;i=5003"])


del Any, TYPE_CHECKING, uuid, o6, di, ia, machinery, mining, mining_transport_dumping, ns0, mining_rear_dump_truck_objtypes
