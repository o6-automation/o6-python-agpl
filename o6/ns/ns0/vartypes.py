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


@o6.variabletype(nodeId="i=69", browseName="DataTypeDescriptionType", displayName="DataTypeDescriptionType", dataType=o6.String)
class DataTypeDescriptionType(BaseDataVariableType):
    dataTypeVersion: PropertyType | None = o6.hasProperty(PropertyType(nodeId="i=104", browseName="DataTypeVersion", dataType=o6.String))
    dictionaryFragment: PropertyType | None = o6.hasProperty(PropertyType(nodeId="i=105", browseName="DictionaryFragment", dataType=o6.ByteString))


@o6.variabletype(nodeId="i=2137", browseName="ServerVendorCapabilityType", displayName="ServerVendorCapabilityType", isAbstract=True)
class ServerVendorCapabilityType(BaseDataVariableType):
    pass


@o6.variabletype(nodeId="i=2150", browseName="ServerDiagnosticsSummaryType", displayName="ServerDiagnosticsSummaryType", dataType=ns0_datypes.ServerDiagnosticsSummaryDataType)
class ServerDiagnosticsSummaryType(BaseDataVariableType):
    cumulatedSessionCount: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2153", browseName="CumulatedSessionCount", dataType=o6.UInt32))
    cumulatedSubscriptionCount: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2161", browseName="CumulatedSubscriptionCount", dataType=o6.UInt32))
    currentSessionCount: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2152", browseName="CurrentSessionCount", dataType=o6.UInt32))
    currentSubscriptionCount: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2160", browseName="CurrentSubscriptionCount", dataType=o6.UInt32))
    publishingIntervalCount: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2159", browseName="PublishingIntervalCount", dataType=o6.UInt32))
    rejectedRequestsCount: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2163", browseName="RejectedRequestsCount", dataType=o6.UInt32))
    rejectedSessionCount: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2155", browseName="RejectedSessionCount", dataType=o6.UInt32))
    securityRejectedRequestsCount: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2162", browseName="SecurityRejectedRequestsCount", dataType=o6.UInt32))
    securityRejectedSessionCount: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2154", browseName="SecurityRejectedSessionCount", dataType=o6.UInt32))
    serverViewCount: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2151", browseName="ServerViewCount", dataType=o6.UInt32))
    sessionAbortCount: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2157", browseName="SessionAbortCount", dataType=o6.UInt32))
    sessionTimeoutCount: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2156", browseName="SessionTimeoutCount", dataType=o6.UInt32))


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
    definition: PropertyType | None = o6.hasProperty(PropertyType(nodeId="i=2366", browseName="Definition", dataType=o6.String))
    valuePrecision: PropertyType | None = o6.hasProperty(PropertyType(nodeId="i=2367", browseName="ValuePrecision", dataType=o6.Double))


@o6.variabletype(nodeId="i=2372", browseName="DiscreteItemType", displayName="DiscreteItemType", isAbstract=True, valueRank=o6.ValueRank.ANY)
class DiscreteItemType(DataItemType):
    pass


@o6.variabletype(nodeId="i=2373", browseName="TwoStateDiscreteType", displayName="TwoStateDiscreteType", dataType=o6.Boolean, valueRank=o6.ValueRank.ANY)
class TwoStateDiscreteType(DiscreteItemType):
    falseState: PropertyType = o6.hasProperty(PropertyType(nodeId="i=2374", browseName="FalseState", dataType=o6.LocalizedText))
    trueState: PropertyType = o6.hasProperty(PropertyType(nodeId="i=2375", browseName="TrueState", dataType=o6.LocalizedText))


@o6.variabletype(nodeId="i=2376", browseName="MultiStateDiscreteType", displayName="MultiStateDiscreteType", dataType=ns0_datypes.UInteger, valueRank=o6.ValueRank.ANY)
class MultiStateDiscreteType(DiscreteItemType):
    enumStrings: PropertyType = o6.hasProperty(PropertyType(nodeId="i=2377", browseName="EnumStrings", dataType=o6.LocalizedText, valueRank=1, arrayDimensions=[0]))


@o6.variabletype(nodeId="i=2380", browseName="ProgramDiagnosticType", displayName="ProgramDiagnosticType", dataType=ns0_datypes.ProgramDiagnosticDataType)
class ProgramDiagnosticType(BaseDataVariableType):
    createClientName: PropertyType = o6.hasProperty(PropertyType(nodeId="i=2382", browseName="CreateClientName", dataType=o6.String))
    createSessionId: PropertyType = o6.hasProperty(PropertyType(nodeId="i=2381", browseName="CreateSessionId", dataType=o6.NodeId))
    invocationCreationTime: PropertyType = o6.hasProperty(PropertyType(nodeId="i=2383", browseName="InvocationCreationTime", dataType=ns0_datypes.UtcTime))
    lastMethodCall: PropertyType = o6.hasProperty(PropertyType(nodeId="i=2385", browseName="LastMethodCall", dataType=o6.String))
    lastMethodCallTime: PropertyType = o6.hasProperty(PropertyType(nodeId="i=2389", browseName="LastMethodCallTime", dataType=ns0_datypes.UtcTime))
    lastMethodInputArguments: PropertyType = o6.hasProperty(PropertyType(nodeId="i=2387", browseName="LastMethodInputArguments", valueRank=1, arrayDimensions=[0]))
    lastMethodOutputArguments: PropertyType = o6.hasProperty(PropertyType(nodeId="i=2388", browseName="LastMethodOutputArguments", valueRank=1, arrayDimensions=[0]))
    lastMethodReturnStatus: PropertyType = o6.hasProperty(PropertyType(nodeId="i=2390", browseName="LastMethodReturnStatus", dataType=ns0_datypes.StatusResult))
    lastMethodSessionId: PropertyType = o6.hasProperty(PropertyType(nodeId="i=2386", browseName="LastMethodSessionId", dataType=o6.NodeId))
    lastTransitionTime: PropertyType = o6.hasProperty(PropertyType(nodeId="i=2384", browseName="LastTransitionTime", dataType=ns0_datypes.UtcTime))


