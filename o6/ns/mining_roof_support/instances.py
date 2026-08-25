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

"""Generated OPC UA mining_roof_support namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.machinery as machinery
import o6.ns.mining as mining
import o6.ns.ns0 as ns0
from . import datatypes as mining_roof_support_datypes
from . import objtypes as mining_roof_support_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

typeDictionary = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=mining_roof_support;i=6006",
    browseName="ns=mining_roof_support;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/Mining/DevelopmentSupport/RoofSupportSystem/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_roof_support;i=6007",
                browseName="NamespaceUri",
                dataType=o6.String,
                value="http://opcfoundation.org/UA/Mining/DevelopmentSupport/RoofSupportSystem/",
            )
        )
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:tns="http://opcfoundation.org/UA/Mining/DevelopmentSupport/RoofSupportSystem/" DefaultByteOrder="LittleEndian" xmlns:opc="http://opcfoundation.org/BinarySchema/" xmlns:ua="http://opcfoundation.org/UA/" TargetNamespace="http://opcfoundation.org/UA/Mining/DevelopmentSupport/RoofSupportSystem/">\n <opc:Import Namespace="http://opcfoundation.org/UA/"/>\n <opc:EnumeratedType LengthInBits="32" Name="RSSStateEnum">\n  <opc:EnumeratedValue Name="UNDEFINED" Value="0"/>\n  <opc:EnumeratedValue Name="ONGOING" Value="1"/>\n  <opc:EnumeratedValue Name="ERROR" Value="2"/>\n  <opc:EnumeratedValue Name="FINISHED" Value="3"/>\n </opc:EnumeratedType>\n</opc:TypeDictionary>\n',
)
typeDictionary_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=mining_roof_support;i=6008",
    browseName="ns=mining_roof_support;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/Mining/DevelopmentSupport/RoofSupportSystem/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_roof_support;i=6009",
                browseName="NamespaceUri",
                dataType=o6.String,
                value="http://opcfoundation.org/UA/Mining/DevelopmentSupport/RoofSupportSystem/Types.xsd",
            )
        )
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema elementFormDefault="qualified" targetNamespace="http://opcfoundation.org/UA/Mining/DevelopmentSupport/RoofSupportSystem/Types.xsd" xmlns:tns="http://opcfoundation.org/UA/Mining/DevelopmentSupport/RoofSupportSystem/Types.xsd" xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd" xmlns:xs="http://www.w3.org/2001/XMLSchema">\n <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd"/>\n <xs:simpleType name="RSSStateEnum">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="UNDEFINED_0"/>\n   <xs:enumeration value="ONGOING_1"/>\n   <xs:enumeration value="ERROR_2"/>\n   <xs:enumeration value="FINISHED_3"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:RSSStateEnum" name="RSSStateEnum"/>\n <xs:complexType name="ListOfRSSStateEnum">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:RSSStateEnum" name="RSSStateEnum" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfRSSStateEnum" name="ListOfRSSStateEnum" nillable="true"/>\n</xs:schema>\n',
)
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashMiningSlashDevelopmentSupportSlashRoofSupportSystemSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=mining_roof_support;i=5001",
    browseName="ns=mining_roof_support;http://opcfoundation.org/UA/Mining/DevelopmentSupport/RoofSupportSystem/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mining_roof_support;i=6011", browseName="IsNamespaceSubset", dataType=o6.Boolean, value=False)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_roof_support;i=6012", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2022-09-01T00:00:00Z")
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_roof_support;i=6013",
                browseName="NamespaceUri",
                dataType=o6.String,
                value="http://opcfoundation.org/UA/Mining/DevelopmentSupport/RoofSupportSystem/",
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mining_roof_support;i=6014", browseName="NamespaceVersion", dataType=o6.String, value="1.0.0")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_roof_support;i=6015",
                browseName="StaticNodeIdTypes",
                dataType=ns0.datatypes.IdType,
                valueRank=1,
                arrayDimensions=[2],
                value=[ns0.datatypes.IdType.NUMERIC, ns0.datatypes.IdType.STRING],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_roof_support;i=6016", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mining_roof_support;i=6017", browseName="StaticStringNodeIdPattern", dataType=o6.String)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
mining.objtypes.MiningEquipmentIdentificationType(
    nodeId="ns=mining_roof_support;i=5002",
    browseName="ns=mining;MiningEquipmentIdentification",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_roof_support;i=6001",
                browseName="ns=di;DeviceClass",
                description="Indicates in which domain or for what purpose the MachineryItem is used.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_roof_support;i=6002",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_roof_support;i=6003",
                browseName="ns=di;ManufacturerUri",
                description="A globally unique identifier of the manufacturer of the MachineryItem.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_roof_support;i=6004",
                browseName="ns=di;Model",
                description="A human-readable, localized name of the model of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_roof_support;i=6010",
                browseName="ns=di;ProductInstanceUri",
                description="A globally unique resource identifier provided by the manufacturer of the machine",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_roof_support;i=6018",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(mining_roof_support_objtypes.RoofSupportSystemType, ns0.reftypes.HasAddIn, o6.ns["ns=mining_roof_support;i=5002"])
ns0.vartypes.PropertyType(
    nodeId="ns=mining_roof_support;i=6019",
    browseName="EnumValues",
    parent="ns=mining_roof_support;i=3002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.EnumValueType(
            value=0, displayName=o6.LocalizedText("UNDEFINED"), description=o6.LocalizedText("Enum value indicating an undefined RSS push operation stage", "en")
        ),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("ONGOING"), description=o6.LocalizedText("Enum value indicating an ongoing RSS push operation", "en")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("ERROR"), description=o6.LocalizedText("Enum value indicating an erroneous RSS push operation", "en")),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("FINISHED"), description=o6.LocalizedText("Enum value indicating a finished RSS push operation ", "en")),
    ],
)
ns0.vartypes.AnalogUnitRangeType(
    nodeId="ns=mining_roof_support;i=6025",
    browseName="ns=mining_roof_support;ClearanceLeft",
    description="The ClearanceLeft Variable describes the length of the safe zone on the left side of the shearer. There is no risk of collision between the shearer and the RSS in that zone",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_roof_support;i=6029",
                browseName="EngineeringUnits",
                description="This is the EngineeringUnit of the left clearance.",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5067858, displayName=o6.LocalizedText("m"), description=o6.LocalizedText("metre")
                ),
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_roof_support;i=6030",
                browseName="EURange",
                description="This is the EURange of the left clearance.",
                dataType=ns0.datatypes.Range,
                value=ns0.datatypes.Range(low=-10.0, high=500.0),
            )
        ),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitRangeType(
    nodeId="ns=mining_roof_support;i=6026",
    browseName="ns=mining_roof_support;ClearanceRight",
    description="The ClearanceRight Variable describes the length of the safe zone on the right side of the shearer. There is no risk of collision between the shearer and the RSS in that zone",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_roof_support;i=6031",
                browseName="EngineeringUnits",
                description="This is the EngineeringUnit of the right clearance.",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5067858, displayName=o6.LocalizedText("m"), description=o6.LocalizedText("metre")
                ),
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_roof_support;i=6032",
                browseName="EURange",
                description="This is the EURange of the right clearance.",
                dataType=ns0.datatypes.Range,
                value=ns0.datatypes.Range(low=-10.0, high=500.0),
            )
        ),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitRangeType(
    nodeId="ns=mining_roof_support;i=6028",
    browseName="ns=mining_roof_support;ShieldWidth",
    description="The ShieldWidth Variable describes the width of the shields including the gap between the shields",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_roof_support;i=6033",
                browseName="EngineeringUnits",
                description="This is the EngineeringUnit of the shield width.",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5067858, displayName=o6.LocalizedText("m"), description=o6.LocalizedText("metre")
                ),
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining_roof_support;i=6034",
                browseName="EURange",
                description="This is the EURange of the shield width.",
                dataType=ns0.datatypes.Range,
                value=ns0.datatypes.Range(low=0.5, high=5.0),
            )
        ),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=mining_roof_support;i=5003",
    browseName="ns=di;ParameterSet",
    description="Flat list of Parameters",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=mining_roof_support;i=6024",
                browseName="ns=mining_roof_support;AFCPushState",
                description="The AFCPushState Variable describes the status of the AFCPush process determined on the actual shearer position",
                dataType=mining_roof_support_datypes.RSSStateEnum,
                value=mining_roof_support_datypes.RSSStateEnum.UNDEFINED,
            )
        ),
        o6.hasComponent(o6.ns["ns=mining_roof_support;i=6025"]),
        o6.hasComponent(o6.ns["ns=mining_roof_support;i=6026"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=mining_roof_support;i=6027",
                browseName="ns=mining_roof_support;ShieldAdvanceState",
                description="The ShieldAdvanceState Variable describes the status of the ShieldAdvance process determined on the actual shearer position",
                dataType=mining_roof_support_datypes.RSSStateEnum,
                value=mining_roof_support_datypes.RSSStateEnum.UNDEFINED,
            )
        ),
        o6.hasComponent(o6.ns["ns=mining_roof_support;i=6028"]),
    ],
)
o6.reference(mining_roof_support_objtypes.RoofSupportSystemType, ns0.reftypes.HasComponent, o6.ns["ns=mining_roof_support;i=5003"])


del Any, TYPE_CHECKING, uuid, o6, di, ia, machinery, mining, ns0, mining_roof_support_datypes, mining_roof_support_objtypes
