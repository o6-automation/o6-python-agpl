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


@o6.datatype(nodeId="ns=fx_cm;i=1035", browseName="ns=fx_cm;PortableKeyValuePair", defaultEncodingId="ns=fx_cm;i=1114")
class PortableKeyValuePair(ns0.datatypes.Structure):
    key: ns0.datatypes.PortableQualifiedName = o6.field(name="Key")
    value: Any = o6.field(name="Value")


@o6.datatype(nodeId="ns=fx_cm;i=1036", browseName="ns=fx_cm;ServerAddressDataType", defaultEncodingId="ns=fx_cm;i=1117")
class ServerAddressDataType(ns0.datatypes.Structure):
    address: o6.String = o6.field(name="Address")
    securityMode: ns0.datatypes.MessageSecurityMode = o6.field(name="SecurityMode")
    securityPolicyUri: o6.String = o6.field(name="SecurityPolicyUri")
    serverUri: o6.String = o6.field(name="ServerUri")


@o6.datatype(nodeId="ns=fx_cm;i=1051", browseName="ns=fx_cm;PortableRelativePathElement", defaultEncodingId="ns=fx_cm;i=1222")
class PortableRelativePathElement(ns0.datatypes.Structure):
    referenceTypeId: ns0.datatypes.PortableNodeId = o6.field(name="ReferenceTypeId")
    isInverse: o6.Boolean = o6.field(name="IsInverse")
    includeSubtypes: o6.Boolean = o6.field(name="IncludeSubtypes")
    targetName: ns0.datatypes.PortableQualifiedName = o6.field(name="TargetName")


@o6.datatype(nodeId="ns=fx_cm;i=1047", browseName="ns=fx_cm;PortableRelativePath", defaultEncodingId="ns=fx_cm;i=1159")
class PortableRelativePath(ns0.datatypes.Structure):
    elements: list[PortableRelativePathElement] = o6.field(name="Elements", arrayDimensions=[0])


@o6.enumtype(nodeId="ns=fx_cm;i=3001", browseName="ns=fx_cm;FxEditEnum")
class FxEditEnum(ns0.datatypes.Enumeration):
    START_EDITING = o6.enumfield(0, name="StartEditing")
    COMMIT_UPDATES = o6.enumfield(1, name="CommitUpdates")
    DISCARD_UPDATES = o6.enumfield(2, name="DiscardUpdates")


@o6.enumtype(nodeId="ns=fx_cm;i=3002", browseName="ns=fx_cm;FxProcessEnum")
class FxProcessEnum(ns0.datatypes.Enumeration):
    ACTION_ESTABLISH_CONNECTIONS_ENABLED = o6.enumfield(0, name="ActionEstablishConnectionsEnabled")
    ACTION_ESTABLISH_CONNECTIONS_DISABLED = o6.enumfield(1, name="ActionEstablishConnectionsDisabled")
    ACTION_ESTABLISH_CONNECTIONS = o6.enumfield(2, name="ActionEstablishConnections")
    ACTION_REMOVE_CONNECTIONS = o6.enumfield(3, name="ActionRemoveConnections")
    ACTION_ENABLE_CONNECTIONS = o6.enumfield(4, name="ActionEnableConnections")
    ACTION_DISABLE_CONNECTIONS = o6.enumfield(5, name="ActionDisableConnections")


@o6.datatype(nodeId="ns=fx_cm;i=3004", browseName="ns=fx_cm;CommunicationFlowQosDataType", defaultEncodingId="ns=fx_cm;i=5017")
class CommunicationFlowQosDataType(ns0.datatypes.Structure):
    qosCategory: o6.String = o6.field(name="QosCategory")
    transmitQos: list[ns0.datatypes.TransmitQosDataType] = o6.field(name="TransmitQos", arrayDimensions=[1])
    receiveQos: list[ns0.datatypes.ReceiveQosDataType] = o6.field(name="ReceiveQos", arrayDimensions=[1])