@o6.variabletype(nodeId="i=2138", browseName="ServerStatusType", displayName="ServerStatusType", dataType=ns0_datypes.ServerStatusDataType)
class ServerStatusType(BaseDataVariableType):
    buildInfo: BuildInfoType
    currentTime: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2140", browseName="CurrentTime", dataType=ns0_datypes.UtcTime))
    secondsTillShutdown: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2752", browseName="SecondsTillShutdown", dataType=o6.UInt32))
    shutdownReason: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2753", browseName="ShutdownReason", dataType=o6.LocalizedText))
    startTime: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2139", browseName="StartTime", dataType=ns0_datypes.UtcTime))
    state: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2141", browseName="State", dataType=ns0_datypes.ServerState))


@o6.variabletype(nodeId="i=2755", browseName="StateVariableType", displayName="StateVariableType", dataType=o6.LocalizedText)
class StateVariableType(BaseDataVariableType):
    effectiveDisplayName: PropertyType | None = o6.hasProperty(PropertyType(nodeId="i=2759", browseName="EffectiveDisplayName", dataType=o6.LocalizedText))
    id: PropertyType = o6.hasProperty(PropertyType(nodeId="i=2756", browseName="Id"))
    name: PropertyType | None = o6.hasProperty(PropertyType(nodeId="i=2757", browseName="Name", dataType=o6.QualifiedName))
    number: PropertyType | None = o6.hasProperty(PropertyType(nodeId="i=2758", browseName="Number", dataType=o6.UInt32))


@o6.variabletype(nodeId="i=2760", browseName="FiniteStateVariableType", displayName="FiniteStateVariableType", dataType=o6.LocalizedText)
class FiniteStateVariableType(StateVariableType):
    id: PropertyType = o6.hasProperty(PropertyType(nodeId="i=2761", browseName="Id", dataType=o6.NodeId))


@o6.variabletype(nodeId="i=3051", browseName="BuildInfoType", displayName="BuildInfoType", dataType=ns0_datypes.BuildInfo)
class BuildInfoType(BaseDataVariableType):
    buildDate: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=3057", browseName="BuildDate", dataType=ns0_datypes.UtcTime))
    buildNumber: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=3056", browseName="BuildNumber", dataType=o6.String))
    manufacturerName: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=3053", browseName="ManufacturerName", dataType=o6.String))
    productName: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=3054", browseName="ProductName", dataType=o6.String))
    productUri: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=3052", browseName="ProductUri", dataType=o6.String))
    softwareVersion: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=3055", browseName="SoftwareVersion", dataType=o6.String))


@o6.variabletype(
    nodeId="i=2244", browseName="SessionSecurityDiagnosticsType", displayName="SessionSecurityDiagnosticsType", dataType=ns0_datypes.SessionSecurityDiagnosticsDataType
)
class SessionSecurityDiagnosticsType(BaseDataVariableType):
    authenticationMechanism: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2248", browseName="AuthenticationMechanism", dataType=o6.String))
    clientCertificate: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=3058", browseName="ClientCertificate", dataType=o6.ByteString))
    clientUserIdHistory: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2247", browseName="ClientUserIdHistory", dataType=o6.String, valueRank=1, arrayDimensions=[0])
    )
    clientUserIdOfSession: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2246", browseName="ClientUserIdOfSession", dataType=o6.String))
    encoding: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2249", browseName="Encoding", dataType=o6.String))
    securityMode: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2251", browseName="SecurityMode", dataType=ns0_datypes.MessageSecurityMode))
    securityPolicyUri: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2252", browseName="SecurityPolicyUri", dataType=o6.String))
    sessionId: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2245", browseName="SessionId", dataType=o6.NodeId))
    transportProtocol: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2250", browseName="TransportProtocol", dataType=o6.String))


