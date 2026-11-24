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
from . import datatypes as fx_cm_datypes
from . import vartypes as fx_cm_vartypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(nodeId="ns=fx_cm;i=1001", browseName="ns=fx_cm;SubscriberConfigurationType", displayName="SubscriberConfigurationType")
class SubscriberConfigurationType(ns0.objtypes.BaseObjectType):
    address: ns0.vartypes.SelectionListType | None
    messageReceiveTimeout: ns0.vartypes.SelectionListType
    receiveQos: ns0.vartypes.SelectionListType | None


@o6.objecttype(nodeId="ns=fx_cm;i=1003", browseName="ns=fx_cm;CommunicationFlowConfigurationType", displayName="CommunicationFlowConfigurationType", isAbstract=True)
class CommunicationFlowConfigurationType(ns0.objtypes.BaseObjectType):
    pass


@o6.objecttype(nodeId="ns=fx_cm;i=1013", browseName="ns=fx_cm;ConnectionConfigurationType", displayName="ConnectionConfigurationType")
class ConnectionConfigurationType(ns0.objtypes.BaseObjectType):
    endpoint1: ConnectionEndpointConfigurationType
    endpoint2: ConnectionEndpointConfigurationType | None


@o6.objecttype(nodeId="ns=fx_cm;i=1014", browseName="ns=fx_cm;PubSubCommunicationFlowConfigurationType", displayName="PubSubCommunicationFlowConfigurationType")
class PubSubCommunicationFlowConfigurationType(CommunicationFlowConfigurationType):
    address: ns0.vartypes.SelectionListType | None
    headerLayoutUri: ns0.vartypes.SelectionListType | None
    publishingInterval: ns0.vartypes.SelectionListType | None
    qos: ns0.vartypes.SelectionListType | None
    securityGroupId: ns0.vartypes.SelectionListType | None
    securityMode: ns0.vartypes.SelectionListType | None
    subscriberConfiguration_: SubscriberConfigurationType | None
    transportProfileUri: ns0.vartypes.SelectionListType | None


@o6.objecttype(nodeId="ns=fx_cm;i=1015", browseName="ns=fx_cm;EstablishConnectionErrorEventType", displayName="EstablishConnectionErrorEventType", isAbstract=True)
class EstablishConnectionErrorEventType(ns0.objtypes.BaseLogEventType):
    pass


@o6.objecttype(nodeId="ns=fx_cm;i=1016", browseName="ns=fx_cm;CommunicationModelConfigurationType", displayName="CommunicationModelConfigurationType", isAbstract=True)
class CommunicationModelConfigurationType(ns0.objtypes.BaseObjectType):
    pass


@o6.objecttype(nodeId="ns=fx_cm;i=1018", browseName="ns=fx_cm;ConnectionConfigurationSetStateMachineType", displayName="ConnectionConfigurationSetStateMachineType")
class ConnectionConfigurationSetStateMachineType(ns0.objtypes.FiniteStateMachineType):
    error: ns0.objtypes.StateType
    errorToProcessing: ns0.objtypes.TransitionType
    lastTransition: ns0.vartypes.FiniteTransitionVariableType
    processing: ns0.objtypes.StateType
    processingToError: ns0.objtypes.TransitionType
    processingToReady: ns0.objtypes.TransitionType
    ready: ns0.objtypes.StateType
    readyToProcessing: ns0.objtypes.TransitionType


@o6.objecttype(nodeId="ns=fx_cm;i=1020", browseName="ns=fx_cm;CloseConnectionErrorEventType", displayName="CloseConnectionErrorEventType", isAbstract=True)
class CloseConnectionErrorEventType(ns0.objtypes.BaseLogEventType):
    pass


CommunicationFlowConfigurationType(nodeId="ns=fx_cm;i=1202", browseName="ns=fx_cm;<CommunicationFlow>", modellingRule="MandatoryPlaceholder", _allow_abstract=True)


