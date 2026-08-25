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

"""Generated OPC UA amb namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.ns0 as ns0
from . import reftypes as amb_reftypes
from . import datatypes as amb_datypes
from . import objtypes as amb_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.objtypes.DataTypeEncodingType(nodeId="ns=amb;i=5001", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=amb;i=5005", browseName="Default XML")
o6.hasEncoding(amb_datypes.RootCauseDataType, o6.ns["ns=amb;i=5005"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=amb;i=5012", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=amb;i=5013", browseName="Default XML")
o6.hasEncoding(amb_datypes.NameNodeIdDataType, o6.ns["ns=amb;i=5013"])
hierarchicalLocations = ns0.objtypes.FolderType(
    nodeId="ns=amb;i=5021",
    browseName="ns=amb;HierarchicalLocations",
    description="Entry point for objects representing the root of a location hierarchy",
    parent="i=31915",
    referenceType=ns0.reftypes.Organizes,
)
operationalLocations = ns0.objtypes.FolderType(
    nodeId="ns=amb;i=5022",
    browseName="ns=amb;OperationalLocations",
    description="Entry point for objects representing the root of a hierarchy of operational locations",
    parent="i=31915",
    referenceType=ns0.reftypes.Organizes,
)
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=amb;i=6013", browseName="ns=amb;RootCauseDataType", dataType=o6.String, value="RootCauseDataType")
o6.reference(o6.ns["ns=amb;i=5001"], "i=39", o6.ns["ns=amb;i=6013"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=amb;i=6014", browseName="ns=amb;RootCauseDataType", dataType=o6.String, value="//xs:element[@name='RootCauseDataType']")
o6.reference(o6.ns["ns=amb;i=5005"], "i=39", o6.ns["ns=amb;i=6014"])
ns0.objtypes.InitialStateType(
    nodeId="ns=amb;i=5006",
    browseName="ns=amb;Planned",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=amb;i=6021", browseName="StateNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(amb_objtypes.MaintenanceEventStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=amb;i=5006"])
ns0.objtypes.StateType(
    nodeId="ns=amb;i=5007",
    browseName="ns=amb;Executing",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=amb;i=6022", browseName="StateNumber", dataType=o6.UInt32, value=2))],
)
o6.reference(amb_objtypes.MaintenanceEventStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=amb;i=5007"])
ns0.objtypes.StateType(
    nodeId="ns=amb;i=5008",
    browseName="ns=amb;Finished",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=amb;i=6023", browseName="StateNumber", dataType=o6.UInt32, value=3))],
)
o6.reference(amb_objtypes.MaintenanceEventStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=amb;i=5008"])
ns0.objtypes.TransitionType(
    nodeId="ns=amb;i=5009",
    browseName="ns=amb;FromPlannedToExecuting",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=amb;i=6024", browseName="TransitionNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(amb_objtypes.MaintenanceEventStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=amb;i=5009"])
o6.reference(o6.ns["ns=amb;i=5009"], "i=51", o6.ns["ns=amb;i=5006"])
o6.reference(o6.ns["ns=amb;i=5009"], "i=52", o6.ns["ns=amb;i=5007"])
ns0.objtypes.TransitionType(
    nodeId="ns=amb;i=5010",
    browseName="ns=amb;FromExecutingToFinished",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=amb;i=6025", browseName="TransitionNumber", dataType=o6.UInt32, value=2))],
)
o6.reference(amb_objtypes.MaintenanceEventStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=amb;i=5010"])
o6.reference(o6.ns["ns=amb;i=5010"], "i=51", o6.ns["ns=amb;i=5007"])
o6.reference(o6.ns["ns=amb;i=5010"], "i=52", o6.ns["ns=amb;i=5008"])
ns0.objtypes.TransitionType(
    nodeId="ns=amb;i=5011",
    browseName="ns=amb;FromFinishedToPlanned",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=amb;i=6026", browseName="TransitionNumber", dataType=o6.UInt32, value=3))],
)
o6.reference(amb_objtypes.MaintenanceEventStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=amb;i=5011"])
o6.reference(o6.ns["ns=amb;i=5011"], "i=51", o6.ns["ns=amb;i=5008"])
o6.reference(o6.ns["ns=amb;i=5011"], "i=52", o6.ns["ns=amb;i=5006"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=amb;i=6027", browseName="ns=amb;NameNodeIdDataType", dataType=o6.String, value="NameNodeIdDataType")
o6.reference(o6.ns["ns=amb;i=5012"], "i=39", o6.ns["ns=amb;i=6027"])
typeDictionary = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=amb;i=6009",
    browseName="ns=amb;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/AMB/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=amb;i=6010", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/AMB/")),
        o6.hasComponent(o6.ns["ns=amb;i=6013"]),
        o6.hasComponent(o6.ns["ns=amb;i=6027"]),
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:tns="http://opcfoundation.org/UA/AMB/" DefaultByteOrder="LittleEndian" xmlns:opc="http://opcfoundation.org/BinarySchema/" xmlns:ua="http://opcfoundation.org/UA/" TargetNamespace="http://opcfoundation.org/UA/AMB/">\n <opc:Import Namespace="http://opcfoundation.org/UA/"/>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="NameNodeIdDataType">\n  <opc:Documentation>A human-readable name of something plus optionally the NodeId in case the something is represented in the AddressSpace</opc:Documentation>\n  <opc:Field TypeName="ua:LocalizedText" Name="Name"/>\n  <opc:Field TypeName="ua:NodeId" Name="NodeId"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="RootCauseDataType">\n  <opc:Documentation>Root cause of an alarm</opc:Documentation>\n  <opc:Field TypeName="ua:NodeId" Name="RootCauseId"/>\n  <opc:Field TypeName="ua:LocalizedText" Name="RootCause"/>\n </opc:StructuredType>\n <opc:EnumeratedType LengthInBits="32" Name="MaintenanceMethodEnum">\n  <opc:EnumeratedValue Name="Local" Value="0"/>\n  <opc:EnumeratedValue Name="Remote" Value="1"/>\n </opc:EnumeratedType>\n</opc:TypeDictionary>\n',
)
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=amb;i=6028", browseName="ns=amb;NameNodeIdDataType", dataType=o6.String, value="//xs:element[@name='NameNodeIdDataType']")
o6.reference(o6.ns["ns=amb;i=5013"], "i=39", o6.ns["ns=amb;i=6028"])
typeDictionary_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=amb;i=6011",
    browseName="ns=amb;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/AMB/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=amb;i=6012", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/AMB/Types.xsd")),
        o6.hasComponent(o6.ns["ns=amb;i=6014"]),
        o6.hasComponent(o6.ns["ns=amb;i=6028"]),
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema elementFormDefault="qualified" targetNamespace="http://opcfoundation.org/UA/AMB/Types.xsd" xmlns:tns="http://opcfoundation.org/UA/AMB/Types.xsd" xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd" xmlns:xs="http://www.w3.org/2001/XMLSchema">\n <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd"/>\n <xs:simpleType name="MaintenanceMethodEnum">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Local_0"/>\n   <xs:enumeration value="Remote_1"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:MaintenanceMethodEnum" name="MaintenanceMethodEnum"/>\n <xs:complexType name="ListOfMaintenanceMethodEnum">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:MaintenanceMethodEnum" name="MaintenanceMethodEnum" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfMaintenanceMethodEnum" name="ListOfMaintenanceMethodEnum" nillable="true"/>\n <xs:complexType name="NameNodeIdDataType">\n  <xs:annotation>\n   <xs:documentation>A human-readable name of something plus optionally the NodeId in case the something is represented in the AddressSpace</xs:documentation>\n  </xs:annotation>\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:LocalizedText" name="Name"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:NodeId" name="NodeId"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:NameNodeIdDataType" name="NameNodeIdDataType"/>\n <xs:complexType name="ListOfNameNodeIdDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:NameNodeIdDataType" name="NameNodeIdDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfNameNodeIdDataType" name="ListOfNameNodeIdDataType" nillable="true"/>\n <xs:complexType name="RootCauseDataType">\n  <xs:annotation>\n   <xs:documentation>Root cause of an alarm</xs:documentation>\n  </xs:annotation>\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:NodeId" name="RootCauseId"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:LocalizedText" name="RootCause"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:RootCauseDataType" name="RootCauseDataType"/>\n <xs:complexType name="ListOfRootCauseDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:RootCauseDataType" name="RootCauseDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfRootCauseDataType" name="ListOfRootCauseDataType" nillable="true"/>\n</xs:schema>\n',
)
ns0.vartypes.PropertyType(
    nodeId="ns=amb;i=6029",
    browseName="EnumValues",
    parent="ns=amb;i=3004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Local"), description=o6.LocalizedText("Maintenance close to the asset")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("Remote"), description=o6.LocalizedText("Maintenance from another location")),
    ],
)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=amb;i=6033",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=amb;i=6034", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
amb_objtypes.MaintenanceEventStateMachineType(
    nodeId="ns=amb;i=5014",
    browseName="ns=amb;MaintenanceState",
    description="Information if the maintenance activity is still planned, currently in execution, or has already been executed.",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=amb;i=6033"])],
)
o6.reference(amb_objtypes.IMaintenanceEventType, ns0.reftypes.HasComponent, o6.ns["ns=amb;i=5014"])
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashAMBSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=amb;i=5018",
    browseName="ns=amb;http://opcfoundation.org/UA/AMB/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=amb;i=6043", browseName="IsNamespaceSubset", dataType=o6.Boolean, value=False)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=amb;i=6044", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2024-02-27T00:00:00Z"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=amb;i=6045", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/AMB/")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=amb;i=6046", browseName="NamespaceVersion", dataType=o6.String, value="1.01.1")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=amb;i=6047", browseName="StaticNodeIdTypes", dataType=ns0.datatypes.IdType, valueRank=1, arrayDimensions=[1], value=[ns0.datatypes.IdType.NUMERIC]
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=amb;i=6048", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=amb;i=6049", browseName="StaticStringNodeIdPattern", dataType=o6.String)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)


ns0.vartypes.PropertyType(
    nodeId="ns=amb;i=6001",
    browseName="InputArguments",
    parent="ns=amb;i=7001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="AliasNameSearchPattern", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="ReferenceTypeFilter", dataType=o6.NodeId, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=amb;i=6002",
    browseName="OutputArguments",
    parent="ns=amb;i=7001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="AliasNodeList", dataType=ns0.datatypes.AliasNameDataType, valueRank=1, arrayDimensions=[0])],
)
o6.call(nodeId="ns=amb;i=7001", browseName="FindAlias", inputArgs=o6.hasProperty(o6.ns["ns=amb;i=6001"]), outputArgs=o6.hasProperty(o6.ns["ns=amb;i=6002"]))

ns0.vartypes.PropertyType(
    nodeId="ns=amb;i=6003",
    browseName="InputArguments",
    parent="ns=amb;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="AliasNameSearchPattern", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="ReferenceTypeFilter", dataType=o6.NodeId, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=amb;i=6004",
    browseName="OutputArguments",
    parent="ns=amb;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="AliasNodeList", dataType=ns0.datatypes.AliasNameDataType, valueRank=1, arrayDimensions=[0])],
)
o6.call(nodeId="ns=amb;i=7002", browseName="FindAlias", inputArgs=o6.hasProperty(o6.ns["ns=amb;i=6003"]), outputArgs=o6.hasProperty(o6.ns["ns=amb;i=6004"]))

assetsByProductInstanceUri = ns0.objtypes.AliasNameCategoryType(
    nodeId="ns=amb;i=5003",
    browseName="ns=amb;AssetsByProductInstanceUri",
    description="Entry point to discover assets by ProductInstanceUri",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=amb;i=6005", browseName="NodeVersion", dataType=o6.String)), o6.hasComponent(o6.ns["ns=amb;i=7002"])],
)


ns0.vartypes.PropertyType(
    nodeId="ns=amb;i=6006",
    browseName="InputArguments",
    parent="ns=amb;i=7003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="AliasNameSearchPattern", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="ReferenceTypeFilter", dataType=o6.NodeId, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=amb;i=6007",
    browseName="OutputArguments",
    parent="ns=amb;i=7003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="AliasNodeList", dataType=ns0.datatypes.AliasNameDataType, valueRank=1, arrayDimensions=[0])],
)
o6.call(nodeId="ns=amb;i=7003", browseName="FindAlias", inputArgs=o6.hasProperty(o6.ns["ns=amb;i=6006"]), outputArgs=o6.hasProperty(o6.ns["ns=amb;i=6007"]))

assetsByAssetId = ns0.objtypes.AliasNameCategoryType(
    nodeId="ns=amb;i=5004",
    browseName="ns=amb;AssetsByAssetId",
    description="Entry point to discover assets by AssetId",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=amb;i=6008", browseName="NodeVersion", dataType=o6.String)), o6.hasComponent(o6.ns["ns=amb;i=7003"])],
)
assets = ns0.objtypes.AliasNameCategoryType(
    nodeId="ns=amb;i=5002",
    browseName="ns=amb;Assets",
    description="Entry point to discover assets",
    references=[o6.organizes(assetsByProductInstanceUri), o6.organizes(assetsByAssetId), o6.hasComponent(o6.ns["ns=amb;i=7001"])],
    parent="i=23470",
    referenceType=ns0.reftypes.Organizes,
)


del Any, TYPE_CHECKING, uuid, o6, ns0, amb_reftypes, amb_datypes, amb_objtypes