@o6.variabletype(nodeId="i=2172", browseName="SubscriptionDiagnosticsType", displayName="SubscriptionDiagnosticsType", dataType=ns0_datypes.SubscriptionDiagnosticsDataType)
class SubscriptionDiagnosticsType(BaseDataVariableType):
    currentKeepAliveCount: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=8890", browseName="CurrentKeepAliveCount", dataType=o6.UInt32))
    currentLifetimeCount: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=8891", browseName="CurrentLifetimeCount", dataType=o6.UInt32))
    dataChangeNotificationsCount: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2191", browseName="DataChangeNotificationsCount", dataType=o6.UInt32))
    disableCount: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2183", browseName="DisableCount", dataType=o6.UInt32))
    disabledMonitoredItemCount: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=8895", browseName="DisabledMonitoredItemCount", dataType=o6.UInt32))
    discardedMessageCount: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=8893", browseName="DiscardedMessageCount", dataType=o6.UInt32))
    enableCount: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2182", browseName="EnableCount", dataType=o6.UInt32))
    eventNotificationsCount: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2998", browseName="EventNotificationsCount", dataType=o6.UInt32))
    eventQueueOverflowCount: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=8902", browseName="EventQueueOverflowCount", dataType=o6.UInt32))
    latePublishRequestCount: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=8889", browseName="LatePublishRequestCount", dataType=o6.UInt32))
    maxKeepAliveCount: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2177", browseName="MaxKeepAliveCount", dataType=o6.UInt32))
    maxLifetimeCount: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=8888", browseName="MaxLifetimeCount", dataType=o6.UInt32))
    maxNotificationsPerPublish: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2179", browseName="MaxNotificationsPerPublish", dataType=o6.UInt32))
    modifyCount: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2181", browseName="ModifyCount", dataType=o6.UInt32))
    monitoredItemCount: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=8894", browseName="MonitoredItemCount", dataType=o6.UInt32))
    monitoringQueueOverflowCount: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=8896", browseName="MonitoringQueueOverflowCount", dataType=o6.UInt32))
    nextSequenceNumber: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=8897", browseName="NextSequenceNumber", dataType=o6.UInt32))
    notificationsCount: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2193", browseName="NotificationsCount", dataType=o6.UInt32))
    priority: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2175", browseName="Priority", dataType=o6.Byte))
    publishRequestCount: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2190", browseName="PublishRequestCount", dataType=o6.UInt32))
    publishingEnabled: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2180", browseName="PublishingEnabled", dataType=o6.Boolean))
    publishingInterval: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2176", browseName="PublishingInterval", dataType=ns0_datypes.Duration))
    republishMessageCount: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2186", browseName="RepublishMessageCount", dataType=o6.UInt32))
    republishMessageRequestCount: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2185", browseName="RepublishMessageRequestCount", dataType=o6.UInt32))
    republishRequestCount: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2184", browseName="RepublishRequestCount", dataType=o6.UInt32))
    sessionId: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2173", browseName="SessionId", dataType=o6.NodeId))
    subscriptionId: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2174", browseName="SubscriptionId", dataType=o6.UInt32))
    transferRequestCount: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2187", browseName="TransferRequestCount", dataType=o6.UInt32))
    transferredToAltClientCount: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2188", browseName="TransferredToAltClientCount", dataType=o6.UInt32))
    transferredToSameClientCount: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2189", browseName="TransferredToSameClientCount", dataType=o6.UInt32))
    unacknowledgedMessageCount: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=8892", browseName="UnacknowledgedMessageCount", dataType=o6.UInt32))


@o6.variabletype(nodeId="i=9002", browseName="ConditionVariableType", displayName="ConditionVariableType", valueRank=o6.ValueRank.ANY)
class ConditionVariableType(BaseDataVariableType):
    sourceTimestamp: PropertyType = o6.hasProperty(PropertyType(nodeId="i=9003", browseName="SourceTimestamp", dataType=ns0_datypes.UtcTime))


@o6.variabletype(nodeId="i=8995", browseName="TwoStateVariableType", displayName="TwoStateVariableType", dataType=o6.LocalizedText)
class TwoStateVariableType(StateVariableType):
    effectiveTransitionTime: PropertyType | None = o6.hasProperty(PropertyType(nodeId="i=9001", browseName="EffectiveTransitionTime", dataType=ns0_datypes.UtcTime))
    falseState: PropertyType | None = o6.hasProperty(PropertyType(nodeId="i=11111", browseName="FalseState", dataType=o6.LocalizedText))
    id: PropertyType = o6.hasProperty(PropertyType(nodeId="i=8996", browseName="Id", dataType=o6.Boolean))
    transitionTime: PropertyType | None = o6.hasProperty(PropertyType(nodeId="i=9000", browseName="TransitionTime", dataType=ns0_datypes.UtcTime))
    trueState: PropertyType | None = o6.hasProperty(PropertyType(nodeId="i=11110", browseName="TrueState", dataType=o6.LocalizedText))


@o6.variabletype(nodeId="i=2762", browseName="TransitionVariableType", displayName="TransitionVariableType", dataType=o6.LocalizedText)
class TransitionVariableType(BaseDataVariableType):
    effectiveTransitionTime: PropertyType | None = o6.hasProperty(PropertyType(nodeId="i=11456", browseName="EffectiveTransitionTime", dataType=ns0_datypes.UtcTime))
    id: PropertyType = o6.hasProperty(PropertyType(nodeId="i=2763", browseName="Id"))
    name: PropertyType | None = o6.hasProperty(PropertyType(nodeId="i=2764", browseName="Name", dataType=o6.QualifiedName))
    number: PropertyType | None = o6.hasProperty(PropertyType(nodeId="i=2765", browseName="Number", dataType=o6.UInt32))
    transitionTime: PropertyType | None = o6.hasProperty(PropertyType(nodeId="i=2766", browseName="TransitionTime", dataType=ns0_datypes.UtcTime))


@o6.variabletype(nodeId="i=2767", browseName="FiniteTransitionVariableType", displayName="FiniteTransitionVariableType", dataType=o6.LocalizedText)
class FiniteTransitionVariableType(TransitionVariableType):
    id: PropertyType = o6.hasProperty(PropertyType(nodeId="i=2768", browseName="Id", dataType=o6.NodeId))


@o6.variabletype(nodeId="i=11238", browseName="MultiStateValueDiscreteType", displayName="MultiStateValueDiscreteType", dataType=ns0_datypes.Number, valueRank=o6.ValueRank.ANY)
class MultiStateValueDiscreteType(DiscreteItemType):
    enumValues: PropertyType = o6.hasProperty(PropertyType(nodeId="i=11241", browseName="EnumValues", dataType=ns0_datypes.EnumValueType, valueRank=1, arrayDimensions=[0]))
    valueAsText: PropertyType = o6.hasProperty(PropertyType(nodeId="i=11461", browseName="ValueAsText", dataType=o6.LocalizedText))