ns0.vartypes.PropertyType(
    nodeId="ns=fx_cm;i=1265",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_cm;i=1481",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Action", dataType=o6.NodeId("ns=fx_cm;i=3001"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="ConnectionConfigurationSets", dataType=o6.NodeId("i=17"), valueRank=1, arrayDimensions=[0], description=o6.LocalizedText()),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fx_cm;i=1267",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_cm;i=1481",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Results", dataType=o6.NodeId("i=19"), valueRank=1, arrayDimensions=[0], description=o6.LocalizedText())],
)
o6.call(
    nodeId="ns=fx_cm;i=1481",
    browseName="ns=fx_cm;EditConnectionConfigurationSets",
    modellingRule="Optional",
    inputArgs=o6.hasProperty(o6.ns["ns=fx_cm;i=1265"]),
    outputArgs=o6.hasProperty(o6.ns["ns=fx_cm;i=1267"]),
)
o6.reference(o6.ns["ns=fx_cm;i=1481"], "i=41", "ns=fx_data;i=1025")

ns0.vartypes.PropertyType(
    nodeId="ns=fx_cm;i=1270",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_cm;i=1483",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="Action", dataType=o6.NodeId("ns=fx_cm;i=3002"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="ConnectionConfigurationSets", dataType=o6.NodeId("i=17"), valueRank=1, arrayDimensions=[0], description=o6.LocalizedText()),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fx_cm;i=1271",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_cm;i=1483",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Results", dataType=o6.NodeId("i=19"), valueRank=1, arrayDimensions=[0], description=o6.LocalizedText())],
)
o6.call(
    nodeId="ns=fx_cm;i=1483",
    browseName="ns=fx_cm;ProcessConnectionConfigurationSets",
    modellingRule="Optional",
    inputArgs=o6.hasProperty(o6.ns["ns=fx_cm;i=1270"]),
    outputArgs=o6.hasProperty(o6.ns["ns=fx_cm;i=1271"]),
)
o6.reference(o6.ns["ns=fx_cm;i=1483"], "i=41", "ns=fx_data;i=1025")


@o6.objecttype(nodeId="ns=fx_cm;i=1246", browseName="ns=fx_cm;AutomationComponentConfigurationType", displayName="AutomationComponentConfigurationType")
class AutomationComponentConfigurationType(ns0.objtypes.BaseObjectType):
    assetVerification_: AssetVerificationType | None
    automationComponentNode: ns0.vartypes.SelectionListType
    commandBundleRequired: ns0.vartypes.BaseDataVariableType = o6.reference(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=fx_cm;i=6009", browseName="ns=fx_cm;CommandBundleRequired", modellingRule="Mandatory", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
        ),
        "ns=fx_cm;i=4003",
    )
    communicationModelConfig: CommunicationModelConfigurationType | None = o6.hasComponent(
        CommunicationModelConfigurationType(nodeId="ns=fx_cm;i=5013", browseName="ns=fx_cm;CommunicationModelConfig", modellingRule="Optional", _allow_abstract=True)
    )


@o6.objecttype(nodeId="ns=fx_cm;i=1129", browseName="ns=fx_cm;ConnectionEndpointConfigurationType", displayName="ConnectionEndpointConfigurationType")
class ConnectionEndpointConfigurationType(ns0.objtypes.BaseObjectType):
    configurationData: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=fx_cm;i=6109",
            browseName="ns=fx_cm;ConfigurationData",
            modellingRule="Optional",
            dataType=fx_cm_datypes.PortableNodeIdentifierValuePair,
            valueRank=1,
            arrayDimensions=[0],
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    connectionEndpoint: ConnectionEndpointParameterType
    controlGroups: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=fx_cm;i=6108",
            browseName="ns=fx_cm;ControlGroups",
            modellingRule="Optional",
            dataType=fx_cm_datypes.PortableNodeIdentifier,
            valueRank=1,
            arrayDimensions=[0],
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    expectedVerificationVariables: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=fx_cm;i=6107",
            browseName="ns=fx_cm;ExpectedVerificationVariables",
            modellingRule="Optional",
            dataType=fx_cm_datypes.PortableNodeIdentifierValuePair,
            valueRank=1,
            arrayDimensions=[0],
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    functionalEntityNode: ns0.vartypes.SelectionListType


