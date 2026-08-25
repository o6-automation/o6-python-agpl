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

"""Generated OPC UA mining_shearer_loader namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.machinery as machinery
import o6.ns.mining as mining
import o6.ns.ns0 as ns0
from . import datatypes as mining_shearer_loader_datypes
from . import objtypes as mining_shearer_loader_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

httpColonSlashSlashOpcfoundationDotOrgSlashUASlashMiningSlashExtractionSlashShearerLoaderSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=mining_shearer_loader;i=5001",
    browseName="ns=mining_shearer_loader;http://opcfoundation.org/UA/Mining/Extraction/ShearerLoader/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mining_shearer_loader;i=6004", browseName="IsNamespaceSubset", dataType=o6.Boolean, value=False)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_shearer_loader;i=6005", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2022-09-01T00:00:00Z")
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_shearer_loader;i=6006", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/Mining/Extraction/ShearerLoader/"
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mining_shearer_loader;i=6007", browseName="NamespaceVersion", dataType=o6.String, value="1.0.0")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_shearer_loader;i=6008",
                browseName="StaticNodeIdTypes",
                dataType=ns0.datatypes.IdType,
                valueRank=1,
                arrayDimensions=[2],
                value=[ns0.datatypes.IdType.NUMERIC, ns0.datatypes.IdType.STRING],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_shearer_loader;i=6009", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mining_shearer_loader;i=6010", browseName="StaticStringNodeIdPattern", dataType=o6.String)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
ns0.vartypes.PropertyType(
    nodeId="ns=mining_shearer_loader;i=6011",
    browseName="EnumValues",
    parent="ns=mining_shearer_loader;i=3004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.EnumValueType(
            value=0, displayName=o6.LocalizedText("MountingPositionLeft"), description=o6.LocalizedText("Enum value indicating the left mounting position of a longwall drum", "en")
        ),
        ns0.datatypes.EnumValueType(
            value=1,
            displayName=o6.LocalizedText("MountingPositionRight"),
            description=o6.LocalizedText("Enum value indicating the right mounting position of a longwall drum", "en"),
        ),
        ns0.datatypes.EnumValueType(
            value=2,
            displayName=o6.LocalizedText("MountingPositionLeftLumpBreaker"),
            description=o6.LocalizedText("Enum value indicating the left mounting position of a longwall lump breaker drum", "en"),
        ),
        ns0.datatypes.EnumValueType(
            value=3,
            displayName=o6.LocalizedText("MountingPositionRightLumpBreaker"),
            description=o6.LocalizedText("Enum value indicating the right mounting position of a longwall lump breaker drum", "en"),
        ),
    ],
)
typeDictionary = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=mining_shearer_loader;i=6012",
    browseName="ns=mining_shearer_loader;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/Mining/Extraction/ShearerLoader/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_shearer_loader;i=6013", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/Mining/Extraction/ShearerLoader/"
            )
        )
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:tns="http://opcfoundation.org/UA/Mining/Extraction/ShearerLoader/" DefaultByteOrder="LittleEndian" xmlns:opc="http://opcfoundation.org/BinarySchema/" xmlns:ua="http://opcfoundation.org/UA/" TargetNamespace="http://opcfoundation.org/UA/Mining/Extraction/ShearerLoader/">\n <opc:Import Namespace="http://opcfoundation.org/UA/"/>\n <opc:EnumeratedType LengthInBits="32" Name="ShearerDirectionEnum">\n  <opc:EnumeratedValue Name="STOP" Value="0"/>\n  <opc:EnumeratedValue Name="LEFT" Value="1"/>\n  <opc:EnumeratedValue Name="RIGHT" Value="2"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="ShearerDrumMountingPositionEnum">\n  <opc:EnumeratedValue Name="MountingPositionLeft" Value="0"/>\n  <opc:EnumeratedValue Name="MountingPositionRight" Value="1"/>\n  <opc:EnumeratedValue Name="MountingPositionLeftLumpBreaker" Value="2"/>\n  <opc:EnumeratedValue Name="MountingPositionRightLumpBreaker" Value="3"/>\n </opc:EnumeratedType>\n</opc:TypeDictionary>\n',
)
typeDictionary_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=mining_shearer_loader;i=6014",
    browseName="ns=mining_shearer_loader;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/Mining/Extraction/ShearerLoader/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_shearer_loader;i=6015",
                browseName="NamespaceUri",
                dataType=o6.String,
                value="http://opcfoundation.org/UA/Mining/Extraction/ShearerLoader/Types.xsd",
            )
        )
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema elementFormDefault="qualified" targetNamespace="http://opcfoundation.org/UA/Mining/Extraction/ShearerLoader/Types.xsd" xmlns:tns="http://opcfoundation.org/UA/Mining/Extraction/ShearerLoader/Types.xsd" xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd" xmlns:xs="http://www.w3.org/2001/XMLSchema">\n <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd"/>\n <xs:simpleType name="ShearerDirectionEnum">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="STOP_0"/>\n   <xs:enumeration value="LEFT_1"/>\n   <xs:enumeration value="RIGHT_2"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:ShearerDirectionEnum" name="ShearerDirectionEnum"/>\n <xs:complexType name="ListOfShearerDirectionEnum">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ShearerDirectionEnum" name="ShearerDirectionEnum" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfShearerDirectionEnum" name="ListOfShearerDirectionEnum" nillable="true"/>\n <xs:simpleType name="ShearerDrumMountingPositionEnum">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="MountingPositionLeft_0"/>\n   <xs:enumeration value="MountingPositionRight_1"/>\n   <xs:enumeration value="MountingPositionLeftLumpBreaker_2"/>\n   <xs:enumeration value="MountingPositionRightLumpBreaker_3"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:ShearerDrumMountingPositionEnum" name="ShearerDrumMountingPositionEnum"/>\n <xs:complexType name="ListOfShearerDrumMountingPositionEnum">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ShearerDrumMountingPositionEnum" name="ShearerDrumMountingPositionEnum" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfShearerDrumMountingPositionEnum" name="ListOfShearerDrumMountingPositionEnum" nillable="true"/>\n</xs:schema>\n',
)
mining.vartypes.LongwallShieldOffsetArrayItemType(
    nodeId="ns=mining_shearer_loader;i=6016",
    browseName="ns=mining_shearer_loader;RoofOffset",
    description="The RoofOffset variable describes a list of the current roof offset per shield",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_shearer_loader;i=6017",
                browseName="EngineeringUnits",
                description="This is the EngineeringUnit of the roof offsets.",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5067858, displayName=o6.LocalizedText("m"), description=o6.LocalizedText("metre")
                ),
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_shearer_loader;i=6019",
                browseName="EURange",
                description="This is the EURange of the roof offsets.",
                dataType=ns0.datatypes.Range,
                value=ns0.datatypes.Range(low=-5.0, high=5.0),
            )
        ),
    ],
    dataType=mining.datatypes.LongwallShieldOffsetDataType,
    valueRank=1,
    arrayDimensions=[0],
)
mining.objtypes.MiningEquipmentIdentificationType(
    nodeId="ns=mining_shearer_loader;i=5003",
    browseName="ns=mining;MiningEquipmentIdentification",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_shearer_loader;i=6001",
                browseName="ns=di;DeviceClass",
                description="Indicates in which domain or for what purpose the MachineryItem is used.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_shearer_loader;i=6002",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_shearer_loader;i=6003",
                browseName="ns=di;ManufacturerUri",
                description="A globally unique identifier of the manufacturer of the MachineryItem.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_shearer_loader;i=6020",
                browseName="ns=di;Model",
                description="A human-readable, localized name of the model of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_shearer_loader;i=6021",
                browseName="ns=di;ProductInstanceUri",
                description="A globally unique resource identifier provided by the manufacturer of the machine",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_shearer_loader;i=6022",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(mining_shearer_loader_objtypes.ShearerLoaderDrumType, ns0.reftypes.HasAddIn, o6.ns["ns=mining_shearer_loader;i=5003"])
mining.vartypes.LongwallShieldOffsetArrayItemType(
    nodeId="ns=mining_shearer_loader;i=6026",
    browseName="ns=mining_shearer_loader;FloorOffset",
    description="The FloorOffset variable describes a list of the current floor offset per shield",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_shearer_loader;i=6027",
                browseName="ns=mining;EngineeringUnits",
                description="This is the EngineeringUnit of the floor offsets.",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5067858, displayName=o6.LocalizedText("m"), description=o6.LocalizedText("metre")
                ),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_shearer_loader;i=6028",
                browseName="ns=mining;EURange",
                description="This is the EURange of the floor offsets.",
                dataType=ns0.datatypes.Range,
                value=ns0.datatypes.Range(low=-5.0, high=5.0),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
    ],
    dataType=mining.datatypes.LongwallShieldOffsetDataType,
    valueRank=1,
    arrayDimensions=[0],
)
mining.objtypes.MiningEquipmentIdentificationType(
    nodeId="ns=mining_shearer_loader;i=5002",
    browseName="ns=mining;MiningEquipmentIdentification",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_shearer_loader;i=6023",
                browseName="ns=di;DeviceClass",
                description="Indicates in which domain or for what purpose the MachineryItem is used.",
                dataType=o6.String,
                value="",
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_shearer_loader;i=6024",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
                value=o6.LocalizedText(),
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_shearer_loader;i=6025",
                browseName="ns=di;ManufacturerUri",
                description="A globally unique identifier of the manufacturer of the MachineryItem.",
                dataType=o6.String,
                value="",
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_shearer_loader;i=6029",
                browseName="ns=di;Model",
                description="A human-readable, localized name of the model of the MachineryItem.",
                dataType=o6.LocalizedText,
                value=o6.LocalizedText(),
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_shearer_loader;i=6030",
                browseName="ns=di;ProductInstanceUri",
                description="A globally unique resource identifier provided by the manufacturer of the machine",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_shearer_loader;i=6031",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(mining_shearer_loader_objtypes.ShearerLoaderType, ns0.reftypes.HasAddIn, o6.ns["ns=mining_shearer_loader;i=5002"])
ns0.vartypes.PropertyType(
    nodeId="ns=mining_shearer_loader;i=6032",
    browseName="EnumValues",
    parent="ns=mining_shearer_loader;i=3002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.EnumValueType(
            value=0, displayName=o6.LocalizedText("STOP"), description=o6.LocalizedText("Enum value representing the stopped driving direction of a longwall shearer", "en")
        ),
        ns0.datatypes.EnumValueType(
            value=1, displayName=o6.LocalizedText("LEFT"), description=o6.LocalizedText("Enum value representing the left driving direction of a longwall shearer", "en")
        ),
        ns0.datatypes.EnumValueType(
            value=2, displayName=o6.LocalizedText("RIGHT"), description=o6.LocalizedText("Enum value representing the right driving direction of a longwall shearer", "en")
        ),
    ],
)
ns0.vartypes.AnalogUnitRangeType(
    nodeId="ns=mining_shearer_loader;i=6043",
    browseName="ns=mining_shearer_loader;MaxLength",
    description="The MaxLength variable describes maximum machine length including extracted drums",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_shearer_loader;i=6046",
                browseName="EngineeringUnits",
                description="This is the EngineeringUnit of the shearer maximum length.",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5067858, displayName=o6.LocalizedText("m"), description=o6.LocalizedText("metre")
                ),
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_shearer_loader;i=6047",
                browseName="EURange",
                description="This is the EURange of the shearer maximum length.",
                dataType=ns0.datatypes.Range,
                value=ns0.datatypes.Range(low=1.0, high=20.0),
            )
        ),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitRangeType(
    nodeId="ns=mining_shearer_loader;i=6044",
    browseName="ns=mining_shearer_loader;Position",
    description="The Position variable describes the current position of the shearer in relation  to the center of the shearer",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_shearer_loader;i=6048",
                browseName="EngineeringUnits",
                description="This is the EngineeringUnit of the shearer position.",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5067858, displayName=o6.LocalizedText("m"), description=o6.LocalizedText("metre")
                ),
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_shearer_loader;i=6049",
                browseName="EURange",
                description="This is the EURange of the shearer position.",
                dataType=ns0.datatypes.Range,
                value=ns0.datatypes.Range(low=-50.0, high=500.0),
            )
        ),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=mining_shearer_loader;i=5008",
    browseName="ns=di;ParameterSet",
    description="Flat list of Parameters",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(o6.ns["ns=mining_shearer_loader;i=6016"]),
        o6.hasComponent(o6.ns["ns=mining_shearer_loader;i=6026"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=mining_shearer_loader;i=6041",
                browseName="ns=mining_shearer_loader;DrivingDirection",
                description="The DrivingDirection variable describes the current driving direction of the shearer loader",
                dataType=mining_shearer_loader_datypes.ShearerDirectionEnum,
                value=mining_shearer_loader_datypes.ShearerDirectionEnum.STOP,
            )
        ),
        o6.hasComponent(o6.ns["ns=mining_shearer_loader;i=6043"]),
        o6.hasComponent(o6.ns["ns=mining_shearer_loader;i=6044"]),
    ],
)
o6.reference(mining_shearer_loader_objtypes.ShearerLoaderType, ns0.reftypes.HasComponent, o6.ns["ns=mining_shearer_loader;i=5008"])
ns0.vartypes.AnalogUnitRangeType(
    nodeId="ns=mining_shearer_loader;i=6062",
    browseName="ns=mining_shearer_loader;DrumDiameter",
    description="The DrumDiameter variable describes drum's diameter",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_shearer_loader;i=6065",
                browseName="EngineeringUnits",
                description="This is the EngineeringUnit of the drum diameter.",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5067858, displayName=o6.LocalizedText("m"), description=o6.LocalizedText("metre")
                ),
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_shearer_loader;i=6066",
                browseName="EURange",
                description="This is the EURange of the drum diameter.",
                dataType=ns0.datatypes.Range,
                value=ns0.datatypes.Range(low=0.5, high=10.0),
            )
        ),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitRangeType(
    nodeId="ns=mining_shearer_loader;i=6063",
    browseName="ns=mining_shearer_loader;DrumHeight",
    description="The DrumHeight variable describes drum's current height as measured from the center of the shearer",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_shearer_loader;i=6067",
                browseName="EngineeringUnits",
                description="This is the EngineeringUnit of the drum height.",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5067858, displayName=o6.LocalizedText("m"), description=o6.LocalizedText("metre")
                ),
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_shearer_loader;i=6068",
                browseName="EURange",
                description="This is the EURange of the drum height.",
                dataType=ns0.datatypes.Range,
                value=ns0.datatypes.Range(low=-2.0, high=10.0),
            )
        ),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=mining_shearer_loader;i=5007",
    browseName="ns=di;ParameterSet",
    description="Flat list of Parameters",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_shearer_loader;i=6064",
                browseName="ns=mining_shearer_loader;MountingPosition",
                description="The MountingPosition property describes drum's mounting position on the shearer",
                dataType=mining_shearer_loader_datypes.ShearerDrumMountingPositionEnum,
                value=mining_shearer_loader_datypes.ShearerDrumMountingPositionEnum.MOUNTING_POSITION_LEFT,
            )
        ),
        o6.hasComponent(o6.ns["ns=mining_shearer_loader;i=6062"]),
        o6.hasComponent(o6.ns["ns=mining_shearer_loader;i=6063"]),
    ],
)
o6.reference(mining_shearer_loader_objtypes.ShearerLoaderDrumType, ns0.reftypes.HasComponent, o6.ns["ns=mining_shearer_loader;i=5007"])


ns0.vartypes.PropertyType(
    nodeId="ns=mining_shearer_loader;i=6034",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=mining_shearer_loader;i=7001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="StartShield",
            dataType=o6.Int16,
            valueRank=-1,
            description=o6.LocalizedText("The StartShield property describes the start shield position from which on the drum height correction shall be applied", "en"),
        ),
        ns0.datatypes.Argument(
            name="EndShield",
            dataType=o6.Int16,
            valueRank=-1,
            description=o6.LocalizedText("The EndShield property describes the end shield position until which the drum height correction shall be applied to ", "en"),
        ),
        ns0.datatypes.Argument(
            name="FaceOffset", dataType=o6.Double, valueRank=-1, description=o6.LocalizedText("The FaceOffset property describes the drum height correction", "en")
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=mining_shearer_loader;i=6035",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=mining_shearer_loader;i=7001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="FloorOffsetResult",
            dataType=o6.Boolean,
            valueRank=-1,
            description=o6.LocalizedText("The FloorOffsetResult property describes the successfull execution of the SetFloorOffset method", "en"),
        )
    ],
)
o6.call(
    nodeId="ns=mining_shearer_loader;i=7001",
    browseName="ns=mining_shearer_loader;SetFloorOffset",
    description="The SetFloorOffset method accepts shield parameters and drum height correction offsets and returns a boolean to indicate succesfull execution",
    inputArgs=o6.hasProperty(o6.ns["ns=mining_shearer_loader;i=6034"]),
    outputArgs=o6.hasProperty(o6.ns["ns=mining_shearer_loader;i=6035"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=mining_shearer_loader;i=6036",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=mining_shearer_loader;i=7003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="StartShield",
            dataType=o6.Int16,
            valueRank=-1,
            description=o6.LocalizedText("The StartShield property describes the start shield position from which on the drum height correction shall be applied", "en"),
        ),
        ns0.datatypes.Argument(
            name="EndShield",
            dataType=o6.Int16,
            valueRank=-1,
            description=o6.LocalizedText("The EndShield property describes the end shield position until which the drum height correction shall be applied to ", "en"),
        ),
        ns0.datatypes.Argument(
            name="FaceOffset", dataType=o6.Double, valueRank=-1, description=o6.LocalizedText("The FaceOffset property describes the drum height correction", "en")
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=mining_shearer_loader;i=6037",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=mining_shearer_loader;i=7003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="RoofOffsetResult",
            dataType=o6.Boolean,
            valueRank=-1,
            description=o6.LocalizedText("The FloorOffsetResult property describes the successfull execution of the SetFloorOffset method", "en"),
        )
    ],
)
o6.call(
    nodeId="ns=mining_shearer_loader;i=7003",
    browseName="ns=mining_shearer_loader;SetRoofOffset",
    description="The SetRoofOffset method accepts shield parameters and drum height correction offsets and returns a boolean to indicate succesfull execution",
    inputArgs=o6.hasProperty(o6.ns["ns=mining_shearer_loader;i=6036"]),
    outputArgs=o6.hasProperty(o6.ns["ns=mining_shearer_loader;i=6037"]),
)

ns0.objtypes.BaseObjectType(
    nodeId="ns=mining_shearer_loader;i=5006",
    browseName="ns=di;MethodSet",
    description="Flat list of Methods",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=mining_shearer_loader;i=7001"]), o6.hasComponent(o6.ns["ns=mining_shearer_loader;i=7003"])],
)
o6.reference(mining_shearer_loader_objtypes.ShearerLoaderType, ns0.reftypes.HasComponent, o6.ns["ns=mining_shearer_loader;i=5006"])


del Any, TYPE_CHECKING, uuid, o6, di, ia, machinery, mining, ns0, mining_shearer_loader_datypes, mining_shearer_loader_objtypes