@o6.variabletype(
    nodeId="i=2165", browseName="SamplingIntervalDiagnosticsType", displayName="SamplingIntervalDiagnosticsType", dataType=ns0_datypes.SamplingIntervalDiagnosticsDataType
)
class SamplingIntervalDiagnosticsType(BaseDataVariableType):
    disabledMonitoredItemsSamplingCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=11699", browseName="DisabledMonitoredItemsSamplingCount", dataType=o6.UInt32)
    )
    maxSampledMonitoredItemsCount: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=11698", browseName="MaxSampledMonitoredItemsCount", dataType=o6.UInt32))
    sampledMonitoredItemsCount: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=11697", browseName="SampledMonitoredItemsCount", dataType=o6.UInt32))
    samplingInterval: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2166", browseName="SamplingInterval", dataType=ns0_datypes.Duration))


@o6.variabletype(nodeId="i=11487", browseName="OptionSetType", displayName="OptionSetType")
class OptionSetType(BaseDataVariableType):
    bitMask: PropertyType | None = o6.hasProperty(PropertyType(nodeId="i=11701", browseName="BitMask", dataType=o6.Boolean, valueRank=1, arrayDimensions=[0]))
    optionSetValues: PropertyType = o6.hasProperty(PropertyType(nodeId="i=11488", browseName="OptionSetValues", dataType=o6.LocalizedText, valueRank=1, arrayDimensions=[0]))


@o6.variabletype(nodeId="i=2197", browseName="SessionDiagnosticsVariableType", displayName="SessionDiagnosticsVariableType", dataType=ns0_datypes.SessionDiagnosticsDataType)
class SessionDiagnosticsVariableType(BaseDataVariableType):
    actualSessionTimeout: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2204", browseName="ActualSessionTimeout", dataType=ns0_datypes.Duration))
    addNodesCount: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2234", browseName="AddNodesCount", dataType=ns0_datypes.ServiceCounterDataType))
    addReferencesCount: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2235", browseName="AddReferencesCount", dataType=ns0_datypes.ServiceCounterDataType))
    browseCount: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2238", browseName="BrowseCount", dataType=ns0_datypes.ServiceCounterDataType))
    browseNextCount: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2239", browseName="BrowseNextCount", dataType=ns0_datypes.ServiceCounterDataType))
    callCount: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2221", browseName="CallCount", dataType=ns0_datypes.ServiceCounterDataType))
    clientConnectionTime: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2205", browseName="ClientConnectionTime", dataType=ns0_datypes.UtcTime))
    clientDescription: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2200", browseName="ClientDescription", dataType=ns0_datypes.ApplicationDescription))
    clientLastContactTime: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2206", browseName="ClientLastContactTime", dataType=ns0_datypes.UtcTime))
    createMonitoredItemsCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2222", browseName="CreateMonitoredItemsCount", dataType=ns0_datypes.ServiceCounterDataType)
    )
    createSubscriptionCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2227", browseName="CreateSubscriptionCount", dataType=ns0_datypes.ServiceCounterDataType)
    )
    currentMonitoredItemsCount: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2208", browseName="CurrentMonitoredItemsCount", dataType=o6.UInt32))
    currentPublishRequestsInQueue: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2209", browseName="CurrentPublishRequestsInQueue", dataType=o6.UInt32))
    currentSubscriptionsCount: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2207", browseName="CurrentSubscriptionsCount", dataType=o6.UInt32))
    deleteMonitoredItemsCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2226", browseName="DeleteMonitoredItemsCount", dataType=ns0_datypes.ServiceCounterDataType)
    )
    deleteNodesCount: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2236", browseName="DeleteNodesCount", dataType=ns0_datypes.ServiceCounterDataType))
    deleteReferencesCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2237", browseName="DeleteReferencesCount", dataType=ns0_datypes.ServiceCounterDataType)
    )
    deleteSubscriptionsCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2233", browseName="DeleteSubscriptionsCount", dataType=ns0_datypes.ServiceCounterDataType)
    )
    endpointUrl: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2202", browseName="EndpointUrl", dataType=o6.String))
    historyReadCount: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2218", browseName="HistoryReadCount", dataType=ns0_datypes.ServiceCounterDataType))
    historyUpdateCount: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2220", browseName="HistoryUpdateCount", dataType=ns0_datypes.ServiceCounterDataType))
    localeIds: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2203", browseName="LocaleIds", dataType=ns0_datypes.LocaleId, valueRank=1, arrayDimensions=[0])
    )
    maxResponseMessageSize: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=3050", browseName="MaxResponseMessageSize", dataType=o6.UInt32))
    modifyMonitoredItemsCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2223", browseName="ModifyMonitoredItemsCount", dataType=ns0_datypes.ServiceCounterDataType)
    )
    modifySubscriptionCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2228", browseName="ModifySubscriptionCount", dataType=ns0_datypes.ServiceCounterDataType)
    )
    publishCount: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2230", browseName="PublishCount", dataType=ns0_datypes.ServiceCounterDataType))
    queryFirstCount: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2241", browseName="QueryFirstCount", dataType=ns0_datypes.ServiceCounterDataType))
    queryNextCount: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2242", browseName="QueryNextCount", dataType=ns0_datypes.ServiceCounterDataType))
    readCount: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2217", browseName="ReadCount", dataType=ns0_datypes.ServiceCounterDataType))
    registerNodesCount: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2730", browseName="RegisterNodesCount", dataType=ns0_datypes.ServiceCounterDataType))
    republishCount: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2231", browseName="RepublishCount", dataType=ns0_datypes.ServiceCounterDataType))
    serverUri: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2201", browseName="ServerUri", dataType=o6.String))
    sessionId: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2198", browseName="SessionId", dataType=o6.NodeId))
    sessionName: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2199", browseName="SessionName", dataType=o6.String))
    setMonitoringModeCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2224", browseName="SetMonitoringModeCount", dataType=ns0_datypes.ServiceCounterDataType)
    )
    setPublishingModeCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2229", browseName="SetPublishingModeCount", dataType=ns0_datypes.ServiceCounterDataType)
    )
    setTriggeringCount: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2225", browseName="SetTriggeringCount", dataType=ns0_datypes.ServiceCounterDataType))
    totalRequestCount: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=8900", browseName="TotalRequestCount", dataType=ns0_datypes.ServiceCounterDataType))
    transferSubscriptionsCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2232", browseName="TransferSubscriptionsCount", dataType=ns0_datypes.ServiceCounterDataType)
    )
    translateBrowsePathsToNodeIdsCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2240", browseName="TranslateBrowsePathsToNodeIdsCount", dataType=ns0_datypes.ServiceCounterDataType)
    )
    unauthorizedRequestCount: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=11892", browseName="UnauthorizedRequestCount", dataType=o6.UInt32))
    unregisterNodesCount: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=2731", browseName="UnregisterNodesCount", dataType=ns0_datypes.ServiceCounterDataType)
    )
    writeCount: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=2219", browseName="WriteCount", dataType=ns0_datypes.ServiceCounterDataType))


