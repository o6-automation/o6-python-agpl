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


@o6.enumtype(nodeId="i=94", browseName="PermissionType")
class PermissionType(UInt32):
    BROWSE = o6.enumfield(0, name="Browse")
    READ_ROLE_PERMISSIONS = o6.enumfield(1, name="ReadRolePermissions")
    WRITE_ATTRIBUTE = o6.enumfield(2, name="WriteAttribute")
    WRITE_ROLE_PERMISSIONS = o6.enumfield(3, name="WriteRolePermissions")
    WRITE_HISTORIZING = o6.enumfield(4, name="WriteHistorizing")
    READ = o6.enumfield(5, name="Read")
    WRITE = o6.enumfield(6, name="Write")
    READ_HISTORY = o6.enumfield(7, name="ReadHistory")
    INSERT_HISTORY = o6.enumfield(8, name="InsertHistory")
    MODIFY_HISTORY = o6.enumfield(9, name="ModifyHistory")
    DELETE_HISTORY = o6.enumfield(10, name="DeleteHistory")
    RECEIVE_EVENTS = o6.enumfield(11, name="ReceiveEvents")
    CALL = o6.enumfield(12, name="Call")
    ADD_REFERENCE = o6.enumfield(13, name="AddReference")
    REMOVE_REFERENCE = o6.enumfield(14, name="RemoveReference")
    DELETE_NODE = o6.enumfield(15, name="DeleteNode")
    ADD_NODE = o6.enumfield(16, name="AddNode")


@o6.enumtype(nodeId="i=95", browseName="AccessRestrictionType")
class AccessRestrictionType(UInt16):
    SIGNING_REQUIRED = o6.enumfield(0, name="SigningRequired")
    ENCRYPTION_REQUIRED = o6.enumfield(1, name="EncryptionRequired")
    SESSION_REQUIRED = o6.enumfield(2, name="SessionRequired")
    APPLY_RESTRICTIONS_TO_BROWSE = o6.enumfield(3, name="ApplyRestrictionsToBrowse")


@o6.datatype(nodeId="i=96", browseName="RolePermissionType", defaultEncodingId="i=128")
class RolePermissionType(Structure):
    roleId: o6.NodeId
    permissions: PermissionType


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
    name: o6.String
    description: o6.LocalizedText
    dataType: o6.NodeId
    valueRank: o6.Int32
    arrayDimensions: list[o6.UInt32]
    maxStringLength: o6.UInt32
    isOptional: o6.Boolean


@o6.datatype(nodeId="i=99", browseName="StructureDefinition", defaultEncodingId="i=122")
class StructureDefinition(DataTypeDefinition):
    defaultEncodingId: o6.NodeId
    baseDataType: o6.NodeId
    structureType: StructureType
    fields: list[StructureField]


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
    referenceTypeId: o6.NodeId
    isInverse: o6.Boolean
    targetId: o6.ExpandedNodeId


@o6.datatype(nodeId="i=258", browseName="Node", defaultEncodingId="i=260")
class Node(Structure):
    nodeId: o6.NodeId
    nodeClass: NodeClass
    browseName: o6.QualifiedName
    displayName: o6.LocalizedText
    description: o6.LocalizedText
    writeMask: o6.UInt32
    userWriteMask: o6.UInt32
    rolePermissions: list[RolePermissionType]
    userRolePermissions: list[RolePermissionType]
    accessRestrictions: o6.UInt16
    references: list[ReferenceNode]


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
    name: o6.String
    dataType: o6.NodeId
    valueRank: o6.Int32
    arrayDimensions: list[o6.UInt32]
    description: o6.LocalizedText


@o6.datatype(nodeId="i=299", browseName="StatusResult", defaultEncodingId="i=301")
class StatusResult(Structure):
    statusCode: o6.StatusCode
    diagnosticInfo: o6.DiagnosticInfo


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
    policyId: o6.String
    tokenType: UserTokenType
    issuedTokenType: o6.String
    issuerEndpointUrl: o6.String
    securityPolicyUri: o6.String


@o6.enumtype(nodeId="i=307", browseName="ApplicationType")
class ApplicationType(Enumeration):
    SERVER = o6.enumfield(0, name="Server")
    CLIENT = o6.enumfield(1, name="Client")
    CLIENT_AND_SERVER = o6.enumfield(2, name="ClientAndServer")
    DISCOVERY_SERVER = o6.enumfield(3, name="DiscoveryServer")


@o6.datatype(nodeId="i=308", browseName="ApplicationDescription", defaultEncodingId="i=310")
class ApplicationDescription(Structure):
    applicationUri: o6.String
    productUri: o6.String
    applicationName: o6.LocalizedText
    applicationType: ApplicationType
    gatewayServerUri: o6.String
    discoveryProfileUri: o6.String
    discoveryUrls: list[o6.String]


@o6.datatype(nodeId="i=311", browseName="ApplicationInstanceCertificate", parent="i=15")
class ApplicationInstanceCertificate:
    pass


@o6.datatype(nodeId="i=312", browseName="EndpointDescription", defaultEncodingId="i=314")
class EndpointDescription(Structure):
    endpointUrl: o6.String
    server: ApplicationDescription
    serverCertificate: o6.ByteString
    securityMode: MessageSecurityMode
    securityPolicyUri: o6.String
    userIdentityTokens: list[UserTokenPolicy]
    transportProfileUri: o6.String
    securityLevel: o6.Byte


@o6.enumtype(nodeId="i=315", browseName="SecurityTokenRequestType")
class SecurityTokenRequestType(Enumeration):
    ISSUE = o6.enumfield(0, name="Issue")
    RENEW = o6.enumfield(1, name="Renew")


@o6.datatype(nodeId="i=316", browseName="UserIdentityToken", defaultEncodingId="i=318", isAbstract=True)
class UserIdentityToken(Structure):
    policyId: o6.String


@o6.datatype(nodeId="i=319", browseName="AnonymousIdentityToken", defaultEncodingId="i=321")
class AnonymousIdentityToken(UserIdentityToken):
    policyId: o6.String


@o6.datatype(nodeId="i=322", browseName="UserNameIdentityToken", defaultEncodingId="i=324")
class UserNameIdentityToken(UserIdentityToken):
    policyId: o6.String
    userName: o6.String
    password: o6.ByteString
    encryptionAlgorithm: o6.String


@o6.datatype(nodeId="i=325", browseName="X509IdentityToken", defaultEncodingId="i=327")
class X509IdentityToken(UserIdentityToken):
    policyId: o6.String
    certificateData: o6.ByteString


@o6.datatype(nodeId="i=331", browseName="EndpointConfiguration", defaultEncodingId="i=333")
class EndpointConfiguration(Structure):
    operationTimeout: o6.Int32
    useBinaryEncoding: o6.Boolean
    maxStringLength: o6.Int32
    maxByteStringLength: o6.Int32
    maxArrayLength: o6.Int32
    maxMessageSize: o6.Int32
    maxBufferSize: o6.Int32
    channelLifetime: o6.Int32
    securityTokenLifetime: o6.Int32


@o6.datatype(nodeId="i=338", browseName="BuildInfo", defaultEncodingId="i=340")
class BuildInfo(Structure):
    productUri: o6.String
    manufacturerName: o6.String
    productName: o6.String
    softwareVersion: o6.String
    buildNumber: o6.String
    buildDate: o6.DateTime


@o6.datatype(nodeId="i=344", browseName="SignedSoftwareCertificate", defaultEncodingId="i=346")
class SignedSoftwareCertificate(Structure):
    certificateData: o6.ByteString
    signature: o6.ByteString


@o6.enumtype(nodeId="i=347", browseName="AttributeWriteMask")
class AttributeWriteMask(UInt32):
    ACCESS_LEVEL = o6.enumfield(0, name="AccessLevel")
    ARRAY_DIMENSIONS = o6.enumfield(1, name="ArrayDimensions")
    BROWSE_NAME = o6.enumfield(2, name="BrowseName")
    CONTAINS_NO_LOOPS = o6.enumfield(3, name="ContainsNoLoops")
    DATA_TYPE = o6.enumfield(4, name="DataType")
    DESCRIPTION = o6.enumfield(5, name="Description")
    DISPLAY_NAME = o6.enumfield(6, name="DisplayName")
    EVENT_NOTIFIER = o6.enumfield(7, name="EventNotifier")
    EXECUTABLE = o6.enumfield(8, name="Executable")
    HISTORIZING = o6.enumfield(9, name="Historizing")
    INVERSE_NAME = o6.enumfield(10, name="InverseName")
    IS_ABSTRACT = o6.enumfield(11, name="IsAbstract")
    MINIMUM_SAMPLING_INTERVAL = o6.enumfield(12, name="MinimumSamplingInterval")
    NODE_CLASS = o6.enumfield(13, name="NodeClass")
    NODE_ID = o6.enumfield(14, name="NodeId")
    SYMMETRIC = o6.enumfield(15, name="Symmetric")
    USER_ACCESS_LEVEL = o6.enumfield(16, name="UserAccessLevel")
    USER_EXECUTABLE = o6.enumfield(17, name="UserExecutable")
    USER_WRITE_MASK = o6.enumfield(18, name="UserWriteMask")
    VALUE_RANK = o6.enumfield(19, name="ValueRank")
    WRITE_MASK = o6.enumfield(20, name="WriteMask")
    VALUE_FOR_VARIABLE_TYPE = o6.enumfield(21, name="ValueForVariableType")
    DATA_TYPE_DEFINITION = o6.enumfield(22, name="DataTypeDefinition")
    ROLE_PERMISSIONS = o6.enumfield(23, name="RolePermissions")
    ACCESS_RESTRICTIONS = o6.enumfield(24, name="AccessRestrictions")
    ACCESS_LEVEL_EX = o6.enumfield(25, name="AccessLevelEx")


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
    specifiedAttributes: o6.UInt32
    displayName: o6.LocalizedText
    description: o6.LocalizedText
    writeMask: o6.UInt32
    userWriteMask: o6.UInt32


@o6.datatype(nodeId="i=352", browseName="ObjectAttributes", defaultEncodingId="i=354")
class ObjectAttributes(NodeAttributes):
    specifiedAttributes: o6.UInt32
    displayName: o6.LocalizedText
    description: o6.LocalizedText
    writeMask: o6.UInt32
    userWriteMask: o6.UInt32
    eventNotifier: o6.Byte


@o6.datatype(nodeId="i=355", browseName="VariableAttributes", defaultEncodingId="i=357")
class VariableAttributes(NodeAttributes):
    specifiedAttributes: o6.UInt32
    displayName: o6.LocalizedText
    description: o6.LocalizedText
    writeMask: o6.UInt32
    userWriteMask: o6.UInt32
    value: Any
    dataType: o6.NodeId
    valueRank: o6.Int32
    arrayDimensions: list[o6.UInt32]
    accessLevel: o6.Byte
    userAccessLevel: o6.Byte
    minimumSamplingInterval: o6.Double
    historizing: o6.Boolean


@o6.datatype(nodeId="i=358", browseName="MethodAttributes", defaultEncodingId="i=360")
class MethodAttributes(NodeAttributes):
    specifiedAttributes: o6.UInt32
    displayName: o6.LocalizedText
    description: o6.LocalizedText
    writeMask: o6.UInt32
    userWriteMask: o6.UInt32
    executable: o6.Boolean
    userExecutable: o6.Boolean


@o6.datatype(nodeId="i=361", browseName="ObjectTypeAttributes", defaultEncodingId="i=363")
class ObjectTypeAttributes(NodeAttributes):
    specifiedAttributes: o6.UInt32
    displayName: o6.LocalizedText
    description: o6.LocalizedText
    writeMask: o6.UInt32
    userWriteMask: o6.UInt32
    isAbstract: o6.Boolean


@o6.datatype(nodeId="i=364", browseName="VariableTypeAttributes", defaultEncodingId="i=366")
class VariableTypeAttributes(NodeAttributes):
    specifiedAttributes: o6.UInt32
    displayName: o6.LocalizedText
    description: o6.LocalizedText
    writeMask: o6.UInt32
    userWriteMask: o6.UInt32
    value: Any
    dataType: o6.NodeId
    valueRank: o6.Int32
    arrayDimensions: list[o6.UInt32]
    isAbstract: o6.Boolean


@o6.datatype(nodeId="i=367", browseName="ReferenceTypeAttributes", defaultEncodingId="i=369")
class ReferenceTypeAttributes(NodeAttributes):
    specifiedAttributes: o6.UInt32
    displayName: o6.LocalizedText
    description: o6.LocalizedText
    writeMask: o6.UInt32
    userWriteMask: o6.UInt32
    isAbstract: o6.Boolean
    symmetric: o6.Boolean
    inverseName: o6.LocalizedText


@o6.datatype(nodeId="i=370", browseName="DataTypeAttributes", defaultEncodingId="i=372")
class DataTypeAttributes(NodeAttributes):
    specifiedAttributes: o6.UInt32
    displayName: o6.LocalizedText
    description: o6.LocalizedText
    writeMask: o6.UInt32
    userWriteMask: o6.UInt32
    isAbstract: o6.Boolean


@o6.datatype(nodeId="i=373", browseName="ViewAttributes", defaultEncodingId="i=375")
class ViewAttributes(NodeAttributes):
    specifiedAttributes: o6.UInt32
    displayName: o6.LocalizedText
    description: o6.LocalizedText
    writeMask: o6.UInt32
    userWriteMask: o6.UInt32
    containsNoLoops: o6.Boolean
    eventNotifier: o6.Byte


@o6.datatype(nodeId="i=376", browseName="AddNodesItem", defaultEncodingId="i=378")
class AddNodesItem(Structure):
    parentNodeId: o6.ExpandedNodeId
    referenceTypeId: o6.NodeId
    requestedNewNodeId: o6.ExpandedNodeId
    browseName: o6.QualifiedName
    nodeClass: NodeClass
    nodeAttributes: Structure
    typeDefinition: o6.ExpandedNodeId


@o6.datatype(nodeId="i=379", browseName="AddReferencesItem", defaultEncodingId="i=381")
class AddReferencesItem(Structure):
    sourceNodeId: o6.NodeId
    referenceTypeId: o6.NodeId
    isForward: o6.Boolean
    targetServerUri: o6.String
    targetNodeId: o6.ExpandedNodeId
    targetNodeClass: NodeClass


@o6.datatype(nodeId="i=382", browseName="DeleteNodesItem", defaultEncodingId="i=384")
class DeleteNodesItem(Structure):
    nodeId: o6.NodeId
    deleteTargetReferences: o6.Boolean


@o6.datatype(nodeId="i=385", browseName="DeleteReferencesItem", defaultEncodingId="i=387")
class DeleteReferencesItem(Structure):
    sourceNodeId: o6.NodeId
    referenceTypeId: o6.NodeId
    isForward: o6.Boolean
    targetNodeId: o6.ExpandedNodeId
    deleteBidirectional: o6.Boolean


@o6.datatype(nodeId="i=388", browseName="SessionAuthenticationToken", parent="i=17")
class SessionAuthenticationToken:
    pass


@o6.datatype(nodeId="i=389", browseName="RequestHeader", defaultEncodingId="i=391")
class RequestHeader(Structure):
    authenticationToken: o6.NodeId
    timestamp: o6.DateTime
    requestHandle: o6.UInt32
    returnDiagnostics: o6.UInt32
    auditEntryId: o6.String
    timeoutHint: o6.UInt32
    additionalHeader: Structure


@o6.datatype(nodeId="i=392", browseName="ResponseHeader", defaultEncodingId="i=394")
class ResponseHeader(Structure):
    timestamp: o6.DateTime
    requestHandle: o6.UInt32
    serviceResult: o6.StatusCode
    serviceDiagnostics: o6.DiagnosticInfo
    stringTable: list[o6.String]
    additionalHeader: Structure


@o6.datatype(nodeId="i=395", browseName="ServiceFault", defaultEncodingId="i=397")
class ServiceFault(Structure):
    responseHeader: ResponseHeader


@o6.datatype(nodeId="i=420", browseName="FindServersRequest", defaultEncodingId="i=422")
class FindServersRequest(Structure):
    requestHeader: RequestHeader
    endpointUrl: o6.String
    localeIds: list[o6.String]
    serverUris: list[o6.String]


@o6.datatype(nodeId="i=423", browseName="FindServersResponse", defaultEncodingId="i=425")
class FindServersResponse(Structure):
    responseHeader: ResponseHeader
    servers: list[ApplicationDescription]


@o6.datatype(nodeId="i=426", browseName="GetEndpointsRequest", defaultEncodingId="i=428")
class GetEndpointsRequest(Structure):
    requestHeader: RequestHeader
    endpointUrl: o6.String
    localeIds: list[o6.String]
    profileUris: list[o6.String]


@o6.datatype(nodeId="i=429", browseName="GetEndpointsResponse", defaultEncodingId="i=431")
class GetEndpointsResponse(Structure):
    responseHeader: ResponseHeader
    endpoints: list[EndpointDescription]


@o6.datatype(nodeId="i=432", browseName="RegisteredServer", defaultEncodingId="i=434")
class RegisteredServer(Structure):
    serverUri: o6.String
    productUri: o6.String
    serverNames: list[o6.LocalizedText]
    serverType: ApplicationType
    gatewayServerUri: o6.String
    discoveryUrls: list[o6.String]
    semaphoreFilePath: o6.String
    isOnline: o6.Boolean


