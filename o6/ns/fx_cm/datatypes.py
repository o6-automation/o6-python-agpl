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

"""Generated OPC UA fx_cm namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.fx_data as fx_data
import o6.ns.ns0 as ns0
from . import reftypes as fx_cm_reftypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.datatype(nodeId="ns=fx_cm;i=1035", browseName="PortableKeyValuePair", defaultEncodingId="ns=fx_cm;i=1114")
class PortableKeyValuePair(ns0.datatypes.Structure):
    key: ns0.datatypes.PortableQualifiedName
    value: Any


@o6.datatype(nodeId="ns=fx_cm;i=1036", browseName="ServerAddressDataType", defaultEncodingId="ns=fx_cm;i=1117")
class ServerAddressDataType(ns0.datatypes.Structure):
    address: o6.String
    securityMode: ns0.datatypes.MessageSecurityMode
    securityPolicyUri: o6.String
    serverUri: o6.String


@o6.datatype(nodeId="ns=fx_cm;i=1051", browseName="PortableRelativePathElement", defaultEncodingId="ns=fx_cm;i=1222")
class PortableRelativePathElement(ns0.datatypes.Structure):
    referenceTypeId: ns0.datatypes.PortableNodeId
    isInverse: o6.Boolean
    includeSubtypes: o6.Boolean
    targetName: ns0.datatypes.PortableQualifiedName


@o6.datatype(nodeId="ns=fx_cm;i=1047", browseName="PortableRelativePath", defaultEncodingId="ns=fx_cm;i=1159")
class PortableRelativePath(ns0.datatypes.Structure):
    elements: list[PortableRelativePathElement]


@o6.enumtype(nodeId="ns=fx_cm;i=3001", browseName="FxEditEnum")
class FxEditEnum(ns0.datatypes.Enumeration):
    START_EDITING = o6.enumfield(0, name="StartEditing")
    COMMIT_UPDATES = o6.enumfield(1, name="CommitUpdates")
    DISCARD_UPDATES = o6.enumfield(2, name="DiscardUpdates")


@o6.enumtype(nodeId="ns=fx_cm;i=3002", browseName="FxProcessEnum")
class FxProcessEnum(ns0.datatypes.Enumeration):
    ACTION_ESTABLISH_CONNECTIONS_ENABLED = o6.enumfield(0, name="ActionEstablishConnectionsEnabled")
    ACTION_ESTABLISH_CONNECTIONS_DISABLED = o6.enumfield(1, name="ActionEstablishConnectionsDisabled")
    ACTION_ESTABLISH_CONNECTIONS = o6.enumfield(2, name="ActionEstablishConnections")
    ACTION_REMOVE_CONNECTIONS = o6.enumfield(3, name="ActionRemoveConnections")
    ACTION_ENABLE_CONNECTIONS = o6.enumfield(4, name="ActionEnableConnections")
    ACTION_DISABLE_CONNECTIONS = o6.enumfield(5, name="ActionDisableConnections")


@o6.datatype(nodeId="ns=fx_cm;i=3004", browseName="CommunicationFlowQosDataType", defaultEncodingId="ns=fx_cm;i=5017")
class CommunicationFlowQosDataType(ns0.datatypes.Structure):
    qosCategory: o6.String
    transmitQos: list[ns0.datatypes.TransmitQosDataType]
    receiveQos: list[ns0.datatypes.ReceiveQosDataType]


@o6.enumtype(nodeId="ns=fx_cm;i=3009", browseName="LastActivityMask")
class LastActivityMask:
    ESTABLISH_ENABLED = o6.enumfield(0, name="EstablishEnabled")
    ESTABLISH_DISABLED = o6.enumfield(1, name="EstablishDisabled")
    ESTABLISH = o6.enumfield(2, name="Establish")
    REMOVE = o6.enumfield(3, name="Remove")
    ENABLE = o6.enumfield(4, name="Enable")
    DISABLE = o6.enumfield(5, name="Disable")
    ERROR = o6.enumfield(15, name="Error")


@o6.enumtype(nodeId="ns=fx_cm;i=3011", browseName="ConnectionStateEnum")
class ConnectionStateEnum(ns0.datatypes.Enumeration):
    CONNECTION_NOT_MONITORED = o6.enumfield(0, name="ConnectionNotMonitored")
    CONNECTION_NOT_ESTABLISHED = o6.enumfield(1, name="ConnectionNotEstablished")
    CONNECTION_INITIAL = o6.enumfield(2, name="ConnectionInitial")
    CONNECTION_READY = o6.enumfield(3, name="ConnectionReady")
    CONNECTION_PRE_OPERATIONAL = o6.enumfield(4, name="ConnectionPreOperational")
    CONNECTION_OPERATIONAL = o6.enumfield(5, name="ConnectionOperational")
    CONNECTION_ERROR = o6.enumfield(6, name="ConnectionError")


@o6.datatype(nodeId="ns=fx_cm;i=3012", browseName="PortableNodeIdentifier", defaultEncodingId="ns=fx_cm;i=5057")
class PortableNodeIdentifier(ns0.datatypes.Union):
    node: ns0.datatypes.PortableNodeId
    alias: o6.String
    identifierBrowsePath: PortableRelativePath


@o6.datatype(nodeId="ns=fx_cm;i=3005", browseName="PortableNodeIdentifierValuePair", defaultEncodingId="ns=fx_cm;i=5016")
class PortableNodeIdentifierValuePair(ns0.datatypes.Structure):
    key: PortableNodeIdentifier
    arrayIndex: list[o6.UInt32]
    value: Any


@o6.datatype(nodeId="ns=fx_cm;i=3006", browseName="NodeIdTranslationDataType", defaultEncodingId="ns=fx_cm;i=5025")
class NodeIdTranslationDataType(ns0.datatypes.Structure):
    nodePlaceholder: o6.NodeId
    portableNode: PortableNodeIdentifier


@o6.enumtype(nodeId="ns=fx_cm;i=3015", browseName="FxErrorEnum")
class FxErrorEnum(ns0.datatypes.Enumeration):
    NO_ERROR = o6.enumfield(0, name="NoError")
    UNKNOWN_STATUS = o6.enumfield(1, name="UnknownStatus")
    ROLLBACK = o6.enumfield(2, name="Rollback")
    PROCESSING_STOPPED = o6.enumfield(3, name="ProcessingStopped")
    CONNECTION_CONFIGURATION_SET_INVALID = o6.enumfield(4, name="ConnectionConfigurationSetInvalid")
    GDS_CONNECTION_ERROR = o6.enumfield(5, name="GdsConnectionError")
    GDS_PROCESSING_ERROR = o6.enumfield(6, name="GdsProcessingError")
    ALIAS_NAME_PROCESSING_ERROR = o6.enumfield(7, name="AliasNameProcessingError")
    EXTERNAL_SKS_CONNECTION_ERROR = o6.enumfield(8, name="ExternalSksConnectionError")
    EXTERNAL_SKS_PROCESSING_ERROR = o6.enumfield(9, name="ExternalSksProcessingError")
    TARGET_SERVER_CONNECTION_ERROR = o6.enumfield(10, name="TargetServerConnectionError")
    RESOLVING_NAMESPACES_ERROR = o6.enumfield(11, name="ResolvingNamespacesError")
    RESOLVING_PATHS_ERROR = o6.enumfield(12, name="ResolvingPathsError")
    VERIFY_ASSET_ERROR = o6.enumfield(13, name="VerifyAssetError")
    VERIFY_FUNCTIONAL_ENTITY_ERROR = o6.enumfield(14, name="VerifyFunctionalEntityError")
    CREATE_CONNECTION_ENDPOINT_ERROR = o6.enumfield(15, name="CreateConnectionEndpointError")
    ESTABLISH_CONTROL_ERROR = o6.enumfield(16, name="EstablishControlError")
    SET_CONFIGURATION_DATA_ERROR = o6.enumfield(17, name="SetConfigurationDataError")
    REASSIGN_CONTROL_ERROR = o6.enumfield(18, name="ReassignControlError")
    RESERVE_COMMUNICATION_IDS_ERROR = o6.enumfield(19, name="ReserveCommunicationIdsError")
    SET_COMMUNICATION_CONFIGURATION_ERROR = o6.enumfield(20, name="SetCommunicationConfigurationError")
    ENABLE_COMMUNICATION_ERROR = o6.enumfield(21, name="EnableCommunicationError")
    CLOSE_CONNECTION_ERROR = o6.enumfield(22, name="CloseConnectionError")
    LOCAL_SKS_KEY_PUSH_ERROR = o6.enumfield(23, name="LocalSksKeyPushError")
    RUNTIME_ERROR = o6.enumfield(24, name="RuntimeError")


@o6.datatype(nodeId="ns=fx_cm;i=3008", browseName="ConnectionDiagnosticsDataType", defaultEncodingId="ns=fx_cm;i=5088")
class ConnectionDiagnosticsDataType(ns0.datatypes.Structure):
    name: o6.QualifiedName
    lastActivity: LastActivityMask
    connectionState: ConnectionStateEnum
    errorEndpoint1: FxErrorEnum
    endpoint1Status: o6.StatusCode
    errorEndpoint2: FxErrorEnum
    endpoint2Status: o6.StatusCode


@o6.datatype(nodeId="ns=fx_cm;i=3021", browseName="SecurityKeyServerAddressDataType", defaultEncodingId="ns=fx_cm;i=5091")
class SecurityKeyServerAddressDataType(ns0.datatypes.Structure):
    address: o6.String
    securityPolicyUri: o6.String
    serverUri: o6.String
    usePushModel: o6.Boolean


@o6.datatype(nodeId="ns=fx_cm;i=13012", browseName="CommunicationFlowConfigurationConfDataType", isAbstract=True)
class CommunicationFlowConfigurationConfDataType(ns0.datatypes.Structure):
    browseName: o6.String
    flowProperties: list[ns0.datatypes.KeyValuePair] | None


@o6.datatype(nodeId="ns=fx_cm;i=13024", browseName="SecurityKeyServerAddressConfDataType", defaultEncodingId="ns=fx_cm;i=5050")
class SecurityKeyServerAddressConfDataType(ns0.datatypes.Structure):
    address: o6.String
    addressSelection: list[o6.String] | None
    addressModify: o6.Boolean | None
    securityPolicyUri: o6.String
    securityPolicyUriSelection: list[o6.String] | None
    securityPolicyUriModify: o6.Boolean | None
    serverUri: o6.String
    serverUriSelection: list[o6.String] | None
    serverUriModify: o6.Boolean | None
    usePushModel: o6.Boolean
    securityGroups: list[ns0.datatypes.SecurityGroupDataType] | None
    pubSubKeyPushTargets: list[ns0.datatypes.PubSubKeyPushTargetDataType] | None
    sksProperties: list[ns0.datatypes.KeyValuePair] | None


@o6.datatype(nodeId="ns=fx_cm;i=13027", browseName="ServerAddressConfDataType", defaultEncodingId="ns=fx_cm;i=5055")
class ServerAddressConfDataType(ns0.datatypes.Structure):
    browseName: o6.String
    address: o6.String
    addressSelection: list[o6.String] | None
    addressModify: o6.Boolean | None
    securityMode: ns0.datatypes.MessageSecurityMode
    securityModeSelection: list[ns0.datatypes.MessageSecurityMode] | None
    securityModeModify: o6.Boolean | None
    securityPolicyUri: o6.String
    securityPolicyUriSelection: list[o6.String] | None
    securityPolicyUriModify: o6.Boolean | None
    serverUri: o6.String
    serverUriSelection: list[o6.String] | None
    serverUriModify: o6.Boolean | None
    serverProperties: list[ns0.datatypes.KeyValuePair] | None
    namespaces: list[o6.String]


@o6.datatype(nodeId="ns=fx_cm;i=13033", browseName="CommunicationModelConfigurationDataType", isAbstract=True)
class CommunicationModelConfigurationDataType(ns0.datatypes.Structure):
    pass


@o6.datatype(nodeId="ns=fx_cm;i=13036", browseName="PubSubCommunicationModelConfigurationDataType", defaultEncodingId="ns=fx_cm;i=5064")
class PubSubCommunicationModelConfigurationDataType(CommunicationModelConfigurationDataType):
    pubSubConfiguration: ns0.datatypes.PubSubConfiguration2DataType
    translationTable: list[NodeIdTranslationDataType]
    configurationReferences: list[ns0.datatypes.PubSubConfigurationRefDataType]


@o6.datatype(nodeId="ns=fx_cm;i=13039", browseName="NodeIdentifier", defaultEncodingId="ns=fx_cm;i=5067")
class NodeIdentifier(ns0.datatypes.Union):
    node: o6.NodeId
    alias: o6.String
    identifierBrowsePath: ns0.datatypes.RelativePath


@o6.datatype(nodeId="ns=fx_cm;i=13042", browseName="NodeIdentifierValuePair", defaultEncodingId="ns=fx_cm;i=5070")
class NodeIdentifierValuePair(ns0.datatypes.Structure):
    key: NodeIdentifier
    arrayIndex: list[o6.UInt32]
    value: Any


@o6.datatype(nodeId="ns=fx_cm;i=13009", browseName="ConnectionEndpointConfigurationConfDataType", defaultEncodingId="ns=fx_cm;i=5035")
class ConnectionEndpointConfigurationConfDataType(ns0.datatypes.Structure):
    functionalEntityNode: NodeIdentifier
    functionalEntityNodeSelection: list[NodeIdentifier] | None
    functionalEntityNodeModify: o6.Boolean | None
    name: o6.String
    nameSelection: list[o6.String] | None
    nameModify: o6.Boolean | None
    connectionEndpointTypeId: o6.NodeId
    inputVariableIds: list[NodeIdentifier] | None
    outputVariableIds: list[NodeIdentifier] | None
    isPersistent: o6.Boolean
    cleanupTimeout: o6.Double
    isPreconfigured: o6.Boolean
    communicationLinks: o6.ExtensionObject | None
    preconfiguredPublishedDataSet: o6.String | None
    publishedDataSetData: ns0.datatypes.PublishedDataSetDataType | None
    preconfiguredSubscribedDataSet: o6.String | None
    subscribedDataSetData: ns0.datatypes.StandaloneSubscribedDataSetDataType | None
    expectedVerificationVariables: list[NodeIdentifierValuePair] | None
    controlGroups: list[NodeIdentifier] | None
    configurationData: list[NodeIdentifierValuePair] | None
    endpointProperties: list[ns0.datatypes.KeyValuePair] | None
    automationComponentIndex: o6.Int32
    outboundFlowIndex: o6.Int32 | None
    inboundFlowIndex: list[o6.Int32] | None


@o6.datatype(nodeId="ns=fx_cm;i=13006", browseName="ConnectionConfigurationConfDataType", defaultEncodingId="ns=fx_cm;i=5032")
class ConnectionConfigurationConfDataType(ns0.datatypes.Structure):
    browseName: o6.String
    endpoint1: ConnectionEndpointConfigurationConfDataType
    endpoint2: ConnectionEndpointConfigurationConfDataType | None
    connectionProperties: list[ns0.datatypes.KeyValuePair] | None


@o6.datatype(nodeId="ns=fx_cm;i=13030", browseName="AssetVerificationConfDataType", defaultEncodingId="ns=fx_cm;i=5061")
class AssetVerificationConfDataType(ns0.datatypes.Structure):
    assetToVerify: NodeIdentifier
    verificationMode: fx_data.datatypes.AssetVerificationModeEnum
    expectedVerificationResult: fx_data.datatypes.AssetVerificationResultEnum
    expectedVerificationVariables: list[NodeIdentifierValuePair]
    expectedAdditionalVerificationVariables: list[NodeIdentifierValuePair]
    assetProperties: list[ns0.datatypes.KeyValuePair] | None


@o6.datatype(nodeId="ns=fx_cm;i=13021", browseName="AutomationComponentConfigurationConfDataType", defaultEncodingId="ns=fx_cm;i=5044")
class AutomationComponentConfigurationConfDataType(ns0.datatypes.Structure):
    browseName: o6.String
    automationComponentNode: NodeIdentifier
    automationComponentNodeSelection: list[NodeIdentifier]
    automationComponentNodeModify: o6.Boolean
    commandBundleRequired: o6.Boolean
    assetVerification: list[AssetVerificationConfDataType]
    communicationModelConfig: CommunicationModelConfigurationDataType
    automationComponentProperties: list[ns0.datatypes.KeyValuePair]
    serverAddressIndex: o6.Int32


@o6.datatype(nodeId="ns=fx_cm;i=13003", browseName="ConnectionConfigurationSetConfDataType", defaultEncodingId="ns=fx_cm;i=5029")
class ConnectionConfigurationSetConfDataType(ns0.datatypes.Structure):
    browseName: o6.String
    connectionConfigurationSetFolder: list[o6.String]
    connections: list[ConnectionConfigurationConfDataType]
    communicationFlows: list[CommunicationFlowConfigurationConfDataType]
    serverAddresses: list[ServerAddressConfDataType]
    automationComponentConfigurations: list[AutomationComponentConfigurationConfDataType]
    rollbackOnError: o6.Boolean
    securityKeyServer: SecurityKeyServerAddressConfDataType
    version: o6.UInt32
    connectionConfigurationSetProperties: list[ns0.datatypes.KeyValuePair]


@o6.datatype(nodeId="ns=fx_cm;i=13045", browseName="NodeIdTranslationConfDataType", defaultEncodingId="ns=fx_cm;i=5073")
class NodeIdTranslationConfDataType(ns0.datatypes.Structure):
    nodePlaceholder: o6.NodeId
    node: NodeIdentifier


@o6.datatype(nodeId="ns=fx_cm;i=13048", browseName="AddressSelectionDataType", defaultEncodingId="ns=fx_cm;i=5076")
class AddressSelectionDataType(ns0.datatypes.Structure):
    address: ns0.datatypes.NetworkAddressDataType
    addressSelection: list[ns0.datatypes.NetworkAddressDataType]
    addressModify: o6.Boolean


@o6.datatype(nodeId="ns=fx_cm;i=13051", browseName="ReceiveQosSelectionDataType", defaultEncodingId="ns=fx_cm;i=5080")
class ReceiveQosSelectionDataType(ns0.datatypes.Structure):
    receiveQos: list[ns0.datatypes.ReceiveQosDataType]
    receiveQosSelection: Any
    receiveQosModify: o6.Boolean


@o6.datatype(nodeId="ns=fx_cm;i=13018", browseName="SubscriberConfigurationConfDataType", defaultEncodingId="ns=fx_cm;i=5041")
class SubscriberConfigurationConfDataType(ns0.datatypes.Structure):
    browseName: o6.String
    address: AddressSelectionDataType | None
    messageReceiveTimeout: o6.Double
    messageReceiveTimeoutSelection: list[o6.Double] | None
    messageReceiveTimeoutModify: o6.Boolean | None
    receiveQos: ReceiveQosSelectionDataType | None
    subscriberProperties: list[ns0.datatypes.KeyValuePair] | None


@o6.datatype(nodeId="ns=fx_cm;i=13015", browseName="PubSubCommunicationFlowConfigurationConfDataType", defaultEncodingId="ns=fx_cm;i=5038")
class PubSubCommunicationFlowConfigurationConfDataType(CommunicationFlowConfigurationConfDataType):
    browseName: o6.String
    flowProperties: list[ns0.datatypes.KeyValuePair] | None
    address: AddressSelectionDataType | None
    transportProfileUri: o6.String | None
    transportProfileUriSelection: list[o6.String] | None
    transportProfileUriModify: o6.Boolean | None
    headerLayoutUri: o6.String | None
    headerLayoutUriSelection: list[o6.String] | None
    headerLayoutUriModify: o6.Boolean | None
    publishingInterval: o6.Double | None
    publishingIntervalSelection: list[o6.Double] | None
    publishingIntervalModify: o6.Boolean | None
    qos: CommunicationFlowQosDataType | None
    qosSelection: list[CommunicationFlowQosDataType] | None
    qosModify: o6.Boolean | None
    securityMode: ns0.datatypes.MessageSecurityMode | None
    securityModeSelection: list[ns0.datatypes.MessageSecurityMode] | None
    securityModeModify: o6.Boolean | None
    securityGroupId: o6.String | None
    securityGroupIdSelection: list[o6.String] | None
    securityGroupIdModify: o6.Boolean | None
    subscriberConfigurations: list[SubscriberConfigurationConfDataType] | None


@o6.enumtype(nodeId="ns=fx_cm;i=13054", browseName="ConnectionConfigurationSetOperation")
class ConnectionConfigurationSetOperation:
    ELEMENT_ADD = o6.enumfield(0, name="ElementAdd")
    ELEMENT_REMOVE = o6.enumfield(1, name="ElementRemove")
    ELEMENT_REPLACE = o6.enumfield(2, name="ElementReplace")


del Any, TYPE_CHECKING, uuid, o6, di, fx_data, ns0, fx_cm_reftypes