@o6.optionsettype(nodeId="ns=fx_cm;i=3009", browseName="ns=fx_cm;LastActivityMask", base=o6.UInt16)
class LastActivityMask:
    ESTABLISH_ENABLED = o6.bitmask(0x01 << 0, name="EstablishEnabled")
    ESTABLISH_DISABLED = o6.bitmask(0x01 << 1, name="EstablishDisabled")
    ESTABLISH = o6.bitmask(0x01 << 2, name="Establish")
    REMOVE = o6.bitmask(0x01 << 3, name="Remove")
    ENABLE = o6.bitmask(0x01 << 4, name="Enable")
    DISABLE = o6.bitmask(0x01 << 5, name="Disable")
    ERROR = o6.bitmask(0x01 << 15, name="Error")


@o6.enumtype(nodeId="ns=fx_cm;i=3011", browseName="ns=fx_cm;ConnectionStateEnum")
class ConnectionStateEnum(ns0.datatypes.Enumeration):
    CONNECTION_NOT_MONITORED = o6.enumfield(0, name="ConnectionNotMonitored")
    CONNECTION_NOT_ESTABLISHED = o6.enumfield(1, name="ConnectionNotEstablished")
    CONNECTION_INITIAL = o6.enumfield(2, name="ConnectionInitial")
    CONNECTION_READY = o6.enumfield(3, name="ConnectionReady")
    CONNECTION_PRE_OPERATIONAL = o6.enumfield(4, name="ConnectionPreOperational")
    CONNECTION_OPERATIONAL = o6.enumfield(5, name="ConnectionOperational")
    CONNECTION_ERROR = o6.enumfield(6, name="ConnectionError")


@o6.datatype(nodeId="ns=fx_cm;i=3012", browseName="ns=fx_cm;PortableNodeIdentifier", defaultEncodingId="ns=fx_cm;i=5057")
class PortableNodeIdentifier(ns0.datatypes.Union):
    node: ns0.datatypes.PortableNodeId = o6.field(name="Node")
    alias: o6.String = o6.field(name="Alias")
    identifierBrowsePath: PortableRelativePath = o6.field(name="IdentifierBrowsePath")


@o6.datatype(nodeId="ns=fx_cm;i=3005", browseName="ns=fx_cm;PortableNodeIdentifierValuePair", defaultEncodingId="ns=fx_cm;i=5016")
class PortableNodeIdentifierValuePair(ns0.datatypes.Structure):
    key: PortableNodeIdentifier = o6.field(name="Key")
    arrayIndex: list[o6.UInt32] = o6.field(name="ArrayIndex", arrayDimensions=[0])
    value: Any = o6.field(name="Value")


@o6.datatype(nodeId="ns=fx_cm;i=3006", browseName="ns=fx_cm;NodeIdTranslationDataType", defaultEncodingId="ns=fx_cm;i=5025")
class NodeIdTranslationDataType(ns0.datatypes.Structure):
    nodePlaceholder: o6.NodeId = o6.field(name="NodePlaceholder")
    portableNode: PortableNodeIdentifier = o6.field(name="PortableNode")


@o6.enumtype(nodeId="ns=fx_cm;i=3015", browseName="ns=fx_cm;FxErrorEnum")
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


@o6.datatype(nodeId="ns=fx_cm;i=3008", browseName="ns=fx_cm;ConnectionDiagnosticsDataType", defaultEncodingId="ns=fx_cm;i=5088")
class ConnectionDiagnosticsDataType(ns0.datatypes.Structure):
    name: o6.QualifiedName = o6.field(name="Name")
    lastActivity: LastActivityMask = o6.field(name="LastActivity")
    connectionState: ConnectionStateEnum = o6.field(name="ConnectionState")
    errorEndpoint1: FxErrorEnum = o6.field(name="ErrorEndpoint1")
    endpoint1Status: o6.StatusCode = o6.field(name="Endpoint1Status")
    errorEndpoint2: FxErrorEnum = o6.field(name="ErrorEndpoint2")
    endpoint2Status: o6.StatusCode = o6.field(name="Endpoint2Status")


