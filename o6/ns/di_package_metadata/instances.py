# Copyright (c) 2026 o6 Automation GmbH
#
# SPDX-License-Identifier: AGPL-3.0-or-later
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

"""Generated OPC UA di_package_metadata namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.ns0 as ns0
from . import datatypes as di_package_metadata_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.vartypes.PropertyType(
    nodeId="ns=di_package_metadata;i=6",
    browseName="EnumStrings",
    parent="ns=di_package_metadata;i=5",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[4],
    value=[o6.LocalizedText("Firmware"), o6.LocalizedText("Application"), o6.LocalizedText("Configuration"), o6.LocalizedText("Solution")],
)
ns0.vartypes.PropertyType(
    nodeId="ns=di_package_metadata;i=8",
    browseName="EnumStrings",
    parent="ns=di_package_metadata;i=7",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[4],
    value=[o6.LocalizedText("DeploymentItem"), o6.LocalizedText("ReleaseNotes"), o6.LocalizedText("LicenseInfo"), o6.LocalizedText("PreInstallNote")],
)
ns0.vartypes.PropertyType(
    nodeId="ns=di_package_metadata;i=10",
    browseName="EnumStrings",
    parent="ns=di_package_metadata;i=9",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[8],
    value=[
        o6.LocalizedText("EqualTo"),
        o6.LocalizedText("GreaterThan"),
        o6.LocalizedText("GreaterEqual"),
        o6.LocalizedText("LessThen"),
        o6.LocalizedText("LessEqual"),
        o6.LocalizedText("RegularExpression"),
        o6.LocalizedText("OneOf"),
        o6.LocalizedText("Exist"),
    ],
)
ns0.objtypes.DataTypeEncodingType(nodeId="ns=di_package_metadata;i=14", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=di_package_metadata;i=15", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=di_package_metadata;i=16", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=di_package_metadata;i=17", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=di_package_metadata;i=19", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=di_package_metadata;i=20", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=di_package_metadata;i=46", browseName="Default XML")
o6.hasEncoding(di_package_metadata_datypes.PackageMetadata, o6.ns["ns=di_package_metadata;i=46"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=di_package_metadata;i=47", browseName="Default XML")
o6.hasEncoding(di_package_metadata_datypes.FileDescriptor, o6.ns["ns=di_package_metadata;i=47"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=di_package_metadata;i=48", browseName="Default XML")
o6.hasEncoding(di_package_metadata_datypes.CompatibilityOption, o6.ns["ns=di_package_metadata;i=48"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=di_package_metadata;i=49", browseName="Default XML")
o6.hasEncoding(di_package_metadata_datypes.CompatibilityRequirement, o6.ns["ns=di_package_metadata;i=49"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=di_package_metadata;i=51", browseName="Default XML")
o6.hasEncoding(di_package_metadata_datypes.PackageTarget, o6.ns["ns=di_package_metadata;i=51"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=di_package_metadata;i=52", browseName="Default XML")
o6.hasEncoding(di_package_metadata_datypes.FxPathElement, o6.ns["ns=di_package_metadata;i=52"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=di_package_metadata;i=78", browseName="Default JSON")
o6.hasEncoding(di_package_metadata_datypes.PackageMetadata, o6.ns["ns=di_package_metadata;i=78"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=di_package_metadata;i=79", browseName="Default JSON")
o6.hasEncoding(di_package_metadata_datypes.FileDescriptor, o6.ns["ns=di_package_metadata;i=79"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=di_package_metadata;i=80", browseName="Default JSON")
o6.hasEncoding(di_package_metadata_datypes.CompatibilityOption, o6.ns["ns=di_package_metadata;i=80"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=di_package_metadata;i=81", browseName="Default JSON")
o6.hasEncoding(di_package_metadata_datypes.CompatibilityRequirement, o6.ns["ns=di_package_metadata;i=81"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=di_package_metadata;i=83", browseName="Default JSON")
o6.hasEncoding(di_package_metadata_datypes.PackageTarget, o6.ns["ns=di_package_metadata;i=83"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=di_package_metadata;i=84", browseName="Default JSON")
o6.hasEncoding(di_package_metadata_datypes.FxPathElement, o6.ns["ns=di_package_metadata;i=84"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=di_package_metadata;i=89", browseName="ns=di_package_metadata;PackageMetadata", dataType=o6.String, value="PackageMetadata")
o6.reference(o6.ns["ns=di_package_metadata;i=14"], "i=39", o6.ns["ns=di_package_metadata;i=89"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=di_package_metadata;i=92", browseName="ns=di_package_metadata;FileDescriptor", dataType=o6.String, value="FileDescriptor")
o6.reference(o6.ns["ns=di_package_metadata;i=15"], "i=39", o6.ns["ns=di_package_metadata;i=92"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=di_package_metadata;i=95", browseName="ns=di_package_metadata;CompatibilityOption", dataType=o6.String, value="CompatibilityOption")
o6.reference(o6.ns["ns=di_package_metadata;i=16"], "i=39", o6.ns["ns=di_package_metadata;i=95"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=di_package_metadata;i=98", browseName="ns=di_package_metadata;CompatibilityRequirement", dataType=o6.String, value="CompatibilityRequirement"
)
o6.reference(o6.ns["ns=di_package_metadata;i=17"], "i=39", o6.ns["ns=di_package_metadata;i=98"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=di_package_metadata;i=104", browseName="ns=di_package_metadata;PackageTarget", dataType=o6.String, value="PackageTarget")
o6.reference(o6.ns["ns=di_package_metadata;i=19"], "i=39", o6.ns["ns=di_package_metadata;i=104"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=di_package_metadata;i=107", browseName="ns=di_package_metadata;FxPathElement", dataType=o6.String, value="FxPathElement")
o6.reference(o6.ns["ns=di_package_metadata;i=20"], "i=39", o6.ns["ns=di_package_metadata;i=107"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=di_package_metadata;i=114", browseName="ns=di_package_metadata;PackageMetadata", dataType=o6.String, value="//xs:element[@name='PackageMetadata']"
)
o6.reference(o6.ns["ns=di_package_metadata;i=46"], "i=39", o6.ns["ns=di_package_metadata;i=114"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=di_package_metadata;i=117", browseName="ns=di_package_metadata;FileDescriptor", dataType=o6.String, value="//xs:element[@name='FileDescriptor']"
)
o6.reference(o6.ns["ns=di_package_metadata;i=47"], "i=39", o6.ns["ns=di_package_metadata;i=117"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=di_package_metadata;i=120", browseName="ns=di_package_metadata;CompatibilityOption", dataType=o6.String, value="//xs:element[@name='CompatibilityOption']"
)
o6.reference(o6.ns["ns=di_package_metadata;i=48"], "i=39", o6.ns["ns=di_package_metadata;i=120"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=di_package_metadata;i=123", browseName="ns=di_package_metadata;CompatibilityRequirement", dataType=o6.String, value="//xs:element[@name='CompatibilityRequirement']"
)
o6.reference(o6.ns["ns=di_package_metadata;i=49"], "i=39", o6.ns["ns=di_package_metadata;i=123"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=di_package_metadata;i=129", browseName="ns=di_package_metadata;PackageTarget", dataType=o6.String, value="//xs:element[@name='PackageTarget']"
)
o6.reference(o6.ns["ns=di_package_metadata;i=51"], "i=39", o6.ns["ns=di_package_metadata;i=129"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=di_package_metadata;i=132", browseName="ns=di_package_metadata;FxPathElement", dataType=o6.String, value="//xs:element[@name='FxPathElement']"
)
o6.reference(o6.ns["ns=di_package_metadata;i=52"], "i=39", o6.ns["ns=di_package_metadata;i=132"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=di_package_metadata;i=240", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=di_package_metadata;i=247", browseName="Default XML")
o6.hasEncoding(di_package_metadata_datypes.UpdateTarget, o6.ns["ns=di_package_metadata;i=247"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=di_package_metadata;i=254", browseName="Default JSON")
o6.hasEncoding(di_package_metadata_datypes.UpdateTarget, o6.ns["ns=di_package_metadata;i=254"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=di_package_metadata;i=256", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=di_package_metadata;i=260", browseName="Default XML")
o6.hasEncoding(di_package_metadata_datypes.Assignment, o6.ns["ns=di_package_metadata;i=260"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=di_package_metadata;i=264", browseName="Default JSON")
o6.hasEncoding(di_package_metadata_datypes.Assignment, o6.ns["ns=di_package_metadata;i=264"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=di_package_metadata;i=265", browseName="ns=di_package_metadata;UpdateTarget", dataType=o6.String, value="UpdateTarget")
o6.reference(o6.ns["ns=di_package_metadata;i=240"], "i=39", o6.ns["ns=di_package_metadata;i=265"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=di_package_metadata;i=268", browseName="ns=di_package_metadata;Assignment", dataType=o6.String, value="Assignment")
o6.reference(o6.ns["ns=di_package_metadata;i=256"], "i=39", o6.ns["ns=di_package_metadata;i=268"])
opcDotUaDotDiDotPackageMetadata = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=di_package_metadata;i=85",
    browseName="ns=di_package_metadata;Opc.Ua.Di.PackageMetadata",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=di_package_metadata;i=87", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/DI/PackageMetadata/")
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di_package_metadata;i=88", browseName="Deprecated", dataType=o6.Boolean, value=True)),
        o6.hasComponent(o6.ns["ns=di_package_metadata;i=89"]),
        o6.hasComponent(o6.ns["ns=di_package_metadata;i=92"]),
        o6.hasComponent(o6.ns["ns=di_package_metadata;i=95"]),
        o6.hasComponent(o6.ns["ns=di_package_metadata;i=98"]),
        o6.hasComponent(o6.ns["ns=di_package_metadata;i=104"]),
        o6.hasComponent(o6.ns["ns=di_package_metadata;i=107"]),
        o6.hasComponent(o6.ns["ns=di_package_metadata;i=265"]),
        o6.hasComponent(o6.ns["ns=di_package_metadata;i=268"]),
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary\r\n  xmlns:opc="http://opcfoundation.org/BinarySchema/"\r\n  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\r\n  xmlns:ua="http://opcfoundation.org/UA/"\r\n  xmlns:tns="http://opcfoundation.org/UA/DI/PackageMetadata/"\r\n  DefaultByteOrder="LittleEndian"\r\n  TargetNamespace="http://opcfoundation.org/UA/DI/PackageMetadata/"\r\n>\r\n  <opc:Import Namespace="http://opcfoundation.org/UA/" Location="Opc.Ua.BinarySchema.bsd"/>\r\n\r\n  <opc:StructuredType Name="PackageMetadata" BaseType="ua:ExtensionObject">\r\n    <opc:Field Name="Name" TypeName="opc:String" />\r\n    <opc:Field Name="Description" TypeName="opc:String" />\r\n    <opc:Field Name="ManufacturerUri" TypeName="opc:String" />\r\n    <opc:Field Name="Manufacturer" TypeName="opc:String" />\r\n    <opc:Field Name="PackageRevision" TypeName="opc:String" />\r\n    <opc:Field Name="PackageType" TypeName="tns:PackageType" />\r\n    <opc:Field Name="SoftwareSubClass" TypeName="opc:String" />\r\n    <opc:Field Name="DeployCompletePackage" TypeName="opc:Boolean" />\r\n    <opc:Field Name="SoftwareRevision" TypeName="opc:String" />\r\n    <opc:Field Name="ReleaseDate" TypeName="opc:DateTime" />\r\n    <opc:Field Name="TargetManufacturerUri" TypeName="opc:String" />\r\n    <opc:Field Name="TargetManufacturer" TypeName="opc:String" />\r\n    <opc:Field Name="NoOfUpdateTargets" TypeName="opc:Int32" />\r\n    <opc:Field Name="UpdateTargets" TypeName="tns:UpdateTarget" LengthField="NoOfUpdateTargets" />\r\n    <opc:Field Name="NoOfFiles" TypeName="opc:Int32" />\r\n    <opc:Field Name="Files" TypeName="tns:FileDescriptor" LengthField="NoOfFiles" />\r\n    <opc:Field Name="NoOfCompatibilities" TypeName="opc:Int32" />\r\n    <opc:Field Name="Compatibilities" TypeName="tns:CompatibilityOption" LengthField="NoOfCompatibilities" />\r\n    <opc:Field Name="NoOfAssignments" TypeName="opc:Int32" />\r\n    <opc:Field Name="Assignments" TypeName="tns:Assignment" LengthField="NoOfAssignments" />\r\n  </opc:StructuredType>\r\n\r\n  <opc:StructuredType Name="UpdateTarget" BaseType="ua:ExtensionObject">\r\n    <opc:Field Name="ProductCode" TypeName="opc:String" />\r\n    <opc:Field Name="Model" TypeName="opc:String" />\r\n  </opc:StructuredType>\r\n\r\n  <opc:StructuredType Name="FileDescriptor" BaseType="ua:ExtensionObject">\r\n    <opc:Field Name="FileType" TypeName="tns:FileType" />\r\n    <opc:Field Name="FileName" TypeName="opc:String" />\r\n    <opc:Field Name="MimeType" TypeName="opc:String" />\r\n    <opc:Field Name="Language" TypeName="opc:String" />\r\n  </opc:StructuredType>\r\n\r\n  <opc:StructuredType Name="CompatibilityOption" BaseType="ua:ExtensionObject">\r\n    <opc:Field Name="NoOfCompatibilityRequirements" TypeName="opc:Int32" />\r\n    <opc:Field Name="CompatibilityRequirements" TypeName="tns:CompatibilityRequirement" LengthField="NoOfCompatibilityRequirements" />\r\n  </opc:StructuredType>\r\n\r\n  <opc:StructuredType Name="CompatibilityRequirement" BaseType="ua:ExtensionObject">\r\n    <opc:Field Name="Variable" TypeName="opc:String" />\r\n    <opc:Field Name="NoOfValues" TypeName="opc:Int32" />\r\n    <opc:Field Name="Values" TypeName="ua:Variant" LengthField="NoOfValues" />\r\n    <opc:Field Name="Operation" TypeName="tns:ComparisonOperation" />\r\n  </opc:StructuredType>\r\n\r\n  <opc:EnumeratedType Name="PackageType" LengthInBits="32">\r\n    <opc:EnumeratedValue Name="Firmware" Value="0" />\r\n    <opc:EnumeratedValue Name="Application" Value="1" />\r\n    <opc:EnumeratedValue Name="Configuration" Value="2" />\r\n    <opc:EnumeratedValue Name="Solution" Value="3" />\r\n  </opc:EnumeratedType>\r\n\r\n  <opc:EnumeratedType Name="FileType" LengthInBits="32">\r\n    <opc:EnumeratedValue Name="DeploymentItem" Value="0" />\r\n    <opc:EnumeratedValue Name="ReleaseNotes" Value="1" />\r\n    <opc:EnumeratedValue Name="LicenseInfo" Value="2" />\r\n    <opc:EnumeratedValue Name="PreInstallNote" Value="3" />\r\n  </opc:EnumeratedType>\r\n\r\n  <opc:EnumeratedType Name="ComparisonOperation" LengthInBits="32">\r\n    <opc:EnumeratedValue Name="EqualTo" Value="0" />\r\n    <opc:EnumeratedValue Name="GreaterThan" Value="1" />\r\n    <opc:EnumeratedValue Name="GreaterEqual" Value="2" />\r\n    <opc:EnumeratedValue Name="LessThen" Value="3" />\r\n    <opc:EnumeratedValue Name="LessEqual" Value="4" />\r\n    <opc:EnumeratedValue Name="RegularExpression" Value="5" />\r\n    <opc:EnumeratedValue Name="OneOf" Value="6" />\r\n    <opc:EnumeratedValue Name="Exist" Value="7" />\r\n  </opc:EnumeratedType>\r\n\r\n  <opc:StructuredType Name="Assignment" BaseType="ua:ExtensionObject">\r\n    <opc:Field Name="Subpackage" TypeName="opc:String" />\r\n    <opc:Field Name="InstallationOrder" TypeName="opc:UInt32" />\r\n    <opc:Field Name="NoOfTargets" TypeName="opc:Int32" />\r\n    <opc:Field Name="Targets" TypeName="tns:PackageTarget" LengthField="NoOfTargets" />\r\n  </opc:StructuredType>\r\n\r\n  <opc:StructuredType Name="PackageTarget" BaseType="ua:ExtensionObject">\r\n    <opc:Field Name="TargetType" TypeName="ua:NodeId" />\r\n    <opc:Field Name="TargetNode" TypeName="ua:NodeId" />\r\n    <opc:Field Name="ProductInstanceUri" TypeName="opc:String" />\r\n    <opc:Field Name="AssetId" TypeName="opc:String" />\r\n    <opc:Field Name="ManufacturerUri" TypeName="opc:String" />\r\n    <opc:Field Name="ProductCode" TypeName="opc:String" />\r\n    <opc:Field Name="SerialNumber" TypeName="opc:String" />\r\n    <opc:Field Name="NoOfFxPath" TypeName="opc:Int32" />\r\n    <opc:Field Name="FxPath" TypeName="tns:FxPathElement" LengthField="NoOfFxPath" />\r\n    <opc:Field Name="NoOfFxScope" TypeName="opc:Int32" />\r\n    <opc:Field Name="FxScope" TypeName="tns:FxPathElement" LengthField="NoOfFxScope" />\r\n    <opc:Field Name="NoOfBrowsePath" TypeName="opc:Int32" />\r\n    <opc:Field Name="BrowsePath" TypeName="ua:RelativePathElement" LengthField="NoOfBrowsePath" />\r\n    <opc:Field Name="TargetServer" TypeName="opc:String" />\r\n  </opc:StructuredType>\r\n\r\n  <opc:StructuredType Name="FxPathElement" BaseType="ua:ExtensionObject">\r\n    <opc:Field Name="AssetConnectorType" TypeName="ua:NodeId" />\r\n    <opc:Field Name="ConnectorId" TypeName="opc:UInt16" />\r\n    <opc:Field Name="ConnectorName" TypeName="opc:String" />\r\n  </opc:StructuredType>\r\n\r\n</opc:TypeDictionary>',
)
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=di_package_metadata;i=271", browseName="ns=di_package_metadata;UpdateTarget", dataType=o6.String, value="//xs:element[@name='UpdateTarget']"
)
o6.reference(o6.ns["ns=di_package_metadata;i=247"], "i=39", o6.ns["ns=di_package_metadata;i=271"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=di_package_metadata;i=274", browseName="ns=di_package_metadata;Assignment", dataType=o6.String, value="//xs:element[@name='Assignment']"
)
o6.reference(o6.ns["ns=di_package_metadata;i=260"], "i=39", o6.ns["ns=di_package_metadata;i=274"])
opcDotUaDotDiDotPackageMetadata_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=di_package_metadata;i=110",
    browseName="ns=di_package_metadata;Opc.Ua.Di.PackageMetadata",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=di_package_metadata;i=112", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/DI/PackageMetadata/Types.xsd"
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di_package_metadata;i=113", browseName="Deprecated", dataType=o6.Boolean, value=True)),
        o6.hasComponent(o6.ns["ns=di_package_metadata;i=114"]),
        o6.hasComponent(o6.ns["ns=di_package_metadata;i=117"]),
        o6.hasComponent(o6.ns["ns=di_package_metadata;i=120"]),
        o6.hasComponent(o6.ns["ns=di_package_metadata;i=123"]),
        o6.hasComponent(o6.ns["ns=di_package_metadata;i=129"]),
        o6.hasComponent(o6.ns["ns=di_package_metadata;i=132"]),
        o6.hasComponent(o6.ns["ns=di_package_metadata;i=271"]),
        o6.hasComponent(o6.ns["ns=di_package_metadata;i=274"]),
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema\r\n  xmlns:xs="http://www.w3.org/2001/XMLSchema"\r\n  xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd"\r\n  xmlns:tns="http://opcfoundation.org/UA/DI/PackageMetadata/Types.xsd"\r\n  targetNamespace="http://opcfoundation.org/UA/DI/PackageMetadata/Types.xsd"\r\n  elementFormDefault="qualified"\r\n>\r\n  <xs:annotation>\r\n    <xs:appinfo>\r\n      <ua:Model ModelUri="http://opcfoundation.org/UA/DI/PackageMetadata/" Version="1.05.0" PublicationDate="2025-04-01T00:00:00Z" />\r\n    </xs:appinfo>\r\n  </xs:annotation>\r\n  \r\n  <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd" />\r\n\r\n  <xs:complexType name="PackageMetadata">\r\n    <xs:sequence>\r\n      <xs:element name="Name" type="xs:string" minOccurs="0" nillable="true" />\r\n      <xs:element name="Description" type="xs:string" minOccurs="0" nillable="true" />\r\n      <xs:element name="ManufacturerUri" type="xs:string" minOccurs="0" nillable="true" />\r\n      <xs:element name="Manufacturer" type="xs:string" minOccurs="0" nillable="true" />\r\n      <xs:element name="PackageRevision" type="xs:string" minOccurs="0" nillable="true" />\r\n      <xs:element name="PackageType" type="tns:PackageType" minOccurs="0" />\r\n      <xs:element name="SoftwareSubClass" type="xs:string" minOccurs="0" nillable="true" />\r\n      <xs:element name="DeployCompletePackage" type="xs:boolean" minOccurs="0" />\r\n      <xs:element name="SoftwareRevision" type="xs:string" minOccurs="0" nillable="true" />\r\n      <xs:element name="ReleaseDate" type="xs:dateTime" minOccurs="0" />\r\n      <xs:element name="TargetManufacturerUri" type="xs:string" minOccurs="0" nillable="true" />\r\n      <xs:element name="TargetManufacturer" type="xs:string" minOccurs="0" nillable="true" />\r\n      <xs:element name="UpdateTargets" type="tns:ListOfUpdateTarget" minOccurs="0" nillable="true" />\r\n      <xs:element name="Files" type="tns:ListOfFileDescriptor" minOccurs="0" nillable="true" />\r\n      <xs:element name="Compatibilities" type="tns:ListOfCompatibilityOption" minOccurs="0" nillable="true" />\r\n      <xs:element name="Assignments" type="tns:ListOfAssignment" minOccurs="0" nillable="true" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="PackageMetadata" type="tns:PackageMetadata" />\r\n\r\n  <xs:complexType name="ListOfPackageMetadata">\r\n    <xs:sequence>\r\n      <xs:element name="PackageMetadata" type="tns:PackageMetadata" minOccurs="0" maxOccurs="unbounded" nillable="true" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="ListOfPackageMetadata" type="tns:ListOfPackageMetadata" nillable="true"></xs:element>\r\n\r\n  <xs:complexType name="UpdateTarget">\r\n    <xs:sequence>\r\n      <xs:element name="ProductCode" type="xs:string" minOccurs="0" nillable="true" />\r\n      <xs:element name="Model" type="xs:string" minOccurs="0" nillable="true" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="UpdateTarget" type="tns:UpdateTarget" />\r\n\r\n  <xs:complexType name="ListOfUpdateTarget">\r\n    <xs:sequence>\r\n      <xs:element name="UpdateTarget" type="tns:UpdateTarget" minOccurs="0" maxOccurs="unbounded" nillable="true" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="ListOfUpdateTarget" type="tns:ListOfUpdateTarget" nillable="true"></xs:element>\r\n\r\n  <xs:complexType name="FileDescriptor">\r\n    <xs:sequence>\r\n      <xs:element name="FileType" type="tns:FileType" minOccurs="0" />\r\n      <xs:element name="FileName" type="xs:string" minOccurs="0" nillable="true" />\r\n      <xs:element name="MimeType" type="xs:string" minOccurs="0" nillable="true" />\r\n      <xs:element name="Language" type="xs:string" minOccurs="0" nillable="true" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="FileDescriptor" type="tns:FileDescriptor" />\r\n\r\n  <xs:complexType name="ListOfFileDescriptor">\r\n    <xs:sequence>\r\n      <xs:element name="FileDescriptor" type="tns:FileDescriptor" minOccurs="0" maxOccurs="unbounded" nillable="true" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="ListOfFileDescriptor" type="tns:ListOfFileDescriptor" nillable="true"></xs:element>\r\n\r\n  <xs:complexType name="CompatibilityOption">\r\n    <xs:sequence>\r\n      <xs:element name="CompatibilityRequirements" type="tns:ListOfCompatibilityRequirement" minOccurs="0" nillable="true" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="CompatibilityOption" type="tns:CompatibilityOption" />\r\n\r\n  <xs:complexType name="ListOfCompatibilityOption">\r\n    <xs:sequence>\r\n      <xs:element name="CompatibilityOption" type="tns:CompatibilityOption" minOccurs="0" maxOccurs="unbounded" nillable="true" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="ListOfCompatibilityOption" type="tns:ListOfCompatibilityOption" nillable="true"></xs:element>\r\n\r\n  <xs:complexType name="CompatibilityRequirement">\r\n    <xs:sequence>\r\n      <xs:element name="Variable" type="xs:string" minOccurs="0" nillable="true" />\r\n      <xs:element name="Values" type="ua:ListOfVariant" minOccurs="0" nillable="true" />\r\n      <xs:element name="Operation" type="tns:ComparisonOperation" minOccurs="0" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="CompatibilityRequirement" type="tns:CompatibilityRequirement" />\r\n\r\n  <xs:complexType name="ListOfCompatibilityRequirement">\r\n    <xs:sequence>\r\n      <xs:element name="CompatibilityRequirement" type="tns:CompatibilityRequirement" minOccurs="0" maxOccurs="unbounded" nillable="true" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="ListOfCompatibilityRequirement" type="tns:ListOfCompatibilityRequirement" nillable="true"></xs:element>\r\n\r\n  <xs:simpleType  name="PackageType">\r\n    <xs:restriction base="xs:string">\r\n      <xs:enumeration value="Firmware_0" />\r\n      <xs:enumeration value="Application_1" />\r\n      <xs:enumeration value="Configuration_2" />\r\n      <xs:enumeration value="Solution_3" />\r\n    </xs:restriction>\r\n  </xs:simpleType>\r\n  <xs:element name="PackageType" type="tns:PackageType" />\r\n\r\n  <xs:complexType name="ListOfPackageType">\r\n    <xs:sequence>\r\n      <xs:element name="PackageType" type="tns:PackageType" minOccurs="0" maxOccurs="unbounded" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="ListOfPackageType" type="tns:ListOfPackageType" nillable="true"></xs:element>\r\n\r\n  <xs:simpleType  name="FileType">\r\n    <xs:restriction base="xs:string">\r\n      <xs:enumeration value="DeploymentItem_0" />\r\n      <xs:enumeration value="ReleaseNotes_1" />\r\n      <xs:enumeration value="LicenseInfo_2" />\r\n      <xs:enumeration value="PreInstallNote_3" />\r\n    </xs:restriction>\r\n  </xs:simpleType>\r\n  <xs:element name="FileType" type="tns:FileType" />\r\n\r\n  <xs:complexType name="ListOfFileType">\r\n    <xs:sequence>\r\n      <xs:element name="FileType" type="tns:FileType" minOccurs="0" maxOccurs="unbounded" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="ListOfFileType" type="tns:ListOfFileType" nillable="true"></xs:element>\r\n\r\n  <xs:simpleType  name="ComparisonOperation">\r\n    <xs:restriction base="xs:string">\r\n      <xs:enumeration value="EqualTo_0" />\r\n      <xs:enumeration value="GreaterThan_1" />\r\n      <xs:enumeration value="GreaterEqual_2" />\r\n      <xs:enumeration value="LessThen_3" />\r\n      <xs:enumeration value="LessEqual_4" />\r\n      <xs:enumeration value="RegularExpression_5" />\r\n      <xs:enumeration value="OneOf_6" />\r\n      <xs:enumeration value="Exist_7" />\r\n    </xs:restriction>\r\n  </xs:simpleType>\r\n  <xs:element name="ComparisonOperation" type="tns:ComparisonOperation" />\r\n\r\n  <xs:complexType name="ListOfComparisonOperation">\r\n    <xs:sequence>\r\n      <xs:element name="ComparisonOperation" type="tns:ComparisonOperation" minOccurs="0" maxOccurs="unbounded" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="ListOfComparisonOperation" type="tns:ListOfComparisonOperation" nillable="true"></xs:element>\r\n\r\n  <xs:complexType name="Assignment">\r\n    <xs:sequence>\r\n      <xs:element name="Subpackage" type="xs:string" minOccurs="0" nillable="true" />\r\n      <xs:element name="InstallationOrder" type="xs:unsignedInt" minOccurs="0" />\r\n      <xs:element name="Targets" type="tns:ListOfPackageTarget" minOccurs="0" nillable="true" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="Assignment" type="tns:Assignment" />\r\n\r\n  <xs:complexType name="ListOfAssignment">\r\n    <xs:sequence>\r\n      <xs:element name="Assignment" type="tns:Assignment" minOccurs="0" maxOccurs="unbounded" nillable="true" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="ListOfAssignment" type="tns:ListOfAssignment" nillable="true"></xs:element>\r\n\r\n  <xs:complexType name="PackageTarget">\r\n    <xs:sequence>\r\n      <xs:element name="TargetType" type="ua:NodeId" minOccurs="0" nillable="true" />\r\n      <xs:element name="TargetNode" type="ua:NodeId" minOccurs="0" nillable="true" />\r\n      <xs:element name="ProductInstanceUri" type="xs:string" minOccurs="0" nillable="true" />\r\n      <xs:element name="AssetId" type="xs:string" minOccurs="0" nillable="true" />\r\n      <xs:element name="ManufacturerUri" type="xs:string" minOccurs="0" nillable="true" />\r\n      <xs:element name="ProductCode" type="xs:string" minOccurs="0" nillable="true" />\r\n      <xs:element name="SerialNumber" type="xs:string" minOccurs="0" nillable="true" />\r\n      <xs:element name="FxPath" type="tns:ListOfFxPathElement" minOccurs="0" nillable="true" />\r\n      <xs:element name="FxScope" type="tns:ListOfFxPathElement" minOccurs="0" nillable="true" />\r\n      <xs:element name="BrowsePath" type="ua:ListOfRelativePathElement" minOccurs="0" nillable="true" />\r\n      <xs:element name="TargetServer" type="xs:string" minOccurs="0" nillable="true" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="PackageTarget" type="tns:PackageTarget" />\r\n\r\n  <xs:complexType name="ListOfPackageTarget">\r\n    <xs:sequence>\r\n      <xs:element name="PackageTarget" type="tns:PackageTarget" minOccurs="0" maxOccurs="unbounded" nillable="true" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="ListOfPackageTarget" type="tns:ListOfPackageTarget" nillable="true"></xs:element>\r\n\r\n  <xs:complexType name="FxPathElement">\r\n    <xs:sequence>\r\n      <xs:element name="AssetConnectorType" type="ua:NodeId" minOccurs="0" nillable="true" />\r\n      <xs:element name="ConnectorId" type="xs:unsignedShort" minOccurs="0" />\r\n      <xs:element name="ConnectorName" type="xs:string" minOccurs="0" nillable="true" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="FxPathElement" type="tns:FxPathElement" />\r\n\r\n  <xs:complexType name="ListOfFxPathElement">\r\n    <xs:sequence>\r\n      <xs:element name="FxPathElement" type="tns:FxPathElement" minOccurs="0" maxOccurs="unbounded" nillable="true" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="ListOfFxPathElement" type="tns:ListOfFxPathElement" nillable="true"></xs:element>\r\n\r\n</xs:schema>',
)


del Any, TYPE_CHECKING, uuid, o6, ns0, di_package_metadata_datypes