@o6.datatype(nodeId="i=435", browseName="RegisterServerRequest", defaultEncodingId="i=437")
class RegisterServerRequest(Structure):
    requestHeader: RequestHeader
    server: RegisteredServer


@o6.datatype(nodeId="i=438", browseName="RegisterServerResponse", defaultEncodingId="i=440")
class RegisterServerResponse(Structure):
    responseHeader: ResponseHeader


@o6.datatype(nodeId="i=441", browseName="ChannelSecurityToken", defaultEncodingId="i=443")
class ChannelSecurityToken(Structure):
    channelId: o6.UInt32
    tokenId: o6.UInt32
    createdAt: o6.DateTime
    revisedLifetime: o6.UInt32


@o6.datatype(nodeId="i=444", browseName="OpenSecureChannelRequest", defaultEncodingId="i=446")
class OpenSecureChannelRequest(Structure):
    requestHeader: RequestHeader
    clientProtocolVersion: o6.UInt32
    requestType: SecurityTokenRequestType
    securityMode: MessageSecurityMode
    clientNonce: o6.ByteString
    requestedLifetime: o6.UInt32


@o6.datatype(nodeId="i=447", browseName="OpenSecureChannelResponse", defaultEncodingId="i=449")
class OpenSecureChannelResponse(Structure):
    responseHeader: ResponseHeader
    serverProtocolVersion: o6.UInt32
    securityToken: ChannelSecurityToken
    serverNonce: o6.ByteString


@o6.datatype(nodeId="i=450", browseName="CloseSecureChannelRequest", defaultEncodingId="i=452")
class CloseSecureChannelRequest(Structure):
    requestHeader: RequestHeader


@o6.datatype(nodeId="i=453", browseName="CloseSecureChannelResponse", defaultEncodingId="i=455")
class CloseSecureChannelResponse(Structure):
    responseHeader: ResponseHeader


@o6.datatype(nodeId="i=456", browseName="SignatureData", defaultEncodingId="i=458")
class SignatureData(Structure):
    algorithm: o6.String
    signature: o6.ByteString


@o6.datatype(nodeId="i=459", browseName="CreateSessionRequest", defaultEncodingId="i=461")
class CreateSessionRequest(Structure):
    requestHeader: RequestHeader
    clientDescription: ApplicationDescription
    serverUri: o6.String
    endpointUrl: o6.String
    sessionName: o6.String
    clientNonce: o6.ByteString
    clientCertificate: o6.ByteString
    requestedSessionTimeout: o6.Double
    maxResponseMessageSize: o6.UInt32


@o6.datatype(nodeId="i=462", browseName="CreateSessionResponse", defaultEncodingId="i=464")
class CreateSessionResponse(Structure):
    responseHeader: ResponseHeader
    sessionId: o6.NodeId
    authenticationToken: o6.NodeId
    revisedSessionTimeout: o6.Double
    serverNonce: o6.ByteString
    serverCertificate: o6.ByteString
    serverEndpoints: list[EndpointDescription]
    serverSoftwareCertificates: list[SignedSoftwareCertificate]
    serverSignature: SignatureData
    maxRequestMessageSize: o6.UInt32


@o6.datatype(nodeId="i=465", browseName="ActivateSessionRequest", defaultEncodingId="i=467")
class ActivateSessionRequest(Structure):
    requestHeader: RequestHeader
    clientSignature: SignatureData
    clientSoftwareCertificates: list[SignedSoftwareCertificate]
    localeIds: list[o6.String]
    userIdentityToken: Structure
    userTokenSignature: SignatureData


@o6.datatype(nodeId="i=468", browseName="ActivateSessionResponse", defaultEncodingId="i=470")
class ActivateSessionResponse(Structure):
    responseHeader: ResponseHeader
    serverNonce: o6.ByteString
    results: list[o6.StatusCode]
    diagnosticInfos: list[o6.DiagnosticInfo]


@o6.datatype(nodeId="i=471", browseName="CloseSessionRequest", defaultEncodingId="i=473")
class CloseSessionRequest(Structure):
    requestHeader: RequestHeader
    deleteSubscriptions: o6.Boolean


@o6.datatype(nodeId="i=474", browseName="CloseSessionResponse", defaultEncodingId="i=476")
class CloseSessionResponse(Structure):
    responseHeader: ResponseHeader


@o6.datatype(nodeId="i=477", browseName="CancelRequest", defaultEncodingId="i=479")
class CancelRequest(Structure):
    requestHeader: RequestHeader
    requestHandle: o6.UInt32


@o6.datatype(nodeId="i=480", browseName="CancelResponse", defaultEncodingId="i=482")
class CancelResponse(Structure):
    responseHeader: ResponseHeader
    cancelCount: o6.UInt32


@o6.datatype(nodeId="i=483", browseName="AddNodesResult", defaultEncodingId="i=485")
class AddNodesResult(Structure):
    statusCode: o6.StatusCode
    addedNodeId: o6.NodeId


@o6.datatype(nodeId="i=486", browseName="AddNodesRequest", defaultEncodingId="i=488")
class AddNodesRequest(Structure):
    requestHeader: RequestHeader
    nodesToAdd: list[AddNodesItem]


@o6.datatype(nodeId="i=489", browseName="AddNodesResponse", defaultEncodingId="i=491")
class AddNodesResponse(Structure):
    responseHeader: ResponseHeader
    results: list[AddNodesResult]
    diagnosticInfos: list[o6.DiagnosticInfo]


@o6.datatype(nodeId="i=492", browseName="AddReferencesRequest", defaultEncodingId="i=494")
class AddReferencesRequest(Structure):
    requestHeader: RequestHeader
    referencesToAdd: list[AddReferencesItem]


@o6.datatype(nodeId="i=495", browseName="AddReferencesResponse", defaultEncodingId="i=497")
class AddReferencesResponse(Structure):
    responseHeader: ResponseHeader
    results: list[o6.StatusCode]
    diagnosticInfos: list[o6.DiagnosticInfo]


@o6.datatype(nodeId="i=498", browseName="DeleteNodesRequest", defaultEncodingId="i=500")
class DeleteNodesRequest(Structure):
    requestHeader: RequestHeader
    nodesToDelete: list[DeleteNodesItem]


@o6.datatype(nodeId="i=501", browseName="DeleteNodesResponse", defaultEncodingId="i=503")
class DeleteNodesResponse(Structure):
    responseHeader: ResponseHeader
    results: list[o6.StatusCode]
    diagnosticInfos: list[o6.DiagnosticInfo]


@o6.datatype(nodeId="i=504", browseName="DeleteReferencesRequest", defaultEncodingId="i=506")
class DeleteReferencesRequest(Structure):
    requestHeader: RequestHeader
    referencesToDelete: list[DeleteReferencesItem]


@o6.datatype(nodeId="i=507", browseName="DeleteReferencesResponse", defaultEncodingId="i=509")
class DeleteReferencesResponse(Structure):
    responseHeader: ResponseHeader
    results: list[o6.StatusCode]
    diagnosticInfos: list[o6.DiagnosticInfo]


@o6.enumtype(nodeId="i=510", browseName="BrowseDirection")
class BrowseDirection(Enumeration):
    FORWARD = o6.enumfield(0, name="Forward")
    INVERSE = o6.enumfield(1, name="Inverse")
    BOTH = o6.enumfield(2, name="Both")
    INVALID = o6.enumfield(3, name="Invalid")


@o6.datatype(nodeId="i=511", browseName="ViewDescription", defaultEncodingId="i=513")
class ViewDescription(Structure):
    viewId: o6.NodeId
    timestamp: o6.DateTime
    viewVersion: o6.UInt32


@o6.datatype(nodeId="i=514", browseName="BrowseDescription", defaultEncodingId="i=516")
class BrowseDescription(Structure):
    nodeId: o6.NodeId
    browseDirection: BrowseDirection
    referenceTypeId: o6.NodeId
    includeSubtypes: o6.Boolean
    nodeClassMask: o6.UInt32
    resultMask: o6.UInt32


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
    referenceTypeId: o6.NodeId
    isForward: o6.Boolean
    nodeId: o6.ExpandedNodeId
    browseName: o6.QualifiedName
    displayName: o6.LocalizedText
    nodeClass: NodeClass
    typeDefinition: o6.ExpandedNodeId


@o6.datatype(nodeId="i=521", browseName="ContinuationPoint", parent="i=15")
class ContinuationPoint:
    pass


@o6.datatype(nodeId="i=522", browseName="BrowseResult", defaultEncodingId="i=524")
class BrowseResult(Structure):
    statusCode: o6.StatusCode
    continuationPoint: o6.ByteString
    references: list[ReferenceDescription]


@o6.datatype(nodeId="i=525", browseName="BrowseRequest", defaultEncodingId="i=527")
class BrowseRequest(Structure):
    requestHeader: RequestHeader
    view: ViewDescription
    requestedMaxReferencesPerNode: o6.UInt32
    nodesToBrowse: list[BrowseDescription]


@o6.datatype(nodeId="i=528", browseName="BrowseResponse", defaultEncodingId="i=530")
class BrowseResponse(Structure):
    responseHeader: ResponseHeader
    results: list[BrowseResult]
    diagnosticInfos: list[o6.DiagnosticInfo]


@o6.datatype(nodeId="i=531", browseName="BrowseNextRequest", defaultEncodingId="i=533")
class BrowseNextRequest(Structure):
    requestHeader: RequestHeader
    releaseContinuationPoints: o6.Boolean
    continuationPoints: list[o6.ByteString]


@o6.datatype(nodeId="i=534", browseName="BrowseNextResponse", defaultEncodingId="i=536")
class BrowseNextResponse(Structure):
    responseHeader: ResponseHeader
    results: list[BrowseResult]
    diagnosticInfos: list[o6.DiagnosticInfo]


@o6.datatype(nodeId="i=537", browseName="RelativePathElement", defaultEncodingId="i=539")
class RelativePathElement(Structure):
    referenceTypeId: o6.NodeId
    isInverse: o6.Boolean
    includeSubtypes: o6.Boolean
    targetName: o6.QualifiedName


@o6.datatype(nodeId="i=540", browseName="RelativePath", defaultEncodingId="i=542")
class RelativePath(Structure):
    elements: list[RelativePathElement]


@o6.datatype(nodeId="i=543", browseName="BrowsePath", defaultEncodingId="i=545")
class BrowsePath(Structure):
    startingNode: o6.NodeId
    relativePath: RelativePath


@o6.datatype(nodeId="i=546", browseName="BrowsePathTarget", defaultEncodingId="i=548")
class BrowsePathTarget(Structure):
    targetId: o6.ExpandedNodeId
    remainingPathIndex: o6.UInt32


@o6.datatype(nodeId="i=549", browseName="BrowsePathResult", defaultEncodingId="i=551")
class BrowsePathResult(Structure):
    statusCode: o6.StatusCode
    targets: list[BrowsePathTarget]


@o6.datatype(nodeId="i=552", browseName="TranslateBrowsePathsToNodeIdsRequest", defaultEncodingId="i=554")
class TranslateBrowsePathsToNodeIdsRequest(Structure):
    requestHeader: RequestHeader
    browsePaths: list[BrowsePath]


@o6.datatype(nodeId="i=555", browseName="TranslateBrowsePathsToNodeIdsResponse", defaultEncodingId="i=557")
class TranslateBrowsePathsToNodeIdsResponse(Structure):
    responseHeader: ResponseHeader
    results: list[BrowsePathResult]
    diagnosticInfos: list[o6.DiagnosticInfo]


@o6.datatype(nodeId="i=558", browseName="RegisterNodesRequest", defaultEncodingId="i=560")
class RegisterNodesRequest(Structure):
    requestHeader: RequestHeader
    nodesToRegister: list[o6.NodeId]


@o6.datatype(nodeId="i=561", browseName="RegisterNodesResponse", defaultEncodingId="i=563")
class RegisterNodesResponse(Structure):
    responseHeader: ResponseHeader
    registeredNodeIds: list[o6.NodeId]


@o6.datatype(nodeId="i=564", browseName="UnregisterNodesRequest", defaultEncodingId="i=566")
class UnregisterNodesRequest(Structure):
    requestHeader: RequestHeader
    nodesToUnregister: list[o6.NodeId]


@o6.datatype(nodeId="i=567", browseName="UnregisterNodesResponse", defaultEncodingId="i=569")
class UnregisterNodesResponse(Structure):
    responseHeader: ResponseHeader


@o6.datatype(nodeId="i=570", browseName="QueryDataDescription", defaultEncodingId="i=572")
class QueryDataDescription(Structure):
    relativePath: RelativePath
    attributeId: o6.UInt32
    indexRange: o6.String


@o6.datatype(nodeId="i=573", browseName="NodeTypeDescription", defaultEncodingId="i=575")
class NodeTypeDescription(Structure):
    typeDefinitionNode: o6.ExpandedNodeId
    includeSubTypes: o6.Boolean
    dataToReturn: list[QueryDataDescription]


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
    nodeId: o6.ExpandedNodeId
    typeDefinitionNode: o6.ExpandedNodeId
    values: list[Any]


@o6.datatype(nodeId="i=580", browseName="NodeReference", defaultEncodingId="i=582")
class NodeReference(Structure):
    nodeId: o6.NodeId
    referenceTypeId: o6.NodeId
    isForward: o6.Boolean
    referencedNodeIds: list[o6.NodeId]


@o6.datatype(nodeId="i=583", browseName="ContentFilterElement", defaultEncodingId="i=585")
class ContentFilterElement(Structure):
    filterOperator: FilterOperator
    filterOperands: list[Structure]


@o6.datatype(nodeId="i=586", browseName="ContentFilter", defaultEncodingId="i=588")
class ContentFilter(Structure):
    elements: list[ContentFilterElement]


@o6.datatype(nodeId="i=589", browseName="FilterOperand", defaultEncodingId="i=591", isAbstract=True)
class FilterOperand(Structure):
    pass


@o6.datatype(nodeId="i=592", browseName="ElementOperand", defaultEncodingId="i=594")
class ElementOperand(FilterOperand):
    index: o6.UInt32


@o6.datatype(nodeId="i=595", browseName="LiteralOperand", defaultEncodingId="i=597")
class LiteralOperand(FilterOperand):
    value: Any


@o6.datatype(nodeId="i=598", browseName="AttributeOperand", defaultEncodingId="i=600")
class AttributeOperand(FilterOperand):
    nodeId: o6.NodeId
    alias: o6.String
    browsePath: RelativePath
    attributeId: o6.UInt32
    indexRange: o6.String


@o6.datatype(nodeId="i=601", browseName="SimpleAttributeOperand", defaultEncodingId="i=603")
class SimpleAttributeOperand(FilterOperand):
    typeDefinitionId: o6.NodeId
    browsePath: list[o6.QualifiedName]
    attributeId: o6.UInt32
    indexRange: o6.String


@o6.datatype(nodeId="i=604", browseName="ContentFilterElementResult", defaultEncodingId="i=606")
class ContentFilterElementResult(Structure):
    statusCode: o6.StatusCode
    operandStatusCodes: list[o6.StatusCode]
    operandDiagnosticInfos: list[o6.DiagnosticInfo]


@o6.datatype(nodeId="i=607", browseName="ContentFilterResult", defaultEncodingId="i=609")
class ContentFilterResult(Structure):
    elementResults: list[ContentFilterElementResult]
    elementDiagnosticInfos: list[o6.DiagnosticInfo]


@o6.datatype(nodeId="i=610", browseName="ParsingResult", defaultEncodingId="i=612")
class ParsingResult(Structure):
    statusCode: o6.StatusCode
    dataStatusCodes: list[o6.StatusCode]
    dataDiagnosticInfos: list[o6.DiagnosticInfo]


@o6.datatype(nodeId="i=613", browseName="QueryFirstRequest", defaultEncodingId="i=615")
class QueryFirstRequest(Structure):
    requestHeader: RequestHeader
    view: ViewDescription
    nodeTypes: list[NodeTypeDescription]
    filter: ContentFilter
    maxDataSetsToReturn: o6.UInt32
    maxReferencesToReturn: o6.UInt32


@o6.datatype(nodeId="i=616", browseName="QueryFirstResponse", defaultEncodingId="i=618")
class QueryFirstResponse(Structure):
    responseHeader: ResponseHeader
    queryDataSets: list[QueryDataSet]
    continuationPoint: o6.ByteString
    parsingResults: list[ParsingResult]
    diagnosticInfos: list[o6.DiagnosticInfo]
    filterResult: ContentFilterResult


@o6.datatype(nodeId="i=619", browseName="QueryNextRequest", defaultEncodingId="i=621")
class QueryNextRequest(Structure):
    requestHeader: RequestHeader
    releaseContinuationPoint: o6.Boolean
    continuationPoint: o6.ByteString


@o6.datatype(nodeId="i=622", browseName="QueryNextResponse", defaultEncodingId="i=624")
class QueryNextResponse(Structure):
    responseHeader: ResponseHeader
    queryDataSets: list[QueryDataSet]
    revisedContinuationPoint: o6.ByteString


@o6.enumtype(nodeId="i=625", browseName="TimestampsToReturn")
class TimestampsToReturn(Enumeration):
    SOURCE = o6.enumfield(0, name="Source")
    SERVER = o6.enumfield(1, name="Server")
    BOTH = o6.enumfield(2, name="Both")
    NEITHER = o6.enumfield(3, name="Neither")
    INVALID = o6.enumfield(4, name="Invalid")


@o6.datatype(nodeId="i=626", browseName="ReadValueId", defaultEncodingId="i=628")
class ReadValueId(Structure):
    nodeId: o6.NodeId
    attributeId: o6.UInt32
    indexRange: o6.String
    dataEncoding: o6.QualifiedName


