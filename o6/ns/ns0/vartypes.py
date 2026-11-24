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
from . import datatypes as ns0_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.variabletype(nodeId="i=62", browseName="BaseVariableType", displayName="BaseVariableType", isAbstract=True, valueRank=o6.ValueRank.ANY)
class BaseVariableType(_VariableNode):
    _nodeid: o6.NodeId
    if TYPE_CHECKING:

        def __init__(
            self,
            *,
            server: object = ...,
            nodeId: o6.NodeIdLike | None = None,
            parent: o6.NodeIdLike | None = None,
            referenceType: o6.NodeIdLike | None = None,
            browseName: str | None = None,
            values: dict[str, object] | None = None,
            references: list[object] | None = None,
            value: object = None,
            dataType: o6.NodeIdLike | None = None,
            valueRank: int | None = None,
            arrayDimensions: list[int] | None = None,
            accessLevel: int | None = None,
            userAccessLevel: int | None = None,
            minimumSamplingInterval: float | None = None,
            historizing: bool = False,
            writeMask: int | None = None,
            userWriteMask: int | None = None,
            rolePermissions: dict[object, int] | None = None,
            accessRestrictions: int = 0,
            eventNotifier: int = 0,
            description: str | None = None,
            displayName: str | None = None,
            modellingRule: str | None = None,
            _allow_abstract: bool = False,
        ) -> None: ...


@o6.variabletype(nodeId="i=63", browseName="BaseDataVariableType", displayName="BaseDataVariableType", valueRank=o6.ValueRank.ANY)
class BaseDataVariableType(BaseVariableType):
    pass


@o6.variabletype(nodeId="i=68", browseName="PropertyType", displayName="PropertyType", valueRank=o6.ValueRank.ANY)
class PropertyType(BaseVariableType):
    pass


@o6.variabletype(nodeId="i=69", browseName="DataTypeDescriptionType", displayName="DataTypeDescriptionType", dataType=o6.String, valueRank=o6.ValueRank.SCALAR)
class DataTypeDescriptionType(BaseDataVariableType):
    dataTypeVersion: PropertyType | None = o6.hasProperty(PropertyType(nodeId="i=104", browseName="DataTypeVersion", modellingRule="Optional", dataType=o6.String, valueRank=-1))
    dictionaryFragment: PropertyType | None = o6.hasProperty(
        PropertyType(nodeId="i=105", browseName="DictionaryFragment", modellingRule="Optional", dataType=o6.ByteString, valueRank=-1)
    )


@o6.variabletype(nodeId="i=2137", browseName="ServerVendorCapabilityType", displayName="ServerVendorCapabilityType", isAbstract=True, valueRank=o6.ValueRank.SCALAR)
class ServerVendorCapabilityType(BaseDataVariableType):
    pass


@o6.variabletype(
    nodeId="i=2150",
    browseName="ServerDiagnosticsSummaryType",
    displayName="ServerDiagnosticsSummaryType",
    dataType=ns0_datypes.ServerDiagnosticsSummaryDataType,
    valueRank=o6.ValueRank.SCALAR,
)
class ServerDiagnosticsSummaryType(BaseDataVariableType):
    cumulatedSessionCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2153", browseName="CumulatedSessionCount", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    cumulatedSubscriptionCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2161", browseName="CumulatedSubscriptionCount", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    currentSessionCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2152", browseName="CurrentSessionCount", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    currentSubscriptionCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2160", browseName="CurrentSubscriptionCount", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    publishingIntervalCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2159", browseName="PublishingIntervalCount", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    rejectedRequestsCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2163", browseName="RejectedRequestsCount", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    rejectedSessionCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2155", browseName="RejectedSessionCount", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    securityRejectedRequestsCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2162", browseName="SecurityRejectedRequestsCount", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    securityRejectedSessionCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2154", browseName="SecurityRejectedSessionCount", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    serverViewCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2151", browseName="ServerViewCount", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    sessionAbortCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2157", browseName="SessionAbortCount", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    sessionTimeoutCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2156", browseName="SessionTimeoutCount", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )


@o6.variabletype(
    nodeId="i=2164",
    browseName="SamplingIntervalDiagnosticsArrayType",
    displayName="SamplingIntervalDiagnosticsArrayType",
    dataType=ns0_datypes.SamplingIntervalDiagnosticsDataType,
    valueRank=o6.ValueRank.ARRAY_1D,
    arrayDimensions=[0],
)
class SamplingIntervalDiagnosticsArrayType(BaseDataVariableType):
    samplingIntervalDiagnostics: SamplingIntervalDiagnosticsType


@o6.variabletype(
    nodeId="i=2171",
    browseName="SubscriptionDiagnosticsArrayType",
    displayName="SubscriptionDiagnosticsArrayType",
    dataType=ns0_datypes.SubscriptionDiagnosticsDataType,
    valueRank=o6.ValueRank.ARRAY_1D,
    arrayDimensions=[0],
)
class SubscriptionDiagnosticsArrayType(BaseDataVariableType):
    subscriptionDiagnostics: SubscriptionDiagnosticsType


@o6.variabletype(
    nodeId="i=2196",
    browseName="SessionDiagnosticsArrayType",
    displayName="SessionDiagnosticsArrayType",
    dataType=ns0_datypes.SessionDiagnosticsDataType,
    valueRank=o6.ValueRank.ARRAY_1D,
    arrayDimensions=[0],
)
class SessionDiagnosticsArrayType(BaseDataVariableType):
    sessionDiagnostics: SessionDiagnosticsVariableType


@o6.variabletype(
    nodeId="i=2243",
    browseName="SessionSecurityDiagnosticsArrayType",
    displayName="SessionSecurityDiagnosticsArrayType",
    dataType=ns0_datypes.SessionSecurityDiagnosticsDataType,
    valueRank=o6.ValueRank.ARRAY_1D,
    arrayDimensions=[0],
)
class SessionSecurityDiagnosticsArrayType(BaseDataVariableType):
    sessionSecurityDiagnostics: SessionSecurityDiagnosticsType


@o6.variabletype(nodeId="i=2365", browseName="DataItemType", displayName="DataItemType", valueRank=o6.ValueRank.ANY)
class DataItemType(BaseDataVariableType):
    definition: PropertyType | None = o6.hasProperty(PropertyType(nodeId="i=2366", browseName="Definition", modellingRule="Optional", dataType=o6.String, valueRank=-1))
    valuePrecision: PropertyType | None = o6.hasProperty(PropertyType(nodeId="i=2367", browseName="ValuePrecision", modellingRule="Optional", dataType=o6.Double, valueRank=-1))


@o6.variabletype(nodeId="i=2372", browseName="DiscreteItemType", displayName="DiscreteItemType", isAbstract=True, valueRank=o6.ValueRank.ANY)
class DiscreteItemType(DataItemType):
    pass


@o6.variabletype(nodeId="i=2373", browseName="TwoStateDiscreteType", displayName="TwoStateDiscreteType", dataType=o6.Boolean, valueRank=o6.ValueRank.ANY)
class TwoStateDiscreteType(DiscreteItemType):
    falseState: PropertyType = o6.hasProperty(PropertyType(nodeId="i=2374", browseName="FalseState", modellingRule="Mandatory", dataType=o6.LocalizedText, valueRank=-1))
    trueState: PropertyType = o6.hasProperty(PropertyType(nodeId="i=2375", browseName="TrueState", modellingRule="Mandatory", dataType=o6.LocalizedText, valueRank=-1))