@o6.datatype(nodeId="ns=fx_cm;i=3021", browseName="ns=fx_cm;SecurityKeyServerAddressDataType", defaultEncodingId="ns=fx_cm;i=5091")
class SecurityKeyServerAddressDataType(ns0.datatypes.Structure):
    address: o6.String = o6.field(name="Address")
    securityPolicyUri: o6.String = o6.field(name="SecurityPolicyUri")
    serverUri: o6.String = o6.field(name="ServerUri")
    usePushModel: o6.Boolean = o6.field(name="UsePushModel")


@o6.datatype(nodeId="ns=fx_cm;i=13012", browseName="ns=fx_cm;CommunicationFlowConfigurationConfDataType", isAbstract=True)
class CommunicationFlowConfigurationConfDataType(ns0.datatypes.Structure):
    browseName: o6.String = o6.field(name="BrowseName")
    flowProperties: list[ns0.datatypes.KeyValuePair] | None = o6.field(name="FlowProperties", arrayDimensions=[0])


@o6.datatype(nodeId="ns=fx_cm;i=13024", browseName="ns=fx_cm;SecurityKeyServerAddressConfDataType", defaultEncodingId="ns=fx_cm;i=5050")
class SecurityKeyServerAddressConfDataType(ns0.datatypes.Structure):
    address: o6.String = o6.field(name="Address")
    addressSelection: list[o6.String] | None = o6.field(name="AddressSelection", arrayDimensions=[0])
    addressModify: o6.Boolean | None = o6.field(name="AddressModify")
    securityPolicyUri: o6.String = o6.field(name="SecurityPolicyUri")
    securityPolicyUriSelection: list[o6.String] | None = o6.field(name="SecurityPolicyUriSelection", arrayDimensions=[0])
    securityPolicyUriModify: o6.Boolean | None = o6.field(name="SecurityPolicyUriModify")
    serverUri: o6.String = o6.field(name="ServerUri")
    serverUriSelection: list[o6.String] | None = o6.field(name="ServerUriSelection", arrayDimensions=[0])
    serverUriModify: o6.Boolean | None = o6.field(name="ServerUriModify")
    usePushModel: o6.Boolean = o6.field(name="UsePushModel")
    securityGroups: list[ns0.datatypes.SecurityGroupDataType] | None = o6.field(name="SecurityGroups", arrayDimensions=[0])
    pubSubKeyPushTargets: list[ns0.datatypes.PubSubKeyPushTargetDataType] | None = o6.field(name="PubSubKeyPushTargets", arrayDimensions=[0])
    sksProperties: list[ns0.datatypes.KeyValuePair] | None = o6.field(name="SksProperties", arrayDimensions=[0])


@o6.datatype(nodeId="ns=fx_cm;i=13027", browseName="ns=fx_cm;ServerAddressConfDataType", defaultEncodingId="ns=fx_cm;i=5055")
class ServerAddressConfDataType(ns0.datatypes.Structure):
    browseName: o6.String = o6.field(name="BrowseName")
    address: o6.String = o6.field(name="Address")
    addressSelection: list[o6.String] | None = o6.field(name="AddressSelection", arrayDimensions=[0])
    addressModify: o6.Boolean | None = o6.field(name="AddressModify")
    securityMode: ns0.datatypes.MessageSecurityMode = o6.field(name="SecurityMode")
    securityModeSelection: list[ns0.datatypes.MessageSecurityMode] | None = o6.field(name="SecurityModeSelection", arrayDimensions=[0])
    securityModeModify: o6.Boolean | None = o6.field(name="SecurityModeModify")
    securityPolicyUri: o6.String = o6.field(name="SecurityPolicyUri")
    securityPolicyUriSelection: list[o6.String] | None = o6.field(name="SecurityPolicyUriSelection", arrayDimensions=[0])
    securityPolicyUriModify: o6.Boolean | None = o6.field(name="SecurityPolicyUriModify")
    serverUri: o6.String = o6.field(name="ServerUri")
    serverUriSelection: list[o6.String] | None = o6.field(name="ServerUriSelection", arrayDimensions=[0])
    serverUriModify: o6.Boolean | None = o6.field(name="ServerUriModify")
    serverProperties: list[ns0.datatypes.KeyValuePair] | None = o6.field(name="ServerProperties", arrayDimensions=[0])
    namespaces: list[o6.String] = o6.field(name="Namespaces", arrayDimensions=[0])


