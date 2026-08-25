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

"""Generated OPC UA fdi namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
from . import datatypes as fdi_datypes
from . import vartypes as fdi_vartypes
from . import objtypes as fdi_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.vartypes.PropertyType(
    nodeId="ns=fdi;i=93",
    browseName="InputArguments",
    parent="ns=fdi;i=92",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Message", dataType=o6.String, valueRank=-1)],
)
logAuditTrailMessage = o6.call(nodeId="ns=fdi;i=92", browseName="ns=fdi;LogAuditTrailMessage", inputArgs=o6.hasProperty(o6.ns["ns=fdi;i=93"]))

fDIServerVersion = ns0.vartypes.PropertyType(
    nodeId="ns=fdi;i=94", browseName="ns=fdi;FDIServerVersion", parent="i=2253", referenceType=ns0.reftypes.HasProperty, dataType=o6.String
)
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fdi;i=95", browseName="Default XML")
o6.hasEncoding(fdi_datypes.RegistrationParameters, o6.ns["ns=fdi;i=95"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fdi;i=96", browseName="Default XML")
o6.hasEncoding(fdi_datypes.RegisteredNode, o6.ns["ns=fdi;i=96"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fdi;i=97", browseName="Default XML")
o6.hasEncoding(fdi_datypes.RegisterNodesResult, o6.ns["ns=fdi;i=97"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fdi;i=98", browseName="Default XML")
o6.hasEncoding(fdi_datypes.TransferIncident, o6.ns["ns=fdi;i=98"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fdi;i=99", browseName="Default XML")
o6.hasEncoding(fdi_datypes.ApplyResult, o6.ns["ns=fdi;i=99"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=fdi;i=103", browseName="ns=fdi;RegistrationParameters", dataType=o6.String, value="//xs:element[@name='RegistrationParameters']")
o6.reference(o6.ns["ns=fdi;i=95"], "i=39", o6.ns["ns=fdi;i=103"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=fdi;i=106", browseName="ns=fdi;RegisteredNode", dataType=o6.String, value="//xs:element[@name='RegisteredNode']")
o6.reference(o6.ns["ns=fdi;i=96"], "i=39", o6.ns["ns=fdi;i=106"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=fdi;i=109", browseName="ns=fdi;RegisterNodesResult", dataType=o6.String, value="//xs:element[@name='RegisterNodesResult']")
o6.reference(o6.ns["ns=fdi;i=97"], "i=39", o6.ns["ns=fdi;i=109"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=fdi;i=112", browseName="ns=fdi;TransferIncident", dataType=o6.String, value="//xs:element[@name='TransferIncident']")
o6.reference(o6.ns["ns=fdi;i=98"], "i=39", o6.ns["ns=fdi;i=112"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=fdi;i=115", browseName="ns=fdi;ApplyResult", dataType=o6.String, value="//xs:element[@name='ApplyResult']")
o6.reference(o6.ns["ns=fdi;i=99"], "i=39", o6.ns["ns=fdi;i=115"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fdi;i=118", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fdi;i=119", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fdi;i=120", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fdi;i=121", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fdi;i=122", browseName="Default Binary")
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=fdi;i=126", browseName="ns=fdi;RegistrationParameters", dataType=o6.String, value="RegistrationParameters")
o6.reference(o6.ns["ns=fdi;i=118"], "i=39", o6.ns["ns=fdi;i=126"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=fdi;i=129", browseName="ns=fdi;RegisteredNode", dataType=o6.String, value="RegisteredNode")
o6.reference(o6.ns["ns=fdi;i=119"], "i=39", o6.ns["ns=fdi;i=129"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=fdi;i=132", browseName="ns=fdi;RegisterNodesResult", dataType=o6.String, value="RegisterNodesResult")
o6.reference(o6.ns["ns=fdi;i=120"], "i=39", o6.ns["ns=fdi;i=132"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=fdi;i=135", browseName="ns=fdi;TransferIncident", dataType=o6.String, value="TransferIncident")
o6.reference(o6.ns["ns=fdi;i=121"], "i=39", o6.ns["ns=fdi;i=135"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=fdi;i=138", browseName="ns=fdi;ApplyResult", dataType=o6.String, value="ApplyResult")
o6.reference(o6.ns["ns=fdi;i=122"], "i=39", o6.ns["ns=fdi;i=138"])
actionIdentifier = fdi_objtypes.ActionType(nodeId="ns=fdi;i=182", browseName="ns=fdi;ActionIdentifier", _allow_abstract=True)


ns0.vartypes.PropertyType(
    nodeId="ns=fdi;i=185",
    browseName="InputArguments",
    parent="ns=fdi;i=184",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="ActionName", dataType=o6.String, valueRank=-1), ns0.datatypes.Argument(name="MethodArguments", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi;i=186",
    browseName="OutputArguments",
    parent="ns=fdi;i=184",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="ActionNodeId", dataType=o6.NodeId, valueRank=-1), ns0.datatypes.Argument(name="InvokeActionError", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=fdi;i=184", browseName="ns=fdi;InvokeAction", inputArgs=o6.hasProperty(o6.ns["ns=fdi;i=185"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi;i=186"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fdi;i=188",
    browseName="InputArguments",
    parent="ns=fdi;i=187",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="ActionNodeId", dataType=o6.NodeId, valueRank=-1), ns0.datatypes.Argument(name="Response", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi;i=189",
    browseName="OutputArguments",
    parent="ns=fdi;i=187",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="RespondActionError", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=fdi;i=187", browseName="ns=fdi;RespondAction", inputArgs=o6.hasProperty(o6.ns["ns=fdi;i=188"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi;i=189"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fdi;i=191",
    browseName="InputArguments",
    parent="ns=fdi;i=190",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ActionNodeId", dataType=o6.NodeId, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi;i=192",
    browseName="OutputArguments",
    parent="ns=fdi;i=190",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="AbortActionError", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=fdi;i=190", browseName="ns=fdi;AbortAction", inputArgs=o6.hasProperty(o6.ns["ns=fdi;i=191"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi;i=192"]))

actionSet = fdi_objtypes.ActionServiceType(
    nodeId="ns=fdi;i=183",
    browseName="ns=fdi;ActionSet",
    references=[o6.hasComponent(o6.ns["ns=fdi;i=184"]), o6.hasComponent(o6.ns["ns=fdi;i=187"]), o6.hasComponent(o6.ns["ns=fdi;i=190"])],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi;i=195",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=fdi;i=194",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("ModalWindow", "\n                ")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("NonModalWindow", "\n                ")),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("UIP", "\n                ")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi;i=197",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=fdi;i=196",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("Window", "\n                ")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Dialog", "\n                ")),
    ],
)
deviceHealthDiagnostics = ns0.vartypes.PropertyType(
    nodeId="ns=fdi;i=198",
    browseName="ns=fdi;DeviceHealthDiagnostics",
    parent="ns=di;i=1002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[0],
)
o6.reference(di.objtypes.DeviceType, ns0.reftypes.HasProperty, o6.ns["ns=fdi;i=198"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fdi;i=8001", browseName="Default JSON")
o6.hasEncoding(fdi_datypes.RegistrationParameters, o6.ns["ns=fdi;i=8001"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fdi;i=8002", browseName="Default JSON")
o6.hasEncoding(fdi_datypes.RegisteredNode, o6.ns["ns=fdi;i=8002"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fdi;i=8003", browseName="Default JSON")
o6.hasEncoding(fdi_datypes.RegisterNodesResult, o6.ns["ns=fdi;i=8003"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fdi;i=8004", browseName="Default JSON")
o6.hasEncoding(fdi_datypes.TransferIncident, o6.ns["ns=fdi;i=8004"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fdi;i=8005", browseName="Default JSON")
o6.hasEncoding(fdi_datypes.ApplyResult, o6.ns["ns=fdi;i=8005"])
opcDotUaDotFdi5_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=fdi;i=123",
    browseName="ns=fdi;Opc.Ua.Fdi5",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdi;i=125", browseName="NamespaceUri", dataType=o6.String, value="http://fdi-cooperation.com/OPCUA/FDI5/")),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=fdi;i=8006", browseName="Deprecated", dataType=o6.Boolean)
        ),
        o6.hasComponent(o6.ns["ns=fdi;i=126"]),
        o6.hasComponent(o6.ns["ns=fdi;i=129"]),
        o6.hasComponent(o6.ns["ns=fdi;i=132"]),
        o6.hasComponent(o6.ns["ns=fdi;i=135"]),
        o6.hasComponent(o6.ns["ns=fdi;i=138"]),
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary\r\n  xmlns:DI="http://opcfoundation.org/UA/DI/"\r\n  xmlns:opc="http://opcfoundation.org/BinarySchema/"\r\n  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\r\n  xmlns:ua="http://opcfoundation.org/UA/"\r\n  xmlns:tns="http://fdi-cooperation.com/OPCUA/FDI5/"\r\n  DefaultByteOrder="LittleEndian"\r\n  TargetNamespace="http://fdi-cooperation.com/OPCUA/FDI5/"\r\n>\r\n  <opc:Import Namespace="http://opcfoundation.org/UA/DI/" Location="Opc.Ua.Di.BinarySchema.bsd"/>\r\n  <opc:Import Namespace="http://opcfoundation.org/UA/" Location="Opc.Ua.BinarySchema.bsd"/>\r\n\r\n  <opc:EnumeratedType Name="WindowModeType" LengthInBits="32">\r\n    <opc:EnumeratedValue Name="ModalWindow" Value="1" />\r\n    <opc:EnumeratedValue Name="NonModalWindow" Value="2" />\r\n    <opc:EnumeratedValue Name="UIP" Value="3" />\r\n  </opc:EnumeratedType>\r\n\r\n  <opc:EnumeratedType Name="StyleType" LengthInBits="32">\r\n    <opc:EnumeratedValue Name="Window" Value="1" />\r\n    <opc:EnumeratedValue Name="Dialog" Value="2" />\r\n  </opc:EnumeratedType>\r\n\r\n  <opc:StructuredType Name="RegistrationParameters" BaseType="ua:ExtensionObject">\r\n    <opc:Field Name="Path" TypeName="ua:RelativePath" />\r\n    <opc:Field Name="SelectionFlags" TypeName="opc:UInt32" />\r\n  </opc:StructuredType>\r\n\r\n  <opc:StructuredType Name="RegisteredNode" BaseType="ua:ExtensionObject">\r\n    <opc:Field Name="NodeStatus" TypeName="opc:Int32" />\r\n    <opc:Field Name="OnlineContextNodeId" TypeName="ua:NodeId" />\r\n    <opc:Field Name="OnlineDeviceNodeId" TypeName="ua:NodeId" />\r\n    <opc:Field Name="OfflineContextNodeId" TypeName="ua:NodeId" />\r\n    <opc:Field Name="OfflineDeviceNodeId" TypeName="ua:NodeId" />\r\n  </opc:StructuredType>\r\n\r\n  <opc:StructuredType Name="RegisterNodesResult" BaseType="ua:ExtensionObject">\r\n    <opc:Field Name="Status" TypeName="opc:Int32" />\r\n    <opc:Field Name="NoOfRegisteredNodes" TypeName="opc:Int32" />\r\n    <opc:Field Name="RegisteredNodes" TypeName="tns:RegisteredNode" LengthField="NoOfRegisteredNodes" />\r\n  </opc:StructuredType>\r\n\r\n  <opc:StructuredType Name="TransferIncident" BaseType="ua:ExtensionObject">\r\n    <opc:Field Name="ContextNodeId" TypeName="ua:NodeId" />\r\n    <opc:Field Name="StatusCode" TypeName="ua:StatusCode" />\r\n    <opc:Field Name="Diagnostics" TypeName="ua:DiagnosticInfo" />\r\n  </opc:StructuredType>\r\n\r\n  <opc:StructuredType Name="ApplyResult" BaseType="ua:ExtensionObject">\r\n    <opc:Field Name="Status" TypeName="opc:Int32" />\r\n    <opc:Field Name="NoOfTransferIncidents" TypeName="opc:Int32" />\r\n    <opc:Field Name="TransferIncidents" TypeName="tns:TransferIncident" LengthField="NoOfTransferIncidents" />\r\n  </opc:StructuredType>\r\n\r\n</opc:TypeDictionary>',
)
opcDotUaDotFdi5 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=fdi;i=100",
    browseName="ns=fdi;Opc.Ua.Fdi5",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdi;i=102", browseName="NamespaceUri", dataType=o6.String, value="http://fdi-cooperation.com/OPCUA/FDI5/Types.xsd")),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=fdi;i=8008", browseName="Deprecated", dataType=o6.Boolean)
        ),
        o6.hasComponent(o6.ns["ns=fdi;i=103"]),
        o6.hasComponent(o6.ns["ns=fdi;i=106"]),
        o6.hasComponent(o6.ns["ns=fdi;i=109"]),
        o6.hasComponent(o6.ns["ns=fdi;i=112"]),
        o6.hasComponent(o6.ns["ns=fdi;i=115"]),
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema\r\n  xmlns:DI="http://opcfoundation.org/UA/DI/Types.xsd"\r\n  xmlns:xs="http://www.w3.org/2001/XMLSchema"\r\n  xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd"\r\n  xmlns:tns="http://fdi-cooperation.com/OPCUA/FDI5/Types.xsd"\r\n  targetNamespace="http://fdi-cooperation.com/OPCUA/FDI5/Types.xsd"\r\n  elementFormDefault="qualified"\r\n>\r\n  <xs:import namespace="http://opcfoundation.org/UA/DI/Types.xsd" />\r\n  <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd" />\r\n\r\n  <xs:simpleType  name="WindowModeType">\r\n    <xs:restriction base="xs:string">\r\n      <xs:enumeration value="ModalWindow_1" />\r\n      <xs:enumeration value="NonModalWindow_2" />\r\n      <xs:enumeration value="UIP_3" />\r\n    </xs:restriction>\r\n  </xs:simpleType>\r\n  <xs:element name="WindowModeType" type="tns:WindowModeType" />\r\n\r\n  <xs:complexType name="ListOfWindowModeType">\r\n    <xs:sequence>\r\n      <xs:element name="WindowModeType" type="tns:WindowModeType" minOccurs="0" maxOccurs="unbounded" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="ListOfWindowModeType" type="tns:ListOfWindowModeType" nillable="true"></xs:element>\r\n\r\n  <xs:simpleType  name="StyleType">\r\n    <xs:restriction base="xs:string">\r\n      <xs:enumeration value="Window_1" />\r\n      <xs:enumeration value="Dialog_2" />\r\n    </xs:restriction>\r\n  </xs:simpleType>\r\n  <xs:element name="StyleType" type="tns:StyleType" />\r\n\r\n  <xs:complexType name="ListOfStyleType">\r\n    <xs:sequence>\r\n      <xs:element name="StyleType" type="tns:StyleType" minOccurs="0" maxOccurs="unbounded" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="ListOfStyleType" type="tns:ListOfStyleType" nillable="true"></xs:element>\r\n\r\n  <xs:complexType name="RegistrationParameters">\r\n    <xs:sequence>\r\n      <xs:element name="Path" type="ua:RelativePath" minOccurs="0" nillable="true" />\r\n      <xs:element name="SelectionFlags" type="xs:unsignedInt" minOccurs="0" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="RegistrationParameters" type="tns:RegistrationParameters" />\r\n\r\n  <xs:complexType name="ListOfRegistrationParameters">\r\n    <xs:sequence>\r\n      <xs:element name="RegistrationParameters" type="tns:RegistrationParameters" minOccurs="0" maxOccurs="unbounded" nillable="true" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="ListOfRegistrationParameters" type="tns:ListOfRegistrationParameters" nillable="true"></xs:element>\r\n\r\n  <xs:complexType name="RegisteredNode">\r\n    <xs:sequence>\r\n      <xs:element name="NodeStatus" type="xs:int" minOccurs="0" />\r\n      <xs:element name="OnlineContextNodeId" type="ua:NodeId" minOccurs="0" nillable="true" />\r\n      <xs:element name="OnlineDeviceNodeId" type="ua:NodeId" minOccurs="0" nillable="true" />\r\n      <xs:element name="OfflineContextNodeId" type="ua:NodeId" minOccurs="0" nillable="true" />\r\n      <xs:element name="OfflineDeviceNodeId" type="ua:NodeId" minOccurs="0" nillable="true" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="RegisteredNode" type="tns:RegisteredNode" />\r\n\r\n  <xs:complexType name="ListOfRegisteredNode">\r\n    <xs:sequence>\r\n      <xs:element name="RegisteredNode" type="tns:RegisteredNode" minOccurs="0" maxOccurs="unbounded" nillable="true" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="ListOfRegisteredNode" type="tns:ListOfRegisteredNode" nillable="true"></xs:element>\r\n\r\n  <xs:complexType name="RegisterNodesResult">\r\n    <xs:sequence>\r\n      <xs:element name="Status" type="xs:int" minOccurs="0" />\r\n      <xs:element name="RegisteredNodes" type="tns:ListOfRegisteredNode" minOccurs="0" nillable="true" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="RegisterNodesResult" type="tns:RegisterNodesResult" />\r\n\r\n  <xs:complexType name="ListOfRegisterNodesResult">\r\n    <xs:sequence>\r\n      <xs:element name="RegisterNodesResult" type="tns:RegisterNodesResult" minOccurs="0" maxOccurs="unbounded" nillable="true" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="ListOfRegisterNodesResult" type="tns:ListOfRegisterNodesResult" nillable="true"></xs:element>\r\n\r\n  <xs:complexType name="TransferIncident">\r\n    <xs:sequence>\r\n      <xs:element name="ContextNodeId" type="ua:NodeId" minOccurs="0" nillable="true" />\r\n      <xs:element name="StatusCode" type="ua:StatusCode" minOccurs="0" />\r\n      <xs:element name="Diagnostics" type="ua:DiagnosticInfo" minOccurs="0" nillable="true" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="TransferIncident" type="tns:TransferIncident" />\r\n\r\n  <xs:complexType name="ListOfTransferIncident">\r\n    <xs:sequence>\r\n      <xs:element name="TransferIncident" type="tns:TransferIncident" minOccurs="0" maxOccurs="unbounded" nillable="true" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="ListOfTransferIncident" type="tns:ListOfTransferIncident" nillable="true"></xs:element>\r\n\r\n  <xs:complexType name="ApplyResult">\r\n    <xs:sequence>\r\n      <xs:element name="Status" type="xs:int" minOccurs="0" />\r\n      <xs:element name="TransferIncidents" type="tns:ListOfTransferIncident" minOccurs="0" nillable="true" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="ApplyResult" type="tns:ApplyResult" />\r\n\r\n  <xs:complexType name="ListOfApplyResult">\r\n    <xs:sequence>\r\n      <xs:element name="ApplyResult" type="tns:ApplyResult" minOccurs="0" maxOccurs="unbounded" nillable="true" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="ListOfApplyResult" type="tns:ListOfApplyResult" nillable="true"></xs:element>\r\n\r\n</xs:schema>',
)
httpColonSlashSlashFdiMinusCooperationDotComSlashOPCUASlashFDI5Slash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=fdi;i=15001",
    browseName="ns=fdi;http://fdi-cooperation.com/OPCUA/FDI5/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdi;i=15002", browseName="NamespaceUri", dataType=o6.String, value="http://fdi-cooperation.com/OPCUA/FDI5/")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdi;i=15003", browseName="NamespaceVersion", dataType=o6.String, value="1.1")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdi;i=15004", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2017-07-14T00:00:00Z"))),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=fdi;i=15005", browseName="IsNamespaceSubset", dataType=o6.Boolean)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=fdi;i=15006", browseName="StaticNodeIdTypes", dataType=ns0.datatypes.IdType, valueRank=1, arrayDimensions=[1], value=[ns0.datatypes.IdType.NUMERIC]
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=fdi;i=15007", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[1], value=["1:65535"]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdi;i=15008", browseName="StaticStringNodeIdPattern", dataType=o6.String, value="\n      ")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=fdi;i=15031", browseName="DefaultRolePermissions", dataType=ns0.datatypes.RolePermissionType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=fdi;i=15032", browseName="DefaultUserRolePermissions", dataType=ns0.datatypes.RolePermissionType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdi;i=15033", browseName="DefaultAccessRestrictions", dataType=ns0.datatypes.AccessRestrictionType)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)


del Any, TYPE_CHECKING, uuid, o6, di, ns0, fdi_datypes, fdi_vartypes, fdi_objtypes