@o6.variabletype(nodeId="i=12021", browseName="ArrayItemType", displayName="ArrayItemType", isAbstract=True, valueRank=o6.ValueRank.ARRAY_ANY)
class ArrayItemType(DataItemType):
    axisScaleType: PropertyType = o6.hasProperty(PropertyType(nodeId="i=12028", browseName="AxisScaleType", dataType=ns0_datypes.AxisScaleEnumeration))
    eURange: PropertyType = o6.hasProperty(PropertyType(nodeId="i=12025", browseName="EURange", dataType=ns0_datypes.Range))
    engineeringUnits: PropertyType = o6.hasProperty(PropertyType(nodeId="i=12026", browseName="EngineeringUnits", dataType=ns0_datypes.EUInformation))
    instrumentRange: PropertyType | None = o6.hasProperty(PropertyType(nodeId="i=12024", browseName="InstrumentRange", dataType=ns0_datypes.Range))
    title: PropertyType = o6.hasProperty(PropertyType(nodeId="i=12027", browseName="Title", dataType=o6.LocalizedText))


@o6.variabletype(nodeId="i=12029", browseName="YArrayItemType", displayName="YArrayItemType", valueRank=o6.ValueRank.ARRAY_1D, arrayDimensions=[0])
class YArrayItemType(ArrayItemType):
    xAxisDefinition: PropertyType = o6.hasProperty(PropertyType(nodeId="i=12037", browseName="XAxisDefinition", dataType=ns0_datypes.AxisInformation))


@o6.variabletype(nodeId="i=12038", browseName="XYArrayItemType", displayName="XYArrayItemType", dataType=ns0_datypes.XVType, valueRank=o6.ValueRank.ARRAY_1D, arrayDimensions=[0])
class XYArrayItemType(ArrayItemType):
    xAxisDefinition: PropertyType = o6.hasProperty(PropertyType(nodeId="i=12046", browseName="XAxisDefinition", dataType=ns0_datypes.AxisInformation))


@o6.variabletype(nodeId="i=12047", browseName="ImageItemType", displayName="ImageItemType", valueRank=o6.ValueRank.ARRAY_2D, arrayDimensions=[0, 0])
class ImageItemType(ArrayItemType):
    xAxisDefinition: PropertyType = o6.hasProperty(PropertyType(nodeId="i=12055", browseName="XAxisDefinition", dataType=ns0_datypes.AxisInformation))
    yAxisDefinition: PropertyType = o6.hasProperty(PropertyType(nodeId="i=12056", browseName="YAxisDefinition", dataType=ns0_datypes.AxisInformation))


@o6.variabletype(nodeId="i=12057", browseName="CubeItemType", displayName="CubeItemType", valueRank=3, arrayDimensions=[0, 0, 0])
class CubeItemType(ArrayItemType):
    xAxisDefinition: PropertyType = o6.hasProperty(PropertyType(nodeId="i=12065", browseName="XAxisDefinition", dataType=ns0_datypes.AxisInformation))
    yAxisDefinition: PropertyType = o6.hasProperty(PropertyType(nodeId="i=12066", browseName="YAxisDefinition", dataType=ns0_datypes.AxisInformation))
    zAxisDefinition: PropertyType = o6.hasProperty(PropertyType(nodeId="i=12067", browseName="ZAxisDefinition", dataType=ns0_datypes.AxisInformation))


@o6.variabletype(nodeId="i=12068", browseName="NDimensionArrayItemType", displayName="NDimensionArrayItemType", valueRank=o6.ValueRank.ARRAY_ANY)
class NDimensionArrayItemType(ArrayItemType):
    axisDefinition: PropertyType = o6.hasProperty(
        PropertyType(nodeId="i=12076", browseName="AxisDefinition", dataType=ns0_datypes.AxisInformation, valueRank=1, arrayDimensions=[0])
    )


@o6.variabletype(nodeId="i=72", browseName="DataTypeDictionaryType", displayName="DataTypeDictionaryType", dataType=o6.ByteString)
class DataTypeDictionaryType(BaseDataVariableType):
    dataTypeVersion: PropertyType | None = o6.hasProperty(PropertyType(nodeId="i=106", browseName="DataTypeVersion", dataType=o6.String))
    deprecated: PropertyType | None = o6.hasProperty(PropertyType(nodeId="i=15001", browseName="Deprecated", dataType=o6.Boolean))
    namespaceUri: PropertyType | None = o6.hasProperty(PropertyType(nodeId="i=107", browseName="NamespaceUri", dataType=o6.String))