@o6.variabletype(nodeId="i=2376", browseName="MultiStateDiscreteType", displayName="MultiStateDiscreteType", dataType=ns0_datypes.UInteger, valueRank=o6.ValueRank.ANY)
class MultiStateDiscreteType(DiscreteItemType):
    enumStrings: PropertyType = o6.hasProperty(
        PropertyType(nodeId="i=2377", browseName="EnumStrings", modellingRule="Mandatory", dataType=o6.LocalizedText, valueRank=1, arrayDimensions=[0])
    )


@o6.variabletype(
    nodeId="i=2380", browseName="ProgramDiagnosticType", displayName="ProgramDiagnosticType", dataType=ns0_datypes.ProgramDiagnosticDataType, valueRank=o6.ValueRank.SCALAR
)
class ProgramDiagnosticType(BaseDataVariableType):
    createClientName: PropertyType = o6.hasProperty(PropertyType(nodeId="i=2382", browseName="CreateClientName", modellingRule="Mandatory", dataType=o6.String, valueRank=-1))
    createSessionId: PropertyType = o6.hasProperty(PropertyType(nodeId="i=2381", browseName="CreateSessionId", modellingRule="Mandatory", dataType=o6.NodeId, valueRank=-1))
    invocationCreationTime: PropertyType = o6.hasProperty(
        PropertyType(nodeId="i=2383", browseName="InvocationCreationTime", modellingRule="Mandatory", dataType=ns0_datypes.UtcTime, valueRank=-1)
    )
    lastMethodCall: PropertyType = o6.hasProperty(PropertyType(nodeId="i=2385", browseName="LastMethodCall", modellingRule="Mandatory", dataType=o6.String, valueRank=-1))
    lastMethodCallTime: PropertyType = o6.hasProperty(
        PropertyType(nodeId="i=2389", browseName="LastMethodCallTime", modellingRule="Mandatory", dataType=ns0_datypes.UtcTime, valueRank=-1)
    )
    lastMethodInputArguments: PropertyType = o6.hasProperty(
        PropertyType(nodeId="i=2387", browseName="LastMethodInputArguments", modellingRule="Mandatory", valueRank=1, arrayDimensions=[0])
    )
    lastMethodOutputArguments: PropertyType = o6.hasProperty(
        PropertyType(nodeId="i=2388", browseName="LastMethodOutputArguments", modellingRule="Mandatory", valueRank=1, arrayDimensions=[0])
    )
    lastMethodReturnStatus: PropertyType = o6.hasProperty(
        PropertyType(nodeId="i=2390", browseName="LastMethodReturnStatus", modellingRule="Mandatory", dataType=ns0_datypes.StatusResult, valueRank=-1)
    )
    lastMethodSessionId: PropertyType = o6.hasProperty(PropertyType(nodeId="i=2386", browseName="LastMethodSessionId", modellingRule="Mandatory", dataType=o6.NodeId, valueRank=-1))
    lastTransitionTime: PropertyType = o6.hasProperty(
        PropertyType(nodeId="i=2384", browseName="LastTransitionTime", modellingRule="Mandatory", dataType=ns0_datypes.UtcTime, valueRank=-1)
    )


@o6.variabletype(nodeId="i=2138", browseName="ServerStatusType", displayName="ServerStatusType", dataType=ns0_datypes.ServerStatusDataType, valueRank=o6.ValueRank.SCALAR)
class ServerStatusType(BaseDataVariableType):
    buildInfo: BuildInfoType
    currentTime: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2140", browseName="CurrentTime", modellingRule="Mandatory", dataType=ns0_datypes.UtcTime, valueRank=-1)
    )
    secondsTillShutdown: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2752", browseName="SecondsTillShutdown", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    shutdownReason: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2753", browseName="ShutdownReason", modellingRule="Mandatory", dataType=o6.LocalizedText, valueRank=-1)
    )
    startTime: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2139", browseName="StartTime", modellingRule="Mandatory", dataType=ns0_datypes.UtcTime, valueRank=-1)
    )
    state: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2141", browseName="State", modellingRule="Mandatory", dataType=ns0_datypes.ServerState, valueRank=-1)
    )


@o6.variabletype(nodeId="i=2755", browseName="StateVariableType", displayName="StateVariableType", dataType=o6.LocalizedText, valueRank=o6.ValueRank.SCALAR)
class StateVariableType(BaseDataVariableType):
    effectiveDisplayName: PropertyType | None = o6.hasProperty(
        PropertyType(nodeId="i=2759", browseName="EffectiveDisplayName", modellingRule="Optional", dataType=o6.LocalizedText, valueRank=-1)
    )
    id: PropertyType = o6.hasProperty(PropertyType(nodeId="i=2756", browseName="Id", modellingRule="Mandatory", valueRank=-1))
    name: PropertyType | None = o6.hasProperty(PropertyType(nodeId="i=2757", browseName="Name", modellingRule="Optional", dataType=o6.QualifiedName, valueRank=-1))
    number: PropertyType | None = o6.hasProperty(PropertyType(nodeId="i=2758", browseName="Number", modellingRule="Optional", dataType=o6.UInt32, valueRank=-1))


@o6.variabletype(nodeId="i=2760", browseName="FiniteStateVariableType", displayName="FiniteStateVariableType", dataType=o6.LocalizedText, valueRank=o6.ValueRank.SCALAR)
class FiniteStateVariableType(StateVariableType):
    id: PropertyType = o6.hasProperty(PropertyType(nodeId="i=2761", browseName="Id", modellingRule="Mandatory", dataType=o6.NodeId, valueRank=-1))


@o6.variabletype(nodeId="i=3051", browseName="BuildInfoType", displayName="BuildInfoType", dataType=ns0_datypes.BuildInfo, valueRank=o6.ValueRank.SCALAR)
class BuildInfoType(BaseDataVariableType):
    buildDate: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=3057", browseName="BuildDate", modellingRule="Mandatory", dataType=ns0_datypes.UtcTime, valueRank=-1)
    )
    buildNumber: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=3056", browseName="BuildNumber", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )
    manufacturerName: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=3053", browseName="ManufacturerName", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )
    productName: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=3054", browseName="ProductName", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )
    productUri: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=3052", browseName="ProductUri", modellingRule="Mandatory", dataType=o6.String, valueRank=-1))
    softwareVersion: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=3055", browseName="SoftwareVersion", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )


