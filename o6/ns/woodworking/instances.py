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

"""Generated OPC UA woodworking namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.isa95_jobcontrol_v2 as isa95_jobcontrol_v2
import o6.ns.machinery as machinery
import o6.ns.machinery_jobs as machinery_jobs
import o6.ns.ns0 as ns0
from . import datatypes as woodworking_datypes
from . import objtypes as woodworking_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.vartypes.PropertyType(
    nodeId="ns=woodworking;i=123",
    browseName="EnumValues",
    parent="ns=woodworking;i=20",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[6],
    value=[
        ns0.datatypes.EnumValueType(
            value=0, displayName=o6.LocalizedText("OTHER"), description=o6.LocalizedText("This state is used if none of the other states below applies.", "en")
        ),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("AUTOMATIC"), description=o6.LocalizedText("The unit is in automatic mode.", "en")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("SEMIAUTOMATIC"), description=o6.LocalizedText("The unit is in semi-automatic mode.", "en")),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("MANUAL"), description=o6.LocalizedText("The unit is in manual mode.", "en")),
        ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("SETUP"), description=o6.LocalizedText("The unit is in setup mode.", "en")),
        ns0.datatypes.EnumValueType(
            value=5,
            displayName=o6.LocalizedText("SLEEP"),
            description=o6.LocalizedText(
                "The unit is in sleep mode. Component is still switched on, energy consumption reduced by e.g. reducing heating, switching drives off. Production is not possible.",
                "en",
            ),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=woodworking;i=128",
    browseName="EnumValues",
    parent="ns=woodworking;i=21",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("OFFLINE"), description=o6.LocalizedText("The component is offline.", "en")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("STANDBY"), description=o6.LocalizedText("The unit is in standby.", "en")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("READY"), description=o6.LocalizedText("The unit is ready to start working.", "en")),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("WORKING"), description=o6.LocalizedText("The unit is working.", "en")),
        ns0.datatypes.EnumValueType(
            value=4,
            displayName=o6.LocalizedText("ERROR"),
            description=o6.LocalizedText("The unit is not able to start working because there is an error. The cause can be an alarm or error or user intervention.", "en"),
        ),
    ],
)
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashWoodworkingSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=woodworking;i=65",
    browseName="ns=woodworking;http://opcfoundation.org/UA/Woodworking/",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=235", browseName="IsNamespaceSubset", dataType=o6.Boolean)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=236", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2025-06-01T01:02:00Z"))
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=237", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/Woodworking/")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=238", browseName="NamespaceVersion", dataType=o6.String, value="1.02.0")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=woodworking;i=239", browseName="StaticNodeIdTypes", dataType=ns0.datatypes.IdType, valueRank=1, arrayDimensions=[1], value=[ns0.datatypes.IdType.NUMERIC]
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=241", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=242", browseName="StaticStringNodeIdPattern", dataType=o6.String)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
ns0.objtypes.DataTypeEncodingType(nodeId="ns=woodworking;i=5010", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=woodworking;i=5011", browseName="Default XML")
o6.hasEncoding(woodworking_datypes.WwMessageArgumentValueDataType, o6.ns["ns=woodworking;i=5011"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=woodworking;i=5012", browseName="Default JSON")
o6.hasEncoding(woodworking_datypes.WwMessageArgumentValueDataType, o6.ns["ns=woodworking;i=5012"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=woodworking;i=5013", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=woodworking;i=5014", browseName="Default XML")
o6.hasEncoding(woodworking_datypes.WwMessageArgumentDataType, o6.ns["ns=woodworking;i=5014"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=woodworking;i=5015", browseName="Default JSON")
o6.hasEncoding(woodworking_datypes.WwMessageArgumentDataType, o6.ns["ns=woodworking;i=5015"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=woodworking;i=6005", browseName="ns=woodworking;WwMessageArgumentDataType", dataType=o6.String, value="WwMessageArgumentDataType")
o6.reference(o6.ns["ns=woodworking;i=5013"], "i=39", o6.ns["ns=woodworking;i=6005"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=woodworking;i=6006", browseName="ns=woodworking;WwMessageArgumentDataType", dataType=o6.String, value="//xs:element[@name='WwMessageArgumentDataType']"
)
o6.reference(o6.ns["ns=woodworking;i=5014"], "i=39", o6.ns["ns=woodworking;i=6006"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=woodworking;i=6007", browseName="ns=woodworking;WwMessageArgumentValueDataType", dataType=o6.String, value="WwMessageArgumentValueDataType"
)
o6.reference(o6.ns["ns=woodworking;i=5010"], "i=39", o6.ns["ns=woodworking;i=6007"])
typeDictionary = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=woodworking;i=6001",
    browseName="ns=woodworking;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/Woodworking/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6002", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/Woodworking/")),
        o6.hasComponent(o6.ns["ns=woodworking;i=6005"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6007"]),
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:tns="http://opcfoundation.org/UA/Woodworking/" DefaultByteOrder="LittleEndian" xmlns:opc="http://opcfoundation.org/BinarySchema/" xmlns:ua="http://opcfoundation.org/UA/" TargetNamespace="http://opcfoundation.org/UA/Woodworking/">\n <opc:Import Namespace="http://opcfoundation.org/UA/"/>\n <opc:StructuredType BaseType="ua:Argument" Name="WwMessageArgumentDataType">\n  <opc:Documentation>The WwArgumentDataType definition extends the argument structure with an argument value.</opc:Documentation>\n  <opc:Field SourceType="ua:Argument" TypeName="opc:CharArray" Name="Name"/>\n  <opc:Field SourceType="ua:Argument" TypeName="ua:NodeId" Name="DataType"/>\n  <opc:Field SourceType="ua:Argument" TypeName="opc:Int32" Name="ValueRank"/>\n  <opc:Field SourceType="ua:Argument" TypeName="opc:Int32" Name="NoOfArrayDimensions"/>\n  <opc:Field LengthField="NoOfArrayDimensions" SourceType="ua:Argument" TypeName="opc:UInt32" Name="ArrayDimensions"/>\n  <opc:Field SourceType="ua:Argument" TypeName="ua:LocalizedText" Name="Description"/>\n  <opc:Field TypeName="tns:WwMessageArgumentValueDataType" Name="Value"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:Union" Name="WwMessageArgumentValueDataType">\n  <opc:Documentation>The WwArgumentValueDataType definition defines the possible types of an argument value.</opc:Documentation>\n  <opc:Field TypeName="opc:UInt32" Name="SwitchField"/>\n  <opc:Field SwitchField="SwitchField" TypeName="opc:Int32" SwitchValue="1" Name="NoOfArray"/>\n  <opc:Field LengthField="NoOfArray" SwitchField="SwitchField" TypeName="tns:WwMessageArgumentValueDataType" SwitchValue="1" Name="Array"/>\n  <opc:Field SwitchField="SwitchField" TypeName="opc:Boolean" SwitchValue="2" Name="Boolean"/>\n  <opc:Field SwitchField="SwitchField" TypeName="opc:Int16" SwitchValue="3" Name="Int16"/>\n  <opc:Field SwitchField="SwitchField" TypeName="opc:Int32" SwitchValue="4" Name="Int32"/>\n  <opc:Field SwitchField="SwitchField" TypeName="opc:Int64" SwitchValue="5" Name="Int64"/>\n  <opc:Field SwitchField="SwitchField" TypeName="opc:SByte" SwitchValue="6" Name="SByte"/>\n  <opc:Field SwitchField="SwitchField" TypeName="opc:UInt16" SwitchValue="7" Name="UInt16"/>\n  <opc:Field SwitchField="SwitchField" TypeName="opc:UInt32" SwitchValue="8" Name="UInt32"/>\n  <opc:Field SwitchField="SwitchField" TypeName="opc:UInt64" SwitchValue="9" Name="UInt64"/>\n  <opc:Field SwitchField="SwitchField" TypeName="opc:Byte" SwitchValue="10" Name="Byte"/>\n  <opc:Field SwitchField="SwitchField" TypeName="opc:DateTime" SwitchValue="11" Name="DateTime"/>\n  <opc:Field SwitchField="SwitchField" TypeName="opc:Guid" SwitchValue="12" Name="Guid"/>\n  <opc:Field SwitchField="SwitchField" TypeName="ua:LocalizedText" SwitchValue="13" Name="LocalizedText"/>\n  <opc:Field SwitchField="SwitchField" TypeName="opc:Double" SwitchValue="14" Name="Double"/>\n  <opc:Field SwitchField="SwitchField" TypeName="opc:Float" SwitchValue="15" Name="Float"/>\n  <opc:Field SwitchField="SwitchField" TypeName="opc:CharArray" SwitchValue="16" Name="String"/>\n  <opc:Field SwitchField="SwitchField" TypeName="opc:CharArray" SwitchValue="17" Name="Other"/>\n </opc:StructuredType>\n <opc:EnumeratedType LengthInBits="32" Name="WwEventCategoryEnumeration">\n  <opc:Documentation>This enumeration represents the category of an event.</opc:Documentation>\n  <opc:EnumeratedValue Name="OTHER" Value="0"/>\n  <opc:EnumeratedValue Name="DIAGNOSTIC" Value="1"/>\n  <opc:EnumeratedValue Name="INFORMATION" Value="2"/>\n  <opc:EnumeratedValue Name="WARNING" Value="3"/>\n  <opc:EnumeratedValue Name="ALARM" Value="4"/>\n  <opc:EnumeratedValue Name="ERROR" Value="5"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="WwUnitModeEnumeration">\n  <opc:Documentation>This enumeration represents the generalized mode of a unit.</opc:Documentation>\n  <opc:EnumeratedValue Name="OTHER" Value="0"/>\n  <opc:EnumeratedValue Name="AUTOMATIC" Value="1"/>\n  <opc:EnumeratedValue Name="SEMIAUTOMATIC" Value="2"/>\n  <opc:EnumeratedValue Name="MANUAL" Value="3"/>\n  <opc:EnumeratedValue Name="SETUP" Value="4"/>\n  <opc:EnumeratedValue Name="SLEEP" Value="5"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="WwUnitStateEnumeration">\n  <opc:Documentation>This enumeration represents the generalized state of a unit.</opc:Documentation>\n  <opc:EnumeratedValue Name="OFFLINE" Value="0"/>\n  <opc:EnumeratedValue Name="STANDBY" Value="1"/>\n  <opc:EnumeratedValue Name="READY" Value="2"/>\n  <opc:EnumeratedValue Name="WORKING" Value="3"/>\n  <opc:EnumeratedValue Name="ERROR" Value="4"/>\n </opc:EnumeratedType>\n</opc:TypeDictionary>\n',
)
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=woodworking;i=6008", browseName="ns=woodworking;WwMessageArgumentValueDataType", dataType=o6.String, value="//xs:element[@name='WwMessageArgumentValueDataType']"
)
o6.reference(o6.ns["ns=woodworking;i=5011"], "i=39", o6.ns["ns=woodworking;i=6008"])
typeDictionary_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=woodworking;i=6003",
    browseName="ns=woodworking;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/Woodworking/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6004", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/Woodworking/Types.xsd")
        ),
        o6.hasComponent(o6.ns["ns=woodworking;i=6006"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6008"]),
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema elementFormDefault="qualified" targetNamespace="http://opcfoundation.org/UA/Woodworking/Types.xsd" xmlns:tns="http://opcfoundation.org/UA/Woodworking/Types.xsd" xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd" xmlns:xs="http://www.w3.org/2001/XMLSchema">\n <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd"/>\n <xs:simpleType name="WwEventCategoryEnumeration">\n  <xs:annotation>\n   <xs:documentation>This enumeration represents the category of an event.</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="OTHER_0"/>\n   <xs:enumeration value="DIAGNOSTIC_1"/>\n   <xs:enumeration value="INFORMATION_2"/>\n   <xs:enumeration value="WARNING_3"/>\n   <xs:enumeration value="ALARM_4"/>\n   <xs:enumeration value="ERROR_5"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:WwEventCategoryEnumeration" name="WwEventCategoryEnumeration"/>\n <xs:complexType name="ListOfWwEventCategoryEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:WwEventCategoryEnumeration" name="WwEventCategoryEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfWwEventCategoryEnumeration" name="ListOfWwEventCategoryEnumeration" nillable="true"/>\n <xs:simpleType name="WwUnitModeEnumeration">\n  <xs:annotation>\n   <xs:documentation>This enumeration represents the generalized mode of a unit.</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="OTHER_0"/>\n   <xs:enumeration value="AUTOMATIC_1"/>\n   <xs:enumeration value="SEMIAUTOMATIC_2"/>\n   <xs:enumeration value="MANUAL_3"/>\n   <xs:enumeration value="SETUP_4"/>\n   <xs:enumeration value="SLEEP_5"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:WwUnitModeEnumeration" name="WwUnitModeEnumeration"/>\n <xs:complexType name="ListOfWwUnitModeEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:WwUnitModeEnumeration" name="WwUnitModeEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfWwUnitModeEnumeration" name="ListOfWwUnitModeEnumeration" nillable="true"/>\n <xs:simpleType name="WwUnitStateEnumeration">\n  <xs:annotation>\n   <xs:documentation>This enumeration represents the generalized state of a unit.</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="OFFLINE_0"/>\n   <xs:enumeration value="STANDBY_1"/>\n   <xs:enumeration value="READY_2"/>\n   <xs:enumeration value="WORKING_3"/>\n   <xs:enumeration value="ERROR_4"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:WwUnitStateEnumeration" name="WwUnitStateEnumeration"/>\n <xs:complexType name="ListOfWwUnitStateEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:WwUnitStateEnumeration" name="WwUnitStateEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfWwUnitStateEnumeration" name="ListOfWwUnitStateEnumeration" nillable="true"/>\n <xs:complexType name="WwMessageArgumentDataType">\n  <xs:annotation>\n   <xs:documentation>The WwArgumentDataType definition extends the argument structure with an argument value.</xs:documentation>\n  </xs:annotation>\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:Argument">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="tns:WwMessageArgumentValueDataType" name="Value"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:WwMessageArgumentDataType" name="WwMessageArgumentDataType"/>\n <xs:complexType name="ListOfWwMessageArgumentDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:WwMessageArgumentDataType" name="WwMessageArgumentDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfWwMessageArgumentDataType" name="ListOfWwMessageArgumentDataType" nillable="true"/>\n <xs:complexType name="WwMessageArgumentValueDataType">\n  <xs:annotation>\n   <xs:documentation>The WwArgumentValueDataType definition defines the possible types of an argument value.</xs:documentation>\n  </xs:annotation>\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="SwitchField"/>\n   <xs:choice>\n    <xs:element minOccurs="0" maxOccurs="1" type="tns:ListOfWwMessageArgumentValueDataType" name="Array"/>\n    <xs:element minOccurs="0" maxOccurs="1" type="xs:boolean" name="Boolean"/>\n    <xs:element minOccurs="0" maxOccurs="1" type="xs:short" name="Int16"/>\n    <xs:element minOccurs="0" maxOccurs="1" type="xs:int" name="Int32"/>\n    <xs:element minOccurs="0" maxOccurs="1" type="xs:long" name="Int64"/>\n    <xs:element minOccurs="0" maxOccurs="1" type="xs:byte" name="SByte"/>\n    <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedShort" name="UInt16"/>\n    <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="UInt32"/>\n    <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedLong" name="UInt64"/>\n    <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedByte" name="Byte"/>\n    <xs:element minOccurs="0" maxOccurs="1" type="xs:dateTime" name="DateTime"/>\n    <xs:element minOccurs="0" maxOccurs="1" type="ua:Guid" name="Guid"/>\n    <xs:element minOccurs="0" maxOccurs="1" type="ua:LocalizedText" name="LocalizedText"/>\n    <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="Double"/>\n    <xs:element minOccurs="0" maxOccurs="1" type="xs:float" name="Float"/>\n    <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="String"/>\n    <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="Other"/>\n   </xs:choice>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:WwMessageArgumentValueDataType" name="WwMessageArgumentValueDataType"/>\n <xs:complexType name="ListOfWwMessageArgumentValueDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:WwMessageArgumentValueDataType" name="WwMessageArgumentValueDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfWwMessageArgumentValueDataType" name="ListOfWwMessageArgumentValueDataType" nillable="true"/>\n</xs:schema>\n',
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=woodworking;i=5003",
    browseName="ns=woodworking;Flags",
    description="The Flags Object provides the flags of the unit.",
    modellingRule="Optional",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6070",
                browseName="ns=woodworking;AirPresent",
                description="The AirPresent Variable is true if the air pressure is present in the machine.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6071", browseName="ns=woodworking;Alarm", description="The Alarm Variable is true if at least one alarm exists.", dataType=o6.Boolean
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6072",
                browseName="ns=woodworking;MachineOn",
                description="The MachineOn Variable is true if the machine is switched on. If the OPC UA Server runs on the machine this value is always true.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6073",
                browseName="ns=woodworking;MachineInitialized",
                description="The MachineInitialized Variable is true if MachineOn is true, the PLC and the control processes are running. The machine is ready for usage for the operator.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6074",
                browseName="ns=woodworking;PowerPresent",
                description="The PowerPresent Variable is true if the power supply is present (the drives are ready to move).",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6075",
                browseName="ns=woodworking;DustChipSuction",
                description="The DustChipSuction Variable is true if the dust and chip suction is ready.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6076",
                browseName="ns=woodworking;Emergency",
                description="The Emergency Variable is true if at least one emergency button is pressed.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6077",
                browseName="ns=woodworking;Safety",
                description="The Safety Variable is true if at least one safety device (light curtain, safety mat, …) has intervened.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6078",
                browseName="ns=woodworking;Calibrated",
                description="The Calibrated Variable is true if all devices are calibrated.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6079",
                browseName="ns=woodworking;Remote",
                description="The Remote Variable is true if the machine is working with programs sent by the supervisor or other external application.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6080",
                browseName="ns=woodworking;WorkpiecePresent",
                description="The WorkpiecePresent Variable is true if at least one piece is inside the machine.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6081", browseName="ns=woodworking;Moving", description="The Moving Variable is true if at least one axis is moving.", dataType=o6.Boolean
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6082",
                browseName="ns=woodworking;Error",
                description="The Error Variable is true if at least one reason exists which prevents the machine from working.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6083", browseName="ns=woodworking;Warning", description="The Warning Variable is true if at least one warning exists.", dataType=o6.Boolean
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6084",
                browseName="ns=woodworking;Hold",
                description="The Hold Variable is true if the movements are paused by the operator.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6085",
                browseName="ns=woodworking;RecipeInRun",
                description="The RecipeInRun Variable is true if the machine runs its program. However, if the machine is paused by the program, the machine is considered to still be running its program, i.e. while the RecipeInHold Variable is true, the RecipeInRun cannot be false.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6086",
                browseName="ns=woodworking;RecipeInSetup",
                description="The RecipeInSetup Variable is true if the RecipeInRun is true and the machine is in the setup phase (example: automatic tool change).",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6087",
                browseName="ns=woodworking;RecipeInHold",
                description="The RecipeInHold Variable is true if the machine is paused by the program. This is only possible if the RecipeInRun Variable is also true.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6088",
                browseName="ns=woodworking;ManualActivityRequired",
                description="The ManualActivityRequired Variable is true if a manual activity by the operator is required. The RecipeInRun is not affected.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6089",
                browseName="ns=woodworking;LoadingEnabled",
                description="The LoadingEnabled Variable is true if the unit is ready to get the next new part. If this is false no part can get into the unit.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6090",
                browseName="ns=woodworking;WaitUnload",
                description="The WaitUnload Variable is true if the machine is waiting to unload pieces.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6091",
                browseName="ns=woodworking;WaitLoad",
                description="The WaitLoad Variable is true if the machine is waiting for pieces.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6092",
                browseName="ns=woodworking;EnergySaving",
                description="The EnergySaving Variable is true if energy saving is activated on the machine.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6093",
                browseName="ns=woodworking;ExternalEmergency",
                description="The ExternalEmergency Variable is true if there is an emergency from the line controller.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6094",
                browseName="ns=woodworking;MaintenanceRequired",
                description="The MaintenanceRequired Variable is true if maintenance is required.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6095",
                browseName="ns=woodworking;FeedRuns",
                description="The FeedRuns Variable is true if the feed is running on a throughfeed machine.",
                dataType=o6.Boolean,
            )
        ),
    ],
)
o6.reference(woodworking_objtypes.IWwBaseStateType, ns0.reftypes.HasComponent, o6.ns["ns=woodworking;i=5003"])
o6.reference(o6.ns["ns=woodworking;i=5003"], "i=17603", woodworking_objtypes.IWwUnitFlagsType)
ns0.objtypes.BaseObjectType(
    nodeId="ns=woodworking;i=5004",
    browseName="ns=woodworking;Overview",
    description="The Overview Object provides a general state of the unit.",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6096",
                browseName="ns=woodworking;CurrentState",
                description="The CurrentState Variable provides the generalized state of the unit.",
                dataType=woodworking_datypes.WwUnitStateEnumeration,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6097",
                browseName="ns=woodworking;CurrentMode",
                description="The CurrentMode Variable provides the generalized mode of the unit.",
                dataType=woodworking_datypes.WwUnitModeEnumeration,
            )
        ),
    ],
)
o6.reference(woodworking_objtypes.IWwBaseStateType, ns0.reftypes.HasComponent, o6.ns["ns=woodworking;i=5004"])
o6.reference(o6.ns["ns=woodworking;i=5004"], "i=17603", woodworking_objtypes.IWwUnitOverviewType)
ns0.vartypes.PropertyType(
    nodeId="ns=woodworking;i=6103",
    browseName="EnumValues",
    parent="ns=woodworking;i=3004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[6],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("OTHER"), description=o6.LocalizedText("No other event category applies or it is unknown.", "en")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("DIAGNOSTIC"), description=o6.LocalizedText("The event is a diagnostic event.", "en")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("INFORMATION"), description=o6.LocalizedText("The event is an information event.", "en")),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("WARNING"), description=o6.LocalizedText("The event is a warning event.", "en")),
        ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("ALARM"), description=o6.LocalizedText("The event is an alarm event.", "en")),
        ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("ERROR"), description=o6.LocalizedText("The event is an error event.", "en")),
    ],
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=woodworking;i=5017",
    browseName="ns=woodworking;Flags",
    description="The Flags Object provides the flags of the unit.",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6138",
                browseName="ns=woodworking;MachineOn",
                description="The MachineOn Variable is true if the machine is switched on. If the OPC UA Server runs on the machine this value is always true.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6139",
                browseName="ns=woodworking;MachineInitialized",
                description="The MachineInitialized Variable is true if MachineOn is true, the PLC and the control processes are running. The machine is ready for usage for the operator.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6140",
                browseName="ns=woodworking;PowerPresent",
                description="The PowerPresent Variable is true if the power supply is present (the drives are ready to move).",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6141",
                browseName="ns=woodworking;AirPresent",
                description="The AirPresent Variable is true if the air pressure is present in the machine.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6142",
                browseName="ns=woodworking;DustChipSuction",
                description="The DustChipSuction Variable is true if the dust and chip suction is ready.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6143",
                browseName="ns=woodworking;Emergency",
                description="The Emergency Variable is true if at least one emergency button is pressed.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6144",
                browseName="ns=woodworking;Safety",
                description="The Safety Variable is true if at least one safety device (light curtain, safety mat, …) has intervened.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6145",
                browseName="ns=woodworking;Calibrated",
                description="The Calibrated Variable is true if all devices are calibrated.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6146",
                browseName="ns=woodworking;Remote",
                description="The Remote Variable is true if the machine is working with programs sent by the supervisor or other external application.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6147",
                browseName="ns=woodworking;WorkpiecePresent",
                description="The WorkpiecePresent Variable is true if at least one piece is inside the machine.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6148", browseName="ns=woodworking;Moving", description="The Moving Variable is true if at least one axis is moving.", dataType=o6.Boolean
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6149",
                browseName="ns=woodworking;Error",
                description="The Error Variable is true if at least one reason exists which prevents the machine from working.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6150", browseName="ns=woodworking;Alarm", description="The Alarm Variable is true if at least one alarm exists.", dataType=o6.Boolean
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6151", browseName="ns=woodworking;Warning", description="The Warning Variable is true if at least one warning exists.", dataType=o6.Boolean
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6152",
                browseName="ns=woodworking;Hold",
                description="The Hold Variable is true if the movements are paused by the operator.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6153",
                browseName="ns=woodworking;RecipeInRun",
                description="The RecipeInRun Variable is true if the machine runs its program. However, if the machine is paused by the program, the machine is considered to still be running its program, i.e. while the RecipeInHold Variable is true, the RecipeInRun cannot be false.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6154",
                browseName="ns=woodworking;RecipeInSetup",
                description="The RecipeInSetup Variable is true if the RecipeInRun is true and the machine is in the setup phase (example: automatic tool change).",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6155",
                browseName="ns=woodworking;RecipeInHold",
                description="The RecipeInHold Variable is true if the machine is paused by the program. This is only possible if the RecipeInRun Variable is also true.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6156",
                browseName="ns=woodworking;ManualActivityRequired",
                description="The ManualActivityRequired Variable is true if a manual activity by the operator is required. The RecipeInRun is not affected.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6157",
                browseName="ns=woodworking;LoadingEnabled",
                description="The LoadingEnabled Variable is true if the unit is ready to get the next new part. If this is false no part can get into the unit.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6158",
                browseName="ns=woodworking;WaitUnload",
                description="The WaitUnload Variable is true if the machine is waiting to unload pieces.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6159",
                browseName="ns=woodworking;WaitLoad",
                description="The WaitLoad Variable is true if the machine is waiting for pieces.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6160",
                browseName="ns=woodworking;EnergySaving",
                description="The EnergySaving Variable is true if energy saving is activated on the machine.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6161",
                browseName="ns=woodworking;ExternalEmergency",
                description="The ExternalEmergency Variable is true if there is an emergency from the line controller.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6162",
                browseName="ns=woodworking;MaintenanceRequired",
                description="The MaintenanceRequired Variable is true if maintenance is required.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6163",
                browseName="ns=woodworking;FeedRuns",
                description="The FeedRuns Variable is true if the feed is running on a throughfeed machine.",
                dataType=o6.Boolean,
            )
        ),
    ],
)
o6.reference(o6.ns["ns=woodworking;i=5017"], "i=17603", woodworking_objtypes.IWwUnitFlagsType)
ns0.objtypes.BaseObjectType(
    nodeId="ns=woodworking;i=5020",
    browseName="ns=woodworking;Overview",
    description="The Overview Object provides a general state of the unit.",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6207",
                browseName="ns=woodworking;CurrentState",
                description="The CurrentState Variable provides the generalized state of the unit.",
                dataType=woodworking_datypes.WwUnitStateEnumeration,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6208",
                browseName="ns=woodworking;CurrentMode",
                description="The CurrentMode Variable provides the generalized mode of the unit.",
                dataType=woodworking_datypes.WwUnitModeEnumeration,
            )
        ),
    ],
)
o6.reference(o6.ns["ns=woodworking;i=5020"], "i=17603", woodworking_objtypes.IWwUnitOverviewType)
ns0.objtypes.BaseObjectType(
    nodeId="ns=woodworking;i=5022",
    browseName="ns=woodworking;Flags",
    description="The Flags Object provides the flags of the unit.",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6209",
                browseName="ns=woodworking;MachineOn",
                description="The MachineOn Variable is true if the machine is switched on. If the OPC UA Server runs on the machine this value is always true.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6210",
                browseName="ns=woodworking;MachineInitialized",
                description="The MachineInitialized Variable is true if MachineOn is true, the PLC and the control processes are running. The machine is ready for usage for the operator.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6211",
                browseName="ns=woodworking;PowerPresent",
                description="The PowerPresent Variable is true if the power supply is present (the drives are ready to move).",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6212",
                browseName="ns=woodworking;AirPresent",
                description="The AirPresent Variable is true if the air pressure is present in the machine.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6213",
                browseName="ns=woodworking;DustChipSuction",
                description="The DustChipSuction Variable is true if the dust and chip suction is ready.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6214",
                browseName="ns=woodworking;Emergency",
                description="The Emergency Variable is true if at least one emergency button is pressed.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6215",
                browseName="ns=woodworking;Safety",
                description="The Safety Variable is true if at least one safety device (light curtain, safety mat, …) has intervened.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6216",
                browseName="ns=woodworking;Calibrated",
                description="The Calibrated Variable is true if all devices are calibrated.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6223",
                browseName="ns=woodworking;Remote",
                description="The Remote Variable is true if the machine is working with programs sent by the supervisor or other external application.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6224",
                browseName="ns=woodworking;WorkpiecePresent",
                description="The WorkpiecePresent Variable is true if at least one piece is inside the machine.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6225", browseName="ns=woodworking;Moving", description="The Moving Variable is true if at least one axis is moving.", dataType=o6.Boolean
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6226",
                browseName="ns=woodworking;Error",
                description="The Error Variable is true if at least one reason exists which prevents the machine from working.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6227", browseName="ns=woodworking;Alarm", description="The Alarm Variable is true if at least one alarm exists.", dataType=o6.Boolean
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6228", browseName="ns=woodworking;Warning", description="The Warning Variable is true if at least one warning exists.", dataType=o6.Boolean
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6229",
                browseName="ns=woodworking;Hold",
                description="The Hold Variable is true if the movements are paused by the operator.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6230",
                browseName="ns=woodworking;RecipeInRun",
                description="The RecipeInRun Variable is true if the machine runs its program. However, if the machine is paused by the program, the machine is considered to still be running its program, i.e. while the RecipeInHold Variable is true, the RecipeInRun cannot be false.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6231",
                browseName="ns=woodworking;RecipeInSetup",
                description="The RecipeInSetup Variable is true if the RecipeInRun is true and the machine is in the setup phase (example: automatic tool change).",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6233",
                browseName="ns=woodworking;RecipeInHold",
                description="The RecipeInHold Variable is true if the machine is paused by the program. This is only possible if the RecipeInRun Variable is also true.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6234",
                browseName="ns=woodworking;ManualActivityRequired",
                description="The ManualActivityRequired Variable is true if a manual activity by the operator is required. The RecipeInRun is not affected.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6235",
                browseName="ns=woodworking;LoadingEnabled",
                description="The LoadingEnabled Variable is true if the unit is ready to get the next new part. If this is false no part can get into the unit.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6236",
                browseName="ns=woodworking;WaitUnload",
                description="The WaitUnload Variable is true if the machine is waiting to unload pieces.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6237",
                browseName="ns=woodworking;WaitLoad",
                description="The WaitLoad Variable is true if the machine is waiting for pieces.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6238",
                browseName="ns=woodworking;EnergySaving",
                description="The EnergySaving Variable is true if energy saving is activated on the machine.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6239",
                browseName="ns=woodworking;ExternalEmergency",
                description="The ExternalEmergency Variable is true if there is an emergency from the line controller.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6240",
                browseName="ns=woodworking;MaintenanceRequired",
                description="The MaintenanceRequired Variable is true if maintenance is required.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6241",
                browseName="ns=woodworking;FeedRuns",
                description="The FeedRuns Variable is true if the feed is running on a throughfeed machine.",
                dataType=o6.Boolean,
            )
        ),
    ],
)
o6.reference(o6.ns["ns=woodworking;i=5022"], "i=17603", woodworking_objtypes.IWwUnitFlagsType)
ns0.objtypes.BaseObjectType(
    nodeId="ns=woodworking;i=5023",
    browseName="ns=woodworking;Overview",
    description="The Overview Object provides a general overview of the unit.",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6248",
                browseName="ns=woodworking;CurrentMode",
                description="The CurrentMode Variable provides the generalized mode of the unit.",
                dataType=woodworking_datypes.WwUnitModeEnumeration,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6249",
                browseName="ns=woodworking;CurrentState",
                description="The CurrentState Variable provides the generalized state of the unit.",
                dataType=woodworking_datypes.WwUnitStateEnumeration,
            )
        ),
    ],
)
o6.reference(o6.ns["ns=woodworking;i=5023"], "i=17603", woodworking_objtypes.IWwUnitOverviewType)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=woodworking;i=6250",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6251", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
machinery.objtypes.MachineryItemState_StateMachineType(
    nodeId="ns=woodworking;i=5019", browseName="ns=machinery;MachineryItemState", references=[o6.hasComponent(o6.ns["ns=woodworking;i=6250"])]
)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=woodworking;i=6252",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6253", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
machinery.objtypes.MachineryOperationModeStateMachineType(
    nodeId="ns=woodworking;i=5025", browseName="ns=machinery;MachineryOperationMode", references=[o6.hasComponent(o6.ns["ns=woodworking;i=6252"])]
)
ns0.objtypes.FolderType(
    nodeId="ns=woodworking;i=5005",
    browseName="ns=machinery;MachineryBuildingBlocks",
    modellingRule="Optional",
    references=[o6.hasAddIn(o6.ns["ns=woodworking;i=5019"]), o6.hasAddIn(o6.ns["ns=woodworking;i=5025"])],
)
o6.reference(woodworking_objtypes.WwMachineType, ns0.reftypes.HasComponent, o6.ns["ns=woodworking;i=5005"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=woodworking;i=6259",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6277", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=woodworking;i=5026",
    browseName="ns=woodworking;Flags",
    description="The Flags Object provides the flags of the unit.",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6298",
                browseName="ns=woodworking;MachineOn",
                description="The MachineOn Variable is true if the machine is switched on. If the OPC UA Server runs on the machine this value is always true.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6299",
                browseName="ns=woodworking;MachineInitialized",
                description="The MachineInitialized Variable is true if the MachineOn is true, the PLC and the control processes are running. The machine is ready for usage for the operator.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6300",
                browseName="ns=woodworking;PowerPresent",
                description="The PowerPresent Variable is true if the power supply is present (the drives are ready to move).",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6301",
                browseName="ns=woodworking;AirPresent",
                description="The AirPresent Variable is true if the air pressure is present in the machine.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6302",
                browseName="ns=woodworking;DustChipSuction",
                description="The DustChipSuction Variable is true if the dust and chip suction is ready.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6303",
                browseName="ns=woodworking;Emergency",
                description="The Emergency Variable is true if at least one emergency button is pressed.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6304",
                browseName="ns=woodworking;Safety",
                description="The Emergency Variable is true if at least one emergency button is pressed.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6305",
                browseName="ns=woodworking;Calibrated",
                description="The Calibrated Variable is true if all devices are calibrated.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6306",
                browseName="ns=woodworking;Remote",
                description="The Remote Variable is true if the machine is working with programs sent by the supervisor or other external application.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6307",
                browseName="ns=woodworking;WorkpiecePresent",
                description="The WorkpiecePresent Variable is true if at least one piece is inside the machine.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6308", browseName="ns=woodworking;Moving", description="The Moving Variable is true if at least one axis is moving.", dataType=o6.Boolean
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6309",
                browseName="ns=woodworking;Error",
                description="The Error Variable is true if at least one reason exists which prevents the machine from working.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6310", browseName="ns=woodworking;Alarm", description="The Alarm Variable is true if at least one alarm exists.", dataType=o6.Boolean
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6311", browseName="ns=woodworking;Warning", description="The Warning Variable is true if at least one warning exists.", dataType=o6.Boolean
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6312",
                browseName="ns=woodworking;Hold",
                description="The Hold Variable is true if the movements are paused by the operator.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6313",
                browseName="ns=woodworking;RecipeInRun",
                description="The RecipeInRun Variable is true if the machine runs its program. However, if the machine is paused by the program, the machine is considered to still be running its program, i.e. while the RecipeInHold Variable is true, the RecipeInRun cannot be false.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6314",
                browseName="ns=woodworking;RecipeInSetup",
                description="The RecipeInSetup Variable is true if the RecipeInRun is true and the machine is in the setup phase (example: automatic tool change).",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6315",
                browseName="ns=woodworking;RecipeInHold",
                description="The RecipeInHold Variable is true if the machine is paused by the program. This is only possible if the RecipeInRun Variable is also true.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6316",
                browseName="ns=woodworking;ManualActivityRequired",
                description="The ManualActivityRequired Variable is true if a manual activity by the operator is required. The RecipeInRun is not affected.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6317",
                browseName="ns=woodworking;LoadingEnabled",
                description="The LoadingEnabled Variable is true if the unit is ready to get the next new part. If this is false no part can get into the unit.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6318",
                browseName="ns=woodworking;WaitUnload",
                description="The WaitUnload Variable is true if the machine is waiting to unload pieces.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6319",
                browseName="ns=woodworking;WaitLoad",
                description="The WaitLoad Variable is true if the machine is waiting for pieces.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6320",
                browseName="ns=woodworking;EnergySaving",
                description="The EnergySaving Variable is true if energy saving is activated on the machine.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6321",
                browseName="ns=woodworking;ExternalEmergency",
                description="The ExternalEmergency Variable is true if there is an emergency from the line controller.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6322",
                browseName="ns=woodworking;MaintenanceRequired",
                description="The MaintenanceRequired Variable is true if maintenance is required.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6323",
                browseName="ns=woodworking;FeedRuns",
                description="The FeedRuns Variable is true if the feed is running on a throughfeed machine.",
                dataType=o6.Boolean,
            )
        ),
    ],
)
o6.reference(o6.ns["ns=woodworking;i=5026"], "i=17603", woodworking_objtypes.IWwUnitFlagsType)
ns0.objtypes.BaseObjectType(
    nodeId="ns=woodworking;i=5027",
    browseName="ns=woodworking;Overview",
    description="The Overview Object provides a general overview of the unit.",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6324",
                browseName="ns=woodworking;CurrentMode",
                description="The CurrentMode Variable provides the generalized mode of the unit.",
                dataType=woodworking_datypes.WwUnitModeEnumeration,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6325",
                browseName="ns=woodworking;CurrentState",
                description="The CurrentState Variable provides the generalized state of the unit.",
                dataType=woodworking_datypes.WwUnitStateEnumeration,
            )
        ),
    ],
)
o6.reference(o6.ns["ns=woodworking;i=5027"], "i=17603", woodworking_objtypes.IWwUnitOverviewType)
isa95_jobcontrol_v2.objtypes.ISA95JobOrderReceiverObjectType(
    nodeId="ns=woodworking;i=5034",
    browseName="ns=machinery_jobs;JobOrderControl",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6282", browseName="ns=isa95_jobcontrol_v2;MaxDownloadableJobOrders", dataType=o6.UInt16)),
        o6.hasComponent(o6.ns["ns=woodworking;i=6259"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6278",
                browseName="ns=isa95_jobcontrol_v2;EquipmentID",
                description="Defines a read-only set of Equipment Class IDs and Equipment IDs that may be specified in a job order.",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6279",
                browseName="ns=isa95_jobcontrol_v2;JobOrderList",
                description="Defines a read-only list of job order information available from the server.",
                dataType=isa95_jobcontrol_v2.datatypes.ISA95JobOrderAndStateDataType,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6280",
                browseName="ns=isa95_jobcontrol_v2;MaterialClassID",
                description="Defines a read-only set of Material Classes IDs that may be specified in a job order.",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6281",
                browseName="ns=isa95_jobcontrol_v2;MaterialDefinitionID",
                description="Defines a read-only set of Material Classes IDs that may be specified in a job order.",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6283",
                browseName="ns=isa95_jobcontrol_v2;PersonnelID",
                description="Defines a read-only set of Personnel IDs and Person IDs that may be specified in a job order.",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6284",
                browseName="ns=isa95_jobcontrol_v2;PhysicalAssetID",
                description="Defines a read-only set of Physical Asset Class IDs and Physical Asset IDs that may be specified in a job order.",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6326",
                browseName="ns=isa95_jobcontrol_v2;WorkMaster",
                description="Defines a read-only set of work master IDs that may be specified in a job order, and the read-only set of parameters that may be specified for a specific work master.",
                dataType=isa95_jobcontrol_v2.datatypes.ISA95WorkMasterDataType,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
    ],
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=woodworking;i=5032",
    browseName="ns=woodworking;Flags",
    description="The Flags Object provides the flags of the unit.",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6366",
                browseName="ns=woodworking;MachineOn",
                description="The MachineOn Variable is true if the machine is switched on. If the OPC UA Server runs on the machine this value is always true.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6367",
                browseName="ns=woodworking;MachineInitialized",
                description="The MachineInitialized Variable is true if the MachineOn is true, the PLC and the control processes are running. The machine is ready for usage for the operator.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6368",
                browseName="ns=woodworking;PowerPresent",
                description="The PowerPresent Variable is true if the power supply is present (the drives are ready to move).",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6369",
                browseName="ns=woodworking;AirPresent",
                description="The AirPresent Variable is true if the air pressure is present in the machine.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6370",
                browseName="ns=woodworking;DustChipSuction",
                description="The DustChipSuction Variable is true if the dust and chip suction is ready.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6371",
                browseName="ns=woodworking;Emergency",
                description="The Emergency Variable is true if at least one emergency button is pressed.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6372",
                browseName="ns=woodworking;Safety",
                description="The Safety Variable is true if at least one safety device (light curtain, safety mat, …) has intervened.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6373",
                browseName="ns=woodworking;Calibrated",
                description="The Calibrated Variable is true if all devices are calibrated.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6374",
                browseName="ns=woodworking;Remote",
                description="The Remote Variable is true if the machine is working with programs sent by the supervisor or other external application.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6375",
                browseName="ns=woodworking;WorkpiecePresent",
                description="The WorkpiecePresent Variable is true if at least one piece is inside the machine.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6376", browseName="ns=woodworking;Moving", description="The Moving Variable is true if at least one axis is moving.", dataType=o6.Boolean
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6377",
                browseName="ns=woodworking;Error",
                description="The Error Variable is true if at least one reason exists which prevents the machine from working.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6378", browseName="ns=woodworking;Alarm", description="The Alarm Variable is true if at least one alarm exists.", dataType=o6.Boolean
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6379", browseName="ns=woodworking;Warning", description="The Warning Variable is true if at least one warning exists.", dataType=o6.Boolean
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6380",
                browseName="ns=woodworking;Hold",
                description="The Hold Variable is true if the movements are paused by the operator.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6381",
                browseName="ns=woodworking;RecipeInRun",
                description="The RecipeInRun Variable is true if the machine runs its program. However, if the machine is paused by the program, the machine is considered to still be running its program, i.e. while the RecipeInHold Variable is true, the RecipeInRun cannot be false.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6382",
                browseName="ns=woodworking;RecipeInSetup",
                description="The RecipeInSetup Variable is true if the RecipeInRun is true and the machine is in the setup phase (example: automatic tool change).",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6383",
                browseName="ns=woodworking;RecipeInHold",
                description="The RecipeInHold Variable is true if the machine is paused by the program. This is only possible if the RecipeInRun Variable is also true.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6384",
                browseName="ns=woodworking;ManualActivityRequired",
                description="The ManualActivityRequired Variable is true if a manual activity by the operator is required. The RecipeInRun is not affected.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6385",
                browseName="ns=woodworking;LoadingEnabled",
                description="The LoadingEnabled Variable is true if the unit is ready to get the next new part. If this is false no part can get into the unit.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6386",
                browseName="ns=woodworking;WaitUnload",
                description="The WaitUnload Variable is true if the machine is waiting to unload pieces.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6387",
                browseName="ns=woodworking;WaitLoad",
                description="The WaitLoad Variable is true if the machine is waiting for pieces.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6388",
                browseName="ns=woodworking;EnergySaving",
                description="The EnergySaving Variable is true if energy saving is activated on the machine.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6389",
                browseName="ns=woodworking;ExternalEmergency",
                description="The ExternalEmergency Variable is true if there is an emergency from the line controller.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6390",
                browseName="ns=woodworking;MaintenanceRequired",
                description="The MaintenanceRequired Variable is true if maintenance is required.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6391",
                browseName="ns=woodworking;FeedRuns",
                description="The FeedRuns Variable is true if the feed is running on a throughfeed machine.",
                dataType=o6.Boolean,
            )
        ),
    ],
)
o6.reference(o6.ns["ns=woodworking;i=5032"], "i=17603", woodworking_objtypes.IWwUnitFlagsType)
ns0.objtypes.BaseObjectType(
    nodeId="ns=woodworking;i=5033",
    browseName="ns=woodworking;Overview",
    description="The Overview Object provides a general overview of the unit.",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6392",
                browseName="ns=woodworking;CurrentState",
                description="The CurrentState Variable provides the generalized state of the unit.",
                dataType=woodworking_datypes.WwUnitStateEnumeration,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6393",
                browseName="ns=woodworking;CurrentMode",
                description="The CurrentMode Variable provides the generalized mode of the unit.",
                dataType=woodworking_datypes.WwUnitModeEnumeration,
            )
        ),
    ],
)
o6.reference(o6.ns["ns=woodworking;i=5033"], "i=17603", woodworking_objtypes.IWwUnitOverviewType)
ns0.objtypes.BaseObjectType(
    nodeId="ns=woodworking;i=5037",
    browseName="ns=woodworking;Flags",
    description="The Flags Object provides the flags of the unit.",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6434",
                browseName="ns=woodworking;MachineOn",
                description="The MachineOn Variable is true if the machine is switched on. If the OPC UA Server runs on the machine this value is always true.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6435",
                browseName="ns=woodworking;MachineInitialized",
                description="The MachineInitialized Variable is true if the MachineOn is true, the PLC and the control processes are running. The machine is ready for usage for the operator.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6436",
                browseName="ns=woodworking;PowerPresent",
                description="The PowerPresent Variable is true if the power supply is present (the drives are ready to move).",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6437",
                browseName="ns=woodworking;AirPresent",
                description="The AirPresent Variable is true if the air pressure is present in the machine.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6438",
                browseName="ns=woodworking;DustChipSuction",
                description="The DustChipSuction Variable is true if the dust and chip suction is ready.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6439",
                browseName="ns=woodworking;Emergency",
                description="The Emergency Variable is true if at least one emergency button is pressed.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6440",
                browseName="ns=woodworking;Safety",
                description="The Safety Variable is true if at least one safety device (light curtain, safety mat, …) has intervened.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6441",
                browseName="ns=woodworking;Calibrated",
                description="The Calibrated Variable is true if all devices are calibrated.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6442",
                browseName="ns=woodworking;Remote",
                description="The Remote Variable is true if the machine is working with programs sent by the supervisor or other external application.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6443",
                browseName="ns=woodworking;WorkpiecePresent",
                description="The WorkpiecePresent Variable is true if at least one piece is inside the machine.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6444", browseName="ns=woodworking;Moving", description="The Moving Variable is true if at least one axis is moving.", dataType=o6.Boolean
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6445",
                browseName="ns=woodworking;Error",
                description="The Error Variable is true if at least one reason exists which prevents the machine from working.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6446", browseName="ns=woodworking;Alarm", description="The Alarm Variable is true if at least one alarm exists.", dataType=o6.Boolean
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6447", browseName="ns=woodworking;Warning", description="The Warning Variable is true if at least one warning exists.", dataType=o6.Boolean
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6448",
                browseName="ns=woodworking;Hold",
                description="The Hold Variable is true if the movements are paused by the operator.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6449",
                browseName="ns=woodworking;RecipeInRun",
                description="The RecipeInRun Variable is true if the machine runs its program. However, if the machine is paused by the program, the machine is considered to still be running its program, i.e. while the RecipeInHold Variable is true, the RecipeInRun cannot be false.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6450",
                browseName="ns=woodworking;RecipeInSetup",
                description="The RecipeInSetup Variable is true if the RecipeInRun is true and the machine is in the setup phase (example: automatic tool change).",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6451",
                browseName="ns=woodworking;RecipeInHold",
                description="The RecipeInHold Variable is true if the machine is paused by the program. This is only possible if the RecipeInRun Variable is also true.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6452",
                browseName="ns=woodworking;ManualActivityRequired",
                description="The ManualActivityRequired Variable is true if a manual activity by the operator is required. The RecipeInRun is not affected.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6453",
                browseName="ns=woodworking;LoadingEnabled",
                description="The LoadingEnabled Variable is true if the unit is ready to get the next new part. If this is false no part can get into the unit.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6454",
                browseName="ns=woodworking;WaitUnload",
                description="The WaitUnload Variable is true if the machine is waiting to unload pieces.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6455",
                browseName="ns=woodworking;WaitLoad",
                description="The WaitLoad Variable is true if the machine is waiting for pieces.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6456",
                browseName="ns=woodworking;EnergySaving",
                description="The EnergySaving Variable is true if energy saving is activated on the machine.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6457",
                browseName="ns=woodworking;ExternalEmergency",
                description="The ExternalEmergency Variable is true if there is an emergency from the line controller.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6458",
                browseName="ns=woodworking;MaintenanceRequired",
                description="The MaintenanceRequired Variable is true if maintenance is required.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6459",
                browseName="ns=woodworking;FeedRuns",
                description="The FeedRuns Variable is true if the feed is running on a throughfeed machine.",
                dataType=o6.Boolean,
            )
        ),
    ],
)
o6.reference(o6.ns["ns=woodworking;i=5037"], "i=17603", woodworking_objtypes.IWwUnitFlagsType)
ns0.objtypes.BaseObjectType(
    nodeId="ns=woodworking;i=5038",
    browseName="ns=woodworking;Overview",
    description="The Overview Object provides a general overview of the unit.",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6460",
                browseName="ns=woodworking;CurrentState",
                description="The CurrentState Variable provides the generalized state of the unit.",
                dataType=woodworking_datypes.WwUnitStateEnumeration,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=woodworking;i=6461",
                browseName="ns=woodworking;CurrentMode",
                description="The CurrentMode Variable provides the generalized mode of the unit.",
                dataType=woodworking_datypes.WwUnitModeEnumeration,
            )
        ),
    ],
)
o6.reference(o6.ns["ns=woodworking;i=5038"], "i=17603", woodworking_objtypes.IWwUnitOverviewType)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6034",
    browseName="ns=woodworking;AbsoluteErrorTime",
    description="The AbsoluteErrorTime Variable provides the absolute time in msec of the ERROR_4 state in msec.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6540", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6541", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6542", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6543", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6544", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
o6.reference(woodworking_objtypes.IWwUnitValuesType, ns0.reftypes.HasComponent, o6.ns["ns=woodworking;i=6034"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6035",
    browseName="ns=woodworking;AbsoluteLength",
    description="The AbsoluteLength Variable provides the absolute produced length in mm.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6545", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6546", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6547", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6548", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6549", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
o6.reference(woodworking_objtypes.IWwUnitValuesType, ns0.reftypes.HasComponent, o6.ns["ns=woodworking;i=6035"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6036",
    browseName="ns=woodworking;AbsoluteMachineOnTime",
    description="The AbsoluteMachineOnTime Variable provides the absolute time in msec the machine is turned on based on the MachineOn state.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6550", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6551", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6552", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6553", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6554", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
o6.reference(woodworking_objtypes.IWwUnitValuesType, ns0.reftypes.HasComponent, o6.ns["ns=woodworking;i=6036"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6037",
    browseName="ns=woodworking;AbsoluteMachineOffTime",
    description="The AbsoluteOfflineTime can be calculated by the machine. The shutdown time and the starting time have to be stored on the machine.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6555", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6556", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6557", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6558", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6559", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
o6.reference(woodworking_objtypes.IWwUnitValuesType, ns0.reftypes.HasComponent, o6.ns["ns=woodworking;i=6037"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6038",
    browseName="ns=woodworking;AbsolutePiecesIn",
    description="The AbsolutePiecesIn Variable provides the absolute count of pieces which came into the machine.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6560", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6561", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6562", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6563", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6564", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
o6.reference(woodworking_objtypes.IWwUnitValuesType, ns0.reftypes.HasComponent, o6.ns["ns=woodworking;i=6038"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6039",
    browseName="ns=woodworking;AbsolutePiecesOut",
    description="The AbsolutePiecesOut Variable provides the absolute count of pieces which came out of the machine.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6565", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6566", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6567", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6568", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6569", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
o6.reference(woodworking_objtypes.IWwUnitValuesType, ns0.reftypes.HasComponent, o6.ns["ns=woodworking;i=6039"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6040",
    browseName="ns=woodworking;AbsolutePowerPresentTime",
    description="The AbsolutePowerPresentTime Variable provides the absolute time in msec the machine has power on based on the PowerPresent state.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6570", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6571", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6572", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6573", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6574", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
o6.reference(woodworking_objtypes.IWwUnitValuesType, ns0.reftypes.HasComponent, o6.ns["ns=woodworking;i=6040"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6041",
    browseName="ns=woodworking;AbsoluteProductionTime",
    description="The AbsoluteProductionTime Variable provides the absolute time in msec of the machine is working at least with one workpiece based on the RecipeInRun and PiecesPresent state.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6575", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6576", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6577", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6578", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6579", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
o6.reference(woodworking_objtypes.IWwUnitValuesType, ns0.reftypes.HasComponent, o6.ns["ns=woodworking;i=6041"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6042",
    browseName="ns=woodworking;AbsoluteProductionWaitWorkpieceTime",
    description="The AbsoluteProductionWaitWorkpieceTime Variable provides the absolute time in msec of the machine is in working mode, bring the consent out to insert workpiece but no workpiece incoming from the previous machine based on the ReceipeInRun and WaitLoad state.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6580", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6581", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6582", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6583", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6584", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
o6.reference(woodworking_objtypes.IWwUnitValuesType, ns0.reftypes.HasComponent, o6.ns["ns=woodworking;i=6042"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6043",
    browseName="ns=woodworking;AbsoluteProductionWithoutWorkpieceTime",
    description="The AbsoluteProductionWithoutWorkpieceTime Variable provides the absolute time in msec of the machine is working but without workpieces inside based on the RecipeInRun and !PiecesPresent state.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6585", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6586", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6587", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6588", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6589", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
o6.reference(woodworking_objtypes.IWwUnitValuesType, ns0.reftypes.HasComponent, o6.ns["ns=woodworking;i=6043"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6044",
    browseName="ns=woodworking;AbsoluteReadyTime",
    description="The AbsoluteReadyTime Variable provides the absolute time in msec of the READY_2 state in msec.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6590", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6591", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6592", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6593", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6594", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
o6.reference(woodworking_objtypes.IWwUnitValuesType, ns0.reftypes.HasComponent, o6.ns["ns=woodworking;i=6044"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6045",
    browseName="ns=woodworking;AbsoluteRunsAborted",
    description="The AbsoluteRunsAborted Variable provides the absolute count of aborted runs.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6595", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6596", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6597", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6598", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6599", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
o6.reference(woodworking_objtypes.IWwUnitValuesType, ns0.reftypes.HasComponent, o6.ns["ns=woodworking;i=6045"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6046",
    browseName="ns=woodworking;AbsoluteRunsGood",
    description="The AbsoluteRunsGood Variable provides the absolute count of finished runs.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6600", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6601", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6602", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6603", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6604", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
o6.reference(woodworking_objtypes.IWwUnitValuesType, ns0.reftypes.HasComponent, o6.ns["ns=woodworking;i=6046"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6047",
    browseName="ns=woodworking;AbsoluteRunsTotal",
    description="The AbsoluteRunsTotal Variable provides the absolute count of total runs.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6605", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6606", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6607", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6608", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6609", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
o6.reference(woodworking_objtypes.IWwUnitValuesType, ns0.reftypes.HasComponent, o6.ns["ns=woodworking;i=6047"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6048",
    browseName="ns=woodworking;AbsoluteStandbyTime",
    description="The AbsoluteStandbyTime Variable provides the absolute time in msec of the STANDBY_1 state in msec.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6610", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6611", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6612", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6613", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6614", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
o6.reference(woodworking_objtypes.IWwUnitValuesType, ns0.reftypes.HasComponent, o6.ns["ns=woodworking;i=6048"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6049",
    browseName="ns=woodworking;AbsoluteWorkingTime",
    description="The AbsoluteWorkingTime Variable provides the absolute time in msec of the WORKING_3 state in msec.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6615", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6616", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6617", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6618", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6619", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
o6.reference(woodworking_objtypes.IWwUnitValuesType, ns0.reftypes.HasComponent, o6.ns["ns=woodworking;i=6049"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6050",
    browseName="ns=woodworking;ActualCycle",
    description="The ActualCycle Variable provides the parts per minutes.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6620", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6621", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6622", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6623", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6624", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
o6.reference(woodworking_objtypes.IWwUnitValuesType, ns0.reftypes.HasComponent, o6.ns["ns=woodworking;i=6050"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6051",
    browseName="ns=woodworking;AxisOverride",
    description="The AxisOverride Variable provides the override for the axis in percent.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6625", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6626", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6627", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6628", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6629", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt32,
)
o6.reference(woodworking_objtypes.IWwUnitValuesType, ns0.reftypes.HasComponent, o6.ns["ns=woodworking;i=6051"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6052",
    browseName="ns=woodworking;FeedSpeed",
    description="The FeedSpeed Variable provides the feed speed in m/min for throughfeed machines.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6630", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6631", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6632", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6633", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6634", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
o6.reference(woodworking_objtypes.IWwUnitValuesType, ns0.reftypes.HasComponent, o6.ns["ns=woodworking;i=6052"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6053",
    browseName="ns=woodworking;RelativeErrorTime",
    description="The RelativeErrorTime Variable provides the relative time since startup of the ERROR_4 state in msec.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6635", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6636", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6637", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6638", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6639", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
o6.reference(woodworking_objtypes.IWwUnitValuesType, ns0.reftypes.HasComponent, o6.ns["ns=woodworking;i=6053"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6054",
    browseName="ns=woodworking;RelativeLength",
    description="The RelativeLength Variable provides the relative produced length in mm since the machine has started.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6640", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6641", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6642", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6643", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6644", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
o6.reference(woodworking_objtypes.IWwUnitValuesType, ns0.reftypes.HasComponent, o6.ns["ns=woodworking;i=6054"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6055",
    browseName="ns=woodworking;RelativeMachineOnTime",
    description="The RelativeMachineOnTime Variable provides the relative time in msec since startup the machine is turned on based on the MachineOn state.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6645", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6646", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6647", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6648", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6649", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
o6.reference(woodworking_objtypes.IWwUnitValuesType, ns0.reftypes.HasComponent, o6.ns["ns=woodworking;i=6055"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6057",
    browseName="ns=woodworking;RelativePiecesIn",
    description="The RelativePiecesIn Variable provides the relative count of pieces which came into the machine since the machine has started.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6655", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6656", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6657", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6658", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6659", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
o6.reference(woodworking_objtypes.IWwUnitValuesType, ns0.reftypes.HasComponent, o6.ns["ns=woodworking;i=6057"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6058",
    browseName="ns=woodworking;RelativePiecesOut",
    description="The RelativePiecesOut Variable provides the relative count of pieces which came out of the machine since the machine has started.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6660", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6661", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6662", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6663", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6664", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
o6.reference(woodworking_objtypes.IWwUnitValuesType, ns0.reftypes.HasComponent, o6.ns["ns=woodworking;i=6058"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6059",
    browseName="ns=woodworking;RelativePowerPresentTime",
    description="The RelativePowerPresentTime Variable provides the relative time in msec since startup the machine has power on based on the PowerPresent state.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6665", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6666", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6667", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6668", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6669", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
o6.reference(woodworking_objtypes.IWwUnitValuesType, ns0.reftypes.HasComponent, o6.ns["ns=woodworking;i=6059"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6060",
    browseName="ns=woodworking;RelativeProductionTime",
    description="The RelativeProductionTime Variable provides the relative time in msec since startup of the machine is working at least with one workpiece based on the RecipeInRun and PiecesPresent state.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6670", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6671", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6672", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6673", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6674", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
o6.reference(woodworking_objtypes.IWwUnitValuesType, ns0.reftypes.HasComponent, o6.ns["ns=woodworking;i=6060"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6061",
    browseName="ns=woodworking;RelativeProductionWaitWorkpieceTime",
    description="The RelativeProductionWaitWorkpieceTime Variable provides the relative time in msec waiting for workpieces since startup of the machine is in working mode, bring the consent out to insert workpiece but no workpiece incoming from the previous machine based on the ReceipeInRun and WaitLoad state.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6675", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6676", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6677", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6678", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6679", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
o6.reference(woodworking_objtypes.IWwUnitValuesType, ns0.reftypes.HasComponent, o6.ns["ns=woodworking;i=6061"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6062",
    browseName="ns=woodworking;RelativeProductionWithoutWorkpieceTime",
    description="The RelativeProductionWithoutWorkpieceTime Variable provides the relative time in msec since startup of the machine is working but without workpieces inside based on the RecipeInRun and !PiecesPresent state.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6680", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6681", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6682", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6683", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6684", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
o6.reference(woodworking_objtypes.IWwUnitValuesType, ns0.reftypes.HasComponent, o6.ns["ns=woodworking;i=6062"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6063",
    browseName="ns=woodworking;RelativeReadyTime",
    description="The RelativeReadyTime Variable provides the relative time since startup of the READY_2 state in msec.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6685", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6686", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6687", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6688", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6689", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
o6.reference(woodworking_objtypes.IWwUnitValuesType, ns0.reftypes.HasComponent, o6.ns["ns=woodworking;i=6063"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6064",
    browseName="ns=woodworking;RelativeRunsAborted",
    description="The RelativeRunsAborted Variable provides the relative count of aborted runs since the machine has started.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6690", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6691", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6692", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6693", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6694", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
o6.reference(woodworking_objtypes.IWwUnitValuesType, ns0.reftypes.HasComponent, o6.ns["ns=woodworking;i=6064"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6065",
    browseName="ns=woodworking;RelativeRunsGood",
    description="The RelativeRunsGood Variable provides the relative count of finished runs since the machine has started.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6695", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6696", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6697", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6698", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6699", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
o6.reference(woodworking_objtypes.IWwUnitValuesType, ns0.reftypes.HasComponent, o6.ns["ns=woodworking;i=6065"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6066",
    browseName="ns=woodworking;RelativeRunsTotal",
    description="The RelativeRunsTotal Variable provides the relative count of total runs since the machine has started.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6700", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6701", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6702", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6703", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6704", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
o6.reference(woodworking_objtypes.IWwUnitValuesType, ns0.reftypes.HasComponent, o6.ns["ns=woodworking;i=6066"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6067",
    browseName="ns=woodworking;RelativeStandbyTime",
    description="The RelativeStandbyTime Variable provides the relative time since startup of the STANDBY_1 state in msec.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6705", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6706", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6707", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6708", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6709", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
o6.reference(woodworking_objtypes.IWwUnitValuesType, ns0.reftypes.HasComponent, o6.ns["ns=woodworking;i=6067"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6068",
    browseName="ns=woodworking;RelativeWorkingTime",
    description="The RelativeWorkingTime Variable provides the relative time since startup of the WORKING_3 state in msec.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6710", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6711", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6712", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6713", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6714", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
o6.reference(woodworking_objtypes.IWwUnitValuesType, ns0.reftypes.HasComponent, o6.ns["ns=woodworking;i=6068"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6069",
    browseName="ns=woodworking;SpindleOverride",
    description="The SpindleOverride Variable provides the override for the spindle in percent.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6715", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6716", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6717", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6718", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6719", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt32,
)
o6.reference(woodworking_objtypes.IWwUnitValuesType, ns0.reftypes.HasComponent, o6.ns["ns=woodworking;i=6069"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6110",
    browseName="ns=woodworking;AbsoluteErrorTime",
    description="The AbsoluteErrorTime Variable provides the absolute time of the ERROR_4 state in msec.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6720", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6721", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6722", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6723", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6724", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6128",
    browseName="ns=woodworking;AbsoluteLength",
    description="The AbsoluteLength Variable provides the absolute produced length in mm.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6725", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6726", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6727", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6728", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6729", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6112",
    browseName="ns=woodworking;AbsoluteMachineOnTime",
    description="The AbsoluteMachineOnTime Variable provides the absolute time in msec the machine is turned on based on the MachineOn state.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6730", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6731", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6732", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6733", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6734", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6102",
    browseName="ns=woodworking;AbsoluteMachineOffTime",
    description="The AbsoluteOfflineTime can be calculated by the machine. The shutdown time and the starting time have to be stored on the machine.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6735", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6736", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6737", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6738", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6739", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6130",
    browseName="ns=woodworking;AbsolutePiecesIn",
    description="The AbsolutePiecesIn Variable provides the absolute count of pieces which came into the machine.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6740", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6741", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6742", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6743", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6744", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6132",
    browseName="ns=woodworking;AbsolutePiecesOut",
    description="The AbsolutePiecesOut Variable provides the absolute count of pieces which came out of the machine.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6745", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6746", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6747", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6748", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6749", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6114",
    browseName="ns=woodworking;AbsolutePowerPresentTime",
    description="The AbsolutePowerPresentTime Variable provides the absolute time in msec the machine has power on based on the PowerPresent state.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6750", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6751", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6752", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6753", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6754", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6116",
    browseName="ns=woodworking;AbsoluteProductionTime",
    description="The AbsoluteProductionTime Variable provides the absolute time in msec of the machine is working at least with one workpiece based on the RecipeInRun and PiecesPresent state.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6755", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6756", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6757", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6758", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6759", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6120",
    browseName="ns=woodworking;AbsoluteProductionWaitWorkpieceTime",
    description="The AbsoluteProductionWaitWorkpieceTime Variable provides the absolute time in msec of the machine is in working mode, bring the consent out to insert workpiece but no workpiece incoming from the previous machine based on the ReceipeInRun and WaitLoad state.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6760", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6761", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6762", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6763", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6764", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6118",
    browseName="ns=woodworking;AbsoluteProductionWithoutWorkpieceTime",
    description="The AbsoluteProductionWithoutWorkpieceTime Variable provides the absolute time in msec of the machine is working but without workpieces inside based on the RecipeInRun and !PiecesPresent state.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6765", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6766", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6767", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6768", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6769", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6106",
    browseName="ns=woodworking;AbsoluteReadyTime",
    description="The AbsoluteReadyTime Variable provides the absolute time of the READY_2 state in msec.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6770", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6771", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6772", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6773", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6774", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6126",
    browseName="ns=woodworking;AbsoluteRunsAborted",
    description="The AbsoluteRunsAborted Variable provides the absolute count of aborted runs.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6775", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6776", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6777", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6778", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6779", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6122",
    browseName="ns=woodworking;AbsoluteRunsGood",
    description="The AbsoluteRunsGood Variable provides the absolute count of finished runs.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6780", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6781", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6782", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6783", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6784", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6124",
    browseName="ns=woodworking;AbsoluteRunsTotal",
    description="The AbsoluteRunsTotal Variable provides the absolute count of total runs.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6785", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6786", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6787", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6788", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6789", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6104",
    browseName="ns=woodworking;AbsoluteStandbyTime",
    description="The AbsoluteStandbyTime Variable provides the absolute time of the STANDBY_1 state in msec.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6790", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6791", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6792", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6793", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6794", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6108",
    browseName="ns=woodworking;AbsoluteWorkingTime",
    description="The AbsoluteWorkingTime Variable provides the absolute time of the WORKING_3 state in msec.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6795", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6796", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6797", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6798", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6799", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6101",
    browseName="ns=woodworking;ActualCycle",
    description="The ActualCycle Variable provides the parts per minutes.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6800", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6801", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6802", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6803", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6804", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6098",
    browseName="ns=woodworking;AxisOverride",
    description="The AxisOverride Variable provides the override for the axis in percent.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6805", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6806", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6807", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6808", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6809", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt32,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6100",
    browseName="ns=woodworking;FeedSpeed",
    description="The FeedSpeed Variable provides the feed speed in m/min for throughfeed machines.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6810", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6811", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6812", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6813", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6814", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6111",
    browseName="ns=woodworking;RelativeErrorTime",
    description="The RelativeErrorTime Variable provides the relative time since startup of the ERROR_4 state in msec.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6815", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6816", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6817", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6818", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6129",
    browseName="ns=woodworking;RelativeLength",
    description="The RelativeLength Variable provides the relative produced length in mm since the machine has started.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6819", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6820", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6821", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6822", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6823", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6113",
    browseName="ns=woodworking;RelativeMachineOnTime",
    description="The RelativeMachineOnTime Variable provides the relative time in msec since startup the machine is turned on based on the MachineOn state.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6824", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6825", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6826", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6827", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6828", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6131",
    browseName="ns=woodworking;RelativePiecesIn",
    description="The RelativePiecesIn Variable provides the relative count of pieces which came into the machine since the machine has started.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6834", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6835", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6836", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6837", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6838", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6133",
    browseName="ns=woodworking;RelativePiecesOut",
    description="The RelativePiecesOut Variable provides the relative count of pieces which came out of the machine since the machine has started.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6839", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6840", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6841", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6842", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6843", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6115",
    browseName="ns=woodworking;RelativePowerPresentTime",
    description="The RelativePowerPresentTime Variable provides the relative time in msec since startup the machine has power on based on the PowerPresent state.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6844", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6845", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6846", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6847", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6848", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6117",
    browseName="ns=woodworking;RelativeProductionTime",
    description="The RelativeProductionTime Variable provides the relative time in msec since startup of the machine is working at least with one workpiece based on the RecipeInRun and PiecesPresent state.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6849", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6850", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6851", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6852", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6853", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6121",
    browseName="ns=woodworking;RelativeProductionWaitWorkpieceTime",
    description="The RelativeProductionWaitWorkpieceTime Variable provides the relative time in msec waiting for workpieces since startup of the machine is in working mode, bring the consent out to insert workpiece but no workpiece incoming from the previous machine based on the ReceipeInRun and WaitLoad state.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6854", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6855", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6856", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6857", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6858", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6119",
    browseName="ns=woodworking;RelativeProductionWithoutWorkpieceTime",
    description="The RelativeProductionWithoutWorkpieceTime Variable provides the relative time in msec since startup of the machine is working but without workpieces inside based on the RecipeInRun and !PiecesPresent state.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6859", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6860", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6861", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6862", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6863", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6107",
    browseName="ns=woodworking;RelativeReadyTime",
    description="The RelativeReadyTime Variable provides the relative time since startup of the READY_2 state in msec.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6864", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6865", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6866", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6867", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6868", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6127",
    browseName="ns=woodworking;RelativeRunsAborted",
    description="The RelativeRunsAborted Variable provides the relative count of aborted runs since the machine has started.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6869", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6870", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6871", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6872", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6873", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6123",
    browseName="ns=woodworking;RelativeRunsGood",
    description="The RelativeRunsGood Variable provides the relative count of finished runs since the machine has started.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6874", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6875", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6876", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6877", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6878", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6125",
    browseName="ns=woodworking;RelativeRunsTotal",
    description="The RelativeRunsTotal Variable provides the relative count of total runs since the machine has started.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6879", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6880", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6881", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6882", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6883", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6105",
    browseName="ns=woodworking;RelativeStandbyTime",
    description="The RelativeStandbyTime Variable provides the relative time since startup of the STANDBY_1 state in msec.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6884", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6885", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6886", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6887", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6888", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6109",
    browseName="ns=woodworking;RelativeWorkingTime",
    description="The RelativeWorkingTime Variable provides the relative time since startup of the WORKING_3 state in msec.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6889", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6890", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6891", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6892", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6893", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6099",
    browseName="ns=woodworking;SpindleOverride",
    description="The SpindleOverride Variable provides the override for the spindle in percent.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6894", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6895", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6896", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6897", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6898", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt32,
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=woodworking;i=5006",
    browseName="ns=woodworking;Values",
    description="The Values Object provides the counters of the unit.",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=woodworking;i=6098"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6099"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6100"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6101"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6102"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6104"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6105"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6106"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6107"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6108"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6109"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6110"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6111"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6112"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6113"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6114"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6115"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6116"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6117"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6118"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6119"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6120"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6121"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6122"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6123"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6124"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6125"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6126"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6127"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6128"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6129"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6130"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6131"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6132"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6133"]),
    ],
)
o6.reference(woodworking_objtypes.IWwBaseStateType, ns0.reftypes.HasComponent, o6.ns["ns=woodworking;i=5006"])
o6.reference(o6.ns["ns=woodworking;i=5006"], "i=17603", woodworking_objtypes.IWwUnitValuesType)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6176",
    browseName="ns=woodworking;AbsoluteErrorTime",
    description="The AbsoluteErrorTime Variable provides the absolute time of the ERROR_4 state in msec.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6899", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6900", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6901", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6902", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6903", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6197",
    browseName="ns=woodworking;AbsoluteLength",
    description="The AbsoluteLength Variable provides the absolute produced length in mm.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6904", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6905", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6906", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6907", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6908", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6178",
    browseName="ns=woodworking;AbsoluteMachineOnTime",
    description="The AbsoluteMachineOnTime Variable provides the absolute time in msec the machine is turned on based on the MachineOn state.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6909", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6910", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6911", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6912", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6913", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6168",
    browseName="ns=woodworking;AbsoluteMachineOffTime",
    description="The AbsoluteOfflineTime can be calculated by the machine. The shutdown time and the starting time have to be stored on the machine.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6914", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6915", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6916", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6917", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6918", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6199",
    browseName="ns=woodworking;AbsolutePiecesIn",
    description="The AbsolutePiecesIn Variable provides the absolute count of pieces which came into the machine.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6919", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6920", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6921", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6922", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6923", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6201",
    browseName="ns=woodworking;AbsolutePiecesOut",
    description="The AbsolutePiecesOut Variable provides the absolute count of pieces which came out of the machine.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6924", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6925", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6926", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6927", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6928", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6180",
    browseName="ns=woodworking;AbsolutePowerPresentTime",
    description="The AbsolutePowerPresentTime Variable provides the absolute time in msec the machine has power on based on the PowerPresent state.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6929", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6930", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6931", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6932", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6933", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6185",
    browseName="ns=woodworking;AbsoluteProductionTime",
    description="The AbsoluteProductionTime Variable provides the absolute time in msec of the machine is working at least with one workpiece based on the RecipeInRun and PiecesPresent state.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6934", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6935", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6936", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6937", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6938", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6189",
    browseName="ns=woodworking;AbsoluteProductionWaitWorkpieceTime",
    description="The AbsoluteProductionWaitWorkpieceTime Variable provides the absolute time in msec of the machine is in working mode, bring the consent out to insert workpiece but no workpiece incoming from the previous machine based on the ReceipeInRun and WaitLoad state.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6939", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6940", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6941", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6942", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6943", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6187",
    browseName="ns=woodworking;AbsoluteProductionWithoutWorkpieceTime",
    description="The AbsoluteProductionWithoutWorkpieceTime Variable provides the absolute time in msec of the machine is working but without workpieces inside based on the RecipeInRun and !PiecesPresent state.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6944", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6945", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6946", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6947", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6948", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6172",
    browseName="ns=woodworking;AbsoluteReadyTime",
    description="The AbsoluteReadyTime Variable provides the absolute time of the READY_2 state in msec.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6949", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6950", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6951", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6952", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6953", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6195",
    browseName="ns=woodworking;AbsoluteRunsAborted",
    description="The AbsoluteRunsAborted Variable provides the absolute count of aborted runs.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6954", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6955", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6956", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6957", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6958", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6191",
    browseName="ns=woodworking;AbsoluteRunsGood",
    description="The AbsoluteRunsGood Variable provides the absolute count of finished runs.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6959", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6960", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6961", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6962", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6963", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6193",
    browseName="ns=woodworking;AbsoluteRunsTotal",
    description="The AbsoluteRunsTotal Variable provides the absolute count of total runs.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6964", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6965", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6966", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6967", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6968", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6170",
    browseName="ns=woodworking;AbsoluteStandbyTime",
    description="The AbsoluteStandbyTime Variable provides the absolute time of the STANDBY_1 state in msec.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6969", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6970", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6971", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6972", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6973", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6174",
    browseName="ns=woodworking;AbsoluteWorkingTime",
    description="The AbsoluteWorkingTime Variable provides the absolute time of the WORKING_3 state in msec.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6974", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6975", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6976", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6977", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6978", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6167",
    browseName="ns=woodworking;ActualCycle",
    description="The ActualCycle Variable provides the parts per minutes.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6979", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6980", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6981", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6982", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6983", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6164",
    browseName="ns=woodworking;AxisOverride",
    description="The AxisOverride Variable provides the override for the axis in percent.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6984", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6985", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6986", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6987", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6988", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt32,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6166",
    browseName="ns=woodworking;FeedSpeed",
    description="The FeedSpeed Variable provides the feed speed in m/min for throughfeed machines.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6989", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6990", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6991", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6992", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6993", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6177",
    browseName="ns=woodworking;RelativeErrorTime",
    description="The RelativeErrorTime Variable provides the relative time since startup of the ERROR_4 state in msec.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6994", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6995", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6996", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6997", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6998", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)


ns0.vartypes.PropertyType(
    nodeId="ns=woodworking;i=6327",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=woodworking;i=7004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="JobOrderID", dataType=o6.String, valueRank=-1, description=o6.LocalizedText("Contains an ID of the job order, as specified by the method caller.")
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=woodworking;i=6328",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=woodworking;i=7004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="JobResponse",
            dataType=o6.NodeId("ns=isa95_jobcontrol_v2;i=3013"),
            valueRank=-1,
            description=o6.LocalizedText(
                "Contains information about the execution of a job order, such as the current status of the job, actual material consumed, actual material produced, actual equipment used, and job specific data."
            ),
        ),
        ns0.datatypes.Argument(name="ReturnStatus", dataType=o6.UInt64, valueRank=-1, description=o6.LocalizedText("Returns the status of the method execution.")),
    ],
)
o6.call(
    nodeId="ns=woodworking;i=7004",
    browseName="ns=isa95_jobcontrol_v2;RequestJobResponseByJobOrderID",
    inputArgs=o6.hasProperty(o6.ns["ns=woodworking;i=6327"]),
    outputArgs=o6.hasProperty(o6.ns["ns=woodworking;i=6328"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=woodworking;i=6329",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=woodworking;i=7005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="JobOrderState",
            dataType=o6.NodeId("ns=isa95_jobcontrol_v2;i=3006"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText(
                "Contains a job status of the JobResponse to be returned. The array shall provide at least one entry representing the top level state and potentially additional entries representing substates. The first entry shall be the top level entry, having the BrowsePath set to null. The order of the substates is not defined."
            ),
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=woodworking;i=6335",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=woodworking;i=7005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="JobResponses",
            dataType=o6.NodeId("ns=isa95_jobcontrol_v2;i=3013"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText(
                "Contains a list of information about the execution of a job order, such as the current status of the job, actual material consumed, actual material produced, actual equipment used, and job specific data. "
            ),
        ),
        ns0.datatypes.Argument(name="ReturnStatus", dataType=o6.UInt64, valueRank=-1, description=o6.LocalizedText("Returns the status of the method execution.")),
    ],
)
o6.call(
    nodeId="ns=woodworking;i=7005",
    browseName="ns=isa95_jobcontrol_v2;RequestJobResponseByJobOrderState",
    inputArgs=o6.hasProperty(o6.ns["ns=woodworking;i=6329"]),
    outputArgs=o6.hasProperty(o6.ns["ns=woodworking;i=6335"]),
)

isa95_jobcontrol_v2.objtypes.ISA95JobResponseProviderObjectType(
    nodeId="ns=woodworking;i=5039",
    browseName="ns=machinery_jobs;JobOrderResults",
    references=[o6.hasComponent(o6.ns["ns=woodworking;i=7004"]), o6.hasComponent(o6.ns["ns=woodworking;i=7005"])],
)
machinery_jobs.objtypes.JobManagementType(
    nodeId="ns=woodworking;i=5028",
    browseName="ns=machinery_jobs;JobManagement",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=woodworking;i=5034"]), o6.hasComponent(o6.ns["ns=woodworking;i=5039"])],
)
o6.reference(woodworking_objtypes.WwMachineType, ns0.reftypes.HasAddIn, o6.ns["ns=woodworking;i=5028"])
o6.reference(o6.ns["ns=woodworking;i=5005"], "i=17604", o6.ns["ns=woodworking;i=5028"])
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6198",
    browseName="ns=woodworking;RelativeLength",
    description="The RelativeLength Variable provides the relative produced length in mm since the machine has started.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=6999", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7000", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7006", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7007", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7008", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6179",
    browseName="ns=woodworking;RelativeMachineOnTime",
    description="The RelativeMachineOnTime Variable provides the relative time in msec since startup the machine is turned on based on the MachineOn state.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7009", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7010", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7011", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7012", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7013", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6200",
    browseName="ns=woodworking;RelativePiecesIn",
    description="The RelativePiecesIn Variable provides the relative count of pieces which came into the machine since the machine has started.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7019", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7020", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7021", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7022", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7023", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6202",
    browseName="ns=woodworking;RelativePiecesOut",
    description="The RelativePiecesOut Variable provides the relative count of pieces which came out of the machine since the machine has started.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7024", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7025", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7026", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7027", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7028", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6184",
    browseName="ns=woodworking;RelativePowerPresentTime",
    description="The RelativePowerPresentTime Variable provides the relative time in msec since startup the machine has power on based on the PowerPresent state.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7029", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7030", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7031", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7032", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7033", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6186",
    browseName="ns=woodworking;RelativeProductionTime",
    description="The RelativeProductionTime Variable provides the relative time in msec since startup of the machine is working at least with one workpiece based on the RecipeInRun and PiecesPresent state.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7034", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7035", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7036", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7037", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7038", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6190",
    browseName="ns=woodworking;RelativeProductionWaitWorkpieceTime",
    description="The RelativeProductionWaitWorkpieceTime Variable provides the relative time in msec waiting for workpieces since startup of the machine is in working mode, bring the consent out to insert workpiece but no workpiece incoming from the previous machine based on the ReceipeInRun and WaitLoad state.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7039", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7040", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7041", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7042", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7043", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6188",
    browseName="ns=woodworking;RelativeProductionWithoutWorkpieceTime",
    description="The RelativeProductionWithoutWorkpieceTime Variable provides the relative time in msec since startup of the machine is working but without workpieces inside based on the RecipeInRun and !PiecesPresent state.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7044", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7045", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7046", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7047", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7048", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6173",
    browseName="ns=woodworking;RelativeReadyTime",
    description="The RelativeReadyTime Variable provides the relative time since startup of the READY_2 state in msec.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7049", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7050", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7051", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7052", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7053", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6196",
    browseName="ns=woodworking;RelativeRunsAborted",
    description="The RelativeRunsAborted Variable provides the relative count of aborted runs since the machine has started.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7054", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7055", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7056", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7057", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7058", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6192",
    browseName="ns=woodworking;RelativeRunsGood",
    description="The RelativeRunsGood Variable provides the relative count of finished runs since the machine has started.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7059", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7060", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7061", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7062", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7063", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6194",
    browseName="ns=woodworking;RelativeRunsTotal",
    description="The RelativeRunsTotal Variable provides the relative count of total runs since the machine has started.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7064", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7065", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7066", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7067", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7068", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6171",
    browseName="ns=woodworking;RelativeStandbyTime",
    description="The RelativeStandbyTime Variable provides the relative time since startup of the STANDBY_1 state in msec.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7069", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7070", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7071", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7072", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7073", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6175",
    browseName="ns=woodworking;RelativeWorkingTime",
    description="The RelativeWorkingTime Variable provides the relative time since startup of the WORKING_3 state in msec.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7074", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7075", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7076", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7077", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7078", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6165",
    browseName="ns=woodworking;SpindleOverride",
    description="The SpindleOverride Variable provides the override for the spindle in percent.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7079", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7080", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7081", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7082", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7083", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt32,
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=woodworking;i=5018",
    browseName="ns=woodworking;Values",
    description="The Overview Object provides a general state of the unit.",
    references=[
        o6.hasComponent(o6.ns["ns=woodworking;i=6164"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6165"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6166"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6167"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6168"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6170"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6171"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6172"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6173"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6174"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6175"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6176"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6177"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6178"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6179"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6180"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6184"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6185"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6186"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6187"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6188"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6189"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6190"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6191"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6192"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6193"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6194"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6195"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6196"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6197"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6198"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6199"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6200"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6201"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6202"]),
    ],
)
o6.reference(o6.ns["ns=woodworking;i=5018"], "i=17603", woodworking_objtypes.IWwUnitValuesType)
ns0.objtypes.BaseObjectType(
    nodeId="ns=woodworking;i=5009",
    browseName="ns=woodworking;Machine",
    description="State of the whole machine.",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=woodworking;i=5017"]), o6.hasComponent(o6.ns["ns=woodworking;i=5018"]), o6.hasComponent(o6.ns["ns=woodworking;i=5020"])],
)
o6.reference(woodworking_objtypes.IWwStateType, ns0.reftypes.HasComponent, o6.ns["ns=woodworking;i=5009"])
o6.reference(o6.ns["ns=woodworking;i=5009"], "i=17603", woodworking_objtypes.IWwBaseStateType)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6266",
    browseName="ns=woodworking;AbsoluteErrorTime",
    description="The AbsoluteErrorTime Variable provides the absolute time of the ERROR_4 state in msec.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7084", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7085", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7086", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7087", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7088", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6292",
    browseName="ns=woodworking;AbsoluteLength",
    description="The AbsoluteLength Variable provides the absolute produced length in mm.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7089", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7090", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7091", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7092", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7093", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6268",
    browseName="ns=woodworking;AbsoluteMachineOnTime",
    description="The AbsoluteMachineOnTime Variable provides the absolute time in msec the machine is turned on based on the MachineOn state.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7094", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7095", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7096", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7097", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7098", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6258",
    browseName="ns=woodworking;AbsoluteMachineOffTime",
    description="The AbsoluteOfflineTime can be calculated by the machine. The shutdown time and the starting time have to be stored on the machine.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7099", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7100", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7101", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7102", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7103", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6294",
    browseName="ns=woodworking;AbsolutePiecesIn",
    description="The AbsolutePiecesIn Variable provides the absolute count of pieces which came into the machine.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7104", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7105", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7106", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7107", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7108", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6296",
    browseName="ns=woodworking;AbsolutePiecesOut",
    description="The AbsolutePiecesOut Variable provides the absolute count of pieces which came out of the machine.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7109", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7110", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7111", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7112", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7113", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6270",
    browseName="ns=woodworking;AbsolutePowerPresentTime",
    description="The AbsolutePowerPresentTime Variable provides the absolute time in msec the machine has power on based on the PowerPresent state.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7114", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7115", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7116", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7117", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7118", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6272",
    browseName="ns=woodworking;AbsoluteProductionTime",
    description="The AbsoluteProductionTime Variable provides the absolute time in msec of the machine is working at least with one workpiece based on the RecipeInRun and PiecesPresent state.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7119", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7120", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7121", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7122", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7123", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6276",
    browseName="ns=woodworking;AbsoluteProductionWaitWorkpieceTime",
    description="The AbsoluteProductionWaitWorkpieceTime Variable provides the absolute time in msec of the machine is in working mode, bring the consent out to insert workpiece but no workpiece incoming from the previous machine based on the ReceipeInRun and WaitLoad state.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7124", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7125", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7126", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7127", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7128", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6274",
    browseName="ns=woodworking;AbsoluteProductionWithoutWorkpieceTime",
    description="The AbsoluteProductionWithoutWorkpieceTime Variable provides the absolute time in msec of the machine is working but without workpieces inside based on the RecipeInRun and !PiecesPresent state.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7129", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7130", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7131", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7132", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7133", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6262",
    browseName="ns=woodworking;AbsoluteReadyTime",
    description="The AbsoluteReadyTime Variable provides the absolute time of the READY_2 state in msec.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7134", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7135", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7136", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7137", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7138", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6290",
    browseName="ns=woodworking;AbsoluteRunsAborted",
    description="The AbsoluteRunsAborted Variable provides the absolute count of aborted runs.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7139", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7140", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7141", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7142", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6286",
    browseName="ns=woodworking;AbsoluteRunsGood",
    description="The AbsoluteRunsGood Variable provides the absolute count of finished runs.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7143", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7144", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7145", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7146", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7147", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6288",
    browseName="ns=woodworking;AbsoluteRunsTotal",
    description="The AbsoluteRunsTotal Variable provides the absolute count of total runs.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7148", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7149", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7150", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7151", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7152", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6260",
    browseName="ns=woodworking;AbsoluteStandbyTime",
    description="The AbsoluteStandbyTime Variable provides the absolute time of the STANDBY_1 state in msec.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7153", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7154", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7155", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7156", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7157", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6264",
    browseName="ns=woodworking;AbsoluteWorkingTime",
    description="The AbsoluteWorkingTime Variable provides the absolute time of the WORKING_3 state in msec.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7158", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7159", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7160", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7161", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7162", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6257",
    browseName="ns=woodworking;ActualCycle",
    description="The ActualCycle Variable provides the parts per minutes.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7163", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7164", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7165", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7166", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7167", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6254",
    browseName="ns=woodworking;AxisOverride",
    description="The AxisOverride Variable provides the override for the axis in percent.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7168", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7169", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7170", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7171", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7172", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt32,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6256",
    browseName="ns=woodworking;FeedSpeed",
    description="The FeedSpeed Variable provides the feed speed in m/min for throughfeed machines.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7173", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7174", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7175", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7176", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7177", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6267",
    browseName="ns=woodworking;RelativeErrorTime",
    description="The RelativeErrorTime Variable provides the relative time since startup of the ERROR_4 state in msec.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7178", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7179", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7180", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7181", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7182", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6293",
    browseName="ns=woodworking;RelativeLength",
    description="The RelativeLength Variable provides the relative produced length in mm since the machine has started.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7183", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7184", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7185", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7186", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7187", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6269",
    browseName="ns=woodworking;RelativeMachineOnTime",
    description="The RelativeMachineOnTime Variable provides the relative time in msec since startup the machine is turned on based on the MachineOn state.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7188", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7189", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7190", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7191", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7192", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6295",
    browseName="ns=woodworking;RelativePiecesIn",
    description="The RelativePiecesIn Variable provides the relative count of pieces which came into the machine since the machine has started.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7198", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7199", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7200", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7201", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7202", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6297",
    browseName="ns=woodworking;RelativePiecesOut",
    description="The RelativePiecesOut Variable provides the relative count of pieces which came out of the machine since the machine has started.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7203", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7204", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7205", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7206", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7207", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6271",
    browseName="ns=woodworking;RelativePowerPresentTime",
    description="The RelativePowerPresentTime Variable provides the relative time in msec since startup the machine has power on based on the PowerPresent state.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7208", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7209", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7210", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7211", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7212", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6273",
    browseName="ns=woodworking;RelativeProductionTime",
    description="The RelativeProductionTime Variable provides the relative time in msec since startup of the machine is working at least with one workpiece based on the RecipeInRun and PiecesPresent state.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7213", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7214", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7215", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7216", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7217", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6285",
    browseName="ns=woodworking;RelativeProductionWaitWorkpieceTime",
    description="The RelativeProductionWaitWorkpieceTime Variable provides the relative time in msec waiting for workpieces since startup of the machine is in working mode, bring the consent out to insert workpiece but no workpiece incoming from the previous machine based on the ReceipeInRun and WaitLoad state.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7218", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7219", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7220", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7221", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7222", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6275",
    browseName="ns=woodworking;RelativeProductionWithoutWorkpieceTime",
    description="The RelativeProductionWithoutWorkpieceTime Variable provides the relative time in msec since startup of the machine is working but without workpieces inside based on the RecipeInRun and !PiecesPresent state.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7223", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7224", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7225", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7226", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7227", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6263",
    browseName="ns=woodworking;RelativeReadyTime",
    description="The RelativeReadyTime Variable provides the relative time since startup of the READY_2 state in msec.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7228", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7229", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7230", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7231", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7232", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6291",
    browseName="ns=woodworking;RelativeRunsAborted",
    description="The RelativeRunsAborted Variable provides the relative count of aborted runs since the machine has started.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7233", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7234", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7235", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7236", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7237", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6287",
    browseName="ns=woodworking;RelativeRunsGood",
    description="The RelativeRunsGood Variable provides the relative count of finished runs since the machine has started.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7238", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7239", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7240", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7241", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7242", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6289",
    browseName="ns=woodworking;RelativeRunsTotal",
    description="The RelativeRunsTotal Variable provides the relative count of total runs since the machine has started.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7243", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7244", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7245", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7246", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7247", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6261",
    browseName="ns=woodworking;RelativeStandbyTime",
    description="The RelativeStandbyTime Variable provides the relative time since startup of the STANDBY_1 state in msec.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7248", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7249", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7250", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7251", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7252", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6265",
    browseName="ns=woodworking;RelativeWorkingTime",
    description="The RelativeWorkingTime Variable provides the relative time since startup of the WORKING_3 state in msec.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7253", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7254", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7255", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7256", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7257", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6255",
    browseName="ns=woodworking;SpindleOverride",
    description="The SpindleOverride Variable provides the override for the spindle in percent.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7258", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7259", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7260", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7261", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7262", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt32,
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=woodworking;i=5024",
    browseName="ns=woodworking;Values",
    description="The Values Object provides the counters of the unit.",
    references=[
        o6.hasComponent(o6.ns["ns=woodworking;i=6254"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6255"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6256"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6257"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6258"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6260"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6261"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6262"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6263"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6264"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6265"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6266"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6267"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6268"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6269"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6270"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6271"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6272"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6273"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6274"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6275"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6276"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6285"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6286"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6287"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6288"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6289"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6290"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6291"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6292"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6293"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6294"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6295"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6296"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6297"]),
    ],
)
o6.reference(o6.ns["ns=woodworking;i=5024"], "i=17603", woodworking_objtypes.IWwUnitValuesType)
ns0.objtypes.BaseObjectType(
    nodeId="ns=woodworking;i=5021",
    browseName="ns=woodworking;<SubUnit>",
    description="Each <SubUnit> Object represents an instance of a state. For example, a CNC machine can have two places where independent jobs are produced. Then there are two <SubUnit> Objects. They may be named “Place 1” and “Place 2”.",
    modellingRule="MandatoryPlaceholder",
    references=[o6.hasComponent(o6.ns["ns=woodworking;i=5022"]), o6.hasComponent(o6.ns["ns=woodworking;i=5023"]), o6.hasComponent(o6.ns["ns=woodworking;i=5024"])],
)
o6.reference(o6.ns["ns=woodworking;i=5021"], "i=17603", woodworking_objtypes.IWwBaseStateType)
ns0.objtypes.BaseObjectType(
    nodeId="ns=woodworking;i=5016",
    browseName="ns=woodworking;SubUnits",
    description="The SubUnits Object is used when a machine has multiple states. For example, a CNC machine can have several places where independent jobs are produced.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=woodworking;i=5021"])],
)
o6.reference(woodworking_objtypes.IWwStateType, ns0.reftypes.HasComponent, o6.ns["ns=woodworking;i=5016"])
o6.reference(o6.ns["ns=woodworking;i=5016"], "i=17603", woodworking_objtypes.IWwSubUnitsType)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6342",
    browseName="ns=woodworking;AbsoluteErrorTime",
    description="The AbsoluteErrorTime Variable provides the absolute time of the ERROR_4 state in msec.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7263", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7264", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7265", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7266", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7267", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6360",
    browseName="ns=woodworking;AbsoluteLength",
    description="The AbsoluteLength Variable provides the absolute produced length in mm.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7268", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7269", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7270", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7271", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7272", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6334",
    browseName="ns=woodworking;AbsoluteMachineOffTime",
    description="The AbsoluteOfflineTime can be calculated by the machine. The shutdown time and the starting time have to be stored on the machine.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7273", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7274", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7275", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7276", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7277", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6344",
    browseName="ns=woodworking;AbsoluteMachineOnTime",
    description="The AbsoluteMachineOnTime Variable provides the absolute time in msec the machine is turned on based on the MachineOn state.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7278", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7279", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7280", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7281", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7282", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6362",
    browseName="ns=woodworking;AbsolutePiecesIn",
    description="The AbsolutePiecesIn Variable provides the absolute count of pieces which came into the machine.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7283", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7284", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7285", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7286", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7287", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6364",
    browseName="ns=woodworking;AbsolutePiecesOut",
    description="The AbsolutePiecesOut Variable provides the absolute count of pieces which came out of the machine.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7288", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7289", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7290", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7291", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7292", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6346",
    browseName="ns=woodworking;AbsolutePowerPresentTime",
    description="The AbsolutePowerPresentTime Variable provides the absolute time in msec the machine has power on based on the PowerPresent state.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7293", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7294", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7295", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7296", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7297", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6348",
    browseName="ns=woodworking;AbsoluteProductionTime",
    description="The AbsoluteProductionTime Variable provides the absolute time in msec of the machine is working at least with one workpiece based on the RecipeInRun and PiecesPresent state.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7298", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7299", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7300", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7301", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7302", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6352",
    browseName="ns=woodworking;AbsoluteProductionWaitWorkpieceTime",
    description="The AbsoluteProductionWaitWorkpieceTime Variable provides the absolute time in msec of the machine is in working mode, bring the consent out to insert workpiece but no workpiece incoming from the previous machine based on the ReceipeInRun and WaitLoad state.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7303", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7304", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7305", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7306", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7307", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6350",
    browseName="ns=woodworking;AbsoluteProductionWithoutWorkpieceTime",
    description="The AbsoluteProductionWithoutWorkpieceTime Variable provides the absolute time in msec of the machine is working but without workpieces inside based on the RecipeInRun and !PiecesPresent state.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7308", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7309", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7310", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7311", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7312", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6338",
    browseName="ns=woodworking;AbsoluteReadyTime",
    description="The AbsoluteReadyTime Variable provides the absolute time of the READY_2 state in msec.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7313", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7314", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7315", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7316", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7317", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6358",
    browseName="ns=woodworking;AbsoluteRunsAborted",
    description="The AbsoluteRunsAborted Variable provides the absolute count of aborted runs.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7318", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7319", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7320", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7321", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7322", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6356",
    browseName="ns=woodworking;AbsoluteRunsTotal",
    description="The AbsoluteRunsTotal Variable provides the absolute count of total runs.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7323", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7324", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7325", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7326", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7327", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6336",
    browseName="ns=woodworking;AbsoluteStandbyTime",
    description="The AbsoluteStandbyTime Variable provides the absolute time of the STANDBY_1 state in msec.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7328", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7329", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7330", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7331", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7332", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6340",
    browseName="ns=woodworking;AbsoluteWorkingTime",
    description="The AbsoluteWorkingTime Variable provides the absolute time of the WORKING_3 state in msec.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7333", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7334", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7335", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7336", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7337", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6333",
    browseName="ns=woodworking;ActualCycle",
    description="The ActualCycle Variable provides the parts per minutes.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7338", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7339", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7340", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7341", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7342", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6330",
    browseName="ns=woodworking;AxisOverride",
    description="The AxisOverride Variable provides the override for the axis in percent.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7343", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7344", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7345", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7346", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7347", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt32,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6332",
    browseName="ns=woodworking;FeedSpeed",
    description="The FeedSpeed Variable provides the feed speed in m/min for throughfeed machines.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7348", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7349", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7350", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7351", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7352", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6343",
    browseName="ns=woodworking;RelativeErrorTime",
    description="The RelativeErrorTime Variable provides the relative time since startup of the ERROR_4 state in msec.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7353", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7354", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7355", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7356", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7357", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6361",
    browseName="ns=woodworking;RelativeLength",
    description="The RelativeLength Variable provides the relative produced length in mm since the machine has started.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7358", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7359", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7360", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7361", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7362", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6345",
    browseName="ns=woodworking;RelativeMachineOnTime",
    description="The RelativeMachineOnTime Variable provides the relative time in msec since startup the machine is turned on based on the MachineOn state.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7363", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7364", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7365", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7366", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7367", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6363",
    browseName="ns=woodworking;RelativePiecesIn",
    description="The RelativePiecesIn Variable provides the relative count of pieces which came into the machine since the machine has started.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7373", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7374", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7375", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7376", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7377", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6365",
    browseName="ns=woodworking;RelativePiecesOut",
    description="The RelativePiecesOut Variable provides the relative count of pieces which came out of the machine since the machine has started.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7378", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7379", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7380", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7381", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7382", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6347",
    browseName="ns=woodworking;RelativePowerPresentTime",
    description="The RelativePowerPresentTime Variable provides the relative time in msec since startup the machine has power on based on the PowerPresent state.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7383", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7384", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7385", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7386", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7387", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6349",
    browseName="ns=woodworking;RelativeProductionTime",
    description="The RelativeProductionTime Variable provides the relative time in msec since startup of the machine is working at least with one workpiece based on the RecipeInRun and PiecesPresent state.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7388", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7389", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7390", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7391", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7392", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6353",
    browseName="ns=woodworking;RelativeProductionWaitWorkpieceTime",
    description="The RelativeProductionWaitWorkpieceTime Variable provides the relative time in msec waiting for workpieces since startup of the machine is in working mode, bring the consent out to insert workpiece but no workpiece incoming from the previous machine based on the ReceipeInRun and WaitLoad state.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7393", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7394", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7395", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7396", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7397", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6351",
    browseName="ns=woodworking;RelativeProductionWithoutWorkpieceTime",
    description="The RelativeProductionWithoutWorkpieceTime Variable provides the relative time in msec since startup of the machine is working but without workpieces inside based on the RecipeInRun and !PiecesPresent state.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7398", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7399", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7400", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7401", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7402", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6339",
    browseName="ns=woodworking;RelativeReadyTime",
    description="The RelativeReadyTime Variable provides the relative time since startup of the READY_2 state in msec.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7403", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7404", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7405", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7406", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7407", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6359",
    browseName="ns=woodworking;RelativeRunsAborted",
    description="The RelativeRunsAborted Variable provides the relative count of aborted runs since the machine has started.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7408", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7409", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7410", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7411", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7412", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6355",
    browseName="ns=woodworking;RelativeRunsGood",
    description="The RelativeRunsGood Variable provides the relative count of finished runs since the machine has started.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7413", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7414", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7415", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7416", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7417", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6357",
    browseName="ns=woodworking;RelativeRunsTotal",
    description="The RelativeRunsTotal Variable provides the relative count of total runs since the machine has started.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7418", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7419", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7420", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7421", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6341",
    browseName="ns=woodworking;RelativeWorkingTime",
    description="The RelativeWorkingTime Variable provides the relative time since startup of the WORKING_3 state in msec.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7422", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7423", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7424", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7425", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7426", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6331",
    browseName="ns=woodworking;SpindleOverride",
    description="The SpindleOverride Variable provides the override for the spindle in percent.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7427", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7428", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7429", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7430", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7431", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt32,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6354",
    browseName="ns=woodworking;AbsoluteRunsGood",
    description="The AbsoluteRunsGood Variable provides the absolute count of finished runs.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7432", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7433", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7434", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7435", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7436", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6337",
    browseName="ns=woodworking;RelativeStandbyTime",
    description="The RelativeStandbyTime Variable provides the relative time since startup of the STANDBY_1 state in msec.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7437", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7438", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7439", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7440", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7441", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=woodworking;i=5029",
    browseName="ns=woodworking;Values",
    description="The Values Object provides the counters of the unit.",
    references=[
        o6.hasComponent(o6.ns["ns=woodworking;i=6330"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6331"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6332"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6333"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6334"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6336"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6337"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6338"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6339"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6340"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6341"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6342"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6343"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6344"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6345"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6346"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6347"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6348"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6349"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6350"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6351"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6352"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6353"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6354"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6355"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6356"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6357"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6358"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6359"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6360"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6361"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6362"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6363"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6364"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6365"]),
    ],
)
o6.reference(o6.ns["ns=woodworking;i=5029"], "i=17603", woodworking_objtypes.IWwUnitValuesType)
ns0.objtypes.BaseObjectType(
    nodeId="ns=woodworking;i=5002",
    browseName="ns=woodworking;<SubUnit>",
    description="Each <SubUnit> Object represents an instance of a state. For example, a CNC machine can have two places where independent jobs are produced. Then there are two <SubUnit> Objects. They may be named “Place 1” and “Place 2”.",
    modellingRule="MandatoryPlaceholder",
    references=[o6.hasComponent(o6.ns["ns=woodworking;i=5026"]), o6.hasComponent(o6.ns["ns=woodworking;i=5027"]), o6.hasComponent(o6.ns["ns=woodworking;i=5029"])],
)
o6.reference(woodworking_objtypes.IWwSubUnitsType, ns0.reftypes.HasComponent, o6.ns["ns=woodworking;i=5002"])
o6.reference(o6.ns["ns=woodworking;i=5002"], "i=17603", woodworking_objtypes.IWwBaseStateType)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6410",
    browseName="ns=woodworking;AbsoluteErrorTime",
    description="The AbsoluteErrorTime Variable provides the absolute time of the ERROR_4 state in msec.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7442", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7443", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7444", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7445", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7446", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6428",
    browseName="ns=woodworking;AbsoluteLength",
    description="The AbsoluteLength Variable provides the absolute produced length in mm.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7447", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7448", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7449", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7450", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7451", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6412",
    browseName="ns=woodworking;AbsoluteMachineOnTime",
    description="The AbsoluteMachineOnTime Variable provides the absolute time in msec the machine is turned on based on the MachineOn state.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7452", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7453", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7454", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7455", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7456", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6402",
    browseName="ns=woodworking;AbsoluteMachineOffTime",
    description="The AbsoluteOfflineTime can be calculated by the machine. The shutdown time and the starting time have to be stored on the machine.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7457", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7458", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7459", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7460", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7461", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6430",
    browseName="ns=woodworking;AbsolutePiecesIn",
    description="The AbsolutePiecesIn Variable provides the absolute count of pieces which came into the machine.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7462", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7463", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7464", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7465", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7466", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6432",
    browseName="ns=woodworking;AbsolutePiecesOut",
    description="The AbsolutePiecesOut Variable provides the absolute count of pieces which came out of the machine.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7467", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7468", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7469", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7470", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7471", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6414",
    browseName="ns=woodworking;AbsolutePowerPresentTime",
    description="The AbsolutePowerPresentTime Variable provides the absolute time in msec the machine has power on based on the PowerPresent state.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7472", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7473", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7474", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7475", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7476", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6416",
    browseName="ns=woodworking;AbsoluteProductionTime",
    description="The AbsoluteProductionTime Variable provides the absolute time in msec of the machine is working at least with one workpiece based on the RecipeInRun and PiecesPresent state.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7477", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7478", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7479", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7480", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7481", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6420",
    browseName="ns=woodworking;AbsoluteProductionWaitWorkpieceTime",
    description="The AbsoluteProductionWaitWorkpieceTime Variable provides the absolute time in msec of the machine is in working mode, bring the consent out to insert workpiece but no workpiece incoming from the previous machine based on the ReceipeInRun and WaitLoad state.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7482", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7483", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7484", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7485", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7486", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6418",
    browseName="ns=woodworking;AbsoluteProductionWithoutWorkpieceTime",
    description="The AbsoluteProductionWithoutWorkpieceTime Variable provides the absolute time in msec of the machine is working but without workpieces inside based on the RecipeInRun and !PiecesPresent state.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7487", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7488", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7489", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7490", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7491", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6406",
    browseName="ns=woodworking;AbsoluteReadyTime",
    description="The AbsoluteReadyTime Variable provides the absolute time of the READY_2 state in msec.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7492", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7493", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7494", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7495", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7496", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6426",
    browseName="ns=woodworking;AbsoluteRunsAborted",
    description="The AbsoluteRunsAborted Variable provides the absolute count of aborted runs.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7497", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7498", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7499", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7500", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7501", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6422",
    browseName="ns=woodworking;AbsoluteRunsGood",
    description="The AbsoluteRunsGood Variable provides the absolute count of finished runs.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7502", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7503", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7504", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7505", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7506", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6424",
    browseName="ns=woodworking;AbsoluteRunsTotal",
    description="The AbsoluteRunsTotal Variable provides the absolute count of total runs.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7507", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7508", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7509", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7510", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7511", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6404",
    browseName="ns=woodworking;AbsoluteStandbyTime",
    description="The AbsoluteStandbyTime Variable provides the absolute time of the STANDBY_1 state in msec.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7512", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7513", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7514", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7515", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7516", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6408",
    browseName="ns=woodworking;AbsoluteWorkingTime",
    description="The AbsoluteWorkingTime Variable provides the absolute time of the WORKING_3 state in msec.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7517", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7518", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7519", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7520", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7521", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6401",
    browseName="ns=woodworking;ActualCycle",
    description="The ActualCycle Variable provides the parts per minutes.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7522", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7523", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7524", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7525", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7526", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6398",
    browseName="ns=woodworking;AxisOverride",
    description="The AxisOverride Variable provides the override for the axis in percent.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7527", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7528", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7529", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7530", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7531", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt32,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6400",
    browseName="ns=woodworking;FeedSpeed",
    description="The FeedSpeed Variable provides the feed speed in m/min for throughfeed machines.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7532", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7533", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7534", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7535", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7536", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6411",
    browseName="ns=woodworking;RelativeErrorTime",
    description="The RelativeErrorTime Variable provides the relative time since startup of the ERROR_4 state in msec.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7537", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7538", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7539", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7540", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7541", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6413",
    browseName="ns=woodworking;RelativeMachineOnTime",
    description="The RelativeMachineOnTime Variable provides the relative time in msec since startup the machine is turned on based on the MachineOn state.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7546", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7547", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7548", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7549", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7550", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6429",
    browseName="ns=woodworking;RelativeLength",
    description="The RelativeLength Variable provides the relative produced length in mm since the machine has started.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7542", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7543", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7544", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7545", browseName="ValuePrecision", dataType=o6.Double)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7551", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6431",
    browseName="ns=woodworking;RelativePiecesIn",
    description="The RelativePiecesIn Variable provides the relative count of pieces which came into the machine since the machine has started.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7557", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7558", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7559", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7560", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7561", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6433",
    browseName="ns=woodworking;RelativePiecesOut",
    description="The RelativePiecesOut Variable provides the relative count of pieces which came out of the machine since the machine has started.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7562", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7563", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7564", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7565", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7566", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6415",
    browseName="ns=woodworking;RelativePowerPresentTime",
    description="The RelativePowerPresentTime Variable provides the relative time in msec since startup the machine has power on based on the PowerPresent state.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7567", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7568", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7569", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7570", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7571", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6417",
    browseName="ns=woodworking;RelativeProductionTime",
    description="The RelativeProductionTime Variable provides the relative time in msec since startup of the machine is working at least with one workpiece based on the RecipeInRun and PiecesPresent state.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7572", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7573", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7574", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7575", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7576", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6421",
    browseName="ns=woodworking;RelativeProductionWaitWorkpieceTime",
    description="The RelativeProductionWaitWorkpieceTime Variable provides the relative time in msec waiting for workpieces since startup of the machine is in working mode, bring the consent out to insert workpiece but no workpiece incoming from the previous machine based on the ReceipeInRun and WaitLoad state.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7577", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7578", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7579", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7580", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7581", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6419",
    browseName="ns=woodworking;RelativeProductionWithoutWorkpieceTime",
    description="The RelativeProductionWithoutWorkpieceTime Variable provides the relative time in msec since startup of the machine is working but without workpieces inside based on the RecipeInRun and !PiecesPresent state.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7582", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7583", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7584", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7585", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7586", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6407",
    browseName="ns=woodworking;RelativeReadyTime",
    description="The RelativeReadyTime Variable provides the relative time since startup of the READY_2 state in msec.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7587", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7588", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7589", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7590", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7591", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6427",
    browseName="ns=woodworking;RelativeRunsAborted",
    description="The RelativeRunsAborted Variable provides the relative count of aborted runs since the machine has started.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7592", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7593", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7594", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7595", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7596", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6423",
    browseName="ns=woodworking;RelativeRunsGood",
    description="The RelativeRunsGood Variable provides the relative count of finished runs since the machine has started.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7597", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7598", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7599", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7600", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7601", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6425",
    browseName="ns=woodworking;RelativeRunsTotal",
    description="The RelativeRunsTotal Variable provides the relative count of total runs since the machine has started.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7602", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7603", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7604", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7605", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7606", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6405",
    browseName="ns=woodworking;RelativeStandbyTime",
    description="The RelativeStandbyTime Variable provides the relative time since startup of the STANDBY_1 state in msec.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7607", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7608", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7609", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7610", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7611", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6409",
    browseName="ns=woodworking;RelativeWorkingTime",
    description="The RelativeWorkingTime Variable provides the relative time since startup of the WORKING_3 state in msec.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7612", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7613", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7614", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7615", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7616", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6399",
    browseName="ns=woodworking;SpindleOverride",
    description="The SpindleOverride Variable provides the override for the spindle in percent.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7617", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7618", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7619", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7620", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7621", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt32,
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=woodworking;i=5035",
    browseName="ns=woodworking;Values",
    description="The Values Object provides the counters of the unit.",
    references=[
        o6.hasComponent(o6.ns["ns=woodworking;i=6398"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6399"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6400"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6401"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6402"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6404"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6405"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6406"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6407"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6408"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6409"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6410"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6411"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6412"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6413"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6414"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6415"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6416"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6417"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6418"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6419"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6420"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6421"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6422"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6423"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6424"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6425"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6426"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6427"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6428"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6429"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6430"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6431"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6432"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6433"]),
    ],
)
o6.reference(o6.ns["ns=woodworking;i=5035"], "i=17603", woodworking_objtypes.IWwUnitValuesType)
ns0.objtypes.BaseObjectType(
    nodeId="ns=woodworking;i=5030",
    browseName="ns=woodworking;Machine",
    description="State of the whole machine.",
    references=[o6.hasComponent(o6.ns["ns=woodworking;i=5032"]), o6.hasComponent(o6.ns["ns=woodworking;i=5033"]), o6.hasComponent(o6.ns["ns=woodworking;i=5035"])],
)
o6.reference(o6.ns["ns=woodworking;i=5030"], "i=17603", woodworking_objtypes.IWwBaseStateType)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6478",
    browseName="ns=woodworking;AbsoluteErrorTime",
    description="The AbsoluteErrorTime Variable provides the absolute time of the ERROR_4 state in msec.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7622", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7623", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7624", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7625", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7626", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6496",
    browseName="ns=woodworking;AbsoluteLength",
    description="The AbsoluteLength Variable provides the absolute produced length in mm.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7627", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7628", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7629", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7630", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7631", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6480",
    browseName="ns=woodworking;AbsoluteMachineOnTime",
    description="The AbsoluteMachineOnTime Variable provides the absolute time in msec the machine is turned on based on the MachineOn state.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7632", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7633", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7634", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7635", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7636", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6470",
    browseName="ns=woodworking;AbsoluteMachineOffTime",
    description="The AbsoluteOfflineTime can be calculated by the machine. The shutdown time and the starting time have to be stored on the machine.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7637", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7638", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7639", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7640", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7641", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6498",
    browseName="ns=woodworking;AbsolutePiecesIn",
    description="The AbsolutePiecesIn Variable provides the absolute count of pieces which came into the machine.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7642", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7643", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7644", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7645", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7646", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6500",
    browseName="ns=woodworking;AbsolutePiecesOut",
    description="The AbsolutePiecesOut Variable provides the absolute count of pieces which came out of the machine.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7647", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7648", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7649", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7650", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7651", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6482",
    browseName="ns=woodworking;AbsolutePowerPresentTime",
    description="The AbsolutePowerPresentTime Variable provides the absolute time in msec the machine has power on based on the PowerPresent state.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7652", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7653", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7654", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7655", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7656", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6484",
    browseName="ns=woodworking;AbsoluteProductionTime",
    description="The AbsoluteProductionTime Variable provides the absolute time in msec of the machine is working at least with one workpiece based on the RecipeInRun and PiecesPresent state.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7657", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7658", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7659", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7660", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7661", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6488",
    browseName="ns=woodworking;AbsoluteProductionWaitWorkpieceTime",
    description="The AbsoluteProductionWaitWorkpieceTime Variable provides the absolute time in msec of the machine is in working mode, bring the consent out to insert workpiece but no workpiece incoming from the previous machine based on the ReceipeInRun and WaitLoad state.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7662", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7663", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7664", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7665", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7666", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6486",
    browseName="ns=woodworking;AbsoluteProductionWithoutWorkpieceTime",
    description="The AbsoluteProductionWithoutWorkpieceTime Variable provides the absolute time in msec of the machine is working but without workpieces inside based on the RecipeInRun and !PiecesPresent state.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7667", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7668", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7669", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7670", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7671", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6474",
    browseName="ns=woodworking;AbsoluteReadyTime",
    description="The AbsoluteReadyTime Variable provides the absolute time of the READY_2 state in msec.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7672", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7673", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7674", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7675", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7676", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6494",
    browseName="ns=woodworking;AbsoluteRunsAborted",
    description="The AbsoluteRunsAborted Variable provides the absolute count of aborted runs.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7677", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7678", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7679", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7680", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7681", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6490",
    browseName="ns=woodworking;AbsoluteRunsGood",
    description="The AbsoluteRunsGood Variable provides the absolute count of finished runs.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7682", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7683", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7684", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7685", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7686", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6492",
    browseName="ns=woodworking;AbsoluteRunsTotal",
    description="The AbsoluteRunsTotal Variable provides the absolute count of total runs.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7687", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7688", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7689", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7690", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7691", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6472",
    browseName="ns=woodworking;AbsoluteStandbyTime",
    description="The AbsoluteStandbyTime Variable provides the absolute time of the STANDBY_1 state in msec.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7692", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7693", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7694", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7695", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7696", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6476",
    browseName="ns=woodworking;AbsoluteWorkingTime",
    description="The AbsoluteWorkingTime Variable provides the absolute time of the WORKING_3 state in msec.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7697", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7698", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7699", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7700", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7701", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6469",
    browseName="ns=woodworking;ActualCycle",
    description="The ActualCycle Variable provides the parts per minutes.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7702", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7703", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7704", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7705", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7706", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6466",
    browseName="ns=woodworking;AxisOverride",
    description="The AxisOverride Variable provides the override for the axis in percent.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7707", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7708", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7709", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7710", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7711", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt32,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6468",
    browseName="ns=woodworking;FeedSpeed",
    description="The FeedSpeed Variable provides the feed speed in m/min for throughfeed machines.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7712", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7713", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7714", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7715", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7716", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6479",
    browseName="ns=woodworking;RelativeErrorTime",
    description="The RelativeErrorTime Variable provides the relative time since startup of the ERROR_4 state in msec.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7717", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7718", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7719", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7720", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7721", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6497",
    browseName="ns=woodworking;RelativeLength",
    description="The RelativeLength Variable provides the relative produced length in mm since the machine has started.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7722", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7723", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7724", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7725", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7726", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6481",
    browseName="ns=woodworking;RelativeMachineOnTime",
    description="The RelativeMachineOnTime Variable provides the relative time in msec since startup the machine is turned on based on the MachineOn state.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7727", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7728", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7729", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7730", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7731", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6499",
    browseName="ns=woodworking;RelativePiecesIn",
    description="The RelativePiecesIn Variable provides the relative count of pieces which came into the machine since the machine has started.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7737", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7738", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7739", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7740", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7741", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6501",
    browseName="ns=woodworking;RelativePiecesOut",
    description="The RelativePiecesOut Variable provides the relative count of pieces which came out of the machine since the machine has started.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7742", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7743", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7744", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7745", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7746", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6485",
    browseName="ns=woodworking;RelativeProductionTime",
    description="The RelativeProductionTime Variable provides the relative time in msec since startup of the machine is working at least with one workpiece based on the RecipeInRun and PiecesPresent state.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7747", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7748", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7749", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7750", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7751", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6483",
    browseName="ns=woodworking;RelativePowerPresentTime",
    description="The RelativePowerPresentTime Variable provides the relative time in msec since startup the machine has power on based on the PowerPresent state.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7752", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7753", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7754", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7755", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7756", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6489",
    browseName="ns=woodworking;RelativeProductionWaitWorkpieceTime",
    description="The RelativeProductionWaitWorkpieceTime Variable provides the relative time in msec waiting for workpieces since startup of the machine is in working mode, bring the consent out to insert workpiece but no workpiece incoming from the previous machine based on the ReceipeInRun and WaitLoad state.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7757", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7758", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7759", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7760", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7761", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6487",
    browseName="ns=woodworking;RelativeProductionWithoutWorkpieceTime",
    description="The RelativeProductionWithoutWorkpieceTime Variable provides the relative time in msec since startup of the machine is working but without workpieces inside based on the RecipeInRun and !PiecesPresent state.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7762", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7763", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7764", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7765", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7766", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6475",
    browseName="ns=woodworking;RelativeReadyTime",
    description="The RelativeReadyTime Variable provides the relative time since startup of the READY_2 state in msec.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7767", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7768", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7769", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7770", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7771", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6495",
    browseName="ns=woodworking;RelativeRunsAborted",
    description="The RelativeRunsAborted Variable provides the relative count of aborted runs since the machine has started.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7772", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7773", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7774", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7775", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7776", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6491",
    browseName="ns=woodworking;RelativeRunsGood",
    description="The RelativeRunsGood Variable provides the relative count of finished runs since the machine has started.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7777", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7778", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7779", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7780", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7781", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6493",
    browseName="ns=woodworking;RelativeRunsTotal",
    description="The RelativeRunsTotal Variable provides the relative count of total runs since the machine has started.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7782", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7783", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7784", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7785", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7786", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6473",
    browseName="ns=woodworking;RelativeStandbyTime",
    description="The RelativeStandbyTime Variable provides the relative time since startup of the STANDBY_1 state in msec.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7787", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7788", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7789", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7790", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7791", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6467",
    browseName="ns=woodworking;SpindleOverride",
    description="The SpindleOverride Variable provides the override for the spindle in percent.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7792", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7793", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7794", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7795", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7796", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt32,
)
ns0.vartypes.BaseAnalogType(
    nodeId="ns=woodworking;i=6477",
    browseName="ns=woodworking;RelativeWorkingTime",
    description="The RelativeWorkingTime Variable provides the relative time since startup of the WORKING_3 state in msec.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7797", browseName="Definition", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7798", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7799", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7800", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=woodworking;i=7801", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=o6.UInt64,
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=woodworking;i=5040",
    browseName="ns=woodworking;Values",
    description="The Values Object provides the counters of the unit.",
    references=[
        o6.hasComponent(o6.ns["ns=woodworking;i=6466"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6467"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6468"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6469"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6470"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6472"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6473"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6474"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6475"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6476"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6477"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6478"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6479"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6480"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6481"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6482"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6483"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6484"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6485"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6486"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6487"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6488"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6489"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6490"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6491"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6492"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6493"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6494"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6495"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6496"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6497"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6498"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6499"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6500"]),
        o6.hasComponent(o6.ns["ns=woodworking;i=6501"]),
    ],
)
o6.reference(o6.ns["ns=woodworking;i=5040"], "i=17603", woodworking_objtypes.IWwUnitValuesType)
ns0.objtypes.BaseObjectType(
    nodeId="ns=woodworking;i=5036",
    browseName="ns=woodworking;<SubUnit>",
    description="Each <SubUnit> Object represents an instance of a state. For example, a CNC machine can have two places where independent jobs are produced. Then there are two <SubUnit> Objects. They may be named “Place 1” and “Place 2”.",
    modellingRule="MandatoryPlaceholder",
    references=[o6.hasComponent(o6.ns["ns=woodworking;i=5037"]), o6.hasComponent(o6.ns["ns=woodworking;i=5038"]), o6.hasComponent(o6.ns["ns=woodworking;i=5040"])],
)
o6.reference(o6.ns["ns=woodworking;i=5036"], "i=17603", woodworking_objtypes.IWwBaseStateType)
ns0.objtypes.BaseObjectType(
    nodeId="ns=woodworking;i=5031",
    browseName="ns=woodworking;SubUnits",
    description="The SubUnits Object is used when a machine has multiple states. For example, a CNC machine can have several places where independent jobs are produced.",
    references=[o6.hasComponent(o6.ns["ns=woodworking;i=5036"])],
)
o6.reference(o6.ns["ns=woodworking;i=5031"], "i=17603", woodworking_objtypes.IWwSubUnitsType)
ns0.objtypes.BaseObjectType(
    nodeId="ns=woodworking;i=5001",
    browseName="ns=woodworking;State",
    description="The State Object provides information about the states of the machine.",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=woodworking;i=5030"]), o6.hasComponent(o6.ns["ns=woodworking;i=5031"])],
)
o6.reference(woodworking_objtypes.WwMachineType, ns0.reftypes.HasComponent, o6.ns["ns=woodworking;i=5001"])
o6.reference(o6.ns["ns=woodworking;i=5001"], "i=17603", woodworking_objtypes.IWwStateType)
ns0.objtypes.FolderType(
    nodeId="ns=woodworking;i=35",
    browseName="ns=woodworking;ManufacturerSpecific",
    description="The ManufacturerSpecific Object provides manufacturer specific functionality.",
    modellingRule="Optional",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=woodworking;i=7808", browseName="ns=woodworking;LastProgramName", dataType=o6.String, accessLevel=3, userAccessLevel=1)
        )
    ],
)
o6.reference(woodworking_objtypes.WwMachineType, ns0.reftypes.HasComponent, o6.ns["ns=woodworking;i=35"])
machinery.objtypes.MachineIdentificationType(
    nodeId="ns=woodworking;i=5007",
    browseName="ns=di;Identification",
    description="The Identification Object provides identification information of the machine.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=woodworking;i=6015",
                browseName="ns=di;ProductInstanceUri",
                description="A globally unique resource identifier provided by the manufacturer of the machine",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=woodworking;i=6016",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=woodworking;i=6017",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=woodworking;i=6018",
                browseName="ns=di;DeviceClass",
                description="Indicates in which domain or for what purpose the MachineryItem is used.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=woodworking;i=6019",
                browseName="ns=di;Model",
                description="A human-readable, localized name of the model of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=woodworking;i=6020",
                browseName="ns=machinery;YearOfConstruction",
                description="The year (Gregorian calendar) in which the manufacturing process of the MachineryItem has been completed. It shall be a four-digit number and never change during the life-cycle of a MachineryItem.",
                dataType=o6.UInt16,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=woodworking;i=6021",
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
                nodeId="ns=woodworking;i=6022",
                browseName="ns=di;ComponentName",
                description="To be used by end users to store a human-readable localized text for the MachineryItem. The minimum number of locales supported for this property shall be two. Servers shall support at least 40 Unicode characters for the clients writing the text part of each locale, this means clients can expect to be able to write texts with a length of 40 Unicode characters into that field.",
                dataType=o6.LocalizedText,
                value=o6.LocalizedText(),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=woodworking;i=6023",
                browseName="ns=di;HardwareRevision",
                description="A string representation of the revision level of the hardware of a MachineryItem. Hardware is physical equipment, as opposed to programs, procedures, rules and associated documentation. Many machines will not provide such information due to the modular and configurable nature of the machine.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=woodworking;i=6024",
                browseName="ns=machinery;InitialOperationDate",
                description="The date, when the MachineryItem was switched on the first time after it has left the manufacturer plant.",
                dataType=o6.DateTime,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=woodworking;i=6025",
                browseName="ns=machinery;Location",
                description="To be used by end users to store the location of the machine in a scheme specific to the end user. Servers shall support at least 60 Unicode characters for the clients writing this value, this means clients can expect to be able to write strings with a length of 60 Unicode characters into that field.",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=woodworking;i=6026",
                browseName="ns=di;ManufacturerUri",
                description="A globally unique identifier of the manufacturer of the MachineryItem.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=woodworking;i=6027",
                browseName="ns=machinery;MonthOfConstruction",
                description="The month in which the manufacturing process of the MachineryItem has been completed. It shall be a number between 1 and 12, representing the month from January to December.",
                dataType=o6.Byte,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=woodworking;i=6028",
                browseName="ns=di;ProductCode",
                description="A machine-readable string of the model of the MachineryItem, that might include options like the hardware configuration of the model. This information might be provided by the ERP system of the vendor. For example, it can be used as order information.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=woodworking;i=6029",
                browseName="ns=di;SoftwareRevision",
                description="A string representation of the revision level of a MachineryItem. In most cases, MachineryItems consist of several software components. In that case, information about the software components might be provided as additional information in the address space, including individual revision information. In that case, this property is either not provided or provides an overall software revision level. The value might change during the life-cycle of a MachineryItem.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=woodworking;i=6030", browseName="ns=woodworking;LocationPlant", description="The LocationPlant provides the location of the plant.", dataType=o6.String
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=woodworking;i=6031",
                browseName="ns=woodworking;LocationGPS",
                description='The LocationGPS provides the location of the plant in GPS coordinates. The format is decimal degrees with north and east coordinates. For example, Hannover Messe has "52.3235858255059, 9.804918108600956".\nSouthern latitudes have a negative value, western longitudes as well. For example, Quito has the coordinates "-0.21975073282167099, -78.51255572531042".',
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=woodworking;i=6032",
                browseName="ns=woodworking;CustomerCompanyName",
                description="The CustomerCompanyName provides the customer name of the Woodworking manufacturer.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasComponent(
            di.vartypes.UIElementType(
                nodeId="ns=woodworking;i=7818", browseName="ns=di;UIElement", description="A user interface element assigned to this group.", _allow_abstract=True
            )
        ),
    ],
)
o6.reference(woodworking_objtypes.WwMachineType, ns0.reftypes.HasAddIn, o6.ns["ns=woodworking;i=5007"])
o6.reference(o6.ns["ns=woodworking;i=5005"], "i=17604", o6.ns["ns=woodworking;i=5007"])


del Any, TYPE_CHECKING, uuid, o6, di, ia, isa95_jobcontrol_v2, machinery, machinery_jobs, ns0, woodworking_datypes, woodworking_objtypes