@o6.datatype(nodeId="i=629", browseName="ReadRequest", defaultEncodingId="i=631")
class ReadRequest(Structure):
    requestHeader: RequestHeader
    maxAge: o6.Double
    timestampsToReturn: TimestampsToReturn
    nodesToRead: list[ReadValueId]


@o6.datatype(nodeId="i=632", browseName="ReadResponse", defaultEncodingId="i=634")
class ReadResponse(Structure):
    responseHeader: ResponseHeader
    results: list[o6.DataValue]
    diagnosticInfos: list[o6.DiagnosticInfo]


@o6.datatype(nodeId="i=635", browseName="HistoryReadValueId", defaultEncodingId="i=637")
class HistoryReadValueId(Structure):
    nodeId: o6.NodeId
    indexRange: o6.String
    dataEncoding: o6.QualifiedName
    continuationPoint: o6.ByteString


@o6.datatype(nodeId="i=638", browseName="HistoryReadResult", defaultEncodingId="i=640")
class HistoryReadResult(Structure):
    statusCode: o6.StatusCode
    continuationPoint: o6.ByteString
    historyData: Structure


@o6.datatype(nodeId="i=641", browseName="HistoryReadDetails", defaultEncodingId="i=643", isAbstract=True)
class HistoryReadDetails(Structure):
    pass


@o6.datatype(nodeId="i=647", browseName="ReadRawModifiedDetails", defaultEncodingId="i=649")
class ReadRawModifiedDetails(HistoryReadDetails):
    isReadModified: o6.Boolean
    startTime: o6.DateTime
    endTime: o6.DateTime
    numValuesPerNode: o6.UInt32
    returnBounds: o6.Boolean


@o6.datatype(nodeId="i=653", browseName="ReadAtTimeDetails", defaultEncodingId="i=655")
class ReadAtTimeDetails(HistoryReadDetails):
    reqTimes: list[o6.DateTime]
    useSimpleBounds: o6.Boolean


@o6.datatype(nodeId="i=656", browseName="HistoryData", defaultEncodingId="i=658")
class HistoryData(Structure):
    dataValues: list[o6.DataValue]


@o6.datatype(nodeId="i=662", browseName="HistoryReadRequest", defaultEncodingId="i=664")
class HistoryReadRequest(Structure):
    requestHeader: RequestHeader
    historyReadDetails: Structure
    timestampsToReturn: TimestampsToReturn
    releaseContinuationPoints: o6.Boolean
    nodesToRead: list[HistoryReadValueId]


@o6.datatype(nodeId="i=665", browseName="HistoryReadResponse", defaultEncodingId="i=667")
class HistoryReadResponse(Structure):
    responseHeader: ResponseHeader
    results: list[HistoryReadResult]
    diagnosticInfos: list[o6.DiagnosticInfo]


@o6.datatype(nodeId="i=668", browseName="WriteValue", defaultEncodingId="i=670")
class WriteValue(Structure):
    nodeId: o6.NodeId
    attributeId: o6.UInt32
    indexRange: o6.String
    value: o6.DataValue


@o6.datatype(nodeId="i=671", browseName="WriteRequest", defaultEncodingId="i=673")
class WriteRequest(Structure):
    requestHeader: RequestHeader
    nodesToWrite: list[WriteValue]


@o6.datatype(nodeId="i=674", browseName="WriteResponse", defaultEncodingId="i=676")
class WriteResponse(Structure):
    responseHeader: ResponseHeader
    results: list[o6.StatusCode]
    diagnosticInfos: list[o6.DiagnosticInfo]


@o6.datatype(nodeId="i=677", browseName="HistoryUpdateDetails", defaultEncodingId="i=679", isAbstract=True)
class HistoryUpdateDetails(Structure):
    pass


@o6.datatype(nodeId="i=686", browseName="DeleteRawModifiedDetails", defaultEncodingId="i=688")
class DeleteRawModifiedDetails(HistoryUpdateDetails):
    nodeId: o6.NodeId
    isDeleteModified: o6.Boolean
    startTime: o6.DateTime
    endTime: o6.DateTime


@o6.datatype(nodeId="i=689", browseName="DeleteAtTimeDetails", defaultEncodingId="i=691")
class DeleteAtTimeDetails(HistoryUpdateDetails):
    nodeId: o6.NodeId
    reqTimes: list[o6.DateTime]


@o6.datatype(nodeId="i=692", browseName="DeleteEventDetails", defaultEncodingId="i=694")
class DeleteEventDetails(HistoryUpdateDetails):
    nodeId: o6.NodeId
    eventIds: list[o6.ByteString]


@o6.datatype(nodeId="i=695", browseName="HistoryUpdateResult", defaultEncodingId="i=697")
class HistoryUpdateResult(Structure):
    statusCode: o6.StatusCode
    operationResults: list[o6.StatusCode]
    diagnosticInfos: list[o6.DiagnosticInfo]


@o6.datatype(nodeId="i=698", browseName="HistoryUpdateRequest", defaultEncodingId="i=700")
class HistoryUpdateRequest(Structure):
    requestHeader: RequestHeader
    historyUpdateDetails: list[Structure]


@o6.datatype(nodeId="i=701", browseName="HistoryUpdateResponse", defaultEncodingId="i=703")
class HistoryUpdateResponse(Structure):
    responseHeader: ResponseHeader
    results: list[HistoryUpdateResult]
    diagnosticInfos: list[o6.DiagnosticInfo]


@o6.datatype(nodeId="i=704", browseName="CallMethodRequest", defaultEncodingId="i=706")
class CallMethodRequest(Structure):
    objectId: o6.NodeId
    methodId: o6.NodeId
    inputArguments: list[Any]


@o6.datatype(nodeId="i=707", browseName="CallMethodResult", defaultEncodingId="i=709")
class CallMethodResult(Structure):
    statusCode: o6.StatusCode
    inputArgumentResults: list[o6.StatusCode]
    inputArgumentDiagnosticInfos: list[o6.DiagnosticInfo]
    outputArguments: list[Any]


@o6.datatype(nodeId="i=710", browseName="CallRequest", defaultEncodingId="i=712")
class CallRequest(Structure):
    requestHeader: RequestHeader
    methodsToCall: list[CallMethodRequest]


@o6.datatype(nodeId="i=713", browseName="CallResponse", defaultEncodingId="i=715")
class CallResponse(Structure):
    responseHeader: ResponseHeader
    results: list[CallMethodResult]
    diagnosticInfos: list[o6.DiagnosticInfo]


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
    trigger: DataChangeTrigger
    deadbandType: o6.UInt32
    deadbandValue: o6.Double


@o6.datatype(nodeId="i=725", browseName="EventFilter", defaultEncodingId="i=727")
class EventFilter(MonitoringFilter):
    @classmethod
    def parse(cls, query: str, logger: object | None = None) -> EventFilter: ...

    selectClauses: list[SimpleAttributeOperand]
    whereClause: ContentFilter


@o6.datatype(nodeId="i=644", browseName="ReadEventDetails", defaultEncodingId="i=646")
class ReadEventDetails(HistoryReadDetails):
    numValuesPerNode: o6.UInt32
    startTime: o6.DateTime
    endTime: o6.DateTime
    filter: EventFilter


@o6.datatype(nodeId="i=731", browseName="MonitoringFilterResult", defaultEncodingId="i=733")
class MonitoringFilterResult(Structure):
    pass


@o6.datatype(nodeId="i=734", browseName="EventFilterResult", defaultEncodingId="i=736")
class EventFilterResult(MonitoringFilterResult):
    selectClauseResults: list[o6.StatusCode]
    selectClauseDiagnosticInfos: list[o6.DiagnosticInfo]
    whereClauseResult: ContentFilterResult


@o6.datatype(nodeId="i=740", browseName="MonitoringParameters", defaultEncodingId="i=742")
class MonitoringParameters(Structure):
    clientHandle: o6.UInt32
    samplingInterval: o6.Double
    filter: Structure
    queueSize: o6.UInt32
    discardOldest: o6.Boolean


@o6.datatype(nodeId="i=743", browseName="MonitoredItemCreateRequest", defaultEncodingId="i=745")
class MonitoredItemCreateRequest(Structure):
    itemToMonitor: ReadValueId
    monitoringMode: MonitoringMode
    requestedParameters: MonitoringParameters


@o6.datatype(nodeId="i=746", browseName="MonitoredItemCreateResult", defaultEncodingId="i=748")
class MonitoredItemCreateResult(Structure):
    statusCode: o6.StatusCode
    monitoredItemId: o6.UInt32
    revisedSamplingInterval: o6.Double
    revisedQueueSize: o6.UInt32
    filterResult: Structure


@o6.datatype(nodeId="i=749", browseName="CreateMonitoredItemsRequest", defaultEncodingId="i=751")
class CreateMonitoredItemsRequest(Structure):
    requestHeader: RequestHeader
    subscriptionId: o6.UInt32
    timestampsToReturn: TimestampsToReturn
    itemsToCreate: list[MonitoredItemCreateRequest]


@o6.datatype(nodeId="i=752", browseName="CreateMonitoredItemsResponse", defaultEncodingId="i=754")
class CreateMonitoredItemsResponse(Structure):
    responseHeader: ResponseHeader
    results: list[MonitoredItemCreateResult]
    diagnosticInfos: list[o6.DiagnosticInfo]


@o6.datatype(nodeId="i=755", browseName="MonitoredItemModifyRequest", defaultEncodingId="i=757")
class MonitoredItemModifyRequest(Structure):
    monitoredItemId: o6.UInt32
    requestedParameters: MonitoringParameters


@o6.datatype(nodeId="i=758", browseName="MonitoredItemModifyResult", defaultEncodingId="i=760")
class MonitoredItemModifyResult(Structure):
    statusCode: o6.StatusCode
    revisedSamplingInterval: o6.Double
    revisedQueueSize: o6.UInt32
    filterResult: Structure


@o6.datatype(nodeId="i=761", browseName="ModifyMonitoredItemsRequest", defaultEncodingId="i=763")
class ModifyMonitoredItemsRequest(Structure):
    requestHeader: RequestHeader
    subscriptionId: o6.UInt32
    timestampsToReturn: TimestampsToReturn
    itemsToModify: list[MonitoredItemModifyRequest]


@o6.datatype(nodeId="i=764", browseName="ModifyMonitoredItemsResponse", defaultEncodingId="i=766")
class ModifyMonitoredItemsResponse(Structure):
    responseHeader: ResponseHeader
    results: list[MonitoredItemModifyResult]
    diagnosticInfos: list[o6.DiagnosticInfo]


@o6.datatype(nodeId="i=767", browseName="SetMonitoringModeRequest", defaultEncodingId="i=769")
class SetMonitoringModeRequest(Structure):
    requestHeader: RequestHeader
    subscriptionId: o6.UInt32
    monitoringMode: MonitoringMode
    monitoredItemIds: list[o6.UInt32]


@o6.datatype(nodeId="i=770", browseName="SetMonitoringModeResponse", defaultEncodingId="i=772")
class SetMonitoringModeResponse(Structure):
    responseHeader: ResponseHeader
    results: list[o6.StatusCode]
    diagnosticInfos: list[o6.DiagnosticInfo]


@o6.datatype(nodeId="i=773", browseName="SetTriggeringRequest", defaultEncodingId="i=775")
class SetTriggeringRequest(Structure):
    requestHeader: RequestHeader
    subscriptionId: o6.UInt32
    triggeringItemId: o6.UInt32
    linksToAdd: list[o6.UInt32]
    linksToRemove: list[o6.UInt32]


@o6.datatype(nodeId="i=776", browseName="SetTriggeringResponse", defaultEncodingId="i=778")
class SetTriggeringResponse(Structure):
    responseHeader: ResponseHeader
    addResults: list[o6.StatusCode]
    addDiagnosticInfos: list[o6.DiagnosticInfo]
    removeResults: list[o6.StatusCode]
    removeDiagnosticInfos: list[o6.DiagnosticInfo]


@o6.datatype(nodeId="i=779", browseName="DeleteMonitoredItemsRequest", defaultEncodingId="i=781")
class DeleteMonitoredItemsRequest(Structure):
    requestHeader: RequestHeader
    subscriptionId: o6.UInt32
    monitoredItemIds: list[o6.UInt32]


@o6.datatype(nodeId="i=782", browseName="DeleteMonitoredItemsResponse", defaultEncodingId="i=784")
class DeleteMonitoredItemsResponse(Structure):
    responseHeader: ResponseHeader
    results: list[o6.StatusCode]
    diagnosticInfos: list[o6.DiagnosticInfo]


@o6.datatype(nodeId="i=785", browseName="CreateSubscriptionRequest", defaultEncodingId="i=787")
class CreateSubscriptionRequest(Structure):
    requestHeader: RequestHeader
    requestedPublishingInterval: o6.Double
    requestedLifetimeCount: o6.UInt32
    requestedMaxKeepAliveCount: o6.UInt32
    maxNotificationsPerPublish: o6.UInt32
    publishingEnabled: o6.Boolean
    priority: o6.Byte


@o6.datatype(nodeId="i=788", browseName="CreateSubscriptionResponse", defaultEncodingId="i=790")
class CreateSubscriptionResponse(Structure):
    responseHeader: ResponseHeader
    subscriptionId: o6.UInt32
    revisedPublishingInterval: o6.Double
    revisedLifetimeCount: o6.UInt32
    revisedMaxKeepAliveCount: o6.UInt32


@o6.datatype(nodeId="i=791", browseName="ModifySubscriptionRequest", defaultEncodingId="i=793")
class ModifySubscriptionRequest(Structure):
    requestHeader: RequestHeader
    subscriptionId: o6.UInt32
    requestedPublishingInterval: o6.Double
    requestedLifetimeCount: o6.UInt32
    requestedMaxKeepAliveCount: o6.UInt32
    maxNotificationsPerPublish: o6.UInt32
    priority: o6.Byte


@o6.datatype(nodeId="i=794", browseName="ModifySubscriptionResponse", defaultEncodingId="i=796")
class ModifySubscriptionResponse(Structure):
    responseHeader: ResponseHeader
    revisedPublishingInterval: o6.Double
    revisedLifetimeCount: o6.UInt32
    revisedMaxKeepAliveCount: o6.UInt32


@o6.datatype(nodeId="i=797", browseName="SetPublishingModeRequest", defaultEncodingId="i=799")
class SetPublishingModeRequest(Structure):
    requestHeader: RequestHeader
    publishingEnabled: o6.Boolean
    subscriptionIds: list[o6.UInt32]


@o6.datatype(nodeId="i=800", browseName="SetPublishingModeResponse", defaultEncodingId="i=802")
class SetPublishingModeResponse(Structure):
    responseHeader: ResponseHeader
    results: list[o6.StatusCode]
    diagnosticInfos: list[o6.DiagnosticInfo]


@o6.datatype(nodeId="i=803", browseName="NotificationMessage", defaultEncodingId="i=805")
class NotificationMessage(Structure):
    sequenceNumber: o6.UInt32
    publishTime: o6.DateTime
    notificationData: list[Structure]


@o6.datatype(nodeId="i=806", browseName="MonitoredItemNotification", defaultEncodingId="i=808")
class MonitoredItemNotification(Structure):
    clientHandle: o6.UInt32
    value: o6.DataValue


@o6.datatype(nodeId="i=821", browseName="SubscriptionAcknowledgement", defaultEncodingId="i=823")
class SubscriptionAcknowledgement(Structure):
    subscriptionId: o6.UInt32
    sequenceNumber: o6.UInt32


@o6.datatype(nodeId="i=824", browseName="PublishRequest", defaultEncodingId="i=826")
class PublishRequest(Structure):
    requestHeader: RequestHeader
    subscriptionAcknowledgements: list[SubscriptionAcknowledgement]


@o6.datatype(nodeId="i=827", browseName="PublishResponse", defaultEncodingId="i=829")
class PublishResponse(Structure):
    responseHeader: ResponseHeader
    subscriptionId: o6.UInt32
    availableSequenceNumbers: list[o6.UInt32]
    moreNotifications: o6.Boolean
    notificationMessage: NotificationMessage
    results: list[o6.StatusCode]
    diagnosticInfos: list[o6.DiagnosticInfo]


@o6.datatype(nodeId="i=830", browseName="RepublishRequest", defaultEncodingId="i=832")
class RepublishRequest(Structure):
    requestHeader: RequestHeader
    subscriptionId: o6.UInt32
    retransmitSequenceNumber: o6.UInt32


@o6.datatype(nodeId="i=833", browseName="RepublishResponse", defaultEncodingId="i=835")
class RepublishResponse(Structure):
    responseHeader: ResponseHeader
    notificationMessage: NotificationMessage


@o6.datatype(nodeId="i=836", browseName="TransferResult", defaultEncodingId="i=838")
class TransferResult(Structure):
    statusCode: o6.StatusCode
    availableSequenceNumbers: list[o6.UInt32]


@o6.datatype(nodeId="i=839", browseName="TransferSubscriptionsRequest", defaultEncodingId="i=841")
class TransferSubscriptionsRequest(Structure):
    requestHeader: RequestHeader
    subscriptionIds: list[o6.UInt32]
    sendInitialValues: o6.Boolean


@o6.datatype(nodeId="i=842", browseName="TransferSubscriptionsResponse", defaultEncodingId="i=844")
class TransferSubscriptionsResponse(Structure):
    responseHeader: ResponseHeader
    results: list[TransferResult]
    diagnosticInfos: list[o6.DiagnosticInfo]


