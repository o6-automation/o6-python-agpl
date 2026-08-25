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

"""Generated OPC UA mining namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.machinery as machinery
import o6.ns.ns0 as ns0
from . import datatypes as mining_datypes
from . import vartypes as mining_vartypes
from . import objtypes as mining_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.objtypes.DataTypeEncodingType(nodeId="ns=mining;i=5001", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=mining;i=5002", browseName="Default XML")
o6.hasEncoding(mining_datypes.LongwallShieldOffsetDataType, o6.ns["ns=mining;i=5002"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=mining;i=5003", browseName="Default JSON")
o6.hasEncoding(mining_datypes.LongwallShieldOffsetDataType, o6.ns["ns=mining;i=5003"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=mining;i=6005", browseName="ns=mining;ShieldOffsetDataType", dataType=o6.String, value="ShieldOffsetDataType")
o6.reference(o6.ns["ns=mining;i=5001"], "i=39", o6.ns["ns=mining;i=6005"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=mining;i=6006", browseName="ns=mining;ShieldOffsetDataType", dataType=o6.String, value="//xs:element[@name='ShieldOffsetDataType']")
o6.reference(o6.ns["ns=mining;i=5002"], "i=39", o6.ns["ns=mining;i=6006"])
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashMiningSlashGeneralSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=mining;i=5004",
    browseName="ns=mining;http://opcfoundation.org/UA/Mining/General/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mining;i=6009", browseName="IsNamespaceSubset", dataType=o6.Boolean, value=False)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=mining;i=6010", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2025-10-01T00:00:00Z"))
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mining;i=6011", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/Mining/General/")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mining;i=6012", browseName="NamespaceVersion", dataType=o6.String, value="1.01.0")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining;i=6013", browseName="StaticNodeIdTypes", dataType=ns0.datatypes.IdType, valueRank=1, arrayDimensions=[1], value=[ns0.datatypes.IdType.NUMERIC]
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=mining;i=6014", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mining;i=6015", browseName="StaticStringNodeIdPattern", dataType=o6.String)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
ns0.objtypes.FolderType(
    nodeId="ns=mining;i=5006",
    browseName="ns=di;DeviceTypeImage",
    modellingRule="Optional",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=mining;i=6022", browseName="ns=di;<ImageIdentifier>", modellingRule="MandatoryPlaceholder", dataType=ns0.datatypes.Image)
        )
    ],
)
o6.reference(mining_objtypes.MiningEquipmentIdentificationType, ns0.reftypes.HasComponent, o6.ns["ns=mining;i=5006"])
ns0.objtypes.FolderType(
    nodeId="ns=mining;i=5007",
    browseName="ns=di;Documentation",
    modellingRule="Optional",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=mining;i=6023", browseName="ns=di;<DocumentIdentifier>", modellingRule="MandatoryPlaceholder", dataType=o6.ByteString)
        )
    ],
)
o6.reference(mining_objtypes.MiningEquipmentIdentificationType, ns0.reftypes.HasComponent, o6.ns["ns=mining;i=5007"])
ns0.objtypes.FolderType(
    nodeId="ns=mining;i=5008",
    browseName="ns=di;ImageSet",
    modellingRule="Optional",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=mining;i=6024", browseName="ns=di;<ImageIdentifier>", modellingRule="MandatoryPlaceholder", dataType=ns0.datatypes.Image)
        )
    ],
)
o6.reference(mining_objtypes.MiningEquipmentIdentificationType, ns0.reftypes.HasComponent, o6.ns["ns=mining;i=5008"])
ns0.objtypes.FolderType(
    nodeId="ns=mining;i=5009",
    browseName="ns=di;ProtocolSupport",
    modellingRule="Optional",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=mining;i=6025", browseName="ns=di;<ProtocolSupportIdentifier>", modellingRule="MandatoryPlaceholder", dataType=o6.ByteString
            )
        )
    ],
)
o6.reference(mining_objtypes.MiningEquipmentIdentificationType, ns0.reftypes.HasComponent, o6.ns["ns=mining;i=5009"])
mining_objtypes.MiningEquipmentIdentificationType(
    nodeId="ns=mining;i=5005",
    browseName="ns=mining;MiningEquipmentIdentification",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining;i=6019",
                browseName="ns=di;DeviceClass",
                description="Indicates in which domain or for what purpose the MachineryItem is used.",
                dataType=o6.String,
                value="",
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining;i=6020",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining;i=6021",
                browseName="ns=di;ManufacturerUri",
                description="A globally unique identifier of the manufacturer of the MachineryItem.",
                dataType=o6.String,
                value="",
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining;i=6030",
                browseName="ns=di;Model",
                description="A human-readable, localized name of the model of the MachineryItem.",
                dataType=o6.LocalizedText,
                value=o6.LocalizedText(),
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining;i=6031",
                browseName="ns=di;ProductInstanceUri",
                description="A globally unique resource identifier provided by the manufacturer of the machine",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining;i=6033",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining;i=6034",
                browseName="ns=di;AssetId",
                description="To be used by end users to store a unique identification in the context of their overall application. Servers shall support at least 40 Unicode characters for the clients writing this value, this means clients can expect to be able to write strings with a length of 40 Unicode characters into that field.",
                dataType=o6.String,
                value="",
            )
        ),
    ],
)
o6.reference(mining_objtypes.MiningEquipmentType, ns0.reftypes.HasAddIn, o6.ns["ns=mining;i=5005"])
o6.reference(o6.ns["ns=mining;i=5016"], "i=17604", o6.ns["ns=mining;i=5005"])
typeDictionary = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=mining;i=6001",
    browseName="ns=mining;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/Mining/General/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mining;i=6002", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/Mining/General/")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining;i=6035",
                browseName="Deprecated",
                description="Indicates that all of the DataType definitions represented by the DataTypeDictionaryType are available through a DataTypeDefinition Attribute.",
                dataType=o6.Boolean,
                value=True,
            )
        ),
        o6.hasComponent(o6.ns["ns=mining;i=6005"]),
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary xmlns:ua="http://opcfoundation.org/UA/" TargetNamespace="http://opcfoundation.org/UA/Mining/General/" DefaultByteOrder="LittleEndian" xmlns:opc="http://opcfoundation.org/BinarySchema/" xmlns:tns="http://opcfoundation.org/UA/Mining/General/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">\n <opc:Import Namespace="http://opcfoundation.org/UA/"/>\n <opc:StructuredType Name="LongwallShieldOffsetDataType" BaseType="ua:ExtensionObject">\n  <opc:Documentation>The LongwallShieldOffsetDataType describes a tuple containing a roof support shield number and its corresponding offset</opc:Documentation>\n  <opc:Field TypeName="opc:UInt16" Name="ShieldNumber"/>\n  <opc:Field TypeName="opc:Double" Name="ShieldOffset"/>\n </opc:StructuredType>\n</opc:TypeDictionary>\n',
)
typeDictionary_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=mining;i=6003",
    browseName="ns=mining;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/Mining/General/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=mining;i=6004", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/Mining/General/Types.xsd")
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mining;i=6036",
                browseName="Deprecated",
                description="Indicates that all of the DataType definitions represented by the DataTypeDictionaryType are available through a DataTypeDefinition Attribute.",
                dataType=o6.Boolean,
                value=True,
            )
        ),
        o6.hasComponent(o6.ns["ns=mining;i=6006"]),
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema targetNamespace="http://opcfoundation.org/UA/Mining/General/Types.xsd" elementFormDefault="qualified" xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:tns="http://opcfoundation.org/UA/Mining/General/Types.xsd">\n <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd"/>\n <xs:complexType name="LongwallShieldOffsetDataType">\n  <xs:annotation>\n   <xs:documentation>The LongwallShieldOffsetDataType describes a tuple containing a roof support shield number and its corresponding offset</xs:documentation>\n  </xs:annotation>\n  <xs:sequence>\n   <xs:element minOccurs="0" name="ShieldNumber" type="xs:unsignedShort" maxOccurs="1"/>\n   <xs:element minOccurs="0" name="ShieldOffset" type="xs:double" maxOccurs="1"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element name="LongwallShieldOffsetDataType" type="tns:LongwallShieldOffsetDataType"/>\n <xs:complexType name="ListOfLongwallShieldOffsetDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" nillable="true" name="LongwallShieldOffsetDataType" type="tns:LongwallShieldOffsetDataType" maxOccurs="unbounded"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element nillable="true" name="ListOfLongwallShieldOffsetDataType" type="tns:ListOfLongwallShieldOffsetDataType"/>\n</xs:schema>\n',
)


del Any, TYPE_CHECKING, uuid, o6, di, ia, machinery, ns0, mining_datypes, mining_vartypes, mining_objtypes