@o6.variabletype(
    nodeId="i=2244",
    browseName="SessionSecurityDiagnosticsType",
    displayName="SessionSecurityDiagnosticsType",
    dataType=ns0_datypes.SessionSecurityDiagnosticsDataType,
    valueRank=o6.ValueRank.SCALAR,
)
class SessionSecurityDiagnosticsType(BaseDataVariableType):
    authenticationMechanism: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2248", browseName="AuthenticationMechanism", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )
    clientCertificate: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=3058", browseName="ClientCertificate", modellingRule="Mandatory", dataType=o6.ByteString, valueRank=-1)
    )
    clientUserIdHistory: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2247", browseName="ClientUserIdHistory", modellingRule="Mandatory", dataType=o6.String, valueRank=1, arrayDimensions=[0])
    )
    clientUserIdOfSession: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2246", browseName="ClientUserIdOfSession", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )
    encoding: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2249", browseName="Encoding", modellingRule="Mandatory", dataType=o6.String, valueRank=-1))
    securityMode: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2251", browseName="SecurityMode", modellingRule="Mandatory", dataType=ns0_datypes.MessageSecurityMode, valueRank=-1)
    )
    securityPolicyUri: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2252", browseName="SecurityPolicyUri", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )
    sessionId: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2245", browseName="SessionId", modellingRule="Mandatory", dataType=o6.NodeId, valueRank=-1))
    transportProtocol: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2250", browseName="TransportProtocol", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )


@o6.variabletype(
    nodeId="i=2172",
    browseName="SubscriptionDiagnosticsType",
    displayName="SubscriptionDiagnosticsType",
    dataType=ns0_datypes.SubscriptionDiagnosticsDataType,
    valueRank=o6.ValueRank.SCALAR,
)
class SubscriptionDiagnosticsType(BaseDataVariableType):
    currentKeepAliveCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=8890", browseName="CurrentKeepAliveCount", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    currentLifetimeCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=8891", browseName="CurrentLifetimeCount", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    dataChangeNotificationsCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2191", browseName="DataChangeNotificationsCount", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    disableCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2183", browseName="DisableCount", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    disabledMonitoredItemCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=8895", browseName="DisabledMonitoredItemCount", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    discardedMessageCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=8893", browseName="DiscardedMessageCount", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    enableCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2182", browseName="EnableCount", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    eventNotificationsCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2998", browseName="EventNotificationsCount", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    eventQueueOverflowCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=8902", browseName="EventQueueOverflowCount", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    latePublishRequestCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=8889", browseName="LatePublishRequestCount", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    maxKeepAliveCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2177", browseName="MaxKeepAliveCount", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    maxLifetimeCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=8888", browseName="MaxLifetimeCount", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    maxNotificationsPerPublish: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2179", browseName="MaxNotificationsPerPublish", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    modifyCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2181", browseName="ModifyCount", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    monitoredItemCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=8894", browseName="MonitoredItemCount", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    monitoringQueueOverflowCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=8896", browseName="MonitoringQueueOverflowCount", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    nextSequenceNumber: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=8897", browseName="NextSequenceNumber", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    notificationsCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2193", browseName="NotificationsCount", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    priority: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2175", browseName="Priority", modellingRule="Mandatory", dataType=o6.Byte, valueRank=-1))
    publishRequestCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2190", browseName="PublishRequestCount", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    publishingEnabled: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2180", browseName="PublishingEnabled", modellingRule="Mandatory", dataType=o6.Boolean, valueRank=-1)
    )
    publishingInterval: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2176", browseName="PublishingInterval", modellingRule="Mandatory", dataType=ns0_datypes.Duration, valueRank=-1)
    )
    republishMessageCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2186", browseName="RepublishMessageCount", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    republishMessageRequestCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2185", browseName="RepublishMessageRequestCount", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    republishRequestCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2184", browseName="RepublishRequestCount", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    sessionId: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2173", browseName="SessionId", modellingRule="Mandatory", dataType=o6.NodeId, valueRank=-1))
    subscriptionId: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2174", browseName="SubscriptionId", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    transferRequestCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2187", browseName="TransferRequestCount", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    transferredToAltClientCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2188", browseName="TransferredToAltClientCount", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    transferredToSameClientCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2189", browseName="TransferredToSameClientCount", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    unacknowledgedMessageCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=8892", browseName="UnacknowledgedMessageCount", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )


@o6.variabletype(nodeId="i=9002", browseName="ConditionVariableType", displayName="ConditionVariableType", valueRank=o6.ValueRank.ANY)
class ConditionVariableType(BaseDataVariableType):
    sourceTimestamp: PropertyType = o6.hasProperty(
        PropertyType(nodeId="i=9003", browseName="SourceTimestamp", modellingRule="Mandatory", dataType=ns0_datypes.UtcTime, valueRank=-1)
    )


@o6.variabletype(nodeId="i=8995", browseName="TwoStateVariableType", displayName="TwoStateVariableType", dataType=o6.LocalizedText, valueRank=o6.ValueRank.SCALAR)
class TwoStateVariableType(StateVariableType):
    effectiveTransitionTime: PropertyType | None = o6.hasProperty(
        PropertyType(nodeId="i=9001", browseName="EffectiveTransitionTime", modellingRule="Optional", dataType=ns0_datypes.UtcTime, valueRank=-1)
    )
    falseState: PropertyType | None = o6.hasProperty(PropertyType(nodeId="i=11111", browseName="FalseState", modellingRule="Optional", dataType=o6.LocalizedText, valueRank=-1))
    id: PropertyType = o6.hasProperty(PropertyType(nodeId="i=8996", browseName="Id", modellingRule="Mandatory", dataType=o6.Boolean, valueRank=-1))
    transitionTime: PropertyType | None = o6.hasProperty(
        PropertyType(nodeId="i=9000", browseName="TransitionTime", modellingRule="Optional", dataType=ns0_datypes.UtcTime, valueRank=-1)
    )
    trueState: PropertyType | None = o6.hasProperty(PropertyType(nodeId="i=11110", browseName="TrueState", modellingRule="Optional", dataType=o6.LocalizedText, valueRank=-1))


@o6.variabletype(nodeId="i=2762", browseName="TransitionVariableType", displayName="TransitionVariableType", dataType=o6.LocalizedText, valueRank=o6.ValueRank.SCALAR)
class TransitionVariableType(BaseDataVariableType):
    effectiveTransitionTime: PropertyType | None = o6.hasProperty(
        PropertyType(nodeId="i=11456", browseName="EffectiveTransitionTime", modellingRule="Optional", dataType=ns0_datypes.UtcTime, valueRank=-1)
    )
    id: PropertyType = o6.hasProperty(PropertyType(nodeId="i=2763", browseName="Id", modellingRule="Mandatory", valueRank=-1))
    name: PropertyType | None = o6.hasProperty(PropertyType(nodeId="i=2764", browseName="Name", modellingRule="Optional", dataType=o6.QualifiedName, valueRank=-1))
    number: PropertyType | None = o6.hasProperty(PropertyType(nodeId="i=2765", browseName="Number", modellingRule="Optional", dataType=o6.UInt32, valueRank=-1))
    transitionTime: PropertyType | None = o6.hasProperty(
        PropertyType(nodeId="i=2766", browseName="TransitionTime", modellingRule="Optional", dataType=ns0_datypes.UtcTime, valueRank=-1)
    )


@o6.variabletype(nodeId="i=2767", browseName="FiniteTransitionVariableType", displayName="FiniteTransitionVariableType", dataType=o6.LocalizedText, valueRank=o6.ValueRank.SCALAR)
class FiniteTransitionVariableType(TransitionVariableType):
    id: PropertyType = o6.hasProperty(PropertyType(nodeId="i=2768", browseName="Id", modellingRule="Mandatory", dataType=o6.NodeId, valueRank=-1))