@o6.datatype(nodeId="i=845", browseName="DeleteSubscriptionsRequest", defaultEncodingId="i=847")
class DeleteSubscriptionsRequest(Structure):
    requestHeader: RequestHeader
    subscriptionIds: list[o6.UInt32]


@o6.datatype(nodeId="i=848", browseName="DeleteSubscriptionsResponse", defaultEncodingId="i=850")
class DeleteSubscriptionsResponse(Structure):
    responseHeader: ResponseHeader
    results: list[o6.StatusCode]
    diagnosticInfos: list[o6.DiagnosticInfo]


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
    serverId: o6.String
    serviceLevel: o6.Byte
    serverState: ServerState


@o6.datatype(nodeId="i=856", browseName="SamplingIntervalDiagnosticsDataType", defaultEncodingId="i=858")
class SamplingIntervalDiagnosticsDataType(Structure):
    samplingInterval: o6.Double
    monitoredItemCount: o6.UInt32
    maxMonitoredItemCount: o6.UInt32
    disabledMonitoredItemCount: o6.UInt32


@o6.datatype(nodeId="i=859", browseName="ServerDiagnosticsSummaryDataType", defaultEncodingId="i=861")
class ServerDiagnosticsSummaryDataType(Structure):
    serverViewCount: o6.UInt32
    currentSessionCount: o6.UInt32
    cumulatedSessionCount: o6.UInt32
    securityRejectedSessionCount: o6.UInt32
    rejectedSessionCount: o6.UInt32
    sessionTimeoutCount: o6.UInt32
    sessionAbortCount: o6.UInt32
    currentSubscriptionCount: o6.UInt32
    cumulatedSubscriptionCount: o6.UInt32
    publishingIntervalCount: o6.UInt32
    securityRejectedRequestsCount: o6.UInt32
    rejectedRequestsCount: o6.UInt32


@o6.datatype(nodeId="i=862", browseName="ServerStatusDataType", defaultEncodingId="i=864")
class ServerStatusDataType(Structure):
    startTime: o6.DateTime
    currentTime: o6.DateTime
    state: ServerState
    buildInfo: BuildInfo
    secondsTillShutdown: o6.UInt32
    shutdownReason: o6.LocalizedText


@o6.datatype(nodeId="i=868", browseName="SessionSecurityDiagnosticsDataType", defaultEncodingId="i=870")
class SessionSecurityDiagnosticsDataType(Structure):
    sessionId: o6.NodeId
    clientUserIdOfSession: o6.String
    clientUserIdHistory: list[o6.String]
    authenticationMechanism: o6.String
    encoding: o6.String
    transportProtocol: o6.String
    securityMode: MessageSecurityMode
    securityPolicyUri: o6.String
    clientCertificate: o6.ByteString


@o6.datatype(nodeId="i=871", browseName="ServiceCounterDataType", defaultEncodingId="i=873")
class ServiceCounterDataType(Structure):
    totalCount: o6.UInt32
    errorCount: o6.UInt32


@o6.datatype(nodeId="i=865", browseName="SessionDiagnosticsDataType", defaultEncodingId="i=867")
class SessionDiagnosticsDataType(Structure):
    sessionId: o6.NodeId
    sessionName: o6.String
    clientDescription: ApplicationDescription
    serverUri: o6.String
    endpointUrl: o6.String
    localeIds: list[o6.String]
    actualSessionTimeout: o6.Double
    maxResponseMessageSize: o6.UInt32
    clientConnectionTime: o6.DateTime
    clientLastContactTime: o6.DateTime
    currentSubscriptionsCount: o6.UInt32
    currentMonitoredItemsCount: o6.UInt32
    currentPublishRequestsInQueue: o6.UInt32
    totalRequestCount: ServiceCounterDataType
    unauthorizedRequestCount: o6.UInt32
    readCount: ServiceCounterDataType
    historyReadCount: ServiceCounterDataType
    writeCount: ServiceCounterDataType
    historyUpdateCount: ServiceCounterDataType
    callCount: ServiceCounterDataType
    createMonitoredItemsCount: ServiceCounterDataType
    modifyMonitoredItemsCount: ServiceCounterDataType
    setMonitoringModeCount: ServiceCounterDataType
    setTriggeringCount: ServiceCounterDataType
    deleteMonitoredItemsCount: ServiceCounterDataType
    createSubscriptionCount: ServiceCounterDataType
    modifySubscriptionCount: ServiceCounterDataType
    setPublishingModeCount: ServiceCounterDataType
    publishCount: ServiceCounterDataType
    republishCount: ServiceCounterDataType
    transferSubscriptionsCount: ServiceCounterDataType
    deleteSubscriptionsCount: ServiceCounterDataType
    addNodesCount: ServiceCounterDataType
    addReferencesCount: ServiceCounterDataType
    deleteNodesCount: ServiceCounterDataType
    deleteReferencesCount: ServiceCounterDataType
    browseCount: ServiceCounterDataType
    browseNextCount: ServiceCounterDataType
    translateBrowsePathsToNodeIdsCount: ServiceCounterDataType
    queryFirstCount: ServiceCounterDataType
    queryNextCount: ServiceCounterDataType
    registerNodesCount: ServiceCounterDataType
    unregisterNodesCount: ServiceCounterDataType


@o6.datatype(nodeId="i=874", browseName="SubscriptionDiagnosticsDataType", defaultEncodingId="i=876")
class SubscriptionDiagnosticsDataType(Structure):
    sessionId: o6.NodeId
    subscriptionId: o6.UInt32
    priority: o6.Byte
    publishingInterval: o6.Double
    maxKeepAliveCount: o6.UInt32
    maxLifetimeCount: o6.UInt32
    maxNotificationsPerPublish: o6.UInt32
    publishingEnabled: o6.Boolean
    modifyCount: o6.UInt32
    enableCount: o6.UInt32
    disableCount: o6.UInt32
    republishRequestCount: o6.UInt32
    republishMessageRequestCount: o6.UInt32
    republishMessageCount: o6.UInt32
    transferRequestCount: o6.UInt32
    transferredToAltClientCount: o6.UInt32
    transferredToSameClientCount: o6.UInt32
    publishRequestCount: o6.UInt32
    dataChangeNotificationsCount: o6.UInt32
    eventNotificationsCount: o6.UInt32
    notificationsCount: o6.UInt32
    latePublishRequestCount: o6.UInt32
    currentKeepAliveCount: o6.UInt32
    currentLifetimeCount: o6.UInt32
    unacknowledgedMessageCount: o6.UInt32
    discardedMessageCount: o6.UInt32
    monitoredItemCount: o6.UInt32
    disabledMonitoredItemCount: o6.UInt32
    monitoringQueueOverflowCount: o6.UInt32
    nextSequenceNumber: o6.UInt32
    eventQueueOverflowCount: o6.UInt32


@o6.datatype(nodeId="i=877", browseName="ModelChangeStructureDataType", defaultEncodingId="i=879")
class ModelChangeStructureDataType(Structure):
    affected: o6.NodeId
    affectedType: o6.NodeId
    verb: o6.Byte


@o6.datatype(nodeId="i=884", browseName="Range", defaultEncodingId="i=886")
class Range(Structure):
    low: o6.Double
    high: o6.Double


@o6.datatype(nodeId="i=887", browseName="EUInformation", defaultEncodingId="i=889")
class EUInformation(Structure):
    namespaceUri: o6.String
    unitId: o6.Int32
    displayName: o6.LocalizedText
    description: o6.LocalizedText


@o6.enumtype(nodeId="i=890", browseName="ExceptionDeviationFormat")
class ExceptionDeviationFormat(Enumeration):
    ABSOLUTE_VALUE = o6.enumfield(0, name="AbsoluteValue")
    PERCENT_OF_VALUE = o6.enumfield(1, name="PercentOfValue")
    PERCENT_OF_RANGE = o6.enumfield(2, name="PercentOfRange")
    PERCENT_OF_EU_RANGE = o6.enumfield(3, name="PercentOfEURange")
    UNKNOWN = o6.enumfield(4, name="Unknown")


@o6.datatype(nodeId="i=891", browseName="Annotation", defaultEncodingId="i=893")
class Annotation(Structure):
    message: o6.String
    userName: o6.String
    annotationTime: o6.DateTime


@o6.datatype(nodeId="i=894", browseName="ProgramDiagnosticDataType", defaultEncodingId="i=896")
class ProgramDiagnosticDataType(Structure):
    createSessionId: o6.NodeId
    createClientName: o6.String
    invocationCreationTime: o6.DateTime
    lastTransitionTime: o6.DateTime
    lastMethodCall: o6.String
    lastMethodSessionId: o6.NodeId
    lastMethodInputArguments: list[Argument]
    lastMethodOutputArguments: list[Argument]
    lastMethodCallTime: o6.DateTime
    lastMethodReturnStatus: StatusResult


@o6.datatype(nodeId="i=897", browseName="SemanticChangeStructureDataType", defaultEncodingId="i=899")
class SemanticChangeStructureDataType(Structure):
    affected: o6.NodeId
    affectedType: o6.NodeId


@o6.datatype(nodeId="i=917", browseName="EventFieldList", defaultEncodingId="i=919")
class EventFieldList(Structure):
    clientHandle: o6.UInt32
    eventFields: list[Any]


@o6.datatype(nodeId="i=920", browseName="HistoryEventFieldList", defaultEncodingId="i=922")
class HistoryEventFieldList(Structure):
    eventFields: list[Any]


@o6.datatype(nodeId="i=659", browseName="HistoryEvent", defaultEncodingId="i=661")
class HistoryEvent(Structure):
    events: list[HistoryEventFieldList]


@o6.datatype(nodeId="i=938", browseName="IssuedIdentityToken", defaultEncodingId="i=940")
class IssuedIdentityToken(UserIdentityToken):
    policyId: o6.String
    tokenData: o6.ByteString
    encryptionAlgorithm: o6.String


@o6.datatype(nodeId="i=945", browseName="NotificationData", defaultEncodingId="i=947")
class NotificationData(Structure):
    pass


@o6.datatype(nodeId="i=809", browseName="DataChangeNotification", defaultEncodingId="i=811")
class DataChangeNotification(NotificationData):
    monitoredItems: list[MonitoredItemNotification]
    diagnosticInfos: list[o6.DiagnosticInfo]


@o6.datatype(nodeId="i=818", browseName="StatusChangeNotification", defaultEncodingId="i=820")
class StatusChangeNotification(NotificationData):
    status: o6.StatusCode
    diagnosticInfo: o6.DiagnosticInfo


@o6.datatype(nodeId="i=914", browseName="EventNotificationList", defaultEncodingId="i=916")
class EventNotificationList(NotificationData):
    events: list[EventFieldList]


@o6.datatype(nodeId="i=948", browseName="AggregateConfiguration", defaultEncodingId="i=950")
class AggregateConfiguration(Structure):
    useServerCapabilitiesDefaults: o6.Boolean
    treatUncertainAsBad: o6.Boolean
    percentDataBad: o6.Byte
    percentDataGood: o6.Byte
    useSlopedExtrapolation: o6.Boolean


@o6.datatype(nodeId="i=650", browseName="ReadProcessedDetails", defaultEncodingId="i=652")
class ReadProcessedDetails(HistoryReadDetails):
    startTime: o6.DateTime
    endTime: o6.DateTime
    processingInterval: o6.Double
    aggregateType: list[o6.NodeId]
    aggregateConfiguration: AggregateConfiguration


@o6.datatype(nodeId="i=728", browseName="AggregateFilter", defaultEncodingId="i=730")
class AggregateFilter(MonitoringFilter):
    startTime: o6.DateTime
    aggregateType: o6.NodeId
    processingInterval: o6.Double
    aggregateConfiguration: AggregateConfiguration


@o6.datatype(nodeId="i=737", browseName="AggregateFilterResult", defaultEncodingId="i=739")
class AggregateFilterResult(MonitoringFilterResult):
    revisedStartTime: o6.DateTime
    revisedProcessingInterval: o6.Double
    revisedAggregateConfiguration: AggregateConfiguration


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
    value: o6.Int64
    displayName: o6.LocalizedText
    description: o6.LocalizedText


@o6.datatype(nodeId="i=102", browseName="EnumField", defaultEncodingId="i=14845")
class EnumField(EnumValueType):
    value: o6.Int64
    displayName: o6.LocalizedText
    description: o6.LocalizedText
    name: o6.String


@o6.datatype(nodeId="i=100", browseName="EnumDefinition", defaultEncodingId="i=123")
class EnumDefinition(DataTypeDefinition):
    fields: list[EnumField]


@o6.datatype(nodeId="i=8912", browseName="TimeZoneDataType", defaultEncodingId="i=8917")
class TimeZoneDataType(Structure):
    offset: o6.Int16
    daylightSavingInOffset: o6.Boolean


@o6.enumtype(nodeId="i=11234", browseName="HistoryUpdateType")
class HistoryUpdateType(Enumeration):
    INSERT = o6.enumfield(1, name="Insert")
    REPLACE = o6.enumfield(2, name="Replace")
    UPDATE = o6.enumfield(3, name="Update")
    DELETE = o6.enumfield(4, name="Delete")


@o6.datatype(nodeId="i=11216", browseName="ModificationInfo", defaultEncodingId="i=11226")
class ModificationInfo(Structure):
    modificationTime: o6.DateTime
    updateType: HistoryUpdateType
    userName: o6.String


@o6.datatype(nodeId="i=11217", browseName="HistoryModifiedData", defaultEncodingId="i=11227")
class HistoryModifiedData(HistoryData):
    dataValues: list[o6.DataValue]
    modificationInfos: list[ModificationInfo]


@o6.enumtype(nodeId="i=11293", browseName="PerformUpdateType")
class PerformUpdateType(Enumeration):
    INSERT = o6.enumfield(1, name="Insert")
    REPLACE = o6.enumfield(2, name="Replace")
    UPDATE = o6.enumfield(3, name="Update")
    REMOVE = o6.enumfield(4, name="Remove")


@o6.datatype(nodeId="i=680", browseName="UpdateDataDetails", defaultEncodingId="i=682")
class UpdateDataDetails(HistoryUpdateDetails):
    nodeId: o6.NodeId
    performInsertReplace: PerformUpdateType
    updateValues: list[o6.DataValue]


@o6.datatype(nodeId="i=683", browseName="UpdateEventDetails", defaultEncodingId="i=685")
class UpdateEventDetails(HistoryUpdateDetails):
    nodeId: o6.NodeId
    performInsertReplace: PerformUpdateType
    filter: EventFilter
    eventData: list[HistoryEventFieldList]


@o6.datatype(nodeId="i=11295", browseName="UpdateStructureDataDetails", defaultEncodingId="i=11300")
class UpdateStructureDataDetails(HistoryUpdateDetails):
    nodeId: o6.NodeId
    performInsertReplace: PerformUpdateType
    updateValues: list[o6.DataValue]


@o6.datatype(nodeId="i=11737", browseName="BitFieldMaskDataType", parent="i=9")
class BitFieldMaskDataType:
    pass


@o6.datatype(nodeId="i=11879", browseName="InstanceNode", defaultEncodingId="i=11889")
class InstanceNode(Node):
    nodeId: o6.NodeId
    nodeClass: NodeClass
    browseName: o6.QualifiedName
    displayName: o6.LocalizedText
    description: o6.LocalizedText
    writeMask: o6.UInt32
    userWriteMask: o6.UInt32
    rolePermissions: list[RolePermissionType]
    userRolePermissions: list[RolePermissionType]
    accessRestrictions: o6.UInt16
    references: list[ReferenceNode]


@o6.datatype(nodeId="i=261", browseName="ObjectNode", defaultEncodingId="i=263")
class ObjectNode(InstanceNode):
    nodeId: o6.NodeId
    nodeClass: NodeClass
    browseName: o6.QualifiedName
    displayName: o6.LocalizedText
    description: o6.LocalizedText
    writeMask: o6.UInt32
    userWriteMask: o6.UInt32
    rolePermissions: list[RolePermissionType]
    userRolePermissions: list[RolePermissionType]
    accessRestrictions: o6.UInt16
    references: list[ReferenceNode]
    eventNotifier: o6.Byte


@o6.datatype(nodeId="i=267", browseName="VariableNode", defaultEncodingId="i=269")
class VariableNode(InstanceNode):
    nodeId: o6.NodeId
    nodeClass: NodeClass
    browseName: o6.QualifiedName
    displayName: o6.LocalizedText
    description: o6.LocalizedText
    writeMask: o6.UInt32
    userWriteMask: o6.UInt32
    rolePermissions: list[RolePermissionType]
    userRolePermissions: list[RolePermissionType]
    accessRestrictions: o6.UInt16
    references: list[ReferenceNode]
    value: Any
    dataType: o6.NodeId
    valueRank: o6.Int32
    arrayDimensions: list[o6.UInt32]
    accessLevel: o6.Byte
    userAccessLevel: o6.Byte
    minimumSamplingInterval: o6.Double
    historizing: o6.Boolean
    accessLevelEx: o6.UInt32


@o6.datatype(nodeId="i=276", browseName="MethodNode", defaultEncodingId="i=278")
class MethodNode(InstanceNode):
    nodeId: o6.NodeId
    nodeClass: NodeClass
    browseName: o6.QualifiedName
    displayName: o6.LocalizedText
    description: o6.LocalizedText
    writeMask: o6.UInt32
    userWriteMask: o6.UInt32
    rolePermissions: list[RolePermissionType]
    userRolePermissions: list[RolePermissionType]
    accessRestrictions: o6.UInt16
    references: list[ReferenceNode]
    executable: o6.Boolean
    userExecutable: o6.Boolean