@o6.objecttype(nodeId="ns=fx_cm;i=1010", browseName="ns=fx_cm;ConnectionManagerCapabilitiesType", displayName="ConnectionManagerCapabilitiesType")
class ConnectionManagerCapabilitiesType(ns0.objtypes.FolderType):
    capability_: ns0.vartypes.BaseDataVariableType | None = o6.reference(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_cm;i=6206", browseName="ns=fx_cm;<Capability>", modellingRule="OptionalPlaceholder", accessLevel=3, userAccessLevel=1),
        "ns=fx_cm;i=4008",
    )
    maxConnectionConfigurationSets: ns0.vartypes.BaseDataVariableType | None = o6.reference(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=fx_cm;i=6207", browseName="ns=fx_cm;MaxConnectionConfigurationSets", modellingRule="Optional", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1
        ),
        "ns=fx_cm;i=4008",
    )
    monitorsAllConnectionEndpoints: ns0.vartypes.BaseDataVariableType | None = o6.reference(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=fx_cm;i=6238", browseName="ns=fx_cm;MonitorsAllConnectionEndpoints", modellingRule="Optional", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
        ),
        "ns=fx_cm;i=4008",
    )
    monitorsLocalConnectionEndpoints: ns0.vartypes.BaseDataVariableType | None = o6.reference(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=fx_cm;i=6235", browseName="ns=fx_cm;MonitorsLocalConnectionEndpoints", modellingRule="Optional", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
        ),
        "ns=fx_cm;i=4008",
    )


@o6.objecttype(nodeId="ns=fx_cm;i=1002", browseName="ns=fx_cm;ConnectionManagerType", displayName="ConnectionManagerType")
class ConnectionManagerType(ns0.objtypes.BaseObjectType):
    aggregatedCurrentState: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=fx_cm;i=6205", browseName="ns=fx_cm;AggregatedCurrentState", modellingRule="Optional", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
        )
    )
    capabilities: ConnectionManagerCapabilitiesType | None = o6.hasComponent(
        ConnectionManagerCapabilitiesType(nodeId="ns=fx_cm;i=5085", browseName="ns=fx_cm;Capabilities", modellingRule="Optional")
    )
    connectionConfigurationSets: ns0.objtypes.FolderType
    connectionManagerConfiguration: ConnectionManagerConfigurationType | None
    connectionManagerLog: ns0.objtypes.LogObjectType | None
    diagnostics: di.objtypes.FunctionalGroupType | None
    editConnectionConfigurationSets: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=fx_cm;i=1481"])
    globalDiscoveryServers: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=fx_cm;i=6252",
            browseName="ns=fx_cm;GlobalDiscoveryServers",
            modellingRule="Optional",
            dataType=o6.String,
            valueRank=1,
            arrayDimensions=[0],
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    processConnectionConfigurationSets: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=fx_cm;i=1483"])


o6.reference(ConnectionManagerType, "i=41", EstablishConnectionErrorEventType)
o6.reference(ConnectionManagerType, "i=41", CloseConnectionErrorEventType)


@o6.objecttype(
    nodeId="ns=fx_cm;i=1017", browseName="ns=fx_cm;AuditUpdateConnectionConfigurationSetEventType", displayName="AuditUpdateConnectionConfigurationSetEventType", isAbstract=True
)
class AuditUpdateConnectionConfigurationSetEventType(ns0.objtypes.AuditWriteUpdateEventType):
    connectionConfigurationSetNode: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=fx_cm;i=6253", browseName="ns=fx_cm;ConnectionConfigurationSetNode", modellingRule="Mandatory", dataType=o6.NodeId, accessLevel=3, userAccessLevel=1
        )
    )
    name: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6254", browseName="ns=fx_cm;Name", modellingRule="Mandatory", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=fx_cm;i=1006", browseName="ns=fx_cm;ConnectionConfigurationSetEventType", displayName="ConnectionConfigurationSetEventType", isAbstract=True)