@o6.variabletype(nodeId="i=11238", browseName="MultiStateValueDiscreteType", displayName="MultiStateValueDiscreteType", dataType=ns0_datypes.Number, valueRank=o6.ValueRank.ANY)
class MultiStateValueDiscreteType(DiscreteItemType):
    enumValues: PropertyType = o6.hasProperty(
        PropertyType(nodeId="i=11241", browseName="EnumValues", modellingRule="Mandatory", dataType=ns0_datypes.EnumValueType, valueRank=1, arrayDimensions=[0])
    )
    valueAsText: PropertyType = o6.hasProperty(PropertyType(nodeId="i=11461", browseName="ValueAsText", modellingRule="Mandatory", dataType=o6.LocalizedText, valueRank=-1))


@o6.variabletype(
    nodeId="i=2165",
    browseName="SamplingIntervalDiagnosticsType",
    displayName="SamplingIntervalDiagnosticsType",
    dataType=ns0_datypes.SamplingIntervalDiagnosticsDataType,
    valueRank=o6.ValueRank.SCALAR,
)
class SamplingIntervalDiagnosticsType(BaseDataVariableType):
    disabledMonitoredItemsSamplingCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=11699", browseName="DisabledMonitoredItemsSamplingCount", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    maxSampledMonitoredItemsCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=11698", browseName="MaxSampledMonitoredItemsCount", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    sampledMonitoredItemsCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=11697", browseName="SampledMonitoredItemsCount", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    samplingInterval: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2166", browseName="SamplingInterval", modellingRule="Mandatory", dataType=ns0_datypes.Duration, valueRank=-1)
    )


@o6.variabletype(nodeId="i=11487", browseName="OptionSetType", displayName="OptionSetType", valueRank=o6.ValueRank.SCALAR)
class OptionSetType(BaseDataVariableType):
    bitMask: PropertyType | None = o6.hasProperty(
        PropertyType(nodeId="i=11701", browseName="BitMask", modellingRule="Optional", dataType=o6.Boolean, valueRank=1, arrayDimensions=[0])
    )
    optionSetValues: PropertyType = o6.hasProperty(
        PropertyType(nodeId="i=11488", browseName="OptionSetValues", modellingRule="Mandatory", dataType=o6.LocalizedText, valueRank=1, arrayDimensions=[0])
    )


@o6.variabletype(
    nodeId="i=2197",
    browseName="SessionDiagnosticsVariableType",
    displayName="SessionDiagnosticsVariableType",
    dataType=ns0_datypes.SessionDiagnosticsDataType,
    valueRank=o6.ValueRank.SCALAR,
)
class SessionDiagnosticsVariableType(BaseDataVariableType):
    actualSessionTimeout: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2204", browseName="ActualSessionTimeout", modellingRule="Mandatory", dataType=ns0_datypes.Duration, valueRank=-1)
    )
    addNodesCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2234", browseName="AddNodesCount", modellingRule="Mandatory", dataType=ns0_datypes.ServiceCounterDataType, valueRank=-1)
    )
    addReferencesCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2235", browseName="AddReferencesCount", modellingRule="Mandatory", dataType=ns0_datypes.ServiceCounterDataType, valueRank=-1)
    )
    browseCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2238", browseName="BrowseCount", modellingRule="Mandatory", dataType=ns0_datypes.ServiceCounterDataType, valueRank=-1)
    )
    browseNextCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2239", browseName="BrowseNextCount", modellingRule="Mandatory", dataType=ns0_datypes.ServiceCounterDataType, valueRank=-1)
    )
    callCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2221", browseName="CallCount", modellingRule="Mandatory", dataType=ns0_datypes.ServiceCounterDataType, valueRank=-1)
    )
    clientConnectionTime: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2205", browseName="ClientConnectionTime", modellingRule="Mandatory", dataType=ns0_datypes.UtcTime, valueRank=-1)
    )
    clientDescription: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2200", browseName="ClientDescription", modellingRule="Mandatory", dataType=ns0_datypes.ApplicationDescription, valueRank=-1)
    )
    clientLastContactTime: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2206", browseName="ClientLastContactTime", modellingRule="Mandatory", dataType=ns0_datypes.UtcTime, valueRank=-1)
    )
    createMonitoredItemsCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2222", browseName="CreateMonitoredItemsCount", modellingRule="Mandatory", dataType=ns0_datypes.ServiceCounterDataType, valueRank=-1)
    )
    createSubscriptionCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2227", browseName="CreateSubscriptionCount", modellingRule="Mandatory", dataType=ns0_datypes.ServiceCounterDataType, valueRank=-1)
    )
    currentMonitoredItemsCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2208", browseName="CurrentMonitoredItemsCount", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    currentPublishRequestsInQueue: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2209", browseName="CurrentPublishRequestsInQueue", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    currentSubscriptionsCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2207", browseName="CurrentSubscriptionsCount", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    deleteMonitoredItemsCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2226", browseName="DeleteMonitoredItemsCount", modellingRule="Mandatory", dataType=ns0_datypes.ServiceCounterDataType, valueRank=-1)
    )
    deleteNodesCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2236", browseName="DeleteNodesCount", modellingRule="Mandatory", dataType=ns0_datypes.ServiceCounterDataType, valueRank=-1)
    )
    deleteReferencesCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2237", browseName="DeleteReferencesCount", modellingRule="Mandatory", dataType=ns0_datypes.ServiceCounterDataType, valueRank=-1)
    )
    deleteSubscriptionsCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2233", browseName="DeleteSubscriptionsCount", modellingRule="Mandatory", dataType=ns0_datypes.ServiceCounterDataType, valueRank=-1)
    )
    endpointUrl: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2202", browseName="EndpointUrl", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )
    historyReadCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2218", browseName="HistoryReadCount", modellingRule="Mandatory", dataType=ns0_datypes.ServiceCounterDataType, valueRank=-1)
    )
    historyUpdateCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2220", browseName="HistoryUpdateCount", modellingRule="Mandatory", dataType=ns0_datypes.ServiceCounterDataType, valueRank=-1)
    )
    localeIds: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2203", browseName="LocaleIds", modellingRule="Mandatory", dataType=ns0_datypes.LocaleId, valueRank=1, arrayDimensions=[0])
    )
    maxResponseMessageSize: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=3050", browseName="MaxResponseMessageSize", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    modifyMonitoredItemsCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2223", browseName="ModifyMonitoredItemsCount", modellingRule="Mandatory", dataType=ns0_datypes.ServiceCounterDataType, valueRank=-1)
    )
    modifySubscriptionCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2228", browseName="ModifySubscriptionCount", modellingRule="Mandatory", dataType=ns0_datypes.ServiceCounterDataType, valueRank=-1)
    )
    publishCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2230", browseName="PublishCount", modellingRule="Mandatory", dataType=ns0_datypes.ServiceCounterDataType, valueRank=-1)
    )
    queryFirstCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2241", browseName="QueryFirstCount", modellingRule="Mandatory", dataType=ns0_datypes.ServiceCounterDataType, valueRank=-1)
    )
    queryNextCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2242", browseName="QueryNextCount", modellingRule="Mandatory", dataType=ns0_datypes.ServiceCounterDataType, valueRank=-1)
    )
    readCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2217", browseName="ReadCount", modellingRule="Mandatory", dataType=ns0_datypes.ServiceCounterDataType, valueRank=-1)
    )
    registerNodesCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2730", browseName="RegisterNodesCount", modellingRule="Mandatory", dataType=ns0_datypes.ServiceCounterDataType, valueRank=-1)
    )
    republishCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2231", browseName="RepublishCount", modellingRule="Mandatory", dataType=ns0_datypes.ServiceCounterDataType, valueRank=-1)
    )
    serverUri: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2201", browseName="ServerUri", modellingRule="Mandatory", dataType=o6.String, valueRank=-1))
    sessionId: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2198", browseName="SessionId", modellingRule="Mandatory", dataType=o6.NodeId, valueRank=-1))
    sessionName: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2199", browseName="SessionName", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )
    setMonitoringModeCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2224", browseName="SetMonitoringModeCount", modellingRule="Mandatory", dataType=ns0_datypes.ServiceCounterDataType, valueRank=-1)
    )
    setPublishingModeCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2229", browseName="SetPublishingModeCount", modellingRule="Mandatory", dataType=ns0_datypes.ServiceCounterDataType, valueRank=-1)
    )
    setTriggeringCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2225", browseName="SetTriggeringCount", modellingRule="Mandatory", dataType=ns0_datypes.ServiceCounterDataType, valueRank=-1)
    )
    totalRequestCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=8900", browseName="TotalRequestCount", modellingRule="Mandatory", dataType=ns0_datypes.ServiceCounterDataType, valueRank=-1)
    )
    transferSubscriptionsCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2232", browseName="TransferSubscriptionsCount", modellingRule="Mandatory", dataType=ns0_datypes.ServiceCounterDataType, valueRank=-1)
    )
    translateBrowsePathsToNodeIdsCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2240", browseName="TranslateBrowsePathsToNodeIdsCount", modellingRule="Mandatory", dataType=ns0_datypes.ServiceCounterDataType, valueRank=-1)
    )
    unauthorizedRequestCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=11892", browseName="UnauthorizedRequestCount", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    unregisterNodesCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2731", browseName="UnregisterNodesCount", modellingRule="Mandatory", dataType=ns0_datypes.ServiceCounterDataType, valueRank=-1)
    )
    writeCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2219", browseName="WriteCount", modellingRule="Mandatory", dataType=ns0_datypes.ServiceCounterDataType, valueRank=-1)
    )