@o6.datatype(nodeId="i=279", browseName="ViewNode", defaultEncodingId="i=281")
class ViewNode(InstanceNode):
    nodeId: o6.NodeId
    nodeClass: NodeClass
    browseName: o6.QualifiedName
    displayName: o6.LocalizedText
    description: o6.LocalizedText
    writeMask: o6.UInt32
    userWriteMask: o6.UInt32
    rolePermissions: list[RolePermissionType]
    userRolePermissions: list[RolePermissionType]
    accessRestrictions: o6.UInt16
    references: list[ReferenceNode]
    containsNoLoops: o6.Boolean
    eventNotifier: o6.Byte


@o6.datatype(nodeId="i=11880", browseName="TypeNode", defaultEncodingId="i=11890")
class TypeNode(Node):
    nodeId: o6.NodeId
    nodeClass: NodeClass
    browseName: o6.QualifiedName
    displayName: o6.LocalizedText
    description: o6.LocalizedText
    writeMask: o6.UInt32
    userWriteMask: o6.UInt32
    rolePermissions: list[RolePermissionType]
    userRolePermissions: list[RolePermissionType]
    accessRestrictions: o6.UInt16
    references: list[ReferenceNode]


@o6.datatype(nodeId="i=264", browseName="ObjectTypeNode", defaultEncodingId="i=266")
class ObjectTypeNode(TypeNode):
    nodeId: o6.NodeId
    nodeClass: NodeClass
    browseName: o6.QualifiedName
    displayName: o6.LocalizedText
    description: o6.LocalizedText
    writeMask: o6.UInt32
    userWriteMask: o6.UInt32
    rolePermissions: list[RolePermissionType]
    userRolePermissions: list[RolePermissionType]
    accessRestrictions: o6.UInt16
    references: list[ReferenceNode]
    isAbstract: o6.Boolean


@o6.datatype(nodeId="i=270", browseName="VariableTypeNode", defaultEncodingId="i=272")
class VariableTypeNode(TypeNode):
    nodeId: o6.NodeId
    nodeClass: NodeClass
    browseName: o6.QualifiedName
    displayName: o6.LocalizedText
    description: o6.LocalizedText
    writeMask: o6.UInt32
    userWriteMask: o6.UInt32
    rolePermissions: list[RolePermissionType]
    userRolePermissions: list[RolePermissionType]
    accessRestrictions: o6.UInt16
    references: list[ReferenceNode]
    value: Any
    dataType: o6.NodeId
    valueRank: o6.Int32
    arrayDimensions: list[o6.UInt32]
    isAbstract: o6.Boolean


@o6.datatype(nodeId="i=273", browseName="ReferenceTypeNode", defaultEncodingId="i=275")
class ReferenceTypeNode(TypeNode):
    nodeId: o6.NodeId
    nodeClass: NodeClass
    browseName: o6.QualifiedName
    displayName: o6.LocalizedText
    description: o6.LocalizedText
    writeMask: o6.UInt32
    userWriteMask: o6.UInt32
    rolePermissions: list[RolePermissionType]
    userRolePermissions: list[RolePermissionType]
    accessRestrictions: o6.UInt16
    references: list[ReferenceNode]
    isAbstract: o6.Boolean
    symmetric: o6.Boolean
    inverseName: o6.LocalizedText


@o6.datatype(nodeId="i=282", browseName="DataTypeNode", defaultEncodingId="i=284")
class DataTypeNode(TypeNode):
    nodeId: o6.NodeId
    nodeClass: NodeClass
    browseName: o6.QualifiedName
    displayName: o6.LocalizedText
    description: o6.LocalizedText
    writeMask: o6.UInt32
    userWriteMask: o6.UInt32
    rolePermissions: list[RolePermissionType]
    userRolePermissions: list[RolePermissionType]
    accessRestrictions: o6.UInt16
    references: list[ReferenceNode]
    isAbstract: o6.Boolean
    dataTypeDefinition: Structure


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
    endpointUrlList: list[o6.String]


@o6.datatype(nodeId="i=11944", browseName="NetworkGroupDataType", defaultEncodingId="i=11958")
class NetworkGroupDataType(Structure):
    serverUri: o6.String
    networkPaths: list[EndpointUrlListDataType]


@o6.enumtype(nodeId="i=12077", browseName="AxisScaleEnumeration")
class AxisScaleEnumeration(Enumeration):
    LINEAR = o6.enumfield(0, name="Linear")
    LOG = o6.enumfield(1, name="Log")
    LN = o6.enumfield(2, name="Ln")


@o6.datatype(nodeId="i=12079", browseName="AxisInformation", defaultEncodingId="i=12089")
class AxisInformation(Structure):
    engineeringUnits: EUInformation
    eURange: Range
    title: o6.LocalizedText
    axisScaleType: AxisScaleEnumeration
    axisSteps: list[o6.Double]


@o6.datatype(nodeId="i=12080", browseName="XVType", defaultEncodingId="i=12090")
class XVType(Structure):
    x: o6.Double
    value: o6.Float


@o6.datatype(nodeId="i=12171", browseName="ComplexNumberType", defaultEncodingId="i=12181")
class ComplexNumberType(Structure):
    real: o6.Float
    imaginary: o6.Float


@o6.datatype(nodeId="i=12172", browseName="DoubleComplexNumberType", defaultEncodingId="i=12182")
class DoubleComplexNumberType(Structure):
    real: o6.Double
    imaginary: o6.Double


@o6.datatype(nodeId="i=12189", browseName="ServerOnNetwork", defaultEncodingId="i=12207")
class ServerOnNetwork(Structure):
    recordId: o6.UInt32
    serverName: o6.String
    discoveryUrl: o6.String
    serverCapabilities: list[o6.String]


@o6.datatype(nodeId="i=12190", browseName="FindServersOnNetworkRequest", defaultEncodingId="i=12208")
class FindServersOnNetworkRequest(Structure):
    requestHeader: RequestHeader
    startingRecordId: o6.UInt32
    maxRecordsToReturn: o6.UInt32
    serverCapabilityFilter: list[o6.String]


@o6.datatype(nodeId="i=12191", browseName="FindServersOnNetworkResponse", defaultEncodingId="i=12209")
class FindServersOnNetworkResponse(Structure):
    responseHeader: ResponseHeader
    lastCounterResetTime: o6.DateTime
    servers: list[ServerOnNetwork]


@o6.datatype(nodeId="i=12193", browseName="RegisterServer2Request", defaultEncodingId="i=12211")
class RegisterServer2Request(Structure):
    requestHeader: RequestHeader
    server: RegisteredServer
    discoveryConfiguration: list[Structure]


@o6.datatype(nodeId="i=12194", browseName="RegisterServer2Response", defaultEncodingId="i=12212")
class RegisterServer2Response(Structure):
    responseHeader: ResponseHeader
    configurationResults: list[o6.StatusCode]
    diagnosticInfos: list[o6.DiagnosticInfo]


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
    specifiedLists: o6.UInt32
    trustedCertificates: list[o6.ByteString]
    trustedCrls: list[o6.ByteString]
    issuerCertificates: list[o6.ByteString]
    issuerCrls: list[o6.ByteString]


@o6.datatype(nodeId="i=12755", browseName="OptionSet", defaultEncodingId="i=12765", isAbstract=True)
class OptionSet(Structure):
    value: o6.ByteString
    validBits: o6.ByteString


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
    mdnsServerName: o6.String
    serverCapabilities: list[o6.String]


@o6.datatype(nodeId="i=14273", browseName="PublishedVariableDataType", defaultEncodingId="i=14323")
class PublishedVariableDataType(Structure):
    publishedVariable: o6.NodeId
    attributeId: o6.UInt32
    samplingIntervalHint: o6.Double
    deadbandType: o6.UInt32
    deadbandValue: o6.Double
    indexRange: o6.String
    substituteValue: Any
    metaDataProperties: list[o6.QualifiedName]


@o6.datatype(nodeId="i=14525", browseName="DataTypeDescription", defaultEncodingId="i=125", isAbstract=True)
class DataTypeDescription(Structure):
    dataTypeId: o6.NodeId
    name: o6.QualifiedName


@o6.datatype(nodeId="i=14533", browseName="KeyValuePair", defaultEncodingId="i=14846")
class KeyValuePair(Structure):
    key: o6.QualifiedName
    value: Any


@o6.datatype(nodeId="i=14593", browseName="ConfigurationVersionDataType", defaultEncodingId="i=14847")
class ConfigurationVersionDataType(Structure):
    majorVersion: o6.UInt32
    minorVersion: o6.UInt32


@o6.enumtype(nodeId="i=14647", browseName="PubSubState")
class PubSubState(Enumeration):
    DISABLED = o6.enumfield(0, name="Disabled")
    PAUSED = o6.enumfield(1, name="Paused")
    OPERATIONAL = o6.enumfield(2, name="Operational")
    ERROR = o6.enumfield(3, name="Error")
    PRE_OPERATIONAL = o6.enumfield(4, name="PreOperational")


@o6.datatype(nodeId="i=15005", browseName="SimpleTypeDescription", defaultEncodingId="i=15421")
class SimpleTypeDescription(DataTypeDescription):
    dataTypeId: o6.NodeId
    name: o6.QualifiedName
    baseDataType: o6.NodeId
    builtInType: o6.Byte


@o6.enumtype(nodeId="i=15008", browseName="BrokerTransportQualityOfService")
class BrokerTransportQualityOfService(Enumeration):
    NOT_SPECIFIED = o6.enumfield(0, name="NotSpecified")
    BEST_EFFORT = o6.enumfield(1, name="BestEffort")
    AT_LEAST_ONCE = o6.enumfield(2, name="AtLeastOnce")
    AT_MOST_ONCE = o6.enumfield(3, name="AtMostOnce")
    EXACTLY_ONCE = o6.enumfield(4, name="ExactlyOnce")


@o6.enumtype(nodeId="i=15031", browseName="AccessLevelType")
class AccessLevelType(Byte):
    CURRENT_READ = o6.enumfield(0, name="CurrentRead")
    CURRENT_WRITE = o6.enumfield(1, name="CurrentWrite")
    HISTORY_READ = o6.enumfield(2, name="HistoryRead")
    HISTORY_WRITE = o6.enumfield(3, name="HistoryWrite")
    SEMANTIC_CHANGE = o6.enumfield(4, name="SemanticChange")
    STATUS_WRITE = o6.enumfield(5, name="StatusWrite")
    TIMESTAMP_WRITE = o6.enumfield(6, name="TimestampWrite")


@o6.enumtype(nodeId="i=15033", browseName="EventNotifierType")
class EventNotifierType(Byte):
    SUBSCRIBE_TO_EVENTS = o6.enumfield(0, name="SubscribeToEvents")
    HISTORY_READ = o6.enumfield(2, name="HistoryRead")
    HISTORY_WRITE = o6.enumfield(3, name="HistoryWrite")


@o6.enumtype(nodeId="i=15406", browseName="AccessLevelExType")
class AccessLevelExType(UInt32):
    CURRENT_READ = o6.enumfield(0, name="CurrentRead")
    CURRENT_WRITE = o6.enumfield(1, name="CurrentWrite")
    HISTORY_READ = o6.enumfield(2, name="HistoryRead")
    HISTORY_WRITE = o6.enumfield(3, name="HistoryWrite")
    SEMANTIC_CHANGE = o6.enumfield(4, name="SemanticChange")
    STATUS_WRITE = o6.enumfield(5, name="StatusWrite")
    TIMESTAMP_WRITE = o6.enumfield(6, name="TimestampWrite")
    NONATOMIC_READ = o6.enumfield(8, name="NonatomicRead")
    NONATOMIC_WRITE = o6.enumfield(9, name="NonatomicWrite")
    WRITE_FULL_ARRAY_ONLY = o6.enumfield(10, name="WriteFullArrayOnly")
    NO_SUB_DATA_TYPES = o6.enumfield(11, name="NoSubDataTypes")
    NON_VOLATILE = o6.enumfield(12, name="NonVolatile")
    CONSTANT = o6.enumfield(13, name="Constant")


@o6.datatype(nodeId="i=15434", browseName="BaseConfigurationDataType", defaultEncodingId="i=16538", isAbstract=True)
class BaseConfigurationDataType(Structure):
    configurationVersion: o6.UInt32
    configurationProperties: list[KeyValuePair]


@o6.datatype(nodeId="i=15435", browseName="BaseConfigurationRecordDataType", defaultEncodingId="i=16539", isAbstract=True)
class BaseConfigurationRecordDataType(Structure):
    name: o6.String
    recordProperties: list[KeyValuePair]


@o6.datatype(nodeId="i=15487", browseName="StructureDescription", defaultEncodingId="i=126")
class StructureDescription(DataTypeDescription):
    dataTypeId: o6.NodeId
    name: o6.QualifiedName
    structureDefinition: StructureDefinition


@o6.datatype(nodeId="i=15488", browseName="EnumDescription", defaultEncodingId="i=127")
class EnumDescription(DataTypeDescription):
    dataTypeId: o6.NodeId
    name: o6.QualifiedName
    enumDefinition: EnumDefinition
    builtInType: o6.Byte


@o6.datatype(nodeId="i=15502", browseName="NetworkAddressDataType", defaultEncodingId="i=21151", isAbstract=True)
class NetworkAddressDataType(Structure):
    networkInterface: o6.String


@o6.datatype(nodeId="i=15510", browseName="NetworkAddressUrlDataType", defaultEncodingId="i=21152")
class NetworkAddressUrlDataType(NetworkAddressDataType):
    networkInterface: o6.String
    url: o6.String


@o6.datatype(nodeId="i=15528", browseName="EndpointType", defaultEncodingId="i=15671")
class EndpointType(Structure):
    endpointUrl: o6.String
    securityMode: MessageSecurityMode
    securityPolicyUri: o6.String
    transportProfileUri: o6.String


@o6.datatype(nodeId="i=15534", browseName="DataTypeSchemaHeader", defaultEncodingId="i=15676", isAbstract=True)
class DataTypeSchemaHeader(Structure):
    namespaces: list[o6.String]
    structureDataTypes: list[StructureDescription]
    enumDataTypes: list[EnumDescription]
    simpleDataTypes: list[SimpleTypeDescription]


@o6.datatype(nodeId="i=15006", browseName="UABinaryFileDataType", defaultEncodingId="i=15422")
class UABinaryFileDataType(DataTypeSchemaHeader):
    namespaces: list[o6.String]
    structureDataTypes: list[StructureDescription]
    enumDataTypes: list[EnumDescription]
    simpleDataTypes: list[SimpleTypeDescription]
    schemaLocation: o6.String
    fileHeader: list[KeyValuePair]
    body: Any


@o6.enumtype(nodeId="i=15539", browseName="ConfigurationUpdateType")
class ConfigurationUpdateType(Enumeration):
    INSERT = o6.enumfield(1, name="Insert")
    REPLACE = o6.enumfield(2, name="Replace")
    INSERT_OR_REPLACE = o6.enumfield(3, name="InsertOrReplace")
    DELETE = o6.enumfield(4, name="Delete")


@o6.datatype(nodeId="i=15538", browseName="ConfigurationUpdateTargetType", defaultEncodingId="i=16541")
class ConfigurationUpdateTargetType(Structure):
    path: o6.String
    updateType: ConfigurationUpdateType


@o6.datatype(nodeId="i=15556", browseName="ApplicationIdentityDataType", defaultEncodingId="i=16543")
class ApplicationIdentityDataType(BaseConfigurationRecordDataType):
    name: o6.String
    recordProperties: list[KeyValuePair]
    applicationUri: o6.String
    applicationNames: list[o6.LocalizedText]
    additionalServers: list[ApplicationDescription]


@o6.datatype(nodeId="i=15557", browseName="EndpointDataType", defaultEncodingId="i=16544")
class EndpointDataType(BaseConfigurationRecordDataType):
    name: o6.String
    recordProperties: list[KeyValuePair]
    discoveryUrls: list[o6.String]
    networkName: o6.String
    port: o6.UInt16


@o6.datatype(nodeId="i=15558", browseName="ServerEndpointDataType", defaultEncodingId="i=16545")
class ServerEndpointDataType(EndpointDataType):
    name: o6.String
    recordProperties: list[KeyValuePair]
    discoveryUrls: list[o6.String]
    networkName: o6.String
    port: o6.UInt16
    endpointUrls: list[o6.String]
    securitySettingNames: list[o6.String]
    transportProfileUri: o6.String
    userTokenSettingNames: list[o6.String]
    reverseConnectUrls: list[o6.String]


@o6.datatype(nodeId="i=15559", browseName="SecuritySettingsDataType", defaultEncodingId="i=16546")
class SecuritySettingsDataType(BaseConfigurationRecordDataType):
    name: o6.String
    recordProperties: list[KeyValuePair]
    securityModes: list[MessageSecurityMode]
    securityPolicyUris: list[o6.String]
    certificateGroupName: o6.String


@o6.datatype(nodeId="i=15560", browseName="UserTokenSettingsDataType", defaultEncodingId="i=16547")
class UserTokenSettingsDataType(BaseConfigurationRecordDataType):
    name: o6.String
    recordProperties: list[KeyValuePair]
    tokenType: UserTokenType
    issuedTokenType: o6.String
    issuerEndpointUrl: o6.String
    securityPolicyUri: o6.String
    certificateGroupName: o6.String
    authorizationServiceName: o6.String