@o6.variabletype(nodeId="i=15113", browseName="GuardVariableType", displayName="GuardVariableType", dataType=o6.LocalizedText)
class GuardVariableType(BaseDataVariableType):
    pass


@o6.variabletype(nodeId="i=15128", browseName="ExpressionGuardVariableType", displayName="ExpressionGuardVariableType", dataType=o6.LocalizedText)
class ExpressionGuardVariableType(GuardVariableType):
    expression: PropertyType = o6.hasProperty(PropertyType(nodeId="i=15129", browseName="Expression", dataType=ns0_datypes.ContentFilter))


@o6.variabletype(nodeId="i=15317", browseName="ElseGuardVariableType", displayName="ElseGuardVariableType", dataType=o6.LocalizedText)
class ElseGuardVariableType(GuardVariableType):
    pass


@o6.variabletype(nodeId="i=15383", browseName="ProgramDiagnostic2Type", displayName="ProgramDiagnostic2Type", dataType=ns0_datypes.ProgramDiagnostic2DataType)
class ProgramDiagnostic2Type(BaseDataVariableType):
    createClientName: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=15385", browseName="CreateClientName", dataType=o6.String))
    createSessionId: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=15384", browseName="CreateSessionId", dataType=o6.NodeId))
    invocationCreationTime: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=15386", browseName="InvocationCreationTime", dataType=ns0_datypes.UtcTime))
    lastMethodCall: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=15388", browseName="LastMethodCall", dataType=o6.String))
    lastMethodCallTime: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=15394", browseName="LastMethodCallTime", dataType=ns0_datypes.UtcTime))
    lastMethodInputArguments: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=15390", browseName="LastMethodInputArguments", dataType=ns0_datypes.Argument, valueRank=1, arrayDimensions=[0])
    )
    lastMethodInputValues: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=15392", browseName="LastMethodInputValues", valueRank=1, arrayDimensions=[0]))
    lastMethodOutputArguments: BaseDataVariableType = o6.hasComponent(
        BaseDataVariableType(nodeId="i=15391", browseName="LastMethodOutputArguments", dataType=ns0_datypes.Argument, valueRank=1, arrayDimensions=[0])
    )
    lastMethodOutputValues: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=15393", browseName="LastMethodOutputValues", valueRank=1, arrayDimensions=[0]))
    lastMethodReturnStatus: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=15395", browseName="LastMethodReturnStatus", dataType=o6.StatusCode))
    lastMethodSessionId: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=15389", browseName="LastMethodSessionId", dataType=o6.NodeId))
    lastTransitionTime: PropertyType = o6.hasProperty(PropertyType(nodeId="i=15387", browseName="LastTransitionTime", dataType=ns0_datypes.UtcTime))


@o6.variabletype(nodeId="i=17277", browseName="AlarmRateVariableType", displayName="AlarmRateVariableType", dataType=o6.Double)
class AlarmRateVariableType(BaseDataVariableType):
    rate: PropertyType = o6.hasProperty(PropertyType(nodeId="i=17278", browseName="Rate", dataType=o6.UInt16))


@o6.variabletype(nodeId="i=16309", browseName="SelectionListType", displayName="SelectionListType")
class SelectionListType(BaseDataVariableType):
    restrictToList: PropertyType | None = o6.hasProperty(PropertyType(nodeId="i=16312", browseName="RestrictToList", dataType=o6.Boolean))
    selectionDescriptions: PropertyType | None = o6.hasProperty(
        PropertyType(nodeId="i=17633", browseName="SelectionDescriptions", dataType=o6.LocalizedText, valueRank=1, arrayDimensions=[0])
    )
    selections: PropertyType = o6.hasProperty(PropertyType(nodeId="i=17632", browseName="Selections", valueRank=1, arrayDimensions=[0]))


@o6.variabletype(nodeId="i=17709", browseName="RationalNumberType", displayName="RationalNumberType", dataType=ns0_datypes.RationalNumber)
class RationalNumberType(BaseDataVariableType):
    denominator: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=17713", browseName="Denominator", dataType=o6.UInt32))
    numerator: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=17712", browseName="Numerator", dataType=o6.Int32))


@o6.variabletype(nodeId="i=17714", browseName="VectorType", displayName="VectorType", isAbstract=True, dataType=ns0_datypes.Vector)
class VectorType(BaseDataVariableType):
    vectorUnit: PropertyType | None = o6.hasProperty(PropertyType(nodeId="i=17715", browseName="VectorUnit", dataType=ns0_datypes.EUInformation))


@o6.variabletype(nodeId="i=17986", browseName="AudioVariableType", displayName="AudioVariableType", dataType=ns0_datypes.AudioDataType)
class AudioVariableType(BaseDataVariableType):
    agencyId: PropertyType | None = o6.hasProperty(PropertyType(nodeId="i=17989", browseName="AgencyId", dataType=o6.String))
    listId: PropertyType | None = o6.hasProperty(PropertyType(nodeId="i=17988", browseName="ListId", dataType=o6.String))
    versionId: PropertyType | None = o6.hasProperty(PropertyType(nodeId="i=17990", browseName="VersionId", dataType=o6.String))


@o6.variabletype(nodeId="i=17716", browseName="3DVectorType", displayName="3DVectorType", dataType=ns0_datypes._3DVector)
class _3DVectorType(VectorType):
    x: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=18769", browseName="X", dataType=o6.Double))
    y: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=18770", browseName="Y", dataType=o6.Double))
    z: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=18771", browseName="Z", dataType=o6.Double))


