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

"""Generated OPC UA fx_data namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.ns0 as ns0

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.enumtype(nodeId="ns=fx_data;i=31", browseName="ns=fx_data;PubSubConnectionEndpointModeEnum")
class PubSubConnectionEndpointModeEnum(ns0.datatypes.Enumeration):
    PUBLISHER_SUBSCRIBER = o6.enumfield(1, name="PublisherSubscriber")
    PUBLISHER = o6.enumfield(2, name="Publisher")
    SUBSCRIBER = o6.enumfield(3, name="Subscriber")


@o6.optionsettype(
    nodeId="ns=fx_data;i=1024",
    browseName="ns=fx_data;FxCommandMask",
    description="This OptionSet defines flags indicating the commands a ConnectionManager may use in its call to the EstablishConnections Method.",
    base=o6.UInt32,
)
class FxCommandMask:
    VERIFY_ASSET_CMD = o6.bitmask(0x01 << 0, name="VerifyAssetCmd")
    VERIFY_FUNCTIONAL_ENTITY_CMD = o6.bitmask(0x01 << 1, name="VerifyFunctionalEntityCmd")
    CREATE_CONNECTION_ENDPOINT_CMD = o6.bitmask(0x01 << 2, name="CreateConnectionEndpointCmd")
    ESTABLISH_CONTROL_CMD = o6.bitmask(0x01 << 3, name="EstablishControlCmd")
    SET_CONFIGURATION_DATA_CMD = o6.bitmask(0x01 << 4, name="SetConfigurationDataCmd")
    REASSIGN_CONTROL_CMD = o6.bitmask(0x01 << 5, name="ReassignControlCmd")
    RESERVE_COMMUNICATION_IDS_CMD = o6.bitmask(0x01 << 6, name="ReserveCommunicationIdsCmd")
    SET_COMMUNICATION_CONFIGURATION_CMD = o6.bitmask(0x01 << 7, name="SetCommunicationConfigurationCmd")
    ENABLE_COMMUNICATION_CMD = o6.bitmask(0x01 << 8, name="EnableCommunicationCmd")


@o6.enumtype(nodeId="ns=fx_data;i=1029", browseName="ns=fx_data;AssetVerificationModeEnum")
class AssetVerificationModeEnum(ns0.datatypes.Enumeration):
    ASSET_COMPATIBILITY = o6.enumfield(0, name="AssetCompatibility")
    ASSET_IDENTITY = o6.enumfield(1, name="AssetIdentity")
    ASSET_IDENTITY_AND_COMPATIBILITY = o6.enumfield(2, name="AssetIdentityAndCompatibility")


@o6.datatype(nodeId="ns=fx_data;i=1033", browseName="ns=fx_data;CommunicationConfigurationResultDataType", defaultEncodingId="ns=fx_data;i=1108", isAbstract=True)
class CommunicationConfigurationResultDataType(ns0.datatypes.Structure):
    pass


@o6.datatype(nodeId="ns=fx_data;i=1034", browseName="ns=fx_data;NodeIdArray", defaultEncodingId="ns=fx_data;i=1111")
class NodeIdArray(ns0.datatypes.Structure):
    node: o6.NodeId = o6.field(name="Node")
    arrayIndex: list[o6.UInt32] = o6.field(name="ArrayIndex", arrayDimensions=[1])


@o6.datatype(nodeId="ns=fx_data;i=1028", browseName="ns=fx_data;NodeIdValuePair", defaultEncodingId="ns=fx_data;i=1093")
class NodeIdValuePair(ns0.datatypes.Structure):
    key: NodeIdArray = o6.field(name="Key")
    value: Any = o6.field(name="Value")


@o6.enumtype(nodeId="ns=fx_data;i=1037", browseName="ns=fx_data;AssetVerificationResultEnum")
class AssetVerificationResultEnum(ns0.datatypes.Enumeration):
    NOT_SET = o6.enumfield(0, name="NotSet")
    MATCH = o6.enumfield(1, name="Match")
    COMPATIBLE = o6.enumfield(2, name="Compatible")
    MISMATCH = o6.enumfield(3, name="Mismatch")


@o6.datatype(nodeId="ns=fx_data;i=1038", browseName="ns=fx_data;AssetVerificationResultDataType", defaultEncodingId="ns=fx_data;i=1205")
class AssetVerificationResultDataType(ns0.datatypes.Structure):
    verificationStatus: o6.StatusCode = o6.field(name="VerificationStatus")
    verificationResult: AssetVerificationResultEnum = o6.field(name="VerificationResult")
    verificationVariablesErrors: list[o6.StatusCode] = o6.field(name="VerificationVariablesErrors", arrayDimensions=[1])
    verificationAdditionalVariablesErrors: list[o6.StatusCode] = o6.field(name="VerificationAdditionalVariablesErrors", arrayDimensions=[1])


@o6.datatype(nodeId="ns=fx_data;i=1039", browseName="ns=fx_data;PubSubCommunicationConfigurationResultDataType", defaultEncodingId="ns=fx_data;i=1208")
class PubSubCommunicationConfigurationResultDataType(CommunicationConfigurationResultDataType):
    result: o6.StatusCode = o6.field(name="Result")
    changesApplied: o6.Boolean = o6.field(name="ChangesApplied")
    referenceResults: list[o6.StatusCode] = o6.field(name="ReferenceResults", arrayDimensions=[1])
    configurationValues: list[ns0.datatypes.PubSubConfigurationValueDataType] = o6.field(name="ConfigurationValues", arrayDimensions=[1])
    configurationObjects: list[o6.NodeId] = o6.field(name="ConfigurationObjects", arrayDimensions=[1])


@o6.datatype(nodeId="ns=fx_data;i=1046", browseName="ns=fx_data;CommunicationConfigurationDataType", defaultEncodingId="ns=fx_data;i=1147", isAbstract=True)
class CommunicationConfigurationDataType(ns0.datatypes.Structure):
    pass


@o6.datatype(nodeId="ns=fx_data;i=1045", browseName="ns=fx_data;PubSubCommunicationConfigurationDataType", defaultEncodingId="ns=fx_data;i=1144")
class PubSubCommunicationConfigurationDataType(CommunicationConfigurationDataType):
    pubSubConfiguration: ns0.datatypes.PubSubConfiguration2DataType = o6.field(name="PubSubConfiguration")
    requireCompleteUpdate: o6.Boolean = o6.field(name="RequireCompleteUpdate")
    configurationReferences: list[ns0.datatypes.PubSubConfigurationRefDataType] = o6.field(name="ConfigurationReferences", arrayDimensions=[1])


@o6.datatype(nodeId="ns=fx_data;i=1048", browseName="ns=fx_data;AssetVerificationDataType", defaultEncodingId="ns=fx_data;i=1153")
class AssetVerificationDataType(ns0.datatypes.Structure):
    assetToVerify: o6.NodeId = o6.field(name="AssetToVerify")
    verificationMode: AssetVerificationModeEnum = o6.field(name="VerificationMode")
    expectedVerificationResult: AssetVerificationResultEnum = o6.field(name="ExpectedVerificationResult")
    expectedVerificationVariables: list[ns0.datatypes.KeyValuePair] = o6.field(name="ExpectedVerificationVariables", arrayDimensions=[1])
    expectedAdditionalVerificationVariables: list[NodeIdValuePair] = o6.field(name="ExpectedAdditionalVerificationVariables", arrayDimensions=[1])


@o6.enumtype(nodeId="ns=fx_data;i=3002", browseName="ns=fx_data;FunctionalEntityVerificationResultEnum")
class FunctionalEntityVerificationResultEnum(ns0.datatypes.Enumeration):
    NOT_SET = o6.enumfield(0, name="NotSet")
    MATCH = o6.enumfield(1, name="Match")
    MISMATCH = o6.enumfield(2, name="Mismatch")


@o6.datatype(nodeId="ns=fx_data;i=3003", browseName="ns=fx_data;RelatedEndpointDataType", defaultEncodingId="ns=fx_data;i=5001")
class RelatedEndpointDataType(ns0.datatypes.Structure):
    address: o6.String = o6.field(name="Address")
    connectionEndpointPath: list[ns0.datatypes.PortableQualifiedName] = o6.field(name="ConnectionEndpointPath", arrayDimensions=[1])
    connectionEndpointName: o6.String = o6.field(name="ConnectionEndpointName")


@o6.datatype(nodeId="ns=fx_data;i=3007", browseName="ns=fx_data;CommunicationLinkConfigurationDataType", defaultEncodingId="ns=fx_data;i=5033", isAbstract=True)
class CommunicationLinkConfigurationDataType(ns0.datatypes.Structure):
    pass


@o6.datatype(nodeId="ns=fx_data;i=1031", browseName="ns=fx_data;PubSubCommunicationLinkConfigurationDataType", defaultEncodingId="ns=fx_data;i=1102")
class PubSubCommunicationLinkConfigurationDataType(CommunicationLinkConfigurationDataType):
    dataSetReaderRef: ns0.datatypes.PubSubConfigurationRefDataType = o6.field(name="DataSetReaderRef")
    expectedSubscribedDataSetVersion: ns0.datatypes.ConfigurationVersionDataType = o6.field(name="ExpectedSubscribedDataSetVersion")
    dataSetWriterRef: ns0.datatypes.PubSubConfigurationRefDataType = o6.field(name="DataSetWriterRef")
    expectedPublishedDataSetVersion: ns0.datatypes.ConfigurationVersionDataType = o6.field(name="ExpectedPublishedDataSetVersion")


@o6.datatype(nodeId="ns=fx_data;i=3008", browseName="ns=fx_data;ConnectionEndpointConfigurationResultDataType", defaultEncodingId="ns=fx_data;i=5036")
class ConnectionEndpointConfigurationResultDataType(ns0.datatypes.Structure):
    connectionEndpointId: o6.NodeId = o6.field(name="ConnectionEndpointId")
    functionalEntityNodeResult: o6.StatusCode = o6.field(name="FunctionalEntityNodeResult")
    connectionEndpointResult: o6.StatusCode = o6.field(name="ConnectionEndpointResult")
    verificationResult: FunctionalEntityVerificationResultEnum = o6.field(name="VerificationResult")
    verificationStatus: o6.StatusCode = o6.field(name="VerificationStatus")
    verificationVariablesErrors: list[o6.StatusCode] = o6.field(name="VerificationVariablesErrors", arrayDimensions=[1])
    establishControlResult: list[o6.StatusCode] = o6.field(name="EstablishControlResult", arrayDimensions=[1])
    configurationDataResult: list[o6.StatusCode] = o6.field(name="ConfigurationDataResult", arrayDimensions=[1])
    reassignControlResult: list[o6.StatusCode] = o6.field(name="ReassignControlResult", arrayDimensions=[1])
    communicationLinksResult: o6.StatusCode = o6.field(name="CommunicationLinksResult")
    enableCommunicationResult: o6.StatusCode = o6.field(name="EnableCommunicationResult")


@o6.datatype(nodeId="ns=fx_data;i=3009", browseName="ns=fx_data;ConnectionEndpointParameterDataType", defaultEncodingId="ns=fx_data;i=5039", isAbstract=True)
class ConnectionEndpointParameterDataType(ns0.datatypes.Structure):
    name: o6.String = o6.field(name="Name")
    connectionEndpointTypeId: o6.NodeId = o6.field(name="ConnectionEndpointTypeId")
    inputVariableIds: list[o6.NodeId] = o6.field(name="InputVariableIds", arrayDimensions=[1])
    outputVariableIds: list[o6.NodeId] = o6.field(name="OutputVariableIds", arrayDimensions=[1])
    isPersistent: o6.Boolean = o6.field(name="IsPersistent")
    cleanupTimeout: o6.Double = o6.field(name="CleanupTimeout")
    relatedEndpoint: RelatedEndpointDataType = o6.field(name="RelatedEndpoint")
    isPreconfigured: o6.Boolean = o6.field(name="IsPreconfigured")


@o6.datatype(nodeId="ns=fx_data;i=3006", browseName="ns=fx_data;PubSubConnectionEndpointParameterDataType", defaultEncodingId="ns=fx_data;i=5060")
class PubSubConnectionEndpointParameterDataType(ConnectionEndpointParameterDataType):
    name: o6.String = o6.field(name="Name")
    connectionEndpointTypeId: o6.NodeId = o6.field(name="ConnectionEndpointTypeId")
    inputVariableIds: list[o6.NodeId] = o6.field(name="InputVariableIds", arrayDimensions=[1])
    outputVariableIds: list[o6.NodeId] = o6.field(name="OutputVariableIds", arrayDimensions=[1])
    isPersistent: o6.Boolean = o6.field(name="IsPersistent")
    cleanupTimeout: o6.Double = o6.field(name="CleanupTimeout")
    relatedEndpoint: RelatedEndpointDataType = o6.field(name="RelatedEndpoint")
    isPreconfigured: o6.Boolean = o6.field(name="IsPreconfigured")
    mode: PubSubConnectionEndpointModeEnum = o6.field(name="Mode")


@o6.datatype(nodeId="ns=fx_data;i=3011", browseName="ns=fx_data;ConnectionEndpointDefinitionDataType", defaultEncodingId="ns=fx_data;i=5054")
class ConnectionEndpointDefinitionDataType(ns0.datatypes.Union):
    parameter: ConnectionEndpointParameterDataType = o6.field(name="Parameter")
    node: o6.NodeId = o6.field(name="Node")


@o6.datatype(nodeId="ns=fx_data;i=1044", browseName="ns=fx_data;ConnectionEndpointConfigurationDataType", defaultEncodingId="ns=fx_data;i=1141")
class ConnectionEndpointConfigurationDataType(ns0.datatypes.Structure):
    functionalEntityNode: o6.NodeId = o6.field(name="FunctionalEntityNode")
    connectionEndpoint: ConnectionEndpointDefinitionDataType = o6.field(name="ConnectionEndpoint")
    expectedVerificationVariables: list[NodeIdValuePair] = o6.field(name="ExpectedVerificationVariables", arrayDimensions=[1])
    controlGroups: list[o6.NodeId] = o6.field(name="ControlGroups", arrayDimensions=[1])
    configurationData: list[NodeIdValuePair] = o6.field(name="ConfigurationData", arrayDimensions=[1])
    communicationLinks: CommunicationLinkConfigurationDataType = o6.field(name="CommunicationLinks")


@o6.enumtype(nodeId="ns=fx_data;i=3012", browseName="ns=fx_data;FxTimeUnitsEnum", description="This enumeration describes the support units of time")
class FxTimeUnitsEnum(ns0.datatypes.Enumeration):
    NANOSECOND = o6.enumfield(0, name="Nanosecond")
    MICROSECOND = o6.enumfield(1, name="Microsecond")
    MILLISECOND = o6.enumfield(2, name="Millisecond")
    SECOND = o6.enumfield(3, name="Second")


@o6.datatype(nodeId="ns=fx_data;i=3017", browseName="ns=fx_data;ReserveCommunicationIdsDataType", defaultEncodingId="ns=fx_data;i=5064", isAbstract=True)
class ReserveCommunicationIdsDataType(ns0.datatypes.Structure):
    pass


@o6.datatype(nodeId="ns=fx_data;i=3018", browseName="ns=fx_data;PubSubReserveCommunicationIdsDataType", defaultEncodingId="ns=fx_data;i=5082")
class PubSubReserveCommunicationIdsDataType(ReserveCommunicationIdsDataType):
    transportProfileUri: o6.String = o6.field(name="TransportProfileUri")
    numReqWriterGroupIds: o6.UInt16 = o6.field(name="NumReqWriterGroupIds")
    numReqDataSetWriterIds: o6.UInt16 = o6.field(name="NumReqDataSetWriterIds")


@o6.datatype(nodeId="ns=fx_data;i=3005", browseName="ns=fx_data;PubSubReserveCommunicationIds2DataType", defaultEncodingId="ns=fx_data;i=5004")
class PubSubReserveCommunicationIds2DataType(PubSubReserveCommunicationIdsDataType):
    transportProfileUri: o6.String = o6.field(name="TransportProfileUri")
    numReqWriterGroupIds: o6.UInt16 = o6.field(name="NumReqWriterGroupIds")
    numReqDataSetWriterIds: o6.UInt16 = o6.field(name="NumReqDataSetWriterIds")
    requestTransportSpecificInfo: o6.Boolean = o6.field(name="RequestTransportSpecificInfo")


@o6.datatype(nodeId="ns=fx_data;i=3019", browseName="ns=fx_data;ReserveCommunicationIdsResultDataType", defaultEncodingId="ns=fx_data;i=5085", isAbstract=True)
class ReserveCommunicationIdsResultDataType(ns0.datatypes.Structure):
    pass


@o6.datatype(nodeId="ns=fx_data;i=3020", browseName="ns=fx_data;PubSubReserveCommunicationIdsResultDataType", defaultEncodingId="ns=fx_data;i=5088")
class PubSubReserveCommunicationIdsResultDataType(ReserveCommunicationIdsResultDataType):
    result: o6.StatusCode = o6.field(name="Result")
    defaultPublisherId: Any = o6.field(name="DefaultPublisherId")
    writerGroupIds: list[o6.UInt16] = o6.field(name="WriterGroupIds", arrayDimensions=[1])
    dataSetWriterIds: list[o6.UInt16] = o6.field(name="DataSetWriterIds", arrayDimensions=[1])


@o6.datatype(nodeId="ns=fx_data;i=3013", browseName="ns=fx_data;PubSubReserveCommunicationIdsResult2DataType", defaultEncodingId="ns=fx_data;i=5007")
class PubSubReserveCommunicationIdsResult2DataType(PubSubReserveCommunicationIdsResultDataType):
    result: o6.StatusCode = o6.field(name="Result")
    defaultPublisherId: Any = o6.field(name="DefaultPublisherId")
    writerGroupIds: list[o6.UInt16] = o6.field(name="WriterGroupIds", arrayDimensions=[1])
    dataSetWriterIds: list[o6.UInt16] = o6.field(name="DataSetWriterIds", arrayDimensions=[1])
    transportSpecificInfo: Any = o6.field(name="TransportSpecificInfo")


@o6.datatype(nodeId="ns=fx_data;i=3021", browseName="ns=fx_data;IntervalRange", defaultEncodingId="ns=fx_data;i=5010")
class IntervalRange(ns0.datatypes.Structure):
    min: o6.UInt32 = o6.field(name="Min")
    max: o6.UInt32 = o6.field(name="Max")
    increment: o6.UInt16 = o6.field(name="Increment")
    multiplier: o6.UInt16 = o6.field(name="Multiplier")
    unit: FxTimeUnitsEnum = o6.field(name="Unit")


del Any, TYPE_CHECKING, uuid, o6, ns0
