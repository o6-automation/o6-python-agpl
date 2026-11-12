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

"""Generated OPC UA fdt namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
from . import reftypes as fdt_reftypes
from . import datatypes as fdt_datypes
from . import vartypes as fdt_vartypes
from . import objtypes as fdt_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.objtypes.DataTypeEncodingType(nodeId="ns=fdt;i=5005", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fdt;i=5006", browseName="Default XML")
o6.hasEncoding(fdt_datypes.SemanticInfoType, o6.ns["ns=fdt;i=5006"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fdt;i=5007", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fdt;i=5012", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fdt;i=5013", browseName="Default XML")
o6.hasEncoding(fdt_datypes.DataRefType, o6.ns["ns=fdt;i=5013"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=fdt;i=5029", browseName="Default XML")
o6.hasEncoding(fdt_datypes.FdtDeviceClassificationType, o6.ns["ns=fdt;i=5029"])
ns0.vartypes.PropertyType(
    nodeId="ns=fdt;i=6001",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=fdt;i=3001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("HighHighAlarm"), description=o6.LocalizedText("Alarm if a process value exceeds ‘highhigh’ limit.")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("HighAlarm"), description=o6.LocalizedText("Alarm if a process value exceeds ‘high’ limit.")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("LowLowAlarm"), description=o6.LocalizedText("Alarm if a process value falls below ‘lowlow’ limit.")),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("LowAlarm"), description=o6.LocalizedText("Alarm if a process value falls below ‘low’ limit.")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdt;i=6002",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=fdt;i=3002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[15],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("AdjustSetValue"), description=o6.LocalizedText("Functional group is used to adjust the set value.")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("AssetManagement"), description=o6.LocalizedText("Functional group is used for asset management.")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("AuditTrail"), description=o6.LocalizedText("Functional group is used for audit trail.")),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("Configuration"), description=o6.LocalizedText("Functional group is used for configuration.")),
        ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("Diagnosis"), description=o6.LocalizedText("Functional group is used for diagnosis.")),
        ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("Force"), description=o6.LocalizedText("Functional group is used for forcing values.")),
        ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("Observe"), description=o6.LocalizedText("Functional group is used for observation of the device.")),
        ns0.datatypes.EnumValueType(
            value=7, displayName=o6.LocalizedText("OfflineCompare"), description=o6.LocalizedText("Functional group is used for comparison of offline data from different devices.")
        ),
        ns0.datatypes.EnumValueType(
            value=8, displayName=o6.LocalizedText("OfflineParameterize"), description=o6.LocalizedText("Functional group is used for offline parameterization.")
        ),
        ns0.datatypes.EnumValueType(
            value=9,
            displayName=o6.LocalizedText("OnlineCompare"),
            description=o6.LocalizedText("Functional group is used for comparison of the device dataset and the instance dataset."),
        ),
        ns0.datatypes.EnumValueType(
            value=10, displayName=o6.LocalizedText("OnlineParameterize"), description=o6.LocalizedText("Functional group is used for online parameterization.")
        ),
        ns0.datatypes.EnumValueType(value=11, displayName=o6.LocalizedText("Identify"), description=o6.LocalizedText("Functional group is used for identification.")),
        ns0.datatypes.EnumValueType(value=12, displayName=o6.LocalizedText("Calibration"), description=o6.LocalizedText("Functional group is used for calibration.")),
        ns0.datatypes.EnumValueType(
            value=13, displayName=o6.LocalizedText("MainOperation"), description=o6.LocalizedText("Functional group is the aggregation of all functional groups.")
        ),
        ns0.datatypes.EnumValueType(value=14, displayName=o6.LocalizedText("NetworkManagement"), description=o6.LocalizedText("Functional group is used for network management.")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdt;i=6003",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=fdt;i=3003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("LowerRange"), description=o6.LocalizedText("Device data represents a lower range.")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("UpperRange"), description=o6.LocalizedText("Device data represents an upper range.")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdt;i=6004",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=fdt;i=3004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("LastValue"), description=o6.LocalizedText("The last known value shall be used.")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("LastValidValue"), description=o6.LocalizedText("The last valid value shall be used.")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("UpperRange"), description=o6.LocalizedText("The upper range shall be used.")),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("LowerRange"), description=o6.LocalizedText("The lower range shall be used.")),
    ],
)
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=fdt;i=6037", browseName="ns=fdt;DataRefType", dataType=o6.String, value="DataRefType")
o6.reference(o6.ns["ns=fdt;i=5012"], "i=39", o6.ns["ns=fdt;i=6037"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=fdt;i=6038", browseName="ns=fdt;DataRefType", dataType=o6.String, value="//xs:element[@name='DataRefType']")
o6.reference(o6.ns["ns=fdt;i=5013"], "i=39", o6.ns["ns=fdt;i=6038"])
fdt_objtypes.FdtDocumentType(
    nodeId="ns=fdt;i=5009",
    browseName="ns=fdt;<DocumentLabel>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=fdt;i=6053", browseName="ns=fdt;Classification", dataType=fdt_datypes.DocumentClassification, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdt;i=6054", browseName="ns=fdt;MediaType", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
    ],
    _allow_abstract=True,
)
ns0.objtypes.FolderType(nodeId="ns=fdt;i=5008", browseName="ns=fdt;ProtocolSupport", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=fdt;i=5009"])])
o6.reference(fdt_objtypes.FdtDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=fdt;i=5008"])
ns0.vartypes.PropertyType(
    nodeId="ns=fdt;i=6058",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=fdt;i=3013",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Input"), description=o6.LocalizedText("Input signal")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("Output"), description=o6.LocalizedText("Output signal")),
    ],
)
fdt_objtypes.FdtDocumentType(
    nodeId="ns=fdt;i=5014",
    browseName="ns=fdt;<FdtDocumentIdentifier>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=fdt;i=6067", browseName="ns=fdt;Classification", dataType=fdt_datypes.DocumentClassification, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdt;i=6068", browseName="ns=fdt;MediaType", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
    ],
    _allow_abstract=True,
)
ns0.objtypes.FolderType(nodeId="ns=fdt;i=5010", browseName="ns=di;Documentation", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=fdt;i=5014"])])
o6.reference(fdt_objtypes.IFdtSupportInfoType, ns0.reftypes.HasComponent, o6.ns["ns=fdt;i=5010"])
fdt_objtypes.FdtDocumentType(
    nodeId="ns=fdt;i=5015",
    browseName="ns=fdt;<FdtProtocolSupportIdentifier>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=fdt;i=6070", browseName="ns=fdt;Classification", dataType=fdt_datypes.DocumentClassification, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdt;i=6071", browseName="ns=fdt;MediaType", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
    ],
    _allow_abstract=True,
)
ns0.objtypes.FolderType(nodeId="ns=fdt;i=5011", browseName="ns=di;ProtocolSupport", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=fdt;i=5015"])])
o6.reference(fdt_objtypes.IFdtSupportInfoType, ns0.reftypes.HasComponent, o6.ns["ns=fdt;i=5011"])
ns0.vartypes.PropertyType(
    nodeId="ns=fdt;i=6077",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=fdt;i=3009",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("None"), description=o6.LocalizedText("The DTM does not support upload / download at all.")),
        ns0.datatypes.EnumValueType(
            value=1,
            displayName=o6.LocalizedText("OnlyDownload"),
            description=o6.LocalizedText("The DTM supports only writing data to the device. Reading data to the device is not supported."),
        ),
        ns0.datatypes.EnumValueType(
            value=2,
            displayName=o6.LocalizedText("OnlyUpload"),
            description=o6.LocalizedText("The DTM supports only reading data from the device. Writing data to the device is not supported."),
        ),
        ns0.datatypes.EnumValueType(
            value=3,
            displayName=o6.LocalizedText("BothUploadAndDownload"),
            description=o6.LocalizedText("The DTM supports both reading values from the device and writing values to the device."),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdt;i=6079",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=fdt;i=3007",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[21],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("BOOL"), description=o6.LocalizedText("1 bit -> true or false")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("SINT"), description=o6.LocalizedText("Signed short integer (1byte)")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("INT"), description=o6.LocalizedText("Signed integer (2 byte)")),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("DINT"), description=o6.LocalizedText("Signed double integer (4 byte)")),
        ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("LINT"), description=o6.LocalizedText("Signed long integer (8 byte)")),
        ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("USINT"), description=o6.LocalizedText("Unsigned short integer (1 byte)")),
        ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("UINT"), description=o6.LocalizedText("Unsigned integer (2 byte)")),
        ns0.datatypes.EnumValueType(value=7, displayName=o6.LocalizedText("UDINT"), description=o6.LocalizedText("Unsigned double integer (4 byte)")),
        ns0.datatypes.EnumValueType(value=8, displayName=o6.LocalizedText("ULINT"), description=o6.LocalizedText("Unsigned long integer (8 byte)")),
        ns0.datatypes.EnumValueType(value=9, displayName=o6.LocalizedText("REAL"), description=o6.LocalizedText("Floating point (4 byte)")),
        ns0.datatypes.EnumValueType(value=10, displayName=o6.LocalizedText("LREAL"), description=o6.LocalizedText("Long floating point (8 byte)")),
        ns0.datatypes.EnumValueType(value=11, displayName=o6.LocalizedText("TIME"), description=o6.LocalizedText("Time")),
        ns0.datatypes.EnumValueType(value=12, displayName=o6.LocalizedText("DATE"), description=o6.LocalizedText("Calendar date")),
        ns0.datatypes.EnumValueType(value=13, displayName=o6.LocalizedText("TimeOfDay"), description=o6.LocalizedText("Clock time")),
        ns0.datatypes.EnumValueType(value=14, displayName=o6.LocalizedText("DateAndTime"), description=o6.LocalizedText("Date and time")),
        ns0.datatypes.EnumValueType(value=15, displayName=o6.LocalizedText("STRING"), description=o6.LocalizedText("Variable-length single-byte character string")),
        ns0.datatypes.EnumValueType(value=16, displayName=o6.LocalizedText("BYTE"), description=o6.LocalizedText("8 bit")),
        ns0.datatypes.EnumValueType(value=17, displayName=o6.LocalizedText("WORD"), description=o6.LocalizedText("16 bit")),
        ns0.datatypes.EnumValueType(value=18, displayName=o6.LocalizedText("DWORD"), description=o6.LocalizedText("32 bit")),
        ns0.datatypes.EnumValueType(value=19, displayName=o6.LocalizedText("LWORD"), description=o6.LocalizedText("64 bit")),
        ns0.datatypes.EnumValueType(value=20, displayName=o6.LocalizedText("WSTRING"), description=o6.LocalizedText("Variable-length double-byte character string")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdt;i=6082",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=fdt;i=3012",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Cancel"), description=o6.LocalizedText("The function was canceled.")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("Success"), description=o6.LocalizedText("The function finished execution successfully.")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Fail"), description=o6.LocalizedText("The function execution failed.")),
    ],
)
http_opcfoundation_org_UA_FDT_ = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=fdt;i=5002",
    browseName="ns=fdt;http://opcfoundation.org/UA/FDT/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdt;i=6080", browseName="IsNamespaceSubset", dataType=o6.Boolean, value=False)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdt;i=6083", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2021-08-06T00:00:00Z"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdt;i=6084", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/FDT/")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdt;i=6085", browseName="NamespaceVersion", dataType=o6.String, value="1.01.00")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=fdt;i=6086", browseName="StaticNodeIdTypes", dataType=ns0.datatypes.IdType, valueRank=1, arrayDimensions=[1], value=[ns0.datatypes.IdType.NUMERIC]
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=fdt;i=6087", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[1], value=["1:2147483647"]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdt;i=6088", browseName="StaticStringNodeIdPattern", dataType=o6.String, value="\n      ")),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
fdt_objtypes.FdtDocumentType(
    nodeId="ns=fdt;i=5004",
    browseName="ns=fdt;<DocumentLabel>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=fdt;i=6090", browseName="ns=fdt;Classification", dataType=fdt_datypes.DocumentClassification, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdt;i=6091", browseName="ns=fdt;MediaType", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
    ],
    _allow_abstract=True,
)
ns0.objtypes.FolderType(nodeId="ns=fdt;i=5003", browseName="ns=fdt;Documentation", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=fdt;i=5004"])])
o6.reference(fdt_objtypes.FdtDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=fdt;i=5003"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=fdt;i=6092", browseName="ns=fdt;SemanticInfoType", dataType=o6.String, value="SemanticInfoType")
o6.reference(o6.ns["ns=fdt;i=5005"], "i=39", o6.ns["ns=fdt;i=6092"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=fdt;i=6093", browseName="ns=fdt;SemanticInfoType", dataType=o6.String, value="//xs:element[@name='SemanticInfoType']")
o6.reference(o6.ns["ns=fdt;i=5006"], "i=39", o6.ns["ns=fdt;i=6093"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fdt;i=6133", browseName="ns=fdt;FdtDeviceClassificationType", dataType=o6.String, value="FdtDeviceClassificationType", historizing=True
)
o6.reference(o6.ns["ns=fdt;i=5007"], "i=39", o6.ns["ns=fdt;i=6133"])
project_Namespace = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=fdt;i=6006",
    browseName="ns=fdt;Project_Namespace",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/FDT/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=fdt;i=6007", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/FDT/", historizing=True)
        ),
        o6.hasComponent(o6.ns["ns=fdt;i=6037"]),
        o6.hasComponent(o6.ns["ns=fdt;i=6092"]),
        o6.hasComponent(o6.ns["ns=fdt;i=6133"]),
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:tns="http://opcfoundation.org/UA/FDT/" DefaultByteOrder="LittleEndian" xmlns:opc="http://opcfoundation.org/BinarySchema/" xmlns:ua="http://opcfoundation.org/UA/" TargetNamespace="http://opcfoundation.org/UA/FDT/">\n <opc:Import Namespace="http://opcfoundation.org/UA/"/>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="DataRefType">\n  <opc:Documentation>Reference to a data item</opc:Documentation>\n  <opc:Field TypeName="opc:CharArray" Name="DataId"/>\n  <opc:Field TypeName="tns:SemanticInfoType" Name="SemanticInfo"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="FdtDeviceClassificationType">\n  <opc:Field TypeName="tns:ClassificationDomainId" Name="ClassificationDomain"/>\n  <opc:Field TypeName="tns:ClassificationId" Name="DeviceClassification"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="SemanticInfoType">\n  <opc:Field TypeName="opc:CharArray" Name="ApplicationDomain"/>\n  <opc:Field TypeName="opc:CharArray" Name="SemanticId"/>\n </opc:StructuredType>\n <opc:EnumeratedType LengthInBits="32" Name="AlarmType">\n  <opc:Documentation>Identifier for the alarm type to show the association between high- and low alarm and high-high- and low-low-alarm. (Provides mapping for Fdt.Dtm.DataAccess.AlarmType.)</opc:Documentation>\n  <opc:EnumeratedValue Name="HighHighAlarm" Value="0"/>\n  <opc:EnumeratedValue Name="HighAlarm" Value="1"/>\n  <opc:EnumeratedValue Name="LowLowAlarm" Value="2"/>\n  <opc:EnumeratedValue Name="LowAlarm" Value="3"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="ApplicationIdEnumeration">\n  <opc:Documentation>Identifies type of an application or function. (Provides mapping for Fdt.ApplicationId)</opc:Documentation>\n  <opc:EnumeratedValue Name="AdjustSetValue" Value="0"/>\n  <opc:EnumeratedValue Name="AssetManagement" Value="1"/>\n  <opc:EnumeratedValue Name="AuditTrail" Value="2"/>\n  <opc:EnumeratedValue Name="Configuration" Value="3"/>\n  <opc:EnumeratedValue Name="Diagnosis" Value="4"/>\n  <opc:EnumeratedValue Name="Force" Value="5"/>\n  <opc:EnumeratedValue Name="Observe" Value="6"/>\n  <opc:EnumeratedValue Name="OfflineCompare" Value="7"/>\n  <opc:EnumeratedValue Name="OfflineParameterize" Value="8"/>\n  <opc:EnumeratedValue Name="OnlineCompare" Value="9"/>\n  <opc:EnumeratedValue Name="OnlineParameterize" Value="10"/>\n  <opc:EnumeratedValue Name="Identify" Value="11"/>\n  <opc:EnumeratedValue Name="Calibration" Value="12"/>\n  <opc:EnumeratedValue Name="MainOperation" Value="13"/>\n  <opc:EnumeratedValue Name="NetworkManagement" Value="14"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="ClassificationDomainId">\n  <opc:EnumeratedValue Name="PowerDistribution" Value="0"/>\n  <opc:EnumeratedValue Name="MotionControl" Value="1"/>\n  <opc:EnumeratedValue Name="Measurement" Value="2"/>\n  <opc:EnumeratedValue Name="OperatorInterface" Value="3"/>\n  <opc:EnumeratedValue Name="ModulesAndControllers" Value="4"/>\n  <opc:EnumeratedValue Name="Communication" Value="5"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="ClassificationId">\n  <opc:Documentation>Classification according to device primary function. \n(Provides mapping to Fdt.Dtm.DeviceClassification.ClassificationId)</opc:Documentation>\n  <opc:EnumeratedValue Name="Flow" Value="0"/>\n  <opc:EnumeratedValue Name="Level" Value="1"/>\n  <opc:EnumeratedValue Name="Pressure" Value="2"/>\n  <opc:EnumeratedValue Name="Temperature" Value="3"/>\n  <opc:EnumeratedValue Name="Valve" Value="4"/>\n  <opc:EnumeratedValue Name="Positioner" Value="5"/>\n  <opc:EnumeratedValue Name="Actuator" Value="6"/>\n  <opc:EnumeratedValue Name="Nc_rc" Value="7"/>\n  <opc:EnumeratedValue Name="Encoder" Value="8"/>\n  <opc:EnumeratedValue Name="SpeedDrive" Value="9"/>\n  <opc:EnumeratedValue Name="Hmi" Value="10"/>\n  <opc:EnumeratedValue Name="AnalogInput" Value="11"/>\n  <opc:EnumeratedValue Name="AnalogOutput" Value="12"/>\n  <opc:EnumeratedValue Name="DigitalInput" Value="13"/>\n  <opc:EnumeratedValue Name="DigitalOutput" Value="14"/>\n  <opc:EnumeratedValue Name="ElectrochemicalAnalyser" Value="15"/>\n  <opc:EnumeratedValue Name="DtmSpecific" Value="16"/>\n  <opc:EnumeratedValue Name="Universal" Value="17"/>\n  <opc:EnumeratedValue Name="Analyser" Value="18"/>\n  <opc:EnumeratedValue Name="RemoteIO" Value="19"/>\n  <opc:EnumeratedValue Name="AnalogCombinedIO" Value="20"/>\n  <opc:EnumeratedValue Name="DigitalCombinedIO" Value="21"/>\n  <opc:EnumeratedValue Name="Recorder" Value="22"/>\n  <opc:EnumeratedValue Name="Controller" Value="23"/>\n  <opc:EnumeratedValue Name="Angle" Value="24"/>\n  <opc:EnumeratedValue Name="LimitSwitch" Value="25"/>\n  <opc:EnumeratedValue Name="Converter" Value="26"/>\n  <opc:EnumeratedValue Name="Motor" Value="27"/>\n  <opc:EnumeratedValue Name="Switchboard" Value="28"/>\n  <opc:EnumeratedValue Name="CircuitBreaker" Value="29"/>\n  <opc:EnumeratedValue Name="PowerMonitoring" Value="30"/>\n  <opc:EnumeratedValue Name="DistributionPanel" Value="31"/>\n  <opc:EnumeratedValue Name="Contactor" Value="32"/>\n  <opc:EnumeratedValue Name="ProtectionStarter" Value="33"/>\n  <opc:EnumeratedValue Name="SoftStarter" Value="34"/>\n  <opc:EnumeratedValue Name="Drive" Value="35"/>\n  <opc:EnumeratedValue Name="AxisControl" Value="36"/>\n  <opc:EnumeratedValue Name="MotorControlCenter" Value="37"/>\n  <opc:EnumeratedValue Name="ControlValve" Value="38"/>\n  <opc:EnumeratedValue Name="Electrical" Value="39"/>\n  <opc:EnumeratedValue Name="Density" Value="40"/>\n  <opc:EnumeratedValue Name="Quality" Value="41"/>\n  <opc:EnumeratedValue Name="SpeedOrRotaryFrequency" Value="42"/>\n  <opc:EnumeratedValue Name="Radiation" Value="43"/>\n  <opc:EnumeratedValue Name="WeightMass" Value="44"/>\n  <opc:EnumeratedValue Name="DistanceOrPositionPresence" Value="45"/>\n  <opc:EnumeratedValue Name="PushButton" Value="46"/>\n  <opc:EnumeratedValue Name="Joystick" Value="47"/>\n  <opc:EnumeratedValue Name="Keypad" Value="48"/>\n  <opc:EnumeratedValue Name="PilotLight" Value="49"/>\n  <opc:EnumeratedValue Name="StackLight" Value="50"/>\n  <opc:EnumeratedValue Name="Display" Value="51"/>\n  <opc:EnumeratedValue Name="CombinedButtonsAndLights" Value="52"/>\n  <opc:EnumeratedValue Name="OperatorStation" Value="53"/>\n  <opc:EnumeratedValue Name="GeneralInput" Value="54"/>\n  <opc:EnumeratedValue Name="GeneralOutput" Value="55"/>\n  <opc:EnumeratedValue Name="CombinedInputOutput" Value="56"/>\n  <opc:EnumeratedValue Name="Relay" Value="57"/>\n  <opc:EnumeratedValue Name="Timer" Value="58"/>\n  <opc:EnumeratedValue Name="Scanner" Value="59"/>\n  <opc:EnumeratedValue Name="ProgrammableController" Value="60"/>\n  <opc:EnumeratedValue Name="CommunicationAdapter" Value="61"/>\n  <opc:EnumeratedValue Name="Gateway" Value="62"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="DocumentClassification">\n  <opc:Documentation>Classification of a document. (Provides mapping for Fdt.Dtm.DocumentClassification)</opc:Documentation>\n  <opc:EnumeratedValue Name="Help" Value="0"/>\n  <opc:EnumeratedValue Name="TechnicalDocumentation" Value="1"/>\n  <opc:EnumeratedValue Name="OrderingInformation" Value="2"/>\n  <opc:EnumeratedValue Name="Miscellaneous" Value="3"/>\n  <opc:EnumeratedValue Name="TenderSpecification" Value="4"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="FunctionExecutionResultState">\n  <opc:EnumeratedValue Name="Cancel" Value="0"/>\n  <opc:EnumeratedValue Name="Success" Value="1"/>\n  <opc:EnumeratedValue Name="Fail" Value="2"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="IECDatatype">\n  <opc:EnumeratedValue Name="BOOL" Value="0"/>\n  <opc:EnumeratedValue Name="SINT" Value="1"/>\n  <opc:EnumeratedValue Name="INT" Value="2"/>\n  <opc:EnumeratedValue Name="DINT" Value="3"/>\n  <opc:EnumeratedValue Name="LINT" Value="4"/>\n  <opc:EnumeratedValue Name="USINT" Value="5"/>\n  <opc:EnumeratedValue Name="UINT" Value="6"/>\n  <opc:EnumeratedValue Name="UDINT" Value="7"/>\n  <opc:EnumeratedValue Name="ULINT" Value="8"/>\n  <opc:EnumeratedValue Name="REAL" Value="9"/>\n  <opc:EnumeratedValue Name="LREAL" Value="10"/>\n  <opc:EnumeratedValue Name="TIME" Value="11"/>\n  <opc:EnumeratedValue Name="DATE" Value="12"/>\n  <opc:EnumeratedValue Name="TimeOfDay" Value="13"/>\n  <opc:EnumeratedValue Name="DateAndTime" Value="14"/>\n  <opc:EnumeratedValue Name="STRING" Value="15"/>\n  <opc:EnumeratedValue Name="BYTE" Value="16"/>\n  <opc:EnumeratedValue Name="WORD" Value="17"/>\n  <opc:EnumeratedValue Name="DWORD" Value="18"/>\n  <opc:EnumeratedValue Name="LWORD" Value="19"/>\n  <opc:EnumeratedValue Name="WSTRING" Value="20"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="RangeType">\n  <opc:Documentation>Type of a range device data. (Provides mapping to Fdt.Dtm.DataAccess.RangeType)</opc:Documentation>\n  <opc:EnumeratedValue Name="LowerRange" Value="0"/>\n  <opc:EnumeratedValue Name="UpperRange" Value="1"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="SignalTypeEnumeration">\n  <opc:EnumeratedValue Name="Input" Value="0"/>\n  <opc:EnumeratedValue Name="Output" Value="1"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="SubstitutionType">\n  <opc:Documentation>Type of substitution data. (Provides mapping to Fdt.Dtm.DataAccess.SubstitutionType)</opc:Documentation>\n  <opc:EnumeratedValue Name="LastValue" Value="0"/>\n  <opc:EnumeratedValue Name="LastValidValue" Value="1"/>\n  <opc:EnumeratedValue Name="UpperRange" Value="2"/>\n  <opc:EnumeratedValue Name="LowerRange" Value="3"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="SupportedTransfer">\n  <opc:Documentation>This enumeration provides values to describe the types of transfers provided for a device. (Provides mapping to Fdt.Dtm.SupportedTransfer)</opc:Documentation>\n  <opc:EnumeratedValue Name="None" Value="0"/>\n  <opc:EnumeratedValue Name="OnlyDownload" Value="1"/>\n  <opc:EnumeratedValue Name="OnlyUpload" Value="2"/>\n  <opc:EnumeratedValue Name="BothUploadAndDownload" Value="3"/>\n </opc:EnumeratedType>\n</opc:TypeDictionary>\n',
)
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=fdt;i=6134", browseName="ns=fdt;FdtDeviceClassificationType", dataType=o6.String, value="//xs:element[@name='FdtDeviceClassificationType']", historizing=True
)
o6.reference(o6.ns["ns=fdt;i=5029"], "i=39", o6.ns["ns=fdt;i=6134"])
project_Namespace_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=fdt;i=6008",
    browseName="ns=fdt;Project_Namespace",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/FDT/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=fdt;i=6009", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/FDT/Types.xsd", historizing=True)
        ),
        o6.hasComponent(o6.ns["ns=fdt;i=6038"]),
        o6.hasComponent(o6.ns["ns=fdt;i=6093"]),
        o6.hasComponent(o6.ns["ns=fdt;i=6134"]),
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema elementFormDefault="qualified" targetNamespace="http://opcfoundation.org/UA/FDT/Types.xsd" xmlns:tns="http://opcfoundation.org/UA/FDT/Types.xsd" xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd" xmlns:xs="http://www.w3.org/2001/XMLSchema">\n <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd"/>\n <xs:simpleType name="AlarmType">\n  <xs:annotation>\n   <xs:documentation>Identifier for the alarm type to show the association between high- and low alarm and high-high- and low-low-alarm. (Provides mapping for Fdt.Dtm.DataAccess.AlarmType.)</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="HighHighAlarm_0"/>\n   <xs:enumeration value="HighAlarm_1"/>\n   <xs:enumeration value="LowLowAlarm_2"/>\n   <xs:enumeration value="LowAlarm_3"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:AlarmType" name="AlarmType"/>\n <xs:complexType name="ListOfAlarmType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:AlarmType" name="AlarmType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfAlarmType" name="ListOfAlarmType" nillable="true"/>\n <xs:simpleType name="ApplicationIdEnumeration">\n  <xs:annotation>\n   <xs:documentation>Identifies type of an application or function. (Provides mapping for Fdt.ApplicationId)</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="AdjustSetValue_0"/>\n   <xs:enumeration value="AssetManagement_1"/>\n   <xs:enumeration value="AuditTrail_2"/>\n   <xs:enumeration value="Configuration_3"/>\n   <xs:enumeration value="Diagnosis_4"/>\n   <xs:enumeration value="Force_5"/>\n   <xs:enumeration value="Observe_6"/>\n   <xs:enumeration value="OfflineCompare_7"/>\n   <xs:enumeration value="OfflineParameterize_8"/>\n   <xs:enumeration value="OnlineCompare_9"/>\n   <xs:enumeration value="OnlineParameterize_10"/>\n   <xs:enumeration value="Identify_11"/>\n   <xs:enumeration value="Calibration_12"/>\n   <xs:enumeration value="MainOperation_13"/>\n   <xs:enumeration value="NetworkManagement_14"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:ApplicationIdEnumeration" name="ApplicationIdEnumeration"/>\n <xs:complexType name="ListOfApplicationIdEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ApplicationIdEnumeration" name="ApplicationIdEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfApplicationIdEnumeration" name="ListOfApplicationIdEnumeration" nillable="true"/>\n <xs:simpleType name="ClassificationDomainId">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="PowerDistribution_0"/>\n   <xs:enumeration value="MotionControl_1"/>\n   <xs:enumeration value="Measurement_2"/>\n   <xs:enumeration value="OperatorInterface_3"/>\n   <xs:enumeration value="ModulesAndControllers_4"/>\n   <xs:enumeration value="Communication_5"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:ClassificationDomainId" name="ClassificationDomainId"/>\n <xs:complexType name="ListOfClassificationDomainId">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ClassificationDomainId" name="ClassificationDomainId" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfClassificationDomainId" name="ListOfClassificationDomainId" nillable="true"/>\n <xs:simpleType name="ClassificationId">\n  <xs:annotation>\n   <xs:documentation>Classification according to device primary function. \n(Provides mapping to Fdt.Dtm.DeviceClassification.ClassificationId)</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Flow_0"/>\n   <xs:enumeration value="Level_1"/>\n   <xs:enumeration value="Pressure_2"/>\n   <xs:enumeration value="Temperature_3"/>\n   <xs:enumeration value="Valve_4"/>\n   <xs:enumeration value="Positioner_5"/>\n   <xs:enumeration value="Actuator_6"/>\n   <xs:enumeration value="Nc_rc_7"/>\n   <xs:enumeration value="Encoder_8"/>\n   <xs:enumeration value="SpeedDrive_9"/>\n   <xs:enumeration value="Hmi_10"/>\n   <xs:enumeration value="AnalogInput_11"/>\n   <xs:enumeration value="AnalogOutput_12"/>\n   <xs:enumeration value="DigitalInput_13"/>\n   <xs:enumeration value="DigitalOutput_14"/>\n   <xs:enumeration value="ElectrochemicalAnalyser_15"/>\n   <xs:enumeration value="DtmSpecific_16"/>\n   <xs:enumeration value="Universal_17"/>\n   <xs:enumeration value="Analyser_18"/>\n   <xs:enumeration value="RemoteIO_19"/>\n   <xs:enumeration value="AnalogCombinedIO_20"/>\n   <xs:enumeration value="DigitalCombinedIO_21"/>\n   <xs:enumeration value="Recorder_22"/>\n   <xs:enumeration value="Controller_23"/>\n   <xs:enumeration value="Angle_24"/>\n   <xs:enumeration value="LimitSwitch_25"/>\n   <xs:enumeration value="Converter_26"/>\n   <xs:enumeration value="Motor_27"/>\n   <xs:enumeration value="Switchboard_28"/>\n   <xs:enumeration value="CircuitBreaker_29"/>\n   <xs:enumeration value="PowerMonitoring_30"/>\n   <xs:enumeration value="DistributionPanel_31"/>\n   <xs:enumeration value="Contactor_32"/>\n   <xs:enumeration value="ProtectionStarter_33"/>\n   <xs:enumeration value="SoftStarter_34"/>\n   <xs:enumeration value="Drive_35"/>\n   <xs:enumeration value="AxisControl_36"/>\n   <xs:enumeration value="MotorControlCenter_37"/>\n   <xs:enumeration value="ControlValve_38"/>\n   <xs:enumeration value="Electrical_39"/>\n   <xs:enumeration value="Density_40"/>\n   <xs:enumeration value="Quality_41"/>\n   <xs:enumeration value="SpeedOrRotaryFrequency_42"/>\n   <xs:enumeration value="Radiation_43"/>\n   <xs:enumeration value="WeightMass_44"/>\n   <xs:enumeration value="DistanceOrPositionPresence_45"/>\n   <xs:enumeration value="PushButton_46"/>\n   <xs:enumeration value="Joystick_47"/>\n   <xs:enumeration value="Keypad_48"/>\n   <xs:enumeration value="PilotLight_49"/>\n   <xs:enumeration value="StackLight_50"/>\n   <xs:enumeration value="Display_51"/>\n   <xs:enumeration value="CombinedButtonsAndLights_52"/>\n   <xs:enumeration value="OperatorStation_53"/>\n   <xs:enumeration value="GeneralInput_54"/>\n   <xs:enumeration value="GeneralOutput_55"/>\n   <xs:enumeration value="CombinedInputOutput_56"/>\n   <xs:enumeration value="Relay_57"/>\n   <xs:enumeration value="Timer_58"/>\n   <xs:enumeration value="Scanner_59"/>\n   <xs:enumeration value="ProgrammableController_60"/>\n   <xs:enumeration value="CommunicationAdapter_61"/>\n   <xs:enumeration value="Gateway_62"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:ClassificationId" name="ClassificationId"/>\n <xs:complexType name="ListOfClassificationId">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ClassificationId" name="ClassificationId" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfClassificationId" name="ListOfClassificationId" nillable="true"/>\n <xs:simpleType name="DocumentClassification">\n  <xs:annotation>\n   <xs:documentation>Classification of a document. (Provides mapping for Fdt.Dtm.DocumentClassification)</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Help_0"/>\n   <xs:enumeration value="TechnicalDocumentation_1"/>\n   <xs:enumeration value="OrderingInformation_2"/>\n   <xs:enumeration value="Miscellaneous_3"/>\n   <xs:enumeration value="TenderSpecification_4"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:DocumentClassification" name="DocumentClassification"/>\n <xs:complexType name="ListOfDocumentClassification">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:DocumentClassification" name="DocumentClassification" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfDocumentClassification" name="ListOfDocumentClassification" nillable="true"/>\n <xs:simpleType name="FunctionExecutionResultState">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Cancel_0"/>\n   <xs:enumeration value="Success_1"/>\n   <xs:enumeration value="Fail_2"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:FunctionExecutionResultState" name="FunctionExecutionResultState"/>\n <xs:complexType name="ListOfFunctionExecutionResultState">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:FunctionExecutionResultState" name="FunctionExecutionResultState" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfFunctionExecutionResultState" name="ListOfFunctionExecutionResultState" nillable="true"/>\n <xs:simpleType name="IECDatatype">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="BOOL_0"/>\n   <xs:enumeration value="SINT_1"/>\n   <xs:enumeration value="INT_2"/>\n   <xs:enumeration value="DINT_3"/>\n   <xs:enumeration value="LINT_4"/>\n   <xs:enumeration value="USINT_5"/>\n   <xs:enumeration value="UINT_6"/>\n   <xs:enumeration value="UDINT_7"/>\n   <xs:enumeration value="ULINT_8"/>\n   <xs:enumeration value="REAL_9"/>\n   <xs:enumeration value="LREAL_10"/>\n   <xs:enumeration value="TIME_11"/>\n   <xs:enumeration value="DATE_12"/>\n   <xs:enumeration value="TimeOfDay_13"/>\n   <xs:enumeration value="DateAndTime_14"/>\n   <xs:enumeration value="STRING_15"/>\n   <xs:enumeration value="BYTE_16"/>\n   <xs:enumeration value="WORD_17"/>\n   <xs:enumeration value="DWORD_18"/>\n   <xs:enumeration value="LWORD_19"/>\n   <xs:enumeration value="WSTRING_20"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:IECDatatype" name="IECDatatype"/>\n <xs:complexType name="ListOfIECDatatype">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:IECDatatype" name="IECDatatype" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfIECDatatype" name="ListOfIECDatatype" nillable="true"/>\n <xs:simpleType name="RangeType">\n  <xs:annotation>\n   <xs:documentation>Type of a range device data. (Provides mapping to Fdt.Dtm.DataAccess.RangeType)</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="LowerRange_0"/>\n   <xs:enumeration value="UpperRange_1"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:RangeType" name="RangeType"/>\n <xs:complexType name="ListOfRangeType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:RangeType" name="RangeType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfRangeType" name="ListOfRangeType" nillable="true"/>\n <xs:simpleType name="SignalTypeEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Input_0"/>\n   <xs:enumeration value="Output_1"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:SignalTypeEnumeration" name="SignalTypeEnumeration"/>\n <xs:complexType name="ListOfSignalTypeEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:SignalTypeEnumeration" name="SignalTypeEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfSignalTypeEnumeration" name="ListOfSignalTypeEnumeration" nillable="true"/>\n <xs:simpleType name="SubstitutionType">\n  <xs:annotation>\n   <xs:documentation>Type of substitution data. (Provides mapping to Fdt.Dtm.DataAccess.SubstitutionType)</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="LastValue_0"/>\n   <xs:enumeration value="LastValidValue_1"/>\n   <xs:enumeration value="UpperRange_2"/>\n   <xs:enumeration value="LowerRange_3"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:SubstitutionType" name="SubstitutionType"/>\n <xs:complexType name="ListOfSubstitutionType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:SubstitutionType" name="SubstitutionType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfSubstitutionType" name="ListOfSubstitutionType" nillable="true"/>\n <xs:simpleType name="SupportedTransfer">\n  <xs:annotation>\n   <xs:documentation>This enumeration provides values to describe the types of transfers provided for a device. (Provides mapping to Fdt.Dtm.SupportedTransfer)</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="None_0"/>\n   <xs:enumeration value="OnlyDownload_1"/>\n   <xs:enumeration value="OnlyUpload_2"/>\n   <xs:enumeration value="BothUploadAndDownload_3"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:SupportedTransfer" name="SupportedTransfer"/>\n <xs:complexType name="ListOfSupportedTransfer">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:SupportedTransfer" name="SupportedTransfer" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfSupportedTransfer" name="ListOfSupportedTransfer" nillable="true"/>\n <xs:complexType name="DataRefType">\n  <xs:annotation>\n   <xs:documentation>Reference to a data item</xs:documentation>\n  </xs:annotation>\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="DataId"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:SemanticInfoType" name="SemanticInfo"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:DataRefType" name="DataRefType"/>\n <xs:complexType name="ListOfDataRefType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:DataRefType" name="DataRefType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfDataRefType" name="ListOfDataRefType" nillable="true"/>\n <xs:complexType name="FdtDeviceClassificationType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:ClassificationDomainId" name="ClassificationDomain"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:ClassificationId" name="DeviceClassification"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:FdtDeviceClassificationType" name="FdtDeviceClassificationType"/>\n <xs:complexType name="ListOfFdtDeviceClassificationType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:FdtDeviceClassificationType" name="FdtDeviceClassificationType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfFdtDeviceClassificationType" name="ListOfFdtDeviceClassificationType" nillable="true"/>\n <xs:complexType name="SemanticInfoType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="ApplicationDomain"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="SemanticId"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:SemanticInfoType" name="SemanticInfoType"/>\n <xs:complexType name="ListOfSemanticInfoType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:SemanticInfoType" name="SemanticInfoType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfSemanticInfoType" name="ListOfSemanticInfoType" nillable="true"/>\n</xs:schema>\n',
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdt;i=6440",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=fdt;i=3010",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Help"), description=o6.LocalizedText("Document contains help information.")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("TechnicalDocumentation"), description=o6.LocalizedText("Document contains technical information.")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("OrderingInformation"), description=o6.LocalizedText("Document contains order information.")),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("Miscellaneous"), description=o6.LocalizedText("Document contains general information.")),
        ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("TenderSpecification"), description=o6.LocalizedText("Document contains tender specification.")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdt;i=6444",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=fdt;i=3008",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[63],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Flow"), description=o6.LocalizedText("Classification is Flow.")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("Level"), description=o6.LocalizedText("Classification is Level.")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Pressure"), description=o6.LocalizedText("Classification is Pressure.")),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("Temperature"), description=o6.LocalizedText("Classification is Temperature.")),
        ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("Valve"), description=o6.LocalizedText("Classification is Valve.")),
        ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("Positioner"), description=o6.LocalizedText("Classification is Positioner.")),
        ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("Actuator"), description=o6.LocalizedText("Classification is Actuator.")),
        ns0.datatypes.EnumValueType(value=7, displayName=o6.LocalizedText("Nc_rc"), description=o6.LocalizedText("Classification is Numeric Control / Robotic Control.")),
        ns0.datatypes.EnumValueType(value=8, displayName=o6.LocalizedText("Encoder"), description=o6.LocalizedText("Classification is Encoder.")),
        ns0.datatypes.EnumValueType(value=9, displayName=o6.LocalizedText("SpeedDrive"), description=o6.LocalizedText("Classification is SpeedDrive.")),
        ns0.datatypes.EnumValueType(value=10, displayName=o6.LocalizedText("Hmi"), description=o6.LocalizedText("Classification is HMI.")),
        ns0.datatypes.EnumValueType(value=11, displayName=o6.LocalizedText("AnalogInput"), description=o6.LocalizedText("Classification is AnalogInput.")),
        ns0.datatypes.EnumValueType(value=12, displayName=o6.LocalizedText("AnalogOutput"), description=o6.LocalizedText("Classification is AnalogOutput.")),
        ns0.datatypes.EnumValueType(value=13, displayName=o6.LocalizedText("DigitalInput"), description=o6.LocalizedText("Classification is DigitalInput.")),
        ns0.datatypes.EnumValueType(value=14, displayName=o6.LocalizedText("DigitalOutput"), description=o6.LocalizedText("Classification is DigitalOutput.")),
        ns0.datatypes.EnumValueType(value=15, displayName=o6.LocalizedText("ElectrochemicalAnalyser"), description=o6.LocalizedText("Classification is ElectrochemicalAnalyser.")),
        ns0.datatypes.EnumValueType(value=16, displayName=o6.LocalizedText("DtmSpecific"), description=o6.LocalizedText("Classification is DtmSpecific.")),
        ns0.datatypes.EnumValueType(value=17, displayName=o6.LocalizedText("Universal"), description=o6.LocalizedText("Classification is Universal.")),
        ns0.datatypes.EnumValueType(value=18, displayName=o6.LocalizedText("Analyser"), description=o6.LocalizedText("Classification is Analyser.")),
        ns0.datatypes.EnumValueType(value=19, displayName=o6.LocalizedText("RemoteIO"), description=o6.LocalizedText("Classification is RemoteIO.")),
        ns0.datatypes.EnumValueType(value=20, displayName=o6.LocalizedText("AnalogCombinedIO"), description=o6.LocalizedText("Classification is AnalogCombinedIO.")),
        ns0.datatypes.EnumValueType(value=21, displayName=o6.LocalizedText("DigitalCombinedIO"), description=o6.LocalizedText("Classification is DigitalCombinedIO.")),
        ns0.datatypes.EnumValueType(value=22, displayName=o6.LocalizedText("Recorder"), description=o6.LocalizedText("Classification is Recorder.")),
        ns0.datatypes.EnumValueType(value=23, displayName=o6.LocalizedText("Controller"), description=o6.LocalizedText("Classification is Controller.")),
        ns0.datatypes.EnumValueType(value=24, displayName=o6.LocalizedText("Angle"), description=o6.LocalizedText("Classification is Angle.")),
        ns0.datatypes.EnumValueType(value=25, displayName=o6.LocalizedText("LimitSwitch"), description=o6.LocalizedText("Classification is LimitSwitch.")),
        ns0.datatypes.EnumValueType(value=26, displayName=o6.LocalizedText("Converter"), description=o6.LocalizedText("Classification is Converter.")),
        ns0.datatypes.EnumValueType(value=27, displayName=o6.LocalizedText("Motor"), description=o6.LocalizedText("Classification is Motor.")),
        ns0.datatypes.EnumValueType(value=28, displayName=o6.LocalizedText("Switchboard"), description=o6.LocalizedText("Classification is Switchboard.")),
        ns0.datatypes.EnumValueType(value=29, displayName=o6.LocalizedText("CircuitBreaker"), description=o6.LocalizedText("Classification is CircuitBreaker.")),
        ns0.datatypes.EnumValueType(value=30, displayName=o6.LocalizedText("PowerMonitoring"), description=o6.LocalizedText("Classification is PowerMonitoring.")),
        ns0.datatypes.EnumValueType(value=31, displayName=o6.LocalizedText("DistributionPanel"), description=o6.LocalizedText("Classification is DistributionPanel.")),
        ns0.datatypes.EnumValueType(value=32, displayName=o6.LocalizedText("Contactor"), description=o6.LocalizedText("Classification is Contactor.")),
        ns0.datatypes.EnumValueType(value=33, displayName=o6.LocalizedText("ProtectionStarter"), description=o6.LocalizedText("Classification is ProtectionStarter.")),
        ns0.datatypes.EnumValueType(value=34, displayName=o6.LocalizedText("SoftStarter"), description=o6.LocalizedText("Classification is SoftStarter.")),
        ns0.datatypes.EnumValueType(value=35, displayName=o6.LocalizedText("Drive"), description=o6.LocalizedText("Classification is Drive.")),
        ns0.datatypes.EnumValueType(value=36, displayName=o6.LocalizedText("AxisControl"), description=o6.LocalizedText("Classification is AxisControl.")),
        ns0.datatypes.EnumValueType(value=37, displayName=o6.LocalizedText("MotorControlCenter"), description=o6.LocalizedText("Classification is MotorControlCenter.")),
        ns0.datatypes.EnumValueType(value=38, displayName=o6.LocalizedText("ControlValve"), description=o6.LocalizedText("Classification is ControlValve.")),
        ns0.datatypes.EnumValueType(value=39, displayName=o6.LocalizedText("Electrical"), description=o6.LocalizedText("Classification is Electrical.")),
        ns0.datatypes.EnumValueType(value=40, displayName=o6.LocalizedText("Density"), description=o6.LocalizedText("Classification is Density.")),
        ns0.datatypes.EnumValueType(value=41, displayName=o6.LocalizedText("Quality"), description=o6.LocalizedText("Classification is Quality.")),
        ns0.datatypes.EnumValueType(value=42, displayName=o6.LocalizedText("SpeedOrRotaryFrequency"), description=o6.LocalizedText("Classification is SpeedOrRotaryFrequency.")),
        ns0.datatypes.EnumValueType(value=43, displayName=o6.LocalizedText("Radiation"), description=o6.LocalizedText("Classification is Radiation.")),
        ns0.datatypes.EnumValueType(value=44, displayName=o6.LocalizedText("WeightMass"), description=o6.LocalizedText("Classification is WeightMass.")),
        ns0.datatypes.EnumValueType(
            value=45, displayName=o6.LocalizedText("DistanceOrPositionPresence"), description=o6.LocalizedText("Classification is DistanceOrPositionPresence.")
        ),
        ns0.datatypes.EnumValueType(value=46, displayName=o6.LocalizedText("PushButton"), description=o6.LocalizedText("Classification is PushButton.")),
        ns0.datatypes.EnumValueType(value=47, displayName=o6.LocalizedText("Joystick"), description=o6.LocalizedText("Classification is Joystick.")),
        ns0.datatypes.EnumValueType(value=48, displayName=o6.LocalizedText("Keypad"), description=o6.LocalizedText("Classification is Keypad.")),
        ns0.datatypes.EnumValueType(value=49, displayName=o6.LocalizedText("PilotLight"), description=o6.LocalizedText("Classification is PilotLight.")),
        ns0.datatypes.EnumValueType(value=50, displayName=o6.LocalizedText("StackLight"), description=o6.LocalizedText("Classification is StackLight.")),
        ns0.datatypes.EnumValueType(value=51, displayName=o6.LocalizedText("Display"), description=o6.LocalizedText("Classification is Display.")),
        ns0.datatypes.EnumValueType(
            value=52, displayName=o6.LocalizedText("CombinedButtonsAndLights"), description=o6.LocalizedText("Classification is CombinedButtonsAndLights.")
        ),
        ns0.datatypes.EnumValueType(value=53, displayName=o6.LocalizedText("OperatorStation"), description=o6.LocalizedText("Classification is OperatorStation.")),
        ns0.datatypes.EnumValueType(value=54, displayName=o6.LocalizedText("GeneralInput"), description=o6.LocalizedText("Classification is GeneralInput.")),
        ns0.datatypes.EnumValueType(value=55, displayName=o6.LocalizedText("GeneralOutput"), description=o6.LocalizedText("Classification is GeneralOutput.")),
        ns0.datatypes.EnumValueType(value=56, displayName=o6.LocalizedText("CombinedInputOutput"), description=o6.LocalizedText("Classification is CombinedInputOutput.")),
        ns0.datatypes.EnumValueType(value=57, displayName=o6.LocalizedText("Relay"), description=o6.LocalizedText("Classification is Relay.")),
        ns0.datatypes.EnumValueType(value=58, displayName=o6.LocalizedText("Timer"), description=o6.LocalizedText("Classification is Timer.")),
        ns0.datatypes.EnumValueType(value=59, displayName=o6.LocalizedText("Scanner"), description=o6.LocalizedText("Classification is Scanner.")),
        ns0.datatypes.EnumValueType(value=60, displayName=o6.LocalizedText("ProgrammableController"), description=o6.LocalizedText("Classification is ProgrammableController.")),
        ns0.datatypes.EnumValueType(value=61, displayName=o6.LocalizedText("CommunicationAdapter"), description=o6.LocalizedText("Classification is CommunicationAdapter.")),
        ns0.datatypes.EnumValueType(value=62, displayName=o6.LocalizedText("Gateway"), description=o6.LocalizedText("Classification is Gateway.")),
    ],
)
deviceTypeId = ns0.vartypes.PropertyType(nodeId="ns=fdt;i=6783", browseName="ns=fdt;DeviceTypeId", dataType=o6.String, accessLevel=3, userAccessLevel=1)
deviceTag = ns0.vartypes.PropertyType(nodeId="ns=fdt;i=6784", browseName="ns=fdt;DeviceTag", dataType=o6.String, accessLevel=3, userAccessLevel=1)
ns0.vartypes.PropertyType(
    nodeId="ns=fdt;i=6787",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=fdt;i=3005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[6],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("PowerDistribution"), description=o6.LocalizedText("Classification domain is PowerDistribution.")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("MotionControl"), description=o6.LocalizedText("Classification domain is MotionControl.")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Measurement"), description=o6.LocalizedText("Classification domain is Measurement.")),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("OperatorInterface"), description=o6.LocalizedText("Classification is OperatorInterface.")),
        ns0.datatypes.EnumValueType(
            value=4, displayName=o6.LocalizedText("ModulesAndControllers"), description=o6.LocalizedText("Classification domain is ModulesAndControllers.")
        ),
        ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("Communication"), description=o6.LocalizedText("Classification domain is Communication.")),
    ],
)


ns0.vartypes.PropertyType(
    nodeId="ns=fdt;i=6029",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdt;i=7001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.NodeId("i=7"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText())],
)
o6.call(nodeId="ns=fdt;i=7001", browseName="Close", inputArgs=o6.hasProperty(o6.ns["ns=fdt;i=6029"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fdt;i=6030",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdt;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.NodeId("i=7"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText())],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdt;i=6039",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdt;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Position", dataType=o6.NodeId("i=9"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText())],
)
o6.call(nodeId="ns=fdt;i=7002", browseName="GetPosition", inputArgs=o6.hasProperty(o6.ns["ns=fdt;i=6030"]), outputArgs=o6.hasProperty(o6.ns["ns=fdt;i=6039"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fdt;i=6040",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdt;i=7003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Mode", dataType=o6.NodeId("i=3"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText())],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdt;i=6041",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdt;i=7003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.NodeId("i=7"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText())],
)
o6.call(nodeId="ns=fdt;i=7003", browseName="Open", inputArgs=o6.hasProperty(o6.ns["ns=fdt;i=6040"]), outputArgs=o6.hasProperty(o6.ns["ns=fdt;i=6041"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fdt;i=6043",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdt;i=7004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="FileHandle", dataType=o6.NodeId("i=7"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="Length", dataType=o6.NodeId("i=6"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdt;i=6044",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdt;i=7004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Data", dataType=o6.NodeId("i=15"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText())],
)
o6.call(nodeId="ns=fdt;i=7004", browseName="Read", inputArgs=o6.hasProperty(o6.ns["ns=fdt;i=6043"]), outputArgs=o6.hasProperty(o6.ns["ns=fdt;i=6044"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fdt;i=6046",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdt;i=7005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="FileHandle", dataType=o6.NodeId("i=7"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="Position", dataType=o6.NodeId("i=9"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
    ],
)
o6.call(nodeId="ns=fdt;i=7005", browseName="SetPosition", inputArgs=o6.hasProperty(o6.ns["ns=fdt;i=6046"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fdt;i=6050",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdt;i=7006",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="FileHandle", dataType=o6.NodeId("i=7"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="Data", dataType=o6.NodeId("i=15"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
    ],
)
o6.call(nodeId="ns=fdt;i=7006", browseName="Write", inputArgs=o6.hasProperty(o6.ns["ns=fdt;i=6050"]))

ns0.objtypes.FileType(
    nodeId="ns=fdt;i=5001",
    browseName="ns=fdt;File",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdt;i=6042", browseName="OpenCount", description="The current number of open file handles.", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdt;i=6047", browseName="Size", description="The size of the file in bytes.", dataType=o6.UInt64)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=fdt;i=6048", browseName="UserWritable", description="Whether the file is writable by the current user.", dataType=o6.Boolean)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdt;i=6049", browseName="Writable", description="Whether the file is writable.", dataType=o6.Boolean)),
        o6.hasComponent(o6.ns["ns=fdt;i=7001"]),
        o6.hasComponent(o6.ns["ns=fdt;i=7002"]),
        o6.hasComponent(o6.ns["ns=fdt;i=7003"]),
        o6.hasComponent(o6.ns["ns=fdt;i=7004"]),
        o6.hasComponent(o6.ns["ns=fdt;i=7005"]),
        o6.hasComponent(o6.ns["ns=fdt;i=7006"]),
    ],
)
o6.reference(fdt_objtypes.FdtDocumentFile, ns0.reftypes.HasComponent, o6.ns["ns=fdt;i=5001"])


del Any, TYPE_CHECKING, uuid, o6, di, ns0, fdt_reftypes, fdt_datypes, fdt_vartypes, fdt_objtypes