@o6.datatype(nodeId="ns=fx_cm;i=13033", browseName="ns=fx_cm;CommunicationModelConfigurationDataType", isAbstract=True)
class CommunicationModelConfigurationDataType(ns0.datatypes.Structure):
    pass


@o6.datatype(nodeId="ns=fx_cm;i=13036", browseName="ns=fx_cm;PubSubCommunicationModelConfigurationDataType", defaultEncodingId="ns=fx_cm;i=5064")
class PubSubCommunicationModelConfigurationDataType(CommunicationModelConfigurationDataType):
    pubSubConfiguration: ns0.datatypes.PubSubConfiguration2DataType = o6.field(name="PubSubConfiguration")
    translationTable: list[NodeIdTranslationDataType] = o6.field(name="TranslationTable", arrayDimensions=[0])
    configurationReferences: list[ns0.datatypes.PubSubConfigurationRefDataType] = o6.field(name="ConfigurationReferences", arrayDimensions=[0])


@o6.datatype(nodeId="ns=fx_cm;i=13039", browseName="ns=fx_cm;NodeIdentifier", defaultEncodingId="ns=fx_cm;i=5067")
class NodeIdentifier(ns0.datatypes.Union):
    node: o6.NodeId = o6.field(name="Node")
    alias: o6.String = o6.field(name="Alias")
    identifierBrowsePath: ns0.datatypes.RelativePath = o6.field(name="IdentifierBrowsePath")


@o6.datatype(nodeId="ns=fx_cm;i=13042", browseName="ns=fx_cm;NodeIdentifierValuePair", defaultEncodingId="ns=fx_cm;i=5070")
class NodeIdentifierValuePair(ns0.datatypes.Structure):
    key: NodeIdentifier = o6.field(name="Key")
    arrayIndex: list[o6.UInt32] = o6.field(name="ArrayIndex", arrayDimensions=[0])
    value: Any = o6.field(name="Value")


@o6.datatype(nodeId="ns=fx_cm;i=13009", browseName="ns=fx_cm;ConnectionEndpointConfigurationConfDataType", defaultEncodingId="ns=fx_cm;i=5035")
class ConnectionEndpointConfigurationConfDataType(ns0.datatypes.Structure):
    functionalEntityNode: NodeIdentifier = o6.field(name="FunctionalEntityNode")
    functionalEntityNodeSelection: list[NodeIdentifier] | None = o6.field(name="FunctionalEntityNodeSelection", arrayDimensions=[0])
    functionalEntityNodeModify: o6.Boolean | None = o6.field(name="FunctionalEntityNodeModify")
    name: o6.String = o6.field(name="Name")
    nameSelection: list[o6.String] | None = o6.field(name="NameSelection", arrayDimensions=[0])
    nameModify: o6.Boolean | None = o6.field(name="NameModify")
    connectionEndpointTypeId: o6.NodeId = o6.field(name="ConnectionEndpointTypeId")
    inputVariableIds: list[NodeIdentifier] | None = o6.field(name="InputVariableIds", arrayDimensions=[0])
    outputVariableIds: list[NodeIdentifier] | None = o6.field(name="OutputVariableIds", arrayDimensions=[0])
    isPersistent: o6.Boolean = o6.field(name="IsPersistent")
    cleanupTimeout: o6.Double = o6.field(name="CleanupTimeout")
    isPreconfigured: o6.Boolean = o6.field(name="IsPreconfigured")
    communicationLinks: o6.ExtensionObject | None = o6.field(name="CommunicationLinks")
    preconfiguredPublishedDataSet: o6.String | None = o6.field(name="PreconfiguredPublishedDataSet")
    publishedDataSetData: ns0.datatypes.PublishedDataSetDataType | None = o6.field(name="PublishedDataSetData")
    preconfiguredSubscribedDataSet: o6.String | None = o6.field(name="PreconfiguredSubscribedDataSet")
    subscribedDataSetData: ns0.datatypes.StandaloneSubscribedDataSetDataType | None = o6.field(name="SubscribedDataSetData")
    expectedVerificationVariables: list[NodeIdentifierValuePair] | None = o6.field(name="ExpectedVerificationVariables", arrayDimensions=[0])
    controlGroups: list[NodeIdentifier] | None = o6.field(name="ControlGroups", arrayDimensions=[0])
    configurationData: list[NodeIdentifierValuePair] | None = o6.field(name="ConfigurationData", arrayDimensions=[0])
    endpointProperties: list[ns0.datatypes.KeyValuePair] | None = o6.field(name="EndpointProperties", arrayDimensions=[0])
    automationComponentIndex: o6.Int32 = o6.field(name="AutomationComponentIndex")
    outboundFlowIndex: o6.Int32 | None = o6.field(name="OutboundFlowIndex")
    inboundFlowIndex: list[o6.Int32] | None = o6.field(name="InboundFlowIndex", arrayDimensions=[0])