@o6.variabletype(nodeId="i=18772", browseName="CartesianCoordinatesType", displayName="CartesianCoordinatesType", isAbstract=True, dataType=ns0_datypes.CartesianCoordinates)
class CartesianCoordinatesType(BaseDataVariableType):
    lengthUnit: PropertyType | None = o6.hasProperty(PropertyType(nodeId="i=18773", browseName="LengthUnit", dataType=ns0_datypes.EUInformation))


@o6.variabletype(nodeId="i=18774", browseName="3DCartesianCoordinatesType", displayName="3DCartesianCoordinatesType", dataType=ns0_datypes._3DCartesianCoordinates)
class _3DCartesianCoordinatesType(CartesianCoordinatesType):
    x: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=18776", browseName="X", dataType=o6.Double))
    y: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=18777", browseName="Y", dataType=o6.Double))
    z: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=18778", browseName="Z", dataType=o6.Double))


@o6.variabletype(nodeId="i=18779", browseName="OrientationType", displayName="OrientationType", isAbstract=True, dataType=ns0_datypes.Orientation)
class OrientationType(BaseDataVariableType):
    angleUnit: PropertyType | None = o6.hasProperty(PropertyType(nodeId="i=18780", browseName="AngleUnit", dataType=ns0_datypes.EUInformation))


@o6.variabletype(nodeId="i=18781", browseName="3DOrientationType", displayName="3DOrientationType", dataType=ns0_datypes._3DOrientation)
class _3DOrientationType(OrientationType):
    a: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=18783", browseName="A", dataType=o6.Double))
    b: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=18784", browseName="B", dataType=o6.Double))
    c: BaseDataVariableType = o6.hasComponent(BaseDataVariableType(nodeId="i=18785", browseName="C", dataType=o6.Double))


@o6.variabletype(nodeId="i=18786", browseName="FrameType", displayName="FrameType", isAbstract=True, dataType=ns0_datypes.Frame)
class FrameType(BaseDataVariableType):
    baseFrame: BaseDataVariableType | None = o6.hasComponent(BaseDataVariableType(nodeId="i=18789", browseName="BaseFrame", dataType=o6.NodeId))
    cartesianCoordinates: CartesianCoordinatesType = o6.hasComponent(
        CartesianCoordinatesType(nodeId="i=18801", browseName="CartesianCoordinates", _allow_abstract=True, dataType=ns0_datypes.CartesianCoordinates)
    )
    constant: PropertyType | None = o6.hasProperty(PropertyType(nodeId="i=18788", browseName="Constant", dataType=o6.Boolean))
    fixedBase: PropertyType | None = o6.hasProperty(PropertyType(nodeId="i=18790", browseName="FixedBase", dataType=o6.Boolean))
    orientation: OrientationType = o6.hasComponent(OrientationType(nodeId="i=18787", browseName="Orientation", _allow_abstract=True, dataType=ns0_datypes.Orientation))


@o6.variabletype(nodeId="i=18791", browseName="3DFrameType", displayName="3DFrameType", dataType=ns0_datypes._3DFrame)
class _3DFrameType(FrameType):
    cartesianCoordinates: _3DCartesianCoordinatesType
    orientation: _3DOrientationType


@o6.variabletype(nodeId="i=19077", browseName="MultiStateDictionaryEntryDiscreteBaseType", displayName="MultiStateDictionaryEntryDiscreteBaseType", dataType=ns0_datypes.Number)
class MultiStateDictionaryEntryDiscreteBaseType(MultiStateValueDiscreteType):
    enumDictionaryEntries: PropertyType = o6.hasProperty(
        PropertyType(nodeId="i=19082", browseName="EnumDictionaryEntries", dataType=o6.NodeId, valueRank=2, arrayDimensions=[0, 0])
    )
    valueAsDictionaryEntries: PropertyType | None = o6.hasProperty(
        PropertyType(nodeId="i=19083", browseName="ValueAsDictionaryEntries", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])
    )


@o6.variabletype(nodeId="i=19084", browseName="MultiStateDictionaryEntryDiscreteType", displayName="MultiStateDictionaryEntryDiscreteType", dataType=ns0_datypes.Number)
class MultiStateDictionaryEntryDiscreteType(MultiStateDictionaryEntryDiscreteBaseType):
    valueAsDictionaryEntries: PropertyType = o6.hasProperty(
        PropertyType(nodeId="i=19090", browseName="ValueAsDictionaryEntries", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])
    )


@o6.variabletype(nodeId="i=19725", browseName="PubSubDiagnosticsCounterType", displayName="PubSubDiagnosticsCounterType", dataType=o6.UInt32)
class PubSubDiagnosticsCounterType(BaseDataVariableType):
    active: PropertyType = o6.hasProperty(PropertyType(nodeId="i=19726", browseName="Active", dataType=o6.Boolean))
    classification: PropertyType = o6.hasProperty(PropertyType(nodeId="i=19727", browseName="Classification", dataType=ns0_datypes.PubSubDiagnosticsCounterClassification))
    diagnosticsLevel: PropertyType = o6.hasProperty(PropertyType(nodeId="i=19728", browseName="DiagnosticsLevel", dataType=ns0_datypes.DiagnosticsLevel))
    timeFirstChange: PropertyType | None = o6.hasProperty(PropertyType(nodeId="i=19729", browseName="TimeFirstChange", dataType=o6.DateTime))