@o6.datatype(nodeId="i=15580", browseName="PublishedDataSetSourceDataType", defaultEncodingId="i=15678", isAbstract=True)
class PublishedDataSetSourceDataType(Structure):
    pass


@o6.datatype(nodeId="i=15581", browseName="PublishedDataItemsDataType", defaultEncodingId="i=15679")
class PublishedDataItemsDataType(PublishedDataSetSourceDataType):
    publishedData: list[PublishedVariableDataType]


@o6.datatype(nodeId="i=15582", browseName="PublishedEventsDataType", defaultEncodingId="i=15681")
class PublishedEventsDataType(PublishedDataSetSourceDataType):
    eventNotifier: o6.NodeId
    selectedFields: list[SimpleAttributeOperand]
    filter: ContentFilter


@o6.enumtype(nodeId="i=15583", browseName="DataSetFieldContentMask")
class DataSetFieldContentMask(UInt32):
    STATUS_CODE = o6.enumfield(0, name="StatusCode")
    SOURCE_TIMESTAMP = o6.enumfield(1, name="SourceTimestamp")
    SERVER_TIMESTAMP = o6.enumfield(2, name="ServerTimestamp")
    SOURCE_PICO_SECONDS = o6.enumfield(3, name="SourcePicoSeconds")
    SERVER_PICO_SECONDS = o6.enumfield(4, name="ServerPicoSeconds")
    RAW_DATA = o6.enumfield(5, name="RawData")


@o6.datatype(nodeId="i=15598", browseName="DataSetWriterTransportDataType", defaultEncodingId="i=15683", isAbstract=True)
class DataSetWriterTransportDataType(Structure):
    pass


@o6.datatype(nodeId="i=15605", browseName="DataSetWriterMessageDataType", defaultEncodingId="i=15688", isAbstract=True)
class DataSetWriterMessageDataType(Structure):
    pass


@o6.datatype(nodeId="i=15597", browseName="DataSetWriterDataType", defaultEncodingId="i=15682")
class DataSetWriterDataType(Structure):
    name: o6.String
    enabled: o6.Boolean
    dataSetWriterId: o6.UInt16
    dataSetFieldContentMask: DataSetFieldContentMask
    keyFrameCount: o6.UInt32
    dataSetName: o6.String
    dataSetWriterProperties: list[KeyValuePair]
    transportSettings: DataSetWriterTransportDataType
    messageSettings: DataSetWriterMessageDataType


@o6.datatype(nodeId="i=15609", browseName="PubSubGroupDataType", defaultEncodingId="i=15689", isAbstract=True)
class PubSubGroupDataType(Structure):
    name: o6.String
    enabled: o6.Boolean
    securityMode: MessageSecurityMode
    securityGroupId: o6.String
    securityKeyServices: list[EndpointDescription]
    maxNetworkMessageSize: o6.UInt32
    groupProperties: list[KeyValuePair]


@o6.datatype(nodeId="i=15611", browseName="WriterGroupTransportDataType", defaultEncodingId="i=15691", isAbstract=True)
class WriterGroupTransportDataType(Structure):
    pass


@o6.datatype(nodeId="i=15532", browseName="DatagramWriterGroupTransportDataType", defaultEncodingId="i=21155")
class DatagramWriterGroupTransportDataType(WriterGroupTransportDataType):
    messageRepeatCount: o6.Byte
    messageRepeatDelay: o6.Double


@o6.datatype(nodeId="i=15616", browseName="WriterGroupMessageDataType", defaultEncodingId="i=15693", isAbstract=True)
class WriterGroupMessageDataType(Structure):
    pass


@o6.datatype(nodeId="i=15480", browseName="WriterGroupDataType", defaultEncodingId="i=21150")
class WriterGroupDataType(PubSubGroupDataType):
    name: o6.String
    enabled: o6.Boolean
    securityMode: MessageSecurityMode
    securityGroupId: o6.String
    securityKeyServices: list[EndpointDescription]
    maxNetworkMessageSize: o6.UInt32
    groupProperties: list[KeyValuePair]
    writerGroupId: o6.UInt16
    publishingInterval: o6.Double
    keepAliveTime: o6.Double
    priority: o6.Byte
    localeIds: list[o6.String]
    headerLayoutUri: o6.String
    transportSettings: WriterGroupTransportDataType
    messageSettings: WriterGroupMessageDataType
    dataSetWriters: list[DataSetWriterDataType]


@o6.datatype(nodeId="i=15618", browseName="ConnectionTransportDataType", defaultEncodingId="i=15695", isAbstract=True)
class ConnectionTransportDataType(Structure):
    pass


@o6.datatype(nodeId="i=15007", browseName="BrokerConnectionTransportDataType", defaultEncodingId="i=15479")
class BrokerConnectionTransportDataType(ConnectionTransportDataType):
    resourceUri: o6.String
    authenticationProfileUri: o6.String


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
    criteriaType: IdentityCriteriaType
    criteria: o6.String


@o6.datatype(nodeId="i=15635", browseName="SubscribedDataSetMirrorDataType", defaultEncodingId="i=15713")
class SubscribedDataSetMirrorDataType(SubscribedDataSetDataType):
    parentNodeName: o6.String
    rolePermissions: list[RolePermissionType]


@o6.enumtype(nodeId="i=15642", browseName="UadpNetworkMessageContentMask")
class UadpNetworkMessageContentMask(UInt32):
    PUBLISHER_ID = o6.enumfield(0, name="PublisherId")
    GROUP_HEADER = o6.enumfield(1, name="GroupHeader")
    WRITER_GROUP_ID = o6.enumfield(2, name="WriterGroupId")
    GROUP_VERSION = o6.enumfield(3, name="GroupVersion")
    NETWORK_MESSAGE_NUMBER = o6.enumfield(4, name="NetworkMessageNumber")
    SEQUENCE_NUMBER = o6.enumfield(5, name="SequenceNumber")
    PAYLOAD_HEADER = o6.enumfield(6, name="PayloadHeader")
    TIMESTAMP = o6.enumfield(7, name="Timestamp")
    PICO_SECONDS = o6.enumfield(8, name="PicoSeconds")
    DATA_SET_CLASS_ID = o6.enumfield(9, name="DataSetClassId")
    PROMOTED_FIELDS = o6.enumfield(10, name="PromotedFields")


@o6.enumtype(nodeId="i=15646", browseName="UadpDataSetMessageContentMask")
class UadpDataSetMessageContentMask(UInt32):
    TIMESTAMP = o6.enumfield(0, name="Timestamp")
    PICO_SECONDS = o6.enumfield(1, name="PicoSeconds")
    STATUS = o6.enumfield(2, name="Status")
    MAJOR_VERSION = o6.enumfield(3, name="MajorVersion")
    MINOR_VERSION = o6.enumfield(4, name="MinorVersion")
    SEQUENCE_NUMBER = o6.enumfield(5, name="SequenceNumber")


@o6.datatype(nodeId="i=15652", browseName="UadpDataSetWriterMessageDataType", defaultEncodingId="i=15717")
class UadpDataSetWriterMessageDataType(DataSetWriterMessageDataType):
    dataSetMessageContentMask: UadpDataSetMessageContentMask
    configuredSize: o6.UInt16
    networkMessageNumber: o6.UInt16
    dataSetOffset: o6.UInt16


@o6.datatype(nodeId="i=15653", browseName="UadpDataSetReaderMessageDataType", defaultEncodingId="i=15718")
class UadpDataSetReaderMessageDataType(DataSetReaderMessageDataType):
    groupVersion: o6.UInt32
    networkMessageNumber: o6.UInt16
    dataSetOffset: o6.UInt16
    dataSetClassId: o6.Guid
    networkMessageContentMask: UadpNetworkMessageContentMask
    dataSetMessageContentMask: UadpDataSetMessageContentMask
    publishingInterval: o6.Double
    receiveOffset: o6.Double
    processingOffset: o6.Double


@o6.enumtype(nodeId="i=15654", browseName="JsonNetworkMessageContentMask")
class JsonNetworkMessageContentMask(UInt32):
    NETWORK_MESSAGE_HEADER = o6.enumfield(0, name="NetworkMessageHeader")
    DATA_SET_MESSAGE_HEADER = o6.enumfield(1, name="DataSetMessageHeader")
    SINGLE_DATA_SET_MESSAGE = o6.enumfield(2, name="SingleDataSetMessage")
    PUBLISHER_ID = o6.enumfield(3, name="PublisherId")
    DATA_SET_CLASS_ID = o6.enumfield(4, name="DataSetClassId")
    REPLY_TO = o6.enumfield(5, name="ReplyTo")
    WRITER_GROUP_NAME = o6.enumfield(6, name="WriterGroupName")


@o6.datatype(nodeId="i=15657", browseName="JsonWriterGroupMessageDataType", defaultEncodingId="i=15719")
class JsonWriterGroupMessageDataType(WriterGroupMessageDataType):
    networkMessageContentMask: JsonNetworkMessageContentMask


@o6.enumtype(nodeId="i=15658", browseName="JsonDataSetMessageContentMask")
class JsonDataSetMessageContentMask(UInt32):
    DATA_SET_WRITER_ID = o6.enumfield(0, name="DataSetWriterId")
    META_DATA_VERSION = o6.enumfield(1, name="MetaDataVersion")
    SEQUENCE_NUMBER = o6.enumfield(2, name="SequenceNumber")
    TIMESTAMP = o6.enumfield(3, name="Timestamp")
    STATUS = o6.enumfield(4, name="Status")
    MESSAGE_TYPE = o6.enumfield(5, name="MessageType")
    DATA_SET_WRITER_NAME = o6.enumfield(6, name="DataSetWriterName")
    FIELD_ENCODING1 = o6.enumfield(7, name="FieldEncoding1")
    PUBLISHER_ID = o6.enumfield(8, name="PublisherId")
    WRITER_GROUP_NAME = o6.enumfield(9, name="WriterGroupName")
    MINOR_VERSION = o6.enumfield(10, name="MinorVersion")
    FIELD_ENCODING2 = o6.enumfield(11, name="FieldEncoding2")


@o6.datatype(nodeId="i=15664", browseName="JsonDataSetWriterMessageDataType", defaultEncodingId="i=15724")
class JsonDataSetWriterMessageDataType(DataSetWriterMessageDataType):
    dataSetMessageContentMask: JsonDataSetMessageContentMask


@o6.datatype(nodeId="i=15665", browseName="JsonDataSetReaderMessageDataType", defaultEncodingId="i=15725")
class JsonDataSetReaderMessageDataType(DataSetReaderMessageDataType):
    networkMessageContentMask: JsonNetworkMessageContentMask
    dataSetMessageContentMask: JsonDataSetMessageContentMask


@o6.datatype(nodeId="i=15667", browseName="BrokerWriterGroupTransportDataType", defaultEncodingId="i=15727")
class BrokerWriterGroupTransportDataType(WriterGroupTransportDataType):
    queueName: o6.String
    resourceUri: o6.String
    authenticationProfileUri: o6.String
    requestedDeliveryGuarantee: BrokerTransportQualityOfService


@o6.datatype(nodeId="i=15669", browseName="BrokerDataSetWriterTransportDataType", defaultEncodingId="i=15729")
class BrokerDataSetWriterTransportDataType(DataSetWriterTransportDataType):
    queueName: o6.String
    resourceUri: o6.String
    authenticationProfileUri: o6.String
    requestedDeliveryGuarantee: BrokerTransportQualityOfService
    metaDataQueueName: o6.String
    metaDataUpdateTime: o6.Double


@o6.datatype(nodeId="i=15670", browseName="BrokerDataSetReaderTransportDataType", defaultEncodingId="i=15733")
class BrokerDataSetReaderTransportDataType(DataSetReaderTransportDataType):
    queueName: o6.String
    resourceUri: o6.String
    authenticationProfileUri: o6.String
    requestedDeliveryGuarantee: BrokerTransportQualityOfService
    metaDataQueueName: o6.String


@o6.enumtype(nodeId="i=15874", browseName="OverrideValueHandling")
class OverrideValueHandling(Enumeration):
    DISABLED = o6.enumfield(0, name="Disabled")
    LAST_USABLE_VALUE = o6.enumfield(1, name="LastUsableValue")
    OVERRIDE_VALUE = o6.enumfield(2, name="OverrideValue")


@o6.datatype(nodeId="i=14744", browseName="FieldTargetDataType", defaultEncodingId="i=14848")
class FieldTargetDataType(Structure):
    dataSetFieldId: o6.Guid
    receiverIndexRange: o6.String
    targetNodeId: o6.NodeId
    attributeId: o6.UInt32
    writeIndexRange: o6.String
    overrideValueHandling: OverrideValueHandling
    overrideValue: Any


@o6.datatype(nodeId="i=15631", browseName="TargetVariablesDataType", defaultEncodingId="i=15712")
class TargetVariablesDataType(SubscribedDataSetDataType):
    targetVariables: list[FieldTargetDataType]


@o6.datatype(nodeId="i=15901", browseName="SessionlessInvokeRequestType", defaultEncodingId="i=15903")
class SessionlessInvokeRequestType(Structure):
    urisVersion: o6.UInt32
    namespaceUris: list[o6.String]
    serverUris: list[o6.String]
    localeIds: list[o6.String]
    serviceId: o6.UInt32


@o6.enumtype(nodeId="i=15904", browseName="DataSetFieldFlags")
class DataSetFieldFlags(UInt16):
    PROMOTED_FIELD = o6.enumfield(0, name="PromotedField")


@o6.datatype(nodeId="i=14524", browseName="FieldMetaData", defaultEncodingId="i=14839")
class FieldMetaData(Structure):
    name: o6.String
    description: o6.LocalizedText
    fieldFlags: DataSetFieldFlags
    builtInType: o6.Byte
    dataType: o6.NodeId
    valueRank: o6.Int32
    arrayDimensions: list[o6.UInt32]
    maxStringLength: o6.UInt32
    dataSetFieldId: o6.Guid
    properties: list[KeyValuePair]


@o6.datatype(nodeId="i=14523", browseName="DataSetMetaDataType", defaultEncodingId="i=124")
class DataSetMetaDataType(DataTypeSchemaHeader):
    namespaces: list[o6.String]
    structureDataTypes: list[StructureDescription]
    enumDataTypes: list[EnumDescription]
    simpleDataTypes: list[SimpleTypeDescription]
    name: o6.String
    description: o6.LocalizedText
    fields: list[FieldMetaData]
    dataSetClassId: o6.Guid
    configurationVersion: ConfigurationVersionDataType


@o6.datatype(nodeId="i=15578", browseName="PublishedDataSetDataType", defaultEncodingId="i=15677")
class PublishedDataSetDataType(Structure):
    name: o6.String
    dataSetFolder: list[o6.String]
    dataSetMetaData: DataSetMetaDataType
    extensionFields: list[KeyValuePair]
    dataSetSource: PublishedDataSetSourceDataType


@o6.datatype(nodeId="i=15623", browseName="DataSetReaderDataType", defaultEncodingId="i=15703")
class DataSetReaderDataType(Structure):
    name: o6.String
    enabled: o6.Boolean
    publisherId: Any
    writerGroupId: o6.UInt16
    dataSetWriterId: o6.UInt16
    dataSetMetaData: DataSetMetaDataType
    dataSetFieldContentMask: DataSetFieldContentMask
    messageReceiveTimeout: o6.Double
    keyFrameCount: o6.UInt32
    headerLayoutUri: o6.String
    securityMode: MessageSecurityMode
    securityGroupId: o6.String
    securityKeyServices: list[EndpointDescription]
    dataSetReaderProperties: list[KeyValuePair]
    transportSettings: DataSetReaderTransportDataType
    messageSettings: DataSetReaderMessageDataType
    subscribedDataSet: SubscribedDataSetDataType


@o6.datatype(nodeId="i=15520", browseName="ReaderGroupDataType", defaultEncodingId="i=21153")
class ReaderGroupDataType(PubSubGroupDataType):
    name: o6.String
    enabled: o6.Boolean
    securityMode: MessageSecurityMode
    securityGroupId: o6.String
    securityKeyServices: list[EndpointDescription]
    maxNetworkMessageSize: o6.UInt32
    groupProperties: list[KeyValuePair]
    transportSettings: ReaderGroupTransportDataType
    messageSettings: ReaderGroupMessageDataType
    dataSetReaders: list[DataSetReaderDataType]


@o6.datatype(nodeId="i=15617", browseName="PubSubConnectionDataType", defaultEncodingId="i=15694")
class PubSubConnectionDataType(Structure):
    name: o6.String
    enabled: o6.Boolean
    publisherId: Any
    transportProfileUri: o6.String
    address: NetworkAddressDataType
    connectionProperties: list[KeyValuePair]
    transportSettings: ConnectionTransportDataType
    writerGroups: list[WriterGroupDataType]
    readerGroups: list[ReaderGroupDataType]


@o6.datatype(nodeId="i=15530", browseName="PubSubConfigurationDataType", defaultEncodingId="i=21154")
class PubSubConfigurationDataType(Structure):
    publishedDataSets: list[PublishedDataSetDataType]
    connections: list[PubSubConnectionDataType]
    enabled: o6.Boolean


@o6.datatype(nodeId="i=16307", browseName="AudioDataType", parent="i=15")
class AudioDataType:
    pass