@o6.datatype(nodeId="ns=fx_cm;i=13006", browseName="ns=fx_cm;ConnectionConfigurationConfDataType", defaultEncodingId="ns=fx_cm;i=5032")
class ConnectionConfigurationConfDataType(ns0.datatypes.Structure):
    browseName: o6.String = o6.field(name="BrowseName")
    endpoint1: ConnectionEndpointConfigurationConfDataType = o6.field(name="Endpoint1")
    endpoint2: ConnectionEndpointConfigurationConfDataType | None = o6.field(name="Endpoint2")
    connectionProperties: list[ns0.datatypes.KeyValuePair] | None = o6.field(name="ConnectionProperties", arrayDimensions=[0])


@o6.datatype(nodeId="ns=fx_cm;i=13030", browseName="ns=fx_cm;AssetVerificationConfDataType", defaultEncodingId="ns=fx_cm;i=5061")
class AssetVerificationConfDataType(ns0.datatypes.Structure):
    assetToVerify: NodeIdentifier = o6.field(name="AssetToVerify")
    verificationMode: fx_data.datatypes.AssetVerificationModeEnum = o6.field(name="VerificationMode")
    expectedVerificationResult: fx_data.datatypes.AssetVerificationResultEnum = o6.field(name="ExpectedVerificationResult")
    expectedVerificationVariables: list[NodeIdentifierValuePair] = o6.field(name="ExpectedVerificationVariables", arrayDimensions=[0])
    expectedAdditionalVerificationVariables: list[NodeIdentifierValuePair] = o6.field(name="ExpectedAdditionalVerificationVariables", arrayDimensions=[0])
    assetProperties: list[ns0.datatypes.KeyValuePair] | None = o6.field(name="AssetProperties", arrayDimensions=[0])


@o6.datatype(nodeId="ns=fx_cm;i=13021", browseName="ns=fx_cm;AutomationComponentConfigurationConfDataType", defaultEncodingId="ns=fx_cm;i=5044")
class AutomationComponentConfigurationConfDataType(ns0.datatypes.Structure):
    browseName: o6.String = o6.field(name="BrowseName")
    automationComponentNode: NodeIdentifier = o6.field(name="AutomationComponentNode")
    automationComponentNodeSelection: list[NodeIdentifier] = o6.field(name="AutomationComponentNodeSelection", arrayDimensions=[0])
    automationComponentNodeModify: o6.Boolean = o6.field(name="AutomationComponentNodeModify")
    commandBundleRequired: o6.Boolean = o6.field(name="CommandBundleRequired")
    assetVerification: list[AssetVerificationConfDataType] = o6.field(name="AssetVerification", arrayDimensions=[0])
    communicationModelConfig: CommunicationModelConfigurationDataType = o6.field(name="CommunicationModelConfig")
    automationComponentProperties: list[ns0.datatypes.KeyValuePair] = o6.field(name="AutomationComponentProperties", arrayDimensions=[0])
    serverAddressIndex: o6.Int32 = o6.field(name="ServerAddressIndex")


