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

"""Generated OPC UA pngsdgm namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
from . import reftypes as pngsdgm_reftypes
from . import datatypes as pngsdgm_datypes
from . import vartypes as pngsdgm_vartypes
from . import objtypes as pngsdgm_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.objtypes.DataTypeEncodingType(nodeId="ns=pngsdgm;i=5001", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pngsdgm;i=5002", browseName="Default XML")
o6.hasEncoding(pngsdgm_datypes.GsdGenIoTimeStampDataType, o6.ns["ns=pngsdgm;i=5002"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pngsdgm;i=5003", browseName="Default JSON")
o6.hasEncoding(pngsdgm_datypes.GsdGenIoTimeStampDataType, o6.ns["ns=pngsdgm;i=5003"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pngsdgm;i=5004", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pngsdgm;i=5005", browseName="Default XML")
o6.hasEncoding(pngsdgm_datypes.GsdGenIoTimeDataType, o6.ns["ns=pngsdgm;i=5005"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pngsdgm;i=5006", browseName="Default JSON")
o6.hasEncoding(pngsdgm_datypes.GsdGenIoTimeDataType, o6.ns["ns=pngsdgm;i=5006"])
ns0.vartypes.PropertyType(
    nodeId="ns=pngsdgm;i=6001",
    browseName="EnumValues",
    parent="ns=pngsdgm;i=3003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("QUALIFIER"), description=o6.LocalizedText("Bit length is 1.")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("EMBEDDED_STATUS"), description=o6.LocalizedText("Bit length is 2.")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("STATUS"), description=o6.LocalizedText("Bit length is 8.")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=pngsdgm;i=6007",
    browseName="EnumValues",
    parent="ns=pngsdgm;i=3005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("FAULT"), description=o6.LocalizedText("Fault")),
        ns0.datatypes.EnumValueType(value=512, displayName=o6.LocalizedText("MAINTENANCE_REQUIRED"), description=o6.LocalizedText("Maintenance required")),
        ns0.datatypes.EnumValueType(value=1024, displayName=o6.LocalizedText("MAINTENANCE_DEMANDED"), description=o6.LocalizedText("Maintenance demanded")),
        ns0.datatypes.EnumValueType(
            value=1536, displayName=o6.LocalizedText("USE_QUALIFIED_CHANNEL_QUALIFIER"), description=o6.LocalizedText("Use QualifiedChannelQualifier variable")
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=pngsdgm;i=6008",
    browseName="EnumValues",
    parent="ns=pngsdgm;i=3006",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.EnumValueType(
            value=0,
            displayName=o6.LocalizedText("ALL_DISAPPEARS"),
            description=o6.LocalizedText("The Diagnosis ASE contains no longer any entries (of any severity) for this channel"),
        ),
        ns0.datatypes.EnumValueType(
            value=2048,
            displayName=o6.LocalizedText("APPEARS"),
            description=o6.LocalizedText("An event appears and/or exists further. The Diagnosis ASE contains this and possible other entries for this channel"),
        ),
        ns0.datatypes.EnumValueType(
            value=4096,
            displayName=o6.LocalizedText("DISAPPEARS"),
            description=o6.LocalizedText("An event disappears and/or exists no longer. The Diagnosis ASE contains no longer any entries of the same severity for this channel"),
        ),
        ns0.datatypes.EnumValueType(
            value=6144,
            displayName=o6.LocalizedText("DISAPPEARS_OTHER_REMAIN"),
            description=o6.LocalizedText("An event disappears. The Diagnosis ASE still contains other entries of the same severity for this channel"),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=pngsdgm;i=6009",
    browseName="EnumValues",
    parent="ns=pngsdgm;i=3007",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("MANUFACTURER_SPECIFIC"), description=o6.LocalizedText("Manufacturer specific")),
        ns0.datatypes.EnumValueType(value=8192, displayName=o6.LocalizedText("INPUT_CHANNEL"), description=o6.LocalizedText("Input")),
        ns0.datatypes.EnumValueType(value=16384, displayName=o6.LocalizedText("OUTPUT_CHANNEL"), description=o6.LocalizedText("Output")),
        ns0.datatypes.EnumValueType(value=24576, displayName=o6.LocalizedText("BIDIRECTIONAL_CHANNEL"), description=o6.LocalizedText("Input/Output")),
    ],
)
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=pngsdgm;i=6011", browseName="ns=pngsdgm;GsdGenIoTimeStampDataType", dataType=o6.String, value="GsdGenIoTimeStampDataType")
o6.reference(o6.ns["ns=pngsdgm;i=5001"], "i=39", o6.ns["ns=pngsdgm;i=6011"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=pngsdgm;i=6012", browseName="ns=pngsdgm;GsdGenIoTimeStampDataType", dataType=o6.String, value="//xs:element[@name='GsdGenIoTimeStampDataType']"
)
o6.reference(o6.ns["ns=pngsdgm;i=5002"], "i=39", o6.ns["ns=pngsdgm;i=6012"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=pngsdgm;i=6013", browseName="ns=pngsdgm;GsdGenIoTimeDataType", dataType=o6.String, value="GsdGenIoTimeDataType")
o6.reference(o6.ns["ns=pngsdgm;i=5004"], "i=39", o6.ns["ns=pngsdgm;i=6013"])
pNGSDG = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=pngsdgm;i=6002",
    browseName="ns=pngsdgm;PNGSDG",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/PNGSDGM/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6003", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/PNGSDGM/")),
        o6.hasComponent(o6.ns["ns=pngsdgm;i=6011"]),
        o6.hasComponent(o6.ns["ns=pngsdgm;i=6013"]),
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:tns="http://opcfoundation.org/UA/PNGSDGM/" DefaultByteOrder="LittleEndian" xmlns:opc="http://opcfoundation.org/BinarySchema/" xmlns:ua="http://opcfoundation.org/UA/" TargetNamespace="http://opcfoundation.org/UA/PNGSDGM/">\n <opc:Import Namespace="http://opcfoundation.org/UA/"/>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="GsdGenIoTimeDataType">\n  <opc:Field TypeName="opc:UInt32" Name="NumberOfMilliseconds"/>\n  <opc:Field TypeName="opc:UInt16" Name="NumberOfDays"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="GsdGenIoTimeStampDataType">\n  <opc:Field TypeName="opc:UInt16" Name="Status"/>\n  <opc:Field TypeName="opc:UInt64" Name="Seconds"/>\n  <opc:Field TypeName="opc:UInt32" Name="Nanoseconds"/>\n </opc:StructuredType>\n <opc:EnumeratedType LengthInBits="32" Name="GsdGenChannelAccumulativeEnumeration">\n  <opc:EnumeratedValue Name="SINGLE" Value="0"/>\n  <opc:EnumeratedValue Name="ACCUMULATIVE" Value="256"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="GsdGenChannelDirectionEnumeration">\n  <opc:EnumeratedValue Name="MANUFACTURER_SPECIFIC" Value="0"/>\n  <opc:EnumeratedValue Name="INPUT_CHANNEL" Value="8192"/>\n  <opc:EnumeratedValue Name="OUTPUT_CHANNEL" Value="16384"/>\n  <opc:EnumeratedValue Name="BIDIRECTIONAL_CHANNEL" Value="24576"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="GsdGenChannelMaintenanceEnumeration">\n  <opc:EnumeratedValue Name="FAULT" Value="0"/>\n  <opc:EnumeratedValue Name="MAINTENANCE_REQUIRED" Value="512"/>\n  <opc:EnumeratedValue Name="MAINTENANCE_DEMANDED" Value="1024"/>\n  <opc:EnumeratedValue Name="USE_QUALIFIED_CHANNEL_QUALIFIER" Value="1536"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="GsdGenChannelSpecifierEnumeration">\n  <opc:EnumeratedValue Name="ALL_DISAPPEARS" Value="0"/>\n  <opc:EnumeratedValue Name="APPEARS" Value="2048"/>\n  <opc:EnumeratedValue Name="DISAPPEARS" Value="4096"/>\n  <opc:EnumeratedValue Name="DISAPPEARS_OTHER_REMAIN" Value="6144"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="GsdGenIoCommunicationStatusEnumeration">\n  <opc:EnumeratedValue Name="INDATA" Value="0"/>\n  <opc:EnumeratedValue Name="OFFLINE" Value="1"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="GsdGenIoConfigurationStatusEnumeration">\n  <opc:EnumeratedValue Name="OK" Value="0"/>\n  <opc:EnumeratedValue Name="SUBSTITUTE" Value="1"/>\n  <opc:EnumeratedValue Name="WRONG" Value="2"/>\n  <opc:EnumeratedValue Name="UNKNOWN" Value="3"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="GsdGenIoConsistencyEnumeration">\n  <opc:EnumeratedValue Name="ITEM_CONSISTENCY" Value="0"/>\n  <opc:EnumeratedValue Name="ALL_ITEMS_CONSISTENCY" Value="1"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="GsdGenIoQualityFormatEnumeration">\n  <opc:EnumeratedValue Name="QUALIFIER" Value="0"/>\n  <opc:EnumeratedValue Name="EMBEDDED_STATUS" Value="1"/>\n  <opc:EnumeratedValue Name="STATUS" Value="2"/>\n </opc:EnumeratedType>\n</opc:TypeDictionary>\n',
)
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=pngsdgm;i=6014", browseName="ns=pngsdgm;GsdGenIoTimeDataType", dataType=o6.String, value="//xs:element[@name='GsdGenIoTimeDataType']"
)
o6.reference(o6.ns["ns=pngsdgm;i=5005"], "i=39", o6.ns["ns=pngsdgm;i=6014"])
pNGSDG_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=pngsdgm;i=6004",
    browseName="ns=pngsdgm;PNGSDG",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/PNGSDGM/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6005", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/PNGSDGM/Types.xsd")),
        o6.hasComponent(o6.ns["ns=pngsdgm;i=6012"]),
        o6.hasComponent(o6.ns["ns=pngsdgm;i=6014"]),
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema elementFormDefault="qualified" targetNamespace="http://opcfoundation.org/UA/PNGSDGM/Types.xsd" xmlns:tns="http://opcfoundation.org/UA/PNGSDGM/Types.xsd" xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd" xmlns:xs="http://www.w3.org/2001/XMLSchema">\n <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd"/>\n <xs:simpleType name="GsdGenChannelAccumulativeEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="SINGLE_0"/>\n   <xs:enumeration value="ACCUMULATIVE_256"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:GsdGenChannelAccumulativeEnumeration" name="GsdGenChannelAccumulativeEnumeration"/>\n <xs:complexType name="ListOfGsdGenChannelAccumulativeEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:GsdGenChannelAccumulativeEnumeration" name="GsdGenChannelAccumulativeEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfGsdGenChannelAccumulativeEnumeration" name="ListOfGsdGenChannelAccumulativeEnumeration" nillable="true"/>\n <xs:simpleType name="GsdGenChannelDirectionEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="MANUFACTURER_SPECIFIC_0"/>\n   <xs:enumeration value="INPUT_CHANNEL_8192"/>\n   <xs:enumeration value="OUTPUT_CHANNEL_16384"/>\n   <xs:enumeration value="BIDIRECTIONAL_CHANNEL_24576"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:GsdGenChannelDirectionEnumeration" name="GsdGenChannelDirectionEnumeration"/>\n <xs:complexType name="ListOfGsdGenChannelDirectionEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:GsdGenChannelDirectionEnumeration" name="GsdGenChannelDirectionEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfGsdGenChannelDirectionEnumeration" name="ListOfGsdGenChannelDirectionEnumeration" nillable="true"/>\n <xs:simpleType name="GsdGenChannelMaintenanceEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="FAULT_0"/>\n   <xs:enumeration value="MAINTENANCE_REQUIRED_512"/>\n   <xs:enumeration value="MAINTENANCE_DEMANDED_1024"/>\n   <xs:enumeration value="USE_QUALIFIED_CHANNEL_QUALIFIER_1536"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:GsdGenChannelMaintenanceEnumeration" name="GsdGenChannelMaintenanceEnumeration"/>\n <xs:complexType name="ListOfGsdGenChannelMaintenanceEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:GsdGenChannelMaintenanceEnumeration" name="GsdGenChannelMaintenanceEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfGsdGenChannelMaintenanceEnumeration" name="ListOfGsdGenChannelMaintenanceEnumeration" nillable="true"/>\n <xs:simpleType name="GsdGenChannelSpecifierEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="ALL_DISAPPEARS_0"/>\n   <xs:enumeration value="APPEARS_2048"/>\n   <xs:enumeration value="DISAPPEARS_4096"/>\n   <xs:enumeration value="DISAPPEARS_OTHER_REMAIN_6144"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:GsdGenChannelSpecifierEnumeration" name="GsdGenChannelSpecifierEnumeration"/>\n <xs:complexType name="ListOfGsdGenChannelSpecifierEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:GsdGenChannelSpecifierEnumeration" name="GsdGenChannelSpecifierEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfGsdGenChannelSpecifierEnumeration" name="ListOfGsdGenChannelSpecifierEnumeration" nillable="true"/>\n <xs:simpleType name="GsdGenIoCommunicationStatusEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="INDATA_0"/>\n   <xs:enumeration value="OFFLINE_1"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:GsdGenIoCommunicationStatusEnumeration" name="GsdGenIoCommunicationStatusEnumeration"/>\n <xs:complexType name="ListOfGsdGenIoCommunicationStatusEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:GsdGenIoCommunicationStatusEnumeration" name="GsdGenIoCommunicationStatusEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfGsdGenIoCommunicationStatusEnumeration" name="ListOfGsdGenIoCommunicationStatusEnumeration" nillable="true"/>\n <xs:simpleType name="GsdGenIoConfigurationStatusEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="OK_0"/>\n   <xs:enumeration value="SUBSTITUTE_1"/>\n   <xs:enumeration value="WRONG_2"/>\n   <xs:enumeration value="UNKNOWN_3"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:GsdGenIoConfigurationStatusEnumeration" name="GsdGenIoConfigurationStatusEnumeration"/>\n <xs:complexType name="ListOfGsdGenIoConfigurationStatusEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:GsdGenIoConfigurationStatusEnumeration" name="GsdGenIoConfigurationStatusEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfGsdGenIoConfigurationStatusEnumeration" name="ListOfGsdGenIoConfigurationStatusEnumeration" nillable="true"/>\n <xs:simpleType name="GsdGenIoConsistencyEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="ITEM_CONSISTENCY_0"/>\n   <xs:enumeration value="ALL_ITEMS_CONSISTENCY_1"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:GsdGenIoConsistencyEnumeration" name="GsdGenIoConsistencyEnumeration"/>\n <xs:complexType name="ListOfGsdGenIoConsistencyEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:GsdGenIoConsistencyEnumeration" name="GsdGenIoConsistencyEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfGsdGenIoConsistencyEnumeration" name="ListOfGsdGenIoConsistencyEnumeration" nillable="true"/>\n <xs:simpleType name="GsdGenIoQualityFormatEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="QUALIFIER_0"/>\n   <xs:enumeration value="EMBEDDED_STATUS_1"/>\n   <xs:enumeration value="STATUS_2"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:GsdGenIoQualityFormatEnumeration" name="GsdGenIoQualityFormatEnumeration"/>\n <xs:complexType name="ListOfGsdGenIoQualityFormatEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:GsdGenIoQualityFormatEnumeration" name="GsdGenIoQualityFormatEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfGsdGenIoQualityFormatEnumeration" name="ListOfGsdGenIoQualityFormatEnumeration" nillable="true"/>\n <xs:complexType name="GsdGenIoTimeDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="NumberOfMilliseconds"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedShort" name="NumberOfDays"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:GsdGenIoTimeDataType" name="GsdGenIoTimeDataType"/>\n <xs:complexType name="ListOfGsdGenIoTimeDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:GsdGenIoTimeDataType" name="GsdGenIoTimeDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfGsdGenIoTimeDataType" name="ListOfGsdGenIoTimeDataType" nillable="true"/>\n <xs:complexType name="GsdGenIoTimeStampDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedShort" name="Status"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedLong" name="Seconds"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="Nanoseconds"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:GsdGenIoTimeStampDataType" name="GsdGenIoTimeStampDataType"/>\n <xs:complexType name="ListOfGsdGenIoTimeStampDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:GsdGenIoTimeStampDataType" name="GsdGenIoTimeStampDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfGsdGenIoTimeStampDataType" name="ListOfGsdGenIoTimeStampDataType" nillable="true"/>\n</xs:schema>\n',
)
pngsdgm_objtypes.GsdGenIoChannelDataType(
    nodeId="ns=pngsdgm;i=5007",
    browseName="ns=pngsdgm;Data",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6042", browseName="ns=pngsdgm;BitLength", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6043", browseName="ns=pngsdgm;BitOffset", dataType=o6.UInt16)),
    ],
)
o6.reference(pngsdgm_objtypes.GsdGenIoChannelType, ns0.reftypes.HasComponent, o6.ns["ns=pngsdgm;i=5007"])
pngsdgm_objtypes.GsdGenIoChannelQualityType(
    nodeId="ns=pngsdgm;i=5008",
    browseName="ns=pngsdgm;Quality",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6044", browseName="ns=pngsdgm;BitOffset", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6045", browseName="ns=pngsdgm;Format", dataType=pngsdgm_datypes.GsdGenIoQualityFormatEnumeration)),
    ],
)
o6.reference(pngsdgm_objtypes.GsdGenIoChannelType, ns0.reftypes.HasComponent, o6.ns["ns=pngsdgm;i=5008"])
pngsdgm_vartypes.GsdGenIoDataItemVariableType(
    nodeId="ns=pngsdgm;i=6047",
    browseName="ns=pngsdgm;<DataItemx>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6048", browseName="ns=pngsdgm;UseAsBits", dataType=o6.Boolean))],
)
o6.reference(pngsdgm_objtypes.GsdGenIoDataType, ns0.reftypes.HasComponent, o6.ns["ns=pngsdgm;i=6047"])
pngsdgm_objtypes.GsdGenIoChannelDataType(
    nodeId="ns=pngsdgm;i=5010",
    browseName="ns=pngsdgm;Data",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6049", browseName="ns=pngsdgm;BitLength", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6050", browseName="ns=pngsdgm;BitOffset", dataType=o6.UInt16)),
    ],
)
pngsdgm_objtypes.GsdGenIoChannelType(
    nodeId="ns=pngsdgm;i=5009",
    browseName="ns=pngsdgm;<InputChannelx>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6051", browseName="ns=pngsdgm;Number", dataType=o6.UInt16)),
        o6.hasComponent(o6.ns["ns=pngsdgm;i=5010"]),
    ],
)
o6.reference(pngsdgm_objtypes.GsdGenIoDataType, ns0.reftypes.HasComponent, o6.ns["ns=pngsdgm;i=5009"])
pngsdgm_objtypes.GsdGenIoChannelDataType(
    nodeId="ns=pngsdgm;i=5012",
    browseName="ns=pngsdgm;Data",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6052", browseName="ns=pngsdgm;BitLength", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6053", browseName="ns=pngsdgm;BitOffset", dataType=o6.UInt16)),
    ],
)
pngsdgm_objtypes.GsdGenIoChannelType(
    nodeId="ns=pngsdgm;i=5011",
    browseName="ns=pngsdgm;<OutputChannelx>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6054", browseName="ns=pngsdgm;Number", dataType=o6.UInt16)),
        o6.hasComponent(o6.ns["ns=pngsdgm;i=5012"]),
    ],
)
o6.reference(pngsdgm_objtypes.GsdGenIoDataType, ns0.reftypes.HasComponent, o6.ns["ns=pngsdgm;i=5011"])
pngsdgm_objtypes.GsdGenIoDataType(
    nodeId="ns=pngsdgm;i=5013",
    browseName="ns=pngsdgm;Input",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6055", browseName="ns=pngsdgm;Consistency", dataType=pngsdgm_datypes.GsdGenIoConsistencyEnumeration))
    ],
)
o6.reference(pngsdgm_objtypes.GsdGenSubmoduleApplicationType, ns0.reftypes.HasComponent, o6.ns["ns=pngsdgm;i=5013"])
pngsdgm_objtypes.GsdGenIoDataType(
    nodeId="ns=pngsdgm;i=5014",
    browseName="ns=pngsdgm;Output",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6056", browseName="ns=pngsdgm;Consistency", dataType=pngsdgm_datypes.GsdGenIoConsistencyEnumeration))
    ],
)
o6.reference(pngsdgm_objtypes.GsdGenSubmoduleApplicationType, ns0.reftypes.HasComponent, o6.ns["ns=pngsdgm;i=5014"])
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashPNGSDGMSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=pngsdgm;i=5017",
    browseName="ns=pngsdgm;http://opcfoundation.org/UA/PNGSDGM/",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6059", browseName="IsNamespaceSubset", dataType=o6.Boolean)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6060", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2023-06-30T00:00:00Z"))
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6061", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/PNGSDGM/")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6062", browseName="NamespaceVersion", dataType=o6.String, value="1.0.0")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=pngsdgm;i=6063", browseName="StaticNodeIdTypes", dataType=ns0.datatypes.IdType, valueRank=1, arrayDimensions=[1], value=[ns0.datatypes.IdType.NUMERIC]
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6064", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6065", browseName="StaticStringNodeIdPattern", dataType=o6.String)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
ns0.vartypes.PropertyType(
    nodeId="ns=pngsdgm;i=6066",
    browseName="EnumValues",
    parent="ns=pngsdgm;i=3004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("SINGLE"), description=o6.LocalizedText("Single channel. Diagnosis only for the reported channel")),
        ns0.datatypes.EnumValueType(
            value=256, displayName=o6.LocalizedText("ACCUMULATIVE"), description=o6.LocalizedText("Multiple channels. Accumulative diagnosis from more than one channel")
        ),
    ],
)
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=pngsdgm;i=6057",
    browseName="ns=pngsdgm;<ValueVariable>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6010", browseName="ns=pngsdgm;BMPNumber", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6067", browseName="ns=pngsdgm;EngineeringUnit", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6068", browseName="ns=pngsdgm;EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6069", browseName="ns=pngsdgm;Dimension", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6071", browseName="ns=pngsdgm;Text", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6072", browseName="ns=pngsdgm;TextArray", dataType=o6.String, valueRank=1, arrayDimensions=[0])),
    ],
    valueRank=-3,
)
o6.reference(pngsdgm_objtypes.GsdGenSubmoduleApplicationType, ns0.reftypes.HasComponent, o6.ns["ns=pngsdgm;i=6057"])
ns0.vartypes.PropertyType(
    nodeId="ns=pngsdgm;i=6073",
    browseName="EnumValues",
    parent="ns=pngsdgm;i=3002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("ITEM_CONSISTENCY"), description=o6.LocalizedText("Each data type is handled consistently.")),
        ns0.datatypes.EnumValueType(
            value=1, displayName=o6.LocalizedText("ALL_ITEMS_CONSISTENCY"), description=o6.LocalizedText("The Submodule requires consistency over the whole Input/Output Data.")
        ),
    ],
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=pngsdgm;i=6084",
    browseName="ns=pngsdgm;<UnitVariable>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6070", browseName="ns=pngsdgm;BMPNumber", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6085", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-3,
)
o6.reference(pngsdgm_objtypes.GsdGenSubmoduleApplicationType, ns0.reftypes.HasComponent, o6.ns["ns=pngsdgm;i=6084"])
ns0.vartypes.AnalogUnitRangeType(
    nodeId="ns=pngsdgm;i=6086",
    browseName="ns=pngsdgm;<UnitRangeVariable>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6087", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6088", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6092", browseName="ns=pngsdgm;BMPNumber", dataType=o6.UInt16)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-3,
)
o6.reference(pngsdgm_objtypes.GsdGenSubmoduleApplicationType, ns0.reftypes.HasComponent, o6.ns["ns=pngsdgm;i=6086"])
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=pngsdgm;i=6089",
    browseName="ns=pngsdgm;<EnumerationVariable>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6093", browseName="ns=pngsdgm;BMPNumber", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6096", browseName="ns=pngsdgm;EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6097", browseName="ns=pngsdgm;EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Enumeration,
)
o6.reference(pngsdgm_objtypes.GsdGenSubmoduleApplicationType, ns0.reftypes.HasComponent, o6.ns["ns=pngsdgm;i=6089"])
di.objtypes.FunctionalGroupType(
    nodeId="ns=pngsdgm;i=5019",
    browseName="ns=pngsdgm;<ArrayFolder>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6095", browseName="ns=pngsdgm;BMPNumber", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6098", browseName="ns=pngsdgm;EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6099", browseName="ns=pngsdgm;EURange", dataType=ns0.datatypes.Range)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=pngsdgm;i=6100", browseName="ns=pngsdgm;Element", modellingRule="MandatoryPlaceholder")),
    ],
)
o6.reference(pngsdgm_objtypes.GsdGenSubmoduleApplicationType, ns0.reftypes.HasComponent, o6.ns["ns=pngsdgm;i=5019"])
ns0.vartypes.OptionSetType(
    nodeId="ns=pngsdgm;i=6090",
    browseName="ns=pngsdgm;<OptionSetVariable>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6091", browseName="OptionSetValues", dataType=o6.LocalizedText, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6094", browseName="ns=pngsdgm;BMPNumber", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6101", browseName="ns=pngsdgm;BitMask", dataType=o6.Boolean, valueRank=1, arrayDimensions=[0])),
    ],
)
o6.reference(pngsdgm_objtypes.GsdGenSubmoduleApplicationType, ns0.reftypes.HasComponent, o6.ns["ns=pngsdgm;i=6090"])
ns0.vartypes.PropertyType(
    nodeId="ns=pngsdgm;i=6102",
    browseName="EnumValues",
    parent="ns=pngsdgm;i=3012",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.EnumValueType(
            value=0, displayName=o6.LocalizedText("INDATA"), description=o6.LocalizedText("The Submodule is part of an active AR and exchanging IO Data with a Controller")
        ),
        ns0.datatypes.EnumValueType(
            value=1, displayName=o6.LocalizedText("OFFLINE"), description=o6.LocalizedText("The Submodule is not part of an active AR but may allow reading data values")
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=pngsdgm;i=6103",
    browseName="EnumValues",
    parent="ns=pngsdgm;i=3015",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("OK"), description=o6.LocalizedText("Proper Submodule which works as configured")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("SUBSTITUTE"), description=o6.LocalizedText("Substitute Submodule which works")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("WRONG"), description=o6.LocalizedText("Wrong Submodule which does not work")),
        ns0.datatypes.EnumValueType(
            value=3, displayName=o6.LocalizedText("UNKNOWN"), description=o6.LocalizedText("Unknown Submodule which is plugged at Subslot not found in expected configuration")
        ),
    ],
)


ns0.vartypes.PropertyType(
    nodeId="ns=pngsdgm;i=6075",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=pngsdgm;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="BreakLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=pngsdgm;i=7002", browseName="ns=di;BreakLock", outputArgs=o6.hasProperty(o6.ns["ns=pngsdgm;i=6075"]))

ns0.vartypes.PropertyType(
    nodeId="ns=pngsdgm;i=6076",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=pngsdgm;i=7003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ExitLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=pngsdgm;i=7003", browseName="ns=di;ExitLock", outputArgs=o6.hasProperty(o6.ns["ns=pngsdgm;i=6076"]))

ns0.vartypes.PropertyType(
    nodeId="ns=pngsdgm;i=6077",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=pngsdgm;i=7004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Context", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=pngsdgm;i=6078",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=pngsdgm;i=7004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="InitLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=pngsdgm;i=7004", browseName="ns=di;InitLock", inputArgs=o6.hasProperty(o6.ns["ns=pngsdgm;i=6077"]), outputArgs=o6.hasProperty(o6.ns["ns=pngsdgm;i=6078"]))

ns0.vartypes.PropertyType(
    nodeId="ns=pngsdgm;i=6083",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=pngsdgm;i=7005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="RenewLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=pngsdgm;i=7005", browseName="ns=di;RenewLock", outputArgs=o6.hasProperty(o6.ns["ns=pngsdgm;i=6083"]))

di.objtypes.LockingServicesType(
    nodeId="ns=pngsdgm;i=5018",
    browseName="ns=pngsdgm;Lock",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6079", browseName="ns=di;Locked", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6080", browseName="ns=di;LockingClient", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6081", browseName="ns=di;LockingUser", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pngsdgm;i=6082", browseName="ns=di;RemainingLockTime", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(o6.ns["ns=pngsdgm;i=7002"]),
        o6.hasComponent(o6.ns["ns=pngsdgm;i=7003"]),
        o6.hasComponent(o6.ns["ns=pngsdgm;i=7004"]),
        o6.hasComponent(o6.ns["ns=pngsdgm;i=7005"]),
    ],
)
o6.reference(pngsdgm_objtypes.GsdGenSubmoduleApplicationType, ns0.reftypes.HasComponent, o6.ns["ns=pngsdgm;i=5018"])


del Any, TYPE_CHECKING, uuid, o6, di, ns0, pngsdgm_reftypes, pngsdgm_datypes, pngsdgm_vartypes, pngsdgm_objtypes