@o6.datatype(nodeId="i=16313", browseName="AdditionalParametersType", defaultEncodingId="i=17537")
class AdditionalParametersType(Structure):
    parameters: list[KeyValuePair]


@o6.datatype(nodeId="i=17467", browseName="DatagramConnectionTransportDataType", defaultEncodingId="i=17468")
class DatagramConnectionTransportDataType(ConnectionTransportDataType):
    discoveryAddress: NetworkAddressDataType


@o6.datatype(nodeId="i=17545", browseName="RsaEncryptedSecret", parent="i=24")
class RsaEncryptedSecret:
    pass


@o6.datatype(nodeId="i=17546", browseName="EccEncryptedSecret", parent="i=24")
class EccEncryptedSecret:
    pass


@o6.datatype(nodeId="i=17548", browseName="EphemeralKeyType", defaultEncodingId="i=17549")
class EphemeralKeyType(Structure):
    publicKey: o6.ByteString
    signature: o6.ByteString


@o6.datatype(nodeId="i=17588", browseName="Index", parent="i=7")
class Index:
    pass


@o6.datatype(nodeId="i=17606", browseName="GenericAttributeValue", defaultEncodingId="i=17610")
class GenericAttributeValue(Structure):
    attributeId: o6.UInt32
    value: Any


@o6.datatype(nodeId="i=17607", browseName="GenericAttributes", defaultEncodingId="i=17611")
class GenericAttributes(NodeAttributes):
    specifiedAttributes: o6.UInt32
    displayName: o6.LocalizedText
    description: o6.LocalizedText
    writeMask: o6.UInt32
    userWriteMask: o6.UInt32
    attributeValues: list[GenericAttributeValue]


@o6.datatype(nodeId="i=17861", browseName="DecimalDataType", defaultEncodingId="i=17863")
class DecimalDataType(Structure):
    scale: o6.Int16
    value: o6.ByteString


@o6.datatype(nodeId="i=18593", browseName="ActionTargetDataType", defaultEncodingId="i=18598")
class ActionTargetDataType(Structure):
    actionTargetId: o6.UInt16
    name: o6.String
    description: o6.LocalizedText


@o6.datatype(nodeId="i=18594", browseName="PublishedActionDataType", defaultEncodingId="i=18599")
class PublishedActionDataType(PublishedDataSetSourceDataType):
    requestDataSetMetaData: DataSetMetaDataType
    actionTargets: list[ActionTargetDataType]


@o6.enumtype(nodeId="i=18595", browseName="ActionState")
class ActionState(Enumeration):
    IDLE = o6.enumfield(0, name="Idle")
    EXECUTING = o6.enumfield(1, name="Executing")
    DONE = o6.enumfield(2, name="Done")


@o6.datatype(nodeId="i=18597", browseName="ActionMethodDataType", defaultEncodingId="i=18600")
class ActionMethodDataType(Structure):
    objectId: o6.NodeId
    methodId: o6.NodeId


@o6.enumtype(nodeId="i=18646", browseName="SortOrderType")
class SortOrderType(Enumeration):
    ASCENDING = o6.enumfield(0, name="Ascending")
    DESCENDING = o6.enumfield(1, name="Descending")


@o6.datatype(nodeId="i=18648", browseName="SortRuleElement", defaultEncodingId="i=18650")
class SortRuleElement(Structure):
    sortOrder: SortOrderType
    eventField: SimpleAttributeOperand


@o6.datatype(nodeId="i=18649", browseName="ReadEventDetailsSorted", defaultEncodingId="i=18651")
class ReadEventDetailsSorted(ReadEventDetails):
    numValuesPerNode: o6.UInt32
    startTime: o6.DateTime
    endTime: o6.DateTime
    filter: EventFilter
    sortClause: list[SortRuleElement]


@o6.datatype(nodeId="i=18793", browseName="PublishedActionMethodDataType", defaultEncodingId="i=18795")
class PublishedActionMethodDataType(PublishedActionDataType):
    requestDataSetMetaData: DataSetMetaDataType
    actionTargets: list[ActionTargetDataType]
    actionMethods: list[ActionMethodDataType]


@o6.datatype(nodeId="i=18794", browseName="DtlsPubSubConnectionDataType", defaultEncodingId="i=18930")
class DtlsPubSubConnectionDataType(Structure):
    clientCipherSuite: o6.String
    serverCipherSuites: list[o6.String]
    zeroRTT: o6.Boolean
    certificateGroupId: o6.NodeId
    verifyClientCertificate: o6.Boolean


@o6.datatype(nodeId="i=18806", browseName="RationalNumber", defaultEncodingId="i=18815")
class RationalNumber(Structure):
    numerator: o6.Int32
    denominator: o6.UInt32


@o6.datatype(nodeId="i=18807", browseName="Vector", defaultEncodingId="i=18816", isAbstract=True)
class Vector(Structure):
    pass


@o6.datatype(nodeId="i=18808", browseName="3DVector", defaultEncodingId="i=18817")
class ThreeDVector(Vector):
    x: o6.Double
    y: o6.Double
    z: o6.Double


@o6.datatype(nodeId="i=18809", browseName="CartesianCoordinates", defaultEncodingId="i=18818", isAbstract=True)
class CartesianCoordinates(Structure):
    pass


@o6.datatype(nodeId="i=18810", browseName="3DCartesianCoordinates", defaultEncodingId="i=18819")
class ThreeDCartesianCoordinates(CartesianCoordinates):
    x: o6.Double
    y: o6.Double
    z: o6.Double


@o6.datatype(nodeId="i=18811", browseName="Orientation", defaultEncodingId="i=18820", isAbstract=True)
class Orientation(Structure):
    pass


@o6.datatype(nodeId="i=18812", browseName="3DOrientation", defaultEncodingId="i=18821")
class ThreeDOrientation(Orientation):
    a: o6.Double
    b: o6.Double
    c: o6.Double


@o6.datatype(nodeId="i=18813", browseName="Frame", defaultEncodingId="i=18822", isAbstract=True)
class Frame(Structure):
    pass


@o6.datatype(nodeId="i=18814", browseName="3DFrame", defaultEncodingId="i=18823")
class ThreeDFrame(Frame):
    cartesianCoordinates: ThreeDCartesianCoordinates
    orientation: ThreeDOrientation


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
    addressSubtype: o6.UInt32
    manAddress: o6.String
    txEnable: o6.Boolean
    addrLen: o6.UInt32
    ifSubtype: ManAddrIfSubtype
    ifId: o6.UInt32


@o6.datatype(nodeId="i=18954", browseName="LldpManagementAddressType", defaultEncodingId="i=19080")
class LldpManagementAddressType(Structure):
    addressSubtype: o6.UInt32
    address: o6.String
    ifSubtype: ManAddrIfSubtype
    ifId: o6.UInt32


@o6.datatype(nodeId="i=18955", browseName="LldpTlvType", defaultEncodingId="i=19081")
class LldpTlvType(Structure):
    tlvType: o6.UInt32
    tlvInfo: o6.ByteString


@o6.enumtype(nodeId="i=18956", browseName="LldpSystemCapabilitiesMap")
class LldpSystemCapabilitiesMap(UInt32):
    OTHER = o6.enumfield(0, name="Other")
    REPEATER = o6.enumfield(1, name="Repeater")
    BRIDGE = o6.enumfield(2, name="Bridge")
    WLAN_ACCESS_POINT = o6.enumfield(3, name="WlanAccessPoint")
    ROUTER = o6.enumfield(4, name="Router")
    TELEPHONE = o6.enumfield(5, name="Telephone")
    DOCSIS_CABLE_DEVICE = o6.enumfield(6, name="DocsisCableDevice")
    STATION_ONLY = o6.enumfield(7, name="StationOnly")
    CVLAN_COMPONENT = o6.enumfield(8, name="CvlanComponent")
    SVLAN_COMPONENT = o6.enumfield(9, name="SvlanComponent")
    TWO_PORT_MAC_RELAY = o6.enumfield(10, name="TwoPortMacRelay")


@o6.datatype(nodeId="i=19311", browseName="JsonNetworkMessage")
class JsonNetworkMessage(Structure):
    messageId: o6.String
    messageType: o6.String
    publisherId: o6.String
    writerGroupName: o6.String
    dataSetClassId: o6.String
    messages: list[Structure]


@o6.datatype(nodeId="i=19312", browseName="JsonDataSetMessage")
class JsonDataSetMessage(Structure):
    dataSetWriterId: o6.UInt16
    dataSetWriterName: o6.String
    publisherId: o6.String
    writerGroupName: o6.String
    sequenceNumber: o6.UInt32
    metaDataVersion: ConfigurationVersionDataType
    minorVersion: o6.UInt32
    timestamp: o6.DateTime
    status: o6.StatusCode
    messageType: o6.String
    payload: Structure


@o6.datatype(nodeId="i=19313", browseName="JsonDataSetMetaDataMessage")
class JsonDataSetMetaDataMessage(Structure):
    messageId: o6.String
    messageType: o6.String
    publisherId: o6.String
    dataSetWriterId: o6.UInt16
    writerGroupName: o6.String
    dataSetWriterName: o6.String
    timestamp: o6.DateTime
    metaData: DataSetMetaDataType


@o6.datatype(nodeId="i=19314", browseName="JsonApplicationDescriptionMessage")
class JsonApplicationDescriptionMessage(Structure):
    messageId: o6.String
    messageType: o6.String
    publisherId: o6.String
    timestamp: o6.DateTime
    description: ApplicationDescription
    serverCapabilities: list[o6.String]


@o6.datatype(nodeId="i=19315", browseName="JsonServerEndpointsMessage")
class JsonServerEndpointsMessage(Structure):
    messageId: o6.String
    messageType: o6.String
    publisherId: o6.String
    timestamp: o6.DateTime
    description: ApplicationDescription
    endpoints: list[EndpointDescription]


@o6.datatype(nodeId="i=19316", browseName="JsonStatusMessage")
class JsonStatusMessage(Structure):
    messageId: o6.String
    messageType: o6.String
    publisherId: o6.String
    timestamp: o6.DateTime
    isCyclic: o6.Boolean
    status: PubSubState
    nextReportTime: o6.DateTime


@o6.datatype(nodeId="i=19317", browseName="JsonPubSubConnectionMessage")
class JsonPubSubConnectionMessage(Structure):
    messageId: o6.String
    messageType: o6.String
    publisherId: o6.String
    timestamp: o6.DateTime
    connection: PubSubConnectionDataType


@o6.datatype(nodeId="i=19318", browseName="JsonActionMetaDataMessage")
class JsonActionMetaDataMessage(Structure):
    messageId: o6.String
    messageType: o6.String
    publisherId: o6.String
    dataSetWriterId: o6.UInt16
    dataSetWriterName: o6.String
    timestamp: o6.DateTime
    actionTargets: list[ActionTargetDataType]
    request: DataSetMetaDataType
    response: DataSetMetaDataType
    actionMethods: list[ActionMethodDataType]


@o6.datatype(nodeId="i=19319", browseName="JsonActionResponderMessage")
class JsonActionResponderMessage(Structure):
    messageId: o6.String
    messageType: o6.String
    publisherId: o6.String
    timestamp: o6.DateTime
    connection: PubSubConnectionDataType


@o6.datatype(nodeId="i=19320", browseName="JsonActionNetworkMessage")
class JsonActionNetworkMessage(Structure):
    messageId: o6.String
    messageType: o6.String
    publisherId: o6.String
    timestamp: o6.DateTime
    responseAddress: o6.String
    correlationData: o6.ByteString
    requestorId: o6.String
    timeoutHint: o6.Double
    messages: list[Structure]


@o6.datatype(nodeId="i=19321", browseName="JsonActionRequestMessage")
class JsonActionRequestMessage(Structure):
    dataSetWriterId: o6.UInt16
    actionTargetId: o6.UInt16
    dataSetWriterName: o6.String
    writerGroupName: o6.String
    metaDataVersion: ConfigurationVersionDataType
    minorVersion: o6.UInt32
    timestamp: o6.DateTime
    messageType: o6.String
    requestId: o6.UInt16
    actionState: ActionState
    payload: Structure


@o6.datatype(nodeId="i=19322", browseName="JsonActionResponseMessage")
class JsonActionResponseMessage(Structure):
    dataSetWriterId: o6.UInt16
    actionTargetId: o6.UInt16
    dataSetWriterName: o6.String
    writerGroupName: o6.String
    metaDataVersion: ConfigurationVersionDataType
    minorVersion: o6.UInt32
    timestamp: o6.DateTime
    status: o6.StatusCode
    messageType: o6.String
    requestId: o6.UInt16
    actionState: ActionState
    payload: Structure


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
    traceId: o6.Guid
    spanId: o6.UInt64


@o6.datatype(nodeId="i=19747", browseName="TraceContextDataType", defaultEncodingId="i=19755")
class TraceContextDataType(SpanContextDataType):
    traceId: o6.Guid
    spanId: o6.UInt64
    parentSpanId: o6.UInt64
    parentIdentifier: o6.String


@o6.datatype(nodeId="i=19748", browseName="NameValuePair", defaultEncodingId="i=19756")
class NameValuePair(Structure):
    name: o6.String
    value: Any


@o6.datatype(nodeId="i=19361", browseName="LogRecord", defaultEncodingId="i=19379")
class LogRecord(Structure):
    time: o6.DateTime
    severity: o6.UInt16
    eventType: o6.NodeId | None
    sourceNode: o6.NodeId | None
    sourceName: o6.String | None
    message: o6.LocalizedText
    traceContext: TraceContextDataType | None
    additionalData: list[NameValuePair] | None


@o6.datatype(nodeId="i=19745", browseName="LogRecordsDataType", defaultEncodingId="i=19753")
class LogRecordsDataType(Structure):
    logRecordArray: list[LogRecord]


@o6.enumtype(nodeId="i=19749", browseName="LogRecordMask")
class LogRecordMask(UInt32):
    EVENT_TYPE = o6.enumfield(0, name="EventType")
    SOURCE_NODE = o6.enumfield(1, name="SourceNode")
    SOURCE_NAME = o6.enumfield(2, name="SourceName")
    TRACE_CONTEXT = o6.enumfield(3, name="TraceContext")
    ADDITIONAL_DATA = o6.enumfield(4, name="AdditionalData")


@o6.enumtype(nodeId="i=20408", browseName="DataSetOrderingType")
class DataSetOrderingType(Enumeration):
    UNDEFINED = o6.enumfield(0, name="Undefined")
    ASCENDING_WRITER_ID = o6.enumfield(1, name="AscendingWriterId")
    ASCENDING_WRITER_ID_SINGLE = o6.enumfield(2, name="AscendingWriterIdSingle")


@o6.datatype(nodeId="i=15645", browseName="UadpWriterGroupMessageDataType", defaultEncodingId="i=15715")
class UadpWriterGroupMessageDataType(WriterGroupMessageDataType):
    groupVersion: o6.UInt32
    dataSetOrdering: DataSetOrderingType
    networkMessageContentMask: UadpNetworkMessageContentMask
    samplingOffset: o6.Double
    publishingOffset: list[o6.Double]


@o6.datatype(nodeId="i=20998", browseName="VersionTime", parent="i=7")
class VersionTime:
    pass


@o6.datatype(nodeId="i=20999", browseName="SessionlessInvokeResponseType", defaultEncodingId="i=21001")
class SessionlessInvokeResponseType(Structure):
    namespaceUris: list[o6.String]
    serverUris: list[o6.String]
    serviceId: o6.UInt32


@o6.datatype(nodeId="i=23468", browseName="AliasNameDataType", defaultEncodingId="i=23499")
class AliasNameDataType(Structure):
    aliasName: o6.QualifiedName
    referencedNodes: list[o6.ExpandedNodeId]


@o6.datatype(nodeId="i=23497", browseName="ReadAnnotationDataDetails", defaultEncodingId="i=23500")
class ReadAnnotationDataDetails(HistoryReadDetails):
    reqTimes: list[o6.DateTime]


@o6.datatype(nodeId="i=23498", browseName="CurrencyUnitType", defaultEncodingId="i=23507")
class CurrencyUnitType(Structure):
    numericCode: o6.Int16
    exponent: o6.SByte
    alphabeticCode: o6.String
    currency: o6.LocalizedText


@o6.enumtype(nodeId="i=23564", browseName="TrustListValidationOptions")
class TrustListValidationOptions(UInt32):
    SUPPRESS_CERTIFICATE_EXPIRED = o6.enumfield(0, name="SuppressCertificateExpired")
    SUPPRESS_HOST_NAME_INVALID = o6.enumfield(1, name="SuppressHostNameInvalid")
    SUPPRESS_REVOCATION_STATUS_UNKNOWN = o6.enumfield(2, name="SuppressRevocationStatusUnknown")
    SUPPRESS_ISSUER_CERTIFICATE_EXPIRED = o6.enumfield(3, name="SuppressIssuerCertificateExpired")
    SUPPRESS_ISSUER_REVOCATION_STATUS_UNKNOWN = o6.enumfield(4, name="SuppressIssuerRevocationStatusUnknown")
    CHECK_REVOCATION_STATUS_ONLINE = o6.enumfield(5, name="CheckRevocationStatusOnline")
    CHECK_REVOCATION_STATUS_OFFLINE = o6.enumfield(6, name="CheckRevocationStatusOffline")


@o6.datatype(nodeId="i=15436", browseName="CertificateGroupDataType", defaultEncodingId="i=16540")
class CertificateGroupDataType(BaseConfigurationRecordDataType):
    name: o6.String
    recordProperties: list[KeyValuePair]
    purpose: o6.NodeId
    certificateTypes: list[o6.NodeId]
    isCertificateAssigned: list[o6.Boolean]
    validationOptions: TrustListValidationOptions