@o6.datatype(nodeId="ns=fx_cm;i=13003", browseName="ns=fx_cm;ConnectionConfigurationSetConfDataType", defaultEncodingId="ns=fx_cm;i=5029")
class ConnectionConfigurationSetConfDataType(ns0.datatypes.Structure):
    browseName: o6.String = o6.field(name="BrowseName")
    connectionConfigurationSetFolder: list[o6.String] = o6.field(name="ConnectionConfigurationSetFolder", arrayDimensions=[0])
    connections: list[ConnectionConfigurationConfDataType] = o6.field(name="Connections", arrayDimensions=[0])
    communicationFlows: list[CommunicationFlowConfigurationConfDataType] = o6.field(name="CommunicationFlows", arrayDimensions=[0])
    serverAddresses: list[ServerAddressConfDataType] = o6.field(name="ServerAddresses", arrayDimensions=[0])
    automationComponentConfigurations: list[AutomationComponentConfigurationConfDataType] = o6.field(name="AutomationComponentConfigurations", arrayDimensions=[0])
    rollbackOnError: o6.Boolean = o6.field(name="RollbackOnError")
    securityKeyServer: SecurityKeyServerAddressConfDataType = o6.field(name="SecurityKeyServer")
    version: o6.UInt32 = o6.field(name="Version")
    connectionConfigurationSetProperties: list[ns0.datatypes.KeyValuePair] = o6.field(name="ConnectionConfigurationSetProperties", arrayDimensions=[0])


@o6.datatype(nodeId="ns=fx_cm;i=13045", browseName="ns=fx_cm;NodeIdTranslationConfDataType", defaultEncodingId="ns=fx_cm;i=5073")
class NodeIdTranslationConfDataType(ns0.datatypes.Structure):
    nodePlaceholder: o6.NodeId = o6.field(name="NodePlaceholder")
    node: NodeIdentifier = o6.field(name="Node")


@o6.datatype(nodeId="ns=fx_cm;i=13048", browseName="ns=fx_cm;AddressSelectionDataType", defaultEncodingId="ns=fx_cm;i=5076")
class AddressSelectionDataType(ns0.datatypes.Structure):
    address: ns0.datatypes.NetworkAddressDataType = o6.field(name="Address")
    addressSelection: list[ns0.datatypes.NetworkAddressDataType] = o6.field(name="AddressSelection", arrayDimensions=[0])
    addressModify: o6.Boolean = o6.field(name="AddressModify")


@o6.datatype(nodeId="ns=fx_cm;i=13051", browseName="ns=fx_cm;ReceiveQosSelectionDataType", defaultEncodingId="ns=fx_cm;i=5080")
class ReceiveQosSelectionDataType(ns0.datatypes.Structure):
    receiveQos: list[ns0.datatypes.ReceiveQosDataType] = o6.field(name="ReceiveQos", arrayDimensions=[0])
    receiveQosSelection: Any = o6.field(name="ReceiveQosSelection")
    receiveQosModify: o6.Boolean = o6.field(name="ReceiveQosModify")