class ConnectionConfigurationSetEventType(ns0.objtypes.BaseEventType):
    action: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=fx_cm;i=6354", browseName="ns=fx_cm;Action", modellingRule="Mandatory", dataType=fx_cm_datypes.FxProcessEnum, accessLevel=3, userAccessLevel=1
        )
    )
    connectionConfigurationSetNode: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=fx_cm;i=6352", browseName="ns=fx_cm;ConnectionConfigurationSetNode", modellingRule="Mandatory", dataType=o6.NodeId, accessLevel=3, userAccessLevel=1
        )
    )
    name: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6353", browseName="ns=fx_cm;Name", modellingRule="Mandatory", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(
    nodeId="ns=fx_cm;i=1007",
    browseName="ns=fx_cm;ConnectionConfigurationSetProcessingStartedEventType",
    displayName="ConnectionConfigurationSetProcessingStartedEventType",
    isAbstract=True,
)
class ConnectionConfigurationSetProcessingStartedEventType(ConnectionConfigurationSetEventType):
    pass


o6.reference(o6.ns["ns=fx_cm;i=1483"], "i=41", ConnectionConfigurationSetProcessingStartedEventType)


@o6.objecttype(
    nodeId="ns=fx_cm;i=1008",
    browseName="ns=fx_cm;ConnectionConfigurationSetProcessingSucceededEventType",
    displayName="ConnectionConfigurationSetProcessingSucceededEventType",
    isAbstract=True,
)
class ConnectionConfigurationSetProcessingSucceededEventType(ConnectionConfigurationSetEventType):
    pass


o6.reference(o6.ns["ns=fx_cm;i=1483"], "i=41", ConnectionConfigurationSetProcessingSucceededEventType)


@o6.objecttype(
    nodeId="ns=fx_cm;i=1009",
    browseName="ns=fx_cm;ConnectionConfigurationSetProcessingFailedEventType",
    displayName="ConnectionConfigurationSetProcessingFailedEventType",
    isAbstract=True,
)
class ConnectionConfigurationSetProcessingFailedEventType(ConnectionConfigurationSetEventType):
    pass


o6.reference(o6.ns["ns=fx_cm;i=1483"], "i=41", ConnectionConfigurationSetProcessingFailedEventType)


@o6.objecttype(nodeId="ns=fx_cm;i=1012", browseName="ns=fx_cm;ConnectionConfigurationSetType", displayName="ConnectionConfigurationSetType")
class ConnectionConfigurationSetType(ns0.objtypes.BaseObjectType):
    automationComponentConfiguration_: AutomationComponentConfigurationType
    communicationFlow_: CommunicationFlowConfigurationType = o6.reference(o6.ns["ns=fx_cm;i=1202"], "ns=fx_cm;i=1060")
    connectionConfigurationSetStateMachine: ConnectionConfigurationSetStateMachineType
    connection_: ConnectionConfigurationType
    connectionsDiagnostics: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=fx_cm;i=6239",
            browseName="ns=fx_cm;ConnectionsDiagnostics",
            modellingRule="Optional",
            dataType=fx_cm_datypes.ConnectionDiagnosticsDataType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    edit: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=6487", browseName="ns=fx_cm;Edit", modellingRule="Optional", dataType=o6.Boolean)
    )
    lock: di.objtypes.LockingServicesType
    pubSubKeyPushTargets: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=fx_cm;i=6209",
            browseName="ns=fx_cm;PubSubKeyPushTargets",
            modellingRule="Optional",
            dataType=ns0.datatypes.PubSubKeyPushTargetDataType,
            valueRank=1,
            arrayDimensions=[0],
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    rollbackOnError: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fx_cm;i=1272", browseName="ns=fx_cm;RollbackOnError", modellingRule="Mandatory", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
    )
    securityGroups: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=fx_cm;i=6208",
            browseName="ns=fx_cm;SecurityGroups",
            modellingRule="Optional",
            dataType=ns0.datatypes.SecurityGroupDataType,
            valueRank=1,
            arrayDimensions=[0],
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    securityKeyServer: fx_cm_vartypes.SecurityKeyServerAddressType | None
    serverAddress_: fx_cm_vartypes.ServerAddressType
    version: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_cm;i=6219", browseName="ns=fx_cm;Version", modellingRule="Optional", dataType=o6.UInt32)
    )