@o6.datatype(nodeId="i=23599", browseName="StandaloneSubscribedDataSetRefDataType", defaultEncodingId="i=23851")
class StandaloneSubscribedDataSetRefDataType(SubscribedDataSetDataType):
    dataSetName: o6.String


@o6.datatype(nodeId="i=23600", browseName="StandaloneSubscribedDataSetDataType", defaultEncodingId="i=23852")
class StandaloneSubscribedDataSetDataType(SubscribedDataSetDataType):
    name: o6.String
    dataSetFolder: list[o6.String]
    dataSetMetaData: DataSetMetaDataType
    subscribedDataSet: SubscribedDataSetDataType


@o6.datatype(nodeId="i=23601", browseName="SecurityGroupDataType", defaultEncodingId="i=23853")
class SecurityGroupDataType(Structure):
    name: o6.String
    securityGroupFolder: list[o6.String]
    keyLifetime: o6.Double
    securityPolicyUri: o6.String
    maxFutureKeyCount: o6.UInt32
    maxPastKeyCount: o6.UInt32
    securityGroupId: o6.String
    rolePermissions: list[RolePermissionType]
    groupProperties: list[KeyValuePair]


@o6.datatype(nodeId="i=23603", browseName="QosDataType", defaultEncodingId="i=23855", isAbstract=True)
class QosDataType(Structure):
    pass


@o6.datatype(nodeId="i=23604", browseName="TransmitQosDataType", defaultEncodingId="i=23856", isAbstract=True)
class TransmitQosDataType(QosDataType):
    pass


@o6.datatype(nodeId="i=23605", browseName="TransmitQosPriorityDataType", defaultEncodingId="i=23857")
class TransmitQosPriorityDataType(TransmitQosDataType):
    priorityLabel: o6.String


@o6.datatype(nodeId="i=23608", browseName="ReceiveQosDataType", defaultEncodingId="i=23860", isAbstract=True)
class ReceiveQosDataType(QosDataType):
    pass


@o6.datatype(nodeId="i=23609", browseName="ReceiveQosPriorityDataType", defaultEncodingId="i=23861")
class ReceiveQosPriorityDataType(ReceiveQosDataType):
    priorityLabel: o6.String


@o6.datatype(nodeId="i=23612", browseName="DatagramConnectionTransport2DataType", defaultEncodingId="i=23864")
class DatagramConnectionTransport2DataType(DatagramConnectionTransportDataType):
    discoveryAddress: NetworkAddressDataType
    discoveryAnnounceRate: o6.UInt32
    discoveryMaxMessageSize: o6.UInt32
    qosCategory: o6.String
    datagramQos: list[QosDataType]


@o6.datatype(nodeId="i=23613", browseName="DatagramWriterGroupTransport2DataType", defaultEncodingId="i=23865")
class DatagramWriterGroupTransport2DataType(DatagramWriterGroupTransportDataType):
    messageRepeatCount: o6.Byte
    messageRepeatDelay: o6.Double
    address: NetworkAddressDataType
    qosCategory: o6.String
    datagramQos: list[TransmitQosDataType]
    discoveryAnnounceRate: o6.UInt32
    topic: o6.String


@o6.datatype(nodeId="i=23614", browseName="DatagramDataSetReaderTransportDataType", defaultEncodingId="i=23866")
class DatagramDataSetReaderTransportDataType(DataSetReaderTransportDataType):
    address: NetworkAddressDataType
    qosCategory: o6.String
    datagramQos: list[ReceiveQosDataType]
    topic: o6.String


@o6.datatype(nodeId="i=23724", browseName="ServiceCertificateDataType", defaultEncodingId="i=23725")
class ServiceCertificateDataType(Structure):
    certificate: o6.ByteString
    issuers: list[o6.ByteString]
    validFrom: o6.DateTime
    validTo: o6.DateTime


@o6.datatype(nodeId="i=23744", browseName="AuthorizationServiceConfigurationDataType", defaultEncodingId="i=23755")
class AuthorizationServiceConfigurationDataType(BaseConfigurationRecordDataType):
    name: o6.String
    recordProperties: list[KeyValuePair]
    serviceUri: o6.String
    serviceCertificates: list[ServiceCertificateDataType]
    issuerEndpointSettings: o6.String


@o6.datatype(nodeId="i=23743", browseName="ApplicationConfigurationDataType", defaultEncodingId="i=23754")
class ApplicationConfigurationDataType(BaseConfigurationDataType):
    configurationVersion: o6.UInt32
    configurationProperties: list[KeyValuePair]
    applicationIdentity: ApplicationIdentityDataType
    certificateGroups: list[CertificateGroupDataType]
    serverEndpoints: list[ServerEndpointDataType]
    clientEndpoints: list[EndpointDataType]
    securitySettings: list[SecuritySettingsDataType]
    userTokenSettings: list[UserTokenSettingsDataType]
    authorizationServices: list[AuthorizationServiceConfigurationDataType]


@o6.datatype(nodeId="i=23751", browseName="UriString", parent="i=12")
class UriString:
    pass


@o6.datatype(nodeId="i=23903", browseName="NumberRange", defaultEncodingId="i=24250")
class NumberRange(Structure):
    low: BaseDataType
    high: BaseDataType


@o6.datatype(nodeId="i=24033", browseName="ProgramDiagnostic2DataType", defaultEncodingId="i=24034")
class ProgramDiagnostic2DataType(Structure):
    createSessionId: o6.NodeId
    createClientName: o6.String
    invocationCreationTime: o6.DateTime
    lastTransitionTime: o6.DateTime
    lastMethodCall: o6.String
    lastMethodSessionId: o6.NodeId
    lastMethodInputArguments: list[Argument]
    lastMethodOutputArguments: list[Argument]
    lastMethodInputValues: list[Any]
    lastMethodOutputValues: list[Any]
    lastMethodCallTime: o6.DateTime
    lastMethodReturnStatus: o6.StatusCode


@o6.datatype(nodeId="i=24051", browseName="AliasNameVerboseDataType", defaultEncodingId="i=24262")
class AliasNameVerboseDataType(Structure):
    aliasName: o6.QualifiedName
    referencedNodes: list[o6.ExpandedNodeId]
    serverUris: list[o6.String]
    aliasNameCategoryId: o6.NodeId


@o6.datatype(nodeId="i=24105", browseName="PortableQualifiedName", defaultEncodingId="i=24108")
class PortableQualifiedName(Structure):
    namespaceUri: o6.String
    name: o6.String


@o6.datatype(nodeId="i=24106", browseName="PortableNodeId", defaultEncodingId="i=24109")
class PortableNodeId(Structure):
    namespaceUri: o6.String
    identifier: o6.NodeId


@o6.datatype(nodeId="i=24052", browseName="AliasCategoryUpdateDataType", defaultEncodingId="i=24338")
class AliasCategoryUpdateDataType(Structure):
    category: PortableNodeId
    lastChange: o6.UInt32


@o6.datatype(nodeId="i=24053", browseName="AliasUpdateDataType", defaultEncodingId="i=24339")
class AliasUpdateDataType(Structure):
    applicationUri: o6.String
    categories: list[AliasCategoryUpdateDataType]


@o6.datatype(nodeId="i=24107", browseName="UnsignedRationalNumber", defaultEncodingId="i=24110")
class UnsignedRationalNumber(Structure):
    numerator: o6.UInt32
    denominator: o6.UInt32


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


@o6.enumtype(nodeId="i=24277", browseName="PasswordOptionsMask")
class PasswordOptionsMask(UInt32):
    SUPPORT_INITIAL_PASSWORD_CHANGE = o6.enumfield(0, name="SupportInitialPasswordChange")
    SUPPORT_DISABLE_USER = o6.enumfield(1, name="SupportDisableUser")
    SUPPORT_DISABLE_DELETE_FOR_USER = o6.enumfield(2, name="SupportDisableDeleteForUser")
    SUPPORT_NO_CHANGE_FOR_USER = o6.enumfield(3, name="SupportNoChangeForUser")
    SUPPORT_DESCRIPTION_FOR_USER = o6.enumfield(4, name="SupportDescriptionForUser")
    REQUIRES_UPPER_CASE_CHARACTERS = o6.enumfield(5, name="RequiresUpperCaseCharacters")
    REQUIRES_LOWER_CASE_CHARACTERS = o6.enumfield(6, name="RequiresLowerCaseCharacters")
    REQUIRES_DIGIT_CHARACTERS = o6.enumfield(7, name="RequiresDigitCharacters")
    REQUIRES_SPECIAL_CHARACTERS = o6.enumfield(8, name="RequiresSpecialCharacters")


@o6.enumtype(nodeId="i=24279", browseName="UserConfigurationMask")
class UserConfigurationMask(UInt32):
    NO_DELETE = o6.enumfield(0, name="NoDelete")
    DISABLED = o6.enumfield(1, name="Disabled")
    NO_CHANGE_BY_USER = o6.enumfield(2, name="NoChangeByUser")
    MUST_CHANGE_PASSWORD = o6.enumfield(3, name="MustChangePassword")


@o6.datatype(nodeId="i=24281", browseName="UserManagementDataType", defaultEncodingId="i=24292")
class UserManagementDataType(Structure):
    userName: o6.String
    userConfiguration: UserConfigurationMask
    description: o6.String


@o6.datatype(nodeId="i=25220", browseName="PriorityMappingEntryType", defaultEncodingId="i=25239")
class PriorityMappingEntryType(Structure):
    mappingUri: o6.String
    priorityLabel: o6.String
    priorityValue_PCP: o6.Byte
    priorityValue_DSCP: o6.UInt32


@o6.datatype(nodeId="i=25269", browseName="PublishedDataSetCustomSourceDataType", defaultEncodingId="i=25529")
class PublishedDataSetCustomSourceDataType(PublishedDataSetSourceDataType):
    cyclicDataSet: o6.Boolean


@o6.datatype(nodeId="i=25270", browseName="PubSubKeyPushTargetDataType", defaultEncodingId="i=25530")
class PubSubKeyPushTargetDataType(Structure):
    applicationUri: o6.String
    pushTargetFolder: list[o6.String]
    endpointUrl: o6.String
    securityPolicyUri: o6.String
    userTokenType: UserTokenPolicy
    requestedKeyCount: o6.UInt16
    retryInterval: o6.Double
    pushTargetProperties: list[KeyValuePair]
    securityGroups: list[o6.String]


@o6.datatype(nodeId="i=23602", browseName="PubSubConfiguration2DataType", defaultEncodingId="i=23854")
class PubSubConfiguration2DataType(PubSubConfigurationDataType):
    publishedDataSets: list[PublishedDataSetDataType]
    connections: list[PubSubConnectionDataType]
    enabled: o6.Boolean
    subscribedDataSets: list[StandaloneSubscribedDataSetDataType]
    dataSetClasses: list[DataSetMetaDataType]
    defaultSecurityKeyServices: list[EndpointDescription]
    securityGroups: list[SecurityGroupDataType]
    pubSubKeyPushTargets: list[PubSubKeyPushTargetDataType]
    configurationVersion: o6.UInt32
    configurationProperties: list[KeyValuePair]


@o6.enumtype(nodeId="i=25517", browseName="PubSubConfigurationRefMask")
class PubSubConfigurationRefMask(UInt32):
    ELEMENT_ADD = o6.enumfield(0, name="ElementAdd")
    ELEMENT_MATCH = o6.enumfield(1, name="ElementMatch")
    ELEMENT_MODIFY = o6.enumfield(2, name="ElementModify")
    ELEMENT_REMOVE = o6.enumfield(3, name="ElementRemove")
    REFERENCE_WRITER = o6.enumfield(4, name="ReferenceWriter")
    REFERENCE_READER = o6.enumfield(5, name="ReferenceReader")
    REFERENCE_WRITER_GROUP = o6.enumfield(6, name="ReferenceWriterGroup")
    REFERENCE_READER_GROUP = o6.enumfield(7, name="ReferenceReaderGroup")
    REFERENCE_CONNECTION = o6.enumfield(8, name="ReferenceConnection")
    REFERENCE_PUB_DATASET = o6.enumfield(9, name="ReferencePubDataset")
    REFERENCE_SUB_DATASET = o6.enumfield(10, name="ReferenceSubDataset")
    REFERENCE_SECURITY_GROUP = o6.enumfield(11, name="ReferenceSecurityGroup")
    REFERENCE_PUSH_TARGET = o6.enumfield(12, name="ReferencePushTarget")


@o6.datatype(nodeId="i=25519", browseName="PubSubConfigurationRefDataType", defaultEncodingId="i=25531")
class PubSubConfigurationRefDataType(Structure):
    configurationMask: PubSubConfigurationRefMask
    elementIndex: o6.UInt16
    connectionIndex: o6.UInt16
    groupIndex: o6.UInt16


@o6.datatype(nodeId="i=25520", browseName="PubSubConfigurationValueDataType", defaultEncodingId="i=25532")
class PubSubConfigurationValueDataType(Structure):
    configurationElement: PubSubConfigurationRefDataType
    name: o6.String
    identifier: Any


@o6.datatype(nodeId="i=25726", browseName="EncodedTicket", parent="i=12")
class EncodedTicket:
    pass


@o6.datatype(nodeId="i=31917", browseName="Handle", parent="i=7")
class Handle:
    pass


@o6.datatype(nodeId="i=31918", browseName="TrimmedString", parent="i=12")
class TrimmedString:
    pass


@o6.enumtype(nodeId="i=32251", browseName="AlarmMask")
class AlarmMask(UInt16):
    ACTIVE = o6.enumfield(0, name="Active")
    UNACKNOWLEDGED = o6.enumfield(1, name="Unacknowledged")
    UNCONFIRMED = o6.enumfield(2, name="Unconfirmed")


@o6.datatype(nodeId="i=32285", browseName="TransactionErrorType", defaultEncodingId="i=32382")
class TransactionErrorType(Structure):
    targetId: o6.NodeId
    error: o6.StatusCode
    message: o6.LocalizedText


@o6.enumtype(nodeId="i=32417", browseName="RedundantServerMode")
class RedundantServerMode(Enumeration):
    PRIMARY_WITH_BACKUP = o6.enumfield(0, name="PrimaryWithBackup")
    PRIMARY_ONLY = o6.enumfield(1, name="PrimaryOnly")
    BACKUP_READY = o6.enumfield(2, name="BackupReady")
    BACKUP_NOT_READY = o6.enumfield(3, name="BackupNotReady")


@o6.datatype(nodeId="i=32421", browseName="BitFieldDefinition", defaultEncodingId="i=32422")
class BitFieldDefinition(Structure):
    name: o6.String
    description: o6.LocalizedText
    reserved: o6.Boolean
    startingBitPosition: o6.UInt32
    endingBitPosition: o6.UInt32


@o6.datatype(nodeId="i=32434", browseName="AnnotationDataType", defaultEncodingId="i=32560")
class AnnotationDataType(Structure):
    annotation: o6.String
    discipline: o6.String
    uri: o6.String


@o6.datatype(nodeId="i=32435", browseName="LinearConversionDataType", defaultEncodingId="i=32561")
class LinearConversionDataType(Structure):
    initialAddend: o6.Float
    multiplicand: o6.Float
    divisor: o6.Float
    finalAddend: o6.Float


@o6.enumtype(nodeId="i=32436", browseName="ConversionLimitEnum")
class ConversionLimitEnum(Enumeration):
    NO_CONVERSION = o6.enumfield(0, name="NoConversion")
    LIMITED = o6.enumfield(1, name="Limited")
    UNLIMITED = o6.enumfield(2, name="Unlimited")


@o6.datatype(nodeId="i=32438", browseName="QuantityDimension", defaultEncodingId="i=32562")
class QuantityDimension(Structure):
    massExponent: o6.SByte
    lengthExponent: o6.SByte
    timeExponent: o6.SByte
    electricCurrentExponent: o6.SByte
    amountOfSubstanceExponent: o6.SByte
    luminousIntensityExponent: o6.SByte
    absoluteTemperatureExponent: o6.SByte
    dimensionlessExponent: o6.SByte


@o6.datatype(nodeId="i=32659", browseName="ReferenceDescriptionDataType", defaultEncodingId="i=32661")
class ReferenceDescriptionDataType(Structure):
    sourceNode: o6.NodeId
    referenceType: o6.NodeId
    isForward: o6.Boolean
    targetNode: o6.ExpandedNodeId


@o6.datatype(nodeId="i=32660", browseName="ReferenceListEntryDataType", defaultEncodingId="i=32662")
class ReferenceListEntryDataType(Structure):
    referenceType: o6.NodeId
    isForward: o6.Boolean
    targetNode: o6.ExpandedNodeId


@o6.datatype(nodeId="i=32799", browseName="ReadEventDetails2", defaultEncodingId="i=32800")
class ReadEventDetails2(ReadEventDetails):
    numValuesPerNode: o6.UInt32
    startTime: o6.DateTime
    endTime: o6.DateTime
    filter: EventFilter
    readModified: o6.Boolean


@o6.datatype(nodeId="i=32824", browseName="HistoryModifiedEvent", defaultEncodingId="i=32825")
class HistoryModifiedEvent(HistoryEvent):
    events: list[HistoryEventFieldList]
    modificationInfos: list[ModificationInfo]


del Any, TYPE_CHECKING, uuid, o6, ns0_reftypes