@o6.variabletype(nodeId="i=12021", browseName="ArrayItemType", displayName="ArrayItemType", isAbstract=True, valueRank=o6.ValueRank.ARRAY_ANY)
class ArrayItemType(DataItemType):
    axisScaleType: PropertyType = o6.hasProperty(
        PropertyType(nodeId="i=12028", browseName="AxisScaleType", modellingRule="Mandatory", dataType=ns0_datypes.AxisScaleEnumeration, valueRank=-1)
    )
    eURange: PropertyType = o6.hasProperty(PropertyType(nodeId="i=12025", browseName="EURange", modellingRule="Mandatory", dataType=ns0_datypes.Range, valueRank=-1))
    engineeringUnits: PropertyType = o6.hasProperty(
        PropertyType(nodeId="i=12026", browseName="EngineeringUnits", modellingRule="Mandatory", dataType=ns0_datypes.EUInformation, valueRank=-1)
    )
    instrumentRange: PropertyType | None = o6.hasProperty(
        PropertyType(nodeId="i=12024", browseName="InstrumentRange", modellingRule="Optional", dataType=ns0_datypes.Range, valueRank=-1)
    )
    title: PropertyType = o6.hasProperty(PropertyType(nodeId="i=12027", browseName="Title", modellingRule="Mandatory", dataType=o6.LocalizedText, valueRank=-1))


@o6.variabletype(nodeId="i=12029", browseName="YArrayItemType", displayName="YArrayItemType", valueRank=o6.ValueRank.ARRAY_1D, arrayDimensions=[0])
class YArrayItemType(ArrayItemType):
    xAxisDefinition: PropertyType = o6.hasProperty(
        PropertyType(nodeId="i=12037", browseName="XAxisDefinition", modellingRule="Mandatory", dataType=ns0_datypes.AxisInformation, valueRank=-1)
    )


@o6.variabletype(nodeId="i=12038", browseName="XYArrayItemType", displayName="XYArrayItemType", dataType=ns0_datypes.XVType, valueRank=o6.ValueRank.ARRAY_1D, arrayDimensions=[0])
class XYArrayItemType(ArrayItemType):
    xAxisDefinition: PropertyType = o6.hasProperty(
        PropertyType(nodeId="i=12046", browseName="XAxisDefinition", modellingRule="Mandatory", dataType=ns0_datypes.AxisInformation, valueRank=-1)
    )


@o6.variabletype(nodeId="i=12047", browseName="ImageItemType", displayName="ImageItemType", valueRank=o6.ValueRank.ARRAY_2D, arrayDimensions=[0, 0])
class ImageItemType(ArrayItemType):
    xAxisDefinition: PropertyType = o6.hasProperty(
        PropertyType(nodeId="i=12055", browseName="XAxisDefinition", modellingRule="Mandatory", dataType=ns0_datypes.AxisInformation, valueRank=-1)
    )
    yAxisDefinition: PropertyType = o6.hasProperty(
        PropertyType(nodeId="i=12056", browseName="YAxisDefinition", modellingRule="Mandatory", dataType=ns0_datypes.AxisInformation, valueRank=-1)
    )


@o6.variabletype(nodeId="i=12057", browseName="CubeItemType", displayName="CubeItemType", valueRank=3, arrayDimensions=[0, 0, 0])
class CubeItemType(ArrayItemType):
    xAxisDefinition: PropertyType = o6.hasProperty(
        PropertyType(nodeId="i=12065", browseName="XAxisDefinition", modellingRule="Mandatory", dataType=ns0_datypes.AxisInformation, valueRank=-1)
    )
    yAxisDefinition: PropertyType = o6.hasProperty(
        PropertyType(nodeId="i=12066", browseName="YAxisDefinition", modellingRule="Mandatory", dataType=ns0_datypes.AxisInformation, valueRank=-1)
    )
    zAxisDefinition: PropertyType = o6.hasProperty(
        PropertyType(nodeId="i=12067", browseName="ZAxisDefinition", modellingRule="Mandatory", dataType=ns0_datypes.AxisInformation, valueRank=-1)
    )


@o6.variabletype(nodeId="i=12068", browseName="NDimensionArrayItemType", displayName="NDimensionArrayItemType", valueRank=o6.ValueRank.ARRAY_ANY)
class NDimensionArrayItemType(ArrayItemType):
    axisDefinition: PropertyType = o6.hasProperty(
        PropertyType(nodeId="i=12076", browseName="AxisDefinition", modellingRule="Mandatory", dataType=ns0_datypes.AxisInformation, valueRank=1, arrayDimensions=[0])
    )