@o6.objecttype(nodeId="ns=fx_cm;i=1261", browseName="ns=fx_cm;ConnectionEndpointParameterType", displayName="ConnectionEndpointParameterType")
class ConnectionEndpointParameterType(ns0.objtypes.BaseObjectType):
    cleanupTimeout: ns0.vartypes.SelectionListType
    communicationLinks: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=fx_cm;i=6179",
            browseName="ns=fx_cm;CommunicationLinks",
            modellingRule="Optional",
            dataType=fx_data.datatypes.CommunicationLinkConfigurationDataType,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    connectionEndpointTypeId: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=fx_cm;i=6172",
            browseName="ns=fx_cm;ConnectionEndpointTypeId",
            modellingRule="Mandatory",
            dataType=ns0.datatypes.PortableNodeId,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    inputVariableIds: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=fx_cm;i=6068",
            browseName="ns=fx_cm;InputVariableIds",
            modellingRule="Optional",
            dataType=fx_cm_datypes.PortableNodeIdentifier,
            valueRank=1,
            arrayDimensions=[0],
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    isPersistent: ns0.vartypes.SelectionListType
    isPreconfigured: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=fx_cm;i=6498", browseName="ns=fx_cm;IsPreconfigured", modellingRule="Mandatory", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
        )
    )
    name: ns0.vartypes.SelectionListType
    outputVariableIds: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=fx_cm;i=6082",
            browseName="ns=fx_cm;OutputVariableIds",
            modellingRule="Optional",
            dataType=fx_cm_datypes.PortableNodeIdentifier,
            valueRank=1,
            arrayDimensions=[0],
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    preconfiguredPublishedDataSet: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=fx_cm;i=6180", browseName="ns=fx_cm;PreconfiguredPublishedDataSet", modellingRule="Optional", dataType=o6.String, accessLevel=3, userAccessLevel=1
        )
    )
    preconfiguredSubscribedDataSet: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=fx_cm;i=6181", browseName="ns=fx_cm;PreconfiguredSubscribedDataSet", modellingRule="Optional", dataType=o6.String, accessLevel=3, userAccessLevel=1
        )
    )


