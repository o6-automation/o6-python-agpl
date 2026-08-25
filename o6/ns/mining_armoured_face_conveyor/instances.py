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

"""Generated OPC UA mining_armoured_face_conveyor namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.machinery as machinery
import o6.ns.mining as mining
import o6.ns.ns0 as ns0
from . import datatypes as mining_armoured_face_conveyor_datypes
from . import vartypes as mining_armoured_face_conveyor_vartypes
from . import objtypes as mining_armoured_face_conveyor_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

httpColonSlashSlashOpcfoundationDotOrgSlashUASlashMiningSlashTransportDumpingSlashArmouredFaceConveyorSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=mining_armoured_face_conveyor;i=5001",
    browseName="ns=mining_armoured_face_conveyor;http://opcfoundation.org/UA/Mining/TransportDumping/ArmouredFaceConveyor/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mining_armoured_face_conveyor;i=6004", browseName="IsNamespaceSubset", dataType=o6.Boolean, value=False)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_armoured_face_conveyor;i=6005", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2022-09-01T00:00:00Z")
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_armoured_face_conveyor;i=6006",
                browseName="NamespaceUri",
                dataType=o6.String,
                value="http://opcfoundation.org/UA/Mining/TransportDumping/ArmouredFaceConveyor/",
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mining_armoured_face_conveyor;i=6007", browseName="NamespaceVersion", dataType=o6.String, value="1.0.0")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_armoured_face_conveyor;i=6008",
                browseName="StaticNodeIdTypes",
                dataType=ns0.datatypes.IdType,
                valueRank=1,
                arrayDimensions=[2],
                value=[ns0.datatypes.IdType.NUMERIC, ns0.datatypes.IdType.STRING],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_armoured_face_conveyor;i=6009", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mining_armoured_face_conveyor;i=6010", browseName="StaticStringNodeIdPattern", dataType=o6.String)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
typeDictionary = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=mining_armoured_face_conveyor;i=6012",
    browseName="ns=mining_armoured_face_conveyor;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/Mining/TransportDumping/ArmouredFaceConveyor/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_armoured_face_conveyor;i=6013",
                browseName="NamespaceUri",
                dataType=o6.String,
                value="http://opcfoundation.org/UA/Mining/TransportDumping/ArmouredFaceConveyor/",
            )
        )
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:tns="http://opcfoundation.org/UA/Mining/TransportDumping/ArmouredFaceConveyor/" DefaultByteOrder="LittleEndian" xmlns:opc="http://opcfoundation.org/BinarySchema/" xmlns:ua="http://opcfoundation.org/UA/" TargetNamespace="http://opcfoundation.org/UA/Mining/TransportDumping/ArmouredFaceConveyor/">\n <opc:Import Namespace="http://opcfoundation.org/UA/"/>\n <opc:EnumeratedType LengthInBits="32" Name="AFCNormalRunningDirectionEnum">\n  <opc:Documentation>Enum describing the direction of the conveyor chain movement during normal operation</opc:Documentation>\n  <opc:EnumeratedValue Name="LEFT" Value="0"/>\n  <opc:EnumeratedValue Name="RIGHT" Value="1"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="AFCStateEnum">\n  <opc:Documentation>Enum describing the current operation state of the chain conveyor</opc:Documentation>\n  <opc:EnumeratedValue Name="UNDEFINED" Value="0"/>\n  <opc:EnumeratedValue Name="STOPPED" Value="1"/>\n  <opc:EnumeratedValue Name="RUNNING" Value="2"/>\n  <opc:EnumeratedValue Name="REVERSE" Value="3"/>\n </opc:EnumeratedType>\n</opc:TypeDictionary>\n',
)
typeDictionary_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=mining_armoured_face_conveyor;i=6014",
    browseName="ns=mining_armoured_face_conveyor;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/Mining/TransportDumping/ArmouredFaceConveyor/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_armoured_face_conveyor;i=6015",
                browseName="NamespaceUri",
                dataType=o6.String,
                value="http://opcfoundation.org/UA/Mining/TransportDumping/ArmouredFaceConveyor/Types.xsd",
            )
        )
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema elementFormDefault="qualified" targetNamespace="http://opcfoundation.org/UA/Mining/TransportDumping/ArmouredFaceConveyor/Types.xsd" xmlns:tns="http://opcfoundation.org/UA/Mining/TransportDumping/ArmouredFaceConveyor/Types.xsd" xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd" xmlns:xs="http://www.w3.org/2001/XMLSchema">\n <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd"/>\n <xs:simpleType name="AFCNormalRunningDirectionEnum">\n  <xs:annotation>\n   <xs:documentation>Enum describing the direction of the conveyor chain movement during normal operation</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="LEFT_0"/>\n   <xs:enumeration value="RIGHT_1"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:AFCNormalRunningDirectionEnum" name="AFCNormalRunningDirectionEnum"/>\n <xs:complexType name="ListOfAFCNormalRunningDirectionEnum">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:AFCNormalRunningDirectionEnum" name="AFCNormalRunningDirectionEnum" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfAFCNormalRunningDirectionEnum" name="ListOfAFCNormalRunningDirectionEnum" nillable="true"/>\n <xs:simpleType name="AFCStateEnum">\n  <xs:annotation>\n   <xs:documentation>Enum describing the current operation state of the chain conveyor</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="UNDEFINED_0"/>\n   <xs:enumeration value="STOPPED_1"/>\n   <xs:enumeration value="RUNNING_2"/>\n   <xs:enumeration value="REVERSE_3"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:AFCStateEnum" name="AFCStateEnum"/>\n <xs:complexType name="ListOfAFCStateEnum">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:AFCStateEnum" name="AFCStateEnum" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfAFCStateEnum" name="ListOfAFCStateEnum" nillable="true"/>\n</xs:schema>\n',
)
ns0.vartypes.PropertyType(
    nodeId="ns=mining_armoured_face_conveyor;i=6019",
    browseName="EnumValues",
    parent="ns=mining_armoured_face_conveyor;i=3002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("UNDEFINED"), description=o6.LocalizedText("Enum value indicating an undefined AFC state", "en")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("STOPPED"), description=o6.LocalizedText("Enum value indicating a stopped AFC state", "en")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("RUNNING"), description=o6.LocalizedText("Enum value indicating a running AFC state", "en")),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("REVERSE"), description=o6.LocalizedText("Enum value indicating a reversed AFC state", "en")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=mining_armoured_face_conveyor;i=6020",
    browseName="EnumValues",
    parent="ns=mining_armoured_face_conveyor;i=3004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("LEFT"), description=o6.LocalizedText("Enum value indicating a normal AFC direction to the left", "en")),
        ns0.datatypes.EnumValueType(
            value=1, displayName=o6.LocalizedText("RIGHT"), description=o6.LocalizedText("Enum value indicating a normal AFC direction to the right", "en")
        ),
    ],
)
mining.objtypes.MiningEquipmentIdentificationType(
    nodeId="ns=mining_armoured_face_conveyor;i=5003",
    browseName="ns=mining;MiningEquipmentIdentification",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_armoured_face_conveyor;i=6001",
                browseName="ns=di;DeviceClass",
                description="Indicates in which domain or for what purpose the MachineryItem is used.",
                dataType=o6.String,
                value="",
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_armoured_face_conveyor;i=6002",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_armoured_face_conveyor;i=6003",
                browseName="ns=di;ManufacturerUri",
                description="A globally unique identifier of the manufacturer of the MachineryItem.",
                dataType=o6.String,
                value="",
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_armoured_face_conveyor;i=6016",
                browseName="ns=di;Model",
                description="A human-readable, localized name of the model of the MachineryItem.",
                dataType=o6.LocalizedText,
                value=o6.LocalizedText(),
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_armoured_face_conveyor;i=6017",
                browseName="ns=di;ProductInstanceUri",
                description="A globally unique resource identifier provided by the manufacturer of the machine",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_armoured_face_conveyor;i=6018",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_armoured_face_conveyor;i=6022",
                browseName="ns=di;AssetId",
                description="To be used by end users to store a unique identification in the context of their overall application. Servers shall support at least 40 Unicode characters for the clients writing this value, this means clients can expect to be able to write strings with a length of 40 Unicode characters into that field.",
                dataType=o6.String,
                value="",
            )
        ),
    ],
)
o6.reference(mining_armoured_face_conveyor_objtypes.AFCType, ns0.reftypes.HasAddIn, o6.ns["ns=mining_armoured_face_conveyor;i=5003"])
mining_armoured_face_conveyor_vartypes.AFCStateType(
    nodeId="ns=mining_armoured_face_conveyor;i=6025",
    browseName="ns=mining_armoured_face_conveyor;AFCState",
    description="The AFCState Variable describes the current state of the AFC",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_armoured_face_conveyor;i=6027",
                browseName="ns=mining_armoured_face_conveyor;AFCNormalRunningDirection",
                description="Direction of the normal AFC operation",
                dataType=mining_armoured_face_conveyor_datypes.AFCNormalRunningDirectionEnum,
                value=mining_armoured_face_conveyor_datypes.AFCNormalRunningDirectionEnum.LEFT,
            )
        )
    ],
    dataType=mining_armoured_face_conveyor_datypes.AFCStateEnum,
    value=mining_armoured_face_conveyor_datypes.AFCStateEnum.UNDEFINED,
)
ns0.vartypes.AnalogUnitRangeType(
    nodeId="ns=mining_armoured_face_conveyor;i=6026",
    browseName="ns=mining_armoured_face_conveyor;Load",
    description="The Load variable describes the current load of the conveyor motor",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_armoured_face_conveyor;i=6028",
                browseName="EngineeringUnits",
                description="This is the EngineeringUnit of the conveyor load.",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20529, displayName=o6.LocalizedText("%"), description=o6.LocalizedText("percent")
                ),
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_armoured_face_conveyor;i=6029",
                browseName="EURange",
                description="This is the EURange of the conveyor load.",
                dataType=ns0.datatypes.Range,
                value=ns0.datatypes.Range(low=0.0, high=200.0),
            )
        ),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=mining_armoured_face_conveyor;i=5002",
    browseName="ns=di;ParameterSet",
    description="Flat list of Parameters",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=mining_armoured_face_conveyor;i=6025"]), o6.hasComponent(o6.ns["ns=mining_armoured_face_conveyor;i=6026"])],
)
o6.reference(mining_armoured_face_conveyor_objtypes.AFCType, ns0.reftypes.HasComponent, o6.ns["ns=mining_armoured_face_conveyor;i=5002"])


del (
    Any,
    TYPE_CHECKING,
    uuid,
    o6,
    di,
    ia,
    machinery,
    mining,
    ns0,
    mining_armoured_face_conveyor_datypes,
    mining_armoured_face_conveyor_vartypes,
    mining_armoured_face_conveyor_objtypes,
)