@o6.variabletype(nodeId="i=72", browseName="DataTypeDictionaryType", displayName="DataTypeDictionaryType", dataType=o6.ByteString, valueRank=o6.ValueRank.SCALAR)
class DataTypeDictionaryType(BaseDataVariableType):
    dataTypeVersion: PropertyType | None = o6.hasProperty(PropertyType(nodeId="i=106", browseName="DataTypeVersion", modellingRule="Optional", dataType=o6.String, valueRank=-1))
    deprecated: PropertyType | None = o6.hasProperty(PropertyType(nodeId="i=15001", browseName="Deprecated", modellingRule="Optional", dataType=o6.Boolean, valueRank=-1))
    namespaceUri: PropertyType | None = o6.hasProperty(PropertyType(nodeId="i=107", browseName="NamespaceUri", modellingRule="Optional", dataType=o6.String, valueRank=-1))


@o6.variabletype(nodeId="i=15113", browseName="GuardVariableType", displayName="GuardVariableType", dataType=o6.LocalizedText, valueRank=o6.ValueRank.SCALAR)
class GuardVariableType(BaseDataVariableType):
    pass


@o6.variabletype(nodeId="i=15128", browseName="ExpressionGuardVariableType", displayName="ExpressionGuardVariableType", dataType=o6.LocalizedText, valueRank=o6.ValueRank.SCALAR)
class ExpressionGuardVariableType(GuardVariableType):
    expression: PropertyType = o6.hasProperty(PropertyType(nodeId="i=15129", browseName="Expression", modellingRule="Mandatory", dataType=ns0_datypes.ContentFilter, valueRank=-1))


@o6.variabletype(nodeId="i=15317", browseName="ElseGuardVariableType", displayName="ElseGuardVariableType", dataType=o6.LocalizedText, valueRank=o6.ValueRank.SCALAR)
class ElseGuardVariableType(GuardVariableType):
    pass


@o6.variabletype(
    nodeId="i=15383", browseName="ProgramDiagnostic2Type", displayName="ProgramDiagnostic2Type", dataType=ns0_datypes.ProgramDiagnostic2DataType, valueRank=o6.ValueRank.SCALAR
)
class ProgramDiagnostic2Type(BaseDataVariableType):
    createClientName: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=15385", browseName="CreateClientName", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )
    createSessionId: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=15384", browseName="CreateSessionId", modellingRule="Mandatory", dataType=o6.NodeId, valueRank=-1)
    )
    invocationCreationTime: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=15386", browseName="InvocationCreationTime", modellingRule="Mandatory", dataType=ns0_datypes.UtcTime, valueRank=-1)
    )
    lastMethodCall: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=15388", browseName="LastMethodCall", modellingRule="Mandatory", dataType=o6.String, valueRank=-1)
    )
    lastMethodCallTime: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=15394", browseName="LastMethodCallTime", modellingRule="Mandatory", dataType=ns0_datypes.UtcTime, valueRank=-1)
    )
    lastMethodInputArguments: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=15390", browseName="LastMethodInputArguments", modellingRule="Mandatory", dataType=ns0_datypes.Argument, valueRank=1, arrayDimensions=[0])
    )
    lastMethodInputValues: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=15392", browseName="LastMethodInputValues", modellingRule="Mandatory", valueRank=1, arrayDimensions=[0])
    )
    lastMethodOutputArguments: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=15391", browseName="LastMethodOutputArguments", modellingRule="Mandatory", dataType=ns0_datypes.Argument, valueRank=1, arrayDimensions=[0])
    )
    lastMethodOutputValues: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=15393", browseName="LastMethodOutputValues", modellingRule="Mandatory", valueRank=1, arrayDimensions=[0])
    )
    lastMethodReturnStatus: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=15395", browseName="LastMethodReturnStatus", modellingRule="Mandatory", dataType=o6.StatusCode, valueRank=-1)
    )
    lastMethodSessionId: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=15389", browseName="LastMethodSessionId", modellingRule="Mandatory", dataType=o6.NodeId, valueRank=-1)
    )
    lastTransitionTime: PropertyType = o6.hasProperty(
        PropertyType(nodeId="i=15387", browseName="LastTransitionTime", modellingRule="Mandatory", dataType=ns0_datypes.UtcTime, valueRank=-1)
    )


@o6.variabletype(nodeId="i=17277", browseName="AlarmRateVariableType", displayName="AlarmRateVariableType", dataType=o6.Double, valueRank=o6.ValueRank.SCALAR)
class AlarmRateVariableType(BaseDataVariableType):
    rate: PropertyType = o6.hasProperty(PropertyType(nodeId="i=17278", browseName="Rate", modellingRule="Mandatory", dataType=o6.UInt16, valueRank=-1))


@o6.variabletype(nodeId="i=16309", browseName="SelectionListType", displayName="SelectionListType", valueRank=o6.ValueRank.SCALAR)
class SelectionListType(BaseDataVariableType):
    restrictToList: PropertyType | None = o6.hasProperty(PropertyType(nodeId="i=16312", browseName="RestrictToList", modellingRule="Optional", dataType=o6.Boolean, valueRank=-1))
    selectionDescriptions: PropertyType | None = o6.hasProperty(
        PropertyType(nodeId="i=17633", browseName="SelectionDescriptions", modellingRule="Optional", dataType=o6.LocalizedText, valueRank=1, arrayDimensions=[0])
    )
    selections: PropertyType = o6.hasProperty(PropertyType(nodeId="i=17632", browseName="Selections", modellingRule="Mandatory", valueRank=1, arrayDimensions=[0]))


@o6.variabletype(nodeId="i=17709", browseName="RationalNumberType", displayName="RationalNumberType", dataType=ns0_datypes.RationalNumber, valueRank=o6.ValueRank.SCALAR)
class RationalNumberType(BaseDataVariableType):
    denominator: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=17713", browseName="Denominator", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    numerator: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=17712", browseName="Numerator", modellingRule="Mandatory", dataType=o6.Int32, valueRank=-1))


@o6.variabletype(nodeId="i=17714", browseName="VectorType", displayName="VectorType", isAbstract=True, dataType=ns0_datypes.Vector, valueRank=o6.ValueRank.SCALAR)
class VectorType(BaseDataVariableType):
    vectorUnit: PropertyType | None = o6.hasProperty(
        PropertyType(nodeId="i=17715", browseName="VectorUnit", modellingRule="Optional", dataType=ns0_datypes.EUInformation, valueRank=-1)
    )


@o6.variabletype(nodeId="i=17986", browseName="AudioVariableType", displayName="AudioVariableType", dataType=ns0_datypes.AudioDataType, valueRank=o6.ValueRank.SCALAR)
class AudioVariableType(BaseDataVariableType):
    agencyId: PropertyType | None = o6.hasProperty(PropertyType(nodeId="i=17989", browseName="AgencyId", modellingRule="Optional", dataType=o6.String, valueRank=-1))
    listId: PropertyType | None = o6.hasProperty(PropertyType(nodeId="i=17988", browseName="ListId", modellingRule="Optional", dataType=o6.String, valueRank=-1))
    versionId: PropertyType | None = o6.hasProperty(PropertyType(nodeId="i=17990", browseName="VersionId", modellingRule="Optional", dataType=o6.String, valueRank=-1))


