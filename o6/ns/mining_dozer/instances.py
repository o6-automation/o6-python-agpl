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

"""Generated OPC UA mining_dozer namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.machinery as machinery
import o6.ns.mining as mining
import o6.ns.ns0 as ns0
from . import datatypes as mining_dozer_datypes
from . import objtypes as mining_dozer_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.vartypes._3DCartesianCoordinatesType(
    nodeId="ns=mining_dozer;i=6014",
    browseName="CartesianCoordinates",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_dozer;i=6015", browseName="X", dataType=o6.Double)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_dozer;i=6016", browseName="Y", dataType=o6.Double)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_dozer;i=6017", browseName="Z", dataType=o6.Double)),
    ],
    dataType=ns0.datatypes._3DCartesianCoordinates,
)
ns0.vartypes._3DOrientationType(
    nodeId="ns=mining_dozer;i=6018",
    browseName="Orientation",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_dozer;i=6019", browseName="A", dataType=o6.Double)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_dozer;i=6020", browseName="B", dataType=o6.Double)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_dozer;i=6021", browseName="C", dataType=o6.Double)),
    ],
    dataType=ns0.datatypes._3DOrientation,
)
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashMiningSlashDevelopmentSupportSlashDozerSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=mining_dozer;i=5004",
    browseName="ns=mining_dozer;http://opcfoundation.org/UA/Mining/DevelopmentSupport/Dozer/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mining_dozer;i=6022", browseName="IsNamespaceSubset", dataType=o6.Boolean, value=False)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=mining_dozer;i=6023", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2022-09-01T00:00:00Z"))
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_dozer;i=6024", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/Mining/DevelopmentSupport/Dozer/"
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mining_dozer;i=6025", browseName="NamespaceVersion", dataType=o6.String, value="1.0.0")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_dozer;i=6026",
                browseName="StaticNodeIdTypes",
                dataType=ns0.datatypes.IdType,
                valueRank=1,
                arrayDimensions=[2],
                value=[ns0.datatypes.IdType.NUMERIC, ns0.datatypes.IdType.STRING],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=mining_dozer;i=6027", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mining_dozer;i=6028", browseName="StaticStringNodeIdPattern", dataType=o6.String)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
ns0.vartypes._3DFrameType(
    nodeId="ns=mining_dozer;i=6013",
    browseName="ns=mining_dozer;ExclusionZone",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mining_dozer;i=6030", browseName="Constant", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mining_dozer;i=6031", browseName="FixedBase", dataType=o6.Boolean)),
        o6.hasComponent(o6.ns["ns=mining_dozer;i=6014"]),
        o6.hasComponent(o6.ns["ns=mining_dozer;i=6018"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_dozer;i=6029", browseName="BaseFrame", dataType=o6.NodeId)),
    ],
    dataType=ns0.datatypes._3DFrame,
    valueRank=1,
    arrayDimensions=[0],
)
typeDictionary = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=mining_dozer;i=6033",
    browseName="ns=mining_dozer;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/Mining/DevelopmentSupport/Dozer/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_dozer;i=6034", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/Mining/DevelopmentSupport/Dozer/"
            )
        )
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:tns="http://opcfoundation.org/UA/Mining/DevelopmentSupport/Dozer/" DefaultByteOrder="LittleEndian" xmlns:opc="http://opcfoundation.org/BinarySchema/" xmlns:ua="http://opcfoundation.org/UA/" TargetNamespace="http://opcfoundation.org/UA/Mining/DevelopmentSupport/Dozer/">\n <opc:Import Namespace="http://opcfoundation.org/UA/"/>\n <opc:EnumeratedType LengthInBits="32" Name="DozerJobMissionEnum">\n  <opc:EnumeratedValue Name="CleanupOperations" Value="0"/>\n  <opc:EnumeratedValue Name="RippingOperations" Value="1"/>\n  <opc:EnumeratedValue Name="TopsoilRemoval" Value="2"/>\n  <opc:EnumeratedValue Name="OverburdenRemoval" Value="3"/>\n  <opc:EnumeratedValue Name="ConstructionOfRoads" Value="4"/>\n  <opc:EnumeratedValue Name="ConstructionOfBerms" Value="5"/>\n  <opc:EnumeratedValue Name="BenchPreparation" Value="6"/>\n  <opc:EnumeratedValue Name="BlastCleanup" Value="7"/>\n  <opc:EnumeratedValue Name="DozerPushIntoVoids" Value="8"/>\n  <opc:EnumeratedValue Name="DozerPushIntoTraps" Value="9"/>\n  <opc:EnumeratedValue Name="Stockpiles" Value="10"/>\n </opc:EnumeratedType>\n</opc:TypeDictionary>\n',
)
typeDictionary_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=mining_dozer;i=6035",
    browseName="ns=mining_dozer;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/Mining/DevelopmentSupport/Dozer/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_dozer;i=6036", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/Mining/DevelopmentSupport/Dozer/Types.xsd"
            )
        )
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema elementFormDefault="qualified" targetNamespace="http://opcfoundation.org/UA/Mining/DevelopmentSupport/Dozer/Types.xsd" xmlns:tns="http://opcfoundation.org/UA/Mining/DevelopmentSupport/Dozer/Types.xsd" xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd" xmlns:xs="http://www.w3.org/2001/XMLSchema">\n <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd"/>\n <xs:simpleType name="DozerJobMissionEnum">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="CleanupOperations_0"/>\n   <xs:enumeration value="RippingOperations_1"/>\n   <xs:enumeration value="TopsoilRemoval_2"/>\n   <xs:enumeration value="OverburdenRemoval_3"/>\n   <xs:enumeration value="ConstructionOfRoads_4"/>\n   <xs:enumeration value="ConstructionOfBerms_5"/>\n   <xs:enumeration value="BenchPreparation_6"/>\n   <xs:enumeration value="BlastCleanup_7"/>\n   <xs:enumeration value="DozerPushIntoVoids_8"/>\n   <xs:enumeration value="DozerPushIntoTraps_9"/>\n   <xs:enumeration value="Stockpiles_10"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:DozerJobMissionEnum" name="DozerJobMissionEnum"/>\n <xs:complexType name="ListOfDozerJobMissionEnum">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:DozerJobMissionEnum" name="DozerJobMissionEnum" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfDozerJobMissionEnum" name="ListOfDozerJobMissionEnum" nillable="true"/>\n</xs:schema>\n',
)
ns0.vartypes.PropertyType(
    nodeId="ns=mining_dozer;i=6037",
    browseName="EnumValues",
    parent="ns=mining_dozer;i=3002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[11],
    value=[
        ns0.datatypes.EnumValueType(
            value=0, displayName=o6.LocalizedText("CleanupOperations"), description=o6.LocalizedText("Enum value representing the clean-up operation of the dozer", "en")
        ),
        ns0.datatypes.EnumValueType(
            value=1, displayName=o6.LocalizedText("RippingOperations"), description=o6.LocalizedText("Enum value representing the soil ripping operation of the dozer", "en")
        ),
        ns0.datatypes.EnumValueType(
            value=2, displayName=o6.LocalizedText("TopsoilRemoval"), description=o6.LocalizedText("Enum value representing the topsoil removal operation of the dozer", "en")
        ),
        ns0.datatypes.EnumValueType(
            value=3, displayName=o6.LocalizedText("OverburdenRemoval"), description=o6.LocalizedText("Enum value representing the overburden removal operation of the dozer", "en")
        ),
        ns0.datatypes.EnumValueType(
            value=4, displayName=o6.LocalizedText("ConstructionOfRoads"), description=o6.LocalizedText("Enum value representing the road construction operation of the dozer", "en")
        ),
        ns0.datatypes.EnumValueType(
            value=5, displayName=o6.LocalizedText("ConstructionOfBerms"), description=o6.LocalizedText("Enum value representing the berm construction operation of the dozer", "en")
        ),
        ns0.datatypes.EnumValueType(
            value=6, displayName=o6.LocalizedText("BenchPreparation"), description=o6.LocalizedText("Enum value representing the bench preparation operation of the dozer", "en")
        ),
        ns0.datatypes.EnumValueType(
            value=7, displayName=o6.LocalizedText("BlastCleanup"), description=o6.LocalizedText("Enum value representing the clean-up operation of the dozer after a blast", "en")
        ),
        ns0.datatypes.EnumValueType(
            value=8, displayName=o6.LocalizedText("DozerPushIntoVoids"), description=o6.LocalizedText("Enum value representing the push-into-voids operation of the dozer", "en")
        ),
        ns0.datatypes.EnumValueType(
            value=9, displayName=o6.LocalizedText("DozerPushIntoTraps"), description=o6.LocalizedText("Enum value representing the push-into-traps operation of the dozer", "en")
        ),
        ns0.datatypes.EnumValueType(
            value=10, displayName=o6.LocalizedText("Stockpiles"), description=o6.LocalizedText("Enum value representing the create stockpiles operation of the dozer", "en")
        ),
    ],
)
mining.objtypes.MiningEquipmentIdentificationType(
    nodeId="ns=mining_dozer;i=5001",
    browseName="ns=mining_dozer;MiningEquipmentIdentification",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_dozer;i=6001",
                browseName="ns=di;AssetId",
                description="To be used by end users to store a unique identification in the context of their overall application. Servers shall support at least 40 Unicode characters for the clients writing this value, this means clients can expect to be able to write strings with a length of 40 Unicode characters into that field.",
                dataType=o6.String,
                value="",
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_dozer;i=6003",
                browseName="ns=di;DeviceClass",
                description="Indicates in which domain or for what purpose the MachineryItem is used.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_dozer;i=6004",
                browseName="ns=di;ManufacturerUri",
                description="A globally unique identifier of the manufacturer of the MachineryItem.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_dozer;i=6005",
                browseName="ns=di;Model",
                description="A human-readable, localized name of the model of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_dozer;i=6006",
                browseName="ns=di;ProductInstanceUri",
                description="A globally unique resource identifier provided by the manufacturer of the machine",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_dozer;i=6032",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_dozer;i=6038",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(mining_dozer_objtypes.DozerType, ns0.reftypes.HasAddIn, o6.ns["ns=mining_dozer;i=5001"])
ns0.vartypes._3DCartesianCoordinatesType(
    nodeId="ns=mining_dozer;i=6040",
    browseName="CartesianCoordinates",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_dozer;i=6041", browseName="X", dataType=o6.Double)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_dozer;i=6042", browseName="Y", dataType=o6.Double)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_dozer;i=6043", browseName="Z", dataType=o6.Double)),
    ],
    dataType=ns0.datatypes._3DCartesianCoordinates,
)
ns0.vartypes._3DOrientationType(
    nodeId="ns=mining_dozer;i=6044",
    browseName="Orientation",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_dozer;i=6045", browseName="A", dataType=o6.Double)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_dozer;i=6046", browseName="B", dataType=o6.Double)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_dozer;i=6047", browseName="C", dataType=o6.Double)),
    ],
    dataType=ns0.datatypes._3DOrientation,
)
ns0.vartypes._3DFrameType(
    nodeId="ns=mining_dozer;i=6039",
    browseName="ns=mining_dozer;MachinePose",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mining_dozer;i=6049", browseName="Constant", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mining_dozer;i=6050", browseName="FixedBase", dataType=o6.Boolean)),
        o6.hasComponent(o6.ns["ns=mining_dozer;i=6040"]),
        o6.hasComponent(o6.ns["ns=mining_dozer;i=6044"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mining_dozer;i=6048", browseName="BaseFrame", dataType=o6.NodeId)),
    ],
    dataType=ns0.datatypes._3DFrame,
    value=ns0.datatypes._3DFrame(cartesianCoordinates=ns0.datatypes._3DCartesianCoordinates(x=0.0, y=0.0, z=0.0), orientation=ns0.datatypes._3DOrientation(a=0.0, b=0.0, c=0.0)),
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=mining_dozer;i=5003",
    browseName="ns=di;ParameterSet",
    description="Flat list of Parameters",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=mining_dozer;i=6013"]), o6.hasComponent(o6.ns["ns=mining_dozer;i=6039"])],
)
o6.reference(mining_dozer_objtypes.DozerType, ns0.reftypes.HasComponent, o6.ns["ns=mining_dozer;i=5003"])


ns0.vartypes.PropertyType(
    nodeId="ns=mining_dozer;i=6007",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=mining_dozer;i=7001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="WorkingArea", dataType=ns0.datatypes._3DFrame, valueRank=1, arrayDimensions=[0]),
        ns0.datatypes.Argument(name="DumpArea", dataType=ns0.datatypes._3DFrame, valueRank=1, arrayDimensions=[0]),
        ns0.datatypes.Argument(name="JobMission", dataType=o6.NodeId("ns=mining_dozer;i=3002"), valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=mining_dozer;i=6008",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=mining_dozer;i=7001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="WorkJobRequestSuccess", dataType=o6.Boolean, valueRank=-1)],
)
o6.call(
    nodeId="ns=mining_dozer;i=7001",
    browseName="ns=mining_dozer;SetWorkJob",
    inputArgs=o6.hasProperty(o6.ns["ns=mining_dozer;i=6007"]),
    outputArgs=o6.hasProperty(o6.ns["ns=mining_dozer;i=6008"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=mining_dozer;i=6009",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=mining_dozer;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="PassthroughExclusionZone",
            dataType=ns0.datatypes._3DFrame,
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText(
                "The PassthroughExclusionZone property describes a 3D polygon specifying the trajectory of another machine that wants to pass through the dozer&#8217;s working area.",
                "en",
            ),
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=mining_dozer;i=6010",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=mining_dozer;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ClearWayResult",
            dataType=o6.Boolean,
            valueRank=-1,
            description=o6.LocalizedText("The ClearWayResult variable indicates whether this method call was successful or not.", "en"),
        )
    ],
)
o6.call(
    nodeId="ns=mining_dozer;i=7002",
    browseName="ns=mining_dozer;Clearway",
    inputArgs=o6.hasProperty(o6.ns["ns=mining_dozer;i=6009"]),
    outputArgs=o6.hasProperty(o6.ns["ns=mining_dozer;i=6010"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=mining_dozer;i=6011",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=mining_dozer;i=7003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="RequestResult", dataType=o6.Boolean, valueRank=-1)],
)
o6.call(nodeId="ns=mining_dozer;i=7003", browseName="ns=mining_dozer;RequestResumeOperation", outputArgs=o6.hasProperty(o6.ns["ns=mining_dozer;i=6011"]))

ns0.vartypes.PropertyType(
    nodeId="ns=mining_dozer;i=6012",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=mining_dozer;i=7004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="RequestResult", dataType=o6.Boolean, valueRank=-1)],
)
o6.call(nodeId="ns=mining_dozer;i=7004", browseName="ns=mining_dozer;RequestStopOperation", outputArgs=o6.hasProperty(o6.ns["ns=mining_dozer;i=6012"]))

ns0.objtypes.BaseObjectType(
    nodeId="ns=mining_dozer;i=5002",
    browseName="ns=di;MethodSet",
    description="Flat list of Methods",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(o6.ns["ns=mining_dozer;i=7001"]),
        o6.hasComponent(o6.ns["ns=mining_dozer;i=7002"]),
        o6.hasComponent(o6.ns["ns=mining_dozer;i=7003"]),
        o6.hasComponent(o6.ns["ns=mining_dozer;i=7004"]),
    ],
)
o6.reference(mining_dozer_objtypes.DozerType, ns0.reftypes.HasComponent, o6.ns["ns=mining_dozer;i=5002"])


del Any, TYPE_CHECKING, uuid, o6, di, ia, machinery, mining, ns0, mining_dozer_datypes, mining_dozer_objtypes