@o6.datatype(nodeId="ns=fx_cm;i=13018", browseName="ns=fx_cm;SubscriberConfigurationConfDataType", defaultEncodingId="ns=fx_cm;i=5041")
class SubscriberConfigurationConfDataType(ns0.datatypes.Structure):
    browseName: o6.String = o6.field(name="BrowseName")
    address: AddressSelectionDataType | None = o6.field(name="Address")
    messageReceiveTimeout: o6.Double = o6.field(name="MessageReceiveTimeout")
    messageReceiveTimeoutSelection: list[o6.Double] | None = o6.field(name="MessageReceiveTimeoutSelection", arrayDimensions=[0])
    messageReceiveTimeoutModify: o6.Boolean | None = o6.field(name="MessageReceiveTimeoutModify")
    receiveQos: ReceiveQosSelectionDataType | None = o6.field(name="ReceiveQos")
    subscriberProperties: list[ns0.datatypes.KeyValuePair] | None = o6.field(name="SubscriberProperties", arrayDimensions=[0])


@o6.datatype(nodeId="ns=fx_cm;i=13015", browseName="ns=fx_cm;PubSubCommunicationFlowConfigurationConfDataType", defaultEncodingId="ns=fx_cm;i=5038")
class PubSubCommunicationFlowConfigurationConfDataType(CommunicationFlowConfigurationConfDataType):
    browseName: o6.String = o6.field(name="BrowseName")
    flowProperties: list[ns0.datatypes.KeyValuePair] | None = o6.field(name="FlowProperties", arrayDimensions=[0])
    address: AddressSelectionDataType | None = o6.field(name="Address")
    transportProfileUri: o6.String | None = o6.field(name="TransportProfileUri")
    transportProfileUriSelection: list[o6.String] | None = o6.field(name="TransportProfileUriSelection", arrayDimensions=[0])
    transportProfileUriModify: o6.Boolean | None = o6.field(name="TransportProfileUriModify")
    headerLayoutUri: o6.String | None = o6.field(name="HeaderLayoutUri")
    headerLayoutUriSelection: list[o6.String] | None = o6.field(name="HeaderLayoutUriSelection", arrayDimensions=[0])
    headerLayoutUriModify: o6.Boolean | None = o6.field(name="HeaderLayoutUriModify")
    publishingInterval: o6.Double | None = o6.field(name="PublishingInterval")
    publishingIntervalSelection: list[o6.Double] | None = o6.field(name="PublishingIntervalSelection", arrayDimensions=[0])
    publishingIntervalModify: o6.Boolean | None = o6.field(name="PublishingIntervalModify")
    qos: CommunicationFlowQosDataType | None = o6.field(name="Qos")
    qosSelection: list[CommunicationFlowQosDataType] | None = o6.field(name="QosSelection", arrayDimensions=[0])
    qosModify: o6.Boolean | None = o6.field(name="QosModify")
    securityMode: ns0.datatypes.MessageSecurityMode | None = o6.field(name="SecurityMode")
    securityModeSelection: list[ns0.datatypes.MessageSecurityMode] | None = o6.field(name="SecurityModeSelection", arrayDimensions=[0])
    securityModeModify: o6.Boolean | None = o6.field(name="SecurityModeModify")
    securityGroupId: o6.String | None = o6.field(name="SecurityGroupId")
    securityGroupIdSelection: list[o6.String] | None = o6.field(name="SecurityGroupIdSelection", arrayDimensions=[0])
    securityGroupIdModify: o6.Boolean | None = o6.field(name="SecurityGroupIdModify")
    subscriberConfigurations: list[SubscriberConfigurationConfDataType] | None = o6.field(name="SubscriberConfigurations", arrayDimensions=[0])


@o6.optionsettype(nodeId="ns=fx_cm;i=13054", browseName="ns=fx_cm;ConnectionConfigurationSetOperation", base=o6.Byte)
class ConnectionConfigurationSetOperation:
    ELEMENT_ADD = o6.bitmask(0x01 << 0, name="ElementAdd")
    ELEMENT_REMOVE = o6.bitmask(0x01 << 1, name="ElementRemove")
    ELEMENT_REPLACE = o6.bitmask(0x01 << 2, name="ElementReplace")


del Any, TYPE_CHECKING, uuid, o6, di, fx_data, ns0, fx_cm_reftypes