@o6.objecttype(nodeId="ns=fx_cm;i=1247", browseName="ns=fx_cm;AssetVerificationType", displayName="AssetVerificationType")
class AssetVerificationType(ns0.objtypes.BaseObjectType):
    assetToVerify: ns0.vartypes.SelectionListType
    expectedAdditionalVerificationVariables: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=fx_cm;i=6526",
            browseName="ns=fx_cm;ExpectedAdditionalVerificationVariables",
            modellingRule="Mandatory",
            dataType=fx_cm_datypes.PortableNodeIdentifierValuePair,
            valueRank=1,
            arrayDimensions=[0],
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    expectedVerificationResult: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=fx_cm;i=6158",
            browseName="ns=fx_cm;ExpectedVerificationResult",
            modellingRule="Mandatory",
            dataType=fx_data.datatypes.AssetVerificationResultEnum,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    expectedVerificationVariables: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=fx_cm;i=6159",
            browseName="ns=fx_cm;ExpectedVerificationVariables",
            modellingRule="Mandatory",
            dataType=fx_cm_datypes.PortableNodeIdentifierValuePair,
            valueRank=1,
            arrayDimensions=[0],
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    verificationMode: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=fx_cm;i=6160",
            browseName="ns=fx_cm;VerificationMode",
            modellingRule="Mandatory",
            dataType=fx_data.datatypes.AssetVerificationModeEnum,
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(nodeId="ns=fx_cm;i=1042", browseName="ns=fx_cm;PubSubCommunicationModelConfigurationType", displayName="PubSubCommunicationModelConfigurationType")
class PubSubCommunicationModelConfigurationType(CommunicationModelConfigurationType):
    configurationReferences: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=fx_cm;i=6529",
            browseName="ns=fx_cm;ConfigurationReferences",
            modellingRule="Mandatory",
            dataType=ns0.datatypes.PubSubConfigurationRefDataType,
            valueRank=1,
            arrayDimensions=[0],
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    configurationValues: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=fx_cm;i=6530",
            browseName="ns=fx_cm;ConfigurationValues",
            modellingRule="Mandatory",
            dataType=ns0.datatypes.PubSubConfigurationValueDataType,
            valueRank=1,
            arrayDimensions=[0],
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    namespaces: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=fx_cm;i=6184",
            browseName="ns=fx_cm;Namespaces",
            modellingRule="Mandatory",
            dataType=o6.String,
            valueRank=1,
            arrayDimensions=[0],
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    pubSubConfiguration: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=fx_cm;i=6528",
            browseName="ns=fx_cm;PubSubConfiguration",
            modellingRule="Mandatory",
            dataType=ns0.datatypes.PubSubConfiguration2DataType,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    translationTable: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=fx_cm;i=6185",
            browseName="ns=fx_cm;TranslationTable",
            modellingRule="Mandatory",
            dataType=fx_cm_datypes.NodeIdTranslationDataType,
            valueRank=1,
            arrayDimensions=[0],
            accessLevel=3,
            userAccessLevel=1,
        )
    )


ns0.vartypes.PropertyType(
    nodeId="ns=fx_cm;i=16032",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_cm;i=7003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="FileHandle", dataType=o6.NodeId("i=7"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="RequireCompleteUpdate", dataType=o6.NodeId("i=1"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="Operations", dataType=o6.NodeId("ns=fx_cm;i=13054"), valueRank=1, arrayDimensions=[0], description=o6.LocalizedText()),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fx_cm;i=16033",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fx_cm;i=7003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="ChangesApplied", dataType=o6.NodeId("i=1"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="OperationResults", dataType=o6.NodeId("i=19"), valueRank=1, arrayDimensions=[0], description=o6.LocalizedText()),
        ns0.datatypes.Argument(name="ConfigurationObjects", dataType=o6.NodeId("i=17"), valueRank=1, arrayDimensions=[0], description=o6.LocalizedText()),
    ],
)
o6.call(
    nodeId="ns=fx_cm;i=7003",
    browseName="ns=fx_cm;CloseAndUpdate",
    modellingRule="Mandatory",
    inputArgs=o6.hasProperty(o6.ns["ns=fx_cm;i=16032"]),
    outputArgs=o6.hasProperty(o6.ns["ns=fx_cm;i=16033"]),
)


@o6.objecttype(nodeId="ns=fx_cm;i=1011", browseName="ns=fx_cm;ConnectionManagerConfigurationType", displayName="ConnectionManagerConfigurationType")
class ConnectionManagerConfigurationType(ns0.objtypes.FileType):
    closeAndUpdate: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=fx_cm;i=7003"])


del Any, TYPE_CHECKING, uuid, o6, di, fx_data, ns0, fx_cm_reftypes, fx_cm_datypes, fx_cm_vartypes