@o6.variabletype(nodeId="i=17716", browseName="3DVectorType", displayName="3DVectorType", dataType=ns0_datypes.ThreeDVector, valueRank=o6.ValueRank.SCALAR)
class ThreeDVectorType(VectorType):
    x: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=18769", browseName="X", modellingRule="Mandatory", dataType=o6.Double, valueRank=-1))
    y: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=18770", browseName="Y", modellingRule="Mandatory", dataType=o6.Double, valueRank=-1))
    z: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=18771", browseName="Z", modellingRule="Mandatory", dataType=o6.Double, valueRank=-1))


@o6.variabletype(
    nodeId="i=18772",
    browseName="CartesianCoordinatesType",
    displayName="CartesianCoordinatesType",
    isAbstract=True,
    dataType=ns0_datypes.CartesianCoordinates,
    valueRank=o6.ValueRank.SCALAR,
)
class CartesianCoordinatesType(BaseDataVariableType):
    lengthUnit: PropertyType | None = o6.hasProperty(
        PropertyType(nodeId="i=18773", browseName="LengthUnit", modellingRule="Optional", dataType=ns0_datypes.EUInformation, valueRank=-1)
    )


@o6.variabletype(
    nodeId="i=18774",
    browseName="3DCartesianCoordinatesType",
    displayName="3DCartesianCoordinatesType",
    dataType=ns0_datypes.ThreeDCartesianCoordinates,
    valueRank=o6.ValueRank.SCALAR,
)
class ThreeDCartesianCoordinatesType(CartesianCoordinatesType):
    x: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=18776", browseName="X", modellingRule="Mandatory", dataType=o6.Double, valueRank=-1))
    y: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=18777", browseName="Y", modellingRule="Mandatory", dataType=o6.Double, valueRank=-1))
    z: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=18778", browseName="Z", modellingRule="Mandatory", dataType=o6.Double, valueRank=-1))


@o6.variabletype(nodeId="i=18779", browseName="OrientationType", displayName="OrientationType", isAbstract=True, dataType=ns0_datypes.Orientation, valueRank=o6.ValueRank.SCALAR)
class OrientationType(BaseDataVariableType):
    angleUnit: PropertyType | None = o6.hasProperty(
        PropertyType(nodeId="i=18780", browseName="AngleUnit", modellingRule="Optional", dataType=ns0_datypes.EUInformation, valueRank=-1)
    )


@o6.variabletype(nodeId="i=18781", browseName="3DOrientationType", displayName="3DOrientationType", dataType=ns0_datypes.ThreeDOrientation, valueRank=o6.ValueRank.SCALAR)
class ThreeDOrientationType(OrientationType):
    a: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=18783", browseName="A", modellingRule="Mandatory", dataType=o6.Double, valueRank=-1))
    b: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=18784", browseName="B", modellingRule="Mandatory", dataType=o6.Double, valueRank=-1))
    c: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=18785", browseName="C", modellingRule="Mandatory", dataType=o6.Double, valueRank=-1))


@o6.variabletype(nodeId="i=18786", browseName="FrameType", displayName="FrameType", isAbstract=True, dataType=ns0_datypes.Frame, valueRank=o6.ValueRank.SCALAR)
class FrameType(BaseDataVariableType):
    baseFrame: BaseDataVariableType | None = o6.hasComponent(
        BaseDataVariableType(nodeId="i=18789", browseName="BaseFrame", modellingRule="Optional", dataType=o6.NodeId, valueRank=-1)
    )
    cartesianCoordinates: CartesianCoordinatesType = o6.hasComponent(
        CartesianCoordinatesType(
            nodeId="i=18801", browseName="CartesianCoordinates", modellingRule="Mandatory", _allow_abstract=True, dataType=ns0_datypes.CartesianCoordinates, valueRank=-1
        )
    )
    constant: PropertyType | None = o6.hasProperty(PropertyType(nodeId="i=18788", browseName="Constant", modellingRule="Optional", dataType=o6.Boolean, valueRank=-1))
    fixedBase: PropertyType | None = o6.hasProperty(PropertyType(nodeId="i=18790", browseName="FixedBase", modellingRule="Optional", dataType=o6.Boolean, valueRank=-1))
    orientation: OrientationType = o6.hasComponent(
        OrientationType(nodeId="i=18787", browseName="Orientation", modellingRule="Mandatory", _allow_abstract=True, dataType=ns0_datypes.Orientation, valueRank=-1)
    )


@o6.variabletype(nodeId="i=18791", browseName="3DFrameType", displayName="3DFrameType", dataType=ns0_datypes.ThreeDFrame, valueRank=o6.ValueRank.SCALAR)
class ThreeDFrameType(FrameType):
    cartesianCoordinates: ThreeDCartesianCoordinatesType
    orientation: ThreeDOrientationType


@o6.variabletype(
    nodeId="i=19077",
    browseName="MultiStateDictionaryEntryDiscreteBaseType",
    displayName="MultiStateDictionaryEntryDiscreteBaseType",
    dataType=ns0_datypes.Number,
    valueRank=o6.ValueRank.SCALAR,
)
class MultiStateDictionaryEntryDiscreteBaseType(MultiStateValueDiscreteType):
    enumDictionaryEntries: PropertyType = o6.hasProperty(
        PropertyType(nodeId="i=19082", browseName="EnumDictionaryEntries", modellingRule="Mandatory", dataType=o6.NodeId, valueRank=2, arrayDimensions=[0, 0])
    )
    valueAsDictionaryEntries: PropertyType | None = o6.hasProperty(
        PropertyType(nodeId="i=19083", browseName="ValueAsDictionaryEntries", modellingRule="Optional", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])
    )


@o6.variabletype(
    nodeId="i=19084",
    browseName="MultiStateDictionaryEntryDiscreteType",
    displayName="MultiStateDictionaryEntryDiscreteType",
    dataType=ns0_datypes.Number,
    valueRank=o6.ValueRank.SCALAR,
)
class MultiStateDictionaryEntryDiscreteType(MultiStateDictionaryEntryDiscreteBaseType):
    valueAsDictionaryEntries: PropertyType = o6.hasProperty(
        PropertyType(nodeId="i=19090", browseName="ValueAsDictionaryEntries", modellingRule="Mandatory", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])
    )


@o6.variabletype(nodeId="i=19725", browseName="PubSubDiagnosticsCounterType", displayName="PubSubDiagnosticsCounterType", dataType=o6.UInt32, valueRank=o6.ValueRank.SCALAR)
class PubSubDiagnosticsCounterType(BaseDataVariableType):
    active: PropertyType = o6.hasProperty(PropertyType(nodeId="i=19726", browseName="Active", modellingRule="Mandatory", dataType=o6.Boolean, valueRank=-1))
    classification: PropertyType = o6.hasProperty(
        PropertyType(nodeId="i=19727", browseName="Classification", modellingRule="Mandatory", dataType=ns0_datypes.PubSubDiagnosticsCounterClassification, valueRank=-1)
    )
    diagnosticsLevel: PropertyType = o6.hasProperty(
        PropertyType(nodeId="i=19728", browseName="DiagnosticsLevel", modellingRule="Mandatory", dataType=ns0_datypes.DiagnosticsLevel, valueRank=-1)
    )
    timeFirstChange: PropertyType | None = o6.hasProperty(
        PropertyType(nodeId="i=19729", browseName="TimeFirstChange", modellingRule="Optional", dataType=o6.DateTime, valueRank=-1)
    )