@o6.variabletype(nodeId="i=15318", browseName="BaseAnalogType", displayName="BaseAnalogType", dataType=ns0_datypes.Number, valueRank=o6.ValueRank.ANY)
class BaseAnalogType(DataItemType):
    eUNumberRange: PropertyType | None = o6.hasProperty(PropertyType(nodeId="i=23905", browseName="EUNumberRange", dataType=ns0_datypes.NumberRange))
    eURange: PropertyType | None = o6.hasProperty(PropertyType(nodeId="i=17568", browseName="EURange", dataType=ns0_datypes.Range))
    engineeringUnits: PropertyType | None = o6.hasProperty(PropertyType(nodeId="i=17569", browseName="EngineeringUnits", dataType=ns0_datypes.EUInformation))
    instrumentNumberRange: PropertyType | None = o6.hasProperty(PropertyType(nodeId="i=23904", browseName="InstrumentNumberRange", dataType=ns0_datypes.NumberRange))
    instrumentRange: PropertyType | None = o6.hasProperty(PropertyType(nodeId="i=17567", browseName="InstrumentRange", dataType=ns0_datypes.Range))


@o6.variabletype(nodeId="i=2368", browseName="AnalogItemType", displayName="AnalogItemType", dataType=ns0_datypes.Number, valueRank=o6.ValueRank.ANY)
class AnalogItemType(BaseAnalogType):
    eURange: PropertyType = o6.hasProperty(PropertyType(nodeId="i=2369", browseName="EURange", dataType=ns0_datypes.Range))


@o6.variabletype(nodeId="i=17497", browseName="AnalogUnitType", displayName="AnalogUnitType", dataType=ns0_datypes.Number, valueRank=o6.ValueRank.ANY)
class AnalogUnitType(BaseAnalogType):
    engineeringUnits: PropertyType = o6.hasProperty(PropertyType(nodeId="i=17502", browseName="EngineeringUnits", dataType=ns0_datypes.EUInformation))


@o6.variabletype(nodeId="i=17570", browseName="AnalogUnitRangeType", displayName="AnalogUnitRangeType", dataType=ns0_datypes.Number, valueRank=o6.ValueRank.ANY)
class AnalogUnitRangeType(AnalogItemType):
    engineeringUnits: PropertyType = o6.hasProperty(PropertyType(nodeId="i=17575", browseName="EngineeringUnits", dataType=ns0_datypes.EUInformation))


@o6.variabletype(nodeId="i=23906", browseName="AnalogNumberItemType", displayName="AnalogNumberItemType", dataType=ns0_datypes.Number, valueRank=o6.ValueRank.ANY)
class AnalogNumberItemType(AnalogItemType):
    eUNumberRange: PropertyType = o6.hasProperty(PropertyType(nodeId="i=23907", browseName="EUNumberRange", dataType=ns0_datypes.NumberRange))


@o6.variabletype(nodeId="i=23918", browseName="AnalogNumberUnitRangeType", displayName="AnalogNumberUnitRangeType", dataType=ns0_datypes.Number, valueRank=o6.ValueRank.ANY)
class AnalogNumberUnitRangeType(AnalogUnitRangeType):
    eUNumberRange: PropertyType = o6.hasProperty(PropertyType(nodeId="i=23927", browseName="EUNumberRange", dataType=ns0_datypes.NumberRange))


@o6.variabletype(nodeId="i=32244", browseName="AlarmStateVariableType", displayName="AlarmStateVariableType", dataType=ns0_datypes.AlarmMask)
class AlarmStateVariableType(BaseDataVariableType):
    activeCount: PropertyType = o6.hasProperty(PropertyType(nodeId="i=32247", browseName="ActiveCount", dataType=o6.UInt32))
    filter: PropertyType = o6.hasProperty(PropertyType(nodeId="i=32250", browseName="Filter", dataType=ns0_datypes.ContentFilter))
    highestActiveSeverity: PropertyType = o6.hasProperty(PropertyType(nodeId="i=32245", browseName="HighestActiveSeverity", dataType=o6.UInt16))
    highestUnackSeverity: PropertyType = o6.hasProperty(PropertyType(nodeId="i=32246", browseName="HighestUnackSeverity", dataType=o6.UInt16))
    unacknowledgedCount: PropertyType = o6.hasProperty(PropertyType(nodeId="i=32248", browseName="UnacknowledgedCount", dataType=o6.UInt32))
    unconfirmedCount: PropertyType = o6.hasProperty(PropertyType(nodeId="i=32249", browseName="UnconfirmedCount", dataType=o6.UInt32))


@o6.variabletype(nodeId="i=32431", browseName="BitFieldType", displayName="BitFieldType", isAbstract=True, dataType=ns0_datypes.UInteger)
class BitFieldType(BaseDataVariableType):
    bitFieldsDefinitions: PropertyType = o6.hasProperty(
        PropertyType(nodeId="i=32432", browseName="BitFieldsDefinitions", dataType=ns0_datypes.BitFieldDefinition, valueRank=1, arrayDimensions=[0])
    )
    langleFieldNameRangle: BaseVariableType = o6.hasComponent(
        BaseVariableType(nodeId="i=32433", browseName="<FieldName>", modellingRule="MandatoryPlaceholder", _allow_abstract=True)
    )
    langleOptionalFieldNameRangle: BaseVariableType | None = o6.hasComponent(
        BaseVariableType(nodeId="i=15014", browseName="<OptionalFieldName>", modellingRule="OptionalPlaceholder", _allow_abstract=True)
    )


@o6.variabletype(nodeId="i=32657", browseName="ReferenceDescriptionVariableType", displayName="ReferenceDescriptionVariableType", dataType=ns0_datypes.ReferenceDescriptionDataType)
class ReferenceDescriptionVariableType(BaseDataVariableType):
    referenceRefinement: PropertyType | None = o6.hasProperty(
        PropertyType(nodeId="i=32658", browseName="ReferenceRefinement", dataType=ns0_datypes.ReferenceListEntryDataType, valueRank=1, arrayDimensions=[0])
    )


del Any, TYPE_CHECKING, uuid, o6, ns0_reftypes, ns0_datypes
