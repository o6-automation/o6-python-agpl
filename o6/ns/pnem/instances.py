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

"""Generated OPC UA pnem namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
from . import reftypes as pnem_reftypes
from . import datatypes as pnem_datypes
from . import vartypes as pnem_vartypes
from . import objtypes as pnem_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnem;i=5001", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnem;i=5002", browseName="Default XML")
o6.hasEncoding(pnem_datypes.StandbyModeTransitionDataType, o6.ns["ns=pnem;i=5002"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnem;i=5003", browseName="Default JSON")
o6.hasEncoding(pnem_datypes.StandbyModeTransitionDataType, o6.ns["ns=pnem;i=5003"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnem;i=5004", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnem;i=5005", browseName="Default XML")
o6.hasEncoding(pnem_datypes.EnergyStateInformationDataType, o6.ns["ns=pnem;i=5005"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnem;i=5006", browseName="Default JSON")
o6.hasEncoding(pnem_datypes.EnergyStateInformationDataType, o6.ns["ns=pnem;i=5006"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnem;i=5007", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnem;i=5008", browseName="Default XML")
o6.hasEncoding(pnem_datypes.PeVersionDataType, o6.ns["ns=pnem;i=5008"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnem;i=5009", browseName="Default JSON")
o6.hasEncoding(pnem_datypes.PeVersionDataType, o6.ns["ns=pnem;i=5009"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnem;i=5010", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnem;i=5011", browseName="Default XML")
o6.hasEncoding(pnem_datypes.AcPeDataType, o6.ns["ns=pnem;i=5011"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnem;i=5012", browseName="Default JSON")
o6.hasEncoding(pnem_datypes.AcPeDataType, o6.ns["ns=pnem;i=5012"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnem;i=5013", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnem;i=5014", browseName="Default XML")
o6.hasEncoding(pnem_datypes.AcPpDataType, o6.ns["ns=pnem;i=5014"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pnem;i=5015", browseName="Default JSON")
o6.hasEncoding(pnem_datypes.AcPpDataType, o6.ns["ns=pnem;i=5015"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=pnem;i=6005", browseName="ns=pnem;StandbyModeTransitionDataType", dataType=o6.String, value="StandbyModeTransitionDataType")
o6.reference(o6.ns["ns=pnem;i=5001"], "i=39", o6.ns["ns=pnem;i=6005"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=pnem;i=6006", browseName="ns=pnem;StandbyModeTransitionDataType", dataType=o6.String, value="//xs:element[@name='StandbyModeTransitionDataType']"
)
o6.reference(o6.ns["ns=pnem;i=5002"], "i=39", o6.ns["ns=pnem;i=6006"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=pnem;i=6007", browseName="ns=pnem;EnergyStateInformationDataType", dataType=o6.String, value="EnergyStateInformationDataType")
o6.reference(o6.ns["ns=pnem;i=5004"], "i=39", o6.ns["ns=pnem;i=6007"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=pnem;i=6008", browseName="ns=pnem;EnergyStateInformationDataType", dataType=o6.String, value="//xs:element[@name='EnergyStateInformationDataType']"
)
o6.reference(o6.ns["ns=pnem;i=5005"], "i=39", o6.ns["ns=pnem;i=6008"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=pnem;i=6009", browseName="ns=pnem;PeVersionDataType", dataType=o6.String, value="PeVersionDataType")
o6.reference(o6.ns["ns=pnem;i=5007"], "i=39", o6.ns["ns=pnem;i=6009"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=pnem;i=6010", browseName="ns=pnem;PeVersionDataType", dataType=o6.String, value="//xs:element[@name='PeVersionDataType']")
o6.reference(o6.ns["ns=pnem;i=5008"], "i=39", o6.ns["ns=pnem;i=6010"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=pnem;i=6011", browseName="ns=pnem;AcPeDataType", dataType=o6.String, value="AcPeDataType")
o6.reference(o6.ns["ns=pnem;i=5010"], "i=39", o6.ns["ns=pnem;i=6011"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=pnem;i=6012", browseName="ns=pnem;AcPeDataType", dataType=o6.String, value="//xs:element[@name='AcPeDataType']")
o6.reference(o6.ns["ns=pnem;i=5011"], "i=39", o6.ns["ns=pnem;i=6012"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=pnem;i=6013", browseName="ns=pnem;AcPpDataType", dataType=o6.String, value="AcPpDataType")
o6.reference(o6.ns["ns=pnem;i=5013"], "i=39", o6.ns["ns=pnem;i=6013"])
typeDictionary = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=pnem;i=6001",
    browseName="ns=pnem;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/PNEM/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6002", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/PNEM/")),
        o6.hasComponent(o6.ns["ns=pnem;i=6005"]),
        o6.hasComponent(o6.ns["ns=pnem;i=6007"]),
        o6.hasComponent(o6.ns["ns=pnem;i=6009"]),
        o6.hasComponent(o6.ns["ns=pnem;i=6011"]),
        o6.hasComponent(o6.ns["ns=pnem;i=6013"]),
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:tns="http://opcfoundation.org/UA/PNEM/" DefaultByteOrder="LittleEndian" xmlns:opc="http://opcfoundation.org/BinarySchema/" xmlns:ua="http://opcfoundation.org/UA/" TargetNamespace="http://opcfoundation.org/UA/PNEM/">\n <opc:Import Namespace="http://opcfoundation.org/UA/"/>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="AcPeDataType">\n  <opc:Field TypeName="opc:Float" Name="A"/>\n  <opc:Field TypeName="opc:Float" Name="B"/>\n  <opc:Field TypeName="opc:Float" Name="C"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="AcPpDataType">\n  <opc:Field TypeName="opc:Float" Name="A_b"/>\n  <opc:Field TypeName="opc:Float" Name="B_c"/>\n  <opc:Field TypeName="opc:Float" Name="C_a"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="EnergyStateInformationDataType">\n  <opc:Field TypeName="opc:Byte" Name="IDSource"/>\n  <opc:Field TypeName="opc:Byte" Name="IDDestination"/>\n  <opc:Field TypeName="opc:Double" Name="RegularTimeToOperate"/>\n  <opc:Field TypeName="opc:Float" Name="ModePowerConsumption"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="PeVersionDataType">\n  <opc:Field TypeName="opc:Byte" Name="MajorVersion"/>\n  <opc:Field TypeName="opc:Byte" Name="MinorVersion"/>\n  <opc:Field TypeName="opc:Byte" Name="Revision"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="StandbyModeTransitionDataType">\n  <opc:Field TypeName="opc:Byte" Name="IDDestination"/>\n  <opc:Field TypeName="opc:Double" Name="CurrentTimeToDestination"/>\n  <opc:Field TypeName="opc:Double" Name="CurrentTimeToOperate"/>\n  <opc:Field TypeName="opc:Float" Name="EnergyConsumptionToDestination"/>\n </opc:StructuredType>\n <opc:EnumeratedType LengthInBits="32" Name="AccuracyClassEnumeration">\n  <opc:EnumeratedValue Name="ACCURACY_CLASS_0" Value="0"/>\n  <opc:EnumeratedValue Name="ACCURACY_CLASS_1" Value="1"/>\n  <opc:EnumeratedValue Name="ACCURACY_CLASS_2" Value="2"/>\n  <opc:EnumeratedValue Name="ACCURACY_CLASS_3" Value="3"/>\n  <opc:EnumeratedValue Name="ACCURACY_CLASS_4" Value="4"/>\n  <opc:EnumeratedValue Name="ACCURACY_CLASS_5" Value="5"/>\n  <opc:EnumeratedValue Name="ACCURACY_CLASS_6" Value="6"/>\n  <opc:EnumeratedValue Name="ACCURACY_CLASS_7" Value="7"/>\n  <opc:EnumeratedValue Name="ACCURACY_CLASS_8" Value="8"/>\n  <opc:EnumeratedValue Name="ACCURACY_CLASS_9" Value="9"/>\n  <opc:EnumeratedValue Name="ACCURACY_CLASS_10" Value="10"/>\n  <opc:EnumeratedValue Name="ACCURACY_CLASS_11" Value="11"/>\n  <opc:EnumeratedValue Name="ACCURACY_CLASS_12" Value="12"/>\n  <opc:EnumeratedValue Name="ACCURACY_CLASS_13" Value="13"/>\n  <opc:EnumeratedValue Name="ACCURACY_CLASS_14" Value="14"/>\n  <opc:EnumeratedValue Name="ACCURACY_CLASS_15" Value="15"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="AccuracyDomainEnumeration">\n  <opc:EnumeratedValue Name="ACCURACY_DOMAIN_RESERVED" Value="0"/>\n  <opc:EnumeratedValue Name="ACCURACY_DOMAIN_PERCENT_FULL_SCALE" Value="1"/>\n  <opc:EnumeratedValue Name="ACCURACY_DOMAIN_PERCENT_ACTUAL_READING" Value="2"/>\n  <opc:EnumeratedValue Name="ACCURACY_DOMAIN_IEC" Value="3"/>\n  <opc:EnumeratedValue Name="ACCURACY_DOMAIN_EN" Value="4"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="PeClassEnumeration">\n  <opc:EnumeratedValue Name="PE_CLASS1" Value="0"/>\n  <opc:EnumeratedValue Name="PE_CLASS2" Value="1"/>\n  <opc:EnumeratedValue Name="PE_CLASS3" Value="2"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="PeSubclassEnumeration">\n  <opc:EnumeratedValue Name="PE_SUBCLASS1" Value="0"/>\n  <opc:EnumeratedValue Name="PE_SUBCLASS2" Value="1"/>\n </opc:EnumeratedType>\n</opc:TypeDictionary>\n',
)
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=pnem;i=6014", browseName="ns=pnem;AcPpDataType", dataType=o6.String, value="//xs:element[@name='AcPpDataType']")
o6.reference(o6.ns["ns=pnem;i=5014"], "i=39", o6.ns["ns=pnem;i=6014"])
typeDictionary_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=pnem;i=6003",
    browseName="ns=pnem;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/PNEM/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6004", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/PNEM/Types.xsd")),
        o6.hasComponent(o6.ns["ns=pnem;i=6006"]),
        o6.hasComponent(o6.ns["ns=pnem;i=6008"]),
        o6.hasComponent(o6.ns["ns=pnem;i=6010"]),
        o6.hasComponent(o6.ns["ns=pnem;i=6012"]),
        o6.hasComponent(o6.ns["ns=pnem;i=6014"]),
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema elementFormDefault="qualified" targetNamespace="http://opcfoundation.org/UA/PNEM/Types.xsd" xmlns:tns="http://opcfoundation.org/UA/PNEM/Types.xsd" xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd" xmlns:xs="http://www.w3.org/2001/XMLSchema">\n <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd"/>\n <xs:simpleType name="AccuracyClassEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="ACCURACY_CLASS_0_0"/>\n   <xs:enumeration value="ACCURACY_CLASS_1_1"/>\n   <xs:enumeration value="ACCURACY_CLASS_2_2"/>\n   <xs:enumeration value="ACCURACY_CLASS_3_3"/>\n   <xs:enumeration value="ACCURACY_CLASS_4_4"/>\n   <xs:enumeration value="ACCURACY_CLASS_5_5"/>\n   <xs:enumeration value="ACCURACY_CLASS_6_6"/>\n   <xs:enumeration value="ACCURACY_CLASS_7_7"/>\n   <xs:enumeration value="ACCURACY_CLASS_8_8"/>\n   <xs:enumeration value="ACCURACY_CLASS_9_9"/>\n   <xs:enumeration value="ACCURACY_CLASS_10_10"/>\n   <xs:enumeration value="ACCURACY_CLASS_11_11"/>\n   <xs:enumeration value="ACCURACY_CLASS_12_12"/>\n   <xs:enumeration value="ACCURACY_CLASS_13_13"/>\n   <xs:enumeration value="ACCURACY_CLASS_14_14"/>\n   <xs:enumeration value="ACCURACY_CLASS_15_15"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:AccuracyClassEnumeration" name="AccuracyClassEnumeration"/>\n <xs:complexType name="ListOfAccuracyClassEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:AccuracyClassEnumeration" name="AccuracyClassEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfAccuracyClassEnumeration" name="ListOfAccuracyClassEnumeration" nillable="true"/>\n <xs:simpleType name="AccuracyDomainEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="ACCURACY_DOMAIN_RESERVED_0"/>\n   <xs:enumeration value="ACCURACY_DOMAIN_PERCENT_FULL_SCALE_1"/>\n   <xs:enumeration value="ACCURACY_DOMAIN_PERCENT_ACTUAL_READING_2"/>\n   <xs:enumeration value="ACCURACY_DOMAIN_IEC_3"/>\n   <xs:enumeration value="ACCURACY_DOMAIN_EN_4"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:AccuracyDomainEnumeration" name="AccuracyDomainEnumeration"/>\n <xs:complexType name="ListOfAccuracyDomainEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:AccuracyDomainEnumeration" name="AccuracyDomainEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfAccuracyDomainEnumeration" name="ListOfAccuracyDomainEnumeration" nillable="true"/>\n <xs:simpleType name="PeClassEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="PE_CLASS1_0"/>\n   <xs:enumeration value="PE_CLASS2_1"/>\n   <xs:enumeration value="PE_CLASS3_2"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:PeClassEnumeration" name="PeClassEnumeration"/>\n <xs:complexType name="ListOfPeClassEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:PeClassEnumeration" name="PeClassEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfPeClassEnumeration" name="ListOfPeClassEnumeration" nillable="true"/>\n <xs:simpleType name="PeSubclassEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="PE_SUBCLASS1_0"/>\n   <xs:enumeration value="PE_SUBCLASS2_1"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:PeSubclassEnumeration" name="PeSubclassEnumeration"/>\n <xs:complexType name="ListOfPeSubclassEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:PeSubclassEnumeration" name="PeSubclassEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfPeSubclassEnumeration" name="ListOfPeSubclassEnumeration" nillable="true"/>\n <xs:complexType name="AcPeDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:float" name="A"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:float" name="B"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:float" name="C"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:AcPeDataType" name="AcPeDataType"/>\n <xs:complexType name="ListOfAcPeDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:AcPeDataType" name="AcPeDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfAcPeDataType" name="ListOfAcPeDataType" nillable="true"/>\n <xs:complexType name="AcPpDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:float" name="A_b"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:float" name="B_c"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:float" name="C_a"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:AcPpDataType" name="AcPpDataType"/>\n <xs:complexType name="ListOfAcPpDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:AcPpDataType" name="AcPpDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfAcPpDataType" name="ListOfAcPpDataType" nillable="true"/>\n <xs:complexType name="EnergyStateInformationDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedByte" name="IDSource"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedByte" name="IDDestination"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="RegularTimeToOperate"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:float" name="ModePowerConsumption"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:EnergyStateInformationDataType" name="EnergyStateInformationDataType"/>\n <xs:complexType name="ListOfEnergyStateInformationDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:EnergyStateInformationDataType" name="EnergyStateInformationDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfEnergyStateInformationDataType" name="ListOfEnergyStateInformationDataType" nillable="true"/>\n <xs:complexType name="PeVersionDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedByte" name="MajorVersion"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedByte" name="MinorVersion"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedByte" name="Revision"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:PeVersionDataType" name="PeVersionDataType"/>\n <xs:complexType name="ListOfPeVersionDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:PeVersionDataType" name="PeVersionDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfPeVersionDataType" name="ListOfPeVersionDataType" nillable="true"/>\n <xs:complexType name="StandbyModeTransitionDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedByte" name="IDDestination"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="CurrentTimeToDestination"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="CurrentTimeToOperate"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:float" name="EnergyConsumptionToDestination"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:StandbyModeTransitionDataType" name="StandbyModeTransitionDataType"/>\n <xs:complexType name="ListOfStandbyModeTransitionDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:StandbyModeTransitionDataType" name="StandbyModeTransitionDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfStandbyModeTransitionDataType" name="ListOfStandbyModeTransitionDataType" nillable="true"/>\n</xs:schema>\n',
)
ns0.vartypes.PropertyType(
    nodeId="ns=pnem;i=6015",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=pnem;i=3007",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("PE_CLASS1"), description=o6.LocalizedText("The PE Entity supports energy management functionality.")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("PE_CLASS2"), description=o6.LocalizedText("The PE Entity supports energy measurement functionality.")),
        ns0.datatypes.EnumValueType(
            value=2, displayName=o6.LocalizedText("PE_CLASS3"), description=o6.LocalizedText("The PE Entity supports both energy management and energy measurement functionality.")
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=pnem;i=6017",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=pnem;i=3008",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.EnumValueType(
            value=0, displayName=o6.LocalizedText("PE_SUBCLASS1"), description=o6.LocalizedText("The PE Entity does not support energy management disabled.")
        ),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("PE_SUBCLASS2"), description=o6.LocalizedText("The PE Entity supports energy management disabled.")),
    ],
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=pnem;i=6032",
    browseName="ns=pnem;ModePowerConsumption",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6033", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(pnem_objtypes.EnergySavingModeType, ns0.reftypes.HasComponent, o6.ns["ns=pnem;i=6032"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=pnem;i=6034",
    browseName="ns=pnem;EnergyConsumptionToPause",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6035", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(pnem_objtypes.EnergySavingModeType, ns0.reftypes.HasComponent, o6.ns["ns=pnem;i=6034"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=pnem;i=6036",
    browseName="ns=pnem;EnergyConsumptionToOperate",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6037", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
o6.reference(pnem_objtypes.EnergySavingModeType, ns0.reftypes.HasComponent, o6.ns["ns=pnem;i=6036"])
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=pnem;i=6016",
    browseName="ns=pnem;StandbyManagementStatus",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=pnem;i=6038",
                browseName="EnumStrings",
                dataType=o6.LocalizedText,
                valueRank=1,
                arrayDimensions=[9],
                value=[
                    o6.LocalizedText("Energy saving disabled"),
                    o6.LocalizedText("Power Off"),
                    o6.LocalizedText("Ready to operate"),
                    o6.LocalizedText("Moving to Energy Saving Mode"),
                    o6.LocalizedText("Energy saving mode"),
                    o6.LocalizedText("Moving to ready to operate"),
                    o6.LocalizedText("Moving to Sleep mode WOL"),
                    o6.LocalizedText("Sleep mode WOL"),
                    o6.LocalizedText("Wake up WOL"),
                ],
            )
        )
    ],
    dataType=o6.Byte,
)
o6.reference(pnem_objtypes.EnergyStandbyManagementType, ns0.reftypes.HasComponent, o6.ns["ns=pnem;i=6016"])
pnem_objtypes.EnergySavingModeStatusType(
    nodeId="ns=pnem;i=5017",
    browseName="ns=pnem;EnergySavingModeStatus",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=pnem;i=6039",
                browseName="ns=pnem;StateInformation",
                dataType=pnem_datypes.EnergyStateInformationDataType,
                value=pnem_datypes.EnergyStateInformationDataType(iDSource=0, iDDestination=0, regularTimeToOperate=0.0, modePowerConsumption=0.0),
            )
        )
    ],
)
o6.reference(pnem_objtypes.EnergyStandbyManagementType, ns0.reftypes.HasComponent, o6.ns["ns=pnem;i=5017"])
ns0.vartypes.PropertyType(
    nodeId="ns=pnem;i=6111",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=pnem;i=3009",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[16],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("ACCURACY_CLASS_0"), description=o6.LocalizedText("Reserved")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("ACCURACY_CLASS_1")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("ACCURACY_CLASS_2")),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("ACCURACY_CLASS_3")),
        ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("ACCURACY_CLASS_4")),
        ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("ACCURACY_CLASS_5")),
        ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("ACCURACY_CLASS_6")),
        ns0.datatypes.EnumValueType(value=7, displayName=o6.LocalizedText("ACCURACY_CLASS_7")),
        ns0.datatypes.EnumValueType(value=8, displayName=o6.LocalizedText("ACCURACY_CLASS_8")),
        ns0.datatypes.EnumValueType(value=9, displayName=o6.LocalizedText("ACCURACY_CLASS_9")),
        ns0.datatypes.EnumValueType(value=10, displayName=o6.LocalizedText("ACCURACY_CLASS_10")),
        ns0.datatypes.EnumValueType(value=11, displayName=o6.LocalizedText("ACCURACY_CLASS_11")),
        ns0.datatypes.EnumValueType(value=12, displayName=o6.LocalizedText("ACCURACY_CLASS_12")),
        ns0.datatypes.EnumValueType(value=13, displayName=o6.LocalizedText("ACCURACY_CLASS_13")),
        ns0.datatypes.EnumValueType(value=14, displayName=o6.LocalizedText("ACCURACY_CLASS_14")),
        ns0.datatypes.EnumValueType(value=15, displayName=o6.LocalizedText("ACCURACY_CLASS_15")),
    ],
)
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashPNEMSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=pnem;i=5021",
    browseName="ns=pnem;http://opcfoundation.org/UA/PNEM/",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6115", browseName="IsNamespaceSubset", dataType=o6.Boolean)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6116", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2021-03-11T00:00:00Z"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6117", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/PNEM/")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6118", browseName="NamespaceVersion", dataType=o6.String, value="1.0.0")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=pnem;i=6119", browseName="StaticNodeIdTypes", dataType=ns0.datatypes.IdType, valueRank=1, arrayDimensions=[1], value=[ns0.datatypes.IdType.NUMERIC]
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6120", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6121", browseName="StaticStringNodeIdPattern", dataType=o6.String)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
ns0.vartypes.PropertyType(
    nodeId="ns=pnem;i=6130",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=pnem;i=3010",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("ACCURACY_DOMAIN_RESERVED"), description=o6.LocalizedText("Reserved")),
        ns0.datatypes.EnumValueType(
            value=1,
            displayName=o6.LocalizedText("ACCURACY_DOMAIN_PERCENT_FULL_SCALE"),
            description=o6.LocalizedText("The accuracy is given as percent of the full-scale reading. "),
        ),
        ns0.datatypes.EnumValueType(
            value=2, displayName=o6.LocalizedText("ACCURACY_DOMAIN_PERCENT_ACTUAL_READING"), description=o6.LocalizedText("The accuracy is given as percent of the actual reading.")
        ),
        ns0.datatypes.EnumValueType(
            value=3, displayName=o6.LocalizedText("ACCURACY_DOMAIN_IEC"), description=o6.LocalizedText("The accuracy is given according to IEC 61557-12. ")
        ),
        ns0.datatypes.EnumValueType(
            value=4, displayName=o6.LocalizedText("ACCURACY_DOMAIN_EN"), description=o6.LocalizedText("The accuracy is given as specified in the EN 50470-3, Chapter 8.")
        ),
    ],
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=pnem;i=6141",
    browseName="ns=pnem;EnergyConsumptionToOperate",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6142", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=pnem;i=6143",
    browseName="ns=pnem;EnergyConsumptionToPause",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6144", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=pnem;i=6145",
    browseName="ns=pnem;ModePowerConsumption",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6146", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
)
pnem_objtypes.EnergySavingModeType(
    nodeId="ns=pnem;i=5016",
    browseName="ns=pnem;<EnergySavingModes>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6140", browseName="ns=pnem;DynamicData", dataType=o6.Boolean)),
        o6.hasComponent(o6.ns["ns=pnem;i=6141"]),
        o6.hasComponent(o6.ns["ns=pnem;i=6143"]),
        o6.hasComponent(o6.ns["ns=pnem;i=6145"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=pnem;i=6147", browseName="ns=pnem;RegularTimeToOperate", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=pnem;i=6148", browseName="ns=pnem;TimeMaxLengthOfStay", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=pnem;i=6149", browseName="ns=pnem;TimeMinLengthOfStay", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=pnem;i=6150", browseName="ns=pnem;TimeMinPause", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=pnem;i=6151", browseName="ns=pnem;TimeToPause", dataType=ns0.datatypes.Duration)),
    ],
)
o6.reference(pnem_objtypes.EnergySavingModesContainerType, ns0.reftypes.HasComponent, o6.ns["ns=pnem;i=5016"])
pnem_vartypes.MeasurementValueType(
    nodeId="ns=pnem;i=6056",
    browseName="ns=pnem;<MeasurementValue>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6057", browseName="ns=pnem;AccuracyClass", dataType=pnem_datypes.AccuracyClassEnumeration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6058", browseName="ns=pnem;AccuracyDomain", dataType=pnem_datypes.AccuracyDomainEnumeration)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=pnem;i=6059",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=-1, displayName=o6.LocalizedText()),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6152", browseName="ns=pnem;PeMeasurementID", dataType=o6.UInt16)),
    ],
    dataType=ns0.datatypes.Number,
)
o6.reference(pnem_objtypes.EnergyMeasurementType, ns0.reftypes.HasComponent, o6.ns["ns=pnem;i=6056"])
pnem_vartypes.MeasurementValueType(
    nodeId="ns=pnem;i=6060",
    browseName="ns=pnem;AcCurrent",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6061", browseName="ns=pnem;AccuracyClass", dataType=pnem_datypes.AccuracyClassEnumeration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6062", browseName="ns=pnem;AccuracyDomain", dataType=pnem_datypes.AccuracyDomainEnumeration)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=pnem;i=6063",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=4279632, displayName=o6.LocalizedText("A"), description=o6.LocalizedText("ampere")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6153", browseName="ns=pnem;PeMeasurementID", dataType=o6.UInt16)),
    ],
    dataType=pnem_datypes.AcPeDataType,
    value=pnem_datypes.AcPeDataType(a=0.0, b=0.0, c=0.0),
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(pnem_objtypes.IEnergyProfileE0Type, ns0.reftypes.HasComponent, o6.ns["ns=pnem;i=6060"])
pnem_vartypes.MeasurementValueType(
    nodeId="ns=pnem;i=6064",
    browseName="ns=pnem;AcActivePowerTotal",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6065", browseName="ns=pnem;AccuracyClass", dataType=pnem_datypes.AccuracyClassEnumeration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6066", browseName="ns=pnem;AccuracyDomain", dataType=pnem_datypes.AccuracyDomainEnumeration)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=pnem;i=6067",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5723220, displayName=o6.LocalizedText("W"), description=o6.LocalizedText("watt")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6154", browseName="ns=pnem;PeMeasurementID", dataType=o6.UInt16)),
    ],
    dataType=o6.Float,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(pnem_objtypes.IEnergyProfileE1Type, ns0.reftypes.HasComponent, o6.ns["ns=pnem;i=6064"])
pnem_vartypes.MeasurementValueType(
    nodeId="ns=pnem;i=6068",
    browseName="ns=pnem;AcActivePowerTotal",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6069", browseName="ns=pnem;AccuracyClass", dataType=pnem_datypes.AccuracyClassEnumeration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6070", browseName="ns=pnem;AccuracyDomain", dataType=pnem_datypes.AccuracyDomainEnumeration)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=pnem;i=6071",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5723220, displayName=o6.LocalizedText("W"), description=o6.LocalizedText("watt")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6155", browseName="ns=pnem;PeMeasurementID", dataType=o6.UInt16)),
    ],
    dataType=o6.Float,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(pnem_objtypes.IEnergyProfileE2Type, ns0.reftypes.HasComponent, o6.ns["ns=pnem;i=6068"])
pnem_vartypes.MeasurementValueType(
    nodeId="ns=pnem;i=6072",
    browseName="ns=pnem;AcActiveEnergyTotalImportLp",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6073", browseName="ns=pnem;AccuracyClass", dataType=pnem_datypes.AccuracyClassEnumeration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6074", browseName="ns=pnem;AccuracyDomain", dataType=pnem_datypes.AccuracyDomainEnumeration)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=pnem;i=6075",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5720146,
                    displayName=o6.LocalizedText("W&#183;h"),
                    description=o6.LocalizedText("watt hour"),
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6156", browseName="ns=pnem;PeMeasurementID", dataType=o6.UInt16)),
    ],
    dataType=o6.Float,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(pnem_objtypes.IEnergyProfileE2Type, ns0.reftypes.HasComponent, o6.ns["ns=pnem;i=6072"])
pnem_vartypes.MeasurementValueType(
    nodeId="ns=pnem;i=6076",
    browseName="ns=pnem;AcActiveEnergyTotalExportLp",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6077", browseName="ns=pnem;AccuracyClass", dataType=pnem_datypes.AccuracyClassEnumeration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6078", browseName="ns=pnem;AccuracyDomain", dataType=pnem_datypes.AccuracyDomainEnumeration)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=pnem;i=6079",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5720146,
                    displayName=o6.LocalizedText("W&#183;h"),
                    description=o6.LocalizedText("watt hour"),
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6157", browseName="ns=pnem;PeMeasurementID", dataType=o6.UInt16)),
    ],
    dataType=o6.Float,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(pnem_objtypes.IEnergyProfileE2Type, ns0.reftypes.HasComponent, o6.ns["ns=pnem;i=6076"])
pnem_vartypes.MeasurementValueType(
    nodeId="ns=pnem;i=6080",
    browseName="ns=pnem;AcActivePower",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6122", browseName="ns=pnem;AccuracyClass", dataType=pnem_datypes.AccuracyClassEnumeration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6123", browseName="ns=pnem;AccuracyDomain", dataType=pnem_datypes.AccuracyDomainEnumeration)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=pnem;i=6124",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5723220, displayName=o6.LocalizedText("W"), description=o6.LocalizedText("watt")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6158", browseName="ns=pnem;PeMeasurementID", dataType=o6.UInt16)),
    ],
    dataType=pnem_datypes.AcPeDataType,
    value=pnem_datypes.AcPeDataType(a=0.0, b=0.0, c=0.0),
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(pnem_objtypes.IEnergyProfileE3Type, ns0.reftypes.HasComponent, o6.ns["ns=pnem;i=6080"])
pnem_vartypes.MeasurementValueType(
    nodeId="ns=pnem;i=6081",
    browseName="ns=pnem;AcReactivePower",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6131", browseName="ns=pnem;AccuracyClass", dataType=pnem_datypes.AccuracyClassEnumeration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6132", browseName="ns=pnem;AccuracyDomain", dataType=pnem_datypes.AccuracyDomainEnumeration)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=pnem;i=6133",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=4469812, displayName=o6.LocalizedText("var"), description=o6.LocalizedText("var")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6159", browseName="ns=pnem;PeMeasurementID", dataType=o6.UInt16)),
    ],
    dataType=pnem_datypes.AcPeDataType,
    value=pnem_datypes.AcPeDataType(a=0.0, b=0.0, c=0.0),
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(pnem_objtypes.IEnergyProfileE3Type, ns0.reftypes.HasComponent, o6.ns["ns=pnem;i=6081"])
pnem_vartypes.MeasurementValueType(
    nodeId="ns=pnem;i=6082",
    browseName="ns=pnem;AcActiveEnergyTotalImportHp",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6083", browseName="ns=pnem;AccuracyClass", dataType=pnem_datypes.AccuracyClassEnumeration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6084", browseName="ns=pnem;AccuracyDomain", dataType=pnem_datypes.AccuracyDomainEnumeration)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=pnem;i=6085",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5720146,
                    displayName=o6.LocalizedText("W&#183;h"),
                    description=o6.LocalizedText("watt hour"),
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6160", browseName="ns=pnem;PeMeasurementID", dataType=o6.UInt16)),
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(pnem_objtypes.IEnergyProfileE3Type, ns0.reftypes.HasComponent, o6.ns["ns=pnem;i=6082"])
pnem_vartypes.MeasurementValueType(
    nodeId="ns=pnem;i=6086",
    browseName="ns=pnem;AcActiveEnergyTotalExportHp",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6087", browseName="ns=pnem;AccuracyClass", dataType=pnem_datypes.AccuracyClassEnumeration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6088", browseName="ns=pnem;AccuracyDomain", dataType=pnem_datypes.AccuracyDomainEnumeration)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=pnem;i=6089",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5720146,
                    displayName=o6.LocalizedText("W&#183;h"),
                    description=o6.LocalizedText("watt hour"),
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6161", browseName="ns=pnem;PeMeasurementID", dataType=o6.UInt16)),
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(pnem_objtypes.IEnergyProfileE3Type, ns0.reftypes.HasComponent, o6.ns["ns=pnem;i=6086"])
pnem_vartypes.MeasurementValueType(
    nodeId="ns=pnem;i=6090",
    browseName="ns=pnem;AcReactiveEnergyTotalImportHp",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6091", browseName="ns=pnem;AccuracyClass", dataType=pnem_datypes.AccuracyClassEnumeration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6092", browseName="ns=pnem;AccuracyDomain", dataType=pnem_datypes.AccuracyDomainEnumeration)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=pnem;i=6093",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=0, displayName=o6.LocalizedText()),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6162", browseName="ns=pnem;PeMeasurementID", dataType=o6.UInt16)),
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(pnem_objtypes.IEnergyProfileE3Type, ns0.reftypes.HasComponent, o6.ns["ns=pnem;i=6090"])
pnem_vartypes.MeasurementValueType(
    nodeId="ns=pnem;i=6094",
    browseName="ns=pnem;AcReactiveEnergyTotalExportHp",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6095", browseName="ns=pnem;AccuracyClass", dataType=pnem_datypes.AccuracyClassEnumeration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6096", browseName="ns=pnem;AccuracyDomain", dataType=pnem_datypes.AccuracyDomainEnumeration)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=pnem;i=6097",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=0, displayName=o6.LocalizedText()),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6163", browseName="ns=pnem;PeMeasurementID", dataType=o6.UInt16)),
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(pnem_objtypes.IEnergyProfileE3Type, ns0.reftypes.HasComponent, o6.ns["ns=pnem;i=6094"])
pnem_vartypes.MeasurementValueType(
    nodeId="ns=pnem;i=6098",
    browseName="ns=pnem;AcVoltagePe",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6134", browseName="ns=pnem;AccuracyClass", dataType=pnem_datypes.AccuracyClassEnumeration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6135", browseName="ns=pnem;AccuracyDomain", dataType=pnem_datypes.AccuracyDomainEnumeration)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=pnem;i=6136",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5655636, displayName=o6.LocalizedText("V"), description=o6.LocalizedText("volt")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6164", browseName="ns=pnem;PeMeasurementID", dataType=o6.UInt16)),
    ],
    dataType=pnem_datypes.AcPeDataType,
    value=pnem_datypes.AcPeDataType(a=0.0, b=0.0, c=0.0),
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(pnem_objtypes.IEnergyProfileE3Type, ns0.reftypes.HasComponent, o6.ns["ns=pnem;i=6098"])
pnem_vartypes.MeasurementValueType(
    nodeId="ns=pnem;i=6099",
    browseName="ns=pnem;AcVoltagePp",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6137", browseName="ns=pnem;AccuracyClass", dataType=pnem_datypes.AccuracyClassEnumeration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6138", browseName="ns=pnem;AccuracyDomain", dataType=pnem_datypes.AccuracyDomainEnumeration)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=pnem;i=6139",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5655636, displayName=o6.LocalizedText("V"), description=o6.LocalizedText("volt")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6165", browseName="ns=pnem;PeMeasurementID", dataType=o6.UInt16)),
    ],
    dataType=pnem_datypes.AcPpDataType,
    value=pnem_datypes.AcPpDataType(a_b=0.0, b_c=0.0, c_a=0.0),
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(pnem_objtypes.IEnergyProfileE3Type, ns0.reftypes.HasComponent, o6.ns["ns=pnem;i=6099"])
pnem_vartypes.MeasurementValueType(
    nodeId="ns=pnem;i=6100",
    browseName="ns=pnem;AcCurrent",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6125", browseName="ns=pnem;AccuracyClass", dataType=pnem_datypes.AccuracyClassEnumeration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6126", browseName="ns=pnem;AccuracyDomain", dataType=pnem_datypes.AccuracyDomainEnumeration)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=pnem;i=6127",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=4279632, displayName=o6.LocalizedText("A"), description=o6.LocalizedText("ampere")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6166", browseName="ns=pnem;PeMeasurementID", dataType=o6.UInt16)),
    ],
    dataType=pnem_datypes.AcPeDataType,
    value=pnem_datypes.AcPeDataType(a=0.0, b=0.0, c=0.0),
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(pnem_objtypes.IEnergyProfileE3Type, ns0.reftypes.HasComponent, o6.ns["ns=pnem;i=6100"])
pnem_vartypes.MeasurementValueType(
    nodeId="ns=pnem;i=6101",
    browseName="ns=pnem;AcPowerFactor",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6128", browseName="ns=pnem;AccuracyClass", dataType=pnem_datypes.AccuracyClassEnumeration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6129", browseName="ns=pnem;AccuracyDomain", dataType=pnem_datypes.AccuracyDomainEnumeration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6167", browseName="ns=pnem;PeMeasurementID", dataType=o6.UInt16)),
    ],
    dataType=pnem_datypes.AcPeDataType,
    value=pnem_datypes.AcPeDataType(a=0.0, b=0.0, c=0.0),
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(pnem_objtypes.IEnergyProfileE3Type, ns0.reftypes.HasComponent, o6.ns["ns=pnem;i=6101"])
pnem_vartypes.MeasurementValueType(
    nodeId="ns=pnem;i=6102",
    browseName="ns=pnem;DcCurrent",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6103", browseName="ns=pnem;AccuracyClass", dataType=pnem_datypes.AccuracyClassEnumeration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6104", browseName="ns=pnem;AccuracyDomain", dataType=pnem_datypes.AccuracyDomainEnumeration)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=pnem;i=6105",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=4279632, displayName=o6.LocalizedText("A"), description=o6.LocalizedText("ampere")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6168", browseName="ns=pnem;PeMeasurementID", dataType=o6.UInt16)),
    ],
    dataType=o6.Float,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(pnem_objtypes.IEnergyProfileD0Type, ns0.reftypes.HasComponent, o6.ns["ns=pnem;i=6102"])


ns0.vartypes.PropertyType(
    nodeId="ns=pnem;i=6041",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=pnem;i=7001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="BreakLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=pnem;i=7001", browseName="ns=di;BreakLock", outputArgs=o6.hasProperty(o6.ns["ns=pnem;i=6041"]))

ns0.vartypes.PropertyType(
    nodeId="ns=pnem;i=6042",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=pnem;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ExitLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=pnem;i=7002", browseName="ns=di;ExitLock", outputArgs=o6.hasProperty(o6.ns["ns=pnem;i=6042"]))

ns0.vartypes.PropertyType(
    nodeId="ns=pnem;i=6043",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=pnem;i=7003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Context", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=pnem;i=6044",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=pnem;i=7003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="InitLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=pnem;i=7003", browseName="ns=di;InitLock", inputArgs=o6.hasProperty(o6.ns["ns=pnem;i=6043"]), outputArgs=o6.hasProperty(o6.ns["ns=pnem;i=6044"]))

ns0.vartypes.PropertyType(
    nodeId="ns=pnem;i=6049",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=pnem;i=7004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="RenewLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=pnem;i=7004", browseName="ns=di;RenewLock", outputArgs=o6.hasProperty(o6.ns["ns=pnem;i=6049"]))

di.objtypes.LockingServicesType(
    nodeId="ns=pnem;i=5020",
    browseName="ns=pnem;Lock",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6045", browseName="ns=di;Locked", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6046", browseName="ns=di;LockingClient", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6047", browseName="ns=di;LockingUser", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnem;i=6048", browseName="ns=di;RemainingLockTime", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(o6.ns["ns=pnem;i=7001"]),
        o6.hasComponent(o6.ns["ns=pnem;i=7002"]),
        o6.hasComponent(o6.ns["ns=pnem;i=7003"]),
        o6.hasComponent(o6.ns["ns=pnem;i=7004"]),
    ],
)
o6.reference(pnem_objtypes.EnergyStandbyManagementType, ns0.reftypes.HasComponent, o6.ns["ns=pnem;i=5020"])


del Any, TYPE_CHECKING, uuid, o6, di, ns0, pnem_reftypes, pnem_datypes, pnem_vartypes, pnem_objtypes