@o6.variabletype(nodeId="i=15318", browseName="BaseAnalogType", displayName="BaseAnalogType", dataType=ns0_datypes.Number, valueRank=o6.ValueRank.ANY)
class BaseAnalogType(DataItemType):
    eUNumberRange: PropertyType | None = o6.hasProperty(
        PropertyType(nodeId="i=23905", browseName="EUNumberRange", modellingRule="Optional", dataType=ns0_datypes.NumberRange, valueRank=-1)
    )
    eURange: PropertyType | None = o6.hasProperty(PropertyType(nodeId="i=17568", browseName="EURange", modellingRule="Optional", dataType=ns0_datypes.Range, valueRank=-1))
    engineeringUnits: PropertyType | None = o6.hasProperty(
        PropertyType(nodeId="i=17569", browseName="EngineeringUnits", modellingRule="Optional", dataType=ns0_datypes.EUInformation, valueRank=-1)
    )
    instrumentNumberRange: PropertyType | None = o6.hasProperty(
        PropertyType(nodeId="i=23904", browseName="InstrumentNumberRange", modellingRule="Optional", dataType=ns0_datypes.NumberRange, valueRank=-1)
    )
    instrumentRange: PropertyType | None = o6.hasProperty(
        PropertyType(nodeId="i=17567", browseName="InstrumentRange", modellingRule="Optional", dataType=ns0_datypes.Range, valueRank=-1)
    )


@o6.variabletype(nodeId="i=2368", browseName="AnalogItemType", displayName="AnalogItemType", dataType=ns0_datypes.Number, valueRank=o6.ValueRank.ANY)
class AnalogItemType(BaseAnalogType):
    eURange: PropertyType = o6.hasProperty(PropertyType(nodeId="i=2369", browseName="EURange", modellingRule="Mandatory", dataType=ns0_datypes.Range, valueRank=-1))


@o6.variabletype(nodeId="i=17497", browseName="AnalogUnitType", displayName="AnalogUnitType", dataType=ns0_datypes.Number, valueRank=o6.ValueRank.ANY)
class AnalogUnitType(BaseAnalogType):
    engineeringUnits: PropertyType = o6.hasProperty(
        PropertyType(nodeId="i=17502", browseName="EngineeringUnits", modellingRule="Mandatory", dataType=ns0_datypes.EUInformation, valueRank=-1)
    )


@o6.variabletype(nodeId="i=17570", browseName="AnalogUnitRangeType", displayName="AnalogUnitRangeType", dataType=ns0_datypes.Number, valueRank=o6.ValueRank.ANY)
class AnalogUnitRangeType(AnalogItemType):
    engineeringUnits: PropertyType = o6.hasProperty(
        PropertyType(nodeId="i=17575", browseName="EngineeringUnits", modellingRule="Mandatory", dataType=ns0_datypes.EUInformation, valueRank=-1)
    )


@o6.variabletype(nodeId="i=23906", browseName="AnalogNumberItemType", displayName="AnalogNumberItemType", dataType=ns0_datypes.Number, valueRank=o6.ValueRank.ANY)
class AnalogNumberItemType(AnalogItemType):
    eUNumberRange: PropertyType = o6.hasProperty(
        PropertyType(nodeId="i=23907", browseName="EUNumberRange", modellingRule="Mandatory", dataType=ns0_datypes.NumberRange, valueRank=-1)
    )


@o6.variabletype(nodeId="i=23918", browseName="AnalogNumberUnitRangeType", displayName="AnalogNumberUnitRangeType", dataType=ns0_datypes.Number, valueRank=o6.ValueRank.ANY)
class AnalogNumberUnitRangeType(AnalogUnitRangeType):
    eUNumberRange: PropertyType = o6.hasProperty(
        PropertyType(nodeId="i=23927", browseName="EUNumberRange", modellingRule="Mandatory", dataType=ns0_datypes.NumberRange, valueRank=-1)
    )


@o6.variabletype(nodeId="i=32244", browseName="AlarmStateVariableType", displayName="AlarmStateVariableType", dataType=ns0_datypes.AlarmMask, valueRank=o6.ValueRank.SCALAR)
class AlarmStateVariableType(BaseDataVariableType):
    activeCount: PropertyType = o6.hasProperty(PropertyType(nodeId="i=32247", browseName="ActiveCount", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1))
    filter: PropertyType = o6.hasProperty(PropertyType(nodeId="i=32250", browseName="Filter", modellingRule="Mandatory", dataType=ns0_datypes.ContentFilter, valueRank=-1))
    highestActiveSeverity: PropertyType = o6.hasProperty(
        PropertyType(nodeId="i=32245", browseName="HighestActiveSeverity", modellingRule="Mandatory", dataType=o6.UInt16, valueRank=-1)
    )
    highestUnackSeverity: PropertyType = o6.hasProperty(
        PropertyType(nodeId="i=32246", browseName="HighestUnackSeverity", modellingRule="Mandatory", dataType=o6.UInt16, valueRank=-1)
    )
    unacknowledgedCount: PropertyType = o6.hasProperty(
        PropertyType(nodeId="i=32248", browseName="UnacknowledgedCount", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1)
    )
    unconfirmedCount: PropertyType = o6.hasProperty(PropertyType(nodeId="i=32249", browseName="UnconfirmedCount", modellingRule="Mandatory", dataType=o6.UInt32, valueRank=-1))


@o6.variabletype(nodeId="i=32431", browseName="BitFieldType", displayName="BitFieldType", isAbstract=True, dataType=ns0_datypes.UInteger, valueRank=o6.ValueRank.SCALAR)
class BitFieldType(BaseDataVariableType):
    bitFieldsDefinitions: PropertyType = o6.hasProperty(
        PropertyType(nodeId="i=32432", browseName="BitFieldsDefinitions", modellingRule="Mandatory", dataType=ns0_datypes.BitFieldDefinition, valueRank=1, arrayDimensions=[0])
    )
    fieldName_: BaseVariableType = o6.hasComponent(
        BaseVariableType(nodeId="i=32433", browseName="<FieldName>", modellingRule="MandatoryPlaceholder", _allow_abstract=True, valueRank=-1)
    )
    optionalFieldName_: BaseVariableType | None = o6.hasComponent(
        BaseVariableType(nodeId="i=15014", browseName="<OptionalFieldName>", modellingRule="OptionalPlaceholder", _allow_abstract=True, valueRank=-1)
    )


@o6.variabletype(
    nodeId="i=32657",
    browseName="ReferenceDescriptionVariableType",
    displayName="ReferenceDescriptionVariableType",
    dataType=ns0_datypes.ReferenceDescriptionDataType,
    valueRank=o6.ValueRank.SCALAR,
)
class ReferenceDescriptionVariableType(BaseDataVariableType):
    referenceRefinement: PropertyType | None = o6.hasProperty(
        PropertyType(
            nodeId="i=32658", browseName="ReferenceRefinement", modellingRule="Optional", dataType=ns0_datypes.ReferenceListEntryDataType, valueRank=1, arrayDimensions=[0]
        )
    )


del Any, TYPE_CHECKING, uuid, o6, ns0_reftypes, ns0_datypes
