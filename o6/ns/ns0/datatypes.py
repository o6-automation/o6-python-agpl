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

"""Generated OPC UA ns0 namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
from . import reftypes as ns0_reftypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.datatype(nodeId="i=24", browseName="BaseDataType", isAbstract=True)
class BaseDataType:
    pass


Boolean = o6.Boolean


String = o6.String


DateTime = o6.DateTime


Guid = o6.Guid


ByteString = o6.ByteString


XmlElement = o6.XmlElement


NodeId = o6.NodeId


ExpandedNodeId = o6.ExpandedNodeId


StatusCode = o6.StatusCode


QualifiedName = o6.QualifiedName


LocalizedText = o6.LocalizedText


@o6.datatype(nodeId="i=22", browseName="Structure", isAbstract=True, parent="i=24")
class Structure:
    def __init__(self, *args: object, **kwargs: object) -> None: ...


DataValue = o6.DataValue


DiagnosticInfo = o6.DiagnosticInfo


@o6.datatype(nodeId="i=26", browseName="Number", isAbstract=True, parent="i=24")
class Number:
    pass


Float = o6.Float


Double = o6.Double


@o6.datatype(nodeId="i=27", browseName="Integer", isAbstract=True, parent="i=26")
class Integer:
    pass


SByte = o6.SByte


Int16 = o6.Int16


Int32 = o6.Int32


Int64 = o6.Int64


@o6.datatype(nodeId="i=28", browseName="UInteger", isAbstract=True, parent="i=26")
class UInteger:
    pass


Byte = o6.Byte


UInt16 = o6.UInt16


UInt32 = o6.UInt32


UInt64 = o6.UInt64


@o6.datatype(nodeId="i=29", browseName="Enumeration", isAbstract=True)
class Enumeration(BaseDataType):
    pass


@o6.datatype(nodeId="i=30", browseName="Image", isAbstract=True, parent="i=15")
class Image:
    pass


@o6.datatype(nodeId="i=50", browseName="Decimal", parent="i=26")
class Decimal:
    pass


@o6.optionsettype(nodeId="i=94", browseName="PermissionType", base=o6.UInt32)
class PermissionType:
    BROWSE = o6.bitmask(0x01 << 0, name="Browse")
    READ_ROLE_PERMISSIONS = o6.bitmask(0x01 << 1, name="ReadRolePermissions")
    WRITE_ATTRIBUTE = o6.bitmask(0x01 << 2, name="WriteAttribute")
    WRITE_ROLE_PERMISSIONS = o6.bitmask(0x01 << 3, name="WriteRolePermissions")
    WRITE_HISTORIZING = o6.bitmask(0x01 << 4, name="WriteHistorizing")
    READ = o6.bitmask(0x01 << 5, name="Read")
    WRITE = o6.bitmask(0x01 << 6, name="Write")
    READ_HISTORY = o6.bitmask(0x01 << 7, name="ReadHistory")
    INSERT_HISTORY = o6.bitmask(0x01 << 8, name="InsertHistory")
    MODIFY_HISTORY = o6.bitmask(0x01 << 9, name="ModifyHistory")
    DELETE_HISTORY = o6.bitmask(0x01 << 10, name="DeleteHistory")
    RECEIVE_EVENTS = o6.bitmask(0x01 << 11, name="ReceiveEvents")
    CALL = o6.bitmask(0x01 << 12, name="Call")
    ADD_REFERENCE = o6.bitmask(0x01 << 13, name="AddReference")
    REMOVE_REFERENCE = o6.bitmask(0x01 << 14, name="RemoveReference")
    DELETE_NODE = o6.bitmask(0x01 << 15, name="DeleteNode")
    ADD_NODE = o6.bitmask(0x01 << 16, name="AddNode")


@o6.optionsettype(nodeId="i=95", browseName="AccessRestrictionType", base=o6.UInt16)
class AccessRestrictionType:
    SIGNING_REQUIRED = o6.bitmask(0x01 << 0, name="SigningRequired")
    ENCRYPTION_REQUIRED = o6.bitmask(0x01 << 1, name="EncryptionRequired")
    SESSION_REQUIRED = o6.bitmask(0x01 << 2, name="SessionRequired")
    APPLY_RESTRICTIONS_TO_BROWSE = o6.bitmask(0x01 << 3, name="ApplyRestrictionsToBrowse")


@o6.datatype(nodeId="i=96", browseName="RolePermissionType", defaultEncodingId="i=128")
class RolePermissionType(Structure):
    roleId: o6.NodeId = o6.field(name="RoleId")
    permissions: PermissionType = o6.field(name="Permissions")


@o6.datatype(nodeId="i=97", browseName="DataTypeDefinition", defaultEncodingId="i=121", isAbstract=True)
class DataTypeDefinition(Structure):
    pass


@o6.enumtype(nodeId="i=98", browseName="StructureType")
class StructureType(Enumeration):
    STRUCTURE = o6.enumfield(0, name="Structure")
    STRUCTURE_WITH_OPTIONAL_FIELDS = o6.enumfield(1, name="StructureWithOptionalFields")
    UNION = o6.enumfield(2, name="Union")
    STRUCTURE_WITH_SUBTYPED_VALUES = o6.enumfield(3, name="StructureWithSubtypedValues")
    UNION_WITH_SUBTYPED_VALUES = o6.enumfield(4, name="UnionWithSubtypedValues")


@o6.datatype(nodeId="i=101", browseName="StructureField", defaultEncodingId="i=14844")
class StructureField(Structure):
    name: o6.String = o6.field(name="Name")
    description: o6.LocalizedText = o6.field(name="Description")
    dataType: o6.NodeId = o6.field(name="DataType")
    valueRank: o6.Int32 = o6.field(name="ValueRank")
    arrayDimensions: list[o6.UInt32] = o6.field(name="ArrayDimensions")
    maxStringLength: o6.UInt32 = o6.field(name="MaxStringLength")
    isOptional: o6.Boolean = o6.field(name="IsOptional")


@o6.datatype(nodeId="i=99", browseName="StructureDefinition", defaultEncodingId="i=122")
class StructureDefinition(DataTypeDefinition):
    defaultEncodingId: o6.NodeId = o6.field(name="DefaultEncodingId")
    baseDataType: o6.NodeId = o6.field(name="BaseDataType")
    structureType: StructureType = o6.field(name="StructureType")
    fields: list[StructureField] = o6.field(name="Fields")


@o6.enumtype(nodeId="i=120", browseName="NamingRuleType")
class NamingRuleType(Enumeration):
    MANDATORY = o6.enumfield(1, name="Mandatory")
    OPTIONAL = o6.enumfield(2, name="Optional")
    CONSTRAINT = o6.enumfield(3, name="Constraint")


@o6.enumtype(nodeId="i=256", browseName="IdType")
class IdType(Enumeration):
    NUMERIC = o6.enumfield(0, name="Numeric")
    STRING = o6.enumfield(1, name="String")
    GUID = o6.enumfield(2, name="Guid")
    OPAQUE = o6.enumfield(3, name="Opaque")


@o6.enumtype(nodeId="i=257", browseName="NodeClass")
class NodeClass(Enumeration):
    UNSPECIFIED = o6.enumfield(0, name="Unspecified")
    OBJECT = o6.enumfield(1, name="Object")
    VARIABLE = o6.enumfield(2, name="Variable")
    METHOD = o6.enumfield(4, name="Method")
    OBJECT_TYPE = o6.enumfield(8, name="ObjectType")
    VARIABLE_TYPE = o6.enumfield(16, name="VariableType")
    REFERENCE_TYPE = o6.enumfield(32, name="ReferenceType")
    DATA_TYPE = o6.enumfield(64, name="DataType")
    VIEW = o6.enumfield(128, name="View")


@o6.datatype(nodeId="i=285", browseName="ReferenceNode", defaultEncodingId="i=287")
class ReferenceNode(Structure):
    referenceTypeId: o6.NodeId = o6.field(name="ReferenceTypeId")
    isInverse: o6.Boolean = o6.field(name="IsInverse")
    targetId: o6.ExpandedNodeId = o6.field(name="TargetId")


@o6.datatype(nodeId="i=258", browseName="Node", defaultEncodingId="i=260")
class Node(Structure):
    nodeId: o6.NodeId = o6.field(name="NodeId")
    nodeClass: NodeClass = o6.field(name="NodeClass")
    browseName: o6.QualifiedName = o6.field(name="BrowseName")
    displayName: o6.LocalizedText = o6.field(name="DisplayName")
    description: o6.LocalizedText = o6.field(name="Description")
    writeMask: o6.UInt32 = o6.field(name="WriteMask")
    userWriteMask: o6.UInt32 = o6.field(name="UserWriteMask")
    rolePermissions: list[RolePermissionType] = o6.field(name="RolePermissions")
    userRolePermissions: list[RolePermissionType] = o6.field(name="UserRolePermissions")
    accessRestrictions: o6.UInt16 = o6.field(name="AccessRestrictions")
    references: list[ReferenceNode] = o6.field(name="References")


@o6.datatype(nodeId="i=288", browseName="IntegerId", parent="i=7")
class IntegerId:
    pass


@o6.datatype(nodeId="i=289", browseName="Counter", parent="i=7")
class Counter:
    pass


@o6.datatype(nodeId="i=290", browseName="Duration", parent="i=11")
class Duration:
    pass


@o6.datatype(nodeId="i=291", browseName="NumericRange", parent="i=12")
class NumericRange:
    pass


@o6.datatype(nodeId="i=294", browseName="UtcTime", parent="i=13")
class UtcTime:
    pass


@o6.datatype(nodeId="i=295", browseName="LocaleId", parent="i=12")
class LocaleId:
    pass


@o6.datatype(nodeId="i=296", browseName="Argument", defaultEncodingId="i=298")
class Argument(Structure):
    name: o6.String = o6.field(name="Name")
    dataType: o6.NodeId = o6.field(name="DataType")
    valueRank: o6.Int32 = o6.field(name="ValueRank")
    arrayDimensions: list[o6.UInt32] = o6.field(name="ArrayDimensions")
    description: o6.LocalizedText = o6.field(name="Description")


@o6.datatype(nodeId="i=299", browseName="StatusResult", defaultEncodingId="i=301")
class StatusResult(Structure):
    statusCode: o6.StatusCode = o6.field(name="StatusCode")
    diagnosticInfo: o6.DiagnosticInfo = o6.field(name="DiagnosticInfo")


@o6.enumtype(nodeId="i=302", browseName="MessageSecurityMode")
class MessageSecurityMode(Enumeration):
    INVALID = o6.enumfield(0, name="Invalid")
    NONE = o6.enumfield(1, name="None")
    SIGN = o6.enumfield(2, name="Sign")
    SIGN_AND_ENCRYPT = o6.enumfield(3, name="SignAndEncrypt")


@o6.enumtype(nodeId="i=303", browseName="UserTokenType")
class UserTokenType(Enumeration):
    ANONYMOUS = o6.enumfield(0, name="Anonymous")
    USER_NAME = o6.enumfield(1, name="UserName")
    CERTIFICATE = o6.enumfield(2, name="Certificate")
    ISSUED_TOKEN = o6.enumfield(3, name="IssuedToken")


@o6.datatype(nodeId="i=304", browseName="UserTokenPolicy", defaultEncodingId="i=306")
class UserTokenPolicy(Structure):
    policyId: o6.String = o6.field(name="PolicyId")
    tokenType: UserTokenType = o6.field(name="TokenType")
    issuedTokenType: o6.String = o6.field(name="IssuedTokenType")
    issuerEndpointUrl: o6.String = o6.field(name="IssuerEndpointUrl")
    securityPolicyUri: o6.String = o6.field(name="SecurityPolicyUri")


@o6.enumtype(nodeId="i=307", browseName="ApplicationType")
class ApplicationType(Enumeration):
    SERVER = o6.enumfield(0, name="Server")
    CLIENT = o6.enumfield(1, name="Client")
    CLIENT_AND_SERVER = o6.enumfield(2, name="ClientAndServer")
    DISCOVERY_SERVER = o6.enumfield(3, name="DiscoveryServer")


@o6.datatype(nodeId="i=308", browseName="ApplicationDescription", defaultEncodingId="i=310")
class ApplicationDescription(Structure):
    applicationUri: o6.String = o6.field(name="ApplicationUri")
    productUri: o6.String = o6.field(name="ProductUri")
    applicationName: o6.LocalizedText = o6.field(name="ApplicationName")
    applicationType: ApplicationType = o6.field(name="ApplicationType")
    gatewayServerUri: o6.String = o6.field(name="GatewayServerUri")
    discoveryProfileUri: o6.String = o6.field(name="DiscoveryProfileUri")
    discoveryUrls: list[o6.String] = o6.field(name="DiscoveryUrls")


@o6.datatype(nodeId="i=311", browseName="ApplicationInstanceCertificate", parent="i=15")
class ApplicationInstanceCertificate:
    pass


@o6.datatype(nodeId="i=312", browseName="EndpointDescription", defaultEncodingId="i=314")
class EndpointDescription(Structure):
    endpointUrl: o6.String = o6.field(name="EndpointUrl")
    server: ApplicationDescription = o6.field(name="Server")
    serverCertificate: o6.ByteString = o6.field(name="ServerCertificate")
    securityMode: MessageSecurityMode = o6.field(name="SecurityMode")
    securityPolicyUri: o6.String = o6.field(name="SecurityPolicyUri")
    userIdentityTokens: list[UserTokenPolicy] = o6.field(name="UserIdentityTokens")
    transportProfileUri: o6.String = o6.field(name="TransportProfileUri")
    securityLevel: o6.Byte = o6.field(name="SecurityLevel")


@o6.enumtype(nodeId="i=315", browseName="SecurityTokenRequestType")
class SecurityTokenRequestType(Enumeration):
    ISSUE = o6.enumfield(0, name="Issue")
    RENEW = o6.enumfield(1, name="Renew")


@o6.datatype(nodeId="i=316", browseName="UserIdentityToken", defaultEncodingId="i=318", isAbstract=True)
class UserIdentityToken(Structure):
    policyId: o6.String = o6.field(name="PolicyId")


@o6.datatype(nodeId="i=319", browseName="AnonymousIdentityToken", defaultEncodingId="i=321")
class AnonymousIdentityToken(UserIdentityToken):
    policyId: o6.String = o6.field(name="PolicyId")


@o6.datatype(nodeId="i=322", browseName="UserNameIdentityToken", defaultEncodingId="i=324")
class UserNameIdentityToken(UserIdentityToken):
    policyId: o6.String = o6.field(name="PolicyId")
    userName: o6.String = o6.field(name="UserName")
    password: o6.ByteString = o6.field(name="Password")
    encryptionAlgorithm: o6.String = o6.field(name="EncryptionAlgorithm")


@o6.datatype(nodeId="i=325", browseName="X509IdentityToken", defaultEncodingId="i=327")
class X509IdentityToken(UserIdentityToken):
    policyId: o6.String = o6.field(name="PolicyId")
    certificateData: o6.ByteString = o6.field(name="CertificateData")


@o6.datatype(nodeId="i=331", browseName="EndpointConfiguration", defaultEncodingId="i=333")
class EndpointConfiguration(Structure):
    operationTimeout: o6.Int32 = o6.field(name="OperationTimeout")
    useBinaryEncoding: o6.Boolean = o6.field(name="UseBinaryEncoding")
    maxStringLength: o6.Int32 = o6.field(name="MaxStringLength")
    maxByteStringLength: o6.Int32 = o6.field(name="MaxByteStringLength")
    maxArrayLength: o6.Int32 = o6.field(name="MaxArrayLength")
    maxMessageSize: o6.Int32 = o6.field(name="MaxMessageSize")
    maxBufferSize: o6.Int32 = o6.field(name="MaxBufferSize")
    channelLifetime: o6.Int32 = o6.field(name="ChannelLifetime")
    securityTokenLifetime: o6.Int32 = o6.field(name="SecurityTokenLifetime")


@o6.datatype(nodeId="i=338", browseName="BuildInfo", defaultEncodingId="i=340")
class BuildInfo(Structure):
    productUri: o6.String = o6.field(name="ProductUri")
    manufacturerName: o6.String = o6.field(name="ManufacturerName")
    productName: o6.String = o6.field(name="ProductName")
    softwareVersion: o6.String = o6.field(name="SoftwareVersion")
    buildNumber: o6.String = o6.field(name="BuildNumber")
    buildDate: o6.DateTime = o6.field(name="BuildDate")


@o6.datatype(nodeId="i=344", browseName="SignedSoftwareCertificate", defaultEncodingId="i=346")
class SignedSoftwareCertificate(Structure):
    certificateData: o6.ByteString = o6.field(name="CertificateData")
    signature: o6.ByteString = o6.field(name="Signature")


@o6.optionsettype(nodeId="i=347", browseName="AttributeWriteMask", base=o6.UInt32)
class AttributeWriteMask:
    ACCESS_LEVEL = o6.bitmask(0x01 << 0, name="AccessLevel")
    ARRAY_DIMENSIONS = o6.bitmask(0x01 << 1, name="ArrayDimensions")
    BROWSE_NAME = o6.bitmask(0x01 << 2, name="BrowseName")
    CONTAINS_NO_LOOPS = o6.bitmask(0x01 << 3, name="ContainsNoLoops")
    DATA_TYPE = o6.bitmask(0x01 << 4, name="DataType")
    DESCRIPTION = o6.bitmask(0x01 << 5, name="Description")
    DISPLAY_NAME = o6.bitmask(0x01 << 6, name="DisplayName")
    EVENT_NOTIFIER = o6.bitmask(0x01 << 7, name="EventNotifier")
    EXECUTABLE = o6.bitmask(0x01 << 8, name="Executable")
    HISTORIZING = o6.bitmask(0x01 << 9, name="Historizing")
    INVERSE_NAME = o6.bitmask(0x01 << 10, name="InverseName")
    IS_ABSTRACT = o6.bitmask(0x01 << 11, name="IsAbstract")
    MINIMUM_SAMPLING_INTERVAL = o6.bitmask(0x01 << 12, name="MinimumSamplingInterval")
    NODE_CLASS = o6.bitmask(0x01 << 13, name="NodeClass")
    NODE_ID = o6.bitmask(0x01 << 14, name="NodeId")
    SYMMETRIC = o6.bitmask(0x01 << 15, name="Symmetric")
    USER_ACCESS_LEVEL = o6.bitmask(0x01 << 16, name="UserAccessLevel")
    USER_EXECUTABLE = o6.bitmask(0x01 << 17, name="UserExecutable")
    USER_WRITE_MASK = o6.bitmask(0x01 << 18, name="UserWriteMask")
    VALUE_RANK = o6.bitmask(0x01 << 19, name="ValueRank")
    WRITE_MASK = o6.bitmask(0x01 << 20, name="WriteMask")
    VALUE_FOR_VARIABLE_TYPE = o6.bitmask(0x01 << 21, name="ValueForVariableType")
    DATA_TYPE_DEFINITION = o6.bitmask(0x01 << 22, name="DataTypeDefinition")
    ROLE_PERMISSIONS = o6.bitmask(0x01 << 23, name="RolePermissions")
    ACCESS_RESTRICTIONS = o6.bitmask(0x01 << 24, name="AccessRestrictions")
    ACCESS_LEVEL_EX = o6.bitmask(0x01 << 25, name="AccessLevelEx")


@o6.enumtype(nodeId="i=348", browseName="NodeAttributesMask")
class NodeAttributesMask(Enumeration):
    NONE = o6.enumfield(0, name="None")
    ACCESS_LEVEL = o6.enumfield(1, name="AccessLevel")
    ARRAY_DIMENSIONS = o6.enumfield(2, name="ArrayDimensions")
    BROWSE_NAME = o6.enumfield(4, name="BrowseName")
    CONTAINS_NO_LOOPS = o6.enumfield(8, name="ContainsNoLoops")
    DATA_TYPE = o6.enumfield(16, name="DataType")
    DESCRIPTION = o6.enumfield(32, name="Description")
    DISPLAY_NAME = o6.enumfield(64, name="DisplayName")
    EVENT_NOTIFIER = o6.enumfield(128, name="EventNotifier")
    EXECUTABLE = o6.enumfield(256, name="Executable")
    HISTORIZING = o6.enumfield(512, name="Historizing")
    INVERSE_NAME = o6.enumfield(1024, name="InverseName")
    IS_ABSTRACT = o6.enumfield(2048, name="IsAbstract")
    MINIMUM_SAMPLING_INTERVAL = o6.enumfield(4096, name="MinimumSamplingInterval")
    NODE_CLASS = o6.enumfield(8192, name="NodeClass")
    NODE_ID = o6.enumfield(16384, name="NodeId")
    SYMMETRIC = o6.enumfield(32768, name="Symmetric")
    USER_ACCESS_LEVEL = o6.enumfield(65536, name="UserAccessLevel")
    USER_EXECUTABLE = o6.enumfield(131072, name="UserExecutable")
    USER_WRITE_MASK = o6.enumfield(262144, name="UserWriteMask")
    VALUE_RANK = o6.enumfield(524288, name="ValueRank")
    WRITE_MASK = o6.enumfield(1048576, name="WriteMask")
    VALUE = o6.enumfield(2097152, name="Value")
    DATA_TYPE_DEFINITION = o6.enumfield(4194304, name="DataTypeDefinition")
    ROLE_PERMISSIONS = o6.enumfield(8388608, name="RolePermissions")
    ACCESS_RESTRICTIONS = o6.enumfield(16777216, name="AccessRestrictions")
    BASE_NODE = o6.enumfield(26501220, name="BaseNode")
    OBJECT = o6.enumfield(26501348, name="Object")
    VIEW = o6.enumfield(26501356, name="View")
    OBJECT_TYPE = o6.enumfield(26503268, name="ObjectType")
    REFERENCE_TYPE = o6.enumfield(26537060, name="ReferenceType")
    VARIABLE = o6.enumfield(26571383, name="Variable")
    METHOD = o6.enumfield(26632548, name="Method")
    VARIABLE_TYPE = o6.enumfield(28600438, name="VariableType")
    ALL = o6.enumfield(33554431, name="All")


@o6.datatype(nodeId="i=349", browseName="NodeAttributes", defaultEncodingId="i=351")
class NodeAttributes(Structure):
    specifiedAttributes: o6.UInt32 = o6.field(name="SpecifiedAttributes")
    displayName: o6.LocalizedText = o6.field(name="DisplayName")
    description: o6.LocalizedText = o6.field(name="Description")
    writeMask: o6.UInt32 = o6.field(name="WriteMask")
    userWriteMask: o6.UInt32 = o6.field(name="UserWriteMask")


@o6.datatype(nodeId="i=352", browseName="ObjectAttributes", defaultEncodingId="i=354")
class ObjectAttributes(NodeAttributes):
    specifiedAttributes: o6.UInt32 = o6.field(name="SpecifiedAttributes")
    displayName: o6.LocalizedText = o6.field(name="DisplayName")
    description: o6.LocalizedText = o6.field(name="Description")
    writeMask: o6.UInt32 = o6.field(name="WriteMask")
    userWriteMask: o6.UInt32 = o6.field(name="UserWriteMask")
    eventNotifier: o6.Byte = o6.field(name="EventNotifier")


@o6.datatype(nodeId="i=355", browseName="VariableAttributes", defaultEncodingId="i=357")
class VariableAttributes(NodeAttributes):
    specifiedAttributes: o6.UInt32 = o6.field(name="SpecifiedAttributes")
    displayName: o6.LocalizedText = o6.field(name="DisplayName")
    description: o6.LocalizedText = o6.field(name="Description")
    writeMask: o6.UInt32 = o6.field(name="WriteMask")
    userWriteMask: o6.UInt32 = o6.field(name="UserWriteMask")
    value: Any = o6.field(name="Value")
    dataType: o6.NodeId = o6.field(name="DataType")
    valueRank: o6.Int32 = o6.field(name="ValueRank")
    arrayDimensions: list[o6.UInt32] = o6.field(name="ArrayDimensions")
    accessLevel: o6.Byte = o6.field(name="AccessLevel")
    userAccessLevel: o6.Byte = o6.field(name="UserAccessLevel")
    minimumSamplingInterval: o6.Double = o6.field(name="MinimumSamplingInterval")
    historizing: o6.Boolean = o6.field(name="Historizing")


@o6.datatype(nodeId="i=358", browseName="MethodAttributes", defaultEncodingId="i=360")
class MethodAttributes(NodeAttributes):
    specifiedAttributes: o6.UInt32 = o6.field(name="SpecifiedAttributes")
    displayName: o6.LocalizedText = o6.field(name="DisplayName")
    description: o6.LocalizedText = o6.field(name="Description")
    writeMask: o6.UInt32 = o6.field(name="WriteMask")
    userWriteMask: o6.UInt32 = o6.field(name="UserWriteMask")
    executable: o6.Boolean = o6.field(name="Executable")
    userExecutable: o6.Boolean = o6.field(name="UserExecutable")


@o6.datatype(nodeId="i=361", browseName="ObjectTypeAttributes", defaultEncodingId="i=363")
class ObjectTypeAttributes(NodeAttributes):
    specifiedAttributes: o6.UInt32 = o6.field(name="SpecifiedAttributes")
    displayName: o6.LocalizedText = o6.field(name="DisplayName")
    description: o6.LocalizedText = o6.field(name="Description")
    writeMask: o6.UInt32 = o6.field(name="WriteMask")
    userWriteMask: o6.UInt32 = o6.field(name="UserWriteMask")
    isAbstract: o6.Boolean = o6.field(name="IsAbstract")


@o6.datatype(nodeId="i=364", browseName="VariableTypeAttributes", defaultEncodingId="i=366")
class VariableTypeAttributes(NodeAttributes):
    specifiedAttributes: o6.UInt32 = o6.field(name="SpecifiedAttributes")
    displayName: o6.LocalizedText = o6.field(name="DisplayName")
    description: o6.LocalizedText = o6.field(name="Description")
    writeMask: o6.UInt32 = o6.field(name="WriteMask")
    userWriteMask: o6.UInt32 = o6.field(name="UserWriteMask")
    value: Any = o6.field(name="Value")
    dataType: o6.NodeId = o6.field(name="DataType")
    valueRank: o6.Int32 = o6.field(name="ValueRank")
    arrayDimensions: list[o6.UInt32] = o6.field(name="ArrayDimensions")
    isAbstract: o6.Boolean = o6.field(name="IsAbstract")


@o6.datatype(nodeId="i=367", browseName="ReferenceTypeAttributes", defaultEncodingId="i=369")
class ReferenceTypeAttributes(NodeAttributes):
    specifiedAttributes: o6.UInt32 = o6.field(name="SpecifiedAttributes")
    displayName: o6.LocalizedText = o6.field(name="DisplayName")
    description: o6.LocalizedText = o6.field(name="Description")
    writeMask: o6.UInt32 = o6.field(name="WriteMask")
    userWriteMask: o6.UInt32 = o6.field(name="UserWriteMask")
    isAbstract: o6.Boolean = o6.field(name="IsAbstract")
    symmetric: o6.Boolean = o6.field(name="Symmetric")
    inverseName: o6.LocalizedText = o6.field(name="InverseName")


@o6.datatype(nodeId="i=370", browseName="DataTypeAttributes", defaultEncodingId="i=372")
class DataTypeAttributes(NodeAttributes):
    specifiedAttributes: o6.UInt32 = o6.field(name="SpecifiedAttributes")
    displayName: o6.LocalizedText = o6.field(name="DisplayName")
    description: o6.LocalizedText = o6.field(name="Description")
    writeMask: o6.UInt32 = o6.field(name="WriteMask")
    userWriteMask: o6.UInt32 = o6.field(name="UserWriteMask")
    isAbstract: o6.Boolean = o6.field(name="IsAbstract")


@o6.datatype(nodeId="i=373", browseName="ViewAttributes", defaultEncodingId="i=375")
class ViewAttributes(NodeAttributes):
    specifiedAttributes: o6.UInt32 = o6.field(name="SpecifiedAttributes")
    displayName: o6.LocalizedText = o6.field(name="DisplayName")
    description: o6.LocalizedText = o6.field(name="Description")
    writeMask: o6.UInt32 = o6.field(name="WriteMask")
    userWriteMask: o6.UInt32 = o6.field(name="UserWriteMask")
    containsNoLoops: o6.Boolean = o6.field(name="ContainsNoLoops")
    eventNotifier: o6.Byte = o6.field(name="EventNotifier")


@o6.datatype(nodeId="i=376", browseName="AddNodesItem", defaultEncodingId="i=378")
class AddNodesItem(Structure):
    parentNodeId: o6.ExpandedNodeId = o6.field(name="ParentNodeId")
    referenceTypeId: o6.NodeId = o6.field(name="ReferenceTypeId")
    requestedNewNodeId: o6.ExpandedNodeId = o6.field(name="RequestedNewNodeId")
    browseName: o6.QualifiedName = o6.field(name="BrowseName")
    nodeClass: NodeClass = o6.field(name="NodeClass")
    nodeAttributes: o6.ExtensionObject = o6.field(name="NodeAttributes")
    typeDefinition: o6.ExpandedNodeId = o6.field(name="TypeDefinition")


@o6.datatype(nodeId="i=379", browseName="AddReferencesItem", defaultEncodingId="i=381")
class AddReferencesItem(Structure):
    sourceNodeId: o6.NodeId = o6.field(name="SourceNodeId")
    referenceTypeId: o6.NodeId = o6.field(name="ReferenceTypeId")
    isForward: o6.Boolean = o6.field(name="IsForward")
    targetServerUri: o6.String = o6.field(name="TargetServerUri")
    targetNodeId: o6.ExpandedNodeId = o6.field(name="TargetNodeId")
    targetNodeClass: NodeClass = o6.field(name="TargetNodeClass")


@o6.datatype(nodeId="i=382", browseName="DeleteNodesItem", defaultEncodingId="i=384")
class DeleteNodesItem(Structure):
    nodeId: o6.NodeId = o6.field(name="NodeId")
    deleteTargetReferences: o6.Boolean = o6.field(name="DeleteTargetReferences")


@o6.datatype(nodeId="i=385", browseName="DeleteReferencesItem", defaultEncodingId="i=387")
class DeleteReferencesItem(Structure):
    sourceNodeId: o6.NodeId = o6.field(name="SourceNodeId")
    referenceTypeId: o6.NodeId = o6.field(name="ReferenceTypeId")
    isForward: o6.Boolean = o6.field(name="IsForward")
    targetNodeId: o6.ExpandedNodeId = o6.field(name="TargetNodeId")
    deleteBidirectional: o6.Boolean = o6.field(name="DeleteBidirectional")


@o6.datatype(nodeId="i=388", browseName="SessionAuthenticationToken", parent="i=17")
class SessionAuthenticationToken:
    pass


@o6.datatype(nodeId="i=389", browseName="RequestHeader", defaultEncodingId="i=391")
class RequestHeader(Structure):
    authenticationToken: o6.NodeId = o6.field(name="AuthenticationToken")
    timestamp: o6.DateTime = o6.field(name="Timestamp")
    requestHandle: o6.UInt32 = o6.field(name="RequestHandle")
    returnDiagnostics: o6.UInt32 = o6.field(name="ReturnDiagnostics")
    auditEntryId: o6.String = o6.field(name="AuditEntryId")
    timeoutHint: o6.UInt32 = o6.field(name="TimeoutHint")
    additionalHeader: o6.ExtensionObject = o6.field(name="AdditionalHeader")


@o6.datatype(nodeId="i=392", browseName="ResponseHeader", defaultEncodingId="i=394")
class ResponseHeader(Structure):
    timestamp: o6.DateTime = o6.field(name="Timestamp")
    requestHandle: o6.UInt32 = o6.field(name="RequestHandle")
    serviceResult: o6.StatusCode = o6.field(name="ServiceResult")
    serviceDiagnostics: o6.DiagnosticInfo = o6.field(name="ServiceDiagnostics")
    stringTable: list[o6.String] = o6.field(name="StringTable")
    additionalHeader: o6.ExtensionObject = o6.field(name="AdditionalHeader")


@o6.datatype(nodeId="i=395", browseName="ServiceFault", defaultEncodingId="i=397")
class ServiceFault(Structure):
    responseHeader: ResponseHeader = o6.field(name="ResponseHeader")


@o6.datatype(nodeId="i=420", browseName="FindServersRequest", defaultEncodingId="i=422")
class FindServersRequest(Structure):
    requestHeader: RequestHeader = o6.field(name="RequestHeader")
    endpointUrl: o6.String = o6.field(name="EndpointUrl")
    localeIds: list[o6.String] = o6.field(name="LocaleIds")
    serverUris: list[o6.String] = o6.field(name="ServerUris")


@o6.datatype(nodeId="i=423", browseName="FindServersResponse", defaultEncodingId="i=425")
class FindServersResponse(Structure):
    responseHeader: ResponseHeader = o6.field(name="ResponseHeader")
    servers: list[ApplicationDescription] = o6.field(name="Servers")


@o6.datatype(nodeId="i=426", browseName="GetEndpointsRequest", defaultEncodingId="i=428")
class GetEndpointsRequest(Structure):
    requestHeader: RequestHeader = o6.field(name="RequestHeader")
    endpointUrl: o6.String = o6.field(name="EndpointUrl")
    localeIds: list[o6.String] = o6.field(name="LocaleIds")
    profileUris: list[o6.String] = o6.field(name="ProfileUris")


@o6.datatype(nodeId="i=429", browseName="GetEndpointsResponse", defaultEncodingId="i=431")
class GetEndpointsResponse(Structure):
    responseHeader: ResponseHeader = o6.field(name="ResponseHeader")
    endpoints: list[EndpointDescription] = o6.field(name="Endpoints")


@o6.datatype(nodeId="i=432", browseName="RegisteredServer", defaultEncodingId="i=434")
class RegisteredServer(Structure):
    serverUri: o6.String = o6.field(name="ServerUri")
    productUri: o6.String = o6.field(name="ProductUri")
    serverNames: list[o6.LocalizedText] = o6.field(name="ServerNames")
    serverType: ApplicationType = o6.field(name="ServerType")
    gatewayServerUri: o6.String = o6.field(name="GatewayServerUri")
    discoveryUrls: list[o6.String] = o6.field(name="DiscoveryUrls")
    semaphoreFilePath: o6.String = o6.field(name="SemaphoreFilePath")
    isOnline: o6.Boolean = o6.field(name="IsOnline")


@o6.datatype(nodeId="i=435", browseName="RegisterServerRequest", defaultEncodingId="i=437")
class RegisterServerRequest(Structure):
    requestHeader: RequestHeader = o6.field(name="RequestHeader")
    server: RegisteredServer = o6.field(name="Server")


@o6.datatype(nodeId="i=438", browseName="RegisterServerResponse", defaultEncodingId="i=440")
class RegisterServerResponse(Structure):
    responseHeader: ResponseHeader = o6.field(name="ResponseHeader")


@o6.datatype(nodeId="i=441", browseName="ChannelSecurityToken", defaultEncodingId="i=443")
class ChannelSecurityToken(Structure):
    channelId: o6.UInt32 = o6.field(name="ChannelId")
    tokenId: o6.UInt32 = o6.field(name="TokenId")
    createdAt: o6.DateTime = o6.field(name="CreatedAt")
    revisedLifetime: o6.UInt32 = o6.field(name="RevisedLifetime")


@o6.datatype(nodeId="i=444", browseName="OpenSecureChannelRequest", defaultEncodingId="i=446")
class OpenSecureChannelRequest(Structure):
    requestHeader: RequestHeader = o6.field(name="RequestHeader")
    clientProtocolVersion: o6.UInt32 = o6.field(name="ClientProtocolVersion")
    requestType: SecurityTokenRequestType = o6.field(name="RequestType")
    securityMode: MessageSecurityMode = o6.field(name="SecurityMode")
    clientNonce: o6.ByteString = o6.field(name="ClientNonce")
    requestedLifetime: o6.UInt32 = o6.field(name="RequestedLifetime")


@o6.datatype(nodeId="i=447", browseName="OpenSecureChannelResponse", defaultEncodingId="i=449")
class OpenSecureChannelResponse(Structure):
    responseHeader: ResponseHeader = o6.field(name="ResponseHeader")
    serverProtocolVersion: o6.UInt32 = o6.field(name="ServerProtocolVersion")
    securityToken: ChannelSecurityToken = o6.field(name="SecurityToken")
    serverNonce: o6.ByteString = o6.field(name="ServerNonce")


@o6.datatype(nodeId="i=450", browseName="CloseSecureChannelRequest", defaultEncodingId="i=452")
class CloseSecureChannelRequest(Structure):
    requestHeader: RequestHeader = o6.field(name="RequestHeader")


@o6.datatype(nodeId="i=453", browseName="CloseSecureChannelResponse", defaultEncodingId="i=455")
class CloseSecureChannelResponse(Structure):
    responseHeader: ResponseHeader = o6.field(name="ResponseHeader")


@o6.datatype(nodeId="i=456", browseName="SignatureData", defaultEncodingId="i=458")
class SignatureData(Structure):
    algorithm: o6.String = o6.field(name="Algorithm")
    signature: o6.ByteString = o6.field(name="Signature")


@o6.datatype(nodeId="i=459", browseName="CreateSessionRequest", defaultEncodingId="i=461")
class CreateSessionRequest(Structure):
    requestHeader: RequestHeader = o6.field(name="RequestHeader")
    clientDescription: ApplicationDescription = o6.field(name="ClientDescription")
    serverUri: o6.String = o6.field(name="ServerUri")
    endpointUrl: o6.String = o6.field(name="EndpointUrl")
    sessionName: o6.String = o6.field(name="SessionName")
    clientNonce: o6.ByteString = o6.field(name="ClientNonce")
    clientCertificate: o6.ByteString = o6.field(name="ClientCertificate")
    requestedSessionTimeout: o6.Double = o6.field(name="RequestedSessionTimeout")
    maxResponseMessageSize: o6.UInt32 = o6.field(name="MaxResponseMessageSize")


@o6.datatype(nodeId="i=462", browseName="CreateSessionResponse", defaultEncodingId="i=464")
class CreateSessionResponse(Structure):
    responseHeader: ResponseHeader = o6.field(name="ResponseHeader")
    sessionId: o6.NodeId = o6.field(name="SessionId")
    authenticationToken: o6.NodeId = o6.field(name="AuthenticationToken")
    revisedSessionTimeout: o6.Double = o6.field(name="RevisedSessionTimeout")
    serverNonce: o6.ByteString = o6.field(name="ServerNonce")
    serverCertificate: o6.ByteString = o6.field(name="ServerCertificate")
    serverEndpoints: list[EndpointDescription] = o6.field(name="ServerEndpoints")
    serverSoftwareCertificates: list[SignedSoftwareCertificate] = o6.field(name="ServerSoftwareCertificates")
    serverSignature: SignatureData = o6.field(name="ServerSignature")
    maxRequestMessageSize: o6.UInt32 = o6.field(name="MaxRequestMessageSize")


@o6.datatype(nodeId="i=465", browseName="ActivateSessionRequest", defaultEncodingId="i=467")
class ActivateSessionRequest(Structure):
    requestHeader: RequestHeader = o6.field(name="RequestHeader")
    clientSignature: SignatureData = o6.field(name="ClientSignature")
    clientSoftwareCertificates: list[SignedSoftwareCertificate] = o6.field(name="ClientSoftwareCertificates")
    localeIds: list[o6.String] = o6.field(name="LocaleIds")
    userIdentityToken: o6.ExtensionObject = o6.field(name="UserIdentityToken")
    userTokenSignature: SignatureData = o6.field(name="UserTokenSignature")


@o6.datatype(nodeId="i=468", browseName="ActivateSessionResponse", defaultEncodingId="i=470")
class ActivateSessionResponse(Structure):
    responseHeader: ResponseHeader = o6.field(name="ResponseHeader")
    serverNonce: o6.ByteString = o6.field(name="ServerNonce")
    results: list[o6.StatusCode] = o6.field(name="Results")
    diagnosticInfos: list[o6.DiagnosticInfo] = o6.field(name="DiagnosticInfos")


@o6.datatype(nodeId="i=471", browseName="CloseSessionRequest", defaultEncodingId="i=473")
class CloseSessionRequest(Structure):
    requestHeader: RequestHeader = o6.field(name="RequestHeader")
    deleteSubscriptions: o6.Boolean = o6.field(name="DeleteSubscriptions")


@o6.datatype(nodeId="i=474", browseName="CloseSessionResponse", defaultEncodingId="i=476")
class CloseSessionResponse(Structure):
    responseHeader: ResponseHeader = o6.field(name="ResponseHeader")


@o6.datatype(nodeId="i=477", browseName="CancelRequest", defaultEncodingId="i=479")
class CancelRequest(Structure):
    requestHeader: RequestHeader = o6.field(name="RequestHeader")
    requestHandle: o6.UInt32 = o6.field(name="RequestHandle")


@o6.datatype(nodeId="i=480", browseName="CancelResponse", defaultEncodingId="i=482")
class CancelResponse(Structure):
    responseHeader: ResponseHeader = o6.field(name="ResponseHeader")
    cancelCount: o6.UInt32 = o6.field(name="CancelCount")


@o6.datatype(nodeId="i=483", browseName="AddNodesResult", defaultEncodingId="i=485")
class AddNodesResult(Structure):
    statusCode: o6.StatusCode = o6.field(name="StatusCode")
    addedNodeId: o6.NodeId = o6.field(name="AddedNodeId")


@o6.datatype(nodeId="i=486", browseName="AddNodesRequest", defaultEncodingId="i=488")
class AddNodesRequest(Structure):
    requestHeader: RequestHeader = o6.field(name="RequestHeader")
    nodesToAdd: list[AddNodesItem] = o6.field(name="NodesToAdd")


@o6.datatype(nodeId="i=489", browseName="AddNodesResponse", defaultEncodingId="i=491")
class AddNodesResponse(Structure):
    responseHeader: ResponseHeader = o6.field(name="ResponseHeader")
    results: list[AddNodesResult] = o6.field(name="Results")
    diagnosticInfos: list[o6.DiagnosticInfo] = o6.field(name="DiagnosticInfos")


@o6.datatype(nodeId="i=492", browseName="AddReferencesRequest", defaultEncodingId="i=494")
class AddReferencesRequest(Structure):
    requestHeader: RequestHeader = o6.field(name="RequestHeader")
    referencesToAdd: list[AddReferencesItem] = o6.field(name="ReferencesToAdd")


@o6.datatype(nodeId="i=495", browseName="AddReferencesResponse", defaultEncodingId="i=497")
class AddReferencesResponse(Structure):
    responseHeader: ResponseHeader = o6.field(name="ResponseHeader")
    results: list[o6.StatusCode] = o6.field(name="Results")
    diagnosticInfos: list[o6.DiagnosticInfo] = o6.field(name="DiagnosticInfos")


@o6.datatype(nodeId="i=498", browseName="DeleteNodesRequest", defaultEncodingId="i=500")
class DeleteNodesRequest(Structure):
    requestHeader: RequestHeader = o6.field(name="RequestHeader")
    nodesToDelete: list[DeleteNodesItem] = o6.field(name="NodesToDelete")


@o6.datatype(nodeId="i=501", browseName="DeleteNodesResponse", defaultEncodingId="i=503")
class DeleteNodesResponse(Structure):
    responseHeader: ResponseHeader = o6.field(name="ResponseHeader")
    results: list[o6.StatusCode] = o6.field(name="Results")
    diagnosticInfos: list[o6.DiagnosticInfo] = o6.field(name="DiagnosticInfos")


@o6.datatype(nodeId="i=504", browseName="DeleteReferencesRequest", defaultEncodingId="i=506")
class DeleteReferencesRequest(Structure):
    requestHeader: RequestHeader = o6.field(name="RequestHeader")
    referencesToDelete: list[DeleteReferencesItem] = o6.field(name="ReferencesToDelete")


@o6.datatype(nodeId="i=507", browseName="DeleteReferencesResponse", defaultEncodingId="i=509")
class DeleteReferencesResponse(Structure):
    responseHeader: ResponseHeader = o6.field(name="ResponseHeader")
    results: list[o6.StatusCode] = o6.field(name="Results")
    diagnosticInfos: list[o6.DiagnosticInfo] = o6.field(name="DiagnosticInfos")


@o6.enumtype(nodeId="i=510", browseName="BrowseDirection")
class BrowseDirection(Enumeration):
    FORWARD = o6.enumfield(0, name="Forward")
    INVERSE = o6.enumfield(1, name="Inverse")
    BOTH = o6.enumfield(2, name="Both")
    INVALID = o6.enumfield(3, name="Invalid")


@o6.datatype(nodeId="i=511", browseName="ViewDescription", defaultEncodingId="i=513")
class ViewDescription(Structure):
    viewId: o6.NodeId = o6.field(name="ViewId")
    timestamp: o6.DateTime = o6.field(name="Timestamp")
    viewVersion: o6.UInt32 = o6.field(name="ViewVersion")


@o6.datatype(nodeId="i=514", browseName="BrowseDescription", defaultEncodingId="i=516")
class BrowseDescription(Structure):
    nodeId: o6.NodeId = o6.field(name="NodeId")
    browseDirection: BrowseDirection = o6.field(name="BrowseDirection")
    referenceTypeId: o6.NodeId = o6.field(name="ReferenceTypeId")
    includeSubtypes: o6.Boolean = o6.field(name="IncludeSubtypes")
    nodeClassMask: o6.UInt32 = o6.field(name="NodeClassMask")
    resultMask: o6.UInt32 = o6.field(name="ResultMask")


@o6.enumtype(nodeId="i=517", browseName="BrowseResultMask")
class BrowseResultMask(Enumeration):
    NONE = o6.enumfield(0, name="None")
    REFERENCE_TYPE_ID = o6.enumfield(1, name="ReferenceTypeId")
    IS_FORWARD = o6.enumfield(2, name="IsForward")
    REFERENCE_TYPE_INFO = o6.enumfield(3, name="ReferenceTypeInfo")
    NODE_CLASS = o6.enumfield(4, name="NodeClass")
    BROWSE_NAME = o6.enumfield(8, name="BrowseName")
    DISPLAY_NAME = o6.enumfield(16, name="DisplayName")
    TYPE_DEFINITION = o6.enumfield(32, name="TypeDefinition")
    TARGET_INFO = o6.enumfield(60, name="TargetInfo")
    ALL = o6.enumfield(63, name="All")


@o6.datatype(nodeId="i=518", browseName="ReferenceDescription", defaultEncodingId="i=520")
class ReferenceDescription(Structure):
    referenceTypeId: o6.NodeId = o6.field(name="ReferenceTypeId")
    isForward: o6.Boolean = o6.field(name="IsForward")
    nodeId: o6.ExpandedNodeId = o6.field(name="NodeId")
    browseName: o6.QualifiedName = o6.field(name="BrowseName")
    displayName: o6.LocalizedText = o6.field(name="DisplayName")
    nodeClass: NodeClass = o6.field(name="NodeClass")
    typeDefinition: o6.ExpandedNodeId = o6.field(name="TypeDefinition")


@o6.datatype(nodeId="i=521", browseName="ContinuationPoint", parent="i=15")
class ContinuationPoint:
    pass


@o6.datatype(nodeId="i=522", browseName="BrowseResult", defaultEncodingId="i=524")
class BrowseResult(Structure):
    statusCode: o6.StatusCode = o6.field(name="StatusCode")
    continuationPoint: o6.ByteString = o6.field(name="ContinuationPoint")
    references: list[ReferenceDescription] = o6.field(name="References")


@o6.datatype(nodeId="i=525", browseName="BrowseRequest", defaultEncodingId="i=527")
class BrowseRequest(Structure):
    requestHeader: RequestHeader = o6.field(name="RequestHeader")
    view: ViewDescription = o6.field(name="View")
    requestedMaxReferencesPerNode: o6.UInt32 = o6.field(name="RequestedMaxReferencesPerNode")
    nodesToBrowse: list[BrowseDescription] = o6.field(name="NodesToBrowse")


@o6.datatype(nodeId="i=528", browseName="BrowseResponse", defaultEncodingId="i=530")
class BrowseResponse(Structure):
    responseHeader: ResponseHeader = o6.field(name="ResponseHeader")
    results: list[BrowseResult] = o6.field(name="Results")
    diagnosticInfos: list[o6.DiagnosticInfo] = o6.field(name="DiagnosticInfos")


@o6.datatype(nodeId="i=531", browseName="BrowseNextRequest", defaultEncodingId="i=533")
class BrowseNextRequest(Structure):
    requestHeader: RequestHeader = o6.field(name="RequestHeader")
    releaseContinuationPoints: o6.Boolean = o6.field(name="ReleaseContinuationPoints")
    continuationPoints: list[o6.ByteString] = o6.field(name="ContinuationPoints")


@o6.datatype(nodeId="i=534", browseName="BrowseNextResponse", defaultEncodingId="i=536")
class BrowseNextResponse(Structure):
    responseHeader: ResponseHeader = o6.field(name="ResponseHeader")
    results: list[BrowseResult] = o6.field(name="Results")
    diagnosticInfos: list[o6.DiagnosticInfo] = o6.field(name="DiagnosticInfos")


@o6.datatype(nodeId="i=537", browseName="RelativePathElement", defaultEncodingId="i=539")
class RelativePathElement(Structure):
    referenceTypeId: o6.NodeId = o6.field(name="ReferenceTypeId")
    isInverse: o6.Boolean = o6.field(name="IsInverse")
    includeSubtypes: o6.Boolean = o6.field(name="IncludeSubtypes")
    targetName: o6.QualifiedName = o6.field(name="TargetName")


@o6.datatype(nodeId="i=540", browseName="RelativePath", defaultEncodingId="i=542")
class RelativePath(Structure):
    elements: list[RelativePathElement] = o6.field(name="Elements")


@o6.datatype(nodeId="i=543", browseName="BrowsePath", defaultEncodingId="i=545")
class BrowsePath(Structure):
    startingNode: o6.NodeId = o6.field(name="StartingNode")
    relativePath: RelativePath = o6.field(name="RelativePath")


@o6.datatype(nodeId="i=546", browseName="BrowsePathTarget", defaultEncodingId="i=548")
class BrowsePathTarget(Structure):
    targetId: o6.ExpandedNodeId = o6.field(name="TargetId")
    remainingPathIndex: o6.UInt32 = o6.field(name="RemainingPathIndex")


@o6.datatype(nodeId="i=549", browseName="BrowsePathResult", defaultEncodingId="i=551")
class BrowsePathResult(Structure):
    statusCode: o6.StatusCode = o6.field(name="StatusCode")
    targets: list[BrowsePathTarget] = o6.field(name="Targets")


@o6.datatype(nodeId="i=552", browseName="TranslateBrowsePathsToNodeIdsRequest", defaultEncodingId="i=554")
class TranslateBrowsePathsToNodeIdsRequest(Structure):
    requestHeader: RequestHeader = o6.field(name="RequestHeader")
    browsePaths: list[BrowsePath] = o6.field(name="BrowsePaths")


@o6.datatype(nodeId="i=555", browseName="TranslateBrowsePathsToNodeIdsResponse", defaultEncodingId="i=557")
class TranslateBrowsePathsToNodeIdsResponse(Structure):
    responseHeader: ResponseHeader = o6.field(name="ResponseHeader")
    results: list[BrowsePathResult] = o6.field(name="Results")
    diagnosticInfos: list[o6.DiagnosticInfo] = o6.field(name="DiagnosticInfos")


@o6.datatype(nodeId="i=558", browseName="RegisterNodesRequest", defaultEncodingId="i=560")
class RegisterNodesRequest(Structure):
    requestHeader: RequestHeader = o6.field(name="RequestHeader")
    nodesToRegister: list[o6.NodeId] = o6.field(name="NodesToRegister")


@o6.datatype(nodeId="i=561", browseName="RegisterNodesResponse", defaultEncodingId="i=563")
class RegisterNodesResponse(Structure):
    responseHeader: ResponseHeader = o6.field(name="ResponseHeader")
    registeredNodeIds: list[o6.NodeId] = o6.field(name="RegisteredNodeIds")


@o6.datatype(nodeId="i=564", browseName="UnregisterNodesRequest", defaultEncodingId="i=566")
class UnregisterNodesRequest(Structure):
    requestHeader: RequestHeader = o6.field(name="RequestHeader")
    nodesToUnregister: list[o6.NodeId] = o6.field(name="NodesToUnregister")


@o6.datatype(nodeId="i=567", browseName="UnregisterNodesResponse", defaultEncodingId="i=569")
class UnregisterNodesResponse(Structure):
    responseHeader: ResponseHeader = o6.field(name="ResponseHeader")


@o6.datatype(nodeId="i=570", browseName="QueryDataDescription", defaultEncodingId="i=572")
class QueryDataDescription(Structure):
    relativePath: RelativePath = o6.field(name="RelativePath")
    attributeId: o6.UInt32 = o6.field(name="AttributeId")
    indexRange: o6.String = o6.field(name="IndexRange")


@o6.datatype(nodeId="i=573", browseName="NodeTypeDescription", defaultEncodingId="i=575")
class NodeTypeDescription(Structure):
    typeDefinitionNode: o6.ExpandedNodeId = o6.field(name="TypeDefinitionNode")
    includeSubTypes: o6.Boolean = o6.field(name="IncludeSubTypes")
    dataToReturn: list[QueryDataDescription] = o6.field(name="DataToReturn")


@o6.enumtype(nodeId="i=576", browseName="FilterOperator")
class FilterOperator(Enumeration):
    EQUALS = o6.enumfield(0, name="Equals")
    IS_NULL = o6.enumfield(1, name="IsNull")
    GREATER_THAN = o6.enumfield(2, name="GreaterThan")
    LESS_THAN = o6.enumfield(3, name="LessThan")
    GREATER_THAN_OR_EQUAL = o6.enumfield(4, name="GreaterThanOrEqual")
    LESS_THAN_OR_EQUAL = o6.enumfield(5, name="LessThanOrEqual")
    LIKE = o6.enumfield(6, name="Like")
    NOT = o6.enumfield(7, name="Not")
    BETWEEN = o6.enumfield(8, name="Between")
    IN_LIST = o6.enumfield(9, name="InList")
    AND = o6.enumfield(10, name="And")
    OR = o6.enumfield(11, name="Or")
    CAST = o6.enumfield(12, name="Cast")
    IN_VIEW = o6.enumfield(13, name="InView")
    OF_TYPE = o6.enumfield(14, name="OfType")
    RELATED_TO = o6.enumfield(15, name="RelatedTo")
    BITWISE_AND = o6.enumfield(16, name="BitwiseAnd")
    BITWISE_OR = o6.enumfield(17, name="BitwiseOr")


@o6.datatype(nodeId="i=577", browseName="QueryDataSet", defaultEncodingId="i=579")
class QueryDataSet(Structure):
    nodeId: o6.ExpandedNodeId = o6.field(name="NodeId")
    typeDefinitionNode: o6.ExpandedNodeId = o6.field(name="TypeDefinitionNode")
    values: list[Any] = o6.field(name="Values")


@o6.datatype(nodeId="i=580", browseName="NodeReference", defaultEncodingId="i=582")
class NodeReference(Structure):
    nodeId: o6.NodeId = o6.field(name="NodeId")
    referenceTypeId: o6.NodeId = o6.field(name="ReferenceTypeId")
    isForward: o6.Boolean = o6.field(name="IsForward")
    referencedNodeIds: list[o6.NodeId] = o6.field(name="ReferencedNodeIds")


@o6.datatype(nodeId="i=583", browseName="ContentFilterElement", defaultEncodingId="i=585")
class ContentFilterElement(Structure):
    filterOperator: FilterOperator = o6.field(name="FilterOperator")
    filterOperands: list[o6.ExtensionObject] = o6.field(name="FilterOperands")


@o6.datatype(nodeId="i=586", browseName="ContentFilter", defaultEncodingId="i=588")
class ContentFilter(Structure):
    elements: list[ContentFilterElement] = o6.field(name="Elements")


@o6.datatype(nodeId="i=589", browseName="FilterOperand", defaultEncodingId="i=591", isAbstract=True)
class FilterOperand(Structure):
    pass


@o6.datatype(nodeId="i=592", browseName="ElementOperand", defaultEncodingId="i=594")
class ElementOperand(FilterOperand):
    index: o6.UInt32 = o6.field(name="Index")


@o6.datatype(nodeId="i=595", browseName="LiteralOperand", defaultEncodingId="i=597")
class LiteralOperand(FilterOperand):
    value: Any = o6.field(name="Value")


@o6.datatype(nodeId="i=598", browseName="AttributeOperand", defaultEncodingId="i=600")
class AttributeOperand(FilterOperand):
    nodeId: o6.NodeId = o6.field(name="NodeId")
    alias: o6.String = o6.field(name="Alias")
    browsePath: RelativePath = o6.field(name="BrowsePath")
    attributeId: o6.UInt32 = o6.field(name="AttributeId")
    indexRange: o6.String = o6.field(name="IndexRange")


@o6.datatype(nodeId="i=601", browseName="SimpleAttributeOperand", defaultEncodingId="i=603")
class SimpleAttributeOperand(FilterOperand):
    typeDefinitionId: o6.NodeId = o6.field(name="TypeDefinitionId")
    browsePath: list[o6.QualifiedName] = o6.field(name="BrowsePath")
    attributeId: o6.UInt32 = o6.field(name="AttributeId")
    indexRange: o6.String = o6.field(name="IndexRange")


@o6.datatype(nodeId="i=604", browseName="ContentFilterElementResult", defaultEncodingId="i=606")
class ContentFilterElementResult(Structure):
    statusCode: o6.StatusCode = o6.field(name="StatusCode")
    operandStatusCodes: list[o6.StatusCode] = o6.field(name="OperandStatusCodes")
    operandDiagnosticInfos: list[o6.DiagnosticInfo] = o6.field(name="OperandDiagnosticInfos")


@o6.datatype(nodeId="i=607", browseName="ContentFilterResult", defaultEncodingId="i=609")
class ContentFilterResult(Structure):
    elementResults: list[ContentFilterElementResult] = o6.field(name="ElementResults")
    elementDiagnosticInfos: list[o6.DiagnosticInfo] = o6.field(name="ElementDiagnosticInfos")


@o6.datatype(nodeId="i=610", browseName="ParsingResult", defaultEncodingId="i=612")
class ParsingResult(Structure):
    statusCode: o6.StatusCode = o6.field(name="StatusCode")
    dataStatusCodes: list[o6.StatusCode] = o6.field(name="DataStatusCodes")
    dataDiagnosticInfos: list[o6.DiagnosticInfo] = o6.field(name="DataDiagnosticInfos")


@o6.datatype(nodeId="i=613", browseName="QueryFirstRequest", defaultEncodingId="i=615")
class QueryFirstRequest(Structure):
    requestHeader: RequestHeader = o6.field(name="RequestHeader")
    view: ViewDescription = o6.field(name="View")
    nodeTypes: list[NodeTypeDescription] = o6.field(name="NodeTypes")
    filter: ContentFilter = o6.field(name="Filter")
    maxDataSetsToReturn: o6.UInt32 = o6.field(name="MaxDataSetsToReturn")
    maxReferencesToReturn: o6.UInt32 = o6.field(name="MaxReferencesToReturn")


@o6.datatype(nodeId="i=616", browseName="QueryFirstResponse", defaultEncodingId="i=618")
class QueryFirstResponse(Structure):
    responseHeader: ResponseHeader = o6.field(name="ResponseHeader")
    queryDataSets: list[QueryDataSet] = o6.field(name="QueryDataSets")
    continuationPoint: o6.ByteString = o6.field(name="ContinuationPoint")
    parsingResults: list[ParsingResult] = o6.field(name="ParsingResults")
    diagnosticInfos: list[o6.DiagnosticInfo] = o6.field(name="DiagnosticInfos")
    filterResult: ContentFilterResult = o6.field(name="FilterResult")


@o6.datatype(nodeId="i=619", browseName="QueryNextRequest", defaultEncodingId="i=621")
class QueryNextRequest(Structure):
    requestHeader: RequestHeader = o6.field(name="RequestHeader")
    releaseContinuationPoint: o6.Boolean = o6.field(name="ReleaseContinuationPoint")
    continuationPoint: o6.ByteString = o6.field(name="ContinuationPoint")


@o6.datatype(nodeId="i=622", browseName="QueryNextResponse", defaultEncodingId="i=624")
class QueryNextResponse(Structure):
    responseHeader: ResponseHeader = o6.field(name="ResponseHeader")
    queryDataSets: list[QueryDataSet] = o6.field(name="QueryDataSets")
    revisedContinuationPoint: o6.ByteString = o6.field(name="RevisedContinuationPoint")


@o6.enumtype(nodeId="i=625", browseName="TimestampsToReturn")
class TimestampsToReturn(Enumeration):
    SOURCE = o6.enumfield(0, name="Source")
    SERVER = o6.enumfield(1, name="Server")
    BOTH = o6.enumfield(2, name="Both")
    NEITHER = o6.enumfield(3, name="Neither")
    INVALID = o6.enumfield(4, name="Invalid")


@o6.datatype(nodeId="i=626", browseName="ReadValueId", defaultEncodingId="i=628")
class ReadValueId(Structure):
    nodeId: o6.NodeId = o6.field(name="NodeId")
    attributeId: o6.UInt32 = o6.field(name="AttributeId")
    indexRange: o6.String = o6.field(name="IndexRange")
    dataEncoding: o6.QualifiedName = o6.field(name="DataEncoding")


@o6.datatype(nodeId="i=629", browseName="ReadRequest", defaultEncodingId="i=631")
class ReadRequest(Structure):
    requestHeader: RequestHeader = o6.field(name="RequestHeader")
    maxAge: o6.Double = o6.field(name="MaxAge")
    timestampsToReturn: TimestampsToReturn = o6.field(name="TimestampsToReturn")
    nodesToRead: list[ReadValueId] = o6.field(name="NodesToRead")


@o6.datatype(nodeId="i=632", browseName="ReadResponse", defaultEncodingId="i=634")
class ReadResponse(Structure):
    responseHeader: ResponseHeader = o6.field(name="ResponseHeader")
    results: list[o6.DataValue] = o6.field(name="Results")
    diagnosticInfos: list[o6.DiagnosticInfo] = o6.field(name="DiagnosticInfos")


@o6.datatype(nodeId="i=635", browseName="HistoryReadValueId", defaultEncodingId="i=637")
class HistoryReadValueId(Structure):
    nodeId: o6.NodeId = o6.field(name="NodeId")
    indexRange: o6.String = o6.field(name="IndexRange")
    dataEncoding: o6.QualifiedName = o6.field(name="DataEncoding")
    continuationPoint: o6.ByteString = o6.field(name="ContinuationPoint")


@o6.datatype(nodeId="i=638", browseName="HistoryReadResult", defaultEncodingId="i=640")
class HistoryReadResult(Structure):
    statusCode: o6.StatusCode = o6.field(name="StatusCode")
    continuationPoint: o6.ByteString = o6.field(name="ContinuationPoint")
    historyData: o6.ExtensionObject = o6.field(name="HistoryData")


@o6.datatype(nodeId="i=641", browseName="HistoryReadDetails", defaultEncodingId="i=643", isAbstract=True)
class HistoryReadDetails(Structure):
    pass


@o6.datatype(nodeId="i=647", browseName="ReadRawModifiedDetails", defaultEncodingId="i=649")
class ReadRawModifiedDetails(HistoryReadDetails):
    isReadModified: o6.Boolean = o6.field(name="IsReadModified")
    startTime: o6.DateTime = o6.field(name="StartTime")
    endTime: o6.DateTime = o6.field(name="EndTime")
    numValuesPerNode: o6.UInt32 = o6.field(name="NumValuesPerNode")
    returnBounds: o6.Boolean = o6.field(name="ReturnBounds")


@o6.datatype(nodeId="i=653", browseName="ReadAtTimeDetails", defaultEncodingId="i=655")
class ReadAtTimeDetails(HistoryReadDetails):
    reqTimes: list[o6.DateTime] = o6.field(name="ReqTimes")
    useSimpleBounds: o6.Boolean = o6.field(name="UseSimpleBounds")


@o6.datatype(nodeId="i=656", browseName="HistoryData", defaultEncodingId="i=658")
class HistoryData(Structure):
    dataValues: list[o6.DataValue] = o6.field(name="DataValues")


@o6.datatype(nodeId="i=662", browseName="HistoryReadRequest", defaultEncodingId="i=664")
class HistoryReadRequest(Structure):
    requestHeader: RequestHeader = o6.field(name="RequestHeader")
    historyReadDetails: o6.ExtensionObject = o6.field(name="HistoryReadDetails")
    timestampsToReturn: TimestampsToReturn = o6.field(name="TimestampsToReturn")
    releaseContinuationPoints: o6.Boolean = o6.field(name="ReleaseContinuationPoints")
    nodesToRead: list[HistoryReadValueId] = o6.field(name="NodesToRead")


@o6.datatype(nodeId="i=665", browseName="HistoryReadResponse", defaultEncodingId="i=667")
class HistoryReadResponse(Structure):
    responseHeader: ResponseHeader = o6.field(name="ResponseHeader")
    results: list[HistoryReadResult] = o6.field(name="Results")
    diagnosticInfos: list[o6.DiagnosticInfo] = o6.field(name="DiagnosticInfos")


@o6.datatype(nodeId="i=668", browseName="WriteValue", defaultEncodingId="i=670")
class WriteValue(Structure):
    nodeId: o6.NodeId = o6.field(name="NodeId")
    attributeId: o6.UInt32 = o6.field(name="AttributeId")
    indexRange: o6.String = o6.field(name="IndexRange")
    value: o6.DataValue = o6.field(name="Value")


@o6.datatype(nodeId="i=671", browseName="WriteRequest", defaultEncodingId="i=673")
class WriteRequest(Structure):
    requestHeader: RequestHeader = o6.field(name="RequestHeader")
    nodesToWrite: list[WriteValue] = o6.field(name="NodesToWrite")


@o6.datatype(nodeId="i=674", browseName="WriteResponse", defaultEncodingId="i=676")
class WriteResponse(Structure):
    responseHeader: ResponseHeader = o6.field(name="ResponseHeader")
    results: list[o6.StatusCode] = o6.field(name="Results")
    diagnosticInfos: list[o6.DiagnosticInfo] = o6.field(name="DiagnosticInfos")


@o6.datatype(nodeId="i=677", browseName="HistoryUpdateDetails", defaultEncodingId="i=679", isAbstract=True)
class HistoryUpdateDetails(Structure):
    pass


@o6.datatype(nodeId="i=686", browseName="DeleteRawModifiedDetails", defaultEncodingId="i=688")
class DeleteRawModifiedDetails(HistoryUpdateDetails):
    nodeId: o6.NodeId = o6.field(name="NodeId")
    isDeleteModified: o6.Boolean = o6.field(name="IsDeleteModified")
    startTime: o6.DateTime = o6.field(name="StartTime")
    endTime: o6.DateTime = o6.field(name="EndTime")


@o6.datatype(nodeId="i=689", browseName="DeleteAtTimeDetails", defaultEncodingId="i=691")
class DeleteAtTimeDetails(HistoryUpdateDetails):
    nodeId: o6.NodeId = o6.field(name="NodeId")
    reqTimes: list[o6.DateTime] = o6.field(name="ReqTimes")


@o6.datatype(nodeId="i=692", browseName="DeleteEventDetails", defaultEncodingId="i=694")
class DeleteEventDetails(HistoryUpdateDetails):
    nodeId: o6.NodeId = o6.field(name="NodeId")
    eventIds: list[o6.ByteString] = o6.field(name="EventIds")


@o6.datatype(nodeId="i=695", browseName="HistoryUpdateResult", defaultEncodingId="i=697")
class HistoryUpdateResult(Structure):
    statusCode: o6.StatusCode = o6.field(name="StatusCode")
    operationResults: list[o6.StatusCode] = o6.field(name="OperationResults")
    diagnosticInfos: list[o6.DiagnosticInfo] = o6.field(name="DiagnosticInfos")


@o6.datatype(nodeId="i=698", browseName="HistoryUpdateRequest", defaultEncodingId="i=700")
class HistoryUpdateRequest(Structure):
    requestHeader: RequestHeader = o6.field(name="RequestHeader")
    historyUpdateDetails: list[o6.ExtensionObject] = o6.field(name="HistoryUpdateDetails")


@o6.datatype(nodeId="i=701", browseName="HistoryUpdateResponse", defaultEncodingId="i=703")
class HistoryUpdateResponse(Structure):
    responseHeader: ResponseHeader = o6.field(name="ResponseHeader")
    results: list[HistoryUpdateResult] = o6.field(name="Results")
    diagnosticInfos: list[o6.DiagnosticInfo] = o6.field(name="DiagnosticInfos")


@o6.datatype(nodeId="i=704", browseName="CallMethodRequest", defaultEncodingId="i=706")
class CallMethodRequest(Structure):
    objectId: o6.NodeId = o6.field(name="ObjectId")
    methodId: o6.NodeId = o6.field(name="MethodId")
    inputArguments: list[Any] = o6.field(name="InputArguments")


@o6.datatype(nodeId="i=707", browseName="CallMethodResult", defaultEncodingId="i=709")
class CallMethodResult(Structure):
    statusCode: o6.StatusCode = o6.field(name="StatusCode")
    inputArgumentResults: list[o6.StatusCode] = o6.field(name="InputArgumentResults")
    inputArgumentDiagnosticInfos: list[o6.DiagnosticInfo] = o6.field(name="InputArgumentDiagnosticInfos")
    outputArguments: list[Any] = o6.field(name="OutputArguments")


@o6.datatype(nodeId="i=710", browseName="CallRequest", defaultEncodingId="i=712")
class CallRequest(Structure):
    requestHeader: RequestHeader = o6.field(name="RequestHeader")
    methodsToCall: list[CallMethodRequest] = o6.field(name="MethodsToCall")


@o6.datatype(nodeId="i=713", browseName="CallResponse", defaultEncodingId="i=715")
class CallResponse(Structure):
    responseHeader: ResponseHeader = o6.field(name="ResponseHeader")
    results: list[CallMethodResult] = o6.field(name="Results")
    diagnosticInfos: list[o6.DiagnosticInfo] = o6.field(name="DiagnosticInfos")


@o6.enumtype(nodeId="i=716", browseName="MonitoringMode")
class MonitoringMode(Enumeration):
    DISABLED = o6.enumfield(0, name="Disabled")
    SAMPLING = o6.enumfield(1, name="Sampling")
    REPORTING = o6.enumfield(2, name="Reporting")


@o6.enumtype(nodeId="i=717", browseName="DataChangeTrigger")
class DataChangeTrigger(Enumeration):
    STATUS = o6.enumfield(0, name="Status")
    STATUS_VALUE = o6.enumfield(1, name="StatusValue")
    STATUS_VALUE_TIMESTAMP = o6.enumfield(2, name="StatusValueTimestamp")


@o6.enumtype(nodeId="i=718", browseName="DeadbandType")
class DeadbandType(Enumeration):
    NONE = o6.enumfield(0, name="None")
    ABSOLUTE = o6.enumfield(1, name="Absolute")
    PERCENT = o6.enumfield(2, name="Percent")


@o6.datatype(nodeId="i=719", browseName="MonitoringFilter", defaultEncodingId="i=721")
class MonitoringFilter(Structure):
    pass


@o6.datatype(nodeId="i=722", browseName="DataChangeFilter", defaultEncodingId="i=724")
class DataChangeFilter(MonitoringFilter):
    trigger: DataChangeTrigger = o6.field(name="Trigger")
    deadbandType: o6.UInt32 = o6.field(name="DeadbandType")
    deadbandValue: o6.Double = o6.field(name="DeadbandValue")


@o6.datatype(nodeId="i=725", browseName="EventFilter", defaultEncodingId="i=727")
class EventFilter(MonitoringFilter):
    @classmethod
    def parse(cls, query: str, logger: object | None = None) -> EventFilter: ...

    selectClauses: list[SimpleAttributeOperand] = o6.field(name="SelectClauses")
    whereClause: ContentFilter = o6.field(name="WhereClause")


@o6.datatype(nodeId="i=644", browseName="ReadEventDetails", defaultEncodingId="i=646")
class ReadEventDetails(HistoryReadDetails):
    numValuesPerNode: o6.UInt32 = o6.field(name="NumValuesPerNode")
    startTime: o6.DateTime = o6.field(name="StartTime")
    endTime: o6.DateTime = o6.field(name="EndTime")
    filter: EventFilter = o6.field(name="Filter")


@o6.datatype(nodeId="i=731", browseName="MonitoringFilterResult", defaultEncodingId="i=733")
class MonitoringFilterResult(Structure):
    pass


@o6.datatype(nodeId="i=734", browseName="EventFilterResult", defaultEncodingId="i=736")
class EventFilterResult(MonitoringFilterResult):
    selectClauseResults: list[o6.StatusCode] = o6.field(name="SelectClauseResults")
    selectClauseDiagnosticInfos: list[o6.DiagnosticInfo] = o6.field(name="SelectClauseDiagnosticInfos")
    whereClauseResult: ContentFilterResult = o6.field(name="WhereClauseResult")


@o6.datatype(nodeId="i=740", browseName="MonitoringParameters", defaultEncodingId="i=742")
class MonitoringParameters(Structure):
    clientHandle: o6.UInt32 = o6.field(name="ClientHandle")
    samplingInterval: o6.Double = o6.field(name="SamplingInterval")
    filter: o6.ExtensionObject = o6.field(name="Filter")
    queueSize: o6.UInt32 = o6.field(name="QueueSize")
    discardOldest: o6.Boolean = o6.field(name="DiscardOldest")


@o6.datatype(nodeId="i=743", browseName="MonitoredItemCreateRequest", defaultEncodingId="i=745")
class MonitoredItemCreateRequest(Structure):
    itemToMonitor: ReadValueId = o6.field(name="ItemToMonitor")
    monitoringMode: MonitoringMode = o6.field(name="MonitoringMode")
    requestedParameters: MonitoringParameters = o6.field(name="RequestedParameters")


@o6.datatype(nodeId="i=746", browseName="MonitoredItemCreateResult", defaultEncodingId="i=748")
class MonitoredItemCreateResult(Structure):
    statusCode: o6.StatusCode = o6.field(name="StatusCode")
    monitoredItemId: o6.UInt32 = o6.field(name="MonitoredItemId")
    revisedSamplingInterval: o6.Double = o6.field(name="RevisedSamplingInterval")
    revisedQueueSize: o6.UInt32 = o6.field(name="RevisedQueueSize")
    filterResult: o6.ExtensionObject = o6.field(name="FilterResult")


@o6.datatype(nodeId="i=749", browseName="CreateMonitoredItemsRequest", defaultEncodingId="i=751")
class CreateMonitoredItemsRequest(Structure):
    requestHeader: RequestHeader = o6.field(name="RequestHeader")
    subscriptionId: o6.UInt32 = o6.field(name="SubscriptionId")
    timestampsToReturn: TimestampsToReturn = o6.field(name="TimestampsToReturn")
    itemsToCreate: list[MonitoredItemCreateRequest] = o6.field(name="ItemsToCreate")


@o6.datatype(nodeId="i=752", browseName="CreateMonitoredItemsResponse", defaultEncodingId="i=754")
class CreateMonitoredItemsResponse(Structure):
    responseHeader: ResponseHeader = o6.field(name="ResponseHeader")
    results: list[MonitoredItemCreateResult] = o6.field(name="Results")
    diagnosticInfos: list[o6.DiagnosticInfo] = o6.field(name="DiagnosticInfos")


@o6.datatype(nodeId="i=755", browseName="MonitoredItemModifyRequest", defaultEncodingId="i=757")
class MonitoredItemModifyRequest(Structure):
    monitoredItemId: o6.UInt32 = o6.field(name="MonitoredItemId")
    requestedParameters: MonitoringParameters = o6.field(name="RequestedParameters")


@o6.datatype(nodeId="i=758", browseName="MonitoredItemModifyResult", defaultEncodingId="i=760")
class MonitoredItemModifyResult(Structure):
    statusCode: o6.StatusCode = o6.field(name="StatusCode")
    revisedSamplingInterval: o6.Double = o6.field(name="RevisedSamplingInterval")
    revisedQueueSize: o6.UInt32 = o6.field(name="RevisedQueueSize")
    filterResult: o6.ExtensionObject = o6.field(name="FilterResult")


@o6.datatype(nodeId="i=761", browseName="ModifyMonitoredItemsRequest", defaultEncodingId="i=763")
class ModifyMonitoredItemsRequest(Structure):
    requestHeader: RequestHeader = o6.field(name="RequestHeader")
    subscriptionId: o6.UInt32 = o6.field(name="SubscriptionId")
    timestampsToReturn: TimestampsToReturn = o6.field(name="TimestampsToReturn")
    itemsToModify: list[MonitoredItemModifyRequest] = o6.field(name="ItemsToModify")


@o6.datatype(nodeId="i=764", browseName="ModifyMonitoredItemsResponse", defaultEncodingId="i=766")
class ModifyMonitoredItemsResponse(Structure):
    responseHeader: ResponseHeader = o6.field(name="ResponseHeader")
    results: list[MonitoredItemModifyResult] = o6.field(name="Results")
    diagnosticInfos: list[o6.DiagnosticInfo] = o6.field(name="DiagnosticInfos")


@o6.datatype(nodeId="i=767", browseName="SetMonitoringModeRequest", defaultEncodingId="i=769")
class SetMonitoringModeRequest(Structure):
    requestHeader: RequestHeader = o6.field(name="RequestHeader")
    subscriptionId: o6.UInt32 = o6.field(name="SubscriptionId")
    monitoringMode: MonitoringMode = o6.field(name="MonitoringMode")
    monitoredItemIds: list[o6.UInt32] = o6.field(name="MonitoredItemIds")


@o6.datatype(nodeId="i=770", browseName="SetMonitoringModeResponse", defaultEncodingId="i=772")
class SetMonitoringModeResponse(Structure):
    responseHeader: ResponseHeader = o6.field(name="ResponseHeader")
    results: list[o6.StatusCode] = o6.field(name="Results")
    diagnosticInfos: list[o6.DiagnosticInfo] = o6.field(name="DiagnosticInfos")


@o6.datatype(nodeId="i=773", browseName="SetTriggeringRequest", defaultEncodingId="i=775")
class SetTriggeringRequest(Structure):
    requestHeader: RequestHeader = o6.field(name="RequestHeader")
    subscriptionId: o6.UInt32 = o6.field(name="SubscriptionId")
    triggeringItemId: o6.UInt32 = o6.field(name="TriggeringItemId")
    linksToAdd: list[o6.UInt32] = o6.field(name="LinksToAdd")
    linksToRemove: list[o6.UInt32] = o6.field(name="LinksToRemove")


@o6.datatype(nodeId="i=776", browseName="SetTriggeringResponse", defaultEncodingId="i=778")
class SetTriggeringResponse(Structure):
    responseHeader: ResponseHeader = o6.field(name="ResponseHeader")
    addResults: list[o6.StatusCode] = o6.field(name="AddResults")
    addDiagnosticInfos: list[o6.DiagnosticInfo] = o6.field(name="AddDiagnosticInfos")
    removeResults: list[o6.StatusCode] = o6.field(name="RemoveResults")
    removeDiagnosticInfos: list[o6.DiagnosticInfo] = o6.field(name="RemoveDiagnosticInfos")


@o6.datatype(nodeId="i=779", browseName="DeleteMonitoredItemsRequest", defaultEncodingId="i=781")
class DeleteMonitoredItemsRequest(Structure):
    requestHeader: RequestHeader = o6.field(name="RequestHeader")
    subscriptionId: o6.UInt32 = o6.field(name="SubscriptionId")
    monitoredItemIds: list[o6.UInt32] = o6.field(name="MonitoredItemIds")


@o6.datatype(nodeId="i=782", browseName="DeleteMonitoredItemsResponse", defaultEncodingId="i=784")
class DeleteMonitoredItemsResponse(Structure):
    responseHeader: ResponseHeader = o6.field(name="ResponseHeader")
    results: list[o6.StatusCode] = o6.field(name="Results")
    diagnosticInfos: list[o6.DiagnosticInfo] = o6.field(name="DiagnosticInfos")


@o6.datatype(nodeId="i=785", browseName="CreateSubscriptionRequest", defaultEncodingId="i=787")
class CreateSubscriptionRequest(Structure):
    requestHeader: RequestHeader = o6.field(name="RequestHeader")
    requestedPublishingInterval: o6.Double = o6.field(name="RequestedPublishingInterval")
    requestedLifetimeCount: o6.UInt32 = o6.field(name="RequestedLifetimeCount")
    requestedMaxKeepAliveCount: o6.UInt32 = o6.field(name="RequestedMaxKeepAliveCount")
    maxNotificationsPerPublish: o6.UInt32 = o6.field(name="MaxNotificationsPerPublish")
    publishingEnabled: o6.Boolean = o6.field(name="PublishingEnabled")
    priority: o6.Byte = o6.field(name="Priority")


@o6.datatype(nodeId="i=788", browseName="CreateSubscriptionResponse", defaultEncodingId="i=790")
class CreateSubscriptionResponse(Structure):
    responseHeader: ResponseHeader = o6.field(name="ResponseHeader")
    subscriptionId: o6.UInt32 = o6.field(name="SubscriptionId")
    revisedPublishingInterval: o6.Double = o6.field(name="RevisedPublishingInterval")
    revisedLifetimeCount: o6.UInt32 = o6.field(name="RevisedLifetimeCount")
    revisedMaxKeepAliveCount: o6.UInt32 = o6.field(name="RevisedMaxKeepAliveCount")


@o6.datatype(nodeId="i=791", browseName="ModifySubscriptionRequest", defaultEncodingId="i=793")
class ModifySubscriptionRequest(Structure):
    requestHeader: RequestHeader = o6.field(name="RequestHeader")
    subscriptionId: o6.UInt32 = o6.field(name="SubscriptionId")
    requestedPublishingInterval: o6.Double = o6.field(name="RequestedPublishingInterval")
    requestedLifetimeCount: o6.UInt32 = o6.field(name="RequestedLifetimeCount")
    requestedMaxKeepAliveCount: o6.UInt32 = o6.field(name="RequestedMaxKeepAliveCount")
    maxNotificationsPerPublish: o6.UInt32 = o6.field(name="MaxNotificationsPerPublish")
    priority: o6.Byte = o6.field(name="Priority")


@o6.datatype(nodeId="i=794", browseName="ModifySubscriptionResponse", defaultEncodingId="i=796")
class ModifySubscriptionResponse(Structure):
    responseHeader: ResponseHeader = o6.field(name="ResponseHeader")
    revisedPublishingInterval: o6.Double = o6.field(name="RevisedPublishingInterval")
    revisedLifetimeCount: o6.UInt32 = o6.field(name="RevisedLifetimeCount")
    revisedMaxKeepAliveCount: o6.UInt32 = o6.field(name="RevisedMaxKeepAliveCount")


@o6.datatype(nodeId="i=797", browseName="SetPublishingModeRequest", defaultEncodingId="i=799")
class SetPublishingModeRequest(Structure):
    requestHeader: RequestHeader = o6.field(name="RequestHeader")
    publishingEnabled: o6.Boolean = o6.field(name="PublishingEnabled")
    subscriptionIds: list[o6.UInt32] = o6.field(name="SubscriptionIds")


@o6.datatype(nodeId="i=800", browseName="SetPublishingModeResponse", defaultEncodingId="i=802")
class SetPublishingModeResponse(Structure):
    responseHeader: ResponseHeader = o6.field(name="ResponseHeader")
    results: list[o6.StatusCode] = o6.field(name="Results")
    diagnosticInfos: list[o6.DiagnosticInfo] = o6.field(name="DiagnosticInfos")


@o6.datatype(nodeId="i=803", browseName="NotificationMessage", defaultEncodingId="i=805")
class NotificationMessage(Structure):
    sequenceNumber: o6.UInt32 = o6.field(name="SequenceNumber")
    publishTime: o6.DateTime = o6.field(name="PublishTime")
    notificationData: list[o6.ExtensionObject] = o6.field(name="NotificationData")


@o6.datatype(nodeId="i=806", browseName="MonitoredItemNotification", defaultEncodingId="i=808")
class MonitoredItemNotification(Structure):
    clientHandle: o6.UInt32 = o6.field(name="ClientHandle")
    value: o6.DataValue = o6.field(name="Value")


@o6.datatype(nodeId="i=821", browseName="SubscriptionAcknowledgement", defaultEncodingId="i=823")
class SubscriptionAcknowledgement(Structure):
    subscriptionId: o6.UInt32 = o6.field(name="SubscriptionId")
    sequenceNumber: o6.UInt32 = o6.field(name="SequenceNumber")


@o6.datatype(nodeId="i=824", browseName="PublishRequest", defaultEncodingId="i=826")
class PublishRequest(Structure):
    requestHeader: RequestHeader = o6.field(name="RequestHeader")
    subscriptionAcknowledgements: list[SubscriptionAcknowledgement] = o6.field(name="SubscriptionAcknowledgements")


@o6.datatype(nodeId="i=827", browseName="PublishResponse", defaultEncodingId="i=829")
class PublishResponse(Structure):
    responseHeader: ResponseHeader = o6.field(name="ResponseHeader")
    subscriptionId: o6.UInt32 = o6.field(name="SubscriptionId")
    availableSequenceNumbers: list[o6.UInt32] = o6.field(name="AvailableSequenceNumbers")
    moreNotifications: o6.Boolean = o6.field(name="MoreNotifications")
    notificationMessage: NotificationMessage = o6.field(name="NotificationMessage")
    results: list[o6.StatusCode] = o6.field(name="Results")
    diagnosticInfos: list[o6.DiagnosticInfo] = o6.field(name="DiagnosticInfos")


@o6.datatype(nodeId="i=830", browseName="RepublishRequest", defaultEncodingId="i=832")
class RepublishRequest(Structure):
    requestHeader: RequestHeader = o6.field(name="RequestHeader")
    subscriptionId: o6.UInt32 = o6.field(name="SubscriptionId")
    retransmitSequenceNumber: o6.UInt32 = o6.field(name="RetransmitSequenceNumber")


@o6.datatype(nodeId="i=833", browseName="RepublishResponse", defaultEncodingId="i=835")
class RepublishResponse(Structure):
    responseHeader: ResponseHeader = o6.field(name="ResponseHeader")
    notificationMessage: NotificationMessage = o6.field(name="NotificationMessage")


@o6.datatype(nodeId="i=836", browseName="TransferResult", defaultEncodingId="i=838")
class TransferResult(Structure):
    statusCode: o6.StatusCode = o6.field(name="StatusCode")
    availableSequenceNumbers: list[o6.UInt32] = o6.field(name="AvailableSequenceNumbers")


@o6.datatype(nodeId="i=839", browseName="TransferSubscriptionsRequest", defaultEncodingId="i=841")
class TransferSubscriptionsRequest(Structure):
    requestHeader: RequestHeader = o6.field(name="RequestHeader")
    subscriptionIds: list[o6.UInt32] = o6.field(name="SubscriptionIds")
    sendInitialValues: o6.Boolean = o6.field(name="SendInitialValues")


@o6.datatype(nodeId="i=842", browseName="TransferSubscriptionsResponse", defaultEncodingId="i=844")
class TransferSubscriptionsResponse(Structure):
    responseHeader: ResponseHeader = o6.field(name="ResponseHeader")
    results: list[TransferResult] = o6.field(name="Results")
    diagnosticInfos: list[o6.DiagnosticInfo] = o6.field(name="DiagnosticInfos")


@o6.datatype(nodeId="i=845", browseName="DeleteSubscriptionsRequest", defaultEncodingId="i=847")
class DeleteSubscriptionsRequest(Structure):
    requestHeader: RequestHeader = o6.field(name="RequestHeader")
    subscriptionIds: list[o6.UInt32] = o6.field(name="SubscriptionIds")


@o6.datatype(nodeId="i=848", browseName="DeleteSubscriptionsResponse", defaultEncodingId="i=850")
class DeleteSubscriptionsResponse(Structure):
    responseHeader: ResponseHeader = o6.field(name="ResponseHeader")
    results: list[o6.StatusCode] = o6.field(name="Results")
    diagnosticInfos: list[o6.DiagnosticInfo] = o6.field(name="DiagnosticInfos")


@o6.enumtype(nodeId="i=851", browseName="RedundancySupport")
class RedundancySupport(Enumeration):
    NONE = o6.enumfield(0, name="None")
    COLD = o6.enumfield(1, name="Cold")
    WARM = o6.enumfield(2, name="Warm")
    HOT = o6.enumfield(3, name="Hot")
    TRANSPARENT = o6.enumfield(4, name="Transparent")
    HOT_AND_MIRRORED = o6.enumfield(5, name="HotAndMirrored")


@o6.enumtype(nodeId="i=852", browseName="ServerState")
class ServerState(Enumeration):
    RUNNING = o6.enumfield(0, name="Running")
    FAILED = o6.enumfield(1, name="Failed")
    NO_CONFIGURATION = o6.enumfield(2, name="NoConfiguration")
    SUSPENDED = o6.enumfield(3, name="Suspended")
    SHUTDOWN = o6.enumfield(4, name="Shutdown")
    TEST = o6.enumfield(5, name="Test")
    COMMUNICATION_FAULT = o6.enumfield(6, name="CommunicationFault")
    UNKNOWN = o6.enumfield(7, name="Unknown")


@o6.datatype(nodeId="i=853", browseName="RedundantServerDataType", defaultEncodingId="i=855")
class RedundantServerDataType(Structure):
    serverId: o6.String = o6.field(name="ServerId")
    serviceLevel: o6.Byte = o6.field(name="ServiceLevel")
    serverState: ServerState = o6.field(name="ServerState")


@o6.datatype(nodeId="i=856", browseName="SamplingIntervalDiagnosticsDataType", defaultEncodingId="i=858")
class SamplingIntervalDiagnosticsDataType(Structure):
    samplingInterval: o6.Double = o6.field(name="SamplingInterval")
    monitoredItemCount: o6.UInt32 = o6.field(name="MonitoredItemCount")
    maxMonitoredItemCount: o6.UInt32 = o6.field(name="MaxMonitoredItemCount")
    disabledMonitoredItemCount: o6.UInt32 = o6.field(name="DisabledMonitoredItemCount")


@o6.datatype(nodeId="i=859", browseName="ServerDiagnosticsSummaryDataType", defaultEncodingId="i=861")
class ServerDiagnosticsSummaryDataType(Structure):
    serverViewCount: o6.UInt32 = o6.field(name="ServerViewCount")
    currentSessionCount: o6.UInt32 = o6.field(name="CurrentSessionCount")
    cumulatedSessionCount: o6.UInt32 = o6.field(name="CumulatedSessionCount")
    securityRejectedSessionCount: o6.UInt32 = o6.field(name="SecurityRejectedSessionCount")
    rejectedSessionCount: o6.UInt32 = o6.field(name="RejectedSessionCount")
    sessionTimeoutCount: o6.UInt32 = o6.field(name="SessionTimeoutCount")
    sessionAbortCount: o6.UInt32 = o6.field(name="SessionAbortCount")
    currentSubscriptionCount: o6.UInt32 = o6.field(name="CurrentSubscriptionCount")
    cumulatedSubscriptionCount: o6.UInt32 = o6.field(name="CumulatedSubscriptionCount")
    publishingIntervalCount: o6.UInt32 = o6.field(name="PublishingIntervalCount")
    securityRejectedRequestsCount: o6.UInt32 = o6.field(name="SecurityRejectedRequestsCount")
    rejectedRequestsCount: o6.UInt32 = o6.field(name="RejectedRequestsCount")


@o6.datatype(nodeId="i=862", browseName="ServerStatusDataType", defaultEncodingId="i=864")
class ServerStatusDataType(Structure):
    startTime: o6.DateTime = o6.field(name="StartTime")
    currentTime: o6.DateTime = o6.field(name="CurrentTime")
    state: ServerState = o6.field(name="State")
    buildInfo: BuildInfo = o6.field(name="BuildInfo")
    secondsTillShutdown: o6.UInt32 = o6.field(name="SecondsTillShutdown")
    shutdownReason: o6.LocalizedText = o6.field(name="ShutdownReason")


@o6.datatype(nodeId="i=868", browseName="SessionSecurityDiagnosticsDataType", defaultEncodingId="i=870")
class SessionSecurityDiagnosticsDataType(Structure):
    sessionId: o6.NodeId = o6.field(name="SessionId")
    clientUserIdOfSession: o6.String = o6.field(name="ClientUserIdOfSession")
    clientUserIdHistory: list[o6.String] = o6.field(name="ClientUserIdHistory")
    authenticationMechanism: o6.String = o6.field(name="AuthenticationMechanism")
    encoding: o6.String = o6.field(name="Encoding")
    transportProtocol: o6.String = o6.field(name="TransportProtocol")
    securityMode: MessageSecurityMode = o6.field(name="SecurityMode")
    securityPolicyUri: o6.String = o6.field(name="SecurityPolicyUri")
    clientCertificate: o6.ByteString = o6.field(name="ClientCertificate")


@o6.datatype(nodeId="i=871", browseName="ServiceCounterDataType", defaultEncodingId="i=873")
class ServiceCounterDataType(Structure):
    totalCount: o6.UInt32 = o6.field(name="TotalCount")
    errorCount: o6.UInt32 = o6.field(name="ErrorCount")


@o6.datatype(nodeId="i=865", browseName="SessionDiagnosticsDataType", defaultEncodingId="i=867")
class SessionDiagnosticsDataType(Structure):
    sessionId: o6.NodeId = o6.field(name="SessionId")
    sessionName: o6.String = o6.field(name="SessionName")
    clientDescription: ApplicationDescription = o6.field(name="ClientDescription")
    serverUri: o6.String = o6.field(name="ServerUri")
    endpointUrl: o6.String = o6.field(name="EndpointUrl")
    localeIds: list[o6.String] = o6.field(name="LocaleIds")
    actualSessionTimeout: o6.Double = o6.field(name="ActualSessionTimeout")
    maxResponseMessageSize: o6.UInt32 = o6.field(name="MaxResponseMessageSize")
    clientConnectionTime: o6.DateTime = o6.field(name="ClientConnectionTime")
    clientLastContactTime: o6.DateTime = o6.field(name="ClientLastContactTime")
    currentSubscriptionsCount: o6.UInt32 = o6.field(name="CurrentSubscriptionsCount")
    currentMonitoredItemsCount: o6.UInt32 = o6.field(name="CurrentMonitoredItemsCount")
    currentPublishRequestsInQueue: o6.UInt32 = o6.field(name="CurrentPublishRequestsInQueue")
    totalRequestCount: ServiceCounterDataType = o6.field(name="TotalRequestCount")
    unauthorizedRequestCount: o6.UInt32 = o6.field(name="UnauthorizedRequestCount")
    readCount: ServiceCounterDataType = o6.field(name="ReadCount")
    historyReadCount: ServiceCounterDataType = o6.field(name="HistoryReadCount")
    writeCount: ServiceCounterDataType = o6.field(name="WriteCount")
    historyUpdateCount: ServiceCounterDataType = o6.field(name="HistoryUpdateCount")
    callCount: ServiceCounterDataType = o6.field(name="CallCount")
    createMonitoredItemsCount: ServiceCounterDataType = o6.field(name="CreateMonitoredItemsCount")
    modifyMonitoredItemsCount: ServiceCounterDataType = o6.field(name="ModifyMonitoredItemsCount")
    setMonitoringModeCount: ServiceCounterDataType = o6.field(name="SetMonitoringModeCount")
    setTriggeringCount: ServiceCounterDataType = o6.field(name="SetTriggeringCount")
    deleteMonitoredItemsCount: ServiceCounterDataType = o6.field(name="DeleteMonitoredItemsCount")
    createSubscriptionCount: ServiceCounterDataType = o6.field(name="CreateSubscriptionCount")
    modifySubscriptionCount: ServiceCounterDataType = o6.field(name="ModifySubscriptionCount")
    setPublishingModeCount: ServiceCounterDataType = o6.field(name="SetPublishingModeCount")
    publishCount: ServiceCounterDataType = o6.field(name="PublishCount")
    republishCount: ServiceCounterDataType = o6.field(name="RepublishCount")
    transferSubscriptionsCount: ServiceCounterDataType = o6.field(name="TransferSubscriptionsCount")
    deleteSubscriptionsCount: ServiceCounterDataType = o6.field(name="DeleteSubscriptionsCount")
    addNodesCount: ServiceCounterDataType = o6.field(name="AddNodesCount")
    addReferencesCount: ServiceCounterDataType = o6.field(name="AddReferencesCount")
    deleteNodesCount: ServiceCounterDataType = o6.field(name="DeleteNodesCount")
    deleteReferencesCount: ServiceCounterDataType = o6.field(name="DeleteReferencesCount")
    browseCount: ServiceCounterDataType = o6.field(name="BrowseCount")
    browseNextCount: ServiceCounterDataType = o6.field(name="BrowseNextCount")
    translateBrowsePathsToNodeIdsCount: ServiceCounterDataType = o6.field(name="TranslateBrowsePathsToNodeIdsCount")
    queryFirstCount: ServiceCounterDataType = o6.field(name="QueryFirstCount")
    queryNextCount: ServiceCounterDataType = o6.field(name="QueryNextCount")
    registerNodesCount: ServiceCounterDataType = o6.field(name="RegisterNodesCount")
    unregisterNodesCount: ServiceCounterDataType = o6.field(name="UnregisterNodesCount")


@o6.datatype(nodeId="i=874", browseName="SubscriptionDiagnosticsDataType", defaultEncodingId="i=876")
class SubscriptionDiagnosticsDataType(Structure):
    sessionId: o6.NodeId = o6.field(name="SessionId")
    subscriptionId: o6.UInt32 = o6.field(name="SubscriptionId")
    priority: o6.Byte = o6.field(name="Priority")
    publishingInterval: o6.Double = o6.field(name="PublishingInterval")
    maxKeepAliveCount: o6.UInt32 = o6.field(name="MaxKeepAliveCount")
    maxLifetimeCount: o6.UInt32 = o6.field(name="MaxLifetimeCount")
    maxNotificationsPerPublish: o6.UInt32 = o6.field(name="MaxNotificationsPerPublish")
    publishingEnabled: o6.Boolean = o6.field(name="PublishingEnabled")
    modifyCount: o6.UInt32 = o6.field(name="ModifyCount")
    enableCount: o6.UInt32 = o6.field(name="EnableCount")
    disableCount: o6.UInt32 = o6.field(name="DisableCount")
    republishRequestCount: o6.UInt32 = o6.field(name="RepublishRequestCount")
    republishMessageRequestCount: o6.UInt32 = o6.field(name="RepublishMessageRequestCount")
    republishMessageCount: o6.UInt32 = o6.field(name="RepublishMessageCount")
    transferRequestCount: o6.UInt32 = o6.field(name="TransferRequestCount")
    transferredToAltClientCount: o6.UInt32 = o6.field(name="TransferredToAltClientCount")
    transferredToSameClientCount: o6.UInt32 = o6.field(name="TransferredToSameClientCount")
    publishRequestCount: o6.UInt32 = o6.field(name="PublishRequestCount")
    dataChangeNotificationsCount: o6.UInt32 = o6.field(name="DataChangeNotificationsCount")
    eventNotificationsCount: o6.UInt32 = o6.field(name="EventNotificationsCount")
    notificationsCount: o6.UInt32 = o6.field(name="NotificationsCount")
    latePublishRequestCount: o6.UInt32 = o6.field(name="LatePublishRequestCount")
    currentKeepAliveCount: o6.UInt32 = o6.field(name="CurrentKeepAliveCount")
    currentLifetimeCount: o6.UInt32 = o6.field(name="CurrentLifetimeCount")
    unacknowledgedMessageCount: o6.UInt32 = o6.field(name="UnacknowledgedMessageCount")
    discardedMessageCount: o6.UInt32 = o6.field(name="DiscardedMessageCount")
    monitoredItemCount: o6.UInt32 = o6.field(name="MonitoredItemCount")
    disabledMonitoredItemCount: o6.UInt32 = o6.field(name="DisabledMonitoredItemCount")
    monitoringQueueOverflowCount: o6.UInt32 = o6.field(name="MonitoringQueueOverflowCount")
    nextSequenceNumber: o6.UInt32 = o6.field(name="NextSequenceNumber")
    eventQueueOverflowCount: o6.UInt32 = o6.field(name="EventQueueOverflowCount")


@o6.datatype(nodeId="i=877", browseName="ModelChangeStructureDataType", defaultEncodingId="i=879")
class ModelChangeStructureDataType(Structure):
    affected: o6.NodeId = o6.field(name="Affected")
    affectedType: o6.NodeId = o6.field(name="AffectedType")
    verb: o6.Byte = o6.field(name="Verb")


@o6.datatype(nodeId="i=884", browseName="Range", defaultEncodingId="i=886")
class Range(Structure):
    low: o6.Double = o6.field(name="Low")
    high: o6.Double = o6.field(name="High")


@o6.datatype(nodeId="i=887", browseName="EUInformation", defaultEncodingId="i=889")
class EUInformation(Structure):
    namespaceUri: o6.String = o6.field(name="NamespaceUri")
    unitId: o6.Int32 = o6.field(name="UnitId")
    displayName: o6.LocalizedText = o6.field(name="DisplayName")
    description: o6.LocalizedText = o6.field(name="Description")


@o6.enumtype(nodeId="i=890", browseName="ExceptionDeviationFormat")
class ExceptionDeviationFormat(Enumeration):
    ABSOLUTE_VALUE = o6.enumfield(0, name="AbsoluteValue")
    PERCENT_OF_VALUE = o6.enumfield(1, name="PercentOfValue")
    PERCENT_OF_RANGE = o6.enumfield(2, name="PercentOfRange")
    PERCENT_OF_EU_RANGE = o6.enumfield(3, name="PercentOfEURange")
    UNKNOWN = o6.enumfield(4, name="Unknown")


@o6.datatype(nodeId="i=891", browseName="Annotation", defaultEncodingId="i=893")
class Annotation(Structure):
    message: o6.String = o6.field(name="Message")
    userName: o6.String = o6.field(name="UserName")
    annotationTime: o6.DateTime = o6.field(name="AnnotationTime")


@o6.datatype(nodeId="i=894", browseName="ProgramDiagnosticDataType", defaultEncodingId="i=896")
class ProgramDiagnosticDataType(Structure):
    createSessionId: o6.NodeId = o6.field(name="CreateSessionId")
    createClientName: o6.String = o6.field(name="CreateClientName")
    invocationCreationTime: o6.DateTime = o6.field(name="InvocationCreationTime")
    lastTransitionTime: o6.DateTime = o6.field(name="LastTransitionTime")
    lastMethodCall: o6.String = o6.field(name="LastMethodCall")
    lastMethodSessionId: o6.NodeId = o6.field(name="LastMethodSessionId")
    lastMethodInputArguments: list[Argument] = o6.field(name="LastMethodInputArguments")
    lastMethodOutputArguments: list[Argument] = o6.field(name="LastMethodOutputArguments")
    lastMethodCallTime: o6.DateTime = o6.field(name="LastMethodCallTime")
    lastMethodReturnStatus: StatusResult = o6.field(name="LastMethodReturnStatus")


@o6.datatype(nodeId="i=897", browseName="SemanticChangeStructureDataType", defaultEncodingId="i=899")
class SemanticChangeStructureDataType(Structure):
    affected: o6.NodeId = o6.field(name="Affected")
    affectedType: o6.NodeId = o6.field(name="AffectedType")


@o6.datatype(nodeId="i=917", browseName="EventFieldList", defaultEncodingId="i=919")
class EventFieldList(Structure):
    clientHandle: o6.UInt32 = o6.field(name="ClientHandle")
    eventFields: list[Any] = o6.field(name="EventFields")


@o6.datatype(nodeId="i=920", browseName="HistoryEventFieldList", defaultEncodingId="i=922")
class HistoryEventFieldList(Structure):
    eventFields: list[Any] = o6.field(name="EventFields")


@o6.datatype(nodeId="i=659", browseName="HistoryEvent", defaultEncodingId="i=661")
class HistoryEvent(Structure):
    events: list[HistoryEventFieldList] = o6.field(name="Events")


@o6.datatype(nodeId="i=938", browseName="IssuedIdentityToken", defaultEncodingId="i=940")
class IssuedIdentityToken(UserIdentityToken):
    policyId: o6.String = o6.field(name="PolicyId")
    tokenData: o6.ByteString = o6.field(name="TokenData")
    encryptionAlgorithm: o6.String = o6.field(name="EncryptionAlgorithm")


@o6.datatype(nodeId="i=945", browseName="NotificationData", defaultEncodingId="i=947")
class NotificationData(Structure):
    pass


@o6.datatype(nodeId="i=809", browseName="DataChangeNotification", defaultEncodingId="i=811")
class DataChangeNotification(NotificationData):
    monitoredItems: list[MonitoredItemNotification] = o6.field(name="MonitoredItems")
    diagnosticInfos: list[o6.DiagnosticInfo] = o6.field(name="DiagnosticInfos")


@o6.datatype(nodeId="i=818", browseName="StatusChangeNotification", defaultEncodingId="i=820")
class StatusChangeNotification(NotificationData):
    status: o6.StatusCode = o6.field(name="Status")
    diagnosticInfo: o6.DiagnosticInfo = o6.field(name="DiagnosticInfo")


@o6.datatype(nodeId="i=914", browseName="EventNotificationList", defaultEncodingId="i=916")
class EventNotificationList(NotificationData):
    events: list[EventFieldList] = o6.field(name="Events")


@o6.datatype(nodeId="i=948", browseName="AggregateConfiguration", defaultEncodingId="i=950")
class AggregateConfiguration(Structure):
    useServerCapabilitiesDefaults: o6.Boolean = o6.field(name="UseServerCapabilitiesDefaults")
    treatUncertainAsBad: o6.Boolean = o6.field(name="TreatUncertainAsBad")
    percentDataBad: o6.Byte = o6.field(name="PercentDataBad")
    percentDataGood: o6.Byte = o6.field(name="PercentDataGood")
    useSlopedExtrapolation: o6.Boolean = o6.field(name="UseSlopedExtrapolation")


@o6.datatype(nodeId="i=650", browseName="ReadProcessedDetails", defaultEncodingId="i=652")
class ReadProcessedDetails(HistoryReadDetails):
    startTime: o6.DateTime = o6.field(name="StartTime")
    endTime: o6.DateTime = o6.field(name="EndTime")
    processingInterval: o6.Double = o6.field(name="ProcessingInterval")
    aggregateType: list[o6.NodeId] = o6.field(name="AggregateType")
    aggregateConfiguration: AggregateConfiguration = o6.field(name="AggregateConfiguration")


@o6.datatype(nodeId="i=728", browseName="AggregateFilter", defaultEncodingId="i=730")
class AggregateFilter(MonitoringFilter):
    startTime: o6.DateTime = o6.field(name="StartTime")
    aggregateType: o6.NodeId = o6.field(name="AggregateType")
    processingInterval: o6.Double = o6.field(name="ProcessingInterval")
    aggregateConfiguration: AggregateConfiguration = o6.field(name="AggregateConfiguration")


@o6.datatype(nodeId="i=737", browseName="AggregateFilterResult", defaultEncodingId="i=739")
class AggregateFilterResult(MonitoringFilterResult):
    revisedStartTime: o6.DateTime = o6.field(name="RevisedStartTime")
    revisedProcessingInterval: o6.Double = o6.field(name="RevisedProcessingInterval")
    revisedAggregateConfiguration: AggregateConfiguration = o6.field(name="RevisedAggregateConfiguration")


@o6.datatype(nodeId="i=2000", browseName="ImageBMP", parent="i=30")
class ImageBMP:
    pass


@o6.datatype(nodeId="i=2001", browseName="ImageGIF", parent="i=30")
class ImageGIF:
    pass


@o6.datatype(nodeId="i=2002", browseName="ImageJPG", parent="i=30")
class ImageJPG:
    pass


@o6.datatype(nodeId="i=2003", browseName="ImagePNG", parent="i=30")
class ImagePNG:
    pass


@o6.datatype(nodeId="i=7594", browseName="EnumValueType", defaultEncodingId="i=8251")
class EnumValueType(Structure):
    value: o6.Int64 = o6.field(name="Value")
    displayName: o6.LocalizedText = o6.field(name="DisplayName")
    description: o6.LocalizedText = o6.field(name="Description")


@o6.datatype(nodeId="i=102", browseName="EnumField", defaultEncodingId="i=14845")
class EnumField(EnumValueType):
    value: o6.Int64 = o6.field(name="Value")
    displayName: o6.LocalizedText = o6.field(name="DisplayName")
    description: o6.LocalizedText = o6.field(name="Description")
    name: o6.String = o6.field(name="Name")


@o6.datatype(nodeId="i=100", browseName="EnumDefinition", defaultEncodingId="i=123")
class EnumDefinition(DataTypeDefinition):
    fields: list[EnumField] = o6.field(name="Fields")


@o6.datatype(nodeId="i=8912", browseName="TimeZoneDataType", defaultEncodingId="i=8917")
class TimeZoneDataType(Structure):
    offset: o6.Int16 = o6.field(name="Offset")
    daylightSavingInOffset: o6.Boolean = o6.field(name="DaylightSavingInOffset")


@o6.enumtype(nodeId="i=11234", browseName="HistoryUpdateType")
class HistoryUpdateType(Enumeration):
    INSERT = o6.enumfield(1, name="Insert")
    REPLACE = o6.enumfield(2, name="Replace")
    UPDATE = o6.enumfield(3, name="Update")
    DELETE = o6.enumfield(4, name="Delete")


@o6.datatype(nodeId="i=11216", browseName="ModificationInfo", defaultEncodingId="i=11226")
class ModificationInfo(Structure):
    modificationTime: o6.DateTime = o6.field(name="ModificationTime")
    updateType: HistoryUpdateType = o6.field(name="UpdateType")
    userName: o6.String = o6.field(name="UserName")


@o6.datatype(nodeId="i=11217", browseName="HistoryModifiedData", defaultEncodingId="i=11227")
class HistoryModifiedData(HistoryData):
    dataValues: list[o6.DataValue] = o6.field(name="DataValues")
    modificationInfos: list[ModificationInfo] = o6.field(name="ModificationInfos")


@o6.enumtype(nodeId="i=11293", browseName="PerformUpdateType")
class PerformUpdateType(Enumeration):
    INSERT = o6.enumfield(1, name="Insert")
    REPLACE = o6.enumfield(2, name="Replace")
    UPDATE = o6.enumfield(3, name="Update")
    REMOVE = o6.enumfield(4, name="Remove")


@o6.datatype(nodeId="i=680", browseName="UpdateDataDetails", defaultEncodingId="i=682")
class UpdateDataDetails(HistoryUpdateDetails):
    nodeId: o6.NodeId = o6.field(name="NodeId")
    performInsertReplace: PerformUpdateType = o6.field(name="PerformInsertReplace")
    updateValues: list[o6.DataValue] = o6.field(name="UpdateValues")


@o6.datatype(nodeId="i=683", browseName="UpdateEventDetails", defaultEncodingId="i=685")
class UpdateEventDetails(HistoryUpdateDetails):
    nodeId: o6.NodeId = o6.field(name="NodeId")
    performInsertReplace: PerformUpdateType = o6.field(name="PerformInsertReplace")
    filter: EventFilter = o6.field(name="Filter")
    eventData: list[HistoryEventFieldList] = o6.field(name="EventData")


@o6.datatype(nodeId="i=11295", browseName="UpdateStructureDataDetails", defaultEncodingId="i=11300")
class UpdateStructureDataDetails(HistoryUpdateDetails):
    nodeId: o6.NodeId = o6.field(name="NodeId")
    performInsertReplace: PerformUpdateType = o6.field(name="PerformInsertReplace")
    updateValues: list[o6.DataValue] = o6.field(name="UpdateValues")


@o6.datatype(nodeId="i=11737", browseName="BitFieldMaskDataType", parent="i=9")
class BitFieldMaskDataType:
    pass


@o6.datatype(nodeId="i=11879", browseName="InstanceNode", defaultEncodingId="i=11889")
class InstanceNode(Node):
    nodeId: o6.NodeId = o6.field(name="NodeId")
    nodeClass: NodeClass = o6.field(name="NodeClass")
    browseName: o6.QualifiedName = o6.field(name="BrowseName")
    displayName: o6.LocalizedText = o6.field(name="DisplayName")
    description: o6.LocalizedText = o6.field(name="Description")
    writeMask: o6.UInt32 = o6.field(name="WriteMask")
    userWriteMask: o6.UInt32 = o6.field(name="UserWriteMask")
    rolePermissions: list[RolePermissionType] = o6.field(name="RolePermissions")
    userRolePermissions: list[RolePermissionType] = o6.field(name="UserRolePermissions")
    accessRestrictions: o6.UInt16 = o6.field(name="AccessRestrictions")
    references: list[ReferenceNode] = o6.field(name="References")


@o6.datatype(nodeId="i=261", browseName="ObjectNode", defaultEncodingId="i=263")
class ObjectNode(InstanceNode):
    nodeId: o6.NodeId = o6.field(name="NodeId")
    nodeClass: NodeClass = o6.field(name="NodeClass")
    browseName: o6.QualifiedName = o6.field(name="BrowseName")
    displayName: o6.LocalizedText = o6.field(name="DisplayName")
    description: o6.LocalizedText = o6.field(name="Description")
    writeMask: o6.UInt32 = o6.field(name="WriteMask")
    userWriteMask: o6.UInt32 = o6.field(name="UserWriteMask")
    rolePermissions: list[RolePermissionType] = o6.field(name="RolePermissions")
    userRolePermissions: list[RolePermissionType] = o6.field(name="UserRolePermissions")
    accessRestrictions: o6.UInt16 = o6.field(name="AccessRestrictions")
    references: list[ReferenceNode] = o6.field(name="References")
    eventNotifier: o6.Byte = o6.field(name="EventNotifier")


@o6.datatype(nodeId="i=267", browseName="VariableNode", defaultEncodingId="i=269")
class VariableNode(InstanceNode):
    nodeId: o6.NodeId = o6.field(name="NodeId")
    nodeClass: NodeClass = o6.field(name="NodeClass")
    browseName: o6.QualifiedName = o6.field(name="BrowseName")
    displayName: o6.LocalizedText = o6.field(name="DisplayName")
    description: o6.LocalizedText = o6.field(name="Description")
    writeMask: o6.UInt32 = o6.field(name="WriteMask")
    userWriteMask: o6.UInt32 = o6.field(name="UserWriteMask")
    rolePermissions: list[RolePermissionType] = o6.field(name="RolePermissions")
    userRolePermissions: list[RolePermissionType] = o6.field(name="UserRolePermissions")
    accessRestrictions: o6.UInt16 = o6.field(name="AccessRestrictions")
    references: list[ReferenceNode] = o6.field(name="References")
    value: Any = o6.field(name="Value")
    dataType: o6.NodeId = o6.field(name="DataType")
    valueRank: o6.Int32 = o6.field(name="ValueRank")
    arrayDimensions: list[o6.UInt32] = o6.field(name="ArrayDimensions")
    accessLevel: o6.Byte = o6.field(name="AccessLevel")
    userAccessLevel: o6.Byte = o6.field(name="UserAccessLevel")
    minimumSamplingInterval: o6.Double = o6.field(name="MinimumSamplingInterval")
    historizing: o6.Boolean = o6.field(name="Historizing")
    accessLevelEx: o6.UInt32 = o6.field(name="AccessLevelEx")


@o6.datatype(nodeId="i=276", browseName="MethodNode", defaultEncodingId="i=278")
class MethodNode(InstanceNode):
    nodeId: o6.NodeId = o6.field(name="NodeId")
    nodeClass: NodeClass = o6.field(name="NodeClass")
    browseName: o6.QualifiedName = o6.field(name="BrowseName")
    displayName: o6.LocalizedText = o6.field(name="DisplayName")
    description: o6.LocalizedText = o6.field(name="Description")
    writeMask: o6.UInt32 = o6.field(name="WriteMask")
    userWriteMask: o6.UInt32 = o6.field(name="UserWriteMask")
    rolePermissions: list[RolePermissionType] = o6.field(name="RolePermissions")
    userRolePermissions: list[RolePermissionType] = o6.field(name="UserRolePermissions")
    accessRestrictions: o6.UInt16 = o6.field(name="AccessRestrictions")
    references: list[ReferenceNode] = o6.field(name="References")
    executable: o6.Boolean = o6.field(name="Executable")
    userExecutable: o6.Boolean = o6.field(name="UserExecutable")


@o6.datatype(nodeId="i=279", browseName="ViewNode", defaultEncodingId="i=281")
class ViewNode(InstanceNode):
    nodeId: o6.NodeId = o6.field(name="NodeId")
    nodeClass: NodeClass = o6.field(name="NodeClass")
    browseName: o6.QualifiedName = o6.field(name="BrowseName")
    displayName: o6.LocalizedText = o6.field(name="DisplayName")
    description: o6.LocalizedText = o6.field(name="Description")
    writeMask: o6.UInt32 = o6.field(name="WriteMask")
    userWriteMask: o6.UInt32 = o6.field(name="UserWriteMask")
    rolePermissions: list[RolePermissionType] = o6.field(name="RolePermissions")
    userRolePermissions: list[RolePermissionType] = o6.field(name="UserRolePermissions")
    accessRestrictions: o6.UInt16 = o6.field(name="AccessRestrictions")
    references: list[ReferenceNode] = o6.field(name="References")
    containsNoLoops: o6.Boolean = o6.field(name="ContainsNoLoops")
    eventNotifier: o6.Byte = o6.field(name="EventNotifier")


@o6.datatype(nodeId="i=11880", browseName="TypeNode", defaultEncodingId="i=11890")
class TypeNode(Node):
    nodeId: o6.NodeId = o6.field(name="NodeId")
    nodeClass: NodeClass = o6.field(name="NodeClass")
    browseName: o6.QualifiedName = o6.field(name="BrowseName")
    displayName: o6.LocalizedText = o6.field(name="DisplayName")
    description: o6.LocalizedText = o6.field(name="Description")
    writeMask: o6.UInt32 = o6.field(name="WriteMask")
    userWriteMask: o6.UInt32 = o6.field(name="UserWriteMask")
    rolePermissions: list[RolePermissionType] = o6.field(name="RolePermissions")
    userRolePermissions: list[RolePermissionType] = o6.field(name="UserRolePermissions")
    accessRestrictions: o6.UInt16 = o6.field(name="AccessRestrictions")
    references: list[ReferenceNode] = o6.field(name="References")


@o6.datatype(nodeId="i=264", browseName="ObjectTypeNode", defaultEncodingId="i=266")
class ObjectTypeNode(TypeNode):
    nodeId: o6.NodeId = o6.field(name="NodeId")
    nodeClass: NodeClass = o6.field(name="NodeClass")
    browseName: o6.QualifiedName = o6.field(name="BrowseName")
    displayName: o6.LocalizedText = o6.field(name="DisplayName")
    description: o6.LocalizedText = o6.field(name="Description")
    writeMask: o6.UInt32 = o6.field(name="WriteMask")
    userWriteMask: o6.UInt32 = o6.field(name="UserWriteMask")
    rolePermissions: list[RolePermissionType] = o6.field(name="RolePermissions")
    userRolePermissions: list[RolePermissionType] = o6.field(name="UserRolePermissions")
    accessRestrictions: o6.UInt16 = o6.field(name="AccessRestrictions")
    references: list[ReferenceNode] = o6.field(name="References")
    isAbstract: o6.Boolean = o6.field(name="IsAbstract")


@o6.datatype(nodeId="i=270", browseName="VariableTypeNode", defaultEncodingId="i=272")
class VariableTypeNode(TypeNode):
    nodeId: o6.NodeId = o6.field(name="NodeId")
    nodeClass: NodeClass = o6.field(name="NodeClass")
    browseName: o6.QualifiedName = o6.field(name="BrowseName")
    displayName: o6.LocalizedText = o6.field(name="DisplayName")
    description: o6.LocalizedText = o6.field(name="Description")
    writeMask: o6.UInt32 = o6.field(name="WriteMask")
    userWriteMask: o6.UInt32 = o6.field(name="UserWriteMask")
    rolePermissions: list[RolePermissionType] = o6.field(name="RolePermissions")
    userRolePermissions: list[RolePermissionType] = o6.field(name="UserRolePermissions")
    accessRestrictions: o6.UInt16 = o6.field(name="AccessRestrictions")
    references: list[ReferenceNode] = o6.field(name="References")
    value: Any = o6.field(name="Value")
    dataType: o6.NodeId = o6.field(name="DataType")
    valueRank: o6.Int32 = o6.field(name="ValueRank")
    arrayDimensions: list[o6.UInt32] = o6.field(name="ArrayDimensions")
    isAbstract: o6.Boolean = o6.field(name="IsAbstract")


@o6.datatype(nodeId="i=273", browseName="ReferenceTypeNode", defaultEncodingId="i=275")
class ReferenceTypeNode(TypeNode):
    nodeId: o6.NodeId = o6.field(name="NodeId")
    nodeClass: NodeClass = o6.field(name="NodeClass")
    browseName: o6.QualifiedName = o6.field(name="BrowseName")
    displayName: o6.LocalizedText = o6.field(name="DisplayName")
    description: o6.LocalizedText = o6.field(name="Description")
    writeMask: o6.UInt32 = o6.field(name="WriteMask")
    userWriteMask: o6.UInt32 = o6.field(name="UserWriteMask")
    rolePermissions: list[RolePermissionType] = o6.field(name="RolePermissions")
    userRolePermissions: list[RolePermissionType] = o6.field(name="UserRolePermissions")
    accessRestrictions: o6.UInt16 = o6.field(name="AccessRestrictions")
    references: list[ReferenceNode] = o6.field(name="References")
    isAbstract: o6.Boolean = o6.field(name="IsAbstract")
    symmetric: o6.Boolean = o6.field(name="Symmetric")
    inverseName: o6.LocalizedText = o6.field(name="InverseName")


@o6.datatype(nodeId="i=282", browseName="DataTypeNode", defaultEncodingId="i=284")
class DataTypeNode(TypeNode):
    nodeId: o6.NodeId = o6.field(name="NodeId")
    nodeClass: NodeClass = o6.field(name="NodeClass")
    browseName: o6.QualifiedName = o6.field(name="BrowseName")
    displayName: o6.LocalizedText = o6.field(name="DisplayName")
    description: o6.LocalizedText = o6.field(name="Description")
    writeMask: o6.UInt32 = o6.field(name="WriteMask")
    userWriteMask: o6.UInt32 = o6.field(name="UserWriteMask")
    rolePermissions: list[RolePermissionType] = o6.field(name="RolePermissions")
    userRolePermissions: list[RolePermissionType] = o6.field(name="UserRolePermissions")
    accessRestrictions: o6.UInt16 = o6.field(name="AccessRestrictions")
    references: list[ReferenceNode] = o6.field(name="References")
    isAbstract: o6.Boolean = o6.field(name="IsAbstract")
    dataTypeDefinition: o6.ExtensionObject = o6.field(name="DataTypeDefinition")


@o6.enumtype(nodeId="i=11939", browseName="OpenFileMode")
class OpenFileMode(Enumeration):
    READ = o6.enumfield(1, name="Read")
    WRITE = o6.enumfield(2, name="Write")
    ERASE_EXISTING = o6.enumfield(4, name="EraseExisting")
    APPEND = o6.enumfield(8, name="Append")


@o6.enumtype(nodeId="i=11941", browseName="ModelChangeStructureVerbMask")
class ModelChangeStructureVerbMask(Enumeration):
    NODE_ADDED = o6.enumfield(1, name="NodeAdded")
    NODE_DELETED = o6.enumfield(2, name="NodeDeleted")
    REFERENCE_ADDED = o6.enumfield(4, name="ReferenceAdded")
    REFERENCE_DELETED = o6.enumfield(8, name="ReferenceDeleted")
    DATA_TYPE_CHANGED = o6.enumfield(16, name="DataTypeChanged")


@o6.datatype(nodeId="i=11943", browseName="EndpointUrlListDataType", defaultEncodingId="i=11957")
class EndpointUrlListDataType(Structure):
    endpointUrlList: list[o6.String] = o6.field(name="EndpointUrlList")


@o6.datatype(nodeId="i=11944", browseName="NetworkGroupDataType", defaultEncodingId="i=11958")
class NetworkGroupDataType(Structure):
    serverUri: o6.String = o6.field(name="ServerUri")
    networkPaths: list[EndpointUrlListDataType] = o6.field(name="NetworkPaths")


@o6.enumtype(nodeId="i=12077", browseName="AxisScaleEnumeration")
class AxisScaleEnumeration(Enumeration):
    LINEAR = o6.enumfield(0, name="Linear")
    LOG = o6.enumfield(1, name="Log")
    LN = o6.enumfield(2, name="Ln")


@o6.datatype(nodeId="i=12079", browseName="AxisInformation", defaultEncodingId="i=12089")
class AxisInformation(Structure):
    engineeringUnits: EUInformation = o6.field(name="EngineeringUnits")
    eURange: Range = o6.field(name="EURange")
    title: o6.LocalizedText = o6.field(name="Title")
    axisScaleType: AxisScaleEnumeration = o6.field(name="AxisScaleType")
    axisSteps: list[o6.Double] = o6.field(name="AxisSteps")


@o6.datatype(nodeId="i=12080", browseName="XVType", defaultEncodingId="i=12090")
class XVType(Structure):
    x: o6.Double = o6.field(name="X")
    value: o6.Float = o6.field(name="Value")


@o6.datatype(nodeId="i=12171", browseName="ComplexNumberType", defaultEncodingId="i=12181")
class ComplexNumberType(Structure):
    real: o6.Float = o6.field(name="Real")
    imaginary: o6.Float = o6.field(name="Imaginary")


@o6.datatype(nodeId="i=12172", browseName="DoubleComplexNumberType", defaultEncodingId="i=12182")
class DoubleComplexNumberType(Structure):
    real: o6.Double = o6.field(name="Real")
    imaginary: o6.Double = o6.field(name="Imaginary")


@o6.datatype(nodeId="i=12189", browseName="ServerOnNetwork", defaultEncodingId="i=12207")
class ServerOnNetwork(Structure):
    recordId: o6.UInt32 = o6.field(name="RecordId")
    serverName: o6.String = o6.field(name="ServerName")
    discoveryUrl: o6.String = o6.field(name="DiscoveryUrl")
    serverCapabilities: list[o6.String] = o6.field(name="ServerCapabilities")


@o6.datatype(nodeId="i=12190", browseName="FindServersOnNetworkRequest", defaultEncodingId="i=12208")
class FindServersOnNetworkRequest(Structure):
    requestHeader: RequestHeader = o6.field(name="RequestHeader")
    startingRecordId: o6.UInt32 = o6.field(name="StartingRecordId")
    maxRecordsToReturn: o6.UInt32 = o6.field(name="MaxRecordsToReturn")
    serverCapabilityFilter: list[o6.String] = o6.field(name="ServerCapabilityFilter")


@o6.datatype(nodeId="i=12191", browseName="FindServersOnNetworkResponse", defaultEncodingId="i=12209")
class FindServersOnNetworkResponse(Structure):
    responseHeader: ResponseHeader = o6.field(name="ResponseHeader")
    lastCounterResetTime: o6.DateTime = o6.field(name="LastCounterResetTime")
    servers: list[ServerOnNetwork] = o6.field(name="Servers")


@o6.datatype(nodeId="i=12193", browseName="RegisterServer2Request", defaultEncodingId="i=12211")
class RegisterServer2Request(Structure):
    requestHeader: RequestHeader = o6.field(name="RequestHeader")
    server: RegisteredServer = o6.field(name="Server")
    discoveryConfiguration: list[o6.ExtensionObject] = o6.field(name="DiscoveryConfiguration")


@o6.datatype(nodeId="i=12194", browseName="RegisterServer2Response", defaultEncodingId="i=12212")
class RegisterServer2Response(Structure):
    responseHeader: ResponseHeader = o6.field(name="ResponseHeader")
    configurationResults: list[o6.StatusCode] = o6.field(name="ConfigurationResults")
    diagnosticInfos: list[o6.DiagnosticInfo] = o6.field(name="DiagnosticInfos")


@o6.enumtype(nodeId="i=12552", browseName="TrustListMasks")
class TrustListMasks(Enumeration):
    NONE = o6.enumfield(0, name="None")
    TRUSTED_CERTIFICATES = o6.enumfield(1, name="TrustedCertificates")
    TRUSTED_CRLS = o6.enumfield(2, name="TrustedCrls")
    ISSUER_CERTIFICATES = o6.enumfield(4, name="IssuerCertificates")
    ISSUER_CRLS = o6.enumfield(8, name="IssuerCrls")
    ALL = o6.enumfield(15, name="All")


@o6.datatype(nodeId="i=12554", browseName="TrustListDataType", defaultEncodingId="i=12680")
class TrustListDataType(Structure):
    specifiedLists: o6.UInt32 = o6.field(name="SpecifiedLists")
    trustedCertificates: list[o6.ByteString] = o6.field(name="TrustedCertificates")
    trustedCrls: list[o6.ByteString] = o6.field(name="TrustedCrls")
    issuerCertificates: list[o6.ByteString] = o6.field(name="IssuerCertificates")
    issuerCrls: list[o6.ByteString] = o6.field(name="IssuerCrls")


@o6.datatype(nodeId="i=12755", browseName="OptionSet", defaultEncodingId="i=12765", isAbstract=True)
class OptionSet(Structure):
    value: o6.ByteString = o6.field(name="Value")
    validBits: o6.ByteString = o6.field(name="ValidBits")


@o6.datatype(nodeId="i=12756", browseName="Union", defaultEncodingId="i=12766", isAbstract=True)
class Union(Structure):
    pass


@o6.datatype(nodeId="i=12877", browseName="NormalizedString", parent="i=12")
class NormalizedString:
    pass


@o6.datatype(nodeId="i=12878", browseName="DecimalString", parent="i=12")
class DecimalString:
    pass


@o6.datatype(nodeId="i=12879", browseName="DurationString", parent="i=12")
class DurationString:
    pass


@o6.datatype(nodeId="i=12880", browseName="TimeString", parent="i=12")
class TimeString:
    pass


@o6.datatype(nodeId="i=12881", browseName="DateString", parent="i=12")
class DateString:
    pass


@o6.datatype(nodeId="i=12890", browseName="DiscoveryConfiguration", defaultEncodingId="i=12900")
class DiscoveryConfiguration(Structure):
    pass


@o6.datatype(nodeId="i=12891", browseName="MdnsDiscoveryConfiguration", defaultEncodingId="i=12901")
class MdnsDiscoveryConfiguration(DiscoveryConfiguration):
    mdnsServerName: o6.String = o6.field(name="MdnsServerName")
    serverCapabilities: list[o6.String] = o6.field(name="ServerCapabilities")


@o6.datatype(nodeId="i=14273", browseName="PublishedVariableDataType", defaultEncodingId="i=14323")
class PublishedVariableDataType(Structure):
    publishedVariable: o6.NodeId = o6.field(name="PublishedVariable")
    attributeId: o6.UInt32 = o6.field(name="AttributeId")
    samplingIntervalHint: o6.Double = o6.field(name="SamplingIntervalHint")
    deadbandType: o6.UInt32 = o6.field(name="DeadbandType")
    deadbandValue: o6.Double = o6.field(name="DeadbandValue")
    indexRange: o6.String = o6.field(name="IndexRange")
    substituteValue: Any = o6.field(name="SubstituteValue")
    metaDataProperties: list[o6.QualifiedName] = o6.field(name="MetaDataProperties")


@o6.datatype(nodeId="i=14525", browseName="DataTypeDescription", defaultEncodingId="i=125", isAbstract=True)
class DataTypeDescription(Structure):
    dataTypeId: o6.NodeId = o6.field(name="DataTypeId")
    name: o6.QualifiedName = o6.field(name="Name")


@o6.datatype(nodeId="i=14533", browseName="KeyValuePair", defaultEncodingId="i=14846")
class KeyValuePair(Structure):
    key: o6.QualifiedName = o6.field(name="Key")
    value: Any = o6.field(name="Value")


@o6.datatype(nodeId="i=14593", browseName="ConfigurationVersionDataType", defaultEncodingId="i=14847")
class ConfigurationVersionDataType(Structure):
    majorVersion: o6.UInt32 = o6.field(name="MajorVersion")
    minorVersion: o6.UInt32 = o6.field(name="MinorVersion")


@o6.enumtype(nodeId="i=14647", browseName="PubSubState")
class PubSubState(Enumeration):
    DISABLED = o6.enumfield(0, name="Disabled")
    PAUSED = o6.enumfield(1, name="Paused")
    OPERATIONAL = o6.enumfield(2, name="Operational")
    ERROR = o6.enumfield(3, name="Error")
    PRE_OPERATIONAL = o6.enumfield(4, name="PreOperational")


@o6.datatype(nodeId="i=15005", browseName="SimpleTypeDescription", defaultEncodingId="i=15421")
class SimpleTypeDescription(DataTypeDescription):
    dataTypeId: o6.NodeId = o6.field(name="DataTypeId")
    name: o6.QualifiedName = o6.field(name="Name")
    baseDataType: o6.NodeId = o6.field(name="BaseDataType")
    builtInType: o6.Byte = o6.field(name="BuiltInType")


@o6.enumtype(nodeId="i=15008", browseName="BrokerTransportQualityOfService")
class BrokerTransportQualityOfService(Enumeration):
    NOT_SPECIFIED = o6.enumfield(0, name="NotSpecified")
    BEST_EFFORT = o6.enumfield(1, name="BestEffort")
    AT_LEAST_ONCE = o6.enumfield(2, name="AtLeastOnce")
    AT_MOST_ONCE = o6.enumfield(3, name="AtMostOnce")
    EXACTLY_ONCE = o6.enumfield(4, name="ExactlyOnce")


@o6.optionsettype(nodeId="i=15031", browseName="AccessLevelType", base=o6.Byte)
class AccessLevelType:
    CURRENT_READ = o6.bitmask(0x01 << 0, name="CurrentRead")
    CURRENT_WRITE = o6.bitmask(0x01 << 1, name="CurrentWrite")
    HISTORY_READ = o6.bitmask(0x01 << 2, name="HistoryRead")
    HISTORY_WRITE = o6.bitmask(0x01 << 3, name="HistoryWrite")
    SEMANTIC_CHANGE = o6.bitmask(0x01 << 4, name="SemanticChange")
    STATUS_WRITE = o6.bitmask(0x01 << 5, name="StatusWrite")
    TIMESTAMP_WRITE = o6.bitmask(0x01 << 6, name="TimestampWrite")


@o6.optionsettype(nodeId="i=15033", browseName="EventNotifierType", base=o6.Byte)
class EventNotifierType:
    SUBSCRIBE_TO_EVENTS = o6.bitmask(0x01 << 0, name="SubscribeToEvents")
    HISTORY_READ = o6.bitmask(0x01 << 2, name="HistoryRead")
    HISTORY_WRITE = o6.bitmask(0x01 << 3, name="HistoryWrite")


@o6.optionsettype(nodeId="i=15406", browseName="AccessLevelExType", base=o6.UInt32)
class AccessLevelExType:
    CURRENT_READ = o6.bitmask(0x01 << 0, name="CurrentRead")
    CURRENT_WRITE = o6.bitmask(0x01 << 1, name="CurrentWrite")
    HISTORY_READ = o6.bitmask(0x01 << 2, name="HistoryRead")
    HISTORY_WRITE = o6.bitmask(0x01 << 3, name="HistoryWrite")
    SEMANTIC_CHANGE = o6.bitmask(0x01 << 4, name="SemanticChange")
    STATUS_WRITE = o6.bitmask(0x01 << 5, name="StatusWrite")
    TIMESTAMP_WRITE = o6.bitmask(0x01 << 6, name="TimestampWrite")
    NONATOMIC_READ = o6.bitmask(0x01 << 8, name="NonatomicRead")
    NONATOMIC_WRITE = o6.bitmask(0x01 << 9, name="NonatomicWrite")
    WRITE_FULL_ARRAY_ONLY = o6.bitmask(0x01 << 10, name="WriteFullArrayOnly")
    NO_SUB_DATA_TYPES = o6.bitmask(0x01 << 11, name="NoSubDataTypes")
    NON_VOLATILE = o6.bitmask(0x01 << 12, name="NonVolatile")
    CONSTANT = o6.bitmask(0x01 << 13, name="Constant")


@o6.datatype(nodeId="i=15434", browseName="BaseConfigurationDataType", defaultEncodingId="i=16538", isAbstract=True)
class BaseConfigurationDataType(Structure):
    configurationVersion: o6.UInt32 = o6.field(name="ConfigurationVersion")
    configurationProperties: list[KeyValuePair] = o6.field(name="ConfigurationProperties")


@o6.datatype(nodeId="i=15435", browseName="BaseConfigurationRecordDataType", defaultEncodingId="i=16539", isAbstract=True)
class BaseConfigurationRecordDataType(Structure):
    name: o6.String = o6.field(name="Name")
    recordProperties: list[KeyValuePair] = o6.field(name="RecordProperties")


@o6.datatype(nodeId="i=15487", browseName="StructureDescription", defaultEncodingId="i=126")
class StructureDescription(DataTypeDescription):
    dataTypeId: o6.NodeId = o6.field(name="DataTypeId")
    name: o6.QualifiedName = o6.field(name="Name")
    structureDefinition: StructureDefinition = o6.field(name="StructureDefinition")


@o6.datatype(nodeId="i=15488", browseName="EnumDescription", defaultEncodingId="i=127")
class EnumDescription(DataTypeDescription):
    dataTypeId: o6.NodeId = o6.field(name="DataTypeId")
    name: o6.QualifiedName = o6.field(name="Name")
    enumDefinition: EnumDefinition = o6.field(name="EnumDefinition")
    builtInType: o6.Byte = o6.field(name="BuiltInType")


@o6.datatype(nodeId="i=15502", browseName="NetworkAddressDataType", defaultEncodingId="i=21151", isAbstract=True)
class NetworkAddressDataType(Structure):
    networkInterface: o6.String = o6.field(name="NetworkInterface")


@o6.datatype(nodeId="i=15510", browseName="NetworkAddressUrlDataType", defaultEncodingId="i=21152")
class NetworkAddressUrlDataType(NetworkAddressDataType):
    networkInterface: o6.String = o6.field(name="NetworkInterface")
    url: o6.String = o6.field(name="Url")


@o6.datatype(nodeId="i=15528", browseName="EndpointType", defaultEncodingId="i=15671")
class EndpointType(Structure):
    endpointUrl: o6.String = o6.field(name="EndpointUrl")
    securityMode: MessageSecurityMode = o6.field(name="SecurityMode")
    securityPolicyUri: o6.String = o6.field(name="SecurityPolicyUri")
    transportProfileUri: o6.String = o6.field(name="TransportProfileUri")


@o6.datatype(nodeId="i=15534", browseName="DataTypeSchemaHeader", defaultEncodingId="i=15676", isAbstract=True)
class DataTypeSchemaHeader(Structure):
    namespaces: list[o6.String] = o6.field(name="Namespaces")
    structureDataTypes: list[StructureDescription] = o6.field(name="StructureDataTypes")
    enumDataTypes: list[EnumDescription] = o6.field(name="EnumDataTypes")
    simpleDataTypes: list[SimpleTypeDescription] = o6.field(name="SimpleDataTypes")


@o6.datatype(nodeId="i=15006", browseName="UABinaryFileDataType", defaultEncodingId="i=15422")
class UABinaryFileDataType(DataTypeSchemaHeader):
    namespaces: list[o6.String] = o6.field(name="Namespaces")
    structureDataTypes: list[StructureDescription] = o6.field(name="StructureDataTypes")
    enumDataTypes: list[EnumDescription] = o6.field(name="EnumDataTypes")
    simpleDataTypes: list[SimpleTypeDescription] = o6.field(name="SimpleDataTypes")
    schemaLocation: o6.String = o6.field(name="SchemaLocation")
    fileHeader: list[KeyValuePair] = o6.field(name="FileHeader")
    body: Any = o6.field(name="Body")


@o6.enumtype(nodeId="i=15539", browseName="ConfigurationUpdateType")
class ConfigurationUpdateType(Enumeration):
    INSERT = o6.enumfield(1, name="Insert")
    REPLACE = o6.enumfield(2, name="Replace")
    INSERT_OR_REPLACE = o6.enumfield(3, name="InsertOrReplace")
    DELETE = o6.enumfield(4, name="Delete")


@o6.datatype(nodeId="i=15538", browseName="ConfigurationUpdateTargetType", defaultEncodingId="i=16541")
class ConfigurationUpdateTargetType(Structure):
    path: o6.String = o6.field(name="Path")
    updateType: ConfigurationUpdateType = o6.field(name="UpdateType")


@o6.datatype(nodeId="i=15556", browseName="ApplicationIdentityDataType", defaultEncodingId="i=16543")
class ApplicationIdentityDataType(BaseConfigurationRecordDataType):
    name: o6.String = o6.field(name="Name")
    recordProperties: list[KeyValuePair] = o6.field(name="RecordProperties")
    applicationUri: o6.String = o6.field(name="ApplicationUri")
    applicationNames: list[o6.LocalizedText] = o6.field(name="ApplicationNames")
    additionalServers: list[ApplicationDescription] = o6.field(name="AdditionalServers")


@o6.datatype(nodeId="i=15557", browseName="EndpointDataType", defaultEncodingId="i=16544")
class EndpointDataType(BaseConfigurationRecordDataType):
    name: o6.String = o6.field(name="Name")
    recordProperties: list[KeyValuePair] = o6.field(name="RecordProperties")
    discoveryUrls: list[o6.String] = o6.field(name="DiscoveryUrls")
    networkName: o6.String = o6.field(name="NetworkName")
    port: o6.UInt16 = o6.field(name="Port")


@o6.datatype(nodeId="i=15558", browseName="ServerEndpointDataType", defaultEncodingId="i=16545")
class ServerEndpointDataType(EndpointDataType):
    name: o6.String = o6.field(name="Name")
    recordProperties: list[KeyValuePair] = o6.field(name="RecordProperties")
    discoveryUrls: list[o6.String] = o6.field(name="DiscoveryUrls")
    networkName: o6.String = o6.field(name="NetworkName")
    port: o6.UInt16 = o6.field(name="Port")
    endpointUrls: list[o6.String] = o6.field(name="EndpointUrls")
    securitySettingNames: list[o6.String] = o6.field(name="SecuritySettingNames")
    transportProfileUri: o6.String = o6.field(name="TransportProfileUri")
    userTokenSettingNames: list[o6.String] = o6.field(name="UserTokenSettingNames")
    reverseConnectUrls: list[o6.String] = o6.field(name="ReverseConnectUrls")


@o6.datatype(nodeId="i=15559", browseName="SecuritySettingsDataType", defaultEncodingId="i=16546")
class SecuritySettingsDataType(BaseConfigurationRecordDataType):
    name: o6.String = o6.field(name="Name")
    recordProperties: list[KeyValuePair] = o6.field(name="RecordProperties")
    securityModes: list[MessageSecurityMode] = o6.field(name="SecurityModes")
    securityPolicyUris: list[o6.String] = o6.field(name="SecurityPolicyUris")
    certificateGroupName: o6.String = o6.field(name="CertificateGroupName")


@o6.datatype(nodeId="i=15560", browseName="UserTokenSettingsDataType", defaultEncodingId="i=16547")
class UserTokenSettingsDataType(BaseConfigurationRecordDataType):
    name: o6.String = o6.field(name="Name")
    recordProperties: list[KeyValuePair] = o6.field(name="RecordProperties")
    tokenType: UserTokenType = o6.field(name="TokenType")
    issuedTokenType: o6.String = o6.field(name="IssuedTokenType")
    issuerEndpointUrl: o6.String = o6.field(name="IssuerEndpointUrl")
    securityPolicyUri: o6.String = o6.field(name="SecurityPolicyUri")
    certificateGroupName: o6.String = o6.field(name="CertificateGroupName")
    authorizationServiceName: o6.String = o6.field(name="AuthorizationServiceName")


@o6.datatype(nodeId="i=15580", browseName="PublishedDataSetSourceDataType", defaultEncodingId="i=15678", isAbstract=True)
class PublishedDataSetSourceDataType(Structure):
    pass


@o6.datatype(nodeId="i=15581", browseName="PublishedDataItemsDataType", defaultEncodingId="i=15679")
class PublishedDataItemsDataType(PublishedDataSetSourceDataType):
    publishedData: list[PublishedVariableDataType] = o6.field(name="PublishedData")


@o6.datatype(nodeId="i=15582", browseName="PublishedEventsDataType", defaultEncodingId="i=15681")
class PublishedEventsDataType(PublishedDataSetSourceDataType):
    eventNotifier: o6.NodeId = o6.field(name="EventNotifier")
    selectedFields: list[SimpleAttributeOperand] = o6.field(name="SelectedFields")
    filter: ContentFilter = o6.field(name="Filter")


@o6.optionsettype(nodeId="i=15583", browseName="DataSetFieldContentMask", base=o6.UInt32)
class DataSetFieldContentMask:
    STATUS_CODE = o6.bitmask(0x01 << 0, name="StatusCode")
    SOURCE_TIMESTAMP = o6.bitmask(0x01 << 1, name="SourceTimestamp")
    SERVER_TIMESTAMP = o6.bitmask(0x01 << 2, name="ServerTimestamp")
    SOURCE_PICO_SECONDS = o6.bitmask(0x01 << 3, name="SourcePicoSeconds")
    SERVER_PICO_SECONDS = o6.bitmask(0x01 << 4, name="ServerPicoSeconds")
    RAW_DATA = o6.bitmask(0x01 << 5, name="RawData")


@o6.datatype(nodeId="i=15598", browseName="DataSetWriterTransportDataType", defaultEncodingId="i=15683", isAbstract=True)
class DataSetWriterTransportDataType(Structure):
    pass


@o6.datatype(nodeId="i=15605", browseName="DataSetWriterMessageDataType", defaultEncodingId="i=15688", isAbstract=True)
class DataSetWriterMessageDataType(Structure):
    pass


@o6.datatype(nodeId="i=15597", browseName="DataSetWriterDataType", defaultEncodingId="i=15682")
class DataSetWriterDataType(Structure):
    name: o6.String = o6.field(name="Name")
    enabled: o6.Boolean = o6.field(name="Enabled")
    dataSetWriterId: o6.UInt16 = o6.field(name="DataSetWriterId")
    dataSetFieldContentMask: DataSetFieldContentMask = o6.field(name="DataSetFieldContentMask")
    keyFrameCount: o6.UInt32 = o6.field(name="KeyFrameCount")
    dataSetName: o6.String = o6.field(name="DataSetName")
    dataSetWriterProperties: list[KeyValuePair] = o6.field(name="DataSetWriterProperties")
    transportSettings: DataSetWriterTransportDataType = o6.field(name="TransportSettings")
    messageSettings: DataSetWriterMessageDataType = o6.field(name="MessageSettings")


@o6.datatype(nodeId="i=15609", browseName="PubSubGroupDataType", defaultEncodingId="i=15689", isAbstract=True)
class PubSubGroupDataType(Structure):
    name: o6.String = o6.field(name="Name")
    enabled: o6.Boolean = o6.field(name="Enabled")
    securityMode: MessageSecurityMode = o6.field(name="SecurityMode")
    securityGroupId: o6.String = o6.field(name="SecurityGroupId")
    securityKeyServices: list[EndpointDescription] = o6.field(name="SecurityKeyServices")
    maxNetworkMessageSize: o6.UInt32 = o6.field(name="MaxNetworkMessageSize")
    groupProperties: list[KeyValuePair] = o6.field(name="GroupProperties")


@o6.datatype(nodeId="i=15611", browseName="WriterGroupTransportDataType", defaultEncodingId="i=15691", isAbstract=True)
class WriterGroupTransportDataType(Structure):
    pass


@o6.datatype(nodeId="i=15532", browseName="DatagramWriterGroupTransportDataType", defaultEncodingId="i=21155")
class DatagramWriterGroupTransportDataType(WriterGroupTransportDataType):
    messageRepeatCount: o6.Byte = o6.field(name="MessageRepeatCount")
    messageRepeatDelay: o6.Double = o6.field(name="MessageRepeatDelay")


@o6.datatype(nodeId="i=15616", browseName="WriterGroupMessageDataType", defaultEncodingId="i=15693", isAbstract=True)
class WriterGroupMessageDataType(Structure):
    pass


@o6.datatype(nodeId="i=15480", browseName="WriterGroupDataType", defaultEncodingId="i=21150")
class WriterGroupDataType(PubSubGroupDataType):
    name: o6.String = o6.field(name="Name")
    enabled: o6.Boolean = o6.field(name="Enabled")
    securityMode: MessageSecurityMode = o6.field(name="SecurityMode")
    securityGroupId: o6.String = o6.field(name="SecurityGroupId")
    securityKeyServices: list[EndpointDescription] = o6.field(name="SecurityKeyServices")
    maxNetworkMessageSize: o6.UInt32 = o6.field(name="MaxNetworkMessageSize")
    groupProperties: list[KeyValuePair] = o6.field(name="GroupProperties")
    writerGroupId: o6.UInt16 = o6.field(name="WriterGroupId")
    publishingInterval: o6.Double = o6.field(name="PublishingInterval")
    keepAliveTime: o6.Double = o6.field(name="KeepAliveTime")
    priority: o6.Byte = o6.field(name="Priority")
    localeIds: list[o6.String] = o6.field(name="LocaleIds")
    headerLayoutUri: o6.String = o6.field(name="HeaderLayoutUri")
    transportSettings: WriterGroupTransportDataType = o6.field(name="TransportSettings")
    messageSettings: WriterGroupMessageDataType = o6.field(name="MessageSettings")
    dataSetWriters: list[DataSetWriterDataType] = o6.field(name="DataSetWriters")


@o6.datatype(nodeId="i=15618", browseName="ConnectionTransportDataType", defaultEncodingId="i=15695", isAbstract=True)
class ConnectionTransportDataType(Structure):
    pass


@o6.datatype(nodeId="i=15007", browseName="BrokerConnectionTransportDataType", defaultEncodingId="i=15479")
class BrokerConnectionTransportDataType(ConnectionTransportDataType):
    resourceUri: o6.String = o6.field(name="ResourceUri")
    authenticationProfileUri: o6.String = o6.field(name="AuthenticationProfileUri")


@o6.datatype(nodeId="i=15621", browseName="ReaderGroupTransportDataType", defaultEncodingId="i=15701", isAbstract=True)
class ReaderGroupTransportDataType(Structure):
    pass


@o6.datatype(nodeId="i=15622", browseName="ReaderGroupMessageDataType", defaultEncodingId="i=15702", isAbstract=True)
class ReaderGroupMessageDataType(Structure):
    pass


@o6.datatype(nodeId="i=15628", browseName="DataSetReaderTransportDataType", defaultEncodingId="i=15705", isAbstract=True)
class DataSetReaderTransportDataType(Structure):
    pass


@o6.datatype(nodeId="i=15629", browseName="DataSetReaderMessageDataType", defaultEncodingId="i=15706", isAbstract=True)
class DataSetReaderMessageDataType(Structure):
    pass


@o6.datatype(nodeId="i=15630", browseName="SubscribedDataSetDataType", defaultEncodingId="i=15707", isAbstract=True)
class SubscribedDataSetDataType(Structure):
    pass


@o6.enumtype(nodeId="i=15632", browseName="IdentityCriteriaType")
class IdentityCriteriaType(Enumeration):
    USER_NAME = o6.enumfield(1, name="UserName")
    THUMBPRINT = o6.enumfield(2, name="Thumbprint")
    ROLE = o6.enumfield(3, name="Role")
    GROUP_ID = o6.enumfield(4, name="GroupId")
    ANONYMOUS = o6.enumfield(5, name="Anonymous")
    AUTHENTICATED_USER = o6.enumfield(6, name="AuthenticatedUser")
    APPLICATION = o6.enumfield(7, name="Application")
    X509_SUBJECT = o6.enumfield(8, name="X509Subject")
    TRUSTED_APPLICATION = o6.enumfield(9, name="TrustedApplication")


@o6.datatype(nodeId="i=15634", browseName="IdentityMappingRuleType", defaultEncodingId="i=15736")
class IdentityMappingRuleType(Structure):
    criteriaType: IdentityCriteriaType = o6.field(name="CriteriaType")
    criteria: o6.String = o6.field(name="Criteria")


@o6.datatype(nodeId="i=15635", browseName="SubscribedDataSetMirrorDataType", defaultEncodingId="i=15713")
class SubscribedDataSetMirrorDataType(SubscribedDataSetDataType):
    parentNodeName: o6.String = o6.field(name="ParentNodeName")
    rolePermissions: list[RolePermissionType] = o6.field(name="RolePermissions")


@o6.optionsettype(nodeId="i=15642", browseName="UadpNetworkMessageContentMask", base=o6.UInt32)
class UadpNetworkMessageContentMask:
    PUBLISHER_ID = o6.bitmask(0x01 << 0, name="PublisherId")
    GROUP_HEADER = o6.bitmask(0x01 << 1, name="GroupHeader")
    WRITER_GROUP_ID = o6.bitmask(0x01 << 2, name="WriterGroupId")
    GROUP_VERSION = o6.bitmask(0x01 << 3, name="GroupVersion")
    NETWORK_MESSAGE_NUMBER = o6.bitmask(0x01 << 4, name="NetworkMessageNumber")
    SEQUENCE_NUMBER = o6.bitmask(0x01 << 5, name="SequenceNumber")
    PAYLOAD_HEADER = o6.bitmask(0x01 << 6, name="PayloadHeader")
    TIMESTAMP = o6.bitmask(0x01 << 7, name="Timestamp")
    PICO_SECONDS = o6.bitmask(0x01 << 8, name="PicoSeconds")
    DATA_SET_CLASS_ID = o6.bitmask(0x01 << 9, name="DataSetClassId")
    PROMOTED_FIELDS = o6.bitmask(0x01 << 10, name="PromotedFields")


@o6.optionsettype(nodeId="i=15646", browseName="UadpDataSetMessageContentMask", base=o6.UInt32)
class UadpDataSetMessageContentMask:
    TIMESTAMP = o6.bitmask(0x01 << 0, name="Timestamp")
    PICO_SECONDS = o6.bitmask(0x01 << 1, name="PicoSeconds")
    STATUS = o6.bitmask(0x01 << 2, name="Status")
    MAJOR_VERSION = o6.bitmask(0x01 << 3, name="MajorVersion")
    MINOR_VERSION = o6.bitmask(0x01 << 4, name="MinorVersion")
    SEQUENCE_NUMBER = o6.bitmask(0x01 << 5, name="SequenceNumber")


@o6.datatype(nodeId="i=15652", browseName="UadpDataSetWriterMessageDataType", defaultEncodingId="i=15717")
class UadpDataSetWriterMessageDataType(DataSetWriterMessageDataType):
    dataSetMessageContentMask: UadpDataSetMessageContentMask = o6.field(name="DataSetMessageContentMask")
    configuredSize: o6.UInt16 = o6.field(name="ConfiguredSize")
    networkMessageNumber: o6.UInt16 = o6.field(name="NetworkMessageNumber")
    dataSetOffset: o6.UInt16 = o6.field(name="DataSetOffset")


@o6.datatype(nodeId="i=15653", browseName="UadpDataSetReaderMessageDataType", defaultEncodingId="i=15718")
class UadpDataSetReaderMessageDataType(DataSetReaderMessageDataType):
    groupVersion: o6.UInt32 = o6.field(name="GroupVersion")
    networkMessageNumber: o6.UInt16 = o6.field(name="NetworkMessageNumber")
    dataSetOffset: o6.UInt16 = o6.field(name="DataSetOffset")
    dataSetClassId: o6.Guid = o6.field(name="DataSetClassId")
    networkMessageContentMask: UadpNetworkMessageContentMask = o6.field(name="NetworkMessageContentMask")
    dataSetMessageContentMask: UadpDataSetMessageContentMask = o6.field(name="DataSetMessageContentMask")
    publishingInterval: o6.Double = o6.field(name="PublishingInterval")
    receiveOffset: o6.Double = o6.field(name="ReceiveOffset")
    processingOffset: o6.Double = o6.field(name="ProcessingOffset")


@o6.optionsettype(nodeId="i=15654", browseName="JsonNetworkMessageContentMask", base=o6.UInt32)
class JsonNetworkMessageContentMask:
    NETWORK_MESSAGE_HEADER = o6.bitmask(0x01 << 0, name="NetworkMessageHeader")
    DATA_SET_MESSAGE_HEADER = o6.bitmask(0x01 << 1, name="DataSetMessageHeader")
    SINGLE_DATA_SET_MESSAGE = o6.bitmask(0x01 << 2, name="SingleDataSetMessage")
    PUBLISHER_ID = o6.bitmask(0x01 << 3, name="PublisherId")
    DATA_SET_CLASS_ID = o6.bitmask(0x01 << 4, name="DataSetClassId")
    REPLY_TO = o6.bitmask(0x01 << 5, name="ReplyTo")
    WRITER_GROUP_NAME = o6.bitmask(0x01 << 6, name="WriterGroupName")


@o6.datatype(nodeId="i=15657", browseName="JsonWriterGroupMessageDataType", defaultEncodingId="i=15719")
class JsonWriterGroupMessageDataType(WriterGroupMessageDataType):
    networkMessageContentMask: JsonNetworkMessageContentMask = o6.field(name="NetworkMessageContentMask")


@o6.optionsettype(nodeId="i=15658", browseName="JsonDataSetMessageContentMask", base=o6.UInt32)
class JsonDataSetMessageContentMask:
    DATA_SET_WRITER_ID = o6.bitmask(0x01 << 0, name="DataSetWriterId")
    META_DATA_VERSION = o6.bitmask(0x01 << 1, name="MetaDataVersion")
    SEQUENCE_NUMBER = o6.bitmask(0x01 << 2, name="SequenceNumber")
    TIMESTAMP = o6.bitmask(0x01 << 3, name="Timestamp")
    STATUS = o6.bitmask(0x01 << 4, name="Status")
    MESSAGE_TYPE = o6.bitmask(0x01 << 5, name="MessageType")
    DATA_SET_WRITER_NAME = o6.bitmask(0x01 << 6, name="DataSetWriterName")
    FIELD_ENCODING1 = o6.bitmask(0x01 << 7, name="FieldEncoding1")
    PUBLISHER_ID = o6.bitmask(0x01 << 8, name="PublisherId")
    WRITER_GROUP_NAME = o6.bitmask(0x01 << 9, name="WriterGroupName")
    MINOR_VERSION = o6.bitmask(0x01 << 10, name="MinorVersion")
    FIELD_ENCODING2 = o6.bitmask(0x01 << 11, name="FieldEncoding2")


@o6.datatype(nodeId="i=15664", browseName="JsonDataSetWriterMessageDataType", defaultEncodingId="i=15724")
class JsonDataSetWriterMessageDataType(DataSetWriterMessageDataType):
    dataSetMessageContentMask: JsonDataSetMessageContentMask = o6.field(name="DataSetMessageContentMask")


@o6.datatype(nodeId="i=15665", browseName="JsonDataSetReaderMessageDataType", defaultEncodingId="i=15725")
class JsonDataSetReaderMessageDataType(DataSetReaderMessageDataType):
    networkMessageContentMask: JsonNetworkMessageContentMask = o6.field(name="NetworkMessageContentMask")
    dataSetMessageContentMask: JsonDataSetMessageContentMask = o6.field(name="DataSetMessageContentMask")


@o6.datatype(nodeId="i=15667", browseName="BrokerWriterGroupTransportDataType", defaultEncodingId="i=15727")
class BrokerWriterGroupTransportDataType(WriterGroupTransportDataType):
    queueName: o6.String = o6.field(name="QueueName")
    resourceUri: o6.String = o6.field(name="ResourceUri")
    authenticationProfileUri: o6.String = o6.field(name="AuthenticationProfileUri")
    requestedDeliveryGuarantee: BrokerTransportQualityOfService = o6.field(name="RequestedDeliveryGuarantee")


@o6.datatype(nodeId="i=15669", browseName="BrokerDataSetWriterTransportDataType", defaultEncodingId="i=15729")
class BrokerDataSetWriterTransportDataType(DataSetWriterTransportDataType):
    queueName: o6.String = o6.field(name="QueueName")
    resourceUri: o6.String = o6.field(name="ResourceUri")
    authenticationProfileUri: o6.String = o6.field(name="AuthenticationProfileUri")
    requestedDeliveryGuarantee: BrokerTransportQualityOfService = o6.field(name="RequestedDeliveryGuarantee")
    metaDataQueueName: o6.String = o6.field(name="MetaDataQueueName")
    metaDataUpdateTime: o6.Double = o6.field(name="MetaDataUpdateTime")


@o6.datatype(nodeId="i=15670", browseName="BrokerDataSetReaderTransportDataType", defaultEncodingId="i=15733")
class BrokerDataSetReaderTransportDataType(DataSetReaderTransportDataType):
    queueName: o6.String = o6.field(name="QueueName")
    resourceUri: o6.String = o6.field(name="ResourceUri")
    authenticationProfileUri: o6.String = o6.field(name="AuthenticationProfileUri")
    requestedDeliveryGuarantee: BrokerTransportQualityOfService = o6.field(name="RequestedDeliveryGuarantee")
    metaDataQueueName: o6.String = o6.field(name="MetaDataQueueName")


@o6.enumtype(nodeId="i=15874", browseName="OverrideValueHandling")
class OverrideValueHandling(Enumeration):
    DISABLED = o6.enumfield(0, name="Disabled")
    LAST_USABLE_VALUE = o6.enumfield(1, name="LastUsableValue")
    OVERRIDE_VALUE = o6.enumfield(2, name="OverrideValue")


@o6.datatype(nodeId="i=14744", browseName="FieldTargetDataType", defaultEncodingId="i=14848")
class FieldTargetDataType(Structure):
    dataSetFieldId: o6.Guid = o6.field(name="DataSetFieldId")
    receiverIndexRange: o6.String = o6.field(name="ReceiverIndexRange")
    targetNodeId: o6.NodeId = o6.field(name="TargetNodeId")
    attributeId: o6.UInt32 = o6.field(name="AttributeId")
    writeIndexRange: o6.String = o6.field(name="WriteIndexRange")
    overrideValueHandling: OverrideValueHandling = o6.field(name="OverrideValueHandling")
    overrideValue: Any = o6.field(name="OverrideValue")


@o6.datatype(nodeId="i=15631", browseName="TargetVariablesDataType", defaultEncodingId="i=15712")
class TargetVariablesDataType(SubscribedDataSetDataType):
    targetVariables: list[FieldTargetDataType] = o6.field(name="TargetVariables")


@o6.datatype(nodeId="i=15901", browseName="SessionlessInvokeRequestType", defaultEncodingId="i=15903")
class SessionlessInvokeRequestType(Structure):
    urisVersion: o6.UInt32 = o6.field(name="UrisVersion")
    namespaceUris: list[o6.String] = o6.field(name="NamespaceUris")
    serverUris: list[o6.String] = o6.field(name="ServerUris")
    localeIds: list[o6.String] = o6.field(name="LocaleIds")
    serviceId: o6.UInt32 = o6.field(name="ServiceId")


@o6.optionsettype(nodeId="i=15904", browseName="DataSetFieldFlags", base=o6.UInt16)
class DataSetFieldFlags:
    PROMOTED_FIELD = o6.bitmask(0x01 << 0, name="PromotedField")


@o6.datatype(nodeId="i=14524", browseName="FieldMetaData", defaultEncodingId="i=14839")
class FieldMetaData(Structure):
    name: o6.String = o6.field(name="Name")
    description: o6.LocalizedText = o6.field(name="Description")
    fieldFlags: DataSetFieldFlags = o6.field(name="FieldFlags")
    builtInType: o6.Byte = o6.field(name="BuiltInType")
    dataType: o6.NodeId = o6.field(name="DataType")
    valueRank: o6.Int32 = o6.field(name="ValueRank")
    arrayDimensions: list[o6.UInt32] = o6.field(name="ArrayDimensions")
    maxStringLength: o6.UInt32 = o6.field(name="MaxStringLength")
    dataSetFieldId: o6.Guid = o6.field(name="DataSetFieldId")
    properties: list[KeyValuePair] = o6.field(name="Properties")


@o6.datatype(nodeId="i=14523", browseName="DataSetMetaDataType", defaultEncodingId="i=124")
class DataSetMetaDataType(DataTypeSchemaHeader):
    namespaces: list[o6.String] = o6.field(name="Namespaces")
    structureDataTypes: list[StructureDescription] = o6.field(name="StructureDataTypes")
    enumDataTypes: list[EnumDescription] = o6.field(name="EnumDataTypes")
    simpleDataTypes: list[SimpleTypeDescription] = o6.field(name="SimpleDataTypes")
    name: o6.String = o6.field(name="Name")
    description: o6.LocalizedText = o6.field(name="Description")
    fields: list[FieldMetaData] = o6.field(name="Fields")
    dataSetClassId: o6.Guid = o6.field(name="DataSetClassId")
    configurationVersion: ConfigurationVersionDataType = o6.field(name="ConfigurationVersion")


@o6.datatype(nodeId="i=15578", browseName="PublishedDataSetDataType", defaultEncodingId="i=15677")
class PublishedDataSetDataType(Structure):
    name: o6.String = o6.field(name="Name")
    dataSetFolder: list[o6.String] = o6.field(name="DataSetFolder")
    dataSetMetaData: DataSetMetaDataType = o6.field(name="DataSetMetaData")
    extensionFields: list[KeyValuePair] = o6.field(name="ExtensionFields")
    dataSetSource: PublishedDataSetSourceDataType = o6.field(name="DataSetSource")


@o6.datatype(nodeId="i=15623", browseName="DataSetReaderDataType", defaultEncodingId="i=15703")
class DataSetReaderDataType(Structure):
    name: o6.String = o6.field(name="Name")
    enabled: o6.Boolean = o6.field(name="Enabled")
    publisherId: Any = o6.field(name="PublisherId")
    writerGroupId: o6.UInt16 = o6.field(name="WriterGroupId")
    dataSetWriterId: o6.UInt16 = o6.field(name="DataSetWriterId")
    dataSetMetaData: DataSetMetaDataType = o6.field(name="DataSetMetaData")
    dataSetFieldContentMask: DataSetFieldContentMask = o6.field(name="DataSetFieldContentMask")
    messageReceiveTimeout: o6.Double = o6.field(name="MessageReceiveTimeout")
    keyFrameCount: o6.UInt32 = o6.field(name="KeyFrameCount")
    headerLayoutUri: o6.String = o6.field(name="HeaderLayoutUri")
    securityMode: MessageSecurityMode = o6.field(name="SecurityMode")
    securityGroupId: o6.String = o6.field(name="SecurityGroupId")
    securityKeyServices: list[EndpointDescription] = o6.field(name="SecurityKeyServices")
    dataSetReaderProperties: list[KeyValuePair] = o6.field(name="DataSetReaderProperties")
    transportSettings: DataSetReaderTransportDataType = o6.field(name="TransportSettings")
    messageSettings: DataSetReaderMessageDataType = o6.field(name="MessageSettings")
    subscribedDataSet: SubscribedDataSetDataType = o6.field(name="SubscribedDataSet")


@o6.datatype(nodeId="i=15520", browseName="ReaderGroupDataType", defaultEncodingId="i=21153")
class ReaderGroupDataType(PubSubGroupDataType):
    name: o6.String = o6.field(name="Name")
    enabled: o6.Boolean = o6.field(name="Enabled")
    securityMode: MessageSecurityMode = o6.field(name="SecurityMode")
    securityGroupId: o6.String = o6.field(name="SecurityGroupId")
    securityKeyServices: list[EndpointDescription] = o6.field(name="SecurityKeyServices")
    maxNetworkMessageSize: o6.UInt32 = o6.field(name="MaxNetworkMessageSize")
    groupProperties: list[KeyValuePair] = o6.field(name="GroupProperties")
    transportSettings: ReaderGroupTransportDataType = o6.field(name="TransportSettings")
    messageSettings: ReaderGroupMessageDataType = o6.field(name="MessageSettings")
    dataSetReaders: list[DataSetReaderDataType] = o6.field(name="DataSetReaders")


@o6.datatype(nodeId="i=15617", browseName="PubSubConnectionDataType", defaultEncodingId="i=15694")
class PubSubConnectionDataType(Structure):
    name: o6.String = o6.field(name="Name")
    enabled: o6.Boolean = o6.field(name="Enabled")
    publisherId: Any = o6.field(name="PublisherId")
    transportProfileUri: o6.String = o6.field(name="TransportProfileUri")
    address: NetworkAddressDataType = o6.field(name="Address")
    connectionProperties: list[KeyValuePair] = o6.field(name="ConnectionProperties")
    transportSettings: ConnectionTransportDataType = o6.field(name="TransportSettings")
    writerGroups: list[WriterGroupDataType] = o6.field(name="WriterGroups")
    readerGroups: list[ReaderGroupDataType] = o6.field(name="ReaderGroups")


@o6.datatype(nodeId="i=15530", browseName="PubSubConfigurationDataType", defaultEncodingId="i=21154")
class PubSubConfigurationDataType(Structure):
    publishedDataSets: list[PublishedDataSetDataType] = o6.field(name="PublishedDataSets")
    connections: list[PubSubConnectionDataType] = o6.field(name="Connections")
    enabled: o6.Boolean = o6.field(name="Enabled")


@o6.datatype(nodeId="i=16307", browseName="AudioDataType", parent="i=15")
class AudioDataType:
    pass


@o6.datatype(nodeId="i=16313", browseName="AdditionalParametersType", defaultEncodingId="i=17537")
class AdditionalParametersType(Structure):
    parameters: list[KeyValuePair] = o6.field(name="Parameters")


@o6.datatype(nodeId="i=17467", browseName="DatagramConnectionTransportDataType", defaultEncodingId="i=17468")
class DatagramConnectionTransportDataType(ConnectionTransportDataType):
    discoveryAddress: NetworkAddressDataType = o6.field(name="DiscoveryAddress")


@o6.datatype(nodeId="i=17545", browseName="RsaEncryptedSecret", parent="i=24")
class RsaEncryptedSecret:
    pass


@o6.datatype(nodeId="i=17546", browseName="EccEncryptedSecret", parent="i=24")
class EccEncryptedSecret:
    pass


@o6.datatype(nodeId="i=17548", browseName="EphemeralKeyType", defaultEncodingId="i=17549")
class EphemeralKeyType(Structure):
    publicKey: o6.ByteString = o6.field(name="PublicKey")
    signature: o6.ByteString = o6.field(name="Signature")


@o6.datatype(nodeId="i=17588", browseName="Index", parent="i=7")
class Index:
    pass


@o6.datatype(nodeId="i=17606", browseName="GenericAttributeValue", defaultEncodingId="i=17610")
class GenericAttributeValue(Structure):
    attributeId: o6.UInt32 = o6.field(name="AttributeId")
    value: Any = o6.field(name="Value")


@o6.datatype(nodeId="i=17607", browseName="GenericAttributes", defaultEncodingId="i=17611")
class GenericAttributes(NodeAttributes):
    specifiedAttributes: o6.UInt32 = o6.field(name="SpecifiedAttributes")
    displayName: o6.LocalizedText = o6.field(name="DisplayName")
    description: o6.LocalizedText = o6.field(name="Description")
    writeMask: o6.UInt32 = o6.field(name="WriteMask")
    userWriteMask: o6.UInt32 = o6.field(name="UserWriteMask")
    attributeValues: list[GenericAttributeValue] = o6.field(name="AttributeValues")


@o6.datatype(nodeId="i=17861", browseName="DecimalDataType", defaultEncodingId="i=17863")
class DecimalDataType(Structure):
    scale: o6.Int16 = o6.field(name="Scale")
    value: o6.ByteString = o6.field(name="Value")


@o6.datatype(nodeId="i=18593", browseName="ActionTargetDataType", defaultEncodingId="i=18598")
class ActionTargetDataType(Structure):
    actionTargetId: o6.UInt16 = o6.field(name="ActionTargetId")
    name: o6.String = o6.field(name="Name")
    description: o6.LocalizedText = o6.field(name="Description")


@o6.datatype(nodeId="i=18594", browseName="PublishedActionDataType", defaultEncodingId="i=18599")
class PublishedActionDataType(PublishedDataSetSourceDataType):
    requestDataSetMetaData: DataSetMetaDataType = o6.field(name="RequestDataSetMetaData")
    actionTargets: list[ActionTargetDataType] = o6.field(name="ActionTargets")


@o6.enumtype(nodeId="i=18595", browseName="ActionState")
class ActionState(Enumeration):
    IDLE = o6.enumfield(0, name="Idle")
    EXECUTING = o6.enumfield(1, name="Executing")
    DONE = o6.enumfield(2, name="Done")


@o6.datatype(nodeId="i=18597", browseName="ActionMethodDataType", defaultEncodingId="i=18600")
class ActionMethodDataType(Structure):
    objectId: o6.NodeId = o6.field(name="ObjectId")
    methodId: o6.NodeId = o6.field(name="MethodId")


@o6.enumtype(nodeId="i=18646", browseName="SortOrderType")
class SortOrderType(Enumeration):
    ASCENDING = o6.enumfield(0, name="Ascending")
    DESCENDING = o6.enumfield(1, name="Descending")


@o6.datatype(nodeId="i=18648", browseName="SortRuleElement", defaultEncodingId="i=18650")
class SortRuleElement(Structure):
    sortOrder: SortOrderType = o6.field(name="SortOrder")
    eventField: SimpleAttributeOperand = o6.field(name="EventField")


@o6.datatype(nodeId="i=18649", browseName="ReadEventDetailsSorted", defaultEncodingId="i=18651")
class ReadEventDetailsSorted(ReadEventDetails):
    numValuesPerNode: o6.UInt32 = o6.field(name="NumValuesPerNode")
    startTime: o6.DateTime = o6.field(name="StartTime")
    endTime: o6.DateTime = o6.field(name="EndTime")
    filter: EventFilter = o6.field(name="Filter")
    sortClause: list[SortRuleElement] = o6.field(name="SortClause")


@o6.datatype(nodeId="i=18793", browseName="PublishedActionMethodDataType", defaultEncodingId="i=18795")
class PublishedActionMethodDataType(PublishedActionDataType):
    requestDataSetMetaData: DataSetMetaDataType = o6.field(name="RequestDataSetMetaData")
    actionTargets: list[ActionTargetDataType] = o6.field(name="ActionTargets")
    actionMethods: list[ActionMethodDataType] = o6.field(name="ActionMethods")


@o6.datatype(nodeId="i=18794", browseName="DtlsPubSubConnectionDataType", defaultEncodingId="i=18930")
class DtlsPubSubConnectionDataType(Structure):
    clientCipherSuite: o6.String = o6.field(name="ClientCipherSuite")
    serverCipherSuites: list[o6.String] = o6.field(name="ServerCipherSuites")
    zeroRTT: o6.Boolean = o6.field(name="ZeroRTT")
    certificateGroupId: o6.NodeId = o6.field(name="CertificateGroupId")
    verifyClientCertificate: o6.Boolean = o6.field(name="VerifyClientCertificate")


@o6.datatype(nodeId="i=18806", browseName="RationalNumber", defaultEncodingId="i=18815")
class RationalNumber(Structure):
    numerator: o6.Int32 = o6.field(name="Numerator")
    denominator: o6.UInt32 = o6.field(name="Denominator")


@o6.datatype(nodeId="i=18807", browseName="Vector", defaultEncodingId="i=18816", isAbstract=True)
class Vector(Structure):
    pass


@o6.datatype(nodeId="i=18808", browseName="3DVector", defaultEncodingId="i=18817")
class ThreeDVector(Vector):
    x: o6.Double = o6.field(name="X")
    y: o6.Double = o6.field(name="Y")
    z: o6.Double = o6.field(name="Z")


@o6.datatype(nodeId="i=18809", browseName="CartesianCoordinates", defaultEncodingId="i=18818", isAbstract=True)
class CartesianCoordinates(Structure):
    pass


@o6.datatype(nodeId="i=18810", browseName="3DCartesianCoordinates", defaultEncodingId="i=18819")
class ThreeDCartesianCoordinates(CartesianCoordinates):
    x: o6.Double = o6.field(name="X")
    y: o6.Double = o6.field(name="Y")
    z: o6.Double = o6.field(name="Z")


@o6.datatype(nodeId="i=18811", browseName="Orientation", defaultEncodingId="i=18820", isAbstract=True)
class Orientation(Structure):
    pass


@o6.datatype(nodeId="i=18812", browseName="3DOrientation", defaultEncodingId="i=18821")
class ThreeDOrientation(Orientation):
    a: o6.Double = o6.field(name="A")
    b: o6.Double = o6.field(name="B")
    c: o6.Double = o6.field(name="C")


@o6.datatype(nodeId="i=18813", browseName="Frame", defaultEncodingId="i=18822", isAbstract=True)
class Frame(Structure):
    pass


@o6.datatype(nodeId="i=18814", browseName="3DFrame", defaultEncodingId="i=18823")
class ThreeDFrame(Frame):
    cartesianCoordinates: ThreeDCartesianCoordinates = o6.field(name="CartesianCoordinates")
    orientation: ThreeDOrientation = o6.field(name="Orientation")


@o6.enumtype(nodeId="i=18947", browseName="ChassisIdSubtype")
class ChassisIdSubtype(Enumeration):
    CHASSIS_COMPONENT = o6.enumfield(1, name="ChassisComponent")
    INTERFACE_ALIAS = o6.enumfield(2, name="InterfaceAlias")
    PORT_COMPONENT = o6.enumfield(3, name="PortComponent")
    MAC_ADDRESS = o6.enumfield(4, name="MacAddress")
    NETWORK_ADDRESS = o6.enumfield(5, name="NetworkAddress")
    INTERFACE_NAME = o6.enumfield(6, name="InterfaceName")
    LOCAL = o6.enumfield(7, name="Local")


@o6.enumtype(nodeId="i=18949", browseName="PortIdSubtype")
class PortIdSubtype(Enumeration):
    INTERFACE_ALIAS = o6.enumfield(1, name="InterfaceAlias")
    PORT_COMPONENT = o6.enumfield(2, name="PortComponent")
    MAC_ADDRESS = o6.enumfield(3, name="MacAddress")
    NETWORK_ADDRESS = o6.enumfield(4, name="NetworkAddress")
    INTERFACE_NAME = o6.enumfield(5, name="InterfaceName")
    AGENT_CIRCUIT_ID = o6.enumfield(6, name="AgentCircuitId")
    LOCAL = o6.enumfield(7, name="Local")


@o6.enumtype(nodeId="i=18951", browseName="ManAddrIfSubtype")
class ManAddrIfSubtype(Enumeration):
    NONE = o6.enumfield(0, name="None")
    UNKNOWN = o6.enumfield(1, name="Unknown")
    PORT_REF = o6.enumfield(2, name="PortRef")
    SYSTEM_PORT_NUMBER = o6.enumfield(3, name="SystemPortNumber")


@o6.datatype(nodeId="i=18953", browseName="LldpManagementAddressTxPortType", defaultEncodingId="i=19079")
class LldpManagementAddressTxPortType(Structure):
    addressSubtype: o6.UInt32 = o6.field(name="AddressSubtype")
    manAddress: o6.String = o6.field(name="ManAddress")
    txEnable: o6.Boolean = o6.field(name="TxEnable")
    addrLen: o6.UInt32 = o6.field(name="AddrLen")
    ifSubtype: ManAddrIfSubtype = o6.field(name="IfSubtype")
    ifId: o6.UInt32 = o6.field(name="IfId")


@o6.datatype(nodeId="i=18954", browseName="LldpManagementAddressType", defaultEncodingId="i=19080")
class LldpManagementAddressType(Structure):
    addressSubtype: o6.UInt32 = o6.field(name="AddressSubtype")
    address: o6.String = o6.field(name="Address")
    ifSubtype: ManAddrIfSubtype = o6.field(name="IfSubtype")
    ifId: o6.UInt32 = o6.field(name="IfId")


@o6.datatype(nodeId="i=18955", browseName="LldpTlvType", defaultEncodingId="i=19081")
class LldpTlvType(Structure):
    tlvType: o6.UInt32 = o6.field(name="TlvType")
    tlvInfo: o6.ByteString = o6.field(name="TlvInfo")


@o6.optionsettype(nodeId="i=18956", browseName="LldpSystemCapabilitiesMap", base=o6.UInt32)
class LldpSystemCapabilitiesMap:
    OTHER = o6.bitmask(0x01 << 0, name="Other")
    REPEATER = o6.bitmask(0x01 << 1, name="Repeater")
    BRIDGE = o6.bitmask(0x01 << 2, name="Bridge")
    WLAN_ACCESS_POINT = o6.bitmask(0x01 << 3, name="WlanAccessPoint")
    ROUTER = o6.bitmask(0x01 << 4, name="Router")
    TELEPHONE = o6.bitmask(0x01 << 5, name="Telephone")
    DOCSIS_CABLE_DEVICE = o6.bitmask(0x01 << 6, name="DocsisCableDevice")
    STATION_ONLY = o6.bitmask(0x01 << 7, name="StationOnly")
    CVLAN_COMPONENT = o6.bitmask(0x01 << 8, name="CvlanComponent")
    SVLAN_COMPONENT = o6.bitmask(0x01 << 9, name="SvlanComponent")
    TWO_PORT_MAC_RELAY = o6.bitmask(0x01 << 10, name="TwoPortMacRelay")


@o6.datatype(nodeId="i=19311", browseName="JsonNetworkMessage")
class JsonNetworkMessage(Structure):
    messageId: o6.String = o6.field(name="MessageId")
    messageType: o6.String = o6.field(name="MessageType")
    publisherId: o6.String = o6.field(name="PublisherId")
    writerGroupName: o6.String = o6.field(name="WriterGroupName")
    dataSetClassId: o6.String = o6.field(name="DataSetClassId")
    messages: list[o6.ExtensionObject] = o6.field(name="Messages")


@o6.datatype(nodeId="i=19312", browseName="JsonDataSetMessage")
class JsonDataSetMessage(Structure):
    dataSetWriterId: o6.UInt16 = o6.field(name="DataSetWriterId")
    dataSetWriterName: o6.String = o6.field(name="DataSetWriterName")
    publisherId: o6.String = o6.field(name="PublisherId")
    writerGroupName: o6.String = o6.field(name="WriterGroupName")
    sequenceNumber: o6.UInt32 = o6.field(name="SequenceNumber")
    metaDataVersion: ConfigurationVersionDataType = o6.field(name="MetaDataVersion")
    minorVersion: o6.UInt32 = o6.field(name="MinorVersion")
    timestamp: o6.DateTime = o6.field(name="Timestamp")
    status: o6.StatusCode = o6.field(name="Status")
    messageType: o6.String = o6.field(name="MessageType")
    payload: o6.ExtensionObject = o6.field(name="Payload")


@o6.datatype(nodeId="i=19313", browseName="JsonDataSetMetaDataMessage")
class JsonDataSetMetaDataMessage(Structure):
    messageId: o6.String = o6.field(name="MessageId")
    messageType: o6.String = o6.field(name="MessageType")
    publisherId: o6.String = o6.field(name="PublisherId")
    dataSetWriterId: o6.UInt16 = o6.field(name="DataSetWriterId")
    writerGroupName: o6.String = o6.field(name="WriterGroupName")
    dataSetWriterName: o6.String = o6.field(name="DataSetWriterName")
    timestamp: o6.DateTime = o6.field(name="Timestamp")
    metaData: DataSetMetaDataType = o6.field(name="MetaData")


@o6.datatype(nodeId="i=19314", browseName="JsonApplicationDescriptionMessage")
class JsonApplicationDescriptionMessage(Structure):
    messageId: o6.String = o6.field(name="MessageId")
    messageType: o6.String = o6.field(name="MessageType")
    publisherId: o6.String = o6.field(name="PublisherId")
    timestamp: o6.DateTime = o6.field(name="Timestamp")
    description: ApplicationDescription = o6.field(name="Description")
    serverCapabilities: list[o6.String] = o6.field(name="ServerCapabilities")


@o6.datatype(nodeId="i=19315", browseName="JsonServerEndpointsMessage")
class JsonServerEndpointsMessage(Structure):
    messageId: o6.String = o6.field(name="MessageId")
    messageType: o6.String = o6.field(name="MessageType")
    publisherId: o6.String = o6.field(name="PublisherId")
    timestamp: o6.DateTime = o6.field(name="Timestamp")
    description: ApplicationDescription = o6.field(name="Description")
    endpoints: list[EndpointDescription] = o6.field(name="Endpoints")


@o6.datatype(nodeId="i=19316", browseName="JsonStatusMessage")
class JsonStatusMessage(Structure):
    messageId: o6.String = o6.field(name="MessageId")
    messageType: o6.String = o6.field(name="MessageType")
    publisherId: o6.String = o6.field(name="PublisherId")
    timestamp: o6.DateTime = o6.field(name="Timestamp")
    isCyclic: o6.Boolean = o6.field(name="IsCyclic")
    status: PubSubState = o6.field(name="Status")
    nextReportTime: o6.DateTime = o6.field(name="NextReportTime")


@o6.datatype(nodeId="i=19317", browseName="JsonPubSubConnectionMessage")
class JsonPubSubConnectionMessage(Structure):
    messageId: o6.String = o6.field(name="MessageId")
    messageType: o6.String = o6.field(name="MessageType")
    publisherId: o6.String = o6.field(name="PublisherId")
    timestamp: o6.DateTime = o6.field(name="Timestamp")
    connection: PubSubConnectionDataType = o6.field(name="Connection")


@o6.datatype(nodeId="i=19318", browseName="JsonActionMetaDataMessage")
class JsonActionMetaDataMessage(Structure):
    messageId: o6.String = o6.field(name="MessageId")
    messageType: o6.String = o6.field(name="MessageType")
    publisherId: o6.String = o6.field(name="PublisherId")
    dataSetWriterId: o6.UInt16 = o6.field(name="DataSetWriterId")
    dataSetWriterName: o6.String = o6.field(name="DataSetWriterName")
    timestamp: o6.DateTime = o6.field(name="Timestamp")
    actionTargets: list[ActionTargetDataType] = o6.field(name="ActionTargets")
    request: DataSetMetaDataType = o6.field(name="Request")
    response: DataSetMetaDataType = o6.field(name="Response")
    actionMethods: list[ActionMethodDataType] = o6.field(name="ActionMethods")


@o6.datatype(nodeId="i=19319", browseName="JsonActionResponderMessage")
class JsonActionResponderMessage(Structure):
    messageId: o6.String = o6.field(name="MessageId")
    messageType: o6.String = o6.field(name="MessageType")
    publisherId: o6.String = o6.field(name="PublisherId")
    timestamp: o6.DateTime = o6.field(name="Timestamp")
    connection: PubSubConnectionDataType = o6.field(name="Connection")


@o6.datatype(nodeId="i=19320", browseName="JsonActionNetworkMessage")
class JsonActionNetworkMessage(Structure):
    messageId: o6.String = o6.field(name="MessageId")
    messageType: o6.String = o6.field(name="MessageType")
    publisherId: o6.String = o6.field(name="PublisherId")
    timestamp: o6.DateTime = o6.field(name="Timestamp")
    responseAddress: o6.String = o6.field(name="ResponseAddress")
    correlationData: o6.ByteString = o6.field(name="CorrelationData")
    requestorId: o6.String = o6.field(name="RequestorId")
    timeoutHint: o6.Double = o6.field(name="TimeoutHint")
    messages: list[o6.ExtensionObject] = o6.field(name="Messages")


@o6.datatype(nodeId="i=19321", browseName="JsonActionRequestMessage")
class JsonActionRequestMessage(Structure):
    dataSetWriterId: o6.UInt16 = o6.field(name="DataSetWriterId")
    actionTargetId: o6.UInt16 = o6.field(name="ActionTargetId")
    dataSetWriterName: o6.String = o6.field(name="DataSetWriterName")
    writerGroupName: o6.String = o6.field(name="WriterGroupName")
    metaDataVersion: ConfigurationVersionDataType = o6.field(name="MetaDataVersion")
    minorVersion: o6.UInt32 = o6.field(name="MinorVersion")
    timestamp: o6.DateTime = o6.field(name="Timestamp")
    messageType: o6.String = o6.field(name="MessageType")
    requestId: o6.UInt16 = o6.field(name="RequestId")
    actionState: ActionState = o6.field(name="ActionState")
    payload: o6.ExtensionObject = o6.field(name="Payload")


@o6.datatype(nodeId="i=19322", browseName="JsonActionResponseMessage")
class JsonActionResponseMessage(Structure):
    dataSetWriterId: o6.UInt16 = o6.field(name="DataSetWriterId")
    actionTargetId: o6.UInt16 = o6.field(name="ActionTargetId")
    dataSetWriterName: o6.String = o6.field(name="DataSetWriterName")
    writerGroupName: o6.String = o6.field(name="WriterGroupName")
    metaDataVersion: ConfigurationVersionDataType = o6.field(name="MetaDataVersion")
    minorVersion: o6.UInt32 = o6.field(name="MinorVersion")
    timestamp: o6.DateTime = o6.field(name="Timestamp")
    status: o6.StatusCode = o6.field(name="Status")
    messageType: o6.String = o6.field(name="MessageType")
    requestId: o6.UInt16 = o6.field(name="RequestId")
    actionState: ActionState = o6.field(name="ActionState")
    payload: o6.ExtensionObject = o6.field(name="Payload")


@o6.enumtype(nodeId="i=19723", browseName="DiagnosticsLevel")
class DiagnosticsLevel(Enumeration):
    BASIC = o6.enumfield(0, name="Basic")
    ADVANCED = o6.enumfield(1, name="Advanced")
    INFO = o6.enumfield(2, name="Info")
    LOG = o6.enumfield(3, name="Log")
    DEBUG = o6.enumfield(4, name="Debug")


@o6.enumtype(nodeId="i=19730", browseName="PubSubDiagnosticsCounterClassification")
class PubSubDiagnosticsCounterClassification(Enumeration):
    INFORMATION = o6.enumfield(0, name="Information")
    ERROR = o6.enumfield(1, name="Error")


@o6.datatype(nodeId="i=19746", browseName="SpanContextDataType", defaultEncodingId="i=19754")
class SpanContextDataType(Structure):
    traceId: o6.Guid = o6.field(name="TraceId")
    spanId: o6.UInt64 = o6.field(name="SpanId")


@o6.datatype(nodeId="i=19747", browseName="TraceContextDataType", defaultEncodingId="i=19755")
class TraceContextDataType(SpanContextDataType):
    traceId: o6.Guid = o6.field(name="TraceId")
    spanId: o6.UInt64 = o6.field(name="SpanId")
    parentSpanId: o6.UInt64 = o6.field(name="ParentSpanId")
    parentIdentifier: o6.String = o6.field(name="ParentIdentifier")


@o6.datatype(nodeId="i=19748", browseName="NameValuePair", defaultEncodingId="i=19756")
class NameValuePair(Structure):
    name: o6.String = o6.field(name="Name")
    value: Any = o6.field(name="Value")


@o6.datatype(nodeId="i=19361", browseName="LogRecord", defaultEncodingId="i=19379")
class LogRecord(Structure):
    time: o6.DateTime = o6.field(name="Time")
    severity: o6.UInt16 = o6.field(name="Severity")
    eventType: o6.NodeId | None = o6.field(name="EventType")
    sourceNode: o6.NodeId | None = o6.field(name="SourceNode")
    sourceName: o6.String | None = o6.field(name="SourceName")
    message: o6.LocalizedText = o6.field(name="Message")
    traceContext: TraceContextDataType | None = o6.field(name="TraceContext")
    additionalData: list[NameValuePair] | None = o6.field(name="AdditionalData")


@o6.datatype(nodeId="i=19745", browseName="LogRecordsDataType", defaultEncodingId="i=19753")
class LogRecordsDataType(Structure):
    logRecordArray: list[LogRecord] = o6.field(name="LogRecordArray")


@o6.optionsettype(nodeId="i=19749", browseName="LogRecordMask", base=o6.UInt32)
class LogRecordMask:
    EVENT_TYPE = o6.bitmask(0x01 << 0, name="EventType")
    SOURCE_NODE = o6.bitmask(0x01 << 1, name="SourceNode")
    SOURCE_NAME = o6.bitmask(0x01 << 2, name="SourceName")
    TRACE_CONTEXT = o6.bitmask(0x01 << 3, name="TraceContext")
    ADDITIONAL_DATA = o6.bitmask(0x01 << 4, name="AdditionalData")


@o6.enumtype(nodeId="i=20408", browseName="DataSetOrderingType")
class DataSetOrderingType(Enumeration):
    UNDEFINED = o6.enumfield(0, name="Undefined")
    ASCENDING_WRITER_ID = o6.enumfield(1, name="AscendingWriterId")
    ASCENDING_WRITER_ID_SINGLE = o6.enumfield(2, name="AscendingWriterIdSingle")


@o6.datatype(nodeId="i=15645", browseName="UadpWriterGroupMessageDataType", defaultEncodingId="i=15715")
class UadpWriterGroupMessageDataType(WriterGroupMessageDataType):
    groupVersion: o6.UInt32 = o6.field(name="GroupVersion")
    dataSetOrdering: DataSetOrderingType = o6.field(name="DataSetOrdering")
    networkMessageContentMask: UadpNetworkMessageContentMask = o6.field(name="NetworkMessageContentMask")
    samplingOffset: o6.Double = o6.field(name="SamplingOffset")
    publishingOffset: list[o6.Double] = o6.field(name="PublishingOffset")


@o6.datatype(nodeId="i=20998", browseName="VersionTime", parent="i=7")
class VersionTime:
    pass


@o6.datatype(nodeId="i=20999", browseName="SessionlessInvokeResponseType", defaultEncodingId="i=21001")
class SessionlessInvokeResponseType(Structure):
    namespaceUris: list[o6.String] = o6.field(name="NamespaceUris")
    serverUris: list[o6.String] = o6.field(name="ServerUris")
    serviceId: o6.UInt32 = o6.field(name="ServiceId")


@o6.datatype(nodeId="i=23468", browseName="AliasNameDataType", defaultEncodingId="i=23499")
class AliasNameDataType(Structure):
    aliasName: o6.QualifiedName = o6.field(name="AliasName")
    referencedNodes: list[o6.ExpandedNodeId] = o6.field(name="ReferencedNodes")


@o6.datatype(nodeId="i=23497", browseName="ReadAnnotationDataDetails", defaultEncodingId="i=23500")
class ReadAnnotationDataDetails(HistoryReadDetails):
    reqTimes: list[o6.DateTime] = o6.field(name="ReqTimes")


@o6.datatype(nodeId="i=23498", browseName="CurrencyUnitType", defaultEncodingId="i=23507")
class CurrencyUnitType(Structure):
    numericCode: o6.Int16 = o6.field(name="NumericCode")
    exponent: o6.SByte = o6.field(name="Exponent")
    alphabeticCode: o6.String = o6.field(name="AlphabeticCode")
    currency: o6.LocalizedText = o6.field(name="Currency")


@o6.optionsettype(nodeId="i=23564", browseName="TrustListValidationOptions", base=o6.UInt32)
class TrustListValidationOptions:
    SUPPRESS_CERTIFICATE_EXPIRED = o6.bitmask(0x01 << 0, name="SuppressCertificateExpired")
    SUPPRESS_HOST_NAME_INVALID = o6.bitmask(0x01 << 1, name="SuppressHostNameInvalid")
    SUPPRESS_REVOCATION_STATUS_UNKNOWN = o6.bitmask(0x01 << 2, name="SuppressRevocationStatusUnknown")
    SUPPRESS_ISSUER_CERTIFICATE_EXPIRED = o6.bitmask(0x01 << 3, name="SuppressIssuerCertificateExpired")
    SUPPRESS_ISSUER_REVOCATION_STATUS_UNKNOWN = o6.bitmask(0x01 << 4, name="SuppressIssuerRevocationStatusUnknown")
    CHECK_REVOCATION_STATUS_ONLINE = o6.bitmask(0x01 << 5, name="CheckRevocationStatusOnline")
    CHECK_REVOCATION_STATUS_OFFLINE = o6.bitmask(0x01 << 6, name="CheckRevocationStatusOffline")


@o6.datatype(nodeId="i=15436", browseName="CertificateGroupDataType", defaultEncodingId="i=16540")
class CertificateGroupDataType(BaseConfigurationRecordDataType):
    name: o6.String = o6.field(name="Name")
    recordProperties: list[KeyValuePair] = o6.field(name="RecordProperties")
    purpose: o6.NodeId = o6.field(name="Purpose")
    certificateTypes: list[o6.NodeId] = o6.field(name="CertificateTypes")
    isCertificateAssigned: list[o6.Boolean] = o6.field(name="IsCertificateAssigned")
    validationOptions: TrustListValidationOptions = o6.field(name="ValidationOptions")


@o6.datatype(nodeId="i=23599", browseName="StandaloneSubscribedDataSetRefDataType", defaultEncodingId="i=23851")
class StandaloneSubscribedDataSetRefDataType(SubscribedDataSetDataType):
    dataSetName: o6.String = o6.field(name="DataSetName")


@o6.datatype(nodeId="i=23600", browseName="StandaloneSubscribedDataSetDataType", defaultEncodingId="i=23852")
class StandaloneSubscribedDataSetDataType(SubscribedDataSetDataType):
    name: o6.String = o6.field(name="Name")
    dataSetFolder: list[o6.String] = o6.field(name="DataSetFolder")
    dataSetMetaData: DataSetMetaDataType = o6.field(name="DataSetMetaData")
    subscribedDataSet: SubscribedDataSetDataType = o6.field(name="SubscribedDataSet")


@o6.datatype(nodeId="i=23601", browseName="SecurityGroupDataType", defaultEncodingId="i=23853")
class SecurityGroupDataType(Structure):
    name: o6.String = o6.field(name="Name")
    securityGroupFolder: list[o6.String] = o6.field(name="SecurityGroupFolder")
    keyLifetime: o6.Double = o6.field(name="KeyLifetime")
    securityPolicyUri: o6.String = o6.field(name="SecurityPolicyUri")
    maxFutureKeyCount: o6.UInt32 = o6.field(name="MaxFutureKeyCount")
    maxPastKeyCount: o6.UInt32 = o6.field(name="MaxPastKeyCount")
    securityGroupId: o6.String = o6.field(name="SecurityGroupId")
    rolePermissions: list[RolePermissionType] = o6.field(name="RolePermissions")
    groupProperties: list[KeyValuePair] = o6.field(name="GroupProperties")


@o6.datatype(nodeId="i=23603", browseName="QosDataType", defaultEncodingId="i=23855", isAbstract=True)
class QosDataType(Structure):
    pass


@o6.datatype(nodeId="i=23604", browseName="TransmitQosDataType", defaultEncodingId="i=23856", isAbstract=True)
class TransmitQosDataType(QosDataType):
    pass


@o6.datatype(nodeId="i=23605", browseName="TransmitQosPriorityDataType", defaultEncodingId="i=23857")
class TransmitQosPriorityDataType(TransmitQosDataType):
    priorityLabel: o6.String = o6.field(name="PriorityLabel")


@o6.datatype(nodeId="i=23608", browseName="ReceiveQosDataType", defaultEncodingId="i=23860", isAbstract=True)
class ReceiveQosDataType(QosDataType):
    pass


@o6.datatype(nodeId="i=23609", browseName="ReceiveQosPriorityDataType", defaultEncodingId="i=23861")
class ReceiveQosPriorityDataType(ReceiveQosDataType):
    priorityLabel: o6.String = o6.field(name="PriorityLabel")


@o6.datatype(nodeId="i=23612", browseName="DatagramConnectionTransport2DataType", defaultEncodingId="i=23864")
class DatagramConnectionTransport2DataType(DatagramConnectionTransportDataType):
    discoveryAddress: NetworkAddressDataType = o6.field(name="DiscoveryAddress")
    discoveryAnnounceRate: o6.UInt32 = o6.field(name="DiscoveryAnnounceRate")
    discoveryMaxMessageSize: o6.UInt32 = o6.field(name="DiscoveryMaxMessageSize")
    qosCategory: o6.String = o6.field(name="QosCategory")
    datagramQos: list[QosDataType] = o6.field(name="DatagramQos")


@o6.datatype(nodeId="i=23613", browseName="DatagramWriterGroupTransport2DataType", defaultEncodingId="i=23865")
class DatagramWriterGroupTransport2DataType(DatagramWriterGroupTransportDataType):
    messageRepeatCount: o6.Byte = o6.field(name="MessageRepeatCount")
    messageRepeatDelay: o6.Double = o6.field(name="MessageRepeatDelay")
    address: NetworkAddressDataType = o6.field(name="Address")
    qosCategory: o6.String = o6.field(name="QosCategory")
    datagramQos: list[TransmitQosDataType] = o6.field(name="DatagramQos")
    discoveryAnnounceRate: o6.UInt32 = o6.field(name="DiscoveryAnnounceRate")
    topic: o6.String = o6.field(name="Topic")


@o6.datatype(nodeId="i=23614", browseName="DatagramDataSetReaderTransportDataType", defaultEncodingId="i=23866")
class DatagramDataSetReaderTransportDataType(DataSetReaderTransportDataType):
    address: NetworkAddressDataType = o6.field(name="Address")
    qosCategory: o6.String = o6.field(name="QosCategory")
    datagramQos: list[ReceiveQosDataType] = o6.field(name="DatagramQos")
    topic: o6.String = o6.field(name="Topic")


@o6.datatype(nodeId="i=23724", browseName="ServiceCertificateDataType", defaultEncodingId="i=23725")
class ServiceCertificateDataType(Structure):
    certificate: o6.ByteString = o6.field(name="Certificate")
    issuers: list[o6.ByteString] = o6.field(name="Issuers")
    validFrom: o6.DateTime = o6.field(name="ValidFrom")
    validTo: o6.DateTime = o6.field(name="ValidTo")


@o6.datatype(nodeId="i=23744", browseName="AuthorizationServiceConfigurationDataType", defaultEncodingId="i=23755")
class AuthorizationServiceConfigurationDataType(BaseConfigurationRecordDataType):
    name: o6.String = o6.field(name="Name")
    recordProperties: list[KeyValuePair] = o6.field(name="RecordProperties")
    serviceUri: o6.String = o6.field(name="ServiceUri")
    serviceCertificates: list[ServiceCertificateDataType] = o6.field(name="ServiceCertificates")
    issuerEndpointSettings: o6.String = o6.field(name="IssuerEndpointSettings")


@o6.datatype(nodeId="i=23743", browseName="ApplicationConfigurationDataType", defaultEncodingId="i=23754")
class ApplicationConfigurationDataType(BaseConfigurationDataType):
    configurationVersion: o6.UInt32 = o6.field(name="ConfigurationVersion")
    configurationProperties: list[KeyValuePair] = o6.field(name="ConfigurationProperties")
    applicationIdentity: ApplicationIdentityDataType = o6.field(name="ApplicationIdentity")
    certificateGroups: list[CertificateGroupDataType] = o6.field(name="CertificateGroups")
    serverEndpoints: list[ServerEndpointDataType] = o6.field(name="ServerEndpoints")
    clientEndpoints: list[EndpointDataType] = o6.field(name="ClientEndpoints")
    securitySettings: list[SecuritySettingsDataType] = o6.field(name="SecuritySettings")
    userTokenSettings: list[UserTokenSettingsDataType] = o6.field(name="UserTokenSettings")
    authorizationServices: list[AuthorizationServiceConfigurationDataType] = o6.field(name="AuthorizationServices")


@o6.datatype(nodeId="i=23751", browseName="UriString", parent="i=12")
class UriString:
    pass


@o6.datatype(nodeId="i=23903", browseName="NumberRange", defaultEncodingId="i=24250")
class NumberRange(Structure):
    low: Any = o6.field(name="Low")
    high: Any = o6.field(name="High")


@o6.datatype(nodeId="i=24033", browseName="ProgramDiagnostic2DataType", defaultEncodingId="i=24034")
class ProgramDiagnostic2DataType(Structure):
    createSessionId: o6.NodeId = o6.field(name="CreateSessionId")
    createClientName: o6.String = o6.field(name="CreateClientName")
    invocationCreationTime: o6.DateTime = o6.field(name="InvocationCreationTime")
    lastTransitionTime: o6.DateTime = o6.field(name="LastTransitionTime")
    lastMethodCall: o6.String = o6.field(name="LastMethodCall")
    lastMethodSessionId: o6.NodeId = o6.field(name="LastMethodSessionId")
    lastMethodInputArguments: list[Argument] = o6.field(name="LastMethodInputArguments")
    lastMethodOutputArguments: list[Argument] = o6.field(name="LastMethodOutputArguments")
    lastMethodInputValues: list[Any] = o6.field(name="LastMethodInputValues")
    lastMethodOutputValues: list[Any] = o6.field(name="LastMethodOutputValues")
    lastMethodCallTime: o6.DateTime = o6.field(name="LastMethodCallTime")
    lastMethodReturnStatus: o6.StatusCode = o6.field(name="LastMethodReturnStatus")


@o6.datatype(nodeId="i=24051", browseName="AliasNameVerboseDataType", defaultEncodingId="i=24262")
class AliasNameVerboseDataType(Structure):
    aliasName: o6.QualifiedName = o6.field(name="AliasName")
    referencedNodes: list[o6.ExpandedNodeId] = o6.field(name="ReferencedNodes")
    serverUris: list[o6.String] = o6.field(name="ServerUris")
    aliasNameCategoryId: o6.NodeId = o6.field(name="AliasNameCategoryId")


@o6.datatype(nodeId="i=24105", browseName="PortableQualifiedName", defaultEncodingId="i=24108")
class PortableQualifiedName(Structure):
    namespaceUri: o6.String = o6.field(name="NamespaceUri")
    name: o6.String = o6.field(name="Name")


@o6.datatype(nodeId="i=24106", browseName="PortableNodeId", defaultEncodingId="i=24109")
class PortableNodeId(Structure):
    namespaceUri: o6.String = o6.field(name="NamespaceUri")
    identifier: o6.NodeId = o6.field(name="Identifier")


@o6.datatype(nodeId="i=24052", browseName="AliasCategoryUpdateDataType", defaultEncodingId="i=24338")
class AliasCategoryUpdateDataType(Structure):
    category: PortableNodeId = o6.field(name="Category")
    lastChange: o6.UInt32 = o6.field(name="LastChange")


@o6.datatype(nodeId="i=24053", browseName="AliasUpdateDataType", defaultEncodingId="i=24339")
class AliasUpdateDataType(Structure):
    applicationUri: o6.String = o6.field(name="ApplicationUri")
    categories: list[AliasCategoryUpdateDataType] = o6.field(name="Categories")


@o6.datatype(nodeId="i=24107", browseName="UnsignedRationalNumber", defaultEncodingId="i=24110")
class UnsignedRationalNumber(Structure):
    numerator: o6.UInt32 = o6.field(name="Numerator")
    denominator: o6.UInt32 = o6.field(name="Denominator")


@o6.enumtype(nodeId="i=24210", browseName="Duplex")
class Duplex(Enumeration):
    FULL = o6.enumfield(0, name="Full")
    HALF = o6.enumfield(1, name="Half")
    UNKNOWN = o6.enumfield(2, name="Unknown")


@o6.enumtype(nodeId="i=24212", browseName="InterfaceAdminStatus")
class InterfaceAdminStatus(Enumeration):
    UP = o6.enumfield(0, name="Up")
    DOWN = o6.enumfield(1, name="Down")
    TESTING = o6.enumfield(2, name="Testing")


@o6.enumtype(nodeId="i=24214", browseName="InterfaceOperStatus")
class InterfaceOperStatus(Enumeration):
    UP = o6.enumfield(0, name="Up")
    DOWN = o6.enumfield(1, name="Down")
    TESTING = o6.enumfield(2, name="Testing")
    UNKNOWN = o6.enumfield(3, name="Unknown")
    DORMANT = o6.enumfield(4, name="Dormant")
    NOT_PRESENT = o6.enumfield(5, name="NotPresent")
    LOWER_LAYER_DOWN = o6.enumfield(6, name="LowerLayerDown")


@o6.enumtype(nodeId="i=24216", browseName="NegotiationStatus")
class NegotiationStatus(Enumeration):
    IN_PROGRESS = o6.enumfield(0, name="InProgress")
    COMPLETE = o6.enumfield(1, name="Complete")
    FAILED = o6.enumfield(2, name="Failed")
    UNKNOWN = o6.enumfield(3, name="Unknown")
    NO_NEGOTIATION = o6.enumfield(4, name="NoNegotiation")


@o6.enumtype(nodeId="i=24218", browseName="TsnFailureCode")
class TsnFailureCode(Enumeration):
    NO_FAILURE = o6.enumfield(0, name="NoFailure")
    INSUFFICIENT_BANDWIDTH = o6.enumfield(1, name="InsufficientBandwidth")
    INSUFFICIENT_RESOURCES = o6.enumfield(2, name="InsufficientResources")
    INSUFFICIENT_TRAFFIC_CLASS_BANDWIDTH = o6.enumfield(3, name="InsufficientTrafficClassBandwidth")
    STREAM_ID_IN_USE = o6.enumfield(4, name="StreamIdInUse")
    STREAM_DESTINATION_ADDRESS_IN_USE = o6.enumfield(5, name="StreamDestinationAddressInUse")
    STREAM_PREEMPTED_BY_HIGHER_RANK = o6.enumfield(6, name="StreamPreemptedByHigherRank")
    LATENCY_HAS_CHANGED = o6.enumfield(7, name="LatencyHasChanged")
    EGRESS_PORT_NOT_AVB_CAPABLE = o6.enumfield(8, name="EgressPortNotAvbCapable")
    USE_DIFFERENT_DESTINATION_ADDRESS = o6.enumfield(9, name="UseDifferentDestinationAddress")
    OUT_OF_MSRP_RESOURCES = o6.enumfield(10, name="OutOfMsrpResources")
    OUT_OF_MMRP_RESOURCES = o6.enumfield(11, name="OutOfMmrpResources")
    CANNOT_STORE_DESTINATION_ADDRESS = o6.enumfield(12, name="CannotStoreDestinationAddress")
    PRIORITY_IS_NOT_AN_SRC_CLASS = o6.enumfield(13, name="PriorityIsNotAnSrcClass")
    MAX_FRAME_SIZE_TOO_LARGE = o6.enumfield(14, name="MaxFrameSizeTooLarge")
    MAX_FAN_IN_PORTS_LIMIT_REACHED = o6.enumfield(15, name="MaxFanInPortsLimitReached")
    FIRST_VALUE_CHANGED_FOR_STREAM_ID = o6.enumfield(16, name="FirstValueChangedForStreamId")
    VLAN_BLOCKED_ON_EGRESS = o6.enumfield(17, name="VlanBlockedOnEgress")
    VLAN_TAGGING_DISABLED_ON_EGRESS = o6.enumfield(18, name="VlanTaggingDisabledOnEgress")
    SR_CLASS_PRIORITY_MISMATCH = o6.enumfield(19, name="SrClassPriorityMismatch")
    FEATURE_NOT_PROPAGATED = o6.enumfield(20, name="FeatureNotPropagated")
    MAX_LATENCY_EXCEEDED = o6.enumfield(21, name="MaxLatencyExceeded")
    BRIDGE_DOES_NOT_PROVIDE_NETWORK_ID = o6.enumfield(22, name="BridgeDoesNotProvideNetworkId")
    STREAM_TRANSFORM_NOT_SUPPORTED = o6.enumfield(23, name="StreamTransformNotSupported")
    STREAM_ID_TYPE_NOT_SUPPORTED = o6.enumfield(24, name="StreamIdTypeNotSupported")
    FEATURE_NOT_SUPPORTED = o6.enumfield(25, name="FeatureNotSupported")


@o6.enumtype(nodeId="i=24220", browseName="TsnStreamState")
class TsnStreamState(Enumeration):
    DISABLED = o6.enumfield(0, name="Disabled")
    CONFIGURING = o6.enumfield(1, name="Configuring")
    READY = o6.enumfield(2, name="Ready")
    OPERATIONAL = o6.enumfield(3, name="Operational")
    ERROR = o6.enumfield(4, name="Error")


@o6.enumtype(nodeId="i=24222", browseName="TsnTalkerStatus")
class TsnTalkerStatus(Enumeration):
    NONE = o6.enumfield(0, name="None")
    READY = o6.enumfield(1, name="Ready")
    FAILED = o6.enumfield(2, name="Failed")


@o6.enumtype(nodeId="i=24224", browseName="TsnListenerStatus")
class TsnListenerStatus(Enumeration):
    NONE = o6.enumfield(0, name="None")
    READY = o6.enumfield(1, name="Ready")
    PARTIAL_FAILED = o6.enumfield(2, name="PartialFailed")
    FAILED = o6.enumfield(3, name="Failed")


@o6.datatype(nodeId="i=24263", browseName="SemanticVersionString", parent="i=12")
class SemanticVersionString:
    pass


@o6.optionsettype(nodeId="i=24277", browseName="PasswordOptionsMask", base=o6.UInt32)
class PasswordOptionsMask:
    SUPPORT_INITIAL_PASSWORD_CHANGE = o6.bitmask(0x01 << 0, name="SupportInitialPasswordChange")
    SUPPORT_DISABLE_USER = o6.bitmask(0x01 << 1, name="SupportDisableUser")
    SUPPORT_DISABLE_DELETE_FOR_USER = o6.bitmask(0x01 << 2, name="SupportDisableDeleteForUser")
    SUPPORT_NO_CHANGE_FOR_USER = o6.bitmask(0x01 << 3, name="SupportNoChangeForUser")
    SUPPORT_DESCRIPTION_FOR_USER = o6.bitmask(0x01 << 4, name="SupportDescriptionForUser")
    REQUIRES_UPPER_CASE_CHARACTERS = o6.bitmask(0x01 << 5, name="RequiresUpperCaseCharacters")
    REQUIRES_LOWER_CASE_CHARACTERS = o6.bitmask(0x01 << 6, name="RequiresLowerCaseCharacters")
    REQUIRES_DIGIT_CHARACTERS = o6.bitmask(0x01 << 7, name="RequiresDigitCharacters")
    REQUIRES_SPECIAL_CHARACTERS = o6.bitmask(0x01 << 8, name="RequiresSpecialCharacters")


@o6.optionsettype(nodeId="i=24279", browseName="UserConfigurationMask", base=o6.UInt32)
class UserConfigurationMask:
    NO_DELETE = o6.bitmask(0x01 << 0, name="NoDelete")
    DISABLED = o6.bitmask(0x01 << 1, name="Disabled")
    NO_CHANGE_BY_USER = o6.bitmask(0x01 << 2, name="NoChangeByUser")
    MUST_CHANGE_PASSWORD = o6.bitmask(0x01 << 3, name="MustChangePassword")


@o6.datatype(nodeId="i=24281", browseName="UserManagementDataType", defaultEncodingId="i=24292")
class UserManagementDataType(Structure):
    userName: o6.String = o6.field(name="UserName")
    userConfiguration: UserConfigurationMask = o6.field(name="UserConfiguration")
    description: o6.String = o6.field(name="Description")


@o6.datatype(nodeId="i=25220", browseName="PriorityMappingEntryType", defaultEncodingId="i=25239")
class PriorityMappingEntryType(Structure):
    mappingUri: o6.String = o6.field(name="MappingUri")
    priorityLabel: o6.String = o6.field(name="PriorityLabel")
    priorityValue_PCP: o6.Byte = o6.field(name="PriorityValue_PCP")
    priorityValue_DSCP: o6.UInt32 = o6.field(name="PriorityValue_DSCP")


@o6.datatype(nodeId="i=25269", browseName="PublishedDataSetCustomSourceDataType", defaultEncodingId="i=25529")
class PublishedDataSetCustomSourceDataType(PublishedDataSetSourceDataType):
    cyclicDataSet: o6.Boolean = o6.field(name="CyclicDataSet")


@o6.datatype(nodeId="i=25270", browseName="PubSubKeyPushTargetDataType", defaultEncodingId="i=25530")
class PubSubKeyPushTargetDataType(Structure):
    applicationUri: o6.String = o6.field(name="ApplicationUri")
    pushTargetFolder: list[o6.String] = o6.field(name="PushTargetFolder")
    endpointUrl: o6.String = o6.field(name="EndpointUrl")
    securityPolicyUri: o6.String = o6.field(name="SecurityPolicyUri")
    userTokenType: UserTokenPolicy = o6.field(name="UserTokenType")
    requestedKeyCount: o6.UInt16 = o6.field(name="RequestedKeyCount")
    retryInterval: o6.Double = o6.field(name="RetryInterval")
    pushTargetProperties: list[KeyValuePair] = o6.field(name="PushTargetProperties")
    securityGroups: list[o6.String] = o6.field(name="SecurityGroups")


@o6.datatype(nodeId="i=23602", browseName="PubSubConfiguration2DataType", defaultEncodingId="i=23854")
class PubSubConfiguration2DataType(PubSubConfigurationDataType):
    publishedDataSets: list[PublishedDataSetDataType] = o6.field(name="PublishedDataSets")
    connections: list[PubSubConnectionDataType] = o6.field(name="Connections")
    enabled: o6.Boolean = o6.field(name="Enabled")
    subscribedDataSets: list[StandaloneSubscribedDataSetDataType] = o6.field(name="SubscribedDataSets")
    dataSetClasses: list[DataSetMetaDataType] = o6.field(name="DataSetClasses")
    defaultSecurityKeyServices: list[EndpointDescription] = o6.field(name="DefaultSecurityKeyServices")
    securityGroups: list[SecurityGroupDataType] = o6.field(name="SecurityGroups")
    pubSubKeyPushTargets: list[PubSubKeyPushTargetDataType] = o6.field(name="PubSubKeyPushTargets")
    configurationVersion: o6.UInt32 = o6.field(name="ConfigurationVersion")
    configurationProperties: list[KeyValuePair] = o6.field(name="ConfigurationProperties")


@o6.optionsettype(nodeId="i=25517", browseName="PubSubConfigurationRefMask", base=o6.UInt32)
class PubSubConfigurationRefMask:
    ELEMENT_ADD = o6.bitmask(0x01 << 0, name="ElementAdd")
    ELEMENT_MATCH = o6.bitmask(0x01 << 1, name="ElementMatch")
    ELEMENT_MODIFY = o6.bitmask(0x01 << 2, name="ElementModify")
    ELEMENT_REMOVE = o6.bitmask(0x01 << 3, name="ElementRemove")
    REFERENCE_WRITER = o6.bitmask(0x01 << 4, name="ReferenceWriter")
    REFERENCE_READER = o6.bitmask(0x01 << 5, name="ReferenceReader")
    REFERENCE_WRITER_GROUP = o6.bitmask(0x01 << 6, name="ReferenceWriterGroup")
    REFERENCE_READER_GROUP = o6.bitmask(0x01 << 7, name="ReferenceReaderGroup")
    REFERENCE_CONNECTION = o6.bitmask(0x01 << 8, name="ReferenceConnection")
    REFERENCE_PUB_DATASET = o6.bitmask(0x01 << 9, name="ReferencePubDataset")
    REFERENCE_SUB_DATASET = o6.bitmask(0x01 << 10, name="ReferenceSubDataset")
    REFERENCE_SECURITY_GROUP = o6.bitmask(0x01 << 11, name="ReferenceSecurityGroup")
    REFERENCE_PUSH_TARGET = o6.bitmask(0x01 << 12, name="ReferencePushTarget")


@o6.datatype(nodeId="i=25519", browseName="PubSubConfigurationRefDataType", defaultEncodingId="i=25531")
class PubSubConfigurationRefDataType(Structure):
    configurationMask: PubSubConfigurationRefMask = o6.field(name="ConfigurationMask")
    elementIndex: o6.UInt16 = o6.field(name="ElementIndex")
    connectionIndex: o6.UInt16 = o6.field(name="ConnectionIndex")
    groupIndex: o6.UInt16 = o6.field(name="GroupIndex")


@o6.datatype(nodeId="i=25520", browseName="PubSubConfigurationValueDataType", defaultEncodingId="i=25532")
class PubSubConfigurationValueDataType(Structure):
    configurationElement: PubSubConfigurationRefDataType = o6.field(name="ConfigurationElement")
    name: o6.String = o6.field(name="Name")
    identifier: Any = o6.field(name="Identifier")


@o6.datatype(nodeId="i=25726", browseName="EncodedTicket", parent="i=12")
class EncodedTicket:
    pass


@o6.datatype(nodeId="i=31917", browseName="Handle", parent="i=7")
class Handle:
    pass


@o6.datatype(nodeId="i=31918", browseName="TrimmedString", parent="i=12")
class TrimmedString:
    pass


@o6.optionsettype(nodeId="i=32251", browseName="AlarmMask", base=o6.UInt16)
class AlarmMask:
    ACTIVE = o6.bitmask(0x01 << 0, name="Active")
    UNACKNOWLEDGED = o6.bitmask(0x01 << 1, name="Unacknowledged")
    UNCONFIRMED = o6.bitmask(0x01 << 2, name="Unconfirmed")


@o6.datatype(nodeId="i=32285", browseName="TransactionErrorType", defaultEncodingId="i=32382")
class TransactionErrorType(Structure):
    targetId: o6.NodeId = o6.field(name="TargetId")
    error: o6.StatusCode = o6.field(name="Error")
    message: o6.LocalizedText = o6.field(name="Message")


@o6.enumtype(nodeId="i=32417", browseName="RedundantServerMode")
class RedundantServerMode(Enumeration):
    PRIMARY_WITH_BACKUP = o6.enumfield(0, name="PrimaryWithBackup")
    PRIMARY_ONLY = o6.enumfield(1, name="PrimaryOnly")
    BACKUP_READY = o6.enumfield(2, name="BackupReady")
    BACKUP_NOT_READY = o6.enumfield(3, name="BackupNotReady")


@o6.datatype(nodeId="i=32421", browseName="BitFieldDefinition", defaultEncodingId="i=32422")
class BitFieldDefinition(Structure):
    name: o6.String = o6.field(name="Name")
    description: o6.LocalizedText = o6.field(name="Description")
    reserved: o6.Boolean = o6.field(name="Reserved")
    startingBitPosition: o6.UInt32 = o6.field(name="StartingBitPosition")
    endingBitPosition: o6.UInt32 = o6.field(name="EndingBitPosition")


@o6.datatype(nodeId="i=32434", browseName="AnnotationDataType", defaultEncodingId="i=32560")
class AnnotationDataType(Structure):
    annotation: o6.String = o6.field(name="Annotation")
    discipline: o6.String = o6.field(name="Discipline")
    uri: o6.String = o6.field(name="Uri")


@o6.datatype(nodeId="i=32435", browseName="LinearConversionDataType", defaultEncodingId="i=32561")
class LinearConversionDataType(Structure):
    initialAddend: o6.Float = o6.field(name="InitialAddend")
    multiplicand: o6.Float = o6.field(name="Multiplicand")
    divisor: o6.Float = o6.field(name="Divisor")
    finalAddend: o6.Float = o6.field(name="FinalAddend")


@o6.enumtype(nodeId="i=32436", browseName="ConversionLimitEnum")
class ConversionLimitEnum(Enumeration):
    NO_CONVERSION = o6.enumfield(0, name="NoConversion")
    LIMITED = o6.enumfield(1, name="Limited")
    UNLIMITED = o6.enumfield(2, name="Unlimited")


@o6.datatype(nodeId="i=32438", browseName="QuantityDimension", defaultEncodingId="i=32562")
class QuantityDimension(Structure):
    massExponent: o6.SByte = o6.field(name="MassExponent")
    lengthExponent: o6.SByte = o6.field(name="LengthExponent")
    timeExponent: o6.SByte = o6.field(name="TimeExponent")
    electricCurrentExponent: o6.SByte = o6.field(name="ElectricCurrentExponent")
    amountOfSubstanceExponent: o6.SByte = o6.field(name="AmountOfSubstanceExponent")
    luminousIntensityExponent: o6.SByte = o6.field(name="LuminousIntensityExponent")
    absoluteTemperatureExponent: o6.SByte = o6.field(name="AbsoluteTemperatureExponent")
    dimensionlessExponent: o6.SByte = o6.field(name="DimensionlessExponent")


@o6.datatype(nodeId="i=32659", browseName="ReferenceDescriptionDataType", defaultEncodingId="i=32661")
class ReferenceDescriptionDataType(Structure):
    sourceNode: o6.NodeId = o6.field(name="SourceNode")
    referenceType: o6.NodeId = o6.field(name="ReferenceType")
    isForward: o6.Boolean = o6.field(name="IsForward")
    targetNode: o6.ExpandedNodeId = o6.field(name="TargetNode")


@o6.datatype(nodeId="i=32660", browseName="ReferenceListEntryDataType", defaultEncodingId="i=32662")
class ReferenceListEntryDataType(Structure):
    referenceType: o6.NodeId = o6.field(name="ReferenceType")
    isForward: o6.Boolean = o6.field(name="IsForward")
    targetNode: o6.ExpandedNodeId = o6.field(name="TargetNode")


@o6.datatype(nodeId="i=32799", browseName="ReadEventDetails2", defaultEncodingId="i=32800")
class ReadEventDetails2(ReadEventDetails):
    numValuesPerNode: o6.UInt32 = o6.field(name="NumValuesPerNode")
    startTime: o6.DateTime = o6.field(name="StartTime")
    endTime: o6.DateTime = o6.field(name="EndTime")
    filter: EventFilter = o6.field(name="Filter")
    readModified: o6.Boolean = o6.field(name="ReadModified")


@o6.datatype(nodeId="i=32824", browseName="HistoryModifiedEvent", defaultEncodingId="i=32825")
class HistoryModifiedEvent(HistoryEvent):
    events: list[HistoryEventFieldList] = o6.field(name="Events")
    modificationInfos: list[ModificationInfo] = o6.field(name="ModificationInfos")


del Any, TYPE_CHECKING, uuid, o6, ns0_reftypes
